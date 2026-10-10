> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## All-depth result

The proposed analytic claims hold. They give the exact residual divisibility


$$
\boxed{v\in 3M\mathbb Z_3^{\,3M}\qquad(M\ge1).}
$$


Moreover, they imply the requested local limiting ray **without an additional index offset**:


$$
\boxed{
Q_n^{\rm loc}(y)=3P_n(y)
\equiv (y+1)(y-1)^{n-2}(3y-71)\pmod{3^K}
}
$$


for every


$$
\boxed{K\ge1,\qquad j\ge1,\qquad 3^K\mid j,\qquad n=4^j+1.}
$$


This is a congruence for the locally normalized primitive ray. The actual primitive integer polynomial retains the unit


$$
Q_n=\lambda_nQ_n^{\rm loc},\qquad
\lambda_n=L_n/3\in\mathbb Z_3^\times.
$$



No assertion about irrationality of $e+\pi$ follows from this local theorem.

### 1. Full moment expansion in the restricted power-series ring

Write $\mathbb Z_3\langle T\rangle$ for ordinary power series with integral coefficients tending to zero $3$-adically, equipped with the coefficient Gauss norm.

The exact factorial-moment expansion is


$$
b_s^{\rm mom}
=(-2)^s\sum_{\ell\ge0}
\frac{(-1)^\ell}{2^\ell\ell!}
\prod_{a=-\ell+1}^{\ell}(s+a),
\qquad s\in\mathbb Z_{\ge0}.
\tag{1}
$$


For these integer arguments the summands with $\ell>s$ vanish. Formula (1) also follows directly by expanding
$(t^2-2t)^s$ in the defining exponential integral.

Fix $r\in\{0,1,2\}$, and substitute $s=3T+r$ in the product in (1). If $z$ of its $2\ell$ constant factors are divisible by $3$, then


$$
z\ge\lfloor2\ell/3\rfloor.
$$


Every contribution to the coefficient of $T^k$ consequently has valuation at least


$$
\boxed{
\max\{k,\lfloor2\ell/3\rfloor\}-v_3(\ell!).
}
\tag{2}
$$


Selecting $k$ variable factors supplies $3^k$; at least $z-k$ divisible constant factors remain if $z>k$.

There are two required convergence statements.

* Uniformly in $k$, the lower bound in (2) tends to infinity with $\ell$. Indeed,
  

$$
\lfloor2\ell/3\rfloor-v_3(\ell!)
  \ge \frac{\ell}{6}-1.
$$


  Thus the series of polynomials converges in the Gauss norm.
* Uniformly in $\ell$, the bound tends to infinity with $k$. Using $v_3(\ell!)\le\ell/2$, split at $\ell=3k/2$. This gives the sufficient bound
  

$$
\max\{k,\lfloor2\ell/3\rfloor\}-v_3(\ell!)
  \ge k/4-1.
$$


  Hence the limiting ordinary coefficients tend to zero.

For every $\ell\ge3$,


$$
\lfloor2\ell/3\rfloor-v_3(\ell!)\ge1.
$$


For example, $\ell=3$ is immediate; for $\ell\ge4$, use
$v_3(\ell!)\le(\ell-1)/2$, and then integrality of the valuation bound. The terms $\ell=0,1,2$ have unit factorial denominators and all their nonconstant coefficients are divisible by $3$. Therefore the sum in (1), after substitution, has every nonconstant coefficient in $3\mathbb Z_3$.

Finally,


$$
(-2)^{3T+r}=(-2)^r\exp\bigl(T\log(1-9)\bigr).
$$


Its coefficient of $T^k$ has valuation at least $2k-v_3(k!)$. This is a restricted integral series, with all nonconstant coefficients divisible by $9$.

It follows that each branch $b_{3T+r}^{\rm mom}$ belongs to
$\mathbb Z_3\langle T\rangle$, with every nonconstant coefficient divisible by $3$. Integral translations handle the indices $3T+r+1$ and $3T+r+2$. Thus the **complete** formula


$$
e_s=4b_s^{\rm mom}+4(s+1)b_{s+1}^{\rm mom}
 +(s+1)(s+2)b_{s+2}^{\rm mom}
\tag{3}
$$


proves


$$
\boxed{
e_{3T+r}\in\mathbb Z_3\langle T\rangle,\qquad
[T^k]e_{3T+r}\in3\mathbb Z_3\quad(k\ge1).
}
\tag{4}
$$


All endpoint scalar terms in (3) have been retained.

In particular $e_0=12$, so (4) gives the stronger branch statement


$$
\boxed{e_{3T}/3\in\mathbb Z_3\langle T\rangle.}
\tag{5}
$$



### 2. The unit-factorial quotient: explicit denominator control

Set


$$
U(a)=\prod_{v=0}^{a-1}(3v+1)(3v+2).
$$


For nonnegative integers $a$,


$$
U(a)=2^a\prod_{v<a}\left(1+\frac92v(v+1)\right).
$$



Here is a direct power-sum denominator bound, avoiding any gamma-function regularity assumption. Expand the integer polynomial


$$
(v(v+1))^\ell=\sum_{h=0}^{2\ell}d_{\ell h}(v)_h,
\qquad d_{\ell h}\in\mathbb Z.
$$


Then


$$
S_\ell(A):=\sum_{v<A}(v(v+1))^\ell
=\sum_{h=0}^{2\ell}\frac{d_{\ell h}}{h+1}(A)_{h+1}.
\tag{6}
$$


Consequently every ordinary coefficient of $S_\ell$ has valuation at least


$$
-\lfloor\log_3(2\ell+1)\rfloor.
$$



Define


$$
F(A)=\sum_{\ell\ge1}
\frac{(-1)^{\ell+1}}{\ell}\left(\frac92\right)^\ell S_\ell(A).
\tag{7}
$$


The coefficient Gauss valuation of its $\ell$-th summand is at least


$$
d_\ell=2\ell-v_3(\ell)-\lfloor\log_3(2\ell+1)\rfloor.
\tag{8}
$$


These bounds are at least $1$ and tend to infinity. For completeness, for $\ell\ge2$ one can use


$$
v_3(\ell)\le\ell-1,\qquad
\lfloor\log_3(2\ell+1)\rfloor\le\ell-1;
$$


the case $\ell=1$ has $d_1=1$. Hence


$$
F\in3\mathbb Z_3\langle A\rangle,\qquad F(0)=0.
$$



The two-variable series


$$
J(Q,D)=\exp\bigl(F(Q+D)-F(Q)-F(D)\bigr)
\tag{9}
$$


belongs to $1+3\mathbb Z_3\langle Q,D\rangle$. Indeed the exponential series converges in Gauss norm, since its $m$-th term has valuation at least $m-v_3(m!)$. At nonnegative integer arguments, (7) is the logarithm of $U(a)/2^a$, so


$$
J(q,D)=\frac{U(q+D)}{U(q)U(D)}.
\tag{10}
$$


Moreover $J(Q,0)=1$.

The exact factorial separation and adjacent-factor identities now give


$$
\binom{3(q+D)+r}{3D}
=\binom{q+D}{D}\,J(q,D)
\prod_{a=1}^{r}\frac{3(q+D)+a}{3q+a}.
\tag{11}
$$


The denominators are units. As functions of $Q$,


$$
(3Q+a)^{-1}=a^{-1}\sum_{m\ge0}(-3Q/a)^m
$$


are restricted integral series. Thus (11) provides the required analytic multiplier, uniformly in every integer $q\ge0$, and every nonconstant coefficient in $D$ is divisible by $3$.

### 3. Exact all-depth residual lemma and uniform tails

Define


$$
K_{q,r}(D)=
J(q,D)\prod_{a=1}^{r}\frac{3(q+D)+a}{3q+a}
\,e_{3(q+D)+r}.
\tag{12}
$$


The preceding results show


$$
K_{q,r}\in\mathbb Z_3\langle D\rangle,
$$


with all nonconstant coefficients divisible by $3$. These statements are uniform in $q$: (12) arises by evaluating a restricted two-variable series at $Q=q$.

Write


$$
K_{q,r}(D)=\sum_{k\ge0}a_k(q,r)D^k.
$$


Conversion using integer Stirling numbers gives


$$
K_{q,r}(D)=\sum_{h\ge0}\kappa_h(q,r)(D)_h,\qquad
\kappa_h(q,r)=\sum_{k\ge h}
a_k(q,r)\left\{\begin{matrix}k\\h\end{matrix}\right\}.
\tag{13}
$$


The inner sums converge; uniformly in $q,r$,


$$
\inf_{h>H}v_3(\kappa_h(q,r))\longrightarrow\infty.
$$


Also


$$
\boxed{\kappa_h(q,r)\in3\mathbb Z_3\quad(h\ge1).}
\tag{14}
$$


These estimates justify rearranging the double series: the Gauss norms of $(D)_h$ are at most one and the Stirling numbers are integers.

For


$$
L=3M,\quad M\ge1,\quad i=3q+r<L,\quad
\tau_D=(-1)^{M-D}\binom MD,
$$


the actual residual entry is


$$
v_i=\sum_{D=0}^M\tau_D\binom{i+3D}{i}e_{i+3D}.
$$


Apply the exact finite-difference identity to (13):


$$
\boxed{
v_{3q+r}
=\sum_{h=0}^{M}
\kappa_h(q,r)(M)_h\binom{q+h}{M}.
}
\tag{15}
$$


There is no infinite interchange left in (15): at integer $0\le D\le M$, every falling factorial with $h>M$ vanishes. Since $q<M$, the $h=0$ term vanishes. Each other term contains $3M$, proving


$$
\boxed{v\in3M\mathbb Z_3^L.}
\tag{16}
$$



There is also a uniform normalized precision statement. If the coefficients $\kappa_h$, $h>H$, have depth at least $P+1$, then the omitted terms of (15), **after division by $3M$**, have depth at least $P$. This follows because $(M)_h/M$ is an integer for $1\le h\le M$. Thus dimension growth causes no loss of residual precision.

### 4. Restricted analytic raw contractions

The raw contractions can themselves be interpolated in $M$ without interpolating any matrix inverse.

For a monomial define


$$
C_{a,t}(M)=
\sum_{h=t}^{a}
\left\{\begin{matrix}a\\h\end{matrix}\right\}
(M)_h\binom ht
$$


and


$$
\mathscr C_M(D^aE^b)=
\sum_{t=0}^{\min(a,b)}C_{a,t}(M)C_{b,t}(M).
\tag{17}
$$


Every output in (17) is an integer polynomial in $M$, of degree at most $a+b$ and Gauss norm at most one.

The Pascal identity
$\binom{D+E}{D}=\sum_k\binom Dk\binom Ek$, followed by the finite-difference identity, proves for every integer $M\ge0$


$$
\mathscr C_M(f)=
\sum_{D,E=0}^{M}\tau_D\tau_E\binom{D+E}{D}f(D,E)
\tag{18}
$$


for polynomials $f$. Formula (17) remains valid when $M$ is smaller than a monomial degree: the excess terms contain $(M)_h=0$.

The norm bound extends $\mathscr C$ continuously from polynomials to


$$
\mathscr C:\mathbb Z_3\langle D,E\rangle
\longrightarrow\mathbb Z_3\langle M\rangle.
$$


Finite sums in (18) permit passage to the limit, so (18) remains exact for restricted series. This supplies uniform raw-contraction tail precision.

In particular set


$$
H(M)=\mathscr C_M\!\left(
J(D,E)\frac{e_{3(D+E)}}3
\right),
$$




$$
G(M)=\mathscr C_M\!\left(
J(D,E)\frac{3(D+E)+1}{3E+1}e_{3(D+E)+1}
\right).
\tag{19}
$$


Then


$$
H,G\in\mathbb Z_3\langle M\rangle,\qquad
R/3=H(M),\quad X=G(M).
$$


At $M=0$, the contraction is evaluation at $D=E=0$. Since


$$
b_0=1,\quad b_1=0,\quad b_2=4,\quad b_3=40,
$$


equation (3) gives


$$
\boxed{H(0)=4,\qquad G(0)=272.}
\tag{20}
$$


Every integral restricted series is $1$-Lipschitz on $\mathbb Z_3$. Therefore


$$
\boxed{H(M)-4\in M\mathbb Z_3,\qquad G(M)-272\in M\mathbb Z_3.}
\tag{21}
$$



### 5. Projection, endpoint terms, and the limiting ratio

Let $m=v_3(M)$. Use the actual columns and Schur quantities from the supplied construction:


$$
c=R-v^TE^{-1}v,\qquad
\xi_{\rm last}=X-v^TE^{-1}w.
$$


Only the established integrality of $E^{-1}$ is needed. The vector $w$ is integral, since it consists of pairings of integral divided-basis combinations. From (16),


$$
v^TE^{-1}v/3\in3^{2m+1}\mathbb Z_3,\qquad
v^TE^{-1}w\in3^{m+1}\mathbb Z_3.
$$


Together with (21),


$$
\boxed{
c/3\equiv4,\qquad \xi_{\rm last}\equiv272\pmod{3^m}.
}
\tag{22}
$$


For $m\ge1$, $c/3$ is consequently a unit.

Retain the constant-row terms in the exact ratio:


$$
\Theta_M=3\eta_{\rm last}
=\frac{\xi_{\rm last}-(b/a)\xi_{\rm const}}
{c/3-b^2/(3a)}.
\tag{23}
$$


The established endpoint remainder bounds are


$$
a\in\mathbb Z_3^\times,\qquad
b,\xi_{\rm const}\in L!\mathbb Z_3.
$$


Writing $F=v_3(L!)=v_3(N!)$, the two endpoint corrections in (23) have depths at least $2F$ and $2F-1$. Since $L=3M$,


$$
F\ge m+1.
$$


Thus these corrections do not affect (22) at precision $3^m$. Division by the unit denominator proves


$$
\boxed{\Theta_M\equiv68\pmod{3^m}\qquad(m\ge1).}
\tag{24}
$$


This proves the projected local limit while making no analytic claim about a dimension-changing inverse.

### 6. Factorial tail and actual primitive unit

Take $K\ge1$ and $3^K\mid j$. LTE gives


$$
m=v_3(M)=v_3(j)\ge K,\qquad
N=4^j=1+3M,\quad L=N-1.
$$



In the exact expansion


$$
3P_n=3h_n-3N!\eta_{\rm const}
-\sum_{d=0}^{L}\frac{N!}{d!}(3\eta_{d+1})h_{d+1},
\qquad h_{d+1}=(y+1)(y-1)^d,
\tag{25}
$$


all $3\eta_i$ are integral. This follows from integral elimination through $E$, the unit $a$, and the final Schur pivot of valuation one.

For **every** lower index $d\le L-1$, the factorial quotient in (25) contains $L$, so


$$
v_3(N!/d!)\ge m+1>K.
$$


There is no thin-tail exception at this precision. The constant term is the endpoint $3P_n(-1)$, whose established exact valuation is $2F\ge2m+2$; it too vanishes modulo $3^K$.

The surviving last term yields


$$
3P_n\equiv
(y+1)(y-1)^L\bigl(3(y-1)-N\Theta_M\bigr)\pmod{3^K}.
$$


Now $N\equiv1\pmod{3^K}$ and (24) gives $\Theta_M\equiv68\pmod{3^K}$. This proves the stated factor $3y-71$.

For clarity, the primitive normalization is not suppressed. Equation (25) gives $3P_n\in\mathbb Z_3[y]$, and


$$
[y^{n-1}](3P_n)=3[y^{n-1}]h_n-N\Theta_M
$$


is a unit, since $\Theta_M\equiv68\equiv2\pmod3$. Thus the minimum coefficient valuation of the monic rational $P_n$ is exactly $-1$. If $Q_n=L_nP_n$ is its actual primitive integer normalization, this proves


$$
v_3(L_n)=1,\qquad Q_n=(L_n/3)Q_n^{\rm loc}.
$$


The endpoint remains nonzero, with


$$
v_3(Q_n(-1))=2v_3(N!).
$$



### 7. Final gcd and whole error

These polynomial results do not evaluate the final determinant gcd. For an integer clearing of the complete coefficient pair $A,B$, retain


$$
g=\gcd(|A|,|B|),\qquad
q=\frac{|B|}{g},\qquad
p=-\frac{\operatorname{sgn}(B)A}{g}.
$$


Where $B\ne0$, the actual whole error is


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B)}g\bigl(A+B(e+\pi)\bigr)
=\frac{\operatorname{sgn}(B)\ell^k}{g}\det H_{\rm complete},
\qquad k=(n+1)/2.
}
$$


No factorial term, rational arctangent term, or period contribution has been discarded. Polynomial endpoint nonvanishing does not alone prove $B\ne0$, nor nonvanishing or decay of this whole evaluated error.

## Closing ledger

1. **New result and proof status.** Proved the full restricted-analytic moment and unit-factorial quotient lemmas; the uniform exact all-depth residual $v\in3M\mathbb Z_3^L$; restricted analytic raw contractions with values $4,272$ at $M=0$; and the local ray
   

$$
Q_n^{\rm loc}\equiv(y+1)(y-1)^{n-2}(3y-71)\pmod{3^K}
$$


   for every $K\ge1$ and every positive $j$ divisible by $3^K$. No extra offset is needed. The projection and polynomial transfer use the established integral elimination and endpoint bounds, not an analytic inverse assumption.

2. **Exact remaining bottleneck.** Irrationality still requires an infinite sequence with nonzero complete response and nonzero **whole primitive errors tending to zero**, after the actual final gcd. The local polynomial theorem supplies neither the necessary denominator control nor that real-error estimate.

3. **Computation request.** None. The all-depth statements above follow from coefficient bounds and exact identities, not finite numerical evidence.
