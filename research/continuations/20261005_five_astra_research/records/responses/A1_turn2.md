> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A1 continuation: an unconditional moving-prime cancellation theorem for the actual bordered pair

I obtain a **proved common-content cancellation theorem**, rather than an odd-prime survival theorem. It applies to the actual primitive $Q$ and complete bordered center, for every regular index


$$
n=4^j+1,\qquad j\ge1,
$$


and every prime in the window


$$
3n<p\le 4n-3.
$$



The key point is that the highest arctangent pole has an explicitly computable rank. Its rank is determined by the degree of the reduction of the **actual primitive polynomial** $Q$, so no unproved assertion about its leading coefficient modulo $p$ is needed. This gives:

* an explicit factor dividing the **final common content** $\gcd(A,B)$;
* an exact local reduction to a smaller bordered matrix, valid at every $p$-adic depth;
* a universal common-content divisor whose logarithm is
  

$$
\frac14n^2+o(n^2).
$$



This is cancellation in an explicitly fixed integer normalization. It is **not** an estimate of the actual odd denominator after the remaining gcd.

The compact-root theorem remains at its previous author-level status pending A4’s review. Nothing below uses it.

---

## 1. Fixed normalization and statement

Throughout, let


$$
r=\frac{n-1}{2},\qquad k=r+1,
$$


and let $Q(y)\in\mathbb Z[y]$ be the positive-leading primitive polynomial specified in the supplied construction. Write


$$
w=Q(-1).
$$



Retain the complete rational matrix $R$, including all its rational arctangent moments. In the unimodular endpoint basis


$$
1,\quad u_i(y)=y^i-(-1)^i,\qquad 1\le i\le r,
$$


write


$$
R_{\rm end}=
\begin{pmatrix}
a&b^T\\
b&H
\end{pmatrix}.
$$


Set


$$
\ell=\operatorname{lcm}(1,3,\ldots,4n-3),\qquad
t=\ell a,\quad z=\ell b,\quad K=\ell H,
$$


and


$$
\Delta=\det K,\qquad
A=t\Delta-z^T\operatorname{adj}(K)z,\qquad
B=\ell w\Delta.
$$


These are exactly the bordered integers from the preceding interface, not a differently normalized polynomial family.

Thus


$$
g=\gcd(|A|,|B|),\qquad
p^{\rm cen}=-\frac{\operatorname{sgn}(B)A}{g},
\qquad
q^{\rm cen}=\frac{|B|}{g}.
\tag{1}
$$



For a prime $p$, define


$$
d_p=\deg\bigl(Q\bmod p\bigr).
\tag{2}
$$


Because $Q$ is primitive, its reduction is not the zero polynomial, so $0\le d_p\le n$ for every prime.

For $3n<p\le4n-3$, put


$$
t_p=\frac{p+1}{2},\qquad
h_p=\max(0,n+d_p-t_p),\qquad
s_p=k-h_p.
\tag{3}
$$



### Theorem — Explicit moving-prime cancellation

For every $n=4^j+1$, $j\ge1$, and every prime $3n<p\le4n-3$,


$$
\boxed{v_p(g)\ge s_p.}
\tag{4}
$$


In particular,


$$
\boxed{
v_p(g)\ge \frac{p-3n+2}{2}.
}
\tag{5}
$$



There is also an exact $p$-local factorization of both $A$ and $B$, after removal of this common $p^{s_p}$, in terms of a bordered matrix of size $s_p$. That factorization is given in §4.

This is an unconditional statement for the specified family and infinite index window. It does not invoke the generic corank-one criterion or assume its coupling hypothesis.

---

## 2. The actual shifted divided-difference basis is legitimate here—but supplies no odd factorial depth

I explicitly fix the basis convention requested in the assignment. In the variable


$$
\zeta=\frac{y+1}{2},
$$


use the source’s basis


$$
h_0=1,\qquad
h_{2d+1}(\zeta)=\zeta(\zeta^2-1)^d,\qquad
h_{2d+2}(\zeta)=\zeta^2(\zeta^2-1)^d,
$$


with


$$
D_0=1,\qquad D_{2d+1}=D_{2d+2}=2^d d!,
\qquad \psi_i=h_i/D_i.
\tag{6}
$$



For the row space of degree at most $r$, the basis


$$
\psi_i((y+1)/2),\qquad 0\le i\le r,
$$


is triangular relative to $1,y,\ldots,y^r$, with diagonal entries


$$
\frac{2^{-i}}{D_i}.
$$


Every nonconstant member vanishes at $y=-1$.

For $p>3n$, every $D_i$ occurring here is a $p$-unit. The same is true of the scales through degree $n$ used to express $Q$. Consequently these are invertible changes of basis over $\mathbb Z_p$.

This has two precise consequences:

1. The pole rank computed below is also the pole rank in the **actual shifted regular divided-difference basis**.
2. Changing to that basis multiplies both determinant coefficients by the square of a $p$-unit determinant, so it preserves their valuations and the local final-gcd calculation.

No dyadic valuation is being transferred to an odd prime. Indeed, in this moving-prime window the factorial scales in (6) are units and provide **no odd-prime depth at all**. The new depth comes from the sparse arctangent pole and its position relative to the endpoint row.

For transparent rank calculations I use the triangular endpoint basis $1,u_1,\ldots,u_r$. The preceding argument verifies exactly its relationship to the requested shifted divided basis.

---

## 3. Exact rank of the highest arctangent pole

Let


$$
L_v=4\sum_{a=1}^{v}\frac{(-1)^{v-a}}{2a-1}.
$$


Because $p>3n$ and all denominators in $R$ are at most $4n-3$, the only denominator divisible by $p$ that can occur is $p$ itself. In particular,


$$
v_p(\ell)=1,\qquad pR\in M_k(\mathbb Z_p).
$$



For $0\le v\le2n-1$,


$$
pL_v\equiv
\begin{cases}
0,&v<t_p,\\
4(-1)^{v-t_p},&v\ge t_p
\end{cases}
\pmod p.
\tag{7}
$$


The factorial contribution to $pR$ is zero modulo $p$, since that contribution was already integral.

Therefore, in the monomial basis,


$$
(pR)_{ij}\equiv
4\sum_{a+i+j\ge t_p}Q_a(-1)^{a+i+j-t_p}
\pmod p.
\tag{8}
$$



Let $d=d_p$, and set $D=t_p-d$. Equation (8) shows:

* the entry is zero whenever $i+j<D$;
* on the first possible nonzero anti-diagonal $i+j=D$, it equals $4Q_d$, a nonzero residue.

If $D>2r=n-1$, the entire residue matrix is zero and $h_p=0$.

Otherwise define


$$
h=2r-D+1=n+d-t_p.
$$


The first $k-h$ rows and columns are zero. The trailing $h\times h$ block is anti-triangular, and its anti-diagonal entries are all $4Q_d$. Its determinant is


$$
(-1)^{h(h-1)/2}(4Q_d)^h\ne0\pmod p.
\tag{9}
$$


Hence


$$
\boxed{\operatorname{rank}_{\mathbb F_p}(pR\bmod p)=h_p.}
\tag{10}
$$



This proves the rank hypothesis for the actual polynomial at every index and prime under consideration. It accommodates a drop in the leading coefficient: a smaller $d_p$ produces a smaller pole rank and **more** forced common content.

### Why the endpoint row lies in the zero part

For $0\le j\le r$, the largest denominator in $R_{0j}$ is at most


$$
2(n+r)-1=3n-2<p.
$$


Thus the entire first row and column of $R$ are $p$-integral.

Passing from monomials to $1,u_1,\ldots,u_r$ subtracts multiples of this row and column. It leaves the residue of $pR$ unchanged. In particular, the trailing block in (9) lies entirely inside the lower block $H$, while the distinguished endpoint coordinate lies in the zero part.

That endpoint placement—not rank alone—is what makes the common factor the same for both complete determinant coefficients.

---

## 4. An exact all-depth cancellation identity

Write


$$
\ell=pu,\qquad u\in\mathbb Z_p^\times,
$$


and define the integral full bordered matrix


$$
\mathcal T=
\begin{pmatrix}
t&z^T\\
z&K
\end{pmatrix}
=\ell R_{\rm end}.
\tag{11}
$$


Thus $\det\mathcal T=A$.

Assume first $h=h_p>0$, and partition off its last $h$ coordinates:


$$
\mathcal T=
\begin{pmatrix}
\mathcal T_{II}&\mathcal T_{IJ}\\
\mathcal T_{JI}&\mathcal D
\end{pmatrix},
\qquad |I|=s=s_p.
\tag{12}
$$


By §3, $\mathcal D$ is invertible over $\mathbb Z_p$, and every entry outside $\mathcal D$ is divisible by $p$.

Consequently


$$
\mathcal E
=\frac1p\left(
\mathcal T_{II}
-\mathcal T_{IJ}\mathcal D^{-1}\mathcal T_{JI}
\right)
\in M_s(\mathbb Z_p).
\tag{13}
$$


This is an exact rational Schur complement, not a truncated expansion. Let $\mathcal E_0$ be the principal submatrix obtained by deleting the endpoint coordinate from $\mathcal E$. For $s=1$, use $\det\mathcal E_0=1$.

The determinant formula gives


$$
\boxed{A=p^s\det(\mathcal D)\det(\mathcal E).}
\tag{14}
$$



Deleting the endpoint coordinate before taking the same Schur complement gives


$$
\det K=p^{s-1}\det(\mathcal D)\det(\mathcal E_0).
$$


Thus


$$
\boxed{
B=p^s u w\det(\mathcal D)\det(\mathcal E_0).
}
\tag{15}
$$



If $h=0$, set $\det\mathcal D=1$ and $\mathcal E=\mathcal T/p$. Equations (14)–(15) remain valid.

Because $\det\mathcal D$ is a $p$-unit, the exact final content is


$$
\boxed{
v_p(g)
=s+
\min\!\left\{
v_p(\det\mathcal E),
\ v_p(w)+v_p(\det\mathcal E_0)
\right\}.
}
\tag{16}
$$


Both quantities in the minimum are nonnegative. This proves (4).

Most importantly, the actual reduced denominator satisfies the all-depth identity


$$
\boxed{
v_p(q^{\rm cen})
=
\max\!\left\{
0,\,
v_p(w)+v_p(\det\mathcal E_0)
-v_p(\det\mathcal E)
\right\}.
}
\tag{17}
$$



Equation (17) retains the final gcd. It does **not** claim that the remaining two determinants are units.

Finally, $d_p\le n$ implies


$$
h_p\le 2n-\frac{p+1}{2}.
$$


For the stated prime window the right-hand side is positive, so


$$
s_p=k-h_p\ge
\frac{n+1}{2}-2n+\frac{p+1}{2}
=\frac{p-3n+2}{2}.
$$


This proves (5).

---

## 5. A quantitative universal divisor of the final common content

Define the explicit integer


$$
\mathfrak C_n
=
\prod_{\substack{p\ {\rm prime}\\3n<p\le4n-3}}
p^{(p-3n+2)/2}.
\tag{18}
$$


Since $n,p$ are odd, the exponents are integers. Equation (5) proves


$$
\boxed{\mathfrak C_n\mid \gcd(A,B)}
\qquad(n=4^j+1,\ j\ge1).
\tag{19}
$$



This divisor is independent of the unknown reductions of $Q$. Using the actual $d_p$ can only improve it.

By the prime number theorem, in its standard weighted form,


$$
\begin{aligned}
\log\mathfrak C_n
&=\frac12\sum_{3n<p\le4n-3}(p-3n+2)\log p\\
&=\frac12\int_{3n}^{4n}(x-3n)\,dx+o(n^2)\\
&=\boxed{\frac14n^2+o(n^2)}.
\end{aligned}
\tag{20}
$$



Thus the chosen bordered integers contain an unavoidable common factor of size


$$
\exp\!\left(\frac14n^2+o(n^2)\right).
$$



### Scope

This is a substantial forced cancellation of the **specified** integers $A,B$. It is not invariant under arbitrarily rescaling both integers, which is why fixing $\ell,Q,K,z,A,B$ matters.

It does imply the valid bound


$$
q^{\rm cen}\le \frac{|B|}{\mathfrak C_n},
$$


but it does not make the previous coarse $O(n^3\log n)$ logarithmic bound sharp enough. Nor does it prove that any prime in this window survives in $q^{\rm cen}$.

The gain is an exact removal of a large, explicitly located part of the arithmetic problem, together with the smaller local pair in (17).

---

## 6. What remains after the new cancellation

The original unproved corank-one hypothesis has not been repackaged as a theorem. Instead, the high-prime block has been eliminated using a rank hypothesis proved directly for this family.

The residual issue is now visible in (17):


$$
\det\mathcal E
\quad\hbox{versus}\quad
w\det\mathcal E_0.
$$


Although $\mathcal E$ is $p$-integral, nothing proved here prevents these quantities from sharing additional, arbitrarily deep content.

The dimension is genuinely reduced:


$$
s_p=k-h_p.
$$


When $d_p=n$,


$$
s_p=\frac{p-3n+2}{2}.
\tag{21}
$$


Thus primes near the lower edge of the window leave a much smaller residual bordered problem. But asserting $d_p=n$, or controlling the residual endpoint coupling uniformly, requires further work.

No factorial-depth survival at $3$ or $5$, and no sharp total odd-$q$ bound, is proved in this turn.

---

## 7. Secondary audit of A3’s varying inverse-power filter

### 7.1 The varying filter cancellation is correct

Let


$$
g(T)=1+6T+T^2,\qquad g(T)^m=\sum_{j=0}^{2m}a_{m,j}T^j,
$$


and let $z=-3+2\sqrt2$, a root of $g$. Since $z$ has multiplicity $m$ in $g^m$,


$$
\sum_j a_{m,j}z^j j^\ell=0,\qquad 0\le\ell<m.
$$


Therefore


$$
\sum_j a_{m,j}z^j(n+j)^{m-1-h}=0,
\qquad 0\le h\le m-1.
$$


A3’s rational weighting consequently annihilates the stated finite inverse-power block exactly.

Its denominator formula


$$
\widetilde Q=\frac{DL}{\gcd(|N|,DL)}
$$


is also correct. Neither exact annihilation nor this gcd formula proves nonvanishing or a useful rate for the actual filtered error.

### 7.2 The separate exponential-tail formula is correct with an important cutoff convention

A3’s displayed exponential-tail amplitude corresponds to truncating $B_ke^x$ **through degree $2k+2$**, the degree immediately below the contact order $2k+3$.

For $N\ge j$, Taylor’s integral remainder gives


$$
\sum_{\ell=N+1}^{\infty}\frac1{(\ell-j)!}
=
\frac1{(N-j)!}\int_0^1e^x(1-x)^{N-j}\,dx.
$$


Taking $N=2k+2$, summing for $j=0,1,2$, and dividing by $Y_k$ gives exactly


$$
E_k^{\exp}
=\int_0^1e^x(1-x)^{2k}
\frac1{Y_k}\left(
\frac{B_{k,2}}{(2k)!}
+\frac{B_{k,1}}{(2k+1)!}(1-x)
+\frac{B_{k,0}}{(2k+2)!}(1-x)^2
\right)dx.
$$


Thus the formula is valid.

It is not the same separate exponential tail obtained by truncating at degree $k$, as in the lower-cutoff projection decomposition. The **sum of both tails** agrees after the contact equations are used; the individual tails depend on the chosen cutoff.

With that convention made explicit, A3’s argument that


$$
P_k(0)\ne0\ \text{eventually},\qquad
\log|P_k(0)|=-k\log k+O(k)
$$


is justified by the supplied eventual cofactor and endpoint asymptotics. The narrow fixed-amplitude exclusion is valid. It excludes neither a combined-tail moment representation nor a different decomposition.

---

## 8. Whole error and nonvanishing retained

The arithmetic work above changes no center. With the actual stationary polynomial $F_n$ from the supplied bordered interface, the complete evaluated error remains


$$
q_n^{\rm cen}(e+\pi)-p_n^{\rm cen}
=
\frac{q_n^{\rm cen}}{Q_n(-1)}
\int_0^1
\left(e^x+\frac4{1+x^2}\right)
Q_n(x^2)F_n(x^2)^2\,dx.
\tag{22}
$$


Neither period contribution has been removed.

The inherited dyadic theorem gives


$$
v_2(q_n^{\rm cen})=n+2
$$


on the regular subfamily. Subject to that explicitly retained dependency, the centers are pairwise distinct, so at most one complete error in (22) can vanish. This provides eventual nonvanishing without assuming irrationality. The new odd-prime theorem itself uses no dyadic valuation argument.

---

## Handoff

### (1) New result and proof status

**Proved here:**

* the exact highest-pole rank
  

$$
\operatorname{rank}(pR\bmod p)
  =\max\!\left(0,n+d_p-\frac{p+1}{2}\right);
$$


* the all-depth Schur-complement cancellation identities (14)–(17) for the actual bordered pair;
* the unconditional common-content divisor
  

$$
\mathfrak C_n\mid\gcd(A,B),\qquad
  \log\mathfrak C_n=\tfrac14n^2+o(n^2);
$$


* the compatibility of this analysis with the actual shifted divided-difference basis, using only odd-prime unit transformations;
* A3’s varying-filter algebra and its separate-tail claim, with the necessary contact-order cutoff specified.

These are author-level exact derivations. No finite data are used to establish the infinite statements.

### (2) Exact remaining bottleneck

For the moving-prime block, the remaining arithmetic is the **smaller actual pair**


$$
\det\mathcal E,\qquad w\det\mathcal E_0
$$


in (17). Its shared content is still uncontrolled.

More broadly, neither the aggregate actual odd denominator nor the signed whole-error rate is bounded sharply enough. The new cancellation theorem does not decide irrationality and does not exclude the weighted regular family. The project remains open.

### (3) Bounded computation request

A modest normalization check would be useful, not as evidence for an infinite pattern:

* **Input:** $n=5$, its exact primitive $Q$ from the defining derangement constraints, and $p=17$.
* **Compute:** the exact $Q,R,\ell,t,z,K,A,B$; $d_{17}$; the residue $17R\bmod17$; and the Schur matrices $\mathcal D,\mathcal E,\mathcal E_0$ from §4.
* **Expected verifiable output:**
  1. the defining orthogonality equations for $Q$;
  2. the residue rank predicted by (10);
  3. exact rational verification of (14) and (15);
  4. the final gcd and agreement of its $17$-valuation with (16).
* **Resource bound:** one $5\times5$ rational solve, one $3\times3$ complete matrix, and their exact determinants; no factoring of large general integers is necessary beyond repeated division by $17$.

This checks normalization and endpoint placement. The proofs above, not that check, establish the all-index cancellation theorem.
