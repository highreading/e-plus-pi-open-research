> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the factorial-digit fixed-$b$ theorem

## 1. Scope and verdict

I independently audited the all-degree theorem and the finite artifacts in

- sources/factorial_digit_entire_fixed_b_rays.md;
- scripts/factorial_digit_entire_nondiagonal_probe.py;
- results/factorial_digit_entire_nondiagonal_a500_b30.json.

The source initially had two missing backslashes before the TeX spacing
command in equation (66). The author corrected that rendering-only defect
before this audit was frozen. I find no remaining mathematical or
computational defect. My verdict is



$$
\boxed{\text{ACCEPT}.}
$$



In particular, I independently obtain, for every



$$
a\geq\max(1,b-1),\qquad b\geq0,
$$



the fully primitive endpoint form



$$
\boxed{
L_{a,b}
=\frac{\Delta^b(a!)(e+\pi)-\Delta^b C_a}
       {\gcd(\Delta^b(a!),\Delta^b C_a)}
=\frac{\Delta^b x_a}{H_{a,b}}.
}
\tag{A1}
$$



I also confirm the rational-case equivalences, the direction and exponents
in the Roth-strength criterion, all 15,094 finite endpoint records, all 31
fixed-$b$ minimizers, and the unique global minimum at $(346,3)$.

## 2. Frozen snapshot

The audited hashes are



$$
\begin{array}{l|l}
\text{artifact}&\text{SHA-256}\\ \hline
\text{source note}&
66e5e2f46ad10db1bd60ce5a93e7a85a9cb3e02d933b3da78bf09a2815b30f7d\\
\text{source script}&
997127083235cafcef7d815feef587db3d4c6c02d56e4d62d749614a3b145c93\\
\text{source result}&
84cb3eaafeba0887c8291883a0acb0e727217d0c3df509bab9ef9fe808522741.
\end{array}
\tag{A2}
$$



The independent script asserts all three hashes before calculating. A clean
rerun of the source script was byte-identical to the frozen source JSON.

## 3. Canonical digits, the combined numerator, and the bounded remainder

For any real $y$, put



$$
d_n(y)=\lfloor n!y\rfloor-n\lfloor(n-1)!y\rfloor.
$$



Writing $u=(n-1)!y$ gives



$$
d_n(y)=\lfloor n\{u\}\rfloor,
$$



so $0\leq d_n(y)\leq n-1$. Moreover,



$$
\lfloor y\rfloor+\sum_{n=2}^{N}\frac{d_n(y)}{n!}
=\frac{\lfloor N!y\rfloor}{N!}\longrightarrow y.
\tag{A3}
$$



Thus the function



$$
G(z)=3+\sum_{n=2}^{\infty}d_n(\pi)\frac{z^n}{n!}
$$



is entire, has integral Hurwitz jets, and satisfies $G(1)=\pi$, with no
irrationality assumption needed for the construction.

Set



$$
c_0=4,\qquad c_1=1,\qquad c_n=d_n(\pi)+1\quad(n\geq2).
$$



Then



$$
s:=e+\pi=\sum_{n=0}^{\infty}\frac{c_n}{n!}.
\tag{A4}
$$



For $n\geq1$,



$$
C_n=n!\sum_{k=0}^{n}\frac{c_k}{k!}
=\lfloor n!e\rfloor+\lfloor n!\pi\rfloor
$$



and



$$
x_n=n!s-C_n=\{n!e\}+\{n!\pi\}.
\tag{A5}
$$



Since $n!e\notin\mathbb Z$, equation (A5) gives the strict bounds



$$
0<x_n<2.
\tag{A6}
$$



Coefficient comparison also gives



$$
C_{n+1}=(n+1)C_n+c_{n+1},\qquad
x_{n+1}=(n+1)x_n-c_{n+1}.
\tag{A7}
$$



These identities are the only arithmetic input needed for the HP endpoint
calculation.

## 4. Re-derivation from the complete HP system

Consider



$$
\deg A\leq a,\qquad \deg B\leq b,\qquad C(z)=\gamma,
$$



with



$$
A+Be^z+\gamma G=O(z^{a+b+1}),\qquad B(1)=\gamma.
\tag{A8}
$$



### 4.1 High equations and rank

First suppose $\gamma\ne0$. The endpoint condition gives the unique
parametrization



$$
\frac{B(z)}{\gamma}
=1+(z-1)\sum_{j=0}^{b-1}t_jz^j.
\tag{A9}
$$



Let



$$
u_j(k)=k^{\underline{j+1}}-k^{\underline j},\qquad
h(k)=\sum_{j=0}^{b-1}t_ju_j(k).
$$



The $k$-th derivative at zero of $(B/\gamma)e^z+G$ is exactly
$c_k+h(k)$. Since $A$ cancels the equations through order $a$, the
remaining equations are



$$
h(a+r)=-c_{a+r}\qquad(1\leq r\leq b).
\tag{A10}
$$



Their matrix is $M_{rj}=u_j(a+r)$. Its determinant is



$$
\det M=\left(\prod_{j=0}^{b-1}j!\right)D_{a,b},
\qquad
D_{a,b}=\frac{\Delta^b(a!)}{a!}.
\tag{A11}
$$



One direct verification uses the functional that sums falling-factorial
coefficients. The $u_j$ form a graded basis of its kernel. Evaluating the
node polynomial



$$
\mathcal W(k)=(k-a-1)^{\underline b}
$$



both at the consecutive nodes and with that functional gives



$$
\ell(\mathcal W)=(-1)^bD_{a,b},
$$



which yields (A11), including its sign. Independently,



$$
D_{a,0}=1,\quad D_{a,1}=a,\quad
D_{a,b}=(a+b-1)D_{a,b-1}+(b-1)D_{a,b-2}.
\tag{A12}
$$



Under the admissibility condition, every coefficient in (A12) is
nonnegative and the relevant leading coefficient is positive, so
$D_{a,b}>0$. Hence $M$ is nonsingular.

If $\gamma=0$, then $B(1)=0$, so $B=(z-1)T$. Its high equations are
$Mt=0$, hence $B=0$; the low equations then give $A=0$. Therefore
every nonzero solution has $\gamma\ne0$, and (A8) has a unique rational
solution up to a common scalar. This handles the full homogeneous system,
not merely a preselected cofactor.

### 4.2 Exact analytic tail

Telescoping gives



$$
\sum_{k>a}\frac{u_j(k)}{k!}=\frac1{(a-j)!},
$$



and therefore the normalized tail functional is



$$
\mathcal T_a(h)
:=a!\sum_{k>a}\frac{h(k)}{k!}
=\sum_{j=0}^{b-1}t_ja^{\underline j}.
\tag{A13}
$$



Every $h$ in the span of the $u_j$ can be written uniquely as



$$
h(k)=P(k)-kP(k-1),\qquad\deg P\leq b-1,
$$



and then



$$
\mathcal T_a(h)=-P(a).
\tag{A14}
$$



Interpolate $P(a+r)=x_{a+r}$ for $0\leq r<b$, and define
$h_0(k)=P(k)-kP(k-1)$. Equation (A7) shows that $h_0$ satisfies the
first $b-1$ equations in (A10). At the last node the discrepancy is the
standard interpolation remainder



$$
x_{a+b}-P(a+b)=\Delta^b x_a.
\tag{A15}
$$



Let $J$ be the unique polynomial in the same kernel with



$$
J(a+1)=\cdots=J(a+b-1)=0,\qquad J(a+b)=1.
$$



Writing $J=P_J-kP_J(k-1)$, the zeros imply



$$
P_J(a+r)=\frac{(a+r)!}{a!}P_J(a)\qquad(0\leq r<b).
$$



Since $\Delta^bP_J(a)=0$, the final normalization gives



$$
-D_{a,b}P_J(a)=1,
\qquad
\mathcal T_a(J)=\frac1{D_{a,b}}.
\tag{A16}
$$



Thus the actual high-equation solution is



$$
h=h_0+(\Delta^b x_a)J.
$$



Equations (A14)--(A16) yield



$$
x_a+\mathcal T_a(h)
=\frac{\Delta^b x_a}{D_{a,b}}.
\tag{A17}
$$



For $b=0$, this is the same identity with $h=0$ and $D_{a,0}=1$.

### 4.3 Endpoint and primitive-content reduction

Put



$$
R_{a,b}=-\frac{A(1)}{\gamma}.
$$



The low equations say that $-A/\gamma$ is the Taylor truncation through
degree $a$ of $(B/\gamma)e^z+G$. The latter function has value
$e+\pi=s$ at one. Its omitted tail is, by (A17),



$$
s-R_{a,b}
=\frac{\Delta^b x_a}{a!D_{a,b}}.
\tag{A18}
$$



Define



$$
W_{a,b}=\Delta^b(a!)=a!D_{a,b},\qquad
Z_{a,b}=\Delta^b C_a.
$$



Because $x_a=a!s-C_a$,



$$
\Delta^b x_a=W_{a,b}s-Z_{a,b}.
\tag{A19}
$$



Comparing (A18) and (A19) gives the exact rational endpoint



$$
R_{a,b}=\frac{Z_{a,b}}{W_{a,b}}.
\tag{A20}
$$



It remains to check that clearing the complete polynomial triple cannot
introduce a hidden endpoint factor. Let



$$
H=\gcd(W,Z),\qquad P=Z/H,\qquad Q=W/H.
$$



After the normalized solution is scaled to a primitive integral full
coefficient vector, its endpoint pair is



$$
\left(-m\frac{P}{Q},m\right)
$$



for some nonzero integer $m$. Integrality of the first coordinate and
$\gcd(P,Q)=1$ force $Q\mid m$. The endpoint gcd therefore removes the
remaining multiplier exactly, leaving, up to the harmless common sign,



$$
(-P,Q)=(-Z/H,W/H).
$$



Choosing the second coordinate positive proves (A1). This argument uses the
complete primitive triple and is independent of denominators in its interior
coefficients.

Finally, (A6) gives



$$
|\Delta^b x_a|
\leq\sum_{r=0}^{b}\binom br|x_{a+r}|
<2^{b+1},
$$



so



$$
|L_{a,b}|<\frac{2^{b+1}}{H_{a,b}}\leq2^{b+1}.
\tag{A21}
$$



## 5. Rational-case audit

The factorial digits detect rationality exactly:



$$
s\in\mathbb Q
\quad\Longleftrightarrow\quad
d_n(\pi)=n-2\ \text{eventually}.
\tag{A22}
$$



For the forward direction, write $s=p/q$. Once $q\mid n!$, the number
$x_n=n!s-C_n$ is an integer. Equations (A5)--(A6) force $x_n=1$.
Equation (A7) then gives $c_{n+1}=n$, hence
$d_{n+1}=n-1=(n+1)-2$.

Conversely, if $d_n=n-2$ eventually, then $c_n=n-1$ eventually, and



$$
\sum_{n>N}\frac{n-1}{n!}=\frac1{N!}.
$$



The infinite factorial series is consequently rational. This also explains
the maximal-tail versus terminating representation and removes any
factorial-expansion ambiguity.

For fixed $b\geq1$, rationality gives $x_a=1$ eventually, hence
$\Delta^b x_a=L_{a,b}=0$ eventually. If $s$ is irrational, any single
zero in (A1) would imply $s=Z/W\in\mathbb Q$; therefore every term is
nonzero. Thus eventual nonvanishing on any fixed $b\geq1$ ray is indeed
equivalent to the open irrationality of $e+\pi$.

For $b=0$, the rational behavior is different. Choose $a$ with
$q^2\mid a!$, write $a!=qt$, and use $x_a=1$:



$$
C_a=tp-1.
$$



Since $q\mid t$, every common divisor of $qt$ and $tp-1$ divides
$t^2$ and $tp-1$, whose gcd is one. Hence $H_{a,0}=1$ and
$L_{a,0}=1$ eventually. The source correctly separates this case.

## 6. Roth inequality: direction and exponent check

The reduced approximant is



$$
\frac{P}{Q}=\frac{Z/H}{W/H},\qquad Q=\frac WH,
$$



and its exact error is



$$
\left|s-\frac PQ\right|=\frac{|\Delta^b x_a|}{W}.
\tag{A23}
$$



For every fixed $\varepsilon>0$, all quantities are positive, so



$$
\begin{aligned}
\frac{|\Delta^b x_a|}{W}<Q^{-2-\varepsilon}
&\iff
\frac{|\Delta^b x_a|}{W}
<\left(\frac HW\right)^{2+\varepsilon}\\
&\iff
|\Delta^b x_a|W^{1+\varepsilon}
<H^{2+\varepsilon}.
\end{aligned}
\tag{A24}
$$



The inequality orientation and both exponents in the source are therefore
correct. The digit-free sufficient condition



$$
2^{b+1}W^{1+\varepsilon}<H^{2+\varepsilon}
\tag{A25}
$$



is also in the correct direction because
$|\Delta^b x_a|<2^{b+1}$.

To invoke Roth against an algebraic irrational $s$, one would still need
infinitely many distinct reduced approximants with unbounded $Q$, nonzero
errors, and (A24) for one fixed $\varepsilon>0$. Rationality must also be
excluded before that contradiction implies transcendence. The source states
all of these qualifications and does not overclaim.

## 7. Independent finite reconstruction

The source uses Machin's formula. The audit instead uses



$$
\boxed{\pi=4\left(\arctan\frac12+\arctan\frac13\right).}
\tag{A26}
$$



Indeed, tangent addition gives tangent one, and the sum lies in
$(0,\pi/2)$, so it equals $\pi/4$. Directed alternating-series
remainders through indices $2400$ and $1600$, respectively, certify
every $\lfloor n!\pi\rfloor$ through $n=530$. An independent
700-term rational Taylor enclosure is used for $e$.

The independently reconstructed vector hashes are



$$
\begin{array}{l|l}
\text{vector}&\text{SHA-256}\\ \hline
(d_0,\ldots,d_{530})&
9823adbf8b8ee2e45695284428ae465af2247354bf889979e8ddceb6139326b4\\
(\lfloor0!\pi\rfloor,\ldots,\lfloor530!\pi\rfloor)&
a862995754a480b542b697e5b5722833520c79019515e6ac9b361c0532266605\\
(C_0,\ldots,C_{530})&
b3652381f2981c3b54814625339e4a4de49556984c9cdc8792139586ce23bd8d.
\end{array}
\tag{A27}
$$



They agree with the source archive. Repeated differencing, rather than the
source binomial formula, gives the same 15,094-record stream hash

6a76552f2a1eb29060f7397b169d53db3f6fec30811e87457e86a5203ed36191.

Every independent directed interval excludes zero. Exact Fraction
comparisons give the same 31 fixed-$b$ minimizers and every archived
threshold count. The small-$b$ results are:

| $b$ | minimizing $a$ | $H_{a,b}$ | $|\Delta^b x_a|$ | $|L_{a,b}|$ |
|---:|---:|---:|---:|---:|
| 0 | 457 | 429158030184 | $0.268318590802116\ldots$ | $6.25220948765832\ldots\times10^{-13}$ |
| 1 | 406 | 149121357214 | $0.471067548404510\ldots$ | $3.15895427191220\ldots\times10^{-12}$ |
| 2 | 151 | 3372687800 | $0.363753031913091\ldots$ | $1.07852565515578\ldots\times10^{-10}$ |
| 3 | 346 | 2875602586336 | $0.0846198720213906\ldots$ | $2.94268312399908\ldots\times10^{-14}$ |
| 4 | 160 | 77085108 | $0.189428092971556\ldots$ | $2.45738895470648\ldots\times10^{-9}$ |
| 5 | 267 | 11544293376 | $0.978013179594425\ldots$ | $8.47183233949741\ldots\times10^{-11}$ |
| 6 | 232 | 1058939046 | $4.79912024502005\ldots$ | $4.53200801608750\ldots\times10^{-9}$ |

The global winner is uniquely $(346,3)$. Its independent upper bound is



$$
2.9426831239990803704\ldots\times10^{-14},
$$



while the smallest competing lower bound is



$$
5.1262279665130644169\ldots\times10^{-13}.
$$



The intervals are disjoint by a factor exceeding seventeen; uniqueness is
an exact rational comparison, not a decimal tie-break.

As a further structural check, the independent program solves nine complete
homogeneous HP matrices over $\mathbb Q$:



$$
(1,0),(1,1),(1,2),(2,3),(3,4),(5,6),(8,2),(12,10),(29,30).
$$



Every matrix has full row rank and nullity one. After clearing and
primitivizing the entire $A,B,\gamma$ vector, every reduced endpoint pair
is exactly $(-Z/H,W/H)$. The last case checks the admissibility boundary
$a=b-1$ at the largest scanned $b$.

## 8. Independent artifacts

The independent program is

scripts/independent_factorial_digit_fixed_b_audit.py

with SHA-256

9a8af7c907e20d0b5fd565d026c292a8a091c23dcae291634f641b3f0b524e77.

Its frozen result is

results/independent_factorial_digit_fixed_b_audit.json

with SHA-256

a466d912b3e887eef1cc7e123aef8e9e2d93e5c180fc940a17391189104d5ac4.

A clean independent rerun was byte-identical. The audit can be reproduced
with

    python scripts/independent_factorial_digit_fixed_b_audit.py \
      --output /tmp/independent_factorial_digit_fixed_b_audit.json

The all-degree endpoint identity and boundedness theorem are accepted. The
finite nonvanishing, minima, and threshold counts remain finite-box facts.
Nothing here proves irrationality, algebraicity, or transcendence of
$e+\pi$.
