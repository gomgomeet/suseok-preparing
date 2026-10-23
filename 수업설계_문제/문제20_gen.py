import json, html, sys, re
sys.path.insert(0, "/tmp/claude-0/-home-claude/7f1459fd-826e-5191-b8ff-48096a85b870/scratchpad/q20")
from data import P
from qset import GRADE, Q
S = json.load(open("/tmp/claude-0/-home-claude/7f1459fd-826e-5191-b8ff-48096a85b870/scratchpad/stds.json", encoding="utf-8"))
KI = json.load(open("/tmp/claude-0/-home-claude/7f1459fd-826e-5191-b8ff-48096a85b870/scratchpad/ki/ki.json", encoding="utf-8"))
e = html.escape
norm = lambda x: re.sub(r"[·⋅\s]|\(.*?\)", "", x)
def area_ki(p):
    for b in KI[p["subj"]]:
        if norm(b["area"]) == norm(p["area"]): return b["ki"]
    raise SystemExit("no area " + p["subj"] + p["area"])
CSS = """
@page{size:A4;margin:14mm 15mm 14mm}
*{box-sizing:border-box}
body{font-family:"Noto Sans CJK KR","Noto Sans KR",sans-serif;color:#1d2730;font-size:9.6pt;line-height:1.55;margin:0}
.page{page-break-after:always}
.page:last-child{page-break-after:auto}
h1{font-size:21pt;margin:0 0 4mm;letter-spacing:-.5px}
h2{font-size:13pt;margin:0 0 3mm;color:#2e6b62}
.sub{color:#5e6a72;font-size:10pt;margin:0 0 6mm}
.kicker{display:inline-block;background:#2e6b62;color:#fff;font-weight:700;font-size:8.5pt;padding:1mm 2.5mm;border-radius:2mm;margin-bottom:4mm}
table{border-collapse:collapse;width:100%}
th,td{border:.3mm solid #b9c2bd;padding:1.4mm 2mm;vertical-align:top;text-align:left}
th{background:#e1eeea;font-weight:700;color:#1d2730}
.list td{font-size:8.6pt}
.qhead{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:.8mm solid #2e6b62;padding-bottom:2mm;margin-bottom:3mm}
.qno{font-size:17pt;font-weight:800;color:#2e6b62}
.qmeta{font-size:10pt;font-weight:700}
.qmeta span{color:#5e6a72;font-weight:400}
.box{border:.3mm solid #b9c2bd;border-radius:2mm;padding:2mm 3mm;margin-bottom:2.6mm}
.box h3{font-size:9.4pt;margin:0 0 1.2mm;color:#2e6b62}
.std p{margin:0 0 .8mm}
.code{font-weight:700;margin-right:1.5mm}
ul{margin:0;padding-left:4.5mm}
li{margin:0 0 .6mm}
.ke td,.ke th{font-size:8.9pt}
.ke th{width:22mm}
.lv th{width:22mm;text-align:center}
.lv td{font-size:8.9pt}
.note{font-size:7.8pt;color:#5e6a72;margin-top:1mm}
.ctx{background:#fff6dc;border-color:#e6d6a5}
.cond{border-color:#c4372c}
.cond h3{color:#c4372c}
ol{margin:0;padding-left:5mm}
.task{margin-top:2mm;font-size:8.6pt;color:#5e6a72;border-top:.3mm dashed #b9c2bd;padding-top:1.6mm}
.tasks li{margin-bottom:1.6mm}
.tasks b{color:#1d2730}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:2mm 6mm}
.small{font-size:8.6pt}
.src li{margin-bottom:1mm}
.rub td:last-child{text-align:center;width:14mm}
"""
CSS += """
.info th{width:24mm;background:#e1eeea;text-align:center;vertical-align:middle}
.info td{font-size:9.2pt}
.qs{margin:0;padding:0;list-style:none;counter-reset:q}
.qs li{border:.3mm solid #b9c2bd;border-radius:2mm;padding:2mm 3mm;margin-bottom:2.4mm;font-size:9.4pt}
.qs .qt{font-weight:800;color:#2e6b62;margin-right:1.5mm}
.qs .pt{float:right;font-size:8.4pt;color:#5e6a72;font-weight:700}
.where{font-size:8pt;color:#5e6a72;margin-top:1.5mm}
"""
QT = [("문제 1", "단원 설계", 25), ("문제 2", "차시 묶음과 탐구 질문", 20), ("문제 3", "차시 과정안", 30), ("문제 4", "학습으로의 평가", 25)]

def page(i, p):
    k = i - 1
    stds = "".join(f'<p><span class="code">[{c}]</span>{e(S[c])}</p>' for c in p["std"])
    kis = "<ul>" + "".join(f"<li>{e(x)}</li>" for x in area_ki(p)) + "</ul>"
    qs = "".join(f'<li><span class="pt">{pt}점</span><span class="qt">{a} {b}</span>{e(t)}</li>' for (a, b, pt), t in zip(QT, Q[k]))
    return f"""
<section class="page">
 <div class="qhead"><div class="qno">문항 {i:02d}</div>
  <div class="qmeta">초등 {GRADE[k]} {e(p['subj'])} <span>· {e(p['area'])} 영역 · {e(p['hours'])}</span></div></div>
 <h2>교과 정보</h2>
 <table class="info">
  <tr><th>학년 · 교과</th><td>초등학교 {GRADE[k]} · {e(p['subj'])} ({e(p['area'])} 영역) · {e(p['hours'])}</td></tr>
  <tr><th>성취기준</th><td class="std">{stds}</td></tr>
  <tr><th>핵심 아이디어</th><td>{kis}<p class="note">{e(p['subj'])}{'' if p['subj'].endswith('과') else '과'} 「{e(p['area'])}」 영역의 핵심 아이디어 전체(교육과정 원문)</p></td></tr>
  <tr><th>학급 상황</th><td>{e(p['ctx'])}</td></tr>
 </table>
 <h2 style="margin-top:4mm">설계 문제 <span style="font-size:9pt;color:#5e6a72;font-weight:400">(100점 · 권장 50~60분)</span></h2>
 <ol class="qs">{qs}</ol>
 <p class="where">답안 작성: 「깊이있는 수업 설계 답안지」 1쪽 단원 설계표에 문제 1·2, 2쪽 차시 과정안에 문제 3·4</p>
</section>"""

rows = "".join(f"<tr><td>{i+1:02d}</td><td>{GRADE[i]}</td><td>{e(p['subj'])} · {e(p['area'])}</td><td>{' '.join('['+c+']' for c in p['std'])}</td><td>{e(p['hours'])}</td></tr>" for i, p in enumerate(P))

cover = f"""
<section class="page">
 <span class="kicker">수석교사 2차 심사 대비 · 수업 및 평가 설계</span>
 <h1>깊이있는 수업 설계 문제 20</h1>
 <p class="sub">교과 정보(학년 · 성취기준 · 핵심 아이디어)를 읽고, 구체적인 설계 문제 4개에 답하는 형식</p>
 <table class="list"><tr><th>번호</th><th>학년</th><th>교과 · 영역</th><th>성취기준</th><th>차시</th></tr>{rows}</table>
 <p class="note">성취기준과 핵심 아이디어는 2022 개정 교육과정(교육부 고시 제2022-33호)의 원문입니다. 핵심 아이디어는 해당 영역의 것을 생략 없이 모두 실었습니다. 학년과 학급 상황은 출제를 위해 설정한 것입니다.</p>
</section>"""

guide = """
<section class="page">
 <h2>문항 구성과 채점 기준</h2>
 <div class="box"><h3>모든 문항의 구성</h3><ul class="small">
  <li><b>교과 정보</b> — 학년 · 교과(영역) · 차시, 성취기준, 핵심 아이디어(영역 전체), 학급 상황</li>
  <li><b>설계 문제</b> — 문항마다 내용에 맞춘 구체적 요구 4개. 답은 「깊이있는 수업 설계 답안지」(깊수다 단원 설계표 · 차시 과정안 양식)에 씁니다.</li></ul></div>
 <div class="box"><h3>채점 기준 (100점)</h3>
  <table class="rub small"><tr><th>문제</th><th>보는 관점</th><th>배점</th></tr>
  <tr><td>1 단원 설계</td><td>핵심 아이디어와 성취기준을 엮어 핵심어를 뽑았는가. 핵심 문장이 목표형(~할 수 있다)이 아닌 명제형으로 관계를 진술하고 학년 눈높이에 맞는가. 핵심 질문이 단원 전체를 이끄는가. 문제가 요구한 조건을 지켰는가</td><td>25</td></tr>
  <tr><td>2 차시 묶음과 탐구 질문</td><td>차시 묶음이 개념을 잇는 흐름인가. 탐구 질문이 핵심 질문에 다가가도록 이어지고 학생이 실제로 탐구할 수 있는가. 학급 상황과 삶의 맥락이 활동 안에 녹아 있는가</td><td>20</td></tr>
  <tr><td>3 차시 과정안</td><td>준비(질문이 생기는 장면) → 탐구(학생이 주도) → 정리·실천(학생이 만드는 일반화) → 성찰이 이어지는가. 피드백 및 유의점이 구체적이고 문제가 요구한 장치를 담았는가</td><td>30</td></tr>
  <tr><td>4 학습으로의 평가</td><td>평가 과제가 핵심 문장의 이해를 새로운 상황에서 확인하는가. 평가 요소가 성취기준과 맞고 성취수준 A·B·C가 관찰 가능한 행동으로 구분되는가. 평가 방법과 피드백이 수업과 이어지는가</td><td>25</td></tr></table></div>
 <div class="box"><h3>핵심 문장 점검법</h3><p class="small">핵심 문장 뒤에 "때문에 학생은 [성취기준]"을 붙여 읽어 자연스러우면 성취기준과 이어진 것입니다.</p></div>
</section>"""
src = """
<section class="page">
 <h2>참고 자료</h2>
 <ul class="src small">
  <li>교육부(2022). 초·중등학교 교육과정 총론 및 교과 교육과정. 교육부 고시 제2022-33호 — 성취기준, 핵심 아이디어, 내용 요소</li>
  <li>경기도교육청. 초등 깊이있는 수업 프레임워크(1028 수정) — 단원 설계 3단계, 핵심어·핵심 문장·핵심 질문, 학습으로의 평가(GRASPS), 탐구 질문, 수업 나눔</li>
  <li>경기도교육청. 2022 개정 교육과정 기반 수업설계 도움자료 「탐구-실행-성찰과정 프레임워크」 — 개발 4단계(교육과정 분석 → 탐구 질문 → 삶과 연계된 수행과제 → 탐구-실행-성찰)</li>
  <li>경기도교육청. 「탐구-실행-성찰과정 프레임워크 2.0」 — 8가지 삶의 맥락, 핵심 아이디어 재구성, 깊이있는 단원 수업 설계안 틀, 설계 체크리스트</li>
  <li>경기도교육청. 2025학년도 교수·학습 및 평가계획[정보공시] 작성 도움자료 — 수업·평가 연계의 주안점</li>
  <li>경기도교육청. 2025 다름과 공존하는 경기초등토론수업 실천자료집 — 문항 11</li>
 </ul>
 <p class="note">각 문항의 학년과 학급 상황은 출제를 위해 설정한 것입니다. 성취수준(A·B·C)을 진술할 때는 한국교육과정평가원 「2022 개정 교육과정에 따른 성취기준별 성취수준(초등학교)」을 참고하세요.</p>
</section>"""


out = f"<!doctype html><html lang='ko'><head><meta charset='utf-8'><title>깊이있는 수업 설계 문제 20</title><style>{CSS}</style></head><body>{cover}{guide}{''.join(page(i+1,p) for i,p in enumerate(P))}{src}</body></html>"
open("/tmp/claude-0/-home-claude/7f1459fd-826e-5191-b8ff-48096a85b870/scratchpad/q20/q20.html", "w", encoding="utf-8").write(out)
print("ok")
