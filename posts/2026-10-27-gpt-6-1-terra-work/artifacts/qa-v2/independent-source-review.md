# comparison-v2 독립 원고 검수

- 검수자: independent source reviewer /root/source_review
- 확인일: 2026-10-27 UTC
- 결과: **pass (수정 후 최종 재검수)**
- 이전 단독소개 pass는 이 비교 원고에 적용하지 않는다. 원고 수정과 Git·게시 작업은 하지 않았다.

## cold-read

새 article.md를 처음부터 읽고 첫 화면 및 제목/heading을 별도로 평가한 뒤 brief/evidence/audit를 읽었다. 앞서 읽은 article-validation, source-freeze-v2, editorial-voice-v2 및 standards의 기준을 적용했다.

원고만으로 이해한 질문은 “기존 Opus/Sol 업무를 저렴한 Terra로 옮길 가치가 있는가”다. 첫 화면은 Terra의 정체, 화면 반복 업무와 어려운 작업의 선택을 설명한다. 주 비교 대상 Opus의 선정 이유와 보조 모델 Sol/Astra의 역할이 첫 절에 있다. 공식 평가는 시각·도구 작업, AA는 종합 성적/비용, 후기는 속도와 만족도, 고정 토큰 계산은 재시도 비용을 설명한다. 직접 모델 시험이나 한국어 품질 비교로 읽히지 않는다. 실제 비교·교체 판단 구조를 충족한다.

제목과 heading만으로도 비교 대상→화면 작업→종합 평가→후기→가격→선택을 이해할 수 있다. 종합 지수는 해당 평가 묶음으로, 후기는 서로 다른 설정의 개인 경험으로 한정한다. 작업별 선택표는 공개 근거의 종합으로 적절하며 저자의 현재 모델·전환 의사는 발명하지 않았다.

## 최초 지적과 수정 확인

1. medium/max 설명이 결과표 뒤에 있었음 → 첫 공식 평가표 앞으로 이동 확인.
2. `모든 업무에서 같은 비율로 절약된다는 뜻은 아닙니다` → 해당 평가 과제·설정·토큰·단가의 결과라는 직접 범위 진술로 변경 확인.
3. fallback을 일반 Opus 기본 동작처럼 설명 → AA의 default fallback 측정 구성으로 한정하고 거절 뒤 다른 모델 재시도 조건 및 Anthropic 출처 추가 확인.
4. 가격 heading `같은 처리량이면 1/4` → `기본 API 단가는 Opus의 4분의 1`로 변경 확인. 장문 할증 예외와 충돌하지 않음.
5. 결론의 표 앞뒤 유지/분담 권고 반복 → 앞은 짧은 표 소개, 뒤는 누락·오입력 및 수정까지 총비용을 확인하는 조건으로 압축 확인. 이는 구체적 개인 작업에서 교체 여부를 바꾸는 검증이므로 막연한 재시험 권유가 아님.

최종 재검수에서 fallback·가중평균 설명이 AA 표 앞으로 이동했고, `전반적인 대체품이라고 평가하기는 어렵습니다` 반복 문장이 삭제된 것을 확인했다. audit의 heading strip과 표 기능도 현재 원고와 일치한다. 남은 필수 원고 교정 없음.

## 공식·독립·후기 직접 검증

web open/find만 사용했으며 브라우저/file:// 접근 및 우회 없음.

| 직접 연 자료 | 확인 결과 |
|---|---|
| [Terra 출시](https://openai.com/index/introducing-gpt-6-1-terra/) | L27~40의 시각·도구·글쓰기 용도 및 MMMU 근접, ALE medium/Astra 관계, max의 Opus 대비 과제비용, 과학평가 관계 일치. 공식 평가 귀속 유지. |
| [Opus overview](https://platform.claude.com/docs/en/models/opus-5-5/overview), [what's new](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5) | 장시간 코딩·지식 업무, $4/$20/$0.20 일치. what's-new L128은 거절 요청 fallback 설정을 설명. 수정한 조건과 일치. |
| [AA Terra](https://artificialanalysis.ai/models/gpt-6-1-terra), [AA Opus](https://artificialanalysis.ai/models/claude-opus-5-5) | max 48/$0.40 및 max default fallback 58/$5.98 확인. v4.3.2의 10개 평가와 비용 가중 평균도 확인. |
| [AA Sol](https://artificialanalysis.ai/models/gpt-6-1-sol), [AA Astra](https://artificialanalysis.ai/models/gpt-6-astra) | max 52/$0.72, 53/$3.26 일치. |
| [AA 출시 분석](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier) | 10월26일 글 L19~26. low/medium 종합 비용효율, Coding Agent Index v2.0 Terra48/Sol54, Terminal-Bench4.0 경쟁수준 일치. 종합48과 코딩48의 지수 구분 유지. |
| [속도 후기](https://www.reddit.com/r/ChatGPT/comments/1xg7rfk/its_my_impression_or_terra_61_is_fing_fast/) | 작성자 본문은 Sol 대비 Terra 속도 체감. 동일 입력·effort 통제 자료 없음. 원고의 개인 경험 요약 정확. |
| [제작 후기](https://www.reddit.com/r/codex/comments/1xgcjjb/gpt_61_terra_on_gpt_plus/) | 본문 L21~34의 Terra high→max, Sol/Opus medium, 픽셀 프로젝트 관리 화면, 결과 선호와 quota 요약 일치. 이를 API 비용 순위로 사용하지 않음. |
| [Sol API](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Astra API](https://developers.openai.com/api/docs/models/gpt-6-astra) | 입력/출력/캐시 각각 $2/$10/$0.10, $10/$50/$1 확인. Astra의 고난도 연구·추론 용도도 명시. |
| [모델 선택 안내](https://learn.chatgpt.com/docs/models) | effort가 사고량·지연·토큰 사용에 영향을 주는 설정임을 확인. |

Terra $1/$5/$0.05와 >272k 입력·캐시2배/출력1.5배, Work 제공 범위는 앞선 동일 세션의 직접 검증 결과와 일치한다. 관련 [Terra 모델 문서](https://developers.openai.com/api/docs/models/gpt-6.1-terra), [Work 안내](https://learn.chatgpt.com/docs/whats-new/october-26-30-2026) 링크가 유지됐다.

산술 재검산: 입력단가×0.1 + 출력단가×0.01 = Terra .15 / Opus .60 / Sol .30 / Astra 1.50. comparison-cost-check.json과 일치. .15×4=.60은 고정 토큰 예시이며 실제 retry에서 토큰이 늘 수 있다는 조건도 유지됐다.

## 검증 범위

`python3 scripts/blog.py check posts/2026-10-27-gpt-6-1-terra-work` → 오류 0, 경고 0, exit 0.

이미지 및 최종 페이지/반응형 검수는 별도다. 부모가 알려 준 file:// 관리자 거부 이후 브라우저 작업은 요청하거나 재시도하지 않았다. 소스 기록만 수행하며 lifecycle은 reviewing을 유지한다.

최종 판정: 공식·독립·개인 경험을 구분하고 설정·가중평균·단가 가정을 보존한 비교 원고로 source pass. 종합 평가는 특정 난도 작업의 직접 실험으로 확대하지 않았고, 선택표는 조건부 편집 판단으로 읽힌다. 존대어 일관성과 문단 연결에 중대한 결함이 남지 않았다. 초기 판단→각 근거→선택표의 종합은 기능이 다르며 결말은 실제 작업에서 판단을 바꿀 누락·오입력/총비용 조건만 남긴다.
