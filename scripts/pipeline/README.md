# 성취기준 학년별 배치 파이프라인

학교 연간 지도 계획(hwp)은 저장소에 올리지 않습니다. 계획서를 받아 다시 배치할 때 순서:

1. `hwptxt.py` 로 hwp 본문을 텍스트로 추출 (파일명: `2026년도_N학년 N학기_교과_연간 지도 계획.txt`)
2. `units2.py txt폴더 > units2.json` 으로 단원명 후보 추출
3. `final.py 초등_성취기준_전체.csv txt폴더 units2.json ../standards_by_grade.json`
   - `match.py` 의 문장 유사도 대조 결과에 `final.py` 의 검토 보정(O 사전)을 덮어씀
4. `python3 scripts/build.py && python3 scripts/build_xlsx.py`

성취기준 원문 CSV: gomgomeet/suseok-exam `prep-materials` 브랜치 `06_교육과정/성취기준/`
