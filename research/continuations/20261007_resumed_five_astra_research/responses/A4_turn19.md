> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Arithmetic audit and scaled exterior-Gram refinement

## 1. Executive conclusions

The two new arguments under review survive the audit at their stated scopes.

1. **A2’s exact-content and denominator theorems are accepted.** For every admissible original index
   

$$
b=3^{249005515+574312172u},\qquad n=2001b,\qquad
   d=b-1,\qquad h=2000b+1,
$$


   retaining $u\equiv2\pmod{29^9}$ and every other original admissibility condition,
   

$$
\gcd(\gamma_0,\ldots,\gamma_d)=h!,
$$


   and, for every prime $p\mid h$,
   

$$
p\nmid a,\qquad \frac{E}{d!}\equiv a\pmod p,\qquad
   v_p(g)=v_p(d!).
$$


   Consequently,
   

$$
\mathcal D_h:=\prod_{p\mid h}p^{v_p(h!)-v_p(d!)}
   \mid q,\qquad h\mid q.
$$



2. **A2’s evaluated comparison is accepted.**
   

$$
\frac{|F|}{R}<(2n+1)3^{18d},\qquad
   \frac gR<\frac{(2n+1)3^{18d}}{\mathcal D_h}.
$$


   The second inequality concerns the actual **all-prime** gcd, not a restricted-prime substitute.

3. **The small-prime divergence conclusions are accepted with their domain qualifications.** In particular,
   

$$
19\mid h\iff u\equiv2\pmod9.
$$


   On any unbounded collection of admissible original indices where $h$ has a prime divisor at most $97$, the actual positive primitive whole error tends to $+\infty$. This does **not** cover the full original progression. The supplied modular receipt explicitly exhibits a surviving progression.

4. **The parent’s exterior-Gram refinement is accepted for every integer $k\ge32$.**
   

$$
M_y\succeq K_k\gamma_k B_k([k^2,4k^2]),
   \qquad K_k=\frac{16^{k-1}}3.
$$


   It gives a lower bound for the **same integer polynomial** $H_k$, with all moments and corrections retained:
   

$$
(-1)^kH_k(e+\pi)\ge
   \Lambda_k^kJ_k^\nu(K_k\gamma_k)^k
   (3k^2)^{k^2}\mathfrak h_k>0.
$$



5. **The matching raw scale is proved, but primitive divergence is not.**
   

$$
\log|H_k(e+\pi)|=4k^2\log k+O(k^2).
$$


   Dividing by the actual final gcd $G_k$ remains essential.

6. **One further evaluated analytic consequence is proved below**, without entering A2’s complementary arithmetic task or A3’s final-content task:
   

$$
\boxed{
   |H_k(e+\pi)|
   \ge
   \left(\frac{\Lambda_k}{16k}\right)^k
   \left(\frac{k^2(k^2-1)}3\right)^{k^2}
   \mathfrak h_k^2
   \qquad(k\ge32).
   }
$$


   In particular,
   

$$
\boxed{
   \log|H_k(e+\pi)|
   \ge k\log\Lambda_k+4k^2\log k
       -(\log48)k^2-O(k\log k).
   }
$$



None of these statements proves rationality or irrationality of $e+\pi$.

---

## 2. Objects, exact boundaries, and arithmetic normalization

### 2.1 A2: the original finite matrix

The matrix is exactly


$$
H_{rj}(X)=X-A_{n+r,j}-B_j,\qquad 0\le r,j\le d,
$$


where


$$
A_{m,j}
=j!\sum_{v=0}^{m-j}(-1)^v\binom{m-j}{v}\frac1{(j+v)!},
$$




$$
B_j=4\sum_{v=0}^{2j-1}\frac{(-1)^v}{2v+1},\qquad B_0=0.
$$


The physical row window is $n,\ldots,n+d$, and the columns are $0,\ldots,d$. Every summand in every $B_j$ is retained.

Write


$$
R_{rj}=A_{n+r,j}+B_j,\qquad
\mathsf W_{rj}=(n+r)!R_{rj}.
$$


The actual arithmetic payments remain


$$
\kappa_r=\gcd\bigl((n+r)!,\mathsf W_{r0},\ldots,\mathsf W_{rd}\bigr),
\qquad C_r=\frac{(n+r)!}{\kappa_r},
$$




$$
Y_{rj}=C_rR_{rj},\qquad
c_j=\gcd_{0\le r\le d}(C_r,Y_{rj}),
$$




$$
\mathcal L_n=\operatorname{lcm}_{r}C_r,\qquad
P_n=\frac{\prod_rC_r}{\prod_jc_j}.
$$


Thus


$$
D_n(X)=\det\left[\frac{C_rX-Y_{rj}}{c_j}\right]
=P_n\det H(X)=U_nX-V_n.
$$


The established scalar bridge is retained as stated:


$$
D_n(X)=\frac{P_n\tau_n}{aK_n}(FX-E-T),
\qquad
K_n=\frac{\prod_{r=0}^d(n+r)!}
{\prod_{j=0}^dj!(n-j)!}.
$$


No factor in this bridge is discarded.

Let $p_h$ be the monic orthogonal polynomial for


$$
x^b(x-1)^de^{-x}\,dx,\qquad x>0.
$$


Its actual least coefficient clearer is $a>0$, and


$$
r(x)=a(x-1)^dp_h(x)=\sum_{k=0}^nr_kx^k
$$


is primitive in $\mathbb Z[x]$. Indeed, minimality of $a$ makes $ap_h$ primitive, and multiplication by the monic primitive polynomial $(x-1)^d$ preserves content.

The charges are


$$
F=\sum_{k=0}^nr_kk!,\qquad
E=\sum_{k=0}^nr_k\sum_{v=0}^k\frac{k!}{v!},
$$




$$
\gamma_j=(-1)^{n-j}(n-j)!r_{n-j}
-\sum_{i<j}\binom{n+1}{j-i}\gamma_i,
$$




$$
w_j=\binom nj\gamma_j,\qquad
T=\sum_{j=0}^dw_jB_j.
$$


The accepted exact identities include


$$
F=\sum_jw_j<0,\qquad
R=\sum_{k=0}^n|r_k|
\frac{k!(3/4)_k}{(n-k+1/4)_{k+1}}
=4(-1)^n\sum_{j=0}^d\frac{w_j}{4j+1}>0.
$$



The established original-domain clearing result is $\ell=1$; both $T$ and $R$ are integers. Therefore


$$
g=\gcd(|F|,|E+T|),\qquad
q=-F/g>0,\qquad p=-(E+T)/g
$$


are the actual primitive objects. Also


$$
G_n=\gcd(U_n,|V_n|)=U_n\frac g{|F|}.
$$



I reuse, without repeating its closed sign proof, the accepted whole-error theorem


$$
M=F(e+\pi)-E-T<0,
$$




$$
\boxed{
\frac R{2g}<q(e+\pi)-p<6005\frac Rg.
}
\tag{2.1}
$$


Both complete integral channels are included in $M$.

### 2.2 Compact family

Here


$$
0\le m<2k,\qquad 0\le j<k,
$$


and


$$
a_0=1,\quad a_d=1-da_{d-1},\quad c_n=a_{2n}-(-1)^n,
$$




$$
\rho_0=0,\quad \rho_{n+1}+\rho_n=\frac1{2n+1},
\quad r_n=-(2n)!+4\rho_n.
$$


Set


$$
C_{mj}=c_{m+j},\quad \mathcal R_{mj}=r_{m+j},
\quad w_m=(-1)^m,\quad v_j=(-1)^j,
$$




$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
$$


The integer affine polynomial is


$$
H_k(s)=\det[C\mid \Lambda_k\mathcal R+s\Lambda_kwv^T]
=H_{0,k}+H_{1,k}s.
\tag{2.2}
$$



The exact measures are


$$
L=\mu-\delta_{-1},
$$




$$
\frac{d\mu}{dx}=
\begin{cases}
e^{-1}\cosh(\sqrt x)/\sqrt x,&0<x<1,\\
e^{-1-\sqrt x}/(2\sqrt x),&x>1,
\end{cases}
$$


and


$$
\frac{d\nu}{dx}
=\frac{e^{\sqrt x}+4/(1+x)}{2\sqrt x},\qquad0<x<1.
$$


Their complete moment relation gives, with $s_0=e+\pi$,


$$
H_k(s)=\Lambda_k^k
\det[C\mid N+(s-s_0)wv^T],
\qquad N_{mj}=\nu_{m+j}.
\tag{2.3}
$$


This identity evaluates the existing integer polynomial; it is not an integer change of normalization.

The actual final gcd and primitive pair remain


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$




$$
q_k=\frac{|H_{1,k}|}{G_k},\qquad
p_k=-\frac{(-1)^kH_{0,k}}{G_k}.
$$


The accepted sign theorem, for $k\ge32$, gives


$$
q_k(e+\pi)-p_k=\frac{|H_k(e+\pi)|}{G_k}>0.
\tag{2.4}
$$



---

## 3. Audit of A2’s exact factorial content

The finite Laguerre expansion yields


$$
(-1)^kk!r_k
=\sum_{j=0}^d
\binom{n+1}{n-j-k}\gamma_j.
\tag{3.1}
$$


Let


$$
\Gamma=\gcd(\gamma_0,\ldots,\gamma_d),\qquad
C=\gcd_{0\le k\le n}(k!r_k).
$$


Equation (3.1) proves $\Gamma\mid C$. Conversely, the triangular recurrence for $\gamma_j$ expresses each $\gamma_j$ by integer operations on the top factorial coefficients, so $C\mid\Gamma$. Hence


$$
\Gamma=C.
\tag{3.2}
$$



Since $n-j\ge h$, induction in that recurrence gives


$$
h!\mid\gamma_j\quad(0\le j\le d),
$$


and therefore $h!\mid\Gamma$.

For the reverse divisibility, suppose some prime $p$ satisfies


$$
v_p(\Gamma)>v_p(h!).
$$


For $0\le k\le h$, divisibility $\Gamma\mid k!r_k$ implies $p\mid r_k$. Thus $\bar r$, the reduction modulo $p$, is divisible by $x^{h+1}$.

It is also divisible by $(x-1)^d$. These factors are coprime over every $\mathbb F_p$, including $\mathbb F_2$. If $\bar r\ne0$, its degree would be at least


$$
h+1+d=n+1,
$$


contrary to $\deg r=n$. If $\bar r=0$, every coefficient of $r$ would be divisible by $p$, contrary to primitivity.

Therefore


$$
\boxed{\gcd(\gamma_0,\ldots,\gamma_d)=h!.}
\tag{3.3}
$$



**Decision: accepted.** The use of actual primitive content is indispensable. The conclusion would generally fail after multiplying $r$ by an additional integer.

---

## 4. Audit at every prime dividing $h$

Fix any prime $p\mid h$.

### 4.1 Rigid reduction of $r$

For every $k<h$,


$$
v_p(k!)<v_p(h!),
$$


because $h!/k!$ includes the $p$-divisible factor $h$. Since $h!\mid k!r_k$, this gives $p\mid r_k$.

Thus $x^h\mid\bar r$. Together with $(x-1)^d\mid\bar r$, primitivity and degree $n=h+d$ force


$$
\boxed{
r(x)\equiv a\,x^h(x-1)^d\pmod p,\qquad p\nmid a.
}
\tag{4.1}
$$


The scalar is $a$ because the leading coefficient of $r$ is $a$.

### 4.2 The complete exponential endpoint

Write


$$
r(1+z)=z^dS(z),\qquad S(z)=\sum_{j=0}^hs_jz^j\in\mathbb Z[z].
$$


The exact endpoint formula is


$$
E=\sum_{j=0}^h(d+j)!s_j.
$$


Hence


$$
\frac E{d!}=\sum_{j=0}^h(d+1)\cdots(d+j)s_j\in\mathbb Z,
\tag{4.2}
$$


where the $j=0$ product is $1$.

From (4.1),


$$
S(z)\equiv a(1+z)^h
=a(1+z^p)^{h/p}\pmod p.
$$


Consequently,


$$
s_0\equiv a,\qquad s_j\equiv0\quad(1\le j<p).
$$


Every product in (4.2) with $j\ge p$ contains $p$ consecutive integers and is divisible by $p$. Thus every term except $j=0$ vanishes modulo $p$:


$$
\boxed{\frac E{d!}\equiv a\not\equiv0\pmod p.}
\tag{4.3}
$$


In particular,


$$
v_p(E)=v_p(d!).
\tag{4.4}
$$



This argument checks all terms of the endpoint expansion; it is not an evaluation of only its constant contribution without controlling the rest.

### 4.3 Strict valuation separation from the complete $T$

Let


$$
\Lambda_B=\operatorname{lcm}(1,3,\ldots,4d-1).
$$


Since $h!\mid w_j$ and every denominator of every $B_j/4$ divides $\Lambda_B$,


$$
T\in\frac{4h!}{\Lambda_B}\mathbb Z.
\tag{4.5}
$$


Here $\Lambda_B\mid h!$, so the displayed generator is an integer.

Put $L_p=v_p(\Lambda_B)$.

* If $L_p=0$, then $v_p(h!/d!)\ge v_p(h)>0$.
* If $L_p>0$, then $p^{L_p}\le4d-1$. The first two multiples of $p^{L_p}$ strictly above $d$ are both at most
  

$$
d+2p^{L_p}\le9d-2<h.
$$


  They contribute at least $2L_p>L_p$ to $v_p(h!/d!)$.

The strict inequality $9d-2<h$ follows directly from


$$
h=2000b+1,\qquad d=b-1.
$$


Therefore


$$
v_p(h!)-v_p(\Lambda_B)>v_p(d!).
\tag{4.6}
$$


Equation (4.5) proves


$$
v_p(T)>v_p(d!)=v_p(E).
$$


This remains valid if $T=0$, using $v_p(0)=+\infty$.

The unequal valuations prevent cancellation:


$$
v_p(E+T)=v_p(d!).
$$


Since $h!\mid F$,


$$
\boxed{v_p(g)=v_p(d!)\qquad(p\mid h).}
\tag{4.7}
$$



**Decision: accepted for every prime divisor of $h$.** The actual odd lcm and the entire $T$ have been used.

The analogous assertion for $R$ also survives: with


$$
\Lambda_R=\operatorname{lcm}(1,5,\ldots,4d+1),
$$


the same two-multiple argument uses $d+2p^{L_p}\le9d+2<h$. Thus $v_p(R)>v_p(d!)$ for $p\mid h$. This local fact alone does not compare $R/g$ as a real number.

### 4.4 The actual denominator divisor

For each $p\mid h$,


$$
v_p(q)=v_p(F)-v_p(g)
\ge v_p(h!)-v_p(d!).
$$


Hence


$$
\boxed{\mathcal D_h\mid q.}
\tag{4.8}
$$


Since $h!/d!$ contains $h$,


$$
h\mid\mathcal D_h\mid q.
\tag{4.9}
$$



No claim has been made about exact $g$-valuations at primes not dividing $h$. Nevertheless, because $q=|F|/g$ is the actual primitive denominator,


$$
\boxed{g=\frac{|F|}{q}\le\frac{|F|}{\mathcal D_h}.}
\tag{4.10}
$$


This implication includes all primes in $g$.

---

## 5. Audit of the inverse convolution and beta comparison

Set $N=n+d$.

### 5.1 Every term in the inverse convolution

Define


$$
t_i=(-1)^{n-i}(n-i)!r_{n-i}.
$$


The triangular recurrence says, through degree $d$, that $(t_i)$ is the convolution of $(\gamma_j)$ with the coefficients of $(1+z)^{n+1}$.

Since


$$
(1+z)^{-n-1}
=\sum_{m\ge0}(-1)^m\binom{n+m}{m}z^m,
$$


the inverse formula is


$$
\gamma_j=\sum_{i=0}^j
(-1)^{j-i}\binom{n+j-i}{j-i}
(-1)^{n-i}(n-i)!r_{n-i}.
\tag{5.1}
$$


There are no omitted terms: the finite triangular inverse requires exactly $0\le i\le j\le d$.

Using $F=\sum_j\binom nj\gamma_j$,


$$
|F|\le\sum_{i=0}^d|r_{n-i}|(n-i)!S_i,
$$


where


$$
S_i=\sum_{j=i}^d\binom nj\binom{n+j-i}{j-i}.
\tag{5.2}
$$



For $i\le j\le d$,


$$
\binom nj\binom{n+j-i}{j-i}
\le\frac{N^{2j-i}}{j!(j-i)!}.
$$


For the majorant $t_j'=N^{2j-i}/(j!(j-i)!)$,


$$
\frac{t'_{j-1}}{t'_j}
=\frac{j(j-i)}{N^2}\le\frac{d^2}{N^2}<\frac14.
$$


The last term therefore bounds the geometric tail:


$$
\boxed{
S_i<\frac{2N^{2d-i}}{d!(d-i)!}.
}
\tag{5.3}
$$



### 5.2 Beta weights

Let


$$
D_i=\frac{(n-i)!}{c_{n,n-i}}
=\frac{(i+1/4)_{n-i+1}}{(3/4)_{n-i}}.
$$


For $i=0$,


$$
D_0=(n+1/4)\prod_{j=0}^{n-1}\frac{j+1/4}{j+3/4}
\le n+\frac14.
$$


For $1\le i\le d$, direct cancellation gives


$$
\frac{D_i}{D_{i-1}}
=\frac{n-i+3/4}{i-3/4}
\le\frac{4(n-i+1)}i.
$$


Thus


$$
D_i\le\left(n+\frac14\right)4^i\binom ni.
\tag{5.4}
$$



All beta weights are positive. Hence


$$
R\ge\sum_{i=0}^d|r_{n-i}|c_{n,n-i}
$$


and


$$
\frac{|F|}{R}\le\max_{0\le i\le d}D_iS_i.
$$


Using $\binom ni\le N^i/i!$, equations (5.3)–(5.4) give


$$
D_iS_i<
2\left(n+\frac14\right)
\frac{N^{2d}}{(d!)^2}4^i\binom di.
$$


Finally,


$$
4^i\binom di\le\sum_{i=0}^d4^i\binom di=5^d.
$$


Therefore


$$
\boxed{
\frac{|F|}{R}<
2\left(n+\frac14\right)5^d
\frac{(n+d)^{2d}}{(d!)^2}.
}
\tag{5.5}
$$



### 5.3 Original-domain specialization

On the original domain, $b$ is far above the threshold $b\ge2002$, so


$$
\frac{n+d}{d}=2002+\frac{2001}{b-1}\le2003.
$$


Using $d!\ge(d/e)^d$ and $e<3$,


$$
\frac{|F|}{R}
<(2n+1)(45\cdot2003^2)^d.
$$


The exact comparison is


$$
45\cdot2003^2=180540405<387420489=3^{18}.
$$


Thus


$$
\boxed{\frac{|F|}{R}<(2n+1)3^{18d}.}
\tag{5.6}
$$


Combining with (4.10),


$$
\boxed{\frac gR<\frac{(2n+1)3^{18d}}{\mathcal D_h}.}
\tag{5.7}
$$



**Decision: accepted.** The argument is coarse but complete. Its principal loss is taking absolute values in (5.1), not an unpaid arithmetic division.

---

## 6. Original small-prime classes and finite receipts

### 6.1 The $19$-class

If $19\mid h$, Legendre’s formula gives


$$
v_{19}(h!)-v_{19}(d!)
\ge\frac h{19}-1-\frac d{18}\ge100b.
$$


The last inequality holds already for $b\ge1$. Thus


$$
q\ge19^{100b},
$$




$$
\frac gR<
\frac{(4002b+1)3^{18(b-1)}}{19^{100b}},
$$


and by (2.1),


$$
q(e+\pi)-p>
\frac{19^{100b}}
{2(4002b+1)3^{18(b-1)}}\longrightarrow+\infty.
\tag{6.1}
$$



For the congruence calculation, write


$$
K=249005515+574312172u.
$$


Modulo $18$,


$$
K\equiv13+14u.
$$


Modulo $19$, $2000\equiv5$, the order of $3$ is $18$, and $3^5\equiv15=-5^{-1}$. Therefore


$$
19\mid h
\iff K\equiv5\pmod{18}
\iff u\equiv2\pmod9.
$$


Intersecting with $u\equiv2\pmod{29^9}$ gives


$$
u\equiv2\pmod{9\cdot29^9}.
$$


Any additional original admissibility restriction remains in force. An infinite divergent subprogression follows only when that intersection is unbounded.

### 6.2 Every prime at most $97$

For $p\le17$,


$$
v_p(h!)-v_p(d!)
\ge\frac h{17}-1-d\ge100b.
$$


For $19\le p\le97$,


$$
v_p(h!)-v_p(d!)
\ge\frac h{97}-1-\frac d{18}\ge20b.
$$


Thus, whenever some prime $p\le97$ divides $h$,


$$
q\ge2^{80b}.
$$


For the second range this follows from $p^{20b}\ge19^{20b}>2^{80b}$; for the first, $p^{100b}\ge2^{100b}$.

Consequently,


$$
\frac gR<
(4002b+1)\left(\frac{3^{18}}{2^{80}}\right)^b
\longrightarrow0.
\tag{6.2}
$$


The whole primitive error diverges along every unbounded collection of such indices.

It follows that a subsequence with primitive errors tending to zero must eventually have


$$
\gcd\left(h,\prod_{p\le97}p\right)=1.
\tag{6.3}
$$



### 6.3 Status of the supplied receipts

I have not executed either receipt.

The $n=13,b=3$ receipt concerns one auxiliary instance with a degree-$11$ linear system and factorial inputs through $26!$. Its reported outputs include


$$
\gcd(\gamma)=11!,\qquad g=56,\qquad
a\equiv E/2!\equiv1\pmod{11}.
$$


These are finite normalization data, not original-index asymptotic evidence.

The modular receipt concerns exact residue classes of


$$
u=2+29^9t.
$$


Its nonempty exclusions are reported as


$$
\begin{array}{c|c|c}
p&\text{period}&\text{excluded }t\\ \hline
19&9&0\\
23&11&8\\
31&15&10\\
47&23&12\\
79&39&6\\
83&41&29
\end{array}
$$


with all other listed primes having empty exclusion sets. Their combined period is


$$
\operatorname{lcm}(9,11,15,23,39,41)=6068205.
$$


The residue $1$ differs from every displayed excluded residue modulo its period. Thus, conditional on the supplied complete modular table, every


$$
t\equiv1\pmod{6068205}
$$


avoids all prime divisors $p\le97$ of $h$.

**Decision:** the symbolic divergence theorem is proved independently of the receipt. The receipt is retained as coordinator-verified finite arithmetic evidence. A covering assertion by these primes is rejected; the reported survivor directly contradicts it.

---

## 7. Audit of the exterior-Gram refinement

### 7.1 Relative control by the exterior norm

For


$$
I_k=[k^2,4k^2],\qquad
E(p)=\int_{I_k}p(x)^2\,dx,\qquad
M(p)=\max_{[-1,1]}|p|,
$$


the accepted Legendre extrapolation lemma gives, for $\deg p\le k-1$,


$$
M(p)^2\le K_kE(p),\qquad K_k=\frac{16^{k-1}}3.
\tag{7.1}
$$



Let


$$
Q_y(x)=\prod_{j=1}^k(x-y_j),\qquad y\in[0,1]^k.
$$


On $I_k$,


$$
Q_y(x)\ge(k^2-1)^k,\qquad
\frac{d\mu}{dx}\ge\frac{e^{-1-2k}}{4k}.
$$


Thus the contribution of $I_k$ is at least $c_kE(p)$, where


$$
c_k=\frac{(k^2-1)^k}{4ke^{1+2k}}
>
c'_k:=\frac1{12k}\left(\frac{k^2-1}{9}\right)^k.
\tag{7.2}
$$



On $[0,1]$,


$$
|Q_y(x)|\le1,\qquad \mu([0,1])\le1,
$$


so the overlap loss is at most $M(p)^2$. The atom contributes


$$
-p(-1)^2Q_y(-1)\ge-2^kM(p)^2.
$$


All other $x>1$ contributions are nonnegative. Therefore, using (7.1),


$$
L(p^2Q_y)
\ge\left[c'_k-(1+2^k)K_k\right]E(p).
\tag{7.3}
$$



The coefficient is exactly $K_k\gamma_k$, because


$$
K_k\frac4k\left(\frac{k^2-1}{144}\right)^k
=\frac1{12k}\left(\frac{k^2-1}{9}\right)^k.
$$


Hence


$$
\gamma_k=\frac4k\left(\frac{k^2-1}{144}\right)^k-1-2^k,
$$


and


$$
\boxed{L(p^2Q_y)\ge K_k\gamma_kE(p).}
\tag{7.4}
$$



For $k\ge32$,


$$
\frac{k^2-1}{288}>3,
$$


so the positive term in $\gamma_k$ exceeds


$$
\frac4k\,2^k3^k\ge4\cdot2^k.
$$


Thus $\gamma_k>0$.

**Decision: accepted.** Crucially, the losses have been bounded relative to the exterior $L^2$ norm before taking determinants. The refinement does not incorrectly reverse the extrapolation inequality.

### 7.2 Matrix and determinant comparison

Define


$$
B_k(I_k)=\left(\int_{I_k}x^{a+b}\,dx\right)_{0\le a,b<k},
$$




$$
M_y=\left(L(x^{a+b}Q_y(x))\right)_{0\le a,b<k}.
$$


For a coefficient vector $v$, equation (7.4) is exactly


$$
v^TM_yv\ge K_k\gamma_k\,v^TB_k(I_k)v.
$$


Therefore


$$
M_y\succeq K_k\gamma_k B_k(I_k).
$$


Since the interval Gram matrix is positive definite, conjugation by its inverse square root proves


$$
\det M_y\ge(K_k\gamma_k)^k\det B_k(I_k).
\tag{7.5}
$$



For an interval $[A,A+\ell]$, substitution $x=A+\ell t$ gives a triangular monomial transformation with diagonal


$$
1,\ell,\ldots,\ell^{k-1}.
$$


The integration measure contributes a further factor $\ell$ to the Gram matrix. Thus


$$
\det B_k([A,A+\ell])
=\ell^k\ell^{k(k-1)}\mathfrak h_k
=\ell^{k^2}\mathfrak h_k,
$$


where the classical Hilbert determinant is


$$
\mathfrak h_k=
\frac{\prod_{j=0}^{k-1}(j!)^4}
{\prod_{j=0}^{2k-1}j!}.
$$


For $\ell=3k^2$,


$$
\boxed{
\det M_y\ge
(K_k\gamma_k)^k(3k^2)^{k^2}\mathfrak h_k.
}
\tag{7.6}
$$



The entire affine-scaling exponent is $k^2$, not $k$ or $k(k-1)$.

### 7.3 The same whole determinant and exact boundaries

Reuse the accepted signed conditional determinant identity:


$$
(-1)^k\det[C\mid N]
=\frac1{k!}\int V(y)^2\det M_y\,d\nu^k(y).
$$


Consequently,


$$
\boxed{
(-1)^kH_k(e+\pi)\ge
\Lambda_k^kJ_k^\nu
(K_k\gamma_k)^k(3k^2)^{k^2}\mathfrak h_k>0,
}
\tag{7.7}
$$


where


$$
J_k^\nu=\frac1{k!}\int V(y)^2\,d\nu^k(y).
$$



All boundaries are unchanged:

- original block size: $2k\times2k$;
- original maximum index: $m+j=3k-2$;
- maximum degree in $M_y$: $2(k-1)+k=3k-2$;
- maximum factorial: $(6k-4)!$;
- last odd denominator in the complete correction: $6k-5$;
- auxiliary exterior Gram moments: only degrees $0,\ldots,2k-2$;
- compact Gram $J_k^\nu$: only degrees $0,\ldots,2k-2$.

No additional contact, physical row, or endpoint term has been introduced.

---

## 8. Density bound, raw growth, and a further evaluated consequence

### 8.1 The lower density bound is in the $x$-coordinate

For $0<x<1$,


$$
e^{\sqrt x}\ge1,\qquad \frac4{1+x}\ge2,\qquad 2\sqrt x\le2.
$$


Therefore


$$
\frac{d\nu}{dx}\ge\frac32.
\tag{8.1}
$$


This is a valid lower bound for the density with respect to $dx$. It does not repeat the invalid upper-density transfer from the $t$-coordinate.

The compact moment Gram matrix therefore dominates $(3/2)\mathcal H_k$, giving


$$
J_k^\nu\ge(3/2)^k\mathfrak h_k.
\tag{8.2}
$$



### 8.2 Matching leading raw growth

Let $S(m)=\sum_{j=0}^{m-1}\log(j!)$. Standard summation of Stirling’s estimate gives


$$
S(m)=\frac12m^2\log m-\frac34m^2+O(m\log m).
$$


Hence


$$
\log\mathfrak h_k=4S(k)-S(2k)
=-2(\log2)k^2+O(k\log k).
\tag{8.3}
$$


Also,


$$
\log\gamma_k=2k\log k-(\log144)k+O(\log k),
$$




$$
\log K_k=(\log16)k+O(1).
$$


Substitution into (7.7), using (8.2) and $\Lambda_k\ge1$, proves


$$
\log|H_k(e+\pi)|\ge4k^2\log k-O(k^2).
\tag{8.4}
$$



The accepted complete upper estimate is


$$
|H_k(e+\pi)|\le F_k^\perp,
$$




$$
F_k^\perp=
\Lambda_k^k21^kk!h_k
\prod_{r=0}^{k-1}(2k+4r)!,
$$




$$
h_k=
\frac{2^{k(k-1)}(\prod_{j=1}^{k-1}j!)^2}
{\prod_{r,j=0}^{k-1}(2r+2j+1)}.
$$


Its leading factorial contribution is


$$
\sum_{r=0}^{k-1}(2k+4r)\log k
=4k^2\log k+O(k\log k).
$$


The $k^2\log k$ terms in $\log h_k$ cancel, leaving $O(k^2)$; the clearer contribution is $k\log\Lambda_k=O(k^2)$. Thus


$$
\log F_k^\perp=4k^2\log k+O(k^2).
$$


Together with (8.4),


$$
\boxed{\log|H_k(e+\pi)|=4k^2\log k+O(k^2).}
\tag{8.5}
$$



### 8.3 Further proved consequence: an explicit lower bound without $\gamma_k$

This consequence stays entirely on the analytic side.

Put


$$
A_k=\frac4k\left(\frac{k^2-1}{144}\right)^k.
$$


For $k\ge32$, the preceding proof gives $A_k>4\cdot2^k$. Therefore


$$
1+2^k<\frac12A_k,
\qquad
\gamma_k>\frac12A_k.
$$


Since $K_kA_k=c'_k$,


$$
K_k\gamma_k>\frac{c'_k}{2}
=\frac1{24k}\left(\frac{k^2-1}{9}\right)^k.
$$


Using this and (8.2) in (7.7),


$$
|H_k(e+\pi)|
\ge
\Lambda_k^k(3/2)^k
\left[\frac1{24k}
\left(\frac{k^2-1}{9}\right)^k\right]^k
(3k^2)^{k^2}\mathfrak h_k^2.
$$


Simplification gives the announced evaluated bound:


$$
\boxed{
|H_k(e+\pi)|
\ge
\left(\frac{\Lambda_k}{16k}\right)^k
\left(\frac{k^2(k^2-1)}3\right)^{k^2}
\mathfrak h_k^2.
}
\tag{8.6}
$$



Taking logarithms, using


$$
k^2\log(1-k^{-2})=O(1)
$$


and (8.3), yields


$$
\boxed{
\log|H_k(e+\pi)|
\ge k\log\Lambda_k+4k^2\log k
-(\log48)k^2-O(k\log k).
}
\tag{8.7}
$$


This improves the explicit lower-side information beyond an unspecified $O(k^2)$, but still says nothing by itself about the final gcd.

---

## 9. Primitive arithmetic and producer separation

### 9.1 What the compact raw growth does and does not prove

Equation (8.5) implies


$$
\log\bigl(q_k(e+\pi)-p_k\bigr)
=4k^2\log k-\log G_k+O(k^2).
\tag{9.1}
$$


Therefore a hypothetical estimate


$$
\log G_k\le(4-\varepsilon)k^2\log k+O(k^2),
\qquad \varepsilon>0,
$$


on an infinite set would force


$$
q_k(e+\pi)-p_k\longrightarrow+\infty
$$


along that set.

**This is a conditional implication, not a proved gcd estimate.**

The known lower divisor


$$
\prod_{r=0}^{k-2}(r!)^2\mid G_k
$$


cannot be substituted for $G_k$ in the denominator of a lower bound. Its insufficiency for an upper-error estimate does not prove actual divergence.

The established compact payments also remain unchanged:


$$
\prod_{m=k}^{2k-1}e_{k,m}
=\frac{|\det C_k|}{\delta_{k,2k-1}}.
$$


For a saturated integer kernel basis $X$, with


$$
B_{rj}=\sum_mX_{rm}r_{m+j},
$$


the least entry clearer is


$$
L_X=
\frac{\Lambda_k}
{\gcd(\Lambda_k,\{\Lambda_kB_{rj}\}_{r,j})}.
$$


If


$$
L_X^k\det\mathcal M_X(s)=A_0+A_1s,
$$


the least simultaneous coefficient clearer remains


$$
\frac{L_X^k}{\gcd(L_X^k,A_0,A_1)},
$$


and the remaining integer content remains


$$
\frac{\gcd(A_0,A_1)}{\gcd(L_X^k,A_0,A_1)}.
$$


The exterior-Gram comparison pays none of these divisions.

### 9.2 Distinct original producers remain distinct

The compact theorem holds for every integer $k\ge32$, hence on


$$
k=9^{18+32u},\qquad u\ge0.
$$


It does not identify this determinant with the separate binary producer having


$$
b=9^{18+32u},\qquad n=4002b.
$$


That producer retains contact range $0,\ldots,b-1$, physical reconstruction range $0,\ldots,b$, and $z_b=0$, together with the complete corrected columns


$$
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^ax_0,
$$


and the full return


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f.
$$


Its paid valuation statement remains


$$
v_2\!\left(\frac S{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$


Nothing here removes $h^F$, $e_0$, the terminal condition, or the subtraction of $a$. Nor does it determine that producer’s actual corrected-column contents, norm, least simultaneous clearer, or final gcd.

The distinct ternary producer is not fully specified in this packet. Its boundary-column obligation remains open and receives no arithmetic transfer from the audited Laguerre matrix.

---

## 10. Decisions, remaining bottlenecks, and bounded checking

### 10.1 Decision ledger

| Claim | Decision |
|---|---|
| Exact content $\gcd(\gamma)=h!$ | **Accepted; proved symbolically** |
| $r\bmod p=a x^h(x-1)^d$, $p\nmid a$, for every $p\mid h$ | **Accepted** |
| Complete endpoint congruence $E/d!\equiv a\pmod p$ | **Accepted** |
| Strict complete-$T$ valuation gap using the actual odd lcm | **Accepted** |
| $v_p(g)=v_p(d!)$ for every $p\mid h$ | **Accepted** |
| $\mathcal D_h\mid q$, hence $h\mid q$ | **Accepted** |
| Inverse convolution and beta comparison | **Accepted term by term** |
| All-prime bound $g/R<(2n+1)3^{18d}/\mathcal D_h$ | **Accepted** |
| $19$-class and $p\le97$ divergence | **Accepted on the stated admissible subsets** |
| Small primes cover the original progression | **Rejected** |
| Exterior-norm comparison $M_y\succeq K_k\gamma_k B_k(I_k)$ | **Accepted for $k\ge32$** |
| Full interval determinant factor $(3k^2)^{k^2}$ | **Accepted** |
| Same-$H_k$ lower bound with unchanged moment boundaries | **Accepted** |
| Compact $x$-density lower bound $3/2$ | **Accepted** |
| Matching raw logarithmic growth | **Accepted** |
| Explicit lower bound (8.6) and constant $-\log48$ in (8.7) | **Further result proved here** |
| A final-gcd upper bound with leading coefficient below $4$ | **Open** |
| Primitive decay in either family | **Open** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

### 10.2 Exact remaining mathematical bottlenecks

For A2, the accepted whole-error comparison makes the successful-sequence obligation exactly


$$
R/g\longrightarrow0
$$


on one infinite set of admissible original indices. Such a set must eventually avoid all the small-prime exclusions established above.

The already proposed complementary obstruction lemma is


$$
|F|\le ChR
$$


for a fixed $C$ on an eventual original tail. Since $q\ge h$, it would imply


$$
q(e+\pi)-p>\frac1{2C}.
$$


This is a concrete open lemma, not proved by the exponential comparison audited here. I do not duplicate the active task of proving or disproving it.

For the compact family, the exact obligation is comparison with the actual all-prime $G_k$ on the same infinite indices:


$$
\frac{|H_k(e+\pi)|}{G_k}.
$$


The analytic numerator is now controlled to matching leading logarithmic order. The missing arithmetic is not supplied by real Gram comparisons or by known lower divisors of $G_k$.

### 10.3 Bounded exact arithmetic

**No additional finite computation is needed for the symbolic theorems proved in this report.** The closed $n=13,b=3$ calculation and the complete modular table need not be repeated.

If the coordinator wants one small transcription check specifically for the new affine-Gram scaling, the following is sufficient and independent of those closed calculations:

- **Input:** $k=2$, $I=[4,16]$, monomials $1,x$.
- **Expected exact matrix:**
  

$$
B_2(I)=
  \begin{pmatrix}
  12&120\\
  120&1344
  \end{pmatrix}.
$$


- **Expected determinant:**
  

$$
\det B_2(I)=1728
  =12^4\det
  \begin{pmatrix}1&1/2\\1/2&1/3\end{pmatrix}.
$$



This checks only the exponent and normalization in the interval-Gram identity. It is not a check of compact positivity at $k=2$, and it has no infinite arithmetic implication.

## Final status

The new A2 arithmetic is valid, and the scaled exterior-Gram refinement is valid. The additional explicit lower bound (8.6) is proved without changing any integer normalization.

The remaining obstacle to the global objective is precise: **neither family yet supplies a nonzero primitive whole error tending to zero on an explicitly admissible infinite set after division by its actual final all-prime gcd.** Conversely, the compact raw-growth theorem does not establish primitive divergence without a suitable upper bound for that gcd.

Thus the report advances the arithmetic restrictions and the evaluated analytic lower bounds, but proves neither rationality nor irrationality of $e+\pi$.
