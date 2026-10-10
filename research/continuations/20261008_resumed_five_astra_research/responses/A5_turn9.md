> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Dual boundary lifts and an evaluated intrinsic exception in the signed Chebyshev producer

## Abstract and proof status

The original index domain is unchanged:


$$
\mathcal N=\{N_u=9^{18+32u}:u\in\mathbb Z_{\ge0}\}.
$$


No auxiliary subsequence replaces this domain.

The requested aggregate estimate


$$
\mathfrak J_N^0:=\gcd(U_N,V_Ny_{K,N})
   \le e^{CN}U_N^{1-\delta_0},
\qquad \delta_0>0,
$$


is **not proved** here. Neither is its separated-prime mass sufficient condition. Consequently, this report proves neither retirement of the signed producer nor rationality or irrationality of $e+\pi$.

There are, however, two new proved results relevant to the proposed boundary-lift approach.

1. For the **original forced boundary**
   

$$
T_0^\pm=0,\qquad T_1^\pm=1,\qquad
   T_{j+1}^\pm=\pm4jT_j^\pm+T_{j-1}^\pm+2,
$$


   the two first-digit lift slopes satisfy the evaluated identity
   

$$
\boxed{
   H_a^-H_{a-1}^+ +H_{a-1}^-H_a^+\equiv-2\pmod p
   }
   \tag{A}
$$


   at every odd prime $p$ and every residue $a$. Thus the two boundary slope directions are always independent. A further uniform lifting congruence, proved below for $p\ge5$, controls the next digit at **every depth** without changing the boundary.

2. The complete intrinsic joint divisor has a genuine, exactly bounded original prime-$5$ exception:
   

$$
\boxed{
   v_5(\mathfrak J_{N_u}^0)=
   \begin{cases}
   1,&u\equiv21\pmod{25},\\
   0,&u\not\equiv21\pmod{25}.
   \end{cases}}
   \tag{B}
$$


   This uses the actual paid Gaussian coefficients, the complete source and exponential endpoint, and the actual reduced $K$-arc. On the exceptional branch,
   

$$
5\nmid 2g_B\Delta d_K,\qquad
   v_5(U)=1,\qquad 5\nmid V,\qquad 5\mid y_K.
$$


   In particular, exceptional joint cancellation occurs even at a prime where the Gaussian division, the source determinant, and the reduced arc denominator are all units.

The second theorem gives a concrete obstruction to turning the unit Wronskian (A), determinant nonvanishing, or “good-prime” status into generic coprimality. It also pays the full higher depth of this exception: no unproved extrapolation from a first digit is used.

The exact remaining issue is still **aggregate prime-power mass**, including primes larger than the moment range and high powers of primes dividing the Gaussian content or $\Delta$.

No tools have been used. A bounded exact-arithmetic receipt for the new calculations is specified at the end.

---

## 1. The unchanged producer and its complete primitive arithmetic

### 1.1 Source, Gaussian normalization, and actual content

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


where


$$
C_0=1,\quad C_1=2t-1,\quad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$



At an original index $N$, put


$$
d=a_Nb_{N-1}-a_{N-1}b_N,\qquad
B=b_{N-1}C_N-b_NC_{N-1}.
$$


The source functional is


$$
\eta(H)=\int_{-\infty}^1e^{t-1}H(t)\,dt.
$$


Its correctly signed coefficient formula is


$$
\boxed{
\eta(H)=\sum_{r\ge0}[x^r]H(1-x)\,r!.
}
\tag{1.1}
$$



Write


$$
\mathcal H(t)=t(1-t)(1+t^2)^2,\qquad
K=\mathcal H C_{N-3}^2,\qquad U=-\eta(K).
$$


The actual paid square normalization is


$$
g_B=\gcd(b_{N-1},b_N)>0,
$$




$$
\alpha=\frac{b_{N-1}}{g_B},\qquad
\beta=\frac{b_N}{g_B},\qquad
F=\alpha C_N-\beta C_{N-1},\qquad
\delta=\frac d{g_B}.
$$


Thus


$$
F(i)=F(-i)=\delta,\qquad \gcd(\alpha,\beta)=1.
$$



Retain


$$
V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
$$


The established content theorem is


$$
\boxed{
h=\operatorname{cont}(W_{\rm raw})=g_B^2c,
}
$$


where


$$
W_{\rm raw}=UB^2+\bigl(\eta(B^2)-d^2\bigr)K.
$$


Consequently,


$$
\tau=\frac Uc,\qquad \nu=\frac Vc,\qquad
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2.
\tag{1.2}
$$



The supplied proofs establish $U,V,M>0$ for $N\ge256$. Every original index satisfies this hypothesis.

### 1.2 Complete endpoints, both arcs, and both clearers

For an integer polynomial $H$, define


$$
E(H)=\sum_{r=0}^{\deg H}(-1)^rr![t^r]H.
$$


Keep


$$
E_F=E(F^2),\qquad E_K=E(K),
$$


and the complete monic-division arcs


$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$



The least simultaneous column clearer is


$$
D=\operatorname{lcm}\bigl(\operatorname{den}(R_F),
                         \operatorname{den}(R_K)\bigr),
$$


where both columns are reduced before taking denominators. Set


$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
\tag{1.3}
$$



Independently, reduce the single aggregate arc:


$$
\tau R_F+\nu R_K=\frac b\lambda,\qquad
\gcd(b,\lambda)=1,\quad\lambda>0.
$$


Then


$$
E=\tau E_F+\nu E_K,\qquad
A=\lambda E-b,\qquad G=\gcd(M,A),
$$


and the actual primitive pair is


$$
\boxed{
q=\frac{\lambda M}{G},\qquad p=\frac A G.
}
\tag{1.4}
$$


Here $\gcd(A,\lambda)=1$, so this is the reduction by the full, ALL-prime gcd.

The exact reconciliation is


$$
\tau X+\nu Y=\frac D\lambda A,
$$




$$
\boxed{
\gcd(D\tau\delta^2,\tau X+\nu Y)=\frac D\lambda G.
}
\tag{1.5}
$$


The raw-interface identity also remains


$$
\gcd(A_{\rm raw},B_{\rm raw})
=\frac{L_{\rm aff}h}{\lambda}G,\qquad
L_{\rm aff}=\operatorname{lcm}(1,\ldots,2N-1).
$$



The physical polynomial terminal is $2N$. Both monic arc quotients have degree at most $2N-2$, so integration denominators end at $2N-1$. In particular,


$$
D\mid L_{\rm aff},\qquad D<256^N.
\tag{1.6}
$$



### 1.3 Intrinsic $K$-column and the surviving denominator divisor

The already evaluated complete $K$-arc is


$$
R_K=\frac{A_K(x)}{30L(x)},\qquad x=4(N-3)^2,
$$


where


$$
L(x)=(x-1)(x-9)(x-25),
$$




$$
A_K(x)=13x^3-455x^2+3502x-5850.
\tag{1.7}
$$


Its actual reduction is


$$
g_{\rm arc}=\gcd(A_K(x),30L(x)),\qquad
a_K=\frac{A_K(x)}{g_{\rm arc}},\qquad
d_K=\frac{30L(x)}{g_{\rm arc}}.
$$


The proved fixed cancellation bound


$$
g_{\rm arc}\mid31\,806\,000
=2^4\,3^3\,5^3\,19\,31
\tag{1.8}
$$


is reused, not recalculated.

Define


$$
y_K=d_KE_K-a_K,\qquad \mu=\frac D{d_K}.
$$


Then


$$
Y=\mu y_K.
$$


For


$$
\mathfrak J^0=\gcd(U,Vy_K),\qquad
\mathfrak J=\gcd(U,VY),
$$


one has, prime by prime,


$$
\boxed{
\mathfrak J^0\mid\mathfrak J\mid\mu\mathfrak J^0.
}
\tag{1.9}
$$



The surviving-divisor theorem reaches the actual denominator:


$$
\frac{\tau}{\gcd(\tau,Y)}\mid q.
$$


Since $\gcd(\tau,\nu)=1$,


$$
\mathfrak J
=c\gcd(\tau,\nu Y)=c\gcd(\tau,Y).
$$


Therefore


$$
\boxed{\frac U{\mathfrak J}\mid q.}
\tag{1.10}
$$


No prime dividing $D,\delta,g_B$, or $\Delta$ is removed from this identity.

### 1.4 The same positive whole error

The rational polynomial is


$$
P=\frac{F^2+(V/U)K}{\delta^2}.
$$


At every original index,


$$
\epsilon_N=
\int_0^1P(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0,
$$


and


$$
\boxed{q_N(e+\pi)-p_N=q_N\epsilon_N>0.}
\tag{1.11}
$$



The supplied analytic proofs give


$$
\epsilon_N\asymp R^{-2N},\qquad
R=1+\sqrt2+\sqrt{2+2\sqrt2},
$$


and


$$
\log U_N=2N\log N+O(N).
\tag{1.12}
$$


Their hypotheses hold throughout the original domain.

For completeness, the whole rational enclosure remains


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


and, with $m=N-3$, $j_r=(1-4r^2)^{-1}=j_{-r}$,


$$
J_K=\frac{61}{420}
+\frac{
916j_m-399(j_{m+1}+j_{m-1})
-58(j_{m+2}+j_{m-2})
-(j_{m+3}+j_{m-3})
}{8192}.
$$


Thus


$$
\boxed{
q_NJ_N=\frac{\lambda_N}{G_N}
       (\tau_NJ_F+\nu_NJ_K).
}
\tag{1.13}
$$


Both positive summands remain present.

The audited critical estimate


$$
\log c_N\le N\log N+O(N)
\tag{1.14}
$$


and the critical-scale Bessel/midpoint analysis are reused. They are not rederived as new progress.

---

## 2. Complete forced source and endpoint coordinates

Put $n=2N$. The integral coordinates are


$$
S_j=\eta(C_j)=1-2j\Theta_j,
\qquad
\mathcal E_j=E(C_j)=(-1)^j-2j\Phi_j,
$$


with


$$
\Theta_0=\Phi_0=0,\qquad \Theta_1=\Phi_1=1,
$$


and


$$
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2,
\tag{2.1}
$$




$$
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j.
\tag{2.2}
$$


In particular, $\Theta_2=-2$ and $\Phi_2=-6$. These are integral recurrences, including their original boundaries.

### 2.1 Fixed thirteen-weight evaluator

Retain


$$
(w_0,\ldots,w_{12})
=(1,8,58,168,399,-176,-916,-176,399,168,58,8,1).
$$


Define


$$
r_0=1,\ s_0=0,\qquad r_1=0,\ s_1=1,
$$




$$
r_{k+1}=r_{k-1}+4(n-k)r_k,\qquad
s_{k+1}=s_{k-1}+4(n-k)s_k,
$$


and


$$
\kappa_0=\kappa_1=\omega_0=\omega_1=0,
$$




$$
\kappa_{k+1}=\kappa_{k-1}+4(n-k)\kappa_k-2,
$$




$$
\omega_{k+1}=\omega_{k-1}+4(n-k)\omega_k-2(-1)^k,
\qquad 1\le k\le11.
\tag{2.3}
$$



Set


$$
\mathsf A=\sum_{k=0}^{12}w_k(n-k)r_k,\qquad
\mathsf B=\sum_{k=0}^{12}w_k(n-k)s_k,
$$




$$
\mathsf C_U=679936-\sum_{k=0}^{12}w_k(n-k)\kappa_k,
$$




$$
\mathsf C_E=-1\,849\,344+
\sum_{k=0}^{12}w_k(n-k)\omega_k.
$$


The complete source and $K$-endpoint planes are


$$
4096U=\mathsf C_U-\mathsf A\Theta_n-\mathsf B\Theta_{n-1},
\tag{2.4}
$$




$$
4096E_K=\mathsf A\Phi_n+\mathsf B\Phi_{n-1}+\mathsf C_E.
\tag{2.5}
$$



For the actual paid square column, put


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
\mathsf C_F^E=\alpha^2+(5-2n)\beta^2+4\alpha\beta.
$$


Then


$$
V=\mathsf C_V-\mathsf P\Theta_n-\mathsf Q\Theta_{n-1},
\tag{2.6}
$$




$$
E_F=\mathsf C_F^E-\mathsf P\Phi_n-\mathsf Q\Phi_{n-1}.
\tag{2.7}
$$


In particular, $-\delta^2$, the endpoint $4\alpha\beta$, and the different source and endpoint constants are retained.

### 2.2 Both complete arc returns

The square arc remains evaluated by


$$
R_j(t)=\frac{C_j(t)-a_j-b_jt}{1+t^2},\qquad
\xi_j=4\int_0^1R_j,\qquad
\upsilon_j=4\int_0^1tR_j.
$$


The initial values at $j=0,1$ are zero, and


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
(1-j^2)^{-1},&j\text{ even}.
\end{cases}
$$


Thus


$$
R_F=\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
                  -2\alpha\beta\xi_{n-1}}2.
\tag{2.8}
$$


The odd singular index is not substituted into the even formula.

### 2.3 Integer returns and the limitation of their determinant

Let


$$
\Delta=\mathsf A\mathsf Q-\mathsf B\mathsf P.
$$


The established determinant theorem gives $\Delta<0$ on the present scope.

The source return has terminal values


$$
z_n=4096\mathsf Q U-\mathsf B V,\qquad
z_{n-1}=\mathsf A V-4096\mathsf P U,
$$


and


$$
z_j=-\Delta\Theta_j+r_j,
$$


with


$$
z_{j-1}=z_{j+1}+4jz_j,\qquad
r_{j-1}=r_{j+1}+4jr_j-2\Delta.
\tag{2.9}
$$


Here


$$
r_n=\mathsf Q\mathsf C_U-\mathsf B\mathsf C_V,\qquad
r_{n-1}=\mathsf A\mathsf C_V-\mathsf P\mathsf C_U.
$$



For the complete endpoint pair, put


$$
k_E=D\mathsf C_E-4096DR_K,\qquad
f_E=D\mathsf C_F^E-DR_F,
$$




$$
w_n=4096\mathsf QY+\mathsf B X,\qquad
w_{n-1}=-4096\mathsf PY-\mathsf A X.
$$


Then


$$
w_j=D\Delta\Phi_j+\sigma_j,
$$


where


$$
\sigma_n=\mathsf Qk_E+\mathsf Bf_E,\qquad
\sigma_{n-1}=-\mathsf Pk_E-\mathsf Af_E,
$$


and


$$
w_{j-1}=w_{j+1}+4jw_j,\qquad
\sigma_{j-1}
=\sigma_{j+1}+4j\sigma_j+2D\Delta(-1)^j.
\tag{2.10}
$$


All these identities are integral, including at primes dividing $2\Delta$.

The joint determinant is still


$$
\boxed{
z_nw_{n-1}-z_{n-1}w_n
=-4096\Delta(UX+VY).
}
\tag{2.11}
$$


It is not a separate small-height certificate for the selected gcd.

---

## 3. New theorem: the two original-boundary lift slopes

Define, for an integer parameter $c$,


$$
T_0(c)=0,\qquad T_1(c)=1,\qquad
T_{j+1}(c)=cjT_j(c)+T_{j-1}(c)+2.
$$


Then


$$
T_j^-=T_j(-4)=\Theta_j,\qquad
T_j^+=T_j(4)=(-1)^{j-1}\Phi_j.
$$



The exact boundary-specific formula is


$$
\boxed{
T_j(c)=\sum_{r=0}^{j-1}c^rr!\binom{j+r}{2r+1}.
}
\tag{3.1}
$$


It follows from the classical second-kind coefficient formula, or directly by substituting into the recurrence and checking $T_0,T_1$.

### 3.1 Explicit slope polynomials

Let $p$ be odd. Modulo $p$, terms with $r\ge p$ vanish. For $j=a+p\ell$,


$$
(1+z)^{a+p\ell+r}
\equiv(1+z)^{a+r}(1+\ell z^p)
\pmod{p,z^{2p}}.
$$


Therefore


$$
T_{a+p\ell}(c)\equiv T_a(c)+\ell H_a(c)\pmod p,
\tag{3.2}
$$


where


$$
\boxed{
H_a(c)=
\sum_{r=(p-1)/2}^{p-1}
c^rr!\binom{a+r}{2r+1-p}\pmod p.
}
\tag{3.3}
$$



This is an explicit polynomial function of the residue $a$. To expose its structure, put $h=(p-1)/2$. In $\mathbb F_p[a]$,


$$
\boxed{
H_a(c)=
\sum_{s=0}^{h}
\frac{c^{h+s}(h+s)!}{(2s)!}
\prod_{j=1}^{s}\left(a^2-\left(j-\frac12\right)^2\right).
}
\tag{3.4}
$$


Every denominator in (3.4) is a $p$-adic unit. If $c\not\equiv0\pmod p$, this is an even monic polynomial of degree $p-1$.

For the two boundaries, write


$$
H_a^\pm=H_a(\pm4).
$$



### 3.2 An evaluated dual Wronskian

The following is stronger than merely knowing that each slope satisfies a homogeneous recurrence.

### Theorem 3.1 — Original-boundary dual slope identity

For every odd prime $p$ and every integer $a$,


$$
\boxed{
H_a^-H_{a-1}^+ +H_{a-1}^-H_a^+\equiv-2\pmod p.
}
\tag{3.5}
$$



#### Proof

First,


$$
H_0(c)=T_p(c),\qquad
H_1(c)=T_{p+1}(c)-1\equiv T_{p-1}(c)+1\pmod p.
\tag{3.6}
$$



Let


$$
Q_j(c)=T_{j+1}(c)T_j(-c)+T_{j+1}(-c)T_j(c).
$$


The opposite signs of $cj$ cancel, while both forcing terms remain:


$$
Q_j(c)-Q_{j-1}(c)=2\bigl(T_j(c)+T_j(-c)\bigr).
$$


Since $Q_0(c)=0$,


$$
\begin{aligned}
&H_0(c)H_1(-c)+H_0(-c)H_1(c)\\
&\qquad\equiv
2\sum_{j=1}^{p-1}\bigl(T_j(c)+T_j(-c)\bigr)
+T_p(c)+T_p(-c)\pmod p.
\end{aligned}
\tag{3.7}
$$



We evaluate the right side, rather than leave it as an unevaluated sum. The hockey-stick identity and (3.1) give


$$
\sum_{j=1}^{p-1}T_j(c)
=\sum_{r=0}^{p-2}c^rr!\binom{p+r}{2r+2}.
$$


For $h\le r\le p-2$, put $k=2r+1-p$. Lucas reduction gives


$$
2\binom{p+r}{2r+2}+\binom{p+r}{2r+1}
\equiv
2\binom r{k+1}+\binom rk.
$$


But


$$
2\binom r{k+1}+\binom rk
=\binom rk\frac{2r-k+1}{k+1}
=\binom rk\frac p{k+1}\equiv0\pmod p.
$$


For $r<h$, both relevant binomial coefficients vanish modulo $p$. The sole surviving coefficient is $r=p-1$, from $T_p(c)+T_p(-c)$. Since $p-1$ is even, Wilson's theorem gives


$$
2c^{p-1}(p-1)!\equiv-2c^{p-1}\pmod p.
$$


Thus, for $c\ne0$,


$$
H_0(c)H_1(-c)+H_0(-c)H_1(c)\equiv-2.
\tag{3.8}
$$



Finally, the slope recurrences are homogeneous:


$$
H_{a+1}^\pm=\pm4aH_a^\pm+H_{a-1}^\pm.
$$


They make


$$
H_a^-H_{a-1}^++H_{a-1}^-H_a^+
$$


independent of $a$. Equation (3.8), with $c=4$, proves (3.5). ∎

The original boundary and the forcing $2$ are essential in the evaluation (3.7). This theorem is not a statement about arbitrary initial states.

### 3.3 A uniform next-digit lift at every depth

The first-digit formula does not by itself authorize higher-depth freezing. The following congruence supplies a valid higher-depth statement for these two boundary sequences.

### Theorem 3.2 — Uniform boundary lift congruence

Let $p\ge5$ be prime, $k\ge1$, and $j,t\ge0$. Then


$$
\boxed{
T_{j+p^kt}(c)-T_j(c)
\equiv p^{k-1}t\,H_{j\bmod p}(c)\pmod{p^k}.
}
\tag{3.9}
$$



#### Proof

Use Vandermonde in (3.1):


$$
\binom{j+r+p^kt}{2r+1}-\binom{j+r}{2r+1}
=
\sum_{s=1}^{2r+1}
\binom{p^kt}{s}\binom{j+r}{2r+1-s}.
$$


The elementary identity


$$
\binom{p^kt}{s}=\frac{p^kt}{s}\binom{p^kt-1}{s-1}
$$


gives


$$
v_p\binom{p^kt}{s}\ge k-v_p(s).
\tag{3.10}
$$



For $r\ge p$ and $p\ge5$,


$$
v_p(r!)\ge\lfloor\log_p(2r+1)\rfloor.
\tag{3.11}
$$


Indeed, if $ap\le r<(a+1)p$, then $v_p(r!)\ge a$, while
$p^{a+1}>2r+1$, using $p^a\ge2(a+1)$.
Hence every $r\ge p$ contribution is divisible by $p^k$.

For $r<p$, the only $s\le2r+1<2p$ that can contribute modulo $p^k$ is $s=p$. Moreover,


$$
\binom{p^kt}{p}\equiv p^{k-1}t\pmod{p^k}.
$$


The remaining sum is precisely (3.3). ∎

The restriction $p\ge5$ is genuine in this proof; inequality (3.11) need not hold at $p=3$.

For the actual $K$-source, suppose two retained even terminals satisfy


$$
n'-n=p^kt.
$$


The fixed integer coefficient polynomials in Section 2 agree modulo $p^k$. Therefore


$$
4096(U_{N'}-U_N)
\equiv p^{k-1}t\,u_1\pmod{p^k},
\tag{3.12}
$$


and


$$
4096(E_{K,N'}-E_{K,N})
\equiv p^{k-1}t\,e_1\pmod{p^k},
\tag{3.13}
$$


with $u_1,e_1$ defined below.

For the unreduced but completely paid arc numerator


$$
\widehat y_K=30L(x)E_K-A_K(x)=g_{\rm arc}y_K,
$$


the corresponding congruence is


$$
4096(\widehat y_{K,N'}-\widehat y_{K,N})
\equiv
p^{k-1}t\,30L(x)e_1\pmod{p^k}.
\tag{3.14}
$$


The fixed factor $g_{\rm arc}$ must still be paid when passing to $y_K$.

No analogous congruence for $V$ with frozen $\alpha,\beta,\delta$ is asserted. Their actual Gaussian changes must be evaluated separately.

---

## 4. Consequences for the two separation minors—and what they do not prove

Fix an original $N$ and an odd prime $p$, and write


$$
n=a+p\ell,\qquad 1\le a\le p.
$$


At the actual even terminal,


$$
\Theta_n=T_a^-+\ell H_a^-,
\quad
\Theta_{n-1}=T_{a-1}^-+\ell H_{a-1}^-,
$$




$$
\Phi_n=-T_a^+-\ell H_a^+,
\quad
\Phi_{n-1}=T_{a-1}^++\ell H_{a-1}^+
\pmod p.
$$



Using the actual paid coefficients at this $N$, define


$$
u_0=\mathsf C_U-\mathsf A T_a^--\mathsf B T_{a-1}^-,
\qquad
u_1=-\mathsf A H_a^--\mathsf B H_{a-1}^-,
$$




$$
v_0=\mathsf C_V-\mathsf P T_a^--\mathsf Q T_{a-1}^-,
\qquad
v_1=-\mathsf P H_a^--\mathsf Q H_{a-1}^-,
$$




$$
e_0=\mathsf C_E-\mathsf A T_a^++\mathsf B T_{a-1}^+,
\qquad
e_1=-\mathsf A H_a^++\mathsf B H_{a-1}^+.
$$


Then


$$
4096U=u_0+\ell u_1,\qquad
V=v_0+\ell v_1,\qquad
4096E_K=e_0+\ell e_1\pmod p.
$$



For the complete reduced $K$-column, put


$$
y_0=d_Ke_0-4096a_K,\qquad y_1=d_Ke_1.
$$


The two original minors are


$$
\mathfrak m_V=u_0v_1-u_1v_0,\qquad
\mathfrak m_K=u_0y_1-u_1y_0.
\tag{4.1}
$$



If both are nonzero, then $p\nmid\mathfrak J^0$, excluding **every depth** at that prime.

### 4.1 The evaluated rank consequence

Put


$$
x_-=H_a^-,\quad y_-=H_{a-1}^-,
\quad x_+=H_a^+,\quad y_+=H_{a-1}^+.
$$


The transformation


$$
\binom{u_1}{e_1}
=
\begin{pmatrix}
-x_-&-y_-\\
-x_+&y_+
\end{pmatrix}
\binom{\mathsf A}{\mathsf B}
$$


has determinant $2$, by Theorem 3.1. Hence


$$
\boxed{
u_1=e_1=0\quad\Longleftrightarrow\quad
\mathsf A=\mathsf B=0\pmod p.
}
\tag{4.2}
$$



The square endpoint slope, with its actual sign, is


$$
f_1=\mathsf P H_a^+-\mathsf QH_{a-1}^+.
$$


A direct expansion gives the further evaluated identity


$$
\boxed{
u_1f_1+e_1v_1=-2\Delta\pmod p.
}
\tag{4.3}
$$


There is no inversion of $\Delta$.

These identities prove that the two boundary lift directions cannot collapse simultaneously except through an actual collapse of the selected coefficient row. They do **not** imply that the affine source and endpoint zero sets are disjoint. The following original exception demonstrates this distinction.

---

## 5. A fully evaluated original prime-$5$ exception

### 5.1 Original index residues and actual Gaussian units

All original indices satisfy


$$
N\equiv9\pmod{12}.
\tag{5.1}
$$


In $\mathbb F_5$, the two images of $i$ are $2$ and $-2$.

At $i=2$, the recurrence is


$$
C_{j+1}=C_j-C_{j-1},\qquad C_0=1,\ C_1=3,
$$


with period $6$:


$$
1,3,2,4,2,3,1,3,\ldots.
$$


At $i=-2$, it is


$$
C_{j+1}=-C_{j-1},\qquad C_0=1,\ C_1=0,
$$


with period $4$:


$$
1,0,4,0,1,0,\ldots.
$$



Using (5.1),


$$
\boxed{
(a_N,b_N,a_{N-1},b_{N-1})
\equiv(2,1,4,4)\pmod5.
}
\tag{5.2}
$$


In particular,


$$
5\nmid g_B,
$$


and the actual paid coefficients satisfy


$$
g_B\alpha\equiv4,\qquad
g_B\beta\equiv1,\qquad
g_B\delta\equiv4\pmod5.
\tag{5.3}
$$


These are proved Gaussian residues on the original domain. No higher-precision Gaussian freezing is used.

Also,


$$
9^2=81\equiv1+5\pmod{25},
$$


so


$$
\boxed{N_u\equiv21+5u\pmod{25}.}
\tag{5.4}
$$


Thus, writing $n=2+5\ell$,


$$
\ell\equiv3+2u\pmod5.
\tag{5.5}
$$



### 5.2 Both boundary slopes and the complete local rows

For $p=5$, the recurrences through $j=6$ give


$$
(T_j^-)_{j=0}^6\equiv(0,1,3,4,2,4,4),
$$




$$
(T_j^+)_{j=0}^6\equiv(0,1,1,1,0,3,2).
$$


Therefore, at the actual residue $a=2$,


$$
\boxed{
(H_2^-,H_1^-,H_2^+,H_1^+)
\equiv(2,3,2,1)\pmod5.
}
\tag{5.6}
$$


Their dual Wronskian is $2\cdot1+3\cdot2=8\equiv-2$, as required.

Evaluating the complete fixed twelve-step recurrences at $n=2\pmod5$ gives


$$
\boxed{
(\mathsf A,\mathsf B,\mathsf C_U,\mathsf C_E)
\equiv(4,0,2,3)\pmod5.
}
\tag{5.7}
$$


This evaluation includes both $-2$ and $-2(-1)^k$ forcing terms.

For an explicit short check, the weighted row is


$$
\bigl(w_k(n-k)\bigr)_{k=0}^{12}
\equiv(2,3,0,2,2,3,4,0,1,4,1,3,0).
$$


Its inner products with $r,s,\kappa,\omega$ are respectively


$$
4,\quad0,\quad4,\quad2.
$$


Since $679936\equiv1$ and $-1\,849\,344\equiv1\pmod5$, these yield (5.7).

Now


$$
\Theta_n=3+2\ell,\qquad
\Theta_{n-1}=1+3\ell,
$$




$$
\Phi_n=-1-2\ell,\qquad
\Phi_{n-1}=1+\ell\pmod5.
$$


As $4096\equiv1\pmod5$, equations (2.4)–(2.5) give


$$
U\equiv2\ell,\qquad E_K\equiv4+2\ell.
$$


Using (5.5),


$$
\boxed{
U_{N_u}\equiv1-u,\qquad E_{K,N_u}\equiv4u\pmod5.
}
\tag{5.8}
$$



For the paid square column, equations (5.3) and $n\equiv2$ give


$$
g_B^2\mathsf P\equiv2,\qquad
g_B^2\mathsf Q\equiv2,\qquad
g_B^2\mathsf C_V\equiv1.
$$


Consequently,


$$
g_B^2V
\equiv1-2(3+2\ell)-2(1+3\ell)\equiv3.
$$


Thus


$$
\boxed{g_B^2V\equiv3\pmod5,\qquad 5\nmid V}
\tag{5.9}
$$


for every original index.

The source first-digit coefficients are therefore


$$
(u_0,u_1)=(0,2),\qquad
(v_0,v_1)=\left(\frac3{g_B^2},0\right),
$$


and


$$
(e_0,e_1)=(4,2)\pmod5.
\tag{5.10}
$$



### 5.3 The complete arc reduction at $5$

The arc cannot be omitted. From (5.4),


$$
x=4(N-3)^2\equiv21+20u\pmod{25}.
$$


Since $x\equiv1\pmod5$, only $x-1$ among the three factors of $L(x)$ is divisible by $5$. Write


$$
s=v_5(L(x))=v_5(n-7)\ge1.
$$



Use the exact identity


$$
A_K(x)=13L(x)+45(3x-65).
\tag{5.11}
$$


If $u\not\equiv1\pmod5$, one obtains $v_5(A_K)=1$, and hence


$$
v_5(d_K)=s.
$$


If $u\equiv1\pmod5$, then $s=1$, $v_5(A_K)\ge2$, and the two powers of $5$ in $30L(x)$ cancel completely. Thus


$$
\boxed{
v_5(d_K)=
\begin{cases}
0,&u\equiv1\pmod5,\\
v_5(n-7),&u\not\equiv1\pmod5.
\end{cases}}
\tag{5.12}
$$



For verification of the exceptional cancellation, when $s=1$,


$$
\frac{A_K(x)}5\equiv1+4u\pmod5.
$$


Its zero class is exactly $u\equiv1\pmod5$. When $u\equiv4\pmod5$, one has $s\ge2$ and the second term in (5.11) still has valuation exactly $1$.

Now write


$$
u=1+5t.
$$


Then


$$
N=81^{25+80t}\equiv1+25t\pmod{125},
\tag{5.13}
$$


because the quadratic binomial term is divisible by $125$ for this exponent. Hence


$$
x\equiv16-25t\pmod{125}.
$$


The needed exact cubic data are


$$
L(16)=-945,\qquad A_K(16)=-13050,\qquad A_K'(16)=-1074.
$$


It follows that


$$
\frac{30L(x)}{25}\equiv1\pmod5,\qquad
\frac{A_K(x)}{25}\equiv3+4t\pmod5.
$$


After the actual reduction, $d_K$ is a unit and


$$
\boxed{
R_K=\frac{a_K}{d_K}\equiv3+4t\pmod5
\qquad(u=1+5t).
}
\tag{5.14}
$$



On this branch, $E_K\equiv4$, so


$$
\boxed{
y_K=d_K(E_K-R_K)
\equiv d_K(1+t)\pmod5.
}
\tag{5.15}
$$


Therefore


$$
5\mid y_K
\quad\Longleftrightarrow\quad
u\equiv21\pmod{25}
$$


among the original indices with $5\mid U$.

### 5.4 Paying the higher depth: $U$ modulo $25$

First-digit vanishing of $y_K$ does not alone bound $v_5(\mathfrak J^0)$. We now evaluate the needed source depth uniformly.

On $u=1+5t$, equation (5.13) gives


$$
m=N-3\equiv-2+25t\pmod{125}.
$$


This is a residue evaluation of the exact coefficient polynomials in $m$. It does not introduce a negative producer index or change the physical degree $2N$.

The first coefficients of $C_m(1-x)$ are


$$
d_1=-2m^2,\qquad
d_2=\frac23m^2(m^2-1),
$$




$$
d_3=-\frac4{45}m^2(m^2-1)(m^2-4).
\tag{5.16}
$$


At this residue, the division by $5$ in $d_3$ is paid by $m^2-4$. Modulo $25$,


$$
d_1\equiv-8,\qquad d_2\equiv8,\qquad d_3\equiv15t.
\tag{5.17}
$$



Only source moments through degree $9$ matter modulo $25$, because


$$
25\mid r!\qquad(r\ge10).
$$


For moments of degree $5,\ldots,9$, coefficients are needed only modulo $5$. Those coefficients are unchanged when $m$ changes by $25$. One way to verify this without unpaid factorial divisions is the integer-binomial formula


$$
[x^r]C_m(1-x)
=\frac{(-4)^r}{2}
\left\{
\binom{m+r}{2r}+\binom{m+r-1}{2r}
\right\}
\quad(r\ge1).
\tag{5.18}
$$


For the required $r\le8$, $2r<25$, and Vandermonde with
$(1+z)^{25}\equiv1+z^{25}\pmod5$ proves the stated period.

At the base residue $m^2=4$,


$$
C_2(1-x)^2=1-16x+80x^2-128x^3+64x^4.
$$


Using


$$
\mathcal H(1-x)
=4x-12x^2+16x^3-12x^4+5x^5-x^6,
$$


their product has coefficient vector


$$
(0,4,-76,528,-1740,3269,-3857,2976,-1488,448,-64).
$$


Positive factorial weighting gives


$$
\eta(\mathcal H C_2^2)\equiv20\pmod{25}.
\tag{5.19}
$$



The variation $d_3\equiv15t$ changes the $x^3$-coefficient of $C_m(1-x)^2$ by $5t\pmod{25}$. It therefore changes the $x^4$-coefficient of $\mathcal H(1-x)C_m(1-x)^2$ by $20t$, whose weighted contribution is


$$
4!\cdot20t\equiv5t\pmod{25}.
$$


All other changes have already been shown irrelevant modulo $25$. Since $U=-\eta(K)$,


$$
\boxed{
U_{N_{1+5t}}\equiv5(1-t)\pmod{25}.
}
\tag{5.20}
$$



In particular, if $t\equiv4\pmod5$, then


$$
U\equiv10\pmod{25},\qquad v_5(U)=1.
\tag{5.21}
$$



### Theorem 5.1 — Exact intrinsic prime-$5$ cancellation

For every original $u\ge0$,


$$
\boxed{
v_5\gcd(U_{N_u},V_{N_u}y_{K,N_u})
=
\begin{cases}
1,&u\equiv21\pmod{25},\\
0,&u\not\equiv21\pmod{25}.
\end{cases}}
$$



#### Proof

If $u\not\equiv1\pmod5$, equation (5.8) makes $U$ a unit.

If $u=1+5t$, equation (5.9) makes $V$ a unit, and (5.15) shows that $y_K$ is divisible by $5$ exactly when $t\equiv4\pmod5$. On that branch, (5.21) gives $v_5(U)=1$. Thus the joint gcd has valuation exactly $1$, independently of any larger valuation of $y_K$. ∎

### 5.5 Both actual minors, fully evaluated

From (5.10),


$$
\boxed{\mathfrak m_V\equiv\frac4{g_B^2}\ne0\pmod5.}
\tag{5.22}
$$



If $u\not\equiv1\pmod5$, then $5\mid d_K$ and $5\nmid a_K$, so


$$
\boxed{\mathfrak m_K\equiv2a_K\ne0\pmod5.}
$$


If $u=1+5t$, then $d_K$ is a unit and


$$
\boxed{
\mathfrak m_K\equiv3d_K(1+t)\pmod5.
}
\tag{5.23}
$$


Hence its vanishing is exactly the original class $u\equiv21\pmod{25}$.

Moreover,


$$
g_B^2\Delta
\equiv4\cdot2-0\cdot2\equiv3\pmod5.
$$


Thus the exception satisfies


$$
5\nmid2g_B\Delta d_K.
$$


It is a genuine complete-endpoint exception at a good determinant prime—not a Gaussian-content artifact or a modular pole discarded from the calculation.

---

## 6. Effect on the actual joint divisor and remaining prime branches

### 6.1 Excess clearing remains paid

At the exceptional class $u\equiv21\pmod{25}$, $v_5(U)=1$ and $5\mid y_K$, so


$$
v_5(\mathfrak J)=1
$$


regardless of $\mu$.

At $u\equiv1\pmod5$, but $u\not\equiv21\pmod{25}$, both $V$ and $y_K$ are units. Hence


$$
v_5(\mathfrak J)=\min\{v_5(U),v_5(\mu)\}.
$$


Together,


$$
\boxed{
v_5(\mathfrak J)=
\begin{cases}
0,&u\not\equiv1\pmod5,\\
1,&u\equiv21\pmod{25},\\
\min\{v_5(U),v_5(\mu)\},
 &u\equiv1\pmod5,\ u\not\equiv21\pmod{25}.
\end{cases}}
\tag{6.1}
$$


These are statements about the complete $Y=\mu y_K$. They do not replace $D$ by $d_K$, nor replace the final $G$ by a selected-prime gcd.

### 6.2 Binary and prime-$3$ payments

The original $m=N-3$ is even. The established coefficient congruence


$$
C_{2j}\equiv1\pmod8
$$


gives $C_m^2\equiv1\pmod{16}$. Since $\eta(\mathcal H)=-332$,


$$
U\equiv332\equiv12\pmod{16},
\qquad v_2(U)=2.
$$



At odd $N$, the Gaussian congruences give $v_2(g_B)=1$, $\alpha\equiv0\pmod4$, and $\beta,\delta$ odd. Consequently,


$$
F^2\equiv1\pmod8,\qquad \delta^2\equiv1\pmod8,
$$


so $8\mid V$. Therefore


$$
\boxed{v_2(\mathfrak J^0)=v_2(\mathfrak J)=2.}
\tag{6.2}
$$



Also $3\mid m$. Modulo $3$, only the first two source moments can contribute. From (1.1) and the coefficient of $x$ in $\mathcal H(1-x)$,


$$
U\equiv-4\equiv2\pmod3.
$$


Thus


$$
\boxed{3\nmid\mathfrak J^0\mathfrak J.}
\tag{6.3}
$$



The already proved prime-$17$ theorem is reused at its stated scope:


$$
17\nmid\mathfrak J^0.
$$


Its complete-$Y$ excess-clearing formula remains unchanged. No prime-$17$ arithmetic has been repeated.

Consequently,


$$
\boxed{
\mathfrak J_N^0
=4\cdot5^{\mathbf 1_{u\equiv21\ (25)}}\,
\mathfrak J_{N,\mathrm{rem}},
\qquad
\gcd(\mathfrak J_{N,\mathrm{rem}},2\cdot3\cdot5\cdot17)=1.
}
\tag{6.4}
$$



### 6.3 What is still not paid

Equation (6.4) is an exact narrowing, not a positive-proportion mass estimate.

In particular:

* The unit Wronskian does not make the affine minors nonzero.
* A simple source lift root can continue to arbitrarily high precision; uniqueness of its lift does not bound how closely an original $N_u$ meets it.
* Gaussian data at other primes must be lifted with the actual division by $g_B$. The proof at $5$ used only a proved original-domain residue modulo $5$.
* A bound $|\Delta|\le e^{O(N)}$ controls the size of $\Delta$, but does not by itself control all powers of primes dividing $\Delta$ that may divide $U$.
* The same distinction applies to the support of $g_B$.
* Primes $p>2N$ are not absent from $U$. The boundary formulas remain valid there, but no bound for their aggregate exceptional product has been proved.
* The joint-transfer determinant (2.11) still has the complete numerator $UX+VY$ on its right side. It does not supply the missing smaller certificate.

These are the precise obstructions to completing the primary target by the present argument.

---

## 7. A concrete remaining lemma and its exact conditional implication

The separated-prime mass lemma from the preceding report remains a valid sufficient target:


$$
\log\mathcal S_N\ge\delta_0\log U_N-CN,
$$


where $\mathcal S_N$ uses both actual nonzero minors.

The new prime-$5$ evaluation determines its $5$-part exactly:


$$
v_5(\mathcal S_N)=
\begin{cases}
v_5(U_N),&u\equiv1\pmod5,\ u\not\equiv21\pmod{25},\\
0,&\text{otherwise}.
\end{cases}
$$


This finite-prime information does not prove positive total mass.

A more explicit alternative follow-on obligation is the following factorial-excess statement.

> **Paid factorial-excess lemma — open.**  
> For the unchanged original objects, prove that
> 

$$
> \boxed{
> \prod_{p\notin\{2,3,5,17\}}
> p^{\max\{0,\,
> \min(v_p(U_N),v_p(V_N)+v_p(y_{K,N}))
> -v_p(N!)\}}
> \le e^{CN}
> }
> \tag{7.1}
>
$$


> with a fixed $C$, for every sufficiently large original $N$.

This is proposed as a definite outstanding lemma, not as a result obtained by naming another product. It asks for actual depth control beyond the $N!$ allowance. For every $p>N$, the factorial allowance is zero, so the lemma explicitly includes the large-prime obligation.

If (7.1) were proved, (6.4) would imply


$$
\mathfrak J_N^0\le20\,N!\,e^{CN}
=e^{O(N)}U_N^{1/2}.
$$


This would give a strict joint saving with $\delta_0=1/2$.

More generally, suppose the requested bound


$$
\mathfrak J_N^0\le e^{CN}U_N^{1-\delta_0}
\tag{7.2}
$$


were established. Then (1.6), (1.9), and (1.10) yield


$$
q_N\ge\frac{U_N}{\mathfrak J_N}
\ge e^{-C'N}U_N^{\delta_0}.
$$


Using the same positive whole error,


$$
\log(q_N\epsilon_N)
\ge2\delta_0N\log N-O(N)\longrightarrow+\infty.
$$


Therefore


$$
\boxed{q_N\epsilon_N\longrightarrow\infty
\qquad(N\in\mathcal N).}
\tag{7.3}
$$



This conditional deduction uses the actual


$$
q_N=\lambda_NM_N/G_N,
$$


not an unreduced or partially reduced denominator. It would retire this signed producer only. It would not prove that $e+\pi$ is rational.

---

## 8. Bounded exact-arithmetic receipt

No computation is needed at an actual huge polynomial degree. The following proposed receipt checks only the new small arithmetic. It has not been executed here.

### 8.1 Bounded inputs

1. Moduli $5,25,125$.
2. The two forced recurrences $T_j^\pm$, only through $j=6$.
3. The thirteen weights and the four local recurrences in (2.3), only through $k=12$, evaluated at $n=2\pmod5$.
4. The Gaussian recurrences at $i=2,-2$, only through return of their initial pairs.
5. The degree-three polynomials $A_K,L$.
6. The degree-six polynomial $\mathcal H(1-x)$ and the degree-four polynomial $C_2(1-x)^2$.
7. The formal parameters $u,t$ in the displayed binomial congruences for $N_u$.

No actual $h,\lambda,G,q$ normalization is an input, and no fixed-$17$ calculation is requested.

### 8.2 Expected verifiable outputs

**Boundary values**


$$
(T_j^-)_{j=0}^6=(0,1,3,4,2,4,4)\pmod5,
$$




$$
(T_j^+)_{j=0}^6=(0,1,1,1,0,3,2)\pmod5.
$$


Hence


$$
(H_2^-,H_1^-,H_2^+,H_1^+)=(2,3,2,1)\pmod5.
$$



**Complete local evaluation**


$$
(\mathsf A,\mathsf B,\mathsf C_U,\mathsf C_E)
=(4,0,2,3)\pmod5.
$$



**Gaussian return**


$$
(a_N,b_N,a_{N-1},b_{N-1})
=(2,1,4,4)\pmod5
$$


for $N\equiv9\pmod{12}$, together with the separately recorded conclusion $5\nmid g_B$.

**Original-index congruences**


$$
N_u\equiv21+5u\pmod{25},
$$




$$
N_{1+5t}\equiv1+25t\pmod{125}.
$$


The extension in $u,t$ is checked symbolically using the displayed binomial expansions, not by enumeration.

**Arc values**


$$
L(16)=-945,\qquad A_K(16)=-13050,\qquad A_K'(16)=-1074,
$$


and


$$
\frac{30L(16-25t)}{25}\equiv1,\qquad
\frac{A_K(16-25t)}{25}\equiv3+4t\pmod5.
$$



**Source jet**


$$
[x^r]\bigl(\mathcal H(1-x)C_2(1-x)^2\bigr)_{r=0}^{10}
=
(0,4,-76,528,-1740,3269,-3857,2976,-1488,448,-64),
$$


with


$$
\sum_{r=0}^{10}r![x^r](\mathcal H(1-x)C_2(1-x)^2)
\equiv20\pmod{25}.
$$


The formal variation gives


$$
d_3-15t\equiv0\pmod{25},
\qquad
U-5(1-t)\equiv0\pmod{25}.
$$



**Final residuals**


$$
U-(1-u),\qquad g_B^2V-3,\qquad E_K-4u
$$


are zero modulo $5$, and, on $u=1+5t$,


$$
y_K-d_K(1+t)\equiv0\pmod5.
$$


At $t=4+5v$,


$$
U\equiv10\pmod{25}.
$$



These outputs verify the bounded arithmetic in Theorem 5.1. Its extension to every original index follows from the proved residue identities and coefficient-period arguments—not from finite extrapolation. This receipt would not prove the aggregate mass lemma.

---

## 9. Final conclusions

### New proved statements

1. The two original-boundary lift slopes have the explicit polynomial formulas (3.3)–(3.4) and the evaluated unit dual Wronskian
   

$$
H_a^-H_{a-1}^+ +H_{a-1}^-H_a^+\equiv-2\pmod p
$$


   at every odd prime.

2. For every $p\ge5$, the original forced boundary sequences satisfy the uniform all-depth next-digit congruence
   

$$
T_{j+p^kt}(c)-T_j(c)
   \equiv p^{k-1}tH_{j\bmod p}(c)\pmod{p^k}.
$$


   This does not freeze the Gaussian data.

3. The actual original intrinsic joint divisor has the exact prime-$5$ valuation
   

$$
v_5(\mathfrak J_{N_u}^0)
   =\mathbf1_{u\equiv21\pmod{25}}.
$$


   Both separation minors are evaluated, and the exceptional higher depth is paid by $U\equiv10\pmod{25}$.

4. The exception occurs with
   

$$
5\nmid2g_B\Delta d_K.
$$


   Thus good-prime determinant hypotheses and independent boundary slopes do not imply joint coprimality.

### Exact remaining bottleneck

No positive proportion of the factorial-size prime-power mass of $U_N$ has yet been excluded from the exceptional source and complete-endpoint branches. The unresolved task is a uniform paid bound for those exceptional depths and their product, including large primes and the actual Gaussian-content and $p\mid\Delta$ branches.

Throughout, the original domain, finite terminal, thirteen weights, both forced returns, both complete arcs, paid $\alpha,\beta,\delta$, actual content, least simultaneous clearer $D$, least aggregate clearer $\lambda$, final ALL-prime $G$, actual primitive denominator, and nonzero whole error have remained in force.

**The new result is an all-odd-prime boundary-lift rank theorem together with an exactly evaluated original intrinsic exception. It is not an aggregate cancellation bound, not producer retirement, and not a resolution of the rationality or irrationality of $e+\pi$.**
