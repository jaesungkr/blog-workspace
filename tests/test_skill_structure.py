import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"

STANDARD_SPECIALISTS = {
    "dev-log-writing",
    "dev-log-prose-polish",
    "dev-log-hero-image",
    "dev-log-infographic",
    "dev-log-article-validation",
    "dev-log-hero-validation",
    "dev-log-infographic-validation",
}
ORCHESTRATORS = {
    "dev-log-workspace",
    "dev-log-rich-post-workspace",
}
EXPECTED_SKILLS = STANDARD_SPECIALISTS | ORCHESTRATORS


class SkillStructureTests(unittest.TestCase):
    def test_every_stage_has_skill_and_ui_metadata(self):
        for name in EXPECTED_SKILLS:
            with self.subTest(skill=name):
                skill = SKILLS / name / "SKILL.md"
                metadata = SKILLS / name / "agents" / "openai.yaml"
                self.assertTrue(skill.is_file())
                self.assertTrue(metadata.is_file())

                text = skill.read_text(encoding="utf-8")
                self.assertRegex(text, rf"(?m)^name: {re.escape(name)}$")
                self.assertNotIn("description: [TODO:", text)

                ui = metadata.read_text(encoding="utf-8")
                self.assertIn(f"${name}", ui)
                self.assertIn("allow_implicit_invocation: true", ui)

    def test_standard_orchestrator_loads_every_standard_specialist(self):
        orchestrator = (
            SKILLS / "dev-log-workspace" / "SKILL.md"
        ).read_text(encoding="utf-8")

        for name in STANDARD_SPECIALISTS:
            with self.subTest(skill=name):
                self.assertIn(f"../{name}/SKILL.md", orchestrator)

        self.assertIn("Stage skills do not commit or push", orchestrator)
        self.assertIn("This orchestrator owns Git delivery", orchestrator)
        self.assertIn("../dev-log-rich-post-workspace/SKILL.md", orchestrator)

    def test_rich_orchestrator_owns_media_render_and_git_delivery(self):
        rich_skill_dir = SKILLS / "dev-log-rich-post-workspace"
        orchestrator = (rich_skill_dir / "SKILL.md").read_text(encoding="utf-8")

        for name in {
            "dev-log-writing",
            "dev-log-prose-polish",
            "dev-log-article-validation",
        }:
            with self.subTest(skill=name):
                self.assertIn(f"../{name}/SKILL.md", orchestrator)

        for relative in {
            "references/rich-post-format.md",
            "references/reader-first-editorial.md",
            "references/media-manifest.md",
            "references/remote-media.md",
            "references/responsive-qa.md",
            "references/tistory-upload.md",
            "scripts/capture_rich_qa.py",
            "scripts/check_rich_post.py",
            "scripts/record_rich_qa.py",
            "scripts/record_rich_final_validation.py",
            "scripts/remote_media.py",
            "scripts/render_rich_post.py",
            "scripts/tistory_media_map.py",
            "assets/rich-post.css",
            "assets/capture-plan-template.md",
            "assets/media-template.json",
            "assets/qa-template.json",
            "assets/independent-qa-template.json",
        }:
            with self.subTest(resource=relative):
                self.assertTrue((rich_skill_dir / relative).is_file())

        self.assertIn("format: rich-post", orchestrator)
        self.assertIn("full local preview", orchestrator)
        self.assertIn("Tistory fragment", orchestrator)
        self.assertIn("This orchestrator owns Git delivery", orchestrator)
        self.assertIn("--preview-theme dark", orchestrator)

        rich_css = (rich_skill_dir / "assets" / "rich-post.css").read_text(
            encoding="utf-8"
        )
        self.assertIn("--rich-surface", rich_css)
        self.assertIn(".dark .devlog-rich", rich_css)
        self.assertIn("a[style]", rich_css)
        self.assertIn("code[style]", rich_css)
        self.assertIn("pre[style]", rich_css)

        reader_gate = (
            rich_skill_dir / "references" / "reader-first-editorial.md"
        ).read_text(encoding="utf-8")
        responsive_qa = (
            rich_skill_dir / "references" / "responsive-qa.md"
        ).read_text(encoding="utf-8")
        rich_format = (
            rich_skill_dir / "references" / "rich-post-format.md"
        ).read_text(encoding="utf-8")

        self.assertIn("plain-language identity", reader_gate)
        self.assertIn("Overload test", reader_gate)
        self.assertIn("target value | target rank | row leader", reader_gate)
        self.assertIn("missing entitlement", reader_gate)
        self.assertIn("Label old passes as historical", reader_gate)
        self.assertIn("Focused evidence for changed components", responsive_qa)
        self.assertIn("scrollLeft = 0", responsive_qa)
        self.assertIn("overflow-x: auto", responsive_qa)
        self.assertIn("estimated reading time", rich_format)

    def test_orchestrators_deliver_raw_tistory_fragment_txt(self):
        for name in ORCHESTRATORS:
            with self.subTest(skill=name):
                orchestrator = (SKILLS / name / "SKILL.md").read_text(
                    encoding="utf-8"
                )
                normalized = " ".join(orchestrator.split())
                self.assertIn("<slug>-tistory-fragment.txt", orchestrator)
                self.assertIn("byte-for-byte", orchestrator)
                self.assertRegex(normalized, r"primary (?:final )?link")

        rich_format = (
            SKILLS
            / "dev-log-rich-post-workspace"
            / "references"
            / "rich-post-format.md"
        ).read_text(encoding="utf-8")
        self.assertIn("<slug>-tistory-fragment.txt", rich_format)
        self.assertIn("raw HTML only", rich_format)

    def test_creation_and_validation_roles_stay_separate(self):
        hero_creation = (
            SKILLS / "dev-log-hero-image" / "SKILL.md"
        ).read_text(encoding="utf-8")
        hero_validation = (
            SKILLS / "dev-log-hero-validation" / "SKILL.md"
        ).read_text(encoding="utf-8")
        infographic_creation = (
            SKILLS / "dev-log-infographic" / "SKILL.md"
        ).read_text(encoding="utf-8")
        infographic_validation = (
            SKILLS / "dev-log-infographic-validation" / "SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn("dev-log-hero-validation", hero_creation)
        self.assertIn("major enterprise", hero_validation)
        self.assertIn("subject-swap", hero_validation)
        self.assertIn("full-size and thumbnail", hero_validation)

        self.assertIn("dev-log-infographic-validation", infographic_creation)
        self.assertIn("untouched full-resolution candidate", infographic_creation)
        self.assertIn("Do not resize, re-encode, save, or commit", infographic_creation)
        self.assertIn("same untouched raster", infographic_validation)
        self.assertIn("Do not create, save, re-encode, or commit", infographic_validation)
        self.assertIn("Enlarged crops", infographic_validation)
        self.assertIn("painted bounds", infographic_validation)

    def test_prose_polish_preserves_evidence_and_hands_off(self):
        prose_polish = (
            SKILLS / "dev-log-prose-polish" / "SKILL.md"
        ).read_text(encoding="utf-8")
        prose_reference = (
            SKILLS
            / "dev-log-prose-polish"
            / "references"
            / "human-prose-benchmarks.md"
        )
        analyzer = (
            SKILLS
            / "dev-log-prose-polish"
            / "scripts"
            / "analyze_prose.py"
        )

        self.assertTrue(prose_reference.is_file())
        self.assertTrue(analyzer.is_file())
        self.assertIn("subject-substitution test", prose_polish)
        self.assertIn("Never add an anecdote", prose_polish)
        self.assertIn("status: reviewing", prose_polish)
        self.assertIn("dev-log-article-validation", prose_polish)
        self.assertIn("target_bundle", prose_polish)
        self.assertIn("Do not count `target_bundle` twice", prose_polish)
        self.assertIn("previously `ready`", prose_polish)
        self.assertIn("already `published`", prose_polish)
        self.assertIn("same non-empty `subcategory`", prose_polish)
        self.assertIn("return the bundle to\n`dev-log-writing`", prose_polish)
        self.assertIn("commit, or push", prose_polish)
        self.assertIn("scan-only clarity test", prose_polish)
        self.assertIn("Spell out what a fraction counts", prose_polish)
        self.assertIn("identify what invalidated it", prose_polish)
        self.assertIn("qualitative or based\n  on actual query-volume data", prose_polish)
        self.assertIn("never promise maximum traffic", prose_polish)

        audit_template = (ROOT / "templates" / "post" / "audit.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("정성\n  판단인지 실제 검색량 자료인지", audit_template)
        self.assertIn("본문 없이도 대상과 설명·비교·측정·변화", audit_template)
        self.assertIn("수치와 폐기한 실험의 의미", audit_template)

        orchestrator = (
            SKILLS / "dev-log-workspace" / "SKILL.md"
        ).read_text(encoding="utf-8")
        writing_position = orchestrator.index("1. `dev-log-writing`")
        polish_position = orchestrator.index("2. `dev-log-prose-polish`")
        validation_position = orchestrator.index(
            "3. `dev-log-article-validation`"
        )
        self.assertLess(writing_position, polish_position)
        self.assertLess(polish_position, validation_position)
        self.assertIn(
            "Rerun `dev-log-prose-polish` before article validation",
            orchestrator,
        )

        audit_template = (ROOT / "templates" / "post" / "audit.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("비교 표본(슬러그·상태)", audit_template)
        self.assertIn("대체 기준", audit_template)

    def test_link_script_discovers_all_dev_log_skills(self):
        script = (ROOT / "scripts" / "link_codex_skill.sh").read_text(
            encoding="utf-8"
        )

        self.assertIn('"$skill_sources"/dev-log-*', script)
        self.assertIn("for skill_source in", script)
        self.assertNotIn(
            'skill_source="$repository_root/.agents/skills/dev-log-workspace"',
            script,
        )


if __name__ == "__main__":
    unittest.main()
