#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Verification script for Blood Pressure metrics calculation
Compares input data against expected output based on DATA_DICTIONARY.md formulas
"""

import csv
from datetime import datetime
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def load_bp_data():
    """Load blood pressure data from CSV"""
    bp_data = []
    with open('user_blood_pressure.csv', 'r', encoding='latin-1') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                dt = datetime.strptime(row['measurement_time'].strip(), '%Y-%m-%d %H:%M:%S')
                bp_data.append({
                    'user_id': row['user_id'].strip(),
                    'sys': int(row['systolic']),
                    'dia': int(row['diastolic']),
                    'time': dt
                })
            except Exception as e:
                pass
    return bp_data

def load_expected_week():
    """Load expected week data"""
    data = {}
    with open('test_expected_chi-so_week_2026_1_19-2026_1_25.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row['user_id'], row['data_type'])
            data[key] = {
                'value': row['value'],
                'calculation': row['calculation'],
                'expected_result': row['expected_result']
            }
    return data

def load_expected_month():
    """Load expected month data"""
    data = {}
    with open('test_expected_chi-so_month_2026_1_1-2026_1_31.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row['user_id'], row['data_type'])
            data[key] = {
                'value': row['value'],
                'calculation': row['calculation'],
                'expected_result': row['expected_result']
            }
    return data

def load_thresholds():
    """Load user health profile thresholds"""
    thresholds = {}
    with open('user_health_profiles.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            uid = row['user_id'].strip()
            thresholds[uid] = {
                'sys_lower': int(row['systolic_threshold_lower']) if row['systolic_threshold_lower'] else None,
                'sys_upper': int(row['systolic_threshold_upper']) if row['systolic_threshold_upper'] else None,
                'dia_lower': int(row['diastolic_threshold_lower']) if row['diastolic_threshold_lower'] else None,
                'dia_upper': int(row['diastolic_threshold_upper']) if row['diastolic_threshold_upper'] else None,
            }
    return thresholds

def load_users():
    """Load users data"""
    users = {}
    with open('users.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            uid = row['user_id'].strip()
            users[uid] = {
                'has_hypertension': int(row['has_hypertension'])
            }
    return users

def filter_by_period(bp_data, user_id, start, end):
    """Filter BP data by user and period"""
    return [bp for bp in bp_data if bp['user_id'] == user_id and start <= bp['time'] <= end]

def calc_kiem_soat(bp_list, thresholds):
    """Calculate % trong nguong muc tieu (for THA diagnosed)"""
    if not bp_list or not thresholds['sys_lower']:
        return None, None, None
    in_range = sum(1 for bp in bp_list 
                   if thresholds['sys_lower'] <= bp['sys'] <= thresholds['sys_upper'] 
                   and thresholds['dia_lower'] <= bp['dia'] <= thresholds['dia_upper'])
    total = len(bp_list)
    pct = round(in_range / total * 100, 1)
    return in_range, total, pct

def calc_bp_load(bp_list):
    """Calculate % vuot 140/90 (for non-THA diagnosed)"""
    if not bp_list:
        return None, None, None
    over = sum(1 for bp in bp_list if bp['sys'] > 140 or bp['dia'] > 90)
    total = len(bp_list)
    pct = round(over / total * 100, 1)
    return over, total, pct

def calc_arv(bp_list):
    """Calculate Average Real Variability"""
    if len(bp_list) < 2:
        return None, None, None
    sorted_bp = sorted(bp_list, key=lambda x: x['time'])
    arv_sum = sum(abs(sorted_bp[i+1]['sys'] - sorted_bp[i]['sys']) for i in range(len(sorted_bp)-1))
    n_minus_1 = len(sorted_bp) - 1
    arv = round(arv_sum / n_minus_1, 1)
    return arv_sum, n_minus_1, arv

def calc_mediff(bp_list):
    """Calculate Morning-Evening Difference
    Morning: 04:00-10:00, Evening: 20:00-00:00
    """
    morning = [bp for bp in bp_list if 4 <= bp['time'].hour < 10]
    evening = [bp for bp in bp_list if 20 <= bp['time'].hour <= 23]
    
    if not morning or not evening:
        return None, None, None
    
    morning_avg = sum(bp['sys'] for bp in morning) / len(morning)
    evening_avg = sum(bp['sys'] for bp in evening) / len(evening)
    diff = round(morning_avg - evening_avg)
    
    return round(morning_avg, 1), round(evening_avg, 1), diff

def main():
    print("=" * 80)
    print("BLOOD PRESSURE METRICS VERIFICATION")
    print("Based on DATA_DICTIONARY.md formulas")
    print("=" * 80)
    
    bp_data = load_bp_data()
    thresholds = load_thresholds()
    users = load_users()
    expected_week = load_expected_week()
    expected_month = load_expected_month()
    
    # Define periods
    week_start = datetime(2026, 1, 19, 0, 0, 0)
    week_end = datetime(2026, 1, 25, 23, 59, 59)
    month_start = datetime(2026, 1, 1, 0, 0, 0)
    month_end = datetime(2026, 1, 31, 23, 59, 59)
    
    user_ids = [
        '00000001-0000-0000-0000-000000000001',
        '00000005-0000-0000-0000-000000000005',
        '00000006-0000-0000-0000-000000000006',
        '00000007-0000-0000-0000-000000000007'
    ]
    
    profile_map = {1: 'THA_diagnosed', 2: 'cao_chua_cdoan', 3: 'binh_thuong', 4: 'ko_on_dinh'}
    
    issues = []
    
    for uid in user_ids:
        user_short = uid[-1]
        profile = users.get(uid, {}).get('has_hypertension', 0)
        profile_name = profile_map.get(profile, 'unknown')
        
        print(f"\n{'='*60}")
        print(f"USER {user_short} ({uid})")
        print(f"Profile: {profile_name} (has_hypertension={profile})")
        print("=" * 60)
        
        # Get data for both periods
        week_bp = filter_by_period(bp_data, uid, week_start, week_end)
        month_bp = filter_by_period(bp_data, uid, month_start, month_end)
        
        print(f"\n📊 Week Data (2026-01-19 ~ 2026-01-25): {len(week_bp)} measurements")
        print(f"📊 Month Data (2026-01-01 ~ 2026-01-31): {len(month_bp)} measurements")
        
        # ============ WEEK CALCULATIONS ============
        print(f"\n--- WEEK CALCULATIONS ---")
        
        if profile == 1:  # THA diagnosed -> kiem_soat
            in_range, total, pct = calc_kiem_soat(week_bp, thresholds.get(uid, {}))
            expected = expected_week.get((uid, 'kiem_soat'), {})
            print(f"\n[kiem_soat] Week:")
            print(f"  Calculated: {in_range}/{total}*100% = {pct}%")
            print(f"  Expected:   {expected.get('calculation')} = {expected.get('value')}")
            if str(pct) + "%" != expected.get('value', ''):
                issues.append(f"u{user_short} week kiem_soat: calc={pct}% vs exp={expected.get('value')}")
        else:  # bp_load
            over, total, pct = calc_bp_load(week_bp)
            expected = expected_week.get((uid, 'bp_load'), {})
            print(f"\n[bp_load] Week:")
            print(f"  Calculated: {over}/{total}*100% = {pct}%")
            print(f"  Expected:   {expected.get('calculation')} = {expected.get('value')}")
            if str(pct) + "%" != expected.get('value', ''):
                issues.append(f"u{user_short} week bp_load: calc={pct}% vs exp={expected.get('value')}")
        
        # ARV Week
        arv_sum, n_minus_1, arv = calc_arv(week_bp)
        expected = expected_week.get((uid, 'arv'), {})
        print(f"\n[arv] Week:")
        print(f"  Calculated: Σ|ΔSYS|/(n-1) = {arv_sum}/{n_minus_1} = {arv}")
        print(f"  Expected:   {expected.get('calculation')} = {expected.get('value')}")
        
        # MEdiff Week
        m_avg, e_avg, diff = calc_mediff(week_bp)
        expected = expected_week.get((uid, 'mediff'), {})
        print(f"\n[mediff] Week:")
        print(f"  Calculated: {m_avg} - {e_avg} = {diff:+d}")
        print(f"  Expected:   {expected.get('calculation')} = {expected.get('value')}")
        
        # ============ MONTH CALCULATIONS ============
        print(f"\n--- MONTH CALCULATIONS ---")
        
        if profile == 1:  # THA diagnosed -> kiem_soat
            in_range, total, pct = calc_kiem_soat(month_bp, thresholds.get(uid, {}))
            expected = expected_month.get((uid, 'kiem_soat'), {})
            print(f"\n[kiem_soat] Month:")
            print(f"  Calculated: {in_range}/{total}*100% = {pct}%")
            print(f"  Expected:   {expected.get('calculation')} = {expected.get('value')}")
            if str(pct) + "%" != expected.get('value', ''):
                issues.append(f"u{user_short} month kiem_soat: calc={pct}% vs exp={expected.get('value')}")
        else:  # bp_load
            over, total, pct = calc_bp_load(month_bp)
            expected = expected_month.get((uid, 'bp_load'), {})
            print(f"\n[bp_load] Month:")
            print(f"  Calculated: {over}/{total}*100% = {pct}%")
            print(f"  Expected:   {expected.get('calculation')} = {expected.get('value')}")
            if str(pct) + "%" != expected.get('value', ''):
                issues.append(f"u{user_short} month bp_load: calc={pct}% vs exp={expected.get('value')}")
        
        # ARV Month
        arv_sum, n_minus_1, arv = calc_arv(month_bp)
        expected = expected_month.get((uid, 'arv'), {})
        print(f"\n[arv] Month:")
        print(f"  Calculated: Σ|ΔSYS|/(n-1) = {arv_sum}/{n_minus_1} = {arv}")
        print(f"  Expected:   {expected.get('calculation')} = {expected.get('value')}")
        
        # MEdiff Month
        m_avg, e_avg, diff = calc_mediff(month_bp)
        expected = expected_month.get((uid, 'mediff'), {})
        print(f"\n[mediff] Month:")
        print(f"  Calculated: {m_avg} - {e_avg} = {diff:+d}")
        print(f"  Expected:   {expected.get('calculation')} = {expected.get('value')}")
    
    print("\n" + "=" * 80)
    print("VERIFICATION SUMMARY")
    print("=" * 80)
    if issues:
        print(f"\n⚠️  FOUND {len(issues)} DISCREPANCIES:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("\n✅ ALL CALCULATIONS MATCH!")

if __name__ == "__main__":
    main()
