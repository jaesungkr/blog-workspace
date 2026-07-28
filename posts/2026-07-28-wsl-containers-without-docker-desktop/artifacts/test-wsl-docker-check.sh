#!/usr/bin/env bash
set -u

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
checker="$script_dir/wsl-docker-check.sh"
test_root="$(mktemp -d)"
trap 'rm -rf "$test_root"' EXIT

passed=0
failed=0

make_common_mocks() {
  mock_dir="$1"
  mkdir -p "$mock_dir"

  cat >"$mock_dir/ps" <<'MOCK'
#!/usr/bin/env bash
printf '%s\n' "${MOCK_PID_ONE:-systemd}"
MOCK

  cat >"$mock_dir/systemctl" <<'MOCK'
#!/usr/bin/env bash
if [ "${MOCK_SERVICE_ACTIVE:-yes}" = "yes" ]; then
  exit 0
fi
exit 3
MOCK

  chmod +x "$mock_dir/ps" "$mock_dir/systemctl"
}

make_docker_mock() {
  mock_dir="$1"
  cat >"$mock_dir/docker" <<'MOCK'
#!/usr/bin/env bash
if [ "${1:-}" = "info" ]; then
  case "${MOCK_DOCKER_INFO:-ok}" in
    ok) exit 0 ;;
    permission)
      printf '%s\n' 'permission denied while trying to connect to the docker API' >&2
      exit 1
      ;;
    *) exit 1 ;;
  esac
fi
if [ "${1:-}" = "compose" ] && [ "${2:-}" = "version" ]; then
  [ "${MOCK_COMPOSE:-yes}" = "yes" ]
  exit
fi
exit 1
MOCK
  chmod +x "$mock_dir/docker"
}

run_case() {
  name="$1"
  expected_exit="$2"
  expected_text="$3"
  include_docker="$4"
  mock_pid_one="$5"
  mock_service_active="$6"
  mock_docker_info="$7"
  mock_compose="$8"
  workdir_override="$9"

  case_dir="$test_root/$name"
  mock_dir="$case_dir/bin"
  mkdir -p "$case_dir"
  make_common_mocks "$mock_dir"
  if [ "$include_docker" = "yes" ]; then
    make_docker_mock "$mock_dir"
  fi
  printf '%s\n' 'Linux version 6.6.0-microsoft-standard-WSL2' >"$case_dir/proc-version"

  set +e
  output="$(
    PATH="$mock_dir:/usr/bin:/bin" \
      MOCK_PID_ONE="$mock_pid_one" \
      MOCK_SERVICE_ACTIVE="$mock_service_active" \
      MOCK_DOCKER_INFO="$mock_docker_info" \
      MOCK_COMPOSE="$mock_compose" \
      WSL_CHECK_PROC_VERSION_PATH="$case_dir/proc-version" \
      WSL_CHECK_PWD_OVERRIDE="$workdir_override" \
      bash "$checker" 2>&1
  )"
  actual_exit=$?
  set -e

  if [ "$actual_exit" -eq "$expected_exit" ] &&
    printf '%s\n' "$output" | grep -Fq "$expected_text"; then
    printf 'PASS %-22s exit=%s contains=%s\n' \
      "$name" "$actual_exit" "$expected_text"
    passed=$((passed + 1))
  else
    printf 'FAIL %-22s expected_exit=%s actual_exit=%s expected_text=%s\n' \
      "$name" "$expected_exit" "$actual_exit" "$expected_text"
    printf '%s\n' "$output"
    failed=$((failed + 1))
  fi
}

set -e
run_case healthy 0 "[PASS] Compose 플러그인" \
  yes systemd yes ok yes /home/dev/projects/demo
run_case windows_mount_warning 0 "[WARN] 프로젝트를 ~/projects" \
  yes systemd yes ok yes /mnt/c/projects/demo
run_case socket_permission 1 "[FAIL] Docker daemon socket 권한이 없습니다" \
  yes systemd yes permission yes /home/dev/projects/demo
run_case systemd_inactive 2 "[FAIL] docker.service가 active가 아닙니다" \
  yes init no ok yes /home/dev/projects/demo
run_case docker_cli_missing 3 "[FAIL] Docker CLI를 찾지 못했습니다" \
  no systemd yes missing no /home/dev/projects/demo

printf 'SUMMARY passed=%s failed=%s total=%s\n' \
  "$passed" "$failed" "$((passed + failed))"

[ "$failed" -eq 0 ]
