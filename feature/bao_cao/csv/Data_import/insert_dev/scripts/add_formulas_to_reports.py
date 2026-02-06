#!/usr/bin/env python3
"""
Script bổ sung phần công thức tính vào các file báo cáo tuần/tháng.
Hiển thị chi tiết cách tính từng chỉ số từ dữ liệu đo.
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
    """Parse start and end date from filename"""
    name = filename.replace('.md', '')
    parts = name.split('_')
    if len(parts) == 2:
        try:
            start_date = datetime.strptime(parts[0], '%Y-%m-%d')
            end_date = datetime.strptime(parts[1], '%Y-%m-%d')
            return start_date, end_date
        except:
            pass
    return None, None


def parse_month_from_filename(filename: str) -> Tuple[Optional[int], Optional[int]]:
    """Parse year and month from filename"""
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


def generate_formula_section(bp_list: List[Dict], sys_range: Tuple[int, int], dia_range: Tuple[int, int]) -> str:
    """Generate the calculation formula section"""
    if not bp_list or len(bp_list) < 1:
        return ""
    
    n = len(bp_list)
    bp_sorted = sorted(bp_list, key=lambda x: x['measurement_time'])
    
    # Extract values
    sys_values = [bp['systolic'] for bp in bp_sorted]
    dia_values = [bp['diastolic'] for bp in bp_sorted]
    hr_values = [bp['heart_rate'] for bp in bp_sorted]
    
    # Calculate metrics
    avg_sys = sum(sys_values) / n
    avg_dia = sum(dia_values) / n
    avg_hr = sum(hr_values) / n
    
    # Find max/min
    max_idx = sys_values.index(max(sys_values))
    min_idx = sys_values.index(min(sys_values))
    max_bp = bp_sorted[max_idx]
    min_bp = bp_sorted[min_idx]
    
    # In-range count
    in_range = sum(1 for bp in bp_sorted 
                   if sys_range[0] <= bp['systolic'] <= sys_range[1] 
                   and dia_range[0] <= bp['diastolic'] <= dia_range[1])
    out_range = n - in_range
    pct = (in_range / n) * 100
    
    # ARV calculation
    arv_diffs = []
    for i in range(1, n):
        time_diff = (bp_sorted[i]['measurement_time'] - bp_sorted[i-1]['measurement_time']).total_seconds() / 3600
        if time_diff <= 24:
            arv_diffs.append(abs(bp_sorted[i]['systolic'] - bp_sorted[i-1]['systolic']))
    arv = sum(arv_diffs) / len(arv_diffs) if arv_diffs else 0
    
    # ME diff
    morning_bp = [bp['systolic'] for bp in bp_sorted if 4 <= bp['measurement_time'].hour < 10]
    evening_bp = [bp['systolic'] for bp in bp_sorted if 20 <= bp['measurement_time'].hour <= 23]
    
    morning_avg = sum(morning_bp) / len(morning_bp) if morning_bp else 0
    evening_avg = sum(evening_bp) / len(evening_bp) if evening_bp else 0
    me_diff = morning_avg - evening_avg if morning_bp and evening_bp else 0
    
    # Build formula strings
    sys_str = '+'.join(str(s) for s in sys_values[:10])
    if n > 10:
        sys_str += f"+...+{sys_values[-1]}"
    
    dia_str = '+'.join(str(d) for d in dia_values[:10])
    if n > 10:
        dia_str += f"+...+{dia_values[-1]}"
    
    hr_str = '+'.join(str(h) for h in hr_values[:10])
    if n > 10:
        hr_str += f"+...+{hr_values[-1]}"
    
    # Out of range list
    out_range_list = []
    for i, bp in enumerate(bp_sorted):
        if not (sys_range[0] <= bp['systolic'] <= sys_range[1] and dia_range[0] <= bp['diastolic'] <= dia_range[1]):
            out_range_list.append(f"#{i+1}: {bp['systolic']}/{bp['diastolic']}")
    out_range_str = ", ".join(out_range_list[:5])
    if len(out_range_list) > 5:
        out_range_str += f", ... (+{len(out_range_list)-5})"
    
    # ARV diff string
    arv_str = "+".join(str(d) for d in arv_diffs[:8])
    if len(arv_diffs) > 8:
        arv_str += f"+...+{arv_diffs[-1]}"
    arv_sum = sum(arv_diffs)
    
    # Morning/Evening values
    morning_str = ", ".join(str(s) for s in morning_bp[:5])
    if len(morning_bp) > 5:
        morning_str += f", ... (+{len(morning_bp)-5})"
    evening_str = ", ".join(str(s) for s in evening_bp[:5])
    if len(evening_bp) > 5:
        evening_str += f", ... (+{len(evening_bp)-5})"
    
    # Classify ARV
    arv_class = "Ổn định" if arv < 10 else ("Biến động" if arv < 14 else "Bất ổn")
    
    # Classify ME diff
    me_class = "Cân bằng" if -15 <= me_diff <= 15 else ("Vọt áp sáng" if me_diff > 15 else "Tăng áp tối")
    
    section = f"""
---

## 📐 Công thức tính và Xác minh

### HA Trung bình
```
SYS_TB = ({sys_str}) / {n}
       = {sum(sys_values)} / {n} = {round(avg_sys)} mmHg

DIA_TB = ({dia_str}) / {n}
       = {sum(dia_values)} / {n} = {round(avg_dia)} mmHg
```

### HA Cao nhất / Thấp nhất
```
HA Cao nhất = max(SYS) → {max_bp['systolic']} mmHg tại {max_bp['measurement_time'].strftime('%d/%m %H:%M')}
            → Cặp: {max_bp['systolic']}/{max_bp['diastolic']} mmHg
HA Thấp nhất = min(SYS) → {min_bp['systolic']} mmHg tại {min_bp['measurement_time'].strftime('%d/%m %H:%M')}
            → Cặp: {min_bp['systolic']}/{min_bp['diastolic']} mmHg
```

### % trong ngưỡng mục tiêu (SYS {sys_range[0]}-{sys_range[1]}, DIA {dia_range[0]}-{dia_range[1]})
```
Trong ngưỡng = {in_range} lần (cả SYS và DIA đều trong ngưỡng)
Ngoài ngưỡng = {out_range} lần ({out_range_str if out_range_str else "không có"})

% = {in_range}/{n} × 100% = {pct:.1f}%
```

### ARV (Độ ổn định - Average Real Variability)
```
ARV = Σ|SYS[i+1] - SYS[i]| / (n-1)  [chỉ cặp trong 24h]

Tổng chênh lệch: {arv_str} = {arv_sum}
Số cặp hợp lệ: {len(arv_diffs)}

ARV = {arv_sum} / {len(arv_diffs)} = {arv:.1f} mmHg  [→ {arv_class}]
```

### ME diff (Morning-Evening difference)
```
Sáng (04:00-10:00): {morning_str if morning_str else "Không có dữ liệu"} → TB = {morning_avg:.1f} mmHg
Tối (20:00-24:00): {evening_str if evening_str else "Không có dữ liệu"} → TB = {evening_avg:.1f} mmHg

ME diff = {morning_avg:.1f} - {evening_avg:.1f} = {me_diff:+.0f} mmHg  [→ {me_class}]
```

### Nhịp tim
```
HR_TB = ({hr_str}) / {n}
      = {sum(hr_values)} / {n} = {round(avg_hr)} bpm

HR_max = {max(hr_values)} bpm
HR_min = {min(hr_values)} bpm
```

"""
    return section


def has_formula_section(content: str) -> bool:
    """Check if file already has formula section"""
    return "## 📐 Công thức tính và Xác minh" in content


def add_formula_to_report(filepath: Path, bp_list: List[Dict], sys_range: Tuple[int, int], dia_range: Tuple[int, int]) -> bool:
    """Add formula section to a report file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if has_formula_section(content):
        return False  # Already has formulas
    
    if not bp_list:
        return False
    
    formula_section = generate_formula_section(bp_list, sys_range, dia_range)
    if not formula_section:
        return False
    
    # Find where to insert (before "## 2. Phân Tích Huyết Áp")
    insert_pattern = r'(---\n\n## 2\. Phân Tích Huyết Áp)'
    
    if re.search(insert_pattern, content):
        new_content = re.sub(insert_pattern, formula_section + r'\1', content)
    else:
        # Try alternative pattern for month reports
        insert_pattern2 = r'(---\n\n## 2\. Phân Tích Huyết Áp)'
        if re.search(insert_pattern2, content):
            new_content = re.sub(insert_pattern2, formula_section + r'\1', content)
        else:
            # Just append before the disclaimer
            new_content = content.replace(
                "> *Báo cáo được tạo tự động",
                formula_section + "\n> *Báo cáo được tạo tự động"
            )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True


def process_user(user_folder: str) -> Dict:
    """Process all reports for a user"""
    user_path = BASE_PATH / user_folder
    week_path = user_path / "week"
    month_path = user_path / "month"
    bp_file = user_path / "user_blood_pressure.csv"
    
    print(f"\n📂 Đang xử lý: {user_folder}")
    
    stats = {"week": 0, "month": 0}
    
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
            
            if add_formula_to_report(week_file, week_bp, sys_range, dia_range):
                print(f"  ✅ Week: {week_file.name} - Thêm công thức ({len(week_bp)} bản ghi)")
                stats["week"] += 1
            else:
                print(f"  ⏭️  Week: {week_file.name} - Đã có công thức")
    
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
            
            if add_formula_to_report(month_file, month_bp, sys_range, dia_range):
                print(f"  ✅ Month: {month_file.name} - Thêm công thức ({len(month_bp)} bản ghi)")
                stats["month"] += 1
            else:
                print(f"  ⏭️  Month: {month_file.name} - Đã có công thức")
    
    return stats


def main():
    print("=" * 70)
    print("📐 BỔ SUNG CÔNG THỨC TÍNH VÀO BÁO CÁO TUẦN/THÁNG")
    print("=" * 70)
    
    total_week = 0
    total_month = 0
    
    for user in USERS:
        stats = process_user(user)
        total_week += stats["week"]
        total_month += stats["month"]
    
    print("\n" + "=" * 70)
    print("📊 TỔNG KẾT")
    print("=" * 70)
    print(f"   📅 Báo cáo tuần đã bổ sung công thức: {total_week}")
    print(f"   📆 Báo cáo tháng đã bổ sung công thức: {total_month}")
    print("=" * 70)


if __name__ == "__main__":
    main()
