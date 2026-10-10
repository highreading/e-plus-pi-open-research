> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root-of-unity constrained Hermite--Padé forms

## Exact reduction, the tangent-number content barrier, and the Lambert diagonal

Checked: 2026-08-27 UTC

## 1. Scope and conclusion

Assume temporarily that



$$
s=e+\pi\in\overline{\mathbb Q}.          \tag{1}
$$



The point



$$
z_0=i\pi=i(s-e),\qquad e^{z_0}=-1              \tag{2}
$$



suggests a modification of the multi-exponential type-I construction.  We
seek



$$
R(z)=\sum_{j=0}^{m}A_j(z)e^{jz},\qquad \deg A_j\leq n,           \tag{3}
$$



with a large zero at the origin, while requiring



$$
S(z):=\sum_{j=0}^{m}(-1)^jA_j(z),\qquad \deg S\leq D.\tag{4}
$$



Then



$$
R(i\pi)=S(i\pi)=S\bigl(i(s-e)\bigr),                            \tag{5}
$$



so, under (1), the endpoint is a polynomial in $e$, of degree at most
$D$, over the fixed number field $\mathbb Q(s,i)$.  This repairs the
two-transcendental-generator defect in the unconstrained nested
Hermite--Padé construction.

The repair is exact, but it does not currently prove (1) false.  The main
findings are as follows.

1. The constrained coefficient space has dimension

   

$$
V=m(n+1)+D+1.                                      \tag{6}
$$



   Dimension counting therefore supplies a form of order at least

   

$$
L=V-1=m(n+1)+D.                                    \tag{7}
$$



   An exact integer matrix and a much smaller annihilator matrix are given
   below.  Exact computation for
   $1\leq m\leq4$, $1\leq n\leq8$, and
   $0\leq D\leq\min(4,n)$ proves rank $V-1$ in every case.  The unique
   form has one extra order precisely when $m,n$ are odd and $D$ is even.
   This parity formula is a proved theorem for $m=1$; for arbitrary $m$
   it is, at present, an exact finite certificate and a well-supported
   normality conjecture, not a theorem.

2. For $m=1$, the problem is exactly Padé approximation to

   

$$
f(z)=\frac1{1+e^z}.                         \tag{8}
$$



   All ranks, the parity defect, and the fixed-$D$ endpoint asymptotic can
   be proved for every $n,D$.  If $d=\lfloor D/2\rfloor\geq1$, and
   $C_{n,D}$ is the primitive endpoint polynomial, then, for fixed $D$,

   

$$
\boxed{
     \frac{|C_{n,D}(i\pi)|}{H(C_{n,D})}
       =\Theta_D\bigl((2d+1)^{-n}\bigr).}                         \tag{9}
$$



   The apparent convergence to the first poles is real, but only exponential
   relative to the primitive endpoint height.

3. The case $D=1$ is trivial: $C_{n,1}$ is $1$ or $z$.  The first
   nontrivial case $D=2$ has the exact primitive form

   

$$
C_{n,2}(z)=P_r+Q_rz^2,qquad
                n\in\{2r-1,2r\},                                \tag{10}
$$



   where

   

$$
\frac{P_r}{Q_r}
      =\frac{8r(2r+1)\tau_r}{\tau_{r+1}}
   \quad\hbox{in lowest terms}                                  \tag{11}
$$



   and $\tau_r$ is the positive tangent number of index $2r-1$.
   Thus

   

$$
Q_r=\frac{\tau_{r+1}}
      {\gcd\!\bigl(\tau_{r+1},8r(2r+1)\tau_r\bigr)},            \tag{12}
$$



   and

   

$$
|C_{n,2}(i\pi)|
        =\left(\frac{8\pi^2}{9}+o(1)\right)Q_r9^{-r}.            \tag{13}
$$



   Equation (12), not the much larger content of the full auxiliary vector,
   is the exact arithmetic bottleneck.  The data show factorial-size $Q_r$,
   but no sufficiently strong general upper bound for the gcd in (12) is
   proved here.

4. On the diagonal $D=n$, the same construction is the Lambert continued
   fraction/diagonal Padé construction for $\tanh(z/2)$.  Here the primitive
   endpoint value really tends to zero superfactorially:

   

$$
\log H(C_{n,n})=n\log n+O(n),\qquad
       \log|C_{n,n}(i\pi)|=-n\log n+O(n).                         \tag{14}
$$



   The pole convergence survives exact integer clearing.  However the degree
   of the resulting polynomial in $e$ is now $n$.  Available
   transcendence measures for $e$ lose a factor growing at least linearly
   in that degree, so (14) is far from a contradiction.

Consequently this route gives a genuine new local construction and a clean
arithmetic target, but no proof that $e+\pi$ is or is not transcendental.

The replayable files are

* `scripts/root_unity_low_degree_hp_certificate.py`;
* `results/root_unity_low_degree_hp_certificate.json`.

## 2. The exact integer jet matrix

Write



$$
A_j(z)=\sum_{r=0}^{n}a_{j,r}z^r.              \tag{15}
$$



For $k\geq0$,



$$
\left.\frac{d^k}{dz^k}\bigl(z^re^{jz}\bigr)\right|_{z=0}
   =
   \begin{cases}
    (k)_rj^{k-r},&r\leq k,\\
    0,&r>k,
   \end{cases}                                                   \tag{16}
$$



where $(k)_r=k!/(k-r)!$.  Hence the vanishing conditions are rows



$$
J_{k,(j,r)}=(k)_rj^{k-r}.                                 \tag{17}
$$



The low-degree endpoint condition contributes, for $D<r\leq n$, the rows



$$
E_{r,(j,q)}=(-1)^j\mathbf 1_{q=r}.                         \tag{18}
$$



All entries in (17)--(18) are integers.  There are



$$
U=(m+1)(n+1)                                                     \tag{19}
$$



columns and $n-D$ independent endpoint rows.  Therefore the constrained
space has the dimension (6).  The first $L=V-1$ jet rows together with
(18) form an $(U-1)$-by-$U$ integer matrix.  Its maximal minors give an
exact primitive integer form whenever its rank is $U-1$.

The certificate constructs this matrix, computes its rational nullspace,
divides the full coefficient content, and then divides the endpoint content
again.  That last division is essential: a transcendence measure applied to
(5) sees only the primitive height of $S$, not the height of the auxiliary
vector $(A_0,\ldots,A_m)$.

The exact grid contains 136 triples.  Every combined matrix has rank $U-1$,
and the restricted jet rank is $L$.  Adding the next jet row fails to raise
the rank exactly for



$$
m\equiv n\equiv1\pmod2,qquad D\equiv0\pmod2. \tag{20}
$$



No finite rank calculation is used below to prove the all-$n$, $m=1$
statements.

## 3. Division by $1+e^z$ and the small annihilator matrix

Set



$$
P(z,y)=\sum_{j=0}^{m}A_j(z)y^j.                 \tag{21}
$$



Polynomial division in $y$ gives uniquely



$$
P(z,y)=S(z)+(y+1)T(z,y),\qquad \deg_yT\leq m-1.     \tag{22}
$$



Consequently



$$
R(z)=S(z)+(1+e^z)B(z),
 \qquad B(z):=T(z,e^z)
       \in\sum_{j=0}^{m-1}\mathbb Q[z]_{\leq n}e^{jz}.           \tag{23}
$$



With $f$ as in (8), (23) is equivalent near the origin to



$$
B(z)+S(z)f(z)=O(z^L).                       \tag{24}
$$



Put



$$
\Phi_{m,n}(X)=\prod_{j=0}^{m-1}(X-j)^{n+1},\qquad
 M=\deg\Phi_{m,n}=m(n+1).                                       \tag{25}
$$



The differential operator $\Phi_{m,n}(d/dz)$ annihilates $B$.  The
ordinary Hermite interpolation problem in the $M$-dimensional exponential
polynomial space in (23) is normal.  Matching the first $M$ jets is always
possible and unique.  Induction on the subsequent Taylor coefficients then
shows that (24), with $L=M+D$, is equivalent to the $D$ equations



$$
\left.
 \frac{d^q}{dz^q}
 \Phi_{m,n}\!\left(\frac d{dz}\right)(S(z)f(z))
 \right|_{z=0}=0,qquad 0\leq q<D.                              \tag{26}
$$



Thus the endpoint polynomial can be obtained from a $D$-by-$(D+1)$
matrix even when the original auxiliary system is large.

For an exact algebraic form of this matrix, define the rational functional



$$
\mathcal L(Q):=Q\!\left(\frac d{dz}\right)f(z)\big|_{z=0}.
                                                                    \tag{27}
$$



Since $[Q(d/dz),z]=Q'(d/dz)$, the entry in row $q$, column $a$
of (26) is



$$
\mathcal L\!\left(
                 \bigl(X^q\Phi_{m,n}(X)\bigr)^{(a)}
                              \right),
       \quad 0\leq q<D,\quad0\leq a\leq D.                    \tag{28}
$$



The generating function of this functional is



$$
\mathcal L(e^{tX})=\frac1{1+e^t}.              \tag{29}
$$



Two useful exact symmetries follow:



$$
\mathcal L(Q(X)+Q(X+1))=Q(0),
 \qquad
 \mathcal L(Q(-X-1))=\mathcal L(Q(X)).                           \tag{30}
$$



These identities explain the parity effects in the exact grid.  They also
give, for $D=1$, the observed constant/monomial split.  A complete
all-$m$ nonvanishing proof for every determinant in (28) remains a missing
normality lemma; it is not silently inferred from the computations.

The endpoint cannot vanish identically.  Indeed, if $S=0$, then (23) says
that $R=(1+e^z)B$.  Because $1+e^z$ is nonzero at the origin, the standard
zero estimate for an $M$-dimensional exponential-polynomial space gives
$\operatorname{ord}_0R\leq M-1$, whereas (7) gives $L\geq M$.

## 4. Complete solution for $m=1$

For $m=1$, write



$$
R(z)=C(z)+B(z)(1+e^z),                     \tag{31}
$$



where $C=S=A_0-A_1$, $\deg C\leq D$, and $\deg B\leq n$.
Then



$$
B(z)+C(z)f(z)=O(z^{n+D+1}).                \tag{32}
$$



Thus $-B/C$ is the $[n/D]$ Padé approximant to $f$, allowing the
usual parity defect.

### 4.1 The moment sequence

Let $\tau_r$ be defined by



$$
\tan z=\sum_{r\geq1}\tau_r\frac{z^{2r-1}}{(2r-1)!}.
                                                                    \tag{33}
$$



Since



$$
\frac1{1+e^z}=\frac12-\frac12\tanh(z/2),                        \tag{34}
$$



we have the exact Taylor expansion



$$
f(z)=\frac12+\sum_{r\geq1}(-1)^ru_rz^{2r-1},                    \tag{35}
$$



where



$$
\begin{aligned}
 u_r
 &=\frac{\tau_r}{2^{2r}(2r-1)!}
   =\frac{(2^{2r}-1)|B_{2r}|}{(2r)!}\\
 &=\frac2{\pi^{2r}}
      \sum_{\ell=0}^{\infty}\frac1{(2\ell+1)^{2r}}.
 \end{aligned}                                                    \tag{36}
$$



Put



$$
x_\ell=\frac1{\pi^2(2\ell+1)^2}.               \tag{37}
$$



Then $u_r=2\sum_{\ell\geq0}x_\ell^r$.  Every shifted Hankel matrix of
these moments is positive definite: for a nonzero vector $v$,



$$
\sum_{a,b=0}^{d-1}v_av_bu_{R+a+b}
  =2\sum_{\ell\geq0}x_\ell^R
       \left(\sum_{a=0}^{d-1}v_ax_\ell^a\right)^2>0.             \tag{38}
$$



### 4.2 Exact ranks and parity

Write $C(z)=\sum_{a=0}^{D}c_az^a$.  Equation (32) first determines $B$
by truncation.  The remaining conditions are exactly



$$
\sum_{a=0}^{D}c_a[z^{k-a}]f(z)=0,
             \qquad n+1\leq k\leq n+D.                          \tag{39}
$$



For $n\geq D$, no constant Taylor coefficient occurs in this block.
Because all positive even coefficients of $f$ vanish, (39) splits into two
parity blocks.  After reversing columns, every square block is a shifted
Hankel matrix from (38), times nonzero row and column signs.  It is therefore
invertible.

It follows that the nullspace is one-dimensional.  More precisely:

* if $D$ is even, $C$ is even;
* if $D$ is odd, $C$ has parity $n+1\pmod2$.

The first coefficient after the block (39) vanishes automatically exactly
when $n$ is odd and $D$ is even.  Positivity of the next enlarged Hankel
minor shows that there is no further defect.  Therefore



$$
\boxed{
 \operatorname{ord}_0R=
 \begin{cases}
 n+D+2,&n\text{ odd and }D\text{ even},\\
 n+D+1,&\text{otherwise}.
 \end{cases}}                                                     \tag{40}
$$



This proves the $m=1$ part of the parity pattern (20) for all $n,D$.

For $D=1$, (39) immediately gives



$$
C_{n,1}(z)=
                \begin{cases}
                  1,&n\text{ odd},\\
                  z,&n\text{ even},
                \end{cases}                                      \tag{41}
$$



up to a nonzero rational scalar.  This is the exact $D=1$ triviality.

### 4.3 Fixed degree and the first omitted pole

Let $d=\lfloor D/2\rfloor\geq1$.  After removing the forced parity, the
nontrivial part of (39) is the orthogonality system for a degree-$d$
polynomial against $d$ consecutive shifted moments $u_r$.  Reversing the
coefficient order gives a polynomial $Q_{R,d}(x)$ orthogonal with respect
to the discrete positive measure



$$
2\sum_{\ell\geq0}\delta_{x_\ell},             \tag{42}
$$



with an additional factor $x^R$, where $2R=n+O_D(1)$.

The Cauchy--Binet expansion of the associated Hankel determinant is



$$
2^d\sum_{0\leq\ell_1<\cdots<\ell_d}
  (x_{\ell_1}\cdots x_{\ell_d})^R
  \prod_{a<b}(x_{\ell_a}-x_{\ell_b})^2                         \tag{43}
$$



times a fixed harmless shifted monomial factor.  All summands are positive.
The coefficient determinant is dominated by the subset
$\{0,1,\ldots,d-1\}$.  At $x=x_0=\pi^{-2}$, all subsets containing
zero cancel because the limiting polynomial has a root there; the leading
surviving subset is $\{1,2,\ldots,d\}$.  The ratio of their exponential
weights is



$$
\left(\frac{x_1\cdots x_d}{x_0\cdots x_{d-1}}\right)^R
     =\left(\frac{x_d}{x_0}\right)^R
     =(2d+1)^{-2R}.                                               \tag{44}
$$



The remaining subsets are bounded by convergent geometric tails uniformly
for fixed $d$.  Coefficient ratios converge to those of
$\prod_{j=0}^{d-1}(x-x_j)$, so their house stays comparable to a nonzero
constant under any fixed normalization.  Translating back from $x$ to
$z^2$, and observing that a forced factor $z$ changes the endpoint by
only $\pi$, proves (9).

Equation (9) is invariant under rational rescaling and therefore already
includes every possible gcd removed in making $C_{n,D}$ primitive.

## 5. The exact $D=2$ tangent-number gcd

Let $n\in\{2r-1,2r\}$.  Equations (35) and (39) give, up to scale,



$$
C(z)=u_r+u_{r+1}z^2.                     \tag{45}
$$



Write $u_r/u_{r+1}=P_r/Q_r$ in lowest terms.  The standard tangent-number
formula in (36) yields



$$
\frac{u_r}{u_{r+1}}
   =8r(2r+1)\frac{\tau_r}{\tau_{r+1}},                            \tag{46}
$$



which proves (10)--(12).

There is also an exact positive expression for the error:



$$
\begin{aligned}
 u_r-\pi^2u_{r+1}
   &=\frac2{\pi^{2r}}
     \sum_{\substack{k\geq3\\k\text{ odd}}}
       \left(k^{-2r}-k^{-2r-2}\right)>0,                         \tag{47}\\
 \frac{u_r}{u_{r+1}}-\pi^2
   &=\left(\frac{8\pi^2}{9}+o(1)\right)9^{-r}.                  \tag{48}
 \end{aligned}
$$



Thus (13) follows exactly after primitive clearing.

The certificate computes (12) for $1\leq r\leq180$.  It also checks a
tempting but false simplification: consecutive tangent numbers do not always
have only a power of two in common.  The first nontrivial odd common factors
in this range are



$$
587\quad(r=45),\qquad 491\quad(r=168).                     \tag{49}
$$



The sufficient no-go estimate



$$
\log\gcd\!\bigl(\tau_{r+1},8r(2r+1)\tau_r\bigr)=o(r\log r)      \tag{50}
$$



would imply $\log Q_r\sim\log\tau_{r+1}\sim2r\log r$, so the
primitive endpoint in (13) would grow rather than shrink.  The data strongly
have this behavior, but (50) is not proved here.  Conversely, a proof-producing
subsequence would require extraordinarily large cancellation in (12), not
merely better clearing of the auxiliary $A_j$'s.

## 6. The growing-degree Lambert diagonal

The fixed-$D$ result does not describe the diagonal $D=n$.  Here (31) is
the ordinary diagonal Padé construction for $e^z$.  Define the integer
reverse-Bessel polynomial



$$
\Theta_n(z)=\sum_{k=0}^{n}
          \frac{(2n-k)!}{k!(n-k)!}z^k.                            \tag{51}
$$



The exact Padé remainder is



$$
e^z\Theta_n(-z)-\Theta_n(z)
   =\frac{(-1)^nz^{2n+1}}{n!}
       \int_0^1e^{tz}t^n(1-t)^n\,dt.                             \tag{52}
$$



Thus one may take $B=\Theta_n(-z)$, $A_0=-\Theta_n(z)$, and the endpoint
polynomial is, up to sign, the even part



$$
\Theta_n(z)+\Theta_n(-z)
  =2\sum_{j=0}^{\lfloor n/2\rfloor}
       b_{n,j}z^{2j},qquad
 b_{n,j}=\frac{(2n-2j)!}{(2j)!(n-2j)!}.                           \tag{53}
$$



The exact content of the $b_{n,j}$'s is



$$
g_n:=\gcd_j b_{n,j}
   =\begin{cases}
      1,&n\text{ even},\\
      n(n+1),&n\text{ odd}.
     \end{cases}                                                  \tag{54}
$$



This follows directly from Legendre's formula prime by prime; the last
coefficient gives the reverse divisibility in the odd case.  The certificate
checks (54) exactly through $n=30$.  Hence the primitive endpoint is



$$
C_{n,n}(z)=\frac1{g_n}
                    \sum_jb_{n,j}z^{2j}.                          \tag{55}
$$



The coefficients in (53) decrease with $j$, so



$$
H(C_{n,n})=\frac{(2n)!}{g_nn!}.                                 \tag{56}
$$



At $z=i\pi$, equation (52) and $e^{i\pi}=-1$ give the exact positive
magnitude



$$
|C_{n,n}(i\pi)|
  =\frac{\pi^{2n+1}}{2g_nn!}
    \int_0^1\cos\!\bigl(\pi(t-\tfrac12)\bigr)
                 t^n(1-t)^n\,dt.                                \tag{57}
$$



There is no hidden phase cancellation: the cosine is nonnegative on
$[0,1]$.  Under the beta probability measure with density proportional to
$t^n(1-t)^n$, $t$ converges in probability to $1/2$.  Therefore



$$
\int_0^1\cos\!\bigl(\pi(t-\tfrac12)\bigr)t^n(1-t)^n\,dt
   =(1+o(1))\frac{n!^2}{(2n+1)!}.                                \tag{58}
$$



Stirling's formula in (56)--(58) proves (14).

Finally,



$$
\frac{\Theta_n(z)-\Theta_n(-z)}
      {\Theta_n(z)+\Theta_n(-z)}                                 \tag{59}
$$



is the corresponding staircase Padé approximant to $\tanh(z/2)$; its
continued fraction is Lambert's



$$
\tanh x=\cfrac{x}{1+\cfrac{x^2}{3+\cfrac{x^2}{5+\ddots}}}.      \tag{60}
$$



Thus (57) is exactly the primitive integer denominator of the Lambert
convergent evaluated at its first pole.  Pole convergence absolutely survives
factorial clearing.  What fails is the Diophantine comparison: after (1),
equation (55) becomes a polynomial in $e$ of degree $n$, while its small
value has only exponent $1+o(1)$ relative to its own height.  The known
lower bounds for a degree-$n$ polynomial at $e$ permit an exponent growing
at least linearly with $n$, and hence are much weaker.

Intermediate regimes $D=D(n)$ interpolate between (9) and (14).  The
Lambert diagonal is already the most favorable exact pole-convergence example
found in this family; allowing $D$ to grow pays the same growing polynomial
degree in the measure for $e$.

## 7. The conditional polynomial in $e$

Let $C\in\mathbb Z[z]$ be a primitive endpoint polynomial of degree at most
$D$.  Choose a positive integer $\delta$ such that $\delta s$ is an
algebraic integer.  Under (1),



$$
P_C(X)=\delta^D C\bigl(i(s-X)\bigr)
            \in\mathcal O_{\mathbb Q(s,i)}[X],                   \tag{61}
$$



and



$$
P_C(e)=\delta^D C(i\pi).                   \tag{62}
$$



For fixed $s,D$, the coefficient house of $P_C$ is comparable, up to a
fixed factor, with $H(C)$.  A nonzero polynomial in $e$ over an algebraic
number field has an explicit lower bound polynomial in this height when the
degree is fixed.  Combining that lower bound with (9) yields a precise
criterion: for fixed $D\geq2$, a contradiction would require endpoint
heights growing slowly enough that the exponential factor
$(2\lfloor D/2\rfloor+1)^{-n}$ beats the relevant fixed-degree height
exponent.

The companion audit
`sources/root_of_unity_low_degree_polynomial_e_measure.md` records the exact
number-field measure and exponent.  In particular, subexponential primitive
endpoint height would be a strong sufficient condition.  Formula (12) shows
that even this sufficient condition becomes a difficult tangent-number gcd
statement already at $D=2$, while the exact computations exhibit
superexponential rather than subexponential height.

For $D=n$, (14) gives a genuinely small primitive endpoint, but (61) has
degree $n$; the growing-degree lower bound is far too weak.  Fixed degree and
growing degree therefore fail for different, explicitly separated reasons.

## 8. What is proved and what remains open

The following statements are rigorous.

* The division identity (22)--(24), the annihilator criterion (26)--(28), and
  the integer jet matrix (17)--(18).
* Every $m=1$ rank and parity assertion, including (40) and the $D=1$
  collapse.
* The fixed-$D$, $m=1$ asymptotic (9), by the positive discrete moment
  determinant.
* The exact tangent-number formula (10)--(13), including the complete gcd
  normalization.
* The diagonal Lambert formulas (51)--(58), their exact content, and the
  height/value scale (14).
* The 136 exact general-$m$ rank calculations and all integer data stored in
  the certificate.

The following are not proved.

* General-$m$ normality and the parity pattern (20) outside the certified
  grid.
* A useful asymptotic bound for the primitive endpoint content for fixed
  $m>1$.
* The tangent-number gcd bound (50), or any opposite large-gcd theorem that
  would create unusually small endpoint height.
* Any contradiction to (1), and therefore any conclusion about the
  transcendence of $e+\pi$.

The sharpest surviving local target from this audit is arithmetic, not
analytic: control the primitive content of the low-degree endpoint polynomial
itself.  Improving only the auxiliary Hermite--Padé clearing cannot affect
the number-field polynomial in (61).
