# 근거 지도: Unsloth Desktop이란? 코딩 없이 내 PC에서 AI를 학습하는 앱

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Unsloth Desktop Beta는 로컬 하드웨어에서 AI 모델을 실행·학습하는 무료 오픈소스 앱이며 Windows, macOS, Linux용 설치 파일이 제공된다. | 공식 | 확인 | `https://unsloth.ai/docs/desktop`, `https://unsloth.ai/download`, 2026-08-14 확인 | 베타의 지원 범위와 설치 파일은 바뀔 수 있음 |
| C02 | v0.1.701-beta 릴리스는 2026-08-11 19:24 UTC에 공개됐으며 Tauri 기반 네이티브 앱을 제공한다. | 공식 릴리스 | 확인 | `https://github.com/unslothai/unsloth/releases/tag/v0.1.701-beta`, GitHub API `published_at` | 한국 시간으로는 2026-08-12 새벽, 후속 버전 가능 |
| C03 | Unsloth는 Desktop, 브라우저 UI인 Studio, 코드 방식인 Core의 세 진입 방식을 안내한다. | 공식 | 확인 | 공식 GitHub README의 Install 절 | 기능·설치 경로의 세부 차이는 업데이트될 수 있음 |
| C04 | Desktop 릴리스는 CPU에서 Chat과 Data Recipes를 지원하고, NVIDIA·AMD·Intel·Mac을 포함한 하드웨어 범주를 안내하되 학습·추론 선택지는 모델과 백엔드마다 다르다고 제한한다. | 공식 | 확인 | GitHub v0.1.701-beta 릴리스의 Hardware + platform support, Desktop FAQ | GPU 세대·드라이버별 상세 호환표가 아니며 독립 검증도 아님 |
| C05 | Desktop의 가장 짧은 시작 경로는 설치 후 상단 `Select model` 또는 `Model hub`에서 기기에 맞는 모델과 양자화를 골라 내려받는 것이다. | 공식·화면 관찰 | 확인 | `https://unsloth.ai/docs/desktop`, 공식 UI 이미지 | 모델별 실제 메모리 사용량은 측정하지 않음 |
| C06 | 공식 데모의 Train 설정 화면은 학습할 기본 모델, 학습 방식, 데이터셋, 컨텍스트·스텝·학습률과 실행 미리보기를 한 화면에 둔다. 채팅 확인에 쓴 GGUF와 Train에서 선택한 모델이 같다고 볼 근거는 없다. | 공식 화면 관찰 | 확인 | 공식 Desktop 문서의 대표 화면과 `Train with no code` 데모 프레임 비교, 2026-08-14 | 데모 UI이며 현재 설치본과 일부 배치가 달라질 수 있음. 화면 비교는 두 모델의 재사용 가능성을 판단하지 않음 |
| C07 | QLoRA는 4비트로 줄여 불러온 기본 모델 위에 작은 LoRA 어댑터를 학습하는 방식으로, 전체 가중치 학습보다 메모리 부담을 낮추는 선택지다. | 기술 설명·공식 가이드 | 확인 | Unsloth fine-tuning guide와 화면의 `QLoRA 4-bit` 표기 | 모델·데이터에 따른 품질과 실제 VRAM 절감률은 별도 측정 필요 |
| C08 | 데이터 품질과 형식이 학습 결과를 크게 좌우하며, 목적·출력 형식·데이터 출처를 먼저 정해야 한다. | 공식 가이드 | 확인 | `https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/datasets-guide` | 특정 데이터셋의 품질은 이 글에서 평가하지 않음 |
| C09 | 공식 데모의 Current Run 화면은 Dataset과 Model weights 99%, `Training in progress`, `waiting for first step (0)`을 동시에 보여 준다. 다운로드 진행률이나 제목만으로 첫 스텝 완료를 판단할 수 없고 스텝 카운터가 0을 벗어나는지 확인해야 한다. | Codex 공식 화면 관찰 | 확인 | 공식 `trainingrun_LLM-unsloth.gif`의 진행 프레임을 2026-08-14 관찰 | 한 데모의 상태 해석이며 대기 원인 전체를 진단하지 않음 |
| C10 | Desktop은 LLM 외에도 이미지·영상 확산, 오디오, 임베딩 모델과 GGUF·MLX를 다룬다고 안내한다. | 벤더 주장 | 확인 | Desktop 공식 소개와 v0.1.701-beta 릴리스 | 모든 조합의 실행·학습을 독립 검증하지 않음 |
| C11 | 공식 FAQ는 앱이 오프라인 실행을 지원하고 텔레메트리를 수집하지 않는다고 밝힌다. | 벤더 주장 | 확인 | `https://unsloth.ai/docs/desktop` FAQ | 코드·네트워크를 독립 감사하지 않음 |
| C12 | 네 공식 화면을 `앱의 정체 -> 모델 선택 -> 학습 설정 -> 시작 확인` 순서로 다시 읽으면 비개발자도 제품의 역할과 첫 행동을 연결할 수 있다. | Codex 편집 판단 | 확인 | 공식 이미지 4장 비교와 reader-friction map | 특정 설치 환경의 성공률이나 학습 품질 순위는 다루지 않음 |

## 공개 자료 검증 설계

- 질문: 로컬 AI와 파인튜닝을 모르는 비개발자가 공식 설명과 화면만으로 Unsloth Desktop의 역할, 가장 쉬운 시작, 학습 준비와 진행 상태를 이해할 수 있는가?
- 실행 주체: Codex
- 환경과 확인 시점: macOS, Codex 인앱 브라우저와 공식 Markdown·GitHub API, 2026-08-14
- 입력: Desktop 공식 소개, 공식 다운로드 페이지, GitHub v0.1.701-beta 릴리스, 공식 README, 파인튜닝·데이터셋 가이드, 공식 UI 이미지와 학습 데모 GIF
- 전처리 또는 표현: 공식 원본 이미지를 보존하고, GIF는 화면에 표시된 특정 시점의 정지 프레임을 캡처해 상태 문구를 확인
- 비교·판정 규칙: 제품 기능은 공식 주장으로, UI의 글자와 상태는 Codex 화면 관찰로 분리. 실행하지 않은 설치·학습 결과는 주장하지 않음
- 성공 기준: 네 화면이 각각 앱의 정체, 모델 선택, 학습 설정, 진행 상태라는 서로 다른 질문에 답하고 본문의 다음 행동과 직접 연결됨
- 반복 횟수와 표본 크기: 공식 페이지 2개, GitHub 릴리스 1개, README 1개, 공식 가이드 2개, 공식 이미지 4개
- 보존할 원자료: `artifacts/media-candidates/`, 최종 공개 파일은 `assets/`

## 관찰 결과

| 관찰 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| O01 | Desktop 대표 화면 | 왼쪽에 Model hub·Projects·Images·Train, 상단에 선택된 GGUF와 양자화가 표시됨 | `artifacts/media-candidates/hero-official.png` | 제품 전체 정보 구조 |
| O02 | Select model 화면 | Recommended·On Device와 모델 크기를 같은 드롭다운에서 확인 가능 | `artifacts/media-candidates/permissions-official.png` | 첫 모델 진입점 |
| O03 | Train 설정 첫 화면 | Model·Method·Dataset·Advanced와 Run preview가 한 화면에 표시됨 | `artifacts/media-candidates/training-first-frame.png` | 학습 전 선택과 미리보기 |
| O04 | Current Run 진행 화면 | Dataset·Model weights 99%, `Training in progress`, `waiting for first step (0)`이 동시에 표시됨 | `artifacts/media-candidates/training-progress-official-frame.jpg` | 다운로드 진행률·상태 제목과 실제 스텝 카운터를 구분하는 단서 |

## 실패와 반례

- 실패한 입력: `https://unsloth.ai/docs/desktop`은 일반 웹 추출기에서 오류가 났지만, 인앱 브라우저의 공개 DOM과 공식 `.md` 페이지로 원문을 확인했습니다.
- 예상과 달랐던 결과: 제품 이름은 Desktop이지만, 공식 자료에는 기존 Studio와 Core 설치 경로도 함께 남아 있어 세 방식을 구분하지 않으면 설치 명령과 네이티브 앱을 혼동하기 쉽습니다.
- 일반화하면 안 되는 범위: 앱 설치 성공률, 특정 GPU의 속도·VRAM, 파인튜닝 품질, 장기 안정성, 실제 개인정보 보호 수준은 이 글에서 독립 검증하지 않았습니다.

## 미해결 항목

- 없음. 직접 실행이 필요한 성능·호환성 주장은 본문 약속에서 제외하고 한계로 명시합니다.

## 출처 메모

- `https://unsloth.ai/docs/desktop`: 제품 정체, 기능, 시작 경로, 공식 UI, FAQ.
- `https://unsloth.ai/download`: 운영체제별 현재 다운로드 링크.
- `https://github.com/unslothai/unsloth/releases/tag/v0.1.701-beta`: 출시 시각, 설치 파일, 릴리스 기능과 수정 사항.
- `https://github.com/unslothai/unsloth`: Desktop·Studio·Core 구분과 하드웨어별 공식 지원 범위.
- `https://unsloth.ai/docs/get-started/fine-tuning-llms-guide`: 파인튜닝과 학습 방식의 공식 입문 설명.
- `https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/datasets-guide`: 데이터 목적·형식·출처와 품질 경계.
