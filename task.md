# Danh Sách Công Việc: Chuyển Nhịp 2 Pha Tương Tác & Sổ Tay Học Tiếng Pháp

## Giai Đoạn 1: Thiết Kế UI Sổ Tay Học Tiếng Pháp Trên Boong Tàu (`ship_2`)
- [x] 1. Thêm thẻ nút gọi diegetic `#frenchNotebookDeskTrigger` (hình cuốn sổ tay mạ vàng với ánh đèn bão) nằm bên cạnh sân khấu trong `build_diegetic_odyssey.py` <!-- id: 70 -->
- [x] 2. Thêm hàm `openFrenchNotebookFromDesk()` kích hoạt âm thanh lật trang giấy xào xạc `playPageTurnSound()` và mở `diegeticStudyRig` <!-- id: 71 -->

## Giai Đoạn 2: Xây Dựng Cơ Chế 2 Pha (Two-Phase Pacing) Cho Tất Cả Các Cảnh Tương Tác
- [x] 3. Bổ sung trạng thái `state.interactivePhase = 'narrative'` (đang nghe thoại) | `'ready'` (thoại xong, chờ nhấp chuột) | `'active'` (đang làm mini-game) <!-- id: 72 -->
- [x] 4. Trong `handleDiegeticTriggers()`, khi vào cảnh tương tác (`diegetic_register`, `diegetic_study`, `diegetic_london`, `diegetic_versailles`, `diegetic_lenin`, `diegetic_unification`, `diegetic_milestone`): tạm ẩn các giàn tương tác, chỉ chạy typewriter <!-- id: 73 -->
- [x] 5. Khi máy đánh chữ hoàn thành (`finishTypewriter()`): chuyển `state.interactivePhase = 'ready'`. Hiển thị gợi ý nhấp chuột hoặc nút mở sổ tay <!-- id: 74 -->
- [x] 6. Cập nhật `advanceDialogue()`: khi `state.interactivePhase === 'ready'`, nhấp chuột sẽ mở giàn tương tác tương ứng (`activateCurrentInteractiveRig()`) thay vì nhảy cóc qua cảnh tiếp theo <!-- id: 75 -->

## Giai Đoạn 3: Biên Dịch, Kiểm Định DOM & Mô Phỏng Toàn Tuyến
- [x] 7. Chạy `python build_diegetic_odyssey.py` biên dịch `preview.html` và `index.html` <!-- id: 76 -->
- [x] 8. Chạy `python verify_dom.py` bảo đảm 100% 77/77 DOM elements hợp lệ <!-- id: 77 -->
- [x] 9. Viết & chạy kịch bản kiểm thử mô phỏng 53 phân cảnh xác nhận luồng 2 pha và mở sổ tay chạy trơn tru <!-- id: 78 -->
- [x] 10. Commit và đồng bộ lên GitHub <!-- id: 79 -->
