# 수능 제출 조건 정정: 독립 소스 재검증

검토일: 2026-11-14. 검토자: independent_article_review.

**판정: pass (수정 원고의 source gate).** 현재 `status: reviewing`인 article.md 전체를 먼저 cold-read한 뒤 brief/evidence/claims와 보존된 공식 원자료를 읽었다. 본문이나 근거 파일을 수정하지 않았다. Library/Git/게시 작업은 하지 않았다.

이전 독립 검토는 수능의 ‘단순 소지’ 요약을 확인하면서 **1교시 전 제출 절차를 놓쳤다.** 이전 pass는 조건이 누락된 옛 원고에 관한 부정확한 판정이므로 수정본의 근거로 재사용하지 않는다. 이번 검토에서는 제출 시점·반환 시점·미제출 소지·시험 중 사용·확인 불응을 각각 확인했다.

## Cold-read 결과

현재 글은 AI 안경의 카메라/소리/화면과 한국·해외 구매 조건을 소개하고, 시험별로 지켜야 할 금지·검사·제재를 구분한다. 제품 설명에서 구매 조건, 예약 후보, 시험 규정으로 이어지는 기존 흐름을 유지한다.

수정한 수능 표에는 ‘가져왔다면 1교시 전 제출’과 ‘미제출 소지 적발’이 함께 보인다. 뒤 첫 문단은 실제로 가져왔을 때 제출하고 돌려받는 순서를 설명하며, 둘째 문단은 시험 중 착용을 포함한 사용과 확인 요구 불응을 설명한다. 따라서 독자는 ‘실수로 시험장에 가져온 순간 자동 무효’라고 읽지 않고, 제출 시점과 별도 위반 행위를 알 수 있다. 바로 다음 SAT 문단은 다른 시험의 규칙으로 자연스럽게 전환된다.

## 원자료 대조

1. **공식 Q&A, IV ‘시험 응시’ 03번, 인쇄/PDF 46쪽**
   - [공식 PDF](https://www.ice.go.kr/upload/ice/na/bbs_1482/2026/04/b38c68a1f07bfba215f2107e1e040910.pdf)
   - 보존 PDF의 추출 텍스트와 실제 페이지 raster `qa-03-page46.png`를 열어 함께 대조했다. 실수 또는 불가피하게 가져온 반입 금지 물품은 첫 교시 전 감독관에게 내고, 본인이 응시하는 모든 영역/과목을 마친 뒤 돌려받는 순서다. 해당 시점까지 내지 않은 경우를 부정행위로 본다. 수정 본문의 제출·반환 설명과 일치한다. 45쪽에도 같은 취지의 일반 관리 절차가 있다.
2. **교육부 2026-11-09 수험생 안내**
   - [공식 게시물](https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=294&boardSeq=107599&lev=0&m=020402&s=moe)
   - 보존 HWPX를 ZIP으로 열고 `Contents/section*.xml`을 독립 파싱했다. 스마트안경을 반입 금지 전자기기에 포함한 문단과, 첫 교시 전 수거 시간에 감독관 지시로 제출하도록 한 다음 문단을 함께 읽었다. 계속 가지고 있다가 적발되는 경우 시험을 무효로 처리한다는 조건이 명시된다. 같은 문서의 표도 스마트안경과 제출 시점을 함께 안내한다.
   - 별도 주의사항에서 시험 중 착용을 사용으로 취급하고 당해 무효와 다음 해 응시자격 박탈을 안내한다. 확인 요구 불응은 심의를 거치는 별도 항목이다. 수정 표·두 문단과 일치한다.
3. **교육부 2026-10-29 스마트안경 대응계획**
   - [공식 게시물](https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=294&boardSeq=107520&lev=0&m=020402&s=moe)
   - 보존 HWPX의 XML을 독립 파싱했다. 시험 중 사용(착용 포함), 반입·단순 소지, 확인 불응을 구분한 표와 본문을 확인했다. 확인 불응의 심의 조건이 보존됐다. 이 자료의 짧은 단순 소지 요약에는 제출 절차가 나타나지 않지만, 더 구체적인 Q&A와 최신 11/9 문서의 제출 절차를 폐지한다는 문구도 찾지 못했다.

## 스마트안경의 별도 절차 및 해석 한계

- 확인한 세 자료에서 소비자용 스마트안경에만 적용되는 별도 제출 면제나 다른 수거·반환 절차는 찾지 못했다. 특히 11/9 안내는 **한 문서 안에서** 스마트안경을 포함한 금지 목록과 첫 교시 전 제출 절차를 안내한다. 따라서 별도 강화계획의 도표만 떼어 읽어, 제출 절차 자체가 사라졌다고 해석하지 않는다.
- 다만 11/9 문서와 Q&A에는 개인의 신체조건·의료상 이유로 필요한 물품을 매 교시 감독관의 사전 점검 뒤 휴대할 수 있다는 일반 규정도 있다. 이를 소비자용 AI 안경의 자동 허용 또는 제출 면제라고 명시한 규정은 확인하지 못했다. 이번 검토는 개별 의료기기 승인 여부나 모든 예외 사례를 판정하지 않는다.
- 사용·착용 제재는 본문처럼 **시험 중**이라는 조건을 보존해야 한다. 일반적인 실수 반입 및 제출 절차와 합치지 않는다. 확인 불응 역시 심의 조건을 삭제하면 안 된다.
- 최신 안내의 단순 소지 도표에도 짧은 요약이 반복되므로, 독자는 같은 문서 앞의 제출 조건과 함께 읽어야 한다. 수정 원고는 그 문맥을 표와 본문에 반영했다.

## 접근과 검증 범위

교육부의 두 공식 게시물은 웹 도구로 열어 제목·일자·해당 HWPX 첨부를 확인했다. 다운로드 링크는 웹 도구의 `application/octet-stream` 미지원으로 본문 파싱이 되지 않아, 저장된 HWPX 원본을 직접 XML로 읽었다. Q&A 온라인 PDF 열기는 timeout이었다. 이를 온라인 열람 성공으로 쓰지 않았으며, 보존 PDF·추출문·실제 페이지 이미지를 대조했다. 이번 독립 검토가 원격 파일을 새로 다운로드해 바이트 동일성까지 확인했다는 뜻은 아니다.

`before-article.md`와 현재 article.md의 diff를 확인했다. 변경은 수능 표·기존 수능 문단을 대체한 두 문단·세 출처 추가이며, 다른 제품과 시험 본문은 바뀌지 않았다. `python3 scripts/blog.py check posts/2026-11-14-ai-glasses-products-exam-rules` 결과는 **오류 0, 경고 0**이다.

현재 article/brief/evidence/claims의 수능 조건은 일치한다. 이 source pass는 새 PDF·HTML 파생본이 갱신됐거나 시각 검토를 마쳤다는 판정이 아니다. 이전 파생본 및 예전 pass 기록을 그대로 전달하지 말고, 수정 소스로 재생성한 산출물의 적절한 렌더 검토가 필요하다.

## 검토 대상 SHA-256

- article.md: `f52fc3d90a94d80f5b78ad0285b4902974025fc8fad3cf76886df868709ab9b7`
- brief.md: `65d018433ed5a077e1b39798dbbd53acfe22cb860c6ccef408731f6f3a584e75`
- evidence.md: `5c72c70a46bcbe9d1515c4726f0c75625fefa1bc2f1eb10872e58f3719ebf045`
- artifacts/claims.json: `d20188d5b0213c001d40875280eb7f559248f0b48d66f6867dda50f8bcfbfe25`

원자료 식별:

- 2027-csat-official-qa.pdf: `bbeff8d8ff7add6cd4d5e16ecb3386d7df456cf6275193c2d3a08bce9331d4bd`
- moe-smart-glasses-plan-20261029.hwpx: `78e953c6fae12aebb115fe27e39327a5e4c71b9b5d92350377ba947653370a6c`
- moe-csat-notice-20261109.hwpx: `1ec91f3b69729d1a2b5e49c8a4cc94ace2c517c7d26fda11973a5513910f0fff`

## 수정본 로컬 반응형 재검토

**별도 판정: local-draft responsive pass.** source pass 뒤 요청받아 `python3 /Users/ja2sng/Documents/Codex/2026-11-14/task-2/capture_local_review.py csat-independent`를 실제 실행했다. 증거는 bundle의 `artifacts/qa-v2/local-browser-csat-independent/receipt.json`과 light/dark 각 1280·360·390 전체 PNG 6종이다. PNG 6종을 모두 `view_image`로 열어 읽었다.

- 여섯 프로필 전부 페이지 가로 넘침 0, H1 1개, 고유 목차 타깃, 이미지 3개 로딩이다.
- 1280 표는 760/760px, 360은 320/620px, 390은 350/620px이며 내부 overflow-x:auto다. 360에서 수정된 시험 표를 오른쪽 끝까지 실제 스크롤하고 light/dark focused 캡처를 열어 새 제출 조건과 미제출 적발·착용 제재가 셀 안에서 모두 읽히는지 확인했다. 바로 아래 첫 문단의 제출 시점 강조도 잘리거나 겹치지 않는다.
- 새 수능 두 문단은 360·390에서 자연스럽게 줄바꿈되며, 문장 끝·출처 링크·다음 SAT 문단이 잘리거나 다른 절과 겹치지 않는다. 제목·캡션·목차·나머지 이미지의 배치도 정상이다.
- dark 전체 캡처에서 리드가 흰 공백으로 나타나는 기존 full-page paint omission은 이번에도 관찰됐다. 현재 수정본 HTML을 새 Chromium 뷰포트에서 열고 decode 완료 뒤 focused 캡처하니 실제 안경 픽셀은 정상이다. 전체 캡처가 모두 정상이라고 보고하지 않으며, 정상 focused 관찰을 함께 보존해 capture omission과 실제 이미지 공백을 구분한다.

새 focused 증거는 task-2/csat-correction의 `independent-dark-360-lead-focus.png`, `independent-dark-360-lead-decoded.png`, `independent-light-360-table-3-right.png`, `independent-dark-360-table-3-right.png`다. 옛 증거 파일을 덮어쓰지 않는 별도 경로다.

최신 delivery HTML SHA-256: light `0d974d4e4d26214171739b2730730e0391406d762c2a43335f5e90adb9c00532`, dark `29dc993953d2542ea767c7a2db85a2666be57dbd2100ef2173600a6b9fa81e2d`. 로컬 검토 종료 시 article/brief/evidence 해시는 위 source pass 값과 같았다. 새 PDF 7쪽의 별도 검토는 같은 디렉터리 `pdf-review.md`에 기록했다. native Tistory/CDN 발행 gate는 수행하지 않았다.
