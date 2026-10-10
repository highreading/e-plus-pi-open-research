> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Outcome

The coefficient-$4002$ extension at $3$ is provable, with different unit residues and a different digit-sum correction from the coefficient-$2001$ family. I also obtain:

- the proposed integral strengthening of the contact matrix and both forcing columns;
- a uniform, substantial $2$-adic factor of the **entire weighted $P$-column**;
- a uniform factor $4b!$ in the **complete endpoint-cancelled weighted $Q$-column**;
- an exact $2$-adic calculation at the first assigned index, including resolution of the first vanishing mixed-product digit and the **actual final gcd**.

I do **not** obtain a uniform actual-$q$ estimate at $2$ sufficient to prove aggregate exclusion or primitive shrinking. The distinction matters: the uniform column divisibilities below do not bound the mixed contraction’s valuation above.

Throughout,


$$
n=4002\,3^a,\qquad b=3^a,\qquad a\ge1,\qquad
\ell=n+2,\qquad \omega_j=(\ell)_{\!j}.
$$


The metric is always


$$
\Omega=\operatorname{diag}(\omega_0^2,\ldots,\omega_b^2).
$$



---

## 1. Analytic domain and exact arithmetic conventions

Here


$$
\frac bn=\frac1{4002}<\frac1{1000},\qquad b\ge3,
$$


so $m_w=1$ satisfies


$$
1\le m_w\le \left\lfloor\frac{b-1}{2}\right\rfloor.
$$


The supplied proportional signed-rate theorem expressly includes both parities and every positive diagonal $B$-coefficient metric. Thus it covers these even indices and this falling metric, at that theorem’s supplied proof status.

Writing $S=e+\pi$, its conclusion is eventually


$$
\epsilon_n=\frac{p_n}{q_n}-S<0,\qquad
\log|\epsilon_n|
=-\tau_c n+o(n),
\quad
\tau_c=\left(2+\frac1{4002}\right)\log(1+\sqrt2).
$$


In particular, the **whole primitive evaluated error** is


$$
L_n=q_nS-p_n=-q_n\epsilon_n>0
$$


eventually, and is nonzero. Neither the logarithmic forcing nor the exponential endpoint correction is removed from this assertion.

For the arithmetic, retain the exact contact notation


$$
\lambda=\frac{(n!)^2}{2^n},\qquad
y=\widetilde N^{-1}f^0,\qquad
Z_w=\mathcal T y,
$$


and


$$
V_w=\omega_b e_b+\mathcal T\widetilde N^{-1}\rho,
\tag{1.1}
$$


where


$$
\rho=h^e+h^F-\widetilde N(1+S_b)^n(j!)_{j<b}.
$$


Thus


$$
u=\lambda z,\qquad Z_w=\operatorname{diag}(\omega_j)z,
\qquad V_w=\operatorname{diag}(\omega_j)v.
$$


Both original forcing columns remain present. Set


$$
\mathfrak D=Z_w^TZ_w>0,\qquad
\mathfrak C=Z_w^TV_w.
$$


The actual center is


$$
c_n=\frac{\mathfrak C}{\lambda\mathfrak D}.
\tag{1.2}
$$



Let $d_B$ be the least common denominator of the actual two-column $B$-lift, and let


$$
N_B=d_B[u,v],\quad
A_B=N_{B,1}^T\Omega N_{B,1},\quad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The final reduction is, throughout,


$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B.
\tag{1.3}
$$



---

## 2. Audit of the integral contact strengthening

The proposed strengthening is correct on the stated finite factorial ranges.

### 2.1 The whole correction matrix is integral

For


$$
a_s(n)=[z^s]\left(1-z+\frac{z^2}{2}\right)^n,
$$


each term has denominator dividing $2^{\lfloor s/2\rfloor}$. Since


$$
v_2(s!)\ge\lfloor s/2\rfloor,
$$


the quantities


$$
a_s(n)(n+i)_{\!s}
$$


are integers.

For $s\ge1$,


$$
a_s(n)(n+i)_{\!s}
=
n(s-1)!\binom{n+i}{s}
[z^{s-1}]\phi'(z)\phi(z)^{n-1}.
$$


Here $\phi'=-1+z$. The coefficient on the right has denominator dividing


$$
2^{\lfloor(s-1)/2\rfloor},
$$


which is cancelled by $(s-1)!$. Consequently,


$$
\boxed{\widetilde N=B(n)+nC,\qquad C\in M_b(\mathbb Z).}
\tag{2.1}
$$


Because $B(n)$ is unimodular,


$$
\boxed{\widetilde N\in\operatorname{GL}_b(\mathbb Z_p)
\quad\text{for every }p\mid n.}
\tag{2.2}
$$


In particular this proves arithmetic normality, at both $2$ and $3$, for every assigned index.

### 2.2 The complete logarithmic factorial coefficients are even integers

The recurrence for $c_r=[z^r]\phi^{-1}$ gives


$$
c_r\in 2^{-\lfloor r/2\rfloor}\mathbb Z.
$$


For $m\ge r\ge1$,


$$
v_2(m!/r)\ge v_2((r-1)!)\ge\lfloor(r-1)/2\rfloor.
$$


Therefore every term in


$$
m!\mathcal F_m
=\sum_{r=1}^m 2(m!/r)c_{r-1}
$$


is an even integer. Hence


$$
\boxed{h^e\in\mathbb Z^b,\qquad h^F\in2\mathbb Z^b.}
\tag{2.3}
$$



A useful quantitative bound, retaining the complete sum, is


$$
v_2(m!\mathcal F_m)
\ge 1+v_2(m!)
-\lfloor\log_2m\rfloor-\lfloor(m-1)/2\rfloor.
$$


Thus, over every factorial index occurring in the forcing,


$$
\boxed{
v_2(h_i^F)\ge
\frac n2+1-2\lfloor\log_2(2n+b-1)\rfloor.
}
\tag{2.4}
$$


On the assigned family this is much larger than $v_2(b!)+4$.

---

## 3. The changed $3$-adic law at coefficient $4002$

Only the coefficient-dependent parts of the split-product argument need changing.

Put


$$
k=v_3(n)=a+1,\qquad
s=v_3((b-1)!),\qquad
\beta=k+s=\frac{b+1}{2}.
$$


The normalized factorial unit remains


$$
\frac{(b-1)!}{3^s}\equiv(-1)^a\pmod3.
$$


But now


$$
\frac n{3^k}=1334\equiv2\pmod3,
\qquad
\frac{2n}{3^k}\equiv1\pmod3.
$$



Accordingly, the normalized length-$b$ product in the complete residual has residue


$$
r_a=(-1)^a,
$$


not $2(-1)^a$. The split-product proof gives


$$
\boxed{
3^{-\beta}\rho_i\equiv(-1)^a\mathcal D_i\pmod3.
}
\tag{3.1}
$$


The complete logarithmic forcing lies beyond this precision: here


$$
v_3(h_i^F)\ge\frac{n-8}{2}-(a+8)>\beta.
$$



The terminal falling factorial changes unit as well:


$$
3^{-\beta}\omega_b\equiv2(-1)^a\pmod3.
$$


After the inverse Pascal transform and the retained endpoint correction in (1.1),


$$
\boxed{
3^{-\beta}V_w\equiv
2(-1)^a(e_0+e_b)\pmod3.
}
\tag{3.2}
$$



The ternary expansion is


$$
4002=12111020_3.
$$


Its digit sum is $8$, and it has six nonzero digits. The constant-term digit factors therefore give


$$
J_0\equiv2^6=1\pmod3.
$$


The inherited first norm lift still gives


$$
\mathfrak D\equiv6J_0^2\pmod9,\qquad v_3(\mathfrak D)=1.
$$


Combining this with (3.2),


$$
\boxed{
3^{-\beta}\mathfrak C\equiv(-1)^a\pmod3,
\qquad
v_3(\mathfrak C)=\beta.
}
\tag{3.3}
$$


In particular $\mathfrak C\ne0$ at every assigned index.

The ordinary $Q$-column is $3$-integral: in the exact subtraction, its divided coefficients are $j!$ plus a vector divisible by $3^\beta$, and


$$
v_3(j!)<\beta\qquad(j<b).
$$


The $P$-column is also integral. Hence $v_3(d_B)=0$.

Since


$$
2v_3(n!)=n-8,
$$


the evaluated final gcd and actual denominator are


$$
\boxed{
v_3(g_B)=n+\frac{b-15}{2},
\qquad
v_3(q_n)=n-\frac{b+15}{2}.
}
\tag{3.4}
$$


This is the coefficient-$4002$ extension, including its changed unit and digit-sum correction.

---

## 4. A uniform normalization of the entire $P$-column at $2$

Write


$$
n=2h,\qquad h=2001b\ \text{odd},\qquad
R=2^h\binom{2h}{h}.
$$


Then


$$
v_2(R)=h+s_2(h)=\frac n2+s_2(n).
\tag{4.1}
$$



The factor $R$ divides the **whole factorial-scaled forcing vector locally at $2$**, not just its central coefficient.

### Lemma 4.1
For every $0\le i<b$,


$$
f_i^0/R\in\mathbb Z_2.
$$



#### Proof

Let


$$
A_l=[t^{2h-l}](1+2t+2t^2)^{2h},
\qquad
D_l=\frac{(2h+l)!}{(2h)!}.
$$


Then


$$
J_i=\sum_{l=0}^i\binom il A_l.
$$



Put


$$
O_j=\prod_{r=1}^j(2h+2r-1).
$$


Direct expansion by the number of quadratic selections gives


$$
\frac{D_{2j}A_{2j}}R
=
O_j\sum_{r=0}^{h-j}
\frac{2^r(h)_{\!j+r}(h+j)_{\!r}}{(2r)!},
\tag{4.2}
$$


and


$$
\frac{D_{2j+1}A_{2j+1}}R
=
O_{j+1}\sum_{r=0}^{h-j-1}
\frac{2^r(h)_{\!j+1+r}(h+j)_{\!r}}{(2r+1)!}.
\tag{4.3}
$$


Each of the two length-$r$ falling products is divisible by $r!$. Moreover,


$$
v_2\!\left(\frac{2^r(r!)^2}{(2r)!}\right)
=
v_2(r!),
$$


and replacing $(2r)!$ by $(2r+1)!$ does not change this valuation. Every displayed summand is therefore $2$-integral.

Finally,


$$
\frac{f_i^0}{R}
=\sum_{l=0}^i
\binom il\frac{D_i}{D_l}\frac{D_lA_l}{R},
$$


and $D_i/D_l$ is integral. ∎

The same formulas also identify the first residue:


$$
\boxed{
(f_i^0/R)_{i<b}\equiv(0,1,1,1,0,0,\ldots)\pmod2,
}
\tag{4.4}
$$


truncated at dimension $b$. For $i\ge4$, every summand has an even factor either in the remaining consecutive product $D_i/D_l$ or in $(h)_{\lceil l/2\rceil}$.

Modulo $2$,


$$
\widetilde N^{-1}=T(-n)P_b^{-1},
\qquad
(1+S_b)^{-n}=T(-n).
$$


The inverse Pascal transform of (4.4) has entries


$$
\binom j1+\binom j2+\binom j3
\equiv
\begin{cases}
0,&j\equiv0\pmod4,\\
1,&j\not\equiv0\pmod4.
\end{cases}
$$


The subsequent $T(-2n)$ transform shifts only by multiples of $4$ modulo $2$. Thus its entries at $j\equiv0\pmod4$ vanish.

On the other hand, $\ell=n+2$ is divisible by $4$, so


$$
\binom{\ell}{j}\not\equiv0\pmod2
\quad\Longrightarrow\quad j\equiv0\pmod4.
$$


The divided multiplication by $z-1$ consequently gives


$$
\boxed{Z_w\in2R\,\mathbb Z_2^{\,b+1}.}
\tag{4.5}
$$



This accounts for substantial common content of the actual weighted $P$-column. It is not inferred from a raw contact determinant.

---

## 5. Two uniform vanishing digits of the full normalized $Q$-column

The exact exponential residual satisfies


$$
\rho_i^e
=
\sum_s a_s(n)(n+i)_{\!s}
\sum_{t=b}^{2n+i-s}(2n+i-s)_{\!t}.
$$


Because the first factor is integral and $t\ge b$,


$$
\rho^e/b!\in\mathbb Z^b.
$$


Bound (2.4) gives the same local conclusion for $h^F/b!$, with ample additional precision. Thus


$$
\rho/b!\in\mathbb Z_2^b.
$$



There is an additional uniform cancellation:

### Lemma 5.1
For every assigned index,


$$
\boxed{V_w\in4b!\,\mathbb Z_2^{\,b+1}.}
\tag{5.1}
$$



Here is a derivation that keeps the endpoint term.

Let $d_s=s!a_s(n)$. In the divided-power coefficient ring,


$$
\phi(z)^2
=1-2z+2z^2-z^3+\frac{z^4}{4}.
$$


All nonconstant divided coefficients are even. Since $n/2$ is odd,


$$
d_0\equiv1,\qquad
d_1\equiv d_3\equiv d_4\equiv2\pmod4,
$$


and every other $d_s$ vanishes modulo $4$. Hence


$$
\widetilde N\equiv B(n)+2E\pmod4,
$$


where


$$
E_{ij}
=\sum_{s\in\{1,3,4\}}
\binom{n+i}{s}\binom{n+i-s}{j}.
\tag{5.2}
$$



For odd $b$, the factorial tail modulo $4$ is


$$
\sum_{t=b}^m\frac{(m)_{\!t}}{b!}
\equiv
\binom mb+
2\delta\left(\binom m{b+1}+\binom m{b+2}\right),
\tag{5.3}
$$


where $\delta=1$ if $b\equiv1\pmod4$, and $\delta=0$ otherwise.

First retain only $r_i=\binom{2n+i}{b}$ and the base matrix $B(n)$. Exact binomial convolution gives the reconstructed divided coefficients


$$
t_j=-\binom{-2n}{b-j}\qquad(0\le j<b).
\tag{5.4}
$$


Including the terminal term $\binom{\ell}{b}e_b$, every weighted coordinate obtained from (5.4) is divisible by $4$. This follows by separating $j$ into its residue classes modulo $4$, using $4\mid2n$ and $4\mid\ell$.

For the correction in (5.2), both its action on the base solution and the corresponding residual correction are supported on odd rows modulo $2$. The inverse Pascal transform, $T(-n)$, and the divided reconstruction preserve that odd-index support modulo $2$. The falling weights annihilate it.

Finally, when $\delta=1$, the two extra columns in (5.3) reconstruct modulo $2$ on indices congruent respectively to $b+1\equiv2\pmod4$ and to an odd residue. The weights again annihilate both. The full logarithmic forcing vanishes at this precision by (2.4). This proves (5.1).

Thus the first normalized $Q$-digit and the next digit both vanish uniformly. This is an explicit calculation, not an appeal to possible isotropy.

These arguments also prove


$$
\boxed{v_2(d_B)=0.}
\tag{5.5}
$$


Indeed the ordinary $Q$-column is obtained from the polynomial $1+\cdots+z^{b-1}$ by adding divided coefficients divisible by $b!$, so division by $j!$, $j<b$, preserves integrality. The $P$-column is integral because the valuation of $\lambda R$ greatly exceeds $v_2((b-1)!)$.

---

## 6. Exact first-index calculation at $2$, including the next mixed digit

The following is a bounded exact calculation from the defining formulas, not evidence for an infinite law.

Take


$$
a=1,\qquad n=12006,\qquad b=3,\qquad h=6003.
$$


Here


$$
s_2(n)=9,\qquad
v_2(R)=6012,\qquad
v_2(\lambda)=11988,\qquad v_2(b!)=1.
$$



### 6.1 Exact modular inputs

Expanding $(\phi^2)^h$ in divided coefficients modulo $16$ gives


$$
(d_0,d_1,\ldots,d_8)
\equiv(1,10,4,14,2,8,0,8,8)\pmod{16},
$$


with all later entries zero modulo $16$. Substitution into the defining contact sums yields


$$
\boxed{
\widetilde N\equiv
\begin{pmatrix}
15&6&5\\
11&9&13\\
5&8&4
\end{pmatrix}\pmod{16}.
}
\tag{6.1}
$$



Formulas (4.2)–(4.3) give


$$
\boxed{f^0/R\equiv(10,7,1)^T\pmod{16}.}
\tag{6.2}
$$


For completeness, the central two series used here are


$$
T_0=\sum_r\frac{2^r(h)_{\!r}^2}{(2r)!}\equiv10,
\qquad
T_1=\sum_r\frac{2^r(h-r)(h)_{\!r}^2}{(2r+1)!}\equiv7
\pmod{16}.
$$


Terms $r\ge8$ vanish by the bound $v_2(r!)\ge7$; the remaining terms are finite rational arithmetic. Terms $r=4,\ldots,7$ also vanish at this precision because $v_2(h-3)=4$.

The exact complete residual gives


$$
\boxed{\rho/b!\equiv(4,2,0)^T\pmod{16}.}
\tag{6.3}
$$


Here the exponential tail needs only $t=3,\ldots,7$:


$$
\sum_{t=3}^m\frac{(m)_{\!t}}{3!}
\equiv
\binom m3+4\binom m4+4\binom m5
+8\binom m6+8\binom m7\pmod{16}.
$$


The complete logarithmic contribution has valuation at least


$$
5976-v_2(3!)=5975
$$


after division by $b!$, so it is zero at the requested precision by proof, not by omission.

Solving (6.1) gives


$$
\widetilde N^{-1}(f^0/R)\equiv(1,3,5)^T,
$$




$$
\widetilde N^{-1}(\rho/b!)\equiv(0,10,8)^T
\pmod{16}.
$$


The divided inverse reconstruction has first row $(1,10,5)$. Its two outputs are respectively


$$
(8,5,5)^T,\qquad(12,10,8)^T\pmod{16}.
$$



Since


$$
\left(\binom{\ell}{0},\binom{\ell}{1},
\binom{\ell}{2},\binom{\ell}{3}\right)
\equiv(1,8,12,8)\pmod{16},
$$


the complete weighted columns are


$$
\boxed{
Z_w/R\equiv(8,8,12,8)^T\pmod{16},
}
\tag{6.4}
$$




$$
\boxed{
V_w/b!\equiv(4,0,0,8)^T\pmod{16}.
}
\tag{6.5}
$$



### 6.2 The first mixed lift cancels; the next one does not

Define the locally integral normalized vectors


$$
X=\frac{Z_w}{4R},\qquad Y=\frac{V_w}{4b!}.
$$


Equations (6.4)–(6.5) give


$$
X\equiv(2,2,3,2)^T,\qquad
Y\equiv(1,0,0,2)^T\pmod4.
$$


Therefore


$$
X^TX\equiv1\pmod4,
$$


while


$$
X^TY\equiv2\pmod4.
\tag{6.6}
$$


The first mixed residue is zero modulo $2$, but its **actual next digit is nonzero**.

It follows exactly that


$$
v_2(\mathfrak D)=2v_2(R)+4=12028,
$$




$$
v_2(\mathfrak C)=v_2(R)+v_2(b!)+5=6018.
$$


Thus, after the actual rational reduction,


$$
\boxed{v_2(q_{12006})=17998.}
\tag{6.7}
$$



Because $v_2(d_B)=0$, the final Gram integers themselves satisfy


$$
v_2(A_B)=36004,\qquad v_2(H_B)=18006.
$$


Consequently the **evaluated final gcd** has


$$
\boxed{v_2(g_B)=18006,}
\tag{6.8}
$$


and subtracting (6.8) from $v_2(A_B)$ gives (6.7).

At this same index, (3.4) gives


$$
v_3(q_{12006})=11997.
$$


This is a genuine two-prime calculation for one assigned center. It does not establish an asymptotic exclusion.

---

## 7. What remains unresolved in the growing $2$-adic calculation

The uniform results permit the normalization


$$
X_a=\frac{Z_w}{2R}\in\mathbb Z_2^{b+1},
\qquad
Y_a=\frac{V_w}{4b!}\in\mathbb Z_2^{b+1}.
$$


They retain both forcings, the endpoint correction, and the same metric. Exactly,


$$
c_n=\frac{2b!}{\lambda R}\,
\frac{X_a^TY_a}{X_a^TX_a}.
\tag{7.1}
$$



However, the results above do not yet determine the growing-dimension valuations of the two evaluated contractions in (7.1). In particular, the nonzero next mixed digit proved in Section 6 is specific to $a=1$; I have not proved its analogue for all $a$, nor a uniform upper bound on the excess mixed-contraction valuation.

The known $3$-part contributes the unconditional lower rate


$$
\liminf_{a\to\infty}\frac{\log q_n}{n}
\ge
\left(1-\frac1{8004}\right)\log3,
$$


which remains below $\tau_c$. The finite $2$-part cannot be added to this infinite rate.

Thus there is still no proved aggregate lower rate exceeding $\tau_c$, and no aggregate upper rate below it. The whole error remains


$$
L_n=-q_n\epsilon_n\ne0
$$


eventually, but its asymptotic primitive size is not decided here.

---

# Concluding ledger

## (1) New result and proof status

**Proved uniformly on $n=4002\,3^a,\ b=3^a,\ a\ge1$:**

- The strengthened integral contact identity
  

$$
\widetilde N=B(n)+nC,\qquad C\in M_b(\mathbb Z),
$$


  and integrality of both complete forcing columns.
- The coefficient-$4002$ first lift
  

$$
3^{-(b+1)/2}\mathfrak C\equiv(-1)^a\pmod3.
$$


- The actual final-$q$ law
  

$$
\boxed{v_3(q_n)=n-\frac{b+15}{2},}
$$


  with $v_3(g_B)=n+(b-15)/2$.
- The whole-column $2$-adic normalizations
  

$$
\boxed{
  Z_w\in2R\,\mathbb Z_2^{b+1},\qquad
  V_w\in4b!\,\mathbb Z_2^{b+1},
  \quad R=2^{n/2}\binom n{n/2},
  }
$$


  and $v_2(d_B)=0$.

**Proved by a bounded exact derivation at the first assigned index:**


$$
\boxed{
v_2(q_{12006})=17998,\qquad
v_2(g_B)=18006.
}
$$


The vanishing first mixed digit is resolved by the explicit next residue $X^TY\equiv2\pmod4$.

These modular calculations have not been independently executed or audited here. Their derivations are given above; no finite calculation is being used to prove an infinite assertion.

## (2) Exact remaining bottleneck

The unresolved main obligation is an upper bound for the valuation of the **complete normalized mixed contraction** $X_a^TY_a$, relative to the normalized norm $X_a^TX_a$, as $b=3^a$ grows.

The matrix being a $2$-unit, the large common $P$-factor, and the complete $4b!$ factor in $V_w$ do not supply that bound. The first-index mixed residue does not justify a growing-dimension transfer.

No rationality or irrationality decision for $e+\pi$, and no asymptotic exclusion of this even subfamily, is claimed.

## (3) One bounded exact computation request

**REQUEST: pro / max / high**

Use only


$$
\boxed{a=2,\qquad n=36018,\qquad b=9,\qquad m_w=1.}
$$


Put


$$
h=18009,\qquad R=2^h\binom{2h}{h}.
$$


The proved scalar valuations are


$$
v_2(R)=18016,\qquad
v_2(\lambda)=36004,\qquad
v_2(9!)=7.
$$



Compute, from the defining finite coefficient sums and the complete $h^e+h^F$ forcing, the exact valuations of


$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4\cdot9!},
\qquad X^TX,\qquad X^TY.
$$


The expected verifiable output is:

1. The exact common $2$-content of each normalized column.
2. A nonzero leading residue for each evaluated contraction, with sufficient modulus to certify its valuation.
3. The actual denominator valuation
   

$$
\boxed{
   v_2(q_{36018})
   =\max\!\left(0,\,
   54012+v_2(X^TX)-v_2(X^TY)\right),
   }
$$


   and the corresponding $v_2(g_B)$, using $v_2(d_B)=0$.
4. A certificate that the **complete logarithmic forcing** lies beyond the employed precision, using (2.4).

This single control would decisively determine whether the first-index mixed-lift pattern persists at the first larger dimension. It would guide the next uniform lemma; it would not itself prove one.
