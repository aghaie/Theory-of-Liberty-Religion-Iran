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


---

## Phase 2 — Uniqueness Audit

**Completion date:** June 2026
**Role:** Adversarial scientific auditor — attempt to falsify uniqueness
**Primary Question:** Does the theory demonstrate THE ONLY CFS or merely A CFS?

### Overall Verdict

**A CFS — not THE ONLY CFS (as currently stated).**

The theory is the **best-performing** system among all 12 tested competitors. It is not demonstrably the only one.

### Scores

| Dimension | Score |
|-----------|-------|
| Competitor Elimination | **78/100** ← strongest result |
| Necessity of Free Will | **85/100** ← strongest individual claim |
| Uniqueness Justification | 35/100 |
| AI Uniqueness | 38/100 |
| Necessity of Theology | 45/100 |
| **Exclusivity Demonstration** | **20/100** ← weakest result |
| **Overall Uniqueness Score** | **50/100** |

*(Phase 1 uniqueness score was 28/100; improvement to 50/100 reflects structured analysis.)*

### Competitor Ranking (test suite score, 10 criteria, max 80)

| Rank | System | Score | % | Last-Round (C5) |
|------|--------|-------|---|-----------------|
| 1 | Theory of Liberty (reference) | 80/80 | 100% | PASS ✓ |
| 2 | Rothbardian Libertarianism | 64.5/80 | 81% | FAIL ✗ |
| 3 | Lockean Natural Rights | 56.5/80 | 71% | FAIL ✗ |
| 4 | Classical Liberalism | 53/80 | 66% | FAIL ✗ |
| 5 | Natural Law Theory | 54/80 | 68% | FAIL ✗ |
| 6 | Kantian Ethics | 48.5/80 | 61% | FAIL ✗ |
| 7 | Social Contractarianism | 43.5/80 | 54% | FAIL ✗ |
| 8 | Rawlsian Liberalism | 39/80 | 49% | FAIL ✗ |
| 9 | Constitutional AI | 34/80 | 43% | FAIL ✗ |
| 10 | Hayekian Order | 33/80 | 41% | FAIL ✗ |
| 11 | CEV | 27.5/80 | 34% | PARTIAL |
| 12 | Rule Utilitarianism | 23.5/80 | 29% | FAIL ✗ |
| 13 | Constitutional Democracy | 32.5/80 | 41% | PARTIAL |
| — | **CE-003 (constructed)** | ~70/80 | ~88% | **PASS** ✓ |

**Critical finding:** The Theory of Liberty is the ONLY system among 12 named-tradition competitors that PASSES C5 (Last-Round Problem). CE-003 (4-axiom secular construct) also passes.

### Strongest Counterexample

**CE-003: Minimum Secular CFS (4 axioms)**
1. Free will exists (denial is self-refuting)
2. Persons own themselves; property via self-ownership
3. Initiating coercion is categorically impermissible (NAP)
4. Terminal period of social interaction is unknowable (secular posit)

This system satisfies all required properties. It refutes the broad uniqueness claim.

**Why it does not defeat the theory:** CE-003's Axiom 4 is asserted without derivation. The Theory of Liberty derives its equivalent from Resurrection (theological) within a richer axiom system.

### Strongest Defense: Compound Uniqueness Claim

The theory IS the only known system satisfying ALL FIVE simultaneously:
- (a) Derives last-round stability (not posits it)
- (b) Agreement-admissible foundational axioms
- (c) Robust under all three adversarial stress conditions
- (d) Unified coverage of all four AI alignment dimensions from one derivation tree
- (e) Sealed authentication mechanism (khatam)

This is the correctly-scoped uniqueness claim.

### Theological Necessity

No theological axiom is logically necessary for grounding liberty. Secular functional equivalents exist for Tawhid, Resurrection, and Prophethood. However: the theological axioms provide superior parsimony, derivational depth, and the unique khatam property.

### Free Will Necessity

Free will (or functional equivalent) is practically necessary for any normative system that uses argument to ground rights. Any system that claims to demonstrate its position implicitly presupposes free will. This is the theory's strongest uniqueness-adjacent claim (85/100).

### Required Actions Before Phase 3

1. Fix CIRC-001 (mysticism definition) and CIRC-005 (authentic religion / CFS circularity)
2. Reformulate uniqueness claim to compound criterion (a-e) — drop "the only CFS"
3. Formally derive: "Any structural last-round solution requires an infinite-horizon mechanism or functional equivalent"
4. Respond formally to CE-003: show superior agreement-admissibility or identify additional criteria CE-003 fails
5. Develop the theological superiority argument: why the theological form is better than the secular functional equivalent

### Readiness for Gödel Audit

**NOT YET READY.** Same prerequisites as Phase 1, plus:
- Uniqueness claim must be reformulated to defensible scope
- CIRC-001 and CIRC-005 must be repaired
- CE-003 response must be incorporated

### Output Files (Phase 2)

| File | Contents |
|------|----------|
| `71_uniqueness_claims.json` | 8 uniqueness claims extracted, classified, prior audit verdicts |
| `72_required_properties.json` | 10 formal required properties derived from theory's own axioms |
| `73_cfs_test_suite.json` | 10-criterion formal test suite with weights |
| `74_competing_systems.json` | 12 competitors + reference system, steelmanned |
| `75_competitor_results.json` | Full test results for all 13 systems |
| `76_counterexamples.json` | 4 counterexamples; CE-003 identified as minimum genuine |
| `77_theological_necessity_audit.json` | Necessity analysis for Tawhid, Resurrection, Prophethood |
| `78_free_will_necessity_audit.json` | FW necessity across 4 philosophical positions |
| `79_last_round_audit.json` | Last-round solutions across all competitors |
| `80_ai_uniqueness_audit.json` | AI alignment uniqueness across 4 dimensions |
| `81_minimum_counterexample.json` | Minimum secular CFS (4 axioms) and minimum theological CFS |
| `82_uniqueness_steelman.json` | 5 strongest defenses of uniqueness |
| `83_uniqueness_refutation.json` | 5 strongest refutations of uniqueness |
| `84_uniqueness_final_verdict.md` | Complete Phase 2 final verdict |
| `85_uniqueness_scorecard.json` | 6-dimension scoring; overall 50/100 |
