# 편집기 입력 준비 원고 검토

- 검토자: review_thoughts_cadence
- 검토일: 2026-10-24
- 결과: pass (원고 source에 한정합니다.)
- article.md SHA256: `a544af5695368f1f40c802c2f6d4f852e0e9475dc5ccd0cab4dfa88400d6248d`
- 상태: reviewing입니다. 최종 게시 버튼은 사용자가 직접 누릅니다.

현재 article.md를 처음부터 끝까지 다시 읽고 brief.md, evidence.md의 최신 편집 요청, workflow-v2.json을 확인했습니다. 직전 원고인 history/before-editor-staging/article.md와의 차이도 대조했습니다.

본문의 설교 영상 링크는 제거되었고, 영상 URL은 frontmatter의 검증용 출처와 근거 기록에 남아 있습니다. 설교 요약의 마지막 문단에서 Thoughts로 넘어가는 구성에 불필요한 문장이 추가되지 않았습니다. 인용된 마태복음 본문과 절 번호는 보존된 성경 대조문과 일치합니다.

마지막 문장은 풀리지 않은 질문과 지금의 고민이 지나가는 과정이라는 원문의 기대를 함께 담습니다. 앞선 문단의 피로·고통·미해결 상태를 지우거나 새로운 해답·납득·실천을 만들지 않았습니다. 주관적 설교 평가, 음식과 식욕의 구별, 자연선택의 조건과 예시, 강아지 비유 및 사랑과 책임에 관한 가정도 이전에 검토한 범위를 유지합니다.

직전 원고와의 차이는 hero_image 지정, 도입 뒤의 대표 이미지 지시문, 독자에게 보이는 설교 영상 링크 삭제, 마지막 두 문장의 통합으로 확인했습니다. 대표 이미지 지시문은 {{media:sermon-hero}}이며 경로는 assets/sermon-hero-v1.png입니다. 이는 예정된 이미지의 참조와 배치만 확인한 것으로, 실제 이미지의 완성·품질·업로드나 렌더링을 승인한 것이 아닙니다.

brief와 workflow의 최신 지시는 티스토리 편집기에 입력하고 마지막 게시 클릭을 사용자에게 남긴다는 경계를 명시합니다. 이 원고 검토를 자동 게시 승인으로 사용하면 안 됩니다.

## 확인 결과

- `python3 scripts/blog.py check posts/2026-10-24-matthew-5-fight-against-lust`: 오류 0개, 경고 0개입니다.
- article.md의 Thoughts와 artifacts/thoughts-edited.md가 일치합니다.
- 성경 인용은 artifacts/scripture-matthew-5-27-30.md와 일치합니다.
- 원고 차이와 전체 독해에서 필수 수정 사항을 발견하지 못했습니다.

원고와 source-pass는 수정하지 않았습니다. 대표 이미지 검수, 미디어 연결, HTML 렌더링과 실제 편집기 미리보기 검수는 별도 단계로 남으며, 이번 source pass는 ready·최종 페이지·게시 승인을 대신하지 않습니다.
