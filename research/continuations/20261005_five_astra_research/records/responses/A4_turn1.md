> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A4 audit and follow-on lemma

**I do not obtain a proof or disproof of the irrationality of $S=e+\pi$.** The matched-$b=3$ arithmetic argument is substantially stronger than the original report’s erroneous seed table suggests: the prime-power transfer has a valid proof, and the complete-numerator valuation argument correctly handles the final denominator gcd. However, I distinguish that paper proof from verification of the supplied finite certificate. I have not independently recomputed all 446 rows of the eight-prime certificate, and therefore do **not** label the resulting family exclusion independently verified in this response.

For the sparse pullback problem, I give a different, bounded result: an **exact continuous norm minimization for a specified high-block multijet construction**, together with the additional integer-lattice condition. It quantifies what distributing a correction among many jets can and cannot accomplish. It is not another spacing theorem and does not establish a favorable infinite construction.

---

# 1. Audit ledger for matched $b=3$

Here “PASS” concerns the displayed mathematical implication, not an unexecuted certificate check.

| Component | Audit result |
|---|---|
| Five-state recurrence | **PASS**, by the polynomial transition and integration-by-parts identities detailed below |
| Explicit high rows and cumulative rows | **PASS**, from the derivative identities; the $n+2$ division is exact before modular reduction |
| Complete endpoint normalization | **PASS relative to the supplied general cofactor endpoint identities** |
| Row/minor/contraction content cancellation | **PASS** on $D_n\ne0$ |
| Final endpoint gcd and actual $q_n$ | **PASS**; it is retained, not replaced by a factorial clearer |
| All-odd-prime-power transfer | **PASS**, with a cleaner proof below that avoids the awkward adjacent-contraction weight estimate |
| Original $n=1$ seed and seven-row table | **FAIL**; the first incorrect contraction is $\sigma_1=-30$, which must be $-16$ |
| Corrected $n=1$ seed | **PASS**, checked directly below |
| Eight-prime certificate | **Supplied finite evidence**; all displayed $V$-entries are nonzero, but I have not independently regenerated every row |
| Prime-unit $\Rightarrow$ actual denominator lower bound | **PASS**, including the complete numerator and final gcd |
| Fixed-$b=3$ normality and whole-error asymptotic | **Inherited author theorem**, not independently re-proved here |
| Eventual matched-$b=3$ exclusion | **Follows from the corrected finite certificate plus the proved arithmetic and inherited analytic theorem**; not claimed here as a fully independent certificate audit |

The exclusion, when those dependencies are accepted, is an **eventual all-index exclusion of shrinking primitive forms in this specific family**. It says nothing by itself about the irrationality of $S$.

---

# 2. Recurrence and high-row audit

## 2.1 Polynomial identities behind the recurrence

Write


$$
H_n(x)=n![z^n]e^{xz}\left(1-z+\frac{z^2}{2}\right)^n.
$$



The relevant polynomial transition is equivalently


$$
H_{n+1}(x)
=\frac{x}{2}H_n''(x)+(n+1-x)H_n'(x)
 +(x-n-1)H_n(x).                                      \tag{2.1}
$$


Multiplying by $x^{n+1}$ gives exactly A2’s transition for
$\mathscr F_n=x^nH_n$:


$$
\mathscr F_{n+1}
=\frac{x^2}{2}\mathscr F_n''
+x(1-x)\mathscr F_n'
+\left(x^2-x-\frac{n(n+1)}2\right)\mathscr F_n.
$$



The differential equation needed for the derivative reduction has the particularly simple form


$$
xH_n'''+(n+2-2x)H_n''+(2x-2)H_n'-2nH_n=0.             \tag{2.2}
$$


These identities can be checked coefficientwise in the defining finite coefficient extraction. At $x=1$, (2.2) and its derivative give


$$
H_n'''(1)=2nH_n(1)-nH_n''(1),
$$




$$
H_n''''(1)=-(n+1)H_n'''(1)
            +2H_n''(1)+2(n-1)H_n'(1).
$$


Substitution into (2.1) and its first two derivatives yields A2’s first three state transitions.

For the integral coordinates, the basic identity is


$$
I(P')=I(P)-P(1),\qquad
I(P)=\int_1^\infty e^{1-x}P(x)\,dx.
$$


For example,


$$
I(x^2\mathscr F_n'')
=M_2-4M_1+2M_0+h_n-J_n,
$$


and


$$
I(x(1-x)\mathscr F_n')
=-M_2+3M_1-M_0.
$$


They give


$$
\mathcal A_{n+1}
=\frac12M_2-\frac{n(n+1)}2M_0+\frac12(h_n-J_n),
$$


as asserted. Applying the same calculation with an additional factor $x$, and using the displayed differential equation for $\mathscr F_n$, gives A2’s $M_2,M_3$ eliminations and hence its $\mathcal M_{n+1}$ transition.

Thus the recurrence is not inferred from a finite run.

## 2.2 High-row indices

At $b=3$, the monic high rows are proportional to


$$
(E_{n+1,0},E_{n+1,1},E_{n+1,2},E_{n+1,3})
$$


and


$$
(E_{n+2,1},E_{n+2,2},E_{n+2,3},E_{n+2,4}).
$$


The second row has the exact integer divisor $n+2$. Removing it gives A2’s $s$-row and the common high-row scale


$$
\rho_n=\frac{n+2}{(2n+2)!(2n+4)!}.
$$


There is no division by $n+2$ in a residue field.

Leibniz’s rule, followed by the two derivative identities above, reproduces the displayed $r$- and $s$-formulas. The cumulative rows use derivative orders $0,1,2$ for $\mathbf p$ and $1,2,3$ at $n+1$ for $\mathbf u$, so their indices agree with the general cofactor source.

The actual approximation domain remains **$n\ge3$**. Smaller nonnegative indices are legitimate scalar seeds only.

---

# 3. The erroneous seed, checked directly

At $n=1$,


$$
H_1(x)=x-1,\qquad
(h_1,u_1,v_1,\mathcal A_1,\mathcal M_1)
=(0,1,0,3,11).
$$


Thus


$$
\mathcal B_1=\mathcal M_1+h_1-u_1=10.
$$



The four rows are


$$
r=(1,0,-4,0),\qquad s=(-1,10,28,-24),
$$




$$
\mathbf u=(0,0,-2,-2),\qquad
\mathbf p=(0,0,1,3).
$$


Their determinants give


$$
(\sigma_1,\chi_1,\kappa_1)=(-16,-44,-40).
$$


Consequently,


$$
V_1=(-16)\cdot3-(-44)\cdot10-(-40)=432.
$$



Modulo $7$, the corrected contraction row is therefore


$$
(\sigma_1,\chi_1,\kappa_1,V_1)\equiv(5,5,2,5).
$$



**The original table fails at this row.** The error is not a harmless common scaling: the erroneous triple and the corrected triple are not proportional. Nevertheless, the corrected $V_1$ is still a $7$-adic unit, so this correction does not destroy the intended $7$-adic unit criterion.

---

# 4. A complete proof of prime-power transfer

The claimed transfer can be established without the delicate weight $W_s$ used for $\mathcal B_n$.

Let $p$ be odd, $a\ge1$, and $m,n\ge0$ with
$m\equiv n\pmod{p^a}$. Put


$$
a_s(n)=[z^s]\left(1-z+\frac{z^2}{2}\right)^n.
$$



For $s\ge1$,


$$
v_p(a_s(m)-a_s(n))
\ge a-\lfloor\log_p s\rfloor.                        \tag{4.1}
$$


Indeed, after assuming $m\ge n$, expand the additional factor as


$$
(1+(\phi-1))^{m-n}.
$$


Only powers $1\le j\le s$ contribute to its nonconstant coefficient of degree at most $s$, and


$$
v_p\binom{m-n}{j}\ge a-v_p(j).
$$


All coefficients of $\phi-1$ are $p$-integral.

For every nonnegative integer $x$,


$$
v_p((x)_s)\ge v_p(s!)\ge\lfloor\log_p s\rfloor.       \tag{4.2}
$$


Furthermore, falling factorials are integer polynomials, so


$$
(m)_s\equiv(n)_s\pmod{p^a}.
$$


Splitting a product difference and applying (4.1)–(4.2) proves transfer term by term in


$$
H_n^{(d)}(1)=\sum_{s\ge0}(n)_{s+d}a_s(n),
\qquad d=0,1,2.                                     \tag{4.3}
$$



For the integral coordinates, introduce the $p$-adic function


$$
\mathfrak D(x)=\sum_{r\ge0}(x)_r,\qquad x\in\mathbb Z_p.
$$


The sum converges uniformly: by continuity from nonnegative integers,


$$
(x)_r/r!\in\mathbb Z_p,
$$


so its terms tend uniformly to zero. Every finite partial sum is an integer polynomial. Hence $\mathfrak D$ is $1$-Lipschitz. At a nonnegative integer $j$,


$$
\mathfrak D(j)=D_j.
$$



Now use the two parallel formulas


$$
\mathcal A_n
=\sum_{s\ge0}(n)_s a_s(n)\mathfrak D(2n-s),           \tag{4.4}
$$




$$
\mathcal M_n
=\sum_{s\ge0}(n)_s a_s(n)\mathfrak D(2n-s+1).         \tag{4.5}
$$


These are the direct integrals of $\mathscr F_n$ and $x\mathscr F_n$. At a nonnegative index $n$, terms with $s>n$ vanish, so the surviving $\mathfrak D$-arguments are nonnegative. Defining $\mathfrak D$ on all of $\mathbb Z_p$ avoids any negative-index ambiguity when the two sums are compared.

The product $(n)_s a_s(n)$ transfers by (4.1)–(4.2), and the $\mathfrak D$-factor transfers by its Lipschitz property. Thus $\mathcal A_n,\mathcal M_n$ transfer. Finally,


$$
\mathcal B_n=\mathcal M_n+h_n-u_n
$$


transfers as well.

Every raw contraction and $V_n$ is polynomial over $\mathbb Z[1/2]$ in the state and $n$. Therefore


$$
V_m\equiv V_n\pmod{p^a},
$$


and likewise for $\sigma,\chi,\kappa$.

**This proves the all-prime-power transfer on the full scalar domain $n\ge0$.** It does not prove periodicity of the endpoint Legendre quantities, the second-kind values, or the primitive denominator.

---

# 5. Endpoint normalization and denominator depth

The supplied general cofactor identities specialize to


$$
\frac{X_n}{Y_n}
=\frac{Q_n+2^{n+1}V_n/(n!)^2}{D_n},
\qquad D_n\ne0.                                    \tag{5.1}
$$


The term $-\kappa_n$ in $V_n$ is indispensable.

On this domain,


$$
\delta_n=\gcd(|\sigma_n|,|\chi_n|,|\kappa_n|)>0.
$$


Factoring the two row contents, then the maximal-minor content, and then the remaining contraction content gives exactly the factorization claimed for $\delta_n$. This uses only linearity of all three contractions in the high-row minor vector.

After dividing by $\delta_n$, retain


$$
N_n=\lambda_n\left(Q_n^*+\frac{2^{n+1}}{(n!)^2}V_n^*\right),
\qquad
Z_n=\lambda_nD_n^*,
$$




$$
g_n=\gcd(|N_n|,|Z_n|),
$$




$$
q_n=\frac{|Z_n|}{g_n},\qquad
p_n=-\operatorname{sign}(Z_n)\frac{N_n}{g_n}.         \tag{5.2}
$$


Thus


$$
c_n=-X_n/Y_n=p_n/q_n,\qquad
L_n=q_nS-p_n=q_n(S-c_n).
$$


This is the actual primitive form.

Suppose a prime $p$ has $V_r\not\equiv0\pmod p$ for all $0\le r<p$. Transfer gives


$$
v_p(V_n)=0\quad(n\ge0).
$$


It also forces $v_p(\delta_n)=0$, since $\delta_n\mid V_n$.

Put $F=v_p(n!)$ and $\ell=\lfloor\log_p(n+1)\rfloor$. The second-kind moment denominators give


$$
v_p(Q_n)\ge-\ell.
$$


Whenever $2F>\ell$,


$$
v_p\left(Q_n+\frac{2^{n+1}}{(n!)^2}V_n\right)=-2F.  \tag{5.3}
$$


The complete numerator is therefore nonzero; its two terms cannot cancel at equal valuation.

Actual rational reduction now gives


$$
v_p(q_n)=2v_p(n!)+v_p(D_n)
        =2v_p(n!)+v_p(D_n^*)\ge2v_p(n!).             \tag{5.4}
$$


This calculation includes the final gcd in (5.2).

For the eight supplied primes, all at least $7$, $n\ge101$ suffices for the strict separation condition for every prime. The endpoint condition $D_n\ne0$ is still required.

---

# 6. What the eight-prime certificate would establish

Let


$$
\mathcal P=\{7,19,31,61,71,73,83,101\}.
$$


The eight supplied tables contain


$$
7+19+31+61+71+73+83+101=446
$$


residue rows. Their displayed $V$-columns have no zero entries.

If those rows are verified from the recurrence and determinant definitions, then


$$
\log q_n\ge W_8n-O(\log n),
\qquad
W_8=\sum_{p\in\mathcal P}\frac{2\log p}{p-1}.         \tag{6.1}
$$


Here $W_8$ is approximately $1.7828$, exceeding


$$
\tau=2\log(1+\sqrt2)\approx1.76275.
$$



The supplied certificate’s quoted rate $2.19816\ldots$ belongs to the **larger thirteen-prime list**, not this eight-prime set. It must not be substituted for $W_8$.

The inherited fixed-$b$ theorem, at $b=3$, supplies eventual normality, $D_n\ne0$, and the whole-error asymptotic


$$
S-c_n=(-1)^n\epsilon_n(\sqrt2-1)^3(1+o(1)),
\qquad
\frac{\log\epsilon_n}{n}\longrightarrow-\tau.
$$


Therefore, after verification of the finite certificate,


$$
\liminf_{n\to\infty}\frac{\log|L_n|}{n}
\ge W_8-\tau>0.                                    \tag{6.2}
$$



So the primitive forms would grow exponentially at **every sufficiently large index**, and no infinite subsequence of this matched-$b=3$ family could tend to zero.

I have checked the paper implication and the corrected small seed, but not independently regenerated all 446 rows. That is the precise remaining audit qualification; it is not a proposed infinite arithmetic conjecture.

---

# 7. Sparse pullbacks: exact multijet norm minimization

I reuse the archived varying-pullback spacing result. Its common-radius argument already covers different polynomials and gives the ratio restriction. I make no new claim for that obstruction.

The following addresses a more specific question: **can spreading a correction across a below-nonlinearity block reduce its analytic cost?**

## 7.1 Specified construction

Fix a real rational integral-Hurwitz polynomial $P$ with $P(0)=0$, $P(1)=1$. Let $N\ge2$ be even, and choose


$$
1\le m\le N<2m.
$$


Consider


$$
Q=P+(1-z)J,\qquad
J(z)=\sum_{k=m}^N b_kz^k,\qquad b_k=K_k/k!,\quad K_k\in\mathbb Z. \tag{7.1}
$$


Write


$$
a(z)=F'(P(z))=\sum_{h\ge0}a_hz^h.
$$



Since $N<2m$, the nonlinear composition terms do not affect the Taylor sum through $N$. Moreover, multiplication by $1-z$ telescopes the endpoint coefficient sum. Consequently the **exact** change in the complete Taylor center is


$$
c_N(Q)-c_N(P)
=\sum_{k=m}^N a_{N-k}b_k.                            \tag{7.2}
$$


This is a useful simplification beyond merely knowing that the response is triangular.

For $r>1$, define


$$
\|J\|_{2,r}^2
=\frac1{2\pi}\int_0^{2\pi}|J(re^{it})|^2\,dt
=\sum_{k=m}^N |b_k|^2r^{2k},
$$


and


$$
A_{m,N}(r)^2=\sum_{h=0}^{N-m}|a_h|^2r^{2h}.
$$


Since $a_0=F'(0)=2$, this last quantity is positive.

## 7.2 Exact continuous optimum

**Lemma.** If the coefficients $b_k$ are temporarily allowed to be arbitrary real numbers, then among all $J$ satisfying


$$
c_N(Q)-c_N(P)=d,
$$


the exact minimum is


$$
\boxed{\min\|J\|_{2,r}
=\frac{|d|\,r^N}{A_{m,N}(r)}.}                      \tag{7.3}
$$


The unique minimizing coefficients are


$$
\boxed{
b_k=
\frac{d\,a_{N-k}r^{-2k}}
{\displaystyle\sum_{j=m}^N a_{N-j}^2r^{-2j}}.
}                                                   \tag{7.4}
$$



**Proof.** Apply weighted Cauchy–Schwarz to (7.2):


$$
|d|^2
\le
\left(\sum_{k=m}^N b_k^2r^{2k}\right)
\left(\sum_{k=m}^N a_{N-k}^2r^{-2k}\right).
$$


The second factor is $r^{-2N}A_{m,N}(r)^2$. Equality holds precisely when the two weighted vectors are proportional, giving (7.4). The functional is nonzero because $a_0=2$, so the minimizing vector is unique. ∎

For the integral-Hurwitz construction, (7.3) is a rigorous lower bound. Equality is possible **only if**


$$
k!b_k\in\mathbb Z\qquad(m\le k\le N)                 \tag{7.5}
$$


for the unique vector (7.4). Thus the relaxed optimum does not silently supply an integral solution.

This turns a fixed $m,N,r,d$ problem into an explicit finite weighted closest-lattice problem, rather than a generic congruence claim.

## 7.3 Full odd cancellation and final gcd

Let


$$
Z_N=N!c_N(P),\qquad f_N=v_2(N!),\qquad O_N=N!/2^{f_N}.
$$


For every member of (7.1), $N!c_N(Q)$ is an odd integer. Its actual denominator is


$$
q_N(Q)
=2^{f_N}\frac{O_N}{\gcd(O_N,N!c_N(Q))}.             \tag{7.6}
$$


Full odd cancellation means precisely


$$
c_N(Q)=\frac{L}{2^{f_N}},\qquad L\in2\mathbb Z+1,
$$


and then $q_N(Q)=2^{f_N}$.

Define the exact base-center distance


$$
d_N=\operatorname{dist}
\left(c_N(P),\,2^{-f_N}(2\mathbb Z+1)\right).
$$


Every full-cancellation member of this specified block obeys


$$
\boxed{
\|J\|_{2,r}\ge\frac{d_Nr^N}{A_{m,N}(r)}.
}                                                   \tag{7.7}
$$



Also, on $|z|=r$,


$$
|(1-z)J(z)|\ge(r-1)|J(z)|.
$$


Hence


$$
\boxed{
\|Q-P\|_{\infty,r}
\ge (r-1)\frac{d_Nr^N}{A_{m,N}(r)}.
}                                                   \tag{7.8}
$$



If $a=F'(P)$ is analytic on a neighborhood of the closed $r$-disk, then


$$
A_{m,N}(r)\le \|a\|_{2,r},
$$


uniformly in both $m$ and $N$. Consequently, increasing the block dimension cannot supply an unbounded multiplicative gain in this continuous relaxation:


$$
\|Q-P\|_{\infty,r}
\ge \frac{r-1}{\|F'(P)\|_{2,r}}\,d_Nr^N.             \tag{7.9}
$$



This holds at each eligible index separately. Making the indices arbitrarily sparse does not weaken it.

### Interpretation and limitation

The new bounded conclusion is the exact optimum (7.3), its unique optimizer, and the arithmetic admissibility condition (7.5). In particular, any improvement from distributing the correction among this block is explicitly measured by $A_{m,N}(r)$; it is uniformly bounded for a fixed analytic base.

Equation (7.9) does **not** establish that $d_N$ is large or small infinitely often. When the base has radius greater than $2$, its complete Taylor tail relates $d_N$ to the familiar dyadic proximity question for $S$. I do not claim that reformulation as new progress. The norm minimization identifies precisely why this specified multijet relaxation does not remove that unresolved input.

For an analytic modified branch with $Q(1)=1$, the whole primitive error remains


$$
L_N=2^{f_N}S-L.
$$


No unconditional individual nonvanishing follows from the norm optimization. Under a rationality hypothesis $S=A/B$, however, $L_N\ne0$ once $f_N>v_2(B)$, because $L$ is odd.

---

# 8. Required concluding ledger

## (1) New result and proof status

- **Proved paper-level audit:** the prime-power transfer is valid, with a direct proof for $\mathcal M_n$ that avoids the adjacent-weight complication.
- **Proved paper-level audit:** the complete endpoint quotient, content removal, final gcd, and prime-unit denominator-depth implication are consistent with the supplied general cofactor identities.
- **Independently corrected finite seed:** at $n=1$,
  

$$
(\sigma,\chi,\kappa,V)=(-16,-44,-40,432).
$$


- **Conditional on finite certificate verification and the inherited whole-error theorem:** the eight-prime set excludes shrinking primitive forms at every sufficiently large matched-$b=3$ index.
- **New bounded follow-on lemma:** the specified high-block multijet construction has the exact continuous minimum (7.3), unique optimizer (7.4), and integral admissibility condition (7.5). It supplies an obstruction to obtaining an unbounded norm advantage merely by enlarging that block.

## (2) Exact remaining bottleneck

For the matched-$b=3$ audit, the remaining independent-check task is finite: regenerate the 446 certificate rows and certify the eight-prime rate crossing. The analytic whole-error theorem remains an explicitly inherited dependency.

For the sparse pullback frontier, no construction has been proved that simultaneously supplies:

1. one common analytic radius greater than $2$;
2. full odd-denominator cancellation at infinitely many sparse even indices;
3. control of the **whole** primitive evaluated error; and
4. the required nonvanishing.

The norm-optimal real correction need not lie in the Hurwitz coefficient lattice, and even its norm requires a quantitative bound on $d_N$. Neither issue is settled by congruence solvability or index sparsity.

## (3) Bounded exact computation request

No new prime search is requested.

**Inputs:** exactly the eight primes


$$
\{7,19,31,61,71,73,83,101\},
$$


the five-state recurrence, the displayed high-row formulas, and the determinant definitions.

**Expected verifiable output:**

1. Regenerate all **446** residue rows from the initial state $(1,0,0,1,2)$.
2. Compare every state and contraction entry with the supplied certificate; report the exact mismatch list.
3. Verify the corrected $n=1$ contractions independently from the four explicit rows above.
4. Return each prime’s exact zero set for $V_r$, $0\le r<p$.
5. Give rational lower and upper bounds proving
   

$$
\sum_{p\in\mathcal P}\frac{2\log p}{p-1}
   >2\log(1+\sqrt2).
$$



Those outputs would close the stated finite audit dependency. They would **not** decide the irrationality of $e+\pi$.
