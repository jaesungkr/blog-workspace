# Kimi K3 source snapshot

- 확인일: 2026-07-30
- 수집 주체: Codex
- 목적: Kimi K3 글의 공식 주장, 재계산 입력, 미디어 출처 보존

| 로컬 파일 | SHA-256 | 원본 URL | 용도 |
|---|---|---|---|
| `sources/kimi-k3-tech-blog.html` | `878b6bc788c2762b533a391376d8a7bc55b9ae36a9aefcfbcc52ddf6966a5348` | https://www.kimi.com/blog/kimi-k3 | 출시 설명·인프라 권장·공식 한계 |
| `sources/kimi-k3-readme.md` | `46bb1354d6d5352b3e791e120667d386dbfb12b3f78b7916b4f31d49a0400443` | https://raw.githubusercontent.com/MoonshotAI/Kimi-K3/main/README.md | 모델 사양·벤치마크·사용법 |
| `sources/kimi-k3-license.txt` | `f45c677fa7f42405512b67f9b18b4ccd6927c6787492867763d80368631b7c54` | https://raw.githubusercontent.com/MoonshotAI/Kimi-K3/main/LICENSE | 공개 가중치 라이선스 |
| `sources/huggingface-model-blobs.json` | `0cae7ad7f36336827eb2b65d84587af81d6f508cb59b3b2c7458adb758e930de` | https://huggingface.co/api/models/moonshotai/Kimi-K3?blobs=true | 샤드 수·크기·revision |
| `sources/huggingface-model.json` | `62626600b7c860cdd75d42b65b5ed18422a3293e00b3ad06a639b7e0c3c8a8ff` | https://huggingface.co/api/models/moonshotai/Kimi-K3?expand=siblings | 파일 목록 교차 확인 |
| `sources/kimi-api-llms.txt` | `42edee0f8a0bb0509edc957f2308bf8e12807108d141d5aa8286469b10dff0dc` | https://platform.kimi.ai/docs/llms.txt | API 문서 색인 |

공식 블로그와 모델 카드는 제품 제공자의 주장입니다. 코딩 성능 수치는
독립 재실행 결과로 취급하지 않습니다. Hugging Face API의 파일 크기는 저장
용량 계산에만 쓰며 실제 추론 메모리나 처리량으로 일반화하지 않습니다.
