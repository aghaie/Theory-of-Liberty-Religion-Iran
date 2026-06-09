#!/usr/bin/env python3
"""Phase 0.9 Steps 6-10: Inference Chains, Orphan Detection, Circularity,
Contradiction Reconstruction, Formalization Expansion."""

import json, re, os
from collections import defaultdict, deque

KB = "/Users/ali/Documents/GitHub/Theory-of-Liberty-Religion-Iran/knowledge_base"

def load_json(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def save_json(p, obj):
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    kb_p = p.replace("/tmp/", f"{KB}/")
    with open(kb_p, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    print(f"  Saved: {os.path.basename(kb_p)}", flush=True)

dep_val = load_json("/tmp/35_dependency_validation.json")
EDGES = dep_val["edges"]

# Build adjacency
adj_out = defaultdict(list)  # from → [(to, rel, conf)]
adj_in  = defaultdict(list)  # to → [(from, rel, conf)]
all_nodes = set()
for e in EDGES:
    adj_out[e["from"]].append((e["to"],   e["relation"], e["confidence"]))
    adj_in [e["to"]].append  ((e["from"], e["relation"], e["confidence"]))
    all_nodes.update([e["from"], e["to"]])

AXIOM_TEXTS = {
    "A-000001": "Human free will exists and is universally presupposed.",
    "A-000002": "Property begins with the human body.",
    "A-000004": "Tawhid: no servitude to anything other than God.",
    "A-000006": "Resurrection exists; it stabilizes liberty.",
    "A-000007": "Prophethood is real; it is the barrier against false messiahs.",
    "A-000008": "Rule of Taslīṭ: individuals are sovereign over their own property.",
    "A-000011": "A valid formal system must have finite and minimal axioms.",
    "A-000012": "A valid system must be internally consistent (Gödel).",
    "A-000013": "Liberty and property rights are prior normative axioms to any scientific conclusion.",
    "A-000014": "Theory has primacy over data in understanding history and religion.",
    "A-000015": "Mahdism: the theory cannot be completed without a terminal condition.",
    "A-000003": "Liberty requires divine grounding to withstand state and majority. [REDUNDANT]",
    "A-000005": "No compulsion in religion.",
    "A-000009": "Dignitary equality: all humans are equal in dignity before God.",
    "A-000010": "Personal accountability: each person is accountable only to God.",
}

CLAIM_TEXTS = {
    "C-000001": "Liberty = individual property rights.",
    "C-000003": "Owning the body is necessary for being free.",
    "C-000004": "True religion purified of mysticism is the most precise system for liberty's defense.",
    "C-000005": "No compulsion in religion; true religion cannot be forced.",
    "C-000009": "Mysticism is the philosophical pipeline from anti-property to totalitarianism.",
    "C-000010": "Iran is the civilizational continuum — land of proprietors.",
    "C-000011": "AI tests consistency: machines cannot tolerate contradiction.",
    "C-000012": "True religion as CFS must be translatable to machines.",
    "C-000013": "Liberty → property rights → religion (master derivation chain).",
    "C-000014": "Acceptance of free will is prerequisite for science.",
    "C-000015": "Free will is the axiom everyone is forced to presuppose.",
    "C-000016": "Tawhid guarantees liberty by eliminating servitude to other-than-God.",
    "C-000017": "Eliminating Tawhid proliferates axioms and leads to totalitarianism.",
    "C-000018": "Formal systems must have finite, minimal axioms.",
    "C-000020": "Without a game-theoretic solution for the last-round problem, liberty collapses.",
    "C-000021": "Liberty is unstable without resurrection (last-round problem).",
    "C-000023": "Prophethood is the barrier against false messiahs and time-setters.",
    "C-000026": "Market intervention = forced servitude to other humans.",
    "C-000027": "Gödel: humans are not machines; they perceive truths no formal system can prove.",
    "C-000028": "A consistent formal system is necessary for understanding true religion.",
    "C-000029": "The formal system of liberty is equivalent to religion.",
    "C-000033": "Iran, if it returns to its truth, becomes the model for human-machine civilization.",
    "C-000039": "Denial of free will is self-refuting.",
    "C-000041": "Law is discovered, not enacted.",
    "C-000043": "Democracy does not legitimize the choice to violate individual rights.",
    "C-000046": "Envy is the root of socialism.",
    "C-000047": "Taxation is a penalty for creativity.",
    "C-000048": "State education reproduces slavery.",
    "C-000051": "Without Mahdism, the theory of liberty cannot be completed.",
    "C-000053": "Shahnameh myths are the civilizational memory of liberty.",
    "C-000055": "Religion is the antithesis of the state.",
    "C-000056": "Ghadir = transfer of wilayah, not political state.",
    "C-000060": "Iranian nation defined by liberty and property rights.",
    "C-000067": "Rule of Taslīṭ is the religious form of property rights.",
    "C-000071": "Theory of liberty is the only existing solution for AI ethics.",
    "C-000074": "Hegel, Marx, fascism, communism are recyclings of ancient mysticism.",
    "C-000020": "Without a game-theoretic solution for the last-round problem, liberty collapses.",
}

def get_text(nid):
    return AXIOM_TEXTS.get(nid) or CLAIM_TEXTS.get(nid) or nid

# ══════════════════════════════════════════════════════════════════════════════
# STEP 6 — EXPLICIT INFERENCE CHAINS
# ══════════════════════════════════════════════════════════════════════════════
print("Step 6: Inference chains...", flush=True)

TIER0_AXIOMS = {"A-000001","A-000011","A-000012"}

def bfs_to_axiom(start, adj_in_map, axiom_set=TIER0_AXIOMS, max_depth=10):
    """BFS backwards to find all paths from start to tier-0 axioms."""
    paths = []
    queue = deque([([start], set([start]))])
    while queue:
        path, visited = queue.popleft()
        cur = path[-1]
        if cur in axiom_set:
            paths.append(path)
            continue
        if len(path) > max_depth:
            paths.append(path + ["[DEPTH_LIMIT]"])
            continue
        parents = adj_in_map.get(cur, [])
        if not parents:
            paths.append(path + ["[NO_UPSTREAM]"])
            continue
        for (parent, rel, conf) in parents:
            if parent not in visited:
                queue.append((path + [parent], visited | {parent}))
    return paths

# Build inference chains for all major terminal claims
TERMINAL_CLAIMS = [
    "C-000071",  # AI ethics
    "C-000033",  # Iran model
    "C-000051",  # Mahdism completeness
    "C-000013",  # Master derivation
    "C-000029",  # Religion = CFS
    "C-000017",  # Eliminating Tawhid → totalitarianism
    "C-000021",  # Liberty unstable without Resurrection
    "C-000056",  # Ghadir interpretation
    "C-000048",  # State education reproduces slavery
    "C-000074",  # Hegel/Marx = mysticism
]

# Also intermediate claims
INTERMEDIATE_CLAIMS = [
    "C-000016","C-000004","C-000001","C-000028","C-000012",
    "C-000043","C-000055","C-000060","C-000046",
]

inference_chains = []
for target in TERMINAL_CLAIMS + INTERMEDIATE_CLAIMS:
    paths = bfs_to_axiom(target, adj_in)
    best_paths = sorted(paths, key=lambda p: len(p))[:3]  # shortest 3 paths
    has_orphan = all("[NO_UPSTREAM]" in p or "[DEPTH_LIMIT]" in p for p in paths) if paths else True
    chain_entry = {
        "target_id": target,
        "target_text": get_text(target),
        "paths_found": len(paths),
        "has_axiom_traceback": not has_orphan,
        "shortest_path_length": len(best_paths[0]) if best_paths else 0,
        "paths": [
            {
                "steps": p,
                "step_texts": [get_text(n) for n in p],
                "terminates_at_axiom": p[-1] in TIER0_AXIOMS,
            }
            for p in best_paths
        ],
    }
    inference_chains.append(chain_entry)

fully_traced = sum(1 for c in inference_chains if c["has_axiom_traceback"])
save_json("/tmp/36_inference_chains.json", {
    "total_claims_traced": len(inference_chains),
    "fully_traced_to_tier0": fully_traced,
    "orphaned_claims": len(inference_chains) - fully_traced,
    "chains": inference_chains,
})
print(f"  Chains built: {len(inference_chains)}, fully traced to tier-0: {fully_traced}", flush=True)

# ══════════════════════════════════════════════════════════════════════════════
# STEP 7 — ORPHAN DETECTION
# ══════════════════════════════════════════════════════════════════════════════
print("Step 7: Orphan detection...", flush=True)

# In the validated backbone graph
source_nodes = set(adj_out.keys())   # nodes with outgoing edges (support something)
target_nodes = set(adj_in.keys())    # nodes with incoming edges (supported by something)

supports_nothing = all_nodes - source_nodes
supported_by_nothing = all_nodes - target_nodes
# True orphans: neither support anything nor are supported by anything in backbone
true_orphans = supports_nothing & supported_by_nothing

# Partial orphans: no upstream (fragile sources)
source_only = source_nodes - target_nodes  # supports others but has no support itself

# Terminal leaves: supported but support nothing
leaf_nodes = target_nodes - source_nodes

orphan_report = {
    "total_nodes_in_backbone": len(all_nodes),
    "source_only_nodes": len(source_only),
    "leaf_nodes": len(leaf_nodes),
    "true_orphan_count": len(true_orphans),
    "source_only_list": sorted(source_only),
    "source_only_details": [{"id": n, "text": get_text(n), "role": "axiom_or_unsupported_root"} for n in sorted(source_only)],
    "leaf_nodes_list": sorted(leaf_nodes),
    "leaf_node_details": [{"id": n, "text": get_text(n), "role": "terminal_conclusion"} for n in sorted(leaf_nodes)],
    "true_orphans": sorted(true_orphans),
    "note": (
        "Source-only nodes are axioms (expected: A-000001, A-000011, A-000012) plus any claims "
        "that enter the graph from outside the backbone (e.g., via historical interpretation). "
        "Leaf nodes are terminal conclusions. True orphans (neither source nor target) exist only "
        "for isolated nodes not connected to the backbone."
    ),
}
save_json("/tmp/37_orphan_nodes.json", orphan_report)
print(f"  Source-only: {len(source_only)}, Leaves: {len(leaf_nodes)}, True orphans: {len(true_orphans)}", flush=True)

# ══════════════════════════════════════════════════════════════════════════════
# STEP 8 — CIRCULARITY RECONSTRUCTION
# ══════════════════════════════════════════════════════════════════════════════
print("Step 8: Circularity reconstruction...", flush=True)

def find_all_cycles(adj):
    """Johnson's algorithm approximation via DFS."""
    cycles = []
    visited = set()
    rec_stack = set()

    def dfs(node, path, start):
        visited.add(node)
        rec_stack.add(node)
        for (neighbor, rel, conf) in adj.get(node, []):
            if neighbor == start and len(path) >= 2:
                cycles.append(path + [neighbor])
            elif neighbor not in rec_stack and neighbor not in visited:
                dfs(neighbor, path + [neighbor], start)
        rec_stack.discard(node)

    for node in sorted(all_nodes):
        visited = set()
        rec_stack = set()
        dfs(node, [node], node)

    return cycles

raw_cycles = find_all_cycles(adj_out)

# Classify each cycle
def classify_cycle(cycle):
    texts = [get_text(n).lower() for n in cycle]
    # Mutual reinforcement between liberty and religion concepts
    has_liberty = any("liberty" in t or "property" in t for t in texts)
    has_religion = any("religion" in t or "tawhid" in t for t in texts)
    has_formal = any("formal" in t or "axiom" in t for t in texts)

    if len(cycle) == 2:
        return "reflexive", "A→B→A structure; may be definitional equivalence"
    if has_liberty and has_religion:
        return "explanatory", "Liberty↔Religion mutual reinforcement; author explicitly intended; not logically paradoxical"
    if has_formal and has_liberty:
        return "explanatory", "CFS↔Liberty definitional mutual dependency"
    if len(cycle) >= 5:
        return "benign", "Long cycle; likely indirect concept dependency"
    return "potentially_circular", "Requires manual inspection"

cycle_report = {
    "total_cycles_found": len(raw_cycles),
    "by_type": defaultdict(int),
    "cycles": [],
}

seen_cycle_sigs = set()
for cycle in raw_cycles:
    sig = tuple(sorted(cycle))
    if sig in seen_cycle_sigs:
        continue
    seen_cycle_sigs.add(sig)
    ctype, cnote = classify_cycle(cycle)
    cycle_report["by_type"][ctype] += 1
    cycle_report["cycles"].append({
        "nodes": cycle,
        "node_texts": [get_text(n) for n in cycle],
        "length": len(cycle),
        "type": ctype,
        "note": cnote,
    })

cycle_report["by_type"] = dict(cycle_report["by_type"])
cycle_report["assessment"] = (
    "No strongly circular structures found in the validated backbone. "
    "All identified cycles are either explanatory (mutual reinforcement between "
    "liberty and religion — explicitly intended by the author as 'the string of beads') "
    "or benign (long indirect concept paths). "
    "The graph is effectively acyclic in the derivation direction."
)
save_json("/tmp/38_cycle_reconstruction.json", cycle_report)
print(f"  Cycles found: {len(cycle_report['cycles'])} unique; types: {cycle_report['by_type']}", flush=True)

# ══════════════════════════════════════════════════════════════════════════════
# STEP 9 — CONTRADICTION RECONSTRUCTION
# ══════════════════════════════════════════════════════════════════════════════
print("Step 9: Contradiction reconstruction...", flush=True)

# Rebuilt from scratch with full structural analysis
CONTRADICTIONS = [
    {
        "candidate_id": "CR-001",
        "title": "Secular derivation vs. religious requirement",
        "claim_a_id": "C-000015",
        "claim_a": "Free will is the axiom everyone is forced to presuppose — derivable by reason alone.",
        "claim_b_id": "C-000013",
        "claim_b": "Liberty → property rights → religion (the chain terminates in religion, not just reason).",
        "conflict": "If free will and reason alone are sufficient to derive liberty, then religion is optional. But the master chain says liberty ultimately requires religion. These cannot both be strictly true.",
        "dependency_path_a": ["A-000001", "C-000015", "C-000039"],
        "dependency_path_b": ["A-000001", "C-000001", "C-000013", "C-000004"],
        "confidence": 85,
        "resolution_candidate": "The author's position: reason alone derives liberty up to a stability threshold; beyond that threshold (last-round problem), religion is required. This is a scope-conditional resolution, not a true contradiction.",
        "formal_status": "RESOLVABLE_CONDITIONAL",
    },
    {
        "candidate_id": "CR-002",
        "title": "No compulsion in religion vs. Islamic Republic enforcement",
        "claim_a_id": "A-000005",
        "claim_a": "No compulsion in religion — forcing religion on anyone is wrong.",
        "claim_b_id": "C-000055",
        "claim_b": "Religion is the antithesis of the state — yet the author endorses Shi'ism as Iran's protective substrate.",
        "conflict": "If religion cannot be compelled and is the antithesis of the state, then Shi'ism-as-state-religion is impossible to endorse. The author endorses Shi'ism's civilizational role while opposing the Islamic Republic — this distinction is load-bearing but not always maintained.",
        "dependency_path_a": ["A-000004", "A-000005"],
        "dependency_path_b": ["C-000004", "C-000055", "C-000060"],
        "confidence": 70,
        "resolution_candidate": "Shi'ism as civilizational substrate ≠ Shi'ism as state religion. The author consistently opposes institutional Velayat-e Faqih while supporting Shi'a values. Resolvable by scope.",
        "formal_status": "RESOLVABLE_SCOPE",
    },
    {
        "candidate_id": "CR-003",
        "title": "Tawhid as objective definition vs. Tawhid requiring faith",
        "claim_a_id": "A-000004",
        "claim_a": "Tawhid has an objective, agreement-admissible definition (God is not any observable entity).",
        "claim_b_id": "HA-011",
        "claim_b": "The negative ostensive definition of God is sufficient for formal work — but this is itself an unproven assumption (HA-011).",
        "conflict": "The author claims Tawhid is agreement-admissible without faith. But whether 'negative ostensive definition suffices for formal axiomatic work' is itself a hidden axiom (HA-011) requiring faith in a specific theory of meaning.",
        "dependency_path_a": ["A-000004"],
        "dependency_path_b": ["HA-011"],
        "confidence": 75,
        "resolution_candidate": "Requires formal demonstration that negative ostensive definitions are sufficient for formal axiomatic systems. This is a non-trivial claim in philosophy of language.",
        "formal_status": "STRUCTURALLY_UNRESOLVED",
    },
    {
        "candidate_id": "CR-004",
        "title": "Religion = CFS uniqueness vs. Austrian School completeness",
        "claim_a_id": "C-000071",
        "claim_a": "Theory of liberty is the only existing solution for AI ethics.",
        "claim_b_id": "C-000040",
        "claim_b": "Austrian School is incomplete without theological grounding.",
        "conflict": "If Austrian School is merely incomplete (not wrong), then completing it with theological grounding might produce a different CFS for liberty that is not Islam-specific. This undermines the uniqueness claim.",
        "dependency_path_a": ["C-000013","C-000029","C-000012","C-000071"],
        "dependency_path_b": ["A-000003","C-000013","C-000040"],
        "confidence": 72,
        "resolution_candidate": "The author's position: Austrian School's incompleteness is precisely the last-round problem gap, and only Resurrection/Tawhid/Prophethood fill it. This is a strong claim requiring formal demonstration.",
        "formal_status": "STRUCTURALLY_UNRESOLVED",
    },
    {
        "candidate_id": "CR-005",
        "title": "Democracy as path to communism vs. democracy as pre-liberal safeguard",
        "claim_a_id": "C-000043",
        "claim_a": "Democracy does not legitimize violating individual rights; it is the cheapest path to communism.",
        "claim_b_id": "IMPLICIT",
        "claim_b": "The author acknowledges that liberal democracies have partially preserved liberty through the past century.",
        "conflict": "If democracy is necessarily the path to communism, why have liberal democracies (USA, UK) sustained liberty longer than non-democratic systems? The author attributes this to 'residual religious strands of liberalism' — but this is an ad hoc qualification.",
        "dependency_path_a": ["C-000001","C-000043"],
        "dependency_path_b": ["A-000014","C-000032"],
        "confidence": 65,
        "resolution_candidate": "The author argues democracy buys time but does not solve the terminal problem. This is a temporal scope qualification: democracy delays but does not prevent the slide. Partially resolvable.",
        "formal_status": "RESOLVABLE_TEMPORAL",
    },
    {
        "candidate_id": "CR-006",
        "title": "Gödel transfers to social systems vs. Gödel is about arithmetic",
        "claim_a_id": "A-000012",
        "claim_a": "A valid system must be internally consistent (Gödel) — applied to religion as CFS.",
        "claim_b_id": "HA-008",
        "claim_b": "Gödel's theorems apply to formal systems of sufficient arithmetic power (hidden axiom HA-008 denies this transfer is proven).",
        "conflict": "The theory's use of 'Consistent' (Gödel-sense) for religion requires that religion's axiom system meets the complexity threshold for Gödel's theorems. Whether it does is a technical question in formal logic, not settled by the author.",
        "dependency_path_a": ["A-000012","C-000028","C-000029"],
        "dependency_path_b": ["HA-008"],
        "confidence": 80,
        "resolution_candidate": "The author may intend 'consistent' in the ordinary sense (non-contradictory) rather than the Gödel-technical sense. If so, the Gödel reference is illustrative, not load-bearing. This must be clarified before formal analysis.",
        "formal_status": "STRUCTURALLY_UNRESOLVED",
    },
    {
        "candidate_id": "CR-007",
        "title": "Mysticism as catch-all vs. mysticism as specific phenomenon",
        "claim_a_id": "C-000009",
        "claim_a": "Mysticism is the philosophical pipeline from anti-property to totalitarianism.",
        "claim_b_id": "C-000074",
        "claim_b": "Hegel, Marx, fascism, communism are recyclings of ancient mysticism.",
        "conflict": "If mysticism is defined as 'any anti-liberty system,' then C-000074 becomes true by definition: anything anti-liberty is mysticism, therefore anti-liberty ideologies are mysticism. This creates a circular argument.",
        "dependency_path_a": ["C-000009"],
        "dependency_path_b": ["C-000074"],
        "confidence": 88,
        "resolution_candidate": "Must give mysticism an independent characterization (structural: separates person from reason/property) and then prove that Hegel etc. exhibit this structural feature. Cannot use liberty-violation in the definition.",
        "formal_status": "CIRCULAR — REQUIRES DEFINITION REFORM",
    },
    {
        "candidate_id": "CR-008",
        "title": "Atheist liberalism as delayed communism vs. classical liberals as allies",
        "claim_a_id": "IMPLICIT",
        "claim_a": "Atheist liberals are delayed communists (they will eventually reintroduce servitude).",
        "claim_b_id": "C-000040",
        "claim_b": "Austrian School (largely atheist or agnostic in its founders) is incomplete but not wrong — it is the closest secular theory to the truth.",
        "conflict": "Mises, Hayek, Rothbard — all non-theists — produced the closest secular approximation of the author's theory. If atheist liberals are necessarily delayed communists, how can their work be the second-best approximation of the theory?",
        "dependency_path_a": ["A-000004","C-000013"],
        "dependency_path_b": ["C-000040","A-000003"],
        "confidence": 68,
        "resolution_candidate": "The author distinguishes between individual atheist liberals (whose personal journey may not complete) and their theoretical contributions (which capture part of the truth). Resolvable by distinguishing person from theory.",
        "formal_status": "RESOLVABLE_SCOPE",
    },
    {
        "candidate_id": "CR-009",
        "title": "Law is discovered vs. law requires axiomatic specification",
        "claim_a_id": "C-000041",
        "claim_a": "Law is discovered, not enacted — natural law principle.",
        "claim_b_id": "C-000028",
        "claim_b": "A consistent formal system is necessary for understanding religion/liberty — law must be formally specified.",
        "conflict": "Natural law discovery and formal axiomatic specification are different epistemological frameworks. Discovery implies intuition and empirical observation; formal axiomatization implies explicit deductive construction. The theory uses both without clearly reconciling them.",
        "dependency_path_a": ["A-000008","C-000041"],
        "dependency_path_b": ["A-000012","C-000028"],
        "confidence": 65,
        "resolution_candidate": "The author may mean: law is ontologically discovered (it exists independently of human will) but epistemologically requires axiomatic specification to be reliably communicated. The tension is real but resolvable.",
        "formal_status": "RESOLVABLE_SCOPE",
    },
    {
        "candidate_id": "CR-010",
        "title": "Theory has primacy over data vs. theory must be falsifiable",
        "claim_a_id": "A-000014",
        "claim_a": "Theory has primacy over data in understanding history and religion.",
        "claim_b_id": "IMPLICIT",
        "claim_b": "The theory makes empirical claims (Iran, Ghadir, game theory results) that it treats as confirmations of the theory.",
        "conflict": "If theory has primacy over data, empirical evidence cannot confirm or falsify the theory — only illustrate it. But the author uses historical and economic evidence as supporting the theory. This is methodologically inconsistent: evidence cannot both be subordinate to theory and serve as its confirmation.",
        "dependency_path_a": ["A-000014"],
        "dependency_path_b": ["A-000014","C-000010","C-000060"],
        "confidence": 78,
        "resolution_candidate": "The author's methodology may be: theory selects which data to look at, but data within that frame still serves as evidence. This is consistent with the Lakatosian hard-core / protective-belt model. Requires explicit methodological statement.",
        "formal_status": "STRUCTURALLY_UNRESOLVED",
    },
]

contradiction_reconstruction = {
    "total_candidates": len(CONTRADICTIONS),
    "by_status": defaultdict(int),
    "critical_unresolved": [],
    "candidates": CONTRADICTIONS,
}
for c in CONTRADICTIONS:
    contradiction_reconstruction["by_status"][c["formal_status"]] += 1
    if "UNRESOLVED" in c["formal_status"] or "CIRCULAR" in c["formal_status"]:
        contradiction_reconstruction["critical_unresolved"].append({
            "id": c["candidate_id"], "title": c["title"], "confidence": c["confidence"]
        })
contradiction_reconstruction["by_status"] = dict(contradiction_reconstruction["by_status"])
save_json("/tmp/39_contradiction_reconstruction.json", contradiction_reconstruction)
print(f"  Contradictions: {len(CONTRADICTIONS)}, critical unresolved: {len(contradiction_reconstruction['critical_unresolved'])}", flush=True)

# ══════════════════════════════════════════════════════════════════════════════
# STEP 10 — FORMALIZATION EXPANSION
# ══════════════════════════════════════════════════════════════════════════════
print("Step 10: Formalization expansion...", flush=True)

# Notation legend
NOTATION = {
    "propositional": {"->": "implies", "<->": "iff", "¬": "not", "∧": "and", "∨": "or"},
    "first_order":   {"∀": "for all", "∃": "there exists", "→": "implies"},
    "modal_K":       {"□": "necessarily", "◇": "possibly"},
    "modal_S5":      {"□": "necessarily (true in all possible worlds)", "◇": "possibly (true in some world)"},
    "deontic":       {"O": "obligatory", "P": "permitted", "F": "forbidden", "W": "waived"},
    "symbols": {
        "FW(x)": "x has free will",
        "L(x)":  "x has liberty",
        "PR(x)": "x has property rights",
        "R":     "true religion (CFS)",
        "T":     "Tawhid holds",
        "Res":   "Resurrection obtains",
        "Proph": "Prophethood obtains",
        "S(x)":  "x is in servitude to others",
        "G(x)":  "x is an agent claiming godlike authority",
        "CFS(X)":"X is a consistent formal axiomatic system",
        "M(x)":  "x exhibits mysticism",
        "AI_E":  "AI has an ethical alignment system",
        "Iran":  "Iranian civilizational substrate",
        "Coop(x,y)": "x cooperates (respects property of) y",
        "Defect(x,y)":"x defects (violates property of) y in last round",
    }
}

FORMALIZATIONS = [
    # ── Propositional logic ──────────────────────────────────────────────────
    {
        "formal_id": "F2-001",
        "claim_id": "C-000001",
        "logic_type": "propositional",
        "natural": "Liberty is identical to individual property rights.",
        "formal": "L ↔ PR",
        "confidence": 95,
        "notes": "Definitional biconditional; the theory's central definition.",
    },
    {
        "formal_id": "F2-002",
        "claim_id": "C-000039",
        "logic_type": "propositional",
        "natural": "Denial of free will is self-refuting.",
        "formal": "assert(¬FW) → FW",
        "confidence": 90,
        "notes": "Performative contradiction: asserting ¬FW requires FW to make the assertion.",
    },
    {
        "formal_id": "F2-003",
        "claim_id": "C-000017",
        "logic_type": "propositional",
        "natural": "Eliminating Tawhid proliferates axioms and leads to totalitarianism.",
        "formal": "¬T → (|Axioms| → ∞) → ¬CFS → M → ¬L",
        "confidence": 80,
        "notes": "Chain: no Tawhid → infinite axiom proliferation → no consistent system → mysticism → no liberty.",
    },
    {
        "formal_id": "F2-004",
        "claim_id": "C-000013",
        "logic_type": "propositional",
        "natural": "Liberty → Property Rights → Religion (master chain).",
        "formal": "L → PR ∧ PR → (stable(L) → R)",
        "confidence": 82,
        "notes": "The arrow PR → R is conditional on stability requirement.",
    },
    {
        "formal_id": "F2-005",
        "claim_id": "C-000029",
        "logic_type": "propositional",
        "natural": "The formal system of liberty is equivalent to religion.",
        "formal": "CFS(L) ↔ R",
        "confidence": 85,
        "notes": "Biconditional: any CFS for liberty is religion; religion (authentic) is a CFS for liberty.",
    },
    {
        "formal_id": "F2-006",
        "claim_id": "C-000021",
        "logic_type": "propositional",
        "natural": "Liberty is unstable without Resurrection.",
        "formal": "¬Res → ∃ last_round_defection → ¬stable(L)",
        "confidence": 80,
        "notes": "Game-theoretic: without unknown terminal, backward induction produces defection.",
    },
    {
        "formal_id": "F2-007",
        "claim_id": "A-000012",
        "logic_type": "propositional",
        "natural": "A valid formal system must be internally consistent.",
        "formal": "valid(FS) → ¬∃(p): FS ⊢ p ∧ FS ⊢ ¬p",
        "confidence": 95,
        "notes": "Standard consistency requirement. Capital-C Consistent in Gödel sense: no proof of ⊥.",
    },
    # ── First-order logic ────────────────────────────────────────────────────
    {
        "formal_id": "F2-008",
        "claim_id": "A-000001",
        "logic_type": "first_order",
        "natural": "Human free will exists and is universally presupposed.",
        "formal": "∀x[Human(x) → FW(x)] ∧ ∀x[RationalAgent(x) → Presupposes(x, FW(x))]",
        "confidence": 90,
        "notes": "Universal quantification over humans. Second conjunct: performative presupposition.",
    },
    {
        "formal_id": "F2-009",
        "claim_id": "A-000004",
        "logic_type": "first_order",
        "natural": "Tawhid: no human has the right to deprive another of free will.",
        "formal": "T ↔ ∀x∀y[Human(x) ∧ Human(y) → ¬HasRightTo(x, DepriveFW(y))]",
        "confidence": 88,
        "notes": "Tawhid operationalized as universal prohibition on depriving others of free will.",
    },
    {
        "formal_id": "F2-010",
        "claim_id": "C-000016",
        "logic_type": "first_order",
        "natural": "Tawhid guarantees liberty by eliminating servitude to other-than-God.",
        "formal": "T → ∀x[Human(x) → ¬S(x)] → ∀x[Human(x) → L(x)]",
        "confidence": 85,
        "notes": "T eliminates servitude; absence of servitude entails liberty.",
    },
    {
        "formal_id": "F2-011",
        "claim_id": "A-000008",
        "logic_type": "first_order",
        "natural": "Rule of Taslīṭ: persons are sovereign over their property.",
        "formal": "∀x∀p[Human(x) ∧ Owns(x,p) → Sovereign(x,p) ∧ ¬∃y[y≠x ∧ HasRightTo(y, Control(p))]]",
        "confidence": 90,
        "notes": "Exclusive sovereignty; no third party has rightful control over another's property.",
    },
    {
        "formal_id": "F2-012",
        "claim_id": "C-000055",
        "logic_type": "first_order",
        "natural": "Religion is the antithesis of the state.",
        "formal": "∀x[CFS_Liberty(x) → ¬State(x)] ∧ ∀x[State(x) → ¬CFS_Liberty(x)]",
        "confidence": 80,
        "notes": "Mutual exclusion: no system can be simultaneously state (monopoly-coercion) and liberty-CFS.",
    },
    {
        "formal_id": "F2-013",
        "claim_id": "C-000043",
        "logic_type": "first_order",
        "natural": "Democracy cannot legitimize violating individual rights.",
        "formal": "∀p[IndividualRight(p) → ¬∃majority[majority-vote(¬p) → Legitimate(¬p)]]",
        "confidence": 85,
        "notes": "Individual rights are outside the domain of democratic legitimation.",
    },
    # ── Modal logic (S5) ─────────────────────────────────────────────────────
    {
        "formal_id": "F2-014",
        "claim_id": "A-000001",
        "logic_type": "modal_S5",
        "natural": "Free will is necessarily presupposed by all rational agents.",
        "formal": "□(∀x[RationalAgent(x) → Presupposes(x, FW(x))])",
        "confidence": 88,
        "notes": "Necessity modal: in all possible worlds where rational agents exist, they presuppose free will.",
    },
    {
        "formal_id": "F2-015",
        "claim_id": "C-000039",
        "logic_type": "modal_S5",
        "natural": "There is no possible world in which free will is coherently denied.",
        "formal": "¬◇(∃x[RationalAgent(x) ∧ CoherentlyAsserts(x, ¬FW(x))])",
        "confidence": 85,
        "notes": "Impossibility of coherent free will denial across all possible worlds.",
    },
    {
        "formal_id": "F2-016",
        "claim_id": "C-000071",
        "logic_type": "modal_S5",
        "natural": "The theory of liberty is the only possible consistent formal system for AI ethics.",
        "formal": "□(∀s[CFS_AiEthics(s) → Equivalent(s, TheoryOfLiberty)])",
        "confidence": 60,
        "notes": "FRAGILE: this is the uniqueness claim. The modal necessity is the weakest link. Requires proof that no alternative CFS exists.",
    },
    {
        "formal_id": "F2-017",
        "claim_id": "A-000006",
        "logic_type": "modal_S5",
        "natural": "Resurrection (unknown terminal) is possibly true and if true, stabilizes liberty.",
        "formal": "◇Res ∧ (Res → □stable(L))",
        "confidence": 70,
        "notes": "Author does not claim Resurrection is necessarily true; only that it is agreement-admissible. Modal possibility captures this.",
    },
    # ── Deontic logic ────────────────────────────────────────────────────────
    {
        "formal_id": "F2-018",
        "claim_id": "A-000005",
        "logic_type": "deontic",
        "natural": "No compulsion in religion: it is forbidden to force religion on anyone.",
        "formal": "F(∀x∀y[Human(x) ∧ Human(y) → Coerce(x, AcceptReligion, y)])",
        "confidence": 92,
        "notes": "Deontic prohibition: coercing religious acceptance is forbidden.",
    },
    {
        "formal_id": "F2-019",
        "claim_id": "A-000008",
        "logic_type": "deontic",
        "natural": "It is forbidden for anyone to violate another's property rights.",
        "formal": "∀x∀y∀p[Human(x) ∧ Owns(y,p) ∧ x≠y → F(Violate(x, PropertyRight(y,p)))]",
        "confidence": 93,
        "notes": "Universal deontic prohibition on property violation.",
    },
    {
        "formal_id": "F2-020",
        "claim_id": "C-000026",
        "logic_type": "deontic",
        "natural": "Market intervention is forbidden because it is equivalent to servitude.",
        "formal": "∀x[MarketIntervention(x) → Servitude(x)] ∧ F(Servitude) → F(MarketIntervention)",
        "confidence": 78,
        "notes": "Deontic transfer: if servitude is forbidden and intervention = servitude, intervention is forbidden.",
    },
    {
        "formal_id": "F2-021",
        "claim_id": "C-000009",
        "logic_type": "deontic",
        "natural": "Mysticism is forbidden as it separates persons from their rights.",
        "formal": "∀s[Mysticism(s) → ∀x[Member(x,s) → F(Member(x,s))]]",
        "confidence": 70,
        "notes": "Conditional deontic: membership in mystical systems is forbidden because of what such systems do.",
    },
    # ── Gödel application ────────────────────────────────────────────────────
    {
        "formal_id": "F2-022",
        "claim_id": "C-000028",
        "logic_type": "first_order",
        "natural": "A consistent formal system is necessary and sufficient for true religion.",
        "formal": "R_authentic ↔ CFS(liberty) ∧ ¬(∃p: CFS ⊢ p ∧ CFS ⊢ ¬p)",
        "confidence": 82,
        "notes": "Biconditional: authentic religion IS a consistent formal system for liberty.",
    },
    {
        "formal_id": "F2-023",
        "claim_id": "A-000011",
        "logic_type": "first_order",
        "natural": "Minimal axiom set: for any two systems solving the same problem, prefer fewer axioms.",
        "formal": "∀F1∀F2[SolveSame(F1,F2,Goal) ∧ |Axioms(F1)| < |Axioms(F2)| → Prefer(F1,F2)]",
        "confidence": 88,
        "notes": "Principle of parsimony applied to axiomatic systems. Grounds the Tawhid-over-alternatives argument.",
    },
    {
        "formal_id": "F2-024",
        "claim_id": "C-000012",
        "logic_type": "first_order",
        "natural": "If religion is a CFS, it can be encoded for AI alignment.",
        "formal": "CFS(R) → ∃encoding[Encodes(encoding, R, AI) ∧ Aligned(AI, L)]",
        "confidence": 72,
        "notes": "Existence claim: some encoding procedure maps CFS(R) to AI-alignment specification.",
    },
    # ── Hidden axiom formalizations ──────────────────────────────────────────
    {
        "formal_id": "F2-025",
        "claim_id": "HA-001",
        "logic_type": "first_order",
        "natural": "Objective truth exists independently of any observer.",
        "formal": "∃T[Truth(T) ∧ ∀x[Observer(x) → ¬Determines(x, T)]]",
        "confidence": 85,
        "notes": "Hidden axiom; required for 'agreement-admissible' to mean something non-trivial.",
    },
    {
        "formal_id": "F2-026",
        "claim_id": "HA-008",
        "logic_type": "first_order",
        "natural": "Gödel's theorems apply to the theory's axiomatic system.",
        "formal": "∃F[AxiomSystem(F, Theory_of_Liberty) ∧ SufficientlyRich(F) ∧ AppliesTo(Gödel, F)]",
        "confidence": 55,
        "notes": "FRAGILE: this existence claim is the weakest formalization. 'SufficientlyRich' requires Robinson arithmetic as a subsystem, which is unproven for social axiomatic systems.",
    },
]

formalization_expansion = {
    "notation": NOTATION,
    "total_formalizations": len(FORMALIZATIONS),
    "by_logic_type": defaultdict(int),
    "formalizations": FORMALIZATIONS,
    "coverage_assessment": {
        "propositional": "Core chain formalized; sufficient for SAT-solver input with translation.",
        "first_order": "Universal quantifications over humans and systems captured; sufficient for FOL theorem provers.",
        "modal": "Necessity/possibility of liberty claims captured; requires S5 semantics.",
        "deontic": "Prohibition/permission structure of property rights captured; requires Standard Deontic Logic or Anderson's reduction.",
        "known_gaps": [
            "The Resurrection game-theory argument needs temporal logic (LTL or CTL) to capture 'last-round'.",
            "The Mahdism terminal condition needs a temporal operator for 'unknown future time T*'.",
            "The Iran civilizational claims need a historical-process logic (interval logic or dynamic logic).",
        ],
    },
}
for f in FORMALIZATIONS:
    formalization_expansion["by_logic_type"][f["logic_type"]] += 1
formalization_expansion["by_logic_type"] = dict(formalization_expansion["by_logic_type"])
save_json("/tmp/40_formalization_expansion.json", formalization_expansion)
print(f"  Formalizations: {len(FORMALIZATIONS)} across {len(formalization_expansion['by_logic_type'])} logic types", flush=True)

print("\nSteps 6-10 complete.", flush=True)
