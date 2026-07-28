#!/usr/bin/env bash
set -u

failures=0
proc_version_path="${WSL_CHECK_PROC_VERSION_PATH:-/proc/version}"
workdir="${WSL_CHECK_PWD_OVERRIDE:-$PWD}"

pass() {
  printf '[PASS] %s\n' "$1"
}

warn() {
  printf '[WARN] %s\n' "$1"
}

fail() {
  printf '[FAIL] %s\n' "$1"
  failures=$((failures + 1))
}

if grep -qi microsoft "$proc_version_path" 2>/dev/null; then
  pass "WSL 환경"
else
  fail "WSL 환경을 확인하지 못했습니다"
fi

pid_one="$(ps -p 1 -o comm= 2>/dev/null | tr -d '[:space:]')"
if [ "$pid_one" = "systemd" ]; then
  pass "PID 1이 systemd"
else
  fail "PID 1이 systemd가 아닙니다: ${pid_one:-unknown}"
fi

if command -v docker >/dev/null 2>&1; then
  pass "Docker CLI 설치"
else
  fail "Docker CLI를 찾지 못했습니다"
fi

if command -v systemctl >/dev/null 2>&1 &&
  systemctl is-active --quiet docker 2>/dev/null; then
  pass "docker.service 실행"
else
  fail "docker.service가 active가 아닙니다"
fi

docker_info_error=""
if command -v docker >/dev/null 2>&1; then
  docker_info_error="$(docker info 2>&1 >/dev/null)" || true
fi

if command -v docker >/dev/null 2>&1 && docker info >/dev/null 2>&1; then
  pass "현재 사용자의 daemon 접근"
elif printf '%s' "$docker_info_error" | grep -qi 'permission denied'; then
  fail "Docker daemon socket 권한이 없습니다"
else
  fail "Docker daemon에 연결하지 못했습니다"
fi

if command -v docker >/dev/null 2>&1 &&
  docker compose version >/dev/null 2>&1; then
  pass "Compose 플러그인"
else
  fail "Compose 플러그인을 확인하지 못했습니다"
fi

case "$workdir" in
  /mnt/*)
    warn "프로젝트를 ~/projects 아래로 옮기는 편이 좋습니다: $workdir"
    ;;
  *)
    pass "Linux 파일시스템의 작업 경로"
    ;;
esac

exit "$failures"
