#!/usr/bin/env python3
"""Check a Tayyib verdict file against references/outputs.md. Exit 1 on any failure.
Usage: python3 check_verdict.py <verdict.md>"""
import re, sys, pathlib

EN = ["The verdict in one paragraph", "Core business", "Ratios", "Sources and agreement", "Reasoning", "Purification", "Re-screen", "Sources"]
AR = ["الحكم في فقرة واحدة", "النشاط الأساسي", "النسب المالية", "المصادر واتفاقها", "التعليل", "التطهير", "إعادة الفحص", "المصادر"]
VERDICT_WORD = {"CLEAN": ("CLEAN", "نظيف"), "BORDERLINE": ("BORDERLINE", "على الحد"), "FAIL": ("FAIL", "غير جائز")}

def check_block(block, idx, fails, warns):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", block, re.S)
    if not m:
        fails.append(f"block {idx}: front block missing or malformed"); return
    fm = dict(l.split(":", 1) for l in m.group(1).splitlines() if ":" in l)
    fm = {k.strip(): v.strip() for k, v in fm.items()}
    body = m.group(2)
    for k in ["tayyib", "name", "type", "language", "screened", "verdict", "sources_read", "sources_agree", "rescreen"]:
        if k not in fm: fails.append(f"block {idx}: front block missing '{k}'")
    lang = fm.get("language"); verdict = fm.get("verdict")
    if lang not in ("ar", "en"): fails.append(f"block {idx}: language must be ar or en")
    if verdict not in VERDICT_WORD: fails.append(f"block {idx}: verdict must be CLEAN, BORDERLINE or FAIL")
    if fm.get("type") not in ("stock", "fund", "cash", "wrapper", "employer", "other"): fails.append(f"block {idx}: type not recognised")
    if not re.match(r"\d{4}-\d{2}-\d{2}$", fm.get("screened", "")): fails.append(f"block {idx}: screened must be YYYY-MM-DD")
    # header verdict line
    want = VERDICT_WORD.get(verdict, ("", ""))[0 if lang == "en" else 1]
    head = "\n".join(body.splitlines()[:6])
    if want and want not in head: fails.append(f"block {idx}: header verdict line does not say {want}")
    # sections
    heads = [re.sub(r"^##\s*", "", l).strip() for l in body.splitlines() if re.match(r"^## ", l)]
    names = EN if lang == "en" else AR
    pos = -1
    for n, w in enumerate(names, 1):
        found = [i for i, h in enumerate(heads) if re.match(rf"^{n}\.\s*{re.escape(w)}\s*$", h)]
        if not found: fails.append(f"block {idx}: section missing or misnamed: '{n}. {w}'"); continue
        if found[0] < pos: fails.append(f"block {idx}: section out of order: '{n}. {w}'")
        pos = max(pos, found[0])
    # footnotes
    defined = set(re.findall(r"^\[\^(\d+)\]:", body, re.M)); used = set(re.findall(r"\[\^(\d+)\](?!:)", body))
    for f in sorted(used - defined, key=int): fails.append(f"block {idx}: footnote used but not defined: [^{f}]")
    for f in sorted(defined - used, key=int): warns.append(f"block {idx}: footnote defined but unused: [^{f}]")
    # marks: ✅ needs evidence on the line (outside the sources section)
    in_src = False
    for i, l in enumerate(body.splitlines(), 1):
        if re.match(r"^## 8\.", l): in_src = True
        if in_src or l.startswith("#") or not l.strip() or l.startswith("Verdict:") or l.startswith("الحكم:"): continue
        for mm in re.finditer("✅", l):
            if not re.search(r"\[\^\d+\]|\]\(https?://", l[mm.end():mm.end() + 160]): fails.append(f"block {idx} line {i}: ✅ without a footnote or link after it")
    # sources table readability count and agreement
    sec4 = re.search(r"^## 4\..*?(?=^## 5\.)", body, re.S | re.M)
    readable = 0
    if sec4:
        rows = [l for l in sec4.group(0).splitlines() if l.startswith("|") and not l.startswith("|--") and not re.match(r"^\|\s*(Source|المصدر)\s*\|", l)]
        for r in rows:
            cells = [c.strip() for c in r.strip("|").split("|")]
            if len(cells) >= 4 and re.search(r"^(yes|نعم)$", cells[3], re.I): readable += 1
    try:
        if int(fm.get("sources_read", "-1")) != readable: fails.append(f"block {idx}: sources_read is {fm.get('sources_read')} but {readable} rows are marked readable")
    except ValueError: fails.append(f"block {idx}: sources_read must be a number")
    if verdict == "CLEAN" and fm.get("sources_agree") != "yes": fails.append(f"block {idx}: CLEAN requires sources_agree: yes")
    if verdict == "CLEAN" and readable < 2: fails.append(f"block {idx}: CLEAN requires at least two readable sources")

def main():
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    text = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
    blocks = [b for b in re.split(r"^\n*---\s*$\n(?=---\n)", text, flags=re.M) if b.strip()]
    # simpler split: on a line that is exactly '---' followed directly by a front block start
    blocks = re.split(r"(?m)^(?=---\ntayyib:)", text); blocks = [b for b in blocks if b.strip()]
    fails, warns = [], []
    for i, b in enumerate(blocks, 1): check_block(b.strip("\n") + "\n", i, fails, warns)
    for w in warns: print("warn:", w)
    for f in fails: print("FAIL:", f)
    print(f"{pathlib.Path(sys.argv[1]).name}: {len(blocks)} verdict(s), {len(fails)} failures, {len(warns)} warnings")
    sys.exit(1 if fails else 0)

if __name__ == "__main__": main()
