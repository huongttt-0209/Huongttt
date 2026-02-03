---
description: Workflow hoàn chỉnh cho Tester kết hợp Manual Skills + TEA Automation (v6.1)
---

# 🧪 Tester Workflow V6.1 - Manual + TEA Integration

> **V6.1 Updates:** Thêm Step 0: Impact Analysis cho SRS update

## 🎯 OVERVIEW

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         TESTER WORKFLOW V6.1                                 │
│                    Manual Skills + TEA Integration                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   📥 INPUT: SRS từ BA                                                        │
│        │                                                                     │
│        ▼                                                                     │
│   ╔═══════════════════════════════════════════════════════════════════════╗  │
│   ║ SRS mới hay SRS update?                                               ║  │
│   ╠═══════════════════════════════════════════════════════════════════════╣  │
│   ║   NEW SRS                              UPDATE SRS                     ║  │
│   ║      │                                      │                          ║  │
│   ║      │                                      ▼                          ║  │
│   ║      │                   ┌──────────────────────────────────────────┐  ║  │
│   ║      │                   │ STEP 0: @impactAnalysis.md  ⭐ NEW       │  ║  │
│   ║      │                   │ ├─ Xác định features bị ảnh hưởng        │  ║  │
│   ║      │                   │ ├─ TCs cần update                        │  ║  │
│   ║      │                   │ └─ Regression scope                      │  ║  │
│   ║      │                   └──────────────────────────────────────────┘  ║  │
│   ║      │                                      │                          ║  │
│   ║      └──────────────────────┬───────────────┘                          ║  │
│   ╚═════════════════════════════╧══════════════════════════════════════════╝  │
│                                 │                                            │
│                                 ▼                                            │
│   ╔═══════════════════════════════════════════════════════════════════════╗  │
│   ║ PHASE 1: ANALYSIS & PLANNING                                          ║  │
│   ╠═══════════════════════════════════════════════════════════════════════╣  │
│   ║ Step 1: @reviewSRS.md → SRS Review + Data Complexity Score            ║  │
│   ║ Step 2: /tea → TD (Optional) → Test Strategy (cho features lớn)       ║  │
│   ╚═══════════════════════════════════════════════════════════════════════╝  │
│        │                                                                     │
│        ▼                                                                     │
│   ╔═══════════════════════════════════════════════════════════════════════╗  │
│   ║ PHASE 2: TEST DESIGN                                                  ║  │
│   ╠═══════════════════════════════════════════════════════════════════════╣  │
│   ║ Step 3: @generateTestData.md → TD_Feature.md (nếu Score ≥ 8)          ║  │
│   ║ Step 4: @createTC.md → TC_Feature.md (Manual Test Cases)              ║  │
│   ╚═══════════════════════════════════════════════════════════════════════╝  │
│        │                                                                     │
│        ▼                                                                     │
│   ╔═══════════════════════════════════════════════════════════════════════╗  │
│   ║ PHASE 3: QUALITY GATE                                                 ║  │
│   ╠═══════════════════════════════════════════════════════════════════════╣  │
│   ║ Step 5: @reviewTC.md → Self Review                                    ║  │
│   ║ Step 6: /analyst + /dev → Multi-agent Review                          ║  │
│   ║ Step 7: /tea → RV (Optional) → Best Practices Review                  ║  │
│   ║ Step 8: @updateTC.md → Fix Issues                                     ║  │
│   ╚═══════════════════════════════════════════════════════════════════════╝  │
│        │                                                                     │
│        ▼                                                                     │
│   ╔═══════════════════════════════════════════════════════════════════════╗  │
│   ║ PHASE 4: TRACEABILITY & COVERAGE                                      ║  │
│   ╠═══════════════════════════════════════════════════════════════════════╣  │
│   ║ Step 9: @traceabilityMatrix.md → Coverage Report                      ║  │
│   ║     HOẶC /tea → TR → TEA Trace Requirements                           ║  │
│   ╚═══════════════════════════════════════════════════════════════════════╝  │
│        │                                                                     │
│        ▼ Coverage ≥ 95%?                                                     │
│                                                                              │
│   ╔═══════════════════════════════════════════════════════════════════════╗  │
│   ║ PHASE 5: AUTOMATION (OPTIONAL - Khi cần Auto Test)                    ║  │
│   ╠═══════════════════════════════════════════════════════════════════════╣  │
│   ║ Step A1: /tea → TF → Setup Test Framework (Playwright/Cypress)        ║  │
│   ║ Step A2: /tea → TA → Generate Automation Code                         ║  │
│   ║ Step A3: /tea → CI → CI/CD Pipeline Integration                       ║  │
│   ╚═══════════════════════════════════════════════════════════════════════╝  │
│        │                                                                     │
│        ▼                                                                     │
│                     ✅ READY FOR TESTING                                     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📋 STEP 0: IMPACT ANALYSIS (Cho SRS UPDATE)

> ⚠️ **Chỉ dùng khi SRS có version update**

```
@impactAnalysis.md Phân tích impact của @feature/xxx/SRS_v2.md so với v1
```

**Output:**
- Features bị ảnh hưởng (Direct/Indirect)
- TCs cần update
- Regression scope recommendation

---

## 📋 PHASE 1: ANALYSIS & PLANNING

### Step 1: Review SRS (BẮT BUỘC)
```
@reviewSRS.md Review SRS cho feature @feature/xxx/SRS.md
```
**Output:** SRS Review Report + Data Complexity Score

### Step 2: Test Design Strategy (TÙY CHỌN - cho features lớn)
```
/tea
→ Chọn [TD] Test Design
→ Input: SRS file
```
**Output:** Risk-based Test Strategy

---

## 📋 PHASE 2: TEST DESIGN

### Step 3: Generate Test Data (nếu Score ≥ 8)
```
@generateTestData.md Tạo test data cho @SRS.md. Lưu TD_Feature.md
```
**Output:** TD_Feature.md

### Step 4: Create Test Cases (BẮT BUỘC)
```
@createTC.md Tạo TC cho @SRS.md với data @TD_Feature.md
```
**Output:** TC_Feature.md

---

## 📋 PHASE 3: QUALITY GATE

### Step 5: Self Review (BẮT BUỘC)
```
@reviewTC.md Review @TC_Feature.md dựa trên @SRS.md
```

### Step 6: Multi-Agent Review (BẮT BUỘC)
```
/analyst Review TC_Feature.md về requirements coverage
/dev Review TC_Feature.md về technical feasibility (TÙY CHỌN)
```

### Step 7: TEA Best Practices Review (TÙY CHỌN)
```
/tea
→ Chọn [RV] Review Tests
→ Input: TC file
```

### Step 8: Update Test Cases (nếu có issues)
```
@updateTC.md Update @TC_Feature.md theo review report
```

---

## 📋 PHASE 4: TRACEABILITY & COVERAGE

### Step 9: Traceability Matrix (BẮT BUỘC)

**Cách 1: Dùng Skill (Tiếng Việt)**
```
@traceabilityMatrix.md Tạo TM cho @SRS.md và @TC_Feature.md
```

**Cách 2: Dùng TEA (English, Advanced)**
```
/tea
→ Chọn [TR] Trace Requirements
→ Input: SRS + TC files
```

**Output:** Coverage Report (phải ≥ 95%)

---

## 📋 PHASE 5: AUTOMATION (OPTIONAL)

> ⚠️ **Chỉ dùng khi cần Test Automation**

### Step A1: Setup Test Framework
```
/tea
→ Chọn [TF] Test Framework
→ Chọn Playwright hoặc Cypress
```
**Output:** Test framework cấu trúc hoàn chỉnh

### Step A2: Generate Automation Code
```
/tea
→ Chọn [TA] Test Automation
→ Input: TC file
```
**Output:** Automation test code (Playwright/Cypress)

### Step A3: CI/CD Integration
```
/tea
→ Chọn [CI] Continuous Integration
→ Input: test folder
```
**Output:** CI/CD pipeline config

---

## 📊 BẢNG TỔNG HỢP V6.1

| Phase | Step | Tool | Output | Khi nào | Loại |
|-------|------|------|--------|---------|------|
| **0** | 0 | `@impactAnalysis.md` | Impact Report | SRS UPDATE | Manual |
| **1** | 1 | `@reviewSRS.md` | SRS Review + Score | Luôn luôn | Manual |
| **1** | 2 | `/tea → TD` | Test Strategy | Optional | TEA |
| **2** | 3 | `@generateTestData.md` | TD_Feature.md | Score ≥ 8 | Manual |
| **2** | 4 | `@createTC.md` | TC_Feature.md | Luôn luôn | Manual |
| **3** | 5 | `@reviewTC.md` | Review Report | Luôn luôn | Manual |
| **3** | 6 | `/analyst` + `/dev` | Multi-agent Review | Luôn luôn | Agent |
| **3** | 7 | `/tea → RV` | Best Practices Review | Optional | TEA |
| **3** | 8 | `@updateTC.md` | TC Updated | Nếu có issues | Manual |
| **4** | 9 | `@traceabilityMatrix.md` / `/tea → TR` | Coverage Report | Luôn luôn | Manual/TEA |
| **5** | A1 | `/tea → TF` | Test Framework | Cần auto | TEA |
| **5** | A2 | `/tea → TA` | Automation Code | Cần auto | TEA |
| **5** | A3 | `/tea → CI` | CI/CD Pipeline | Cần auto | TEA |

---

## ⚡ QUICK REFERENCE

### Manual Skills (Tiếng Việt)
```bash
@impactAnalysis.md @SRS_v2.md         # Impact Analysis (SRS update)
@reviewSRS.md @SRS.md                 # Review SRS
@generateTestData.md @SRS.md          # Tạo Test Data
@createTC.md @SRS.md @TD.md           # Tạo Test Cases
@reviewTC.md @TC.md @SRS.md           # Review Test Cases
@updateTC.md @TC.md                   # Update Test Cases
@traceabilityMatrix.md @SRS @TC       # Traceability Matrix
```

### TEA Workflows (English)
```bash
/tea → TD    # Test Design (strategy + risk assessment)
/tea → RV    # Review Tests (best practices)
/tea → TR    # Trace Requirements (coverage matrix)
/tea → TF    # Test Framework (setup Playwright/Cypress)
/tea → TA    # Test Automation (generate code)
/tea → CI    # CI/CD Integration
/tea → AT    # ATDD (acceptance tests first)
/tea → NR    # NFR Assessment
/tea → TMT   # Teach Me Testing (learning)
```

### Multi-Agent
```bash
/analyst            # Requirements expert
/dev                # Technical expert
/tea                # Testing expert
/party-mode         # All agents together
```

---

## 🎯 KHI NÀO DÙNG GÌ?

| Scenario | Dùng |
|----------|------|
| **SRS update** | `@impactAnalysis.md` → rồi tiếp Phase 1 |
| Review SRS hàng ngày | `@reviewSRS.md` |
| Tạo Manual TC (Tiếng Việt) | `@createTC.md` |
| Cần Test Strategy (feature lớn) | `/tea → TD` |
| Review TC theo best practices | `/tea → RV` |
| Cần automation code | `/tea → TA` |
| Setup test framework | `/tea → TF` |
| CI/CD integration | `/tea → CI` |
| Học testing | `/tea → TMT` |

---

## 💡 TIPS

1. **SRS update** → Chạy Step 0 (@impactAnalysis) TRƯỚC
2. **Luôn bắt đầu** với `@reviewSRS.md` để đánh giá complexity
3. **Score ≥ 8** → Tạo Test Data file riêng
4. **Quality Gate** → Ít nhất mời `/analyst`
5. **Coverage ≥ 95%** mới Ready for Testing
6. **Cần automation** → Phase 5 với TEA
7. **Feature critical** → Dùng `/party-mode`
