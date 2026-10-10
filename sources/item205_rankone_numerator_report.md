> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 205 — localized Smith content of the all-moving rank-one gates

Date: 2026-08-30

## 1. Scope and verdict

This item continues Route 1 from Item 196.  It keeps the two first gates
(A_0,B_0) separate from the second-lift digit (A_1), and it does not infer
modular nonvanishing from a characteristic-zero sign.

Put



$$
k=3s+2,qquad M_k=\operatorname {lcm}(1,\ldots ,k).
$$



Let (G_s=B_s/u^k) be Item 196's normalized rational primitive and write



$$
V_{s,1}(-1)=a_s,qquad V_{s,1}(i)=b_s+ic_s,qquad
 a_s,b_s,c_s\in\mathbb Q.                              \tag{1.1}
$$



The main conclusions are the following.

**PROVED — three-coordinate and Frobenius-swap reduction.**  The complete
moving input is the rational vector ((a_s,b_s,c_s)).  The two residue
classes use



$$
(a_s,b_s,c_s)\quad(\rho=1),qquad
 (a_s,c_s,b_s)\quad(\rho=3).                           \tag{1.2}
$$



Thus the two Gaussian entries do not create six independent moving
coordinates.

**PROVED — exact localized Smith-content theorem.**  Define



$$
\Lambda_s=2^{k-1}M_k,qquad
 X_s=\Lambda_sa_s,qquad
 Y_s+iZ_s=\Lambda_sV_{s,1}(i),                         \tag{1.3}
$$



and



$$
h_s=\gcd(X_s,Y_s,Z_s).                                \tag{1.4}
$$



The three entries in (1.3) are integers.  For every odd prime (p>k),



$$
\boxed{
 v_p(h_s)=\min\{v_p(g_0(s)),v_p(g_1(s))\}.}            \tag{1.5}
$$



In fact (1.5) holds at every power (p^e), not just at the radical level.
Consequently the admissible-prime part of the common moving content is
exactly the admissible-prime part of the smaller integer



$$
\delta_s=\gcd(g_0(s),g_1(s)).                         \tag{1.6}
$$



Every prime in this content forces both (A_0) and (B_0) to vanish for
every admissible (j).  This isolates one genuine arithmetic source of
moving zeros.

**PROVED — an infinite but zero-rate resonance ray.**  If



$$
s\equiv3\pmod4,qquad p=5s+4\ \hbox{is prime},         \tag{1.7}
$$



then (p\mid\delta_s), hence the entire moving vector and both first gates
vanish modulo (p).  On a cell row



$$
2m+1=(j+1)p-s,
$$



equation (1.7) gives



$$
10m+1=(5j+4)p.                \tag{1.8}
$$



Therefore, for fixed (m), the log-prime weight of every row on this ray is
at most (log(10m+1)=O(log m)).  The ray is infinite by Dirichlet's
theorem, but it has zero Route-1 rate and supplies no new positive-mass
content.

**PROVED — scoped height and local-resultant obstructions.**  One has



$$
\delta_s\le g_1(s)\le4^{5s+2}.                        \tag{1.9}
$$



This bounds the number of admissible prime divisors on one frozen
(s)-fiber by (O(s/\log s)), but it gives no sublinear count as (s)
moves through (0\le s\le(p-3)/3).  A precise height-envelope countermodel
in Section 7 permits (p/3-O(\log p)) roots.  It is a countermodel only to
the height inference, not to the actual coefficient recurrence.

The exact coefficient transfer also has determinant zero at its unique
central step.  Common terminal zeros leave a one-dimensional survivor, so
the naive local transfer determinant/resultant is identically unable to
remove the moving gcd.  This is a scoped no-go for that eliminant, not for a
global arithmetic argument using the fixed initial state.

**OPEN.**  No uniform sublinear count is proved for primes dividing the
primitive (A_0)- or (B_0)-numerator after (delta_s) is removed.  The
exact ((m,p,j,s)=(11,13,1,3)) witness is still a primitive (B_0)-zero.
The digit (A_1) and the joint gate (A_0=A_1=B_0=0) remain separate and
open.  No content exponent and no conclusion about (e+\pi) is claimed.

## 2. The three-coordinate moving vector

Item 196 gives



$$
V_{s,\rho}(a)=u(a)G_s(\sigma_\rho(a)),qquad
 a\in\{-1,i,-i\}.                                    \tag{2.1}
$$



The coefficients of (G_s) are rational.  Hence



$$
V_{s,1}(-i)=b_s-ic_s.                                \tag{2.2}
$$



Moreover



$$
\frac{u(i)}{u(-i)}=\frac{1+i}{1-i}=i.
$$



It follows exactly that



$$
V_{s,3}(i)=iV_{s,1}(-i)=c_s+ib_s,qquad
 V_{s,3}(-i)=c_s-ib_s,                                \tag{2.3}
$$



while (V_{s,3}(-1)=a_s).  This proves (1.2).

For either gate, conjugate Gaussian terms pair to a rational linear form in
these three coordinates.  The Cartier weights depend only on (j), and
Item 196 proves that their denominators are (p)-units when (p\ge2j+3).
Thus a common (p)-factor of the three moving coordinates forces both first
gates, independently of the weight vector.

## 3. Canonical integral clearing

Item 196 proves



$$
M_kB_s\in\mathbb Z[x].                               \tag{3.1}
$$



At (x=-1), since (u(-1)=-2),



$$
2^{k-1}M_kV_{s,1}(-1)=(-1)^{k+1}M_kB_s(-1)\in\mathbb Z. \tag{3.2}
$$



At (x=i), since (u(i)=1+i),



$$
2^{k-1}M_kV_{s,1}(i)
 =M_k(1-i)^{k-1}B_s(i)\in\mathbb Z[i].                \tag{3.3}
$$



Equations (3.2)--(3.3) prove the integrality asserted in (1.3).  Every
prime divisor of (Lambda_s) is at most (k).  Hence (Lambda_s) is a
unit at every cell prime (p>k), and (1.4) is a canonical localized first
Smith divisor: its (p)-valuation is the minimum valuation of the three
moving coordinates.

## 4. Exact (Q)-adic proof of the Smith-content theorem

Recall



$$
Q=(1+x)(1+x^2),qquad u=x(1-x),                       \tag{4.1}
$$





$$
uB_s'-ku'B_s=H_s
 =Q^{2s}\bigl(g_1(s)Q-g_0(s)\bigr),                   \tag{4.2}
$$



and



$$
\deg B_s=6s+2<6s+3=\deg Q^{2s+1}.                   \tag{4.3}
$$



Fix an odd prime (p>k), an integer (e\ge1), and put
(R=\mathbb Z/p^e\mathbb Z).

First suppose (p^e\mid g_0(s)) and (p^e\mid g_1(s)).  The principal-part
formula for (G_s) is linear in (H_s) and has only the denominators
(1,\ldots,k).  They are units in (R).  Therefore (B_s), and hence all
three entries in (1.3), vanish modulo (p^e).

Conversely suppose (p^e\mid h_s).  Since (Lambda_s) and all three
values of (u) at the roots of (Q) are units, (B_s) vanishes at
(-1,i,-i) modulo (p^e).  The monic factors (x+1) and (x^2+1) are
comaximal over (R): their resultant is (2), a unit.  Monic division and
the Chinese remainder theorem therefore give



$$
Q\mid B_s\quad\hbox{in }R[x]. \tag{4.4}
$$



The induction below is division-safe even though (R) is not a field.
Assume (Q^r\mid B_s), write (B_s=Q^rC), and take
(1\le r\le2s).  Equation (4.2) becomes



$$
Q^{r-1}\{ruQ'C+Q(uC'-ku'C)\}
 =Q^{2s}(g_1Q-g_0).                                   \tag{4.5}
$$



Multiplication by a monic polynomial is injective in (R[x]), so the
factor (Q^{r-1}) may be cancelled.  Reduction modulo (Q) then gives



$$
ruQ'C\equiv0\pmod Q.          \tag{4.6}
$$



Direct polynomial reduction yields the particularly small identity



$$
uQ'\equiv-4\pmod Q.           \tag{4.7}
$$



Because (p>3s+2>2s\ge r), the scalar (4r) is a unit in (R).
Thus (Q\mid C).  Induction gives



$$
Q^{2s+1}\mid B_s.             \tag{4.8}
$$



By (4.3) and monicity, (4.8) forces (B_s=0) in (R[x]).  Equation
(4.2), followed by another cancellation of the monic factor (Q^{2s}),
gives



$$
g_1(s)Q-g_0(s)=0\quad\hbox{in }R[x]. \tag{4.9}
$$



The nonconstant coefficients in (4.9) give (g_1(s)=0), and then the
constant coefficient gives (g_0(s)=0).  This proves the equivalence at
every (p^e), hence (1.5).

## 5. The exact resonance ray and its overlap ledger

The coefficient forms can be rewritten as



$$
g_0(s)=[x^k](1-x^4)^{2s+1}(1-x)^{-5s-4},             \tag{5.1}
$$





$$
g_1(s)=[x^k](1-x^4)^{2s}(1-x)^{-5s-3}.               \tag{5.2}
$$



Assume (1.7).  Then (k<p), and in (mathbb F_p[[x]]), through degree
(k),



$$
(1-x)^{-p}=(1-x^p)^{-1}\equiv1,                     \tag{5.3}
$$





$$
(1-x)^{1-p}=\frac{1-x}{1-x^p}\equiv1-x.             \tag{5.4}
$$



For (s\equiv3\pmod4), one has (k=3s+2\equiv3\pmod4).  The polynomial
in (5.3) has support only in degrees (0\pmod4), while the polynomial in
(5.4) has support only in degrees (0,1\pmod4).  Hence both coefficients
in (5.1)--(5.2) vanish modulo (p).  The content theorem now forces the
whole moving vector to vanish.

The row identity (1.8) follows without approximation:



$$
\begin{aligned}
 5(2m+1)
 &=5(j+1)p-(p-4)\\
 &=(5j+4)p+4.
\end{aligned}
$$



Thus every distinct resonance prime on the (m)-th row divides the single
integer (10m+1).  Their squarefree product also divides (10m+1), and



$$
\sum_{\text{resonance rows at }m}\log p
 \le\log(10m+1)=O(\log m)=o(m).                       \tag{5.5}
$$



This removes the entire deterministic ray from any positive-rate content
ledger.  It makes no assertion that (1.7) lists all prime divisors of
(delta_s).

For (s=3), (p=19) is the first member.  The rows with (j=1,3) are



$$
(m,p,j,s)=(17,19,1,3),\qquad(36,19,3,3),             \tag{5.6}
$$



and both have (A_0=B_0=0).

## 6. Exact numerator recurrence and the local-resultant obstruction

Put



$$
F_s(x)=\frac{(1-x^4)^{2s}}{(1-x)^{5s+3}}
        =\sum_{n\ge0}A_n(s)x^n,                       \tag{6.1}
$$



with (A_n=0) for (n<0).  Logarithmic differentiation gives the exact
integer recurrence



$$
\boxed{
 (n+1)A_{n+1}
 =(5s+3)(A_n+A_{n-1}+A_{n-2})+(n-3s)A_{n-3}.}         \tag{6.2}
$$



The two resonant numerators are



$$
g_1(s)=A_k(s),qquad
 g_0(s)=A_k+A_{k-1}+A_{k-2}+A_{k-3}.                  \tag{6.3}
$$



Let (T_n) carry
((A_n,A_{n-1},A_{n-2},A_{n-3})) to
((A_{n+1},A_n,A_{n-1},A_{n-2})).  From (6.2),



$$
\det T_n={3s-n\over n+1}.     \tag{6.4}
$$



All denominators through (n=k-1) are (p)-units for an admissible
prime.  The transfer nevertheless has an exact characteristic-zero rank
drop at (n=3s).  It is not a bad-prime artifact.

Indeed, for (s\ge1) and (p>k), the congruences (g_0=g_1=0), together
with (6.2) at (n=3s,3s+1), imply



$$
(A_k,A_{k-1},A_{k-2},A_{k-3},A_{k-4})
 =t(0,0,-1,1,0)                                      \tag{6.5}
$$



for a free scalar (t).  Thus the two terminal equations do not annihilate
the transferred state.  Any eliminant formed by multiplying the full local
transfer determinants contains the zero factor (6.4), while the terminal
system retains the survivor (6.5).

This proves a precise scoped obstruction: the naive local transfer
determinant, Casoratian, or its two-output linear resultant cannot produce a
nonzero integer that excludes common moving content.  The fixed initial
state (A_0=1,A_{-1}=A_{-2}=A_{-3}=0) still contains global arithmetic
information.  A cancellation-aware global recurrence or another
(p)-adic argument is not ruled out.

## 7. Height ledger and why it gives no moving-prime count

Write (Q^e=\sum q_rx^r).  Its coefficients are nonnegative and
(sum q_r=4^e).  Also



$$
[x^d](1-x)^{-k-1}={k+d\choose d}\le4^k
 \quad(0\le d\le k).                                  \tag{7.1}
$$



Using (e=2s) and (k=3s+2) gives



$$
g_1(s)\le4^{2s}4^k=4^{5s+2};                         \tag{7.2}
$$



similarly (g_0(s)\le4^{5s+3}).  Therefore



$$
\log\operatorname {rad}_{>k}(h_s)
 \le(5s+2)\log4,                                     \tag{7.3}
$$



and, on a fixed (s)-fiber,



$$
\omega_{>k}(h_s)
 \le{(5s+2)\log4\over\log(k+1)}=O(s/\log s).         \tag{7.4}
$$



The desired direction fixes (p) and lets (s) range through an interval
of length (p/3+O(1)).  Summing (7.3) over that interval costs
(O(p^2)), so it is weaker than the trivial root count.

There is an exact obstruction to using only this height envelope.  For an
odd prime (p), put



$$
s_0(p)=\min\{s:p\le4^{5s+2}\}.                       \tag{7.5}
$$



Define mock positive integer pairs by



$$
(\widetilde g_0(s),\widetilde g_1(s))=
 \begin{cases}
 (1,1),&s<s_0(p),\\
 (p,p),&s_0(p)\le s\le(p-3)/3.
 \end{cases}                                          \tag{7.6}
$$



They obey the proved height inequalities and have



$$
{p\over3}-O(\log p)                                  \tag{7.7}
$$



common roots modulo (p).  This countermodel is deliberately scoped: it
does **not** satisfy (6.2) and is not asserted to arise from the rank-one
primitive.  It proves only that positivity, integrality, denominator-unit
clearing, and (7.2) cannot yield a sublinear moving-prime count.

## 8. The two (s=3) witnesses are arithmetically different

Exact evaluation gives



$$
(a_3,b_3,c_3)
 =\left({20878112\over165},-{312208\over5},
                 -{10458512\over165}\right),          \tag{8.1}
$$



and



$$
165(a_3,b_3,c_3)
 =304(68678,-33891,-34403).                            \tag{8.2}
$$



Moreover



$$
\delta_3=\gcd(31260320,19414656)=608.                \tag{8.3}
$$



Thus (19) is common moving content, exactly as (1.5) predicts.  This is
the arithmetic source of the two common-gate rows in (5.6).

By contrast, on Item 196's exact row



$$
(m,p,j,s)=(11,13,1,3),
$$



one has



$$
C^A_{1,3,1}={2607104\over99}\equiv4\pmod {13},
\qquad
 C^B_{1,3,1}=-{2213120\over33}\equiv0\pmod {13}.     \tag{8.4}
$$



Since (13\nmid\delta_3), this zero survives primitive-content removal.
It is a zero of one contraction, not a zero of the moving vector.  Hence the
content theorem does not replace the still-open primitive (A_0)- and
(B_0)-numerator problems.

Nothing here evaluates (A_1).  In particular, a common first-gate zero
does not imply the joint condition (A_0=A_1=B_0=0) or a third valuation
copy.

## 9. Deterministic certificate and frozen work artifacts

The standard-library checker

    work/item205_rankone_numerator_certificate.py

imports the pinned Item 196 checker from either its own directory or the
sibling archive `scripts/` directory.  It performs these exact tasks:

1. constructs the canonical integer vector (1.3) and verifies the
   (
ho=1\leftrightarrow3) swap;
2. verifies that the prime-(>k) parts of (h_s) and (delta_s) agree in
   the declared finite audit;
3. reconstructs (g_0,g_1) from (6.2), checks the unique singular transfer,
   and checks (7.2);
4. verifies the resonance ray and its (10m+1) row overlap;
5. reproduces the (p=19) common-content rows and the distinct (p=13)
   primitive (B_0)-witness;
6. records exact height-envelope countermodels.

The canonical range is (0\le s\le40).  Every statement inferred from
that range is labeled **FINITE** in the JSON.  In particular, the observed
fact that all admissible large content primes through (s=40) lie on
(1.7) is not extrapolated.  The all-(s) results are (1.2), (1.5),
(1.7)--(1.9), (6.2)--(6.5), and their proofs above.

Canonical and replay JSON files are byte-identical.  An archive-layout run
with the checker and its dependencies under `scripts/`, writing to sibling
`results/`, is also byte-identical.  The frozen work artifact set is

    work/item205_rankone_numerator_report.md
    work/item205_rankone_numerator_certificate.py
    work/item205_rankone_numerator_certificate.json
    work/item205_rankone_numerator_certificate_replay.json
    work/item205_rankone_numerator_hashes.sha256

Status summary:

- **PROVED:** the three-coordinate/rho-swap reduction.
- **PROVED:** the exact prime-power localized Smith identity (1.5).
- **PROVED:** the infinite resonance ray and its zero-rate row overlap.
- **PROVED:** the numerator recurrence, singular-transfer survivor, height
  ceiling, and scoped no-go statements.
- **FINITE:** the exact audit through (s=40), with no extrapolation.
- **OPEN:** any sublinear moving-prime zero count for the primitive (A_0)
  or (B_0) contractions.
- **OPEN:** (A_1), the joint gate, any Route-1 exponent improvement, and
  the arithmetic nature of (e+\pi).
