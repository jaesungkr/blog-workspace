---
title: "Drifty, 고양이 AI 시간 관리 앱"
slug: drifty-browser
date: 2026-09-27
category: "Log"
subcategory: "개발 · 디지털"
status: ready
format: rich-post-v2
tags: [Drifty, 드리프티, AI 시간 관리, 자동 시간 추적, Windows 앱]
summary: "데스크톱 고양이가 집중 복귀를 돕는 Drifty를 소개합니다. AI가 일과 딴짓을 구분하는 방식, 자동 시간 기록, 무료·Cloud 선택과 Windows 지원 상태를 정리합니다."
hero_image: assets/drifty-hero.png
published_url: ""
sources:
  - https://drifty.so/ko/
  - https://docs.drifty.so/start-here/what-drifty-is/
  - https://docs.drifty.so/ai-and-classification/how-it-reads-work/
  - https://docs.drifty.so/ai-and-classification/privacy-boundary/
  - https://docs.drifty.so/account/billing/
  - https://github.com/edgethink00/drifty_releases/releases/tag/1.11.22-win
  - https://github.com/edgethink00/drifty_releases/releases/tag/1.11.20-winbeta.6
  - https://www.instagram.com/p/DdtJZrqmpkS/?img_index=1
---

안녕하세요. dev.log입니다.

자료를 찾으려고 연 YouTube에서 어느새 쇼츠를 넘기고 있을 때가 있습니다. 그때 화면 위의 고양이가 다가와 보던 탭을 닫고, 하던 일로 돌아가도록 돕는 앱이 있습니다.

**Drifty는 AI로 일과 딴짓을 구분하고, 데스크톱 고양이가 집중 복귀를 돕는 시간 관리 앱입니다.** 타이머를 켜지 않아도 사용한 앱과 사이트를 기록합니다. 고양이와 자동 종료는 선택 기능이므로, 처음에는 기록을 보면서 AI가 자신의 업무를 제대로 구분하는지 확인해 볼 수 있습니다.

{{media:drifty-lead}}

### 딴짓하는 탭을 닫아 주는 고양이

[Drifty 공식 홈페이지](https://drifty.so/ko/)에서 눈에 띄는 기능은 데스크톱 위를 돌아다니는 고양이입니다. AI가 활동을 딴짓으로 판단하면 집중 복귀를 유도하고, 설정에 따라 고양이가 달려와 브라우저 탭을 닫는 동작을 보여 줍니다.

알림을 받았을 때는 하던 일로 돌아가거나, 잠깐 쉬거나, 딴짓이 아니라고 정정할 수 있습니다. 메뉴 막대의 Companion이 이 선택을 제공하며, 탭을 닫거나 앱을 종료하는 `Extreme Nudge`는 **사용자가 켜는 베타 기능**입니다. 고양이를 표시하거나 자동 종료를 켜지 않아도 시간 기록은 사용할 수 있습니다.

업무용 영상을 잘못 닫으면 오히려 방해가 됩니다. 자동 종료를 켜기 전에는 강의나 메신저 대화가 어떻게 분류되는지 먼저 확인하는 편이 좋습니다. [Windows Beta 0.0.6 릴리스](https://github.com/edgethink00/drifty_releases/releases/tag/1.11.20-winbeta.6)에도 Firefox 자동 종료와 고양이 동작 검증이 기록돼 있습니다. 다만 Mac과 Windows의 모든 화면과 기능이 같다는 뜻은 아닙니다.

### YouTube 강의도 딴짓으로 볼까?

Drifty는 앱 이름만으로 일과 딴짓을 나누지 않고, 업무 프로필과 최근 활동을 함께 참고한다고 설명합니다. 같은 YouTube라도 업무에 필요한 강의인지, 관련 없는 영상을 보고 있는지 구분하려는 방식입니다.

[공식 분류 안내](https://docs.drifty.so/ai-and-classification/how-it-reads-work/)와 홈페이지의 예시를 보면, 개발자가 Slack에서 React 오류를 논의하고 GitHub에서 코드를 수정한 뒤 관련 YouTube 강의를 봅니다. Drifty는 앞선 작업과 연결된 이 강의를 집중 활동으로 분류합니다. 업무와 무관한 쇼츠를 보는 상황과 다르게 판단하는 것입니다.

자신이 하는 일은 업무 프로필인 `Memory.md`에 적고, 잘못 붙은 분류는 직접 고칠 수 있습니다. 정정한 내용은 이후 판단에 참고됩니다. 물론 이 예시가 분류 정확도를 보장하지는 않습니다. 같은 영상도 맡은 업무와 앞뒤 활동에 따라 다르게 분류될 수 있습니다.

### 하루의 기록을 한 화면에서 보기

Drifty는 활성 앱과 사이트, 창 정보와 머문 시간을 백그라운드에서 기록합니다. 홈페이지는 이를 3분 단위 블록으로 보여 준다고 안내합니다. 사용자가 작업마다 타이머를 켜거나 태그를 붙일 필요는 없습니다.

기록된 활동에는 집중(`Focus`), 중립(`Neutral`), 딴짓(`Drift`)이라는 분류가 붙습니다. 아래 공식 홈페이지의 예시 화면에서는 가운데 시간대별 활동을 보고, 오른쪽에서 분류별 비중을 확인할 수 있습니다. 아래쪽에는 자주 쓴 앱과 사이트가 정리됩니다.

{{media:drifty-dashboard}}

하루를 돌아볼 때는 총 사용 시간보다 딴짓으로 표시된 구간을 먼저 살펴보세요. 업무 중 잠깐 쉰 시간인지, 생각보다 오래 머문 사이트인지 구분하면 다음 날 바꿀 습관을 찾기 쉽습니다. 고객에게 청구할 정확한 시간이나 프로젝트별 원가가 필요하다면 전용 타임시트가 더 적합합니다. [개발자용 공식 안내](https://drifty.so/use-cases/developers/)도 Drifty의 용도를 업무 흐름 회고로 한정합니다.

### 무료로 시작할까, Cloud를 쓸까?

Mac에서는 계정 없이 자동 기록과 로컬 타임라인부터 사용할 수 있습니다. AI 분류까지 쓰려면 기기 안에서 모델을 실행하거나, 외부 AI 서비스를 연결하는 방식을 고릅니다. 로컬 모델을 준비할 수 있다면 무료 로컬 AI를, 모델 설정을 맡기고 싶다면 Drifty Cloud를 고려할 수 있습니다.

2026년 9월 27일 [공식 요금 안내](https://docs.drifty.so/account/billing/)와 홈페이지에 나온 선택지는 다음과 같습니다. BYOK는 자신이 발급받은 API 키로 외부 AI 서비스를 연결하는 방식입니다.

| 선택 | 비용 | 준비할 것과 특징 |
|---|---|---|
| 로컬 AI | 무료 | 기기 안에서 분류합니다. 로컬 모델이 필요하며, Mac 안내 기준으로 약 5-7GB RAM을 사용합니다. |
| OpenRouter BYOK | 공식 추정 월 4-6달러 | 자신의 API 키를 연결합니다. 선택한 모델과 사용량에 따라 실제 요금이 달라집니다. |
| Drifty Cloud | 월 7달러 또는 연 60달러 | Drifty가 관리하는 AI로 분류합니다. 별도의 모델 설치나 API 키 설정이 필요 없습니다. |

[공식 개인정보 문서](https://docs.drifty.so/ai-and-classification/privacy-boundary/)는 화면 녹화나 스크린샷을 저장하지 않으며, Mac의 원시 활동 기록을 로컬 데이터베이스에 보관한다고 설명합니다. Cloud나 BYOK를 선택하면 앱 이름, 사이트, 머문 시간 등 분류에 필요한 일부 정보가 선택한 AI 공급자에게 전송됩니다. 기기 밖으로 보내는 정보를 줄이고 싶다면 로컬 AI를 먼저 살펴볼 이유가 있습니다.

Windows 릴리스에도 로컬 모델 설치와 분류 검증이 기록돼 있습니다. 다만 계정 없는 사용 범위, 세부 저장 경로와 개인정보 설정은 Mac만큼 자세히 문서화돼 있지 않아 설치한 버전에서 확인해야 합니다.

### Windows에서도 설치 가능

[소개 피드](https://www.instagram.com/p/DdtJZrqmpkS/?img_index=1)에는 Windows 출시를 반기는 댓글도 있습니다. 2026년 9월 27일 확인한 [공식 Windows 릴리스](https://github.com/edgethink00/drifty_releases/releases/tag/1.11.22-win)에는 **Windows 10/11 x64용 1.11.22 설치 파일**이 공개돼 있습니다.

같은 설치 파일이 `Windows Beta 0.0.8`이라는 이름으로도 배포됩니다. 저장소의 `Pre-release` 표시는 Mac용 최신 릴리스를 유지하기 위한 운영 방식이며, Windows 업데이트 경로는 따로 있습니다.

설치할 기기에 따라 지원 상태를 확인하면 됩니다.

| 환경 | 2026-09-27 확인 상태 | 설치 전에 볼 점 |
|---|---|---|
| Apple Silicon Mac | macOS 13 이상 정식 배포 | 공식 다운로드와 설치 문서가 가장 자세합니다. |
| Intel Mac | 대기자 명단 | 현재 공개 설치 파일은 Apple Silicon용입니다. |
| Windows | Windows 10/11 x64용 1.11.22 공개 | 설치 문서와 일부 다운로드 문구는 아직 Mac 중심입니다. |
| iPhone·iPad | iOS 앱 없음 | 데스크톱 활동 기록을 위한 제품입니다. |

다운로드 안내에는 혼동할 부분이 남아 있습니다. 확인 당시 한국어 홈페이지의 Windows 링크를 열어도 본문에 Mac용 DMG 안내가 나타났습니다. 같은 화면을 만난다면 위 공식 릴리스에서 Windows용 설치 파일을 확인하세요.

1.11.22에서는 마지막 설정 단계의 `Start tracking`이 처음에 실패로 표시되는 알려진 문제도 있습니다. 실제 기록은 이미 시작됐을 수 있으며, 공식 노트는 버튼을 다시 누르면 설정이 끝난다고 안내합니다. 설치 시점에 더 새 버전이 있다면 해당 릴리스 노트를 먼저 확인하세요.

고양이가 탭을 닫는 모습이 궁금해 설치하더라도, 첫날에는 하루의 기록과 분류부터 살펴보세요. 자신의 업무를 잘 이해하는지 확인한 뒤 복귀 알림과 자동 종료를 차례로 켜 보면, 어느 정도의 개입이 집중에 도움이 되는지 판단하기 쉽습니다.
