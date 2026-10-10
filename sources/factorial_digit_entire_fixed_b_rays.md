> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Canonical factorial digits of $\pi$: exact endpoint formula on every fixed-$b$ ray

## 1. Scope and verdict

Put



$$
d_n=\lfloor n!\pi\rfloor-n\lfloor (n-1)!\pi\rfloor
 \quad(n\geq2),
 \qquad
 G(z)=3+\sum_{n=2}^{\infty}d_n\frac{z^n}{n!}.
\tag{1}
$$



The definition and the identity $G(1)=\pi$ do not require an
irrationality assumption.  The coefficients are integral Hurwitz jets and
$G$ is entire.

This note completely evaluates the endpoint-matched Hermite--Padé systems



$$
\begin{split}
 &\deg A\leq a,\qquad \deg B\leq b,\qquad C(z)=\gamma,\\
 &A(z)+B(z)e^z+\gamma G(z)=O(z^{a+b+1}),
 \qquad B(1)=\gamma,
 \end{split}
\tag{2}
$$



for



$$
a\geq\max(1,b-1),\qquad b\geq0.
\tag{3}
$$



Write $s=e+\pi$, and define the integer sequences



$$
C_n=\lfloor n!e\rfloor+\lfloor n!\pi\rfloor,
 \qquad
 x_n=n!s-C_n
 \quad(n\geq1).
\tag{4}
$$



With $\Delta y_a=y_{a+1}-y_a$, set



$$
W_{a,b}=\Delta^b(a!),\qquad
 Z_{a,b}=\Delta^b C_a,\qquad
 H_{a,b}=\gcd(W_{a,b},Z_{a,b}).
\tag{5}
$$



The main exact formula is



$$
\boxed{
 L_{a,b}
 =\frac{W_{a,b}s-Z_{a,b}}{H_{a,b}}
 =\frac{\Delta^b x_a}{H_{a,b}}.}
\tag{6}
$$



Here $L_{a,b}$ is obtained after clearing the full polynomial triple,
making that triple primitive, and then reducing the two endpoint
coefficients by their endpoint gcd.  Thus (6) includes every denominator
and every endpoint-content cancellation; it is not a raw-cofactor formula.

Since $0<x_n<2$, (6) gives the all-degree bound



$$
|L_{a,b}|<\frac{2^{b+1}}{H_{a,b}}\leq2^{b+1}.
\tag{7}
$$



Consequently, for every fixed $b$, this ray cannot satisfy an
all-degree divergence theorem.  It is a genuinely surviving regime, but
(6) alone proves neither nonvanishing nor convergence to zero.  In fact,
for every fixed $b\geq1$, eventual nonvanishing of (6) is equivalent to
the presently open irrationality of $e+\pi$.

## 2. Canonical factorial digits without assuming irrationality

For an arbitrary real number $y$, define



$$
d_n(y)=\lfloor n!y\rfloor-n\lfloor(n-1)!y\rfloor.
\tag{8}
$$



If $u=(n-1)!y$, then



$$
d_n(y)=\lfloor n\{u\}\rfloor,
\tag{9}
$$



so



$$
0\leq d_n(y)\leq n-1.
\tag{10}
$$



Moreover, the definition telescopes exactly:



$$
\lfloor y\rfloor+\sum_{n=2}^{N}\frac{d_n(y)}{n!}
 =\frac{\lfloor N!y\rfloor}{N!}
 \longrightarrow y.
\tag{11}
$$



Thus (1) is the canonical factorial expansion with the terminating
convention when $y$ is rational.  Specializing (11) to $y=\pi$
proves $G(1)=\pi$.  The bound $d_n\leq n-1$ also gives, on every
compact set,



$$
\sum_{n\geq2}|d_n|\frac{|z|^n}{n!}
 \leq\sum_{n\geq2}n\frac{|z|^n}{n!}<\infty,
\tag{12}
$$



so $G$ is entire.  Its jets are
$G^{(0)}(0)=3$, $G'(0)=0$, and $G^{(n)}(0)=d_n\in\mathbb Z$ for
$n\geq2$.

## 3. The combined digits and the exact rationality obstruction

Define



$$
c_0=4,\qquad c_1=1,\qquad c_n=d_n+1\quad(n\geq2).
\tag{13}
$$



Adding the factorial series for $e$ and $\pi$ gives



$$
s=e+\pi
 =5+\sum_{n=2}^{\infty}\frac{d_n+1}{n!}
 =\sum_{n=0}^{\infty}\frac{c_n}{n!}.
\tag{14}
$$



For $n\geq1$, the integral Taylor numerator



$$
B_n=\sum_{k=0}^{n}\frac{n!}{k!}
\tag{15}
$$



equals $\lfloor n!e\rfloor$: the positive omitted tail is strictly
between zero and one.  Put $B_0=1$.  Equation (11) now shows, for every
$n\geq0$,



$$
C_n:=n!\sum_{k=0}^{n}\frac{c_k}{k!}
 =B_n+\lfloor n!\pi\rfloor.
\tag{16}
$$



For $n\geq1$, this is exactly the $C_n$ in (4).  Consequently



$$
C_{n+1}=(n+1)C_n+c_{n+1},
 \qquad
 x_{n+1}=(n+1)x_n-c_{n+1}.
\tag{17}
$$



Also, for $n\geq1$,



$$
x_n=\{n!e\}+\{n!\pi\},
 \qquad 0<x_n<2.
\tag{18}
$$



The lower inequality is strict because $n!e\notin\mathbb Z$; more
elementarily, its omitted exponential tail is positive and nonintegral.

The digit pattern in (13) exactly detects rationality of the target:



$$
\boxed{
 e+\pi\in\mathbb Q
 \quad\Longleftrightarrow\quad
 d_n=n-2\text{ for all sufficiently large }n.}
\tag{19}
$$



Indeed, if $d_n=n-2$ eventually, then $c_n=n-1$ eventually and



$$
\sum_{n>N}\frac{n-1}{n!}
 =\sum_{n>N}\left(\frac1{(n-1)!}-\frac1{n!}\right)
 =\frac1{N!},
\tag{20}
$$



so (14) is rational.  Conversely, let $s=p/q$ be rational in lowest
terms.  Once $q\mid n!$, the number $x_n=n!s-C_n$ is an integer.
By (18), it must equal one.  Substitution in (17) gives



$$
c_{n+1}=n,
\tag{21}
$$



or $d_m=m-2$ for every sufficiently large $m=n+1$.  The tail (20)
is precisely the usual maximal-tail representation of the same rational
number that also has a terminating factorial expansion; thus no
terminating/maximal ambiguity was suppressed in (19).

## 4. Full rank of the endpoint-matched system

Use the falling-factorial notation



$$
k^{\underline j}=k(k-1)\cdots(k-j+1),
 \qquad k^{\underline0}=1,
\tag{22}
$$



and put



$$
u_j(k)=k^{\underline{j+1}}-k^{\underline j}
 \quad(0\leq j<b).
\tag{23}
$$



Suppose first that $\gamma\ne0$.  The endpoint condition in (2)
allows the unique parametrization



$$
\frac{B(z)}{\gamma}=1+(z-1)T(z),
 \qquad
 T(z)=\sum_{j=0}^{b-1}t_jz^j.
\tag{24}
$$



The normalized $k$-th jet of
$(B/\gamma)e^z+G$ is



$$
c_k+h(k),
 \qquad h(k)=\sum_{j=0}^{b-1}t_j u_j(k).
\tag{25}
$$



Since $A$ has degree at most $a$, the high equations in (2) are



$$
h(a+r)=-c_{a+r}\quad(1\leq r\leq b).
\tag{26}
$$



Let



$$
M_{rj}=u_j(a+r)
 \quad(1\leq r\leq b,\ 0\leq j<b),
 \qquad
 \kappa_b=\prod_{j=0}^{b-1}j!.
\tag{27}
$$



Then



$$
\det M=\kappa_bD_{a,b},
 \qquad
 D_{a,b}=\frac{\Delta^b(a!)}{a!}>0.
\tag{28}
$$



Here and below an empty determinant and empty product have value one.
For completeness, define on polynomials in the falling-factorial basis



$$
\ell\!\left(\sum_jp_jk^{\underline j}\right)=\sum_jp_j.
\tag{29}
$$



The polynomials $u_0,\ldots,u_{b-1}$ form a basis of $\ker\ell$
inside the polynomials of degree at most $b$.  Let



$$
\mathcal W(k)=\prod_{r=1}^{b}(k-a-r)=(k-a-1)^{\underline b}.
\tag{30}
$$



The determinant of the functionals consisting of evaluation at
$a+1,\ldots,a+b$ followed by $\ell$, on the monic graded basis
$1,u_0,\ldots,u_{b-1}$, can be evaluated in two ways.  Expansion in
the last row gives $(-1)^b\det M$.  Replacing the final monomial by
$\mathcal W$ gives



$$
\kappa_b\ell(\mathcal W),
\tag{31}
$$



because the consecutive-node Vandermonde is $\kappa_b$.  The falling
binomial identity yields



$$
\begin{split}
 \ell(\mathcal W)
 &=\sum_{r=0}^{b}\binom br
       \bigl(-(a+1)\bigr)^{\underline{b-r}}\\
 &=(-1)^b\sum_{r=0}^{b}(-1)^{b-r}\binom br
       \frac{(a+r)!}{a!}
 =(-1)^bD_{a,b}.
 \end{split}
\tag{32}
$$



This proves (28), including its sign.

The numbers $D_{a,b}$ have the useful exact recurrence



$$
D_{a,0}=1,\qquad D_{a,1}=a,
 \qquad
 D_{a,b}=(a+b-1)D_{a,b-1}+(b-1)D_{a,b-2}.
\tag{33}
$$



To prove it, expand



$$
a!D_{a,b}=\int_0^\infty t^a(t-1)^be^{-t}\,dt
\tag{34}
$$



and integrate the derivative of
$t^{a+1}(t-1)^{b-1}e^{-t}$.  The recurrence and the two positive base
values prove $D_{a,b}>0$ under (3).  In particular,



$$
\begin{split}
 D_{a,2}&=a^2+a+1,\\
 D_{a,3}&=a^3+3a^2+5a+2,\\
 D_{a,4}&=a^4+6a^3+17a^2+20a+9.
 \end{split}
\tag{35}
$$



It remains to justify the normalization $\gamma\ne0$.  If
$\gamma=0$, then $B(1)=0$, so $B=(z-1)T$.  The high equations
become $Mt=0$; (28) forces $B=0$, and then the low equations force
$A=0$.  Thus every nonzero solution of (2) has $\gamma\ne0$, and
(24)--(26) give its unique rational solution up to a common scalar.

## 5. Exact tail and finite-difference identity

For $0\leq j<b$, direct telescoping gives



$$
\sum_{k>a}\frac{u_j(k)}{k!}
 =\sum_{k>a}\left(\frac1{(k-j-1)!}-\frac1{(k-j)!}\right)
 =\frac1{(a-j)!}.
\tag{36}
$$



Thus, for $h=\sum t_ju_j$, define



$$
\mathcal T_a(h)=a!\sum_{k>a}\frac{h(k)}{k!}
 =\sum_{j=0}^{b-1}t_ja^{\underline j}.
\tag{37}
$$



Every $h\in\ker\ell$ can be written uniquely as



$$
h(k)=P(k)-kP(k-1),\qquad \deg P\leq b-1,
\tag{38}
$$



and (37) then says



$$
\mathcal T_a(h)=-P(a).
\tag{39}
$$



We now compute the tail of the solution of (26).  Interpolate a
polynomial $P$ of degree at most $b-1$ through



$$
P(a+r)=x_{a+r}\quad(0\leq r<b),
\tag{40}
$$



and put $h_0(k)=P(k)-kP(k-1)$.  By (17), $h_0$ has the required
values in (26) for $1\leq r<b$.  Let $J\in\ker\ell$ be the unique
polynomial which vanishes at $a+1,\ldots,a+b-1$ and satisfies
$J(a+b)=1$.  If $J(k)=P_J(k)-kP_J(k-1)$ and
$p=P_J(a)$, its zeros imply



$$
P_J(a+r)=\frac{(a+r)!}{a!}p\quad(0\leq r<b).
\tag{41}
$$



Because $\Delta^bP_J(a)=0$, equations (28) and (41) give



$$
P_J(a+b)=p\left(\frac{(a+b)!}{a!}-D_{a,b}\right).
\tag{42}
$$



The normalization $J(a+b)=1$ therefore gives
$-pD_{a,b}=1$.  By (39),



$$
\mathcal T_a(J)=\frac1{D_{a,b}}.
\tag{43}
$$



The discrepancy between $h_0(a+b)$ and the last equation in (26) is



$$
x_{a+b}-P(a+b)=\Delta^b x_a.
\tag{44}
$$



Consequently the actual solution is



$$
h=h_0+(\Delta^b x_a)J,
\tag{45}
$$



and (39), (40), and (43) prove



$$
x_a+\mathcal T_a(h)=\frac{\Delta^b x_a}{D_{a,b}}.
\tag{46}
$$



For $b=0$, the same statement is immediate with $h=0$ and
$D_{a,0}=1$.

Now put



$$
R_{a,b}=-\frac{A(1)}{\gamma}.
\tag{47}
$$



The low equations in (2) say that $-A/\gamma$ is the Taylor
truncation of $(B/\gamma)e^z+G$ through degree $a$.  The value of the
full analytic function at one is $s$, by $B(1)/\gamma=1$.  Hence its
tail, together with (46), gives



$$
s-R_{a,b}
 =\frac{x_a+\mathcal T_a(h)}{a!}
 =\frac{\Delta^b x_a}{a!D_{a,b}}.
\tag{48}
$$



But



$$
\Delta^b x_a
 =\Delta^b(n!s-C_n)
 =W_{a,b}s-Z_{a,b},
 \qquad W_{a,b}=a!D_{a,b}.
\tag{49}
$$



Comparison of (48) and (49) proves the exact rational approximant



$$
R_{a,b}=\frac{Z_{a,b}}{W_{a,b}}.
\tag{50}
$$



Equations (17), (33), (49), and



$$
\Delta^bY_a=\Delta^{b-1}Y_{a+1}-\Delta^{b-1}Y_a
\tag{51}
$$



are exact integer recurrences for computing every quantity in (5) and
(6), using only the canonical digit block through index $a+b$.

## 6. Complete endpoint-content reduction

Write



$$
H=H_{a,b},\qquad P=Z_{a,b}/H,qquad Q=W_{a,b}/H.
\tag{52}
$$



Then $\gcd(P,Q)=1$ and $R_{a,b}=P/Q$.  Begin with the normalized
rational solution $\gamma=1$, clear all coefficients of the full triple,
and then make the full coefficient vector primitive.  Its endpoint pair
has the form



$$
\left(-m\frac PQ,m\right)
\tag{53}
$$



for a nonzero integer $m$.  Since the first entry is also an integer,
coprimality forces $Q\mid m$.  Thus (53) is an integral multiple of



$$
(-P,Q)=\left(-\frac{Z_{a,b}}H,\frac{W_{a,b}}H\right).
\tag{54}
$$



Dividing the two endpoint coefficients by their endpoint gcd removes
that multiple exactly.  This proves (6), independently of the denominator
needed to clear the interior polynomial coefficients.

Because $0<x_n<2$,



$$
|\Delta^b x_a|
 \leq\sum_{r=0}^{b}\binom br|x_{a+r}|
 <2^{b+1},
\tag{55}
$$



which proves (7).

## 7. What happens if $e+\pi$ is rational

Suppose $s=p/q$ in lowest terms.  Section 3 proves that



$$
x_a=1
\tag{56}
$$



for every sufficiently large $a$.  Therefore, for each fixed
$b\geq1$,



$$
\Delta^b x_a=0,
 \qquad L_{a,b}=0
\tag{57}
$$



eventually.  If instead $b=0$, choose $a$ so large that
$q^2\mid a!$, and write $a!=qt$, so $q\mid t$.  From (56),



$$
C_a=tp-1.
\tag{58}
$$



Since every common divisor of $qt$ and $tp-1$ also divides $t^2$
and $tp-1$, it must be one.  Hence



$$
H_{a,0}=\gcd(a!,C_a)=1,
 \qquad L_{a,0}=1
\tag{59}
$$



eventually.

These statements precisely delimit the logical obstruction.  For a fixed
$b\geq1$, $L_{a,b}\ne0$ for every sufficiently large $a$ if and
only if $s$ is irrational: by (6), even one zero would give
$s=Z_{a,b}/W_{a,b}\in\mathbb Q$, while rationality gives the eventual
zeros in (57).  For $b=0$, rationality instead produces the nonzero
constant primitive value one.  In particular, an unbounded subsequence of
$H_{a,0}$ would already exclude rationality and, by (7), would produce
nonzero primitive forms tending to zero.  No such all-degree gcd theorem
is currently proved.

## 8. Varying $b$, denominator growth, and the Roth threshold

The reduced rational approximant in (50) has denominator



$$
Q_{a,b}=\frac{W_{a,b}}{H_{a,b}},
\tag{60}
$$



and exact error



$$
\left|s-\frac{P_{a,b}}{Q_{a,b}}\right|
 =\frac{|\Delta^b x_a|}{W_{a,b}}
 <\frac{2^{b+1}}{W_{a,b}}
 =\frac{2^{b+1}}{Q_{a,b}H_{a,b}}.
\tag{61}
$$



For any fixed $\varepsilon>0$, the exact condition for this approximant
to satisfy the Roth-strength inequality



$$
\left|s-\frac{P}{Q}\right|<Q^{-2-\varepsilon}
\tag{62}
$$



is



$$
|\Delta^b x_a|W_{a,b}^{1+\varepsilon}
 <H_{a,b}^{2+\varepsilon}.
\tag{63}
$$



The digit-free bound (55) gives the stronger, easily checked sufficient
condition



$$
2^{b+1}W_{a,b}^{1+\varepsilon}
 <H_{a,b}^{2+\varepsilon}.
\tag{64}
$$



Thus a transcendence argument along varying $b$ would require not merely
$H_{a,b}\to\infty$, but gcd growth on roughly the square-root scale of
$W_{a,b}$, unless a separate theorem forces exceptionally small
$|\Delta^b x_a|$.  It would also require nonzero errors and unbounded,
distinct reduced denominators.  No deterministic lower bound for
$H_{a,b}$ beyond $H_{a,b}\geq1$, no such square-root-scale
subsequence, and no useful all-degree lower bound for
$|\Delta^b x_a|$ are proved here.  These are the exact remaining
arithmetic bottlenecks, rather than analytic continuation or rank.

## 9. Exact finite diagnostics

The companion program used Machin's identity with alternating rational
remainders to certify every $\lfloor n!\pi\rfloor$ through $n=530$.
It scanned all 15,094 admissible endpoints with



$$
1\leq a\leq500,\qquad 0\leq b\leq30,
\tag{65}
$$



using exact integers for $W,Z,H$ and directed rational intervals for
both $\Delta^b x_a$ and $L_{a,b}$.  All intervals excluded zero.
The following table records separately the cancellation numerator and the
endpoint gcd at each small fixed-$b$ minimum.  The decimal strings are
rounded diagnostic renderings; all comparisons use the exact rational
endpoints reconstructed by the script, whose hashes are stored in the
result.

| $b$ | minimizing $a$ | $H_{a,b}$ | $|\Delta^b x_a|$ | $|L_{a,b}|$ |
|---:|---:|---:|---:|---:|
| 0 | 457 | 429,158,030,184 | 0.268318590802116 | $6.25220948765832\times10^{-13}$ |
| 1 | 406 | 149,121,357,214 | 0.471067548404510 | $3.15895427191220\times10^{-12}$ |
| 2 | 151 | 3,372,687,800 | 0.363753031913091 | $1.07852565515578\times10^{-10}$ |
| 3 | 346 | 2,875,602,586,336 | 0.0846198720213906 | $2.94268312399908\times10^{-14}$ |
| 4 | 160 | 77,085,108 | 0.189428092971556 | $2.45738895470648\times10^{-9}$ |
| 5 | 267 | 11,544,293,376 | 0.978013179594425 | $8.47183233949741\times10^{-11}$ |
| 6 | 232 | 1,058,939,046 | 4.79912024502005 | $4.53200801608750\times10^{-9}$ |

The global minimum in (65) is uniquely certified at $(a,b)=(346,3)$,
the fourth row of the table.  The previously observed small case
$(8,2)$ has



$$
H_{8,2}=840,\qquad
 |\Delta^2x_8|=0.155483269210311\ldots,\qquad
 |L_{8,2}|=0.000185099130012275\ldots.
\tag{66}
$$



Thus its smallness, like that of the finite-box record, primarily comes
from endpoint gcd rather than an exceptionally tiny finite difference.
For the record $(346,3)$,
$\log H/\log W=0.0168921\ldots$, far below the square-root scale
suggested by (64).  This is diagnostic only; neither that ratio nor any
finite minimum is an asymptotic theorem.

The scan is reproducible byte for byte with:

```text
python scripts/factorial_digit_entire_nondiagonal_probe.py \
  --output results/factorial_digit_entire_nondiagonal_a500_b30.json
```

Frozen companion artifacts:

* `scripts/factorial_digit_entire_nondiagonal_probe.py`  
  SHA-256 `997127083235cafcef7d815feef587db3d4c6c02d56e4d62d749614a3b145c93`;
* `results/factorial_digit_entire_nondiagonal_a500_b30.json`  
  SHA-256 `84cb3eaafeba0887c8291883a0acb0e727217d0c3df509bab9ef9fe808522741`.

The exact formulas (6), (17), (28), (33), and (48)--(54), as well as the
uniform bound (7), are all-degree theorems.  The nonvanishing statements,
minima, threshold counts, and numerical ratios in the JSON file are
finite-box certificates only.  They do not prove irrationality or
transcendence of $e+\pi$.
