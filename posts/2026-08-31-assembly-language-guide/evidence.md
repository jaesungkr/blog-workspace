# 근거 지도: 어셈블리어란 무엇인가, ARM64 코드로 읽는 사용처와 장단점

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Clang의 백엔드는 중간 표현을 대상별 어셈블리로 바꾸고, assembler는 이를 기계어 오브젝트로 바꾼다. | 공식 | 확인 | [Clang Toolchain](https://clang.llvm.org/docs/Toolchain.html) | 실제 컴파일러는 중간 파일을 만들지 않고 단계를 합칠 수 있음 |
| C02 | 어셈블리어는 하나의 범용 문법이 아니며, 대상 아키텍처와 assembler가 인식하는 명령·표기가 다르다. | 공식 | 확인 | [GNU as Statements](https://sourceware.org/binutils/docs/as/Statements.html), [AArch64 Syntax](https://sourceware.org/binutils/docs/as/AArch64-Syntax.html) | 본문은 ARM64 GNU/Clang 계열 표기만 예로 사용 |
| C03 | AArch64에는 31개의 범용 레지스터가 있고 `xN`은 64비트, `wN`은 같은 레지스터의 하위 32비트를 가리킨다. AAPCS64에서는 첫 여덟 레지스터가 인자와 결과에 쓰인다. | 공식 | 확인 | [Armv8-A ISA 안내서](https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/Learn%20the%20Architecture/Armv8-A%20Instruction%20Set%20Architecture.pdf), [AAPCS64](https://github.com/ARM-software/abi-aa/blob/main/aapcs64/aapcs64.rst) | 플랫폼 ABI가 추가 제약을 둘 수 있음 |
| C04 | A64 명령은 32비트 고정 길이로 인코딩된다. | 공식 | 확인 | [Armv8-A ISA 안내서](https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/Learn%20the%20Architecture/Armv8-A%20Instruction%20Set%20Architecture.pdf) | x86처럼 가변 길이인 다른 ISA에는 적용되지 않음 |
| C05 | Linux는 주로 C로 작성되지만 아키텍처 의존부에는 어셈블리를 사용하고, ARM64 부팅 진입부도 현재 `.S`로 유지된다. | 공식·원시 코드 | 확인 | [Linux kernel HOWTO](https://www.kernel.org/doc/html/latest/process/howto.html), [Linux ARM64 head.S](https://github.com/torvalds/linux/blob/master/arch/arm64/kernel/head.S) | 커널 전체에서 어셈블리가 차지하는 비율을 주장하지 않음 |
| C06 | 임베디드 시작 코드에서는 벡터 테이블, 초기 스택, reset handler처럼 CPU가 C 런타임보다 먼저 요구하는 상태를 다룬다. | 공식 | 확인 | [Arm Cortex-M startup file 설명](https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/decoding-the-startup-file-for-arm-cortex-m4) | 특정 Cortex-M4 예시이며 모든 MCU 초기화가 동일하지 않음 |
| C07 | GCC는 성능 민감 코드나 C가 직접 노출하지 않는 명령에 extended asm을 쓸 수 있다고 설명하고, Rust도 현재 `asm!` API를 제공한다. | 공식 | 확인 | [GCC Extended Asm](https://gcc.gnu.org/onlinedocs/gcc/Extended-Asm.html), [Rust core::arch::asm](https://doc.rust-lang.org/stable/core/arch/macro.asm.html) | API 존재가 직접 어셈블리 사용을 항상 권장한다는 뜻은 아님 |
| C08 | Microsoft는 x64·ARM64에서 인라인 assembler를 지원하지 않으며 C++, compiler intrinsic, 별도 assembler source를 대안으로 안내한다. | 공식 | 확인 | [Microsoft MASM for x64](https://learn.microsoft.com/cpp/assembler/masm/masm-for-x64-ml64-exe) | MSVC 생태계의 정책이며 GCC·Clang 전체에 일반화하지 않음 |
| C09 | GDB는 소스 줄과 주소를 연결하고 기계 명령, 원시 인코딩, 소스 혼합 디스어셈블을 보여 준다. | 공식 | 확인 | [GDB Machine Code](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Machine-Code.html) | 디스어셈블 결과가 원래 소스의 변수명과 구조를 완전히 복원하지는 않음 |
| C10 | OpenSSL은 2026년 현재도 x86-64 AES 등 일부 암호 구현에 아키텍처별 어셈블리 생성 소스를 유지한다. | 원시 코드 | 확인 | [OpenSSL aes-x86_64.pl](https://github.com/openssl/openssl/blob/master/crypto/aes/asm/aes-x86_64.pl), [OpenSSL platform config](https://github.com/openssl/openssl/blob/master/Configurations/10-main.conf) | 과거 주석의 벤치마크 수치를 현재 성능 주장에 사용하지 않음 |
| C11 | 로컬 ARM64에서 `add` 함수는 `-O2` 시 `add`와 `ret` 두 명령으로 생성됐고, 직접 작성한 동등 함수는 세 입력에서 예상값을 반환했다. | Codex 실행 | 확인 | `artifacts/experiment/examples-O2.s`, `examples-O2-objdump.txt`, `run-output.txt` | 작은 함수 한 개이며 일반적인 성능 우위를 뜻하지 않음 |
| C12 | 같은 함수의 `-O0` 출력은 인자를 스택에 저장하고 다시 읽었으며, `-O2` 출력보다 많은 명령을 사용했다. | Codex 실행 | 확인 | `artifacts/experiment/examples-O0.s`, `examples-O2.s` | 디버그 친화 출력과 최적화 출력을 비교한 구조 예시이며 실행 시간 측정이 아님 |
| C13 | macOS ARM64에서 C가 찾는 `_asm_add` 대신 `asm_add`만 내보낸 첫 소스는 링크에 실패했다. | Codex 실행 | 확인 | `artifacts/experiment/handwritten_add_naive.s`, `link-failure.txt` | Mach-O 심볼 규칙의 한 사례이며 Linux ELF와 표기가 다를 수 있음 |
| C14 | `absolute_value(int)` 구조 예제는 `INT_MIN`에서 `-x`가 표현 범위를 벗어나므로 그 입력을 제외해야 한다. | 공식·언어 의미·구조 예시 | 확인 | [Clang UndefinedBehaviorSanitizer](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html), 예제 식 `x < 0 ? -x : x` 대조 | 본문은 최솟값을 제외한 입력의 명령 구조만 설명 |

## 직접 검증 설계

- 질문: 고급 언어의 덧셈·조건문·메모리 접근·함수 호출이 현재 Apple Silicon에서 어떤 ARM64 명령과 인코딩으로 바뀌며, 직접 작성한 덧셈 함수가 C에서 호출되는가?
- 실행 주체: Codex
- 환경과 확인 시점: Apple Silicon ARM64, macOS 26.5.2, Apple Clang 21.0.0, Apple LLVM objdump 21.0.0, 2026-08-31
- 입력: `examples.c`, `handwritten_add.s`, `test_handwritten.c`
- 전처리 또는 표현: 동일 C 파일을 `clang -S -O0`, `clang -S -O2`, `clang -c -O2`로 변환하고 `objdump -d`로 오브젝트를 디스어셈블
- 비교·판정 규칙: 원 C 의미와 생성 명령을 함수별로 대응시키고, 직접 작성 함수는 세 입력의 산술 결과가 C의 예상값과 일치하면 통과
- 성공 기준: 컴파일·assemble·link가 성공하고 세 실행 결과가 각각 12, 5, 1234567이며 `objdump`가 명령 인코딩을 표시
- 반복 횟수와 표본 크기: 함수 4개를 최적화 2단계로 각 1회 생성, 직접 작성 함수 입력 3개를 각 1회 실행
- 보존할 원자료: `artifacts/experiment/`의 모든 소스, 환경, 명령, 어셈블리, 오브젝트 디스어셈블, 실행 출력, 실패 로그, SHA-256

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | `add`를 `-O2`로 컴파일 | `add w0, w1, w0`와 `ret`, 두 개의 32비트 인코딩이 생성됨 | `artifacts/experiment/examples-O2.s`, `examples-O2-objdump.txt` | ARM64·Clang 21의 작은 정수 함수 |
| E02 | `absolute_value`를 `-O2`로 컴파일 | `cmp`, 조건부 부호 반전 `cneg`, `ret` 세 명령으로 생성됨 | 같은 파일 | 분기 없는 조건부 명령을 선택한 한 사례이며 `INT_MIN` 입력은 C 의미상 제외 |
| E03 | 포인터 역참조 뒤 1 더하기 | `ldr`로 메모리에서 읽고 `add`로 즉시값 1을 더함 | 같은 파일 | 레지스터와 메모리 역할을 보여 주는 구조 예시 |
| E04 | `add_then_double`에서 noinline `add` 호출 | frame/link register 보존, `bl _add`, `lsl` 두 배 계산, 복원·반환이 생성됨 | 같은 파일 | macOS AAPCS 계열 함수 호출의 한 사례 |
| E05 | 직접 작성한 `_asm_add`를 C에서 호출 | 3개 입력이 모두 예상값과 일치 | `artifacts/experiment/run-output.txt` | 기능 확인이며 성능 비교가 아님 |
| E06 | 밑줄 없이 `asm_add` 심볼을 공개 | linker가 C의 `_asm_add`를 찾지 못해 실패 | `artifacts/experiment/link-failure.txt` | macOS Mach-O 이름 규칙의 이식성 비용 |

## 실패와 반례

- 실패한 입력: `.globl asm_add`와 `asm_add:`만 선언한 `handwritten_add_naive.s`
- 예상과 달랐던 결과: 명령 자체는 assemble됐지만 C 코드가 요구한 `_asm_add` 심볼과 이름이 달라 link에 실패했습니다.
- 수정: Mach-O C 심볼 규칙에 맞춰 `_asm_add`를 공개한 뒤 같은 C 테스트를 연결했습니다.
- 일반화하면 안 되는 범위: ARM64 명령이 같아도 object format과 platform ABI가 달라지면 심볼, 호출, stack 규칙이 달라집니다. 명령 수 차이는 실행 시간 차이를 직접 측정한 결과가 아닙니다. `absolute_value(int)`는 `INT_MIN`을 제외한 구조 예시입니다.

## 미해결 항목

- 없음. 현재 원고가 사용하는 주장과 예시는 모두 확인됐습니다.

## 출처 메모

- 공식 자료는 2026-08-31에 다시 확인했습니다.
- OpenSSL의 오래된 성능 주석은 현재 성능 수치로 옮기지 않고, 현재 저장소가 아키텍처별 어셈블리 소스를 유지한다는 사실만 사용합니다.
- Linux와 Microsoft 자료를 함께 사용해 “사라졌다” 또는 “항상 필요하다”라는 단정 대신, 고급 언어 중심에 저수준 예외가 남아 있는 현재 위치를 설명합니다.
