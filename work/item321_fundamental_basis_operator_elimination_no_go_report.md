> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 321 — actual residue basis, split factor solutions, and an operator-elimination no-go

Date: 2026-08-31

## 1. Outcome and capacity first

Retain Item 317's three actual residue solutions



$$
A_s,\qquad Z_s=(-2(1+i))^sB_s,\qquad \overline Z_s,       \tag{1.1}
$$



all annihilated by



$$
\sum_{j=0}^3P_j(s)y_{s+j}=0.     \tag{1.2}
$$



This item proves their exact Casoratian and shows that they form a
fundamental basis modulo every actual prime outside a fixed-$M$ set of
logarithmic mass $O(\log M)=o(M)$.

It then factors each of the eight actual period quadrics for
$D_{s,\epsilon}$ into two genuine solutions of the same operator.
Together with $Z_s$, the two factors are again a fundamental basis; the
basis-change determinant has absolute norm $64$ or $8$, hence is a
$p$-unit for every actual $p\geq13$.

The finite-field Frobenius audit is negative for localization: the
Item-308 norm algebra is split modulo every actual prime.  Therefore
vanishing of the norm never forces simultaneous vanishing of both linear
factors.

Finally, the fundamental matrix classifies every transported quadratic
invariant: it is a pullback of a constant form and hence a coordinate
tautology.  Eliminating a regular orbit with one of the actual collision
quadrics produces the zero ideal, because every quadric has an explicit
invertible isotropic fundamental state.  Substituting the actual initial
state returns $D_{s,\epsilon}$ itself, and the raw fixed-$M$ union
product has only the already known $O(M^2)$ logarithmic-height bound.

This is a strict **common-operator elimination no-go**, not a no-go for
new arithmetic of the actual initial values.  In particular, it does not
claim that either linear factor vanishes on the actual orbit.

Thus



$$
\boxed{\text{new linear log rate}=0,\qquad
       \text{new fixed-}j=1\text{ capacity reduction}=0.} \tag{1.3}
$$



The regular-row collision mass and the $1/36$-per-$6M$ ceiling remain
open.

## 2. Exact Casoratian of the actual residue solutions

Define



$$
F_s=
\begin{pmatrix}
A_s&Z_s&\overline Z_s\\
A_{s+1}&Z_{s+1}&\overline Z_{s+1}\\
A_{s+2}&Z_{s+2}&\overline Z_{s+2}
\end{pmatrix},
\qquad W_s=\det F_s.                                      \tag{2.1}
$$



The exact Item-308 coefficient formulas give



$$
\begin{array}{c|ccc}
s&A_s&Z_s&\overline Z_s\\ \hline
1&-11&
-\dfrac{91}{8}+\dfrac{33}{4}i&
-\dfrac{91}{8}-\dfrac{33}{4}i\\[2mm]
2&\dfrac{6517}{8}&
-\dfrac{28357}{256}-\dfrac{55363}{256}i&
-\dfrac{28357}{256}+\dfrac{55363}{256}i\\[2mm]
3&-\dfrac{103389}{128}&
\dfrac{13678665}{4096}-\dfrac{9202479}{8192}i&
\dfrac{13678665}{4096}+\dfrac{9202479}{8192}i .
\end{array}                                                  \tag{2.2}
$$



Direct exact evaluation gives



$$
\boxed{
W_1={7985352375\over2^{20}}\,i
={3^2\,5^3\,7^2\,11\,13\,1013\over2^{20}}\,i\ne0.}       \tag{2.3}
$$



Let $T_s$ be Item 317's companion matrix.  Since
$F_{s+1}=T_sF_s$ and



$$
\det T_s=-{P_0(s)\over P_3(s)},  \tag{2.4}
$$



one has the exact all-$s$ transport



$$
\boxed{W_{s+1}=-{P_0(s)\over P_3(s)}W_s.}                 \tag{2.5}
$$



Put



$$
Q(s)=660s^2+1600s+779.           \tag{2.6}
$$



The two pivot quadratics telescope because



$$
660s^2+2920s+3039=Q(s+1).                   \tag{2.7}
$$



Substituting the complete factorizations of $P_0,P_3$ into (2.5)
therefore proves



$$
\boxed{
\begin{aligned}
W_s={}&i\,{3\,5^3\,7^2\,11\,13\over2^{20}}
       \left(-{9\over4096}\right)^{s-1}Q(s)\\
&\quad\cdot
\prod_{n=1}^{s-1}
{(2n+1)(6n+5)(6n+7)(6n+11)(6n+13)
\over n(n+1)(n+2)(2n+3)(2n+5)} .
\end{aligned}}                                               \tag{2.8}
$$



This is an all-$s$ identity, not a finite determinant test.

## 3. Actual-prime and fixed-$M$ basis localization

On an actual row



$$
p=4h+6s+3,\qquad h,s\geq1,       \tag{3.1}
$$



every denominator in (2.8) is a $p$-unit.  Indeed, its nonconstant
factors are at most $2s+3<p$, and the remaining denominators are powers
of $2$.  Item 308 independently proves that the coefficient
denominators are supported at $2,3$.

The numerator audit is exact.

If $h=1$, then $p=6s+7$.  For $s\geq2$, this is precisely the
factor $6n+13$ at $n=s-1$ in (2.8).  For $s=1$, one has $p=13$,
the displayed constant factor.

If $h\geq2$, then



$$
p\geq6s+11.                     \tag{3.2}
$$



Every constant and linear numerator factor in (2.8) is then strictly
between $0$ and $p$.  Only $Q(s)$ can vanish modulo $p$.  Hence



$$
\boxed{
W_s\equiv0\pmod p
\quad\Longleftrightarrow\quad
h=1\ \text{or}\ p\mid Q(s).}                             \tag{3.3}
$$



The statement includes the small actual row $p=13,s=h=1$; no small
prime is omitted.

Now retain the fixed-$M$ indexing



$$
\mathcal S_M=\{s\geq1:4s\leq M-5,\ s\equiv M+1\pmod3\},
\quad
p_s={4M+2s+1\over3},\quad h_s={M-4s-2\over3}.             \tag{3.4}
$$



The following polynomial identity is division-free:



$$
\boxed{
Q(s)-8(330M^2-235M+18)
=5(66s-132M+127)(4M+2s+1).}                              \tag{3.5}
$$



Since $4M+2s+1=3p_s$, it proves on every actual row



$$
Q(s)\equiv8(330M^2-235M+18)\pmod {p_s}.                  \tag{3.6}
$$



The quadratic on the right is nonzero for all $M\geq1$, since



$$
330(M-1)^2+425(M-1)+113>0.                               \tag{3.7}
$$



The exception $h_s=1$ occurs on at most one fixed-$M$ row
$(M=4s+5)$.  The map $s\mapsto p_s$ is injective.  Thus



$$
\boxed{
\sum_{\substack{s\in\mathcal S_M,\ p_s\ {\rm prime}\\
                 W_s\equiv0\ ({\rm mod}\ p_s)}}\log p_s
=O(\log M)=o(M).}                                        \tag{3.8}
$$



Away from this zero-rate set, $F_s$ is invertible over every residue
field or residue extension used below.  Hence the actual
$(A,Z,\overline Z)$ columns are a fundamental solution basis.

## 4. The eight period quadrics factor into actual operator solutions

Normalize Item 317's exact readout by



$$
q_{s,\epsilon}:={D_{s,\epsilon}\over9\,2^{27s+21}}.
                                                               \tag{4.1}
$$



Over the fixed number field



$$
L=\mathbb Q(i,\sqrt2),            \tag{4.2}
$$



put



$$
\ell_{r,\epsilon,s}
   =\alpha_{r,\epsilon}Z_s+
      \beta_{r,\epsilon}\overline Z_s,\qquad r=s\bmod4,   \tag{4.3}
$$



where



$$
\begin{array}{c|c|cc}
r&\epsilon&\alpha_{r,\epsilon}&\beta_{r,\epsilon}\\ \hline
0&0&\sqrt2&\sqrt2\\
0&1&\sqrt2&-\sqrt2\\
1&0&1+i&-1+i\\
1&1&1+i&1-i\\
2&0&\sqrt2&-\sqrt2\\
2&1&\sqrt2&\sqrt2\\
3&0&1+i&1-i\\
3&1&1+i&-1+i .
\end{array}                                                  \tag{4.4}
$$



Substitution into the eight exact coefficient rows of Item 317 gives



$$
\boxed{
q_{s,\epsilon}
=A_s^2+\ell_{r,\epsilon,s}^{\,2}
=Y^+_{r,\epsilon,s}Y^-_{r,\epsilon,s},}                  \tag{4.5}
$$



with



$$
Y^\pm_{r,\epsilon,n}
=A_n\pm i\bigl(
 \alpha_{r,\epsilon}Z_n+
 \beta_{r,\epsilon}\overline Z_n\bigr).                  \tag{4.6}
$$



For each fixed $(r,\epsilon)$, the coefficients in (4.6) are constant
in $n$.  Since $A,Z,\overline Z$ all satisfy (1.2), both
$Y^+_{r,\epsilon}$ and $Y^-_{r,\epsilon}$ are genuine all-index
solutions of that same operator.  Equation (4.5) uses them only on the
phase $s\equiv r\pmod4$; no periodic coefficient has been inserted into
the scalar recurrence.

The change from $(A,Z,\overline Z)$ to
$(Y^+,Y^-,Z)$ has coefficient matrix



$$
C_{r,\epsilon}=
\begin{pmatrix}
1&1&0\\
i\alpha&-i\alpha&1\\
i\beta&-i\beta&0
\end{pmatrix},
\qquad
\boxed{\det C_{r,\epsilon}=2i\beta_{r,\epsilon}.}          \tag{4.7}
$$



For even $r$, the absolute $L/\mathbb Q$ norm of this determinant is
$64=2^6$.  For odd $r$, the determinant lies in $\mathbb Q(i)$ and
has absolute norm $8=2^3$.  Therefore it is a unit at every prime above
an actual $p\geq13$.  Combining (3.8) and (4.7) proves:



$$
\boxed{
\{Y^+_{r,\epsilon},Y^-_{r,\epsilon},Z\}
\text{ is a fundamental common-operator basis outside }
O(\log M)\text{ fixed-}M\text{ mass}.}                    \tag{4.8}
$$



This is a statement about linear independence.  It makes no assertion
that either $Y^+$ or $Y^-$ vanishes at an actual collision row.

## 5. Exact Frobenius audit: every actual norm is split

Item 308 writes



$$
D_{s,\epsilon}
=\eta_sz_s^2-\delta_{s,\epsilon}b_{s,\epsilon}^2,
\qquad
\eta_s=\begin{cases}2,&s\text{ even},\\1,&s\text{ odd},\end{cases}
\quad
\delta_{s,\epsilon}=\left({2\over p}\right).              \tag{5.1}
$$



The actual congruence $p=4h+6s+3$, with
$\epsilon=h\bmod2$, determines $p\bmod8$.  The complete audit is



$$
\begin{array}{c|c|c|c|c|c}
s\bmod4&\epsilon&p\bmod8&\delta&\eta&\delta\eta\\ \hline
0&0&3&-1&2&-2\\
0&1&7&+1&2& 2\\
1&0&1&+1&1& 1\\
1&1&5&-1&1&-1\\
2&0&7&+1&2& 2\\
2&1&3&-1&2&-2\\
3&0&5&-1&1&-1\\
3&1&1&+1&1& 1 .
\end{array}                                                  \tag{5.2}
$$



In the $1$ and $2$ rows, splitting is immediate from
$(2/p)=+1$.  If $\delta\eta=-1$, then $p\equiv5\pmod8$, so
$(-1/p)=+1$.  If $\delta\eta=-2$, then $p\equiv3\pmod8$, so



$$
\left({-2\over p}\right)
 =\left({-1\over p}\right)\left({2\over p}\right)=+1.     \tag{5.3}
$$



Consequently



$$
\boxed{\left({\delta_{s,\epsilon}\eta_s\over p}\right)=+1
       \quad\text{on every actual row}.}                  \tag{5.4}
$$



Thus a square root $u^2=\delta\eta$ exists in $\mathbb F_p$, and



$$
D_{s,\epsilon}
=-\delta_{s,\epsilon}(b_{s,\epsilon}-uz_s)
                         (b_{s,\epsilon}+uz_s)            \tag{5.5}
$$



is split modulo $p$.  Frobenius fixes the two split lines rather than
forcing both to vanish.  Hence norm zero permits one factor to vanish
alone.  There is no inert-norm strengthening to simultaneous vanishing.

All field discriminants and all basis-change norms above are supported at
$2$; $p=2$ is absent.  The smallest actual prime $13$ occurs only at
$s=h=1$, already isolated in (3.3).

## 6. Classification of transported quadratic invariants

Work over any characteristic-zero or actual residue field on which
$F_s,T_s$ are invertible.  Let $H_s$ be a symmetric form on scalar
solution-state coordinates.  The condition that
$X_s^TH_sX_s$ be transported invariant under
$X_{s+1}=T_sX_s$ is



$$
T_s^TH_{s+1}T_s=H_s.             \tag{6.1}
$$



Set



$$
C_s=F_s^TH_sF_s.                 \tag{6.2}
$$



Using $F_{s+1}=T_sF_s$, equation (6.1) gives



$$
C_{s+1}=C_s.                     \tag{6.3}
$$



Conversely every constant symmetric $C$ gives



$$
\boxed{H_s=F_s^{-T}CF_s^{-1}.}                           \tag{6.4}
$$



Therefore (6.4) classifies every transported quadratic invariant on
regular support: it is the pullback of a constant form by the actual
fundamental coordinate matrix.

The period quadrics exhibit the same tautology from the other side.  For
a fixed row $\mathcal Q_{r,\epsilon}$ in solution-label coordinates,
put



$$
G_s=F_s\mathcal Q_{r,\epsilon}F_s^T.                      \tag{6.5}
$$



Then



$$
G_{s+1}=T_sG_sT_s^T,\qquad
F_s^{-1}G_sF_s^{-T}=\mathcal Q_{r,\epsilon}.              \tag{6.6}
$$



Each $\mathcal Q_{r,\epsilon}$ has rank two and determinant zero by
(4.5).  Its transported determinant is therefore identically zero; the
nonzero minors reproduce the split factors and Casoratians already
displayed.  No new fixed-$M$ integer divisor is produced.

This does not classify invariants that use additional arithmetic of the
specific initial values outside the common-operator transport law.

## 7. Scoped global no-go for common-operator elimination

The factorization gives an exact elimination witness, not merely a
dimension count.  For any row of (4.4), take the first row in
$(A,Z,\overline Z)$-coordinates to be



$$
v=(-i\beta,0,1).                 \tag{7.1}
$$



Then $\ell(v)=\beta$, so



$$
q(v)=(-i\beta)^2+\beta^2=0.      \tag{7.2}
$$



Yet $v$ completes to the invertible fundamental state



$$
\widetilde F_s=
\begin{pmatrix}
-i\beta&0&1\\
0&1&0\\
1&0&0
\end{pmatrix},
\qquad
\det\widetilde F_s=-1.                                   \tag{7.3}
$$



On regular support, the recurrence transports (7.3) uniquely through
any finite orbit window while retaining invertibility.  Thus the
recurrence equations plus one actual period-quadric collision have a
solution over the coefficient field at every regular row.  Eliminating
the orbit variables therefore gives the zero ideal in the base
coefficient ring: every purely common-operator single-collision
resultant is identically zero.

This statement uses the exact actual quadric and its exact common-operator
factor solutions.  Its scope is nevertheless strict: the witness
$\widetilde F_s$ is not the actual Item-308 initial state.

If the actual initial state is substituted before elimination, the row
scalar is simply $D_{s,\epsilon}$, up to the explicit powers of $2,3$.
The direct union container is



$$
\mathscr R_{\rm raw}(M)=
\prod_{s\in\mathcal S_M}
       \max(1,|D_{s,h_s\bmod2}|).                         \tag{7.4}
$$



Item 308 proves $\log\max(1,|D_{s,\epsilon}|)=O(s)$.  Since
$|\mathcal S_M|=O(M)$ and $s\leq M/4$,



$$
\log\mathscr R_{\rm raw}(M)=O(M^2). \tag{7.5}
$$



This is the original inadmissible height scale, not a fixed-$M$
sublinear resultant.  Sections 6--7 therefore close the following exact
information class:



$$
\boxed{
\begin{gathered}
\text{common operator and its regular pivots}\\
+\ \text{transported quadratic forms}\\
+\ \text{single-row algebraic elimination without extra}\\
\text{arithmetic of the actual initial values}.
\end{gathered}}                                           \tag{7.6}
$$



They do not rule out a new gcd theorem, a relation among the actual
initial values, or a genuinely sublinear-height fixed-$M$ resultant.

## 8. Capacity, strict labels, and the remaining lemma

The exact Casoratian removes only $O(\log M)$ exceptional mass.  On its
complement, every collision factor is a coordinate in a fundamental
solution basis, and the actual norm is split.  Consequently the common
operator supplies neither propagation nor a Frobenius double-zero that
would reduce regular collision support.

The live target remains



$$
\boxed{
\mathcal W_D(M)=
\sum_{\substack{s\in\mathcal S_M\setminus\{2,4,6\}\\
                 p_s\ {\rm prime}\\
                 p_s\mid D_{s,h_s\bmod2}}}\log p_s=o(M).} \tag{8.1}
$$



The smallest remaining lemma can now be stated factorwise: for the eight
fixed common-operator solutions $Y^\pm_{r,\epsilon}$ in (4.6), prove
that actual prime-ideal zeros on their matching phases and outside (3.8)
have total underlying rational-prime mass $o(M)$.  Such a theorem must
use arithmetic of their actual initial values beyond regular transport.
A fixed-$M$ gcd or resultant of logarithmic height $o(M)$ would
suffice.

- **PROVED:** the exact Casoratian (2.8); the division-free fixed-$M$
  localization (3.5)--(3.8); fundamental-basis support outside
  $O(\log M)$; all eight factorizations into genuine operator solutions;
  the $p$-unit basis changes; and universal splitting of the actual norm.

- **SCOPED COMMON-OPERATOR NO-GO:** transported quadratic invariants are
  coordinate pullbacks, and regular single-collision elimination gives
  the zero ideal.  Actual substitution returns only the $O(M^2)$-height
  raw product.

- **EXACT FINITE ONLY:** none is used to prove an all-$s$, fixed-$M$,
  Frobenius, or density statement.

- **OPEN:** arithmetic of the actual factor-solution initial values;
  a sublinear fixed-$M$ gcd/resultant; regular moving-prime
  localization; (8.1); fixed-$j=1$ closure; Route 1; and every
  conclusion about $e+\pi$.

- **NOT CLAIMED:** that either factor vanishes on the actual orbit; an
  inert-norm double zero; a prime scan; a factor census; simultaneous
  realization of the elimination witness by the actual sequence; or
  positive capacity.

The ledger remains



$$
\boxed{\text{capacity booked}=0,\qquad
       \text{fixed-}j=1\text{ ceiling}={1\over36}
       \text{ per }6M.}                                  \tag{8.2}
$$



No canonical, master, or status file is edited by this research package.

## 9. Deterministic replay

From the archive root, run

~~~text
python work/item321_fundamental_basis_operator_elimination_no_go_certificate.py --output work/item321_fundamental_basis_operator_elimination_no_go_certificate.replay.json
~~~

The checker pins the canonical Item 308 and Item 317 packages.  It
recomputes the exact initial residues and Casoratian; proves the
telescoping pivot identity and division-free fixed-$M$ congruence;
verifies all eight quadric factorizations, ranks, basis determinants,
field norms, and invertible isotropic witnesses; and audits all eight
actual Frobenius classes.  It uses exact symbolic arithmetic and performs
no prime scan.
