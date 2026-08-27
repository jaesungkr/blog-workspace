# 근거 지도: GLM-5.3-Flash 비교 - Ox Alpha 정체 공개 뒤 다시 본 성능과 가격

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Z.AI는 출시 전에 GLM-5.3-Flash를 `ox-alpha`라는 이름으로 OpenCode와 OpenRouter에서 익명 테스트했다고 밝혔습니다. | 공식 | 확인 | [Z.AI 모델 문서](https://docs.z.ai/guides/vlm/glm-5.3-flash) | oxalpha.com의 모든 요청이 같은 경로였는지는 별도 확인 불가 |
| C02 | GLM-5.3-Flash는 GLM-5 계열 최초의 네이티브 멀티모달 모델이며 320B 전체·18B 활성 매개변수를 사용합니다. | 공식 | 확인 | [Z.AI 모델 문서](https://docs.z.ai/guides/vlm/glm-5.3-flash), [Hugging Face 모델 카드](https://huggingface.co/zai-org/GLM-5.3-Flash) | 매개변수 수는 구조 정보이며 실제 작업 품질을 보장하지 않음 |
| C03 | 모델은 선형·희소 어텐션을 결합하고 100만 토큰 문맥을 지원하며, 공개 가중치는 MIT 라이선스입니다. | 공식 | 확인 | 같은 Z.AI 문서와 Hugging Face 모델 카드 | 전체 문맥 정확도와 로컬 배포 성능은 재현하지 않음 |
| C04 | Z.AI는 GLM-5.3 대비 어텐션 연산 3.01배, KV 캐시 4.44배 감소를 주장합니다. | 벤더 주장 | 확인 | [Z.AI 모델 문서](https://docs.z.ai/guides/vlm/glm-5.3-flash) | 구조 계산이며 사용자 체감 속도와 같은 지표가 아님 |
| C05 | Z.AI 표에서 GLM-5.3-Flash는 DeepSWE 63.4, Toolathlon Verified 78.4, AutomationBench 48.8로 GLM-5.2의 46.2, 59.9, 26.2보다 높습니다. | 벤더 평가 | 확인 | [Z.AI 출시 글](https://z.ai/blog/glm-5.3-flash), [Hugging Face 모델 카드](https://huggingface.co/zai-org/GLM-5.3-Flash) | 벤치마크마다 하네스·추론 설정·반복 횟수가 달라 전체 품질로 일반화할 수 없음 |
| C06 | 같은 Z.AI 표에서 GLM-5.3-Flash는 DeepSWE에서 Opus 4.8보다 높고 GPT-5.6 Terra·Gemini 3.7 Flash보다 낮습니다. | 벤더 평가 | 확인 | 같은 출시 글 | 모델별 최적 설정과 제공 환경이 동일하다고 단정할 수 없음 |
| C07 | Artificial Analysis v4.1.1에서 GLM-5.3-Flash는 지능 지수 57, 출력 50.2토큰/초, 지수 과제당 비용 $0.09, 전체 출력 150M토큰으로 측정됐습니다. | 독립 검증 | 확인 | [Artificial Analysis GLM-5.3-Flash](https://artificialanalysis.ai/models/glm-5-3-flash/) | 2026-08-27 시점의 API 측정이며 공급 상태에 따라 변할 수 있음 |
| C08 | 같은 지수에서 GLM-5.2는 53·69.3토큰/초·$0.44·140M토큰입니다. | 독립 검증 | 확인 | [Artificial Analysis GLM-5.2](https://artificialanalysis.ai/models/glm-5-2) | 복합 지수는 개별 코딩 작업의 승패가 아님 |
| C09 | 같은 지수에서 GPT-5.6 Terra max는 57·108.9토큰/초·$0.53·96M토큰, Gemini 3.7 Flash high는 56·361.7토큰/초·$0.40·64M토큰입니다. | 독립 검증 | 확인 | [GPT-5.6 Terra](https://artificialanalysis.ai/models/gpt-5-6-terra), [Gemini 3.7 Flash](https://artificialanalysis.ai/models/gemini-3-7-flash) | 추론 노력 수준이 모델마다 다르며 공급자·API도 다름 |
| C10 | Z.AI 정상가는 입력 $0.15·캐시 입력 $0.03·출력 $0.50/1M토큰이며, 2026-09-09 24:00 UTC+8까지 50% 할인을 안내합니다. | 공식 | 확인 | [Z.AI 가격표](https://docs.z.ai/guides/overview/pricing) | 할인 종료 뒤 정상가로 돌아가며 공급자 가격은 다를 수 있음 |
| C11 | 정상가로 입력 1,000만·출력 200만 토큰을 계산하면 GLM-5.3-Flash는 $2.50, GLM-5.3·5.2는 $22.80입니다. | Codex 실행 | 확인 | `artifacts/compare_costs.py`, `artifacts/compare_costs.txt` | 캐시·도구 호출·저장 비용과 공급자 마진을 제외한 구조 예시 |
| C12 | 2026-08-24 Codex가 oxalpha.com에서 실행한 네 문항은 React 진단·근거 제한·계산을 통과하고 일정 퍼즐의 검산을 실패했습니다. | Codex 실행 | 확인 | `../2026-08-24-ox-alpha-review/artifacts/test-prompts-and-responses.md` | 독립 사이트의 상위 제공자를 확인하지 못했으므로 GLM-5.3-Flash 결과로 귀속하지 않음 |
| C13 | GLM-5.3-Flash는 추론을 끌 수 없고 `reasoning_effort`의 low·high·max를 지원하며 기본값은 max입니다. | 공식 | 확인 | Z.AI 모델 문서와 Hugging Face 모델 카드 | 노력 수준별 속도·품질은 이번 글에서 재측정하지 않음 |
| C14 | OpenRouter는 정식 모델 페이지에서 2026-08-26 출시, 131,072 최대 출력, 공급자별 지연·처리량 차이를 표시합니다. | 공식 플랫폼 | 확인 | [OpenRouter 모델 페이지](https://openrouter.ai/z-ai/glm-5.3-flash) | 공급자 수치와 가격은 실시간으로 변할 수 있음 |

## 비교 설계

- 질문: 정식 공개 뒤 GLM-5.3-Flash를 기본 코딩 모델로 둘 근거가 충분한가요?
- 실행 주체: 공개 수치는 Z.AI와 Artificial Analysis, 가격 시나리오와 기존 테스트 재해석은 Codex
- 환경과 확인 시점: 2026-08-27 Asia/Seoul, 공개 웹 문서와 저장소 원자료
- 입력: Z.AI의 모델·가격·벤치마크 문서, Artificial Analysis v4.1.1 요약, 2026-08-24 oxalpha.com 네 문항 원자료
- 전처리 또는 표현: 제조사 평가와 독립 측정을 분리하고, 독립 지표는 동일 페이지 형식의 지능·출력 속도·과제당 비용·출력량만 비교
- 비교·판정 규칙: 지능 지수와 출력 속도는 높을수록, 과제당 비용은 낮을수록 유리하다고 읽습니다. 전체 출력량은 답변·추론에 사용한 토큰이므로 비슷한 점수의 비용 효율을 해석할 때만 참고하고, 한 지표로 종합 우승을 정하지 않습니다.
- 성공 기준: 기본 후보는 GLM-5.2보다 높은 독립 지능 지수와 낮은 비용을 함께 보여야 하며, 예외 조건은 속도와 검산 실패로 명시
- 반복 횟수와 표본 크기: 외부 지표는 각 평가 기관이 공개한 값 1개씩, 기존 Codex 테스트는 문항별 1회
- 보존할 원자료: `artifacts/compare_costs.py`, `artifacts/compare_costs.txt`, 이전 번들의 `artifacts/test-prompts-and-responses.md`

## 가격 계산 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | 입력 1,000만·출력 200만 토큰, 캐시 제외, 현재 할인가 | GLM-5.3-Flash $1.25 | `artifacts/compare_costs.txt` | 2026-09-09까지의 일시 가격 |
| E02 | 같은 사용량, 정상가 | GLM-5.3-Flash $2.50 | 같은 파일 | 장기 비교용 기준 |
| E03 | 같은 사용량, Z.AI 가격표의 GLM-5.3·5.2 | 각각 $22.80 | 같은 파일 | Flash 정상가의 9.12배 |

## 기존 직접 테스트의 실패와 반례

- 실패한 입력: 일정 퍼즐에서 oxalpha.com 응답이 `C-A-B-D-E`를 제시하고 `C=1`, `D=4`를 정확히 두 슬롯 차이라고 오판했습니다.
- 예상과 달랐던 결과: 답과 검산 문장이 같은 산술 오류를 반복했습니다.
- 반례: 오류를 지적한 새 대화에서는 유일한 정답 `A-B-C-E-D`를 찾았습니다.
- 일반화하면 안 되는 범위: 이 한 건으로 GLM-5.3-Flash가 논리에 약하다고 결론 내리지 않으며, 3/4 통과를 정확도 75%로 쓰지 않습니다.

## 미해결 항목

- OpenRouter는 문맥을 1,310,720토큰으로 표시하지만 Z.AI 공식 문서는 1M으로 설명합니다. 본문은 공급자 메타데이터를 섞지 않고 공식 문서의 `100만 토큰`만 사용합니다.
- oxalpha.com 독립 웹 인터페이스의 모든 요청이 OpenRouter·OpenCode의 공식 `ox-alpha` 경로와 동일했는지는 확인하지 못했습니다. 본문은 Z.AI가 확인한 익명 사전 테스트와 dev.log가 사용한 사이트 관찰을 구분합니다.
- GLM-5.3-Flash의 100만 토큰 전체 문맥, 멀티모달, 로컬 배포, 노력 수준별 성능은 주장하지 않습니다.

## 출처 메모

- OpenCode·OpenRouter에서 제공된 공식 `ox-alpha = GLM-5.3-Flash`는 공개 포렌식 추정이 아니라 Z.AI의 정식 확인으로 갱신합니다.
- Z.AI 수치는 제조사 평가로, Artificial Analysis 수치는 독립 복합 지표로 표시합니다.
- Artificial Analysis에서 `Flash`는 제품명일 뿐 출력 속도 1위를 뜻하지 않습니다. 같은 시점 GLM-5.3-Flash는 50.2토큰/초, Gemini 3.7 Flash high는 361.7토큰/초로 측정됐습니다.
- 장기 비용 판단에는 50% 할인가가 아니라 정상가를 사용하고, 할인 종료 시각은 별도로 알립니다.
