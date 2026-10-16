"""심층면접 연습실 페이지 생성: scripts/interview.html + 성취기준 배치 데이터 → docs/interview.html"""
import json, os
from norm import load, SUBJ_ORDER
from refs import REFS
HERE = os.path.dirname(os.path.abspath(__file__))
rows = []
for r in load():
    if not r["배치"]:
        continue
    pl = sorted({(b["학년"], b["학기"], b["단원"]) for b in r["배치"]})
    rows.append([r["코드"], r["성취기준"], r["교과"], r["영역"], [[g, s[0], u] for g, s, u in pl], REFS.get(r["코드"], [])])
rows.sort(key=lambda x: (SUBJ_ORDER.index(x[2]), x[0]))
tpl = open(os.path.join(HERE, "interview.html"), encoding="utf-8").read()
out = os.path.join(os.path.dirname(HERE), "docs", "interview.html")
open(out, "w", encoding="utf-8").write(tpl.replace("__STD__", json.dumps(rows, ensure_ascii=False, separators=(",", ":"))))
print(out, len(rows))
