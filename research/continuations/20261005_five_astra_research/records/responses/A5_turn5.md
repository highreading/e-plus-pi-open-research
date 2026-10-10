> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 5: the first nonzero cross-norm lift at $3$, and a global factorial-tail reduction

No decision on the irrationality of $e+\pi$ is obtained.

The new arithmetic result is an **exact first nonzero lift**, valid throughout the assigned growing-degree family:


$$
n=2001\cdot3^a,\qquad b=3^a,\qquad a\ge1.
$$


In the normalization of A5 turn 4, I obtain


$$
\boxed{\chi=v_3(\mathfrak C)=\frac{b+1}{2}.}
\tag{1}
$$


More precisely,


$$
\boxed{
3^{-(b+1)/2}\mathfrak C\equiv 2(-1)^a\pmod3.
}
\tag{2}
$$


Thus the previously unresolved cross contraction is nonzero at every assigned index, not merely eventually.

Combining this with the retained norm identity $v_3(\mathfrak D)=1$ gives the **actual reduced denominator**, after its final gcd:


$$
\boxed{
v_3(q_n)=n-\frac{b+13}{2}.
}
\tag{3}
$$


In particular, the second supplied control, which only established $\chi\ge4$ at $(n,b)=(18009,9)$, should lift to


$$
\chi=5,\qquad \mathfrak C\equiv486\pmod{729},
\qquad v_3(q_n)=17998.
$$



I also prove a same-family, all-prime factorial-tail factorization. It leads to an explicit, pivot-free, bounded integer recurrence for the **entire actual center and its final gcd**. It is not yet an asymptotically favorable bound for that gcd.

---

## 1. Exact setup and retained identities

Write


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
F(z)=4\arctan\frac{z}{2-z},\qquad
\ell=n+2,
$$


and retain the same positive falling metric


$$
\omega_j=(\ell)_{\!j}=\frac{\ell!}{(\ell-j)!},
\qquad
\Omega=\operatorname{diag}(\omega_0^2,\ldots,\omega_b^2).
$$



I use the exact endpoint-matched contact identities from turn 4:


$$
u=\lambda K D_b^{-1}\widetilde N^{-1}f^0,\qquad
v=e_0+K D_b^{-1}\widetilde N^{-1}(h^e+h^F),
\tag{4}
$$


where


$$
\lambda=\frac{(n!)^2}{2^n},\qquad
D_b=\operatorname{diag}(0!,1!,\ldots,(b-1)!),
\qquad K=Z(1+D)^{-n}.
$$


Thus $u$ has endpoint coordinates $(1,0)$, $v$ has endpoint coordinates $(0,1)$, and


$$
\sum_j u_j=0,\qquad \sum_jv_j=1.
$$



The divided contact matrix is


$$
\widetilde N_{ij}
=\sum_{s=0}^{\min(2n,n+i)}
a_s(n)(n+i)_{\!s}\binom{n+i-s}{j},
\qquad a_s(n)=[z^s]\phi(z)^n.
\tag{5}
$$


The two forcing columns are the complete ones:


$$
f^0_i=\frac{(n+i)!}{n!}J_i,\qquad
J_i=[t^n](1+2t+2t^2)^n(1+t)^i,
\tag{6}
$$


and


$$
h^e_i=\sum_s a_s(n)(n+i)_{\!s}\,\mathcal D_{2n+i-s},
\tag{7}
$$




$$
h^F_i=\sum_s a_s(n)(n+i)_{\!s}
       (2n+i-s)!\,\mathcal F_{2n+i-s},
\tag{8}
$$


with


$$
\mathcal D_m=m!\sum_{r=0}^m\frac1{r!},
\qquad
\mathcal F_m=[z^m]\frac{F(z)}{1-z}.
$$



Define the integer weighted reconstruction matrix


$$
\mathcal T
=\operatorname{diag}(\omega_j)KD_b^{-1}.
\tag{9}
$$


In divided coefficients, if $S$ is the upper shift and


$$
(\mathcal Zy)_j=j\,y_{j-1}-y_j,
$$


then


$$
\mathcal T
=\operatorname{diag}\!\binom{\ell}{j}\,
\mathcal Z(1+S)^{-n}.
\tag{10}
$$


In particular, all entries of $\mathcal T$ are integers. Explicitly, for $0\le j\le b$, $0\le r<b$,


$$
\mathcal T_{jr}
=\binom{\ell}{j}
\left[
j\binom{-n}{r-j+1}-\binom{-n}{r-j}
\right],
\tag{11}
$$


where a binomial coefficient with negative lower index is zero.

Put


$$
y=\widetilde N^{-1}f^0,\qquad
z=KD_b^{-1}y,
$$


and


$$
Z_w=\operatorname{diag}(\omega_j)z=\mathcal Ty,
\qquad
V_w=\operatorname{diag}(\omega_j)v.
$$


The contractions in question are


$$
\mathfrak D=Z_w^TZ_w,\qquad
\mathfrak C=Z_w^TV_w.
\tag{12}
$$



The previously derived unit reduction and norm calculation give


$$
\widetilde N\equiv P_b\pmod9,\qquad
(1+S)^{-n}\equiv I\pmod9,
\tag{13}
$$


where $(P_b)_{ij}=\binom ij$, and


$$
v_3(\mathfrak D)=1.
\tag{14}
$$


I do not rederive the saturation and norm calculation here. The new argument below identifies the complete cross contraction, including $h^F$, at its first nonzero scale.

---

## 2. An exact exponential-tail subtraction

The useful comparison is not an asymptotic expansion of $h^e$. It is an exact polynomial subtraction that respects the endpoint correction.

Let


$$
B'_0(z)=1+z+\cdots+z^{b-1},
\qquad
c^!_j=j!\quad(0\le j<b),
$$


and set


$$
x=(1+S)^n c^!.
\tag{15}
$$


Thus $D_b^{-1}x$ is the ordinary coefficient vector of
$(1+D)^nB'_0$.

Define the full residual column


$$
\rho=h^e+h^F-\widetilde N x.
\tag{16}
$$


The exponential part is exactly


$$
\rho^e_i
=\sum_s a_s(n)(n+i)_{\!s}
  \sum_{t=b}^{2n+i-s}(2n+i-s)_{\!t}.
\tag{17}
$$


Indeed,


$$
\frac{e^z}{1-z}-e^zB'_0(z)
=\frac{e^zz^b}{1-z},
$$


and


$$
m![z^m]\frac{e^zz^b}{1-z}
=\sum_{t=b}^m m_{\!t}.
$$


Applying the defining contact operator gives (17).

There is also an exact cancellation of the coordinate-zero endpoint:


$$
e_0+\mathcal T x
=\operatorname{diag}(\omega_j)\bigl(1+(z-1)B'_0(z)\bigr)
=\omega_b e_b.
$$


Consequently,


$$
\boxed{
V_w=\omega_b e_b+\mathcal T\widetilde N^{-1}\rho.
}
\tag{18}
$$


Both forcing columns and the endpoint term are retained in this identity.

This subtraction is the reason that the cross contraction has a much deeper valuation than the earlier modulo-$9$ argument alone detects.

---

## 3. First nonzero lift of the complete residual

Set


$$
k=v_3(n)=a+1,\qquad
s_b=v_3((b-1)!)=\frac{b-1-2a}{2},
$$


and


$$
\beta=k+s_b=\frac{b+1}{2}.
\tag{19}
$$



### 3.1 A split falling-product bound

A summand in (17), before multiplication by $a_s(n)$, contains


$$
(n+i)_{\!s}(2n+i-s)_{\!t},\qquad t\ge b.
\tag{20}
$$


Index the factors by $r=0,\ldots,s+t-1$. They are


$$
n+i-r\quad(r<s),\qquad
2n+i-r\quad(r\ge s).
$$



Because $0\le i<b=3^a$, the first $b$ factors contain the factor indexed by $r=i$. That factor is either $n$ or $2n$, and has valuation $k$. For every other $r$ among the first $b$ factors,


$$
v_3(n+i-r)=v_3(2n+i-r)=v_3(i-r),
$$


since $0<|i-r|<3^a$, whereas $3^{a+1}\mid n$.

Therefore the first $b$ factors have total valuation


$$
k+v_3(i!)+v_3((b-1-i)!).
$$


Lucas's theorem gives


$$
\binom{b-1}{i}\not\equiv0\pmod3,
$$


so


$$
v_3(i!)+v_3((b-1-i)!)=s_b.
$$


Hence


$$
v_3\!\left((n+i)_{\!s}(2n+i-s)_{\!t}\right)\ge\beta.
\tag{21}
$$



If $s+t\ge b+3$, the next three factors include a multiple of $3$, regardless of where the split occurs. Thus


$$
s+t\ge b+3
\quad\Longrightarrow\quad
v_3\!\left((n+i)_{\!s}(2n+i-s)_{\!t}\right)\ge\beta+1.
\tag{22}
$$



For $s=1,2$, the coefficient itself supplies an additional factor of $3$:


$$
a_1(n)=-n,\qquad a_2(n)=\frac{n^2}{2}.
\tag{23}
$$


It follows that, modulo $3^{\beta+1}$, only the terms


$$
s=0,\qquad t=b,b+1,b+2
$$


can contribute to $\rho^e_i$. Therefore


$$
\frac{\rho^e_i}{3^\beta}
\equiv
\frac{(2n+i)_{\!b}}{3^\beta}
\left[
1+(2n+i-b)+(2n+i-b)(2n+i-b-1)
\right]\pmod3.
\tag{24}
$$



### 3.2 The normalized length-$b$ product is independent of $i$

Let


$$
U_a=\frac{(b-1)!}{3^{s_b}}\pmod3.
$$


For $0\le i<b$,


$$
\frac{(2n+i)_{\!b}}{3^\beta}
\equiv
\frac{2n}{3^k}\,
(-1)^i\,
\frac{i!(b-1-i)!}{3^{s_b}}
\pmod3.
$$


But


$$
\binom{b-1}{i}\equiv(-1)^i\pmod3.
$$


Thus


$$
\boxed{
\frac{(2n+i)_{\!b}}{3^\beta}
\equiv r_a:=\frac{2n}{3^k}U_a\pmod3,
}
\tag{25}
$$


uniformly over every row.

The unit factorial satisfies


$$
U_a=-U_{a-1}\pmod3,\qquad U_0=1.
$$


Indeed, the nonmultiples of $3$ in $1,\ldots,3^a-1$ form $3^{a-1}$ pairs whose products are $-1$ modulo $3$; the multiples of $3$, after removing their powers of $3$, contribute $U_{a-1}$. Hence


$$
U_a=(-1)^a\pmod3.
$$


Since


$$
n/3^k=667\equiv1\pmod3,
$$


we obtain


$$
\boxed{r_a=2(-1)^a\pmod3.}
\tag{26}
$$



The bracket in (24) is


$$
1+i+i(i-1)\equiv\mathcal D_i\pmod3.
$$


The last congruence follows directly from


$$
\mathcal D_i=\sum_{r=0}^i i_{\!r},
$$


because every term with $r\ge3$ is divisible by $3$.

Therefore


$$
\boxed{
3^{-\beta}\rho^e_i\equiv r_a\mathcal D_i\pmod3.
}
\tag{27}
$$



### 3.3 The complete logarithmic forcing is beyond this scale

Every factorial index $m=2n+i-s$ in $h^F$ satisfies


$$
n\le m\le 2n+b-1.
$$


The exact Taylor coefficients of $F$ give


$$
v_3(m!\mathcal F_m)
\ge v_3(m!)-\lfloor\log_3m\rfloor.
$$


Thus


$$
v_3(h^F_i)
\ge \frac{n-7}{2}-(a+7).
\tag{28}
$$


Here


$$
v_3(n!)=\frac{n-7}{2},
$$


and


$$
\left\lfloor\log_3(2n+b-1)\right\rfloor=a+7.
$$



The difference between the right side of (28) and $\beta+1$ is


$$
\left[\frac{2001b-7}{2}-a-7\right]-\frac{b+3}{2}
=1000b-a-12>0
$$


for every $a\ge1$. Therefore


$$
h^F\equiv0\pmod{3^{\beta+1}}.
\tag{29}
$$



Combining (27) and (29) proves a statement about the **whole** residual:


$$
\boxed{
\rho\in3^\beta\mathbb Z_3^b,\qquad
3^{-\beta}\rho_i\equiv r_a\mathcal D_i\pmod3.
}
\tag{30}
$$



---

## 4. The weighted $Q$-column and the cross contraction

Modulo $3$,


$$
\widetilde N^{-1}\equiv P_b^{-1}.
$$


The inverse Pascal transform of $(\mathcal D_i)$ is $(i!)$:


$$
\mathcal D_i=\sum_{j=0}^i\binom ij j!.
$$


Hence (30) gives


$$
3^{-\beta}\widetilde N^{-1}\rho
\equiv r_a c^!\pmod3.
\tag{31}
$$



Also $(1+S)^{-n}\equiv I\pmod3$. The divided multiplication operator $\mathcal Z$ sends the factorial vector to


$$
(\mathcal Zc^!)_0=-1,\qquad
(\mathcal Zc^!)_j=0\quad(1\le j<b),
\qquad
(\mathcal Zc^!)_b=b!.
$$


The last entry vanishes modulo $3$. Thus


$$
3^{-\beta}\mathcal T\widetilde N^{-1}\rho
\equiv-r_a e_0\pmod3.
\tag{32}
$$



The terminal falling factorial has the same depth:


$$
v_3(\omega_b)=\beta.
$$


The same normalized-product calculation, now with $n+2$ in place of $2n+i$, gives


$$
\frac{\omega_b}{3^\beta}\equiv(-1)^a\pmod3.
\tag{33}
$$


Using $-r_a=-2(-1)^a\equiv(-1)^a\pmod3$, equations (18), (32), and (33) yield


$$
\boxed{
3^{-\beta}V_w\equiv(-1)^a(e_0+e_b)\pmod3.
}
\tag{34}
$$



This is stronger than a valuation of the cross contraction: it gives the first nonzero lift of the entire actual weighted $Q$-column.

For the $P$-column, the retained reduction gives


$$
(Z_w)_0\equiv-J_0\pmod3,\qquad
(Z_w)_b\equiv0\pmod3.
\tag{35}
$$


The constant-term digit factorization of


$$
J_0=\operatorname{CT}(t^{-1}+2+2t)^n
$$


gives $J_0\equiv1\pmod3$. Indeed, the nonzero ternary digits of


$$
2001=2202010_3
$$


are three $2$'s and one $1$, and the corresponding constant-term factors are all $2$ modulo $3$. Multiplication by $3^a$ only appends zero digits.

Taking the scalar product of (34) with $Z_w$ therefore gives


$$
\frac{\mathfrak C}{3^\beta}
\equiv(-1)^a\bigl((Z_w)_0+(Z_w)_b\bigr)
\equiv-(-1)^a
=2(-1)^a\pmod3.
$$


The residue is nonzero. This proves (1) and (2).

### Finite controls versus the theorem

The supplied controls are consistent with this proof:

- $a=1$: $\beta=2$, and $36/9\equiv1=2(-1)\pmod3$.
- $a=2$: $\beta=5$, so vanishing modulo $81$ is expected but does not resolve the valuation.

The infinite statement above comes from (17)–(35), not from those two controls.

---

## 5. Translation to the actual denominator and evaluated gcd

The actual rational center remains


$$
c_n=\frac{\mathfrak C}{\lambda\mathfrak D}.
\tag{36}
$$


Since


$$
v_3(\lambda)=2v_3(n!)=n-7,\qquad
v_3(\mathfrak D)=1,\qquad
v_3(\mathfrak C)=\frac{b+1}{2},
$$


and


$$
\frac{b+1}{2}<n-6
$$


throughout the assigned domain, rational reduction gives


$$
\boxed{
v_3(q_n)
=n-6-\frac{b+1}{2}
=n-\frac{b+13}{2}.
}
\tag{37}
$$



For explicit compatibility with the final primitive Gram gcd, let $d_B$ be the least common denominator of the actual two-column lift and put


$$
d=v_3(d_B).
$$


Let $N_B=d_B[u,v]$ be its primitive integer lift, and retain


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},\qquad
g_B=\gcd(A_B,|H_B|).
$$


Then


$$
v_3(A_B)=2d+4v_3(n!)+1,
$$




$$
v_3(H_B)=2d+2v_3(n!)+\frac{b+1}{2}.
$$


The second is strictly smaller, so


$$
\boxed{
v_3(g_B)
=2d+2v_3(n!)+\frac{b+1}{2}.
}
\tag{38}
$$


Subtracting (38) from $v_3(A_B)$ gives precisely (37).

Thus the norm depth has not been substituted for the denominator. The evaluated cross contraction determines the last cancellation.

---

## 6. A new same-family global factorial-tail factor

The exact subtraction in Section 2 also has an all-prime consequence. This does not depend on $b$ being a power of $3$.

### Global factorial-tail lemma

For the same endpoint-matched contact construction, if


$$
n\ge2b\ge2,
$$


then


$$
\boxed{
\rho=b!\,r,\qquad r\in\mathbb Z[1/2]^b.
}
\tag{39}
$$


Consequently,


$$
\boxed{
V_w=b!\left[
\binom{n+2}{b}e_b+\mathcal T\widetilde N^{-1}r
\right].
}
\tag{40}
$$



#### Proof

For the exponential part, every term in (17) contains


$$
(2n+i-s)_{\!t},\qquad t\ge b.
$$


This falling factorial is divisible by $b!$. Since the remaining coefficients belong to $\mathbb Z[1/2]$,


$$
\rho^e/b!\in\mathbb Z[1/2]^b.
$$



For the logarithmic part, write


$$
[z^r]F(z)=\frac{2c_{r-1}}r,\qquad c_{r-1}\in\mathbb Z[1/2].
$$


It suffices to show that $m!/(r\,b!)$ is integral at every odd prime for $1\le r\le m$, whenever $m\ge2b$.

For each prime power $p^j\le m$,


$$
\left\lfloor\frac m{p^j}\right\rfloor
-\left\lfloor\frac b{p^j}\right\rfloor\ge1.
$$


If $p^j>b$, this is immediate; if $p^j\le b$, use $m\ge2b$. Summing over $j$ gives


$$
v_p(m!)-v_p(b!)\ge\lfloor\log_pm\rfloor\ge v_p(r).
$$


Hence $m!\mathcal F_m/b!\in\mathbb Z[1/2]$.

Every $m$ in (8) is at least $n\ge2b$, proving (39). Finally, $\omega_b=b!\binom{n+2}{b}$, so (18) gives (40). ∎

This is a uniform factorial factor in the **actual weighted $Q$-column**, including the logarithmic forcing and the endpoint term. It is not a moving-prime chart.

At an odd prime dividing $n$, where $\widetilde N$ is a local unit matrix, it immediately yields


$$
V_w\in p^{v_p(b!)}\mathbb Z_p^{b+1}.
$$


For the assigned family this applies, at the same indices, to $3,23,29$. At $3$, Sections 3–4 identify the additional factor and the exact first nonzero lift. At $23$ and $29$, this statement alone does not identify the cross-norm cancellation.

---

## 7. Bounded recursive reduction of the entire center's content

The preceding factorization provides an explicit global reduction which cancels the contact determinant and the proved factorial factor **before** taking the final gcd.

This is a computation-free identity and a bounded exact algorithm. It is not an estimate asserting that the remaining gcd is large.

### 7.1 Integer data

Remain on the assigned family. Set


$$
A=2^n\widetilde N\in M_b(\mathbb Z),\qquad
\Delta=\det A\ne0.
$$


Choose the explicit dyadic clearer


$$
L=2^{3n+2b},
\qquad R=Lr\in\mathbb Z^b.
\tag{41}
$$


This is deliberately nonminimal. To check sufficiency, the coefficients $a_s(n)$ have denominators dividing $2^n$, the coefficients $c_j$ of $1/\phi$ have denominators dividing $2^j$, the largest factorial index is $2n+b-1$, and division by $b!$ can add at most $v_2(b!)<b$ to the dyadic denominator. Thus (41) clears every term.

Define


$$
U=\mathcal T\,\operatorname{adj}(A)f^0\in\mathbb Z^{b+1},
\tag{42}
$$




$$
V=L\Delta\binom{n+2}{b}e_b
  +2^n\mathcal T\,\operatorname{adj}(A)R
  \in\mathbb Z^{b+1}.
\tag{43}
$$


Then exactly


$$
Z_w=\frac{2^n}{\Delta}U,\qquad
V_w=\frac{b!}{L\Delta}V.
\tag{44}
$$



Let


$$
A_0=U^TU>0,\qquad H_0=U^TV.
\tag{45}
$$


The cross-norm theorem proves $H_0\ne0$ on every assigned index. Substitution into (36) gives


$$
c_n
=\frac{b!\,H_0}{L(n!)^2A_0}.
$$


Because $b!\mid(n!)^2$, put


$$
K_0=\frac{(n!)^2}{b!}\in\mathbb Z_{>0}.
$$


We obtain the global identity


$$
\boxed{
c_n=\frac{H_0}{LK_0A_0}.
}
\tag{46}
$$



The actual final reduction is therefore


$$
\boxed{
g_0=\gcd(LK_0A_0,|H_0|),\qquad
p_n=\frac{H_0}{g_0},\qquad
q_n=\frac{LK_0A_0}{g_0}.
}
\tag{47}
$$


All common content of $U$, all content of $V$, and every additional cancellation in their evaluated scalar product are included in this gcd. No coefficient gcd is declared to equal it.

The determinant $\Delta^2$ has canceled identically, and the factor $b!$ proved in Section 6 has reduced the factorial scalar from $(n!)^2$ to $(n!)^2/b!$.

### 7.2 A pivot-free recurrence for both adjugate columns

The recurrence can be made deterministic throughout the family.

Since


$$
\widetilde N\equiv P_b\pmod3,
$$


every leading principal minor of $A$ is nonzero modulo $3$, hence nonzero over $\mathbb Q$. Thus fraction-free elimination on the augmented integer matrix


$$
[A\mid f^0\mid R]
$$


requires no pivot search.

Starting with previous pivot $d_{-1}=1$, at step $r$ update every lower-right entry, including both forcing columns, by


$$
B^{(r+1)}_{ij}
=
\frac{
B^{(r)}_{rr}B^{(r)}_{ij}
-B^{(r)}_{ir}B^{(r)}_{rj}
}{d_{r-1}},
\qquad i,j>r,
\tag{48}
$$


and set $d_r=B^{(r)}_{rr}$. The divisions are exact integer divisions: the determinant identity for bordered minors gives (48), and induction identifies the successive pivots with the leading principal determinants.

After the $b-1$ elimination steps, let $E$ be the resulting upper-triangular block and $F^{(1)},F^{(2)}$ its two transformed forcing columns. The last pivot is $\Delta$.

For either forcing column, compute $X=\Delta A^{-1}f$ by backward recurrence


$$
X_{b-1}=F_{b-1},
$$




$$
\boxed{
X_i=
\frac{\Delta F_i-\sum_{j=i+1}^{b-1}E_{ij}X_j}{E_{ii}},
\qquad i=b-2,\ldots,0.
}
\tag{49}
$$


These divisions are again exact, because the unique result is $\operatorname{adj}(A)f\in\mathbb Z^b$.

Equations (48)–(49) compute both vectors needed in (42)–(43). Integer scalar products and the Euclidean algorithm then compute precisely the final gcd in (47), without prime factorization.

This is a bounded recursive reduction of the whole center's content:

- coefficient sums have explicitly bounded ranges;
- elimination has $b-1$ stages;
- back substitution has $b$ stages;
- the last operation is a gcd of two explicitly computed integers.

For a literal bound on the gcd stage, let $H\ge2$ be the maximum of


$$
L,\ K_0,\ 2^n,\ \binom{n+2}{b},
$$


and the absolute values of all entries of $A,f^0,R,\mathcal T$. By the determinant expansion,


$$
|U_j|\le b\,b!\,H^{b+1},\qquad
|V_j|\le(b+1)b!\,H^{b+2}.
$$


Consequently


$$
LK_0A_0\le(b+1)b^2(b!)^2H^{2b+4},
$$




$$
|H_0|\le(b+1)^2b(b!)^2H^{2b+3}.
$$


The Euclidean algorithm takes fewer than twice the base-$2$ logarithm of one plus the larger of these bounds, up to an absolute additive constant.

This reduction is exact and uniform in the growing dimension. Its limitation is quantitative: it does not yet prove a favorable asymptotic bound for the gcd in (47).

---

## 8. Whole error and the aggregate limitation

The exact $3$-part is now


$$
v_3(q_n)=
\left(1-\frac1{4002}\right)n-\frac{13}{2}.
$$


Thus


$$
\log q_n
=
\left[\left(1-\frac1{4002}\right)n-\frac{13}{2}\right]\log3
+\log q_{n,3'},
\tag{50}
$$


where $q_{n,3'}$ is the actual prime-to-$3$ part.

The contribution at $3$ is known both above and below. Its linear rate


$$
\left(1-\frac1{4002}\right)\log3
$$


is smaller than the inherited full signed error rate


$$
\tau_c=
\left(2+\frac1{2001}\right)\log(1+\sqrt2).
$$


Therefore this one-prime theorem neither proves primitive shrinking nor excludes the family.

At the dependency status of the supplied proportional signed-rate theorem, eventually


$$
\epsilon_n=c_n-(e+\pi)\ne0,\qquad
\log|\epsilon_n|=-\tau_cn+o(n).
$$


The complete primitive evaluated error is


$$
\boxed{
L_n=q_n(e+\pi)-p_n=-q_n\epsilon_n\ne0.
}
\tag{51}
$$


Since all assigned $n$ are odd, the supplied sign theorem gives $\epsilon_n>0$ eventually, hence $L_n<0$ eventually.

The exact aggregate arithmetic object is now concretely


$$
\boxed{
\gcd\!\left(
L\frac{(n!)^2}{b!}\,U^TU,\,
|U^TV|
\right),
}
\tag{52}
$$


with $U,V$ produced by (41)–(49). The new global tail factor is a genuine cancellation, but no estimate established here makes the prime-to-$3$ contribution in (50) small enough.

There is no demonstrated insufficient-balance failure for this center sequence.

---

## 9. Independent review of A3 and the primorial consequence

### 9.1 Raw normalization and residue-zero unit: pass

The raw identities


$$
V_k=(k+1)\widetilde V_k,\qquad
Q_k=(k+1)\widetilde Q_k,\qquad
\mathscr D_k=(k+1)\widetilde D_k
$$


are consistent with the contiguous formulas. Keeping $k+1$ inside the filter is essential and is done correctly.

The residue-zero unit can also be checked directly in the supplied normalization. The Rodrigues/partial-exponential identities give


$$
\mathcal A_k
=\sum_s(k)_{\!s}a_s(k)\,\mathcal D_{2k-s},
$$




$$
\mathcal B_k
=\frac1{k+1}
\sum_s(k+1)_{\!s}a_s(k+1)\,\mathcal D_{2k+2-s}.
$$


At $k\equiv0\pmod p$, $p$ odd, only $s=0$ survives in the first expression and only $s=0,1$ in the second. Hence


$$
\mathcal A_k\equiv1,\qquad
\mathcal B_k\equiv\mathcal D_2-\mathcal D_1=3\pmod p.
$$


Together with the derivative residues displayed by A3, this gives


$$
\widetilde V_k\equiv4\pmod p.
$$


The division by $k+1$ is legal here because the residue is zero, not $p-1$. Thus the required **raw** $V_N$ is a unit at every odd $p\mid N$.

### 9.2 Unique last term, small indices, final gcd: pass

A3's strict valuation separation is valid uniformly over odd $p\mid N$, $p\nmid a$. The coordinator's sharper small-index check is also valid:

- $k\le p-2$: no odd-prime moment denominator is present;
- $k=p-1$: the factor $k+1=p$ cancels the possible one-level second-kind pole;
- $k\ge p$: $2v_p(k!)>\lfloor\log_p(k+1)\rfloor$.

Thus every earlier weighted term has valuation strictly greater than $-4v_p(N!)$, while the last term has exactly that valuation. The fourth factorial scale is retained correctly.

On $\mathcal J\ne0$,


$$
v_p(q)=
\max\{0,v_p(\mathcal J)-v_p(\mathcal H)\}
\ge2v_p(N!).
$$


This is a statement after the full cross-index endpoint gcd.

### 9.3 Eventual nonvanishing: pass

The eventual same sign of all $J_k$, together with positive filter weights, gives $\mathcal J\ne0$ uniformly in $m$ once $n$ is above the stated threshold.

The rational/irrational case split is logically sound. Once the actual reduced denominators tend to infinity:

- an irrational $e+\pi$ equals none of the rational centers;
- a rational $e+\pi$ has one fixed reduced denominator and therefore cannot equal the centers eventually.

This proves eventual nonvanishing of the entire filtered error without deciding the target.

### 9.4 Odd-primorial consequence: pass, for fixed filter parameters

Fix the positive integer $a$ occurring in the last filter weight. Define


$$
N_x=\prod_{\substack{p\le x\\p\text{ odd}\\p\nmid a}}p.
$$


The local theorem is uniform in $p$, so it may be summed over all these primes at the same index $N_x$.

Legendre's formula gives, uniformly for $p\le N$,


$$
v_p(N!)=\frac{N}{p-1}
+O\!\left(\frac{\log N}{\log p}\right).
$$


After multiplication by $\log p$ and summation,


$$
\log q\ge
2N_x\sum_{\substack{p\le x\\p\text{ odd}\\p\nmid a}}
\frac{\log p}{p-1}
-O(\pi(x)\log N_x).
$$


For fixed $a$, only finitely many primes are omitted. The PNT and partial summation give


$$
\log N_x=(1+o(1))x,\qquad
\sum_{\substack{p\le x\\p\text{ odd}\\p\nmid a}}
\frac{\log p}{p-1}
=(1+o(1))\log x.
$$


The error is


$$
O(x^2/\log x)=o(N_x\log x),
$$


and


$$
\log\log N_x=\log x+o(1).
$$


Therefore


$$
\boxed{
\liminf_{x\to\infty}
\frac{\log q}{N_x\log\log N_x}\ge2.
}
\tag{53}
$$



The qualification “fixed $a$” matters; arbitrary $a=a(x)$ could remove a growing set of primes. With fixed filter parameters, the claimed consequence passes.

It is a lower bound. Without an appropriate lower estimate for the complete signed error, it does not establish shrinking or exclude the filtered route.

---

# Concluding ledger

## (1) New result and proof status

**Proved by the explicit arithmetic derivation above, using the retained exact contact and norm identities:**

1. On
   

$$
n=2001\cdot3^a,\quad b=3^a,\quad a\ge1,
$$


   the complete cross contraction has the exact first nonzero lift
   

$$
\boxed{
   \chi=\frac{b+1}{2},\qquad
   3^{-\chi}\mathfrak C\equiv2(-1)^a\pmod3.
   }
$$



2. The entire weighted $Q$-column satisfies
   

$$
\boxed{
   3^{-(b+1)/2}V_w\equiv(-1)^a(e_0+e_b)\pmod3.
   }
$$



3. The actual primitive denominator is
   

$$
\boxed{
   v_3(q_n)=n-\frac{b+13}{2},
   }
$$


   with the corresponding evaluated final-gcd depth given in (38).

4. For the same matched construction with $n\ge2b$, the exact residual has the global factor
   

$$
\rho\in b!\,\mathbb Z[1/2]^b.
$$



5. Equations (41)–(49) give a bounded, pivot-free integer recurrence for the entire actual center and its final gcd, retaining both forcing columns, all factorial scales, the same metric, and the endpoint correction.

6. A3's raw-unit, uniform last-term, final-gcd, and eventual-nonvanishing arguments pass this review. The primorial consequence passes for fixed filter parameters.

The whole-error asymptotic retains the supplied analytic theorem's dependency status. No irrationality conclusion is asserted.

## (2) Exact remaining bottleneck

The local cross-norm bottleneck at $3$ is resolved.

The remaining same-family arithmetic bottleneck is quantitative control of the evaluated integer gcd


$$
\gcd\!\left(
L\frac{(n!)^2}{b!}\,U^TU,\,
|U^TV|
\right)
$$


beyond its now-known $3$-part. The bounded recurrence computes that gcd exactly at each index but does not yet control its asymptotic size.

In particular, neither a favorable aggregate denominator bound nor an actual primitive-balance failure has been proved.

## (3) Bounded exact computation request

A new, narrowly targeted audit would test the predicted first lift, not repeat the modulo-$9$ controls.

**Inputs**


$$
(a,n,b)=(2,18009,9),\qquad (3,54027,27).
$$



**Requested moduli**


$$
3^{6}=729,\qquad 3^{15}=14348907,
$$


respectively.

**Expected verifiable outputs**

- The complete residual $\rho=h^e+h^F-\widetilde N(1+S)^n(j!)$, confirming
  

$$
\rho/3^{(b+1)/2}\equiv2(-1)^a(\mathcal D_i)_{i=0}^{b-1}\pmod3.
$$


- The normalized weighted $Q$-column:
  

$$
V_w/3^{(b+1)/2}\equiv(-1)^a(e_0+e_b)\pmod3.
$$


- The full cross contraction:
  

$$
\begin{array}{c|c|c|c}
  a&\chi&\mathfrak C\text{ modulo }3^{\chi+1}&v_3(q_n)\\ \hline
  2&5&486\pmod{729}&17998\\
  3&14&4782969\pmod{14348907}&54007
  \end{array}
$$


- A certificate that the complete logarithmic forcing is zero at the requested modulus, using its proved factorial valuation bound rather than omitting it by convention.

These would be finite normalization audits only. They would not prove the missing aggregate bound.
