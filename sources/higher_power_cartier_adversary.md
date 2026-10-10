> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Higher-prime-power Cartier continuation: adversary audit

Date: 2026-08-28

## Verdict

**PROVED.** None of frozen items 149--153 supplies a $p^2$-lift of the
Cartier content divisor.  The most natural lifts are false for the actual
coordinates, not merely unproved: a top layer $q=p^2$, a first-Cartier
rank-zero row followed by the item-149 rank-one mechanism, and a vanishing
item-151 rank-two determinant can all leave



$$
v_p(c_m)=1
$$



exactly.  The only generally valid local upper bound presently available is
the height bound (and the exact valuation identity below); mod-$p$ Cartier
rank data alone admits arbitrarily large lift valuation and hence gives no
finite upper bound.

The matching ledger $c_m\Delta_m g_m$ is exact when its three factors are
formed **sequentially in the frozen normalization**.  The same prime may
legitimately occur in all three factors.  It is nevertheless a normalization
error to compute $\Delta_m$ from the raw coordinate $V_m$, or to regard
the three occurrences as independent Cartier gains.

Standard Dwork/Hasse--Witt inversion does not repair this gap.  The relevant
Cartier comparison matrix is singular exactly where the argument needs a
lift, so the usual invertibility hypothesis is unavailable.  It is **OPEN**
whether a separately constructed higher Frobenius crystal for these
high-pole relative forms yields additional information.  It is not justified
to identify the rank-defective comparison matrix with the ambient
Hasse--Witt matrix.

## Frozen normalization and theorem boundary

**PROVED.** The actual coordinates audited here are



$$
X_m=D_m^\sharp A_m,\qquad Y_m=D_m^\sharp B_m,
\qquad U_m=X_m/G_m,\quad V_m=Y_m/G_m,
$$





$$
c_m=\gcd(U_m,V_m),
$$



where $G_m$ is the already removed **squarefree** rank-zero Cartier
product.  Equivalently, with the integral raw coordinates of the frozen
actual-coordinate audit,



$$
\begin{aligned}
v_p(U_m)&={\bf1}_{p=2}+v_p(\widehat A_m)-v_p(T)-v_p(G_m),\\
v_p(V_m)&=v_p(K)+v_p(\widehat B_m)-v_p(G_m),\\
v_p(c_m)&=\min\{v_p(U_m),v_p(V_m)\}.                 \tag{1}
\end{aligned}
$$



Item 149 proves one surviving copy of each $p\in\mathcal H_m$, including
the case $p\in\mathcal P_m$ where one earlier copy has already been divided
out through $G_m$.  Item 151 proves one surviving copy at each vanishing
rank-two determinant.  Both statements explicitly stop at squarefree
divisibility.  Items 150 and 152 concern slope-10 determinant nonvanishing
(with item 152's 2-adic pattern still finite/conjectural); they do not assert
odd $p^2$-content.  Item 153 reduces the corrected m-ray obstruction back to
the old pair up to powers of two; its scaled-gcd-divides-$(6m)!$ observation
through $m=1000$ is finite evidence and supplies no valuation theorem.

## Exact counterexamples to natural lifts

### 1. Top prime-power layer does not count $p$-adic digits

**PROVED (exact actual-coordinate counterexample).** At $m=3,p=3$, the
item-149 top layer is $q_p=9=p^2$, and $p\in\mathcal H_3$.  The frozen
coordinates are



$$
U_3=-6381983278607499264,
\qquad V_3=2031448371040408320,
\qquad c_3=9984.
$$



Exact division gives



$$
(v_3(U_3),v_3(V_3),v_3(c_3))=(1,3,1).             \tag{2}
$$



Thus each of the implications



$$
q_p=p^{e_p}\hbox{ is used }\Longrightarrow p^{e_p}\mid c_m,
\qquad
e_p\ge2\Longrightarrow p^2\mid c_m
$$



is false.  The iterate $\mathcal C^{e_p}$ detects the $p^{e_p}$
denominator layer **modulo $p$**; it is not a congruence modulo
$p^{e_p}$.

### 2. The already removed $G_m$-digit cannot be counted again

**PROVED (exact actual-coordinate counterexample).** At $m=9,p=13$, the
prime is first-Cartier rank zero and belongs to $G_9$.  With
$X_9=G_9U_9,\;Y_9=G_9V_9$, exact valuations are



$$
(v_{13}(G_9),v_{13}(X_9),v_{13}(Y_9))=(1,2,3),
$$



but after the required squarefree division,



$$
(v_{13}(U_9),v_{13}(V_9),v_{13}(c_9))=(1,2,1).       \tag{3}
$$



Here



$$
c_9=1215352320.
$$



Consequently “one old rank-zero digit plus one item-149 digit” means one
digit in $G_m$ and one in the post-$G_m$ content; it does **not** mean
$p^2\mid c_m$.

### 3. A zero rank-two determinant need not lift to $p^2$

**PROVED (exact actual-coordinate counterexample).** At $m=4,p=7$, the
item-151 rank-two coefficient determinant is zero modulo $7$.  Nevertheless



$$
(v_7(U_4),v_7(V_4),v_7(c_4))=(1,2,1),
\qquad c_4=205632.                                      \tag{4}
$$



Therefore $\Delta_{q,s}=0\pmod p$ does not imply
$p^2\mid c_m$.  It certifies precisely the one squarefree copy stated in
item 151.

### 4. Finite prevalence (diagnostic only)

**EXPERIMENTAL (exact finite diagnostic; not asymptotic).** Among the 986
item-149
forced-prime rows in the $m\le100$ scan plus the $m=150,200$ probes, 772
have $v_p(c_m)=1$ exactly.  Among the 124 vanishing item-151 rank-two rows,
65 have $v_p(c_m)=1$ exactly.  This is not an asymptotic frequency claim;
it only shows that failure of the $p^2$-lift is common in the certified
window.

## $c_m,\Delta_m,g_m$: sequential ledger, overlap, and a normalization trap

Let the primitive positive period form after content division be



$$
L_m=a_m+\varepsilon_m b_m\pi,
\qquad b_m=|V_m|/c_m,qquad \gcd(a_m,b_m)=1.
$$



For the beta pair $(p_N,q_N)$, the frozen definitions are



$$
\Delta_m=\gcd(b_m,q_N),\qquad b_m=\Delta_m b_0,
\quad q_N=\Delta_m q_0,
$$





$$
P^*=b_0p_N-\varepsilon_mq_0a_m,
\qquad g_m=\gcd(P^*,\Delta_m).                         \tag{5}
$$



**PROVED (normalization counterexample).** At $m=6,N=4$,



$$
(p_4,q_4)=(2721,1001),\qquad c_6=3060288000,
$$



and the primitive coefficients are



$$
a_6=-4963607491493737684466139136,
$$





$$
b_6=1579965335678382366167848485.
$$



The correct sequential computation gives



$$
\Delta_6=\gcd(b_6,1001)=91,
$$





$$
P^*=101842382168858349895531000031,
\qquad g_6=7.                                           \tag{6}
$$



In contrast, using the raw coordinate before division by $c_6$ gives



$$
\gcd(|V_6|,q_4)=1001\ne91.                              \tag{7}
$$



Thus (7) overstates the matching gcd by the factor $11$, which has already
been consumed by $c_6$.

**PROVED (overlap is real but not double counting).** In the same example,



$$
(v_7(c_6),v_7(\Delta_6),v_7(g_6))=(1,1,1).              \tag{8}
$$



The factor $7^3$ in $c_6\Delta_6g_6$ is legitimate: $c_6$ first
primitive-reduces the original period pair, $\Delta_6$ then minimally
matches the beta and period coefficients, and $g_6$ finally
primitive-reduces the matched pair.  Relative to the naive raw coefficient
$|V_6|q_4$, these are three distinct sequential cancellations.  What is
invalid is to treat them as probabilistically independent, or to compute any
later factor from the earlier, unnormalized coordinates.

The equal-valuation theorem remains essential:



$$
v_p(g_m)>0\Longrightarrow
v_p(b_m)=v_p(q_N)>0.                                    \tag{9}
$$



Merely knowing $p\mid c_m$, $p\mid V_m$, or $p\mid\Delta_m$ does not
establish a $g_m$-gain.

## What can and cannot upper-bound $v_p(c_m)$

**PROVED.** Equation (1) is the exact local answer.  In particular,



$$
v_p(c_m)\le v_p(U_m),\qquad v_p(c_m)\le v_p(V_m),       \tag{10}
$$



with the right sides given by the actual raw-coordinate formula (1).  If
both coordinates are nonzero, the elementary height bound is



$$
v_p(c_m)\le
\left\lfloor{\log\min(|U_m|,|V_m|)\over\log p}\right\rfloor.   \tag{11}
$$



The frozen irrationality-measure argument also proves



$$
\limsup_m {\log c_m\over6m}\le1.99566316016\ldots,
$$



and hence, for each fixed prime,



$$
v_p(c_m)\le
{(11.97397896096\ldots+o(1))m\over\log p}.              \tag{12}
$$



This is rigorous but far too weak: it permits linearly many digits at every
fixed small prime.

**PROVED (Cartier-data no-go).** No upper bound follows from mod-$p$
rank-one data alone.  For every $r\ge1$, the two lifted triples



$$
(qR_0,L_0,E_0)=(1,1,1),
\qquad(qR_1,L_1,E_1)=(1+p^r,1,1+p^r)
$$



have the same nonzero proportional reduction modulo $p$, while both
relevant minors have valuation exactly $r$.  Thus the same Cartier rank
datum is compatible with arbitrarily large determinant valuation.  Any
useful actual upper bound must use integral lift information about
$\widehat A_m,\widehat B_m$, not just the first Cartier/Hasse--Witt rank.

**OPEN.** No frozen item proves a uniform bound such as
$v_p(c_m)=O(\log_p m)$, nor a total small-prime multiplicity estimate strong
enough to make the remaining prime-power mass $o(m)$.

## Dwork / higher-Hasse--Witt assessment

**PROVED (applicability boundary).** The pole polynomial has



$$
\operatorname{disc}Q=-16,
$$



so for every odd $p$ in items 149 and 151 the pole divisor remains
separable.  The observed rank defect is therefore not degeneration of the
ambient pole geometry.  It is a rank defect of the selected Cartier images
of the two high-pole differentials (or of their endpoint comparison minors).

If the item-151 $2\times2$ coefficient matrix is used as the candidate
Hasse--Witt matrix, its determinant is $\Delta_{q,s}$; on the content locus
it is singular by definition.  In the item-149 region the two images already
lie in one line, and on the rank-zero locus both vanish.  Hence any standard
Dwork step that requires inversion of this matrix is unavailable at exactly
the rows where a higher digit is sought.

**OPEN / NO IDENTIFICATION THEOREM.** It would be too strong to say that the
*ambient* Hasse--Witt operator fails precisely on the content locus.  The
frozen notes do not construct a smooth proper family or an integral
Frobenius-stable lattice whose Hasse--Witt matrix is the above comparison
matrix.  These are rational differentials on a fixed separable pole
configuration, with pole order and normalization varying with $m$.  The
ambient cohomology may remain ordinary while this chosen two-section
projection loses rank.  Conversely, a singular comparison minor need not be
equivalent to $p\mid c_m$ without the endpoint congruence and denominator
ledger.

Higher Hasse--Witt matrices could in principle measure the order of this
singularity, but that requires new modulo-$p^2$ (or crystalline) lift data.
First-level singularity supplies no inverse and, by the exact counterexamples
(2)--(4), supplies no automatic second digit.

## Reproduction and pinned inputs

Run

```text
python scripts/higher_power_cartier_adversary_check.py
```

The checker is read-only with respect to the Desktop archive.  It pins and
replays these frozen inputs:

```text
7284ea76cef084e7cb0faeba172454ebe2825a9dd60682c7d1b91c3f78852e96  mixed_cubic_positive_match_exact_scan_m100_N6m.json
10991033ef60dece85f588cdc676a29bd5d1503ad2a28eb718c020f81dbdd6c3  mixed_cubic_small_prime_rank_one_cartier_certificate.json
1fbc73c50ca83cdbbabef090460a944218dc1074a573b32555e4a009f2cb1b02  mixed_cubic_rank_two_cartier_certificate.json
```

The finite counts are diagnostics only; equations (1)--(12) and the
normalization/Dwork boundaries are exact deductions.
