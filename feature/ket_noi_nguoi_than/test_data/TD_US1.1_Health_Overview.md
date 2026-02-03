# 🧪 Test Data Design: US 1.1 - Xem Tổng quan Sức khỏe

**Feature:** Kết nối Người thân - US 1.1  
**SRS Version:** v2.9  
**TEA Analyst:** Murat | **Date:** 03/02/2026  
**Review Status:** ✅ Updated after BA + PM Review

---

## 📊 1. DATA COMPLEXITY ANALYSIS

| Factor | Weight | Score | Rationale |
|--------|--------|:-----:|-----------|
| Permissions (6 categories) | High | 3 | Permission #1 ON/OFF drives visibility |
| BP Data patterns | High | 4 | Empty/Sparse/Full for Week/Month |
| Connection states | Medium | 2 | Connected, Pending, Disconnected |
| Report states | Medium | 2 | Read/Unread, Empty, Multiple types |
| Time-based logic | High | 3 | Auto-select Week→Month fallback |
| Edge cases | Medium | 3 | Multi-reading/day, Boundary dates |

**Total Score: 17** → ✅ Requires Structured TD File

---

## 🎭 2. TEST DATA PERSONAS

### 2.1 Patient Personas (được theo dõi)

| ID | Persona | Danh xưng | BP Week | BP Month | Reports | Priority | Use Cases |
|----|---------|-----------|:-------:|:--------:|:-------:|:--------:|-----------|
| **P01** | Đầy đủ dữ liệu | Mẹ | ✅ 7d | ✅ 30d | 5 | **P0** | Happy path, Charts |
| **P02** | Chỉ có data Tháng | Bố | ❌ | ✅ 15d | 3 | **P0** | Auto-fallback Month |
| **P03** | Không có data | Bà ngoại | ❌ | ❌ | 0 | **P0** | Empty states |
| **P04** | Nhiều lần đo/ngày | Ông nội | ✅ 5d | ✅ 20d | 2 | **P1** | Average calculation |
| **P05** | User mới (3 ngày) | Cô | ✅ 3d | ✅ 3d | 0 | **P1** | New user empty report |
| **P06** | Báo cáo chưa đọc | Chú | ✅ 7d | ✅ 28d | 10 | **P1** | Unread badge, list |
| **P07** | Week Boundary | Dì | ✅ 2d | ✅ 3d | 1 | **P2** | Week boundary edge case |

### 2.2 Caregiver Personas (người theo dõi)

| ID | Persona | Following | Permission #1 | Priority | Use Cases |
|----|---------|:---------:|:-------------:|:--------:|-----------|
| **C01** | Full access | P01, P02 | ON | **P0** | **Multi-patient switch** |
| **C02** | Limited access | P03 | OFF | **P0** | Permission block hidden |
| **C03** | Single patient | P01 | ON | **P0** | Simple happy path |
| **C04** | New caregiver | P05 | ON | **P1** | New user scenarios |
| **C05** | No selection | P01, P04, P06 | ON | **P1** | Default View State |

### 2.3 Ngưỡng Huyết áp Mục tiêu (từ Profile)

> **Reference:** SRS Thiết lập lịch đo huyết áp

| Patient | Health Status | BP Target Sys | BP Target Dia | Source |
|---------|---------------|:-------------:|:-------------:|--------|
| P01, P02, P05, P06, P07 | THA (chẩn đoán) | 110-129 | 60-79 | VNHA Default |
| P04 | THA (elderly) | 120-140 | 70-90 | Elderly threshold |
| P03 | Bình thường | - | - | Không có target |

---

## 🔄 3. MULTI-PATIENT SWITCHING (NEW - PM Review)

> **User Scenario:** Caregiver C01 theo dõi cả P01 và P02, cần verify switching behavior

### 3.1 Switching Flow Test Data

| Step | Action | Expected | Data Persistence |
|:----:|--------|----------|:----------------:|
| 1 | C01 chọn P01 | Show P01 BP chart (7 days) | - |
| 2 | C01 switch to P02 | Show P02 chart + Auto-fallback Month | ✅ P01 data cached |
| 3 | C01 switch back P01 | Show P01 chart (Week view) | ✅ Restore last view |

### 3.2 State Persistence Verification

```json
{
  "localStorage": {
    "selectedPatient": "P01",
    "lastView": {
      "P01": { "filter": "week", "chip": "all" },
      "P02": { "filter": "month", "chip": "all" }
    }
  }
}
```

---

## 📊 4. BLOOD PRESSURE DATA SETS

### 4.1 P01: Đầy đủ dữ liệu (7 ngày + 30 ngày) - **Priority: P0**

```csv
patient_id,date,time,systolic,diastolic,note
P01,2026-02-03,07:30,125,82,Sáng
P01,2026-02-03,19:00,132,85,Tối
P01,2026-02-02,08:00,128,80,Sáng
P01,2026-02-01,07:45,130,84,
P01,2026-01-31,08:15,127,79,
P01,2026-01-30,07:30,135,88,Sau tập thể dục
P01,2026-01-29,20:00,122,78,
P01,2026-01-28,08:00,126,81,
```

**Expected:**
- Week view: 7 data points
- Tooltip format: `"T2, 03/02: 128/83 mmHg"` (avg 2 readings)
- Chart Y-axis range: 70-140 mmHg

---

### 4.2 P02: Chỉ có Tháng (Auto-fallback test) - **Priority: P0**

```csv
patient_id,date,time,systolic,diastolic,note
P02,2026-01-20,09:00,140,90,
P02,2026-01-15,08:30,138,88,
P02,2026-01-10,07:45,142,92,
P02,2026-01-05,08:00,145,94,Cao
```

**Expected:**
- Week view: **Empty** → Auto-select Month (BR-DB-002)
- Month view: 4 data points
- Toggle default: "Tháng" (fallback)

---

### 4.3 P03: Không có dữ liệu (Empty State) - **Priority: P0**

```csv
patient_id,date,time,systolic,diastolic,note
# No data
```

**Expected:**
- Empty State: "Không có đủ dữ liệu để tạo biểu đồ"
- Both Week/Month empty
- Kolia mascot illustration
- **Danh xưng test:** "[Bà ngoại] chưa có lần đo nào..."

---

### 4.4 P04: Nhiều lần đo/ngày (Average test) - **Priority: P1**

```csv
patient_id,date,time,systolic,diastolic,note
P04,2026-02-03,06:00,130,85,Sáng sớm
P04,2026-02-03,12:00,142,90,Sau ăn trưa
P04,2026-02-03,18:00,128,82,Chiều
P04,2026-02-03,21:00,125,80,Tối
P04,2026-02-02,07:00,132,84,
P04,2026-02-02,19:00,138,88,
```

**Expected (BR-DB-004):**
- 03/02: AVG Sys = (130+142+128+125)/4 = **131 mmHg**
- 03/02: AVG Dia = (85+90+82+80)/4 = **84 mmHg**
- Tap chip 03/02 → Hour view shows 4 points

---

### 4.5 P07: Week Boundary Test - **Priority: P2**

> **PM Note:** Technical edge case, not common user scenario

```csv
patient_id,date,time,systolic,diastolic,note
P07,2026-01-28,08:00,128,82,Exactly on 7th day of week
P07,2026-01-27,07:30,130,84,6th day of week
P07,2026-02-01,09:00,126,80,First day of NEW week
```

**Expected:**
- Week 1 (27/01-02/02): 2 readings (28, 27 Jan)
- Week 2 (03/02-09/02): 1 reading (01 Feb)

---

## 📋 5. REPORT DATA SETS

### 5.1 Report Type Clarification

> **BA Confirmed:** Report list hiển thị 3 loại: **Tuần | Tháng** (Ngày chỉ là filter trong danh sách, không phải report type riêng)

| Report Type | In Scope | Notes |
|-------------|:--------:|-------|
| Tuần | ✅ | Auto-generated weekly |
| Tháng | ✅ | Auto-generated monthly |
| Ngày | ⚠️ | **Filter** trong SCR-REPORT-LIST, không phải report type |

### 5.2 P01: Có báo cáo đầy đủ

| report_id | type | period | created_at | read |
|-----------|------|--------|------------|:----:|
| RPT001 | week | 2026-W05 | 2026-02-02 | ✅ |
| RPT002 | week | 2026-W04 | 2026-01-26 | ✅ |
| RPT003 | month | 2026-01 | 2026-02-01 | ❌ |
| RPT004 | week | 2026-W03 | 2026-01-19 | ❌ |
| RPT005 | week | 2026-W02 | 2026-01-12 | ✅ |

**Expected:**
- Dashboard badge: 2 (unread)
- SCR-REPORT-LIST: Unread có ● đỏ

---

### 5.3 P06: Nhiều báo cáo chưa đọc

| report_id | type | read | note |
|-----------|------|:----:|------|
| RPT101-107 | week | ❌ | 7 tuần liên tiếp |
| RPT108-110 | month | ❌ | 3 tháng |

**Expected (BR-RPT-001):**
- Block hiển thị **3 báo cáo chưa đọc mới nhất**
- "Còn 7 báo cáo khác chưa đọc"

---

## 🔐 6. PERMISSION STATES

| Scenario | patient_id | caregiver_id | permission_1 | Expected |
|----------|------------|--------------|:------------:|----------|
| Full access | P01 | C01 | ON | All blocks visible |
| No access | P03 | C02 | OFF | Block hidden |
| Mid-session revoke | P01 | C03 | ON→OFF | 403 + Toast |

---

## 📝 7. DYNAMIC TEXT VERIFICATION

> **Reference:** SRS B4.2.9

| Patient | Danh xưng | Empty State Message |
|---------|-----------|---------------------|
| P03 | Bà ngoại | "[Bà ngoại] chưa có lần đo nào trong khoảng thời gian này." |
| P05 | Cô | "Chưa có báo cáo nào. Báo cáo sẽ được tạo tự động..." |

---

## 🗂️ 8. FILES GENERATED

| File | Format | Records | Path |
|------|--------|:-------:|------|
| Patients | CSV | 7 | `test_data/patients.csv` |
| Caregivers | CSV | 5 | `test_data/caregivers.csv` |
| Connections | CSV | 9 | `test_data/connections.csv` |
| BP Readings | CSV | 40 | `test_data/blood_pressure.csv` |
| Reports | CSV | 18 | `test_data/reports.csv` |

---

## ✅ 9. COVERAGE MATRIX

| Scenario | Data Set | Priority | Covered |
|----------|----------|:--------:|:-------:|
| B4.2.1 Happy path | P01 + C01 | P0 | ✅ |
| B4.2.2 Detail day | P01 | P0 | ✅ |
| B4.2.4 Toggle filter | P01, P02 | P0 | ✅ |
| B4.2.5 Auto-fallback | P02 | P0 | ✅ |
| B4.2.6 Tooltip | P01, P04 | P1 | ✅ |
| B4.2.7 Report list | P01, P06 | P1 | ✅ |
| B4.2.9 Empty HA | P03 | P0 | ✅ |
| B4.2.10 Empty report | P05 | P1 | ✅ |
| B4.2.11 Permission OFF | P03 + C02 | P0 | ✅ |
| BR-DB-004 Average | P04 | P1 | ✅ |
| Week Boundary | P07 | P2 | ✅ |
| Dynamic Danh xưng | P03, P05 | P1 | ✅ |
| Default View State | C05 | P1 | ✅ |
| **Multi-patient Switch** | C01 + P01/P02 | **P0** | ✅ |

**Coverage: 100%** 🎯

---

## 📌 REVIEW STATUS

| Reviewer | Issues | Status |
|----------|--------|:------:|
| BA (Mary) | Ngưỡng mục tiêu, Danh xưng, Boundary | ✅ Fixed |
| PM (John) | Multi-patient switch, Priority labels, Report Ngày | ✅ Fixed |

---

## 🏷️ PRIORITY LEGEND

| Priority | Definition | Test Coverage |
|:--------:|------------|:-------------:|
| **P0** | Critical - Must test before release | 7 scenarios |
| **P1** | Important - Should test | 5 scenarios |
| **P2** | Nice-to-have - Edge cases | 1 scenario |
