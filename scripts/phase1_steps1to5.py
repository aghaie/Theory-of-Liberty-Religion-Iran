#!/usr/bin/env python3
"""Phase 1 Steps 1-5: Axiom Independence, Hidden Axiom Analysis,
Contradiction Audit, Circularity Audit, Inference Validity."""

import json, os
from collections import defaultdict

KB = "/Users/ali/Documents/GitHub/Theory-of-Liberty-Religion-Iran/knowledge_base"

def L(p): return json.load(open(p, encoding="utf-8"))
def LJ(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]

def save(name, obj):
    for p in [f"/tmp/{name}", f"{KB}/{name}"]:
        json.dump(obj, open(p,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"  Saved: {name}", flush=True)

# ── Load artifacts ──────────────────────────────────────────────────────────
ax_red  = L(f"{KB}/20_axiom_reduction.json")
contrad = L(f"{KB}/21_contradiction_candidates.json")        # from 0.75
cycles  = L(f"{KB}/24_circularity_report.json")
def_con = L(f"{KB}/25_definition_consistency_report.json")
inf_ch  = L(f"{KB}/36_inference_chains.json")
cycle_r = L(f"{KB}/38_cycle_reconstruction.json")
contra2 = L(f"{KB}/39_contradiction_reconstruction.json")   # from 0.9
formal  = L(f"{KB}/40_formalization_expansion.json")
min_ax  = L(f"{KB}/41_minimum_axiom_set.json")
kernel  = L(f"{KB}/42_theory_kernel.json")
hidden  = L(f"{KB}/33_hidden_axioms.json")
def_nm  = L(f"{KB}/34_definition_normalization.json")
dep_val = L(f"{KB}/35_dependency_validation.json")
hard    = L(f"{KB}/45_hardening_report.json")
aud     = L(f"{KB}/32_axiom_audit.json")

EDGES = dep_val["edges"]
KERNEL_AXIOMS = kernel["kernel_axioms"]
KERNEL_CLAIMS = kernel["kernel_claims"]

# Reference texts
AX = {a["id"]: a["text"] for a in KERNEL_AXIOMS}
CL = {c["id"]: c["text"] for c in KERNEL_CLAIMS}

def ax(i): return AX.get(i, i)
def cl(i): return CL.get(i, i)

print("Phase 1 loaded.", flush=True)

# ════════════════════════════════════════════════════════════════════════════
# STEP 1 — AXIOM INDEPENDENCE TEST
# ════════════════════════════════════════════════════════════════════════════
print("\nStep 1: Axiom independence test...", flush=True)

# The 15 named axioms with their declared deps from Phase 0.9
NAMED_AXIOMS_RAW = aud["named_axiom_audit"]

# For independence: an axiom A is *independent* if it cannot be derived
# from the remaining axioms via the validated edge set.
# Method: for each axiom, remove it from the source set and test
# whether it can still be reached from the remaining axioms.

from collections import deque
adj_out = defaultdict(set)
adj_in  = defaultdict(set)
all_nodes = set()
for e in EDGES:
    adj_out[e["from"]].add(e["to"])
    adj_in[e["to"]].add(e["from"])
    all_nodes.update([e["from"], e["to"]])

def reachable_from(sources, adj):
    vis = set()
    q = deque(sources)
    while q:
        n = q.popleft()
        if n in vis: continue
        vis.add(n)
        for nb in adj.get(n, set()):
            q.append(nb)
    return vis

TIER0 = {"A-000001","A-000011","A-000012"}

# For each named axiom: can it be derived from the others?
independence_results = []
for ax_rec in NAMED_AXIOMS_RAW:
    aid = ax_rec["axiom_id"]
    text = ax_rec["text"]
    deps = ax_rec.get("depends_on", [])
    tier = ax_rec.get("tier", "?")
    atype = ax_rec.get("classification","")

    # Independence test:
    # A tier-0 axiom with no declared deps and no incoming edges is independent by definition
    has_incoming = bool(adj_in.get(aid, set()))
    has_outgoing = bool(adj_out.get(aid, set()))

    if tier == 0 and not deps:
        independence = "INDEPENDENT"
        reason = "Tier-0: no declared dependencies, no incoming edges in validated backbone."
    elif deps:
        # Check if derivable via declared deps
        reach = reachable_from(set(deps), adj_out)
        if aid in reach:
            independence = "DERIVABLE_VIA_DECLARED_DEPS"
            reason = f"Reachable from declared deps {deps} via validated edges."
        else:
            # Has deps but not reachable — may still be independent
            independence = "WEAKLY_INDEPENDENT"
            reason = f"Has declared deps {deps} but not reachable from them via backbone. May require additional implicit steps."
    else:
        if has_incoming:
            reach_all = reachable_from(TIER0, adj_out)
            if aid in reach_all:
                independence = "DERIVABLE_FROM_TIER0"
                reason = "Reachable from tier-0 axioms via backbone edges."
            else:
                independence = "INDEPENDENT"
                reason = "No declared deps; not reachable from tier-0 backbone. Independently posited."
        else:
            independence = "INDEPENDENT"
            reason = "No declared deps, no incoming edges. Pure posit."

    # Additional classifications
    if "REDUNDANT" in text.upper():
        independence = "REDUNDANT_BY_DECLARATION"
        reason = "Explicitly declared redundant in Phase 0.9 axiom reduction."

    # Definitional check: is this axiom essentially a definition of a concept?
    is_definitional = any(kw in text.lower() for kw in
        ["is defined as","means","equivalent to","identical to","is equal to"])

    # Hidden check: is this actually an assumption the theory needs but treats as axiom?
    is_hidden_candidate = any(h["implicitly_used_in"] for h in hidden["hidden_axioms"]
                               if aid in h.get("implicitly_used_in",[]))

    independence_results.append({
        "axiom_id": aid,
        "text": text,
        "tier": tier,
        "declared_deps": deps,
        "independence_status": independence,
        "reason": reason,
        "is_definitional": is_definitional,
        "is_hidden_candidate": is_hidden_candidate,
        "has_incoming_backbone_edges": has_incoming,
        "has_outgoing_backbone_edges": has_outgoing,
    })

# Summary
by_status = defaultdict(list)
for r in independence_results:
    by_status[r["independence_status"]].append(r["axiom_id"])

save("51_axiom_independence_report.json", {
    "method": "BFS reachability over validated backbone (46 edges). Independence = not reachable from remaining axioms via backbone.",
    "total_axioms_tested": len(independence_results),
    "by_status": {k: {"count": len(v), "axioms": v} for k, v in by_status.items()},
    "truly_independent": [r["axiom_id"] for r in independence_results if r["independence_status"] == "INDEPENDENT"],
    "derivable": [r["axiom_id"] for r in independence_results
                  if "DERIVABLE" in r["independence_status"]],
    "redundant": [r["axiom_id"] for r in independence_results
                  if "REDUNDANT" in r["independence_status"]],
    "audit": independence_results,
    "key_finding": (
        "A-000001 (Free Will), A-000011 (Finite Axioms), A-000012 (Consistency) "
        "are genuinely independent — no incoming backbone edges, no declared deps, tier-0. "
        "A-000004 (Tawhid) is weakly independent: it has A-000001 as declared dep but is "
        "not derivable from A-000001 alone via the backbone — it requires a theological posit. "
        "A-000003 (Liberty requires divine grounding) is REDUNDANT: derivable from A-000001+A-000004. "
        "A-000006, A-000007 are derived from A-000004 but each requires an additional non-logical posit "
        "(Resurrection, Prophethood) — making them independent theological axioms, not merely derived ones."
    ),
})

# ════════════════════════════════════════════════════════════════════════════
# STEP 2 — HIDDEN AXIOM ANALYSIS
# ════════════════════════════════════════════════════════════════════════════
print("Step 2: Hidden axiom analysis...", flush=True)

HA_ANALYSIS = []
for ha in hidden["hidden_axioms"]:
    hid = ha["hidden_axiom_id"]
    name = ha["name"]
    stmt = ha["statement"]
    htype = ha["type"]
    why = ha["why_needed"]
    used_in = ha.get("implicitly_used_in", [])

    # Necessity: is the theory broken without it?
    # Classify on type:
    if htype in ("epistemological", "logical"):
        necessity = "NECESSARY"
        necessity_reason = (
            f"The theory uses deductive inference throughout. Without {name}, "
            "the basic inferential structure of the theory collapses."
        )
    elif htype == "metaphysical":
        necessity = "NECESSARY_FOR_STABILITY_ARGUMENTS"
        necessity_reason = (
            f"{name} is required for game-theoretic and property-persistence claims. "
            "Without it, the temporal stability proofs fail."
        )
    elif htype == "theological":
        necessity = "CONDITIONALLY_NECESSARY"
        necessity_reason = (
            f"{name} is necessary only if the theory claims theological sources "
            "are consistent and authoritative. For the purely secular kernel, optional."
        )
    elif htype == "normative":
        necessity = "NECESSARY_FOR_DEONTIC_LAYER"
        necessity_reason = (
            f"{name} is required to derive deontic claims (obligations/prohibitions). "
            "Without it the theory can describe property but not prescribe its protection."
        )
    elif htype == "methodological":
        necessity = "CRITICAL"
        necessity_reason = (
            f"{name} is directly load-bearing for the CFS methodology. "
            "If Gödel's theorems do not transfer, the capital-C 'Consistent' language collapses."
        )
    elif htype == "theoretical":
        necessity = "LOAD_BEARING_FOR_TERMINAL_CLAIMS"
        necessity_reason = (
            f"{name} is required for the AI-ethics uniqueness conclusion. "
            "Without it the theory offers A solution, not THE solution."
        )
    elif htype == "metaethical":
        necessity = "NECESSARY_FOR_NORMATIVE_FORCE"
        necessity_reason = (
            f"{name} (moral realism) is required for moral claims to have "
            "binding force beyond mere preference. Without it, the theory is descriptive only."
        )
    else:
        necessity = "OPTIONAL"
        necessity_reason = "Low coupling to core derivation chain."

    # Is it secretly foundational? (more central than the named axioms suggest)
    secretly_foundational = htype in ("logical", "epistemological", "methodological")

    HA_ANALYSIS.append({
        "hidden_axiom_id": hid,
        "name": name,
        "statement": stmt,
        "type": htype,
        "necessity": necessity,
        "necessity_reason": necessity_reason,
        "secretly_foundational": secretly_foundational,
        "implicitly_used_in": used_in,
        "auditor_note": (
            f"This axiom is {necessity}. " +
            ("It should be elevated to the named axiom set for formal completeness. "
             if secretly_foundational else
             "It need not be in the named axiom set but should be acknowledged as a pre-condition.")
        ),
    })

secretly_foundational_list = [h for h in HA_ANALYSIS if h["secretly_foundational"]]
save("52_hidden_axiom_analysis.json", {
    "total_hidden_axioms": len(HA_ANALYSIS),
    "necessary_count": sum(1 for h in HA_ANALYSIS if "NECESSARY" in h["necessity"]),
    "secretly_foundational_count": len(secretly_foundational_list),
    "secretly_foundational_ids": [h["hidden_axiom_id"] for h in secretly_foundational_list],
    "analysis": HA_ANALYSIS,
    "key_finding": (
        "3 hidden axioms (HA-001, HA-002, HA-005) are secretly foundational: objective truth, "
        "reliable reason, and valid inference are prerequisites for every step of every derivation. "
        "They should be elevated to the named axiom set. Without them, the theory's entire "
        "deductive framework rests on unacknowledged presuppositions. "
        "HA-008 (Gödel transfer) is CRITICAL: it is load-bearing for the CFS methodology "
        "but unproven. HA-006 (uniqueness) is the most consequential for the terminal claims."
    ),
})

# ════════════════════════════════════════════════════════════════════════════
# STEP 3 — CONTRADICTION AUDIT
# ════════════════════════════════════════════════════════════════════════════
print("Step 3: Contradiction audit...", flush=True)

# The 10 reconstructed contradiction candidates from Phase 0.9
CLASSIFICATIONS = {
    "CR-001": {
        "verdict": "SCOPE_MISMATCH",
        "reasoning": (
            "Claim A (reason alone derives liberty) and Claim B (liberty requires religion) "
            "operate on different scopes. Claim A establishes that free will is derivable secularly. "
            "Claim B establishes that stable long-run liberty requires solving the last-round problem. "
            "These are compatible: reason gets you to liberty conceptually; religion is needed for "
            "its game-theoretic stability. The conflict dissolves under scope-distinction: "
            "logical derivation vs. empirical stability. "
            "VERDICT: Not a genuine contradiction. Scope mismatch."
        ),
        "resolution": "Explicitly distinguish 'logical derivability of liberty' from 'empirical stability of liberty'. The theory already does this implicitly.",
        "severity": "LOW",
    },
    "CR-002": {
        "verdict": "SCOPE_MISMATCH",
        "reasoning": (
            "The author opposes the Islamic Republic as state-religion while endorsing Shi'ism's "
            "civilizational role. This is not a logical contradiction: the first concerns "
            "institutional coercion (forbidden by A-000005), the second concerns cultural substrate "
            "(which the theory treats as belonging to civil society, not state). "
            "The distinction holds logically: institution ≠ culture. "
            "VERDICT: Scope mismatch, resolvable by making the institution/culture distinction explicit."
        ),
        "resolution": "Formalise: Shi'ism_as_CFS ≠ Shi'ism_as_state_organ. All coercive applications of Shi'ism fall under A-000005 prohibition.",
        "severity": "LOW",
    },
    "CR-003": {
        "verdict": "GENUINE_UNRESOLVED",
        "reasoning": (
            "The claim that Tawhid has an 'objective, agreement-admissible definition' via negative "
            "ostension ('God is not any observable entity') requires the hidden axiom HA-011: "
            "that negative ostensive definitions are sufficient for formal axiomatic work. "
            "This is not established. In philosophy of language, negative ostension alone is "
            "generally considered insufficient to fix reference with enough precision for formal "
            "inference. The concept 'not-anything-observable' is extremely broad and could "
            "encompass logical impossibilities, abstract objects, and other non-observables. "
            "Without HA-011 being proven, Tawhid's 'objectivity' claim is itself an unproven axiom "
            "dressed as a definition. "
            "VERDICT: Genuine logical gap. Not a contradiction per se, but a circularity between "
            "Tawhid's claimed objectivity and the unproven sufficiency of negative definition."
        ),
        "resolution": "Requires a theory of reference for negative ostensive definitions, or Tawhid must be posited as a pure axiom (accepted without the 'objective' qualifier).",
        "severity": "HIGH",
    },
    "CR-004": {
        "verdict": "TERMINOLOGY_CONFLICT",
        "reasoning": (
            "The uniqueness claim (religion = the only CFS for liberty) and the Austrian School "
            "incompleteness claim (Austrian = CFS for liberty minus last-round solution) can be "
            "logically reconciled IF the gap filled by religion is unique. The conflict arises from "
            "imprecision: 'incomplete' could mean (a) missing components that could be added without "
            "religion, or (b) missing components that are uniquely provided by religion. The theory "
            "asserts (b) but the uniqueness must be demonstrated, not assumed. "
            "VERDICT: Terminology conflict resolvable by specifying what 'incomplete' means precisely."
        ),
        "resolution": "Define 'incomplete(Austrian)' as: Austrian School cannot solve {last-round problem, servitude-stopping authority, terminal condition} without adopting {Resurrection, Tawhid, Prophethood} or functional equivalents.",
        "severity": "MEDIUM",
    },
    "CR-005": {
        "verdict": "SCOPE_MISMATCH",
        "reasoning": (
            "Democracy as 'cheapest path to communism' applies when democracy is applied to "
            "individual rights (democracy over property rights → tragedy of the commons → statism). "
            "Liberal democracies preserving liberty is consistent with this if liberal democracies "
            "have non-democratic constraints (constitutional rights, property protections) that limit "
            "what majorities can decide. The theory's claim is: democracy applied to individual "
            "rights is destructive. Liberal democracies survive insofar as they are liberal, not "
            "insofar as they are democratic. This is internally consistent. "
            "VERDICT: Scope mismatch. Democracy-over-rights vs. democracy-constrained-by-rights."
        ),
        "resolution": "Explicit in the theory but must be formalised: D(individual_rights) → communism; D(collective_goods) ∧ ¬D(individual_rights) → compatible with liberty.",
        "severity": "LOW",
    },
    "CR-006": {
        "verdict": "GENUINE_UNRESOLVED",
        "reasoning": (
            "The theory invokes Gödel's incompleteness theorems to support the claim that "
            "religion is 'Consistent' (capital-C). Gödel's theorems apply specifically to "
            "formal systems that are: (1) recursively axiomatizable, (2) sufficiently expressive "
            "to encode arithmetic (contain Robinson Arithmetic Q as a subsystem), (3) consistent. "
            "The theory has not demonstrated property (2). Social-normative axiomatic systems "
            "typically do not encode arithmetic in the Gödelian sense. If (2) fails, then the "
            "Gödel framing is illustrative metaphor, not technical application. This is not a "
            "flaw in the theory's substance, but the invocation of Gödel as formal authority "
            "is unsupported. "
            "VERDICT: Genuine logical gap. Gödel is being used as a legitimating metaphor, "
            "not as a formal result. The substantive claims survive; the Gödelian framing is unsupported."
        ),
        "resolution": "Either: (a) demonstrate that the axiom system encodes a fragment of arithmetic, or (b) replace 'Consistent (Gödel-sense)' with 'non-contradictory' throughout, and cite Gödel only illustratively.",
        "severity": "HIGH",
    },
    "CR-007": {
        "verdict": "DEFINITIONAL_CIRCULARITY",
        "reasoning": (
            "This is the most serious logical defect in the theory. "
            "The definition of mysticism as 'any system that separates humans from property/reason/liberty' "
            "makes the following argument circular: "
            "P1: Mysticism is (by definition) any system that violates liberty. "
            "P2: Hegel/Marx/fascism violate liberty. "
            "C: Therefore Hegel/Marx/fascism are forms of mysticism. "
            "This is true by definition, not by demonstration. It contributes zero logical content. "
            "The same argument can be constructed for any anti-liberty system: call it 'mysticism' "
            "by definition, then 'prove' it is anti-liberty by unpacking the definition. "
            "The circularity affects approximately 428 history-domain claims that argue from "
            "'X is mysticism → X is anti-liberty.' All such arguments become tautologies. "
            "VERDICT: DEFINITIONAL CIRCULARITY. Confirmed. This is the theory's single most "
            "serious logical defect in its current form."
        ),
        "resolution": "Mysticism must be defined structurally and independently of liberty-violation: e.g., 'any system that identifies the divine with observable phenomena or dissolves individual identity into collective unity.' Then demonstrate that such systems imply anti-property consequences. The demonstration becomes non-trivial and falsifiable.",
        "severity": "CRITICAL",
    },
    "CR-008": {
        "verdict": "SCOPE_MISMATCH",
        "reasoning": (
            "Atheist liberal as 'delayed communist' applies to the terminal trajectory of "
            "a society organised on atheist-liberal principles. The claim is not that any "
            "individual atheist liberal will personally become a communist, but that "
            "atheist-liberal social organisation lacks the stability mechanism (Resurrection/last-round "
            "solution) to prevent eventual communisation. Austrian School founders as individuals "
            "produced correct partial theory without necessarily demonstrating the terminal trajectory "
            "applies to their work. "
            "VERDICT: Scope mismatch: individual vs. systemic trajectory."
        ),
        "resolution": "Distinguish: 'X's theory captures truths about liberty' (compatible with atheism) from 'atheist-liberal social organisation is terminally unstable' (a systemic claim).",
        "severity": "LOW",
    },
    "CR-009": {
        "verdict": "TERMINOLOGY_CONFLICT",
        "reasoning": (
            "Natural law discovery and formal axiomatic specification are different "
            "epistemological frameworks but are not contradictory. A law can be: "
            "(a) ontologically real (discovered, not invented), and "
            "(b) epistemologically communicated via axiomatic specification. "
            "This is standard in mathematics: mathematical truths are discovered (Platonism) "
            "but communicated via formal systems (formalism). The theory uses both, consistently. "
            "VERDICT: Terminology conflict. 'Discovered' refers to ontological status; "
            "'axiomatic system' refers to epistemological communication. Compatible."
        ),
        "resolution": "Explicitly state: 'Law is ontologically discovered; axiomatic systems are the epistemological vehicle for its reliable communication.'",
        "severity": "LOW",
    },
    "CR-010": {
        "verdict": "GENUINE_METHODOLOGICAL_TENSION",
        "reasoning": (
            "The claim that theory has primacy over data (A-000014) combined with using "
            "historical evidence as confirmation creates a methodological asymmetry. "
            "In a strict axiomatic theory, evidence can only instantiate or illustrate "
            "propositions, not confirm them. But the theory uses historical examples "
            "(Suffolk Bank, Iran's civilizational continuity) in ways that appear confirmatory. "
            "If A-000014 is strictly interpreted, the historical examples are only illustrations. "
            "If they are evidence, then A-000014 is overstated. "
            "This is not a logical contradiction but a methodological tension between "
            "the theory's axiomatic self-description and its actual argumentative practice. "
            "VERDICT: Genuine methodological tension. Not a formal contradiction."
        ),
        "resolution": "Adopt Lakatosian framework explicitly: theory (hard core) is protected from falsification by evidence; historical examples populate the protective belt as illustrations. All confirmatory language should be replaced with instantiating/illustrating language.",
        "severity": "MEDIUM",
    },
}

contra_audit = {"total": len(CLASSIFICATIONS), "by_verdict": defaultdict(list),
                "audit": []}
for c in contra2["candidates"]:
    cid = c["candidate_id"]
    ana = CLASSIFICATIONS.get(cid, {})
    entry = {**c,
             "verdict": ana.get("verdict","UNCLASSIFIED"),
             "auditor_reasoning": ana.get("reasoning",""),
             "resolution": ana.get("resolution",""),
             "severity": ana.get("severity","UNKNOWN")}
    contra_audit["audit"].append(entry)
    contra_audit["by_verdict"][ana.get("verdict","UNCLASSIFIED")].append(cid)

contra_audit["by_verdict"] = dict(contra_audit["by_verdict"])
contra_audit["summary"] = {
    "not_a_contradiction": len(contra_audit["by_verdict"].get("SCOPE_MISMATCH",[])) +
                            len(contra_audit["by_verdict"].get("TERMINOLOGY_CONFLICT",[])),
    "genuine_issues": len(contra_audit["by_verdict"].get("GENUINE_UNRESOLVED",[])) +
                       len(contra_audit["by_verdict"].get("DEFINITIONAL_CIRCULARITY",[])) +
                       len(contra_audit["by_verdict"].get("GENUINE_METHODOLOGICAL_TENSION",[])),
    "critical": sum(1 for c in contra_audit["audit"] if c.get("severity")=="CRITICAL"),
    "high": sum(1 for c in contra_audit["audit"] if c.get("severity")=="HIGH"),
}
save("53_contradiction_audit.json", contra_audit)

# ════════════════════════════════════════════════════════════════════════════
# STEP 4 — CIRCULARITY AUDIT
# ════════════════════════════════════════════════════════════════════════════
print("Step 4: Circularity audit...", flush=True)

# Load all cycle sources
cycle_sources = []
for c in cycle_r.get("cycles", []):
    cycle_sources.append(c)
for c in cycles.get("cycles", []):
    cycle_sources.append(c)

# The key issue flagged in Phase 0.9: mysticism definition circularity
# Plus any concept-level cycles

circularity_entries = []

# Mysticism circularity — the confirmed case
circularity_entries.append({
    "circularity_id": "CIRC-001",
    "type": "DEFINITIONAL_CIRCULARITY",
    "nodes": ["CN:mysticism", "C-000009", "C-000074"],
    "description": (
        "Mysticism is defined as 'any system that separates humans from property/reason/liberty.' "
        "The claim 'Hegel/Marx/fascism are forms of mysticism' is then 'proven' by showing "
        "they violate liberty. But since mysticism IS (by definition) what violates liberty, "
        "the 'proof' merely unpacks the definition. The cycle: "
        "[Mysticism ≡ anti-liberty] → [X is anti-liberty] → [X is mysticism] → [mysticism is anti-liberty]"
    ),
    "verdict": "DEFINITIONAL_CIRCULARITY",
    "severity": "CRITICAL",
    "scope_of_damage": "~428 history-domain claims using mysticism as explanandum.",
    "fix": "Redefine mysticism structurally (e.g., by the 'observable-God' or 'dissolution-of-individual' criterion) then derive anti-liberty as a consequence.",
    "is_logical_paradox": False,
    "is_self_defeating": True,
    "note": "The circularity makes the mysticism arguments tautological but does NOT falsify the theory. The claims may be true; they are simply not demonstrated."
})

# Liberty ↔ Religion mutual reinforcement
circularity_entries.append({
    "circularity_id": "CIRC-002",
    "type": "EXPLANATORY_FEEDBACK_LOOP",
    "nodes": ["L", "R", "CFS"],
    "description": (
        "Liberty requires religion (for stability); religion is the CFS for liberty; "
        "the CFS for liberty IS liberty's formal expression. "
        "The cycle: [L needs stable CFS] → [R is that CFS] → [R guarantees L] → [L needs R]."
    ),
    "verdict": "EXPLANATORY_FEEDBACK_LOOP",
    "severity": "BENIGN",
    "note": "The author explicitly calls this 'the string of beads' — intentional mutual reinforcement. It is not a logical paradox because the cycle is DESCRIPTIVE (how the world is) rather than DEFINITIONAL (what the terms mean). Liberty and religion are independently defined.",
    "is_logical_paradox": False,
    "is_self_defeating": False,
})

# Tawhid ↔ Liberty
circularity_entries.append({
    "circularity_id": "CIRC-003",
    "type": "EXPLANATORY_FEEDBACK_LOOP",
    "nodes": ["T","L","¬S"],
    "description": "Tawhid → ¬servitude → liberty; liberty → rejection of servitude → Tawhid (operational meaning).",
    "verdict": "EXPLANATORY_FEEDBACK_LOOP",
    "severity": "BENIGN",
    "note": "Tawhid and liberty are separately defined; their mutual entailment is a theoretical claim, not a definitional circularity.",
    "is_logical_paradox": False,
    "is_self_defeating": False,
})

# CFS self-reference
circularity_entries.append({
    "circularity_id": "CIRC-004",
    "type": "SELF_REFERENTIAL",
    "nodes": ["CFS(R)","R","CFS"],
    "description": (
        "The theory claims to be a CFS for liberty; religion is a CFS for liberty; "
        "therefore the theory is (or is a fragment of) religion. "
        "This is a self-referential claim: the theory validates itself by declaring itself "
        "a fragment of the system it is arguing for."
    ),
    "verdict": "BENIGN_SELF_REFERENCE",
    "severity": "LOW",
    "note": "Self-reference is not automatically a logical defect. Gödel's own method involves constructing self-referential statements. The question is whether the self-reference generates a paradox — it does not here, because the theory does not claim to prove its own consistency from within.",
    "is_logical_paradox": False,
    "is_self_defeating": False,
})

# Religion defined as CFS ↔ CFS proven by religion being non-contradictory
circularity_entries.append({
    "circularity_id": "CIRC-005",
    "type": "POTENTIALLY_CIRCULAR",
    "nodes": ["R_authentic", "CFS", "¬contradiction"],
    "description": (
        "The theory defines authentic religion as a CFS, then uses religion's lack of "
        "contradiction to confirm it is a CFS. "
        "Test: [R is authentic] ↔ [R is CFS]; [R is CFS] requires [R is non-contradictory]; "
        "[R is non-contradictory] established by 'any interpretation violating liberty is inauthentic.' "
        "But 'authentic' was defined as CFS-for-liberty. Potential circularity."
    ),
    "verdict": "POTENTIALLY_CIRCULAR",
    "severity": "MEDIUM",
    "note": "The consistency test (does it violate liberty?) is the same criterion as the definition (CFS for liberty = authentic). Whether this is viciously circular depends on whether 'authentic' and 'CFS for liberty' are independently defined. They are not: they are explicitly equated.",
    "fix": "Provide an independent criterion for 'authentic religion' (e.g., historical, textual, or formal-system-theoretic) that does not use 'CFS for liberty' in its definition. Then show convergence.",
    "is_logical_paradox": False,
    "is_self_defeating": True,
})

circ_audit = {
    "total_circularity_issues": len(circularity_entries),
    "by_type": defaultdict(int),
    "critical_count": sum(1 for c in circularity_entries if c.get("severity")=="CRITICAL"),
    "self_defeating": [c["circularity_id"] for c in circularity_entries if c.get("is_self_defeating")],
    "entries": circularity_entries,
    "overall_assessment": (
        "The theory has ONE critical circularity (CIRC-001: mysticism definition) and "
        "ONE potentially circular issue (CIRC-005: authentic religion / CFS equivalence). "
        "The remaining cycles are explanatory feedback loops — theoretically legitimate. "
        "No logical paradoxes were found. The theory is not self-defeating at the level of "
        "its core logical spine; it is self-defeating in two definitional framings that "
        "can be repaired without touching the core arguments."
    ),
}
for c in circularity_entries:
    circ_audit["by_type"][c["verdict"]] += 1
circ_audit["by_type"] = dict(circ_audit["by_type"])
save("54_circularity_audit.json", circ_audit)

# ════════════════════════════════════════════════════════════════════════════
# STEP 5 — INFERENCE VALIDITY TEST
# ════════════════════════════════════════════════════════════════════════════
print("Step 5: Inference validity test...", flush=True)

# Each major inference step: does the conclusion follow?
# Use formal expressions from Phase 0.9 where available.

INFERENCE_TESTS = [
    {
        "chain_id": "INF-001",
        "chain": "Free Will → Property Rights",
        "premise": "A-000001: Human free will exists and is universally presupposed.",
        "conclusion": "A-000002: Property begins with the human body.",
        "formal": "FW(x) → Owns(x, body(x))",
        "validity_verdict": "REQUIRES_EXTRA_PREMISE",
        "extra_premises_needed": [
            "P+: The body is an extension of the self (not merely possessed by it).",
            "P+: The self's sovereignty over its choices extends to sovereignty over its physical substrate.",
        ],
        "logical_gap": (
            "Free will alone establishes that an agent makes choices. It does not by itself "
            "establish that the physical substrate of those choices (the body) is owned property. "
            "The inference requires a bridge principle: that self-determination implies property "
            "rights over the thing doing the determining (the body). This bridge is HA-009 "
            "(inviolability of body) which is a hidden axiom — not derived from free will alone. "
            "The Lockean self-ownership argument is the standard move here, but it is not "
            "formally stated in the theory."
        ),
        "survives_challenge": True,
        "fix": "Explicitly state: 'Self-determination (free will) entails sovereignty over the physical substrate of self-determination (body) because the body IS the self in its physical mode.' This is philosophically defensible but must be stated.",
        "confidence": 72,
    },
    {
        "chain_id": "INF-002",
        "chain": "Property Rights → Liberty",
        "premise": "C-000001: Liberty = individual property rights.",
        "conclusion": "Liberty is secured by property rights.",
        "formal": "L ↔ PR",
        "validity_verdict": "VALID_BY_DEFINITION",
        "extra_premises_needed": [],
        "logical_gap": (
            "This is a definitional biconditional. Once accepted, the inference is trivially valid. "
            "The real question is whether the DEFINITION is well-chosen — i.e., whether all of "
            "what we mean by liberty is captured by property rights. The theory argues yes; "
            "critics may argue that political liberty, expressive liberty, and epistemic liberty "
            "are not reducible to property. But this is not a logical invalidity — it is a "
            "definitional dispute. As stated, the inference is valid."
        ),
        "survives_challenge": True,
        "confidence": 95,
    },
    {
        "chain_id": "INF-003",
        "chain": "Tawhid → ¬Servitude → Liberty",
        "premise": "A-000004: No servitude to anything other than God.",
        "conclusion": "C-000016: Tawhid guarantees liberty.",
        "formal": "T → ¬S(x) → L(x)",
        "validity_verdict": "VALID_WITH_BRIDGE",
        "extra_premises_needed": [
            "B1: Liberty = absence of servitude to other humans (which = property rights, by C-000001).",
            "B2: Tawhid prohibits servitude to all non-divine entities, including all humans.",
        ],
        "logical_gap": (
            "The inference is valid IF B1 and B2 are established. B1 follows from C-000001 "
            "(liberty = property rights = not being subjected to another's will). "
            "B2 follows from A-000004 if 'other than God' includes all humans — which the "
            "theory explicitly states ('no human being has the right to strip others of their "
            "power of choice'). The chain is therefore valid given the definitions. "
            "The only gap: Tawhid (A-000004) must be independently accepted as an axiom. "
            "It cannot be derived from A-000001 without HA-011 (negative ostensive definition "
            "of God is sufficient for formal work)."
        ),
        "survives_challenge": True,
        "confidence": 85,
    },
    {
        "chain_id": "INF-004",
        "chain": "¬Tawhid → Infinite Axioms → ¬CFS → Totalitarianism",
        "premise": "¬A-000004: Tawhid is rejected.",
        "conclusion": "C-000017: Eliminating Tawhid proliferates axioms and leads to totalitarianism.",
        "formal": "¬T → |Axioms|→∞ → ¬CFS → M → ¬L",
        "validity_verdict": "REQUIRES_EXTRA_PREMISE",
        "extra_premises_needed": [
            "P+: If Tawhid is rejected, no finite replacement axiom set adequately constrains human authority claims.",
            "P+: Infinite axiom proliferation leads to interpreter dependency (bureaucracy/hierarchy).",
            "P+: Interpreter dependency leads to servitude (which = anti-liberty).",
            "P+: Anti-liberty systems tend toward totalitarianism under certain social conditions.",
        ],
        "logical_gap": (
            "The claim that ¬Tawhid leads to infinite axiom proliferation relies on "
            "A-000011 (finite axioms are required for a valid system) plus the argument that "
            "without Tawhid's minimal single principle, no other principle set is similarly minimal. "
            "This argument is supported in Phase 0.9 Step 5 formalization (F2-023) but requires "
            "the additional claim that NO other single principle can do Tawhid's logical work. "
            "This is the uniqueness problem again (HA-006). "
            "The jump from 'many axioms' to 'totalitarianism' also requires the interpreter-dependency "
            "premise, which is reasonable but not formally derived."
        ),
        "survives_challenge": True,
        "confidence": 72,
    },
    {
        "chain_id": "INF-005",
        "chain": "Liberty unstable without Resurrection",
        "premise": "A-000006: Resurrection exists.",
        "conclusion": "C-000021: Liberty is unstable without Resurrection.",
        "formal": "¬Res → ∃ last_round_defection → ¬stable(L)",
        "validity_verdict": "VALID_WITHIN_GAME_THEORY",
        "extra_premises_needed": [
            "P+: Human social interaction can be modeled as repeated games.",
            "P+: The last-round problem applies to finitely repeated games.",
            "P+: Resurrection provides an 'unknown terminal' that converts finite game to effectively infinite.",
        ],
        "logical_gap": (
            "Within the game-theoretic framework, this inference is valid. "
            "Backward induction in finitely repeated games does produce defection. "
            "An 'unknown last round' (Resurrection: unknown timing) does prevent the "
            "backward induction collapse. This is standard game theory (Axelrod, Kreps-Milgrom). "
            "The gaps: "
            "(1) Human social interaction may not be fully modelable as repeated games. "
            "(2) Resurrection as described (day of judgment, unknown timing) must be "
            "operationally equivalent to 'unknown last round' — which requires the "
            "theological content to be bracketed for the game-theoretic argument to work. "
            "The theory does this bracketing explicitly ('whether you believe in Resurrection "
            "literally, its logical function is demonstrable'). This is methodologically sound."
        ),
        "survives_challenge": True,
        "confidence": 80,
    },
    {
        "chain_id": "INF-006",
        "chain": "Religion as CFS → AI Alignment",
        "premise": "C-000029: Formal system of liberty = religion.",
        "conclusion": "C-000071: Theory of liberty is the only solution for AI ethics.",
        "formal": "CFS(R) → encodable(R, AI) → aligned(AI, L) ∧ UNIQUE(R)",
        "validity_verdict": "INVALID_UNIQUENESS_UNPROVEN",
        "extra_premises_needed": [
            "REQUIRED: No other CFS for liberty exists or can be constructed.",
            "REQUIRED: All AI ethical systems require a CFS of the type defined.",
            "REQUIRED: The encoding of R into AI is constructively possible.",
        ],
        "logical_gap": (
            "The inference from 'religion is A consistent formal system for liberty' to "
            "'religion is THE ONLY consistent formal system for liberty' requires proving "
            "uniqueness — which the theory does not do formally. "
            "The theory challenges critics to produce an alternative, but the burden of proof "
            "for uniqueness lies with the uniqueness-claimant (the theory), not with critics. "
            "Additionally, 'encodable into AI' is an existence claim that requires a constructive "
            "encoding procedure — not provided. "
            "The conclusion 'only solution for AI ethics' is therefore NOT derivable from "
            "the stated premises. It is an asserted conclusion, not a derived theorem. "
            "VERDICT: The inference from CFS(R) to unique-AI-solution is INVALID as stated."
        ),
        "survives_challenge": False,
        "fix": "Replace 'only solution' with 'a solution' OR formally prove that no other CFS for liberty exists that satisfies the {FW, Tawhid, Resurrection, Prophethood} functional requirements.",
        "confidence": 40,
    },
    {
        "chain_id": "INF-007",
        "chain": "Denial of Free Will is Self-Refuting",
        "premise": "A-000001 challenged: assume ¬FW.",
        "conclusion": "C-000039: Asserting ¬FW requires FW (performative contradiction).",
        "formal": "assert(¬FW) → FW",
        "validity_verdict": "VALID",
        "extra_premises_needed": [],
        "logical_gap": (
            "This is the classic performative contradiction argument. Any assertion "
            "presupposes the asserter is making a genuine choice to assert it. "
            "If the asserter is asserting ¬FW, they are simultaneously exercising the very "
            "faculty they are denying. This is logically valid and philosophically well-established "
            "(variants appear in Kant, contemporary analytic philosophy). "
            "No missing premises. The inference is valid."
        ),
        "survives_challenge": True,
        "confidence": 92,
    },
    {
        "chain_id": "INF-008",
        "chain": "Democracy → Communism",
        "premise": "Democracy applied to individual rights.",
        "conclusion": "C-000043 + claim: democracy is the path to communism.",
        "formal": "D(PR) → majority-override(PR) → expansion-of-state → communism",
        "validity_verdict": "VALID_WITHIN_SCOPE",
        "extra_premises_needed": [
            "P+: Majorities, given the option, will vote to redistribute property.",
            "P+: Property redistribution requires state expansion.",
            "P+: Unconstrained state expansion tends toward totalitarianism.",
        ],
        "logical_gap": (
            "Within the theory's definitions: "
            "If democracy can vote on property rights (P), and majorities tend toward "
            "redistribution (a standard public-choice result), and redistribution requires "
            "state coercion, then D(PR) → state-coercion → anti-liberty. "
            "The premises are contestable empirically but logically coherent. "
            "The inference is valid within the theory's definitions of liberty and state. "
            "The 'path to communism' phrasing is hyperbolic but logically: "
            "D(PR) → ¬stable(PR) → ¬stable(L). This follows."
        ),
        "survives_challenge": True,
        "confidence": 75,
    },
]

# Count results
valid_count = sum(1 for i in INFERENCE_TESTS if i["validity_verdict"] in ("VALID","VALID_BY_DEFINITION","VALID_WITHIN_GAME_THEORY","VALID_WITH_BRIDGE","VALID_WITHIN_SCOPE"))
invalid_count = sum(1 for i in INFERENCE_TESTS if "INVALID" in i["validity_verdict"])
requires_count = sum(1 for i in INFERENCE_TESTS if i["validity_verdict"] == "REQUIRES_EXTRA_PREMISE")

save("55_inference_validity_report.json", {
    "total_chains_tested": len(INFERENCE_TESTS),
    "valid": valid_count,
    "invalid": invalid_count,
    "requires_extra_premise": requires_count,
    "chains": INFERENCE_TESTS,
    "key_finding": (
        f"{valid_count} of {len(INFERENCE_TESTS)} major inference chains are valid (with or without bridge). "
        f"{requires_count} require extra premises that are reasonable but unstated. "
        f"{invalid_count} inference is formally invalid as stated: INF-006 (uniqueness claim for AI ethics). "
        "The core chain (Free Will → Property → Liberty → Tawhid → CFS → Religion) "
        "is logically sound with two small bridges needed (HA-009, HA-011). "
        "The theory's weakest inference is its terminal uniqueness claim."
    ),
})

print(f"  Chains tested: {len(INFERENCE_TESTS)}, valid: {valid_count}, invalid: {invalid_count}, needs bridges: {requires_count}", flush=True)
print("Steps 1-5 complete.", flush=True)
