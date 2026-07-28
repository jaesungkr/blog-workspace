import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"

EXPECTED_SKILLS = {
    "dev-log-workspace",
    "dev-log-writing",
    "dev-log-hero-image",
    "dev-log-infographic",
    "dev-log-article-validation",
    "dev-log-hero-validation",
    "dev-log-infographic-validation",
}


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

    def test_orchestrator_loads_every_specialist(self):
        orchestrator = (
            SKILLS / "dev-log-workspace" / "SKILL.md"
        ).read_text(encoding="utf-8")

        for name in EXPECTED_SKILLS - {"dev-log-workspace"}:
            with self.subTest(skill=name):
                self.assertIn(f"../{name}/SKILL.md", orchestrator)

        self.assertIn("Stage skills do not commit or push", orchestrator)
        self.assertIn("This orchestrator owns Git delivery", orchestrator)

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
