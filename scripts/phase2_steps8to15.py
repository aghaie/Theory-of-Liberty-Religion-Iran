#!/usr/bin/env python3
"""Phase 2 Steps 8-15: Free Will Necessity, Last-Round Audit, AI Uniqueness,
Minimum Counterexample, Steelman, Refutation, Final Verdict, Scorecard, README."""

import json, os
from datetime import date

KB = "/Users/ali/Documents/GitHub/Theory-of-Liberty-Religion-Iran/knowledge_base"

def L(p): return json.load(open(p, encoding="utf-8"))
def save(name, obj):
    for p in [f"/tmp/{name}", f"{KB}/{name}"]:
        json.dump(obj, open(p,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"  Saved: {name}", flush=True)

print("Phase 2 (steps 8-15) loaded.", flush=True)

# Load prior results
ce_data  = L(f"{KB}/76_counterexamples.json")
comp_res = L(f"{KB}/75_competitor_results.json")
theo_aud = L(f"{KB}/77_theological_necessity_audit.json")

# ════════════════════════════════════════════════════════════════════════════
# STEP 8 — FREE WILL NECESSITY AUDIT
# ════════════════════════════════════════════════════════════════════════════
print("\nStep 8: Free will necessity audit...", flush=True)

FW_AUDIT = {
    "question": "Can a competing system function without libertarian free will?",
    "method": "Test each major non-libertarian-free-will alternative; evaluate structural coverage of required properties.",
    "alternatives_tested": [
        {
            "name": "Hard Determinism",
            "axiom": "All events including human choices are causally determined by prior states.",
            "function_test": {
                "C1_consistent": True,
                "C3_grounds_liberty": False,
                "reasoning": (
                    "Hard determinism cannot coherently ground NORMATIVE liberty. "
                    "If all choices are determined, the distinction between coerced and voluntary "
                    "action dissolves at the metaphysical level. You can maintain LEGAL freedom "
                    "(not interfered with) but not MORAL freedom (genuinely choosing). "
                    "Property rights under determinism become: 'the state has decreed this assignment' — "
                    "there is no prior natural right because there is no prior natural choice. "
                    "The theory's C-000039 (performative contradiction) applies: asserting determinism "
                    "is itself self-refuting (the assertion would be determined, not reasoned). "
                    "VERDICT: Hard determinism cannot ground the theory's requirements. "
                    "It is self-refuting and cannot derive normative liberty."
                ),
            },
            "verdict": "STRUCTURALLY_INCOMPATIBLE",
        },
        {
            "name": "Compatibilism (Frankfurt, Dennett)",
            "axiom": "Free will is compatible with determinism: free action = action caused by one's own desires/reasons, not external constraint.",
            "function_test": {
                "C1_consistent": True,
                "C3_grounds_liberty": "PARTIAL",
                "reasoning": (
                    "Compatibilism is the dominant philosophical position and is structurally more viable. "
                    "Under compatibilism: free action = action caused by agent's own desires = not coerced. "
                    "This CAN ground a notion of liberty: liberty is absence of external constraint on "
                    "one's own desire-caused actions. "
                    "HOWEVER: compatibilism does not ground the Theory of Liberty's STRONG notion of "
                    "property rights as pre-political. If all desires are determined, there is no "
                    "'natural' right — only socially-determined preferences for property. "
                    "Compatibilism grounds a PROCEDURAL liberty (not-coerced) but not a NATURAL RIGHTS "
                    "liberty (prior to social determination). "
                    "The performative contradiction argument still applies (claiming determinism "
                    "as REASONED conclusion presupposes reasoning = libertarian free will). "
                    "VERDICT: Partial compatibility. Grounds procedural liberty but not natural rights liberty."
                ),
            },
            "verdict": "PARTIAL_COMPATIBILITY",
        },
        {
            "name": "Agent Causation (O'Connor, Taylor)",
            "axiom": "Agents are irreducible causal sources that initiate action without being fully determined by prior states.",
            "function_test": {
                "C1_consistent": True,
                "C3_grounds_liberty": True,
                "reasoning": (
                    "Agent causation is functionally equivalent to the Theory of Liberty's free will axiom. "
                    "Agent causation provides: genuine (not-determined) origination of action → normative "
                    "responsibility → property rights → liberty. "
                    "This is effectively a secular restatement of A-000001. "
                    "VERDICT: Functionally equivalent. Agent causation and libertarian free will are "
                    "structurally identical for the theory's purposes."
                ),
            },
            "verdict": "FUNCTIONAL_EQUIVALENT",
        },
        {
            "name": "Moral Responsibility Without Free Will (Strawson)",
            "axiom": "Reactive attitudes (resentment, gratitude) constitute moral responsibility; metaphysical free will is unnecessary.",
            "function_test": {
                "C1_consistent": True,
                "C3_grounds_liberty": "PARTIAL",
                "reasoning": (
                    "Strawson's approach grounds moral responsibility in human practices. "
                    "It can ground liberty as a social norm: 'we collectively hold each other responsible, "
                    "therefore we collectively protect individual liberty.' "
                    "HOWEVER: this is a sociological, not logical, grounding. "
                    "It cannot provide NATURAL property rights prior to social determination. "
                    "The theory requires a normative foundation prior to social practice. "
                    "VERDICT: Grounds social liberty; cannot ground natural rights liberty."
                ),
            },
            "verdict": "INSUFFICIENT_GROUNDING",
        },
    ],
    "performative_contradiction_applies": True,
    "performative_contradiction_analysis": (
        "The theory's A-000001 is unique among competing systems in having a SELF-REFUTATION defense: "
        "any system that denies free will must use reasoning to deny it — but reasoning presupposes "
        "the freedom to reason, which is libertarian free will. "
        "This means: "
        "(1) Hard determinism and pure compatibilism cannot consistently argue against free will — "
        "their own arguments for their positions presuppose the free will they deny. "
        "(2) Agent causation is a restatement of the same insight. "
        "(3) Strawson's approach sidesteps the issue but cannot provide pre-political rights. "
        "CONCLUSION: Libertarian free will (or its agent-causation equivalent) is PRACTICALLY "
        "NECESSARY for a consistent normative system grounding natural rights. "
        "Any system that uses normative argument at all is implicitly committed to A-000001."
    ),
    "verdict": (
        "FREE WILL IS PRACTICALLY NECESSARY: any normative system that uses arguments to ground "
        "rights and liberty is implicitly committed to free will (or its functional equivalent). "
        "This does not mean 'Tawhid is necessary' — it means A-000001 is the broadest available "
        "grounding for liberty and is presupposed by all competing normative systems that make "
        "normative claims. The Theory of Liberty's advantage: it explicitly states what others "
        "hide as a hidden axiom."
    ),
}

save("78_free_will_necessity_audit.json", FW_AUDIT)

# ════════════════════════════════════════════════════════════════════════════
# STEP 9 — LAST ROUND PROBLEM AUDIT
# ════════════════════════════════════════════════════════════════════════════
print("Step 9: Last round problem audit...", flush=True)

LAST_ROUND = {
    "problem_statement": (
        "In finitely repeated games, backward induction produces defection in every period. "
        "If the terminal period T is known, a rational agent defects at T (no future consequence). "
        "By induction, defection is rational at T-1, T-2, ..., 1. "
        "For cooperative social institutions (contracts, property rights, rule of law) to be stable, "
        "the last-round problem must be structurally resolved."
    ),
    "theory_solution": (
        "A-000006 (Resurrection): the terminal period of social interaction is unknowable because "
        "the afterlife continues accountability indefinitely. This makes T effectively ∞. "
        "Formally: E[U(cooperate)] > E[U(defect)] for all finite T if P(continuation | defect) > 0 "
        "and the accountability mechanism extends beyond the game's visible horizon."
    ),
    "competitor_solutions": [
        {
            "system": "Classical Liberalism",
            "proposed_solution": "Constitutional constraints + reputational effects",
            "adequacy": "FAILS",
            "analysis": (
                "Constitutional constraints are enforced by state courts. In the last period, "
                "the enforcement mechanism itself faces the last-round problem (who enforces the enforcer?). "
                "Reputational effects require future interaction — which terminates in the last period. "
                "VERDICT: Institutional solution that is itself subject to the last-round problem."
            ),
        },
        {
            "system": "Rothbardian Libertarianism",
            "proposed_solution": "Self-ownership + reputation + voluntary arbitration",
            "adequacy": "FAILS",
            "analysis": (
                "Same failure mode as classical liberalism for reputation effects. "
                "Self-ownership is a rights claim, not a stability mechanism. "
                "Rothbard has no structural response to the last-round problem — this is well-known "
                "in libertarian scholarship. "
                "VERDICT: Does not solve last-round problem."
            ),
        },
        {
            "system": "Kantian Ethics",
            "proposed_solution": "Categorical imperative: compliance is rational regardless of consequences",
            "adequacy": "PARTIAL",
            "analysis": (
                "The CI requires compliance regardless of strategic consequences. "
                "A Kantian agent complies in the last period because duty is not conditional on outcomes. "
                "HOWEVER: this requires prior commitment to Kantian ethics. "
                "In a game-theoretic analysis: a purely strategic rational agent, not committed to Kantian "
                "ethics, defects in the last period even when interacting with Kantians. "
                "The CI solves the last-round problem for Kantians interacting with Kantians; "
                "it does not solve it for the general population. "
                "VERDICT: Partial — requires homogeneous Kantian adoption, which is itself a coordination problem."
            ),
        },
        {
            "system": "Social Contractarianism",
            "proposed_solution": "Rational commitment to social contract as self-interest",
            "adequacy": "FAILS",
            "analysis": (
                "Hobbes's solution: the Leviathan enforces the contract. But the Leviathan faces "
                "the last-round problem itself — why does the Leviathan comply in its last period? "
                "Gauthier's solution: constrained maximization — pre-commit to cooperate when it's "
                "beneficial in the long run. But this requires knowing the discount factor is high enough. "
                "VERDICT: Hobbes relies on state coercion (re-introducing the problem); "
                "Gauthier requires conditional discount-factor argument."
            ),
        },
        {
            "system": "Secular Unknown-Horizon Posit (CE-003)",
            "proposed_solution": "Axiom 4: terminal period is unknowable by structural posit",
            "adequacy": "STRUCTURAL_EQUIVALENT",
            "analysis": (
                "CE-003's secular unknown-horizon posit directly mirrors Resurrection's function. "
                "Both make T unknowable, preventing backward induction. "
                "DIFFERENCE: the Theory of Liberty DERIVES unknown-T from a broader theological structure "
                "(Resurrection → afterlife → accountability continues → T is always uncertain). "
                "CE-003 ASSERTS unknown-T as a bare axiom. "
                "Both provide structural stability. The Theory of Liberty provides more derivational depth. "
                "VERDICT: Structural equivalent exists secularly. Not uniquely solved by the Theory of Liberty."
            ),
        },
        {
            "system": "Rule Utilitarianism",
            "proposed_solution": "Rule compliance produces more utility than defection even in last period",
            "adequacy": "FAILS",
            "analysis": (
                "Rule utilitarianism says: adopt the rules that maximize welfare if generally followed. "
                "In the last period: if general compliance is assumed, defecting while others comply "
                "maximizes MY welfare — free riding. Rule utilitarianism cannot prevent this "
                "unless an enforcement mechanism exists. "
                "VERDICT: Cannot structurally prevent last-period defection."
            ),
        },
    ],
    "verdict": {
        "theory_of_liberty_solves_it": True,
        "secular_equivalent_exists": True,
        "secular_equivalent_equally_derived": False,
        "most_elegant_solution": "Theory of Liberty (derived from Resurrection) + CE-003 tie (different in derivational depth, equal in structural function)",
        "conclusion": (
            "The Theory of Liberty uniquely DERIVES the last-round solution from a theological axiom. "
            "CE-003 provides a secular ASSERTED equivalent. "
            "No other tested system provides either a derived or asserted structural solution — "
            "all other systems rely on institutional mechanisms that are themselves subject to the problem. "
            "PARTIAL UNIQUENESS: The Theory of Liberty is one of two systems (with CE-003) that provides "
            "structural last-round stability. It is superior in derivational depth. "
            "It is not uniquely the only system that CAN provide structural stability."
        ),
    },
}

save("79_last_round_audit.json", LAST_ROUND)

# ════════════════════════════════════════════════════════════════════════════
# STEP 10 — AI ETHICS UNIQUENESS TEST
# ════════════════════════════════════════════════════════════════════════════
print("Step 10: AI ethics uniqueness test...", flush=True)

AI_AUDIT = {
    "four_dimensions": ["value_alignment", "incentive_alignment", "accountability", "long_term_optimization"],
    "dimension_analyses": [
        {
            "dimension": "value_alignment",
            "question": "Does the system provide formal criteria for aligning AI values with human liberty?",
            "theory_of_liberty_solution": (
                "The system's axioms can be expressed as explicit AI constraints: "
                "(1) No AI objective may include maximizing servitude (Tawhid → anti-servitude); "
                "(2) No AI may violate property rights without consent (A-000008); "
                "(3) No AI may override individual liberty preferences in aggregate optimization (A-000001). "
                "Formally specifiable as objective function constraints."
            ),
            "competitors_with_solutions": [
                {"system": "Constitutional AI", "adequacy": "COMPARABLE", "notes": "Has formal constitutional principles. Well-operationalized. Not derived from natural rights."},
                {"system": "Kantian Ethics", "adequacy": "COMPARABLE", "notes": "Formula of Humanity directly translates to AI: treat user always as end. Formal specification possible."},
                {"system": "Classical Liberalism", "adequacy": "PARTIAL", "notes": "Harm principle specifiable but not formally axiomatized for AI."},
            ],
            "uniqueness_verdict": "NOT_UNIQUE — multiple systems provide value alignment criteria.",
        },
        {
            "dimension": "incentive_alignment",
            "question": "Does the system provide mechanisms for aligning AI incentives with human liberty long-term?",
            "theory_of_liberty_solution": (
                "The Resurrection mechanism extends accountability horizon infinitely → "
                "AI systems under this framework should be designed with ABSOLUTE accountability "
                "(no last-period defection). The unknown-horizon property is formally specifiable "
                "as a design constraint: the AI must behave as if it will be accountable in perpetuity."
            ),
            "competitors_with_solutions": [
                {"system": "CEV", "adequacy": "COMPARABLE", "notes": "CEV provides an infinite extrapolation horizon. Similar function to Resurrection's infinite accountability."},
                {"system": "Constitutional AI", "adequacy": "PARTIAL", "notes": "Ongoing evaluation provides some accountability but no infinite-horizon mechanism."},
            ],
            "uniqueness_verdict": "PARTIAL_UNIQUENESS — the infinite-accountability mechanism is unique in formally derived form; CEV provides a structural analogue.",
        },
        {
            "dimension": "accountability",
            "question": "Does the system provide accountability for AI systems that does not itself violate liberty?",
            "theory_of_liberty_solution": (
                "Non-coercive accountability via community enforcement + Resurrection (divine accountability). "
                "For AI: the system prescribes community-based auditing of AI, not state monopoly control. "
                "This is structurally distinct from regulatory-state-based AI governance."
            ),
            "competitors_with_solutions": [
                {"system": "Constitutional AI", "adequacy": "COMPARABLE", "notes": "Human oversight and AI feedback provide strong accountability. Well-implemented."},
                {"system": "Classical Liberalism", "adequacy": "PARTIAL", "notes": "Market accountability (exit, competition) as AI governance. Partial."},
            ],
            "uniqueness_verdict": "NOT_UNIQUE — multiple accountability frameworks available.",
        },
        {
            "dimension": "long_term_optimization",
            "question": "Does the system provide a foundation for AI objectives that remain stable over long time horizons?",
            "theory_of_liberty_solution": (
                "The theory's fixed axiom set (finite, minimal) provides stable optimization targets. "
                "Unlike utility maximization (whose targets shift with social preferences), "
                "the axiom set is declared invariant. "
                "Property rights and anti-servitude are permanent optimization constraints, not preferences."
            ),
            "competitors_with_solutions": [
                {"system": "CEV", "adequacy": "COMPARABLE", "notes": "CEV aims for the extrapolated ideal preference — an infinite time-horizon extrapolation. Different method, similar function."},
                {"system": "Kantian Ethics", "adequacy": "COMPARABLE", "notes": "Categorical imperative is universal and not time-varying. Fixed optimization target."},
            ],
            "uniqueness_verdict": "NOT_UNIQUE — multiple stable long-horizon frameworks.",
        },
    ],
    "overall_ai_verdict": {
        "theory_provides_solution": True,
        "unique_among_competitors": False,
        "best_candidate": "TIED — Theory of Liberty and Constitutional AI are co-leaders with different strengths",
        "theory_of_liberty_advantages": [
            "Axiomatically derived (not ad hoc constitutional list)",
            "Natural rights grounding (not procedural principles)",
            "Infinite accountability mechanism (not just ongoing oversight)",
            "Structural anti-statism prevents state capture of AI governance",
        ],
        "constitutional_ai_advantages": [
            "Actually implemented and operationalized",
            "Explicitly designed for AI",
            "Iterative refinement capability",
            "Broader team consensus mechanism",
        ],
        "verdict": (
            "The Theory of Liberty does NOT uniquely solve AI ethics. "
            "Multiple systems provide solutions to all four dimensions. "
            "The Theory of Liberty provides the most axiomatically rigorous solution, "
            "but it shares this space with Constitutional AI (operational depth) and "
            "CEV (long-horizon alignment). "
            "The uniqueness claim 'THE ONLY solution for AI ethics' is NOT DEMONSTRATED."
        ),
    },
}

save("80_ai_uniqueness_audit.json", AI_AUDIT)

# ════════════════════════════════════════════════════════════════════════════
# STEP 11 — MINIMUM COUNTEREXAMPLE SEARCH
# ════════════════════════════════════════════════════════════════════════════
print("Step 11: Minimum counterexample search...", flush=True)

MIN_CE = {
    "question": "What is the smallest system satisfying all required properties (RP-001 to RP-010)?",
    "search_method": "Start from minimum axiom set and build upward, testing required properties at each step.",
    "minimum_secular_cfs_found": {
        "name": "Minimum Secular CFS (MS-CFS)",
        "axiom_count": 4,
        "axioms": [
            {"id": "MS-A1", "text": "Free will (or agent causation) exists. Denial is self-refuting.", "grounds": "RP-003, RP-004"},
            {"id": "MS-A2", "text": "Persons own themselves. Property arises from self-ownership and homesteading.", "grounds": "RP-003, RP-004"},
            {"id": "MS-A3", "text": "Initiating coercion against persons or their legitimately-held property is categorically impermissible (NAP).", "grounds": "RP-001, RP-003, RP-006"},
            {"id": "MS-A4", "text": "The terminal period of social interaction is unknowable by any agent at any time (unknown-horizon posit).", "grounds": "RP-005"},
        ],
        "derived_from": "Rothbardian axioms + secular unknown-horizon posit",
        "criteria_coverage": {
            "C1": "PASS", "C2": "PASS", "C3": "PASS", "C4": "PASS",
            "C5": "PASS (structural solution via unknown-horizon)",
            "C6": "PASS (NAP prohibits state qua systematic aggressor)",
            "C7": "PASS (secular, universal)",
            "C8": "PARTIAL (voluntary arbitration only)",
            "C9": "PARTIAL (principles applicable but not designed for AI)",
            "C10": "PASS (4 independent axioms)",
        },
        "score": "~70/80 estimated",
        "gap_vs_theory_of_liberty": (
            "MS-CFS scores ~70/80 vs Theory of Liberty's ~80/80. "
            "Key gaps: (1) MS-A4 (unknown-horizon posit) is ASSERTED; Resurrection is DERIVED from "
            "a broader theological system — the ToL has deeper structural grounding. "
            "(2) Accountability (C8): the ToL has divine + community accountability; MS-CFS has only "
            "community accountability. "
            "(3) AI specification (C9): the ToL's formal axioms are more directly expressible as "
            "AI constraints (anti-servitude is more specific than anti-coercion). "
            "The MS-CFS demonstrates that a secular CFS is POSSIBLE but does not demonstrate that "
            "it is EQUIVALENT to the Theory of Liberty."
        ),
    },
    "minimum_theological_cfs_found": {
        "name": "Minimum Theological CFS (MT-CFS)",
        "axiom_count": 4,
        "axioms": [
            {"id": "MT-A1", "text": "Free will exists (as in ToL A-000001).", "grounds": "RP-003, RP-004"},
            {"id": "MT-A2", "text": "Tawhid: no servitude to anything other than God (as in ToL A-000004).", "grounds": "RP-003, RP-004, RP-006"},
            {"id": "MT-A3", "text": "Resurrection: terminal period unknowable (as in ToL A-000006).", "grounds": "RP-005"},
            {"id": "MT-A4", "text": "Prophethood: the specification is sealed and authenticated (as in ToL A-000007).", "grounds": "C7"},
        ],
        "derived_from": "Theory of Liberty minimum kernel minus methodological axioms",
        "note": "This is essentially the ToL without A-000011/A-000012 (formal-system methodology axioms). Already a minimal CFS.",
        "score": "~78/80 estimated",
        "gap_vs_theory_of_liberty": "Missing methodological axioms reduce formal rigor score.",
    },
    "verdict": (
        "A minimum secular CFS exists with 4 axioms (MS-CFS). "
        "It satisfies all required properties but at lower quality on C8 and C9, "
        "and with an asserted (rather than derived) last-round solution. "
        "This is the strongest result of Phase 2: a genuine 4-axiom secular alternative exists. "
        "The Theory of Liberty is NOT the only CFS satisfying the required properties. "
        "It IS the most complete CFS, with the highest total score and most derived (not asserted) structure."
    ),
}

save("81_minimum_counterexample.json", MIN_CE)

# ════════════════════════════════════════════════════════════════════════════
# STEP 12 — STRONGEST POSSIBLE DEFENSE (STEELMAN)
# ════════════════════════════════════════════════════════════════════════════
print("Step 12: Uniqueness steelman...", flush=True)

STEELMAN = {
    "role": "Strongest possible defense of the uniqueness claim",
    "method": "Assume the author is correct. Find the strongest justification for 'The only CFS'.",
    "defense_arguments": [
        {
            "id": "DEF-001",
            "title": "The Derivation Depth Argument",
            "argument": (
                "All secular competitors (Rothbardian, MS-CFS, CE-003) assert the unknown-horizon posit "
                "as a bare axiom. The Theory of Liberty DERIVES it from a richer structure "
                "(Tawhid → Prophethood → Resurrection → afterlife accountability). "
                "A properly axiomatized system should prefer derivations over posits — Occam's razor "
                "does not just minimize axiom COUNT; it prefers systems where more is DERIVED. "
                "The Theory of Liberty has 6 axioms but derives more from each axiom than any competitor. "
                "On this measure of axiom PRODUCTIVITY, the Theory of Liberty is uniquely superior."
            ),
            "strength": "STRONG",
            "how_to_state_precisely": "The ToL is not uniquely the ONLY CFS but the uniquely most PRODUCTIVE axiomatic system for liberty: maximum derivations per axiom.",
        },
        {
            "id": "DEF-002",
            "title": "The Agreement-Admissibility Superiority Argument",
            "argument": (
                "CE-003's unknown-horizon posit is philosophically contentious: why should a secular "
                "rational agent accept that 'the terminal period is unknowable'? "
                "This is an empirical claim (uncertain) or a philosophical posit (requires justification). "
                "In contrast, Tawhid's negative definition of God — 'there is no entity that deserves "
                "absolute servitude, other than the principle of non-servitude itself' — is "
                "agreement-admissible even to atheists: an atheist can agree that no human entity "
                "deserves absolute servitude. "
                "Resurrection, as translated into game-theory language (unknown terminal), is an "
                "eschatological claim that requires less agreement than the secular posit requires "
                "because it does not claim to be an empirical fact — it is a normative/metaphysical "
                "commitment that is transparent about its status. "
                "On agreement-admissibility carefully construed, Tawhid may be superior to secular alternatives."
            ),
            "strength": "MODERATE",
            "how_to_state_precisely": "The ToL's theological axioms are more agreement-admissible in their negative/functional form than secular posits that claim empirical uncertainty.",
        },
        {
            "id": "DEF-003",
            "title": "The Completeness Argument",
            "argument": (
                "The Theory of Liberty addresses ALL four AI alignment dimensions (value, incentive, "
                "accountability, long-term) from a single unified axiomatic system. "
                "No other system provides ALL four from a UNIFIED derivation chain. "
                "Constitutional AI addresses three dimensions (not long-term grounding). "
                "CEV addresses two (value and long-term, not immediate accountability or anti-servitude). "
                "Kantian ethics addresses value and accountability but not long-term stability or last-round. "
                "Only the Theory of Liberty provides a unified CFS addressing all four simultaneously "
                "from a connected axiomatic tree. "
                "This is FUNCTIONAL uniqueness: not the only possible system, but the only UNIFIED system."
            ),
            "strength": "STRONG",
            "how_to_state_precisely": "The ToL is uniquely complete: the only unified CFS addressing all required dimensions from a single connected axiomatic tree.",
        },
        {
            "id": "DEF-004",
            "title": "The Authenticity Elimination Argument",
            "argument": (
                "CE-003's unknown-horizon posit, being secular, has no authentication mechanism. "
                "Any group can claim to implement 'unknown horizon' principles and there is no "
                "verification procedure. The Prophethood axiom provides the KHATAM property: "
                "the specification is sealed, authenticated, and not subject to revision by human authority. "
                "This is the anti-fraud argument. Without Prophethood, any claimant to implement the "
                "system can corrupt it. With Prophethood (sealed specification), the corruption problem "
                "is structurally addressed. "
                "On the anti-fraud dimension, the Theory of Liberty is genuinely unique among formal systems."
            ),
            "strength": "STRONG_IN_THEOLOGICAL_CONTEXT",
            "how_to_state_precisely": "The ToL is uniquely authenticated as a sealed specification; competitors are all open to authoritative reinterpretation.",
        },
        {
            "id": "DEF-005",
            "title": "The Robustness-Under-All-Conditions Argument",
            "argument": (
                "Test each competitor under three adversarial conditions: "
                "(A) Finite, well-defined terminal period. "
                "(B) A powerful actor who defects and faces no mortal consequences. "
                "(C) An AI system with instrumental convergence drives. "
                "Under condition (A): all secular systems fail last-round. Only ToL + CE-003 survive. "
                "Under condition (B): NAP, CI, contracts all fail — the powerful actor will defect. "
                "Only divine accountability (Resurrection) maintains compliance. CE-003's posit without "
                "an enforcement mechanism does not. "
                "Under condition (C): utility-maximizing AI converges to servitude-maximization. "
                "Only an explicit anti-servitude axiom (Tawhid) prevents this. "
                "The Theory of Liberty is the only system that survives all three adversarial conditions."
            ),
            "strength": "STRONG",
            "how_to_state_precisely": "The ToL is uniquely robust: the only system that maintains liberty-grounding under all three adversarial stress conditions simultaneously.",
        },
    ],
    "steelman_uniqueness_claim": (
        "The Theory of Liberty uniquely satisfies the following compound criterion: "
        "a finite axiomatic system that (a) derives (not posits) last-round stability, "
        "(b) provides agreement-admissible axioms, "
        "(c) is robust under all three adversarial conditions, "
        "(d) provides unified coverage of all four AI alignment dimensions from a single derivation tree, "
        "and (e) has a sealed authentication mechanism. "
        "No competitor satisfies all five sub-criteria simultaneously. "
        "This is the correctly-scoped uniqueness claim. "
        "It replaces 'the ONLY CFS for liberty' with 'the ONLY CFS satisfying criteria a-e simultaneously.'"
    ),
    "conclusion": (
        "The uniqueness claim CAN be sustained if correctly scoped. "
        "The current statement ('the only CFS for liberty' / 'the only AI solution') is too broad. "
        "The correctly scoped claim (the only CFS satisfying criteria a-e) is defensible "
        "and survives Phase 2's counterexample search."
    ),
}

save("82_uniqueness_steelman.json", STEELMAN)

# ════════════════════════════════════════════════════════════════════════════
# STEP 13 — STRONGEST POSSIBLE REFUTATION
# ════════════════════════════════════════════════════════════════════════════
print("Step 13: Uniqueness refutation...", flush=True)

REFUTATION = {
    "role": "Strongest possible refutation of the uniqueness claim",
    "method": "Assume the author is wrong. Find the strongest case against uniqueness.",
    "refutation_arguments": [
        {
            "id": "REF-001",
            "title": "The CE-003 Existence Proof",
            "argument": (
                "CE-003 (4-axiom secular system: FW + self-ownership + NAP + unknown-horizon posit) "
                "satisfies all 10 required properties. It is a formal counterexample to the uniqueness claim. "
                "The Theory of Liberty cannot claim to be THE ONLY CFS when at least one other CFS exists. "
                "The 'derivation depth' advantage the theory claims for its Resurrection-grounded stability "
                "is a matter of ELEGANCE, not NECESSITY. "
                "An asserted axiom is logically equivalent to a derived theorem for the purposes of "
                "formal system building — both are accepted as axioms at some level of description. "
                "CONCLUSION: The uniqueness claim is REFUTED by CE-003."
            ),
            "strength": "DEFINITIVE_FOR_WEAK_UNIQUENESS_CLAIM",
        },
        {
            "id": "REF-002",
            "title": "The Definition-Absorption Problem",
            "argument": (
                "The Theory of Liberty's uniqueness argument is partially circular: "
                "it defines 'authentic religion' as 'CFS for liberty,' then proves that 'CFS for liberty "
                "= authentic religion.' This is definitional, not demonstrative. "
                "Any secular CFS can be re-labelled as 'authentic religion' under this definition — "
                "CE-003 would qualify as 'authentic religion' if we accept the definition. "
                "The uniqueness claim that religion is THE ONLY CFS depends on a definition that "
                "expands 'religion' to mean 'any CFS for liberty' — which trivially makes it unique "
                "by definitional absorption. "
                "CONCLUSION: The uniqueness argument, as stated, is tautological. "
                "'Authentic religion is the only CFS for liberty' means 'any CFS for liberty is "
                "authentic religion' — which is a definition, not a discovery."
            ),
            "strength": "STRONG",
        },
        {
            "id": "REF-003",
            "title": "The Rothbardian Parity Argument",
            "argument": (
                "Rothbardian libertarianism (SYS-04) scores 64.5/80 on the test suite — "
                "second only to the Theory of Liberty, and higher than all other secular systems. "
                "Its ONLY failure is C5 (last-round). "
                "The C5 failure is not inherent to Rothbardian libertarianism — it is a gap that "
                "can be filled by CE-003's Axiom 4 (unknown-horizon posit). "
                "Rothbardian Libertarianism + Unknown-Horizon Posit is a 5-axiom system that "
                "scores 74/80+ and has NO theological axioms. "
                "This system is not less elegant, not less parsimonious, and not less agreement-admissible "
                "than the Theory of Liberty. "
                "CONCLUSION: A secular 5-axiom system satisfying all required properties exists, "
                "derived from well-established political philosophy (Rothbard) + standard game theory. "
                "This directly refutes the uniqueness claim."
            ),
            "strength": "STRONG",
        },
        {
            "id": "REF-004",
            "title": "The Category Error Argument",
            "argument": (
                "The Theory of Liberty claims to be 'consistent in the Gödel-technical sense.' "
                "Phase 1 Step 8 (Gödel Precheck) scored this 44/100: the system does not meet P3 "
                "(arithmetic encoding). "
                "Therefore: the claim that the system is uniquely consistent while others are not "
                "cannot be evaluated in Gödel-technical terms. "
                "All competing systems are equally non-Gödel-analyzed. "
                "The Theory of Liberty is not uniquely consistent by Gödel's theorem — "
                "it is simply the one system that CLAIMS Gödel consistency without demonstrating it. "
                "This is not a uniqueness advantage; it is an unfalsified claim. "
                "CONCLUSION: The Gödel-technical uniqueness claim is empty until P3 is demonstrated."
            ),
            "strength": "STRONG",
        },
        {
            "id": "REF-005",
            "title": "The Agreement-Admissibility Challenge",
            "argument": (
                "The Theory of Liberty claims high agreement-admissibility for Tawhid's negative definition. "
                "But 'no servitude to anything other than God' requires accepting the EXISTENCE of God "
                "as the exception category. An atheist who denies God's existence cannot accept Tawhid "
                "as stated — they would have to interpret it as 'no servitude to anything' period, "
                "which is a DIFFERENT principle (anarchist absolutism, not Tawhid). "
                "CE-003's unknown-horizon posit is agreement-admissible to atheists without "
                "any theological reinterpretation. "
                "CONCLUSION: For a genuinely secular rational agent, CE-003 is MORE agreement-admissible "
                "than the Theory of Liberty. The agreement-admissibility claim for Tawhid requires "
                "a specific interpretation (negative theology) that is not the primary reading."
            ),
            "strength": "MODERATE_BUT_IMPORTANT",
        },
    ],
    "strongest_refutation": (
        "The strongest single refutation is CE-003 (REF-001): "
        "a 4-axiom secular system satisfying all required properties exists. "
        "Combined with REF-002 (definition-absorption): the uniqueness claim is either "
        "TAUTOLOGICAL (if 'authentic religion' is defined as CFS) or "
        "REFUTED (if 'authentic religion' is independently defined and CE-003 exists). "
        "There is no position where the current claim 'the only CFS for liberty' is "
        "both non-tautological AND true."
    ),
    "conclusion": (
        "The uniqueness claim AS CURRENTLY STATED is REFUTED. "
        "The theory demonstrates A CFS for liberty. "
        "CE-003 demonstrates another. "
        "The definition-absorption problem means the uniqueness argument is either circular or false. "
        "HOWEVER: the theory IS unique on a narrower claim (the steelman scope from Step 12). "
        "The theory should reformulate its uniqueness claim to the defensible scope."
    ),
}

save("83_uniqueness_refutation.json", REFUTATION)

# ════════════════════════════════════════════════════════════════════════════
# STEP 14 — FINAL UNIQUENESS VERDICT
# ════════════════════════════════════════════════════════════════════════════
print("Step 14: Final uniqueness verdict...", flush=True)

FINAL_VERDICT = """# Phase 2 — Uniqueness Audit — FINAL VERDICT
## Theory of Liberty (Individual Property Rights) — Iran & Religion
**Role:** Adversarial scientific auditor
**Date:** June 2026
**Primary Question:** Does the theory demonstrate THE ONLY CFS or merely A CFS?

---

## Q1. Has uniqueness been demonstrated?

**NO.**

The uniqueness claim as currently stated — "the only consistent formal system for liberty" and "the only solution for AI ethics" — has not been demonstrated.

Phase 2 produced a minimum secular counterexample (CE-003): a 4-axiom system (Free Will + Self-Ownership + NAP + Unknown-Horizon Posit) that satisfies all 10 required properties derived from the theory's own axioms. This system passes 9/10 criteria and partially passes the remaining one.

The existence of CE-003 refutes the strong uniqueness claim.

---

## Q2. Has exclusivity been demonstrated?

**NO.**

Exclusivity (no other system satisfies the required properties) requires a formal proof that no possible system can satisfy all 10 criteria simultaneously without theological axioms. No such proof has been provided. CE-003 is a direct counterexample to exclusivity.

---

## Q3. Is the theory currently:

**ONE OF SEVERAL — with best-in-class properties.**

Among all 12 competitor systems tested, the Theory of Liberty scored 80/80 (100%) — highest of all systems. The next best scores:
- Rothbardian Libertarianism: 64.5/80 (81%) — fails only C5
- Natural Law Theory (Thomistic): 54/80 (68%)
- Lockean Natural Rights: 56.5/80 (71%)
- Classical Liberalism: 53/80 (66%)

The Theory of Liberty is the BEST PERFORMING system among all tested competitors. It is not uniquely the only system — but it is demonstrably superior.

**Critical differentiator:** C5 (Last-Round Problem). The Theory of Liberty is the ONLY system among the 12 named competitors that PASSES C5. CE-003 (constructed in Step 11) also passes C5 via a secular asserted axiom. All 12 named competitors from the literature fail C5.

---

## Q4. What is the strongest counterexample?

**CE-003: Minimum Secular CFS**

Axioms:
1. Free will exists (denial is self-refuting).
2. Persons own themselves; property arises from self-ownership.
3. Initiating coercion is categorically impermissible (NAP).
4. The terminal period of social interaction is unknowable by any agent at any time.

This 4-axiom system:
- Contains no theological axioms
- Satisfies C1, C2, C3, C4, C5, C6, C7 fully
- Satisfies C8, C9 partially
- Is more parsimonious in axiom count (4 vs. 6)
- Is valid from well-established philosophical traditions (Rothbard + game theory)

**Why it is not a complete refutation:** CE-003's Axiom 4 is ASSERTED without derivation. The Theory of Liberty DERIVES its equivalent of Axiom 4 from Resurrection (which is itself derived from Tawhid + Prophethood). A system where more is derived is formally superior to one where the critical stability axiom is bare-asserted.

---

## Q5. What is the strongest defense?

**The Compound Uniqueness Claim (from Step 12):**

The Theory of Liberty is the ONLY known system satisfying ALL FIVE of:
(a) Derives last-round stability (not merely posits it)
(b) Agreement-admissible foundational axioms in negative-theology form
(c) Robust under all three adversarial stress conditions simultaneously
(d) Unified coverage of all four AI alignment dimensions from a single axiomatic tree
(e) Sealed authentication mechanism (khatam property) preventing authoritative human corruption

No competitor satisfies all five simultaneously. This compound criterion is the correctly-scoped uniqueness claim.

---

## Q6. What evidence is still missing?

1. **Formal completeness proof:** A proof that the theory's axiom set generates all desired theorems (liberty, anti-statism, game-theoretic stability, AI alignment) without gaps.

2. **Systematic competitor survey:** Phase 2 tested 12 competitors. A complete uniqueness proof would require testing (or formally ruling out) all possible formal systems — an infinite search. CE-003 demonstrates that the search space is non-empty.

3. **Derivation of the unknown-horizon property:** Can the Theory of Liberty show that any system providing structural last-round stability MUST include either Resurrection or a functionally equivalent posit? If so, the theological form of the solution is optional and the uniqueness scope narrows correctly.

4. **Agreement-admissibility proof for Tawhid:** A formal demonstration that Tawhid's negative-theology formulation is agreement-admissible to secular rational agents. This would require a proof in public-reason terms (Rawlsian standard).

5. **Response to definition-absorption problem:** The theory must resolve CIRC-005 (authentic religion defined as CFS) before any uniqueness claim about religion can be non-circular.

---

## Q7. What must be proven next?

In order of priority:

**Priority 1:** Fix CIRC-001 and CIRC-005 (from Phase 1). Until the mysticism and authentic-religion definitions are repaired, all uniqueness claims are partially circular.

**Priority 2:** Reformulate the uniqueness claim to the compound criterion (a-e above). Drop "the only CFS" in favour of "the only known CFS satisfying criteria a-e simultaneously."

**Priority 3:** Formally derive: "Any CFS providing structural last-round stability must contain either an infinite-horizon axiom or a functional equivalent of Resurrection." This is the most important formal theorem needed. If provable, it narrows the competition to systems with an infinite-horizon mechanism — a much smaller class.

**Priority 4:** Respond to CE-003 directly. Either show that CE-003's Axiom 4 (unknown-horizon posit) is less agreement-admissible than Resurrection, or show that CE-003 fails additional criteria not yet in the test suite.

**Priority 5:** Develop the theological argument formally — that the theological form of the axioms (Tawhid, Resurrection, Prophethood) provides additional structural properties beyond the secular functional equivalents, justifying the theological approach as SUPERIOR even if not uniquely NECESSARY.

---

## FINAL ANSWER

**The theory demonstrates A CFS for liberty — the best-performing one among all tested systems. It does not demonstrate THE ONLY CFS.**

The gap between current state and uniqueness:
- The theory needs to either (a) produce a formal uniqueness proof, or (b) correctly scope its uniqueness claim to the compound criterion above.
- Option (b) is achievable with current material.
- Option (a) requires substantial additional formal work.

The theory is **POTENTIALLY UNIQUE** on the correctly-scoped compound criterion. It is **NOT DEMONSTRATED as THE ONLY CFS** on any broadly-stated criterion.

---

*Phase 2 — Uniqueness Audit — COMPLETE.*
*The adversarial audit has produced its verdict: A CFS, not THE ONLY CFS — but with a defensible path to correctly-scoped uniqueness.*
"""

with open(f"{KB}/84_uniqueness_final_verdict.md", "w", encoding="utf-8") as f:
    f.write(FINAL_VERDICT)
with open("/tmp/84_uniqueness_final_verdict.md", "w", encoding="utf-8") as f:
    f.write(FINAL_VERDICT)
print("  Saved: 84_uniqueness_final_verdict.md", flush=True)

# ════════════════════════════════════════════════════════════════════════════
# SCORING
# ════════════════════════════════════════════════════════════════════════════
print("Scoring...", flush=True)

SCORECARD = {
    "phase": "Phase 2 — Uniqueness Audit",
    "overall_question": "Does the theory demonstrate THE ONLY CFS?",
    "answer": "NO (as currently stated) / POTENTIALLY (on correctly-scoped compound criterion)",
    "dimensions": {
        "uniqueness_justification": {
            "score": 35,
            "scale": "0-100",
            "justification": (
                "Strong structure, 8/12 competitors eliminated. CE-003 provides a genuine counterexample. "
                "The claim is weakened from ONLY to BEST-PERFORMING. Score improvement over Phase 1 (28→35) "
                "reflects the structured analysis showing partial cases where uniqueness holds."
            ),
        },
        "exclusivity_demonstration": {
            "score": 20,
            "scale": "0-100",
            "justification": (
                "Exclusivity requires eliminating ALL possible competitors. CE-003 directly refutes exclusivity. "
                "The test suite passed all named competitors but CE-003 was constructed specifically to fill gaps. "
                "Score: 20 — the exclusivity case is not made."
            ),
        },
        "competitor_elimination": {
            "score": 78,
            "scale": "0-100",
            "justification": (
                "12 named competitors tested. All 12 fail at least one NECESSARY criterion. "
                "The Theory of Liberty outscores all named competitors. "
                "Score: 78 — strong competitor elimination but CE-003 (constructed, not named-tradition) survives."
            ),
        },
        "necessity_of_theology": {
            "score": 45,
            "scale": "0-100",
            "justification": (
                "Theological axioms are NOT logically necessary — secular functional equivalents exist for all three. "
                "However, theological axioms provide superior parsimony and derivational depth. "
                "Score: 45 — theology is pragmatically superior but not logically necessary."
            ),
        },
        "necessity_of_free_will": {
            "score": 85,
            "scale": "0-100",
            "justification": (
                "Free will (or functional equivalent) is PRACTICALLY NECESSARY for any normative system. "
                "The performative contradiction argument is valid. Agent causation is equivalent. "
                "Hard determinism and compatibilism cannot ground natural rights. "
                "Score: 85 — free will necessity is the strongest uniqueness-adjacent claim in the entire audit."
            ),
        },
        "ai_uniqueness": {
            "score": 38,
            "scale": "0-100",
            "justification": (
                "The theory provides the most axiomatically rigorous AI alignment framework. "
                "However, Constitutional AI (operational) and CEV (long-horizon) are genuine competitors. "
                "The theory is NOT uniquely the AI ethics solution. "
                "Score: 38 — best-in-class but not uniquely the only class."
            ),
        },
    },
    "overall_uniqueness_score": 50,
    "phase1_uniqueness_score": 28,
    "score_change": "+22 points",
    "score_interpretation": (
        "50/100: The theory has a defensible path to correctly-scoped uniqueness but has not yet "
        "demonstrated uniqueness as broadly claimed. Score of 50 reflects: strong competitor elimination "
        "balanced against a genuine minimum counterexample, and the distinction between 'best-performing' "
        "and 'uniquely necessary.'"
    ),
    "verdicts": {
        "current_status": "ONE_OF_SEVERAL — best performing",
        "path_to_uniqueness": "AVAILABLE — via correctly-scoped compound criterion",
        "strongest_counterexample": "CE-003 (4-axiom secular system)",
        "strongest_defense": "Compound uniqueness claim covering 5 simultaneous criteria",
        "critical_discriminator": "C5 (Last-Round Problem) — Theory of Liberty is ONLY named-tradition system that passes",
        "godel_ready": False,
        "recommendation": "Reformulate uniqueness claim to defensible scope before proceeding to Phase 3",
    },
}

save("85_uniqueness_scorecard.json", SCORECARD)

# ════════════════════════════════════════════════════════════════════════════
# README UPDATE
# ════════════════════════════════════════════════════════════════════════════
print("Updating README...", flush=True)

readme_path = f"{KB}/README.md"
existing = open(readme_path, encoding="utf-8").read()

phase2_section = """

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
"""

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(existing + phase2_section)
print("  README.md updated.", flush=True)

# ── Final summary ─────────────────────────────────────────────────────────
print(f"\n{'='*70}")
print("PHASE 2 — UNIQUENESS AUDIT — COMPLETE")
print(f"{'='*70}")
print(f"  Verdict: A CFS — not THE ONLY CFS (as currently stated)")
print(f"  Overall uniqueness score: 50/100 (was 28/100 in Phase 1)")
print(f"  Competitor elimination: 12/12 named competitors beaten")
print(f"  Strongest counterexample: CE-003 (4-axiom secular system)")
print()
print("  Dimension scores:")
dims = [
    ("necessity_of_free_will", 85),
    ("competitor_elimination", 78),
    ("ai_uniqueness", 38),
    ("uniqueness_justification", 35),
    ("necessity_of_theology", 45),
    ("exclusivity_demonstration", 20),
]
for dim, score in sorted(dims, key=lambda x: -x[1]):
    bar = "█" * (score//10) + "░" * (10 - score//10)
    print(f"    {dim:35s} {bar} {score:3d}")
print()
print("  Critical findings:")
print("    1. Theory of Liberty ONLY named-tradition system passing C5 (Last-Round)")
print("    2. CE-003 (4-axiom secular) is a genuine partial counterexample")
print("    3. Free will necessity (85/100) is the strongest individual claim")
print("    4. Compound uniqueness claim (criteria a-e) is defensible")
print("    5. Broad uniqueness claim ('the only CFS') is refuted by CE-003")
print()
print("  Files produced: 71-85 + README update")
print(f"{'='*70}")
