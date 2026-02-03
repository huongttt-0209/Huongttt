# 📊 Data Dictionary: test_expected_chi-so.csv

> **File:** `feature/bao_cao/csv/HA/test_expected_chi-so.csv`  
> **Mục đích:** Test data dự kiến cho các chỉ số huyết áp (Blood Pressure metrics)  
> **SRS Reference:** BR-005, BR-006

---

## 📁 INPUT FILES

### 1. user_blood_pressure.csv
| Cột | Mô tả | Ví dụ |
|:---|:---|:---|
| `id` | ID bản ghi | 1, 2, 3... |
| `user_id` | ID user | `u01-0000-0000-0000-000000000001` |
| `systolic` | Huyết áp tâm thu (mmHg) | 122, 155, 118 |
| `diastolic` | Huyết áp tâm trương (mmHg) | 75, 95, 72 |
| `heart_rate` | Nhịp tim (bpm) | 70, 82, 68 |
| `measurement_time` | Thời gian đo | `2026-01-20 06:00:00` |
| `notes` | Ghi chú | `tuần này - sáng`, `tháng trước` |

### 2. user_health_profiles.csv
| Cột | Mô tả | Ví dụ |
|:---|:---|:---|
| `user_id` | ID user | `u01-0000-0000-0000-000000000001` |
| `systolic_threshold_lower` | Ngưỡng tâm thu dưới | 120 |
| `systolic_threshold_upper` | Ngưỡng tâm thu trên | 130 |
| `diastolic_threshold_lower` | Ngưỡng tâm trương dưới | 70 |
| `diastolic_threshold_upper` | Ngưỡng tâm trương trên | 80 |

### 3. test_event_eat.csv (Sự kiện liên quan)
| Cột | Mô tả | Ví dụ |
|:---|:---|:---|
| `event_type` | Loại sự kiện | `an_man`, `van_dong`, `stress`, `caffeine`, `ruou_bia` |
| `event_time` | Thời gian sự kiện | `2026-01-20 19:00:00` |
| `interval_hours` | Khoảng cách đến lần đo HA (giờ) | 11.5, 0.5, 1.5 |

### 4. users.csv
| Cột | Mô tả | Giá trị |
|:---|:---|:---|
| `has_hypertension` | Tình trạng HA | 1=THA chẩn đoán, 2=Cao chưa CĐ, 3=Bình thường, 4=Không ổn định |

---

## 📐 CÔNG THỨC TÍNH TOÁN (BR-006)

### 1. kiem_soat (% trong ngưỡng mục tiêu)
**Áp dụng cho:** `has_hypertension = 1` (THA đã chẩn đoán)

```
kiem_soat = (Số lần đo trong ngưỡng / Tổng số lần đo) × 100%
```

**Điều kiện trong ngưỡng:**
- `systolic_threshold_lower ≤ systolic ≤ systolic_threshold_upper` VÀ
- `diastolic_threshold_lower ≤ diastolic ≤ diastolic_threshold_upper`

**Ví dụ u01:**
- Ngưỡng: SYS 120-130, DIA 70-80
- Tuần này: 21 lần đo, 19 lần trong ngưỡng
- `kiem_soat = 19/21 × 100% = 90.5%` → **Kiểm soát tối ưu** (>70%)

---

### 2. bp_load (% vượt 140/90)
**Áp dụng cho:** `has_hypertension = 2, 3, 4` (Chưa chẩn đoán THA)

```
bp_load = (Số lần đo vượt 140/90 / Tổng số lần đo) × 100%
```

**Điều kiện vượt ngưỡng:**
- `systolic > 140` HOẶC `diastolic > 90`

**Ví dụ u05:**
- Tuần này: 21 lần đo, 19 lần vượt 140/90
- `bp_load = 19/21 × 100% = 90.5%` → **Gánh nặng lớn** (>30%)

**Ví dụ u06:**
- Tuần này: 21 lần đo, 2 lần vượt (141/91 và 143/92)
- `bp_load = 2/21 × 100% = 9.5%` → **Bình thường** (<15%)

---

### 3. arv (Average Real Variability)
**Công thức:**
```
ARV = (1/(n-1)) × Σ|BPₖ₊₁ - BPₖ|
```

**Ví dụ u01 (tuần này, 21 lần đo SYS):**
```
Δ1 = |125-122| = 3
Δ2 = |118-125| = 7
Δ3 = |124-118| = 6
...
ARV = Σ|Δ| / 20 = ~5 → Ổn định (<10)
```

**Ví dụ u07 (tuần này, dao động lớn):**
```
SYS: 115 → 145 → 125 → 110 → 155 → 130 → 118 → 148...
ARV = ~18 → Bất ổn (>14)
```

---

### 4. mediff (Morning-Evening Difference)
**Công thức:**
```
MEdiff = SYS_sáng_TB - SYS_tối_TB
```

**Khung giờ:**
- Sáng: 04:00 - 10:00
- Tối: 20:00 - 00:00

**Ví dụ u01:**
```
SYS_sáng = (122+124+126+132+128+126+134)/7 = 127.4
SYS_tối = (118+120+119+121+118+120+122)/7 = 119.7
MEdiff = 127.4 - 119.7 = +7.7 ≈ +7 → Cân bằng (-15~15)
```

**Ví dụ u07:**
```
SYS_sáng = (115+110+118+112+120+108+115)/7 = 114
SYS_tối = (125+130+122+128+135+140+132)/7 = 130.3
MEdiff = 114 - 130.3 = -16.3 ≈ -20 → Tăng áp về tối (<-15)
```

---

### 5. xu_huong_tuan (Xu hướng tuần)
**Công thức:**
```
Δ_tuần = SYS_TB_tuần_này - SYS_TB_tuần_trước
```

**Ví dụ u01:**
```
Tuần này: (122+125+118+124+128+120+126+130+119+132+...)/21 = 125
Tuần trước: (125+120+127+122+124+119+126+121)/8 = 123
Δ_tuần = 125 - 123 = +2 → Ổn định (±5)
```

---

### 6. xu_huong_thang (Xu hướng tháng)
**Công thức:**
```
Δ_tháng = SYS_TB_tháng_này - SYS_TB_tháng_trước
```

**Ví dụ u01:**
```
Tháng này (Jan): 125
Tháng trước (Dec): 118
Δ_tháng = 125 - 118 = +7 → Tăng nhẹ (>5)
```

---

## 📊 OUTPUT FILE: test_expected_chi-so.csv

| # | Cột | Kiểu | Mô tả | Nguồn |
|:---:|:---|:---|:---|:---|
| 1 | `user_id` | UUID | ID user | `users.csv` |
| 2 | `user_profile` | Enum | Tình trạng HA | `users.has_hypertension` |
| 3 | `data_type` | Enum | Loại chỉ số | Theo BR-006 |
| 4 | `metric_name` | String | Tên hiển thị | SRS |
| 5 | `calculation` | String | Công thức | `user_blood_pressure` |
| 6 | `value` | Number | Kết quả | Tính toán |
| 7 | `expected_result` | String | Phân loại | Ngưỡng BR-006 |
| 8 | `notes` | String | Ngưỡng | SRS |
| 9 | `srs_ref` | String | Tham chiếu | BR-005/BR-006 |

---

## 📈 NGƯỠNG PHÂN LOẠI (BR-006)

### kiem_soat
| % | Phân loại |
|:---|:---|
| >70% | Kiểm soát tối ưu |
| 50-70% | Kiểm soát tốt |
| 25-50% | Kiểm soát kém |
| <25% | Không được kiểm soát |

### bp_load
| % | Phân loại |
|:---|:---|
| <15% | Bình thường |
| 15-30% | Chớm cao |
| >30% | Gánh nặng lớn |

### arv
| Giá trị | Phân loại |
|:---|:---|
| <10 | Ổn định |
| 10-14 | Biến động |
| >14 | Bất ổn |

### mediff
| mmHg | Phân loại |
|:---|:---|
| >15 | Vọt áp buổi sáng (Morning Surge) |
| -15 ~ 15 | Cân bằng |
| <-15 | Tăng áp về tối (Risky Evening) |

---

## 👥 SUMMARY (4 Users)

| User | Profile | kiem_soat/bp_load | ARV | MEdiff | Δtuần | Δtháng |
|:---|:---|:---|:---|:---|:---|:---|
| u01 | THA_diagnosed | 90.5% Tối ưu | 5 Ổn định | +7 Cân bằng | +2 | +7 |
| u05 | cao_chua_cdoan | 90.5% Gánh nặng | 12 Biến động | +18 Morning | +5 | +10 |
| u06 | binh_thuong | 9.5% Bình thường | 6 Ổn định | +5 Cân bằng | +2 | +4 |
| u07 | ko_on_dinh | 38.1% Gánh nặng | 18 Bất ổn | -20 Risky | +3 | +4 |
