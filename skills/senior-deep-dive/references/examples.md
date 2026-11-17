# Worked examples: numbers plus information flow

Numbers and flows are ways to expose mechanisms, not decoration. Prefer one **combined worked example** with actual stages and intermediate values. Always label assumed figures as hypothetical. Never present them as measured results from the project.

## Example A: RAG retrieval and reranking (hypothetical)

**Question:** Why not send the top 50 vector results to the LLM directly?

**Purpose:** Retrieval trades speed for candidate coverage, while reranking evaluates a query/document pair more precisely before context construction. The reranker cannot recover relevant content omitted by retrieval.

```text
User question
    | query embedding
    v
Vector index (top 50 candidate chunks)
    | 50 query-chunk pairs
    v
Reranker (score each pair)
    | top 5 chunks, original sources retained
    v
Prompt assembly -> LLM -> Answer + citations
```

Hypothetical figures: a retrieval stage takes 25 ms; reranking 50 pairs takes 80 ms; generation takes 600 ms. Ignoring queuing/network, total is ~705 ms versus ~625 ms without reranking — about 13% slower in this *illustrative* example. The 80 ms is not a universally valid benchmark: hardware, batch size, model and sequence lengths change it. Show **Recall@50** to evaluate candidate coverage, **nDCG@5** or a task-grounded relevance measure for ordering, and end-to-end answer quality/latency to decide if the 80 ms earns its keep. A system with insufficient top-50 recall needs a better retriever or wider candidate set; reranking alone cannot fix missing evidence.

If the real project contains measured timings, substitute sourced values or explicitly contrast them with this illustration.

## Example B: CUDA GPU AHE pipeline (hypothetical)

**Question:** Why are the tile histograms, CDFs and interpolation separate conceptual stages?

```text
Input image (1024 x 1024, 8-bit)
    | partition into 16 x 16 tiles of 64 x 64 pixels
    v
Per-tile histogram (256 intensity bins)
    | prefix sum -> local CDF
    v
Per-tile intensity mapping LUT
    | for each pixel: sample up to four neighboring tile LUTs
    v
Spatial bilinear interpolation -> output image
```

A 64 x 64 tile contains 4096 pixels. If one bin contains 1024 pixels and 2048 pixels have intensity at or below this bin, the inclusive local CDF at that bin is `2048/4096 = 0.5`, producing an illustrative mapping near `0.5 x 255 = 127.5` (subject to the specific equalization convention and rounding). If neighboring mappings for a chosen pixel are `120, 130, 140, 150` and the normalized interpolation coordinates are `(x=0.25, y=0.5)`, the bilinearly weighted output is `0.75*0.5*120 + 0.25*0.5*130 + 0.75*0.5*140 + 0.25*0.5*150 = 132.5`. This illustrates why the LUT values are spatially blended: independent tile equalization could create abrupt boundaries.

At image edges, implementations may clamp, mirror, use fewer unique tiles or otherwise handle boundaries; verify actual behavior rather than assuming. Do not imply the example's dimensions, performance, or border policy came from an inspected repository.

## Example C: non-numeric flow

For authorization, trace a user request across identity/authentication, policy enforcement, resource lookup, and response or denial. Clearly distinguish the request's control decisions from data returned. Do not invent a token format or permission model.

## Example-selection rules

- **Numbers required (`numeric`/`both`):** use values with units, intermediate calculations and one measurable takeaway. If the system is qualitative, use dimensions or a clearly bounded synthetic scenario rather than invented performance.
- **Flow required (`flow`/`both`):** include an actual entry, intermediate transformations, dependency boundaries, final outcome, and at least one important fork or failure path when relevant.
- **Theory focus:** derive only the math that drives a meaningful choice; define variables and state assumptions.
- **Very-deep:** add the sensitivity of the result to one changed parameter. E.g., top 50 vs top 200 candidates may improve recall but raise reranking latency, often approximately with candidate count for a simple pairwise reranker, before batching effects.
- **Source fidelity:** if numeric values are from docs/benchmarks, cite them; if hypothetical, say so at the point of use.
