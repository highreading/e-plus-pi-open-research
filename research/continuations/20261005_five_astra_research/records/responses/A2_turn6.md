> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 turn 6: split-product theorem at $p\ge 5$, its $23$-specialization, and a same-index carry reduction

No rationality or irrationality decision for $e+\pi$ follows from this report.

The main new arithmetic result is a split-product theorem for the **actual complete center** at


$$
b=p^a,\qquad n=Mp^a,\qquad p\ge5.
$$


Under an explicit constant-term unit condition, it determines the weighted $Q$-column, the first nonzero complete cross contraction, the local least $B$-lift denominator, and the **final reduced center denominator**.

For the requested specialization,


$$
p=23,\qquad M=2001,\qquad a\ge1,
$$


the unit condition is proved using Legendre reflection. The resulting exact law is


$$
\boxed{
v_{23}(q_n)=\frac{4001\,23^a-63}{22}.
}
\tag{1}
$$


This concerns $n=2001\,23^a$, not $n=2001\,3^a$, and therefore cannot be added to the established $3$-part.

At the **original indices**


$$
n=2001\,3^a,\qquad b=3^a,
$$


I obtain a different, non-$p$-power reduction. In particular, the complete weighted $Q$-column has an additional factor of $23$ beyond $b!$ on the specified infinite class


$$
\boxed{
a\not\equiv0,7\pmod{11}.
}
\tag{2}
$$


This is a column-divisibility theorem, **not** an actual-$q$ bound. I also give explicit first-digit formulas for the norm and divided cross contraction and an all-depth, finite carry computation for the remaining arithmetic.

---

## 1. Cross-review of the global tail and integral strengthening

I use the supplied contact identities, with


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
\lambda=\frac{(n!)^2}{2^n},\qquad
\ell=n+2,
$$


and the actual falling weights


$$
\omega_j=(n+2)_{\!j},\qquad
\Omega=\operatorname{diag}(\omega_j^2).
$$



Write


$$
u=\lambda z,\qquad
Z_w=\operatorname{diag}(\omega_j)z,\qquad
V_w=\operatorname{diag}(\omega_j)v,
$$


where $u,v$ are the two actual $B$-lift columns. Thus


$$
\mathfrak D=Z_w^TZ_w,\qquad
\mathfrak C=Z_w^TV_w,\qquad
c_n=\frac{\mathfrak C}{\lambda\mathfrak D}.
\tag{3}
$$



### 1.1 The integral strengthening passes

Let


$$
a_s(n)=[z^s]\phi(z)^n,\qquad
\alpha_s(n,i)=a_s(n)(n+i)_{\!s}.
$$


The denominator of $a_s(n)$ divides $2^{\lfloor s/2\rfloor}$, while


$$
s!\mid(n+i)_{\!s},\qquad v_2(s!)\ge\lfloor s/2\rfloor.
$$


Hence $\alpha_s(n,i)\in\mathbb Z$.

For $s\ge1$, the exact identity


$$
\alpha_s(n,i)
=n(s-1)!\binom{n+i}{s}
[z^{s-1}]\phi'(z)\phi(z)^{n-1}
$$


has an integral factor after $n$: the remaining dyadic denominator divides
$2^{\lfloor(s-1)/2\rfloor}$, which $(s-1)!$ clears. Consequently


$$
\boxed{\widetilde N=B(n)+nC,\qquad C\in M_b(\mathbb Z).}
\tag{4}
$$


Here $B(n)_{ij}=\binom{n+i}{j}$, and its Pascal–Toeplitz factorization has determinant one.

The complete logarithmic coefficients are also even integers. Indeed, if


$$
\phi^{-1}=\sum_{r\ge0}c_rz^r,
$$


then $c_r$ has denominator dividing $2^{\lfloor r/2\rfloor}$, and


$$
m!\mathcal F_m
=\sum_{r=1}^m 2\frac{m!}{r}c_{r-1}.
$$


Since $m!/r$ is divisible by $(r-1)!$, each summand is an even integer. All indices here satisfy $1\le r\le m$; no negative-factorial convention is involved.

Thus (4), and local invertibility at every prime dividing $n$, hold over the claimed integral domain.

### 1.2 A5’s complete $b!$-tail factor passes

Retain the exact subtraction


$$
\rho=h^e+h^F-\widetilde N(1+S)^n(j!)_{j<b}.
$$


Its exponential part is


$$
\rho_i^e
=\sum_s\alpha_s(n,i)
 \sum_{t=b}^{2n+i-s}(2n+i-s)_{\!t}.
\tag{5}
$$


Every exponential summand is divisible by $b!$.

For the logarithmic part, when $m\ge2b$,


$$
v_p(m!)-v_p(b!)\ge\lfloor\log_pm\rfloor\ge v_p(r)
\quad(1\le r\le m).
$$


The first inequality follows by counting at least one additional multiple of each $p^j\le m$ between $b+1$ and $m$. Therefore


$$
\boxed{
\rho=b!r,\qquad r\in\mathbb Z[1/2]^b,\qquad n\ge2b.
}
\tag{6}
$$


The actual endpoint term is retained in


$$
\boxed{
V_w=\omega_be_b+\mathcal T\widetilde N^{-1}\rho
=b!\left[\binom{n+2}{b}e_b+\mathcal T\widetilde N^{-1}r\right].
}
\tag{7}
$$



A5’s subsequent global center reduction also passes. In its notation,


$$
Z_w=\frac{2^n}{\Delta}U,\qquad
V_w=\frac{b!}{L\Delta}V
$$


gives exactly


$$
c_n=\frac{U^TV}{L((n!)^2/b!)\,U^TU}.
$$


Thus the final gcd is indeed


$$
\gcd\!\left(L\frac{(n!)^2}{b!}U^TU,\ |U^TV|\right).
$$


The determinant and factorial cancellations are legitimate. They do not themselves estimate that evaluated gcd.

---

## 2. General split-product theorem

Let $p\ge5$, $a\ge1$, and


$$
b=p^a,\qquad n=Mb,\qquad M\ge2.
$$


Put


$$
h=v_p(M),\qquad k=a+h,\qquad
F_n=v_p(n!),\qquad F_b=v_p(b!),
$$


and


$$
\beta=F_b+h
      =k+v_p((b-1)!).
\tag{8}
$$


Define


$$
J_0=\operatorname{CT}(t^{-1}+2+2t)^n,
\qquad
U_a=\frac{(b-1)!}{p^{v_p((b-1)!)}}\pmod p,
$$


and


$$
w=\frac{n}{p^k}U_a\pmod p.
\tag{9}
$$



Assume


$$
J_0\not\equiv0\pmod p
\tag{10}
$$


and the explicit whole-logarithmic-forcing separation


$$
F_n-\lfloor\log_p(2n+b-1)\rfloor\ge\beta+1.
\tag{11}
$$



### Theorem

For the actual factorial $B$-metric center with $m_w=1$:

1. $\widetilde N$ is invertible, and
   

$$
\mathfrak D\equiv6J_0^2\pmod p,\qquad v_p(\mathfrak D)=0.
   \tag{12}
$$



2. The complete weighted $Q$-column satisfies
   

$$
\boxed{
   p^{-\beta}V_w\equiv-2w\,e_0+w\,e_b\pmod p.
   }
   \tag{13}
$$



3. The complete cross contraction satisfies
   

$$
\boxed{
   p^{-\beta}\mathfrak C\equiv2wJ_0\pmod p,
   \qquad v_p(\mathfrak C)=\beta.
   }
   \tag{14}
$$


   In particular, $\mathfrak C\ne0$.

4. The actual two-column $B$-lift is $p$-integral. Its least common denominator $d_B$ satisfies
   

$$
v_p(d_B)=0.
   \tag{15}
$$



5. With the final primitive Gram contraction
   

$$
A_B=d_B^2u^T\Omega u,\qquad
   H_B=d_B^2u^T\Omega v,\qquad
   g_B=\gcd(A_B,|H_B|),
$$


   one has
   

$$
v_p(A_B)=4F_n,\qquad
   v_p(H_B)=2F_n+\beta,
$$


   and hence
   

$$
\boxed{
   v_p(g_B)=2F_n+\beta,\qquad
   v_p(q_n)=2F_n-\beta.
   }
   \tag{16}
$$



The norm condition is explicitly $6J_0^2\in\mathbb F_p^\times$. For $p\ge5$, it follows from (10). This is precisely where the exceptional $p=3$ norm does **not** transfer unchanged.

### 2.1 Unit contact reduction and the weighted $P$-column

For $1\le r<b=p^a$,


$$
v_p\binom nr\ge k-v_p(r)\ge1.
$$


The same estimate holds for $\binom{-n}{r}$. Therefore, in the full growing dimension,


$$
\widetilde N\equiv P_b\pmod p,\qquad
(1+S)^{-n}\equiv I\pmod p.
\tag{17}
$$



Let $R(t)=1+2t+2t^2$. Frobenius gives


$$
R(t)^n\equiv R(t^b)^M\pmod p.
$$


For $i<b$, only the constant coefficient of $(1+t)^i$ can contribute to the required coefficient of degree $n$. Hence $J_i\equiv J_0\pmod p$, and


$$
f_i^0\equiv i!J_0\pmod p.
$$


The first three inverse-Pascal coordinates are therefore


$$
(t_0^P,t_1^P,t_2^P)\equiv(J_0,0,J_0)\pmod p.
$$


After the actual weighted reconstruction, they become


$$
(Z_{w,0},Z_{w,1},Z_{w,2})
\equiv(-J_0,2J_0,-J_0)\pmod p.
\tag{18}
$$



For $3\le j<b$, Lucas’s theorem gives $\binom{n+2}{j}\equiv0\pmod p$. At $j=b$, the divided multiplication contributes the additional factor $b$, so $Z_{w,b}\equiv0\pmod p$ as well. This proves (12).

### 2.2 The complete split-product tail

Consider a term of (5) with $t\ge b$:


$$
(n+i)_{\!s}(2n+i-s)_{\!t},\qquad 0\le i<b.
$$


Index its factors by $r=0,\ldots,s+t-1$. They are


$$
n+i-r\quad(r<s),\qquad
2n+i-r\quad(r\ge s).
$$



Among the first $b$ factors, the one with $r=i$ is either $n$ or $2n$, of valuation $k$. Every other factor has the valuation of $i-r$, since


$$
0<|i-r|<p^a,\qquad p^a\mid n.
$$


Thus the first $b$ factors have valuation


$$
k+v_p(i!)+v_p((b-1-i)!)
=k+v_p((b-1)!)=\beta.
\tag{19}
$$


The equality uses $\binom{p^a-1}{i}\in\mathbb Z_p^\times$.

If $s+t\ge b+p$, the next $p$ factors contain another multiple of $p$, independently of the split. Such terms vanish modulo $p^{\beta+1}$.

If $1\le s<p$, the coefficient identity


$$
s\,a_s(n)=n[z^{s-1}]\phi'\phi^{n-1}
$$


gives $p\mid a_s(n)$. Consequently the only surviving terms are


$$
s=0,\qquad t=b,b+1,\ldots,b+p-1.
\tag{20}
$$



The normalized initial product is independent of $i$:


$$
\frac{(2n+i)_{\!b}}{p^\beta}
\equiv 2\frac{n}{p^k}U_a=2w\pmod p.
\tag{21}
$$


Indeed, the signs in $i!(b-1-i)!$ cancel those in
$\binom{b-1}{i}\equiv(-1)^i\pmod p$.

It follows that


$$
p^{-\beta}\rho_i^e
\equiv2w\sum_{d=0}^{p-1}(i)_{\!d}
\equiv2w\,\mathcal D_i\pmod p,
\tag{22}
$$


where $\mathcal D_i=\sum_{d=0}^i(i)_{\!d}$. Terms with $d\ge p$ are divisible by $p$.

### 2.3 The factorial unit recurrence is valid for every odd $p$

The unit in (9) is


$$
\boxed{U_a=(-1)^a\pmod p.}
\tag{23}
$$


To prove this, separate $1,\ldots,p^a-1$ into multiples and nonmultiples of $p$. The latter consist of $p^{a-1}$ complete nonzero residue blocks, whose product is


$$
((p-1)!)^{p^{a-1}}\equiv(-1)^{p^{a-1}}=-1\pmod p.
$$


After removing their powers of $p$, the multiples contribute $U_{a-1}$. Thus $U_a=-U_{a-1}$, starting from $U_0=1$.

This proof, rather than a $3$-specific recurrence, supplies the required unit.

### 2.4 Whole logarithmic forcing and reconstruction

Every factorial index in $h^F$ lies in


$$
n\le m\le2n+b-1.
$$


For odd $p$,


$$
v_p(m!\mathcal F_m)\ge v_p(m!)-\lfloor\log_pm\rfloor.
$$


Since $\alpha_s(n,i)$ is integral, condition (11) makes the **entire** $h^F$ vanish modulo $p^{\beta+1}$. Thus (22) holds for the complete residual $\rho$.

The inverse Pascal transform of $(\mathcal D_i)$ is $(i!)$. Equations (17) and (22) imply


$$
p^{-\beta}(1+S)^{-n}\widetilde N^{-1}\rho
\equiv2w(i!)_{i<b}\pmod p.
\tag{24}
$$


The divided multiplication by $z-1$ annihilates the internal factorial coordinates, leaving $-1$ at zero and $b!\equiv0\pmod p$ at the top.

Also,


$$
v_p(\omega_b)=\beta,\qquad
p^{-\beta}\omega_b\equiv w\pmod p.
\tag{25}
$$


Substitution in the exact endpoint-retaining identity (7) proves (13). Taking its scalar product with (18) proves (14).

More explicitly, the divided $Q$-coefficients satisfy


$$
t_j^Q\equiv (1+2wp^\beta)j!\pmod{p^{\beta+1}},
\qquad 0\le j<b.
\tag{26}
$$


Since $\beta+1>v_p((b-1)!)$, division by $j!$ preserves integrality. The $P$-column is integral because its possible factorial denominators are dominated by $v_p(\lambda)=2F_n$. This proves (15), for the $B$-lift only; it is not an assertion about simultaneous integrality of every reconstructed $A,C$ coefficient.

Finally, $\beta<2F_n$ follows from (11), so the second valuation in (16) is strictly smaller than the first. This evaluates the final gcd and completes the theorem.

---

## 3. Specialization to $M=2001$, particularly $p=23$

For $M=2001$ and $p\ge5$, $h\le1$. Moreover,


$$
F_n-F_b\ge2000p^{a-1},
$$


whereas


$$
\lfloor\log_p(2n+b-1)\rfloor\le a+5.
$$


Therefore


$$
F_n-\lfloor\log_p(2n+b-1)\rfloor-(\beta+1)
\ge2000p^{a-1}-a-6-h>0.
\tag{27}
$$


The complete-logarithmic-forcing hypothesis holds at every assigned index. The only remaining hypothesis for a given $p\ge5$ is the constant-term unit.

### 3.1 Constant-term digit factorization

Put $W=t^{-1}+2+2t$. If $M=\sum d_rp^r$, Frobenius and the support $[-1,1]$ give


$$
\operatorname{CT}W^{Mp^a}
\equiv\prod_r\operatorname{CT}W^{d_r}\pmod p.
\tag{28}
$$


There is no hidden carry in the constant term: an exponent from $W^{d_0}$ has absolute value $<p$, so a total exponent divisible by $p$ forces that exponent to be zero; division by $p$ then repeats the argument.

At $p=23$,


$$
2001=3\cdot23^2+18\cdot23,
$$


so


$$
J_0\equiv C_3C_{18}\pmod{23},
\qquad C_d=\operatorname{CT}W^d.
\tag{29}
$$



### 3.2 Legendre reflection proves the suggested residue

In a quadratic extension, choose $\delta^2=-4$. The standard constant-term identity is


$$
C_d=\delta^dP_d(2/\delta).
\tag{30}
$$


For $0\le d<p$,


$$
P_{p-1-d}(x)\equiv P_d(x)\pmod p.
\tag{31}
$$


One direct justification uses the coefficients


$$
\frac{(-d)_r(d+1)_r}{(r!)^2}
$$


of the hypergeometric expression: replacing $d$ by $p-1-d$ interchanges the two numerator parameters modulo $p$; all denominators with $r<p$ are units, and the remaining coefficients vanish.

Since $18=22-4$,


$$
C_{18}\equiv\delta^{14}C_4=(-4)^7C_4\pmod{23}.
$$


Now


$$
C_3=32\equiv9,\qquad C_4=136\equiv21,\qquad
(-4)^7\equiv15\pmod{23}.
$$


Hence


$$
C_{18}\equiv15\cdot21\equiv16,\qquad
\boxed{J_0\equiv9\cdot16\equiv6\pmod{23}.}
\tag{32}
$$


This proves the unit independently of the suggested bounded calculation.

### 3.3 Exact $23$-adic laws on $n=2001\,23^a$

Here


$$
h=1,\qquad
F_n=\frac{2001b-21}{22},\qquad
\beta=\frac{b+21}{22}.
$$


Also


$$
w\equiv18(-1)^a\pmod{23}.
$$


The theorem gives


$$
\boxed{\mathfrak D\equiv9\pmod{23},}
\tag{33}
$$




$$
\boxed{
23^{-\beta}V_w
\equiv18(-1)^a(-2e_0+e_b)\pmod{23},
}
\tag{34}
$$


and


$$
\boxed{
23^{-\beta}\mathfrak C\equiv9(-1)^a\pmod{23}.
}
\tag{35}
$$



The least $B$-lift denominator is a $23$-unit, and the evaluated final gcd has depth


$$
\boxed{
v_{23}(g_B)=2F_n+\beta=\frac{4003b-21}{22}.
}
\tag{36}
$$


Subtracting this from $v_{23}(A_B)=4F_n$ yields (1).

For example, at $a=1$,


$$
(n,b)=(46023,23),\quad F_n=2091,\quad\beta=2,
$$


so the paper prediction is


$$
\mathfrak C\equiv7406\pmod{12167},
\qquad v_{23}(q_n)=4180.
\tag{37}
$$



---

## 4. Returning to $p=23$ at the original indices

Now—and only in this section—fix


$$
n=2001\,3^a,\qquad b=3^a,\qquad a\ge1.
\tag{38}
$$


Then $v_{23}(n)=1$, but $b$ is not a $23$-power. The preceding theorem does not apply.

The useful replacement is a divided residual calculation valid more generally for an odd prime $p\mid n$ with $p\nmid b$. Write


$$
n=pN,\qquad b=pB+r,\qquad1\le r<p.
\tag{39}
$$


All congruences below are modulo $p$.

### 4.1 A first-digit reduction of the complete $b!$-divided residual

Let $r^{\mathrm{res}}=\rho/b!$, retaining both forcing columns.

For $s\ge1$, the integral strengthening gives $p\mid\alpha_s(n,i)$. Thus only $s=0$ survives in (5) after division by $b!$. Also,


$$
p\mid\frac{t!}{b!}\qquad(t\ge b+p-r).
$$


Therefore


$$
r_i^{\mathrm{res}}
\equiv
\sum_{d=0}^{p-r-1}\frac{(b+d)!}{b!}
          \binom{2n+i}{b+d},
\tag{40}
$$


provided the divided logarithmic forcing vanishes modulo $p$.

At the original $23$-indices this proviso always holds:


$$
v_{23}(h_i^F/b!)
\ge F_n-F_b-\lfloor\log_{23}(2n+b-1)\rfloor\ge1.
\tag{41}
$$


For example, $F_n-F_b\ge\lfloor2000b/23\rfloor$, which already dominates the displayed logarithm for $b\ge3$.

Writing $i=pq+s$, Lucas gives the explicit residual array


$$
\boxed{
r_{pq+s}^{\mathrm{res}}
\equiv
\binom{2N+q}{B}
\sum_{t=r}^{s}\frac{t!}{r!}\binom{s}{t}.
}
\tag{42}
$$


The sum is zero for $s<r$.

This is a complete divided residual, not an exponential-only replacement.

### 4.2 Two finite transforms collapse exactly

Let $P_b$ be the Pascal matrix. Modulo $p$,


$$
\widetilde N=P_b(1+S)^n.
$$


Thus the divided reconstruction following inversion is


$$
(1+S)^{-n}\widetilde N^{-1}
=(1+S)^{-2n}P_b^{-1}.
\tag{43}
$$



Vandermonde’s identity applied to (40) shows


$$
(P_b^{-1}r^{\mathrm{res}})_{pq+s}
=
\begin{cases}
\dfrac{s!}{r!}\binom{2N}{B-q},&s\ge r,\\[6pt]
0,&s<r.
\end{cases}
\tag{44}
$$


When $s\ge r$, necessarily $q<B$.

Since $(1+S)^{-2n}$ only shifts by multiples of $p$ modulo $p$, the binomial convolution is


$$
\sum_{h=0}^{B-q-1}
\binom{-2N}{h}\binom{2N}{B-q-h}
=-\binom{-2N}{B-q}.
$$


Consequently the divided reconstructed residual is


$$
\boxed{
t^{\mathrm{res}}_{pq+s}
=
\begin{cases}
-\dfrac{s!}{r!}\binom{-2N}{B-q},&s\ge r,\\[6pt]
0,&s<r.
\end{cases}
}
\tag{45}
$$



### 4.3 The complete weighted $Q$-column modulo $p$, after dividing by $b!$

Set


$$
Y=V_w/b!.
$$


Applying the actual weighted multiplication and retaining the terminal term in (7) gives:

- If $r\ge3$,
  

$$
\boxed{Y\equiv0\pmod p.}
  \tag{46}
$$



- If $r=1$, its only possibly nonzero coordinates are
  

$$
\boxed{
  Y_{pq+1}\equiv
  2\binom Nq\binom{-2N}{B-q},
  \qquad0\le q\le B.
  }
  \tag{47}
$$



- If $r=2$, its only possibly nonzero coordinates are
  

$$
\boxed{
  Y_{pq+2}\equiv
  \binom Nq\binom{-2N}{B-q},
  \qquad0\le q\le B.
  }
  \tag{48}
$$



The $q=B$ entries in (47)–(48) are exactly the endpoint contribution, not an extrapolation of an internal coordinate.

For $p=23$, the powers of $3$ modulo $23$ have period $11$:


$$
3,9,4,12,13,16,2,6,18,8,1.
$$


Thus (46) proves the announced infinite-class result


$$
\boxed{
V_w\in23^{\,v_{23}(b!)+1}\mathbb Z_{23}^{b+1}
\quad\text{if }a\not\equiv0,7\pmod{11}.
}
\tag{49}
$$


There is no inference here that this is the exact depth.

---

## 5. Explicit norm and divided-cross objects at the same indices

The preceding reduction can also express the first digit of the $P$-column and of the full scalar contractions without a matrix inverse.

Let


$$
J=\operatorname{CT}W^n\pmod p,\qquad
A_h=\binom{2N+h}{h},\qquad
E_h=\binom{2N+h-1}{h},\qquad A_{-1}=0.
\tag{50}
$$



### 5.1 The divided $P$-column

The forcing satisfies $f_i^0\equiv J i!\pmod p$. Its inverse-Pascal transform is $J\,!i$, where $!i$ is the derangement number. The elementary congruence


$$
!(i+p)\equiv-!i\pmod p
$$


and the finite hockey-stick identity give


$$
\boxed{
t_i^P
\equiv J\,!i\binom{2N+H_i}{H_i},
\qquad
H_i=\left\lfloor\frac{b-1-i}{p}\right\rfloor.
}
\tag{51}
$$



Only the weighted coordinates with low base-$p$ digit $0,1,2$ can contribute to the norm.

If $r\ge3$,


$$
\boxed{
\mathfrak D
\equiv
6J^2\sum_{q=0}^B\binom Nq^2A_{B-q}^2.
}
\tag{52}
$$


If $r=1$ or $2$,


$$
\boxed{
\mathfrak D
\equiv
J^2\sum_{q=0}^B\binom Nq^2
\left(5A_{B-q}^2+A_{B-q-1}^2\right).
}
\tag{53}
$$



### 5.2 The complete divided cross contraction

Define


$$
\Xi=\mathfrak C/b!=Z_w^TY.
\tag{54}
$$


Then:

- $r\ge3$ implies $\Xi\equiv0\pmod p$.

- For $r=1$,
  

$$
\boxed{
  \Xi\equiv
  4J(-1)^B
  \sum_{q=0}^B\binom Nq^2A_{B-q}E_{B-q}.
  }
  \tag{55}
$$



- For $r=2$,
  

$$
\boxed{
  \Xi\equiv
  -J(-1)^B
  \sum_{q=0}^B\binom Nq^2A_{B-q-1}E_{B-q}.
  }
  \tag{56}
$$



These formulas identify a concrete obstruction: even the first nonzero digit now depends on binomial carry sums and on the digits of $2001\,3^a$. It is no longer a constant factorial unit.

### 5.3 The $J$-unit condition itself is digit-sensitive

For $p=23$, the recurrence


$$
dC_d=(4d-2)C_{d-1}+4(d-1)C_{d-2}
\tag{57}
$$


gives, for $0\le d\le11$,


$$
(C_d)\equiv
(1,2,8,9,21,17,2,0,7,6,2,19).
$$


Legendre reflection gives


$$
C_d\equiv(-4)^{d-11}C_{22-d}\qquad(12\le d\le22).
$$


Therefore the only zero digit factors are


$$
\boxed{C_7=C_{15}=0\pmod{23}.}
$$


By the proved constant-term digit factorization,


$$
\boxed{
J\ne0\pmod{23}
\iff
\text{the base-\(23\) expansion of \(2001\,3^a\)
contains neither \(7\) nor \(15\)}.
}
\tag{58}
$$


This exact digit characterization is not a claim about how often such exponents occur.

As one bounded hand-check, at $a=3$,


$$
(n,b)=(54027,27),\quad N=2349,\quad B=1,\quad r=4.
$$


The digits of $n$ are $(0,3,10,4)_{23}$, so $J=10$. Equation (52) gives


$$
\mathfrak D\equiv1\pmod{23},
\qquad
\Xi\equiv0\pmod{23}.
\tag{59}
$$


This determines the norm unit but not the next cross digit.

---

## 6. Exact all-depth residual/carry reduction and the final gcd

The first-digit formulas do not imply $O(\log n)$ cross depth. Here is the finite arithmetic object that must be controlled at higher precision.

For the original indices, set


$$
F_n=v_{23}(n!),\qquad F_b=v_{23}(b!),\qquad
\delta=v_{23}(\mathfrak D),\qquad
\xi=v_{23}(\Xi).
\tag{60}
$$



The global tail factor and local invertibility prove that the ordinary $Q$-column is $23$-integral: its correction is obtained by dividing $b!$ times integral divided coefficients by $j!$, $j<b$. The $P$-column is integral as well. Thus


$$
v_{23}(d_B)=0
\tag{61}
$$


also at these non-$23$-power dimensions.

The **actual final gcd** therefore has valuation


$$
\boxed{
v_{23}(g_B)
=\min\{4F_n+\delta,\ 2F_n+F_b+\xi\},
}
\tag{62}
$$


and the actual primitive denominator is


$$
\boxed{
v_{23}(q_n)
=\max\{0,\ 2F_n-F_b+\delta-\xi\}.
}
\tag{63}
$$


Both $\mathfrak D$ and $\Xi$ are nonzero: $\mathfrak D>0$, while nonvanishing of the complete cross contraction at the original indices follows from the already established $3$-adic theorem.

### 6.1 Dimension-uniform precision cutoffs

For any prescribed $H\ge1$, $\rho/b!\pmod{23^H}$ is determined by an explicitly bounded set of coefficients.

For $s\ge1$,


$$
v_{23}(\alpha_s(n,i))
\ge1+v_{23}((s-1)!).
\tag{64}
$$


Hence terms with


$$
s\ge23(H-1)+1
$$


vanish modulo $23^H$. Also


$$
v_{23}(t!/b!)\ge H\qquad(t\ge b+23H).
$$


Consequently the exponential divided residual requires only


$$
\boxed{
0\le s\le23(H-1),\qquad
b\le t<b+23H,
}
\tag{65}
$$


intersected with the defining finite factorial ranges.

The complete logarithmic contribution vanishes if


$$
H\le F_n-F_b-\lfloor\log_{23}(2n+b-1)\rfloor.
\tag{66}
$$


Beyond that threshold it must be included through its original finite sum; there is no convention that drops it.

The contact matrix itself has the same $s$-cutoff (64). Its inverse is lifted from the proved unit inverse modulo $23$, for example by


$$
X_{\mathrm{new}}=X(2I-\widetilde N X)
$$


at successively doubled precision.

Factorial quotients in (65) are evaluated by their exact Legendre valuations and their unit parts. The latter obey the finite recurrence


$$
\operatorname{unit}_p(m!)
\equiv
\left(\prod_{\substack{1\le j\le m\\p\nmid j}}j\right)
\operatorname{unit}_p(\lfloor m/p\rfloor!)
\pmod{p^H}.
\tag{67}
$$


This retains every carry and does not transfer a $3$-adic modulus window.

Thus (65)–(67), the integral contact matrix, and the actual reconstruction determine


$$
\mathfrak D\bmod23^H,\qquad \Xi\bmod23^H
$$


at every finite precision. Equations (52)–(56) are its explicit first layer. Since the two rational contractions are nonzero, increasing precision eventually determines $\delta,\xi$; no logarithmic bound on the required precision has been proved.

---

## 7. Whole evaluated error and what can be aggregated

Let


$$
\tau=\left(2+\frac1{2001}\right)\log(1+\sqrt2).
$$


At the supplied dependency status of the proportional signed-rate theorem, for either proportional allocation considered here,


$$
\epsilon_n=c_n-(e+\pi)\ne0
\quad\text{eventually},\qquad
\log|\epsilon_n|=-\tau n+o(n).
$$


The actual primitive form is always


$$
\boxed{
L_n=q_n(e+\pi)-p_n=-q_n\epsilon_n\ne0
\quad\text{eventually}.
}
\tag{68}
$$


It includes the complete exponential residual, logarithmic contribution, and coordinate-zero endpoint correction.

For the new $23$-power family alone,


$$
\log|L_n|
=
\log q_{n,23'}
+\left[
\frac{4001}{2001\cdot22}\log23-\tau
\right]n
-\frac{63}{22}\log23+o(n).
\tag{69}
$$


The uncontrolled quantity is the actual prime-to-$23$ part. Equation (69) is neither a shrinking proof nor an exclusion.

At the original $3$-power indices, the established $3$-part can be combined with (63), because these are now the **same centers**:


$$
\begin{aligned}
\log|L_n|
={}&
\left(n-\frac{b+13}{2}\right)\log3\\
&+\max\{0,2F_n-F_b+\delta-\xi\}\log23\\
&+\sum_{\ell\ne3,23}v_\ell(q_n)\log\ell
-\tau n+o(n).
\end{aligned}
\tag{70}
$$


Here $F_n,F_b,\delta,\xi$ in the second line are $23$-adic quantities. The first-digit reductions above do not control $\xi-\delta$ on an unbounded exponent class, so no favorable aggregate balance has been established.

---

# Concluding ledger

## (1) New result and proof status

**Cross-review passed**

- A5’s complete $b!$-tail factor and exact center/gcd reduction.
- The coordinator’s integral strengthening
  

$$
\widetilde N=B(n)+nC\quad\text{over }\mathbb Z.
$$


- Integrality, including the retained logarithmic forcing.

**Proved here**

1. A growing-dimensional split-product theorem for $b=p^a$, $p\ge5$, with explicit $J_0$-unit, norm-unit, and whole-logarithmic-forcing hypotheses.

2. At $n=2001\,23^a,\ b=23^a$, all hypotheses hold, and
   

$$
\boxed{
   v_{23}(\mathfrak C)=\frac{23^a+21}{22},\quad
   v_{23}(d_B)=0,\quad
   v_{23}(q_n)=\frac{4001\,23^a-63}{22}.
   }
$$


   The complete cross contraction is nonzero throughout $a\ge1$.

3. At the original indices $n=2001\,3^a,\ b=3^a$, an exact first-digit divided residual and weighted-$Q$ reduction, including
   

$$
V_w\in23^{v_{23}(b!)+1}\mathbb Z_{23}^{b+1}
   \quad(a\not\equiv0,7\pmod{11}).
$$



4. Explicit binomial-carry sums for the norm and complete divided cross contraction, plus the dimension-uniform all-depth cutoffs (65).

**Not proved**

- An actual-$q$ upper or lower rate at $23$ on an infinite class of the original indices.
- An aggregate denominator bound sufficient for primitive shrinking or exclusion.
- Irrationality or rationality of $e+\pi$.

## (2) Exact remaining bottleneck

At the original indices, the new $23$-adic bottleneck is specifically the difference


$$
\boxed{
v_{23}(\Xi)-v_{23}(\mathfrak D),
\qquad
\Xi=\mathfrak C/b!,
}
$$


for the finite carry system (42)–(67). The first layer often vanishes identically in the cross contraction, and $J_0$ itself has digit-dependent zeros. No finite sample supplies an $O(\log n)$ depth bound.

Even resolving this difference would leave the actual contribution of primes other than $3,23$ in (70).

## (3) Bounded exact computation request

**REQUEST: pro / max / high**

Two narrowly bounded normalization checks would be useful.

### A. New $23$-power first lift

**Inputs**


$$
n=46023,\quad b=23,\quad m_w=1,\quad\text{modulus }23^3=12167.
$$



**Expected verifiable output**


$$
J_0\equiv6\pmod{23},\qquad
\mathfrak D\equiv9\pmod{23},
$$




$$
V_w\equiv6877e_0+2645e_{23}\pmod{12167},
$$




$$
\boxed{\mathfrak C\equiv7406\pmod{12167}.}
$$


These certify, at this finite index,


$$
v_{23}(\mathfrak C)=2,\qquad v_{23}(q_n)=4180.
$$


The whole logarithmic forcing has valuation at least $2088$, so its disappearance at this requested precision must be certified by that bound.

### B. First unresolved carry at an original same index

**Inputs**


$$
n=54027,\quad b=27,\quad p=23,\quad
\Xi=\mathfrak C/27!,\quad\text{precision }23^2.
$$



**Expected verifiable output**

- Confirm the derived first layer
  

$$
J_0\equiv10,\qquad
  \mathfrak D\equiv1,\qquad
  \Xi\equiv0\pmod{23}.
$$


- Return the exact residue
  

$$
\boxed{\Xi/23\pmod{23}}
$$


  if division is valid, using the complete residual.
- For the divided residual modulo $23^2$, only
  

$$
0\le s\le23,\qquad27\le t<73
$$


  are required by (65); the complete logarithmic part is beyond this precision.

If the returned residue is nonzero, this finite index has


$$
v_{23}(q_n)=4908.
$$


No nonzero prediction is made in advance, and either output would be finite evidence only—not an infinite-class denominator law.
