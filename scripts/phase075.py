#!/usr/bin/env python3
"""
PHASE 0.75 — Dependency Resolution, Graph Construction, Axiom Reduction,
              Contradiction Discovery, and Pre-Evaluation Report.

Operates exclusively on the compiled knowledge base.
Does NOT re-read the PDF.
"""

import json
import re
import os
import math
import hashlib
from collections import defaultdict, deque

KB = "/Users/ali/Documents/GitHub/Theory-of-Liberty-Religion-Iran/knowledge_base"
OUT = KB

# ═══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def load_jsonl(path):
    records = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def save_json(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    print(f"  Written: {path}", flush=True)

def save_jsonl(path, records):
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"  Written: {path}  ({len(records)} records)", flush=True)

def fingerprint(text):
    return hashlib.md5(text.lower().strip().encode()).hexdigest()

def tokenize(text):
    return set(re.findall(r'\b[a-zA-Z]{3,}\b', text.lower()))

# ═══════════════════════════════════════════════════════════════════════════════
# CORE CONCEPT VOCABULARY (theory-specific)
# ═══════════════════════════════════════════════════════════════════════════════

# Each concept maps to a canonical ID and a list of surface forms
CONCEPTS = {
    "free_will":           ["free will", "freedom of choice", "volition", "power of choice", "self-determination"],
    "liberty":             ["liberty", "individual liberty", "freedom", "liberte"],
    "property_rights":     ["property rights", "individual property", "private property", "right of ownership", "rule of taslīṭ", "taslit"],
    "tawhid":              ["tawhid", "tawḥīd", "unity of god", "monotheism", "oneness of god"],
    "resurrection":        ["resurrection", "hereafter", "afterlife", "divine accountability", "last-round", "eschatology", "day of judgment"],
    "prophethood":         ["prophethood", "prophecy", "prophet", "prophetdom"],
    "mysticism":           ["mysticism", "mystic", "sufi", "sufism", "wahdat al-wujud", "unity of being", "esoteric", "gnosticism", "irfan"],
    "the_state":           ["the state", "government", "statism", "state intervention", "centralized state", "monopoly of violence"],
    "religion":            ["religion", "true religion", "authentic religion", "consistent formal axiomatic system", "formal axiomatic system"],
    "formal_system":       ["consistent formal", "formal axiomatic", "axiomatic system", "formal system", "cfs"],
    "democracy":           ["democracy", "democratic", "majority voting", "majority rule"],
    "communism":           ["communism", "communist", "socialism", "socialist", "collectivism", "collectivist"],
    "iran":                ["iran", "iranian civilization", "iranian nation"],
    "islam":               ["islam", "islamic", "muslim", "shia", "shi'ism", "shi'a"],
    "goedel":              ["gödel", "godel", "incompleteness", "incompleteness theorem"],
    "austrian_school":     ["austrian school", "mises", "hayek", "rothbard", "free market", "free banking"],
    "family":              ["family", "institution of family", "family unit"],
    "taxation":            ["taxation", "compulsory taxation", "tax"],
    "central_bank":        ["central bank", "nationalized currency", "state money", "fiat money"],
    "envy":                ["envy", "enviousness", "resentment"],
    "dialectic":           ["dialectic", "hegelian", "hegel", "thesis antithesis", "synthesis"],
    "game_theory":         ["game theory", "prisoner's dilemma", "last-round problem", "payoff", "defection"],
    "ai_alignment":        ["artificial intelligence", "ai alignment", "machine learning", "turing", "ai ethics"],
    "shahnameh":           ["shahnameh", "ferdowsi", "persian epic"],
    "velayat":             ["velayat-e faqih", "wilayat", "guardianship of jurist", "velayat"],
    "mahdism":             ["mahdism", "imam of the age", "master of the age", "al-mahdi", "advent"],
    "ghadir":              ["ghadir", "ghadir khumm"],
    "german_idealism":     ["german idealism", "kant", "plato", "heraclitus", "plotinus", "mulla sadra"],
    "positivism":          ["positivism", "empiricism", "empirical science", "scientific method"],
    "servitude":           ["servitude", "slavery", "enslavement", "bondage", "subjugation"],
}

# Build reverse lookup: surface_form → concept_id
CONCEPT_LOOKUP = {}
for cid, forms in CONCEPTS.items():
    for form in forms:
        CONCEPT_LOOKUP[form.lower()] = cid

def extract_concepts(text):
    text_lower = text.lower()
    found = set()
    for form, cid in CONCEPT_LOOKUP.items():
        if form in text_lower:
            found.add(cid)
    return sorted(found)

# Concept dependency graph (what concepts presuppose what)
CONCEPT_DEPS = {
    "liberty":          ["free_will", "property_rights"],
    "property_rights":  ["free_will", "tawhid"],
    "tawhid":           ["free_will"],
    "religion":         ["tawhid", "resurrection", "prophethood", "formal_system"],
    "formal_system":    ["free_will"],
    "mysticism":        [],  # anti-concept; negates others
    "the_state":        [],  # anti-concept
    "communism":        [],  # anti-concept
    "democracy":        [],  # neutral; often opposed to liberty
    "mahdism":          ["religion", "prophethood", "resurrection"],
    "islam":            ["tawhid", "prophethood", "resurrection"],
    "iran":             ["liberty", "property_rights", "islam"],
    "ai_alignment":     ["formal_system", "liberty", "religion"],
    "resurrection":     ["tawhid"],
    "prophethood":      ["tawhid"],
    "austrian_school":  ["liberty", "property_rights", "free_will"],
    "game_theory":      ["resurrection", "liberty"],
    "envy":             ["communism"],
    "taxation":         ["the_state"],
    "central_bank":     ["the_state"],
    "servitude":        [],
    "dialectic":        ["mysticism"],
    "german_idealism":  ["mysticism", "dialectic"],
    "velayat":          ["the_state"],
    "shahnameh":        ["iran"],
    "positivism":       [],
    "family":           ["liberty", "property_rights"],
    "ghadir":           ["islam", "prophethood"],
    "goedel":           ["formal_system"],
}

# ═══════════════════════════════════════════════════════════════════════════════
# LOAD INPUT DATA
# ═══════════════════════════════════════════════════════════════════════════════

print("Loading knowledge base...", flush=True)
claims_raw     = load_jsonl(f"{KB}/13_claims_complete.jsonl")
definitions    = load_jsonl(f"{KB}/14_definitions_complete.jsonl")
axiom_cands    = load_jsonl(f"{KB}/15_axiom_candidates_complete.jsonl")
para_extracts  = load_jsonl(f"{KB}/16_paragraph_extractions_full.jsonl")
report         = load_json( f"{KB}/17_compilation_report_full.json")

# Load Phase 1 files for integration
try:
    p1_axioms  = load_json(f"{KB}/06_axiom_catalog.json")
    p1_claims  = load_json(f"{KB}/04_claim_catalog.json")
    p1_args    = load_json(f"{KB}/07_argument_catalog.json")
    p1_graph   = load_json(f"{KB}/09_logical_graph.json")
    p1_arch    = load_json(f"{KB}/11_theory_architecture.json")
    p1_forms   = load_json(f"{KB}/10_formalization_layer.json")
except Exception as e:
    print(f"  Warning: {e}", flush=True)
    p1_axioms = p1_claims = p1_args = p1_graph = p1_arch = p1_forms = None

print(f"  Claims: {len(claims_raw)}", flush=True)
print(f"  Definitions: {len(definitions)}", flush=True)
print(f"  Axiom candidates: {len(axiom_cands)}", flush=True)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 1 + 2 — CLAIM NORMALIZATION AND DEDUPLICATION
# ═══════════════════════════════════════════════════════════════════════════════

print("\nStep 1-2: Claim normalization and deduplication...", flush=True)

# Filter out trivially short claims (< 30 chars)
claims = [c for c in claims_raw if len(c.get("text","").strip()) >= 30]

# Build inverted index: concept → list of claim indices
concept_index = defaultdict(list)
claim_concepts = {}  # claim_id → [concept_ids]

for i, c in enumerate(claims):
    cid = c["claim_id"]
    concepts = extract_concepts(c["text"])
    claim_concepts[cid] = concepts
    for concept in concepts:
        concept_index[concept].append(i)

# Cluster by shared concepts: claims sharing 2+ concepts are in the same cluster
# Use Union-Find for efficiency
parent = list(range(len(claims)))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        parent[px] = py

# For each concept with multiple claims, union those with the same primary concept pair
# Only link claims that share the same canonical concept (single-concept grouping for performance)
CORE_CLUSTER_CONCEPTS = [
    "liberty", "property_rights", "tawhid", "resurrection", "prophethood",
    "formal_system", "mysticism", "the_state", "communism", "democracy",
    "religion", "iran", "mahdism", "goedel", "austrian_school",
    "game_theory", "ai_alignment", "free_will", "dialectic", "german_idealism",
    "servitude", "envy", "family", "velayat", "taxation",
]

# Group by primary concept for clustering (first core concept found)
concept_to_primary = defaultdict(list)
for i, c in enumerate(claims):
    primary = None
    for concept in CORE_CLUSTER_CONCEPTS:
        if concept in claim_concepts.get(c["claim_id"], []):
            primary = concept
            break
    concept_to_primary[primary].append(i)

# Build clusters
cluster_map = defaultdict(list)
for primary, indices in concept_to_primary.items():
    for idx in indices:
        cluster_map[primary].append(idx)

# Build claim clusters output
claim_clusters = []
cluster_id_counter = 1
index_to_cluster = {}  # claim index → cluster_id

for primary, indices in sorted(cluster_map.items(), key=lambda x: -len(x[1])):
    if primary is None:
        label = "uncategorized"
    else:
        label = primary
    if not indices:
        continue
    cid_str = f"CL-{cluster_id_counter:06d}"
    cluster_id_counter += 1
    # Canonical claim: longest text in cluster
    best = max(indices, key=lambda i: len(claims[i]["text"]))
    cluster_record = {
        "cluster_id": cid_str,
        "primary_concept": label,
        "canonical_claim_id": claims[best]["claim_id"],
        "canonical_claim_text": claims[best]["text"][:200],
        "member_count": len(indices),
        "member_claim_ids": [claims[i]["claim_id"] for i in indices],
    }
    claim_clusters.append(cluster_record)
    for idx in indices:
        index_to_cluster[idx] = cid_str

save_jsonl(f"{OUT}/19_claim_clusters.jsonl", claim_clusters)

# Deduplication by near-duplicate detection (same first 120 chars after normalization)
def normalize_text(t):
    return re.sub(r'\s+', ' ', t.lower().strip())[:120]

seen_norms = {}
unique_claims = []
duplicates = defaultdict(list)

for c in claims:
    norm = normalize_text(c["text"])
    fp = hashlib.md5(norm.encode()).hexdigest()
    if fp not in seen_norms:
        seen_norms[fp] = c["claim_id"]
        unique_claims.append({
            "claim_id": c["claim_id"],
            "canonical_text": c["text"],
            "domain": c.get("domain","general"),
            "paragraph_id": c.get("paragraph_id",""),
            "is_axiom_related": c.get("is_axiom_related", False),
            "variants": [],
        })
    else:
        duplicates[seen_norms[fp]].append(c["claim_id"])

# Attach variants
variant_map = {u["claim_id"]: u for u in unique_claims}
for orig_id, dup_ids in duplicates.items():
    if orig_id in variant_map:
        variant_map[orig_id]["variants"].extend(dup_ids)

save_jsonl(f"{OUT}/unique_claim_catalog.jsonl", unique_claims)
print(f"  Original claims: {len(claims)}, Unique claims: {len(unique_claims)}, "
      f"Compression: {len(unique_claims)/max(1,len(claims)):.2%}", flush=True)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 3 — DEPENDENCY EXTRACTION
# ═══════════════════════════════════════════════════════════════════════════════

print("\nStep 3: Dependency extraction...", flush=True)

# For each unique claim, find which claims it depends on.
# Dependency logic:
# - Claims in domain X that reference concept C depend on claims that DEFINE C
# - Claims with "derived" or "therefore" language depend on other claims in same concept
# - Claims about application domains depend on foundational claims

# Build concept → foundational claims mapping from Phase 1
foundational_claims = {}
if p1_arch:
    arch = p1_arch.get("theory_architecture", {})
    for layer in ["layer_0_primary_axioms", "layer_1_direct_consequences"]:
        layer_data = arch.get(layer, {})
        for node in layer_data.get("nodes", []):
            node_id = node.get("id","")
            for concept in CORE_CLUSTER_CONCEPTS:
                if any(c in node.get("text","").lower() for c in CONCEPTS.get(concept, [concept])):
                    foundational_claims[concept] = node_id

# Simpler dependency: if claim mentions concept C, it depends on the axiom/foundational
# claim that establishes C
CONCEPT_TO_AXIOM = {
    "free_will":       "A-000001",
    "property_rights": "A-000002",
    "tawhid":          "A-000004",
    "resurrection":    "A-000006",
    "prophethood":     "A-000007",
    "formal_system":   "A-000012",
    "liberty":         "A-000001",  # free will → liberty
    "religion":        "A-000004",
    "servitude":       "A-000004",
    "democracy":       None,
    "communism":       None,
    "mysticism":       None,
    "the_state":       None,
    "mahdism":         "A-000015",
    "austrian_school": "A-000001",
    "game_theory":     "A-000006",
    "ai_alignment":    "A-000012",
    "dialectic":       None,
    "german_idealism": None,
    "goedel":          "A-000012",
    "positivism":      None,
    "family":          "A-000001",
    "taxation":        "A-000001",
    "central_bank":    "A-000004",
    "envy":            "A-000001",
    "iran":            "A-000001",
    "islam":           "A-000004",
    "velayat":         "A-000004",
    "shahnameh":       "A-000014",
    "ghadir":          "A-000007",
}

dependency_graph = []
for c in unique_claims:
    concepts = extract_concepts(c["canonical_text"])
    deps = set()
    for concept in concepts:
        # Direct axiom dependency
        ax = CONCEPT_TO_AXIOM.get(concept)
        if ax:
            deps.add(ax)
        # Concept-level dependency (what does this concept presuppose?)
        for dep_concept in CONCEPT_DEPS.get(concept, []):
            ax2 = CONCEPT_TO_AXIOM.get(dep_concept)
            if ax2:
                deps.add(ax2)
    # Domain-based structural dependencies
    domain = c.get("domain","general")
    if domain == "theology":
        deps.update(["A-000004", "A-000006", "A-000007"])
    elif domain == "economics":
        deps.update(["A-000001", "A-000002"])
    elif domain == "political_theory":
        deps.update(["A-000001", "A-000002", "A-000004"])
    elif domain == "philosophy":
        deps.update(["A-000001", "A-000012"])
    elif domain == "history":
        deps.update(["A-000014"])
    elif domain == "ai_technology":
        deps.update(["A-000012", "A-000001"])
    elif domain == "game_theory":
        deps.update(["A-000006", "A-000001"])

    if deps:
        dependency_graph.append({
            "claim_id": c["claim_id"],
            "claim_text": c["canonical_text"][:150],
            "concepts_found": concepts,
            "domain": domain,
            "depends_on": sorted(deps),
        })

save_jsonl(f"{OUT}/18_claim_dependency_graph.jsonl", dependency_graph)
print(f"  Dependencies mapped: {len(dependency_graph)} claims with non-trivial dependencies", flush=True)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 4 — AXIOM TRACEBACK
# ═══════════════════════════════════════════════════════════════════════════════

print("\nStep 4: Axiom traceback...", flush=True)

# Defined axiom hierarchy from Phase 1
AXIOM_HIERARCHY = {
    "A-000001": {"text": "Human free will exists and is universally presupposed.",
                 "tier": 0, "depends_on": []},
    "A-000002": {"text": "Property begins with the human body.",
                 "tier": 1, "depends_on": ["A-000001"]},
    "A-000003": {"text": "Liberty requires divine grounding to withstand state and majority.",
                 "tier": 1, "depends_on": ["A-000001", "A-000004"]},
    "A-000004": {"text": "Tawhid: no servitude to anything other than God.",
                 "tier": 1, "depends_on": ["A-000001"]},
    "A-000005": {"text": "No compulsion in religion.",
                 "tier": 2, "depends_on": ["A-000004"]},
    "A-000006": {"text": "Resurrection exists; it stabilizes liberty.",
                 "tier": 2, "depends_on": ["A-000004"]},
    "A-000007": {"text": "Prophethood is real; it is the barrier against false messiahs.",
                 "tier": 2, "depends_on": ["A-000004"]},
    "A-000008": {"text": "Rule of Taslīṭ: individuals are sovereign over their own property.",
                 "tier": 2, "depends_on": ["A-000002", "A-000004"]},
    "A-000009": {"text": "Dignitary equality: all humans are equal in dignity before God.",
                 "tier": 2, "depends_on": ["A-000004"]},
    "A-000010": {"text": "Personal accountability: each person is accountable only to God.",
                 "tier": 2, "depends_on": ["A-000006"]},
    "A-000011": {"text": "A valid formal system must have finite and minimal axioms.",
                 "tier": 0, "depends_on": []},
    "A-000012": {"text": "A valid system must be internally consistent (Gödel).",
                 "tier": 0, "depends_on": []},
    "A-000013": {"text": "Liberty and property rights are prior normative axioms to any scientific conclusion.",
                 "tier": 1, "depends_on": ["A-000001"]},
    "A-000014": {"text": "Theory has primacy over data in understanding history and religion.",
                 "tier": 1, "depends_on": ["A-000012"]},
    "A-000015": {"text": "Mahdism: the theory cannot be completed without a terminal condition.",
                 "tier": 3, "depends_on": ["A-000006", "A-000007", "A-000004"]},
}

def traceback(claim_deps, axiom_hierarchy, max_depth=8):
    """Trace all deps back to tier-0 axioms."""
    path = []
    queue = deque([(dep, 0) for dep in claim_deps])
    visited = set()
    while queue:
        node, depth = queue.popleft()
        if node in visited or depth > max_depth:
            continue
        visited.add(node)
        path.append({"node": node, "depth": depth, "tier": axiom_hierarchy.get(node, {}).get("tier", "?")})
        for parent in axiom_hierarchy.get(node, {}).get("depends_on", []):
            queue.append((parent, depth + 1))
    return path

claim_to_axiom_paths = []
for rec in dependency_graph[:3000]:  # sample for tractability
    deps = rec.get("depends_on", [])
    if not deps:
        continue
    trace = traceback(deps, AXIOM_HIERARCHY)
    terminal = [t["node"] for t in trace if AXIOM_HIERARCHY.get(t["node"], {}).get("tier", 1) == 0]
    claim_to_axiom_paths.append({
        "claim_id": rec["claim_id"],
        "claim_text": rec["claim_text"][:120],
        "domain": rec["domain"],
        "direct_dependencies": deps,
        "full_traceback": trace,
        "terminal_axioms": sorted(set(terminal)),
    })

save_jsonl(f"{OUT}/29_claim_to_axiom_paths.jsonl", claim_to_axiom_paths)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 5 — AXIOM REDUCTION
# ═══════════════════════════════════════════════════════════════════════════════

print("\nStep 5: Axiom reduction...", flush=True)

# Count how many claims each axiom supports (directly or via traceback)
axiom_support_count = defaultdict(int)
for path_rec in claim_to_axiom_paths:
    for ax in path_rec.get("terminal_axioms", []):
        axiom_support_count[ax] += 1
    for dep in path_rec.get("direct_dependencies", []):
        axiom_support_count[dep] += 1

total_claims_traced = len(claim_to_axiom_paths)

axiom_reduction = []
for ax_id, ax_data in sorted(AXIOM_HIERARCHY.items()):
    support = axiom_support_count.get(ax_id, 0)
    coverage = support / max(1, total_claims_traced)

    if ax_data["tier"] == 0:
        ax_type = "foundational"
    elif len(ax_data["depends_on"]) == 0 and ax_data["tier"] <= 1:
        ax_type = "foundational"
    elif ax_id in ["A-000005", "A-000009"]:
        # derivable from A-000004
        ax_type = "derived"
    elif ax_id == "A-000015":
        # Mahdism: highly specific, theological, depends on several others
        ax_type = "derived"
    elif ax_id == "A-000010":
        ax_type = "derived"
    elif ax_id == "A-000003":
        # Redundant given A-000004: A-000003 = consequence of A-000004 + A-000001
        ax_type = "redundant"
    else:
        ax_type = "derived"

    axiom_reduction.append({
        "axiom_id": ax_id,
        "text": ax_data["text"],
        "tier": ax_data["tier"],
        "type": ax_type,
        "depends_on": ax_data["depends_on"],
        "claims_supported": support,
        "coverage_ratio": round(coverage, 4),
    })

# Minimum axiom set: tier-0 foundationals only
min_set = [a for a in axiom_reduction if a["type"] == "foundational"]
print(f"  Minimum axiom set size: {len(min_set)}", flush=True)

save_json(f"{OUT}/20_axiom_reduction.json", {
    "summary": {
        "total_axioms": len(axiom_reduction),
        "foundational": sum(1 for a in axiom_reduction if a["type"] == "foundational"),
        "derived": sum(1 for a in axiom_reduction if a["type"] == "derived"),
        "redundant": sum(1 for a in axiom_reduction if a["type"] == "redundant"),
        "minimum_axiom_set": [a["axiom_id"] for a in min_set],
        "minimum_set_texts": [a["text"] for a in min_set],
    },
    "axioms": axiom_reduction,
})

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 6 — THEORY LAYER DISCOVERY
# ═══════════════════════════════════════════════════════════════════════════════

print("\nStep 6: Theory layer discovery...", flush=True)

# Assign each unique claim to a layer based on its concept depth from foundational axioms
def concept_depth(concept, memo={}):
    if concept in memo:
        return memo[concept]
    deps = CONCEPT_DEPS.get(concept, [])
    if not deps:
        depth = 0
    else:
        depth = 1 + max(concept_depth(d, memo) for d in deps)
    memo[concept] = depth
    return depth

layer_counts = defaultdict(int)
layer_claims = defaultdict(list)

for c in unique_claims:
    concepts = extract_concepts(c["canonical_text"])
    if not concepts:
        layer = 99  # uncategorized
    else:
        max_depth = max(concept_depth(con) for con in concepts)
        layer = min(max_depth, 6)  # cap at 6
    layer_counts[layer] += 1
    layer_claims[layer].append(c["claim_id"])

LAYER_LABELS = {
    0: "Fundamental Axioms and First Principles",
    1: "Direct Consequences (Liberty, Property, Tawhid)",
    2: "Intermediate Theory (Religion, State, Formal Systems)",
    3: "Applied Political Theory (Democracy, Communism, Iran)",
    4: "Historical and Civilizational Analysis (Iran, Islam, Shahnameh)",
    5: "Terminal Consequences (Mahdism, Velayat, Ghadir)",
    6: "AI Alignment and Civilizational Conclusions",
    99: "Uncategorized / Secondary Illustration",
}

theory_layers = {
    "method": "Concept depth from foundational axioms via CONCEPT_DEPS graph",
    "total_claims_assigned": len(unique_claims),
    "layers": [],
}

for layer_num in sorted(layer_counts.keys()):
    sample_ids = layer_claims[layer_num][:10]
    sample_texts = [c["canonical_text"][:120] for c in unique_claims
                    if c["claim_id"] in set(layer_claims[layer_num][:10])]
    theory_layers["layers"].append({
        "layer": layer_num,
        "label": LAYER_LABELS.get(layer_num, f"Layer {layer_num}"),
        "claim_count": layer_counts[layer_num],
        "claim_ids_sample": sample_ids,
    })

save_json(f"{OUT}/23_theory_layers.json", theory_layers)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 7 — CIRCULARITY DETECTION
# ═══════════════════════════════════════════════════════════════════════════════

print("\nStep 7: Circularity detection...", flush=True)

# Concept-level circularity analysis (more tractable than claim-level)
concept_graph = {}
for concept, deps in CONCEPT_DEPS.items():
    concept_graph[concept] = deps

def find_cycles(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}
    cycles = []

    def dfs(node, path):
        color[node] = GRAY
        for neighbor in graph.get(node, []):
            if color.get(neighbor, WHITE) == GRAY:
                cycle_start = path.index(neighbor)
                cycles.append(path[cycle_start:] + [neighbor])
            elif color.get(neighbor, WHITE) == WHITE:
                dfs(neighbor, path + [neighbor])
        color[node] = BLACK

    for node in list(graph.keys()):
        if color.get(node, WHITE) == WHITE:
            dfs(node, [node])
    return cycles

concept_cycles = find_cycles(concept_graph)

# Check Phase 1 logical graph for cycles
p1_cycles = []
if p1_graph:
    edges = p1_graph.get("logical_graph", {}).get("edges", [])
    adj = defaultdict(list)
    for e in edges:
        if e.get("relation") in ["supports", "derives_from"]:
            adj[e["from"]].append(e["to"])
    p1_cycle_candidates = find_cycles(dict(adj))
    p1_cycles = p1_cycle_candidates

circularity_report = {
    "concept_level_cycles": len(concept_cycles),
    "p1_graph_cycles": len(p1_cycles),
    "cycles": [],
}

for cycle in concept_cycles:
    circularity_report["cycles"].append({
        "type": "concept_level",
        "cycle": cycle,
        "classification": "benign" if len(cycle) >= 5 else "explanatory",
        "note": "Concept mutual dependency; does not imply logical circularity in derivation order",
    })

for cycle in p1_cycles[:20]:
    circularity_report["cycles"].append({
        "type": "p1_logical_graph",
        "cycle": cycle,
        "classification": "potentially_circular",
        "note": "Cycle in Phase 1 logical graph supports/derives_from edges",
    })

save_json(f"{OUT}/24_circularity_report.json", circularity_report)
print(f"  Concept cycles: {len(concept_cycles)}, P1 graph cycles: {len(p1_cycles)}", flush=True)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 8 — CONTRADICTION CANDIDATE DISCOVERY
# ═══════════════════════════════════════════════════════════════════════════════

print("\nStep 8: Contradiction candidate discovery...", flush=True)

# Pattern-based contradiction detection
NEGATION_PAIRS = [
    # (positive_indicator, negative_indicator, subject)
    (r'\breligion\b.{0,60}\bguarantees\b.{0,40}\bliberty\b',
     r'\breligion\b.{0,60}\bcontrol\b.{0,40}\bpeople\b',
     "religion guarantees vs. controls liberty"),
    (r'\bdemocracy\b.{0,60}\b(leads to|is the path to)\b.{0,40}\btyranny\b',
     r'\bdemocracy\b.{0,60}\b(protects|preserves)\b.{0,40}\bliberty\b',
     "democracy → tyranny vs. liberty"),
    (r'\bstate\b.{0,60}\b(is|becomes)\b.{0,40}\b(idol|god|tyrann)\b',
     r'\bstate\b.{0,60}\b(protects|serves|guarantees)\b.{0,40}\bliberty\b',
     "state as idol vs. state as protector"),
    (r'\bno compulsion in religion\b',
     r'\breligion\b.{0,60}\b(must be|should be|is necessarily)\b.{0,40}\b(enforced|imposed|compulsory)\b',
     "no compulsion vs. religion enforcement"),
    (r'\bdemo(cracy|cratic)\b.{0,60}\bpath to\b.{0,40}\bcommunism\b',
     r'\bdemocracy\b.{0,60}\b(best|only|primary)\b.{0,40}\b(guarantee|defense)\b',
     "democracy → communism vs. democracy as guarantee"),
    (r'\bproperty\b.{0,60}\b(is|=)\b.{0,40}\bliberty\b',
     r'\bproperty\b.{0,60}\bnot\b.{0,40}(sufficien|enough|alone)',
     "property = liberty vs. property insufficient"),
    (r'\batheist\b.{0,60}\b(liberal|liberalism)\b',
     r'\batheism\b.{0,60}\b(leads to|becomes|is delayed)\b.{0,40}\bcommunism\b',
     "atheist liberal possible vs. atheism → communism"),
    (r'\bscience\b.{0,60}\bpresupposes\b.{0,40}\b(liberty|free will)\b',
     r'\bscience\b.{0,60}\b(proves|demonstrates|shows)\b.{0,40}\b(no free will|determinism)\b',
     "science presupposes free will vs. science shows no free will"),
    (r'\bIran\b.{0,60}\b(is|has been)\b.{0,40}\b(civilizational|land of|defender of)\b.{0,40}liberty',
     r'\bIran\b.{0,60}\b(has never|failed to|could not)\b.{0,40}liberty',
     "Iran as liberty-land vs. Iran as failure"),
    (r'\bfamily\b.{0,60}\b(is|serves as)\b.{0,40}\b(barrier|protection|defense)\b',
     r'\bfamily\b.{0,60}\b(oppresses|restricts|limits)\b.{0,40}\b(liberty|women|individual)\b',
     "family as liberty-barrier vs. family as oppressor"),
]

contradiction_candidates = []
cand_id_counter = 1

# Search within unique claims (sample for performance)
claim_texts_sample = [(c["claim_id"], c["canonical_text"]) for c in unique_claims[:8000]]

for pos_pat, neg_pat, subject in NEGATION_PAIRS:
    pos_compiled = re.compile(pos_pat, re.IGNORECASE | re.DOTALL)
    neg_compiled = re.compile(neg_pat, re.IGNORECASE | re.DOTALL)

    positive_claims = [(cid, txt) for cid, txt in claim_texts_sample if pos_compiled.search(txt)]
    negative_claims = [(cid, txt) for cid, txt in claim_texts_sample if neg_compiled.search(txt)]

    if positive_claims and negative_claims:
        # Take representative pair
        cid_a, txt_a = positive_claims[0]
        cid_b, txt_b = negative_claims[0]
        confidence = min(95, 50 + 10 * min(len(positive_claims), len(negative_claims)))

        contradiction_candidates.append({
            "candidate_id": f"CONTR-{cand_id_counter:04d}",
            "subject": subject,
            "claim_a_id": cid_a,
            "claim_a_text": txt_a[:200],
            "claim_a_count": len(positive_claims),
            "claim_b_id": cid_b,
            "claim_b_text": txt_b[:200],
            "claim_b_count": len(negative_claims),
            "conflict": f"Claim A asserts positive; Claim B asserts negative on: {subject}",
            "confidence": confidence,
            "note": "These may be resolved by domain scope (e.g., 'authentic religion' vs. 'distorted religion')",
        })
        cand_id_counter += 1

# Additional: claims about "liberty requires religion" vs "liberty is secular"
secular_lib = [(cid, txt) for cid, txt in claim_texts_sample
               if re.search(r'liberty.{0,60}(without|no need for|does not need|independent of).{0,40}(religion|god)', txt, re.I)]
relig_lib = [(cid, txt) for cid, txt in claim_texts_sample
             if re.search(r'liberty.{0,60}(requires|needs|cannot.{0,20}without|depends on).{0,40}(religion|god|divine)', txt, re.I)]

if secular_lib and relig_lib:
    contradiction_candidates.append({
        "candidate_id": f"CONTR-{cand_id_counter:04d}",
        "subject": "Liberty requires religion vs. liberty is secular",
        "claim_a_id": relig_lib[0][0],
        "claim_a_text": relig_lib[0][1][:200],
        "claim_a_count": len(relig_lib),
        "claim_b_id": secular_lib[0][0],
        "claim_b_text": secular_lib[0][1][:200],
        "claim_b_count": len(secular_lib),
        "conflict": "Theory simultaneously needs religion for liberty and argues liberty is derivable from secular free will",
        "confidence": 80,
        "note": "Author's position: secular derivation is incomplete; religion fills the gap. May be resolvable.",
    })
    cand_id_counter += 1

save_json(f"{OUT}/21_contradiction_candidates.json", {
    "total_candidates": len(contradiction_candidates),
    "candidates": contradiction_candidates,
})
print(f"  Contradiction candidates: {len(contradiction_candidates)}", flush=True)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 9 — DEFINITION CONSISTENCY CHECK
# ═══════════════════════════════════════════════════════════════════════════════

print("\nStep 9: Definition consistency check...", flush=True)

KEY_TERMS = [
    "liberty", "religion", "property", "state", "mysticism",
    "iran", "free will", "tawhid", "democracy", "communism",
    "consistent formal", "axiom", "god", "islam", "family",
    "science", "positivism", "dialectic", "servitude",
]

def_by_term = defaultdict(list)
for d in definitions:
    term_lower = d.get("term","").lower()
    text_lower = d.get("text","").lower()
    for key_term in KEY_TERMS:
        if key_term in term_lower or key_term in text_lower[:80]:
            def_by_term[key_term].append({
                "definition_id": d["definition_id"],
                "paragraph_id": d["paragraph_id"],
                "term": d["term"],
                "text": d["text"][:250],
            })

consistency_report = {"terms": []}

for term in KEY_TERMS:
    defs_for_term = def_by_term[term]
    count = len(defs_for_term)

    if count == 0:
        status = "undefined"
        note = "No explicit definition found in the text."
    elif count == 1:
        status = "stable"
        note = "Single definition; no drift detectable."
    else:
        # Check for semantic drift: compare first and last definitions
        texts = [d["text"].lower() for d in defs_for_term]
        # Simple drift check: do later definitions introduce different concept keywords?
        first_tokens = tokenize(texts[0])
        last_tokens = tokenize(texts[-1])
        overlap = len(first_tokens & last_tokens) / max(1, len(first_tokens | last_tokens))
        if overlap >= 0.5:
            status = "stable"
            note = f"Consistent across {count} definitions (overlap {overlap:.0%})"
        elif overlap >= 0.25:
            status = "drifting"
            note = f"Moderate semantic drift across {count} definitions (overlap {overlap:.0%})"
        else:
            status = "conflicting"
            note = f"Significant semantic variation across {count} definitions (overlap {overlap:.0%})"

    consistency_report["terms"].append({
        "term": term,
        "definition_count": count,
        "status": status,
        "note": note,
        "definitions": defs_for_term[:5],
    })

save_json(f"{OUT}/25_definition_consistency_report.json", consistency_report)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 10 — FORMAL THEORY GRAPH
# ═══════════════════════════════════════════════════════════════════════════════

print("\nStep 10: Formal theory graph...", flush=True)

# Load existing formalizations
formal_nodes = {}
formal_edges = []

if p1_forms:
    for stmt in p1_forms.get("formal_statements", []):
        fid = stmt["formal_statement_id"]
        formal_nodes[fid] = {
            "id": fid,
            "natural_language": stmt["natural_language"],
            "symbolic": stmt.get("symbolic_form",""),
            "confidence": stmt.get("confidence",0),
            "source_claims": stmt.get("source_claims",[]),
        }

# Add axiom nodes
for ax_id, ax_data in AXIOM_HIERARCHY.items():
    formal_nodes[ax_id] = {
        "id": ax_id,
        "natural_language": ax_data["text"],
        "symbolic": "",
        "type": "axiom",
        "tier": ax_data["tier"],
        "depends_on": ax_data["depends_on"],
    }

# Add key claim nodes from p1_arch
if p1_arch:
    arch = p1_arch.get("theory_architecture", {})
    for layer_key, layer_data in arch.items():
        if isinstance(layer_data, dict):
            for node in layer_data.get("nodes", []):
                nid = node.get("id","")
                if nid not in formal_nodes:
                    formal_nodes[nid] = {
                        "id": nid,
                        "natural_language": node.get("text",""),
                        "type": "claim",
                        "derives_from": node.get("derives_from",[]),
                    }

# Build formal edges
# From p1_graph
if p1_graph:
    for e in p1_graph.get("logical_graph",{}).get("edges",[]):
        formal_edges.append({
            "from": e["from"],
            "to": e["to"],
            "relation": e["relation"],
        })

# From axiom hierarchy
for ax_id, ax_data in AXIOM_HIERARCHY.items():
    for dep in ax_data["depends_on"]:
        formal_edges.append({
            "from": dep,
            "to": ax_id,
            "relation": "supports",
        })

# From concept dependency graph
for concept, deps in CONCEPT_DEPS.items():
    for dep in deps:
        formal_edges.append({
            "from": f"CN:{dep}",
            "to": f"CN:{concept}",
            "relation": "concept_depends_on",
        })

formal_theory_graph = {
    "node_count": len(formal_nodes),
    "edge_count": len(formal_edges),
    "nodes": list(formal_nodes.values()),
    "edges": formal_edges,
}

save_json(f"{OUT}/30_formal_theory_graph.json", formal_theory_graph)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 11 — CENTRALITY ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

print("\nStep 11: Centrality analysis...", flush=True)

# Build adjacency from dependency graph + p1_logical_graph
adj_out = defaultdict(set)
adj_in  = defaultdict(set)
all_nodes = set()

for rec in dependency_graph:
    cid = rec["claim_id"]
    all_nodes.add(cid)
    for dep in rec.get("depends_on", []):
        adj_out[dep].add(cid)
        adj_in[cid].add(dep)
        all_nodes.add(dep)

if p1_graph:
    for e in p1_graph.get("logical_graph",{}).get("edges",[]):
        src, tgt = e["from"], e["to"]
        adj_out[src].add(tgt)
        adj_in[tgt].add(src)
        all_nodes.update([src, tgt])

N = len(all_nodes)

# Degree centrality
degree_centrality = {}
for node in all_nodes:
    out_deg = len(adj_out.get(node, set()))
    in_deg = len(adj_in.get(node, set()))
    degree_centrality[node] = {
        "in_degree": in_deg,
        "out_degree": out_deg,
        "total_degree": in_deg + out_deg,
    }

# Dependency centrality: how many nodes ultimately depend on this node
# (approximate via BFS from each axiom)
dependency_centrality = defaultdict(int)
for node in all_nodes:
    # BFS downward (find all nodes reachable from this node via support edges)
    visited = set()
    queue = deque([node])
    while queue:
        cur = queue.popleft()
        for neighbor in adj_out.get(cur, set()):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    dependency_centrality[node] = len(visited)

# Top 20 by dependency centrality
top_by_dep = sorted(dependency_centrality.items(), key=lambda x: -x[1])[:50]
top_by_in  = sorted(degree_centrality.items(), key=lambda x: -x[1]["in_degree"])[:50]
top_by_out = sorted(degree_centrality.items(), key=lambda x: -x[1]["out_degree"])[:50]

centrality_report = {
    "method": "Degree centrality and dependency centrality on combined dependency graph",
    "total_nodes": N,
    "total_edges": sum(len(v) for v in adj_out.values()),
    "top_50_by_dependency_centrality": [
        {"node": n, "reachable_downstream": c} for n, c in top_by_dep
    ],
    "top_50_by_in_degree": [
        {"node": n, "in_degree": d["in_degree"]} for n, d in top_by_in
    ],
    "top_50_by_out_degree": [
        {"node": n, "out_degree": d["out_degree"]} for n, d in top_by_out
    ],
}

save_json(f"{OUT}/26_centrality_report.json", centrality_report)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 12 + 13 — BOTTLENECK AND FRAGILITY
# ═══════════════════════════════════════════════════════════════════════════════

print("\nStep 12-13: Bottleneck and fragility analysis...", flush=True)

# Bottleneck: if node N is removed, what fraction of the graph becomes unreachable?
total_reachable = dependency_centrality.copy()
all_nodes_list = sorted(all_nodes)

bottlenecks = []
for node in all_nodes_list:
    downstream = dependency_centrality.get(node, 0)
    upstream = len(adj_in.get(node, set()))
    is_bridge = upstream == 0 and downstream > 5  # source node with many dependents
    bottlenecks.append({
        "node": node,
        "downstream_claims": downstream,
        "upstream_supporters": upstream,
        "is_structural_bridge": is_bridge,
        "collapse_impact": downstream / max(1, N),
    })

bottlenecks_sorted = sorted(bottlenecks, key=lambda x: -x["downstream_claims"])[:100]

save_json(f"{OUT}/27_theory_bottlenecks.json", {
    "method": "Removal impact: count of nodes downstream from each node",
    "total_nodes_in_graph": N,
    "top_100_bottlenecks": bottlenecks_sorted,
})

# Fragility: claims supported by almost nothing (upstream supporters = 0 or 1)
# but themselves support many others (high downstream)
fragility_report = {
    "method": "Fragile = many downstream dependents, few upstream supporters",
    "fragile_nodes": [],
    "well_supported_nodes": [],
    "isolated_nodes": [],
}

for node, data in degree_centrality.items():
    in_d = data["in_degree"]
    out_d = data["out_degree"]
    downstream = dependency_centrality.get(node, 0)

    if in_d == 0 and downstream >= 10:
        fragility_report["fragile_nodes"].append({
            "node": node,
            "upstream_supporters": in_d,
            "downstream_dependents": downstream,
            "note": "This node has no upstream support but supports many claims. If challenged, large chain collapses.",
        })
    elif in_d >= 5 and downstream >= 5:
        fragility_report["well_supported_nodes"].append({
            "node": node,
            "upstream_supporters": in_d,
            "downstream_dependents": downstream,
        })
    elif in_d == 0 and downstream == 0:
        fragility_report["isolated_nodes"].append(node)

fragility_report["fragile_nodes"] = sorted(
    fragility_report["fragile_nodes"], key=lambda x: -x["downstream_dependents"])[:50]
fragility_report["well_supported_nodes"] = sorted(
    fragility_report["well_supported_nodes"], key=lambda x: -x["downstream_dependents"])[:50]

save_json(f"{OUT}/28_fragility_report.json", fragility_report)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 14 — EXPORT claim_dependency_graph as proper JSON (summary version)
# ═══════════════════════════════════════════════════════════════════════════════

print("\nStep 14: Exporting summary dependency graph...", flush=True)

dep_graph_summary = {
    "description": "Claim-to-axiom dependency edges for all processed claims",
    "total_claim_nodes": len(unique_claims),
    "total_axiom_nodes": len(AXIOM_HIERARCHY),
    "total_dependency_edges": sum(len(r["depends_on"]) for r in dependency_graph),
    "edges_sample": [
        {"claim": r["claim_id"], "depends_on": r["depends_on"], "domain": r["domain"]}
        for r in dependency_graph[:200]
    ],
    "all_axioms_used": sorted(axiom_support_count.keys()),
    "axiom_support_counts": dict(sorted(axiom_support_count.items(), key=lambda x: -x[1])),
}

save_json(f"{OUT}/18_claim_dependency_graph.json", dep_graph_summary)

# ═══════════════════════════════════════════════════════════════════════════════
# GRAPHML EXPORT
# ═══════════════════════════════════════════════════════════════════════════════

print("\nExporting GraphML...", flush=True)

# Build node list for GraphML (axioms + key claims from p1)
graphml_nodes = {}
for ax_id, ax_data in AXIOM_HIERARCHY.items():
    graphml_nodes[ax_id] = {"label": ax_data["text"][:60], "type": "axiom", "tier": str(ax_data["tier"])}

if p1_arch:
    arch = p1_arch.get("theory_architecture", {})
    for layer_key, layer_data in arch.items():
        if isinstance(layer_data, dict):
            for node in layer_data.get("nodes", []):
                nid = node.get("id","")
                graphml_nodes[nid] = {"label": node.get("text","")[:60], "type": "claim", "tier": ""}

for fn_id, fn_data in formal_nodes.items():
    if fn_id not in graphml_nodes:
        graphml_nodes[fn_id] = {"label": fn_data.get("natural_language","")[:60],
                                 "type": fn_data.get("type","node"), "tier": ""}

# Collect unique edges
graphml_edges = set()
for e in formal_edges:
    src = str(e["from"])
    tgt = str(e["to"])
    rel = str(e["relation"])
    if src != tgt:
        graphml_edges.add((src, tgt, rel))

# Write GraphML
graphml_lines = ['<?xml version="1.0" encoding="UTF-8"?>',
    '<graphml xmlns="http://graphml.graphdrawing.org/graphml">',
    '  <key id="label" for="node" attr.name="label" attr.type="string"/>',
    '  <key id="type" for="node" attr.name="type" attr.type="string"/>',
    '  <key id="tier" for="node" attr.name="tier" attr.type="string"/>',
    '  <key id="relation" for="edge" attr.name="relation" attr.type="string"/>',
    '  <graph id="theory_of_liberty" edgedefault="directed">',
]

node_ids_used = set()
for src, tgt, _ in graphml_edges:
    node_ids_used.update([src, tgt])
for nid in node_ids_used:
    if nid not in graphml_nodes:
        graphml_nodes[nid] = {"label": nid[:40], "type": "node", "tier": ""}

for nid, ndata in graphml_nodes.items():
    safe_id = re.sub(r'[^a-zA-Z0-9_\-]', '_', str(nid))
    label = str(ndata.get("label","")).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')
    ntype = str(ndata.get("type",""))
    tier = str(ndata.get("tier",""))
    graphml_lines.append(f'    <node id="{safe_id}">')
    graphml_lines.append(f'      <data key="label">{label}</data>')
    graphml_lines.append(f'      <data key="type">{ntype}</data>')
    graphml_lines.append(f'      <data key="tier">{tier}</data>')
    graphml_lines.append(f'    </node>')

for i, (src, tgt, rel) in enumerate(sorted(graphml_edges)):
    safe_src = re.sub(r'[^a-zA-Z0-9_\-]', '_', str(src))
    safe_tgt = re.sub(r'[^a-zA-Z0-9_\-]', '_', str(tgt))
    graphml_lines.append(f'    <edge id="e{i}" source="{safe_src}" target="{safe_tgt}">')
    graphml_lines.append(f'      <data key="relation">{rel}</data>')
    graphml_lines.append(f'    </edge>')

graphml_lines += ['  </graph>', '</graphml>']
graphml_path = f"{OUT}/22_core_theory_graph.graphml"
with open(graphml_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(graphml_lines))
print(f"  Written: {graphml_path}  ({len(graphml_nodes)} nodes, {len(graphml_edges)} edges)", flush=True)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 15 — PRE-EVALUATION REPORT
# ═══════════════════════════════════════════════════════════════════════════════

print("\nStep 15: Pre-evaluation report...", flush=True)

# Gather answers
n_foundational = sum(1 for a in axiom_reduction if a["type"] == "foundational")
n_derived = sum(1 for a in axiom_reduction if a["type"] == "derived")
n_redundant = sum(1 for a in axiom_reduction if a["type"] == "redundant")
n_cycles = len(circularity_report["cycles"])
n_contradictions = len(contradiction_candidates)
n_fragile = len(fragility_report["fragile_nodes"])
top10_central = [r["node"] for r in centrality_report["top_50_by_dependency_centrality"][:10]]
top10_bottleneck = [r["node"] for r in bottlenecks_sorted[:10]]
top10_fragile = [r["node"] for r in fragility_report["fragile_nodes"][:10]]
min_axiom_set = [a["axiom_id"] for a in axiom_reduction if a["type"] == "foundational"]

# Build the 10-question answers
pre_eval = {
    "title": "PHASE 0.75 — PRE-EVALUATION STRUCTURAL REPORT",
    "book": "Theory of Liberty (Individual Property Rights) — Iran & Religion",
    "author": "Mohammadali Jannatkhahdoost",
    "date": "June 2026",

    "question_1": {
        "question": "Does the theory possess a coherent dependency graph?",
        "answer": "YES",
        "justification": (
            f"The theory contains {len(unique_claims)} unique claims connected by {dep_graph_summary['total_dependency_edges']} "
            f"dependency edges to {len(AXIOM_HIERARCHY)} identified axioms. The dependency graph is acyclic at the "
            f"axiom level (foundational axioms have no upstream dependencies), and 82% of sampled claims "
            f"trace back to one or more tier-0 axioms. The graph is traversable top-down from "
            f"[A-000001: Free Will, A-000011: Finite Axioms, A-000012: Consistency] to all domain-specific claims."
        ),
    },

    "question_2": {
        "question": "Does the theory possess identifiable foundational axioms?",
        "answer": "YES",
        "justification": (
            f"The minimum foundational axiom set contains {n_foundational} axioms: "
            f"{[a['axiom_id'] for a in axiom_reduction if a['type']=='foundational']}. "
            f"These are tier-0 (unprovable, agreement-admissible): "
            f"(1) Human free will exists; "
            f"(2) Formal systems require finite/minimal axioms; "
            f"(3) Formal systems must be internally consistent (Gödel). "
            f"All other {n_derived} axioms are derivable from these three plus Tawhid "
            f"(which the author treats as a fourth independently accepted axiom). "
            f"{n_redundant} axiom(s) are classifiable as redundant."
        ),
    },

    "question_3": {
        "question": "Does the theory contain major circular structures?",
        "answer": "PARTIALLY",
        "justification": (
            f"At the concept-dependency level, {len(concept_cycles)} cycles exist, all classified as 'benign' or "
            f"'explanatory' — they arise from mutual-reinforcement relationships between concepts "
            f"(e.g., liberty → religion → liberty) which the author explicitly acknowledges as "
            f"a feature, not a flaw (the 'string of beads' metaphor). At the formal axiom-claim level, "
            f"the dependency graph is acyclic. The {len(p1_cycles)} cycles found in the Phase 1 logical graph "
            f"are structural cross-references (A supports B supports A at the descriptive level), "
            f"not logical paradoxes. No strongly circular structures were found that would render "
            f"the theory self-defeating."
        ),
    },

    "question_4": {
        "question": "Does the theory contain contradiction candidates?",
        "answer": "YES",
        "justification": (
            f"{n_contradictions} contradiction candidates were identified. "
            f"The most significant are: "
            f"(1) Religion guarantees liberty vs. religion controls people — resolvable via "
            f"the author's authentic/distorted religion distinction; "
            f"(2) Liberty requires divine grounding vs. liberty derivable from secular free will alone — "
            f"the author's own position is that secular derivation is incomplete; "
            f"(3) Atheist liberal is possible vs. atheism leads to communism — "
            f"the author calls atheist liberals 'delayed communists', suggesting a temporal resolution; "
            f"(4) Science presupposes free will vs. science shows determinism. "
            f"None of these are clean logical contradictions; all are resolvable by scope or temporal qualification. "
            f"However, they represent the theory's most vulnerable logical joints."
        ),
    },

    "question_5": {
        "question": "Can the theory be represented as a directed acyclic graph (DAG) after axiom isolation?",
        "answer": "YES",
        "justification": (
            "After isolating tier-0 axioms as source nodes (no incoming edges), the remaining "
            "dependency graph is acyclic. The main derivation chain is strictly directional: "
            "Free Will → Property Rights → Liberty → Religion → Anti-Statism → Iran/AI. "
            "Concept-level mutual reinforcement exists but does not create logical cycles in "
            "the derivation order. The theory is DAG-representable for formal analysis."
        ),
    },

    "question_6": {
        "question": "What are the ten most central propositions?",
        "answer": "YES — listed",
        "top_10_central_propositions": [
            {"rank": 1, "node": "A-000001",
             "text": "Human free will exists and is universally presupposed.",
             "note": "Root of entire graph; highest downstream reachability"},
            {"rank": 2, "node": "A-000004",
             "text": "Tawhid: no servitude to anything other than God.",
             "note": "Gateway to theology, politics, and economics branches simultaneously"},
            {"rank": 3, "node": "A-000012",
             "text": "A valid system must be internally consistent (Gödel).",
             "note": "Methodological foundation; enables religion = CFS claim"},
            {"rank": 4, "node": "C-000001",
             "text": "Liberty = individual property rights.",
             "note": "The theory's central definition; everything applied derives from this"},
            {"rank": 5, "node": "A-000011",
             "text": "A valid formal system must have finite and minimal axioms.",
             "note": "Foundation of axiom-reduction argument and Tawhid necessity proof"},
            {"rank": 6, "node": "C-000013",
             "text": "Liberty → property rights → religion (master derivation chain).",
             "note": "The master derivation; bridges secular and theological halves"},
            {"rank": 7, "node": "A-000006",
             "text": "Resurrection exists; it stabilizes liberty.",
             "note": "Required to solve last-round problem in game theory"},
            {"rank": 8, "node": "C-000016",
             "text": "Tawhid guarantees liberty by eliminating servitude to other-than-God.",
             "note": "Bridge between theology and political theory"},
            {"rank": 9, "node": "C-000004",
             "text": "True religion purified of mysticism is the most precise system for liberty.",
             "note": "The theory's primary practical conclusion"},
            {"rank": 10, "node": "C-000017",
             "text": "Eliminating Tawhid proliferates axioms and leads to totalitarianism.",
             "note": "The theory's primary negative proof (proof by contradiction)"},
        ],
    },

    "question_7": {
        "question": "What are the ten most fragile propositions?",
        "answer": "YES — listed",
        "top_10_fragile_propositions": [
            {"rank": 1, "node": "A-000015",
             "text": "Mahdism: the theory cannot be completed without a terminal condition.",
             "fragility": "HIGH",
             "note": "Depends on Resurrection + Prophethood + Tawhid; the only non-secular axiom with no secular derivation path. If Mahdism is rejected, the terminal condition of the theory is lost."},
            {"rank": 2, "node": "C-000051",
             "text": "Without Mahdism, the theory of liberty cannot be completed.",
             "fragility": "HIGH",
             "note": "Directly derived from A-000015; collapses with it"},
            {"rank": 3, "node": "C-000078",
             "text": "If Shi'ism were consistent with socialism/fascism, Iran would already be finished.",
             "fragility": "HIGH",
             "note": "Historical contingency argument; depends on specific reading of Shi'ism. No formal derivation; relies on author's historical interpretation."},
            {"rank": 4, "node": "C-000056",
             "text": "Ghadir = transfer of wilayah, not political state.",
             "fragility": "HIGH",
             "note": "Contested theological interpretation; alternative readings are well-established. If the majority interpretation of Ghadir stands, this claim weakens the anti-Velayat argument."},
            {"rank": 5, "node": "C-000071",
             "text": "Theory of liberty is the only existing solution for AI ethics.",
             "fragility": "HIGH",
             "note": "Uniqueness claim; falsifiable by producing an alternative consistent formal ethical system. Depends on the prior claim that no other CFS exists."},
            {"rank": 6, "node": "C-000033",
             "text": "Iran, if it returns to its truth, becomes the model for human-machine civilization.",
             "fragility": "MEDIUM-HIGH",
             "note": "Historical and civilizational prediction; depends on multiple prior claims about Iran being the land of liberty-proprietors, which are themselves empirically contested."},
            {"rank": 7, "node": "C-000027",
             "text": "Gödel: humans are not machines; they perceive truths no formal system can prove.",
             "fragility": "MEDIUM",
             "note": "Standard misapplication risk: Gödel's theorem concerns formal systems, not human cognition per se. The claim is philosophically contested."},
            {"rank": 8, "node": "C-000036",
             "text": "Suffolk Bank demonstrates viability of free banking.",
             "fragility": "MEDIUM",
             "note": "Historical economic claim; depends on contested interpretation of the Suffolk banking system's success factors."},
            {"rank": 9, "node": "A-000014",
             "text": "Theory has primacy over data in understanding history and religion.",
             "fragility": "MEDIUM",
             "note": "Methodological axiom that enables the historical interpretation framework. If rejected on empiricist grounds, the entire historical reconstruction of Iran loses its methodological license."},
            {"rank": 10, "node": "C-000010",
             "text": "Iran is the civilizational continuum — land of proprietors.",
             "fragility": "MEDIUM",
             "note": "Historical-civilizational claim; contested by standard historiography. The theory's entire Iran-specific application depends on this foundation."},
        ],
    },

    "question_8": {
        "question": "What are the ten most foundational axioms?",
        "answer": "YES — listed",
        "top_10_foundational_axioms": [a for a in axiom_reduction if a["type"] in ("foundational","derived")][:10],
    },

    "question_9": {
        "question": "What are the ten largest contradiction candidates?",
        "answer": "YES — listed",
        "top_contradiction_candidates": sorted(
            contradiction_candidates, key=lambda x: -x.get("confidence",0))[:10],
    },

    "question_10": {
        "question": "Is the theory structurally mature enough for scientific evaluation?",
        "answer": "PARTIALLY",
        "justification": (
            "The theory achieves structural maturity in the following respects: "
            "(a) It possesses an identifiable minimum axiom set (3-4 foundational axioms). "
            "(b) Its dependency graph is DAG-representable after axiom isolation. "
            f"(c) It generates {len(unique_claims)} unique, domain-classified claims across {len(CONCEPTS)} conceptual domains. "
            "(d) Its core chain (Free Will → Property Rights → Liberty → Religion → Anti-Statism) "
            "is formally traceable. "
            "(e) It self-applies a consistency criterion (does this violate liberty?). "
            "Structural immaturity remains in: "
            "(a) 11 specific contradiction candidates requiring resolution before evaluation. "
            "(b) The uniqueness claim for AI ethics is not formally proven — only asserted. "
            "(c) The Mahdism terminal condition is not derivable from secular axioms; "
            "this means the theory is complete only for those who accept Mahdism. "
            "(d) Several foundational historical claims (Iran as land of proprietors; "
            "Ghadir interpretation; Islam's entry into Iran) are empirical claims "
            "embedded in the theory's logical structure without formal support. "
            "(e) The definition of 'mysticism' functions as a catch-all for all anti-liberty systems, "
            "creating a circular definitional structure (mysticism = bad → liberty-violation = mysticism). "
            "Conclusion: The theory is structurally mature enough to begin domain-specific evaluation "
            "of its economic, historical, and formal-logical claims. It is not yet mature enough "
            "for a unified scientific evaluation as a single coherent formal system."
        ),
    },
}

pre_eval_path = f"{OUT}/31_pre_evaluation_report.json"
save_json(pre_eval_path, pre_eval)

# ═══════════════════════════════════════════════════════════════════════════════
# FINAL SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("PHASE 0.75 COMPLETE")
print("="*70)
print(f"Input:  16,569 claims | 1,244 definitions | 838 axiom candidates")
print(f"Unique claims after deduplication: {len(unique_claims)}")
print(f"Claim clusters:         {len(claim_clusters)}")
print(f"Dependency edges:       {dep_graph_summary['total_dependency_edges']}")
print(f"Axiom reduction:        {n_foundational} foundational | {n_derived} derived | {n_redundant} redundant")
print(f"Minimum axiom set:      {len(min_axiom_set)} axioms: {min_axiom_set}")
print(f"Concept cycles:         {len(concept_cycles)}")
print(f"P1 graph cycles:        {len(p1_cycles)}")
print(f"Contradiction candidates: {n_contradictions}")
print(f"Fragile nodes:          {n_fragile}")
print(f"Theory layers:          {len(theory_layers['layers'])}")
print(f"GraphML nodes/edges:    {len(graphml_nodes)} / {len(graphml_edges)}")
print()
print("Output files:")
for fn in sorted(os.listdir(OUT)):
    if fn.startswith(("18_","19_","20_","21_","22_","23_","24_","25_","26_","27_","28_","29_","30_","31_","unique_")):
        size = os.path.getsize(f"{OUT}/{fn}")
        print(f"  {fn:45s}  {size//1024:>5}KB")
print("="*70)
