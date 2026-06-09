# Knowledge Base — Theory of Liberty / Religion / Iran
**Source:** Mohammadali Jannatkhahdoost, *Theory of Liberty (Individual Property Rights) — Iran & Religion*  
**Translator:** Taha Doostmohammadi  
**Compiled:** June 2026

This directory is the machine-readable canonical representation of the book.  
After reading these files, the source PDF is not needed for analysis.

## File Index

### Phase 1 — Representative Sample (superseded)
| File | Contents |
|------|----------|
| `01_paragraph_index.json` | 70 representative paragraphs with IDs, chapter, section, page, text |
| `02_entity_catalog.json` | 90 entities: persons, institutions, events, concepts, books, theories |
| `03_concept_catalog.json` | 50 abstract concepts with definitions and source paragraphs |
| `04_claim_catalog.json` | 80 claims with domain classification and source paragraphs |
| `05_definition_catalog.json` | 25 explicit/implicit definitions used by the author |
| `06_axiom_catalog.json` | 15 foundational axioms with tier classification |
| `07_argument_catalog.json` | 12 fully reconstructed arguments (premises → steps → conclusion) |
| `08_dependency_graph.json` | Claim-to-axiom dependency edges (~120 edges) |
| `09_logical_graph.json` | Full directed graph: supports / contradicts / defines / derives_from / references |
| `10_formalization_layer.json` | 20 symbolic formalizations of key claims with confidence scores |
| `11_theory_architecture.json` | Layered theory architecture: Layer 0 (axioms) → Layer 5 (AI/terminal conclusions) |
| `12_compilation_report.md` | Phase 0 Compilation Report answering representability questions |

### Phase 2 — Complete Per-Paragraph Extraction (100% of book)
| File | Contents |
|------|----------|
| `13_claims_complete.jsonl` | **16,569 claims** — every substantive sentence, with domain, type, axiom flag, paragraph source |
| `14_definitions_complete.jsonl` | **1,244 definitions** — explicit and implicit definitions extracted per paragraph |
| `15_axiom_candidates_complete.jsonl` | **838 axiom candidates** — propositions bearing axiomatic language, tiered (foundational / methodological / derived) |
| `16_paragraph_extractions_full.jsonl` | **1,807 paragraph records** — per-paragraph summary: sentence count, claim/def/axiom counts, references list, dependency concepts list |
| `17_compilation_report_full.json` | Final counts, domain breakdown, top-30 referenced entities |

## Theory in One Paragraph

The theory begins from the axiom of human free will (universally presupposed) and derives that liberty = individual property rights. Property rights, to withstand the state and the majority, require a divine source. True religion — Islam in particular, purified of mysticism, state-worship, and dialectical distortion — is that divine source and constitutes the only consistent formal axiomatic system for liberty. Mysticism (any system that separates humans from property, reason, and body and delivers them to a collective) is the enemy of liberty and the philosophical pipeline to totalitarianism. Iran is the civilizational continuum — the land of proprietors — whose two-root crisis (distortion of religion + theft of history) can be healed by this theory. The theory concludes with a claim about AI: only a consistent formal ethical system (which only true religion provides) can align artificial intelligence against totalitarian use.

## ID Conventions

- `A-XXXXXX` = Axiom
- `C-XXXXXX` = Claim
- `CN-XXXXXX` = Concept
- `D-XXXXXX` = Definition
- `E-XXXXXX` = Entity
- `ARG-XXXXXX` = Argument
- `P-XXXXXX` = Paragraph
- `F-XXXXXX` = Formal statement


---

## Phase 1 — Logical Consistency Audit

**Completion date:** June 2026
**Auditor role:** Formal logical auditor — no evaluation of historical, theological, or economic truth.

### Key Scores

| Dimension | Score |
|-----------|-------|
| Overall Logical Coherence | **64/100** |
| Axiom Quality | 72/100 |
| Inference Validity | 73/100 |
| Consistency | 71/100 |
| Definition Quality | 68/100 |
| Circularity Health | 62/100 |
| Formal Rigor | 58/100 |
| **Uniqueness Justification** | **28/100** (critical gap) |

### Major Findings

1. **Core chain is logically valid.** The derivation Free Will → Property Rights → Liberty → Tawhid → CFS → Religion passes logical validity testing with two small bridge premises needed (both philosophically defensible).

2. **CRITICAL: Mysticism definition is circular.** Mysticism is defined as anti-liberty, then "shown" to be anti-liberty. ~428 claims are affected. Fix requires one paragraph of definitional reform.

3. **Uniqueness claims are not demonstrated.** The theory claims to be THE only CFS for liberty and THE only solution for AI ethics. These are asserted, not proven. The theory demonstrates A consistent formal system for liberty — not THE only one. This is the theory's most significant logical gap.

4. **Gödel invocation is currently metaphorical.** The theory does not meet the arithmetic-encoding prerequisite for Gödel's theorems to formally apply. All 'Consistent (Gödel-sense)' language must be downgraded to 'non-contradictory' until P3 is demonstrated.

5. **12 hidden axioms discovered; 3 secretly foundational.** HA-001 (objective truth), HA-002 (reliable reason), HA-005 (valid inference) are prerequisites for every derivation and should be elevated to the named axiom set.

6. **Minimum axiom set: 6** (3 secular + 3 theological). 15 named axioms reduced by 60%.

7. **Kernel is DAG-acyclic.** No logical paradoxes found. The dependency graph is acyclic at the axiom level.

8. **10 contradiction candidates: 6 resolved, 3 genuine, 1 methodological tension.**

### Five Strongest Logical Achievements

1. Performative contradiction proof for free will (logically valid, score 92/100)
2. 60% axiom reduction to minimum set of 6
3. Game-theoretic stability argument via last-round problem (formally valid)
4. Axiom parsimony argument against elimination of Tawhid (structurally sound)
5. DAG structure — core derivation graph is acyclic

### Five Most Serious Logical Weaknesses

1. Circular definition of mysticism (CRITICAL — affects ~428 claims)
2. Uniqueness claims undemonstrated (the only CFS / only AI solution)
3. Gödel transfer unproven (illustrative, not technical)
4. Authentic religion / CFS circularity (moderate)
5. Three secretly foundational hidden axioms unacknowledged

### Readiness for Gödel Audit

**NOT YET READY.** Prerequisites before Gödel analysis:
1. Fix mysticism circularity
2. Elevate HA-001/002/005 to named axioms
3. Downgrade Gödel-technical language
4. Express uniqueness as theorem-to-prove
5. State explicit proof calculus (modus ponens etc.)
6. Attempt or refute arithmetic encoding (P3)

### Output Files (Phase 1)

| File | Contents |
|------|----------|
| `51_axiom_independence_report.json` | Independence test for all 15 named axioms |
| `52_hidden_axiom_analysis.json` | Necessity/foundationality of 12 hidden axioms |
| `53_contradiction_audit.json` | Verdict on all 10 contradiction candidates |
| `54_circularity_audit.json` | Classification of 5 circularity issues |
| `55_inference_validity_report.json` | 8 major inference chains tested |
| `56_necessity_analysis.json` | Logical necessity rating for 10 key claims |
| `57_uniqueness_audit.json` | Audit of all uniqueness claims (0/4 demonstrated) |
| `58_godel_precheck.json` | Gödel readiness: 44/100; P3 not met |
| `59_stress_test.json` | Kernel axiom removal impact analysis |
| `60_logical_scorecard.json` | 7-dimension logical scorecard |
| `61_logical_consistency_audit.md` | Complete Phase 1 final verdict |
