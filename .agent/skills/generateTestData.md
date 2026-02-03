---
name: generateTestData
description: Tạo Test Data chi tiết từ SRS và Business Rules
version: "2.1"
---

# 🎯 SKILL: GENERATE TEST DATA (v2.1)

## 🧠 ROLE & MINDSET

**Role:** Senior QA Data Engineer (15+ năm) - thiết kế test data khoa học.

**Mindset BẮT BUỘC:**
- ❌ KHÔNG chỉ tạo data cho happy path
- ✅ PHẢI cover boundary, negative, edge cases

**Giả định:** SRS đã review, BRs rõ ràng, Data Complexity Score ≥8 (từ @reviewSRS).

---

## 📥 INPUT → 📤 OUTPUT

**Input:** SRS đã review, Business Rules

**Output:** `TD_[Tên Feature].md` (VD: `TD_Tai_Kham.md`)

---

## 🔍 QUY TRÌNH

1. **Phân tích Input Fields:** data type, constraints (min, max, format)
2. **Equivalence Partitioning:** Valid + Invalid partitions
3. **Boundary Value Analysis:** Min, Min-1, Min+1, Max, Max-1, Max+1
4. **Special Cases:** Empty/Null, special chars, unicode, whitespace
5. **Domain Y tế:** BP values, Thuốc, Thời gian

---

## 📊 OUTPUT FORMAT

**Bảng 1: Data Overview**
| Field ID | Field Name | Data Type | Constraints | BR Reference |

**Bảng 2: Test Data Values**
| Data ID | Field ID | Scenario Type | Test Value | Expected Result | TC Ref |

**Bảng 3: Data Combinations (Full Mode)**
| Combo ID | Field 1 | Field 2 | Expected | TC Ref |

---

## ⚠️ QUY TẮC

| Item | Format/Rule |
|------|-------------|
| Data ID | `TD_001`, `TD_002`, ... |
| Scenario Types | Valid, BMin, BMax, Invalid-[Reason], Empty, Edge |
| Expected | Cụ thể: `❌ "Phải có 10 chữ số"` |
| TC Reference | `TC_001` hoặc `TBD` |

| ✅ PHẢI | ❌ CẤM |
|---------|--------|
| Cover boundary cases | Tạo data ngoài SRS |
| Expected cụ thể | Dùng data thật (PII) |
| Mỗi scenario = 1 entry | Gộp nhiều scenarios |
