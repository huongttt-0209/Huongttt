#!/usr/bin/env python3
"""
Script bổ sung dữ liệu đo huyết áp vào các file báo cáo tuần.
Thêm bảng chi tiết các lần đo HA vào cuối mỗi file báo cáo tuần.
"""

import os
import csv
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

# Đường dẫn gốc
BASE_PATH = Path("/Users/teamai/Downloads/antigravity/koliaa/Huongttt/feature/bao_cao/csv/Data_import/insert_dev")

# Các user cần xử lý
USERS = ["user_tha", "user_bp_load", "user_ha_thap", "user_ko_on_dinh"]


def parse_date_range_from_filename(filename: str) -> tuple:
    """Parse start and end date from filename like '2025-12-01_2025-12-07.md'"""
    name = filename.replace('.md', '')
    parts = name.split('_')
    if len(parts) == 2:
        start_date = datetime.strptime(parts[0], '%Y-%m-%d')
        end_date = datetime.strptime(parts[1], '%Y-%m-%d')
        return start_date, end_date
    return None, None


def load_bp_data(filepath: Path) -> list:
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
                    'id': row.get('id', ''),
                    'systolic': int(row.get('systolic', 0)),
                    'diastolic': int(row.get('diastolic', 0)),
                    'heart_rate': int(row.get('heart_rate', 0)),
                    'measurement_time': measurement_time,
                    'notes': row.get('notes', '').strip()
                })
            except (ValueError, KeyError) as e:
                print(f"  ⚠️ Lỗi parse dòng: {row} - {e}")
                continue
    return data


def get_time_period(hour: int) -> str:
    """Classify time period based on hour"""
    if 4 <= hour < 12:
        return "🌅 Sáng"
    elif 12 <= hour < 18:
        return "☀️ Chiều"
    else:
        return "🌙 Tối"


def filter_bp_for_week(bp_data: list, start_date: datetime, end_date: datetime) -> list:
    """Filter BP data for a specific week"""
    end_date_inclusive = end_date.replace(hour=23, minute=59, second=59)
    return [
        bp for bp in bp_data 
        if start_date <= bp['measurement_time'] <= end_date_inclusive
    ]


def generate_bp_table(bp_list: list) -> str:
    """Generate markdown table for BP measurements"""
    if not bp_list:
        return "\n> *Không có dữ liệu đo trong tuần này.*\n"
    
    # Sort by measurement time
    bp_list = sorted(bp_list, key=lambda x: x['measurement_time'])
    
    lines = []
    lines.append("\n---\n")
    lines.append("## 📋 Chi tiết các lần đo huyết áp\n")
    lines.append(f"> *Tổng số: {len(bp_list)} lần đo*\n")
    lines.append("")
    lines.append("| # | Ngày | Giờ | Buổi | SYS | DIA | HR | Ghi chú |")
    lines.append("|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|")
    
    for i, bp in enumerate(bp_list, 1):
        date_str = bp['measurement_time'].strftime('%d/%m')
        time_str = bp['measurement_time'].strftime('%H:%M')
        period = get_time_period(bp['measurement_time'].hour)
        notes = bp['notes'][:30] + "..." if len(bp['notes']) > 30 else bp['notes']
        
        lines.append(f"| {i} | {date_str} | {time_str} | {period} | {bp['systolic']} | {bp['diastolic']} | {bp['heart_rate']} | {notes} |")
    
    lines.append("")
    return "\n".join(lines)


def has_bp_detail_section(content: str) -> bool:
    """Check if file already has BP detail section"""
    return "## 📋 Chi tiết các lần đo huyết áp" in content


def process_user(user_folder: str):
    """Process all weekly reports for a user"""
    user_path = BASE_PATH / user_folder
    week_path = user_path / "week"
    bp_file = user_path / "user_blood_pressure.csv"
    
    print(f"\n📂 Đang xử lý: {user_folder}")
    
    if not week_path.exists():
        print(f"  ❌ Không tìm thấy thư mục week/")
        return 0
    
    if not bp_file.exists():
        print(f"  ❌ Không tìm thấy file user_blood_pressure.csv")
        return 0
    
    # Load BP data
    bp_data = load_bp_data(bp_file)
    print(f"  📊 Đã tải {len(bp_data)} bản ghi huyết áp")
    
    # Get all week files
    week_files = sorted([f for f in week_path.iterdir() if f.suffix == '.md'])
    print(f"  📁 Tìm thấy {len(week_files)} file báo cáo tuần")
    
    updated_count = 0
    
    for week_file in week_files:
        start_date, end_date = parse_date_range_from_filename(week_file.name)
        if not start_date:
            print(f"  ⚠️ Không parse được filename: {week_file.name}")
            continue
        
        # Read current content
        with open(week_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has BP detail
        if has_bp_detail_section(content):
            print(f"  ⏭️  {week_file.name} - Đã có dữ liệu chi tiết")
            continue
        
        # Filter BP data for this week
        week_bp = filter_bp_for_week(bp_data, start_date, end_date)
        
        # Generate BP table
        bp_table = generate_bp_table(week_bp)
        
        # Append to file
        new_content = content.rstrip() + "\n" + bp_table
        
        with open(week_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✅ {week_file.name} - Thêm {len(week_bp)} bản ghi")
        updated_count += 1
    
    return updated_count


def main():
    print("=" * 60)
    print("🩺 BỔ SUNG DỮ LIỆU ĐO HUYẾT ÁP VÀO BÁO CÁO TUẦN")
    print("=" * 60)
    
    total_updated = 0
    
    for user in USERS:
        updated = process_user(user)
        total_updated += updated
    
    print("\n" + "=" * 60)
    print(f"✅ HOÀN TẤT: Đã cập nhật {total_updated} file báo cáo tuần")
    print("=" * 60)


if __name__ == "__main__":
    main()
