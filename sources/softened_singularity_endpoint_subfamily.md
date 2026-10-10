> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The softened-singularity endpoint subfamily

## Scope and conclusion

This note studies one explicit, deliberately unbalanced family of endpoint-matched
linear forms in



$$
s=e+\pi.
$$



It does **not** prove either algebraicity or transcendence of $s$.  It proves
that the family fails in two substantial regimes: every fixed truncation degree
$b\geq2$, and every proportional ray $b/n\to\lambda$ with
$0<\lambda<2$, as well as every fixed-offset critical diagonal
$b=2n+d$.  It also records the exact tail and branch-point formulas that
remain available in the general threshold-and-beyond regimes.  The arithmetic
obstacle there is an upper bound for a gcd, not a missing numerical estimate.

All assertions below use



$$
F(z)=4\arctan\!\frac{z}{2-z},\qquad
 D(z)=z^2-2z+2,\qquad F(1)=\pi,\qquad D(1)=1.
$$



## 1. Construction and the exact integer form

Put



$$
h_n(z)=e^{-z}D(z)^nF(z)
       =\sum_{k\geq0}\eta_{n,k}\frac{z^k}{k!}
$$



and, for $b\geq0$,



$$
E_b=\sum_{k=0}^b\frac{(-1)^k}{k!},\qquad
 H_{n,b}=\sum_{k=0}^b\frac{\eta_{n,k}}{k!}.
$$



Take $C(z)=D(z)^n$, take $A$ constant, and choose the polynomial
$B$, of degree at most $b$, so that



$$
A+B(z)e^z+D(z)^nF(z)=O(z^{b+1}).                 \tag{1}
$$



After multiplication by $e^{-z}$, (1) gives the unique choice



$$
B(z)=-T_b\bigl(Ae^{-z}+h_n(z)\bigr),             \tag{2}
$$



where $T_b$ denotes Taylor truncation through degree $b$.  The endpoint
condition $B(1)=C(1)=1$ is therefore



$$
-AE_b-H_{n,b}=1.
$$



For $b\geq2$, $E_b\ne0$, and hence



$$
A=-\frac{1+H_{n,b}}{E_b}.                         \tag{3}
$$



The value at $z=1$ of the left side of (1) is $A+s$.  Multiplying it
by $b!E_b$ gives the integer-coefficient form



$$
\boxed{L_{n,b}=U_b s-V_{n,b}},\qquad
 U_b=b!E_b={!b},\qquad
 V_{n,b}=b!\bigl(1+H_{n,b}\bigr).                 \tag{4}
$$



Here $!b$ is the derangement number.  If



$$
g_{n,b}=\gcd(U_b,V_{n,b}),                        \tag{5}
$$



then the primitive form is $L_{n,b}/g_{n,b}$.

### Integrality of the coefficients

Let $f=e^{-z}F=\sum_{k\geq0}\eta_{0,k}z^k/k!$.  The differential
identity



$$
D(z)\bigl(f'(z)+f(z)\bigr)=4e^{-z}               \tag{6}
$$



gives, with negative-index terms interpreted as zero,



$$
2(\eta_{0,k+1}+\eta_{0,k})
 -2k(\eta_{0,k}+\eta_{0,k-1})
 +k(k-1)(\eta_{0,k-1}+\eta_{0,k-2})=4(-1)^k.      \tag{7}
$$



Starting with $\eta_{0,0}=0$, (7) gives $\eta_{0,1}=2$ and then
integers inductively: after solving for $\eta_{0,k+1}$, every term is
integral because $k(k-1)$ is even.  Multiplication by $D$ gives



$$
\eta_{n+1,k}=2\eta_{n,k}-2k\eta_{n,k-1}
                 +k(k-1)\eta_{n,k-2}.             \tag{8}
$$



Thus every $\eta_{n,k}$ is an integer, and (4) indeed has integer
coordinates.  The recurrences useful for exact computation are



$$
U_b=bU_{b-1}+(-1)^b,\qquad
 V_{n,b}=bV_{n,b-1}+\eta_{n,b},                   \tag{9}
$$



with $U_0=V_{n,0}=1$.

## 2. Exact tail identity

Set



$$
c=\frac{\pi}{e},\qquad
 \epsilon_b=e^{-1}-E_b,\qquad
 \rho_{n,b}=c-H_{n,b}.
$$



Since $e^{-1}s=1+c$, direct substitution in (4) gives



$$
\boxed{L_{n,b}=b!\bigl(\rho_{n,b}-s\epsilon_b\bigr).}       \tag{10}
$$



This identity is exact.  In particular, estimates for the two analytic
tails must still be combined with control of the arithmetic gcd (5).

There is also a useful Darboux form.  Define



$$
Q(z)=\frac{e^{-z}F(z)-c}{1-z}.                    \tag{11}
$$



The apparent singularity at $z=1$ is removable.  Because
$D(1)=1$, for every $b\geq2n$,



$$
\boxed{H_{n,b}=c+[z^b]D(z)^nQ(z),\qquad
 \rho_{n,b}=-[z^b]D(z)^nQ(z).}                    \tag{12}
$$



The remaining singularities of $Q$ nearest the origin are logarithmic
branch points at $1\pm i$; the factor $D^n$ softens each one to order
$n$, but does not remove the logarithm.

## 3. A complete fixed-$b$ obstruction

Write $D=2d$, where



$$
d(0)=1,\qquad d'(0)=-1,
$$



and note that $F(z)=2z+O(z^2)$.  For each fixed $k\geq1$, Leibniz's
rule shows that



$$
\eta_{n,k}=2^nP_k(n),                             \tag{13}
$$



where $P_k$ is a polynomial in $n$ of degree at most $k-1$.  The
only contribution to its leading term uses $F'(0)=2$ and differentiates
$d(z)^n$ exactly $k-1$ times.  Consequently



$$
P_k(n)=2k(-1)^{k-1}n^{k-1}+O_k(n^{k-2}).          \tag{14}
$$



It follows that, for fixed $b\geq2$,



$$
V_{n,b}=b!+2^nP_b^*(n),                           \tag{15}
$$



where $P_b^*$ has degree $b-1$ and leading coefficient
$2b(-1)^{b-1}$.  On the other hand $U_b={!b}\ne0$ is fixed and



$$
g_{n,b}\leq |U_b|.
$$



Therefore



$$
\left|\frac{L_{n,b}}{g_{n,b}}\right|
       \longrightarrow\infty
$$



at the order $2^nn^{b-1}$.  No fixed $b\geq2$ in this family can
produce small primitive linear forms.

For $b=2$ everything is explicit:



$$
\eta_{n,1}=2^{n+1},\qquad
 \eta_{n,2}=-2^{n+1}(2n+1),
$$





$$
U_2=1,\qquad
 V_{n,2}=2+2^{n+1}(1-2n),
$$



and hence



$$
\boxed{L_{n,2}=s-2+2^{n+1}(2n-1)>0.}              \tag{16}
$$



The gcd is identically one here.

## 4. Proportional degrees below the polynomial-degree threshold

The cumulative sum in (4) is a single coefficient:



$$
H_{n,b}=[z^b]\frac{e^{-z}D(z)^nF(z)}{1-z}.        \tag{17}
$$



Put $w=-z$ and define



$$
P(w)=w^2+2w+2,\qquad
 \mathcal A(w)=\frac{e^wF(-w)}{1+w}.
$$



Then



$$
H_{n,b}=(-1)^b[w^b]\mathcal A(w)P(w)^n.           \tag{18}
$$



Suppose $b/n\to\lambda$ with $0<\lambda<2$.  The positive saddle
$r=r(\lambda)$ is determined by



$$
\lambda=\frac{rP'(r)}{P(r)}
        =\frac{2r(r+1)}{r^2+2r+2},                 \tag{19}
$$



or explicitly



$$
r(\lambda)=
 \frac{\lambda-1+\sqrt{2-(\lambda-1)^2}}{2-\lambda}.
                                                                    \tag{20}
$$



The branch points lie on the saddle circle when $\lambda=1$, because
$r(1)=\sqrt2$.  This does not end the saddle range: their contribution
after multiplication by $P^n$ is exponentially smaller than the positive
saddle for every fixed $\lambda<2$.  The saddle variance is



$$
\sigma^2(r)=r\frac{d}{dr}\frac{rP'(r)}{P(r)}
 =\frac{2r(r^2+4r+2)}{(r^2+2r+2)^2}>0.             \tag{21}
$$



If $r_n$ is obtained from (19) with $b/n$ in place of $\lambda$,
the large-powers saddle calculation gives



$$
[w^b]\mathcal A(w)P(w)^n
 \sim
 \frac{\mathcal A(r_n)P(r_n)^nr_n^{-b}}
      {\sqrt{2\pi n\sigma^2(r_n)}}.               \tag{22}
$$



Here is a proof that the pole and the two logarithmic cuts do not alter the
leading saddle term.  Write $a_{n,b}=[w^b]\mathcal A(w)P(w)^n$, and let
$I_r$ denote the integral over the positively oriented circle $|w|=r$,
with the branches specified below.  The function $\mathcal A$ has a simple
pole at $w=-1$, with residue $c=\pi/e$.  If the expanded contour encloses
that pole but no cut, the coefficient relation, including its sign, is



$$
a_{n,b}=I_r-c(-1)^{b+1}.                           \tag{23}
$$



Indeed, the residue crossed by the contour is



$$
\operatorname{Res}_{w=-1}
 \frac{\mathcal A(w)P(w)^n}{w^{b+1}}
 =c(-1)^{b+1},
$$



because $P(-1)=1$.  This bounded residue is exponentially smaller than
the positive saddle.  At the isolated collision $r_n=1$
(equivalently $b/n=4/5$), shift the circular part of the contour by
$O(1/n)$ and indent around $-1$.  The indentation again contributes
(23) plus an exponentially smaller arc, because $|P(-1)|=1<P(1)=5$.

For the branch points, choose horizontal cuts



$$
w=-1-x\pm i,\qquad x\geq0.                         \tag{24}
$$



The logarithmic representation (38) below permits exactly these branch
choices, and the jump of $F(-w)$ across either cut is constant
(with magnitude $4\pi$).  Thus, apart from factors bounded for fixed
$\lambda$, the cut integrand has exponential part
$|P(w)|^n/|w|^b$.  More explicitly, when $\lambda$ stays in a compact
subinterval of $(0,2)$, the cut segments inside $|w|\leq r_n$ have
uniformly bounded length, $|e^w/(1+w)|$ is uniformly bounded on them,
and they stay a positive distance from $w=0$.  On (24), direct calculation
gives



$$
|w|^2=x^2+2x+2,
 \qquad |P(w)|^2=x^2(x^2+4),                        \tag{25}
$$



and



$$
|w|^4-|P(w)|^2
 =4(x^3+x^2+2x+1)>0.                               \tag{26}
$$



Hence $|P(w)|<|w|^2$.  On the part of either cut enclosed by the saddle
circle $|w|\leq r_n$,



$$
\frac{|P(w)|^n}{|w|^b}
 \leq r_n^{(2-b/n)n}.                               \tag{27}
$$



The main saddle has exponential size



$$
\frac{P(r_n)^n}{r_n^b}.
$$



The ratio of the bound in (27) to this size is at most



$$
\left(\frac{r_n^2}{P(r_n)}\right)^n,               \tag{28}
$$



which decays exponentially because $P(r)=r^2+2r+2>r^2$.  The endpoints
at $x=0$ cause no extra term: $P(w)^n$ vanishes there and dominates the
logarithm.  If $r_n=1$, or if a branch point lies on $|w|=r_n$, replace
the radius by $r_n(1+1/n)$, make the corresponding small indent, and then
let the indent shrink.  The radial displacement changes the saddle estimate
by a factor $1+o(1)$, because the first radial derivative of its phase
vanishes at $r_n$; the pole term stays bounded, and (28) still gives a
uniform exponential gap for the cut and indent pieces.  This proves (22)
throughout $0<\lambda<2$, uniformly when $\lambda$ stays in a compact
subinterval.

For completeness, $P$ has positive coefficients of span one, so on
$|w|=r$,



$$
|P(w)|<P(r)\quad(w\ne r).
$$



This gives exponential suppression off the unique saddle.  Also



$$
\mathcal A(r)=\frac{e^rF(-r)}{1+r}<0,
$$



so the leading constant in (22) is nonzero.  Finally,



$$
\Phi(\lambda)=\frac{P(r(\lambda))}{r(\lambda)^\lambda}>1.   \tag{29}
$$



Equations (18), (22), and (29) show that $|H_{n,b}|$ grows
exponentially on every such ray.

This analytic growth survives every possible gcd.  Indeed
$g_{n,b}\leq U_b$, while for $b\geq2$,



$$
\frac13\leq E_b\leq\frac12.
$$



Therefore



$$
\left|\frac{L_{n,b}}{g_{n,b}}\right|
 \geq\frac{|L_{n,b}|}{U_b}
 =\left|s-\frac{1+H_{n,b}}{E_b}\right|
\longrightarrow\infty.                          \tag{30}
$$



Thus every proportional ray $b/n\to\lambda\in(0,2)$, including the
initially tempting range $1/2\leq\lambda<2$, is rigorously eliminated.

### The critical diagonals $b=2n+d$

The boundary $b/n=2$ also admits a complete result when the offset $d$
is fixed.  Move the exponential into the large-power phase and write



$$
\mathcal B(w)=\frac{F(-w)}{1+w},\qquad
 H_{n,b}=(-1)^b[w^b]\mathcal B(w)e^wP(w)^n.         \tag{31}
$$



For $b=2n+d$, the positive saddle $r_n$ is the unique solution of



$$
2n+d=r_n+n\frac{r_nP'(r_n)}{P(r_n)}.              \tag{32}
$$



Let $R=\sqrt{2n}$.  From



$$
\frac{rP'(r)}{P(r)}=2-\frac2r+O(r^{-3}),
 \qquad
 \sigma^2(r)=\frac2r+O(r^{-3}),
$$



equation (32) gives



$$
r_n=R+\frac d2+O(R^{-1}),\qquad
 r_n+n\sigma^2(r_n)=2R+O(1).                      \tag{33}
$$



The saddle estimate with the now varying radius is



$$
[w^{2n+d}]\mathcal B(w)e^wP(w)^n
 \sim
 \frac{\mathcal B(r_n)e^{r_n}P(r_n)^nr_n^{-2n-d}}
      {\sqrt{2\pi\bigl(r_n+n\sigma^2(r_n)\bigr)}}. \tag{34}
$$



For clarity, the usual local proof remains uniform here.  The angular
variance in (34) is $2R+O(1)$; every fixed higher angular cumulant of
$e^wP(w)^n$ is $O(R)$, so after scaling the central arc by
$R^{-1/2}$, the cubic and higher terms are $o(1)$.  Positivity and span
one suppress the remaining circular arcs.  The pole contribution is
bounded.  On either horizontal cut, $|P(w)|<|w|^2$ now gives



$$
\frac{|P(w)|^n}{|w|^{2n+d}}<|w|^{-d},
$$



while $|e^w|=e^{-1-x}$.  Thus the entire cut contribution is at most
polynomial in $R$, and is negligible compared with the main term below.

Finally,



$$
\mathcal B(r)=-\frac{\pi}{r}\bigl(1+O(r^{-1})\bigr),
$$



and



$$
e^{r_n}P(r_n)^nr_n^{-2n-d}
 =e^{2R}R^{-d}(1+o(1)).
$$



Substitution in (34) yields the explicit nonzero asymptotic



$$
\boxed{
 H_{n,2n+d}\sim
 (-1)^{d+1}\frac{\sqrt\pi}{2}
 e^{2\sqrt{2n}}(\sqrt{2n})^{-d-3/2}.}              \tag{35}
$$



In particular, $|H_{n,2n+d}|\to\infty$ for every fixed integer $d$.
The gcd-independent bound (30) therefore eliminates every fixed-offset
critical diagonal as well.

The same calculation gives a nontrivial growing window above the critical
diagonal.  Let $d=d_n\geq0$, let $R=\sqrt{2n}$, assume $d=o(R)$,
and restrict to a range in which the saddle term below tends to infinity
(so it dominates the bounded pole term).  Solving (32) one order more
accurately and expanding its phase gives



$$
r_n=R+\frac d2+O\!\left(\frac{d^2+1}{R}\right),
$$



and



$$
\log|H_{n,2n+d}|
 =2R-d\log R-\frac{d^2}{4R}-\frac32\log R
  +O\!\left(1+\frac{d^3}{R^2}\right).             \tag{36}
$$



The saddle proof above is uniform here: $r_n\asymp R$, its variance is
$\asymp R$, and for $d\geq0$ the cut bound $|w|^{-d}$ is uniformly
integrable after multiplication by $e^{-1-x}$.  In particular, suppose
that, for some fixed $0<\delta<2$,



$$
0\leq b-2n\leq
 (2-\delta)\frac{\sqrt{2n}}{\log\sqrt{2n}}          \tag{37}
$$



holds.  Then the right side of (36) is at least
$\delta\sqrt{2n}+o(\sqrt n)$.  Hence the saddle tends to infinity and
(36) applies uniformly in this window.  The entire window is therefore
eliminated by (30), independently of the gcd.

## 5. Exact branch-point coefficient formula

Let



$$
\alpha=\frac{1+i}{2}.
$$



The logarithmic representation



$$
F(z)=-2i\bigl(\log(1-\bar\alpha z)-\log(1-\alpha z)\bigr)   \tag{38}
$$



and the beta integral give, for every integer $k>2n$,



$$
\boxed{
 [z^k]D(z)^nF(z)
 =(-1)^n2^{n+2}\operatorname{Im}\!\left[
 \alpha^k\int_0^1
 t^{k-2n-1}(1-t)^n(t+i)^n\,dt
 \right].}                                          \tag{39}
$$



To verify (39), use, for $m>n$,



$$
[z^m](1-az)^n\log(1-az)
 =\frac{(-1)^{n-1}n!a^m}{m(m-1)\cdots(m-n)},        \tag{40}
$$



and



$$
\frac{n!}{m(m-1)\cdots(m-n)}
 =\int_0^1t^{m-n-1}(1-t)^n\,dt.                     \tag{41}
$$



Formula (39) was also checked by exact symbolic expansion for
$0\leq n\leq4$ and several successive $k>2n$.  It exposes the
oscillatory factor that a transition analysis at and beyond the
polynomial-degree threshold $b/n=2$ must control.

## 6. What remains unresolved in this family

At $b/n=2$, the fixed-radius saddle of (19) escapes to infinity.  The
fixed-offset transition and a growing window were handled in (31)--(37),
but general approaches
to the threshold beyond the window (37) remain open; for $b/n>2$, there
is no finite positive saddle for the quadratic power $P^n$.  Equations
(10), (12), and (39) provide exact starting points for a broader transition
analysis.  Such an analysis can
estimate the **raw** real number $L_{n,b}$, but it does not by itself
estimate the primitive form: one also needs a uniform upper bound for



$$
g_{n,b}=\gcd({!b},V_{n,b}).                        \tag{42}
$$



No such bound strong enough for the threshold-and-beyond range is proved
here.  Finite exact computations show small gcds and growing primitive
forms, but those observations are not an all-degree theorem and must not
be substituted for the missing bound (42).

## 7. Reproducible finite check

The companion exact script
`scripts/softened_singularity_endpoint_probe.py` computes (7)--(9), uses
directed rational bounds for $e+\pi$, and certifies the following finite
statement:

* for every $2\leq n\leq60$, among $2\leq b\leq4n$, the smallest
  primitive absolute value occurs at $b=2$;
* this is a finite certificate only; (16) proves divergence at fixed
  $b=2$, not global optimality for all $n$ and $b$;
* when the search is restricted to
  $b\geq\max(2,\lceil n/2\rceil)$, its minimum lies at that lower
  boundary for every $2\leq n\leq60$, in agreement with the saddle
  obstruction (30).

The machine-readable summary is
`results/softened_singularity_endpoint_n60.json`.
