> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3: cylinder identification, the first corrected transition zero, and continuation beyond the next critical value

I obtain three new results:

1. The transition profile is exactly a positive constant times
   

$$
-e^{\tau^2/(4a)}D_{3/2}(-\tau/\sqrt a).
$$


   It has **exactly two real zeros, both simple**, one on each side of zero.

2. The next coefficient of the actual degree-three density can be calculated explicitly. It yields a uniform first correction to the transition profile and an explicit necessary lattice condition for cancellation.

3. The original paired-branch criterion does **not** cover the whole negative-dominant range if it is restricted to the total-density interval $(-r,-2\rho^3)$. However, splitting the actual density by the signs of its two circle factors gives a stronger continuation argument. This proves that **some even Morse coefficient survives at every fixed negative-dominant interior order**. This assertion does not, by itself, control arbitrary integer rounding at exceptional orders.

The special-function zero count below uses the standard real-zero theorem for parabolic cylinder functions, not numerical root evidence. The density calculations use the supplied actual weights. No irrationality conclusion follows.

## 1. Exact special-function identity

Retain


$$
b=\sqrt2,\quad M=1+b,\quad \rho=M^{-1},\quad
r=2M,\quad h=5-r,\quad c_0=h/r,
$$


and


$$
a=\frac5{r^2h},\qquad
A=-2bM,\qquad K=\frac{e^{-2b}}{\pi M b^{3/2}}.
$$


Put


$$
E_\tau(x)=e^{-ax^2/2+\tau x},\qquad
I(\tau)=\int_0^\infty x^{1/2}E_\tau'''(x)\,dx .
$$


The actual profile is


$$
\Psi(\tau)=(-r)^3AK\,I(\tau).
$$



For $\Re \nu>0$, the standard cylinder integral is


$$
\int_0^\infty x^{\nu-1}e^{-ax^2/2+\tau x}\,dx
=\Gamma(\nu)a^{-\nu/2}e^{\tau^2/(4a)}
 D_{-\nu}(-\tau/\sqrt a).
$$


Here


$$
D_\lambda(z)=U(-\lambda-\tfrac12,z).
$$



Regularized integration by parts gives


$$
I(\tau)=-\frac38\,\operatorname{FP}
 \int_0^\infty x^{-5/2}E_\tau(x)\,dx .
$$


One way to justify this without informal endpoint manipulations is to integrate from $\epsilon$ to infinity three times, subtract the resulting explicit powers of $\epsilon$, and pass to the limit. Equivalently, continue the Mellin integral meromorphically to $\nu=-3/2$. The original integral defining $I$ is convergent.

Since $\Gamma(-3/2)=4\sqrt\pi/3$,


$$
\boxed{
I(\tau)=-\frac{\sqrt\pi}{2}a^{3/4}
 e^{\tau^2/(4a)}D_{3/2}(-\tau/\sqrt a).
}
$$


Consequently


$$
\boxed{
\Psi(\tau)=
-\frac{\sqrt\pi}{2}(-r)^3AK\,a^{3/4}
 e^{\tau^2/(4a)}D_{3/2}(-\tau/\sqrt a).
}\tag{1}
$$


The constant $(-r)^3AK$ is strictly positive. Both its sign and the negative cylinder argument matter.

The classical real-zero theorem for $D_\nu$, equivalently $U(-\nu-\tfrac12,\cdot)$, gives exactly two real zeros for $\nu=3/2$. They are simple. Simplicity also follows directly from


$$
D_\nu''(z)+(\nu+\tfrac12-z^2/4)D_\nu(z)=0:
$$


a common zero of a solution and its derivative would force the solution to vanish identically.

Together with $\Psi(0)>0$ and the negative signs on the two distant tails, this gives


$$
\boxed{\text{\(\Psi\) has exactly two simple real zeros }
\tau_-<0<\tau_+.}\tag{2}
$$


This uses an existing infinite zero theorem; no root computation is involved.

## 2. The missing actual density coefficient

Write $t_1,t_2,y$ for the signed local angular coordinates and the nonnegative Heine coordinate at the negative endpoint. Set


$$
R^2=t_1^2+t_2^2+y^2,\qquad s=T+r.
$$


The map has expansion


$$
s=bR^2+Q_4+O(R^6),
$$


where


$$
\begin{aligned}
Q_4={}&-\frac b{12}(t_1^4+t_2^4)
+\left(\frac b{12}-\frac{b^2}{2M}\right)y^4\\
&-\frac{b^2}{2M}
 \left(t_1^2t_2^2+t_1^2y^2+t_2^2y^2\right).
\end{aligned}\tag{3}
$$


The relative quadratic correction to the product measure is


$$
L_2=\frac{b-2}{2}(t_1^2+t_2^2)-\frac b{2M}y^2.
$$


Using spherical averages, which are unchanged on the hemisphere for these even polynomials,


$$
\langle L_2\rangle=\frac{b-2}{3}-\frac b{6M},
\qquad
\langle Q_4\rangle=-\frac b{60}-\frac{b^2}{5M}.
$$


Radial inversion of $s=bR^2+Q_4+\cdots$ therefore gives the measure-density correction


$$
\boxed{
\ell=\frac{\langle L_2\rangle}{b}
-\frac{5\langle Q_4\rangle}{2b^2}
=\frac{8b-15}{24b}+\frac1{3M}.
}\tag{4}
$$



The actual degree-three weight is


$$
A_3=u(3F+G)-2B.
$$


At the corner $F=O(R^4)$. To obtain the quadratic term, let
$\delta_i=v_i+M$. The weight derivatives are


$$
q'(-M)=1-2b,\qquad h'(-M)=8-4b,
$$


and differentiation of the supplied symmetric expression for $G$ gives


$$
G=-M^2+M(1-2b)(\delta_1+\delta_2)+O(R^4).
$$


It follows that


$$
A_3=A+3b^2(t_1^2+t_2^2)-by^2+O(R^4).
$$


Its averaged quadratic correction, expressed in the variable $s$, is


$$
\frac{6b^2-b}{3b}=2b-\frac13.
$$



Thus the coefficient previously left inside an $O(s^{3/2})$ is explicit:


$$
\boxed{
f_3(-r+s)=K\left(As^{1/2}+B_3s^{3/2}+O(s^{5/2})\right),
\qquad
B_3=A\ell+2b-\frac13.
}\tag{5}
$$


The required other coefficients are


$$
f_2(-r+s)=3AKs^{1/2}+O(s^{3/2}),\qquad
f_4(-r+s)=KC_4s^{5/2}+O(s^{7/2}),
$$


where


$$
C_4=\frac{1-2b}{15M}.
$$



These are coefficients of the actual pushforward densities, not amplitudes inferred from a proposed asymptotic.

## 3. Uniform next transition coefficient

Use the actual scaled parameter


$$
\tau=\frac{m-c_0n}{h\sqrt n}.
$$


This convention retains integer rounding exactly.

Let $\epsilon=n^{-1/2}$, and put


$$
\gamma=\frac{\phi'''(-r)}6
=\frac13\left(-\frac1{r^3}+\frac{c_0}{h^3}\right),
\qquad
Q_\tau(x)=\gamma x^3-\frac{\tau}{2h}x^2.
$$


For $s=\epsilon x$, the normalized kernel is


$$
E_\tau(x)\left(1+\epsilon Q_\tau(x)+O(\epsilon^2)\right)
$$


in Gaussian-weighted derivative norms.

For precision about the quartic phase, the order-$\epsilon^2$ exponent is


$$
-\frac14\left(\frac1{r^4}+\frac{c_0}{h^4}\right)x^4
+\frac{\tau}{3h^2}x^3.
\tag{6}
$$


It affects the next, relative $n^{-1}$, coefficient—not the first relative $n^{-1/2}$ coefficient. Its control is included in the error below.

Directly expanding


$$
D^3=T^3\partial_s^3+3T^2\partial_s^2+T\partial_s
$$


and the degree-two and degree-four terms gives


$$
\boxed{
\mathcal Z_{n,m}
=(-1)^nr^nh^mn^{3/4}
\left[\Psi(\tau)+n^{-1/2}\Xi(\tau)+O(n^{-1})\right],
}\tag{7}
$$


uniformly for $\tau$ in a fixed compact real interval, where


$$
\begin{aligned}
\Xi(\tau)=K\bigg\{&
-r^3A\int_0^\infty x^{1/2}(Q_\tau E_\tau)'''dx\\
&-r^3B_3\int_0^\infty x^{3/2}E_\tau'''dx
+3r^2A\int_0^\infty x^{3/2}E_\tau'''dx\\
&+6r^2A\int_0^\infty x^{1/2}E_\tau''dx
+r^4C_4\int_0^\infty x^{5/2}E_\tau''''dx
\bigg\}.
\end{aligned}\tag{8}
$$


Every integral in (8) is convergent.

The coefficient $6r^2A$ includes **both** the lower derivative in $D^3$ and the leading $f_2D^2$ contribution. Degrees one and zero enter only at smaller orders. Formula (8) also retains the next $f_3$ density, the leading $f_4$ density, and the phase correction.

The same Gaussian localization as in the supplied transition proof gives (7). The positive-support contribution remains exponentially separated. The entire exponential correction, including the adjacent truncation term and the separate $H_{k+1}W_k$ contraction, remains bounded by


$$
C(N+1)^4\frac{d^n}{n!}
 \left(5+\frac d{n+1}\right)^m,\qquad N=n+m,
$$


and is negligible at the displayed orders.

### Corrected zero and necessary integer condition

For either $\tau_j\in\{\tau_-,\tau_+\}$, simplicity gives the corrected scaled zero


$$
\boxed{
\tau_j^{\mathrm{corr}}(n)
=\tau_j-\frac{\Xi(\tau_j)}{\Psi'(\tau_j)\sqrt n}
+O(n^{-1}).
}\tag{9}
$$


In terms of the integer filter order, complete cancellation near this root necessarily requires


$$
\boxed{
m=c_0n+h\tau_j\sqrt n
-h\frac{\Xi(\tau_j)}{\Psi'(\tau_j)}
+O(n^{-1/2}).
}\tag{10}
$$


This is a necessary condition, not a sufficient one. Higher coefficients and the whole remainder still matter.

In particular, an eventual separation


$$
\operatorname{dist}\!\left(
c_0n+h\tau_j\sqrt n
-h\frac{\Xi(\tau_j)}{\Psi'(\tau_j)},\mathbb Z
\right)\gg n^{-1/2}
$$


would rule out complete cancellation in that root window. No such infinite lattice-separation statement is proved here.

## 4. The original phase-pair criterion does not cover the entire range

Put $k=2\rho^3$. The right branch reaches the endpoint phase before $T=-k$ precisely when


$$
\phi_c(-k)<\phi_c(-r),
$$


or


$$
c<
c_{\mathrm{pair}}
:=\frac{\log(r/k)}{\log((5-k)/h)}.
\tag{11}
$$


Thus the original criterion has a precise finite boundary.

It does not cover all of $(c_0,c_{\mathrm s})$. For example $c=5/4$ satisfies both


$$
B_-(5/4)>B_+(5/4),\qquad
k(5-k)^{5/4}>rh^{5/4}.
\tag{12}
$$


These are exact radical inequalities: raising to the fourth power reduces them respectively to


$$
(20/9)^4(25/9)^5>(2\rho)^4(5+2\rho)^5,
$$


and


$$
(2\rho^3)^4(5-2\rho^3)^5>(2M)^4(5-2M)^5.
$$


They can be checked in $\mathbb Q(\sqrt2)$, using $\rho^2+2\rho=1$. The first places $5/4<c_{\mathrm s}$; the second places $5/4>c_{\mathrm{pair}}$.

## 5. Stronger continuation: separate the two actual negative components

There is a useful distinction between the **total density** and the component germ that occurs at a negative-dominant saddle.

For $T<0$, the two circle factors have the same sign. Split each actual measure into


$$
\mu_h^{--}\quad(v_1<0,\ v_2<0),\qquad
\mu_h^{++}\quad(v_1>0,\ v_2>0).
$$


Their supports satisfy


$$
\operatorname{supp}\mu_h^{++}\subset[-k,0].
$$


Hence throughout $(-r,-k)$,


$$
f_h=f_h^{--}.
\tag{13}
$$



Crucially, all $f_h^{--}$ are real analytic on the larger interval


$$
\boxed{(-r,0).}\tag{14}
$$


Indeed, at a nonzero value the boundaries $v_i=0$ cannot occur. Over compact subintervals away from zero, both the Heine variable and the circle factors are bounded away from their problematic limits. The restricted map is proper there. Its only nonzero critical value in this sign component is $-r$, so the proper analytic-submersion argument applies on $(-r,0)$.

Define


$$
\mathcal F^{--}=\sum_{h=0}^4(D^*)^hf_h^{--}.
$$


It has the known nonzero singularity at $-r$, and is analytic everywhere else in $(-r,0)$.

Every negative-dominant saddle lies below $-k$, so its total effective amplitude equals $\mathcal F^{--}$ in a neighborhood. Suppose all its even Morse coefficients vanished. Then the phase-pair identity would hold for $\mathcal F^{--}$. Continue the two branches down to the phase level $\phi_c(-r)$. The right branch reaches a point strictly between the saddle and zero. At that point $\mathcal F^{--}/\phi_c'$ is finite; on the left it diverges with the nonzero endpoint singularity. Contradiction.

Therefore


$$
\boxed{
\text{At every fixed }c\in(c_0,c_{\mathrm s}),
\text{ at least one even Morse coefficient is nonzero.}
}\tag{15}
$$


This removes complete odd-Morse cancellation as an explanation for any member of the finite exceptional set. It does not yet give uniform lower bounds for arbitrary moving integer saddles near those exceptional orders.

### What happens at the next actual critical value?

At $(v_1,v_2,y)=(\rho,\rho,0)$, put $s=T+k$. Then


$$
s=b\rho^2(t_1^2+t_2^2)+b\rho^4y^2+O(R^4).
$$


The new component starts on the **right** of $-k$. Its measure coefficient is


$$
K_{++}=\frac{e^{2b}}{\pi b^{3/2}\rho^3}>0.
$$


At that corner,


$$
F=0,\quad G=-\rho^2,\quad B=\rho^2,\quad D_0=0,
$$


so


$$
A_3^{++}=2\rho^3-2\rho^2=-2\rho^2(1-\rho)\ne0.
$$


Consequently, from the right,


$$
\boxed{
\mathcal F^{++}(-k+s)
=\frac38 k^3K_{++}A_3^{++}s^{-5/2}
+O(s^{-3/2}).
}\tag{16}
$$


The leading degree-four weight again vanishes to fourth angular order, so it cannot cancel (16). The background $\mathcal F^{--}$ is analytic there and cannot cancel it either.

Thus the next critical singularity has the **same leading half-integer exponent**, not an unequal one. More importantly, it belongs to a newly appearing component. Using it as if it obstructed continuation of the original analytic germ would be invalid. The sign-component argument above supplies the correct continuation instead.

## 6. Arithmetic scope retained

For $n\ge2,m\ge0$, $N=n+m$, retain


$$
L_N=2^{N+1}(2N+2)!(N!)^4,\quad
U=L_N\mathcal H_{n,m},\quad V=L_N\mathcal J_{n,m},
$$




$$
g=\gcd(|U|,|V|),\qquad
P=-\operatorname{sgn}(V)U/g,\qquad q=|V|/g.
$$


These are used only where the inherited endpoint theorem ensures $V\ne0$. The exact whole primitive error remains


$$
\boxed{
q(e+\pi)-P=q\,\frac{\mathcal Z_{n,m}}{\mathcal J_{n,m}}.
}
$$


Formula (7) proves eventual nonvanishing on compact transition sets separated from the two roots. Near either root, (10) is only a necessary cancellation condition. No new unconditional primitive-growth or primitive-shrinking statement is asserted there.

## Closing ledger

### (1) New result and proof status

**Proved from the stated exact weights and standard special-function formulas:** identity (1), exactly two simple profile zeros, explicit density coefficient (5), uniform first correction (7)–(8), and corrected-zero condition (9)–(10).

**Proved:** the restricted total-density pairing criterion misses part of the negative-dominant range; nevertheless sign-component continuation proves survival of some even Morse coefficient at every fixed order in that range. The next actual critical singularity is (16), with a nonzero signed coefficient.

### (2) Exact remaining bottleneck

Near the two transition roots, the bottleneck is quantitative proximity of the actual integer $m$ to the explicit corrected expression (10), together with further uniform coefficients if that proximity is exceptionally small.

At the finite interior-amplitude exceptions, complete odd cancellation is now ruled out, but arbitrary integer rounding still requires a uniform moving-saddle analysis.

Independently, no adequate upper control of the actual final gcd-reduced denominator has been supplied for an irrationality proof. Irrationality of $e+\pi$ remains undecided.

### (3) Computation request

**None required for the stated analytical conclusions.** A useful bounded independent audit would expand (3)–(5) and reduce the two radical inequalities following (12) exactly in $\mathbb Q(\sqrt2)$. Such a receipt would check algebra only; it would not settle either infinite lattice-proximity problem.
