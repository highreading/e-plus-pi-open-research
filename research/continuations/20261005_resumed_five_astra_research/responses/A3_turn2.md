> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 2 — Actual endpoint arithmetic: factorial prime powers survive the full gcd

## 1. Main result and its scope

Let


$$
S=e+\pi,\qquad M=1+\sqrt2,\qquad d=b-1,
$$


and retain the complete rational columns produced by `full_lift(n,b)`, including the exterior $+1$ in coordinate zero. The center remains exactly


$$
\widehat c
=\frac{n^2}{d}\frac{v_0}{u_0}
+\left(1-\frac{n^2}{d}\right)\frac{v_b}{u_b}.
\tag{1.1}
$$


No coefficient, index, metric realization, or endpoint has been changed.

The principal advance is an arbitrary-order arithmetic theorem for these actual columns.

> **Prime-survival theorem.**  
> Let $p$ be an odd prime, let
> 

$$
> 2\le d<p,\qquad p\mid n,
>
$$


> and put
> 

$$
> \tau_n=\sum_{r=0}^{\lfloor n/2\rfloor}
> \frac{n!}{r!^2(n-2r)!2^r},
> \qquad
> D_d=d!\sum_{r=0}^{d}\frac{(-1)^r}{r!}.
> \tag{1.2}
>
$$


> Assume
> 

$$
> \tau_nD_d\not\equiv0\pmod p.
> \tag{1.3}
>
$$


> Then the original finite contact matrix is invertible, both endpoint first-column entries are nonzero, and the actual reduced denominator of (1.1) satisfies
> 

$$
> \boxed{v_p(\widehat q)=2v_p(n!).}
> \tag{1.4}
>
$$


> More specifically, in the endpoint normalization of A3, Turn 1,
> 

$$
> \boxed{
> v_p(A)=v_p(F)=v_p(G)=v_p(H_{\rm gcd})=v_p(J)=v_p(T)=0,
> }
> \tag{1.5}
>
$$


> and
> 

$$
> \boxed{v_p(h)+v_p(B)=2v_p(n!).}
> \tag{1.6}
>
$$


> Thus the $p$-part of the shared endpoint denominator $h$ does **not** cancel through the final shared-content gcd.

This is proved below directly from the complete producer. It is not extrapolated from the sixteen computations.

There are three useful consequences.

1. **An actual infinite obstruction to the proposed denominator budget.** For $d=2$ and every positive multiple $n$ of $105$,
   

$$
v_p(\widehat q)=2v_p(n!)\qquad(p=3,5,7).
   \tag{1.7}
$$


   Consequently,
   

$$
\boxed{
   \frac{\widehat q\,M^{-2n-3}}{n}
   >
   \frac{2^n}{11025\,M^3n^7}
   \longrightarrow\infty.
   }
   \tag{1.8}
$$


   The shared-content cancellation sought in Turn 1 cannot make its sufficient upper-bound budget tend to zero on this progression.

   There is an analogous obstruction for $d=3,4$ on $385\mid n$, using $p=5,7,11$.

2. **Rigorous eventual nonvanishing on genuine asymptotic subfamilies.** For each
   

$$
d\in\{2,3,4,8\},
$$


   the centers with $n=11m$, $m=1,2,\ldots$, are pairwise distinct. Hence, for each fixed such $d$,
   

$$
\boxed{\widehat c_{11m,d}-S=0\text{ for at most one }m.}
   \tag{1.9}
$$


   In particular, their whole errors are eventually nonzero. This conclusion does not require knowing whether $S$ is rational.

3. **A limitation that must remain explicit.** Equation (1.8) is a lower bound for the denominator times the *proved upper-bound scale* of the error. It is **not** by itself a lower bound for the actual whole primitive form. A quantitative lower bound for the signed endpoint defect is still needed to prove that
   

$$
|\widehat qS-\widehat p|\to\infty
$$


   on these progressions.

Thus the report advances both actual endpoint gcd arithmetic and nonvanishing, but does not prove an exclusion theorem for the actual primitive forms, and does not settle irrationality of $e+\pi$.

### Source discipline

I retain the accepted quantitative CSC and signed endpoint law at their stated scopes. I do not use A3, Turn 0’s unreviewed common-error expansion.

The completed raw-diagonal exclusion remains valid for its original primitively normalized family. Its denominator and prime transfers are not transferred to the present center. The new prime theorem below is proved for the present complete lift.

No tools, external endpoints, or files have been accessed or executed.

---

## 2. A universal exact endpoint formula from the complete producer

This section gives an auditable finite formula before making any congruence reduction.

The original dimensions remain


$$
\mathsf T:\{0,\ldots,d\}^2,\qquad
\mathcal S:\{0,\ldots,d\}^2,\qquad
Z:\{0,\ldots,b\}\times\{0,\ldots,d\}.
\tag{2.1}
$$


Here $\mathsf T$ denotes the producer’s contact matrix; it is distinguished from the scalar numerator $T$ in the endpoint gcd formula.

### 2.1 Complete scalar coefficients

Put


$$
Q(z)=1-z+\frac{z^2}{2},\qquad
q_j=[z^j]Q(z)^n,
\tag{2.2}
$$


with $q_j=0$ outside $0\le j\le2n$.

Define


$$
\alpha_0=\alpha_1=1,\qquad
\alpha_j=\alpha_{j-1}-\frac12\alpha_{j-2}\quad(j\ge2),
\tag{2.3}
$$


and


$$
\eta_\ell
=\sum_{s=0}^{\ell}\frac1{s!}
+\sum_{s=1}^{\ell}\frac{2\alpha_{s-1}}s.
\tag{2.4}
$$


These are exactly the producer’s `ainv` and `hq` coefficients. In particular, (2.4) contains both the complete finite exponential sum and the complete logarithmic/arctangent contribution.

Set


$$
\mathcal W_\ell=\ell!\eta_\ell.
\tag{2.5}
$$


Then


$$
\boxed{
\mathcal W_0=1,\qquad
\mathcal W_\ell
=\ell\mathcal W_{\ell-1}
+1+2(\ell-1)!\alpha_{\ell-1}\quad(\ell\ge1).
}
\tag{2.6}
$$


Every $\mathcal W_\ell$ belongs to $\mathbb Z[1/2]$. This recurrence is a convenient way to retain the full force without repeatedly forming large rational partial sums.

Also put


$$
\mathcal B_k
=k![z^k]\bigl(e^zQ(z)^n\bigr)
=\sum_{j=0}^{\min(k,2n)}q_j\,k^{\underline j},
\tag{2.7}
$$


where $x^{\underline j}=x(x-1)\cdots(x-j+1)$.

These coefficients can be generated by


$$
\boxed{
\mathcal B_{k+1}
=(k+1-n)\mathcal B_k
+\frac{k(2n-k-1)}2\mathcal B_{k-1}
+\frac{k(k-1)}2\mathcal B_{k-2},
}
\tag{2.8}
$$


with $\mathcal B_0=1$ and negative-index terms zero. Equation (2.8) follows by differentiating $e^zQ(z)^n$ and multiplying by $Q(z)$.

### 2.2 A row-scaled contact system over $\mathbb Z[1/2]$

For $0\le i,j\le d$, define


$$
C_{ij}
=(n+i)^{\underline j}\mathcal B_{n+i-j}.
\tag{2.9}
$$


When $n\ge d$, this is exactly


$$
C=\operatorname{diag}\bigl((n+i)!\bigr)_{i=0}^{d}\,\mathsf T.
\tag{2.10}
$$



Define the two row-scaled forces


$$
z_i=(n+i)!\,n!\,t_i,
\qquad
t_i=[z^{n+i}]\frac{Q(z)^n}{(1-z)^{n+1}},
\tag{2.11}
$$


and


$$
\boxed{
w_i
=\sum_{j=0}^{\min(2n,n+i)}
q_j\,(n+i)^{\underline j}\,
\mathcal W_{2n+i-j}.
}
\tag{2.12}
$$


The second formula is the complete producer force after row scaling:


$$
(n+i)!\!
\sum_j q_j
\frac{(2n+i-j)!}{(n+i-j)!}\eta_{2n+i-j}
=w_i.
$$


The upper index is exactly $2n+d$; no coefficient beyond the producer’s finite jet is required.

Let


$$
x=C^{-1}z,\qquad y=C^{-1}w.
\tag{2.13}
$$


These are precisely the two internal columns before reconstruction.

### 2.3 Exact endpoint reconstruction, including $+1$

The reconstruction matrix satisfies


$$
\mathcal S_{jk}
=(-1)^{k-j}
\binom{n+k-j-1}{k-j}\frac{k!}{j!},
\qquad 0\le j\le k\le d.
\tag{2.14}
$$


In particular, if


$$
s_j=(-1)^j n^{\overline j},
\qquad n^{\overline0}=1,
\tag{2.15}
$$


then $\mathcal S_{0j}=s_j$ and $\mathcal S_{dd}=1$.

The actual endpoints are therefore


$$
\boxed{
u_0=-s^Tx,\qquad u_b=x_d,
}
\tag{2.16}
$$




$$
\boxed{
v_0=1-s^Ty,\qquad v_b=y_d.
}
\tag{2.17}
$$


The $1$ in (2.17) is the original exterior endpoint. It will have a visible arithmetic effect below.

These formulas retain every coordinate used by the original inverse. They are not an endpoint-only replacement for the contact system.

### 2.4 Determinant formula for primitive endpoint rows

Let


$$
\Delta=\det C,
$$


and define the dyadic rational determinants


$$
X_0=-s^T\operatorname{adj}(C)z,\qquad
X_b=e_d^T\operatorname{adj}(C)z,
\tag{2.18}
$$




$$
Y_0=\Delta-s^T\operatorname{adj}(C)w,\qquad
Y_b=e_d^T\operatorname{adj}(C)w.
\tag{2.19}
$$


Then


$$
u_j=X_j/\Delta,\qquad v_j=Y_j/\Delta
\quad(j=0,b).
\tag{2.20}
$$



Choose a power of two $L$ clearing
$\Delta,X_0,X_b,Y_0,Y_b$, and set


$$
X_j^*=\operatorname{sgn}(\Delta)LX_j,\qquad
Y_j^*=\operatorname{sgn}(\Delta)LY_j.
\tag{2.21}
$$


The primitive endpoint rows are


$$
\boxed{
\widetilde u_j=\frac{X_j^*}{\gcd(|X_j^*|,|Y_j^*|)},\qquad
\widetilde v_j=\frac{Y_j^*}{\gcd(|X_j^*|,|Y_j^*|)}.
}
\tag{2.22}
$$


They agree with the rows obtained from the actual jointly primitive $U,V$:


$$
(\widetilde u_j,\widetilde v_j)
=(U_j/r_j,V_j/r_j).
$$


The common positive rational proportionality between the two integral row representations disappears under primitive reduction.

The temporary power $L$ is **not** the actual two-column clearer $d_B$, and is not used as a denominator estimate.

Now define, exactly as in Turn 1,


$$
h=\gcd(|\widetilde u_0|,|\widetilde u_b|),\qquad
\widetilde u_0=hA,\qquad
\widetilde u_b=hB,
\tag{2.23}
$$




$$
g=\gcd(n^2,d),\qquad a=n^2/g,\qquad k=d/g,
\tag{2.24}
$$




$$
J=B\widetilde v_0-A\widetilde v_b,\qquad
T=aJ+kA\widetilde v_b.
\tag{2.25}
$$


Then


$$
F=\gcd(|A|,a)\gcd(|B|,a-k),
$$




$$
G=\gcd(k,|J|),\qquad
H_{\rm gcd}=\gcd\!\left(h,\frac{|T|}{FG}\right),
\tag{2.26}
$$


and the full primitive denominator is


$$
\boxed{
\widehat q=\frac{k h|AB|}{FGH_{\rm gcd}}.
}
\tag{2.27}
$$


Equations (2.2)–(2.27) are a universal finite endpoint procedure for the complete lift whenever its contact matrix is invertible.

### 2.5 A finite-boundary recurrence

There is also an endpoint update that does not require recomputing an entire inverse.

At fixed $n$, write a leading-principal enlargement as


$$
C_d=
\begin{pmatrix}
C_{d-1}&c\\
r&\gamma
\end{pmatrix},
\qquad
\beta=C_{d-1}^{-1}c,\qquad
\delta=\gamma-r\beta.
$$


If the indicated pivots are nonzero, set


$$
\xi=\frac{z_d-rx^{(d-1)}}{\delta},\qquad
\upsilon=\frac{w_d-ry^{(d-1)}}{\delta}.
$$


Then


$$
u_b^{(d)}=\xi,\qquad v_b^{(d)}=\upsilon,
\tag{2.28}
$$


and, with


$$
\Lambda_d=s_{<d}^{T}\beta-s_d,
$$




$$
\boxed{
u_0^{(d)}=u_0^{(d-1)}+\Lambda_d\xi,\qquad
v_0^{(d)}=v_0^{(d-1)}+\Lambda_d\upsilon.
}
\tag{2.29}
$$


The exterior $+1$ remains in the initial value and is not reintroduced or discarded during this update. If an intermediate pivot vanishes, the determinant formulas remain the appropriate universal formulation.

---

## 3. Proof of the prime-survival theorem

All congruences in this section are in $\mathbb Z_{(p)}$, so powers of two are units.

Assume


$$
p>d\ge2,\qquad p\mid n.
\tag{3.1}
$$



### 3.1 The contact matrix is a unit matrix after row scaling

In characteristic $p$,


$$
Q(z)^n=\bigl(Q(z)^{n/p}\bigr)^p.
$$


Consequently,


$$
q_j\equiv0\pmod p\qquad(1\le j<p).
\tag{3.2}
$$


For $j\ge p$, the integer $k^{\underline j}$ is divisible by $p$, whenever that term occurs.

Equation (2.7) thus gives


$$
\mathcal B_k\equiv1\pmod p\qquad(k\ge0).
\tag{3.3}
$$


It follows that


$$
C_{ij}\equiv i^{\underline j}\pmod p.
\tag{3.4}
$$


This is lower triangular for $0\le i,j\le d<p$, with diagonal entries $i!$. Therefore


$$
\boxed{
\det C\equiv\prod_{i=0}^{d}i!\not\equiv0\pmod p.
}
\tag{3.5}
$$


In particular, the actual rational contact matrix is invertible. Its inverse after row scaling is $p$-integral.

### 3.2 The first column has an exact squared-factorial scale

The series


$$
\frac{Q(z)^n}{(1-z)^n}
$$


belongs to $\mathbb F_p[[z^p]]$. Since $n$ is divisible by $p$ and $0\le i\le d<p$,


$$
t_i
=[z^{n+i}]\frac{Q(z)^n}{(1-z)^{n+1}}
\equiv
[z^n]\frac{Q(z)^n}{(1-z)^{n+1}}
=\tau_n
\pmod p.
\tag{3.6}
$$


The final equality follows by expanding


$$
Q(z)=(1-z)+z^2/2:
$$




$$
[z^n]\frac{Q(z)^n}{(1-z)^{n+1}}
=
\sum_{r=0}^{\lfloor n/2\rfloor}
\binom nr2^{-r}\binom{n-r}{r}.
$$



Divide the first row-scaled force by $(n!)^2$. Equation (2.11) gives


$$
\frac{z_i}{(n!)^2}
=(n+1)(n+2)\cdots(n+i)t_i
\equiv i!\tau_n\pmod p.
\tag{3.7}
$$


The unique solution of


$$
\sum_{j=0}^{i}i^{\underline j}X_j=i!
$$


is


$$
X_j=\frac{D_j}{j!}.
\tag{3.8}
$$


Indeed,


$$
\sum_{j=0}^{i}\binom ijD_j=i!,
$$


the standard derangement identity, follows directly by expanding the defining alternating sums.

Thus


$$
\boxed{
\frac{x_j}{(n!)^2}
\equiv \tau_n\frac{D_j}{j!}\pmod p.
}
\tag{3.9}
$$



Since $s_0=1$ and $s_j\equiv0\pmod p$ for $1\le j\le d$, the endpoint reconstruction gives


$$
\boxed{
\frac{u_0}{(n!)^2}\equiv-\tau_n,\qquad
\frac{u_b}{(n!)^2}\equiv\tau_n\frac{D_d}{d!}\pmod p.
}
\tag{3.10}
$$


Under (1.3), both are units. If $N_p=v_p(n!)$, then


$$
\boxed{v_p(u_0)=v_p(u_b)=2N_p.}
\tag{3.11}
$$



### 3.3 The complete companion has a unit at $b$

The complete force is important here.

For every $\ell$,


$$
\mathcal W_\ell
=\ell!\sum_{s=0}^{\ell}\frac1{s!}
+\sum_{s=1}^{\ell}\frac{2\ell!\alpha_{s-1}}s
\in\mathbb Z_{(p)}.
\tag{3.12}
$$


When $\ell\ge2p$,


$$
v_p(\ell!)>\lfloor\log_p\ell\rfloor.
$$


Therefore every term in the second sum in (3.12) vanishes modulo $p$. This is a congruence of the complete force, not a replacement of that force by an incomplete companion.

For $\ell=2n+i$, $0\le i<p$,


$$
\mathcal W_{2n+i}
\equiv
\sum_{t=0}^{2n+i}(2n+i)^{\underline t}
\equiv
\sum_{t=0}^{i}i^{\underline t}
\pmod p.
\tag{3.13}
$$


In (2.12), terms with $1\le j<p$ vanish by (3.2), and terms with $j\ge p$ vanish through the falling factorial. Hence


$$
w_i\equiv\sum_{t=0}^{i}i^{\underline t}\pmod p.
\tag{3.14}
$$


Together with (3.4), this says that


$$
\boxed{y_j\equiv1\pmod p\qquad(0\le j\le d).}
\tag{3.15}
$$



Now retain the exterior endpoint:


$$
v_0=1-s^Ty\equiv1-y_0\equiv0\pmod p,
$$


whereas


$$
v_b=y_d\equiv1\pmod p.
$$


Thus


$$
\boxed{v_p(v_0)\ge1,\qquad v_p(v_b)=0.}
\tag{3.16}
$$



All reconstructed coordinates in both columns are $p$-integral. Consequently the **least actual two-column clearer** satisfies


$$
\boxed{p\nmid d_B.}
\tag{3.17}
$$


This identifies the local normalization at the actual clearer, rather than at an arbitrarily enlarged one.

### 3.4 Exact row contents, $h,J,T$, and the final gcd

Let


$$
t_p=\min\{2N_p,v_p(v_0)\},
\tag{3.18}
$$


using $v_p(0)=+\infty$. Since $p\nmid d_B$, (3.11) and (3.16) imply


$$
v_p(r_0)=t_p,\qquad v_p(r_b)=0,
\tag{3.19}
$$


and


$$
v_p(\widetilde u_0)=2N_p-t_p,\qquad
v_p(\widetilde u_b)=2N_p.
$$


Therefore


$$
\boxed{
v_p(h)=2N_p-t_p,\qquad
v_p(A)=0,\qquad
v_p(B)=t_p\ge1.
}
\tag{3.20}
$$


Also $\widetilde v_b$ is a unit. It follows that


$$
J=B\widetilde v_0-A\widetilde v_b
\equiv-A\widetilde v_b\not\equiv0\pmod p.
\tag{3.21}
$$



Because $p>d$, the integers $g$ and $k$ are units at $p$, while $a$ is divisible by $p$. Hence $a-k$ is a unit and


$$
T=aJ+kA\widetilde v_b
\equiv kA\widetilde v_b\not\equiv0\pmod p.
\tag{3.22}
$$


Every possible cancellation factor in (2.27) is now accounted for:


$$
v_p(F)=0,\qquad v_p(G)=0,\qquad v_p(H_{\rm gcd})=0.
\tag{3.23}
$$


Substitution in the genuine primitive formula yields


$$
v_p(\widehat q)
=v_p(h)+v_p(B)=2N_p.
$$


This proves the theorem.

### 3.5 Why the raw endpoint minor does not supply extra cancellation

The same proof gives an especially useful normalization warning:


$$
\boxed{
v_p(U_bV_0-U_0V_b)=2N_p,
}
\tag{3.24}
$$


but


$$
\boxed{
v_p(r_0r_bh)=2N_p,\qquad v_p(J)=0.
}
\tag{3.25}
$$


Thus the large factorial divisibility of the raw endpoint minor is completely consumed by the row contents and the shared endpoint denominator before the normalized minor $J$ is reached.

It cannot be credited a second time as a divisor of $G$, or used to suggest a large $H_{\rm gcd}$. This resolves a specific actual-family common-factor issue left open in Turn 1.

---

## 4. Four small-prime transfers, with arbitrary-order proofs

The condition $\tau_n\not\equiv0\pmod p$ can be checked by base-$p$ digits.

Let


$$
\mathcal L(z)=z^{-1}+1+\frac z2.
$$


Then


$$
\tau_n=\operatorname{CT}_z\mathcal L(z)^n.
\tag{4.1}
$$


Writing $n=n_0+pm$, with $0\le n_0<p$, Frobenius gives


$$
\mathcal L(z)^n
=\mathcal L(z)^{n_0}\mathcal L(z^p)^m
\quad\text{in characteristic }p.
$$


The exponents in $\mathcal L(z)^{n_0}$ lie strictly between $-p$ and $p$. Only its constant term can combine with a multiple-of-$p$ exponent to give zero. Therefore


$$
\boxed{\tau_n\equiv\tau_{n_0}\tau_m\pmod p.}
\tag{4.2}
$$


Iterating,


$$
\boxed{\tau_n\equiv\prod_r\tau_{n_r}\pmod p.}
\tag{4.3}
$$



This is the arbitrary-order transfer. The following finite seed checks are its only bounded inputs.

The exact values through index $10$ are


$$
1,\ 1,\ 2,\ 4,\ \frac{17}{2},\ \frac{37}{2},\
41,\ 92,\ \frac{1667}{8},\ \frac{3803}{8},\ \frac{4363}{4}.
\tag{4.4}
$$


They also follow from


$$
(r+1)\tau_{r+1}=(2r+1)\tau_r+r\tau_{r-1}.
\tag{4.5}
$$



| $p$ | $(\tau_0,\ldots,\tau_{p-1})\bmod p$ |
|---|---|
| $3$ | $1,1,2$ |
| $5$ | $1,1,2,4,1$ |
| $7$ | $1,1,2,4,5,1,6$ |
| $11$ | $1,1,2,4,3,2,8,4,9,1,10$ |

All entries are nonzero. Consequently,


$$
\boxed{
\tau_n\not\equiv0\pmod p
\quad\text{for every }n\ge0,\quad p\in\{3,5,7,11\}.
}
\tag{4.6}
$$



No prime-density claim or infinite family of seed-good primes is being inferred from this table.

For the requested dimensions,


$$
D_2=1,\qquad D_3=2,\qquad D_4=9,\qquad D_8=14833.
\tag{4.7}
$$


Thus:

- $p=3,5,7,11$ are available for $d=2$;
- $p=5,7,11$ are available for $d=3,4$;
- $p=11$ is available for $d=8$.

The hypotheses matter. For example, $p=5$ is outside $p>d$ when $d=8$. Also $13\mid D_8$, so merely taking a prime larger than $d$ is insufficient.

---

## 5. Infinite denominator obstructions and rigorous nonvanishing

### 5.1 $d=2$, $105\mid n$

The theorem supplies the exact valuations


$$
v_p(\widehat q)=2v_p(n!)\qquad(p=3,5,7).
$$


Legendre’s formula gives


$$
v_p(n!)
=\frac{n-s_p(n)}{p-1}
\ge\frac{n}{p-1}-\lfloor\log_p n\rfloor-1.
$$


Therefore


$$
\boxed{
\widehat q
\ge
\frac{\exp(L_2n)}{11025\,n^6},
\qquad
L_2=\log3+\frac12\log5+\frac13\log7.
}
\tag{5.1}
$$


This is a lower bound for the actual denominator after the complete gcd.

A simple exact comparison suffices:


$$
e^{L_2}=3\sqrt5\,7^{1/3}
>3\cdot\frac{11}{5}\cdot\frac{19}{10}
=\frac{627}{50}>12,
$$


whereas


$$
M^2=3+2\sqrt2<6.
$$


Thus


$$
\frac{\widehat qM^{-2n-3}}n
>
\frac{2^n}{11025\,M^3n^7}.
\tag{5.2}
$$



In particular, no choice $h_0\mid H_{\rm gcd}$ can satisfy the sufficient cofactor estimate proposed in Turn 1 on this progression. Its proposed upper bound for $\widehat q$ is at least $\widehat q$, and $\widehat q$ already violates that scale exponentially.

### 5.2 $d=3,4$, $385\mid n$

Using $p=5,7,11$,


$$
\boxed{
\widehat q
\ge
\frac{\exp(L_{34}n)}{148225\,n^6},
\qquad
L_{34}=\frac12\log5+\frac13\log7+\frac15\log11.
}
\tag{5.3}
$$


Moreover,


$$
e^{L_{34}}
>
\frac{11}{5}\frac{19}{10}\frac85
=\frac{836}{125}>6,
$$


and in fact


$$
e^{L_{34}}/M^2>11/10.
$$


Hence, for either $d=3$ or $d=4$,


$$
\boxed{
\frac{\widehat qM^{-2n-d-1}}n
>
\frac{(11/10)^n}
{148225\,M^{d+1}n^7}
\longrightarrow\infty.
}
\tag{5.4}
$$



These progressions contain both parities and lie in the genuine fixed-$d$, hence all-sublinear, domain.

### 5.3 Pairwise distinct centers and eventual nonvanishing

Fix one of $d=2,3,4,8$, and let $n=11m$. The theorem gives


$$
v_{11}(\widehat q_{11m,d})
=2v_{11}((11m)!).
\tag{5.5}
$$


The right side is strictly increasing with $m$: passing from $(11m)!$ to $(11m+11)!$ introduces a new multiple of $11$.

Reduced rational numbers with different denominator valuations cannot be equal. Therefore the centers


$$
\widehat c_{11m,d}
$$


are pairwise distinct.

A fixed real number can equal at most one member of a pairwise distinct sequence. Thus


$$
\widehat c_{11m,d}=S
$$


for at most one $m$. This proves (1.9).

The same argument applies on $105\mid n$, $d=2$, using $p=3$, and on $385\mid n$, $d=3,4$, using $p=5$.

This is an **actual-family nonvanishing theorem**, not a deduction from the CSC remainder and not an abstract rational-array countermodel. It gives no effective first nonzero index, but proves that there is at most one exceptional index on each stated progression.

The local proof also gives


$$
c_0\ne c_b
$$


at every eligible prime-survival pair, since


$$
v_p(c_0)\ge1-2N_p,\qquad v_p(c_b)=-2N_p.
$$


Thus $J\ne0$ there without invoking the analytic CSC.

---

## 6. Full error, what is excluded, and what is still missing

### 6.1 The whole evaluated error is unchanged

Retain the exact force identity from the accepted reconstruction:


$$
e_j:=c_j-S
=
\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac{D}{P_j},
\qquad D=\det H_b.
\tag{6.1}
$$


Here the complete exponential force is


$$
eE_i
=-[z^{n+i}](1-z+z^2/2)^n
\int_0^1s^ne^{1-s+sz}\,ds,
$$




$$
E_j=\nu_{n,d}\!\left(
R_j\sum_{i=0}^{d}\sigma^i e_{d-i}(z^{-1})eE_i
\right).
\tag{6.2}
$$


The original $P_j,F_j$, their full contours, signed sectors, and both minus connectors remain those of the source.

With $\lambda=n^2/d$, the complete extrapolated error is


$$
\boxed{
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
}
\tag{6.3}
$$


The actual primitive form is exactly


$$
\boxed{
\widehat qS-\widehat p
=\widehat q(S-\widehat c).
}
\tag{6.4}
$$


The prime theorem concerns precisely this $\widehat q$, not a metric clearer, an unreduced Gram norm, or a denominator of an incomplete companion.

### 6.2 What the accepted analytic results supply

On $2\le d=o(n)$, Turn 1’s accepted deduction gives


$$
|\widehat c-S|
\le
CM^{-2n-b}
\left(
\frac{d+1}{n}
+\frac{n^2}{d}e^{-\kappa n}
\right).
\tag{6.5}
$$


For fixed $d$, this is $O(M^{-2n-b}/n)$.

The new arithmetic shows that the product of $\widehat q$ with this available scale diverges on the progressions in Sections 5.1–5.2. Therefore:

> **The proposed “make the final gcd large enough to use the current upper bound” route is impossible on these progressions.**

It does **not** follow that the actual whole forms diverge. Multiplying a diverging denominator by an error *upper bound* does not give an error lower bound.

### 6.3 The precise remaining obstacle to a full exclusion theorem

Put


$$
x=d/n^2,\qquad
r_{n,d}=\log(e_0/e_b)+x.
$$


The accepted exact relation is


$$
\frac{\widehat c-S}{e_b}
=1+\frac{e^{-x+r_{n,d}}-1}{x}.
\tag{6.6}
$$


Its zero threshold is


$$
r_*(x)=x+\log(1-x).
\tag{6.7}
$$



The new arithmetic proves that equality with this threshold can occur at most once on each of the specified progressions. It does not bound the distance to the threshold. The accepted CSC still permits the signed error to be much smaller than its upper-bound scale.

A concrete next lemma is therefore:

> **Endpoint-defect lower bound sought, already sufficient at $d=2$.**  
> Prove that there are $c>0$, a finite $K$, and $N$ such that, for $105\mid n$, $n\ge N$,
> 

$$
> \left|
> \frac{F_0}{P_0}
> -\left(1-\frac2{n^2}\right)\frac{F_b}{P_b}
> \right|
> \ge
> c\,n^{-K}\left|\frac{F_b}{P_b}\right|.
> \tag{6.8}
>
$$


> Every quantity is the actual finite-system quantity with its complete scalar contour.

This is a lower bound for a specific endpoint defect, not another common-error coefficient.

To see its consequence, the principal part of (6.3), at $d=2$, is


$$
(-1)^{n+1}\frac{n^2}{2}
\left[
\frac{F_0}{P_0}
-\left(1-\frac2{n^2}\right)\frac{F_b}{P_b}
\right].
$$


The already established complete factorial residual bounds give


$$
\begin{aligned}
\left|
\lambda\frac{E_0}{P_0}
+(1-\lambda)\frac{E_b}{P_b}
+(-1)^n\lambda\frac{D}{P_0}
\right|
\le{}&
C(2\lambda-1)\frac{2^d}{n!\sqrt n}\\
&+C\lambda\frac{\sqrt n}{n!B_0}.
\end{aligned}
\tag{6.9}
$$


For fixed $d$, this is smaller than $M^{-2n-b}$ times every fixed negative power of $n$. Thus (6.8), combined with the accepted signed endpoint law, would imply


$$
|\widehat c-S|
\ge c' n^{2-K}M^{-2n-3}
$$


eventually on $105\mid n$. Equation (5.1) would then prove


$$
|\widehat qS-\widehat p|\longrightarrow\infty.
$$



That final quantitative separation has not been proved here. Eventual nonvanishing has been proved independently, but nonvanishing alone does not supply it.

---

## 7. What the sixteen completed cases now tell us

The coordinator’s receipt establishes, at its finite scope, that all sixteen complete fractions agree with the decomposed final-gcd formula. The reported small values of $H_{\rm gcd}$ are consistent with the new theorem, but were not used to infer it.

Four entries directly test the theorem’s exact hypotheses:

| Actual pair | Eligible prime | Theorem predicts $v_p(\widehat q)$ | Receipt |
|---|---:|---:|---:|
| $n=65,d=2$ | $5$ | $2v_5(65!)=30$ | $30$ |
| $n=65,d=3$ | $5$ | $30$ | $30$ |
| $n=65,d=4$ | $5$ | $30$ | $30$ |
| $n=129,d=2$ | $3$ | $2v_3(129!)=124$ | $124$ |

Their shared/unshared valuations also match (3.20):

- $(65,2),p=5$: $v_p(h)=28,\ v_p(B)=2$;
- $(65,3),p=5$: $29+1=30$;
- $(65,4),p=5$: $29+1=30$;
- $(129,2),p=3$: $123+1=124$.

In all four, $A,F,G,H_{\rm gcd}$ are units at the indicated prime, as predicted.

The excluded hypotheses are visible too. At $(65,8)$, $p=5$ is not larger than $d$, and the receipt gives $v_5(\widehat q)=29$, not $30$. The theorem does not cover that case. At $(129,3)$, $p=3$ is likewise outside its range.

The numerical sign change between $d=3$ and $d=4$ is useful guidance against asserting a universal extrapolated-error sign. It is not needed for the nonvanishing theorem above. The supplied decimal errors are not, by themselves, rational interval certificates of those individual signs.

---

## 8. Bounded exact arithmetic for independent inspection

No new large reconnaissance grid is required for the arbitrary-order theorem. Its finite algebraic inputs are very small.

### 8.1 Seed certificate

**Inputs**

- Recurrence (4.5), with $\tau_0=\tau_1=1$;
- primes $3,5,7,11$;
- derangement recurrence
  

$$
D_0=1,\quad D_1=0,\quad
  D_j=(j-1)(D_{j-1}+D_{j-2});
$$


- target dimensions $2,3,4,8$.

**Expected verifiable output**

1. The eleven exact rational values in (4.4).
2. The four nonzero residue rows in the table in Section 4.
3. $D_2=1,D_3=2,D_4=9,D_8=14833$.
4. The stated eligible-prime checks.

The finite seed computation does not itself prove the all-$n$ conclusion; the exact digit transfer (4.2)–(4.3) does that.

### 8.2 Local audit using already computed complete columns

For the four records in Section 7, retain the personally inspected least $d_B$, full $U,V$, and endpoint $+1$. Verify exactly:



$$
p\nmid d_B,
$$




$$
v_p(U_0)=v_p(U_b)=2v_p(n!),\qquad
v_p(V_0)\ge1,\quad v_p(V_b)=0,
$$




$$
v_p(J)=v_p(T)=0,
$$




$$
v_p(r_0r_bh)=v_p(U_bV_0-U_0V_b)=2v_p(n!),
$$


and


$$
v_p(\widehat q)=2v_p(n!).
$$



These checks use repeated exact division by one small prime and gcds; no factorization of the large endpoint integers is required.

### 8.3 Optional certification of the sixteen individual whole errors

Using the already computed primitive $(\widehat p,\widehat q)$, form an exact rational interval for $S$ from:

- $\sum_{r=0}^{512}1/r!$, with its positive factorial tail bound;
- Machin’s identity
  

$$
\pi=16\arctan(1/5)-4\arctan(1/239),
$$


  with 512 alternating-series terms and next-term bounds.

Return rational intervals for both


$$
\widehat c-S,\qquad \widehat qS-\widehat p.
$$


An interval excluding zero certifies that individual whole error and its sign. An interval containing zero must be reported as inconclusive at the prescribed bound.

This would turn the receipt’s numerical signs into finite exact certificates. It would not prove the endpoint-defect lower bound (6.8).

---

## 9. Final ledger

### New results proved here

1. **Universal complete endpoint formulas and a finite-boundary recurrence**, directly matching `full_lift`, with both force components and the exterior $+1$.

2. **An exact local theorem for the actual final gcd**:
   

$$
v_p(\widehat q)=2v_p(n!)
$$


   under explicit hypotheses $p>d$, $p\mid n$, and $\tau_nD_d\not\equiv0\pmod p$.

3. **Identification of the shared-content obstruction**:
   

$$
v_p(H_{\rm gcd})=0,\qquad
   v_p(h)+v_p(B)=2v_p(n!).
$$


   Large raw-minor divisibility is already exhausted by $r_0r_bh$, leaving $J$ and $T$ units.

4. **Arbitrary-order small-prime transfers**, using proved digit factorization and exact seeds at $3,5,7,11$.

5. **Exponential failure of the current sufficient denominator budget** on:
   

$$
d=2,\quad105\mid n;
   \qquad
   d=3,4,\quad385\mid n.
$$



6. **Actual-family eventual nonvanishing**: for each $d=2,3,4,8$, the sequence $n=11m$ has pairwise distinct centers and therefore at most one zero whole error.

### Exact remaining bottlenecks

- A full exclusion theorem for the **actual primitive forms** on the new progressions requires a quantitative lower bound for the signed endpoint defect, such as (6.8). The current upper bound and the new denominator lower bound do not imply that conclusion.
- Outside the proved prime-survival subfamilies, the global size of $A,B$ and the all-prime shared gcd $H_{\rm gcd}$ remain unresolved.
- No same-index family of nonzero whole primitive forms tending to zero has been established.

The new arithmetic therefore points in a definite direction: on substantial genuine subfamilies, the shared endpoint denominator contains factorial prime powers that **survive**, rather than improve, the primitive denominator. The observed small shared gcd is no longer merely a numerical phenomenon at those primes and indices.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


