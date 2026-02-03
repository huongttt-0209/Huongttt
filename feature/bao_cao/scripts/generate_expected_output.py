#!/usr/bin/env python3
"""
BP Expected Output Generator
Generates expected test output CSV files based on input data and BR-005/BR-006 formulas.

Usage:
    python generate_expected_output.py --period week --start 2026-01-19 --end 2026-01-25
    python generate_expected_output.py --period month --start 2026-01-01 --end 2026-01-31
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import argparse
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, '..', 'csv', 'full_test')
OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'csv', 'full_test')

# User profile mapping
PROFILE_MAP = {
    1: 'THA_diagnosed',
    2: 'cao_chua_cdoan', 
    3: 'binh_thuong',
    4: 'ko_on_dinh',
    5: 'ha_thap',
    6: 'khong_ro'
}


def load_data():
    """Load all input CSV files"""
    users = pd.read_csv(os.path.join(INPUT_DIR, 'users.csv'))
    profiles = pd.read_csv(os.path.join(INPUT_DIR, 'user_health_profiles.csv'))
    bp = pd.read_csv(os.path.join(INPUT_DIR, 'user_blood_pressure.csv'))
    bp['measurement_time'] = pd.to_datetime(bp['measurement_time'])
    
    # Try to load events, may not exist
    events_path = os.path.join(INPUT_DIR, 'events.csv')
    events = pd.read_csv(events_path) if os.path.exists(events_path) else None
    
    return users, profiles, bp, events


def filter_bp_by_period(bp_df, start_date, end_date):
    """Filter BP data by date range"""
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date) + timedelta(days=1) - timedelta(seconds=1)
    return bp_df[(bp_df['measurement_time'] >= start) & (bp_df['measurement_time'] <= end)]


def calc_kiem_soat(bp_user, profile):
    """Calculate control rate for THA diagnosed users (has_hypertension=1)"""
    if len(bp_user) == 0:
        return None, None, None
    
    sys_lower = profile['systolic_threshold_lower']
    sys_upper = profile['systolic_threshold_upper']
    dia_lower = profile['diastolic_threshold_lower']  
    dia_upper = profile['diastolic_threshold_upper']
    
    if pd.isna(sys_lower) or pd.isna(sys_upper):
        return None, None, None
    
    in_range = bp_user[
        (bp_user['systolic'] >= sys_lower) & 
        (bp_user['systolic'] <= sys_upper) &
        (bp_user['diastolic'] >= dia_lower) & 
        (bp_user['diastolic'] <= dia_upper)
    ]
    
    total = len(bp_user)
    in_count = len(in_range)
    rate = (in_count / total) * 100
    
    # Classification
    if rate > 70:
        result = "Kiểm soát tối ưu"
    elif rate >= 50:
        result = "Kiểm soát tốt"
    elif rate >= 25:
        result = "Kiểm soát kém"
    else:
        result = "Không được kiểm soát"
    
    calc_str = f"{in_count}/{total}*100%"
    return rate, result, calc_str


def calc_bp_load(bp_user):
    """Calculate BP load for non-THA users (has_hypertension=2,3,4,5,6)"""
    if len(bp_user) == 0:
        return None, None, None
    
    over_threshold = bp_user[
        (bp_user['systolic'] > 140) | (bp_user['diastolic'] > 90)
    ]
    
    total = len(bp_user)
    over_count = len(over_threshold)
    rate = (over_count / total) * 100
    
    # Classification
    if rate > 30:
        result = "Gánh nặng lớn"
    elif rate >= 15:
        result = "Chớm cao"
    else:
        result = "Bình thường"
    
    calc_str = f"{over_count}/{total}*100%"
    return rate, result, calc_str


def calc_hypotension_load(bp_user):
    """Calculate hypotension load for ha_thap users (has_hypertension=5)"""
    if len(bp_user) == 0:
        return None, None, None
    
    under_threshold = bp_user[
        (bp_user['systolic'] < 90) | (bp_user['diastolic'] < 60)
    ]
    
    total = len(bp_user)
    under_count = len(under_threshold)
    rate = (under_count / total) * 100
    
    # Classification
    if rate > 30:
        result = "Rủi ro tụt huyết áp"
    elif rate >= 15:
        result = "Thường xuyên thấp"
    else:
        result = "Ít khi thấp"
    
    calc_str = f"{under_count}/{total}*100%"
    return rate, result, calc_str


def calc_arv(bp_user):
    """Calculate Average Real Variability"""
    if len(bp_user) < 2:
        return None, None, None
    
    sorted_bp = bp_user.sort_values('measurement_time')
    sys_values = sorted_bp['systolic'].values
    
    deltas = np.abs(np.diff(sys_values))
    arv = np.sum(deltas) / (len(sys_values) - 1)
    
    # Classification
    if arv < 10:
        result = "Ổn định"
    elif arv <= 14:
        result = "Biến động"
    else:
        result = "Bất ổn"
    
    calc_str = f"Σ|ΔSYSᵢ|/(n-1)={int(np.sum(deltas))}/{len(sys_values)-1}"
    return round(arv, 1), result, calc_str


def calc_mediff(bp_user):
    """Calculate Morning-Evening difference"""
    if len(bp_user) == 0:
        return None, None, None
    
    # Morning: 04:00 - 10:00
    morning = bp_user[bp_user['measurement_time'].dt.hour.between(4, 10)]
    # Evening: 20:00 - 23:59
    evening = bp_user[bp_user['measurement_time'].dt.hour >= 20]
    
    if len(morning) == 0 or len(evening) == 0:
        return None, None, None
    
    morning_avg = morning['systolic'].mean()
    evening_avg = evening['systolic'].mean()
    mediff = morning_avg - evening_avg
    
    # Classification
    if mediff > 15:
        result = "Vọt áp buổi sáng"
    elif mediff < -15:
        result = "Tăng áp về tối"
    else:
        result = "Cân bằng"
    
    calc_str = f"{round(morning_avg, 1)} - {round(evening_avg, 1)}"
    return round(mediff, 0), result, calc_str


def calc_trend(bp_current, bp_previous, period_type):
    """Calculate trend vs previous period"""
    if len(bp_current) == 0:
        return None, None, None
    
    current_avg = bp_current['systolic'].mean()
    
    if bp_previous is None or len(bp_previous) == 0:
        return None, None, None
    
    previous_avg = bp_previous['systolic'].mean()
    delta = current_avg - previous_avg
    
    # Classification
    if abs(delta) <= 5:
        result = "Ổn định"
    elif delta > 5:
        result = "Tăng nhẹ"
    else:
        result = "Giảm nhẹ"
    
    calc_str = f"{round(current_avg, 1)} - {round(previous_avg, 1)}"
    return round(delta, 0), result, calc_str


def calc_tuan_thu(bp_user, total_days):
    """Calculate adherence rate"""
    if len(bp_user) == 0:
        return None, None, None
    
    days_with_bp = bp_user['measurement_time'].dt.date.nunique()
    rate = (days_with_bp / total_days) * 100
    
    # Classification
    if rate >= 80:
        result = "Tốt"
    elif rate >= 50:
        result = "Khá"
    else:
        result = "Cần cải thiện"
    
    calc_str = f"{days_with_bp}/{total_days}*100%"
    return round(rate, 1), result, calc_str


def calc_sys_stats(bp_user, profile=None):
    """Calculate SYS statistics (avg, max, min)"""
    if len(bp_user) == 0:
        return None, None, None, None, None, None
    
    sys_avg = bp_user['systolic'].mean()
    sys_max = bp_user['systolic'].max()
    sys_min = bp_user['systolic'].min()
    
    # Matching diastolic for max/min
    max_idx = bp_user['systolic'].idxmax()
    min_idx = bp_user['systolic'].idxmin()
    dia_at_max = bp_user.loc[max_idx, 'diastolic']
    dia_at_min = bp_user.loc[min_idx, 'diastolic']
    
    return (
        round(sys_avg, 1), f"Σ(SYS)/{len(bp_user)}",
        int(sys_max), dia_at_max,
        int(sys_min), dia_at_min
    )


def generate_expected_output(period_type, start_date, end_date, prev_start=None, prev_end=None):
    """Generate expected output for all users"""
    users, profiles, bp, events = load_data()
    
    # Calculate previous period if not provided
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)
    
    if period_type == 'week':
        if prev_start is None:
            prev_start = start - timedelta(days=7)
            prev_end = start - timedelta(days=1)
    else:  # month
        if prev_start is None:
            prev_start = (start - timedelta(days=1)).replace(day=1)
            prev_end = start - timedelta(days=1)
    
    total_days = (end - start).days + 1
    period_str = f"{start_date}~{end_date}"
    
    results = []
    
    for _, user in users.iterrows():
        user_id = user['user_id']
        has_ht = user['has_hypertension']
        profile_name = PROFILE_MAP.get(has_ht, 'unknown')
        
        # Get user's profile thresholds
        user_profile = profiles[profiles['user_id'] == user_id]
        if len(user_profile) > 0:
            user_profile = user_profile.iloc[0]
        else:
            user_profile = None
        
        # Filter BP data for current and previous period
        bp_current = filter_bp_by_period(bp[bp['user_id'] == user_id], start_date, end_date)
        bp_previous = filter_bp_by_period(bp[bp['user_id'] == user_id], prev_start, prev_end)
        
        # Skip users with no data (U10)
        if len(bp_current) == 0:
            continue
        
        # Calculate metrics based on user type
        
        # 1. Control rate or BP load
        if has_ht == 1:  # THA diagnosed
            value, result, calc = calc_kiem_soat(bp_current, user_profile)
            if value is not None:
                results.append({
                    'user_id': user_id,
                    'user_profile': profile_name,
                    'data_type': 'kiem_soat',
                    'metric_name': '% trong ngưỡng mục tiêu',
                    'calculation': calc,
                    'value': f"{value:.1f}%",
                    'expected_result': result,
                    'notes': '>70%' if value > 70 else ('50-70%' if value >= 50 else ('<25%' if value < 25 else '25-50%')),
                    'srs_ref': 'BR-006',
                    'period': period_str
                })
        elif has_ht == 5:  # Low BP
            value, result, calc = calc_hypotension_load(bp_current)
            if value is not None:
                results.append({
                    'user_id': user_id,
                    'user_profile': profile_name,
                    'data_type': 'hypotension_load',
                    'metric_name': '% dưới 90/60',
                    'calculation': calc,
                    'value': f"{value:.1f}%",
                    'expected_result': result,
                    'notes': '>30%' if value > 30 else ('15-30%' if value >= 15 else '<15%'),
                    'srs_ref': 'BR-006',
                    'period': period_str
                })
        else:  # Non-THA
            value, result, calc = calc_bp_load(bp_current)
            if value is not None:
                results.append({
                    'user_id': user_id,
                    'user_profile': profile_name,
                    'data_type': 'bp_load',
                    'metric_name': '% vượt 140/90',
                    'calculation': calc,
                    'value': f"{value:.1f}%",
                    'expected_result': result,
                    'notes': '>30%' if value > 30 else ('15-30%' if value >= 15 else '<15%'),
                    'srs_ref': 'BR-006',
                    'period': period_str
                })
        
        # 2. ARV
        value, result, calc = calc_arv(bp_current)
        if value is not None:
            results.append({
                'user_id': user_id,
                'user_profile': profile_name,
                'data_type': 'arv',
                'metric_name': 'ARV tâm thu',
                'calculation': calc,
                'value': value,
                'expected_result': result,
                'notes': '<10' if value < 10 else ('10-14' if value <= 14 else '>14'),
                'srs_ref': 'BR-006',
                'period': period_str
            })
        
        # 3. MEdiff
        value, result, calc = calc_mediff(bp_current)
        if value is not None:
            results.append({
                'user_id': user_id,
                'user_profile': profile_name,
                'data_type': 'mediff',
                'metric_name': 'ME diff tâm thu',
                'calculation': calc,
                'value': f"+{int(value)}" if value >= 0 else str(int(value)),
                'expected_result': result,
                'notes': '>15 mmHg Morning Surge' if value > 15 else ('<-15 mmHg Risky Evening' if value < -15 else '-15~15 mmHg'),
                'srs_ref': 'BR-006',
                'period': period_str
            })
        
        # 4. Trend
        trend_type = 'xu_huong_tuan' if period_type == 'week' else 'xu_huong_thang'
        value, result, calc = calc_trend(bp_current, bp_previous, period_type)
        if value is not None:
            vs_text = f"vs {prev_start}~{prev_end}" if prev_start else ""
            results.append({
                'user_id': user_id,
                'user_profile': profile_name,
                'data_type': trend_type,
                'metric_name': f"Δ SYS vs {'tuần' if period_type == 'week' else 'tháng'} trước",
                'calculation': calc,
                'value': f"+{int(value)}" if value >= 0 else str(int(value)),
                'expected_result': result,
                'notes': '±5 mmHg',
                'srs_ref': 'BR-005',
                'period': f"{period_str} {vs_text}"
            })
        
        # For monthly reports, add additional metrics
        if period_type == 'month':
            # 5. Adherence rate
            value, result, calc = calc_tuan_thu(bp_current, total_days)
            if value is not None:
                results.append({
                    'user_id': user_id,
                    'user_profile': profile_name,
                    'data_type': 'tuan_thu',
                    'metric_name': 'Tỷ lệ tuân thủ lịch đo',
                    'calculation': calc,
                    'value': f"{value:.1f}%",
                    'expected_result': result,
                    'notes': '>=80% tốt, 50-80% khá',
                    'srs_ref': 'BR-005',
                    'period': period_str
                })
            
            # 6. SYS statistics
            sys_avg, calc_avg, sys_max, dia_max, sys_min, dia_min = calc_sys_stats(bp_current, user_profile)
            if sys_avg is not None:
                results.append({
                    'user_id': user_id,
                    'user_profile': profile_name,
                    'data_type': 'sys_tb',
                    'metric_name': 'SYS trung bình tháng',
                    'calculation': calc_avg,
                    'value': sys_avg,
                    'expected_result': 'Cao' if sys_avg >= 140 else ('Bình thường' if sys_avg < 130 else 'Chớm cao'),
                    'notes': 'mục tiêu <130',
                    'srs_ref': 'BR-005',
                    'period': period_str
                })
                results.append({
                    'user_id': user_id,
                    'user_profile': profile_name,
                    'data_type': 'sys_max',
                    'metric_name': 'SYS cao nhất tháng',
                    'calculation': f"MAX(SYS)",
                    'value': f"{sys_max}/{dia_max}",
                    'expected_result': 'Rất cao' if sys_max >= 160 else ('Cao' if sys_max >= 140 else 'Bình thường'),
                    'notes': '>160 nguy hiểm',
                    'srs_ref': 'BR-005',
                    'period': period_str
                })
                results.append({
                    'user_id': user_id,
                    'user_profile': profile_name,
                    'data_type': 'sys_min',
                    'metric_name': 'SYS thấp nhất tháng',
                    'calculation': f"MIN(SYS)",
                    'value': f"{sys_min}/{dia_min}",
                    'expected_result': 'Thấp' if sys_min < 90 else ('Bình thường' if sys_min < 120 else 'Cao'),
                    'notes': '<90 cần chú ý',
                    'srs_ref': 'BR-005',
                    'period': period_str
                })
    
    return pd.DataFrame(results)


def main():
    parser = argparse.ArgumentParser(description='Generate expected BP test output')
    parser.add_argument('--period', choices=['week', 'month'], required=True, help='Report period type')
    parser.add_argument('--start', required=True, help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end', required=True, help='End date (YYYY-MM-DD)')
    parser.add_argument('--prev-start', help='Previous period start date (optional)')
    parser.add_argument('--prev-end', help='Previous period end date (optional)')
    args = parser.parse_args()
    
    print(f"Generating expected output for {args.period}: {args.start} to {args.end}")
    
    result_df = generate_expected_output(
        args.period, args.start, args.end,
        args.prev_start, args.prev_end
    )
    
    # Generate output filename
    start_parts = args.start.replace('-', '_')
    end_parts = args.end.replace('-', '_')
    output_file = f"test_expected_chi-so_{args.period}_{start_parts}-{end_parts}.csv"
    output_path = os.path.join(OUTPUT_DIR, output_file)
    
    result_df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"Generated: {output_path}")
    print(f"Total records: {len(result_df)}")
    
    # Print summary
    print("\n📊 Summary by user:")
    for user_id in result_df['user_id'].unique():
        user_data = result_df[result_df['user_id'] == user_id]
        print(f"  {user_id[:12]}... - {len(user_data)} metrics")


if __name__ == '__main__':
    main()
