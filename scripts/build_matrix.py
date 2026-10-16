"""학년별 내용 체계 도식표 데이터: 교과 → 내용 영역(행) × 1~6학년(열) → 단원·성취기준
실행: python3 scripts/build_matrix.py  → docs/matrix.html, matrix.json
"""
import json, os, re
from norm import load, SUBJ_ORDER

HERE = os.path.dirname(os.path.abspath(__file__))
dot = lambda s: s.replace("⋅", "·")

# 사회·과학: 성취기준 묶음(엑셀 '영역') → 교육과정 내용 영역
TOPIC = {
 "과학": {
  "힘과 우리 생활": "운동과 에너지", "소리의 성질": "운동과 에너지", "자석의 이용": "운동과 에너지", "빛의 성질": "운동과 에너지",
  "열과 우리 생활": "운동과 에너지", "물체의 운동": "운동과 에너지", "전기의 이용": "운동과 에너지",
  "물체와 물질": "물질", "물의 상태 변화": "물질", "여러 가지 기체": "물질", "용해와 용액": "물질", "혼합물의 분리": "물질",
  "산과 염기": "물질", "물질의 연소": "물질",
  "동물의 생활": "생명", "식물의 생활": "생명", "생물의 한살이": "생명", "다양한 생물과 우리 생활": "생명", "생물과 환경": "생명",
  "우리 몸의 구조와 기능": "생명", "식물의 구조와 기능": "생명",
  "지구와 바다": "지구와 우주", "땅의 변화": "지구와 우주", "밤하늘 관찰": "지구와 우주", "지층과 화석": "지구와 우주",
  "날씨와 우리 생활": "지구와 우주", "지구의 운동": "지구와 우주", "계절의 변화": "지구와 우주",
  "감염병과 건강한 생활": "과학과 사회", "기후변화와 우리 생활": "과학과 사회", "자원과 에너지": "과학과 사회", "과학과 나의 진로": "과학과 사회",
 },
 "사회": {
  "우리가 사는 곳": "지리 인식", "지도로 만나는 우리 지역": "지리 인식", "우리나라 국토 여행": "지리 인식", "지구, 대륙 그리고 국가들": "지리 인식",
  "다양한 환경과 삶의 모습": "자연환경과 인간 생활", "우리나라 지리 탐구": "자연환경과 인간 생활", "세계의 자연환경": "자연환경과 인간 생활",
  "지역문제를 해결하고 지역을 알리는 노력": "지속가능한 세계", "지구촌 사람들": "지속가능한 세계",
  "일상에서 만나는 과거": "역사", "옛날과 오늘날의 생활 모습": "역사", "우리 지역의 문화유산": "역사",
  "유적과 유물로 살펴본 옛 사람들의 생활": "역사", "달라지는 시대, 변화하는 생활 모습": "역사",
  "식민 통치와 저항, 전쟁이 바꾼 사회와 생활": "역사", "평화 통일을 위한 노력, 민주화와 산업화": "역사",
  "민주주의와 자치": "정치", "민주주의와 시민 참여": "정치", "법과 인권의 보장": "법",
  "경제활동과 지역 간 교류": "경제", "시장경제와 국가 간 거래": "경제", "사회 변화와 다양한 문화": "사회·문화",
 },
}
ROW_ORDER = {
 "과학": ["운동과 에너지", "물질", "생명", "지구와 우주", "과학과 사회"],
 "사회": ["지리 인식", "자연환경과 인간 생활", "지속가능한 세계", "역사", "정치", "법", "경제", "사회·문화"],
}


def short_unit(u):
    u = u.split(" › ")[0]
    u = re.sub(r"^\s*\d+\.\s*", "", u)
    u = re.sub(r"^(?:독서단원|독서)[.:]\s*", "독서: ", u)
    u = re.sub(r"^매체[.:]\s*", "매체: ", u)
    u = re.sub(r"\s*\((?:탐구|2022 개정[^)]*)\)$", "", u)
    return u.strip()


data = load()
subjects = []
for subj in SUBJ_ORDER:
    rs = [r for r in data if r["교과"] == subj]
    rows = ROW_ORDER.get(subj) or list(dict.fromkeys(dot(r["영역"]) for r in rs))
    grid = {row: {g: {} for g in range(1, 7)} for row in rows}
    unplaced = []
    for r in rs:
        row = TOPIC[subj].get(r["영역"]) if subj in TOPIC else dot(r["영역"])
        if row is None:
            raise SystemExit(f"영역 매핑 없음: {subj} {r['영역']}")
        if not r["배치"]:
            unplaced.append({"code": r["코드"], "text": r["성취기준"], "row": row, "group": r["영역"]})
            continue
        for b in r["배치"]:
            u = "전 단원" if subj == "음악" else short_unit(b["단원"])
            cell = grid[row][b["학년"]].setdefault(u, {"sems": [], "stds": []})
            if b["학기"] not in cell["sems"]:
                cell["sems"].append(b["학기"])
            if all(s["code"] != r["코드"] for s in cell["stds"]):
                cell["stds"].append({"code": r["코드"], "text": r["성취기준"], "kind": r["구분"], "group": r["영역"]})
    out_rows = []
    for row in rows:
        cells = []
        for g in range(1, 7):
            units = [{"u": u, "sems": sorted(v["sems"]), "stds": sorted(v["stds"], key=lambda s: s["code"])}
                     for u, v in sorted(grid[row][g].items(), key=lambda kv: (min(kv[1]["sems"]), min(s["code"] for s in kv[1]["stds"])))]
            cells.append(units)
        out_rows.append({"name": row, "cells": cells})
    grades = [g for g in range(1, 7) if any(r["cells"][g - 1] for r in out_rows)]
    subjects.append({"name": subj, "rows": out_rows, "grades": grades, "unplaced": unplaced,
                     "count": len({r["코드"] for r in rs})})

payload = {"subjects": subjects}
json.dump(payload, open(os.path.join(HERE, "matrix.json"), "w", encoding="utf-8"), ensure_ascii=False)
tpl = open(os.path.join(HERE, "matrix.html"), encoding="utf-8").read()
open(os.path.join(os.path.dirname(HERE), "docs", "matrix.html"), "w", encoding="utf-8").write(
    tpl.replace("__DATA__", json.dumps(payload, ensure_ascii=False, separators=(",", ":"))))
for s in subjects:
    print(s["name"], s["count"], [r["name"] for r in s["rows"]], "학년", s["grades"], "미배치", len(s["unplaced"]))
