> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The centered-cosh lower lift: rank-one displacement, product endpoints, and an arithmetic barrier

## 1. Scope and verdict

Put



$$
S(z)=\frac1{2\cosh z}=\sum_{j\geq0}s_jz^j,\qquad
 s_{2j}=\frac{E_{2j}}{2(2j)!},\quad s_{2j+1}=0,             \tag{1}
$$



where $E_{2j}$ are the signed Euler numbers.  This note studies



$$
P_n[C]=-T_n(SC),\qquad
 R_n[C]=C+2\cosh(z)P_n[C],                                 \tag{2}
$$



where $T_n$ is ordinary Taylor truncation through degree $n$, at



$$
\zeta=\frac{i\pi}{2}.              \tag{3}
$$



The all-parameter conclusions are:

1. Multiplication by $z$ has exact displacement rank one.  Its kernel
   consists precisely of endpoints whose lift already uses only $n$
   auxiliary parameters.
2. On that kernel, a global Wronskian is an exact square.  Polarization
   identifies symmetric products of lower lifts with rational exterior
   sums, and their endpoint is the ordinary product.
3. If $t$ additional tail coefficients vanish, every factor has origin
   order at least $n+t+1$.  An unconditional product-space argument
   produces a nonzero endpoint of degree at most $2t+2$.
4. Exact saturated searches with $D=n-1$ find stronger quadratic
   survivors through $n=20$.  At the tested extremal rows
   $t=\lfloor(n-1)/3\rfloor$.  This is finite-only; no all-$n$
   quadratic rank theorem is claimed.
5. If that finite pattern persisted, its centered analytic gain would
   have leading constant only $2/3$ in $n\log n$.  A
   survivor-specific height theorem additionally needs a bound for a
   low-image quotient/Smith factor.  Ordinary Siegel lemma controls the
   high kernel but does not guarantee a nonzero endpoint.

Thus this is a genuine low-endpoint construction, not a classification of
$e+\pi$.  Current arithmetic information does not meet the degree-two
lower-bound threshold.

## 2. Canonical lift and exact displacement

Since $2\cosh(z)S(z)=1$, (2) is equivalently



$$
R_n[C]=2\cosh(z)\{SC-T_n(SC)\}=O(z^{n+1}).                \tag{4}
$$



Define



$$
\ell_n(C)=[z^n](SC).              \tag{5}
$$



The identity $T_n(zF)=zT_{n-1}(F)$ gives



$$
\boxed{
 P_n[zC]-zP_n[C]=\ell_n(C)z^{n+1},\qquad
 R_n[zC]-zR_n[C]=2\ell_n(C)z^{n+1}\cosh z .}              \tag{6}
$$



Thus the displacement map has rank zero or one on every endpoint space,
and it has rank one exactly when $\ell_n$ is nonzero there.  On



$$
E_D=\mathbb Q[z]_{\leq D},         \tag{7}
$$



its rank is one whenever $\min(D,n)\geq1$.  If
$\min(D,n)=0$, its rank is one for even $n$ and zero for odd $n$.
Indeed



$$
\ell_n(z^a)=
 \begin{cases}
 \displaystyle \frac{E_{n-a}}{2(n-a)!},
       &0\leq a\leq n,\ n-a\ {\rm even},\\[5pt]
 0,&\text{otherwise},
 \end{cases}                                               \tag{8}
$$



and every even Euler number is nonzero.  Multiplication by $2n!$
gives the integral row



$$
L_{n,a}=
 \begin{cases}
 (n)_aE_{n-a},
       &0\leq a\leq\min(D,n),\ n-a\ {\rm even},\\
 0,&\text{otherwise},
 \end{cases}
 \qquad (n)_a=\frac{n!}{(n-a)!}.                            \tag{9}
$$



When the row is nonzero, division by the gcd of its nonzero entries makes
(9) the primitive one-row presentation of the saturated lattice



$$
\ker(\ell_n)\cap\mathbb Z^{D+1}.       \tag{10}
$$



The sole Smith invariant before primitive row division is that gcd.  In
the exceptional rank-zero case the kernel is the full endpoint lattice
and there is no nonzero Smith invariant.

If $C\in\ker\ell_n$, then



$$
P_n[C]=P_{n-1}[C],\qquad P_n[zC]=zP_n[C],\qquad
 R_n[zC]=zR_n[C].                                          \tag{11}
$$



For example, for $n\geq1$,



$$
C_n=\begin{cases}1,&n\text{ odd},\\z,&n\text{ even}\end{cases}              \tag{12}
$$



belongs to the kernel.  In both cases $R_n[C_n]$ has exact origin
order $n+1$ and auxiliary degree $n-1$.

## 3. Endpoint correction, square, and polarization

Use



$$
W(F,G)=FG'-F'G.                   \tag{13}
$$



At $\zeta=i\pi/2$, $2\cosh\zeta=0$ and
$2\sinh\zeta=2i$.  Hence



$$
\begin{aligned}
 W(R_n[C],R_n[D])(\zeta)&=\Delta_n(C,D)(\zeta),\\
 \Delta_n(C,D)
   &=W(C,D)+2i\{C P_n[D]-P_n[C]D\}.                        \tag{14}
 \end{aligned}
$$



This fixes both the sign and factor $2i$.  For
$C\in\ker\ell_n$, (11) and (13) give



$$
W(R_n[C],R_n[zC])=R_n[C]^2,              \tag{15}
$$



and (14) reduces identically to



$$
\Delta_n(C,zC)=C^2.                \tag{16}
$$



More generally, if $C,D\in\ker\ell_n$,



$$
\begin{aligned}
 W(R_n[C],R_n[zD])+W(R_n[D],R_n[zC])&=2R_n[C]R_n[D],\\
 \Delta_n(C,zD)+\Delta_n(D,zC)&=2CD.                        \tag{17}
 \end{aligned}
$$



Thus every rational symmetric product tensor on the displacement kernel
has a rational two-column exterior realization.  The factor $2$ in
(17) matters integrally but is harmless over $\mathbb Q$.

The monomials (12) give degree-zero or degree-two endpoints and origin
order $2n+2$.  They do not give small endpoints: the values are $1$
and $-\pi^2/4$.  Their global polynomial degree is $2n-2$, so the
order surplus is only four.

## 4. Extra tail jets and an unconditional product theorem

For $0\leq t\leq D-1$, put



$$
U_{n,t,D}=\left\{C\in E_D:
      [z^k](SC)=0\quad(n\leq k\leq n+t)\right\}.            \tag{18}
$$



There are $t+1$ equations, so



$$
\dim U_{n,t,D}\geq D-t.            \tag{19}
$$



For every $C\in U_{n,t,D}$,



$$
\deg P_n[C]\leq n-1,\qquad
 R_n[C]=O(z^{n+t+1}).                                      \tag{20}
$$



Assume $D\leq n-1$.  A symmetric tensor on $U_{n,t,D}$ with product
endpoint $Q(z)$ has a polarized global form with



$$
\begin{array}{c|c|c|c}
\text{frequency band}&\text{polynomial degree}&\text{origin order}
     &\text{endpoint at }\zeta\\ \hline
-2,-1,0,1,2&\leq2n-2&\geq2(n+t+1)&Q(\zeta).
\end{array}                                                \tag{21}
$$



There is always a nonzero such endpoint with



$$
\deg Q\leq2t+2.               \tag{22}
$$



To prove this, let $V\subset\mathbb Q[z]_{\leq D}$ have dimension
$k$, with a basis $f_1,\ldots,f_k$ of strictly increasing degrees.
The $2k-1$ products



$$
f_1f_1,\ldots,f_1f_k,f_2f_k,\ldots,f_kf_k                \tag{23}
$$



have strictly increasing, distinct leading degrees.  Thus
$\dim(VV)\geq2k-1$.  With $V=U_{n,t,D}$, (19) and the intersection
bound in $\mathbb Q[z]_{\leq2D}$ give



$$
\begin{aligned}
 \dim\bigl(VV\cap\mathbb Q[z]_{\leq2t+2}\bigr)
 &\geq\{2(D-t)-1\}+(2t+3)-(2D+1)\\
 &\geq1.                                                    \tag{24}
 \end{aligned}
$$



This proves a product survivor, but its endpoint degree grows at the
same linear scale as the additional tail length.  At $t=D-1$, (18) is
the one-dimensional lower-parameter Padé problem when its rows have full
rank.  The product construction instead uses the higher-dimensional
space at smaller $t$; it is not merely that unique denominator.

## 5. Direct tensor equations and the precise rank gap

For $n\leq k\leq n+t$, multiply the $k$-th equation in (18) by
$2k!$.  Its integral monomial row is



$$
A_{k,a}=
 \begin{cases}
 (k)_aE_{k-a},
       &0\leq a\leq\min(D,k),\ k-a\ {\rm even},\\
 0,&\text{otherwise}.
 \end{cases}                                               \tag{25}
$$



Primitive row division leaves the rational kernel unchanged.  Use
symmetric coordinates $x_{ab}=x_{ba}$, $0\leq a\leq b\leq D$, with



$$
X=\sum_a x_{aa}e_a\otimes e_a
   +\sum_{a<b}x_{ab}(e_a\otimes e_b+e_b\otimes e_a).        \tag{26}
$$



Then $AX=0$ says exactly that both tensor slots lie in
$U_{n,t,D}$, and the endpoint product is



$$
Q_X(z)=\sum_a x_{aa}z^{2a}+2\sum_{a<b}x_{ab}z^{a+b}.       \tag{27}
$$



Killing every coefficient of (27) above $d$ is an explicit integral
system with coefficients $0,1,2$.  A fixed-degree survivor is
equivalent to the strict rank gap



$$
\operatorname{rank}(A X,\,[z^{d+1}],\ldots,[z^{2D}])
 <
 \operatorname{rank}(A X,\,[z^0],\ldots,[z^{2D}]).          \tag{28}
$$



The dimension inequality



$$
\binom{\dim U_{n,t,D}+1}{2}>2D-d                           \tag{29}
$$



does not prove (28): a nonzero high-kernel tensor may lie in the kernel
of the full multiplication map.  This is the exact rank-gap caveat.

## 6. Exact saturated grid

The companion certificate uses $D=n-1$, $d=2$, primitive rows (25),
an HNF/LLL saturated basis of (18), and its symmetric product map.  All
ranks and kernels are exact.  In the finite lattice output, the symmetric
algebra basis is $b_ib_j$, $i\leq j$, for the saturated endpoint
basis $b_i$.  It is rationally equivalent to (26); reported lattice
indices belong to this explicit convention, so no unrecorded factor-two
claim is made.  On



$$
5\leq n\leq20,\qquad t=\left\lfloor\frac{n-1}{3}\right\rfloor,               \tag{30}
$$



the following finite pattern occurs:

* If $n\equiv1,2\pmod3$, the low rank gap is one and its primitive
  direction is an even quadratic $a_n+b_nz^2$.
* If $n\equiv0\pmod3$, the low rank gap is two; constants and
  quadratics both survive.
* In the larger scan over every $0\leq t\leq n-2$, the maximum tested
  $t$ with a constant survivor is $\lfloor n/3\rfloor-1$, and the
  maximum with a degree-at-most-two survivor is
  $\lfloor(n-1)/3\rfloor$.

These are finite certificate statements, not recurrences in $n$.
The first two one-dimensional primitive directions are the exact anchors



$$
Q_{5}(z)=9375+3904z^2,\qquad
 Q_{7}(z)=6337786868+2568511585z^2.                         \tag{31a}
$$



Representative primitive quadratic heights are



$$
\begin{array}{c|rrrrrr}
n&7&10&13&16&19&20\\ \hline
\#\text{ decimal digits of }H(a_n+b_nz^2)&10&18&30&43&58&63.
\end{array}                                                 \tag{31}
$$



The exact values of



$$
\frac{\log H(a_n+b_nz^2)}{n\log n}                         \tag{32}
$$



increase from about $1.66$ at $n=7$ to about $2.38$ at
$n=19,20$.  A deterministic bounded search in the saturated
high-kernel gives globally normalized analytic coefficient heights with
essentially the same ratios.  This is negative finite evidence; no
asymptotic height law is inferred.

## 7. Centered Schwarz gain

Let $F$ be a nonzero survivor in (21), and put



$$
L=2(n+t+1),\qquad K=2n-2,\qquad A=L-K=2t+4.               \tag{33}
$$



If $H_{\rm an}(F)$ is the largest absolute coefficient in its centered
frequency representation, then for $\rho\geq1$, on $|z|=\rho$,



$$
|F(z)|\leq5(K+1)H_{\rm an}(F)\rho^K e^{2\rho}.             \tag{34}
$$



Schwarz's lemma at $|\zeta|=\pi/2$, optimized at
$\rho=A/2$, gives



$$
|Q(\zeta)|
 \leq5(K+1)H_{\rm an}(F)e^{-G_{n,t}},                      \tag{35}
$$



where



$$
\boxed{G_{n,t}=A\log\frac{A}{e\pi}-K\log\frac\pi2.}        \tag{36}
$$



If $t/n\to\tau>0$, then



$$
\frac{G_{n,t}}{n\log n}\longrightarrow2\tau.              \tag{37}
$$



Thus the finite quadratic scaling (30), if persistent, would have
leading gain $2/3$.  For fixed $t$, (36) is negative of order $n$,
since $\pi/2>1$; the monomial squares of Section 3 cannot become small.

## 8. Arithmetic ledger and quotient-height obstruction

The beta-value formula gives



$$
\frac{|E_{2j}|}{(2j)!}
 =\frac{4^{j+1}}{\pi^{2j+1}}\,\beta(2j+1)\leq1,             \tag{38}
$$



so $|s_j|\leq1/2$, and



$$
|A_{k,a}|\leq k!                  \tag{39}
$$



before primitive row division.  Suppose



$$
\frac Dn\to\delta,\qquad\frac tn\to\tau,\qquad0<\tau<\delta.                \tag{40}
$$



The direct tensor system has



$$
N=\binom{D+2}{2}\sim\frac{\delta^2n^2}{2},\qquad
 \dim\operatorname{Sym}^2U\geq
       \binom{D-t+1}{2}\sim\frac{(\delta-\tau)^2n^2}{2}.    \tag{41}
$$



Indeed, if $r=\operatorname{rank}A$ and
$k=D+1-r$, a rational change of basis carrying $\ker A$ to the first
$k$ coordinate axes shows that the symmetric solutions of $AX=0$
have dimension exactly $\binom{k+1}{2}$.  Thus the slot equations have
rank $N-\binom{k+1}{2}$.  For fixed target degree $d$, adding the
$2D-d$ high anti-diagonals changes this rank by only $O(n)$.

Selecting independent displayed rows retains entry bound $(n+t)!$.
Ordinary pigeonhole Siegel lemma therefore supplies some vector in that
high kernel with optimistic leading height



$$
\log H(X)\leq\{\theta(\delta,\tau)+o(1)\}n\log n,\qquad
 \theta(\delta,\tau)
 =\frac{(2\delta\tau-\tau^2)(1+\tau)}{(\delta-\tau)^2}.      \tag{42}
$$



Equation (42) is not a survivor theorem: that small vector may satisfy
$Q_X=0$.  Rank gap (28) proves only that some rational direction has
nonzero low image.  Without a bound for the quotient lattice or its
Smith factor, the rigorous cofactor survivor construction gives only



$$
\log H(X)=O(n^3\log n).             \tag{43}
$$



This is far larger than (37).  A quotient-Siegel theorem preserving
(42), or a structured low-image content theorem, is a genuinely missing
arithmetic input.

Granting the optimistic constant (42), the monomial lifts have analytic
coefficients bounded by $1$, so both raw endpoint and global analytic
heights have leading majorant $\theta n\log n$, up to polynomial
factors.  If endpoint normalization removes content



$$
\log c_X\sim\chi n\log n,           \tag{44}
$$



their exponents are at best $\theta-\chi$.  For an even primitive
quadratic,



$$
Q(\zeta)=a-\frac{b\pi^2}{4}.        \tag{45}
$$



If $s=e+\pi$ were rational, $4a-b(s-e)^2$ would, after clearing only
a fixed denominator, be a degree-two integer polynomial at $e$.
The degree-two measure contributes leading cost $2\log H(Q)$.
Combining this with (37), the displayed matched-majorant ledger could
close only under the optimistic inequality



$$
2\tau>3\{\theta(\delta,\tau)-\chi\}.                \tag{46}
$$



At the finite pattern's scaling $(\delta,\tau)=(1,1/3)$,



$$
\theta(1,1/3)=\frac53,\qquad
 \boxed{\chi>\frac{13}{9}}.                                \tag{47}
$$



Thus this particular majorant would require more than $13/9$ units of
$n\log n$ content even after granting the unproved
survivor-preserving version of (42).  Smaller actual representatives or a
sharper quotient theorem could change the ledger.  The finite primitive
heights in (31) show no such cancellation, but do not prove
impossibility.

## 9. Dilation and the half-phase class

Set $w=2z$.  Then



$$
e^{w/2}R_n[C](w/2)
   =e^{w/2}C(w/2)+(1+e^w)P_n[C](w/2).                      \tag{48}
$$



At $w=i\pi$, the endpoint phase $e^{w/2}=i$ is algebraic, but
globally it has half-integral frequency.  Multiplication by any integral
frequency $e^{jw}$ preserves that class modulo $\mathbb Z$.  Hence
the centered-cosh construction is the genuinely half-phase class, not
an integral-frequency polynomial-endpoint family in disguise.

More generally, a pre-dilation shift indexed by an integer $a$ becomes
the class $a/2\pmod{\mathbb Z}$.  Even $a$ is integral and reduces
to the ordinary two-frequency polynomial-endpoint family; odd $a$
remains the half-phase/sech class studied here.  If
$\deg C\leq D$, clearing the dilation gives



$$
2^D C(w/2)=\sum_{a=0}^D c_a2^{D-a}w^a.                 \tag{49}
$$



Primitive gcd removal is the only possible saving.  Thus dilation changes
height by at most $D\log2$ before content and creates no new asymptotic
exponent.

## 10. Replay and logical status

The companion script verifies (6), (14)--(17), primitive tail rows, HNF
saturation, all finite ranks in Section 6, primitive quadratic
directions, exact origin orders of selected global products, and the
finite height/margin ledger.  Every rank and coefficient assertion is
exact; decimal evaluations are diagnostics only.

The all-parameter results are (6), (14)--(29), and the implications
(33)--(49) with their stated hypotheses.  The quadratic pattern
(30)--(32) is not extrapolated.  No conclusion about the arithmetic
nature of $e+\pi$ is claimed.
