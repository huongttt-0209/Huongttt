# 🎯 TRACEABILITY MATRIX: BP Report

**SRS:** Huongttt_SRS_1.0_bao_cao.md  
**TC:** TC_Bieu_Do_Huyet_Ap.csv  
**Date:** 2026-01-29

---

## 📊 Bảng 1: Requirements Traceability Matrix

| Req ID | Requirement Description | Priority | Test Cases | Coverage | Status |
|:---|:---|:---:|:---|:---:|:---:|
| BR-006.1 | Kiểm soát THA (4 levels: >70%, 50-70%, 25-50%, <25%) | High | TC_001, TC_002, TC_003, TC_004 | 100% | ✅ Covered |
| BR-006.2 | BP Load (3 levels: >30%, 15-30%, <15%) | High | TC_005, TC_006, TC_007 | 100% | ✅ Covered |
| BR-006.3 | Hypotension Load (3 levels: >30%, 15-30%, <15%) | High | TC_008, TC_009, TC_010 | 100% | ✅ Covered |
| BR-006.4 | ARV biến thiên (3 levels: <10, 10-14, >14) | High | TC_011, TC_012, TC_013 | 100% | ✅ Covered |
| BR-006.5 | MEdiff nhịp sinh học (3 patterns: >15, -15~15, <-15) | High | TC_014, TC_015, TC_016 | 100% | ✅ Covered |
| BR-006.6a | Tương quan Thuốc (1-8h) | Medium | TC_017 | 100% | ✅ Covered |
| BR-006.6b | Tương quan Stress (0-45p) | Medium | TC_018 | 100% | ✅ Covered |
| BR-006.6c | Tương quan Caffeine (30p-2h) | Medium | TC_019 | 100% | ✅ Covered |
| BR-006.6d | Tương quan Rượu (12-24h) | Medium | TC_020 | 100% | ✅ Covered |
| BR-006.6e | Tương quan Vận động (30p-2h) | Medium | TC_021 | 100% | ✅ Covered |
| BR-006.6f | Tương quan Ăn mặn (12-24h) | Medium | TC_022 | 100% | ✅ Covered |
| BR-006.7 | Điều kiện >=2 lần đo/ngày | Medium | TC_024 | 100% | ✅ Covered |
| BR-006.8 | High Frequency (>5 lần/ngày) | Low | TC_025 | 100% | ✅ Covered |
| BR-007 | Empty state - Không có dữ liệu | High | TC_023 | 100% | ✅ Covered |
| BR-005.1 | Xu hướng so với tuần trước | High | TC_026 | 100% | ✅ Covered |
| BR-005.2 | Xu hướng so với tháng trước | High | TC_027 | 100% | ✅ Covered |

---

## 📈 Bảng 2: Coverage Summary

| Metric | Value |
|:---|:---:|
| Total Requirements | 16 |
| Fully Covered (100%) | 16 |
| Partially Covered (<100%) | 0 |
| Not Covered (0%) | 0 |
| **Overall Coverage** | **100%** |

---

## 🔍 Bảng 3: Gap Analysis

| Gap Type | ID | Description | Recommendation |
|:---|:---|:---|:---|
| - | - | Không có gap | - |

**✅ Không phát hiện gap nào!**

---

## 🔄 Bảng 4: Test Case → Requirement Reverse Mapping

| TC ID | Testcase Name | Mapped Req | Status |
|:---|:---|:---|:---:|
| TC_001 | Kiểm soát THA Tối ưu (>70%) | BR-006.1 | ✅ |
| TC_002 | Kiểm soát THA Tốt (50-70%) | BR-006.1 | ✅ |
| TC_003 | Kiểm soát THA Kém (25-50%) | BR-006.1 | ✅ |
| TC_004 | Kiểm soát THA Không KS (<25%) | BR-006.1 | ✅ |
| TC_005 | BP Load Gánh nặng (>30%) | BR-006.2 | ✅ |
| TC_006 | BP Load Bình thường (<15%) | BR-006.2 | ✅ |
| TC_007 | BP Load Chớm cao (=15%) | BR-006.2 | ✅ |
| TC_008 | Hypotension Rủi ro (>30%) | BR-006.3 | ✅ |
| TC_009 | Hypotension Ít khi (<15%) | BR-006.3 | ✅ |
| TC_010 | Hypotension Thường xuyên | BR-006.3 | ✅ |
| TC_011 | ARV Ổn định (<10) | BR-006.4 | ✅ |
| TC_012 | ARV Biến động (10-14) | BR-006.4 | ✅ |
| TC_013 | ARV Bất ổn (>14) | BR-006.4 | ✅ |
| TC_014 | MEdiff Morning Surge (>15) | BR-006.5 | ✅ |
| TC_015 | MEdiff Cân bằng (-15~15) | BR-006.5 | ✅ |
| TC_016 | MEdiff Risky Evening (<-15) | BR-006.5 | ✅ |
| TC_017 | Tương quan Thuốc | BR-006.6a | ✅ |
| TC_018 | Tương quan Stress | BR-006.6b | ✅ |
| TC_019 | Tương quan Caffeine | BR-006.6c | ✅ |
| TC_020 | Tương quan Rượu | BR-006.6d | ✅ |
| TC_021 | Tương quan Vận động | BR-006.6e | ✅ |
| TC_022 | Tương quan Ăn mặn | BR-006.6f | ✅ |
| TC_023 | Empty State | BR-007 | ✅ |
| TC_024 | <2 lần đo/ngày | BR-006.7 | ✅ |
| TC_025 | High Frequency | BR-006.8 | ✅ |
| TC_026 | Xu hướng TĂNG | BR-005.1 | ✅ |
| TC_027 | Xu hướng GIẢM | BR-005.2 | ✅ |

**Orphan TCs:** 0 ✅

---

## 🎯 Quality Gate Decision

| Metric | Value | Threshold | Result |
|:---|:---:|:---:|:---:|
| Overall Coverage | 100% | ≥95% | ✅ PASS |
| High Priority Covered | 100% | 100% | ✅ PASS |
| Orphan TCs | 0 | 0 | ✅ PASS |

```
╔═══════════════════════════════════════╗
║     TRACEABILITY QUALITY GATE         ║
╠═══════════════════════════════════════╣
║  Coverage:    100%   ✅ PASS          ║
║  Gaps:        0      ✅ PASS          ║
║  Orphans:     0      ✅ PASS          ║
╠═══════════════════════════════════════╣
║  DECISION:   ✅ PASS                  ║
║  Ready for Testing!                   ║
╚═══════════════════════════════════════╝
```
