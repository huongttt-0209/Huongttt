#!/usr/bin/env python3
"""
Script tạo Report Nhận xét Huyết áp theo Tuần/Tháng
Áp dụng SRS BR-005/BR-006
Hỗ trợ tất cả loại người dùng: THA, HA thấp, BP Load, Không ổn định
Version: 3.0 - Universal
"""

import os
import sys
import csv
from datetime import datetime, timedelta
from collections import defaultdict

# Default thresholds - sẽ được override từ user_health_profiles
DEFAULT_SYS_LOWER = 120
DEFAULT_SYS_UPPER = 140
DEFAULT_DIA_LOWER = 70
DEFAULT_DIA_UPPER = 90

# Khung giờ ME diff
MORNING_START = 4
MORNING_END = 10
EVENING_START = 20
EVENING_END = 24

# Khung giờ tương quan sự kiện (theo SRS)
EVENT_WINDOWS = {
    'medication': (1, 8),
    'stress': (0, 0.75),
    'caffeine': (0.5, 2),
    'exercise': (0.5, 2),
    'salt': (12, 24),
    'alcohol': (12, 24)
}

EVENT_NAMES = {
    'medication': 'Uống thuốc',
    'stress': 'Stress',
    'caffeine': 'Caffeine',
    'exercise': 'Vận động',
    'salt': 'Ăn mặn',
    'alcohol': 'Rượu/Bia'
}

# Mapping has_hypertension
HAS_HYPERTENSION_LABELS = {
    1: ("THA đã chẩn đoán", "kiem_soat"),
    2: ("HA thấp", "hypotension_load"),
    3: ("HA không ổn định", "arv"),
    4: ("HA bình thường", "bp_load"),
    5: ("Chưa chẩn đoán THA", "bp_load"),
    6: ("Không rõ", "bp_load")
}

def parse_datetime(dt_str):
    return datetime.strptime(dt_str.strip(), '%Y-%m-%d %H:%M:%S')

def is_morning(hour):
    return MORNING_START <= hour < MORNING_END

def is_evening(hour):
    return EVENING_START <= hour < EVENING_END

def get_week_monday(dt):
    days_since_monday = dt.weekday()
    return (dt - timedelta(days=days_since_monday)).date()

def classify_kiem_soat(percent):
    if percent > 70:
        return "Kiểm soát tối ưu", ">70%"
    elif percent >= 50:
        return "Kiểm soát tốt", "50-70%"
    elif percent >= 25:
        return "Kiểm soát kém", "25-50%"
    else:
        return "Không kiểm soát", "<25%"

def classify_bp_load(percent):
    """Phân loại BP Load cho người chưa chẩn đoán THA"""
    if percent < 15:
        return "Bình thường", "<15%", "Hệ tim mạch đang được bảo vệ tốt."
    elif percent <= 30:
        return "Chớm cao", "15-30%", "Bắt đầu có dấu hiệu quá tải, cần điều chỉnh lối sống."
    else:
        return "Gánh nặng lớn", ">30%", "Nguy cơ cao gây tổn thương tim, thận. Cần can thiệp y tế."

def classify_hypotension_load(percent):
    """Phân loại Hypotension Load cho người HA thấp"""
    if percent < 15:
        return "Ít khi thấp", "<15%", "Huyết áp thấp không thường xuyên."
    elif percent <= 30:
        return "Thường xuyên thấp", "15-30%", "Cơ thể thiếu máu/oxy ở mức độ vừa."
    else:
        return "Rủi ro tụt HA", ">30%", "Nguy cơ cao té ngã, choáng do thiếu máu não."

def classify_arv(arv):
    if arv < 10:
        return "Ổn định", "<10"
    elif arv <= 14:
        return "Biến động", "10-14"
    else:
        return "Bất ổn", ">14"

def classify_mediff(mediff):
    if mediff > 15:
        return "Vọt áp buổi sáng", ">15 mmHg"
    elif mediff < -15:
        return "Tăng áp về tối", "<-15 mmHg"
    else:
        return "Cân bằng", "-15~15 mmHg"

def calculate_arv_with_time(week_data):
    if len(week_data) < 2:
        return 0
    sorted_data = sorted(week_data, key=lambda x: x['dt'])
    diffs = []
    for i in range(len(sorted_data) - 1):
        time_diff = (sorted_data[i+1]['dt'] - sorted_data[i]['dt']).total_seconds() / 3600
        if time_diff <= 24:
            diffs.append(abs(sorted_data[i+1]['sys'] - sorted_data[i]['sys']))
    if not diffs:
        return 0
    return sum(diffs) / len(diffs)

def get_bp_highest(data):
    if not data:
        return None, None
    sorted_data = sorted(data, key=lambda x: (-x['sys'], -x['dia']))
    return sorted_data[0]['sys'], sorted_data[0]['dia']

def get_bp_lowest(data):
    if not data:
        return None, None
    sorted_data = sorted(data, key=lambda x: (x['sys'], x['dia']))
    return sorted_data[0]['sys'], sorted_data[0]['dia']

def load_user_config(user_dir):
    """Đọc thông tin user từ users.csv và user_health_profiles.csv"""
    config = {
        'user_name': 'Unknown',
        'has_hypertension': 1,
        'user_type': 'THA đã chẩn đoán',
        'analysis_type': 'kiem_soat',
        'sys_lower': DEFAULT_SYS_LOWER,
        'sys_upper': DEFAULT_SYS_UPPER,
        'dia_lower': DEFAULT_DIA_LOWER,
        'dia_upper': DEFAULT_DIA_UPPER
    }
    
    # Đọc users.csv
    users_file = os.path.join(user_dir, 'users.csv')
    if os.path.exists(users_file):
        with open(users_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                config['user_name'] = os.path.basename(user_dir)
                config['has_hypertension'] = int(row.get('has_hypertension', 1))
                break
    
    # Đọc health_profiles
    profiles_file = os.path.join(user_dir, 'user_health_profiles.csv')
    if os.path.exists(profiles_file):
        with open(profiles_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('systolic_threshold_lower'):
                    config['sys_lower'] = int(row['systolic_threshold_lower'])
                if row.get('systolic_threshold_upper'):
                    config['sys_upper'] = int(row['systolic_threshold_upper'])
                if row.get('diastolic_threshold_lower'):
                    config['dia_lower'] = int(row['diastolic_threshold_lower'])
                if row.get('diastolic_threshold_upper'):
                    config['dia_upper'] = int(row['diastolic_threshold_upper'])
                break
    
    # Map loại người dùng
    ht = config['has_hypertension']
    if ht in HAS_HYPERTENSION_LABELS:
        config['user_type'], config['analysis_type'] = HAS_HYPERTENSION_LABELS[ht]
    
    return config

def load_events(user_dir):
    events = []
    events_file = os.path.join(user_dir, 'events.csv')
    if os.path.exists(events_file):
        with open(events_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('event_time'):
                    events.append({
                        'dt': parse_datetime(row['event_time']),
                        'type': row['event_type'],
                        'notes': row.get('notes', '')
                    })
    return events

def analyze_event_correlation(week_data, events, week_start, week_end):
    correlations = []
    week_events = [e for e in events 
                   if week_start - timedelta(days=1) <= e['dt'].date() <= week_end]
    
    for event in week_events:
        event_type = event['type']
        if event_type not in EVENT_WINDOWS:
            continue
        
        window_start_h, window_end_h = EVENT_WINDOWS[event_type]
        bp_after_event = []
        for bp in week_data:
            hours_diff = (bp['dt'] - event['dt']).total_seconds() / 3600
            if window_start_h <= hours_diff <= window_end_h:
                bp_after_event.append(bp)
        
        if bp_after_event:
            sys_avg = sum(b['sys'] for b in bp_after_event) / len(bp_after_event)
            correlations.append({
                'event': EVENT_NAMES.get(event_type, event_type),
                'time': event['dt'].strftime('%d/%m %H:%M'),
                'bp_count': len(bp_after_event),
                'sys_avg': sys_avg,
            })
    return correlations

def analyze_abnormal(data, config):
    is_in_target = lambda sys, dia: (config['sys_lower'] <= sys <= config['sys_upper']) and \
                                     (config['dia_lower'] <= dia <= config['dia_upper'])
    
    out_of_target = [r for r in data if not is_in_target(r['sys'], r['dia'])]
    count_out = len(out_of_target)
    
    morning_out = sum(1 for r in out_of_target if 4 <= r['dt'].hour < 12)
    afternoon_out = sum(1 for r in out_of_target if 12 <= r['dt'].hour < 18)
    evening_out = sum(1 for r in out_of_target if r['dt'].hour >= 18 or r['dt'].hour < 4)
    
    peak_time = "sáng" if morning_out >= max(afternoon_out, evening_out) else \
                "chiều" if afternoon_out >= evening_out else "tối"
    
    if out_of_target:
        max_bp = max(out_of_target, key=lambda x: x['sys'])
        peak_day = max_bp['dt'].strftime('%d/%m')
        peak_value = f"{max_bp['sys']}/{max_bp['dia']}"
    else:
        peak_day = None
        peak_value = None
    
    return {
        'count_out': count_out,
        'total': len(data),
        'peak_time': peak_time,
        'morning_out': morning_out,
        'afternoon_out': afternoon_out,
        'evening_out': evening_out,
        'peak_day': peak_day,
        'peak_value': peak_value
    }

def analyze_hr(data, prev_data=None):
    hr_values = [r['hr'] for r in data]
    hr_avg = sum(hr_values) / len(hr_values)
    hr_max = max(hr_values)
    hr_min = min(hr_values)
    
    too_fast = sum(1 for hr in hr_values if hr > 100)
    too_slow = sum(1 for hr in hr_values if hr < 60)
    
    trend = None
    if prev_data:
        prev_hr = [r['hr'] for r in prev_data]
        prev_avg = sum(prev_hr) / len(prev_hr)
        diff = hr_avg - prev_avg
        if diff > 5:
            trend = f"Tăng +{diff:.0f} bpm so với kỳ trước"
        elif diff < -5:
            trend = f"Giảm {diff:.0f} bpm so với kỳ trước"
        else:
            trend = "Ổn định so với kỳ trước"
    
    return {
        'avg': hr_avg,
        'max': hr_max,
        'min': hr_min,
        'too_fast': too_fast,
        'too_slow': too_slow,
        'trend': trend
    }

def generate_week_report(week_start, week_data, week_num, events, config, prev_week_data=None, prev_sys_avg=None):
    week_end = week_start + timedelta(days=6)
    
    is_in_target = lambda sys, dia: (config['sys_lower'] <= sys <= config['sys_upper']) and \
                                     (config['dia_lower'] <= dia <= config['dia_upper'])
    
    total = len(week_data)
    in_target = sum(1 for r in week_data if is_in_target(r['sys'], r['dia']))
    kiem_soat = (in_target / total * 100) if total > 0 else 0
    
    sys_values = [r['sys'] for r in week_data]
    dia_values = [r['dia'] for r in week_data]
    hr_values = [r['hr'] for r in week_data]
    
    sys_avg = sum(sys_values) / len(sys_values)
    dia_avg = sum(dia_values) / len(dia_values)
    hr_avg = sum(hr_values) / len(hr_values)
    
    arv = calculate_arv_with_time(week_data)
    bp_high_sys, bp_high_dia = get_bp_highest(week_data)
    bp_low_sys, bp_low_dia = get_bp_lowest(week_data)
    
    # ME diff
    morning_sys = [r['sys'] for r in week_data if is_morning(r['dt'].hour)]
    evening_sys = [r['sys'] for r in week_data if is_evening(r['dt'].hour)]
    
    if morning_sys and evening_sys:
        mediff = sum(morning_sys)/len(morning_sys) - sum(evening_sys)/len(evening_sys)
        mediff_class, mediff_note = classify_mediff(mediff)
    else:
        mediff = None
        mediff_class = "Không đủ dữ liệu"
        mediff_note = "Thiếu dữ liệu sáng/tối"
    
    arv_class, arv_note = classify_arv(arv)
    
    days_with_data = len(set(r['dt'].date() for r in week_data))
    compliance = days_with_data / 7 * 100
    
    correlations = analyze_event_correlation(week_data, events, week_start, week_end)
    abnormal = analyze_abnormal(week_data, config)
    hr_analysis = analyze_hr(week_data, prev_week_data)
    
    trend_text = ""
    if prev_sys_avg:
        diff_sys = sys_avg - prev_sys_avg
        if diff_sys > 5:
            trend_text = f"📈 Tăng +{diff_sys:.0f} mmHg so với tuần trước"
        elif diff_sys < -5:
            trend_text = f"📉 Giảm {diff_sys:.0f} mmHg so với tuần trước"
        else:
            trend_text = f"➡️ Ổn định so với tuần trước ({diff_sys:+.0f} mmHg)"
    
    # Tạo markdown
    report = f"""# 📊 Báo Cáo Huyết Áp Tuần {week_num}

> **User:** {config['user_name']} ({config['user_type']})  
> **Kỳ báo cáo:** {week_start.strftime('%d/%m/%Y')} - {week_end.strftime('%d/%m/%Y')}  
> **Ngưỡng mục tiêu:** SYS {config['sys_lower']}-{config['sys_upper']}, DIA {config['dia_lower']}-{config['dia_upper']} mmHg

---

## 1. Tổng Quan Theo Dõi

| Chỉ số | Giá trị |
|:---|:---|
| Số lần đo | {total} lần |
| Số ngày có đo | {days_with_data}/7 ngày |
| Tỷ lệ tuân thủ | {compliance:.1f}% |

{f"**{trend_text}**" if trend_text else ""}

---

## 2. Phân Tích Huyết Áp

### 2.1 Tổng quan chỉ số

| Chỉ số | Giá trị |
|:---|:---|
| **HA Trung bình** | {sys_avg:.0f}/{dia_avg:.0f} mmHg |
| **HA Cao nhất** | {bp_high_sys}/{bp_high_dia} mmHg |
| **HA Thấp nhất** | {bp_low_sys}/{bp_low_dia} mmHg |
| **Nhịp tim TB** | {hr_avg:.0f} bpm |

"""
    
    # Nhận xét chính dựa trên loại người dùng
    analysis_type = config['analysis_type']
    
    if analysis_type == 'kiem_soat':
        kiem_soat_class, kiem_soat_note = classify_kiem_soat(kiem_soat)
        report += f"""### 2.2 Mức độ Kiểm soát HA

| Chỉ số | Giá trị | Phân loại | Ngưỡng |
|:---|:---|:---|:---|
| **% trong ngưỡng** | {kiem_soat:.1f}% | **{kiem_soat_class}** | {kiem_soat_note} |

> **Diễn giải:** """
        if kiem_soat > 70:
            report += "Huyết áp rất ổn định, đạt trạng thái lý tưởng."
        elif kiem_soat >= 50:
            report += "Đạt yêu cầu điều trị. Đa số thời gian cơ thể được bảo vệ."
        elif kiem_soat >= 25:
            report += "Huyết áp dao động nhiều. Hiệu quả thuốc chưa ổn định."
        else:
            report += "Nguy cơ biến cố cao. Cần can thiệp y tế."
    
    elif analysis_type == 'bp_load':
        # Tính BP Load (vượt ngưỡng 140/90)
        bp_over = sum(1 for r in week_data if r['sys'] > 140 or r['dia'] > 90)
        bp_load_percent = (bp_over / total * 100) if total > 0 else 0
        bp_load_class, bp_load_note, bp_load_explain = classify_bp_load(bp_load_percent)
        report += f"""### 2.2 Gánh nặng Huyết áp (BP Load)

| Chỉ số | Giá trị | Phân loại | Ngưỡng |
|:---|:---|:---|:---|
| **BP Load** | {bp_load_percent:.1f}% | **{bp_load_class}** | {bp_load_note} |

> **Diễn giải:** {bp_load_explain}"""
    
    elif analysis_type == 'hypotension_load':
        # Tính Hypotension Load (dưới 90/60)
        hypo_count = sum(1 for r in week_data if r['sys'] < 90 or r['dia'] < 60)
        hypo_percent = (hypo_count / total * 100) if total > 0 else 0
        hypo_class, hypo_note, hypo_explain = classify_hypotension_load(hypo_percent)
        report += f"""### 2.2 Tần suất Huyết áp thấp (Hypotension Load)

| Chỉ số | Giá trị | Phân loại | Ngưỡng |
|:---|:---|:---|:---|
| **Hypotension Load** | {hypo_percent:.1f}% | **{hypo_class}** | {hypo_note} |

> **Diễn giải:** {hypo_explain}"""
    
    else:  # arv - không ổn định
        report += f"""### 2.2 Mức độ Ổn định HA

| Chỉ số | Giá trị | Phân loại | Ngưỡng |
|:---|:---|:---|:---|
| **% trong ngưỡng** | {kiem_soat:.1f}% | - | - |

> **Nhận xét:** Huyết áp không ổn định, cần theo dõi ARV và ME diff."""
    
    report += f"""

### 2.3 Độ Ổn Định HA (ARV)

| Chỉ số | Giá trị | Phân loại | Ngưỡng |
|:---|:---|:---|:---|
| **ARV tâm thu** | {arv:.1f} | **{arv_class}** | {arv_note} |

> **Diễn giải:** """

    if arv < 10:
        report += "Hệ mạch vận hành êm ái, ít áp lực cơ học."
    elif arv <= 14:
        report += "Mạch máu bắt đầu chịu áp lực từ dao động."
    else:
        report += "Nguy cơ cao tổn thương thành mạch."

    report += f"""

### 2.4 Nhịp Sinh Học HA (ME diff)

| Chỉ số | Giá trị | Phân loại | Ngưỡng |
|:---|:---|:---|:---|
| **ME diff** | {f"{mediff:+.0f}" if mediff else "N/A"} mmHg | **{mediff_class}** | {mediff_note} |

> **Diễn giải:** """

    if mediff is not None:
        if mediff > 15:
            report += "Vọt áp buổi sáng - tăng nguy cơ đột quỵ sáng sớm."
        elif mediff < -15:
            report += "Non-dipper - rất hại cho tim và thận."
        else:
            report += "Nhịp sinh học ổn định."
    else:
        report += "Thiếu dữ liệu sáng/tối."

    report += f"""

### 2.5 Phát Hiện Bất Thường

| Chỉ số | Giá trị |
|:---|:---|
| **Số lần vượt ngưỡng** | {abnormal['count_out']}/{abnormal['total']} lần ({100-kiem_soat:.1f}%) |
| **Thời điểm thường xảy ra** | Buổi {abnormal['peak_time']} |
| **Phân bố** | Sáng: {abnormal['morning_out']}, Chiều: {abnormal['afternoon_out']}, Tối: {abnormal['evening_out']} |"""

    if abnormal['peak_day']:
        report += f"""
| **Ngày HA cao nhất** | {abnormal['peak_day']} ({abnormal['peak_value']} mmHg) |"""

    if correlations:
        report += f"""

---

## 3. Tương Quan Với Sự Kiện

| Sự kiện | Thời điểm | Số lần đo sau | SYS TB sau |
|:---|:---|:---:|:---:|"""
        for c in correlations:
            report += f"""
| {c['event']} | {c['time']} | {c['bp_count']} | {c['sys_avg']:.0f} mmHg |"""
        report += """

> **Ghi chú:** Các yếu tố như stress, caffeine, rượu bia có thể ảnh hưởng đến huyết áp."""

    report += f"""

---

## 4. Phân Tích Nhịp Tim

| Chỉ số | Giá trị |
|:---|:---|
| **Nhịp tim Trung bình** | {hr_analysis['avg']:.0f} bpm |
| **Nhịp tim Cao nhất** | {hr_analysis['max']} bpm |
| **Nhịp tim Thấp nhất** | {hr_analysis['min']} bpm |"""

    if hr_analysis['trend']:
        report += f"""
| **Xu hướng** | {hr_analysis['trend']} |"""

    if hr_analysis['too_fast'] > 0 or hr_analysis['too_slow'] > 0:
        report += f"""

⚠️ **Bất thường:** Nhanh (>100): {hr_analysis['too_fast']}, Chậm (<60): {hr_analysis['too_slow']}"""
    else:
        report += """

✅ **Nhịp tim ổn định** trong ngưỡng 60-100 bpm."""

    report += f"""

---

## 5. Khuyến Nghị

"""
    if kiem_soat > 70 and arv < 10:
        report += """✅ **Tình trạng tốt!** Tiếp tục duy trì thói quen hiện tại."""
    elif kiem_soat >= 50:
        report += """⚠️ **Cần cải thiện:** Kiểm tra việc tuân thủ thuốc, hạn chế muối."""
    else:
        report += """🚨 **Cần chú ý:** Liên hệ bác sĩ để đánh giá lại phác đồ."""

    report += f"""

---

> *Báo cáo được tạo tự động theo SRS BR-005/BR-006*  
> *Lưu ý: Báo cáo này không thay thế tư vấn y khoa chuyên môn.*
"""
    
    return report, sys_avg

def generate_month_report(month_key, month_data, config, prev_month_data=None):
    year, month = month_key
    
    is_in_target = lambda sys, dia: (config['sys_lower'] <= sys <= config['sys_upper']) and \
                                     (config['dia_lower'] <= dia <= config['dia_upper'])
    
    total = len(month_data)
    in_target = sum(1 for r in month_data if is_in_target(r['sys'], r['dia']))
    kiem_soat = (in_target / total * 100) if total > 0 else 0
    
    sys_values = [r['sys'] for r in month_data]
    dia_values = [r['dia'] for r in month_data]
    hr_values = [r['hr'] for r in month_data]
    
    sys_avg = sum(sys_values) / len(sys_values)
    dia_avg = sum(dia_values) / len(dia_values)
    hr_avg = sum(hr_values) / len(hr_values)
    
    days_with_data = len(set(r['dt'].date() for r in month_data))
    
    bp_high_sys, bp_high_dia = get_bp_highest(month_data)
    bp_low_sys, bp_low_dia = get_bp_lowest(month_data)
    arv = calculate_arv_with_time(month_data)
    arv_class, arv_note = classify_arv(arv)
    
    morning_sys = [r['sys'] for r in month_data if is_morning(r['dt'].hour)]
    evening_sys = [r['sys'] for r in month_data if is_evening(r['dt'].hour)]
    
    if morning_sys and evening_sys:
        mediff = sum(morning_sys)/len(morning_sys) - sum(evening_sys)/len(evening_sys)
        mediff_class, mediff_note = classify_mediff(mediff)
    else:
        mediff = None
        mediff_class = "Không đủ dữ liệu"
        mediff_note = "Thiếu dữ liệu"
    
    abnormal = analyze_abnormal(month_data, config)
    hr_analysis = analyze_hr(month_data, prev_month_data)
    
    trend = ""
    if prev_month_data:
        prev_in_target = sum(1 for r in prev_month_data if is_in_target(r['sys'], r['dia']))
        prev_kiem_soat = (prev_in_target / len(prev_month_data) * 100) if prev_month_data else 0
        diff = kiem_soat - prev_kiem_soat
        if diff > 5:
            trend = f"📈 Cải thiện +{diff:.1f}% so với tháng trước"
        elif diff < -5:
            trend = f"📉 Giảm {diff:.1f}% so với tháng trước"
        else:
            trend = f"➡️ Ổn định so với tháng trước"
    
    month_names = {1: "Tháng 1", 2: "Tháng 2", 3: "Tháng 3", 4: "Tháng 4", 
                   5: "Tháng 5", 6: "Tháng 6", 7: "Tháng 7", 8: "Tháng 8",
                   9: "Tháng 9", 10: "Tháng 10", 11: "Tháng 11", 12: "Tháng 12"}
    
    report = f"""# 📊 Báo Cáo Huyết Áp {month_names[month]} {year}

> **User:** {config['user_name']} ({config['user_type']})  
> **Kỳ báo cáo:** {month_names[month]} {year}  
> **Ngưỡng mục tiêu:** SYS {config['sys_lower']}-{config['sys_upper']}, DIA {config['dia_lower']}-{config['dia_upper']} mmHg

---

## 1. Tổng Quan Theo Dõi

| Chỉ số | Giá trị |
|:---|:---|
| **Tổng số lần đo** | {total} lần |
| **Số ngày có đo** | {days_with_data} ngày |
| **Tỷ lệ đo trong ngưỡng** | {kiem_soat:.1f}% |

{f"**{trend}**" if trend else ""}

---

## 2. Phân Tích Huyết Áp

### 2.1 Tổng quan chỉ số tháng

| Chỉ số | Giá trị |
|:---|:---|
| **HA Trung bình** | {sys_avg:.0f}/{dia_avg:.0f} mmHg |
| **HA Cao nhất** | {bp_high_sys}/{bp_high_dia} mmHg |
| **HA Thấp nhất** | {bp_low_sys}/{bp_low_dia} mmHg |
| **Nhịp tim TB** | {hr_avg:.0f} bpm |

### 2.2 Độ Ổn Định HA (ARV)

| Chỉ số | Giá trị | Phân loại | Ngưỡng |
|:---|:---|:---|:---|
| **ARV tâm thu** | {arv:.1f} | **{arv_class}** | {arv_note} |

### 2.3 Nhịp Sinh Học HA (ME diff)

| Chỉ số | Giá trị | Phân loại | Ngưỡng |
|:---|:---|:---|:---|
| **ME diff** | {f"{mediff:+.0f}" if mediff else "N/A"} mmHg | **{mediff_class}** | {mediff_note} |

### 2.4 Phát Hiện Bất Thường

| Chỉ số | Giá trị |
|:---|:---|
| **Số lần vượt ngưỡng** | {abnormal['count_out']}/{abnormal['total']} lần ({100-kiem_soat:.1f}%) |
| **Thời điểm thường xảy ra** | Buổi {abnormal['peak_time']} |

---

## 3. Phân Tích Nhịp Tim

| Chỉ số | Giá trị |
|:---|:---|
| **Nhịp tim Trung bình** | {hr_analysis['avg']:.0f} bpm |
| **Nhịp tim Cao nhất** | {hr_analysis['max']} bpm |
| **Nhịp tim Thấp nhất** | {hr_analysis['min']} bpm |

{"✅ Nhịp tim ổn định" if hr_analysis['too_fast'] == 0 and hr_analysis['too_slow'] == 0 else f"⚠️ Phát hiện bất thường: Nhanh: {hr_analysis['too_fast']}, Chậm: {hr_analysis['too_slow']}"}

---

## 4. Lời Khuyên Tháng Tới

"""
    if kiem_soat > 70:
        report += """🎉 **Xuất sắc!** Tiếp tục duy trì."""
    elif kiem_soat >= 50:
        report += """👍 **Khá tốt!** Cố gắng nâng tỷ lệ kiểm soát >70%."""
    else:
        report += """⚠️ **Cần cải thiện!** Tham khảo ý kiến bác sĩ."""

    report += f"""

---

> *Báo cáo được tạo tự động theo SRS BR-005*  
> *Lưu ý: Báo cáo này không thay thế tư vấn y khoa.*
"""
    
    return report

def process_user(user_dir):
    print(f"\n{'='*60}")
    print(f"Processing: {os.path.basename(user_dir)}")
    print(f"{'='*60}")
    
    config = load_user_config(user_dir)
    print(f"  Loại: {config['user_type']}")
    print(f"  Ngưỡng: SYS {config['sys_lower']}-{config['sys_upper']}, DIA {config['dia_lower']}-{config['dia_upper']}")
    
    bp_file = os.path.join(user_dir, 'user_blood_pressure.csv')
    if not os.path.exists(bp_file):
        print(f"  ❌ Không tìm thấy user_blood_pressure.csv")
        return
    
    # Đọc dữ liệu
    with open(bp_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            if row.get('measurement_time'):
                data.append({
                    'dt': parse_datetime(row['measurement_time']),
                    'sys': int(row['systolic']),
                    'dia': int(row['diastolic']),
                    'hr': int(row['heart_rate'])
                })
    
    events = load_events(user_dir)
    print(f"  Đọc được {len(data)} lần đo, {len(events)} sự kiện")
    
    # Tạo thư mục week/month
    week_dir = os.path.join(user_dir, 'week')
    month_dir = os.path.join(user_dir, 'month')
    os.makedirs(week_dir, exist_ok=True)
    os.makedirs(month_dir, exist_ok=True)
    
    # Group theo tuần
    weeks = defaultdict(list)
    for r in data:
        week_start = get_week_monday(r['dt'])
        weeks[week_start].append(r)
    
    # Group theo tháng
    months = defaultdict(list)
    for r in data:
        month_key = (r['dt'].year, r['dt'].month)
        months[month_key].append(r)
    
    # Tạo reports tuần
    print("  Tạo báo cáo tuần...")
    sorted_weeks = sorted(weeks.keys())
    prev_sys_avg = None
    prev_week_data = None
    
    for i, week_start in enumerate(sorted_weeks):
        week_data = weeks[week_start]
        week_num = i + 1
        week_end = week_start + timedelta(days=6)
        
        report, sys_avg = generate_week_report(
            week_start, week_data, week_num, events, config,
            prev_week_data, prev_sys_avg
        )
        
        filename = os.path.join(week_dir, f"{week_start.strftime('%Y-%m-%d')}_{week_end.strftime('%Y-%m-%d')}.md")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        
        prev_sys_avg = sys_avg
        prev_week_data = week_data
    
    print(f"    ✅ {len(weeks)} báo cáo tuần")
    
    # Tạo reports tháng
    print("  Tạo báo cáo tháng...")
    sorted_months = sorted(months.keys())
    for i, month_key in enumerate(sorted_months):
        month_data = months[month_key]
        prev_data = months[sorted_months[i-1]] if i > 0 else None
        report = generate_month_report(month_key, month_data, config, prev_data)
        
        year, month = month_key
        filename = os.path.join(month_dir, f"month_{year}-{month:02d}.md")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
    
    print(f"    ✅ {len(months)} báo cáo tháng")

def main():
    base_dir = "/Users/teamai/Downloads/antigravity/koliaa/Huongttt/feature/bao_cao/csv/Data_import/insert_dev"
    
    users = ['user_tha', 'user_ko_on_dinh', 'user_ha_thap', 'user_bp_load']
    
    for user in users:
        user_dir = os.path.join(base_dir, user)
        if os.path.exists(user_dir):
            process_user(user_dir)
        else:
            print(f"❌ Không tìm thấy: {user_dir}")
    
    print("\n🎉 HOÀN THÀNH TẤT CẢ!")

if __name__ == '__main__':
    main()
