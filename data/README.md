# data/ — Extracted Knowledge Base

This directory contains everything extracted from the source book. These are the **raw facts** — not evaluations, not verdicts. Audits are in `../audit/`.

All files are read-only outputs of the processing scripts in `../scripts/`. Do not edit manually.

---

## Contents

### `phase0_sample/` — Representative Sample (01–12)
Initial 70-paragraph extraction used to establish the knowledge schema.

| File | Contents |
|------|----------|
| `01_paragraph_index.json` | 70 paragraphs with IDs, chapter, section, page |
| `02_entity_catalog.json` | 90 entities: persons, institutions, events, concepts |
| `03_concept_catalog.json` | 50 abstract concepts with definitions |
| `04_claim_catalog.json` | 80 claims with domain classification |
| `05_definition_catalog.json` | 25 explicit and implicit definitions |
| `06_axiom_catalog.json` | 15 foundational axioms, tiered |
| `07_argument_catalog.json` | 12 fully reconstructed arguments |
| `08_dependency_graph.json` | Claim-to-axiom dependency edges |
| `09_logical_graph.json` | Full directed graph: supports / contradicts / derives_from |
| `10_formalization_layer.json` | 20 symbolic formalizations with confidence scores |
| `11_theory_architecture.json` | Layer 0 (axioms) → Layer 5 (AI/terminal conclusions) |
| `12_compilation_report.md` | Phase 0 completion report |

### `phase0_extraction/` — Complete Extraction (13–17)
100% of the book processed. Supersedes the sample.

| File | Contents |
|------|----------|
| `13_claims_complete.jsonl` | **16,569 claims** — domain, type, axiom flag, paragraph source |
| `14_definitions_complete.jsonl` | **1,244 definitions** — explicit and implicit |
| `15_axiom_candidates_complete.jsonl` | **838 axiom candidates** — tiered |
| `16_paragraph_extractions_full.jsonl` | **1,807 paragraph records** |
| `17_compilation_report_full.json` | Final counts, domain breakdown, top-30 entities |
| `unique_claim_catalog.jsonl` | **16,178 deduplicated claims** |

### `phase075_graph/` — Dependency Resolution & Graph (18–31)

| File | Contents |
|------|----------|
| `18_claim_dependency_graph.json` | Summary: 35,052 edges |
| `18_claim_dependency_graph.jsonl` | Full 10,895 edge records |
| `19_claim_clusters.jsonl` | 26 thematic clusters |
| `20_axiom_reduction.json` | 15 → 6 minimum axioms |
| `21_contradiction_candidates.json` | Initial contradiction candidates |
| `22_core_theory_graph.graphml` | **154 nodes, 169 edges** — open in Gephi or Cytoscape |
| `23_theory_layers.json` | 7-layer architecture |
| `24_circularity_report.json` | Graph circularity detection |
| `25_definition_consistency_report.json` | Cross-definition consistency |
| `26_centrality_report.json` | Betweenness and eigenvector centrality |
| `27_theory_bottlenecks.json` | Structural bottlenecks |
| `28_fragility_report.json` | Fragility under node removal |
| `29_claim_to_axiom_paths.jsonl` | 3,000 BFS paths from claims to axioms |
| `30_formal_theory_graph.json` | Formal graph summary |
| `31_pre_evaluation_report.json` | Pre-evaluation structural report |

### `phase09_hardening/` — Theory Compiler Hardening (31–45)

| File | Contents |
|------|----------|
| `31_claim_atomization_report.json` | 17,229 atoms, 660 splits |
| `32_axiom_audit.json` | 636 retained / 838 candidates |
| `33_hidden_axioms.json` | **12 hidden axioms** discovered |
| `34_definition_normalization.json` | 12 canonical definitions, 3 conflicts |
| `35_dependency_validation.json` | 46 validated backbone edges |
| `36_inference_chains.json` | 19 chains, 12 fully traced |
| `37_orphan_nodes.json` | 8 source-only, 24 leaves, 0 true orphans |
| `38_cycle_reconstruction.json` | 0 graph cycles |
| `39_contradiction_reconstruction.json` | 10 candidates, 5 critical |
| `40_formalization_expansion.json` | 26 formalizations: propositional / FOL / modal / deontic |
| `41_minimum_axiom_set.json` | 3 secular + 3 theological = 6 minimum axioms |
| `42_theory_kernel.json` | **The irreducible core: 6 axioms + 14 claims + 8 definitions** |
| `43_graph_integrity_report.json` | Graph integrity score: 60/100 |
| `44_formal_readiness_report.json` | Theorem prover readiness: 64/100 |
| `45_hardening_report.json` | Final hardening summary |

---

## Data Format

**JSON** (`.json`) — single structured object, human-readable
**JSONL** (`.jsonl`) — one JSON record per line; use `jq`, pandas, or any JSON parser
**GraphML** (`.graphml`) — standard XML graph format; open with Gephi, Cytoscape, or NetworkX

## ID Conventions

| Prefix | Meaning |
|--------|---------|
| `A-XXXXXX` | Axiom |
| `C-XXXXXX` | Claim |
| `D-XXXXXX` | Definition |
| `P-XXXXXX` | Paragraph |
| `F-XXXXXX` | Formal statement |
| `CN-XXXXXX` | Concept |
| `E-XXXXXX` | Entity |
| `ARG-XXXXXX` | Argument |
