---
description: Workflow hoàn chỉnh cho Tester từ review SRS đến Ready for Testing
---

# 🧪 Tester Workflow FINAL - Dự án Kolia

## 🚀 WORKFLOW V5.1 (+ Impact Analysis)

```
┌────────────────────────────────────────────────────────────────────────────┐
│                        ✏️ TESTER WORKFLOW V5.1                              │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  📥 INPUT: SRS từ BA                                                        │
│       │                                                                     │
│       ▼                                                                     │
│  ╔══════════════════════════════════════════════════════════════════════╗  │
│  ║ SRS mới hay SRS update?                                              ║  │
│  ╠══════════════════════════════════════════════════════════════════════╣  │
│  ║                                                                       ║  │
│  ║   NEW SRS                              UPDATE SRS                    ║  │
│  ║      │                                      │                         ║  │
│  ║      │                                      ▼                         ║  │
│  ║      │                    ┌─────────────────────────────────────┐    ║  │
│  ║      │                    │ STEP 0: @impactAnalysis.md  ⭐ NEW  │    ║  │
│  ║      │                    │ ├─ Xác định features bị ảnh hưởng   │    ║  │
│  ║      │                    │ ├─ TCs cần update                   │    ║  │
│  ║      │                    │ └─ Regression scope                 │    ║  │
│  ║      │                    │ 💡 VD: @impactAnalysis.md Phân tích │    ║  │
│  ║      │                    │    impact của @SRS_v2.md            │    ║  │
│  ║      │                    └─────────────────────────────────────┘    ║  │
│  ║      │                                      │                         ║  │
│  ║      └──────────────────────┬───────────────┘                         ║  │
│  ╚═════════════════════════════╧════════════════════════════════════════╝  │
│                                │                                            │
│                                ▼                                            │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │ STEP 1: @reviewSRS.md                                                 │  │
│  │ ├─ Task 1-6: Review testability, issues, risks, scenarios           │  │
│  │ └─ Task 7: DATA COMPLEXITY ASSESSMENT ⭐                             │  │
│  │           → Output: Score X điểm → Cần/Không cần Test Data riêng    │  │
│  │ 💡 VD: @reviewSRS.md Review SRS @feature/tai_kham/SRS_Tai_Kham.md    │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│       │                                                                     │
│       │  🔍 REVIEW: /analyst nếu cần clarify                               │
│       │                                                                     │
│  SRS OK? ─ NO → Gửi lại BA                                                  │
│       │                                                                     │
│       ▼ YES                                                                 │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │ STEP 2 (Optional): /tea → TD                                          │  │
│  │ └─ Cho features lớn, cần test strategy                               │  │
│  │ 💡 VD: /tea Tôi cần TD cho feature Tái Khám. SRS: @SRS_Tai_Kham.md   │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│       │                                                                     │
│       │  🔍 REVIEW: /analyst (scenarios) + /pm (scope)                     │
│       │                                                                     │
│       ▼                                                                     │
│  ╔══════════════════════════════════════════════════════════════════════╗  │
│  ║ DECISION: Cần Test Data riêng không? (từ Task 7)                     ║  │
│  ╠══════════════════════════════════════════════════════════════════════╣  │
│  ║                                                                       ║  │
│  ║   Score ≥ 8 điểm                    Score < 8 điểm                   ║  │
│  ║        │                                  │                           ║  │
│  ║        ▼                                  ▼                           ║  │
│  ║   STEP 3A: @generateTestData.md      STEP 3B: Skip                   ║  │
│  ║   └─ Output: TD_Feature.md           └─ Ghi data trực tiếp trong TC  ║  │
│  ║ 💡 VD: @generateTestData.md Tạo TD cho @SRS.md. Lưu TD_Tai_Kham.md   ║  │
│  ╚════════════════════════════╤═════════════════════════════════════════╝  │
│                               │                                             │
│                               ▼                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │ STEP 4: @createTC.md                                                  │  │
│  │ ├─ Output: TC_Feature.md                                             │  │
│  │ └─ Cột Data Ref: link đến TD_xxx hoặc "-"                           │  │
│  │ 💡 VD: @createTC.md Tạo TC cho @SRS.md với data @TD_Tai_Kham.md      │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│       │                                                                     │
│       ▼                                                                     │
│  ╔══════════════════════════════════════════════════════════════════════╗  │
│  ║                        🔍 QUALITY GATE                                ║  │
│  ╠══════════════════════════════════════════════════════════════════════╣  │
│  ║  Step 1: @reviewTC.md         → Self Review                          ║  │
│  ║  Step 2: /analyst             → Requirements check (BẮT BUỘC)        ║  │
│  ║  Step 3: /dev                 → Technical check (TÙY CHỌN)           ║  │
│  ║  Step 4: /tea → RV            → Best practices (TÙY CHỌN)            ║  │
│  ║  HOẶC: /bmad_party-mode       → Cho TC critical (Y tế, SOS)          ║  │
│  ║ 💡 VD: @reviewTC.md Review @TC.md dựa trên @SRS.md                   ║  │
│  ╚════════════════════════════════╤═════════════════════════════════════╝  │
│                                   │                                         │
│  Issues? ─ YES → @updateTC.md → Quay lại Quality Gate                      │
│  💡 VD: @updateTC.md Update @TC_Tai_Kham.md theo review report             │
│                                   │                                         │
│                                   ▼ NO                                      │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │ STEP 5: @traceabilityMatrix.md                                        │  │
│  │ └─ Output: Coverage Report + Quality Gate Decision                   │  │
│  │ 💡 VD: @traceabilityMatrix.md Tạo TM cho @SRS.md và @TC_Tai_Kham.md  │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│       │                                                                     │
│  Coverage ≥ 95%? ─ NO → Bổ sung TC → Quay lại Step 4                       │
│                                   │                                         │
│                                   ▼ YES                                     │
│                          ✅ READY FOR TESTING                               │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 📝 VÍ DỤ CÁCH VIẾT YÊU CẦU

### Step 0: Impact Analysis (cho SRS update)
```
@impactAnalysis.md Phân tích impact của @feature/tai_kham/SRS_Tai_Kham_v2.md so với v1
```

### Step 1: Review SRS
```
@reviewSRS.md Review SRS cho feature Tái Khám @feature/tai_kham/SRS_Tai_Kham.md
```

### Step 2: Test Design (Optional)
```
/tea Tôi cần TD (Test Design) cho feature Tái Khám. SRS: @feature/tai_kham/SRS_Tai_Kham.md
```

### Step 3A: Tạo Test Data (nếu Score ≥ 8)
```
@generateTestData.md Tạo test data cho @feature/tai_kham/SRS_Tai_Kham.md. Lưu vào TD_Tai_Kham.md
```

### Step 4: Tạo Test Cases
```
@createTC.md Tạo test cases cho @feature/tai_kham/SRS_Tai_Kham.md với test data @feature/tai_kham/TD_Tai_Kham.md
```

### Step 5: Review Test Cases
```
@reviewTC.md Review @feature/tai_kham/TC_Tai_Kham.md dựa trên @feature/tai_kham/SRS_Tai_Kham.md
```

### Step 6: Update Test Cases (nếu có issues)
```
@updateTC.md Update @feature/tai_kham/TC_Tai_Kham.md theo review report
```

### Step 7: Traceability Matrix
```
@traceabilityMatrix.md Tạo ma trận truy xuất cho @feature/tai_kham/SRS_Tai_Kham.md và @feature/tai_kham/TC_Tai_Kham.md
```

### Quality Gate với Party Mode (cho TC critical)
```
/bmad_party-mode Mời /analyst, /dev, /tea review TC cho feature SOS (Y tế critical)
```

---

## 📊 Bảng Tổng hợp FINAL

| Step | Công cụ | Output | Khi nào | Review bằng |
|------|---------|--------|---------|-------------|
| 0 | `@impactAnalysis.md` | Impact Report | SRS UPDATE | `/analyst` |
| 1 | `@reviewSRS.md` | SRS Review + Score | Luôn luôn | `/analyst` |
| 2 | `/tea` → `TD` | Test Strategy | Optional | `/analyst` + `/pm` |
| 3A | `@generateTestData.md` | TD_Feature.md | Score ≥ 8 | - |
| 3B | Skip | - | Score < 8 | - |
| 4 | `@createTC.md` | TC_Feature.md | Luôn luôn | - |
| 5 | `@reviewTC.md` | Review Report | Luôn luôn | `/analyst` + `/dev` |
| 6 | `@updateTC.md` | TC updated | Nếu có issues | - |
| 7 | `@traceabilityMatrix.md` | Coverage Report | Luôn luôn | `/analyst` |

---

## ⚡ Quick Reference

```bash
# ===== SKILLS =====
@impactAnalysis.md @SRS_v2.md         # Impact Analysis (SRS update)
@reviewSRS.md @SRS.md                 # Review SRS + Data Complexity
@generateTestData.md @SRS.md          # Tạo Test Data (nếu cần)
@createTC.md @SRS.md                  # Tạo Test Cases
@reviewTC.md @TC.md @SRS.md           # Review Test Cases
@updateTC.md @TC.md                   # Update Test Cases
@traceabilityMatrix.md @SRS @TC       # Traceability Matrix

# ===== AGENTS + COMMANDS =====
/tea → TD                             # Test Design (strategy)
/tea → RV                             # Review Tests (best practices)
/analyst                              # Review requirements
/dev                                  # Review technical
/bmad_party-mode                      # Multi-agent discussion
```

---

## 🎯 Quy tắc vàng

1. **SRS update** → Chạy Step 0 (@impactAnalysis) trước
2. **Luôn chạy Task 7** trong reviewSRS để biết cần Test Data riêng không
3. **Score ≥ 8** → Tạo TD file trước, rồi mới tạo TC
4. **Quality Gate** là bắt buộc, ít nhất mời `/analyst`
5. **Coverage ≥ 95%** mới được Ready for Testing

---

## 💡 Tips

- Luôn **tag đúng file path** với `@` để AI đọc đúng file
- Ghi rõ **output mong muốn** (tên file, vị trí lưu)
- Với feature critical (Y tế, SOS): Dùng `/bmad_party-mode` thay vì review từng agent
- **SRS có version mới?** → @impactAnalysis trước để biết scope update
