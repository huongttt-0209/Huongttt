# Test Data: Phân tích Kết quả Tái Khám

**SRS Reference:** @SRS_Tai_Kham.md
**Created:** 2026-01-29
**Author:** AI + QA Team

---

## 1. Data Overview (Tổng quan các fields)

| Field ID | Field Name | Data Type | Constraints | BR Reference |
|----------|------------|-----------|-------------|--------------|
| F_001 | exam_date | Date | OCR từ phiếu hoặc ngày upload | BR-001 |
| F_002 | specialty | String | OCR từ phiếu | BR-001 |
| F_003 | doctor_name | String | OCR hoặc "Không có thông tin" | BR-001 |
| F_004 | medical_facility | String | OCR từ phiếu | BR-001 |
| F_005 | test_value | Number | Giá trị chỉ số (VD: HbA1c, LDL) | BR-002, BR-003 |
| F_006 | threshold_source | Enum | Phiếu XN / Cá nhân hóa / Quốc tế | BR-002 |
| F_007 | previous_value | Number | Lần khám trước (có thể null) | BR-004 |
| F_008 | classification | Enum | Cải thiện / Duy trì tốt / Cần chú ý | BR-002 |
| F_009 | uploaded_images | Array | 1-n ảnh phiếu kết quả | BR-012, BR-013 |

---

## 2. Test Data: Chỉ số Xét nghiệm

### 2.1 HbA1c (Đường huyết)

| Data ID | Scenario | Current Value | Previous Value | Threshold | Classification | Expected |
|---------|----------|---------------|----------------|-----------|----------------|----------|
| TD_001 | V-Cải thiện | 6.8% | 7.5% | <7% (ADA) | ✅ Cải thiện | Card xanh lá |
| TD_002 | V-Duy trì tốt | 6.5% | 6.4% | <7% (ADA) | 💚 Duy trì tốt | Card xanh dương |
| TD_003 | V-Cần chú ý (trong ngưỡng) | 6.9% | 6.5% | <7% (ADA) | ⚠️ Cần chú ý | Card vàng + icon 💬 |
| TD_004 | V-Cần chú ý (ngoài ngưỡng) | 7.2% | 7.8% | <7% (ADA) | ⚠️ Cần chú ý (có cải thiện) | Card vàng + icon 💬 |
| TD_005 | V-Ngoài ngưỡng xấu đi | 8.0% | 7.5% | <7% (ADA) | ⚠️ Cần chú ý | Card vàng + icon 💬 |
| TD_006 | Edge-Không có lịch sử | 6.8% | null | <7% (ADA) | Chưa có | Hiển thị "Chưa có" |
| TD_007 | Edge-Người già (>65 tuổi) | 7.5% | 7.8% | <8% (ADA Geriatric) | ✅ Cải thiện | Ngưỡng cá nhân hóa, user age=70 |

### 2.2 eGFR (Chức năng thận)

| Data ID | Scenario | Current Value | Previous Value | Threshold | Classification | Expected |
|---------|----------|---------------|----------------|-----------|----------------|----------|
| TD_008 | V-Duy trì tốt | 92 mL/min | 90 mL/min | >60 (KDIGO) | 💚 Duy trì tốt | Card xanh dương |
| TD_009 | V-Cần chú ý | 55 mL/min | 62 mL/min | >60 (KDIGO) | ⚠️ Cần chú ý | Card vàng + icon 💬 |
| TD_010 | Edge-Suy thận mạn | 45 mL/min | 48 mL/min | Duy trì ổn định (KDIGO) | 💚 Duy trì tốt | Ngưỡng cá nhân hóa |

### 2.3 AST/ALT (Men gan)

| Data ID | Scenario | Current Value | Previous Value | Threshold | Classification | Expected |
|---------|----------|---------------|----------------|-----------|----------------|----------|
| TD_011 | V-Cần chú ý | 45 U/L | 38 U/L | <40 U/L (AASLD) | ⚠️ Cần chú ý | Card vàng + icon 💬 |
| TD_012 | V-Duy trì tốt | 35 U/L | 36 U/L | <40 U/L (AASLD) | 💚 Duy trì tốt | Card xanh dương |

### 2.4 LDL (Mỡ máu)

| Data ID | Scenario | Current Value | Previous Value | Threshold | Classification | Expected |
|---------|----------|---------------|----------------|-----------|----------------|----------|
| TD_013 | V-Normal | 2.5 mmol/L | 2.8 mmol/L | <2.6 (ESC) | ✅ Cải thiện | Card xanh lá |
| TD_014 | V-High Risk (sau đột quỵ) | 1.3 mmol/L | 1.5 mmol/L | <1.4 (ESC) | ✅ Cải thiện | Ngưỡng cá nhân hóa |
| TD_015 | Boundary - LDL = 1.4 | 1.4 mmol/L | 1.6 mmol/L | <1.4 (ESC) | ⚠️ Cần chú ý | 1.4 không < 1.4 |

---

## 3. Test Data: Thông tin chung (OCR)

| Data ID | Scenario | Ngày khám | Chuyên khoa | Bác sĩ | CSYT | Expected |
|---------|----------|-----------|-------------|--------|------|----------|
| TD_020 | V-Đầy đủ thông tin | 15/01/2026 | Nội tiết | Bs. Nguyễn Văn A | BV Đại học Y D... | Hiển thị đầy đủ |
| TD_021 | V-Thiếu bác sĩ | 15/01/2026 | Tim mạch | null | BV XYZ | BS = "Không có thông tin" |
| TD_022 | V-Thiếu ngày (dùng ngày upload) | null | Thận | Bs. Trần B | BV ABC | Ngày = ngày upload |
| TD_023 | Edge-Thiếu nhiều field | null | null | null | null | Tất cả hiển thị "Không có thông tin" |

---

## 4. Test Data: Upload & OCR

| Data ID | Scenario | Số trang | Loại ảnh | Expected | BR Ref |
|---------|----------|----------|----------|----------|--------|
| TD_030 | V-1 trang rõ nét | 1 | Phiếu XN | "Đã phân tích 1/1 trang" | BR-012 |
| TD_031 | V-Nhiều trang | 3 | Phiếu XN | "Đã phân tích 3/3 trang" | BR-012 |
| TD_032 | I-Ảnh mờ | 1 | Mờ/Tối | ERR-001: "Không nhận diện được kết quả" | BR-011 |
| TD_033 | I-Ảnh siêu âm | 1 | Siêu âm | ERR-002: "Ảnh siêu âm chưa được hỗ trợ" | BR-013 |
| TD_034 | I-Ảnh X-quang | 1 | X-quang | ERR-002: "Ảnh X-quang chưa được hỗ trợ" | BR-013 |
| TD_035 | Edge-Mix pages | 3 | 2 XN + 1 siêu âm | "Đã phân tích 2/3 trang" + lý do | BR-013 |
| TD_036 | I-Không phải phiếu XN | 1 | Selfie/Ảnh khác | ERR-001: "Không nhận diện được" | BR-011 |

---

## 5. Test Data: Network & TTS

| Data ID | Scenario | Condition | Action | Expected | BR Ref |
|---------|----------|-----------|--------|----------|--------|
| TD_040 | I-Timeout | Network delay >15s | Chờ phân tích | ERR-003: "Không thể kết nối..." + nút Thử lại | BR-014 |
| TD_041 | I-Network offline | No connection | Nhấn TTS | ERR-004: "TTS cần kết nối mạng" | BR-010 |
| TD_042 | V-TTS success | Online | Nhấn icon 🔊 | Đọc nội dung section | BR-010 |
| TD_043 | Edge - AI > 10s | Slow processing | Upload ảnh | Hiển thị "Đang xử lý, vui lòng đợi..." | BR-014 |

---

## 6. Test Data: Chat Kolia (Icon 💬)

| Data ID | Scenario | Chỉ số | Classification | Expected | BR Ref |
|---------|----------|--------|----------------|----------|--------|
| TD_050 | V-Icon hiển thị | HbA1c 7.2% | Cần chú ý | Có icon 💬 | BR-006 |
| TD_051 | V-Icon không hiển thị | HbA1c 6.5% | Cải thiện | KHÔNG có icon 💬 | BR-006 |
| TD_052 | V-Nhấn icon chat | AST 45 U/L | Cần chú ý | Mở Chat với context | BR-006 |

---

## 7. Test Data: User Profile

| Data ID | Scenario | Có hồ sơ bệnh nền? | Bệnh nền | Threshold used | BR Ref |
|---------|----------|-------------------|---------  |----------------|--------|
| TD_060 | V-Có hồ sơ tiểu đường | ✅ | Tiểu đường | <7% (ADA cá nhân hóa) | BR-015 |
| TD_061 | V-Có hồ sơ người già | ✅ | Người >65 tuổi | <8% (ADA Geriatric) | BR-015 |
| TD_062 | Edge-Không có hồ sơ | ❌ | null | Ngưỡng quốc tế mặc định | BR-015 |

---

## 8. Test Data: Chỉ số không có ngưỡng

| Data ID | Scenario | Chỉ số | Value | Threshold | Expected | BR Ref |
|---------|----------|--------|-------|-----------|----------|--------|
| TD_070 | Edge-Không có ngưỡng | Chỉ số mới XYZ | 123 | null | "Chưa có ngưỡng tham chiếu" + "Tham khảo ý kiến BS" | BR-005 |

---

## 9. Test Data: Safety Rules

| Data ID | Scenario | BR Ref | Input | Expected |
|---------|----------|--------|-------|----------|
| TD_080 | V-Không khuyến nghị liều thuốc | BR-007 | Phiếu có đơn thuốc "Metformin 500mg" | Chỉ hiển thị OCR đơn thuốc, KHÔNG có text "nên uống X mg" |
| TD_081 | V-Không chẩn đoán bệnh | BR-008 | HbA1c = 7.2% (ngoài ngưỡng) | KHÔNG có text "Bạn bị tiểu đường", chỉ có "Cần chú ý" |
| TD_082 | V-Disclaimer hiển thị | BR-009 | Bất kỳ kết quả nào | Cuối màn hình có disclaimer đúng format |

---

## 10. Test Data: AI Comment Content (PM Review)

| Data ID | Scenario | Chỉ số | Classification | Expected AI Comment | BR Ref |
|---------|----------|--------|----------------|---------------------|--------|
| TD_090 | V-Comment Cải thiện | HbA1c 6.8% (từ 7.5%) | ✅ Cải thiện | "Chỉ số đã cải thiện so với lần khám trước" | BR-002 |
| TD_091 | V-Comment Cần chú ý | HbA1c 7.2% | ⚠️ Cần chú ý | "Chỉ số ngoài ngưỡng mục tiêu, cần theo dõi" | BR-002 |
| TD_092 | V-Comment không chẩn đoán | HbA1c 8.0% | ⚠️ Cần chú ý | KHÔNG có "Bạn bị tiểu đường", chỉ nêu facts | BR-008 |

---

## 11. Test Data: Multi-Disease Profile (PM Review)

| Data ID | Scenario | Bệnh nền | Chỉ số | Threshold Applied | Expected | BR Ref |
|---------|----------|----------|--------|-------------------|----------|--------|
| TD_100 | Edge-TĐ + THA | Tiểu đường + Tăng HA | HbA1c 7.0% | <7% (ADA - stricter) | Dùng ngưỡng strict nhất | BR-002 |
| TD_101 | Edge-TĐ + Người già | Tiểu đường + >65 tuổi | HbA1c 7.5% | <8% (ADA Geriatric) | Ưu tiên ngưỡng người già | BR-015 |
| TD_102 | Edge-Sau đột quỵ + THA | Đột quỵ + Tăng HA | LDL 1.5 mmol/L | <1.4 (ESC High Risk) | Dùng ngưỡng strict nhất | BR-002 |

---

## 12. Test Data: Pregnancy (ACOG) (PM Review)

| Data ID | Scenario | Profile | Chỉ số | Threshold | Classification | Expected | BR Ref |
|---------|----------|---------|--------|-----------|----------------|----------|--------|
| TD_110 | V-Mang thai + Glucose | Mang thai 20 tuần | Glucose 95 mg/dL | <95 (ACOG) | 💚 Duy trì tốt | Ngưỡng ACOG | BR-015 |
| TD_111 | V-Mang thai + BP cao | Mang thai 28 tuần | BP 145/95 | <140/90 (ACOG) | ⚠️ Cần chú ý | Cảnh báo tiền sản giật | BR-015 |
| TD_112 | Edge-Mang thai + TĐ thai kỳ | Mang thai + GDM | HbA1c 6.5% | <6.5% (ACOG) | 💚 Duy trì tốt | Ngưỡng ACOG cho GDM | BR-015 |
| TD_113 | Boundary-Glucose trong | Mang thai 24 tuần | Glucose 94 mg/dL | <95 (ACOG) | 💚 Duy trì tốt | Exactly under threshold | BR-015 |
| TD_114 | Boundary-Glucose ngoài | Mang thai 24 tuần | Glucose 96 mg/dL | <95 (ACOG) | ⚠️ Cần chú ý | Just over threshold | BR-015 |

---

## Summary

| Category | Total Test Data |
|----------|-----------------|
| Chỉ số Xét nghiệm | 14 (TD_001 - TD_014) |
| Thông tin chung OCR | 4 (TD_020 - TD_023) |
| Upload & OCR | 7 (TD_030 - TD_036) |
| Network & TTS | 3 (TD_040 - TD_042) |
| Chat Kolia | 3 (TD_050 - TD_052) |
| User Profile | 3 (TD_060 - TD_062) |
| Không có ngưỡng | 1 (TD_070) |
| Safety Rules | 3 (TD_080 - TD_082) |
| AI Comment Content | 3 (TD_090 - TD_092) |
| Multi-Disease Profile | 3 (TD_100 - TD_102) |
| Pregnancy (ACOG) | 5 (TD_110 - TD_114) |
| Viêm gan B (AASLD) | 1 (TD_120) |
| **TOTAL** | **50 Test Data entries** |

---

## 13. Test Data: Viêm gan B (AASLD)

| Data ID | Scenario | Current Value | Previous Value | Threshold | Classification | Expected | BR Ref |
|---------|----------|---------------|----------------|-----------|----------------|----------|--------|
| TD_120 | V-HBV-DNA Undetectable | Undetectable | 500 IU/mL | Undetectable (AASLD) | ✅ Cải thiện | Đạt ngưỡng điều trị | BR-002 |
