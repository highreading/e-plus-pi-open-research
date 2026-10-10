> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 5 — Exact seed elimination in the endpoint quotient, new primewise cancellation laws, and the remaining projected-content problem

## Executive conclusion

The irrationality or rationality of $e+\pi$ remains unresolved.

The completed $n=3375$ computation and its whole-form enclosure are accepted at their stated **finite** scope. No regeneration of $n=225$, $n=3375$, or the direct $n=17$ validation is proposed.

The principal new result is an exact coefficient identity that identifies where the actual factorial seed enters—and where it disappears:


$$
\boxed{u_k(n)=E_n h_k(n)+g_k(n),\qquad h_k,g_k\in\mathbb Z[n].}
$$


Here $h_k$ is the actual homogeneous reference coefficient, and $g_k$ is an explicitly given, zero-seeded forced polynomial. At the three terminal rows, this yields


$$
\boxed{
\frac{v_j^{\rm rec}}{u_j^{\rm rec}}
=
\frac{E_nR_j+C_j}{n!R_j},
\qquad R_j,C_j\in\mathbb Z,
}
$$


with the **complete logarithmic force and exterior correction included in $C_j$**.

Consequently, at every $p>n+2$,


$$
\boxed{
v_p(d_j)=\max\{0,v_p(R_j)-v_p(C_j)\}.
}
$$


More precisely, if


$$
g=v_p(G_j),\qquad x=v_p(\xi_j),\qquad c=v_p(C_j),
$$


then


$$
\boxed{
\begin{aligned}
v_p(\gamma_j)&=(g-c)_+,\\
v_p(\mathcal C_j^\sharp)&=\min\{x,(c-g)_+\},\\
v_p(d_j)&=(g+x-c)_+.
\end{aligned}}
\tag{E1}
$$


This isolates the endpoint-specific force/cancellation factor after the already controlled common structural factor has been separated. In particular, the large-prime projected cancellation is **independent of the additive seed term $E_n$**. A congruence proving that $E_n$ is a unit cannot, by itself, exclude that cancellation: the seed lies exactly in the reference direction that the relevant quotient removes.

There are also new bounds at previously unhandled small primes:

1. For every prime $p\ge5$ dividing $n-1$,
   

$$
\boxed{
   v_p(\gamma_0)=v_p(\gamma_3)=2v_p(n!),\qquad
   v_p(\zeta_0)=v_p(\zeta_3)=0,
   }
   \tag{E2}
$$


   and therefore
   

$$
\boxed{
   v_p(d_j)=2v_p(n!)+v_p(\xi_j).
   }
   \tag{E3}
$$


   Thus the endpoint-specific exponential/logarithmic cancellation is completely excluded at these primes, without assuming that the reference projection is a unit.

2. For every odd $p\mid n+1$, on the original odd-index domain,
   

$$
\boxed{
   v_p(\gamma_0),v_p(\gamma_3)\le2v_p(n!),
   \qquad
   v_p(d_j)\le2v_p(n!)+v_p(\xi_j).
   }
   \tag{E4}
$$


   The endpoint-$0$ primitive-row reduction, missing in Turn 4, is proved below.

3. At $2$, the actual force has the valid prime-power index period
   

$$
\boxed{
   u_{k+2^{s+1}}(n)\equiv u_k(n)\pmod{2^s},
   }
   \tag{E5}
$$


   and the endpoint-$3$ normalization satisfies
   

$$
\boxed{
   v_2(\gamma_3)\le
   \begin{cases}
   2v_2(n!)-1,&n\equiv1\pmod4,\\
   2v_2(n!),&n\equiv3\pmod4.
   \end{cases}}
   \tag{E6}
$$



These are proofs on their stated domains, not extrapolations from the completed numerical examples. They do not yet provide a sufficiently strong bound on the large-prime endpoint-specific projected contents.

---

## 1. Scope and completed finite evidence

The index domain remains


$$
n=15^r,\quad r\ge2,
\qquad\text{or}\qquad
n=105^r,\quad r\ge2.
$$



Throughout, I retain:

- the original $3\times3$ contact matrix;
- both corrected four-coordinate reconstructed columns;
- the original complete force through exactly $2n+2$;
- the complete logarithmic-force identity at its established three-row scope;
- the terminal return;
- the exterior $+1$;
- the least clearer over all eight reconstruction entries;
- the actual row contents and primitive endpoint triples;
- the all-prime final gcd;
- the actual primitive denominator;
- the same-index whole error.

The coefficient identities below are exact reorganizations of that construction. In particular, using a coefficient formula for the three contact-force entries does **not** shorten the underlying complete forcing range.

### 1.1 The $n=3375$ results are now complete

The supplied source, receipt, and A4’s independent algebraic review support the following finite conclusions:



$$
\boxed{(g_0,g_1,g_2,g_3)=(113940000,9780750,10125,1)}
$$


for the four actual reconstruction row contents.

The actual imbalance satisfies:

- $|AB|$ has $50546$ digits;
- its complementary part above $3377=n+2$ has $50539$ digits;
- its selected $3/5$-part is $16875=3^3 5^4$;
- its complete part at primes at most $3377$ is
  

$$
3^3 5^4\cdot7\cdot19\cdot31.
$$



At both endpoints,


$$
\gamma_{\rm large}=\mathcal C^\sharp_{\rm large}=1,
\qquad W=1.
$$



The five whole-form results are:

| Probe | Sign | $\lfloor\log_{10}|q(e+\pi)-p|\rfloor$ |
|---|---:|---:|
| Endpoint $3$ | $-$ | $43069$ |
| Endpoint $0$ | $-$ | $43068$ |
| Half | $-$ | $68342$ |
| $n^2/2$ | $+$ | $68338$ |
| Reference-canceling | $-$ | $31327$ |

All five are nonzero and have absolute value greater than $1$.

These are completed, rigorously enclosed finite evaluations. They are not an infinite exclusion theorem.

### 1.2 Closed structural results are reused, not reproved

I retain:

- the all-prime primitivity of consecutive factorial-normalized moment triples;
- the exact common normalized-defect law;
- A4’s exclusion of $13$ from $W_n$;
- the conclusion that
  

$$
(W_n)_{>n+2}
$$


  is either $1$ or one prime to exponent $1$;
- the accepted large-prime two-kernel comparisons at their normalization-unit scope;
- the stronger previously established selected-part law $5n$ on the smooth families, rather than treating the weaker $n\mid |AB|$ as the current target.

The fifteen-state moment–force connection remains correct. Its determinant does not establish projected-pair primitivity. The new work below concerns the actual projected arithmetic.

---

## 2. Audit of the fixed-seed congruences

Write


$$
q(z)=1-z+\frac{z^2}{2},
\qquad
a_k(n)=k![z^k]e^zq(z)^n,
$$


and


$$
u_k(n)=k![z^k]\Omega_n(z),
\qquad
\Omega_n(z)=q(z)^n
\frac{d^n}{dz^n}\left(\frac{e^z}{1-z}\right).
$$



### 2.1 Factorial-normalized coefficients of $q^n$ are integer polynomials

Put


$$
b_r(n)=r![z^r]q(z)^n.
$$


With $w(z)=-z+z^2/2$,


$$
q(z)^n=\sum_{m\ge0}(n)_m\frac{w(z)^m}{m!}.
$$


For $r=m+\ell$, $0\le\ell\le m$,


$$
r![z^r]\frac{w(z)^m}{m!}
=
(-1)^{m-\ell}
\frac{(m+\ell)!}{(m-\ell)!\,\ell!\,2^\ell}.
$$


The absolute value is an integer: it counts partitions into $m-\ell$ singletons and $\ell$ unordered pairs.

Therefore


$$
\boxed{b_r(n)\in\mathbb Z[n].}
\tag{2.1}
$$



This establishes the needed polynomial integrality at $2$ as well as at odd primes. Merely observing that the ordinary coefficients are dyadic would not establish congruence in $n$ modulo powers of $2$.

The exact force formula


$$
u_k(n)=
\sum_{r=0}^k\binom{k}{r}b_r(n)E_{n+k-r}
$$


then proves the claimed congruence in $n$, using the already proved periodicity of $E_m$:


$$
n'\equiv n\pmod{p^s}
\quad\Longrightarrow\quad
u_k(n')\equiv u_k(n)\pmod{p^s}.
$$



### 2.2 The negative-index issue in the odd-prime period proof

For $M=p^s$, define the actual integer polynomial


$$
S_M(X)=\sum_{r=0}^{M-1}(X)_r.
$$


For every nonnegative $m$,


$$
E_m\equiv S_M(m)\pmod M.
$$



For fixed nonnegative $n$, write


$$
q(z)^n=\sum_{r=0}^{2n}q_rz^r.
$$


When $p$ is odd, the polynomial


$$
\sum_{r=0}^{2n}q_r(K)_rS_M(n+K-r)
$$


belongs to $\mathbb Z_p[K]$, and agrees with $u_k(n)$ modulo $p^s$ at every nonnegative integer $K=k$.

If $r>k$, the factor $(k)_r$ is zero. Consequently, an artificially negative argument of $S_M$ contributes nothing to the original coefficient evaluation.

Thus the proof does **not** require defining $E_m$ at negative indices. It uses a polynomial extension of a congruence, with the zero falling-factorial factors retained. This justifies


$$
\boxed{u_{k+p^s}(n)\equiv u_k(n)\pmod{p^s}\qquad(p\text{ odd}).}
\tag{2.2}
$$



### 2.3 New: the corresponding $2$-power force period

For every $s\ge1$,


$$
\boxed{
u_{k+2^{s+1}}(n)\equiv u_k(n)\pmod{2^s}.
}
\tag{2.3}
$$



**Proof.** Set $M=2^{s+1}$, and write


$$
A_n(z)=\frac{d^n}{dz^n}\left(\frac{e^z}{1-z}\right).
$$


Leibniz’s rule gives


$$
u_{k+M}(n)
=
\sum_{r=0}^{M}
\binom Mr
\left.
D^k\bigl((D^rq^n)A_{n+M-r}\bigr)
\right|_{z=0}.
$$



For $r=0$, subtract the corresponding expression with $A_n$. Each coefficient difference contains


$$
E_{n+M+j}-E_{n+j},
$$


which is divisible by $2^s$.

For $r\ge1$, the factorial-normalized coefficients of $D^rq^n$ are $b_{r+j}(n)$, and


$$
v_2(b_{r+j}(n))
\ge
\sum_{\nu\ge2}\left\lfloor\frac{r+j}{2^\nu}\right\rfloor
\ge
\sum_{\nu\ge2}\left\lfloor\frac r{2^\nu}\right\rfloor.
$$


All derivatives of $A_{n+M-r}$ at zero are integers. Hence the $r$-th term has valuation at least


$$
s+1-v_2(r)
+
\sum_{\nu\ge2}\left\lfloor\frac r{2^\nu}\right\rfloor
\ge s.
$$


This proves the claim. ∎

The period $2^{s+1}$, rather than $2^s$, is important. At $s=1$, the odd-$n$ force has period-four parity pattern


$$
0,1,0,0.
$$



### 2.4 Reference units: exact scope

The constant-term formula and Lucas-type digit identity remain valid:


$$
\tau_m=\operatorname{CT}_x
\left(1+x+\frac1{2x}\right)^m,
$$




$$
\tau_{a+pb}\equiv\tau_a\tau_b\pmod p
\qquad(0\le a<p,\ p\text{ odd}).
$$



The complete digit tables for $3,5,7$ contain no zero. Thus $\tau_m$ is a unit at those three primes for every $m$.

This is **not** a unit theorem at all odd primes. Below, whenever an argument at another prime needs a reference unit, that condition is proved or left explicit.

---

## 3. New exact coefficient relation: the seed lies in the reference direction

Define


$$
\mathscr H_n(z)=\frac{q(z)^n}{(1-z)^{n+1}},
\qquad
I_n(z)=\int_0^z e^t(1-t)^n\,dt.
$$



The force differential equation gives


$$
\frac{d}{dz}\bigl((1-z)^{n+1}A_n(z)\bigr)
=e^z(1-z)^n.
$$


Since $A_n(0)=E_n$,


$$
\boxed{
\Omega_n(z)=\mathscr H_n(z)\bigl(E_n+I_n(z)\bigr).
}
\tag{3.1}
$$



This identity uses the actual seed $E_n$; no homogeneous replacement is made.

### 3.1 Integral polynomial coefficients

Put


$$
h_k(n)=k![z^k]\mathscr H_n(z),
$$


and


$$
f_m(n)=m![z^m]e^z(1-z)^n.
$$


Then


$$
h_k(n)=
\sum_{r=0}^k
\binom kr b_r(n)(n+1)^{\overline{k-r}},
$$


and


$$
f_m(n)=
\sum_{r=0}^m(-1)^r\binom mr(n)_r.
$$


Thus


$$
h_k,f_m\in\mathbb Z[n].
$$



Define


$$
g_0(n)=0,\qquad
g_k(n)=
\sum_{m=1}^k
\binom km h_{k-m}(n)f_{m-1}(n)
\quad(k\ge1).
$$


Coefficient extraction in (3.1) proves


$$
\boxed{
u_k(n)=E_nh_k(n)+g_k(n),
\qquad h_k,g_k\in\mathbb Z[n].
}
\tag{3.2}
$$



For example,


$$
(h_0,h_1,h_2)=(1,1,n+2),
$$




$$
(g_0,g_1,g_2)=(0,1,3-n),
$$


recovering the actual initial force values.

Equation (3.2) is an exact affine dependence on the factorial seed, not just a congruence.

### 3.2 At the original terminal rows, $h_k$ is the actual reference column

At precisely the three retained contact rows,


$$
[z^{n+i}]\mathscr H_n(z)
=
\tau_nv_i+\tau_{n+1}w_i,
\qquad 0\le i\le2.
\tag{3.3}
$$


This is the established reference coefficient identity, reused at its original scope.

Therefore the entire $E_n$-dependent part of the exponential contact force is


$$
E_nt,
\qquad
t=\tau_nv+\tau_{n+1}w.
$$



This exact alignment is the key new information for projected content.

---

## 4. Integral terminal columns with complete forcing

Let $N=n+2$, and retain


$$
v'=(2N,N,n+1)^T,\qquad
w'=(0,N,2n+3)^T.
$$



Define the integral reference column


$$
\boxed{\mathbf H=(n+2)!\,t.}
\tag{4.1}
$$


Its integrality also follows directly from the integral $h_k$.

The exterior-corrected exponential column remains


$$
\mathbf U=
\begin{pmatrix}
(n+1)(n+2)(u_n-a_n)\\
(n+2)(u_{n+1}-a_{n+1})\\
u_{n+2}-a_{n+2}
\end{pmatrix}.
$$



Define


$$
\mathbf B=
\begin{pmatrix}
(n+1)(n+2)(g_n-a_n)\\
(n+2)(g_{n+1}-a_{n+1})\\
g_{n+2}-a_{n+2}
\end{pmatrix}.
$$


Then (3.2) gives the integral identity


$$
\boxed{\mathbf U=E_n\mathbf H+\mathbf B.}
\tag{4.2}
$$



The complete logarithmic contribution, in the same normalization, is


$$
\boxed{
\mathbf Q=
4n!(n+2)!\,(\rho_nv+\rho_{n+1}w).
}
\tag{4.3}
$$


It is integral. Indeed,


$$
\mathbf Q
=
2n!(n+1)!\,(\rho_nv'+\rho_{n+1}w'),
$$


and the factorial reference-denominator bounds suffice.

Finally put


$$
\boxed{\mathbf C=\mathbf B+\mathbf Q.}
\tag{4.4}
$$



Thus


$$
\boxed{
(n+2)!\,(\widehat w-T_0)=E_n\mathbf H+\mathbf C.
}
\tag{4.5}
$$



Here:

- $\widehat w$ is the complete exponential-plus-logarithmic force;
- the subtraction of $T_0$ is retained;
- at endpoint $0$, that subtraction is exactly what restores the exterior $+1$;
- no terminal term has been discarded.

---

## 5. New endpoint projection equation and exact large-prime laws

Let $r_j\in\mathbb Z^3$ be the actual primitive integral row proportional to


$$
\ell_j\operatorname{adj}(T).
$$


Define


$$
R_j=r_j\mathbf H,\qquad C_j=r_j\mathbf C.
$$


Both are integers.

The exact reconstructed endpoint ratio is


$$
\boxed{
\frac{v_j^{\rm rec}}{u_j^{\rm rec}}
=
\frac{E_nR_j+C_j}{n!R_j}.
}
\tag{5.1}
$$


This follows directly from


$$
u_j^{\rm rec}
=\frac{n!\,\ell_j\operatorname{adj}(T)t}{\det T},
$$


and the exterior-corrected complete numerator.

Consequently the actual denominator has the all-prime expression


$$
\boxed{
d_j=
\frac{|n!R_j|}
{\gcd(|n!R_j|,\ |E_nR_j+C_j|)}.
}
\tag{5.2}
$$


No primitive-row content, reference clearer, or prime has been omitted.

### 5.1 The seed disappears from large-prime cancellation

At $p>n+2$, $n!$ is a unit, so


$$
\gcd(R_j,E_nR_j+C_j)=\gcd(R_j,C_j)
$$


in $\mathbb Z_p$. Therefore


$$
\boxed{
v_p(d_j)=\bigl(v_p(R_j)-v_p(C_j)\bigr)_+.
}
\tag{5.3}
$$



This is an exact terminal projection equation for the actual construction. The seed $E_n$ has disappeared because it multiplies the same reference projection that occurs in the denominator.

### 5.2 Exact separation of structural and force cancellation

Retain


$$
G_j=\gcd(r_jv',r_jw'),
$$




$$
(\mathfrak a_j,\mathfrak b_j)
=\left(\frac{r_jv'}{G_j},\frac{r_jw'}{G_j}\right),
$$




$$
\xi_j=\mathfrak a_j\tau_n+\mathfrak b_j\tau_{n+1}.
$$


Then


$$
R_j=\frac{(n+1)!}{2}G_j\xi_j.
\tag{5.4}
$$



Let $p>n+2$, and write


$$
g=v_p(G_j),\qquad x=v_p(\xi_j),\qquad c=v_p(C_j).
$$


All three are nonnegative, allowing $c=+\infty$.

The complete logarithmic term and the seed term satisfy


$$
C_j-r_j\mathbf U\in G_j\mathbb Z_p.
\tag{5.5}
$$


Indeed,


$$
C_j-r_j\mathbf U=-E_nR_j+r_j\mathbf Q,
$$


and both terms are divisible by $G_j$ over $\mathbb Z_p$.

Using the actual primitive-triple formula gives


$$
\boxed{v_p(\gamma_j)=(g-c)_+.}
\tag{5.6}
$$



For cancellation, when $c<g$, $\gamma_j$ contains $p$ and the primitive exponential coordinate is a unit, so $\mathcal C_j^\sharp$ has no $p$-factor.

When $c\ge g$, the primitive numerator differs from a unit multiple of $C_j/p^g$ by a multiple of $\xi_j$. Therefore


$$
\boxed{
v_p(\mathcal C_j^\sharp)
=\min\{x,c-g\}.
}
$$


Combining the two cases,


$$
\boxed{
v_p(\mathcal C_j^\sharp)
=\min\{x,(c-g)_+\}.
}
\tag{5.7}
$$



Finally,


$$
\boxed{
v_p(d_j)=(g+x-c)_+.
}
\tag{5.8}
$$



These formulas preserve the $G_j$-depth. Replacing $C_j$ by an unnormalized force projection and forgetting the threshold $g$ would give the wrong cancellation law.

### 5.3 Relation to the complete two-kernel determinants

With the original complete


$$
s=\frac{\widehat w-T_0}{n!},
$$


equation (4.5) gives


$$
s=\frac{E_n}{n!}t+
\frac{\mathbf C}{n!(n+2)!}.
$$


Hence the actual terminal minors satisfy


$$
\boxed{
\mu_i
=
\frac{2(n+2)}{(n+2)!}
\det(t,\mathbf C,T_i).
}
\tag{5.9}
$$



Thus the seed cancellation also occurs before applying either endpoint kernel. This is not merely a cancellation in one specially chosen endpoint ratio.

### 5.4 What this proves—and what it does not

The new identity isolates the outstanding endpoint-specific factor:


$$
\min\{v_p(\xi_j),(v_p(C_j)-v_p(G_j))_+\}.
$$



It also proves a precise obstruction to a proposed seed-unit argument:

> The large-prime projected contents cannot be excluded merely by proving congruences or unit properties of $E_n$, because the entire $E_n$-dependent terminal column is in the reference direction and vanishes from the relevant projected quotient.

This statement is derived from the actual seed and actual forcing. It does not invoke arbitrary input triples.

The identity does **not** yet bound the residual column $\mathbf C$ uniformly on the original families. That is the remaining large-prime problem.

---

## 6. New theorem at all primes $p\ge5$ dividing $n-1$

This extends the earlier selected $7$-calculation to an entire unhandled prime regime, including the case where the reference projection is not a unit.

Let


$$
p\ge5,\qquad p^s\mid n-1,\qquad t=v_p(n!).
$$



### 6.1 Actual moment, force, and primitive-row reductions

Using congruence in $n$ and odd-prime index periodicity,


$$
(a_{n-2},a_{n-1},a_n,a_{n+1},a_{n+2})
\equiv(3,1,0,0,1)\pmod{p^s},
$$


and


$$
(u_n,u_{n+1},u_{n+2})
\equiv(3,8,32)\pmod{p^s}.
$$



Because $n+1$ and $n+2$ are units,


$$
n!T\equiv
\begin{pmatrix}
0&1&0\\
0&0&1\\
1/6&0&0
\end{pmatrix}\pmod{p^s}.
$$


Its determinant is a unit. Thus the actual primitive endpoint rows are, up to local unit multiples,


$$
\boxed{
r_0\equiv(1,-2,-6),\qquad
r_3\equiv(0,1,0)\pmod{p^s}.
}
\tag{6.1}
$$



Also,


$$
v'\equiv(6,3,2),\qquad
w'\equiv(0,3,5),
$$


and


$$
\mathbf U\equiv(18,24,31).
$$


Therefore


$$
(r_0v',r_0w')\equiv(-12,-36),
\qquad
(r_3v',r_3w')\equiv(3,3),
$$


and


$$
\boxed{
r_0\mathbf U\equiv-216,\qquad
r_3\mathbf U\equiv24\pmod{p^s}.
}
\tag{6.2}
$$



For every $p\ge5$, these force projections are units, as are $G_0,G_3$.

### 6.2 Exact force-cancellation exclusion

Since


$$
v_p(K_n)=2t,
$$


the actual primitive-triple law gives


$$
\boxed{
v_p(\gamma_0)=v_p(\gamma_3)=2t.
}
\tag{6.3}
$$



Here $p\le n-1$, so $t\ge1$. The primitive exponential coordinates are units, while


$$
v_p(\gamma_j\eta_j)\ge2t-t=t>0.
$$


Consequently


$$
\boxed{v_p(\zeta_j)=0,\qquad j=0,3.}
\tag{6.4}
$$



It follows that


$$
\boxed{
v_p(d_j)=2t+v_p(\xi_j).
}
\tag{6.5}
$$



This excludes **all endpoint-specific complete-force cancellation** at these primes. It does not require $\xi_j$ to be a unit.

With the actual $L$, it also gives


$$
\boxed{
v_p\bigl(\gcd(\gamma_jX_j,V_j)\bigr)=v_p(L).
}
\tag{6.6}
$$


Thus any cancellation at these primes is exactly the already present reference-clearer factor—not an additional force intersection.

### 6.3 The remaining reference projection

Write $n=1+pb$. Lucas reduction gives


$$
\tau_n\equiv\tau_b,\qquad
\tau_{n+1}\equiv2\tau_b\pmod p.
$$


Hence, up to local units,


$$
\xi_0\equiv-84\tau_b,\qquad
\xi_3\equiv9\tau_b\pmod p.
$$



If $p\ne7$ and $\tau_b$ is a unit, both projections are units and


$$
\boxed{v_p(d_0)=v_p(d_3)=2t.}
\tag{6.7}
$$



At $p=7$, the endpoint-$0$ factor $84$ explains the opposite orientation already found on $15^r$.

If $\tau_b$ is not a unit, the reference depths remain to be evaluated, but (6.4) still excludes complete-force cancellation. This distinction is important: no generic all-prime reference-unit assumption has been introduced.

---

## 7. New endpoint-$0$ reduction at odd primes dividing $n+1$

Let


$$
p\text{ odd},\qquad s=v_p(n+1),\qquad t=v_p(n!).
$$


Put


$$
m=n+1,\qquad N=n+2,\qquad J=(n+2)!T.
$$



For compactness write


$$
A=a_n,\quad B=a_{n-1},\quad C=a_{n-2},
\quad D=a_{n+1},\quad E=a_{n+2}.
$$


Then


$$
J=
\begin{pmatrix}
mNA&nmNB&n(n-1)mNC\\
ND&mNA&nmNB\\
E&ND&mNA
\end{pmatrix}.
\tag{7.1}
$$



Odd-prime index periodicity gives


$$
D\equiv1,\qquad E\equiv2\pmod{p^s}.
$$



### 7.1 The missing primitive reduction

Let


$$
\mathscr R_0=\ell_0\operatorname{adj}(J),
\qquad
\ell_0=(-1,n,-n(n+1)).
$$


Every entry of $\mathscr R_0$ is divisible by $m$. Direct expansion gives, modulo $p^s$,


$$
\frac{\mathscr R_0}{m}
\equiv(A+B+1,\,2C,\,-2C).
$$


The moment recurrence at $k=n$, reduced modulo $p^s$, gives


$$
A+B+C\equiv1.
$$


Therefore


$$
\boxed{
\frac{\mathscr R_0}{n+1}
\equiv(2-C,\,2C,\,-2C)\pmod{p^s}.
}
\tag{7.2}
$$



This vector is primitive modulo $p$: if $C\equiv0$, its first entry is $2$; otherwise one of the last two entries is a unit.

Thus the raw endpoint-$0$ row has **exactly** $s$ factors of $p$ in its content. After the actual primitive reduction,


$$
\boxed{
r_0\equiv(2-C,2C,-2C),\qquad
r_3\equiv(1,0,0)\pmod{p^s},
}
\tag{7.3}
$$


up to local units.

Since


$$
v'\equiv(2,1,0),\qquad w'\equiv(0,1,1),
$$


we obtain


$$
r_0v'\equiv4,\quad r_0w'\equiv0,
\qquad
r_3v'\equiv2,\quad r_3w'\equiv0.
$$


Hence


$$
\boxed{v_p(G_0)=v_p(G_3)=0.}
\tag{7.4}
$$



### 7.2 Complete exponential projections

Index periodicity and the actual initial force values give


$$
u_{n+1}\equiv E_n,\qquad
u_{n+2}\equiv E_n+1\pmod{p^s}.
$$


Therefore


$$
\mathbf U\equiv(0,E_n-1,E_n-1)^T\pmod{p^s}.
$$


Both rows in (7.3) annihilate this vector:


$$
\boxed{
v_p(r_0\mathbf U),\,v_p(r_3\mathbf U)\ge s.
}
\tag{7.5}
$$



Since $v_p(K_n)=2t+s$,


$$
\boxed{
v_p(\gamma_0),\,v_p(\gamma_3)\le2t.
}
\tag{7.6}
$$



This closes the endpoint-$0$ normalization gap in Turn 4 for this prime regime.

### 7.3 Actual denominator bound

At odd primes, $\xi_j$ is $p$-integral. Also


$$
v_p(\eta_j)\ge-(t+s).
$$


Writing $g_j=v_p(\gamma_j)$, the exact denominator law gives


$$
v_p(d_j)\le v_p(\xi_j)+\max\{g_j,t+s\}.
$$



For odd $n$, $t\ge s$. Indeed, $p^s\mid n+1$ and $n+1$ is even, so


$$
n\ge2p^s-1,
$$


which already implies $\lfloor n/p\rfloor\ge s$.

Thus


$$
\boxed{
v_p(d_j)\le2t+v_p(\xi_j),
\qquad j=0,3.
}
\tag{7.7}
$$



If $\tau_n$ is a unit, (7.3)–(7.4) show that both $\xi_j$ are units, and the bound becomes $v_p(d_j)\le2t$. No such unit assumption is needed for (7.7).

---

## 8. New $2$-adic endpoint-$3$ cost bounds

Retain the notation in (7.1). The raw endpoint-$3$ adjugate row is


$$
\mathscr R_3=
\left(
N^2D^2-mNAE,\;
nmNBE-mN^2AD,\;
m^2N^2A^2-nmN^2BD
\right).
\tag{8.1}
$$



### 8.1 The case $n\equiv3\pmod4$

The moment parity pattern gives


$$
A,D\ \text{odd},\qquad B,E\ \text{even}.
$$


The first coordinate of $\mathscr R_3$ is odd, so the row is already primitive at $2$.

Put $s=v_2(n+1)\ge2$. Its second and third coordinates are divisible by $2^s$. Hence


$$
v_2(r_3v')=1,
\qquad
v_2(G_3)=1.
$$


Because the first coordinate of $\mathbf U$ is divisible by $n+1$, and the other two row coefficients are also divisible by $n+1$,


$$
v_2(r_3\mathbf U)\ge s.
$$


The exact gamma law gives


$$
\boxed{v_2(\gamma_3)\le2v_2(n!).}
\tag{8.2}
$$



### 8.2 The case $n\equiv1\pmod4$

Now


$$
A,D\ \text{even},\qquad B,E\ \text{odd},
\qquad v_2(m)=1.
$$


In (8.1), the middle coordinate has valuation exactly $1$, while the other two have valuation at least $2$. Therefore the raw row content has exactly one factor of $2$, and the actual primitive row satisfies


$$
r_3\equiv(0,1,0)\pmod2.
$$


Thus $G_3$ is odd.

The complete exponential parity vector is


$$
\mathbf U\equiv(0,0,1)^T\pmod2,
$$


so $r_3\mathbf U$ is even. Since


$$
v_2(K_n)=2v_2(n!),
$$


we obtain


$$
\boxed{v_2(\gamma_3)\le2v_2(n!)-1.}
\tag{8.3}
$$



These are actual primitive-row bounds. They are not denominator bounds at $2$: the $2$-adic reference valuations and the complete $\zeta_j$-cancellation must still be retained in the all-prime formula.

---

## 9. Consequences for the existing $n=3375$ artifact

No force or reconstructed column needs to be regenerated.

### 9.1 Sharpened $3/5/7$ predictions from the completed finite imbalance

The previously proved endpoint-$3$ laws give


$$
v_3(d_3)=3368,\qquad v_5(d_3)=1686,\qquad v_7(d_3)=1120.
$$


The completed imbalance has exponents $3,4,1$ at $3,5,7$, with the proved orientations. Therefore:

| Prime | $v_p(\gamma_0)$ | $v_p(d_0)$ | $v_p(\gamma_3)$ | $v_p(d_3)$ |
|---|---:|---:|---:|---:|
| $3$ | $3365$ | $3365$ | $3368$ | $3368$ |
| $5$ | $1682$ | $1682$ | $1686$ | $1686$ |
| $7$ | $1120$ | $1121$ | $1120$ | $1120$ |

The endpoint-$0$ gamma equalities at $3,5$ follow because the resulting denominator exponents exceed $v_p(n!)$; in that range the earlier exact law forces the primitive exponential coordinate to prevent further cancellation.

The expected projection outputs are now


$$
\boxed{
v_3(r_0\mathbf U)=3,\qquad
v_5(r_0\mathbf U)=4,\qquad
\eta_7(3375)=1.
}
\tag{9.1}
$$



For the actual


$$
L=2^{n+1}\operatorname{lcm}(1,\ldots,n+1),
$$




$$
v_3(L)=7,\qquad v_5(L)=5,\qquad v_7(L)=4.
$$


Hence the corresponding dual-content predictions are


$$
\boxed{
\begin{array}{c|cc}
p&v_p(\mathcal C_0^\sharp)&v_p(\mathcal C_3^\sharp)\\ \hline
3&7&7\\
5&5&5\\
7&5&4
\end{array}}
\tag{9.2}
$$


while the actual endpoint denominator cancellation at $7$ has valuation $4$ at both endpoints.

These are sharpened deductions for the coordinator’s already planned postprocessing, not a request to repeat it.

### 9.2 A new unhandled-prime prediction: $p=241$

Since


$$
3375-1=2\cdot7\cdot241,
\qquad
v_{241}(3375!)=14,
$$


Theorem 6 gives


$$
v_{241}(\gamma_0)=v_{241}(\gamma_3)=28,
\qquad v_{241}(\zeta_j)=0.
$$



The small exact reference value


$$
\tau_{14}=\frac{251701}{8}\equiv223\pmod{241}
$$


is a unit. Because


$$
3375=1+241\cdot14,
$$


the reference-unit criterion in §6.3 applies. Therefore


$$
\boxed{
v_{241}(d_0)=v_{241}(d_3)=28.
}
\tag{9.3}
$$


For the actual $L$, $v_{241}(L)=1$, so


$$
\boxed{
v_{241}(X_j)=v_{241}(V_j)
=v_{241}(\mathcal C_j^\sharp)=1.
}
\tag{9.4}
$$



This is a new exact local prediction on an unhandled prime, derived without computing the force.

### 9.3 The $n+1$ prime $211$

Here


$$
3376=16\cdot211,
\qquad v_{211}(3375!)=15.
$$



For completeness, the reference unit can be proved by a small exact calculation. The generating function


$$
\sum_{m\ge0}\tau_mz^m=(1-2z-z^2)^{-1/2}
$$


implies


$$
\tau_{p-1}\equiv(-1)^{(p-1)/2}\pmod p.
$$


Also


$$
\tau_{15}=73439\equiv11\pmod{211}.
$$


Since


$$
3375=210+211\cdot15,
$$


Lucas reduction yields


$$
\tau_{3375}\equiv-11\pmod{211}.
$$


Both endpoint reference projections are therefore units in the reduction of §7.

Consequently,


$$
\boxed{
v_{211}(\gamma_0),v_{211}(\gamma_3),
v_{211}(d_0),v_{211}(d_3)\le30.
}
\tag{9.5}
$$



The completed absence of $211$ from $|AB|$ additionally says that the two denominator exponents are equal. The new theorem bounds that common exponent; it does not assign it an uncomputed value.

### 9.4 The new binary bound

For $3375$,


$$
v_2(n!)=3375-s_2(3375)=3367,
\qquad v_2(n+1)=4.
$$


Thus


$$
\boxed{
v_2(G_3)=1,\qquad
v_2(r_3\mathbf U)\ge4,\qquad
v_2(\gamma_3)\le6734.
}
\tag{9.6}
$$



These additional checks are optional postprocessing of existing exact entries. No new original-index producer is required for any theorem in this report.

---

## 10. The exact remaining projected-content lemma

The common structural factor is already sharply controlled:


$$
(W_n)_{>n+2}=1
\quad\text{or one prime to exponent }1.
$$


It should not be substituted for the endpoint-specific cancellation problem.

The new seed-elimination identity makes that remaining problem more concrete. For $p>n+2$, define


$$
g_{j,p}=v_p(G_j),\qquad
x_{j,p}=v_p(\xi_j),\qquad
c_{j,p}=v_p(C_j).
$$


Then the exact endpoint-specific cancellation contribution is


$$
\boxed{
\kappa_{j,p}
=
\min\{x_{j,p},(c_{j,p}-g_{j,p})_+\}.
}
\tag{10.1}
$$



### Follow-on lemma: seed-free terminal residual intersection

A sufficient next result would bound, on an infinite subsequence of one original family,


$$
\boxed{
\sum_{p>n+2}
\left(
\kappa_{0,p}+\kappa_{3,p}
\right)\log p,
}
\tag{10.2}
$$


together with the endpoint-specific structural depths


$$
(g_{j,p}-c_{j,p})_+,
$$


or directly bound the resulting all-prime denominator imbalance.

The important change is that $\mathbf C$ is now specified independently of $E_n$:


$$
\mathbf C
=
\left(
\frac{(n+2)!}{(n+i)!}(g_{n+i}-a_{n+i})
\right)_{i=0}^2
+
4n!(n+2)!(\rho_nv+\rho_{n+1}w).
$$


Every term is explicit, integral, and belongs to the original complete construction.

A useful invariant must therefore control this **zero-seeded forced residual**, jointly with the actual reference projection and after the $G_j$-threshold. Another invariant proving only that the full fifteen-state connection is primitive would not address (10.2).

The new small-prime theorems remove several local regimes from this residual problem:

- at $p\ge5\mid n-1$, complete-force cancellation is absent;
- at odd $p\mid n+1$, both primitive gamma costs are bounded by $2v_p(n!)$;
- at $2$, the stated endpoint-$3$ normalization costs are explicit.

The other small-prime regimes, including actual reference content and $\zeta_j$-cancellation where not covered above, remain part of the all-prime obligation.

---

## 11. Actual primitive denominator and whole same-index error

The endpoint denominator remains


$$
\boxed{
d_j=\frac{|\gamma_jX_j|}
{\gcd(|\gamma_jX_j|,|V_j|)}.
}
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
$$




$$
H_{\rm gcd}
=
\gcd\!\left(h,\frac{|T_{\rm wt}|}{F_{\rm gcd}G}\right).
$$


The actual primitive pair is still


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


Every prime remains in the final gcd.

The complete same-index error is


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
\tag{11.2}
$$



For nonzero factors, its exact logarithmic decomposition is


$$
\begin{aligned}
\log|q_\lambda(e+\pi)-p_\lambda|
={}&\log(kh|AB|)
-\log(F_{\rm gcd}GH_{\rm gcd})\\
&+\log|e_3\alpha_{n,2}|
+\log|\lambda-\Lambda_{n,2}|.
\end{aligned}
\tag{11.3}
$$



The accepted error asymptotics may be inserted only at their stated original-index and weight scope. They do not supply the missing arithmetic estimates for the first line of (11.3).

Accordingly:

- the completed large forms at $3375$ do not prove an infinite exclusion;
- the selected-part law $5n$ does not by itself settle the full denominator comparison;
- the new local theorems do not yet prove that (11.3) tends to $+\infty$, stays bounded below, or tends to $-\infty$ on the required infinite sequence.

An irrationality proof still requires


$$
0<
q_\lambda|e_3\alpha_{n,2}|
\,|\lambda-\Lambda_{n,2}|
\longrightarrow0
$$


along infinitely many original indices. No such sequence is established here.

---

## 12. Proof status and bounded arithmetic

| Statement | Status |
|---|---|
| Completed $225$, $3375$, and direct $17$ results | Retained at their finite scopes; no rerun |
| $3375$ whole-form signs and magnitudes | Accepted rigorous finite enclosures |
| Integral polynomial coefficients $b_r(n)$ | Proof audited |
| Negative-index handling in odd-prime force periodicity | Proof clarified; no negative $E_m$ required |
| Force index period $2^{s+1}$ modulo $2^s$ | **New proof** |
| $u_k=E_nh_k+g_k$, with $h_k,g_k\in\mathbb Z[n]$ | **New exact coefficient relation** |
| Complete integral endpoint equation (5.1) | **New proof** |
| Large-prime laws (5.6)–(5.8) | **New exact primewise identities** |
| Seed cancellation in all complete terminal minors | **New proof** |
| No extra force cancellation at $p\ge5\mid n-1$ | **New theorem** |
| Both endpoint gamma bounds at odd $p\mid n+1$ | **New theorem** |
| Endpoint-$0$ primitive-row reduction at $p\mid n+1$ | **New explicit derivation** |
| Endpoint-$3$ binary gamma bounds | **New theorem** |
| $3375$ predictions at $241,211,2$ | Theorem-derived; artifact postprocessing not represented as executed |
| Uniform large-prime residual-intersection bound | Open |
| Remaining all-small-prime denominator control | Open |
| Infinite denominator/whole-error comparison | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

### Bounded exact arithmetic still relevant

No new computation is needed to prove the results above.

The coordinator’s already planned $3/5/7$ postprocessing should return the sharpened values in (9.1)–(9.2), using only the existing artifact.

If the new local predictions are appended to that same postprocessing, the inputs are:

- archived actual primitive endpoint triples and denominators;
- primitive contact rows, obtained from the archived $3\times3$ matrix;
- archived $\mathbf U$, or its entries reconstructed from the already stored moment and force coefficients;
- the actual $L,X_j,V_j,\mathcal C_j^\sharp$.

The expected verifiable outputs are:

1. At $241$:
   

$$
v_{241}(\gamma_0)=v_{241}(\gamma_3)
   =v_{241}(d_0)=v_{241}(d_3)=28,
$$


   and the valuations in (9.4).

2. At $211$:
   

$$
v_{211}(\gamma_j)\le30,\qquad
   v_{211}(d_j)\le30,
$$


   with equal actual denominator exponents.

3. At $2$:
   

$$
v_2(G_3)=1,\qquad
   v_2(r_3\mathbf U)\ge4,\qquad
   v_2(\gamma_3)\le6734.
$$



These are bounded valuation extractions from an existing artifact, not force recomputation, and no execution of them is claimed here.

---

## Conclusion

The fixed factorial seed admits a stronger exact analysis than the fifteen-state determinant supplies:


$$
\boxed{
\Omega_n=\mathscr H_n(E_n+I_n),
\qquad
u_k=E_nh_k+g_k.
}
$$


At the original terminal rows, $\mathscr H_n$ is exactly the reference column. Hence the seed term cancels from the complete projected arithmetic, yielding the exact large-prime laws


$$
\boxed{
v_p(\gamma_j)=(g-c)_+,\quad
v_p(\mathcal C_j^\sharp)=\min\{x,(c-g)_+\},\quad
v_p(d_j)=(g+x-c)_+.
}
$$



This identifies the correct remaining object: not $E_n$ alone, not full-state primitivity, and not the already small common $W$, but the endpoint-specific **seed-free complete terminal residual** jointly with the actual reference projection.

The new local results additionally exclude complete-force cancellation at every $p\ge5\mid n-1$, resolve the missing primitive endpoint-$0$ reduction at odd $p\mid n+1$, and bound the endpoint-$3$ binary normalization cost.

The exact remaining bottleneck is a sufficiently strong infinite-family bound for the residual intersection depths in (10.1), together with the uncovered small-prime costs, followed by comparison of the actual all-prime primitive denominator with the whole same-index error.



$$
\boxed{\text{No unconditional proof or disproof of the irrationality of }e+\pi\text{ has been obtained.}}
$$


