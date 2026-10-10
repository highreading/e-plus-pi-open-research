> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Accessory scaling: an exact finite diagnostic and a compactness criterion

Date: 2026-09-13. This note separates a predeclared finite computation from
all-index algebra and from a conditional compactness theorem. It proves
neither an accessory limit nor a bound on the actual endpoint remainder.

## 1. Definitions and the closed diagnostic set

Use the actual raw family and its homogeneous equation from
`raw_hp_homogeneous_ode.md`:



$$
R_n=A_n+B_ne^z+C_n\arctan z=O(z^{3n+1}),\qquad
C_n(1)=4B_n(1),\qquad \deg(A_n,B_n,C_n)\le n.
$$



The equation is



$$
A_{3,n}y'''+A_{2,n}y''+A_{1,n}y'+A_{0,n}y=0,
\qquad A_{3,n}=z(1+z^2)Q_n.
\tag{1}
$$



Here $Q_n\ne0$, $q_n=\deg Q_n\le3$, and
$\lambda_n=\operatorname{lc}Q_n$. The notation $q_n$ in this note
means the **degree** of the accessory polynomial, not the primitive
endpoint denominator used elsewhere. Define



$$
\widehat Q_n(\zeta)=\frac{Q_n(n\zeta)}{\lambda_n n^{q_n}},\qquad
\widehat A_{j,n}(\zeta)=
\frac{A_{j,n}(n\zeta)}{\lambda_n n^{q_n+3}},\quad j=0,1,2,3.
\tag{2}
$$



The prescribed degrees were 2,4,8, with 16 authorized only if inexpensive.
The exact construction at 16 took less than one second, so the final set
is exactly $\{2,4,8,16\}$. No additional degrees were sampled. Each row
was constructed from the original rational Taylor equations, independently
of the new degree update. Polynomial cofactors, divisions, and every
coefficient in (2) were computed exactly over the rationals. The three
subleading identities proved below were checked exactly on all four rows.

The full exact polynomials A,B,C, monic Q, and scaled A1,A0 are retained in
`raw_accessory_scaling_probe.json`. The script is
`probe_raw_accessory_scaling.py`. Its saved-case mechanism avoids repeating
previous rows. The JSON additionally records 80-digit numerical accessory
roots and exact rational real-root isolating intervals of width at most
$10^{-35}$. Thus the stated reality and separation of the roots in these
four cases are exact finite facts. The numerical B,C root radii are
unvalidated numerical diagnostics, explicitly not root bounds for all n.

## 2. Finite results, with no extrapolation

All four observed accessory degrees are 3. Write
$Q_n/\lambda_n=z^3+q_2z^2+q_1z+q_0$. Rounded monic coefficients and
accessory roots in the original z coordinate are:

| n | q2 | q1 | q0 | three real roots of Q |
|---:|---:|---:|---:|---|
| 2 | 5.297530950 | -1.685778605 | -0.1015919231 | -5.595557175, -0.051886680, 0.349912906 |
| 4 | -2.825099844 | 1.346082310 | 0.2671243597 | -0.149235045, 0.837775654, 2.136559234 |
| 8 | -2.403210766 | 1.304371885 | 0.1163043373 | -0.077686240, 1.036465554, 1.444431452 |
| 16 | -2.302690594 | 1.277172809 | 0.0560305860 | -0.040814194, 1.158239266, 1.185265522 |

Coefficient arrays below are in descending powers of $\zeta$. The
normalizing denominator for A1,A0 is $\lambda_n n^6$, even though their
degrees are at most 5 and 4. This is necessary for the leading coefficients
to remain on a common scale with A3.

| n | coefficients of Qhat |
|---:|---|
| 2 | [1, 2.648765475, -0.4214446513, -0.01269899039] |
| 4 | [1, -0.7062749609, 0.08413014435, 0.004173818121] |
| 8 | [1, -0.3004013458, 0.02038081071, 0.0002271569088] |
| 16 | [1, -0.1439181621, 0.004988956283, 0.00001367934228] |

| n | coefficients of A1hat |
|---:|---|
| 2 | [1, 2.821928147, 1.939003075, 0.7252936162, 1.073376152, -0.1841051874] |
| 4 | [1.5, 1.034507489, -0.8367418660, 0.1669556486, -0.03731090420, 0.005089005541] |
| 8 | [1.75, 1.491056879, -0.4716471985, 0.03885403106, -0.001903732866, 0.0001336768824] |
| 16 | [1.875, 1.733982472, -0.2565093446, 0.009633955666, -0.0001118863039, 0.000003861435868] |

| n | coefficients of A0hat |
|---:|---|
| 2 | [-0.5, -0.4975454099, 0.1844826567, 0.1199057562, -0.02031803017] |
| 4 | [-0.75, -0.06421370997, 0.04900177253, -0.01299255098, 0.002085835031] |
| 8 | [-0.875, -0.003908056137, 0.01515541161, -0.0006777302512, 0.00005904187906] |
| 16 | [-0.9375, 0.006094250636, 0.004308250878, -0.00004047790120, 0.000001811680409] |

The numerical maximum root moduli divided by n for B,C respectively are
(1.35801,0.61110), (1.24361,0.37529), (1.50542,0.22631), and
(1.68391,0.13188). The exact-data diagnostic therefore does not support
assuming that accessory roots must be of size proportional to n. The
two positive roots at n=16 are also close to each other. No eventual
boundedness, reality, coalescence, coefficient convergence, or root scale
is inferred from these four cases. In particular, no curve or recurrence
is fitted to them.

## 3. Three exact subleading identities in the cubic regime

This section holds for every n for which $\deg Q_n=3$. It does not
assume Q is squarefree, nor that Q avoids 0 or the logarithmic poles.
The degree ledger proves that B has degree n, while the two Laurent
solution powers at infinity are n and n-1. Choose normalized germs



$$
U=e^zz^n(1+\beta z^{-1}+O(z^{-2})),\quad
H=z^n(1+\alpha z^{-1}+O(z^{-2})),\quad
V=z^{n-1}(1+\gamma z^{-1}+O(z^{-2})).
\tag{3}
$$



The low line V is unique; changing H by a multiple of V changes alpha
but not gamma. The exponential coefficient is the polynomial root sum



$$
\beta=\frac{[z^{n-1}]B}{[z^n]B}=-\sum_{B(\rho)=0}\rho.
\tag{4}
$$



Write the monic accessories as



$$
\begin{aligned}
Q/\lambda&=z^3+q_2z^2+q_1z+q_0,\\
A_1/\lambda&=(2n-2)z^5+u_4z^4+O(z^3),\\
A_0/\lambda&=-n(n-1)z^4+v_3z^3+O(z^2).
\end{aligned}
\tag{5}
$$



Then



$$
\boxed{q_2=\beta+2\gamma+2,}
\tag{6}
$$





$$
\boxed{u_4=\beta+3n^2-n+(2n-3)q_2,}
\tag{7}
$$





$$
\boxed{v_3=-n\beta-n^3-n^2-n(n-2)q_2.}
\tag{8}
$$



For (6), form the Wronskian of H,U,V from (3). The first two nonzero
terms, after removal of its nonzero constant scale, are



$$
e^zz^{3n-2}\left(1+
\frac{\beta+2\gamma+2}{z}+O(z^{-2})\right).
\tag{9}
$$



The contribution of alpha cancels because adding a multiple of the low
solution does not change a Wronskian. The coefficient of the next term
of H cannot affect (9): its replacement has degree n-2, so lowers the
Wronskian degree by two. The same is true of the second relative terms
of U and V. Comparing (9) with
$e^zz^{3n-1}Q/(1+z^2)^2$, whose monic expansion has first correction
q2/z, proves (6).

To obtain (7), substitute the first two terms of U into the scalar
equation, using the exact formula for A2 from the ODE note. The first
nontrivial coefficient, after the leading cancellation, is



$$
-\beta-3n^2-2nq_2+n+3q_2+u_4=0.
\tag{10}
$$



For the high Laurent branch H, the next equation is a resonance: alpha
is free, and its coefficient is zero. The coefficient equation is



$$
-2n^3-n^2q_2+2n^2+nq_2+nu_4+v_3=0.
\tag{11}
$$



This gives (8) after (7). Thus the two unknown subleading accessories
are fixed by q2 and the first polynomial root sum beta; no unproved
selection of the high Laurent coefficient is involved.

There is an exact formula for gamma from polynomial coefficients. When
$\deg C=n$, put $a=[z^n]A/[z^n]C$, and set



$$
v_0=[z^{n-1}]A-a[z^{n-1}]C-[z^n]C,\quad
v_1=[z^{n-2}]A-a[z^{n-2}]C-[z^{n-1}]C.
\tag{12}
$$



The low Laurent germ is $A-aC-C\arctan(1/z)$, so its first terms
are $v_0z^{n-1}+v_1z^{n-2}$. The degree ledger forces $v_0\ne0$,
and $\gamma=v_1/v_0$. If instead $\deg C=n-1$, the low solution
is C and $\gamma=[z^{n-2}]C/[z^{n-1}]C$. Negative polynomial
indices mean zero. Formula (12) also applies if A has degree below n.

Consequently, a small value of q2 can encode substantial cancellation
between a root sum of B and a ratio of leading cross-coefficients of
A,C. A bound on the separate root sums does not automatically control
the denominator v0. In particular, $q_2=O(n)$ is exactly the bound
$\beta+2\gamma+2=O(n)$; it must not be replaced by the individually
weaker estimates $\beta,\gamma=O(n^2)$.

## 4. A rigorous sufficient root condition for scaled compactness

**Conditional theorem.** Let an unbounded set of actual indices n
satisfy the following root bounds, with one constant K independent of n:
every root of B_n, C_n, and Q_n lies in $|z|\le Kn$. Then all four
scaled accessory polynomials in (2), as well as Qhat, have uniformly
bounded coefficients. Thus every subsequence with fixed accessory degree
has a coefficientwise convergent further subsequence. This theorem
allows all degrees $0\le q_n\le3$, repeated roots, and roots at any
of the fixed singular points.

**Proof.** Choose one radius $R>K+4$, and consider $z=n\zeta$ with
$|\zeta|=R$. For a polynomial P of degree at most n with all roots in
the stated disk, its product formula gives, for j=1,2,3,



$$
\left|\frac{P^{(j)}(z)}{P(z)}\right|
\le\frac{(\deg P)_{\underline j}}{[n(R-K)]^j}
\le (R-K)^{-j}.
\tag{13}
$$



A derivative that vanishes is included in this inequality. In particular
both C and U=exp(z)B are nonzero on this circle. Their logarithmic slope
difference obeys



$$
J:=\frac{U'}U-\frac{C'}C
=1+\frac{B'}B-\frac{C'}C,\qquad
|J|\ge1-\frac2{R-K}>\frac12.
\tag{14}
$$



Their derivative quotients through order three are uniformly bounded;
for U this follows by expanding $(\partial_z+1)^jB/B$.
Put $p_j=A_j/A_3$, j=0,1,2. The exact Wronskian formula gives



$$
p_2=-1-\frac{3n-1}{z}-\frac{Q'}Q+
\frac{4z}{1+z^2}.
\tag{15}
$$



It is uniformly bounded on the circle, since
$|Q'/Q|\le3/[n(R-K)]$, $|z|=nR$, and $R>4$. Applying the
scalar equation to U and C and subtracting yields the exact identity



$$
p_1=-\frac{U'''/U-C'''/C+
p_2(U''/U-C''/C)}{U'/U-C'/C}.
\tag{16}
$$



By (13)–(15), this is uniformly bounded. The C equation then gives



$$
p_0=-C'''/C-p_2C''/C-p_1C'/C,
\tag{17}
$$



which is uniformly bounded as well. No lower bound for a leading
coefficient of B or C is needed because these are scale-invariant
quotients.

Vieta's formula applied to the roots of Q/n proves uniform coefficient
bounds for Qhat. Also, exactly,



$$
\widehat A_3(\zeta)=
\zeta(\zeta^2+n^{-2})\widehat Q(\zeta).
\tag{18}
$$



Thus A3hat is uniformly bounded on the circle, and so are A0hat,A1hat,
A2hat by (15)–(17). They are polynomials of degrees bounded independently
of n. Cauchy's coefficient formula on $|\zeta|=R$ proves uniform
coefficient bounds. The finite-dimensional subsequence conclusion
follows. This proves the theorem.

An equivalent assumption for Q alone is the collection of coefficient
bounds
$[z^{q-r}](Q/\lambda)=O(n^r)$, $0\le r\le q$. Vieta gives one
direction; the elementary Cauchy root bound for the scaled monic
polynomial gives the other. Therefore the theorem can use these finitely
many accessory-ratio bounds together with O(n) roots of B and C.

## 5. Exact remaining intermediate problems

The theorem isolates a concrete compactness route: prove a uniform O(n)
root bound for the two actual polynomial solution factors B,C, and for
the accessory cubic (or its at most three scaled coefficient ratios).
The finite sample does not establish any of these all-index estimates.
For q=3, (6) exposes the first accessory coefficient as a cancellation
problem in a specific low-Laurent leading minor. Equations (7)–(8) then
control two more accessory coefficients once beta and q2 are bounded
at their required scales. They do not control the remaining coefficients.

Even the full compactness conclusion would provide only subsequential
coefficient limits. It gives neither a unique limiting equation nor the
selected solution branch or its connection constant. The fixed target
z=1 becomes $\zeta=1/n$; it lies in the collapsing inner region near
0 and the rescaled logarithmic poles. Therefore a large-circle root
bound or an outer limiting equation cannot by itself estimate R_n(1).
The primitive endpoint denominator remains a separate arithmetic input.

The new rigorous progress is (6)–(8) and the conditional compactness
criterion. The numerical table is a diagnostic for choosing a sensible
next estimate, not a proof of asymptotic behavior.

## 6. An explicit conditional limiting curve to test

The exact identities permit a more specific conjectural target than an
arbitrary limiting cubic. Suppose, on an unbounded cubic-degree
subsequence, that all of the following are proved:

1. The accessory roots are uniformly bounded in the original z plane.
2. $\beta_n/n^2\longrightarrow-1$.
3. If $a_{j,r}=[z^r](A_{j,n}/\lambda_n)$, then
   $a_{1,r}/n^{6-r}\longrightarrow0$ for r=0,1,2,3, and
   $a_{0,r}/n^{6-r}\longrightarrow0$ for r=0,1,2.

The first condition can be weakened to $\widehat Q_n\to\zeta^3$.
The third condition is a list of seven additional coefficient limits;
it is **not** a consequence of the first two identities alone. Under
these hypotheses, (7)–(8) prove



$$
\widehat Q_n\to\zeta^3,\quad
\widehat A_{3,n}\to\zeta^6,\quad
\widehat A_{2,n}\to-\zeta^6-3\zeta^5,
\quad\widehat A_{1,n}\to2\zeta^5+2\zeta^4,
\quad\widehat A_{0,n}\to-\zeta^4.
\tag{19}
$$



For example,
$v_3/n^3=-\beta/n^2-1-1/n-(1-2/n)q_2/n\to0$, so the
$\zeta^3$ coefficient of A0hat disappears rather than tending to -1.
The surviving -1 is its $\zeta^4$ coefficient.

If a sequence of nonzero solutions additionally has locally holomorphic
logarithmic-derivative convergence
$y_n'(n\zeta)/y_n(n\zeta)\to p(\zeta)$ on a domain away from zero,
Cauchy's derivative estimates justify the leading equation. After
division by $\zeta^4$, it is exactly



$$
\zeta^2p^3-\zeta(\zeta+3)p^2+(2\zeta+2)p-1=0,
$$





$$
\boxed{(\zeta p-1)\bigl(\zeta p^2-(\zeta+2)p+1\bigr)=0.}
\tag{20}
$$



Thus the possible algebraic branches under these extra assumptions are
$1/\zeta$ and
$(\zeta+2\pm\sqrt{\zeta^2+4})/(2\zeta)$. This is conditional
algebra only; existence of the limits, the zero-free domain, and the
branch selected by the actual family remain unproved.

The saved beta/n^2 values at n=2,4,8,16 are respectively
-1.002454590, -0.832648810, -0.895790935, -0.942665859. The corresponding
gamma/n^2 values are 0.913418664, 0.265540035, 0.413495383, 0.462929237.
Together with the displayed lower scaled coefficients, these four rows
make the hypotheses a reasonable explicit target to investigate. They
do not verify an asymptotic hypothesis or a rate, and no extrapolating
fit was performed.

`check_raw_accessory_subleading.py` checks the three identities with
symbolic n and free first two relative coefficients, including the
irrelevance of the second coefficients at the stated order. It also
checks the factorization (20). The output is
`raw_accessory_subleading_checks.json`; these controls use no new degree
samples.

Independent verification: audit_sources checked the full conditional
compactness proof in Section 4. Audit_results independently expanded the
Wronskian and both scalar-equation coefficients in Section 3, checked
the polynomial formula for gamma, and separately passed Section 4. Both
reviews found no substantive gap and made no additional degree sample.
