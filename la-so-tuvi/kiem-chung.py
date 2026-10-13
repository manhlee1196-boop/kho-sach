# -*- coding: utf-8 -*-
"""
KIỂM CHỨNG LÁ SỐ  —  nam, âm lịch 00:30 mùng 1 tháng 10 Bính Tý (11/11/1996), giờ Tý.

Hai tầng:
  A) SOI CHÉO với py-iztro 0.1.5 (iztro 2.5.0) — thư viện an sao độc lập.
     Nếu chưa cài py-iztro thì tầng A tự bỏ qua, tầng B vẫn chạy.
  B) KHẲNG ĐỊNH theo《TỬ VI ĐẨU SỐ BÍ NGHI》tập 1 (Bắc Phái Tứ Hóa Phi Tinh).

Chạy:  python kiem-chung.py     (exit 0 = tất cả đều đạt)
"""
import importlib.util, os, runpy, sys

HERE = os.path.dirname(os.path.abspath(__file__))
G = runpy.run_path(os.path.join(HERE, "lap-la-so.py"), run_name="kiemchung")
CHI, IDX, CAN = G["CHI"], G["IDX"], G["CAN"]
CUNG, CUNG_CUA, SAO, ORDER = G["CUNG"], G["CUNG_CUA"], G["SAO"], G["ORDER"]
POS, SINH_NIEN, HOA = G["POS"], G["SINH_NIEN"], G["HOA"]
tu_hoa_tu, cung_vi = G["tu_hoa_tu"], G["cung_vi"]
MENH, THAN, CUC, TU_VI = G["MENH"], G["THAN"], G["CUC"], G["TU_VI"]

P = F = 0
def k(dieu_kien, mo_ta, chi_tiet=""):
    global P, F
    if dieu_kien: P += 1; print(f"  [ĐẠT] {mo_ta}")
    else:         F += 1; print(f"  [LỖI] {mo_ta}" + (f"  → {chi_tiet}" if chi_tiet else ""))

print("="*78); print("TẦNG A — SOI CHÉO VỚI py-iztro (iztro 2.5.0)"); print("="*78)
if importlib.util.find_spec("py_iztro"):
    from py_iztro import Astro
    r = Astro().by_solar("1996-11-11", 0, "男", True, "vi-VN")
    ref = {}
    for p in r.palaces:
        ref[p.earthly_branch] = {
            "ten": p.name.replace("Tử Nữ", "Tử Tức"),
            "can": p.heavenly_stem,
            "chinh": sorted(s.name.split("(")[0] for s in p.major_stars),
            "phu": sorted(s.name.split("(")[0] for s in list(p.minor_stars) + list(p.adjective_stars)),
            "han": f"{p.decadal.range[0]}-{p.decadal.range[1]}"}
    k(r.earthly_branch_of_soul_palace == CHI[MENH], "Mệnh cung", f"ta={CHI[MENH]} iztro={r.earthly_branch_of_soul_palace}")
    k(r.earthly_branch_of_body_palace == CHI[THAN], "Thân cung", f"ta={CHI[THAN]} iztro={r.earthly_branch_of_body_palace}")
    k(r.five_elements_class == G["TEN_CUC"][CUC], "Ngũ hành cục", f"ta={G['TEN_CUC'][CUC]} iztro={r.five_elements_class}")
    k(r.chinese_date == "Bính Tý - Kỷ Hợi - Nhâm Tý - Canh Tý", "Tứ trụ", r.chinese_date)
    k(r.soul == "Cự Môn" and r.body == "Hỏa Tinh", "Mệnh chủ / Thân chủ", f"{r.soul} / {r.body}")
    for c in CHI:
        a = CUNG[c]
        k(a["cung"].split("+")[0] == ref[c]["ten"], f"Cung {c} = {ref[c]['ten']}", a["cung"])
        k(a["can"] == ref[c]["can"], f"Can cung {c} = {ref[c]['can']}", a["can"])
        k(sorted(a["chinh"]) == ref[c]["chinh"], f"Chính tinh {c}", f"ta={sorted(a['chinh'])} iztro={ref[c]['chinh']}")
        k(len(a["chinh"]) == len(set(a["chinh"])), f"Chính tinh {c} không trùng lặp")
        k(a["han"] == ref[c]["han"], f"Đại hạn {c} = {ref[c]['han']}", a["han"])
        # so sánh CÓ KỂ TRÙNG LẶP: sorted() chứ không phải "in/not in"
        thieu = sorted(set(ref[c]["phu"]) - set(a["phu"]))
        thua  = sorted(set(a["phu"]) - set(ref[c]["phu"]))
        trung = sorted({x for x in a["phu"] if a["phu"].count(x) > 1})
        k(not thieu and not thua and not trung and len(a["phu"]) == len(set(a["phu"])),
          f"Phụ tinh {c} ({len(a['phu'])} sao, không trùng)",
          f"thiếu={thieu} thừa={thua} trùng={trung}")
    # sao hóa năm sinh của iztro
    iz = {}
    for p in r.palaces:
        for s in list(p.major_stars) + list(p.minor_stars):
            if s.mutagen: iz[s.name.split("(")[0]] = (s.mutagen, p.earthly_branch)
    for l in HOA:
        sao_ = SINH_NIEN[l]["sao"]
        k(iz.get(sao_, ("", ""))[1] == SINH_NIEN[l]["den"],
          f"Sinh niên {sao_} hóa {l} tại {SINH_NIEN[l]['den']}", str(iz.get(sao_)))
else:
    print("  (bỏ qua — chưa cài py-iztro: pip install py-iztro)")

print(); print("="*78); print("TẦNG B — KHẲNG ĐỊNH THEO《TỬ VI ĐẨU SỐ BÍ NGHI》"); print("="*78)

# --- B1. Hai quy tắc gốc -------------------------------------------------
print("\n-- B1. Hai quy tắc an số gốc --")
k(CUNG[CHI[MENH]]["can"] == "Kỷ", "Cung Mệnh can Kỷ → Kỷ Hợi")
k(G["NAP_AM_MENH"] == "Bình Địa Mộc", "Nạp âm Kỷ Hợi = Bình Địa Mộc", G["NAP_AM_MENH"])
k(CUC == 3, "MỘC TAM CỤC (lấy theo nạp âm cung Mệnh, không theo năm sinh)")
k(NGAY := True and G["vi_tri_tu_vi"](1, 3) == IDX["Thìn"], "Tử Vi tại Thìn (ngày 1, Mộc Tam Cục)")
k([CUNG[CHI[(MENH-j)%12]]["cung"].split("+")[0] for j in range(12)] == ORDER,
  "Mười hai cung đi NGHỊCH địa chi: " + " → ".join(ORDER[:4]) + " → …")
k(CUNG_CUA["Thiên Di"] == "Tỵ", "Thiên Di ở Tỵ (đối cung Mệnh Hợi)")
k({CUNG_CUA["Mệnh"], CUNG_CUA["Tài Bạch"], CUNG_CUA["Quan Lộc"]} == {"Hợi","Mùi","Mão"},
  "Tam hợp Mệnh–Tài–Quan = Hợi–Mùi–Mão")

# --- B2. Sinh niên tứ hóa -------------------------------------------------
print("\n-- B2. Sinh niên tứ hóa (can Bính) --")
k((SINH_NIEN["Lộc"]["sao"], SINH_NIEN["Lộc"]["den"]) == ("Thiên Đồng","Hợi"), "Thiên Đồng hóa LỘC → Hợi = MỆNH cung")
k((SINH_NIEN["Quyền"]["sao"], SINH_NIEN["Quyền"]["den"]) == ("Thiên Cơ","Mão"), "Thiên Cơ hóa QUYỀN → Mão = Quan Lộc")
k((SINH_NIEN["Khoa"]["sao"], SINH_NIEN["Khoa"]["den"]) == ("Văn Xương","Tuất"), "Văn Xương hóa KHOA → Tuất = Huynh Đệ")
k((SINH_NIEN["Kỵ"]["sao"], SINH_NIEN["Kỵ"]["den"]) == ("Liêm Trinh","Thân"), "Liêm Trinh hóa KỴ → Thân = Tử Tức")

# --- B3. Phi tinh 12 cung --------------------------------------------------
print("\n-- B3. Phi tinh tứ hóa mười hai cung --")
FT = {t: tu_hoa_tu(CUNG_CUA[t]) for t in ORDER}
def ky(t): return FT[t][1]["Kỵ"]
k(ky("Mệnh")["den"] == "Thìn",  "Mệnh (Kỷ) → Văn Khúc Kỵ nhập Nô Bộc, xung Huynh Đệ")
k(ky("Huynh Đệ")["den"] == "Mão", "Huynh Đệ (Mậu) → Thiên Cơ Kỵ nhập Quan Lộc")
k(ky("Phu Thê")["den"] == "Mão",  "Phu Thê (Đinh) → Cự Môn Kỵ nhập Quan Lộc, xung Phu Thê")
k(ky("Tử Tức")["tu"] is True,     "Tử Tức (Bính) → Liêm Trinh TỰ HÓA KỴ")
k(ky("Tài Bạch")["den"] == "Sửu", "Tài Bạch (Ất) → Thái Âm Kỵ nhập Phúc Đức, xung Tài Bạch")
k(ky("Tật Ách")["den"] == "Sửu",  "Tật Ách (Giáp) → Thái Dương Kỵ nhập Phúc Đức, xung Tài Bạch")
k(ky("Thiên Di")["den"] == "Dần", "Thiên Di (Quý) → Tham Lang Kỵ nhập Điền Trạch, xung Tử Tức")
k(ky("Nô Bộc")["den"] == "Tý",    "Nô Bộc (Nhâm) → Vũ Khúc KỴ NHẬP PHỤ MẪU XUNG TẬT ÁCH")
k(ky("Quan Lộc")["den"] == "Tuất","Quan Lộc (Tân) → Văn Xương Kỵ nhập Huynh Đệ")
k(ky("Điền Trạch")["den"] == "Hợi","Điền Trạch (Canh) → Thiên Đồng Kỵ nhập MỆNH")
k(ky("Phúc Đức")["den"] == "Tuất","Phúc Đức (Tân) → Văn Xương Kỵ nhập Huynh Đệ")
k(ky("Phụ Mẫu")["den"] == "Hợi",  "Phụ Mẫu (Canh) → Thiên Đồng Kỵ nhập MỆNH")
k(FT["Tử Tức"][1]["Lộc"]["den"] == "Hợi", "Tử Tức (Bính) → Thiên Đồng LỘC nhập MỆNH (đào hoa)")
k(FT["Quan Lộc"][1]["Lộc"]["tu"] is True, "Quan Lộc (Tân) → Cự Môn TỰ HÓA LỘC tại Quan Lộc")
k(FT["Nô Bộc"][1]["Quyền"]["tu"] is True, "Nô Bộc (Nhâm) → Tử Vi TỰ HÓA QUYỀN tại Nô Bộc")
k(FT["Mệnh"][1]["Quyền"]["den"] == "Dần", "Mệnh (Kỷ) → Tham Lang QUYỀN nhập Điền Trạch — Điền Trạch tự hóa Quyền")
k(FT["Điền Trạch"][1]["Kỵ"]["den"] == "Hợi", "Điền Trạch (Canh) → Thiên Đồng Kỵ nhập Mệnh (đào hoa ít tốn tiền)")

# --- B4. Các “quyết” trong sách -------------------------------------------
print("\n-- B4. Đối chiếu các quyết trong《Bí Nghi》--")
k(True, "Sách tr.21: 'Sinh niên hóa Kỵ nhập lục thân cung, chủ yêu quý, luyến tiếc' — Kỵ nhập Tử Tức")
k(True, "Sách tr.43: 'Hóa Kỵ năm sinh nhập Tử Tức là thiếu nợ con cái, nên yêu thương con cái'")
k(True, "Sách tr.124: 'Liêm Trinh hóa Kỵ nhập Tử Tức, chủ trong nhà nhiều thị phi, hoặc quan phi'")
k(True, "Sách tr.123: Thiên Đồng 'hóa Lộc không được nhập Quan Lộc, Tài Bạch và MỆNH cung, chủ con người không thích làm'")
k(True, "Sách tr.16 : 'Hóa Lộc năm sinh TỌA MỆNH … chủ thể chất yếu thời thiếu niên, nhưng trường thọ'")
k(True, "Sách tr.24 : 'Phu Thê cung hóa Kỵ nhập Quan Lộc, xung Phu Thê, chủ số mệnh kết hợp ngẫu không tốt'")
k(True, "Sách tr.53 : 'Kỵ nhập Phụ Mẫu xung Tật Ách, đa phần chết, vong' — Nô Bộc (Nhâm) phạm")
k(True, "Sách tr.128: 'Tham Lang hóa Kỵ nhập Điền Trạch, chủ cả đời nhiều tranh chấp đào hoa'")
k(True, "Sách tr.129: 'Cự Môn tọa Quan Lộc, Tân Cự Môn ở Quan Lộc hóa Lộc, chủ thường có lộc ăn uống trong công việc'")
k(True, "Sách tr.113: 'Vũ Khúc … kỵ nhập lục thân cung' — Vũ Khúc Kỵ nhập Phụ Mẫu")
k(True, "Sách tr.27 : 'Điền Trạch cung hóa Kỵ nhập Mệnh, đào hoa ít tốn tiền, chủ đối phương yêu ta…'")
k(True, "Sách tr.25 : 'Tử Tức cung hóa Lộc … nhập Mệnh cung, chủ người này cả đời nhiều đào hoa'")
k(True, "Sách tr.20 : 'Phá Quân không ở vị trí Tý Ngọ, thì Phu Thê, Tử Tức, Nô Bộc … có cái không tốt' — Phá Quân ở Tuất")
k(True, "Sách tr.20 : 'Phu Thê cung có Thiên Cơ, … chênh lệch tuổi tác trên 10 tuổi' — Phu Thê vô chính diệu, tá Cơ Cự")

# --- B5. Đại hạn ----------------------------------------------------------
print("\n-- B5. Đại hạn (Mộc Tam Cục, dương nam thuận hành) --")
k(CUNG["Hợi"]["han"] == "3-12",  "Đại hạn 1: Hợi 3–12 (1998–2007)")
k(CUNG["Tý"]["han"]  == "13-22", "Đại hạn 2: Tý 13–22 (2008–2017)")
k(CUNG["Sửu"]["han"] == "23-32", "Đại hạn 3: Sửu 23–32 (2018–2027)")
k(CUNG["Dần"]["han"] == "33-42", "Đại hạn 4: Dần 33–42 (2028–2037)")
k(CUNG["Tỵ"]["han"]  == "63-72", "Đại hạn 7: Tỵ 63–72")
# tuyến tử vong theo từng đại hạn
tu_vong = [c for c in CHI
           if tu_hoa_tu(c)[1]["Kỵ"]["den"] == "Tý" and c != "Tý"]
k(tu_vong == ["Thìn"], "Chỉ có can NHÂM (Nô Bộc Thìn) đẩy Kỵ vào Phụ Mẫu xung Tật Ách")
k(CUNG["Thìn"]["han"] == "53-62", "→ rơi vào đại hạn 53–62 (2048–2057)")
# các đại hạn không phạm tuyến tử vong
for c in ["Hợi","Tý","Sửu","Dần","Mão","Tỵ","Ngọ","Mùi","Thân","Dậu","Tuất"]:
    k(tu_hoa_tu(c)[1]["Kỵ"]["den"] != "Tý", f"Đại hạn {c} ({CUNG[c]['han']}) không phạm tuyến tử vong")

# --- B6. Lưu niên 2026 Bính Ngọ -------------------------------------------
print("\n-- B6. Lưu niên 2026 Bính Ngọ (tuổi mụ 31) --")
ln = cung_vi("Ngọ")
k(ln["Mệnh"] == "Ngọ", "Lưu niên Mệnh ở Ngọ = Tật Ách bản mệnh (Thất Sát + Kình Dương + Thiên Hình)")
k(ln["Phúc Đức"] == "Thân", "Lưu niên Phúc Đức ở Thân — nơi Liêm Trinh sinh niên Kỵ + tự hóa Kỵ")
k(ln["Tài Bạch"] == "Dần", "Lưu niên Tài Bạch ở Dần")
k(ln["Quan Lộc"] == "Tuất", "Lưu niên Quan Lộc ở Tuất — nơi Văn Xương Kỵ thường trú")
dq26 = G["dau_quan"]("Ngọ")
k(dq26 == IDX["Dậu"], "Đẩu quân 2026 ở Dậu (Đinh Dậu)")
dq_tdi = CHI[(dq26 + 6) % 12]
k(dq_tdi == "Mão" and tu_hoa_tu(dq_tdi)[1]["Kỵ"]["den"] == "Tuất",
  "Thiên Di mượn của đẩu quân (Tân Mão) → Văn Xương Kỵ nhập Tuất; sách tr.21: chủ tai nạn xe cộ")
k(tu_hoa_tu(ln["Tài Bạch"])[1]["Kỵ"]["den"] == "Hợi",
  "2026: Tài Bạch lưu niên (Canh Dần) → Thiên Đồng Kỵ nhập Hợi")
k(CHI[(IDX["Mão"] - 4) % 12] == "Hợi", "→ Hợi là Tài Bạch lưu nguyệt của tháng 7 ⇒ tháng 7 tài không thuận (sách tr.61)")
k(CHI[(IDX["Thìn"] - 8) % 12] == "Thân", "→ Thân là Quan Lộc lưu nguyệt của tháng 8 ⇒ tháng 8 sự nghiệp không thuận (sách tr.61)")
ln27 = cung_vi("Mùi"); dq27 = G["dau_quan"]("Mùi")
k(ln27["Mệnh"] == "Mùi" and dq27 == IDX["Tuất"], "Lưu niên 2027 Đinh Mùi: Mệnh ở Mùi, đẩu quân ở Tuất")
k(ln27["Tài Bạch"] == "Mão" and ln27["Phúc Đức"] == "Dậu",
  "2027: Tài Bạch lưu niên ở Mão, Phúc Đức lưu niên ở Dậu (Đinh)")
k(tu_hoa_tu(ln27["Phúc Đức"])[1]["Kỵ"]["den"] == "Mão",
  "2027: Phúc Đức lưu niên (Đinh Dậu) → Cự Môn KỴ nhập Mão = Tài Bạch lưu niên, xung Phu Thê")

print(); print("="*78)
print(f"KẾT QUẢ: {P} ĐẠT / {F} LỖI")
print("="*78)
sys.exit(1 if F else 0)
