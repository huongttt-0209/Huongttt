#!/usr/bin/env python3
"""
Script xác minh toàn bộ dữ liệu tính toán trong các báo cáo tuần/tháng
dựa trên DATA_DICTIONARY.md

Kiểm tra:
1. kiem_soat (% trong ngưỡng mục tiêu) - cho has_hypertension=1
2. bp_load (% vượt 140/90) - cho has_hypertension=2,3,4,5
3. ARV (độ ổn định)
4. ME diff (nhịp sinh học)
5. Các chỉ số cơ bản: HA TB, Cao nhất, Thấp nhất, HR
"""

import os
import re
import csv
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import json

BASE_PATH = Path("/Users/teamai/Downloads/antigravity/koliaa/Huongttt/feature/bao_cao/csv/Data_import/insert_dev")

# User configurations based on DATA_DICTIONARY
USERS = {
    "user_tha": {
        "has_hypertension": 1,
        "metric_type": "kiem_soat",  # % trong ngưỡng mục tiêu
        "target_sys": (120, 130),
        "target_dia": (70, 80),
    },
    "user_bp_load": {
        "has_hypertension": 5,
        "metric_type": "kiem_soat",  # Có ngưỡng mục tiêu cá nhân
        "target_sys": (120, 140),
        "target_dia": (70, 90),
    },
    "user_ha_thap": {
        "has_hypertension": 2,
        "metric_type": "kiem_soat",  # Có ngưỡng cá nhân
        "target_sys": (120, 140),
        "target_dia": (70, 90),
    },
    "user_ko_on_dinh": {
        "has_hypertension": 3,
        "metric_type": "bp_load",  # Không có ngưỡng → dùng BP Load (>140/90)
        "target_sys": None,
        "target_dia": None,
    },
}


def load_bp_data(filepath: Path) -> List[Dict]:
    """Load blood pressure data from CSV"""
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
            except:
                continue
    return sorted(data, key=lambda x: x['measurement_time'])


def calculate_metrics(bp_list: List[Dict], config: Dict) -> Dict:
    """Calculate all metrics for a BP dataset"""
    if not bp_list:
        return {}
    
    n = len(bp_list)
    bp_sorted = sorted(bp_list, key=lambda x: x['measurement_time'])
    
    # Basic stats
    sys_values = [bp['systolic'] for bp in bp_sorted]
    dia_values = [bp['diastolic'] for bp in bp_sorted]
    hr_values = [bp['heart_rate'] for bp in bp_sorted]
    
    avg_sys = sum(sys_values) / n
    avg_dia = sum(dia_values) / n
    avg_hr = sum(hr_values) / n
    
    max_sys = max(sys_values)
    min_sys = min(sys_values)
    max_hr = max(hr_values)
    min_hr = min(hr_values)
    
    # Find max/min BP pairs
    max_idx = sys_values.index(max_sys)
    min_idx = sys_values.index(min_sys)
    max_bp = bp_sorted[max_idx]
    min_bp = bp_sorted[min_idx]
    
    # Calculate kiem_soat or bp_load
    if config['metric_type'] == 'kiem_soat' and config['target_sys']:
        # kiem_soat: % trong ngưỡng mục tiêu
        in_range = sum(1 for bp in bp_sorted 
                      if config['target_sys'][0] <= bp['systolic'] <= config['target_sys'][1]
                      and config['target_dia'][0] <= bp['diastolic'] <= config['target_dia'][1])
        pct_metric = (in_range / n) * 100
        metric_name = "kiem_soat"
    else:
        # bp_load: % vượt 140/90
        over_140_90 = sum(1 for bp in bp_sorted 
                         if bp['systolic'] > 140 or bp['diastolic'] > 90)
        pct_metric = (over_140_90 / n) * 100
        metric_name = "bp_load"
    
    # ARV
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
    
    # Days with measurements
    days = len(set(bp['measurement_time'].date() for bp in bp_sorted))
    
    return {
        "count": n,
        "days": days,
        "avg_sys": round(avg_sys),
        "avg_dia": round(avg_dia),
        "avg_hr": round(avg_hr),
        "max_sys": max_sys,
        "max_dia": max_bp['diastolic'],
        "min_sys": min_sys,
        "min_dia": min_bp['diastolic'],
        "max_hr": max_hr,
        "min_hr": min_hr,
        "metric_name": metric_name,
        "pct_metric": round(pct_metric, 1),
        "arv": round(arv, 1),
        "me_diff": round(me_diff),
        "arv_pairs": len(arv_diffs),
    }


def extract_report_values(filepath: Path) -> Dict:
    """Extract calculated values from a report file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    values = {}
    
    # HA Trung bình
    match = re.search(r'\*\*HA Trung bình\*\*\s*\|\s*(\d+)/(\d+)\s*mmHg', content)
    if match:
        values['avg_sys'] = int(match.group(1))
        values['avg_dia'] = int(match.group(2))
    
    # HA Cao nhất
    match = re.search(r'\*\*HA Cao nhất\*\*\s*\|\s*(\d+)/(\d+)\s*mmHg', content)
    if match:
        values['max_sys'] = int(match.group(1))
        values['max_dia'] = int(match.group(2))
    
    # HA Thấp nhất
    match = re.search(r'\*\*HA Thấp nhất\*\*\s*\|\s*(\d+)/(\d+)\s*mmHg', content)
    if match:
        values['min_sys'] = int(match.group(1))
        values['min_dia'] = int(match.group(2))
    
    # Nhịp tim TB
    match = re.search(r'\*\*Nhịp tim TB\*\*\s*\|\s*(\d+)\s*bpm', content)
    if match:
        values['avg_hr'] = int(match.group(1))
    
    # ARV
    match = re.search(r'\*\*ARV tâm thu\*\*\s*\|\s*([\d.]+)', content)
    if match:
        values['arv'] = float(match.group(1))
    
    # ME diff
    match = re.search(r'\*\*ME diff\*\*\s*\|\s*([+-]?\d+)\s*mmHg', content)
    if match:
        values['me_diff'] = int(match.group(1))
    
    # % trong ngưỡng hoặc bp_load
    match = re.search(r'\*\*% trong ngưỡng\*\*\s*\|\s*([\d.]+)%', content)
    if match:
        values['pct_in_range'] = float(match.group(1))
    
    match = re.search(r'\*\*% bình thường.*?\*\*\s*\|\s*([\d.]+)%', content)
    if match:
        values['pct_normal'] = float(match.group(1))
    
    return values


def compare_values(expected: Dict, actual: Dict, tolerance: float = 0.5) -> List[Dict]:
    """Compare expected vs actual values and return discrepancies"""
    issues = []
    
    comparisons = [
        ('avg_sys', 'HA Trung bình SYS', 1),
        ('avg_dia', 'HA Trung bình DIA', 1),
        ('max_sys', 'HA Cao nhất SYS', 0),
        ('max_dia', 'HA Cao nhất DIA', 0),
        ('min_sys', 'HA Thấp nhất SYS', 0),
        ('min_dia', 'HA Thấp nhất DIA', 0),
        ('avg_hr', 'Nhịp tim TB', 1),
        ('arv', 'ARV', tolerance),
        ('me_diff', 'ME diff', 2),
    ]
    
    for key, name, tol in comparisons:
        if key in expected and key in actual:
            diff = abs(expected[key] - actual[key])
            if diff > tol:
                issues.append({
                    'metric': name,
                    'expected': expected[key],
                    'actual': actual[key],
                    'diff': diff,
                })
    
    return issues


def verify_user(user_name: str, config: Dict) -> Dict:
    """Verify all reports for a user"""
    user_path = BASE_PATH / user_name
    bp_file = user_path / "user_blood_pressure.csv"
    
    results = {
        "user": user_name,
        "config": config,
        "week_reports": [],
        "issues": [],
        "passed": 0,
        "failed": 0,
    }
    
    if not bp_file.exists():
        results["issues"].append("Không tìm thấy file BP")
        return results
    
    bp_data = load_bp_data(bp_file)
    
    # Verify week reports
    week_path = user_path / "week"
    if week_path.exists():
        for wf in sorted(week_path.iterdir()):
            if wf.suffix != '.md':
                continue
            
            # Parse date range
            name = wf.name.replace('.md', '')
            parts = name.split('_')
            if len(parts) != 2:
                continue
            
            try:
                start = datetime.strptime(parts[0], '%Y-%m-%d')
                end = datetime.strptime(parts[1], '%Y-%m-%d')
            except:
                continue
            
            # Filter BP data for this week
            end_inclusive = end.replace(hour=23, minute=59, second=59)
            week_bp = [bp for bp in bp_data if start <= bp['measurement_time'] <= end_inclusive]
            
            if not week_bp:
                continue
            
            # Calculate expected values
            expected = calculate_metrics(week_bp, config)
            
            # Extract actual values from report
            actual = extract_report_values(wf)
            
            # Compare
            issues = compare_values(expected, actual)
            
            report_result = {
                "file": wf.name,
                "count": len(week_bp),
                "expected": expected,
                "actual": actual,
                "issues": issues,
                "passed": len(issues) == 0,
            }
            
            results["week_reports"].append(report_result)
            
            if report_result["passed"]:
                results["passed"] += 1
            else:
                results["failed"] += 1
                results["issues"].extend([f"{wf.name}: {i['metric']}: Expected={i['expected']}, Got={i['actual']}" for i in issues])
    
    return results


def main():
    print("=" * 80)
    print("🔍 XÁC MINH DỮ LIỆU TÍNH TOÁN THEO DATA_DICTIONARY.md")
    print("=" * 80)
    
    all_results = []
    total_passed = 0
    total_failed = 0
    
    for user_name, config in USERS.items():
        print(f"\n📂 {user_name}")
        print(f"   has_hypertension={config['has_hypertension']}, metric={config['metric_type']}")
        
        results = verify_user(user_name, config)
        all_results.append(results)
        
        total_passed += results["passed"]
        total_failed += results["failed"]
        
        if results["issues"]:
            print(f"   ❌ ISSUES FOUND: {len(results['issues'])}")
            for issue in results["issues"][:5]:
                print(f"      • {issue}")
            if len(results["issues"]) > 5:
                print(f"      ... và {len(results['issues'])-5} vấn đề khác")
        else:
            print(f"   ✅ All {results['passed']} reports PASSED")
    
    # Summary
    print("\n" + "=" * 80)
    print("📊 TỔNG KẾT")
    print("=" * 80)
    
    for res in all_results:
        status = "✅" if res["failed"] == 0 else "❌"
        print(f"   {status} {res['user']}: {res['passed']} passed, {res['failed']} failed")
    
    print(f"\n   TOTAL: {total_passed} PASSED, {total_failed} FAILED")
    
    # Write detailed report
    report_path = BASE_PATH / "verification_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        # Convert datetime objects to strings for JSON serialization
        for res in all_results:
            for wr in res["week_reports"]:
                if "expected" in wr:
                    wr["expected"] = {k: str(v) if isinstance(v, datetime) else v for k, v in wr["expected"].items()}
        json.dump(all_results, f, indent=2, ensure_ascii=False, default=str)
    
    print(f"\n   📄 Chi tiết: {report_path}")
    print("=" * 80)


if __name__ == "__main__":
    main()
