# Danh Sách Công Việc: Khắc Phục Lỗi Chữ Đè & Khôi Phục Toàn Diện Tuyến Thoại Từ Đầu Đến Cuối

## Giai Đoạn 1: Khắc Phục Lỗi Chữ Đè Tại Luân Đôn (`diegeticLondonRig`)
- [x] 1. Xóa bỏ toàn bộ text tĩnh nằm trong 3 lớp tuyết `snowLayer1`, `snowLayer2`, `snowLayer3` <!-- id: 50 -->
- [x] 2. Giữ 3 lớp tuyết làm visual layer có hiệu ứng tan biến (`scale-95 opacity-0`) tự nhiên <!-- id: 51 -->
- [x] 3. Tạo một dòng trạng thái động duy nhất hiển thị tiến trình cào tuyết 3 đợt <!-- id: 52 -->

## Giai Đoạn 2: Khôi Phục 100% Tuyến Thoại Từ Đầu Đến Cuối (Dialogue Preservation)
- [x] 4. Xóa bỏ triệt để mọi lệnh `dialogueBox.classList.add('hidden')` trong `handleDiegeticTriggers()` <!-- id: 53 -->
- [x] 5. Căn chỉnh khoảng cách & z-index của các giàn tương tác (`diegeticRegisterRig`, `diegeticStudyRig`, `diegeticMarseilleRig`, `diegeticLondonRig`, `diegeticVersaillesRig`, `diegeticLeninRig`) để hiển thị hài hòa ở nửa trên sân khấu, không che lấp hộp thoại <!-- id: 54 -->
- [x] 6. Chuẩn hóa `marseille_step_1` để lời dẫn hiển thị đầy đủ trong hộp thoại chuẩn cinematic <!-- id: 55 -->
- [x] 7. Hỗ trợ nhấp chuột lên sân khấu nền (click on stage) để tiến thoại / hoàn thành máy đánh chữ mượt mà <!-- id: 56 -->

## Giai Đoạn 3: Sửa Lỗi Chuyển Cảnh & Luồng Kịch Bản
- [x] 8. Sửa hàm `finishLondonSnowScene()` tìm chính xác ID `'london_1_trust'` thay vì `'london_trust'` <!-- id: 57 -->
- [x] 9. Đảm bảo toàn bộ chuỗi đối thoại Luân Đôn (`london_1` -> `london_1_trust` -> `london_2` -> `london_2_trust`) kết nối mượt mà sang Hồi 4 <!-- id: 58 -->

## Giai Đoạn 4: Biên Dịch & Kiểm Thử Hồi Quy
- [x] 10. Chạy `python build_diegetic_odyssey.py` cập nhật `preview.html` và `index.html` <!-- id: 59 -->
- [x] 11. Chạy `python verify_dom.py` bảo đảm 77/77 DOM elements hợp lệ 100% <!-- id: 60 -->

## Giai Đoạn 5: Vào Vai Người Dùng Khó Tính Kiểm Thử Toàn Tuyến
- [x] 12. Phát hiện & sửa triệt để nguyên nhân gốc rễ gây ngắt quãng thoại (`ReferenceError: step is not defined` trên `smokeCanvas` trong `handleDiegeticTriggers`) <!-- id: 61 -->
- [x] 13. Kiểm thử tự động chạy qua toàn bộ 53 phân cảnh từ Hồi 1 đến Hồi 6, xác nhận 100% hộp thoại và hiệu ứng âm thanh hiển thị trơn tru không lỗi runtime <!-- id: 62 -->
- [x] 14. Commit và push lên Git repository <!-- id: 63 -->
