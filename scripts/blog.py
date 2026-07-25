#!/usr/bin/env python3
"""dev.log 글 묶음을 만들고, 검사하고, 티스토리 HTML로 변환한다."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from md2tistory import split_frontmatter


ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "posts"
TEMPLATE_DIR = ROOT / "templates" / "post"

TAXONOMY = {
    "Log": {"AI 개념 · 실전", "AI 모델 · 비교", "개발 · 디지털"},
    "Trends": {"AI 뉴스 · 테크 · 산업", "경제 · 금융", "사회 · 문화"},
    "Health": {"질환 · 의약품", "영양 · 식단"},
    "Reflections": {"말씀 묵상", "신앙 질문", "성경 읽기", "성경 인물"},
}
STATUSES = {
    "planning",
    "researching",
    "drafting",
    "reviewing",
    "ready",
    "published",
}
FINAL_STATUSES = {"ready", "published"}
POST_DIR_RE = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)$"
)
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)


@dataclass(frozen=True)
class Diagnostic:
    level: str
    path: Path
    message: str


def relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def scalar(meta: dict, key: str) -> str:
    value = meta.get(key, "")
    return value if isinstance(value, str) else ""


def list_value(meta: dict, key: str) -> list[str]:
    value = meta.get(key, [])
    if isinstance(value, list):
        return [str(item) for item in value]
    if isinstance(value, str) and value:
        return [value]
    return []


def clean_heading(text: str) -> str:
    text = re.sub(r"[`*_~]", "", text).strip()
    return re.sub(r"[\s.!?…,:;)\]』」]+$", "", text)


def ends_in_da(text: str) -> bool:
    return clean_heading(text).endswith("다")


def has_raster_signature(path: Path) -> bool:
    with path.open("rb") as image:
        header = image.read(12)
    suffix = path.suffix.lower()
    if suffix == ".png":
        return header.startswith(b"\x89PNG\r\n\x1a\n")
    if suffix in {".jpg", ".jpeg"}:
        return header.startswith(b"\xff\xd8\xff")
    if suffix == ".webp":
        return header.startswith(b"RIFF") and header[8:12] == b"WEBP"
    return False


def resolve_post_dir(target: str | Path) -> Path:
    path = Path(target)
    if not path.is_absolute():
        path = (ROOT / path).resolve()
    if path.is_file():
        if path.name != "article.md":
            raise ValueError("article.md 또는 글 디렉터리를 지정하세요.")
        return path.parent
    return path


def post_directories() -> list[Path]:
    if not POSTS_DIR.exists():
        return []
    return sorted(
        path
        for path in POSTS_DIR.iterdir()
        if path.is_dir() and POST_DIR_RE.fullmatch(path.name)
    )


def add(
    diagnostics: list[Diagnostic],
    level: str,
    path: Path,
    message: str,
) -> None:
    diagnostics.append(Diagnostic(level, path, message))


def check_post(post_dir: Path) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    article = post_dir / "article.md"
    match = POST_DIR_RE.fullmatch(post_dir.name)

    if not match:
        add(
            diagnostics,
            "ERROR",
            post_dir,
            "디렉터리명은 YYYY-MM-DD-영문-slug 형식이어야 합니다.",
        )

    for name in ("brief.md", "evidence.md", "article.md", "audit.md"):
        path = post_dir / name
        if not path.is_file():
            add(diagnostics, "ERROR", path, "필수 파일이 없습니다.")
    for name in ("assets", "artifacts"):
        path = post_dir / name
        if not path.is_dir():
            add(diagnostics, "ERROR", path, "필수 디렉터리가 없습니다.")

    if not article.is_file():
        return diagnostics

    raw = article.read_text(encoding="utf-8")
    meta, body = split_frontmatter(raw)
    required = (
        "title",
        "slug",
        "date",
        "category",
        "subcategory",
        "status",
        "tags",
        "summary",
        "hero_image",
        "published_url",
        "sources",
    )
    for key in required:
        if key not in meta:
            add(
                diagnostics,
                "ERROR",
                article,
                f"프론트매터에 `{key}` 키가 없습니다.",
            )

    title = scalar(meta, "title")
    slug = scalar(meta, "slug")
    date = scalar(meta, "date")
    category = scalar(meta, "category")
    subcategory = scalar(meta, "subcategory")
    status = scalar(meta, "status")
    summary = scalar(meta, "summary")
    hero_image = scalar(meta, "hero_image")
    published_url = scalar(meta, "published_url")
    tags = list_value(meta, "tags")
    sources = list_value(meta, "sources")

    if not title:
        add(diagnostics, "ERROR", article, "제목이 비어 있습니다.")
    elif ends_in_da(title):
        add(diagnostics, "ERROR", article, "제목이 `~다`로 끝납니다.")

    if not SLUG_RE.fullmatch(slug):
        add(
            diagnostics,
            "ERROR",
            article,
            "slug는 영문 소문자, 숫자, 하이픈만 사용할 수 있습니다.",
        )

    try:
        dt.date.fromisoformat(date)
    except ValueError:
        add(diagnostics, "ERROR", article, "date는 YYYY-MM-DD 형식이어야 합니다.")

    if match:
        if date and match.group("date") != date:
            add(
                diagnostics,
                "ERROR",
                article,
                "프론트매터 date가 디렉터리 날짜와 다릅니다.",
            )
        if slug and match.group("slug") != slug:
            add(
                diagnostics,
                "ERROR",
                article,
                "프론트매터 slug가 디렉터리 slug와 다릅니다.",
            )

    if category not in TAXONOMY:
        add(diagnostics, "ERROR", article, "현재 상위 카테고리가 아닙니다.")
    elif subcategory not in TAXONOMY[category]:
        choices = ", ".join(sorted(TAXONOMY[category]))
        add(
            diagnostics,
            "ERROR",
            article,
            f"`{category}`의 현재 하위 카테고리가 아닙니다: {choices}",
        )

    if status not in STATUSES:
        add(
            diagnostics,
            "ERROR",
            article,
            "status가 허용된 작업 단계가 아닙니다.",
        )

    stripped_body = body.lstrip()
    if not stripped_body.startswith("안녕하세요. dev.log입니다."):
        add(
            diagnostics,
            "ERROR",
            article,
            "본문이 표준 인사 `안녕하세요. dev.log입니다.`로 시작하지 않습니다.",
        )

    headings = HEADING_RE.findall(body)
    for hashes, heading in headings:
        if len(hashes) != 3:
            add(
                diagnostics,
                "ERROR",
                article,
                f"본문 소제목은 `###`를 사용하세요: {heading}",
            )
        if ends_in_da(heading):
            add(
                diagnostics,
                "ERROR",
                article,
                f"소제목이 `~다`로 끝납니다: {heading}",
            )

    if "—" in body:
        add(diagnostics, "ERROR", article, "em dash(`—`) 대신 하이픈을 사용하세요.")

    if re.search(r"<!--.*?-->", body, re.DOTALL):
        level = "ERROR" if status in FINAL_STATUSES else "WARN"
        add(diagnostics, level, article, "본문에 편집용 HTML 주석이 남아 있습니다.")

    has_reference_appendix = re.search(
        r"^###\s+(참고문헌|참고 자료|출처|References)\s*$",
        body,
        re.MULTILINE,
    )
    allows_reference_appendix = (
        category == "Log" and subcategory == "AI 모델 · 비교"
    )
    if has_reference_appendix and not allows_reference_appendix:
        add(
            diagnostics,
            "WARN",
            article,
            "분리된 참고문헌보다 관련 문장에 출처와 한계를 붙이세요.",
        )
    has_required_reference_tail = bool(
        headings and clean_heading(headings[-1][1]) == "참고 자료"
    )
    if allows_reference_appendix and not has_required_reference_tail:
        level = "ERROR" if status in FINAL_STATUSES else "WARN"
        add(
            diagnostics,
            level,
            article,
            "AI 모델 · 비교 글의 마지막 절에 `### 참고 자료`를 추가하세요.",
        )

    if "이 글은 일반적인 정보 정리이며" in body:
        add(
            diagnostics,
            "WARN",
            article,
            "관성적인 면책 문구보다 구체적인 위험과 상담 기준을 본문에 적으세요.",
        )

    anti_patterns = {
        "라고 할 수 있습니다": "불필요한 완곡 표현",
        "검토를 진행합니다": "명사화 표현",
        "개선이 이루어집니다": "좀비 명사",
        "보여집니다": "이중 피동",
        "되어집니다": "이중 피동",
    }
    for pattern, label in anti_patterns.items():
        if pattern in body:
            add(
                diagnostics,
                "WARN",
                article,
                f"{label}을 직접적인 한국어로 고치세요: `{pattern}`",
            )

    if status in FINAL_STATUSES:
        if not summary:
            add(diagnostics, "ERROR", article, "ready 상태에는 summary가 필요합니다.")
        if not tags:
            add(diagnostics, "ERROR", article, "ready 상태에는 태그가 필요합니다.")
        if category != "Reflections" and not sources:
            add(
                diagnostics,
                "ERROR",
                article,
                "ready 상태의 수익형 글에는 사용한 sources가 필요합니다.",
            )
        if not hero_image:
            add(diagnostics, "ERROR", article, "ready 상태에는 hero_image가 필요합니다.")
        else:
            hero_path = (post_dir / hero_image).resolve()
            try:
                hero_path.relative_to(post_dir.resolve())
            except ValueError:
                add(
                    diagnostics,
                    "ERROR",
                    article,
                    "hero_image는 글 디렉터리 안의 파일이어야 합니다.",
                )
            else:
                if not hero_path.is_file():
                    add(
                        diagnostics,
                        "ERROR",
                        hero_path,
                        "최종 대표 이미지 파일이 없습니다.",
                    )
                elif hero_path.suffix.lower() not in {
                    ".png",
                    ".jpg",
                    ".jpeg",
                    ".webp",
                }:
                    add(
                        diagnostics,
                        "ERROR",
                        hero_path,
                        "대표 이미지는 PNG, JPEG 또는 WebP 래스터 파일이어야 합니다.",
                    )
                elif not has_raster_signature(hero_path):
                    add(
                        diagnostics,
                        "ERROR",
                        hero_path,
                        "확장자와 실제 대표 이미지 형식이 일치하지 않습니다.",
                    )

        for name in ("brief.md", "evidence.md", "audit.md"):
            path = post_dir / name
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            if "<!--" in text:
                add(
                    diagnostics,
                    "ERROR",
                    path,
                    "ready 상태인데 템플릿 주석이 남아 있습니다.",
                )
            if name == "evidence.md":
                unresolved_row = re.search(
                    r"^\|(?:[^|\n]*\|){3}\s*(미확인|원문 필요)\s*\|",
                    text,
                    re.MULTILINE,
                )
                unchecked_item = re.search(r"^- \[ \]", text, re.MULTILINE)
                if unresolved_row or unchecked_item:
                    add(
                        diagnostics,
                        "ERROR",
                        path,
                        "ready 상태인데 미확인 근거가 남아 있습니다.",
                    )
            if name == "audit.md" and re.search(r"^- \[ \]", text, re.MULTILINE):
                add(
                    diagnostics,
                    "ERROR",
                    path,
                    "ready 상태인데 최종 감사의 미확인 항목이 남아 있습니다.",
                )

    if status == "published" and not re.match(r"^https?://", published_url):
        add(
            diagnostics,
            "ERROR",
            article,
            "published 상태에는 실제 published_url이 필요합니다.",
        )

    return diagnostics


def print_diagnostics(diagnostics: list[Diagnostic]) -> tuple[int, int]:
    errors = sum(item.level == "ERROR" for item in diagnostics)
    warnings = sum(item.level == "WARN" for item in diagnostics)
    for item in diagnostics:
        print(f"[{item.level}] {relative(item.path)}: {item.message}")
    return errors, warnings


def cmd_new(args: argparse.Namespace) -> int:
    if not SLUG_RE.fullmatch(args.slug):
        print("오류: slug는 영문 소문자, 숫자, 하이픈만 사용할 수 있습니다.")
        return 2
    if args.category not in TAXONOMY:
        print("오류: 현재 상위 카테고리를 지정하세요.")
        return 2
    if args.subcategory not in TAXONOMY[args.category]:
        choices = ", ".join(sorted(TAXONOMY[args.category]))
        print(f"오류: {args.category} 하위 카테고리는 {choices} 중 하나입니다.")
        return 2
    try:
        date = dt.date.fromisoformat(args.date)
    except ValueError:
        print("오류: --date는 YYYY-MM-DD 형식이어야 합니다.")
        return 2

    post_dir = POSTS_DIR / f"{date.isoformat()}-{args.slug}"
    if post_dir.exists():
        print(f"오류: 이미 존재합니다: {relative(post_dir)}")
        return 2

    substitutions = {
        "title": args.title,
        "slug": args.slug,
        "date": date.isoformat(),
        "category": args.category,
        "subcategory": args.subcategory,
        "post_dir": relative(post_dir),
    }
    post_dir.mkdir(parents=True)
    for source in TEMPLATE_DIR.rglob("*"):
        destination = post_dir / source.relative_to(TEMPLATE_DIR)
        if source.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix == ".md":
            text = source.read_text(encoding="utf-8")
            destination.write_text(
                text.format(**substitutions),
                encoding="utf-8",
            )
        else:
            shutil.copyfile(source, destination)

    print(f"생성: {relative(post_dir)}")
    print("다음: brief.md에서 독자, 핵심 메시지, first-party value를 먼저 정하세요.")
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    if args.all:
        targets = post_directories()
        if not targets:
            print("검사할 현재 글이 없습니다.")
            return 0
    else:
        try:
            targets = [resolve_post_dir(args.target)]
        except ValueError as exc:
            print(f"오류: {exc}")
            return 2

    diagnostics: list[Diagnostic] = []
    for target in targets:
        diagnostics.extend(check_post(target))

    errors, warnings = print_diagnostics(diagnostics)
    print(
        f"검사 완료: {len(targets)}개 글, 오류 {errors}개, 경고 {warnings}개"
    )
    if errors or (args.strict and warnings):
        return 1
    return 0


def cmd_render(args: argparse.Namespace) -> int:
    try:
        post_dir = resolve_post_dir(args.target)
    except ValueError as exc:
        print(f"오류: {exc}")
        return 2

    article = post_dir / "article.md"
    if not article.is_file():
        print(f"오류: article.md가 없습니다: {relative(article)}")
        return 2

    meta, _ = split_frontmatter(article.read_text(encoding="utf-8"))
    status = scalar(meta, "status")
    if status not in FINAL_STATUSES:
        print("오류: ready 또는 published 상태의 글만 렌더링할 수 있습니다.")
        return 1

    diagnostics = check_post(post_dir)
    errors, warnings = print_diagnostics(diagnostics)
    if errors:
        print(f"렌더링 중단: 오류 {errors}개, 경고 {warnings}개")
        return 1

    slug = scalar(meta, "slug")
    output = ROOT / "dist" / f"{slug}.html"
    command = [
        sys.executable,
        str(ROOT / "scripts" / "md2tistory.py"),
        str(article),
        "--output",
        str(output),
    ]
    result = subprocess.run(command, cwd=ROOT, check=False)
    return result.returncode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="dev.log 글 작업공간 도구")
    subparsers = parser.add_subparsers(dest="command", required=True)

    new = subparsers.add_parser("new", help="새 글 작업 묶음을 만듭니다.")
    new.add_argument("slug")
    new.add_argument("--title", required=True)
    new.add_argument("--category", required=True, choices=sorted(TAXONOMY))
    new.add_argument("--subcategory", required=True)
    new.add_argument("--date", default=dt.date.today().isoformat())
    new.set_defaults(func=cmd_new)

    check = subparsers.add_parser("check", help="글 묶음의 자동 검사 항목을 확인합니다.")
    group = check.add_mutually_exclusive_group(required=True)
    group.add_argument("target", nargs="?", help="글 디렉터리 또는 article.md")
    group.add_argument("--all", action="store_true", help="posts/의 모든 글")
    check.add_argument(
        "--strict",
        action="store_true",
        help="경고가 있어도 실패 코드로 종료합니다.",
    )
    check.set_defaults(func=cmd_check)

    render = subparsers.add_parser("render", help="ready 글을 티스토리 HTML로 만듭니다.")
    render.add_argument("target", help="글 디렉터리 또는 article.md")
    render.set_defaults(func=cmd_render)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
