> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the compact and signed arithmetic theorems

## Executive conclusion

The central arithmetic claims in the four supplied reports pass independent proof audit at their stated scopes:

1. **Compact binary obstruction.** Every maximal minor of the original $Y_k$ has the asserted binary divisor. Consequently,
   

$$
\boxed{\mathcal W_k\notin I_{2k-1}(Y_k)\qquad\text{for every }k\ge18.}
$$


   This is an unconditional disproof of that particular integral descent assertion—not merely a failure to construct its Bézout coefficients.

2. **Compact capped $3$-primary spectrum.** For $k=3^s$, $s\ge4$, the stated Smith spectrum modulo $3^h$ is correct when
   

$$
\boxed{1\le h,\qquad 2h\le s+2.}
$$


   The proof uses the actual scaled return entries, actual physical pivot rows, and the retained contact atom. It does not determine the full maximal contents.

3. **Compact next payment constant.** The constant
   

$$
\boxed{24-18\log3}
$$


   is correct. Its derivation must retain $\zeta_{Z,k}$, $\chi_{Y,k}$, and $2(k-1)\log\Lambda_k$ until their contributions have been bounded.

4. **Signed boundary theorems.** The integral alternating endpoint, dual Wronskian, and every-depth lift congruence are correct. The Wronskian holds at every odd prime; the supplied every-depth proof holds for $p\ge5$, not automatically at $p=3$.

5. **Signed original prime-$5$ exception.** The exact assertion
   

$$
\boxed{
   v_5\gcd(U_{N_u},V_{N_u}y_{K,N_u})
   =\mathbf1_{u\equiv21\pmod{25}}
   }
$$


   passes, including the actual Gaussian unit condition, the complete arc reduction modulo $125$, and the source calculation modulo $25$ that pays the exceptional depth.

There is also a new original-domain result. Write


$$
x=4(N_u-3)^2,\qquad L(x)=(x-1)(x-9)(x-25),
$$


and let $g_{\rm arc}$ be the actual gcd used to reduce the complete $K$-arc. Define


$$
\begin{aligned}
\varepsilon_5(u)&=\mathbf1_{u\equiv1\pmod5},\\
\varepsilon_{19}(u)&=\mathbf1_{u\equiv3\pmod9},\\
\varepsilon_{31}(u)&=\mathbf1_{u\equiv5\text{ or }7\pmod{15}}.
\end{aligned}
$$


Then


$$
\boxed{
g_{\rm arc}
=90\,5^{\varepsilon_5(u)}
       19^{\varepsilon_{19}(u)}
       31^{\varepsilon_{31}(u)}.
}
\tag{N1}
$$


In particular,


$$
\boxed{
g_{\rm arc}\in\{90,450,1710,2790,8550\},
\qquad
d_K=\frac{L(x)}
 {3\,5^{\varepsilon_5(u)}19^{\varepsilon_{19}(u)}31^{\varepsilon_{31}(u)}}.
}
\tag{N2}
$$


Thus the original reduced $K$-arc denominator satisfies the sharper bound


$$
\boxed{d_K\ge \frac{L(x)}{285},\qquad v_2(d_K)=0,\qquad v_3(d_K)=2.}
\tag{N3}
$$



This is an exact original-family arc-denominator result. It is **not** a bound for the final gcd $G$, the simultaneous clearer $D$, or the aggregate signed joint divisor.

No report audited here proves an aggregate saving sufficient to retire either producer. None decides whether $e+\pi$ is rational or irrational.

---

## 1. Scope, dependencies, and fixed arithmetic

The original infinite domain is retained:


$$
K_u=N_u=9^{18+32u}=3^{36+64u},
\qquad u\in\mathbb Z_{\ge0}.
$$


Residue-class descriptions below classify this whole domain; they do not replace it by a new subsequence.

The previously checked compact $k=81$, modulus-$27$ receipt and signed prime-$17$ receipt are reused only at their established scopes. They are not rerun. Their finite arithmetic supports the proofs but does not replace the uniform arguments.

The already completed analytic estimates, content-transfer identities, and source-normalization results are also reused at their stated hypotheses. No fixed-base gcd theorem or almost-$S$-unit theorem is imported: the supplied applicability gates do not establish the required hypotheses for these factorial-height original objects.

### 1.1 Compact objects

Retain


$$
a_0=1,\qquad a_d=1-da_{d-1},
$$




$$
u_n=a_{2n},\quad f_n=(2n)!,\quad w_n=(-1)^n,\quad c_n=u_n-w_n,
$$


and


$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad r_n=-f_n+4\rho_n.
$$


The complete returns are


$$
\sigma_n=c_{n+1}+c_n=u_{n+1}+u_n,
$$




$$
\boxed{\tau_n=-(2n+2)!-(2n)!+\frac4{2n+1}.}
\tag{1.1}
$$



For


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),
$$


the original rectangles are


$$
Z_k=
\left[
(c_{m+j})_{\substack{0\le m<2k\\0\le j<k}}
\ \middle|\
(\Lambda_k\tau_{m+j})_{\substack{0\le m<2k\\0\le j<k-1}}
\right],
$$




$$
Y_k=
\left[
(\sigma_{m+j})_{\substack{0\le m<2k-1\\0\le j<k}}
\ \middle|\
(\Lambda_k\tau_{m+j})_{\substack{0\le m<2k-1\\0\le j<k}}
\right].
$$


Their actual maximal contents are


$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
\mathscr L_k=\delta_{2k-1}(Y_k).
$$



The physical boundary remains


$$
\boxed{\text{moment }3k-2,\quad (6k-4)!,\quad\text{last odd denominator }6k-5.}
\tag{1.2}
$$



For


$$
H_k(z)=H_{0,k}+H_{1,k}z
=\det[c_{m+j}\mid \Lambda_k(r_{m+j}+z(-1)^{m+j})],
$$


the final normalization is


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$




$$
q_k=\frac{|H_{1,k}|}{G_k},\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k}.
$$


Thus


$$
q_k(e+\pi)-p_k
=\frac{\operatorname{sgn}(H_{1,k})H_k(e+\pi)}{G_k}.
$$


On the supplied original nonvanishing and positivity domain,


$$
\boxed{
0<\ell_{K_u}
=q_{K_u}(e+\pi)-p_{K_u}
=\frac{|H_{K_u}(e+\pi)|}{G_{K_u}}.
}
\tag{1.3}
$$



The established all-prime relation remains


$$
\boxed{
\operatorname{lcm}(\mathscr R_k,\mathscr L_k)
\mid G_k\mid\Lambda_k\mathscr R_k\mathscr L_k.
}
\tag{1.4}
$$



### 1.2 Signed objects

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


with


$$
C_0=1,\quad C_1=2t-1,\quad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$


At the original $N=N_u$, retain


$$
\mathcal H=t(1-t)(1+t^2)^2,\qquad K=\mathcal H C_{N-3}^2,
\qquad U=-\eta(K),
$$


where


$$
\eta(H)=\int_{-\infty}^1e^{t-1}H(t)\,dt
=\sum_{r\ge0}[x^r]H(1-x)\,r!.
\tag{1.5}
$$


The last equality has **no additional alternating sign**.

The actual Gaussian division is


$$
g_B=\gcd(b_{N-1},b_N)>0,\qquad
\alpha=\frac{b_{N-1}}{g_B},\quad
\beta=\frac{b_N}{g_B},
$$




$$
F=\alpha C_N-\beta C_{N-1},\qquad
\delta=\frac{a_Nb_{N-1}-a_{N-1}b_N}{g_B}.
$$


Hence $F(i)=F(-i)=\delta$. Retain


$$
V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V),
$$


and the established exact content


$$
\boxed{h=g_B^2c.}
\tag{1.6}
$$


Then


$$
\tau=\frac Uc,\quad \nu=\frac Vc,\quad
W_{\rm prim}=\tau F^2+\nu K,\quad M=\tau\delta^2.
$$



For the complete endpoint functional


$$
E(H)=\sum_{r=0}^{\deg H}(-1)^rr![t^r]H,
$$


put


$$
E_F=E(F^2),\qquad E_K=E(K),
$$




$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


The actual least simultaneous clearer is


$$
D=\operatorname{lcm}(\operatorname{den}R_F,\operatorname{den}R_K),
$$


and


$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$



Independently, reduce


$$
\tau R_F+\nu R_K=\frac b\lambda,\qquad \gcd(b,\lambda)=1,\quad\lambda>0.
$$


With


$$
E=\tau E_F+\nu E_K,\qquad A=\lambda E-b,\qquad G=\gcd(M,A),
$$


the actual primitive pair is


$$
\boxed{q=\frac{\lambda M}{G},\qquad p=\frac AG.}
\tag{1.7}
$$


Because $\gcd(A,\lambda)=1$, this uses the full gcd of numerator and denominator.

The physical polynomial terminal is $2N$; the monic arc quotients have degree at most $2N-2$, and their integration denominators stop at $2N-1$.

---

# Part I. Audit of A2 turn 6

## 2. Finite differences and every original contact minor: PASS

Let $\Delta y_n=y_{n+1}-y_n$, and put


$$
S(d)=\sum_{r=0}^{d-1}v_2(r!).
$$



### 2.1 The sequence divisibility

Integration by parts gives the exact finite polynomial-moment identity


$$
a_d=\int_0^\infty e^{-t}(1-t)^d\,dt.
$$


Therefore


$$
\Delta^r u_n
=\int_0^\infty e^{-t}(t-1)^{2n}t^r(t-2)^r\,dt.
$$


Expanding


$$
t^r(t-2)^r
=\sum_{i=0}^r\binom ri(-2)^{r-i}t^{r+i},
$$


each resulting integral is an integer multiple of $(r+i)!$. Moreover,


$$
\frac{\binom ri\,2^{r-i}(r+i)!}{2^rr!}
=\binom{r+i}{2i}(2i-1)!!\in\mathbb Z.
$$


Consequently,


$$
\boxed{2^rr!\mid\Delta^r u_n.}
\tag{2.1}
$$


Since $\sigma_n=2u_n+\Delta u_n$,


$$
\boxed{2^{r+1}r!\mid\Delta^r\sigma_n.}
\tag{2.2}
$$



These are integral divisibilities, not assertions that factorials are local units.

### 2.2 Every contact-return minor

The finite double-Pascal identity is


$$
\sigma_{m+j}
=\sum_{r\le m}\sum_{s\le j}
\binom mr\binom js\,\Delta^{r+s}\sigma_0.
$$


Thus the finite block factors as


$$
2P_{\rm row}D_{\rm row}BD_{\rm col}P_{\rm col}^{T},
\qquad D_{rr}=2^rr!,
$$


with $B$ integral.

For any $d$-minor, Cauchy–Binet supplies $d$ distinct diagonal factors on each side. Because


$$
2^rr!\mid2^{r+1}(r+1)!,
$$


every such product contains at least the divisor from indices $0,\ldots,d-1$. Hence


$$
\boxed{
2^{d^2}\left(\prod_{r=0}^{d-1}r!\right)^2
\mid \text{every }d\text{-minor of }(\sigma_{m+j}).
}
\tag{2.3}
$$


Its binary valuation is


$$
C(d)=d^2+2S(d).
$$



### 2.3 The contact atom in $Z_k$

For $c_n=u_n-(-1)^n$,


$$
\Delta^{r+s}c_0=\Delta^{r+s}u_0-(-2)^{r+s}.
$$


After extracting $2^r$ and $2^s$, the transformed matrix is


$$
U_{rs}-(-1)^r(-1)^s,
\qquad
U_{rs}=\frac{\Delta^{r+s}u_0}{2^{r+s}}.
$$


Here $r!s!\mid U_{rs}$, by (2.1). The atom is rank one, so a $d$-minor expands into a $d$-minor of $U$ and terms containing $(d-1)$-minors of $U$. Therefore


$$
\boxed{
2^{d(d-1)}
\left(\prod_{r=0}^{d-2}r!\right)^2
\mid \text{every }d\text{-minor of }(c_{m+j}).
}
\tag{2.4}
$$


The shortening of the factorial product is necessary. Deleting the atom would give a different assertion.

---

## 3. The complete mixed return and balanced type counts: PASS

Write


$$
g_n=(2n+2)!+(2n)!,\qquad b_n=\frac4{2n+1},
$$


so that


$$
\boxed{\tau_n=-g_n+b_n.}
$$



All denominators of $b_n$, and $\Lambda_k$, are units in $\mathbb Z_{(2)}$. This localization is legitimate for a binary lower divisor of the original integer columns $\Lambda_k\tau_n$; it does not remove their odd-prime payments.

### 3.1 Factorial block

The entry factorization


$$
g_{m+j}
=(2m)!(2j)!\binom{2m+2j}{2m}
\bigl((2m+2j+2)(2m+2j+1)+1\bigr)
$$


shows that every $d$-minor has valuation at least


$$
F(d)=2\sum_{r=0}^{d-1}v_2((2r)!)
=d(d-1)+2S(d).
\tag{3.1}
$$



### 3.2 Full arctangent forcing

The Cauchy determinant formula gives


$$
\det\left(\frac4{2m_i+2j_h+1}\right)
=
\pm\frac{
4^d2^{d(d-1)}
\prod_{i<h}(m_h-m_i)\prod_{i<h}(j_h-j_i)}
{\prod_{i,h}(2m_i+2j_h+1)}.
$$


Each Vandermonde is divisible by $\prod_{r<d}r!$, as follows from the integer-valued binomial basis. Thus every $d$-minor of the forcing block has valuation at least


$$
F(d)+2d.
\tag{3.2}
$$



### 3.3 Mixing the two blocks

Choose $s$ factorial columns and $t=d-s$ forcing columns, then expand along the chosen factorial columns. Each term has valuation at least


$$
F(s)+F(t)+2t.
$$


Therefore


$$
E(d)=\min_{s+t=d}\{F(s)+F(t)+2t\}.
$$



The increment when $s$ increases by one is


$$
2v_2((2s)!)-2v_2((2t-2)!)-2.
$$


It is negative for $s<t$, and nonnegative after the balanced minimizing choice. The boundary cases $d=0,1$ agree with the same formulas. Hence


$$
\boxed{
E(d)=
2\left\lfloor\frac{d^2}{4}\right\rfloor
+2S\!\left(\left\lfloor\frac d2\right\rfloor\right)
+2S\!\left(\left\lceil\frac d2\right\rceil\right).
}
\tag{3.3}
$$



This calculation pays the complete forcing block. Treating $\tau$ as merely $-g$ would not prove (3.3).

---

## 4. Original maximal minors and non-descent for every $k\ge18$: PASS

A maximal minor of $Y_k$ has exactly one of two types:

* $k-1$ contact-return columns and $k$ complete right-return columns;
* $k$ contact-return columns and $k-1$ complete right-return columns.

Their respective lower valuations are


$$
C(k-1)+E(k),\qquad C(k)+E(k-1).
$$


The first is smaller. Indeed,


$$
C(k)-C(k-1)=2k-1+2v_2((k-1)!),
$$


whereas


$$
E(k)-E(k-1)=
\begin{cases}
2v_2((k-2)!)+2,&k\text{ even},\\
2v_2((k-1)!),&k\text{ odd}.
\end{cases}
$$


The difference is positive for all $k\ge2$.

Thus every original $Y_k$ maximal minor is divisible by $2^{\nu_k^Y}$, where


$$
\nu_k^Y=C(k-1)+E(k).
\tag{4.1}
$$


Every $Z_k$ maximal minor contains all $k$ contact columns and all $k-1$ returns, so


$$
\nu_k^Z=k(k-1)+2S(k-1)+E(k-1)
\tag{4.2}
$$


is likewise a valid lower valuation.

To evaluate (4.1), let


$$
T(d)=\sum_{r=0}^{d-1}s_2(r).
$$


Legendre’s formula and the even–odd digit decomposition give


$$
S(d)=\frac{d(d-1)}2-T(d),
$$




$$
T(k)=T(\lfloor k/2\rfloor)+T(\lceil k/2\rceil)+\lfloor k/2\rfloor.
$$


Substitution yields


$$
\boxed{
\nu_k^Y
=k^2-3k+3-\epsilon_k+4S(k)+2s_2(k-1),
}
\tag{4.3}
$$


where $\epsilon_k$ is the parity of $k$.

Since $\Lambda_k$ is odd,


$$
v_2(\mathcal W_k)=15k+4S(k).
$$


Therefore


$$
\boxed{
\nu_k^Y-v_2(\mathcal W_k)
=k^2-18k+3-\epsilon_k+2s_2(k-1)>0
\quad(k\ge18).
}
\tag{4.4}
$$


Every integer combination of the original maximal minors is divisible by $2^{\nu_k^Y}$, while $\mathcal W_k$ is not. Hence


$$
\boxed{\mathcal W_k\notin I_{2k-1}(Y_k)\quad(k\ge18).}
\tag{4.5}
$$



No rank hypothesis is needed: if every maximal minor vanished, the ideal would be zero and the conclusion would still hold.

All finite differences used above remain inside (1.2). In particular, the largest difference in the $Y$-contact argument requires $u_{3k-2}$, and no larger moment.

### What this disproves—and what it does not

The proposed integral descent is false. Integer Bézout coefficients with right side $\mathcal W_k$ do not exist.

This does not disprove good-prime normality. It also does not decide the odd-localized assertion. If


$$
\operatorname{odd}(\mathscr L_k)\mid\mathcal W_k^{\rm odd},
$$


then the least binary exponent in an identity


$$
\sum_j\beta_jM_{k,j}=2^a\mathcal W_k^{\rm odd}
$$


is exactly


$$
\boxed{a=v_2(\mathscr L_k),}
$$


not merely its lower bound $\nu_k^Y$.

---

## 5. The evaluated upper divisor-size bound: PASS at $H_{1,k}\ne0$

The cancellation identity is complete. From


$$
u_n=\frac1e\left((2n)!+\int_0^1e^t t^{2n}\,dt\right),
$$


one obtains


$$
d_n:=e\sigma_n+\tau_n
=\int_0^1e^t(1+t^2)t^{2n}\,dt+\frac4{2n+1},
$$


so


$$
0<d_n<\frac{10}{2n+1}\le10.
\tag{5.1}
$$


Also,


$$
|c_n|\le4(2n)!,\qquad |\sigma_n|\le4(2n+2)!.
\tag{5.2}
$$



The rank hypotheses used in the source are valid in the original objects:

* Adjacent sums of the right columns of $H_k(z)$ remove the $z(-1)^{m+j}$ part, leaving the original $Z_k$ and one bordered column. Thus $H_{1,k}\ne0$ implies $\operatorname{rank}Z_k=2k-1$.
* The unit triangular row transformation retaining row $0$ and replacing later rows by adjacent row sums leaves $Y_k$ below the first row. If $Y_k$ lacked full row rank, every coefficient of the resulting affine determinant would vanish. Thus $H_{1,k}\ne0$ implies $\operatorname{rank}Y_k=2k-1$.

The $k$ contact-return columns of $Y_k$ are independent because their leading Hankel Gram matrix is positive definite:


$$
\int_0^\infty e^{-t}\bigl((t-1)^2+1\bigr)
P((t-1)^2)^2\,dt>0
$$


for nonzero $P$ of degree below $k$. They can therefore be extended to a nonzero maximal minor using $k-1$ return columns.

In that minor, adding $e\Lambda_k$ times the matching contact column replaces each return by $\Lambda_k d$. In $Z_k$, the corresponding operation uses the two already present contact columns $c_j,c_{j+1}$. These real operations preserve the numerical determinant; they are not asserted to preserve integer content.

Log-convexity of factorials bounds each determinant term by the product with the largest rows paired in order with the shifts. In both cases this is


$$
\prod_{i=0}^{k-1}(2k+4i)!.
$$


Therefore


$$
\boxed{
1\le\mathscr R_k,\mathscr L_k\le
\mathcal U_k:=
(2k-1)!\,4^k10^{k-1}\Lambda_k^{k-1}
\prod_{i=0}^{k-1}(2k+4i)!.
}
\tag{5.3}
$$


The final factorial is exactly $(6k-4)!$.

This proves a size bound, not a divisibility $\mathscr L_k\mid\mathcal U_k$. Its leading size,


$$
\log\mathcal U_k=4k^2\log k+O(k^2),
$$


is too large for the decisive content target.

The previously completed $k=4,p=23$ values $16,17$ remain finite normality evidence only. They are not needed for any uniform proof above.

---

# Part II. Audit of A2 turn 7

## 6. The capped $3$-primary theorem: PASS at the stated depth

Let


$$
k=3^s,\quad s\ge4,\quad Q=3^h,\quad
1\le h,\quad 2h\le s+2.
$$


Write


$$
T_n=\Lambda_k\tau_n,\qquad n_0=\frac{3k-1}{2}.
$$



### 6.1 Periodicity and the complete integer quotients

The recurrence proves, by induction,


$$
a_{d+Q}\equiv a_d\pmod Q.
$$


Hence $u_n$ and $\sigma_n$ are $Q$-periodic modulo $Q$. The atom $(-1)^n$ is not $Q$-periodic, because $Q$ is odd.

Since


$$
3k\le6k-5<9k,
$$




$$
v_3(\Lambda_k)=s+1.
$$


The exact integer entry is


$$
T_n=-\Lambda_k\bigl((2n+2)!+(2n)!\bigr)
+\frac{4\Lambda_k}{2n+1}.
$$


At the present depth $h\le s+1$, its factorial part vanishes modulo $Q$, so


$$
T_n\equiv\frac{4\Lambda_k}{2n+1}\pmod Q.
\tag{6.1}
$$


The quotient on the right is an integer before reduction.

Modulo $3$, the only nonzero entry in the physical return range occurs at $2n+1=3k$. Therefore


$$
T_n\equiv\gamma\,\mathbf1_{n=n_0}\pmod3,
\qquad
\gamma=\frac{4\Lambda_k}{3k}\in\mathbb Z_{(3)}^\times.
\tag{6.2}
$$



### 6.2 Actual unit return rows

Let $r=k$ for $Y_k$, and $r=k-1$ for $Z_k$. Select


$$
m_i=n_0-i,\qquad 0\le i<r.
$$


These are actual physical rows. Their return block


$$
M_{ij}=T_{n_0-i+j}
$$


satisfies


$$
M\equiv\gamma I_r\pmod3.
\tag{6.3}
$$


It is therefore invertible over $\mathbb Z_{(3)}$ and modulo $Q$.

Put


$$
D_0=3^{s+2-h}.
$$


The depth condition gives $Q\mid D_0$. From (6.1),


$$
T_n\not\equiv0\pmod Q\Longrightarrow D_0\mid2n+1.
$$


For the pivot block this implies


$$
M_{ij}\ne0\pmod Q\Longrightarrow D_0\mid j-i.
$$


Thus $M$, and its inverse modulo $Q$, preserve residue classes modulo $Q$.

For a free row $m$,


$$
T_{m+j}\ne0\pmod Q\Longrightarrow m+j\equiv n_0\pmod Q.
\tag{6.4}
$$



### 6.3 The row-unit Schur reduction

For a contact block $C$, eliminate the return pivots:


$$
S=C_F-T_FM^{-1}C_P.
$$


When $C_{m,c}=\sigma_{m+c}$, residue preservation and contact periodicity imply


$$
(M^{-1}C_P)_{j,c}=d_j\sigma_{n_0-j+c}\pmod Q
$$


for some scalar $d_j$. Equation (6.4) then gives


$$
\boxed{S_{m,c}=\eta_m\sigma_{m+c}\pmod Q.}
\tag{6.5}
$$


All free-row return entries vanish modulo $3$, so


$$
\eta_m\equiv1\pmod3.
$$


Every $\eta_m$ is a unit. This proves the claimed row-unit reduction, not just a rank statement.

### 6.4 Completion for $Y_k$

The free rows number $k-1$, and their first interval contains


$$
0,\ldots,\frac{k-1}{2}.
$$


The depth bound implies $h\le s-1$, hence $Q\le k/3$. Both free rows and contact shifts contain representatives $0,\ldots,Q-1$.

After dividing by $\eta_m$, repetitions can be eliminated by unit row and column operations, leaving


$$
\Sigma_Q=(\sigma_{a+b})_{0\le a,b<Q},
$$


together with $k$ return units and the required zero padding.

### 6.5 Completion for $Z_k$: the atom is essential

Make the integral unit triangular contact transformation


$$
(c_0,c_1,\ldots,c_{k-1})
\longmapsto(c_0,\sigma_0,\ldots,\sigma_{k-2}).
$$


After eliminating the $k-1$ return pivots and dividing free rows by their units, the remaining columns have the form


$$
u_m-b_m,\qquad \sigma_m,\ldots,\sigma_{m+k-2},
$$


where


$$
b_m\equiv(-1)^m\pmod3.
$$



Since $Q$ is odd,


$$
\frac12\sum_{j=0}^{Q-1}(-1)^j\sigma_{m+j}
=\frac{u_m+u_{m+Q}}2
\equiv u_m\pmod Q.
$$


The required columns are present. Subtracting this combination from the first column leaves $-b_m$.

The free rows include $0$ and $Q$. Their $\sigma$-rows agree modulo $Q$, but


$$
b_Q-b_0\equiv-2\not\equiv0\pmod3.
$$


Their row difference therefore supplies one additional unit pivot in the atom column. Eliminating it does not alter the remaining $\sigma$-block. The same $\Sigma_Q$ remains.

Thus both rectangles have $k$ unit pivots before the cyclic contact block is evaluated.

### 6.6 Cyclic Gram factorization, with all factorial divisions paid

Let


$$
U_Q=(u_{a+b})_{0\le a,b<Q}.
$$


Cyclic row shift $P$ gives


$$
\Sigma_Q=(I+P)U_Q\pmod Q.
$$


Because $Q$ is odd,


$$
(I+P)^{-1}=\frac12\sum_{j=0}^{Q-1}(-P)^j.
$$


Multiplication of residue indices by $2$ then makes $U_Q$ permutation equivalent to


$$
A_Q=(a_{r+t})_{0\le r,t<Q}.
$$



The exact finite identity


$$
a_d=\sum_{j=0}^d(-1)^j\binom djj!
$$


gives $\Delta^ja_0=(-1)^jj!$. Double-Pascal transformation and row/column signs reduce $A_Q$ to


$$
F_Q=((r+t)!)_{0\le r,t<Q}.
$$


Now


$$
F_Q=L_0\operatorname{diag}((j!)^2)L_0^T,
\qquad
(L_0)_{rj}=\binom rj\frac{r!}{j!}\quad(j\le r).
\tag{6.6}
$$


The matrix $L_0$ is integer unit lower triangular. The entry identity is


$$
r!t!\sum_j\binom rj\binom tj=(r+t)!.
$$


No factorial has been inverted as a unit.

Consequently,


$$
\Sigma_Q\sim\operatorname{diag}((j!)^2)_{0\le j<Q}\pmod{3^h}.
$$


For $j\ge Q$, $2v_3(j!)\ge h$, so the padding can be represented by the remaining capped factorial entries. This proves


$$
\boxed{
\{\min(e_{A,i},h)\}_{i=1}^{2k-1}
=
\{0^{[k]}\}\cup
\{\min(2v_3(j!),h):0\le j\le k-2\},
}
\tag{6.7}
$$


for $A=Y_k,Z_k$.

All contact values used here are within the original terminal. Local unit inverses are valid for this $3$-primary analysis; they are not automatically allowable over $\mathbb Z[1/2]$.

---

## 7. Consequences and the exact depth obstruction

At every original index, $h=19$ is allowed. For $j=0,\ldots,23$, the values $2v_3(j!)$ occur in triples:


$$
0,\ 2,\ 4,\ 8,\ 10,\ 12,\ 16,\ 18.
$$


Thus the source table is correct:


$$
\operatorname{rank}_{\mathbb F_3}Y_k
=\operatorname{rank}_{\mathbb F_3}Z_k=k+3,
$$


and


$$
\boxed{
v_3(\delta_{k+24}(Y_k))
=v_3(\delta_{k+24}(Z_k))=210.
}
\tag{7.1}
$$


The capped total is


$$
210+19(k-25)=19k-265.
$$



The parent $k=81$, modulus-$27$ receipt has the predicted finite profile


$$
1^{[84]},\quad9^{[3]},\quad0^{[74]},
$$


with capped total $228$. It remains a finite receipt; the uniform conclusion is supplied by the proof above.

The exact $3$-allowance in the odd certificate is also correct:


$$
v_3(\mathcal W_k^{\rm odd})
=k^2+(2-s)k.
$$


Indeed,


$$
\sum_{j=0}^{k-1}v_3(j!)=\frac{k(k-1-2s)}4.
$$



The obstruction to continuing the capped proof is precise:

* beyond $h\le s+1$, the full factorial term in $T_n$ cannot simply be removed;
* beyond $2h\le s+2$, return support need not preserve contact residue classes modulo $3^h$, so (6.5) is unjustified.

The resulting cross-residue terms are real terms of the original Schur complement. A capped front end is not an upper bound for a maximal content.

The assigned two-cofactor high-depth problem is therefore still open. This report does not rename that obligation as a result.

---

## 8. Finite-jet payments and the next constant: PASS

The transformations


$$
(T_\star y)_m
=\sum_{r=0}^{m}(-1)^r\binom{b_\star}{r}
(2m-2r+1)_{h_\star+2r}\,y_{m-r}
$$


have


$$
(h_Z,b_Z)=(2k-3,2k-1),\qquad
(h_Y,b_Y)=(2k-1,2k+1).
$$


They factor as $T_\star=D_\star S_\star$, where $S_\star$ is integer unit lower triangular and


$$
(D_Z)_{mm}=(2m+1)_{2k-3},\qquad
(D_Y)_{mm}=(2m+1)_{2k-1}.
$$


The identity follows from


$$
(D_\star)_{mm}\frac{(2m)!}{(2m-2r)!}
=(2m-2r+1)_{h_\star+2r}.
$$



The denominator $2(m-r+j)+1$ of every return term lies among the factors of this rising factorial. Thus the complete forcing is integrally absorbed term by term. No physical input beyond (1.2) is introduced.

Retain the actual jet contents $\mathscr C_{Z,k},\mathscr C_{Y,k}$, the products


$$
t_Z=\prod_{m=0}^{2k-1}(2m+1)_{2k-3},\qquad
t_Y=\prod_{m=0}^{2k-2}(2m+1)_{2k-1},
$$


and the actual corrections


$$
\zeta_{Z,k}
=\operatorname{lcm}_m
\frac{(2m+1)_{2k-3}}
{\gcd((2m+1)_{2k-3},|v_m|)},
$$




$$
\chi_{Y,k}
=\frac{\gcd(\Lambda_ka_Y,b_Y)}{\gcd(a_Y,b_Y)}.
$$


Here $a_Y$ is the gcd of jet minors omitting a contact-return column and $b_Y$ the gcd of those omitting a right-return column.

The exact identities are


$$
\boxed{
\mathscr R_k=
\frac{\Lambda_k^{k-1}\mathscr C_{Z,k}\zeta_{Z,k}}{t_Z},
\qquad
\mathscr L_k=
\frac{\Lambda_k^{k-1}\mathscr C_{Y,k}\chi_{Y,k}}{t_Y}.
}
\tag{8.1}
$$


For $Y$, these follow directly from the two distinct column-scaling counts. For $Z$, scaling row $m$ multiplies its cofactor by $t_Z/(D_Z)_{mm}$; the primitive cofactor vector produces exactly the displayed least clearer $\zeta_{Z,k}$.

Neither correction is $1$ by default.

### 8.1 Evaluation of the row payments

For


$$
T_0(k)=\prod_{m=0}^{2k-1}\prod_{r=1}^{2k}(2m+r),
$$


a Riemann sum gives


$$
\log T_0(k)
=4k^2\log k+
k^2\int_0^2\int_0^2\log(2x+y)\,dy\,dx
+O(k\log k).
$$


With


$$
F(z)=\frac{z^2}{2}\log z-\frac{3z^2}{4},
$$


the integral equals


$$
\frac12\{F(6)-F(4)-F(2)+F(0)\}=9\log3-6.
$$


Deleting the boundary strips distinguishing $t_Z,t_Y$ changes the logarithm by only $O(k\log k)$. Hence each has expansion


$$
4k^2\log k+(9\log3-6)k^2+O(k\log k).
$$



Every diagonal factor divides $(6k-5)!$, so


$$
\log\zeta_{Z,k}=O(k\log k).
$$


Also $\chi_{Y,k}\mid\Lambda_k$, and therefore $\log\chi_{Y,k}=O(k)$.

Finally, $\Lambda_k$ is the odd part of $\operatorname{lcm}(1,\ldots,6k-5)$. The standard prime number theorem for the Chebyshev function gives


$$
\log\Lambda_k=6k+o(k).
$$



Taking logarithms in (8.1), **before** suppressing the corrections, gives


$$
\begin{aligned}
\log\mathscr R_k+\log\mathscr L_k
={}&\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
-8k^2\log k\\
&+2(k-1)\log\Lambda_k
-(18\log3-12)k^2\\
&+\log\zeta_{Z,k}+\log\chi_{Y,k}+O(k\log k).
\end{aligned}
$$


Thus


$$
\boxed{
\log\mathscr R_k+\log\mathscr L_k
=
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
-8k^2\log k+(24-18\log3)k^2+o(k^2).
}
\tag{8.2}
$$



The odd-certificate height


$$
\log\mathcal W_k^{\rm odd}
=2k^2\log k+(3-2\log2)k^2+o(k^2)
$$


also follows correctly from factorial summation and the removal of the binary factorial part.

The individual original right-column clearers


$$
\Lambda_{k,j}=\operatorname{lcm}(1,3,\ldots,4k+2j-3)
$$


remain unchanged. The actual least coefficient clearer of $H_k/\Lambda_k^k$ remains


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}),
}
$$


and the remaining coefficient content is $G_k/d_{H,k}$.

---

# Part III. Audit of A5 turns 8 and 9

## 9. Integral endpoint and complete coefficient planes: PASS

For every polynomial $H$,


$$
E(H')=H(0)-E(H).
$$


Since


$$
C_j'=2j\,U_{j-1}(2t-1),
$$


the polynomial division by $2j$ is already paid. Defining


$$
\Phi_j=E(U_{j-1}(2t-1)),\qquad \Phi_0=0,
$$


gives


$$
\boxed{E(C_j)=(-1)^j-2j\Phi_j.}
\tag{9.1}
$$



A useful exact coefficient identity is


$$
U_{j-1}(2t-1)
=(-1)^{j-1}\sum_{r=0}^{j-1}(-4)^r
\binom{j+r}{2r+1}t^r.
$$


Therefore


$$
\Theta_j=T_j(-4),\qquad
\Phi_j=(-1)^{j-1}T_j(4),
$$


where


$$
T_j(c)=\sum_{r=0}^{j-1}c^rr!\binom{j+r}{2r+1}.
\tag{9.2}
$$


This identity is tied to $T_0=0,T_1=1$.

For completeness, the coefficient recurrence follows from


$$
r!\left[
\binom{j+r+1}{2r+1}-\binom{j+r-1}{2r+1}
\right]
=j(r-1)!\binom{j+r-1}{2r-1}
\quad(r\ge1).
$$


The constant coefficient gives the forcing $2$. Thus


$$
T_{j+1}(c)=cjT_j(c)+T_{j-1}(c)+2,
$$


and consequently


$$
\boxed{
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j.
}
\tag{9.3}
$$


In particular $\Phi_1=1,\Phi_2=-6$. No singular normalized recurrence is inverted.

### 9.1 The thirteen weights and both forcings

Let $n=2N$. The weights are


$$
(1,8,58,168,399,-176,-916,-176,399,168,58,8,1).
$$


They can be checked from the degree-six identity


$$
2048\mathcal H
=458+176C_1-399C_2-168C_3-58C_4-8C_5-C_6.
$$


Together with $C_{N-3}^2=(1+C_{n-6})/2$, this gives


$$
8192K=4096\mathcal H-\sum_{k=0}^{12}w_kC_{n-k}.
\tag{9.4}
$$


All indices $n-k$ remain physical and positive on the original domain.

The complete constants are


$$
\eta(\mathcal H)=-332,\qquad E(\mathcal H)=-903.
$$


Using


$$
\sum w_k=\sum(-1)^kw_k=0
$$


in (9.4) gives exactly


$$
4096U=\mathsf C_U-\mathsf A\Theta_n-\mathsf B\Theta_{n-1},
$$




$$
4096E_K=\mathsf A\Phi_n+\mathsf B\Phi_{n-1}+\mathsf C_E.
$$


The backward recurrences for $\kappa_k,\omega_k$ must, and do, include respectively


$$
-2,\qquad -2(-1)^k.
$$



The square formulas also have the correct distinct constants. The product identity for $F^2$ includes $C_1$, whose endpoint is $-3$. It yields


$$
V=\mathsf C_V-\mathsf P\Theta_n-\mathsf Q\Theta_{n-1},
$$




$$
E_F=\mathsf C_F^E-\mathsf P\Phi_n-\mathsf Q\Phi_{n-1},
$$


where


$$
\mathsf C_V=\alpha^2+(2n-3)\beta^2-\delta^2,
$$




$$
\boxed{\mathsf C_F^E=\alpha^2+(5-2n)\beta^2+4\alpha\beta.}
$$


Neither $-\delta^2$ nor $4\alpha\beta$ may be omitted.

---

## 10. Both complete arc denominators and the final payment: PASS

Because $F(\pm i)=\delta$,


$$
\frac{F^2-\delta^2}{1+t^2}\in\mathbb Z[t].
$$


This follows from monic division: its integer remainder vanishes at both $i$ and $-i$. Also


$$
\frac K{1+t^2}=t(1-t)(1+t^2)C_{N-3}^2\in\mathbb Z[t].
$$


Both degrees are at most $2N-2$. Therefore, after complete reduction,


$$
\operatorname{den}(R_F),\operatorname{den}(R_K)
\mid L_{\rm aff}:=\operatorname{lcm}(1,\ldots,2N-1),
$$


and


$$
D\mid L_{\rm aff}.
\tag{10.1}
$$



This is a valid denominator bound for **both** complete arcs. The reports do not supply a closed formula for the actual reduced $R_F$ denominator or for $D$; their definitions must remain actual gcd/lcm definitions.

The complete return for the square arc is also correct. Polynomial division gives


$$
R_{j+1}=(4t-2)R_j-R_{j-1}+4b_j,
$$


which produces


$$
\xi_{j+1}=4\upsilon_j-2\xi_j-\xi_{j-1}+16b_j,
$$




$$
\upsilon_{j+1}
=-4\xi_j-2\upsilon_j-\upsilon_{j-1}+16(\ell_j-a_j).
$$


The piecewise definition


$$
\ell_j=0\quad(j\text{ odd}),\qquad
\ell_j=(1-j^2)^{-1}\quad(j\text{ even})
$$


avoids the spurious substitution at $j=1$. The exact complete square arc is


$$
R_F=\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}-2\alpha\beta\xi_{n-1}}2.
$$



### 10.1 Complete $K$-arc and its fixed cancellation cap

Writing $m=N-3$, $j_r=(1-4r^2)^{-1}$, the even part of
$t(1-t)(1+t^2)$ gives


$$
R_K=\frac{13}{30}
+\frac{42j_m-20(j_{m+1}+j_{m-1})-(j_{m+2}+j_{m-2})}{128}.
$$


For $x=4m^2$, combination yields


$$
\boxed{
R_K=\frac{A_K(x)}{30L(x)},
}
$$




$$
A_K(x)=13x^3-455x^2+3502x-5850.
\tag{10.2}
$$


The two polynomial identities


$$
A_K=13L+45(3x-65),
$$




$$
27L=(3x-65)(9x^2-120x-269)-23560
$$


show that


$$
\boxed{
\gcd(A_K(x),30L(x))\mid
1350\cdot23560
=2^4\,3^3\,5^3\,19\,31.
}
\tag{10.3}
$$


Indeed, a common divisor divides both $1350(3x-65)$ and $30L$, so the second identity gives the displayed constant. This is an all-prime argument.

Let


$$
g_{\rm arc}=\gcd(A_K,30L),\qquad
a_K=A_K/g_{\rm arc},\qquad d_K=30L/g_{\rm arc}.
$$


Then $\gcd(a_K,d_K)=1$.

### 10.2 Simultaneous versus aggregate clearing

The aggregate clearer is not generally $D$. If


$$
B_D=\tau DR_F+\nu DR_K\in\mathbb Z,
$$


then exactly


$$
\lambda=\frac D{\gcd(D,B_D)}.
$$


The reconciliation is


$$
\tau X+\nu Y=\frac D\lambda A,
$$




$$
\boxed{
\gcd(D\tau\delta^2,\tau X+\nu Y)=\frac D\lambda G.
}
\tag{10.4}
$$


The raw-interface identity remains


$$
\gcd(A_{\rm raw},B_{\rm raw})
=\frac{L_{\rm aff}h}{\lambda}G.
$$



These identities retain all paid Gaussian divisions, actual content, both least clearers, and the final all-prime gcd.

### 10.3 Intrinsic joint divisor and the actual $q$

Set


$$
y_K=d_KE_K-a_K,\qquad \mu=D/d_K.
$$


Then $Y=\mu y_K$, and


$$
\mathfrak J^0=\gcd(U,Vy_K),\qquad
\mathfrak J=\gcd(U,VY)
$$


satisfy


$$
\boxed{\mathfrak J^0\mid\mathfrak J\mid\mu\mathfrak J^0.}
\tag{10.5}
$$



Moreover,


$$
\mathfrak J=c\gcd(U/c,Y).
$$


At a prime with $t=v_p(\tau)>v_p(Y)$, $\nu$ is a unit and


$$
v_p(\tau X+\nu Y)=v_p(Y).
$$


Reduction of the fraction with denominator $D\tau\delta^2$ therefore leaves at least $t-v_p(Y)$ powers of $p$ in the actual denominator. This proves, at every prime,


$$
\boxed{\frac U{\mathfrak J}\mid q=\frac{\lambda M}{G}.}
\tag{10.6}
$$



For $p\mid d_K$, the reduced column satisfies $p\nmid y_K$, and hence


$$
v_p(\mathfrak J)
=v_p(c)+\min\{v_p(U/c),v_p(\mu)\}.
\tag{10.7}
$$



The integral source and endpoint transfer equations also pass. Direct expansion of their terminal determinant gives


$$
z_nw_{n-1}-z_{n-1}w_n
=-4096\Delta(UX+VY).
$$


This is an exact identity, but its right side is the complete output already under investigation. It is not a smaller-height gcd certificate.

---

## 11. Dual boundary slopes: PASS at every odd prime

For the exact original-boundary sequence (9.2), terms with $r\ge p$ vanish modulo $p$. Vandermonde, or coefficient extraction from $(1+z)^{a+p\ell+r}$, gives


$$
T_{a+p\ell}(c)\equiv T_a(c)+\ell H_a(c)\pmod p,
$$


where


$$
H_a(c)=
\sum_{r=(p-1)/2}^{p-1}
c^rr!\binom{a+r}{2r+1-p}.
\tag{11.1}
$$


All lower factorials in these binomial-polynomial coefficients are $p$-units.

With $h=(p-1)/2$, pairing the factors gives


$$
H_a(c)=
\sum_{s=0}^{h}
\frac{c^{h+s}(h+s)!}{(2s)!}
\prod_{j=1}^{s}\left(a^2-\left(j-\frac12\right)^2\right)
\quad\text{in }\mathbb F_p[a].
$$


For $c\not\equiv0\pmod p$, its highest coefficient is $c^{p-1}=1$, so it is even and monic of degree $p-1$.

### 11.1 Evaluation of the Wronskian

Put


$$
Q_j(c)=T_{j+1}(c)T_j(-c)+T_{j+1}(-c)T_j(c).
$$


The opposite $cj$ terms cancel, while both forcing terms remain:


$$
Q_j(c)-Q_{j-1}(c)=2(T_j(c)+T_j(-c)).
$$


Since


$$
H_0(c)=T_p(c),\qquad
H_1(c)\equiv T_{p-1}(c)+1\pmod p,
$$


the initial dual Wronskian equals


$$
2\sum_{j=1}^{p-1}(T_j(c)+T_j(-c))+T_p(c)+T_p(-c).
\tag{11.2}
$$



This sum is evaluable. Hockey-stick summation gives


$$
\sum_{j=1}^{p-1}T_j(c)
=\sum_{r=0}^{p-2}c^rr!\binom{p+r}{2r+2}.
$$


For $(p-1)/2\le r\le p-2$, write $k=2r+1-p$. Lucas reduction produces


$$
2\binom r{k+1}+\binom rk
=\binom rk\frac p{k+1}\equiv0\pmod p.
$$


For smaller $r$, the relevant coefficients vanish. Only $r=p-1$ from $T_p(c)+T_p(-c)$ survives. Wilson’s theorem gives


$$
-2c^{p-1}.
$$


For $c=4$, this is $-2$.

The homogeneous slope recurrences make


$$
H_a^-H_{a-1}^++H_{a-1}^-H_a^+
$$


independent of $a$. Thus


$$
\boxed{
H_a^-H_{a-1}^++H_{a-1}^-H_a^+\equiv-2\pmod p
}
\tag{11.3}
$$


for every odd prime.

The source boundary $(0,1)$ and forcing $2$ are essential to this evaluation. It is not a theorem for arbitrary boundary states.

---

## 12. Every-depth congruence: PASS for $p\ge5$, with the tail paid

Let $p\ge5$, $k\ge1$, and $j,t\ge0$. Extend the finite sum (9.2) to a common finite upper limit for $j$ and $j+p^kt$, using zero binomial coefficients beyond the original limit. Vandermonde gives differences involving


$$
\binom{p^kt}{s}.
$$


For $t>0$,


$$
v_p\binom{p^kt}{s}\ge k-v_p(s).
\tag{12.1}
$$


The case $t=0$ is immediate.

For $r\ge p$,


$$
v_p(r!)\ge\lfloor\log_p(2r+1)\rfloor.
\tag{12.2}
$$


To verify this, take $ap\le r<(a+1)p$. Then $v_p(r!)\ge a$, while


$$
p^{a+1}>2r+1
$$


follows from $p^a\ge2(a+1)$, valid for $p\ge5,a\ge1$. Since $s\le2r+1$, (12.1)–(12.2) make every such **difference contribution** divisible by $p^k$.

This does not claim that all individual terms with $r\ge p$ vanish modulo $p^k$.

For $r<p$, only $s=p$ can survive, and


$$
\binom{p^kt}{p}
=p^{k-1}t\binom{p^kt-1}{p-1}
\equiv p^{k-1}t\pmod{p^k}.
$$


The remaining coefficient is exactly (11.1). Hence


$$
\boxed{
T_{j+p^kt}(c)-T_j(c)
\equiv p^{k-1}tH_{j\bmod p}(c)\pmod{p^k}.
}
\tag{12.3}
$$



For two actual even terminals differing by $p^kt$, the fixed integer $K$-coefficient rows agree modulo $p^k$; therefore the stated lift congruences for $U$, $E_K$, and the fully paid numerator


$$
\widehat y_K=30L(x)E_K-A_K(x)
$$


follow.

There is no corresponding permission to freeze $\alpha,\beta,\delta$ in $V$. Their actual Gaussian changes must be separately established.

### 12.1 What the unit slopes imply

The slope map


$$
\binom{u_1}{e_1}
=
\begin{pmatrix}
-H_a^-&-H_{a-1}^-\\
-H_a^+&H_{a-1}^+
\end{pmatrix}
\binom{\mathsf A}{\mathsf B}
$$


has determinant $2$. Thus


$$
u_1=e_1=0\iff \mathsf A=\mathsf B=0\pmod p.
$$


Direct expansion also gives


$$
u_1f_1+e_1v_1=-2\Delta\pmod p.
$$



These are rank assertions. They do not imply affine coprimality. The prime-$5$ exception below proves that the stronger promotion would be false in the original objects.

---

## 13. Original prime-$5$ theorem: independent arithmetic audit

### 13.1 Gaussian units and original index residues: PASS

Every original $N$ satisfies $N\equiv9\pmod{12}$. The Gaussian recurrences at $i=2,-2$ modulo $5$ have the displayed periods $6,4$, giving


$$
(a_N,b_N,a_{N-1},b_{N-1})\equiv(2,1,4,4)\pmod5.
$$


Thus


$$
5\nmid g_B,\qquad
g_B\alpha\equiv4,\quad g_B\beta\equiv1,\quad g_B\delta\equiv4.
\tag{13.1}
$$


Only after establishing this unit condition may the raw Gaussian residues be divided by $g_B$.

Since $N_u=81^{9+16u}$,


$$
N_u\equiv21+5u\pmod{25}.
$$


Writing $n=2+5\ell$,


$$
\ell\equiv3+2u\pmod5.
\tag{13.2}
$$



### 13.2 Complete local rows: PASS

The forced boundary values modulo $5$ are


$$
(T_j^-)_{j=0}^6=(0,1,3,4,2,4,4),
$$




$$
(T_j^+)_{j=0}^6=(0,1,1,1,0,3,2).
$$


The homogeneous slope recurrence then gives


$$
(H_2^-,H_1^-,H_2^+,H_1^+)=(2,3,2,1).
$$



For an explicit independent check of the fixed local evaluation at $n=2\pmod5$, the four recurrence arrays through $12$ are


$$
\begin{aligned}
r={}&(1,0,1,0,1,2,2,0,2,2,1,0,1),\\
s={}&(0,1,4,1,0,1,3,3,3,1,0,1,4),\\
\kappa={}&(0,0,3,3,4,4,4,3,2,3,1,4,0),\\
\omega={}&(0,0,2,3,2,0,4,4,1,3,4,3,3).
\end{aligned}
$$


Their inner products with


$$
(w_k(n-k))_{k=0}^{12}
=(2,3,0,2,2,3,4,0,1,4,1,3,0)
$$


are $4,0,4,2$. Therefore


$$
(\mathsf A,\mathsf B,\mathsf C_U,\mathsf C_E)
=(4,0,2,3)\pmod5.
$$



Substitution gives


$$
\boxed{
U_{N_u}\equiv1-u,\qquad E_{K,N_u}\equiv4u\pmod5.
}
\tag{13.3}
$$


The paid Gaussian data yield


$$
g_B^2\mathsf P=g_B^2\mathsf Q=2,\qquad
g_B^2\mathsf C_V=1,
$$


and hence


$$
\boxed{g_B^2V\equiv3\pmod5,\qquad5\nmid V.}
\tag{13.4}
$$



### 13.3 The complete arc at $5$: PASS

From (13.2),


$$
x=4(N-3)^2\equiv21+20u\pmod{25}.
$$


Only $x-1$ among the factors of $L$ is divisible by $5$. Put


$$
s_5=v_5(L)=v_5(n-7)\ge1.
$$


The identity


$$
A_K=13L+45(3x-65)
$$


shows:

* if $u\equiv4\pmod5$, then $s_5\ge2$ and $v_5(A_K)=1$;
* otherwise $s_5=1$, and
  

$$
A_K/5\equiv1+4u\pmod5.
$$



Thus


$$
v_5(d_K)=
\begin{cases}
0,&u\equiv1\pmod5,\\
v_5(n-7),&u\not\equiv1\pmod5.
\end{cases}
\tag{13.5}
$$



On $u=1+5t$,


$$
N=81^{25+80t}\equiv1+25t\pmod{125}.
$$


Here the quadratic binomial term is divisible by $125$, because its exponent is divisible by $5$. Consequently,


$$
x\equiv16-25t\pmod{125}.
$$


Using


$$
L(16)=-945,\quad A_K(16)=-13050,\quad A_K'(16)=-1074,
$$


one gets


$$
\frac{30L(x)}{25}\equiv1,\qquad
\frac{A_K(x)}{25}\equiv3+4t\pmod5.
$$


The division by $25$ is paid by working first modulo $125$. After actual reduction, $d_K$ is a $5$-unit, and


$$
R_K\equiv3+4t\pmod5.
$$


Since $E_K\equiv4$ on this branch,


$$
\boxed{y_K\equiv d_K(1+t)\pmod5.}
\tag{13.6}
$$


Thus the complete intrinsic endpoint vanishes precisely at $t\equiv4\pmod5$, equivalently $u\equiv21\pmod{25}$, among indices with $5\mid U$.

### 13.4 Source depth modulo $25$: PASS

On the same branch,


$$
m=N-3\equiv-2+25t\pmod{125}.
$$


This is a residue evaluation of coefficient polynomials, not a negative producer index.

The first coefficients of $C_m(1-x)$ are


$$
d_1=-2m^2,\quad
d_2=\frac23m^2(m^2-1),\quad
d_3=-\frac4{45}m^2(m^2-1)(m^2-4).
$$


The factor $m^2-4$ pays the division by $5$ in $d_3$. Modulo $25$,


$$
d_1=-8,\qquad d_2=8,\qquad d_3=15t.
\tag{13.7}
$$



For higher coefficients needed below, use the integer-binomial identity


$$
[x^r]C_m(1-x)
=\frac{(-4)^r}{2}
\left\{\binom{m+r}{2r}+\binom{m+r-1}{2r}\right\}.
$$


For $r\le8$, $2r<25$. Vandermonde and
$(1+z)^{25}\equiv1+z^{25}\pmod5$ prove the required period $25$ modulo $5$, without inverting a factorial divisible by $5$.

Since $25\mid r!$ for $r\ge10$, only moments through $9$ contribute modulo $25$. At the base residue,


$$
C_2(1-x)^2=1-16x+80x^2-128x^3+64x^4,
$$


and


$$
\mathcal H(1-x)=4x-12x^2+16x^3-12x^4+5x^5-x^6.
$$


Their product has coefficients


$$
(0,4,-76,528,-1740,3269,-3857,2976,-1488,448,-64).
$$


Positive factorial weighting gives $20\pmod{25}$.

The change $d_3=15t$ changes the squared polynomial’s $x^3$-coefficient by $5t$, hence the product’s $x^4$-coefficient by $20t$. Its factorial contribution is


$$
4!\,20t\equiv5t\pmod{25}.
$$


All other variations are either zero modulo $25$, or divisible by $5$ and multiplied by a factorial divisible by $5$. Therefore


$$
\boxed{U_{N_{1+5t}}\equiv5(1-t)\pmod{25}.}
\tag{13.8}
$$


At $t\equiv4\pmod5$, $U\equiv10\pmod{25}$, so $v_5(U)=1$.

Combining (13.3), (13.4), (13.6), and (13.8) proves


$$
\boxed{
v_5(\mathfrak J^0_{N_u})
=\mathbf1_{u\equiv21\pmod{25}}.
}
\tag{13.9}
$$



The two minors also evaluate as claimed:


$$
\mathfrak m_V\equiv4/g_B^2\ne0,
$$


and


$$
\mathfrak m_K\equiv
\begin{cases}
2a_K\ne0,&u\not\equiv1\pmod5,\\
3d_K(1+t),&u=1+5t.
\end{cases}
$$


Furthermore,


$$
g_B^2\Delta\equiv3\pmod5.
$$


Thus the exception indeed has


$$
5\nmid2g_B\Delta d_K.
$$


A “good determinant prime” and independent slopes do not imply affine coprimality.

---

## 14. Binary, prime-$3$, and reused prime-$17$ scopes

### 14.1 Binary scope: PASS

The coefficient congruence $C_{2j}\equiv1\pmod8$ follows, for example, from


$$
C_{2j}=2C_j^2-1
$$


and $C_j^2\equiv1\pmod4$. Since $m=N-3$ is even,


$$
C_m^2\equiv1\pmod{16}.
$$


Therefore


$$
U\equiv-\eta(\mathcal H)=332\equiv12\pmod{16},
\qquad v_2(U)=2.
$$



For odd $N$, $b_{N-1}$ is divisible by $8$, while $b_N\equiv2\pmod4$. Hence


$$
v_2(g_B)=1,\qquad 4\mid\alpha,\qquad\beta,\delta\text{ odd}.
$$


It follows that $F^2\equiv1\pmod8$ and $8\mid V$. Thus


$$
\boxed{v_2(\mathfrak J^0)=v_2(\mathfrak J)=2.}
\tag{14.1}
$$



### 14.2 Prime-$3$ scope: PASS

Only moments of degrees below $3$ can contribute to $\eta(K)$ modulo $3$. The $x^2$-coefficient is zero modulo $3$, because $3\mid m$. The $x$-coefficient is $4$. Hence


$$
U\equiv-4\equiv2\pmod3,
$$


so


$$
\boxed{3\nmid\mathfrak J^0\mathfrak J.}
\tag{14.2}
$$


This does not extend the every-depth boundary theorem to $p=3$.

### 14.3 Prime $17$: reused, not rederived

The paid prime-$17$ arithmetic and Gaussian periods are reused. Their uniform extension uses the proved boundary lift and original exponent congruence, not finite extrapolation.

The established conclusion is


$$
17\nmid\mathfrak J^0,\qquad
v_{17}(d_K)=s_u:=v_{17}(2N_u-9)\ge1.
$$


With $e_u=v_{17}(D)$, the complete-column payment is


$$
\boxed{
v_{17}(\mathfrak J)
=\min\{v_{17}(U),e_u-s_u\}.
}
\tag{14.3}
$$


The final denominator consequence is only a divisibility:


$$
17^{\max(0,v_{17}(U)-e_u+s_u)}\mid q.
$$


It is not an equality for $v_{17}(q)$.

Consequently, the exact intrinsic narrowing remains


$$
\boxed{
\mathfrak J^0
=4\cdot5^{\mathbf1_{u\equiv21\ (25)}}\mathfrak J_{\rm rem},
\qquad
\gcd(\mathfrak J_{\rm rem},2\cdot3\cdot5\cdot17)=1.
}
\tag{14.4}
$$



---

# Part IV. A new original-domain arc-denominator theorem

## 15. Exact evaluation of $g_{\rm arc}$

The fixed cap (10.3) permits an exact original-domain evaluation using only the five possible cancellation primes.

### 15.1 Primes $2$ and $3$

Since $N=81^{9+16u}\equiv1\pmod{16}$, $x=4(N-3)^2$ is divisible by $16$. Thus $L(x)$ is odd. In $A_K(x)$, the constant term has binary valuation $1$, while every other term has larger valuation. Therefore


$$
v_2(A_K)=v_2(30L)=1,\qquad v_2(g_{\rm arc})=1.
$$



Also $N=3^{36+64u}\equiv0\pmod{81}$, so


$$
x\equiv36\pmod{81}.
$$


Hence


$$
v_3(x-9)=3,\qquad v_3(x-1)=v_3(x-25)=0,
$$


and $v_3(L)=3$. In


$$
A_K=13L+45(3x-65),
$$


the two terms have valuations $3$ and $2$, respectively. Thus


$$
v_3(A_K)=2,\quad v_3(30L)=4,\quad v_3(g_{\rm arc})=2.
\tag{15.1}
$$



### 15.2 Prime $5$

The audited calculation in §13 gives


$$
\boxed{
v_5(g_{\rm arc})=1+\mathbf1_{u\equiv1\pmod5}.
}
\tag{15.2}
$$



### 15.3 Prime $19$

Because $19\nmid30\cdot45$, simultaneous divisibility of $A_K$ and $L$ requires


$$
3x-65\equiv0\pmod{19},
$$


namely $x\equiv9\pmod{19}$. This is equivalent to


$$
N\equiv11\text{ or }14\pmod{19}.
$$


The powers of $9$ modulo $19$, through their return to $1$, are


$$
1,9,5,7,6,16,11,4,17,1.
$$


The original exponent is $18+32u\equiv5u\pmod9$. The value $14$ does not occur, while $11=9^6$. Thus


$$
19\mid g_{\rm arc}\iff5u\equiv6\pmod9
\iff u\equiv3\pmod9.
$$


The fixed cap gives valuation at most $1$, so


$$
\boxed{v_{19}(g_{\rm arc})=\mathbf1_{u\equiv3\pmod9}.}
\tag{15.3}
$$



### 15.4 Prime $31$

Likewise, modulo $31$,


$$
3x-65\equiv3(x-1),
$$


so simultaneous divisibility requires $x\equiv1$. This is equivalent to


$$
N\equiv18\text{ or }19\pmod{31}.
$$


The powers of $9$ modulo $31$ are


$$
1,9,19,16,20,25,8,10,28,4,5,14,2,18,7,1.
$$


The original exponent is $3+2u\pmod{15}$. Hence


$$
N\equiv19\iff u\equiv7\pmod{15},
$$




$$
N\equiv18\iff u\equiv5\pmod{15}.
$$


Again the fixed cap limits the valuation to $1$:


$$
\boxed{
v_{31}(g_{\rm arc})
=\mathbf1_{u\equiv5\text{ or }7\pmod{15}}.
}
\tag{15.4}
$$



No other prime can occur by (10.3). Equations (15.1)–(15.4) prove (N1).

### 15.5 Evaluated consequences

The $31$-condition is incompatible with both the $5$-extra condition and the $19$-condition:

* $u\equiv5,7\pmod{15}$ gives $u\equiv0,2\pmod5$, not $1$;
* it gives $u\equiv2,1\pmod3$, whereas $u\equiv3\pmod9$ gives $u\equiv0\pmod3$.

Therefore the only possible gcd values are


$$
90,\quad450,\quad1710,\quad2790,\quad8550.
$$


Consequently,


$$
d_K=\frac{30L}{g_{\rm arc}}
=\frac{L}
 {3\,5^{\varepsilon_5}19^{\varepsilon_{19}}31^{\varepsilon_{31}}},
$$


and


$$
\boxed{d_K\ge L/285,\quad v_2(d_K)=0,\quad v_3(d_K)=2.}
$$



One must distinguish two conclusions:

* $g_{\rm arc}\le8550$ is a **size bound**;
* it is not true that every $g_{\rm arc}$ divides $8550$, because $2790$ contains $31$.

A uniform divisibility cap from the exact formula is


$$
g_{\rm arc}\mid265050.
$$



This concrete follow-on lemma sharpens the complete original arc arithmetic after the failure of generic affine-coprimality reasoning. It does not recreate the assigned factorial-excess problem. The actual excess clearer remains


$$
\boxed{
\mu=\frac D{d_K}
=\frac{3\,5^{\varepsilon_5}19^{\varepsilon_{19}}31^{\varepsilon_{31}}D}{L(x)}.
}
$$


Neither $D$ nor $\lambda$ has been replaced by $d_K$.

---

# Part V. Status, whole errors, and remaining obligations

## 16. Assertion-by-assertion ledger

| Assertion | Verdict and exact scope |
|---|---|
| Integral finite-difference divisors for $u,\sigma$ | **PASS**, all stated nonnegative indices |
| Every original contact minor divisor, including the $Z$-atom | **PASS** |
| Complete factorial-plus-forcing return bound and balanced minimum | **PASS** |
| Exact maximal-minor column-type counts | **PASS** |
| $\mathcal W_k\notin I_{2k-1}(Y_k)$ for every $k\ge18$ | **PASS**, unconditional |
| Original-content size bound $\mathcal U_k$ | **PASS** when $H_{1,k}\ne0$; not an ideal certificate |
| Capped $3$-primary spectrum | **PASS** for $k=3^s,s\ge4,2h\le s+2$ |
| Extension of the same row-scalar proof beyond that depth | **FAIL if asserted**: cross-residue terms are no longer removed |
| Next constant $24-18\log3$ | **PASS**, with $\zeta,\chi,\log\Lambda$ retained and bounded |
| Capped spectrum or lower divisor as an upper maximal-content bound | **FAIL if asserted** |
| Integral alternating endpoint and complete coefficient planes | **PASS** |
| Both monic arc quotients and denominator boundary $2N-1$ | **PASS** |
| Fixed all-prime cubic arc cancellation cap | **PASS** |
| $\mathfrak J^0\mid\mathfrak J\mid\mu\mathfrak J^0$ and $U/\mathfrak J\mid q$ | **PASS**, all primes |
| Dual Wronskian $-2$ | **PASS**, every odd prime |
| Every-depth boundary congruence | **PASS** for $p\ge5$ |
| Freezing Gaussian data in a general lift | **FAIL if asserted**; not used in the valid proofs |
| Exact original prime-$5$ exception and depth $1$ | **PASS** |
| Unit slopes or unit $\Delta$ imply affine coprimality | **FAIL**, contradicted by the original $5$-exception |
| Binary and $3$-parts of the signed intrinsic divisor | **PASS**, at their displayed scope |
| Prime-$17$ arithmetic | **REUSED**, with complete-arc payment retained |
| New exact original $g_{\rm arc}$ formula (N1) | **NEW PROOF** |
| Compact all-prime upper content target | **OPEN** |
| Signed aggregate exceptional prime-power bound | **OPEN** |
| Rationality or irrationality of $e+\pi$ | **UNRESOLVED** |

---

## 17. The same primitive whole errors remain the relevant quantities

### 17.1 Compact conditional implications

The supplied original-index analytic estimate is


$$
\log|H_k(e+\pi)|=4k^2\log k+O(k^2).
$$


If one proved, at those same indices,


$$
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
\le(12-\eta)k^2\log k+O(k^2),
\qquad\eta>0,
$$


then (1.4) and (8.2), using the actual all-prime $G_k$, would give


$$
\log\ell_k
=\log|H_k(e+\pi)|-\log G_k
\ge\eta k^2\log k+O(k^2)\longrightarrow+\infty.
$$


At the critical leading coefficient, the correct sufficient comparison is


$$
C_H>C_J+24-18\log3.
$$



These are conditional producer-retirement deductions. Neither required content bound has been proved here.

Conversely, a proof that


$$
0<\ell_{K_u}\to0
$$


would prove irrationality of $e+\pi$. Nothing in the lower divisors or capped spectrum proves that decay.

### 17.2 Signed complete whole error

The unchanged polynomial and ordinary error are


$$
P=\frac{F^2+(V/U)K}{\delta^2},
$$




$$
\epsilon_N
=\int_0^1P(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0.
$$


The actual whole error is


$$
\boxed{
q_N(e+\pi)-p_N
=q_N\epsilon_N>0,
\qquad q_N=\frac{\lambda_NM_N}{G_N}.
}
\tag{17.1}
$$



The complete rational enclosure also remains. With $m=N-3$,


$$
J_F=
\alpha^2\frac{2N^2-1}{4N^2-1}
+\beta^2\frac{2(N-1)^2-1}{4(N-1)^2-1},
$$




$$
J_K=\frac{61}{420}
+\frac{
916j_m-399(j_{m+1}+j_{m-1})
-58(j_{m+2}+j_{m-2})
-(j_{m+3}+j_{m-3})
}{8192},
$$




$$
J_N=\frac{J_F+(V/U)J_K}{\delta^2},
$$


one has


$$
3J_N<\epsilon_N<7J_N,\qquad
q_NJ_N=\frac{\lambda_N}{G_N}(\tau_NJ_F+\nu_NJ_K).
$$


Both positive summands remain present.

The established estimates


$$
\epsilon_N\asymp R^{-2N},\qquad
\log U_N=2N\log N+O(N),\qquad
\log c_N\le N\log N+O(N)
$$


are reused, as is the paid lower bound


$$
q_N\epsilon_N>
\frac{N^N}{512\,2400^N c_N\sqrt{119N\log_2N}}.
$$


Their critical-scale arithmetic has not been improved to an aggregate saving here.

If, conditionally, one proved


$$
\mathfrak J_N^0\le e^{CN}U_N^{1-\delta_0},
\qquad\delta_0>0,
$$


then $D<256^N$, (10.5), and (10.6) would give


$$
q_N\ge e^{-C'N}U_N^{\delta_0},
$$


and therefore


$$
\log(q_N\epsilon_N)\ge2\delta_0N\log N-O(N)\to+\infty
$$


on the same original indices.

That would retire this signed producer only. It would not prove $e+\pi$ rational.

### 17.3 The separate binary producer is untouched

No compact or signed conclusion is transferred to the separate binary producer. It retains


$$
b=9^{18+32u},\quad n=4002b,\quad 0\le j<b,\quad z_b=0,
$$




$$
x=\tfrac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},\qquad x=2^ax_0,
$$


and the complete return


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f.
$$


Only its already paid bound


$$
v_2(S/2^{a+1})\ge\chi-a,\qquad
\chi=v_2\binom{n+b-1}{b-1},
$$


is retained. Its $Q=x_0^Tx_0$, actual corrected-column contents, least clearer, final all-prime gcd, primitive denominator, and whole error are not altered.

The later gray-kernel and next terminal-$J$ tasks assigned elsewhere are not silently imported into this audit.

---

## 18. Bounded exact-arithmetic verification specification

No tool execution is needed for the proofs above, and none has been performed here. The closed $k=81$, modulus-$27$, and prime-$17$ receipts should not be rerun.

If a coordinator-authored arithmetic receipt is desired for the independently audited prime-$5$ calculation and the new original arc sharpening, its inputs can remain small and bounded.

### Inputs

1. Moduli $5,25,125$.
2. The two original forced recurrences through index $6$, followed by one homogeneous slope step.
3. The thirteen weights and the four local recurrences through $k=12$, at $n=2\pmod5$.
4. The two Gaussian recurrences modulo $5$, only through return of the initial pair.
5. The degree-three polynomials $A_K,L$, and the degree-six and degree-four source-jet polynomials in §13.
6. For the new arc theorem:
   * $N\equiv1\pmod{16}$, $N\equiv0\pmod{81}$;
   * $N\equiv21+5u\pmod{25}$;
   * the displayed power tables of $9$ modulo $19$ and $31$;
   * the already proved fixed cap (10.3).

No original-degree polynomial, large content, least-clearer normalization, final $G$, or numerical $q$ is an input.

### Expected verifiable outputs

The prime-$5$ outputs are


$$
(\mathsf A,\mathsf B,\mathsf C_U,\mathsf C_E)=(4,0,2,3)\pmod5,
$$




$$
(a_N,b_N,a_{N-1},b_{N-1})=(2,1,4,4)\pmod5,
$$




$$
U=1-u,\quad g_B^2V=3,\quad E_K=4u\pmod5,
$$


and, on $u=1+5t$,


$$
R_K=3+4t\pmod5,\qquad
y_K=d_K(1+t)\pmod5,\qquad
U=5(1-t)\pmod{25}.
$$


At $t\equiv4\pmod5$, the expected source residue is $U\equiv10\pmod{25}$.

For the new arc theorem, the expected valuation output is


$$
(v_2(g_{\rm arc}),v_3(g_{\rm arc}),v_5(g_{\rm arc}),
v_{19}(g_{\rm arc}),v_{31}(g_{\rm arc}))
=
(1,2,1+\varepsilon_5,\varepsilon_{19},\varepsilon_{31}).
$$


Over the bounded residue list $u=0,\ldots,44$, the corresponding gcd-value profile is


$$
\boxed{
90^{[26]},\quad450^{[8]},\quad1710^{[4]},
\quad2790^{[6]},\quad8550^{[1]}.
}
$$


The uniform extension is justified by the proved congruences and multiplicative periods, not by extrapolating these $45$ values.

Such a receipt would check the small arithmetic only. It would not prove the outstanding compact high-depth bound, signed aggregate mass lemma, producer retirement, or irrationality.

---

## Final conclusion

The audit validates the new compact binary obstruction and capped $3$-primary theorem, including their original finite boundaries and complete forcing. It also validates the signed integral endpoint, all-odd-prime dual Wronskian, $p\ge5$ every-depth boundary lift, and exact original prime-$5$ intrinsic exception, with all Gaussian, factorial, binomial, and arc divisions paid.

The new proved contribution is the exact original-domain reduction


$$
g_{\rm arc}
=90\,5^{\mathbf1_{u\equiv1\ (5)}}
       19^{\mathbf1_{u\equiv3\ (9)}}
       31^{\mathbf1_{u\equiv5,7\ (15)}},
$$


and therefore the actual denominator formula and bound $d_K\ge L(x)/285$.

The remaining bottlenecks are unchanged in their essential scale:

* **Compact:** actual high-depth and all-prime upper control of the original maximal contents, with the true binary payment and exact finite-jet transfers.
* **Signed:** an aggregate bound for the exceptional prime-power mass in $\gcd(U,Vy_K)$, including large primes and the paid Gaussian-content and determinant branches.

The final gcds remain all-prime gcds. The primitive denominators remain $|H_{1,k}|/G_k$ and $\lambda_NM_N/G_N$. The relevant errors remain the nonzero whole errors at the same original infinite indices.

**No unconditional proof of rationality or irrationality of $e+\pi$ is obtained.**
