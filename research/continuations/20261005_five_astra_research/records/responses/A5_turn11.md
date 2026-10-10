> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 audit and simultaneous ternary law for the CRT centers

**The proposed $3$-adic law is valid, including when $k=v_3(n)>a+1$.** The varying ternary digits change a unit in the complete mixed contraction, but they do not introduce a cancellation.

The dyadic boundary calculation also passes an independent audit. In particular, its finite-boundary coefficient $90$ is correct. I give below a direct reference-column audit that does not require extrapolating the coefficient-$4002$ norm formula.

There is one important precision qualification in the ternary residual calculation:

> The tail at $t=b+2$ cannot simply be discarded. It combines with the tail at $t=b+1$, producing the two-block expression
> 

$$
> (2n+i)_{\underline b}
> +(2n+i-b)(2n+i)_{\underline{b+1}}.
>
$$


> Its normalized residue is proportional to $1+i^2$, not $1+i$.

With that term retained, the complete residual and endpoint give a nonzero mixed contraction uniformly.

No conclusion about the rationality of $e+\pi$ follows. The simultaneous denominator lower bound is unconditional arithmetic; its interpretation as exclusion of the selected shrinking-form route remains conditional on A3’s mesoscopic **whole actual error** theorem.

---

## 1. Domain, actual columns, and conclusions

Let


$$
b=3^a=9^r,\qquad a=2r,\qquad r\ge1.
$$


For the specified CRT sequence, put


$$
K=3+\lfloor\log_2(b+4)\rfloor,
$$


and let $h$ be the least integer at least $b^3$ satisfying


$$
h\equiv1\pmod{2^K},\qquad h\equiv0\pmod{3b}.
$$


Set


$$
n=2h,\qquad k=v_3(n),\qquad u=\frac n{3^k}.
$$


Thus


$$
k\ge a+1,
$$


but equality is not assumed.

Write


$$
F_t=v_3(t!),\qquad
\beta=k+F_{b-1}=k+F_b-a.
$$


Since $b=3^a$,


$$
F_b=\frac{b-1}{2}.
$$



Retain the exact supplied divided-coordinate reconstruction


$$
Z_w=\operatorname{diag}(W_j)\mathcal ZT(-n)\widetilde N^{-1}f^0,
$$




$$
V_w=\omega_b e_b+
\operatorname{diag}(W_j)\mathcal ZT(-n)\widetilde N^{-1}\rho,
$$


where


$$
W_j=\binom{n+2}{j},\qquad
(\mathcal Zt)_j=jt_{j-1}-t_j,
$$


and the vectors are extended by $t_{-1}=t_b=0$. In this reconstruction,


$$
\omega_b=b!W_b.
$$


All transformations have dimension exactly $b$, and all weighted columns have coordinates $0,\ldots,b$.

The residual is the complete one:


$$
\rho=h^e+h^F-\widetilde N T(n)(j!)_{j<b}.
$$


Define


$$
\mathfrak D=Z_w^TZ_w,\qquad
\mathfrak C=Z_w^TV_w,\qquad
\lambda=\frac{(n!)^2}{2^n}.
$$



The ternary result is


$$
\boxed{
v_3(\mathfrak D)=1,\qquad
v_3(\mathfrak C)=\beta,\qquad
v_3(d_B)=0.
}
\tag{1.1}
$$



More precisely, let $\nu_3(n)$ denote the number of nonzero ternary digits of $n$, and put


$$
J=J_0=\operatorname{CT}(t^{-1}+2+2t)^n.
$$


Then


$$
\boxed{
J\equiv(-1)^{\nu_3(n)}\pmod3,
}
\tag{1.2}
$$


and


$$
\boxed{
3^{-\beta}V_w\equiv u(-1)^a(e_0+e_b)\pmod3,
}
\tag{1.3}
$$




$$
\boxed{
3^{-\beta}\mathfrak C
\equiv -u(-1)^aJ\pmod3.
}
\tag{1.4}
$$


For the assigned even $a$, these simplify to


$$
3^{-\beta}V_w\equiv u(e_0+e_b),\qquad
3^{-\beta}\mathfrak C\equiv-uJ\pmod3.
$$



In particular, the **complete** mixed contraction is nonzero at every assigned index.

---

# Part I. Independent dyadic audit

## 2. Complete forcing and precision transfer

### 2.1 Divided coefficients

Let


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
d_s=s![z^s]\phi(z)^n.
$$


In the integral divided-power ring,


$$
\phi(z)^2=1+2U(z),
$$


where the divided coefficients of $U$ in degrees $1,2,3,4$ are


$$
-1,\ 2,\ -3,\ 3.
$$



Since $h\equiv1\pmod8$,


$$
(1+2U)^h\equiv1+2U\pmod{16}.
$$


Indeed, the linear difference has a factor $2(h-1)$; the quadratic and cubic differences have sufficient factors from $h-1$; and every term of degree at least four in $U$ has a factor $16$.

Consequently, in every retained dimension,


$$
\boxed{
(d_0,d_1,d_2,d_3,d_4)
\equiv(1,-2,4,-6,6)\pmod{16},
\qquad d_s\equiv0\pmod{16}\quad(s>4).
}
\tag{2.1}
$$


This is a whole-coefficient assertion, not a bounded-degree approximation whose cutoff grows unnoticed.

### 2.2 Normalized $P$-forcing

Here is an explicit check of the normalization used in the transfer.

Let


$$
A_l=[t^{2h-l}](1+2t+2t^2)^{2h},\qquad
D_l=\frac{(2h+l)!}{(2h)!},\qquad
B_l=\frac{D_lA_l}{R},
$$


where


$$
R=2^h\binom{2h}{h}.
$$



Separating even and odd numbers of linear factors gives


$$
B_{2j}
=
\left(\prod_{t=1}^j(2h+2t-1)\right)
(h)_{\underline j}
\sum_{r\ge0}
\frac{2^r(r!)^2}{(2r)!}
\binom{h-j}{r}\binom{h+j}{r},
\tag{2.2}
$$


and


$$
B_{2j+1}
=
\left(\prod_{t=0}^j(2h+2t+1)\right)
(h)_{\underline{j+1}}
\sum_{r\ge0}
\frac{2^r(r!)^2}{(2r+1)!}
\binom{h-j-1}{r}\binom{h+j}{r}.
\tag{2.3}
$$


The sums terminate by the binomial conventions.

Both displayed coefficient ratios have valuation $v_2(r!)$. Thus all their summands are $2$-integral. For $l\ge3$, the external falling factorial contains $h-1$, so


$$
B_l\equiv0\pmod8.
$$


For $l=0,1,2$, only $r=0,1,2,3$ need checking. The terms involving $h-1$ vanish at the necessary precision, giving


$$
B_0\equiv2,\qquad B_1\equiv B_2\equiv3\pmod8.
$$



Now


$$
\frac{f_i^0}{R}
=\sum_{l=0}^i\binom il\frac{D_i}{D_l}B_l.
$$


Therefore


$$
\boxed{
f^0/R\equiv(2,1,3,1,4,4,0,\ldots)\pmod8.
}
\tag{2.4}
$$


For $i\ge6$, the surviving factorial products contain $n+6$, which is divisible by $8$. This proves the support cutoff uniformly.

### 2.3 Complete logarithmic forcing

The logarithmic function satisfies


$$
\mathcal F'(z)=\frac2{\phi(z)}.
$$


The identity


$$
\frac1{\phi(z)}
=\frac{1+z+z^2/2}{1+z^4/4}
$$


shows directly that


$$
v_2(m!\mathcal F_m)
\ge
1+v_2(m!)-\lfloor\log_2m\rfloor
-\left\lfloor\frac{m-1}{2}\right\rfloor.
$$


In the complete divided forcing, all factorial indices lie in


$$
n\le m\le2n+b-1.
$$


Using $v_2(m!)=m-s_2(m)$ consequently gives


$$
\boxed{
v_2(h_i^F)
\ge h+1-2\lfloor\log_2(2n+b-1)\rfloor.
}
\tag{2.5}
$$



For the CRT choice,


$$
b^3\le h<b^3+3b\,2^K,
\qquad 2^K\le8(b+4),
$$


so $h<5b^3$ for $b\ge9$. It follows that


$$
\begin{aligned}
v_2(h_i^F/b!)
&\ge
h+1-2\lfloor\log_2(4h+b-1)\rfloor-v_2(b!)\\
&>
b^3-b-9-6\log_2b\\
&>4.
\end{aligned}
\tag{2.6}
$$


Thus the **entire** logarithmic forcing disappears modulo $16$ after division by $b!$.

For the exponential factorial tail,


$$
v_2((b+5)!/b!)=4
\qquad(b\equiv1\pmod8).
$$


Hence the exact modulo-$16$ residual retains precisely the possible tails


$$
t=b,b+1,b+2,b+3,b+4;
$$


all later tails vanish at that precision.

### 2.4 Binomial precision loss

For integral $x,\Delta$, and $1\le j\le M$, Vandermonde gives


$$
v_2\left(\binom{x+\Delta}{j}-\binom xj\right)
\ge v_2(\Delta)-\lfloor\log_2M\rfloor,
\tag{2.7}
$$


because


$$
\binom{\Delta}{t}
=\frac{\Delta}{t}\binom{\Delta-1}{t-1}.
$$



Here $n-2$ is divisible by $2^{K+1}$. Every lower index in the reduced contact, residual, Toeplitz and weight formulas is at most $b+4$. Thus


$$
K+1-\lfloor\log_2(b+4)\rfloor\ge4
$$


proves the required modulo-$16$ transfer to $n=2$.

The contact matrices are units over $\mathbb Z_2$, so their inverses transfer at the same precision. The normalized $P$-forcing transfers by (2.4), not by an unjustified continuity claim about the large scalar $R$.

---

## 3. Audit of the three reference boundary identities

Set, for this reference calculation only,


$$
n=2,\qquad B=b-1=8d.
$$


The reference residual is the exponential residue to which the actual **complete** residual transfers.

Let $r$ be that residual divided by $b!$, and $g=P^{-1}r$. Its first possible nonzero row is $B-3$. Direct evaluation gives


$$
r_{B-3},r_{B-2},r_{B-1},r_B
\equiv(1,4,4d+7,4)\pmod8.
$$


The finite inverse-Pascal transform gives


$$
\boxed{
g_{B-3},g_{B-2},g_{B-1},g_B
\equiv(1,6,4,4)\pmod8,
}
\tag{3.1}
$$


with all earlier entries zero.

For example,


$$
g_{B-2}\equiv4-(B-2)\equiv6\pmod8,
$$


and


$$
g_{B-1}
\equiv(4d+7)-4(B-1)+\binom{B-1}{2}
\equiv4\pmod8.
$$


At the last row, the factors $B,\binom B2,\binom B3$ give $g_B\equiv4$.

Let


$$
\boldsymbol\ell_i=(-1)^i\binom{i+3}{3},
\qquad0\le i\le B,
$$


the first row of $T(-4)$. Equation (3.1) gives


$$
\boxed{\boldsymbol\ell g\equiv4\pmod8.}
\tag{3.2}
$$


The first three terminal products vanish modulo $8$, while


$$
4\binom{B+3}{3}\equiv4\pmod8.
$$



At $n=2$, the contact correction is


$$
E_{ij}=\sum_{s=1}^4c_s\left[
\binom is\delta_{j,i-s}
+2\binom i{s-1}\binom{-1}{j+s-i-1}
+\binom i{s-2}\binom{-2}{j+s-i-2}
\right],
\tag{3.3}
$$


where


$$
(c_1,c_2,c_3,c_4)=(-1,2,-3,3).
$$



Modulo $2$, $\boldsymbol\ell_i$ is supported on $i\equiv0\pmod4$. On such a row of $E$, only


$$
E_{i,i-4}\equiv\binom i4\pmod2
$$


can survive. Thus $\boldsymbol\ell E$ is supported on


$$
j\equiv0\pmod8,\qquad j+4\le B.
$$


Every row of $E$ indexed by a multiple of $8$ is zero modulo $2$. Hence


$$
\boxed{\boldsymbol\ell E^2\equiv0\pmod2.}
\tag{3.4}
$$



For the linear carry, finite summation of (3.3) gives


$$
\boxed{
\begin{aligned}
(\boldsymbol\ell E)_{B-3}
={}&-2\binom{B+1}{4}
-6\binom{B+2}{5}\\
&-12\binom{B+3}{6}
+90\binom{B+4}{7}.
\end{aligned}
}
\tag{3.5}
$$


The coefficient $90$ is correct. Before truncation, the three contributions for a fixed $s$ have coefficient


$$
\binom{s+3}{3}-2\binom{s+2}{3}+\binom{s+1}{3}=s+1.
$$


For $s=4$, the first contribution lies at $i=B+1$, outside the matrix. Its removal changes the coefficient to


$$
-2\binom63+\binom53=-30;
$$


the remaining sign and $c_4=3$ produce $90$.

The first, second and fourth binomials in (3.5) are even when $B\equiv0\pmod8$. Therefore


$$
(\boldsymbol\ell E)_{B-3}\equiv0\pmod4.
$$


Also $(\boldsymbol\ell E)_{B-2}$ is even by the support calculation. Using (3.1),


$$
\boxed{\boldsymbol\ell Eg\equiv0\pmod4.}
\tag{3.6}
$$



All three requested identities therefore pass:


$$
\boxed{
\boldsymbol\ell g=4\pmod8,\qquad
\boldsymbol\ell Eg=0\pmod4,\qquad
\boldsymbol\ell E^2g=0\pmod2.
}
$$



The inverse expansion gives


$$
\eta_0
\equiv\boldsymbol\ell g
-2\boldsymbol\ell Eg
+4\boldsymbol\ell E^2g
\equiv4\pmod8.
$$


Thus the transferred actual column satisfies


$$
\boxed{Y_0=-\eta_0/4\equiv1\pmod2.}
\tag{3.7}
$$



---

## 4. Direct reference audit of both divided columns

This supplies an independent check of the whole-column divisions used in the mixed contraction.

At the reference $n=2$, the weights are


$$
(W_0,\ldots,W_b)=(1,4,6,4,1,0,\ldots,0).
$$



For the $Q$-column, $g\bmod2$ is supported only at $B-3\equiv1\pmod4$. Since $T(-4)\bmod2$ shifts by multiples of four, $\eta_2$ is even. The same row-support argument used above shows that the contact correction to $\eta_4$ vanishes modulo $4$; its base terms are multiples of


$$
\binom{B-4}{3},\qquad 2\binom{B-3}{3},
$$


both divisible by $4$. Hence $\eta_4\equiv0\pmod4$.

Together with $\eta_0\equiv4\pmod8$, these facts show that every reference weighted $Q$-coordinate is divisible by $4$. The transferred endpoint is also retained: its weight agrees modulo $16$ with $\binom4b=0$. Therefore


$$
Y\in\mathbb Z_2^{b+1}.
$$



For the $P$-column, let $g^P=P^{-1}(f^0/R)$. From (2.4),


$$
g_i^P\equiv
(-1)^i\left(2-i+3\binom i2-\binom i3\right)\pmod4.
$$


Thus


$$
g_{4q}^P/2\equiv1+q\pmod2,
\qquad
g_i^P\equiv0\pmod2\iff4\mid i.
$$



At rows $0$ and $4$, the linear contact carry vanishes modulo $4$: its relevant row support lies in columns divisible by $8$, where $g^P$ is even. Writing $M=B/4=2d$, the elementary expansion


$$
(1+z)^{-4}
\equiv(1+z^4)^{-1}
-2z^2(1+z^4)^{-2}\pmod4
$$


then gives


$$
\frac{\theta^P_{4q}}2
\equiv(1+q)(M-q+1)\pmod2
\qquad(q=0,1).
$$


Consequently


$$
\theta^P_0\equiv2\pmod4,\qquad
\theta^P_4\equiv0\pmod4.
$$


Also


$$
\theta^P_2\equiv M\equiv0\pmod2.
$$


Applying the reference weights proves


$$
Z_w/R\equiv2e_0\pmod4.
$$



The precision transfer therefore yields, for every selected CRT index,


$$
\boxed{
X\equiv e_0\pmod2,\qquad
Y\in\mathbb Z_2^{b+1},\qquad Y_0\equiv1\pmod2.
}
\tag{4.1}
$$


In particular,


$$
\boxed{
v_2(X^TX)=v_2(X^TY)=0.
}
\tag{4.2}
$$



This audit does not claim a universal value for $X^TY\bmod4$. The supplied value $1\bmod4$ at $(4482,9)$ remains finite evidence.

---

# Part II. The uniform actual $3$-adic law

## 5. Contact matrix and full Frobenius forcing modulo $9$

The following ternary proof in fact applies whenever


$$
b=3^a,\quad a\ge2,\quad n>0\text{ is even},\quad v_3(n)=k\ge a+1.
$$


These conditions imply $n\ge6b$.

For $s\ge1$,


$$
d_s
=n(s-1)![z^{s-1}]\phi'(z)\phi(z)^{n-1}.
$$


The coefficient on the right is $3$-integral, since its only possible coefficient denominators are powers of $2$. Hence


$$
\boxed{v_3(d_s)\ge k+F_{s-1}.}
\tag{5.1}
$$


In particular,


$$
\widetilde N=B(n)+nC,\qquad C\in M_b(\mathbb Z_3).
$$



For $1\le j<b$,


$$
v_3\binom{\pm n}{j}
\ge k-v_3(j)
\ge k-(a-1)\ge2.
$$


Thus


$$
\boxed{
T(\pm n)\equiv I\pmod9,\qquad
\widetilde N\equiv P\pmod9.
}
\tag{5.2}
$$


The contact matrix is therefore invertible over $\mathbb Z_3$.

Let


$$
\mathcal R(t)=1+2t+2t^2.
$$


For every integral polynomial $F$,


$$
F(t)^{3^k}\equiv F(t^{3^{k-1}})^3\pmod9.
$$


This follows by first using Frobenius modulo $3$, then cubing; the cross terms acquire a factor $9$.

Since $n=3^ku$, the **whole polynomial**


$$
\mathcal R(t)^n\bmod9
$$


is supported on multiples of $3^{k-1}$, hence on multiples of $b$. This statement includes coefficients near degree $n$; it is not a truncation at degree $b$.

In particular, the coefficients at degrees $n-1,n-2$ vanish modulo $9$, and the actual forcing quantities satisfy


$$
J_0\equiv J_1\equiv J_2\pmod9.
$$


The first three entries of $f^0$ are therefore


$$
(J,J,2J)\pmod9.
$$


Their inverse-Pascal transform is


$$
(J,0,J)\pmod9.
$$


The actual weighted reconstruction gives


$$
(Z_{w,0},Z_{w,1},Z_{w,2})
\equiv(-J,2J,-J)\pmod9.
\tag{5.3}
$$



For $3\le j\le b$, Lucas’s theorem gives


$$
3\mid W_j.
$$


All these other squared coordinates consequently vanish modulo $9$. Thus


$$
\boxed{\mathfrak D\equiv6J^2\pmod9.}
\tag{5.4}
$$



### The actual central coefficient is always a unit

Write $n=\sum d_\ell3^\ell$, $d_\ell\in\{0,1,2\}$. Modulo $3$,


$$
(t^{-1}+2+2t)^n
=\prod_\ell
(t^{-3^\ell}+2+2t^{3^\ell})^{d_\ell}.
$$


In each lowest remaining factor, its Laurent exponent lies between $-2$ and $2$. To contribute to the constant term it must be divisible by $3$, hence must be zero. Iteration proves digitwise factorization of the constant term.

The digit factors are


$$
1,\quad2,\quad8
$$


for digits $0,1,2$, respectively. Therefore


$$
J\equiv2^{\nu_3(n)}=(-1)^{\nu_3(n)}\pmod3.
$$


This proves (1.2), and (5.4) gives


$$
\boxed{v_3(\mathfrak D)=1.}
\tag{5.5}
$$



No fixed digit sum or fixed parity factor from $4002$ has been used.

---

## 6. The complete residual at precision $\beta+1$

The exact exponential residual, before adding $h^F$, is


$$
\rho_i^e
=
\sum_s d_s\binom{n+i}{s}
\sum_{t=b}^{2n+i-s}
t!\binom{2n+i-s}{t}.
\tag{6.1}
$$


All sums have their original finite bounds.

### 6.1 All nonconstant divided-coefficient blocks disappear

For $s\ge1$, every term in (6.1) has valuation at least


$$
k+F_b=\beta+a>\beta.
$$


Thus only $s=0$ can contribute modulo $3^{\beta+1}$.

Put


$$
P_i=(2n+i)_{\underline b},
\qquad 0\le i<b.
$$


The product contains $2n$ and the nonzero shifts


$$
2n+j,\qquad -(b-1-i)\le j\le i.
$$


Since $k>a-1$, every nonzero shift has the valuation of $j$. Also


$$
\binom{b-1}{i}\equiv(-1)^i\pmod3
$$


is a unit. Therefore


$$
v_3(P_i)
=k+F_i+F_{b-1-i}
=k+F_{b-1}
=\beta.
\tag{6.2}
$$



Let


$$
U=\frac{(b-1)!}{3^{F_{b-1}}}\pmod3.
$$


The factorial-unit recursion at $b=3^a$ gives


$$
U=(-1)^a.
$$


The signs from the negative shifts cancel the factor $(-1)^i$ from the binomial coefficient. Hence, uniformly in $i$,


$$
\boxed{
3^{-\beta}P_i\equiv2u(-1)^a\pmod3.
}
\tag{6.3}
$$



### 6.2 The two-block reduction, with the $b+2$ tail included

Let $x_i=2n+i-b$. The first three tails satisfy the exact identity


$$
\begin{aligned}
&(2n+i)_{\underline b}
+(2n+i)_{\underline{b+1}}
+(2n+i)_{\underline{b+2}}\\
&\qquad=P_i\bigl(1+x_i+x_i(x_i-1)\bigr)
=P_i(1+x_i^2).
\end{aligned}
\tag{6.4}
$$


Equivalently, they are the two blocks


$$
P_i+x_i(2n+i)_{\underline{b+1}}.
$$



Every tail beginning with $t=b+3$ contains the extra product


$$
x_i(x_i-1)(x_i-2),
$$


which is divisible by $3$. By (6.2), all such tails have valuation at least $\beta+1$.

It follows that


$$
\boxed{
3^{-\beta}\rho_i^e
\equiv
2u(-1)^a(1+i^2)\pmod3.
}
\tag{6.5}
$$


The residue pattern of $1+i^2$ is $1,2,2$, periodically.

### 6.3 The whole logarithmic contribution is beyond this precision

Since


$$
m\mathcal F_m=2[z^{m-1}]\phi(z)^{-1},
$$


and these coefficients are $3$-integral,


$$
v_3(m!\mathcal F_m)\ge F_m-\lfloor\log_3m\rfloor.
$$


The complete forcing therefore satisfies


$$
\boxed{
v_3(h_i^F)
\ge F_n-\lfloor\log_3(2n+b-1)\rfloor.
}
\tag{6.6}
$$



This lower bound exceeds $\beta$ uniformly on the stated domain. Indeed, $n\ge6b$, and


$$
F_n\ge n/3-1,\qquad k\le\log_3n,\qquad 2n+b-1<3n.
$$


Consequently,


$$
\begin{aligned}
F_n-\lfloor\log_3(2n+b-1)\rfloor-\beta
&\ge
\frac n3-\frac{b-1}{2}+a-2-2\log_3n.
\end{aligned}
$$


The right side is increasing for $n\ge6b$, and at $n=6b$ is


$$
\frac{3b+1}{2}-a-2-2\log_3 6>0
\qquad(b=3^a,\ a\ge2).
$$


Thus the **complete** residual obeys


$$
\boxed{
3^{-\beta}\rho_i
\equiv
2u(-1)^a(1+i^2)\pmod3.
}
\tag{6.7}
$$



---

## 7. Inverse remainder, terminal unit, and noncancellation

The fact that $k$ can be much smaller than $\beta$ causes no inverse-precision problem. The exact identity


$$
\widetilde N^{-1}-B(n)^{-1}
=-n\widetilde N^{-1}CB(n)^{-1}
$$


shows that, when applied to $\rho\in3^\beta\mathbb Z_3^b$, the inverse remainder lies in


$$
3^{\beta+k}\mathbb Z_3^b.
$$


Thus it vanishes at the required normalized precision. Replacing the remaining Toeplitz factors by $I$ is also legitimate by (5.2).

Let


$$
A=2u(-1)^a\pmod3.
$$


The finite inverse-Pascal transform of $1+i^2$ is


$$
(1,1,2,0,\ldots).
$$


Hence


$$
3^{-\beta}T(-n)\widetilde N^{-1}\rho
\equiv A(1,1,2,0,\ldots)\pmod3.
$$


Applying $\mathcal Z$ and the actual weights leaves only


$$
-Ae_0
$$


modulo $3$.

The retained terminal factorial satisfies


$$
\omega_b=(n+2)_{\underline b}.
$$


The same product argument as in (6.2)–(6.3), now with $n$ in place of $2n$, proves


$$
\boxed{
v_3(\omega_b)=\beta,\qquad
3^{-\beta}\omega_b\equiv u(-1)^a\pmod3.
}
\tag{7.1}
$$


Since $-A=-2u(-1)^a=u(-1)^a\pmod3$, the residual and terminal pieces give


$$
3^{-\beta}V_w
\equiv u(-1)^a(e_0+e_b)\pmod3.
$$



For the mixed contraction, $Z_{w,0}\equiv-J\pmod3$, while


$$
Z_{w,b}\equiv0\pmod3.
$$


Therefore


$$
3^{-\beta}\mathfrak C
\equiv-u(-1)^aJ\pmod3.
$$



This explicitly proves that cancellation cannot occur:

* the complete residual supplies a unit at coordinate zero;
* the terminal coordinate is retained, with its exact unit;
* its scalar-product contribution is one additional power of $3$ deeper because $Z_{w,b}$ is divisible by $3$;
* the inverse and logarithmic remainders are also beyond the normalized precision.

Thus


$$
\boxed{v_3(\mathfrak C)=\beta}
$$


for every index in the stated domain.

---

# Part III. Least lift denominator and the actual final gcd

## 8. Local integrality of the ordinary lift

The ordinary-coordinate reconstruction divides the relevant divided coefficients by $j!$.

At $3$, the $Q$-correction has depth at least


$$
\beta=F_b+k-a\ge F_b+1.
$$


Thus every division by $j!$, $0\le j\le b$, is harmless. The terminal ordinary coordinate is integral.

For the $P$-column, $f^0$, the contact inverse and the Toeplitz reconstruction are $3$-integral, while


$$
v_3(\lambda)=2F_n\ge F_b.
$$


Hence both ordinary columns are $3$-integral, proving


$$
\boxed{v_3(d_B)=0.}
\tag{8.1}
$$



The dyadic audit likewise gives $v_2(d_B)=0$: the $Q$-correction is divisible by $b!$, and the $P$-scalar $\lambda R$ has valuation


$$
\frac{3n}{2}-s_2(n),
$$


more than sufficient for all retained factorial divisions.

Retain, globally,


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


and


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B.
}
\tag{8.2}
$$


This is the actual final Gram gcd and actual primitive denominator.

### At $3$

The exact scalar relations give


$$
v_3(A_B)=4F_n+1,\qquad
v_3(H_B)=2F_n+\beta.
$$


Their difference is positive on the stated domain. Consequently,


$$
\boxed{
v_3(g_B)=2F_n+\beta,
}
\tag{8.3}
$$


and


$$
\boxed{
v_3(q_n)=2F_n+1-\beta
=n-s_3(n)+1-\beta.
}
\tag{8.4}
$$



### At $2$

Put $s=s_2(n)$ and $F_b^{(2)}=v_2(b!)$. The audited units give


$$
v_2(A_B)=3n-2s+2,
$$




$$
v_2(H_B)=\frac{3n}{2}-s+F_b^{(2)}+3.
$$


Thus


$$
\boxed{
v_2(g_B)=\frac{3n}{2}-s_2(n)+v_2(b!)+3,
}
\tag{8.5}
$$




$$
\boxed{
v_2(q_n)=\frac{3n}{2}-v_2(b!)-s_2(n)-1.
}
\tag{8.6}
$$



No subtraction of unrelated valuation lower bounds is used in either prime calculation.

---

## 9. Same-center consequence and the remaining analytic condition

For the specified least-representative CRT sequence,


$$
n\sim2b^3.
$$


Also


$$
k=O(\log n),\qquad s_3(n)=O(\log n),\qquad
\beta=O(b+\log n).
$$


Therefore


$$
v_3(q_n)=n-o(n),\qquad
v_2(q_n)=\frac32n-o(n).
$$


These are simultaneous statements about the **same actual primitive centers**. In particular,


$$
\boxed{
\liminf_{r\to\infty}\frac{\log q_n}{n}
\ge\frac32\log2+\log3
>2\log(1+\sqrt2).
}
\tag{9.1}
$$



The arithmetic statement is unconditional.

For the analytic implication, define the whole actual error


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi).
$$


If A3 proves, on this precise mesoscopic sequence,


$$
\epsilon_n\ne0\quad\text{eventually},\qquad
\log|\epsilon_n|
=-2\log(1+\sqrt2)\,n+o(n),
\tag{9.2}
$$


then the complete primitive evaluated form satisfies


$$
L_n=q_n(e+\pi)-p_n=-q_n\epsilon_n,
$$


and


$$
\begin{aligned}
\log|L_n|
={}&v_2(q_n)\log2+v_3(q_n)\log3\\
&+\sum_{p\ne2,3}v_p(q_n)\log p
-2\log(1+\sqrt2)\,n+o(n).
\end{aligned}
\tag{9.3}
$$


Every other prime contribution is nonnegative. Thus, conditionally on (9.2),


$$
\liminf\frac{\log|L_n|}{n}
\ge
\frac32\log2+\log3-2\log(1+\sqrt2)>0.
$$



This would exclude shrinking of this selected primitive center form on the CRT sequence. It would not prove rationality, irrationality, or exclusion of other endpoint directions.

---

# Concluding ledger

## (1) New result and proof status

**Proved here**

1. The dyadic boundary identities pass:
   

$$
\boldsymbol\ell g=4\pmod8,\quad
   \boldsymbol\ell Eg=0\pmod4,\quad
   \boldsymbol\ell E^2g=0\pmod2.
$$


   The finite-boundary coefficient $90$ is correct.

2. The coefficient precision transfer and complete forcing cutoffs are valid uniformly on the specified CRT family.

3. A direct reference-column audit proves
   

$$
X\equiv e_0,\qquad Y_0\equiv1\pmod2,
$$


   and hence both actual dyadic contractions are units.

4. For arbitrary $k=v_3(n)\ge a+1$, the same actual centers satisfy
   

$$
\beta=k+F_b-a,\qquad
   v_3(\mathfrak D)=1,\qquad
   v_3(\mathfrak C)=\beta,\qquad v_3(d_B)=0.
$$


   The exact normalized mixed unit is
   

$$
3^{-\beta}\mathfrak C
   \equiv-u(-1)^a(-1)^{\nu_3(n)}\pmod3.
$$



5. The actual final gcd and denominator have
   

$$
v_3(g_B)=2F_n+\beta,\qquad
   v_3(q_n)=n-s_3(n)+1-\beta.
$$



No additional ternary-digit CRT restriction is needed.

**Not proved:** the mesoscopic whole real-error theorem, or irrationality or rationality of $e+\pi$.

## (2) Exact remaining bottleneck

For the same-center route exclusion, the remaining dependency is precisely A3’s proof of the nonzero, complete actual error law (9.2) for


$$
b=9^r,\qquad n=2h,\qquad h=b^3+O(b^2)
$$


with the stated CRT selection and actual factorial metric.

The fixed-positive-allocation theorem cannot supply that dependency by substituting $c=0$.

## (3) One optional bounded modular certificate

No computation is needed for the infinite derivations above. An independent modular check of the new ternary law could use the already prescribed center


$$
\boxed{n=4482,\quad b=9,\quad p=3,\quad\text{modulus }3^6=729.}
$$



Here


$$
k=3,\quad u=166,\quad F_n=2239,\quad \beta=5,\quad
J\equiv2\pmod3.
$$



**Expected verifiable outputs from the original defining coefficients and complete forcing**


$$
\boxed{
3^{-5}\rho\equiv(2,1,1,2,1,1,2,1,1)\pmod3,
}
$$




$$
\boxed{
Z_w\equiv(1,1,1,0,\ldots,0)\pmod3,
\qquad \mathfrak D\equiv6\pmod9,
}
$$




$$
\boxed{
3^{-5}V_w\equiv e_0+e_9\pmod3,
\qquad
3^{-5}\mathfrak C\equiv1\pmod3,
}
$$


and therefore


$$
\boxed{
v_3(q_n)=4474,\qquad v_3(g_B)=4483.
}
$$



A complete-forcing certificate is


$$
v_3(h_i^F)\ge2239-\lfloor\log_3 8972\rfloor=2231.
$$


For the modulo-$729$ original-coefficient calculation, (5.1) certifies omission of divided coefficients $s\ge10$, and $F_{15}=6$ certifies omission of factorial tails $t\ge15$. Thus this check needs neither large exact coefficients nor a large-degree exact computation.

Its output would be finite corroboration or falsification of the formulas, not the proof of their infinite scope.
