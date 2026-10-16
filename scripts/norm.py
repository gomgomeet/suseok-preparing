"""성취기준 학년별 배치 데이터를 읽고, 계획서 원문 단원명을 정리된 단원명으로 맞춘다."""
import json, os, re
from grades import GRADES

HERE = os.path.dirname(os.path.abspath(__file__))
SUBJ_ORDER = ["국어", "수학", "사회", "과학", "도덕", "실과", "체육", "음악", "미술"]


def _core(s):
    return re.sub(r"^\s*\d+\.\s*", "", s).replace(" ", "")


# 사회는 계획서의 주제·차시명을 학기 단원 묶음(grades.py)으로 모은다: (학년, 학기) → [(핵심어들, 단원 묶음 순번)]
SOCIAL = {
 (3, "1학기"): [(("장소",), 0), (("시간", "과거", "달라진"), 1)],
 (3, "2학기"): [(("교통", "통신", "사회 변화"), 0), (("풍습", "옛날"), 1), (("문화",), 2), (("",), 0)],
 (4, "1학기"): [(("지도", "위치"), 0), (("국가유산", "역사"), 1), (("경제", "교류"), 2)],
 (4, "2학기"): [(("민주", "자치"), 0), (("지역문제", "알리"), 1), (("환경", "도시"), 2)],
 (5, "1학기"): [(("인구",), 2), (("독도", "국토", "지리 탐구"), 0), (("지형", "기후", "자연재해"), 1), (("법", "인권"), 3)],
 (5, "2학기"): [(("선사", "고조선", "고대", "고려", "유적", "청동기"), 0), (("조선", "개항", "달라지는 시대"), 1), (("식민", "일제", "광복", "전쟁", "저항"), 2)],
 (6, "2학기"): [(("지형", "기후", "자연환경", "해안"), 0), (("시장", "경제", "무역", "근로자", "거래"), 1), (("인구", "지구촌", "지속가능", "독도", "국토"), 2)],
 (6, "1학기"): [(("통일", "항쟁", "산업화"), 0), (("선거", "미디어", "국가기관", "민주주의"), 1), (("세계", "지구본", "대륙"), 2)],
}


def unit_name(grade, subj, sem, raw):
    """계획서에서 뽑은 단원명(raw)을 grades.py 의 정리된 단원명으로 바꾼다. 못 찾으면 raw."""
    units = [u for u, _ in GRADES.get(grade, {}).get(subj, {}).get(sem, [])]
    if subj == "사회" and (grade, sem) in SOCIAL:
        for kws, i in SOCIAL[(grade, sem)]:
            if any(k in raw for k in kws):
                return units[i] + (" › " + raw.split(" › ", 1)[1] if " › " in raw else "")
    if subj == "음악":
        return "전 단원 (제재곡별 연주·감상·창작)"
    if raw == "(단원 미상)":
        return "여러 단원 공통"
    if " › " in raw:
        big, sub = raw.split(" › ", 1)
        cs = _core(sub)
        for u in units:  # 하위 표제가 사실은 별도 단원(보충 단원 등)인 경우
            if len(cs) >= 4 and cs in _core(u) and _core(u) != _core(big):
                return u
        return f"{unit_name(grade, subj, sem, big)} › {sub}"
    c = _core(raw)
    for u in units:
        if _core(u) == c:
            return u
    for u in units:
        cu = _core(u)
        if c and (c in cu or cu.split("(")[0] in c):
            return u
    return raw


def load():
    """[{학년군, 교과, 영역, 영역번호?, 코드, 성취기준, 배치:[{학년,학기,단원}], 구분, 근거}]"""
    data = json.load(open(os.path.join(HERE, "standards_by_grade.json"), encoding="utf-8"))
    for r in data:
        for b in r["배치"]:
            b["단원"] = unit_name(b["학년"], r["교과"], b["학기"], b["단원"])
    return data


def by_grade(data):
    """학년 → [(성취기준 레코드, 학기들, 단원들)] (한 학년에서 한 성취기준은 한 줄)"""
    out = {g: [] for g in range(1, 7)}
    for r in data:
        per = {}
        for b in r["배치"]:
            per.setdefault(b["학년"], []).append(b)
        for g, bs in per.items():
            sems = list(dict.fromkeys(b["학기"] for b in bs))
            units = list(dict.fromkeys(f"{b['학기'][0]}학기 {b['단원']}" if len(sems) > 1 else b["단원"] for b in bs))
            out[g].append((r, sems, units))
    for g in out:
        out[g].sort(key=lambda x: (SUBJ_ORDER.index(x[0]["교과"]), min(x[1]), x[0]["코드"]))
    return out


def label(r):
    k = r["구분"]
    return "단일 학년" if re.fullmatch(r"\d학년", k) else k
