> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The pointed Euler double root and the bounded-eliminant barrier

## An integral $x(x-1)$ normalization, exact seed subresultants, and a restricted no-go

Checked: 2026-08-27 UTC

## 1. Scope and outcome

Let the secant Euler numbers be defined by



$$
\operatorname {sech}z=\sum_{j\geq0}E_j{z^j\over j!},
 \qquad E_{2j+1}=0.                                      \tag{1}
$$



Let $M=2m\geq4$.  The frozen adjacent-Euler note encoded a common
divisor of $E_M$ and $E_{M-2}$ as a fourth-order root at zero of a
centered Euler polynomial.  Its full discriminant has logarithmic height
$O(M^2\log M)$.

This continuation makes the strongest canonical reduction found from the
Appell, shift, special-value, and subresultant identities.  If
$\mathcal E_n(X)$ is the ordinary Euler polynomial, there is a monic
integral polynomial $P_m(U)$ of degree $m-1$ such that



$$
\boxed{\mathcal E_{2m}(X)=X(X-1)P_m(X(X-1)).}             \tag{2}
$$



For every positive common divisor $d\mid E_M,E_{M-2}$, the fixed point



$$
U_0=-{1\over4}                    \tag{3}
$$



is a double root of $P_m$ modulo $d$.  Secant Euler numbers are odd,
so clearing powers of 4 is legitimate for the complete modulus.
Consequently



$$
\boxed{d\mid\operatorname {Disc}(P_m).} \tag{4}
$$



This removes both permanent roots of the ordinary Euler polynomial and
the artificial $4^{\Theta(M^2)}$ factor created by the centered affine
coordinate.  It is a genuinely smaller eliminant than the discriminants
in the frozen note.  Its degree is still linear in $M$, however, and
the direct determinant ledger remains



$$
\log|\operatorname {Disc}(P_m)|
                         =O(M^2\log M).                    \tag{5}
$$



The actual interior seed $M=3288,\ p=151483$ gives a sharper negative
test: modulo $p$, $P_{1644}$ has exactly one double root and every
other root is simple.  Hence only the zeroth principal subresultant, the
resultant/discriminant, is forced to vanish in that example.  This seed
refutes any universal claim that adjacent Euler divisibility forces the
next, higher subdiscriminant to vanish.  It does not rule out every
conceivable eliminant.

The Appell recurrence degenerates at (3) to the original adjacent Euler
condition, while every centered shift jet at zero is a parity or
permanent-root identity.  These give a precise restricted no-go for the
canonical bounded-jet constructions.  None of the results below bounds
the first-period factor $J_N$, and none classifies $e+\pi$.

## 2. The integral $X(X-1)$ coordinate

The ordinary Euler polynomials are defined by



$$
{2e^{Xz}\over e^z+1}=\sum_{n\geq0}\mathcal E_n(X){z^n\over n!}.
                                                               \tag{6}
$$



We use the classical identities



$$
\begin{aligned}
 \mathcal E_n(X+1)+\mathcal E_n(X)&=2X^n,\\
 \mathcal E_n(1-X)&=(-1)^n\mathcal E_n(X),\\
 \mathcal E_n'(X)&=n\mathcal E_{n-1}(X).
 \end{aligned}                                                \tag{7}
$$



For even positive degree, $\mathcal E_{2m}(X)$ is monic and belongs to
$\mathbb Z[X]$.  One coefficient proof starts from



$$
\mathcal E_{2m}(X)=X^{2m}+
 \sum_{r=1}^{m}\binom{2m}{2r-1}{G_{2r}\over2r}
 X^{2m-2r+1},                                                 \tag{8}
$$



where $2z/(e^z+1)=\sum G_nz^n/n!$.  The standard integral-coefficient
form of the Genocchi theorem is



$$
{1\over2r}\binom{2m}{2r-1}G_{2r}\in\mathbb Z
       \qquad(1\leq r\leq m).                                \tag{9}
$$



Equations (8)--(9) prove the asserted integrality.

Put $U=X(X-1)$.  Every polynomial in $\mathbb Z[X]$ has a unique
expression



$$
A(U)+XB(U),\qquad A,B\in\mathbb Z[U], \tag{10}
$$



obtained by replacing $X^2$ by $X+U$.  If it is fixed by
$X\mapsto1-X$, comparison with $A(U)+(1-X)B(U)$ gives
$(2X-1)B(U)=0$, hence $B=0$.  Thus the invariant ring is
$\mathbb Z[U]$.

For $m\geq1$, (7) and symmetry give
$\mathcal E_{2m}(0)=\mathcal E_{2m}(1)=0$.  The invariant polynomial is
therefore divisible by $X(X-1)=U$.  This proves (2), including



$$
P_m\in\mathbb Z[U],\qquad \deg P_m=m-1,\qquad
       P_m\ \hbox{monic}.                                    \tag{11}
$$



Two special values are useful.  If $G_M$ is the Genocchi number in
(8), differentiation at $X=0$ gives



$$
P_m(0)=-G_M=2(2^M-1)B_M.                  \tag{12}
$$



The shift identity at $X=1$ gives
$\mathcal E_M(2)=2$, and hence



$$
P_m(2)=1.                     \tag{13}
$$



Thus the first nonpermanent integral evaluation is a unit, not a new
integer forced to contain $d$.  Combining (3), (4), and (13) merely
recovers $3\nmid d$, because $U_0$ and 2 coincide modulo 3.

## 3. Exact fixed-point double-root descent

Define the centered and square-coordinate Euler polynomials by



$$
\begin{aligned}
 \mathcal F_M(T)&=2^M\mathcal E_M\!\left({T+1\over2}\right),\\
 \mathcal F_M(T)&=f_M(T^2),\\
 f_M(Y)&=\sum_{k=0}^m\binom M{2k}E_{M-2k}Y^k.
 \end{aligned}                                               \tag{14}
$$



Since $U=X(X-1)=(T^2-1)/4$, (2) gives



$$
\boxed{
 f_M(Y)=4^mH_m\!\left({Y-1\over4}\right),\qquad
 H_m(U)=UP_m(U),
 }                                                           \tag{15}
$$



where $H_m(U)=\mathcal E_M(X)$.  In particular,



$$
f_M(0)=E_M,\qquad
 f_M'(0)=\binom M2E_{M-2}.                                  \tag{16}
$$



Let $d\mid E_M,E_{M-2}$.  Since $d$ is odd, 4 is a unit in
$R=\mathbb Z/d\mathbb Z$.  Let $u_0=-4^{-1}\in R$.
Differentiating (15) gives



$$
f_M(0)=4^mH_m(u_0),\qquad
 f_M'(0)=4^{m-1}H_m'(u_0).                                  \tag{17}
$$



Equations (16)--(17) imply $H_m(u_0)=H_m'(u_0)=0$.  Since
$u_0$ is a unit and $H_m=UP_m$,



$$
\begin{aligned}
 0=H_m(u_0)&=u_0P_m(u_0),\\
 0=H_m'(u_0)&=P_m(u_0)+u_0P_m'(u_0).
 \end{aligned}                                               \tag{18}
$$



Thus $P_m(u_0)=P_m'(u_0)=0$, proving the double-root assertion
over the full composite modulus, including every prime-power layer.

The resultant adjugate identity supplies $A,B\in\mathbb Z[U]$ with



$$
AP_m+BP_m'=\operatorname {Res}(P_m,P_m').                  \tag{19}
$$



Evaluation at $u_0$ modulo $d$ proves (4).  The resultant is nonzero.
Brillhart's theorem says that no even ordinary Euler polynomial has a
multiple complex root.  The roots 0 and 1 are simple; after removing
them, the two-to-one invariant map is unramified away from
$X=1/2$, while $\mathcal E_{2m}(1/2)=2^{-2m}E_{2m}\ne0$.
Hence the substitution cannot create a multiple root of $P_m$.

## 4. Why the differential and shift jets do not shrink the degree

Applying the Appell identity twice to
$\mathcal E_M(X)=H_m(U)$, using
$(dU/dX)^2=4U+1$ and $d^2U/dX^2=2$, gives



$$
(4U+1)H_m''(U)+2H_m'(U)=M(M-1)H_{m-1}(U).                 \tag{20}
$$



At $U_0=-1/4$, the highest-derivative coefficient vanishes:



$$
2H_m'(U_0)=M(M-1)H_{m-1}(U_0).                            \tag{21}
$$



After restoring the invertible powers of 4 in (17), (21) is exactly the
equivalence between $E_{M-2}\equiv0\pmod d$ and
$H_m'(U_0)\equiv0\pmod d$.  It is not a third congruence.
Differentiating (20) $r$ times gives at $U_0$



$$
(4r+2)H_m^{(r+1)}(U_0)
       =M(M-1)H_{m-1}^{(r)}(U_0).                           \tag{22}
$$



For $r\geq1$, the right side contains an uncontrolled derivative of
$H_{m-1}$.  The recurrence does not propagate the two known
vanishings to a bounded tower of new vanishings.

The centered shift identity is



$$
\mathcal F_M(T+1)+\mathcal F_M(T-1)=2T^M.     \tag{23}
$$



For $0\leq r<M$, differentiating and setting $T=0$ gives



$$
\mathcal F_M^{(r)}(1)+\mathcal F_M^{(r)}(-1)=0.      \tag{24}
$$



Since $\mathcal F_M$ is even, (24) is automatic when $r$ is odd.
When $r$ is even it says $\mathcal F_M^{(r)}(1)=0$, the
permanent-root identity
$(M)_r\mathcal F_{M-r}(1)=0$.  At $r=M$, both sides of (23)
give $2M!$.  Thus every local shift jet at zero is a parity identity
or a permanent-root identity.  A determinant made only from these
bounded jets is either the original pair (16) or identically dependent.

This is a restricted statement about these canonical local identities,
not a theorem excluding every possible use of the shift equation.

## 5. The exact seed and the low-subdiscriminant obstruction

Take



$$
M=3288,\qquad m=1644,\qquad p=151483.     \tag{25}
$$



The frozen seed certificate proves
$p\mid E_{3286},E_{3288}$.  The replay attached to this note constructs
all coefficients of $f_{3288}$ in $\mathbb F_p[Y]$ and computes
Euclidean polynomial gcds.  It obtains exactly



$$
\boxed{
 \gcd(f_{3288},f_{3288}')=Y,\qquad
 \gcd\!\left({f_{3288}\over Y-1},
       \left({f_{3288}\over Y-1}\right)'\right)=Y.
 }                                                           \tag{26}
$$



The affine map $Y=1+4U$ is invertible over $\mathbb F_p$.  Therefore
(26) says that $P_{1644}$ has gcd of degree one with its derivative,
namely



$$
U+4^{-1}=U+37871.                  \tag{27}
$$



Thus $U=-4^{-1}$ has multiplicity exactly two and every other root is
simple over an algebraic closure of $\mathbb F_p$.  The replay also
finds



$$
P_{1644}(0)=22227\not\equiv0\pmod p.
                                                               \tag{28}
$$



For two polynomials over a field, gcd degree one means that the zeroth
principal subresultant vanishes and the next principal subresultant is
nonzero.  Applied to $P_{1644},P_{1644}'$, (27) proves that the full
resultant/discriminant is the only member at the vanishing end of the
subresultant chain.  A proposed all-$M$ theorem asserting that
simultaneous divisibility of $E_M,E_{M-2}$ also forces the next
principal subresultant, a higher subdiscriminant, or a second independent
multiple root to vanish is therefore false.  The exact seed is not
extrapolated to an asymptotic assertion.

## 6. Height of the normalized full eliminants

Write



$$
f_M(Y)=\sum_{k=0}^m a_kY^k,\qquad
                 a_k=\binom M{2k}E_{M-2k}.                 \tag{29}
$$



The beta-value bound used in the frozen note gives



$$
|a_k|\leq M!.                 \tag{30}
$$



If $H_m(U)=\sum_{j=0}^mh_jU^j$, (15) yields



$$
h_j=4^{j-m}\sum_{k=j}^m\binom kj a_k.                     \tag{31}
$$



The hockey-stick identity and (30) give



$$
|h_j|\leq M!\binom{m+1}{j+1}
       \leq 2^{m+1}M! =:B_M.                               \tag{32}
$$



The coefficients of $P_m=H_m/U$ obey the same bound.  Put $r=m-1$.
Hadamard's inequality on the $(2r-1)$-row Sylvester matrix gives



$$
|\operatorname {Disc}(P_m)|
 \leq
 \bigl(\sqrt{r+1}\,B_M\bigr)^{r-1}
 \bigl(r\sqrt r\,B_M\bigr)^r.                              \tag{33}
$$



This proves (5).  The normalization is materially sharper than applying
the same bound before removing $Y=1$ and the powers of 4, but it does
not change the linear matrix dimension.

The recurrence-based alternative has the same ledger.  Both
$P_m(U_0)$ and $P_{m-1}(U_0)$ vanish modulo $d$, so, whenever it is
nonzero,



$$
d\mid\operatorname {Res}(P_m,P_{m-1}). \tag{34}
$$



Its Sylvester matrix has $2m-3=\Theta(M)$ rows with entries of
logarithmic height $O(M\log M)$, again giving
$O(M^2\log M)$.  If this resultant were zero in characteristic zero,
it would not be an eliminating integer at all; nonvanishing alone would
not improve the height ledger.

Before elimination one already has



$$
d\leq|E_{M-2}|\leq(M-2)!.            \tag{35}
$$



Thus the normalized full discriminant, the recurrence resultant, and
their ordinary Hadamard bounds do not improve the trivial
common-divisor estimate.  Equation (26) shows why one cannot replace the
full discriminant by a universally vanishing higher subdiscriminant.  A
successful route needs an additional arithmetic factor of the full
resultant having provably small height and still containing every
adjacent first-period layer.

## 7. References, replay, and logical boundary

Relevant primary sources are:

1. J. Brillhart, *On the Euler and Bernoulli polynomials*, J. Reine
   Angew. Math. 234 (1969), 45--64,
   <https://doi.org/10.1515/crll.1969.234.45>.  This supplies the
   integral-coefficient and multiple-root facts used above.
2. D. Dumont and J. Zeng, *Polynômes d'Euler et fractions continues de
   Stieltjes--Rogers*, Ramanujan J. 2 (1998), 387--410,
   <https://doi.org/10.1023/A:1009759202242>.  This treats exactly the
   representation $\mathcal E_{2m}(X)=H_m(X(X-1))$ and its recurrence.
3. W. S. Brown and J. F. Traub, *On Euclid's algorithm and the theory of
   subresultants*, J. ACM 18 (1971), 505--514,
   <https://doi.org/10.1145/321662.321665>.  This is the
   subresultant--gcd criterion used in Section 5.

The deterministic companion certificate checks the integral invariant
factorization, affine identities, recurrences, special values,
coefficient bound, and discriminant divisibility on a declared exact
degree grid.  It separately performs the complete degree-1644 modular
gcd computation in (26).  The replay is memory-light and does not use a
hardware accelerator.

From the research directory run

    python3 scripts/root_unity_adjacent_euler_bounded_eliminant_certificate.py
    sha256sum -c results/root_unity_adjacent_euler_bounded_eliminant_hashes.sha256

The all-parameter conclusions are proved in Sections 2--6.  The finite
grids audit formulas, and the one seed is used only as an exact
counterexample to a universal higher-subdiscriminant implication.  This
note does not prove $\log J_N=o(N\log N)$, does not prove irrationality
of $e+\pi$, and does not prove or disprove its transcendence.
