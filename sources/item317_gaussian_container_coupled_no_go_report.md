> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 317 — exact Gaussian telescoper, actual-container coupled system, and pivot-only no-go

Date: 2026-08-31

## 1. Outcome and capacity first

Let $A_s$ be the rational aggregate of Items 310 and 312 and $B_s$
the pinned Gaussian aggregate of Item 308.  Write



$$
\lambda={1+i\over2},\qquad r=\lambda^{-3}=-2(1+i),
 \qquad Z_s=r^sB_s.                                      \tag{1.1}
$$



This item proves, by one exact residue-level differential telescoper, that
$A_s$ and $Z_s$ satisfy the same all-$s$ operator



$$
\boxed{\sum_{j=0}^3P_j(s)y_{s+j}=0\qquad(s\geq1).}       \tag{1.2}
$$



Equivalently, the actual Gaussian coordinate satisfies



$$
\boxed{
 (1+i)P_0(s)B_s-4iP_1(s)B_{s+1}
 +8(-1+i)P_2(s)B_{s+2}+32P_3(s)B_{s+3}=0.}               \tag{1.3}
$$



Thus the Gaussian result is not a bounded fit and not merely a qualitative
P-recursiveness closure.

The actual Item-308 integer container $D_{s,\epsilon}$ is an exact
periodic quadratic readout of the three common-operator solutions
$A_s,Z_s,\overline Z_s$.  Symmetric-square transport gives an explicit
24-dimensional all-$s$ coupled system.  For each fixed pair
$(s\bmod4,\epsilon)$, the four quadratic blocks combine into one exact
six-dimensional step-four system.  This is the promised exact coupled
annihilator for the actual container.  No minimal scalar order is claimed.

All forward and backward singularities of this system through a four-step
period divide eight explicit degree-seven fixed-$M$ integers.  Their
combined logarithmic prime mass is



$$
O(\log M)=o(M).              \tag{1.4}
$$



However, regular transport alone does not localize zeros of the quadratic
readout.  At every regular row there is a nonzero common-operator state for
which the exact readout is zero.  This is a rigorous, strictly scoped
**pivot-only no-go**: arguments using only the exact operator, its pivots,
and regularity exclude no off-pivot row.  It is not a counterexample to the
actual Item-308 initial state.

Consequently



$$
\boxed{\text{new linear log rate}=0,\qquad
        \text{new fixed-}j=1\text{ capacity reduction}=0.} \tag{1.5}
$$



The off-ray target and the $1/36$-per-$6M$ fixed-$j=1$ ceiling remain
open.

## 2. Exact input sequences

Put



$$
q(t)=t^2-2t+2,\qquad N_s(t)=N_0(t)+sN_1(t),             \tag{2.1}
$$



where



$$
\begin{aligned}
N_0(t)&=4-\frac43t-\frac83t^2+\frac{16}3t^3-3t^4+t^5,\\
N_1(t)&=\frac{80}3t-\frac{224}3t^2+\frac{256}3t^3
                         -46t^4+10t^5.                   \tag{2.2}
\end{aligned}
$$



Items 308 and 310 define



$$
A_s=-[x^{2s+5}]
 { (1+x)^{3s+1/2}N_s(1+x)\over(1+x^2)^{2s+1}}            \tag{2.3}
$$



and



$$
B_s=[x^{2s}]
 { (1+x)^{3s+1/2}N_s((1-i)(1+x))
  \over
  2^{2s+1}i^{2s+6}(1+i)^{2s+1}
  (1+(1+i)x)^{2s+6}(1+\lambda x)^{2s+1}}.                \tag{2.4}
$$



The four operator coefficients are



$$
\begin{aligned}
P_0(s)={}&9(2s+1)(6s+5)(6s+7)(6s+11)(6s+13)
                  (660s^2+2920s+3039),                   \tag{2.5}\\
P_1(s)={}&24s(6s+11)(6s+13)
 (1697520s^4+10905280s^3+24360488s^2\\
&\hspace{47mm}+22368528s+7001703),                        \tag{2.6}\\
P_2(s)={}&768s(s+1)(2s+3)(6s+13)
 (3960s^3+20820s^2+33034s+14047),                        \tag{2.7}\\
P_3(s)={}&4096s(s+1)(s+2)(2s+3)(2s+5)
                  (660s^2+1600s+779).                    \tag{2.8}
\end{aligned}
$$



Every $P_j$ has degree seven.  Equations (2.5) and (2.8) are the
complete rational factorizations of the backward and forward pivots; the
two displayed quadratics are irreducible by Item 312.

## 3. One exact differential telescoper for both poles

Define



$$
F_s(t)={t^{3s+1/2}\over
              (1-t)^{2s+6}q(t)^{2s+1}},
 \qquad \omega_s=N_s(t)F_s(t)\,dt,                       \tag{3.1}
$$



and



$$
R(t)={t^3\over(1-t)^2q(t)^2}.                            \tag{3.2}
$$



The sealed data file gives an explicit
$\mathcal P(s,t)\in\tfrac13\mathbb Z[s,t]$, of degree seven in $s$
and degree twenty in $t$.  Put



$$
K_s(t)={t\mathcal P(s,t)\over(1-t)^5q(t)^5}.             \tag{3.3}
$$



Exact clearing in $\mathbb Q[s,t]$ proves



$$
\boxed{
 K_s'(t)+{F_s'(t)\over F_s(t)}K_s(t)
 =\sum_{j=0}^3P_j(s)R(t)^jN_{s+j}(t).}                   \tag{3.4}
$$



Since $F_{s+j}=R^jF_s$, multiplication by $F_s(t)dt$
gives the differential-form identity



$$
\boxed{\sum_{j=0}^3P_j(s)\omega_{s+j}=d(K_sF_s).}       \tag{3.5}
$$



The residue of an exact local derivative is zero.  At $t=1$, use
$t=1+x$.  Because $q(1+x)=1+x^2$ and $2s+6$ is even,



$$
A_s=-\operatorname {Res}_{t=1}\omega_s. \tag{3.6}
$$



At the Gaussian root



$$
\rho=\lambda^{-1}=1-i,                                  \tag{3.7}
$$



use $t=\rho(1+x)$.  The exact local identities



$$
\begin{aligned}
1-t&=i(1+(1+i)x),\\
q(t)&=-2(1+i)x(1+\lambda x),\\
dt&=\rho\,dx                                               \tag{3.8}
\end{aligned}
$$



and (2.4) give, for one fixed local square-root branch,



$$
\operatorname {Res}_{t=\rho}\omega_s
             =-\lambda^{-3s-3/2}B_s.                     \tag{3.9}
$$



Taking the residues of (3.5) at $1$ and at $\rho$ proves (1.2) for
$A_s$ and $Z_s=\lambda^{-3s}B_s$, for every integer $s\geq1$.
The conjugate equation proves the same statement for $\overline Z_s$.
Multiplying the $B_s$ equation by $1+i$ and using
$(1+i)r^j=(1+i),-4i,8(-1+i),32$ proves (1.3).

This proof uses no finite recurrence interpolation.  The complete
$\mathcal P(s,t)$ is stored in
`scripts/item317_residue_telescoper_data.json`, with SHA-256
`f9ca57040fc7ae1030f9d915955085e3263e6c30f3129f2e9c4961198defa81b`.

## 4. Gaussian pivots and the actual-prime unit audit

The trailing and leading Gaussian coefficients in (1.3) are



$$
(1+i)P_0(s),\qquad32P_3(s).      \tag{4.1}
$$



Their new Gaussian contents have norms $2$ and powers of $2$.
The rational contents of $P_0,P_3$ are supported only at $2,3$.
Every admissible structural-row prime satisfies



$$
p\geq6s+7\geq13.                 \tag{4.2}
$$



Hence every Gaussian multiplier and every cleared rational content in
(4.1) is a $p$-unit.  The only rational-prime pivot factors are exactly
the factors of $P_0(s)P_3(s)$; no additional Gaussian prime support is
hidden by the rescaling (1.1).

## 5. Exact readout of the actual Item-308 containers

Write $B_s=U_s+iV_s$ and



$$
\delta_s=\delta_{s,0}=(-1)^{s(s+1)/2+1}.                 \tag{5.1}
$$



Item 308's exact integral scalings are



$$
\begin{aligned}
a_s&=3\,2^{12s+10}A_s,\\
b_{s,0}&=3\delta_s2^{15s+12}U_s,\\
b_{s,1}&=-3\delta_{s,1}2^{15s+12}V_s,
 \qquad\delta_{s,1}=-\delta_s.                           \tag{5.2}
\end{aligned}
$$



Substitute $B_s=r^{-s}Z_s$ and its conjugate into



$$
D_{s,\epsilon}=2^{3s+1}a_s^2
                 -\delta_{s,\epsilon}b_{s,\epsilon}^2.   \tag{5.3}
$$



Exact simplification gives the all-$s$ identity



$$
\boxed{
 {D_{s,\epsilon}\over9\,2^{27s+21}}
 =A_s^2-2\delta_s(-i)^sZ_s^2
       -2\delta_si^s\overline Z_s^{\,2}
       -4(-1)^\epsilon\delta_sZ_s\overline Z_s.}         \tag{5.4}
$$



All coefficients in (5.4) have period four.  For clarity, the four
coefficients of
$(A_s^2,Z_s^2,\overline Z_s^{\,2},Z_s\overline Z_s)$ are



$$
\begin{array}{c|c|rrrr}
s\bmod4&\epsilon&A^2&Z^2&\overline Z^{\,2}&Z\overline Z\\ \hline
0&0&1&2&2&4\\
0&1&1&2&2&-4\\
1&0&1&2i&-2i&-4\\
1&1&1&2i&-2i&4\\
2&0&1&2&2&-4\\
2&1&1&2&2&4\\
3&0&1&2i&-2i&4\\
3&1&1&2i&-2i&-4.
                                                               \tag{5.5}
\end{array}
$$



The certificate verifies (5.4) symbolically on these eight exhaustive
period classes.  They are symbolic residue classes, not finite evidence.

## 6. Exact coupled annihilator for $D_{s,\epsilon}$

For any solution $y$ of (1.2), set



$$
Y_s^y=(y_s,y_{s+1},y_{s+2})^T,\qquad
 Y_{s+1}^y=T_sY_s^y,                                     \tag{6.1}
$$



where



$$
T_s=\begin{pmatrix}
 0&1&0\\0&0&1\\a&b&c
 \end{pmatrix},\qquad
 a=-{P_0\over P_3},\quad b=-{P_1\over P_3},\quad
 c=-{P_2\over P_3}.                                      \tag{6.2}
$$



Thus



$$
\det T_s=-{P_0(s)\over P_3(s)}.  \tag{6.3}
$$



For two solutions $u,v$, use the symmetric product state



$$
Q_s(u,v)=
 \begin{pmatrix}
u_0v_0\\u_0v_1+u_1v_0\\u_0v_2+u_2v_0\\
u_1v_1\\u_1v_2+u_2v_1\\u_2v_2
 \end{pmatrix},\qquad u_j=u_{s+j},\quad v_j=v_{s+j}.     \tag{6.4}
$$



Direct multiplication gives



$$
Q_{s+1}(u,v)=S_sQ_s(u,v),                               \tag{6.5}
$$



with the explicit matrix



$$
S_s=\begin{pmatrix}
0&0&0&1&0&0\\
0&0&0&0&1&0\\
0&a&0&2b&c&0\\
0&0&0&0&0&1\\
0&0&a&0&b&2c\\
a^2&ab&ac&b^2&bc&c^2
\end{pmatrix}.                                           \tag{6.6}
$$



Its determinant is



$$
\det S_s=\left({P_0\over P_3}\right)^4. \tag{6.7}
$$



Stack the four exact blocks



$$
Q_s(A,A),\quad Q_s(Z,Z),\quad
 Q_s(\overline Z,\overline Z),\quad Q_s(Z,\overline Z)  \tag{6.8}
$$



into $W_s\in\mathbb Q(i)^{24}$, and put



$$
\widehat W_s=2^{27s}W_s.          \tag{6.9}
$$



Then



$$
\boxed{
 \widehat W_{s+1}=2^{27}
 \operatorname {diag}(S_s,S_s,S_s,S_s)\widehat W_s,}
                                                               \tag{6.10}
$$



and (5.4) is exactly



$$
\boxed{D_{s,\epsilon}=9\,2^{21}
                    \ell_{s,\epsilon}\widehat W_s,}      \tag{6.11}
$$



where the row vector $\ell_{s,\epsilon}$ is given by (5.5) and selects
the first coordinate in each block.  Equations (6.10)--(6.11) are an
explicit all-$s$ coupled annihilator for the actual container.

There is a sharper residue-wise form.  Fix
$r_0=s\bmod4$ and $\epsilon$, and combine the four blocks in (6.8)
using the constant row of (5.5).  The resulting six-state vector
$V_s^{(r_0,\epsilon)}$, for $s\equiv r_0\pmod4$, satisfies



$$
\boxed{
 \widehat V_{s+4}=2^{108}
 S_{s+3}S_{s+2}S_{s+1}S_s\widehat V_s,}                  \tag{6.12}
$$



and $D_{s,\epsilon}=9\,2^{21}$ times its first coordinate.  Exact
cyclic-vector elimination therefore supplies a step-four scalar
annihilator of order at most six over $\mathbb Q(i)(s)$ for each fixed
$(s\bmod4,\epsilon)$.  No minimality and no smaller global interlaced
order are asserted; (6.10) and (6.12), rather than qualitative holonomy,
are the promoted theorem.

## 7. Complete four-step pivot localization at fixed $M$

The actual fixed-$M$ indexing is



$$
\mathcal S_M=\{s\geq1:4s\leq M-5,\ s\equiv M+1\pmod3\},
\qquad p_s={4M+2s+1\over3}.                               \tag{7.1}
$$



The cell is nonempty only for $M\geq9$, and



$$
2s\equiv-(4M+1)\pmod {p_s}.      \tag{7.2}
$$



Forward or backward transport over (6.12) uses only
$P_3(s+k)$ or $P_0(s+k)$, $0\leq k\leq3$.  Exact substitution gives



$$
2^7P_\nu\left(-{4M+1\over2}+k\right)
                  =c_{\nu,k}R_{\nu,k}(M),                \tag{7.3}
$$



where



$$
\begin{array}{c|c|c}
\nu,k&c_{\nu,k}&R_{\nu,k}(M)\\ \hline
0,0&2^{18}3^2&-M(3M-2)(3M-1)(6M-5)(6M-1)
                    (330M^2-565M+218)\\
0,1&2^{17}3^2&-(2M-1)(3M-4)(3M-2)(6M-7)(6M-5)
                    (330M^2-895M+583)\\
0,2&2^{18}3^2&-(M-1)(3M-5)(3M-4)(6M-11)(6M-7)
                    (330M^2-1225M+1113)\\
0,3&2^{17}3^2&-(2M-3)(3M-7)(3M-5)(6M-13)(6M-11)
                    (330M^2-1555M+1808)\\
3,0&2^{22}&-(M-1)(2M-1)(4M-3)(4M-1)(4M+1)
                    (330M^2-235M+18)\\
3,1&2^{22}&-(M-1)(2M-3)(4M-5)(4M-3)(4M-1)
                    (330M^2-565M+218)\\
3,2&2^{22}&-(M-2)(2M-3)(4M-7)(4M-5)(4M-3)
                    (330M^2-895M+583)\\
3,3&2^{22}&-(M-2)(2M-5)(4M-9)(4M-7)(4M-5)
                    (330M^2-1225M+1113).
                                                               \tag{7.4}
\end{array}
$$



All discarded contents in (7.4) are $p_s$-units.  Every linear factor
is positive for $M\geq9$.  Each quadratic is increasing and positive
there: its derivative is already positive by $M=3$, and direct
substitution at $M=9$ is positive.  Hence all eight
$R_{\nu,k}(M)$ are nonzero for the complete admissible range.

The shift-zero pair is precisely Item 312's already localized pivot
support.  The three new shifts introduce no linear mass.  Indeed, with



$$
R_{\rm shift}(M)=
       \prod_{k=0}^3R_{0,k}(M)R_{3,k}(M),                 \tag{7.5}
$$



one has $\deg R_{\rm shift}=56$, and (7.2)--(7.4) imply



$$
p_s\mid\prod_{k=0}^3P_0(s+k)P_3(s+k)
                 \quad\Longrightarrow\quad
p_s\mid R_{\rm shift}(M).                               \tag{7.6}
$$



The map $s\mapsto p_s$ is injective on $\mathcal S_M$.  Therefore



$$
\boxed{
\sum_{\substack{s\in\mathcal S_M,\ p_s\ {\rm prime}\\
p_s\mid\prod_{k=0}^3P_0(s+k)P_3(s+k)}}\log p_s
 \leq\log|R_{\rm shift}(M)|=O(\log M)=o(M).}             \tag{7.7}
$$



This is an exact fixed-$M$ singular-container localization theorem for
the coupled system.  It localizes only failure of transport.  It does not
assert that a prime dividing $D_{s,\epsilon}$ must divide a pivot.

## 8. Exact scoped no-go on every regular row

Work over the residue algebra at a row for which the factors in (7.6)
are units.  Then $T_s$, $S_s$, and the required forward and backward
transitions are invertible by (6.3) and (6.7).

Choose the local state of one common-operator solution $y$ to be



$$
(y_s,y_{s+1},y_{s+2})=(0,1,0),   \tag{8.1}
$$



and take both Gaussian solution states to be zero.  Regularity extends
this nonzero local state uniquely through every required transition.
At the chosen row, the exact quadratic readout (5.4) is nevertheless
zero: its only surviving term is $y_s^2=0$.  The powers of two and the
factor $9$ in (6.11) are units, so the actual scaled readout is also
zero.

Thus, for every off-pivot row separately, a nonzero solution state with
$D_{s,\epsilon}=0$ remains admissible.  In particular, no implication



$$
D_{s,\epsilon}\equiv0\pmod {p_s}
       \Longrightarrow p_s\mid R_{\rm shift}(M)           \tag{8.2}
$$



can follow from the operator, pivot factorization, and regularity alone.
This closes that information class and leaves its entire rowwise
off-pivot support available to the raw union bound.

The scope is essential.  The state (8.1) is not claimed to equal the
actual Item-308 initial state, does not define a comparison for the
original orbit, and says nothing against a sequence-specific invariant,
initial-value congruence, or arithmetic resultant for the actual
$(A_s,Z_s,\overline Z_s)$.

## 9. Capacity, strict labels, and the remaining lemma

The exact Gaussian operator and the exact container system strengthen the
structural description of the fixed-$j=1$ branch.  Their complete pivot
support has weighted $o(M)$ mass.  But the theorem removes no collision
row on regular support, so it gives no master-capacity reduction.

The required off-ray estimate remains



$$
\boxed{
\mathcal W_D(M)=
\sum_{\substack{s\in\mathcal S_M\setminus\{2,4,6\}\\
                 p_s\ {\rm prime}\\
                 p_s\mid D_{s,h_s\bmod2}}}\log p_s=o(M),
\qquad h_s={M-4s-2\over3}.}                              \tag{9.1}
$$



The smallest remaining lemma is a sequence-specific regular-state
theorem: using the actual initial values or an exact invariant/resultant,
prove that the rows in (9.1) with



$$
p_s\nmid R_{\rm shift}(M)              \tag{9.2}
$$



have weighted $o(M)$ mass.  A fixed-$M$ resultant of height
$\exp(o(M))$ containing every such actual collision prime would suffice.
The coupled operator and its pivots alone cannot supply it by Section 8.

- **PROVED:** the all-$s$ differential telescoper; the exact Gaussian
  operator (1.3); the actual-container identity (5.4); the 24-dimensional
  all-$s$ and six-dimensional residue-wise coupled systems; complete
  pivot factorization; and the degree-56 fixed-$M$ singular localization
  with mass $O(\log M)$.

- **SCOPED PIVOT-ONLY NO-GO:** exact operator coefficients, pivot
  factorization, and regular invertibility alone exclude no off-pivot row.

- **EXACT FINITE ONLY:** none is used for the operator, the coupled
  system, the pivot localization, or any density claim.

- **OPEN:** scalar minimality; a useful actual-initial-state invariant or
  arithmetic resultant; regular collision localization; (9.1); the
  fixed-$j=1$ closer; Route 1; and every conclusion about $e+\pi$.

- **NOT CLAIMED:** a prime scan, a factor census of $D_{s,\epsilon}$,
  simultaneous realization of the no-go witness on the actual sequence,
  necessity of pivot divisibility for collision, or positive capacity.

The ledger remains



$$
\boxed{\text{capacity booked}=0,\qquad
        \text{fixed-}j=1\text{ ceiling}={1\over36}
        \text{ per }6M.}                                 \tag{9.3}
$$



The canonical report, script, sealed data, certificates, ledger, manifest,
hash list, and root audit are stored in the archive; master/status integration
is recorded separately.

## 10. Deterministic replay

From the archive root, run

~~~text
python scripts/item317_gaussian_container_coupled_no_go_certificate.py --output results/item317_gaussian_container_coupled_no_go_certificate_replay.json
~~~

The checker pins the canonical Item 308, Item 310, and Item 312 packages.
It reconstructs and clears (3.4) exactly; verifies both residue maps and
the Gaussian multipliers; proves the eight symbolic readout classes;
constructs $T_s$ and $S_s$ and checks both determinants; derives and
factors all eight shifted fixed-$M$ pivot containers; proves their
nonvanishing and total degree; and records the regular-state no-go.  It
uses exact symbolic arithmetic, performs no prime scan, and factors no
$D_{s,\epsilon}$.
