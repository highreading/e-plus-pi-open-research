> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Growing positive targets: exact two-place synchronization and cross-content saturation

Checked: 2026-08-27 UTC.

## 1. Verdict

Let



$$
s=e+\pi
$$



and suppose



$$
F\in\mathbb Z[x],\qquad F\ge0\text{ on }[0,1],qquad F\not\equiv0,
\tag{1}
$$



with



$$
A(F)=F(i)=F(-i)=a\in\mathbb Z\setminus\{0\}.
\tag{2}
$$



The fixed-target theorem forces $|a|\to\infty$ in any potentially
shrinking family.  In this growing-target regime there is an exact
two-place description of the remaining arithmetic.

Put



$$
B=B(F)=\sum_{k\ge0}(-1)^kF^{(k)}(0)
\tag{3}
$$



and



$$
G=\frac{F-a}{1+x^2}\in\mathbb Z[x].
\tag{4}
$$



Write the rational $\pi$-correction in lowest terms as



$$
4\int_0^1G(x)\,dx=\frac MD,
 \qquad D>0,qquad\gcd(M,D)=1.
\tag{5}
$$



Then



$$
L(F):=\int_0^1F(x)
 \left(e^x+\frac4{1+x^2}\right)dx
 =a(e+\pi)+\frac{M-BD}{D}.
\tag{6}
$$



Define the exact cross-content



$$
g=\gcd(aD,M-BD).
\tag{7}
$$



Because $M-BD$ is coprime to $D$,



$$
\boxed{g=\gcd(a,M-BD),\qquad g\mid a.}
\tag{8}
$$



The fully primitive positive form is



$$
\Lambda_F
 =\frac{aD}{g}(e+\pi)+\frac{M-BD}{g}
 =\frac DgL(F)>0.
\tag{9}
$$



Its decisive feature is the positive decomposition



$$
\boxed{
 \Lambda_F
 =\frac Dg(ae-B)+\frac1g(aD\pi+M),}
\tag{10}
$$



in which both summands are strictly positive.  Therefore no cancellation
between the $e$- and $\pi$-components can make the form small.

For a noninteger real number $y$, write



$$
\{y\}=y-\lfloor y\rfloor\in(0,1).
\tag{11}
$$



Equation (10) gives the universal two-place lower bound



$$
\boxed{
 \Lambda_F\ge
 \frac{D\{ae\}+\{aD\pi\}}{g}
 \ge
 \frac{D\{ae\}+\{aD\pi\}}{|a|}.}
\tag{12}
$$



For $a>0$, put



$$
\alpha=\frac{aD}{g},qquad
 k=\frac{M-BD}{g}.
\tag{13}
$$



Then $(\alpha,k)$ is primitive and



$$
\Lambda_F=\alpha s+k.
\tag{14}
$$



More precisely, the primitive rational approximation to $s$ splits into
two simultaneous **one-sided** approximations:



$$
\boxed{
 \begin{aligned}
 \varepsilon_e&=e-\frac Ba>0,\\
 \varepsilon_\pi&=\pi+\frac{M}{aD}>0,\\
 \varepsilon_e+\varepsilon_\pi&=\frac{\Lambda_F}{\alpha}.
 \end{aligned}}
\tag{15}
$$



The cross-content is exactly the congruence which synchronizes them:



$$
\boxed{M\equiv BD\pmod g.}
\tag{16}
$$



Thus an exceptional small form requires good lower approximations to $e$
and $\pi$, at the same time, with the congruence (16), and realized by one
nonnegative common-kernel polynomial.

The continued fraction of $e$ supplies an effective universal barrier. For
all integers $p$ and all $q\ge1$,



$$
\boxed{
 |qe-p|>
 \frac1{q\{4\log_2q+8\}}.}
\tag{17}
$$



Consequently



$$
\boxed{
 \Lambda_F>
 \frac{D}{|a|^2\{4\log_2|a|+8\}}.}
\tag{18}
$$



Any shrinking positive primitive family must therefore satisfy



$$
|a_n|\longrightarrow\infty,
 \qquad
 D_n=o\bigl(|a_n|^2\log |a_n|\bigr).
\tag{19}
$$



For a Roth-breaking target, the restriction is stronger.  If, for some
fixed $\eta>0$,



$$
0<\Lambda_F\le\alpha^{-1-\eta},
\tag{20}
$$



then



$$
\boxed{
 \alpha^{2+\eta}
 <a^2\{4\log_2a+8\},}
\tag{21}
$$



and hence



$$
\boxed{
 g>
 \frac{D\,a^{\eta/(2+\eta)}}
      {\{4\log_2a+8\}^{1/(2+\eta)}}.}
\tag{22}
$$



This proves that any positive Roth-breaking construction must have genuinely
exceptional cross-content.

However, no general sublinear upper bound for $g$ is possible, even after
requiring the polynomial itself to be primitive and positive.  An explicit
family below has



$$
g=8m,\qquad a=272m,qquad\operatorname {cont}(F_m)=1.
\tag{23}
$$



Its primitive output pair is the constant pair $(34,-193)$.  Thus linear
cross-content growth is structurally real, but this example does not shrink.

The exact survivor is now narrower but still open: arrange the synchronized
approximations (15)--(16) so that the primitive pair varies and its positive
value tends to zero.  This note neither constructs such a family nor rules it
out.

## 2. Exact decomposition and primitive arithmetic

Repeated integration by parts gives



$$
\int_0^1F(x)e^x\,dx=ae-B.
\tag{24}
$$



The endpoint equality in (2) gives the monic divisibility (4), and hence



$$
4\int_0^1\frac{F(x)}{1+x^2}\,dx
 =a\pi+\frac MD.
\tag{25}
$$



Both integrals in (24)--(25) are strictly positive by (1).  Adding them
proves (6).

Since $M$ is coprime to $D$, so is $M-BD$.  Thus



$$
\gcd(aD,M-BD)=\gcd(a,M-BD),
\tag{26}
$$



which proves (8).  Clearing the denominator and dividing by this exact
content proves (9).  Multiplying (24) by $D/g$ and (25) by the same factor
gives (10).

If $x\notin\mathbb Z$ and $x+n>0$ for an integer $n$, then



$$
x+n\ge x-\lfloor x\rfloor=\{x\}.
\tag{27}
$$



Apply this first to $x=ae,n=-B$, and then to
$x=aD\pi,n=M$.  Equation (12) follows from (10), (27), and $g\le|a|$.

Assume now that $a>0$.  Division of the two positive summands in (10) by
$\alpha=aD/g$ gives the first two lines of (15).  Their sum is



$$
e+\pi+\frac{M-BD}{aD}
 =s+\frac{k}{\alpha}
 =\frac{\Lambda_F}{\alpha},
\tag{28}
$$



proving the last line.  Equation (16) is simply the definition of $k$.

The denominator itself remains bounded by the degree.  If $d=\deg F$,
then $\deg G\le d-2$, so



$$
D\mid\operatorname {lcm}(1,2,\ldots,d-1).
\tag{29}
$$



The issue is not hidden denominator clearing: it is whether the numerator
in (6) shares the exceptional divisor (7) with the growing target.

## 3. An explicit lower bound from the continued fraction of $e$

Euler's continued fraction is



$$
e=[2;1,2,1,1,4,1,1,6,1,\ldots].
\tag{30}
$$



Writing its partial quotients as $a_j$, one has, for $r\ge1$,



$$
a_{3r-2}=1,qquad a_{3r-1}=2r,qquad a_{3r}=1.
\tag{31}
$$



Let $p_n/q_n$ be a convergent.  Since every partial quotient is at least
one,



$$
q_n\ge F_{n+1}\ge2^{(n-1)/2},
\tag{32}
$$



where $F_j$ is the Fibonacci sequence.  Therefore



$$
n\le2\log_2q_n+1.
\tag{33}
$$



The complete-quotient formula for a convergent gives



$$
\left|e-\frac{p_n}{q_n}\right|
 >\frac1{(a_{n+1}+2)q_n^2}.
\tag{34}
$$



Equations (31)--(33) imply



$$
a_{n+1}+2\le4\log_2q_n+8.
\tag{35}
$$



If a reduced rational $p/q$ is not a convergent, Legendre's criterion
gives



$$
\left|e-\frac pq\right|\ge\frac1{2q^2},
\tag{36}
$$



which is stronger than (17).  Equations (34)--(36) prove (17) for reduced
rationals.  If $p/q$ is not reduced, divide by its content; multiplication
back by that content only strengthens the asserted bound for $|qe-p|$.

Apply (17) with $q=|a|$ and the integer corresponding to $B$.  The first
positive summand in (10) gives



$$
\Lambda_F
 >\frac{D}{g|a|\{4\log_2|a|+8\}}
 \ge\frac{D}{|a|^2\{4\log_2|a|+8\}},
\tag{37}
$$



which proves (18)--(19).

For (20), equation (15) and (17) give



$$
\Lambda_F
 =\alpha(\varepsilon_e+\varepsilon_\pi)
 >\frac{\alpha}{a^2\{4\log_2a+8\}}.
\tag{38}
$$



Combining (38) with (20) proves (21).  Since $g=aD/\alpha$, equation
(22) follows immediately.

These estimates use only the $e$-component.  The exact positive
$\pi$-term in (12) can strengthen a particular family, but no sufficiently
uniform theorem on the synchronized fractional parts is presently proved.

## 4. Linear cross-content is possible for primitive positive polynomials

The earlier positive endpoint-zero witness is



$$
F_0=4x(1-x)^2(31-3x^2).
\tag{39}
$$



Direct calculation gives



$$
A(F_0)=F_0(i)=F_0(-i)=272,
\tag{40}
$$



and



$$
B(F_0)=724,qquad
 c_{F_0}=-1544.
\tag{41}
$$



Thus its raw output pair is $(272,-1544)=8(34,-193)$.

Now put



$$
T=-2090+4553x+744x^2
\tag{42}
$$



and



$$
R=x(1-x)^2(1+x^2)T.
\tag{43}
$$



This is an exact zero-output direction:



$$
A(R)=R(i)=R(-i)=0,
\tag{44}
$$



while



$$
B(R)=-40,qquad
 4\int_0^1\frac{R(x)}{1+x^2}\,dx=-40.
\tag{45}
$$



Hence its total rational coordinate is



$$
-B(R)+4\int_0^1\frac{R(x)}{1+x^2}\,dx=0.
\tag{46}
$$



For every integer $m\ge17$, define



$$
F_m=mF_0+R.
\tag{47}
$$



Factoring gives



$$
F_m=x(1-x)^2S_m(x),
\tag{48}
$$



where



$$
S_m=4m(31-3x^2)+(1+x^2)T.
\tag{49}
$$



At $m=17$,



$$
S_{17}=744x^4+4553x^3-1550x^2+4553x+18.
\tag{50}
$$



Its derivative is



$$
S_{17}'=2976x^3+13659x^2-3100x+4553>0
 \qquad(0\le x\le1),
\tag{51}
$$



because $4553-3100x\ge1453$ and the other displayed terms are
nonnegative.  Therefore $S_{17}\ge18$.  For $m>17$, equation (49) adds



$$
4(m-17)(31-3x^2)>0
\tag{52}
$$



on $[0,1]$.  Thus every $F_m$ is strictly positive on $(0,1)$.

The two highest coefficients of $F_m$, inherited from $R$, are



$$
[x^7]F_m=744,qquad[x^6]F_m=3065,
\tag{53}
$$



and $\gcd(744,3065)=1$.  Hence every $F_m$ is primitive as an integer
polynomial.

Equations (40)--(47) give



$$
a_m=272m,qquad c_{F_m}=-1544m,qquad D_m=1.
\tag{54}
$$



Therefore



$$
g_m=\gcd(272m,1544m)=8m
\tag{55}
$$



and



$$
\Lambda_{F_m}=34(e+\pi)-193.
\tag{56}
$$



This family proves that a primitive polynomial can lie arbitrarily deep in
one fixed output ray.  Polynomial primitivity alone gives no upper bound on
cross-content.  But (56) is constant and positive, so the construction is a
barrier example, not a shrinking or Roth-breaking sequence.

## 5. What remains for a constructive family

For a positive growing-target family to prove irrationality, it is necessary
to make



$$
\alpha_n\to\infty,qquad
 0<\Lambda_n=\alpha_n(e+\pi)+k_n\to0.
\tag{57}
$$



Equations (15)--(16) show that this requires all of the following:

1. a lower approximation $B_n/a_n<e$;
2. a lower approximation $-M_n/(a_nD_n)<\pi$;
3. the errors must sum to $\Lambda_n/\alpha_n$;
4. $M_n\equiv B_nD_n\pmod {g_n}$;
5. one integer polynomial must realize both endpoint coordinates and remain
   nonnegative on $[0,1]$;
6. its exact denominator must satisfy (29), while a shrinking family must
   also satisfy (19).

The zero-output direction in Section 4 shows that large congruence content
can be inserted without polynomial content.  It does not make the primitive
ray move.  A successful construction must combine such content amplification
with a sequence of genuinely changing primitive rays which approximate
$-s$.

No determinant, Markov--Lukacs representation, or generic lattice-volume
argument presently enforces this synchronization.  Conversely, the linear
cross-content example prevents a blanket proof based only on
$g=o(a)$.

## 6. Certificate and scope

The deterministic exact-arithmetic certificate is

    scripts/growing_target_positive_synchronization_certificate.py

and its frozen output is

    results/growing_target_positive_synchronization_certificate.json

It verifies the endpoint and output identities for $F_0$ and $R$, the
zero-output relation (44)--(46), positivity and polynomial primitivity of
the family (47), and the exact cross-content and primitive pair through
$m=1000$.  It checks Euler's partial-quotient pattern and convergent
denominator growth through sixty convergents, and independently verifies a
slightly weaker form of (17) with rigorous rational enclosures for every
denominator through 500.  The all-degree continued-fraction bound is the
proof in Section 3, not a finite-computation inference.

This package provides an exact structural barrier and an exact
cross-content-saturation construction.  It does not provide a shrinking
positive family, and it does not determine whether $e+\pi$ is irrational,
algebraic, or transcendental.
