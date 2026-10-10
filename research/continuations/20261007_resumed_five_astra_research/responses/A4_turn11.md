> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Audit of complete-source arithmetic, endpoint normalization, and the fixed-parameter scalar telescoper

## Abstract

The supplied work does not establish either rationality or irrationality of $e+\pi$.

The principal mathematical claims audited here have the following status.

1. **Endpoint temporal repulsion is valid at its stated moving-prime cutoff.** The actual seeded recurrences are invertible over $\mathbb Z_p$ throughout the relevant block. The entrance expressions retain their necessary $F_k$-terms, and the adjacent-overlap bound follows from an explicit elimination. It does not bound an isolated terminal depth.

2. **The complete-source crossing formulas modulo $p$ and $p^2$ are correct for both Legendre branches.** Their factorial factors, Wilson quotient, half-exponent Fermat quotient, and logarithmic amplitude $2$ are indispensable.

3. **The $3\times5$ frame formulas are correct for the actual corrected columns**, subject to the retained physical-to-complete terminal identity and integrality results. In particular,
   

$$
D_8=\frac{|\det J|}{d_{\rm one}},
   \qquad
   d_{\rm one}^2\mid |\det J|\,d_{\rm all}.
$$


   Full-frame primitivity does not supply the missing endpoint-content theorem.

4. **The prime-$29$ content-scale and terminal-coordinate obstruction are valid at their stated scope.** The source recovery permits the old complete-source integrality theorem to be used for the actual producer; hence its certified source-denominator exponent is $\delta=0$. The old source recurrence and rank-three reduction are not new results.

5. **The fixed-parameter rational-antidifference obstruction is valid.** It excludes one specific first-order rational certificate, not general Green identities or creative telescoping, and gives no bound on the norm valuation $\nu$.

Two further deductions are proved below:

- an exact **all-prime endpoint denominator formula**, including the residual factorial payment, and a quantitative comparison between the actual large-prime primitive endpoint denominator and the paid contact denominator;
- a sharper **bounded terminal-candidate criterion** for the prime-$29$ coordinate obstruction.

A further correction is that the simple-pole residue condition in the proposed mixed-antidifference test is automatic for the actual interpolation degrees. Only its double-pole orbit sum can obstruct that particular rational antidifference.

These results clarify the remaining arithmetic problem but do not resolve its factorial or exponential scale.

---

## 1. Scope, original domains, and use of the supplied evidence

There are two different original families. They must not be conflated.

### 1.1 Endpoint family

Throughout the endpoint analysis,


$$
n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2,
$$


and


$$
m=n+1,\qquad N=n+2,\qquad K_{\rm phys}=2n+2.
$$


Thus $n$ is odd and $n\ge225$.

For temporal transport, an original block is


$$
n\le k\le t,\qquad t=bn,\qquad b\in\{15,105\}.
$$


The auxiliary consecutive indices do not enlarge the approximation family.

### 1.2 Prime-$29$ family

Here


$$
p=29,\qquad
E(u)=249005515+574312172u,
$$




$$
b=3^{E(u)},\qquad n=2001b,
\qquad u\ge0,\quad u\equiv2\pmod{29^9}.
$$


The original finite domains remain


$$
0\le j<b,\qquad 1\le i\le b-2,\qquad 0\le j\le b,
$$


for contact coordinates, interior source rows, and reconstructed coordinates respectively.

### 1.3 What is reused, and what is independently checked

The recovery notes identify established results whose closed proofs are not repeated:

- the original finite producers and returns;
- the actual primitive endpoint rows;
- the normalized companion and complete terminal decomposition;
- the archived endpoint intersection theorem;
- the prime-$29$ complete-source recurrence, finite displacement, rank-three reduction, and source integrality;
- the retained signed whole-error theorem for the prime-$29$ family.

The deductions below explicitly retain those dependencies. A recovery statement or a hash is not itself a replacement proof of an omitted theorem. In particular, the present audit checks the new deductions from the recovered results, rather than claiming to reconstruct every archived producer theorem.

The two supplied numerical receipts are treated as **reported finite exact-arithmetic results**. Their scope is not enlarged to an infinite family. No computation has been performed here.

---

# Part I. Endpoint audit

## 2. The complete physical construction is unchanged

Put


$$
q(z)=1-z+\frac{z^2}{2},\qquad q_j=[z^j]q(z)^n,
$$


and


$$
\alpha_0=\alpha_1=1,\qquad
\alpha_s=\alpha_{s-1}-\frac12\alpha_{s-2}.
$$


The actual complete source is


$$
\eta_s=\sum_{r=0}^s\frac1{r!}
       +2\sum_{r=1}^s\frac{\alpha_{r-1}}r,
\qquad
\mathcal W_s=s!\eta_s.
$$


Its physical force is


$$
w_i=
\sum_{j=0}^{\min(2n,n+i)}
q_j(n+i)^{\underline j}\mathcal W_{2n+i-j},
\qquad 0\le i\le2,
$$


with


$$
\widehat w_i=\frac{w_i}{(n+i)!}.
$$


The largest source index is exactly $K_{\rm phys}=2n+2$.

Let


$$
c_k=[z^k]e^zq(z)^n,
\qquad
T=
\begin{pmatrix}
c_n&c_{n-1}&c_{n-2}\\
c_{n+1}&c_n&c_{n-1}\\
c_{n+2}&c_{n+1}&c_n
\end{pmatrix}.
$$


The raw endpoint rows are


$$
R_j^{\rm raw}=\ell_j\operatorname{adj}(T),
\qquad
\ell_0=(-1,n,-nm),\quad \ell_3=(0,0,1).
$$


The physical returns are


$$
N_0=\det T+R_0^{\rm raw}\widehat w,
\qquad
N_3=R_3^{\rm raw}\widehat w.
$$


The exterior return in $N_0$ is not optional.

With


$$
t_{\rm ref}=
\begin{pmatrix}
\tau_n\\
(\tau_n+\tau_{n+1})/2\\
\tau_{n+2}/2
\end{pmatrix},
\quad
x=T^{-1}(n!t_{\rm ref}),\quad y=T^{-1}\widehat w,
$$


and


$$
S=
\begin{pmatrix}
1&-n&nm\\
0&1&-2n\\
0&0&1
\end{pmatrix},
$$


write $sx=Sx,\ sy=Sy$. The complete corrected columns are


$$
u=(-sx_0,\ sx_0-sx_1,\ sx_1-sx_2,\ sx_2),
$$




$$
v=(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2).
$$


In particular, the original exterior $+1$ remains present.

All uses of $T^{-1}$ require $\det T\ne0$. No inverse is extended beyond the original physical terminal, and the retained coefficient $1$ of the terminal force $\mathfrak f_{K_{\rm phys}}$ in $b_{K_{\rm phys}+1}$ is not removed.

---

## 3. Temporal primitivity, entrance expressions, and overlap bounds

### 3.1 Primitivity is valid for the actual seeds

Write


$$
m_k=k+1,\quad N_k=k+2,\quad A_k=k^2+3k+1.
$$


The supplied moment recurrence is


$$
z_{k+1}=\mathsf U_kz_k,\qquad z_k=(P_k,Q_k,F_k)^T,
$$


where


$$
\mathsf U_k=
\begin{pmatrix}
0&m_kN_k&N_k/2\\
N_k&-A_k&-\dfrac{kN_k}{2m_k}\\
-N_k(2k+3)&N_kA_k&\dfrac{N_k(k^2-2)}{2m_k}
\end{pmatrix},
$$


with actual seed


$$
z_2=(0,10,-66)^T.
$$


Direct expansion gives


$$
\det\mathsf U_k=\frac{(k+1)(k+2)^2(k+3)}2.
$$



The reference recurrence is


$$
\binom{\tau_{k+1}}{\tau_{k+2}}
=
\begin{pmatrix}
0&1\\
(k+1)/(k+2)&(2k+3)/(k+2)
\end{pmatrix}
\binom{\tau_k}{\tau_{k+1}},
$$


with seed $(\tau_2,\tau_3)=(2,4)$, and determinant


$$
-\frac{k+1}{k+2}.
$$



If $p>t+2$, every denominator and determinant factor occurring for
$2\le k<t$ is a $p$-adic unit. Both recurrences therefore lie in the appropriate general linear group over $\mathbb Z_p$. The two actual seeds are primitive over $\mathbb Z_p$, since $p>t+2>2$. Hence all transported states are primitive.

This validates the primitivity hypotheses used in A3 turn 4. It is not a seed-free assertion.

### 3.2 The entrance expressions are correct

Define


$$
\overline M_k=Q_k\tau_k-P_k\tau_{k+1}.
$$


Set $u=\tau_k,\ v=\tau_{k+1}$ and


$$
H_k=3k^2+8k+4.
$$


The complete entrance forms are


$$
\mathcal L_k=
-2m_k(2k+3)P_k
+2m_kA_kQ_k
+(k^2-2)F_k,
$$


and


$$
\begin{aligned}
\mathcal E_k={}&
2m_kN_kP_kv-2m_k^3Q_ku-2m_kH_kQ_kv\\
&-\bigl(m_k^2u+(3k^2+7k+3)v\bigr)F_k.
\end{aligned}
$$


Substitution gives exactly


$$
\mathcal L_k=\frac{2m_k}{N_k}F_{k+1},
\qquad
\mathcal E_k=2m_k\overline M_{k+1}.
$$



For example,


$$
\begin{aligned}
\overline M_{k+1}
={}&N_kP_kv-m_k^2Q_ku-(A_k+m_k(2k+3))Q_kv\\
&-\left(\frac{m_k}{2}u+
\frac{kN_k+m_k(2k+3)}{2m_k}v\right)F_k.
\end{aligned}
$$


Multiplication by $2m_k$ yields the stated $\mathcal E_k$.

**The $F_k$-terms are essential.** Omitting them gives repeated-alignment equations, not the equations for a new isolated entrance.

### 3.3 The overlap elimination is valid

For $p>t+2$, let


$$
a_k(p)=\min\{v_p(F_k),v_p(\overline M_k)\}.
$$


Suppose


$$
e=\min(a_k(p),a_{k+1}(p))>0.
$$


Primitivity implies, modulo $p^e$,


$$
(P_k,Q_k,F_k)\equiv\eta(u,v,0)
$$


with $\eta$ a unit.

Put


$$
B_k=2k+3,\qquad K_k=k^2+8k+11.
$$


The next $F$-equation gives


$$
B_ku-A_kv\equiv0\pmod{p^e}.
$$


The next alignment equation gives


$$
v\bigl((N_k-m_k^2)u-H_kv\bigr)\equiv0\pmod{p^e}.
$$


The required elimination identity is


$$
(N_k-m_k^2)A_k-B_kH_k=-m_k^2K_k.
$$



If $v$ is a unit, elimination gives $p^e\mid K_k$. If $v$ is not a unit, $u$ is a unit and $p\mid B_k$. At $k=-3/2\pmod p$,


$$
N_k-m_k^2\equiv\frac14\pmod p,
$$


so the second bracket is a unit. Consequently $p^e\mid v$, and then $p^e\mid B_k$. Thus


$$
\boxed{\min(a_k(p),a_{k+1}(p))\le v_p(B_kK_k).}
$$



For $n\le k<t$,


$$
0<B_k\le2t+1<p^2,
$$




$$
0<K_k\le t^2+6t+4<(t+3)^2\le p^2.
$$


The two factors cannot both vanish modulo $p$, because $B_k=0$ gives


$$
4K_k\equiv5\pmod p.
$$


Hence every overlap has depth at most one.

There are at most three roots modulo $p$ of $B_kK_k$, and the interval has length less than $p$. Therefore


$$
\boxed{\sum_{k=n}^{t-1}\min(a_k(p),a_{k+1}(p))\le3.}
$$



The exclusion of three consecutive positive depths is also correct. The possible common-root pairings at adjacent steps lead only to the exceptional primes


$$
2,\ 29,\ 11,\ 19,
$$


all excluded by $p>t+2$.

### 3.4 Exact limitation

These statements do not bound $a_t(p)$ when $a_{t-1}(p)=0$. They therefore do not bound


$$
\sum_{p>t+2}(a_t(p)-a_n(p))_+\log p
$$


at the required scale.

Nor do they yield useful acquisition in the required direction. The retained identity is


$$
\mathcal I_t=
\frac{\mathcal I_n c^{\min}_{n,t}}
{\mathcal M_{n,t}\mathcal L_{n,t}},
$$


where


$$
\mathcal M_{n,t}
=
\prod_{n+2<p\le t+2}
p^{\min(v_p(F_n),v_p(M_n))}
$$


and


$$
\mathcal L_{n,t}
=
\prod_{p>t+2}p^{(a_n(p)-a_t(p))_+}.
$$


Growth of useful inventory requires an acquisition **lower bound** sufficient to pay both losses. An upper bound on endpoint contact loss is a different objective.

---

## 4. Complete-contact payment and its scope

Let


$$
V=(v'\;w'\;e_2),\qquad
v'=(2N,N,m)^T,\quad w'=(0,N,2n+3)^T,
$$


and let $r_j$ be the actual primitive integer endpoint row.

Write


$$
r_jV=(\alpha_j,\beta_j,r_{j,2}),
\qquad G_j=\gcd(|\alpha_j|,|\beta_j|).
$$


The actual three-coordinate content is $\kappa_j$, and


$$
G_j=\kappa_jd_{c,j},\qquad
b_{c,j}=\gcd(d_{c,j},|C|),\quad C=mZ.
$$



The recovered complete terminal is


$$
\mathbf C=S_cv'+T_cw'+Ce_2,
$$


with


$$
S_c=\frac m2b_n+2n!m!\rho_n,
$$




$$
T_c=b_{n+1}-\frac m2b_n+2n!m!\rho_{n+1}.
$$


The complete contact is $C_j=r_j\mathbf C$.

The overlap identification gives exactly


$$
C_j=\kappa_jb_{c,j}\mathscr E_j.
$$


Since $\kappa_jb_{c,j}$ divides both $G_j$ and $C_j$, the archived intersection theorem implies


$$
\kappa_3b_{c,3}\mid4m^2N^2,
$$




$$
\kappa_0b_{c,0}\mid4m^2N^2(n+3).
$$


This transport is valid. It uses the archived theorem for the actual primitive rows and moment state; it does not reprove that theorem.

Because $n$ is odd, every prime divisor of $n+3$ is at most $(n+3)/2<N$. Therefore


$$
(\kappa_jb_{c,j})_{>N}=1.
$$


Thus the payment is polynomial in size and removes no prime above $N$.

Under the retained hypotheses


$$
\det T\ne0,\qquad F\ne0,\qquad \widehat R_j\ne0,
$$


the paid comparison consequently remains


$$
\gcd(|T_{\rm aff}|,D_j)_{>N}
=
\gcd(|C_j|,D_j)_{>N},
$$


where


$$
D_j=\frac{|\widehat R_j|}{\gcd(|\widehat R_j|,|F|)}.
$$



The local valuation argument is sound: after the stated unimodular contact-coordinate change, the complementary reference coordinate is a unit; division by the actual $g_{\rm aff}$ leaves a unit coefficient multiplying the complete residual. No unit hypothesis on an auxiliary third coordinate is needed.

This does **not** evaluate $\gcd(D_j,C_j)$.

The seed-blind amplitude obstruction is also correctly delimited. At a contact prime $p>N$ with $p\nmid G_j$, the companion determinant


$$
\tau_n\rho_{n+1}-\tau_{n+1}\rho_n=\frac{(-1)^n}{n+1}
$$


is a unit, so the companion-amplitude slope is a unit. Arbitrary amplitude variation can force resonance by CRT. This excludes only arguments uniform in that amplitude family; the original amplitude remains exactly $2$.

---

## 5. Audit of the source crossing at both $p$-adic levels

### 5.1 Exact recurrence and prime seed

The complete source satisfies


$$
\boxed{\mathcal W_s=s\mathcal W_{s-1}
+1+2(s-1)!\alpha_{s-1}.}
$$


This follows directly by multiplying $\eta_s-\eta_{s-1}$ by $s!$.

For odd $p$, put


$$
\chi_p=\left(\frac{-1}{p}\right),
\qquad
\varepsilon_p=\left(\frac2p\right).
$$


The characteristic roots $(1\pm i)/2$ give the exact identity


$$
\alpha_{p-1}=\chi_p\varepsilon_p2^{-(p-1)/2}.
$$


Euler’s criterion then gives


$$
\alpha_{p-1}\equiv\chi_p\pmod p.
$$



For $N<p\le K_{\rm phys}$, Wilson’s theorem yields


$$
\mathcal W_p\equiv1-2\chi_p\pmod p.
$$


Thus the two branch values are


$$
-1\quad(\chi_p=1),\qquad 3\quad(\chi_p=-1),
$$


both units in the original range.

### 5.2 Crossing modulo $p$

Since $K_{\rm phys}<2p$, for


$$
1\le d\le K_{\rm phys}-p
$$


the factorial $(p+d-1)!$ contains a factor $p$. Therefore


$$
\mathcal W_{p+d}\equiv d\mathcal W_{p+d-1}+1\pmod p.
$$


If


$$
E_0=1,\qquad E_d=dE_{d-1}+1,
$$


then


$$
\boxed{\mathcal W_{p+d}\equiv E_d-2\chi_p d!\pmod p.}
$$



The $d!$ is necessary. It is the homogeneous propagation of the complete crossing seed.

For illustration, at the next position,


$$
\mathcal W_{p+1}\equiv
\begin{cases}
0&\chi_p=1,\\
4&\chi_p=-1.
\end{cases}
$$


Thus even the source itself is not uniformly a unit after crossing. A unit crossing seed cannot be propagated into a unit assertion for all later source values, much less for their endpoint convolution.

### 5.3 Crossing modulo $p^2$

Define the integer quotients


$$
\mathfrak w_p=\frac{(p-1)!+1}{p},
\qquad
\mathfrak h_p=
\frac{2^{(p-1)/2}-\varepsilon_p}{p}.
$$


Set


$$
B_d=E_d-2\chi_pd!,
\qquad
R_d=\frac{\mathcal W_{p+d}-B_d}{p}.
$$



Expanding


$$
2^{(p-1)/2}=\varepsilon_p+p\mathfrak h_p
$$


gives


$$
\alpha_{p-1}
\equiv
\chi_p-p\chi_p\varepsilon_p\mathfrak h_p
\pmod{p^2}.
$$


Together with


$$
(p-1)!=-1+p\mathfrak w_p,
$$


the exact recurrence at $s=p$ gives


$$
\boxed{
R_0\equiv
\mathcal W_{p-1}
+2\chi_p(\mathfrak w_p+\varepsilon_p\mathfrak h_p)
\pmod p.}
$$



For $d\ge1$,


$$
\frac{(p+d-1)!}{p}\equiv-(d-1)!\pmod p.
$$


Consequently,


$$
\boxed{
R_d\equiv
dR_{d-1}+B_{d-1}-2(d-1)!\,a_d\pmod p,}
$$


where


$$
a_d=
\begin{cases}
\alpha_d&\chi_p=1,\\[1mm]
\frac12\alpha_{d-2}&\chi_p=-1,
\end{cases}
\qquad \alpha_{-1}=0.
$$



The second branch follows because Frobenius interchanges the characteristic roots:


$$
\frac{r_-r_+^d-r_+r_-^d}{r_+-r_-}
=\frac12\alpha_{d-2}.
$$


In particular, at $d=1$ this branch contributes zero, not $\alpha_1$.

**Audit decision:** both branch formulas are correct, including the factorial factors and the complete seed. They give only the first two levels. Deep endpoint cancellation remains uncontrolled.

---

## 6. Integer-frame invariants and endpoint saturation

### 6.1 Matching the physical source

Define


$$
J=N!T,\qquad H=N!t_{\rm ref},\qquad
E_n=n!\sum_{r=0}^n\frac1{r!}.
$$


The retained terminal identity is


$$
N!\widehat w=J_0+E_nH+\mathbf C.
$$


Its physical coefficient representation is consistent with


$$
\widehat w_i=
[z^{n+i}]q(z)^n\frac{d^n}{dz^n}
\left(
\frac{e^z+2\int_0^zq(t)^{-1}\,dt}{1-z}
\right).
$$


Indeed, differentiating the series produces precisely the original finite convolution.

The further decomposition into the archived exponential and logarithmic terminal columns uses the recovered three-row terminal identities. No earlier-row homogeneous logarithmic recurrence is inferred from it.

Put


$$
A_{\rm src}=n!H,\qquad B_{\rm src}=\mathbf C+E_nH,
$$


and


$$
B_\partial=
\begin{pmatrix}
-1&n&-nm\\
1&-n-1&nm+2n\\
0&1&-2n-1\\
0&0&1
\end{pmatrix}.
$$


Then


$$
u=B_\partial J^{-1}A_{\rm src},
\qquad
v=e_1+B_\partial J^{-1}B_{\rm src},
\quad e_1=(0,1,0,0)^T.
$$



The exterior correction has moved from row $0$ to the integral vector $e_1$; it has not disappeared.

### 6.2 Least simultaneous clearer

Let


$$
\Delta_J=\det J,\quad Q_J=|\Delta_J|,
$$




$$
a=\operatorname{adj}(J)A_{\rm src},
\qquad b=\operatorname{adj}(J)B_{\rm src},
$$




$$
U=B_\partial a,\qquad V=\Delta_Je_1+B_\partial b.
$$


The last three rows of $B_\partial$ form a unimodular matrix, so $B_\partial$ has an integral left inverse.

Hence


$$
\gcd(Q_J,U_0,\ldots,U_3,V_0,\ldots,V_3)
=
\gcd(Q_J,a_0,a_1,a_2,b_0,b_1,b_2).
$$


The right side is $d_{\rm one}$, the gcd of the determinant and the six one-replacement determinants. Therefore


$$
\boxed{D_8=\frac{Q_J}{d_{\rm one}}.}
$$



This is an identity for the actual eight entries, not a proposed substitute for their least clearer.

### 6.3 Full-frame content

Let $d_{\rm all}$ be the gcd of all ten maximal minors of


$$
[J_0,J_1,J_2,A_{\rm src},B_{\rm src}].
$$


Clearly


$$
d_{\rm all}\mid d_{\rm one}\mid Q_J.
$$


The adjugate identity


$$
\Delta_J\det(J_i,A_{\rm src},B_{\rm src})
=
\pm(a_rb_s-a_sb_r)
$$


shows that


$$
d_{\rm one}^2\mid
\Delta_J\det(J_i,A_{\rm src},B_{\rm src})
$$


for each complementary pair $r,s$. Taking the gcd over all maximal minors gives


$$
\boxed{d_{\rm one}^2\mid Q_Jd_{\rm all}.}
$$



The quotient lattice


$$
\frac{J\mathbb Z^3+\mathbb ZA_{\rm src}+\mathbb ZB_{\rm src}}
{J\mathbb Z^3}
$$


has order $Q_J/d_{\rm all}$, is generated by two elements, and has exponent $D_8$. Thus its invariant factors are


$$
\boxed{\frac{d_{\rm one}}{d_{\rm all}},
\qquad\frac{Q_J}{d_{\rm one}}.}
$$



At a prime where $d_{\rm all}$ is a unit,


$$
\left\lceil\frac{v_p(\Delta_J)}2\right\rceil
\le v_p(D_8)\le v_p(\Delta_J).
$$


Full-frame primitivity therefore does not make the common clearer small.

### 6.4 Actual row contents

For every nonzero row pair,


$$
g_j^{\rm num}=\gcd(|U_j|,|V_j|),
$$




$$
g_j^{(8)}=\frac{g_j^{\rm num}}{d_{\rm one}},
$$


and


$$
\widetilde u_j=
\operatorname{sgn}(\Delta_J)\frac{U_j}{g_j^{\rm num}},
\qquad
\widetilde v_j=
\operatorname{sgn}(\Delta_J)\frac{V_j}{g_j^{\rm num}}.
$$


Thus


$$
|\widetilde u_j|=\frac{|U_j|}{\gcd(|U_j|,|V_j|)}.
$$


The common clearer and full-frame content cannot replace this rowwise gcd.

### 6.5 Extra minors: the factorial is correct

Using the supplied coordinates


$$
J_i=\frac12VW^{(i)},\qquad
H=\frac{m!}{2}V(\tau_n,\tau_{n+1},0)^T,
$$


and $\det V=2N^2$, one obtains


$$
\begin{aligned}
\det(J_i,A_{\rm src},B_{\rm src})
=\frac{n!m!N^2}{2}\Big[
&C(\tau_{n+1}W^{(i)}_1-\tau_nW^{(i)}_2)\\
&+(\mathcal K_n-2(n!)^2)f_i
\Big].
\end{aligned}
$$


The factor $n!m!N^2/2$ is correct: it comes from $n!$, the two factors $1/2$, and $\det V=2N^2$. The complete companion contribution is $-2(n!)^2$ at the original odd indices. Neither factorial may be dropped.

### 6.6 The omitted-column obstruction is genuine

The endpoint kernels are


$$
\begin{array}{c|c|c}
j&\text{kernel columns}&\text{omitted column}\\ \hline
3&J_0,J_1&J_2\\
0&nJ_0+J_1,\ -nmJ_0+J_2&J_0.
\end{array}
$$


If


$$
K_{j,1}\times K_{j,2}=\pm h_j^Kr_j,
$$


then


$$
r_jJ_{\rm omit}=\pm\frac{\Delta_J}{h_j^K}.
$$



After paying the kernel saturation index $h_j^K$, the endpoint-restricted maximal-minor content is


$$
\gcd(|r_jH|,|C_j|).
$$


After adjoining the omitted moment column, it is only


$$
\gcd\left(
|r_jH|,\ |C_j|,\ \left|\frac{\Delta_J}{h_j^K}\right|
\right).
$$



Therefore endpoint annihilation of $H$ and $\mathbf C$ does not imply rank loss of the full frame. If $p\nmid\Delta_J$, the omitted projection is a unit and full rank is automatic.

This refutes the proposed rank implication, not a conjectural numerical bound for the actual endpoint correlation.

---

## 7. New endpoint consequence: exact primitive denominator with all factorial payments

The preceding identities permit a direct theorem about the **actual primitive endpoint denominator**.

### Theorem 7.1 — Complete-source endpoint denominator

Fix $j=0$ or $3$, and assume the endpoint first entry is nonzero. Put


$$
R_j=r_jH,\qquad
g_j^*=\gcd(|R_j|,|C_j|).
$$


Define


$$
\zeta_j=
\frac{C_j+E_nR_j}{g_j^*}\in\mathbb Z,
\qquad
\phi_j=\gcd(n!,|\zeta_j|).
$$


Then


$$
\boxed{
|\widetilde u_j|
=
\frac{|R_j|}{g_j^*}\,\frac{n!}{\phi_j}.
}
\tag{7.1}
$$



In particular, the only extra all-prime payment beyond
$|R_j|/\gcd(R_j,C_j)$ is the explicitly retained divisor


$$
\frac{n!}{\gcd(n!,|\zeta_j|)}
$$


of $n!$.

#### Proof

For an endpoint, the corresponding coordinate of $e_1$ is zero. The integer row


$$
(B_\partial)_j\operatorname{adj}(J)
$$


is an integer multiple $\gamma_jr_j$ of the actual primitive row. Therefore


$$
U_j=\gamma_j n!R_j,
\qquad
V_j=\gamma_j(C_j+E_nR_j).
$$


The actual row gcd cancels $|\gamma_j|$, giving


$$
|\widetilde u_j|
=
\frac{n!|R_j|}
{\gcd(n!|R_j|,\ |C_j+E_nR_j|)}.
$$



Since


$$
\gcd(R_j,C_j+E_nR_j)=g_j^*,
$$


the two integers


$$
R_j/g_j^*,\qquad \zeta_j
$$


are coprime. Hence


$$
\gcd(n!R_j/g_j^*,\zeta_j)=\gcd(n!,\zeta_j)=\phi_j.
$$


This proves (7.1). ∎

The cancellation of $\gamma_j$ is not an unpaid saturation: it occurs inside the actual two-entry row gcd.

### Corollary 7.2 — Exact large-prime valuation and paid-contact comparison

At $p>N$,


$$
r_jH=\frac{m!}{2L}\widehat R_j,
\qquad L=2^{(n+1)/2},
$$


and the multiplier is a unit. Thus, writing


$$
r=v_p(\widehat R_j),\quad c=v_p(C_j),\quad f=v_p(F),
$$


one has


$$
\boxed{v_p(|\widetilde u_j|)=(r-c)_+.}
\tag{7.2}
$$



Let


$$
S_j=\gcd(D_j,|C_j|)_{>N},
\qquad
D_{j,>N}=(D_j)_{>N}.
$$


Then


$$
\boxed{
\frac{D_{j,>N}}{S_j}
\ \mid\
(|\widetilde u_j|)_{>N}
\ \mid\
F_{>N}\frac{D_{j,>N}}{S_j}.
}
\tag{7.3}
$$


More precisely, the quotient in the first divisibility has valuation


$$
\boxed{\min\{f,(r-c)_+\}.}
\tag{7.4}
$$



#### Proof

The valuation of $D_j/S_j$ is


$$
(r-f-c)_+.
$$


Subtracting this from $(r-c)_+$ gives


$$
(r-c)_+-(r-f-c)_+
=\min\{f,(r-c)_+\}.
$$


This lies between $0$ and $f$. ∎

This is a quantitative transport to the actual primitive endpoint denominator, not merely another frame projection. It also identifies the limitation precisely:

- above $N$, the paid contact denominator determines the actual endpoint denominator up to an explicit divisor of $F$;
- at small primes, the residual factorial factor in (7.1) remains;
- neither $F$, the complete contact gcd, nor the final weighted gcd has acquired an asymptotic bound.

Thus this theorem improves the accounting but does not yet improve the exponential or factorial budget.

---

# Part II. Prime-$29$ audit

## 8. Complete force, old recurrence, and arithmetic scale

The original columns remain


$$
Z_w=\mathcal RA^{-1}f^0,
\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b,
$$


where


$$
W_j=\binom{n+2}{j},
\qquad
(\mathcal R\theta)_j=W_j(j\theta_{j-1}-\theta_j),
\quad \theta_{-1}=\theta_b=0.
$$


The complete first force is


$$
f_i^0=\frac{(n+i)!}{n!}
[z^n](1+2z+2z^2)^n(1+z)^i.
$$


With the retained unit $C_n=f_0^0$,


$$
\bar f=f^0/C_n,\qquad \bar Z=Z_w/C_n.
$$



The second force is still


$$
\mathbf r=A_{IE}z+\frac{h^F}{b!},
\qquad z_h=\frac{(b+h)!}{b!}.
$$


Its two complete initial charges include


$$
r_i=\sum_s a_s(n)(n+i)_{\underline s}
\left(T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}\right),
\qquad i=0,1,
$$


and its interior forcing includes every


$$
\mathcal H_i=
\sum_s a_s(n+1)(n+i)_{\underline s}
\binom{2n+i-s+1}{b},
\qquad1\le i\le b-2.
$$



The recovered actual matrix rule is


$$
A_{\rm ext}(i,j)=
\sum_s s![z^s]q(z)^n
\binom{n+i}{s}\binom{2n+i-s}{j}.
$$


Thus the old moment-source results apply to the actual producer, not merely to a matrix sharing its modular inverse.

In particular, the already established recurrence is


$$
\begin{aligned}
r_{i+1}-(2n+2i+1)r_i
&+\frac{(n+i)(n+3i-1)}2r_{i-1}\\
&-\frac{(i-1)(n+i)(n+i-1)}2r_{i-2}
=\mathcal H_i.
\end{aligned}
$$


Its leading coefficient is $1$; division by $2$ is harmless at $29$. The old proof retains both logarithmic initial charges and proves zero additional logarithmic forcing in the interior range.

Accordingly, the recovered complete-source integrality theorem gives


$$
\boxed{\delta=0}
$$


for the actual family. This is a reused result, not a novelty of A2 turn 7.

The old rank-three reduction is likewise reused. It does not assert saturation of the weighted lattice and does not evaluate the primitive norm valuation.

### 8.1 The bound on $c$

Write


$$
Z_w=29^{c+2}x,
$$


with $x$ primitive at $29$. The lower inequality


$$
c+2\le w,\qquad w=v_{29}\binom{n+2}{b},
$$


is a retained original terminal theorem. It should not be inferred merely from divisibility of the last coordinate.

The upper bound is independently elementary. Let


$$
M=\lfloor\log_{29}(n+2)\rfloor.
$$


Legendre’s formula gives


$$
w=\sum_{k\ge1}
\left(
\left\lfloor\frac{n+2}{29^k}\right\rfloor
-\left\lfloor\frac b{29^k}\right\rfloor
-\left\lfloor\frac{n+2-b}{29^k}\right\rfloor
\right).
$$


Each summand is $0$ or $1$, and all vanish for $29^k>n+2$. Hence


$$
\boxed{c+2\le w\le M,}
$$


and


$$
\boxed{29^{2c+4}\le(n+2)^2.}
$$



A factor $29^{O(c)}$ therefore has logarithm $O(\log n)$. It cannot by itself offset an exponential error or a factorial-scale denominator.

This does not bound $v_{29}(g_B)$, because primitive norm and mixed-product cancellation remain separate.

---

## 9. Strong coordinate obstruction and a sharper candidate bound

Put


$$
\bar Z=29^a\bar x,\qquad a=c+2,
$$




$$
\bar x^T\bar x=29^\nu\bar\eta,
\qquad \bar\eta\in\mathbb Z_{29}^\times,
$$


and


$$
K_{\rm loc}=a+2+\nu.
$$


The terminal vector and projection are


$$
t_j=\frac{(N-j)!}{(N-b)!},\qquad t_b=1,
$$




$$
\tau=t^Tt\equiv8\pmod{29},\qquad
P=I-\frac{tt^T}{\tau}.
$$


The scalar objective is


$$
\bar Z^T(6PY-29\bar Z)\in29^{2a+\nu+2}\mathbb Z_{29},
$$


whereas the stronger proposal is


$$
6PY-29\bar Z\in29^{K_{\rm loc}}\mathbb Z_{29}^{b+1}.
$$



The latter indeed implies the additional norm condition


$$
36\|PY\|^2-29^2\|\bar Z\|^2
\in29^{2a+\nu+3}\mathbb Z_{29}.
$$


That condition is not required by scalar alignment alone.

### 9.1 Audit of the terminal obstruction

For $r\in\{1,\ldots,b\}$, put $j=b-r$ and


$$
F_r=\frac{b!}{(b-r)!},\qquad
G_r=\frac{(N-b+r)!}{(N-b)!},
$$




$$
f_r=v_{29}(F_r),\qquad g_r=v_{29}(G_r).
$$


Then


$$
W_{b-r}=W_b\frac{F_r}{G_r},
\qquad
v_{29}(W_{b-r})=w+f_r-g_r.
$$



Define


$$
T_{b-r}=
\sum_{s=0}^{b-r}
\left((N-b+r+1)^{\overline s}\right)^2,
\qquad
t_r^{\rm sq}=v_{29}(T_{b-r}).
$$


The established integral unitriangular reconstruction gives


$$
\bigl(E(6PY-29\bar Z)\bigr)_{b-r}
=
-W_{b-r}h_{b-r}
-\frac{6W_b}{\tau}G_rT_{b-r}.
$$


If $h\in29^{-\delta}\mathbb Z_{29}^b$, the first term has valuation at least


$$
w+f_r-g_r-\delta,
$$


while the second has exact valuation


$$
w+g_r+t_r^{\rm sq}.
$$


Thus the two strict inequalities


$$
f_r>2g_r+t_r^{\rm sq}+\delta,
$$




$$
K_{\rm loc}>w+g_r+t_r^{\rm sq}
$$


force failure of the strong coordinate target.

This is a valid unequal-valuation obstruction. It retains the physical terminal, which creates the second term.

The original cutoff


$$
r<
\left\lceil\frac{812}{27}
\bigl(\lfloor\log_{29}b\rfloor+2\bigr)\right\rceil
$$


is also valid, from


$$
f_r\le r/28+\lfloor\log_{29}b\rfloor,
\qquad
g_r\ge r/29-1.
$$



### 9.2 New sharpened terminal-candidate lemma

The binomial valuation bound used for $W_b$ applies to every $W_j$:


$$
v_{29}\binom Nj\le M=\lfloor\log_{29}N\rfloor.
$$


Consequently,


$$
w+f_r-g_r\le M.
$$



Suppose a row satisfies the first obstruction inequality. Since all quantities are integers,


$$
f_r\ge2g_r+t_r^{\rm sq}+\delta+1.
$$


Combining the two inequalities yields


$$
\boxed{
w+g_r+t_r^{\rm sq}\le M-\delta-1.
}
\tag{9.1}
$$


It also gives


$$
g_r<M-w-\delta.
$$


Since $g_r\ge\lfloor r/29\rfloor$,


$$
\boxed{
r<29(M-w-\delta).
}
\tag{9.2}
$$



Therefore:

- if $M-w-\delta\le0$, no row can satisfy this terminal-lattice obstruction;
- every possible witness lies below both the original cutoff and (9.2);
- if $K_{\rm loc}\ge M-\delta$, every row satisfying the first obstruction inequality automatically satisfies the second.

For the recovered actual source, $\delta=0$. Hence


$$
r<29(M-w),
$$


and any candidate witness has boundary valuation at most $M-1$.

This is a new bounded arithmetic consequence. It does not assert that a witness exists at an original index.

### 9.3 The square-sum test remains genuinely finite

For a candidate put


$$
M_r=f_r-2g_r-\delta.
$$


When $M_r>0$, compute modulo $29^{M_r}$


$$
s_0=1,\qquad
s_{h+1}=s_h(N-b+r+1+h)^2.
$$


Since every product of $h$ consecutive integers is divisible by $h!$,


$$
v_{29}(s_h)\ge2v_{29}(h!).
$$


Thus all terms vanish once


$$
h\ge29\left\lceil M_r/2\right\rceil.
$$


The exact original finite sum is therefore determined modulo $29^{M_r}$ by


$$
\sum_{h=0}^{\min\{b-r,\;29\lceil M_r/2\rceil-1\}}s_h.
$$



No arbitrary suffix or infinite replacement sum is involved.

Failure of the coordinate target still does not imply failure of the scalar target: the coordinate defect can be orthogonal to $\bar Z$ at the required precision.

---

## 10. Audit of the genuinely new rational-antidifference obstruction

Let $U\in\mathbb Q[X]$, $\deg U\le b$, interpolate


$$
U(j)=(-1)^j\bar\theta_j\quad(0\le j<b),\qquad U(b)=0,
$$


and define


$$
H_{\rm pol}(X)=XU(X-1)+U(X).
$$


Then


$$
\bar Z_j=(-1)^{j-1}W_jH_{\rm pol}(j)
$$


for every $0\le j\le b$.

Likewise, the second interpolation must use


$$
V(b)=(-1)^{b+1},
$$


so that it encodes the physical $W_be_b$. With


$$
G_{\rm pol}(X)=XV(X-1)+V(X),
$$


one has


$$
Y_j=(-1)^{j-1}W_jG_{\rm pol}(j).
$$



The interpolation denominators are rational denominators; a factorial interpolation clearer is not a $29$-adic unit and is not the original $d_B$.

### 10.1 The no-go proof is correct

Suppose a rational function $R(X)$ satisfied


$$
\frac{(N-X)^2}{(X+1)^2}R(X+1)-R(X)=H_{\rm pol}(X)^2.
$$


Let


$$
D_N(X)=\prod_{k=0}^N(X-k),
\qquad
F(X)=\frac{R(X)}{D_N(X)^2}.
$$


Because


$$
\frac{D_N(X+1)}{D_N(X)}=\frac{X+1}{X-N},
$$


this would imply


$$
F(X+1)-F(X)=\frac{H_{\rm pol}(X)^2}{D_N(X)^2}.
$$



For a rational difference, the sum of the coefficients of poles of a fixed order along a complete integer-translation orbit is zero. Translation simply shifts a finitely supported coefficient sequence.

The double-pole coefficients on the right are


$$
\frac{H_{\rm pol}(k)^2}{k!^2(N-k)!^2},
\qquad0\le k\le N.
$$


Their sum is strictly positive.

Indeed, $\bar Z\ne0$: $\bar f_0=1$, $A$ is invertible, and $\mathcal R$ is injective on the original contact space. Thus $H_{\rm pol}\ne0$. Also


$$
\deg H_{\rm pol}\le b+1<N+1,
$$


so it cannot vanish at all $N+1$ integers.

The positive orbit sum contradicts the necessary zero-sum condition. Therefore the proposed rational antidifference does not exist.

### 10.2 Exact scope

The theorem concerns a rational-function identity at fixed $N,b$. It does not exclude:

- identities shifting a parameter;
- higher-dimensional or matrix Green identities;
- source-specific identities outside this rational ansatz;
- finite interpolation of already known partial sums.

It gives no upper bound on $\nu$. A positive real residue is not a $29$-adic noncancellation theorem.

### 10.3 Correction: one residue condition is automatic here

For a polynomial $h$, the simple-pole coefficients of $h/D_N^2$ are


$$
a_{1,k}
=
\frac{h'(k)-2h(k)(\mathsf H_k-\mathsf H_{N-k})}
{k!^2(N-k)!^2}.
$$


The coefficient of $X^{-1}$ in the expansion at infinity equals


$$
\sum_{k=0}^Na_{1,k}.
$$



For the actual mixed defect,


$$
h=H_{\rm pol}(6G_{\rm pol}-29H_{\rm pol}),
$$


and


$$
\deg h\le2b+2<2N+1.
$$


Hence


$$
\frac{h(X)}{D_N(X)^2}=O(X^{-2}),
$$


so its $X^{-1}$-coefficient vanishes. Therefore


$$
\boxed{\sum_{k=0}^Na_{1,k}=0}
$$


automatically.

Thus, for these actual interpolation degrees, rational antidifference existence is equivalent to the single remaining condition


$$
\sum_{k=0}^N
\frac{h(k)}{k!^2(N-k)!^2}=0.
$$



This is a correction to the formulation of the test, not an evaluation of the original scalar. Its range $0\le k\le N$ is a pole-orbit range, not the original contraction range $0\le j\le b$. No original norm valuation or force-channel relation follows.

The separate Hahn/finite-Green investigation should not be duplicated by treating this residue criterion as its solution.

---

# Part III. Final normalization, finite evidence, and remaining obligations

## 11. All-prime primitive normalization remains indispensable

### 11.1 Endpoint weighted approximation

The actual least clearer and row contents remain


$$
D_8=\operatorname{lcm}_{0\le j\le3}
\bigl(\operatorname{den}(u_j),\operatorname{den}(v_j)\bigr),
$$




$$
g_j^{(8)}=\gcd(|D_8u_j|,|D_8v_j|).
$$


For nonzero endpoint first entries, put


$$
h_{\rm end}=\gcd(|\widetilde u_0|,|\widetilde u_3|),
$$




$$
\widetilde u_0=h_{\rm end}A_{\rm wt},
\qquad
\widetilde u_3=h_{\rm end}B_{\rm wt}.
$$


For a reduced weight $\lambda=a/k$, $k>0$, define


$$
J_{\rm wt}=B_{\rm wt}\widetilde v_0-A_{\rm wt}\widetilde v_3,
$$




$$
T_{\rm wt}=aJ_{\rm wt}+kA_{\rm wt}\widetilde v_3,
$$




$$
F_{\rm gcd}
=\gcd(|A_{\rm wt}|,|a|)
 \gcd(|B_{\rm wt}|,|a-k|),
$$




$$
G_{\rm wt}=\gcd(k,|J_{\rm wt}|),
$$




$$
H_{\rm gcd}
=\gcd\left(
h_{\rm end},
\frac{|T_{\rm wt}|}{F_{\rm gcd}G_{\rm wt}}
\right).
$$


Then the actual primitive fraction is


$$
q_\lambda=
\frac{kh_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
$$




$$
p_\lambda=
\operatorname{sgn}(A_{\rm wt}B_{\rm wt})
\frac{T_{\rm wt}}{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}}.
$$



All gcds are over all primes. The formula is the complete reduction of the denominator $kh_{\rm end}A_{\rm wt}B_{\rm wt}$: endpoint primitivity controls the factors supported on $A_{\rm wt}$ and $B_{\rm wt}$, $G_{\rm wt}$ accounts for the weight denominator, and the remaining cancellation is the displayed gcd with $h_{\rm end}$.

The required whole error is


$$
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda\left[
(e+\pi)
-\lambda\frac{\widetilde v_0}{\widetilde u_0}
-(1-\lambda)\frac{\widetilde v_3}{\widetilde u_3}
\right].
$$


The new endpoint formula (7.1) does not replace this final gcd or prove this expression nonzero.

### 11.2 Prime-$29$ approximation

Retain the actual integer columns $N_{B,1},N_{B,2}$, their actual contents, and their least simultaneous clearer $d_B$. Put


$$
\omega_j=\frac{(n+2)!}{(n+2-j)!},
\qquad
\Omega=\operatorname{diag}(\omega_0^2,\ldots,\omega_b^2),
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The actual all-prime normalization is


$$
g_B=\gcd(A_B,|H_B|),
\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$



Writing


$$
\operatorname{diag}(\omega_j)N_{B,i}=k_iv_i
$$


with $v_i$ primitive, and


$$
S=v_1^Tv_1,\qquad T=v_1^Tv_2,
$$


gives


$$
g_B=k_1\gcd(k_1S,|k_2T|).
$$


For every prime $\ell$,


$$
v_\ell(q_n)=
\max\{v_\ell(k_1)-v_\ell(k_2)+v_\ell(S)-v_\ell(T),0\}.
$$


The primitive multiplier remains $d_B^2/g_B$.

Neither division by $C_n$, division by the unit $\tau$, nor a rational interpolation denominator replaces this normalization.

At the same original index,


$$
\epsilon_n=p_n/q_n-(e+\pi),
\qquad
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$


Using the retained signed whole-error theorem,


$$
\log|\epsilon_n|
=-\lambda n+o(n),
\qquad
\lambda=\left(2+\frac1{2001}\right)\log(1+\sqrt2),
$$


with eventual nonzero error.

The outstanding comparison is therefore


$$
\log|q_n\epsilon_n|
=\log q_n-\lambda n+o(n).
$$


A saving $29^{O(c)}$, whose logarithm is $O(\log n)$, does not resolve this linear-scale comparison.

---

## 12. What the supplied finite receipts establish

### 12.1 Temporal receipt

The receipt concerns only


$$
n=225,\quad t=3375,\quad3377<p\le5000,
$$


with depth clipping at $4$. It reports 193 primes and zero alignment depth at every listed position.

A useful logical point is that a clipped depth equal to zero is an exact zero:


$$
\min(4,a)=0\quad\Longrightarrow\quad a=0.
$$


Thus, conditional on the reported modular calculations, the restricted endpoint inventory, acquisition, and loss products are exactly $1$, not merely unresolved depth-$4$ approximations.

This gives no information about other blocks, primes above $5000$, or the medium-prime loss. It supplies no acquisition lower bound.

### 12.2 Frame/source receipt

At $n=225$, the receipt reports:

- agreement of $D_8$ with the preserved actual clearer;
- agreement of actual row contents;
- three zero Plücker residuals;
- successful first- and second-level source checks at $229$ and $239$, covering both Legendre branches;
- no endpoint/full-frame discrepancy above $227$ at this index.

The first invariant factor has no prime factor above $227$. That does not identify its exact value or prove the quotient cyclic. The reported decimal lengths alone do not determine the invariant factors.

The absence of a discrepancy at this finite index is fully compatible with the omitted-column obstruction: the obstruction concerns the validity of an implication, not a claim that every index exhibits a discrepancy.

These closed finite calculations need not be repeated.

---

## 13. A bounded follow-on arithmetic certificate

No new computation is needed to prove the algebraic results in this report. A useful optional finite check would test the **new denominator transport**, not rerun the producer or the already checked frame identities.

### Inputs

Use only the preserved original $n=225$ data:

- $J,H,\mathbf C,F$;
- the actual primitive endpoint rows $r_0,r_3$;
- the preserved actual endpoint pairs $(\widetilde u_j,\widetilde v_j)$;
- the retained $\widehat R_j$ and $D_j$.

No source recurrence, companion calculation, or producer $3375$ is requested.

### Calculations

For $j=0,3$, compute


$$
R_j=r_jH,\quad C_j=r_j\mathbf C,\quad
g_j^*=\gcd(|R_j|,|C_j|),
$$




$$
\zeta_j=(C_j+E_{225}R_j)/g_j^*,
\qquad
\phi_j=\gcd(225!,|\zeta_j|).
$$


Then compute


$$
Q_j^{\rm new}
=\frac{|R_j|}{g_j^*}\frac{225!}{\phi_j}.
$$



Remove primes at most $227$ from the relevant positive integers and form


$$
S_j=\gcd(D_j,|C_j|)_{>227},
$$




$$
X_j=
\frac{(|\widetilde u_j|)_{>227}}
{(D_j)_{>227}/S_j}.
$$



### Expected verifiable output

The certificate should give the exact integers above and verify


$$
Q_j^{\rm new}=|\widetilde u_j|,
$$




$$
X_j\in\mathbb Z_{>0},
\qquad
X_j\mid F_{>227}.
$$


It should also report the exact residual factorial factor


$$
225!/\phi_j.
$$



Only dot products, gcds, exact divisions, and removal of primes at most $227$ are required. No unrestricted factorization is needed.

This would certify the new transport at one original index. It would not establish an infinite denominator estimate or any whole-error limit.

---

## 14. Proof ledger and exact remaining bottleneck

| Statement | Status |
|---|---|
| Actual-seed temporal primitivity above $t+2$ | Checked |
| Complete entrance expressions, including $F_k$ | Checked |
| Adjacent shared depth at most $1$, total at most $3$ | Checked |
| Bound on isolated terminal depth | Open |
| Polynomial payment transport and absence of payment primes above $N$ | Valid deduction from recovered theorem |
| Complete-source crossing modulo $p,p^2$, both branches | Checked |
| $D_8=|\det J|/d_{\rm one}$, invariant factors, quadratic divisibility | Checked for the actual corrected frame |
| Full-frame primitivity as an endpoint-content theorem | Invalid inference |
| Exact all-prime endpoint denominator formula (7.1) | **New, proved** |
| Actual large-prime endpoint denominator comparison (7.3) | **New, proved** |
| Prime-$29$ source recurrence and rank-three reduction | Old results, reused |
| $29^{2c+4}\le(n+2)^2$ | Checked, with retained terminal lower bound |
| Strong coordinate obstruction and finite square-sum test | Checked |
| Sharper candidate bound $r<29(M-w-\delta)$ | **New, proved** |
| Actual original index violating the strong target | Not established |
| Fixed-parameter rational norm antidifference | Proved impossible |
| Automatic simple-pole residue cancellation at actual degrees | **New correction, proved** |
| Bound for $\nu$ or complete scalar accepting value | Open |
| All-prime primitive denominator versus same-index whole error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

### Final status decision

The endpoint work now has a more exact connection between complete contact arithmetic and the actual primitive endpoint denominator:


$$
|\widetilde u_j|
=
\frac{|r_jH|}{\gcd(|r_jH|,|C_j|)}
\frac{n!}{
\gcd\!\left(
n!,
\left|\frac{C_j+E_nr_jH}{\gcd(|r_jH|,|C_j|)}\right|
\right)}.
$$


This retains the complete source and all factorial payments. Above $N$, the paid contact denominator determines the actual endpoint denominator up to a divisor of $F$.

What remains missing is an infinite-family estimate for the fixed-seed endpoint contact depths—including isolated entrances and primes beyond the physical crossing range—and its transport through all losses and the final weighted gcd.

For prime $29$, the remaining local obligation is an evaluated relation for the complete original norm and mixed contraction at the actual precision $a+2+\nu$, with the actual word, both initial charges, all interior forcing, both returns, and the physical terminal. The rational-antidifference obstruction neither supplies that relation nor bounds $\nu$. The actual weighted contents and the all-prime gcd must still be restored afterward.

Finally, either approximation route must establish


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0
$$


on the **same infinite original indices** carrying the arithmetic estimates. If $e+\pi=A/D$ were rational, every nonzero such integer linear form would have absolute value at least $1/D$. The displayed convergence would therefore prove irrationality.

No supplied finite certificate, and no theorem proved in this report, establishes that convergence.



$$
\boxed{\text{The unconditional rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


