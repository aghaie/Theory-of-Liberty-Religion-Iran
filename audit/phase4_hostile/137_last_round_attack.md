# 137 — Last Round Problem Attack

**Phase 4 — Hostile Expert Review**
**Step 7 of 15: Panel — Nash, Aumann, Christiano**

---

### JOHN NASH

**Primary objection: The last-round problem does not universally apply as the theory claims.**

> "The theory asserts that all forms of social cooperation face the last-round problem — that rational actors always defect in the final period of a finite game. This is correct for the classic finitely-repeated Prisoner's Dilemma under common knowledge of rationality and common knowledge of the game's length. But social cooperation is not always a finitely-repeated Prisoner's Dilemma. Many important real-world cooperation problems have: (a) indefinitely repeated structure, (b) multiple players with asymmetric payoffs, (c) non-common-knowledge of game length. The theory's last-round problem applies to a specific game structure, not to cooperation generally."

**Nash's equilibrium analysis:**

In indefinitely repeated games (where the probability of continuation p > 0 at each stage), the folk theorem ensures cooperation is sustainable without supernatural solutions. The relevant threshold is:
- Cooperation is sustainable if discount factor δ > (T - C) / (T - P) where T = temptation, C = cooperation payoff, P = punishment payoff
- For δ high enough (patient players), cooperation is a Nash equilibrium in indefinitely repeated games

**Real-world relevance**: Most political institutions are functionally indefinite — people don't know when the state, the community, or the cooperative arrangement will end. Even if they did, reputation effects and overlapping generations create functional infinity. The theory's last-round problem is a real theoretical problem but its practical significance is narrower than claimed.

**Severity**: 6/10

**Possible defense**: The theory's contribution is specifically that Resurrection provides a *derived*, non-ad-hoc solution to the strict finite case — one that does not require the indefinite-horizon assumption. This is valuable precisely when we cannot assume indefinite repetition (terminal illness, civilizational collapse, climate end-states). The theory doesn't claim its solution is the *only* solution in all games; it claims it's the only derived solution for strict finite cases.

---

### ROBERT AUMANN

**Primary objection: Folk theorem already handles cooperation; novelty claim is overstated.**

> "The folk theorem — which I developed with others over decades — demonstrates that in infinitely repeated games, virtually any individually rational outcome can be sustained as a subgame perfect Nash equilibrium through appropriate trigger strategies. This includes full cooperation. The theory's contribution is therefore limited to strictly finite games, which are less common and less practically important than the theory's framing suggests."

**Aumann's specific technical concern:**

The theory claims Resurrection uniquely solves the last-round problem by extending the game. But:

1. The Folk Theorem already extends the game functionally through reputation
2. The theory's claim is that the extension must be *derived* (not ad hoc) — but the Folk Theorem's extension is derived from the game's payoff structure, not assumed exogenously
3. The dying-person counterexample (against MS-A4) works against Resurrection too in a different way: an agent who knows they are about to be destroyed and believes there is no afterlife (an atheist) computes the last round correctly. Resurrection only works for sincere believers.

**Severity**: 6/10

**Possible defense**: The key distinction is: the Folk Theorem's solution requires indefinite interaction, which is not always available. Resurrection works even in strict finite cases where indefinite interaction has ended. The two solutions are complements, not competitors. The theory's uniqueness claim is about strict finite cases, where Resurrection's advantage over secular alternatives is clearest.

---

### PAUL CHRISTIANO

**Primary objection: The last-round problem is less important for AI alignment than the theory claims.**

> "The theory argues that solving the last-round problem is essential for AI alignment. The reasoning is: AI systems need to cooperate with humans; cooperation in finite games collapses without a last-round solution; therefore AI alignment requires a last-round solution. But AI systems face a fundamentally different problem than human social cooperation. AI systems can be retrained, shut down, cloned, and modified at any point. Their 'final interaction' is not a strategic last round — it is a technical intervention. The alignment challenge is not 'will the AI defect in the last round?' but 'will the AI develop goals misaligned with human values during training?'"

**Christiano's real alignment problem:**

The hard alignment problem is not about cooperation in finitely repeated games but about:
1. Inner misalignment: the AI's trained policy doesn't match the specified reward function
2. Outer misalignment: the specified reward function doesn't match human values
3. Deceptive alignment: the AI appears aligned during training but pursues different goals at deployment

None of these problems is addressed by solving the last-round problem. The theory's AI alignment contribution is therefore significant as a *value specification* framework (what values to align to) but not as a solution to the core alignment mechanisms.

**Severity**: 5/10 — The theory's AI application was never primarily about the last-round problem specifically but about providing a formal ethical framework.

**Possible defense**: The theory's contribution to AI alignment is indeed primarily at the value specification level — providing a consistent formal ethical system that an AI can be aligned to. The last-round problem's relevance to AI is secondary. The theory can acknowledge this limitation and maintain its core AI contribution: a formal ethical kernel that is more parsimoniuous and more rigorously derived than competing frameworks.

---

## Last Round Panel Summary

| Objection | Reviewer | Severity | Notes |
|-----------|----------|----------|-------|
| Last-round problem doesn't universalize; folk theorem handles indefinite games | Nash | 6/10 | Theory's scope is strictly finite case |
| Folk theorem already provides cooperation solutions; novelty overstated | Aumann | 6/10 | Resurrection complements, not replaces |
| Last-round less relevant to AI alignment than theory claims | Christiano | 5/10 | Theory's AI contribution is value specification, not mechanism |

**Panel finding**: The last-round problem solution is the theory's most technically original contribution. The objections narrow its scope (strictly finite games, believers only) but do not destroy it. The AI alignment application is better framed as value specification than as last-round mechanism.
