> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the universal pullback-radius bound

## Verdict

**ACCEPT**, for the frozen source snapshot below.

The note under audit correctly proves a universal analytic ceiling for every
holomorphic endpoint-fixing pullback that omits the two singular values of



$$
F(w)=4\arctan\frac{w}{2-w}.
$$



More precisely, if $\phi(0)=0$, $\phi(1)=1$, and $\phi$ maps
$\mathbb D_R$ into
$\Omega=\mathbb C\setminus\{1-i,1+i\}$, then



$$
R\leq R_*=\sqrt{\frac{1+y}{1-y}}
<5.262410788162386,
$$



where



$$
y=\operatorname{Im}\left(
i\frac{K((1-i)/2)}{K((1+i)/2)}
\right).
$$



The affine normalization, inverse-modular-lambda convention, quotient
distance, global $\Gamma(2)$ minimization, Schwarz--Pick direction and
metric factor, half-angle formula, analytic sharpness, polynomial
singularity argument, and exact rational numerical enclosure are all valid.
No correction to the frozen source was needed.

## 1. Frozen artifacts and independent artifacts

The three inputs were hashed before the audit:

| artifact | SHA-256 |
|---|---|
| `sources/universal_pullback_radius_bound.md` | `eb753d610e81ffd909c97ae1e4c128f7cbdaa7fd90607edf2d9817ab37faac17` |
| `scripts/pullback_hyperbolic_radius_bound.py` | `f83f5d27a302c8fa74b4b0def2ada68037c1f0e555f1031410f1fd9eb10d3846` |
| `results/pullback_hyperbolic_radius_bound.json` | `f981094e58a95ad0070939bda6f2db0b6ea0b2bdef9ad33ba6b379971bef9993` |

The independent program rehashed the inputs after all calculations; the same
three values remained in force.  The independent artifacts are:

| artifact | SHA-256 |
|---|---|
| `scripts/independent_pullback_hyperbolic_radius_audit.py` | `6807d6d433220c3c177b833763db169b087d7a5f0e3c715e4a957b1e5f461d19` |
| `results/independent_pullback_hyperbolic_radius_audit.json` | `7cd4793f1c259735ceccf16543778e00ac075979a225eda131800f0771a7e93e` |

Rerunning the source certificate with its documented defaults produced a
temporary JSON file with SHA-256
`f981094e58a95ad0070939bda6f2db0b6ea0b2bdef9ad33ba6b379971bef9993`.
It therefore reproduces the archived JSON byte-for-byte.

## 2. Affine endpoint map

The affine map in the source is



$$
T(w)=\frac{w-(1-i)}{2i}.
$$



It sends the deleted values $1-i,1+i$ to $0,1$, respectively, and
therefore identifies $\Omega$ conformally with
$X=\mathbb C\setminus\{0,1\}$.  Direct calculation gives



$$
T(1)=\frac12,
\qquad
T(0)=\frac{-1+i}{2i}=\frac{1+i}{2}.
$$



Thus the two target points and their order in the hyperbolic-distance
calculation are correct.  Distance is symmetric, so the later use of the
lifts $i$ and $\tau_1$ is unaffected by which endpoint is named first.

## 3. Schwarz--Pick normalization and inequality direction

All metrics in the source use curvature $-1$.  On the radius-$R$ disk,
scaling to the unit disk gives



$$
d_{\mathbb D_R}(0,1)
=2\operatorname{artanh}\frac1R.
$$



For a holomorphic map $\phi:\mathbb D_R\to\Omega$, Schwarz--Pick contracts
the complete hyperbolic distance, hence



$$
\delta=d_\Omega(0,1)
\leq d_{\mathbb D_R}(0,1)
=2\operatorname{artanh}\frac1R.
$$



The right-hand side decreases as $R$ increases.  Applying the increasing
function $\tanh$ gives



$$
\tanh(\delta/2)\leq\frac1R,
\qquad
R\leq\coth(\delta/2).
$$



Thus neither the inequality direction nor the factor of two is reversed.
The only nontrivial case has $R>1$, so both marked points lie in the source
disk; if a polynomial pullback already has Taylor radius at most one, the
claimed upper bound is automatic.

## 4. Inverse modular-lambda convention

Use the parameter convention



$$
K(m)=\frac\pi2,{}_2F_1\left(\frac12,\frac12;1;m\right).
$$



For the principal branches, the classical inverse relation is



$$
\tau(m)=i\frac{K(1-m)}{K(m)},
\qquad
\lambda(\tau(m))=m.
$$



This is the parameter $m$, not the elliptic modulus $k$; accordingly no
square is missing.  At $m=1/2$, the numerator and denominator agree and
$\tau=i$, so $\lambda(i)=1/2$, fixing the convention.  The point
$m=(1+i)/2$ and the straight continuation from $1/2$ avoid the standard
branch cuts.  Moreover, both $m$ and $1-m=\overline m$ have modulus less
than one, so the defining hypergeometric series with real coefficients gives
directly



$$
K(1-m)=K(\overline m)=\overline{K(m)}.
$$



Consequently



$$
\tau_1=i\frac{\overline{K(m)}}{K(m)},
\qquad |\tau_1|=1.
$$



The exact enclosure audited below proves that its imaginary part satisfies
$0<y<1$, so this lift is in $\mathbb H$.  As a diagnostic independent of
the exact proof, an 80-digit theta-constant calculation evaluated



$$
\left(\frac{\vartheta_2(0,e^{\pi i\tau_1})}
{\vartheta_3(0,e^{\pi i\tau_1})}\right)^4
$$



and recovered $(1+i)/2$ with absolute residual below $10^{-80}$.  This
decimal calculation is not used for rigor.

## 5. Quotient distance and the global $\Gamma(2)$ minimum

The modular lambda function is the universal covering



$$
\lambda:\mathbb H\longrightarrow
\mathbb C\setminus\{0,1\}
$$



with deck group $\Gamma(2)$ modulo the central sign.  A universal covering
is a local isometry for the complete curvature-$-1$ metrics.  Therefore



$$
\delta=inf_{\gamma\in\Gamma(2)}
d_{\mathbb H}(i,\gamma\tau_1).
$$



For $u\in\mathbb H$, the curvature-$-1$ upper-half-plane formula is



$$
\cosh d_{\mathbb H}(i,u)=\frac{|u|^2+1}{2\operatorname{Im}u}.
$$



If



$$
\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix},
$$



then



$$
\operatorname{Im}(\gamma\tau_1)
=\frac{y}{|c\tau_1+d|^2}.
$$



Substitution proves exactly the source formula



$$
\cosh d_{\mathbb H}(i,\gamma\tau_1)
=\frac{|a\tau_1+b|^2+|c\tau_1+d|^2}{2y}.
$$



The claimed minimum is global, not a finite search.  Write
$\tau_1=x+iy$.  Since $|\tau_1|=1$ and $0<y<1$, one has $|x|<1$.
For $\gamma\in\Gamma(2)$, $a,d$ are odd and $b,c$ are even.  If
$b=0$, then $|a\tau_1+b|^2=a^2\geq1$.  If $b\ne0$, then



$$
\begin{aligned}
|a\tau_1+b|^2
&=a^2+b^2+2abx\\
&>a^2+b^2-2|ab|\\
&=(|a|-|b|)^2\geq1,
\end{aligned}
$$



because the difference of an odd and an even integer cannot be zero.  The
same argument, with $c$ even and $d$ odd, gives
$|c\tau_1+d|^2\geq1$.  Hence every numerator is at least two.  The identity
(and equivalently the central negative identity) has numerator
$|\tau_1|^2+1=2$, so it attains the infimum.  It follows that



$$
\cosh\delta=\frac1y.
$$



As a diagnostic only, the independent program enumerated 738 matrices in
$\Gamma(2)$ with entries bounded by 21 and found the identity class to be
minimal.  The parity proof above, not that enumeration, covers the infinite
group.

## 6. The exact constant and analytic sharpness

The half-angle identity has the correct form:



$$
\coth^2\frac\delta2
=\frac{\cosh\delta+1}{\cosh\delta-1}.
$$



Using $\cosh\delta=1/y$ gives



$$
R_*=\coth\frac\delta2
=\sqrt{\frac{1+y}{1-y}}.
$$



This also confirms that the right-hand side is increasing in $y$ on
$(0,1)$, as used in the numerical upper bound.

The sharpness argument is valid.  Conjugate the upper-half-plane universal
cover to a cover $p:\mathbb D\to\Omega$, and take the lifts of $0,1$
corresponding to $\tau_1,i$.  Their distance is $\delta$.  Also



$$
d_{\mathbb D}(0,1/R_*)
=2\operatorname{artanh}(1/R_*)=\delta.
$$



Holomorphic disk automorphisms act transitively on ordered pairs at a fixed
hyperbolic distance.  An automorphism can therefore carry
$(0,1/R_*)$ to the ordered lift pair.  Composing it with
$z\mapsto z/R_*$ and then with $p$ gives a holomorphic map on
$|z|<R_*$ that omits the punctures and sends $0,1$ to $0,1$.
This realizes equality in the unrestricted holomorphic class.  No polynomial
or arithmetic property is implied.

## 7. Genuine singularities for polynomial pullbacks

Let $z_0$ be a zero of multiplicity $m$ of
$\phi(z)-(1+i)$.  Locally,



$$
\phi(z)-(1+i)=c(z-z_0)^m+O((z-z_0)^{m+1}),\qquad c\ne0,
$$



and



$$
\phi'(z)=mc(z-z_0)^{m-1}+O((z-z_0)^m).
$$



Because the other denominator factor equals $2i$ at $z_0$,



$$
(F\circ\phi)'(z)=\frac{-2mi}{z-z_0}+O(1).
$$



The residue is nonzero.  The same computation over $1-i$ gives the
conjugate nonzero residue.  Thus every preimage is a genuine logarithmic
singularity even when it is a critical point of $\phi$.  A nonconstant
polynomial has preimages of both values.  If its nearest such preimage has
modulus greater than one, applying the universal bound to all smaller source
disks and taking a limit gives Taylor radius at most $R_*$; if the modulus
is at most one, the conclusion is already immediate.

## 8. Independent exact rational enclosure

The source advances its hypergeometric coefficient recursively and stores a
complex rational as a pair of Python `Fraction` values.  The independent
program instead formed, in SymPy's exact Gaussian rationals, the closed-form
sum



$$
S_{180}=\sum_{n=0}^{180}
\frac{\binom{2n}{n}^2}{16^n}
\left(\frac{1+i}{2}\right)^n.
$$



This is independent of the source recurrence.  Since
$\binom{2n}{n}\leq4^n$, every coefficient is at most one.  Moreover
$|(1+i)/2|=1/\sqrt2<71/100$, so the exact omitted-tail bound is



$$
E=\frac{(71/100)^{181}}{1-71/100}.
$$



Writing $S_{180}=A_0+iB_0$, the audit used



$$
A_0-E\leq A\leq A_0+E,
\qquad
B_0-E\leq B\leq B_0+E.
$$



Exact rational comparison verifies



$$
0<B_0-E<B_0+E<A_0-E<A_0+E.
$$



For



$$
y=\frac{A^2-B^2}{A^2+B^2},
$$



the independently propagated enclosure is



$$
\frac{(A_0-E)^2-(B_0+E)^2}
{(A_0+E)^2+(B_0+E)^2}
\leq y\leq
\frac{(A_0+E)^2-(B_0-E)^2}
{(A_0-E)^2+(B_0-E)^2}.
$$



Every numerator and denominator of the following archived fields agrees
exactly with this symbolic recomputation:

* the four component endpoints and common tail bound;
* the lower and upper endpoints for $y$;
* the upper endpoint for $(1+y)/(1-y)$; and
* the asserted rational upper bound for its square root.

Integer cross multiplication, without decimal floating point, proves



$$
\frac{930296508588526}{10^{15}}<y
<\frac{930296508588527}{10^{15}}.
$$



It also proves



$$
\left(\frac{5262410788162386}{10^{15}}\right)^2
>
\frac{1+y_{\rm upper}}{1-y_{\rm upper}}.
$$



Since the radius function is increasing and the last square comparison is
strict,



$$
R_*<5.262410788162386
$$



follows rigorously.  The longer decimals in the source result remain
diagnostics and were not used in any inequality.

## 9. Format and scope checks

The source note is valid UTF-8 and passes an `iconv` round trip.  Pandoc
converted it with `--from=markdown+tex_math_dollars --to=html` without an
error or warning.  Both source and independent Python files compile, and
both JSON outputs parse.

This accepted theorem is an analytic ceiling, not progress by itself on the
arithmetic classification of $e+\pi$.  It rules out an unbounded-radius
pullback strategy, while leaving a large gap between the current explicit
radius $>3/2$ and the universal ceiling $R_*$.
