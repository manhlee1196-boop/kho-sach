# Lá số Tử Vi — nam mệnh 1/10/1996 (âm lịch) giờ Tý

Luận giải theo **《Tử Vi Đẩu Số Bí Nghi》tập 1** (bản demo 151 trang trong repo này) —
phái **Bắc phái Tứ Hóa Phi Tinh**, chủ giảng Thái Minh Hồng.

## Tệp

| Tệp | Nội dung |
|---|---|
| **`luận-giải-lá-số.html`** | **Bản chính** — lá số 12 cung + toàn bộ bài luận giải, mở bằng trình duyệt |
| `lá-số-tử-vi.html` | Chỉ riêng lá số (sơ đồ 12 cung, tứ hóa năm sinh, phi tinh từng cung) |
| `LUAN-GIAI.md` | Nguồn Markdown của bài luận giải |
| `lap-la-so.py` | Script an lá số: chính tinh, phụ tinh, vòng Thái Tuế / Tràng Sinh, can 12 cung, phi tinh tứ hóa, đại hạn, lưu niên, bảng quyết đoán Tài–Quan |
| `kiem-chung.py` | Đối chiếu **80 khẳng định** trong bài luận giải với lá số vừa an |

## Đương số

| | |
|---|---|
| Âm lịch | 00:30 ngày 1 tháng 10 năm Bính Tý |
| Dương lịch | Thứ Hai, 11/11/1996 — giờ Tý |
| Tứ trụ | Bính Tý · Kỷ Hợi · Nhâm Tý · Canh Tý |
| Cục | Giản Hạ Thủy → **Thủy Nhị Cục** |
| Mệnh – Thân | **đồng cung tại Kỷ Hợi**, vô chính diệu, mượn Liêm Trinh–Tham Lang ở Tỵ |

## Chạy lại

```bash
pip install sxtwl          # chỉ cần cho bước đổi âm <-> dương lịch
python3 lap-la-so.py       # in lá số + phi tinh + đại hạn + lưu niên
python3 kiem-chung.py      # 80 PASS / 0 FAIL
```

## Giới hạn

Tài liệu trong repo là **bản demo 151 trang** (sách gốc tr.1–131), **thiếu** các chuyên luận
về các cách Kỵ đặc thù của Bắc phái (*Nghịch thủy kỵ, Thủy mệnh kỵ, Thuận thủy kỵ,
Tiêm triền kỵ, Thị phi kỵ, Phản cung kỵ, Tuần hoàn kỵ, Tháo mã kỵ, Nhập khố kỵ,
Tiến mã kỵ, Thoái mã kỵ, Tuyệt mệnh kỵ*) cùng *Cửu tinh bố thập nhị cung cố định bàn*,
*Thiên nhân hợp nhất luận mệnh pháp*, *Thiên địa định số*. Bài luận giải vì thế dừng ở tầng
**tứ hóa năm sinh + phi tinh 12 cung + thập bát phi tinh**. Chi tiết ở mục 9 của bài.
