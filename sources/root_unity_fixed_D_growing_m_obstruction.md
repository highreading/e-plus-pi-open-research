> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fixed endpoint degree with a growing number of exponentials

## An all-parameter $D=2$ construction, its multiset-Eulerian denominator,
## and a fixed-degree obstruction

Checked: 2026-08-27 UTC

## 1. Verdict

Continue to assume, only to test the proposed route, that



$$
s=e+\pi\in\overline{\mathbb Q}.          \tag{1}
$$



The constrained root-of-unity construction has



$$
R(z)=\sum_{j=0}^{m}A_j(z)e^{jz}
     =S(z)+(1+e^z)B(z),\qquad R(i\pi)=S(i\pi).                  \tag{2}
$$



The previous audit solved fixed $m=1$ and left open the possibility that
letting $m$ grow while keeping $\deg S=D$ fixed might give an endpoint
approximation exponent tending to infinity.  The conclusions of the present
audit are:

1. For $D=2$, every $m\geq1$ and $n\geq2$ admit a canonical nonzero
   even endpoint polynomial.  Put

   

$$
\Phi_{m,n}(X)=\prod_{j=0}^{m-1}(X-j)^{n+1},\qquad
    \varepsilon\equiv mn\pmod2,\qquad
    \Psi_{m,n}(X)=X^\varepsilon\Phi_{m,n}(X).                    \tag{3}
$$



   If

   

$$
\mathcal L(Q)=Q(d/dz)\frac1{1+e^z}\bigg|_{z=0},           \tag{4}
$$



   then the endpoint is, up to rational scale,

   

$$
\boxed{
       S_{m,n}(z)=-\mathcal L(\Psi_{m,n}'')
                  +\mathcal L(\Psi_{m,n})z^2.}                  \tag{5}
$$



   In particular,

   

$$
\rho_{m,n}:=\frac{[z^0]S_{m,n}}{[z^2]S_{m,n}}
       =-\frac{\mathcal L(\Psi_{m,n}'')}
                    {\mathcal L(\Psi_{m,n})}\in\mathbb Q.      \tag{6}
$$



   The denominator in (6) never vanishes.  This is not inferred from a
   finite rank grid: it follows from MacMahon's identity and Simion's theorem
   that multiset Eulerian polynomials have simple negative roots.

2. Formula (6) has an exact pole representation.  The two nearest poles
   $\pm i\pi$ cancel identically from $\rho_{m,n}-\pi^2$, and the next
   poles $\pm3i\pi$ control the observed convergence.  Exact data show
   exponential decay in $M=m(n+1)$; on the diagonal $m=n$, the measured
   quantity $-M^{-1}\log|\rho_{m,n}-\pi^2|$ rises from about $0.80$ at
   $m=n=4$ to about $1.06$ at $m=n=12$, toward the nearest/next-pole
   value $\log3$.  This is a diagnostic, not a proved two-parameter
   asymptotic.  A uniform lower bound preventing cancellation in the
   complex saddle integral remains open.

3. The primitive endpoint content cannot rescue the fixed-degree route.
   If

   

$$
C_{m,n}(z)=P_{m,n}+Q_{m,n}z^2             \tag{7}
$$



   is the primitive integer scaling of (5), with $Q_{m,n}>0$, then

   

$$
\frac{|C_{m,n}(i\pi)|}{H(C_{m,n})}
       =\frac{Q_{m,n}}{\max(|P_{m,n}|,Q_{m,n})}
          |\rho_{m,n}-\pi^2|.                                   \tag{8}
$$



   Thus (8) tracks the endpoint-only content exactly.  More decisively, for
   every fixed $D$ there is a finite constant $K_\pi(D)$ such that every
   primitive $C\in\mathbb Z[z]\setminus\{0\}$, $\deg C\leq D$, satisfies

   

$$
|C(i\pi)|\gg_D H(C)^{-K_\pi(D)}.           \tag{9}
$$



   This follows from a fixed-degree algebraic approximation measure for
   $\pi$.  Hence no sequence of fixed-degree endpoint polynomials can have
   an unbounded small-value exponent relative to its own primitive height,
   regardless of how $m,n$, auxiliary denominators, or endpoint gcds are
   chosen.

4. Under (1), the companion $e$-measure has height exponent

   

$$
E(r,D)=r^2D+r-1,
       \qquad r=[\mathbb Q(s):\mathbb Q].                        \tag{10}
$$



   Since $E(r,D)\to\infty$ with the unknown algebraic degree $r$, while
   (9) bounds every fixed-$D$ endpoint exponent independently of $m,n$,
   growing $m$ at fixed $D$ cannot beat every possible algebraic degree.
   This is a rigorous obstruction to the proposed one-polynomial comparison,
   not a proof about $e+\pi$ and not a no-go theorem for determinants using
   several independent endpoints.

   The quantifiers matter.  For a specified algebraic degree $r$ and a
   specified $D$, (9) does not decide whether an achieved finite endpoint
   exponent might exceed $E(r,D)$.  Nor does it compare the
   $D$-dependence of $K_\pi(D)$ with $r^2D$ when $D$ grows.  What it
   rules out is precisely the proposed fixed-$D$ strategy of forcing the
   endpoint exponent to infinity merely by sending $m,n$ to infinity.

The replayable certificate is

* `scripts/root_unity_D2_growing_m_certificate.py`;
* `results/root_unity_D2_growing_m_certificate.json`.

## 2. The $D=2$ endpoint matrix

Write



$$
f(z)=\frac1{1+e^z},\qquad q=n+1,\qquad M=mq.                    \tag{11}
$$



As proved in the base audit, matching the first $M$ jets determines
$B$ uniquely in



$$
\sum_{j=0}^{m-1}\mathbb Q[z]_{\leq n}e^{jz}.      \tag{12}
$$



The two additional conditions needed for order at least $M+2$ are



$$
\sum_{a=0}^2s_a\mathcal L(\Phi_{m,n}^{(a)})=0,
 \qquad
 \sum_{a=0}^2s_a\mathcal L((X\Phi_{m,n})^{(a)})=0.              \tag{13}
$$



Equivalently, $(s_0,s_1,s_2)^T$ lies in the kernel of



$$
K_{m,n}=
 \begin{pmatrix}
  \mathcal L(\Phi)&\mathcal L(\Phi')&\mathcal L(\Phi'')\\
  \mathcal L(X\Phi)&\mathcal L((X\Phi)')&
                         \mathcal L((X\Phi)'')
 \end{pmatrix}.                                                  \tag{14}
$$



All entries are rational.  Matrix (14), rather than the much larger integer
jet matrix, is the exact fixed-$D$ object.

## 3. Shift/reflection reduction to one functional value

The generating function (4) gives the two identities



$$
\mathcal L(Q(X+1))+\mathcal L(Q(X))=Q(0),\qquad
 \mathcal L(Q(-X-1))=\mathcal L(Q(X)).                           \tag{15}
$$



If a polynomial $p$ vanishes at $0,1,\ldots,m-1$, iterating the first
identity gives



$$
\mathcal L(p(X+m))=(-1)^m\mathcal L(p). \tag{16}
$$



Since $n\geq2$, each of $\Phi^{(a)}$ for $0\leq a\leq2$ still
vanishes at those $m$ integers.  The reflection formula



$$
\Phi(-X-1)=(-1)^M\Phi(X+m)                   \tag{17}
$$



therefore yields



$$
\mathcal L(\Phi^{(a)})
        =(-1)^{mn+a}\mathcal L(\Phi^{(a)}).                     \tag{18}
$$



Let $G=X\Phi$ and $H=(X-(m-1))\Phi$.  Since



$$
G(-X-1)=(-1)^{M+1}H(X+m),                   \tag{19}
$$



the same argument gives



$$
\mathcal L(G^{(a)})=(-1)^{mn+a+1}
       \left(\mathcal L(G^{(a)})
                    -(m-1)\mathcal L(\Phi^{(a)})\right).       \tag{20}
$$



For even $a\in\{0,2\}$, equations (18)--(20) say:

* if $mn$ is even, then

  

$$
2\mathcal L((X\Phi)^{(a)})
          =(m-1)\mathcal L(\Phi^{(a)});                         \tag{21}
$$



* if $mn$ is odd, then

  

$$
\mathcal L(\Phi^{(a)})=0.              \tag{22}
$$



Consequently the two even columns of (14) have rank one.  When $mn$ is
even their common equation is the first row, and when $mn$ is odd it is
the second row.  In the notation (3), both cases are exactly



$$
s_0\mathcal L(\Psi)
                     +s_2\mathcal L(\Psi'')=0,                  \tag{23}
$$



which proves (5) as soon as $\mathcal L(\Psi)\ne0$.

This argument proves existence and uniqueness inside the even endpoint
subspace.  Full rank two of (14) also requires the odd-column pivot



$$
\mathcal L((X\Phi)')\ne0\quad(mn\text{ even}),\qquad
 \mathcal L(\Phi')\ne0\quad(mn\text{ odd}).                     \tag{24}
$$



The certificate finds no exception in its exact grid, but a proof of (24)
for all $m,n$ is not needed for (5) and is not claimed here.  Thus this
note proves a canonical nonzero $D=2$ construction, not full general
normality of every constrained system.

## 4. All-parameter nonvanishing from a multiset Eulerian polynomial

For a polynomial $p$, rational continuation of its ordinary generating
function gives the exact Abel identity



$$
\mathcal L(p)=\left.\sum_{r\geq0}p(r)x^r\right|_{x=-1}.
                                                                    \tag{25}
$$



Indeed, in a left half-plane



$$
\frac1{1+e^z}=\sum_{r\geq0}(-1)^re^{rz},                        \tag{26}
$$



and a polynomial differential operator may be applied termwise before
rational continuation to $z=0$.

Let $A_{m,q}(x)$ be defined by MacMahon's identity



$$
\sum_{r\geq0}\binom{r+m}{m}^{q}x^r
      =\frac{A_{m,q}(x)}{(1-x)^{mq+1}}.                          \tag{27}
$$



It is the descent polynomial for permutations of the multiset having
$q$ symbols, each repeated $m$ times.  Since



$$
\Phi_{m,n}(r)=(r)_m^q,                    \tag{28}
$$



shifting $r=m+t$ in (27) gives



$$
\sum_{r\geq0}\Phi_{m,n}(r)x^r
   =(m!)^q\frac{x^mA_{m,q}(x)}{(1-x)^{M+1}}.                    \tag{29}
$$



For equal multiplicities, $A_{m,q}$ is palindromic of exact degree



$$
m(q-1)=mn.                         \tag{30}
$$



Simion's multiindexed Sturm theorem says more: every zero of a multiset
Eulerian polynomial is real, negative, and simple.  Palindromicity pairs
every zero $\alpha\ne-1$ with $1/\alpha$.  Therefore



$$
\operatorname{ord}_{x=-1}A_{m,q}(x)=
   \begin{cases}
      0,&mn\text{ even},\\
      1,&mn\text{ odd}.
   \end{cases}                                                    \tag{31}
$$



Equations (25), (29), and (31) now give explicit nonzero formulas.  If
$mn$ is even,



$$
\mathcal L(\Psi)=\mathcal L(\Phi)
    =\frac{(m!)^q(-1)^mA_{m,q}(-1)}{2^{M+1}}\ne0.                \tag{32}
$$



If $mn$ is odd, applying $x\,d/dx$ to (29) gives



$$
\mathcal L(\Psi)=\mathcal L(X\Phi)
    =\frac{(m!)^q(-1)^{m+1}A_{m,q}'(-1)}{2^{M+1}}\ne0.           \tag{33}
$$



This proves the denominator nonvanishing in (6) for every $m\geq1$ and
$n\geq2$.  The restriction $n\geq2$ is natural here because $D=2$
requires $n\geq D$ in the original coefficient problem.

Reference for the simple-root theorem: R. Simion, *A multi-indexed Sturm
sequence of polynomials and unimodality of certain combinatorial sequences*,
J. Combin. Theory Ser. A **36** (1984), 15--22,
doi:10.1016/0097-3165(84)90075-X.

## 5. Exact pole and rotated-Laplace representations

The poles of $f$ are



$$
a_\ell=(2\ell+1)i\pi,
                         \qquad \ell\in\mathbb Z.                \tag{34}
$$



For a polynomial $p(X)=\sum_kp_kX^k$, define



$$
I_a(p)=\sum_kp_k k!a^{-k-1}.             \tag{35}
$$



The Mittag--Leffler expansion of $f$ gives, whenever $p(0)=0$,



$$
\mathcal L(p)=\sum_{\ell\in\mathbb Z}
                                             I_{a_\ell}(p).      \tag{36}
$$



For $p=\Psi$, the lowest power is at least three.  Both (36) and the
corresponding differentiated series are absolutely convergent, and



$$
I_a(p'')=a^2I_a(p).                 \tag{37}
$$



Combining (6), (34), and (36)--(37) gives the exact quotient



$$
\boxed{
 \rho_{m,n}=\pi^2
   \frac{\displaystyle\sum_{\ell\in\mathbb Z}(2\ell+1)^2
                          I_{a_\ell}(\Psi)}
        {\displaystyle\sum_{\ell\in\mathbb Z}I_{a_\ell}(\Psi)}.} \tag{38}
$$



In particular,



$$
\rho_{m,n}-\pi^2=\pi^2
   \frac{\displaystyle\sum_{\ell\in\mathbb Z}
                   \bigl((2\ell+1)^2-1\bigr)I_{a_\ell}(\Psi)}
        {\displaystyle\sum_{\ell\in\mathbb Z}I_{a_\ell}(\Psi)}. \tag{39}
$$



The terms $a_0=i\pi$ and $a_{-1}=-i\pi$ vanish identically from the
numerator of (39).  This is the exact first-pole cancellation; it does not
depend on an asymptotic approximation.

For $b>0$, (35) is also the convergent rotated-Laplace integral



$$
I_{ib}(p)=-i\int_0^\infty e^{-bu}p(-iu)\,du.    \tag{40}
$$



For positive real $a$, put $N=M+\varepsilon$ and let
$U$ have the gamma distribution with shape $N+1$ and scale one.  Direct
substitution in the ordinary Laplace integral gives



$$
I_a(\Psi)=N!a^{-N-1}\,
  \mathbb E\prod_{j=0}^{m-1}\left(1-\frac{aj}{U}\right)^q.      \tag{41}
$$



Both sides of (41) are finite algebraic expressions in $a$, so (41)
continues to every $a\ne0$, including the poles in (38).  Equations
(38)--(41) are an exact integral/determinantal representation for the
growing-$m$ endpoint.

The leading factor in (41) predicts



$$
\left|\frac{I_{3i\pi}(\Psi)}{I_{i\pi}(\Psi)}\right|
                  \approx3^{-N}                                 \tag{42}
$$



when $q=n+1$ is large.  The expectation contributes a correction of
order roughly $\exp(O(m/q))$, consistent with the exact diagnostics.
Turning this into a two-sided estimate requires a uniform noncancellation
bound for a complex expectation.  No such bound is asserted here.

## 6. Primitive endpoint height and exact ratio

Both values in (5) are rational.  Clear their common denominator, divide
their integer gcd, and choose the sign so that the quadratic coefficient is
positive.  This produces the unique primitive pair in (7), and (6) becomes



$$
\rho_{m,n}=\frac{P_{m,n}}{Q_{m,n}}.      \tag{43}
$$



Consequently



$$
C_{m,n}(i\pi)=P_{m,n}-Q_{m,n}\pi^2
               =Q_{m,n}(\rho_{m,n}-\pi^2),                     \tag{44}
$$



which proves (8).  This value is nonzero because $i\pi$ is transcendental
and $C_{m,n}$ is a nonzero integer polynomial.  No coefficient of $B$ or
any $A_j$ occurs in (43)--(44).  Thus this normalization tracks exactly the
content seen by the number-field polynomial in $e$.

There is a simple unconditional upper bound on the primitive height.  The
moments satisfy



$$
2^{k+1}\mathcal L(X^k)\in\mathbb Z,qquad
 |\mathcal L(X^k)|\ll k!,                                      \tag{45}
$$



and the coefficient $\ell^1$-norm of $\Phi$ is $(m!)^q$.  Clearing
by $2^{N+1}$, differentiating at most twice, and then taking a primitive
part yields



$$
\log H(C_{m,n})=O(N\log N),              \tag{46}
$$



uniformly for $m,n\geq2$.  Formula (46) is only an upper bound; it does
not estimate the endpoint gcd from below.  The exact data show that on the
tested diagonal



$$
\frac{\log H(C_{n,n})}{M\log M}\approx0.3\text{--}0.4,
 \qquad
 \frac{-\log|\rho_{n,n}-\pi^2|}{M}\longrightarrow\log3
 \quad\hbox{numerically}.                                      \tag{47}
$$



It follows in the data that



$$
\frac{-\log(|C_{n,n}(i\pi)|/H(C_{n,n}))}{\log H(C_{n,n})}
 \quad\hbox{decreases rather than diverges}.                    \tag{48}
$$



Again, (47)--(48) are diagnostics; the rigorous comparison is the next
section.

## 7. A fixed-degree $\pi$-measure blocks every growing-$m$ regime

### Lemma

For every fixed $D\geq1$, there are constants $c_D>0$ and
$K_\pi(D)<\infty$ such that every nonzero
$C\in\mathbb Z[z]$ with $\deg C\leq D$ satisfies



$$
|C(i\pi)|\geq c_DH(C)^{-K_\pi(D)}.      \tag{49}
$$



### Proof

Put



$$
F(X)=C(iX)\in\mathbb Z[i][X],\qquad
       U(X)=F(X)\overline{F(X)}=C(iX)C(-iX)\in\mathbb Z[X].     \tag{50}
$$



Then



$$
\deg U\leq2D,\qquad H(U)\leq(D+1)H(C)^2,
 \qquad U(\pi)=|C(i\pi)|^2.                                   \tag{51}
$$



Every root $\alpha$ of $U$ has algebraic degree at most $2D$, and
the length of its primitive minimal polynomial is bounded by a constant
depending on $D$ times $H(U)$; this is the standard fixed-degree factor
height bound.  Apply Aleksentsev's algebraic approximation measure for
$\pi$, with one fixed admissible degree parameter at least $2D$, to
every root of $U$.  It gives



$$
|\pi-\alpha|\gg_D H(U)^{-K_D'}          \tag{52}
$$



for some finite $K_D'$.  Factoring $U$, multiplying (52) over its at
most $2D$ roots, and using that its leading coefficient is a nonzero
integer gives



$$
|U(\pi)|\gg_DH(U)^{-K_D''}.             \tag{53}
$$



Equations (51) and (53) prove (49), after enlarging the fixed exponent.
$\square$

This proof only needs finiteness of a fixed-degree measure.  The explicit
Aleksentsev form already recorded in
`sources/algebraic_translation_approximation_no_go.md` is



$$
|\pi-\alpha|\geq
 \exp\!\left[-21.4708\,\mathscr D
       (\log L+\mathscr D\log\mathscr D)(1+\log\mathscr D)\right], \tag{54}
$$



with one sufficiently large fixed $\mathscr D\geq\deg\alpha$ and
$L\geq L(\alpha)$.  Thus all constants in (49) can be made effective.

For any sequence of primitive fixed-degree endpoints with height tending to
infinity, (49) implies



$$
\limsup
 \frac{-\log(|C(i\pi)|/H(C))}{\log H(C)}
       \leq K_\pi(D)+1<\infty.                                  \tag{55}
$$



If the heights stay bounded, there are only finitely many primitive integer
polynomials, so their nonzero endpoint values have a positive minimum.
There is therefore no bounded-height exception to (55).

Under (1), the normalized endpoint gives a degree-at-most-$D$ polynomial
in $e$ over $\mathbb Q(s,i)$.  The companion audit proves the lower
height exponent (10); at fixed hypothetical $s$ and fixed $D$, the
coefficient house of that polynomial is comparable to $H(C)$, up to fixed
$(s,D)$-dependent factors.  A contradiction based on a single endpoint
requires the exponent on the left of (55) to exceed $E(r,D)+1$.  Since the
former is bounded for fixed $D$, while the latter is unbounded in the
unknown degree $r$, no choice of growing $m,n$ at fixed $D$ can settle
every algebraic hypothesis by this comparison.

For clarity, (55) is not a numerical comparison between a possible achieved
exponent at degree $D$ and $E(r,D)$ for a fixed, known $r$.  It also
does not rule out a carefully coupled regime $D\to\infty$.  Its exact
logical content is that, at any one fixed $D$, varying $m,n$ cannot make
the endpoint exponent unbounded; hence it cannot automatically overtake
$E(r,D)$ for every a priori possible algebraic degree $r$.

This obstruction is endpoint-only and is therefore immune to auxiliary
factorial clearing or a large gcd in the full Hermite--Padé vector.

## 8. Higher endpoint multiplicity

A natural variant imposes a higher-order root at $y=-1$:



$$
P(z,y)=S(z)+(y+1)^hT(z,y).                                     \tag{56}
$$



Writing $B(z)=T(z,e^z)$ gives



$$
R(z)=S(z)+(1+e^z)^hB(z),\qquad R(i\pi)=S(i\pi),                \tag{57}
$$



and, near the origin,



$$
B(z)+S(z)f_h(z)=O(z^L),
        \qquad f_h(z)=(1+e^z)^{-h}.                              \tag{58}
$$



If the quotient space has integer frequency set $\Gamma$ and polynomial
degree bound $n$, its annihilator and endpoint functional are



$$
\Phi_{\Gamma,n}(X)=\prod_{\gamma\in\Gamma}
                         (X-\gamma)^{n+1},\qquad
 \mathcal L_h(e^{tX})=(1+e^t)^{-h}.                             \tag{59}
$$



The exact endpoint matrix is again



$$
\mathcal L_h\!\left((X^q\Phi_{\Gamma,n})^{(a)}\right),
       \qquad 0\leq q<D,\quad0\leq a\leq D.                   \tag{60}
$$



Thus the clean bridge to a polynomial in $e$ survives unchanged.

For the suggested choice $D=2h$, the $2h$ endpoint degrees match the
total multiplicity of the conjugate first poles $\pm i\pi$.  However
$f_h$ has the same pole locations as $f$; only their orders change.
For fixed $h$, its Taylor coefficients are finite sums of terms



$$
k^{j}a_\ell^{-k}\quad(0\leq j<h),              \tag{61}
$$



up to constants and lower powers of $k$.  Hence the exponential separation
between the first and second pole pairs remains $3^{-k}$, with polynomial
factors depending on $h$.  Raising the endpoint multiplicity does not
produce a superlinear fixed-$h$ pole-distance gain; it spends endpoint
degree to cancel confluent principal parts.

More importantly, for every fixed $h$, the degree $D=2h$ is fixed, so
the obstruction (49)--(55) applies verbatim.  If $h\to\infty$, then the
endpoint degree also tends to infinity.  Neither (55) nor the present pole
argument gives a useful uniform theorem in that regime; a claimed gain there
would have to be compared with the growing degree in the $e$-measure and
with the primitive endpoint content.  No such superlinear gain is proved.

## 9. Arbitrary integer frequencies and shifts

Let



$$
P(z,y)=\sum_{\lambda\in\Lambda}
                                  A_\lambda(z)y^\lambda          \tag{62}
$$



be a Laurent polynomial with finite integer frequency set $\Lambda$.
Division at $y=-1$ always gives



$$
P(z,y)=S(z)+(y+1)T(z,y),\qquad
             S(z)=\sum_{\lambda\in\Lambda}(-1)^\lambda
                                      A_\lambda(z).              \tag{63}
$$



Consequently the endpoint functional is still exactly (4).  Only the
annihilator of the quotient-frequency space changes.  For a full quotient
space with frequency set $\Gamma$, it is the first polynomial in (59)
with $h=1$.  Gaps or asymmetric frequencies can change the rational
numbers in the small endpoint matrix, but not the functional and not the
fixed-degree bound (49).

Pure shifts are even more rigid.  Replacing every frequency by
$\lambda+c$ replaces $P(z,y)$ by $y^cP(z,y)$, so



$$
S(z)\longmapsto(-1)^cS(z).          \tag{64}
$$



Thus a common integer shift leaves the primitive endpoint polynomial and
its height/value ratio exactly unchanged, up to sign.  It cannot improve
the arithmetic normalization.

Arbitrary frequency sets remain potentially useful for finite quantitative
optimization or for producing several independent endpoints.  They cannot,
by themselves, evade the fixed-$D$ obstruction for one endpoint
polynomial.  In particular, changing the annihilator does not create an
unbounded endpoint exponent at fixed degree.

## 10. Certificate and precise open point

The deterministic certificate checks exactly, for



$$
1\leq m\leq12,qquad2\leq n\leq12,           \tag{65}
$$



all 132 instances of:

* the shift/reflection relations (21)--(22);
* the exact degree, positivity, and palindromicity of $A_{m,n+1}$;
* the correct parity of $A_{m,n+1}(-1)$ and
  $A_{m,n+1}'(-1)$;
* the Abel identities (32)--(33);
* the primitive rational pair $(P_{m,n},Q_{m,n})$.

Selected exact pairs and high-precision endpoint diagnostics are stored in
the result JSON.  The all-parameter proof of nonvanishing uses Simion's
theorem; it is not extrapolated from these 132 cases.

What remains genuinely open inside this local construction is a uniform
two-parameter asymptotic for (38), including cancellation control in (41),
and a full proof of the odd pivot (24).  Neither missing lemma can overturn
the fixed-degree obstruction (55).  It could matter only for a different
argument using several endpoints, a growing endpoint degree, or additional
arithmetic structure not reduced to one fixed-degree value at $i\pi$.
