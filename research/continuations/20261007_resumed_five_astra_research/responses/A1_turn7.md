> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The adjacent depth-$26$ window: exact residue reduction and an unavoidable radical

## Abstract

The proposed adjacent window


$$
\frac{147968}{59049}<\frac{\Omega}{D}<3
$$


does contain infinitely many original indices. It removes the macroscopic zero rows caused by the degree band in the window above $3$, but it does **not** produce an almost nonsingular depth-$26$ matrix.

The obstruction comes from the original ternary word, not from a choice of unfavorable auxiliary digits. On the original progression,


$$
s=\frac D{486}\equiv1\pmod9,
$$


whereas, for sufficiently large $h$,


$$
c'=\frac{3^{h-31}-1}{2}\equiv4\pmod9.
$$


These congruences force **every square equal-sector Hankel block to be singular modulo $3$**. There are $241$ such sectors. The remaining unequal pair contributes at least one further radical direction. Consequently the explicit depth-$26$ Hankel candidate satisfies


$$
\boxed{\dim_{\mathbb F_3}\ker K_{26}\ge242.}
$$


In particular, neither rank $\nu-1$ nor a nonzero first bordered cofactor modulo $3$ is possible anywhere in this sufficiently large adjacent original window.

The proof uses the classical binomial determinant product, including its factorial valuation payments. An exact recursive description of the sector kernels and their endpoint restrictions is also given. It does not yet bound the radical dimension from above or evaluate a paid next Schur digit. The actual depth-$26$ identification remains conditional on the retained hypotheses stated in the sources, especially the stronger linear perturbation estimate not independently established by A4 turn4.

No rationality or irrationality conclusion for $e+\pi$ follows.

---

## 1. Original objects and the scope of the result

Retain exactly


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1,\qquad A=4^j-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


and


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$


The finite coordinates remain


$$
U_u=(y-1)^u\quad(0\le u<D),\qquad
z_i=(y-1)^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),
\qquad
\nu=\frac D2-1,\qquad d=D+\nu.
$$


The physical terminal is $Y_m$, not an infinite continuation.

The complete functional remains


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad \mathfrak f(y^r)=(2r)!,
$$


with the original cutoff


$$
2v+1\le4H-4D+5.
$$



The object analyzed below is the explicit finite matrix


$$
K_{ij}=-[y^{c-i-j}](y-1)^D,\qquad 0\le i,j<\nu,
\tag{1.1}
$$


over $\mathbb F_3$, where


$$
\Omega=H/3^{25},\qquad c=(\Omega-1)/2.
$$



The sector analysis is an unconditional algebraic theorem about (1.1) on the stated original indices. Its application to


$$
U=-S_{\rm act}/3^{26}
$$


requires the candidate identification $\bar U=K$.

### Source audit qualification

The stationary Gram identity in A1 turn6 is valid under its stated integral-basis, orthogonality and integrality assumptions: expanding $F^*=F+3^p\Delta$ gives exactly the claimed quadratic error payment.

However, the supplied independent audit A4 turn4 establishes only


$$
\Phi_R\in3^{20}M.
$$


Identification of the **actual** depth-$26$ digit additionally uses


$$
\Phi_R\in3^{21}M.
$$


A1 turn6 attributes this stronger estimate to retained earlier mathematics whose proof is not attached here. Likewise, its nested corrected-column support theorem is a retained input. The present report does not promote these hypotheses to independently audited conclusions.

The exact actual-block identity


$$
E_{\rm act}-E_c=3^7J
$$


is separately supported by the receipt and A4 turn4. It does not, by itself, supply the stronger linear estimate.

---

## 2. Infinite original scope of the adjacent window

Choose any closed interval strictly inside


$$
\left(\frac{147968}{59049},3\right)
$$


for $\Omega/D$. This corresponds to a nonempty interval strictly inside the original $D/H$-window.

Put


$$
\alpha=\log_3 4.
$$


It is irrational: rationality would imply an equality between positive powers of $4$ and $3$. Along


$$
j=84645+531441k,\qquad k\ge0,
$$


the fractional parts of $j\alpha$ are dense, and visit every nonempty open interval infinitely often.

For $N=\lceil j\alpha\rceil$, set $H=3^N$. Then


$$
\frac DH=1-3^{j\alpha-N}+3^{-N}.
$$


The final summand tends to zero. Strict interior margins therefore give infinitely many original indices in the proposed adjacent window.

This establishes real-window density only. The congruences used below are proved separately on the original progression; none is inferred from density.

---

## 3. Original word constraints

Write


$$
D=486s.
$$


The original valuation $v_3(D)=5$ implies $3\nmid s$.

For sufficiently large $h$,


$$
\Omega=3^{h-26}=243\,3^{h-31},
$$


so


$$
c=243c'+121,\qquad
c'=\frac{3^{h-31}-1}{2}.
\tag{3.1}
$$


In particular, when $h\ge33$,


$$
c'\equiv4\pmod9.
\tag{3.2}
$$



A second constraint is crucial.

### Lemma 3.1
On the original progression, for sufficiently large $h$,


$$
\boxed{s\equiv1\pmod9.}
$$



### Proof

The progression gives $j\equiv81\pmod{729}$. By the lifting-the-exponent identity,


$$
v_3(4^{729}-1)=7.
$$


Thus $4^j\equiv4^{81}\pmod{3^7}$.

Expand


$$
4^{81}=(1+3)^{81}.
$$


After division by $243$, the first three terms beyond the constant are


$$
1,\qquad120,\qquad9480.
$$


Their sum is $7\pmod9$. Every term with $k\ge4$ vanishes modulo $9$ after this division: indeed


$$
v_3\binom{81}{k}=4-v_3(k)
$$


for $0<k<81$, and


$$
k-1-v_3(k)\ge2\qquad(k\ge4).
$$


The terminal term also has more than sufficient valuation. Hence


$$
\frac{4^j-1}{243}\equiv7\pmod9.
$$


Since $H/243\equiv0\pmod9$ eventually,


$$
2s=\frac D{243}\equiv-7\equiv2\pmod9,
$$


proving the claim. ∎

---

## 4. Exact $243$-sector reduction

In characteristic $3$,


$$
(y-1)^D=(y^{243}-1)^{2s}.
\tag{4.1}
$$


Write original residual indices as


$$
i=a+243u,\qquad j=b+243v,\qquad 0\le a,b\le242.
$$


Because


$$
\nu=243s-1,
$$


the sector lengths are


$$
n_a=
\begin{cases}
s,&0\le a\le241,\\
s-1,&a=242.
\end{cases}
\tag{4.2}
$$



An entry can be nonzero only if


$$
a+b\equiv121\pmod{243}.
$$


The only possibilities are $a+b=121$ or $364$. Define


$$
\epsilon_{ab}=\frac{a+b-121}{243}\in\{0,1\}.
$$


Then the exact block is


$$
\boxed{
K_{(a,u),(b,v)}
=-[z^{c'-\epsilon_{ab}-u-v}](z-1)^{2s}.
}
\tag{4.3}
$$



The involution pairing sectors is


$$
a\longmapsto121-a\pmod{243}.
$$


It has one fixed point, $a=182$. The unequal pair is precisely


$$
122\longleftrightarrow242.
$$


After deleting these two sectors, there remain $241$ equal-length sectors: $120$ paired couples and one fixed sector.

### Signs

For $T=c'-\epsilon_{ab}$, put


$$
B_s(T)_{uv}=\binom{2s}{T-u-v},
$$


where out-of-range binomial coefficients are zero. Since $2s$ is even, (4.3) is


$$
-(-1)^T(-1)^u(-1)^v B_s(T)_{uv}.
\tag{4.4}
$$


Thus the signs are removed by explicit invertible diagonal matrices; they do not alter ranks or kernel dimensions.

### Endpoint

Under the candidate actual endpoint transport,


$$
\bar e_i=(-1)^i.
$$


In sector coordinates this is


$$
\boxed{\bar e_{a,u}=(-1)^{a+u}.}
\tag{4.5}
$$


After the diagonal sign change used in (4.4), it becomes the constant vector with value $(-1)^a$ in sector $a$.

For a kernel vector represented by


$$
X_a(z)=\sum_{u=0}^{n_a-1}x_{a,u}z^u
$$


in the original signed coordinates, its endpoint observation is exactly


$$
(-1)^aX_a(-1).
\tag{4.6}
$$


This retains the actual endpoint projection; it is not replaced by a generic nonzero vector.

---

## 5. Classical determinant product with all factorial payments

For the equal sectors, reverse the row ordering of $B_s(T)$. With


$$
L=T-s+1,\qquad B=2s-L,
$$


the resulting matrix is


$$
\left(\binom{2s}{L+u-v}\right)_{0\le u,v<s}.
$$


The classical binomial determinant identity gives


$$
\det\left(\binom{2s}{L+u-v}\right)
=
\prod_{i=0}^{s-1}
\frac{(2s+i)!\,i!}{(L+i)!\,(B+i)!}.
\tag{5.1}
$$


The original row reversal contributes $(-1)^{s(s-1)/2}$; the additional signs in (4.4) are units.

Strict interior margins in the adjacent window imply, eventually,


$$
2s<T<3s-1
$$


for both $T=c'$ and $T=c'-1$. Hence $L,B\ge0$, and all factorial arguments in (5.1) are valid. The rational product is a nonzero integer determinant over characteristic zero.

Its exact ternary valuation is


$$
\sum_{k\ge1}\sum_{i=0}^{s-1}
\left(
\left\lfloor\frac{2s+i}{3^k}\right\rfloor+
\left\lfloor\frac{i}{3^k}\right\rfloor-
\left\lfloor\frac{L+i}{3^k}\right\rfloor-
\left\lfloor\frac{B+i}{3^k}\right\rfloor
\right).
\tag{5.2}
$$


No denominator factorial has been treated as a unit without payment.

### Lemma 5.1
Every individual $k$-layer in (5.2) is nonnegative.

### Proof

Let $q=3^k$, and write $L=q\lambda+l$, $B=q\mu+b$, with $0\le l,b<q$. The summand is periodic in $i$ with period $q$, and its sum over a full period is zero.

For the remaining initial segment, if $l+b<q$, the summand has the successive pattern


$$
0,\quad +1,\quad0,\quad-1,
$$


with the positive interval preceding the negative interval and equal total lengths. Every initial partial sum is nonnegative.

If $l+b\ge q$, the pattern is


$$
+1,\quad0,\quad-1,\quad0,
$$


again with equal positive and negative total lengths. The same conclusion follows. ∎

---

## 6. The forced singularity at the $9$-layer

Use the original constraints


$$
s\equiv1,\qquad c'\equiv4\pmod9.
$$



For $T=c'$,


$$
L\equiv4,\qquad B\equiv7,\qquad 2s\equiv2\pmod9.
$$


For $T=c'-1$,


$$
L\equiv3,\qquad B\equiv8,\qquad 2s\equiv2\pmod9.
$$


In both cases $L+B$ has one carry modulo $9$.

Since $s\equiv1\pmod9$, full $9$-periods contribute zero and the remaining initial segment consists only of $i=0$. Its contribution is $1$. Therefore the $k=2$ layer of (5.2) equals $1$.

By Lemma 5.1 the other layers cannot cancel this payment. Thus


$$
\boxed{
v_3\det B_s(c')\ge1,\qquad
v_3\det B_s(c'-1)\ge1.
}
\tag{6.1}
$$



This is a uniform original-word obstruction, not a finite experimental observation.

### Theorem 6.2 — Failure of the almost-full-rank proposal

For all sufficiently large original tuples in the adjacent window,


$$
\boxed{\dim\ker K\ge242,\qquad \operatorname{rank}K\le\nu-242.}
$$



### Proof

Every equal-sector square block is singular by (6.1).

For a paired couple with square block $A$, the full block is


$$
\begin{pmatrix}0&A\\A^T&0\end{pmatrix},
$$


whose nullity is twice the nullity of $A$. The $120$ couples therefore contribute at least $240$ dimensions. The fixed sector contributes at least one.

For the unequal pair, the off-diagonal block has dimensions $s\times(s-1)$, so its full symmetric block has nullity at least one.

The sectors are disjoint invariant summands. Adding the lower bounds gives $242$. ∎

In particular,


$$
\operatorname{adj}(K)=0.
$$


For every endpoint vector, including the actual vector (4.5), the bordered matrix has rank at most


$$
\operatorname{rank}K+2\le\nu-240.
$$


Thus its determinant also vanishes.

**The proposed rank-$\nu-1$, nonzero-bordered-cofactor certificate cannot occur on any sufficiently large original subfamily in this window.**

---

## 7. Exact kernel recursion and the outstanding local obligation

The preceding lower bound does not determine the full radical. The following recursion specifies it exactly without introducing favorable digits.

For a rectangular block


$$
A_{uv}=-[z^{T-u-v}](z-1)^N,
\qquad 0\le u<r,\quad0\le v<t,
$$


write


$$
N=3N_1+d,\quad0\le d<3,
$$


and


$$
u=a+3u',\qquad v=b+3v'.
$$


For each $a,b\in\{0,1,2\}$, let $\rho\in\{0,1,2\}$ satisfy


$$
\rho\equiv T-a-b\pmod3.
$$


If $\rho>d$, that subblock is zero. Otherwise it is


$$
(-1)^{d-\rho}\binom d\rho
\left(
-[w^{T_1-u'-v'}](w-1)^{N_1}
\right),
\tag{7.1}
$$


where


$$
T_1=\frac{T-a-b-\rho}{3}.
$$


The exact row length is the number of integers $u<r$ congruent to $a\pmod3$; the column length is defined similarly. Empty sectors remain empty.

Equation (7.1) follows directly from


$$
(z-1)^N=(z-1)^d(z^3-1)^{N_1}.
$$


Iteration terminates and gives the full finite matrix and kernel, with no boundary extension.

Equivalently, a column polynomial $X(z)$, $\deg X<t$, lies in the kernel precisely when


$$
[z^k](z-1)^NX(z)=0
\qquad(T-r+1\le k\le T).
\tag{7.2}
$$


The endpoint on that kernel is the evaluation (4.6).

These are evaluated structural recursions, but they do **not** yet establish that the radical dimension is uniformly bounded. Nor do they evaluate the next actual Schur digit.

### Concrete follow-on lemma

A useful next theorem would prove, for the **actual** pair


$$
s=D/486,\qquad c'=(3^{h-31}-1)/2,
$$


one of the following:

1. exact ranks and endpoint restrictions of $B_s(c')$, $B_s(c'-1)$, and the $s\times(s-1)$ unequal block; or
2. a finite-state recursion proving a uniform bound for their nullities and identifying a kernel basis.

The recursion must follow the original $s$-word and all truncated lengths. A theorem about arbitrary favorable ternary words would not suffice.

Once a nondegenerate complement is certified, the next actual matrix must be evaluated, not inferred from the mod-$3$ recursion. If


$$
U=\begin{pmatrix}A&B\\B^T&C\end{pmatrix},
\qquad \det A\in\mathbb Z_3^\times,
$$


then retain


$$
R=C-B^TA^{-1}B,\qquad
f=e_R-B^TA^{-1}e_C,
$$


and the complete bordered diagonal


$$
3^{26}d_{\rm act}-e_C^TA^{-1}e_C.
$$


A prospective inverse of $R=3V$ incurs the new, independent payment


$$
R^{-1}=3^{-1}V^{-1}.
$$


Neither the old LOW payment nor an endpoint calculation pays this division.

The supplied data do not evaluate $U\bmod9$, and therefore do not determine $R/3\bmod3$. The same limitation prevents an honest evaluation here of the alternative next Schur digit in the window above $3$.

---

## 8. Primitive arithmetic: what the new obstruction means

At depth $26$, retain


$$
D_0=\det U,
$$




$$
D_1=e_{\rm act}^T\operatorname{adj}(U)e_{\rm act}
-3^{26}d_{\rm act}D_0.
$$


The exact primitive ratio gives


$$
\boxed{
v_3(q)=
\max\!\left(
0,\,
h-26+v_3Q_{\rm loc}(-1)+v_3D_1-v_3D_0
\right).
}
\tag{8.1}
$$



The new radical lower bound supplies no evaluated value for


$$
v_3D_1-v_3D_0.
$$


It therefore supplies **no primitive-denominator improvement**. Large common determinant and cofactor valuations are not a substitute for this relative valuation.

The actual complete closure remains


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


Nothing in the sector decomposition changes the logarithmic forcing, exponential charges, finite returns, exterior constants, complete corrected columns, or terminal $Y_m$.

Likewise, retain the prescribed actual contents, multiplier, paid divisions and least simultaneous clearer. The final integers are


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


with


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole error is still


$$
\boxed{
q(e+\pi)-p=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{8.2}
$$



An irrationality proof requires this complete expression to be nonzero and tend to zero at the **same infinite original indices**. No result here establishes that requirement.

---

## 9. Bounded verification and proof-status ledger

No closed producer or multiplier-chain computation should be repeated.

A small new exact arithmetic check may independently verify the forced singularity lemma.

**Bounded inputs**


$$
j_0=84645,\quad 3^7=2187,\quad q=9,
$$


together with the two residue triples


$$
(s,L,B)\equiv(1,4,7),\qquad(1,3,8)\pmod9.
$$



**Expected verifiable outputs**

1. $j_0\equiv81\pmod{729}$.
2. $(4^{81}-1)/243\equiv7\pmod9$, evaluated by modular arithmetic or the displayed binomial expansion.
3. For each residue triple, the nine floor-difference values sum to zero.
4. The length-one initial partial sum is $1$.
5. The sector involution has fixed point $182$, unequal pair $\{122,242\}$, and $120$ other couples.

This is a bounded audit of the new algebraic obstruction, not a computation of an original full matrix and not an infinite-family proof by enumeration.

| Claim | Status |
|---|---|
| Infinite original scope of the adjacent real window | Proved |
| Original congruence $s\equiv1\pmod9$ | Proved |
| Exact $243$-sector reduction, signs and lengths | Proved |
| Endpoint formula within every sector | Proved for the stated endpoint; actual application retains transport hypotheses |
| Every equal block singular modulo $3$ | Proved using the classical determinant product |
| $\dim\ker K\ge242$ | New proved result |
| Rank $\nu-1$ or nonzero first bordered cofactor modulo $3$ | Disproved for this candidate window |
| Exact finite kernel recursion | Proved |
| Uniform upper bound for the radical dimension | Open |
| Actual next Schur digit and paid inverse | Open |
| Actual depth-$26$ identification | Conditional on retained candidate hypotheses |
| Relative valuation and all-prime primitive denominator | Open |
| Nonzero vanishing whole error on the same indices | Open |

## Conclusion

The adjacent window does not provide the hoped-for almost-full-rank shortcut. Its original arithmetic forces every equal-sector binomial Hankel determinant to vanish modulo $3$, giving the rigorous obstruction


$$
\boxed{\operatorname{rank}K_{26}\le\nu-242.}
$$



The next local bottleneck is now more precise: determine the full original-word sector radicals and endpoint restrictions, then evaluate the **actual** next Schur digit with its complete bordered diagonal and independently paid inverse. The mod-$3$ Hankel formula alone cannot determine that digit.

The global bottleneck remains the actual relative cofactor valuation, its transport through all prescribed contents and clearing operations to the **all-prime primitive denominator**, and comparison with the **nonzero whole error at the same infinite original indices**.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


