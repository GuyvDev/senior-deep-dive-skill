"""Offline, standard-library packaging and scenario coverage checks.

This test does not execute an LLM or evaluate its behavioral compliance.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "senior-deep-dive"
SKILL = SKILL_DIR / "SKILL.md"
SCENARIOS = ROOT / "evals" / "scenarios.json"


def parse_frontmatter(text):
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise AssertionError("SKILL.md must begin with closed YAML frontmatter")
    fm = match.group(1)
    # Restrict to the two scalar fields this package intentionally uses.
    fields = {}
    for line in fm.splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise AssertionError("Malformed frontmatter line: " + line)
        fields[key.strip()] = value.strip()
    return fields, text[match.end():]


class SkillQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.body = SKILL.read_text(encoding="utf-8")
        cls.fm, cls.content = parse_frontmatter(cls.body)
        cls.cases = json.loads(SCENARIOS.read_text(encoding="utf-8"))

    def test_standard_metadata(self):
        self.assertEqual(set(self.fm), {"name", "description"})
        name = self.fm["name"]
        self.assertEqual(name, SKILL_DIR.name)
        self.assertRegex(name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(name), 64)
        self.assertTrue(40 <= len(self.fm["description"]) <= 1024)
        self.assertNotIn("<", self.fm["description"])
        self.assertNotIn(">", self.fm["description"])
        self.assertIn("Explain", self.fm["description"])
        self.assertIn("Use for", self.fm["description"])

    def test_structure_and_progressive_disclosure(self):
        self.assertTrue(self.content.lstrip().startswith("# Senior Deep Dive"))
        self.assertLess(len(self.body.splitlines()), 500)
        for section in ("Scope and invocation", "Choose a response profile", "Establish a defensible project model", "Explain the mechanism", "Explain versus critique", "Communication and final quality check"):
            self.assertIn(section, self.content)
        self.assertGreaterEqual(self.content.count("references/"), 3)

    def test_references_are_present_and_one_level_deep(self):
        refs = set(re.findall(r"\]\((references/[^)#]+\.md)\)", self.content))
        self.assertEqual(refs, {"references/profiles.md", "references/evidence.md", "references/examples.md", "references/critique.md"})
        for ref in refs:
            self.assertTrue((SKILL_DIR / ref).is_file(), ref)
            self.assertEqual(len(Path(ref).parts), 2)

    def test_independent_controls_and_overrides(self):
        for selector in ("depth", "focus", "examples", "mode", "language"):
            self.assertIn(f"`{selector}`", self.content)
        for value in ("very-deep", "deep", "mechanisms", "tradeoffs", "theory", "balanced", "all", "numeric", "flow", "both", "critique", "explain", "auto"):
            self.assertIn(f"`{value}`", self.content)
        self.assertIn("independent", self.content)
        self.assertIn("Explicit values win", self.content)
        self.assertIn("Hebrew", self.content)

    def test_safety_and_grounding(self):
        for phrase in ("read-only", "Never edit files", "Verified in project", "Inferred from evidence", "General engineering knowledge", "Unknown / not verified", "hypothetical", "line-by-line", "Do not pretend"):
            self.assertIn(phrase.lower(), self.content.lower())

    def test_numeric_and_flow_examples(self):
        content = (SKILL_DIR / "references/examples.md").read_text(encoding="utf-8")
        for part in ("RAG", "CUDA", "CDF", "50", "80 ms", "2048/4096", "Bilinear", "Hypothetical"):
            self.assertIn(part.lower(), content.lower())
        self.assertIn("->", content)
        self.assertIn("132.5", content)

    def test_eval_case_coverage(self):
        cases = self.cases
        self.assertGreaterEqual(len(cases), 15)
        self.assertEqual(len(set(c["id"] for c in cases)), len(cases))
        self.assertGreaterEqual(sum(c["should_trigger"] for c in cases), 10)
        self.assertGreaterEqual(sum(not c["should_trigger"] for c in cases), 4)
        for case in cases:
            self.assertIsInstance(case["prompt"], str)
            self.assertTrue(case["prompt"].strip())
            self.assertIsInstance(case["must"], list)
            self.assertGreaterEqual(len(case["must"]), 1)
            self.assertTrue(set(case["expected"]).issubset({"depth", "focus", "examples", "mode", "language"}))
        values = {k: {c["expected"].get(k) for c in cases} - {None} for k in ("depth", "focus", "examples", "mode", "language")}
        self.assertTrue({"deep", "very-deep"}.issubset(values["depth"]))
        self.assertTrue({"balanced", "mechanisms", "tradeoffs", "theory", "all"}.issubset(values["focus"]))
        self.assertTrue({"numeric", "flow", "both"}.issubset(values["examples"]))
        self.assertTrue({"explain", "critique"}.issubset(values["mode"]))
        self.assertTrue({"he", "en"}.issubset(values["language"]))

    def test_root_documentation(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for phrase in ("Quick start", "Controls", "Testing", "Codex", "Claude", "Cursor", "GitHub Copilot", "MIT", "Data-System-School", "architecture-skills", "poteto/how"):
            self.assertIn(phrase, readme)
        self.assertIn("python3 -m unittest", readme)
        self.assertTrue((ROOT / "LICENSE").is_file())
        self.assertTrue((ROOT / ".github/workflows/validate.yml").is_file())


if __name__ == "__main__":
    unittest.main()
