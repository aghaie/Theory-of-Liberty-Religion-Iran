#!/usr/bin/env python3
"""Phase 2 Steps 1-7: Uniqueness Audit — Claim Extraction, Test Suite,
Competitor Construction, Test Run, Counterexample Search, Theological Necessity,
Free Will Necessity."""

import json, os
from collections import defaultdict

KB = "/Users/ali/Documents/GitHub/Theory-of-Liberty-Religion-Iran/knowledge_base"

def L(p):
    return json.load(open(p, encoding="utf-8"))

def save(name, obj):
    for p in [f"/tmp/{name}", f"{KB}/{name}"]:
        json.dump(obj, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"  Saved: {name}", flush=True)

# Load Phase 1 + kernel artifacts
min_ax   = L(f"{KB}/41_minimum_axiom_set.json")
kernel   = L(f"{KB}/42_theory_kernel.json")
ax_ind   = L(f"{KB}/51_axiom_independence_report.json")
inf_v    = L(f"{KB}/55_inference_validity_report.json")
nec_ana  = L(f"{KB}/56_necessity_analysis.json")
uniq_au  = L(f"{KB}/57_uniqueness_audit.json")
godel    = L(f"{KB}/58_godel_precheck.json")
scorecard = L(f"{KB}/60_logical_scorecard.json")

print("Phase 2 loaded.", flush=True)

# ════════════════════════════════════════════════════════════════════════════
# STEP 1 — EXTRACT UNIQUENESS CLAIMS
# ════════════════════════════════════════════════════════════════════════════
print("\nStep 1: Extracting uniqueness claims...", flush=True)

UNIQUENESS_CLAIMS = [
    {
        "id": "UC-001",
        "claim_text": "The theory of liberty is THE only existing solution for AI ethics.",
        "source": "kernel_claim_C-000071 / AI-alignment chapter",
        "strength": "ABSOLUTE",
        "scope": "AI ethics / value alignment",
        "dependencies": ["A-000001", "A-000004", "A-000011", "A-000012", "C-000029"],
        "logical_form": "∀S [S = CFS_for_liberty → S ≡ authentic_religion]  →  ¬∃S′ [S′ ≠ ToL ∧ S′ solves_AI_ethics]",
        "how_stated_in_text": "Challenge-method: 'produce a competing system and we will evaluate it'",
        "prior_audit_verdict": "NOT_DEMONSTRATED",
    },
    {
        "id": "UC-002",
        "claim_text": "Authentic religion is THE only consistent formal system for liberty.",
        "source": "C-000029 / CFS biconditional chapter",
        "strength": "ABSOLUTE",
        "scope": "political philosophy / formal systems",
        "dependencies": ["A-000001", "A-000004", "A-000011", "A-000012"],
        "logical_form": "∀S [CFS(S, L) ↔ authentic_religion(S)]",
        "how_stated_in_text": "Biconditional: CFS for liberty ↔ authentic religion (by definition + argument)",
        "prior_audit_verdict": "PARTIALLY_DEMONSTRATED (right-to-left by definition; left-to-right not proven)",
    },
    {
        "id": "UC-003",
        "claim_text": "Tawhid is the uniquely minimal principle that grounds liberty with finite axioms.",
        "source": "C-000017 / axiom-parsimony chapter",
        "strength": "STRONG",
        "scope": "axiomatic minimality",
        "dependencies": ["A-000004", "A-000011"],
        "logical_form": "∀P [single_agreement_admissible_anti_servitude_principle(P) → P ≡ Tawhid]",
        "how_stated_in_text": "Argued: eliminating Tawhid requires infinitely many replacement axioms",
        "prior_audit_verdict": "NOT_DEMONSTRATED",
    },
    {
        "id": "UC-004",
        "claim_text": "Without Resurrection, liberty is uniquely unstable (no other mechanism solves the last-round problem).",
        "source": "C-000021 / game-theory chapter",
        "strength": "STRONG",
        "scope": "game-theoretic stability",
        "dependencies": ["A-000006"],
        "logical_form": "∀M [solves_last_round(M) → M ≡ Resurrection_or_functional_equivalent]",
        "how_stated_in_text": "Game-theoretic argument: infinite iteration requires infinite or unknown horizon",
        "prior_audit_verdict": "PARTIAL — the logical structure is valid; whether Resurrection is the ONLY solution is unstated",
    },
    {
        "id": "UC-005",
        "claim_text": "The Qur'an is the uniquely inimitable formal specification of the system (tahaddi challenge).",
        "source": "theological chapters",
        "strength": "THEOLOGICAL",
        "scope": "textual / theological",
        "dependencies": ["A-000007"],
        "logical_form": "¬∃T [T ≠ Quran ∧ T is_complete_CFS_specification]",
        "how_stated_in_text": "Classical i'jaz argument: challenge to produce equivalent text",
        "prior_audit_verdict": "OUTSIDE_LOGICAL_SCOPE (theological claim, not subject to formal audit)",
    },
    {
        "id": "UC-006",
        "claim_text": "The system is consistent in the Gödel-technical sense, uniquely among normative systems.",
        "source": "methodology chapter / Gödel framing",
        "strength": "METHODOLOGICAL",
        "scope": "formal-methods claim",
        "dependencies": ["A-000012", "HA-008"],
        "logical_form": "Con(ToL) ∧ ∀S [normative_system(S) ∧ S ≠ ToL → ¬Con(S)]",
        "how_stated_in_text": "Gödel framing: the self-application test proves consistency",
        "prior_audit_verdict": "INVALID — Gödel precheck scored 44/100; P3 (arithmetic encoding) not met",
    },
    {
        "id": "UC-007",
        "claim_text": "States (coercive monopolies) cannot be agreement-admissible; only religion as CFS can be.",
        "source": "anti-statism chapter",
        "strength": "STRONG",
        "scope": "political philosophy",
        "dependencies": ["A-000001", "A-000004", "A-000008"],
        "logical_form": "∀S [coercive_monopoly(S) → ¬agreement_admissible(S)] ∧ [authentic_religion → agreement_admissible]",
        "how_stated_in_text": "Argued: compulsion cannot be consented to ex ante by rational agents",
        "prior_audit_verdict": "STRONGLY_SUPPORTED for the negative claim; the positive exclusivity is unstated",
    },
    {
        "id": "UC-008",
        "claim_text": "Denial of free will is self-refuting; therefore free will is the uniquely valid starting axiom.",
        "source": "C-000039 / performative-contradiction chapter",
        "strength": "LOGICALLY_NECESSARY",
        "scope": "epistemological / foundational",
        "dependencies": ["A-000001"],
        "logical_form": "assert(¬FW) ⊃ FW  ∴  FW is necessarily true  ∴  FW must be an axiom of any valid normative system",
        "how_stated_in_text": "Performative contradiction: denying free will is self-refuting",
        "prior_audit_verdict": "LOGICALLY_VALID for the self-refutation; uniqueness as starting axiom is a further inference",
    },
]

save("71_uniqueness_claims.json", {
    "total_uniqueness_claims": len(UNIQUENESS_CLAIMS),
    "by_strength": {
        "ABSOLUTE": [u["id"] for u in UNIQUENESS_CLAIMS if u["strength"]=="ABSOLUTE"],
        "STRONG": [u["id"] for u in UNIQUENESS_CLAIMS if u["strength"]=="STRONG"],
        "LOGICALLY_NECESSARY": [u["id"] for u in UNIQUENESS_CLAIMS if u["strength"]=="LOGICALLY_NECESSARY"],
        "METHODOLOGICAL": [u["id"] for u in UNIQUENESS_CLAIMS if u["strength"]=="METHODOLOGICAL"],
        "THEOLOGICAL": [u["id"] for u in UNIQUENESS_CLAIMS if u["strength"]=="THEOLOGICAL"],
    },
    "prior_audit_summary": {
        "not_demonstrated": ["UC-001","UC-003","UC-006"],
        "partially_demonstrated": ["UC-002","UC-004","UC-007"],
        "logically_valid_limited_scope": ["UC-008"],
        "outside_scope": ["UC-005"],
    },
    "claims": UNIQUENESS_CLAIMS,
})

# ════════════════════════════════════════════════════════════════════════════
# STEP 2 — EXTRACT REQUIRED PROPERTIES
# ════════════════════════════════════════════════════════════════════════════
print("Step 2: Extracting required properties...", flush=True)

REQUIRED_PROPERTIES = [
    {
        "id": "RP-001",
        "name": "Internal Consistency",
        "description": "The system contains no internal contradictions; it passes the self-application test (applying the system's own principles to itself does not produce a violation).",
        "derived_from": "A-000012 + Phase 1 consistency score",
        "operationalization": "No pair (P, ¬P) is derivable from the axioms. The system does not forbid what it requires.",
        "criticality": "NECESSARY",
    },
    {
        "id": "RP-002",
        "name": "Finite Axiom Set",
        "description": "The system can be fully specified by a finite and enumerable set of axioms.",
        "derived_from": "A-000011",
        "operationalization": "The axiom set has cardinality |A| < ∞, and A is decidable.",
        "criticality": "NECESSARY",
    },
    {
        "id": "RP-003",
        "name": "Grounding of Liberty",
        "description": "Liberty (individual property rights over body and legitimately acquired assets) is derivable from the axioms, not merely asserted.",
        "derived_from": "A-000001 + A-000002 + C-000001",
        "operationalization": "The system has a derivation path from its foundational axioms to a liberty-affirming theorem.",
        "criticality": "NECESSARY",
    },
    {
        "id": "RP-004",
        "name": "Property Rights Prior to State",
        "description": "Individual property rights are recognized as existing prior to and independent of state authority.",
        "derived_from": "A-000002 + A-000008",
        "operationalization": "The system does not derive property from state grant or democratic consent.",
        "criticality": "NECESSARY",
    },
    {
        "id": "RP-005",
        "name": "Solution to Last-Round Problem",
        "description": "The system provides a structural mechanism that prevents defection in the final period of any finitely-repeated social game.",
        "derived_from": "A-000006 + C-000021",
        "operationalization": "The system contains either (a) an infinite-horizon mechanism, or (b) an epistemic mechanism making the terminal round unknowable, or (c) a dominance argument that makes cooperation always dominant regardless of horizon.",
        "criticality": "HIGH",
    },
    {
        "id": "RP-006",
        "name": "Structural Resistance to Totalitarianism",
        "description": "The system contains an axiom or derived principle that makes unlimited concentration of coercive power structurally impermissible.",
        "derived_from": "A-000004 + C-000055",
        "operationalization": "There exists a theorem T in the system such that T = 'no entity may hold monopoly coercive power over all persons.'",
        "criticality": "HIGH",
    },
    {
        "id": "RP-007",
        "name": "Agreement-Admissibility",
        "description": "The core principles of the system can, in principle, be accepted by any rational agent regardless of prior commitments, without being imposed by force.",
        "derived_from": "A-000009 + anti-statism argument",
        "operationalization": "The system's foundational axiom does not require belief in a particular historical claim, ethnic identity, or coercive imposition to be accepted.",
        "criticality": "HIGH",
    },
    {
        "id": "RP-008",
        "name": "Accountability Mechanism",
        "description": "The system provides a mechanism for holding agents accountable for violations of liberty that does not itself violate liberty.",
        "derived_from": "A-000010 + C-000029",
        "operationalization": "The system has a theorem deriving accountability without state monopoly on coercive enforcement.",
        "criticality": "HIGH",
    },
    {
        "id": "RP-009",
        "name": "Supports AI Value Alignment",
        "description": "The system provides formal criteria sufficient to evaluate whether an AI system's objectives are aligned with human liberty.",
        "derived_from": "C-000071 + AI-alignment chapter",
        "operationalization": "The system's axioms can be expressed as evaluable constraints on an AI objective function.",
        "criticality": "CONTEXTUAL",
    },
    {
        "id": "RP-010",
        "name": "Axiom Minimality",
        "description": "The system's axiom set is irreducible: no axiom is derivable from the others.",
        "derived_from": "A-000011 + Phase 1 Step 1",
        "operationalization": "No axiom A_i can be proven from {A_1,...,A_{i-1},A_{i+1},...,A_n}.",
        "criticality": "FORMAL",
    },
]

save("72_required_properties.json", {
    "total_properties": len(REQUIRED_PROPERTIES),
    "by_criticality": {
        "NECESSARY": [r["id"] for r in REQUIRED_PROPERTIES if r["criticality"]=="NECESSARY"],
        "HIGH": [r["id"] for r in REQUIRED_PROPERTIES if r["criticality"]=="HIGH"],
        "CONTEXTUAL": [r["id"] for r in REQUIRED_PROPERTIES if r["criticality"]=="CONTEXTUAL"],
        "FORMAL": [r["id"] for r in REQUIRED_PROPERTIES if r["criticality"]=="FORMAL"],
    },
    "properties": REQUIRED_PROPERTIES,
    "note": "All properties derived from the theory's own axioms and kernel claims. No external requirements imported.",
})

# ════════════════════════════════════════════════════════════════════════════
# STEP 3 — BUILD FORMAL TEST SUITE
# ════════════════════════════════════════════════════════════════════════════
print("Step 3: Building formal test suite...", flush=True)

TEST_SUITE = [
    {
        "criterion_id": "C1",
        "name": "Internal Consistency",
        "from_property": "RP-001",
        "test": "Does the system avoid deriving both P and ¬P for any proposition P central to liberty?",
        "pass_threshold": "No direct contradiction in core axioms or kernel claims.",
        "weight": 10,
    },
    {
        "criterion_id": "C2",
        "name": "Finite Enumerable Axiom Set",
        "from_property": "RP-002",
        "test": "Can the system be fully specified by a finite, listable set of axioms?",
        "pass_threshold": "Axiom set has definite cardinality; no open-ended or procedural axiom generation.",
        "weight": 8,
    },
    {
        "criterion_id": "C3",
        "name": "Derived Grounding of Liberty",
        "from_property": "RP-003",
        "test": "Is liberty (individual property rights) a theorem derivable from foundational axioms, not merely a postulate?",
        "pass_threshold": "A derivation path exists from tier-0 axioms to a liberty theorem.",
        "weight": 10,
    },
    {
        "criterion_id": "C4",
        "name": "Property Rights Prior to State",
        "from_property": "RP-004",
        "test": "Does the system recognize property rights as pre-political and non-state-derived?",
        "pass_threshold": "Property rights are not derived from democratic consent, social contract, or state grant.",
        "weight": 9,
    },
    {
        "criterion_id": "C5",
        "name": "Last-Round Problem Solution",
        "from_property": "RP-005",
        "test": "Does the system contain a structural mechanism preventing terminal-period defection in finitely-repeated social games?",
        "pass_threshold": "The system provides an infinite-horizon, epistemic-uncertainty, or dominance mechanism.",
        "weight": 9,
    },
    {
        "criterion_id": "C6",
        "name": "Structural Anti-Totalitarianism",
        "from_property": "RP-006",
        "test": "Does the system have a derived or axiomatic prohibition on unlimited coercive monopoly power?",
        "pass_threshold": "A theorem or axiom explicitly makes totalitarian concentration structurally impermissible.",
        "weight": 8,
    },
    {
        "criterion_id": "C7",
        "name": "Agreement-Admissibility",
        "from_property": "RP-007",
        "test": "Can the system's foundational axioms be accepted by rational agents without coercion and without presupposing a particular historical or ethnic identity?",
        "pass_threshold": "The core axioms do not require acceptance of unverifiable historical claims or group membership as prerequisites.",
        "weight": 8,
    },
    {
        "criterion_id": "C8",
        "name": "Non-Coercive Accountability",
        "from_property": "RP-008",
        "test": "Does the system derive a mechanism for holding agents accountable for liberty-violations that does not itself violate liberty?",
        "pass_threshold": "A theorem exists connecting accountability to non-coercive or proportional response mechanisms.",
        "weight": 7,
    },
    {
        "criterion_id": "C9",
        "name": "AI Value Alignment Criteria",
        "from_property": "RP-009",
        "test": "Can the system's axioms be expressed as evaluable, formal constraints on an AI objective function?",
        "pass_threshold": "At minimum 3 formalizable constraints exist that could be implemented as an alignment specification.",
        "weight": 6,
    },
    {
        "criterion_id": "C10",
        "name": "Axiom Minimality / Parsimony",
        "from_property": "RP-010",
        "test": "Is the axiom set irreducible (no axiom is derivable from the others)?",
        "pass_threshold": "No confirmed redundancy found in the axiom set.",
        "weight": 5,
    },
]

save("73_cfs_test_suite.json", {
    "total_criteria": len(TEST_SUITE),
    "max_score": sum(c["weight"] for c in TEST_SUITE),
    "scoring_key": {"PASS": 1.0, "PARTIAL": 0.5, "FAIL": 0.0},
    "criteria": TEST_SUITE,
    "note": "PASS = criterion met. PARTIAL = criterion partially met with significant gaps. FAIL = criterion not met.",
})

print("Steps 1-3 complete.", flush=True)
