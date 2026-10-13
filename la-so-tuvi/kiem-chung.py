# -*- coding: utf-8 -*-
"""
Kiểm chứng: đối chiếu 70+ khẳng định trong LUAN-GIAI.md với lá số vừa an.
Chạy:  python3 kiem-chung.py      (thoát 0 = tất cả PASS, 1 = có FAIL)
"""
import io, os, re, sys, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(os.path.join(HERE, "lap-la-so.py"), encoding="utf-8").read(),
                 "lap-la-so.py", "exec"), globals())
doc = open(os.path.join(HERE, "LUAN-GIAI.md"), encoding="utf-8").read()

ok = fail = 0
def chk(name, cond, detail=""):
    global ok, fail
    if cond: ok += 1; print(f"  PASS  {name}")
    else:    fail += 1; print(f"  FAIL  {name}  {detail}")

# fly[t] = {Lộc: (sao, đích, cung, tự_hóa), ...}
F = fly

print("== 1. Cấu trúc lá số ==")
chk("Mệnh & Thân đồng cung tại Hợi", CHI[menh]=="Hợi" and CHI[than]=="Hợi")
chk("Mệnh Hợi vô chính diệu", stars["Hợi"]["chinh"]==[])
chk("Tử Vi tại Sửu", pos["Tử Vi"]=="Sửu")
chk("Tử Phá đồng cung Sửu", {"Tử Vi","Phá Quân"} <= set(stars["Sửu"]["chinh"]))
chk("Liêm Tham đồng cung Tỵ", {"Liêm Trinh","Tham Lang"} <= set(stars["Tỵ"]["chinh"]))
chk("Đồng Lương đồng cung Thân", {"Thiên Đồng","Thiên Lương"} <= set(stars["Thân"]["chinh"]))
chk("Vũ Sát đồng cung Dậu", {"Vũ Khúc","Thất Sát"} <= set(stars["Dậu"]["chinh"]))
chk("Đủ 14 chính tinh, 12 cung", sum(len(stars[c]["chinh"]) for c in stars)==14 and len(stars)==12)
chk("Tả Hữu đồng cung Sửu", {"Tả Phù","Hữu Bật"} <= set(stars["Sửu"]["phu"]))
chk("Văn Xương Tuất / Văn Khúc Thìn", pos["Văn Xương"]=="Tuất" and pos["Văn Khúc"]=="Thìn")
chk("Khôi Hợi / Việt Dậu", pos["Thiên Khôi"]=="Hợi" and pos["Thiên Việt"]=="Dậu")
chk("Lộc Tồn Tỵ, Kình Ngọ, Đà Thìn", pos["Lộc Tồn"]=="Tỵ" and pos["Kình Dương"]=="Ngọ" and pos["Đà La"]=="Thìn")
chk("Không Kiếp đồng cung Hợi", pos["Địa Không"]=="Hợi" and pos["Địa Kiếp"]=="Hợi")
chk("Hỏa Tinh Dần, Linh Tinh Tuất", pos["Hỏa Tinh"]=="Dần" and pos["Linh Tinh"]=="Tuất")
chk("Khốc & Hư đều ở Ngọ", pos["Thiên Khốc"]=="Ngọ" and pos["Thiên Hư"]=="Ngọ")
chk("Long Trì Thìn, Phượng Các Tuất", pos["Long Trì"]=="Thìn" and pos["Phượng Các"]=="Tuất")
chk("Thiên Mã Dần, Đào Hoa Dậu", pos["Thiên Mã"]=="Dần" and pos["Đào Hoa"]=="Dậu")
chk("Hồng Loan Mão, Thiên Hỷ Dậu", pos["Hồng Loan"]=="Mão" and pos["Thiên Hỷ"]=="Dậu")
chk("Thiên Diêu Tuất, Thiên Hình Ngọ", pos["Thiên Diêu"]=="Tuất" and pos["Thiên Hình"]=="Ngọ")
chk("Kiếp Sát Tỵ, Thiên Không Sửu", pos["Kiếp Sát"]=="Tỵ" and pos["Thiên Không"]=="Sửu")
chk("Đẩu quân Mão, tiểu hạn 2026 Thìn", CHI[dq]=="Mão" and CHI[tieu]=="Thìn")
chk("Thái Tuế tại Tý", thaitue["Tý"]=="Thái Tuế" and thaitue["Ngọ"]=="Tuế Phá")
chk("Tràng Sinh tại Thân (Thủy nhị cục)", truong["Thân"]=="Tràng Sinh" and truong["Tỵ"]=="Tuyệt")

print("== 2. Can 12 cung (ngũ hổ độn: Bính -> Canh Dần) ==")
for c,g in {"Dần":"Canh","Mão":"Tân","Thìn":"Nhâm","Tỵ":"Quý","Ngọ":"Giáp","Mùi":"Ất",
            "Thân":"Bính","Dậu":"Đinh","Tuất":"Mậu","Hợi":"Kỷ","Tý":"Canh","Sửu":"Tân"}.items():
    chk(f"can {c}={g}", CUNG[c]["can"]==g, CUNG[c]["can"])

print("== 3. Sinh niên tứ hóa (can Bính) ==")
chk("Thiên Đồng Lộc -> Thân (Điền Trạch)", SN["Lộc"]=="Thiên Đồng" and pos["Thiên Đồng"]=="Thân" and cung_ten["Thân"]=="Điền Trạch")
chk("Thiên Cơ Quyền -> Tý (Huynh Đệ)",     SN["Quyền"]=="Thiên Cơ" and pos["Thiên Cơ"]=="Tý" and cung_ten["Tý"]=="Huynh Đệ")
chk("Văn Xương Khoa -> Tuất (Phụ Mẫu)",    SN["Khoa"]=="Văn Xương" and pos["Văn Xương"]=="Tuất" and cung_ten["Tuất"]=="Phụ Mẫu")
chk("Liêm Trinh Kỵ -> Tỵ (Thiên Di)",      SN["Kỵ"]=="Liêm Trinh" and pos["Liêm Trinh"]=="Tỵ" and cung_ten["Tỵ"]=="Thiên Di")

print("== 4. Phi tinh Mệnh cung (Kỷ Hợi) ==")
m = F["Mệnh"]
chk("Vũ Khúc Lộc -> Dậu (Phúc Đức)",   m["Lộc"][0]=="Vũ Khúc"  and m["Lộc"][2]=="Phúc Đức")
chk("Tham Lang Quyền -> Tỵ (Thiên Di)", m["Quyền"][0]=="Tham Lang" and m["Quyền"][2]=="Thiên Di")
chk("Thiên Lương Khoa -> Thân (Điền Trạch)", m["Khoa"][0]=="Thiên Lương" and m["Khoa"][2]=="Điền Trạch")
chk("Văn Khúc Kỵ -> Thìn (Tật Ách)",     m["Kỵ"][0]=="Văn Khúc" and m["Kỵ"][2]=="Tật Ách")

print("== 5. Hai tuyến sinh-bệnh ==")
nho = sorted(t for t in F if F[t]["Kỵ"][2]=="Phụ Mẫu")
chk("Kỵ nhập Phụ Mẫu xung Tật Ách: đúng 3 cung (Nô Bộc, Phu Thê, Tài Bạch)", nho==["Nô Bộc","Phu Thê","Tài Bạch"], str(nho))
tat = sorted(t for t in F if F[t]["Kỵ"][2]=="Tật Ách")
chk("Kỵ nhập Tật Ách xung Phụ Mẫu: Mệnh + Quan Lộc", tat==["Mệnh","Quan Lộc"], str(tat))
chk("không có Kỵ nhập Quan Lộc (tuyến tử vong thứ hai)", all(F[t]["Kỵ"][2]!="Quan Lộc" for t in F))

print("== 6. Tự hóa ==")
tu = sorted((t,l) for t in F for l in F[t] if F[t][l][3])
chk("chỉ 2 tự hóa: Điền Trạch-Lộc, Thiên Di-Kỵ", tu==[("Thiên Di","Kỵ"),("Điền Trạch","Lộc")], str(tu))

print("== 7. Nơi tụ tứ hóa (đếm cả sinh niên) ==")
from collections import defaultdict
cnt = defaultdict(lambda: defaultdict(int))
for t in F:
    for l in F[t]: cnt[F[t][l][1]][l] += 1
for l in SN: cnt[sn_pos[l]][l] += 1
chk("Tuất: Lộc2 Quyền2 Khoa2 Kỵ3", [cnt["Tuất"][x] for x in ("Lộc","Quyền","Khoa","Kỵ")]==[2,2,2,3], str(dict(cnt["Tuất"])))
chk("Thìn: Lộc1 Quyền1 Khoa5 Kỵ2", [cnt["Thìn"][x] for x in ("Lộc","Quyền","Khoa","Kỵ")]==[1,1,5,2], str(dict(cnt["Thìn"])))
chk("Tỵ : Lộc2 Quyền1 Khoa0 Kỵ3", [cnt["Tỵ"][x]  for x in ("Lộc","Quyền","Khoa","Kỵ")]==[2,1,0,3], str(dict(cnt["Tỵ"])))
chk("Dậu: Lộc1 Quyền2 Khoa1 Kỵ1", [cnt["Dậu"][x] for x in ("Lộc","Quyền","Khoa","Kỵ")]==[1,2,1,1], str(dict(cnt["Dậu"])))
chk("Thân: Lộc3 Quyền2 Khoa1 Kỵ2", [cnt["Thân"][x] for x in ("Lộc","Quyền","Khoa","Kỵ")]==[3,2,1,2], str(dict(cnt["Thân"])))
chk("Mùi (Quan Lộc) không nhận tứ hóa nào", sum(cnt["Mùi"].values())==0)

print("== 8. Đại hạn ==")
for c,t in [("Hợi","2-11"),("Tý","12-21"),("Sửu","22-31"),("Dần","32-41"),("Mão","42-51"),
            ("Thìn","52-61"),("Tỵ","62-71"),("Ngọ","72-81"),("Mùi","82-91"),("Thân","92-101"),
            ("Dậu","102-111"),("Tuất","112-121")]:
    chk(f"ĐH {c} = {t}", CUNG[c]["han"]==t, CUNG[c]["han"])

print("== 9. Văn bản LUAN-GIAI.md khớp lá số ==")
for frag in ["Mệnh–Thân đồng cung","Thủy Nhị Cục","vô chính diệu","Liêm Trinh **〔Kỵ〕**",
             "Thiên Đồng **〔Lộc〕**","Thứ Hai, 11/11/1996","Bính Tý · Kỷ Hợi · Nhâm Tý · **Canh Tý**",
             "Lộc ×2, Quyền ×2, Khoa ×2, Kỵ ×3","Lộc 1, Quyền 1, Khoa 5, Kỵ 2",
             "Đào Hoa + Thiên Hỷ tại Dậu","| Tử Vi | tại Sửu |"]:
    chk(f'có "{frag}"', frag in doc)
for bad in ["Thiên Hỷ tại Tuất","Bốn nơi tụ","Khoa ×5, **Kỵ ×3**"]:
    chk(f'không còn "{bad}"', bad not in doc)
chk("mục 9 có ghi rõ Thiên Thương/Thiên Sứ không được an", "Thiên Thương – Thiên Sứ không được an" in doc)

print(f"\n=== {ok} PASS / {fail} FAIL ===")
sys.exit(1 if fail else 0)
