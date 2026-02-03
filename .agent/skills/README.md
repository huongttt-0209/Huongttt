# 📚 SKILLS OVERVIEW

> **Version:** Lean 2.x | **Updated:** 2026-01-30

Bộ skills tối ưu cho QA Workflow - Kolia (Mobile Healthcare).

---

## 🎯 SKILL CATALOG

| Skill | Version | Purpose |
|-------|---------|---------|
| [@createTC](./createTC.md) | v2.3 | Viết TC từ SRS |
| [@reviewSRS](./reviewSRS.md) | v2.3 | Review SRS |
| [@reviewTC](./reviewTC.md) | v3.2 | Review TCs |
| [@updateTC](./updateTC.md) | v2.7 | Update TC sau review |
| [@generateTestData](./generateTestData.md) | v2.1 | Tạo Test Data |
| [@generateDBTestData](./generateDBTestData.md) | v2.1 | Tạo CSV cho DB |
| [@impactAnalysis](./impactAnalysis.md) | v2.1 | Phân tích impact |
| [@traceabilityMatrix](./traceabilityMatrix.md) | v2.1 | Tạo RTM |

---

## 🔄 WORKFLOW

```
SRS → @reviewSRS → (Need TD? → @generateTestData) → @createTC → @reviewTC → @updateTC → @traceabilityMatrix

Feature Change → @impactAnalysis → @updateTC
```

---

## ⚡ QUICK REFERENCE

| Situation | Skill | Mode |
|-----------|-------|------|
| Nhận SRS mới | @reviewSRS | Full |
| Viết TC | @createTC | Full/Quick |
| Review TC | @reviewTC | Full |
| Fix TC | @updateTC | Quick |
| Release audit | @traceabilityMatrix | Full |
| Feature change | @impactAnalysis | Full |

---

## 📋 LEAN FORMAT (v2.x)

Mỗi skill có:
- ✅ YAML frontmatter (name, description, version)
- ✅ ROLE & MINDSET (gộp)
- ✅ INPUT → OUTPUT (gộp)
- ✅ QUY TRÌNH
- ✅ QUY TẮC (Golden + Cấm gộp)
- ✅ QUALITY GATE (nếu cần)
