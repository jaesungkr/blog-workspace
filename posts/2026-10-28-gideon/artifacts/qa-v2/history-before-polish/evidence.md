# 근거와 출처

원본 전달 패키지 25개 파일을 artifacts/approved-source/에 바이트 그대로 보관했습니다. archive-manifest.json의 24개 항목은 크기와 SHA-256을 모두 검증했습니다. article.md는 frontmatter 추가, 중복 H1 제거, 두 상대 이미지 경로만 assets/로 변경했습니다.

- 사사기 6~8장의 직접 기록과 해석 구분, 군사 수, 에봇의 모양에 관한 한계: independent-factual-source-review-redacted.json. 해당 검토자의 기존 사실 검토이며 이 보관 작업의 새로운 성경 조사로 주장하지 않습니다.
- 두 쉬운성경 발췌는 공백 기준 총 15단어입니다. 제공자의 사용허락 표시를 제3자의 포괄적 재게시 허가로 해석하지 않습니다.
- 이미지 출처·권리·작가·연대: images/manifest.json과 images/README.md. Ferdinand Bol의 약 1640년 작품과 작가 미상의 1873년 삽화입니다. 책 저자를 삽화 작가로 표시하지 않습니다.
- 초기 전체 native preview: independent-preview-review-redacted.json, independent-source-parity.json, qa-screenshot-inventory-redacted.json. 42장 검토 기록은 삭제 전 원고에 관한 역사적 증거입니다. 스크린샷 바이트는 전달·보관하지 않았습니다.
- 마지막 문단 삭제: footer-removal.diff, footer-removal-audit.json, footer-removal-receipt-redacted.json. 역사적 파일의 ../images/ 상대 경로를 정규화한 뒤 현재와 초기 portable Markdown을 비교해 해당 한 줄만 삭제되었음을 직접 재검증했습니다. live 저장·readback은 제공된 게시자 영수증이며 이 작업에서 live를 다시 열지 않았습니다.
- 원격 이미지 검증은 remote-images-verification.json의 게시자 기록입니다. 두 번째 이미지는 Tistory 재압축으로 원본과 바이트·픽셀이 다릅니다.

현재 승인 원격 이미지 Markdown SHA-256은 16c0b623d1bd6c30f04b51fba5377d10b1f31a75d2e1688a672015430e25e523입니다. 이미지 경로만 바뀐 portable Markdown SHA-256은 b62793d8fef6b8e8df940da103003108afc65527b49090e008392fa99562ea29입니다. 이 차이는 source-provenance.json에 기록되어 있습니다.

## Media claim registry

- ART1: Ferdinand Bol, 약 1640년, 후대의 사사기 6:21 장면. images/manifest.json의 첫 항목.
- ART2: 작가 미상, 1873년, 후대의 양털 장면. images/manifest.json의 둘째 항목. media.json은 원본 JPEG 저장 크기를 기록하고 EXIF 방향 8 및 화면 크기 1700×1142는 원본 manifest에 보존합니다.

media origin `user_supplied`는 전달 패키지에서 받은 파일이라는 저장소 enum이며 저작권 소유 주장이 아닙니다. 권리 필드와 원본 manifest는 public domain 출처를 기록합니다.

| ID | 근거 | 한계 |
| --- | --- | --- |
| ART1 | 볼의 기드온과 천사, 원본 images/manifest.json | 후대 예술적 묘사 |
| ART2 | 1873년 양털 삽화, 원본 images/manifest.json | 작가 미상, 후대 예술적 묘사 |

## 현재 승인 축약본 (2026-10-28 10:03:17 UTC 저장)

위의 25개 파일·footer-only·42장 검토 설명은 이전 전체 원고의 역사적 증거입니다. 현재 원본 패키지는 artifacts/qa-v2/revision-2026-10-28-shortened/이며 10개 파일과 manifest 9개 항목을 검증했습니다. 현재 factual PASS, 전체 native preview 30장 검토, 저장·정규화 live text 일치 영수증을 각각 구분하여 보관합니다. 이 소비자가 새 성경 조사나 live 검사, 부재한 스크린샷 픽셀 검사를 수행한 것은 아닙니다.

현재 승인 MD SHA-256: 9e73a0b23fa4c20ae01f9a395e5f98d2d8ec7511f1140526de678bdfc05ff8eb. portable MD SHA-256: 40730b5aaaa3de64421c12ff8f7b52c4b372496016e2a8901bd8d2cc06e472ba. 이미지 경로만 바뀌었으며 저장소 article.md는 frontmatter·중복 H1 제거·assets 경로 변환만 더합니다. 다섯째 절은 승인본대로 사사기 8:22~28을 가리킵니다. 이미지·권리 원본 manifest와 EXIF 방향은 이전 패키지에 그대로 보존합니다.

831→485 본문 단어 및 약 41.6% 감소는 생산자 고정 집계에 따른 전달 수치입니다. 해당 집계 구현은 이 delta에 없으므로 소비자 재계산 PASS로 표시하지 않습니다.
