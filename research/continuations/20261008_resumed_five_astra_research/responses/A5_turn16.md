> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A source-specific depth bound at the arc roots, and an evaluated Gaussian–Hermite first jet

## Abstract and proof status

The rationality or irrationality of $e+\pi$ remains unresolved. In particular, this report does **not** prove a fixed $\eta>0$ for


$$
\kappa_N^{\mathrm{prod}}
\le (N!)^{1-\eta}e^{CN}
\qquad
\bigl(N=9^{18+32u},\ u\ge0\bigr).
$$



There are two new proved results.

1. **A uniform bound on an actual source-depth band.**  
   A factorial-moment divided-difference argument controls the source at the three roots of the original arc denominator. Put
   

$$
\ell=2N-6,
$$


   and
   

$$
\mathfrak u_1=-2228,\qquad
   \mathfrak u_3=-2877556,\qquad
   \mathfrak u_5=-5227842548.
$$


   If $p\ge17$, $s\in\{1,3,5\}$, and
   

$$
v_p(\ell^2-s^2)\ge v_p(\mathfrak u_s)+2,
$$


   then
   

$$
v_p(U)=v_p(\mathfrak u_s).
$$


   Consequently, the contribution of **all** these primes, at **all** their unpaid source depths, to $\log\kappa_N^{\mathrm{prod}}$ is less than $47$. This is an evaluated upper bound for a specified part of the displayed positive-part mass, not a coefficient-content or height restatement.

2. **A fully evaluated first Frobenius jet coupling the actual Gaussian source and both endpoint states.**  
   At every prime $p\ge17$ dividing $2N-1$, the four original quantities
   

$$
U,\quad V,\quad E_K,\quad E_F
$$


   satisfy explicit congruences involving the actual divided $\alpha,\beta,\delta$, the original adjacent Hermite endpoints, and two distinct, evaluated forcing constants. These congruences give additional source-specific exclusions and a precise higher-depth continuation problem. They do **not** force endpoint surplus at these denominator primes: the actual reduced endpoint has $v_p(y_K)=0$.

The first result pays a genuine infinite prime/depth range. However, no argument shows that this range carries a fixed positive fraction of the possible $N\log N$ mass. The second result identifies the remaining local collision rather than bounding its higher lifts. Thus the primary strict intrinsic-content objective is still open.

No previous source array, small-prime scan, signed-return height calculation, cofactor-separation proof, or fixed-product proof is repeated. No calculation at an original index is proposed.

---

## 1. Original objects and scope of reuse

Throughout,


$$
\boxed{N=9^{18+32u},\qquad u\in\mathbb Z_{\ge0}},
$$


and


$$
n=2N,\qquad m=N-3,\qquad \ell=2N-6.
$$


Every such $N$ is odd. The physical polynomial terminal remains $2N$.

### 1.1 The actually divided Gaussian source

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


with


$$
C_0=1,\qquad C_1=2t-1,\qquad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$


Retain the actual divisions


$$
d=a_Nb_{N-1}-a_{N-1}b_N,\qquad
g_B=\gcd(b_{N-1},b_N)>0,
$$




$$
\alpha=\frac{b_{N-1}}{g_B},\qquad
\beta=\frac{b_N}{g_B},\qquad
\delta=\frac d{g_B}.
$$


Thus


$$
F=\alpha C_N-\beta C_{N-1},
\qquad F(i)=F(-i)=\delta,
\qquad \gcd(\alpha,\beta)=1.
$$



For an integer polynomial $H$, use


$$
\eta(H)=\sum_{j\ge0}j![z^j]H(1-z),
\qquad
E(H)=\sum_{j\ge0}(-1)^jj![t^j]H(t).
$$


These agree with the integral and endpoint definitions in the sources.

Put


$$
\mathcal H(t)=t(1-t)(1+t^2)^2,
\qquad K=\mathcal H C_m^2,
$$




$$
U=-\eta(K),\qquad
V=\eta(F^2)-\delta^2,\qquad
c=\gcd(U,V).
$$


The established normalization is retained:


$$
\operatorname{cont}(W_{\rm raw})=g_B^2c,
$$




$$
\tau=U/c,\qquad \nu=V/c,\qquad
\gcd(\tau,\nu)=1,
$$




$$
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2.
$$


On the original domain, $U,V,M>0$.

In particular, every valuation of $V$ below is a valuation **after** the $g_B$-division. No prime of $g_B$ is inverted in the new arguments.

### 1.2 Both arcs, both least clearers, and the final gcd

Retain


$$
E_F=E(F^2),\qquad E_K=E(K),
$$




$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,
\qquad
R_K=4\int_0^1\frac{K}{1+t^2}\,dt.
$$


The monic quotient polynomials have degree at most $2N-2$.

After reducing both arcs completely, set


$$
D=\operatorname{lcm}\bigl(\operatorname{den}(R_F),
                         \operatorname{den}(R_K)\bigr),
$$




$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$


Independently reduce the aggregate arc:


$$
\tau R_F+\nu R_K=\frac b\lambda,\qquad
\gcd(b,\lambda)=1,\quad \lambda>0.
$$


Then


$$
E=\tau E_F+\nu E_K,\qquad
A=\lambda E-b,\qquad G=\gcd(M,A),
$$


and the actual primitive pair is


$$
\boxed{p_N=\frac AG,\qquad q_N=\frac{\lambda M}{G}.}
$$


The gcd $G$ is over **all primes**.

The established reconciliations remain


$$
\tau X+\nu Y=\frac D\lambda A,
$$




$$
\gcd(D\tau\delta^2,\tau X+\nu Y)=\frac D\lambda G,
$$




$$
D\mid\operatorname{lcm}(1,\ldots,2N-1),\qquad D<256^N.
$$



### 1.3 The reduced $K$-arc and the unpaid multiplier

Write


$$
x=\ell^2,\qquad
L(x)=(x-1)(x-9)(x-25),
$$




$$
A_K(x)=13x^3-455x^2+3502x-5850.
$$


The retained exact reduction is


$$
R_K=\frac{A_K(x)}{30L(x)}=\frac{a_K}{d_K},
$$


where


$$
g_{\rm arc}
=90\,5^{\varepsilon_5}19^{\varepsilon_{19}}31^{\varepsilon_{31}},
$$




$$
\varepsilon_5=\mathbf1_{u\equiv1\pmod5},\quad
\varepsilon_{19}=\mathbf1_{u\equiv3\pmod9},\quad
\varepsilon_{31}=\mathbf1_{u\equiv5,7\pmod{15}},
$$


and


$$
a_K=A_K(x)/g_{\rm arc},\qquad
d_K=30L(x)/g_{\rm arc}.
$$


In particular,


$$
\gcd(a_K,d_K)=1,\qquad
0<a_K<10N^6,\qquad
0<d_K<\frac{64}{3}N^6.
$$



Set


$$
y_K=d_KE_K-a_K,\qquad \mu=D/d_K.
$$


Then


$$
\gcd(d_K,y_K)=1,\qquad Y=\mu y_K.
$$



The intrinsic factors remain


$$
\mathfrak J^0=\gcd(U,Vy_K)
=c\gcd(\tau,y_K),
\qquad
\mathfrak J=\gcd(U,VY),
$$


with


$$
\mathfrak J^0\mid\mathfrak J\mid\mu\mathfrak J^0,
\qquad
U/\mathfrak J\mid q_N.
$$



Write


$$
\gamma=\gcd(\tau,y_K),\qquad
b^\circ=\gcd(\gamma,a_K),\qquad
r^\circ=\gamma/b^\circ.
$$


The turn14 separation and turn15 fixed-product theorem are reused at their stated scope, with their reported independent-audit status unchanged. In particular,


$$
b^\circ<10N^6
$$


and


$$
r^\circ\sqrt{\frac c{\kappa^{\mathrm{prod}}}}
<d_K36^NN!.
$$


Their proofs are not repeated.

For each prime $p$, put


$$
c_p=\min\{v_p(U),v_p(V)\},\qquad
t_p=v_p(U)-c_p,\qquad z_p=v_p(y_K),
$$




$$
h_p=v_p(Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}),
\qquad b_p=v_p(b^\circ).
$$


The exact target is


$$
\boxed{
k_p:=v_p(\kappa^{\mathrm{prod}})
=
[c_p-h_p-2b_p-2(z_p-t_p)_+]_+.
}
\tag{1.1}
$$



---

## 2. A factorial-moment divided-difference lemma

The new depth estimate comes from the actual Chebyshev factorial coefficients. It does not follow merely from continuity of polynomial coefficients modulo $p$: a one-power denominator loss must be paid.

### 2.1 The coefficient formula

For an integer $L\ge0$, define


$$
C_L^+(z)=T_L(1-2z).
$$


For $1\le r\le L$,


$$
[z^r]C_L^+(z)
=
(-1)^r\frac{4^r}{(2r)!}
L^2\prod_{j=1}^{r-1}(L^2-j^2).
\tag{2.1}
$$


The coefficient at $r=0$ is $1$.

Let $s$ be a positive integer, let $p>2s$ be an odd prime, and suppose


$$
a=v_p(L^2-s^2)\ge1.
$$


Since $p>2s$, $p\nmid Ls$, and exactly one of $L-s,L+s$ is divisible by $p$.

### Lemma 2.1 — The one-power factorial bill

For every coefficient index $r$, the factorial-weighted divided difference satisfies


$$
\boxed{
v_p\!\left(
r!\,[z^r]\frac{C_L^+(z)-C_s^+(z)}{L^2-s^2}
\right)\ge-1.
}
\tag{2.2}
$$



#### Proof

For $r\le s$, the coefficient is a polynomial divided difference in $L^2$, with denominator dividing $(2r)!$. Since $p>2s$, that denominator is a $p$-adic unit. Its valuation is therefore nonnegative.

Now let $r>s$. The coefficient of $C_s^+$ vanishes, and the factor $L^2-s^2$ occurs in the numerator of (2.1). It remains to compare the valuation of


$$
\frac{r!}{(2r)!}
\frac{L^2\prod_{j=1}^{r-1}(L^2-j^2)}{L^2-s^2}.
\tag{2.3}
$$



Fix a prime power $q=p^b$.

If $b\le a$, then $L\equiv s$ or $-s\pmod q$. After deleting the factor corresponding to $j=s$, the number of numerator factors divisible by $q$ is


$$
\left\lfloor\frac{r-1-s}{q}\right\rfloor+
\left\lfloor\frac{r-1+s}{q}\right\rfloor.
\tag{2.4}
$$


The denominator contribution, after multiplication by $r!$, is


$$
\left\lfloor\frac{2r}{q}\right\rfloor-
\left\lfloor\frac r q\right\rfloor.
\tag{2.5}
$$



Write $r=kq+t$, $0\le t<q$. Because $q>2s$, subtraction of (2.5) from (2.4) is nonnegative whenever $q\le r$. When $q>r$, it can be negative only for


$$
r<q<2r,
$$


and then it is at least $-1$. There is at most one power of an odd prime in that interval.

If $b>a$, neither deleted factor $L-s,L+s$ is divisible by $q$. Apart from the extra unit $L$, the original numerator is the product of the $2r-1$ consecutive integers


$$
L-r+1,\ldots,L+r-1.
$$


It consequently contains at least


$$
\left\lfloor\frac{2r-1}{q}\right\rfloor
$$


multiples of $q$. Its contribution minus (2.5) is nonnegative. Indeed, the only possible loss from replacing $2r$ by $2r-1$ occurs when $q\mid 2r$; because $q$ is odd, then $q\mid r$, and $\lfloor r/q\rfloor$ pays that loss.

Summing over $b$, the total deficit is at most one. The factor $4^r$ is a $p$-adic unit. This proves (2.2). ∎

### 2.2 Multiplication by the original $\mathcal H$

Multiplying a coefficient of degree $r$ by a fixed integer polynomial and then taking a factorial moment replaces $r!$ by $(r+j)!$, for some $j\ge0$. The quotient


$$
(r+j)!/r!
$$


is an integer, so it cannot worsen (2.2).

Therefore


$$
\eta\!\left(\mathcal H(C_L-C_s)\right)
\equiv0\pmod{p^{a-1}}.
\tag{2.6}
$$



For the original $L=\ell$, $L$ is even, whereas $s=1,3,5$ is odd. At the other endpoint,


$$
C_\ell(t)=C_\ell^+(t),\qquad
C_s(t)=-C_s^+(t).
$$


The same argument, including the alternating factorial signs in $E$, gives


$$
E\!\left(\mathcal H(C_\ell+C_s)\right)
\equiv0\pmod{p^{a-1}}.
\tag{2.7}
$$



The different signs in (2.6) and (2.7) are essential. They are the two different affine boundary constants in this specialization.

Since


$$
C_m^2=\frac{1+C_\ell}{2},
$$


define


$$
\mathfrak u_s
=-\eta\!\left(\frac{\mathcal H(1+C_s)}2\right),
\qquad
\mathfrak e_s
=E\!\left(\frac{\mathcal H(1-C_s)}2\right).
\tag{2.8}
$$


These are integers: $1\pm C_s$ have even coefficients.

We have proved the following original-source congruences.

### Theorem 2.2 — Stability at the three actual arc roots

Let $p\ge17$, $s\in\{1,3,5\}$, and


$$
a=v_p(\ell^2-s^2)\ge1.
$$


Then, at the original index $N$,


$$
\boxed{
U\equiv\mathfrak u_s\pmod{p^{a-1}},
\qquad
E_K\equiv\mathfrak e_s\pmod{p^{a-1}}.
}
\tag{2.9}
$$



All polynomial degrees used in this proof are at most $\ell+6=2N$. No endpoint or recurrence is extended beyond the original terminal.

---

## 3. Evaluation of both forcing constants

The constants in (2.8) must be evaluated; leaving them as named moments would not provide the claimed depth cap.

We have


$$
\mathcal H(1-z)
=4z-12z^2+16z^3-12z^4+5z^5-z^6.
$$


Put


$$
M_j=\eta\!\left(z^j\mathcal H(1-z)\right)
=\sum_{r=1}^{6}[z^r]\mathcal H(1-z)\,(r+j)!,
$$


where this displayed notation denotes the finite factorial sum, not a second application of $\eta$.

The needed values are


$$
\begin{array}{c|r|r}
j&M_j&A_j\\ \hline
0&-332&903\\
1&-2560&6056\\
2&-22104&47070\\
3&-211584&414864\\
4&-2225760&4083240\\
5&-25539840&44357760
\end{array}
\tag{3.1}
$$


where


$$
A_j=(j+1)!+(j+2)!+2(j+3)!+2(j+4)!+(j+5)!+(j+6)!.
$$


Thus


$$
E(t^j\mathcal H)=(-1)^{j+1}A_j.
$$



The three source-side factors, in the $z=1-t$ coordinate, are


$$
\frac{1+C_1(1-z)}2=1-z,
$$




$$
\frac{1+C_3(1-z)}2=1-9z+24z^2-16z^3,
$$




$$
\frac{1+C_5(1-z)}2
=1-25z+200z^2-560z^3+640z^4-256z^5.
$$


The endpoint-side factors $(1-C_s(t))/2$ have these same displayed coefficient lists in $t$.

Substitution into (3.1) gives


$$
\boxed{
\begin{array}{c|r|r}
s&\mathfrak u_s&\mathfrak e_s\\ \hline
1&-2228&-6959\\
3&-2877556&-7822911\\
5&-5227842548&-14210750303
\end{array}
}
\tag{3.2}
$$



For example,


$$
-\mathfrak u_3
=M_0-9M_1+24M_2-16M_3
=2877556,
$$


whereas


$$
\mathfrak e_3
=-A_0-9A_1-24A_2-16A_3
=-7822911.
$$


This explicitly verifies that the two forcing constants are different.

---

## 4. An actual upper bound for a band of the unpaid mass

Define


$$
\mathcal B_N=
\left\{
p\ge17:
\text{ for some }s\in\{1,3,5\},
\ v_p(\ell^2-s^2)\ge v_p(\mathfrak u_s)+2
\right\}.
\tag{4.1}
$$


For $p\ge17$, at most one of the three choices of $s$ is possible: the pairwise differences among $1,9,25$ have no prime divisor at least $17$.

### Theorem 4.1 — Bounded unpaid mass on the deep arc-root band

At every original $N$,


$$
\boxed{
\prod_{p\in\mathcal B_N}p^{\,v_p(\kappa^{\mathrm{prod}})}
\ \bigm|\
2228\cdot2877556\cdot5227842548.
}
\tag{4.2}
$$


In particular,


$$
\boxed{
\sum_{p\in\mathcal B_N}
[c_p-h_p-2b_p-2(z_p-t_p)_+]_+\log p
<47.
}
\tag{4.3}
$$



#### Proof

Fix $p\in\mathcal B_N$, and let $s$ be its unique associated root. Write


$$
a=v_p(\ell^2-s^2),\qquad d_s=v_p(\mathfrak u_s).
$$


The defining condition gives $a-1>d_s$. By Theorem 2.2,


$$
U\equiv\mathfrak u_s\pmod{p^{a-1}},
$$


so the two summands have unequal valuations, and therefore


$$
\boxed{v_p(U)=d_s.}
\tag{4.4}
$$


Consequently,


$$
c_p\le d_s.
$$



For completeness, these are actual denominator primes. The numerator values at the three roots are


$$
A_K(1)=-2790,\qquad
A_K(9)=-1710,\qquad
A_K(25)=450.
$$


At $p\ge17$, the supplied exact arc reduction removes at most one power of $p$. Since $a\ge2$, $p\mid d_K$. Hence


$$
z_p=0,\qquad b_p=0,
$$


and the displayed unpaid depth is exactly


$$
k_p=[c_p-h_p]_+\le c_p\le d_s.
\tag{4.5}
$$


Thus the contribution assigned to root $s$ divides $|\mathfrak u_s|$. Multiplication over the disjoint three root bands proves (4.2).

Finally,


$$
2228<2^{12},\quad
2877556<2^{22},\quad
5227842548<2^{33},
$$


so the logarithm of the right side of (4.2) is less than


$$
67\log2<47.
$$


This proves (4.3). ∎

### 4.1 What has actually been paid

Outside the fixed prime divisors of


$$
C_*:=2228\cdot2877556\cdot5227842548,
$$


the theorem says simply:


$$
\boxed{
p\ge17,\quad
p^2\mid(\ell^2-1)(\ell^2-9)(\ell^2-25)
\quad\Longrightarrow\quad p\nmid U.
}
\tag{4.6}
$$



At the fixed exceptional primes dividing $C_*$, the theorem gives the stated exact cap once the arc-root depth exceeds $v_p(\mathfrak u_s)+1$.

This is an upper valuation result in the required direction. It follows from congruence to a specific nonzero integer at a strictly larger modulus. It is not an inference from a determinant lower bound.

### 4.2 What it does not pay

Every prime $p>N$ is outside this deep band. Indeed,


$$
0<\ell-s<\ell+s\le2N-1,
$$


and, for $p>N$, neither linear factor can be divisible by $p^2$; also $p$ cannot divide both.

Thus the theorem leaves every possible large-prime source depth in the remaining obligation. It does not turn an archimedean $N!$-bound into factorial divisibility.

Nor is there a proved lower bound on how much potential mass lies in $\mathcal B_N$. The estimate (4.3), although uniform and source-specific, does not itself yield a fixed fractional-factorial saving.

---

## 5. The binary unpaid depth vanishes

This is a short new consequence of the actual Gaussian division, using the established determinant-$2$ payment rather than repeating it.

Modulo $4$, the Chebyshev recurrence gives


$$
C_{2j}(t)\equiv1,\qquad
C_{2j+1}(t)\equiv2t-1.
\tag{5.1}
$$


Therefore, for odd $N$,


$$
4\mid b_{N-1},\qquad b_N\equiv2\pmod4.
$$


It follows that


$$
v_2(g_B)=1,\qquad \alpha\ \text{is even},\qquad \beta\ \text{is odd}.
$$


Also $\delta$ is odd. Hence


$$
F^2\equiv1\pmod4,\qquad \delta^2\equiv1\pmod4,
$$


as integer-polynomial and integer congruences, respectively. Since $\eta$ is an integer linear functional,


$$
4\mid V.
$$



Reuse the established values


$$
v_2(U)=2,\qquad v_2(y_K)=1,
$$


and the oddness of the Hermite denominators. Then


$$
c_2=2,\qquad t_2=0,\qquad b_2=0,\qquad h_2=0.
$$


Formula (1.1) yields


$$
\boxed{v_2(\kappa^{\mathrm{prod}})=0.}
\tag{5.2}
$$



No division by $4096$ or by the determinant $2$ was made modulo $2$.

---

## 6. An evaluated first jet at $p\mid 2N-1$

The preceding stability theorem deliberately leaves a one-power loss. The next calculation evaluates that loss for one actual arc branch, including the changing divided Gaussian data and both forcing states.

Let


$$
p\ge17,\qquad p\mid2N-1.
$$


Write


$$
2N-1=ap,\qquad
k=\frac{p+1}{2}.
$$


Because $N$ and $p$ are odd, $a$ is odd. Set


$$
b=\frac{a-1}{2},\qquad
\varsigma=(-1)^b,\qquad
\chi=a\,k!\,\varsigma,
\tag{6.1}
$$


and retain the actual Gaussian integer


$$
D_{\rm G}=\alpha^2-\beta^2.
\tag{6.2}
$$



Define the fixed coprime integers


$$
\boxed{
A_0=1629588422,\qquad B_0=395174561,
}
\tag{6.3}
$$


and the actual Hermite combinations


$$
L_Q=A_0Q_N^{\mathrm H}+B_0Q_{N-1}^{\mathrm H},
$$




$$
L_P=A_0P_N^{\mathrm H}+B_0P_{N-1}^{\mathrm H}.
\tag{6.4}
$$



### Theorem 6.1 — Complete original-source first jet

At every original $N$, for every prime $p\ge17$ dividing $2N-1$,


$$
\boxed{
\begin{aligned}
4U&\equiv4\mathfrak u_5-45\chi L_Q,\\
V&\equiv-\delta^2+2\chi D_{\rm G}Q_N^{\mathrm H},\\
4E_K&\equiv4\mathfrak e_5+45\varsigma\chi L_P,\\
E_F&\equiv2(\alpha+\beta)^2
       +2\varsigma\chi D_{\rm G}P_N^{\mathrm H}
\end{aligned}
\pmod p.
}
\tag{6.5}
$$


Here


$$
\mathfrak u_5=-5227842548,\qquad
\mathfrak e_5=-14210750303.
$$



These congruences use the actual $\alpha,\beta,\delta$. They remain valid when $p\mid g_B$, because no inverse of $g_B$, $\alpha$, $\beta$, or $\delta$ is used.

The proof follows.

---

## 7. Proof of the first-jet theorem

### 7.1 Factorial moments are finite jets modulo $p$

Modulo $p$, $\eta(H)$ depends only on


$$
H(1-z)\pmod{z^p},
$$


because $p\mid j!$ for $j\ge p$. Similarly, $E(H)$ depends only on


$$
H(t)\pmod{t^p}.
$$



Every auxiliary expression below is projected into one of these degree-$<p$ jet rings **before** applying the moment. Since


$$
p-1\le2N-2,
$$


these evaluated jets lie inside the original physical terminal.

### 7.2 Chebyshev Frobenius identities

Let $w=2t-1$. Over $\mathbb F_p[w]$,


$$
T_p(w)=w^p,\qquad
U_{p-1}(w)=(w^2-1)^{(p-1)/2},
\tag{7.1}
$$


where $U_j$ denotes the Chebyshev polynomial of the second kind.

For example, these identities follow by substituting


$$
w=(z+z^{-1})/2
$$


into the usual Laurent formulas and applying Frobenius. The Laurent substitution is injective on $\mathbb F_p[w]$, so this proves polynomial identities.

Put


$$
D_s(w)=(w^2-1)^{(p+1)/2}U_{s-1}(w).
\tag{7.2}
$$


The addition formulas give, near $t=1$,


$$
C_{ap+s}\equiv C_s+aD_s,\qquad
C_{ap-s}\equiv C_s-aD_s
\pmod{p,(1-t)^p}.
\tag{7.3}
$$


Near $t=0$, because $a$ is odd,


$$
C_{ap+s}\equiv-C_s+aD_s,\qquad
C_{ap-s}\equiv-C_s-aD_s
\pmod{p,t^p}.
\tag{7.4}
$$


Also


$$
C_{ap}\equiv1\pmod{p,(1-t)^p},
\qquad
C_{ap}\equiv-1\pmod{p,t^p}.
\tag{7.5}
$$



The constants $1$ and $-1$ in (7.5) are precisely why the two endpoint forcing constants must not be merged.

Here


$$
n=ap+1,\qquad \ell=ap-5.
\tag{7.6}
$$



### 7.3 Hermite residues, without an enlarged endpoint range

The established Hermite coefficient formula is


$$
a_{r,j}=\frac{(r+j)!}{j!(r-j)!},
$$


with the corresponding endpoint sums for $P_r^{\mathrm H}$ and $Q_r^{\mathrm H}$.

For $r=p,p-1$, every term with $j\ge1$ is divisible by $p$. Thus, whenever these indices lie in the original range,


$$
P_p^{\mathrm H}\equiv P_{p-1}^{\mathrm H}\equiv1,
$$




$$
Q_p^{\mathrm H}\equiv-1,\qquad
Q_{p-1}^{\mathrm H}\equiv1
\pmod p.
$$


The recurrence coefficients are periodic modulo $p$, so, only for indices whose two sides are at most $N$,


$$
P_{r+p}^{\mathrm H}\equiv P_r^{\mathrm H},
\qquad
Q_{r+p}^{\mathrm H}\equiv-Q_r^{\mathrm H}
\pmod p.
\tag{7.7}
$$



Since $N=bp+k$,


$$
P_N^{\mathrm H}\equiv P_k^{\mathrm H},\qquad
Q_N^{\mathrm H}\equiv\varsigma Q_k^{\mathrm H},
\tag{7.8}
$$


and similarly at $N-1,k-1$.

If $p>N$, then necessarily $p=2N-1$, $a=1$, and $k=N$; in this case (7.8) is an identity and no period step is used.

A second useful finite identity is reflection. If


$$
k\le r<p,
$$


the factorial coefficient product


$$
a_{r,j}=\frac1{j!}
\prod_{i=0}^{j-1}(r-i)(r+i+1)
$$


is congruent modulo $p$ to its counterpart at $p-1-r$; terms beyond that smaller index vanish. Hence the projected moments of $v^r$, where $v=t(1-t)$, are


$$
\eta(v^r)\equiv(-1)^rr!Q_{p-1-r}^{\mathrm H},
$$




$$
E(v^r)\equiv(-1)^rr!P_{p-1-r}^{\mathrm H}
\pmod p.
\tag{7.9}
$$


Only the reflected indices are used as endpoint objects.

In the calculation below those indices range from


$$
\frac{p-13}{2}\quad\text{to}\quad\frac{p-5}{2},
$$


and then up to $k$. They are nonnegative and at most $N$.

### 7.4 Evaluation of the $K$-defect

We have


$$
w^2=1-4v,\qquad
U_4(w)=5-80v+256v^2,
$$


and


$$
(1+t^2)^2
=\left(\frac52-4v+v^2\right)
+w\left(\frac32-v\right).
\tag{7.10}
$$


Also,


$$
wv^r=-\frac{(v^{r+1})'}{r+1}.
$$


Both endpoint functionals satisfy


$$
\eta((v^{r+1})')=-\eta(v^{r+1}),
\qquad
E((v^{r+1})')=-E(v^{r+1}),
$$


because $v^{r+1}$ vanishes at both endpoints. Thus


$$
\eta(wv^r)=\frac{\eta(v^{r+1})}{r+1},
\qquad
E(wv^r)=\frac{E(v^{r+1})}{r+1}.
\tag{7.11}
$$


Every denominator $r+1$ used here is less than $p$, so it is a unit modulo $p$.

Put


$$
R=k+1=\frac{p+3}{2}.
$$


After extracting the common factor $(-1)^RR!$, the three projected moments of


$$
v^{R+j}(1+t^2)^2,\qquad j=0,1,2,
$$


have the following coefficient pairs in the adjacent reflected endpoint basis:


$$
\begin{array}{c|c}
j&\text{coefficient pair}\\ \hline
0&(35,\ 334)/4\\
1&(-4170,\ -50335)/8\\
2&(947345,\ 11427150)/16.
\end{array}
\tag{7.12}
$$


For verification, the required backward recurrence coefficients are exactly


$$
12,\quad16,\quad20.
$$


Combining (7.12) with $5-80v+256v^2$ gives


$$
(60797055,\ 733352670)/4.
\tag{7.13}
$$



Let $j_0=(p-5)/2=k-3$. The recurrence, entirely within indices at most $k$, gives


$$
Z_{j_0}\equiv4Z_k+Z_{k-1},
\qquad
Z_{j_0-1}\equiv33Z_k+8Z_{k-1}
\pmod p
\tag{7.14}
$$


for either endpoint sequence $Z=P^{\mathrm H},Q^{\mathrm H}$.

The resulting coefficient pair is


$$
\begin{aligned}
&(4\cdot60797055+33\cdot733352670,\,
  60797055+8\cdot733352670)\\
&\hspace{10mm}
=(24443826330,\ 5927618415)
=15(A_0,B_0).
\end{aligned}
\tag{7.15}
$$



Since


$$
\mathcal H D_5
=(-4)^k v^{k+1}(1+t^2)^2U_4(w)
$$


and $4^k\equiv4\pmod p$, equations (7.10)–(7.15) yield


$$
\eta(\mathcal H D_5)
\equiv-15R!\bigl(A_0Q_k^{\mathrm H}
                 +B_0Q_{k-1}^{\mathrm H}\bigr),
\tag{7.16}
$$




$$
E(\mathcal H D_5)
\equiv-15R!\bigl(A_0P_k^{\mathrm H}
                 +B_0P_{k-1}^{\mathrm H}\bigr).
\tag{7.17}
$$


Finally,


$$
R!=(k+1)k!\equiv\frac32k!\pmod p.
$$



Using $\ell=ap-5$ in (7.3)–(7.4), then using the constants from (3.2), proves the first and third congruences in (6.5).

### 7.5 Evaluation of the divided Gaussian square defect

The exact square identity is


$$
F^2=
\frac{\alpha^2+\beta^2}{2}
+\frac{\alpha^2}{2}C_n
+\frac{\beta^2}{2}C_{n-2}
-\alpha\beta(C_{n-1}+C_1).
\tag{7.18}
$$


At $n=ap+1$, its source-side constant is zero, because


$$
\eta(C_1)=-1,\qquad \eta(1)=1.
$$


After the required subtraction of $\delta^2$, the complete source constant is therefore $-\delta^2$.

At the other endpoint,


$$
E(C_1)=-3,\qquad E(1)=1,
$$


and the signs in (7.4)–(7.5) give the complete constant


$$
2(\alpha^2+\beta^2)+4\alpha\beta
=2(\alpha+\beta)^2.
$$


The $4\alpha\beta$ term has not disappeared.

The remaining defect in both cases is $aD_{\rm G}D_1/2$. Its projected moments are


$$
\eta(D_1)\equiv4k!Q_k^{\mathrm H},
\qquad
E(D_1)\equiv4k!P_k^{\mathrm H}.
$$


Combining these identities with (7.8) proves the second and fourth congruences in (6.5). ∎

---

## 8. What the first jet proves about the unpaid depths

### 8.1 The actual arc removes endpoint surplus on this branch

If $p\ge17$ divides $2N-1=\ell+5$, then


$$
p\nmid\ell-5
$$


and $A_K(25)=450$ is a $p$-adic unit. Therefore


$$
v_p(d_K)=v_p(2N-1)>0,
\qquad
v_p(y_K)=0.
$$


Consequently,


$$
\boxed{
z_p=b_p=0,\qquad
k_p=[c_p-h_p]_+.
}
\tag{8.1}
$$



The first jet is thus being applied directly to a range of the displayed unpaid mass. It is not controlling a different gcd.

### 8.2 Source-specific exclusions

The second congruence in (6.5) immediately gives


$$
\boxed{
p\nmid\delta,\quad
p\mid D_{\rm G}Q_N^{\mathrm H}
\quad\Longrightarrow\quad p\nmid c.
}
\tag{8.2}
$$


This is an actual Gaussian/Hermite exclusion, valid even at primes of the original $g_B$-division.

Conversely, if $p\mid c$ and $p\nmid\delta$, then


$$
p\nmid \chi D_{\rm G}Q_N^{\mathrm H}.
\tag{8.3}
$$


In particular, $p\nmid a$, so the arc-root depth is exactly one.

There is also a first-depth Hermite payment in a different Gaussian case. If


$$
p\mid c,\quad p\mid\delta,\quad
p\nmid D_{\rm G}\mathfrak u_5,
$$


then the first congruence in (6.5) forces $p\nmid\chi$, while the second forces


$$
p\mid Q_N^{\mathrm H}.
$$


Thus $h_p\ge1$, and the first source depth is paid in (8.1).

These are limited, proved prime/depth statements. They do not bound arbitrary further lifts.

### 8.3 The exact remaining source collision

If $p\mid c$, eliminating $\chi$ from the first two congruences in (6.5) gives


$$
\boxed{
\bigl(45A_0\delta^2-8\mathfrak u_5D_{\rm G}\bigr)
Q_N^{\mathrm H}
+
45B_0\delta^2Q_{N-1}^{\mathrm H}
\equiv0\pmod p.
}
\tag{8.4}
$$


Every coefficient here is evaluated in the original divided Gaussian data.

Equation (8.4) is a necessary condition on the actual original source. It is not an upper bound for $c_p$: a congruence can lift. In particular, the fact that its Gaussian coefficients have exponential height does not bound the valuation of the displayed linear combination, whose Hermite coordinates have factorial height.

### 8.4 The full primitive source balance and endpoint forcing remain

The exact equality $\tau V=\nu U$ gives, from (6.5),


$$
\boxed{
\chi\bigl(8\tau D_{\rm G}Q_N^{\mathrm H}
          +45\nu L_Q\bigr)
\equiv4\tau\delta^2+4\nu\mathfrak u_5
\pmod p.
}
\tag{8.5}
$$


No division by $c,\tau,\nu$ is made modulo $p$.

For the actual


$$
T=E-M=\tau(E_F-\delta^2)+\nu E_K,
$$


the matching endpoint congruence is


$$
\boxed{
\begin{aligned}
4T\equiv{}&
4\tau\bigl(2(\alpha+\beta)^2-\delta^2\bigr)
+4\nu\mathfrak e_5\\
&+\varsigma\chi
 \bigl(8\tau D_{\rm G}P_N^{\mathrm H}
       +45\nu L_P\bigr)
\pmod p.
\end{aligned}
}
\tag{8.6}
$$


Thus both forcing constants, the square’s $4\alpha\beta$ contribution, the subtraction of $\delta^2$, and the actual primitive source balance are all present.

The determinant payment is also explicit. Since $N$ is odd,


$$
P_N^{\mathrm H}Q_{N-1}^{\mathrm H}
-P_{N-1}^{\mathrm H}Q_N^{\mathrm H}=2.
$$


At a prime dividing $c$, the four jets imply


$$
\boxed{
\begin{aligned}
&\delta^2(E_K-\mathfrak e_5)
-\mathfrak u_5\bigl(E_F-2(\alpha+\beta)^2\bigr)\\
&\hspace{20mm}
\equiv
-45\varsigma\chi^2D_{\rm G}B_0
\pmod p.
\end{aligned}
}
\tag{8.7}
$$


For example, if $p\nmid\delta B_0$, then (8.3) makes the right side a unit.

This is a nontrivial relation between the two complete affine endpoint states. It is **not** an endpoint-surplus theorem. On this arc branch, $y_K$ is already a unit. Any proof of a uniform saving must therefore control the source collision itself rather than claim that its depth is automatically returned in $y_K$.

No original prime with a given collision is asserted to exist merely because (8.4) is formally possible.

---

## 9. A concrete higher-depth follow-on lemma

The evaluated first jet suggests the following sharply scoped obligation.

> **Regular simple-arc continuation lemma — open.**  
> At every original $N$, let $p\ge17$ satisfy
> 

$$
> p\mid2N-1,\qquad v_p(2N-1)=1,
>
$$


> and
> 

$$
> p\nmid C_*B_0\delta(\alpha^2-\beta^2).
>
$$


> Prove
> 

$$
> \boxed{
> [\,\min(v_p(U),v_p(V))
>       -v_p(Q_{N-1}^{\mathrm H}Q_N^{\mathrm H})\,]_+
> \le1.
> }
> \tag{9.1}
>
$$



This is a higher-precision noncoincidence statement for the actual collision (8.4), not a statement about arbitrary affine triples.

If (9.1) were proved, the entire unpaid mass in its stated regular range would be at most


$$
\sum_{p\mid2N-1}\log p
\le\log(2N-1).
$$


That conditional implication is rigorous.

The lemma itself is not proved here. A proof must evaluate the next forced jet, or a higher jet after the Hermite credit, and show that the actual Gaussian-dependent collision does not persist too deeply.

Moreover, even this lemma would leave:

* its Gaussian exceptional primes;
* the other simple arc-root branches;
* primes not dividing $d_K$;
* the general $p>N$ range.

The exponential height of a Gaussian exceptional factor bounds its support-weight, not the source depth at that support. It cannot be substituted for the missing upper valuation estimate.

---

## 10. Complete finite source and return ledger retained

The new proofs above use the original polynomials directly. For identification with the supplied affine system, the following finite data remain unchanged.

### 10.1 Both affine boundary states

For $0\le j\le n$,


$$
\eta(C_j)=1-2j\Theta_j,\qquad
E(C_j)=(-1)^j-2j\Phi_j,
$$


with


$$
\Theta_0=\Phi_0=0,\qquad
\Theta_1=\Phi_1=1.
$$


For exactly $1\le j\le n-1$,


$$
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2,
$$




$$
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j.
$$


Equivalently, the full three-coordinate states are


$$
\begin{pmatrix}\Theta_{j+1}\\\Theta_j\\1\end{pmatrix}
=
\begin{pmatrix}-4j&1&2\\1&0&0\\0&0&1\end{pmatrix}
\begin{pmatrix}\Theta_j\\\Theta_{j-1}\\1\end{pmatrix},
$$




$$
\begin{pmatrix}\Phi_{j+1}\\\Phi_j\\(-1)^{j+1}\end{pmatrix}
=
\begin{pmatrix}-4j&1&2\\1&0&0\\0&0&-1\end{pmatrix}
\begin{pmatrix}\Phi_j\\\Phi_{j-1}\\(-1)^j\end{pmatrix},
$$


with seeds


$$
(1,0,1)^t,\qquad(1,0,-1)^t.
$$


Neither third forcing coordinate has been removed.

### 10.2 All thirteen weights and corrected columns

The weights are


$$
(1,8,58,168,399,-176,-916,-176,399,168,58,8,1).
$$


For $1\le k\le11$,


$$
r_{k+1}=r_{k-1}+4(n-k)r_k,\qquad
s_{k+1}^*=s_{k-1}^*+4(n-k)s_k^*,
$$




$$
\kappa_{k+1}=\kappa_{k-1}+4(n-k)\kappa_k-2,
$$




$$
\omega_{k+1}=\omega_{k-1}+4(n-k)\omega_k-2(-1)^k,
$$


with


$$
(r_0,s_0^*)=(1,0),\qquad(r_1,s_1^*)=(0,1),
$$




$$
\kappa_0=\kappa_1=\omega_0=\omega_1=0.
$$


Retain


$$
\mathsf A=\sum_{k=0}^{12}w_k(n-k)r_k,\qquad
\mathsf B=\sum_{k=0}^{12}w_k(n-k)s_k^*,
$$




$$
\mathsf C_U=679936-\sum_{k=0}^{12}w_k(n-k)\kappa_k,
$$




$$
\mathsf C_E=-1849344+\sum_{k=0}^{12}w_k(n-k)\omega_k.
$$


Then


$$
4096U=\mathsf C_U-\mathsf A\Theta_n-\mathsf B\Theta_{n-1},
$$




$$
4096E_K=\mathsf C_E+\mathsf A\Phi_n+\mathsf B\Phi_{n-1}.
$$



For the actually divided Gaussian square,


$$
\mathsf P=n\alpha^2+(n-2)\beta^2,
$$




$$
\mathsf Q=4(n-1)(n-2)\beta^2-2(n-1)\alpha\beta,
$$




$$
\mathsf C_V=\alpha^2+(2n-3)\beta^2-\delta^2,
$$




$$
\mathsf C_F^E=\alpha^2+(5-2n)\beta^2+4\alpha\beta,
$$


and


$$
V=\mathsf C_V-\mathsf P\Theta_n-\mathsf Q\Theta_{n-1},
$$




$$
E_F=\mathsf C_F^E-\mathsf P\Phi_n-\mathsf Q\Phi_{n-1}.
$$



The original source balance is


$$
\begin{aligned}
&(\nu\mathsf A-4096\tau\mathsf P)\Theta_n
+(\nu\mathsf B-4096\tau\mathsf Q)\Theta_{n-1}\\
&\hspace{15mm}
=\nu\mathsf C_U-4096\tau\mathsf C_V.
\end{aligned}
$$


The corresponding complete endpoint is


$$
\begin{aligned}
4096T={}&
4096\tau(\mathsf C_F^E-\delta^2)+\nu\mathsf C_E\\
&+(\nu\mathsf A-4096\tau\mathsf P)\Phi_n
+(\nu\mathsf B-4096\tau\mathsf Q)\Phi_{n-1}.
\end{aligned}
$$


The new jets in Section 8 are evaluations of these original objects, not replacements for them.

### 10.3 Rational interface and its bills

For $j\ge1$,


$$
s_j=\frac1j-2\Theta_j,
$$


and only on $2\le j\le n-1$,


$$
s_{j-1}=s_{j+1}+4js_j+\frac2{j^2-1},
$$


with


$$
S_0=1,\qquad s_1=-1,\qquad s_2=9/2.
$$


The local constants are


$$
e_k=\frac1{n-k}-\frac{r_k}{n}
-\frac{s_k^*}{n-1}-2\kappa_k.
$$


Their divisions are paid by


$$
Q_{\rm loc}(n)=\prod_{r=0}^{12}(n-r).
$$


The global forcing is paid by


$$
\mathcal L_n=\operatorname{lcm}(1,\ldots,n),\qquad
\frac{2\mathcal L_n}{j^2-1}
=\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}.
$$


Neither clearer replaces $D$.

The complete affine constants remain


$$
\mathsf E
=2\mathsf C_U-\frac{\mathsf A}{n}-\frac{\mathsf B}{n-1},
$$




$$
2\mathsf C_V=\frac{\mathsf P}{n}
+\frac{\mathsf Q}{n-1}
+(\alpha+\beta)^2-2\delta^2+\frac{2\beta^2}{n}.
$$



### 10.4 Source, endpoint, and arc returns

With


$$
\Delta=\mathsf A\mathsf Q-\mathsf B\mathsf P,
$$


retain


$$
z_n=4096\mathsf Q U-\mathsf B V,\qquad
z_{n-1}=\mathsf A V-4096\mathsf P U,
$$




$$
z_j=-\Delta\Theta_j+\varrho_j,\qquad
z_{j-1}=z_{j+1}+4jz_j,
$$




$$
\varrho_{j-1}=\varrho_{j+1}+4j\varrho_j-2\Delta,
$$


with


$$
\varrho_n=\mathsf Q\mathsf C_U-\mathsf B\mathsf C_V,
\qquad
\varrho_{n-1}=\mathsf A\mathsf C_V-\mathsf P\mathsf C_U.
$$


The rational forcing form is


$$
2z_j=\Delta s_j+\rho_j,\qquad
\rho_j=2\varrho_j-\Delta/j,
$$




$$
\rho_{j-1}=\rho_{j+1}+4j\rho_j-\frac{2\Delta}{j^2-1}.
$$



For the endpoint return,


$$
k_E=D\mathsf C_E-4096DR_K,\qquad
f_E=D\mathsf C_F^E-DR_F,
$$




$$
w_n=4096\mathsf QY+\mathsf B X,\qquad
w_{n-1}=-4096\mathsf PY-\mathsf A X,
$$




$$
w_j=D\Delta\Phi_j+\sigma_j,
$$




$$
\sigma_n=\mathsf Qk_E+\mathsf Bf_E,\qquad
\sigma_{n-1}=-\mathsf Pk_E-\mathsf Af_E,
$$




$$
w_{j-1}=w_{j+1}+4jw_j,
$$




$$
\sigma_{j-1}
=\sigma_{j+1}+4j\sigma_j+2D\Delta(-1)^j.
$$


The determinant remains


$$
z_nw_{n-1}-z_{n-1}w_n
=-4096\Delta(UX+VY).
$$


There is no division by $\Delta$.

The complete square-arc recurrence, with zero initial values at $j=0,1$, remains


$$
\xi_{j+1}=4\upsilon_j-2\xi_j-\xi_{j-1}+16b_j,
$$




$$
\upsilon_{j+1}
=-4\xi_j-2\upsilon_j-\upsilon_{j-1}
+16(\ell_j-a_j),
$$


where


$$
\ell_j=
\begin{cases}
0,&j\text{ odd},\\
(1-j^2)^{-1},&j\text{ even},
\end{cases}
$$


and


$$
R_F=
\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
      -2\alpha\beta\xi_{n-1}}2.
$$


All its rational divisions continue to be reconciled with the actual least arc clearer.

The previously established analytic comparisons retain their original finite boundaries and cutoff $k\ge512$. They are not used as numerical gcd estimates here.

---

## 11. Remaining mass and the actual whole-error budget

The proved arithmetic reduction is


$$
v_2(\kappa^{\mathrm{prod}})=0,
$$


and


$$
\sum_{p\in\mathcal B_N}v_p(\kappa^{\mathrm{prod}})\log p<47.
$$


Thus the remaining obligation is the actual complementary mass


$$
\boxed{
\sum_{\substack{p\notin\mathcal B_N\\p\ne2}}
[c_p-h_p-2b_p-2(z_p-t_p)_+]_+\log p.
}
\tag{11.1}
$$


No strict fractional-factorial bound for (11.1) is established.

The turn15 implication remains available without redoing its proof:


$$
\log\mathfrak J_N^0
\le\frac32N\log N
+\frac12\log\kappa_N^{\mathrm{prod}}+O(N).
$$


Consequently, a future proof of


$$
\kappa_N^{\mathrm{prod}}
\le(N!)^{1-\eta}e^{CN},
\qquad \eta>0,
$$


would give


$$
\log\mathfrak J_N^0
\le\left(2-\frac\eta2\right)N\log N+O(N).
$$



The producer itself remains unchanged:


$$
P_N(t)=\frac{F(t)^2+(V/U)K(t)}{\delta^2},
$$




$$
\boxed{
\epsilon_N=
\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0,
}
$$




$$
\boxed{
q_N(e+\pi)-p_N=q_N\epsilon_N>0,
\qquad q_N=\frac{\lambda_NM_N}{G_N}.
}
$$



The complete rational enclosure is still


$$
3J_N<\epsilon_N<7J_N,
\qquad
J_N=\frac{J_F+(V/U)J_K}{\delta^2},
$$


where


$$
J_F=
\alpha^2\frac{2N^2-1}{4N^2-1}
+\beta^2\frac{2(N-1)^2-1}{4(N-1)^2-1},
$$


and, with $j_r=(1-4r^2)^{-1}$,


$$
J_K=\frac{61}{420}
+\frac{
916j_m-399(j_{m+1}+j_{m-1})
-58(j_{m+2}+j_{m-2})
-(j_{m+3}+j_{m-3})
}{8192}.
$$


Hence


$$
q_NJ_N
=\frac{\lambda_N}{G_N}
\bigl(\tau_NJ_F+\nu_NJ_K\bigr).
$$


Both positive summands remain.

Under the future strict multiplier bound, the established


$$
U/\mathfrak J\mid q_N,\qquad
\mathfrak J\mid\mu\mathfrak J^0,\qquad \mu<256^N,
$$


and


$$
\epsilon_N\asymp R^{-2N},
\qquad
R=1+\sqrt2+\sqrt{2+2\sqrt2},
$$


would yield, at the same original indices,


$$
\log(q_N\epsilon_N)
\ge\frac\eta2N\log N-O(N)\longrightarrow+\infty.
$$


That would retire this producer only. It would not determine the rationality of $e+\pi$.

The new bounded band and first-jet exclusions do not yet justify this conditional conclusion.

---

## 12. Bounded exact-arithmetic audit of the new coefficients

No computation at an original index is needed or proposed. No old source array or small-prime scan should be rerun.

An optional, bounded audit can check the new coefficient receipts in Sections 3 and 7.

### Inputs

1. The polynomial
   

$$
\mathcal H=t-t^2+2t^3-2t^4+t^5-t^6.
$$


2. Only $C_1,C_3,C_5$, of degrees at most $5$.
3. Factorials through $11!$.
4. The identities
   

$$
w^2=1-4v,\qquad
   U_4(w)=5-80v+256v^2,
$$


   

$$
(1+t^2)^2
   =\left(\frac52-4v+v^2\right)
     +w\left(\frac32-v\right).
$$


5. A formal adjacent pair $Z_0,Z_1$ and exactly three recurrence steps
   

$$
Z_2=12Z_1+Z_0,\quad
   Z_3=16Z_2+Z_1,\quad
   Z_4=20Z_3+Z_2.
$$



These are bounded polynomial and rational-arithmetic inputs. There is no prime enumeration and no Gaussian recurrence at a large index.

### Expected verifiable outputs

* The six pairs in (3.1).
* The three source/endpoint constant pairs in (3.2).
* The three coefficient pairs in (7.12).
* Their combination
  

$$
(60797055,\ 733352670)/4.
$$


* The final integral coefficient identity
  

$$
(24443826330,\ 5927618415)
  =15(1629588422,\ 395174561).
$$



The constants can be checked independently by direct polynomial factorial evaluation and by the displayed moment recurrences.

This audit would check fixed algebraic receipts in the new proof. It would not establish the open continuation lemma, a strict multiplier bound, producer retirement, or irrationality of $e+\pi$.

---

## 13. Final proof-status ledger

| Statement | Status |
|---|---|
| Original domain, terminal, Gaussian division, complete forcing and columns | Retained unchanged |
| Least simultaneous $D$, least aggregate $\lambda$, all-prime $G$, actual $q$ | Retained unchanged |
| Turn14 separation and turn15 fixed-product theorem | Reused at their reported scope and review status |
| Factorial divided-difference bound with exactly one $p$-power loss | **Proved here** |
| Both evaluated arc-root forcing constants | **Proved here by bounded exact identities** |
| Entire unpaid mass on $\mathcal B_N$ is $<47$ | **Proved here in the actual positive part** |
| $v_2(\kappa^{\mathrm{prod}})=0$ | **Proved here using the established binary endpoint payment** |
| Complete four-column Gaussian–Hermite jet at $p\mid2N-1$ | **Proved here** |
| Source exclusions and first-depth Hermite payment from that jet | **Proved here at their explicit hypotheses** |
| Higher-lift noncoincidence of the remaining collision | **Open** |
| Fixed $\eta>0$ in a strict sub-factorial bound for $\kappa^{\mathrm{prod}}$ | **Not proved** |
| Retirement of this producer | **Still conditional** |
| Rationality or irrationality of $e+\pi$ | **Open** |

No external gcd theorem is imported. In particular, the Cauchy–Binet lower-valuation mechanism described in the Sun filter does not supply the upper source valuation needed here.

### Final conclusion

The new proved depth result is the uniform, actual bound


$$
\boxed{
\prod_{p\in\mathcal B_N}
p^{\,v_p(\kappa_N^{\mathrm{prod}})}
\mid
2228\cdot2877556\cdot5227842548,
}
$$


together with the fully evaluated original-source jet (6.5).

The precise obstruction is now visible on a concrete unpaid branch. At $p\mid2N-1$, the reduced arc forces $y_K$ to be a unit, while common source divisibility requires the actual Gaussian–Hermite collision (8.4). The first jet does not bound how deeply that collision can lift. Dropping either affine forcing constant would conceal this obstruction rather than resolve it.

A higher-precision noncoincidence proof such as (9.1) would be a concrete next step. It would still need to be supplemented by upper-depth control at the Gaussian exceptional primes, the other arc branches, primes outside $d_K$, and the unrestricted $p>N$ range.

**This report proves a limited source-specific depth payment and an evaluated local coupling, not the requested strict intrinsic-content estimate. The global arithmetic bottleneck and the rationality or irrationality of $e+\pi$ remain unresolved.**
