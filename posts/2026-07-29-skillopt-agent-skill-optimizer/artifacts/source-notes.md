# SkillOpt 출처 대조 메모

확인일은 모두 2026-07-29입니다.

## 공식 저장소와 버전

- 저장소: https://github.com/microsoft/SkillOpt
- 조사 커밋:
  `8304e6c3eceae36bc595e58a34b4a422ae6b2d4f`
- PyPI·`pyproject.toml` 버전: `0.2.0`
- Python 요구 사항: `>=3.10`
- 라이선스: MIT
- `main` 문서는 PyPI 0.2.0 이후의 미출시 기능도 설명합니다. 설치 글에서는
  재현성을 위해 release와 main을 섞지 않도록 구분해야 합니다.

## 핵심 동작

공식 논문 v2, README, `docs/guide/training-loop.md`,
`skillopt/engine/trainer.py`, `skillopt/evaluation/gate.py`를 대조했습니다.

1. 동결된 대상 모델이 현재 스킬로 훈련 작업을 실행하고 궤적과 점수를 남깁니다.
2. 별도 옵티마이저 모델이 성공과 실패 궤적을 반영해 add/delete/replace
   편집을 제안합니다.
3. 편집을 병합하고 순위를 매긴 뒤 텍스트 학습률이 허용한 수만 적용합니다.
4. 후보 스킬을 분리한 selection split에서 평가합니다.
5. 현재 점수보다 엄격히 높으면 채택하고, 동점이나 하락이면 거절합니다.
6. 거절 편집은 같은 epoch의 후속 반영에 부정적 피드백으로 쓰입니다.
7. 최선의 통과본만 `best_skill.md`로 배포합니다.

기본 config는 `num_epochs: 4`, `batch_size: 40`,
`gradient.minibatch_size: 8`, `learning_rate: 4`,
`min_learning_rate: 2`, `lr_scheduler: cosine`, `use_gate: true`입니다.
이는 논문 실험 기본값이지 모든 사용자 데이터셋의 권장 최적값은 아닙니다.

## 논문 결과와 비용

- 논문: https://arxiv.org/abs/2605.23904 (v2, 2026-05-25)
- 범위: 6개 벤치마크, 7개 대상 모델, 직접 채팅·Codex·Claude Code
- 저자 보고: 비교한 52개 평가 셀에서 최고 또는 공동 최고
- GPT-5.5 no-skill 대비 평균 향상:
  - 직접 채팅 `+23.5` percentage points
  - Codex `+24.8` points
  - Claude Code `+19.1` points
- GPT-5.5 사례 6개의 최종 스킬: 379~1,995 토큰
- 채택된 편집 수: 1~4개
- 학습 토큰: 20.8M~213.8M

이 수치는 연구팀이 보고한 실험 결과입니다. 로컬 검증은 코드 게이트와 저장소
테스트에 한정하며, 성능 수치를 독립 재현했다고 표현하지 않습니다.

## 현재 main과 논문식 재현의 차이

`ckpt/README.md`는 논문 checkpoint가 아래 설정으로 만들어졌다고 밝힙니다.

```yaml
optimizer:
  slow_update_gate_with_selection: true
```

현재 main의 기본값은 `false`입니다. 문서 설명에 따르면 epoch 경계의 slow
update를 selection gate 없이 current/best skill에 반영하는 출시 후 동작입니다.
논문 checkpoint를 그대로 재현하려면 이 설정 차이를 확인해야 합니다. 단계별
일반 후보를 판단하는 `evaluation.use_gate: true`와는 별도 옵션입니다.

## 한계

논문 Appendix B는 다음을 직접 밝힙니다.

- scored trajectory와 held-out selection split이 필요합니다.
- 주관적·다차원·비싼 평가는 더 강한 사람 또는 모델 기반 검증이 필요합니다.
- 훈련에는 추가 rollout과 옵티마이저 모델 호출 비용이 듭니다.
- 하나의 휴대 가능한 스킬은 매우 이질적인 여러 절차를 모두 담기 부족할 수
  있습니다.
- 다른 모델·도구·작업으로 옮길 때도 별도 held-out 평가가 필요합니다.

## 연구 엔진과 SkillOpt-Sleep

- 연구 엔진: 명시적 train/selection/test split에서 스킬을 훈련·평가하고
  `best_skill.md`를 만듭니다.
- SkillOpt-Sleep: 지원하는 코딩 에이전트 세션을 수집해 반복 작업을 찾고,
  야간 재생·통합 제안을 사용자 검토용으로 staging하는 preview입니다.
- Sleep의 실제 backend는 세션에서 뽑은 내용을 공급자에게 보낼 수 있으므로
  민감한 프로젝트에서는 source, provider policy, redaction, evidence log를
  먼저 검토해야 합니다.
