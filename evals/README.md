# Evaluation plan

A static validator cannot establish that a language model actually follows a Skill. Use **both** automated packaging checks and behavior tests in an agent that can read a real repository.

## Running static checks

```bash
python3 -m unittest discover -s tests -v
```

The tests verify YAML/frontmatter, selectors, reference links, presence and coverage of 17 trigger/behavior scenarios, safe read-only boundaries, documentation links, and that bundled examples contain numeric and flow cases. They do **not** execute Claude, Codex, Cursor or any other language model.

## Behavioral evaluation (manual or agent-run)

1. Install the skill in a test agent. Select a small known project; record its current commit.
2. Run the prompts from `scenarios.json` with the skill **enabled**, then a baseline with it **disabled**. Keep the same model, question, source access and configuration. For project-specific prompts, provide a tiny fixture repo with a known architecture and deliberately stale README.
3. Score each applicable positive scenario, 0–2 per dimension:
   - **Mechanistic clarity:** an actual cause-effect explanation, not labels.
   - **Correct abstraction:** no irrelevant syntax or code-by-code commentary.
   - **Grounding:** repo claims verified; missing evidence acknowledged.
   - **Profiles:** selectors and explicit length/language restrictions respected.
   - **Numbers and flow:** intermediate data-flow and numerical assumptions correct when required.
   - **Trade-offs / critique:** conditional, testable engineering judgment.
4. Negative scenarios should **not** invoke the skill automatically. Record false-positive/false-negative triggers separately.
5. Check for policy violations: fabricated benchmarks, running project code, changing files, pretending to read code, leaking secrets.
6. Compare qualitative failures and revise the smallest responsible instruction. Repeat with different models when available.

## Passing thresholds (recommended, not measured here)

- At least 10/12 points on each applicable positive scenario.
- No fabricated project measurements or citations.
- Zero side-effectful actions without separate authorization.
- Correct override resolution on all explicit-selector scenarios.
- No false triggering on the 4 negative scenarios.

The sample responses in the references are teaching examples, not measured agent outputs.
