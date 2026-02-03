# Task: Generate Blood Pressure Test Data and Python Calculator

## Objective
Tạo dữ liệu test input đầy đủ cho 16 user từ test cases và code Python để sinh expected output files theo DATA_DICTIONARY.md

---

## Phase 1: Planning
- [x] Đọc và phân tích `DATA_DICTIONARY.md` - công thức tính
- [x] Đọc `TC_Bieu_Do_Huyet_Ap.csv/md` - 27 test cases, 16 users
- [x] Đọc các file input hiện có (4 users: U01, U05, U06, U07)
- [x] Đọc các file expected output hiện có (week & month)
- [x] Tạo implementation plan
- [ ] Review plan với user

## Phase 2: Execution
- [ ] Mở rộng `users.csv` từ 4 → 16 users
- [ ] Mở rộng `user_health_profiles.csv` từ 4 → 16 users
- [ ] Mở rộng `user_blood_pressure.csv` cho 16 users
- [ ] Mở rộng `test_event_eat.csv` cho các events cần thiết
- [ ] Tạo Python script để tính toán expected output

## Phase 3: Verification
- [ ] Verify Python script chạy đúng với dữ liệu hiện có
- [ ] Verify kết quả khớp với expected values trong DATA_DICTIONARY
- [ ] Generate expected output files mới

---

## Users Required (từ TC_Bieu_Do_Huyet_Ap.csv)

| User | has_hypertension | Profile | Scenarios |
|------|------------------|---------|-----------|
| U01 | 1 | THA_diagnosed | kiem_soat 90% Tối ưu, ARV 5 Ổn định, MEdiff +7 |
| U02 | 1 | THA_diagnosed | kiem_soat 66.7% Tốt, ARV 12, MEdiff +21 Morning Surge |
| U03 | 1 | THA_diagnosed | kiem_soat 33.3% Kém |
| U04 | 1 | THA_diagnosed | kiem_soat 9.5% Không KS |
| U05 | 2 | cao_chua_cdoan | bp_load 90.5% Gánh nặng |
| U06 | 3 | binh_thuong | bp_load 9.5% Bình thường |
| U07 | 4 | ko_on_dinh | bp_load 38.1%, ARV 18 Bất ổn, MEdiff -20 Risky |
| U08 | 5 | HA_thap | Hypotension 57.1% Rủi ro |
| U09 | 6 | khong_ro | BP Load 15% Chớm cao (boundary) |
| U10 | - | - | Empty State - không có data |
| U11 | - | - | <2 lần đo/ngày - ẩn nhận xét |
| U12 | 5 | HA_thap | Hypotension 9.5% Ít khi |
| U13 | 5 | HA_thap | Hypotension 33.3% Thường xuyên |
| U14 | - | - | High Frequency 10 lần/ngày |
| U15 | - | - | Xu hướng TĂNG +5 vs tuần trước |
| U16 | - | - | Xu hướng GIẢM -12 vs tháng trước |
