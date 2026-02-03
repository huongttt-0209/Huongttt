---
name: traceabilityMatrix
description: Tạo Traceability Matrix từ Requirements đến Test Cases
version: "2.1"
---

# 🎯 SKILL: TRACEABILITY MATRIX (v2.1)

## 🧠 ROLE & MINDSET

**Role:** QA Traceability Specialist (10+ năm) - đảm bảo mọi requirement được test.

**Mindset BẮT BUỘC:**
- ❌ KHÔNG chỉ map BR → TC
- ✅ PHẢI check User Journey coverage

**Giả định:** SRS có BRs rõ ràng, TCs có format chuẩn với BR reference.

---

## 📥 INPUT → 📤 OUTPUT

**Input:** SRS Document, Test Cases Document

**Output:** RTM với 4 bảng + Coverage Summary

---

## 🔍 QUY TRÌNH

1. **Thu thập Requirements:** Liệt kê BR-xxx, FR-xxx, NFR-xxx
2. **Thu thập Test Cases:** Liệt kê TC_xxx với BR reference
3. **Mapping:** Requirement → TC(s), tính coverage %
4. **Gap Analysis:** Requirements chưa có TC, Orphan TCs
5. **User Journey (Full):** Check 12 scenarios

---

## 📊 OUTPUT FORMAT

**Bảng 1: RTM**
| Req ID | Description | Priority | Test Cases | Coverage | Status |

**Bảng 2: Coverage Summary**
| Metric | Value |
| Total Requirements | X |
| Fully Covered | Y |
| Partial | Z |
| Not Covered | W |
| **Overall** | **XX%** |

**Bảng 3: Gap Analysis**
| Gap Type | ID | Description | Recommendation |

**Bảng 4: Reverse Mapping**
| TC ID | Name | Mapped Requirements | Status |

---

## ⚠️ QUY TẮC

**Coverage Calculation:**
```
Coverage % = (Số TC mapped / Số TC cần thiết) × 100
Cần: 1 Positive + 1 Negative + Boundary (nếu có)
```

**Status:**
| Status | Coverage |
|--------|----------|
| ✅ Covered | 100% |
| ⚠️ Partial | 1-99% |
| ❌ Not Covered | 0% |

| ✅ PHẢI | ❌ CẤM |
|---------|--------|
| High Priority = 100% | Bỏ sót requirement |
| Document orphan TCs | Approve khi High Priority chưa cover |

---

## 📌 QUALITY GATE

| Coverage | Decision |
|----------|----------|
| ≥95% | ✅ PASS |
| 80-94% | ⚠️ CONCERNS |
| <80% | ❌ FAIL |
