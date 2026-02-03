## 📊 KẾT QUẢ TÍNH TOÁN CHI TIẾT - USER11

### 1️⃣ DỮ LIỆU ĐẦU VÀO

**User Info:**
- Họ tên: **Dương Văn Ít_Đo**
- Giới tính: male
- Ngày sinh: 1973-12-05
- `has_hypertension = 1` → **THA đã chẩn đoán**

**Ngưỡng mục tiêu:**
- SYS: 120 ≤ systolic ≤ 130
- DIA: 70 ≤ diastolic ≤ 80

**Dữ liệu đo:** 7 lần

---

### 2️⃣ BẢNG DỮ LIỆU ĐO

| # | Ngày giờ | SYS | DIA | HR | Ghi chú |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | 19/01 08:00 | 128 | 80 | 72 | U11 chỉ 1 lần/ngày |
| 2 | 20/01 09:00 | 130 | 82 | 74 | U11 chỉ 1 lần/ngày |
| 3 | 21/01 07:30 | 126 | 78 | 70 | U11 chỉ 1 lần/ngày |
| 4 | 22/01 08:30 | 132 | 84 | 76 | U11 chỉ 1 lần/ngày |
| 5 | 23/01 09:00 | 128 | 80 | 72 | U11 chỉ 1 lần/ngày |
| 6 | 24/01 08:00 | 125 | 77 | 69 | U11 chỉ 1 lần/ngày |
| 7 | 25/01 07:00 | 130 | 82 | 74 | U11 chỉ 1 lần/ngày |

---

### 3️⃣ TÍNH TOÁN TỪNG CHỈ SỐ

#### **A. kiem_soat (% trong ngưỡng mục tiêu)**

```
Công thức: kiem_soat = (Số lần đo trong ngưỡng / Tổng số lần đo) × 100%
Điều kiện: 120 ≤ SYS ≤ 130 VÀ 70 ≤ DIA ≤ 80
```

| # | SYS | DIA | SYS OK? | DIA OK? | Kết quả |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 128 | 80 | ✅ | ✅ | ✅ |
| 2 | 130 | 82 | ✅ | ❌ | ❌ |
| 3 | 126 | 78 | ✅ | ✅ | ✅ |
| 4 | 132 | 84 | ❌ | ❌ | ❌ |
| 5 | 128 | 80 | ✅ | ✅ | ✅ |
| 6 | 125 | 77 | ✅ | ✅ | ✅ |
| 7 | 130 | 82 | ✅ | ❌ | ❌ |

**Tính toán:**
```
Trong ngưỡng: 4 lần
Tổng: 7 lần
kiem_soat = 4/7 × 100% = 57.1%
```

**Phân loại:** Kiểm soát tốt

---

#### **B. ARV (Average Real Variability)**

```
Công thức: ARV = Σ|ΔSYSᵢ| / (n-1)
Trong đó: ΔSYSᵢ = SYSᵢ₊₁ - SYSᵢ
```

| Cặp | SYS₁ → SYS₂ | |ΔSYS| |
|:---:|:---|:---:|
| 1-2 | 128 → 130 | 2 |
| 2-3 | 130 → 126 | 4 |
| 3-4 | 126 → 132 | 6 |
| 4-5 | 132 → 128 | 4 |
| 5-6 | 128 → 125 | 3 |
| 6-7 | 125 → 130 | 5 |

**Tính toán:**
```
Σ|ΔSYS| = 24
n-1 = 6
ARV = 24/6 = 4.0
```

**Phân loại:** Ổn định

---

#### **C. ME diff (Morning-Evening Difference)**

```
Công thức: ME diff = TB_sáng - TB_tối
Sáng: 4h-10h | Tối: 20h-23h
```

⚠️ Không đủ dữ liệu sáng/tối để tính MEdiff