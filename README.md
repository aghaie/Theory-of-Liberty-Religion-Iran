# Theory of Liberty — Religion & Iran
### A Machine-Audited Knowledge Base

**Source:** Mohammadali Jannatkhahdoost, *Theory of Liberty (Individual Property Rights) — Iran & Religion*
**Audit Engine:** Claude Sonnet 4.6 · **Status:** Phase 4 Complete · Classification: C (Substantially Survives)

---

## What Is This?

This repository applies formal logic and computational philosophy to a Persian political philosophy book. The book argues that authentic Islam — stripped of mysticism and state-worship — constitutes the only consistent formal axiomatic system capable of grounding individual liberty.

This project does not evaluate whether the argument is *true*. It evaluates whether the argument is *formally sound*: consistent, non-circular, derivationally complete, and logically sufficient.

The result is a machine-readable knowledge base of **16,569 claims**, **1,244 definitions**, **838 axiom candidates**, and **126 structured analysis files** across 8 audit phases.

---

## The Theory — Core Claim

> *Liberty = Individual Property Rights. Property rights require a foundation that cannot be overturned by the state or majority vote. Such a foundation requires a divine grounding. True religion — not mysticism, not state-theology — is the only consistent formal system that provides this grounding. Therefore: true Islam = liberty, and liberty's enemy = the mystical tradition.*

### Minimum Axiom Kernel (6 Axioms)

| ID | Statement | Tier |
|----|-----------|------|
| A-000001 | Free will exists; its denial is self-refuting | 0 — Secular |
| A-000004 | Tawhid: no servitude to anything other than God | 1 — Theological |
| A-000006 | Resurrection: accountability extends beyond death | 2 — Theological |
| A-000007 | Prophethood: authenticated specification (sealed at khatam) | 2 — Theological |
| A-000011 | A formal system must have finite and minimal axioms | 0 — Methodological |
| A-000012 | A formal system must be internally consistent | 0 — Methodological |

---

## Audit Scorecard

| Phase | Dimension | Score | Verdict |
|-------|-----------|-------|---------|
| Phase 0.9 | Graph Integrity | 60/100 | Structurally sound |
| Phase 1 | Logical Coherence | 62/100 | CIRC-001 critical |
| Phase 2 | Uniqueness | 50/100 | *A* CFS, not *the only* CFS |
| Phase 2.5 | Uniqueness (post CE-003 destruction) | **65/100** | CE-003 = weak counterexample |
| Phase 3 | Formal System Status | 39/100 | **B: Proto-Formal** |

### Score Progression

```
Phase 0.9  ████████████░░░░░░░░  60  Graph integrity
Phase 1    ████████████░░░░░░░░  62  Logical coherence
Phase 2    ██████████░░░░░░░░░░  50  Uniqueness (initial)
Phase 2.5  █████████████░░░░░░░  65  Uniqueness (CE-003 destroyed)
Phase 3    ███████░░░░░░░░░░░░░  39  Formal system rigor
```

---

## Key Findings

### What the Audit Confirmed
- **Free will axiom**: Practically necessary (85/100). Self-refutation argument is structurally valid.
- **Last-round stability**: The only tested system solving the game-theoretic last-round problem via derived (non-ad-hoc) axiom. Resurrection immune to dying-person counterexample; MS-A4 (secular rival) is not.
- **Kernel parsimony**: 1.06 derivations/axiom — 3× more parsimonious than minimum secular counterexample.
- **Axiomatic structure**: 6-axiom kernel with 14 claims and 8 definitions is coherent and internally non-circular at the structural level.
- **Category B classification**: Exceeds Rawls, Nozick, Rothbard, and Kant in formal system properties.

### What the Audit Found Deficient
- **CIRC-001 (Critical)**: "Mysticism" is defined as "anti-liberty tendency" — the argument against mysticism is circular.
- **CIRC-005 (Moderate)**: "Authentic religion" is defined as "CFS for liberty" — the uniqueness claim is partially self-referential.
- **No formal proof calculus**: The system uses informal derivation. No Hilbert-style, Natural Deduction, or Sequent Calculus proof sequences exist.
- **Robinson Arithmetic not encodable**: The system cannot encode Robinson Arithmetic Q. Gödel's theorems do not apply.
- **Uniqueness not proven**: CE-003 (a 4-axiom secular system) partially satisfies the same criteria, weakening the uniqueness claim.

---

## Competing Systems Benchmark

| System | CFS Score | C5: Last-Round | Status |
|--------|-----------|----------------|--------|
| **Theory of Liberty** | **80/80 (100%)** | **PASS** | Reference |
| Rothbardian Libertarianism | 64.5/80 (81%) | FAIL | Closest rival |
| Lockean Natural Rights | 56.5/80 (71%) | FAIL | |
| Classical Liberalism | 53/80 (66%) | FAIL | |
| CE-003 (constructed minimum) | ~70/80 (88%) | PASS | Weak counterexample |
| Rawlsian / Kantian / Hayekian | < 60% | FAIL | |

---

## Project Structure

```
Theory-of-Liberty-Religion-Iran/
│
├── README.md                          ← This file
├── CONTRIBUTING.md                    ← How to challenge or extend the audit
├── CITATION.cff                       ← Academic citation format
├── LICENSE                            ← MIT (scripts) + CC BY 4.0 (data)
├── LICENSE-DATA                       ← CC BY 4.0 full terms
├── .gitignore
│
├── source/
│   └── Theory of Liberty-Religion-Iran.pdf  ← Source book (read-only)
│
├── scripts/                           ← All processing scripts, in run order
│   ├── extract_full.py                  Phase 0: 100% paragraph extraction
│   ├── phase075.py                      Phase 0.75: dependency graph
│   ├── phase09_steps1to5.py  }
│   ├── phase09_steps6to10.py }          Phase 0.9: theory hardening
│   ├── phase09_steps11to15.py}
│   ├── phase1_steps1to5.py   }          Phase 1: logical consistency audit
│   ├── phase1_steps6to11.py  }
│   ├── phase2_steps1to7.py   }
│   ├── phase2_steps4to7.py   }          Phase 2: uniqueness audit
│   ├── phase2_steps8to15.py  }
│   ├── phase25_steps1to8.py  }          Phase 2.5: CE-003 counterexample audit
│   ├── phase25_steps9to15.py }
│   ├── phase3_steps1to8.py   }          Phase 3: formal system qualification
│   └── phase3_steps9to16.py  }
│
├── data/                              ← Extracted knowledge (raw facts from the book)
│   ├── README.md
│   ├── phase0_sample/                   (01–12)  70-paragraph sample
│   ├── phase0_extraction/               (13–17)  Full extraction: 16,569 claims
│   ├── phase075_graph/                  (18–31)  Dependency graph: 35,052 edges
│   └── phase09_hardening/               (31–45)  Theory kernel: 6 axioms
│
└── audit/                             ← Adversarial audit results (evaluations)
    ├── README.md
    ├── phase1_audit/                    (51–61)   Logical consistency: 62/100
    ├── phase2_uniqueness/               (71–85)   Uniqueness: 65/100 · CE-003 found
    ├── phase25_ce003/                   (91–105)  CE-003 = weak counterexample
    ├── phase3_formal/                   (111–126) B: Proto-Formal · 39/100
    └── phase4_hostile/                  (131–145) Hostile review: C (Survives with repairs)
```

---

## Key Files

| File | Why It Matters |
|------|----------------|
| `data/phase075_graph/22_core_theory_graph.graphml` | Theory graph — open in Gephi or Cytoscape |
| `data/phase09_hardening/42_theory_kernel.json` | The irreducible 6-axiom core |
| `data/phase0_extraction/13_claims_complete.jsonl` | All 16,569 claims |
| `audit/phase1_audit/61_logical_consistency_audit.md` | Phase 1 verdict |
| `audit/phase2_uniqueness/84_uniqueness_final_verdict.md` | Phase 2 verdict |
| `audit/phase25_ce003/104_counterexample_verdict.md` | CE-003 verdict |
| `audit/phase3_formal/126_formal_system_final_verdict.md` | Phase 3 verdict |
| `audit/phase4_hostile/144_hostile_review_final_verdict.md` | Phase 4 — hostile review verdict (C: Survives) |
| `audit/phase4_hostile/141_killshot_analysis.md` | Kill shot analysis — no single fatal critique found |
| `audit/phase4_hostile/140_top_criticisms.json` | 25 strongest criticisms, ranked by severity |

---

## How to Navigate

**To understand the theory:** Start with `data/phase09_hardening/42_theory_kernel.json`

**To see what was proven and what wasn't:** Read the four verdict files in `audit/` (61, 84, 104, 126)

**To visualize the argument structure:** Open `data/phase075_graph/22_core_theory_graph.graphml` in Gephi

**To explore all claims:** The `.jsonl` files in `data/phase0_extraction/` are line-delimited JSON

**To understand the open problems:** See the "Open Issues" section in `audit/README.md`

**To challenge a finding:** Open an issue using the Audit Challenge template in `.github/ISSUE_TEMPLATE/`

---

## Formal System Classification

The theory was evaluated against the Hilbert-Tarski-Gödel consensus for formal axiomatic systems:

| Category | Description | Examples |
|----------|-------------|---------|
| A — Full Formal System | Complete: formal language, proof calculus, machine-verifiable | ZFC, Peano Arithmetic |
| **B — Proto-Formal** | **Axiomatic intent, implicit inference, no proof calculus** | **This theory** |
| C — Structured Philosophy | Rigorous but not axiomatic in formal sense | Rawls, Nozick, Rothbard, Kant |
| D — Informal Argument | No formal structure | Most political philosophy |

To reach Category A, the theory needs: explicit inference rules, 8 Hilbert-style proof sequences, and a Robinson Arithmetic module.

---

## Roadmap to Phase 4

| Priority | Action | Effect |
|----------|--------|--------|
| P1 | Fix CIRC-001: structural definition of mysticism | Unblocks ~428 claims |
| P2 | Fix CIRC-005: independent definition of authentic religion | Uniqueness argument becomes non-circular |
| P3 | Name hidden axioms HA-001/002/005 | Epistemological foundation explicit |
| P4 | State inference rules (MP, RAA, UI, HS) | Enables proof calculus |
| P5 | Write 3 bridge premises as named axioms | Completes 5 proof reconstructions |
| P6 | Write 8 Hilbert-style proof sequences | Path to Category A |
| P7 | Add Robinson Arithmetic Q module | Gödel analysis becomes possible |
| P8 | Translate kernel to Lean 4 | Mechanically verified core |

---

## Technical Notes

- All processing scripts are in `scripts/` in run order — from `extract_full.py` through `phase3_steps9to16.py`
- `.jsonl` files are line-delimited JSON — one record per line
- `.graphml` is standard XML — load with Gephi, Cytoscape, or NetworkX
- No external dependencies required to read the knowledge base
- The source PDF was not modified; all analysis is derived from the text only

---

*Audited June 2026. The audit is adversarial and does not represent the author's position.*


---

## Phase 4 — Hostile Expert Review

**Panel**: 20 reviewers — Gödel, Tarski, Russell, Quine, Dennett, Parfit, Lewis, Rawls, Nozick, Ostrom, Hayek, Yudkowsky, Bostrom, Christiano, Stuart Russell, Nash, Aumann, Popper, Lakatos, Sowell

**Files**: `audit/phase4_hostile/` (131–145)

### Final Classification

**C — Substantially Survives with Repairs Required**

The theory survives hostile expert review in its core but not in its peripheral claims.

### What Survives
- Anti-totalitarianism structural argument (most robust; 90% confidence)
- Free will foundation (85%)
- Last-round game-theoretic solution (scoped to finite case with common knowledge; 75%)
- Parsimony of 6-axiom kernel (objective metric; 90%)
- AI alignment values specification (not complete mechanism; 80%)

### What Collapses Under Review
- Uniqueness claim ("THE ONLY CFS") — CE-003 and secular alternatives exist
- Formal system Category A claim — Category B (39/100) only
- CIRC-001 (mysticism = anti-liberty) — circular, must be reformulated
- CIRC-005 (authentic religion = CFS for liberty) — circular, must be reformulated
- Universal last-round solution — scoped to common-knowledge communities

### Strongest Criticism
**Tarski's circularity objection**: CIRC-001 and CIRC-005 make ~600 claims analytically true, not discovered. Until fixed, the uniqueness argument and anti-mysticism argument are circular. Severity: 9/10.

### Best Defense
**Structural reformulation of Tawhid**: "No finite entity possesses non-contingent, non-delegated, unlimited authority over rational agents." This is defensible by atheists and believers alike, removes the God-existence prerequisite, and preserves the full anti-totalitarianism conclusion.

### Survivability Verdict
If all 25 strongest criticisms are stipulated as correct, the theory does not collapse — it contracts. What remains is still more formally rigorous than Rawls, Nozick, Hayek, Rothbard, and Kant by the standards of Phase 3. The core metaphysical derivation is intact.

### Academic Reception Forecast
| Institution | Interest | Key Blocker |
|-------------|----------|-------------|
| Oxford Philosophy | Medium | CIRC-001/005; no formal proofs |
| MIRI | **High** | Needs Lean 4 formalization |
| Princeton Politics | Medium-High | Rawls engagement; circularity |
| U Chicago Economics | Medium | Needs empirical predictions |
| DeepMind / Anthropic | Low-Medium | Non-ML approach |

**After full formalization (Lean 4, Hilbert proofs, Robinson Q)**: potential for exceptional academic reception as the only mechanically verified formal axiomatic system in political philosophy.

### Required Repairs to Reach Classification D
1. Fix CIRC-001 and CIRC-005 with structural definitions
2. Reformulate uniqueness claim as "strongest available CFS"
3. Add explicit inference rules (MP, RAA, UI, HS)
4. Scope the last-round solution to finite case with common knowledge
5. Reformulate Tawhid structurally (remove God-existence prerequisite)
