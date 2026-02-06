#!/usr/bin/env python3
"""
Script tính lại ME diff (Morning-Evening Difference) sau khi chuyển UTC+7
Theo SRS BR-006:
- Sáng: 04:00 - 10:00
- Tối: 20:00 - 00:00
"""

import os
import csv
from datetime import datetime
from collections import defaultdict

BASE_DIR = "/Users/teamai/Downloads/antigravity/koliaa/Huongttt/feature/bao_cao/csv/Data_import/insert_dev"

# Khung giờ theo SRS
MORNING_START = 4  # 04:00
MORNING_END = 10   # 10:00
EVENING_START = 20 # 20:00
EVENING_END = 24   # 00:00 (midnight)

def parse_datetime(dt_str):
    """Parse datetime string"""
    return datetime.strptime(dt_str.strip(), '%Y-%m-%d %H:%M:%S')

def get_week_key(dt):
    """Tạo key cho tuần (YYYY-WW)"""
    return dt.isocalendar()[:2]  # (year, week)

def is_morning(hour):
    """Kiểm tra có thuộc khung sáng không"""
    return MORNING_START <= hour < MORNING_END

def is_evening(hour):
    """Kiểm tra có thuộc khung tối không"""
    return EVENING_START <= hour < EVENING_END

def calculate_mediff_for_user(user_folder):
    """Tính ME diff cho 1 user"""
    user_path = os.path.join(BASE_DIR, user_folder)
    bp_file = os.path.join(user_path, 'user_blood_pressure.csv')
    
    if not os.path.exists(bp_file):
        return {}
    
    # Đọc dữ liệu
    with open(bp_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    # Group theo tuần và khung giờ
    weekly_data = defaultdict(lambda: {'morning': [], 'evening': []})
    
    for row in rows:
        dt = parse_datetime(row['measurement_time'])
        week_key = get_week_key(dt)
        hour = dt.hour
        sys_val = int(row['systolic'])
        
        if is_morning(hour):
            weekly_data[week_key]['morning'].append(sys_val)
        elif is_evening(hour):
            weekly_data[week_key]['evening'].append(sys_val)
    
    # Tính ME diff cho mỗi tuần
    results = {}
    for week_key, data in sorted(weekly_data.items()):
        morning_vals = data['morning']
        evening_vals = data['evening']
        
        if morning_vals and evening_vals:
            morning_avg = sum(morning_vals) / len(morning_vals)
            evening_avg = sum(evening_vals) / len(evening_vals)
            mediff = round(morning_avg - evening_avg)
            
            # Phân loại
            if mediff > 15:
                classification = "Vọt áp buổi sáng"
            elif mediff < -15:
                classification = "Tăng áp về tối"
            else:
                classification = "Cân bằng"
            
            results[week_key] = {
                'mediff': mediff,
                'classification': classification,
                'morning_count': len(morning_vals),
                'evening_count': len(evening_vals),
                'morning_avg': round(morning_avg, 1),
                'evening_avg': round(evening_avg, 1)
            }
        else:
            results[week_key] = {
                'mediff': None,
                'classification': 'Không đủ dữ liệu',
                'morning_count': len(morning_vals),
                'evening_count': len(evening_vals)
            }
    
    return results

def main():
    print("=" * 60)
    print("TÍNH LẠI ME DIFF SAU CHUYỂN ĐỔI UTC+7")
    print("Khung giờ: Sáng 04:00-10:00, Tối 20:00-00:00")
    print("=" * 60)
    
    for user_folder in sorted(os.listdir(BASE_DIR)):
        user_path = os.path.join(BASE_DIR, user_folder)
        if not os.path.isdir(user_path) or user_folder.startswith('.'):
            continue
        
        print(f"\n{'='*40}")
        print(f"USER: {user_folder}")
        print(f"{'='*40}")
        
        results = calculate_mediff_for_user(user_folder)
        
        for week_key, data in sorted(results.items()):
            year, week = week_key
            if data['mediff'] is not None:
                print(f"  Tuần {week}/{year}: ME diff = {data['mediff']:+d} mmHg → {data['classification']}")
                print(f"    Sáng: {data['morning_count']} lần (TB={data['morning_avg']}), Tối: {data['evening_count']} lần (TB={data['evening_avg']})")
            else:
                print(f"  Tuần {week}/{year}: {data['classification']}")
                print(f"    Sáng: {data['morning_count']} lần, Tối: {data['evening_count']} lần")

if __name__ == '__main__':
    main()
