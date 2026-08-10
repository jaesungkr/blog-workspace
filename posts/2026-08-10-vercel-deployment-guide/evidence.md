# 근거 지도: Vercel 사용법, GitHub 첫 배포부터 환경 변수·도메인까지

확인일은 모두 2026-08-10입니다. 원문 HTML과 본문에 사용한 공식 이미지 원본은 `artifacts/sources/`에 보존했습니다.

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Vercel은 Git 저장소를 연결해 웹 앱을 빌드·배포할 수 있는 플랫폼이며 자동 Preview·Production 환경을 제공합니다. | 공식 | 확인 | [Getting started with Vercel](https://vercel.com/docs/getting-started-with-vercel), `vercel-getting-started.html` | Vercel의 제품 정의이며 다른 플랫폼과의 독립 비교가 아닙니다. |
| C02 | 대시보드에서 프로젝트를 만들고 저장소를 고른 뒤 프로젝트 이름, Framework Preset, Root Directory, Build Output Settings, 환경 변수를 확인하고 Deploy를 실행할 수 있습니다. | 공식 | 확인 | [Deploying Git Repositories with Vercel](https://vercel.com/docs/git), [Managing Projects](https://vercel.com/docs/projects/managing-projects), `vercel-git.html`, `vercel-managing-projects.html`, `ui/add-new-project-light.png` | 프로젝트 구조에 따라 자동 감지가 틀릴 수 있고 화면 배치는 바뀔 수 있습니다. |
| C03 | 새 프로젝트의 첫 배포는 항상 Production이며, 그 뒤 Production Branch의 변경은 Production으로, 그 밖의 브랜치·PR·무옵션 `vercel`은 Preview로 배포됩니다. | 공식 | 확인 | [Environments - First deployment](https://vercel.com/docs/deployments/environments#first-deployment), [Deploying Git Repositories with Vercel](https://vercel.com/docs/git), `vercel-environments.html`, `vercel-git.html` | Production Branch는 설정에서 다른 브랜치로 바꿀 수 있습니다. |
| C04 | 환경 변수는 Production·Preview·Development 등 대상 환경을 나눠 설정하며, 변경값은 과거 배포가 아니라 새 배포에 적용됩니다. 프레임워크별 공개 접두사는 브라우저 노출과 관계가 있습니다. | 공식 | 확인 | [Environment variables](https://vercel.com/docs/environment-variables), [Framework environment variables](https://vercel.com/docs/environment-variables/framework-environment-variables), `vercel-environment-variables.html`, `vercel-framework-environment-variables.html`, `ui/env-var-section-light.png` | 실제 공개 규칙은 사용 중인 프레임워크 문서도 함께 확인해야 하며 UI 배치는 바뀔 수 있습니다. |
| C05 | 사용자 도메인은 Project Settings의 Domains에서 추가하며, apex 도메인은 A 레코드, 서브도메인은 CNAME이 일반적입니다. 프로젝트 화면이 요구하는 Type·Name·Value를 DNS에 옮기고, DNS 검증 뒤 Vercel이 SSL 인증서 생성을 자동으로 시도합니다. | 공식 | 확인 | [Adding & Configuring a Custom Domain](https://vercel.com/docs/domains/working-with-domains/add-a-domain), [Working with SSL Certificates](https://vercel.com/docs/domains/working-with-ssl), `vercel-add-domain.html`, `vercel-working-with-ssl.html`, `ui/verify-domain-light.png` | 실제 DNS 값은 프로젝트 화면이 제시한 값을 우선해야 하며 전파와 인증서 검증에 시간이 걸릴 수 있습니다. |
| C06 | GitHub 저장소가 목록에 없다면 개인 저장소 소유권, 조직 역할, 저장소 접근 권한, Vercel GitHub App 권한을 확인해야 합니다. | 공식 | 확인 | [Deploying GitHub Projects with Vercel](https://vercel.com/docs/git/vercel-for-github) | 조직 정책과 요금제에 따라 추가 제한이 생길 수 있습니다. |
| C07 | Instant Rollback은 이전 운영 배포로 트래픽을 돌릴 수 있으나, 환경 변수 변경은 함께 갱신되지 않으며 Hobby는 직전 운영 배포만 대상으로 합니다. | 공식 | 확인 | [Performing an Instant Rollback](https://vercel.com/docs/instant-rollback), `vercel-instant-rollback.html` | 롤백 뒤 운영 도메인 자동 할당을 다시 활성화해야 하는 흐름이 생길 수 있습니다. |
| C08 | 초보자는 배포 전 빌드, Root Directory, 환경 변수 범위, Production Branch, Preview URL, 도메인 DNS를 순서대로 확인하면 원인을 더 빨리 좁힐 수 있습니다. | Codex 작성 결정 프레임워크 | 확인 | C02-C07을 실제 설정 의존 순서로 재배열 | 계정 화면을 직접 조작해 얻은 통계나 성공률은 아닙니다. |

## 직접 검증 설계

- 질문: 공식 문서의 여러 설정을 초보자가 실제로 확인할 순서로 줄일 수 있는가?
- 실행 주체: Codex
- 환경과 확인 시점: 2026-08-10, Vercel 공식 문서 10개 대조
- 입력: 프로젝트 생성, Git 배포, 환경 변수, 사용자 도메인, 롤백 문서의 전제와 동작
- 전처리 또는 표현: `최초 배포 전 -> 브랜치 배포 -> 운영 연결 -> 실패 복구` 단계로 분류
- 비교·판정 규칙: 앞 단계가 틀리면 뒤 단계 확인이 무의미한 항목을 먼저 배치
- 성공 기준: 독자가 증상 하나를 보고 첫 확인 화면과 다음 행동을 한 행에서 찾을 수 있음
- 반복 횟수와 표본 크기: 공식 문서 10개, 독립 성능 실험 없음
- 보존할 원자료: `artifacts/sources/*.html`, `artifacts/sources/vercel-getting-started-og.png`, `artifacts/sources/ui/*.png`

## 결과

| 산출물 | 관찰 결과 | 본문 위치 | 해석 범위 |
|---|---|---|---|
| 배포 전 6문항 | 빌드·경로·환경·브랜치·Preview·DNS 순서로 확인 지점을 압축 | `배포 버튼 전 6문항` | 초보자의 기본 Git 연동 배포 |
| 증상별 첫 확인 지점 | 저장소 누락, 빌드 실패, Preview/Production 차이, 도메인 대기를 각각 권한·로그·환경 범위·DNS로 연결 | `막혔을 때 첫 확인 지점` | 공식 문서에 나온 대표 문제만 포함 |
| 공식 UI 스크린샷 3개 | 프로젝트 생성 메뉴, 환경 변수 입력 구조, DNS 레코드 표에서 독자가 봐야 할 위치를 각각 시각화 | 프로젝트 생성·환경 변수·사용자 도메인 절 | 공식 문서 화면이며 특정 사용자 계정의 실행 결과가 아님 |

## 실패와 반례

- 직접 계정이나 프로젝트를 조작하지 않았으므로 특정 UI 배치와 성공 시간을 체험값으로 단정하지 않습니다.
- 모노레포, 사설 패키지, 커스텀 런타임, 외부 DNS·조직 정책은 기본 흐름만으로 해결되지 않을 수 있습니다.
- DNS 전파 시간과 빌드 시간은 환경마다 달라 숫자로 약속하지 않습니다.
- 롤백은 코드 배포를 되돌리지만 외부 데이터베이스나 API 상태까지 되돌리지 않습니다.

## 미해결 항목

- 없음. 계정·요금제·프로젝트별 세부값은 독자가 자신의 Vercel 화면에서 확인하도록 범위를 명시합니다.

## 출처 스냅숏 SHA-256

| 파일 | SHA-256 |
|---|---|
| `vercel-getting-started.html` | `cdb2bb95276cb46f38add664874fbccc7408405d9e3e1a1ef040e40c9fce2e8a` |
| `vercel-git.html` | `f191fc98b5e599e6a450be368e40401159dd76f7db9678fad2ca2fa2f2949abe` |
| `vercel-environment-variables.html` | `dfb5b19af75ed38c4bea73385f3c4ea983cb764e85700830a4dcd1b650c3529e` |
| `vercel-add-domain.html` | `862c11d824e0748fdf62bc111b48704c43fc508d5eddf4e62b4042535106268c` |
| `vercel-instant-rollback.html` | `1572318d90d638170fe99a126bd2a8aa2b6cd52922a77ec414543751b8706754` |
| `vercel-for-github.html` | `144ba55c8b6b59bf7c82ad0c3ff85e02c38b9f66c080eaaae7250d30365fb417` |
| `vercel-managing-projects.html` | `318a98a5ef2a4054ab469c142ac3c5ceb694db318b879192e263713608c97f88` |
| `vercel-environments.html` | `6c245385a8105c2a49e24f227f294cc6ab33d767153f4aa7d8cf0ba74d7e66b4` |
| `vercel-framework-environment-variables.html` | `8e6d85873ef7bf0b394b6df6f7afa009645a9807b6c1267fe6cfe03ada9f3de0` |
| `vercel-working-with-ssl.html` | `e063c0e8477b41dbb56a2839d3ea4661231b3826c11afca55f4143df969dedce` |
| `vercel-getting-started-og.png` | `49120e5aba964096551376e0015381ebccee1424f035b91992cd0daf4d906a40` |
| `ui/add-new-project-light.png` | `d46f775fde97174f5e8278160869879361e88b91efedec34ab293ca8d48daec5` |
| `ui/env-var-section-light.png` | `ae7e68d58e720ccd6779fb9bc8e9e03921e68ca8d5eda27410d07473ff374c28` |
| `ui/verify-domain-light.png` | `b649bcfefee71fcb0abb22aeaeeb8792bfa111d788521822034e8e3f5a06fcd6` |
