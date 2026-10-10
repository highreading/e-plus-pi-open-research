> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 239 — The corrected actual Witt bridge in the fixed $j=2$ cell

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Continue in the $j=2$, $s\ge2$ cell



$$
4m+1=5p-2s,\qquad
 r=\frac{p-6s-3}{2},\qquad
 q_\nu=2s-\nu,\qquad \nu=0,1.                         \tag{1.1}
$$



Put



$$
P_\nu(z)=(1-z)^r(1+z)^{1+3\nu}(1+z^2)^{q_\nu}.       \tag{1.2}
$$



Item 235 proved that simply lifting the old beta period to
$\mathbb Z/p^2\mathbb Z$ does not recover the actual second digit of
the integer quotient $C_\nu/p$.  This item supplies the correction.

> **PROVED — complete separated Frobenius bridge modulo $p^2$.**
> Let $\widetilde A_p,\widetilde B_p$ be the exact binomial quotients
> in (2.4), and form the three lifted linear moments
> $\widetilde X_\nu,\widetilde Y_\nu,\widetilde Y'_\nu$.  There is an
> explicit quadratic convolution scalar $R_\nu$ such that
> 

$$
> \boxed{\frac{C_\nu}{p}\equiv
> -35(9\widetilde X_\nu-10\widetilde Y_\nu+
> \widetilde Y'_\nu)+35pR_\nu\pmod {p^2}.}             \tag{1.3}
>
$$



> **PROVED — corrected actual endpoint/beta bridge.**  Define the
> canonical lifted beta period $S_\nu^{(2)}$ and the explicit carry
> $K_\nu$ in Section 4.  Then
> 

$$
> \boxed{\frac{C_\nu}{p}\equiv
> -35(-1)^{r+1}\{S_\nu^{(2)}+pK_\nu\}\pmod {p^2}.}     \tag{1.4}
>
$$


> The carry is the sum of a depth-one harmonic/inverse-square endpoint
> term and one depth-two $A_p^2,B_p^2,A_pB_p$ convolution coordinate.
> No unknown scalar remains in (1.4).

> **PROVED — precise extra-digit condition.**  Since $p\ge17$,
> $-35$ is a unit, and
> 

$$
> \boxed{p^3\mid C_\nu
> \iff S_\nu^{(2)}+pK_\nu=0\pmod {p^2}.}               \tag{1.5}
>
$$


> Conditional on the ordinary first digit, put
> $\eta_\nu=S_\nu^{(2)}/p+K_\nu\pmod p$.  Then
> $p^3\mid C_\nu$ exactly when $\eta_\nu=0$.

> **PROVED SCOPED BARRIER — the corrected coefficient kernel is not an
> old fixed-endpoint kernel.**  On the admissible row $p=17,s=2$, the denominators
> $2$ and $6$ have the same class modulo four, but their corrected
> derivative weights are $12$ and $199\pmod {17^2}$.  Thus no fixed
> covector on the old endpoints $1,i,-i$ represents the corrected
> coefficientwise kernel.  This does not exclude an aggregate identity
> on the restricted $P_\nu$ row family caused by coefficient
> cancellations.

> **GLOBAL INTERFACE.**  An ordinary common-log collision is only the
> pair $p^2\mid C_0,C_1$.  It forces the first digits but does not
> force $\eta_0=\eta_1=0$.  Equations (1.4)--(1.5) classify an
> **additional** digit, $p^3\mid C_\nu$; they do not exclude the
> ordinary $j=2$ cell and justify no capacity booking.

> **EXACT FINITE ONLY.**  Direct integer extraction agrees with
> (1.3)--(1.4) on all 148 triples $(p,s,\nu)$ through $p\le101$.
> Through $p\le401$, there are five separate first-digit zeros for
> $\nu=0$, six for $\nu=1$, and no simultaneous common-log row.
> Exactly one separate coefficient has an additional digit:
> $(p,s,\nu)=(227,13,1)$.  It is directly checked as
> $p^3\mid C_1$, but it is not a simultaneous collision.

> **OPEN.**  No useful terminal recurrence has been derived for the
> non-four-periodic corrected kernel, and no all-prime classification
> of simultaneous zeros is known.  Item 239 books zero new rate, zero
> capacity reduction, and no conclusion about $e+\pi$.

## 2. The actual second Frobenius digit

Write



$$
U=1-z,\quad V=1+z^2,\quad U_0=1-z^p,\quad V_0=1+z^{2p},
 \quad G=\frac{U^7}{V^5}.                              \tag{2.1}
$$



The exact coefficient from Item 197 is



$$
C_\nu=[z^{\,5p-q_\nu-1}]G(z)^pP_\nu(z).              \tag{2.2}
$$



The corresponding coefficient of $G(z^p)P_\nu$ is zero by the frozen
degree audit.  Therefore



$$
\frac{C_\nu}{p}
 =[z^{\,5p-q_\nu-1}]
 \frac{G(z)^p-G(z^p)}pP_\nu(z).                       \tag{2.3}
$$



Define the exact integer polynomials



$$
\begin{aligned}
 \widetilde A_p(z)
 &=\frac{(1-z)^p-(1-z^p)}p
   =\sum_{k=1}^{p-1}(-1)^k\frac1p\binom pk z^k,\\
 \widetilde B_p(z)
 &=\frac{(1+z^2)^p-(1+z^{2p})}p
   =\sum_{k=1}^{p-1}\frac1p\binom pk z^{2k}.
\end{aligned}                                                       \tag{2.4}
$$



With



$$
X=\frac{\widetilde A_p}{U_0},\qquad
 Y=\frac{\widetilde B_p}{V_0},                                     \tag{2.5}
$$



one has



$$
G(z)^p=G(z^p)(1+pX)^7(1+pY)^{-5}.                  \tag{2.6}
$$



Expanding modulo $p^3$ before dividing by $p$ gives



$$
\boxed{
\frac{G(z)^p-G(z^p)}p
\equiv G(z^p)\{
7X-5Y+p(21X^2+15Y^2-35XY)
\}\pmod {p^2}.}                                      \tag{2.7}
$$



Thus all three quadratic terms are genuine second-digit data.

Let



$$
H_t=\sum_{a=1}^t\frac1a\pmod p,\qquad H_0=0.          \tag{2.8}
$$



The binomial product formula gives



$$
\begin{aligned}
\widetilde A_p(z)
&\equiv-\sum_{k=1}^{p-1}\frac{1-pH_{k-1}}kz^k
                                                   \pmod {p^2},\\
\widetilde B_p(z)
&\equiv\sum_{k=1}^{p-1}(-1)^{k-1}
\frac{1-pH_{k-1}}kz^{2k}
                                                   \pmod {p^2}.
\end{aligned}                                                       \tag{2.9}
$$



## 3. Exact coefficient separation

Define



$$
\begin{aligned}
\widetilde X_\nu
&=[z^{p-q_\nu-1}]\widetilde A_pP_\nu,\\
\widetilde Y_\nu
&=[z^{p-q_\nu-1}]\widetilde B_pP_\nu,\\
\widetilde Y'_\nu
&=[z^{2p-q_\nu-1}]\widetilde B_pP_\nu
\qquad\pmod {p^2}.
\end{aligned}                                                       \tag{3.1}
$$



Let $A_p=\widetilde A_p\bmod p$ and
$B_p=\widetilde B_p\bmod p$.  For $R,S\in\{A,B\}$, put



$$
(RS)_{h,\nu}
 =[z^{hp-q_\nu-1}]R_p(z)S_p(z)P_\nu(z)\pmod p.        \tag{3.2}
$$



The fixed $z^p$-section coefficients required by (2.7) are



$$
\begin{array}{c|rrrrr}
F(y)&[y^0]F&[y^1]F&[y^2]F&[y^3]F&[y^4]F\\ \hline
(1-y)^6/(1+y^2)^5&1&-6&10&10&-45\\
(1-y)^7/(1+y^2)^6&1&-7&15&7&-70\\
(1-y)^5/(1+y^2)^5&1&-5&5&15&-30\\
(1-y)^7/(1+y^2)^7&1&-7&14&14&-84\\
(1-y)^6/(1+y^2)^6&1&-6&9&16&-54.
\end{array}                                                       \tag{3.3}
$$



The first two rows reproduce the linear term in (1.3).  For the
quadratic terms,



$$
\begin{aligned}
(7[-45],-5[-70],-5[7])
  &=-35(9,-10,1),\\
(21[15],21[-30],15[-7],15[14],15[14],15[-84],
 -35[9],-35[16],-35[-54])
  &=35(9,-18,-3,6,6,-36,-9,-16,54).
\end{aligned}                                                       \tag{3.4}
$$



This is the symbolic coefficient ledger behind (1.3): it involves no
specialization of $p,s,\nu$.  The formal quadratic coefficients
$(21,15,-35)$ are
$\binom72,\binom62,7(-5)$ from (2.7).



$$
\deg P_\nu=\frac{p+2s-1}{2}+\nu,                    \tag{3.5}
$$





$$
\begin{aligned}
\deg(A_p^2P_\nu)&=2p-2+\deg P_\nu,\\
\deg(B_p^2P_\nu)&=4p-4+\deg P_\nu,\\
\deg(A_pB_pP_\nu)&=3p-3+\deg P_\nu.
\end{aligned}                                                       \tag{3.6}
$$



Only these moving sections can reach the target:



$$
\begin{array}{c|c}
\text{product}&h\\ \hline
A_p^2&1,2\\
B_p^2&1,2,3,4\\
A_pB_p&1,2,3.
\end{array}                                                       \tag{3.7}
$$



The next omitted targets exceed the respective degrees by positive
amounts $r+3$, $r+5$, and $r+4$.

Set



$$
\boxed{
\begin{aligned}
R_\nu={}&9(AA)_{2,\nu}-18(AA)_{1,\nu}\\
&-3(BB)_{4,\nu}+6(BB)_{3,\nu}
+6(BB)_{2,\nu}-36(BB)_{1,\nu}\\
&-9(AB)_{3,\nu}-16(AB)_{2,\nu}+54(AB)_{1,\nu}.
\end{aligned}}                                                     \tag{3.8}
$$



Substitution into (2.7) proves



$$
\boxed{
\frac{C_\nu}{p}\equiv
-35(9\widetilde X_\nu-10\widetilde Y_\nu+
\widetilde Y'_\nu)+35pR_\nu\pmod {p^2}.}             \tag{3.9}
$$



## 4. Translation to a corrected beta period

Write



$$
P_\nu(z)=\sum_{\ell=0}^{d_\nu}c_{\nu,\ell}z^\ell,
 \qquad n_\ell=r+\ell+1.                              \tag{4.1}
$$



Reciprocity gives



$$
c_{\nu,d_\nu-\ell}=(-1)^rc_{\nu,\ell},
 \qquad 1\le n_\ell<p.                                \tag{4.2}
$$



Define



$$
C(n)=i^n+(-i)^n,\qquad
 J_\chi(n)=i^{p+n}+(-i)^{p+n},\qquad
 \chi=(-1)^{(p-1)/2}.                                 \tag{4.3}
$$





$$
\begin{array}{c|rrrr}
n\bmod4&0&1&2&3\\ \hline
C(n)&2&0&-2&0\\
J_\chi(n)&0&-2\chi&0&2\chi.
\end{array}                                                       \tag{4.4}
$$



The Item 219 weight is



$$
W_\chi(n)=9-10C(n)+J_\chi(n).                        \tag{4.5}
$$



Consequently the reduction modulo $p$ of the following lifted period
is exactly the ordinary Item 219 beta period (in the same normalization),
not merely an analogous auxiliary quantity.

Define its canonical lift



$$
S_\nu^{(2)}
 =\sum_{\ell=0}^{d_\nu}
 c_{\nu,\ell}\frac{W_\chi(n_\ell)}{n_\ell}
 \pmod {p^2}.                                         \tag{4.6}
$$



The depth-one carry kernel is



$$
\boxed{
\begin{aligned}
K_p^{(1)}(n)={}&-\frac{J_\chi(n)}{n^2}
-9\frac{H_{n-1}}n\\
&+\mathbf1_{2\mid n}\,
10C(n)\frac{H_{n/2-1}}n\\
&-\mathbf1_{2\nmid n}\,
J_\chi(n)\frac{H_{(p+n)/2-1}}n
\pmod p.
\end{aligned}}                                                     \tag{4.7}
$$



Its first term is the high-section denominator carry



$$
\frac1{p+n}=\frac1n-\frac p{n^2}\pmod {p^2}.          \tag{4.8}
$$



For the depth-two part, put



$$
a(t)=[z^t]A_p^2,\quad
 b(t)=[z^t]B_p^2,\quad
 c(t)=[z^t]A_pB_p\pmod p,                             \tag{4.9}
$$



with out-of-support coefficients equal to zero, and set



$$
\boxed{
\begin{aligned}
K_p^{(2)}(n)={}&9a(p+n)-18a(n)\\
&-3b(3p+n)+6b(2p+n)+6b(p+n)-36b(n)\\
&-9c(2p+n)-16c(p+n)+54c(n)
\pmod p.
\end{aligned}}                                                     \tag{4.10}
$$



Finally,



$$
K_\nu=\sum_{\ell=0}^{d_\nu}c_{\nu,\ell}
\{K_p^{(1)}(n_\ell)+K_p^{(2)}(n_\ell)\}\pmod p.        \tag{4.11}
$$



The scalar $\sum_\ell c_{\nu,\ell}K_p^{(2)}(n_\ell)$ is the one
explicit depth-two enlargement in this bridge.  No claim of algebraic
independence from every possible larger cohomology system is needed.

For the proof, apply (4.2) term by term.  The low lifted sections become
the endpoint denominators $n_\ell$; the high lifted $B$-section has
denominator $p+n_\ell$, giving (4.8).  Equation (2.9) produces (4.7).
Applying reciprocity to the nine quadratic sections gives (4.10), with
the common sign $(-1)^r$.  Explicitly,



$$
\begin{aligned}
9\widetilde X_\nu-10\widetilde Y_\nu+\widetilde Y'_\nu
&=(-1)^{r+1}
\left\{S_\nu^{(2)}
+p\sum_\ell c_{\nu,\ell}K_p^{(1)}(n_\ell)\right\},\\
R_\nu
&=(-1)^r\sum_\ell c_{\nu,\ell}K_p^{(2)}(n_\ell).
\end{aligned}                                                       \tag{4.12}
$$



Equations (3.9), (4.11), and (4.12) prove (1.4).

## 5. The exact $p^3$-divisibility condition

Because $-35$ is a unit, (1.4) proves (1.5).  The ordinary first-digit
condition for one coordinate is



$$
S_\nu^{(2)}\equiv0\pmod p.                          \tag{5.1}
$$



Indeed, by (4.5)--(4.6), $S_\nu^{(2)}\bmod p$ is the ordinary Item 219
beta period.  Thus (5.1) is precisely the original per-coordinate first
gate $p^2\mid C_\nu$, expressed in the present normalization.

Under (5.1), the representative $S_\nu^{(2)}\in\{0,\ldots,p^2-1\}$
is divisible by $p$, and



$$
\boxed{
\eta_\nu=\frac{S_\nu^{(2)}}p+K_\nu\pmod p,\qquad
p^3\mid C_\nu\iff\eta_\nu=0.}                         \tag{5.2}
$$



For both coordinates,



$$
\boxed{
p^3\mid C_0,\ C_1
\iff
S_0^{(2)}+pK_0=S_1^{(2)}+pK_1=0\pmod {p^2}.}          \tag{5.3}
$$



This is necessary and sufficient for an additional common digit.  It
does not assert that such rows never occur.

## 6. Why the old order-four terminal machine does not apply

The corrected primitive kernel is



$$
\Phi_p(n)=\frac{W_\chi(n)}n+
 p\{K_p^{(1)}(n)+K_p^{(2)}(n)\}\pmod {p^2}.           \tag{6.1}
$$



After differentiation its weight is



$$
\mathcal W_p(n)=W_\chi(n)+pn
\{K_p^{(1)}(n)+K_p^{(2)}(n)\}\pmod {p^2}.             \tag{6.2}
$$



For a fixed covector $(u,v,w)$ on the three old endpoint coordinates,
the monomial $z^n$ has weight



$$
u+v\frac{i^n+(-i)^n}{2}
   +w\frac{i^n-(-i)^n}{2i}.                           \tag{6.3}
$$



This is identically four-periodic over every coefficient ring.  But for
$p=17$, direct evaluation of the proved kernels (4.7), (4.10) gives



$$
\begin{array}{c|cc}
n&2&6\\ \hline
 [z^{n-r-1}]P_0&1&2\\
 K_p^{(1)}(n)&4&9\\
 K_p^{(2)}(n)&4&4\\
K_p^{(1)}(n)+K_p^{(2)}(n)&8&13\\
n\{K_p^{(1)}(n)+K_p^{(2)}(n)\}\pmod {17}&16&10\\
\mathcal W_p(n)\pmod {17^2}&12&199.
\end{array}                                                       \tag{6.4}
$$



Here $r=1$, so the first table row also verifies directly that both
denominators occur with nonzero coefficient in the actual
$(p,s,\nu)=(17,2,0)$ support.  Since $W_\chi(2)=W_\chi(6)=29$, the
last row is exactly $29+17(16)\equiv12$ and
$29+17(10)\equiv199\pmod {17^2}$.  The denominators are congruent
modulo four.  This proves that the coefficientwise corrected
kernel is non-four-periodic and hence is not in the span of the three
fixed endpoint kernels in (6.3).  This is a proof by contradiction using
the universal four-periodicity of (6.3), not an inference from a scan.
It does not rule out cancellation after summation against the restricted
coefficient vectors of $P_\nu$, a larger endpoint/cohomology system, or
a new recurrence with the explicit bulk carry (6.2).

## 7. Exact finite replay

The direct integer replay covers all 74 admissible rows through
$p\le101$, hence 148 triples $(p,s,\nu)$.  It evaluates the integer
$C_\nu$, verifies (3.9) and (1.4), and checks the equivalence (1.5).

The 1,115-row census through $p\le401$ has the following separate
first-digit zeros:



$$
\begin{array}{r|r|c|r|r|r}
p&s&\nu&\eta_\nu&K_\nu^{(1)}&K_\nu^{(2)}\\ \hline
109&8&1&19&8&102\\
131&11&0&4&36&29\\
173&16&0&79&49&19\\
191&3&0&33&79&89\\
211&7&1&29&160&194\\
227&13&1&0&131&42\\
337&28&1&149&149&172\\
367&5&1&348&322&106\\
367&9&0&25&277&46\\
383&9&1&25&156&50\\
383&53&0&345&177&285.
\end{array}                                                       \tag{7.1}
$$



Thus the first-zero counts are $5$ and $6$.  The only individual
additional digit is



$$
(p,s,\nu)=(227,13,1).                                \tag{7.2}
$$



Direct integer extraction at this row gives



$$
m=277,\qquad
 C_1\equiv0\pmod {227^3},\qquad
 S_1^{(2)}+227K_1\equiv0\pmod {227^2}.                \tag{7.3}
$$



There is no simultaneous first-digit common-log row through the finite
bound, so (7.2) is not a collision.  No asymptotic inference is made.

## 8. Reproducibility, status, and booking

The standard-library checker item239_j2_actual_witt_bridge_certificate.py:

1. reconstructs the binomial quotients and checks (2.9);
2. derives all fixed sections in (3.3);
3. evaluates the symbolic section ledger and the lifted-linear and nine
   quadratic moments in (3.9);
4. evaluates both endpoint kernels (4.7), (4.10);
5. compares both bridges against exact integer $C_\nu$;
6. replays the $p^3$-equivalence; and
7. produces the bounded census and the non-four-periodic witness.

From the archive root, run:

    python scripts/item239_j2_actual_witt_bridge_certificate.py --output results/item239_j2_actual_witt_bridge_certificate.json
    python scripts/item239_j2_actual_witt_bridge_certificate.py --output results/item239_j2_actual_witt_bridge_certificate_replay.json

Canonical and replay outputs are byte-identical and contain no host
path, timestamp, random seed, or elapsed time.

### Status ledger

**PROVED**

- the complete actual quotient $C_\nu/p\bmod p^2$;
- the separated lifted-linear and quadratic bridge (3.9);
- the corrected endpoint bridge (1.4);
- the necessary and sufficient $p^3$-condition (5.2); and
- the coefficientwise non-four-periodic fixed-endpoint barrier (6.4).

**EXACT FINITE ONLY**

- the 148 direct integer comparisons through $p\le101$;
- the 1,115-row census through $p\le401$; and
- the individual row (7.2).

**OPEN**

- a useful terminal recurrence for the corrected kernel;
- an aggregate old-endpoint identity on the restricted $P_\nu$ row
  family through coefficient cancellations;
- an all-prime classification of simultaneous zeros;
- any zero-rate theorem or exclusion of the ordinary $j=2$ cell; and
- any new Route-1 rate or divisibility exponent.

The booking is



$$
\boxed{
\text{new unconditional log rate}=0,\qquad
\text{new divisibility exponent}=0,\qquad
\text{capacity reduction}=0.}                        \tag{8.1}
$$



Item 239 proves no statement about the arithmetic nature of $e+\pi$.
