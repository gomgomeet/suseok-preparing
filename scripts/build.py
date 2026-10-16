"""성취수준 마크다운(과목별)과 보기 페이지(docs/index.html)를 생성한다.
실행: python3 scripts/build.py
"""
import html, json, os, sys

sys.path.insert(0, os.path.dirname(__file__))
from data import GENERAL, SUBJECTS, INTEGRATED_NOTE
from grades import GRADES, MISSING
from norm import load as load_std, by_grade as std_by_grade, label

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_DIR = os.path.join(ROOT, "성취수준")
os.makedirs(MD_DIR, exist_ok=True)

NOTICE = ("> 학년군·영역 구성은 2022 개정 교육과정(교육부 고시 제2022-33호) 기준입니다. "
          "A·B·C 기술은 한국교육과정평가원 '성취수준의 일반적 특성'(초등 3단계)을 영역에 적용해 정리한 것으로, "
          "평가원 「2022 개정 교육과정에 따른 성취기준별 성취수준(초등학교)」 원문과 문구가 다를 수 있습니다. "
          "평가계획·통지에 쓸 때는 원문과 대조하세요.")


def cell(s):
    return s.replace("|", "\\|")


def subject_md(sub):
    out = [f"# {sub['name']} 성취수준 (2022 개정, 초등)", "", NOTICE, ""]
    for band, rows in sub["bands"].items():
        out += [f"## {band}", "", "| 영역 | A (잘함) | B (보통) | C (노력 요함) |", "|---|---|---|---|"]
        for area, code, a, b, c in rows:
            label = f"**{area}**" + (f"<br>`[{code}-○○]`" if code else "")
            out.append(f"| {label} | {cell(a)} | {cell(b)} | {cell(c)} |")
        out.append("")
    return "\n".join(out)


def readme_md():
    out = ["# 초등 교과별 성취수준 정리 (2022 개정 교육과정)", "",
           "수석교사 준비용 자료. 9개 교과의 학년군·영역별 성취수준(A·B·C)을 과목별 파일로 정리했습니다.", "",
           NOTICE, "", "## 학년별 파일 (2026학년도 연간 지도 계획 기준)", "",
           " · ".join(f"[{g}학년](학년별/{g}학년.md)" for g in sorted(GRADES)), "",
           "각 학년 파일에는 그 학년에서 다루는 성취기준(코드·원문)이 과목별로 학기·단원과 함께 정리되어 있고, 영역 성취수준(A·B·C)이 붙어 있습니다. "
           "같은 내용을 엑셀로 정리한 [초등_성취기준_학년별.xlsx](초등_성취기준_학년별.xlsx)도 있습니다(학년별 시트, 미배치 시트, 학년군 원본 대비 시트).", "",
           "## 과목별 파일", "", "| 과목 | 학년군 | 영역 수 |", "|---|---|---|"]
    for s in SUBJECTS:
        bands = " · ".join(s["bands"].keys())
        n = sum(len(v) for v in s["bands"].values())
        out.append(f"| [{s['name']}](성취수준/{s['slug']}.md) | {bands} | {n} |")
    out += ["", f"※ {INTEGRATED_NOTE}", "", "## 성취수준의 일반적 특성 (초등 3단계)", "",
            "| 수준 | 특성 |", "|---|---|"]
    out += [f"| {k} | {v} |" for k, v in GENERAL.items()]
    out += ["", "## 학년별 적용", "",
            "초등 교육과정은 학년군(1~2, 3~4, 5~6학년) 단위로 성취수준이 제시됩니다. "
            "같은 학년군의 두 학년은 동일한 성취수준을 공유하고, 학교 교육과정에서 학년별로 성취기준을 배분해 적용합니다.", "",
            "## 원문 확인처", "",
            "- [경남교육청: 2022 개정 교육과정에 따른 성취기준별 성취수준(초등학교)](https://www.gne.go.kr/user/bbs/BD_selectBbs.do?q_bbsSn=1464&q_bbsDocNo=1715916)",
            "- [에듀넷: 2022 개정 교육과정 성취수준](https://www.edunet.net/nedu/ncicsvc/listTchBoardForm.do?boardNum=16&menu_id=642)",
            "- [국가기초학력지원센터 공지](https://k-basics.org/user/noticeView.do?menuSeq=726&bbsSeq=1826)", "",
            "## 다시 생성", "", "```", "python3 scripts/build.py", "```", ""]
    return "\n".join(out)


def band_of(g):
    return "1~2학년" if g <= 2 else "3~4학년" if g <= 4 else "5~6학년"


SUB = {s["name"]: s for s in SUBJECTS}
GRADE_NOTE = ("> 성취기준은 2022 개정 교육과정(교육부 고시 제2022-33호) 원문입니다. 학기·단원은 2026학년도 학교 연간 지도 계획과 "
              "대조해 배치했습니다(자동 대조 + 교사 검토 보정). 성취수준은 해당 학년군의 영역 성취수준을 적용합니다.")
KIND_MARK = {"두 학년 공통": " ◆공통", "두 학년 반복·심화": " ◇반복·심화"}
STD_DATA = load_std()
STD_BY_G = std_by_grade(STD_DATA)


def grade_md(g):
    out = [f"# {g}학년 성취기준 (2026학년도 학교 교육과정 배치)", "", GRADE_NOTE, "",
           "◆공통: 같은 학년군의 두 학년에서 모두 다룸 · ◇반복·심화: 음악·미술·체육처럼 두 학년에 걸쳐 반복·심화", ""]
    subjects = list(dict.fromkeys(r["교과"] for r, _, _ in STD_BY_G[g]))
    for name in subjects:
        rows = [(r, sems, units) for r, sems, units in STD_BY_G[g] if r["교과"] == name]
        out += [f"## {name} ({len(rows)}개)", "", "| 학기 | 단원 | 코드 | 성취기준 |", "|---|---|---|---|"]
        for r, sems, units in rows:
            out.append(f"| {' · '.join(sems)} | {cell('<br>'.join(units))} | {r['코드']}{KIND_MARK.get(label(r), '')} | {cell(r['성취기준'])} |")
        used = []
        for sem, us in GRADES.get(g, {}).get(name, {}).items():
            for _, ds in us:
                used += [d for d in ds if d not in used]
        lv = [x for x in SUB[name]["bands"][band_of(g)] if x[0] in used]
        if lv:
            out += ["", f"<details><summary>{g}학년 {name} 영역 성취수준 (A·B·C)</summary>", "",
                    "| 영역 | A (잘함) | B (보통) | C (노력 요함) |", "|---|---|---|---|"]
            out += [f"| **{x[0]}** | {cell(x[2])} | {cell(x[3])} | {cell(x[4])} |" for x in lv]
            out += ["", "</details>"]
        out.append("")
    if g >= 5:
        un = [r for r in STD_DATA if not r["배치"] and r["학년군"] == "5~6학년군"]
        out += ["## 아직 배치하지 못한 5~6학년군 성취기준 (2학기 계획서 미제출)", "",
                "| 교과 | 묶음 | 코드 | 성취기준 |", "|---|---|---|---|"]
        out += [f"| {r['교과']} | {r['영역']} | {r['코드']} | {cell(r['성취기준'])} |" for r in un]
        out.append("")
    out += [f"※ {MISSING}", ""]
    return "\n".join(out)


def build_html():
    grades = []
    for g in sorted(GRADES):
        subs = []
        for n in dict.fromkeys(r["교과"] for r, _, _ in STD_BY_G[g]):
            used = []
            for _, us in GRADES[g].get(n, {}).items():
                for _, ds in us:
                    used += [d for d in ds if d not in used]
            subs.append({"name": n, "areas": used, "stds": [
                {"code": r["코드"], "text": r["성취기준"], "sems": sems, "units": units, "kind": label(r)}
                for r, sems, units in STD_BY_G[g] if r["교과"] == n]})
        grades.append({"grade": g, "band": band_of(g), "subjects": subs})
    unplaced = [{"subj": r["교과"], "group": r["영역"], "code": r["코드"], "text": r["성취기준"]}
                for r in STD_DATA if not r["배치"]]
    data = json.dumps({"general": GENERAL, "note": INTEGRATED_NOTE, "grades": grades, "missing": MISSING, "unplaced": unplaced,
                       "subjects": [{"name": s["name"], "slug": s["slug"], "bands": [
                           {"band": b, "rows": [list(r) for r in rows]} for b, rows in s["bands"].items()]}
                           for s in SUBJECTS]}, ensure_ascii=False)
    tpl = open(os.path.join(os.path.dirname(__file__), "page.html"), encoding="utf-8").read()
    return tpl.replace("__DATA__", data)


for s in SUBJECTS:
    open(os.path.join(MD_DIR, f"{s['slug']}.md"), "w", encoding="utf-8").write(subject_md(s))
GR_DIR = os.path.join(ROOT, "학년별")
os.makedirs(GR_DIR, exist_ok=True)
for g in sorted(GRADES):
    open(os.path.join(GR_DIR, f"{g}학년.md"), "w", encoding="utf-8").write(grade_md(g))
open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8").write(readme_md())
os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
open(os.path.join(ROOT, "docs", "index.html"), "w", encoding="utf-8").write(build_html())
print("ok", len(SUBJECTS), "subjects")
