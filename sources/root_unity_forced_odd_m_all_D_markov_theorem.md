> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The forced odd-frequency next coefficient in every endpoint degree

## An external-node reproducing-kernel theorem and the corrected hard-parity closure

Checked: 2026-08-27 UTC

## 1. Verdict and scope

Let



$$
m=2k+1\ge3,
 \qquad n\ge4\text{ even},
 \qquad D=2d+1\ge3\text{ odd},
 \qquad D\le n.                                           \tag{1}
$$



Put $h=n+1$.  Since $n$ and $D$ have opposite parity, (1) gives



$$
h\ge 2d+3.                           \tag{2}
$$



This is the sole parity-forced family left open by the top-cardinal and
corrected even-frequency border theorems.  The preliminary forced-odd-
frequency audit reduced it to a normalized Euler-border comparison but did
not prove that comparison.

This note proves the missing statement.

> **All-degree forced-odd-frequency theorem.**  Under (1), the parity-forced
> top candidate satisfies
> 

$$
>                 [z^{n+D}]\Gamma=0,
>
$$


> but its next coefficient is nonzero:
> 

$$
>          \boxed{[z^{n+D-1}]\Gamma\ne0.}                 \tag{3}
>
$$


> Consequently, for the corrected exterior polynomial
> $\Delta=W-\Gamma$,
> 

$$
>          \boxed{\deg\Delta=n+D-1.}                     \tag{4}
>
$$



Indeed, $\deg W\le2D-2$, while parity in (1) gives
$n+D-1\ge2D$.  Thus the coefficient in (3) is strictly above the
degree of $W$.

The new ingredient is a positive external-node reproducing-kernel theorem.
It proves, separately for every divisor pole $a\ge0$ used by the
top Hermite cardinal, that



$$
\boxed{
 \operatorname {NB}_A\!\left(\mathcal E\!\left(\frac{V}{x+a}\right)\right)
 <
 \operatorname {NB}_G\!\left(\mathcal E\!\left(\frac{V}{x+a}\right)\right).} \tag{5}
$$



This includes the Laurent divisor $a=0$.  Positive linearity then proves
the comparison for the actual cardinal Stieltjes function $\rho$.

The proof is all-parameter.  Exact finite calculations in the companion
certificate are replays and sign audits, not extrapolations.  No conclusion
about the arithmetic nature of $e+\pi$ is claimed here.

The deterministic replay files are

* `scripts/root_unity_forced_odd_m_all_D_markov_certificate.py`;
* `results/root_unity_forced_odd_m_all_D_markov_certificate.json`.

## 2. The already-proved common-column reduction

Set



$$
\begin{aligned}
 x&=t^2,
 &z(x)&=\operatorname {csch}^2(\pi\sqrt x),\\
 g(x)&=\pi\sqrt x\coth(\pi\sqrt x),
 &V(x)&=\prod_{j=1}^k(x+j^2)^h,                           \tag{6}\\
 d\nu(x)&=\frac{x^{(h-1)/2}}{\sinh(\pi\sqrt x)}\,dx,
 &\mathcal E&=2x\frac d{dx}+h+1,\\
 T&=1+2z\frac d{dz}.
 \end{aligned}
$$



The endpoint rows are



$$
A_u=x^uV,\qquad G_u=\mathcal E A_u,
 \qquad 0\le u<d.                                        \tag{7}
$$



If $Q_v(1+z)$ is the even derivative-polynomial column of degree $v$,
the positive pairing is



$$
\langle f,Q_v\rangle
 =\int_0^\infty f(x)Q_v(1+z(x))\,d\nu(x).                \tag{8}
$$



For a row function $f$, define



$$
\begin{aligned}
 \operatorname {NB}_A(f)&=
 \frac{\det\!\begin{pmatrix}
 (\langle A_u,Q_v\rangle)_{0\le u<d,\ 0\le v\le d}\\
 (\langle f,Q_v\rangle)_{0\le v\le d}
 \end{pmatrix}}
 {\det\!\begin{pmatrix}
 (\langle A_u,Q_v\rangle)_{0\le u<d,\ 0\le v\le d}\\
 e_d^T
 \end{pmatrix}},\\[2mm]
 \operatorname {NB}_G(f)&=
 \frac{\det\!\begin{pmatrix}
 (\langle G_u,Q_v\rangle)_{0\le u<d,\ 0\le v\le d}\\
 (\langle f,Q_v\rangle)_{0\le v\le d}
 \end{pmatrix}}
 {\det\!\begin{pmatrix}
 (\langle G_u,Q_v\rangle)_{0\le u<d,\ 0\le v\le d}\\
 e_d^T
 \end{pmatrix}}.                                         \tag{9}
 \end{aligned}
$$



Both denominators are nonzero by endpoint normality.  The corrected phase
audit gives the exact normalized bracket



$$
\operatorname {NB}_A(V\psi)
 +\operatorname {NB}_G(\mathcal E(V\rho))
 -\operatorname {NB}_A(\mathcal E(V\rho)).               \tag{10}
$$



More precisely, if the expression in (10) is denoted by $\mathfrak B$,
then the already-audited common phase is



$$
[z^{n+D-1}]\Gamma=\alpha\mathfrak B,
 \qquad
 \alpha=(-1)^dC_*\pi^{2d}\ne0,
 \qquad
 C_*=\frac12(-1)^{k+kh+(h+1)/2}.                         \tag{10a}
$$



Thus positivity of (10), rather than merely its nonvanishing up to an
unspecified scalar, proves (3).

Here



$$
\rho(x)=\frac{w_0}{x}
          +2\sum_{j=1}^k\frac{w_j}{x+j^2},
 \qquad w_j>0,                                           \tag{11}
$$



and the independent pole-cancellation theorem proves



$$
\psi(x)=\sum_{j=1}^k\frac{c_j}{x+j^2},
 \qquad c_j>0.                                           \tag{12}
$$



The divided-difference/Andreief argument already proves



$$
\operatorname {NB}_A(V\psi)>0.       \tag{13}
$$



Thus (3) follows once



$$
\operatorname {NB}_A(\mathcal E(V\rho))
 <\operatorname {NB}_G(\mathcal E(V\rho))                \tag{14}
$$



is proved.  Sections 3--6 prove the stronger polewise assertion (5).

## 3. The biorthogonal Markov form

The formal adjoint identity is



$$
\boxed{
 \int_0^\infty (\mathcal Ef)(x)p(z(x))\,d\nu(x)
 =\int_0^\infty g(x)f(x)(Tp)(z(x))\,d\nu(x).}            \tag{15}
$$



It follows by one integration by parts.  At infinity the exponential in
$d\nu$ kills every row.  At zero the worst row needed for (5) is
$V/x$, and the boundary is
$O(x^{(h-2)/2-d})=o(1)$ by (2).  Hence (15) is valid for
all rows used below, including the central Laurent divisor.

Let $p$ and $p_g$ be the monic degree-$d$ polynomials in $z$
defined by



$$
\begin{aligned}
 \int_0^\infty x^uV(x)p(z(x))\,d\nu(x)&=0,\\
 \int_0^\infty x^uV(x)g(x)p_g(z(x))\,d\nu(x)&=0,
 \qquad 0\le u<d.                                       \tag{16}
 \end{aligned}
$$



The mixed moment determinants are nonzero: on ordered positive nodes the
$x$-Vandermonde is positive and the $z$-Vandermonde has the fixed sign



$$
\epsilon_r=(-1)^{r(r-1)/2},             \tag{17}
$$



because $z(x)$ is strictly decreasing.  Andreief's identity therefore
gives strict sign $\epsilon_r$ to every square initial mixed moment
determinant.

Put



$$
q=\frac{Tp}{2d+1},\qquad r=q-p_g.                        \tag{18}
$$



Both $q$ and $p_g$ are monic, so $\deg r\le d-1$.  If
$W_a=V/(x+a)$, where $a\ge0$, the endpoint-normalized null-polynomial
calculation gives



$$
\boxed{
 \operatorname {NB}_A(\mathcal EW_a)
 -\operatorname {NB}_G(\mathcal EW_a)
 =\ell_d(2d+1)
  \int_0^\infty\frac{g(x)V(x)}{x+a}r(z(x))\,d\nu(x),}    \tag{19}
$$



where $\ell_d>0$ is the leading coefficient of $Q_d(1+z)$.
Equation (19) is the exact Markov form of the required comparison.  It
remains to prove that its integral is negative.

## 4. Positivity of the divisor Markov transforms

Write



$$
d\mu_0(x)=V(x)\,d\nu(x),\qquad
 d\mu(x)=g(x)V(x)\,d\nu(x),                              \tag{20}
$$



and define, for $1\le j\le k$,



$$
J_j=\int_0^\infty
                 \frac{p(z(x))}{x+j^2}\,d\mu_0(x).       \tag{21}
$$



Then



$$
\boxed{J_j>0.}                   \tag{22}
$$



Here is a sign-complete proof.  The determinantal formula for the monic
polynomial $p$, followed by integration against $(x+j^2)^{-1}d\mu_0$,
expresses $J_j$ as a $(d+1)$-row mixed moment determinant divided by
the $d$-row determinant defining (16).  On ordered nodes
$0<x_1<\cdots<x_{d+1}$, the last row on the left has divided difference



$$
\left(\frac1{x+j^2}\right)[x_1,\ldots,x_{d+1}]
 =\frac{(-1)^d}{\prod_{i=1}^{d+1}(x_i+j^2)}.              \tag{23}
$$



Thus the numerator sign is $(-1)^d\epsilon_{d+1}$, while the
denominator sign is $\epsilon_d$.  Since



$$
\epsilon_{d+1}/\epsilon_d=(-1)^d,       \tag{24}
$$



their quotient is strictly positive.  This proves (22), with no finite-
parameter assumption.

## 5. A positive external-node reproducing kernel

We isolate the general lemma responsible for the remaining sign.

> **External-node Stieltjes-kernel lemma.**  Let $\mu$ be a positive
> measure on $(0,\infty)$ whose support contains at least $d$ distinct
> points, let $z(x)$ be strictly decreasing on that support, and suppose
> the mixed moments below and the Stieltjes moments in (28) exist.  For
> $d\ge1$, put
> 

$$
> M_{uv}=\int_0^\infty x^uz(x)^v\,d\mu(x),
> \qquad 0\le u,v<d.                                     \tag{25}
>
$$


> For $\xi<0$, let
> 

$$
> v_\xi=(1,\xi,\ldots,\xi^{d-1})^T,
> \qquad
> R_\xi(z)= (1,z,\ldots,z^{d-1})M^{-1}v_\xi.             \tag{26}
>
$$


> Then $R_\xi$ reproduces evaluation at $\xi$:
> 

$$
> \int_0^\infty P(x)R_\xi(z(x))\,d\mu(x)=P(\xi)
> \quad(\deg P<d).                                       \tag{27}
>
$$


> Moreover, for every $a\ge0$,
> 

$$
> \boxed{
> K_d(a,\xi):=\int_0^\infty
> \frac{R_\xi(z(x))}{x+a}\,d\mu(x)>0.}                 \tag{28}
>
$$



The mixed moment matrix $M$ is nonsingular by the same Andreief sign
argument as in (17).  Formula (27) follows immediately from (25)--(26).

For the strict sign in (28), write $\xi=-b$, $b>0$, and put



$$
\ell_a=\left(\int_0^\infty\frac{z(x)^v}{x+a}\,d\mu(x)
         \right)_{0\le v<d}.
$$



The Schur determinant is



$$
\mathcal B=\det\!\begin{pmatrix}M&v_\xi\\\ell_a&0\end{pmatrix}
            =-\det(M)K_d(a,\xi).                         \tag{29}
$$



Generalized Andreief gives



$$
\mathcal B=\frac1{d!}\int
 \det\bigl(F(x_1),\ldots,F(x_d),G_\xi\bigr)
 \det\bigl(z(x_j)^v\bigr)_{
      \substack{0\le v<d\\1\le j\le d}}
 \prod_{j=1}^d d\mu(x_j),                               \tag{30}
$$



where



$$
\begin{aligned}
 F(x)&=(1,x,\ldots,x^{d-1},(x+a)^{-1})^T,\\
 G_\xi&=(1,\xi,\ldots,\xi^{d-1},0)^T.                  \tag{31}
 \end{aligned}
$$



For ordered positive nodes, let $p_a$ be the polynomial of degree below
$d$ which interpolates $(x+a)^{-1}$ at those nodes.  A Schur
complement of the ordinary Vandermonde gives



$$
\det\bigl(F(x_1),\ldots,F(x_d),G_\xi\bigr)
       =-\prod_{i<j}(x_j-x_i)\,p_a(\xi).                  \tag{32}
$$



The interpolation value at $\xi=-b$ is explicit:



$$
p_a(-b)=
 \frac{1-\displaystyle\prod_{i=1}^d
                  \frac{b+x_i}{a+x_i}}
      {a-b}.                                              \tag{33}
$$



If $a>b$, both numerator and denominator in (33) are positive.  If
$a<b$, both are negative.  At $a=b$, the continuous value is



$$
p_a(-a)=\sum_{i=1}^d\frac1{a+x_i}>0. \tag{34}
$$



Equations (33)--(34) also include $a=0$ because $b>0$.  Hence
$p_a(\xi)>0$ in every case.  The first determinant in (30) is therefore
strictly negative times the positive $x$-Vandermonde, while the second
has sign $\epsilon_d$.  Thus



$$
\operatorname {sgn}\mathcal B=-\epsilon_d,
        \qquad \operatorname {sgn}\det M=\epsilon_d.     \tag{35}
$$



Equation (29) now proves (28).  Notice that the proof controls the
integrated Markov transform; it does not assert that $R_\xi$ has one
pointwise sign.

## 6. The exact negative-node representation

Let



$$
d\eta(x)=r(z(x))\,d\mu(x).        \tag{36}
$$



For every polynomial $P$ of degree below $d$, orthogonality of
$p_g$, (15), and (18) give



$$
\begin{aligned}
 \int P\,d\eta
 &=\int PgV(q-p_g)\,d\nu\\
 &=\frac1{2d+1}\int \mathcal E(PV)p\,d\nu.              \tag{37}
 \end{aligned}
$$



Expanding the Euler operator,



$$
\mathcal E(PV)
 =V\{2xP'+(h+1)P\}+2xPV'.                                \tag{38}
$$



The first term on the right is $V$ times a polynomial of degree below
$d$, so it vanishes against $p$.  Since



$$
\frac{V'}V
 =h\sum_{j=1}^k\frac1{x+j^2},                             \tag{39}
$$



polynomial division gives



$$
\frac{xP(x)}{x+j^2}
 =Q_j(x)-\frac{j^2P(-j^2)}{x+j^2},
 \qquad \deg Q_j<d.                                      \tag{40}
$$



The $Q_j$-term again vanishes against $p$.  Combining
(21), (37)--(40) proves the exact moment identity



$$
\boxed{
 \int_0^\infty P(x)\,d\eta(x)
 =-\frac{2h}{2d+1}
   \sum_{j=1}^k j^2J_jP(-j^2)
 \quad(\deg P<d).}                                       \tag{41}
$$



Use the reproducing polynomials (26) for the particular measure $\mu$
in (20).  All moments required by the lemma converge.  At zero, the worst
case is $a=0$ and a degree-$(d-1)$ polynomial in $z$; its integrand
is
$O(x^{(h-2)/2-d})$, which is integrable by (2).  At infinity the
exponential factor in $d\nu$ dominates.  Both sides of



$$
r(z)=-\frac{2h}{2d+1}
       \sum_{j=1}^k j^2J_jR_{-j^2}(z)                    \tag{42}
$$



have degree at most $d-1$, and (27) and (41) show that their first
$d$ mixed moments are identical.  Nonsingularity of $M$ makes (42) a
polynomial identity, not merely a moment equivalence.

Apply the Stieltjes-kernel lemma to (42).  For every $a\ge0$,



$$
\begin{aligned}
 \int_0^\infty\frac{r(z(x))}{x+a}\,d\mu(x)
 &=-\frac{2h}{2d+1}\sum_{j=1}^k
       j^2J_jK_d(a,-j^2)\\
 &<0,                                                     \tag{43}
 \end{aligned}
$$



because every factor $J_j$ and $K_d(a,-j^2)$ is strictly positive.
Substitution in (19) proves (5).

Finally, (11) is a positive linear combination of the divisors
$V/x$ and $V/(x+j^2)$.  The two normalized-border maps have fixed
denominators and are linear in their border row.  Summing (5) with the
positive cardinal weights proves the strict inequality (14).  Together
with (13), the normalized bracket (10) is strictly positive.  The exact
phase reduction therefore proves (3), and the degree comparison following
(4) completes the theorem.

## 7. Logical consequences and limits

Combining this theorem with the top-cardinal theorem and the corrected
even-frequency theorem proves corrected exterior nonvanishing throughout
their common regime $m\ge2$, $n\ge D\ge2$.  This note supplies the
previously missing family $m$ odd, $n$ even, $D$ odd.

What it does **not** prove is equally important.

1. It gives nonvanishing and the actual degree in the forced family, but no
   new primitive-content or saturated-height estimate for $\Delta$.
2. It does not by itself improve the endpoint value/height exponent needed
   for an arithmetic contradiction under the hypothesis that $e+\pi$ is
   algebraic.
3. The reproducing polynomial $R_\xi$, and likewise $q-p_g$, need not
   have one coefficientwise or pointwise sign.  Positivity occurs only
   after the Stieltjes transform in (28).
4. The theorem uses the divisor structure (39).  It does not extend to an
   arbitrary positive-coefficient border polynomial.

## 8. Deterministic replay

The companion certificate uses exact rational arithmetic.  It checks:

1. the Schur determinant (29), generalized-Andreief cofactor identity, and
   interpolation formulas (32)--(34) on deterministic rational node grids;
2. the strict signs in the abstract external-node kernel lemma for exact
   discrete positive measures with decreasing rational $z$;
3. the divided-difference determinant and positivity of $J_j$ for exact
   discrete mixed moment systems; and
4. the original root-of-unity normalized-border inequality, separately for
   every central and noncentral divisor, on a finite exact Bernoulli-moment
   grid.

The first three checks replay the algebra behind the proof.  The fourth is
an independent finite audit of normalization and signs.  The universal
quantifiers in the theorem come from Sections 3--6, not from that grid.
