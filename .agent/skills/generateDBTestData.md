---
name: generateDBTestData
description: Tạo Test Data dạng CSV để Dev import vào Database
version: "2.1"
---

# 🎯 SKILL: GENERATE DB TEST DATA (v2.1)

## 🧠 ROLE & MINDSET

**Role:** Test Data Engineer - tạo CSV phù hợp cấu trúc DB.

**Mindset BẮT BUỘC:**
- ❌ KHÔNG tạo data vi phạm constraints
- ✅ PHẢI đảm bảo FK integrity và import order

---

## 📥 INPUT → 📤 OUTPUT

**Input:** TD_*.md, Database Schema, SRS

**Output:** Folder `csv/` với README + CSV files theo thứ tự import

```
csv/
├── README.md              # Import order + notes
├── 01_users.csv           # Parent table first
├── 02_health_profiles.csv
└── ...
```

---

## 🔍 QUY TRÌNH

1. **Phân tích Schema:** tables, columns, FK relationships
2. **Map TD → CSV:** mỗi scenario → records
3. **Tạo CSV:** Header = tên cột DB, UTF-8, comma-separated

---

## ⚠️ QUY TẮC

| Item | Format/Rule |
|------|-------------|
| ID | Unique, consistent (UUID/sequential) |
| FK | Phải tồn tại trong bảng parent |
| Date/Time | `YYYY-MM-DD HH:MM:SS` |
| Status | Số/string theo schema, ghi chú trong README |

| ✅ PHẢI | ❌ CẤM |
|---------|--------|
| Parent table trước child | Vi phạm FK constraints |
| Document import order | Duplicate PK |
| UTF-8 encoding | Mixed date formats |

---

## ✅ VALIDATION CHECKLIST

- [ ] FK tồn tại trong parent
- [ ] Không duplicate PK
- [ ] Date format nhất quán
- [ ] README có import order
