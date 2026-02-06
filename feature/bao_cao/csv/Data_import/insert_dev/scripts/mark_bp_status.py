#!/usr/bin/env python3
"""
Script đánh dấu các lần đo vượt ngưỡng mục tiêu HA trong báo cáo tuần.
Thêm emoji 🔴 cho các lần đo ngoài ngưỡng và ✅ cho trong ngưỡng.
"""

import os
import re
from pathlib import Path

# Đường dẫn gốc
BASE_PATH = Path("/Users/teamai/Downloads/antigravity/koliaa/Huongttt/feature/bao_cao/csv/Data_import/insert_dev")

# Các user cần xử lý
USERS = ["user_tha", "user_bp_load", "user_ha_thap", "user_ko_on_dinh"]


def extract_target_range(content: str) -> tuple:
    """Extract target BP range from report header"""
    # Pattern: "SYS 120-130, DIA 70-80 mmHg" or similar
    sys_pattern = r'SYS\s*(\d+)-(\d+)'
    dia_pattern = r'DIA\s*(\d+)-(\d+)'
    
    sys_match = re.search(sys_pattern, content)
    dia_match = re.search(dia_pattern, content)
    
    if sys_match and dia_match:
        sys_min, sys_max = int(sys_match.group(1)), int(sys_match.group(2))
        dia_min, dia_max = int(dia_match.group(1)), int(dia_match.group(2))
        return (sys_min, sys_max), (dia_min, dia_max)
    
    return None, None


def is_in_range(sys: int, dia: int, sys_range: tuple, dia_range: tuple) -> bool:
    """Check if BP reading is within target range"""
    sys_ok = sys_range[0] <= sys <= sys_range[1]
    dia_ok = dia_range[0] <= dia <= dia_range[1]
    return sys_ok and dia_ok


def mark_bp_readings(filepath: Path) -> tuple:
    """Mark BP readings with status indicators"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract target range
    sys_range, dia_range = extract_target_range(content)
    if not sys_range:
        return 0, 0, "Không tìm thấy ngưỡng mục tiêu"
    
    # Find the BP detail table
    if "## 📋 Chi tiết các lần đo huyết áp" not in content:
        return 0, 0, "Không có bảng chi tiết"
    
    # Pattern to match table rows: | 1 | 01/12 | 13:30 | ☀️ Chiều | 124 | 76 | 68 | notes |
    # Updated to also handle already marked rows
    row_pattern = r'\|\s*(\d+)\s*\|\s*(\d+/\d+)\s*\|\s*(\d+:\d+)\s*\|\s*([^|]+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([^|]*)\s*\|'
    
    in_count = 0
    out_count = 0
    
    def replace_row(match):
        nonlocal in_count, out_count
        
        num = match.group(1)
        date = match.group(2)
        time = match.group(3)
        period = match.group(4).strip()
        sys = int(match.group(5))
        dia = int(match.group(6))
        hr = int(match.group(7))
        notes = match.group(8).strip()
        
        # Remove existing markers from notes if any
        notes_clean = re.sub(r'^[✅🔴⚠️]\s*', '', notes)
        
        if is_in_range(sys, dia, sys_range, dia_range):
            status = "✅"
            in_count += 1
        else:
            status = "🔴"
            out_count += 1
        
        # Add status to beginning of notes
        new_notes = f"{status} {notes_clean}" if notes_clean else status
        
        return f"| {num} | {date} | {time} | {period} | {sys} | {dia} | {hr} | {new_notes} |"
    
    new_content = re.sub(row_pattern, replace_row, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return in_count, out_count, f"Ngưỡng: SYS {sys_range[0]}-{sys_range[1]}, DIA {dia_range[0]}-{dia_range[1]}"


def process_user(user_folder: str) -> dict:
    """Process all weekly reports for a user"""
    user_path = BASE_PATH / user_folder
    week_path = user_path / "week"
    
    print(f"\n📂 Đang xử lý: {user_folder}")
    
    if not week_path.exists():
        print(f"  ❌ Không tìm thấy thư mục week/")
        return {"updated": 0, "in_range": 0, "out_range": 0}
    
    # Get all week files
    week_files = sorted([f for f in week_path.iterdir() if f.suffix == '.md'])
    
    total_in = 0
    total_out = 0
    updated = 0
    
    for week_file in week_files:
        in_count, out_count, info = mark_bp_readings(week_file)
        
        if in_count + out_count > 0:
            print(f"  ✅ {week_file.name}: {in_count} ✅ | {out_count} 🔴 ({info})")
            total_in += in_count
            total_out += out_count
            updated += 1
        else:
            print(f"  ⏭️  {week_file.name}: {info}")
    
    return {"updated": updated, "in_range": total_in, "out_range": total_out}


def main():
    print("=" * 70)
    print("🎯 ĐÁNH DẤU CÁC LẦN ĐO VƯỢT NGƯỠNG MỤC TIÊU")
    print("=" * 70)
    print("   ✅ = Trong ngưỡng mục tiêu")
    print("   🔴 = Vượt ngưỡng mục tiêu")
    print("=" * 70)
    
    total_stats = {"updated": 0, "in_range": 0, "out_range": 0}
    
    for user in USERS:
        stats = process_user(user)
        total_stats["updated"] += stats["updated"]
        total_stats["in_range"] += stats["in_range"]
        total_stats["out_range"] += stats["out_range"]
    
    total_readings = total_stats["in_range"] + total_stats["out_range"]
    in_pct = (total_stats["in_range"] / total_readings * 100) if total_readings > 0 else 0
    out_pct = (total_stats["out_range"] / total_readings * 100) if total_readings > 0 else 0
    
    print("\n" + "=" * 70)
    print("📊 TỔNG KẾT")
    print("=" * 70)
    print(f"   📁 File đã cập nhật: {total_stats['updated']}")
    print(f"   ✅ Trong ngưỡng: {total_stats['in_range']} ({in_pct:.1f}%)")
    print(f"   🔴 Ngoài ngưỡng: {total_stats['out_range']} ({out_pct:.1f}%)")
    print("=" * 70)


if __name__ == "__main__":
    main()
