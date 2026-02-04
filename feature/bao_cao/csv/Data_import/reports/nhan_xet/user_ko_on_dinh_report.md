# 📊 Báo Cáo Nhận Xét Huyết Áp - user_ko_on_dinh (Không ổn định)

> **User ID:** `00000003-0000-0000-0000-000000000003`  
> **Tình trạng HA:** Huyết áp không ổn định  
> **Đặc điểm:** ARV cao, ME diff cực đoan (tăng áp về tối)  
> **Khoảng thời gian:** 01/12/2025 - 31/01/2026

---

## 📈 Tổng Quan Dữ Liệu

| Chỉ số | Tháng 12/2025 | Tháng 01/2026 | Xu hướng |
|:---|:---:|:---:|:---:|
| **Tổng lần đo** | 40 | 61 | ↑ |
| **Ngày có đo** | 18 | 27 | ↑ |
| **SYS trung bình** | 146.6 mmHg | 149.7 mmHg | ↑ Tăng |
| **SYS max / min** | 170 / 108 | 182 / 105 | ↑↓ Biên rộng |

---

## ⚠️ Nhận Xét Về Nguy Cơ Tăng Huyết Áp - BP Load (BR-006)

### Tháng 12/2025

**Công thức:** `bp_load = 27/40 × 100% = 67.5%`

| Phân loại | Ngưỡng | Kết quả |
|:---|:---|:---:|
| ❌ **Gánh nặng lớn** | >30% | **67.5%** |

### Tháng 01/2026

**Công thức:** `bp_load = 43/61 × 100% = 70.5%`

| Phân loại | Ngưỡng | Kết quả |
|:---|:---|:---:|
| ❌ **Gánh nặng lớn** | >30% | **70.5%** |

**Nhận xét AI:**
> "⚠️ **Cảnh báo nghiêm trọng:** BP Load của bạn ở mức rất cao (67-70%), gấp đôi ngưỡng nguy hiểm. Điều này cho thấy hệ tim mạch đang chịu áp lực quá tải liên tục. Bạn **cần gặp bác sĩ ngay** để được can thiệp y tế."

---

## 📊 Nhận Xét Sự Ổn Định Huyết Áp (ARV) - **VẤN ĐỀ CHÍNH**

**Công thức:** `ARV = (1/(n-1)) × Σ|BPₖ₊₁ - BPₖ|`

| Tuần | ARV | Phân loại | Nhận xét |
|:---|:---:|:---|:---|
| T1 (01-07/12) | 34.2 | ❌ **Bất ổn nghiêm trọng** | Dao động cực lớn |
| T2 (08-14/12) | 33.6 | ❌ **Bất ổn nghiêm trọng** | Nguy cơ cao tổn thương mạch |
| T3 (15-21/12) | 5.0 | ✅ Ổn định | Ít dữ liệu (chỉ 2 lần đo) |
| T4 (22-28/12) | 15.7 | ❌ **Bất ổn** | Dao động lớn |
| T6 (05-11/01) | 29.4 | ❌ **Bất ổn nghiêm trọng** | Nguy cơ rất cao |
| T7 (12-18/01) | 30.3 | ❌ **Bất ổn nghiêm trọng** | Hệ mạch chịu áp lực lớn |
| T8 (19-25/01) | 36.0 | ❌ **Bất ổn nghiêm trọng** | ARV cực cao |
| T9 (26-31/01) | 38.7 | ❌ **Bất ổn nghiêm trọng** | Nguy hiểm nhất |

**Nhận xét AI:**
> "🚨 **CẢNH BÁO KHẨN:** ARV của bạn liên tục ở mức **bất ổn nghiêm trọng** (30-38), gấp 3 lần ngưỡng an toàn (<10). Huyết áp dao động từ 105 đến 182 mmHg trong cùng một tuần. Điều này gây nguy cơ rất cao về:
> - Tổn thương thành mạch
> - Nguy cơ đột quỵ
> - Tổn thương cơ quan đích (tim, thận, não)
>
> **Bạn cần được theo dõi y tế chặt chẽ!**"

---

## 🌅 Nhận Xét Nhịp Sinh Học (ME Difference) - **VẤN ĐỀ NGHIÊM TRỌNG**

**Công thức:** `MEdiff = SYS_sáng_TB - SYS_tối_TB`

| Tuần | ME diff | Phân loại | Ý nghĩa |
|:---|:---:|:---|:---|
| T1 | +37 | ⚠️ **Vọt áp sáng** | Tăng nguy cơ đột quỵ sáng sớm |
| T2 | -53 | ❌ **Tăng áp về tối** | Non-dipper nghiêm trọng |
| T4 | +23 | ⚠️ **Vọt áp sáng** | Áp lực máu tăng quá mức khi thức dậy |
| T6 | -62 | ❌ **Tăng áp về tối** | Non-dipper cực kỳ nghiêm trọng |
| T7 | -36 | ❌ **Tăng áp về tối** | Rất hại cho tim và thận |
| T8 | -47 | ❌ **Tăng áp về tối** | Non-dipper nghiêm trọng |
| T9 | -55 | ❌ **Tăng áp về tối** | Non-dipper cực kỳ nghiêm trọng |

**Nhận xét AI:**
> "🚨 **CẢNH BÁO:** Pattern nhịp sinh học của bạn là **Non-dipper nghiêm trọng** - huyết áp không giảm vào ban đêm mà còn tăng cao. ME diff từ -36 đến -62 mmHg là cực kỳ bất thường. Tình trạng này:
> - Gây tổn thương tim và thận liên tục
> - Tăng nguy cơ suy tim
> - Tăng nguy cơ bệnh thận mãn tính
>
> **Cần điều trị đặc biệt với thuốc hạ áp buổi tối!**"

---

## 📋 Tỷ Lệ Tuân Thủ Đo

| Tháng | Lần đo | Ngày có đo/Tổng ngày | Đánh giá |
|:---|:---:|:---:|:---|
| 12/2025 | 40 | 18/31 (58%) | ❌ Tuân thủ kém |
| 01/2026 | 61 | 27/31 (87%) | ✅ Cải thiện tốt |

---

## 💡 Khuyến Nghị Hành Động KHẨN

1. **🏥 Gặp bác sĩ TIM MẠCH ngay** - Tình trạng cần can thiệp y tế
2. **💊 Điều chỉnh thuốc** - Có thể cần thêm thuốc hạ áp buổi tối
3. **📊 Theo dõi 24h** - Cần đo huyết áp liên tục 24h (ABPM)
4. **🩺 Kiểm tra thận, tim** - Đánh giá tổn thương cơ quan đích
5. **😴 Cải thiện giấc ngủ** - Kiểm tra ngưng thở khi ngủ (OSA)

---

*⚠️ Lưu ý: Đây là báo cáo tự động. Với các chỉ số bất thường như trên, bạn CẦN được bác sĩ thăm khám và tư vấn trực tiếp.*
