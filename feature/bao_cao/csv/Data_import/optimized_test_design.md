# 📋 Thiết Kế Chi Tiết 4 Users × 8 Tuần (Realistic)

## Mục Tiêu

Thiết kế bộ dữ liệu **4 users** với tần suất đo **realistic** - không phải ai cũng đo đầy đủ mỗi ngày.

---

## 1. Tổng Quan 4 Users

| # | User | has_hyp | Đặc điểm tình trạng | Tần suất đo |
|:---:|:---|:---:|:---|:---|
| 1 | `user_tha` | 1 | THA đã chẩn đoán, đang điều trị | **3 lần/ngày** (tuân thủ tốt) |
| 2 | `user_bp_load` | 2 | Cao chưa chẩn đoán, mới phát hiện | **2 lần/ngày** (sáng-tối) |
| 3 | `user_ko_on_dinh` | 4 | Không ổn định, hay quên | **1-2 lần/ngày, bỏ nhiều ngày** |
| 4 | `user_ha_thap` | 5 | HA thấp, chỉ đo khi có triệu chứng | **1-3 lần/ngày, không đều** |

---

## 2. Chi Tiết Từng User (Góc Nhìn Người Dùng)

---

### 2.1 User THA - "Bệnh nhân tuân thủ"

**Câu chuyện người dùng:**
> Ông Nguyễn, 56 tuổi, THA 2 năm. Uống thuốc đều, nghe lời bác sĩ đo 3 lần/ngày. 
> Đôi khi bận việc bỏ buổi trưa, cuối tuần hay quên, Tết thì "nghỉ xả hơi" luôn.

**Tần suất đo - Realistic:**

| Tuần | Tình huống thực tế | Ngày đo | Lần/ngày | Tổng | Tỷ lệ |
|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | Mới được doctor nhắc, quyết tâm | 7/7 | 3 | **21** | 100% |
| 2 | Vẫn tốt, CN bỏ buổi trưa | 7/7 | 2-3 | **19** | 90% |
| 3 | Đi công tác 2 ngày | 5/7 | 2-3 | **13** | 62% |
| 4 | Quay lại, cố gắng bù | 7/7 | 3-4 | **24** | 114% |
| 5 | **TẾT - chỉ đo khi nhớ** | 3/7 | 1-2 | **5** | **24%** |
| 6 | Sau Tết, còn lười | 5/7 | 2 | **10** | 48% |
| 7 | Cảm thấy mệt, đo nhiều hơn | 7/7 | 3-4 | **25** | 119% |
| 8 | Ổn định trở lại | 7/7 | 3 | **21** | 100% |

**Tổng: ~138 lần đo (thay vì 168 nếu đều)**

---

### 2.2 User BP Load - "Người mới phát hiện"

**Câu chuyện người dùng:**
> Chị Hương, 45 tuổi, khám sức khỏe phát hiện HA cao. Bác sĩ bảo theo dõi.
> Đầu tiên chăm chỉ, sau quên dần. Khi thấy chỉ số xấu lại chăm lại.

**Tần suất đo - Realistic:**

| Tuần | Tình huống thực tế | Ngày đo | Lần/ngày | Tổng | Tỷ lệ |
|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | Vừa mua máy, hay đo thử | 7/7 | 3-4 | **25** | 179% |
| 2 | Hào hứng giảm dần | 6/7 | 2-3 | **15** | 107% |
| 3 | Bình thường | 5/7 | 2 | **10** | 71% |
| 4 | Quên dần | 4/7 | 1-2 | **6** | **43%** |
| 5 | **TẾT - không đo** | 1/7 | 1 | **1** | **7%** |
| 6 | Thấy chỉ số xấu, lo lắng | 7/7 | 3-4 | **24** | 171% |
| 7 | Duy trì | 6/7 | 2-3 | **16** | 114% |
| 8 | Ổn định | 6/7 | 2 | **12** | 86% |

**Tổng: ~109 lần đo**

---

### 2.3 User Không Ổn Định - "Hay quên, hay lo"

**Câu chuyện người dùng:**
> Anh Tú, 52 tuổi, HA thất thường. Hay quên đo, nhưng khi cảm thấy khó chịu 
> (đau đầu, chóng mặt) thì đo liên tục để kiểm tra. Đo xong thấy cao lại lo.

**Tần suất đo - Realistic:**

| Tuần | Tình huống thực tế | Ngày đo | Lần/ngày | Tổng | Tỷ lệ |
|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | Bình thường, hay quên | 3/7 | 1-2 | **5** | **24%** |
| 2 | Đau đầu, lo lắng, đo nhiều | 5/7 | 3-5 | **18** | 86% |
| 3 | Thấy ổn, lại quên | 2/7 | 1 | **2** | **10%** |
| 4 | Khám doctor, được nhắc | 6/7 | 2-3 | **15** | 71% |
| 5 | **TẾT - hoàn toàn không đo** | 0/7 | 0 | **0** | **0%** |
| 6 | Sau Tết choáng, đo liên tục | 6/7 | 4-6 | **30** | **143%** |
| 7 | Giảm dần | 4/7 | 2-3 | **10** | 48% |
| 8 | Bình thường | 5/7 | 2 | **10** | 48% |

**Tổng: ~90 lần đo (rất không đều)**

**Edge cases test được:**
- Tuần 3: Chỉ 2 lần đo → Cảnh báo "Không đủ data"
- Tuần 5: 0 lần đo → Cảnh báo "Không có data"
- Tuần 6: Đo quá nhiều (>21 lần/tuần)

---

### 2.4 User HA Thấp - "Đo khi có triệu chứng"

**Câu chuyện người dùng:**
> Cô Lan, 35 tuổi, HA thấp mãn tính. Chỉ đo khi chóng mặt hoặc muốn check 
> sau khi đứng dậy đột ngột. Không đo đều vì "thấy khỏe thì không cần".

**Tần suất đo - Realistic:**

| Tuần | Tình huống thực tế | Ngày đo | Lần/ngày | Tổng | Tỷ lệ |
|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | Khỏe, ít đo | 2/7 | 1 | **2** | **10%** |
| 2 | Hay chóng mặt buổi sáng | 5/7 | 2-3 | **12** | 57% |
| 3 | Chóng mặt nhiều, đo liên tục | 7/7 | 3-4 | **25** | 119% |
| 4 | Được kê thuốc, theo dõi | 7/7 | 3 | **21** | 100% |
| 5 | **TẾT - ít triệu chứng** | 2/7 | 1 | **2** | **10%** |
| 6 | Lại chóng mặt sau Tết | 6/7 | 2-3 | **16** | 76% |
| 7 | Ổn dần | 4/7 | 1-2 | **6** | 29% |
| 8 | Khám lại, doctor bảo đo | 6/7 | 2-3 | **15** | 71% |

**Tổng: ~99 lần đo**

---

## 3. Tổng Hợp Tần Suất Đo

### Biểu đồ số lần đo theo tuần:

```
Lần đo
   30 |                              ██ (U3-T6: 30)
   25 |    ██           ██    ██    ▓▓           ██ (U1-T7: 25)
   21 | ██ ▓▓           ▓▓    ██ ▓▓              ▓▓ ██
   15 |    ▓▓ ██    ██       ▓▓ ▓▓ ▓▓ ▓▓ ██ ██ ▓▓ ▓▓
   10 |       ▓▓ ██ ▓▓ ██       ██    ▓▓ ██ ██ ▓▓
    5 | ▓▓ ██ ▓▓ ██ ▓▓ ██ ██              ██
    0 |___|___|___|___|___|___|___|___|___
        T1  T2  T3  T4  T5  T6  T7  T8
        
▓▓ = User THA    ██ = User BP Load
░░ = User KÔĐ    ▒▒ = User HA Thấp
```

### So sánh % tuân thủ:

| User | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | TB |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| THA | 100% | 90% | 62% | 114% | **24%** | 48% | 119% | 100% | 82% |
| BP Load | 179% | 107% | 71% | **43%** | **7%** | 171% | 114% | 86% | 97% |
| Không ổn định | **24%** | 86% | **10%** | 71% | **0%** | **143%** | 48% | 48% | 54% |
| HA Thấp | **10%** | 57% | 119% | 100% | **10%** | 76% | 29% | 71% | 59% |

### Edge Cases được test:

| Case | User | Tuần | Mô tả |
|:---|:---|:---:|:---|
| Không đo | Ko ổn định | T5 | 0 lần đo → "Không có dữ liệu" |
| Quá ít | Ko ổn định | T3 | 2 lần → "Không đủ dữ liệu để phân tích" |
| Ít đo | HA Thấp | T1, T5 | 2 lần → Cảnh báo cần đo thêm |
| Đo quá nhiều | Ko ổn định | T6 | 30 lần → Hiển thị bình thường |
| Đo nhiều hơn yêu cầu | THA | T4, T7 | >21 lần → Tính bình thường |


---

## 3. Ma Trận Coverage Tổng Hợp

| Loại nhận xét | User THA | User BP | User KÔĐ | User Thấp |
|:---|:---:|:---:|:---:|:---:|
| Kiểm soát tối ưu (>70%) | ✅ T1,2,8 | - | - | - |
| Kiểm soát tốt (50-70%) | ✅ T3,7 | - | - | - |
| Kiểm soát kém (25-50%) | ✅ T4,6 | - | - | - |
| Không kiểm soát (<25%) | ✅ T5 | - | - | - |
| BP Load bình thường | - | ✅ T1,2,8 | - | - |
| BP Load chớm cao | - | ✅ T3,4,7 | - | - |
| BP Load gánh nặng | - | ✅ T5,6 | ✅ Tất cả | - |
| Hypo ít khi | - | - | - | ✅ T1,2,8 |
| Hypo thường xuyên | - | - | - | ✅ T3,4,7 |
| Hypo rủi ro | - | - | - | ✅ T5,6 |
| ARV ổn định | ✅ T1,2,4,7,8 | - | - | - |
| ARV biến động | ✅ T3 | - | - | - |
| ARV bất ổn | ✅ T5,6 | - | ✅ Tất cả | - |
| ME diff cân bằng | ✅ T1,3,5-8 | - | - | - |
| ME diff vọt sáng | ✅ T2 | - | ✅ T4 | - |
| ME diff tăng tối | ✅ T4 | - | ✅ Đa số | - |
| **Không đủ data** | - | - | ✅ T5 | - |
| Tuân thủ tốt (>80%) | ✅ | - | - | - |
| Tuân thủ khá (50-80%) | - | ✅ | - | ✅ |
| Tuân thủ kém (<50%) | - | - | ✅ | - |

**→ 17/17 nhận xét chính + 3 mức tuân thủ + edge case "Không đủ data"**

---

## 4. Cấu Trúc Folder

```
Data_import/
└── optimized_4users/
    ├── README.md
    │
    ├── user_tha/
    │   ├── users.csv
    │   ├── user_health_profiles.csv
    │   ├── user_blood_pressure.csv           ← ~154 lần đo
    │   ├── events.csv
    │   ├── expected_chi-so_week.csv          ← 8 tuần
    │   └── expected_chi-so_month.csv         ← 2 tháng
    │
    ├── user_bp_load/
    │   ├── users.csv
    │   ├── user_health_profiles.csv
    │   ├── user_blood_pressure.csv           ← ~92 lần đo
    │   ├── events.csv
    │   ├── expected_chi-so_week.csv
    │   └── expected_chi-so_month.csv
    │
    ├── user_ko_on_dinh/
    │   ├── users.csv
    │   ├── user_health_profiles.csv
    │   ├── user_blood_pressure.csv           ← ~67 lần đo (không đều)
    │   ├── events.csv
    │   ├── expected_chi-so_week.csv
    │   └── expected_chi-so_month.csv
    │
    └── user_ha_thap/
        ├── users.csv
        ├── user_health_profiles.csv
        ├── user_blood_pressure.csv           ← ~101 lần đo
        ├── events.csv
        ├── expected_chi-so_week.csv
        └── expected_chi-so_month.csv
```

---

## 5. Quyết Định Cần Xác Nhận

1. **OK với 4 users này?** Hay cần thêm/bớt?
2. **Tần suất đo có realistic không?** Hay cần điều chỉnh?
3. **Có cần thêm user cho has_hypertension = 3, 6 không?**
4. **Folder name: `optimized_4users` hay tên khác?**

---

*Ngày tạo: 2026-02-04*
