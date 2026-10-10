> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 Turn 17: an original-domain obstruction to pointwise reciprocal-moment domination

## 1. Executive summary

The rationality or irrationality of $e+\pi$ remains unresolved.

This report does **not** prove the requested uniform estimate


$$
|F|\le C hR,
$$


nor an infinite-domain estimate forcing $g/R$ to grow. It does establish a new, explicitly evaluated obstruction to a natural proposed proof of that estimate.

The new result concerns the **actual original contact polynomial**, not an auxiliary small-index substitute:

> **Original-domain signed-kernel theorem.**  
> There is an exact reciprocal-moment representation
> 

$$
> \frac{R}{|F|}=\int_0^\infty \mathcal K_n(x)\,d\mathbb P_n(x),
>
$$


> where $\mathbb P_n$ is a positive probability measure constructed from the actual modified orthogonal polynomial. Nevertheless, at every original index,
> 

$$
> \boxed{
> \mathcal K_n\!\left(\frac1{16n}\right)>\frac{15}{4},
> \qquad
> \mathcal K_n\!\left(\frac4n\right)<-\frac{23}{25}.
> }
>
$$


> In particular, the exact reciprocal-moment comparison kernel changes sign inside $(0,1)$, where the probability density is strictly positive.

Thus positive modified orthogonality does **not** turn the desired $F/R$ comparison into pointwise domination by a positive reciprocal kernel. This failure occurs throughout the original domain, including


$$
u=2+29^9(1+6068205v),\qquad v\ge0,
$$


subject to the original admissibility conditions and lower cutoff.

The calculation also identifies the cancellation explicitly. On the scale $x=c/n$, the kernel has the uniform limit


$$
\mathcal K_n(c/n)\longrightarrow
4\sum_{k=0}^{\infty}\frac{(-c)^k}{k!(5/4)_k},
\qquad 0\le c\le4,
$$


with a fully explicit error bound. The limiting series is negative at $c=4$; its sign is certified below by a five-term rational calculation.

This is a **rigorous failed implication that narrows the question**, not a proof that the desired averaged inequality is false. The remaining possibility is that cancellation in the *integrated* signed kernel yields


$$
\int\mathcal K_n\,d\mathbb P_n\ge\frac1{Ch}.
$$


A concrete, evaluated tail lemma sufficient for that conclusion is given in Section 9.

No tools or new numerical computation were used.

---

## 2. Original objects and arithmetic payments

### 2.1 Domain and finite boundaries

Retain


$$
b=3^{249005515+574312172u},\qquad n=2001b,
\qquad u\equiv2\pmod{29^9},
$$


with every original admissibility condition on $u$. Put


$$
d=b-1,\qquad h=n-d=2000b+1.
$$


Thus $d$ is even and $n,h$ are odd.

The finite matrix remains


$$
H_{rj}(X)=X-A_{n+r,j}-B_j,\qquad 0\le r,j\le d,
$$


where


$$
A_{m,j}
=j!\sum_{v=0}^{m-j}(-1)^v\binom{m-j}{v}\frac1{(j+v)!},
$$


and


$$
B_j=4\sum_{v=0}^{2j-1}\frac{(-1)^v}{2v+1},
\qquad B_0=0.
$$



The physical row window is exactly


$$
n,n+1,\ldots,n+d,
$$


and the column window is $0,\ldots,d$. Every summand of every $B_j$ is retained.

The separate earlier producer, with its own corrected forcing, returns and physical terminal, is not identified with this matrix. Those formulas are absent from the supplied packet. No cancellation or arithmetic gain is transferred to that producer.

### 2.2 Actual contents and clearers

To avoid confusing the matrix entries with the positive scalar $R$, write


$$
\mathsf A_{rj}=A_{n+r,j}+B_j,\qquad
\mathsf W_{rj}=(n+r)!\mathsf A_{rj}.
$$


Retain the actual quantities


$$
\kappa_r=\gcd\bigl((n+r)!,\mathsf W_{r0},\ldots,\mathsf W_{rd}\bigr),
\qquad
C_r=\frac{(n+r)!}{\kappa_r},
$$




$$
Y_{rj}=C_r\mathsf A_{rj},\qquad
c_j=\gcd_{0\le r\le d}(C_r,Y_{rj}),
$$




$$
\mathcal L_n=\operatorname{lcm}_{0\le r\le d}C_r,\qquad
P_n=\frac{\prod_{r=0}^dC_r}{\prod_{j=0}^dc_j}.
$$


Then


$$
D_n(X)=
\det\left[\frac{C_rX-Y_{rj}}{c_j}\right]_{r,j=0}^d
=P_n\det H(X)=U_nX-V_n
$$


is the same paid integer polynomial as before.

The finite-difference payment remains


$$
K_n=
\frac{\prod_{r=0}^d(n+r)!}
     {\prod_{j=0}^d j!(n-j)!}.
$$


The established scalar reduction is


$$
D_n(X)=\frac{P_n\tau_n}{aK_n}(FX-E-T).
\tag{2.1}
$$


Here $a$ is the actual least coefficient clearer defined below, and $\tau_n$ is the established cofactor normalization. For completeness, it can be written


$$
\tau_n=
\frac{(-1)^n}{n!}
\frac{\prod_{s=0}^{d-1}s!}{\prod_{j=h}^{n-1}j!}
\frac{\Delta_h}{\Delta_h^{(0)}},
$$


where


$$
\Delta_h^{(0)}=\prod_{i=0}^{h-1}i!(i+b)!,
$$


and $\Delta_h$ is the moment determinant of the actual modified weight.

None of these divisions is removed by the analytic normalizations below.

---

## 3. Established scalar data and their precise scope

Let $p_h$ be the monic degree-$h$ orthogonal polynomial for


$$
d\mu(x)=x^b(x-1)^d e^{-x}\,dx,\qquad x>0.
\tag{3.1}
$$


The measure is positive apart from isolated zeros because $d$ is even.

Its moments are


$$
\mu_j=\sum_{v=0}^d(-1)^{d-v}\binom dv(j+b+v)!.
$$


The construction of $p_h$ requires moments through $\mu_{2h-1}$; the largest factorial is $(2n)!$.

Let $a>0$ be the actual least coefficient clearer, and retain


$$
r(x)=a(x-1)^dp_h(x)=\sum_{k=0}^nr_kx^k.
$$


This is the actual primitive integer polynomial.

The charges remain


$$
F=\sum_{k=0}^nr_kk!,\qquad
E=\sum_{k=0}^nr_k\sum_{v=0}^k\frac{k!}{v!},
$$




$$
\gamma_j=(-1)^{n-j}(n-j)!r_{n-j}
-\sum_{i<j}\binom{n+1}{j-i}\gamma_i,
$$




$$
w_j=\binom nj\gamma_j,\qquad W(y)=\sum_{j=0}^dw_jy^j,
\qquad T=\sum_{j=0}^dw_jB_j.
$$



On the original domain, the established factorial divisibility gives


$$
\ell=1,\qquad T\in\mathbb Z.
$$


The unchanged positive integer charge is


$$
R=\sum_{k=0}^n|r_k|
\frac{k!(3/4)_k}{(n-k+1/4)_{k+1}}
=-4\sum_{j=0}^d\frac{w_j}{4j+1}\in\mathbb Z_{>0}.
\tag{3.2}
$$



The actual ALL-prime reduction is


$$
g=\gcd(|F|,|E+T|),\qquad
q=-\frac Fg>0,\qquad p=-\frac{E+T}{g}.
\tag{3.3}
$$


The paid determinant’s final gcd remains exactly


$$
G_n=\gcd(U_n,|V_n|)=U_n\frac g{|F|}.
\tag{3.4}
$$



The accepted whole-error result is


$$
M=F(e+\pi)-E-T
=e\int_0^1e^{-x}r(x)\,dx
+4\int_0^1\frac{W(s^4)}{1+s^2}\,ds<0,
$$


and


$$
\boxed{
\frac{R}{2g}<q(e+\pi)-p<6005\frac Rg.
}
\tag{3.5}
$$


Both complete channels and their endpoints remain present.

I also reuse the assigned arithmetic conclusions


$$
\mathcal D_h\mid q,\qquad h\mid q,
$$


where


$$
\mathcal D_h=\prod_{\mathfrak p\mid h}
\mathfrak p^{\,v_{\mathfrak p}(h!)-v_{\mathfrak p}(d!)}.
$$


They imply, without discarding any other prime,


$$
g=\frac{|F|}{q}\le\frac{|F|}{h}.
\tag{3.6}
$$



The new analysis therefore concerns precisely the missing comparison


$$
\frac{R}{|F|}\ge\frac1{Ch}.
\tag{3.7}
$$



---

## 4. An exact reciprocal-moment representation

Write the zeros of $p_h$ as


$$
\rho_1,\ldots,\rho_h,
\qquad
P(x)=\frac{p_h(x)}{p_h(0)}
=\prod_{i=1}^h\left(1-\frac{x}{\rho_i}\right).
\tag{4.1}
$$


The accepted original Gaussian-quadrature argument gives


$$
\rho_i\ge L_b,\qquad
L_b=\frac{b^2}{8004b+2}>1.
\tag{4.2}
$$


Its exact scope is important: the quadrature has


$$
N=h+\frac d2
$$


nodes, is exact through $2N-1$, and uses the strictly positive modified weights


$$
\omega_i(\lambda_i-1)^d.
$$


No stronger interlacing assertion or unpaid degree extension is used here.

### 4.1 Reciprocal Taylor coefficients

Define


$$
H_j=h_j(\rho_1^{-1},\ldots,\rho_h^{-1}),
$$


where $h_j$ is the complete homogeneous symmetric polynomial, and put


$$
A_d(x)=\sum_{j=0}^dH_jx^j.
\tag{4.3}
$$


Thus $H_0=1$, every $H_j>0$, and


$$
A_d(x)=\left[\frac1{P(x)}\right]_{\le d}.
\tag{4.4}
$$


The bracket means Taylor truncation at zero.

These coefficients are rational and can be generated directly from $P$, without finding its roots. If


$$
P(x)=1+\sum_{j=1}^hP_jx^j,
$$


then


$$
H_0=1,\qquad
H_m=-\sum_{j=1}^{\min(m,h)}P_jH_{m-j}.
\tag{4.5}
$$



Set


$$
\beta=\frac14,\qquad
K_d(x)=\sum_{k=0}^d
\frac{(-1)^k\binom nk}{(\beta)_{k+1}}x^k,
\tag{4.6}
$$


and define the second explicit degree-$d$ polynomial


$$
Q_d(x)=\bigl[K_d(x)A_d(x)\bigr]_{\le d}.
\tag{4.7}
$$


Equivalently,


$$
Q_d(x)=
\sum_{k=0}^d
\frac{(-1)^k\binom nk}{(\beta)_{k+1}}
x^k A_{d-k}(x).
\tag{4.8}
$$



The comparison kernel will be


$$
\boxed{\mathcal K_n(x)=\frac{Q_d(x)}{A_d(x)}.}
\tag{4.9}
$$


Its denominator is strictly positive for every $x>0$.

### 4.2 Why these are the actual $F$ and $R$ functionals

The established Laguerre kernel identity gives


$$
W(y)=\int_0^\infty e^{-x}r(x)L_n^{(0)}((1-y)x)\,dx.
$$


Integrating against $y^{\beta-1}$, the coefficient of $x^k$ in the integrated kernel is


$$
\frac{(-1)^k}{k!}\binom nk
\int_0^1y^{\beta-1}(1-y)^k\,dy
=
\frac{(-1)^k\binom nk}{(\beta)_{k+1}}.
$$


Orthogonality eliminates the terms $k=b,\ldots,n$, since $b=d+1$. Hence


$$
R=-\int_0^\infty e^{-x}r(x)K_d(x)\,dx.
\tag{4.10}
$$



Now put


$$
f_0(x)=x^{-b},\qquad f_\beta(x)=x^{-b}K_d(x).
$$


Interpolation at the $h$ zeros of $p_h$, followed by orthogonality, gives


$$
\int p_h(x)f(x)\,d\mu(x)
=
\int p_h(x)^2 f[\rho_1,\ldots,\rho_h,x]\,d\mu(x).
\tag{4.11}
$$


This applies to both displayed functions. At zero, their poles are canceled by the factor $x^b$ in $\mu$; at infinity, the exponential ensures integrability.

For positive arguments,


$$
(-1)^h
(t^{-m})[t_0,\ldots,t_h]
=
\left(\prod_{i=0}^ht_i^{-1}\right)
h_{m-1}(t_0^{-1},\ldots,t_h^{-1}).
\tag{4.12}
$$


This follows, for example, by expanding the divided difference of $1/(t+z)$ at $z=0$. It also remains valid at repeated arguments by continuity.

Applying (4.12), and separating the reciprocal variable $x^{-1}$, gives


$$
(-1)^hf_0[\rho_1,\ldots,\rho_h,x]
=
\frac{x^{-b}A_d(x)}{\prod_i\rho_i},
\tag{4.13}
$$


and


$$
(-1)^hf_\beta[\rho_1,\ldots,\rho_h,x]
=
\frac{x^{-b}Q_d(x)}{\prod_i\rho_i}.
\tag{4.14}
$$



Since $h$ is odd and


$$
|r_0|=a\prod_i\rho_i,
$$


equations (4.10)–(4.14) prove the exact identities


$$
\boxed{
\frac{|F|}{|r_0|}
=
\int_0^\infty
P(x)^2(x-1)^d e^{-x}A_d(x)\,dx,
}
\tag{4.15}
$$




$$
\boxed{
\frac{R}{|r_0|}
=
\int_0^\infty
P(x)^2(x-1)^d e^{-x}Q_d(x)\,dx.
}
\tag{4.16}
$$



These identities use the actual $r,F,R$. Dividing by $|r_0|$ is only an auxiliary analytic normalization; it does not rescale the integer form.

### 4.3 Positive probability measure, signed comparison kernel

Define


$$
d\mathbb P_n(x)=
\frac{|r_0|}{|F|}
P(x)^2(x-1)^d e^{-x}A_d(x)\,dx.
\tag{4.17}
$$


Equation (4.15) shows that this is a positive probability measure. Equation (4.16) becomes


$$
\boxed{
\frac{R}{|F|}
=\int_0^\infty\mathcal K_n(x)\,d\mathbb P_n(x).
}
\tag{4.18}
$$



This is a genuine positive-measure representation, but its kernel is not positive. The next section evaluates that failure on the original domain.

---

## 5. Explicit evaluation on the scale $x=c/n$

Define the entire function


$$
\Psi(c)=\sum_{k=0}^\infty
\frac{(-c)^k}{k!(5/4)_k}.
\tag{5.1}
$$


No special-function theorem is needed below; only this absolutely convergent series is used.

### Theorem 5.1 — Uniform signed-kernel approximation

For $0\le c\le4$, with the value at $c=0$ interpreted continuously,


$$
\boxed{
\left|
\frac{\mathcal K_n(c/n)}4-\Psi(c)
\right|
\le
\frac{324}{L_b}+\frac{648}{n}+2^{9-d},
}
\tag{5.2}
$$


provided $d\ge8$ and $4/n<L_b$.

#### Proof

Put $x=c/n$. From (4.8),


$$
\frac{\mathcal K_n(x)}4
=
\sum_{k=0}^d
\frac{(-c)^k}{k!(5/4)_k}
\left(\prod_{s=0}^{k-1}\left(1-\frac{s}{n}\right)\right)
\frac{A_{d-k}(x)}{A_d(x)}.
\tag{5.3}
$$



There are three differences from (5.1).

**First: the reciprocal-root factor.** Since $0\le x<\min\rho_i$,


$$
1\le A_d(x)\le\frac1{P(x)}.
$$


Also $A_{d-k}(x)\ge1$. Therefore


$$
0\le1-\frac{A_{d-k}(x)}{A_d(x)}
\le1-P(x)
\le x\sum_{i=1}^h\frac1{\rho_i}
\le\frac4{L_b}.
\tag{5.4}
$$


The product inequality used here is


$$
1-\prod_i(1-t_i)\le\sum_it_i,\qquad 0\le t_i\le1.
$$



Since


$$
\sum_{k=0}^\infty\frac{4^k}{k!(5/4)_k}
\le\sum_{k=0}^\infty\frac{4^k}{k!}
=e^4<81,
$$


the resulting error is at most $324/L_b$.

**Second: the falling-factorial factor.** For $k\le d<n$,


$$
0\le
1-\prod_{s=0}^{k-1}\left(1-\frac{s}{n}\right)
\le\frac{k(k-1)}{2n}.
$$


Thus its total contribution is at most


$$
\frac1{2n}
\sum_{k=0}^\infty\frac{4^kk(k-1)}{k!}
=
\frac{8e^4}{n}
<\frac{648}{n}.
\tag{5.5}
$$



**Third: the omitted tail.** For $k\ge8$,


$$
\frac{4^k}{k!}\le2^{9-k}.
$$


Indeed $4^8/8!<2$, and subsequent ratios are less than $1/2$. Consequently


$$
\sum_{k>d}\frac{4^k}{k!(5/4)_k}
\le\sum_{k>d}\frac{4^k}{k!}
\le2^{9-d}.
\tag{5.6}
$$



Combining the three estimates proves (5.2). ∎

This calculation retains, rather than discards, the alternating terms in the reciprocal convolution. Its evaluated limit is oscillatory.

---

## 6. A sign change at every original index

Every original index is far above $b=10^9$. In particular, with $b$ an integer power of $3$ and $u\equiv2\pmod{29^9}$, a nonnegative exponent requires $u\ge2$; already $u=2$ gives exponent $1397629859$.

For $b\ge10^9$,


$$
L_b\ge\frac b{8005},
$$


and hence


$$
\frac{324}{L_b}+\frac{648}{n}+2^{9-d}<\frac1{100}.
\tag{6.1}
$$



### 6.1 A positive value

At $c=1/16$, the alternating terms in (5.1) decrease in magnitude. Therefore


$$
\Psi(1/16)\ge1-\frac{1/16}{5/4}
=\frac{19}{20}.
$$


Equations (5.2) and (6.1) give


$$
\frac{\mathcal K_n(1/(16n))}{4}
>\frac{19}{20}-\frac1{100}
=\frac{47}{50}.
$$


Thus


$$
\boxed{
\mathcal K_n\!\left(\frac1{16n}\right)
>\frac{94}{25}>\frac{15}{4}.
}
\tag{6.2}
$$



### 6.2 A negative value

At $c=4$, the term magnitudes decrease from the first nonconstant term onward. The even partial sum through $k=4$ is therefore an upper bound:


$$
\begin{aligned}
\Psi(4)
&\le
1-\frac{16}{5}
+\frac{128}{45}
-\frac{2048}{1755}
+\frac{8192}{29835}\\
&=-\frac{7397}{29835}
<-\frac6{25}.
\end{aligned}
\tag{6.3}
$$


Consequently,


$$
\frac{\mathcal K_n(4/n)}4
<-\frac6{25}+\frac1{100}
=-\frac{23}{100},
$$


so


$$
\boxed{
\mathcal K_n\!\left(\frac4n\right)<-\frac{23}{25}.
}
\tag{6.4}
$$



Both points lie in $(0,1)$. On that interval:

* $P(x)\ne0$, because every $\rho_i>1$;
* $(x-1)^d>0$;
* $A_d(x)>0$.

Thus the density in (4.17) is strictly positive there. Continuity gives an interval of negative kernel values carrying positive $\mathbb P_n$-measure.

This proves the theorem announced in Section 1.

---

## 7. The precise failed implication

A tempting argument would be:

1. positive modified orthogonality produces a positive reciprocal-moment measure;
2. the beta-charge functional should dominate the factorial functional pointwise in that representation;
3. therefore $R/|F|\ge1/(Ch)$.

The first step is valid. The second is false in the actual original objects.

Indeed, any pointwise inequality


$$
\mathcal K_n(x)\ge\frac1{Ch}
$$


with $C>0$ fails at $x=4/n$. Even the weaker assertion


$$
\mathcal K_n(x)\ge0
$$


fails on a positive-measure interval.

Equivalently, with the exact divided differences from Section 4,


$$
(-1)^hf_\beta[\rho_1,\ldots,\rho_h,x]
$$


does not retain the positive sign of


$$
(-1)^hf_0[\rho_1,\ldots,\rho_h,x].
$$



This is not merely the previously known small-example sign change of $W$. It is a sign change of the **reciprocal-moment comparison kernel itself**, proved uniformly at all original indices.

It also does not contradict any accepted result:

* $R>0$ says that the signed average in (4.18) is positive.
* The whole-error theorem concerns the complete integrated exponential and arctangent channels.
* Neither assertion requires the kernel in (4.18) to be pointwise positive.

The uniform obstruction $|F|\le ChR$ may still be true. What is excluded is this particular pointwise-positive proof of it.

---

## 8. An evaluated bound for the small-$x$ contribution

The same representation gives a useful quantitative separation.

For $0\le x\le4/n$, equation (5.3) and the absolute series bound give


$$
|\mathcal K_n(x)|\le324.
\tag{8.1}
$$


Moreover,


$$
P(x)^2A_d(x)\le P(x)\le1,
$$


and


$$
e^{-x}(1-x)^d\le1.
$$


Hence


$$
\boxed{
\left|
\int_0^{4/n}
P(x)^2(x-1)^d e^{-x}Q_d(x)\,dx
\right|
\le\frac{1296}{n}.
}
\tag{8.2}
$$


In terms of the unchanged charges,


$$
\boxed{
\left|
|r_0|\int_0^{4/n}
P(x)^2(x-1)^d e^{-x}Q_d(x)\,dx
\right|
\le\frac{1296|r_0|}{n}.
}
\tag{8.3}
$$



Thus the newly detected negative contribution is not left as an unnamed oscillatory integral: its absolute contribution is explicitly bounded by an already available coefficient charge.

This estimate alone does not control the remaining integral, and no sign is assigned to that remainder.

---

## 9. A concrete follow-on lemma with a complete factorial evaluation

The failure above suggests separating the explicitly controlled small-$x$ region from the rest, rather than seeking pointwise positivity.

Define the rational polynomial


$$
Z_\beta(x)=P(x)^2(x-1)^dQ_d(x)
=\sum_{j=0}^{2n}z_jx^j,
\tag{9.1}
$$


padding with zero coefficients if its degree is smaller than $2n$. Define


$$
\mathcal T_\beta(t)=
\sum_{j=0}^{2n}z_jj!
\sum_{s=0}^j\frac{t^s}{s!}.
\tag{9.2}
$$


Repeated integration by parts gives the complete tail evaluation


$$
\boxed{
\int_t^\infty e^{-x}Z_\beta(x)\,dx
=e^{-t}\mathcal T_\beta(t).
}
\tag{9.3}
$$



All inputs are explicit:

1. $P=p_h/p_h(0)$, from the existing rational orthogonal-polynomial construction;
2. $A_d$, from recurrence (4.5);
3. $Q_d$, from the finite convolution (4.8);
4. the polynomial product (9.1);
5. factorials only through $(2n)!$.

No new physical matrix row, column, moment beyond the established boundary, or integer normalization is introduced.

### Proposed tail-comparison lemma

Prove that one fixed $C>0$ satisfies


$$
\boxed{
e^{-4/n}\mathcal T_\beta(4/n)
\ge
\frac{1296}{n}
+\frac{|F|}{C h|r_0|}
}
\tag{9.4}
$$


at all sufficiently large original indices.

This is a **stronger sufficient lemma**, not an assertion that it is necessary or already true.

Combining (9.4) with (8.2) and (4.16) would yield


$$
\frac R{|r_0|}
\ge\frac{|F|}{C h|r_0|},
$$


hence


$$
|F|\le ChR.
$$


The accepted $q\ge h$ would then give the actual ALL-prime comparison


$$
\frac gR=\frac{|F|}{qR}\le C,
$$


and therefore


$$
\boxed{q(e+\pi)-p>\frac1{2C}.}
$$


That would exclude vanishing primitive errors for this entire matrix family.

Unlike a generic appeal to a positive integrand, (9.4) specifies the exact signed tail, its complete endpoint evaluation, the required margin, and its factorial boundary. Its proof remains open.

---

## 10. The surviving progression and primes outside $h$

The supplied small-prime certificate establishes, through exact periodic congruences, that


$$
u=2+29^9(1+6068205v),\qquad v\ge0,
$$


avoids every prime divisor $\le97$ of $h$, subject to the original admissibility conditions. It does not control larger prime divisors or the final gcd.

The new signed-kernel theorem applies on this progression because it applies on the entire original domain. It does **not** give a new estimate for $g/R$ there.

In particular:

* $g$ remains $\gcd(|F|,|E+T|)$, over all primes;
* $q=|F|/g$ remains the actual primitive denominator;
* no prime outside $h$ is omitted;
* no common divisor is inferred from the auxiliary rational polynomials $P,A_d,Q_d$.

The possible contribution of primes outside $h$ would be handled by the final identity


$$
g/R=(|F|/R)/q
$$


if the analytic comparison were proved. At present that implication is conditional.

---

## 11. Source assessment and bounded verification

The earlier material is used at its stated scope.

* The finite matrix reduction, exact scalar charges, actual clearers and final gcd identities are reused.
* The whole-error sign theorem and its paid bounds are reused after checking their original hypotheses: even $d$, the exact quadrature degree, positive modified discrete weights, and zeros above $1$.
* The exact-content and $h$-supported denominator theorem are retained as assigned established results.
* The $(n,b)=(13,3)$ certificate is a finite normalization certificate only.
* The small-prime certificate proves its periodic exclusions, not primitive decay or an exhaustive covering.
* No conclusion about $e+\pi$ is imported from the unrelated determinant families or literature packets.

No new large computation is needed to verify the theorem proved here. Its numerical constants reduce to small exact inequalities.

An optional independently authored arithmetic check has the following bounded inputs and expected outputs:



$$
\beta=\frac14,\qquad c=4,\qquad 0\le k\le4,
$$


with


$$
a_k=\frac{4^k}{k!(5/4)_k}.
$$



Expected exact output:


$$
(a_0,a_1,a_2,a_3,a_4)
=
\left(
1,\frac{16}{5},\frac{128}{45},
\frac{2048}{1755},\frac{8192}{29835}
\right),
$$




$$
\sum_{k=0}^4(-1)^ka_k
=-\frac{7397}{29835}<-\frac6{25}.
$$


The same check may verify


$$
324\cdot8005=2593620
$$


and the rational bound, valid for $b\ge10^9$, $n=2001b$, $d=b-1$,


$$
\frac{2593620}{b}+\frac{648}{2001b}+2^{9-d}<\frac1{100}.
$$



These are transcription checks for the explicit estimates, not finite evidence for an unproved infinite $g/R$ law. There is no reason to repeat the closed content or small-prime calculations.

---

## 12. Conclusion and proof-status ledger

| Statement | Status |
|---|---|
| Original finite boundaries, complete $B_j$, actual contents and paid divisions retained | Established and reused |
| $R\in\mathbb Z_{>0}$, $\ell=1$, actual ALL-prime $g$, primitive $q$ | Established and unchanged |
| Whole error nonzero and $R/(2g)<q(e+\pi)-p<6005R/g$ | Established and reused |
| Exact reciprocal-moment representation $R/|F|=\int\mathcal K_n\,d\mathbb P_n$ | **New proved statement** |
| Uniform evaluated approximation of $\mathcal K_n(c/n)$ | **New proved statement** |
| Positive and negative kernel values at the same original indices | **New proved statement** |
| Pointwise positive reciprocal-kernel domination | **Disproved for the actual original objects** |
| Explicit small-$x$ contribution bound $1296|r_0|/n$ | **New proved statement** |
| Tail lemma (9.4) | Concrete open sufficient obligation |
| Uniform $|F|\le ChR$ | Open |
| Growth of $g/R$ on the surviving progression | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

The new result is not an irrationality theorem and not a universal impossibility theorem. It rules out a specific proposed analytic shortcut: **positive modified orthogonality does not make the exact reciprocal-moment comparison kernel positive, even on the original domain**.

The remaining mathematical bottleneck is now more precise. One must either:

1. control the **signed average** in (4.18), for example through the completely evaluated tail lemma (9.4), strongly enough to obtain $|F|\le ChR$; or
2. prove an actual ALL-prime growth theorem for $g/R$ on an infinite admissible original subsequence.

Until one of those obligations is resolved, this matrix supplies nonzero, fully paid integer linear forms, but no vanishing primitive-error sequence and no unconditional conclusion about $e+\pi$.
