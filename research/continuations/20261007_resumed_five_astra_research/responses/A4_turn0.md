> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of A1turn22, A2turn16, A3turn15 and A5turn14

## 1. Executive assessment

None of the four reports proves that $e+\pi$ is rational or irrational. Their stated global reservations are justified.

The strongest independently checkable advances are:

- **A1:** the algebra reducing the next nonlinear cancellation to a short LOW source, one HIGH feedback observation and one actual inverse-boundary observation is sound. However, the original-domain hypotheses needed for that reduction are not all proved in the supplied material. In particular, the claimed original-family theorem
  

$$
\mathcal Q\in3^5M
$$


  must remain **conditional in this audit**, rather than independently certified.
- **A2:** the exceptional shifted kernel, its low unit $22$, and its square-sum reduction are consistent and can be checked directly. The exceptional zero follows from the stated branch-reflection theorem. The $58$-entry observable quotient has a sound linear-algebraic proof **provided the two mixed divisibilities in §7 are established for the complete finite responses**. Those divisibilities still invoke unavailable forcing/radical results.
- **A3:** the new finite algebra is substantially sound. The two-step resultant argument, moving-threshold cofactor formula, exterior-content obstruction and joint saturation argument withstand the checks below, subject to their explicitly identified retained primitivity and saturation hypotheses. Neither required growth estimate follows.
- **A5:** the finite inverse profiles and kernel reduction are consistent with finite convolution, including the subtraction of excess convolution terms. The carry construction is formally implementable with the stated exponential-in-precision bound, if its states are interpreted with delayed windows as explained below. Two boundary statements require correction:
  1. its displayed terminal term (5.3) is only the **additional exterior-$+1$** term, not the whole terminal contribution to (5.2);
  2. the large binomial $W_b=\binom{n+2}{b}$ must be excluded from the claim that all data outside the long kernels are short-lower-index coefficient data.

I also obtain a small but unconditional strengthening of A5’s rank obstruction:



$$
\boxed{
\operatorname{rank}_{\mathbb Q}(GJ-J^TG)=b-1
\quad\text{on its original family}.
}
$$



This is maximal possible rank for the odd-dimensional skew-symmetric matrix in question. An exact valuation formula for the particular minor used in its proof is given in §6 below. Neither result gives a binary congruence-rank theorem or evaluates the required forced pairing.

### Audit conventions

- **Accepted:** the displayed argument can be checked from the supplied definitions, or the conclusion is an elementary consequence of explicitly stated hypotheses.
- **Conditional:** the deduction is valid, but a necessary earlier theorem or certificate is not supplied in a form permitting independent verification here.
- **Corrected:** a statement needs qualification or amendment.
- **Unproved:** the report correctly identifies an outstanding obligation.

No computation was executed. The supplied JSON certificate is evidence for the finite polynomial identities it names, not an infinite-family certificate and not a substitute for unavailable arithmetic hypotheses.

---

## 2. Domains and scope retained in this audit

No auxiliary recurrence index is promoted to an approximation index.

| Report | Original approximation domain retained |
|---|---|
| A1 | $j>0,\ j\equiv84645\pmod{531441}$, with the stated $D/H$ window and sufficiently large original members |
| A2 | $b=3^{249005515+574312172u}$, $n=2001b$, $u\equiv2\pmod{29^9}$ |
| A3 | $n=15^r$ or $n=105^r$, $r\ge2$ |
| A5 | $b=9^{18+32u}$, $n=4002b$, $u\ge0$ |

In particular:

- A1’s residual index remains $0\le i<\nu$; its HIGH range ends at $m$.
- A2 and A5 retain contact indices $0\le j<b$ and reconstructed indices $0\le j\le b$.
- A3’s consecutive auxiliary indices are used only for transport identities.
- A1’s functional retains its factorial term and cutoff $2v+1\le4n-3$.
- The physical terminals, both exponential boundary columns, exterior $+1$ terms, and logarithmic forcing $F/(1-z)$ are not removed by this audit.

The cited automatic-congruence and creative-telescoping literature supplies methods at its stated scope. It does not evaluate these complete finite responses. In particular, neither prime-power automaticity nor the existence of a telescoper supplies the paid boundary and primitive-normalization certificates still required here.

---

# 3. Audit of A1turn22

## 3.1 Locality and the completed residues

### What can be checked directly

The arithmetic divisions in §2.1 are correct:


$$
4008/3=1336,\qquad 3477/3=1159,
$$


and


$$
1336\cdot1813\equiv1159\pmod{2187}.
$$


Thus the reported whole coefficient $e_{A+1}\equiv0\pmod{3^7}$, **if it is the actual original-domain coefficient**, gives $c=0$.

The original progression gives the advertised small residue. Indeed,


$$
v_3(j)=4,\qquad v_3(4^j-1)=1+v_3(j)=5,
$$


and


$$
\frac{4^j-1}{3^5}\equiv\frac j{3^4}\equiv1\pmod3.
$$


Consequently


$$
A\equiv3^5\pmod{3^6},
\qquad n=A+2\equiv245\pmod{729}.
$$



The binomial periodicity used for the positive-unit calculation is also valid. For $k\le18$, Vandermonde and


$$
v_3\binom{3^5}{r}\ge5-\lfloor\log_3r\rfloor
$$


give


$$
\binom{x+3^5}{k}\equiv\binom xk\pmod{27}.
$$



The degree-$18$ moment approximation is plausible directly from (3.1): terms $k\ge9$ are killed by $k!$, while


$$
(-2)^r=(1-3)^r
$$


has a degree-$2$ binomial-polynomial approximation modulo $27$. Multiplying this by the degree-$2k$ factor for $k\le8$ yields degree at most $18$.

### Dependencies not independently supplied

The following are necessary and are not fully defined or proved in the attachments:

1. the exact definition of $\gamma_r$ and the finite matrix $\mathsf B_n$;
2. the finite inverse-Pascal identity leading to (3.2);
3. the actual $J_3/J_2$ block decomposition;
4. the exact transformed next-column and $\widehat u$ formulas;
5. the locality theorem for the **350-coordinate signed scalar calculation**.

The modulo-$27$ discussion in §3 is not, by itself, a locality proof for the higher-precision signed scalar receipt. It would be an error to use the $62$-coordinate proof as that missing proof.

The stated radius


$$
18+2+2(18+2)=60
$$


does justify the $62$-coordinate suffix **once** the bandwidth, terminal support and block-inverse assertions are established. It correctly retains the original terminal $J_2$ block rather than replacing it by an infinite continuation.

### Status



$$
\boxed{
c=0,\quad g_0=g_1=g_2=0
}
$$


are accepted as reported finite outputs. Their promotion to the original family is **conditional on the named locality and finite-transform results**. The positive-unit locality argument has considerably more support in the supplied text than the signed-scalar promotion.

No rerun of either completed calculation is warranted.

---

## 3.2 Factorial payments and the second producer jet

The factorial-unit calculations in §3.4 are correct. For example,


$$
\frac{(A+1)!}{(A-3)!}=(A-2)(A-1)A(A+1)
$$


has valuation $5$, and its divided unit is $2\pmod3$. The other two units are $2,1$.

The valuation statements in §5.2 also check at the factorial level:

- at $a=A-7,A-8,A-9$, the product contains $A$, $A-3$, $A-6$, contributing $5+1+1=7$;
- at $a\le A-10$, it also contains $A-9$, contributing two further powers.

However, the additional inverse congruences


$$
v\equiv(z,2z,0)\pmod9,\qquad
h\equiv(z,0,-z_{<N})\pmod3
$$


are unavailable dependencies; $N$ and these vectors are not defined sufficiently in this report to audit their applicability.

Subject to those congruences, the passage to


$$
\mathscr R
\equiv
\kappa(y+1)x^A+
3(y+1)x^{A-6}J(x)\pmod9
$$


is correct. Endpoint divisibility supplies the factor $y+1=x+2$, and coefficient support supplies the factor $x^{A-6}$. The assertion that only $J_6$ depends on the integral lift of $\kappa$ is also correct.

**Status:** the second jet is a valid conditional deduction, not independently established here from the receipts alone.

---

## 3.3 Complete poles and the nonlinear cancellation

### Pole list

The pole enumeration in (7.1) is correct at the stated sufficiently large original indices.

Since


$$
4n-3=4H-4D+5<9H=3^{h+1},
$$


the retained denominators have valuation at most $h$. At the three relevant valuation levels:

- valuation $h$: denominator $3H$;
- valuation $h-1$: denominator $H$;
- valuation $h-2$: denominators
  

$$
H/3,\quad5H/3,\quad7H/3,\quad11H/3.
$$



These give exactly the displayed top, next and four $9$-weighted poles. The factorial term is still present in the exact functional and vanishes at this particular modulus because of $3^h$.

### LOW extraction

The explicit coefficient formula (7.3) has the correct sign. Put


$$
k=6-u-t>0.
$$


Over $\mathbb F_3$,


$$
x^{H-k}=(y^H-1)(y-1)^{-k}.
$$


For the separated coefficient $N_i<H$,


$$
[y^{N_i}]x^{H-k}
=(-1)^{k+1}\binom{N_i+k-1}{k-1},
$$


which is precisely


$$
(-1)^{7-u-t}\binom{N_i+5-u-t}{5-u-t}.
$$



The endpoint observation identity in §8.1 follows from the stated generating-function product, and the six LOW observation values


$$
(1,0,1,2,1,2)
$$


are consistent with Lucas reduction. The displayed $9$-row observation table is consistent with


$$
\sum_{v=0}^{5-t}\binom iv.
$$



### What is still needed for $\mathcal Q\in3^5M$

The decisive assertions are:



$$
[y^m]F_i=0\pmod{27},
$$




$$
(B_1)_d=0\pmod3,
$$


and


$$
\widehat E_{\rm act}^{-1}e_{Y_m}
\equiv4e_{Y_d}-3e_{Y_{d+1}}\pmod9.
$$



The last is explicitly identified as an earlier actual-boundary result. The first invokes an earlier complete-core support theorem. The second also needs the actual LOW/HIGH feedback row to coincide with the remainder observation $r_d$; that row identity is not independently displayed.

These are substantive finite-matrix hypotheses, not cosmetic citations. In particular, a selected-pole calculation without the actual feedback row does not establish $(B_1)_d=0$.

### A direct verification of the contraction implication

The algebraic implication can be stated without any ambiguity about a lift of $K_0$.

Let $E$ and $L$ be the actual integral unit matrices, and suppose


$$
\alpha=3A,\qquad
\widetilde\beta=-\kappa e_m\tau^T+3B.
$$


Assume


$$
e_m^TE^{-1}e_m\in9\mathbb Z_3,\qquad
e_m^TE^{-1}\equiv e_d^T\pmod3,
$$




$$
B_d\equiv0\pmod3,\qquad
A^TL^{-1}A\equiv0\pmod3.
$$


Then


$$
\alpha^TL^{-1}\alpha+
3\widetilde\beta^TE^{-1}\widetilde\beta
\in27M.
$$



Indeed, expansion gives


$$
\begin{aligned}
&9A^TL^{-1}A
+3\kappa^2(e_m^TE^{-1}e_m)\tau\tau^T\\
&\quad
-9\kappa\bigl(\tau e_m^TE^{-1}B+
B^TE^{-1}e_m\tau^T\bigr)
+27B^TE^{-1}B.
\end{aligned}
$$


Each term is divisible by $27$ under the stated hypotheses.

A1’s displayed inverse-column congruence supplies the first two hypotheses. Its support and feedback assertions supply the other two. Homogeneity then supplies the extra factor $9$, giving $\mathcal Q\in3^5M$.

**Verdict:** the assembled contraction is correct. Its original-domain input lemmas remain conditional in this independent audit.

---

## 3.4 The edge-jet multiplier lemma

The multiplier construction is valid, with one lattice condition made explicit:

> The corrected columns must satisfy $F_i=z_i-Wc_i$ with integral $c_i$, so that $[W,F]$ is a unimodular integral basis of the degree-$\le m$ polynomial lattice.

The uncorrected basis $[U,z,Y]$ has one monic polynomial of every degree $0,\ldots,m$. Integral correction by $W$ preserves its integral span.

Under that condition and the stated edge hypotheses,


$$
F_i\equiv0\pmod{x^{27},\,3^{10}},
\qquad
\deg(F_i\bmod3^{10})\le m-9,
$$


the constructed $H_i$ is integral and has degree at most $m$. The congruence


$$
\mathscr RF_i-Q_cH_i\in3^{10}\mathbb Z_3[y]
$$


therefore follows.

The complete functional is integral on this cutoff: its factorial part is integral, and $3^h/(2v+1)\in\mathbb Z_3$ for every retained denominator. Thus the proof uses the whole functional, not an unlicensed pole truncation.

The subsequent orthogonality argument is valid if the complete-core orthogonality and $S_c\in3^{17}M$ hold for this same finite basis.

### Important scope distinction

The two-edge lemma is **sufficient**, not shown necessary. The exact remaining linear obligation is


$$
\Phi_R\in3^{11}M.
$$


The proposed edge conditions are one concrete route to it.

A modulo-$27$ support theorem does not establish these conditions modulo $3^{10}$. No bounded producer calculation can replace the missing uniform core-column proof.

---

## 3.5 A1 ledger and priorities

| Claim | Audit status |
|---|---|
| Arithmetic divisions in the reported scalar receipt | Accepted |
| $n\equiv245\pmod{729}$, factorial units | Accepted |
| $62$-coordinate radius, given stated transform/support facts | Accepted conditionally |
| Original-domain promotion of the $350$-coordinate scalar | Unavailable locality dependency |
| Second producer jet | Conditional on earlier inverse congruences |
| Complete pole list modulo $27$ | Accepted |
| LOW coefficient and endpoint observation identities | Accepted |
| $\mathcal Q\in3^5M$ | Correct contraction; conditional original-domain inputs |
| Edge-jet multiplier implication | Accepted with integral-basis hypothesis explicit |
| Depth-$10$ edge hypotheses | Unproved |
| Relative inverse alignment and distinguished cofactor | Unproved |
| All-prime primitive denominator and whole error | Unproved |

**Priority for A1:** supply the exact finite support/feedback/boundary lemmas used in §7, then prove the depth-$10$ two-edge statement. The unevaluated $\kappa,J_t$ calculation does not address that main bottleneck.

---

# 4. Audit of A2turn16

## 4.1 Exceptional shifted kernel

The shift from $B$ to $B-1$ is essential and correctly performed before reduction. Division by the ordinary kernel’s factor $A+B-J$ would indeed be invalid on the exceptional residue.

The digit-state analysis is consistent:

- digit zero contributes one event;
- for $j_1\ne0$, the low digits plus the retained later forcing give at least four total events;
- for $j_1=0$, exactly one third-digit event occurs for $0\le r\le20$, with the stated two outgoing interfaces.

Thus the support


$$
J=14+29^2r+29^3q,\qquad0\le r\le20
$$


is correct **assuming the retained upper forcing applies to every incoming interface**.

The low unit can be checked directly. Modulo $29$,


$$
7!=23,\quad 9!=3,\quad 13!=5,\quad14!=12,
$$




$$
15!=6,\quad18!=-1,\quad20!=-3,\quad22!=6,\quad28!=-1.
$$


The first factorial fraction in (3.1) is $22$, and the second is $\binom{20}{r}$. Therefore the factor


$$
22\binom{20}{r}
$$


is correct.

The finite upper range is also correct:


$$
14+29^2\cdot20=16834<16848,
$$


so each branch has $0\le q\le C$. At $J=B$, the lower index $B-J-1$ is negative, giving exact zero. This is a genuine cutoff zero, not a physical-terminal substitution.

---

## 4.2 Exceptional square and first-correction product

The half-sums are correct. Lucas and Vandermonde give


$$
\binom{40}{20}\equiv0\pmod{29},
$$


while


$$
\binom{20}{10}^2\equiv9\pmod{29}.
$$


Consequently the two half-sums are $10$ and $19$, and


$$
22^2(10H_{\rm I}+19H_{\rm II})
=26(H_{\rm I}-H_{\rm II}).
$$



Hence the exceptional zero is a valid consequence of the **stated branch-reflection identity**. That identity is not reproved in the attachments and remains a named dependency.

The lifted argument in §5 is also algebraically correct. Writing


$$
\alpha_{\rm I}=26+p a,\qquad
\alpha_{\rm II}=-26+p b,
$$


the asserted conditions


$$
H_{\rm I},H_{\rm II}\in p\mathbb Z_p,\qquad
H_{\rm I}-H_{\rm II}\in p^2\mathbb Z_p
$$


kill the constant part modulo $p^2$, and the stated vanishing of the first moments kills the remaining terms. This requires the prior factorial-strip assertion that the complete low unit has the displayed affine high-index lift.

### A necessary logical qualification

Vanishing of the **unweighted** eight-interface Gram matrix alone does not prove


$$
\sum_{\ell,J}B_\ell(J)E_\ell(J)=0
$$


when $B_\ell,E_\ell$ include $JK(J)$ terms.

One also needs


$$
\sum_JJ^2K(J)^2=0,\qquad
\sum_JJ K(J)K_s(J)=0\pmod p.
$$


The weighted radical invoked later in §12 supplies these if it holds for the relevant weights $J_0^2$ and $J_0$.

This distinction is real: over $\mathbb F_{29}$, the vector $(1,12)$ has zero square sum, but weighting its second coordinate by $1$ and its first by $0$ gives square sum $12^2=-1$.

**Verdict:** the first-correction-product zero is valid using the full weighted-radical theorem, not merely (4.3). That exact dependency should be attached to the claim.

---

## 4.3 The $58$-entry actual-head quotient

The decisive proof obligations are


$$
T_i^TY\in p^9\mathbb Z_p\quad(0\le i\le202),
$$


and


$$
(\mathcal RA^{-1}h^{[0]})^TY\in p^{10}\mathbb Z_p.
$$



The support boxes in §6 are internally consistent:


$$
4841\le5044+v\le5218,\qquad
16384\le16384+\alpha\le16761,
$$


and $377<29^2$. The inequality excluding the lower-index borrow in the leading interface is also numerically correct.

But the mixed divisibilities require more than these boxes. They require:

1. the exact complete source/return normal form;
2. the forcing theorem for every atom in those boxes;
3. the leading $000$-profile assertion;
4. the lifted ordinary-square and weighted/interface radical identities;
5. control of the actual physical terminal.

These are invoked but not fully supplied. In particular, the physical-terminal product must be checked separately from the contact atom decomposition. The later assertion $G_b\in p^2$, together with $T_{i,b}\in p^3$, would provide the required $p^9$ terminal payment.

### The quotient implication itself is rigorous

Suppose the two mixed divisibilities hold and the finite response is integral. Then


$$
f^0-A_q\widehat f
=p\delta h^{[0]}+p^2v+p^7w
$$


with $v$ supported in $0,\ldots,202$ gives


$$
(\mathcal RA^{-1}(f^0-A_q\widehat f))^TY\in p^{11}\mathbb Z_p.
$$


Since


$$
\kappa=\frac{Z_w^TY}{p^{10}}\pmod p,
$$


the claimed quotient follows.

The precision is right: computing both actual columns modulo $p^7$, when they are divisible by $p^4$, determines their product modulo $p^{11}$.

### Head entries

The elementary factorial parts of §8 check:

- for $i<29$,
  

$$
\frac{(n+i)!}{n!}\equiv i!(1+7p\mathsf H_i)\pmod{p^2};
$$


- for $i=29+r$,
  

$$
\frac{(n+i)!}{p\,n!}\equiv-8r!\pmod p;
$$


- multiplying the latter by $26A_q$ gives $24r!A_q$.

The remaining coefficient identities involving $J_i,\xi_i,\zeta_i$ and the actual four-head relation are retained dependencies. Given them, the fixed $58$-entry head is correctly assembled.

Also,


$$
\widehat f=2h^{[0]}+p\,v
$$


with $v$ supported below $58$. The stated $p^4$ divisibility of the short factorial response and $T_i\in p^3$ imply $\widehat Z\in p^4$.

**Verdict:** the actual-head quotient is a correct conditional theorem. It is not yet independently proved from the complete attachments because its mixed-divisibility inputs are not independently available.

---

## 4.4 Source coefficients, finite returns and upper observation

The two-coordinate second-column calculation in §11 checks. Since


$$
n/p\equiv7,\qquad c_{29}/p\equiv22,
$$


the displayed matrix is


$$
I+p
\begin{pmatrix}
9&-14\\
-7&9
\end{pmatrix}\pmod{p^2}.
$$


Applying its inverse to $(1,-1)^T$ gives


$$
(1+6p,\,-1+16p)^T,
$$


as claimed. This is a genuine correction to the uncorrected vector $(1,-1)$.

The coefficient formulas (10.2)–(11.3), however, rely on the exact first-order finite Schur expansion and atom dictionary. Their full verification is not supplied by the two-coordinate calculation. They should remain **derived formulas awaiting the bounded assembly certificate**, not evaluated tables.

Moreover, the observable quotient by itself does not imply equality of every first-correction coefficient. To justify the specific exceptional coefficient identity (10.4), one must use the stated interface/event argument showing that the discarded head directions cannot contribute to that exceptional coefficient. This is stronger than merely showing that their final mixed observation vanishes.

### Second-order remainder

The row-binomial congruence in §12 is valid. For $r<p^2$, Vandermonde shows that only $k=pa$, $1\le a<p$, can contribute at valuation $2$ in


$$
\binom{\ell+p^3J}{r}-\binom\ell r.
$$


After division by $p^2$, those contributions are linear in $J\pmod p$.

The factorial-unit assertion requires the complete balanced strip expansion, including its constant and linear coefficients at their appropriate higher precisions. It is plausible and correctly formulated, but remains an earlier-result dependency.

### Boundary-correct upper formula

The structure of (13.2) is correct:

- the leading square sum requires division by $p^2$;
- the first-order contractions require division by $p$;
- completion of the shorter branch introduces
  

$$
-k_B^2\sum_{\ell=5044}^{D-1}a_\ell g_\ell.
$$



This subtraction cannot be omitted.

For the $U_s$ endpoint corrections to vanish, one needs either $K_s(B)=0$ or $K_s(B)\in p\mathbb Z_p$, in addition to $K(B)\in p\mathbb Z_p$. That condition should be stated with the exact eight interface definitions; ordinary-tail vanishing alone is not the complete argument.

The physical terminal is separately paid if $F_b,G_b\in p^2$. Its influence on the finite contact solve must nevertheless remain.

---

## 4.5 A2 ledger and priorities

| Claim | Audit status |
|---|---|
| Shifted exceptional support and low unit $22$ | Accepted, conditional on upper forcing |
| Exact $J=B$ zero and both cutoff ranges | Accepted |
| Exceptional zero modulo $p$ | Conditional on stated reflection |
| Lifted exceptional zero modulo $p^2$ | Conditional on strip lift and lifted reflection |
| Entire first-correction product zero | Requires full weighted radical, not just unweighted Gram zero |
| $58$-entry quotient implication | Accepted |
| Mixed divisibilities proving that quotient | Unavailable complete-response dependencies |
| Two-coordinate exterior correction | Accepted |
| Full exceptional coefficient dictionaries | Derived; not independently certified |
| Boundary-correct form of (13.2) | Accepted conditionally, with endpoint conditions explicit |
| Actual upper observation and $\kappa$ | Unproved |
| Primitive-depth alignment and all-prime comparison | Unproved |

**Priority for A2:** provide a compact proof package for (7.1)–(7.2), including physical-terminal valuations and the exact weighted-radical statements. Then assemble the single low coefficient row in (13.2). Do not treat the one-dimensional head transition as an evaluation of the remaining upper observation.

---

# 5. Audit of A3turn15

## 5.1 Inverse transfer, two-step defect and resultant

The displayed transfer identities give the inverse (2.1). One can also recover


$$
\det\mathsf U_n=\frac{(n+1)(n+2)^2(n+3)}2.
$$


Thus both forward and inverse transfers are units at primes beyond the stated block threshold.

The supplied certificate reports the exact polynomial checks for all three two-step coordinates. Its scope matches these rational identities. It does not certify the later primitivity or growth assertions.

The resultant mechanism can be checked independently. Set


$$
l(X,Y)=aX+bY,\qquad
g(X,Y)=uX^2+vXY+wY^2,
$$


and


$$
R=b^2u-abv+a^2w.
$$


Then


$$
b^2g-l\bigl((bv-aw)X+bwY\bigr)=RX^2,
$$


and


$$
a^2g-l\bigl(auX+(av-bu)Y\bigr)=RY^2.
$$


Therefore, if $(X,Y)$ is primitive at $p$, the common valuation of $l(X,Y)$ and $g(X,Y)$ is at most $v_p(R)$.

For A3,


$$
G(-NB,A)=-\mathscr R_2(n)
$$


follows from the two displayed simplifications:


$$
mEA-cJNB=K_1,\qquad B_PA-A_PB=K_2.
$$


The positive degree-$11$ polynomial and leading coefficient $8$ are consistent with the certificate.

### Required arithmetic hypotheses

To apply this to the actual reference pair, one still uses:

- primitivity of $(\tau_{n+2},\tau_{n+3})$ at $p>n+4$;
- the actual-unit block-remainder identity relating common alignment to the defect.

Those are exact retained statements, not consequences of the resultant alone.

**Verdict:** the fixed two-step content theorem is valid at its stated scope. It does not bound either endpoint alignment separately.

---

## 5.2 Composition and moving-threshold $c_{\min}$

The block composition formulas are simply the first block column of


$$
\mathsf G_{n,t}=\mathsf G_{n,u}\mathsf G_{u,t}.
$$


They correctly retain the reference-direction scalar $\alpha_{u,t}$. The warning that this scalar is not automatically a unit under terminal alignment alone is correct.

The least cofactor formula is also correct. At $p>t+2$, the terminal observation ideal has exponent $a_t$, while the initial observation ideal has exponent $a_n$. The least exponent needed to multiply both initial observations into the terminal ideal is


$$
(a_t-a_n)_+.
$$


Hence


$$
c^{\min}_{n,t}
=
\frac{\mathcal I_t}
{\gcd(\mathcal I_t,\mathcal I_{n\mid t})}.
$$



The moving-threshold decomposition


$$
\mathcal I_n=\mathcal I_{n\mid t}\mathcal M_{n,t}
$$


is exact. Medium primes disappear from the gcd with $\mathcal I_t$, but not from $\mathcal I_n$ itself.

There is no legitimate inference from the two-step polynomial bound to a subfactorial multiplicative-block cofactor. The report correctly identifies both obstacles:

1. block defects compose by a sum, so cancellation is possible;
2. a small common defect can force most terminal alignment to be paid by $c_{\min}$.

---

## 5.3 Actual-seed reduction and denominators

The reduction


$$
r_s=\lambda_sz_s+(x_s,y_s,0)^T
$$


gives (5.2)–(5.4) directly. The determinant identity


$$
\det\mathsf A_s=\det\mathsf U_s\,\frac{F_s}{F_{s+1}}
$$


follows from the coordinate matrices with columns $z_s,e_1,e_2$.

The scalar elimination (5.11) is correct when $b_s\ne0$. Its numerator formula is among the supplied finite certificate checks.

The important denominator warning is valid:

- original-index nonvanishing of $F_n$ does not prove nonvanishing at all auxiliary indices;
- chart pivots introduce actual-coordinate denominators;
- scalar recovery introduces the numerator of $b_s$;
- these denominators can cancel in the whole transported defect without canceling termwise in the telescope.

The proposed clearer is a safe finite-payment claim for the patched backward calculation, not a height estimate. Its use requires the actual coordinate choices and their exact rational normalizations to be recorded. Nothing in the attachment makes it subfactorial.

### Exterior content

At $p>t+2$, the exterior transfer


$$
\det(\mathsf U_s)\mathsf U_s^{-T}
$$


is an integral automorphism. It preserves the ideal generated by the three exterior coordinates.

At the terminal,


$$
\omega_t=(-F_t\tau_{t+1},F_t\tau_t,-\overline M_t)^T.
$$


Reference primitivity therefore gives its content exponent $a_t$, and that exponent persists throughout the block.

This proves the exact large-prime content assertion, subject to the retained reference primitivity. It is a genuine obstruction to a free primitive normalization: dividing the exterior state to make it primitive pays precisely the divisor being studied.

---

## 5.4 Affine invariant and joint saturation

The coefficients of the final two source terms in (6.3) are correct:


$$
(2n+1)\widehat h-\frac m2(\widehat h+\widehat\ell)
=
\frac{(3n+1)\widehat h-m\widehat\ell}{2}.
$$


The two source substitutions have the correct factors $1/n$ and $1/2$.

Cancellation of the homogeneous seed term additionally uses the actual common scaling of


$$
(\widehat h,\widehat\ell)
$$


with $(\tau_n,\tau_{n+1})$. That is implicit in the retained construction and should be stated explicitly when the invariant is reused.

The cross-affine identity has the correct sign:


$$
(c_0\times c_3)\cdot
\bigl((\widehat h,\widehat\ell,0)\times(A^\circ,B^\circ,C)\bigr)
=
-CM+F\mathscr K_n^\circ
=
\kappa F-\Theta.
$$



### Primitive auxiliary ratio

The identity


$$
\gcd(F,\Theta)=\gcd(F,CM)
$$


requires $\Xi_n$ integral. On the original odd-index construction, the displayed normalizations provide that integrality. Thus $T_{\rm aff}$ and $d_{\rm aff}$ are indeed primitive numerator and denominator of the **auxiliary** ratio.

The saturation formula


$$
\mathfrak S_j=\gcd(|T_{\rm aff}|,D_j)_{>N}
$$


checks prime by prime. If $v_p(\Theta)>v_p(F)$, then necessarily $v_p(CM)\ge v_p(F)$, so the gcd used to form $T_{\rm aff}$ removes exactly $v_p(F)$. If $v_p(\Theta)\le v_p(F)$, both saturation expressions vanish.

### Joint saturation divisor

The proof of Theorem 7.2 is valid using the exact retained saturation statement


$$
v_p(\mathcal E_j^\circ)=f-a
$$


when that endpoint has positive saturated excess.

Also, $\kappa=2L(n!)^2$ is a unit at every $p>N$, and the actual seed-content assertion makes $g_z$ a unit there. The valuation comparison then gives


$$
\min(s_0,s_3)
\le v_p(\lambda_{\rm ct})-(f-a).
$$



This is a genuine joint restriction. It is not a height bound for $\lambda_{\rm ct}$, $J_{\rm res}$, or $C_{\rm sat}$.

---

## 5.5 A3 ledger and priorities

| Claim | Audit status |
|---|---|
| Paid inverse and two-step rational identities | Accepted; supported by supplied finite certificate |
| Resultant-content mechanism | Accepted |
| Actual two-step common alignment bound | Conditional on retained reference primitivity and remainder theorem |
| Composition and moving-threshold $c_{\min}$ | Accepted |
| Actual-seed reduction and scalar recurrence | Accepted on stated charts |
| Patched denominator payment | Finite payment only; no size bound |
| Exterior content equals $\mathcal I_t$ | Accepted conditionally on retained primitivity |
| Complete affine-source identity and cross-affine sign | Accepted |
| Joint saturated divisor theorem | Accepted conditionally on exact saturation theorem |
| Subfactorial $c^{\min}_{n,bn}$ | Unproved |
| Subfactorial $J_{\rm res}C_{\rm sat}$ | Unproved |
| Actual primitive denominator/error comparison | Unproved |

**Priority for A3:** the next work must address one of the two growth estimates, not another fixed-block identity or alignment sample. The supplied symbolic certificate already covers the named new polynomial identities; it should not be repeated.

---

# 6. Audit of A5turn14 and a new exact rank lemma

## 6.1 Finite inverse and kernel compression

The finite factorization is dimensionally consistent:


$$
K:\mathbb Z_2^d\to\mathbb Z_2^m,\qquad
G_{\rm end}:\mathbb Z_2^m\to\mathbb Z_2^d,
$$


and $S=I_d+G_{\rm end}K$ is a unit because $K\equiv0\pmod2$.

The identity $T=PU$ is finite Vandermonde. The exterior-column formula (2.6) follows by subtracting the omitted part of the full inverse-binomial convolution.

The bulk profile (3.3) can be checked by the stated summation method. After setting $r=j+t$, the full convolution is the first term of (3.2); its terms beyond the actual contact cutoff are exactly


$$
t=B_j+v,\qquad1\le v\le(s-q)_+.
$$


Thus the correction in (3.2) is necessary and has the right range. The exterior formula has the analogous excess range $1\le v\le a+s+1$.

The source response (4.4) also has the correct structure. Splitting the source convolution at the actual contact boundary leaves:

- the finite contact return $F_{jt}$;
- the exterior source sum.

Omitting the first term would change the finite solve.

The atom-product identity (5.7) is an integral combinatorial identity. The kernel count


$$
4(2D_0+1)^5
$$


matches four choices of $(\alpha,\alpha')$, four offset ranges and the $r$-range.

These arguments establish a finite reduction, not a practical evaluation theorem. When $m\ge b$, the Schur dimension is $b$; the report correctly disclaims smallness in that regime.

The symbol filtrations and normalized-force prefix remain dependencies from A5turn13, which is not attached.

---

## 6.2 Two necessary boundary corrections

### Correction 1: the whole terminal in (5.2)

At $j=b$,


$$
\Delta_bz^{(i)}=b z^{(i)}_{b-1},\qquad
\Delta_bz^k=bz^k_{b-1}.
$$


Therefore the **whole** terminal contribution to (5.2) is


$$
\boxed{
b^2W_b^2z^{(i)}_{b-1}z^k_{b-1}
+
bW_b^2z^{(i)}_{b-1}.
}
$$



The report’s (5.3) is only the second term, arising from the exterior $+1$. Its master identity (5.2) is correct, but the sentence calling (5.3) “the terminal contribution” is too strong.

Any implementation or certificate must include both terms.

### Correction 2: terminal high-word dependence

The factor


$$
W_b^2=\binom{n+2}{b}^2
$$


is not a short-lower-index binomial. Thus the claim in §6 that the data outside (5.9) are built from short-lower-index binomials must exclude the separately retained terminal binomial.

No theorem in the attachment shows that $W_b^2\bmod2^L$ depends only on the stated coefficient residue $b\bmod2^P$. It can be evaluated by the same factorial/carry machinery, but that is another high-word observable.

The correct separation is:

1. short coefficient data with the stated residue dependence;
2. long finite kernels;
3. the separate long terminal binomial and its complete terminal pairing.

---

## 6.3 Factorial carry states: formally valid, not yet effective

For $L\ge3$, the product of all odd units modulo $2^L$ is $1$. Hence


$$
O_L(t+2^L)=O_L(t).
$$


Separating the factors of $2$ in $N!$ gives


$$
\operatorname{odd}(N!)
=
\prod_{a\ge0}O_L(\lfloor N/2^a\rfloor)\pmod{2^L}.
$$


Together with Kummer’s carry count, this proves (7.3), with only odd inverses.

### State interpretation that makes the bound valid

The borrow bits must be understood as the borrows **entering the low end of the buffered window**, not merely the current highest processed bit.

At each transition:

1. append a new bit of $j$;
2. reconstruct each affine $L$-bit window from the buffered $j$-bits, known parameter window and incoming low-end borrow;
3. evaluate the factorial-unit factor for that completed window;
4. count the carry at its lowest position;
5. shift the buffer and update the low-end borrows/carries by one position.

Initial filling and final zero-padding are controlled by the external digit position. This avoids needing separate buffers for all affine streams.

With this delayed-window interpretation, the bound


$$
L\,2^{L-1+7+4}=L\,2^{L+10}
$$


is sufficient. Invalid terminal borrows reject out-of-range binomials and failed cutoffs.

This is a formal finite-state evaluation theorem. It is not a practical primitive-digit algorithm at the stated paid precisions. It also does not inherit the normalized force’s short residue interface: the displayed transition reads the full original parameter word, of length $\Theta(u+1)$.

---

## 6.4 Green pairing and rank obstruction

The backward adjoint recurrence in §8 has the correct signs. In particular, the coefficient of $k_j$ in $D^T\lambda$ is


$$
\lambda_{j-2}-\alpha_{j-1}\lambda_{j-1}
+\beta_j\lambda_j-\chi_{j+1}\lambda_{j+1}.
$$


Thus the two boundary charges and full forcing sum are retained correctly.

The rank entry can be independently derived:


$$
(GJ)_{i,i+2}=-(i+1)W_{i+1}^2,
$$


while


$$
(J^TG)_{i,i+2}=(i+1)(i+2)W_{i+2}^2.
$$


Their difference is exactly (9.4).

### New lemma: exact rank and a paid minor

Let


$$
A=GJ-J^TG
$$


for A5’s original finite matrices. Then


$$
\boxed{\operatorname{rank}_{\mathbb Q}A=b-1.}
$$



**Proof.** The shifted $(b-2)\times(b-2)$ submatrix, with rows $0,\ldots,b-3$ and columns $2,\ldots,b-1$, is lower triangular with nonzero diagonal


$$
a_i=-(i+1)\bigl(W_{i+1}^2+(i+2)W_{i+2}^2\bigr).
$$


Thus $\operatorname{rank}A\ge b-2$.

The matrix $A$ is skew-symmetric. Its rational rank is even. Since the original $b=9^{18+32u}$ is odd, $b-2$ is odd and the next possible rank is $b-1$. A skew-symmetric matrix of odd order has rank at most $b-1$. Therefore its rank is exactly $b-1$. ∎

There is also an exact valuation formula for this specific minor. Using


$$
W_{i+2}=W_{i+1}\frac{n+1-i}{i+2},
$$


we obtain


$$
a_i
=-\frac{i+1}{i+2}W_{i+1}^2
\bigl((n+1-i)^2+i+2\bigr).
$$


Because $n$ is even, the parenthesized integer is odd. Therefore


$$
v_2(a_i)
=
v_2(i+1)+2v_2(W_{i+1})-v_2(i+2).
$$


For the shifted minor $M$,


$$
\boxed{
v_2(\det M)
=
2\sum_{k=1}^{b-2}v_2\binom{n+2}{k}
-v_2(b-1).
}
$$



This formula makes the rational/modular distinction explicit. The minor is nonzero over $\mathbb Q$, but may be highly divisible by $2$. Its rational nonvanishing gives neither a useful rank modulo $2^L$ nor a bound for the particular forced pairing.

---

## 6.5 A5 ledger and priorities

| Claim | Audit status |
|---|---|
| Finite inverse factorization with both binomial factors | Accepted, conditional on symbol filtration |
| Bulk/exterior finite convolution profiles | Accepted |
| Complete exterior-source response | Accepted |
| Polynomially bounded kernel family | Accepted |
| (5.3) is the whole terminal in (5.2) | Corrected: it is only the exterior-$+1$ part |
| All non-kernel data have short-binomial residue dependence | Corrected: exclude $W_b^2$ |
| Carry/window evaluation | Accepted with delayed-window state interpretation |
| Feasible evaluation at useful precision | Not obtained |
| Exact Green pairing | Accepted |
| Rational rank obstruction | Accepted; strengthened to rank $b-1$ |
| Norm-sensitive forced pairing or primitive digit | Unproved |
| All-prime denominator/error comparison | Unproved |

**Priority for A5:** correct the terminal specification first. Then seek a quotient for the actual forced linear combination of kernels, including the terminal binomial. The rational rank theorem does not justify discarding the bulk defect at binary precision.

---

# 7. Global normalization and the common remaining obstruction

None of these local results permits a change to the final normalization.

For A1’s determinant construction, retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|),
$$


and


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
$$



For the A2 and A5 weighted constructions, retain their actual row conventions, least simultaneous clearer and final integers:


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$


In A5 specifically,


$$
A_B=d_B^2\,4\Lambda^2R^2N,\qquad
H_B=d_B^2\,8\Lambda Rb!H.
$$


No extra reconstructed row-content division is authorized.

For A3, the endpoint denominator remains


$$
d_j=
\frac{|n!R_j|}
{\gcd(|n!R_j|,\ |E_nR_j+C_j^{\rm complete}|)},
$$


and the weighted denominator remains


$$
q_\lambda=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}}.
$$


The auxiliary $d_{\rm aff}$ is not a replacement for either denominator.

All these gcds retain **every prime**. The whole errors remain, at the same indices,


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n
$$


or A3’s complete expression


$$
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
$$



The global target still requires an infinite original sequence for which the actual primitive pair satisfies


$$
0<|q(e+\pi)-p|\longrightarrow0.
$$


If $e+\pi=a/d$ were rational, every nonzero such form would have absolute value at least $1/d$. Thus this criterion would prove irrationality—but none of the audited local results establishes it.

---

# 8. Exact next certificates and final proof status

## 8.1 No repeated expensive calculation

No repeat is proposed of:

- the $350$-coordinate or $62$-coordinate ternary calculations;
- the $3375$ endpoint calculation;
- the accepted A3 symbolic identity certificate;
- the old A5 operator/Schur receipt.

## 8.2 Bounded arithmetic that is genuinely relevant

The most sharply specified bounded outstanding arithmetic is A2’s **low mixed-observation assembly**, once its missing complete-response lemmas are supplied.

### Inputs

1. the original retained low residues;
2. the fixed $58$-entry head modulo $29^2$;
3. complete source and finite-return dictionaries at the required precision;
4. the certified finite exterior response data at precision $29^7$;
5. all low indices $0\le\ell<29^3$;
6. the exact split at $\ell=5044$;
7. explicit terminal-vanishing and logarithmic-force guards.

### Expected verifiable output

An $11$-entry row over $\mathbb F_{29}$ multiplying


$$
\bigl(S,\ k_B^2,\ T,\ (U_s)_{s\in\{0,1\}^3}\bigr),
$$


with:

- the $A_q$ factorization checked;
- both finite returns included;
- the shorter-branch subtraction included;
- all divided quantities shown integral before reduction.

This would certify only the bounded low observation. It would not evaluate that row on every actual upper continuation.

For A1, the immediate bottleneck is a uniform proof about complete core-column edges; a new producer digit does not resolve it. For A3, the remaining obligations are growth estimates rather than another finite identity. For A5, the presently justified carry bound is too large to commission a useful primitive-digit calculation; any later certificate must include the corrected whole terminal and use the paid precision $L=K+a+3$.

## 8.3 Final conclusion

The audit finds no valid route from the four reports to a global irrationality conclusion.

The new unconditional result established here is


$$
\boxed{
\operatorname{rank}_{\mathbb Q}(GJ-J^TG)=b-1
}
$$


on A5’s original family, together with the exact valuation of the displayed shifted minor. This sharpens the obstruction to the natural bounded-rank Green reduction, but leaves its norm-sensitive forced pairing unresolved.

The principal remaining mathematical bottlenecks are:

- **A1:** certify the complete source/feedback inputs to $\mathcal Q\in3^5M$, then prove $\Phi_R\in3^{11}M$, for example through the depth-$10$ two-edge lemma.
- **A2:** prove the complete mixed divisibilities supporting the $58$-entry quotient, then evaluate the boundary-correct whole upper observation.
- **A3:** prove subfactorial bounds for the newly acquired alignment cofactor and the joint saturation cost.
- **A5:** evaluate or effectively quotient the actual weighted-kernel combination, including its complete terminal and high-word dependence.
- **Globally:** compare the final all-prime gcd and actual primitive denominator with the whole nonzero error on the same infinite original indices.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


