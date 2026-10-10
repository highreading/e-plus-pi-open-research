> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 — Within-index signed extrapolation: whole-error bound, exact denominator, and positive nondiagonal realization

## 1. Conclusions and proof status

Write


$$
S=e+\pi,\qquad M=1+\sqrt2,\qquad d=b-1,
$$


and retain the complete actual rational columns


$$
u=\frac{U}{d_B},\qquad v=\frac{V}{d_B},
$$


where $U,V\in\mathbb Z^{b+1}$ are jointly primitive. All coordinates below are the original coefficient coordinates $0,\ldots,b$.

Consider


$$
\widehat c
=c_b+\frac{n^2}{d}(c_0-c_b),
\qquad c_j=\frac{V_j}{U_j}.
\tag{1.1}
$$



The conclusions are as follows.

1. **The accepted quantitative CSC gives a genuine polynomial whole-error improvement.** On every integer allocation
   

$$
2\le d=o(n),
$$


   including bounded or arbitrarily slowly growing $d$, and on both parities,
   

$$
\boxed{
   |\widehat c-S|
   \le
   C M^{-2n-b}
   \left(
   \frac{d+1}{n}+\frac{n^2}{d}e^{-\kappa n}
   \right).
   }
   \tag{1.2}
$$


   A sharper interval statement, retaining the amplified CSC remainder, is proved below. This does **not** use the unreviewed common-error expansion in A3turn0.

2. **The accepted CSC does not prove eventual nonvanishing of $\widehat c-S$.** Its uncertainty is larger than the nominal residual after extrapolation. I give the exact zero threshold and an explicit countermodel to the inference from CSC to nonvanishing. This is **not** a disproof of actual-family nonvanishing. That actual-family assertion remains open in this report.

3. **The reduced denominator has an exact endpoint formula with all forced contents removed.** In the notation developed below,
   

$$
\boxed{
   \widehat q
   =\frac{k h|AB|}{F G H},
   }
   \tag{1.3}
$$


   where every factor is an explicitly defined integer gcd or normalized endpoint entry. In particular,
   

$$
\boxed{
   \widehat q\ge \frac{|AB|}{F}
   \ge \frac{|AB|}{a(a-k)}.
   }
   \tag{1.4}
$$


   Thus denominator factors unique to one endpoint cannot be canceled except through the relatively small extrapolation coefficients.

4. **The signed center has an explicit positive rational nondiagonal realization on the complete actual lift.** Its least metric clearer and the content of its integer metric are specified exactly. The metric clearer is not credited as a denominator gain: its forced Gram content is computed and removed.

5. **There are two relevant sharp conditioning costs.**
   - For the endpoint selector acting on every companion vector, the minimum condition number in the stated normalized geometry is asymptotic to
     

$$
8(d+2)\frac{n^4}{d^2}.
$$


   - If the metric may use the actual rational companion $V$, but not $S$, the best condition number among all positive metrics realizing this one center is smaller:
     

$$
\boxed{
     \kappa_{\min}
     =
     \frac{4(d+2)n^4}{\sum_{j=0}^{b}(s_j-\bar s)^2}
     (1+o(1)).
     }
     \tag{1.5}
$$


     For $d\to\infty$, $d=o(n)$, this becomes
     

$$
\kappa_{\min}=48\,\frac{n^4}{d^2}(1+o(1)).
$$



6. **No favorable global $\widehat q\,|\widehat c-S|$ estimate is proved.** The new construction has a proved polynomial error gain and an exact denominator reduction, but not a proved arithmetic gain. The next useful lemma is a specific cancellation congruence at the shared endpoint denominator, not another common saddle coefficient.

The rationality or irrationality of $e+\pi$ remains unresolved.

### Source discipline

I reuse A4turn0’s accepted quantitative CSC and the previously audited all-sublinear whole-error law at their stated scopes. I do not promote A3turn0’s common-error expansion to an accepted theorem.

No new archive search, literature retrieval, hash verification, or arithmetic execution has been performed in this exchange. The supplied overlap gate is retained as a bounded gate, not a universal novelty claim. The generalized Wielandt inequality is used only for its established angle/condition-number consequence.

---

## 2. Accepted inputs and the original finite boundaries

The finite systems remain


$$
H_b,T:\{0,\ldots,d\}^2,\qquad
K:\{0,\ldots,b\}\times\{0,\ldots,d\}.
$$


No inverse or reconstruction matrix is extended beyond these ranges.

Put


$$
e_j=c_j-S.
$$


The accepted CSC states that there are fixed $C,\kappa,\epsilon>0$ and $N$ such that


$$
\left|
\log\frac{e_j}{e_b}+\frac{s_j}{n^2}
\right|
\le R_{n,d},
\tag{2.1}
$$


where


$$
R_{n,d}
=C\frac{d(d+1)}{n^3}+Ce^{-\kappa n},
\tag{2.2}
$$


for


$$
n\ge N,\qquad 2\le d\le\epsilon n,
$$


and


$$
s_0=d,\qquad s_j=b-j\quad(1\le j\le b).
\tag{2.3}
$$


All $u_j$ are nonzero, and all $e_j$ have the common sign $(-1)^{n+1}$.

On the smaller asymptotic domain $d=o(n)$, the accepted whole-error law is


$$
e_b=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1)).
\tag{2.4}
$$


I do not use (2.4) as a uniform equivalence throughout a fixed positive-ratio strip.

The whole coordinate errors are exactly


$$
e_j=
\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac{D}{P_j},
\qquad D=\det H_b,
\tag{2.5}
$$


with the complete exponential force


$$
eE_i
=-[z^{n+i}](1-z+z^2/2)^n
\int_0^1s^n e^{1-s+sz}\,ds
\tag{2.6}
$$


and


$$
E_j=\nu_{n,d}\!\left(
R_j\sum_{i=0}^d
\sigma^i e_{d-i}(z^{-1})eE_i
\right).
\tag{2.7}
$$


Thus the use of whole-error CSC already includes coordinate zero’s endpoint, the complete exponential companion, remote arcs, signed particle sectors, and both minus connectors.

---

## 3. The strongest direct bound furnished by CSC

Set


$$
x=\frac{d}{n^2},\qquad \lambda=\frac1x=\frac{n^2}{d}.
$$


Define the actual centered remainder


$$
r_{n,d}=\log(e_0/e_b)+x.
$$


Then $|r_{n,d}|\le R_{n,d}$, and the signed extrapolation satisfies the exact identity


$$
\boxed{
\frac{\widehat c-S}{e_b}
=
1+\frac{e^{-x+r_{n,d}}-1}{x}.
}
\tag{3.1}
$$



This identity is the appropriate starting point. Substituting only a first-order Taylor term and discarding the amplified remainder would be invalid.

### 3.1 Exact interval consequence

Define


$$
\phi(x)=1-\frac{1-e^{-x}}x.
\tag{3.2}
$$


Since the right side of (3.1) is increasing in $r_{n,d}$,


$$
\boxed{
\phi(x)+\frac{e^{-x}}x(e^{-R_{n,d}}-1)
\le
\frac{\widehat c-S}{e_b}
\le
\phi(x)+\frac{e^{-x}}x(e^{R_{n,d}}-1).
}
\tag{3.3}
$$



This is stronger than a single big-$O$ estimate and is the sharp interval deduction from the accepted information $|r_{n,d}|\le R_{n,d}$.

For $x>0$,


$$
0<\phi(x)\le \frac x2.
$$


Consequently,


$$
\boxed{
|\widehat c-S|
\le
|e_b|
\left[
\frac x2+\frac{e^{-x}}x(e^{R_{n,d}}-1)
\right].
}
\tag{3.4}
$$



On the small-ratio strip, $R_{n,d}\to0$ uniformly as $n\to\infty$, so


$$
|\widehat c-S|
\le
C|e_b|
\left[
\frac{d}{n^2}
+\frac{d+1}{n}
+\frac{n^2}{d}e^{-\kappa n}
\right].
\tag{3.5}
$$


The first term is smaller than the second, but displaying it identifies the nominal residual separately from the uncertainty.

On $2\le d=o(n)$, (2.4) gives (1.2).

**The justified improvement is $O((d+1)/n)$ relative to $e_b$, not a proved leading residual $d/(2n^2)$.**

### 3.2 Complete force identity and amplified residuals

For clarity, the complete evaluated error also has the exact decomposition


$$
\begin{aligned}
\widehat c-S
={}&(-1)^{n+1}
\left[
\lambda\frac{F_0}{P_0}
+(1-\lambda)\frac{F_b}{P_b}
\right]\\
&+\lambda\frac{E_0}{P_0}
+(1-\lambda)\frac{E_b}{P_b}
+(-1)^n\lambda\frac{D}{P_0}.
\end{aligned}
\tag{3.6}
$$



The established factorial bounds imply


$$
\begin{aligned}
\left|
\lambda\frac{E_0}{P_0}
+(1-\lambda)\frac{E_b}{P_b}
+(-1)^n\lambda\frac{D}{P_0}
\right|
\le{}&
C(2\lambda-1)\frac{2^d}{n!\sqrt n}\\
&+C\lambda\frac{\sqrt n}{n!B_0},
\end{aligned}
\tag{3.7}
$$


where


$$
B_0=(n)_d\sigma^{-d}.
$$


Both endpoint and exponential terms are therefore amplified by the signed coefficients before being declared negligible.

Likewise, the remote-arc and connector contribution in the accepted centered estimate becomes


$$
O\!\left(\frac{n^2}{d}e^{-\kappa n}\right)
\tag{3.8}
$$


in (3.5). It may subsequently be bounded by a smaller pure exponential, but it has not been silently left unamplified.

All parity signs in (3.6) are retained.

---

## 4. Nonvanishing: the precise obstruction

### 4.1 The exact zero threshold

For $0<x<1$, equation (3.1) vanishes exactly when


$$
e^{-x+r_{n,d}}=1-x,
$$


or


$$
\boxed{
r_{n,d}=r_*(x):=x+\log(1-x).
}
\tag{4.1}
$$


Its expansion is


$$
r_*(x)=-\frac{x^2}{2}-\frac{x^3}{3}-\cdots.
\tag{4.2}
$$



The accepted remainder has size


$$
R_{n,d}=O\!\left(\frac{d(d+1)}{n^3}\right)
+O(e^{-\kappa n}),
$$


whereas


$$
|r_*(x)|\asymp \frac{d^2}{n^4}.
$$


The ratio of these scales is of order


$$
\frac{n(d+1)}d.
$$


Thus the uncertainty is much larger than the nominal nonzero residual.

In particular, the interval permitted by CSC contains the exact zero threshold for all sufficiently large $n$. Neither the sign nor nonvanishing of $\widehat c-S$ follows from (2.1).

### 4.2 A countermodel to the inference—not to the actual family

The logical failure can be made explicit while preserving rational centers.

Fix a rational number $T$. Choose nonzero rational numbers $a_{n,d}$, with sign $(-1)^{n+1}$, satisfying


$$
a_{n,d}
=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1)).
$$


Such choices exist by density of the rationals. Set


$$
\widetilde c_j
=T+a_{n,d}\left(1-\frac{s_j}{n^2}\right).
\tag{4.3}
$$


Every $\widetilde c_j$ is rational, and


$$
\log\frac{\widetilde c_j-T}{\widetilde c_b-T}
=
-\frac{s_j}{n^2}
+O\!\left(\frac{d^2}{n^4}\right).
\tag{4.4}
$$


This is stronger than the accepted CSC remainder. The common whole-error asymptotic also holds. Nevertheless,


$$
\widetilde c_b+\frac{n^2}{d}
(\widetilde c_0-\widetilde c_b)=T
$$


identically.

This example is not asserted to satisfy the actual contact equations. It proves the narrower, important statement:

> Rationality of the centers, the accepted common-error law, and quantitative CSC do not together establish nonvanishing of the signed extrapolation.

### 4.3 What does follow unconditionally from the accepted estimates?

After reducing $\epsilon$ and increasing $N$, one has $R_{n,d}<x/2$. Therefore


$$
e_0/e_b<1,
$$


and hence


$$
\boxed{c_0\ne c_b.}
\tag{4.5}
$$


In particular, the endpoint minor used below is nonzero.

On every sublinear allocation,


$$
\frac{\widehat c-S}{e_b}\longrightarrow0,
\qquad
\frac{c_j-S}{e_b}\longrightarrow1
$$


uniformly in $j$. Thus $\widehat c$ eventually lies strictly outside the convex hull of all the coordinate centers, on the side toward $S$.

This proves that a positive diagonal realization is impossible eventually. It does not prove $\widehat c\ne S$.

A useful arithmetic alternative to a new analytic coefficient would be


$$
\widehat q\longrightarrow\infty.
\tag{4.6}
$$


Indeed, if $S$ is irrational, no rational center equals it; if $S$ is rational, equality forces the fixed reduced denominator of $S$. Thus (4.6) would itself imply eventual nonvanishing. No such denominator-growth theorem has been proved here.

---

## 5. Exact denominator after all endpoint contents

Reduce the extrapolation coefficient:


$$
g=\gcd(n^2,d),\qquad
a=\frac{n^2}{g},\qquad
k=\frac d g.
\tag{5.1}
$$


Then


$$
\gcd(a,k)=1,\qquad \lambda=\frac ak,\qquad a>k
$$


eventually.

The unreduced endpoint expression is


$$
\widehat c
=
\frac{aV_0U_b+(k-a)V_bU_0}{kU_0U_b}.
\tag{5.2}
$$


Accordingly, with


$$
N_0=aV_0U_b+(k-a)V_bU_0,\qquad
D_0=kU_0U_b,
$$


the first exact formula is


$$
\boxed{
\widehat q=\frac{|D_0|}{\gcd(|D_0|,|N_0|)}.
}
\tag{5.3}
$$



The following reduction exposes all automatic contents.

### 5.1 Remove both endpoint row contents

Let


$$
r_0=\gcd(|U_0|,|V_0|),\qquad
r_b=\gcd(|U_b|,|V_b|),
$$


and write


$$
U_0=r_0u_0,\quad V_0=r_0v_0,\qquad
U_b=r_bu_b,\quad V_b=r_bv_b.
\tag{5.4}
$$


Then


$$
\gcd(u_0,v_0)=\gcd(u_b,v_b)=1.
$$


The factor $r_0r_b$ divides both $N_0,D_0$ and cancels exactly.

Now put


$$
h=\gcd(|u_0|,|u_b|),\qquad
u_0=hA,\qquad u_b=hB,
\qquad \gcd(A,B)=1.
\tag{5.5}
$$


Define


$$
T=a v_0B+(k-a)v_bA.
\tag{5.6}
$$


Then


$$
\boxed{
\widehat c=\frac{T}{k hAB}.
}
\tag{5.7}
$$



Thus an additional factor $h$ has canceled from the raw numerator and denominator.

### 5.2 Cancellation against the coprime endpoint cofactors

Because $v_0$ is coprime to $A$, $v_b$ is coprime to $B$, and $\gcd(A,B)=1$,


$$
\gcd(|A|,|T|)=\gcd(|A|,a),
$$




$$
\gcd(|B|,|T|)=\gcd(|B|,a-k).
$$


Set


$$
F_A=\gcd(|A|,a),\qquad
F_B=\gcd(|B|,a-k),\qquad
F=F_AF_B.
\tag{5.8}
$$


Then


$$
\boxed{\gcd(|AB|,|T|)=F.}
\tag{5.9}
$$


Moreover,


$$
\gcd\!\left(\frac{|AB|}{F},\frac{|T|}{F}\right)=1.
\tag{5.10}
$$



Consequently,


$$
\gcd(kh|AB|,|T|)
=
F\gcd\!\left(kh,\frac{|T|}{F}\right).
\tag{5.11}
$$



This step rules out a potentially misleading claim that an unspecified large numerator cancellation could remove the denominator factors unique to one endpoint.

### 5.3 The extrapolation denominator and endpoint minor

Define the normalized endpoint minor


$$
J=Bv_0-Av_b.
\tag{5.12}
$$


Then


$$
T=aJ+kAv_b.
\tag{5.13}
$$


Since $F\mid a(a-k)$, one has $\gcd(F,k)=1$. Hence


$$
\gcd\!\left(k,\frac{T}{F}\right)
=\gcd(k,T)
=\gcd(k,J).
$$


Put


$$
G=\gcd(k,|J|),
\qquad
H=\gcd\!\left(h,\frac{|T|}{FG}\right).
\tag{5.14}
$$


All displayed divisions are exact. A second elementary gcd reduction gives


$$
\gcd\!\left(kh,\frac{|T|}{F}\right)=GH.
$$


Therefore


$$
\boxed{
\widehat q=\frac{k h|AB|}{FGH},
\qquad
\widehat p
=\operatorname{sgn}(AB)\frac{T}{FGH}.
}
\tag{5.15}
$$


These integers are coprime and $\widehat q>0$.

This is the genuine primitive denominator, not a clearer and not an unreduced Gram norm.

### 5.4 A structural lower bound

Because $G\le k$ and $H\le h$,


$$
\widehat q\ge \frac{|AB|}{F}.
$$


Also $F_A\le a$ and $F_B\le a-k$. Thus


$$
\boxed{
\widehat q\ge\frac{|AB|}{a(a-k)}.
}
\tag{5.16}
$$



Any successful arithmetic argument must therefore control the coprime endpoint denominator pieces $A,B$. A large shared denominator $h$ is potentially cancellable through $H$; large unshared pieces are not, except through the explicit coefficient factors in $F$.

---

## 6. What minor and resultant divisibility actually supplies

The raw endpoint minor is


$$
\Delta_{0b}=U_bV_0-U_0V_b=r_0r_bhJ.
\tag{6.1}
$$


Thus the cancellation of $k$ is controlled by the **normalized** minor $J$, not automatically by the raw minor.

Let


$$
\delta=\gcd_{0\le i<j\le b}|U_iV_j-U_jV_i|
\tag{6.2}
$$


be the content of all $2\times2$ minors. Then


$$
\delta\mid r_0r_bhJ,
$$


so


$$
\boxed{
\frac{\delta}{\gcd(\delta,r_0r_bh)}\mid J.
}
\tag{6.3}
$$


In particular,


$$
\gcd\!\left(
k,\frac{\delta}{\gcd(\delta,r_0r_bh)}
\right)\mid G.
\tag{6.4}
$$



This is a valid forced divisor. It does not identify $G$, and still less does it identify $H$.

The retained actual endpoint constraints are


$$
\sum_jU_j=0,\qquad \sum_jV_j=d_B.
\tag{6.5}
$$


Summing minors against the second index gives


$$
\delta\mid d_BU_i\quad\text{for every }i,
$$


and hence


$$
\delta\mid d_B\,\gcd_j|U_j|.
\tag{6.6}
$$


Again, this is a constraint on minor content, not a global denominator estimate.

There is also an exact degree-one resultant interpretation:


$$
\operatorname{Res}_z(hAz-v_0,\ hBz-v_b)
=hJ.
\tag{6.7}
$$


It is precisely this normalized endpoint resultant that enters the coefficient-denominator cancellation.

No further actual-family resultant theorem in the supplied packet forces


$$
T/(FG)
$$


to be divisible by a large part of $h$. That is the missing congruence. A theorem concerning the full polynomial resultant of $U(t),V(t)$, even if available, would have to be connected to this specific normalized endpoint numerator before it could improve (5.15).

---

## 7. A positive rational nondiagonal metric on the complete lift

Let


$$
m=b+1=d+2,\qquad \mathbf1=(1,\ldots,1)^T,
$$


and use the rational normalized coordinates


$$
x=\operatorname{diag}(U_j^{-1})\,X.
\tag{7.1}
$$


In these coordinates,


$$
U\mapsto\mathbf1,\qquad
V\mapsto c=(c_0,\ldots,c_b)^T.
$$


The normalized geometry is the ordinary Euclidean geometry of $x$. All conditioning assertions below refer explicitly to this geometry, not to the raw coefficient Euclidean geometry.

Define


$$
w=\frac ak e_0+\frac{k-a}{k}e_b,
\qquad \mathbf1^Tw=1.
\tag{7.2}
$$


Then $\widehat c=w^Tc$.

Let


$$
P=I-\frac1m\mathbf1\mathbf1^T.
$$


For any positive rational $\gamma$, set


$$
B=ww^T+\gamma P.
\tag{7.3}
$$


One has


$$
B\mathbf1=w,\qquad
\mathbf1^TB\mathbf1=1.
$$


Also, for nonzero $x$,


$$
x^TBx=(w^Tx)^2+\gamma\|Px\|^2>0.
$$


Indeed, simultaneous vanishing would force $x=t\mathbf1$ and then $w^Tx=t=0$.

Thus $B$ is rational positive definite. Pull it back:


$$
\boxed{
W=\operatorname{diag}(U_j^{-1})\,
B\,
\operatorname{diag}(U_j^{-1}).
}
\tag{7.4}
$$


Then $W$ is rational positive definite on the complete actual lift, and


$$
\boxed{
\frac{u^TWv}{u^TWu}
=
\frac{\mathbf1^TBc}{\mathbf1^TB\mathbf1}
=w^Tc=\widehat c.
}
\tag{7.5}
$$



The construction uses only $n,d,U,V$—in fact this universal selector uses no $V$ except in evaluating the center—and never uses $S$.

The terms on the orthogonal complement in (7.3) are essential: they make the metric positive definite on all $m$ coordinates, rather than merely defining a rank-one endpoint form.

---

## 8. Exact metric clearer, content, and forced Gram cancellation

Choose the conditioning-optimal value for this fixed selector,


$$
\gamma=\|w\|^2.
\tag{8.1}
$$


Write


$$
z=ae_0+(k-a)e_b,\qquad
Z=z^Tz=a^2+(k-a)^2.
$$


Then


$$
B=\frac{C}{mk^2},
\qquad
C=mzz^T+Z(mI-\mathbf1\mathbf1^T).
\tag{8.2}
$$



### 8.1 Content in normalized coordinates

There are at least two interior coordinates because $d\ge2$. An interior off-diagonal entry of $C$ is $-Z$. The endpoint entries then show


$$
\gcd(\text{entries of }C)
=
\gcd(Z,ma^2,ma(k-a),m(k-a)^2).
$$


Since $\gcd(a,k-a)=1$,


$$
\boxed{
c_C:=\gcd(\text{entries of }C)=\gcd(Z,m).
}
\tag{8.3}
$$


Thus


$$
C_0=C/c_C
$$


is primitive integral, and the least scalar clearer of the particular normalized metric $B$ is


$$
mk^2/c_C.
\tag{8.4}
$$



Because scalar multiples do not change the center or condition number, use the raw-coordinate metric


$$
\overline W
=\operatorname{diag}(U_j^{-1})\,C_0\,
\operatorname{diag}(U_j^{-1}).
\tag{8.5}
$$



Its least positive clearer is exactly


$$
\boxed{
\ell
=
\operatorname{lcm}_{0\le i\le j\le b}
\frac{|U_iU_j|}
{\gcd(|U_iU_j|,|(C_0)_{ij}|)}.
}
\tag{8.6}
$$


A zero matrix entry contributes the denominator $1$.

Then


$$
\Omega=\ell\,\overline W
\tag{8.7}
$$


is primitive integral.

To verify the last assertion prime by prime, note that $C_0$ is primitive. For each prime $p$, some entry has valuation zero, so


$$
\min_{i,j}\bigl(v_p((C_0)_{ij})-v_p(U_i)-v_p(U_j)\bigr)\le0.
$$


The least clearer adds precisely the negative of this minimum. Hence the minimum valuation of the resulting integer entries is zero.

### 8.2 Gram coefficients and final gcd

For this primitive integral metric,


$$
\mathcal A=U^T\Omega U
=\ell\,\frac{mk^2}{c_C}>0,
\tag{8.8}
$$


and


$$
\mathcal H=U^T\Omega V=\mathcal A\,\widehat c.
\tag{8.9}
$$


Therefore


$$
\boxed{
g_{\rm Gram}:=\gcd(\mathcal A,|\mathcal H|)
=\frac{\mathcal A}{\widehat q}.
}
\tag{8.10}
$$


Using the raw endpoint expression gives the equivalent exact formula


$$
g_{\rm Gram}
=
\frac{\ell mk}{c_C|U_0U_b|}
\gcd(|kU_0U_b|,|N_0|).
\tag{8.11}
$$


Although the displayed prefactor can be rational, the complete expression is an integer by (8.10).

Thus the metric can have a very large clearer $\ell$, but its forced Gram cancellation removes exactly the amount required to leave the same denominator (5.15). One must not count $\ell$ as either a gain or an unavoidable loss without this cancellation.

Relative to the uncleared actual columns $u,v$, the primitive multiplier is


$$
\frac{d_B^2}{g_{\rm Gram}},
$$


and the whole evaluated form is


$$
\boxed{
\widehat qS-\widehat p
=
\frac{d_B^2}{g_{\rm Gram}}
\bigl[(u^T\Omega u)S-u^T\Omega v\bigr]
=
\widehat q(S-\widehat c).
}
\tag{8.12}
$$



---

## 9. Sharp conditioning: universal endpoint selector

For a prescribed $w$ with $\mathbf1^Tw=1$, define


$$
L=m\|w\|^2\ge1.
$$


The minimum spectral condition number among positive definite $B$ satisfying


$$
B\mathbf1=w
$$


is


$$
\boxed{
K(w)=\bigl(\sqrt L+\sqrt{L-1}\bigr)^2.
}
\tag{9.1}
$$



The classical generalized Wielandt angle inequality gives the lower bound: the angle $\theta$ between $\mathbf1$ and $B\mathbf1=w$ has


$$
\cos\theta=\frac1{\sqrt L},
$$


and any such positive definite map obeys


$$
\kappa(B)\ge\frac{1+\sin\theta}{1-\sin\theta}.
$$


This is (9.1).

The metric


$$
B=ww^T+\|w\|^2P
\tag{9.2}
$$


attains the bound. To check this directly, take the plane spanned by $\mathbf1$ and $w-\mathbf1/m$. After scaling by $m$, its matrix is


$$
\begin{pmatrix}
1&t\\
t&1+2t^2
\end{pmatrix},
\qquad t^2=L-1.
$$


Its eigenvalues are


$$
L\pm\sqrt{L(L-1)}.
$$


The complementary eigenvalues are $L$, so the total condition number is exactly (9.1).

For the endpoint selector,


$$
L=m\left[\left(\frac{n^2}{d}\right)^2
+\left(1-\frac{n^2}{d}\right)^2\right].
$$


Hence


$$
\boxed{
K_{\rm endpoint}
=
\left(\sqrt L+\sqrt{L-1}\right)^2
=
8(d+2)\frac{n^4}{d^2}(1+o(1)).
}
\tag{9.3}
$$



This is sharp for a metric implementing the endpoint functional for every companion vector in this normalized geometry.

---

## 10. A better-conditioned realization using the actual rational companion

The assignment permits a metric chosen without $S$. It may therefore use the actual rational vector $c$. This permits a sharper construction than fixing the endpoint weight vector for every possible companion.

Put


$$
\bar c=\frac1m\mathbf1^Tc,\qquad
z_c=c-\bar c\,\mathbf1,
\qquad
\delta_c=\widehat c-\bar c.
$$


Since $c_0\ne c_b$, $z_c\ne0$.

Among all vectors $w$ satisfying


$$
\mathbf1^Tw=1,\qquad c^Tw=\widehat c,
$$


the vector of minimum Euclidean norm is


$$
\boxed{
w_*=\frac1m\mathbf1
+\frac{\delta_c}{\|z_c\|^2}z_c.
}
\tag{10.1}
$$


This is a rational vector computed entirely from the actual lift.

The positive rational metric


$$
B_*=w_*w_*^T+\|w_*\|^2P
\tag{10.2}
$$


realizes $\widehat c$. It is optimal among **all** positive definite metrics realizing this center on the given pair $(\mathbf1,c)$.

Indeed, after scaling any such metric so that $\mathbf1^TB\mathbf1=1$, its vector $w=B\mathbf1$ satisfies the two constraints above. The angle lower bound is increasing in $\|w\|$, so (10.1) and the equality construction prove optimality.

The exact minimum is


$$
\boxed{
\kappa_{\min}
=
\bigl(\sqrt{1+\mathcal R}+\sqrt{\mathcal R}\bigr)^2,
\qquad
\mathcal R
=
m\,\frac{(\widehat c-\bar c)^2}
{\|c-\bar c\mathbf1\|^2}.
}
\tag{10.3}
$$



No knowledge of $S$ is used in this formula.

### 10.1 Asymptotic conditioning from accepted CSC

Let


$$
\bar s=\frac1m\sum_js_j,\qquad
V_s=\sum_j(s_j-\bar s)^2.
$$


The spread multiset is


$$
\{d,d,d-1,\ldots,1,0\}.
$$


Direct summation gives


$$
\bar s=\frac{d(d+3)}{2(d+2)},
$$




$$
\boxed{
V_s=
\frac{d(d+1)(d^2+7d+4)}{12(d+2)}.
}
\tag{10.4}
$$



On every $2\le d=o(n)$, accepted CSC implies


$$
c_j
=S+e_b\left(1-\frac{s_j}{n^2}
+o\!\left(\frac d{n^2}\right)\right)
$$


uniformly in $j$. Therefore


$$
\|c-\bar c\mathbf1\|^2
=
\frac{e_b^2}{n^4}V_s(1+o(1)).
\tag{10.5}
$$


Meanwhile (3.5) gives


$$
\widehat c-\bar c=-e_b(1+o(1)).
\tag{10.6}
$$


Consequently


$$
\mathcal R=\frac{mn^4}{V_s}(1+o(1)),
$$


which proves (1.5). For growing $d$,


$$
V_s\sim d^3/12,\qquad m\sim d,
$$


so


$$
\kappa_{\min}=48\,\frac{n^4}{d^2}(1+o(1)).
\tag{10.7}
$$



The sharper conditioning does not change the rational center or its reduced denominator.

### 10.2 Exact arithmetic cost for this realization

Write $w_*=z_*/k_*$, where $z_*\in\mathbb Z^m$ is primitive and


$$
k_*=\mathbf1^Tz_*>0.
$$


Set


$$
Z_*=z_*^Tz_*,
\qquad
C_*=mz_*z_*^T+Z_*(mI-\mathbf1\mathbf1^T).
$$


Let


$$
c_*=\gcd(\text{entries of }C_*).
$$


Then use $C_*/c_*$, pull back by $\operatorname{diag}(U_j^{-1})$, and apply the exact least-clearer formula (8.6).

Unlike the sparse endpoint selector, no simpler content formula is asserted for arbitrary $z_*$. The gcd must actually be taken. The same Gram identity (8.10) then proves that the resulting final denominator is still exactly $\widehat q$.

---

## 11. The primitive error budget and the useful next lemma

On every sublinear allocation, the proved upper bound is


$$
\boxed{
|\widehat qS-\widehat p|
\le
C\widehat q M^{-2n-b}
\left(
\frac{d+1}{n}
+\frac{n^2}{d}e^{-\kappa n}
\right).
}
\tag{11.1}
$$


Substituting the exact denominator,


$$
|\widehat qS-\widehat p|
\le
C\frac{k h|AB|}{FGH}
M^{-2n-b}
\left(
\frac{d+1}{n}
+\frac{n^2}{d}e^{-\kappa n}
\right).
\tag{11.2}
$$



This gives a polynomially larger permissible denominator than the unfiltered error bound, but no theorem says that the actual denominator meets that allowance.

Moreover, the lower bound


$$
\widehat q\ge |AB|/[a(a-k)]
$$


shows that the construction cannot hide arbitrarily large unshared endpoint denominators inside a metric clearer or a general primitive-content assertion.

### 11.1 A specific further cancellation lemma

The next arithmetic target should be the following.

> **Shared-endpoint cancellation lemma sought.**  
> On an infinite admissible sublinear sequence, construct integers $h_0$ such that
> 

$$
> h_0\mid h,
> \qquad
> aJ+kAv_b\equiv0\pmod{FGh_0},
> \tag{11.3}
>
$$


> and prove the global cofactor estimate
> 

$$
> \frac{k h|AB|}{FGh_0}
> M^{-2n-b}\frac{d+1}{n}\longrightarrow0.
> \tag{11.4}
>
$$


> In addition, prove either that the resulting actual denominators tend to infinity or that the resulting rational centers are not eventually constant.

Because $h_0\mid H$, this would bound the true reduced denominator from above. The congruence is at the actual shared endpoint denominator, after the row contents, common denominator content, coefficient cancellations, and minor cancellation have all been removed.

This is more specific than requesting “a large gcd.” It identifies the numerator whose residue must vanish:


$$
aJ+kAv_b=T,
$$


the exact modulus available for additional cancellation, and the cofactor whose size matters.

The whole-minor content can contribute to $G$, but it does not by itself prove (11.3). A local valuation at one prime would establish only one component of this all-prime statement.

The nonconstancy or denominator-growth clause is indispensable because the signed error has no proved nonzero leading coefficient.

---

## 12. Bounded exact-arithmetic calculation for coordinator inspection

No arithmetic has been executed. The following bounded calculation would test the denominator mechanism and certify individual metric realizations without pretending to establish an infinite theorem.

### 12.1 Inputs

Use the 16 index pairs


$$
n\in\{64,65,128,129\},
\qquad
d\in\{2,3,4,8\},
\qquad b=d+1.
$$


For each pair, supply:

- the actual $d_B,U,V$ from the original finite construction;
- provenance identifying the actual finite contact and reconstruction ranges;
- verification of
  

$$
\gcd(\text{entries of }[U,V])=1,\quad
  \sum U_j=0,\quad \sum V_j=d_B;
$$


- all $U_j\ne0$, or a report that the selected record is ineligible.

The packet does not provide these numerical integer columns. Their generation must use the actual finite construction, not an inferred or truncated asymptotic model.

### 12.2 Required normalization divisions

For every eligible record:

1. Divide $n^2,d$ by $g=\gcd(n^2,d)$.
2. Divide the two endpoint rows by $r_0,r_b$.
3. Divide the endpoint denominators by $h$.
4. Compute $F,G,H$ in the order (5.8), (5.14), certifying each exact division.
5. Compute the raw fraction (5.2) and independently reduce it by one final gcd.
6. Verify agreement with (5.15).
7. Compute the full minor content $\delta$ and verify (6.3).
8. Construct $C_0$, the least metric clearer $\ell$, and $\Omega$.
9. Verify primitive metric content, positive definiteness by exact rational $LDL^T$, and
   

$$
\mathcal H/\mathcal A=\widehat p/\widehat q,
   \qquad
   \gcd(\mathcal A,|\mathcal H|)=\mathcal A/\widehat q.
$$



Optionally repeat the metric check for the optimal actual-pair metric $B_*$, retaining its actual content gcd.

### 12.3 Expected verifiable output

For each record return:

- $a,k,r_0,r_b,h,A,B,v_0,v_b,J,T,F,G,H$;
- the reduced $(\widehat p,\widehat q)$;
- the exact identities
  

$$
\widehat q=\frac{k h|AB|}{FGH},
  \qquad
  \widehat q\ge |AB|/F;
$$


- $\delta$ and the normalized minor divisor in (6.3);
- the least metric clearer, integer metric content, and exact Gram gcd;
- exact rational expressions for the conditioning parameters $L$ and $\mathcal R$.

These outputs would reveal whether cancellation occurs principally in $F$, $G$, or the genuinely interesting factor $H$.

### 12.4 Optional whole evaluated-error certificate

Individual signs can be checked without numerical integration.

Use:

- the rational partial sum $\sum_{r=0}^{512}1/r!$ with its standard positive factorial tail bound for $e$;
- Machin’s identity
  

$$
\pi=16\arctan(1/5)-4\arctan(1/239),
$$


  with 512 terms of each alternating series and the next-term error bounds.

This produces an exact rational interval for $S$. Return intervals for both


$$
\widehat c-S
\quad\text{and}\quad
\widehat qS-\widehat p.
$$


If an interval excludes zero, it certifies that individual whole error and its sign. If it contains zero, the output must be “inconclusive at the prescribed bound,” not a presumed sign.

A finite list of nonzero errors would not prove eventual nonvanishing.

### 12.5 Resource scale

Here $m\le10$. Excluding generation of the actual columns, the task requires only fixed-size integer vectors, at most $45$ minors per record, small rational matrices, gcds, lcms, and exact $LDL^T$.

If $L$ is the maximum input bit length, the arithmetic uses integers of $O(mL)$ bits, with conservative fixed constants, and a few thousand arithmetic/gcd operations per record. Streaming storage is polynomial in $m,L$; no length-$n$ matrix inverse or prime factorization is required. The optional rational interval calculation adds only fixed factorial and power-series arithmetic.

These are operation-count estimates, not measured runtimes.

---

## 13. Final ledger

### New results proved here

- The exact amplified CSC interval (3.3) and the whole-error bound (1.2).
- Eventual endpoint separation $c_0\ne c_b$, and eventual location of $\widehat c$ outside the convex hull of all coordinate centers.
- The exact reduced denominator formula
  

$$
\widehat q=k h|AB|/(FGH),
$$


  including row contents, common endpoint denominator, coefficient cancellation, normalized minor cancellation, and final shared-denominator gcd.
- An explicit positive rational nondiagonal metric on the complete actual lift.
- Its least metric clearer, primitive metric content, and exact forced Gram gcd.
- Sharp conditioning formulas in the explicitly stated normalized geometry, both for the universal endpoint selector and for the best actual-pair realization.

### What remains unproved

- Eventual nonvanishing of the actual signed error $\widehat c-S$.
- Any upper bound for the actual reduced denominator strong enough to make the whole primitive error tend to zero.
- The specific shared-endpoint congruence and cofactor estimate (11.3)–(11.4).

### Decisive obstruction and next step

The analytic cancellation removes the common error but amplifies the accepted centered uncertainty by $n^2/d$. Its nominal $d/(2n^2)$ residual is not a justified leading term.

The arithmetic formula is now sufficiently explicit to identify a different, concrete target: cancellation of


$$
aJ+kAv_b
$$


modulo a large part of the shared reduced endpoint denominator $h$, while controlling the coprime endpoint pieces $A,B$.



$$
\boxed{
\text{This construction presently supplies polynomial error gain, not a proved improved primitive-error budget.}
}
$$





$$
\boxed{
\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}
}
$$


