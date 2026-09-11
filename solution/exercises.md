# K4 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 4 tiếng
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng `*Câu trả lời của bạn*` bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.5, 1.0 và 1.5 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> temperature càng thấp thì câu trả lời càng ngắn gọn, lặp lại, formal. temp càng cao thì model chọn nhiều từ, sáng tạo, văn vẻ. 

### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> tôi sẽ chọn temperature 0.0 vì model sẽ ít chọn từ ngữ màu mè, formal hơn

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 3 lần,
mỗi lần trung bình ~350 token đầu ra.

**Ước tính GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này? Nêu một
trường hợp GPT-4o xứng đáng với chi phí và một trường hợp nên dùng mini:**
> *Câu trả lời của bạn*

---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích blockchain là gì?"** nhưng hai system prompt khác nhau:
- "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
- "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."

**Hai phản hồi khác nhau như thế nào (độ dài, từ vựng, ví dụ)? System prompt
ảnh hưởng đến hành vi model ra sao?** (3–4 câu)
> Phản hồi từ góc độ giáo viên tiểu học sẽ có độ dài ngắn, từ vựng rất đơn giản, dễ hiểu; phản hồi của chuyên gia tài chính sẽ dài hơn, dày đặc thuật ngữ chuyên ngành. Ảnh hưởng của system prompt: System prompt điều chỉnh hành vi của mô hình, thiết lập khung ngữ cảnh, phong cách giao tiếp và mức độ chuyên môn. nó kiểm soát cách mô hình lựa chọn từ vựng, cấu trúc câu.

### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~100 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Vì sao tiếng Việt thường tốn
nhiều token hơn tiếng Anh cùng độ dài?**
> tiếng việt tốn token hơn tiếng anh vì mỗi chữ cái gồm các dấu, trong khi tiếng anh thì không có dấu. hai con số chênh nhau khoảng 20%

---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì
non-streaming lại phù hợp hơn?** (1 đoạn văn)
> streaming cần thiết khi cần xử lý tức thì - low latency, ví dụ như voice AI chăm sóc khách hàng. non-streaming cần dùng khi xử lý lượng lớn context window, xử lý các vấn đề phức tạp, cần suy luận, cần độ chính xác cao.

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**So với delay cố định (ví dụ luôn chờ 1 giây), exponential backoff có lợi
thế gì khi API bị quá tải? Điều gì xảy ra nếu hàng nghìn client cùng retry
với delay cố định giống nhau?**
> exponential backoff giúp giảm áp lực lên server khi có quá nhiều lượt truy cập/ calling/ requesting. Lợi thế so với delay cố định: Delay cố định giữ nguyên nhịp độ request dày đặc liên tục, dễ khiến server tiếp tục kiệt sức. Hậu quả khi hàng nghìn client cùng retry với delay cố định: Gây ra hiệu ứng Thundering Herd.

---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Bạn chọn persona gì cho trợ lý của mình? Viết lại system prompt đó và giải
thích 1–2 lựa chọn từ ngữ quan trọng trong prompt (ví dụ: vì sao yêu cầu
"trả lời ngắn gọn", vì sao chỉ định ngôn ngữ...):**
> thiết kế persona tùy thuộc theo yêu cầu của bài toán/ doanh nghiệp/ ngữ cảnh thực tế để đưa ra câu trả lời tối ưu nhất. để có một câu trả lời sát với kỳ vọng, phải điều chỉnh theo nhu cầu người dùng.

### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn hiện có hạn chế lớn nhất là gì (ví dụ: history chỉ 3 lượt,
không có bộ nhớ dài hạn, không kiểm duyệt nội dung...)? Đề xuất một cải
thiện cụ thể và mô tả ngắn cách triển khai:**
> Đề xuất cải thiện: Tích hợp Cơ chế quản lý Context cục bộ (Local Context Persistence) lưu trữ vào tệp ẩn (ví dụ: .assistant_history.json hoặc SQLite) ngay tại thư mục gốc của dự án. Cách triển khai: Mỗi khi người dùng gõ lệnh, hệ thống tự động tải $N$ lượt hội thoại gần nhất hoặc tóm tắt trạng thái hiện tại từ file lưu trữ cục bộ vào system prompt; Sử dụng cơ chế trượt cửa sổ (Sliding Window) kết hợp lưu trữ Vectornhỏ (hoặc file JSON gọn nhẹ) để tự động nén các đoạn chat cũ, giữ kích thước payload tối ưu và bảo mật tuyệt đối dữ liệu trên máy cá nhân.

---

## Danh Sách Kiểm Tra Nộp Bài

- [ ] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [ ] Cả 4 checkpoint pytest đều pass
- [ ] Tất cả 9 câu trong file này đã được trả lời
- [ ] Đã copy bài làm vào folder `solution/`, push lên fork và dán link trên trang bài Lab ở VLearn trước 23:59 ngày 11/09/2026
