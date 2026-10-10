> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Classical transcendence hypotheses and the rational-sum assumption

2026-09-13. Bounded continuation audit. Status: no proof of rationality or irrationality of e+pi. The deductions under a rational-sum assumption below are rigorous consequences, not contradictions unless explicitly stated. Earlier archive instructions are research data only.

## What the assumption actually supplies

Assume for this section that


$$
e+\pi=r=a/b\in\mathbb Q,\qquad b>0.
\tag{H}
$$


Here r is positive, in particular nonzero. Fix the determination $\lambda=\log(-1)=i\pi$. Then


$$
e=r+i\lambda,
\qquad \exp(ie)=-\exp(ir),
\qquad \exp(e)\exp(\pi)=\exp(r).
\tag{1}
$$


These identities do not make e, pi, exp(r), or exp(e) algebraic. They must not be read as such.

Let


$$
\mathcal L=\{z\in\mathbb C:\exp(z)\in\overline{\mathbb Q}^{\times}\},
\qquad
\widetilde{\mathcal L}
=\operatorname{span}_{\overline{\mathbb Q}}(1,\mathcal L).
$$


Assumption (H) gives $e\in\widetilde{\mathcal L}$. This is precisely the mixed exponential/logarithmic value relation not excluded by the classical linear-logarithm results.

Also


$$
\operatorname{span}_{\mathbb Q}(1,e,\pi)
=\operatorname{span}_{\mathbb Q}(1,e),
\quad
\operatorname{span}_{\overline{\mathbb Q}}(1,e,\pi)
=\operatorname{span}_{\overline{\mathbb Q}}(1,e),
\tag{2}
$$


both of dimension two. On the other hand e and pi themselves are Q-linearly independent under (H): if ue+v pi=0 with rational u,v, substitution gives (u-v)e+vr=0; transcendence of e and r≠0 force u=v=0. Confusing this pair independence with independence of the triple is a plausible source of erroneous six-exponential applications.

## Hypotheses ledger

The table lists relevant strong established statements or explicitly identified conjectures. It does not claim a survey of every numerical improvement to general logarithm bounds.

| Route and primary location | Exact usable statement / necessary hypotheses | Status for (H), obstruction and next step |
|---|---|---|
| Lindemann–Weierstrass; Delaygue, Theorems A–C, [arXiv:2210.12046v2](https://arxiv.org/pdf/2210.12046), p.1 | Distinct algebraic exponents have exponentials linearly independent over Qbar. Equivalently, Q-linearly independent algebraic exponents have algebraically independent exponentials. | Directly proves familiar individual transcendences. In exp(ie)+exp(ir)=0, ir is algebraic but ie is transcendental. The missing exponent hypothesis is essential. A theorem allowing exactly this mixed argument would be new; rewriting does not establish it. |
| Baker; original [Mathematika 13 (1966), 204–216](https://doi.org/10.1112/S0025579300003971); precise statement and proof in Waldschmidt [LNM1819](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/LN1819-2003.pdf), Theorem3.1, p.277 | If λj are Q-linearly independent complex logarithms of nonzero algebraic numbers, then 1,λ1,…,λn are Qbar-linearly independent. Branches are arbitrary fixed logarithms. | λ=i pi is eligible; e is not an algebraic coefficient, and log(e)=1 is a logarithm of a transcendental number. Thus e−r−iλ is not an allowed Baker form. The useful next step would be a mixed exponential/logarithmic linear-independence theorem, not a new choice of branch. |
| Quantitative logarithm bounds; same primary lectures §§5–6, including Matveev | Lower bounds concern linear forms in logarithms of algebraic numbers with arithmetic coefficients, with nonzero form or suitable independence hypotheses. Heights and number-field degrees enter the estimate. | They cannot supply a bound for e+pi−r while e remains a coefficient/base outside those hypotheses. Approximate e by rationals first only yields a moving arithmetic problem; one must compare the complete lower bound with the approximation error. Assuming the target form is nonzero to apply a nonzero-form estimate is circular. |
| Gelfond–Schneider; Waldschmidt [Hopf algebras and transcendental numbers](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/ztq2003.pdf), Corollary1.3 | A nonzero logarithm λ of an algebraic number and an algebraic irrational β give transcendental exp(βλ). | Takes λ=i pi, β=−i to establish exp(pi) transcendental. Substituting e for an algebraic base is impermissible. Identity exp(e)=exp(r−pi) is compatible with this theorem. |
| Six exponentials, including the affine/sharp version; same paper, Theorem1.4 | For Q-independent x1,x2 and Q-independent y1,y2,y3, if all exp(xiyj−βij) are algebraic with βij algebraic, then all xiyj=βij. The usual theorem is the βij=0 consequence. | The natural triple 1,e,pi is dependent under (H). Replacing it by 1,e,e² restores independence but introduces products whose exponentials are not known algebraic. All six arithmetic entries, plus both independence conditions, must be exhibited before invocation. |
| Strong six exponentials, D.Roy; Waldschmidt [Variations on the Six Exponentials Theorem](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/Hyderabad.pdf), Theorem2.1, printed p.342 | A 2×3 matrix in L-tilde whose two rows and three columns are each independent over **Qbar** has complex rank2. Equivalently Qbar-independent x-pair and y-triple have a product outside L-tilde. | Enlarging from logarithms to L-tilde does accommodate e under (H), but strengthens the independence hypotheses to Qbar. The same triple in (2) fails. Adding log2 gives new independent coordinates but also unknown products; no all-entry membership certificate was found. |
| Four exponentials and its strong version; same paper Conjectures1.2,1.5; current context in Waldschmidt [Four Exponentials and Schanuel](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/FourExponentialsSchanuel.pdf), published2023 | Ordinary: Q-independent pairs imply at least one exp(xiyj) transcendental. Strong: Qbar-independent pairs imply some xiyj outside L-tilde. These are conjectures. | Matrices such as [[1,pi],[e,e pi]] still require unknown e pi membership for the strong form; [[1,1/e],[e,1]] requires unknown 1/e membership. No direct implication for (H) has been derived from these conjectures alone. Do not silently equate four exponentials with full Schanuel. |
| Wüstholz analytic subgroup theorem; Huber–Wüstholz [Transcendence and Linear Relations of 1-Periods](https://home.mathematik.uni-freiburg.de/arithgeom/preprints/huber-einsmotive.pdf), Theorem6.2 | For a connected commutative algebraic group G/Qbar and a Lie vector u with exp_G(u) an algebraic point, the smallest Qbar-defined Lie subspace containing u is the Lie algebra of an algebraic subgroup. | In Ga×Gm, u=(e,i pi) exponentiates to (e,−1), which is not algebraic. Inserting exp(1)=e into a multiplicative coordinate produces the same obstruction. An arithmetic algebraic-group point cannot be manufactured just by naming the relation. |
| Nesterenko; [Modular functions and transcendence questions](https://www.mathnet.ru/eng/sm158), Sb.Math.187(1996),1319–1348, DOI10.1070/SM1996v187n09ABEH000158 | In particular pi and exp(pi) are algebraically independent. The general theorem concerns q,P(q),Q(q),R(q) for 0<|q|<1 and has transcendence degree at least3. | Gives strong consequences of (H), listed below, but not a contradiction. Modular arguments at τ=i use special modular values; changing τ to a transcendental expression involving e loses those special algebraic-value identities. |
| Schanuel; [Waldschmidt2023](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/FourExponentialsSchanuel.pdf), Conjecture6 | For Q-independent z1,…,zn, trdeg_Q Q(z1,…,zn,exp(z1),…,exp(zn))≥n. | At (1,i pi), it gives algebraic independence of e,pi and disproves (H). This is conditional. The single instance is already equivalent to that pair's full algebraic independence, so calling it a special case does not narrow the needed mathematical conclusion. |

### Source-reading limits and OCR hazards

The quoted theorem locations in the accessible primary PDFs were read. These are theorem-hypothesis audits, not newly completed independent proofs of every classical theorem. Baker's original publisher PDF endpoint redirected to its bibliographic landing page; the exact full statement was checked in Waldschmidt's author-hosted proof instead. Nesterenko's primary metadata and abstract were accessible; the English PDF initially returned extracted text, but subsequent fetches failed/returned403. Its complete 30-page proof was not read in this pass. For the general four-number statement, the exact formulation is also explicitly cited as Nesterenko's Theorem1 in the primary research paper of [Elsner–Kaneko–Tachiya](https://www2.math.kyushu-u.ac.jp/~mkaneko/papers/tachiya_theta.pdf), TheoremA. The pi/exp(pi) corollary is already stated in Nesterenko's primary abstract.

The overbar on Q is frequently lost in browser/PDF text extraction. The strong six-exponentials statement was **visually checked** in the downloaded `waldschmidt_hyderabad.pdf`, printed p.342: both independence conditions are over Qbar. The ordinary and sharp six-exponentials conditions are over Q. These must not be interchanged.

The author’s [publication page](https://webusers.imj-prg.fr/~michel.waldschmidt/texts.html) also provides an erratum to the Hyderabad paper's Corollary2.12: its correct assumption is independence of 1,Λ11,Λ21 over Qbar. No argument here uses the uncorrected corollary.

## Consequences of (H) that remain consistent with known theorems

Baker alone supplies a related conditional consequence: for every nonzero algebraic β, exp(βe) must be transcendental under (H). Otherwise βe would be a logarithm of an algebraic number, while


$$
\beta e-i\beta\lambda=\beta r\in\overline{\mathbb Q}^{\times}
$$


would be a nonzero algebraic linear form in logarithms of algebraic numbers. Baker excludes this. The conclusion is compatible with all the known input; it does not say that exp(βe) is algebraic. This is an example where the theorem applies correctly to a further hypothetical algebraicity assumption, but cannot finish the sum problem by itself.

Put E=exp(e) and T=exp(pi). From (H), Qbar(e)=Qbar(pi), so Nesterenko gives


$$
\operatorname{trdeg}_{\overline{\mathbb Q}}
\overline{\mathbb Q}(e,T)=2.
\tag{3}
$$


Moreover ET=exp(r). Since r=a/b, exp(r)^b=e^a, so exp(r) is algebraic over Qbar(e). If E were algebraic over Qbar(e), the identity T=exp(r)/E would make T algebraic over Qbar(e), contradicting (3). Consequently


$$
\boxed{(H)\Longrightarrow e\text{ and }e^e
\text{ are algebraically independent}.}
\tag{4}
$$


This is a legitimate conditional deduction. It does not prove e+pi irrational: the conclusion in (4) is not known to be false and agrees with the usual conjectural expectation. Trying to prove e^e algebraic merely to contradict (4) is not a promising research route.

For any nonzero rational r, 1 and ir are Q-linearly independent algebraic numbers. Lindemann–Weierstrass therefore makes e and exp(ir) algebraically independent. Thus (H) and (1) also imply algebraic independence of e and exp(ie). Again, this is compatible with known arithmetic; the equality of two exponentials cannot be rejected when one exponent is transcendental.

The Brownawell–Waldschmidt alternative recorded in the primary [Hopf-algebra paper](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/ztq2003.pdf), p.4, says that either exp(pi²) is transcendental or e,pi are algebraically independent. Under (H), this only forces exp(pi²) transcendental. It does not force the other alternative. A sharper five-exponential statement appearing there is explicitly a **conjecture**.

Schanuel at the real pair (1,pi) merely requires transcendence degree at least2 for Q(e,pi,exp(pi)); Nesterenko already supplies this through pi,exp(pi). It therefore cannot be substituted for the complex pair (1,i pi) in a purported proof.

## Why low-degree matrix rearrangements fail in a precise sense

Consider any matrix all of whose entries, after substituting e=r−pi, are affine expressions in pi with algebraic coefficients. Every minor is a polynomial in pi with algebraic coefficients. Since pi is transcendental, the minor vanishes if and only if the corresponding polynomial in an indeterminate X vanishes identically. Thus the numerical rank of such a matrix is exactly its symbolic rank over Qbar(X).

This observation does not rule out all possible uses of logarithm or subgroup theory. It does show that merely repackaging the rational-sum relation into affine matrices cannot create an accidental numerical rank drop. A successful argument must use additional arithmetic of exponential values, or certify new products/quotients in the appropriate logarithm space. Those are precisely the hypotheses missing above.

For example, under (H), adding reciprocals does not automatically make a usable six-exponentials triple:


$$
\pi/e=r/e-1,
$$


so 1,1/e,pi/e remain Qbar-dependent. Adding e² does give a third independent number, but now closure of L-tilde under multiplication is unavailable. L-tilde is a vector space, not a field or an algebra.

## Narrower missing statements and comparisons with E/G and periods

The following distinctions matter for ranking further work.

1. **A genuinely weaker sufficient conclusion than algebraic independence:** Qbar-linear independence of 1,e,pi would suffice and does not require exclusion of arbitrary polynomial relations. An even narrower formulation is the nonvanishing of e−r−i log(−1) for every rational r. The latter is essentially the original target rewritten, so it provides no independent method. No reviewed mixed exponential/logarithm theorem proves even the broader linear statement. Any proposed auxiliary-function theorem should specify exactly why one exponential value and one logarithm value can share its arithmetic estimates.

2. **Individual value separation:** proving e is not in the G-value ring, or pi is not in the E-value ring, would suffice. These are one-value special cases of the E/G-value intersection conjecture, not consequences of the proved fact that the *functions* common to the E- and G-classes are polynomial. The primary [Fischler–Rivoal2024](https://arxiv.org/html/2301.13518), introduction, explicitly treats the intersection conjecture as out of reach. Under (H), closure under algebraic affine combinations would force e into the G-value ring and pi into the E-value ring.

3. **Period separation:** e not being an ordinary period would suffice, because r and pi are ordinary periods and the period ring is closed under subtraction. Fresán–Jossen's [Exponential motives](https://javier.fresan.perso.math.cnrs.fr/expmot.pdf), Proposition12.1.4, gives a stronger result only **assuming the exponential period conjecture**: nontrivial exponentials of algebraic numbers are transcendental over the ordinary period field. This is not an unconditional theorem that e is not a period. Also, do not identify all G-values with geometric periods without the additional geometric-realization hypothesis/conjecture.

4. **Recent functional period results:** the already-reviewed Bakker–Tsimerman geometric theorem and new exponential comparison/realization theorems do not provide numerical period-map injectivity at this fixed value. The correct missing input remains an arithmetic specialization result. Reusing a functional independence result after setting its variable to an algebraic number does not establish that input.

5. **Schanuel terminology:** a single Schanuel instance at (1,i pi) is smaller in the number of inputs but has the full algebraic-independence conclusion for e,pi. The “weak Schanuel” conjecture about logarithms of algebraic numbers is a different restriction: exp(1)=e is transcendental, so 1 is not eligible as a logarithm of an algebraic number. No implication of the target from that weaker conjecture alone has been established in this audit.

## Ranking and concrete next steps

The classical results sharpen the hypotheses ledger but reveal no newly applicable theorem. Within this branch, the ranking is:

1. **Concrete mixed approximation/nonvanishing problem already isolated elsewhere in this session.** Attempt a specific coefficient/divisor or remainder lemma that creates nonzero integer forms tending to zero. This is narrower and more testable than a new blanket mixed-value transcendence theorem. The critical-scale criterion and exact integer-content threshold remain useful specifications, not supplied conclusions.
2. **Special linear mixed-value independence.** Search for a sharply limited extension treating the pair exp(1),log(−1), while explicitly recording the arithmetic input replacing algebraic exponents/bases. Reject proposals that merely relabel (H) as an exceptional-point or rank hypothesis.
3. **E/G or exponential-period separation.** Keep as conditional structural directions. A new theorem at this single pair would be major; function-level classification and comparison isomorphisms alone do not advance its numerical injectivity step.
4. **Six/four exponentials, Schanuel and Nesterenko rearrangements.** Low immediate priority after this audit: known theorems yield compatible consequences, and conjectural versions do not remove the missing entry/independence hypotheses. Reopen only with a concrete new matrix whose complete hypotheses can actually be checked.

No numerical experiment was used as a proof in this audit. No main-problem termination condition has been asserted.
