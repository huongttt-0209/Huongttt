#!/usr/bin/env python3
"""
Script cập nhật công thức tính và kết quả trong các file báo cáo tuần/tháng.
Tính toán lại tất cả các chỉ số từ dữ liệu CSV theo SRS BR-005.

Công thức:
- HA Trung bình: Trung bình cộng tất cả các giá trị SYS và DIA
- HA Cao nhất: Cặp SYS/DIA có SYS cao nhất (nếu trùng, lấy DIA cao hơn)
- HA Thấp nhất: Cặp SYS/DIA có SYS thấp nhất (nếu trùng, lấy DIA thấp hơn)
- ARV: Trung bình độ chênh lệch giữa các lần đo liên tiếp (trong 24h)
- ME diff: HA sáng TB - HA tối TB (sáng: 4-10h, tối: 20-24h)
- % trong ngưỡng: Số lần cả SYS và DIA trong ngưỡng / Tổng lần đo
"""

import os
import re
import csv
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# Đường dẫn gốc
BASE_PATH = Path("/Users/teamai/Downloads/antigravity/koliaa/Huongttt/feature/bao_cao/csv/Data_import/insert_dev")

# Các user cần xử lý  
USERS = ["user_tha", "user_bp_load", "user_ha_thap", "user_ko_on_dinh"]


def load_bp_data(filepath: Path) -> List[Dict]:
    """Load blood pressure data from CSV file"""
    data = []
    if not filepath.exists():
        return data
    
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                measurement_time = datetime.strptime(row['measurement_time'].strip(), '%Y-%m-%d %H:%M:%S')
                data.append({
                    'systolic': int(row.get('systolic', 0)),
                    'diastolic': int(row.get('diastolic', 0)),
                    'heart_rate': int(row.get('heart_rate', 0)),
                    'measurement_time': measurement_time,
                })
            except (ValueError, KeyError):
                continue
    return sorted(data, key=lambda x: x['measurement_time'])


def parse_date_range_from_filename(filename: str) -> Tuple[Optional[datetime], Optional[datetime]]:
    """Parse start and end date from filename like '2025-12-01_2025-12-07.md'"""
    name = filename.replace('.md', '')
    parts = name.split('_')
    if len(parts) == 2:
        start_date = datetime.strptime(parts[0], '%Y-%m-%d')
        end_date = datetime.strptime(parts[1], '%Y-%m-%d')
        return start_date, end_date
    return None, None


def parse_month_from_filename(filename: str) -> Tuple[Optional[int], Optional[int]]:
    """Parse year and month from filename like 'month_2025-12.md'"""
    match = re.search(r'month_(\d{4})-(\d{2})\.md', filename)
    if match:
        return int(match.group(1)), int(match.group(2))
    return None, None


def filter_bp_for_period(bp_data: List[Dict], start_date: datetime, end_date: datetime) -> List[Dict]:
    """Filter BP data for a specific period"""
    end_inclusive = end_date.replace(hour=23, minute=59, second=59)
    return [bp for bp in bp_data if start_date <= bp['measurement_time'] <= end_inclusive]


def filter_bp_for_month(bp_data: List[Dict], year: int, month: int) -> List[Dict]:
    """Filter BP data for a specific month"""
    return [bp for bp in bp_data 
            if bp['measurement_time'].year == year and bp['measurement_time'].month == month]


def extract_target_range(content: str) -> Tuple[Optional[Tuple[int, int]], Optional[Tuple[int, int]]]:
    """Extract target BP range from report header"""
    sys_match = re.search(r'SYS\s*(\d+)-(\d+)', content)
    dia_match = re.search(r'DIA\s*(\d+)-(\d+)', content)
    
    if sys_match and dia_match:
        return (int(sys_match.group(1)), int(sys_match.group(2))), \
               (int(dia_match.group(1)), int(dia_match.group(2)))
    return None, None


def calculate_metrics(bp_list: List[Dict], sys_range: Tuple[int, int], dia_range: Tuple[int, int]) -> Dict:
    """Calculate all BP metrics from data"""
    if not bp_list:
        return None
    
    n = len(bp_list)
    
    # HA Trung bình
    avg_sys = sum(bp['systolic'] for bp in bp_list) / n
    avg_dia = sum(bp['diastolic'] for bp in bp_list) / n
    avg_hr = sum(bp['heart_rate'] for bp in bp_list) / n
    
    # HA Cao nhất (theo SYS, nếu trùng lấy DIA cao hơn)
    sorted_by_high = sorted(bp_list, key=lambda x: (-x['systolic'], -x['diastolic']))
    highest = sorted_by_high[0]
    
    # HA Thấp nhất (theo SYS, nếu trùng lấy DIA thấp hơn)
    sorted_by_low = sorted(bp_list, key=lambda x: (x['systolic'], x['diastolic']))
    lowest = sorted_by_low[0]
    
    # Nhịp tim cao/thấp
    hr_list = [bp['heart_rate'] for bp in bp_list]
    hr_max = max(hr_list)
    hr_min = min(hr_list)
    
    # % trong ngưỡng mục tiêu
    in_range_count = sum(1 for bp in bp_list 
                         if sys_range[0] <= bp['systolic'] <= sys_range[1] 
                         and dia_range[0] <= bp['diastolic'] <= dia_range[1])
    pct_in_range = (in_range_count / n) * 100
    
    # ARV (Average Real Variability) - chỉ tính các cặp trong 24h
    arv_sum = 0
    arv_count = 0
    for i in range(1, n):
        time_diff = (bp_list[i]['measurement_time'] - bp_list[i-1]['measurement_time']).total_seconds() / 3600
        if time_diff <= 24:
            arv_sum += abs(bp_list[i]['systolic'] - bp_list[i-1]['systolic'])
            arv_count += 1
    arv = arv_sum / arv_count if arv_count > 0 else 0
    
    # ME diff (Morning-Evening difference)
    # Sáng: 04:00 - 10:00, Tối: 20:00 - 24:00
    morning_bp = [bp for bp in bp_list if 4 <= bp['measurement_time'].hour < 10]
    evening_bp = [bp for bp in bp_list if 20 <= bp['measurement_time'].hour <= 23]
    
    if morning_bp and evening_bp:
        morning_avg_sys = sum(bp['systolic'] for bp in morning_bp) / len(morning_bp)
        evening_avg_sys = sum(bp['systolic'] for bp in evening_bp) / len(evening_bp)
        me_diff = morning_avg_sys - evening_avg_sys
    else:
        me_diff = 0
    
    # Số ngày có đo
    days_with_data = len(set(bp['measurement_time'].date() for bp in bp_list))
    
    # Vượt ngưỡng (ngoài ngưỡng mục tiêu)
    out_of_range = n - in_range_count
    
    # Phân bố theo buổi
    morning_count = len([bp for bp in bp_list if 4 <= bp['measurement_time'].hour < 12])
    afternoon_count = len([bp for bp in bp_list if 12 <= bp['measurement_time'].hour < 18])
    evening_count = len([bp for bp in bp_list if bp['measurement_time'].hour >= 18 or bp['measurement_time'].hour < 4])
    
    # Ngày có HA cao nhất
    max_day = highest['measurement_time'].strftime('%d/%m')
    
    return {
        'count': n,
        'days': days_with_data,
        'avg_sys': round(avg_sys),
        'avg_dia': round(avg_dia),
        'avg_hr': round(avg_hr),
        'high_sys': highest['systolic'],
        'high_dia': highest['diastolic'],
        'low_sys': lowest['systolic'],
        'low_dia': lowest['diastolic'],
        'hr_max': hr_max,
        'hr_min': hr_min,
        'pct_in_range': round(pct_in_range, 1),
        'arv': round(arv, 1),
        'me_diff': round(me_diff),
        'out_of_range': out_of_range,
        'morning': morning_count,
        'afternoon': afternoon_count,
        'evening': evening_count,
        'max_day': max_day,
        'max_sys': highest['systolic'],
        'max_dia': highest['diastolic'],
    }


def classify_control(pct: float) -> Tuple[str, str]:
    """Classify BP control level"""
    if pct > 70:
        return "**Kiểm soát tối ưu**", "Huyết áp rất ổn định, đạt trạng thái lý tưởng."
    elif pct >= 50:
        return "**Kiểm soát tốt**", "Đạt yêu cầu điều trị. Đa số thời gian cơ thể được bảo vệ."
    elif pct >= 25:
        return "**Kiểm soát kém**", "Huyết áp dao động nhiều. Hiệu quả phác đồ thuốc chưa ổn định."
    else:
        return "**Không được kiểm soát**", "Rất ít khi huyết áp đạt đích. Nguy cơ biến cố cao."


def classify_arv(arv: float) -> Tuple[str, str]:
    """Classify ARV stability"""
    if arv < 10:
        return "**Ổn định**", "Hệ mạch vận hành êm ái, ít áp lực cơ học."
    elif arv < 14:
        return "**Biến động**", "Mạch máu bắt đầu chịu áp lực từ sự dao động."
    else:
        return "**Bất ổn**", "Nguy cơ cao tổn thương thành mạch và cơ quan đích."


def classify_me_diff(me_diff: float) -> Tuple[str, str]:
    """Classify ME diff rhythm"""
    if me_diff > 15:
        return "**Vọt áp buổi sáng**", "Áp lực máu tăng quá mức khi thức dậy."
    elif me_diff < -15:
        return "**Tăng áp về tối**", "Dấu hiệu Non-dipper, rất hại cho tim và thận."
    else:
        return "**Cân bằng**", "Nhịp sinh học ổn định."


def update_week_report(filepath: Path, metrics: Dict) -> bool:
    """Update weekly report with recalculated metrics"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get original content for comparison
    original = content
    
    # Update metrics in tables
    patterns = [
        # Số lần đo
        (r'\| Số lần đo \| \d+ lần \|', f'| Số lần đo | {metrics["count"]} lần |'),
        
        # HA Trung bình
        (r'\| \*\*HA Trung bình\*\* \| \d+/\d+ mmHg \|', 
         f'| **HA Trung bình** | {metrics["avg_sys"]}/{metrics["avg_dia"]} mmHg |'),
        
        # HA Cao nhất
        (r'\| \*\*HA Cao nhất\*\* \| \d+/\d+ mmHg \|',
         f'| **HA Cao nhất** | {metrics["high_sys"]}/{metrics["high_dia"]} mmHg |'),
        
        # HA Thấp nhất
        (r'\| \*\*HA Thấp nhất\*\* \| \d+/\d+ mmHg \|',
         f'| **HA Thấp nhất** | {metrics["low_sys"]}/{metrics["low_dia"]} mmHg |'),
        
        # Nhịp tim TB
        (r'\| \*\*Nhịp tim TB\*\* \| \d+ bpm \|',
         f'| **Nhịp tim TB** | {metrics["avg_hr"]} bpm |'),
        
        # Nhịp tim Trung bình
        (r'\| \*\*Nhịp tim Trung bình\*\* \| \d+ bpm \|',
         f'| **Nhịp tim Trung bình** | {metrics["avg_hr"]} bpm |'),
        
        # Nhịp tim Cao nhất
        (r'\| \*\*Nhịp tim Cao nhất\*\* \| \d+ bpm \|',
         f'| **Nhịp tim Cao nhất** | {metrics["hr_max"]} bpm |'),
        
        # Nhịp tim Thấp nhất
        (r'\| \*\*Nhịp tim Thấp nhất\*\* \| \d+ bpm \|',
         f'| **Nhịp tim Thấp nhất** | {metrics["hr_min"]} bpm |'),
        
        # % trong ngưỡng - weekly format
        (r'\| \*\*% trong ngưỡng\*\* \| [\d.]+% \|',
         f'| **% trong ngưỡng** | {metrics["pct_in_range"]}% |'),
        
        # ARV
        (r'\| \*\*ARV tâm thu\*\* \| [\d.]+ \|',
         f'| **ARV tâm thu** | {metrics["arv"]} |'),
        
        # ME diff
        (r'\| \*\*ME diff\*\* \| [+-]?\d+ mmHg \|',
         f'| **ME diff** | {"+" if metrics["me_diff"] >= 0 else ""}{metrics["me_diff"]} mmHg |'),
        
        # Số lần vượt ngưỡng
        (r'\| \*\*Số lần vượt ngưỡng\*\* \| \d+/\d+ lần \([\d.]+%\) \|',
         f'| **Số lần vượt ngưỡng** | {metrics["out_of_range"]}/{metrics["count"]} lần ({100 - metrics["pct_in_range"]:.1f}%) |'),
        
        # Ngày HA cao nhất
        (r'\| \*\*Ngày HA cao nhất\*\* \| \d+/\d+ \(\d+/\d+ mmHg\) \|',
         f'| **Ngày HA cao nhất** | {metrics["max_day"]} ({metrics["max_sys"]}/{metrics["max_dia"]} mmHg) |'),
        
        # Phân bố
        (r'\| \*\*Phân bố\*\* \| Sáng: \d+, Chiều: \d+, Tối: \d+ \|',
         f'| **Phân bố** | Sáng: {metrics["morning"]}, Chiều: {metrics["afternoon"]}, Tối: {metrics["evening"]} |'),
    ]
    
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    # Update control classification
    control_class, control_explain = classify_control(metrics['pct_in_range'])
    content = re.sub(
        r'\| \*\*% trong ngưỡng\*\* \| [\d.]+% \| [^|]+ \| [^|]+ \|',
        f'| **% trong ngưỡng** | {metrics["pct_in_range"]}% | {control_class} | >70% |',
        content
    )
    
    # Update ARV classification
    arv_class, arv_explain = classify_arv(metrics['arv'])
    content = re.sub(
        r'\| \*\*ARV tâm thu\*\* \| [\d.]+ \| [^|]+ \| [^|]+ \|',
        f'| **ARV tâm thu** | {metrics["arv"]} | {arv_class} | <10 |',
        content
    )
    
    # Update ME diff classification
    me_class, me_explain = classify_me_diff(metrics['me_diff'])
    content = re.sub(
        r'\| \*\*ME diff\*\* \| [+-]?\d+ mmHg \| [^|]+ \| [^|]+ \|',
        f'| **ME diff** | {"+" if metrics["me_diff"] >= 0 else ""}{metrics["me_diff"]} mmHg | {me_class} | -15~15 mmHg |',
        content
    )
    
    # Write back if changed
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def update_month_report(filepath: Path, metrics: Dict) -> bool:
    """Update monthly report with recalculated metrics - same logic as week"""
    return update_week_report(filepath, metrics)


def process_user(user_folder: str) -> Dict:
    """Process all reports for a user"""
    user_path = BASE_PATH / user_folder
    week_path = user_path / "week"
    month_path = user_path / "month"
    bp_file = user_path / "user_blood_pressure.csv"
    
    print(f"\n📂 Đang xử lý: {user_folder}")
    
    stats = {"week_updated": 0, "month_updated": 0}
    
    if not bp_file.exists():
        print(f"  ❌ Không tìm thấy file user_blood_pressure.csv")
        return stats
    
    bp_data = load_bp_data(bp_file)
    print(f"  📊 Đã tải {len(bp_data)} bản ghi huyết áp")
    
    # Process week reports
    if week_path.exists():
        week_files = sorted([f for f in week_path.iterdir() if f.suffix == '.md'])
        for week_file in week_files:
            start_date, end_date = parse_date_range_from_filename(week_file.name)
            if not start_date:
                continue
            
            with open(week_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            sys_range, dia_range = extract_target_range(content)
            if not sys_range:
                continue
            
            week_bp = filter_bp_for_period(bp_data, start_date, end_date)
            if not week_bp:
                continue
            
            metrics = calculate_metrics(week_bp, sys_range, dia_range)
            
            # Calculate compliance for week (days with data / 7)
            total_days = (end_date - start_date).days + 1
            compliance = (metrics['days'] / total_days) * 100
            metrics['compliance'] = round(compliance, 1)
            
            if update_week_report(week_file, metrics):
                print(f"  ✅ Week: {week_file.name} - Cập nhật {len(week_bp)} bản ghi")
                stats["week_updated"] += 1
            else:
                print(f"  ⏭️  Week: {week_file.name} - Không thay đổi")
    
    # Process month reports
    if month_path.exists():
        month_files = sorted([f for f in month_path.iterdir() if f.suffix == '.md'])
        for month_file in month_files:
            year, month = parse_month_from_filename(month_file.name)
            if not year:
                continue
            
            with open(month_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            sys_range, dia_range = extract_target_range(content)
            if not sys_range:
                continue
            
            month_bp = filter_bp_for_month(bp_data, year, month)
            if not month_bp:
                continue
            
            metrics = calculate_metrics(month_bp, sys_range, dia_range)
            
            if update_month_report(month_file, metrics):
                print(f"  ✅ Month: {month_file.name} - Cập nhật {len(month_bp)} bản ghi")
                stats["month_updated"] += 1
            else:
                print(f"  ⏭️  Month: {month_file.name} - Không thay đổi")
    
    return stats


def main():
    print("=" * 70)
    print("📐 CẬP NHẬT CÔNG THỨC TÍNH VÀ KẾT QUẢ TỪ DỮ LIỆU CSV")
    print("=" * 70)
    print("Công thức theo SRS BR-005:")
    print("  • HA Trung bình = Σ(SYS)/n, Σ(DIA)/n") 
    print("  • HA Cao nhất = max(SYS), max(DIA) tại max(SYS)")
    print("  • HA Thấp nhất = min(SYS), min(DIA) tại min(SYS)")
    print("  • ARV = Σ|SYS[i+1] - SYS[i]| / (n-1) [trong 24h]")
    print("  • ME diff = HA sáng TB - HA tối TB")
    print("=" * 70)
    
    total_week = 0
    total_month = 0
    
    for user in USERS:
        stats = process_user(user)
        total_week += stats["week_updated"]
        total_month += stats["month_updated"]
    
    print("\n" + "=" * 70)
    print("📊 TỔNG KẾT")
    print("=" * 70)
    print(f"   📅 Báo cáo tuần đã cập nhật: {total_week}")
    print(f"   📆 Báo cáo tháng đã cập nhật: {total_month}")
    print("=" * 70)


if __name__ == "__main__":
    main()
