#!/usr/bin/env python3
"""Render the sample verdicts in skills/tayyib/examples/{ar,en}/ to docs/samples/{ar,en}/*.pdf.
Needs python-markdown and Google Chrome. Run from the repo root."""
import glob, os, re, subprocess, sys, pathlib
try:
    import markdown
except ImportError:
    sys.exit("pip install markdown")
ROOT = pathlib.Path(__file__).resolve().parents[2]
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Aref+Ruqaa:wght@400;700&family=IBM+Plex+Sans+Arabic:wght@400;500;600&family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">'
CSS = {
 "en": '''@page{size:A4;margin:22mm 20mm 26mm}body{font-family:"Source Serif 4",Georgia,serif;font-size:10.5pt;line-height:1.5;color:#142420}
h1{font-family:"Bricolage Grotesque",Arial,sans-serif;font-size:19pt;margin:0 0 4pt;border-bottom:2px solid #142420;padding-bottom:6pt}
h2{font-family:"Bricolage Grotesque",Arial,sans-serif;font-size:13pt;margin:16pt 0 4pt;page-break-after:avoid}
table{font-family:"Bricolage Grotesque",Arial,sans-serif}''',
 "ar": '''@page{size:A4;margin:22mm 20mm 26mm}body{font-family:"IBM Plex Sans Arabic","Noto Naskh Arabic",Tahoma,sans-serif;font-size:11pt;line-height:1.75;color:#142420;direction:rtl;text-align:right}
h1{font-family:"IBM Plex Sans Arabic",Tahoma,sans-serif;font-size:18pt;margin:0 0 4pt;border-bottom:2px solid #142420;padding-bottom:6pt}
h2{font-family:"IBM Plex Sans Arabic",Tahoma,sans-serif;font-size:13pt;margin:16pt 0 4pt;page-break-after:avoid}
table{font-family:"IBM Plex Sans Arabic",Tahoma,sans-serif}th,td{text-align:right;padding:4pt 0 4pt 6pt}a{direction:ltr;unicode-bidi:embed}'''
}
COMMON = '''p{margin:0 0 7pt}a{color:#0f4c75;text-decoration:none}table{width:100%;border-collapse:collapse;font-size:9pt;margin:4pt 0 8pt}
tr{page-break-inside:avoid}th,td{text-align:left;vertical-align:top;padding:4pt 6pt 4pt 0;border-bottom:1px solid #d5dcd7}th{color:#5a6a63;font-weight:500;border-bottom:1px solid #142420}
li{margin:2pt 0}sup{font-size:7pt;color:#b4761a;font-family:Arial,sans-serif;margin:0 1px}.stamp{display:inline-block;border:2px solid #1f6f4a;color:#1f6f4a;border-radius:5px;padding:2pt 8pt;font-weight:700}
.fm{font-family:ui-monospace,Menlo,monospace;font-size:8pt;color:#5a6a63;background:#eef1ee;padding:6pt 8pt;border-radius:4px;direction:ltr;text-align:left;white-space:pre-wrap;margin:0 0 10pt}
.end{font-size:8.5pt;color:#5a6a63;border-top:1px solid #d5dcd7;margin-top:18pt;padding-top:6pt}ul{padding-inline-start:16pt}li b{color:#b4761a}'''
tmp = pathlib.Path(os.environ.get("TMPDIR", "/tmp")) / "tayyib-samples"; tmp.mkdir(exist_ok=True)
for lang in ("ar", "en"):
    out = ROOT / "docs" / "samples" / lang; out.mkdir(parents=True, exist_ok=True)
    for md in sorted(glob.glob(str(ROOT / f"skills/tayyib/examples/{lang}/*.md"))):
        text = pathlib.Path(md).read_text()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        front, body = (m.group(1), m.group(2)) if m else ("", text)
        body = re.sub(r"^\[\^(\d+)\]: (.*?)(https?://\S+)\s*$", r"- **\1** \2[\3](\3)", body, flags=re.M)
        body = re.sub(r"\[\^(\d+)\]", r"<sup>\1</sup>", body)
        html_body = markdown.markdown(body, extensions=["tables"])
        html_body = re.sub(r"<p>(Verdict:|الحكم:)\s*(.*?)</p>", r'<p><span class="stamp">\1 \2</span></p>', html_body)
        name = pathlib.Path(md).stem
        end = "طيّب، حكم نموذجي. me2resh.github.io/tayyib" if lang == "ar" else "Tayyib, sample verdict. me2resh.github.io/tayyib"
        html = f'<!doctype html><html lang="{lang}" dir="{"rtl" if lang=="ar" else "ltr"}"><head><meta charset="utf-8">{FONTS}<style>{CSS[lang]}{COMMON}</style></head><body><div class="fm">{front}</div>{html_body}<p class="end">{end}</p></body></html>'
        hp = tmp / f"{lang}-{name}.html"; hp.write_text(html)
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                        f"--print-to-pdf={out / (name + '.pdf')}", f"file://{hp}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        print("built", out / (name + ".pdf"))
