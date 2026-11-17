# Profile routing and override semantics

The five selectors are **orthogonal**; this avoids conflating “deep” with “low level” or “theory” with “verbose”. Use the most recent explicit request as the source of truth for each selector. Unspecified selectors remain `auto` for this question, not inherited silently from unrelated previous tasks. An established user preference may supply a default where consistent.

## Selectors

### Depth
- `deep`: rigorous explanation of purpose, core mechanism, boundaries, a worked example, 2–3 meaningful trade-offs, a failure mode, and validation. No line-by-line implementation.
- `very-deep`: retain the same abstraction level; add internal invariants, more causal steps, justified quantitative/analytical estimates, comparison under changed assumptions, more nuanced failure analysis, and experimental validation. Do not increase detail by listing functions or syntax.
- `auto`: typically deep; prefer very-deep for multilayer interactions, major architectural evaluation, mathematical derivations, or an explicit request for thorough/rigorous treatment. Do not use very-deep merely because the repository is large.

### Engineering focus
- `balanced`: mechanism + project placement + choice + caveat.
- `mechanisms` (`flow`, `dataflow`, `זרימה`, `מנגנונים`): trace trigger, processing stages, state, trust boundaries, representations, data/control movement and outputs.
- `tradeoffs` (`decisions`, `alternatives`, `החלטות`, `חלופות`, `שיקולים`): evaluate competing designs using real constraints and measurable consequences.
- `theory` (`math`, `מתמטיקה`, `תיאוריה`): derive foundations, assumptions, invariants, equations, complexity, and conceptual relations as needed.
- `all` (`כולם`, `הכל`): balance mechanisms, decisions, and theory where each is germane; avoid padding or repeating the same fact in three places.
- `auto`: choose mechanisms for “what happens from X to Y”, tradeoffs for “why this instead of that”, theory for “prove / derive / mathematically”, balanced for general “explain how this works”.

### Examples
- `numeric`: at least one genuinely useful numerical walkthrough with units, explicit assumed numbers, and calculations; if numerical illustration is misleading, say why and use a conceptual quantitative bound instead.
- `flow`: a stepwise trace with input, transformations, boundaries, and output; diagram if it helps.
- `both`: numerical example **and** an end-to-end data/control-flow example. They can be the *same* example traced through numbered stages to avoid duplication.
- `auto`: use both when helpful; otherwise use the more illuminating one. Do not fabricate project benchmarks.

### Mode
- `explain`: characterize current behavior, reasoned rationale, alternatives without presuming defects.
- `critique`: explain first, challenge assumptions and relevant risks using a confidence-labeled critique.
- `auto`: default explain; user requests “critique”, “review the design”, “what's wrong”, “is this robust”, “is this decision justified” select critique.

### Language
- `auto`: mirror user, retaining standard technical English terms where clearer; `he`: Hebrew RTL with English terms and LTR math/code; `en`: English.

## Override examples

| User message | Resolved settings |
| --- | --- |
| `Explain the cache invalidation flow` | `depth=deep focus=mechanisms examples=both mode=explain language=en` (auto selection, subject to useful evidence) |
| `Explain deeply the trade-offs of cross-encoders` | `depth=deep focus=tradeoffs examples=both mode=explain language=en` |
| `depth=very-deep focus=theory examples=numeric: derive attention scaling` | explicit depth/focus/examples; `mode=explain`, language inferred |
| `תסביר לעומק מאוד איך הבקשה עוברת במערכת, עם תרשים` | `depth=very-deep focus=mechanisms examples=flow language=he` |
| `עומק=עמוק, דגש=החלטות, דוגמאות=מספרים וזרימה; האם הארכיטקטורה טובה?` | `depth=deep focus=tradeoffs examples=both mode=critique language=he` |
| `focus=all; keep the answer short` | all relevant lenses but concise; explicit brevity wins |

## Edge conditions

- Do not show the profile table or ask a selector questionnaire in the answer; respond naturally.
- If user sets only `examples=flow`, auto-select depth and focus independently.
- If a user says “no math” and `focus=theory`, emphasize rigorous verbal intuition and assumptions instead of equations; their direct restriction prevails.
- If a question asks for code despite activating this skill, follow the explicit code request rather than insisting on zero code.
- If no repo is present and the question is project-specific, note that architecture details cannot be verified. Give sound general mechanisms, not fabricated repo details.
