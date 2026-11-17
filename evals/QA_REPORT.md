# Quality assurance — initial package

**Date:** 2026-11-17

**Scope:** Packaging/static verification performed in this workspace, plus arithmetic checks for synthetic examples. No claim of a live Codex/Claude/Cursor evaluation.

## Requirement-by-requirement check

| User requirement | Implemented in | Checked |
| --- | --- | --- |
| Senior-level high abstraction **and** high depth | `SKILL.md` §§ 1,3,5 | Static content review |
| Depth: deep / very-deep / automatic | `SKILL.md`, `references/profiles.md` | Metadata/selector tests |
| Focus: balanced / mechanisms / trade-offs / theory / all | `references/profiles.md` | Scenario coverage tests |
| Numeric examples and data-flow, individually or together | `references/examples.md` | Structural and arithmetic review |
| Choose a profile by default, override any subset | `SKILL.md` § 1 | Selector and scenario tests |
| Explain / critique modes | `SKILL.md` § 4, `references/critique.md` | Coverage tests |
| Ground answers in the real project | `references/evidence.md` | Safety/grounding text checks |
| Hebrew/English | `SKILL.md`, `README.he.md` | Metadata and example tests |
| Cross-agent, portable skills packaging | Agent Skills `SKILL.md` manifest | YAML parsed; folder and links verified |
| Clear public README and installation | `README.md`, `README.he.md` | Documentation tests |
| Model behavior regression scenarios | `evals/scenarios.json` | 17 cases are syntactically validated |

## Static verification results

- **11/11** local `unittest` checks passed.
- Skill YAML frontmatter parsed successfully with PyYAML (independent check); only required fields are present.
- Exactly one `SKILL.md` is present in the skill bundle; linked reference files exist and are at a single level.
- Skill instruction file is under Anthropic's recommended 500-line guideline.
- Synthetic RAG illustration: `(705 - 625) / 625 = 12.8%`; stated as approximately 13%.
- Synthetic AHE illustration: four bilinear weights sum to 1; weighted output is `132.5`.
- No application, network endpoint, API key, existing repository, or agent model was used for evaluation.

## Not yet validated

- Whether any particular installed agent **automatically** chooses the skill for each trigger prompt.
- Whether real language-model answers score highly on the 17 behavior scenarios.
- Whether runtime tools provide truthful `path:line` citations in a particular project.

These require a supported agent runtime and a real test repository. The rubric in `evals/README.md` specifies how to run an A/B evaluation rather than claiming success without measurements.
