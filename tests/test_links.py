"""Verify local Markdown links and illustrative numeric arithmetic without dependencies."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class LinksAndMathTests(unittest.TestCase):
    def test_all_relative_markdown_links_resolve(self):
        for file in ROOT.rglob("*.md"):
            if "__pycache__" in file.parts:
                continue
            data = file.read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^)]+)\)", data):
                if target.startswith(("https://", "http://", "mailto:", "#")):
                    continue
                path = (file.parent / target.split("#", 1)[0]).resolve()
                self.assertTrue(path.is_file(), f"Broken link in {file.relative_to(ROOT)}: {target}")

    def test_rag_math(self):
        retrieval, rerank, generate = 25, 80, 600
        with_rerank = retrieval + rerank + generate
        without = retrieval + generate
        self.assertEqual((with_rerank, without), (705, 625))
        self.assertAlmostEqual((with_rerank - without) / without * 100, 12.8)

    def test_ahe_math(self):
        x, y = .25, .5
        vals = (120, 130, 140, 150)
        weights = ((1-x)*(1-y), x*(1-y), (1-x)*y, x*y)
        self.assertAlmostEqual(sum(weights), 1.0)
        self.assertAlmostEqual(sum(w*v for w,v in zip(weights, vals)), 132.5)
        self.assertEqual(2048/4096, 0.5)


if __name__ == "__main__":
    unittest.main()
