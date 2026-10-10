> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A3 result: an exact growing-filter identity and a quantitative cancellation-stability gate

I do **not** obtain a proof or disproof of irrationality of $S=e+\pi$. The growing filters below are new rational combinations of the excluded centers; the exclusion of the individual centers does not automatically exclude these combinations.

The main results are:

1. an exact integral identity for their **whole evaluated errors**, with a rational series version and explicit truncation bounds, valid for every finite $m$, including $m=m(n)$;
2. an exact formula for their **fully reduced denominator**, retaining the final endpoint gcd;
3. a uniform beta-integral calculation showing what growing multiplicity does to an inverse-index correction, and precisely how accurate a uniform remainder estimate would have to be to make that calculation applicable to the actual centers.

The last calculation gives a genuine growing-$m$ analytic gate, but not a denominator-versus-error exclusion for the actual family.

---

## 1. The new centers and their exact primitive denominators

For index $k\ge2$, take the rational projective solution from the supplied $b=2$ projection formulas:


$$
R_k(z)=A_k(z)+B_k(z)e^z+C_k(z)F(z),
\qquad
F(z)=4\arctan\frac{z}{2-z},
$$


with


$$
\deg A_k,\deg C_k\le k,\quad \deg B_k\le2,\quad
R_k(z)=O(z^{2k+3}),\quad B_k(1)=C_k(1)=Y_k.
$$


Whenever $Y_k\ne0$, put


$$
r_k=-\frac{A_k(1)}{Y_k}=\frac{p_k}{q_k},
\qquad q_k>0,\qquad \gcd(p_k,q_k)=1.
$$


Thus


$$
E_k:=S-r_k=\frac{R_k(1)}{Y_k}.
$$



The supplied eventual normality and endpoint theorem provides a single $N_*$ such that these definitions apply to every $k\ge N_*$. No effective value of $N_*$ is claimed.

Write


$$
g(T)=T^2+6T+1,\qquad
g(T)^m=\sum_{j=0}^{2m}a_{m,j}T^j.
$$


The coefficients $a_{m,j}$ are positive integers and


$$
\sum_{j=0}^{2m}a_{m,j}=8^m.
$$


Reuse the supplied canonical filter


$$
W_m(T)=\frac{g(T)^m}{8^m}.
$$



For $n\ge N_*$ and every integer $m\ge1$, define


$$
\boxed{
c_{n,m}=\frac1{8^m}\sum_{j=0}^{2m}a_{m,j}r_{n+j}.
}
\tag{1}
$$


This is a combination of $2m+1$ different indices, not the original center at a single index. No assertion that accidental numerical coincidences between centers never occur is needed.

Set


$$
L_{n,m}=\operatorname{lcm}_{0\le j\le2m}q_{n+j},
\qquad
U_{n,m}=
\sum_{j=0}^{2m}a_{m,j}p_{n+j}\frac{L_{n,m}}{q_{n+j}},
$$


and


$$
G_{n,m}=\gcd\bigl(|U_{n,m}|,\,8^mL_{n,m}\bigr).
$$


Then the **actual reduced center and denominator** are


$$
\boxed{
c_{n,m}=\frac{P_{n,m}}{Q_{n,m}},\qquad
P_{n,m}=\frac{U_{n,m}}{G_{n,m}},\qquad
Q_{n,m}=\frac{8^mL_{n,m}}{G_{n,m}}>0.
}
\tag{2}
$$


In particular,


$$
\gcd(P_{n,m},Q_{n,m})=1.
$$



This includes $U_{n,m}=0$, when $Q_{n,m}=1$. The coefficient-denominator cost $8^m$, the lcm $L_{n,m}$, and the final gcd $G_{n,m}$ are three different objects. Neither $8^m$ nor the unfiltered prime divisors can simply be asserted to survive in $Q_{n,m}$.

The primitive integer form is exactly


$$
\boxed{
Q_{n,m}S-P_{n,m}
=Q_{n,m}\mathcal E_{n,m},\qquad
\mathcal E_{n,m}:=S-c_{n,m}
=\frac1{8^m}\sum_{j=0}^{2m}a_{m,j}E_{n+j}.
}
\tag{3}
$$



---

## 2. Exact complete integral identity, uniformly in growing multiplicity

The following representation avoids using a fixed-index asymptotic.

Write


$$
B_k(z)=\sum_{\ell=0}^2 b_{k,\ell}z^\ell,\qquad
C_k(z)=\sum_{\ell=0}^k d_{k,\ell}z^\ell,
\qquad K_k=2k+3.
$$


All these coefficients can be taken rational, for example using the supplied rational cross product and projection.

Let


$$
t(u)=\frac{1+iu}{2},\qquad -1\le u\le1,
$$


and define the rational moments


$$
\mu_h=\int_{-1}^1t(u)^h\,du
=\frac{(1+i)^{h+1}-(1-i)^{h+1}}
 {i\,2^h(h+1)}.
\tag{4}
$$


The moment expansion is


$$
F(z)=z\int_{-1}^1\frac{du}{1-t(u)z}
=\sum_{r\ge1}\mu_{r-1}z^r.
\tag{5}
$$


For example, its derivative is $2/(1-z+z^2/2)$, as is the derivative of the stated $F$, and both vanish at zero.

Because $A_k$ has degree below $K_k$ and the coefficients of $R_k$ below $K_k$ vanish,


$$
R_k(1)=
\sum_{\ell=0}^2 b_{k,\ell}
 \sum_{r=K_k}^{\infty}\frac1{(r-\ell)!}
+
\sum_{\ell=0}^k d_{k,\ell}
 \sum_{r=K_k}^{\infty}\mu_{r-\ell-1}.
\tag{6}
$$



For an integer $d\ge1$, Taylor's integral remainder gives


$$
\sum_{h=d}^{\infty}\frac1{h!}
=\frac1{(d-1)!}\int_0^1e^x(1-x)^{d-1}\,dx.
\tag{7}
$$


Also $|t(u)|\le2^{-1/2}<1$, so geometric summation in the second tail is absolutely justified. Consequently,


$$
\boxed{
\begin{aligned}
E_k={}&
\frac1{Y_k}\sum_{\ell=0}^2
 \frac{b_{k,\ell}}{(K_k-\ell-1)!}
 \int_0^1 e^x(1-x)^{K_k-\ell-1}\,dx\\
&+\frac1{Y_k}\int_{-1}^1
 \frac{\displaystyle\sum_{\ell=0}^k
       d_{k,\ell}t(u)^{K_k-\ell-1}}
      {1-t(u)}\,du.
\end{aligned}}
\tag{8}
$$


The second integral is real because the values at $u$ and $-u$ are conjugate.

Substituting (8) into (3) gives the promised complete filtered identity:


$$
\boxed{
\begin{aligned}
\mathcal E_{n,m}
={}&\frac1{8^m}
\sum_{j=0}^{2m}\frac{a_{m,j}}{Y_{n+j}}
\left[
\sum_{\ell=0}^2
 \frac{b_{n+j,\ell}}{(2(n+j)+2-\ell)!}
 \int_0^1e^x(1-x)^{2(n+j)+2-\ell}\,dx\right.\\
&\hspace{43mm}\left.
+\int_{-1}^1
 \frac{\displaystyle\sum_{\ell=0}^{n+j}
 d_{n+j,\ell}t(u)^{2(n+j)+2-\ell}}
 {1-t(u)}\,du
\right].
\end{aligned}}
\tag{9}
$$



This is an identity for every allowed $(n,m)$, without an asymptotic restriction on $m/n$. Both full tails, all coefficient signs, and each endpoint divisor $Y_{n+j}$ remain present. In particular, it does not silently replace the error by a logarithmic reference error.

### Why the filter cannot immediately be moved inside as $g(t)^m$

The summands in (9) involve different $Y_k$, different $B_k,C_k$, and different factorial kernels. Thus (9) does **not** simplify merely by replacing a geometric factor with $g(t)^m$.

That simplification would require a common index-moment representation for the normalized sequence $E_k$. No such representation for the complete $b=2$ errors is proved by the supplied fixed-$b$ asymptotics.

---

## 3. Rational series truncation and a rigorous nonvanishing test

The exact representation also supplies a bounded certification procedure for any specified pair $(n,m)$, without evaluating $e$ or $\pi$ numerically.

For $H\ge K_k$, define the rational truncation


$$
T_{k,H}=
\frac1{Y_k}\left[
\sum_{\ell=0}^2 b_{k,\ell}
 \sum_{r=K_k}^{H}\frac1{(r-\ell)!}
+
\sum_{\ell=0}^k d_{k,\ell}
 \sum_{r=K_k}^{H}\mu_{r-\ell-1}
\right].
\tag{10}
$$


Since


$$
|\mu_h|\le2\,2^{-h/2},
$$


and


$$
\sum_{r=H+1}^{\infty}\frac1{(r-\ell)!}
\le
\frac{H+2-\ell}{H+1-\ell}\frac1{(H+1-\ell)!},
$$


we obtain


$$
|E_k-T_{k,H}|\le D_{k,H},
\tag{11}
$$


where


$$
\begin{aligned}
D_{k,H}:=\frac1{|Y_k|}\bigg[
&\sum_{\ell=0}^2 |b_{k,\ell}|
 \frac{H+2-\ell}{H+1-\ell}
 \frac1{(H+1-\ell)!}\\
&+\frac2{1-2^{-1/2}}
 \sum_{\ell=0}^k|d_{k,\ell}|\,2^{-(H-\ell)/2}
\bigg].
\end{aligned}
\tag{12}
$$


The displayed bound belongs to $\mathbb Q(\sqrt2)$, so comparisons can be certified exactly.

For arbitrarily chosen $H_j\ge K_{n+j}$, put


$$
\mathcal T_{n,m}=\frac1{8^m}
 \sum_{j=0}^{2m}a_{m,j}T_{n+j,H_j},\qquad
\mathcal D_{n,m}=\frac1{8^m}
 \sum_{j=0}^{2m}a_{m,j}D_{n+j,H_j}.
$$


Then


$$
\boxed{
|\mathcal E_{n,m}-\mathcal T_{n,m}|
\le\mathcal D_{n,m}.
}
\tag{13}
$$


In particular,


$$
|\mathcal T_{n,m}|>\mathcal D_{n,m}
\quad\Longrightarrow\quad
\mathcal E_{n,m}\ne0,
\tag{14}
$$


with the sign determined by $\mathcal T_{n,m}$.

This is a proved nonvanishing **criterion**, not an assertion that it holds throughout an infinite growing-$m$ range. Eventual nonvanishing of the separate $E_k$ does not imply nonvanishing of their filtered sum.

---

## 4. New growing-multiplicity lemma: the exact inverse-index response

A tractable follow-on is to determine the filter response to the first possible inverse-index correction **without** expanding shifts in powers of $j/n$.

Set


$$
s=3-2\sqrt2,\qquad z=-s,\qquad a=s^2.
$$


Thus $0<s<1$, $g(z)=0$, and


$$
6s=1+s^2.
$$


Consequently


$$
g(zx)=1-6sx+s^2x^2=(1-x)(1-a x).
\tag{15}
$$



Define


$$
I_{n,m}:=
\frac1{8^m}\sum_{j=0}^{2m}\frac{a_{m,j}z^j}{n+j},
\qquad n\ge1,\quad m\ge1.
$$


Using $1/(n+j)=\int_0^1x^{n+j-1}dx$ gives the exact identity


$$
\boxed{
I_{n,m}
=\frac1{8^m}\int_0^1x^{n-1}(1-x)^m(1-a x)^m\,dx>0.
}
\tag{16}
$$



This proves nonvanishing and sign of this model contribution for **every** $n,m$, including proportional and superproportional multiplicity.

### 4.1 Explicit bounds valid for all $n,m$

Since $1-a\le1-a x\le1$,


$$
\boxed{
\left(\frac{1-a}{8}\right)^m B(n,m+1)
\le I_{n,m}\le
8^{-m}B(n,m+1),
}
\tag{17}
$$


where, exactly,


$$
B(n,m+1)=\frac{(n-1)!\,m!}{(n+m)!}.
\tag{18}
$$


Thus the factorial $m!$ and the rising denominator


$$
n(n+1)\cdots(n+m)
$$


are retained, rather than replaced by $n^{m+1}$.

### 4.2 A growing sublinear window

For $m=o(n)$,


$$
\log B(n,m+1)
=\log(m!)-(m+1)\log n
+O\!\left(\frac{m(m+1)}n\right),
\tag{19}
$$


because


$$
B(n,m+1)=m!n^{-(m+1)}
 \prod_{h=0}^{m}(1+h/n)^{-1}
$$


and $0\le\log(1+h/n)\le h/n$.

In particular, if $m\to\infty$ and $m=o(n)$, (17) and Stirling's formula yield


$$
\boxed{
\log I_{n,m}
=-m\log(n/m)-\log n+O\!\left(m+\frac{m^2}{n}\right).
}
\tag{20}
$$


Hence


$$
\frac1n\log I_{n,m}\longrightarrow0.
\tag{21}
$$



**Proved model conclusion.** If the filtered actual error were dominated by a nonzero $z^k/k$ correction, then every sublinear window $m=o(n)$ would still have exponential rate $\log s$, even though its subexponential improvement can be substantial.

This does not assume or prove such domination for the actual $b=2$ errors.

### 4.3 Proportional multiplicity: a different exponential rate

Suppose $m/n\to\alpha>0$. Applying the elementary Laplace principle to the positive integral (16) gives


$$
\boxed{
\lim_{n\to\infty}\frac1n\log I_{n,m}
=
-\alpha\log8+
\max_{0<x<1}
\left\{
\log x+\alpha\log(1-x)+\alpha\log(1-a x)
\right\}.
}
\tag{22}
$$


The maximizer $x_\alpha$ is unique. Indeed the expression is strictly concave, tends to $-\infty$ at both endpoints, and its derivative vanishes precisely when


$$
\frac1x-\frac{\alpha}{1-x}-\frac{\alpha a}{1-a x}=0.
$$


Equivalently,


$$
\boxed{
1-(1+\alpha)(1+a)x+a(1+2\alpha)x^2=0,
}
\tag{23}
$$


with $x_\alpha$ the root in $(0,1)$.

For completeness, (22) follows by restricting the integral to a fixed small interval around $x_\alpha$ for the lower bound, and splitting off small endpoint intervals for the upper bound; on compact subintervals the exponents converge uniformly. The factors vanishing at the endpoints make those endpoint pieces exponentially negligible after choosing them sufficiently small.

Thus proportional multiplicity can change the model exponential rate. Formula (22), rather than the fixed-$m$ asymptotic, is the appropriate benchmark for that range.

---

## 5. Exact stability requirement for applying this lemma to the actual errors

The difficulty is not the beta integral itself. It is controlling everything left over in the **whole** normalized error.

For any fixed constants $C\ne0$ and $A$, define the exact residual


$$
\eta_k=\frac{E_k}{Cz^k}-1-\frac{A}{k}.
\tag{24}
$$


This is a definition, not an assumed asymptotic expansion. Since $W_m(z)=0$,


$$
\boxed{
\mathcal E_{n,m}
=Cz^n\left[
A I_{n,m}
+
\frac1{8^m}\sum_{j=0}^{2m}
 a_{m,j}z^j\eta_{n+j}
\right].
}
\tag{25}
$$


All actual exponential and logarithmic contributions not represented by the two model terms are contained in $\eta_k$.

Let


$$
M_{n,m}=\max_{0\le j\le2m}|\eta_{n+j}|.
$$


Because the $a_{m,j}$ are positive,


$$
\left|
\frac1{8^m}\sum_{j=0}^{2m}a_{m,j}z^j\eta_{n+j}
\right|
\le M_{n,m}W_m(s).
$$


Using $1+s^2=6s$,


$$
W_m(s)=
\left(\frac{1+6s+s^2}{8}\right)^m
=\left(\frac{3s}{2}\right)^m.
$$


Therefore


$$
\boxed{
\left|\frac{\mathcal E_{n,m}}{Cz^n}
-AI_{n,m}\right|
\le M_{n,m}\left(\frac{3s}{2}\right)^m.
}
\tag{26}
$$



If $A\ne0$, the explicit sufficient condition


$$
M_{n,m}\left(\frac{3s}{2}\right)^m
\le\theta |A|I_{n,m},
\qquad 0\le\theta<1,
\tag{27}
$$


would imply


$$
(1-\theta)|CA|s^nI_{n,m}
\le|\mathcal E_{n,m}|
\le(1+\theta)|CA|s^nI_{n,m},
\tag{28}
$$


and the exact sign


$$
\operatorname{sign}\mathcal E_{n,m}
=\operatorname{sign}(CA)(-1)^n.
\tag{29}
$$



This isolates a quantitative obstacle that is hidden by a fixed-$m$ expansion. In particular, merely knowing $\eta_k=O(k^{-r})$ for a fixed $r$ does not make (27) effective for growing $m$. The beta-integral signal becomes much smaller than the corresponding absolute residual bound.

The bound (26) is also sharp as a bound based solely on $M_{n,m}$: choosing residual signs proportional to $(-1)^j$ makes all the summands $z^j\eta_{n+j}$ have the same sign. Thus improvement requires genuine structure of the residual sequence, not simply a better presentation of the triangle inequality.

---

## 6. The exact joint arithmetic–analytic gate

If (27) were proved in a specified growing window, (2) and (28) would give


$$
\boxed{
\begin{aligned}
\log\bigl(Q_{n,m}|\mathcal E_{n,m}|\bigr)
={}&m\log8+\log L_{n,m}-\log G_{n,m}\\
&+n\log s+\log I_{n,m}+\log|CA|+O_\theta(1).
\end{aligned}}
\tag{30}
$$


This is the appropriate joint cost expression. It contains:

- the actual final gcd $G_{n,m}$;
- the lcm of the already reduced individual denominators;
- the coefficient cost $8^m$;
- the whole filtered error, subject to the explicitly stated stability hypothesis;
- a nonvanishing conclusion supplied by that same hypothesis.

For $m=o(n)$, the model analytic rate is unchanged by (21). For $m/n\to\alpha>0$, the analytic contribution must instead be evaluated using (22).

However, the supplied prime-depth theorems for the individual $q_k$ do not bound $G_{n,m}$. Cancellation among several indices can remove common prime powers. Consequently, even establishing (27) would not yet prove either shrinking or divergence of the primitive forms.

---

## 7. Status and handoff

### (1) New result and proof status

**Proved here, author-level:**

- Exact definition (1) and primitive reduction (2) for the growing-multiplicity filtered centers.
- Complete exponential/logarithmic integral identity (9), valid for all $n\ge N_*$, $m\ge1$.
- Rational truncation enclosure (13) and rigorous nonvanishing criterion (14).
- Positive beta-integral identity (16), all-parameter bounds (17), sublinear-window estimate (20), and proportional-window rate (22).
- Exact residual stability inequality (26), including a sufficient whole-error nonvanishing condition (27).

**Not proved:** an infinite growing-$m$ nonvanishing theorem for the actual errors, a primitive-error exclusion for these filters, or irrationality of $e+\pi$.

### (2) Exact remaining bottleneck

There are two independent missing estimates:

1. **Analytic:** a structured uniform estimate for the exact residual in (25), strong enough relative to $I_{n,m}$. A fixed-order asymptotic, or the known fixed-$b$ error rate, does not suffice.
2. **Arithmetic:** a lower bound on
   

$$
Q_{n,m}=\frac{8^mL_{n,m}}{G_{n,m}}
$$


   after cancellation among all indices. The individual-center exclusions do not supply it.

A useful next lemma would be a common signed-moment representation for the actual normalized sequence $E_k$, with a controlled remainder. Such a representation could allow the filter to act on the index variable exactly, as it does in (16), rather than through unstable fixed-order expansions.

### (3) Computation request

**None.** The identities above have direct symbolic proofs, and a finite scan would not decide either missing infinite estimate. For a later, specifically chosen pair $(n,m)$, formulas (10)–(14) give an exact bounded nonvanishing certificate protocol, but no pair is requested here merely for exploratory sampling.
