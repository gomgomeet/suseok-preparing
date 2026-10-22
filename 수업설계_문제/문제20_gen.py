import json, html, sys
sys.path.insert(0, "/tmp/claude-0/-home-claude/7f1459fd-826e-5191-b8ff-48096a85b870/scratchpad/q20")
from data import P
S = json.load(open("/tmp/claude-0/-home-claude/7f1459fd-826e-5191-b8ff-48096a85b870/scratchpad/stds.json", encoding="utf-8"))
e = html.escape
assert len(P) == 20

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

def stds(p):
    return "".join(f'<p><span class="code">[{c}]</span>{e(S[c])}</p>' for c in p["std"])

def page(i, p):
    code, (a, b, c) = p["lv"][0], p["lv"][1]
    li = lambda xs: "<ul>" + "".join(f"<li>{e(x)}</li>" for x in xs) + "</ul>"
    return f"""
<section class="page">
 <div class="qhead"><div class="qno">문항 {i:02d}</div>
  <div class="qmeta">초등 {e(p['band'])} {e(p['subj'])} <span>· {e(p['area'])} 영역 · 권장 {e(p['hours'])}</span></div></div>
 <div class="box std"><h3>성취기준</h3>{stds(p)}</div>
 <div class="box"><h3>핵심 아이디어</h3>{li(p['ki'])}</div>
 <div class="box"><h3>내용 요소 ({e(p['band'])})</h3>
  <table class="ke"><tr><th>지식·이해</th><td>{' · '.join(e(x) for x in p['ku'])}</td></tr>
  <tr><th>과정·기능</th><td>{' · '.join(e(x) for x in p['pf'])}</td></tr>
  <tr><th>가치·태도</th><td>{' · '.join(e(x) for x in p['va'])}</td></tr></table></div>
 <div class="box"><h3>성취수준 — [{code}]</h3>
  <table class="lv"><tr><th>A</th><td>{e(a)}</td></tr><tr><th>B</th><td>{e(b)}</td></tr><tr><th>C</th><td>{e(c)}</td></tr></table></div>
 <div class="box ctx"><h3>학교·학급 상황</h3>{e(p['ctx'])}</div>
 <div class="box cond"><h3>이 문항의 설계 조건</h3><ol>{''.join(f'<li>{e(x)}</li>' for x in p['cond'])}</ol></div>
 <p class="task">위 자료를 바탕으로 [공통 설계 과제] ①~⑥에 따라 단원 수업 설계안과 공개 차시 과정안을 작성하시오. (권장 시간 50~60분)</p>
</section>"""

rows = "".join(f"<tr><td>{i+1:02d}</td><td>{e(p['band'])}</td><td>{e(p['subj'])} · {e(p['area'])}</td><td>{' '.join('['+c+']' for c in p['std'])}</td><td>{e(p['hours'])}</td></tr>" for i, p in enumerate(P))

cover = f"""
<section class="page">
 <span class="kicker">수석교사 2차 심사 대비 · 수업 및 평가 설계</span>
 <h1>깊이있는 수업 설계 문제 20</h1>
 <p class="sub">성취기준 · 핵심 아이디어 · 내용 요소(지식·이해, 과정·기능, 가치·태도) · 성취수준을 제시하고, 이를 바탕으로 단원과 공개 차시를 계획하는 문제</p>
 <table class="list"><tr><th>번호</th><th>학년군</th><th>교과 · 영역</th><th>성취기준</th><th>권장 차시</th></tr>{rows}</table>
 <p class="note">성취기준·핵심 아이디어·내용 요소는 2022 개정 교육과정(교육부 고시 제2022-33호) 교과 교육과정의 내용 체계에서 해당 부분을 옮겼습니다. 성취수준(A·B·C)은 한국교육과정평가원의 초등 성취수준(3단계) 진술 방식에 맞추어 출제용으로 구성한 것이므로, 실제 평가 계획에 쓸 때는 평가원 「성취기준별 성취수준」 원문과 대조하세요.</p>
</section>"""

guide = """
<section class="page">
 <h2>답안 작성 안내 — 공통 설계 과제</h2>
 <p class="small">각 문항의 제시 자료를 분석하여 아래 ①~⑥을 모두 작성합니다. 경기도교육청 「초등 깊이있는 수업 프레임워크」의 단원 설계 3단계(교육과정 살펴보기 → 학습으로의 평가 설계 → 수업 설계)와 「탐구-실행-성찰과정 프레임워크 2.0」의 깊이있는 단원 수업 설계안 틀을 따릅니다.</p>
 <ol class="tasks">
  <li><b>교육과정 살펴보기</b> — 단원(주제)명, 핵심어 3~5개, 제시된 핵심 아이디어를 학년·학급 수준으로 재구성한 <b>핵심 문장</b>(명제형, 개념 간 관계 진술), 핵심 문장을 추론하게 하는 <b>핵심 질문</b>. 핵심 문장 뒤에 "때문에 학생은 [성취기준]"을 붙여 읽어 자연스러운지 점검합니다.</li>
  <li><b>탐구 질문</b> — 핵심 질문에 차츰 다가가도록 학생의 탐구를 이끄는 질문 3~4개(단원 흐름 순서). 질문의 유형을 엄밀히 나누기보다 탐구 과정에 필요한 질문으로 쓰고, 학생이 질문을 만들고 고르는 과정을 넣을 수 있습니다.</li>
  <li><b>삶의 맥락</b> — 경기도교육청 8가지 삶의 맥락 중 1~2개를 골라 단원과 연계하는 방안.</li>
  <li><b>학습으로의 평가</b> — 무엇을 평가하는가 / 왜 평가하는가(핵심 문장 이해 확인) → <b>GRASPS</b> 평가 과제(목표·역할·청중·상황·결과물·준거) → 제시된 <b>성취수준</b>과 연결한 수행 수준(3~4단계, 관찰 가능한 행동으로) → 형성평가와 피드백 계획 1가지 이상.</li>
  <li><b>탐구–실행–성찰 수업 흐름</b> — 차시 흐름(준비 → 탐구 → 정리 → 실천)과 차시별 탐구 질문, 그중 <b>공개 차시 1차시 과정안</b>(도입–전개–정리, 수업 방법, 수업·평가 연계의 주안점).</li>
  <li><b>포용과 맞춤형 지원</b> — 성취수준 C에 머무를 수 있는 학생을 위한 단계적 실마리와, A 수준 학생을 위한 도전 과제.</li>
 </ol>
 <div class="grid">
  <div class="box"><h3>경기도교육청 8가지 삶의 맥락</h3><ol class="small">
   <li>개인과 사회 공동의 행복</li><li>정체성과 자기주도성</li><li>보편적 사회복지</li><li>포용력과 이해력</li>
   <li>공감과 상호 협력</li><li>생태 전환과 기후 변화</li><li>디지털 전환과 AI</li><li>책임 있는 민주시민</li></ol></div>
  <div class="box"><h3>GRASPS</h3><ul class="small">
   <li><b>G</b>oal 목표 — 과제가 이루려는 것</li><li><b>R</b>ole 역할 — 학생이 맡는 실제 역할</li><li><b>A</b>udience 청중 — 결과를 보고 들을 대상</li>
   <li><b>S</b>ituation 상황 — 실세계 맥락</li><li><b>P</b>roduct 결과물 — 만들어 낼 산출물·수행</li><li><b>S</b>tandard 준거 — 성공을 판단할 기준</li></ul></div>
 </div>
 <div class="box"><h3>스스로 채점하기 (100점)</h3>
  <table class="rub small"><tr><th>항목</th><th>관점</th><th>배점</th></tr>
  <tr><td>단원 설계 일관성</td><td>핵심어·핵심 문장·핵심 질문이 성취기준·핵심 아이디어와 맞는가. 핵심 문장이 목표형(~할 수 있다)이 아닌 명제형으로 관계를 진술하는가</td><td>20</td></tr>
  <tr><td>탐구 질문</td><td>핵심 질문에 다가가도록 차시를 잇고, 학생이 실제로 탐구할 수 있으며 학년 눈높이에 맞는가</td><td>15</td></tr>
  <tr><td>단원 흐름·삶의 맥락</td><td>차시가 개념을 잇는 흐름으로 조직되고, 삶의 맥락이 형식이 아니라 탐구와 실천에 녹아 있는가</td><td>15</td></tr>
  <tr><td>공개 차시 과정안</td><td>질문이 생기는 도입 → 학생 탐구 → 학생이 만드는 일반화 → 성찰이 이어지는가</td><td>20</td></tr>
  <tr><td>학습으로의 평가</td><td>평가 과제가 핵심 문장 이해를 새로운 상황에서 확인하고, 수행 수준이 제시된 성취수준과 일관되며 관찰 가능한가</td><td>20</td></tr>
  <tr><td>포용·피드백</td><td>C 수준 학생의 단계적 실마리, A 수준 학생의 도전, 형성평가에 따른 피드백이 구체적인가</td><td>10</td></tr></table></div>
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
 <p class="note">성취수준(A·B·C)은 출제용으로 구성한 것입니다. 한국교육과정평가원 「2022 개정 교육과정에 따른 성취기준별 성취수준(초등학교)」 원문과 문구가 다를 수 있습니다.</p>
</section>"""

out = f"<!doctype html><html lang='ko'><head><meta charset='utf-8'><title>깊이있는 수업 설계 문제 20</title><style>{CSS}</style></head><body>{cover}{guide}{''.join(page(i+1,p) for i,p in enumerate(P))}{src}</body></html>"
open("/tmp/claude-0/-home-claude/7f1459fd-826e-5191-b8ff-48096a85b870/scratchpad/q20/q20.html", "w", encoding="utf-8").write(out)
print("ok")
