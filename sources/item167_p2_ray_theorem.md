> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 167 — exact valuation three on the prime-square ray

Date: 2026-08-29

## 1. Scope and verdict

Put



$$
u=x(1-x),\qquad Q=(1+x)(1+x^2),\qquad
\omega_s={u^{6m}\over Q^{4m+1+s}}\,dx\quad(s=0,1).
$$



Write the endpoint coordinates as



$$
H_s=R_s+{L_s\over4}\log 2+{E_s\over8}\pi
$$



and retain the item-163 minors



$$
\mathscr A=L_1(pR_0)-L_0(pR_1)=pA_m,\qquad
\mathscr B=L_1E_0-L_0E_1=8B_m.                  \tag{1.1}
$$



This note treats the pre-tail prime-square ray



$$
\boxed{
p=20k+19\ {\rm prime},\qquad
\ell=2k+1,\qquad
m=18k+17+\ell p={p^2-1\over10}.}                \tag{1.2}
$$



The conclusions are:

**PROVED — all-prime third layer.** Every prime in (1.2) satisfies



$$
\boxed{p^3\mid c_m.}                             \tag{1.3}
$$



The missing item-164 endpoint determinant is reduced to an explicit
proper Hermite primitive. Comparing it with a zero-resonance Frobenius
primitive reduces both endpoint values to



$$
\sum_{r=0}^{(p-1)/2}{1\over4r+1}=0\pmod p.       \tag{1.4}
$$



The terms in (1.4) cancel under a fixed-point-free involution.

**PROVED — exact fourth-layer obstruction.** The first remaining period
digit has the closed form



$$
\boxed{b_1=-2h\lambda\gamma\delta\ne0\pmod p.}    \tag{1.5}
$$



Therefore



$$
\boxed{v_p(c_m)=3};
\qquad\text{in particular }p^4\nmid c_m.         \tag{1.6}
$$



**PROVED — zero-rate limitation.** This theorem is arithmetically thin.
At fixed $m$, (1.2) supplies at most one prime, and



$$
\log p={1\over2}\log(10m+1)=O(\log m)=o(m).       \tag{1.7}
$$



It gives no positive exponential content rate.

**EXPERIMENTAL — exact finite replay only.** The certificate checks all
38 ray primes through $p\le2000$, ending at $p=1999$, with no third-layer
failure and no fourth-layer survivor. For



$$
p=19,59,79,139,179,199                            \tag{1.8}
$$



it also recomputes the deeper Hasse digits independently. These finite
rows audit the theorem; they are not its proof.

**OPEN.** No positive-mass third or fourth layer outside the thin divisor
set of $10m+1$, no improved Route-1 exponential constant, and no result
about the rationality, irrationality, or transcendence of $e+\pi$ is
claimed.

## 2. Exact band and degree hypotheses

The complete item-164 slab is



$$
p=20k+19,\qquad m=18k+17+\ell p,\qquad
0\le\ell\le5k+3.                                  \tag{2.1}
$$



The ray value $\ell=2k+1$ lies in this interval. Direct substitution gives



$$
10m+1=p^2,\qquad
4m+1={2p^2+3\over5},\qquad
4m+2={2p^2+8\over5}.                              \tag{2.2}
$$



Consequently



$$
p\le4m+1<p^2.                                      \tag{2.3}
$$



Thus the applicable top prime power is exactly $q_p=p$, or $e_p=1$.
The top inequality is strict: the ray has $4m+1\ne p^2$, although it has
$10m+1=p^2$. This distinction is essential because the item-163
normalization changes at $e_p=2$.

Set



$$
\alpha=5+6\ell=12k+11,\qquad d=4+4\ell=8k+8,       \tag{2.4}
$$



and, after the item-164 second Cartier step,



$$
n=\alpha-1=12k+10,\qquad K=d+1=8k+9.              \tag{2.5}
$$



The prime-square identity is exactly



$$
\alpha+d=p,\qquad n+K=p,                           \tag{2.6}
$$



and all relevant exponents satisfy



$$
0<d<K<p,\qquad 0<n<p.                              \tag{2.7}
$$



These inequalities ensure separable $p$-integral partial fractions,
pole order $K<p$, and no unrecorded $p^2$-denominator band.

For $e_p=1$ and the item-163 zero-shift ledger, write



$$
{\mathscr A\over p}=a_0+a_1p+a_2p^2+\cdots,\qquad
{\mathscr B\over p}=b_0+b_1p+b_2p^2+\cdots.        \tag{2.8}
$$



The slab already has $a_0=b_0=0$, and



$$
v_p(U_m)=1+v_p(\mathscr A/p),\qquad
v_p(V_m)=2+v_p(\mathscr B/p),\qquad
v_p(c_m)=\min\{v_p(U_m),v_p(V_m)\}.                \tag{2.9}
$$



Hence $p^3\mid c_m$ reduces to $a_1=0$. Once this is proved,
$b_1\ne0$ forces the exact value (1.6), independently of $a_2$.

## 3. The second-Cartier collapse

Let



$$
\mathfrak D=uQ=x(1-x^4),\qquad
\rho=8k+7={2p-3\over5},                            \tag{3.1}
$$



and let the zero-constant polynomials $T_s$ be defined by



$$
T_0'=\mathfrak D^\rho,\qquad
T_1'={\mathfrak D^\rho\over Q}
    =x^\rho(1-x)(1-x^4)^{\rho-1}.                 \tag{3.2}
$$



All divisions defining these primitives are $p$-integral. On the ray,
$d\equiv-\alpha\pmod p$, so the item-164 numerator becomes



$$
N_s=T_s\{\alpha u'Q-dQ'u\}
   =\alpha T_s\mathfrak D'
   \quad\text{in }\mathbb F_p[x].                  \tag{3.3}
$$



The exact second-Cartier coefficient filter therefore has support



$$
H_0=h x^4,\qquad H_1=\lambda x^3+\mu x^4.          \tag{3.4}
$$



Indeed, $N_0$ has only exponents $0\pmod4$, whereas $N_1$ has only
exponents $0,1\pmod4$. Since $p\equiv3\pmod4$ and
$\deg H_s\le5$, the filter leaves precisely (3.4).

Put



$$
G={u^n x^3\over Q^K}\,dx,\qquad X=xG.              \tag{3.5}
$$



The transformed pair is



$$
\Phi_0=hX,\qquad \Phi_1=\lambda G+\mu X.            \tag{3.6}
$$



Define



$$
\gamma=(-1)^{7k+6}{n\choose7k+6},\qquad
\delta=(-1)^{2k+1}{n\choose2k+1}.                  \tag{3.7}
$$



Writing



$$
G={P\over Q^p}\,dx,\qquad P=x^{n+3}(1-x^4)^n,      \tag{3.8}
$$



shows that the only Cartier-selected term of $P\,dx$ is at exponent
$2p-1$. For $xP\,dx$, the only selected term is at exponent $p-1$.
Thus



$$
\mathcal C(G)=\gamma{x\over Q}\,dx,\qquad
\mathcal C(X)=\delta{1\over Q}\,dx.                \tag{3.9}
$$



Because $p\equiv3\pmod4$, Frobenius fixes the logarithmic coordinate and
negates the circular coordinate. The elementary integrals



$$
\int_0^1{dx\over Q}={1\over4}\log2+{1\over8}\pi,\qquad
\int_0^1{x\,dx\over Q}=-{1\over4}\log2+{1\over8}\pi
                                                               \tag{3.10}
$$



therefore give



$$
(L(G),E(G))=(-\gamma,-\gamma),\qquad
(L(X),E(X))=(\delta,-\delta).                    \tag{3.11}
$$



Set



$$
W=\delta G+\gamma X+\gamma\delta{dx\over1+x^2}.   \tag{3.12}
$$



Since



$$
\mathcal C\left({dx\over1+x^2}\right)
   =-{dx\over1+x^2},\qquad
{x+1\over Q}={1\over1+x^2},                      \tag{3.13}
$$



equation (3.9) gives $\mathcal C(W)=0$. Hence $W$ is an exact rational
differential. Absolute exactness alone does not imply equal endpoint
values; that relative statement is proved next.

## 4. Relative endpoint lemma

### 4.1 Proper primitive and zero-resonance primitive

The differential $W$ has poles only at the three roots of $Q$, of order
at most $K<p$, and it is $O(x^{-2})dx$ at infinity. Its unique primitive
normalized to vanish at infinity has the form



$$
F={A(x)\over Q(x)^d},\qquad \deg A<3d.             \tag{4.1}
$$



Here $A$ is a Hermite numerator, not the item-163 integer $A_m$.

Multiplying the denominator of $W$ from $Q^K$ to $Q^p$ gives



$$
W={P_*(x)\over Q(x)^p}\,dx,                        \tag{4.2}
$$



where



$$
\boxed{
P_*=(\delta x^3+\gamma x^4)\mathfrak D^n
   +\gamma\delta(1+x)^p(1+x^2)^{p-1}.}             \tag{4.3}
$$



The two summands have degrees at most $3p-3$ and $3p-2$.
Since $\mathcal C(W)=0$, the coefficients of $P_*$ at the only possible
resonant exponents $p-1$ and $2p-1$ vanish. Therefore



$$
T(x)=\sum_j{[x^j]P_*\over j+1}x^{j+1}             \tag{4.4}
$$



is a well-defined zero-constant polynomial over $\mathbb F_p$; at the
two resonant indices the numerator is literally zero. It satisfies



$$
W=d\left({T\over Q^p}\right),\qquad \deg T\le3p-1. \tag{4.5}
$$



The primitive in (4.5) is the zero-resonance Frobenius primitive, not the
proper Hermite primitive (4.1). Their difference has zero derivative.
Since $\mathbb F_p$ is perfect,



$$
{T\over Q^p}-{A\over Q^d}=H(x)^p                 \tag{4.6}
$$



for some $H\in\mathbb F_p(x)$. Multiplication by $Q^p$ gives



$$
T=AQ^{n+1}+J(x)^p.                                 \tag{4.7}
$$



The left side is polynomial, so $J=HQ$ is polynomial. Moreover



$$
\deg(AQ^{n+1})<3d+3(n+1)=3p,
$$



and hence



$$
\deg J\le2.                                        \tag{4.8}
$$



This comparison uses every required degree and pole-order hypothesis:
$K<p$, $\deg A<3d$, $\deg P_*\le3p-2$, and
$n+d+1=p$.

### 4.2 Quadratic interpolation

Let $i^2=-1$ in the residue splitting field. Evaluating (4.7) at the
three roots of $Q$, and using $p\equiv3\pmod4$, yields



$$
T(-1)=J(-1),\qquad T(i)=J(-i),\qquad T(-i)=J(i).   \tag{4.9}
$$



Write



$$
T=\sum_e t_ex^e,\qquad
S_r=\sum_{e\equiv r\ (4)}t_e.                     \tag{4.10}
$$



For the general quadratic $J=c_0+c_1x+c_2x^2$, the three interpolation
conditions (4.9) give



$$
c_0=S_0-S_1,\qquad
J(1)=S_0+S_2+S_3-3S_1,                            \tag{4.11}
$$



and therefore



$$
T(1)-J(1)=4S_1.                                    \tag{4.12}
$$



Also, because $T(0)=0$, equation (4.7) gives



$$
A(0)=-c_0.                                         \tag{4.13}
$$



Thus it is enough to prove $S_0=S_1=0$.

### 4.3 Fixed-point-free cancellation

The first summand of (4.3) has exponent classes $1,2\pmod4$, because
$n\equiv2\pmod4$. After the integration in (4.4), it contributes only
to $S_2,S_3$.

For the second summand, Fermat gives



$$
(1+x)^p(1+x^2)^{p-1}
=(1+x^p)\sum_{j=0}^{p-1}(-1)^j x^{2j}.             \tag{4.14}
$$



Only even $j=2r$ contribute to $S_0$ or $S_1$. The unshifted term has
primitive exponent $4r+1$ and contributes to $S_1$; the $x^p$-shifted
term has primitive exponent $p+4r+1\equiv0\pmod4$ and contributes to
$S_0$. Their denominators are congruent modulo $p$. None is resonant:
the potentially resonant index $(p-1)/2=10k+9$ is odd. Hence



$$
S_0=S_1
=\gamma\delta\sum_{r=0}^{(p-1)/2}{1\over4r+1}.     \tag{4.15}
$$



Every denominator is a unit. Indeed,
$1\le4r+1\le2p-1$, and equality to the only multiple $p$ in this
interval is impossible: $p\equiv3\pmod4$, whereas
$4r+1\equiv1\pmod4$.

Apply the involution



$$
r\longmapsto r'={p-1\over2}-r.                    \tag{4.16}
$$



It preserves the index interval and satisfies



$$
4r'+1\equiv-(4r+1)\pmod p.                        \tag{4.17}
$$



It has no fixed point. A fixed point would imply $4r=p-1$, impossible
because $p-1\equiv2\pmod4$. Thus the sum cancels in pairs:



$$
S_0=S_1=0.                                         \tag{4.18}
$$



Equations (4.11)--(4.13) now give



$$
J(0)=A(0)=0,\qquad T(1)=J(1).                     \tag{4.19}
$$



Evaluating (4.7) at $x=1$, where $Q(1)=4$, gives



$$
A(1)4^{n+1}=T(1)-J(1)=0.                          \tag{4.20}
$$



Therefore the proper primitive vanishes at both endpoints:



$$
[F]_0^1=0,\qquad R(W)=0.                          \tag{4.21}
$$



This is the required relative endpoint theorem.

## 5. Third digit, fourth digit, and nonvanishing

From (3.6) and (3.11), the item-164 next $A$-digit is



$$
\begin{aligned}
a_1
 &=L(\Phi_1)R(\Phi_0)-L(\Phi_0)R(\Phi_1)\\
 &=-h\lambda\{\gamma R(X)+\delta R(G)\}\\
 &=-h\lambda R(W)=0.                               \tag{5.1}
\end{aligned}
$$



Equations (2.8)--(2.9) prove $p^3\mid c_m$.

The period determinant of the transformed pair is



$$
L(\Phi_1)E(\Phi_0)-L(\Phi_0)E(\Phi_1)
=2h\lambda\gamma\delta.                            \tag{5.2}
$$



Frobenius fixes $L$ and changes the sign of $E$, so the actual next digit
in $\mathscr B/p$ is



$$
b_1=-2h\lambda\gamma\delta.                        \tag{5.3}
$$



It remains to prove that every factor is nonzero.

First, (3.2)--(3.4) give



$$
h=-4\alpha T_0(1),\qquad
T_0(1)={1\over4}{(2k+1)!(8k+7)!\over(10k+9)!}.    \tag{5.4}
$$



Every factorial argument is below $p$, so $h\ne0$.

Next let $S$ be the sum of the $1\pmod4$ coefficients of $T_1$.
Expanding (3.2) and applying the reciprocal binomial identity gives



$$
\begin{aligned}
S
 &=-\sum_{q=0}^{\rho-1}
 {(-1)^q{\rho-1\choose q}\over \rho+4q+2}\\
 &=-{1\over4}{(\rho-1)!\over((\rho+2)/4)_\rho},
\qquad \lambda=-4\alpha S.                        \tag{5.5}
\end{aligned}
$$



The integer denominators $\rho+2+4q$ lie between $8k+9$ and $2p-5$.
The only possible multiple of $p$ would be $p$, but



$$
p-(\rho+2)=12k+10\not\equiv0\pmod4.               \tag{5.6}
$$



Thus all factors in (5.5) are units and $\lambda\ne0$.

Finally, the two indices in (3.7) lie between $0$ and $n<p$, so
$\gamma\delta\ne0$. Since $p$ is odd, (5.3) is nonzero. Equation (2.9)
then gives



$$
v_p(V_m)=3,\qquad v_p(U_m)\ge3,\qquad
\boxed{v_p(c_m)=3}.                                \tag{5.7}
$$



## 6. Infinitude and thinness

Dirichlet's theorem supplies infinitely many primes
$p\equiv19\pmod {20}$, so (5.7) is an infinite all-prime theorem on this
ray. It remains a zero-rate theorem because



$$
10m+1=p^2.                                         \tag{6.1}
$$



For fixed $m$, at most one positive prime satisfies (6.1). Its full
third-copy logarithmic contribution is at most $3\log p=O(\log m)=o(m)$;
the newly gained copy alone contributes only $\log p$. Nothing here
changes a prime-number-theorem-scale content constant.

## 7. Exact certificate and replay

From the archive root, the archive-relative replay is:

    python scripts/item167_p2_ray_certificate.py --prime-bound 2000 --direct-bound 200 --output results/item167_p2_ray_certificate_p2000.json

In the staging workspace, replace scripts and results by work. The
checker:

1. reconstructs the exact item-164 $H_0,H_1,\Phi_0,\Phi_1$ row;
2. verifies (3.4), (3.7), (5.4), and (5.5);
3. constructs $P_*$, checks its two zero resonances, and verifies
   $S_0=S_1=0$ by (4.15)--(4.18);
4. checks $a_1=0$ and the exact nonzero value (5.3); and
5. independently recomputes $a_0,a_1,b_0,b_1$ through the deeper Hasse
   tower for the six primes in (1.8).

Two canonical runs are byte-identical. The companion SHA-256 manifest
pins the report, checker, dependency, and both JSON files.

## 8. Status ledger

### PROVED

- The relative endpoint identity $R(W)=0$ for every prime on (1.2).
- The all-prime divisibility $p^3\mid c_m$.
- The nonzero fourth-layer digit (5.3), hence $v_p(c_m)=3$.
- Infinitude of the ray and its $O(\log m)=o(m)$ logarithmic mass.

### EXPERIMENTAL FINITE

- All 38 ray primes through $p\le2000$ satisfy the exact certificate.
- Six independent deeper-Hasse computations give



$$
(p,b_1)=(19,4),(59,50),(79,14),(139,24),(179,150),(199,34),
$$



with $a_0=a_1=b_0=0$ in every row.

### OPEN

- A positive-mass deeper layer outside the thin set $p\mid10m+1$.
- Any improvement of the proved Route-1 exponential content rate.
- Any conclusion about $e+\pi$.
