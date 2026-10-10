> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 turn 8: repaired even normalization audit and a four-state odd norm recursion

No irrationality or rationality decision for $e+\pi$ follows.

I obtain two substantive outcomes.

1. **The even normalizations pass a paper audit**, including the coefficient-$4002$ $3$-law. The support argument in A5’s Lemma 5.1 needs an additional qualification: the correction matrix does not itself have odd-row support. Its action on the specific base solution does. I prove the required statement below, completing the uniform $4b!$-divisibility argument without relying on the finite controls.

2. **The odd leading norm has a four-state Lucas carry recursion**, together with a Boolean companion that distinguishes vanishing caused by whole-column content from genuine cancellation among nonzero norm terms. Applied to the actual constrained family, it proves
   

$$
\boxed{
   Z_w\equiv0\pmod{29}
   \quad\text{if}\quad
   a\equiv31,59,87,115,143,171,199\pmod{812}.
   }
$$


   These are infinite subclasses of $a\equiv3\pmod{28}$. Thus some aligned first zeros are demonstrably **whole-$P$-column zeros**, not merely isotropic scalar norms.

The recursion does not establish an infinite norm-unit class or an all-depth relative quotient law.

---

## 1. Even-family audit: domain and conclusions

In this section only,


$$
n=4002\,3^a,\qquad b=3^a,\qquad a\ge1,\qquad \ell=n+2.
$$


Thus $n=2h$ with $h$ odd, $b$ is odd, and $4\mid\ell$. The factorial metric is


$$
\omega_j=(n+2)_j,\qquad
\Omega=\operatorname{diag}(\omega_j^2),
$$


at $m_w=1$.

I retain A5’s actual columns and complete residual:


$$
Z_w=\mathcal T\widetilde N^{-1}f^0,\qquad
V_w=\omega_b e_b+\mathcal T\widetilde N^{-1}\rho,
$$




$$
\rho=h^e+h^F-\widetilde N T(n)(j!)_{j<b}.
$$


Here $T(x)_{ij}=\binom{x}{j-i}$, and


$$
B(n)=P\,T(n)
$$


with $P$ the lower Pascal matrix. The established integral identity


$$
\widetilde N=B(n)+nC,\qquad C\in M_b(\mathbb Z)
$$


is reused, not claimed anew.

The audit conclusions are


$$
\boxed{
Z_w\in2R\mathbb Z_2^{b+1},\qquad
V_w\in4b!\mathbb Z_2^{b+1},
\qquad
R=2^{n/2}\binom n{n/2},
}
\tag{1.1}
$$


and


$$
\boxed{
v_3(q_n)=n-\frac{b+15}{2},\qquad
v_3(g_B)=n+\frac{b-15}{2}.
}
\tag{1.2}
$$



These conclusions are uniform. They do not determine the growing $2$-adic mixed contraction.

### 1.1 Complete logarithmic forcing

The bound needed in the $2$-adic audit remains the whole-coefficient bound


$$
v_2(h_i^F)\ge
\frac n2+1-2\left\lfloor\log_2(2n+b-1)\right\rfloor.
\tag{1.3}
$$


Indeed,


$$
v_2(m!\mathcal F_m)
\ge
1+v_2(m!)
-\lfloor\log_2m\rfloor-\lfloor(m-1)/2\rfloor,
$$


and every occurring factorial index satisfies


$$
n\le m\le2n+b-1.
$$


Using $v_2(m!)=m-s_2(m)$ gives (1.3). On the assigned family its right side exceeds $v_2(b!)+2$. Consequently the **entire** $h^F/b!$, not an individual summand, vanishes modulo $4$.

---

## 2. Audit of the coefficient-$4002$ $3$-law

The changed factorial units in A5 are correct. The norm lift can also be justified directly, rather than imported without its coefficient-dependent check.

Put


$$
k=v_3(n)=a+1,\qquad
\beta=k+v_3((b-1)!)=\frac{b+1}{2}.
$$


For $1\le r<b$,


$$
v_3\binom{\pm n}{r}\ge a+1-v_3(r)\ge2.
$$


Hence, in the full dimension $b$,


$$
T(\pm n)\equiv I\pmod9,\qquad
\widetilde N\equiv P\pmod9.
\tag{2.1}
$$



Let


$$
\mathcal R(t)=1+2t+2t^2.
$$


Since $n=1334\cdot3^{a+1}$, the elementary implication


$$
F(t)^{3^a}\equiv F(t^{3^a})\pmod3
\quad\Longrightarrow\quad
F(t)^{3^{a+1}}\equiv F(t^{3^a})^3\pmod9
$$


shows that $\mathcal R(t)^n\bmod9$ is supported on multiples of $b$. Therefore the first three forcing quantities satisfy


$$
J_0\equiv J_1\equiv J_2\pmod9.
$$


The first three entries of $f^0$ are consequently


$$
(J_0,J_0,2J_0)\pmod9,
$$


and their inverse-Pascal transform is


$$
(J_0,0,J_0)\pmod9.
$$


Actual weighted reconstruction gives


$$
(Z_{w,0},Z_{w,1},Z_{w,2})
\equiv(-J_0,2J_0,-J_0)\pmod9.
$$


For every $3\le j\le b$, Lucas’s theorem gives


$$
3\mid\binom{n+2}{j}.
$$


All remaining squared coordinates therefore vanish modulo $9$, proving


$$
\boxed{\mathfrak D=Z_w^TZ_w\equiv6J_0^2\pmod9.}
\tag{2.2}
$$



Now


$$
4002=12111020_3.
$$


There are six nonzero digits, and both nonzero constant-term digit factors equal $2\bmod3$. Thus


$$
J_0\equiv1\pmod3,\qquad v_3(\mathfrak D)=1.
$$



The split-product residual has normalized unit


$$
3^{-\beta}\rho_i\equiv(-1)^a\mathcal D_i\pmod3,
$$


because $2n/3^{a+1}\equiv1\pmod3$. Its whole logarithmic part is beyond this precision:


$$
v_3(h_i^F)\ge
\frac{n-8}{2}-\lfloor\log_3(2n+b-1)\rfloor>\beta.
$$


The terminal factorial has unit $2(-1)^a$. Including that terminal term gives


$$
3^{-\beta}V_w\equiv2(-1)^a(e_0+e_b)\pmod3.
$$


Taking the scalar product with the leading $P$-column yields


$$
\boxed{
3^{-\beta}\mathfrak C\equiv(-1)^a\pmod3.
}
\tag{2.3}
$$


In particular, the complete cross contraction is nonzero at every assigned even index.

Both actual $B$-lift columns are $3$-integral, so the local least $B$-denominator satisfies $v_3(d_B)=0$. Since


$$
2v_3(n!)=n-8,
$$


the two final Gram valuations are


$$
v_3(A_B)=2n-15,\qquad
v_3(H_B)=n+\frac{b-15}{2}.
$$


Their minimum is the second valuation, proving (1.2) with the **actual final gcd** retained.

---

## 3. Audit of the uniform even $P$-normalization

A5’s two coefficient expansions imply the claimed integrality and permit a short, explicit parity verification.

Write $n=2h$, $h$ odd, and use A5’s notation


$$
A_l=[t^{2h-l}](1+2t+2t^2)^{2h},\qquad
D_l=\frac{(2h+l)!}{(2h)!}.
$$


The displayed expansions for $D_lA_l/R$ are integral at $2$, because


$$
v_2\!\left(\frac{2^r(r!)^2}{(2r)!}\right)=v_2(r!),
$$


and replacing $(2r)!$ by $(2r+1)!$ does not change this valuation.

Only $r=0,1$ can contribute modulo $2$. In the even-index expansion this gives


$$
\frac{D_{2j}A_{2j}}R
\equiv
(h)_j\bigl[1+(h-j)(h+j)\bigr]
\equiv j(h)_j\pmod2.
$$


It is nonzero only at $j=1$. In the odd-index expansion, the result is nonzero only at $j=0$. Hence


$$
\frac{D_lA_l}{R}\equiv
\begin{cases}
1,&l=1,2,\\
0,&\text{otherwise}
\end{cases}
\pmod2.
$$


Substitution into the exact forcing expansion proves


$$
f^0/R\equiv(0,1,1,1,0,\ldots)\pmod2.
\tag{3.1}
$$



The inverse-Pascal transform of (3.1) has entries


$$
\binom j1+\binom j2+\binom j3,
$$


which vanish exactly when $j\equiv0\pmod4$. Modulo $2$, the subsequent $T(-2n)$ transform shifts only by multiples of $4$, so the reconstructed divided column still vanishes on these indices.

A weight $\binom{\ell}{j}$ can be odd only when $j\equiv0\pmod4$. On those indices, divided multiplication


$$
t\longmapsto (jt_{j-1}-t_j)
$$


also gives zero modulo $2$. The endpoint $j=b$ has an even weight because $b$ is odd. Thus


$$
Z_w/R\equiv0\pmod2,
$$


proving the first inclusion in (1.1).

---

## 4. Repair and completion of A5’s Lemma 5.1

### 4.1 The qualification needed in the original support statement

The correction matrix


$$
E_{ij}=
\sum_{s\in\{1,3,4\}}
\binom{n+i}{s}\binom{n+i-s}{j}
\tag{4.1}
$$


does **not** itself have odd-row support modulo $2$. For example, its $s=4$ term can be nonzero on an even row.

What is true, and sufficient, is:

> The corresponding residual correction has odd-row support, and $E$ sends the particular base solution used in the proof to a vector with odd-row support.

Here is the missing verification.

### 4.2 Exact expansion modulo $4$

Let $d_s=s!a_s(n)$. In the integral divided-power ring,


$$
\phi(z)^2=1-2z+2z^2-z^3+\frac{z^4}{4}.
$$


Its nonconstant divided coefficients are even. Since $n/2$ is odd,


$$
d_1\equiv d_3\equiv d_4\equiv2\pmod4,
$$


and every other nonconstant $d_s$ vanishes modulo $4$. Thus


$$
\widetilde N\equiv B(n)+2E\pmod4.
$$



For odd $b$, with $\delta=1$ when $b\equiv1\pmod4$ and $0$ otherwise,


$$
\sum_{t=b}^{m}\frac{(m)_t}{b!}
\equiv
\binom mb+
2\delta\left(\binom m{b+1}+\binom m{b+2}\right)
\pmod4.
\tag{4.2}
$$


Set


$$
r_i=\binom{2n+i}{b},\qquad y^0=B(n)^{-1}r.
$$


Finite binomial convolution gives


$$
\boxed{
y_j^0=\binom n{b-j}-\binom{-n}{b-j}
\qquad(0\le j<b).
}
\tag{4.3}
$$


Because $n$ is even and $b$ odd, (4.3) is supported on odd $j$ modulo $2$.

The nonconstant residual correction is


$$
G_i=
\sum_{s\in\{1,3,4\}}
\binom{n+i}{s}\binom{2n+i-s}{b}\pmod2.
\tag{4.4}
$$


If $i$ is even, the $s=1,3$ terms vanish because their first binomial has even upper and odd lower index. For $s=4$, the second upper index is even while $b$ is odd. Thus


$$
G_i=0\quad(i\text{ even}).
\tag{4.5}
$$



Likewise, on an even row of $E$, the $s=1,3$ terms vanish. In the $s=4$ term, the remaining upper index is even, so all odd columns vanish. Since $y^0$ is supported on odd columns,


$$
(Ey^0)_i=0\quad(i\text{ even}).
\tag{4.6}
$$



Equations (4.5)–(4.6) prove the precise support assertion needed by the inverse correction.

### 4.3 The inverse and weights preserve the required cancellation

Modulo $4$, the contact correction to the reconstructed divided column is


$$
2T(-n)B(n)^{-1}(G-Ey^0).
$$


Modulo $2$,


$$
T(-n)B(n)^{-1}=T(-2n)P^{-1}.
$$


The inverse Pascal transform preserves odd-index support: if $i$ is even and $j$ odd, then $\binom ij\equiv0\pmod2$. The shift $T(-2n)$ also preserves that support. Divided multiplication preserves it as well.

Every odd-index weight is even; in fact $4\mid\binom{\ell}{j}$ for odd $j$. Therefore this correction contributes zero to $V_w/b!\pmod4$.

For the extra tails in (4.2), Newton transformation gives


$$
(P^{-1}r^{(k)})_j=\binom{2n}{k-j},
\qquad r_i^{(k)}=\binom{2n+i}{k}.
$$


Since $4\mid2n$, this is supported on $j\equiv k\pmod4$. When $\delta=1$, the two values $k=b+1,b+2$ are $2,3\bmod4$. The $T(-2n)$ shift preserves these classes. Divided multiplication can then produce only classes $2,3\bmod4$, whose weights are even. Their prefactor $2$ again makes the weighted contribution zero modulo $4$.

Finally, the base reconstructed column is


$$
t_j^0=-\binom{-2n}{b-j}.
$$


Its weighted contribution is divisible by $4$:

- for odd $j$, the weight is divisible by $4$;
- for even $j$, $b-j$ is odd, so $4\mid t_j^0$;
- the other multiplication term is covered by
  

$$
j\binom{\ell}{j}=\ell\binom{\ell-1}{j-1},\qquad4\mid\ell;
$$


- the retained terminal coordinate has odd index $b$, hence a weight divisible by $4$.

The complete logarithmic contribution vanishes at this precision by (1.3). This proves


$$
\boxed{V_w\in4b!\mathbb Z_2^{b+1}}
$$


uniformly.

Thus the lemma passes **after supplying the specific-base-solution support argument**, rather than treating $E$ as an odd-supported operator on arbitrary vectors.

The ordinary $Q$-column is $2$-integral because its divided correction is divisible by $b!$. The $P$-column is integral because $v_2(\lambda R)$ exceeds every relevant $v_2(j!)$. Consequently


$$
v_2(d_B)=0.
$$


Nothing in this audit supplies an upper bound for the normalized mixed-contraction valuation. The supplied $a=1,2$ controls remain finite evidence only.

---

## 5. A four-state digit/carry recursion for the odd norm

Return now to the original family


$$
n=2001\,3^a,\qquad b=3^a,\qquad a\ge1.
$$



The following recursion is valid more generally for an odd prime $p$, integers $N,B\ge0$, and the scalar


$$
S_B(N)=\sum_{q=0}^{B}
\binom Nq^2\binom{2N+B-q}{B-q}^2.
\tag{5.1}
$$


Binomial coefficients with lower index exceeding a nonnegative upper index are zero.

The tools here are classical Lucas splitting. The new object is the explicit small-state recursion tailored to the coupled upper indices in (5.1).

### 5.1 Squared-binomial series and the changing negative upper index

For any integer $U$, define the formal series over $\mathbb F_p$


$$
F_U(x)=\sum_{j\ge0}\binom Uj^2x^j.
$$


For $0\le u<p$, write


$$
f_u(x)=\sum_{j=0}^{u}\binom uj^2x^j.
$$


If $U=u+pU'$, generalized Lucas splitting gives


$$
\boxed{F_U(x)=f_u(x)F_{U'}(x^p)\quad\text{in }\mathbb F_p[[x]].}
\tag{5.2}
$$


For negative $U$, this follows just as for positive $U$ from


$$
(1+z)^U\equiv(1+z)^u(1+z^p)^{U'}\pmod p;
$$


all these formal series have well-defined integral coefficients.

Since


$$
\binom{2N+H}{H}^2=\binom{-2N-1}{H}^2,
$$


we have


$$
S_B(N)=[x^B]F_N(x)F_{-2N-1}(x).
\tag{5.3}
$$



The changing negative upper index requires two states, not one. Define


$$
G_{d,e}(N,B)
=[x^{B-e}]F_N(x)F_{-2N-d}(x),
\qquad d\in\{1,2\},\ e\in\{0,1\},
\tag{5.4}
$$


with negative coefficient indices interpreted as zero. Thus


$$
S_B(N)=G_{1,0}(N,B).
$$



### 5.2 Explicit transition

Write


$$
N=n_0+pN',\qquad B=b_0+pB',
\qquad0\le n_0,b_0<p.
$$


For each $d$, put


$$
d'=\left\lceil\frac{2n_0+d}{p}\right\rceil\in\{1,2\},
\qquad
m_0=pd'-2n_0-d.
\tag{5.5}
$$


Then $0\le m_0<p$, and exactly


$$
-2N-d=m_0+p(-2N'-d').
$$


Define


$$
L_{n_0,m_0}(t)=[x^t]f_{n_0}(x)f_{m_0}(x),
$$


taking this to be zero outside its polynomial degree range.

The recursion is


$$
\boxed{
G_{d,e}(N,B)=
\sum_{k=0}^{1}
L_{n_0,m_0}(b_0-e+pk)\,
G_{d',k}(N',B')
\pmod p.
}
\tag{5.6}
$$



#### Proof

Apply (5.2) to both factors in (5.4). A low-degree exponent $t$ must satisfy


$$
t\equiv b_0-e\pmod p.
$$


Because the product of the two low-digit polynomials has degree at most $2p-2$, the only possibilities are


$$
t=b_0-e,\qquad t=b_0-e+p.
$$


Their remaining coefficient indices are $B'$ and $B'-1$, respectively. This gives (5.6).

In particular, the carry $q_0+h_0=b_0+p$ is retained. When $e=1,b_0=0$, the first candidate is negative and automatically vanishes; the second candidate remains. No borrow is silently discarded. ∎

At the terminal pair $N=B=0$,


$$
(G_{1,0},G_{1,1},G_{2,0},G_{2,1})=(1,0,1,0).
\tag{5.7}
$$


Equations (5.5)–(5.7) give a product of explicit four-by-four transition matrices along the digits.

This determines the leading residue. It does **not** bound the number of higher $p$-adic lifts needed to determine a valuation.

---

## 6. A Boolean companion: column zeros versus isotropic norm zeros

There is a useful additional output from the same carry structure.

Let $\mathcal H_{d,e}(N,B)$ be true exactly when there exist $q,h\ge0$ such that


$$
q+h=B-e,\qquad
\binom Nq\binom{-2N-d}{h}\not\equiv0\pmod p.
$$


Its transition is


$$
\boxed{
\mathcal H_{d,e}(N,B)=
\bigvee_{k=0}^{1}
\left[
0\le b_0-e+pk\le n_0+m_0
\ \wedge\
\mathcal H_{d',k}(N',B')
\right].
}
\tag{6.1}
$$


The terminal vector is $(\mathrm{true},\mathrm{false},\mathrm{true},\mathrm{false})$.

Indeed, every digit binomial within $0\le q_0\le n_0$, $0\le h_0\le m_0$ is a unit, and their possible sums fill the interval


$$
0\le q_0+h_0\le n_0+m_0.
$$


Thus (6.1) records existence of a nonvanishing summand, without cancellation in $\mathbb F_p$.

At $p=29$, $J$ is a unit at every original index by the previously established digit-factor theorem. When $r=b\bmod29\ge3$, the leading $P$-coordinates are the triples


$$
J(-1)^q\binom Nq\binom{2N+B-q}{B-q}(-1,2,-1),
\qquad0\le q\le B.
$$


Consequently,


$$
\boxed{
Z_w\equiv0\pmod{29}
\iff
\mathcal H_{1,0}(N,B)=\mathrm{false}.
}
\tag{6.2}
$$



Therefore:

- $S_B(N)=0$ and $\mathcal H_{1,0}=\mathrm{false}$ means a whole-column zero;
- $S_B(N)=0$ and $\mathcal H_{1,0}=\mathrm{true}$ means cancellation among nonzero leading norm terms.

This distinction is relevant to any proposed all-depth relative law.

---

## 7. Specialization to the constrained $29$-family

The inputs are not independent. Here


$$
N=69b,\qquad B=\lfloor b/29\rfloor,\qquad b=3^a.
\tag{7.1}
$$



More generally, multiplication by $M=2001/p$ can be retained digit by digit. If


$$
b=\sum_{i\ge0}r_ip^i,
$$


then


$$
c_0=0,\qquad
n_i\equiv Mr_i+c_i\pmod p,\qquad
c_{i+1}=\left\lfloor\frac{Mr_i+c_i}{p}\right\rfloor,
\tag{7.2}
$$


and


$$
0\le c_i\le M-1.
$$


The $i$-th digit of $B$ is $r_{i+1}$. Thus (5.6) is coupled to the actual multiplication carry and a one-digit lookahead; it does not replace the constrained family by arbitrary $N,B$.

### 7.1 The first low-digit polynomial on $a\equiv3\pmod{28}$

Suppose


$$
a=3+28t,\qquad t\ge0.
$$


Then $b\bmod29=27$, and hence


$$
N\bmod29=7.
$$


Starting in $d=1$, formula (5.5) gives


$$
d'=1,\qquad m_0=14.
$$


The first low-digit polynomial is therefore


$$
f_7(x)f_{14}(x),
$$


of degree $21<29$. Its coefficient vector modulo $29$ is


$$
\boxed{
(1,13,27,19,5,16,28,24,2,28,16,
16,28,2,24,28,16,5,19,27,13,1).
}
\tag{7.3}
$$


For verification, the two factors have coefficient vectors


$$
f_7:\ (1,20,6,7,7,6,20,1),
$$




$$
f_{14}:\ (1,22,16,24,22,1,24,13,24,1,22,24,16,22,1).
$$


Every coefficient in (7.3) is nonzero.

Write


$$
B=j+29B',\qquad0\le j<29.
$$


Since


$$
\left\lfloor N/29\right\rfloor=69B+64,
$$


the first recursion is particularly simple:


$$
\boxed{
S_B(N)=c_j\,G_{1,0}(69B+64,B')\pmod{29},
}
\tag{7.4}
$$


where $c_j$ is (7.3) for $0\le j\le21$ and zero for $22\le j\le28$. There is no outgoing coefficient carry at this first step: its required degree would be at least $29$.

### 7.2 Proved infinite whole-column-zero subclasses

A direct modular power calculation gives


$$
3^{28}\equiv436=1+15\cdot29\pmod{29^2}.
$$


Thus


$$
3^{3+28t}
\equiv27(1+15\cdot29)^t
\equiv27-29t\pmod{29^2}.
$$


Therefore


$$
j=B\bmod29\equiv-t\pmod{29}.
\tag{7.5}
$$



If $t\equiv1,\ldots,7\pmod{29}$, then $j=28,\ldots,22$. Not only does (7.4) vanish: the Boolean transition also has no admissible carry, because


$$
j>7+14=21.
$$


Every leading amplitude is zero.

Hence, on the actual original family,


$$
\boxed{
Z_w\in29\mathbb Z_{29}^{b+1}
\quad\text{for}\quad
a\equiv31,59,87,115,143,171,199\pmod{812}.
}
\tag{7.6}
$$


It follows that


$$
\boxed{
v_{29}(\mathfrak D)\ge2
}
\tag{7.7}
$$


on these infinite subclasses.

The already proved $Y=V_w/b!\in29\mathbb Z_{29}^{b+1}$ then also gives


$$
\boxed{
v_{29}(\Xi)\ge2,\qquad \Xi=Z_w^TY.
}
\tag{7.8}
$$



This is an infinite conclusion obtained from a finite congruence obstruction. Conversely, the other twenty-two residue classes of $t\bmod29$ only avoid this **first** obstruction. Formula (7.4) leaves the higher-digit factor intact. They are not proved norm-unit classes.

---

## 8. What the recursion says about the proposed all-depth relation

On $a\equiv3\pmod{28}$, the established first carry is


$$
\Xi/29\equiv J S_B(N),\qquad
\mathfrak D\equiv6J^2S_B(N)\pmod{29}.
$$


Let $C_n=\operatorname{CT}(t^{-1}+2+2t)^n$, now regarded as an actual integer. It is a $29$-unit. The first-carry identity is exactly equivalent to the existence of


$$
\mathcal R_n\in\mathbb Z_{29}
$$


such that


$$
\boxed{
\Xi=\frac{29}{6C_n}\mathfrak D+29^2\mathcal R_n.
}
\tag{8.1}
$$


This retains the actual complete contractions.

A sufficient all-depth strengthening would be


$$
\boxed{
v_{29}(\mathcal R_n)\ge v_{29}(\mathfrak D).
}
\tag{8.2}
$$


It would make the remainder strictly higher than the first term in (8.1), proving


$$
v_{29}(\Xi)=1+v_{29}(\mathfrak D).
$$



But the proved congruence supplies only $v_{29}(\mathcal R_n)\ge0$. On the new subclasses (7.6), the norm has depth at least two, so (8.2) asks for at least two additional digits of remainder divisibility. Those digits have not been established.

Moreover, because these zeros include whole-column content, one cannot interpret them solely as a scalar isotropy problem. The Boolean recursion gives an explicit way to separate these two mechanisms before attempting a further lift.

This is the exact point at which the present all-depth route stops. Equation (8.1) alone is not a relative error estimate.

---

## 9. Final gcd, complete logarithmic bound, and whole signed error

For the original odd family, put


$$
\lambda=\frac{(n!)^2}{2^n},\qquad
\mathfrak D=Z_w^TZ_w,\qquad
\Xi=\frac{Z_w^TV_w}{b!}.
$$


The actual center is


$$
c_n=\frac{b!\,\Xi}{\lambda\mathfrak D}.
$$



At $p=29$, the complete divided logarithmic forcing satisfies


$$
\boxed{
v_{29}(h_i^F/b!)
\ge
F_n-F_b-\lfloor\log_{29}(2n+b-1)\rfloor,
}
\tag{9.1}
$$


where


$$
F_n=v_{29}(n!),\qquad F_b=v_{29}(b!).
$$


This exceeds $2$ throughout $b=3^a\ge3$. At a higher requested precision $H$, its omission is justified only when the right side of (9.1) is at least $H$; otherwise the complete logarithmic sum must be included.

The actual two-column $B$-lift is $29$-integral, so


$$
v_{29}(d_B)=0.
$$


With


$$
N_B=d_B[u,v],\quad
A_B=N_{B,1}^T\Omega N_{B,1},\quad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


retain


$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B.
$$


Writing


$$
\delta=v_{29}(\mathfrak D),\qquad
\xi=v_{29}(\Xi),
$$


the exact local identities remain


$$
\boxed{
v_{29}(g_B)=
\min\{4F_n+\delta,\ 2F_n+F_b+\xi\},
}
\tag{9.2}
$$




$$
\boxed{
v_{29}(q_n)=
\max\{0,\ 2F_n-F_b+\delta-\xi\}.
}
\tag{9.3}
$$


The norm is positive, and the complete cross contraction is nonzero by the established original $3$-adic theorem. Thus these valuations are finite.

The new lower bounds $\delta,\xi\ge2$ do **not** determine their difference and therefore do not evaluate (9.3) on the new subclasses.

Using the supplied signed-rate theorem, set


$$
\tau_{\rm odd}=
\left(2+\frac1{2001}\right)\log(1+\sqrt2).
$$


At these exact odd indices,


$$
\epsilon_n=c_n-(e+\pi)>0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|=-\tau_{\rm odd}n+o(n).
$$


The whole primitive evaluated error is


$$
\boxed{
L_n=q_n(e+\pi)-p_n=-q_n\epsilon_n<0
\quad\text{eventually}.
}
\tag{9.4}
$$


It includes the complete exponential residual, logarithmic forcing, and endpoint correction.

The complete same-index logarithmic accounting is


$$
\begin{aligned}
\log|L_n|
={}&
\left(n-\frac{b+13}{2}\right)\log3\\
&+\max\{0,2F_n-F_b+\delta-\xi\}\log29\\
&+\sum_{\ell\ne3,29}v_\ell(q_n)\log\ell
-\tau_{\rm odd}n+o(n).
\end{aligned}
\tag{9.5}
$$


No prime contribution in the third line is discarded. The even-family audit concerns different centers and cannot be added to (9.5).

---

# Concluding ledger

## (1) New result and proof status

**Paper audit completed**

- The coefficient-$4002$ $3$-law passes, including its norm lift modulo $9$, local least $B$-denominator, nonzero complete cross contraction, and actual final gcd.
- The uniform even $P$-normalization passes.
- The uniform complete $Q$-normalization passes after supplying the missing specific-base-solution support argument. The correction matrix itself is not an odd-supported operator on arbitrary vectors.
- No infinite even $2$-contraction law is asserted.

**Proved here**

- The four-state recursion (5.6), retaining both coefficient carries and the changing negative upper index.
- The Boolean carry recursion (6.1), which detects whole leading-column zeros.
- The constrained first-digit reduction (7.4).
- The infinite original-index column-zero subclasses (7.6), with
  

$$
v_{29}(\mathfrak D)\ge2,\qquad v_{29}(\Xi)\ge2.
$$



**Not proved**

An infinite norm-unit class, an all-depth relative quotient law, a favorable aggregate final-gcd rate, or irrationality or rationality of $e+\pi$.

## (2) Exact remaining bottleneck

At $29$, the unresolved quantity remains


$$
v_{29}(\Xi)-v_{29}(\mathfrak D).
$$


For the concrete relative identity (8.1), a sufficient next obligation is


$$
v_{29}(\mathcal R_n)\ge v_{29}(\mathfrak D).
$$


The newly proved infinite column-zero subclasses provide explicit locations where this is a genuinely higher-depth obligation, not a consequence of the first scalar congruence.

Even such a local law would leave the actual contributions of other primes in (9.5).

## (3) Bounded exact computation request

**REQUEST: pro / max / high**

This request is separate from the already pending direct $29$-adic center control.

### A. Independent carry-recursion verification

**Inputs**

- $p=29$;
- all $0\le N,B\le58$;
- $d=1,2$, $e=0,1$.

**Expected verifiable output**

Compare (5.6) with direct evaluation of


$$
\sum_{\substack{q,h\ge0\\q+h=B-e}}
\binom Nq^2\binom{-2N-d}{h}^2\pmod{29},
$$


and compare (6.1) with direct existence of a nonzero summand. Report every discrepancy, if any. This bounded rectangle includes changing negative-index states and coefficient carries.

### B. Constrained-family scalar and support classification

**Inputs**


$$
a=3+28t,\qquad0\le t\le58,
$$




$$
b=3^a,\qquad N=69b,\qquad B=\lfloor b/29\rfloor.
$$



**Expected verifiable output**

For each exponent, return


$$
S_B(N)\pmod{29},
\qquad
\mathcal H_{1,0}(N,B).
$$


Also verify the explicit low polynomial (7.3).

The proved predictions are:

- at $t=0$, $S_B(N)=1$ and the Boolean value is true;
- whenever $t\bmod29\in\{1,\ldots,7\}$, $S_B(N)=0$ and the Boolean value is false.

For the other inputs, no residue prediction is imposed. In particular, identify any case with scalar residue zero but Boolean value true; such a case isolates genuine leading norm cancellation from whole-column content.

These outputs would be finite diagnostics of the next lifting problem, not an infinite valuation bound.
