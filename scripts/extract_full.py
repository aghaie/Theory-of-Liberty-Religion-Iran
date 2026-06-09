#!/usr/bin/env python3
"""
Full per-paragraph extraction for Theory of Liberty — Iran & Religion
Produces: paragraph_extractions.jsonl, claims_complete.jsonl,
          definitions_complete.jsonl, axiom_candidates_complete.jsonl
"""

import json
import re
import sys

# ── Vocabulary / patterns ────────────────────────────────────────────────────

# Claim-indicator phrases (sentence openers that mark normative/theoretical claims)
CLAIM_INDICATORS = [
    r'\bI claim\b', r'\bI argue\b', r'\bI contend\b', r'\bI demonstrate\b',
    r'\bI prove\b', r'\bI show\b', r'\bI maintain\b', r'\bI assert\b',
    r'\btherefore\b', r'\bconsequently\b', r'\bit follows\b', r'\bthus\b',
    r'\bhence\b', r'\bin conclusion\b', r'\bwe conclude\b', r'\bthe conclusion\b',
    r'\bis necessarily\b', r'\bmust be\b', r'\bcannot be\b', r'\bis equivalent to\b',
    r'\bif and only if\b', r'\bimplies\b', r'\bdemonstrates\b', r'\bestablishes\b',
    r'\bproves\b', r'\bshows that\b', r'\bit is clear\b', r'\bit is evident\b',
    r'\bwithout .* there is no\b', r'\bany .* is\b', r'\beverywhere .* is\b',
    r'\bwhoever .* is\b', r'\bwhenever .* is\b', r'\bthe result is\b',
    r'\bthe only .* is\b', r'\bnever .* is\b', r'\bwill inevitably\b',
    r'\bthe terminal point\b', r'\bthe telos\b', r'\bis the antithesis\b',
    r'\bLib?erty .* is\b', r'\bproperty .* is\b', r'\breligion .* is\b',
    r'\bmysticism .* is\b', r'\bthe state .* is\b', r'\btawhid .* is\b',
    r'\bis a consistent\b', r'\bis the only\b', r'\bis the root\b',
]
CLAIM_PATTERN = re.compile('|'.join(CLAIM_INDICATORS), re.IGNORECASE)

AXIOM_INDICATORS = [
    r'\baxiom\b', r'\bfoundation\b', r'\bfundamental principle\b',
    r'\bstarting point\b', r'\bunprovable\b', r'\bagreement-admissible\b',
    r'\bself-evident\b', r'\bpresupposed\b', r'\btaken as given\b',
    r'\bwithout proof\b', r'\bwe accept without\b', r'\bthe premise\b',
    r'\bprior to all\b', r'\bprior normative\b', r'\bnecessary condition\b',
    r'\bsufficient condition\b', r'\bconsistent formal axiomatic\b',
    r'\bformal axiomatic system\b', r'\bGödel\b', r'\bincompleteness\b',
    r'\baxiomatic\b', r'\bpostulate\b', r'\bfirst principle\b',
]
AXIOM_PATTERN = re.compile('|'.join(AXIOM_INDICATORS), re.IGNORECASE)

DEFINITION_INDICATORS = [
    r'\bis defined as\b', r'\bby .* I mean\b', r'\bmeans\b', r'\brefers to\b',
    r'\bdenotes\b', r'\bsignifies\b', r'\bthe definition of\b', r'\bI define\b',
    r'\bin other words\b', r'\bthat is\b', r'\bi\.e\.\b', r'\bi mean\b',
    r'\bI call\b', r'\bI use the term\b', r'\bwhat I mean by\b',
    r'\bthe concept of\b', r'\bby .* we mean\b', r'\bis nothing other than\b',
    r'\bis essentially\b', r'\bis precisely\b', r'\bis simply\b',
    r'\bis in fact\b', r'\bimagine\b', r'\bsuppose\b',
]
DEFINITION_PATTERN = re.compile('|'.join(DEFINITION_INDICATORS), re.IGNORECASE)

# Reference: known names in the book
KNOWN_REFERENCES = [
    'Mises', 'Hayek', 'Rothbard', 'Hobbes', 'Locke', 'Kant', 'Hegel',
    'Marx', 'Plato', 'Aristotle', 'Gödel', 'Turing', 'Peikoff', 'Rand',
    'Shariati', 'Khomeini', 'Ibn Arabi', 'Mulla Sadra', 'Suhrawardi',
    'Ferdowsi', 'Rumi', 'Plotinus', 'Augustine', 'Heraclitus', 'Fardid',
    'Harari', 'Dawkins', 'Hitchens', 'Harris', 'Dennett', 'Hirsi Ali',
    'Newton', 'Einstein', 'Spinoza', 'Hume', 'Rousseau', 'Voltaire',
    'Aquinas', 'al-Ghazali', 'al-Farabi', 'Avicenna', 'Averroes',
    'Jannatkhahdoost', 'Jannatkhah', 'Bahram Gur', 'Cyrus', 'Darius',
    'Muhammad', 'Prophet', 'Imam Ali', 'Imam Sadiq', 'Imam Baqir',
    'Imam Kazim', 'Imam Hussain', 'Imam Khomeini', 'Ahl al-Bayt',
    'Mahdism', 'Mahdi', 'Imam of the Age', 'Zionism', 'Zionists',
    'Ghadir', 'Karbala', 'Mecca', 'Medina', 'Qur', 'Quran',
    'Torah', 'Gospel', 'Bible', 'Islamic Republic', 'Pahlavi',
    'Austrian School', 'Suffolk Bank', 'Keynes', 'Keynesian',
    'Bitcoin', 'Friedman', 'Schumpeter', 'Weber',
    'Foucault', 'Nietzsche', 'Schopenhauer', 'Stirner',
    'Lenin', 'Stalin', 'Hitler', 'Mussolini', 'Mao',
    'Adam Smith', 'Ricardo', 'Bastiat', 'Tocqueville',
    'Manichaeism', 'Manichaean', 'Zoroaster', 'Zurvanism',
    'North Korea', 'Soviet Union', 'China', 'America', 'Iran',
    'Velayat-e Faqih', 'Wilayat', 'Tawhid', 'Taslīṭ', 'huqūq',
    'Shahnameh', 'Avesta', 'Masnavi',
]
REF_PATTERN = re.compile(r'\b(' + '|'.join(re.escape(r) for r in KNOWN_REFERENCES) + r')\b')

# Concept keywords for dependency tracking
CORE_CONCEPTS = [
    'Liberty', 'property rights', 'free will', 'Tawhid', 'mysticism',
    'religion', 'the state', 'democracy', 'communism', 'socialism',
    'Resurrection', 'Prophethood', 'Mahdism', 'Austrian School',
    'consistent formal system', 'axiomatic', 'Gödel', 'servitude',
    'collectivism', 'individualism', 'free market', 'private property',
    'family', 'education', 'taxation', 'central bank', 'money',
    'Iran', 'Islam', 'Shi\'ism', 'Velayat-e Faqih', 'Shahnameh',
    'AI', 'artificial intelligence', 'natural law', 'human rights',
    'envy', 'bureaucracy', 'positivism', 'dialectic', 'Hegelian',
    'pantheism', 'emanationism', 'wahdat al-wujud', 'game theory',
    'last-round problem', 'prisoner\'s dilemma',
]
DEP_PATTERN = re.compile(r'\b(' + '|'.join(re.escape(c) for c in CORE_CONCEPTS) + r')\b', re.IGNORECASE)

# ── Sentence splitter ────────────────────────────────────────────────────────

def split_sentences(text):
    """Split text into sentences, preserving abbreviation-dot false positives."""
    text = text.replace('\n', ' ')
    # Protect common abbreviations
    text = re.sub(r'\b(Mr|Mrs|Dr|Prof|vs|etc|e\.g|i\.e|al|vol|p|pp|ch)\.',
                  lambda m: m.group(0).replace('.', '<!DOT!>'), text)
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z"])', text)
    sentences = [s.replace('<!DOT!>', '.').strip() for s in sentences if s.strip()]
    return sentences


# ── Extraction functions ─────────────────────────────────────────────────────

claim_counter = [0]
def_counter = [0]
axiom_counter = [0]

def extract_claims(para_id, sentences):
    claims = []
    for sent in sentences:
        if len(sent) < 20:
            continue
        # Every substantive sentence IS a claim (the book is theoretical throughout)
        # Classify it: normative claim if has indicator; descriptive otherwise
        is_normative = bool(CLAIM_PATTERN.search(sent))
        is_axiom_related = bool(AXIOM_PATTERN.search(sent))
        domain = classify_domain(sent)
        claim_counter[0] += 1
        cid = f"C-{claim_counter[0]:06d}"
        claims.append({
            "claim_id": cid,
            "paragraph_id": f"P-{para_id:04d}",
            "text": sent,
            "type": "normative" if is_normative else "descriptive",
            "is_axiom_related": is_axiom_related,
            "domain": domain,
        })
    return claims


def extract_definitions(para_id, text, sentences):
    defs = []
    for sent in sentences:
        if not DEFINITION_PATTERN.search(sent):
            continue
        if len(sent) < 20:
            continue
        def_counter[0] += 1
        did = f"D-{def_counter[0]:06d}"
        # Try to extract the term being defined
        term = extract_defined_term(sent)
        defs.append({
            "definition_id": did,
            "paragraph_id": f"P-{para_id:04d}",
            "term": term,
            "text": sent,
        })
    return defs


def extract_axiom_candidates(para_id, text, sentences):
    candidates = []
    for sent in sentences:
        if not AXIOM_PATTERN.search(sent):
            continue
        if len(sent) < 20:
            continue
        axiom_counter[0] += 1
        aid = f"AX-{axiom_counter[0]:06d}"
        candidates.append({
            "axiom_id": aid,
            "paragraph_id": f"P-{para_id:04d}",
            "text": sent,
            "tier": classify_axiom_tier(sent),
        })
    return candidates


def extract_references(text):
    refs = []
    seen = set()
    for m in REF_PATTERN.finditer(text):
        name = m.group(0)
        if name not in seen:
            seen.add(name)
            refs.append(name)
    return refs


def extract_dependencies(text):
    deps = []
    seen = set()
    for m in DEP_PATTERN.finditer(text):
        concept = m.group(0).lower().strip()
        if concept not in seen:
            seen.add(concept)
            deps.append(m.group(0))
    return deps


# ── Classification helpers ───────────────────────────────────────────────────

DOMAIN_KEYWORDS = {
    "economics": ['market', 'money', 'price', 'tax', 'bank', 'currency', 'property',
                  'wealth', 'trade', 'capital', 'debt', 'inflation', 'rial', 'bitcoin',
                  'austrian', 'keynes', 'free market', 'mudarabah', 'suffolk'],
    "theology": ['god', 'religion', 'tawhid', 'resurrection', 'prophet', 'quran',
                 'islam', 'imam', 'shirk', 'servitude', 'divine', 'faith', 'hadith',
                 'shi', 'sunni', 'surah', 'verse', 'ahl al-bayt', 'mahdi', 'ghadir'],
    "political_theory": ['state', 'government', 'liberty', 'democracy', 'communism',
                         'socialism', 'fascism', 'collectivism', 'liberalism',
                         'statism', 'tyranny', 'totalitar', 'velayat'],
    "philosophy": ['axiom', 'formal system', 'gödel', 'logic', 'ontolog', 'epistemolog',
                   'kant', 'hegel', 'plato', 'aristotle', 'dialectic', 'positivism',
                   'phenomenolog', 'mysticism', 'metaphysics'],
    "history": ['iran', 'islamic republic', 'pahlavi', 'revolution', 'ottoman',
                'safavid', 'sassanid', 'roman', 'nazi', 'soviet', 'karbala',
                'shahnameh', 'ferdowsi', 'ancient', 'century', 'medieval'],
    "game_theory": ['prisoner', 'game theory', 'last-round', 'payoff', 'defect',
                    'cooperate', 'nash', 'equilibrium', 'strategy'],
    "ai_technology": ['artificial intelligence', ' ai ', 'machine learning', 'algorithm',
                      'turing', 'robot', 'automation', 'alignment'],
    "sociology": ['family', 'society', 'community', 'individual', 'education',
                  'culture', 'tradition', 'class', 'envy', 'bureaucracy'],
}

def classify_domain(text):
    text_lower = text.lower()
    scores = {}
    for domain, keywords in DOMAIN_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in text_lower)
        if score > 0:
            scores[domain] = score
    if not scores:
        return "general"
    return max(scores, key=scores.get)


def classify_axiom_tier(text):
    text_lower = text.lower()
    if any(k in text_lower for k in ['free will', 'tawhid', 'resurrection', 'prophethood',
                                      'self-evident', 'agreement-admissible', 'unprovable']):
        return "tier_1_foundational"
    elif any(k in text_lower for k in ['consistent formal', 'axiomatic system', 'finite axiom',
                                        'minimal axiom', 'gödel']):
        return "tier_2_methodological"
    else:
        return "tier_3_derived"


def extract_defined_term(sent):
    """Try to extract the term being defined from the sentence."""
    patterns = [
        r'"([^"]+)"\s+(?:is|means|refers to|denotes)',
        r"'([^']+)'\s+(?:is|means|refers to|denotes)",
        r'([A-Z][a-zA-Z\s]{2,30})\s+(?:is defined as|means|refers to|denotes)',
        r'[Bb]y\s+"([^"]+)"\s+[Ii] mean',
        r'[Bb]y\s+([A-Z][a-zA-Z\s]{2,20})\s+[Ii] mean',
        r'[Tt]he (?:concept|term|notion|idea) of\s+"?([^",]{3,40})"?',
        r'[Ww]hat I mean by\s+"?([^",]{3,40})"?',
    ]
    for pat in patterns:
        m = re.search(pat, sent)
        if m:
            return m.group(1).strip()
    # Fallback: first noun phrase
    m = re.match(r'^([A-Z][a-zA-Z\s]{2,30}(?:of\s+[A-Z][a-zA-Z\s]{2,20})?)\s', sent)
    if m:
        return m.group(1).strip()
    return sent[:40].strip()


# ── Main pipeline ────────────────────────────────────────────────────────────

def process_paragraphs(input_path, output_dir):
    print(f"Reading paragraphs from {input_path} ...", flush=True)

    all_extractions = []
    all_claims = []
    all_definitions = []
    all_axioms = []

    with open(input_path, 'r', encoding='utf-8') as fh:
        lines = fh.readlines()

    total = len(lines)
    print(f"Total paragraphs: {total}", flush=True)

    for i, line in enumerate(lines):
        if i % 200 == 0:
            print(f"  Processing paragraph {i}/{total} ...", flush=True)

        record = json.loads(line.strip())
        para_id = record['id']
        text = record['text']

        # Skip pure title/header paragraphs (very short, no sentence structure)
        if len(text.strip()) < 15:
            continue

        sentences = split_sentences(text)

        claims = extract_claims(para_id, sentences)
        definitions = extract_definitions(para_id, text, sentences)
        axiom_candidates = extract_axiom_candidates(para_id, text, sentences)
        references = extract_references(text)
        dependencies = extract_dependencies(text)

        extraction = {
            "paragraph_id": f"P-{para_id:04d}",
            "text_length": len(text),
            "sentence_count": len(sentences),
            "claim_count": len(claims),
            "definition_count": len(definitions),
            "axiom_candidate_count": len(axiom_candidates),
            "references": references,
            "dependencies": dependencies,
            "claim_ids": [c["claim_id"] for c in claims],
            "definition_ids": [d["definition_id"] for d in definitions],
            "axiom_candidate_ids": [a["axiom_id"] for a in axiom_candidates],
        }

        all_extractions.append(extraction)
        all_claims.extend(claims)
        all_definitions.extend(definitions)
        all_axioms.extend(axiom_candidates)

    # ── Write output files ───────────────────────────────────────────────────
    print("Writing output files ...", flush=True)

    out_para = f"{output_dir}/paragraph_extractions.jsonl"
    out_claims = f"{output_dir}/claims_complete.jsonl"
    out_defs = f"{output_dir}/definitions_complete.jsonl"
    out_axioms = f"{output_dir}/axiom_candidates_complete.jsonl"

    with open(out_para, 'w', encoding='utf-8') as f:
        for rec in all_extractions:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')

    with open(out_claims, 'w', encoding='utf-8') as f:
        for rec in all_claims:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')

    with open(out_defs, 'w', encoding='utf-8') as f:
        for rec in all_definitions:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')

    with open(out_axioms, 'w', encoding='utf-8') as f:
        for rec in all_axioms:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')

    # ── Final report ─────────────────────────────────────────────────────────
    paragraphs_processed = len(all_extractions)
    total_claims = len(all_claims)
    total_defs = len(all_definitions)
    total_axioms = len(all_axioms)

    # Domain breakdown for claims
    domain_counts = {}
    for c in all_claims:
        d = c.get('domain', 'general')
        domain_counts[d] = domain_counts.get(d, 0) + 1

    # Reference frequency
    ref_freq = {}
    for e in all_extractions:
        for r in e.get('references', []):
            ref_freq[r] = ref_freq.get(r, 0) + 1
    top_refs = sorted(ref_freq.items(), key=lambda x: -x[1])[:30]

    report = {
        "report": "PHASE 0 — COMPLETE PER-PARAGRAPH EXTRACTION",
        "book": "Theory of Liberty (Individual Property Rights) — Iran & Religion",
        "author": "Mohammadali Jannatkhahdoost",
        "total_paragraphs_in_source": total,
        "paragraphs_processed": paragraphs_processed,
        "paragraphs_skipped_too_short": total - paragraphs_processed,
        "total_claims_extracted": total_claims,
        "total_definitions_extracted": total_defs,
        "total_axiom_candidates_extracted": total_axioms,
        "claims_by_domain": domain_counts,
        "top_30_referenced_entities": dict(top_refs),
        "output_files": {
            "paragraph_extractions": out_para,
            "claims": out_claims,
            "definitions": out_defs,
            "axiom_candidates": out_axioms,
        }
    }

    report_path = f"{output_dir}/compilation_report_full.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print("\n" + "="*60)
    print("EXTRACTION COMPLETE")
    print("="*60)
    print(f"Total paragraphs in source:        {total}")
    print(f"Paragraphs processed:              {paragraphs_processed}")
    print(f"Total claims extracted:            {total_claims}")
    print(f"Total definitions extracted:       {total_defs}")
    print(f"Total axiom candidates extracted:  {total_axioms}")
    print("="*60)
    print(f"\nClaims by domain:")
    for dom, cnt in sorted(domain_counts.items(), key=lambda x: -x[1]):
        print(f"  {dom:30s}: {cnt}")
    print(f"\nTop 20 most-referenced entities:")
    for name, cnt in top_refs[:20]:
        print(f"  {name:30s}: {cnt} paragraphs")
    print(f"\nFull report written to: {report_path}")

    return report


if __name__ == '__main__':
    import_path = '/tmp/paragraphs.jsonl'
    output_dir = '/tmp/kb_full'
    process_paragraphs(import_path, output_dir)
