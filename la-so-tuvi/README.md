# Lá số Tử Vi — Bắc Phái Tứ Hóa Phi Tinh

**Đương số:** NAM · 00:30 mùng 1 tháng 10 năm **Bính Tý** (âm lịch) = thứ Hai **11/11/1996** · **giờ Tý**
**Căn cứ:**《TỬ VI ĐẨU SỐ BÍ NGHI》tập 1 (bản demo 151 trang) — chuyên đề *Thập bát phi tinh* / *Tứ Hóa Phi Tinh* Bắc Phái (Khâm Thiên Tứ Hóa).

> ⚠️ **Bản này thay thế hoàn toàn bản trước.** Bản trước sai **Mộc/Thủy cục** và **chiều an 12 cung**, nên ra Mệnh *vô chính diệu*. Lá số đúng là **Mộc Tam Cục, Thiên Đồng thủ Mệnh tại Hợi**. Chi tiết ở mục **§0 ĐÍNH CHÍNH** của `LUAN-GIAI.md`.

---

## File

| File | Nội dung |
|---|---|
| **`luận-giải-lá-số.html`** | **Bản luận giải đầy đủ** + bàn đồ. Mở file này. |
| `lá-số-tử-vi.html` | Chỉ bàn đồ 12 cung (chính tinh, phụ tinh, tứ hóa năm sinh, phi tinh, đại hạn, Tràng Sinh) |
| `LUAN-GIAI.md` | Nguồn của bản luận giải (Markdown) |
| `lap-la-so.py` | Engine an số **tự chứa** + tầng phi tinh / đại hạn / lưu niên / lưu nguyệt / đẩu quân |
| `kiem-chung.py` | Bộ kiểm chứng — xem dưới |
| `tao-html.py` | Sinh 2 file HTML từ `lap-la-so.py` + `LUAN-GIAI.md` |

## Chạy lại

```bash
cd la-so-tuvi
python lap-la-so.py      # in lá số + phi tinh 12 cung + đại hạn
python kiem-chung.py     # 153 khẳng định; exit 0 = đạt hết
python tao-html.py       # sinh lại 2 file HTML  (cần: pip install markdown)
```

## `kiem-chung.py` — 153 ĐẠT / 0 LỖI

**Tầng A — soi chéo với `py-iztro` 0.1.5 (iztro 2.5.0)**, một engine an sao độc lập, **từng sao ở cả 12 cung**:
Mệnh/Thân cung · ngũ hành cục · tứ trụ · Mệnh chủ/Thân chủ · tên cung · can cung · **14 chính tinh** · **toàn bộ phụ tinh & tạp tinh** · khoảng đại hạn · vị trí 4 sao hóa năm sinh.

**Tầng B — khẳng định theo《Bí Nghi》** (kèm số trang):
hai quy tắc an số gốc · sinh niên tứ hóa · phi tinh 12 cung · 14 câu "quyết" trích nguyên văn · 12 đại hạn (quét tuyến tử vong) · lưu niên 2026–2027 + lưu nguyệt.

Tầng A tự bỏ qua nếu chưa cài `py-iztro` (`pip install py-iztro`); tầng B vẫn chạy.

## Hai quy tắc dễ sai (nguyên nhân bản trước hỏng)

1. **Ngũ hành cục lấy theo nạp âm của CAN CHI CUNG MỆNH, không theo năm sinh.**
   Mệnh = Kỷ Hợi → *Bình Địa Mộc* → **Mộc Tam Cục** (không phải Giản Hạ Thủy của Bính Tý).
2. **Mười hai cung đi NGHỊCH địa chi từ cung Mệnh:**
   Mệnh → Huynh Đệ → Phu Thê → Tử Tức → Tài Bạch → Tật Ách → Thiên Di → Nô Bộc → Quan Lộc → Điền Trạch → Phúc Đức → Phụ Mẫu.
   (Khớp ví dụ trong《Bí Nghi》demo tr.114–118: Mệnh Bính Tý thì Huynh Đệ ở Ất Hợi, Phụ Mẫu ở Đinh Sửu.)

## Kết quả chính

| | |
|---|---|
| Cục | **Mộc Tam Cục** (Kỷ Hợi = Bình Địa Mộc) |
| Mệnh = Thân | **Hợi** — **Thiên Đồng thủ Mệnh**, sinh niên **Lộc** tọa Mệnh |
| Tứ trụ | Bính Tý · Kỷ Hợi · Nhâm Tý · Canh Tý |
| Sinh niên tứ hóa | Thiên Đồng **Lộc** → Hợi *(Mệnh)* · Thiên Cơ **Quyền** → Mão *(Quan Lộc)* · Văn Xương **Khoa** → Tuất *(Huynh Đệ)* · Liêm Trinh **Kỵ** → Thân *(Tử Tức)* |
| Đại hạn hiện hành | **23–32, Tân Sửu (2018–2027)** |
| Điểm mạnh | Phúc tinh hóa Lộc thủ Mệnh; Quan Lộc Cự Môn tự hóa Lộc + Thiên Cơ Quyền; ra ngoài có ấm (Thiên Lương + Lộc Tồn) |
| Điểm yếu | Thiên Đồng Lộc nhập Mệnh → *"không thích làm"*; Tài Bạch vô chính diệu bị **2 Kỵ xung**; Kỵ trùng Kỵ ở Tử Tức; Văn Xương Kỵ thường trú (xe cộ, giấy tờ) |
| Rủi ro lớn nhất | Nô Bộc → Vũ Khúc **Kỵ nhập Phụ Mẫu xung Tật Ách** = *tuyến tử vong* (sách tr.53, tr.107) — nguồn: bạn bè/tiền bạc; kích hoạt ở **đại hạn 53–62** |
| Điểm tựa lớn nhất | Sinh niên Kỵ **không** tọa Mệnh ⇒ không đại hạn nào kích hoạt *"kiếp lớn (kiếp sinh tử)"* (sách tr.16 mục 9) |

## Giới hạn

Bản PDF là **bản demo bị cắt**: thiếu *Tứ hóa phi tinh kỳ phổ* (Nghịch thủy kỵ, Thủy mệnh kỵ, Thuận thủy Kỵ, Tiêm triền Kỵ, Thị phi Kỵ, Phản cung Kỵ, Tuần hoàn Kỵ, Tháo mã Kỵ, Nhập khố Kỵ) và thiếu chính giải 5/18 sao (Phá Quân, Tả Phù, Hữu Bật, Văn Xương, Văn Khúc). Sách cũng thuần Bắc Phái nên **không** luận Địa Không/Địa Kiếp, Tuần/Triệt, Nhật Nguyệt đồng cung, Hỏa Tham. Chi tiết ở **§9** của bản luận giải.
