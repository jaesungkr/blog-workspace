# 독립 최종 페이지 검수

- 검수자: /root/source_review
- 사용자 기준일: 2026-10-27 (Asia/Seoul). 캡처 도구의 원시 checked_at은 도구가 반환한 UTC 값을 그대로 보존했다.
- 판정: pass. 원고 편집 검수를 다시 열지 않았으며 승인 원고·이미지·CSS·미디어는 수정하지 않았다.
- 대상: final-rendered 및 final-dark-rendered의 canonical remote-media 후보. 티스토리 편집기는 조작하지 않았다.

## 실행과 캡처

capture_rich_qa_v2.py를 final-light와 final-dark에서 각각 새 Chrome155 세션으로 실행했다. 두 테마 모두1280×900 및360×800이 통과했다. 세션 식별자는 light6164fbeb-12a1-46f3-9d50-5ce70ae5a674, darka9b8fb24-59dd-42ed-85a0-bb1fa7e11865이다.

정규 증거는 각 테마의 desktop-1280.png/mobile-360.png와 browser-capture.json에 있다. 정규 캡처가 첫 뷰포트만 저장하므로, 같은 canonical HTML을 추가 독립 headless 세션에서 열어 inspection/에 네 전체 페이지 캡처를 저장하고 끝까지 확인했다. 화면 높이는 데스크톱7994px, 모바일10210px이었다. 원본 픽셀 크기·관측 내용은 inspection/observations.json에 있다.

전체에서 구조·소제목 줄바꿈·섹션 순서·표·그림·참고자료가 누락되지 않음을 확인했다. 모바일에서 표의 오른쪽 조건 열이 정규 첫 화면과 전체 축소 캡처에 보이지 않는 상태이므로, 서비스 표를 오른쪽 끝으로 민 focused screenshot을 두 테마에서 보존했다. 두 그림의 실제 painted pixels와 라벨 확인, 참고자료 목록의 마커·간격 확인을 위한 추가 focused screenshot도 inspection/에 있다. 반복되는 모든 표나 문단에 개별 증거를 만들지는 않았다.

## 자동 관측 대조

-1280px와360px 모두 clientWidth와scrollWidth가 같아 페이지 가로 넘침이 없다.
-모든 후보의 H1은1개, 목차 링크는6개이고 target이 유일하다.
-원격 이미지2개가 각 테마·너비에서 로드됐다. hero1672×941, workflow1448×1086이다. 전체와 focused view에 실제 그림이 그려져 있어 naturalWidth만으로 통과하지 않았다.
-데스크톱의 표 폭은760px이며 가로 스크롤이 필요 없다. 모바일 wrapper는320px, 표 scrollWidth는620px이다. 오른쪽 끝에서도 마지막 열이 읽히고 본문은 움직이지 않는다.
-참고자료는7개 disc 마커, 목차는6개 decimal 마커로 렌더된다. 모바일/데스크톱 모두 마커와 항목 간격이 보인다.
-fragment는 H1 0개, 미해결 media directive0개, 로컬 src/href0개이고 네이티브 이미지 블록2개를 담고 있다.

## 시각 판단

도입과 추천 문장은 hero 앞에 있고, hero 뒤의 목차는6개 항목으로 유지된다.360px에서 긴 모델 비교 소제목과 목차 항목이 줄바꿈되지만 잘리거나 겹치지 않는다. 일반 본문과 그림에는 가로 스크롤이 없다.

그림의 실제 표시 폭은 데스크톱916px, 모바일320px이다. hero의 모델명·세 조형물·캡션이 식별되고, workflow의 자료 준비/클립 생성/최종 편집 라벨·제품·화살표가 모바일에서도 읽힌다. 각 캡션은 해당 그림 바로 아래에 붙어 있으며 다음 본문과 구분된다.

dark에서는 본문과 표의 글자, 제목, 캡션, 링크가 충분히 구분된다. 실제 계산된 링크 색은 light rgb(0,102,204), dark rgb(102,179,255)로 어두운 배경에서 밝게 바뀐다. 원본 인라인 링크 속성은 남아 있고 dark용 scoped CSS가 가독성을 보완한다. 그림 filter는 none이며 밝은 원본 그림과 중립 주변을 유지한다. 원본 픽셀을 반전하거나 재색칠하지 않았다.

목록·표·이미지·문단 배치에서 미해결 페이지 결함을 발견하지 못했다. final-measurements.json에서는 사람 판단인 readable_media/status, fragment status, dark_theme 판단만 채웠다. 캡처 도구가 만든 자동 측정과 해시는 변경하지 않았다.

이 판단은 독립 canonical 후보에 대한 최종 페이지 기록이다. 실제 티스토리 native attachment 변환과 hELLO 미리보기, 게시 후 live desktop/mobile 확인은 게시 담당자가 별도로 수행해야 한다.
