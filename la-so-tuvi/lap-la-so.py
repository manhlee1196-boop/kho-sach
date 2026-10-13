# -*- coding: utf-8 -*-
"""
An lá số Tử Vi + phi tinh tứ hóa
Đương số: NAM, âm lịch 00:30 ngày 1/10 năm Bính Tý  =  Dương lịch 11/11/1996, giờ Tý.
Luận theo《Tử Vi Đẩu Số Bí Nghi》tập 1 (Bắc phái Tứ Hóa Phi Tinh).

Chạy:  python3 lap-la-so.py     (in lá số, phi tinh 12 cung, đại hạn, lưu niên)
Kiểm:  python3 kiem-chung.py    (đối chiếu 71 khẳng định với lá số đã an)

Phần đổi âm<->dương lịch dùng thư viện sxtwl (pip install sxtwl); toàn bộ phép
an sao bên dưới là thuần Python, không phụ thuộc gì thêm.
"""
# -*- coding: utf-8 -*-
"""Lập lá số Tử Vi: nam, âm lịch 1/10/1996 (Bính Tý), giờ Tý (00:30)"""
import json

CHI = ["Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi","Thân","Dậu","Tuất","Hợi"]
CAN = ["Giáp","Ất","Bính","Đinh","Mậu","Kỷ","Canh","Tân","Nhâm","Quý"]
IDX = {c:i for i,c in enumerate(CHI)}

nam_can = "Bính"; nam_chi = "Tý"
thang = 10; ngay = 1; gio = "Tý"
duong_nam = True   # Bính = dương can

CUNG = {c:{"chi":c,"can":None,"chinh":[],"phu":[],"hoa":[],"cung":"","han":""} for c in CHI}

# ---------- 1. Mệnh / Thân ----------
# An Mệnh: từ Dần khởi tháng Giêng thuận đến tháng sinh, rồi từ đó khởi giờ Tý nghịch đến giờ sinh
i = IDX["Dần"] + (thang-1)          # thuận theo địa chi
menh = (i - IDX[gio]) % 12
# An Thân: từ cung tháng sinh khởi giờ Tý thuận đến giờ sinh
than = (i + IDX[gio]) % 12
print("Cung tháng sinh (tháng %d) ="%thang, CHI[i])
print("MỆNH cung:", CHI[menh], " THÂN cung:", CHI[than], " đồng cung" if menh==than else "")

# ---------- 2. Cục ----------
nap_am = "Giản Hạ Thủy (Nước dưới khe)"   # Bính Tý - Đinh Sửu
cuc = 2  # Thủy Nhị Cục
print("Nạp âm:", nap_am, "->", ["","Thủy Nhị Cục","Mộc Tam Cục","Kim Tứ Cục","Thổ Ngũ Cục","Hỏa Lục Cục"][cuc-1])

# ---------- 3. Tử Vi ----------
n, c = ngay, cuc
k = 0
while (n+k) % c: k += 1
q = (n+k)//c
tuv = (IDX["Dần"] + (q-1)) % 12
tuv = (tuv + k) % 12 if k % 2 == 0 else (tuv - k) % 12
print("Tử Vi tại", CHI[tuv], f"(ngày {n}, cục {c}: thêm {k}, thương {q})")

# ---------- 4. 14 chính tinh ----------
stars = {}
def put(star, pos, chinh=True):
    stars.setdefault(CHI[pos], {"chinh":[],"phu":[]})
    (stars[CHI[pos]]["chinh"] if chinh else stars[CHI[pos]]["phu"]).append(star)

# hệ Tử Vi (nghịch)
off_tv = {"Tử Vi":0,"Thiên Cơ":1,"Thái Dương":3,"Vũ Khúc":4,"Thiên Đồng":5,"Liêm Trinh":8}
for s,o in off_tv.items(): put(s,(tuv-o)%12)
# Thiên Phủ đối xứng qua trục Dần-Thân
phu = (IDX["Dần"] + (IDX["Dần"] - tuv)) % 12
print("Thiên Phủ tại", CHI[phu])
off_tf = {"Thiên Phủ":0,"Thái Âm":1,"Tham Lang":2,"Cự Môn":3,"Thiên Tướng":4,"Thiên Lương":5,"Thất Sát":6,"Phá Quân":10}
for s,o in off_tf.items(): put(s,(phu+o)%12)

# ---------- 5. Tả Hữu, Xương Khúc, Khôi Việt, Lộc Tồn, Kình Đà, Mã, Đào Hoa ----------
ta = (IDX["Thìn"] + (thang-1)) % 12
huu = (IDX["Tuất"] - (thang-1)) % 12
khuc = (IDX["Thìn"] + IDX[gio]) % 12
xuong = (IDX["Tuất"] - IDX[gio]) % 12
khoi = {"Giáp":"Sửu","Ất":"Tý","Bính":"Hợi","Đinh":"Hợi","Mậu":"Sửu","Kỷ":"Tý","Canh":"Sửu","Tân":"Dần","Nhâm":"Mão","Quý":"Mão"}[nam_can]
viet = {"Giáp":"Mùi","Ất":"Thân","Bính":"Dậu","Đinh":"Dậu","Mậu":"Mùi","Kỷ":"Thân","Canh":"Mùi","Tân":"Ngọ","Nhâm":"Tỵ","Quý":"Tỵ"}[nam_can]
loc = {"Giáp":"Dần","Ất":"Mão","Bính":"Tỵ","Đinh":"Ngọ","Mậu":"Tỵ","Kỷ":"Ngọ","Canh":"Thân","Tân":"Dậu","Nhâm":"Hợi","Quý":"Tý"}[nam_can]
kinh = (IDX[loc]+1)%12; da = (IDX[loc]-1)%12
nhom = {"Thân":"Dần","Tý":"Dần","Thìn":"Dần","Dần":"Thân","Ngọ":"Thân","Tuất":"Thân",
        "Tỵ":"Hợi","Dậu":"Hợi","Sửu":"Hợi","Hợi":"Tỵ","Mão":"Tỵ","Mùi":"Tỵ"}[nam_chi]
dao = {"Thân":"Dậu","Tý":"Dậu","Thìn":"Dậu","Dần":"Mão","Ngọ":"Mão","Tuất":"Mão",
       "Tỵ":"Ngọ","Dậu":"Ngọ","Sửu":"Ngọ","Hợi":"Tý","Mão":"Tý","Mùi":"Tý"}[nam_chi]
hong = (IDX["Mão"] - IDX[nam_chi]) % 12
hy   = (hong+6)%12
dieu = (IDX["Sửu"] + (thang-1)) % 12
hinh = (IDX["Dậu"] + (thang-1)) % 12
khoc = (IDX["Ngọ"] - IDX[nam_chi]) % 12
hu   = (IDX["Ngọ"] + IDX[nam_chi]) % 12
long = (IDX["Thìn"] + IDX[nam_chi]) % 12
phuong = (IDX["Tuất"] - IDX[nam_chi]) % 12
thang_ = (IDX["Mão"] - IDX[nam_chi]) % 12
tai  = (IDX["Mão"] + IDX[nam_chi]) % 12
hoah = {"Thân":"Dần","Tý":"Dần","Thìn":"Dần","Dần":"Sửu","Ngọ":"Sửu","Tuất":"Sửu",
        "Tỵ":"Mão","Dậu":"Mão","Sửu":"Mão","Hợi":"Dậu","Mão":"Dậu","Mùi":"Dậu"}[nam_chi]
holo = {"Thân":"Tuất","Tý":"Tuất","Thìn":"Tuất","Dần":"Mão","Ngọ":"Mão","Tuất":"Mão",
        "Tỵ":"Tuất","Dậu":"Tuất","Sửu":"Tuất","Hợi":"Tuất","Mão":"Tuất","Mùi":"Tuất"}[nam_chi]
dkhong = (IDX["Hợi"] - IDX[gio]) % 12
dkiep  = (IDX["Hợi"] + IDX[gio]) % 12
kkiep = {"Thân":"Tỵ","Tý":"Tỵ","Thìn":"Tỵ","Dần":"Hợi","Ngọ":"Hợi","Tuất":"Hợi",
         "Tỵ":"Dần","Dậu":"Dần","Sửu":"Dần","Hợi":"Thân","Mão":"Thân","Mùi":"Thân"}[nam_chi]
dhao = IDX[{"Thân":"Mão","Tý":"Mão","Thìn":"Mão","Dần":"Dậu","Ngọ":"Dậu","Tuất":"Dậu",
        "Tỵ":"Hợi","Dậu":"Hợi","Sửu":"Hợi","Hợi":"Tỵ","Mão":"Tỵ","Mùi":"Tỵ"}[nam_chi]]
xhao = (dhao+6)%12
tkhong = (IDX[nam_chi]+1)%12
# Tam Thai Bát Tọa
tam = (ta + (thang-1)) % 12
bat = (huu - (thang-1)) % 12
# Ân Quang Thiên Quý (khởi từ Xương/Khúc đếm tháng thuận/nghịch, rồi đếm ngày thuận/nghịch, lùi/tiến 1)
aq = (xuong + (thang-1) + (ngay-1) - 1) % 12
tq = (khuc - (thang-1) - (ngay-1) + 1) % 12
# Thiên Giải / Giải Thần (đối cung)
tgiai = (IDX["Mùi"] + (thang-1)) % 12
ggiai = (tgiai+6)%12
# vòng Thái Tuế
vong_tt = ["Thái Tuế","Thiếu Dương","Tang Môn","Thiếu Âm","Quan Phù","Tử Phù","Tuế Phá","Long Đức","Bạch Hổ","Phúc Đức","Điếu Khách","Trực Phù"]
thaitue = {}
for j,s in enumerate(vong_tt): thaitue[CHI[(IDX[nam_chi]+j)%12]] = s
# vòng Tràng Sinh (Thủy nhị cục -> Tràng Sinh tại Thân; dương nam thuận)
vong_ts = ["Tràng Sinh","Mộc Dục","Quan Đới","Lâm Quan","Đế Vượng","Suy","Bệnh","Tử","Mộ","Tuyệt","Thai","Dưỡng"]
start_ts = {"2":IDX["Thân"],"3":IDX["Hợi"],"4":IDX["Hợi"],"5":IDX["Thân"],"6":IDX["Dần"]}[str(cuc)]
truong = {}
for j,s in enumerate(vong_ts):
    p = (start_ts + j) % 12 if duong_nam else (start_ts - j) % 12
    truong[CHI[p]] = s

for s,p in [("Tả Phù",ta),("Hữu Bật",huu),("Văn Khúc",khuc),("Văn Xương",xuong),("Thiên Khôi",IDX[khoi]),("Thiên Việt",IDX[viet]),
            ("Lộc Tồn",IDX[loc]),("Kình Dương",kinh),("Đà La",da),("Thiên Mã",IDX[nhom]),("Đào Hoa",IDX[dao]),
            ("Hồng Loan",hong),("Thiên Hỷ",hy),("Thiên Diêu",dieu),("Thiên Hình",hinh),("Thiên Khốc",khoc),("Thiên Hư",hu),
            ("Long Trì",long),("Phượng Các",phuong),("Thiên Thương",thang_),("Thiên Sứ",tai),("Hỏa Tinh",IDX[hoah]),("Linh Tinh",IDX[holo]),
            ("Địa Không",dkhong),("Địa Kiếp",dkiep),("Kiếp Sát",IDX[kkiep]),("Đại Hao",dhao),("Tiểu Hao",xhao),("Thiên Không",tkhong),
            ("Tam Thai",tam),("Bát Tọa",bat),("Ân Quang",aq),("Thiên Quý",tq),("Thiên Giải",tgiai),("Giải Thần",ggiai)]:
    stars.setdefault(CHI[p],{"chinh":[],"phu":[]})["phu"].append(s)

print("\n--- VÒNG SAO PHỤ (tra cứu) ---")
for k,v in [("Tả Phù",ta),("Hữu Bật",huu),("Văn Xương",xuong),("Văn Khúc",khuc),("Thiên Khôi",IDX[khoi]),("Thiên Việt",IDX[viet]),
            ("Lộc Tồn",IDX[loc]),("Kình Dương",kinh),("Đà La",da),("Thiên Mã",IDX[nhom]),("Đào Hoa",IDX[dao]),
            ("Hồng Loan",hong),("Thiên Hỷ",hy),("Thiên Diêu",dieu),("Thiên Hình",hinh),("Thiên Khốc",khoc),("Thiên Hư",hu),
            ("Long Trì",long),("Phượng Các",phuong),("Thiên Thương",thang_),("Thiên Sứ",tai),("Hỏa Tinh",IDX[hoah]),("Linh Tinh",IDX[holo]),
            ("Địa Không",dkhong),("Địa Kiếp",dkiep),("Kiếp Sát",IDX[kkiep]),("Đại Hao",dhao),("Tiểu Hao",xhao),("Thiên Không",tkhong),
            ("Tam Thai",tam),("Bát Tọa",bat),("Ân Quang",aq),("Thiên Quý",tq),("Thiên Giải",tgiai),("Giải Thần",ggiai)]:
    print(f"  {k:12s} {CHI[v]}")

# ---------- 6. 12 cung + can cung (ngũ hổ độn) ----------
can_dau = {"Giáp":"Bính","Ất":"Mậu","Bính":"Canh","Đinh":"Nhâm","Mậu":"Giáp","Kỷ":"Bính","Canh":"Mậu","Tân":"Canh","Nhâm":"Nhâm","Quý":"Giáp"}[nam_can]
for j,c in enumerate(CHI):
    CUNG[c]["can"] = CAN[(CAN.index(can_dau)+((j-2)%12))%10]   # can_dau ứng với cung Dần
ten12 = ["Mệnh","Phụ Mẫu","Phúc Đức","Điền Trạch","Quan Lộc","Nô Bộc","Thiên Di","Tật Ách","Tài Bạch","Tử Tức","Phu Thê","Huynh Đệ"]
for j,t in enumerate(ten12): CUNG[CHI[(menh-j)%12]]["cung"] = t
CUNG[CHI[than]]["cung"] += "+Thân"

# ---------- 7. Đại hạn / Tiểu hạn ----------
han = []
for k in range(12):
    p = (menh + k) % 12 if duong_nam else (menh - k) % 12
    han.append((CHI[p], cuc + k*10, cuc + k*10 + 9))
for c,a,b in han: CUNG[c]["han"] = f"{a}-{b}"
tieu = (IDX["Tuất"] + 30) % 12   # tuổi mụ 31 năm 2026, năm Tý khởi Tuất thuận
# Đẩu quân
dq = (IDX[nam_chi] - (thang-1)) % 12
dq = (dq + IDX[gio]) % 12

# ---------- 8. Tứ Hóa ----------
TH = {
 "Giáp":("Liêm Trinh","Phá Quân","Vũ Khúc","Thái Dương"),
 "Ất":("Thiên Cơ","Thiên Lương","Tử Vi","Thái Âm"),
 "Bính":("Thiên Đồng","Thiên Cơ","Văn Xương","Liêm Trinh"),
 "Đinh":("Thái Âm","Thiên Đồng","Thiên Cơ","Cự Môn"),
 "Mậu":("Tham Lang","Thái Âm","Hữu Bật","Thiên Cơ"),
 "Kỷ":("Vũ Khúc","Tham Lang","Thiên Lương","Văn Khúc"),
 "Canh":("Thái Dương","Vũ Khúc","Thái Âm","Thiên Đồng"),
 "Tân":("Cự Môn","Thái Dương","Văn Khúc","Văn Xương"),
 "Nhâm":("Thiên Lương","Tử Vi","Tả Phù","Vũ Khúc"),
 "Quý":("Phá Quân","Cự Môn","Thái Âm","Tham Lang"),
}
pos = {}
for c,d in stars.items():
    for s in d["chinh"]+d["phu"]: pos[s]=c

print("\n--- SINH NIÊN TỨ HÓA (can", nam_can, ") ---")
for lbl,s in zip(["Lộc","Quyền","Khoa","Kỵ"], TH[nam_can]):
    print(f"  {s} hóa {lbl} -> {pos.get(s,'?')}  ({CUNG[pos.get(s,'')]['cung']})")

print("\n--- PHI TINH TỨ HÓA TỪ 12 CUNG ---")
fly = {}
order = ["Mệnh","Phụ Mẫu","Phúc Đức","Điền Trạch","Quan Lộc","Nô Bộc","Thiên Di","Tật Ách","Tài Bạch","Tử Tức","Phu Thê","Huynh Đệ"]
for j,t in enumerate(order):
    c = CHI[(menh-j)%12]
    can = CUNG[c]["can"]
    r = []
    for lbl,s in zip(["Lộc","Quyền","Khoa","Kỵ"], TH[can]):
        tgt = pos.get(s,"?")
        tu = "(tự hóa)" if tgt==c else ""
        r.append(f"{s}{lbl}->{tgt}[{CUNG[tgt]['cung']}]{tu}")
    fly[t]=(c,can,r)
    print(f"  {t:10s} {can}{c}: " + " | ".join(r))

# ---------- in lá số ----------
print("\n" + "="*70)
grid = {"row0":["Tỵ","Ngọ","Mùi","Thân"],"row1":["Thìn",None,None,"Dậu"],"row2":["Mão",None,None,"Tuất"],"row3":["Dần","Sửu","Tý","Hợi"]}
for row in grid.values():
    for c in row:
        if not c: print(" "*34, end="|"); continue
        d = CUNG[c]
        st = stars.get(c,{"chinh":[],"phu":[]})
        print(f"[{d['can']}{c} {d['cung']} {d['han']}] " + ",".join(st['chinh']) + "  // " + ",".join(st['phu'][:8]), end="  |")
    print()

print("\nTiểu hạn 31 tuổi (2026):", CHI[tieu], "| Đẩu quân bản mệnh:", CHI[dq], "| Đẩu quân lưu niên Bính Ngọ 2026:", CHI[(IDX["Ngọ"]-(thang-1)+IDX[gio])%12])


order12 = ["Mệnh","Phụ Mẫu","Phúc Đức","Điền Trạch","Quan Lộc","Nô Bộc","Thiên Di","Tật Ách","Tài Bạch","Tử Tức","Phu Thê","Huynh Đệ"]
cung_ten = {CHI[(menh-j)%12]: order12[j] for j in range(12)}

# ==================================================================
#  PHẦN 2 — PHI TINH TỨ HÓA, ĐẠI HẠN, LƯU NIÊN, BẢNG QUYẾT ĐOÁN
# ==================================================================
SN = dict(zip(["Lộc","Quyền","Khoa","Kỵ"], TH[nam_can]))
sn_pos = {lbl: pos[s] for lbl, s in SN.items()}
def palaces(anchor):
    return {order[j]: CHI[(IDX[anchor]-j) % 12] for j, order in
            [(j, order12) for j in range(12)]} if False else \
           {order12[j]: CHI[(IDX[anchor]-j) % 12] for j in range(12)}

print("\n--- PHI TINH TỨ HÓA TỪ 12 CUNG BẢN MỆNH ---")
fly = {}
for t, c in palaces(CHI[menh]).items():
    can = CUNG[c]["can"]
    fly[t] = {lbl: (s, pos[s], cung_ten[pos[s]], pos[s] == c)
              for lbl, s in zip(["Lộc","Quyền","Khoa","Kỵ"], TH[can])}
    print(f"  {t:10s} {can}{c}: " + " | ".join(
        f"{s}{lbl}->{pos[s]}({cung_ten[pos[s]]}){'[tự hóa]' if pos[s]==c else ''}"
        for lbl, s in zip(["Lộc","Quyền","Khoa","Kỵ"], TH[can])))

print("\n--- ĐẠI HẠN (Thủy Nhị Cục, dương nam thuận hành, khởi 2 tuổi) ---")
for k in range(12):
    p = CHI[(menh+k) % 12]
    print(f"  {cuc+k*10:>3}-{cuc+k*10+9:<3} {CUNG[p]['can']}{p}  ({1995+cuc+k*10}-{1995+cuc+k*10+9})")

print("\n--- QUYẾT ĐOÁN TÀI-QUAN THEO ĐẠI HẠN (Bí Nghi, sách tr.107-108) ---")
for k in range(12):
    p = CHI[(menh+k) % 12]
    print(f"\n  ĐH {cuc+k*10}-{cuc+k*10+9} tại {CUNG[p]['can']}{p}:")
    pv = palaces(p)
    for role in ["Quan Lộc","Tài Bạch","Điền Trạch"]:
        q = pv[role]; can = CUNG[q]["can"]
        k_ = TH[can][3]
        tgt = pos[k_]
        note = ""
        if cung_ten[tgt] == "Phụ Mẫu": note = "  <<<< KỴ nhập PHỤ MẪU xung TẬT ÁCH (tuyến nặng)"
        elif cung_ten[tgt] == "Tật Ách": note = "  << Kỵ nhập Tật Ách xung Phụ Mẫu (tuyến bệnh)"
        elif cung_ten[tgt] in ("Quan Lộc","Phu Thê"): note = f"  << Kỵ nhập {cung_ten[tgt]}"
        print(f"    {role:10s} {can}{q}: Kỵ = {k_} -> {tgt} ({cung_ten[tgt]}){note}")

print("\n--- LƯU NIÊN 2026-2030 ---")
for yr, ychi in [(2026,"Ngọ"),(2027,"Mùi"),(2028,"Thân"),(2029,"Dậu"),(2030,"Tuất")]:
    can = CAN[(yr-1984) % 10]
    pv = palaces(ychi)
    print(f"  {yr} {can}{ychi} ({yr-1996+1}t): Mệnh LN {ychi}; "
          + " ".join(f"{l}:{s}->{pos[s]}({cung_ten[pos[s]]})"
                     for l, s in zip(["Lộc","Quyền","Khoa","Kỵ"], TH[can])))
