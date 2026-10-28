# 보관 검토

승인 원고의 제목·다섯 절·두 발췌·두 이미지의 설명과 출처를 읽었습니다. 역사적 파일의 두 이미지 상대 경로 ../images/를 images/로 정규화하면 초기 원고와 현재 원고의 차이는 마지막 ‘본문 읽기’ 한 문단 삭제뿐입니다. 다섯 개 GODpia 절 링크가 그대로 남습니다. 원고의 표현이나 줄임말, 절 제목을 추가 교정하지 않았습니다.

두 실제 JPEG 픽셀을 직접 열어 확인했습니다. 볼 판화는 세로 460×595이며 천사와 기드온, 제물 장면입니다. 양털 삽화는 원본 1142×1700, EXIF 방향 8을 적용한 가로 1700×1142이며 천막 앞에서 양털을 짜는 장면과 그릇이 바르게 보입니다. 원본 바이트와 방향 메타데이터를 보존했습니다.

사실 검토, 초기 전체 native preview 검토, 최신 한 문단 삭제 검증을 별개로 보관합니다. 42개 스크린샷은 해시·텍스트 목록만 있으며 이 소비자가 픽셀·방향을 재검사한 것으로 주장하지 않습니다. 1844×1183 캡처 크기를 mobile viewport로 오인하지 않습니다. 제공된 측정값은 PC1280/mobile360 preview를 기록합니다.

private native 원본·서명 URL·스크린샷 바이트·Library 내부 참조는 제외했습니다. sanitized HTML은 정확한 native payload나 재게시용 파일이 아닙니다. canonical source-pass/final-page/remote/native 증거를 재구성하거나 strict gate PASS를 만들지 않습니다. published는 기존 실제 게시 상태이며 strict 완료 선언이 아닙니다.

## 저장소 검사 결과

기본 검사: 오류 8개. 승인된 다섯 H2의 레벨, 두 절 제목의 ~다 종결, 인용 귀속의 em dash가 현재 저장소 편집 규칙과 다릅니다. 사용자의 보관·한 문단 삭제 범위를 지키기 위해 기존 승인 문장을 변경하지 않았습니다.

strict 검사: revision_required. 보관용 Markdown 이미지와 native media directives 차이, 비공개 native attachment/CDN 바인딩과 canonical remote/source/final-page 기록 누락을 보고합니다. 원본과 역사적 검토는 보관했지만 새 strict gate를 통과한 배포 산출물이 아닙니다. 검사 출력은 artifacts/qa-v2에 보존했습니다.

archive verify_archive.py: PASS (24 manifest 항목, 25 파일, 본문 동등성, 경로 정규화 후 한 문단 삭제, HTML의 5절·5링크·2이미지, 15 인용 단어, 이미지 원본 바이트, 42개 역사적 캡처 목록). 기본 git diff --check는 원본 보존 파일의 마지막 빈 줄과 patch 문맥의 공백을 지적합니다. 원본 해시 보존을 위해 그대로 두었으며 blank-at-eof/blank-at-eol만 제외한 diff 검사로 추가 오류가 없는지 확인합니다.
