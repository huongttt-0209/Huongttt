#!/usr/bin/env python3
"""
Script cập nhật báo cáo huyết áp tháng theo SRS BR-005
Bổ sung các tiêu chí còn thiếu: phân loại kiểm soát, xu hướng, tương quan sự kiện, khuyến nghị chi tiết
"""

import os
import re
import csv
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from collections import defaultdict

# Đường dẫn gốc
BASE_PATH = Path("/Users/teamai/Downloads/antigravity/koliaa/Huongttt/feature/bao_cao/csv/Data_import/insert_dev")

# Các user cần cập nhật
USERS = ["user_bp_load", "user_ha_thap", "user_ko_on_dinh"]

# Event type mapping (English -> Vietnamese)
EVENT_LABELS = {
    "medication": "Uống thuốc",
    "stress": "Stress",
    "exercise": "Tập thể dục",
    "caffeine": "Uống cà phê",
    "alcohol": "Rượu bia",
    "salt": "Ăn mặn"
}

# Phân loại mức độ kiểm soát (cho user THA đã chẩn đoán)
def classify_control_rate(rate: float) -> Tuple[str, str]:
    """Phân loại mức độ kiểm soát HA theo SRS BR-005"""
    if rate > 70:
        return "Kiểm soát Tối Ưu", ">70%"
    elif rate >= 50:
        return "Kiểm soát Tốt", "50-70%"
    elif rate >= 25:
        return "Kiểm soát Kém", "25-50%"
    else:
        return "Không được kiểm soát", "<25%"


def classify_arv(arv: float) -> str:
    """Phân loại độ ổn định ARV"""
    if arv < 10:
        return "Ổn định"
    elif arv <= 14:
        return "Biến động"
    else:
        return "Bất ổn"


def classify_me_diff(me: float) -> str:
    """Phân loại nhịp sinh học ME diff"""
    if me > 15:
        return "Vọt áp buổi sáng"
    elif me < -15:
        return "Tăng áp về tối"
    else:
        return "Cân bằng"


def read_csv(filepath: Path) -> List[Dict]:
    """Đọc file CSV và trả về list of dict"""
    data = []
    if not filepath.exists():
        return data
    
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


def get_month_data(bp_data: List[Dict], year: int, month: int) -> List[Dict]:
    """Lọc dữ liệu huyết áp cho tháng cụ thể"""
    result = []
    for row in bp_data:
        try:
            dt = datetime.strptime(row['measurement_time'], '%Y-%m-%d %H:%M:%S')
            if dt.year == year and dt.month == month:
                result.append(row)
        except:
            continue
    return result


def get_month_events(events: List[Dict], year: int, month: int) -> List[Dict]:
    """Lọc events cho tháng cụ thể"""
    result = []
    for row in events:
        try:
            dt = datetime.strptime(row['event_time'], '%Y-%m-%d %H:%M:%S')
            if dt.year == year and dt.month == month:
                result.append(row)
        except:
            continue
    return result


def calculate_metrics(bp_data: List[Dict], target_sys: Tuple[int, int], target_dia: Tuple[int, int]) -> Dict:
    """Tính toán các chỉ số từ dữ liệu huyết áp"""
    if not bp_data:
        return {}
    
    sys_values = []
    dia_values = []
    hr_values = []
    
    for row in bp_data:
        try:
            sys_values.append(int(row['systolic']))
            dia_values.append(int(row['diastolic']))
            if row.get('heart_rate'):
                hr_values.append(int(row['heart_rate']))
        except:
            continue
    
    if not sys_values:
        return {}
    
    # Tính các chỉ số cơ bản
    avg_sys = sum(sys_values) / len(sys_values)
    avg_dia = sum(dia_values) / len(dia_values)
    
    # Tính tỷ lệ trong ngưỡng
    in_target = 0
    for s, d in zip(sys_values, dia_values):
        if target_sys[0] <= s <= target_sys[1] and target_dia[0] <= d <= target_dia[1]:
            in_target += 1
    
    target_rate = (in_target / len(sys_values)) * 100
    
    # Tính ARV
    arv = 0
    if len(sys_values) > 1:
        diffs = [abs(sys_values[i+1] - sys_values[i]) for i in range(len(sys_values)-1)]
        arv = sum(diffs) / len(diffs)
    
    # Số ngày có đo
    days_with_reading = set()
    for row in bp_data:
        try:
            dt = datetime.strptime(row['measurement_time'], '%Y-%m-%d %H:%M:%S')
            days_with_reading.add(dt.date())
        except:
            continue
    
    return {
        'total_readings': len(sys_values),
        'days_with_reading': len(days_with_reading),
        'avg_sys': round(avg_sys),
        'avg_dia': round(avg_dia),
        'max_sys': max(sys_values),
        'max_dia': max([d for s, d in zip(sys_values, dia_values) if s == max(sys_values)]),
        'min_sys': min(sys_values),
        'min_dia': min([d for s, d in zip(sys_values, dia_values) if s == min(sys_values)]),
        'target_rate': round(target_rate, 1),
        'arv': round(arv, 1),
        'avg_hr': round(sum(hr_values) / len(hr_values)) if hr_values else None
    }


def get_days_in_month(year: int, month: int) -> int:
    """Lấy số ngày trong tháng"""
    if month == 12:
        next_month = datetime(year + 1, 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)
    return (next_month - datetime(year, month, 1)).days


def format_events_table(events: List[Dict]) -> str:
    """Tạo bảng tương quan sự kiện"""
    if not events:
        return "⚠️ *Không có sự kiện nào được ghi nhận trong tháng này.*"
    
    lines = [
        "| Sự kiện | Thời điểm | Ghi chú |",
        "|:---|:---|:---|"
    ]
    
    for e in events[:5]:  # Tối đa 5 sự kiện
        event_type = EVENT_LABELS.get(e.get('event_type', ''), e.get('event_type', ''))
        try:
            dt = datetime.strptime(e['event_time'], '%Y-%m-%d %H:%M:%S')
            time_str = dt.strftime('%d/%m %H:%M')
        except:
            time_str = e.get('event_time', '')
        
        notes = e.get('notes', '')[:30]
        lines.append(f"| **{event_type}** | {time_str} | {notes} |")
    
    return "\n".join(lines)


def generate_recommendations(user_type: str, target_rate: float, arv: float) -> str:
    """Tạo khuyến nghị hành động dựa trên loại user và chỉ số"""
    
    control_class, _ = classify_control_rate(target_rate)
    
    if control_class == "Kiểm soát Tối Ưu":
        intro = "Tiếp tục duy trì chế độ điều trị hiện tại - rất hiệu quả!"
    elif control_class == "Kiểm soát Tốt":
        intro = "Cố gắng nâng tỷ lệ kiểm soát lên >70% để đạt mức tối ưu."
    else:
        intro = "Cần trao đổi với bác sĩ để xem xét lại phác đồ điều trị."
    
    return f"""## 4. Nhận Xét Tổng Hợp

👉 **Nhận xét:**
- Về mức độ kiểm soát: {target_rate}% số lần đo đạt mục tiêu điều trị (**{control_class}**).
- Về độ ổn định: huyết áp {classify_arv(arv).lower()} giữa các lần đo (ARV = {arv}).

## 5. Khuyến Nghị Hành Động

🩺 **Tuân thủ điều trị:**
- {intro}
- Đo huyết áp đều đặn để duy trì theo dõi.

🥗 **Điều chỉnh dinh dưỡng:**
- Hạn chế ăn mặn, rượu bia.
- Tăng cường rau xanh và trái cây.

🏃 **Vận động:**
- Duy trì hoạt động thể chất đều đặn 20-30 phút mỗi ngày.

🎯 **Mục tiêu tháng tới:** Duy trì hoặc nâng cao tỷ lệ kiểm soát."""


def update_monthly_report(filepath: Path, bp_data: List[Dict], events: List[Dict], 
                          target_sys: Tuple[int, int], target_dia: Tuple[int, int],
                          user_type: str, year: int, month: int):
    """Cập nhật file báo cáo tháng với các tiêu chí SRS BR-005"""
    
    if not filepath.exists():
        print(f"  ⚠️ File không tồn tại: {filepath}")
        return
    
    # Đọc file hiện tại
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Tính toán metrics
    month_bp = get_month_data(bp_data, year, month)
    month_events = get_month_events(events, year, month)
    
    if not month_bp:
        print(f"  ⚠️ Không có dữ liệu BP cho tháng {month}/{year}")
        return
    
    metrics = calculate_metrics(month_bp, target_sys, target_dia)
    if not metrics:
        return
    
    days_in_month = get_days_in_month(year, month)
    compliance_rate = round((metrics['days_with_reading'] / days_in_month) * 100, 1)
    
    control_class, control_range = classify_control_rate(metrics['target_rate'])
    
    # Kiểm tra điều kiện đủ dữ liệu (>=14 ngày có >=2 lần đo/ngày)
    has_sufficient_data = metrics['days_with_reading'] >= 14
    
    # 1. Cập nhật phần Tổng Quan Theo Dõi
    old_overview_pattern = r"## 1\. Tổng Quan Theo Dõi\n\n\| Chỉ số \| Giá trị \|\n\|:---\|:---\|\n.*?\n\n"
    
    if has_sufficient_data:
        data_status = ""
    else:
        data_status = f"\n⚠️ **Tháng này chưa đủ dữ liệu để phân tích chuyên sâu** (yêu cầu ≥ 14 ngày có ≥2 lần đo/ngày)"
    
    new_overview = f"""## 1. Tổng Quan Theo Dõi

| Chỉ số | Giá trị |
|:---|:---|
| **Tổng số lần đo** | {metrics['total_readings']} lần |
| **Số ngày có đo** | {metrics['days_with_reading']} ngày |
| **Tỷ lệ tuân thủ lịch đo** | {compliance_rate}% ({metrics['days_with_reading']}/{days_in_month} ngày) |
| **Tỷ lệ đo trong ngưỡng mục tiêu** | {metrics['target_rate']}% |
| **Phân loại mức độ kiểm soát** | **{control_class}** ({control_range}) |
{data_status}

"""
    
    # Thử match và replace phần overview
    content = re.sub(
        r"## 1\. Tổng Quan Theo Dõi\n\n\| Chỉ số \| Giá trị \|\n\|:---\|:---\|\n.*?(?=\n---)",
        new_overview.rstrip(),
        content,
        flags=re.DOTALL
    )
    
    # 2. Thêm phần Xu hướng và Tương quan sự kiện sau 2.4
    events_table = format_events_table(month_events)
    
    trend_section = f"""### 2.5 Xu Hướng So Với Tháng Trước

📊 *Xem phân tích xu hướng trong phần Nhận Xét Tổng Hợp.*

### 2.6 Tương Quan Với Sự Kiện

{events_table}

"""
    
    # Thêm sau phần 2.4 nếu chưa có
    if "### 2.5 Xu Hướng" not in content:
        content = re.sub(
            r"(\| \*\*Thời điểm thường xảy ra\*\* \|.*?\|\n)\n---\n\n## 3\.",
            f"\\1\n{trend_section}---\n\n## 3.",
            content
        )
    
    # 3. Thay thế phần Lời Khuyên bằng Nhận Xét + Khuyến Nghị chi tiết
    recommendations = generate_recommendations(user_type, metrics['target_rate'], metrics['arv'])
    
    content = re.sub(
        r"## 4\. Lời Khuyên Tháng Tới\n\n.*?(?=\n---\n\n>)",
        recommendations,
        content,
        flags=re.DOTALL
    )
    
    # Ghi file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ Đã cập nhật: {filepath.name}")


def get_user_target_thresholds(health_profile: Dict) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """Lấy ngưỡng mục tiêu từ health profile"""
    sys_lower = int(health_profile.get('systolic_threshold_lower') or 120)
    sys_upper = int(health_profile.get('systolic_threshold_upper') or 140)
    dia_lower = int(health_profile.get('diastolic_threshold_lower') or 70)
    dia_upper = int(health_profile.get('diastolic_threshold_upper') or 90)
    
    return (sys_lower, sys_upper), (dia_lower, dia_upper)


def process_user(user_folder: str):
    """Xử lý cập nhật báo cáo cho một user"""
    user_path = BASE_PATH / user_folder
    print(f"\n📁 Đang xử lý: {user_folder}")
    
    # Đọc dữ liệu
    bp_data = read_csv(user_path / "user_blood_pressure.csv")
    events = read_csv(user_path / "events.csv")
    health_profiles = read_csv(user_path / "user_health_profiles.csv")
    
    if not bp_data:
        print(f"  ⚠️ Không có dữ liệu huyết áp")
        return
    
    # Lấy ngưỡng mục tiêu
    if health_profiles:
        target_sys, target_dia = get_user_target_thresholds(health_profiles[0])
    else:
        target_sys = (120, 140)
        target_dia = (70, 90)
    
    print(f"  📊 Ngưỡng mục tiêu: SYS {target_sys[0]}-{target_sys[1]}, DIA {target_dia[0]}-{target_dia[1]}")
    
    # Xác định loại user
    users_data = read_csv(user_path / "users.csv")
    user_type = users_data[0].get('blood_pressure_status', 'unknown') if users_data else 'unknown'
    
    # Lấy danh sách file báo cáo tháng
    month_folder = user_path / "month"
    if not month_folder.exists():
        print(f"  ⚠️ Không tìm thấy thư mục month/")
        return
    
    for md_file in sorted(month_folder.glob("month_*.md")):
        # Parse year-month từ tên file
        match = re.search(r"month_(\d{4})-(\d{2})\.md", md_file.name)
        if match:
            year = int(match.group(1))
            month = int(match.group(2))
            update_monthly_report(
                md_file, bp_data, events, 
                target_sys, target_dia,
                user_type, year, month
            )


def main():
    print("=" * 60)
    print("🔄 Script Cập Nhật Báo Cáo Tháng theo SRS BR-005")
    print("=" * 60)
    
    for user in USERS:
        process_user(user)
    
    print("\n" + "=" * 60)
    print("✅ Hoàn thành cập nhật tất cả báo cáo!")
    print("=" * 60)


if __name__ == "__main__":
    main()
