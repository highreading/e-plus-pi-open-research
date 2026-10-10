> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A1 research result: an exact odd-content interface and a complete evaluated-error identity

I use the supplied exact dyadic theorem as established on the assigned domain


$$
\mathcal N=\{4^j+1:j\ge1\}.
$$


In particular, I do **not** repeat its mod-$8$ argument or import any valuation from the excluded raw or fixed-$b$ families.

The results below give:

* an exact odd-prime endpoint identity in a smaller bordered matrix;
* an all-depth odd-prime survival criterion;
* an explicit, though presently too large, total reduced-denominator bound;
* an exact integral formula for the **whole** evaluated error of this same center;
* unconditional eventual nonvanishing of that error, with at most one exceptional index in $\mathcal N$.

They do not establish shrinking primitive forms or decide the irrationality of $e+\pi$.

---

## 1. Start with the complete determinant

Fix $n\in\mathcal N$, and put


$$
k=\frac{n+1}{2},\qquad r=k-1.
$$


Write $Q(y)=q_n(y)$ for the supplied primitive integer orthogonal polynomial, with positive leading coefficient:


$$
\sum_{a=0}^n Q_a\bigl(d_{2(a+s)}-(-1)^{a+s}\bigr)=0,
\qquad 0\le s<n.
$$


Thus $Q$ is not the denominator of the center. Set


$$
w=Q(-1),\qquad v_i=(-1)^i,\quad 0\le i<k.
$$


The complete rational matrix is


$$
R_{ij}=-\sum_{a=0}^n Q_a(2(i+j+a))!
       +\sum_{a=0}^n Q_a L_{i+j+a},
$$


where


$$
L_s=4\sum_{h=0}^{s-1}\frac{(-1)^h}{2s-1-2h},
\qquad L_0=0.
$$


All these rational arctangent terms remain present. With $S=e+\pi$,


$$
\boxed{\det(R+Swvv^T)=\alpha+\beta S,}
$$




$$
\alpha=\det R,\qquad \beta=w\,v^T\operatorname{adj}(R)v.
$$


The center is


$$
c_n=-\frac{\alpha}{\beta}.
$$



The supplied regular-subfamily results ensure $w\ne0$, $\alpha\ne0$, and $\beta\ne0$. Their established primitive denominator conclusion is


$$
\boxed{v_2(q_n^{\rm cen})=n+2.}                       \tag{1}
$$



Hereafter $q_n^{\rm cen}$ always means the positive denominator of $c_n$ in lowest terms.

---

## 2. New exact identity for the whole evaluated moment matrix

Define


$$
W(x)=e^x+\frac4{1+x^2},\qquad 0\le x\le1.
$$



### Lemma 1 — Complete compact-interval representation

For every $n\in\mathcal N$ and $0\le s<n$,


$$
-\sum_a Q_a(2(s+a))!+\sum_a Q_aL_{s+a}
   +S\,w(-1)^s
=
\int_0^1W(x)x^{2s}Q(x^2)\,dx.                       \tag{2}
$$


Consequently,


$$
\boxed{(R+Swvv^T)_{ij}
 =\int_0^1W(x)Q(x^2)x^{2i}x^{2j}\,dx.}             \tag{3}
$$



#### Proof

For every integer $t\ge0$,


$$
e\,d_{2t}=\int_{-\infty}^1e^x x^{2t}\,dx
=(2t)!+\int_0^1e^x x^{2t}\,dx.
$$


The orthogonality equations therefore give


$$
\sum_aQ_a(2(s+a))!
=e\,w(-1)^s-\int_0^1e^x x^{2s}Q(x^2)\,dx.
$$


Polynomial division also gives the exact identity


$$
4\int_0^1\frac{x^{2t}}{1+x^2}\,dx
=\pi(-1)^t+L_t.
$$


Multiply by $Q_a$, sum with $t=s+a$, and combine the two identities. Since
$i+j\le2k-2=n-1$, all matrix entries lie in the orthogonality domain. ∎

This is an identity for the entire evaluated expression, not a first omitted coefficient or one selected tail.

---

## 3. A smaller rational block and the exact final gcd

The rank-one direction can be isolated by an integral change of basis. Put


$$
u_i(y)=y^i-(-1)^i,\qquad 1\le i\le r.
$$


Each $u_i$ vanishes at $y=-1$. The basis


$$
1,u_1,\ldots,u_r
$$


is obtained from the monomial basis by a unimodular integer matrix $U$ satisfying


$$
U^Tv=e_0.
$$



Write


$$
U^TRU=
\begin{pmatrix}
a&b^T\\
b&H
\end{pmatrix}.                                      \tag{4}
$$


Explicitly,


$$
a=R_{00},\qquad b_i=R_{0i}-(-1)^iR_{00},
$$




$$
H_{ij}=R_{ij}-(-1)^jR_{i0}-(-1)^iR_{0j}
                  +(-1)^{i+j}R_{00}.                \tag{5}
$$


Then


$$
U^T(R+Swvv^T)U=
\begin{pmatrix}
a+Sw&b^T\\
b&H
\end{pmatrix}.                                      \tag{6}
$$


In particular,


$$
\boxed{\beta=w\det H.}                              \tag{7}
$$


Thus $H$ is nonsingular on the entire assigned domain.

For explicit integer normalization, take


$$
\ell_n=\operatorname{lcm}\{1,3,5,\ldots,4n-3\}.
$$


This clears every entry of $R$, since the largest occurring $L$-index is $2n-1$. Define


$$
t=\ell_n a,\qquad z=\ell_n b,\qquad K=\ell_n H.
$$


All are integral. Set


$$
\Delta=\det K,\qquad
A=t\Delta-z^T\operatorname{adj}(K)z,\qquad
B=\ell_n w\Delta.                                   \tag{8}
$$


The determinant scalings give exactly


$$
\alpha=\frac{A}{\ell_n^k},\qquad
\beta=\frac{B}{\ell_n^k}.                             \tag{9}
$$



Therefore, with the **final endpoint gcd**


$$
g=\gcd(|A|,|B|),
$$


the fully reduced center is


$$
\boxed{
p_n^{\rm cen}=-\frac{\operatorname{sgn}(B)A}{g},
\qquad
q_n^{\rm cen}=\frac{|B|}{g}.
}                                                   \tag{10}
$$


This normalization cancels every common endpoint factor. Neither $\ell_n$ nor any content of $K$ is being identified with $q_n^{\rm cen}$.

---

## 4. New all-index odd-prime lemma

### Lemma 2 — Exact local endpoint identity and a full-depth survival test

For every odd prime $p$ and every $n\in\mathcal N$,


$$
\boxed{
v_p(q_n^{\rm cen})
=
\max\!\left\{
0,\,
v_p(\ell_n)+v_p(w)+v_p(\Delta)
-v_p\!\left(t\Delta-z^T\operatorname{adj}(K)z\right)
\right\}.
}                                                   \tag{11}
$$



Suppose additionally that $K\bmod p$ has corank exactly one. Let
$h\in\mathbf F_p^r\setminus\{0\}$ span its radical. If


$$
z^Th\not\equiv0\pmod p,                              \tag{12}
$$


then $A$ is a $p$-unit and


$$
\boxed{
v_p(q_n^{\rm cen})
=v_p(\ell_n)+v_p(w)+v_p(\Delta).
}                                                   \tag{13}
$$


Thus all of the indicated determinant depth survives the complete final gcd.

#### Proof

Equation (11) follows directly from (8)–(10).

For the second assertion, a symmetric matrix of corank one over $\mathbf F_p$ has


$$
\operatorname{adj}(K)=\lambda hh^T
$$


for some nonzero $\lambda\in\mathbf F_p$. Indeed, the adjugate is nonzero of rank one, its columns lie in the radical, and symmetry gives the displayed form. Since $\Delta=0\bmod p$,


$$
A=-z^T\operatorname{adj}(K)z
=-\lambda(z^Th)^2\ne0\pmod p.
$$


Hence $v_p(A)=0$, proving (13) at every depth of $\Delta$. ∎

### Why this criterion is useful—and what it does not prove

The criterion distinguishes two genuinely different phenomena:

* a singular lower block with nonzero coupling contributes denominator factors;
* a singular lower block with zero coupling is precisely where endpoint cancellation may occur.

It is therefore not enough to find large content or singularity in a Gram block. One must examine its coupling to the distinguished endpoint row.

No assertion is made here that condition (12) holds uniformly at any fixed odd prime. The lemma is an all-index implication, not a finite-prime certificate.

---

## 5. An explicit total reduced-denominator bound

A crude total bound can be obtained without replacing $q_n^{\rm cen}$ by a coefficient clearer.

Put


$$
M_n=(4n-2)!+1,\qquad
T_n=n^{n/2}M_n^n.
$$


The $n\times(n+1)$ coefficient matrix defining $Q$ has entries


$$
C_{s+a}=d_{2(s+a)}-(-1)^{s+a}
$$


with absolute value at most $M_n$, because $s+a\le2n-1$.
Its signed maximal minors give an integer vector on the orthogonal ray.
Hadamard’s inequality bounds each such minor by $T_n$. Passing to its primitive vector cannot increase its coefficients. Thus


$$
|Q_a|\le T_n,\qquad |w|\le(n+1)T_n.                  \tag{14}
$$



Also,


$$
|L_s|\le4s\le8n-4.
$$


It follows that every entry of $R$ has absolute value at most


$$
E_n=(n+1)T_n\bigl((4n-2)!+8n\bigr).
$$


By (5), entries of $K$ have absolute value at most $4\ell_nE_n$. Hence


$$
|\Delta|\le r^{r/2}(4\ell_nE_n)^r.
$$


Using the **actual** reduction (10),


$$
\boxed{
q_n^{\rm cen}
\le |B|
\le
\ell_n(n+1)T_n\,r^{r/2}(4\ell_nE_n)^r.
}                                                   \tag{15}
$$


In particular,


$$
\log q_n^{\rm cen}=O(n^3\log n).                     \tag{16}
$$



This is a proved total upper bound, but it is not close to a useful approximation budget. It discards potentially enormous final cancellation and therefore cannot support an exponential-error irrationality argument.

Combining (1) and (10), it is convenient to isolate the actual odd part:


$$
\boxed{q_n^{\rm cen}=2^{n+2}o_n,\qquad o_n\text{ a positive odd integer}.} \tag{17}
$$


The exact identities above determine $o_n$; they do not yet give a sharp asymptotic bound for it.

---

## 6. The complete evaluated error as a constrained quadratic integral

Define the signed functional


$$
\mathcal J_n(f)
=\int_0^1W(x)Q(x^2)f(x^2)\,dx.
$$


From (3)–(6),


$$
\mathcal J_n(1)=a+Sw,\quad
\mathcal J_n(u_i)=b_i,\quad
\mathcal J_n(u_iu_j)=H_{ij}.
$$


The latter two quantities are rational: their period responses vanish because every $u_i(-1)=0$.

Set


$$
d=H^{-1}b,\qquad
F_n(y)=1-\sum_{i=1}^r d_i u_i(y).                    \tag{18}
$$


Then $F_n\in\mathbf Q[y]$, $\deg F_n\le r$, and


$$
F_n(-1)=1,\qquad \mathcal J_n(F_nu_i)=0.
$$


Expansion gives


$$
\mathcal J_n(F_n^2)
=a+Sw-b^TH^{-1}b.
$$


On the other hand,


$$
\alpha=\det H\,(a-b^TH^{-1}b),\qquad \beta=w\det H.
$$


Consequently:

### Lemma 3 — Exact whole-error identity

For every $n\in\mathcal N$,


$$
\boxed{
S-c_n
=
\frac1w
\int_0^1
\left(e^x+\frac4{1+x^2}\right)
Q(x^2)F_n(x^2)^2\,dx.
}                                                   \tag{19}
$$


The associated primitive integer form is exactly


$$
\boxed{
q_n^{\rm cen}S-p_n^{\rm cen}
=
\frac{q_n^{\rm cen}}{w}
\int_0^1
\left(e^x+\frac4{1+x^2}\right)
Q(x^2)F_n(x^2)^2\,dx.
}                                                   \tag{20}
$$



These formulas retain both period contributions, the actual rational center, and its final gcd.

### Exact analytic obstruction

Although $W(x)>0$ and $F_n(x^2)^2\ge0$, the weight also contains $Q(x^2)$. Its sign on $[0,1]$ has not been controlled by the supplied results. Thus (19) is **not** a positive-measure norm identity.

In particular, it is invalid to infer positivity, a lower bound, or an asymptotic decay rate merely from the square in (19). One needs either:

1. a signed asymptotic analysis of this integral, including the dependence of $F_n$ on $n$; or
2. a separate structural sign theorem for the corresponding constrained signed form.

Also, $F_n$ is obtained by stationarity for a possibly indefinite form. Calling it a minimizing polynomial would require an additional definiteness theorem.

---

## 7. Eventual nonvanishing follows without assuming irrationality

There is nevertheless an unconditional nonvanishing consequence of the already established primitive dyadic depths.

### Lemma 4 — At most one exact zero on the regular subfamily

Among $n\in\mathcal N$, at most one can satisfy


$$
S-c_n=0.
$$


Hence the complete errors in (19) are nonzero for every sufficiently large $n\in\mathcal N$.

#### Proof

If $S=c_n=c_N$, then these are the same rational number. A rational number has a unique positive reduced denominator. But (1) gives


$$
v_2(q_n^{\rm cen})=n+2,\qquad
v_2(q_N^{\rm cen})=N+2,
$$


so equality of the denominators forces $n=N$. ∎

This proves eventual nonvanishing without knowing whether $S$ is rational. It does not give an effective exceptional-index bound or the sign of the error.

A related exact separation law is available. If $n<N$ belong to $\mathcal N$, then the reduced numerators are odd, and


$$
v_2\!\left(
p_n^{\rm cen}q_N^{\rm cen}
-p_N^{\rm cen}q_n^{\rm cen}
\right)=n+2.
$$


Therefore


$$
\boxed{
|c_n-c_N|
\ge\frac{2^{n+2}}{q_n^{\rm cen}q_N^{\rm cen}}
=\frac1{2^{N+2}o_no_N}.
}                                                   \tag{21}
$$


In particular,


$$
|S-c_n|+|S-c_N|
\ge\frac1{2^{N+2}o_no_N}.                             \tag{22}
$$


This is an all-index compatibility restriction on any future simultaneous odd-content and error estimates.

---

## 8. What remains open in this parameter window

The present work does **not** exclude the regular weighted family. It supplies exact interfaces, but neither favorable nor unfavorable asymptotic rates have been established.

For this same center, the precise target is now


$$
\boxed{
\frac{2^{n+2}o_n}{|w|}
\left|
\int_0^1W(x)Q(x^2)F_n(x^2)^2\,dx
\right|
\longrightarrow0.
}                                                   \tag{23}
$$


The eventual nonzero qualification is already supplied by Lemma 4.

The next unexcluded window is therefore still


$$
n=4^j+1,\quad k=(n+1)/2,
$$


not a neighboring excluded raw or fixed-$b$ center. More specifically, the next arithmetic target is the odd local coupling in Lemma 2; the next analytic target is the signed constrained integral in Lemma 3.

The coarse bound (15) is inadequate, but an inadequate upper bound is **not** a proof that favorable bounds fail. No family exclusion follows from it.

---

## Final handoff

### (1) New result and proof status

**Proved here:**

* the complete compact-interval matrix identity (2)–(3);
* the bordered integer endpoint pair (8), with its actual final gcd and primitive denominator (10);
* the exact odd-prime identity (11) and all-depth corank-one survival criterion (13);
* the explicit total denominator upper bound (15);
* the complete constrained integral error (19)–(20);
* at most one zero error on the assigned infinite subfamily, hence unconditional eventual nonvanishing;
* the exact dyadic separation bound (21).

These are author-level derivations, not claimed independent audits. No finite computation was used.

### (2) Exact remaining bottleneck

Obtain quantitative control of **both**


$$
o_n=\frac{q_n^{\rm cen}}{2^{n+2}}
\quad\text{and}\quad
\frac1w\int_0^1W(x)Q(x^2)F_n(x^2)^2\,dx
$$


for the same $n=4^j+1$ center.

The arithmetic issue is endpoint coupling and cancellation, not merely Gram content. The analytic issue is a signed integral, not a positive square norm. Neither issue is settled by the dyadic theorem.

### (3) Bounded computation request

**None requested at this stage.** The new lemmas are exact symbolic statements. A small-index factorization or numerical error table would not decide their missing infinite rate estimates, so I do not propose one as a substitute.

The irrationality of $e+\pi$ remains unresolved by this work.
