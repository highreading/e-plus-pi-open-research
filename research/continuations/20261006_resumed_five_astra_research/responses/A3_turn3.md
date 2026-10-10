> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 3 — Fixed-seed coefficient saturation at all primes, an exact common-defect law, and the obstruction to a determinant-only exterior argument

## Executive conclusion

The irrationality or rationality of $e+\pi$ remains unresolved.

The new result in this turn is an **all-prime fixed-seed saturation theorem for the coefficient moments**. It uses the actual generating function


$$
e^z\left(1-z+\frac{z^2}{2}\right)^n,
$$


not an arbitrary solution of its recurrence.

Put


$$
a_k(n)=k!\,[z^k]\left(e^z\left(1-z+\frac{z^2}{2}\right)^n\right).
$$


Then


$$
\boxed{\gcd\bigl(a_k(n),a_{k+1}(n),a_{k+2}(n)\bigr)=1}
\tag{E1}
$$


for every $n,k\ge0$.

This yields two exact consequences for the original endpoint moments.

First, with the original


$$
D_{\rm mom}=2^n(n+2)!,
$$


one has


$$
\boxed{
\gcd\bigl(D_{\rm mom}b,D_{\rm mom}c,D_{\rm mom}d\bigr)
=
2^n(n+2)\varepsilon_n,
}
\tag{E2}
$$


where


$$
\varepsilon_n=
\begin{cases}
2,&n\equiv1\pmod4,\\
1,&n\not\equiv1\pmod4.
\end{cases}
$$



Second, define the integer-normalized defects


$$
\begin{aligned}
h_n&=(n+1)!\,H,\\
b_{0,n}&=(n+1)!\,B_0^\partial,\\
b_{3,n}&=(n+1)!\,B_3^\partial,
\end{aligned}
\qquad
P_n=n^2+5n+3,
$$


and


$$
W_n=\gcd\bigl(|h_n|,|b_{0,n}|,P_n\bigr).
$$


On both original families,


$$
\boxed{
\gcd\bigl(|h_n|,|b_{0,n}|,|b_{3,n}|\bigr)=2W_n,
\qquad 3\nmid W_n.
}
\tag{E3}
$$


Equivalently,


$$
\boxed{
\gcd\bigl(
|D_{\rm mom}H|,
|D_{\rm mom}B_0^\partial|,
|D_{\rm mom}B_3^\partial|
\bigr)
=
2^{n+1}(n+2)W_n.
}
\tag{E4}
$$



These are fixed-seed, all-prime identities. In particular, they explicitly handle small primes where backward invertibility of the coefficient transfer fails.

They do **not** identify the small-prime contents of the actual endpoint triples: those also involve the endpoint reference lattice and the complete exponential coordinate. That distinction remains essential.

The exterior-transfer investigation also gives a precise obstruction. The two evaluated terminal determinants are two projections of a three-coordinate minor vector. Their projection kernels are exactly the endpoint lines. Thus even primitivity of the **entire exterior state**, propagated by an invertible transfer, permits both selected determinants to vanish. The actual terminal-force normal evaluation does not remove this obstruction.

The missing theorem is therefore a fixed-seed **projected-minor or terminal-line avoidance estimate**, not another proof of state primitivity.

No computation has been executed here. The accepted $n=225$ computations are not requested again. The announced original $n=3375$ computation is neither requested nor assigned an outcome.

---

## 1. Scope, retained inputs, and accepted finite evidence

The index domain remains


$$
n=15^r,\quad r\ge2,
\qquad\text{or}\qquad
n=105^r,\quad r\ge2.
$$


Every such $n$ is odd and divisible by $3$.

The following objects are unchanged:

- the $3\times3$ contact matrix, with coordinates $0,1,2$;
- both corrected reconstructed columns, with coordinates $0,1,2,3$;
- the complete force through precisely $2n+2$;
- the fixed exponential boundary;
- the terminal return and exterior $+1$;
- the least clearer over all eight reconstruction entries;
- the actual row contents and primitive endpoint triples;
- every prime in the final denominator gcd;
- the same-index whole error.

I reuse, without repeating their generic proofs:

1. A3 Turn 2’s two-kernel determinant identities and polynomial-distortion comparisons;
2. the independently established equality $\delta_j=0$ at $p>n+2$;
3. the exact structural-content laws away from $Q_0,Q_3$;
4. A4 Turn 3’s exact common structural gcd law.

Here


$$
Q_0=n^2+6n+4,\qquad Q_3=n^2+4n+1.
$$



### The new $n=225$ post-processing

The supplied source and certificate support the stated **finite** conclusions:

- the large-prime part of the cleared $H$-numerator has $521$ digits;
- the large part of the common resultant has $1420$ digits;
- at both endpoints,
  

$$
\gcd(X_{j,\mathrm{large}},\mathcal F_{\mathrm{large}})=1;
$$


- no factor of $X_j$ above $226$ is supported on $H$;
- the displayed integer Bézout residuals are zero.

The source recovers the common force coordinates from the already archived endpoint values. Accordingly, its syzygy reconstruction is post-processing of the accepted original force, not an independent regeneration of that force. This is exactly the advertised scope.

The cutoff distinction is retained: the common-resultant post-processing strips primes at most $226=n+1$, whereas the two-kernel structural statements use $p>227=n+2$.

Nothing in these finite results proves an infinite support theorem.

---

## 2. The actual integer coefficient transfer and its fixed seed

Write


$$
q(z)=1-z+\frac{z^2}{2},
\qquad
c_k(n)=[z^k]e^zq(z)^n,
\qquad
a_k(n)=k!c_k(n).
$$


The symbol $a_k(n)$ in this section is not the contact moment $c_{n-2}$.

Differentiating the **actual generating function** gives


$$
q(z)\frac{d}{dz}\bigl(e^zq(z)^n\bigr)
=
\bigl(q(z)+nq'(z)\bigr)e^zq(z)^n.
$$


Coefficient comparison yields


$$
(k+1)c_{k+1}
=
(k+1-n)c_k
+\frac{2n-k-1}{2}c_{k-1}
+\frac12c_{k-2}.
$$


Consequently


$$
\boxed{
a_{k+1}
=
(k+1-n)a_k
+\frac{k(2n-k-1)}2a_{k-1}
+\frac{k(k-1)}2a_{k-2}.
}
\tag{2.1}
$$


Both displayed half-products are integers.

The fixed initial state is


$$
\boxed{
a_0=1,\qquad a_1=1-n,\qquad a_2=(n-1)^2.
}
\tag{2.2}
$$



For $k\ge2$, the three-state transfer is


$$
\begin{pmatrix}a_{k+1}\\a_k\\a_{k-1}\end{pmatrix}
=
A_{n,k}
\begin{pmatrix}a_k\\a_{k-1}\\a_{k-2}\end{pmatrix},
$$


where


$$
A_{n,k}=
\begin{pmatrix}
k+1-n&k(2n-k-1)/2&k(k-1)/2\\
1&0&0\\
0&1&0
\end{pmatrix},
$$


and


$$
\boxed{\det A_{n,k}=\frac{k(k-1)}2.}
\tag{2.3}
$$



For the scaling specified in the assignment,


$$
C_k=2^kk!c_k=2^ka_k,
$$


the recurrence becomes


$$
\boxed{
C_{k+1}
=
2(k+1-n)C_k
+2k(2n-k-1)C_{k-1}
+4k(k-1)C_{k-2},
}
\tag{2.4}
$$


with determinant $4k(k-1)$.

Thus the advertised support of the transfer determinant is correct. But the determinant alone does not prove the all-prime result below: at small primes, some transfers are singular. The fixed generating function supplies the additional information.

---

## 3. Fixed-seed congruences, including the singular small primes

### 3.1 Integrality and congruence in the exponent $n$

Let


$$
u(z)=-z+\frac{z^2}{2}.
$$


For $m\ge0$, the series $u(z)^m/m!$ has integral exponential coefficients. Indeed, its only possible nonzero coefficient degrees are $r=m+\ell$, $0\le\ell\le m$, and


$$
r!\,[z^r]\frac{u(z)^m}{m!}
=
(-1)^{m-\ell}
\frac{(m+\ell)!}{(m-\ell)!\,\ell!\,2^\ell}.
\tag{3.1}
$$


The absolute value counts a partition into $\ell$ unordered pairs and $m-\ell$ singletons, so it is an integer.

Now


$$
q(z)^n
=
\sum_{m\ge0}(n)_m\frac{u(z)^m}{m!}.
$$


For each fixed coefficient, this is a finite sum. Multiplication by $e^z$ preserves integral exponential coefficients. Therefore


$$
\boxed{a_k(n)\in\mathbb Z[n].}
\tag{3.2}
$$



In particular, for every positive integer $N$,


$$
\boxed{
n'\equiv n\pmod N
\quad\Longrightarrow\quad
a_k(n')\equiv a_k(n)\pmod N
}
\tag{3.3}
$$


for every $k$.

One useful specialization is


$$
\boxed{
p^s\mid n
\quad\Longrightarrow\quad
a_k(n)\equiv1\pmod{p^s}
\quad\text{for every }k,
}
\tag{3.4}
$$


because $a_k(0)=1$.

This is a fixed-seed statement. It is not true for arbitrary initial states of (2.1).

### 3.2 Congruence in the coefficient index at odd primes

Write


$$
q(z)^n=\sum_{r=0}^{2n}q_r(n)z^r.
$$


Every $q_r(n)$ is dyadic, and


$$
a_k(n)=\sum_{r=0}^{2n}q_r(n)(k)_r.
\tag{3.5}
$$


Thus, for fixed $n$, $a_k(n)$ is a polynomial in $k$ over $\mathbb Z[1/2]$.

For every odd prime $p$,


$$
\boxed{
k'\equiv k\pmod{p^s}
\quad\Longrightarrow\quad
a_{k'}(n)\equiv a_k(n)\pmod{p^s}.
}
\tag{3.6}
$$


In particular,


$$
\boxed{a_{k+p}(n)\equiv a_k(n)\pmod p.}
\tag{3.7}
$$



This periodicity supplies the information lost at the singular transfer positions $k\equiv0,1\pmod p$.

### 3.3 The prime $2$

For the primitivity theorem, the following exact parity description suffices.

By (3.3), if $n$ is even then


$$
a_k(n)\equiv a_k(0)=1\pmod2.
$$


If $n$ is odd then


$$
a_k(n)\equiv a_k(1)
=
1-k+\binom{k}{2}\pmod2.
$$


The latter has the period-four pattern


$$
\boxed{1,\ 0,\ 0,\ 1.}
\tag{3.8}
$$



Higher-power control is also available:


$$
\boxed{
a_{k+2^{s+1}}(n)\equiv a_k(n)\pmod{2^s},
\qquad s\ge1.
}
\tag{3.9}
$$


Here is a proof, to make the prime-power claim checkable.

Set


$$
b_r=r!\,[z^r]q(z)^n.
$$


Since the coefficient of $z^r$ has denominator dividing $2^{\lfloor r/2\rfloor}$,


$$
v_2(b_r)\ge
v_2(r!)-\lfloor r/2\rfloor
=
\sum_{\nu\ge2}\left\lfloor\frac r{2^\nu}\right\rfloor.
\tag{3.10}
$$


Let


$$
Q_r(k)=
\left.\frac{d^k}{dz^k}\left(e^z\frac{d^r}{dz^r}q(z)^n\right)\right|_{z=0}.
$$


It is an integral binomial combination of $b_{r},b_{r+1},\ldots$, so the same lower bound, evaluated at $r$, holds for $Q_r(k)$.

With $M=2^{s+1}$,


$$
a_{k+M}-a_k
=
\sum_{r=1}^{M}\binom Mr Q_r(k).
$$


For $1\le r\le M$,


$$
v_2\binom Mr=s+1-v_2(r),
$$


and


$$
\sum_{\nu\ge2}\left\lfloor\frac r{2^\nu}\right\rfloor
\ge v_2(r)-1.
$$


Every summand is therefore divisible by $2^s$, proving (3.9).

These congruences concern the moment coefficients only. They are not, without further work, congruences for the complete endpoint force.

---

## 4. New theorem: every consecutive factorial-normalized moment triple is primitive

### Theorem 4.1

For every $n,k\ge0$,


$$
\boxed{
\gcd\bigl(a_k(n),a_{k+1}(n),a_{k+2}(n)\bigr)=1.
}
\tag{4.1}
$$



### Proof

Fix a prime $p$.

If $p=2$, the assertion follows immediately from §3.3. When $n$ is even, all entries are odd. When $n$ is odd, every three consecutive terms of the pattern $1,0,0,1$ contain an odd entry.

Now let $p$ be odd. By (3.7), reduce the three consecutive indices modulo $p$.

If they pass through residue $0$, one of the corresponding values is


$$
a_0(n)=1\pmod p.
$$



Otherwise, they are represented by


$$
r,r+1,r+2\in\{1,\ldots,p-1\}.
$$


Suppose all three values vanish modulo $p$. Apply (2.1) at $k=r+1$. Its backward coefficient


$$
\frac{(r+1)r}{2}
$$


is a unit modulo $p$, so $a_{r-1}\equiv0\pmod p$.

Repeating this backward step reaches $a_0\equiv0\pmod p$, contradicting $a_0=1$.

No prime divides all three values. ∎

### What has—and has not—been proved

This theorem removes the small-prime loss for the **actual coefficient state after factorial normalization**.

It does not say that an arbitrary pair of linear projections of that primitive state is primitive. Indeed, the two defect projections are precisely where the outstanding structural gcd problem remains.

---

## 5. Exact content of the cleared three-moment state

Return to


$$
b=c_{n-1},\qquad c=c_n,\qquad d=c_{n+1}.
$$


Put


$$
x=a_{n-1}(n),\qquad y=a_n(n),\qquad z=a_{n+1}(n).
$$


Then


$$
(n+1)!\,(b,c,d)
=
\bigl(n(n+1)x,\ (n+1)y,\ z\bigr).
\tag{5.1}
$$



By Theorem 4.1, $\gcd(x,y,z)=1$. Therefore


$$
g_n:=\gcd\bigl(n(n+1)x,(n+1)y,z\bigr)
\mid n(n+1).
\tag{5.2}
$$


For completeness, this divisibility follows prime by prime: among $x,y,z$, at least one is a unit, and its attached multiplier divides $n(n+1)$.

Every odd prime factor permitted by (5.2) is actually excluded:

- If $p\mid n$, equation (3.4) gives $z\equiv1\pmod p$.
- If $p\mid n+1$, equation (3.6) gives
  

$$
z=a_{n+1}(n)\equiv a_0(n)=1\pmod p.
$$



At $2$:

- if $n$ is even, $z$ is odd;
- if $n\equiv3\pmod4$, $z$ is odd;
- if $n\equiv1\pmod4$, all three entries in (5.1) are even, while (5.2) permits only one factor $2$.

Hence


$$
\boxed{g_n=\varepsilon_n.}
\tag{5.3}
$$


Multiplying (5.1) by $2^n(n+2)$ proves


$$
\boxed{
\gcd\bigl(
|D_{\rm mom}b|,
|D_{\rm mom}c|,
|D_{\rm mom}d|
\bigr)
=
2^n(n+2)\varepsilon_n.
}
\tag{5.4}
$$



This is an exact all-prime saturation statement for the original moments. No factorial-sized unknown common content remains in this three-entry state.

---

## 6. New all-prime common-defect identity

Define


$$
\begin{aligned}
h&=n(n+1)x+(n+1)(n-3)y-2(n-1)z,\\
b_0&=6z-(n+1)(n+6)y,\\
b_3&=2(n+2)z-(n+1)(n+3)y.
\end{aligned}
\tag{6.1}
$$


These are exactly


$$
h=(n+1)!H,\qquad
b_j=(n+1)!B_j^\partial.
$$



The linear transformation from $(x,y,z)$ to $(h,b_0,b_3)$ has determinant


$$
\boxed{-2n(n+1)^2P_n.}
\tag{6.2}
$$


It also satisfies


$$
\boxed{
(n+2)b_0-3b_3=-(n+1)P_n y.
}
\tag{6.3}
$$



### Theorem 6.1 — Common normalized defects at every prime

For every odd positive $n$ divisible by $3$,


$$
\boxed{
\gcd(|h|,|b_0|,|b_3|)
=
2\gcd(|h|,|b_0|,P_n).
}
\tag{6.4}
$$


Moreover,


$$
\boxed{3\nmid\gcd(h,b_0,P_n).}
\tag{6.5}
$$



### Proof

Write


$$
G=\gcd(|h|,|b_0|,|b_3|),
\qquad
W=\gcd(|h|,|b_0|,P_n).
$$



#### Odd primes dividing $n(n+1)$

If $p\mid n$, then $x,y,z\equiv1\pmod p$, and (6.1) gives


$$
h\equiv-1\pmod p.
\tag{6.6}
$$


If $p\mid n+1$, then $z\equiv1\pmod p$, and


$$
h\equiv4\pmod p.
\tag{6.7}
$$


Thus no odd prime dividing $n(n+1)$ divides either $G$ or $W$.

Because $3\mid n$, equation (6.6) also proves $3\nmid G W$.

#### All remaining odd primes

Fix an odd prime $p\ne3$ not dividing $n(n+1)$.

If $p\mid G$, then $y$ must be a unit. Otherwise $b_0\equiv0$ would force $z\equiv0$, and $h\equiv0$ would then force $x\equiv0$, contradicting Theorem 4.1.

Let $e=v_p(G)$. Equation (6.3), with $(n+1)y$ a unit, gives


$$
v_p(P_n)\ge e.
$$


Thus $v_p(W)\ge e$.

Conversely, if


$$
f=\min\{v_p(h),v_p(b_0),v_p(P_n)\},
$$


then (6.3), with $3$ a unit, proves $p^f\mid b_3$. Hence $v_p(G)\ge f$.

Therefore $v_p(G)=v_p(W)$ at every odd prime.

#### The prime $2$

The number $P_n$ is odd when $n$ is odd, so $W$ is odd.

If $n\equiv1\pmod4$, §3.3 gives


$$
x\ \text{odd},\qquad y,z\ \text{even}.
$$


In (6.1), the first term of $h$ has valuation exactly $1$, while its other two terms have valuation at least $3$. Both $b_0,b_3$ are even. Thus $v_2(G)=1$.

If $n\equiv3\pmod4$, then


$$
x\ \text{even},\qquad y,z\ \text{odd}.
$$


Both $b_0$ and $b_3$ have valuation exactly $1$, and $h$ is even. Again $v_2(G)=1$.

Combining all primes gives $G=2W$. ∎

Since


$$
D_{\rm mom}=2^n(n+2)(n+1)!,
$$


Theorem 6.1 proves (E4).

### Scope of the improvement

The common normalized defect content is now completely described at small primes as well as large primes:


$$
W_n\mid P_n,\qquad 3\nmid W_n.
$$


This is more than a support statement: the valuation multiplicities are included.

However, it is a law for the normalized **moment defects**. It is not an all-prime equality for $\gcd(\gamma_0,\gamma_3)$. At small primes, the reference vectors, factorial normalizations, and actual exponential coordinate must still be accounted for.

---

## 7. Combining the two-kernel reduction with A4’s exact common structural gcd

Let


$$
N=n+2,
\qquad
\Gamma_j=(\gamma_j)_{>N}.
$$


Retain A3’s


$$
U_j=
\gcd\bigl(
|D_{\rm mom}H|,
|D_{\rm mom}B_j^\partial|
\bigr)_{>N}.
$$


Theorem 6.1 gives


$$
\gcd(U_0,U_3)=(W_n)_{>N}.
$$


A4’s accepted structural theorem gives, independently at its stated scope,


$$
\gcd(\Gamma_0,\Gamma_3)=V_n,
$$


where


$$
\boxed{V_n=(W_n)_{>N}.}
\tag{7.1}
$$



A3’s polynomial-distortion result therefore permits the exact notation


$$
U_j=\epsilon_j\Gamma_j,
\qquad
\epsilon_j\mid(Q_j)_{>N}.
\tag{7.2}
$$



There is a useful additional separation:


$$
\boxed{
\gcd(\epsilon_0,U_3)=
\gcd(\epsilon_3,U_0)=1.
}
\tag{7.3}
$$


Indeed, a common prime would divide $V_n$, hence $P_n$, and also the corresponding $Q_j$. But above $n+2$, primes dividing $P_n$ divide neither $Q_0$ nor $Q_3$.

Thus the polynomial saturation losses are endpoint-specific; they do not contaminate the exact common structural factor.

In particular,


$$
\boxed{
\frac{\Gamma_0\Gamma_3}{V_n^2}
=
\frac{U_0U_3}{V_n^2\epsilon_0\epsilon_3}.
}
\tag{7.4}
$$


This is the sharpened structural imbalance formula.

Now retain, without changing their definitions,


$$
\mathfrak D_j
=
\gcd\bigl(
X_j^\circ,\mathcal F,\mathcal F_j^{\rm alt}
\bigr)_{>N},
\qquad
\widehat K_j=\frac{U_j|X_j|_{>N}}{\mathfrak D_j}.
$$


The proved comparison remains


$$
(d_j)_{>N}\mid\widehat K_j
\mid(Q_j)_{>N}(d_j)_{>N}.
\tag{7.5}
$$



Since every prime of $V_n$ divides both actual $\gamma_j$, it occurs in neither $\mathfrak D_j$. Hence $V_n$ divides both $\widehat K_j$, and also both actual large-prime endpoint denominators. It can be removed as an exact common factor before computing imbalance.

This does **not** allow the structural imbalance and the $X_j/\mathfrak D_j$ imbalance to be multiplied separately: cross-cancellation between their prime valuations remains possible.

---

## 8. What the exterior connection actually propagates

The proposed augmented-transfer route has two distinct issues:

1. closure and propagation of a complete exterior state;
2. control of the particular two evaluated projections used in the endpoint gcd.

The second issue remains even if the first is completely solved.

### 8.1 Exact exterior propagation for a same-transfer forced state

Suppose an independently verified integer normalization of the **actual complete force** gives


$$
M_{k+1}=A_kM_k,
\qquad
F_{k+1}=A_kF_k+B_kM_k.
\tag{8.1}
$$


Here $B_k$ must be the actual coefficient matrix, and $F_{k_0}$ must contain the actual fixed exponential boundary. They cannot be replaced by a homogeneous companion.

Set


$$
Z_k=M_k\wedge F_k.
$$


Then, exactly,


$$
\boxed{
Z_{k+1}
=
(\wedge^2A_k)Z_k
+
(A_kM_k)\wedge(B_kM_k).
}
\tag{8.2}
$$



The second term is quadratic in the fixed moment state. Thus adjoining its six symmetric-square coordinates gives a closed nine-state linear transfer:


$$
\begin{pmatrix}
Z_{k+1}\\ \operatorname{Sym}^2M_{k+1}
\end{pmatrix}
=
\begin{pmatrix}
\wedge^2 A_k&L_k\\
0&\operatorname{Sym}^2 A_k
\end{pmatrix}
\begin{pmatrix}
Z_k\\ \operatorname{Sym}^2M_k
\end{pmatrix},
\tag{8.3}
$$


where $L_k$ is obtained by expanding the quadratic term in (8.2). No division by $2$ is necessary if the six ordinary monomials are used.

For a three-state $A_k$,


$$
\det(\wedge^2A_k)=(\det A_k)^2,
\qquad
\det(\operatorname{Sym}^2A_k)=(\det A_k)^4.
$$


Therefore the nine-state determinant is


$$
\boxed{(\det A_k)^6.}
\tag{8.4}
$$



This proves the advertised type of controlled determinant support **conditional on the exact complete-force transfer (8.1)**.

It does not evaluate that transfer’s boundary constants. The terminal identities in the attached reports do not, by themselves, supply all entries of $B_k$ and the full initial force state. I therefore do not present (8.3) as a newly verified producer for the original force.

Nor has the actual reference column been shown to be a third trajectory of $A_k$. Extending it backward artificially would not supply the missing fixed-seed arithmetic.

### 8.2 Why an ordinary homogeneous Wronskian is insufficient

When $A_k$ is invertible, the quadratic source in (8.2) vanishes identically in $M_k$ if and only if


$$
A_k^{-1}B_k
$$


is scalar.

Indeed,


$$
(A_kM)\wedge(B_kM)=0
$$


for every $M$ is equivalent to


$$
M\wedge(A_k^{-1}B_kM)=0
$$


for every $M$. Applying this to basis vectors and their pairwise sums forces the linear map to be scalar.

Thus a homogeneous Abel identity cannot simply be assumed for a same-coefficient inhomogeneous force. The quadratic source must either be retained or canceled by an explicitly proved identity.

Even after doing that, determinant support controls the content of the **whole propagated state**, not its chosen terminal projections.

---

## 9. A precise obstruction for the original endpoint kernels

This obstruction can be evaluated directly from the already proved, complete terminal determinants. It does not require an arbitrary companion.

Retain the actual columns


$$
t=\tau_nv+\tau_{n+1}w,
\qquad
s=\frac{\widehat w-T_0}{n!}.
$$


The column $s$ includes the complete force and the exterior correction.

Define


$$
\mu_i=2(n+2)n!\det(t,s,T_i),
\qquad i=0,1,2.
\tag{9.1}
$$


At primes $p>n+2$, the displayed scaling is a unit.

The exact kernel definitions give


$$
\boxed{
\Theta=\mu_1+n\mu_0,
}
\tag{9.2}
$$




$$
\boxed{
\Theta_0=\mu_2+(n+2)\mu_1+n\mu_0,
}
\tag{9.3}
$$




$$
\boxed{
\Theta_3=\mu_1-(n+2)\mu_0.
}
\tag{9.4}
$$



These are the original complete determinants, not surrogate remainders.

### 9.1 Endpoint $0$: a missing primitive coordinate

The change of coordinates


$$
(\mu_0,\mu_1,\mu_2)
\longmapsto
(\mu_0,\Theta,\Theta_0)
$$


has matrix


$$
\begin{pmatrix}
1&0&0\\
n&1&0\\
n&n+2&1
\end{pmatrix}
$$


and determinant $1$.

Consequently, at every prime,


$$
\boxed{
(\mu_0,\mu_1,\mu_2)
=
(\mu_0,\Theta,\Theta_0)
}
\tag{9.5}
$$


as generated ideals.

Primitivity of the full minor vector therefore permits


$$
\Theta\equiv\Theta_0\equiv0\pmod{p^a},
\qquad
\mu_0\in\mathbb Z_p^\times.
$$


The simultaneous zero condition is exactly


$$
\boxed{
(\mu_0,\mu_1,\mu_2)
\equiv
\mu_0(1,-n,n(n+1))
\pmod{p^a}.
}
\tag{9.6}
$$


The surviving direction is $-\ell_0$, up to its scalar.

### 9.2 Endpoint $3$: the other missing coordinate

The transformation


$$
(\mu_0,\mu_1,\mu_2)
\longmapsto
(\Theta,\Theta_3,\mu_2)
$$


has determinant $2(n+1)$. Thus at every $p>n+2$,


$$
\boxed{
(\mu_0,\mu_1,\mu_2)
=
(\Theta,\Theta_3,\mu_2).
}
\tag{9.7}
$$


Both selected determinants may vanish while $\mu_2$ remains a unit. Their simultaneous zero condition is


$$
\boxed{
(\mu_0,\mu_1,\mu_2)\equiv(0,0,\mu_2)\pmod{p^a}.
}
\tag{9.8}
$$


This is exactly the endpoint direction $\ell_3$.

### 9.3 The actual force boundary does not contradict these directions

The retained complete terminal normal evaluation is


$$
\boxed{
q_\partial^Ts=\frac{2(n+1)(2d-c)}{n!}.
}
\tag{9.9}
$$


The logarithmic part lies in the reference plane and is annihilated by $q_\partial$; the exterior subtraction remains in (9.9).

At a large prime where $2d-c$ is a unit and the reference column $t$ is primitive, (9.9) makes $t\wedge s$ primitive. If $\Delta$ is also a unit, then the full vector $(\mu_0,\mu_1,\mu_2)$ is primitive.

Nevertheless, (9.6) or (9.8) is still compatible with that primitivity: the unselected coordinate is a unit.

This identifies the obstruction in the original terminal algebra:

> A unit determinant or a primitive complete exterior state does not prevent the fixed terminal minor vector from lying on an endpoint line modulo a prime power.

This is **not** a claim that such a bad prime has been found for an original index. It is a proof that the proposed determinant-only implication would not exclude one.

No impossibility theorem for all possible Wronskian or Bézout identities is being asserted. An additional invariant might exclude these lines—but its value on the actual fixed seed, and its relation to the two selected projections, would have to be proved.

---

## 10. The concrete follow-on lemma

The new coefficient theorem closes the moment-state saturation issue, including its singular small-prime positions. It does not close the projected arithmetic.

A useful next target is now the following.

### Fixed-seed terminal-line intersection lemma

For infinitely many $n$ in one original family, bound the total prime-power depth with which the actual complete minor vector


$$
\mu(n)=(\mu_0,\mu_1,\mu_2)
$$


meets the two endpoint lines (9.6) and (9.8), **jointly with the actual $X_j^\circ$-condition**.

Equivalently, prove a suitable bound for


$$
\begin{aligned}
&\sum_{p>n+2}
\min\!\left\{
v_p(X_0^\circ),
v_p(\mu_1+n\mu_0),
v_p(\mu_2+(n+2)\mu_1+n\mu_0)
\right\}\log p\\
+{}&
\sum_{p>n+2}
\min\!\left\{
v_p(X_3^\circ),
v_p(\mu_1+n\mu_0),
v_p(\mu_1-(n+2)\mu_0)
\right\}\log p.
\end{aligned}
\tag{10.1}
$$


All determinant-clearing factors in this expression are units at the displayed primes, so it is exactly the logarithmic complete two-kernel gcd contribution.

This must be combined with a bound for the **individual**, rather than merely common, structural defect gcds $U_j/V_n$, or replaced by a direct actual-imbalance theorem.

An augmented connection would advance this lemma only if it supplies an explicit Bézout or adjoint identity whose terminal functional involves the selected projections and whose value on the **full original seed** has controlled support or size. A determinant formula for the entire connection is insufficient.

### Small-prime requirement

The congruences of §3 and the exact common-defect law of §6 can now be used to handle the coefficient part at every small prime. But the actual endpoint denominator still requires


$$
\boxed{
v_p(d_j)
=
v_p(\gamma_jX_j)
-\min\{v_p(\gamma_jX_j),v_p(V_j)\}
}
\tag{10.2}
$$


at all primes, including $p\le n+2$.

At those primes one may not replace this by the large-prime $\mathcal C_j^\sharp$ formula. In particular:

- the endpoint reference lattice need not be saturated in the displayed rational coordinates;
- $L$ need not be a unit;
- the complete exponential coordinate can affect primitive reduction;
- cancellation in $V_j=\gamma_jY_j+L\mathsf E_j$ must be evaluated, not inferred from moment primitivity.

Thus the small-prime moment obstruction has been sharpened substantially, but the small-prime **whole endpoint** obstruction remains.

---

## 11. Actual primitive denominator and whole error

None of the new normalized moment quantities replaces an actual row or primitive triple.

The endpoint denominator remains


$$
d_j=\frac{|\gamma_jX_j|}
{\gcd(|\gamma_jX_j|,|V_j|)}.
$$



For a reduced weight $\lambda=a/k$, retain


$$
J_{\rm wt}=B\widetilde v_0-A\widetilde v_3,
\qquad
T_{\rm wt}=aJ_{\rm wt}+kA\widetilde v_3,
$$




$$
F_{\rm gcd}
=\gcd(|A|,|a|)\gcd(|B|,|a-k|),
$$




$$
G=\gcd(k,|J_{\rm wt}|),
\qquad
H_{\rm gcd}
=
\gcd\!\left(h,\frac{|T_{\rm wt}|}{F_{\rm gcd}G}\right).
$$


The actual primitive pair is


$$
\boxed{
q_\lambda=
\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
\qquad
p_\lambda=
\operatorname{sgn}(AB)
\frac{T_{\rm wt}}{F_{\rm gcd}GH_{\rm gcd}}.
}
\tag{11.1}
$$


Every prime remains in these gcds.

The same-index complete error remains


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
\tag{11.2}
$$


The required irrationality condition is still


$$
\boxed{
0<
q_\lambda|e_3\alpha_{n,2}|
\,|\lambda-\Lambda_{n,2}|
\longrightarrow0
}
\tag{11.3}
$$


along an infinite sequence.

The accepted $n=225$ row contents remain


$$
(508500,\ 28350,\ 15525,\ 772).
$$


The accepted five whole-form evaluations remain nonzero and greater than $1$ in absolute value. Neither the new resultant post-processing nor the present all-prime moment theorem changes those evaluations.

---

## 12. Proof status and bounded verification

### 12.1 Status ledger

| Statement | Status |
|---|---|
| Integer three-state coefficient transfer and its fixed initial state | Proved directly from the generating function |
| Congruence in $n$ modulo every integer | Proved |
| Odd-prime-power periodicity in the coefficient index | Proved |
| $2$-power index period $2^{s+1}$ modulo $2^s$ | Proved |
| Primitivity of every consecutive factorial-normalized moment triple | **Proved** |
| Exact all-prime content of the cleared moment triple | **Proved** |
| Exact all-prime common normalized-defect law | **Proved** |
| Combination with A4’s exact common structural gcd | Proved at $p>n+2$ |
| Endpoint-specific separation of the $Q_j$-distortion factors | Proved |
| Nine-state wedge/symmetric-square propagation | Conditional on the exact full-force transfer (8.1) |
| Original full-force transfer boundary constants in that representation | Not evaluated here |
| A determinant-only invariant controlling the two projected kernel gcds | Does not follow; precise projection obstruction proved |
| Infinite fixed-seed $O(n)$ logarithmic content bound | Open |
| Actual all-prime denominator/whole-error comparison | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

### 12.2 Bounded exact arithmetic

No additional original-index producer computation is needed to prove the new identities.

A new, bounded symbolic check could corroborate only the algebra introduced in this turn. Its inputs are symbolic $n,x,y,z,\mu_0,\mu_1,\mu_2$, the recurrence matrices in §2, and the three linear forms in (6.1).

Expected verifiable outputs are:

1. zero residuals for the two transfer determinants;
2. the exact determinant
   

$$
-2n(n+1)^2(n^2+5n+3)
$$


   for the defect transformation;
3. zero residual for
   

$$
(n+2)b_0-3b_3+(n+1)P_ny;
$$


4. determinants $1$ and $2(n+1)$ for the two terminal-minor coordinate changes;
5. zero residuals for the endpoint-line substitutions (9.6) and (9.8).

These are small symbolic calculations, not original-family gcd evaluations. Their execution is not represented as having occurred.

The announced $n=3375$ source and certificate will supply a separate finite result when received. No endpoint denominator, row content, gcd, or whole-error outcome for that index is assumed here.

---

## Conclusion

The fixed exponential coefficient seed supplies arithmetic information that transfer invertibility alone does not:



$$
\boxed{
\gcd\bigl(a_k(n),a_{k+1}(n),a_{k+2}(n)\bigr)=1
\quad\text{at every prime}.
}
$$



For the original odd, $3$-divisible indices, this gives the exact all-prime normalized common-defect law


$$
\boxed{
\gcd\bigl(
|D_{\rm mom}H|,
|D_{\rm mom}B_0^\partial|,
|D_{\rm mom}B_3^\partial|
\bigr)
=
2^{n+1}(n+2)
\gcd\bigl(
|(n+1)!H|,
|(n+1)!B_0^\partial|,
P_n
\bigr).
}
$$


Its large-prime part agrees with A4’s exact common structural factor $V_n$, and the remaining $Q_j$-distortion factors are endpoint-specific.

The exterior investigation identifies the exact next obstruction: the two complete kernel determinants omit one primitive minor coordinate. Their simultaneous divisibility is compatible with a primitive augmented state and with the actual complete terminal normal evaluation. What must be controlled is the fixed seed’s approach to the endpoint lines modulo prime powers.

A proof of that projected arithmetic estimate would still have to retain the small-prime endpoint normalization and then compare the **actual all-prime primitive denominator** with the **same-index whole error**.



$$
\boxed{\text{No unconditional proof or disproof of the irrationality of }e+\pi\text{ has been obtained.}}
$$


