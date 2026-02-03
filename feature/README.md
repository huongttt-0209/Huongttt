# 📁 Feature Folder Structure

Folder này chứa tất cả tài liệu theo cấu trúc **Hybrid** - mỗi feature một folder riêng.

## 📋 Cấu trúc chuẩn cho mỗi feature:

```
feature/
└── [tên_feature]/
    ├── README.md                    # Mô tả feature
    ├── SRS_[Feature].md             # SRS từ BA
    ├── TD_[Feature].md              # Test Data (nếu Score ≥ 8)
    ├── TC_[Feature].md              # Test Cases
    └── TM_[Feature].md              # Traceability Matrix
```

## 📂 Danh sách Features:

| Feature | Folder | Status |
|---------|--------|--------|
| Tái Khám | `tai_kham/` | 🔄 In Progress |
| SOS | `sos/` | ⏳ Pending |
| Báo Cáo | `bao_cao/` | ⏳ Pending |

## 🔄 Workflow cho mỗi feature:

```
1. @reviewSRS.md     → Review SRS + Data Complexity Score
2. @generateTestData → Tạo TD (nếu Score ≥ 8)
3. @createTC.md      → Tạo TC
4. @reviewTC.md      → Review TC
5. @updateTC.md      → Update TC (nếu cần)
6. @traceabilityMatrix → Tạo TM
```

## ⚡ Quick Start:

```bash
# Step 1: Review SRS
@reviewSRS.md @feature/tai_kham/SRS_Tai_Kham.md

# Step 2: Tạo Test Data (nếu cần)
@generateTestData.md @feature/tai_kham/SRS_Tai_Kham.md

# Step 3: Tạo Test Cases
@createTC.md @feature/tai_kham/SRS_Tai_Kham.md
```
