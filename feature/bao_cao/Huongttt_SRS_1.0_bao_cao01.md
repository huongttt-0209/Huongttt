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
    
  Chỉ cần tâm trương hoặc tâm thu \>140/90 thì lần đo đó được coi là vượt ngưỡng 140/90 mmHG  
  **Bước 2**: **\[Nhận xét tần suất vượt ngưỡng\]** lồng ghép **\[Lý giải áp lực lên thành mạch và nguy cơ quá tải hệ tim mạch\]**.  
  BP\\ Load \= \\left( \\frac{\\text{Số lần đo vượt ngưỡng}}{\\text{Tổng số lần đo}} \\right) \\times 100\\%  
  **Dưới 15% \- Bình thường:** Hệ tim mạch đang được bảo vệ tốt.  
  **15% \- 30% \- Chớm cao:** Bắt đầu có dấu hiệu quá tải, cần điều chỉnh lối sống.  
  **Trên 30% \- Gánh nặng lớn lên hệ tim mạch:** Nguy cơ cao gây tổn thương tim, thận. Cần can thiệp y tế.  
* Nhận xét về tần suất huyết áp thấp *(Lưu ý: chỉ hiển thị cho người có tình trạng HA “Huyết áp thấp”)*  
  **Bước** 1: Tính toán Hypotension Load theo công thức:   
  Hypotension\\ Load \= \\left( \\frac{\\text{Số lần đo} \< 90/60\\ \\text{mmHg}}{\\text{Tổng số lần đo}} \\right) \\times 100\\%  
  Chỉ cần tâm trương hoặc tâm thu \<90/60 thì lần đo đó được coi là \<90/60 mmHg  
  **Bước** 2: **\[Nhận xét tần suất\]** kết hợp **\[Lý giải nguy cơ thiếu máu/oxy tương ứng\]**.  
  **Mức 1 (Ít khi thấp):** Gánh nặng \< 15%.  
  **Mức 2 (Thường xuyên thấp):** Gánh nặng 15% \- 30%.  
  **Mức 3 (Rủi ro tụt huyết áp):** Gánh nặng \> 30%  
* Nhận xét về sự ổn định của huyết áp   
  **Bước 1**: Tính toán ARV tâm thu theo công thức  
  ARV \= \\frac{1}{N-1} \\sum\_{k=1}^{N-1} |BP\_{k+1} \- BP\_k|  
  \\begin{itemize}  
      \\item n: Tổng số lần đo trong giai đoạn theo dõi.  
      \\item BP\_i: Giá trị huyết áp của lần đo thứ i.  
      \\item |BP\_{i+1} \- BP\_i|: Chênh lệch giữa lần đo sau và lần đo trước đó.  
  \\end{itemize}  
    
  Khoảng cách tối đa giữa 2 lần đo liên tiếp là 24h, nếu \<24h, bỏ qua cặp giá trị .  
  **Bước 2**: Diễn giải chỉ số và đưa ra nhận xét về độ ổn định của chỉ số HA  
  \< 10 \- Ổn định: Hệ mạch vận hành êm ái, ít áp lực cơ học  
  10 – 14 \- Biến động: Mạch máu bắt đầu chịu áp lực từ sự dao động.  
  \> 14 \- Bất ổn: Nguy cơ cao tổn thương thành mạch và cơ quan đích.  
* **Nhận xét về nhịp sinh học của huyết áp**  
  **Bước** 1: Tính toán chỉ số ME difference (tâm thu)  
  ME\_{diff} \= \\text{HATT}\_{\\text{Sáng trung bình}} \- \\text{HATT}\_{\\text{Tối trung bình}}  
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

  **\*Điều kiện dữ liệu tối thiểu (Data Sufficiency)**

  Hệ thống chỉ thực hiện các phân tích chuyên sâu khi đạt điều kiện:

  | *Loại báo cáo* | *Quy định về dữ liệu* |
  | :---- | :---- |
  | ***Báo cáo Tuần*** | ***>= 3 ngày có lượt đo tối thiểu (>=2 lần đo/ngày)*** |
  | ***Báo cáo Tháng*** | ***>= 14 ngày có lượt đo tối thiểu (>=2 lần đo/ngày)*** |

  * **Xử lý khi không đủ dữ liệu:** Ẩn các nhận xét chuyên sâu. Hiển thị thông điệp tương ứng với loại báo cáo:
    * **Báo cáo Tuần:** *"Tuần này bạn chưa đủ dữ liệu để Kolia phân tích chuyên sâu. Hãy đo huyết áp ít nhất 2 lần/ngày (tốt nhất nên đo vào sáng và tối) trong tối thiểu 3 ngày mỗi tuần để nhận được phân tích tối ưu nhất."*
    * **Báo cáo Tháng:** *"Tháng này bạn chưa đủ dữ liệu để Kolia phân tích chuyên sâu. Hãy đo huyết áp ít nhất 2 lần/ngày (tốt nhất nên đo vào sáng và tối) trong tối thiểu 14 ngày mỗi tháng để nhận được phân tích tối ưu nhất."*

  **Các nhận xét chuyên sâu (khi đủ điều kiện dữ liệu):**

  * **Nhận xét về mức độ kiểm soát huyết áp** *(Lưu ý: chỉ hiển thị cho người có tình trạng HA "Bác sĩ đã chẩn đoán bị bệnh Tăng huyết áp")*  
    **Bước 1**: Tính Phần trăm số lần đo nằm trong khoảng mục tiêu \- tức là cả tâm thu và tâm trương đều nằm trong ngưỡng mục tiêu \= Số lần đo trong ngưỡng mục tiêu/Tổng số lần đo\*100%  
    **Bước 2**: Diễn giải và đánh giá lâm sàng mức độ kiểm soát huyết áp dựa trên phân loại  
    **\> 70% \- Kiểm soát tối ưu:** Huyết áp rất ổn định, đạt trạng thái lý tưởng để ngăn ngừa biến chứng tim mạch.  
    **50% – 70% \- Kiểm soát tốt:** Đạt yêu cầu điều trị. Đa số thời gian cơ thể được bảo vệ trước áp lực máu cao.  
    **25% – 50% \- Kiểm soát kém:** Huyết áp dao động nhiều. Hiệu quả của phác đồ thuốc hiện tại chưa ổn định.  
    **\< 25% \- Không được kiểm soát:** Rất ít khi huyết áp đạt đích. Nguy cơ xảy ra biến cố (đột quỵ, suy tim) ở mức cao.  

  * **Nhận xét về nguy cơ tăng huyết áp** *(Lưu ý: chỉ hiển thị cho người có tình trạng HA "Thường đo thấy chỉ số cao, nhưng chưa được chẩn đoán bệnh Tăng huyết áp", "Huyết áp bình thường", "Huyết áp không ổn định", "Không rõ/ Không theo dõi")*  
    **Bước 1**: Tính toán BP load theo công thức (ngưỡng THA: 140/90)   
    BP\ Load \= \\left( \\frac{\\text{Số lần đo vượt ngưỡng}}{\\text{Tổng số lần đo}} \\right) \\times 100\\%  
    Chỉ cần tâm trương hoặc tâm thu \>140/90 thì lần đo đó được coi là vượt ngưỡng 140/90 mmHG  
    **Bước 2**: **\[Nhận xét tần suất vượt ngưỡng\]** lồng ghép **\[Lý giải áp lực lên thành mạch và nguy cơ quá tải hệ tim mạch\]**.  
    **Dưới 15% \- Bình thường:** Hệ tim mạch đang được bảo vệ tốt.  
    **15% \- 30% \- Chớm cao:** Bắt đầu có dấu hiệu quá tải, cần điều chỉnh lối sống.  
    **Trên 30% \- Gánh nặng lớn lên hệ tim mạch:** Nguy cơ cao gây tổn thương tim, thận. Cần can thiệp y tế.  

  * **Nhận xét về tần suất huyết áp thấp** *(Lưu ý: chỉ hiển thị cho người có tình trạng HA "Huyết áp thấp")*  
    **Bước 1**: Tính toán Hypotension Load theo công thức:   
    Hypotension\ Load \= \\left( \\frac{\\text{Số lần đo} \< 90/60\\ \\text{mmHg}}{\\text{Tổng số lần đo}} \\right) \\times 100\\%  
    Chỉ cần tâm trương hoặc tâm thu \<90/60 thì lần đo đó được coi là \<90/60 mmHg  
    **Bước 2**: **\[Nhận xét tần suất\]** kết hợp **\[Lý giải nguy cơ thiếu máu/oxy tương ứng\]**.  
    **Mức 1 (Ít khi thấp):** Gánh nặng \< 15%.  
    **Mức 2 (Thường xuyên thấp):** Gánh nặng 15% \- 30%.  
    **Mức 3 (Rủi ro tụt huyết áp):** Gánh nặng \> 30%  

  * **Nhận xét về sự ổn định của huyết áp**  
    **Bước 1**: Tính toán ARV tâm thu theo công thức  
    ARV \= \\frac{1}{N-1} \\sum\_{k=1}^{N-1} |BP\_{k+1} \- BP\_k|  
    \\begin{itemize}  
        \\item n: Tổng số lần đo trong giai đoạn theo dõi.  
        \\item BP\_i: Giá trị huyết áp của lần đo thứ i.  
        \\item |BP\_{i+1} \- BP\_i|: Chênh lệch giữa lần đo sau và lần đo trước đó.  
    \\end{itemize}  
    Khoảng cách tối đa giữa 2 lần đo liên tiếp là 24h, nếu \>24h, bỏ qua cặp giá trị.  
    **Bước 2**: Diễn giải chỉ số và đưa ra nhận xét về độ ổn định của chỉ số HA  
    \< 10 \- Ổn định: Hệ mạch vận hành êm ái, ít áp lực cơ học  
    10 – 14 \- Biến động: Mạch máu bắt đầu chịu áp lực từ sự dao động.  
    \> 14 \- Bất ổn: Nguy cơ cao tổn thương thành mạch và cơ quan đích.  

  * **Nhận xét về nhịp sinh học của huyết áp**  
    **Bước 1**: Tính toán chỉ số ME difference (tâm thu)  
    ME\_{diff} \= \\text{HATT}\_{\\text{Sáng trung bình}} \- \\text{HATT}\_{\\text{Tối trung bình}}  
    Sáng: 04:00 đến 10h00  
    Tối: 20:00 đến 00h00  
    Cần tối thiểu 1 lần đo trong mỗi khoảng thời gian  
    **Bước 2**: Nhận xét về nhịp sinh học của huyết áp dựa trên các ngưỡng giá trị

  | Chỉ số MEdiff​ | Phân loại nhịp | Ý nghĩa y khoa |
  | :---- | :---- | :---- |
  | \>15 mmHg | Vọt áp buổi sáng (Morning Surge) | Áp lực máu tăng quá mức khi thức dậy, tăng nguy cơ đột quỵ sáng sớm. |
  | −15 đến 15 mmHg | Cân bằng (Balanced) | Nhịp sinh học ổn định, huyết áp sáng và tối không chênh lệch quá mức. |
  | \<−15 mmHg | Tăng áp về tối (Risky Evening) | Dấu hiệu của tình trạng "Non-dipper" (không hạ áp về đêm), rất hại cho tim và thận. |

  * **Nhận xét tương quan giữa huyết áp với kết quả uống thuốc, sự kiện ăn uống\&vận động, các nguyên nhân được ghi nhận cùng kết quả HA (nếu có)**

  | Loại sự kiện | Khung giờ lấy kết quả đo HA (Sau sự kiện) | Ý nghĩa phân tích tương quan | Giải thích cơ sở khoa học |
  | :---- | :---- | :---- | :---- |
  | **Uống thuốc HA** | **1 giờ — 8 giờ** | **Đánh giá hiệu quả thuốc** | Đây là thời gian thuốc đạt nồng độ đỉnh trong máu (Tmax), cho thấy khả năng hạ áp tốt nhất của liều thuốc. |
  | **Stress / Đau / Cảm xúc** | **0 phút — 45 phút** | **Đánh giá độ nhạy cảm tâm lý** | Phản ứng của hệ thần kinh giao cảm (phóng thích Adrenaline) làm co mạch và tăng HA diễn ra ngay lập tức. |
  | **Caffeine / Thuốc lá** | **30 phút — 2 giờ** | **Đánh giá phản ứng kích thích** | Caffeine và Nicotine gây tăng HA nhanh chóng nhưng thời gian bán thải ngắn, tác động rõ nhất trong khoảng này. |
  | **Vận động mạnh** | **30 phút — 2 giờ** | **Đánh giá đáp ứng phục hồi** | HA tăng khi tập, nhưng sau 30 phút nghỉ ngơi, một hệ tim mạch tốt sẽ thấy HA giảm nhẹ (hiệu ứng hạ áp sau tập). |
  | **Ăn mặn (Nhiều muối)** | **12 giờ — 24 giờ** | **Đánh giá tác động giữ nước** | Muối cần thời gian để thẩm thấu và giữ nước trong hệ tuần hoàn, thường gây tăng HA vào sáng ngày hôm sau. |
  | **Rượu / Bia** | **12 giờ — 24 giờ** | **Đánh giá phản ứng dội ngược** | Rượu gây giãn mạch (giảm HA) lúc mới uống, nhưng gây tăng HA mạnh vào hôm sau do hệ thần kinh bị kích thích lại. |

  * **Khuyến nghị hành động:** Đưa ra khuyến nghị về tuân thủ điều trị, điều chỉnh dinh dưỡng, vận động để cải thiện các vấn đề được nêu bên trên.

  **Phân tích xu hướng và bất thường:**
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

