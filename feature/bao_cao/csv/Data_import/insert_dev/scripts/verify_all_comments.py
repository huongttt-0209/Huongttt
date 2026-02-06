#!/usr/bin/env python3
"""
Script kiểm tra toàn bộ tiêu chí nhận xét trong báo cáo user_bp_load.

Các tiêu chí cần kiểm tra:
1. Tỷ lệ tuân thủ (số ngày đo / 7)
2. BP Load và phân loại
3. ARV và phân loại  
4. ME diff và phân loại
5. Xu hướng so với tuần trước
6. Khuyến nghị (dựa trên BP Load)
"""

import os
import re
from pathlib import Path

BASE_PATH = Path("/Users/teamai/Downloads/antigravity/koliaa/Huongttt/feature/bao_cao/csv/Data_import/insert_dev")
USER = "user_bp_load"

# Tiêu chí SRS
BP_LOAD_CRITERIA = {
    "normal": (0, 15, "Bình thường", "Hệ tim mạch đang được bảo vệ tốt"),
    "borderline": (15, 30, "Chớm cao", "Bắt đầu có dấu hiệu quá tải"),
    "high": (30, 100, "Gánh nặng lớn", "Nguy cơ cao gây tổn thương tim, thận"),
}

ARV_CRITERIA = {
    "stable": (0, 10, "Ổn định", "Hệ mạch vận hành êm ái"),
    "variable": (10, 14, "Biến động", "Mạch máu bắt đầu chịu áp lực"),
    "unstable": (14, 999, "Bất ổn", "Nguy cơ cao tổn thương thành mạch"),
}

ME_CRITERIA = {
    "morning_surge": (15, 999, "Vọt áp buổi sáng", "Áp lực máu tăng quá mức khi thức dậy"),
    "balanced": (-15, 15, "Cân bằng", "Nhịp sinh học ổn định"),
    "evening_rise": (-999, -15, "Tăng áp về tối", "Non-dipper"),
}

RECOMMENDATION_RULES = {
    "good": ["Tình trạng tốt", "Tiếp tục duy trì"],
    "attention": ["Cần chú ý", "Liên hệ bác sĩ"],
}


def extract_all_metrics(filepath: Path) -> dict:
    """Extract all metrics and comments from report"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    result = {"file": filepath.name, "issues": []}
    
    # 1. Tỷ lệ tuân thủ
    match = re.search(r'\|\s*Tỷ lệ tuân thủ\s*\|\s*([\d.]+)%\s*\|', content)
    if match:
        result["compliance"] = float(match.group(1))
    
    # 2. Số ngày đo
    match = re.search(r'\|\s*Số ngày có đo\s*\|\s*(\d+)/7\s*ngày\s*\|', content)
    if match:
        result["days_measured"] = int(match.group(1))
        expected_compliance = round((int(match.group(1)) / 7) * 100, 1)
        if abs(expected_compliance - result.get("compliance", 0)) > 0.5:
            result["issues"].append(f"Compliance mismatch: {result.get('compliance')}% != {expected_compliance}%")
    
    # 3. BP Load
    match = re.search(r'\*\*BP Load\*\*\s*\|\s*([\d.]+)%\s*\|', content)
    if match:
        result["bp_load"] = float(match.group(1))
    
    match = re.search(r'\*\*BP Load\*\*\s*\|\s*[\d.]+%\s*\|\s*\*\*([^*]+)\*\*', content)
    if match:
        result["bp_load_class"] = match.group(1).strip()
    
    # 4. BP Load diễn giải
    match = re.search(r'### 2\.2 Gánh nặng.*?\*\*Diễn giải:\*\*\s*([^\n]+)', content, re.DOTALL)
    if match:
        result["bp_load_explain"] = match.group(1).strip()
    
    # 5. ARV
    match = re.search(r'\*\*ARV tâm thu\*\*\s*\|\s*([\d.]+)\s*\|', content)
    if match:
        result["arv"] = float(match.group(1))
    
    match = re.search(r'\*\*ARV tâm thu\*\*\s*\|\s*[\d.]+\s*\|\s*\*\*([^*]+)\*\*', content)
    if match:
        result["arv_class"] = match.group(1).strip()
    
    # 6. ME diff
    match = re.search(r'\*\*ME diff\*\*\s*\|\s*([+-]?\d+)\s*mmHg', content)
    if match:
        result["me_diff"] = int(match.group(1))
    
    match = re.search(r'\*\*ME diff\*\*\s*\|[^|]+\|\s*\*\*([^*]+)\*\*', content)
    if match:
        result["me_class"] = match.group(1).strip()
    
    # 7. Xu hướng
    match = re.search(r'\*\*(📈 Tăng|📉 Giảm|➡️ Ổn định)[^*]*\*\*', content)
    if match:
        result["trend"] = match.group(0).replace("**", "")
    
    # 8. Khuyến nghị
    match = re.search(r'## 5\. Khuyến Nghị\s*\n\s*([^\n]+)', content)
    if match:
        result["recommendation"] = match.group(1).strip()
    
    # 9. Số lần vượt ngưỡng
    match = re.search(r'\*\*Số lần vượt ngưỡng\*\*\s*\|\s*(\d+)/(\d+)\s*lần\s*\(([\d.]+)%\)', content)
    if match:
        result["over_threshold_count"] = int(match.group(1))
        result["total_measurements"] = int(match.group(2))
        result["over_threshold_pct"] = float(match.group(3))
    
    return result


def verify_bp_load_class(value: float) -> tuple:
    """Get expected BP Load classification"""
    if value < 15:
        return "Bình thường", "Hệ tim mạch đang được bảo vệ tốt"
    elif value <= 30:
        return "Chớm cao", "Bắt đầu có dấu hiệu quá tải"
    else:
        return "Gánh nặng lớn", "Nguy cơ cao gây tổn thương tim, thận"


def verify_arv_class(value: float) -> tuple:
    """Get expected ARV classification"""
    if value < 10:
        return "Ổn định", "Hệ mạch vận hành êm ái"
    elif value <= 14:
        return "Biến động", "Mạch máu bắt đầu chịu áp lực"
    else:
        return "Bất ổn", "Nguy cơ cao tổn thương thành mạch"


def verify_me_class(value: int) -> tuple:
    """Get expected ME diff classification"""
    if value > 15:
        return "Vọt áp buổi sáng", "Áp lực máu tăng quá mức khi thức dậy"
    elif value >= -15:
        return "Cân bằng", "Nhịp sinh học ổn định"
    else:
        return "Tăng áp về tối", "Non-dipper"


def verify_recommendation(bp_load: float) -> str:
    """Get expected recommendation based on BP Load"""
    if bp_load < 15:
        return "good"  # Tình trạng tốt
    else:
        return "attention"  # Cần chú ý


def main():
    print("=" * 100)
    print("🔍 KIỂM TRA TOÀN BỘ TIÊU CHÍ NHẬN XÉT - user_bp_load")
    print("=" * 100)
    
    week_path = BASE_PATH / USER / "week"
    all_issues = []
    
    for wf in sorted(week_path.iterdir()):
        if wf.suffix != '.md':
            continue
        
        metrics = extract_all_metrics(wf)
        print(f"\n📅 {metrics['file']}")
        print("-" * 60)
        
        issues = []
        
        # 1. Check BP Load classification
        if "bp_load" in metrics and "bp_load_class" in metrics:
            expected_class, expected_explain = verify_bp_load_class(metrics["bp_load"])
            actual_class = metrics["bp_load_class"]
            if expected_class not in actual_class:
                issues.append(f"BP Load: {metrics['bp_load']}% → Expected '{expected_class}', Got '{actual_class}'")
                print(f"   🔴 BP Load: {metrics['bp_load']}% → Expected '{expected_class}', Got '{actual_class}'")
            else:
                print(f"   ✅ BP Load: {metrics['bp_load']}% → '{actual_class}'")
        
        # 2. Check ARV classification
        if "arv" in metrics and "arv_class" in metrics:
            expected_class, expected_explain = verify_arv_class(metrics["arv"])
            actual_class = metrics["arv_class"]
            if expected_class not in actual_class:
                issues.append(f"ARV: {metrics['arv']} → Expected '{expected_class}', Got '{actual_class}'")
                print(f"   🔴 ARV: {metrics['arv']} → Expected '{expected_class}', Got '{actual_class}'")
            else:
                print(f"   ✅ ARV: {metrics['arv']} → '{actual_class}'")
        
        # 3. Check ME diff classification
        if "me_diff" in metrics and "me_class" in metrics:
            expected_class, expected_explain = verify_me_class(metrics["me_diff"])
            actual_class = metrics["me_class"]
            if expected_class not in actual_class:
                issues.append(f"ME diff: {metrics['me_diff']} → Expected '{expected_class}', Got '{actual_class}'")
                print(f"   🔴 ME diff: {metrics['me_diff']} → Expected '{expected_class}', Got '{actual_class}'")
            else:
                print(f"   ✅ ME diff: {metrics['me_diff']} mmHg → '{actual_class}'")
        
        # 4. Check recommendation consistency
        if "bp_load" in metrics and "recommendation" in metrics:
            expected_rec = verify_recommendation(metrics["bp_load"])
            rec_text = metrics["recommendation"]
            if expected_rec == "good" and "Tình trạng tốt" not in rec_text:
                issues.append(f"Recommendation: BP Load={metrics['bp_load']}% should be 'Tình trạng tốt'")
                print(f"   🔴 Khuyến nghị: BP Load={metrics['bp_load']}% nhưng không thấy 'Tình trạng tốt'")
            elif expected_rec == "attention" and "Cần chú ý" not in rec_text:
                issues.append(f"Recommendation: BP Load={metrics['bp_load']}% should be 'Cần chú ý'")
                print(f"   🔴 Khuyến nghị: BP Load={metrics['bp_load']}% nhưng không thấy 'Cần chú ý'")
            else:
                print(f"   ✅ Khuyến nghị: '{rec_text[:50]}...'")
        
        # 5. Check BP Load % = vượt ngưỡng %
        if "bp_load" in metrics and "over_threshold_pct" in metrics:
            if abs(metrics["bp_load"] - metrics["over_threshold_pct"]) > 0.5:
                issues.append(f"BP Load ({metrics['bp_load']}%) != Vượt ngưỡng ({metrics['over_threshold_pct']}%)")
                print(f"   🔴 BP Load ({metrics['bp_load']}%) != Vượt ngưỡng ({metrics['over_threshold_pct']}%)")
            else:
                print(f"   ✅ BP Load = Vượt ngưỡng: {metrics['bp_load']}%")
        
        if issues:
            all_issues.extend([(metrics['file'], i) for i in issues])
        else:
            print(f"   ✅ ALL CHECKS PASSED")
    
    # Summary
    print("\n" + "=" * 100)
    print("📊 TỔNG KẾT")
    print("=" * 100)
    
    if all_issues:
        print(f"\n🔴 CÓ {len(all_issues)} VẤN ĐỀ:")
        for file, issue in all_issues:
            print(f"   • {file}: {issue}")
    else:
        print("\n✅ TẤT CẢ TIÊU CHÍ NHẬN XÉT ĐỀU ĐÚNG!")
    
    print("=" * 100)


if __name__ == "__main__":
    main()
