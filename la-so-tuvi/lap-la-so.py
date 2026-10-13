# -*- coding: utf-8 -*-
"""
LẬP LÁ SỐ TỬ VI  —  NAM, âm lịch 00:30 mùng 1 tháng 10 năm Bính Tý
                    (= dương lịch thứ Hai 11/11/1996), giờ Tý.

Engine tự chứa, không phụ thuộc thư viện ngoài.
Tầng luận giải: Tứ Hóa Phi Tinh Bắc Phái theo《TỬ VI ĐẨU SỐ BÍ NGHI》tập 1.

HAI QUY TẮC DỄ SAI (đã kiểm chứng chéo với py-iztro 0.1.5 / iztro 2.5.0
và với chính ví dụ trong《Bí Nghi》demo tr.114–118):

 (1) NGŨ HÀNH CỤC lấy theo NẠP ÂM CỦA CAN CHI CUNG MỆNH,
     KHÔNG lấy theo nạp âm của năm sinh.
         Mệnh = Kỷ Hợi → Mậu Tuất/Kỷ Hợi = Bình Địa Mộc → MỘC TAM CỤC.

 (2) MƯỜI HAI CUNG đi NGHỊCH địa chi từ cung Mệnh:
     Mệnh → Huynh Đệ → Phu Thê → Tử Tức → Tài Bạch → Tật Ách → Thiên Di
     → Nô Bộc → Quan Lộc → Điền Trạch → Phúc Đức → Phụ Mẫu.
     (《Bí Nghi》ví dụ Mệnh Bính Tý: Huynh Đệ ở Ất Hợi, Phụ Mẫu ở Đinh Sửu.)
"""

CHI = ["Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi","Thân","Dậu","Tuất","Hợi"]
CAN = ["Giáp","Ất","Bính","Đinh","Mậu","Kỷ","Canh","Tân","Nhâm","Quý"]
IDX = {c: i for i, c in enumerate(CHI)}

# ============================ DỮ LIỆU SINH ============================
NAM_CAN, NAM_CHI = "Bính", "Tý"
THANG, NGAY, GIO = 10, 1, "Tý"
DUONG_NAM = True                       # Bính = dương can

# ======================= 1. NẠP ÂM 60 GIÁP TÝ ========================
NAP_AM = [
 "Hải Trung Kim","Lô Trung Hỏa","Đại Lâm Mộc","Lộ Bàng Thổ","Kiếm Phong Kim","Sơn Đầu Hỏa",
 "Giản Hạ Thủy","Thành Đầu Thổ","Bạch Lạp Kim","Dương Liễu Mộc","Tuyền Trung Thủy","Ốc Thượng Thổ",
 "Tích Lịch Hỏa","Tùng Bách Mộc","Trường Lưu Thủy","Sa Trung Kim","Sơn Hạ Hỏa","Bình Địa Mộc",
 "Bích Thượng Thổ","Kim Bạch Kim","Phúc Đăng Hỏa","Thiên Hà Thủy","Đại Dịch Thổ","Thoa Xuyến Kim",
 "Tang Đố Mộc","Đại Khê Thủy","Sa Trung Thổ","Thiên Thượng Hỏa","Thạch Lựu Mộc","Đại Hải Thủy"]
def giap_ty_index(can, chi):
    """Số thứ tự 0..59 của can chi."""
    for n in range(60):
        if n % 10 == CAN.index(can) and n % 12 == IDX[chi]:
            return n
def nap_am(can, chi): return NAP_AM[giap_ty_index(can, chi) // 2]

NGU_HANH = {"Kim":4, "Mộc":3, "Thủy":2, "Hỏa":6, "Thổ":5}
TEN_CUC  = {2:"Thủy Nhị Cục", 3:"Mộc Tam Cục", 4:"Kim Tứ Cục", 5:"Thổ Ngũ Cục", 6:"Hỏa Lục Cục"}

# ==================== 2. MỆNH CUNG / THÂN CUNG =======================
cung_thang = (IDX["Dần"] + (THANG - 1)) % 12
MENH = (cung_thang - IDX[GIO]) % 12          # thuận tới tháng, rồi nghịch tới giờ
THAN = (cung_thang + IDX[GIO]) % 12          # thuận tới tháng, rồi thuận tới giờ

# ==================== 3. CAN 12 CUNG (ngũ hổ độn) ====================
CAN_DAU = {"Giáp":"Bính","Ất":"Mậu","Bính":"Canh","Đinh":"Nhâm","Mậu":"Giáp",
           "Kỷ":"Bính","Canh":"Mậu","Tân":"Canh","Nhâm":"Nhâm","Quý":"Giáp"}[NAM_CAN]
def can_cung(chi):
    return CAN[(CAN.index(CAN_DAU) + ((IDX[chi] - 2) % 12)) % 10]

# ======================= 4. NGŨ HÀNH CỤC =============================
CAN_MENH = can_cung(CHI[MENH])
NAP_AM_MENH = nap_am(CAN_MENH, CHI[MENH])
HANH = NAP_AM_MENH[-3:] if NAP_AM_MENH.endswith(("Kim","Mộc")) else NAP_AM_MENH[-2:]
for h in ("Kim","Mộc","Thủy","Hỏa","Thổ"):
    if NAP_AM_MENH.endswith(h): HANH = h; break
CUC = NGU_HANH[HANH]

# ========================== 5. TỬ VI ================================
def vi_tri_tu_vi(ngay, cuc):
    k = 0
    while (ngay + k) % cuc: k += 1
    q = (ngay + k) // cuc
    p = (IDX["Dần"] + (q - 1)) % 12
    return (p + k) % 12 if k % 2 == 0 else (p - k) % 12
TU_VI = vi_tri_tu_vi(NGAY, CUC)
THIEN_PHU = (IDX["Dần"] + (IDX["Dần"] - TU_VI)) % 12      # đối xứng qua trục Dần–Thân

# ======================= 6. 14 CHÍNH TINH ===========================
SAO = {c: {"chinh": [], "phu": []} for c in CHI}
for s, o in {"Tử Vi":0,"Thiên Cơ":1,"Thái Dương":3,"Vũ Khúc":4,"Thiên Đồng":5,"Liêm Trinh":8}.items():
    SAO[CHI[(TU_VI - o) % 12]]["chinh"].append(s)
for s, o in {"Thiên Phủ":0,"Thái Âm":1,"Tham Lang":2,"Cự Môn":3,"Thiên Tướng":4,
             "Thiên Lương":5,"Thất Sát":6,"Phá Quân":10}.items():
    SAO[CHI[(THIEN_PHU + o) % 12]]["chinh"].append(s)

# ======================== 7. PHỤ TINH ===============================
ta    = (IDX["Thìn"] + (THANG - 1)) % 12                 # Tả Phù: Thìn khởi giêng thuận
huu   = (IDX["Tuất"] - (THANG - 1)) % 12                 # Hữu Bật: Tuất khởi giêng nghịch
xuong = (IDX["Tuất"] - IDX[GIO]) % 12                    # Văn Xương: Tuất khởi Tý giờ nghịch
khuc  = (IDX["Thìn"] + IDX[GIO]) % 12                    # Văn Khúc: Thìn khởi Tý giờ thuận
tam   = (ta  + (NGAY - 1)) % 12                          # Tam Thai: Tả Phù + (ngày-1)
bat   = (huu - (NGAY - 1)) % 12                          # Bát Tọa: Hữu Bật - (ngày-1)
aq    = (xuong + (NGAY - 1) - 1) % 12                    # Ân Quang: Văn Xương + (ngày-1) - 1
tq    = (khuc  + (NGAY - 1) - 1) % 12                    # Thiên Quý: Văn Khúc + (ngày-1) - 1
giai  = (IDX["Mùi"] + (THANG - 1)) % 12                  # Giải Thần: Mùi khởi giêng thuận
khoi  = {"Giáp":"Sửu","Ất":"Tý","Bính":"Hợi","Đinh":"Hợi","Mậu":"Sửu","Kỷ":"Tý",
         "Canh":"Sửu","Tân":"Dần","Nhâm":"Mão","Quý":"Mão"}[NAM_CAN]
viet  = {"Giáp":"Mùi","Ất":"Thân","Bính":"Dậu","Đinh":"Dậu","Mậu":"Mùi","Kỷ":"Thân",
         "Canh":"Mùi","Tân":"Ngọ","Nhâm":"Tỵ","Quý":"Tỵ"}[NAM_CAN]
loc   = {"Giáp":"Dần","Ất":"Mão","Bính":"Tỵ","Đinh":"Ngọ","Mậu":"Tỵ","Kỷ":"Ngọ",
         "Canh":"Thân","Tân":"Dậu","Nhâm":"Hợi","Quý":"Tý"}[NAM_CAN]
kinh, da = (IDX[loc] + 1) % 12, (IDX[loc] - 1) % 12
TAM_HOP = {"Thân":"Dần","Tý":"Dần","Thìn":"Dần","Dần":"Thân","Ngọ":"Thân","Tuất":"Thân",
           "Tỵ":"Hợi","Dậu":"Hợi","Sửu":"Hợi","Hợi":"Tỵ","Mão":"Tỵ","Mùi":"Tỵ"}
ma    = TAM_HOP[NAM_CHI]
dao   = {"Thân":"Dậu","Tý":"Dậu","Thìn":"Dậu","Dần":"Mão","Ngọ":"Mão","Tuất":"Mão",
         "Tỵ":"Ngọ","Dậu":"Ngọ","Sửu":"Ngọ","Hợi":"Tý","Mão":"Tý","Mùi":"Tý"}[NAM_CHI]
hong  = (IDX["Mão"] - IDX[NAM_CHI]) % 12
hy    = (hong + 6) % 12
dieu  = (IDX["Sửu"] + (THANG - 1)) % 12
hinh  = (IDX["Dậu"] + (THANG - 1)) % 12
khoc  = (IDX["Ngọ"] - IDX[NAM_CHI]) % 12
hu    = (IDX["Ngọ"] + IDX[NAM_CHI]) % 12
long  = (IDX["Thìn"] + IDX[NAM_CHI]) % 12
phuong= (IDX["Tuất"] - IDX[NAM_CHI]) % 12
hoah  = {"Thân":"Dần","Tý":"Dần","Thìn":"Dần","Dần":"Sửu","Ngọ":"Sửu","Tuất":"Sửu",
         "Tỵ":"Mão","Dậu":"Mão","Sửu":"Mão","Hợi":"Dậu","Mão":"Dậu","Mùi":"Dậu"}[NAM_CHI]
holo  = {"Thân":"Tuất","Tý":"Tuất","Thìn":"Tuất","Dần":"Mão","Ngọ":"Mão","Tuất":"Mão",
         "Tỵ":"Tuất","Dậu":"Tuất","Sửu":"Tuất","Hợi":"Tuất","Mão":"Tuất","Mùi":"Tuất"}[NAM_CHI]
dkhong= (IDX["Hợi"] - IDX[GIO]) % 12
dkiep = (IDX["Hợi"] + IDX[GIO]) % 12
tkhong= (IDX[NAM_CHI] + 1) % 12
# ---- Tạp tinh: tra đúng bảng của iztro 2.5.0 (đã đối chiếu từng sao) ----
i_chi, i_can = IDX[NAM_CHI], CAN.index(NAM_CAN)
cogod = IDX[{"Dần":"Tỵ","Mão":"Tỵ","Thìn":"Tỵ","Tỵ":"Thân","Ngọ":"Thân","Mùi":"Thân",
             "Thân":"Hợi","Dậu":"Hợi","Tuất":"Hợi","Hợi":"Dần","Tý":"Dần","Sửu":"Dần"}[NAM_CHI]]
quad  = IDX[{"Dần":"Sửu","Mão":"Sửu","Thìn":"Sửu","Tỵ":"Thìn","Ngọ":"Thìn","Mùi":"Thìn",
             "Thân":"Mùi","Dậu":"Mùi","Tuất":"Mùi","Hợi":"Tuất","Tý":"Tuất","Sửu":"Tuất"}[NAM_CHI]]
hoacai= IDX[{"Dần":"Tuất","Ngọ":"Tuất","Tuất":"Tuất","Thân":"Thìn","Tý":"Thìn","Thìn":"Thìn",
             "Tỵ":"Sửu","Dậu":"Sửu","Sửu":"Sửu","Hợi":"Mùi","Mùi":"Mùi","Mão":"Mùi"}[NAM_CHI]]
tquan = IDX[["Mùi","Thìn","Tỵ","Dần","Mão","Dậu","Hợi","Dậu","Tuất","Ngọ"][i_can]]
tphuc = IDX[["Dậu","Thân","Tý","Hợi","Mão","Dần","Ngọ","Tỵ","Ngọ","Tỵ"][i_can]]
ttru  = IDX[["Tỵ","Ngọ","Tý","Tỵ","Ngọ","Thân","Dần","Ngọ","Dậu","Hợi"][i_can]]
tduc  = (IDX["Dậu"] + i_chi) % 12
ngduc = (IDX["Tỵ"]  + i_chi) % 12
tkhg  = (i_chi + 1) % 12
phatoai = IDX[["Tỵ","Sửu","Dậu"][i_chi % 3]]
philiem = IDX[["Thân","Dậu","Tuất","Tỵ","Ngọ","Mùi","Dần","Mão","Thìn","Hợi","Tý","Sửu"][i_chi]]
ngiai   = IDX[["Tuất","Dậu","Thân","Mùi","Ngọ","Tỵ","Thìn","Mão","Dần","Sửu","Tý","Hợi"][i_chi]]
tvu     = IDX[["Tỵ","Thân","Dần","Hợi"][(THANG - 1) % 4]]
tnguyet = IDX[["Tuất","Tỵ","Thìn","Dần","Mùi","Mão","Hợi","Mùi","Dần","Ngọ","Tuất","Dần"][THANG - 1]]
amsat   = IDX[["Dần","Tý","Tuất","Thân","Ngọ","Thìn"][(THANG - 1) % 6]]
daiphu  = (IDX["Ngọ"] + (NGAY - 1)) % 12
phongcao= (IDX["Dần"] + (NGAY - 1)) % 12
# Tuần Không / Triệt Lộ / Không Vong
_tk = (i_chi + 9 - i_can + 1) % 12
if i_chi % 2 != _tk % 2: _tk = (_tk + 1) % 12
tuan_khong = CHI[_tk]                     # iztro báo một cung; cổ pháp phủ cả cặp (Thân–Dậu)
triet = IDX[["Thân","Ngọ","Thìn","Dần","Tý"][i_can % 5]]
khongvong = IDX[["Dậu","Mùi","Tỵ","Mão","Sửu"][i_can % 5]]

PHU = [("Tả Phù",ta),("Hữu Bật",huu),("Văn Xương",xuong),("Văn Khúc",khuc),
       ("Thiên Khôi",IDX[khoi]),("Thiên Việt",IDX[viet]),("Lộc Tồn",IDX[loc]),
       ("Kình Dương",kinh),("Đà La",da),("Thiên Mã",IDX[ma]),("Hàm Trì",IDX[dao]),
       ("Hồng Loan",hong),("Thiên Hỷ",hy),("Thiên Diêu",dieu),("Thiên Hình",hinh),
       ("Thiên Khốc",khoc),("Thiên Hư",hu),("Long Trì",long),("Phụng Các",phuong),
       ("Hỏa Tinh",IDX[hoah]),("Linh Tinh",IDX[holo]),
       ("Địa Không",dkhong),("Địa Kiếp",dkiep),("Thiên Không",tkhg),
       ("Tam Thai",tam),("Bát Tọa",bat),("Ân Quang",aq),("Thiên Quý",tq),
       ("Giải Thần",giai),("Cô Thần",cogod),("Quả Tú",quad),("Hoa Cái",hoacai),
       ("Thiên Quan",tquan),("Thiên Phúc",tphuc),("Thiên Trù",ttru),("Thiên Đức",tduc),
       ("Nguyệt Đức",ngduc),("Thiên Vu",tvu),("Thiên Nguyệt",tnguyet),("Âm Sát",amsat),
       ("Đài Phụ",daiphu),("Phong Cáo",phongcao),("Niên Giải",ngiai),
       ("Phi Liêm",philiem),("Phá Toái",phatoai),("Không Vong",khongvong),
       ("Triệt Lộ",triet),("Tuần Không",IDX[tuan_khong]),
       ("Thiên Tài",(MENH + i_chi) % 12),("Thiên Thọ",(THAN + i_chi) % 12)]
for ten, p in PHU:
    SAO[CHI[p]]["phu"].append(ten)

# ==================== 8. MƯỜI HAI CUNG ==============================
ORDER = ["Mệnh","Huynh Đệ","Phu Thê","Tử Tức","Tài Bạch","Tật Ách",
         "Thiên Di","Nô Bộc","Quan Lộc","Điền Trạch","Phúc Đức","Phụ Mẫu"]
CUNG = {}
for j, ten in enumerate(ORDER):
    c = CHI[(MENH - j) % 12]                     # mười hai cung đi NGHỊCH địa chi
    CUNG[c] = {"can": can_cung(c), "cung": ten, "chinh": SAO[c]["chinh"],
               "phu": SAO[c]["phu"], "han": ""}
CUNG[CHI[THAN]]["cung"] += "+Thân"
CUNG_CUA = {CUNG[c]["cung"].split("+")[0]: c for c in CUNG}
# Thiên Thương cư Nô Bộc, Thiên Sứ cư Tật Ách (cố định, không theo năm sinh).
# LƯU Ý: CUNG[c]["phu"] CHÍNH LÀ SAO[c]["phu"] (cùng một list) — chỉ append một lần.
SAO[CUNG_CUA["Nô Bộc"]]["phu"].append("Thiên Thương")
SAO[CUNG_CUA["Tật Ách"]]["phu"].append("Thiên Sứ")

# ==================== 9. ĐẠI HẠN ===================================
for k in range(12):
    c = CHI[(MENH + k) % 12] if DUONG_NAM else CHI[(MENH - k) % 12]
    a = CUC + k * 10
    CUNG[c]["han"] = f"{a}-{a+9}"

# ==================== 10. VÒNG TRÀNG SINH ==========================
VONG_TS = ["Tràng Sinh","Mộc Dục","Quan Đới","Lâm Quan","Đế Vượng","Suy",
           "Bệnh","Tử","Mộ","Tuyệt","Thai","Dưỡng"]
START_TS = {2: IDX["Thân"], 3: IDX["Hợi"], 4: IDX["Hợi"], 5: IDX["Thân"], 6: IDX["Dần"]}[CUC]
TRUONG = {}
for j, s in enumerate(VONG_TS):
    TRUONG[CHI[(START_TS + j) % 12] if DUONG_NAM else CHI[(START_TS - j) % 12]] = s

# ==================== 11. TỨ HÓA BẮC PHÁI ==========================
TH = {"Giáp":("Liêm Trinh","Phá Quân","Vũ Khúc","Thái Dương"),
      "Ất":("Thiên Cơ","Thiên Lương","Tử Vi","Thái Âm"),
      "Bính":("Thiên Đồng","Thiên Cơ","Văn Xương","Liêm Trinh"),
      "Đinh":("Thái Âm","Thiên Đồng","Thiên Cơ","Cự Môn"),
      "Mậu":("Tham Lang","Thái Âm","Hữu Bật","Thiên Cơ"),
      "Kỷ":("Vũ Khúc","Tham Lang","Thiên Lương","Văn Khúc"),
      "Canh":("Thái Dương","Vũ Khúc","Thái Âm","Thiên Đồng"),
      "Tân":("Cự Môn","Thái Dương","Văn Khúc","Văn Xương"),
      "Nhâm":("Thiên Lương","Tử Vi","Tả Phù","Vũ Khúc"),
      "Quý":("Phá Quân","Cự Môn","Thái Âm","Tham Lang")}
HOA = ["Lộc","Quyền","Khoa","Kỵ"]
POS = {}
for c in CHI:
    for s in SAO[c]["chinh"] + SAO[c]["phu"]:
        POS[s] = c
def hoa_cua(can):
    return {l: {"sao": s, "den": POS.get(s), "cung": CUNG[POS[s]]["cung"].split("+")[0] if s in POS else None}
            for l, s in zip(HOA, TH[can])}
SINH_NIEN = hoa_cua(NAM_CAN)

def tu_hoa_tu(cung_chi):
    can = can_cung(cung_chi)
    r = hoa_cua(can)
    for l in HOA: r[l]["tu"] = (r[l]["den"] == cung_chi)
    return can, r

def cung_vi(anchor):
    return {ORDER[j]: CHI[(IDX[anchor] - j) % 12] for j in range(12)}

# ==================== 12. ĐẨU QUÂN / LƯU NIÊN / LƯU NGUYỆT =========
def dau_quan(nam_chi, thang=THANG, gio=GIO):
    return ((IDX[nam_chi] - (thang - 1)) % 12 + IDX[gio]) % 12

if __name__ == "__main__":
    import sys
    print(f"Tứ trụ      : {NAM_CAN}{NAM_CHI} · Kỷ Hợi · Nhâm Tý · Canh Tý")
    print(f"Mệnh cung   : {CHI[MENH]} ({CAN_MENH})   Thân cung: {CHI[THAN]}  {'(đồng cung)' if MENH==THAN else ''}")
    print(f"Nạp âm Mệnh : {CAN_MENH}{CHI[MENH]} = {NAP_AM_MENH}  →  {TEN_CUC[CUC]}")
    print(f"Tử Vi       : {CHI[TU_VI]}     Thiên Phủ: {CHI[THIEN_PHU]}")
    print(f"Tuần Không  : {tuan_khong}  (cổ pháp phủ cặp Thân–Dậu)    Triệt Lộ: {CHI[triet]}")
    print("\nSINH NIÊN TỨ HÓA (can %s):" % NAM_CAN)
    for l in HOA:
        print(f"   {SINH_NIEN[l]['sao']:10s} hóa {l:5s} → {SINH_NIEN[l]['den']} ({SINH_NIEN[l]['cung']})")
    print("\n%-22s %-11s %s" % ("CUNG","ĐẠI HẠN","SAO"))
    for j, t in enumerate(ORDER):
        c = CUNG_CUA[t]
        print(f"  {CUNG[c]['can']}{c}  {CUNG[c]['cung']:12s} {CUNG[c]['han']:9s} "
              f"{TRUONG[c]:10s} chính: {', '.join(CUNG[c]['chinh']) or '—'}")
        if CUNG[c]["phu"]:
            print(f"  {'':22s} {'':9s} {'':10s} phụ  : {', '.join(CUNG[c]['phu'])}")
    print("\nPHI TINH 12 CUNG")
    for t in ORDER:
        c = CUNG_CUA[t]; can, r = tu_hoa_tu(c)
        print(f"  {t:10s} {can}{c}: " + "  ".join(
            f"{h['sao']}{l}→{h['den']}({h['cung']}){'↺' if h['tu'] else ''}" for l, h in r.items()))

def in_dai_han():
    print("\n" + "="*78); print("ĐẠI HẠN (Mộc Tam Cục, dương nam thuận hành)"); print("="*78)
    for k in range(12):
        c = CHI[(MENH + k) % 12]
        can, r = tu_hoa_tu(c); cv = cung_vi(c)
        print(f"\n{CUNG[c]['han']:>9}  {can}{c}  ({1996+int(CUNG[c]['han'].split('-')[0])-1}"
              f"–{1996+int(CUNG[c]['han'].split('-')[1])-1})  bản mệnh: {CUNG[c]['cung'].split('+')[0]}")
        print("           " + "  ".join(f"{h['sao']}{l}→{h['den']}({h['cung'].split('+')[0]}){'↺' if h['tu'] else ''}" for l,h in r.items()))
        print("           " + " · ".join(f"{t}={cv[t]}" for t in ["Mệnh","Tài Bạch","Quan Lộc","Điền Trạch","Phu Thê","Tử Tức","Phụ Mẫu","Tật Ách"]))

def in_luu_nien(nam):
    ychi = CHI[(nam - 1984) % 12]; ycan = CAN[(nam - 1984) % 10]
    cv = cung_vi(ychi); dq = dau_quan(ychi); r = hoa_cua(ycan)   # TỨ HÓA THEO CAN NĂM
    print(f"\n### {nam} {ycan}{ychi} — tuổi mụ {nam-1995}   (can năm {ycan}: "
          + " · ".join(f"{s_} {l}" for l, s_ in zip(HOA, TH[ycan])) + ")")
    print("  Đẩu quân:", CHI[dq], f"({can_cung(CHI[dq])}{CHI[dq]})", "| Thiên Di mượn:", CHI[(dq+6)%12])
    for l in HOA:
        ln = [t for t in ORDER if cv[t] == r[l]["den"]][0]
        print(f"  Lưu niên {r[l]['sao']:10s} hóa {l:5s} → {r[l]['den']}  = lưu niên {ln:9s} | bản mệnh {CUNG[r[l]['den']]['cung'].split('+')[0]}")
        if r[l]["den"] == CHI[dq]: print("       ^ rơi đúng cung Đẩu quân")
    dqc = can_cung(CHI[dq]); tdi = CHI[(dq + 6) % 12]; tdic = can_cung(tdi)
    print(f"  Tứ hóa ĐẨU QUÂN ({dqc}{CHI[dq]}): " + "  ".join(
        f"{x}{l}→{POS[x]}{'  ★KỴ THẬT' if l=='Kỵ' and POS[x]==ychi else ''}" for l, x in zip(HOA, TH[dqc])))
    print(f"  Tứ hóa THIÊN DI MƯỢN ({tdic}{tdi}): " + "  ".join(
        f"{x}{l}→{POS[x]}" for l, x in zip(HOA, TH[tdic])))
    print("  Lưu nguyệt (khởi đẩu quân, thuận): " + ", ".join(f"{m}={CHI[(dq+m-1)%12]}" for m in range(1,13)))
    return cv, dq, r
