# Danh Sách Công Việc: Phục Dựng Chân Dung Lịch Sử Bác Hồ (1910) Đăm Chiêu & Chân Thực Cho Hồi 0

## Giai Đoạn 1: Lập Kế Hoạch & Thiết Kế Tạo Hình Nghệ Thuật
- [x] 1. Phân tích nguyên nhân sai lệch nhân trắc học & thần thái trong ảnh cũ `prologue_2_nguyen_tat_thanh.jpg` <!-- id: 80 -->
- [x] 2. Đối chiếu ảnh tư liệu gốc cực nét `reference_nguyen_ai_quoc_1921.jpg` để xác định cấu trúc giải phẫu (trán cao, mắt sâu sáng quắc, gò má, cằm thanh nghị) <!-- id: 81 -->
- [x] 3. Tạo kế hoạch triển khai chi tiết `implementation_plan_authentic_portrait_prologue_2.md` và trình người dùng phê duyệt <!-- id: 82 -->

## Giai Đoạn 2: Sinh Ảnh Mỹ Thuật Điện Ảnh Đỉnh Cao (Chờ Người Dùng Duyệt)
- [ ] 4. Sử dụng `generate_image` với `reference_nguyen_ai_quoc_1921.jpg` tạo chân dung Nguyễn Tất Thành (1910) bờ biển Phan Thiết, dáng vẻ đăm chiêu sâu thẳm <!-- id: 83 -->
- [ ] 5. Kiểm tra visual chi tiết của ảnh vừa sinh, đánh giá thần thái "đăm chiêu" và độ giống tư liệu lịch sử <!-- id: 84 -->
- [ ] 6. Cập nhật và lưu vào `prologue_2_nguyen_tat_thanh.jpg` <!-- id: 85 -->

## Giai Đoạn 3: Biên Dịch, Thẩm Định & Kiểm Thử
- [ ] 7. Chạy `python build_diegetic_odyssey.py` biên dịch `preview.html` và `index.html` <!-- id: 86 -->
- [ ] 8. Chạy `python verify_dom.py` bảo đảm 100% 77/77 DOM elements hợp lệ <!-- id: 87 -->
- [ ] 9. Kiểm tra hiển thị tại `http://localhost:8080/preview.html` đảm bảo bố cục UI và typography tương phản rõ nét <!-- id: 88 -->
- [ ] 10. Commit & Push lên kho mã nguồn GitHub `main` <!-- id: 89 -->
