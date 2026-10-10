> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fixed-target positive common-kernel forms have a uniform primitive gap

Checked: 2026-08-27 UTC.

## 1. Verdict

For an integer polynomial $F$, define



$$
A(F)=\sum_{k\ge0}(-1)^kF^{(k)}(1),
 \qquad
 B(F)=\sum_{k\ge0}(-1)^kF^{(k)}(0).
\tag{1}
$$



Fix an integer $a\ne0$.  Suppose



$$
F\in\mathbb Z[x],\qquad
 F\ge0\text{ on }[0,1],\qquad F\not\equiv0,
\tag{2}
$$



and



$$
A(F)=F(i)=F(-i)=a.
\tag{3}
$$



Then the positive common-kernel integral



$$
L(F)=\int_0^1F(x)
 \left(e^x+\frac4{1+x^2}\right)dx
\tag{4}
$$



cannot tend to zero while $a$ is fixed.  More strongly, neither can its
fully cleared and primitive integer linear form.

Let



$$
\delta_a=ae-\lfloor ae\rfloor.
\tag{5}
$$



Since $e$ is irrational, $0<\delta_a<1$.  The exact uniform bounds are



$$
\boxed{L(F)\ge\delta_a}
\tag{6}
$$



and



$$
\boxed{L(F)_{\rm primitive}\ge\frac{\delta_a}{|a|}.}
\tag{7}
$$



For the especially favorable target $a=2$, one has $5<2e<6$, so



$$
\boxed{
 L(F)_{\rm primitive}\ge e-\frac52>\frac5{24}.}
\tag{8}
$$



This is a complete obstruction for every fixed nonzero integer target.  It
does not assume a square ansatz, endpoint multiplicities, a
Markov--Lukacs representation, or any particular Stein--Robin coordinates.
It includes every endpoint-localizing construction with



$$
F\equiv a\pmod{1+x^2}.
\tag{9}
$$



The denominator comparison is exact.  If the rational coordinate of (4) is
$N/D$ in lowest terms, then the content removed from the cleared pair
$(aD,N)$ divides $a$.  Hence a growing least-common-multiple denominator
can only amplify the fixed exponential gap, apart from a bounded factor
dividing $a$.

There is nevertheless an infinite, elementary fixed-target positive family.
For $n\equiv3\pmod4$, put



$$
H_n=x^n+n x^{n-1},
 \qquad
 F_n=H_n+H_{n+2}.
\tag{10}
$$



Then



$$
F_n=x^{n-1}\{n+x+(n+2)x^2+x^3\}\ge0,
\tag{11}
$$



and



$$
A(F_n)=F_n(i)=F_n(-i)=2.
\tag{12}
$$



This shows that positivity and a fixed target are feasible in arbitrarily
high degree.  The family does not shrink: its exponential component is
exactly $2e$.  Thus the obstruction is quantitative, not a claim that the
fixed-target positive cone is empty.

Nothing here treats targets $a_n$ which grow with the degree.  That remains
the only possible positive common-kernel regime after this theorem.

## 2. The exponential component is already discrete

Repeated integration by parts gives the exact identity



$$
\int_0^1F(x)e^x\,dx=eA(F)-B(F).
\tag{13}
$$



Under (3), this becomes



$$
E(F):=\int_0^1F(x)e^x\,dx=ae-B(F).
\tag{14}
$$



Every endpoint derivative of an integer polynomial is an integer, so



$$
B(F)\in\mathbb Z.
\tag{15}
$$



The hypotheses in (2) imply $E(F)>0$.  Therefore



$$
B(F)<ae.
\tag{16}
$$



Among all integers strictly below the noninteger real number $ae$, the
largest is $\lfloor ae\rfloor$.  Equations (14)--(16) prove



$$
E(F)\ge ae-\lfloor ae\rfloor=\delta_a.
\tag{17}
$$



The rational-kernel component



$$
P(F)=4\int_0^1\frac{F(x)}{1+x^2}\,dx
\tag{18}
$$



is also strictly positive.  Hence



$$
L(F)=E(F)+P(F)>E(F)\ge\delta_a,
\tag{19}
$$



which proves (6).  Notice that no estimate for the size, degree, or
coefficients of $F$ enters this argument.

For completeness, if $a=0$, then (14) is a positive integer.  Thus
$E(F)\ge1$, and after primitive reduction the resulting constant integer
form is $1$.  The zero target is therefore no exception.

## 3. Exact rational coordinate and primitive content

The endpoint equations in (3) imply



$$
1+x^2\mid F-a.
\tag{20}
$$



Because the divisor is monic,



$$
G_F(x)=\frac{F(x)-a}{1+x^2}\in\mathbb Z[x].
\tag{21}
$$



It follows that



$$
\begin{aligned}
 P(F)
 &=a\pi+4\int_0^1G_F(x)\,dx,\\
 L(F)
 &=a(e+\pi)+c_F,
 \end{aligned}
\tag{22}
$$



where



$$
c_F=-B(F)+4\int_0^1G_F(x)\,dx\in\mathbb Q.
\tag{23}
$$



Write this rational number in lowest terms as



$$
c_F=\frac ND,qquad D>0,qquad\gcd(N,D)=1.
\tag{24}
$$



Clearing denominators gives



$$
D L(F)=aD(e+\pi)+N.
\tag{25}
$$



Let



$$
g=\gcd(aD,N).
\tag{26}
$$



Since $N$ is coprime to $D$, every prime power in (26) must come from
$a$.  More precisely,



$$
\boxed{g=\gcd(a,N),\qquad g\mid a.}
\tag{27}
$$



The fully primitive form and its positive value are therefore



$$
\Lambda_F
 =\frac{aD}{g}(e+\pi)+\frac Ng
 =\frac DgL(F)>0.
\tag{28}
$$



Equations (19), (27), and $D\ge1$ give



$$
\Lambda_F\ge\frac Dg\delta_a
             \ge\frac{\delta_a}{|a|},
\tag{29}
$$



proving (7).

If $d=\deg F$, then $\deg G_F\le d-2$.  Direct integration of its
integer monomials also gives the universal denominator relation



$$
D\mid\operatorname {lcm}(1,2,\ldots,d-1).
\tag{30}
$$



Unlike a universal-denominator estimate alone, (27) is primitive-invariant:
the final content is bounded by the fixed target itself.  No exceptional
gcd can cancel an unbounded part of (30).

## 4. The explicit target-two gap

The elementary exponential series gives



$$
e>1+1+\frac12+\frac16+\frac1{24}=\frac{65}{24}
\tag{31}
$$



and $e<3$.  Consequently



$$
5<2e<6,
 \qquad
 \delta_2=2e-5.
\tag{32}
$$



Substitution in (29) gives



$$
\Lambda_F\ge\frac{2e-5}{2}=e-\frac52
 >\frac{65}{24}-\frac{60}{24}
 =\frac5{24}.
\tag{33}
$$



This bound includes the possibility that the cleared pair has content two.
It therefore applies after all rational integration denominators and all
final common content have been removed.

## 5. An infinite fixed-target positive family

Let $!n$ be the derangement number and put



$$
u_n=A(x^n)=(-1)^n!n.
\tag{34}
$$



The derangement recurrence is equivalent to



$$
u_n+n u_{n-1}=1.
\tag{35}
$$



Thus the polynomial in (10) satisfies



$$
A(H_n)=A(x^n+n x^{n-1})=1.
\tag{36}
$$



Its other endpoint functional cancels exactly:



$$
\begin{aligned}
 B(H_n)
 &=(-1)^n n!+n(-1)^{n-1}(n-1)!\\
 &=0.
 \end{aligned}
\tag{37}
$$



If $n\equiv3\pmod4$, then



$$
\begin{aligned}
 H_n(i)&=-(n+i),\\
 H_{n+2}(i)&=n+2+i.
 \end{aligned}
\tag{38}
$$



Their sum is two, and conjugation gives the same value at $-i$.  Equations
(35)--(38) prove (12).  Formula (11) proves nonnegativity directly.

Moreover,



$$
\int_0^1F_n(x)e^x\,dx
 =2e-B(F_n)=2e.
\tag{39}
$$



So even though $x^{n-1}$ localizes the support toward $x=1$, the factor
of size $n$ forced by the exact recurrence preserves a nonzero amount of
mass.  The rational-kernel component is positive as well, hence



$$
L(F_n)>2e.
\tag{40}
$$



The exact certificate checks this family through $n=203$.  It divides
$F_n-2$ by $1+x^2$, computes the minimal rational denominator in (24),
checks (30), and removes the final content.  The exact denominators already
have 88 decimal digits at $n=203$, while every recorded content is one.
These growing denominators magnify the nonzero gap; they do not create
decay.

## 6. Consequences for proposed localization mechanisms

The theorem applies unchanged to each of the following approaches:

1. integer polynomials congruent to $a$ modulo $1+x^2$, including
   arbitrarily high-degree endpoint-localizing products;
2. the Stein--Robin parametrization $F=a+\mathcal TP$;
3. Markov--Lukacs representations of every polynomial nonnegative on
   $[0,1]$;
4. Bernstein- or beta-basis positive combinations;
5. exact least-common-multiple clearing followed by arbitrary primitive
   reduction.

The reason is structural: all of these retain the positive exponential
component (14), whose rational endpoint coordinate is an integer.  The
fractional part in (17) is fixed before the $\pi$-coordinate or its
denominator is considered.

Therefore no fixed nonzero target, including $a=2$, can produce a positive
primitive linear form tending to zero.  A viable positive family must let
$|a_n|\to\infty$ and then control the cross-content between the two output
coordinates.  This matches the exact survivor left by the earlier positive
cone and Stein--Robin audits.

## 7. Certificate and scope

The deterministic exact-arithmetic certificate is

    scripts/fixed_target_positive_common_kernel_gap_certificate.py

and its frozen output is

    results/fixed_target_positive_common_kernel_gap_certificate.json

It verifies the recurrence (35), the target-two family (10)--(12), positivity
from the coefficient factorization, the endpoint value $B(F_n)=0$, exact
division by $1+x^2$, the minimal rational coordinate, the denominator
divisibility (30), and the final-content divisibility (27) through
$n=203$.  It also records a rigorous rational enclosure of $e$ and
checks the numerical-free lower bound in (33).

The all-degree fixed-target theorem is the proof in Sections 2--4; finite
computation is not used as a substitute.  The theorem does not address
growing targets and therefore does not decide whether $e+\pi$ is
irrational, algebraic, or transcendental.
