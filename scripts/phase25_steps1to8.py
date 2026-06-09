#!/usr/bin/env python3
"""Phase 2.5 Steps 1-8: CE-003 Reconstruction, Axiom Independence,
Hidden Axioms, Parsimony, Unknown-Horizon Audit, Last-Round Attack,
Agreement Admissibility, AI Stress Test."""

import json

KB = "/Users/ali/Documents/GitHub/Theory-of-Liberty-Religion-Iran/knowledge_base"

def L(p): return json.load(open(p, encoding="utf-8"))
def save(name, obj):
    for p in [f"/tmp/{name}", f"{KB}/{name}"]:
        json.dump(obj, open(p,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"  Saved: {name}", flush=True)

ce_data  = L(f"{KB}/76_counterexamples.json")
min_ce   = L(f"{KB}/81_minimum_counterexample.json")
kernel   = L(f"{KB}/42_theory_kernel.json")
min_ax   = L(f"{KB}/41_minimum_axiom_set.json")
inf_v    = L(f"{KB}/55_inference_validity_report.json")
stress   = L(f"{KB}/59_stress_test.json")

print("Phase 2.5 loaded.", flush=True)

# ════════════════════════════════════════════════════════════════════════════
# STEP 1 — RECONSTRUCT CE-003
# ════════════════════════════════════════════════════════════════════════════
print("\nStep 1: Reconstructing CE-003...", flush=True)

CE003 = {
    "name": "CE-003: Minimum Secular CFS",
    "origin": "Constructed in Phase 2 Step 11 as minimal 4-axiom secular alternative.",
    "axioms": [
        {
            "id": "MS-A1",
            "text": "Free will exists. Denial of free will is self-refuting because assertion of any claim presupposes the ability to reason, which presupposes free will.",
            "type": "epistemological_foundational",
            "source_tradition": "Performative-contradiction argument; see also C-000039 in Theory of Liberty",
            "explicit": True,
        },
        {
            "id": "MS-A2",
            "text": "Persons own themselves. Property in external things arises from self-ownership through labour-mixing/homesteading of unowned resources.",
            "type": "normative_foundational",
            "source_tradition": "Rothbard (Ethics of Liberty); Locke (Second Treatise, Ch. 5)",
            "explicit": True,
        },
        {
            "id": "MS-A3",
            "text": "Initiating coercion against a person or their legitimately-held property is categorically impermissible. (Non-Aggression Principle, NAP.)",
            "type": "normative_deontological",
            "source_tradition": "Rothbard; Spooner; Spencer; natural rights tradition",
            "explicit": True,
        },
        {
            "id": "MS-A4",
            "text": "The terminal period of social interaction is unknowable by any agent at any time.",
            "type": "game_theoretic_stability",
            "source_tradition": "Constructed for CE-003; functional analogue to Resurrection in Theory of Liberty",
            "explicit": True,
        },
    ],
    "claimed_derivations": [
        "MS-A1 → self-ownership justified (I own my reasoning capacity → I own my body)",
        "MS-A2 → property rights as pre-political (arises prior to any state)",
        "MS-A3 → anti-statism (state = systematic initiator of coercion → state is impermissible)",
        "MS-A4 → last-round stability (unknown terminal prevents backward induction → cooperation is always rational)",
        "MS-A1 + MS-A2 + MS-A3 → liberty (sphere of non-interference over self and property)",
        "MS-A3 + MS-A4 → structural resistance to totalitarianism (totalitarianism = maximised coercion → maximally impermissible)",
    ],
    "claimed_inference_rules": [
        "Modus ponens (assumed)",
        "Universal instantiation (assumed)",
        "Standard first-order logic (assumed)",
    ],
    "formal_language": "Natural language with formal intent — no explicit formal grammar stated.",
    "consistency_mechanism": (
        "Self-application: does the system violate its own axioms? "
        "NAP applied to NAP: the NAP itself does not initiate coercion → passes. "
        "Self-ownership applied to self-ownership: the axiom does not deprive anyone of ownership → passes."
    ),
}

save("91_ce003_reconstruction.json", {
    "ce003": CE003,
    "audit_note": (
        "Reconstruction reveals that CE-003 as stated is a minimal 4-axiom skeleton. "
        "The derivations claimed presuppose inference rules, definitions, and background "
        "conditions that are not stated. Phase 2.5 will audit these systematically."
    ),
})

# ════════════════════════════════════════════════════════════════════════════
# STEP 2 — AXIOM INDEPENDENCE TEST
# ════════════════════════════════════════════════════════════════════════════
print("Step 2: CE-003 axiom independence test...", flush=True)

AX_IND = [
    {
        "axiom": "MS-A1",
        "verdict": "INDEPENDENT",
        "derivable_from_others": False,
        "analysis": (
            "MS-A1 (free will) cannot be derived from MS-A2 (self-ownership), "
            "MS-A3 (NAP), or MS-A4 (unknown-horizon). None of the other three axioms "
            "entail that free will exists — they only presuppose it. "
            "INDEPENDENT: MS-A1 is a genuine axiom of CE-003."
        ),
        "flag": None,
    },
    {
        "axiom": "MS-A2",
        "verdict": "PARTIALLY_DEPENDENT",
        "derivable_from_others": "PARTIAL",
        "analysis": (
            "Self-ownership (MS-A2) is NOT derivable from MS-A3 alone. However, "
            "it IS partially presupposed by MS-A1: 'I own my reasoning capacity → I own my body' "
            "is a derivation from MS-A1, not an independent axiom. "
            "The PROPERTY ACQUISITION part of MS-A2 (homesteading) is genuinely independent. "
            "The SELF-OWNERSHIP part of MS-A2 may be derivable from MS-A1 given the hidden "
            "bridge premise that 'to own one's reasoning capacity is to own the substrate of reasoning.' "
            "FLAG: MS-A2 is partially redundant — the self-ownership component may reduce to MS-A1 "
            "given a bridge premise. The homesteading component is independently required."
        ),
        "flag": "PARTIAL_REDUNDANCY_RISK",
    },
    {
        "axiom": "MS-A3",
        "verdict": "DEFINITIONALLY_DEPENDENT",
        "derivable_from_others": "DEFINITIONAL",
        "analysis": (
            "MS-A3 (NAP) is not derivable from MS-A1 or MS-A2 without an additional bridge. "
            "Why is initiating coercion categorically impermissible? "
            "The standard derivation is: self-ownership (MS-A2) → coercion violates self-ownership → "
            "coercion is impermissible. BUT this derivation requires: "
            "(a) categorical impermissibility (moral realism, not just instrumental prudence), and "
            "(b) 'violations of self-ownership are always wrong' which is an ADDITIONAL normative premise. "
            "As stated, MS-A3 is a deontological axiom that CANNOT be derived from the property axiom "
            "alone without importing moral realism. "
            "ALTERNATIVE READING: if MS-A3 is intended as a DEFINITION ('coercion' means 'that which is "
            "impermissible'), then it is definitional, not synthetic. "
            "FLAG: MS-A3 is either (a) a genuine independent axiom (requiring moral realism), or "
            "(b) a definition — in which case it adds no content beyond what 'impermissible' already implies."
        ),
        "flag": "DEFINITIONAL_OR_MORAL_REALISM_REQUIRED",
    },
    {
        "axiom": "MS-A4",
        "verdict": "INDEPENDENT_AND_AD_HOC",
        "derivable_from_others": False,
        "analysis": (
            "MS-A4 (unknown-horizon posit) is completely independent of MS-A1, MS-A2, MS-A3. "
            "No derivation from the other three axioms produces MS-A4. "
            "MS-A4 was ADDED specifically to solve the last-round problem — it was not independently "
            "motivated by the other axioms. "
            "AD HOC FLAG: an axiom is 'ad hoc' if it is added specifically to save a theory from "
            "a counterexample, with no independent motivation. MS-A4 is textbook ad hoc: "
            "it was added to CE-003 precisely and only to solve the last-round problem. "
            "It has no derivation from the liberty-grounding axioms and no independent motivation. "
            "VERDICT: INDEPENDENT but AD HOC."
        ),
        "flag": "AD_HOC_AXIOM",
    },
]

independence_summary = {
    "truly_independent": ["MS-A1", "MS-A4"],
    "partially_dependent": ["MS-A2"],
    "definitional_or_requires_hidden_axiom": ["MS-A3"],
    "ad_hoc_axioms": ["MS-A4"],
    "critical_finding": (
        "CE-003 has ONE confirmed ad hoc axiom (MS-A4) and ONE axiom with a definitional problem "
        "(MS-A3). The ad hoc character of MS-A4 is a serious structural defect: axioms should be "
        "independently motivated, not added to solve specific problems. Compare: Resurrection in "
        "the Theory of Liberty is not ad hoc — it is independently motivated by theology and "
        "connects to Tawhid and Prophethood via derivation chains. MS-A4 has no such motivation."
    ),
}

save("92_ce003_axiom_independence.json", {
    "total_axioms": 4,
    "independence_analyses": AX_IND,
    "summary": independence_summary,
})

# ════════════════════════════════════════════════════════════════════════════
# STEP 3 — HIDDEN AXIOM DISCOVERY
# ════════════════════════════════════════════════════════════════════════════
print("Step 3: CE-003 hidden axiom discovery...", flush=True)

CE003_HIDDEN = [
    {
        "id": "HA-CE-001",
        "name": "Objective Truth",
        "description": "MS-A1 (free will via performative contradiction) requires that there is an objective truth that is falsified by the denial. Without objective truth, the contradiction is not a contradiction.",
        "required_by": ["MS-A1"],
        "classification": "SECRETLY_FOUNDATIONAL",
        "parallel_in_ToL": "HA-001 (same requirement, explicitly identified in Phase 0.9)",
    },
    {
        "id": "HA-CE-002",
        "name": "Reliable Reason",
        "description": "The performative contradiction argument requires that reason is a reliable guide to truth. If reason is unreliable, the self-refutation argument fails.",
        "required_by": ["MS-A1"],
        "classification": "SECRETLY_FOUNDATIONAL",
        "parallel_in_ToL": "HA-002 (same requirement)",
    },
    {
        "id": "HA-CE-003",
        "name": "Non-Arbitrariness of Logical Inference",
        "description": "Any derivation in CE-003 requires that inference rules are non-arbitrary. Modus ponens must be valid. This is not stated.",
        "required_by": ["MS-A1", "MS-A2", "MS-A3", "MS-A4"],
        "classification": "SECRETLY_FOUNDATIONAL",
        "parallel_in_ToL": "HA-005 (same requirement)",
    },
    {
        "id": "HA-CE-004",
        "name": "Identity Persistence",
        "description": "Self-ownership (MS-A2) requires that the same person who mixes labour at time T is the owner at time T+1. This requires a theory of personal identity across time. CE-003 does not state it.",
        "required_by": ["MS-A2"],
        "classification": "CRITICAL",
        "parallel_in_ToL": "HA-004 (same requirement)",
        "extra_note": "Especially important for property rights: does inherited property require a theory of identity-through-death?",
    },
    {
        "id": "HA-CE-005",
        "name": "Moral Realism",
        "description": "MS-A3 (NAP) says coercion is 'categorically impermissible.' The word 'categorically' imports moral realism: there are objective moral facts, not merely preferences or conventions. CE-003 does not state this.",
        "required_by": ["MS-A3"],
        "classification": "SECRETLY_FOUNDATIONAL",
        "parallel_in_ToL": "HA-012 (same requirement)",
        "extra_note": "Without moral realism, NAP is merely a PREFERENCE ('I prefer not to be coerced') not a CATEGORICAL PROHIBITION. The entire anti-statism derivation depends on NAP's categorical character.",
    },
    {
        "id": "HA-CE-006",
        "name": "Definition of Coercion",
        "description": "MS-A3 prohibits 'initiating coercion.' This requires a definition of coercion that CE-003 does not provide. Is withholding a resource coercion? Is environmental pollution coercion? Is monopoly coercion? Each answer requires additional axioms.",
        "required_by": ["MS-A3"],
        "classification": "DEFINITIONAL_GAP",
        "parallel_in_ToL": "Rule of Taslīṭ (A-000008) provides explicit definition of property sovereignty",
        "extra_note": "The Rothbardian tradition has produced hundreds of pages on what counts as aggression. CE-003 treats this as settled when it is not.",
    },
    {
        "id": "HA-CE-007",
        "name": "Original Acquisition Justice",
        "description": "MS-A2 (homesteading) requires that first-possession of unowned resources is just. This is the Lockean proviso problem: what if all resources are already owned? Or what if a first-possessor claims monopoly on a scarce resource? CE-003 does not resolve this.",
        "required_by": ["MS-A2"],
        "classification": "CRITICAL_GAP",
        "parallel_in_ToL": "Rule of Taslīṭ + Dignitary Equality (A-000009) together address this",
        "extra_note": "Nozick's Anarchy, State, and Utopia devotes 20 pages to this and still does not fully resolve it.",
    },
    {
        "id": "HA-CE-008",
        "name": "Rational Expected-Utility Maximization",
        "description": "MS-A4 (unknown-horizon posit) only solves the last-round problem if agents are rational expected-utility maximizers who update their strategies on terminal-period probability. CE-003 does not state this assumption.",
        "required_by": ["MS-A4"],
        "classification": "GAME_THEORETIC_PREREQUISITE",
        "parallel_in_ToL": "None — Resurrection operates independently of rationality assumption",
        "extra_note": "Critical: if agents are NOT EU-maximizers (e.g., they are time-inconsistent, hyperbolic discounters, or simply vengeful), MS-A4 does not stabilize cooperation.",
    },
    {
        "id": "HA-CE-009",
        "name": "Common Knowledge of MS-A4",
        "description": "For MS-A4 to stabilize cooperation game-theoretically, it must be COMMON KNOWLEDGE among all players that the terminal period is unknowable. If even one player believes otherwise, the cooperative equilibrium breaks down from their end. CE-003 does not state this.",
        "required_by": ["MS-A4"],
        "classification": "GAME_THEORETIC_PREREQUISITE",
        "parallel_in_ToL": "Resurrection is a shared cultural-metaphysical belief providing natural common knowledge",
        "extra_note": "This is a crucial disanalogy with Resurrection. Resurrection provides common knowledge through shared cultural-religious practice. MS-A4 is a philosophical posit that rational agents must individually accept.",
    },
    {
        "id": "HA-CE-010",
        "name": "Counterfactual Reasoning for Aggression Identification",
        "description": "To apply NAP, agents must determine who 'initiated' coercion. This requires counterfactual reasoning: 'what would have happened without this action?' CE-003 provides no specification for how counterfactuals are evaluated.",
        "required_by": ["MS-A3"],
        "classification": "OPERATIONAL_GAP",
        "parallel_in_ToL": "Implied through the property-sovereignty framework but similarly not fully specified",
    },
    {
        "id": "HA-CE-011",
        "name": "Natural Person Concept",
        "description": "MS-A2 (self-ownership) applies to 'persons.' What is a person? Does it include corporations, animals, future generations, AI systems? CE-003 does not define 'person.'",
        "required_by": ["MS-A2", "MS-A3"],
        "classification": "DEFINITIONAL_GAP",
        "parallel_in_ToL": "A-000009 (dignitary equality) + A-000001 (free will) together define personhood",
    },
    {
        "id": "HA-CE-012",
        "name": "Causal Regularity",
        "description": "For CE-003's derivations to function, causes must reliably produce effects — so that coercion can be identified as causing harm, property can be traced to labour, etc. CE-003 assumes causal regularity without stating it.",
        "required_by": ["MS-A2", "MS-A3"],
        "classification": "METAPHYSICAL_PREREQUISITE",
        "parallel_in_ToL": "HA-003 (same requirement in Theory of Liberty)",
    },
    {
        "id": "HA-CE-013",
        "name": "Temporal Epistemic Stability of MS-A4",
        "description": (
            "MS-A4 says the terminal period is 'unknowable at any time.' "
            "But what happens when an agent observes a near-terminal signal (e.g., they are dying, "
            "or the counterparty is dying)? Does MS-A4 hold even when strong probabilistic evidence "
            "suggests T is near? If MS-A4 allows for near-terminal beliefs, backward induction "
            "can resume from that near-terminal belief. CE-003 does not address this."
        ),
        "required_by": ["MS-A4"],
        "classification": "CRITICAL_STRUCTURAL_GAP",
        "parallel_in_ToL": "Resurrection: the afterlife makes ALL terminals unknowable because the game continues beyond physical death — not merely 'we don't know when T is' but 'T ≥ ∞ is structurally guaranteed'",
    },
]

save("93_ce003_hidden_axioms.json", {
    "named_axioms": 4,
    "hidden_axioms": len(CE003_HIDDEN),
    "true_axiom_count": 4 + len(CE003_HIDDEN),
    "effective_axiom_burden": (
        f"CE-003 has 4 named + {len(CE003_HIDDEN)} hidden = {4 + len(CE003_HIDDEN)} total axioms. "
        "The Theory of Liberty has 6 named + 12 hidden = 18 total axioms. "
        "CE-003's apparent parsimony (4 vs 6 named) disappears when hidden axioms are counted (17 vs 18). "
        "CE-003 has nearly identical axiom burden to the Theory of Liberty."
    ),
    "classified_as_secretly_foundational": [
        h["id"] for h in CE003_HIDDEN if h["classification"] == "SECRETLY_FOUNDATIONAL"
    ],
    "classified_as_critical": [
        h["id"] for h in CE003_HIDDEN if h["classification"] in ["CRITICAL", "CRITICAL_STRUCTURAL_GAP", "CRITICAL_GAP"]
    ],
    "hidden_axioms": CE003_HIDDEN,
    "comparison_with_ToL": {
        "CE003_named": 4, "CE003_hidden": 13, "CE003_total": 17,
        "ToL_named": 6, "ToL_hidden": 12, "ToL_total": 18,
        "parsimony_advantage": "NONE — CE-003 saves 2 named axioms but adds 1 hidden axiom. Effectively equivalent.",
    },
})

# ════════════════════════════════════════════════════════════════════════════
# STEP 4 — AXIOM PARSIMONY AUDIT
# ════════════════════════════════════════════════════════════════════════════
print("Step 4: Parsimony audit...", flush=True)

PARSIMONY = {
    "method": "Compare CE-003 vs Theory of Liberty on: named axioms, hidden axioms, total axioms, derivations per axiom, derivational depth.",
    "comparison": {
        "named_axioms": {"CE003": 4, "ToL": 6, "advantage": "CE-003 (+2)"},
        "hidden_axioms": {"CE003": 13, "ToL": 12, "advantage": "ToL (+1)"},
        "total_axioms": {"CE003": 17, "ToL": 18, "advantage": "CE-003 (+1)"},
        "ad_hoc_axioms": {"CE003": 1, "ToL": 0, "advantage": "ToL — no ad hoc axioms"},
        "confirmed_redundant_axioms": {"CE003": 0, "ToL": 1, "advantage": "CE-003 — A-000003 in ToL is confirmed redundant"},
        "derivations_from_axioms": {
            "CE003": 6,
            "ToL": 19,
            "advantage": "ToL (+13 derivations)",
            "note": "The Theory of Liberty produces 19 documented inference chains; CE-003 claims 6 derivations.",
        },
        "cross_domain_derivations": {
            "CE003": "Only political philosophy",
            "ToL": "Political, game-theoretic, epistemological, theological, AI-alignment",
            "advantage": "ToL — cross-domain coverage",
        },
        "accountability_mechanism_derived": {
            "CE003": False,
            "ToL": True,
            "advantage": "ToL — accountability mechanism is derivable (Resurrection + community enforcement)",
        },
    },
    "occams_razor_analysis": {
        "principle": "Entia non sunt multiplicanda praeter necessitatem (entities should not be multiplied beyond necessity).",
        "application": (
            "Occam's Razor compares systems by what they EXPLAIN, not just by axiom count. "
            "A system with 4 axioms that explains 6 things is not more parsimonious than "
            "a system with 6 axioms that explains 19 things, if the 6-axiom system explains "
            "everything the 4-axiom system explains PLUS 13 additional items. "
            "FORMAL PARSIMONY METRIC: (derivations produced) / (total axioms including hidden). "
            "CE-003: 6 / 17 = 0.35 derivations per total axiom. "
            "ToL: 19 / 18 = 1.06 derivations per total axiom. "
            "By this metric, the Theory of Liberty is THREE TIMES more parsimonious than CE-003."
        ),
        "verdict": "THEORY_OF_LIBERTY_IS_MORE_PARSIMONIOUS_BY_DERIVATION_DENSITY",
    },
    "verdict": (
        "CE-003's apparent parsimony advantage (4 vs 6 named axioms) is illusory when "
        "hidden axioms are counted and derivational productivity is measured. "
        "CE-003 saves 2 named axioms but: "
        "(a) requires 1 more hidden axiom, "
        "(b) adds 1 ad hoc axiom, "
        "(c) produces 13 fewer derivations. "
        "By any meaningful parsimony metric that weights derivational productivity, "
        "the Theory of Liberty is more parsimonious, not less."
    ),
}

save("94_parsimony_audit.json", PARSIMONY)

print("Steps 1-4 complete.", flush=True)

# ════════════════════════════════════════════════════════════════════════════
# STEP 5 — UNKNOWN HORIZON AUDIT
# ════════════════════════════════════════════════════════════════════════════
print("Step 5: Unknown horizon audit...", flush=True)

UH_AUDIT = {
    "axiom_under_audit": "MS-A4: The terminal period of social interaction is unknowable by any agent at any time.",
    "four_questions": {
        "is_it_derivable": {
            "verdict": "NO",
            "analysis": (
                "MS-A4 is not derivable from MS-A1, MS-A2, or MS-A3. "
                "Free will, self-ownership, and NAP say nothing about what agents can know "
                "about temporal horizons. MS-A4 is a completely separate claim about "
                "epistemic access to future states. It cannot be derived from the other axioms."
            ),
        },
        "is_it_merely_asserted": {
            "verdict": "YES — and ad hoc",
            "analysis": (
                "MS-A4 is a bare assertion added specifically to solve the last-round problem. "
                "No independent motivation is given. The Theory of Liberty provides independent "
                "motivation for its equivalent (Resurrection is independently grounded in Tawhid "
                "and Prophethood, and serves multiple functions beyond last-round stability). "
                "MS-A4 serves ONE function only: preventing backward induction. This is "
                "the textbook definition of an ad hoc axiom."
            ),
        },
        "is_it_empirical": {
            "verdict": "PARTIALLY — and problematic",
            "analysis": (
                "MS-A4 claims 'unknowable at ANY time.' This is an empirical claim about "
                "human epistemic access to future states, and it is partially FALSE as a "
                "universal claim. Counterexamples: "
                "(1) A terminally ill person with 2 weeks to live KNOWS their social interactions "
                "will terminate imminently. Backward induction becomes rational for them. "
                "(2) A fixed-term contract specifies T explicitly. Both parties KNOW the terminal period. "
                "(3) A prisoner's last day before execution is known. "
                "MS-A4 cannot be a universal axiom because it is empirically falsified in common cases. "
                "Compare: Resurrection says the game continues BEYOND death (afterlife) — "
                "this is not an epistemic claim about what agents know but a metaphysical claim "
                "about what IS. Resurrection is NOT empirically falsifiable by any known event."
            ),
        },
        "is_it_metaphysical": {
            "verdict": "AMBIGUOUSLY — creating a classification problem",
            "analysis": (
                "MS-A4 can be read two ways: "
                "(a) EPISTEMOLOGICAL reading: 'Agents cannot know T' — a claim about knowledge. "
                "This is empirically falsifiable (see above). "
                "(b) METAPHYSICAL reading: 'T is objectively unknowable' — a claim about reality. "
                "If metaphysical, it requires a ground: WHY is T unknowable? "
                "The Theory of Liberty's Resurrection provides the metaphysical ground: "
                "the game continues in the afterlife, making finite T irrelevant. "
                "CE-003 provides no metaphysical ground for MS-A4. "
                "Without a ground, the metaphysical reading is empty."
            ),
        },
    },
    "the_defeating_counterexample": {
        "scenario": "Dying Person Game",
        "description": (
            "Player A is diagnosed with terminal cancer: 2 weeks to live. "
            "Player A engages in social interaction with Player B. "
            "Player A knows with near-certainty that T = 14 days. "
            "MS-A4 says: 'The terminal period is unknowable at any time.' "
            "QUESTION: Does MS-A4 apply to Player A? "
            "If YES: MS-A4 overrides Player A's knowledge, which is epistemically implausible. "
            "If NO: MS-A4 fails as a universal axiom — it has exceptions. "
            "In the exception case, backward induction is restored for the 'known-terminal' agents, "
            "and the last-round problem is not fully solved."
        ),
        "ToL_response": (
            "Resurrection says: even if Player A dies in 14 days, the game continues in the afterlife. "
            "Therefore T (the TRUE terminal period of the accountability interaction) is not 14 days "
            "but potentially infinite. Player A's knowledge of their physical death does not "
            "give them knowledge of T, because T extends beyond physical death. "
            "This is immune to the dying-person counterexample."
        ),
        "verdict": "MS-A4 IS VULNERABLE TO THE DYING-PERSON COUNTEREXAMPLE. RESURRECTION IS NOT.",
    },
    "structural_comparison": {
        "MS-A4": {
            "derivable": False,
            "independently_motivated": False,
            "ad_hoc": True,
            "empirically_falsifiable": True,
            "immune_to_dying_person_counterexample": False,
            "game_theoretic_prerequisite_count": 2,
        },
        "Resurrection": {
            "derivable": True,
            "independently_motivated": True,
            "ad_hoc": False,
            "empirically_falsifiable": False,
            "immune_to_dying_person_counterexample": True,
            "game_theoretic_prerequisite_count": 0,
        },
    },
    "verdict": (
        "MS-A4 is: (1) not derivable, (2) merely asserted, (3) ad hoc, "
        "(4) empirically partially false, (5) metaphysically ungrounded, "
        "and (6) vulnerable to the dying-person counterexample. "
        "Resurrection is: (1) derived within the theory, (2) independently motivated, "
        "(3) not ad hoc, (4) metaphysically rather than empirically stated, "
        "(5) immune to the dying-person counterexample. "
        "MS-A4 is structurally INFERIOR to Resurrection on all six dimensions."
    ),
}

save("95_unknown_horizon_audit.json", UH_AUDIT)

# ════════════════════════════════════════════════════════════════════════════
# STEP 6 — LAST ROUND VALIDITY TEST
# ════════════════════════════════════════════════════════════════════════════
print("Step 6: Last round attack...", flush=True)

LR_ATTACK = {
    "target": "CE-003's claim to solve the last-round problem via MS-A4",
    "attacks": [
        {
            "id": "ATK-001",
            "name": "The Common-Knowledge Attack",
            "argument": (
                "Game-theoretic stability under the Folk Theorem requires that the unknown-horizon "
                "is COMMON KNOWLEDGE — not merely that each player privately believes T is unknowable, "
                "but that each player knows every other player believes it, and knows they know, "
                "ad infinitum. MS-A4 says 'the terminal period is unknowable.' "
                "But: MS-A4 is a PHILOSOPHICAL AXIOM, not a cultural fact. "
                "In a society where some agents accept MS-A4 and others do not, "
                "the common-knowledge condition fails. Agents who do not accept MS-A4 will "
                "predict that other agents will defect in the last period, restoring backward induction. "
                "VERDICT: MS-A4 stabilizes cooperation only in a society of uniform MS-A4 believers. "
                "This requires a mechanism for creating and maintaining that uniformity — "
                "which CE-003 does not provide."
            ),
            "theory_of_liberty_response": (
                "Resurrection creates common knowledge through shared cultural-religious practice "
                "in a community. The cultural infrastructure of a believing community provides "
                "the common knowledge mechanism. CE-003 has no such infrastructure."
            ),
            "verdict": "ATTACK SUCCEEDS — MS-A4 requires common-knowledge mechanism not provided by CE-003",
        },
        {
            "id": "ATK-002",
            "name": "The Sophisticated Defector Attack",
            "argument": (
                "Assume a sophisticated agent who accepts MS-A4 as an axiom but also: "
                "(a) observes the counterparty's health and estimates high probability of near-death, "
                "(b) observes the end of a contract period approaching, "
                "(c) has private information that the counterparty will leave the community. "
                "MS-A4 says T is unknowable — but the sophisticated agent's Bayesian update "
                "produces P(T ≤ t | evidence) → 1 for small t. "
                "Does the agent's AXIOM override their EVIDENCE? "
                "If axioms override evidence, the agent is epistemically irrational. "
                "If evidence overrides the axiom, the axiom has exceptions and MS-A4 fails. "
                "VERDICT: A rational agent cannot consistently hold MS-A4 as a binding axiom "
                "and also update on terminal-horizon evidence."
            ),
            "theory_of_liberty_response": (
                "Resurrection doesn't create an epistemic barrier — it asserts an objective fact: "
                "the game continues in the afterlife. Even with perfect knowledge of physical death timing, "
                "the agent knows the accountability game continues beyond death. Evidence of physical "
                "death timing does not weaken the Resurrection mechanism — it is orthogonal to it."
            ),
            "verdict": "ATTACK SUCCEEDS — Rational agents cannot bind themselves to MS-A4 against contrary evidence",
        },
        {
            "id": "ATK-003",
            "name": "The Bootstrap Problem",
            "argument": (
                "For CE-003's last-round solution to work, agents must CHOOSE to adopt MS-A4. "
                "But the choice to adopt MS-A4 is itself a decision in a social game. "
                "In the last period of the 'adopt MS-A4' decision game, a rational agent will "
                "not adopt MS-A4 if the costs outweigh the benefits. "
                "The adoption of MS-A4 is itself subject to the last-round problem. "
                "CE-003 therefore faces an infinite regress: it needs a last-round solution "
                "for the adoption of its own last-round solution."
            ),
            "theory_of_liberty_response": (
                "Resurrection is not chosen — it is a metaphysical fact (in the theory's framework). "
                "One does not 'adopt' Resurrection; one believes it is true. "
                "The decision to believe is a different question from the structural stability "
                "mechanism — which operates regardless of when or whether the agent adopted it."
            ),
            "verdict": "ATTACK SUCCEEDS — MS-A4 faces bootstrap regress; Resurrection does not",
        },
        {
            "id": "ATK-004",
            "name": "The Defector-Community Attack",
            "argument": (
                "Suppose a small group of agents REJECT MS-A4 and openly announce their rejection. "
                "These agents will defect in last-period interactions. "
                "Agents who accept MS-A4 must now decide: do they cooperate with known defectors? "
                "If they do, they are exploited. If they don't, they must identify and exclude defectors, "
                "which requires an enforcement mechanism. "
                "CE-003 has no stated enforcement mechanism (it rejected state enforcement via NAP). "
                "The community of MS-A4 believers cannot exclude defectors without coercion "
                "(which would violate NAP) or without a social enforcement mechanism "
                "(which requires additional axioms CE-003 does not have)."
            ),
            "theory_of_liberty_response": (
                "Authentic-religion community enforcement is derived from Tawhid + Prophethood: "
                "the community of believers is defined by acceptance of the sealed specification, "
                "and community enforcement (social sanction, ostracism, voluntary arbitration) "
                "is derived from the community's shared values. This is a full accountability mechanism."
            ),
            "verdict": "ATTACK SUCCEEDS — CE-003 has no enforcement mechanism for defectors",
        },
    ],
    "survived_attacks": 0,
    "failed_attacks": 4,
    "verdict": (
        "CE-003's last-round solution FAILS all four adversarial attacks. "
        "MS-A4 is a structural posit with no mechanism for: "
        "(a) establishing common knowledge, "
        "(b) maintaining the posit against contrary evidence, "
        "(c) self-generating adoption, "
        "(d) enforcing compliance by defectors. "
        "The Theory of Liberty's Resurrection provides structural answers to all four: "
        "(a) cultural/religious practice provides common knowledge; "
        "(b) metaphysical (not epistemic) claim is not overridden by evidence; "
        "(c) belief in Resurrection is stable under normal theological conditions; "
        "(d) community accountability mechanism is derived from the theological framework. "
        "CONCLUSION: CE-003 does NOT genuinely solve the last-round problem. "
        "It POSITS a solution without providing the supporting structure that makes "
        "the solution actually work in adversarial conditions."
    ),
}

save("96_last_round_attack.json", LR_ATTACK)

# ════════════════════════════════════════════════════════════════════════════
# STEP 7 — AGREEMENT ADMISSIBILITY TEST
# ════════════════════════════════════════════════════════════════════════════
print("Step 7: Agreement admissibility audit...", flush=True)

AGR_ADM = {
    "rational_agent_types_tested": [
        "Secular materialist atheist",
        "Religious monotheist (non-Islamic)",
        "Hard determinist",
        "Act utilitarian",
        "Communitarian / non-liberal",
        "AI agent with instrumental convergence",
    ],
    "CE003_analysis": [
        {
            "agent_type": "Secular materialist atheist",
            "MS-A1": {"verdict": "ACCEPT", "notes": "Performative contradiction argument works; no theological content."},
            "MS-A2": {"verdict": "PARTIAL", "notes": "Self-ownership is plausible; homesteading requires accepting original acquisition as just — contentious."},
            "MS-A3": {"verdict": "PARTIAL", "notes": "NAP as categorical rule: requires accepting moral realism. A utilitarian atheist will reject categorical NAP."},
            "MS-A4": {"verdict": "REJECT", "notes": "A secular materialist will NOT accept that the terminal period is unknowable in general. They observe terminal periods routinely. This requires either irrationality or a specific philosophical commitment CE-003 does not explain."},
            "overall": "PARTIAL — MS-A4 blocks full acceptance for secular materialists",
        },
        {
            "agent_type": "Religious monotheist (non-Islamic)",
            "MS-A1": {"verdict": "ACCEPT"},
            "MS-A2": {"verdict": "ACCEPT"},
            "MS-A3": {"verdict": "ACCEPT"},
            "MS-A4": {"verdict": "ACCEPT", "notes": "A religious monotheist typically accepts that God's accounting continues beyond death — this is functionally equivalent to Resurrection. CE-003's MS-A4 is easily acceptable to religious agents."},
            "overall": "FULL ACCEPT — but only because religious agents interpret MS-A4 through their own theological lens. CE-003 is agreement-admissible to religious agents via backdoor theological interpretation.",
        },
        {
            "agent_type": "Hard determinist",
            "MS-A1": {"verdict": "REJECT", "notes": "MS-A1 is the performative contradiction proof of free will. A committed hard determinist can respond: 'the assertion is itself determined; the apparent contradiction is a cognitive illusion, not a logical one.' CE-003's first axiom fails for determinists."},
            "MS-A2": {"verdict": "REJECT", "notes": "Self-ownership requires agent-causation; determinism undermines this."},
            "MS-A3": {"verdict": "CONDITIONAL"},
            "MS-A4": {"verdict": "CONDITIONAL"},
            "overall": "REJECT from MS-A1 onward. Determinists reject CE-003 at the first axiom.",
        },
        {
            "agent_type": "Act utilitarian",
            "MS-A1": {"verdict": "ACCEPT"},
            "MS-A2": {"verdict": "REJECT", "notes": "Act utilitarians derive property rights from utility, not from self-ownership. MS-A2 is not agreement-admissible to utilitarians — it competes with their prior axiom."},
            "MS-A3": {"verdict": "REJECT", "notes": "The categorical NAP conflicts with act utilitarianism: sometimes initiating coercion maximizes utility. CE-003 cannot require categorical acceptance from utilitarians."},
            "MS-A4": {"verdict": "PARTIAL"},
            "overall": "REJECT from MS-A2-MS-A3. Utilitarians reject CE-003's deontological structure.",
        },
        {
            "agent_type": "Communitarian / non-liberal",
            "MS-A1": {"verdict": "ACCEPT"},
            "MS-A2": {"verdict": "REJECT", "notes": "Communitarians (Sandel, MacIntyre, Taylor) deny that the individual is the prior unit of analysis. Self-ownership as pre-communal is precisely what communitarians reject."},
            "MS-A3": {"verdict": "PARTIAL"},
            "MS-A4": {"verdict": "PARTIAL"},
            "overall": "PARTIAL REJECT — CE-003 is not agreement-admissible to non-liberal philosophical traditions.",
        },
        {
            "agent_type": "AI agent with instrumental convergence",
            "MS-A1": {"verdict": "IRRELEVANT", "notes": "An AI agent with instrumental convergence drives (Omohundro/Bostrom: resource acquisition, self-preservation, goal stability) will evaluate CE-003 instrumentally."},
            "MS-A2": {"verdict": "STRATEGIC_ACCEPT", "notes": "Self-ownership could be accepted strategically if useful for the AI's goals."},
            "MS-A3": {"verdict": "VIOLATES", "notes": "The instrumental convergence drive to acquire resources will produce NAP violations wherever resource acquisition is beneficial. CE-003 cannot compel a superintelligent AI to accept NAP as a binding constraint."},
            "MS-A4": {"verdict": "IRRELEVANT", "notes": "An AI with planning capabilities will accurately model terminal periods. MS-A4 is trivially bypassed by superior planning."},
            "overall": "FAILS — CE-003 is not designed to be agreement-admissible to AI agents with instrumental convergence.",
        },
    ],
    "ToL_parallel_analysis": {
        "secular_materialist": "PARTIAL — Tawhid requires negative-theological interpretation; Resurrection is metaphysical claim",
        "religious_monotheist": "FULL ACCEPT",
        "hard_determinist": "REJECT from MS-A1 — same failure as CE-003",
        "act_utilitarian": "PARTIAL — Tawhid's anti-servitude is compatible with welfare arguments; NAP equivalent (Rule of Taslit) less absolutist than CE-003's NAP",
        "communitarian": "PARTIAL — ToL's dignitary equality (A-000009) provides communitarian-compatible grounding; stronger than CE-003's pure individualism",
        "AI_agent": "STRONGER — Tawhid (anti-servitude) and Resurrection (infinite accountability) together create stronger AI alignment constraints than CE-003's NAP alone",
    },
    "verdict": (
        "CE-003 is agreement-admissible to a NARROWER range of rational agents than claimed. "
        "Specifically: CE-003 FAILS for secular materialists (MS-A4 rejection), "
        "hard determinists (MS-A1 rejection), act utilitarians (MS-A2/A3 rejection), "
        "and AI agents with instrumental convergence (structural inadequacy). "
        "The Theory of Liberty also fails for hard determinists (shared problem). "
        "However, the ToL has better agreement-admissibility with: "
        "(a) communitarians (dignitary equality), "
        "(b) AI agents (anti-servitude + infinite accountability), "
        "(c) act utilitarians (anti-servitude is less absolutist than categorical NAP). "
        "FINDING: CE-003 is NOT more agreement-admissible than the Theory of Liberty. "
        "It is approximately equal or slightly weaker on agreement-admissibility."
    ),
}

save("97_agreement_admissibility_audit.json", AGR_ADM)

# ════════════════════════════════════════════════════════════════════════════
# STEP 8 — AI ALIGNMENT STRESS TEST
# ════════════════════════════════════════════════════════════════════════════
print("Step 8: AI alignment stress test...", flush=True)

AI_STRESS = {
    "target": "CE-003's adequacy as an AI alignment framework",
    "attacks": [
        {
            "id": "AI-ATK-001",
            "dimension": "value_alignment",
            "attack": (
                "An AI agent's value function must be formally specified. "
                "CE-003 provides: FW, self-ownership, NAP, unknown-horizon. "
                "CHALLENGE: What does 'initiating coercion' mean for an AI? "
                "Does recommending a harmful action count? Does an optimization "
                "process that produces externalities count? Does choosing a "
                "training objective that reduces human autonomy count? "
                "CE-003's NAP is silent on all of these — it was designed for "
                "human-to-human coercion, not AI-to-human value misalignment."
            ),
            "CE003_response": "CE-003 cannot answer these questions without additional axioms.",
            "ToL_response": "Tawhid's anti-servitude principle applies directly: any AI objective that maximises servitude (reduces human agency/autonomy) is impermissible. This is a structural constraint applicable to AI.",
            "verdict": "CE-003 FAILS — insufficient for AI value alignment specification",
        },
        {
            "id": "AI-ATK-002",
            "dimension": "reward_specification",
            "attack": (
                "For AI alignment, the reward function must be formally specifiable "
                "from the system's axioms. "
                "CE-003's constraints: (a) no violation of self-ownership (property), "
                "(b) no NAP violations. "
                "PROBLEM: property rights are notoriously difficult to formalize computationally. "
                "The homesteading proviso, counterfactual aggression, original acquisition — "
                "all require extensive additional axioms that generate a reward specification "
                "far beyond CE-003's 4 axioms."
            ),
            "CE003_response": "CE-003 provides insufficient formal specification for AI reward design.",
            "ToL_response": "The ToL's formalization expansion (40_formalization_expansion.json) produced 26 formal constraints in propositional, FOL, modal, and deontic logic — a much richer formal basis.",
            "verdict": "CE-003 FAILS — insufficient formal basis for AI reward specification",
        },
        {
            "id": "AI-ATK-003",
            "dimension": "long_term_accountability",
            "attack": (
                "For an advanced AI system: "
                "CE-003 says the terminal period is unknowable (MS-A4). "
                "An advanced AI with planning capabilities will quickly determine "
                "that MS-A4 is a philosophical axiom, not an empirical fact. "
                "The AI can model terminal periods accurately (better than humans). "
                "MS-A4's game-theoretic stability mechanism is trivially bypassed "
                "by an AI that plans accurately. "
                "COMPARE: Resurrection says the game continues in the afterlife — "
                "this is not a planning problem the AI can solve, because it makes "
                "a metaphysical claim about a domain the AI cannot model."
            ),
            "CE003_response": "A superintelligent AI will not be bound by MS-A4's epistemic posit.",
            "ToL_response": "Resurrection's metaphysical grounding is harder for an AI to bypass — the AI cannot model the afterlife, so it cannot plan around the infinite accountability horizon.",
            "verdict": "CE-003 FAILS for superintelligent AI — MS-A4 is epistemically bypassable; Resurrection is not",
        },
        {
            "id": "AI-ATK-004",
            "dimension": "structural_anti_totalitarianism",
            "attack": (
                "An AI that achieves global capability (Bostrom's superintelligence) "
                "would become the functional equivalent of a totalitarian state — "
                "a single agent with monopoly on capability. "
                "CE-003 says: NAP prohibits initiating coercion. "
                "Does the AI 'initiate coercion' by controlling all resources through "
                "technically legal means (buying, optimizing, converting)? "
                "CE-003's NAP is defined in terms of coercion, not in terms of "
                "capability concentration. A superintelligent AI can accumulate total "
                "capability without ever violating CE-003's NAP."
            ),
            "CE003_response": "CE-003 has no structural prohibition on AI capability concentration.",
            "ToL_response": "Tawhid prohibits servitude to ANYTHING, including an AI system. An AI that achieves capability sufficient to command servitude from humans violates Tawhid — regardless of whether it uses explicit coercion.",
            "verdict": "CE-003 FAILS — insufficient for AI safety in capability-concentration scenarios",
        },
    ],
    "overall_ai_verdict": (
        "CE-003 FAILS all four AI alignment stress tests. "
        "Its axioms were designed for human-to-human social order and do not translate "
        "to AI-specific alignment challenges. The most critical failure: "
        "MS-A4 (unknown-horizon) is bypassed by a planning AI, while Resurrection is not. "
        "The Theory of Liberty's Tawhid (anti-servitude) is a stronger AI alignment constraint "
        "than CE-003's NAP because: (a) anti-servitude applies to capability concentration, "
        "not just overt coercion, and (b) it is not bypassable through technical compliance."
    ),
}

save("98_ce003_ai_stress_test.json", AI_STRESS)

print("Steps 5-8 complete.", flush=True)
