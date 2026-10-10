> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Family022 audit: centres, first joins, capacity, and the variance ledger

## 1. Outcome and scope

The supplied sections contain substantial valid mathematics beyond a generic almost-everywhere argument. In particular:

1. **The centre-density and centre-kernel arguments are proved at their stated finite-block scope.** The adjusted-host construction also supplies the claimed lower densities, shell counts, and exterior separation, subject to the stated choices of constants.
2. **The one-prime matching rule admits an exact deterministic transfer identity.** Its capacities use the actual residual-scaled raw weights and the actual mask probabilities—not hypothetical independent residue probabilities.
3. **The variance-budget argument is valid under the stated history-preservation and equivariance hypotheses.** Its implicit constant can be replaced by the explicit bound
   

$$
\sum_p(J_p+K_p')\le 3N_0M_{\rm birth},
$$


   where $M_{\rm birth}$ is the total first mass inserted at births. The further inequality $M_{\rm birth}\le W$ depends on the birth prescriptions.
4. **Two arithmetic mask sums used in the first-join discussion can be evaluated explicitly.** These give deterministic bounds with explicit harmonic-height costs and justify parts of the roundoff summation without appealing to an unnamed divisor-moment calculation.

However:

- The packet does **not** establish the sparse-alignment or chronological-partition inputs.
- The complete birth prescriptions, direct comparisons, and several good-mask properties used by `joins.tex` are not supplied.
- Consequently, the packet proves a meaningful **conditional reduction**, not the complete Family022 theorem.
- None of these results has yet been connected to the actual A3 projected scalar sequence. In particular, no supplied identity identifies its coefficients with the matching capacities below, and no supplied estimate controls its fully paid primitive denominator or its nonzero whole error.

Thus **no unconditional rationality or irrationality conclusion for $e+\pi$ follows**.

The original A3 index domain remains


$$
n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2,
$$


with the archived admissible projection indices and their special boundary corrections unchanged. Nothing in this report replaces that domain by a denser family or by almost every parameter.

---

## 2. What is proved in the centre and hierarchy sections?

### 2.1 Density above an original host

For a common-width family $\mathcal V$ dividing $L$, set


$$
k_L=Lr,\qquad
\delta_L=\sum_{v\in\mathcal V}\frac{\phi(v)}L,\qquad
m_L=k_L\delta_L.
$$



The proof of


$$
\delta_L\ll_{k_0}k_L^{H_0},\qquad \delta_L\le1
$$


is valid.

The important hypothesis is not merely $v\mid L$. It is that $L$ is at least every relevant original host. Under this hypothesis $2L$ cannot be popular: otherwise any nonraw assigned row would have a larger original host, and any raw assigned row would cease to be raw. This gives, when $2Lr\le k_0$,


$$
\frac{\delta_L}{2}
\le
\sum_{\substack{v\mid2L\\r(v)=r}}\frac{\phi(v)}{2L}
<(2Lr)^{H_0}.
$$


For $2Lr>k_0$, the divisor identity


$$
\sum_{v\mid L}\phi(v)=L
$$


supplies the required fixed-parameter bound.

This is an actual density estimate for the assigned divisor families. It is not a statement about numerator residues.

### 2.2 Adjusted hosts preserve the necessary hypothesis

Write the minimizing cost as


$$
T=b+10a+10c_++(-c)_+,
\qquad
\log(Lr)=-b+a+c.
$$


The elementary inequalities used in the source are valid:


$$
T\ge |\log(Lr)|,
\qquad
T\ge10\log(Lr)\quad\text{when }\log(Lr)>0.
$$



If $H_v$ is the row's original host, using $(H_v,r)$ as a candidate gives


$$
T\le-\log(H_vr).
$$


Combining this with $T\ge-\log(Lr)$ yields $L\ge H_v$. Thus the density lemma really does apply to adjusted objects.

For shell $s=B_i^*$,


$$
k_L\ge e^{-(s+1)}.
$$


After the density purge,


$$
\delta_L\ge e^{-.32s},
\qquad
m_L\ge e^{-1}e^{-1.32s}.
$$


The lower bounds concern the **original assigned families**, not later surviving masks or numerator points. Subsequent arguments must not silently apply them to a thinned family.

### 2.3 The centre count and purge

The popular-centre count follows from the displayed incidence argument and the tensor lemma. For centres $D,D'\asymp e^{-b}/r$,


$$
(D,D')r
\asymp
e^{-b}
\left(\frac D{(D,D')}\frac{D'}{(D,D')}\right)^{-1/2}.
$$


The tensor lemma applies with $s=1/2>1-u$, giving


$$
\sum_{D,D'}(D,D')r\ll e^{-b}n^{2u}.
$$


Hence


$$
n^{2-2u}\ll W_r e^{(1+2H_0)b},
$$


and choosing $u>1/2$ sufficiently close to $1/2$ gives the stated bound.

The density-purge calculation is also correctly organized. The relevant exponent is


$$
3H_0b+2a+c\le .21T.
$$


After multiplying by the discarded density $e^{-.32s}$, the resulting shell contribution is summable:


$$
O\!\left(W_{r_0}(s+1)^3e^{-.11s}\right).
$$


Covering an object by more than one source witness can overcount, but cannot invalidate this upper bound.

### 2.4 Kernel summation and shell multiplicity

The identity


$$
\Theta_{ij}
=(m_Lm_M)^{1/2}(UT)^{-1/2}
\left(\frac{r_{\min}}{r_{\max}}\right)^{1/2}
(\delta_L\delta_M)^{-1/2}
$$


is exact.

The original centre-kernel lemma assumes at most one object per $(L,r)$. Adjusted objects can have different shells at the same $(L,r)$; the later decay-kernel proof correctly avoids applying that lemma without qualification. It fixes the two shells first, applies the tensor and width estimates there, and then sums the shells using exponential decay.

In particular, it does **not** sum an undamped constant bound over arbitrarily many shells.

### 2.5 Hierarchy: feasible locally, not fully verified globally

The displayed ordering is locally feasible. For example, one can choose $h_H$ small relative to $\sigma$, then $h_*$ much smaller than $\sigma h_H$, and subsequently choose $A_0$ large enough for the path estimates.

Several requirements nevertheless depend on missing proofs:

- The initial choice of $\beta$ is supposed to absorb **absolute** coefficients in the foreign-child partition and distant-join costs.
- The choice of $s'$ precedes later tiny-power choices and therefore requires the relevant divisor-moment powers to be fixed independently of those choices.
- The non-clipping loss estimates must be independent of $N_0$.
- The conditional partition-jitter losses must be summable uniformly in the realized history.

These are genuine quantitative requirements. The supplied prose states them, but the absent partition and sparse sections are needed to validate them.

The colour selection has two distinct effects which must remain separate:

1. it retains only a fixed fraction of the block mass;
2. it separates distinct surviving bands.

It does not separate centres within one band, and it does not create independence between matchings or residue colours.

---

## 3. A deterministic single-prime transfer lemma with actual capacities

This section supplies a local result directly in the projected-table variables.

### 3.1 Exact product coupling

Fix one cell, one width, a prime power $p^\nu$, and one after-prime mask $a\mid I'$. Let


$$
\pi=\pi_{I'}(a),\qquad R_p=1-\frac1p.
$$



For a plus label $\xi$, define its residual-scaled raw weight


$$
P_\xi=R_p^{[\nu\ge2]}w_\xi^-.
$$


For a minus label $x$, write


$$
M_x=w_x^-.
$$


Set


$$
P=\sum_\xi P_\xi,\qquad M=\sum_xM_x.
$$



When $P,M>0$, the product coupling is


$$
\boxed{\quad
\mathfrak m_{x,\xi}
=\frac{M_xP_\xi}{\max(P,M)}.
\quad}                                                    \tag{3.1}
$$


When either total is zero, take all link masses to be zero.

Its capacities are exact:


$$
\sum_x\mathfrak m_{x,\xi}
=P_\xi\min\!\left(1,\frac MP\right)\le P_\xi,
$$




$$
\sum_\xi\mathfrak m_{x,\xi}
=M_x\min\!\left(1,\frac PM\right)\le M_x,
$$


and its total mass is $\min(P,M)$.

Thus the actual weighted capacity of a plus source is


$$
\boxed{\quad c_\xi=\pi P_\xi
=\pi_{I'}(a)R_p^{[\nu\ge2]}w_\xi^-.\quad}                    \tag{3.2}
$$


For an accounting class $A$, the actual incoming link weight from $\xi$ is


$$
\boxed{\quad
q_{\xi A}
=\pi\sum_{\substack{x\in A\\x\text{ linked to }\xi}}
\mathfrak m_{x,\xi}.
\quad}                                                    \tag{3.3}
$$


In particular,


$$
\sum_Aq_{\xi A}\le c_\xi.
$$



These are the cap weights used by the variance proof. Replacing them by arbitrary vertex weights would lose the connection to the table update.

### 3.2 Exact scalar transfer identity

Let $f$ be any real-valued test on the finite labelled configuration. A matched portion of raw size $m$ has weighted size


$$
\mu=\pi m.
$$


Its before-prime masses are $\mu/p$ at the plus endpoint and $R_p\mu$ at the minus endpoint. Its after-prime masses are $\mu S$ and $\mu(1-S)$, where $S$ is the actual plus-success indicator.

Therefore its contribution to the scalar change is exactly


$$
\mu(S-1/p)\bigl(f(\xi)-f(x)\bigr).
$$


An unpaired plus portion contributes $\mu(S-1/p)f(\xi)$; an unpaired minus portion contributes zero.

Consequently,


$$
\boxed{
\begin{aligned}
\Delta\!\left(\sum_z\lambda_zf(z)\right)
={}&
\sum_{\text{matched }(x,\xi)}
\pi\mathfrak m_{x,\xi}(S_\xi-1/p)
       \bigl(f(\xi)-f(x)\bigr)\\
&+\sum_{\text{unpaired plus }\xi}
\pi u_\xi(S_\xi-1/p)f(\xi).
\end{aligned}}                                             \tag{3.4}
$$



This identity is pointwise and deterministic. It does not assume independent successes.

Taking $f\equiv1$ cancels every matched transfer. The remaining unpaired-plus terms have zero orbit mean, proving first-mass preservation after summing complete translation orbits.

For a nonconstant scalar test, however, the factors $f(\xi)-f(x)$ remain. A mass capacity alone does not bound them.

### 3.3 Colour covariance, without independence

Suppose the test differences in (3.4) are constant under transported pre-$p$ configurations. Write the resulting signed coefficient of source $\xi$ as $b_\xi$.

Each source succeeds in one residue colour $c(\xi)\bmod p$. If


$$
B_c=\sum_{c(\xi)=c}b_\xi,
$$


then the exact orbit variance is


$$
\boxed{\quad
\mathbb E\left(\sum_\xi b_\xi(S_\xi-1/p)\right)^2
=\frac1p\sum_{c\bmod p}B_c^2
-\frac1{p^2}\left(\sum_cB_c\right)^2.
\quad}                                                    \tag{3.5}
$$



Indeed,


$$
\mathbb E(S_\xi S_\eta)
=\begin{cases}
1/p,&c(\xi)=c(\eta),\\
0,&c(\xi)\ne c(\eta).
\end{cases}
$$


This is exactly the colour dependence retained in the raw-covariance formula in `joins.tex`.

A useful warning follows immediately. If all positive coefficients have one colour and total $B$, then at that colour the fluctuation equals $R_pB$, whereas its variance is $R_pB^2/p$. Their ratio is


$$
\frac{(R_pB)^2}{R_pB^2/p}=p-1.
$$


There is no prime-uniform conversion of an orbit variance bound into a bound at one prescribed orbit position.

### 3.4 The rational height cost of product coupling

Suppose the residual-scaled endpoint weights are rational and have common denominator $D$:


$$
P_\xi=A_\xi/D,\qquad M_x=B_x/D.
$$


Put


$$
A=\sum_\xi A_\xi,\qquad B=\sum_xB_x.
$$


Then


$$
\mathfrak m_{x,\xi}
=\frac{A_\xi B_x}{D\max(A,B)}.                              \tag{3.6}
$$



Thus $D\max(A,B)$ is a simultaneous clearer for this link matrix. It is not necessarily the least one.

If both lists are capped by $N_0$, then


$$
\max(A,B)\le DN_0,
$$


so


$$
\log\operatorname{den}(\mathfrak m_{x,\xi})
\le2\log D+\log N_0.
$$


Including the mask coefficient gives the valid upper clearer


$$
I'D\max(A,B).
$$



This exhibits an important distinction:

- **Mass capacity:** no loss beyond the displayed endpoint capacities.
- **Rational denominator capacity:** a new integer $\max(A,B)$ can enter, with prime divisors unrelated to the current prime $p$.

The Family022 argument does not need to clear these rational weights into an integer linear form. An A3 transfer would need to pay that cost—or prove an actual cancellation removing it.

---

## 4. The variance ledger is a proved conditional lemma

The proof in `tables.tex` is sound under its structural hypotheses. Here is a precise version with an explicit constant.

### Proposition 4.1 — Deterministic history-preserving variance budget

Consider a finite chronology satisfying:

1. before each prime update, the labelled weights, links, and accounting classes are equivariant under the relevant pre-core translations;
2. each class has one width;
3. every class has weighted mass at most $N_0$;
4. prime updates satisfy the matching rule above;
5. thinning restricts classes without splitting their surviving equivalence relations;
6. coarsening only merges classes;
7. total first mass inserted at births is $M_{\rm birth}$.

Then


$$
J_p\ge0,\qquad K_p'\ge0,
\qquad
\boxed{\quad
\sum_p(J_p+K_p')\le3N_0M_{\rm birth}.
\quad}                                                    \tag{4.1}
$$



#### Proof

For an old class $A$, apply (3.4) with its indicator. Each portion contributes


$$
\mu\bigl(\mathbf1_{\{\xi\in A\}}-\mathbf1_{\{x\in A\}}\bigr)
(S_\xi-1/p),
$$


with the minus term omitted for an unpaired plus portion.

Because the old class and all pre-link data transport equivariantly, its post-mass $Y_A$ has orbit mean equal to its old mass $m_A$. Summing over the complete set of old classes,


$$
J_p
=\sum_A r_A\bigl(\mathbb EY_A^2-m_A^2\bigr)
=\sum_A r_A\operatorname{Var}(Y_A)\ge0.
$$


Stabilizers merely repeat orbit elements equally and do not alter the identity.

Merging classes increases the sum of squared masses, so $K_p'\ge0$.

If a discard removes class mass $d_A$, its accounting-energy loss is


$$
r_A\bigl(m_A^2-(m_A-d_A)^2\bigr)
=r_A(2m_Ad_A-d_A^2)
\le2N_0r_Ad_A.
$$


There is no additional splitting loss by hypothesis.

Prime updates preserve first mass. Hence the total discarded first mass is at most $M_{\rm birth}$, and the final accounting energy is at most $N_0M_{\rm birth}$.

Writing $I_{\rm birth}\ge0$ for the accounting energy inserted at births and $D_{\mathcal A}$ for total discard loss,


$$
\mathcal A_{\rm final}
=I_{\rm birth}+\sum_p(J_p+K_p')-D_{\mathcal A}.
$$


Therefore


$$
\sum_p(J_p+K_p')
\le N_0M_{\rm birth}+2N_0M_{\rm birth}.
$$


This proves (4.1). ∎

### What remains conditional here?

The ledger does not construct classes satisfying its hypotheses.

In particular:

- A later partition must preserve an old equivalence class even if an intermediate connecting label has died.
- The class must remain inside a cell.
- One new cell must not combine several old cells of the same child in a way that invalidates the inherited cap.
- The selected nonexceptional tight pairs must permit the prescribed coarsening.

These are precisely the responsibilities of the missing sparse and partition sections. They cannot be inferred from the nonnegativity of $J_p$.

The source’s broad-energy proof correctly uses the sparse input separately to pay:

- unrestricted $1/p^2$ terms;
- successful pairs outside the tight range;
- exceptional tight pairs.

The variance budget pays the remaining history-sensitive self cost. It is not a replacement for those sparse estimates.

---

## 5. Explicit deterministic arithmetic behind the first-join roundoff

The following calculations close two local arithmetic steps in the supplied discussion.

### 5.1 An exact finite gcd-mask sum

Let $\mathcal Q$ be any finite set of processed primes. Restrict $d,e$ to divisors of the $\mathcal Q$-parts of $L,M$. Set


$$
G=(L,M),\qquad U=L/G,\qquad T=M/G.
$$



At one prime write


$$
\nu_p(L)=b+h,\qquad \nu_p(M)=b,\qquad h\ge0.
$$


For deficits $j,k$, the local factor in


$$
\frac{(Td,Ue)}{de}
$$


is


$$
p^{\min(j,h+k)-j-k}.
$$



Its exact finite sum is


$$
\boxed{\quad
\sum_{j=0}^{b+h}\sum_{k=0}^{b}
p^{\min(j,h+k)-j-k}
=\sum_{k=0}^{b}(h+2k+1)p^{-k}.
\quad}                                                    \tag{5.1}
$$



To verify this, fix $k$. The terms $j\le h+k$ contribute


$$
(h+k+1)p^{-k}.
$$


The remaining terms contribute


$$
\sum_{t=k+1}^{b}p^{-t}.
$$


Summing the latter over $k$ gives $\sum_{t=1}^{b}tp^{-t}$, proving (5.1).

In particular,


$$
\sum_{k=0}^{b}(h+2k+1)p^{-k}
\le(h+1)(1+10/p).                                         \tag{5.2}
$$



The omega factor used in `joins.tex` can also be retained. At $h=0$, all terms except $(j,k)=(0,0)$ have total unweighted size $O(1/p)$, and multiplication by $2^{[j>0]+[k>0]}$ costs at most four. At $h\ge1$, the nondecaying terms have weighted total $1+2h\le(h+1)^2$. Hence


$$
\sum_{j,k}
2^{[j>0]+[k>0]}p^{\min(j,h+k)-j-k}
\le(h+1)^2(1+40/p).
$$


Euler multiplication gives the concrete bound


$$
\boxed{
\sum_{d,e}
2^{\omega(d)+\omega(e)}
\frac{(Td,Ue)}{de}
\le
\tau(UT)^2
\exp\!\left(40\sum_{\substack{p\in\mathcal Q\\p\mid LM}}\frac1p\right).
}                                                         \tag{5.3}
$$



All finite exponent boundaries are retained in (5.1). Good-mask or assignment restrictions only reduce the nonnegative sum.

Independent outer laws and one common outer law remain distinct. After restrictions have legitimately been dropped, either is a probability law, so averaging (5.3) against it does not enlarge the bound. This does not authorize replacing a one-law coefficient by its square.

### 5.2 Exact target-grid relative sum

Let $V$ be a positive integer and define


$$
E=\frac{V}{(V,L)}.
$$


At a prime, write


$$
a=\nu_p(L),\qquad b=\nu_p(V),\qquad h=(a-b)_+.
$$


After factoring out the local contribution of $E^{-1}$,


$$
\frac{(V,L/d)}V
=E^{-1}\prod_p p^{-(\nu_p(d)-h_p)_+}.
$$



Thus the unweighted local deficit sum is exactly


$$
\boxed{\quad
\sum_{j=0}^{a}p^{-(j-h)_+}
=h+1+\sum_{t=1}^{a-h}p^{-t}.
\quad}                                                    \tag{5.4}
$$


With a factor $2^{[j>0]}$, it is at most


$$
(h+1)^2(1+4/p).
$$



In the mixed-join application $V=M/c$, and


$$
h_p\le\nu_p(U)+\nu_p(c).
$$


Therefore


$$
\boxed{
\sum_{d}
2^{\omega(d)}\frac{(V,L/d)}V
\le
E^{-1}\tau(U)^2\tau(c)^2
\exp\!\left(4\sum_{\substack{p\text{ processed}\\p\mid L}}\frac1p\right).
}                                                         \tag{5.5}
$$



A factor depending on $\omega(c)$ is absorbed by one additional divisor power. This explicitly justifies the arithmetic shape of the source’s mixed relative-error bound.

### 5.3 Height payment for distant roundoffs

Suppose a roundoff majorant has already been proved in the form


$$
C\Theta_{ij}\tau(UT)^C
\exp(\epsilon H+C_\Sigma\Sigma),
\qquad
H=B_i+B_j+\log(2UT).
$$


The preceding calculation shows why the coefficient of the harmonic sum can be absolute.

For $u=3/4$, the centre lower bounds give


$$
\Theta_{ij}
\ll
(m_Lm_M)^{3/4}(UT)^{-1/2}
\left(\frac{r_{\min}}{r_{\max}}\right)^{1/2}
e^{.49(B_i^*+B_j^*)}.
$$


At height $Y$,


$$
B_i^*,B_j^*<2Y/A_0,
$$


so the shell-conversion cost is at most $e^{1.96Y/A_0}$.

Use


$$
\tau(UT)^C\ll_\eta(UT)^\eta.
$$


Reserve the factor $(UT)^{-1/16}$. On distant pairs,


$$
\log(UT)>\beta Y/2,
$$


and hence


$$
(UT)^{-1/16}\le e^{-\beta Y/32}.
$$


The remaining tensor exponent is


$$
s=\frac12-\epsilon-\eta-\frac1{16}.
$$


For $\epsilon+\eta<1/16$, this exceeds $3/8$, and therefore exceeds $1-u=1/4$.

Since the elementary prime bounds give $\Sigma\le C_HY+O(1)$, a sufficiently large fixed $\beta$ leaves exponential decay in $Y$. Tensor summation, dyadic-width convolution, and the $O((Y+1)^2)$ shell-pair count then give


$$
O(W^{3/2}).
$$



This is a rigorous deterministic summation **conditional on the displayed per-pair roundoff majorant**. It does not prove that majorant for an arbitrary history.

### 5.4 Height payment for mixed roundoffs

Suppose the mixed classification and its good-mask hypotheses hold. If the width-separated alternative fails, exterior separation gives


$$
\frac{v}{(v,L)}\frac{r_j}{r_{\min}}>e^{.015B_j^*}
$$


for every assigned true denominator $v$ of the newborn centre.

Since $v\mid V=M/c$,


$$
\frac{V}{(V,L)}\ge\frac{v}{(v,L)}.
$$


Thus the geometric factor in (5.5) satisfies


$$
\frac{r_{\min}}{r_j}\frac{(V,L)}V
<e^{-.015B_j^*}.                                         \tag{5.6}
$$



The remaining costs have the form


$$
e^{\epsilon H+C\Sigma}\tau(U)^C\tau(c)^C.
$$


Under


$$
H=O(\beta A_0B_j),\qquad
\Sigma\le s_{\rm low}B_j,\qquad
\tau(c)\le e^{s'B_j},
$$


one may choose the fixed small exponents so that these costs are at most


$$
e^{.005B_j^*}.
$$


This leaves $e^{-.01B_j^*}$.

If colour separation gives $B_i\le B_j/M_{\rm col}$, the adjusted-centre count bounds the number of possible old centres by


$$
O(e^{4B_j/M_{\rm col}}).
$$


For example, $M_{\rm col}\ge800$ leaves an exponential saving after this count.

This verifies the quantitative shape of the oriented $O(W)$ argument. Its unresolved hypotheses are the mixed classification in the actual construction and the good-mask divisor bound—not the elementary divisor sum itself.

---

## 6. Audit of the first-join proof

### 6.1 What the backward calculation genuinely proves

The raw covariance identity is exact:


$$
w_x^+
=R_pw_x^-
-\sum_\xi\mathfrak m_{x,\xi}(I_\xi-1/p),
$$


and consequently


$$
\begin{aligned}
\mathbb E(w_x^+w_y^+)
={}&R_p^2w_x^-w_y^-\\
&+\sum_{\xi,\eta}
\mathfrak m_{x,\xi}\mathfrak m_{y,\eta}
\left(\mathbb E(I_\xi I_\eta)-p^{-2}\right).
\end{aligned}
$$


The proof correctly retains the actual raw prefixes and raw link masses. It does not multiply link fractions by an artificially enlarged prefix.

Stopping each joint-loss branch at its splitting prime also avoids recursively charging the same covariance through later adaptive expansions.

### 6.2 Later omissions: exact, but hypothesis-sensitive

The factor $1/b_i^+$ is justified only after all of the following have been established:

- the branch has not stopped at a larger bad omission;
- the partner is full at each later-omission prime;
- the relevant centre exponents agree there;
- pre-$p$ links and retained static fields are invariant under the indicated translations;
- adaptive good masks have deficit at most one at those primes.

Under these hypotheses, the numerator congruence on the **original minus grid** averages to $1/l$ at each later omitted prime $l$, while the broadened image-distance predicate is invariant. The factor is not a success probability on the linked image grid.

The proof distinguishes these two grids correctly.

### 6.3 Capacity and one-law accounting

For fixed successful image labels and preserved later-mask data,


$$
\sum_x\mathfrak m_{x,\xi}\le w_\xi
$$


is the actual matching-column bound. Hence, for a common outer mask,


$$
\pi_I(a)c_\xi c_\eta
\sum_{x,y}\mathfrak m_{x,\xi}\mathfrak m_{y,\eta}
\le
\pi_I(a)c_\xi c_\eta w_\xi w_\eta.
$$


There is exactly one $\pi_I(a)$ on each side.

The claim of no extra origin-mask multiplicity is valid provided the labels retain the entire assigned row and future mask. Erasing that history would invalidate the argument.

The unique comparison-epoch claim also requires the component history: the earlier component of an image must remain inside the corresponding old child. This is a structural hypothesis, not a consequence of the numerical column capacity.

### 6.4 What remains unproved in this packet

The remaining-first-join proposition depends on:

- birth weights and hard means from the missing prescriptions section;
- good-mask reciprocal and divisor-moment purges;
- the direct birth comparisons and additional hole test;
- the actual chronological partitions and their span properties;
- sparse-history equivariance and the stored danger-train construction.

The closure paragraph says these are established in other sections. That statement is not a proof of them in the supplied packet.

Accordingly, the correct status is:

> The packet proves several first-join mechanisms and conditional estimates. It does not yet prove the full first-sharing input for the actual selected tables.

This is not a disproof of the full paper. It is a precise limitation of the evidence supplied here.

---

## 7. The conditional finite-block reduction

The final measure-theoretic reduction is logically sound assuming its inputs.

Its parameter order is important:

1. fix the avoided-set measure $\mu$;
2. fix the hierarchy, selection fraction, and hard-mean constant;
3. choose $k_0,\lambda_0,w$ in the stated order;
4. choose $N_0$ after the clipping constants;
5. obtain a uniform $L^2$ bound;
6. only then approximate the avoided set by one fixed finite union of intervals;
7. finally pass sufficiently far down the block tail for uniform virtual equidistribution.

The soft loss is compared with the expected virtual mass $V$, rather than with a lower bound whose dependence might force a circular parameter choice. That correction is mathematically significant.

The passage from point arrays to interval trains also preserves the mass convention: half-width $r(v)/2$ gives interval length $r(v)$.

No step here turns a null-set conclusion into a statement about a prescribed scalar. That deterministic limitation is already established and need not be repeated as the entire audit.

---

## 8. Can these lemmas constrain the actual A3 projected scalar?

### 8.1 The missing bridge is an exact representation

The local identity (3.4) applies to an actual table statistic


$$
\sum_x\pi_I(a_x)w_x f(x).
$$


To constrain an A3 projected residual, one must first prove an identity of this kind for that residual, with:

- the actual finite index set;
- the complete forced source;
- the actual projection coefficients;
- the omitted-column correction at $j=0$;
- the physical terminal contribution;
- every factorial and rational normalization.

No such identity is supplied.

The similarity of words such as “projection,” “capacity,” or “exterior” does not provide this representation.

### 8.2 The precise deterministic obstruction

Even if such a representation were obtained, (3.4) shows the outstanding quantity:


$$
f(\xi)-f(x)
$$


on every matched portion, together with $f(\xi)$ on every unpaired plus portion.

A deterministic bound follows from Cauchy–Schwarz:


$$
|\Delta\mathcal L_f|^2
\le
\left(\sum_\rho\mu_\rho(S_\rho-1/p)^2\right)
\left(\sum_\rho\mu_\rho|D_\rho f|^2\right),                 \tag{8.1}
$$


where $D_\rho f$ is the matched difference or the unpaired value.

The second factor is an actual weighted oscillation cost. Neither the cap $N_0$, the centre-density bound, nor the variance ledger controls it for an arbitrary scalar covector.

This is consistent with the earlier diagonal-graph obstruction: upper capacities alone do not force a scalar saving. The previously established rough-integer totient estimate likewise does not identify the scalar coefficients or pay their denominators.

### 8.3 Concrete follow-on lemma

A useful next lemma would have the following form.

> **Actual projected-transfer lemma.** For infinitely many original A3 indices, represent the complete projected scalar by a finite labelled transfer system satisfying the structural hypotheses above. Prove, for its actual coefficients, a bound on the right-hand side of (8.1), including every unpaired contribution and every boundary correction. Then bound the actual least simultaneous clearer and final all-prime gcd so that the resulting whole integer-form error tends to zero and is nonzero.

This is more specific than requesting “better overlap control.” It isolates two objects that must be evaluated:

1. the weighted oscillation of the actual projected covector;
2. the arithmetic denominator introduced by the actual transfer weights.

The height calculation (3.6) shows why the second obligation cannot be omitted.

### 8.4 Primitive payment remains unchanged

The archived A3 denominator accounting contains


$$
\frac{|R_j|}{\gcd(R_j,C_j)}
\frac{n!}{\gcd(n!,\zeta_j)}
$$


and the additional retained $F$-payment. The full formulas are not supplied here, so they must not be simplified or replaced.

After all actual rational quantities have been cleared, if the integer form is


$$
Q_n^{\rm raw}(e+\pi)-P_n^{\rm raw},
$$


then the primitive pair uses


$$
g_n=\gcd\!\left(|P_n^{\rm raw}|,|Q_n^{\rm raw}|\right)
$$


over **all primes**. Its whole error is divided by that same $g_n$.

A useful irrationality sequence still requires


$$
0<
\left|q_n(e+\pi)-p_n\right|
\longrightarrow0
$$


on one and the same infinite set of original indices. A local content gain, a raw denominator estimate, or a small isolated residual does not establish this condition.

---

## 9. Proof-dependency ledger

| Claim | Status from this packet | Essential remaining dependency |
|---|---|---|
| Small-width and finite-block reductions | Proved | None beyond stated elementary hypotheses |
| Deficit law and determinant-cycle averaging | Proved | Correct separate treatment of numerator residues |
| One-coordinate and tensor kernels | Proved at stated scope | None for their present applications |
| Original-host density and adjusted-host bounds | Proved | Original assigned families must be retained in the notation |
| Shell counts, purge, exterior separation | Proved | Fixed colour separation and small $k_0$ |
| Width/height kernel summation | Proved | Lower densities are pre-thinning densities |
| One-prime cap and mass preservation | Proved conditionally on equivariant cells and links | Actual partition construction |
| Exact transfer identity (3.4) and capacities (3.2)–(3.3) | Proved here | No scalar application yet |
| Rational coupling-height bound | Proved here | Actual cancellation/least-clearer analysis for any application |
| Variance budget $3N_0M_{\rm birth}$ | Proved here under explicit structural hypotheses | History-preserving partitions and birth mass bound |
| Explicit gcd-mask sums (5.1)–(5.5) | Proved here | None within their finite domains |
| Distant/mixed roundoff summation | Proved conditional on stated per-pair majorants and good-mask hypotheses | Birth/direct/partition inputs |
| Backward covariance and local charge capacity | Proved under stated history and mask hypotheses | Their validation in missing construction sections |
| Complete first-sharing input | Not established by packet | Prescriptions, direct comparisons, partitions |
| Sparse-alignment input | Stated, not proved here | Missing sparse section |
| Chronological partition input | Stated, not proved here | Missing partition section |
| Virtual marginals and equidistribution | Conditional proof supplied | Actual birth prescriptions and structural history |
| Finite-block contradiction | Valid conditional deduction | All construction inputs |
| Hausdorff consequence | Not audited as a complete proof | Missing consequences section and its precise transfer application |
| Application to A3 primitive scalar sequence | Open | Exact representation, paid denominator, nonzero whole error |
| Irrationality or rationality of $e+\pi$ | Unresolved | Same-index infinite integer-form criterion |

---

## 10. Bounded exact arithmetic check for independent inspection

No computation has been executed. The following small rational check is sufficient to verify the new local formulas independently. It is an auxiliary algebra check, not an original A3 computation and not a substitute for the missing proof sections.

### Inputs

Take


$$
p=3,\qquad \nu=2,\qquad I'=5,\qquad a=1,\qquad
\pi_{5}(1)=\frac45,\qquad N_0=2.
$$


Use before-prime raw weights


$$
(w_{\xi_1}^-,w_{\xi_2}^-)=(1,1/2),
\qquad
(M_{x_1},M_{x_2})=(1,1/3).
$$


The residual-scaled plus weights are


$$
(P_{\xi_1},P_{\xi_2})=(2/3,1/3).
$$



For the three orbit colours $g=0,1,2$, set


$$
S_{\xi_1}(g)=\mathbf1_{\{g=0\}},
\qquad
S_{\xi_2}(g)=\mathbf1_{\{g=1\}}.
$$


Take classes


$$
A=\{\xi_1,x_1\},\qquad B=\{\xi_2,x_2\}.
$$



### Expected verifiable outputs

1. **Product coupling**
   

$$
(\mathfrak m_{x_i,\xi_j})
   =
   \begin{pmatrix}
   1/2&1/4\\
   1/6&1/12
   \end{pmatrix}.
$$


   Its column sums are $2/3,1/3$, and its row sums are $3/4,1/4$.

2. **Raw cap**
   The post-update raw load is $11/9<2$ for each of the three colours.

3. **Weighted mass**
   The total before and after weighted mass is $44/45$.

4. **Class fluctuations**
   The old class masses are $32/45$ and $12/45$. The three fluctuations of class $A$ are
   

$$
\frac7{45},\quad-\frac8{45},\quad\frac1{45},
$$


   and those of $B$ are their negatives.

5. **Variance**
   The sum of the two orbit-averaged class variances is
   

$$
\frac{76}{2025}.
$$



6. **One-law versus product-law capacity**
   For the pair $(\xi_1,\xi_1)$, the one-law capacity is
   

$$
\frac45\left(\frac23\right)^2=\frac{16}{45},
$$


   while the product-law capacity is
   

$$
\left(\frac45\right)^2\left(\frac23\right)^2
   =\frac{64}{225}.
$$


   They are not interchangeable.

7. **Actual least clearers**
   The raw link matrix has least simultaneous clearer $12$. After multiplication by $4/5$, its least simultaneous clearer is $15$, not the unreduced upper clearer $60$.

All inputs and expected outputs are finite rational numbers.

---

## 11. Final conclusion

The new proved contribution is a deterministic local package:

- exact actual-weight matching capacities;
- an exact scalar transfer identity;
- an explicit rational-height cost for product coupling;
- the sharpened variance budget $3N_0M_{\rm birth}$;
- exact finite gcd-mask sums and their height-decay consequences.

This package validates substantive parts of the supplied Family022 mechanism. It also identifies exactly where history, colour dependence, common-mask accounting, and denominator clearing enter.

The remaining primary-proof bottleneck is the validation of the sparse-alignment and chronological-partition constructions, together with the missing birth/direct hypotheses used by first joins.

The remaining A3 bottleneck is different and more arithmetic:

> Prove an exact transfer for the complete actual projected scalar, control its matched and unpaired oscillation costs, and obtain the actual all-prime primitive denominator together with a nonzero whole error tending to zero on the same infinite original indices.

The bounded check above can verify the local algebra. It cannot settle either infinite bottleneck, and the unconditional status of $e+\pi$ remains unresolved.
