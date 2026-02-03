#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate individual user files from users.csv and user_health_profiles.csv
Output: CSV format with 0797 phone prefix
"""

import csv
import os
from datetime import datetime

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_CSV = os.path.join(BASE_DIR, 'full_test', 'users.csv')
PROFILES_CSV = os.path.join(BASE_DIR, 'full_test', 'user_health_profiles.csv')
OUTPUT_DIR = os.path.join(BASE_DIR, 'Data_import', 'user')

# Mapping has_hypertension to tinh_trang_THA
THA_MAP = {
    1: 'THA đã chẩn đoán',
    2: 'Cao chưa chẩn đoán', 
    3: 'Bình thường',
    4: 'Không ổn định',
    5: 'Huyết áp thấp',
    6: 'Không rõ'
}

# Sample disease data for variety
DISEASE_DATA = {
    '00000001': 'Tăng huyết áp, Tiểu đường type 2',
    '00000002': 'Tăng huyết áp',
    '00000003': 'Tăng huyết áp, Bệnh tim mạch',
    '00000004': 'Tăng huyết áp, Suy thận',
    '00000005': '',
    '00000006': '',
    '00000007': 'Rối loạn lipid máu',
    '00000008': 'Thiếu máu',
    '00000009': '',
    '00000010': '',
    '00000011': 'Tăng huyết áp',
    '00000012': 'Huyết áp thấp',
    '00000013': 'Huyết áp thấp, Thiếu máu',
    '00000014': 'Tăng huyết áp',
    '00000015': 'Tăng huyết áp, Béo phì',
    '00000016': 'Tăng huyết áp'
}

def convert_phone(old_phone):
    """Convert phone from 0901xxxxxx to 0797xxxxxx"""
    if old_phone.startswith('0901'):
        return '0797' + old_phone[4:]
    return old_phone

def load_users():
    users = {}
    with open(USERS_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            uid = row['user_id'].strip()
            old_phone = row['phone']
            new_phone = convert_phone(old_phone)
            users[uid] = {
                'phone': new_phone,
                'name': row['full_name'],
                'dob': row['date_of_birth'],
                'gender': 'Nam' if row['gender'] == 'male' else 'Nữ',
                'has_hypertension': int(row['has_hypertension'])
            }
    return users

def load_profiles():
    profiles = {}
    with open(PROFILES_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            uid = row['user_id'].strip()
            profiles[uid] = {
                'height': row['height_cm'] if row['height_cm'] else '',
                'weight': row['weight_kg'] if row['weight_kg'] else ''
            }
    return profiles

def create_user_file(user_id, user_data, profile_data, output_dir):
    """Create individual user CSV file"""
    
    # Extract short ID for disease lookup
    short_id = user_id[:8]
    
    # Get THA status
    tinh_trang = THA_MAP.get(user_data['has_hypertension'], 'Không rõ')
    
    # Pregnancy: only for female, set to Không
    pregnancy = 'Không' if user_data['gender'] == 'Nữ' else ''
    
    # Diseases
    diseases = DISEASE_DATA.get(short_id, '')
    
    # Generate filename using phone number
    filename = f"user_{user_data['phone']}.csv"
    filepath = os.path.join(output_dir, filename)
    
    # Write CSV file
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        # Header row
        writer.writerow(['Trường', 'Giá trị', 'Ghi chú'])
        # Data rows
        writer.writerow(['Số điện thoại', user_data['phone'], '✓'])
        writer.writerow(['Tên', user_data['name'], ''])
        writer.writerow(['Tuổi (format: YYYY-MM-DD)', user_data['dob'], ''])
        writer.writerow(['Giới tính', user_data['gender'], ''])
        writer.writerow(['tinh_trang_THA', tinh_trang, ''])
        writer.writerow(['Mang thai / Cho con bú', pregnancy, ''])
        writer.writerow(['Bệnh nền', diseases, ''])
        writer.writerow(['Chiều cao (cm)', profile_data.get('height', ''), ''])
        writer.writerow(['Cân nặng (kg)', profile_data.get('weight', ''), ''])
    
    print(f"✅ Created: {filename}")
    return filename

def main():
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Clean old files
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith('.txt') or f.endswith('.csv'):
            os.remove(os.path.join(OUTPUT_DIR, f))
    
    # Load data
    users = load_users()
    profiles = load_profiles()
    
    print(f"📁 Loading {len(users)} users...")
    print(f"📂 Output directory: {OUTPUT_DIR}")
    print(f"📞 Phone format: 0797xxxxxx")
    print("-" * 50)
    
    created_files = []
    for user_id, user_data in users.items():
        profile_data = profiles.get(user_id, {})
        filename = create_user_file(user_id, user_data, profile_data, OUTPUT_DIR)
        created_files.append(filename)
    
    print("-" * 50)
    print(f"🎉 Created {len(created_files)} CSV files!")

if __name__ == "__main__":
    main()
