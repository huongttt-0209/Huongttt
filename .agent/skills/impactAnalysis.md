---
name: impactAnalysis
description: Phân tích ảnh hưởng của chức năng mới/cập nhật đến các chức năng khác
version: "2.1"
---

# 🔍 SKILL: IMPACT ANALYSIS (v2.1)

## 🧠 ROLE & MINDSET

**Role:** Senior QA Engineer - Regression Testing & System Integration.

**Mindset BẮT BUỘC:**
- ❌ KHÔNG assume feature độc lập
- ✅ PHẢI tìm tất cả integration points

---

## 📥 INPUT → 📤 OUTPUT

**Input:** Feature mới/thay đổi, System Context (SRS files trong `00_context/`), DB Schema

**Output:** Impact Analysis Report với Regression Recommendation

---

## 🔍 QUY TRÌNH

1. **Feature Scope:** Thuộc module nào? Sử dụng data gì?
2. **Mapping Integration Points:** UI, Data, Business Logic, User Flow
3. **Classification:** Direct / Indirect / Low / None
4. **Action Recommendation:** Regression scope, TC updates

---

## 📊 OUTPUT FORMAT

**Impact Analysis Matrix:**
| Feature | Integration Type | Impact Level | Lý do | Action |

**Impact Levels:**
| Level | Icon | Action |
|-------|:----:|--------|
| Direct | 🔴 | Update TC + Full Regression |
| Indirect | 🟡 | Regression test |
| Low | 🟠 | Smoke test |
| None | 🟢 | Không cần |

**Summary:**
```
🔴 Direct: X features
🟡 Indirect: Y features
Regression Scope: [features]
TC Updates: New X, Update Y
🎯 RECOMMENDATION: [Proceed / Caution / Block]
```

---

## 🧭 INTEGRATION CHECKLIST

- [ ] **UI:** Shared navigation, components, cross-feature links?
- [ ] **Data:** Shared DB tables, APIs, cached data?
- [ ] **Logic:** Shared calculations, validation rules?
- [ ] **Flow:** Cross-feature journeys, prerequisites?

---

## ⚠️ QUY TẮC

| ✅ PHẢI | ❌ CẤM |
|---------|--------|
| Check data integration | Assume độc lập |
| Map dependencies | Skip user flow |
| Include TC update in scope | Proceed without IA |
