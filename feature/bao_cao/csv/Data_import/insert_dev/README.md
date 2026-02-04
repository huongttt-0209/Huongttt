# 📋 Test Data 4 Users × 8 Tuần

Bộ dữ liệu 4 users với tần suất đo realistic theo góc nhìn người dùng thực.

## Danh sách 4 Users

| Folder | has_hyp | Tính cách | Nhận xét test |
|:---|:---:|:---|:---|
| `user_tha/` | 1 | Tuân thủ tốt | 4 mức kiểm soát HA + ARV + ME diff |
| `user_bp_load/` | 2 | Mới phát hiện | 3 mức BP Load |
| `user_ko_on_dinh/` | 4 | Hay quên, hay lo | ARV bất ổn + Edge cases |
| `user_ha_thap/` | 5 | Đo khi triệu chứng | 3 mức Hypotension Load |

## Timeline

- Tháng 12/2025: Tuần 1-4 (baseline)
- Tháng 01/2026: Tuần 5-8 (so sánh)
- Tuần 5 = Tuần Tết (ít đo)

## Coverage: 100%

✅ 17/17 loại nhận xét + Edge cases

*Chi tiết: xem `optimized_test_design.md`*
