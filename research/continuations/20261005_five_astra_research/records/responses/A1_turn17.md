> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Audit outcome

The restricted-series argument in turn15 survives the coefficient and interchange audit. In particular, its contraction operator computes **ordinary Taylor coefficients**, not coefficients inferred from integer values.

I obtain the following true jets:


$$
\boxed{
H'(0)\equiv3,\quad G'(0)\equiv21,\quad
\Theta_{\rm raw}'(0)\equiv15,\quad
(N\Theta_{\rm raw})'(0)\equiv3\pmod{27}.
}
$$


Thus all four proposed residues modulo $9$ are correct.

The improved projection estimate also follows from the specified hypotheses. The remaining issue in promoting this to an unconditional polynomial congruence from the supplied documents is narrower: turn14 refers to a “first radical support” calculation, but does not provide its complete coordinate/force derivation. Below I give an explicit integral-elimination lemma that supplies that calculation once its coordinate hypotheses are verified. I distinguish this interface from the parts proved directly here.

### 1. Audit of convergence and coefficient bounds

Put


$$
P_\ell(s)=\frac{(-1)^\ell}{2^\ell\ell!}
 \prod_{a=-\ell+1}^{\ell}(s+a).
$$


For every fixed integer $r$, the coefficient of $T^k$ in $P_\ell(3T+r)$ has valuation at least


$$
\max\{k,\lfloor2\ell/3\rfloor\}-v_3(\ell!).
\tag{1}
$$


Indeed, among the $2\ell$ consecutive constant factors at least
$\lfloor2\ell/3\rfloor$ are divisible by $3$. Selecting $k$ variable factors supplies $3^k$, and removes at most $k$ of those divisible constant factors.

Both uniform bounds used in turn15 are valid:


$$
\lfloor2\ell/3\rfloor-v_3(\ell!)\ge \ell/6-1,
$$


and


$$
\max\{k,\lfloor2\ell/3\rfloor\}-v_3(\ell!)
\ge k/4-1.
$$


For the second, split at $\ell=3k/2$ and use $v_3(\ell!)\le\ell/2$. These establish Gauss-norm convergence and decay of the resulting ordinary coefficients. They apply also to $r=3$, needed below.

The Faulhaber argument is likewise sound. Expanding in falling factorials gives


$$
\sum_{v<A}(v(v+1))^\ell
=\sum_{h=0}^{2\ell}\frac{d_{\ell h}}{h+1}(A)_{h+1},
\qquad d_{\ell h}\in\mathbb Z.
$$


Thus its ordinary coefficients have valuation at least
$-\lfloor\log_3(2\ell+1)\rfloor$. The logarithmic summand consequently has Gauss valuation at least


$$
2\ell-v_3(\ell)-\lfloor\log_3(2\ell+1)\rfloor,
$$


which is positive and tends to infinity. Substitution $A=Q+D$ is a bounded map of restricted-series rings: all binomial coefficients involved are integral. The subsequent exponential converges because its $h$-th term has valuation at least $h-v_3(h!)$.

Importantly,


$$
\boxed{J(D,0)=J(0,E)=1.}
\tag{2}
$$


Both identities follow from $F(0)=0$. They eliminate all nonconstant pure-variable contributions from $J$.

The Stirling conversion in turn15 is also legitimate. Its coefficient tails tend uniformly to zero, and each falling factorial has integral coefficients. For an integer argument $0\le D\le M$, terms with falling-factorial index greater than $M$ vanish. Thus the residual identity is a genuinely finite identity after evaluation; no unbounded interchange remains.

### 2. Why the contraction really computes the asserted derivative

Write $I_{ab}(M)=\mathscr C_M(D^aE^b)$, with the exact contraction of turn15. Its defining polynomials have integral coefficients. For $a>0$, every $C_{a,t}(M)$ is divisible by $M$, since every contributing falling factorial has positive index. Hence


$$
I_{ab}(M)\in M^2\mathbb Z[M]\qquad(a,b>0).
\tag{3}
$$


For $a=0$,


$$
I_{0b}(M)=C_{b,0}(M)
=\sum_h\left\{\begin{matrix}b\\h\end{matrix}\right\}(M)_h
=M^b.
\tag{4}
$$



The contraction is Gauss-norm nonincreasing. Extraction of the coefficient of $M$ is also Gauss-norm nonincreasing. Consequently coefficient-tail convergence is preserved through contraction and through derivative evaluation at zero.

Equations (3)–(4) say that only the $D$ and $E$ coefficients of the input can contribute to the linear Taylor coefficient. Applying (2) therefore proves


$$
\boxed{
H'(0)=2\left(\frac{e_{3T}}3\right)'_{T=0},
\qquad
G'(0)=3e_1+2(e_{3T+1})'_{T=0}.
}
\tag{5}
$$


In the second identity, the pure-$D$ restriction of the adjacent-factor multiplier is $3D+1$, while its pure-$E$ restriction is $1$. This accounts for the $3e_1$ term.

### 3. An explicit bounded computation of the true jet

Let $B_r(T)=b_{3T+r}$, for $0\le r\le3$. Gauss-norm convergence justifies differentiation:


$$
B_r'(0)=\log(-8)b_r+
3(-2)^r\sum_{\ell\ge0}P_\ell'(r).
\tag{6}
$$


For $\ell>r$, exactly one factor of the product vanishes at $s=r$. Multiplying the remaining factors gives


$$
P_\ell'(r)
=(-1)^{r+1}
\frac{(\ell-r-1)!(r+\ell)!}{2^\ell\ell!}.
\tag{7}
$$


In particular,


$$
v_3\!\left(3(-2)^rP_\ell'(r)\right)
\ge1+v_3((\ell-r-1)!).
\tag{8}
$$


Here $(r+\ell)!/\ell!$ is an integer. This bound tends to infinity and proves derivative-tail convergence directly, independently of value congruences.

For a small, reproducible calculation modulo $81$, retain $0\le\ell\le12$. For every omitted $\ell\ge13$ and $r\le3$, (8) gives depth at least


$$
1+v_3(9!)=5.
$$


Also $\log(-8)\equiv-9\pmod{81}$. Thus the following finite formula determines each entry exactly modulo $81$:


$$
B_r'(0)\equiv
-9b_r+3(-2)^r
\left[
 \sum_{\ell=0}^{r}P_\ell'(r)
 +(-1)^{r+1}\sum_{\ell=r+1}^{12}
 \frac{(\ell-r-1)!(r+\ell)!}{2^\ell\ell!}
\right]\pmod{81}.
\tag{9}
$$


The finite $\ell\le r$ terms are retained, not replaced by (7). Evaluation gives


$$
\begin{array}{c|rrrr}
r&0&1&2&3\\ \hline
B_r'(0)\bmod81&6&72&51&36.
\end{array}
\tag{10}
$$


These agree with, but do not require inference from, the supplied modulus-$729$ receipt.

Differentiating the complete moment formula gives


$$
(e_{3T})'_0
=4B_0'+12b_1+4B_1'+9b_2+2B_2',
$$




$$
(e_{3T+1})'_0
=4B_1'+12b_2+8B_2'+15b_3+6B_3'.
$$


Using $(b_0,b_1,b_2,b_3)=(1,0,4,40)$, these are respectively


$$
45,\quad21\pmod{81}.
$$


Consequently (5) yields


$$
H'(0)\equiv3,\qquad G'(0)\equiv21\pmod{27}.
$$



Since $H(0)=4$, $G(0)=272$, and
$\Theta_{\rm raw}=G/H$,


$$
\Theta_{\rm raw}(0)=68,\qquad
\Theta_{\rm raw}'(0)=\frac{G'(0)-68H'(0)}4
\equiv15\pmod{27}.
$$


With $N=1+3M$,


$$
(N\Theta_{\rm raw})'(0)
=204+\Theta_{\rm raw}'(0)\equiv3\pmod{27}.
\tag{11}
$$



The inverse of $H$ need not be asserted to lie in the whole unit-disc Tate algebra merely because $H(0)$ is a unit. What is sufficient here is that its **formal** inverse has integral coefficients and converges for $M\in3\mathbb Z_3$. Therefore, for $m=v_3(M)\ge2$,


$$
\boxed{
N\Theta_{\rm raw}(M)\equiv68+3M\pmod{3^{m+2}}.
}
\tag{12}
$$


All higher Taylor terms have depth at least $2m\ge m+2$.

### 4. Projection transfer at the extra two digits

Use precisely the stipulated bounds


$$
v\in3M\mathbb Z_3^L,\qquad
w\in3\mathbb Z_3^L,\qquad E^{-1}\in M_L(\mathbb Z_3).
$$


Then


$$
v^TE^{-1}v/3\in3^{2m+1}\mathbb Z_3,\qquad
v^TE^{-1}w\in3^{m+2}\mathbb Z_3.
\tag{13}
$$


For $m\ge1$, both have depth at least $m+2$.

Retain the complete endpoint terms:


$$
\Theta_M=
\frac{\xi_{\rm last}-(b/a)\xi_{\rm const}}
{c/3-b^2/(3a)}.
$$


Under the endpoint hypotheses recorded in turn15,


$$
a\in\mathbb Z_3^\times,\qquad
b,\xi_{\rm const}\in L!\mathbb Z_3,
$$


their depths are at least $2F$ and $2F-1$, where
$F=v_3(L!)\ge m+1$. These also reach $m+2$ for $m\ge1$.
All relevant denominators are units. Thus


$$
\boxed{\Theta_M-\Theta_{\rm raw}(M)\in3^{m+2}\mathbb Z_3.}
\tag{14}
$$


This uses no analytic interpolation of the dimension-changing inverse.

### 5. Exact factorial-tail interface

For precision $3^{m+2}$, the only dangerous lower factorial indices are


$$
d=L-1,\quad L-2,\quad L-3.
$$


Their factorial quotients have depth $m+1$. Every $d\le L-4$ has depth at least $m+2$, because its quotient contains both $L$ and $L-3$. Therefore the needed coefficient assertion is exactly


$$
3\eta_L\equiv3\eta_{L-1}\equiv3\eta_{L-2}\equiv0\pmod3.
\tag{15}
$$



Here is a bounded lemma giving the required **full-support** calculation, rather than checking just those three coefficients.

**Integral-force support lemma.** Suppose the actual divided-basis elimination has an integral regular block $A$ with integral inverse, an exceptional column $z$, and regular-to-exceptional coupling $u\in3\mathbb Z_3^d$. Suppose the full regular force is integral. If the solution’s exceptional coordinate is $\theta/3$, with $\theta\in\mathbb Z_3$, then the regular coordinates $x$ satisfy


$$
3x=3A^{-1}f-A^{-1}u\,\theta\equiv0\pmod3.
$$


Consequently, if


$$
z=\sum_{D=0}^{M}(-1)^{M-D}\binom MD\,f_{3D},
$$


then, in the original divided coordinates,


$$
3\eta_{d+1}\equiv
\begin{cases}
\theta(-1)^{M-D}\binom MD,&d=3D,\\
0,&3\nmid d
\end{cases}
\pmod3
\tag{16}
$$


for **every** $0\le d\le L$. This proves the complete support statement.

For $3\mid M$, (16) implies (15): the first two indices are not divisible by $3$, and the coefficient at $d=L-3$ is $-M\theta$.

The supplied turn14 states this radical support, but its derivation does not display the full regular force or the coordinate transformation identifying its $f_{3D}$ with the $\eta$-coordinates in the factorial expansion. Integrality of $3\eta$ alone does not establish (16). Thus the lemma is proved, while its complete-coordinate application is an explicit remaining verification from the present source packet.

**Conditional polynomial conclusion.** Once that interface is verified, every lower factorial term vanishes modulo $3^{m+2}$. The constant endpoint has depth $2F\ge m+2$. Equations (12)–(14) then prove


$$
Q_n^{\rm loc}\equiv
(y+1)(y-1)^{n-2}(3y-71-3M)\pmod{3^{m+2}}.
$$


For


$$
j=3^K w,\quad K\ge2,\quad w\ge1,\quad n=4^j+1,
$$


LTE gives $m=v_3(j)\ge K$, and


$$
3M=4^j-1\equiv3j=3^{K+1}w\pmod{3^{K+2}}.
$$


Hence the proposed sharpened law is exactly the law predicted by the **true** jet; no correction to its linear term is needed.

### 6. Primitive normalization and whole error

The local polynomial remains


$$
Q_n^{\rm loc}=3P_n,\qquad
Q_n=(L_n/3)Q_n^{\rm loc},\qquad L_n/3\in\mathbb Z_3^\times.
$$


The unit must not be suppressed. The retained endpoint statement is


$$
Q_n(-1)\ne0,\qquad v_3(Q_n(-1))=2v_3((n-1)!).
$$



None of these local results evaluates the final determinant gcd. For an actual integer clearing $A,B$ of the complete determinant coefficient pair, retain


$$
g=\gcd(|A|,|B|),\qquad q=|B|/g,\qquad
p=-\operatorname{sgn}(B)A/g.
$$


On the domain $B\ne0$, the whole error is


$$
q(e+\pi)-p
=\frac{\operatorname{sgn}(B)}g\bigl(A+B(e+\pi)\bigr)
=\frac{\operatorname{sgn}(B)\ell^k}{g}\det H_{\rm complete},
\qquad k=(n+1)/2.
$$


Polynomial endpoint nonvanishing does not establish nonvanishing or decay of this whole real error.

## Closing ledger

1. **New result and proof status.** The all-depth coefficient/interchange audit passes. The true jets modulo $27$, derivative-tail bounds, and projection transfer modulo $3^{m+2}$ are proved. The integral-force support lemma is proved. The sharpened polynomial law follows conditionally on its complete-coordinate application; the supplied documents assert, but do not fully exhibit, that interface.

2. **Exact remaining bottleneck.** Locally: verify the full regular-force integrality and the exceptional-column-to-$\eta$ coordinate map required by (16). Globally: control the actual final gcd and nonzero whole primitive errors on an infinite index domain. No irrationality conclusion follows.

3. **Computation request.** None. The derivative calculation is reduced explicitly to (9). The remaining local task is an exact symbolic elimination identity, not a large-degree numerical test.
