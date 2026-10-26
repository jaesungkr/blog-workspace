# AI 영상 제작 툴 비교: 선두 모델과 용도별 추천 사이트

확인일: 2026-10-26 (Asia/Seoul). 조사 실행자: Codex. 공개 웹 자료를 읽고 기능·이용 경로·평가 조건을 대조했다. 영상 생성·계정별 기능·한국어 대사·대기 시간·상업적 권리 자체에 관한 실사용 시험은 하지 않았다. 기능 소개는 제공사 주장, 선두권은 아래 평가별 관측, 용도별 권고는 편집 판단이다.

## 주장과 출처

| ID | 확인한 주장 | 출처와 근거 | 한계/원고 처리 |
| --- | --- | --- | --- |
| C01 | Kling 4.0은 3~30초, 720p/1080p/4K, 여러 참조·영상 수정 기능을 지원한다. | https://kling.ai/quickstart/kling-4-model-user-guide 공식 가이드, Input/Parameter 표와 편집 예시. | 원본 유지 성능·성공률 미측정. 자료 역할 미지정 시 예측 가능성 저하라는 안내 포함. |
| C02 | Wan 3.0은 최대 30초, 문서·링크 등 다양한 입력, 영상 수정 기능을 제공한다. | https://www.alibabacloud.com/blog/wan3-0-30-second-ai-video-generation-from-any-input_603452 공식 기능·FAQ. | 웹 플랫폼별 입력 기능 차이. 오디오 질감/문자 정확도 개선 과제는 제공사 스스로 명시. |
| C03 | Wan 공식 API 1080p 요율은 초당 $0.20이다. | 위 Alibaba 페이지의 API Pricing 표. | 특정 API 안내의 요율. 프로모션·다른 지역·중계 플랫폼·구독 크레딧에 확대 금지. |
| C04 | Seedance 2.5는 최대 30초의 영상·오디오 공동 생성과 장면 연결·참조·수정을 강조한다. | https://seed.bytedance.com/en/seedance2_5 및 https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5 (2026-07-31). | 공식 시연을 성공률로 해석하지 않는다. 공개 페이지의 Try on Dreamina 링크와 models 페이지로 공식 경로 확인. |
| C05 | AA 오디오 포함 T2V v2.1에서 Wan3.0 표시1위, UtopaiX2위, HeyGenVideo1 3위, MiniMaxH3 4위, Seedance2.5 5위. | https://artificialanalysis.ai/video/leaderboard/text-to-video 의 Overall/With Audio. 맹검 쌍별 선호 평가. | 상위 신뢰구간 겹침. API 표는 기본 조건 분당 요금. UI·한국어·수정 성공률을 측정하지 않음. |
| C06 | Arena T2V에서 Gemini Omni 1.1 Flash 표시1위. | https://arena.ai/leaderboard/video/text-to-video , 페이지 자체 날짜 2026-09-21. | 확인일과 갱신일 분리. 다른 평가와 Elo 절대값 비교 금지. Kling4 미등재, 이전 버전 점수 대체 금지. |
| C07 | Omni는 대화형 영상 수정, 이미지·영상·소리 참조 및 Gemini/Flow 경로를 제공한다. | https://deepmind.google/models/gemini-omni/ 공식 Capabilities와 Try 항목. | Omni 계열과 Veo, Omni1.1과 기존 Omni를 구분. |
| C08 | Omni1.1 Flash는 장면 연장과 시작·끝 프레임 지정을 지원한다. | https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/ , 2026-08-27. | 최대 출력 길이/4K 숫자는 본문에서 생략. |
| C09 | Veo3.1은 오디오를 포함한 짧은 영상 생성 모델이다. | https://ai.google.dev/gemini-api/docs/veo 공식 문서. | 특정 API의 8초/해상도 조건을 구독 웹 UI 전체 조건으로 확대하지 않는다. |
| C10 | Higgsfield는 다수 모델을 제공하며 Kling4도 안내한다. | https://higgsfield.ai/kling-4-0-intro , https://github.com/higgsfield-ai/skills/blob/main/higgsfield-generate/references/model-catalog.md , https://higgsfield.ai/pricing | 동일 공간에서 비교할 출발점이라는 편집 권고. 가장 쉬움/저렴함/최고 품질 주장 없음. 요금 페이지는 동적이며 특정 월정액 확정 금지. |
| C11 | Runway Gen4.5는 복잡한 지시·카메라 연출을 강조하며 인과관계·물체 지속성·시간 순서 한계가 있다. | https://runway.com/research/introducing-runway-gen-4.5 의 Capabilities/Limitations. | 출시 당시 1위 문구는 현재 순위로 전재하지 않는다. Google Omni1.1 글은 Runway의 Omni 제공도 설명한다. |
| C12 | Luma Ray 계열은 원본 수정·참조·HDR을 지원하되 모드별 범위가 다르다. | https://lumalabs.ai/learning-hub/ray3-faqs , https://lumalabs.ai/learning-hub/luma-video-models-guide-ray3.14-veo-sora-kling-compared | 검색 결과로 공식 가이드 내용 확인. 본문 링크는 유지하되 최신 단일 버전으로 단정하지 않는다. |
| C13 | Firefly는 자체/파트너 모델을 제공하고 조건을 구분한다. | https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-non-adobe-models.html , https://helpx.adobe.com/creative-cloud/apps/generative-ai/non-adobe-models-in-adobe-products.html | 모든 파트너 출력을 법적으로 안전하다고 보장하지 않는다. 권리 확인이라는 구체적 경계만 둔다. |
| C14 | Pika는 외부 모델과 교체·연장·소리 도구를 제공한다. | https://pika.art/ 의 현재 Video Models/Video Apps/Audio 항목. | 과거 밈 전용 소개로 제한하지 않는다. |
| C15 | MiniMax H3 공식 체험 경로는 Hailuo이다. | https://www.minimax.io/blog/minimax-h3 및 https://design.minimax.io/h3 | API 최대2K와 공개 가중치768p 조건이 달라 웹 UI에 수치 확대 금지. |
| C16 | HeyGen은 말하는 아바타와 영상 번역을 제공한다. | https://www.heygen.com/ 공식 Avatar/Video Translation 항목. | 언어 수·성능 보장·시장 점유율 전재 금지. 아바타와 일반 생성 모델의 영역을 구분한다. |
| C17 | Sora 웹·앱 종료일4/26, API종료일9/24. | https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation 및 https://developers.openai.com/api/docs/deprecations | 2026년. 과거 평가표 잔존과 현재 이용 가능성 구분. |
| C18 | 무제한도 적용 모델/대기열/동시 작업 조건이 있다. | https://higgsfield.ai/blog/new-unlimited-more-models | 현재 개별 계정 제한 수치는 확정하지 않음. 일반 결제 시 확인할 항목으로만 사용. |
| C19 | 자료 준비, 클립 생성, 최종 편집 과정을 설명하는 개념 삽화. | 기존 원고의 모델/서비스/편집 도구 구분과 C01·C02·C04. 아래 C19 범위 설명 참조. | 가상 제품의 예시이며 실제 생성 결과나 별도 서비스 세 개의 사용을 뜻하지 않음. |

## 원본 관측 보존

`artifacts/research/leaderboard-observation.json`은 웹 도구가 반환한 표를 선택적으로 전사한 관측 기록이다. 스크린샷이나 원본 HTML이라고 표기하지 않는다. 자동 갱신되는 페이지이므로 날짜·과제·선두·신뢰구간을 함께 기록한다.

사용자가 보낸 소셜 게시물은 in-app browser에서 캡션을 읽었다. 주장들은 독립 검증 없이 인용하지 않았다. ‘Wan이 4.5배 저렴’, ‘Seedance가 확실한 종합 우승’, ‘Kling4 UGC 대량 최적’은 비교 조건/직접 시험이 없으므로 제외했다. 해당 URL과 참고 사실은 공개 원고·HTML·참고 자료에 넣지 않는다.

## 고유한 판단 체계와 계산

독립 평가의 품질 선두와 사이트 선택을 분리한다. 새 장면/원본 수정/여러 자료/이어지는 장면/말하는 아바타로 독자 상황을 나누고 공식 기능에 연결한다. 이는 편집한 선택 기준이며 측정 순위가 아니다.

`artifacts/research/cost-example.json`: Codex가 공식 $0.20/s × 5s = $1.00, 5회 × $1.00 / 채택1개 = $5.00를 계산했다. 성공률20%를 측정한 것이 아니다. 가격표 전체나 4.5배 비교를 만들지 않는다.

## 미해결 사항

공개 원고에 사용할 미해결 사실은 없다. 한국 계정별 최신 제공 여부·로그인 후 차감량·한국어 성능·생성 대기 시간은 이 글의 검증 범위 밖이며 확정하지 않았다. 게시 전 실제 계정에서 선택 모델·조건을 다시 볼 필요가 있다.

## C19: 추가 설명 이미지의 범위

자료를 준비하고, 모델로 짧은 클립을 생성한 뒤, 선택한 클립과 자막·소리를 편집해 완성하는 과정을 설명한다. 기존 원고의 모델/서비스/편집 도구 구분과 C01·C02·C04의 자료 입력 및 생성 기능을 시각화한 것이다. 모든 작업이 반드시 세 개의 별도 서비스에서 이루어진다는 뜻은 아니다. 동일한 가상 제품의 사진·동작 프레임·편집 타임라인은 개념 삽화이며 실제 생성 성공 사례가 아니다. 공개 라벨은 자료 준비 / 클립 생성 / 최종 편집이다.
