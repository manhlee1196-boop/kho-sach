# -*- coding: utf-8 -*-
"""
Tạo hai file HTML từ lap-la-so.py + LUAN-GIAI.md:
    lá-số-tử-vi.html          bàn đồ 12 cung
    luận-giải-lá-số.html      bản luận giải + bàn đồ

Chạy:  python tao-html.py      (cần:  pip install markdown)
"""
import html, os, runpy

HERE = os.path.dirname(os.path.abspath(__file__))
G = runpy.run_path(os.path.join(HERE, "lap-la-so.py"), run_name="taohtml")
CHI, IDX, CUNG, SAO = G["CHI"], G["IDX"], G["CUNG"], G["SAO"]
CUNG_CUA, ORDER = G["CUNG_CUA"], G["ORDER"]
MENH, THAN, CUC, TU_VI = G["MENH"], G["THAN"], G["CUC"], G["TU_VI"]
SN, HOA, POS = G["SINH_NIEN"], G["HOA"], G["POS"]
TH, TRUONG, tuan_khong = G["TH"], G["TRUONG"], G["tuan_khong"]
tu_hoa_tu, cung_vi = G["tu_hoa_tu"], G["cung_vi"]
CLS = {"Lộc": "loc", "Quyền": "quy", "Khoa": "khoa", "Kỵ": "ky"}

# sao nào mang tứ hóa bay vào từng cung
incoming = {c: {l: [] for l in CLS} for c in CHI}
for t in ORDER:
    c0 = CUNG_CUA[t]
    can, r = tu_hoa_tu(c0)
    for l in HOA:
        incoming[r[l]["den"]][l].append((t, r[l]["sao"], r[l]["tu"]))
SN_SAO = {l: SN[l]["sao"] for l in HOA}

# ============================== CSS ==============================
CSS = """
:root{--ink:#1d1b18;--red:#7a1f1f;--blue:#243b6b;--line:#d9cba6;--paper:#fffdf7}
*{box-sizing:border-box}
body{font-family:"Segoe UI",Roboto,"DejaVu Sans",Arial,sans-serif;margin:0;background:#f4f1ea;color:var(--ink);line-height:1.7}
.wrap{max-width:1760px;margin:0 auto;padding:24px}
h1{font-size:24px;color:var(--red);margin:0 0 4px;letter-spacing:.4px}
.sub{color:#6b5c40;font-size:13.5px;margin:0 0 18px}
table.board{border-collapse:collapse;width:100%;background:var(--paper);table-layout:fixed;box-shadow:0 2px 14px rgba(0,0,0,.08)}
table.board td{border:1.5px solid #b9a878;vertical-align:top;padding:7px 8px;height:210px;position:relative}
table.board td.mid{background:#fbf6e9;text-align:center;vertical-align:middle}
.hd{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px dotted #c9b888;padding-bottom:3px;margin-bottom:5px}
.can-chi{font-weight:700;font-size:15px;color:var(--blue);letter-spacing:.5px}
.han{font-size:10.5px;color:#8a7748;white-space:nowrap}
.cung{display:inline-block;margin:1px 4px 3px 0;padding:1px 7px;border-radius:9px;font-size:11.5px;font-weight:700;background:#efe3c6;color:#5c4a22}
.cung.menh{background:#7a1f1f;color:#fff}
.cung.than{background:#243b6b;color:#fff}
.cs{display:block;font-weight:700;font-size:14.5px;color:#2b2118;margin:1px 0}
.ps{display:inline-block;font-size:11.5px;color:#4a3f2c;margin:0 5px 1px 0}
.vcd{font-style:italic;font-size:11.5px;color:#9a8a63}
i.b{font-style:normal;font-size:9.5px;font-weight:700;padding:0 4px;border-radius:7px;margin-left:4px;vertical-align:2px;color:#fff}
i.b.loc{background:#1d7a3d} i.b.quy{background:#b5651d} i.b.khoa{background:#243b6b} i.b.ky{background:#a11212}
.fly{margin-top:6px;padding-top:5px;border-top:1px dotted #c9b888;font-size:10.5px;line-height:1.5}
.fly b{font-weight:700}
.fly .f-l{color:#1d7a3d} .fly .f-q{color:#b5651d} .fly .f-k{color:#243b6b} .fly .f-j{color:#a11212}
.fly .tu{font-weight:700;border-bottom:1.5px dotted currentColor}
.ts{position:absolute;left:8px;bottom:5px;font-size:10px;color:#a2906a}
.legend{max-width:1760px;margin:16px auto 0;padding:12px 16px;background:var(--paper);border:1px solid var(--line);font-size:12.5px;color:#4a3f2c}
.legend b{color:var(--red)}
.legend .row{margin:3px 0}
"""

DOC_CSS_EXTRA = """
.chartwrap{max-width:1760px;margin:0 auto;padding:22px 22px 6px}
.doc{max-width:1010px;margin:0 auto;padding:8px 26px 80px}
.doc h1{font-size:26px;color:var(--red);border-bottom:3px double var(--line);padding-bottom:10px;margin:34px 0 14px}
.doc h2{font-size:21px;color:var(--red);margin:38px 0 10px;border-bottom:1px solid var(--line);padding-bottom:6px}
.doc h3{font-size:17px;color:var(--blue);margin:28px 0 8px}
.doc h4{font-size:15px;color:#5b4a2f;margin:20px 0 6px}
.doc table{border-collapse:collapse;width:100%;margin:14px 0;font-size:13.5px;background:var(--paper);table-layout:auto;box-shadow:none}
.doc th,.doc td{border:1px solid var(--line);padding:7px 9px;vertical-align:top;text-align:left;height:auto;position:static}
.doc th{background:#f3ead6;font-weight:700}
.doc tr:nth-child(even) td{background:#fbf7ec}
.doc blockquote{margin:14px 0;padding:10px 16px;background:#fff8e6;border-left:4px solid #d4a017;font-size:14px;color:#4a3f2a;border-radius:0 4px 4px 0}
.doc blockquote p{margin:4px 0}
.doc code{background:#f0e9d8;padding:1px 5px;border-radius:3px;font-size:12.5px}
.doc pre{background:#2b2118;color:#f0e9d8;padding:14px 16px;border-radius:6px;overflow-x:auto;font-size:12.5px}
.doc pre code{background:none;color:inherit;padding:0}
.doc hr{border:0;border-top:1px solid var(--line);margin:28px 0}
.doc ul,.doc ol{padding-left:24px}
.doc li{margin:4px 0}
.doc strong{color:#5c1414}
.doc a{color:var(--blue)}
"""

# ============================== BÀN ĐỒ ==============================
# 4 hàng của bàn đồ truyền thống; ô giữa là khối 2x2 (colspan+rowspan)
LAYOUT = [
    ["Tỵ", "Ngọ", "Mùi", "Thân"],
    ["Thìn", "MID", "Dậu"],
    ["Mão", "Tuất"],
    ["Dần", "Sửu", "Tý", "Hợi"],
]
ATTR = {"MID": ' class="mid" colspan="2" rowspan="2"'}

MID = ("TỨ TRỤ & CĂN BẢN",
       ["<b>Bính Tý</b> · Kỷ Hợi · Nhâm Tý · Canh Tý",
        "Mệnh chủ <b>Cự Môn</b> · Thân chủ <b>Hỏa Tinh</b>",
        "Nạp âm cung Mệnh Kỷ Hợi = <i>Bình Địa Mộc</i>",
        f"<b>{G['TEN_CUC'][CUC].upper()}</b>",
        f"Tử Vi tại <b>{CHI[TU_VI]}</b> · Thiên Phủ tại <b>Tý</b>",
        f"Mệnh cung = Thân cung = <b>{CHI[MENH]}</b>",
        f"Tuần Không: <b>{tuan_khong}</b> (cổ pháp Thân–Dậu)",
        f"Triệt Lộ: <b>{CHI[G['triet']]}</b>",
        f"Dương nam · đại hạn thuận hành · khởi <b>tuổi {CUC}</b>"])

def badges(sao):
    return "".join(f'<i class="b {CLS[l]}">{l}</i>' for l in HOA if SN_SAO[l] == sao)

def cell(c):
    d = CUNG[c]
    ten = d["cung"].split("+")[0]
    lab = ""
    if ten == "Mệnh": lab += '<span class="cung menh">MỆNH</span>'
    else:             lab += f'<span class="cung">{ten}</span>'
    if "+" in d["cung"]: lab += '<span class="cung than">THÂN</span>'
    chinh = "".join(f'<span class="cs">{s}{badges(s)}</span>' for s in d["chinh"])
    if not chinh:
        doi = CHI[(IDX[c] + 6) % 12]
        muon = " + ".join(CUNG[doi]["chinh"]) or "—"
        chinh = f'<span class="vcd">vô chính diệu — tá {muon} ({doi})</span>'
    phu = "".join(f'<span class="ps">{s}{badges(s)}</span>' for s in d["phu"])
    fl = ""
    for l, k in [("Lộc","f-l"), ("Quyền","f-q"), ("Khoa","f-k"), ("Kỵ","f-j")]:
        for (src, sao, tu) in incoming[c][l]:
            fl += (f'<div class="{k}">{src} → <b>{sao} {l}</b>'
                   f'{" <span class=tu>tự hóa</span>" if tu else ""}</div>')
    return (f'<div class="hd"><span class="can-chi">{d["can"]}{c}</span>'
            f'<span class="han">ĐH {d["han"]}</span></div>{lab}{chinh}{phu}'
            f'<div class="fly">{fl}</div><div class="ts">{TRUONG[c]}</div>')

rows = []
for row in LAYOUT:
    tds = ""
    for c in row:
        if c == "MID":
            inner = "<b>" + MID[0] + "</b><br><br>" + "<br>".join(MID[1])
            tds += f"<td{ATTR['MID']}>{inner}</td>"
        else:
            tds += f"<td>{cell(c)}</td>"
    rows.append(f"<tr>{tds}</tr>")

BOARD = '<table class="board">' + "".join(rows) + "</table>"
LEGEND = f"""<div class="legend">
<div class="row"><b>Đọc bàn đồ:</b> mỗi ô = một cung. Đầu ô là <b>can chi</b> và <b>đại hạn</b> (ĐH). Sao đậm = chính tinh; nhãn màu = tứ hóa năm sinh
(<i class="b loc">Lộc</i> Thiên Đồng · <i class="b quy">Quyền</i> Thiên Cơ · <i class="b khoa">Khoa</i> Văn Xương · <i class="b ky">Kỵ</i> Liêm Trinh).</div>
<div class="row"><b>Khối dưới mỗi ô</b> = <b>tứ hóa phi tinh</b> bay vào cung đó, ghi rõ cung xuất phát. Chữ <span style="border-bottom:1.5px dotted">tự hóa</span> = sao hóa rơi lại chính cung xuất phát.</div>
<div class="row"><b>Góc trái dưới</b> = vòng Tràng Sinh (Mộc Tam Cục khởi Tràng Sinh tại Hợi, dương nam thuận hành).</div>
<div class="row"><b>Ô vô chính diệu</b> ghi rõ sao tá mượn từ đối cung.</div>
</div>"""

HEAD = ('<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        "<title>{t}</title><style>{c}</style></head><body>")

with open(os.path.join(HERE, "lá-số-tử-vi.html"), "w", encoding="utf-8") as f:
    f.write(HEAD.format(t="Lá số Tử Vi — nam, 1/10/1996 âm lịch giờ Tý", c=CSS))
    f.write('<div class="wrap">')
    f.write("<h1>LÁ SỐ TỬ VI — BẮC PHÁI TỨ HÓA PHI TINH</h1>")
    f.write('<p class="sub">NAM · 00:30 mùng 1 tháng 10 Bính Tý (âm lịch) = thứ Hai 11/11/1996 · giờ Tý &nbsp;|&nbsp; '
            "<b>Mộc Tam Cục</b> · Mệnh = Thân = Hợi · Tử Vi tại Thìn · <b>Thiên Đồng thủ Mệnh</b> "
            "&nbsp;|&nbsp; an số đã kiểm chứng với py-iztro 0.1.5 (<code>kiem-chung.py</code>: 141 ĐẠT / 0 LỖI)</p>")
    f.write(BOARD + LEGEND + "</div></body></html>")

# ======================= BẢN LUẬN GIẢI + BÀN ĐỒ =======================
try:
    import markdown
except ImportError:
    raise SystemExit("cần cài markdown:  pip install markdown")

md = open(os.path.join(HERE, "LUAN-GIAI.md"), encoding="utf-8").read()
body = markdown.markdown(md, extensions=["tables", "fenced_code", "toc", "sane_lists"],
                         extension_configs={"toc": {"toc_depth": "2-3"}})
with open(os.path.join(HERE, "luận-giải-lá-số.html"), "w", encoding="utf-8") as f:
    f.write(HEAD.format(t="Luận giải lá số Tử Vi — nam, 1/10/1996 âm lịch giờ Tý",
                        c=CSS + DOC_CSS_EXTRA))
    f.write('<div class="chartwrap"><h1>LÁ SỐ</h1>')
    f.write('<p class="sub">NAM · 00:30 mùng 1 tháng 10 Bính Tý (âm lịch) = thứ Hai 11/11/1996 · giờ Tý &nbsp;|&nbsp; '
            "<b>Mộc Tam Cục</b> · Mệnh = Thân = Hợi · Tử Vi tại Thìn · <b>Thiên Đồng thủ Mệnh</b></p>")
    f.write(BOARD + LEGEND + "</div>")
    f.write('<div class="doc">' + body + "</div></body></html>")

print("đã tạo:  lá-số-tử-vi.html")
print("đã tạo:  luận-giải-lá-số.html")
