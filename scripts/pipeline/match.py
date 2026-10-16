"""성취기준(CSV)을 학교 연간 지도 계획의 단원 내용과 대조해 학년·학기·단원에 배치한다.
사용: python3 -I match.py standards.csv txt_dir units2.json out.json
"""
import csv, json, os, re, sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

csv_path, txt_dir, units_path, out_path = sys.argv[1:5]
STD = list(csv.DictReader(open(csv_path, encoding="utf-8-sig")))
UNITS = json.load(open(units_path, encoding="utf-8"))
JUNK = {"수학 익힘", "차시명", "차시명 및 주요 내용", "학습 주제", "활동명", "주제", "학습 내용", "국활", "국어", "국어 활동",
        "다가가기", "배울 내용 살펴보기", "마무리하기", "수학을 찾아요", "수학이랑 만들어요", "수학이랑 함께해요", "프로젝트",
        "7. 창의 프로젝트", "안전하게 탐구하기", "심화 보충(담임 재량)", "단원 정리", "열려라 과학"}
BAND = {1: "1~2학년군", 2: "1~2학년군", 3: "3~4학년군", 4: "3~4학년군", 5: "5~6학년군", 6: "5~6학년군"}
SUBJ = ["국어", "수학", "사회", "과학", "도덕", "체육", "음악", "미술", "실과"]

# 1) 계획서를 단원 단위 조각으로 나눈다
segs = []  # (grade, sem, subj, unit, text)
for fn in sorted(os.listdir(txt_dir)):
    if not fn.endswith(".txt"):
        continue
    g, sem, subj = re.search(r"(\d)학년[ _](\d)학기_(.+?)_", fn).groups()
    if subj not in SUBJ:
        continue
    g = int(g)
    L = [l.strip() for l in open(os.path.join(txt_dir, fn), encoding="utf-8") if l.strip()][1:]
    titles = [t for t in UNITS[str(g)][subj][sem] if t not in JUNK and not t.startswith("창의가 팡팡")]
    lineset = set(L)
    sys.path.insert(0, "/home/claude/suseok-preparing/scripts")
    from grades import GRADES as _G
    titles += [u for u, _ in _G.get(g, {}).get(subj, {}).get(f"{sem}학기", []) if u in lineset and u not in titles]
    titles += [l for l in lineset if re.match(r"^[1-8]\. \S", l) and len(l) < 22 and "?" not in l and "(" not in l
               and sum(1 for x in L if x == l) >= 2 and l not in titles and subj in ("국어",)]
    big_names = [u for u, _ in _G.get(g, {}).get(subj, {}).get(f"{sem}학기", [])]
    cur, big, buf = "(단원 미상)", None, []
    def flush():
        if buf:
            lab = cur if (big is None or cur == big) else f"{big} › {cur}"
            segs.append((g, f"{sem}학기", subj, lab, " ".join(buf)))
    for l in L:
        if l in titles and l != cur and not (big and f"{big} › {l}" == cur):
            flush()
            if l in big_names or subj != "국어":
                big = l if l in big_names else big
                cur = l
            else:
                cur = l
            buf = []
        buf.append(l)
    flush()

# 같은 단원 조각 합치기
merged = {}
for g, sem, subj, unit, text in segs:
    merged.setdefault((g, sem, subj, unit), []).append(text)
SEG = [(k, " ".join(v)) for k, v in merged.items() if len(" ".join(v)) > 20]

# 2) 성취기준마다 같은 학년군·교과의 단원 조각과 유사도 비교
vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 3), sublinear_tf=True)
vec.fit([t for _, t in SEG] + [s["성취기준"] for s in STD])
out = []
for s in STD:
    if s["교과"] not in SUBJ:
        continue
    cand = [(k, t) for k, t in SEG if k[2] == s["교과"] and BAND[k[0]] == s["학년군"]]
    rec = dict(s)
    if not cand:
        rec.update(grade=None, status="계획서 없음", matches=[])
        out.append(rec); continue
    q = vec.transform([s["성취기준"]])
    sims = cosine_similarity(q, vec.transform([t for _, t in cand]))[0]
    tsims = cosine_similarity(q, vec.transform([re.sub(r"^[\d.\s]+|독서단원:|독서:", "", k[3]) for k, _ in cand]))[0]
    sims = sims + 0.6 * tsims
    ranked = sorted(zip(sims, [k for k, _ in cand]), reverse=True)
    best = {}
    for sc, k in ranked:
        best.setdefault(k[0], (sc, k))
    rec["matches"] = [{"grade": k[0], "sem": k[1], "unit": k[3], "score": round(float(sc), 3)} for sc, k in best.values()]
    out.append(rec)
json.dump(out, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "standards,", len(SEG), "unit segments")
