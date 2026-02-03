#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate individual user folders with all related data files
Creates: user1, user2, ... user16 folders with users.csv, profiles.csv, bp.csv, events.csv, expected_*.csv
"""

import csv
import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, 'full_test')
OUTPUT_DIR = os.path.join(BASE_DIR, 'Data_import')

def load_csv(filename, encoding='utf-8'):
    """Load CSV file and return list of dicts"""
    filepath = os.path.join(INPUT_DIR, filename)
    data = []
    with open(filepath, 'r', encoding=encoding) as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            data.append(row)
    return data, fieldnames

def write_csv(filepath, data, fieldnames):
    """Write list of dicts to CSV file"""
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    # Load all source data
    print("📂 Loading source files...")
    users, users_fields = load_csv('users.csv')
    profiles, profiles_fields = load_csv('user_health_profiles.csv')
    bp_data, bp_fields = load_csv('user_blood_pressure.csv')
    events, events_fields = load_csv('events.csv')
    expected_week, week_fields = load_csv('test_expected_chi-so_week_2026_01_19-2026_01_25.csv', 'utf-8-sig')
    expected_month, month_fields = load_csv('test_expected_chi-so_month_2026_01_01-2026_01_31.csv', 'utf-8-sig')
    
    print(f"  ✓ users.csv: {len(users)} users")
    print(f"  ✓ user_health_profiles.csv: {len(profiles)} profiles")
    print(f"  ✓ user_blood_pressure.csv: {len(bp_data)} records")
    print(f"  ✓ events.csv: {len(events)} events")
    print(f"  ✓ expected_week: {len(expected_week)} records")
    print(f"  ✓ expected_month: {len(expected_month)} records")
    
    # Create user folders
    print("\n📁 Creating user folders...")
    
    for idx, user in enumerate(users, start=1):
        user_id = user['user_id']
        folder_name = f"user{idx}"
        folder_path = os.path.join(OUTPUT_DIR, folder_name)
        
        # Create folder
        os.makedirs(folder_path, exist_ok=True)
        
        # 1. User info
        user_data = [user]
        write_csv(os.path.join(folder_path, 'users.csv'), user_data, users_fields)
        
        # 2. Health profile
        user_profiles = [p for p in profiles if p['user_id'] == user_id]
        write_csv(os.path.join(folder_path, 'user_health_profiles.csv'), user_profiles, profiles_fields)
        
        # 3. Blood pressure data
        user_bp = [bp for bp in bp_data if bp['user_id'] == user_id]
        write_csv(os.path.join(folder_path, 'user_blood_pressure.csv'), user_bp, bp_fields)
        
        # 4. Events
        user_events = [e for e in events if e['user_id'] == user_id]
        write_csv(os.path.join(folder_path, 'events.csv'), user_events, events_fields)
        
        # 5. Expected week
        user_exp_week = [e for e in expected_week if e['user_id'] == user_id]
        write_csv(os.path.join(folder_path, 'expected_chi-so_week.csv'), user_exp_week, week_fields)
        
        # 6. Expected month
        user_exp_month = [e for e in expected_month if e['user_id'] == user_id]
        write_csv(os.path.join(folder_path, 'expected_chi-so_month.csv'), user_exp_month, month_fields)
        
        print(f"  ✅ {folder_name}: {user['full_name']} ({len(user_bp)} BP, {len(user_events)} events)")
    
    print(f"\n🎉 Created {len(users)} user folders in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
