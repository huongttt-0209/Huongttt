# 📋 Test Cases: Biểu đồ Huyết Áp

**Module:** Bao_Cao  
**Feature:** Bieu_do_HA  
**SRS Reference:** BR-005, BR-006, BR-007  
**Total TCs:** 27

---

## 📊 Test Cases Table

| ID | Section | Testcase name | Sub-case | Pre-condition | Step | Expected output | Priority | Data Ref |
|----|---------|---------------|----------|---------------|------|-----------------|----------|----------|
| TC_HA_001 | BR-006 | [FUNC] Kiểm soát THA Tối ưu | >70% | 1. User U01 đăng nhập<br>2. has_hypertension = 1<br>3. Ngưỡng SYS 120-130, DIA 70-80 | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét Kiểm soát HA | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Kiểm soát Tối ưu"<br>3.2. Tỷ lệ = 90% | High | TD_001 |
| TC_HA_002 | BR-006 | [FUNC] Kiểm soát THA Tốt | 50-70% | 1. User U02 đăng nhập<br>2. has_hypertension = 1<br>3. Ngưỡng SYS 120-135, DIA 75-85 | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét Kiểm soát HA | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Kiểm soát Tốt"<br>3.2. Tỷ lệ = 66.7% | High | TD_002 |
| TC_HA_003 | BR-006 | [FUNC] Kiểm soát THA Kém | 25-50% | 1. User U03 đăng nhập<br>2. has_hypertension = 1<br>3. Ngưỡng SYS 120-130, DIA 70-80 | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét Kiểm soát HA | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Kiểm soát Kém"<br>3.2. Tỷ lệ = 33.3% | High | TD_003 |
| TC_HA_004 | BR-006 | [FUNC] Kiểm soát THA Không KS | <25% | 1. User U04 đăng nhập<br>2. has_hypertension = 1<br>3. Ngưỡng SYS 120-130, DIA 70-80 | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét Kiểm soát HA | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Không được kiểm soát"<br>3.2. Tỷ lệ = 9.5% | High | TD_004 |
| TC_HA_005 | BR-006 | [FUNC] BP Load Gánh nặng | >30% | 1. User U05 đăng nhập<br>2. has_hypertension = 2 (Cao chưa CĐ) | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét Nguy cơ THA | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Gánh nặng lớn lên hệ tim mạch"<br>3.2. BP Load = 90.5% | High | TD_005 |
| TC_HA_006 | BR-006 | [FUNC] BP Load Bình thường | <15% | 1. User U06 đăng nhập<br>2. has_hypertension = 3 (Bình thường) | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét Nguy cơ THA | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Hệ tim mạch được bảo vệ tốt"<br>3.2. BP Load = 9.5% | High | TD_006 |
| TC_HA_007 | BR-006 | [BOUNDARY] BP Load Chớm cao | =15% | 1. User U09 đăng nhập<br>2. has_hypertension = 6 (Không rõ) | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét Nguy cơ THA | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Chớm cao - cần điều chỉnh lối sống"<br>3.2. BP Load = 15% | Medium | TD_009 |
| TC_HA_008 | BR-006 | [FUNC] Hypotension Rủi ro | >30% | 1. User U08 đăng nhập<br>2. has_hypertension = 5 (HA thấp) | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét HA thấp | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Rủi ro tụt huyết áp"<br>3.2. Hypotension Load = 57.1% | High | TD_008 |
| TC_HA_009 | BR-006 | [FUNC] Hypotension Ít khi | <15% | 1. User U12 đăng nhập<br>2. has_hypertension = 5 (HA thấp) | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét HA thấp | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Ít khi thấp"<br>3.2. Hypotension Load = 9.5% | Medium | TD_012 |
| TC_HA_010 | BR-006 | [FUNC] Hypotension Thường xuyên | 15-30% | 1. User U13 đăng nhập<br>2. has_hypertension = 5 (HA thấp) | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét HA thấp | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Thường xuyên thấp"<br>3.2. Hypotension Load = 33.3% | Medium | TD_013 |
| TC_HA_011 | BR-006 | [FUNC] ARV Ổn định | <10 | 1. User U01 đăng nhập<br>2. Có >=20 records BP | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét Độ ổn định HA | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Ổn định - Hệ mạch vận hành êm ái"<br>3.2. ARV = 4-5 | High | TD_001 |
| TC_HA_012 | BR-006 | [FUNC] ARV Biến động | 10-14 | 1. User U02 đăng nhập<br>2. Có >=20 records BP | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét Độ ổn định HA | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Biến động - Mạch máu bắt đầu chịu áp lực"<br>3.2. ARV = 12 | High | TD_002 |
| TC_HA_013 | BR-006 | [FUNC] ARV Bất ổn | >14 | 1. User U07 đăng nhập<br>2. Có >=20 records BP | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét Độ ổn định HA | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Bất ổn - Nguy cơ cao tổn thương thành mạch"<br>3.2. ARV = 18-19 | High | TD_007 |
| TC_HA_014 | BR-006 | [FUNC] MEdiff Morning Surge | >15 | 1. User U02 đăng nhập<br>2. Data sáng cao (145-155)<br>3. Data tối thấp (122-130) | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét Nhịp sinh học HA | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Vọt áp buổi sáng (Morning Surge)"<br>3.2. MEdiff = +21 | High | TD_002 |
| TC_HA_015 | BR-006 | [FUNC] MEdiff Cân bằng | -15~15 | 1. User U01 đăng nhập<br>2. Data sáng và tối cân bằng (~124-126) | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét Nhịp sinh học HA | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Cân bằng (Balanced)"<br>3.2. MEdiff = +6-7 | High | TD_001 |
| TC_HA_016 | BR-006 | [FUNC] MEdiff Risky Evening | <-15 | 1. User U07 đăng nhập<br>2. Data tối cao hơn sáng (tối ~135-145, sáng ~115-120) | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét Nhịp sinh học HA | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Tăng áp về tối (Risky Evening)"<br>3.2. MEdiff = -16~-20 | High | TD_007 |
| TC_HA_017 | BR-006 | [FUNC] Tương quan Thuốc | 1-8h sau uống | 1. User U02 đăng nhập<br>2. Có event uống thuốc lúc 06:30<br>3. BP đo lúc 08:30-14:00 | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Tương quan Sự kiện | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "HA giảm sau uống thuốc 1-8h"<br>3.2. Từ 145→128 mmHg | High | TD_002 |
| TC_HA_018 | BR-006 | [FUNC] Tương quan Stress | 0-45p | 1. User U07 đăng nhập<br>2. Có event stress<br>3. BP đo trong 0-45p sau | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Tương quan Sự kiện | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3. Hiển thị "HA tăng ngay sau stress trong 0-45 phút" | High | TD_007 |
| TC_HA_019 | BR-006 | [FUNC] Tương quan Caffeine | 30p-2h | 1. User U07 đăng nhập<br>2. Có event uống caffeine<br>3. BP tăng trong 30p-2h | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Tương quan Sự kiện | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3. Hiển thị "HA tăng trong 30p-2h sau caffeine" | Medium | TD_007 |
| TC_HA_020 | BR-006 | [FUNC] Tương quan Rượu | 12-24h | 1. User U07 đăng nhập<br>2. Có event uống rượu<br>3. BP tăng ngày hôm sau | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Tương quan Sự kiện | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3. Hiển thị "HA tăng 12-24h sau uống rượu (phản ứng dội ngược)" | Medium | TD_007 |
| TC_HA_021 | BR-006 | [FUNC] Tương quan Vận động | 30p-2h | 1. User U06 đăng nhập<br>2. Có event vận động<br>3. BP giảm sau 30p-2h | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Tương quan Sự kiện | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3. Hiển thị "HA giảm nhẹ 30p-2h sau vận động (hiệu ứng hạ áp sau tập)" | Medium | TD_006 |
| TC_HA_022 | BR-006 | [FUNC] Tương quan Ăn mặn | 12-24h | 1. User U05 đăng nhập<br>2. Có event ăn mặn<br>3. BP tăng sáng hôm sau | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Tương quan Sự kiện | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3. Hiển thị "HA tăng 12-24h sau ăn mặn (tác động giữ nước)" | Medium | TD_005 |
| TC_HA_023 | BR-007 | [UI] Empty State | Không có data | 1. User U10 đăng nhập<br>2. Không có BP data trong kỳ | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem hiển thị báo cáo | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Hiển thị "Không có đủ dữ liệu để tạo biểu đồ"<br>3.2. Các chỉ số hiển thị "--" | High | TD_010 |
| TC_HA_024 | BR-006 | [UI] Ẩn nhận xét chuyên sâu | <2 lần/ngày | 1. User U11 đăng nhập<br>2. Có <2 lần đo mỗi ngày | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Nhận xét chuyên sâu | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Ẩn các nhận xét ARV, MEdiff<br>3.2. Hiển thị thông báo hướng dẫn đo thêm | Medium | TD_011 |
| TC_HA_025 | BR-006 | [BOUNDARY] High Frequency | 10 lần/ngày | 1. User U14 đăng nhập<br>2. Có 10 lần đo mỗi ngày | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem biểu đồ và nhận xét | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3.1. Biểu đồ hiển thị đầy đủ 10 điểm<br>3.2. Nhận xét tính toán chính xác | Medium | TD_014 |
| TC_HA_026 | BR-005 | [FUNC] Xu hướng TĂNG | vs tuần trước | 1. User U15 đăng nhập<br>2. SYS tuần này cao hơn tuần trước +5 mmHg | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tuần<br>3. Xem phần Xu hướng HA | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tuần hiện tại<br>3. Hiển thị "So với tuần trước, HA có xu hướng TĂNG +5 mmHg" | High | TD_015 |
| TC_HA_027 | BR-005 | [FUNC] Xu hướng GIẢM | vs tháng trước | 1. User U16 đăng nhập<br>2. SYS tháng này thấp hơn tháng trước -12 mmHg | 1. Vào Báo cáo > Báo cáo định kỳ<br>2. Chọn kỳ Tháng<br>3. Xem phần Xu hướng HA | 1. Mở màn Báo cáo định kỳ<br>2. Hiển thị dữ liệu tháng hiện tại<br>3. Hiển thị "So với tháng trước, HA có xu hướng GIẢM -12 mmHg (cải thiện tốt)" | High | TD_016 |

---

## 📏 Numbering Rules Applied

### Pre-condition:
```
1. User U01 đăng nhập
2. has_hypertension = 1
3. Ngưỡng SYS 120-130, DIA 70-80
```

### Steps:
```
1. Vào Báo cáo > Báo cáo định kỳ
2. Chọn kỳ Tuần
3. Xem phần Nhận xét Kiểm soát HA
```

### Expected Output (mapping 1-1 với Step):
```
Step 1 → Expected 1. Mở màn Báo cáo định kỳ
Step 2 → Expected 2. Hiển thị dữ liệu tuần hiện tại
Step 3 (nhiều kết quả) → Expected 3.1., 3.2.
Step 3 (1 kết quả) → Expected 3.
```

---

## 📊 Coverage Summary

| BR | Description | TCs | Count |
|:---|:---|:---|:---:|
| BR-005 | Xu hướng | TC_026, TC_027 | 2 |
| BR-006 | Phân tích chuyên sâu | TC_001-022, TC_024-025 | 24 |
| BR-007 | Empty state | TC_023 | 1 |
| **Total** | | | **27** |

---

## 📁 Data Reference Mapping

| Data Ref | User | Usage |
|:---|:---|:---|
| TD_001 | U01 | TC_001, TC_011, TC_015 |
| TD_002 | U02 | TC_002, TC_012, TC_014, TC_017 |
| TD_003 | U03 | TC_003 |
| TD_004 | U04 | TC_004 |
| TD_005 | U05 | TC_005, TC_022 |
| TD_006 | U06 | TC_006, TC_021 |
| TD_007 | U07 | TC_013, TC_016, TC_018-020 |
| TD_008 | U08 | TC_008 |
| TD_009 | U09 | TC_007 |
| TD_010 | U10 | TC_023 |
| TD_011 | U11 | TC_024 |
| TD_012 | U12 | TC_009 |
| TD_013 | U13 | TC_010 |
| TD_014 | U14 | TC_025 |
| TD_015 | U15 | TC_026 |
| TD_016 | U16 | TC_027 |
