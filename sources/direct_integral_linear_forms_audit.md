> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Direct integral linear forms in $1$ and $e+\pi$

Checked: 2026-08-26 UTC

## Scope and outcome

This note investigates direct, sign-controlled integral constructions rather
than the endpoint Hermite--Padé matrices studied elsewhere in the archive.  It
starts with integration-by-parts forms for $e$ and rational-kernel beta
forms for $\pi$, then asks whether their coefficients can be synchronized
without losing the smallness of the integrals.

The main new results are rigorous barrier theorems for the most natural
common-kernel construction.  With the symmetric beta kernel



$$
w_n(x)=x^n(1-x)^n,
\qquad n\equiv0\pmod 8,
$$



form the primitive exponential linear form from
$n!^{-1}\int_0^1w_n(x)e^x\,dx$, and form **any** primitive integer
$\pi$-linear form obtained from
$\int_0^1w_n(x)/(1+x^2)\,dx$.  Every positive integer combination which
matches their $e$- and $\pi$-coefficients has value at least



$$
\frac{n!}{(2n+1)2^{n/2}}.                         \tag{A}
$$



Thus the matched forms do not merely fail to tend to zero: their values tend
to infinity.  Even after removing any new common content from the final
matched form, its absolute value is at least



$$
\frac{4n!}{D_{2n-1}(2n+1)2^n},
\qquad D_{2n-1}=\operatorname{lcm}(1,\ldots,2n-1), \tag{A'}
$$



which also tends to infinity.  The result therefore permits full primitive
normalization.

The complementary log-free class $n\equiv4\pmod8$ has opposite
coefficient signs, but it does not evade the barrier.  A direct comparison
shows that the coefficient-matched difference has a fixed sign and absolute
value at least



$$
\frac{n!}{2(2n+1)2^{n/2}}.                        \tag{B}
$$



After final primitive reduction, the corresponding lower bound is



$$
\frac{2n!}{D_{2n-1}(2n+1)2^n},                    \tag{B'}
$$



which again tends to infinity.  Therefore all symmetric log-free beta
kernels $n\equiv0\pmod4$ are ruled out with full primitive normalization
allowed.

A second, broader but less primitive-invariant barrier covers all
non-diagonal beta kernels $x^a(1-x)^b$ for which the logarithm term
vanishes.  Clearing the polynomial-integral denominator by the universal
least common multiple makes the positive $\pi$-form diverge uniformly.

These theorems rule out clearly defined direct families.  They do not rule
out sign-indefinite cancellation, unrelated kernels with specially correlated
primitive coefficients, or an entirely different integral construction.
Nothing here proves that $e+\pi$ is algebraic, irrational, or
transcendental.

## 1. Endpoint integration by parts for $e$

For a polynomial $F\in\mathbb Q[x]$ of degree $d$, repeated integration
by parts gives the exact identity



$$
\int_0^1F(x)e^x\,dx=eA(F)-B(F),                   \tag{1}
$$



where



$$
A(F)=\sum_{k=0}^d(-1)^kF^{(k)}(1),
\qquad
B(F)=\sum_{k=0}^d(-1)^kF^{(k)}(0).                \tag{2}
$$



If all endpoint derivatives are integers, (1) is an integer linear form in
$1,e$.  A nonnegative nonzero $F$ makes the value in (1) strictly
positive.

For the symmetric beta polynomial put



$$
F_n(x)=\frac{x^n(1-x)^n}{n!},
\qquad
E_n=\int_0^1F_n(x)e^x\,dx.                        \tag{3}
$$



All endpoint derivatives of $F_n$ are integers.  Define



$$
q_n=(-1)^nA(F_n),\qquad p_n=(-1)^nB(F_n).          \tag{4}
$$



Expanding at the two endpoints gives



$$
q_n=(-1)^n\sum_{j=0}^n(-1)^j
     \frac{(n+j)!}{j!(n-j)!},                     \tag{5}
$$





$$
p_n=\sum_{j=0}^n
     \frac{(n+j)!}{j!(n-j)!}.                     \tag{6}
$$



Consequently



$$
E_n=(-1)^n(q_ne-p_n)>0.                           \tag{7}
$$



### 1.1 Positivity and a coefficient lower bound

Reverse the order of summation in (5).  The absolute terms are



$$
T_h=\binom nh\frac{(2n-h)!}{n!},
\qquad0\leq h\leq n,
$$



and



$$
\frac{T_{h+1}}{T_h}
=\frac{n-h}{(h+1)(2n-h)}<1.                       \tag{8}
$$



The alternating sum therefore has the sign of its first term and is at
least its first term minus its second.  Hence



$$
q_n\geq\frac{(2n)!-n(2n-1)!}{n!}
=\frac{n(2n-1)!}{n!}.                             \tag{9}
$$



### 1.2 The form is already primitive

Both sequences in (5)--(6) satisfy



$$
X_n=2(2n-1)X_{n-1}+X_{n-2}\qquad(n\geq2),         \tag{10}
$$



with



$$
q_0=q_1=1,\qquad p_0=1,\quad p_1=3.               \tag{11}
$$



Equation (10) follows directly by coefficient comparison in the finite sums;
equivalently, (5)--(6) are the values at $-2$ and $2$ of the standard
Bessel-polynomial recurrence, with the sign in (5) removed.

The determinant



$$
D_n=p_nq_{n-1}-p_{n-1}q_n
$$



satisfies $D_n=-D_{n-1}$ and $D_1=2$.  Every $p_n,q_n$ is odd by
(10)--(11).  A common divisor of $p_n,q_n$ divides $D_n=\pm2$ and is
odd, so



$$
\gcd(p_n,q_n)=1.                                  \tag{12}
$$



Thus the factorial division in (3) has already produced the primitive
integer form; there is no further hidden content capable of reducing
$q_n$.

## 2. Rational-kernel beta forms for $\pi$

For nonnegative integers $a,b$, set



$$
J_{a,b}=\int_0^1\frac{x^a(1-x)^b}{1+x^2}\,dx.     \tag{13}
$$



Divide in $\mathbb Z[x]$:



$$
x^a(1-x)^b=(1+x^2)S_{a,b}(x)+\alpha_{a,b}x+\rho_{a,b}.
                                                               \tag{14}
$$



It follows that



$$
J_{a,b}=r_{a,b}
+\frac{\alpha_{a,b}}2\log2
+\frac{\rho_{a,b}}4\pi,
\qquad
r_{a,b}=\int_0^1S_{a,b}(x)\,dx\in\mathbb Q.       \tag{15}
$$



Evaluation at $x=i$ gives



$$
\rho_{a,b}+i\alpha_{a,b}
=i^a(1-i)^b
=2^{b/2}\exp\!\left(\frac{(2a-b)\pi i}{4}\right).             \tag{16}
$$



Therefore the unwanted $\log2$ term vanishes exactly when



$$
2a-b\equiv0\pmod4.                               \tag{17}
$$



In that case $b$ is even and



$$
\rho_{a,b}=(-1)^{(2a-b)/4}2^{b/2}.                \tag{18}
$$



This gives an exact non-diagonal classification; it is not a numerical
pattern.

For the symmetric case $a=b=n$, condition (17) is $n\equiv0\pmod4$
and



$$
\rho_n=(1+i)^n=(-1)^{n/4}2^{n/2}.                 \tag{19}
$$



In particular,



$$
n\equiv0\pmod8\quad\Longrightarrow\quad
J_n:=J_{n,n}=r_n+\frac{2^{n/2}}4\pi>0             \tag{20}
$$



with a positive $\pi$-coefficient.

## 3. A primitive-invariant coefficient-matching barrier

We now prove the bound (A).

Let $n\geq8$ be divisible by $8$.  By (7) and (12),



$$
E_n=q_ne-p_n>0                                   \tag{21}
$$



is a primitive integer form with $q_n>0$.  Write a primitive integer
form obtained from (20) as



$$
L_n=A_n+B_n\pi=m_nJ_n>0,                          \tag{22}
$$



where $A_n,B_n\in\mathbb Z$, $B_n>0$,
$\gcd(A_n,B_n)=1$, and $m_n\in\mathbb Q_{>0}$.  The exact denominator
of $r_n$ and the content removed in reaching (22) are deliberately left
arbitrary.  From (20) and (22), the value-to-coefficient ratio is invariant:



$$
\frac{L_n}{B_n}
=\frac{J_n}{2^{n/2}/4}
=\frac{4J_n}{2^{n/2}}.                            \tag{23}
$$



Consider any positive integer combination



$$
uE_n+vL_n                                           \tag{24}
$$



whose coefficients of $e$ and $\pi$ agree.  This means



$$
u q_n=v B_n.                                      \tag{25}
$$



In the minimal combination,



$$
v=\frac{q_n}{\gcd(q_n,B_n)}\geq\frac{q_n}{B_n};   \tag{26}
$$



every other positive matched combination is a positive integer multiple of
it.  Since both integrals are positive, (23) and (26) give



$$
uE_n+vL_n\geq vL_n
\geq\frac{q_n}{B_n}L_n
=\frac{4q_nJ_n}{2^{n/2}}.                         \tag{27}
$$



On $[0,1]$, $(1+x^2)^{-1}\geq1/2$.  Hence



$$
J_n\geq\frac12\int_0^1x^n(1-x)^n\,dx
=\frac{(n!)^2}{2(2n+1)!}.                         \tag{28}
$$



Combining (9), (27), and (28) yields



$$
uE_n+vL_n
\geq
\frac{4}{2^{n/2}}
\frac{n(2n-1)!}{n!}
\frac{(n!)^2}{2(2n+1)!}
=\boxed{\frac{n!}{(2n+1)2^{n/2}}}.                \tag{29}
$$



The right side tends to infinity by Stirling's formula.  It already equals
$2520/17>1$ at $n=8$, and its ratio after increasing $n$ by eight is
greater than one for every $n\geq8$.

This proves the claimed positive-sum barrier.  Three features are worth
emphasizing.

1. The exact denominator of $r_n$ never enters the proof.
2. Arbitrary primitive reduction of the $\pi$-form cancels from the ratio
   $L_n/B_n$.
3. Matching larger multiples only increases the positive value.

Thus neither exact denominator cancellation nor endpoint-content removal
repairs this common-kernel construction.

### 3.1 The opposite-sign symmetric class also has a fixed-sign barrier

Let $n\geq4$ satisfy



$$
n\equiv4\pmod8.                                   \tag{29a}
$$



The exponential form is still



$$
E_n=q_ne-p_n>0,
$$



but (19) now gives



$$
\rho_n=-2^{n/2}.
$$



Put



$$
c_n=\frac{2^{n/2}}4.
$$



Then



$$
J_n=r_n-c_n\pi>0.                                 \tag{29b}
$$



After arbitrary primitive integer normalization, write



$$
L_n=A_n-B_n\pi=m_nJ_n>0,
\qquad B_n>0,\quad m_n>0.
$$



As in (23), primitive reduction cancels from the ratio:



$$
\frac{L_n}{B_n}=\frac{J_n}{c_n}.                  \tag{29c}
$$



To obtain equal **positive** coefficients of $e$ and $\pi$, one must
form



$$
uE_n-vL_n,\qquad uq_n=vB_n=C.                     \tag{29d}
$$



Its value per common coefficient is



$$
\frac{E_n}{q_n}-\frac{J_n}{c_n}.                  \tag{29e}
$$



This difference has a rigorous fixed sign.  Since $e^x\leq e$ on
$[0,1]$,



$$
E_n\leq\frac{e\,n!}{(2n+1)!}.                     \tag{29f}
$$



Equations (9) and (28) give



$$
\frac{E_n/q_n}{J_n/c_n}
\leq
\frac{e\,2^{n/2}}{2n(2n-1)!}
<\frac12                                            \tag{29g}
$$



for every $n\geq4$.  The last inequality is already extremely strict at
$n=4$ and follows thereafter from elementary factorial growth (one may
use $e<3$).

It follows that (29e) is negative and



$$
\left|\frac{E_n}{q_n}-\frac{J_n}{c_n}\right|
>\frac{J_n}{2c_n}.                                \tag{29h}
$$



The least common coefficient is
$C=\operatorname{lcm}(q_n,B_n)\geq q_n$; every other matched form is an
integer multiple.  Therefore



$$
|uE_n-vL_n|
\geq\frac{q_nJ_n}{2c_n}
\geq
\boxed{\frac{n!}{2(2n+1)2^{n/2}}}.                \tag{29i}
$$



The final inequality again uses (9) and (28), and the boxed quantity tends
to infinity.  This proves both noncancellation and the barrier without using
the exact denominator or content of the $\pi$-form.

### 3.2 Final cross-content and full primitive normalization

It remains to check that removing a common divisor created only after
matching the two separately primitive forms cannot destroy the preceding
bounds.  The check is uniform.

Write the primitive component coefficient pairs as



$$
(-p_n,q_n),\qquad(A_n,\varepsilon B_n),
\qquad \varepsilon\in\{1,-1\},                    \tag{29j}
$$



where $B_n>0$ and both pairs are coprime.  Put



$$
d_n=\gcd(q_n,B_n),\qquad
u_n=\frac{B_n}{d_n},\qquad
v_n=\frac{q_n}{d_n},\qquad
C_n=\frac{q_nB_n}{d_n}.                           \tag{29k}
$$



Here $C_n$ is the least common $e$- and $\pi$-coefficient.  The
constant coefficient of the matched sum or difference has the form



$$
K_n=-u_np_n\mathbin{\pm}v_nA_n.                   \tag{29l}
$$



Let



$$
H_n=\gcd(K_n,C_n)                                 \tag{29m}
$$



be the content removed in the final primitive reduction.  Then



$$
H_n\mid d_n,\qquad\text{and hence}\qquad H_n\leq B_n.          \tag{29n}
$$



To prove this, fix a prime $\ell$.  If
$v_\ell(q_n)\ne v_\ell(B_n)$, exactly one of $q_n/d_n$ and
$B_n/d_n$ is divisible by $\ell$.  Since
$\gcd(p_n,q_n)=\gcd(A_n,B_n)=1$, exactly one of the two terms in (29l)
is then divisible by $\ell$; hence $\ell\nmid K_n$.  If the two
valuations are equal, both quotients are $\ell$-adic units and the
exponent of $\ell$ in $C_n$, hence in $H_n$, is at most their common
valuation, which is the exponent in $d_n$.  This proves (29n), including
prime powers rather than only radicals.

Now write the rational part of $J_n$ in lowest terms as



$$
r_n=\frac{a_n}{b_n},\qquad \gcd(a_n,b_n)=1.
$$



The polynomial quotient in (14) has degree at most $2n-2$, so



$$
b_n\mid D_{2n-1},
\qquad D_{2n-1}=\operatorname{lcm}(1,\ldots,2n-1).             \tag{29o}
$$



Since



$$
J_n=r_n\mathbin{\pm}c_n\pi,\qquad c_n=\frac{2^{n/2}}4\in\mathbb Z,
$$



multiplication by $b_n$ gives coefficient pair
$(a_n,\pm b_nc_n)$.  Primitive reduction divides both by
$\gcd(a_n,c_n)$, because $\gcd(a_n,b_n)=1$.  Consequently



$$
B_n\leq b_nc_n\leq D_{2n-1}\frac{2^{n/2}}4.        \tag{29p}
$$



For $n\equiv0\pmod8$, divide the raw bound (29) by
$H_n\leq B_n$ and use (29p).  The final primitive matched form satisfies



$$
|\Lambda_n^{\mathrm{prim}}|
\geq
\frac{4n!}{D_{2n-1}(2n+1)2^n}.                   \tag{29q}
$$



For $n\equiv4\pmod8$, equations (29i), (29n), and (29p) similarly give



$$
|\Lambda_n^{\mathrm{prim}}|
\geq
\frac{2n!}{D_{2n-1}(2n+1)2^n}.                   \tag{29r}
$$



Finally,



$$
\log D_{2n-1}=2n+o(n)                             \tag{29s}
$$



by the prime number theorem, whereas
$\log(n!)=n\log n-n+O(\log n)$.  Both (29q) and (29r) therefore tend
to infinity.  This closes the final-content issue and makes the two
symmetric barriers fully primitive-invariant.

## 4. A universal-denominator barrier for all beta parameters

Assume (17), put $d=a+b$, and let



$$
D_{d-1}=\operatorname{lcm}(1,2,\ldots,d-1).
$$



The quotient $S_{a,b}$ in (14) has degree at most $d-2$, so the
denominator of $r_{a,b}=\int_0^1S_{a,b}$ divides $D_{d-1}$.  Therefore



$$
4D_{d-1}J_{a,b}=A_{a,b}+D_{d-1}\rho_{a,b}\pi      \tag{30}
$$



has integer coefficients.

As above,



$$
J_{a,b}\geq\frac12 B(a+1,b+1)
=\frac{a!b!}{2(d+1)!}
=\frac1{2(d+1)\binom da}
\geq\frac1{2(d+1)2^d}.                            \tag{31}
$$



Consequently



$$
4D_{d-1}J_{a,b}
\geq\frac{2D_{d-1}}{(d+1)2^d}.                   \tag{32}
$$



The prime number theorem in the equivalent Chebyshev-function form gives



$$
\log D_{d-1}=d+o(d).                              \tag{33}
$$



Since $1-\log2>0$, the right side of (32) tends to infinity, uniformly
in $a,b$ with $a+b=d$.  Thus universal least-common-multiple clearing
destroys the beta decay for **every** log-free diagonal or non-diagonal beta
kernel.

Unlike Section 3, this statement concerns the specified universal
normalization (30).  Exceptional common content in its two integer
coefficients may permit further primitive reduction.  The theorem should not
be misquoted as a lower bound for every primitive non-diagonal form.  Its
role is to identify rigorously the universal-denominator synchronization
failure.

## 5. Recurrences do not synchronize the two coefficient systems

The beta integrals do have useful exact recurrences.  Directly from the
integrands,



$$
J_{a+2,b}+J_{a,b}=B(a+1,b+1),                     \tag{34}
$$



and



$$
J_{a,b+1}=J_{a,b}-J_{a+1,b}.                      \tag{35}
$$



For



$$
I_{a,b}=\int_0^1x^a(1-x)^be^x\,dx,
$$



the second identity has the formal analogue



$$
I_{a,b+1}=I_{a,b}-I_{a+1,b},                      \tag{36}
$$



but integration by parts, for $a,b\geq1$, gives the different relation



$$
I_{a,b}=bI_{a,b-1}-aI_{a-1,b}.                    \tag{37}
$$



The rational-kernel recurrence (34) is second order in $a$ with a beta
rational forcing term, whereas the exponential endpoint coefficients obey
the Bessel recurrence (10).  Applying (35)--(37) does not preserve either
the log-free congruence (17) at every step or equality of the two target
coefficients.  The exact recurrences therefore reorganize the same
denominator and coefficient data; they do not provide the missing
synchronization.

This is a diagnosis of these displayed recurrences, not a theorem that no
more elaborate recurrence can exist.

## 6. Remaining sign-indefinite variants

Section 3.1 shows that the apparently sign-indefinite symmetric class
$n\equiv4\pmod8$ actually has a fixed negative matched difference and is
also ruled out.

For non-diagonal $x^a(1-x)^b$, the endpoint coefficient of $e$
has sign $(-1)^a$: after reversing its finite alternating sum, the terms
strictly decrease.  Equation (18) gives the independent sign of the
$\pi$-coefficient.  Only the congruence classes in which these signs agree
lead to a positive matched sum.  Opposite-sign classes are analytically
uncontrolled differences; the symmetric comparison in (29g) does not
automatically extend to them.

Thus the remaining sign issue is genuinely non-diagonal.  No claim is made
that such differences vanish or become small; they simply lie outside the
two symmetric barrier theorems.

## 7. Exact finite verification

The script

```text
scripts/direct_integral_beta_probe.py
```

constructs $w_n$, performs exact division by $1+x^2$, integrates the
quotient over $\mathbb Q$, removes the exact content of the resulting
integer $\pi$-form, computes $p_n,q_n$, verifies
$\gcd(p_n,q_n)=1$, computes the final matched content $H_n$, verifies
$H_n\mid\gcd(q_n,B_n)$, and checks the raw and fully primitive lower
bounds in Section 3.

The archived output

```text
results/direct_integral_beta_probe_n64.json
```

covers every $n\equiv0\pmod4$ from $4$ through $64$, checking the
positive-sum bound for $n\equiv0\pmod8$ and the fixed-sign difference
bound for $n\equiv4\pmod8$.  For example, at $n=8$,



$$
q_8=312129649,\qquad p_8=848456353,\qquad\rho_8=16,
$$



and



$$
J_8=-\frac{188684}{15015}+4\pi.
$$



After primitive reduction this is the form



$$
-47171+15015\pi=\frac{15015}{4}J_8.
$$



The exact positive coefficient-matching lower bound from the actual $q_8$
is



$$
\frac{24009973}{134640},
$$



while the simpler theorem bound is $2520/17$.  These computations are
checks, not ingredients in the all-index proof.

For every archived $n=4,8,\ldots,64$, the final content happens to be
$H_n=1$.  The all-index proof does not extrapolate that observation; it
uses the unconditional bounds (29n)--(29p).

## 8. Audit of Rivoal's simultaneous exponential/logarithm approximants

The published primary source is T. Rivoal, *Simultaneous Padé approximants
to the Euler, exponential and logarithmic functions*, Journal de Théorie des
Nombres de Bordeaux **27** (2015), 565--589,
DOI [10.5802/jtnb.914](https://doi.org/10.5802/jtnb.914).  For mathematical
use here, the controlling source is the author's
[corrected preprint](https://rivoal.perso.math.cnrs.fr/articles/explog.pdf),
whose note added in April 2021 says that several published misprints were
corrected, especially in Theorem 3.  It also removes the theorem numbered 4
in the published paper after correction of another misprint, describing it
as having little practical interest.  The downloaded corrected file checked
on 2026-08-26 has SHA-256
fefdfc7dbca65c33ffc83c2d1d88b798af1f0d43ec53c412b1dfad6552b642c9.

Accordingly, no argument below treats the published Theorem 4 as a valid
input.  The sound input is corrected Theorem 3.  The corrected preprint
retains the author's motivation from hoped-for linear independence involving
$e$ and a logarithm, together with the warning that the constructions do
not appear strong enough for the hoped-for Diophantine applications.

### 8.1 Corrected Theorem 3 has rigidly coupled arguments

Corrected Theorem 3 assumes



$$
d\geq2c,\qquad f\geq c,                            \tag{38}
$$



and gives one polynomial $P(z)$ in simultaneous forms for



$$
\log(1-1/z),\qquad \exp(1/z).                     \tag{39}
$$



The logarithmic remainder has order $O(z^{-c-1})$, while the exponential
remainder has order $O(z^{-(f-c+1)})$; the corrected exponential
polynomial term also contains the factor $z^{d-f-c}$.  These corrections
are substantial relative to the published statement, but they do not change
the shared functional argument $1/z$.

Forcing the exponential value to be $e$ therefore forces $1/z=1$, and
the logarithm becomes $\log0$, not a multiple of $\pi$.  Forcing
$\log(-1)=i\pi$ forces $1/z=2$, and the exponential value is $e^2$,
not $e$.

A common change of variable cannot fix this because it preserves the
coupling.  For example, replacing $1/z$ by $\eta/z$ in both functions
would give $\log(1-\eta/z)$ together with $e^{\eta/z}$.  At a point
where the exponential is $e$, the logarithm is again $\log0$.

The published 2015 theorem numbered 4 formally displayed the analogous
coupling $\log(1-z)$, $e^z$, but the author's corrected preprint removes
that result; it is not relied on here.  A construction for $e^z$ and
$\log(1-\eta z)$ with **independent** scales would be a new scaled theorem,
not a specialization of corrected Theorem 3.

### 8.2 Root-of-unity scaling and the product-formula obstruction

Suppose, even granting such an independently scaled extension, that



$$
\zeta_N=e^{2\pi i/N},qquad\eta=1-\zeta_N.         \tag{40}
$$



Then



$$
\log(1-\eta)=\log\zeta_N=\frac{2\pi i}{N}         \tag{41}
$$



for the principal branch, and



$$
|\eta|=2\sin(\pi/N).                              \tag{42}
$$



For large $N$, a selected complex embedding can therefore make a local
remainder containing $\eta^M$ look very small.  But the coefficients lie
in the cyclotomic field $K=\mathbb Q(\zeta_N)$, not in $\mathbb Q$.
The exact norm is



$$
|N_{K/\mathbb Q}(1-\zeta_N)|=\Phi_N(1)
=\begin{cases}
p,&N=p^k\text{ is a prime power},\\
1,&N>1\text{ is not a prime power}.
\end{cases}                                      \tag{43}
$$



Consequently



$$
\prod_{a\in(\mathbb Z/N\mathbb Z)^*}
|1-\zeta_N^a|^M=\Phi_N(1)^M\geq1.                 \tag{44}
$$



The selected-embedding contraction is exactly compensated by other
embeddings when $\eta$ is a cyclotomic unit, and is overcompensated in
the prime-power case.

Taking an algebraic norm of a linear form does not solve the problem: it
produces a polynomial in $e$ and $\pi$ of degree $[K:\mathbb Q]$, not
an integer linear form in $1,e,\pi$.  Taking a trace preserves linearity,
but a rigorous upper bound has the form



$$
|\operatorname{Tr}_{K/\mathbb Q}R|
\leq\sum_\sigma|R^\sigma|,                        \tag{45}
$$



and the conjugate remainders involve
$|1-\zeta_N^a|^M$.  Equation (44) shows that they cannot all inherit the
selected small factor.  The remainders are complex and have no common sign,
so no conjugate cancellation is proved.  Branches of
$\log(\zeta_N^a)$ yield rational multiples of $i\pi$, but this does not
control the magnitudes or phases in (45).

This product-formula argument does not prove that every conceivable
cyclotomic trace must be large; accidental trace cancellation is logically
possible.  It proves that the proposed selected-embedding estimate supplies
no small rational linear form.  A successful use would need new simultaneous
control of all conjugates and their phases.

### 8.3 Approximation order is not a Diophantine estimate

Corrected Theorem 3 gives the local orders $O(z^{-c-1})$ and
$O(z^{-(f-c+1)})$ under $d\geq2c$ and $f\geq c$.  These are exact
Padé-type conditions for fixed parameters.  By themselves they do not bound
the implied constants as the parameters grow, clear the factorial
denominators of all evaluated polynomials, or prove noncancellation after a
trace.  The corrected preprint gives an integral formula for the logarithmic
remainder and a series formula for the exponential remainder, but the needed
root-of-unity combination is complex rather than a positive beta integral.

Thus the corrected construction is structurally relevant but does not bypass
either coefficient synchronization or cyclotomic denominator/embedding
growth.

## 9. What the barriers leave open

The following routes remain logically open:

* two different kernels whose **primitive** $e$- and $\pi$-coefficients
  are arithmetically correlated, rather than merely made equal by taking
  cross-multiples;
* a non-diagonal sign-indefinite family with an independent proof of
  nonvanishing and a quantitative cancellation estimate;
* a cyclotomic construction with simultaneous control at every embedding and
  a trace that remains linear;
* a multiple integral whose integration-by-parts arithmetic directly
  produces a common coefficient of $e$ and $\pi$, with no subsequent
  denominator synchronization.

The symmetric common-kernel idea, universal beta denominator clearing,
the elementary beta recurrences, and the direct or hypothetically scaled
specializations of Rivoal's corrected Theorem 3 do not provide such a route.

## 10. Exact theorem statement and residual scope

The result proved in Sections 1--3 can be stated compactly as follows.

**Theorem.**  Let $n\geq4$ and $4\mid n$.  Put



$$
w_n(x)=x^n(1-x)^n,
$$





$$
E_n=\frac1{n!}\int_0^1w_n(x)e^x\,dx=q_ne-p_n,
$$



where $p_n,q_n$ are the positive coprime integers in (5)--(7), and put



$$
J_n=\int_0^1\frac{w_n(x)}{1+x^2}\,dx
=r_n+\varepsilon_n c_n\pi,
\quad
\varepsilon_n=(-1)^{n/4},\quad c_n=\frac{2^{n/2}}4.
$$



Let



$$
L_n=A_n+\varepsilon_nB_n\pi=m_nJ_n
$$



be its primitive integer normalization, with $B_n>0$, $m_n>0$, and
$\gcd(A_n,B_n)=1$.  Set



$$
d_n=\gcd(q_n,B_n),\qquad
u_n=\frac{B_n}{d_n},\qquad
v_n=\frac{q_n}{d_n}.
$$



If $\varepsilon_n=1$, define



$$
\Lambda_n=u_nE_n+v_nL_n.
$$



Then $\Lambda_n>0$, it is an integer linear form in $1,e+\pi$, and



$$
\Lambda_n\geq\frac{n!}{(2n+1)2^{n/2}}.
$$



If $\varepsilon_n=-1$, define



$$
\Lambda_n=u_nE_n-v_nL_n.
$$



Then $\Lambda_n<0$, it is again an integer linear form in $1,e+\pi$,
and



$$
|\Lambda_n|\geq\frac{n!}{2(2n+1)2^{n/2}}.
$$



In either case let $H_n$ be the gcd of the constant coefficient and the
common $e+\pi$ coefficient of $\Lambda_n$, and set
$\Lambda_n^{\mathrm{prim}}=\Lambda_n/H_n$.  With



$$
D_{2n-1}=\operatorname{lcm}(1,\ldots,2n-1),
$$



one has



$$
|\Lambda_n^{\mathrm{prim}}|
\geq
\begin{cases}
\displaystyle
\frac{4n!}{D_{2n-1}(2n+1)2^n},
&n\equiv0\pmod8,\\[8pt]
\displaystyle
\frac{2n!}{D_{2n-1}(2n+1)2^n},
&n\equiv4\pmod8.
\end{cases}                                      \tag{46}
$$



Both lower bounds in (46) tend to infinity.  Thus no sequence of fully
primitive integer linear forms generated by this symmetric common-kernel
matching procedure can tend to zero.

The positivity hypotheses are exact: $E_n,J_n,m_n,B_n,u_n,v_n$ are
positive; in the second class the minus sign is forced by the negative
$\pi$-coefficient of $J_n$.  The fixed sign in that class is supplied by
(29g), not by a numerical comparison.

The theorem does **not** include non-diagonal kernels, different beta indices
for the two component integrals, unrelated kernels, or cyclotomic traces.
Those are the precise residual scope.  It also does not prove any
irrationality or transcendence statement about $e+\pi$; it proves that
this broad and natural direct-integral attempt cannot do so.
