import os, re, sys, json
d = sys.argv[1]
start = re.compile(r"^1(\s*[~,]\s*\d+)?$|^1/\d+$")
num = re.compile(r"^[\d\s~,\-/]+(쪽)?$")
bad = re.compile(r"^(\d\)|준비|단원 도입|독서 준비|독서 후|독서|실천|정리|대단원 도입|•|-|<|\(|※|2022 개정)")
out = {}
for fn in sorted(os.listdir(d)):
    if not fn.endswith(".txt"): continue
    g, sem, subj = re.search(r"(\d)학년[ _](\d)학기_(.+?)_", fn).groups()
    L = [l.strip() for l in open(os.path.join(d, fn), encoding="utf-8") if l.strip()]
    units = []
    for i, l in enumerate(L):
        if not start.match(l): continue
        for k in range(1, 5):
            if i - k < 0: break
            t = L[i - k]
            if num.match(t) or bad.match(t) or t == "1.": continue
            if "/" in t or "?" in t or "!" in t or len(t) > 40 or "(과" in t: break
            if t not in units: units.append(t)
            break
    out.setdefault(g, {}).setdefault(subj, {})[sem] = units
json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
