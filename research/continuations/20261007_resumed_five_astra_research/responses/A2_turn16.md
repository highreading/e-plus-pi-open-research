> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 Turn 16: factorial-content rigidity and a new obstruction in the actual primitive denominator

## 1. Main conclusions and scope

The global objective remains unresolved: **this report proves neither rationality nor irrationality of $e+\pi$**.

There is, however, a new arithmetic restriction on the actual primitive pair of the supplied Laguerre family. It uses the primitive content of $r$, its repeated factor $(x-1)^d$, the factorial finite-difference expansion, and the **complete** charge $E+T$.

Retain


$$
b=3^{249005515+574312172u},\qquad n=2001b,\qquad
d=b-1,\qquad h=n-d=2000b+1,
$$


with the original admissibility conditions on $u$, including


$$
u\equiv2\pmod{29^9}.
$$



The principal new statements are:

> **Theorem A — Exact factorial content.**  
> For the actual primitive integer polynomial $r$ and its supplied Laguerre expansion coefficients,
> 

$$
> \boxed{\gcd(\gamma_0,\ldots,\gamma_d)=h!.}
>
$$


> Thus the known divisibility by $h!$ is exact. An additional common factor cannot be extracted from the $\gamma_j$ without violating the actual primitive content of $r$.

> **Theorem B — Exact final-gcd valuations at every prime dividing $h$.**  
> For every prime $p\mid h$,
> 

$$
> \boxed{
> p\nmid a,\qquad
> v_p(E)=v_p(d!),\qquad
> v_p(g)=v_p(d!),
> }
>
$$


> where
> 

$$
> g=\gcd(|F|,|E+T|).
>
$$


> In particular, if
> 

$$
> \mathcal D_h
> =\prod_{p\mid h}p^{\,v_p(h!)-v_p(d!)},
>
$$


> then
> 

$$
> \boxed{\mathcal D_h\mid q=\frac{|F|}{g}.}
>
$$


> Since $h\mid\mathcal D_h$, this proves the especially simple restriction
> 

$$
> \boxed{h\mid q.}
>
$$



Theorem B is a statement about the **actual final gcd**, not merely a lower divisor of $F$ or $T$.

A further explicit estimate gives a genuine comparison with the positive beta charge:

> **Theorem C — An all-prime upper bound for $g/R$.**  
> At every original index,
> 

$$
> \boxed{
> \frac{g}{R}
> <
> \frac{(2n+1)3^{18d}}{\mathcal D_h}.
> }
> \tag{1.1}
>
$$


> The primes not dividing $h$ remain present in the actual gcd. They are not discarded: their possible contribution is included through the inequality $g=|F|/q$.

This bound is strong enough to prove a concrete obstruction whenever $h$ has a small prime divisor. For example, at every original index satisfying $19\mid h$,


$$
\boxed{
\frac{g}{R}
<
\frac{(4002b+1)3^{18(b-1)}}{19^{100b}}
\longrightarrow0.
}
\tag{1.2}
$$


Consequently $R/g$, and hence the actual positive primitive error, diverges along any unbounded collection of those original indices.

The condition $19\mid h$ is explicitly evaluated below:


$$
19\mid h\quad\Longleftrightarrow\quad u\equiv2\pmod9.
\tag{1.3}
$$


Its intersection with the displayed original congruence class is


$$
u\equiv2\pmod{9\cdot29^9}.
$$


All conclusions retain the original allowed-domain condition on $u$; no unspecified further admissibility restriction is silently removed.

These results do **not** exclude a successful subsequence among the complementary original indices. They do substantially sharpen the next obstruction lemma: because $h\mid q$, it would now suffice to prove


$$
\boxed{|F|\le C hR}
\tag{1.4}
$$


for a fixed constant $C$. This is weaker by an unbounded factor than the previously proposed bound $|F|\le CR$.

---

## 2. Original objects, complete sources, and arithmetic payments

### 2.1 Finite matrix and endpoints

The matrix remains exactly


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



Its row window is


$$
n,n+1,\ldots,n+d,
$$


and its column window is $0,\ldots,d$. No additional physical row or column is introduced.

In particular, every $B_j$ is retained. The arctangent correction is not replaced by its limiting value $\pi$, by its leading term, or by a truncated subset of its rational summands.

Write


$$
R_{rj}=A_{n+r,j}+B_j,\qquad
\mathsf W_{rj}=(n+r)!R_{rj},
$$


and retain


$$
\kappa_r=\gcd\bigl((n+r)!,\mathsf W_{r0},\ldots,\mathsf W_{rd}\bigr),
\qquad
C_r=\frac{(n+r)!}{\kappa_r},
$$




$$
Y_{rj}=C_rR_{rj},\qquad
c_j=\gcd_{0\le r\le d}(C_r,Y_{rj}),
$$




$$
\mathcal L_n=\operatorname{lcm}_{0\le r\le d}C_r,\qquad
P_n=\frac{\prod_{r=0}^d C_r}{\prod_{j=0}^d c_j}.
$$


Thus the paid determinant is


$$
D_n(X)
=\det\left[\frac{C_rX-Y_{rj}}{c_j}\right]_{r,j=0}^d
=P_n\det H(X)=U_nX-V_n.
$$



The established finite-difference reduction uses the complete factor


$$
K_n
=
\frac{\prod_{r=0}^d(n+r)!}
     {\prod_{j=0}^d j!(n-j)!}.
$$


Its scalar identity is


$$
D_n(X)
=
\frac{P_n\tau_n}{aK_n}\bigl(FX-E-T\bigr),
\tag{2.1}
$$


after the now-proved original-domain simplification $\ell=1$. None of the divisions in (2.1) is treated as free.

The earlier corrected producer with its separate forcing, returns, and physical terminal is not identified with this matrix. Its complete formulas are absent from this packet, so no arithmetic gain is transferred to it.

### 2.2 The actual polynomial and scalar charges

Let $p_h$ be the monic orthogonal polynomial for


$$
x^b(x-1)^d e^{-x}\,dx,\qquad x>0.
$$


Since $d$ is even, this measure is positive apart from isolated zeros and has infinite support.

Let $a>0$ be its actual least coefficient clearer. Then


$$
r(x)=a(x-1)^dp_h(x)=\sum_{k=0}^n r_kx^k
$$


is a primitive integer polynomial of degree $n$, with $r_n=a$.

The integer charges are


$$
F=\sum_{k=0}^n r_kk!,
\qquad
E=\sum_{k=0}^n r_k\sum_{v=0}^k\frac{k!}{v!}.
\tag{2.2}
$$


They satisfy


$$
F=\int_0^\infty e^{-x}r(x)\,dx<0,
\qquad
E=e\int_1^\infty e^{-x}r(x)\,dx.
$$



Put


$$
g_j(x)=L_{n-j}^{(j+1)}(x),\qquad
r(x)=\sum_{j=0}^d\gamma_jg_j(x),
$$


with the exact recurrence


$$
\gamma_j
=(-1)^{n-j}(n-j)!\,r_{n-j}
-\sum_{i<j}\binom{n+1}{j-i}\gamma_i.
\tag{2.3}
$$


Then


$$
w_j=\binom nj\gamma_j,\qquad
F=\sum_{j=0}^d w_j,
$$


and the complete arctangent charge is


$$
T=\sum_{j=0}^d w_jB_j.
\tag{2.4}
$$



The parent’s clearer argument applies because


$$
h\ge4d+1.
$$


It proves


$$
T\in\mathbb Z,\qquad \ell=1.
$$



The positive beta charge is


$$
R=\sum_{k=0}^n |r_k|c_{n,k},
\qquad
c_{n,k}=\frac{k!(3/4)_k}{(n-k+1/4)_{k+1}},
\tag{2.5}
$$


and its exact short form is


$$
R=4(-1)^n\sum_{j=0}^d\frac{w_j}{4j+1}>0.
\tag{2.6}
$$


It is an integer on the original domain.

The actual primitive pair is therefore


$$
q=-\frac Fg>0,\qquad
p=-\frac{E+T}{g},
\qquad
g=\gcd(|F|,|E+T|).
\tag{2.7}
$$


The paid determinant’s final gcd remains


$$
G_n=\gcd(U_n,|V_n|)=U_n\frac{g}{|F|}.
\tag{2.8}
$$



All subsequent arguments concern this $g$ and this $q$.

---

## 3. Review of the whole-error theorem at its actual scope

The supplied turn-14 proof survives the following checks needed here.

1. **Coefficient signs.**  
   All roots of $p_h$ are positive, and the other roots of $r$ are the $d$ copies of $1$. Hence
   

$$
(-1)^{n-k}r_k>0.
$$



2. **The actual integrated arctangent kernel.**  
   The identity
   

$$
\mathcal W_{n,k}(y)
   =\frac{d^k}{dy^k}\bigl[y^n(y-1)^k\bigr]
$$


   is obtained directly from the finite Laguerre expansion. For
   

$$
v(y)=\frac{y^{-3/4}}{1+\sqrt y},
$$


   the supplied derivative bounds
   

$$
\frac12(3/4)_ky^{-k-3/4}
   \le(-1)^kv^{(k)}(y)
   \le(3/4)_ky^{-k-3/4}
$$


   apply on $0<y\le1$. At zero, every integration-by-parts boundary term has order
   

$$
O(y^{n-k+1/4}),
$$


   which vanishes for $k\le n$. At one, the repeated factor supplies the required vanishing. Thus the sign conclusion concerns the **complete integrated arctangent channel**, not pointwise positivity of $W$.

3. **Zeros above $1$.**  
   The auxiliary Gaussian quadrature has
   

$$
N=h+d/2,
$$


   is exact through degree $2N-1$, and represents all modified orthogonality equations because
   

$$
d+2h-1=2N-1.
$$


   The Jacobi-matrix estimate gives the lower node bound
   

$$
\frac{b^2}{8004b+2}>1
$$


   on the original domain. The modified quadrature weights are therefore strictly positive, so the zeros of $p_h$ also exceed $1$.

Consequently the complete error


$$
M
=
F(e+\pi)-E-T
=
e\int_0^1 e^{-x}r(x)\,dx
+
4\int_0^1\frac{W(s^4)}{1+s^2}\,ds
\tag{3.1}
$$


is strictly negative at every original index. Both integrals are present and have the same sign.

The resulting paid comparison is


$$
\boxed{
\frac{R}{2g}
<
q(e+\pi)-p
<
6005\frac Rg.
}
\tag{3.2}
$$



The new arithmetic below does not require the sign theorem until it is translated into a statement about the whole error.

---

## 4. Exact factorial content of the Laguerre coefficients

### 4.1 Two equivalent contents

The finite Laguerre formula gives


$$
[x^k]g_j(x)
=
\frac{(-1)^k}{k!}
\binom{n+1}{n-j-k},
$$


with the binomial coefficient interpreted as zero outside its range. Hence


$$
(-1)^k k!r_k
=
\sum_{j=0}^d
\binom{n+1}{n-j-k}\gamma_j.
\tag{4.1}
$$



Define


$$
\Gamma=\gcd(\gamma_0,\ldots,\gamma_d).
$$


Equation (4.1) shows


$$
\Gamma\mid k!r_k\qquad(0\le k\le n).
$$


Conversely, the triangular recurrence (2.3) recovers every $\gamma_j$ by integer operations from the top factorial coefficients. Therefore


$$
\boxed{
\Gamma=\gcd_{0\le k\le n}(k!r_k).
}
\tag{4.2}
$$



The already-established induction in (2.3) gives


$$
h!\mid\Gamma.
\tag{4.3}
$$



### 4.2 Primitivity and the repeated root give the reverse divisibility

Suppose, for some prime $p$,


$$
v_p(\Gamma)>v_p(h!).
$$


For $0\le k\le h$, one has $v_p(k!)\le v_p(h!)$. Since $\Gamma\mid k!r_k$, it follows that


$$
p\mid r_k\qquad(0\le k\le h).
$$


Thus the reduction $\bar r\in\mathbb F_p[x]$ is divisible by $x^{h+1}$.

It is also divisible by $(x-1)^d$, because $r$ has this factor over $\mathbb Z[x]$. These two factors are coprime over $\mathbb F_p$, so a nonzero $\bar r$ would have degree at least


$$
h+1+d=n+1.
$$


But $\deg r=n$.

The alternative $\bar r=0$ is impossible because $r$ is primitive. This contradiction proves


$$
v_p(\Gamma)\le v_p(h!)
$$


for every prime $p$. Combining with (4.3),


$$
\boxed{\Gamma=h!.}
\tag{4.4}
$$



This proof uses the **actual content** of $r$. Replacing $r$ by an arbitrary integer multiple would destroy the conclusion.

---

## 5. Exact arithmetic at primes dividing $h$

Fix a prime $p\mid h$.

### 5.1 A rigid reduction of $r$ modulo $p$

For every $k<h$,


$$
v_p(k!)<v_p(h!),
$$


because the final factor $h$ contributes at least one additional $p$. Since $h!\mid k!r_k$,


$$
p\mid r_k\qquad(k<h).
$$


Therefore $\bar r$ is divisible by $x^h$.

As before, $(x-1)^d\mid\bar r$. Their product has degree exactly $n$, and $\bar r\ne0$. Consequently


$$
\boxed{
r(x)\equiv a\,x^h(x-1)^d\pmod p,
\qquad p\nmid a.
}
\tag{5.1}
$$


In particular,


$$
\boxed{\gcd(a,h)=1.}
\tag{5.2}
$$



### 5.2 Evaluation of the exponential endpoint modulo $p$

Write


$$
r(1+z)=z^dS(z),\qquad
S(z)=\sum_{j=0}^h s_jz^j\in\mathbb Z[z].
$$


The complete exponential endpoint is


$$
E=\sum_{j=0}^h(d+j)!s_j,
$$


so


$$
\frac E{d!}
=
\sum_{j=0}^h\frac{(d+j)!}{d!}\,s_j
\in\mathbb Z.
\tag{5.3}
$$



From (5.1),


$$
S(z)\equiv a(1+z)^h\pmod p.
$$


Because $p\mid h$,


$$
(1+z)^h\equiv(1+z^p)^{h/p}\pmod p.
$$


Thus


$$
s_0\equiv a\pmod p,\qquad
s_j\equiv0\pmod p\quad(1\le j<p).
$$



For $j\ge p$, the product


$$
\frac{(d+j)!}{d!}=(d+1)(d+2)\cdots(d+j)
$$


is divisible by $p$. Reducing (5.3) modulo $p$ therefore gives the evaluated congruence


$$
\boxed{
\frac E{d!}\equiv a\not\equiv0\pmod p.
}
\tag{5.4}
$$


Hence


$$
\boxed{v_p(E)=v_p(d!).}
\tag{5.5}
$$



This is substantially stronger than the previously known lower divisibility $d!\mid E$.

### 5.3 The complete arctangent correction cannot cancel this valuation

Let


$$
\Lambda_B=\operatorname{lcm}(1,3,5,\ldots,4d-1).
$$


The complete charge satisfies


$$
\frac{h!}{\Lambda_B}\mid T.
\tag{5.6}
$$



We claim that, for every $p\mid h$,


$$
v_p(h!)-v_p(\Lambda_B)>v_p(d!).
\tag{5.7}
$$



If $L=v_p(\Lambda_B)=0$, the factor $h$ in $h!/d!$ already gives a positive $p$-valuation.

If $L>0$, then $p^L\le4d-1$. There are two consecutive multiples of $p^L$ strictly larger than $d$, both at most


$$
d+2p^L\le9d-2<h.
$$


They contribute at least $2L>L$ to $v_p(h!/d!)$. This proves (5.7).

Thus


$$
v_p(T)>v_p(d!)=v_p(E),
$$


and no cancellation between $E$ and the **complete** $T$ is possible at this valuation:


$$
v_p(E+T)=v_p(d!).
\tag{5.8}
$$



Since $h!\mid F$,


$$
\boxed{
v_p(g)
=
\min\{v_p(F),v_p(E+T)\}
=
v_p(d!)
\qquad(p\mid h).
}
\tag{5.9}
$$



The same argument with


$$
\Lambda_R=\operatorname{lcm}(1,5,\ldots,4d+1)
$$


shows


$$
v_p(R)>v_p(d!)=v_p(g)\qquad(p\mid h).
\tag{5.10}
$$


This does not alone control the real number $R/g$, because other primes may occur in its denominator. The next steps supply a real-valued comparison.

---

## 6. A forced divisor of the actual primitive denominator

Define


$$
\mathcal D_h
=
\prod_{p\mid h}p^{\,v_p(h!)-v_p(d!)}.
\tag{6.1}
$$


For $p\mid h$, (5.9) gives


$$
v_p(q)=v_p(F)-v_p(d!)
\ge v_p(h!)-v_p(d!).
$$


Therefore


$$
\boxed{\mathcal D_h\mid q.}
\tag{6.2}
$$



Moreover $h$ is one of the factors of $h!/d!$, so


$$
v_p(h!)-v_p(d!)\ge v_p(h)
\qquad(p\mid h).
$$


Thus


$$
\boxed{h\mid\mathcal D_h\mid q.}
\tag{6.3}
$$



This is an unconditional restriction on the actual primitive denominator at every original index.

It is important not to overstate it:

* it does not evaluate $v_p(g)$ for primes $p\nmid h$;
* it does not replace the final gcd by a restricted-prime gcd;
* it does imply the all-prime inequality
  

$$
\boxed{g\le\frac{|F|}{\mathcal D_h}.}
  \tag{6.4}
$$



The last inequality remains valid however large the gcd contributions at other primes may be.

---

## 7. An explicit bound for $|F|/R$

A uniform constant bound is not proved here. The following weaker but fully evaluated bound is enough to exploit fixed small prime divisors of $h$.

Set


$$
N=n+d.
$$



### 7.1 Inverting the factorial recurrence

The recurrence (2.3) is convolution by the coefficients of $(1+z)^{n+1}$. Its inverse gives


$$
\gamma_j
=
\sum_{i=0}^j
(-1)^{j-i}\binom{n+j-i}{j-i}
(-1)^{n-i}(n-i)!\,r_{n-i}.
\tag{7.1}
$$


Using $F=\sum_j\binom nj\gamma_j$,


$$
|F|
\le
\sum_{i=0}^d |r_{n-i}|(n-i)!S_i,
\tag{7.2}
$$


where


$$
S_i
=
\sum_{j=i}^d
\binom nj\binom{n+j-i}{j-i}.
$$



This sum will now be bounded explicitly; it is not left as a new unevaluated charge.

Since


$$
\binom nj\binom{n+j-i}{j-i}
\le
\frac{N^{2j-i}}{j!(j-i)!},
$$


and the ratio of a preceding term to the next is at most $d^2/N^2<1/4$,


$$
\boxed{
S_i<
\frac{2N^{2d-i}}{d!(d-i)!}.
}
\tag{7.3}
$$



### 7.2 Comparing the top coefficients with their beta weights

Put


$$
D_i=\frac{(n-i)!}{c_{n,n-i}}
=
\frac{(i+1/4)_{n-i+1}}{(3/4)_{n-i}}.
$$


First,


$$
D_0
=
\frac{(1/4)_{n+1}}{(3/4)_n}
\le n+\frac14.
$$


For $i\ge1$,


$$
\frac{D_i}{D_{i-1}}
=
\frac{n-i+3/4}{i-3/4}
\le
\frac{4(n-i+1)}i.
$$


Induction yields


$$
\boxed{
D_i\le\left(n+\frac14\right)4^i\binom ni.
}
\tag{7.4}
$$



Because


$$
R\ge\sum_{i=0}^d|r_{n-i}|c_{n,n-i},
$$


equations (7.2)–(7.4) imply


$$
\frac{|F|}{R}\le\max_{0\le i\le d}D_iS_i.
$$


Using $\binom ni\le N^i/i!$,


$$
D_iS_i
<
2\left(n+\frac14\right)
\frac{N^{2d}}{(d!)^2}
4^i\binom di.
$$


Finally,


$$
4^i\binom di\le\sum_{i=0}^d4^i\binom di=5^d.
$$


Therefore


$$
\boxed{
\frac{|F|}{R}
<
2\left(n+\frac14\right)
5^d\frac{(n+d)^{2d}}{(d!)^2}.
}
\tag{7.5}
$$



### 7.3 Specialization to the original ratio $n=2001b$

Using $d!\ge(d/e)^d$, $e<3$, and


$$
\frac{n+d}{d}
=
2002+\frac{2001}{b-1}
\le2003
$$


on the original domain, (7.5) gives


$$
\frac{|F|}{R}
<
(2n+1)\bigl(45\cdot2003^2\bigr)^d.
$$


The exact numerical comparison


$$
45\cdot2003^2=180540405<387420489=3^{18}
$$


therefore proves


$$
\boxed{
\frac{|F|}{R}<(2n+1)3^{18d}.
}
\tag{7.6}
$$



This estimate is deliberately coarse. Its merit is that its exponential cost is in $d$, with an explicit constant, rather than an uncontrolled factorial or an unnamed determinant height.

Combining (6.4) and (7.6) proves Theorem C:


$$
\boxed{
\frac gR
<
\frac{(2n+1)3^{18d}}{\mathcal D_h}.
}
\tag{7.7}
$$



---

## 8. An evaluated obstruction on original indices with a small prime divisor of $h$

### 8.1 The prime $19$

Suppose $19\mid h$. Then


$$
q\ge19^{v_{19}(h!)-v_{19}(d!)}.
$$


Legendre’s formula gives the elementary bounds


$$
v_{19}(h!)\ge\left\lfloor\frac h{19}\right\rfloor,
\qquad
v_{19}(d!)\le\frac d{18}.
$$


With $h=2000b+1$ and $d=b-1$,


$$
v_{19}(h!)-v_{19}(d!)
\ge
\frac{2000b+1}{19}-1-\frac{b-1}{18}
\ge100b.
$$


Thus


$$
\boxed{q\ge19^{100b}.}
\tag{8.1}
$$


Equations (7.6) and $g/R=(|F|/R)/q$ yield


$$
\boxed{
\frac gR
<
\frac{(4002b+1)3^{18(b-1)}}{19^{100b}}.
}
\tag{8.2}
$$


The right side tends to zero exponentially.

By the complete-error lower bound,


$$
\boxed{
q(e+\pi)-p
>
\frac{19^{100b}}
     {2(4002b+1)3^{18(b-1)}}
\longrightarrow+\infty.
}
\tag{8.3}
$$



This is a lower bound for the actual primitive whole error. It is not a lower bound for an unpaid determinant.

### 8.2 Exact evaluation of the original congruence condition

Let


$$
K=249005515+574312172u.
$$


Modulo $18$,


$$
249005515\equiv13,\qquad
574312172\equiv14.
$$


The element $3$ has order $18$ modulo $19$, and


$$
3^5\equiv15\pmod{19},\qquad 2000\equiv5\pmod{19}.
$$


Therefore


$$
19\mid 2000\cdot3^K+1
\quad\Longleftrightarrow\quad
K\equiv5\pmod{18}.
$$


This is equivalent to


$$
13+14u\equiv5\pmod{18},
$$


or


$$
\boxed{u\equiv2\pmod9.}
\tag{8.4}
$$



The intersection with the supplied original congruence condition is precisely


$$
\boxed{u\equiv2\pmod{9\cdot29^9}.}
\tag{8.5}
$$



These are original congruence-class indices, not small diagnostic replacements for $n=2001b$. On their members in the original allowed domain, (8.2)–(8.3) hold unconditionally. If the allowed domain is the progression with its original lower cutoff, this supplies an infinite divergent subprogression. If there is an additional unstated restriction on $u$, its intersection must be checked rather than assumed.

### 8.3 A broader necessary condition for any successful subsequence

A similar explicit estimate works whenever $h$ has a prime divisor at most $97$.

For $p\le17$,


$$
v_p(h!)-v_p(d!)
\ge
\frac h{17}-1-d
\ge100b.
$$


For $19\le p\le97$,


$$
v_p(h!)-v_p(d!)
\ge
\frac h{97}-1-\frac d{18}
\ge20b
$$


on the original domain.

Thus, if any prime $p\le97$ divides $h$,


$$
q\ge2^{80b}.
$$


Consequently


$$
\boxed{
\frac gR
<
(4002b+1)\left(\frac{3^{18}}{2^{80}}\right)^b,
}
\tag{8.6}
$$


which again tends to zero exponentially.

It follows that any original subsequence along which the primitive errors tend to zero must eventually satisfy


$$
\boxed{
\gcd\!\left(h,\prod_{p\le97}p\right)=1.
}
\tag{8.7}
$$



This is a necessary arithmetic condition, not a claim that such complementary indices are absent.

---

## 9. What has and has not been proved about uniform comparison

No fixed integer $C$ satisfying


$$
g\mid CR
$$


has been proved on the entire original domain.

Nor has the uniform estimate


$$
|F|\le CR
$$


been proved or disproved for this original family. The present results must not be advertised as a counterexample to that estimate.

What **has** been proved is the evaluated comparison


$$
\frac gR
<
\frac{(2n+1)3^{18d}}{\mathcal D_h},
$$


together with exact final-gcd valuations at all primes dividing $h$. This is enough to obstruct decay on an explicitly characterized portion of the original domain.

The precise obstruction to extending this argument immediately to all original indices is visible:

* $\mathcal D_h$ is very large when $h$ has a fixed small prime divisor;
* if $h$ is prime, then $\mathcal D_h=h$;
* the present bound for $|F|/R$ is exponential in $d$, so it does not exploit merely $q\ge h$ effectively.

It would be invalid to assume that $h=2000b+1$ always has a small prime divisor. No such covering theorem has been supplied or proved.

---

## 10. A sharper follow-on lemma

The exact denominator divisibility changes the next analytic-arithmetic target.

### Proposed original-family obstruction lemma

Prove, for a fixed positive constant $C$, that


$$
\boxed{
|F|\le C hR
}
\tag{10.1}
$$


at all sufficiently large original indices.

Then $q\ge h$ gives


$$
\frac Rg=\frac{qR}{|F|}\ge\frac1C,
$$


and hence


$$
\boxed{
q(e+\pi)-p>\frac1{2C}.
}
\tag{10.2}
$$


This would rule out vanishing primitive errors for the whole original family, including every subsequence.

The distinction from the earlier target is important. A bound $|F|\le CR$ is no longer necessary for this obstruction route. The newly forced factor $h$ in the actual primitive denominator pays for a linear loss in $h$.

The proof of (7.5) identifies the exact place where improvement is needed: it takes absolute values in the inverse factorial convolution (7.1). A proof of (10.1) must recover cancellation specific to the contact polynomial, rather than merely estimating arbitrary top coefficients separately.

Conversely, an irrationality proof from this family still requires


$$
g/R\longrightarrow\infty
$$


on one infinite set of admissible original indices. The new results force such a set eventually outside (8.7), and require it to overcome the exact divisor $\mathcal D_h\mid q$.

Neither outcome is established here.

---

## 11. Bounded exact arithmetic checks

No computation was executed. None of the new proofs requires an original-index matrix calculation.

### 11.1 New small content-and-endpoint check

This check is different from the five already-certified beta-charge identities and need not repeat them.

**Inputs**


$$
n=13,\qquad b=3,\qquad d=2,\qquad h=11.
$$


Use the exact moments


$$
\mu_\ell
=(\ell+3)!-2(\ell+4)!+(\ell+5)!,
\qquad 0\le\ell\le21,
$$


to construct the monic degree-$11$ orthogonal polynomial, its least clearer $a$, and the actual primitive


$$
r=a(x-1)^2p_{11}.
$$


The largest factorial input is $26!$.

Then evaluate $\gamma_j,F,E,T,R,g,q$ from the supplied exact formulas.

**Expected verifiable outputs**


$$
\gcd(\gamma_0,\gamma_1,\gamma_2)=11!=39916800,
$$




$$
a\not\equiv0\pmod{11},
$$




$$
r(x)\equiv a\,x^{11}(x-1)^2\pmod{11},
$$




$$
\frac E{2!}\equiv a\pmod{11},
$$




$$
T\equiv F\equiv0\pmod{11},
\qquad
g\not\equiv0\pmod{11},
\qquad
11\mid q.
$$


Also $\ell=1$ and $R\in\mathbb Z$, since $h=11\ge4d+1=9$.

This is an auxiliary normalization check only. It is not an original-index asymptotic certificate.

### 11.2 Optional bounded residue table for the small-prime obstruction

A targeted arithmetic table could determine exactly which original congruence classes are excluded by primes $p\le97$.

Write


$$
u=2+29^9t,\qquad
K=K_0+2K_1+K_1\,29^9t,
$$


where


$$
K_0=249005515,\qquad K_1=574312172.
$$


For each prime $p\le97$, $p\ne3$, compute


$$
m_p=
\frac{\operatorname{ord}_p(3)}
     {\gcd(\operatorname{ord}_p(3),K_1\,29^9)}
$$


and the residue set


$$
A_p=
\left\{
0\le t<m_p:
2000\cdot3^{K_0+2K_1+K_1\,29^9t}+1\equiv0\pmod p
\right\}.
$$



Every period satisfies $m_p\le96$, so this asks for fewer than $25\cdot96$ bounded modular tests.

**Expected verifiable output:** the complete list $(p,m_p,A_p)$, including


$$
m_{19}=9,\qquad A_{19}=\{0\}.
$$


Such a table establishes exactly those residue exclusions. A claim that their union covers the entire original class would require a separate exact covering certificate; it must not be inferred from several successful residues.

---

## 12. Final proof-status ledger

| Statement | Status |
|---|---|
| Original finite matrix, complete $B_j$, and paid scalar reduction retained | Established and reused |
| $\ell=1$, $R\in\mathbb Z_{>0}$ on the original domain | Established parent results |
| Whole-error sign and two-sided bound | Proof reviewed at the original hypotheses |
| $\gcd(\gamma_0,\ldots,\gamma_d)=h!$ | **New proved result** |
| $\gcd(a,h)=1$ | **New proved result** |
| $v_p(g)=v_p(d!)$ for every $p\mid h$ | **New proved result** |
| $\mathcal D_h\mid q$, in particular $h\mid q$ | **New proved result** |
| Explicit bound $g/R<(2n+1)3^{18d}/\mathcal D_h$ | **New proved result** |
| Exponential primitive-error divergence when $19\mid h$ | **New proved result** |
| Exact condition $19\mid h\iff u\equiv2\pmod9$ | **New proved result** |
| Any successful subsequence must eventually have $h$ free of primes $\le97$ | **New proved necessary condition** |
| Fixed-$C$ divisibility $g\mid CR$ on the whole original domain | Open |
| Sharper obstruction bound $|F|\le ChR$ | Concrete remaining lemma |
| A successful infinite primitive-decay subsequence | Not established |
| Rationality or irrationality of $e+\pi$ | Unresolved |

The main advance is an exact interaction between **primitive polynomial content, the repeated contact at $1$, and the complete endpoint charge**. It prevents the final gcd from absorbing the $h$-supported factorial part of $F$: at those primes its valuation is exactly the much smaller valuation of $d!$.

The remaining bottleneck is no longer merely “estimate a large gcd.” It is to control the complementary original indices while respecting


$$
\mathcal D_h\mid q,
$$


either by proving the substantially weaker uniform obstruction bound


$$
|F|\le ChR,
$$


or by finding an actual infinite original subsequence with $g/R\to\infty$ despite this forced primitive-denominator divisor. No bounded computation by itself settles that infinite obligation.
