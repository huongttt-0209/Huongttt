# 🎯 Traceability Matrix: Phân tích Kết quả Tái Khám

> **SRS Ref:** `SRS_Tai_Kham.md` v1.2  
> **TC Ref:** `TC_Phan_Tich_Ket_Qua.md` (41 TCs)  
> **Created:** 2026-01-29  
> **Author:** QA Traceability Specialist

---

## 📊 Bảng 1: Requirements Traceability Matrix

| Req ID | Requirement Description | Priority | Test Cases | Coverage | Status |
|:---|:---|:---:|:---|:---:|:---:|
| BR-001 | Hiển thị Thông tin chung (OCR) - Fallback "Không có thông tin" | Medium | TC_001, TC_002, TC_003, TC_004 | 100% | ✅ Covered |
| BR-002 | Thứ tự ưu tiên nguồn ngưỡng + Phân loại tiến triển | High | TC_005, TC_006, TC_007, TC_008, TC_009, TC_027, TC_028, TC_029, TC_030, TC_031, TC_037, TC_038, TC_041 | 100% | ✅ Covered |
| BR-003 | Hiển thị nguồn ngưỡng (VD: "Theo ADA 2024") | High | TC_005 (combined) | 100% | ✅ Covered |
| BR-004 | Fallback không có lịch sử - Hiển thị "Chưa có" | Medium | TC_010 | 100% | ✅ Covered |
| BR-005 | Fallback không có ngưỡng - "Chưa có ngưỡng tham chiếu" | Medium | TC_011 | 100% | ✅ Covered |
| BR-006 | Icon 💬 CHỈ hiển thị với "Cần chú ý" → mở Chat Kolia | Medium | TC_012, TC_013, TC_014, TC_040 | 100% | ✅ Covered |
| BR-007 | Safety: AI KHÔNG khuyến nghị liều thuốc | High | TC_015 | 100% | ✅ Covered |
| BR-008 | Safety: AI KHÔNG chẩn đoán bệnh | High | TC_016, TC_039 | 100% | ✅ Covered |
| BR-009 | Disclaimer bắt buộc cuối màn hình | High | TC_017 | 100% | ✅ Covered |
| BR-010 | TTS chỉ hoạt động khi có kết nối mạng | Medium | TC_018, TC_019 | 100% | ✅ Covered |
| BR-011 | OCR Error: Hiển thị cảnh báo + hướng dẫn + nút "Thử lại" | High | TC_020, TC_021 | 100% | ✅ Covered |
| BR-012 | Multi-page: Gộp kết quả + ghi chú "Đã phân tích X/X trang" | Medium | TC_022 | 100% | ✅ Covered |
| BR-013 | Siêu âm/X-quang: Ghi chú không hỗ trợ (ERR-002) | Medium | TC_023, TC_024, TC_036 | 100% | ✅ Covered |
| BR-014 | Network/Timeout (>15s): Hiển thị lỗi + nút Thử lại | High | TC_025 | 100% | ✅ Covered |
| BR-015 | User Profile fallback: Dùng ngưỡng quốc tế mặc định | Medium | TC_026, TC_032, TC_033, TC_034, TC_035 | 100% | ✅ Covered |

---

## 📊 Bảng 2: Coverage Summary

| Metric | Value |
|:---|:---:|
| Total Requirements | 15 |
| Fully Covered (100%) | 15 |
| Partially Covered (<100%) | 0 |
| Not Covered (0%) | 0 |
| **Overall Coverage** | **100%** |

---

## 📊 Bảng 3: Error Messages Coverage

| Error Code | Message | Test Cases | Status |
|:---|:---|:---|:---:|
| ERR-001 | "Không nhận diện được kết quả tái khám từ ảnh" | TC_020, TC_021 | ✅ Covered |
| ERR-002 | "Ảnh siêu âm/X-quang chưa được hỗ trợ..." | TC_023, TC_024, TC_036 | ✅ Covered |
| ERR-003 | "Không thể kết nối. Vui lòng kiểm tra mạng..." | TC_025 | ✅ Covered |
| ERR-004 | "TTS cần kết nối mạng" | TC_019 | ✅ Covered |

---

## 📊 Bảng 4: Gap Analysis

| Gap Type | ID | Description | Recommendation |
|:---|:---|:---|:---|
| - | - | Không phát hiện gaps | - |

**✅ Không có Missing TC, Orphan TC, hoặc Low Coverage**

---

## 📊 Bảng 5: Test Case → Requirement Reverse Mapping

| TC ID | Testcase Name | Mapped Requirements | Status |
|:---|:---|:---|:---:|
| TC_001 | [FUNC] Hiển thị Thông tin chung đầy đủ | BR-001 | ✅ Mapped |
| TC_002 | [FUNC] Thông tin chung - Thiếu Bác sĩ | BR-001 | ✅ Mapped |
| TC_003 | [FUNC] Thông tin chung - Thiếu Ngày khám | BR-001 | ✅ Mapped |
| TC_004 | [EDGE] Thông tin chung - Thiếu nhiều field | BR-001 | ✅ Mapped |
| TC_005 | [FUNC] Phân loại Cải thiện | BR-002, BR-003 | ✅ Mapped |
| TC_006 | [FUNC] Phân loại Duy trì tốt | BR-002 | ✅ Mapped |
| TC_007 | [FUNC] Phân loại Cần chú ý - Trong ngưỡng xấu đi | BR-002, BR-006 | ✅ Mapped |
| TC_008 | [FUNC] Phân loại Cần chú ý - Ngoài ngưỡng có cải thiện | BR-002 | ✅ Mapped |
| TC_009 | [FUNC] Phân loại Cần chú ý - Ngoài ngưỡng xấu đi | BR-002 | ✅ Mapped |
| TC_010 | [EDGE] Không có lịch sử chỉ số | BR-004 | ✅ Mapped |
| TC_011 | [EDGE] Chỉ số không có ngưỡng | BR-005 | ✅ Mapped |
| TC_012 | [FUNC] Icon 💬 hiển thị với Cần chú ý | BR-006 | ✅ Mapped |
| TC_013 | [FUNC] Icon 💬 KHÔNG hiển thị với Cải thiện | BR-006 | ✅ Mapped |
| TC_014 | [FUNC] Nhấn icon 💬 mở Chat Kolia | BR-006 | ✅ Mapped |
| TC_015 | [SAFETY] AI không khuyến nghị liều thuốc | BR-007 | ✅ Mapped |
| TC_016 | [SAFETY] AI không chẩn đoán bệnh | BR-008 | ✅ Mapped |
| TC_017 | [FUNC] Disclaimer hiển thị | BR-009 | ✅ Mapped |
| TC_018 | [FUNC] TTS thành công | BR-010 | ✅ Mapped |
| TC_019 | [ERR] TTS offline | BR-010 | ✅ Mapped |
| TC_020 | [ERR] OCR không nhận diện - Ảnh mờ | BR-011 | ✅ Mapped |
| TC_021 | [ERR] OCR không nhận diện - Không phải phiếu XN | BR-011 | ✅ Mapped |
| TC_022 | [FUNC] Multi-page - Tất cả hợp lệ | BR-012 | ✅ Mapped |
| TC_023 | [EDGE] Multi-page có siêu âm | BR-013 | ✅ Mapped |
| TC_024 | [ERR] Upload ảnh siêu âm | BR-013 | ✅ Mapped |
| TC_025 | [ERR] Network timeout | BR-014 | ✅ Mapped |
| TC_026 | [EDGE] User không có hồ sơ bệnh nền | BR-015 | ✅ Mapped |
| TC_027 | [EDGE] Ngưỡng cá nhân hóa - Người già | BR-002 | ✅ Mapped |
| TC_028 | [EDGE] Ngưỡng cá nhân hóa - Suy thận mạn | BR-002 | ✅ Mapped |
| TC_029 | [EDGE] Ngưỡng cá nhân hóa - Sau đột quỵ | BR-002 | ✅ Mapped |
| TC_030 | [EDGE] Multi-disease: TĐ + THA | BR-002 | ✅ Mapped |
| TC_031 | [EDGE] Multi-disease: TĐ + Người già | BR-002 | ✅ Mapped |
| TC_032 | [EDGE] Mang thai + Glucose = 95 (boundary) | BR-015 | ✅ Mapped |
| TC_033 | [EDGE] Mang thai + BP cao | BR-015 | ✅ Mapped |
| TC_034 | [BOUNDARY] Mang thai - Glucose trong ngưỡng | BR-015 | ✅ Mapped |
| TC_035 | [BOUNDARY] Mang thai - Glucose ngoài ngưỡng | BR-015 | ✅ Mapped |
| TC_036 | [ERR] Upload ảnh X-quang | BR-013 | ✅ Mapped |
| TC_037 | [FUNC] AI Comment - Cải thiện | BR-002 | ✅ Mapped |
| TC_038 | [FUNC] AI Comment - Cần chú ý | BR-002 | ✅ Mapped |
| TC_039 | [SAFETY] AI Comment không chẩn đoán | BR-008 | ✅ Mapped |
| TC_040 | [FUNC] Icon 💬 KHÔNG hiển thị với Duy trì tốt | BR-006 | ✅ Mapped |
| TC_041 | [EDGE] Viêm gan B - HBV-DNA Undetectable | BR-002 | ✅ Mapped |

**Orphan TCs: 0** ✅

---

## 🎯 Quality Gate Decision

```
╔════════════════════════════════════════════════════════════╗
║             TRACEABILITY MATRIX QUALITY GATE               ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  Overall Coverage: 100%                                    ║
║                                                            ║
║  ─────────────────────────────────────────────────────────  ║
║  METRICS:                                                  ║
║  ├─ Requirements Covered:  15/15 (100%)            ✅      ║
║  ├─ Error Codes Covered:   4/4 (100%)              ✅      ║
║  ├─ Orphan TCs:            0                       ✅      ║
║  ├─ High Priority BRs:     8/8 (100%)              ✅      ║
║  └─ Medium Priority BRs:   7/7 (100%)              ✅      ║
║                                                            ║
║  ─────────────────────────────────────────────────────────  ║
║                                                            ║
║  🎯 DECISION: ✅ PASS - Ready for Testing                  ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

---

## 📋 Recommendations

| # | Category | Recommendation | Status |
|:---:|:---|:---|:---:|
| 1 | Missing TC | None identified | ✅ |
| 2 | Orphan TC | None identified | ✅ |
| 3 | Low Coverage | None identified | ✅ |

**Overall Test Readiness: ✅ READY**
