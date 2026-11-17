# Architecture critique rubric

Critique requires an accurate explanatory baseline; do not criticize a system from a guessed design. The goal is judgment under constraints, not a catalog of fashionable architectural patterns.

## Frame the decision

1. **Observed design:** grounded description, sources and trust/data boundaries.
2. **Goals and constraints:** latency SLOs, throughput, budget, team size, accuracy, reliability, privacy and operational constraints; distinguish stated vs assumed.
3. **Decision alternatives:** current approach, the simplest credible alternative, and one boundary condition under which a different approach wins.
4. **Trade-off analysis:** meaningful quantitative or comparative effects. When precise numbers are unavailable, give a measurable evaluation plan rather than guessing.
5. **Failure modes:** concrete triggering conditions, blast radius, recoverability, detection and mitigations. Distinguish verified defects from possible risks.
6. **Verdict:** conditional recommendation, confidence, and missing evidence needed to change the recommendation.

## Useful engineering lenses

| Lens | Concrete question |
| --- | --- |
| Correctness | Which invariants must always hold? What violates them? |
| Data and state | Where is truth stored, and where can it diverge? |
| Performance | What is on the critical path? What scales with input/candidate count? |
| Reliability | What happens on partial failure, retry, duplication, timeout or crash? |
| Security/privacy | Where are trust boundaries, authorization and sensitive data? |
| ML quality | Are splits, labels, evaluation metrics and deployment distribution aligned? |
| Cost/resources | What uses GPU, CPU, RAM, storage, tokens or network? |
| Complexity/maintenance | What new operational burden is justified by measurable gain? |

A short narrow question should cover only a few lenses. `focus=all` invokes all **relevant** lenses, not all rows indiscriminately.

## Confidence and severity

- **Verified issue:** reproducible or directly demonstrated by code/test/trace.
- **Potential concern:** plausible if specific stated assumption holds; spell out the assumption.
- **Design preference:** an opinion or alternative, not evidence of a bug.

Rank by likelihood *and* impact, not merely novelty. Cite evidence and suggest an experiment: load test, ablation, failure injection, profiling, calibration, data-leakage audit, or tracing as applicable. Propose changes only as recommendations; **do not implement them** without authorization.
