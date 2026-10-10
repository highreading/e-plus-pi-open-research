> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Endpoint periods, a scalar recurrence, and a nonvanishing Casoratian

Date: 2026-08-27.

## 1. Outcome

Fix an even integer $n\ge2$ and an odd prime $p>2n+1$, and put



$$
c=\frac{p-2n-1}{2}.
 \tag{1}
$$



For the $c$ admissible one-block large-prime parameters



$$
s_v=2v+1,\qquad
 K_v=n+\frac{p+s_v}{2},\qquad
 u_v=c-v
 \quad(0\le v\le c-1),
 \tag{2}
$$



let $D_v=D_{n,K_v,p}$ and $U_v=U_{n,K_v,p}$ be the accepted central
and rational-coordinate digits.  This note proves four exact facts.

1. The central digit is a second endpoint period of the same integrand
   that produces $U_v$.
2. Every endpoint period satisfies one scalar order-three recurrence
   whose coefficients depend only on $n,v$, not on $p$.
3. The three scalar solutions 

$$
D_v,\operatorname {Re}I_v,
   \operatorname {Im}I_v
$$

 have an explicit nonzero initial Casoratian.
4. Consequently, on the generic branch $v_p(q_n)=1$, the matching
   residual

   

$$
F_v=4(q_n/p)U_v-p_nD_v\pmod p
    \tag{3}
$$



   is not the zero solution and cannot vanish at three consecutive
   admissible values of $v$.

This is a local restriction on adjacent forms.  It is not a bound on
the total number of separated zeros: exact target examples with two
separated returns remain, and an arbitrary solution of the scalar
operator can have at least three nonconsecutive or partly consecutive
zeros.

All arithmetic below takes place in the Gaussian residue ring
$\mathcal R_p=\mathbb F_p[i]$.  No argument treats this ring as a field.
Every displayed division is by a proved nonzero scalar in
$\mathbb F_p$.

## 2. Both Fourier digits are endpoint periods

Retain



$$
P_n(z)=(1-i)^n(z-1)^n(z-i)^n,\qquad
 R_v(z)=P_n(z)(1+z)^{2v+1}.
 \tag{4}
$$



For a polynomial of degree at most $p-2$, use the formal endpoint
integral



$$
\int_a^b\sum_r f_rz^r\,dz
 =\sum_r f_r\frac{b^{r+1}-a^{r+1}}{r+1}.
 \tag{5}
$$



Define



$$
I_v=\int_1^i z^{u_v-1}R_v(z)\,dz.
 \tag{6}
$$



The accepted digit formula gives



$$
U_v=\operatorname {Im}I_v.
 \tag{7}
$$



The central digit has the companion representation



$$
\boxed{
 D_v=\int_{-1}^{0}z^{u_v-1}R_v(z)\,dz.}
 \tag{8}
$$



### Proof of (8)

Write $d_v=2n+2v+1=\deg R_v$ and
$R_v(z)=\sum_{t=0}^{d_v}\rho_tz^t$.  Since $n$ is even,



$$
z^{2n}P_n(z^{-1})=\overline {P_n(z)}.
 \tag{9}
$$



Indeed,



$$
\begin{aligned}
 z^{2n}P_n(z^{-1})
 &=(1-i)^n(1-z)^n(1-iz)^n\\
 &=(1-i)^n(-i)^n(z-1)^n(z+i)^n
 =\overline {P_n(z)},
\end{aligned}
$$



because
$(1-i)^n(-i)^n/(1+i)^n=(-i)^{2n}=1$.
The factor $(1+z)^{2v+1}$ is reciprocal, so



$$
z^{d_v}R_v(z^{-1})=\overline {R_v(z)},\qquad
 \rho_{d_v-t}=\overline{\rho_t}.
 \tag{10}
$$



The exact first-digit formula is



$$
D_v=\sum_{t=0}^{d_v}\rho_t
       \frac{(-1)^{K_v-t-1}}{K_v-t}.
 \tag{11}
$$



Since $K_v-d_v=u_v$, reverse the index in (11) and apply (10):



$$
D_v=\sum_{t=0}^{d_v}\overline{\rho_t}
       \frac{(-1)^{u_v+t-1}}{u_v+t}.
 \tag{12}
$$



The right side is the conjugate of the integral in (8).  The accepted
first-digit theorem also proves $D_v\in\mathbb F_p$.  Hence conjugating
(12) proves (8). $\square$

## 3. A $p$-independent scalar order-three operator

For a path $\gamma$ whose endpoints belong to
$\{-1,0,1,i\}$, put



$$
I_v^\gamma=\int_\gamma z^{u_v-1}R_v(z)\,dz,\qquad
 J_v^\gamma=\int_\gamma z^{u_v}R_v(z)\,dz.
 \tag{13}
$$



The integration-by-parts proof of the coupled three-state recurrence
applies to all these paths.  At $-1,1,i$, the exact derivative terms
vanish because of the factors
$(z+1)(z-1)(z-i)$.  At $0$, they vanish because
$u_v\ge3$ on the recurrence range.  Thus every state



$$
\mathbf S_v^\gamma=
 (I_v^\gamma,I_{v+1}^\gamma,J_v^\gamma)^T
 \tag{14}
$$



obeys the same transition.

The relation $2c+2n+1=p$ gives



$$
c\equiv-n-\frac12\pmod p.
 \tag{15}
$$



Substitution of (15) into the exact Gaussian transition simplifies it
to



$$
\mathbf S_{v+1}^\gamma=M_v\mathbf S_v^\gamma,
 \tag{16}
$$



where, with $T_v=2n+2v+5$,



$$
M_v=\frac1{T_v}
 \begin{pmatrix}
 0&T_v&0\\
 -16(v+1)-4in&2(3n+6v+11+in)&-4in\\
 2(n+2-i(n+4v+4))&i(2n+2v+3)&2(n+4v+6-in)
 \end{pmatrix}.
 \tag{17}
$$



For $0\le v\le c-3$, one has $0<T_v<p$, so this denominator is a
unit.

Define



$$
E_v=(2n+2v+5)(2n+2v+7)
 \tag{18}
$$



and



$$
Q_v=n^2+12nv+21n+16v^2+58v+53.
 \tag{19}
$$



### Theorem 3.1

The first coordinate $X_v$ of every solution of (16) satisfies



$$
\boxed{
\begin{aligned}
 E_vX_{v+3}
 ={}&64(v+1)(2v+3)X_v-8Q_vX_{v+1}\\
 &+2(2n+2v+5)(4n+10v+23)X_{v+2}
\end{aligned}}
 \tag{20}
$$



for $0\le v\le c-4$.  The same equation holds separately for the
real and imaginary coordinates of $X_v$.

### Proof

Let $e_1,e_2,e_3$ denote the coordinate row vectors.  Direct
multiplication of the two matrices in (17) gives the row identity



$$
e_2M_{v+1}M_v
 =A_ve_1+B_ve_2+C_ve_2M_v,
 \tag{21}
$$



where



$$
A_v=\frac{64(v+1)(2v+3)}{E_v},\qquad
 B_v=-\frac{8Q_v}{E_v},\qquad
 C_v=\frac{2(4n+10v+23)}{2n+2v+7}.
 \tag{22}
$$



Apply (21) to $\mathbf S_v^\gamma$.  Its four terms are respectively
$I_{v+3}^\gamma,I_v^\gamma,I_{v+1}^\gamma,I_{v+2}^\gamma$.
This proves (20).  All coefficients in (22) lie in $\mathbb F_p$, so
taking either coordinate proves the last assertion. $\square$

The forward and backward pivots in (20) are units.  On the stated range,



$$
0<2n+2v+5<2n+2v+7<p,
 \tag{23}
$$



and



$$
0<v+1<p,\qquad0<2v+3<p.
 \tag{24}
$$



In particular, a scalar solution that has three consecutive zeros is
the zero solution on its entire admissible range: (20) propagates the
triple forward using (23) and backward using (24).

### Scalar Wronskian

For three scalar solutions $X^{(1)},X^{(2)},X^{(3)}$, define



$$
W_v=\det\left(X^{(j)}_{v+r}\right)_
                 {\substack{0\le r\le2\\1\le j\le3}}.
 \tag{25}
$$



The companion matrix of (20) has determinant $A_v$, so



$$
W_{v+1}=A_vW_v.
 \tag{26}
$$



Equivalently,



$$
W_v\prod_{j=0}^{v-1}A_j^{-1}
 \tag{27}
$$



is an exact conserved scaled Wronskian.  This invariant says whether
three solutions form a basis; it does not bound separated zeros of one
solution.

## 4. The factorial normalization and an exact right factor

Recall



$$
D_v=\kappa_v\Phi_n(2v+1),\qquad
 \kappa_v=-\frac{(2v+1)!}{n!\ell_v!K_v!}.
 \tag{28}
$$



Modulo $p$, the consecutive normalization ratio loses all dependence
on $p$:



$$
\frac{\kappa_{v+1}}{\kappa_v}
 =\frac{8(v+1)}{2n+2v+3}.
 \tag{29}
$$



Thus $\widetilde X_v=X_v/\kappa_v$ satisfies



$$
\widetilde X_{v+3}
 =\widehat A_v\widetilde X_v
  +\widehat B_v\widetilde X_{v+1}
  +\widehat C_v\widetilde X_{v+2},
 \tag{30}
$$



where



$$
\widehat A_v=
 \frac{(2v+3)(2n+2v+3)}{8(v+2)(v+3)},
 \tag{31}
$$





$$
\widehat B_v=
 -\frac{n^2+12nv+21n+16v^2+58v+53}{8(v+2)(v+3)},
 \tag{32}
$$





$$
\widehat C_v=
 \frac{4n+10v+23}{4(v+3)}.
 \tag{33}
$$



Equations (30)--(33) answer the normalization question exactly: the
normalized scalar operator is $p$-independent; only the coefficient
field and finite admissible index range remember $p$.

There is also an exact factor after the known polynomial solution.  For
fixed even $n$, set



$$
\phi_v=\Phi_n(2v+1),\qquad r_v=\frac{\phi_{v+1}}{\phi_v}
 \in\mathbb Q(v).
 \tag{34}
$$



Let $E$ be the forward shift and



$$
\widehat L=E^3-\widehat C_vE^2-\widehat B_vE-\widehat A_v.
 \tag{35}
$$



In the Ore ring $\mathbb Q(v)[E]$,



$$
\boxed{
 \widehat L=
 \left(E^2+\alpha_vE+\beta_v\right)(E-r_v),}
 \tag{36}
$$



where



$$
\alpha_v=r_{v+2}-\widehat C_v,\qquad
 \beta_v=\alpha_vr_{v+1}-\widehat B_v
        =\frac{\widehat A_v}{r_v}.
 \tag{37}
$$



Expansion uses $Ef(v)=f(v+1)E$.  The equality between the two
expressions for $\beta_v$ is precisely (30) applied to $\phi_v$.
This factorization is an identity of rational functions, so it does not
require $\phi_v$ to be nonzero after reduction at every individual
finite-field index.

The factor has coefficient complexity of degree $n/2$ through
$\phi_v$.  It therefore does not by itself give a uniform zero count.
No symmetric-square assertion is made here.

## 5. The initial contour Casoratian is always a unit

Assume $c\ge3$, so the first three admissible indices exist.  Form



$$
\mathcal C_{n,c}=
 \begin{pmatrix}
 D_0&\operatorname {Re}I_0&\operatorname {Im}I_0\\
 D_1&\operatorname {Re}I_1&\operatorname {Im}I_1\\
 D_2&\operatorname {Re}I_2&\operatorname {Im}I_2
 \end{pmatrix}.
 \tag{38}
$$



Put $r=n/2$ and



$$
\chi(c)=(-1)^{c(c+1)/2}.
 \tag{39}
$$



### Theorem 5.1

The following equality holds in $\mathbb F_p$, with the rational
number on the right reduced modulo $p$:



$$
\boxed{
\begin{aligned}
 \det\mathcal C_{n,c}
 ={}&(-1)^{r+1}\chi(c)
 \frac{2^{24}}{3^4\,5^2\,7^2}\\
 &\times
 \prod_{j=1}^{r-1}
 \frac{2^{14}(j+1)^3(2j+1)^2}
 {j(4j+5)(4j+7)^2(4j+9)}.
\end{aligned}}
 \tag{40}
$$



In particular,



$$
\boxed{\det\mathcal C_{n,c}\ne0\pmod p.}
 \tag{41}
$$



### Proof

For $n=2$, direct expansion of the three endpoint integrals, after
using $c\equiv-5/2\pmod p$, gives



$$
\det\mathcal C_{2,c}
 =\chi(c)\frac{2^{24}}{3^4\,5^2\,7^2}.
 \tag{42}
$$



It remains to prove the product ratio.  Keep $p$ fixed and replace



$$
(n,c)\longmapsto(n+2,c-2).
 \tag{43}
$$



With



$$
A_{n,c}(z)=P_n(z)(1+z)z^{c-1},\qquad
 w(z)=\frac{(1+z)^2}{z},
 \tag{44}
$$



one has



$$
A_{n+2,c-2}(z)=H(z)A_{n,c}(z),\qquad
 H(z)=-2i\,z^{-2}(z-1)^2(z-i)^2.
 \tag{45}
$$



Exact Hermite reduction of $H(z)w(z)^v$, for $v=0,1,2$, modulo a
derivative whose endpoint values vanish gives



$$
\begin{pmatrix}
 I^{\gamma}_{n+2,c-2,0}\\
 I^{\gamma}_{n+2,c-2,1}\\
 I^{\gamma}_{n+2,c-2,2}
 \end{pmatrix}
 =
 T_n
 \begin{pmatrix}
 I^{\gamma}_{n,c,0}\\
 I^{\gamma}_{n,c,1}\\
 I^{\gamma}_{n,c,2}
 \end{pmatrix}
 \tag{46}
$$



for each relevant endpoint path $\gamma$.  The exact matrix is



$$
T_n=
\begin{pmatrix}
\dfrac{16(2n^2-3n-8)}{n(2n+5)}
&
\dfrac{4(8n+11)(n+4)}{n(2n+5)}
&
-\dfrac{2(3n+4)}n
\\
-\dfrac{384(3n+4)}{n(2n+5)(2n+7)}
&
\dfrac{16(7n^3+59n^2+166n+132)}
      {n(2n+5)(2n+7)}
&
-\dfrac{16(n^2+6n+6)}{n(2n+7)}
\\
-\dfrac{3072(n^2+9n+10)}
       {n(2n+5)(2n+7)(2n+9)}
&
\dfrac{128(n^4+30n^3+192n^2+457n+330)}
       {n(2n+5)(2n+7)(2n+9)}
&
-\dfrac{16(n^3+31n^2+134n+120)}
       {n(2n+7)(2n+9)}
\end{pmatrix}.
 \tag{47}
$$



For an exact audit of (46), let



$$
L_{n,c}=\frac n{z-1}+\frac n{z-i}
         +\frac1{z+1}+\frac{c-1}{z}.
 \tag{48}
$$



The companion certificate displays explicit rational functions
$Q_{n,v}(z)$, with pole order $v+1$ at zero, and verifies after
clearing all denominators that



$$
H(z)w(z)^v-\sum_{j=0}^2(T_n)_{v,j}w(z)^j
 =Q_{n,v}'(z)+Q_{n,v}(z)L_{n,c}(z)
 \tag{49}
$$



for $v=0,1,2$, using $c=-n-1/2$ in the coefficient field.

In the induction leading to a target with $c\ge3$, every old value of
$c$ in (43) is at least $5$.  Therefore
$Q_{n,v}A_{n,c}$ is a polynomial, vanishes at
$-1,0,1,i$, and has degree at most $p-1$.  Formal integration of
the derivative in (49) has exactly zero boundary term.  This proves
(46) for the paths in (8) and (6), and the entries of $T_n$ lie in
$\mathbb F_p$, so it also proves (46) after taking real or imaginary
coordinates.

Direct calculation from (47) gives



$$
\det T_n=
 \frac{4096(n+1)^2(n+2)^3}
 {n(2n+5)(2n+7)^2(2n+9)}.
 \tag{50}
$$



Substituting $n=2j$ into (50) gives



$$
\det T_{2j}
 =
 \frac{2^{14}(j+1)^3(2j+1)^2}
 {j(4j+5)(4j+7)^2(4j+9)}.
 \tag{51}
$$



Starting from $n=2$, equations (42), (46), and (51) prove (40);
the phase changes by
$\chi(c+2)=-\chi(c)$, producing the factor $(-1)^{r+1}$.

Finally, every positive integer appearing in a numerator or denominator
of (40) is strictly less than $p$.  In particular, the largest
denominator factor is
$4(r-1)+9=2n+5<p$, because $c\ge3$ implies
$p\ge2n+7$.  Thus every factor in (40) is a unit modulo $p$, proving
(41). $\square$

## 6. Excluding the identically-zero matching branch

Suppose $v_p(q_n)=1$, and put



$$
\bar q_n=q_n/p\pmod p.
 \tag{52}
$$



Then $\bar q_n\ne0$.  Also $p_n\ne0\pmod p$, because the primitive
Bessel pair satisfies $\gcd(p_n,q_n)=1$.

By (7), (8), and Theorem 3.1, the target residual



$$
F_v=4\bar q_n\operatorname {Im}I_v-p_nD_v
 \tag{53}
$$



is a scalar solution of (20).  If it were identically zero, then
$D_v$ and $\operatorname {Im}I_v$ would be proportional nonzero
solutions.  This contradicts the nonzero three-column Casoratian (41).
Hence $F_v$ is not identically zero.

Combining this fact with the two unit pivots (23)--(24) gives the exact
adjacent-return theorem:



$$
\boxed{\text{\(F_v\) cannot vanish at three consecutive admissible
values of \(v\).}}
 \tag{54}
$$



Since $K_{v+1}=K_v+1$, (54) is equivalently a restriction on any
three consecutive $K$-forms within the same one-block band for the
fixed prime $p$.

The conclusion concerns the final generic congruence.  It does not say
that the prime is generic at all three forms: the exceptional branches
$D_v=0$ and $U_v=0$, prime powers, and crossings of the band boundary
must still be handled separately in any product-over-adjacent-forms
argument.

## 7. Exact obstructions to stronger conclusions

The target itself can have two separated zeros.  The certificate verifies



$$
(n,p)=(18,3167):\quad v=713,1306,
 \tag{55}
$$



and



$$
(n,p)=(82,953):\quad v=55,281.
 \tag{56}
$$



Thus (54) is not an at-most-one theorem.

Nor can recurrence order alone give an at-most-two theorem.  For
$n=2,p=17,c=6$, the exact scalar solution of (20) with initial values



$$
(X_0,X_1,X_2)=(1,9,0)
 \tag{57}
$$



is



$$
(X_0,\ldots,X_5)=(1,9,0,0,2,0)\pmod {17}.
 \tag{58}
$$



It has zeros at $v=2,3,5$ but no run of three.  Any stronger return
bound must use the special endpoint-period initial state of (53), not
only the abstract scalar operator.

## 8. Exact certificate and reproducibility

The companion script performs the following exact checks.

1. It verifies the simplified transition (17), the row identity (21),
   and the scalar recurrence in independent modular cases.
2. It verifies the endpoint identity (8) directly and checks the
   factorial normalization.
3. It checks the scalar Wronskian multiplier (26).
4. It verifies all three rational-function identities (49) symbolically,
   after clearing denominators, and verifies (50).
5. It computes the four $n=2$ phase cases in (42) using exact rational
   arithmetic.
6. It verifies the target examples (55)--(56) and the arbitrary-solution
   obstruction (58).

Run

    python -m py_compile scripts/critical_fourier_endpoint_period_scalar_recurrence_certificate.py
    python scripts/critical_fourier_endpoint_period_scalar_recurrence_certificate.py

For a byte-identical rerun, use

    python scripts/critical_fourier_endpoint_period_scalar_recurrence_certificate.py \
      --output /tmp/critical_fourier_endpoint_period_scalar_recurrence_certificate.json
    cmp results/critical_fourier_endpoint_period_scalar_recurrence_certificate.json \
      /tmp/critical_fourier_endpoint_period_scalar_recurrence_certificate.json

The no-three-consecutive theorem and the Casoratian formula are
all-parameter results in the one-block band.  They do not by themselves
bound all separated returns, control exceptional prime powers, close the
remaining critical-Fourier strip, or classify $e+\pi$.
