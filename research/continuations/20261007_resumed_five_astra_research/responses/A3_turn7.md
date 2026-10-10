> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fixed-amplitude forcing: an exponential-height logarithmic part and a factorial-height obstruction

## Abstract and proof status

The supplied work does not prove either rationality or irrationality of $e+\pi$. This report does not resolve that question.

The new result is a quantitative decomposition of the **actual amplitude-$2$, zero-seeded forced response**, with its original finite terminal retained. Write


$$
N=n+2,\qquad K=2n+2,\qquad
\mathscr L_N=\operatorname{lcm}(1,\ldots,N),\qquad
Q_n=2^{n-1}\mathscr L_N.
$$


The complete forced vector from A3 turn 6 has an exact decomposition


$$
\boxed{\mathbf Z_n=\mathbf E_n+A_n\mathbf L_n,\qquad
A_n=\frac{n!N!}{Q_n}\in\mathbb Z,}
$$


where both vectors are integral and


$$
\|\mathbf E_n\|_\infty<8N!10^n,\qquad
\|\mathbf L_n\|_\infty\le 2^{11}320^n.
$$


Here $\mathbf L_n$ contains the **entire logarithmic forcing with amplitude $2$**; $\mathbf E_n$ contains the entire exponential forcing. No physical source term is discarded. The logarithmic part therefore admits an explicitly proved exponential-height normalization using only primes at most $N$.

There is, however, a sharp fixed-source obstruction to declaring the **whole normalized forced transfer** to have exponential arithmetic height. At every original index,


$$
\boxed{\operatorname{den}(z_1/n!)=n!.}
$$


On the specified infinite original subfamily


$$
\boxed{\mathcal S=\{15^{2a}:a\ge1\},}
$$


the first forced coordinate is


$$
\boxed{z_1=1+\frac{n!}{2^{(n-3)/2}},}
$$


is coprime to every prime at most $N$, and satisfies


$$
\boxed{
\log z_1
=n\log n-\left(1+\frac{\log2}{2}\right)n+O(\log n).
}
$$


Thus this is an actual fixed-amplitude integer of factorial height, supported entirely on primes above $N$. It is not a free-seed or lattice counterexample.

This obstruction is deliberately limited: it defeats a coordinatewise “divide by $n!$, then use an $O(n)$-height forcing certificate” argument. It does **not** rule out a special endpoint adjoint identity that cancels this contribution.

For the paid endpoint contacts, the resulting proved general bound still has worst-case leading coefficient $4$ in $n\log n$ for the two-endpoint aggregate. The exact kernel, $F$, and binary payments are displayed below. This is not subfactorial. No useful moving-acquisition lower bound paying both retained losses is obtained.

---

## 1. Original objects and scope

The approximation indices remain exactly


$$
n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2.
$$


Set


$$
m=n+1,\qquad N=n+2,\qquad K=2n+2.
$$


All original $n$ are odd and at least $225$.

The source remains


$$
q(z)=1-z+\frac{z^2}{2},\qquad
\alpha_0=\alpha_1=1,\qquad
\alpha_s=\alpha_{s-1}-\frac12\alpha_{s-2},
$$




$$
\eta_s=\sum_{r=0}^s\frac1{r!}
       +2\sum_{r=1}^s\frac{\alpha_{r-1}}r,\qquad
\mathcal W_s=s!\eta_s.
$$


In particular,


$$
\mathcal W_s=s\mathcal W_{s-1}
+1+2(s-1)!\alpha_{s-1}.
$$



The physical convolution remains


$$
\widehat w_i
=\sum_{a=0}^{n+i}[z^a]q(z)^n
 \frac{\mathcal W_{2n+i-a}}{(n+i-a)!},
\qquad 0\le i\le2.
$$


Its maximum source index is exactly $K$. No inverse or forcing equation is extended beyond that terminal.

Let


$$
c_k=[z^k]e^zq(z)^n,\qquad
T=
\begin{pmatrix}
c_n&c_{n-1}&c_{n-2}\\
c_{n+1}&c_n&c_{n-1}\\
c_{n+2}&c_{n+1}&c_n
\end{pmatrix},
\qquad J=N!T.
$$


Write $J_0,J_1,J_2$ for the columns of $J$, and $\Delta=\det J$.

The reference vector is


$$
t=
\begin{pmatrix}
\tau_n\\
(\tau_n+\tau_{n+1})/2\\
\tau_{n+2}/2
\end{pmatrix},
\qquad H=N!t,
$$


with the retained recurrence


$$
\tau_0=\tau_1=1,\qquad
(k+2)\tau_{k+2}=(2k+3)\tau_{k+1}+(k+1)\tau_k.
$$



For assertions involving the inverse or the paid endpoint contact, the hypotheses remain


$$
\boxed{\det T\ne0,\qquad F\ne0,\qquad R_j\ne0.}
$$


Here $R_j=r_jH$, where $r_j$ is the actual primitive endpoint row. The forcing results in Sections 3–5 do not require these nondegeneracy assumptions. Consequently their infinite-family statements do not depend on an unproved assertion that a set of nondegenerate endpoint indices is infinite.

### Results reused rather than recomputed

The following are used at their supplied scope:

* the complete terminal identity
  

$$
N!\widehat w=J_0+E_nH+\mathbf C,
  \qquad E_n=n!\sum_{r=0}^n\frac1{r!};
$$


* the actual primitive endpoint rows and kernel contents;
* the polynomial intersection payments;
* the paid contact equality above $N$;
* the complete-source crossing formulas and their stated two-level scope;
* the temporal overlap theorem, which does not bound isolated entrances;
* the least-clearer and actual row-content formulas;
* A4’s all-prime primitive endpoint denominator formula;
* the archived binary denominator theorem on its explicit infinite subfamily.

The prime-$29$ construction is a different original family. No assertion from it is transferred to the present endpoints.

---

## 2. What the new finite certificate establishes

The coordinator’s supplied certificate reports, at $n=225$:

* all 228 forced positions satisfy the exact recurrence;
* the complete-source identity has zero residual;
* both saturated endpoint identities have zero residual;
* the endpoint-$0$ $+\Delta$ correction is present;
* the paid contact-loss product over all 38 primes
  

$$
227<p\le452
$$


  equals $1$.

There is an additional limitation visible directly in the certificate: at **every** listed prime, and at both endpoints,


$$
v_p(R_j)=0.
$$


Thus the finite product is $1$ because that band contains no positive reference depth at this index. It does not sample a positive-depth reference contact and show that the complete forcing prevents its lift.

The exceptional entry


$$
v_{347}(C_0)=1,\qquad v_{347}(\Xi_0)=0
$$


is consistent with


$$
C_0=\lambda_nR_0+\Xi_0,
$$


because $R_0$ is a $347$-adic unit. No contradiction or contact is implied.

These are useful finite checks. They supply no infinite depth estimate, and none is inferred here. No part of the producer, crossing, or frame audit is requested again.

---

## 3. The retained complete forced recurrence

Put


$$
Y(z)=\frac{e^z+2\int_0^zq(t)^{-1}\,dt}{1-z},
\qquad
g(z)=q(z)^nY^{(n)}(z).
$$


Then


$$
[z^{n+i}]g(z)=\widehat w_i.
$$



The homogeneous response is


$$
A(z)=\frac{q(z)^n}{(1-z)^{n+1}},
$$


whose three retained coefficients are $t$. Define the zero-seeded response by


$$
z(z)=g(z)-\mathcal W_nA(z)=\sum_{\ell\ge0}z_\ell z^\ell.
$$


Thus $z_{-2}=z_{-1}=z_0=0$.

To avoid a collision between a forcing coefficient and an endpoint row, denote the logarithmic polynomial coefficient by $\rho_\ell^{\rm force}$:


$$
\rho_\ell^{\rm force}
=n!(-1)^\ell\binom{n+1}{\ell}2^{-\ell}\alpha_{n-\ell},
\qquad 0\le\ell\le n,
$$


and $\rho_\ell^{\rm force}=0$ for $\ell>n$.

The complete recurrence is


$$
\begin{aligned}
(\ell+1)z_{\ell+1}={}&(2\ell+1)z_\ell
+\frac{2n+1-3\ell}{2}z_{\ell-1}\\
&+\frac{\ell-n-1}{2}z_{\ell-2}
+\epsilon_\ell+2\rho_\ell^{\rm force},
\end{aligned}
\tag{3.1}
$$


where


$$
\epsilon_\ell=[z^\ell]q(z)^{n+1}e^z
$$


is evaluated by the retained recurrence


$$
(\ell+1)\epsilon_{\ell+1}
=(\ell-n)\epsilon_\ell
+\left(n-\frac{\ell-1}{2}\right)\epsilon_{\ell-1}
+\frac12\epsilon_{\ell-2}.
$$



Only


$$
0\le\ell\le n+1
$$


is needed. Every division is by $2$ or by an integer at most $N$.

Set


$$
\mathbf Z_n=N!(z_n,z_{n+1},z_{n+2})^T.
$$


The established source-removal identity is


$$
\mathbf C=(\mathcal W_n-E_n)H+\mathbf Z_n-J_0.
\tag{3.2}
$$



The issue now is quantitative: what arithmetic height remains after separating the explicitly evaluated logarithmic forcing from the exponential forcing?

---

## 4. New theorem: a small-prime, exponential-height normalization of the logarithmic response

### 4.1 Exact separation of the two complete forcings

Write


$$
z_\ell=z_\ell^{\exp}+n!\,z_\ell^{\log},
\tag{4.1}
$$


where the logarithmic component includes amplitude $2$.

Let $q_a=[z^a]q(z)^n$. For $0\le\ell\le N$, put $v=\ell-a$. Directly from the original source,


$$
\boxed{
z_\ell^{\exp}
=\sum_{a=0}^{\ell}q_a
 \frac{(n+v)!}{v!}
 \sum_{u=1}^{v}\frac1{(n+u)!},
}
\tag{4.2}
$$


and


$$
\boxed{
z_\ell^{\log}
=2\sum_{a=0}^{\ell}q_a
 \binom{n+v}{n}
 \sum_{u=1}^{v}\frac{\alpha_{n+u-1}}{n+u}.
}
\tag{4.3}
$$


An inner sum is zero when $v=0$.

These formulas follow by subtracting $\eta_n$ from $\eta_{n+v}$ in the actual coefficient formula:


$$
z_\ell
=\sum_{a=0}^{\ell}q_a
 \frac{(n+v)!}{v!}(\eta_{n+v}-\eta_n).
$$


They include precisely the physical source indices $n+1,\ldots,n+\ell$, with $n+\ell\le K$.

Equations (4.2)–(4.3) are used below to prove integrality and height bounds. They are not being offered as an unevaluated replacement for the contact problem.

### 4.2 A denominator-cancellation lemma

**Lemma 4.1.** If


$$
0\le v\le N,\qquad 1\le u\le v,
$$


then


$$
\boxed{
\mathscr L_N\frac{\binom{n+v}{n}}{n+u}\in\mathbb Z.
}
\tag{4.4}
$$



**Proof.** Fix a prime $p$, and write $b=v_p(n+u)$.

If $p^b\le N$, then $\mathscr L_N$ already contains $p^b$.

Suppose $p^b>N$. Since


$$
n+u\le n+v\le K<2N,
$$


we have $p^{b-1}\le N$, so $\mathscr L_N$ contains at least $p^{b-1}$. Also $n,v<p^b$, whereas $n+v\ge p^b$. In Legendre’s formula for the binomial coefficient, the contribution at $p^b$ is


$$
\left\lfloor\frac{n+v}{p^b}\right\rfloor
-\left\lfloor\frac n{p^b}\right\rfloor
-\left\lfloor\frac v{p^b}\right\rfloor=1.
$$


All the other floor differences are nonnegative. Hence


$$
p\mid\binom{n+v}{n},
$$


paying the one remaining power. ∎

This proof treats the cancellation of possible denominator primes above $N$; it does not silently include them in a new clearer.

### 4.3 Dyadic accounting, including amplitude $2$

The recurrence for $\alpha_s$ gives


$$
\alpha_{s+4}=-\frac14\alpha_s,
\qquad
(\alpha_0,\alpha_1,\alpha_2,\alpha_3)=(1,1,\tfrac12,0).
$$


Consequently,


$$
2^{\lfloor s/2\rfloor}\alpha_s\in\{0,1,-1\}.
\tag{4.5}
$$


Also


$$
2^{\lfloor a/2\rfloor}q_a\in\mathbb Z.
\tag{4.6}
$$



In a term of (4.3), $a+u\le\ell\le N$, so


$$
\left\lfloor\frac a2\right\rfloor
+\left\lfloor\frac{n+u-1}{2}\right\rfloor
\le n.
$$


The explicit amplitude $2$ therefore reduces the needed dyadic payment to $2^{n-1}$.

Combining this with Lemma 4.1 proves


$$
\boxed{Q_nz_\ell^{\log}\in\mathbb Z,\qquad
Q_n=2^{n-1}\mathscr L_N,\qquad 0\le\ell\le N.}
\tag{4.7}
$$



This $Q_n$ is an explicit sufficient auxiliary clearer, not a claim about a least clearer. Every prime dividing it is at most $N$.

### 4.4 Exponential component

Each term of (4.2), after multiplication by $N!$, is integral. Indeed,


$$
\frac{(n+v)!}{(n+u)!}\in\mathbb Z.
$$


The possible denominator of $q_a$ divides $2^{\lfloor a/2\rfloor}$. Since $N-v\ge a$, the product $N!/v!$ contains at least $\lfloor a/2\rfloor$ even factors. Thus


$$
\boxed{N!z_\ell^{\exp}\in\mathbb Z,\qquad 0\le\ell\le N.}
\tag{4.8}
$$



### 4.5 Explicit height bounds

The coefficient absolute-value sum is


$$
\sum_a|q_a|\le(5/2)^n.
$$


Also


$$
\binom{n+v}{n}\le2^{n+v}\le2^K.
$$



For the exponential component,


$$
\frac{(n+v)!}{v!}
 \sum_{u=1}^{v}\frac1{(n+u)!}
\le
\frac{v}{n+1}\binom{n+v}{n}.
$$


Since $v\le N<2(n+1)$,


$$
\boxed{|z_\ell^{\exp}|<8\,10^n.}
\tag{4.9}
$$



Using $|\alpha_s|\le1$ in (4.3) similarly gives


$$
\boxed{|z_\ell^{\log}|<16\,10^n.}
\tag{4.10}
$$



For completeness, an elementary explicit estimate is


$$
\log\mathscr L_N<4N\log2.
\tag{4.11}
$$


One proof bounds $\mathscr L_N$ by the lcm at the next power of $2$, and uses


$$
\psi(2k)-\psi(k)\le\log\binom{2k}{k}\le2k\log2
$$


at successive dyadic scales.

Thus


$$
Q_n<2^{5n+7},
$$


and


$$
\boxed{|Q_nz_\ell^{\log}|\le2^{11}320^n.}
\tag{4.12}
$$



### Theorem 4.2 — Quantitative complete-source decomposition

Define


$$
\mathbf E_n=N!
\begin{pmatrix}
z_n^{\exp}\\z_{n+1}^{\exp}\\z_{n+2}^{\exp}
\end{pmatrix},
\qquad
\mathbf L_n=Q_n
\begin{pmatrix}
z_n^{\log}\\z_{n+1}^{\log}\\z_{n+2}^{\log}
\end{pmatrix}.
$$


Then


$$
\mathbf E_n,\mathbf L_n\in\mathbb Z^3,
$$




$$
\boxed{\mathbf Z_n=\mathbf E_n+A_n\mathbf L_n,\qquad
A_n=\frac{n!N!}{Q_n}\in\mathbb Z,}
\tag{4.13}
$$


and


$$
\boxed{
\|\mathbf E_n\|_\infty<8N!10^n,\qquad
\|\mathbf L_n\|_\infty\le2^{11}320^n.
}
\tag{4.14}
$$



**Remaining integrality check.** For odd primes, $Q_n\mid n!N!$ follows from $\mathscr L_N\mid N!$. At $2$,


$$
v_2(n!)+v_2(N!)-\lfloor\log_2N\rfloor\ge n-1
$$


for $n\ge225$, for example by $v_2(s!)=s-s_2(s)$. This proves $A_n\in\mathbb Z$.

Every prime dividing $A_n$ is at most $N$. In particular, $A_n$ is a unit at every contact prime $p>N$. It may not be deleted from the residue of the complete forcing.

---

## 5. New fixed-amplitude obstruction at an infinite original subfamily

The preceding theorem makes the logarithmic part small after normalization. It does not make the whole forcing small in arithmetic height.

At $\ell=0$, the exact forced recurrence gives


$$
\boxed{z_1=1+2n!\alpha_n.}
\tag{5.1}
$$


The $1$ is the complete exponential forcing at that position. Dropping it changes the source.

On the original domain,


$$
n\equiv1\ \text{or}\ 7\pmod8.
$$


Using (4.5),


$$
\alpha_n=
\begin{cases}
2^{-(n-1)/2},&n\equiv1\pmod8,\\
0,&n\equiv7\pmod8.
\end{cases}
$$


Therefore


$$
z_1=
\begin{cases}
1+n!/2^{(n-3)/2},&n\equiv1\pmod8,\\
1,&n\equiv7\pmod8.
\end{cases}
\tag{5.2}
$$



### Theorem 5.1 — Exact primitive height at the first forced position

At every original index,


$$
\boxed{\gcd(z_1,n!)=1,\qquad
\operatorname{den}(z_1/n!)=n!.}
\tag{5.3}
$$


For $n\ge225$, the logarithmic height of the reduced rational number $z_1/n!$ is exactly


$$
\boxed{h(z_1/n!)=\log(n!).}
\tag{5.4}
$$



**Proof.** The assertion is immediate when $z_1=1$.

Otherwise, put $k=(n-1)/2$. Every odd prime dividing $n!$ divides $n!/2^{k-1}$, so $z_1\equiv1$ at that prime. Moreover,


$$
v_2(n!)\ge k,
$$


so $n!/2^{k-1}$ is even and $z_1$ is odd. Hence $\gcd(z_1,n!)=1$.

For the original $n\ge225$, $0<z_1<n!$, so the reduced denominator is the larger of numerator and denominator. ∎

### Theorem 5.2 — A factorial-height rough integer from the actual source

On


$$
\mathcal S=\{n=15^{2a}:a\ge1\},
$$


one has


$$
\boxed{\gcd(z_1,\mathscr L_N)=1.}
\tag{5.5}
$$


Thus every prime factor of $z_1$ exceeds $N$. Furthermore,


$$
\boxed{
\log z_1
=n\log n-\left(1+\frac{\log2}{2}\right)n+O(\log n).
}
\tag{5.6}
$$



**Proof.** Here $n\equiv1\pmod{32}$, in particular $n\equiv1\pmod8$. Theorem 5.1 excludes all primes at most $n$. The integer $n+1$ is even and is not a new prime.

It remains only to consider $p=n+2$ if it is prime. Then $p\equiv3\pmod8$. Wilson’s theorem gives


$$
n!=(p-2)!\equiv1\pmod p.
$$


Euler’s criterion gives


$$
2^{(n-3)/2}=2^{(p-5)/2}\equiv-\frac14\pmod p.
$$


Consequently,


$$
z_1\equiv1-4=-3\not\equiv0\pmod p.
$$


This proves (5.5).

Finally,


$$
\log z_1
=\log(n!)-\frac{n-3}{2}\log2+o(1),
$$


and Stirling’s formula gives (5.6). ∎

### Exact scope of the obstruction

This is a source-specific theorem for the fixed amplitude $2$, not a seed-blind CRT argument.

It proves that:

* normalizing every forced position by $n!$ requires a simultaneous clearer divisible by $n!$;
* the first primitive numerator itself has leading factorial-height coefficient $1$ on $\mathcal S$;
* above-$N$ arithmetic cannot be made small merely by calling the normalized logarithmic forcing exponential-height.

It does **not** prove that this large integer survives either endpoint projection. The endpoint functional can mix all forced positions and can cancel its contribution. A successful adjoint identity must establish that cancellation quantitatively rather than assume it.

Also, (5.5) does not determine how the prime factors divide between


$$
N<p\le K
\quad\text{and}\quad
p>K.
$$


No above-terminal conclusion is inferred from it.

---

## 6. Exact endpoint transport of the new decomposition

Write


$$
\mathbf t_j=\ell_j\operatorname{adj}(J),\qquad
\ell_0=(-1,n,-nm),\quad \ell_3=(0,0,1),
$$




$$
h_j^K=\gcd\bigl(|t_{j,0}|,|t_{j,1}|,|t_{j,2}|\bigr),
\qquad
r_j=\sigma_j\mathbf t_j/h_j^K.
$$


These are the actual kernel contents and actual saturated endpoint rows.

The omitted projections remain


$$
\mathbf t_3J_2=\Delta,\qquad
\mathbf t_0J_0=-\Delta.
$$


Therefore the evaluated complete endpoint numerator is


$$
\boxed{
\Xi_j=r_j(\mathbf E_n-J_0)+A_n\,r_j\mathbf L_n.
}
\tag{6.1}
$$


In raw-row form,


$$
\Xi_3=\frac{\sigma_3}{h_3^K}
 \mathbf t_3(\mathbf E_n+A_n\mathbf L_n),
\tag{6.2}
$$


whereas


$$
\boxed{
\Xi_0=\frac{\sigma_0}{h_0^K}
 \left[\mathbf t_0(\mathbf E_n+A_n\mathbf L_n)+\Delta\right].
}
\tag{6.3}
$$


The exterior correction has not been lost in the new decomposition.

Combining with (3.2),


$$
C_j=(\mathcal W_n-E_n)R_j+\Xi_j.
$$


Hence, with the existing $F$-payment retained,


$$
\boxed{
s_j(p)=
\min\{(v_p(R_j)-v_p(F))_+,v_p(\Xi_j)\},
\qquad p>N.
}
\tag{6.4}
$$



Equation (6.1) locates the quantitative difficulty more precisely than a homogeneous-source argument:

* $r_j\mathbf L_n$ is the projection of an exponentially bounded integral vector;
* $A_n$ is a known small-prime-supported unit at $p>N$, but has factorial real height;
* $r_j(\mathbf E_n-J_0)$ is the complete exponential/exterior contribution;
* the **sum**, not either summand, controls the paid contact.

Neither a bound for $\mathbf L_n$ nor a unit assertion for $A_n$ bounds the valuation of this sum.

---

## 7. The proved height budget for paid contacts

The following bound is not the desired subfactorial theorem. Its purpose is to give an explicit, correctly paid quantitative baseline.

### 7.1 Removing only legitimate reference factors

Since


$$
A(z)=q(z)^n(1-z)^{-n-1},
$$


the vector


$$
\mathbf T_n=2^nt
$$


is integral. Define the nonzero integer


$$
\mathcal B_j=r_j\mathbf T_n
=\frac{2^nR_j}{N!}.
\tag{7.1}
$$


At every $p>N$,


$$
v_p(\mathcal B_j)=v_p(R_j).
$$


Thus the reference $N!$-factor has been removed by a genuine integral normalization, not by assuming a factorial unit at small primes.

### 7.2 Explicit size bound, with actual kernel content

Cauchy’s estimate on $|z|=1$ gives


$$
|J_{ab}|\le N!e(5/2)^n.
$$


On $|z|=1/2$,


$$
|q(z)|\le13/8,\qquad
|(1-z)^{-n-1}|\le2^{n+1}.
$$


For the three retained coefficients,


$$
\|t\|_\infty\le8(13/2)^n.
$$



Every adjugate entry is bounded by twice the square of the entry bound. Moreover,


$$
\|\ell_3\|_1=1,\qquad
\|\ell_0\|_1=1+n+nm=m^2.
$$


Consequently, with $w_3=1$ and $w_0=m^2$,


$$
\boxed{
|\mathcal B_j|
\le
\frac{48e^2w_j}{h_j^K}
(N!)^2(325/4)^n.
}
\tag{7.2}
$$



This retains the actual $h_j^K$, rather than replacing the primitive row by an unpaid raw row.

### 7.3 Paid aggregate

Set


$$
\mathcal C_j^{>}(n)=\prod_{p>N}p^{s_j(p)},
\qquad
\Gamma_j(n)=\gcd(|\mathcal B_j|,|F|)_{>N}.
$$


From (6.4),


$$
\mathcal C_j^{>}(n)
\mid \frac{(|\mathcal B_j|)_{>N}}{\Gamma_j(n)}.
\tag{7.3}
$$



On $\mathcal S$, reuse the archived binary reference depths:


$$
v_2(R_0)=k+2,\qquad v_2(R_3)=k,\qquad
k=(n-1)/2.
$$


Writing $t_2=v_2(n!)$, one has $v_2(N!)=t_2+1$, and therefore


$$
v_2(\mathcal B_0)=n+k+1-t_2,\qquad
v_2(\mathcal B_3)=n+k-1-t_2.
\tag{7.4}
$$



Let


$$
\mathcal C_{\rm agg}(n)=
\prod_{p>N}p^{\max(s_0(p),s_3(p))}.
$$


Using (7.2)–(7.4),


$$
\boxed{
\begin{aligned}
\log\mathcal C_{\rm agg}(n)
\le{}&
4\log(N!)
+2n\log(325/4)
+2\log(48e^2)+2\log m\\
&-\log(h_0^Kh_3^K)
-\log(\Gamma_0\Gamma_3)\\
&-(3n-1-2t_2)\log2.
\end{aligned}
}
\tag{7.5}
$$



All displayed deductions are valid for the actual nondegenerate endpoints. The $\Gamma_j$ are not claimed to have been asymptotically evaluated; they explicitly retain the existing $F$-payment.

Since $t_2=n-O(\log n)$, the explicit binary payment is $O(n)$. If no further growth of the actual $h_j^K$ or $\Gamma_j$ is proved, the certified worst-case leading term in (7.5) is


$$
\boxed{4n\log n.}
\tag{7.6}
$$


For one endpoint the corresponding worst-case coefficient is $2$.

This is **not**


$$
o(n\log n).
$$


Calling it subfactorial would be incorrect.

### Separate prime bands

Define


$$
\mathcal C_{\rm cross}
=\prod_{N<p\le K}p^{\max(s_0(p),s_3(p))},
$$




$$
\mathcal C_{\rm high}
=\prod_{p>K}p^{\max(s_0(p),s_3(p))}.
$$


Then


$$
\mathcal C_{\rm agg}
=\mathcal C_{\rm cross}\mathcal C_{\rm high}.
$$


The size argument bounds their product, but proves no separate depth restriction in either band. In particular, it does not extend the crossing formulas above $K$.

---

## 8. Primitive endpoint and final weighted denominators

An estimate for paid contact loss is not yet an estimate for the final primitive denominator.

### 8.1 Complete corrected columns and physical returns

With


$$
x=T^{-1}(n!t),\qquad y=T^{-1}\widehat w,
\qquad
S=
\begin{pmatrix}
1&-n&nm\\
0&1&-2n\\
0&0&1
\end{pmatrix},
$$


write $sx=Sx,\ sy=Sy$. The complete columns remain


$$
u=(-sx_0,\ sx_0-sx_1,\ sx_1-sx_2,\ sx_2),
$$




$$
v=(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2).
$$


The exterior $+1$ is present.

The physical returns remain


$$
N_0=\det T+R_0^{\rm raw}\widehat w,\qquad
N_3=R_3^{\rm raw}\widehat w.
$$


Nothing here removes the retained coefficient $1$ of the terminal force in the physical return.

The least simultaneous clearer is still


$$
D_8=\operatorname{lcm}_{0\le j\le3}
\bigl(\operatorname{den}(u_j),\operatorname{den}(v_j)\bigr)
=\frac{|\Delta|}{d_{\rm one}}.
$$


The actual contents and rows are


$$
g_j^{(8)}=\gcd(|D_8u_j|,|D_8v_j|),
$$




$$
\widetilde u_j=D_8u_j/g_j^{(8)},\qquad
\widetilde v_j=D_8v_j/g_j^{(8)}.
$$


Neither $Q_n$ nor any forcing normalization replaces $D_8$.

### 8.2 Reused all-prime endpoint formula

Put


$$
g_j^*=\gcd(|R_j|,|C_j|),\qquad
\zeta_j=\frac{C_j+E_nR_j}{g_j^*},\qquad
\phi_j=\gcd(n!,|\zeta_j|).
$$


A4’s exact formula is


$$
\boxed{
d_j:=|\widetilde u_j|
=\frac{|R_j|}{g_j^*}\frac{n!}{\phi_j}.
}
\tag{8.1}
$$


The residual factorial divisor is retained.

Above $N$, the actual denominator satisfies the supplied exact comparison


$$
\frac{D_{j,>N}}{S_j}
\mid (d_j)_{>N}
\mid F_{>N}\frac{D_{j,>N}}{S_j},
\qquad
S_j=\gcd(D_j,|C_j|)_{>N}.
\tag{8.2}
$$


An upper bound for $S_j$ does not by itself evaluate either side.

On $\mathcal S$, the archived theorem gives, without recalculation,


$$
\boxed{
v_2(d_0)=t_2+k-1,\qquad
v_2(d_3)=t_2+k-3.
}
\tag{8.3}
$$


This is an exponential-scale binary result. It does not remove a positive $n\log n$ coefficient.

### 8.3 All-prime weighted normalization

For signed primitive first entries, write


$$
h_{\rm end}=\gcd(|\widetilde u_0|,|\widetilde u_3|),
\quad
\widetilde u_0=h_{\rm end}A_{\rm wt},\quad
\widetilde u_3=h_{\rm end}B_{\rm wt}.
$$


For a reduced weight $\lambda=a/k_{\rm wt}$, $k_{\rm wt}>0$, retain


$$
J_{\rm wt}=B_{\rm wt}\widetilde v_0-A_{\rm wt}\widetilde v_3,
$$




$$
T_{\rm wt}=aJ_{\rm wt}+k_{\rm wt}A_{\rm wt}\widetilde v_3,
$$




$$
F_{\rm gcd}
=\gcd(|A_{\rm wt}|,|a|)
 \gcd(|B_{\rm wt}|,|a-k_{\rm wt}|),
$$




$$
G_{\rm wt}=\gcd(k_{\rm wt},|J_{\rm wt}|),
$$




$$
H_{\rm gcd}
=\gcd\!\left(
h_{\rm end},
\frac{|T_{\rm wt}|}{F_{\rm gcd}G_{\rm wt}}
\right).
$$


Then


$$
\boxed{
q_\lambda=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
}
$$




$$
\boxed{
p_\lambda=
\operatorname{sgn}(A_{\rm wt}B_{\rm wt})
\frac{T_{\rm wt}}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}}.
}
\tag{8.4}
$$


Every gcd is all-prime.

For an explicit conservative height comparison, (7.2) and (8.1) give


$$
d_j\le
\frac{48e^2w_j\,n!(N!)^3(325/8)^n}
{h_j^K g_j^*\phi_j}.
$$


Consequently


$$
\boxed{
q_\lambda\le
\frac{
k_{\rm wt}(48e^2)^2m^2(n!)^2(N!)^6(325/8)^{2n}
}{
h_0^Kh_3^K\,g_0^*g_3^*\,\phi_0\phi_3\,
h_{\rm end}F_{\rm gcd}G_{\rm wt}H_{\rm gcd}
}.
}
\tag{8.5}
$$


This keeps all actual payments. Without a further lower bound for their product, the conservative numerator has leading coefficient $8$ in $n\log n$, in addition to $\log k_{\rm wt}$. This is a worst-case upper bound, not an assertion that the actual denominator has that leading coefficient.

### 8.4 Same-index whole error

The required error is


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=q_\lambda\left[
(e+\pi)-\lambda\frac{\widetilde v_0}{\widetilde u_0}
-(1-\lambda)\frac{\widetilde v_3}{\widetilde u_3}
\right].
}
\tag{8.6}
$$


Equivalently, the archived notation gives


$$
q_\lambda(e+\pi)-p_\lambda
=q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
$$


No estimate for a different weight or for one summand is substituted.

If


$$
\mathcal E_n(\lambda)
=\left|
(e+\pi)-\lambda\frac{\widetilde v_0}{\widetilde u_0}
-(1-\lambda)\frac{\widetilde v_3}{\widetilde u_3}
\right|,
$$


then the exact requirement is


$$
\log q_\lambda+\log\mathcal E_n(\lambda)\longrightarrow-\infty,
$$


together with nonvanishing, on the same infinite original indices.

For example, the conservative bound (8.5), with
$\log k_{\rm wt}=o(n\log n)$, would be sufficient if a same-index theorem proved


$$
0<\mathcal E_n(\lambda)
\le \exp(-(8+\varepsilon)n\log n)
$$


for some fixed $\varepsilon>0$. No such whole-error theorem is supplied or proved here. The actual payments may improve this sufficient threshold, but their unknown asymptotics may not be replaced by favorable assumptions.

---

## 9. Why acquisition remains a different obligation

The retained moving-index identity is


$$
\boxed{
\mathcal I_t
=\frac{\mathcal I_n c^{\min}_{n,t}}
{\mathcal M_{n,t}\mathcal L_{n,t}},
\qquad t=bn,\quad b\in\{15,105\},
}
$$


where


$$
\mathcal M_{n,t}
=\prod_{n+2<p\le t+2}
p^{\min(v_p(F_n),v_p(M_n))}
$$


and


$$
\mathcal L_{n,t}
=\prod_{p>t+2}p^{(a_n(p)-a_t(p))_+}.
$$



Neither loss has been canceled.

The factorial-size integer $z_1$ of Theorem 5.2 is not a useful-acquisition theorem. Its factors have not been proved to enter the required inventory or survive either endpoint projection. Likewise, (7.5) is an upper bound for contact loss, not a lower bound for $c^{\min}_{n,t}$.

The temporal theorem controls adjacent overlaps, not isolated terminal acquisition. It therefore supplies no missing lower bound here.

---

## 10. Concrete next lemma and the remaining adjoint problem

The new decomposition reduces one genuine uncertainty: the normalized logarithmic response is now known to be an integral vector of height $O(n)$, with an explicitly paid clearer supported at primes at most $N$.

The remaining endpoint expression is the specific integer


$$
\boxed{
r_j(\mathbf E_n-J_0)+A_n r_j\mathbf L_n.
}
\tag{10.1}
$$


Both summands, including the exterior return, are evaluated by the original finite source.

A useful next lemma is therefore the following.

> **Fixed-source endpoint cancellation lemma.**  
> On a proved infinite set of nondegenerate indices in $\mathcal S$, establish
> 

$$
> \sum_{N<p\le K}
> \max_{j=0,3}
> \min\!\left\{
> (v_p(\mathcal B_j)-v_p(F))_+,\,
> v_p\!\left(r_j(\mathbf E_n-J_0)+A_n r_j\mathbf L_n\right)
> \right\}\log p
> =o(n\log n).
>
$$


> Prove a separate corresponding estimate for $p>K$, or explicitly identify a source identity that treats both bands.

A source-specific Bézout or adjoint proof of this lemma must meet three additional checks:

1. **Endpoint cancellation of the factorial-height coordinate.**  
   It must explain why the primitive contribution exhibited in Theorem 5.1 disappears or is sufficiently paid. The full normalized transfer does not have $O(n)$ height.

2. **Complete fixed-amplitude forcing.**  
   It must retain both terms in (10.1). An adjoint identity for $r_j\mathbf L_n$ alone is insufficient.

3. **A nonzero evaluated certificate.**  
   After actual kernel saturation and the existing $F$-payment, its final integer must be proved nonzero and have the claimed height. A formal resultant, a named gcd, or an unevaluated adjoint pairing does not establish that bound.

No theorem here proves that such a special endpoint identity is impossible. The fixed-seed problem remains open. What is ruled out is the specific coordinatewise small-height shortcut.

---

## 11. Bounded exact arithmetic, if an auxiliary certificate is desired

No calculation has been executed in this report. None is needed for Theorems 4.2, 5.1, or 5.2.

A new, bounded optional check can certify the **new forcing decomposition**, without repeating the completed recurrence, crossing, or frame audits.

### Inputs

Use only the preserved $n=225$ data:


$$
N=227,\qquad K=452,\qquad
\mathbf Z_{225},\ J_0,\ r_0,\ r_3,
$$


and the already available coefficients of $q(z)^{225}$.

Form


$$
Q_{225}=2^{224}\operatorname{lcm}(1,\ldots,227),
\qquad
A_{225}=\frac{225!\,227!}{Q_{225}}.
$$


Evaluate (4.3) only for


$$
\ell=225,226,227.
$$


This uses $\alpha_s$ only through $s=451$, inside the original physical source range.

### Expected verifiable outputs

1. Three integers forming $\mathbf L_{225}$, with
   

$$
\|\mathbf L_{225}\|_\infty\le2^{11}320^{225};
$$


   in particular each absolute value has at most 1884 binary digits.

2. An integral vector
   

$$
\mathbf E_{225}
   =\mathbf Z_{225}-A_{225}\mathbf L_{225},
$$


   satisfying
   

$$
\|\mathbf E_{225}\|_\infty<8\cdot227!\cdot10^{225}.
$$



3. Zero residuals in the two new decomposed endpoint identities
   

$$
\Xi_j-r_j(\mathbf E_{225}-J_0)
          -A_{225}r_j\mathbf L_{225}=0.
$$



No prime factorization, enlarged prime inspection, new producer, or first-size extrapolation is requested. This optional check would certify only those three finite decompositions.

---

## Conclusion

The new proved advance is a quantitative separation of the actual complete forcing:


$$
\boxed{
\mathbf Z_n=\mathbf E_n+
\frac{n!N!}{2^{n-1}\operatorname{lcm}(1,\ldots,N)}
\,\mathbf L_n,
}
$$


with integral $\mathbf L_n$ of logarithmic height $O(n)$, integral $\mathbf E_n$ of height $\log(N!)+O(n)$, and all source terms and paid divisions retained.

The new fixed-amplitude obstruction is equally explicit:


$$
\boxed{\operatorname{den}(z_1/n!)=n!,}
$$


and on $n=15^{2a}$,


$$
\boxed{
z_1=1+n!/2^{(n-3)/2},\qquad
(z_1)_{\le N}=1,\qquad
\log z_1=n\log n-\left(1+\tfrac12\log2\right)n+O(\log n).
}
$$


Thus the complete forcing cannot be assigned exponential arithmetic height by a coordinatewise factorial normalization.

After actual saturation, $F$-payment, and the known binary payment, the proved general two-endpoint contact bound still has worst-case leading term $4n\log n$. It does not reach the needed subfactorial scale. The exact all-prime primitive endpoint formula, residual factorial divisor, least simultaneous clearer, actual contents, final weighted gcd, and whole signed error all remain necessary.

The precise unresolved bottleneck is now the arithmetic cancellation in


$$
r_j(\mathbf E_n-J_0)+A_n r_j\mathbf L_n
$$


at the same primes where the paid reference projection is deep, separately in the crossing and above-terminal bands. Alternatively, one needs a useful moving-acquisition lower bound that pays both retained losses. Neither has been proved.

Finally, an irrationality proof still requires nonzero integer linear forms


$$
q_\lambda(e+\pi)-p_\lambda\longrightarrow0
$$


at the same infinite original indices. No result in this report supplies that final chain.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


