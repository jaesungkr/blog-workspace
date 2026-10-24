---
title: "REA 사용법: 메모 앱 분석으로 확인한 기능과 한계"
slug: rea-open-source
date: 2026-10-17
category: "Log"
subcategory: "개발 · 디지털"
status: reviewing
format: rich-post-v2
tags: [REA, 오픈소스, 역공학, AI, 개발도구]
summary: "작은 메모 앱을 REA로 분석해 저장 코드를 찾고, 쉼표·따옴표·줄바꿈이 들어간 CSV 출력을 실행 결과와 대조했습니다."
hero_image: assets/rea-official-lead.png
published_url: "https://dop3n.tistory.com/entry/REA란-AI로-앱의-작동-원리를-알아내는-오픈소스-도구"
sources:
  - https://github.com/morluto/rea
  - https://rea.tools/first-investigation/
  - https://rea.tools/get-started/
  - https://rea.tools/faq/
  - https://registry.npmjs.org/rea-agents/6.7.0
---

안녕하세요. dev.log입니다.

앱에서 ‘내보내기’를 눌렀는데 파일이 어디에 저장되는지 모르겠다면, 버튼과 연결된 코드를 찾아보면 됩니다. **REA(Reverse Engineer Anything)는 AI가 이런 코드를 찾아 프로그램의 작동 방식을 설명하도록 돕는 오픈소스 도구**입니다. 프로그램을 분석해 어떤 코드가 서로 연결되는지 정리해 줍니다.

처음 써본다면 [공식 실습에서 제공하는 작은 메모 앱](https://rea.tools/first-investigation/)으로 시작해 보세요. 이 예제로 파일을 저장하는 코드를 찾고, 메모 제목에 쉼표나 따옴표가 들어가도 제대로 내보내는지 확인했습니다.

{{media:rea-official-lead}}

### 메모 앱 하나로 시작하기

실습에 쓸 메모 앱은 파일이 여섯 개뿐입니다. 데스크톱 앱을 만드는 Electron으로 작성됐지만, 여기서는 코드를 읽고 변환 함수만 실행하므로 Electron을 설치하지 않아도 됩니다. [공식 예제 ZIP](https://rea.tools/examples/notes-example.zip)을 내려받아 압축을 풀면 `notes-example` 폴더가 나옵니다.

명령을 실행하려면 JavaScript 실행 프로그램인 Node.js와 패키지 관리 도구인 npm이 필요합니다. npm에 포함된 `npx`로 REA를 내려받아 실행할 수 있습니다. REA 6.7.0을 쓰려면 Node.js 버전이 다음 중 하나에 해당해야 합니다.

- 22 계열: 22.19 이상
- 24 계열: 24.11 이상
- 26 이상

터미널에서 `node -v`로 버전을 확인하고, `notes-example` 폴더가 들어 있는 상위 폴더로 이동하세요.

본문의 명령은 macOS·Linux에서 Bash나 Zsh를 사용할 때 실행하는 형태입니다. Windows PowerShell을 쓴다면 [공식 실습의 PowerShell 명령](https://rea.tools/first-investigation/#check)을 참고하세요. 실험은 macOS arm64, Node.js 26.0.0, npm 11.12.1에서 진행했으며 REA 버전은 6.7.0으로 맞췄습니다.

```bash
npx -y rea-agents@6.7.0 analyze-javascript-application \
  ./notes-example --format json --full-output
```

이 명령을 실행하면 REA가 앱 파일을 읽고, 분석 결과를 JSON 형식의 텍스트로 보여 줍니다. 여기서는 AI 채팅에 연결하지 않고 터미널에서 REA만 실행합니다. [공식 시작 안내](https://rea.tools/get-started/)에는 AI 채팅에서 REA 도구를 호출할 수 있도록 연결하는 MCP 설정 방법도 나와 있습니다.

결과에서 `ok`가 `true`이면 분석이 완료됐다는 뜻이고, `parse_failures`가 `0`이면 파일을 해석하다 실패한 경우가 없다는 뜻입니다. 이번에는 전체 여섯 파일 중 JavaScript 파일 네 개를 분석했습니다. 내보내기 요청을 보내는 코드 한 곳과 이를 받아 처리하는 코드 한 곳도 연결했습니다.

### 내보내기 버튼에서 저장 코드까지

예제의 ‘Export notes’ 버튼은 파일을 어디에 저장하고, 그 파일에는 무엇이 들어갈까요? REA의 분석 결과와 실제 코드를 함께 보면 버튼을 누른 뒤 어떤 처리가 이어지는지 알 수 있습니다.

{{media:rea-notes-flow}}

| 파일 | 확인한 처리 | 다음 단계 |
|---|---|---|
| `renderer.js` | 버튼 클릭 시 `notes.exportCsv()`를 호출합니다. | 화면에서 내보내기를 요청합니다. |
| `preload.js` | `notes:export`라는 이름으로 요청을 보냅니다. | 앱 내부의 처리 코드로 전달합니다. |
| `main.js` | 같은 이름의 요청을 받아 저장 경로를 정합니다. | CSV를 만든 뒤 파일에 씁니다. |
| `csv.js` | 메모의 번호와 제목을 CSV로 변환합니다. | 파일에 들어갈 문자열을 돌려줍니다. |

화면에서 요청을 보내면 앱 내부에서 이를 받아 처리합니다. Electron은 이때 IPC라는 통신 방식을 사용합니다. REA 결과에 나온 `paired_renderer_transmissions: 1`은 요청 하나와 이를 받는 코드 한 곳을 연결했다는 뜻입니다. 이 코드를 따라가면 저장 위치와 파일 내용을 찾을 수 있습니다.

파일을 저장하는 부분은 [공식 예제의 `main.js`](https://rea.tools/examples/notes-electron/main.js) 8~12행에 있습니다.

```javascript
ipcMain.handle("notes:export", () => {
  const destination = path.join(app.getPath("downloads"), "notes.csv");
  writeFileSync(destination, toCsv(notes), "utf8");
  return destination;
});
```

코드에는 다운로드 폴더에 `notes.csv`를 만들고, `toCsv(notes)`로 변환한 메모 내용을 쓰도록 되어 있습니다. CSV는 데이터를 행과 열로 나눠 저장하는 텍스트 파일입니다. 엑셀 같은 프로그램으로 열 수 있으며, 이 예제에는 메모 번호인 `id`와 제목인 `title` 두 열이 들어갑니다.

여기까지는 코드를 읽어서 확인한 내용입니다. 앱을 실행해 다운로드 폴더에 파일이 만들어지는지까지 확인하지는 않았습니다. 폴더에 쓰기 권한이 없거나 디스크에 문제가 생겼을 때의 동작도 따로 확인해야 합니다.

### 쉼표가 들어간 메모도 그대로 저장될까?

CSV는 쉼표를 기준으로 열을 나눕니다. 그렇다면 제목이 `Hello, "REA"`일 때는 어떻게 될까요? 제목에 들어 있는 쉼표도 열을 나누는 기호로 읽힐 수 있습니다. 공식 실습에서도 이 제목을 넣어 변환 결과를 확인합니다.

실험에서는 일반 제목과 공식 예제의 제목, 한국어가 들어간 제목, 줄바꿈이 있는 제목, 빈 메모 목록을 넣어 봤습니다. 원본 `csv.js`는 수정하지 않고 `toCsv` 함수에 이 다섯 입력을 전달했습니다. 먼저 정해 둔 예상 문자열과 실제 출력을 비교하고, Python으로 CSV를 다시 읽어 메모 번호와 제목이 원래 값과 같은지도 확인했습니다.

| 입력 | 실제 출력에서 확인한 점 | 다시 읽은 결과 |
|---|---|---|
| `First note` | 제목을 큰따옴표로 감쌌습니다. | 원래 제목과 같았습니다. |
| `Hello, "REA"` | 제목 안의 큰따옴표를 두 번 적었습니다. | 쉼표와 따옴표가 유지됐습니다. |
| `서울, "메모"` | 한국어 제목에도 같은 규칙을 적용했습니다. | 원래 제목과 같았습니다. |
| 두 줄로 된 제목 | 큰따옴표 안에 실제 줄바꿈을 남겼습니다. | 한 제목 안의 줄바꿈이 유지됐습니다. |
| 빈 메모 목록 | 열 이름인 `id,title`만 출력했습니다. | 데이터 행이 없었습니다. |

`Hello, "REA"`의 실제 출력은 다음과 같습니다.

```csv
id,title
1,"Hello, ""REA"""
```

{{media:rea-csv-escaping}}

제목 전체를 큰따옴표로 감싸면 제목에 들어 있는 쉼표를 열 구분자와 구별할 수 있습니다. 제목 안의 큰따옴표는 `""`처럼 두 번 적습니다. CSV를 다시 읽으면 이 두 글자를 큰따옴표 하나로 해석합니다.

이 예제에서는 다섯 입력 모두 예상한 문자열로 변환됐고, 다시 읽은 메모 번호와 제목도 원래 값과 같았습니다.

직접 확인하려면 `notes-example` 폴더에서 아래 명령을 실행해 보세요. 제목을 바꾸면 다른 입력도 확인할 수 있습니다.

```bash
node -e 'const {toCsv}=require("./csv.js"); process.stdout.write(toCsv([{id:1,title:"Hello, \"REA\""}]))'
```

### 일반 AI에게 파일을 읽히면 어떨까?

파일을 읽을 수 있는 개발용 AI라면 같은 폴더를 주고 “메모를 어디에 저장하는지 찾아줘”라고 요청해도 됩니다. 이번 예제는 파일이 여섯 개뿐이라, REA 없이 코드를 읽어도 저장 위치를 찾기 어렵지 않습니다.

REA는 파일을 분석해 **화면에서 보낸 요청을 어느 코드가 받는지, 그 코드가 어디에 있는지 정리해 줍니다.** AI는 이 결과를 참고해 동작을 설명합니다. 다만 이번에는 같은 AI에 REA를 연결했을 때와 연결하지 않았을 때를 비교하지 않았습니다. 어느 쪽이 더 빠르고 정확한지는 별도의 비교가 필요합니다.

AI가 동작을 설명했다면 “그 내용을 어느 파일의 어떤 코드에서 확인할 수 있나요?”라고 물어보세요. 해당 코드를 찾으면 이번 CSV 변환처럼 작은 입력을 넣어 설명이 맞는지 확인할 수 있습니다.

### 어떤 앱부터 맡기면 좋을까?

처음에는 자신이 만들었거나 분석을 허가받은 앱에서, 내보내기처럼 결과를 확인하기 쉬운 기능 하나를 골라 보세요. 소스 코드가 있는지, 완성된 실행 파일만 있는지에 따라 필요한 도구가 달라집니다. [공식 FAQ](https://rea.tools/faq/)에서도 두 경우를 구분해 안내합니다.

| 확인하려는 대상 | 시작할 방법 | 준비할 것 |
|---|---|---|
| REA가 무엇을 하는지 | 공식 계산기·게임 데모를 봅니다. | 웹브라우저가 있으면 됩니다. |
| 이번 메모 앱처럼 소스가 있는 예제 | 폴더를 지정해 정적 분석을 실행합니다. | Node.js와 npm이 필요합니다. |
| 완성된 실행 파일의 내부를 자세히 분석하기 | 대상에 맞는 분석 도구를 연결합니다. | Hopper·Ghidra·IDA 같은 별도 도구가 필요합니다. |

분석할 수 있는 범위는 가진 자료에 따라 달라집니다. 웹페이지를 분석한다고 비공개 서버 코드까지 볼 수는 없습니다. 실행 파일을 분석해도 원래 코드에 있던 주석과 변수 이름을 모두 되찾을 수는 없습니다.

REA 자체는 [MIT 라이선스](https://github.com/morluto/rea/blob/main/LICENSE)로 공개되어 있습니다. 함께 쓰는 AI 서비스나 일부 분석 도구에는 별도 비용이 들 수 있습니다. 회사나 고객의 앱을 AI로 분석할 때는 분석 결과가 AI 서비스로 전달될 수 있으므로, [모델 제공자의 데이터 정책](https://rea.tools/faq/#sharing)도 먼저 확인하세요.

저장 위치를 찾았다면 다음에는 “파일 저장에 실패하면 화면에 어떤 오류가 표시되나요?”라고 물어보세요. 같은 내보내기 기능에서 오류를 처리하는 코드까지 찾아볼 수 있습니다.
