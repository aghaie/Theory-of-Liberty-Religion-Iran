#!/usr/bin/env python3
"""Phase 2 Steps 4-7: Competing Systems, Test Run, Counterexample Search,
Theological Necessity Audit."""

import json, os

KB = "/Users/ali/Documents/GitHub/Theory-of-Liberty-Religion-Iran/knowledge_base"

def L(p): return json.load(open(p, encoding="utf-8"))
def save(name, obj):
    for p in [f"/tmp/{name}", f"{KB}/{name}"]:
        json.dump(obj, open(p,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"  Saved: {name}", flush=True)

print("Phase 2 (steps 4-7) loaded.", flush=True)

# ════════════════════════════════════════════════════════════════════════════
# STEP 4 — GENERATE COMPETING SYSTEMS
# ════════════════════════════════════════════════════════════════════════════
print("\nStep 4: Building competing systems...", flush=True)

COMPETITORS = [
    {
        "id": "SYS-01",
        "name": "Classical Liberalism",
        "canonical_sources": ["Locke (Second Treatise)", "Mill (On Liberty)", "Smith (Theory of Moral Sentiments)"],
        "steelman_reconstruction": (
            "Axioms: (1) individuals possess natural rights to life, liberty, and property by virtue of personhood; "
            "(2) rational self-interest leads to cooperative social institutions; "
            "(3) no person may initiate force against another's rights; "
            "(4) government is limited to protection of rights and enforcement of contracts. "
            "Derivations: from (1)-(3), liberty is derived as the sphere of non-interference; "
            "from (4), government obtains legitimacy only from consent of rights-holders."
        ),
        "finite_axioms": True,
        "estimated_axiom_count": 6,
        "theological_dependency": False,
        "notes": "The strongest purely secular competing system. Richly developed tradition."
    },
    {
        "id": "SYS-02",
        "name": "Lockean Natural Rights Theory",
        "canonical_sources": ["Locke (Second Treatise)", "Nozick (Anarchy, State, and Utopia)"],
        "steelman_reconstruction": (
            "Axioms: (1) God created humans as His workmanship, entailing duty not to destroy oneself or others; "
            "(2) persons acquire property by mixing their labour with unowned things (Lockean proviso); "
            "(3) natural law is accessible by reason; "
            "(4) legitimate government derives from consent. "
            "Derivations: natural law → natural rights → property rights → limited government."
        ),
        "finite_axioms": True,
        "estimated_axiom_count": 5,
        "theological_dependency": True,
        "notes": "Closest structural competitor — also has theological grounding + property as prior to state."
    },
    {
        "id": "SYS-03",
        "name": "Hayekian Spontaneous Order",
        "canonical_sources": ["Hayek (Constitution of Liberty)", "Hayek (Law, Legislation and Liberty)"],
        "steelman_reconstruction": (
            "Axioms: (1) dispersed knowledge in society cannot be aggregated by any central planner; "
            "(2) spontaneous order (catallaxy) emerges from rule-following behaviour in markets; "
            "(3) abstract rules of conduct (not specific outcomes) are the proper subject of law; "
            "(4) individual liberty is necessary for the price system to function; "
            "(5) evolved social institutions encode tacit knowledge. "
            "Derivations: from (1)-(2), central planning is epistemically impossible → market liberty is necessary; "
            "from (3)-(5), rule of law is the institutional form of liberty."
        ),
        "finite_axioms": False,
        "estimated_axiom_count": 10,
        "theological_dependency": False,
        "notes": "Epistemological rather than deontological; rights emerge from evolutionary process rather than prior axiom."
    },
    {
        "id": "SYS-04",
        "name": "Rothbardian Libertarianism",
        "canonical_sources": ["Rothbard (Man, Economy and State)", "Rothbard (The Ethics of Liberty)"],
        "steelman_reconstruction": (
            "Axioms: (1) every person owns themselves (self-ownership axiom); "
            "(2) legitimate property arises from homesteading unowned resources; "
            "(3) the non-aggression principle (NAP): initiating force is categorically impermissible; "
            "(4) all voluntary exchange is legitimate. "
            "Derivations: from (1)+(3), the state is categorically illegitimate (systematic aggressor); "
            "from (1)+(2), property rights are derived without theological premise."
        ),
        "finite_axioms": True,
        "estimated_axiom_count": 4,
        "theological_dependency": False,
        "notes": "Most parsimonious secular competitor. Self-ownership + NAP are extremely minimal."
    },
    {
        "id": "SYS-05",
        "name": "Kantian Deontological Ethics",
        "canonical_sources": ["Kant (Groundwork)", "Kant (Metaphysics of Morals)"],
        "steelman_reconstruction": (
            "Axioms: (1) rational agents are ends-in-themselves, never merely means; "
            "(2) the Categorical Imperative (Formula of Universal Law): act only on maxims you could will to be universal laws; "
            "(3) the Formula of Humanity: treat humanity always as end, never merely as means; "
            "(4) perfect duties are absolute; imperfect duties allow latitude. "
            "Derivations: from (1)+(3), rights to bodily integrity and liberty are derived as conditions for treating persons as ends; "
            "from (2), maxims requiring coercion fail universalizability."
        ),
        "finite_axioms": True,
        "estimated_axiom_count": 4,
        "theological_dependency": False,
        "notes": "Rigorous derivation of rights from rational personhood. Highly developed formal tradition."
    },
    {
        "id": "SYS-06",
        "name": "Constitutional Liberal Democracy",
        "canonical_sources": ["Rawls (Political Liberalism)", "Dworkin (Law's Empire)", "US Constitution"],
        "steelman_reconstruction": (
            "Axioms: (1) political authority requires justification to all citizens (public reason); "
            "(2) a constitutional framework of basic rights and liberties binds all political action; "
            "(3) democratic majority rule is constrained by rights-based counter-majoritarian rules; "
            "(4) separation of powers prevents concentration. "
            "Derivations: from (1)+(2), a constitutional order protecting liberty is the uniquely legitimate form; "
            "from (3)+(4), totalitarianism is structurally prevented."
        ),
        "finite_axioms": False,
        "estimated_axiom_count": 15,
        "theological_dependency": False,
        "notes": "Institutional rather than axiomatic. Very high axiom count for complete specification."
    },
    {
        "id": "SYS-07",
        "name": "Rule Utilitarianism",
        "canonical_sources": ["Brandt (A Theory of the Good and the Right)", "Hooker (Ideal Code, Real World)"],
        "steelman_reconstruction": (
            "Axioms: (1) the right action is that which conforms to the set of rules whose general acceptance "
            "maximizes aggregate welfare; (2) welfare is measurable in principle; "
            "(3) rule compliance produces predictability essential for social cooperation. "
            "Derivations: empirical argument that liberty-protecting rules generally maximize welfare; "
            "therefore a system of liberty rights is derivable from utility maximization."
        ),
        "finite_axioms": True,
        "estimated_axiom_count": 3,
        "theological_dependency": False,
        "notes": "Most parsimonious on axiom count, but derivation of property rights depends on empirical welfare claims."
    },
    {
        "id": "SYS-08",
        "name": "Social Contractarianism",
        "canonical_sources": ["Hobbes (Leviathan)", "Rousseau (Social Contract)", "Gauthier (Morals by Agreement)"],
        "steelman_reconstruction": (
            "Axioms: (1) rational agents in a pre-political state would agree to a system of mutual constraint; "
            "(2) the terms of agreement are those that rational self-interested agents would accept; "
            "(3) political authority is legitimate only if it could have emerged from rational contract. "
            "Derivations: from (1)-(3), a minimal state protecting rights is the rational contract outcome; "
            "from Gauthier's bargaining theory, property rights are the rational division of cooperative surplus."
        ),
        "finite_axioms": True,
        "estimated_axiom_count": 5,
        "theological_dependency": False,
        "notes": "Depends on idealized rational agent model; actual contract vs. hypothetical contract ambiguity."
    },
    {
        "id": "SYS-09",
        "name": "Constitutional AI (Anthropic)",
        "canonical_sources": ["Anthropic (2023) Constitutional AI: Harmlessness from AI Feedback", "Bai et al. 2022"],
        "steelman_reconstruction": (
            "Axioms: (1) a set of principles (a 'constitution') can be used to evaluate AI outputs; "
            "(2) the principles include: be helpful, harmless, and honest; "
            "(3) AI should not assist with actions that violate human rights; "
            "(4) the system is self-supervised via AI feedback on principle compliance. "
            "Derivations: from (1)-(4), an aligned AI is one whose outputs satisfy the constitutional principles consistently."
        ),
        "finite_axioms": True,
        "estimated_axiom_count": 12,
        "theological_dependency": False,
        "notes": "Operational AI alignment system, not a political philosophy. Principles-based but not axiomatically derived."
    },
    {
        "id": "SYS-10",
        "name": "Coherent Extrapolated Volition (CEV)",
        "canonical_sources": ["Yudkowsky (2004) Coherent Extrapolated Volition"],
        "steelman_reconstruction": (
            "Axioms: (1) the CEV of humanity is the extrapolated preference of what humans would want "
            "if they knew more, thought faster, and were more the people they wish they were; "
            "(2) an AI should implement the CEV if it can be computed; "
            "(3) individual volitions are aggregated through a process that is itself fair by CEV standards. "
            "Derivations: from (1)-(3), liberty-preserving outcomes are those the CEV would select."
        ),
        "finite_axioms": False,
        "estimated_axiom_count": None,
        "theological_dependency": False,
        "notes": "Procedural rather than axiomatic. No explicit finite axiom set. Computability not demonstrated."
    },
    {
        "id": "SYS-11",
        "name": "Natural Law Theory (Thomistic)",
        "canonical_sources": ["Aquinas (Summa Theologiae)", "Finnis (Natural Law and Natural Rights)"],
        "steelman_reconstruction": (
            "Axioms: (1) human nature has a telos (end/purpose) knowable by reason; "
            "(2) moral law is participation in eternal law via human reason; "
            "(3) basic goods (life, knowledge, friendship, practical reasonableness) are self-evidently valuable; "
            "(4) the common good requires political authority; "
            "(5) authority is just only when it respects natural rights and common good. "
            "Derivations: from (1)-(3), human rights are derived as conditions for the basic goods; "
            "from (4)-(5), limited government is derived."
        ),
        "finite_axioms": True,
        "estimated_axiom_count": 7,
        "theological_dependency": True,
        "notes": "Richly developed tradition. More axioms than the ToL (7 vs 6). Also has theological grounding."
    },
    {
        "id": "SYS-12",
        "name": "Rawlsian Liberalism",
        "canonical_sources": ["Rawls (A Theory of Justice)", "Rawls (Political Liberalism)"],
        "steelman_reconstruction": (
            "Axioms: (1) the veil of ignorance: rational agents behind the veil have no knowledge of their "
            "position in society; (2) from (1), rational agents would choose: (a) equal basic liberties for all, "
            "(b) fair equality of opportunity, (c) the difference principle (benefit the least advantaged). "
            "(3) principles of justice are those rational agents behind the veil would choose. "
            "Derivations: from (1)+(2), a constitutional framework protecting basic liberties is required by justice."
        ),
        "finite_axioms": True,
        "estimated_axiom_count": 4,
        "theological_dependency": False,
        "notes": "Hypothetical-contractarian. Veil of ignorance is a methodological device, not an empirical claim."
    },
    {
        "id": "SYS-00",
        "name": "Theory of Liberty (ToL) — reference",
        "canonical_sources": ["Jannatkhahdoost (Theory of Liberty, Religion, Iran)"],
        "steelman_reconstruction": (
            "Axioms (minimum kernel, 6): A-000001 (FW), A-000004 (Tawhid), A-000006 (Resurrection), "
            "A-000007 (Prophethood), A-000011 (Finite Axioms), A-000012 (Consistency). "
            "Derivations: FW → self-ownership → property rights → liberty; "
            "Tawhid → no-servitude → anti-statism; "
            "Resurrection → last-round solution → liberty stability; "
            "Prophethood → anti-fraud → authentic-religion identification; "
            "A-000011+A-000012 → CFS methodology → formal evaluation criteria."
        ),
        "finite_axioms": True,
        "estimated_axiom_count": 6,
        "theological_dependency": True,
        "notes": "Reference system. 3 secular axioms + 3 theological axioms in minimum kernel."
    },
]

save("74_competing_systems.json", {
    "total_systems": len(COMPETITORS),
    "including_reference": True,
    "reference_system": "SYS-00",
    "systems": COMPETITORS,
    "note": "All systems are steelmanned — strongest possible reconstruction used.",
})

# ════════════════════════════════════════════════════════════════════════════
# STEP 5 — RUN TEST SUITE
# ════════════════════════════════════════════════════════════════════════════
print("Step 5: Running test suite...", flush=True)

RESULTS = [
    # ────────────────────────────── SYS-00: Theory of Liberty (reference) ──
    {
        "system_id": "SYS-00",
        "system_name": "Theory of Liberty (reference)",
        "criteria": {
            "C1": {"verdict":"PASS","score":10,"justification":"Kernel has no confirmed contradictions. Self-application test passed. Phase 1 score 71/100."},
            "C2": {"verdict":"PASS","score":8,"justification":"6 axioms in minimum kernel. Finite and enumerable."},
            "C3": {"verdict":"PASS","score":10,"justification":"Full derivation: FW→self-ownership→PR→liberty. Traced through 46 backbone edges."},
            "C4": {"verdict":"PASS","score":9,"justification":"A-000002+A-000008: property is prior to state. Rule of Taslit. Anti-statism derived from Tawhid."},
            "C5": {"verdict":"PASS","score":9,"justification":"A-000006 (Resurrection): unknown terminal prevents backward induction. Standard game-theory result applied."},
            "C6": {"verdict":"PASS","score":8,"justification":"Tawhid prohibits servitude to any entity. State as coercive monopoly = shirk (servitude to non-God). Structural prohibition derived."},
            "C7": {"verdict":"PARTIAL","score":4,"justification":"Tawhid is agreement-admissible via negative definition (not 'you must believe' but 'nothing else deserves servitude'). However requires accepting a theological frame. Partial."},
            "C8": {"verdict":"PARTIAL","score":3.5,"justification":"Accountability via Resurrection (divine) + community enforcement. Non-coercive collective accountability mechanism is present but not fully formalized."},
            "C9": {"verdict":"PASS","score":6,"justification":"26 formalizations produced. Constraints on AI: forbid servitude-maximizing objectives, require property-rights preservation, require game-theoretic stability."},
            "C10":{"verdict":"PARTIAL","score":2.5,"justification":"6 axioms; A-000003 confirmed redundant. 5/6 core axioms appear independent. One overlap identified."},
        },
        "total_score": 10+8+10+9+9+8+4+3.5+6+2.5,
        "max_score": 80,
    },
    # ────────────────────────────── SYS-01: Classical Liberalism ──────────
    {
        "system_id": "SYS-01",
        "system_name": "Classical Liberalism",
        "criteria": {
            "C1": {"verdict":"PASS","score":10,"justification":"Classical liberalism is internally consistent within its axioms. Mill and Locke are not contradictory. The harm principle does not contradict natural rights (different domains)."},
            "C2": {"verdict":"PASS","score":8,"justification":"Reducible to ~6 axioms (natural rights, harm principle, consent, property, limited government, rule of law). Enumerable."},
            "C3": {"verdict":"PARTIAL","score":5,"justification":"Liberty is the founding premise of classical liberalism, not derived from a deeper axiom. It is asserted, not derived. The grounding is typically 'self-evident' or 'natural' — both are assertion, not derivation."},
            "C4": {"verdict":"PASS","score":9,"justification":"Property rights are definitively pre-political in Locke-influenced classical liberalism. Property arises from labour/homesteading, not state grant."},
            "C5": {"verdict":"FAIL","score":0,"justification":"Classical liberalism has NO structural solution to the last-round problem. It relies on reputation effects, constitutional constraints, and cultural norms — none of which provide game-theoretic structural stability in finite interactions. This is the system's most significant gap."},
            "C6": {"verdict":"PARTIAL","score":4,"justification":"Constitutional constraints and separation of powers resist totalitarianism. But these are institutional mechanisms, not structural axioms — they can be overridden by constitutional revision or emergency powers. The anti-totalitarianism is not axiomatically derived."},
            "C7": {"verdict":"PASS","score":8,"justification":"Classical liberal principles do not require acceptance of particular ethnic, religious, or historical claims. Harm principle and property rights can be accepted by rational agents across cultures."},
            "C8": {"verdict":"PARTIAL","score":3.5,"justification":"Classical liberalism relies on state enforcement for accountability (courts, police). This creates a tension: state enforcement is itself coercive. The mechanism is acknowledged but the tension unresolved."},
            "C9": {"verdict":"PARTIAL","score":3,"justification":"Classical liberal principles (non-interference, property rights) can be expressed as AI constraints, but the system was not designed for AI and lacks formal specification."},
            "C10":{"verdict":"PARTIAL","score":2.5,"justification":"Axiom set is moderately minimal but contains some redundancies (e.g., rule of law is derivable from natural rights + enforcement logic)."},
        },
        "total_score": 10+8+5+9+0+4+8+3.5+3+2.5,
        "max_score": 80,
    },
    # ────────────────────────────── SYS-02: Lockean Natural Rights ─────────
    {
        "system_id": "SYS-02",
        "system_name": "Lockean Natural Rights Theory",
        "criteria": {
            "C1": {"verdict":"PASS","score":10,"justification":"Locke's system is internally consistent. No confirmed contradiction in the core natural rights framework."},
            "C2": {"verdict":"PASS","score":8,"justification":"Reducible to ~5 axioms: creator duty, labour-mixing, natural law, property, consent. Enumerable."},
            "C3": {"verdict":"PASS","score":10,"justification":"Liberty is derived: God creates → humans are His property → humans must not be violated → natural rights → liberty. Full derivation exists."},
            "C4": {"verdict":"PASS","score":9,"justification":"Property is definitively pre-political in Locke. The labour-mixing theory grounds property independently of any state."},
            "C5": {"verdict":"FAIL","score":0,"justification":"No structural last-round solution. Locke relies on natural law enforcement by community and the state as trustee — both fail the last-round problem. In the final period, rational self-interest dominates."},
            "C6": {"verdict":"PARTIAL","score":4,"justification":"Locke's theory of revolution (people may overthrow government that violates natural rights) provides resistance to tyranny, but it is a political mechanism, not a structural axiom. It requires collective action that itself faces coordination problems."},
            "C7": {"verdict":"PARTIAL","score":4,"justification":"Lockean natural law requires accepting: God exists, natural law is knowable by reason, and the creator-ownership premise. The theological axioms are more specific (require a creator concept) than Tawhid's negative definition."},
            "C8": {"verdict":"PARTIAL","score":3.5,"justification":"Accountability via community enforcement and natural law internalization. Similar problem to classical liberalism: relies on state for enforcement in practice."},
            "C9": {"verdict":"PARTIAL","score":3,"justification":"Natural rights constraints can be expressed as AI design principles. However, not designed for AI applications and lacks formal specification."},
            "C10":{"verdict":"PASS","score":5,"justification":"Locke's 5 axioms appear independent. The labour-mixing theory is not derivable from the creator-duty axiom alone; consent is not derivable from property. Reasonably minimal."},
        },
        "total_score": 10+8+10+9+0+4+4+3.5+3+5,
        "max_score": 80,
    },
    # ────────────────────────────── SYS-03: Hayekian Order ─────────────────
    {
        "system_id": "SYS-03",
        "system_name": "Hayekian Spontaneous Order",
        "criteria": {
            "C1": {"verdict":"PASS","score":10,"justification":"Hayekian epistemological arguments are internally consistent. No self-contradiction in the knowledge-dispersion premise."},
            "C2": {"verdict":"FAIL","score":0,"justification":"Hayek's system is NOT axiomatically finite. It relies on evolutionary emergence, tacit knowledge, and spontaneous order — all of which are process-based, not axiom-based. The theory explicitly rejects axiomatization of social outcomes."},
            "C3": {"verdict":"FAIL","score":0,"justification":"Liberty is derived as epistemically necessary (central planning is impossible), not as a moral axiom. The derivation depends on empirical claims about knowledge dispersal that are contingent. Liberty is a conclusion from epistemic argument, but not from a foundational moral axiom — the grounding is empirical-epistemic, not normative."},
            "C4": {"verdict":"PARTIAL","score":4.5,"justification":"Hayek's evolved legal institutions protect property. But property rights are not pre-political in the strong Lockean sense — they emerge from evolutionary legal process. The pre-political status is weaker."},
            "C5": {"verdict":"FAIL","score":0,"justification":"No solution to last-round problem. Hayek's spontaneous order depends on repeated interactions and reputation — both collapse in the last period. The evolutionary argument does not prevent terminal-period defection."},
            "C6": {"verdict":"PARTIAL","score":4,"justification":"Hayek's strong argument against central planning is a form of anti-totalitarianism. But it is epistemological (central planning CANNOT work) rather than structural (central planning is FORBIDDEN). The anti-totalitarianism is consequentialist, not axiomatic."},
            "C7": {"verdict":"PASS","score":8,"justification":"Hayekian principles do not require any particular religious, cultural, or historical commitment. The knowledge-problem argument is universally applicable."},
            "C8": {"verdict":"PARTIAL","score":3.5,"justification":"Market mechanisms and legal institutions provide accountability. But these rely on state enforcement courts and legal system. Same tension as classical liberalism."},
            "C9": {"verdict":"PARTIAL","score":3,"justification":"Hayekian principles are applicable to AI (decentralized AI, market-discovery AI). But not formally specified for AI alignment."},
            "C10":{"verdict":"FAIL","score":0,"justification":"Not axiomatically minimal — not axiomatically organized at all. The 'axioms' are epistemological observations, not formal axioms."},
        },
        "total_score": 10+0+0+4.5+0+4+8+3.5+3+0,
        "max_score": 80,
    },
    # ────────────────────────────── SYS-04: Rothbardian Libertarianism ─────
    {
        "system_id": "SYS-04",
        "system_name": "Rothbardian Libertarianism",
        "criteria": {
            "C1": {"verdict":"PASS","score":10,"justification":"Self-ownership + NAP are internally consistent. Rothbard's system has no confirmed internal contradiction within its stated axioms."},
            "C2": {"verdict":"PASS","score":8,"justification":"4 axioms: self-ownership, homesteading, NAP, voluntary exchange. Highly minimal and enumerable."},
            "C3": {"verdict":"PASS","score":10,"justification":"Full derivation: self-ownership → body as property → property rights → liberty (as sphere of non-aggression). Rothbard's derivation is explicit and traceable."},
            "C4": {"verdict":"PASS","score":9,"justification":"Property is definitively pre-political — it arises from self-ownership, prior to any state. The state as aggressor is derived from the NAP. This is the strongest statement of property-prior-to-state."},
            "C5": {"verdict":"FAIL","score":0,"justification":"NO solution to last-round problem. This is Rothbardian libertarianism's most critical vulnerability. In purely secular game theory, NAP compliance is rational in repeated games but collapses in the final period. Rothbard has no structural response to this. 'Virtue ethics' is sometimes invoked but this adds axioms."},
            "C6": {"verdict":"PASS","score":8,"justification":"The state is categorically prohibited as systematic aggressor under NAP. This is the strongest structural anti-totalitarianism available in any secular system: not 'limit the state' but 'no state is legitimate.' Axiomatically derived, not institutional."},
            "C7": {"verdict":"PASS","score":8,"justification":"Self-ownership and NAP do not require any religious, cultural, or historical commitment. Rothbard's 'ethics of liberty' is explicitly universal and secular. High agreement-admissibility."},
            "C8": {"verdict":"PARTIAL","score":3.5,"justification":"Accountability via voluntary courts, arbitration, and community enforcement. The stateless accountability mechanisms are theorized but have not been empirically demonstrated at scale."},
            "C9": {"verdict":"PARTIAL","score":3,"justification":"NAP + self-ownership can be expressed as AI constraints: no AI objective may override property rights, no AI may initiate coercive action. Formal specification is possible but not designed for AI."},
            "C10":{"verdict":"PASS","score":5,"justification":"4 axioms, each independent. Self-ownership is not derivable from NAP alone; homesteading is not derivable from self-ownership alone; NAP follows from but is not identical to self-ownership. Well-minimized."},
        },
        "total_score": 10+8+10+9+0+8+8+3.5+3+5,
        "max_score": 80,
    },
    # ────────────────────────────── SYS-05: Kantian Ethics ─────────────────
    {
        "system_id": "SYS-05",
        "system_name": "Kantian Deontological Ethics",
        "criteria": {
            "C1": {"verdict":"PARTIAL","score":5,"justification":"Kant's system has well-known internal tensions: the perfect duty to keep promises can conflict with the perfect duty to preserve life. The universalizability formula and the humanity formula sometimes yield different results (Bernard Williams). Not fully consistent."},
            "C2": {"verdict":"PASS","score":8,"justification":"4 main formulations of CI, plus duties to self and others. Finite and enumerable."},
            "C3": {"verdict":"PASS","score":10,"justification":"Full derivation: rational personhood → end-in-itself → cannot be coerced → right to liberty. The Formula of Humanity directly grounds liberty rights."},
            "C4": {"verdict":"PARTIAL","score":4.5,"justification":"Kant's property rights (in Metaphysics of Morals) are derived from rational agency. Pre-political property exists in Kant but the derivation is complex and property rights can be overridden by the general will in certain readings."},
            "C5": {"verdict":"FAIL","score":0,"justification":"No structural last-round solution. Kant relies on the categorical imperative as overriding rational self-interest — but in game theory, the CI is not self-enforcing. In the last period, a purely Kantian agent may comply with duty, but this requires prior commitment to duty that is itself not game-theoretically stable."},
            "C6": {"verdict":"PARTIAL","score":4,"justification":"The Formula of Humanity prevents using persons as mere means — this is an anti-totalitarian principle. But Kant's support for republican government (not full anti-statism) leaves room for significant state power."},
            "C7": {"verdict":"PASS","score":8,"justification":"Kant's ethics are explicitly universal — derived from rational personhood, not historical, religious, or cultural particularity. High agreement-admissibility."},
            "C8": {"verdict":"PARTIAL","score":3.5,"justification":"Accountability via duty and rational law. Kant has a theory of punishment as rational desert. But depends on legal institutions."},
            "C9": {"verdict":"PARTIAL","score":3,"justification":"Kantian AI alignment: Categorical Imperative as machine ethics (cf. Allen et al.). Formal specification possible. End-in-itself principle translatable to AI constraints."},
            "C10":{"verdict":"PARTIAL","score":2.5,"justification":"Kant's 4 formulations of the CI are arguably different expressions of one principle, but this is debated. Some redundancy possible."},
        },
        "total_score": 5+8+10+4.5+0+4+8+3.5+3+2.5,
        "max_score": 80,
    },
    # ─── SYS-06: Constitutional Liberal Democracy ─────────────────────────
    {
        "system_id": "SYS-06",
        "system_name": "Constitutional Liberal Democracy",
        "criteria": {
            "C1": {"verdict":"PARTIAL","score":5,"justification":"Constitutional democracy has tensions: majority rule vs. rights constraints, proceduralism vs. substantive justice. Not always consistent."},
            "C2": {"verdict":"FAIL","score":0,"justification":"No finite formal axiom set. Constitutional democracy is institutional and procedural, not axiomatic. Different constitutions contain different rights. No minimal specification exists."},
            "C3": {"verdict":"PARTIAL","score":5,"justification":"Liberty is constitutionally protected but not axiomatically derived. The derivation relies on historical consensus and political philosophy, not formal axiomatics."},
            "C4": {"verdict":"FAIL","score":0,"justification":"In constitutional democracy, property rights are not strictly pre-political. They can be modified by democratic legislation (eminent domain, taxation, redistribution). The pre-political status of property is explicitly rejected in many constitutional traditions."},
            "C5": {"verdict":"PARTIAL","score":4.5,"justification":"Constitutional constraints and judicial review provide some structural stability. Term limits and democratic accountability create partial iterative mechanisms. But these are institutional, not structural game-theoretic solutions."},
            "C6": {"verdict":"PARTIAL","score":4,"justification":"Separation of powers and checks-and-balances resist concentration. But totalitarianism has emerged from constitutional democracies (Weimar Republic → Nazi Germany). The constitutional mechanism is insufficient by historical evidence."},
            "C7": {"verdict":"PARTIAL","score":4,"justification":"Constitutional democracy can be accepted by rational agents across cultures but depends on prior acceptance of democratic legitimacy norms which are not universally held."},
            "C8": {"verdict":"PASS","score":7,"justification":"Constitutional accountability is the strongest institutional accountability mechanism. Courts, elections, civil society. Well-developed."},
            "C9": {"verdict":"PARTIAL","score":3,"justification":"Constitutional rights frameworks can inform AI regulation (rights-based AI governance). But not formally specified for AI alignment."},
            "C10":{"verdict":"FAIL","score":0,"justification":"Not axiomatically organized. No minimal axiom set exists. Each constitution is different."},
        },
        "total_score": 5+0+5+0+4.5+4+4+7+3+0,
        "max_score": 80,
    },
    # ─── SYS-07: Rule Utilitarianism ──────────────────────────────────────
    {
        "system_id": "SYS-07",
        "system_name": "Rule Utilitarianism",
        "criteria": {
            "C1": {"verdict":"FAIL","score":0,"justification":"Rule utilitarianism has a known consistency problem: if following a rule decreases welfare in a specific case, it is unclear whether the rule applies or utility calculation overrides. The transition from act to rule generates inconsistency."},
            "C2": {"verdict":"PASS","score":8,"justification":"3 axioms: welfare maximization, rule compliance as means, measurement principle. Very minimal."},
            "C3": {"verdict":"FAIL","score":0,"justification":"Liberty is derived empirically (free societies maximize welfare). This derivation is contingent, not necessary. In scenarios where restricting liberty maximizes welfare, the derivation fails. Liberty is not a logically necessary conclusion from utility axioms."},
            "C4": {"verdict":"FAIL","score":0,"justification":"Property rights in rule utilitarianism are instrumental to welfare maximization. They can be overridden when restriction of property maximizes overall welfare. Pre-political status explicitly rejected."},
            "C5": {"verdict":"FAIL","score":0,"justification":"No structural last-round solution. In the last period, utility maximization in iterated games produces the same backward induction as any other system."},
            "C6": {"verdict":"FAIL","score":0,"justification":"Utilitarianism historically supports totalitarianism under sufficient welfare arguments: a benevolent dictator maximizing aggregate welfare is not prohibited by utilitarian axioms. The anti-totalitarianism is not axiomatic."},
            "C7": {"verdict":"PARTIAL","score":4,"justification":"Rule utilitarianism can be accepted in principle by rational agents. The welfare-maximization premise is broadly intuitive. But the measurement problem (how to measure welfare) makes operationalization agreement-inadmissible."},
            "C8": {"verdict":"PARTIAL","score":3.5,"justification":"Accountability via welfare consequences. Rule violation reduces welfare, creating accountability incentive. But this requires welfare measurement which is contested."},
            "C9": {"verdict":"PARTIAL","score":3,"justification":"Utility maximization is the dominant AI objective function (RLHF, reward modeling). Rule utilitarianism is closest to current AI design. But the rule → utility tension undermines formal specification."},
            "C10":{"verdict":"PASS","score":5,"justification":"3 independent axioms. Well-minimized but the minimality makes the derivation of property rights require empirical premises."},
        },
        "total_score": 0+8+0+0+0+0+4+3.5+3+5,
        "max_score": 80,
    },
    # ─── SYS-08: Social Contractarianism ──────────────────────────────────
    {
        "system_id": "SYS-08",
        "system_name": "Social Contractarianism",
        "criteria": {
            "C1": {"verdict":"PARTIAL","score":5,"justification":"Contractarianism has a known consistency problem: the actual contract vs. hypothetical contract distinction. Hobbes's actual contract (submit to Leviathan) generates different results than Gauthier's hypothetical contract."},
            "C2": {"verdict":"PASS","score":8,"justification":"5 axioms reducible from standard formulation. Finite."},
            "C3": {"verdict":"PARTIAL","score":5,"justification":"Liberty is derived as a component of the rational contract (parties prefer liberty over servitude). But this derivation requires that rational agents behind the contract prefer liberty — which is an additional assumption."},
            "C4": {"verdict":"PARTIAL","score":4.5,"justification":"Gauthier derives property rights from rational bargaining over cooperative surplus. Pre-political in principle, but the derivation depends on the rational agent model which is not pre-political."},
            "C5": {"verdict":"FAIL","score":0,"justification":"No structural last-round solution. The social contract in finite interactions is itself subject to the last-round problem: why comply in the final period? Hobbes acknowledges this and responds with sovereign enforcement — which is state coercion."},
            "C6": {"verdict":"PARTIAL","score":4,"justification":"Rational contractors would not agree to totalitarianism (it reduces everyone's welfare below what they could ensure individually). But this depends on the rationality assumptions and fails if the Leviathan argument (Hobbes) is accepted."},
            "C7": {"verdict":"PASS","score":8,"justification":"The social contract framework is explicitly universal — derived from rational self-interest, not cultural particularity. High agreement-admissibility for the Gauthier/Rawls variants."},
            "C8": {"verdict":"PARTIAL","score":3.5,"justification":"Contract compliance via self-interest and reputation. Relies on state enforcement ultimately."},
            "C9": {"verdict":"PARTIAL","score":3,"justification":"Contract principles can inform AI governance. AI systems governed by contractarian principles: respect bargained-for agreements, do not defect."},
            "C10":{"verdict":"PARTIAL","score":2.5,"justification":"Moderate redundancy: the rational agent and the contract premises partially overlap."},
        },
        "total_score": 5+8+5+4.5+0+4+8+3.5+3+2.5,
        "max_score": 80,
    },
    # ─── SYS-09: Constitutional AI ────────────────────────────────────────
    {
        "system_id": "SYS-09",
        "system_name": "Constitutional AI (Anthropic)",
        "criteria": {
            "C1": {"verdict":"PARTIAL","score":5,"justification":"The constitutional principles are not formally proven consistent. Different principles can conflict (helpfulness vs. harmlessness). No formal consistency proof exists."},
            "C2": {"verdict":"PASS","score":8,"justification":"A finite set of constitutional principles is used (12-50 principles depending on version). Enumerable."},
            "C3": {"verdict":"FAIL","score":0,"justification":"Liberty is not axiomatically derived. 'Be helpful, harmless, and honest' does not derive liberty as a formal conclusion. Liberty is at most an instrumental value within the constitution."},
            "C4": {"verdict":"FAIL","score":0,"justification":"No axiom establishing property rights. Constitutional AI does not ground property rights as pre-political."},
            "C5": {"verdict":"FAIL","score":0,"justification":"No last-round solution. Constitutional AI is not designed for social game-theoretic stability."},
            "C6": {"verdict":"PARTIAL","score":4,"justification":"Constitutional AI principles include prohibition on helping with illegal activities and harmful content. This provides some anti-totalitarian constraint but it is operational, not axiomatic."},
            "C7": {"verdict":"PARTIAL","score":4,"justification":"The constitutional principles are designed to be broadly acceptable. But they are specified by Anthropic, not derived from universal rational premises. Agreement-admissibility is partial."},
            "C8": {"verdict":"PASS","score":7,"justification":"AI feedback and human oversight provide strong accountability mechanisms. The system is designed for accountability."},
            "C9": {"verdict":"PASS","score":6,"justification":"This system IS an AI alignment system. Full formal specification for AI. Direct applicability."},
            "C10":{"verdict":"FAIL","score":0,"justification":"Principles are not axiomatically minimal. Many are redundant or overlapping."},
        },
        "total_score": 5+8+0+0+0+4+4+7+6+0,
        "max_score": 80,
    },
    # ─── SYS-10: CEV ──────────────────────────────────────────────────────
    {
        "system_id": "SYS-10",
        "system_name": "Coherent Extrapolated Volition (CEV)",
        "criteria": {
            "C1": {"verdict":"FAIL","score":0,"justification":"CEV has a fundamental consistency problem: individual extrapolated volitions may be mutually inconsistent. No procedure is specified for resolving contradictions in the aggregate CEV."},
            "C2": {"verdict":"FAIL","score":0,"justification":"CEV is not axiomatic. It is procedural and computational. No finite axiom set. Computability not demonstrated."},
            "C3": {"verdict":"PARTIAL","score":5,"justification":"CEV would likely derive liberty-respecting norms (most people's extrapolated volitions prefer autonomy). But this is contingent, not necessary."},
            "C4": {"verdict":"PARTIAL","score":4.5,"justification":"CEV might derive pre-political property rights if human volitions tend that way. But this is an empirical claim about actual human values, not a logical derivation."},
            "C5": {"verdict":"PARTIAL","score":4.5,"justification":"CEV's unknown terminal (CEV computation is not complete) provides informal epistemic uncertainty. But this is not a structural mechanism — it is a feature of the theory's incompleteness."},
            "C6": {"verdict":"PARTIAL","score":4,"justification":"CEV presumably would not condone totalitarianism (most humans do not want it). But no structural prohibition exists."},
            "C7": {"verdict":"FAIL","score":0,"justification":"CEV requires accepting: (1) a superintelligent AI can compute it, (2) the extrapolation procedure is correct, (3) the aggregate is well-defined. These are substantial commitments most rational agents would not accept."},
            "C8": {"verdict":"PARTIAL","score":3.5,"justification":"Accountability via CEV: the AI implements the CEV which is the aggregate ideal preference. But this requires trusting the computation."},
            "C9": {"verdict":"PASS","score":6,"justification":"CEV is explicitly designed as an AI alignment solution. It is the most ambitious AI alignment proposal. Full applicability."},
            "C10":{"verdict":"FAIL","score":0,"justification":"Not axiomatically organized."},
        },
        "total_score": 0+0+5+4.5+4.5+4+0+3.5+6+0,
        "max_score": 80,
    },
    # ─── SYS-11: Natural Law Theory ───────────────────────────────────────
    {
        "system_id": "SYS-11",
        "system_name": "Natural Law Theory (Thomistic)",
        "criteria": {
            "C1": {"verdict":"PASS","score":10,"justification":"Thomistic natural law is internally consistent within its framework. No confirmed contradiction in Finnis's reconstruction."},
            "C2": {"verdict":"PASS","score":8,"justification":"7 basic goods + 9 requirements of practical reasonableness. Finite and enumerable."},
            "C3": {"verdict":"PASS","score":10,"justification":"Full derivation: human nature → telos → basic goods → rights → liberty as condition for flourishing. Rigorous derivation via Finnis."},
            "C4": {"verdict":"PASS","score":9,"justification":"Natural law grounds property rights in human nature and reason, prior to any state. Pre-political property is fundamental to natural law tradition."},
            "C5": {"verdict":"FAIL","score":0,"justification":"No structural last-round solution. Natural law relies on internalized virtue and natural inclinations. In purely game-theoretic analysis, the last-period incentive dominates. Natural law has no infinite-horizon mechanism."},
            "C6": {"verdict":"PARTIAL","score":4,"justification":"Natural law prohibits grave injustices and unlimited government (lex iniusta non est lex). But the prohibition is moral, not structural. Historically, natural law has been invoked both for and against strong state power."},
            "C7": {"verdict":"PARTIAL","score":4,"justification":"Thomistic natural law requires accepting: God exists, human nature has a telos accessible to reason, the basic goods are non-arbitrary. These are metaphysical commitments not all rational agents share."},
            "C8": {"verdict":"PARTIAL","score":3.5,"justification":"Natural law accountability via conscience and legal systems. Strong theory of punishment as corrective justice. But relies on state enforcement."},
            "C9": {"verdict":"PARTIAL","score":3,"justification":"Natural law constraints applicable to AI (respect human dignity, support human flourishing). Not formally specified for AI but compatible."},
            "C10":{"verdict":"PARTIAL","score":2.5,"justification":"7 axioms vs. theory's 6. The basic goods may not all be independent (some overlap between life and health, knowledge and play)."},
        },
        "total_score": 10+8+10+9+0+4+4+3.5+3+2.5,
        "max_score": 80,
    },
    # ─── SYS-12: Rawlsian Liberalism ──────────────────────────────────────
    {
        "system_id": "SYS-12",
        "system_name": "Rawlsian Liberalism",
        "criteria": {
            "C1": {"verdict":"PARTIAL","score":5,"justification":"Rawls's two principles have known tensions: the difference principle can conflict with the equal liberty principle. Lexical ordering resolves most but not all conflicts."},
            "C2": {"verdict":"PASS","score":8,"justification":"3 core axioms: veil of ignorance, maximin reasoning, two principles. Reducible to finite set."},
            "C3": {"verdict":"PARTIAL","score":5,"justification":"Equal basic liberties are derived as the first principle of justice (rational agents behind veil choose them). But the derivation depends on the veil of ignorance device which itself requires justification."},
            "C4": {"verdict":"FAIL","score":0,"justification":"Property rights in Rawls are NOT pre-political. Rawls explicitly allows redistribution (difference principle). The 'property-owning democracy' is a political arrangement, not a pre-political right."},
            "C5": {"verdict":"FAIL","score":0,"justification":"No structural last-round solution. Rawlsian justice applies to the basic structure of society, not individual game-theoretic interactions. No mechanism for terminal-period stability."},
            "C6": {"verdict":"PARTIAL","score":4,"justification":"Equal basic liberties (first principle) are lexically prior to other considerations, providing some structural protection. But Rawls supports democratic state authority which can restrict liberty in principle."},
            "C7": {"verdict":"PASS","score":8,"justification":"Rawls's 'public reason' framework is explicitly designed for acceptance across reasonable comprehensive doctrines. High agreement-admissibility within liberal societies."},
            "C8": {"verdict":"PARTIAL","score":3.5,"justification":"Accountability via democratic institutions. Constitutional constraints provide formal accountability."},
            "C9": {"verdict":"PARTIAL","score":3,"justification":"Rawlsian constraints applicable to AI policy. Not designed for AI alignment."},
            "C10":{"verdict":"PARTIAL","score":2.5,"justification":"Some redundancy: the difference principle can be partially derived from veil reasoning + risk-aversion."},
        },
        "total_score": 5+8+5+0+0+4+8+3.5+3+2.5,
        "max_score": 80,
    },
]

# Compute and annotate
for r in RESULTS:
    r["percentage"] = round(r["total_score"] / r["max_score"] * 100, 1)
    r["criteria_passed"] = sum(1 for c in r["criteria"].values() if c["verdict"]=="PASS")
    r["criteria_partial"] = sum(1 for c in r["criteria"].values() if c["verdict"]=="PARTIAL")
    r["criteria_failed"] = sum(1 for c in r["criteria"].values() if c["verdict"]=="FAIL")
    r["c5_last_round"] = r["criteria"]["C5"]["verdict"]
    r["c3_grounding"] = r["criteria"]["C3"]["verdict"]

results_sorted = sorted(RESULTS, key=lambda x: -x["total_score"])

save("75_competitor_results.json", {
    "test_suite_max_score": 80,
    "ranking": [
        {"rank": i+1, "system": r["system_name"], "score": r["total_score"], "pct": r["percentage"],
         "passed": r["criteria_passed"], "partial": r["criteria_partial"], "failed": r["criteria_failed"],
         "c5_last_round": r["c5_last_round"]}
        for i, r in enumerate(results_sorted)
    ],
    "results": RESULTS,
    "critical_finding": (
        "NO competing system PASSES criterion C5 (Last-Round Problem) except Theory of Liberty. "
        "This is the most structurally discriminating criterion. "
        "Rothbardian Libertarianism scores highest among secular systems (64.5/80 = 81%) "
        "but FAILS C5 and C5 alone prevents it from matching the Theory of Liberty's overall score."
    ),
})

# ════════════════════════════════════════════════════════════════════════════
# STEP 6 — COUNTEREXAMPLE SEARCH
# ════════════════════════════════════════════════════════════════════════════
print("Step 6: Counterexample search...", flush=True)

COUNTEREXAMPLES = [
    {
        "id": "CE-001",
        "name": "Rothbardian Libertarianism + Infinite Shadow of the Future",
        "description": (
            "Augment Rothbardian libertarianism (self-ownership, NAP, homesteading, voluntary exchange) "
            "with a 5th axiom: 'Agents rationally assign positive probability to the continuation of social "
            "interaction in every period (Axelrod/Fudenberg discount-factor argument).' "
            "This produces: δ sufficiently close to 1 → cooperation is always a Nash equilibrium even in "
            "finite repetitions. The Resurrection mechanism is replaced by a secular infinite-shadow axiom."
        ),
        "axiom_count": 5,
        "theological_axioms": 0,
        "criteria_analysis": {
            "C1": "PASS — consistent.",
            "C2": "PASS — 5 finite axioms.",
            "C3": "PASS — self-ownership → liberty.",
            "C4": "PASS — property pre-political.",
            "C5": "PARTIAL — the 'infinite shadow' requires δ→1, which is an empirical condition. If δ < threshold, defection re-emerges. It is not structurally guaranteed as a logical consequence, only as a sufficient condition. The Theory of Liberty's Resurrection provides an ABSOLUTE (not probabilistic) unknown terminal, making cooperation always rational regardless of δ.",
            "C6": "PASS — NAP categorically forbids state.",
            "C7": "PASS — secular, universal.",
            "C8": "PARTIAL — stateless accountability only.",
            "C9": "PARTIAL — not designed for AI.",
            "C10": "PASS — 5 independent axioms.",
        },
        "verdict": "PARTIAL_COUNTEREXAMPLE",
        "analysis": (
            "This system passes 7/10 criteria and partially passes 2 others, failing only C5 fully. "
            "The 'infinite shadow' argument weakens C5: δ-dependent stability is probabilistic, not structural. "
            "The Theory of Liberty's Resurrection provides ABSOLUTE stability (unknown terminal = always cooperate), "
            "while this system provides CONDITIONAL stability (δ > threshold). "
            "The counterexample is genuine but inferior on C5: it is a PARTIAL counterexample. "
            "VERDICT: Does not fully satisfy all required properties. Theory of Liberty maintains advantage on C5."
        ),
        "strength": "STRONGEST_SECULAR_COUNTEREXAMPLE",
    },
    {
        "id": "CE-002",
        "name": "Lockean Natural Rights + Eschatological Secular Interpretation",
        "description": (
            "Reinterpret Locke's Resurrection-equivalent: humans are God's workmanship (duty not to destroy), "
            "combined with a philosophical naturalist reinterpretation: 'agents rationally act as if life has "
            "infinite value (Pascal-Locke argument).' Locke already has theological grounding and property "
            "rights prior to state. This system is structurally close to the Theory of Liberty."
        ),
        "axiom_count": 6,
        "theological_axioms": 2,
        "criteria_analysis": {
            "C5": "PARTIAL — Pascal-Locke argument is probabilistic, not structural. God-as-workmanship is a theological axiom but does not provide game-theoretic unknown terminal.",
            "C7": "PARTIAL — requires creator-concept theological axiom which is more specific than Tawhid's negative definition.",
        },
        "verdict": "PARTIAL_COUNTEREXAMPLE",
        "analysis": (
            "Locke's system with 6 axioms is structurally similar to the Theory of Liberty. "
            "The key differences: (1) Locke's last-round mechanism is weaker (God-as-workmanship does not "
            "provide the game-theoretic unknown terminal that Resurrection does); "
            "(2) Locke's theological axioms are more specific (require creator concept, not just negative definition). "
            "Lockean system is the closest theological competitor but scores slightly lower on C5 and C7. "
            "VERDICT: Partial counterexample. Does not demonstrate that the Theory of Liberty is uniquely necessary, "
            "but also does not pass all criteria as well."
        ),
        "strength": "STRONG_THEOLOGICAL_COMPETITOR",
    },
    {
        "id": "CE-003",
        "name": "Minimal Secular CFS: {FW, self-ownership, NAP, unknown-horizon-posit}",
        "description": (
            "Construct the absolute minimum secular system: "
            "(1) Free will exists (self-refutation argument). "
            "(2) Persons own themselves. "
            "(3) No aggression (NAP). "
            "(4) The terminal period of social interaction is unknowable (secular unknown-horizon posit). "
            "This is the minimum 4-axiom system that satisfies all required properties."
        ),
        "axiom_count": 4,
        "theological_axioms": 0,
        "criteria_analysis": {
            "C1": "PASS",
            "C2": "PASS",
            "C3": "PASS — self-ownership → liberty",
            "C4": "PASS — self-ownership is pre-political",
            "C5": "PARTIAL-to-PASS — unknown-horizon posit directly solves last-round. But it is a POSIT (asserted axiom), not derived from anything. The Theory of Liberty DERIVES the unknown horizon from Resurrection (which is itself grounded in Tawhid and Prophethood). The posit is weaker than the derivation.",
            "C6": "PASS — NAP prohibits state",
            "C7": "PASS — secular",
            "C8": "PARTIAL",
            "C9": "PARTIAL",
            "C10": "PASS",
        },
        "verdict": "PARTIAL_COUNTEREXAMPLE",
        "analysis": (
            "This 4-axiom system is the MINIMUM COUNTEREXAMPLE — the smallest possible system satisfying most criteria. "
            "Its critical vulnerability: Axiom (4) (unknown-horizon posit) is ASSERTED without derivation. "
            "The Theory of Liberty DERIVES the unknown horizon from theological axioms (Resurrection → afterlife → infinite horizon). "
            "Formally: CE-003 has an asserted axiom where ToL has a derived theorem. "
            "The CE-003 solution is logically valid but axiomatically more burdensome in one sense "
            "(requires a specific additional axiom with no derivation) and less burdensome in another "
            "(no theological axioms). "
            "This is the most important counterexample: it demonstrates that the STRUCTURE of the "
            "last-round solution can be replicated secularly, but only by adding an explicit axiom. "
            "VERDICT: Genuine partial counterexample. The secular unknown-horizon posit is a valid "
            "structural analogue to Resurrection. It creates a secular CFS with the same structural "
            "properties as the Theory of Liberty's theological CFS."
        ),
        "strength": "MINIMUM_GENUINE_COUNTEREXAMPLE",
    },
    {
        "id": "CE-004",
        "name": "Kantian Ethics + Virtue Ethics Hybrid",
        "description": (
            "Augment Kantian ethics with virtue ethics: add an axiom that agents internalize moral law as "
            "character (Aristotelian habit). This replaces the last-round problem: virtuous agents comply "
            "with duty not for strategic reasons but for character reasons."
        ),
        "axiom_count": 6,
        "theological_axioms": 0,
        "criteria_analysis": {
            "C5": "PARTIAL — virtue internalization is a psychological/sociological claim, not a game-theoretic structural solution. Depends on prior character formation which itself faces collective action problems.",
            "C4": "PARTIAL — Kantian property rights are derivable but not as pre-political as Lockean/Rothbardian.",
        },
        "verdict": "WEAK_COUNTEREXAMPLE",
        "analysis": (
            "The virtue ethics addition does not resolve the last-round problem structurally. "
            "A virtuous agent in the last period still faces the question: why comply? "
            "Character virtue says 'because that is who I am' but this is a psychological claim "
            "that requires prior character formation — which itself faces the last-round problem "
            "in the educational/cultural context. "
            "VERDICT: Weak counterexample. Virtue addition does not provide structural stability."
        ),
        "strength": "WEAK",
    },
]

counterexample_verdict = (
    "PARTIAL COUNTEREXAMPLE FOUND: CE-003 (4-axiom secular system with unknown-horizon posit) "
    "is a genuine partial counterexample. It demonstrates that the STRUCTURE of the Theory of Liberty "
    "can be replicated without theological axioms by substituting an explicit secular unknown-horizon axiom. "
    "HOWEVER: CE-003 does not fully defeat the Theory of Liberty's uniqueness claim because: "
    "(1) CE-003 adds an axiom that the Theory of Liberty derives — the ToL is structurally more economical; "
    "(2) The unknown-horizon posit in CE-003 is naked (no derivation), while Resurrection is embedded in a "
    "broader theological system that provides additional derivations; "
    "(3) CE-003 has weaker C8 (accountability) and C9 (AI alignment) than the ToL. "
    "CONCLUSION: The Theory of Liberty is NOT uniquely necessary. CE-003 demonstrates a structural "
    "analogue. The uniqueness claim must be downgraded from 'the only CFS' to 'the only derived CFS' "
    "or 'the most complete CFS' based on this counterexample."
)

save("76_counterexamples.json", {
    "total_counterexamples_tested": len(COUNTEREXAMPLES),
    "genuine_partial_counterexamples": ["CE-001", "CE-003"],
    "strong_theological_competitors": ["CE-002"],
    "weak_counterexamples": ["CE-004"],
    "strongest_counterexample": "CE-003",
    "counterexamples": COUNTEREXAMPLES,
    "overall_verdict": counterexample_verdict,
    "uniqueness_status_after_search": (
        "WEAKENED BUT NOT DISPROVEN. "
        "The Theory of Liberty demonstrates a CFS for liberty with superior properties on C5 "
        "(absolute vs. conditional last-round stability) compared to all secular competitors. "
        "CE-003 demonstrates that the structure can be replicated with an additional secular axiom. "
        "The uniqueness claim is weakened from 'ONLY CFS' to 'ONLY DERIVED CFS WITH ABSOLUTE C5 SOLUTION.'"
    ),
})

# ════════════════════════════════════════════════════════════════════════════
# STEP 7 — THEOLOGICAL NECESSITY AUDIT
# ════════════════════════════════════════════════════════════════════════════
print("Step 7: Theological necessity audit...", flush=True)

THEO_AUDIT = {
    "question": "Can liberty be grounded without Tawhid, Resurrection, and Prophethood?",
    "method": "For each theological axiom: find the strongest secular functional equivalent; evaluate whether it provides identical structural coverage.",
    "axioms_tested": [
        {
            "axiom_id": "A-000004",
            "axiom": "Tawhid: no servitude to anything other than God.",
            "function_in_theory": "Provides the unique single-principle anti-servitude axiom that is agreement-admissible and makes all human servitude impermissible.",
            "secular_functional_equivalents": [
                {
                    "name": "Non-Aggression Principle (NAP)",
                    "adequacy": "PARTIAL",
                    "gap": (
                        "NAP prohibits AGGRESSION but not all servitude. Consensual servitude (voluntary slavery) "
                        "is not prohibited by NAP alone. Tawhid prohibits ALL servitude including consensual. "
                        "NAP cannot derive the absolute prohibition on voluntary slavery that Tawhid provides."
                    ),
                },
                {
                    "name": "Kantian Formula of Humanity (treat persons always as ends)",
                    "adequacy": "PARTIAL",
                    "gap": (
                        "Formula of Humanity prohibits using persons as MERE means, not as any means. "
                        "Kant permits contractual arrangements where persons are means-among-other-purposes. "
                        "The absolute prohibition on servitude requires a stronger axiom."
                    ),
                },
                {
                    "name": "Self-ownership Axiom (Rothbard)",
                    "adequacy": "PARTIAL",
                    "gap": (
                        "Self-ownership prohibits non-consensual servitude. "
                        "It does not prohibit consensual self-enslavement. "
                        "Rothbard himself struggled with voluntary slavery contracts. "
                        "Tawhid provides an absolute prohibition regardless of consent."
                    ),
                },
            ],
            "necessity_verdict": "NOT_LOGICALLY_NECESSARY",
            "reasoning": (
                "Tawhid's function can be partially replicated by secular axioms. "
                "HOWEVER: no single secular axiom provides ALL of Tawhid's structural functions simultaneously: "
                "(a) absolute prohibition on all servitude (including consensual), "
                "(b) agreement-admissibility without prior religious commitment, "
                "(c) derivation of anti-statism from an anti-servitude principle, "
                "(d) grounding of accountability without state enforcement. "
                "Secular alternatives require 2-3 axioms to cover what Tawhid covers with 1. "
                "CONCLUSION: Not logically necessary, but functionally most parsimonious."
            ),
        },
        {
            "axiom_id": "A-000006",
            "axiom": "Resurrection exists; it stabilizes liberty by making the terminal period unknowable.",
            "function_in_theory": "Solves the last-round problem: unknown terminal prevents backward induction in finitely-repeated social games.",
            "secular_functional_equivalents": [
                {
                    "name": "Unknown-Horizon Posit (secular)",
                    "adequacy": "FUNCTIONAL_EQUIVALENT",
                    "gap": (
                        "The secular unknown-horizon posit (CE-003, Axiom 4) provides the SAME structural "
                        "game-theoretic function. It is axiomatically asserted, not derived from a broader "
                        "theological system. This is a genuine functional equivalent. "
                        "The Theory of Liberty derives unknown-horizon from Resurrection; "
                        "CE-003 asserts it directly. Both solve the last-round problem structurally."
                    ),
                },
                {
                    "name": "Infinite Discount Factor (δ→1)",
                    "adequacy": "CONDITIONAL",
                    "gap": "Requires empirical condition δ→1. Conditional, not structural.",
                },
            ],
            "necessity_verdict": "NOT_LOGICALLY_NECESSARY",
            "reasoning": (
                "The unknown-horizon posit can be asserted secularly without Resurrection. "
                "CE-003 demonstrates this. The function of Resurrection is logically replicable. "
                "HOWEVER: within the Theory of Liberty's own framework, Resurrection is NOT merely "
                "a functional posit — it is derived from Tawhid + Prophethood and embedded in a "
                "theological system that provides additional structure. The secular posit is a "
                "bare axiom with no further derivations; Resurrection is a derived theorem with "
                "rich structural implications (moral accountability, personal identity, justice). "
                "CONCLUSION: The STRUCTURAL FUNCTION is replicable; the full semantic content is not."
            ),
        },
        {
            "axiom_id": "A-000007",
            "axiom": "Prophethood is real; it provides authenticated specification of the formal system.",
            "function_in_theory": "Anti-fraud function: distinguishes authentic religion (CFS for liberty) from false religion (CFS for tyranny). Prevents any human from claiming absolute authority.",
            "secular_functional_equivalents": [
                {
                    "name": "Open-Source / Transparent Specification",
                    "adequacy": "PARTIAL",
                    "gap": (
                        "Transparency ensures the specification can be audited but does not "
                        "prevent authoritative interpreters from claiming exclusive competence. "
                        "The anti-fraud function is weaker."
                    ),
                },
                {
                    "name": "Constitutional Entrenchment",
                    "adequacy": "PARTIAL",
                    "gap": (
                        "Constitutional documents can be interpreted divergently. "
                        "The Theory of Liberty argues that constitutional democracies fail precisely "
                        "because interpreters claim authority. Prophethood's seal (khatam) prevents "
                        "any further claimant — a unique structural feature."
                    ),
                },
            ],
            "necessity_verdict": "NOT_LOGICALLY_NECESSARY_BUT_UNIQUELY_ELEGANT",
            "reasoning": (
                "The anti-fraud function can be approximated by secular mechanisms. "
                "However, no secular mechanism provides the 'seal' property: the finality of Prophetic "
                "specification that prevents all future authoritative amendment. "
                "Constitutional documents require constitutional courts; open-source requires technical "
                "auditors. Both re-introduce expert authority. The khatam argument — once revealed, "
                "the specification is closed and no human authority can supersede it — is structurally "
                "unique to the Prophetic framework. "
                "CONCLUSION: The anti-fraud function is partially replicable; the khatam property is not."
            ),
        },
    ],
    "summary": {
        "tawhid_logically_necessary": False,
        "resurrection_logically_necessary": False,
        "prophethood_logically_necessary": False,
        "theological_axioms_provide_unique_structural_value": True,
        "secular_cfs_possible": True,
        "secular_cfs_equally_parsimonious": False,
        "secular_cfs_provides_identical_coverage": False,
    },
    "final_theological_verdict": (
        "NO theological axiom is logically necessary for grounding liberty. "
        "Secular functional equivalents exist for all three theological axioms. "
        "HOWEVER: no secular system provides the combination of (a) parsimony (all three functions "
        "in fewer axioms), (b) absolute prohibition on servitude, (c) structural last-round stability "
        "without conditional empirical requirements, and (d) the khatam anti-fraud property. "
        "The theological axioms are PRAGMATICALLY SUPERIOR within the theory's own criteria "
        "but not LOGICALLY NECESSARY for grounding liberty per se. "
        "This is the critical distinction: The theory demonstrates that theology provides "
        "the most elegant and parsimonious solution to the formal requirements of liberty, "
        "not that it is the only possible solution."
    ),
}

save("77_theological_necessity_audit.json", THEO_AUDIT)
print("Steps 4-7 complete.", flush=True)
