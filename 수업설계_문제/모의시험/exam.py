import json, html
e = html.escape
D = "/tmp/claude-0/-home-claude/7f1459fd-826e-5191-b8ff-48096a85b870/scratchpad/"
KI = json.load(open(D + "ki/ki.json", encoding="utf-8"))

def ki(subj, area):
    return next(b["ki"] for b in KI[subj] if b["area"] == area)

EX = [
dict(tag="A", file="모의문제지_샘플A_6학년_미술", grade="6학년", subj="미술", area="감상", unit="작품과 대화하기(감상 단원 재구성)", hours=8,
 std=[("6미03-01","미술 작품을 작품이 만들어진 시대적, 지역적 배경 등과 연결하여 이해할 수 있다."),
      ("6미03-02","미술 작품의 내용(소재, 주제 등)과 형식(재료와 용구, 표현 방법, 조형 요소와 원리 등)을 분석하여 작품의 특징을 설명할 수 있다."),
      ("6미03-04","다양한 방법을 활용하여 작품을 감상하며 작품에 관한 서로 다른 관점을 존중할 수 있다.")],
 ctx="학생 24명. 학생들은 '사진처럼 똑같이 그린 그림이 잘 그린 그림'이라고 여기고, 추상 작품을 보면 \"나도 그리겠다\"며 웃어넘긴다. 다음 달 지역 미술관에서 지역 작가 기획전이 열려 학급 단위 관람이 1회 가능하다. 미술에 자신감이 낮아 감상 발표를 꺼리는 학생 4명. 1인 1태블릿.",
 cond=["단원을 8차시로 계획하되, 차시마다 '준비–탐구–정리·실천–성찰' 중 어느 단계인지 표시할 것",
       "제시된 핵심 아이디어에서 핵심어 3개 이상을 뽑고, 핵심 문장(학생이 남길 이해 1문장), 핵심 질문 1개, 핵심 질문에 다가가는 탐구 질문 2~3개를 제시할 것",
       "학생이 작품을 보고 스스로 질문을 만들고, 모둠에서 탐구 질문으로 다듬는 장면을 1개 이상 포함할 것",
       "미술관 관람을 몇 차시에 둘지 정하고, 관람 전·후 활동과 어떻게 이어지는지 쓸 것",
       "단원 중간에 징검다리 평가 1회를 배치하고, 그 결과를 다음 차시에 어떻게 반영할지 쓸 것",
       "디지털 도구를 1개 이상 활용하고 학습 목표와 연결된 선정 이유를 쓸 것. 감상 발표를 꺼리는 학생을 위한 개별화 전략과, 서로 다른 관점을 존중하기 위한 대화 규칙을 각 1가지 이상 쓸 것"],
 note2="감상 유의점",
 scene=[("장면 1", "작품을 보고 학생이 질문 만들고 다듬기"), ("장면 2", "내용·형식을 근거로 해석 말하기 (서로 다른 관점)")],
 cons=dict(gu="4학년 사회", unit="3. 지역의 역사와 문화유산", lesson="5/10차시(40분)",
   std="[4사06-02] 지역의 박물관, 기념관, 유적지 등을 체험하고 지역의 역사를 이해한다.",
   goal="우리 지역 문화유산의 이름과 특징을 말할 수 있다.",
   flow=["도입(5분): 지난주 현장 체험학습 사진 보기, 학습 목표 읽기",
         "전개(30분): 교사가 PPT로 문화유산 5곳의 역사 설명(15분) → 학습지 빈칸 채우기(10분) → 체험학습 때 찍은 사진을 패들릿에 올리기(5분)",
         "정리(5분): 학습지 정답 확인, 다음 차시 예고"],
   ev="학습지 빈칸 10개 중 8개 이상 맞히면 '도달', 미만이면 '미도달'",
   obs="패들릿에는 친구와 찍은 사진이 대부분이고 문화유산에 대한 설명이나 질문은 거의 없었음. PPT 설명 중 엎드려 있는 학생이 5명 있었음.",
   worry="\"현장 체험학습을 다녀와도 놀러 간 기억만 남는 것 같아요. 학습지를 더 많이 풀게 해야 할까요?\""),
),
dict(tag="B", file="모의문제지_샘플B_2학년_통합교과", grade="2학년", subj="통합교과", area="우리는 지금 어떻게 살아갈까", unit="가을아, 놀자(주제 단원 재구성)", hours=10,
 std=[("2바03-02","계절의 변화에 대응하며 생활한다."),
      ("2슬03-02","계절과 생활의 관계를 탐구한다."),
      ("2즐03-02","자연의 변화를 느끼며 놀이한다.")],
 ctx="학생 20명. 학교 뒤뜰에 은행나무와 작은 텃밭이 있지만 학생들은 쉬는 시간 대부분을 실내에서 보낸다. 날씨가 쌀쌀해졌는데도 얇은 옷차림으로 등교하는 학생이 많고, \"가을은 그냥 시원한 날\"이라고 말한다. 글쓰기가 아직 서툰 학생 5명, 한국어가 서툰 다문화 학생 1명.",
 cond=["주제 단원을 10차시로 계획하되, 차시마다 '준비–탐구–정리·실천–성찰' 중 어느 단계인지와 관련 교과(바·슬·즐)를 표시할 것",
       "제시된 핵심 아이디어에서 핵심어 3개 이상을 뽑고, 2학년 눈높이의 핵심 문장(학생이 남길 이해 1문장), 핵심 질문 1개, 핵심 질문에 다가가는 탐구 질문 2~3개를 제시할 것",
       "학교 뒤뜰에서 계절의 변화를 관찰한 뒤 학생이 스스로 궁금한 것을 말하고, 학급의 탐구 질문으로 모으는 장면을 1개 이상 포함할 것",
       "계절에 맞는 생활 실천(옷차림, 건강 등)이 가정과 이어지도록 하는 방법을 쓸 것",
       "단원 중간에 징검다리 평가 1회를 배치하고, 그 결과를 다음 차시에 어떻게 반영할지 쓸 것",
       "디지털 도구를 1개 이상 활용하고 학습 목표와 연결된 선정 이유를 쓸 것. 야외 활동 안전 유의점 2가지 이상과, 글쓰기가 서툰 학생·한국어가 서툰 학생을 위한 개별화 전략을 각 1가지 이상 쓸 것"],
 note2="야외 안전 유의점",
 scene=[("장면 1", "뒤뜰 관찰 뒤 학생이 궁금한 것 말하고 모으기"), ("장면 2", "관찰한 것을 근거로 계절과 생활의 관계 말하기")],
 cons=dict(gu="4학년 과학", unit="5. 생물과 환경", lesson="3/9차시(40분)",
   std="[4과14-02] 생물 요소들의 먹고 먹히는 관계를 조사하여 먹이그물로 표현할 수 있다.",
   goal="먹이그물을 만들 수 있다.",
   flow=["도입(5분): 먹이사슬 동영상 시청, 학습 목표 읽기",
         "전개(30분): 교사가 먹이사슬과 먹이그물의 뜻 설명(10분) → 모둠별로 생물 카드를 전지에 붙여 먹이그물 만들기(15분) → 모둠 결과물 사진 찍어 제출(5분)",
         "정리(5분): 먹이그물의 뜻 다시 읽기, 다음 차시 예고"],
   ev="모둠 먹이그물 완성 여부(O/X)",
   obs="모둠마다 2~3명이 카드를 붙이고 나머지는 구경하거나 장난을 침. 완성한 먹이그물이 모둠마다 거의 같았고, '왜 그렇게 연결했는지' 묻자 대답하는 학생이 적었음.",
   worry="\"모둠 활동을 하면 몇 명만 하고 나머지는 놀아요. 그냥 개별 학습지로 바꾸는 게 나을까요?\""),
),
]

CSS = """
@page{size:A4;margin:13mm 14mm 12mm}
*{box-sizing:border-box}
body{font-family:"Noto Sans CJK KR",sans-serif;color:#1d2730;font-size:9.4pt;line-height:1.5;margin:0}
.page{page-break-after:always}.page:last-child{page-break-after:auto}
h1{font-size:19pt;margin:0;text-align:center}
.c{text-align:center}.sub{text-align:center;color:#5e6a72;margin:1mm 0 5mm}
table{border-collapse:collapse;width:100%;table-layout:fixed}
th,td{border:.3mm solid #8f9a95;padding:1.4mm 2mm;vertical-align:top;text-align:left}
th{background:#e1eeea;font-weight:700}
.l{width:32mm;background:#f3f6f4;font-weight:700}
.tk{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:.8mm solid #2e6b62;padding-bottom:1.5mm;margin:0 0 3mm}
.tk b{font-size:14pt;color:#2e6b62}.tk span{font-size:10pt;font-weight:700}
.tk em{font-style:normal;font-size:12pt;font-weight:800;margin-left:3mm}
.prob{margin:0 0 2.5mm}
.cond{border:.4mm solid #c4372c;border-radius:2mm;padding:2mm 3mm;margin-top:3mm}
.cond h3{margin:0 0 1mm;font-size:10pt;color:#c4372c}
ol{margin:0;padding-left:5mm}li{margin-bottom:.8mm}
ul{margin:0;padding-left:4.5mm}
.ah{font-weight:800;font-size:10.5pt;margin:4mm 0 1.5mm}
.hint{display:block;font-size:7.6pt;color:#5e6a72;font-weight:400}
.small{font-size:8.6pt}.note{font-size:8pt;color:#5e6a72}
.rule li{margin-bottom:1.2mm}
.ctr th,.ctr td.ct{text-align:center;vertical-align:middle}
.box{border:.3mm solid #b9c2bd;border-radius:2mm;padding:2mm 3mm;margin-top:3mm;background:#f5f8f6}
.box h3{margin:0 0 1mm;font-size:9.6pt;color:#2e6b62}
"""

def H(mm): return f'style="height:{mm}mm"'

def exam(x):
    k = ki(x["subj"], x["area"])
    subjname = "통합교과(바른 생활 · 슬기로운 생활 · 즐거운 생활)" if x["subj"] == "통합교과" else x["subj"]
    stds = "".join(f"<p style='margin:0 0 .8mm'><b>[{c}]</b> {e(t)}</p>" for c, t in x["std"])
    kis = "<ul>" + "".join(f"<li>{e(s)}</li>" for s in k) + "</ul>"
    c = x["cons"]
    cover = f"""<section class="page">
 <p class="c" style="margin:6mm 0 1mm;font-weight:700">2027 수석교사 자격연수 대상자 선발 대비</p>
 <h1>2차 심사(역량평가) 모의 문제지</h1>
 <p class="sub">초등 · 수업 영역(과제 1~3) · 샘플 {x['tag']} · 연습용</p>
 <table><tr><th style="width:24mm">수험번호</th><td></td><th style="width:20mm">성명</th><td></td></tr>
 <tr><th>응시일</th><td>2026.&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;&nbsp;.</td><th>총 소요 시간</th><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;분</td></tr></table>
 <table class="ctr" style="margin-top:5mm"><tr><th style="width:12mm">과제</th><th>내용</th><th style="width:36mm">평가 영역</th><th style="width:14mm">배점</th><th style="width:30mm">제한 시간</th></tr>
 <tr><td class="ct">1</td><td>교수·학습과정안(평가계획 포함) 작성</td><td class="ct">수업 및 평가 설계</td><td class="ct">10</td><td class="ct">50분</td></tr>
 <tr><td class="ct">2</td><td>수업 설명 및 수업 시연 준비</td><td class="ct">수업 수행</td><td class="ct">15</td><td class="ct">설명 10분 · 시연 10분</td></tr>
 <tr><td class="ct">3</td><td>수업 및 평가 컨설팅 보고서 작성</td><td class="ct">수업 및 평가 컨설팅</td><td class="ct">15</td><td class="ct">50분</td></tr></table>
 <div class="ah">응시자 유의사항</div>
 <ol class="rule small">
  <li>배점은 제2회 모의 문제지와 같이 「2027 수석교사 자격연수 대상자 선발 계획」(경기도교육청, 2026. 9.)의 2차 심사 평가영역을 따랐습니다. 과제 4·5(심층면접)는 이 문제지에서 다루지 않습니다.</li>
  <li>과제별 시간과 형식은 연습용입니다. 실제 방식은 2차 심사 세부계획으로 확인하세요.</li>
  <li>타이머를 켜고 제한 시간 안에 작성합니다. 시간이 끝나면 쓰던 곳에 표시하고 멈춥니다.</li>
  <li>문제에 제시된 성취기준과 핵심 아이디어는 2022 개정 교육과정 원문이며, 핵심 아이디어는 해당 영역의 것을 모두 실었습니다. 단원명·학급 실태·컨설팅 사례는 연습용으로 만든 가상 상황입니다.</li>
  <li>답안은 개조식과 표를 활용해 짧고 명확하게 씁니다.</li>
 </ol>
 <div class="box"><h3>쓰기 전 점검</h3><ul class="small">
  <li>핵심 문장은 '활동 다짐'이 아니라 학생이 남길 '이해'를 명제형으로 쓴다 — 뒤에 "때문에 학생은 [성취기준]"을 붙여 읽어 본다</li>
  <li>핵심 질문은 정답이 하나가 아닌 열린 질문으로, 탐구 질문은 핵심 질문에 다가가는 순서로 쓴다</li>
  <li>학습 목표는 '~할 수 있다'로, 평가 기준은 관찰 가능한 행동으로 쓴다</li>
  <li>자료(◉)·유의점(※) 칸과 S 예상 반응을 빠짐없이 채운다</li>
  <li>컨설팅은 '진단(목표–활동–평가 정렬)'부터, 다음 단계는 언제·무엇을·어떻게로 약속한다</li></ul></div>
</section>"""

    t1 = f"""<section class="page">
 <div class="tk"><div><b>과제 1</b><em>교수·학습과정안(평가계획 포함) 작성</em></div><span>50분 · 10점</span></div>
 <p class="prob">【문제】 다음 교과 정보와 조건에 맞추어 단원 차시 계획과 1차시분 교수·학습과정안, 평가계획을 작성하시오.</p>
 <table>
  <tr><td class="l">학년 · 교과</td><td>초등학교 {x['grade']} {e(subjname)} / 영역: {e(x['area'])} / 단원: {e(x['unit'])}</td></tr>
  <tr><td class="l">성취기준</td><td>{stds}</td></tr>
  <tr><td class="l">핵심 아이디어<span class="hint">교육과정 원문 · 영역 전체</span></td><td>{kis}</td></tr>
  <tr><td class="l">학급 실태</td><td>{e(x['ctx'])}</td></tr>
 </table>
 <div class="cond"><h3>〈작성 조건〉</h3><ol>{''.join(f'<li>{e(s)}</li>' for s in x['cond'])}</ol></div>
</section>"""

    rows = "".join(f"<tr><td class='ct'>{i}</td><td></td><td></td><td></td><td></td></tr>" for i in range(1, x["hours"] + 1))
    rh = 12 if x["hours"] <= 8 else 10
    a1 = f"""<section class="page">
 <div class="ah" style="margin-top:0">【답안지 1-1】 단원 설계</div>
 <table>
  <tr><td class="l">핵심 아이디어<span class="hint">위에서 중심으로 삼을 문장</span></td><td {H(13)}></td></tr>
  <tr><td class="l">핵심어</td><td {H(9)}></td></tr>
  <tr><td class="l">핵심 문장<span class="hint">학생이 남길 이해</span></td><td {H(15)}></td></tr>
  <tr><td class="l">핵심 질문</td><td {H(11)}></td></tr>
  <tr><td class="l">탐구 질문<span class="hint">핵심 질문에 다가가는 순서로</span></td><td {H(22)}>①<br><br>②<br><br>③</td></tr>
  <tr><td class="l">수업자 의도<span class="hint">학급 실태 연결</span></td><td {H(22)}></td></tr>
 </table>
 <div class="ah">【답안지 1-2】 차시 계획</div>
 <table class="ctr"><colgroup><col style="width:11mm"><col style="width:20mm"><col style="width:40mm"><col><col style="width:38mm"></colgroup>
  <tr><th>차시</th><th>단계</th><th>차시 주제</th><th>주요 활동 (탐구 질문)</th><th>평가 · 피드백</th></tr>
  {rows.replace("<tr>", f"<tr style='height:{rh}mm'>")}
 </table>
 <p class="small" style="margin-top:1.5mm">※ 징검다리 평가 차시: (&nbsp;&nbsp;&nbsp;&nbsp;)차시 → 결과 반영 방법:</p>
</section>"""

    a2 = f"""<section class="page">
 <div class="ah" style="margin-top:0">【답안지 1-3】 본시 교수·학습과정안 (&nbsp;&nbsp;&nbsp;/{x['hours']}차시, 40분)</div>
 <table>
  <tr><td class="l">학습 목표</td><td {H(11)}></td></tr>
  <tr><td class="l">탐구 질문</td><td {H(9)}></td></tr>
  <tr><td class="l">디지털 도구와<br>선정 이유</td><td {H(13)}></td></tr>
  <tr><td class="l">수업 방법(모형)</td><td {H(8)}></td></tr>
  <tr><td class="l">{e(x['note2'])}</td><td {H(13)}>①<br>②</td></tr>
 </table>
 <table class="ctr" style="margin-top:2mm"><colgroup><col style="width:20mm"><col><col style="width:12mm"><col style="width:42mm"></colgroup>
  <tr><th>단계</th><th>교수·학습 활동 (T: 발문 / S: 예상 반응)</th><th>시간</th><th>자료(◉) · 유의점(※)</th></tr>
  <tr style="height:34mm"><th>준비</th><td></td><td></td><td></td></tr>
  <tr style="height:80mm"><th>탐구</th><td></td><td></td><td></td></tr>
  <tr style="height:38mm"><th>정리 · 실천</th><td></td><td></td><td></td></tr>
  <tr style="height:26mm"><th>성찰</th><td></td><td></td><td></td></tr>
 </table>
</section>"""

    special = "감상 발표를 꺼리는 학생:<br><br><br>관점 존중 대화 규칙:" if x["tag"] == "A" else "글쓰기가 서툰 학생:<br><br><br>한국어가 서툰 학생:"
    a3 = f"""<section class="page">
 <div class="ah" style="margin-top:0">【답안지 1-4】 평가계획 (학습으로의 평가)</div>
 <table>
  <tr><td class="l">성취기준</td><td colspan="3" {H(14)}></td></tr>
  <tr><td class="l">평가 요소</td><td {H(23)}></td><td class="l" style="width:24mm">평가 방법</td><td></td></tr>
  <tr><td class="l">평가 시기</td><td {H(14)}></td><td class="l">평가 도구</td><td></td></tr>
  <tr><td class="l">평가 과제<span class="hint">삶과 이어진 수행 과제</span></td><td colspan="3" {H(35)}></td></tr>
  <tr><td class="l">매우 잘함</td><td colspan="3" {H(22)}></td></tr>
  <tr><td class="l">잘함</td><td colspan="3" {H(22)}></td></tr>
  <tr><td class="l">보통</td><td colspan="3" {H(22)}></td></tr>
  <tr><td class="l">노력 요함</td><td colspan="3" {H(22)}></td></tr>
  <tr><td class="l">피드백 ·<br>개별화 전략</td><td colspan="3" {H(61)}>{special}</td></tr>
 </table>
</section>"""

    sc = "".join(f"""<tr><td class="l" style="height:105mm">{a}<span class="hint" style="font-size:8pt;color:#1d2730">{e(b)}</span></td>
   <td>T:<br><br>S:<br><br>T(되묻기):<br><br>S:</td></tr>""" for a, b in x["scene"])
    t2 = f"""<section class="page">
 <div class="tk"><div><b>과제 2</b><em>수업 설명 및 수업 시연 준비</em></div><span>설명 10분 + 시연 10분 · 15점</span></div>
 <p class="prob">【문제】 과제 1에서 작성한 과정안을 바탕으로 수업 설명(10분)과 수업 시연(10분)을 준비하시오. 메모지에 핵심만 쓰고, 소리 내어 시간을 재며 연습합니다.</p>
 <div class="ah">【메모지 2-1】 수업 설명 (10분)</div>
 <table>
  <tr><td class="l">① 단원과 학생 실태, 재구성 이유 (2분)</td><td {H(34)}></td></tr>
  <tr><td class="l">② 핵심 아이디어·핵심 문장·핵심 질문·탐구 질문 (2분)</td><td {H(34)}></td></tr>
  <tr><td class="l">③ {x['hours']}차시 흐름과 본시의 위치 (2분)</td><td {H(34)}><span class="small">{' → '.join(f'{i}차시' for i in range(1, x['hours'] + 1))}<br>(본시: ○차시)</span></td></tr>
  <tr><td class="l">④ 핵심 장면·발문, 도구 선정 근거 (2분)</td><td {H(34)}></td></tr>
  <tr><td class="l">⑤ 평가·피드백, 개별화 전략 (2분)</td><td {H(34)}></td></tr>
 </table>
</section>
<section class="page">
 <div class="ah" style="margin-top:0">【메모지 2-2】 수업 시연 (10분) – 보여 줄 장면 2개</div>
 <table>{sc}</table>
 <p class="small" style="margin-top:2mm">【자기 점검】 실제 소요 시간 설명 (&nbsp;&nbsp;&nbsp;)분 / 시연 (&nbsp;&nbsp;&nbsp;)분<br>
 ※ 장면 1에서 질문을 만드는 사람이 '학생'인지, 장면 2에서 학생이 '근거'를 말하는지 확인합니다.</p>
</section>"""

    t3 = f"""<section class="page">
 <div class="tk"><div><b>과제 3</b><em>수업 및 평가 컨설팅 보고서 작성</em></div><span>50분 · 15점</span></div>
 <p class="prob">【문제】 다음은 ○○초등학교 경력 4년 차 교사가 수업 컨설팅을 요청하며 제출한 수업 계획과 수업 관찰 메모이다. 이 교사를 위한 수업 및 평가 컨설팅 보고서를 작성하시오.</p>
 <p class="note">〈제시 자료〉 ※ 연습용으로 만든 가상 사례입니다.</p>
 <table>
  <tr><td class="l">학년 · 교과</td><td>{e(c['gu'])} / 단원: {e(c['unit'])} / 본시: {e(c['lesson'])}</td></tr>
  <tr><td class="l">성취기준</td><td>{e(c['std'])}</td></tr>
  <tr><td class="l">학습 목표</td><td>{e(c['goal'])}</td></tr>
  <tr><td class="l">수업 흐름</td><td><ul>{''.join(f'<li>{e(s)}</li>' for s in c['flow'])}</ul></td></tr>
  <tr><td class="l">평가</td><td>{e(c['ev'])}</td></tr>
  <tr><td class="l">수업 관찰 메모</td><td>{e(c['obs'])}</td></tr>
  <tr><td class="l">수업자 고민</td><td>{e(c['worry'])}</td></tr>
 </table>
 <div class="ah">【답안지 3】 컨설팅 보고서</div>
 <table>
  <tr><td class="l">1. 수업 개요와 수업자 의도·고민 진단</td><td {H(30)}></td></tr>
  <tr><td class="l">2. 강점<span class="hint">근거 장면 포함</span></td><td {H(26)}>①<br><br>②<br><br>③</td></tr>
 </table>
</section>
<section class="page">
 <table>
  <tr><td class="l">3. 개선점<span class="hint">이유 포함</span></td><td {H(34)}>①<br><br><br>②</td></tr>
  <tr><td class="l">4. 구체적 지원 방안<span class="hint">핵심 질문·학생 탐구·대화 장면 재설계</span></td><td {H(58)}></td></tr>
  <tr><td class="l">5. 평가 개선안<span class="hint">4단계 기준</span></td><td {H(42)}>매우 잘함:<br><br>잘함:<br><br>보통:<br><br>노력 요함:</td></tr>
  <tr><td class="l">6. 다음 단계<span class="hint">언제·무엇을·어떻게</span></td><td {H(34)}>(1)<br><br>(2)<br><br>(3)</td></tr>
 </table>
 <div class="box"><h3>채점 관점 (과제 1·3)</h3><ul class="small">
  <li>성취기준 – 핵심 아이디어 – 핵심 문장 – 핵심 질문 – 활동 – 평가가 한 줄로 이어지는가</li>
  <li>학생이 질문하고 탐구하는 장면이 구체적인가 (질문을 만드는 사람이 학생인가)</li>
  <li>디지털 도구가 학습 목표와 연결되어 있는가</li>
  <li>평가 기준이 학생 반응(관찰 가능한 행동)으로 구분될 만큼 구체적인가</li>
  <li>징검다리 평가 결과가 다음 차시 수업에 반영되는가</li>
  <li>컨설팅 제안마다 '왜'와 '어떻게'가 함께 있고, 수업자의 의도와 강점을 존중하는가</li></ul></div>
</section>"""

    return f"<!doctype html><html lang='ko'><head><meta charset='utf-8'><title>모의 문제지 샘플 {x['tag']}</title><style>{CSS}</style></head><body>{cover}{t1}{a1}{a2}{a3}{t2}{t3}</body></html>"

for x in EX:
    open(D + f"mock/{x['file']}.html", "w", encoding="utf-8").write(exam(x))
print("ok")
