# 근거 지도: Drifty, 고양이 AI 시간 관리 앱

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Drifty는 타이머 없이 활성 앱·사이트·세션을 자동으로 기록하고 3분 단위 블록으로 보여 줍니다. | 공식 | 확인 | [한국어 홈페이지](https://drifty.so/ko/), [What drifty is](https://docs.drifty.so/start-here/what-drifty-is/) | 실제 기록 누락률과 운영체제별 차이는 직접 측정하지 않았습니다. |
| C02 | 기록된 활동은 업무 프로필과 최근 맥락을 바탕으로 Focus·Neutral·Drift로 분류되며, 사용자가 잘못된 분류를 고칠 수 있습니다. | 벤더 주장 | 확인 | [한국어 홈페이지](https://drifty.so/ko/), [How drifty reads work](https://docs.drifty.so/ai-and-classification/how-it-reads-work/) | 분류 정확도 수치가 공개된 독립 벤치마크는 확인하지 못했습니다. 홈페이지도 예시 결과가 맥락에 따라 달라진다고 밝힙니다. |
| C03 | Drifty는 화면을 녹화하거나 스크린샷을 저장하지 않습니다. Mac 공식 문서는 원시 활동 기록을 로컬 데이터베이스에 보관한다고 설명합니다. | 공식 | 확인 | [Privacy & Data Boundaries](https://docs.drifty.so/ai-and-classification/privacy-boundary/), [FAQ](https://docs.drifty.so/troubleshooting/faq/) | Cloud·BYOK 분류를 선택하면 필요한 일부 활동 정보가 선택한 공급자에게 전송됩니다. 선택적 기기 동기화는 별도 예외이며, Windows의 세부 저장 경로와 모든 개인정보 설정은 같은 수준으로 문서화돼 있지 않습니다. |
| C04 | AI 분류는 Drifty Cloud, OpenRouter BYOK, 로컬 AI 또는 사용자 지정 엔드포인트 가운데 고를 수 있습니다. Windows Beta 0.0.6 릴리스도 로컬 모델 설치와 두 차례 로컬 분류 검증을 기록합니다. | 공식 | 확인 | [Choose your AI](https://docs.drifty.so/ai-and-classification/choose-your-ai/), [한국어 홈페이지](https://drifty.so/ko/), [Windows Beta 0.0.6](https://github.com/edgethink00/drifty_releases/releases/tag/1.11.20-winbeta.6) | 홈페이지의 로컬 AI 메모리 안내는 Mac 기준입니다. Windows 세부 설치 조건과 모든 기능 동등성은 문서가 충분하지 않습니다. |
| C05 | Mac 공식 문서의 무료 경로는 자동 기록·로컬 타임라인·로컬 또는 BYOK 분류를 포함하고, Pro는 월 7달러 또는 연 60달러입니다. | 공식 | 확인 | [Account & Billing](https://docs.drifty.so/account/billing/), [한국어 홈페이지](https://drifty.so/ko/) | 가격과 체험 조건은 바뀔 수 있으며 2026-09-27 확인값입니다. OpenRouter 월 4-6달러는 벤더가 제시한 사용량 추정치입니다. Windows의 계정 없는 사용 범위는 설치한 버전에서 따로 확인해야 합니다. |
| C06 | 2026-09-27 공식 저장소에는 Windows 10/11 x64용 Drifty 1.11.22 서명 설치 프로그램이 공개돼 있습니다. | 공식 | 확인 | [Drifty for Windows 1.11.22](https://github.com/edgethink00/drifty_releases/releases/tag/1.11.22-win) 다운로드·검증 절 | GitHub의 Windows 전용 태그는 macOS Latest를 대체하지 않도록 `prerelease` 상태를 유지합니다. |
| C07 | 같은 서명 바이트가 `Windows Beta 0.0.8`과 `Windows 1.11.22`로 함께 배포됩니다. | 공식 | 확인 | [공식 릴리스 목록](https://github.com/edgethink00/drifty_releases/releases), Beta 0.0.8와 Windows 1.11.22의 동일 SHA-256 `5CFD...160E` | 공개 피드는 Windows를 베타로 소개하고, 저장소는 안정 업데이트 주소도 함께 운영합니다. 독자에게 이 표기 차이를 설명해야 합니다. |
| C08 | Windows 1.11.22에는 첫 설정의 `Start tracking`이 한 번 실패로 표시될 수 있으나 실제 추적은 이미 시작된 알려진 문제가 있습니다. | 공식 | 확인 | [Drifty for Windows 1.11.22](https://github.com/edgethink00/drifty_releases/releases), Notes의 known issue | 이후 버전에서 수정될 수 있는 시점 민감 정보입니다. |
| C09 | 2026-09-27 한국어 홈페이지는 Windows 사용 가능과 다운로드 링크를 표시하지만, 공개 설치 문서와 다운로드 페이지에는 Mac 중심 문구가 남아 있습니다. | Codex 실행 | 확인 | `artifacts/research-observation-2026-09-27.md`; [한국어 홈페이지](https://drifty.so/ko/), [Install](https://docs.drifty.so/start-here/install/), [Windows 파라미터 다운로드](https://drifty.so/ko/download/?platform=windows) | 웹 라우팅과 문구는 언제든 바뀔 수 있습니다. 한 번의 브라우저 관찰을 장기 상태로 일반화하지 않습니다. |
| C10 | Drifty의 자동 종료와 데스크톱 펫은 선택 기능이며, 분류가 틀리면 `Not a drift`로 정정할 수 있습니다. Windows Beta 0.0.6은 Firefox 자동 종료와 고양이 동작을 서명 빌드에서 검증했습니다. | 공식 | 확인 | [한국어 홈페이지](https://drifty.so/ko/), [Windows Beta 0.0.6](https://github.com/edgethink00/drifty_releases/releases/tag/1.11.20-winbeta.6), [Changelog](https://drifty.so/changelog/) | 자동 종료는 Beta 선택 항목이며 브라우저·운영체제별 안전 조건이 다릅니다. Mac과 Windows의 화면·기능 동등성을 보장하지 않습니다. |
| C11 | Drifty는 업무 흐름 회고를 돕지만 청구용 타임시트나 자동 프로젝트 회계를 대신하지 않습니다. | 공식 범위 + 편집 판단 | 확인 | [Developers use case](https://drifty.so/use-cases/developers/)의 `What it does not replace` | 제품이 모든 타임시트 용도를 금지한다는 뜻이 아니라, 공식 설명이 보장하는 범위를 좁힌 판단입니다. |
| C12 | 공개 Instagram 피드는 Drifty를 자동 AI 타임 트래커로 소개하고 Windows 베타와 데스크톱 고양이를 강조합니다. | 사용자 제공 공개 자료 | 확인 | [사용자 제공 Instagram 피드](https://www.instagram.com/p/DdtJZrqmpkS/?img_index=1), 2026-09-27 브라우저 열람 | 홍보 피드이며 독립 검증 자료로 사용하지 않습니다. 쿠폰 이벤트 문구는 본문 범위에서 제외합니다. |

## 직접 검증 설계

- 질문: Windows판이 실제로 공개됐는지, 공식 홈페이지·설치 문서·릴리스 저장소가 같은 상태를 가리키는지 확인합니다.
- 실행 주체: Codex
- 환경과 확인 시점: 2026-09-27, Codex 인앱 브라우저와 공개 웹 검색
- 입력: 한국어 홈페이지, `?platform=windows` 다운로드 경로, 설치 문서, GitHub 공식 릴리스, 사용자 제공 Instagram 피드
- 전처리 또는 표현: 각 화면에서 플랫폼 문구, 링크 대상, 버전, 운영체제, 설치 파일 이름, known issue를 추출했습니다.
- 비교·판정 규칙: Windows 10/11 x64 설치 파일과 버전·서명 해시가 공식 릴리스에 있으면 `실제 공개`, 문서가 Mac 설치만 설명하면 `문서 편차`로 기록합니다.
- 성공 기준: 적어도 하나의 공식 Windows 설치 릴리스와 현재 홈페이지 표기를 확인하고, 상충하는 안내를 숨기지 않습니다.
- 반복 횟수와 표본 크기: 동일 날짜의 공식 표면 5곳을 한 차례 교차 확인했습니다. 장기 사용 테스트는 하지 않았습니다.
- 보존할 원자료: `artifacts/research-observation-2026-09-27.md`

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | 한국어 홈페이지 FAQ | Windows에서도 사용할 수 있으며 Windows용 다운로드 링크를 표시했습니다. | `artifacts/research-observation-2026-09-27.md` | 현재 제품 안내의 플랫폼 선언입니다. |
| E02 | Windows 파라미터 다운로드 페이지 | URL과 내비게이션은 Windows를 가리키지만 본문은 Mac DMG와 Apple Silicon을 표시했습니다. | `artifacts/research-observation-2026-09-27.md` | 현재 웹 문구 또는 라우팅 편차입니다. Windows 미출시의 증거로 해석하지 않습니다. |
| E03 | 공식 GitHub 릴리스 | Windows 10/11 x64 1.11.22 설치 파일과 검증 내역, Beta 0.0.8의 동일 해시가 공개됐습니다. | `artifacts/research-observation-2026-09-27.md` | Windows 설치 파일이 실제로 공개됐다는 직접 근거입니다. |
| E04 | 설치 문서 | 설치 과정, 권한, 메뉴 막대 설명이 macOS를 기준으로 작성돼 있습니다. | `artifacts/research-observation-2026-09-27.md` | Windows 세부 사용법을 문서만으로 완전히 설명할 수 없습니다. |

## 실패와 반례

- 예상과 달랐던 결과: `?platform=windows`를 붙인 한국어 다운로드 페이지가 Windows 설치 프로그램 대신 Mac DMG 문구를 표시했습니다.
- 알려진 Windows 반례: 1.11.22의 마지막 온보딩 단계에서 첫 `Start tracking`이 실패로 보일 수 있습니다.
- 일반화하면 안 되는 범위: 홈페이지의 예시 분류와 공급자 설명은 벤더 자료입니다. 실제 정확도, 배터리 사용량, 성능, 모든 Mac·Windows 기능 동등성을 검증하지 않았습니다.

## 미해결 항목

- 본문에 사용할 핵심 주장은 플랫폼 범위와 정확한 Windows 릴리스 태그까지 매핑했습니다.
- Windows 다운로드 페이지 문구는 배포 후 바뀔 수 있으므로 발행 직전 링크를 다시 확인할 가치가 있습니다.

## 출처 메모

- 2026-09-27 사용자 수정: 제목을 `Drifty, 고양이 AI 시간 관리 앱`으로 지정하고 홈페이지 대시보드 스크린샷을 제공했습니다. `assets/drifty-dashboard.png`는 3378×1902 원본이며 화면 속 시간·비중은 공식 예시 데이터입니다. 사용자의 실제 앱 사용 결과로 해석하지 않습니다. 이 화면은 C01·C02·C10을 시각적으로 설명하며 분류 정확도나 고양이 동작 자체의 실험 증거는 아닙니다.
- 같은 날 재확인한 홈페이지·분류 안내·요금 문서·Windows 1.11.22 릴리스에서 기존 본문에 쓰인 핵심 수치와 조건을 유지했습니다. 배포용 본문에서는 동일 해시와 채널 운영의 세부 사항을 줄였으며 원자료는 C06·C07에 보존합니다.

- 공개 피드는 주제 발견과 제품의 현재 홍보 포인트 확인에만 사용합니다.
- Windows 공개 여부는 피드 댓글이 아니라 공식 릴리스 파일과 검증 내역으로 판정합니다.
- 가격은 공식 문서의 2026-09-27 값이며 독립 가격 비교가 아닙니다.
- 분류 정확도는 수치로 주장하지 않습니다.
