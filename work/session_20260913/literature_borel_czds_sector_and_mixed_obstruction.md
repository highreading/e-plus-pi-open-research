> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Borel complex-zero decrease: a valid pencil theorem and an actual half-plane obstruction

Date: 2026-09-13. Bounded original/literature continuation by audit_results.
Independent review pending.

The stronger Laguerre complex-zero-decreasing theorem does apply to every
real phase-adjusted high Legendre combination. It proves that each such
Borel transform has at most $n-2$ nonreal zeros. It does not apply directly
to the actual mixed polynomial after rotation, whose coefficients are
generally complex. Applied before rotation, its inequality is in the
opposite direction from the desired upper bound on real zeros.

There is an exact all-index obstruction to replacing the interval count by
a half-plane count: for every $n\ge3$ and $c>0$, the actual high-block
polynomial


$$
F_{2n-1}(x)-cF_{2n-2}(x)
$$


has all $2n-1$ zeros in the open right half-plane. This is not a
counterexample to the proposed bound on zeros in $(0,1)$. It rules out
that particular stronger half-plane estimate.

No degree/prime scan or numerical zero calculation is used.

## 1. Objects, phases, and the precise known theorem

Write


$$
\mathcal B\!\left(\sum a_jx^j\right)=\sum \frac{a_j}{j!}x^j,\qquad
 F_k=\mathcal BQ_k,
$$


where $Q_k$ is the actual monic imaginary-axis Legendre polynomial.
The polynomials


$$
p_k(t)=i^{-k}Q_k(it),\qquad g_k(t)=i^{-k}F_k(it)=\mathcal Bp_k(t)
                                                               \tag{1}
$$


are real, and $p_k$ is the monic ordinary Legendre polynomial.
The real and complex rotations commute with $\mathcal B$.

The [Craven–Csordas survey, Definition 1.5 and Theorem 4.1](https://math.hawaii.edu/~tom/mathfiles/czdssurvey.pdf)
states the complex-zero-decreasing inequality for **real input
polynomials**, counting all nonreal zeros with multiplicity. It explicitly
includes the sequence $1/j!$, obtained from $1/\Gamma(z+1)$. Thus


$$
Z_{\mathbb C\setminus\mathbb R}(\mathcal Bp)
 \le Z_{\mathbb C\setminus\mathbb R}(p),\qquad p\in\mathbb R[x].
                                                               \tag{2}
$$


All diagonal coefficients are nonzero, so degree is unchanged. Equivalently,
$\mathcal Bp$ has **at least** as many total real zeros as $p$.
This is not an upper bound on positive real zeros.

For a real actual mixture $Q=\sum c_kQ_k$, the rotated polynomial is


$$
Q(it)=\sum c_ki^kp_k(t)=U(t)+iV(t),
                                                               \tag{3}
$$


where $U$ is real and even and $V$ is real and odd. If both parities
are present, no single scalar phase makes the entire polynomial real.
The actual target is $\mathcal BQ=\sum c_kF_k$; its rotation is
$\mathcal BU+i\mathcal BV$, rather than a real member of (1).

## 2. A genuine all-index consequence for the real high pencil

**Proposition 1.** Let $0\ne p$ be a real combination of
$p_m,p_{m+1},\ldots,p_N$, where $m\le N$, and let $d=\deg p$.
Then


$$
Z_{\mathbb C\setminus\mathbb R}(\mathcal Bp)\le d-m,
\quad\text{and hence}\quad
 Z_{\mathbb C\setminus\mathbb R}(\mathcal Bp)
 \le2\left\lfloor\frac{d-m}{2}\right\rfloor.                    \tag{4}
$$



Proof. The input is orthogonal on $[-1,1]$, with its positive constant
weight, to every polynomial of degree less than $m$. If it had fewer
than $m$ sign changes there, multiply the linear factors at its
sign-change points. The resulting product with $p$ would have a fixed
nonzero sign almost everywhere, contradicting orthogonality. Thus $p$
has at least $m$ distinct real zeros. Apply (2) and degree preservation.
The even-integer refinement uses real coefficients of $\mathcal Bp$.

Taking $m=n+1$, $N=2n-1$ gives


$$
Z_{\mathbb C\setminus\mathbb R}
 \left(\sum_{k=n+1}^{2n-1}a_kg_k\right)\le n-2
 \quad (a_k\in\mathbb R).                                    \tag{5}
$$


This is stronger than preservation of the zeros of one polynomial or of
one parity alone. It does not assert that the surviving real zeros remain
inside $[-1,1]$, and it does not transfer orthogonality through Borel.

In (3), every nonzero real pencil $U+sV$, $s\in\mathbb R$, satisfies
the input hypothesis and so $\mathcal BU+s\mathcal BV$ satisfies (4).
The desired value of the pencil parameter is $s=i$, which (2) does not
cover. A quantitative theorem for that complex parameter would require
additional information beyond these real-pencil root counts.

## 3. Why a complex-coefficient count extension cannot be assumed

The failure is algebraic, not merely a missing citation. Let


$$
p(z)=(z-1)(z-i)=z^2-(1+i)z+i.
$$


It has one real zero and one nonreal zero, while


$$
\mathcal Bp(z)=\tfrac12(z-(1+i))^2
$$


has two nonreal zeros, counted with multiplicity. Thus (2) is false for
general complex coefficients.

Nor does preservation of a half-plane imply a monotonic count of zeros
in that half-plane for inputs having zeros on both sides. A real,
boundary-free example is


$$
q(x)=(x-4)((x+1)^2+25)=x^3-2x^2+18x-104.
$$


Its open-right-half-plane zero count is one. But


$$
6\mathcal Bq(x)=x^3-6x^2+108x-624=:r(x)
$$


has all three roots there. Indeed
$r'=3((x-2)^2+32)>0$, and $r(0)<0<r(6)$, so it has a unique
real root $a\in(0,6)$. Its nonreal pair has real part
$(6-a)/2>0$. This example is not asserted to be an actual high-block
mixture. It specifically disproves the proposed general half-plane
count-preservation rule, including within the real-input rotation symmetry.

## 4. What sector preservation really supplies

For degree $d$, the binomial symbol of Borel is


$$
J_d(z)=\sum_{j=0}^d\binom dj\frac{z^j}{j!}=L_d(-z).
                                                               \tag{6}
$$


All its roots are negative real numbers. The circular-region Schur–Szegő
composition statement in the
[same survey, Theorem 2.4(1)](https://math.hawaii.edu/~tom/mathfiles/czdssurvey.pdf)
therefore gives the following exact consequence: if all roots of a
complex input lie in an open half-plane through the origin, so do all
roots of its Borel transform. For explicit strictness, put the finite
input root set in the closed half-plane
$\operatorname{Re}(e^{-i\theta}z)\ge\epsilon>0$.
The theorem applies to this closed circular region, and describes each
output root as $-\beta_j w$, where $\beta_j<0$ is a root of $J_d$
and $w$ belongs to that region. Its rotated real part is therefore
strictly positive.
Intersect two half-planes to obtain convex-sector preservation.

This conclusion genuinely permits complex coefficients. It requires
**all** input roots in the region. It does not give a count inequality
for a general input split across regions; Section 3 illustrates the
distinction.

There is no uniform strict sector contraction for $1/j!$. For fixed
$0<\theta<\pi/2$, consider


$$
p_m(z)=z^m(z^2-2\cos\theta\,z+1).
$$


After setting $z=(m+1)u$ and removing its nonzero common factor, its
Borel transform has quadratic factor


$$
1-2\cos\theta\,u+\frac{m+1}{m+2}u^2.
$$


For large $m$ its two roots have arguments


$$
\pm\theta_m,\qquad
 \cos\theta_m=\cos\theta
                 \sqrt{\frac{m+2}{m+1}},\qquad \theta_m\longrightarrow\theta.
                                                               \tag{7}
$$


Consequently no fixed smaller angle works for all degrees.
This is also the factorial instance of the necessary condition in
[Cardon–Forgács–Piotrowski–Sorensen–White, Section 4.2](https://arxiv.org/pdf/1802.02641).
That paper's stricter contraction theorem concerns a different multiplier,
$\exp(-a j^2)$, and cannot be substituted for Borel.

For completeness, $4+z^4$ and its Borel transform have exactly the same
four arguments, so strict contraction of arbitrary double sectors fails
as well. These generic examples do not refute an estimate using additional
actual high-block structure.

## 5. An actual all-index obstruction to a half-plane replacement

**Proposition 2.** For every $k\ge0$ and $c>0$, all roots of


$$
Q_{k+1}(x)-cQ_k(x),\qquad F_{k+1}(x)-cF_k(x)
                                                               \tag{8}
$$


lie in the open right half-plane.

Proof for the raw polynomial. Ordinary monic Legendre polynomials have
simple strictly interlacing roots. Thus the partial fractions are


$$
\frac{p_k(z)}{p_{k+1}(z)}
   =\sum_{j=1}^{k+1}\frac{w_j}{z-t_j},
 \qquad w_j>0,\quad \sum_jw_j=1.                              \tag{9}
$$


The positivity follows immediately from the signs of
$p_k(t_j)/p_{k+1}'(t_j)$ in the interlacing order. Hence the imaginary
part of (9) is strictly negative for $\operatorname{Im}z>0$, strictly
positive for $\operatorname{Im}z<0$, and zero on the real line away
from the poles.

The equation $p_{k+1}+icp_k=0$ is equivalent to
$p_k/p_{k+1}=i/c$. No pole is a root, by coprimality. Every root
therefore lies in the open lower half-plane. Since


$$
Q_{k+1}(iz)-cQ_k(iz)
       =i^{k+1}(p_{k+1}(z)+icp_k(z)),
$$


rotation gives the first assertion of (8). The second follows from the
genuine half-plane-preservation statement in Section 4 and linearity.

Set $k=2n-2$. Both indices belong to the actual high block for $n\ge3$,
and the degree is $2n-1>n$. Therefore an upper bound of $n$ for all
right-half-plane zeros of arbitrary actual mixtures is false in every
such degree. The positive-interval zero bound can still hold because
most of these half-plane zeros may be nonreal or outside the interval.

## 6. Chasse's sector result: checked scope and access limitation

The indexed author-hosted
[Chasse paper, Theorem 3.3](https://people.kth.se/~chasse/LaguerreSector.pdf)
was inspected at its theorem statement: the Obreschkoff result retains a
real-rooted real polynomial input and imposes a narrow double-sector
condition on the second polynomial; the Schur-composition version also
requires nonnegative coefficients of that second input. This is not a
theorem allowing an arbitrary complex high Legendre mixture as the first
input.

The author-hosted URL currently returns 404 to direct retrieval; the search
index supplied the theorem and the sector definitions, but not a reliable
full text for its later Theorems 3.9–3.11. No unseen later assertion is
invoked here. The half-plane result actually used in Proposition 2 was
checked independently through the accessible Schur–Szegő theorem. The
later sector-reducer paper was read directly in its primary arXiv version.

## 7. Exact remaining crossing problem and route priority

Write a nonzero real actual mixture as


$$
f(x)=A(x^2)+xB(x^2).
$$


If one parity component is zero, its positive zeros are handled directly
by the corresponding parity ECT theorem. Assume below both $A,B$ are
nonzero. The two separate parity ECT bounds control positive zeros of $A$ and
$B$, but not all crossings between them. There is an exact formulation
which preserves the missing sign information.

Let $D=\gcd(A,B)$ over $\mathbb R[y]$, $A=DA_0$, $B=DB_0$, and


$$
P(y)=A_0(y)^2-yB_0(y)^2.
$$


On $0<y<1$, coprimality means a zero of $P$ is never a common zero
of $A_0,B_0$. The corresponding positive zero of
$A_0(x^2)+xB_0(x^2)$ occurs exactly when $A_0(y)B_0(y)<0$.
Moreover the unwanted factor $A_0(y)-\sqrt yB_0(y)$ is nonzero there,
so multiplicities agree. Thus, counting multiplicities,


$$
Z_{(0,1)}(f)
 =Z_{(0,1)}(D)
  +\sum_{\substack{y\in(0,1):P(y)=0\\A_0(y)B_0(y)<0}}
        \operatorname{ord}_y(P).                            \tag{10}
$$


Here the first term denotes zeros in the y interval; $y=x^2$ is a
diffeomorphism and preserves multiplicities.
For a distinct-zero count, take the cardinality of the UNION of the
positive zero set of $D$ and the displayed sign-selected set, so that
an intersection is not counted twice. The originally needed mixed bound
concerns this union; a bound counting all multiplicities would be a
stronger sufficient statement and is not silently assumed.

The sharp next lemma would bound the **sign-selected** crossings in
(10), for the actual two parity coefficient arrays, together with the
common-factor contribution. Counting every zero of $P$, or every
zero of $f$ in a half-plane, discards precisely the information now
shown to matter. The real-pencil theorem (5) is available as additional
structure, but a theorem converting it to this signed ray crossing
bound has not been proved.

This route remains auxiliary until such a ray-specific or mixed
Wronskian estimate is available. Ordinary CZDS and sector preservation
do not close the mixed zero bound and give no irrationality proof.
