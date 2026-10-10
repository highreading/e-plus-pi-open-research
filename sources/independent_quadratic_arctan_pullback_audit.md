> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the quadratic arctangent pullback note

Date: 2026-08-26

Audited snapshots:

```text
9a0a4f3fdb7b86704b80b208350753ad1233af891480d4513903fccae0e21095  sources/quadratic_arctan_pullback_arithmetic_radius.md
c7c4101104a7f91f74af197e1b530fbef36694e914a2b73768314d4eecaa2fa6  scripts/quadratic_arctan_pullback_probe.py
5d68f547b8e70ab98cbee54036df9ba2d14a5d0948cda54043d25cab89081720  results/quadratic_arctan_pullback_p2_p5_n8.json
9aedaafe9662866aa206aab84f58c863fb9714eeb28057a4b6e1da806e888b37  scripts/quadratic_integral_jet_pullback_search.py
da45bdcbc7ae8959e0101bd18856f36617044d75d48ae77a449837ef39c44368  results/quadratic_integral_jet_pullback_search_R16.json
```

## Verdict and logical status

The exact claims in equations (3)--(18) pass.  In particular, the radius
argument for (p\geq6) is valid, none of the candidate singularities is
cancelled, and the displayed denominators are the exact reduced denominators
of the jets, including at (m=0).

The 32 endpoint-matched Hermite--Padé records also pass an independent exact
recomputation.  The candidate counts and finite integrality decisions in the
broader box search are exact and independently reproduced.  The last step of
that search---ranking algebraic root moduli and comparing them with
$\sqrt2$---uses floating arithmetic in both the original and independent
programs.  It is therefore only a finite numerical diagnostic, exactly as the
source note says.  Neither the scan nor this audit turns that observation into
an exact classification theorem.

No correction to the audited source was needed.  Nothing here establishes an
arithmetic conclusion about (e+\pi).

## 1. Analytic continuation and the singular radius

Put



$$
u_p(z)=\frac{(p-1)z}{p-z^2},\qquad F_p(z)=4\arctan u_p(z).
$$



Since



$$
u_p'(z)=\frac{(p-1)(p+z^2)}{(p-z^2)^2},
$$



the identity (F_p'=4u_p'/(1+u_p^2)) gives



$$
F_p'(z)=
 \frac{4(p-1)(p+z^2)}
 {z^4+(p^2-4p+1)z^2+p^2}.                    \tag{A1}
$$



This rederives (3).  The apparent poles of (u_p), at (z^2=p), are not
singularities of (A1), since its denominator there is



$$
p^2+(p^2-4p+1)p+p^2=p(p-1)^2\neq0.
$$



Equivalently, the logarithmic representation of arctangent has a locally
nonzero rational argument at a pole of (u_p), so a local branch continues
through it.

The remaining denominator zeros are precisely the preimages of (i) and


$$
-i).  For (u_p(z)=i), cross multiplication gives

\[
 z^2-i(p-1)z-p=0,                              \tag{A2}
\]

whose discriminant is

\[
 \Delta_p=4p-(p-1)^2=8-(p-3)^2.               \tag{A3}
\]

There is no hidden numerator cancellation.  With

\[
 A_p=p^2-4p+1,\qquad D_p(t)=t^2+A_pt+p^2,
\]

the only possible common zero with the numerator of (A1) would have
\(t=z^2=-p
$$

, but



$$
D_p(-p)=p(2p-A_p)=p(-p^2+6p-1)\neq0
$$



for every integer (p\geq2).  The zeros of (D_p) are also distinct:
$A_p=-2p$ would force (p=1), while (A_p=2p) would force


$$
p^2-6p+1=0), which has no integer root.  Thus every denominator zero of
(A1) is a genuine simple pole of (F_p'), hence a logarithmic singularity of
the continued germ of (F_p).

For (2\leq p\leq5), (A3) is positive and the two roots of (A2) are

\[
 \frac{i(p-1)\pm\sqrt{\Delta_p}}2.
\]

Their squared moduli are

\[
 \frac{(p-1)^2+\Delta_p}{4}=p.
\]

The equation for (-i) gives their conjugates, so

\[
 \rho(F_p)=\sqrt p\qquad(2\leq p\leq5).        \tag{A4}
\]

For (p\geq6), the intermediate fact needed in the source's argument is

\[
 A_p-2p=p^2-6p+1>0.                            \tag{A5}
\]

It is (1) at (p=6) and increases thereafter.  Consequently the two roots
of (D_p(t)) are distinct negative reals.  If (y=-t=|z|^2), the two
positive squared radii are the roots of

\[
 f_p(y)=y^2-A_py+p^2,
\]

and the smaller one is

\[
 \rho(F_p)^2=\frac{A_p-\sqrt{A_p^2-4p^2}}2.    \tag{A6}
\]

Moreover,

\[
 f_p(4)=16-4A_p+p^2
       =12+16p-3p^2
       =-(p-6)(3p+2).                           \tag{A7}
\]

Since (f_p(0)>0) and both roots are positive, (A7) places (4) between the
two roots.  At (p=6) the roots are (4) and (9), whereas for (p>6) the
smaller root is strictly below (4).  Together with (A4), this proves (6)--(8)
and the unique maximum \(\rho(F_5)=\sqrt5
$$

.  Substitution of (p=5) in
(A1) gives (9).

## 2. Exact Taylor jets and their reduced denominators

Write



$$
F_p'(z)=\sum_{m\geq0}q_{p,m}z^{2m}.
$$



Multiplying (A1) by its denominator gives



$$
(p^2+A_pz^2+z^4)\sum_{m\geq0}q_{p,m}z^{2m}
 =4(p-1)(p+z^2).                                \tag{A8}
$$



The constant and quadratic coefficients of (A8) yield



$$
q_{p,0}=\frac{4(p-1)}p,
 \qquad
 q_{p,1}=\frac{4(p-1)(-p^2+5p-1)}{p^3}.
$$



For (m\geq2), coefficient comparison gives



$$
p^2q_{p,m}+A_pq_{p,m-1}+q_{p,m-2}=0.
$$



Thus, on defining



$$
c_{p,0}=1,\quad c_{p,1}=-p^2+5p-1,
$$





$$
c_{p,m}=-A_pc_{p,m-1}-p^2c_{p,m-2},
$$



induction proves the exact identity



$$
q_{p,m}=\frac{4(p-1)c_{p,m}}{p^{2m+1}}.        \tag{A9}
$$



This proves (10)--(12).  Because (F_p') is even,



$$
F_p^{(2m+1)}(0)
 =\frac{4(p-1)(2m)!c_{p,m}}{p^{2m+1}},
 \qquad F_p^{(2m+2)}(0)=0,                      \tag{A10}
$$



which is (13).

If (p) is an odd prime, then (A_p\equiv1\pmod p),


$$
c_{p,1}\equiv-1\pmod p), and the recurrence gives

\[
 c_{p,m}\equiv-c_{p,m-1}\equiv(-1)^m\pmod p.  \tag{A11}
\]

Neither (4(p-1)) nor (c_{p,m}) contains a factor (p).  Since the only
prime in the denominator of (A10) is (p), the reduced denominator is
exactly

\[
 p^{,2m+1-v_p((2m)!)}.                         \tag{A12}
\]

Legendre's formula gives

\[
 2m+1-v_p((2m)!)
 =2m+1-\frac{2m-s_p(2m)}{p-1}.                 \tag{A13}
\]

The exponent is nonnegative (indeed positive here), so (A12) needs no
implicit positive-part convention.  At (p=5), (A13) is
\(3m/2+1+s_5(2m)/4=3m/2+O(\log m)
$$

.  This verifies (14)--(16).

For (p=2), the recurrence has odd initial values and reduces modulo (2)
to (c_{2,m}\equiv c_{2,m-1}\), so every (c_{2,m}) is odd.  Because



$$
v_2((2m)!)=2m-s_2(2m)=2m-s_2(m),
$$



the remaining denominator exponent in (A10) is



$$
\max\{0,(2m+1)-2-v_2((2m)!)\}
 =\max\{0,s_2(m)-1\}.                           \tag{A14}
$$



For (p=4), again every (c_{4,m}) is odd.  The denominator before
reduction is (2^{4m+2}), while the numerator has valuation
$2+v_2((2m)!)$.  Its exact reduced denominator exponent is therefore



$$
4m+2-2-(2m-s_2(m))=2m+s_2(m).                 \tag{A15}
$$



Equations (A14)--(A15) prove (17)--(18), including (m=0).  As a separate
finite implementation check, the independent program compared the actual
reduced denominators with (A12), (A14), and (A15) for every
$0\leq m\leq100$ and (p=2,3,4,5), with no mismatch.  That scan is only a
check; the preceding congruence and valuation arguments are the proofs.

## 3. Independent exact audit of the HP records

Write ordinary-coefficient polynomials



$$
B(z)=\sum_{j=0}^n b_jz^j,\qquad
 C(z)=\sum_{j=0}^n c_jz^j.
$$



For (k>n), the polynomial (A) contributes no (k)-th derivative at the
origin.  The high-order vanishing equations are therefore



$$
\sum_{j=0}^n(k)_j
 \bigl(b_j+c_jF_p^{(k-j)}(0)\bigr)=0,
 \qquad n+1\leq k\leq3n,                        \tag{A16}
$$



where $(k)_j=k!/(k-j)!$.  The endpoint row is



$$
-\sum_{j=0}^n b_j+\sum_{j=0}^n c_j=0.          \tag{A17}
$$



Thus the exact matrix convention is a $(2n+1)$-by-$(2n+2)$ matrix whose
columns are first (b_0,\ldots,b_n), then (c_0,\ldots,c_n), with rows
(A16) followed by (A17).  Once a kernel vector is chosen, the low equations
uniquely reconstruct



$$
a_k=-\frac1{k!}\sum_{j=0}^k(k)_j
 \bigl(b_j+c_jF_p^{(k-j)}(0)\bigr),
 \qquad0\leq k\leq n.                            \tag{A18}
$$



The first unconstrained ordinary Taylor coefficient is



$$
[z^{3n+1}](A+Be^z+CF_p)
 =\sum_{j=0}^n\frac{b_j+c_jF_p^{(3n+1-j)}(0)}{(3n+1-j)!}. \tag{A19}
$$



These formulas agree with the audited script.

The independent program did not import the original HP program or its matrix
routines.  It used `Fraction` arithmetic, a direct Gauss--Jordan reduction,
(A18), least-common-multiple denominator clearing, and a full-coordinate gcd.
For the endpoint signs it used independent rational bounds: the exponential
series through index (300) with a geometric tail majorant, adjacent
alternating partial sums through indices (500,501) for
$\arctan(1/5)$, adjacent partial sums through (120,121) for
$\arctan(1/239)$, and Machin's identity



$$
\pi=16\arctan(1/5)-4\arctan(1/239).
$$



For all 32 pairs $(p,n)$, (p=2,3,4,5) and (1\leq n\leq8), it
independently matched:

1. matrix shape, full row rank, and nullity one;
2. primitive-triple height and SHA-256 digest;
3. endpoint pair, its full gcd, the reduced pair, and reduced height;
4. the exact numerator and denominator of (A19); and
5. the certified endpoint sign and both bounding base-10 decades.

The independently certified decade table is



$$
\begin{array}{c|rrrrrrrr}
p&1&2&3&4&5&6&7&8\\ \hline
2&0&3&9&18&31&48&68&90\\
3&1&4&12&25&39&57&81&105\\
4&0&1&8&17&32&47&68&91\\
5&0&6&14&24&40&62&89&118
\end{array}
$$



It is exactly (21).  The original HP program was also rerun against the saved
arguments; its regenerated JSON was byte-for-byte identical to the archived
JSON.  These are exact finite certificates, not an all-degree rank theorem or
an asymptotic height estimate.

## 4. Independent audit of the broader finite search

For



$$
N(z)=Az+Bz^2,\qquad Q(z)=C+Dz+Ez^2,
\qquad u=N/Q,
$$



the endpoint constraint is (A+B=C+D+E\), exactly as in (22).  Since (C>0),
the factor (z) in (N) is never common with (Q).  If (B\neq0), the only
other numerator root is (-A/B), and a common factor exists exactly when



$$
B^2Q(-A/B)=CB^2-DAB+EA^2=0.                    \tag{A20}
$$



If (B=0), there is no other root.  This validates the original exact
reducibility test.

Because (Q(0)=C>0), absence of a denominator zero on ([0,1]) is equivalent
to strict positivity there.  It is decided exactly by its two endpoint values
and, when (E>0) and (-D/(2E)\in(0,1)), the value at that unique interior
minimum.  The independent enumerator used `Fraction` for this test.  The
original uses binary floating arithmetic only to decide whether that vertex
lies in the open interval; for the bounded integer inputs here, a nonendpoint
vertex is separated from (0,1) by at least (1/32), while endpoint values
are represented exactly, so this does not alter the enumeration.

Direct polynomial algebra gives



$$
4(N'Q-NQ')=4AC+8BCz+4(BD-AE)z^2,               \tag{A21}
$$



and



$$
Q^2+N^2=C^2+2CDz+(D^2+2CE+A^2)z^2
 +(2DE+2AB)z^3+(E^2+B^2)z^4.                   \tag{A22}
$$



Formal division of (A21) by (A22), followed by multiplication of the
coefficient of (z^r) by (r!\), exactly tests
$F^{(r+1)}(0)\in\mathbb Z$.  A fresh implementation of (A20)--(A22), with
the same displayed integer box, reproduced

```text
53036  primitive candidates with a safe path tested
  517  reducible parameterizations skipped
16158  candidates integral through derivative order 25
```

The SHA-256 digest of the independently enumerated, ordered list of all
16,158 parameter tuples is

```text
4a733843ad90def9fb19bce82cea49c098e063db7160929b0a718582a5a36cbe
```

These counts and integrality decisions use exact integer/rational arithmetic.

For a sign (s\in\{1,-1\}), the singularity equation (u(z)=si\) is



$$
(B-siE)z^2+(A-siD)z-siC=0.                     \tag{A23}
$$



The two signs give conjugate root sets, so it suffices numerically to solve
one quadratic and take the least modulus.  The original script uses
`numpy.roots`; the independent program used the explicit complex quadratic
formula in binary64 and then recomputed the 20 largest observed radii with
100-decimal-digit `mpmath` arithmetic.  It again found no value above
$\sqrt2+10^{-12}$.  The top two floating results were



$$
\begin{array}{c|c}
(A,B,C,D,E)&\text{computed least modulus}\\ \hline
(1,0,2,-1,0)&1.4142135623730950488016887242\ldots\\
(2,-1,4,-2,-1)&1.2898702345526634890795609928\ldots
\end{array}
$$



The first tuple is exactly (u(z)=z/(2-z)), for which (A23) proves that the
radius is exactly $\sqrt2$.  The observed gap to the runner-up makes the
reported floating comparison numerically stable, but the assertion that this
is the global ranking of the finite list is still a floating enumeration, not
a symbolic certificate of 16,158 algebraic inequalities.  Accordingly, the
source is correct to call the no-hit statement a reproducible finite
diagnostic rather than a theorem.

The original broad-search program was rerun with the archived arguments; its
regenerated JSON was byte-for-byte identical to the saved result.

## 5. Independent artifacts

```text
28a203d76a2ff9ec3ab71deea070a2de3bbfcf200846757a050ca6f248afb196  scripts/quadratic_arctan_pullback_independent_audit.py
0d8be7d1cb1a1f45d8a72473a2012776feb5e94a4ca95297720bc998fc6b0697  results/quadratic_arctan_pullback_independent_audit.json
```

The JSON labels the root-radius portion as floating diagnostic and records the
100-digit reranking values separately from the exact enumeration fields.
