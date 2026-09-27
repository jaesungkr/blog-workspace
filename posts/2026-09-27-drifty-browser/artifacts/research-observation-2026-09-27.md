# Drifty 공개 표면 교차 확인 로그

- 실행 주체: Codex
- 확인 시점: 2026-09-27, Asia/Seoul
- 환경: Codex 인앱 브라우저, 공개 웹 페이지, 로그인하지 않은 상태
- 목적: Windows판의 실제 공개 여부와 홈페이지·문서·릴리스 안내의 일치 여부를 확인합니다.

## 한국어 홈페이지

- URL: `https://drifty.so/ko/`
- 관찰: 첫 화면은 `스스로 기록하는 시간 관리`라고 제품을 설명했습니다.
- 관찰: 자동 기록, AI 분류, 개인정보 보호를 핵심 장점으로 제시했습니다.
- 관찰: 기능 영역은 앱·사이트·세션을 3분 단위로 기록한다고 적었습니다.
- 관찰: FAQ를 펼치자 `Windows에서도 사용할 수 있습니다. Windows용 다운로드. iOS 앱은 없습니다.`라는 문구와 `https://drifty.so/ko/download/?platform=windows` 링크가 나타났습니다.
- 관찰: AI 선택 표는 Drifty Cloud 월 7달러, OpenRouter 사용량 추정 월 4-6달러, 로컬 AI 무료와 Mac에서 약 5-7GB RAM 사용을 표시했습니다.

## Windows 파라미터 다운로드 경로

- URL: `https://drifty.so/ko/download/?platform=windows`
- 관찰: 내비게이션 링크 설명은 `Windows용 다운로드`였지만, 페이지 제목과 본문은 `Mac용 drifty 다운로드`, Apple Silicon DMG, macOS 13 이상을 표시했습니다.
- 해석: Windows 미출시로 판정하지 않았습니다. 같은 날 공식 릴리스 저장소에 Windows 설치 파일과 검증 내역이 존재하기 때문입니다. 현재 웹 라우팅 또는 본문 문구 편차로만 기록합니다.

## 공식 설치 문서

- URL: `https://docs.drifty.so/start-here/install/`
- 관찰: 서명·공증된 macOS 디스크 이미지, Applications 폴더, macOS 접근성 권한, 메뉴 막대를 기준으로 설치를 설명했습니다.
- 해석: Windows의 세부 설치와 권한 절차는 이 문서만으로 설명하지 않습니다.

## 공식 GitHub 릴리스

- URL: `https://github.com/edgethink00/drifty_releases/releases`
- 관찰: 2026-09-27에 `Drifty for Windows 1.11.22`와 `Drifty Windows Beta 0.0.8 (1.11.22)`가 공개됐습니다.
- 관찰: Windows 1.11.22는 Windows 10/11 x64용 `drifty_1.11.22_x64-setup.exe`를 명시했습니다.
- 관찰: 두 릴리스는 같은 서명 바이트와 SHA-256 `5CFD82F17299BC38D62B744A8CF520723E644CBAE0B602CF3417A719D238160E`를 사용한다고 밝혔습니다.
- 관찰: Windows 전용 태그의 GitHub `prerelease` 상태는 macOS `Latest`를 대체하지 않기 위한 것이며, `latest-windows.json`이 Windows 안정 업데이트 주소라고 설명했습니다.
- 관찰: 알려진 문제로 마지막 온보딩 단계의 첫 `Start tracking`이 `tracker_start failed`라고 표시될 수 있으나 실제 추적은 이미 실행 중일 수 있고, 다시 누르면 완료된다고 적었습니다.

## 사용자 제공 Instagram 피드

- URL: `https://www.instagram.com/p/DdtJZrqmpkS/?img_index=1`
- 게시 계정: `ai_freaks.kr`와 `drifty.kr` 공동 표기
- 확인 가능한 게시 시점 표기: 열람 당시 `2일`
- 핵심 문구: 컴퓨터 활동을 자동으로 기록하는 AI 타임 트래커, Mac 전용에서 Windows 베타로 확장, 3분 단위 타임라인, 같은 YouTube도 강의와 쇼츠를 구분, 딴짓 시 탭을 닫는 고양이, Drifty Cloud 소개
- 댓글 관찰: `드디어 윈도우 오픈됐네요!!! 빨리 깔아야지!`라는 반응이 보였습니다.
- 사용 범위: 주제 발견과 현재 홍보 포인트 확인에만 사용합니다. 쿠폰 이벤트와 반응 수치는 본문에 쓰지 않습니다.

## 재현 경계

- 공개 페이지는 언제든 바뀔 수 있습니다.
- 앱을 다운로드하거나 실행하지 않았습니다.
- 실제 분류 정확도, 배터리 사용량, 설치 성공률, Mac·Windows 기능 동등성을 측정하지 않았습니다.
- Windows 공개 여부는 홍보 피드보다 공식 설치 파일과 릴리스 검증 내역을 우선해 판정했습니다.
