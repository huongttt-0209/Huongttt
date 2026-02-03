# **PHẦN 1: USER STORY**

**1.1 Epic Information**

Epic ID: EPIC-002  
Epic Title: Báo cáo và Phân tích Sức khỏe  
Epic Description: Cung cấp cho người dùng công cụ theo dõi sức khỏe trực quan, kết hợp giữa bảng điều khiển hoạt động hàng ngày và các báo cáo phân tích xu hướng dài hạn theo tuần/tháng, giúp người dùng nắm bắt tình hình, duy trì động lực và dễ dàng chia sẻ dữ liệu với chuyên gia y tế.  
**1.2 User Story**

**As a** người dùng quan tâm đến sức khoẻ hàng ngày  
**I want to** xem một bảng điều khiển tổng quan các chỉ số và nhiệm vụ trong ngày  
**So that** tôi có thể nhanh chóng nắm bắt tình hình sức khoẻ hiện tại và biết cần phải làm gì tiếp theo.  
**Story ID:** US-001  
**Story Points:** TBD  
**Priority**: High  
**Sprint**: Sprint 5

**As a** người dùng muốn theo dõi và phân tích tiến trình hàng tuần  
**I want to** xem danh sách các báo cáo tuần và có thể chọn để xem chi tiết từng báo cáo  
**So that** tôi có thể vừa so sánh các tuần với nhau, vừa phân tích sâu các biến động sức khoẻ khi cần.  
**Story ID**: US-002  
**Story Points**: TBD  
**Priority**: High  
**Sprint**: Sprint 5

**As a** người dùng muốn đánh giá xu hướng sức khoẻ dài hạn  
**I want to** xem danh sách các báo cáo tháng và có thể chọn để xem chi tiết từng báo cáo  
**So that** tôi có thể có cái nhìn tổng thể về sự cải thiện sức khoẻ của mình qua các tháng.  
**Story ID:** US-003  
**Story Points:** TBD  
**Priority**: Medium  
**Sprint**: Sprint 5

# **PHẦN 2: ACCEPTANCE CRITERIA**

## **US-001: Xem Tiêu điểm ngày**

*2.1 Happy Path Scenarios*

Scenario 1: (US-001) Người dùng xem màn hình Tiêu điểm ngày với đầy đủ dữ liệu  
Given người dùng đã đăng nhập và có ít nhất một chỉ số huyết áp và một nhiệm vụ trong ngày.  
When người dùng nhấn vào tab "Báo cáo" trên thanh điều hướng chính.  
Then hệ thống hiển thị màn hình "Báo cáo sức khỏe" với tab "Tiêu điểm ngày" được chọn mặc định.  
And một banner chào hỏi được hiển thị ở đầu trang phù hợp với thời gian trong ngày.  
And mục "Góc sức khỏe hôm nay" hiển thị đúng thời gian và chỉ số Tâm thu/Tâm trương của lần đo gần nhất, kèm theo nhận xét tương ứng.  
And mục "Nhiệm vụ trong ngày" hiển thị đúng tiến độ hoàn thành (ví dụ: "2/3 nhiệm vụ").  
And một thông điệp động viên được hiển thị dựa trên tiến độ hoàn thành nhiệm vụ.  
Business Rule Reference: BR-003, BR-004

Scenario 2: (US-001) Người dùng mở rộng và thu gọn danh sách nhiệm vụ  
Given người dùng đang ở màn hình "Tiêu điểm ngày".  
When người dùng nhấn vào "Xem chi tiết nhiệm vụ".  
Then danh sách nhiệm vụ được mở rộng, hiển thị tên từng nhiệm vụ và trạng thái (đã hoàn thành có dấu tick, chưa hoàn thành có nút "Thực hiện").  
And nút "Xem chi tiết nhiệm vụ" chuyển thành "Ẩn chi tiết nhiệm vụ".  
When người dùng nhấn vào "Ẩn chi tiết nhiệm vụ".  
Then danh sách nhiệm vụ được thu gọn lại.  
And nút "Ẩn chi tiết nhiệm vụ" chuyển về "Xem chi tiết nhiệm vụ".

Scenario 3: (US-001) Người dùng điều hướng để thực hiện một nhiệm vụ  
Given người dùng đang xem danh sách nhiệm vụ mở rộng.  
When người dùng nhấn vào nút "Thực hiện" của một nhiệm vụ chưa hoàn thành.  
Then hệ thống điều hướng người dùng đến màn hình chức năng tương ứng của nhiệm vụ đó.  
Business Rule Reference: BR-008

*2.2 Edge Cases & Error Scenarios*

Scenario 1: (US-001) Người dùng xem Tiêu điểm ngày khi chưa có dữ liệu huyết áp  
Given người dùng đã đăng nhập nhưng chưa đo huyết áp lần nào trong ngày.  
When người dùng vào màn hình "Tiêu điểm ngày".  
Then phần "Góc sức khỏe hôm nay" hiển thị theo quy tắc cho trường hợp không có dữ liệu.  
Business Rule Reference: BR-006

## **US-002: Xem báo cáo tuần**

*2.1 Happy Path Scenarios*

Scenario 1: (US-002) Người dùng xem danh sách báo cáo tuần  
Given người dùng đã có ít nhất một báo cáo tuần được tạo.  
When người dùng vào màn hình "Báo cáo" và chọn tab "Báo cáo định kỳ".  
Then hệ thống hiển thị danh sách các báo cáo tuần, mỗi item hiển thị tiêu đề "Báo cáo tuần" và ngày/giờ tạo báo cáo.  
And bộ lọc "Danh sách theo tuần" được chọn mặc định.

Scenario 2: (US-002) Người dùng xem chi tiết một báo cáo tuần  
Given người dùng đang ở màn hình danh sách báo cáo định kỳ.  
When người dùng nhấn vào một báo cáo tuần cụ thể.  
Then hệ thống điều hướng đến màn hình chi tiết của báo cáo tuần đó, hiển thị đầy đủ các phần phân tích.  
And ở cuối chi tiết báo cáo có các nút "Tư vấn thêm" và "Chia sẻ báo cáo".  
Business Rule Reference: BR-005

Scenario 3: (US-002) Người dùng chia sẻ một báo cáo tuần  
Given người dùng đang xem chi tiết một báo cáo tuần.  
When người dùng nhấn vào nút "Chia sẻ báo cáo".  
Then hệ thống tạo ra một file PDF chứa nội dung báo cáo.  
And hệ thống mở menu chia sẻ mặc định của hệ điều hành.  
Business Rule Reference: BR-009

**Scenario 4:** Người dùng sử dụng bộ lọc và tương tác biểu đồ.

**Given:** Người dùng đang xem chi tiết báo cáo tuần

**Then:** Hệ thống hiển thị Filter lọc ngày cho biểu đồ huyết áp và nhịp tim.

**And:** Cho phép swipe ngang qua những ngày có kết quả đo theo thứ tự từ cũ đến mới.

**When:** Người dùng nhấn vào một ngày cụ thể trên biểu đồ.

**Then:** Hệ thống hiển thị biểu đồ chi tiết của ngày đó (trục X là giờ).

*2.2 Edge Cases & Error Scenarios*

Scenario 1: (US-002) Người dùng lần đầu sử dụng và chưa có báo cáo tuần nào  
Given người dùng mới sử dụng ứng dụng và chưa có đủ dữ liệu để tạo báo cáo tuần.  
When người dùng vào tab "Báo cáo định kỳ".  
Then màn hình hiển thị giao diện trạng thái trống, thông báo rằng chưa có dữ liệu báo cáo.

Scenario 2: (US-002) Báo cáo tuần không có dữ liệu cho một hoặc nhiều phần  
Given người dùng đang xem chi tiết một báo cáo tuần.  
And trong tuần đó, có ít nhất một phần (ví dụ: Phân tích lối sống) không có dữ liệu để tổng hợp.  
When người dùng cuộn đến phần không có dữ liệu đó.  
Then hệ thống hiển thị giao diện tương ứng cho trường hợp không có dữ liệu như đã định nghĩa.  
And các phần khác có dữ liệu vẫn hiển thị bình thường.  
Business Rule Reference: BR-007  
*2.3 Alternative Path Scenarios*

Scenario 1: (US-002) Người dùng quay lại từ màn hình chi tiết báo cáo tuần  
Given người dùng đang xem màn hình chi tiết báo cáo tuần.  
When người dùng nhấn nút quay lại ("\<") trên header.  
Then hệ thống điều hướng người dùng quay về màn hình danh sách báo cáo.

## **US-003: Xem báo cáo tháng**

***Happy Path Scenarios***

Scenario 1: (US-003) Người dùng chuyển bộ lọc và xem danh sách báo cáo tháng  
Given người dùng đã có ít nhất một báo cáo tháng được tạo.  
When người dùng vào tab "Báo cáo định kỳ" và nhấn vào bộ lọc "Danh sách theo tuần".  
And người dùng chọn "Danh sách theo tháng" từ bottom sheet.  
Then danh sách được cập nhật để hiển thị các báo cáo tháng.

Scenario 2: (US-003) Người dùng xem chi tiết một báo cáo tháng  
Given người dùng đang ở màn hình danh sách báo cáo tháng.  
When người dùng nhấn vào một báo cáo tháng cụ thể.  
Then hệ thống điều hướng đến màn hình chi tiết của báo cáo tháng đó.  
Business Rule Reference: BR-005

Scenario 3: (US-003) Người dùng chia sẻ một báo cáo tháng  
Given người dùng đang xem chi tiết một báo cáo tháng.  
When người dùng nhấn vào nút "Chia sẻ báo cáo".  
Then hệ thống tạo ra một file PDF chứa nội dung báo cáo.  
And hệ thống mở menu chia sẻ mặc định của hệ điều hành.  
Business Rule Reference: BR-009

**Scenario 4:** Người dùng sử dụng bộ lọc và tương tác biểu đồ.

**Given:** Người dùng đang xem chi tiết báo cáo tháng

**Then:** Hệ thống hiển thị Filter lọc ngày cho biểu đồ huyết áp và nhịp tim.

**And:** Cho phép swipe ngang qua những ngày có kết quả đo theo thứ tự từ cũ đến mới.

**When:** Người dùng nhấn vào một ngày cụ thể trên biểu đồ.

**Then:** Hệ thống hiển thị biểu đồ chi tiết của ngày đó (trục X là giờ).

***Edge Cases & Error Scenarios***

Scenario 1: (US-003) Người dùng lần đầu sử dụng và chưa có báo cáo tháng nào  
Given người dùng mới sử dụng ứng dụng và chưa có đủ dữ liệu để tạo báo cáo tháng.  
When người dùng vào tab "Báo cáo định kỳ" và chuyển bộ lọc sang "Danh sách theo tháng".  
Then màn hình hiển thị giao diện trạng thái trống, thông báo rằng chưa có dữ liệu báo cáo.

Scenario 2: (US-003) Báo cáo tháng không có dữ liệu cho một hoặc nhiều phần  
Given người dùng đang xem chi tiết một báo cáo tháng.  
When người dùng cuộn đến phần không có dữ liệu đó.  
Then hệ thống hiển thị giao diện tương ứng cho trường hợp không có dữ liệu như đã định nghĩa.  
Business Rule Reference: BR-007

***Alternative Path Scenarios***

Scenario 1: (US-003) Người dùng hủy thao tác chọn bộ lọc  
Given người dùng đang ở màn hình danh sách báo cáo định kỳ.  
When người dùng nhấn vào bộ lọc để mở bottom sheet tùy chọn (Tuần/Tháng).  
And người dùng nhấn ra ngoài khu vực bottom sheet hoặc nhấn nút đóng.  
Then bottom sheet được đóng lại.  
And danh sách báo cáo không có gì thay đổi.

Scenario 2: (US-003) Người dùng quay lại từ màn hình chi tiết báo cáo tháng  
Given người dùng đang xem màn hình chi tiết báo cáo tháng.  
When người dùng nhấn nút quay lại ("\<") trên header.  
Then hệ thống điều hướng người dùng quay về màn hình danh sách báo cáo.

# **PHẦN 3: BUSINESS RULES**

Rule ID: BR-001 

Rule Name: Quy tắc tạo Báo cáo tuần tự động 

Description: Hệ thống tự động tổng hợp dữ liệu và tạo báo cáo tuần vào lúc 00:00 ngày Thứ Hai của tuần kế tiếp. Báo cáo sau khi được tạo là một bản ghi tĩnh và không thay đổi dữ liệu.

Rule ID: BR-002 

Rule Name: Quy tắc tạo Báo cáo tháng tự động 

Description: Hệ thống tự động tổng hợp dữ liệu và tạo báo cáo tháng vào lúc 00:00 ngày đầu tiên của tháng kế tiếp. Báo cáo sau khi được tạo là một bản ghi tĩnh và không thay đổi dữ liệu.

Rule ID: BR-003 

Rule Name: Quy tắc làm mới dữ liệu Tiêu điểm ngày

Description: Dữ liệu trên tab "Tiêu điểm ngày" phải được tự động làm mới mỗi khi người dùng truy cập vào màn hình, hoặc ngay sau khi người dùng hoàn thành một nhiệm vụ liên quan (ví dụ: đo huyết áp).

Rule ID: BR-004 

Rule Name: Quy tắc Nội dung và Logic hiển thị Tiêu điểm ngày

**Description:** Mô tả logic hiển thị cho từng thành phần trên màn hình "Tiêu điểm ngày".

* **1\. Banner chào hỏi:**  
  * **Logic:** Hiển thị lời chào, mô tả ngắn và hình ảnh minh họa thay đổi linh hoạt theo thời gian thực trong ngày.  
  * **Các mốc thời gian:**  
    * Buổi sáng (04:00 \- 10:59): "Buổi sáng tốt lành"  
    * Buổi trưa (11:00 \- 13:59): "Buổi trưa năng động"  
    * Buổi chiều (14:00 \- 17:59): "Buổi chiều hiệu quả"  
    * Buổi tối (18:00 \- 03:59): "Buổi tối thư giãn"  
* **2\. Góc sức khỏe hôm nay:**  
  * **Logic:** Luôn hiển thị kết quả của lần đo huyết áp gần nhất được ghi nhận trong ngày (từ 00:00 đến thời điểm hiện tại).  
  * **Nội dung:** Thời gian đo, chỉ số Tâm thu/Tâm trương.  
  * **Nhận xét:** AI tạo một nhận xét ngắn gọn, trực tiếp dựa trên việc so sánh chỉ số đo được với ngưỡng huyết áp mục tiêu của người dùng.  
* **3\. Nhiệm vụ trong ngày:**  
  * **Logic tính tiến độ:** Hiển thị dưới dạng "X/Y nhiệm vụ", trong đó X là số nhiệm vụ đã hoàn thành và Y là tổng số nhiệm vụ được giao trong ngày.  
  * **Logic hiển thị danh sách (khi mở rộng):** Liệt kê tất cả nhiệm vụ. Nhiệm vụ đã hoàn thành hiển thị dấu tick màu xanh. Nhiệm vụ chưa hoàn thành có nút "Thực hiện".  
* **4\. Thông điệp động viên:**  
  * **Logic:** Hiển thị một câu động viên được cá nhân hóa, tạo bởi AI dựa trên tiến độ hoàn thành nhiệm vụ trong ngày của người dùng.  
  * **Ví dụ:** "Tuyệt vời\! Bạn đã hoàn thành 2/3 nhiệm vụ. Hãy tiếp tục duy trì thói quen tốt này nhé."

**Rule ID: BR-006** 

**Rule Name: Quy tắc nội dung và Logic phân tích chuyên sâu Báo cáo ngày** 

**Description:** Quy định toàn bộ cấu trúc hiển thị, điều kiện tính toán và các thuật toán phân tích lâm sàng dành riêng cho màn hình Báo cáo ngày (màn hình chi tiết khi người dùng nhấn từ Tiêu điểm ngày hoặc Báo cáo định kỳ).

#### **1\. Logic Hiển thị Biểu đồ huyết áp 24H**

* **Loại biểu đồ:** Biểu đồ đường (Line Chart) thể hiện biến động chỉ số.  
* **Cấu trúc trục:**  
  * **Trục hoành (X):** Hiển thị thời gian theo **Giờ** trong ngày.  
  * **Trục tung (Y):** Hiển thị giá trị chỉ số (Huyết áp: mmHg).

**2\. Logic nhận xét cho biểu đồ**

**\*Điều kiện dữ liệu tối thiểu (Data Sufficiency)**

Hệ thống chỉ thực hiện các phân tích chuyên sâu (từ mục 3 đến mục 6 của Rule này) khi đạt điều kiện:

* **Điều kiện đủ:** Có **\>= 2 lần đo/ngày**.  
* **Xử lý khi không đủ dữ liệu:** Ẩn các nhận xét chuyên sâu. Hiển thị thông điệp: *"Hãy chú ý đo huyết áp thường xuyên (ít nhất 2 lần/ngày) để Kolia có đủ dữ liệu đưa ra phân tích chuyên sâu và tối ưu nhất cho bạn."*  
* **Nhận xét về mức độ kiểm soát huyết áp** *(Lưu ý: chỉ hiển thị cho người có tình trạng HA "Bác sĩ đã chẩn đoán bị bệnh Tăng huyết áp")*  
  **Bước 1**: Tính Phần trăm số lần đo nằm trong khoảng mục tiêu \- tức là cả tâm thu và tâm trương đều nằm trong ngưỡng mục tiêu \= Số lần đo trong ngưỡng mục tiêu/Tổng số lần đo\*100%  
  **Bước 2**: Diễn giải và đánh giá lâm sàng mức độ kiểm soát huyết áp dựa trên phân loại  
  **\> 70% \- Kiểm soát tối ưu:** Huyết áp rất ổn định, đạt trạng thái lý tưởng để ngăn ngừa biến chứng tim mạch.  
  **50% – 70% \- Kiểm soát tốt:** Đạt yêu cầu điều trị. Đa số thời gian cơ thể được bảo vệ trước áp lực máu cao.  
  **25% – 50% \- Kiểm soát kém:** Huyết áp dao động nhiều. Hiệu quả của phác đồ thuốc hiện tại chưa ổn định.  
  **\< 25% \- Không được kiểm soát:** Rất ít khi huyết áp đạt đích. Nguy cơ xảy ra biến cố (đột quỵ, suy tim) ở mức cao.  
* **Nhận xét về nguy cơ tăng huyết áp** *(Lưu ý: chỉ hiển thị cho người có tình trạng HA “Thường đo thấy chỉ số cao, nhưng chưa được chẩn đoán bệnh Tăng huyết áp, “Huyết áp bình thường”, "Huyết áp không ổn định", "Không rõ/ Không theo dõi)*  
  **Bước 1**: Tính toán BP load theo công thức (ngưỡng THA: 140/90)   
  ![][image1]  
  Chỉ cần tâm trương hoặc tâm thu \>140/90 thì lần đo đó được coi là vượt ngưỡng 140/90 mmHG  
  **Bước 2**: **\[Nhận xét tần suất vượt ngưỡng\]** lồng ghép **\[Lý giải áp lực lên thành mạch và nguy cơ quá tải hệ tim mạch\]**.  
  **Dưới 15% \- Bình thường:** Hệ tim mạch đang được bảo vệ tốt.  
  **15% \- 30% \- Chớm cao:** Bắt đầu có dấu hiệu quá tải, cần điều chỉnh lối sống.  
  **Trên 30% \- Gánh nặng lớn lên hệ tim mạch:** Nguy cơ cao gây tổn thương tim, thận. Cần can thiệp y tế.  
* Nhận xét về tần suất huyết áp thấp *(Lưu ý: chỉ hiển thị cho người có tình trạng HA “Huyết áp thấp”)*  
  **Bước** 1: Tính toán Hypotension Load theo công thức:   
  ![][image2]  
  Chỉ cần tâm trương hoặc tâm thu \<90/60 thì lần đo đó được coi là \<90/60 mmHg  
  **Bước** 2: **\[Nhận xét tần suất\]** kết hợp **\[Lý giải nguy cơ thiếu máu/oxy tương ứng\]**.  
  **Mức 1 (Ít khi thấp):** Gánh nặng \< 15%.  
  **Mức 2 (Thường xuyên thấp):** Gánh nặng 15% \- 30%.  
  **Mức 3 (Rủi ro tụt huyết áp):** Gánh nặng \> 30%  
* Nhận xét về sự ổn định của huyết áp   
  **Bước 1**: Tính toán ARV tâm thu theo công thức  
  ![][image3]  
  ![][image4]  
  Khoảng cách tối đa giữa 2 lần đo liên tiếp là 24h, nếu \<24h, bỏ qua cặp giá trị .  
  **Bước 2**: Diễn giải chỉ số và đưa ra nhận xét về độ ổn định của chỉ số HA  
  \< 10 \- Ổn định: Hệ mạch vận hành êm ái, ít áp lực cơ học  
  10 – 14 \- Biến động: Mạch máu bắt đầu chịu áp lực từ sự dao động.  
  \> 14 \- Bất ổn: Nguy cơ cao tổn thương thành mạch và cơ quan đích.  
* **Nhận xét về nhịp sinh học của huyết áp**  
  **Bước** 1: Tính toán chỉ số ME difference (tâm thu)  
  ![][image5]  
  Sáng: 04:00 đến 10h00  
  Tối: 20:00 đến 00h00  
  Cần tối thiểu 1 lần đo trong mỗi khoảng thời gian  
  **Bước** 2: Nhận xét về nhịp sinh học của huyết áp dựa trên cách ngưỡng giá trị

| Chỉ số MEdiff​ | Phân loại nhịp | Ý nghĩa y khoa |
| :---- | :---- | :---- |
| \>15 mmHg | Vọt áp buổi sáng (Morning Surge) | Áp lực máu tăng quá mức khi thức dậy, tăng nguy cơ đột quỵ sáng sớm. |
| −15 đến 15 mmHg | Cân bằng (Balanced) | Nhịp sinh học ổn định, huyết áp sáng và tối không chênh lệch quá mức. |
| \<−15 mmHg | Tăng áp về tối (Risky Evening) | Dấu hiệu của tình trạng "Non-dipper" (không hạ áp về đêm), rất hại cho tim và thận. |

* Nhận xét tương quan giữa huyết áp với kết quả uống thuốc, sự kiện ăn uống\&vận động, các nguyên nhân được ghi nhận cùng kết quả HA (nếu có)

| Loại sự kiện | Khung giờ lấy kết quả đo HA (Sau sự kiện) | Ý nghĩa phân tích tương quan | Giải thích cơ sở khoa học |
| :---- | :---- | :---- | :---- |
| **Uống thuốc HA** | **1 giờ — 8 giờ** | **Đánh giá hiệu quả thuốc** | Đây là thời gian thuốc đạt nồng độ đỉnh trong máu (Tmax), cho thấy khả năng hạ áp tốt nhất của liều thuốc. |
| **Stress / Đau / Cảm xúc** | **0 phút — 45 phút** | **Đánh giá độ nhạy cảm tâm lý** | Phản ứng của hệ thần kinh giao cảm (phóng thích Adrenaline) làm co mạch và tăng HA diễn ra ngay lập tức. |
| **Caffeine / Thuốc lá** | **30 phút — 2 giờ** | **Đánh giá phản ứng kích thích** | Caffeine và Nicotine gây tăng HA nhanh chóng nhưng thời gian bán thải ngắn, tác động rõ nhất trong khoảng này. |
| **Vận động mạnh** | **30 phút — 2 giờ** | **Đánh giá đáp ứng phục hồi** | HA tăng khi tập, nhưng sau 30 phút nghỉ ngơi, một hệ tim mạch tốt sẽ thấy HA giảm nhẹ (hiệu ứng hạ áp sau tập). |
| **Ăn mặn (Nhiều muối)** | **12 giờ — 24 giờ** | **Đánh giá tác động giữ nước** | Muối cần thời gian để thẩm thấu và giữ nước trong hệ tuần hoàn, thường gây tăng HA vào sáng ngày hôm sau. |
| **Rượu / Bia** | **12 giờ — 24 giờ** | **Đánh giá phản ứng dội ngược** | Rượu gây giãn mạch (giảm HA) lúc mới uống, nhưng gây tăng HA mạnh vào hôm sau do hệ thần kinh bị kích thích lại. |

* Khuyến nghị hành động về tuân thủ điều trị, điều chỉnh dinh dưỡng, vận động để cải thiện các vấn đề được nêu bên trên.

Rule ID: BR-005 Rule Name: Quy tắc Nội dung và Logic hiển thị Báo cáo định kỳ (Tuần/Tháng) Description: 

**1\. Thông tin Người dùng**

* **Nội dung:** Hiển thị các thông tin cơ bản của người dùng và khoảng huyết áp mục tiêu đã thiết lập.  
* *Ví dụ:* Họ và tên: Nguyễn Văn A, Tuổi: 56, Giới tính: Nam. Khoảng Huyết áp Mục tiêu: SYS: 120-130 mmHg, DIA: 70-80 mmHg.

#### **2\. Khoảng Thời gian Báo cáo**

* **Nội dung:** Nêu rõ khoảng thời gian tổng hợp dữ liệu của báo cáo.  
* *Ví dụ:* "Báo cáo tuần từ 12/05/2025 đến 18/05/2025".

#### **3\. Phân tích Theo dõi Huyết áp & Nhịp tim**

* **Tỷ lệ Tuân thủ Lịch đo:**  
  * **Logic:** Tính toán dựa trên công thức: (Số ngày có lượt đo /Tổng số ngày trong kỳ báo cáo) x 100%.  (%, làm tròn 1 số sau dấu phẩy)  
  * **Hiển thị:** Dưới dạng phần trăm và một thanh tiến trình (progress bar) để trực quan.  
* **Tổng quan chỉ số trong kỳ:**  
  * **Logic:** Tính toán và hiển thị các chỉ số thống kê từ dữ liệu huyết áp trong kỳ báo cáo.  
  * **Nội dung:**  
    * **Huyết áp Trung bình:** Giá trị SYS/DIA trung bình.  
    * **Huyết áp Cao nhất:** Giá trị SYS/DIA cao nhất.  
    * **Huyết áp Thấp nhất:** Giá trị SYS/DIA thấp nhất.  
    * **Tỷ lệ các lần đo trong ngưỡng mục tiêu** (Lưu ý: chỉ hiển thị cho người đã được chẩn đoán bị bệnh THA)**:** Tỷ lệ số lần đo có kết quả nằm trong ngưỡng mục tiêu

| Chỉ số | Phương pháp tính toán | Công thức |
| ----- | ----- | ----- |
| HA Trung bình | Tính trung bình cộng riêng biệt cho tất cả các giá trị tâm thu và tâm trương. | Tâm thu TB \= Tổng(Tất cả giá trị Tâm thu) / Số lần đo Tâm trương TB \= Tổng(Tất cả giá trị Tâm trương) / Số lần đo |
| HA Cao nhất | Chọn cặp giá trị dựa trên Tâm thu cao nhất | Tìm cặp giá trị có tâm thu cao nhất trong tất cả các cặp giá trị tâm thu/tâm trương.  Nếu có nhiều hơn 2 cặp giá trị trùng giá trị tâm thu cao nhất thì chọn cặp giá trị có tâm trương cao hơn |
| HA Thấp nhất | Chọn cặp giá trị dựa trên Tâm thu thấp nhất | Tìm cặp giá trị có tâm thu thấp nhất trong tất cả các cặp giá trị tâm thu/tâm trương.  Nếu có nhiều hơn 2 cặp giá trị trùng giá trị tâm thu thấp nhất thì chọn cặp giá trị có tâm trương thấp hơn |
| Tỷ lệ các lần đo có kết quả trong ngưỡng mục tiêu | Phần trăm số lần đo có giá trị tâm thu và tâm trương nằm trong khoảng mục tiêu | Tỷ lệ các lần đo có kết quả nằm trong ngưỡng mục tiêu \= Số lần đo có giá trị tâm trương và tâm thu trong ngưỡng mục tiêu/Tổng số lần đo\*100% Lưu ý: Lần đo được coi là trong ngưỡng khi cả tâm thu (SYS)  và tâm trương (DIA) đều trong ngưỡng mục tiêu. Nếu bất kỳ chỉ số nào (SYS hoặc DIA) nằm ngoài khoảng mục tiêu, lần đo đó được coi là ngoài ngưỡng mục tiêu. |

* **Biểu đồ Diễn biến Huyết áp:**  
  * Biểu đồ đường (Line chart): Thể hiện diễn biến của huyết áp tâm thu và tâm trương theo thời gian (ngày) trong suốt kỳ báo cáo. Trục hoành là ngày, trục tung là giá trị huyết áp, 2 khoảng giới hạn biểu diễn ngưỡng huyết áp tâm thu \- tâm trương mục tiêu  
  * Nếu một ngày có nhiều lần đo, điểm dữ liệu có thể là giá trị trung bình của ngày hôm đó.  
* **Nhận xét tự động về huyết áp:**  
  * **Logic hiển thị:** Tạo ra các nhận xét dựa trên phân tích dữ liệu huyết áp của kỳ báo cáo so với kỳ trước và các dữ liệu liên quan khác.  
    * **Phân tích xu hướng:** So sánh huyết áp trung bình của kỳ này với kỳ trước.  
    * **Phát hiện bất thường:** Đếm số lần đo vượt ngưỡng mục tiêu và xác định các thời điểm/ngày thường xảy ra.  
    * **Phân tích tương quan:** Kiểm tra xem ngày có huyết áp bất thường có trùng với ngày người dùng ghi nhận triệu chứng bất thường không.  
  * *Ví dụ:* "So với tuần trước, huyết áp trung bình của bạn có xu hướng **giảm nhẹ**. Số lần đo vượt ngưỡng mục tiêu là **3 lần**, chủ yếu vào buổi sáng. Ngày có huyết áp cao nhất (14/05) trùng với thời điểm bạn ghi nhận triệu chứng 'Đau đầu'."  
* **Biểu đồ và Phân tích Nhịp tim:**  
  * **Biểu đồ đường (Line chart):** Thể hiện diễn biến của nhịp tim theo thời gian (ngày) trong suốt kỳ báo cáo. Trục hoành là ngày, trục tung là giá trị nhịp tim.  
  * Nếu một ngày có nhiều lần đo, điểm dữ liệu có thể là giá trị trung bình của ngày hôm đó.  
* **Nhận xét tự động về nhịp tim:**		  
  * **Phân tích xu hướng:** So sánh nhịp tim trung bình của kỳ này với kỳ trước để xác định xu hướng chung (tăng, giảm, ổn định).  
    * **Phát hiện bất thường:** Đếm số lần nhịp tim nằm ngoài khoảng an toàn (ví dụ: quá nhanh hoặc quá chậm) và xác định các quy luật về thời gian xảy ra.  
    * **Phân tích tương quan:** Tìm mối liên hệ giữa những ngày có nhịp tim bất thường với các triệu chứng người dùng đã ghi nhận (ví dụ: "hồi hộp", "khó thở") hoặc các hoạt động cụ thể.

#### **4\. Đánh giá Nguy cơ Biến chứng Tim mạch**

* **Mục tiêu:** Cung cấp một ước tính về nguy cơ mắc các biến cố tim mạch trong 10 năm tới.  
* **Logic lựa chọn thang điểm và tính toán:** Hệ thống tự động chọn thang điểm phù hợp nhất dựa trên thông tin người dùng (tuổi, giới tính, tiền sử bệnh...): SCORE2, SCORE2-OP, ASCVD (PCE), SCORE Diabetes.

  ##  ***1\. Thang điểm SCORE2***

  ***Mục đích:** Ước tính nguy cơ 10 năm của biến cố tim mạch **gây tử vong và không gây tử vong** (nhồi máu cơ tim, đột quỵ).*

  ### ***Đối tượng sử dụng***

* *Người trưởng thành **từ 40 đến 69 tuổi**.*  
* *Không có tiền sử bệnh tim mạch (CVD) hoặc đái tháo đường.*

	*\*Lưu ý: Trong danh sách bệnh nền, bệnh tim mạch (CVD) bao gồm:*

	*\- (5) Bệnh mạch vành*

*\- (12) Cơn đau thắt ngực.*

*\- (6) Suy tim và phì đại thất trái.*

*\- (10) Hẹp động mạch cảnh*

*\- (19) Hẹp động mạch thận.*

*\- (13) Bệnh mạch máu ngoại vi.*

*\- (8) Cơn thiếu máu não thoáng qua.*

*\- (11) Nhồi máu cơ tim.*

*\- (7) Đột quỵ*

*\- (17) Nhồi máu não*

*\- (18) Xuất huyết não.*

### ***Input đầu vào***

*Các thông tin cần thiết để tính toán điểm số bao gồm:*

* ***Vùng nguy cơ của quốc gia:** Cao (Việt Nam được xếp vào vùng nguy cơ cao)*  
* ***Giới tính:** Nam / Nữ \=\> Lấy trong profile người dùng*  
* ***Tuổi:** Tính theo năm \=\> Lấy trong profile người dùng*  
* ***Tình trạng hút thuốc:** Có / Không \=\> Từ nhiệm vụ khảo sát*  
* ***Huyết áp tâm thu (Systolic Blood Pressure \- SBP):** mmHg \=\> Giá trị tâm thu trung bình trong khoảng thời gian báo cáo*   
* ***Cholesterol toàn phần (Total Cholesterol):** mmol/L hoặc mg/dL \=\> Từ kết quả tái khám*  
* ***HDL Cholesterol:** mmol/L hoặc mg/dL \=\> Từ kết quả tái khám*

  ### ***Tài liệu và Mô hình tính toán***

* ***Công cụ tính toán trực tuyến:***  
  * ***MDCalc:** [https://www.mdcalc.com/calc/10499/systematic-coronary-risk-evaluation-score2](https://www.mdcalc.com/calc/10499/systematic-coronary-risk-evaluation-score2)*   
* ***Bài báo khoa học gốc:***  
  * *SCORE2 working group and ESC Cardiovascular risk collaboration. (2021). SCORE2 risk prediction algorithms: new models to estimate 10-year risk of cardiovascular disease in Europe. European Heart Journal, 42(25), 2439–2454.*  
  * *Link: [https://academic.oup.com/eurheartj/article/42/25/2439/6297709](https://academic.oup.com/eurheartj/article/42/25/2439/6297709)* 

  ## ***2\. Thang điểm SCORE2-OP***

  ***Mục đích:** Ước tính nguy cơ 10 năm của biến cố tim mạch **gây tử vong và không gây tử vong** (nhồi máu cơ tim, đột quỵ).*

  ### ***Đối tượng sử dụng***

* *Người trưởng thành **từ 70 tuổi trở lên**.*  
* *Không có tiền sử bệnh tim mạch (CVD) hoặc đái tháo đường.*

	*\*Lưu ý: Trong danh sách bệnh nền, bệnh tim mạch (CVD) bao gồm:*

	*\- (5) Bệnh mạch vành*

*\- (12) Cơn đau thắt ngực.*

*\- (6) Suy tim và phì đại thất trái.*

*\- (10) Hẹp động mạch cảnh*

*\- (19) Hẹp động mạch thận.*

*\- (13) Bệnh mạch máu ngoại vi.*

*\- (8) Cơn thiếu máu não thoáng qua.*

*\- (11) Nhồi máu cơ tim.*

*\- (7) Đột quỵ*

*\- (17) Nhồi máu não*

*\- (18) Xuất huyết não.*

### ***Input đầu vào***

*Các thông tin đầu vào tương tự như SCORE2:*

* ***Vùng nguy cơ của quốc gia:** Cao (Việt Nam được xếp vào vùng nguy cơ cao)*  
* ***Giới tính:** Nam / Nữ \=\> Lấy trong profile người dùng*  
* ***Tuổi:** Tính theo năm \=\> Lấy trong profile người dùng*  
* ***Tình trạng hút thuốc:** Có / Không \=\> Từ nhiệm vụ khảo sát*  
* ***Huyết áp tâm thu (Systolic Blood Pressure \- SBP):** mmHg \=\> Giá trị tâm thu trung bình trong khoảng thời gian báo cáo*  
* ***Cholesterol toàn phần (Total Cholesterol):** mmol/L hoặc mg/dL \=\> Từ kết quả tái khám*  
* ***HDL Cholesterol:** mmol/L hoặc mg/dL \=\> Từ kết quả tái khám*

  ### ***Tài liệu và Mô hình tính toán***

* ***Công cụ tính toán trực tuyến:***  
  * ***MDCalc:** [https://www.mdcalc.com/calc/10503/score2-older-persons-score2-op](https://www.mdcalc.com/calc/10503/score2-older-persons-score2-op)*   
* ***Bài báo khoa học gốc:***  
  * *SCORE2-OP working group and ESC Cardiovascular risk collaboration. (2021). SCORE2-OP risk prediction algorithms: estimating incident cardiovascular event risk in older persons in four geographical risk regions. European Heart Journal, 42(25), 2455–2467.*  
  * *Link: [https://academic.oup.com/eurheartj/article/42/25/2455/6297711](https://academic.oup.com/eurheartj/article/42/25/2455/6297711)* 

  ## ***3\. Thang điểm SCORE2-Diabetes***

  ***Mục đích:** Ước tính nguy cơ 10 năm của biến cố tim mạch **gây tử vong và không gây tử vong** (nhồi máu cơ tim, đột quỵ).*

  ***Đối tượng:*** 

* *Người **dưới 70 tuổi***  
* *Mắc bệnh đái tháo đường*  
* *Không có tiền sử bệnh tim mạch (CVD).*  
  *\*Lưu ý: Trong danh sách bệnh nền, bệnh tim mạch (CVD) bao gồm:*

	*\- (5) Bệnh mạch vành*

*\- (12) Cơn đau thắt ngực.*

*\- (6) Suy tim và phì đại thất trái.*

*\- (10) Hẹp động mạch cảnh*

*\- (19) Hẹp động mạch thận.*

*\- (13) Bệnh mạch máu ngoại vi.*

*\- (8) Cơn thiếu máu não thoáng qua.*

*\- (11) Nhồi máu cơ tim.*

*\- (7) Đột quỵ*

*\- (17) Nhồi máu não*

*\- (18) Xuất huyết não.*

***Input đầu vào:***

1. ***Vùng nguy cơ của quốc gia:** Cao (Việt Nam được xếp vào vùng nguy cơ cao)*  
2. ***Giới tính:** Nam / Nữ \=\> Lấy trong profile người dùng*  
3. ***Tuổi:** Tính theo năm \=\> Lấy trong profile người dùng*  
4. ***Tình trạng hút thuốc:** Có / Không \=\> Từ nhiệm vụ khảo sát*  
5. ***Huyết áp tâm thu (Systolic Blood Pressure \- SBP):** mmHg \=\> Giá trị tâm thu trung bình trong khoảng thời gian báo cáo*   
6. ***Cholesterol toàn phần (Total Cholesterol):** mmol/L hoặc mg/dL \=\> Từ kết quả tái khám*  
7. ***HDL Cholesterol:** mmol/L hoặc mg/dL \=\> Từ kết quả tái khám*  
8. ***HbA1c (%)** \=\> Từ kết quả tái khám*  
9. ***Độ lọc cầu thận ước tính (eGFR)** \=\> Từ kết quả tái khám*  
10. ***Thời gian mắc bệnh ĐTĐ (năm)** \=\> Từ nhiệm vụ khảo sát*

    ### ***Tài liệu và Mô hình tính toán***

* ***Công cụ tính toán trực tuyến:***  
  * ***MDCalc:** [https://www.mdcalc.com/calc/10510/score2-diabetes](https://www.mdcalc.com/calc/10510/score2-diabetes)*  
* ***Bài báo khoa học:***   
  * *D. M. A. van der Lee, R. M. et al. (2023). SCORE2-Diabetes: 10-year cardiovascular risk estimation in patients with type 2 diabetes in Europe. European Heart Journal, 44(28), 2544–2556.*  
  * *Link: [https://academic.oup.com/eurheartj/article/44/28/2544/7185610](https://academic.oup.com/eurheartj/article/44/28/2544/7185610)*   
* **Hiển thị kết quả:**  
  * **Chỉ số nguy cơ:** Hiển thị kết quả ước tính dưới dạng phần trăm.  (%, làm tròn 1 số sau dấu phẩy)  
  * **Phân loại mức độ nguy cơ:** Sử dụng một thanh màu hoặc thước đo trực quan để phân loại nguy cơ: Thấp, Trung bình, Cao, Rất cao.  
* **Diễn giải & Khuyến nghị:**  
  * Một đoạn diễn giải về mức độ nguy cơ và thông điệp cốt lõi (trấn an, cảnh báo,...)  
  * Khuyến nghị tương ứng về lối sống, hành động y tế, nguy cơ tiến triển nếu không kiểm soát.  
* **Lưu ý quan trọng:** hiển thị text “Kết quả này được phân tích dựa trên các thang điểm dự đoán nguy cơ tim mạch (SCORE2, SCORE OP, SCORE Diabetes), không thay thế chỉ định y khoa.”

#### **5\. Tổng hợp Ghi nhận Triệu chứng**

* **Hiển thị:** Trình bày dưới dạng danh sách hoặc dòng thời gian, bao gồm: Thời điểm \- Triệu chứng \- Mô tả chi tiết.  
* **Nhận xét Tự động:**  
  * **Logic hiển thị:**  
    * **So sánh số lượng:** Đếm số lượng triệu chứng trong kỳ và so sánh với kỳ trước.  
    * **Tìm kiếm quy luật:** Phân tích xem có triệu chứng nào lặp lại vào một thời điểm cụ thể trong ngày/tuần không.  
  * *Ví dụ:* "Bạn đã ghi nhận **3** triệu chứng trong tuần này, **nhiều hơn** so với tuần trước. Triệu chứng 'Chóng mặt' thường xuất hiện vào buổi sáng."

#### **6\. Báo cáo Tuân thủ Dùng thuốc**

* **Tỷ lệ Tuân thủ:**  
  * **Logic:** Tính toán dựa trên công thức: (Số liều báo cáo đã uống/ Tổng số liều phải uống) x 100%  (%, làm tròn 1 số sau dấu phẩy)  
* **Chi tiết các lần quên/sai liều:**  
  * **Logic:** Liệt kê các bản ghi về việc quên hoặc uống sai liều mà người dùng đã nhập.  
* **Nhận xét Tự động:**  
  * **Logic hiển thị:**  
    * **Đánh giá chung:** Dựa vào tỷ lệ tuân thủ để đưa ra nhận xét (ví dụ: \>95% là rất tốt).  
    * **Tìm kiếm quy luật:** Phân tích xem việc quên thuốc có thường xảy ra vào một buổi cụ thể (sáng/tối) hoặc ngày cụ thể không.  
  * *Ví dụ:* "Tỷ lệ tuân thủ uống thuốc của bạn tuần này rất tốt, đạt 95%. Dường như bạn hay quên liều thuốc vào buổi tối, hãy thử đặt lời nhắc bổ sung."

#### **7\. Phân tích Lối sống**

* **Logic hiển thị:** Nếu người dùng có ghi nhận các hoạt động lối sống, hệ thống sẽ tổng hợp và phân tích tương quan giữa chúng và chỉ số huyết áp.  
  * **Tổng hợp hoạt động:** Đếm số ngày có hoạt động thể chất, số bữa ăn nhiều muối, v.v.  
  * **Phân tích tương quan:** So sánh huyết áp trung bình vào những ngày có hoạt động tích cực (ví dụ: đi bộ) với những ngày không có.  
* *Ví dụ:* "Bạn đã ghi nhận **3/7** ngày có đi bộ. Chúng tôi nhận thấy huyết áp của bạn có xu hướng tốt hơn vào những ngày bạn có hoạt động thể chất."

#### **8\. Lời khuyên Chung và Động viên**

* **Logic hiển thị:** Nội dung được cá nhân hóa dựa trên việc phân tích tổng hợp dữ liệu trong kỳ báo cáo. Hệ thống sẽ đánh giá dựa trên các yếu tố chính: tỷ lệ tuân thủ (đo huyết áp, uống thuốc), tỷ lệ chỉ số trong ngưỡng mục tiêu, và xu hướng huyết áp so với kỳ trước.  
  * **Trường hợp 1: Kết quả tích cực** 

  *Ví dụ:* "Thật tuyệt vời\! Các chỉ số và tỷ lệ tuân thủ của bạn trong tuần này rất đáng khen. Hãy tiếp tục phát huy nhé\!"

  * **Trường hợp 2: Có điểm cần cải thiện** 

  *Ví dụ:* "Tuần này có một vài chỉ số vượt ngưỡng. Hãy chú ý hơn đến việc tuân thủ lịch trình và trao đổi với bác sĩ nếu cần."

  * **Trường hợp 3: Cần chú ý đặc biệt** 

  *Ví dụ:* "Chúng tôi nhận thấy tỷ lệ tuân thủ của bạn tuần này khá thấp, đồng thời huyết áp có xu hướng tăng. Vui lòng trao đổi với bác sĩ để có lời khuyên phù hợp."

* **Mục tiêu cho kỳ tới:** Đưa ra một mục tiêu cụ thể, có thể đo lường được.  
  * *Ví dụ:* "Hãy cùng đặt mục tiêu cho tuần tới là duy trì tỷ lệ đo huyết áp trên 90% nhé\!"

#### **9\. Miễn trừ Trách nhiệm**

* Luôn hiển thị dòng chữ: "Lưu ý: Báo cáo này được tạo ra dựa trên thông tin bạn cung cấp và không thay thế cho chẩn đoán hay tư vấn trực tiếp từ bác sĩ hoặc chuyên gia y tế."

Rule ID: BR-006 

Rule Name: Quy tắc xử lý trường hợp không có dữ liệu cho Tiêu điểm ngày 

Description:

* **Định nghĩa "Không có dữ liệu":** Người dùng không có bất kỳ chỉ số huyết áp nào được ghi nhận trong ngày.  
* **Logic xử lý giao diện:**  
  * **Khu vực "Góc sức khỏe hôm nay":**  
    * Thời gian đo: Hiển thị "--:--"  
    * Chỉ số Tâm thu/Tâm trương: Hiển thị "--"  
    * Nhận xét: Hiển thị thông điệp nêu rõ thực trạng và nhắc nhở người dùng, ví dụ: "Bạn chưa có lần đo nào hôm nay. Hãy thực hiện lần đo đầu tiên để theo dõi sức khỏe nhé\!".

Rule ID: BR-007 

Rule Name: Quy tắc xử lý trường hợp không có dữ liệu cho Báo cáo định kỳ 

Description:

* **Định nghĩa "Không có dữ liệu":** Không có bất kỳ dữ liệu nào của một phần thông tin cụ thể được ghi nhận trong khoảng thời gian của báo cáo.  
* **Logic xử lý cho từng phần:**  
  * **Phân tích huyết áp và nhịp tim:**  
    * Tổng quan chỉ số (Trung bình, Cao nhất, Thấp nhất): Hiển thị giá trị là "--".  
    * Biểu đồ: Không hiển thị biểu đồ, thay bằng dòng chữ: "Không có đủ dữ liệu để tạo biểu đồ".  
    * Nhận xét: Vẫn hiển thị nhận xét, nội dung bao gồm: (1) Nêu thực trạng không có dữ liệu, (2) Nêu lợi ích của việc theo dõi thường xuyên, (3) Nhắc nhở người dùng cải thiện trong kỳ báo cáo tới.  
  * **Đánh giá nguy cơ biến chứng:**  
    * Infographic: Vẫn hiển thị bình thường vì được tính toán dựa trên thông tin cá nhân của người dùng.  
    * Diễn giải: Nội dung giải thích ý nghĩa con số nguy cơ và nhấn mạnh rằng việc cung cấp thêm dữ liệu sức khỏe sẽ giúp kết quả ước tính chính xác hơn.  
  * **Tổng hợp triệu chứng:**  
    * Danh sách triệu chứng: Hiển thị dòng chữ "Không có dữ liệu".  
    * Nhận xét: Vẫn hiển thị nhận xét với cấu trúc tương tự như phần Phân tích huyết áp.  
  * **Báo cáo tuân thủ dùng thuốc:**  
    * Tỷ lệ và chi tiết: Hiển thị "Không có dữ liệu".  
    * Nhận xét: Vẫn hiển thị nhận xét với cấu trúc tương tự.  
  * **Phân tích lối sống:**  
    * Nội dung phân tích: Hiển thị nhận xét với cấu trúc tương tự.  
  * **Lời khuyên chung và Động viên:**  
    * Nội dung: Vẫn hiển thị, tập trung vào việc động viên người dùng bắt đầu theo dõi và đặt mục tiêu cho kỳ báo cáo tiếp theo.

**Rule ID: BR-008** 

**Rule** Name: Quy tắc điều **hướng từ nút "Thực hiện" nhiệm vụ** 

**Description:** Khi người dùng nhấn nút "Thực hiện" trên một nhiệm vụ chưa hoàn thành trong danh sách nhiệm vụ của "Tiêu điểm ngày", hệ thống phải điều hướng người dùng đến màn hình chức năng tương ứng của nhiệm vụ đó.

* **Ví dụ:** Nhấn "Thực hiện" ở nhiệm vụ "Đo huyết áp" sẽ mở màn hình Đo huyết áp.

**Rule ID: BR-009**

**Rule Name: Quy tắc chức năng "Chia sẻ báo cáo"** 

**Description:**

* Khi người dùng nhấn nút "Chia sẻ báo cáo" từ màn hình chi tiết báo cáo định kỳ, hệ thống sẽ tạo một file **PDF (định dạng .pdf)**, chứa toàn bộ nội dung của chi tiết báo cáo.  
* Bố cục và nội dung của file PDF phải giữ nguyên như trên giao diện ứng dụng.  
* Sau khi tạo file PDF, hệ thống sẽ mở menu chia sẻ mặc định của hệ điều hành 

**Rule ID:** BR-010 

**Rule Name:** Quy tắc Phân loại Nguy cơ Tim mạch theo từng Thang điểm 

**Description:** Quy tắc này định nghĩa sự tương ứng giữa chỉ số nguy cơ biến chứng tim mạch (tính theo %), văn bản phân loại mức độ và màu sắc được sử dụng để hiển thị trên giao diện người dùng (ví dụ: trong biểu đồ tròn).

Quy tắc áp dụng cho 3 thang điểm riêng biệt: **SCORE2**, **SCORE2-OP**, và **SCORE2-Diabetes**.

### **1\. Thang điểm SCORE2 (Dành cho người 40-69 tuổi)**

Áp dụng cho người dùng không mắc tiểu đường.

Ngưỡng phân loại của SCORE2 thay đổi tùy theo độ tuổi của người bệnh (chia thành 2 nhóm tuổi nhỏ).

| Độ tuổi người dùng | Tỷ lệ % Nguy cơ (10 năm) | Phân loại Nguy cơ (Risk Class) | Màu sắc (Visual) |
| :---- | :---- | :---- | :---- |
| **Dưới 50 tuổi** | \< 2.5% | Thấp đến Trung bình | Xanh lá |
|  | 2.5% \- \< 7.5% | Cao | Cam |
|  | ≥ 7.5% | Rất cao | Đỏ |
| **Từ 50 đến 69 tuổi** | \< 5.0% | Thấp đến Trung bình | Xanh lá |
|  | 5.0% \- \< 10% | Cao | Cam |
|  | ≥ 10% | Rất cao | Đỏ |

### 

### **2\. Thang điểm SCORE2-OP (Dành cho người ≥ 70 tuổi)**

Áp dụng cho người cao tuổi (Older Persons).

Do tuổi cao là một yếu tố nguy cơ tự nhiên, ngưỡng phân loại của SCORE2-OP cao hơn so với người trẻ.

| Độ tuổi người dùng | Tỷ lệ % Nguy cơ (10 năm) | Phân loại Nguy cơ (Risk Class) | Màu sắc (Visual) |
| :---- | :---- | :---- | :---- |
| **Từ 70 tuổi trở lên** | \< 7.5% | Thấp đến Trung bình | Xanh lá |
|  | 7.5% \- \< 15% | Cao | Cam |
|  | ≥ 15% | Rất cao | Đỏ |

### 

### **3\. Thang điểm SCORE2-Diabetes (Dành cho người mắc Đái tháo đường)**

Áp dụng cho bệnh nhân Đái tháo đường type 2 (40-69 tuổi).

Theo hướng dẫn lâm sàng, việc đánh giá mức độ nguy cơ cho bệnh nhân tiểu đường cũng dựa trên độ tuổi tương tự như quần thể chung (SCORE2).

| Độ tuổi người dùng | Tỷ lệ % Nguy cơ (10 năm) | Phân loại Nguy cơ (Risk Class) | Màu sắc (Visual) |
| :---- | :---- | :---- | :---- |
| **Dưới 50 tuổi** | \< 2.5% | Thấp đến Trung bình | Xanh lá |
|  | 2.5% \- \< 7.5% | Cao | Cam |
|  | ≥ 7.5% | Rất cao | Đỏ |
| **Từ 50 đến 69 tuổi** | \< 5.0% | Thấp đến Trung bình | Xanh lá |
|  | 5.0% \- \< 10% | Cao | Cam |
|  | ≥ 10% | Rất cao | Đỏ |

# **PHẦN 4: COMPONENT DESCRIPTION**

## **4.1 Component Dùng Chung**

Component 1: Thanh điều hướng dưới cùng (Bottom Navigation Bar)  
Type: Navigation Bar  
Data Type: Array  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Enabled  
Available State: \- Active (khi người dùng đang ở màn hình tương ứng)  
Default Value: Mục "Báo cáo" được Active khi người dùng ở Màn hình Báo cáo.  
Available Value: \["Trang chủ", "Báo cáo", "Cây của Alio", "Giáo dục", "Kết nối người thân"\]  
Validation Rule: N/A  
Behavior: Nhấn vào một mục sẽ điều hướng người dùng đến màn hình tương ứng và cập nhật trạng thái Active.

## **4.2 Component Riêng Của Từng Màn**

### **4.2.1 Màn 1: Báo cáo Sức khỏe**

Component 1.1: Tiêu đề màn hình  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: "Báo cáo sức khỏe"  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: N/A  
Behavior: N/A

Component 1.2: Cụm Tab điều hướng  
Type: Tab Group  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Enabled  
Available State: \- Active (tab đang được chọn)  
Default Value: "Tiêu điểm ngày"  
Available Value: \["Tiêu điểm ngày", "Báo cáo định kỳ"\]  
Validation Rule: N/A  
Behavior: Khi nhấn vào một tab, nội dung bên dưới sẽ được cập nhật tương ứng với tab đó.

\-- CÁC COMPONENT THUỘC TAB "Tiêu điểm ngày" \--  
Component 1.3: Banner chào hỏi  
Type: Card  
Data Type: Object  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-004  
Behavior: Là container cho các component con (Ảnh, Tiêu đề, Mô tả). Nội dung và hình ảnh thay đổi theo thời gian trong ngày.

Component 1.3.1: Tiêu đề Banner  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: "Buổi sáng tốt lành" (Phụ thuộc vào thời gian thực)  
Available Value: \["Buổi sáng tốt lành", "Buổi trưa năng động", "Buổi chiều hiệu quả", "Buổi tối thư giãn"\]  
Validation Rule: BR-004  
Behavior: N/A

Component 1.3.2: Mô tả Banner  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: "Dưới đây là tổng quan về sức khỏe và các nhiệm vụ anh Dũng cần hoàn thành hôm nay" (Nội dung được AI tạo ra)  
Available Value: N/A  
Validation Rule: BR-004, GR-BIZ-01  
Behavior: N/A

Component 1.3.3: Ảnh minh họa Banner  
Type: Image  
Data Type: File  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-004  
Behavior: N/A

Component 1.4: Tiêu đề mục "Góc sức khỏe hôm nay"  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: "Góc sức khỏe hôm nay"  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: N/A  
Behavior: N/A

Component 1.5: Thẻ "Góc sức khỏe hôm nay"  
Type: Card  
Data Type: Object  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-006  
Behavior: Hiển thị dữ liệu lần đo huyết áp gần nhất trong ngày.

Component 1.5.1: Icon Trạng thái  
Type: Icon  
Data Type: N/A  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: Icon mặt trời  
Available Value: N/A  
Validation Rule: N/A  
Behavior: N/A

Component 1.5.2: Thời gian đo  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: "--:--" (khi không có dữ liệu)  
Available Value: Bất kỳ giá trị thời gian hợp lệ nào theo định dạng HH:mm  
Validation Rule: BR-006  
Behavior: N/A

Component 1.5.3: Text link “Cập nhật”  
Type: Text link  
Data Type: N/A  
Required: No  
Label: "Cập nhật"  
Placeholder: N/A  
Default State: Enabled  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: N/A  
Behavior: Khi người dùng nhấn chọn textlink \> ứng dụng điều hướng sang màn nhiệm vụ Đo huyết áp.

Component 1.5.4: Giá trị Tâm thu  
Type: Text Label  
Data Type: Number  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: "--" (khi không có dữ liệu)  
Available Value: Số nguyên dương  
Validation Rule: BR-006  
Behavior: N/A

Component 1.5.5: Nhãn Tâm thu  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: "Tâm thu"  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: N/A  
Behavior: N/A

Component 1.5.6: Giá trị Tâm trương  
Type: Text Label  
Data Type: Number  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: "--" (khi không có dữ liệu)  
Available Value: Số nguyên dương  
Validation Rule: BR-006  
Behavior: N/A

Component 1.5.7: Nhãn Tâm trương  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: "Tâm trương"  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: N/A  
Behavior: N/A

Component 1.6: Thẻ Nhận xét Huyết áp  
Type: Card  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: Nội dung do AI tạo ra.  
Available Value: N/A  
Validation Rule: BR-004, BR-006  
Behavior: Hiển thị nhận xét về chỉ số huyết áp hoặc lời nhắc nhở khi chưa có dữ liệu.

Component 1.7: Tiêu đề mục "Nhiệm vụ trong ngày"  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: "Nhiệm vụ trong ngày"  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: N/A  
Behavior: N/A

Component 1.8: Thẻ Tiến độ Nhiệm vụ  
Type: Card  
Data Type: Object  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-004  
Behavior: Hiển thị tổng quan tiến độ hoàn thành nhiệm vụ trong ngày.

Component 1.8.1: Tiêu đề tiến độ  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: "Anh đã hoàn thành" (Nội dung động theo danh xưng)  
Available Value: N/A  
Validation Rule: GR-BIZ-01  
Behavior: N/A

Component 1.8.2: Văn bản tiến độ  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: "X/Y nhiệm vụ"  
Available Value: N/A  
Validation Rule: BR-004  
Behavior: Hiển thị số nhiệm vụ hoàn thành / tổng số nhiệm vụ.

Component 1.8.3: Thanh tiến độ  
Type: Progress Bar  
Data Type: Number  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: 0  
Available Value: 0-100  
Validation Rule: BR-004  
Behavior: Thể hiện % nhiệm vụ đã hoàn thành.

Component 1.9: Nút "Xem/Ẩn chi tiết nhiệm vụ"  
Type: Button  
Data Type: String  
Required: N/A  
Label: "Xem chi tiết nhiệm vụ"  
Placeholder: N/A  
Default State: Enabled  
Available State: \- Trạng thái mở rộng: Label đổi thành "Ẩn chi tiết nhiệm vụ"  
Default Value: N/A  
Available Value: N/A  
Validation Rule: N/A  
Behavior: Khi nhấn, hiển thị hoặc ẩn Component 1.10.

Component 1.10: Danh sách chi tiết nhiệm vụ  
Type: List View  
Data Type: Array  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Hidden  
Available State: \- Visible (khi người dùng nhấn Component 1.9)  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-004  
Behavior: Hiển thị danh sách các thẻ nhiệm vụ con.

Component 1.10.1: Thẻ Nhiệm vụ (Item)  
Type: Card  
Data Type: Object  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Enabled  
Available State: \- Completed (nền mờ hơn, không có nút Thực hiện)  
Default Value: N/A  
Available Value: N/A  
Validation Rule: N/A  
Behavior: Là container cho các thông tin của một nhiệm vụ.

Component 1.10.1.1: Icon Trạng thái Nhiệm vụ  
Type: Icon  
Data Type: N/A  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: \- Completed (hiển thị icon dấu tick màu xanh)  
Default Value: Icon vòng tròn nét đứt  
Available Value: N/A  
Validation Rule: N/A  
Behavior: N/A

Component 1.10.1.2: Tên nhiệm vụ  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: \["Đo huyết áp", "Uống thuốc", "Tái khám", ...\]  
Validation Rule: N/A  
Behavior: N/A

Component 1.10.1.3: Nút "Thực hiện"  
Type: Button  
Data Type: N/A  
Required: N/A  
Label: "Thực hiện"  
Placeholder: N/A  
Default State: Enabled  
Available State: \- Hidden (khi nhiệm vụ đã hoàn thành)  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-008  
Behavior: Khi nhấn, điều hướng đến màn hình chức năng tương ứng của nhiệm vụ.

Component 1.11: Thẻ Thông điệp động viên  
Type: Card  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: Nội dung do AI tạo ra.  
Available Value: N/A  
Validation Rule: BR-004  
Behavior: Hiển thị thông điệp động viên dựa trên tiến độ nhiệm vụ.

Component 1.12: Nút "Tư vấn thêm"  
Type: Button  
Data Type: N/A  
Required: N/A  
Label: "Tư vấn thêm"  
Placeholder: N/A  
Default State: Enabled  
Available State: \- Active (khi nhấn)  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-011  
Behavior: Khi nhấn, mở màn hình chat với Alio.

Component 1.13: Thanh điều hướng dưới cùng  
Tham chiếu: Component Dùng Chung 1

### **4.2.2 Màn 2: Danh sách Báo cáo định kỳ**

Ghi chú: Màn hình này là nội dung của tab "Báo cáo định kỳ" trên Màn 1\.

Component 2.1: Nút Lọc báo cáo  
Type: Dropdown Button  
Data Type: String  
Required: N/A  
Label: "Danh sách theo tuần"  
Placeholder: N/A  
Default State: Enabled  
Available State: \- Active (khi nhấn để mở bottom sheet)  
Default Value: "Danh sách theo tuần"  
Available Value: \["Danh sách theo tuần", "Danh sách theo tháng"\]  
Validation Rule: N/A  
Behavior: Khi nhấn, mở Màn 4.2.3: Bottom Sheet Lọc báo cáo.

Component 2.2: Danh sách báo cáo  
Type: List View  
Data Type: Array  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: \- Empty (khi không có báo cáo nào, hiển thị Component 2.4)  
Default Value: N/A  
Available Value: N/A  
Validation Rule: N/A  
Behavior: Hiển thị danh sách các báo cáo.

Component 2.3: Thẻ Báo cáo (Item)  
Type: Button  
Data Type: Object  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Enabled  
Available State: \- Active (khi nhấn)  
Default Value: N/A  
Available Value: N/A  
Validation Rule: N/A  
Behavior: Khi nhấn, điều hướng đến Màn 4.2.4: Chi tiết báo cáo định kỳ.

Component 2.3.1: Icon báo cáo  
Type: Icon  
Data Type: N/A  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: Icon clipboard  
Available Value: N/A  
Validation Rule: N/A  
Behavior: N/A

Component 2.3.2: Tiêu đề báo cáo  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: "Báo cáo tuần" / "Báo cáo tháng"  
Available Value: N/A  
Validation Rule: N/A  
Behavior: N/A

Component 2.3.3: Khoảng thời gian báo cáo  
Type: Text Label  
Data Type: N/A  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: "dd/mm/yyyy \- dd/mm/yyyy"  
Available Value: N/A  
Validation Rule: N/A  
Behavior: 

* Nếu là báo cáo tuần, khoảng thời gian là 7 ngày.   
* Nếu là báo cáo tháng, khoảng thời gian là số ngày của tháng đó.

Component 2.3.4: Icon Điều hướng  
Type: Icon  
Data Type: N/A  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: Icon mũi tên sang phải  
Available Value: N/A  
Validation Rule: N/A  
Behavior: N/A

Component 2.4: Giao diện Trạng thái trống  
Type: Custom View  
Data Type: N/A  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Hidden  
Available State: \- Visible (khi Component 2.2 rỗng)  
Default Value: N/A  
Available Value: N/A  
Validation Rule: N/A  
Behavior: Hiển thị khi không có dữ liệu báo cáo.

Component 2.4.1: Ảnh minh họa  
Type: Image  
Data Type: File  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: N/A  
Behavior: N/A

Component 2.4.2: Văn bản thông báo  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: "Chưa có dữ liệu báo cáo"  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: N/A  
Behavior: N/A

### **4.2.3 Màn 3: Bottom Sheet Lọc báo cáo**

Component 3.1: Lựa chọn "Danh sách theo tuần"  
Type: Button  
Data Type: N/A  
Required: N/A  
Label: "Danh sách theo tuần"  
Placeholder: N/A  
Default State: Enabled  
Available State: \- Selected (nếu đang là bộ lọc hiện tại)  
Default Value: N/A  
Available Value: N/A  
Validation Rule: N/A  
Behavior: Khi nhấn, cập nhật danh sách ở Màn 2 và đóng bottom sheet.

Component 3.2: Lựa chọn "Danh sách theo tháng"  
Type: Button  
Data Type: N/A  
Required: N/A  
Label: "Danh sách theo tháng"  
Placeholder: N/A  
Default State: Enabled  
Available State: \- Selected (nếu đang là bộ lọc hiện tại)  
Default Value: N/A  
Available Value: N/A  
Validation Rule: N/A  
Behavior: Khi nhấn, cập nhật danh sách ở Màn 2 và đóng bottom sheet.

### **4.2.4 Màn 4: Chi tiết báo cáo định kỳ**

Component 4.1: Nút Quay lại  
Type: Icon Button  
Data Type: N/A  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Enabled  
Available State: \- Active (khi nhấn)  
Default Value: N/A  
Available Value: N/A  
Validation Rule: N/A  
Behavior: Khi nhấn, quay lại Màn 2\.

Component 4.2: Tiêu đề màn hình  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: "Báo cáo tuần" / "Báo cáo tháng"  
Available Value: N/A  
Validation Rule: N/A  
Behavior: N/A

\-- MỤC "THÔNG TIN NGƯỜI DÙNG" \--  
Component 4.3 \- 4.6: Các nhãn và giá trị thông tin  
(Họ tên, Tuổi, Giới tính, Huyết áp mục tiêu)  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-005  
Behavior: Hiển thị thông tin tĩnh lấy từ hồ sơ người dùng.

\-- MỤC "KHOẢNG THỜI GIAN BÁO CÁO" \--  
Component 4.7: Văn bản khoảng thời gian  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: "Báo cáo tuần từ dd/mm/yyyy đến dd/mm/yyyy"  
Available Value: N/A  
Validation Rule: BR-005  
Behavior: N/A

\-- MỤC "PHÂN TÍCH HUYẾT ÁP & NHỊP TIM" \--  
Component 4.8: Tỷ lệ tuân thủ lịch đo HA  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: "Tỷ lệ tuân thủ lịch đo huyết áp"  
Placeholder: N/A  
Default State: Visible  
Available State: \- No Data: Hiển thị "Không có dữ liệu"  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: N/A

Component 4.9: Thanh tiến trình tuân thủ  
Type: Progress Bar  
Data Type: Number  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: \- Hidden (khi không có dữ liệu)  
Default Value: N/A  
Available Value: 0-100  
Validation Rule: BR-005, BR-007  
Behavior: N/A

Component 4.10 \- 4.13: Các thẻ chỉ số tổng quan  
(HA trung bình, HA cao nhất, HA thấp nhất, Tỷ lệ trong mục tiêu)  
Type: Card  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: \- No Data: Giá trị hiển thị "Không có dữ liệu"  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: Mỗi thẻ chứa một nhãn và một giá trị.

Component 4.14: Biểu đồ diễn biến huyết áp  
Type: Chart  
Data Type: Array  
Required: N/A  
Label: "Biểu đồ diễn biến huyết áp"  
Placeholder: N/A  
Default State: Visible  
Available State: \- No Data: Hiển thị văn bản "Không có đủ dữ liệu để tạo biểu đồ"  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: Hiển thị biểu đồ đường với các điểm dữ liệu Tâm thu, Tâm trương.

Component 4.15: Nhận xét huyết áp  
Type: Card  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: Nội dung do AI tạo ra.  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: Hiển thị nhận xét về xu hướng huyết áp trong kỳ.

\-- MỤC "PHÂN TÍCH NHỊP TIM" \--  
Component 4.16: Các thẻ chỉ số tổng quan Nhịp tim  
(Nhịp tim trung bình, Nhịp tim cao nhất, Nhịp tim thấp nhất)  
Type: Card  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: \- No Data: Giá trị hiển thị "Không có dữ liệu"  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: Mỗi thẻ chứa một nhãn (VD: "Nhịp tim TB") và một giá trị.

Component 4.17: Biểu đồ diễn biến nhịp tim  
Type: Chart  
Data Type: Array  
Required: N/A  
Label: "Biểu đồ diễn biến nhịp tim"  
Placeholder: N/A  
Default State: Visible  
Available State: \- No Data: Hiển thị văn bản "Không có đủ dữ liệu để tạo biểu đồ"  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: Hiển thị biểu đồ đường với các điểm dữ liệu Nhịp tim.

Component 4.18: Nhận xét nhịp tim  
Type: Card  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: Nội dung do AI tạo ra.  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: Hiển thị nhận xét về xu hướng nhịp tim trong kỳ.

\-- MỤC "ĐÁNH GIÁ NGUY CƠ BIẾN CHỨNG" \--  
Component 4.19: Tiêu đề mục  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: "Đánh giá nguy cơ biến chứng"  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: N/A

Component 4.20: Thẻ trực quan hóa Nguy cơ  
Type: Card  
Data Type: N/A  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: \- No Data: Hiển thị "Không có dữ liệu"  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-005, BR-007, BR-010  
Behavior: Là container cho các component con (4.20.1, 4.20.2, 4.20.3) để hiển thị trực quan hóa nguy cơ.

Component 4.20.1: Biểu đồ tròn tiến trình Nguy cơ  
Type: Chart  
Data Type: Number  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-010  
Behavior: Hiển thị một vòng tròn tiến trình (gauge chart). Màu sắc và % hoàn thành của vòng tròn được xác định bởi BR-010 dựa trên giá trị % nguy cơ.

Component 4.20.2: Giá trị % Nguy cơ  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-010  
Behavior: Hiển thị giá trị % của nguy cơ (ví dụ: "12.5%"), nằm ở trung tâm của Component 4.20.1.

Component 4.20.3: Phân loại Nguy cơ  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: \["Thấp", "Trung bình", "Cao", "Rất cao"\]  
Validation Rule: BR-010  
Behavior: Hiển thị văn bản phân loại nguy cơ (ví dụ: "Trung bình"), nằm bên dưới Component 4.20.2. Nội dung văn bản được xác định bởi BR-010.  
Component 4.21: Nhận xét nguy cơ biến chứng  
Type: Card  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: Nội dung do AI tạo ra.  
Available Value: N/A  
Validation Rule: BR-005, BR-007, BR-010  
Behavior: Hiển thị giải thích chi tiết về mức độ nguy cơ. Nội dung AI tạo ra phải dựa trên phân loại nguy cơ (Thấp, Trung bình, Cao, Rất cao) được xác định bởi BR-010.

Component 4.22: Miễn trừ trách nhiệm Nguy cơ biến chứng  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: "Kết quả này được phân tích dựa trên các thang điểm dự đoán nguy cơ tim mạch (SCORE2, SCORE OP, SCORE Diabetes và ASCVD), không thay thế chỉ định y khoa."  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: Hiển thị tĩnh bên dưới mục Đánh giá nguy cơ biến chứng.

\-- MỤC "TỔNG HỢP TRIỆU CHỨNG" \--  
Component 4.23: Tiêu đề mục  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: "Tổng hợp triệu chứng"  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: N/A

Component 4.24: Danh sách triệu chứng  
Type: List View  
Data Type: Array  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: \- Empty: Hiển thị văn bản "Không có dữ liệu"  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: Hiển thị danh sách các triệu chứng được ghi nhận trong kỳ. Mỗi item bao gồm tên triệu chứng và số lần xuất hiện.

Component 4.25: Nhận xét triệu chứng  
Type: Card  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: Nội dung do AI tạo ra.  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: Hiển thị phân tích về các triệu chứng nổi bật.

\-- MỤC "BÁO CÁO TUÂN THỦ DÙNG THUỐC" \--  
Component 4.26: Tiêu đề mục  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: "Báo cáo tuân thủ dùng thuốc"  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: N/A

Component 4.27: Tỷ lệ tuân thủ dùng thuốc  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: "Tỷ lệ tuân thủ"  
Placeholder: N/A  
Default State: Visible  
Available State: \- No Data: Hiển thị "Không có dữ liệu"  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: Hiển thị giá trị %.

Component 4.28: Thanh tiến trình tuân thủ thuốc  
Type: Progress Bar  
Data Type: Number  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: \- Hidden (khi không có dữ liệu)  
Default Value: N/A  
Available Value: 0-100  
Validation Rule: BR-005, BR-007  
Behavior: N/A

Component 4.29: Nhận xét tuân thủ thuốc  
Type: Card  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: Nội dung do AI tạo ra.  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: Hiển thị nhận xét, khen ngợi hoặc nhắc nhở về việc tuân thủ.

\-- MỤC "PHÂN TÍCH LỐI SỐNG" \--  
Component 4.30: Tiêu đề mục  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: "Phân tích lối sống"  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: N/A

Component 4.31: Các chỉ số lối sống  
Type: Custom View  
Data Type: Object  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: \- No Data: Hiển thị "Không có dữ liệu"  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: Hiển thị các cặp (Nhãn: Giá trị) cho các chỉ số như "Giấc ngủ trung bình", "Số bước chân trung bình".

Component 4.32: Nhận xét lối sống  
Type: Card  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: Nội dung do AI tạo ra.  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: Hiển thị nhận xét về ảnh hưởng của lối sống đến sức khỏe.

\-- MỤC "KẾT LUẬN" \--

Component 4.33: Thẻ Kết luận và Lời khuyên  
Type: Card  
Data Type: String  
Required: N/A  
Label: N/A  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: Nội dung do AI tạo ra.  
Available Value: N/A  
Validation Rule: BR-005, BR-007  
Behavior: Hiển thị lời khuyên, động viên và mục tiêu cho kỳ tới.

\-- CÁC NÚT CHỨC NĂNG \--

**Component 4.34: Kolia tư vấn** \- Tham chiếu đến [tài liệu Common](https://docs.google.com/document/d/1KBY8RFNa2_HSTCNG-H_pesqSfkCHRSanbpHb-qx_yu0/edit?usp=sharing) (Component 8.4: Kolia tư vấn).

Component 4.35: Nút "Chia sẻ báo cáo"  
Type: Button  
Data Type: N/A  
Required: N/A  
Label: "Chia sẻ báo cáo"  
Placeholder: N/A  
Default State: Enabled  
Available State: \- Active (khi nhấn)  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-009  
Behavior: Khi nhấn, tạo file PDF và mở menu chia sẻ của hệ điều hành.

**Component 4.36: Nút "Về trang chủ"**

* **Type:** Button  
* **Data Type:** N/A  
* **Required:** N/A  
* **Label:** "Về trang chủ"  
* **Placeholder:** N/A  
* **Default State:** Enabled  
* **Available State:** Enabled, Active (khi nhấn)  
* **Default Value:** N/A  
* **Available Value:** N/A  
* **Validation Rule:** N/A  
* **Behavior:** Nhấn để đóng màn hình chi tiết báo cáo định kỳ, điều hướng đến màn hình chính.

Component 4.37: Miễn trừ trách nhiệm  
Type: Text Label  
Data Type: String  
Required: N/A  
Label: "Lưu ý: Báo cáo này được tạo ra dựa trên dữ liệu do người dùng cung cấp và chỉ mang tính chất tham khảo, không thay thế cho chẩn đoán, tư vấn hay điều trị y tế chuyên nghiệp. Vui lòng tham khảo ý kiến bác sĩ hoặc chuyên gia y tế có trình độ để được tư vấn cụ thể về tình trạng sức khỏe của bạn."  
Placeholder: N/A  
Default State: Visible  
Available State: N/A  
Default Value: N/A  
Available Value: N/A  
Validation Rule: BR-005  
Behavior: Luôn hiển thị ở cuối màn hình.

# **PHẦN 5: NON-FUNCTIONAL REQUIREMENTS** 

## **5.1 Performance Requirements (Yêu cầu về hiệu năng)** 

Requirement ID: NFR-P001 

Description: Màn hình "Tiêu điểm ngày" phải được tải đầy đủ trong vòng dưới 2 giây. 

Requirement ID: NFR-P002 

Description: Màn hình "Chi tiết báo cáo định kỳ" phải được tải và hiển thị đầy đủ trong vòng dưới 3 giây. 

Requirement ID: NFR-P003 

Description: Chức năng "Chia sẻ báo cáo" phải hoàn tất việc tạo file PDF trong vòng dưới 5 giây. 

Requirement ID: NFR-P004 Description: Thao tác chuyển đổi giữa các tab "Tiêu điểm ngày" và "Báo cáo định kỳ" phải có phản hồi tức thì (dưới 0.5 giây).

## **5.2 Security Requirements (Yêu cầu về bảo mật)** 

Requirement ID: NFR-S001 

Description: Toàn bộ dữ liệu sức khỏe và thông tin cá nhân của người dùng phải được mã hóa khi lưu trữ (at-rest) và khi truyền tải (in-transit). 

Requirement ID: NFR-S002 

Description: Chức năng chia sẻ báo cáo phải đảm bảo file PDF được tạo ra an toàn, không chứa các siêu dữ liệu ẩn có thể làm lộ thông tin người dùng.

## **5.3 Usability Requirements (Yêu cầu về trải nghiệm người dùng)** 

Requirement ID: NFR-U001 

Description: Ứng dụng phải xử lý được tình trạng mất kết nối mạng khi tải báo cáo theo quy tắc GR-CON-01, hiển thị thông báo rõ ràng và cho phép thử lại. 

Requirement ID: NFR-U002 Description: Giao diện cho các trạng thái "không có dữ liệu" phải rõ ràng, cung cấp thông tin hữu ích và mang tính khuyến khích người dùng theo đúng định nghĩa tại BR-006 và BR-007. 

Requirement ID: NFR-U003 

Description: Các biểu đồ, đồ thị trong báo cáo phải dễ đọc, có chú thích rõ ràng và hiển thị tốt trên nhiều kích thước màn hình khác nhau.

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAgkAAACSCAYAAADPXFlRAAAapElEQVR4Xu3deZtUxd3G8byHRFlcYdQxKosREwERRCD4oCCLLILKLiKgBAlqBgNcosE4YADBIF5ohAQTREE0CoLRiAQlopFNiYSYF3Ie7sJqa6rqdJ+eXma6+f7xuaBP1enu6TrL79T6gx/+8EcJAACA7wf+BgAAACFIAAAAUQQJAAAgiiABAABEESQAAIAoggQAABBFkAAAAKIIEgAAQBRBAgAAiCJIAAAAUQQJAAAgiiABAABEESQAAIAoggQAABBFkAAAAKIIEgAAQBRBAgAAiCJIAAAAUQQJAAAgiiABAABEESQAAIAoggQAABBFkAAAAKIIEgAAQBRBAgAAiCJIAAAAUQQJAAAgiiABAABEESQAAIAoggQAABBFkAAAAKIIEgAAQBRBAgAAiCJIAAAAUQQJAKLGjB6TNDUtThYvftz8O3fu3CDP2LHjkkceeTRZsGBBMm/eg7l//Xzlct555wfbAFQOQQKAqOVPLE/ef//95H//+1+On+exxx5LDh48mEs/dOhQsm7d+iBfOTQ1NSWHDx8OtgOoHIIEAKmam1cmq1evTt59910TBDQ2Xhnksfn8beXwxRdfJG+88UayYsUK8/nHjh0L8gCoHIIEAKk++OCDZNKkScnkyZPNTVpP834e2bdvX7Ct3AgSgOojSACQ6ttvv00aGxuTTp06J//617+Szz//POnQoWOLPJde2sXk8/ctN4IEoPoIEgCkWrlyVe7/V111tblRv/nmmy3yPPnkU8nGjRuDfcuNIAGoPoIEAKkmTLirxWvbQbFPn765bbt3707uu29WsG+5ESQA1UeQACDq8suvSK64orHFNhskrF69xry2TQ3XXdcr2L/cCBKA6iNIABDV3NwcbJsxY0YuUNDr3/zmN8mGDRuCfNbIkaOSO+8cm1m+eRD0mSdOnAi2A6gcggQAURrZ4G+74IILk6NHj5obtm7oe/fuPRM4zAzySZcuXZPXX3/d9GHISv0e/PexCBKA6iNIABBQM4OtLfBpkiWlTZ06zTQ19Ox5bZCnEvSZX331VbAdQOUQJAAITJw4Mdm/f3+wXbp372GCg+PHj5sZFv30SiFIAKqPIAEoA1XDL1y4MNheizp3viD59NNPU5sRZNiwYeamPW3a9CCtUvR5J0+eDLYDqByCBKAEF154UTJr1qzk448/TjZv3hyk15qBA29J3nnnHXND1iyKvXpdH+SRH/3oPJOnR4+eQVo59e8/IBk69NZk1KjR5vP++9//JnPmzD0TpNyWNDRcFuQHUF4ECUCRhgwZkkyfPj3ZtOklMyTP9vav9SBBwxm//vprU6Uv+r87mZJPiz/528pNTR76Luos+eWXXxpHjhwxv7tWoPTzAygvggSgSFrHQDp27GReawGieggSAMBHkACUiCABQL0iSABKRJAAoF4RJAAlIkgAUK8IEoASESQAqFcECUCJCBIA1CuCBKBEBAkA6hVBAlCi74OELUEaANQyggSgRDZI2LKFIAFAfSFIAEpkg4Q//vGPQVotuuGG3slf/vKX5LXXtic7duw4Y2eyc+dOs5Tzrl27jLfeeus7b+e8/XblrFjxdPA9AVQeQQJQIhsk/OlPfwrSatH48RNyU023F1qzwf+eACqPIAEokQ0Stm7dGqTVqmuv/YlZM8G/WWv1Rz9vOU2ZMtX07Tj1zTfBZ2ulTT8/gMoiSABK9H2Q8GqQVsvuvXdycKP+/PPPk8svvyLIW24XX3xJMnfu3BafnW/pagCVQZAAlMgGCa++Wl9BgvhBgg2GtFS0n7cSFi5cmJw+fdp8bjVWnQTQEkECUCIbJKizn59W6/r1uyn5z3/+EwQK2ubnraTGxkbzuZs2bQrSAFQOQQJQAlWL6wlXN7D33nvPvPbz1Lr58+cHQYJU+289euSoqVX48Y+vCtIKqZdOpUA+6s+zYMHDwfZSECQU0KFDR9Mh7dJLuwRpODfpJNSwvL/97W9B575///vfyUcffWSGBM6ePTvYtxapaUFNDH6QsGHDhiBvJY0bN8587uOPPx6kFaK+FP42oN58/PHHycaNG4PtpSBIKOChh84+RfXr1y9IS9O7d+9kzpy5ybx5DyYPPvhQjl6rM9YDD8wxnbDUk3vMmDuD/V3XXdcrmTZtejJp0t3JhAl3meFp+levtX9Dw2XBPta8efPMjersZ01Jpk6dlsyceZ/h50V2K1euSr7++mtz4/nnP/+ZHDp0KEevtV3py5YtC/atVeqsqL/LDxR0DPp5K2n9+ueTL7/8suiRDlmDhGHDbjPnqH/uuuewziud3/fff38yffr0ZPDgIcH75DNr1ixzDYh9jr0+6L11nuo81/XEfw+0XtYytuVQahn77++Wsa7J5SxjgoQqe+6551p1MezTp++Zm/n4ZOnSZbn9P/30U3NQ3H33Pcldd008c+OekSxa9EiyadNLuTwHDvwjGTRocIv3UnBy332zzGQ2Nt/Ro0fN09TkyZODz3YtX/5kcvLkSbOPnnCff/55c/APHHhLkBfIwg8SRM0snTp1DvK2J1mDhFtv/T8TiGtkx4svvpj7GzVR1j333Hvmgj4pF6TrRqDqXZvniy++OHNuDQze06caEV0HYteHiRMnmuuD0nXN+fvf/57Ls3///uSqq64O3g/FccvYPY79MtaDVaXL+Je//GVZy/jAgQMECdUyYMDNybfffpsrvNa084wYcUdu/8ceeyxIt2zHN0mbNGbkyFG5PC+99HKQnmbdunVmn27dugdpQLH++te/5o5DV3ufETFrkOBqamrK/X0//enPgnRLNX02n2qTunZtCPLEuNeHRx9Nvz4MHXprcuzYMZNP/V+KrUVBOvcYrocy1oMmQUIVqA32nXfeaXEA6ancz1eInvbt/vmqq9SD3P2s8847P8jzs5/dkEvXd/PTY9QUoVoHHdR+GtAaPXr0TE6cONHieLX8vO1Ja4KEP//5z+bvyrKv+zto2KafHpP1+iB6T5tXtZB+OlrH/qb1UsYECVWiKiXdWDXrnC00XTD8fIXYqn7x01wdO3YyNQg279ix44I8ot7dSlcNh/bx033Kx8qEqIS1a9e2uGjK66+/Hg1w24MsNwFX37435v4uNff56T73d1izZm2Q7lOHaHt90BoZfrpPbdj2/ffu3Ruko3j1WMb/+AdBQlWokNSmpAuebXJQu6ufrxD3oPLTXG4tgaipw88j+g42j57o/HTX+ed3MAfoNdd0C9KAUl144UUtjlnrkUceDfK2B8UGCeq8Zv+mn/zkuiDd5/4Gau/2033qF2Tz56uGtn7729/m8mvRLT8dxavHMj548CBBQqX16nV98tq213KvbY/uzz77LMhbiHtQ+WkudSZ086bNZrd58+Zcnp//fGiQ7vrFL37Rqn4UQFax9RVUI3bLLYOCvG2t2CDh5Zdfznze24meRE0xXbp0DfL43KrlQtXQ4j4g6Nz201G8eixjgoQq0Kx511//09xrjYVXoWmGubSbdxpb4BoO56e5VEVk84qfbj399PeRZr6RDVdffY35TFV3+WlAufhrK1iffPJJkLetFRMk6Dw/cuSI+VsKzQWhGhXNmWH/dvWK9/PEuPNOFBoZomHQNu+pU6eSyy67PMiD4lSzjDWyrFplrHOPIKFCOnfubG7W/sVE08DawlNB+vulUZOB3S9fJxeNt1YePYEtWLAgSHdp2Ix9z2effTZIlzGjx5j01avXBGlAuTU0NJgnMXtcWu1tLg7/vM7HnpOifkl+uigAd0d6FDOs2L02iJ/uuvnmm3P9lTQk209H62QpYw1VLEcZF2qCK2cZa5glQUKFqCBVSP58CJo4xxb2kCGFq4yshx/+vqrJH1er6WxVnbRnzx6Tvm3btkyTNel97HvGVhxUxKuDRJPN6OLtp7eGOkjedFP/skk7IVG71PTlDhcWPT25NXJtrZggQUOM7d+huUwsDWNualps2o71fmpu0dh63Uz898jHvTaIn+6yHd9Uk9leO4XWIlvGempPK2OTXoYyztf8pg6T5SxjgoQKUkFpKl2/SWHJkiW5wtYESf5+adzqRF0w1Y6lf92LqbatW7c+2DeN5qy3+37wwQdB+vInlps0P9AphYbi2M8sB/3O1Z7zH5XnDvWy9u1739TQ+XnbQtYgQee/gmz7N+icVdOd65szNw6dx+q7NHv2A0WvJeFeG/QEqTHyQ4b83Bg+fLjpFKeblCbGUR5NtqNh0v77oHXcMlY5ppWx0stRxprjJq2MbZ5ylbFG5REkVIAK7ne/+12wXXTDtQWpCNNPj1H1kd1HEaWfLjow7UXCT8vHvq+460nowFdUrI6X/j5ANWhODvf4tEaNGh3krbasQYLfz8JPd91xx8hcvsWLs68n4b6/Fp7SU6qdhe/OO8eam0r//gNSnyo1/NTWQurp10+vFE0udfjw4WB7rXHLuFDNZjnK2JZvrIz9/Sx3iHExZUyQUAE6EfXE07Nnz+Siiy42M12pk4l07nyB6aRiC0tND/7+MZpq0+6jgMFPlyeeeCKXJ+1iEOMefO5832oD/vWvfx3kB6pF83u4x6elpzY/b7VlDRL+8Ic/5L53lhuinS5dT6RZmgzF/W2Krca2dK3S/sU0gbaGak/VNGpvWpoV0M9TjNtvH27er1QabeC/d1ZuGftpMaWWsZ+Wld2/mDImSKgAtwNLIRoy4+8fY2dqyzfCYPTo0bn3TZsXIcb9PvYJTYvv6ClOQY2fv5745YHs/N+yUpqbm4PPrubnp8kaJNgJyyTLxfbJJ5/K5V+0aFGQHuP+Lq292WmRIrWXt6Y5R6OflixZGmyP0cRymjZ+xYoV5vuWGiTs3r07ODZaQ2sq+O+dlVvGflpMqWXsp2WlfYstYy0wl+W4LcY5HSRomIkOel1AdCLEvPnmm7nC3rVrV/AePgUFCg6UX8Mp/XTLHalQzJLC7sGntjJt+/3vf1/SwQiUiy5o+/bta3Gcav0QP1+1ZQ0S3O+txXj8dJ9W+izm79T1weZXO7SfnpVu8q2dcEe99GN9mgrRdy41SFDnagVGpfL7jhXDLWM/Laatylj7F1vGBAllpJ72qj7KUjtgC/yrr74K0nyaWcvmz9er9d13383lU0cWPz2Ne4DrYNDSoMePHzcnjp+3HLToiaZ2LpcXXthIx8U6p5E1Oj7VjNdeyrrYIEFNJIVuRGomtJOtSb42Zsu9PmSZtS9Gv+np06fNaoZ+Whaqvm6rIKE9cMvYT/O1ZRlr/2LLmCChjLRIknqwdu/eI0jz2QIXP82n+ett3nzrK7ijHLIceJb7XTQaQ/9meeJpLQUwH330UdkoMtbThP85qA/qy7Njx07TNlrKkrflliVI0A3BnltZHh7UNm7z7969x0yF7ufx2euDzv/WTpijc1Lv4TYvPvPMM2b426pVqwoGN+qofa4GCbVUxuqInlbGfn6LIKGMVIhZe6vag0T8NJcK1J2q1k9Pe0+/h22+jozufqrZ0Exg+fID1aKbk2av07HpdqptD7IECe6oJPWA99N9dpicFFpLRdzrg5YD9tOzstXf9vWUKVPMJGoaSaUbU6E+TudykFBMGffq1atNy1gdJu1rv4z9/BZBQolUJa8OLyp43WCzLH7kL2Tjp7s050HWvG6+nj2vzW3XeNx8cye483sX+gygmuwxqQuan9bWCgUJOs/tsEJ11os9jSsYV3u+nuhsTaCmbb/xxsI93rWve31o7VwmGtWgpga9h4bGKShTG/j06dPNNvWbKvTQUEqQoKZNf3utKLaMbVm1VRmrc2paGfv7WAQJJdA627bwLJ3oehL3I0QFE2+99Vayf//+YBEbvY+qnTRmWHk13FFNFx9++GHw/tqmaT01fMj/Pm4vX42b1TYdHFu2bMnbBGIXJRFNI+2nA21BQ9t0TGrGOj+tPUgLEtavf940g+nm514X1OFMAbmuD6Lz2M71by1f/mTBOfl/9atfmX11U3L31aRi+gxdO/x98rG/s6xY8XSLG53fL0k1lLq2+DS7rJqD/O2ip9W0IEOfqQng/O3tna61aWWsvmFpZaw8WctY1/q0MtZcGP4++dgy3r59e8Ey9hEklECTF6mqTMNfRK8VrWkkgv/D33bb7bmZuHRg2X10gmjqTKXZyZd0YOlgUM2EhiHqIDP5j579DOWNzcd9ySWXmohQB4O+hzr1KQBRO5Sf1+UOx1Gk6aefa1S1qlU0H3zwoRwtAWtHfqTRPpoSVdG+OhdpvPq9905Opk2bnnqRRFzv3n3M8b9mzdogrb2IBQm6+Ot76/zTeer2E3LZNJ2buug3N6/M3CFNNx9dY8x15Lvrg64jumbo/fJVHccsXfp9T3tdP/SkqWuJn090Hmh0lk/V4Lo2+dtF/Uk0RNJ/L9Fn1lqQoDLWg15ryjhrfwKVsY6jtDJ2VxXOopgy9hEk1BlN3DRmzJ2mdkDBhqqqCi0ipfyq/tIUzH7auUgXNf+Et/y8Lj+vq1aDhK1bt6Ze4CtFn2cXeMrSqautxIKEWmQ7K6vN2g7PzrLUsauU5oYsI7xQGlvGgwYNLrqMCRKAPOxFzN7sVVvg5/Gp5kBPDu2pJ34hmjxLM+GpNkvV1W6A07fvjUH+Snntte3mM9Xj+sorfxyktyf1ECQMGzbM/N7uBDu2DVz/V7u1nmLzNVdKKUFCoWXvURq3jO22WBn7+1kECUAeOpFs5x5Rn5JY5ySXAonJkycH29uzESNG5P5G3fzUR6YtggR9nqpYNZeGn9be1EOQoH5Q+s3dCXZeeeWV3A1Ebdl6CvX385USJKgK3d+O8im1jAkSgDw++eQT868m8bE3TZ1Ufj6XTqhqV9GXSh1t1ffiiivO9qXRUs3VDhK0TojaW7W6nZ9WSV27Npie5mqq89PyqYcgQW3bKmPbaVrsKq1q6lHbeJa+EsUECZrDRWWsKeD1OVqQTlPZqz9UQ8NlQX6UptQyJkgAUqivhq0R0A3Erkiozkj+6BVL222EXsuqGSRoVTzdKNrid9ONSZ/77LPPBmmF1EOQ0K1bd8PfLsUEusUECaiuUsuYIAFIoQVo3JNIQ5fsjVP/9/OLXQbc315rqhkk2HVJWnOjLpVubPpsjWP30wqphyChXDRd/N69e4PtqH0ECUAK/6JnawlEtQp+ftHQVIKE7OxvqnHf1R4BognH9Nlaq8RPy4IgoaUuXboG21D7CBKACLVTx8ab2xtnWiBw8OBB07nR315rqhEkaNEmTUijiWmqvfaG2sTt8r6tnaxJc2D424B6c/fd9xSclrtYBAmoeXate3+7hjbam6fGHLtpmjpY2ydNmhTsV2sqGSSoxuCll87O8plWI1MJGsanzpFuoKc5Mfx8ACqLIAE1T00NBw4cCLY/8MCc3A3Gr4LTuvDa3th4ZbBfrXGDhCxzzBfjqafOzvCpcdtaYthPLzfNfLlt27bozHia08LPD6CyCBJQ02xTw+rVa4I0rcluJ1fSdNruhD+aAEg1Df4+taiSQYJ9X83wqVoKre4oN9wQZ9M1VbP06dPX7NevX78zbjJD6gYPHpKMGHGHqc2ZP3++mc5ZK97ZESlpVJ7+9wNQWQQJqGm2qSFteJCmubZPpeq8phnLtF2vJ0y4K8hfDM3BoPXmS+WvHVIsN0jQjdhPbw29jx3J0F743xFA5REkoKbt27ev4GqYr776au5GY/sg6P92MqLWclfyLIWWL/ffuxhukHDTTf2D9GJpnLa/ol1bU82P/z0BVB5BAmqWetyrliC2yqZr5MhRuZuNlgDXtnJMJqNe/qoFKFWhqaMLcYMEVef76cXS2hAaDTB16jQz29vMmfeZFTPl/vvvN2bPnv2dB3LUByTN2Txn97HvIQqQ7HuLPktmzJj5nRmGJgDyvyeAyiNIQM0aN26cuTFqUiQ/zaUe+u5TqTrHNTc3B/lqVbmDBACwCBJQsz788MPk0KFDwfYYLUzjBgpZ14qvBW6QcPPN5R0jDeDcRpCAmqWb4gsvZJtdbNWqVS2CBD+9lrlBwsCBA4N0AGgtggTULN0U586dG2yP0fC8cyNIKH5dAwBIQ5CAmqJplP2JdvQ6S+/3sWPP9mGITeFcSzQ3hNaU37Nnj1ke2/0t5PDhwyZdOnbsFOwPAFkRJKBmaBSAJkc6ceKEmXhH8/kfO3bMjOfPcuNXB0YtELR169YgrZZo6Obp06fNvA+fffaZ6Zfh0jb9LlrSuXPnzsH+AJAVQQIAAIgiSACQl+YtaG5embz44otJU9PiIL2Sqr0kNYCWCBIAFHTRRReb/g6VXuRp/PjxZqrqtWvXmqYlNZv4eQBUD0ECgIKGDbvNBAmV7uOg6aDfeOMNsybH5s1bCBKANkaQAKCgJUuWVn3o6KJFiwgSgDZGkAAgLy3RrNEUBAnAuYcgAUBew4cPNwHCqVOnctt69+5t5qbQTJalLlCVhiABaHsECQDyWrZsmQkSdu7caV5PmTIlee+995KHH15o5qcYMKAy60UQJABtjyABQCqNarBNDeq8uGHDhqRDh44mTdt27dqVG6aovD179kzVo0fPpHv3Hkm3bt2Ta67pllx99TWG/5mWgoTjx48H2wFUD0ECgFS33362qUG2b9/eommhsbExyF9OChI0u6a/HUD1ECQASLV06dmmBmvRokeSSy65NMhXCQQJQNsjSACQSotEKThQv4RBgwab/2ttiHzNBOWiIEETKvnbAVQPQQKAVGZUwzff5CZRWrduvdn2zDPPmL4JR44cMf0MlNa3743JjBkzi9apU3yCJgUJWrzL3w6geggSAKRSQLBjx47c61deecVse+ih+aa/gmoa/H3KRUHCyZMng+0AqocgAUAqBQRNTU251zNmzDDbZs+enbz99tvJ+PETgn1K0b//gGTo0FuTUaNGm+mZtdz1nDlzzciKhobLgvwAKosgAUAqDVf0t0k1+iQAaHsECQAAIIogAQAARBEkAACAKIIEAAAQRZAAAACiCBIAAEAUQQIAAIgiSAAAAFEECQAAIIogAQAARBEkAACAKIIEAAAQRZAAAACiCBIAAEAUQQIAAIgiSAAAAFEECQAAIIogAQAARBEkAACAKIIEAAAQRZAAAACiCBIAAEDU/wPJrtr3+RyPsAAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,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>

[image5]: <data:image/png;base64,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>