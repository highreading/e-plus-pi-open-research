> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent referee report on the same-$H$ reference-Gram candidate

## 1. Verdict and scope

**The new analytic candidate passes at its stated scope.** Its finite-degree extrapolation estimate, complete reference cutoff, overlap and atom payments, uniform Loewner comparison, Vandermonde AM–GM inequality, Laguerre normalization, determinant lower bound, and $k^2$-constant are all valid.

In particular, for the **unchanged original compact determinant**, the candidate proves


$$
(-1)^kH_k(e+\pi)
\ge
\left(\frac{3\Lambda_k}{64}\right)^k
\mathfrak h_k\,B_k>0
\qquad(k\ge512),
\tag{1.1}
$$


where


$$
\mathfrak h_k=\det\left(\frac1{i+j+1}\right)_{0\le i,j<k},
\qquad
B_k=2^{k(k-1)}
\prod_{j=0}^{k-1}j!(3k-1+j)!.
\tag{1.2}
$$


Consequently,


$$
\log |H_k(e+\pi)|
\ge
4k^2\log k+
\left(15\log2-\frac92\log3\right)k^2+o(k^2).
\tag{1.3}
$$



The arithmetic implication also passes, **conditionally**. If both actual odd maximal-minor contents satisfy the proposed odd descent, and if an actual binary upper bound with coefficient


$$
A<
A_*:=
\frac{19\log2-\frac92\log3-6}{\log2}
\tag{1.4}
$$


is proved, then the positive primitive whole errors diverge at the same original indices. An exact elementary certificate below gives


$$
3.2114985014<A_*<3.2114985015.
\tag{1.5}
$$


Thus the requested condition $A<3.2114985014$ is sufficient. In particular, $A=3$ leaves the strictly positive margin


$$
16\log2-\frac92\log3-6>0.
\tag{1.6}
$$



**None of the necessary content upper hypotheses is proved here or in the supplied A2 report.** Therefore neither primitive divergence nor primitive decay follows unconditionally.

The rationality or irrationality of $e+\pi$ remains unresolved.

### Scope exclusions

- This is an independent mathematical audit of the **coordinator’s new analytic candidate**.
- It is not an independent audit of my earlier actual27/core27 argument. That separate audit remains required.
- The completed physical6 prefix calculation is not repeated.
- The other three6-returns are not addressed.
- Only the compact material in old A4 Sections 7–8 is reused. Its distinct historical Laguerre-matrix producer is not reopened.
- No original compact finite arrays are recomputed. The supplied $k=1,\ldots,10$ reference receipt remains finite supporting arithmetic only.

### Decision ledger

| Step | Decision | Exact scope |
|---|---|---|
| Original compact interface and signed conditional identity | **PASS** | Same coefficients, measures, clearers and matrix boundaries |
| Legendre evaluation kernel on $[-1,k]$ | **PASS** | $\deg p\le k-1,\ k\ge2$ |
| Payment of the complete reference interval $0\le x\le k$ | **PASS** | No uncontrolled low reference tail is deleted |
| Full overlap and negative-atom payment | **PASS** | Uniformly for every $y\in[0,1]^k$ |
| $M_y\succeq D_k/32$ | **PASS** | Every integer $k\ge512$ |
| Highest reference factorial $(6k-4)!$ | **PASS** | Exactly the original physical terminal |
| Vandermonde AM–GM factor | **PASS** | Size inequality, not divisibility |
| Laguerre monic norm product | **PASS** | Parameter $\alpha=3k-1$, with exact normalization |
| Same-$H$ determinant lower bound | **PASS** | No arithmetic normalization is changed |
| Constant $15\log2-\frac92\log3$ | **PASS** | Uses the established unconditional lcm/PNT asymptotic |
| Conditional content-to-divergence implication | **PASS, conditional** | Requires actual odd contents and an actual binary upper bound |
| Actual odd-content descent | **OPEN** | Not supplied by the analytic proof |
| Required binary upper bound | **OPEN** | Lower divisors and capped $3$-adic data do not prove it |
| Global rationality/irrationality conclusion | **NOT OBTAINED** | No unconditional primitive decay or divergence is established |

---

## 2. Fixed original objects and primitive normalization

### 2.1 Original index set and finite boundary

The infinite original index set remains


$$
\mathcal K=\{K_u:u\ge0\},
\qquad
K_u=9^{18+32u}=3^{36+64u}.
\tag{2.1}
$$


Every such index exceeds $512$, since already $3^6=729>512$.

For the compact family retain


$$
0\le m<2k,\qquad 0\le j<k,
\tag{2.2}
$$


and


$$
a_0=1,\qquad a_d=1-da_{d-1},
$$




$$
c_n=a_{2n}-(-1)^n,
\qquad
\rho_0=0,\qquad
\rho_{n+1}+\rho_n=\frac1{2n+1},
$$




$$
r_n=-(2n)!+4\rho_n.
\tag{2.3}
$$


Set


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
\tag{2.4}
$$



The integer affine polynomial is exactly


$$
H_k(s)=
\det\left[
(c_{m+j})\
\middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right]
=H_{0,k}+H_{1,k}s.
\tag{2.5}
$$


It is affine because the parameter-dependent part has rank one.

The largest moment index is


$$
(2k-1)+(k-1)=3k-2.
$$


Thus the physical boundary is exactly


$$
\boxed{
\text{moment }3k-2,\qquad
\text{factorial }(6k-4)!,\qquad
\text{last odd denominator }6k-5.
}
\tag{2.6}
$$



No successor row, successor contact, or extended terminal is introduced below.

### 2.2 Actual clearers and final gcd

The individual original right-column clearers remain


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3),
\qquad 0\le j<k.
\tag{2.7}
$$


The common least entry clearer of the complete unprojected right block is $\Lambda_k$.

The key exact identity behind these assertions is


$$
r_n+r_{n-1}
=-(2n)!-(2n-2)!+\frac4{2n-1}.
\tag{2.8}
$$


Since $2n-1$ is odd, clearing two consecutive moments forces divisibility by $2n-1$. For a fixed column, the forced odd denominators range from $2j+1$ through $4k+2j-3$. Every smaller odd denominator divides an odd multiple in that range, so the stated column lcm is indeed least. This is an entry-clearer statement; it is not a determination of determinant content.

The final gcd remains the **ALL-prime** gcd


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|).
\tag{2.9}
$$


For the rational coefficient pair of $H_k/\Lambda_k^k$, define


$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


Its exact least simultaneous coefficient clearer and subsequent content are


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
}
\tag{2.10}
$$


After both payments, the primitive coefficient pair is precisely $H_k/G_k$, up to common sign.

The independently accepted A5 result supplies


$$
(-1)^kH_{1,k}>0\qquad(k\ge64).
\tag{2.11}
$$


We reuse that theorem at its stated scope; its complementary-minor proof is not repeated.

Consequently, at every original index,


$$
q_k=\frac{|H_{1,k}|}{G_k}>0,
\qquad
p_k=-\frac{(-1)^kH_{0,k}}{G_k},
\tag{2.12}
$$


and


$$
\ell_k:=q_k(e+\pi)-p_k
=\frac{(-1)^kH_k(e+\pi)}{G_k}.
\tag{2.13}
$$


The quantity requiring control is this **whole error**, not merely
$\lvert e+\pi-p_k/q_k\rvert$.

---

## 3. Measures and the exact conditional determinant

### 3.1 Complete measures

Let $\mu$ be the pushforward of $e^{-s}\,ds$, $s\ge0$, under


$$
x=(s-1)^2.
$$


Then $\mu$ has total mass $1$, and


$$
\frac{d\mu}{dx}
=
\frac{e^{-1}}{2\sqrt x}
\left(e^{-\sqrt x}
+\mathbf1_{(0,1)}(x)e^{\sqrt x}\right).
\tag{3.1}
$$


In particular,


$$
\frac{d\mu}{dx}
=\frac{e^{-1-\sqrt x}}{2\sqrt x}\quad(x>1),
\qquad
\mu([0,1])=1-e^{-2}.
\tag{3.2}
$$



The signed functional is exactly


$$
L(f)=\int f\,d\mu-f(-1).
\tag{3.3}
$$


The atom has mass $-1$; it is not suppressed.

The complete compact measure is


$$
\frac{d\nu}{dx}
=
\frac{e^{\sqrt x}+4/(1+x)}{2\sqrt x},
\qquad 0<x<1.
\tag{3.4}
$$


This includes both the exponential and arctangent channels.

The recurrence for $a_d$ gives


$$
L(x^n)=c_n.
$$


Finite integration by parts and the arctangent recurrence give the full moment relation


$$
\nu_n:=\int x^n\,d\nu(x)
=e\,c_n+(e+\pi)(-1)^n+r_n.
\tag{3.5}
$$



Thus, at $s_0=e+\pi$, adding $e\Lambda_k$ times each contact column to the corresponding right column yields


$$
H_k(s_0)=\Lambda_k^k\det[C\mid N],
\tag{3.6}
$$


where


$$
C_{mj}=c_{m+j},
\qquad
N_{mj}=\nu_{m+j}.
$$


This is a determinant-preserving operation on the evaluated real matrix. It does not alter the original integer polynomial or its content.

### 3.2 Conditional identity: sign and factorial normalization

For $y=(y_1,\ldots,y_k)\in[0,1]^k$, put


$$
Q_y(x)=\prod_{r=1}^k(x-y_r),
\qquad
M_y(i,j)=L(x^{i+j}Q_y(x)),
\quad 0\le i,j<k.
\tag{3.7}
$$



The reused identity is


$$
\boxed{
(-1)^kH_k(e+\pi)
=
\frac{\Lambda_k^k}{k!}
\int_{[0,1]^k}V(y)^2\det M_y\,d\nu^k(y).
}
\tag{3.8}
$$



Its normalization can be checked directly. Symmetrizing determinant integration in the two $k$-column groups gives


$$
\det[C\mid N]
=
\frac1{(k!)^2}
\int
V(x)^2V(y)^2
\prod_{i,j}(y_j-x_i)\,dL^k(x)\,d\nu^k(y).
$$


The cross product is


$$
\prod_{i,j}(y_j-x_i)
=(-1)^{k^2}\prod_i Q_y(x_i)
=(-1)^k\prod_i Q_y(x_i),
$$


and


$$
\det M_y
=\frac1{k!}\int V(x)^2\prod_iQ_y(x_i)\,dL^k(x).
$$


These formulas prove (3.8), including its sign and its single remaining $1/k!$.

All determinant integrations are legitimate: they involve finite polynomials, $\mu$ has every polynomial moment, and $\nu$ is compactly supported.

---

## 4. Audit of the uniform reference-Gram comparison

### 4.1 Finite-degree Legendre estimate on $[-1,k]$

Let $p$ be a real polynomial with


$$
\deg p\le k-1,
\qquad
E_k(p)=\int_{k^2}^{4k^2}p(x)^2\,dx.
$$


The affine coordinate


$$
t=\frac{2x-5k^2}{3k^2}
\tag{4.1}
$$


maps $[k^2,4k^2]$ onto $[-1,1]$.

For $x\in[-1,k]$ and $k\ge2$,


$$
|t|
\le \frac53+\frac{2}{3k^2}
\le\frac{11}{6}<2.
\tag{4.2}
$$



Let $P_j$ be the ordinary Legendre polynomial normalized by $P_j(1)=1$. Its recurrence is


$$
(j+1)P_{j+1}(t)
=(2j+1)tP_j(t)-jP_{j-1}(t).
$$


The bounds $P_0=1$, $|P_1(t)|\le2$, and induction give


$$
|P_j(t)|\le5^j\qquad(|t|\le2).
\tag{4.3}
$$


Indeed, the induction step is bounded by


$$
4\cdot5^j+5^{j-1}<5^{j+1}.
$$



Since


$$
\int_{k^2}^{4k^2}P_j(t(x))^2\,dx
=\frac{3k^2}{2j+1},
$$


the orthonormal evaluation kernel is


$$
\frac1{3k^2}
\sum_{j=0}^{k-1}(2j+1)P_j(t)^2.
$$


Cauchy–Schwarz therefore yields


$$
\begin{aligned}
|p(x)|^2
&\le E_k(p)\frac1{3k^2}
\sum_{j=0}^{k-1}(2j+1)25^j\\
&\le E_k(p)\frac{25^{k-1}}{3k^2}
\sum_{j=0}^{k-1}(2j+1).
\end{aligned}
$$


Because the last sum equals $k^2$,


$$
\boxed{
\max_{[-1,k]}|p|^2
\le K'_kE_k(p),
\qquad
K'_k=\frac{25^{k-1}}3.
}
\tag{4.4}
$$



**Decision: PASS.** The factor $3k^2$, the degree restriction, and the enlarged evaluation interval are all correct.

---

### 4.2 The complete reference form and its low cutoff

Define


$$
R_k(p)=
\int_0^\infty
p(x)^2x^k\frac{e^{-\sqrt x}}{2\sqrt x}\,dx.
\tag{4.5}
$$


It is positive for every nonzero polynomial $p$.

On $[k^2,4k^2]$,


$$
x^k\frac{e^{-\sqrt x}}{2\sqrt x}
\ge
\frac{k^{2k}e^{-2k}}{4k}
=:r_k.
$$


Hence


$$
R_k(p)\ge r_kE_k(p).
\tag{4.6}
$$



Let $R_{k,\mathrm{low}}$ denote the part of (4.5) over $0\le x\le k$. By (4.4),


$$
\begin{aligned}
R_{k,\mathrm{low}}(p)
&\le
K'_kE_k(p)
\int_0^k\frac{x^{k-1/2}}2\,dx\\
&=
K'_kE_k(p)\frac{k^{k+1/2}}{2k+1}.
\end{aligned}
$$


For $p\ne0$, division by (4.6) gives


$$
\frac{R_{k,\mathrm{low}}(p)}{R_k(p)}
\le
\frac{4k}{75(2k+1)}
\sqrt k\left(\frac{25e^2}{k}\right)^k
<
\frac2{75}\sqrt k\left(\frac{225}{k}\right)^k,
\tag{4.7}
$$


using $e<3$.

The cutoff is verified without decimal approximations. For $k\ge512$,


$$
\frac{225}{k}<\frac12
$$


because $450<512$. Also $k2^{-k}$ decreases for integers $k\ge2$, and


$$
k2^{-k}\le4\cdot2^{-4}=\frac14\qquad(k\ge4).
$$


Therefore


$$
\frac2{75}\sqrt k\left(\frac{225}{k}\right)^k
\le
\frac2{75}k2^{-k}
\le\frac1{150}<\frac14.
\tag{4.8}
$$


Thus


$$
\boxed{
R_{k,\mathrm{high}}(p)
:=R_k(p)-R_{k,\mathrm{low}}(p)
\ge\frac34R_k(p)
\qquad(k\ge512).
}
\tag{4.9}
$$



**Decision: PASS.** The entire reference interval $0\le x\le k$, not merely $0\le x\le1$, has been paid.

---

### 4.3 Positive exterior contribution

For $x\ge k$, $y_r\in[0,1]$, and $k\ge2$,


$$
Q_y(x)\ge(x-1)^k
\ge\left(1-\frac1k\right)^kx^k.
\tag{4.10}
$$


The function


$$
t\longmapsto t\log(1-1/t)
$$


is increasing for $t>1$, since, with $u=1/(t-1)>0$, its derivative is


$$
u-\log(1+u)>0.
$$


Consequently,


$$
\left(1-\frac1k\right)^k\ge\frac14\qquad(k\ge2).
\tag{4.11}
$$



Using the exact exterior density of $\mu$,


$$
\begin{aligned}
\int_k^\infty p(x)^2Q_y(x)\,d\mu(x)
&\ge\frac1{4e}R_{k,\mathrm{high}}(p)\\
&\ge\frac3{16e}R_k(p)
>\frac1{16}R_k(p).
\end{aligned}
\tag{4.12}
$$



The factor $e^{-1}$ in $\mu$ has been retained. The comparison uses the complete reference integral over $[k,\infty)$, not just the finite exterior interval used to control polynomial evaluation.

---

### 4.4 Entire overlap and atom loss

On $0\le x\le1$,


$$
|Q_y(x)|\le1.
$$


Since $\mu([0,1])\le1$, the complete possible overlap loss is at most


$$
\max_{[-1,1]}|p|^2.
$$



At the actual atom,


$$
|Q_y(-1)|=\prod_r(1+y_r)\le2^k.
$$


Thus the whole possible adverse contribution of the atom is at most


$$
2^k\max_{[-1,1]}|p|^2.
$$


This bounds the entire atom even when its sign is favorable.

Together, these losses are at most


$$
(1+2^k)K'_kE_k(p).
\tag{4.13}
$$


All remaining $x>1$ contributions are nonnegative.

Relative to $R_k(p)$, (4.6) gives


$$
\begin{aligned}
\frac{(1+2^k)K'_kE_k(p)}{R_k(p)}
&\le
\frac{4k}{75}(1+2^k)
\left(\frac{25e^2}{k^2}\right)^k\\
&\le
\frac{8k}{75}\left(\frac{450}{k^2}\right)^k.
\end{aligned}
\tag{4.14}
$$


For $k\ge512$,


$$
\frac{450}{k^2}<\frac12
$$


because $900<512^2$. Therefore


$$
\frac{8k}{75}\left(\frac{450}{k^2}\right)^k
\le\frac8{75}k2^{-k}
\le\frac2{75}<\frac1{32},
\tag{4.15}
$$


where the last inequality is exactly $64<75$.

Combining (4.12)–(4.15),


$$
\boxed{
L(p^2Q_y)\ge\frac1{32}R_k(p)
\qquad
(k\ge512,\ \deg p\le k-1,\ y\in[0,1]^k).
}
\tag{4.16}
$$



**Decision: PASS.** No overlap branch, contact atom, or reference low tail has been omitted.

---

### 4.5 Matrix inequality and physical factorial terminal

Write


$$
p(x)=\sum_{i=0}^{k-1}v_ix^i.
$$


Then


$$
L(p^2Q_y)=v^TM_yv.
$$


In the reference form, the substitution $z=\sqrt x$ gives


$$
\int_0^\infty
x^{k+i+j}\frac{e^{-\sqrt x}}{2\sqrt x}\,dx
=
\int_0^\infty z^{2k+2i+2j}e^{-z}\,dz
=(2k+2i+2j)!.
$$


Hence


$$
R_k(p)=v^TD_kv,
\qquad
D_k=\bigl((2k+2i+2j)!\bigr)_{0\le i,j<k}.
\tag{4.17}
$$


Equation (4.16) is exactly


$$
\boxed{M_y\succeq \frac1{32}D_k.}
\tag{4.18}
$$



The reference moment degree in $x$ is at most


$$
k+2(k-1)=3k-2,
$$


and the highest factorial is


$$
2k+2(k-1)+2(k-1)=6k-4.
$$


These are precisely the original physical boundaries.

Because $D_k$ is positive definite, conjugation by $D_k^{-1/2}$ proves


$$
\boxed{
\det M_y\ge32^{-k}\det D_k.
}
\tag{4.19}
$$



**Decision: PASS.** This is a quadratic-form comparison, not an invalid inference from entrywise estimates.

---

## 5. Audit of the evaluated factorial determinant bound

### 5.1 Vandermonde factorization and AM–GM

The Gram determinant formula gives


$$
\det D_k
=
\frac1{k!}
\int_{(0,\infty)^k}
V(z_1^2,\ldots,z_k^2)^2
\prod_{i=1}^kz_i^{2k}e^{-z_i}\,dz_i.
\tag{5.1}
$$


For positive $z_i$,


$$
V(z^2)^2
=
V(z)^2\prod_{i<j}(z_i+z_j)^2.
$$


For each pair,


$$
(z_i+z_j)^2\ge4z_iz_j.
$$


There are $k(k-1)/2$ pairs, and each $z_i$ occurs in $k-1$ of them. Therefore


$$
\boxed{
V(z^2)^2
\ge
2^{k(k-1)}V(z)^2\prod_i z_i^{k-1}.
}
\tag{5.2}
$$


Substituting this into (5.1) produces the weight


$$
z^{2k+k-1}e^{-z}=z^{3k-1}e^{-z}.
$$



The binary exponent and the Laguerre parameter are therefore exactly


$$
k(k-1),\qquad \alpha=3k-1.
$$



---

### 5.2 Exact Laguerre monic norms

For $\alpha=3k-1$, let


$$
q_j(z)=(-1)^j j!L_j^{(\alpha)}(z).
$$


The standard leading coefficient of $L_j^{(\alpha)}$ is $(-1)^j/j!$, so $q_j$ is monic.

The needed normalization can also be derived directly from Rodrigues’ formula:


$$
q_j(z)=
(-1)^jz^{-\alpha}e^z
\frac{d^j}{dz^j}\bigl(e^{-z}z^{j+\alpha}\bigr).
\tag{5.3}
$$


Integration by parts $j$ times gives orthogonality against all degrees below $j$, and


$$
\int_0^\infty q_j(z)z^jz^\alpha e^{-z}\,dz
=j!\Gamma(j+\alpha+1).
$$


All boundary terms vanish: $\alpha=3k-1\ge2$, and the exponential controls infinity. Since $q_j-z^j$ has lower degree,


$$
\boxed{
\int_0^\infty q_j(z)^2z^\alpha e^{-z}\,dz
=j!\Gamma(j+\alpha+1)
=j!(3k-1+j)!.
}
\tag{5.4}
$$



The unitriangular change from monomials to monic orthogonal polynomials has determinant $1$. Hence


$$
\det\bigl((3k-1+i+j)!\bigr)_{i,j<k}
=
\prod_{j=0}^{k-1}j!(3k-1+j)!.
\tag{5.5}
$$


Combining (5.1)–(5.5),


$$
\boxed{
\det D_k\ge
B_k=
2^{k(k-1)}
\prod_{j=0}^{k-1}j!(3k-1+j)!.
}
\tag{5.6}
$$



At $k=1$, equality holds. For $k\ge2$, the inequality is a genuine positive-integral size comparison.

The comparison Laguerre Gram matrix uses factorials only through


$$
(3k-1)+2(k-1)=5k-3\le6k-4.
$$


Its monic norm product uses factorials only through $4k-2$. Thus no hidden degree extension occurs.

**Decision: PASS.** Formula (5.6) is not an integer divisibility assertion about $D_k$, $H_k$, or $G_k$.

---

## 6. Same-$H$ lower bound and its next constant

### 6.1 Complete compact density

For $0<x<1$,


$$
e^{\sqrt x}\ge1,\qquad
\frac4{1+x}\ge2,\qquad
2\sqrt x\le2.
$$


Thus, with respect to $dx$,


$$
\frac{d\nu}{dx}\ge\frac32.
\tag{6.1}
$$


Let


$$
J_k^\nu=\frac1{k!}\int_{[0,1]^k}V(y)^2\,d\nu^k(y).
$$


Then


$$
J_k^\nu\ge\left(\frac32\right)^k\mathfrak h_k.
\tag{6.2}
$$



Here $\mathfrak h_k$ is the ordinary Hilbert determinant. It is not the differently normalized half-moment determinant denoted $h_k$ in parts of A5.

Using (3.8), (4.19), (5.6), and (6.2),


$$
\begin{aligned}
(-1)^kH_k(e+\pi)
&\ge \Lambda_k^k32^{-k}J_k^\nu\det D_k\\
&\ge
\left(\frac{3\Lambda_k}{64}\right)^k
\mathfrak h_kB_k.
\end{aligned}
$$


This proves (1.1).

In particular, at every original index,


$$
\boxed{
\ell_k
=\frac{|H_k(e+\pi)|}{G_k}
\ge
\frac{(3\Lambda_k/64)^k\mathfrak h_kB_k}{G_k}>0.
}
\tag{6.3}
$$


The final gcd has not been discarded.

---

### 6.2 Stirling calculation, including all $k^2$-constants

Define


$$
S(m)=\sum_{j=0}^{m-1}\log(j!).
$$


Stirling summation gives


$$
S(m)=\frac12m^2\log m-\frac34m^2+O(m\log m).
\tag{6.4}
$$


Exactly,


$$
\log B_k
=k(k-1)\log2+S(k)+S(4k-1)-S(3k-1).
\tag{6.5}
$$



The contributions are:

- From $S(k)$:
  

$$
\frac12k^2\log k-\frac34k^2+O(k\log k).
$$


- From $S(4k-1)-S(3k-1)$:
  

$$
\frac72k^2\log k+
  \left(16\log2-\frac92\log3-\frac{21}{4}\right)k^2
  +O(k\log k).
$$


- From $k(k-1)\log2$:
  

$$
(\log2)k^2+O(k).
$$



Therefore


$$
\boxed{
\log B_k
=
4k^2\log k+
\left(17\log2-\frac92\log3-6\right)k^2
+O(k\log k).
}
\tag{6.6}
$$



The Hilbert determinant formula is


$$
\mathfrak h_k
=
\frac{\prod_{j=0}^{k-1}(j!)^4}
{\prod_{j=0}^{2k-1}j!},
$$


so


$$
\log\mathfrak h_k
=4S(k)-S(2k)
=-2(\log2)k^2+O(k\log k).
\tag{6.7}
$$



Finally, with $N=6k-5$,


$$
\log\Lambda_k
=
\psi(N)-\lfloor\log_2N\rfloor\log2
=6k+o(k),
\tag{6.8}
$$


by the established unconditional prime number theorem for $\psi$.

Taking logarithms of (1.1), the $k^2$-contributions are


$$
6+
\left(17\log2-\frac92\log3-6\right)
-2\log2.
$$


Hence


$$
\boxed{
C_H=15\log2-\frac92\log3,
}
\tag{6.9}
$$


as claimed.

This is a lower-bound constant. It is not a claim that the actual next-order asymptotic constant of $\log|H_k(e+\pi)|$ equals $C_H$.

---

### 6.3 A useful reuse observation

The accepted A5 theorem already gives, for the same determinant,


$$
|H_k(e+\pi)|
\ge \frac12e^{-2k}\Lambda_k^kJ_k^\nu\det D_k
\qquad(k\ge64).
$$


Combining that established result with the newly audited bound (5.6) yields the stronger finite prefactor


$$
\boxed{
|H_k(e+\pi)|
\ge
\frac12
\left(\frac{3\Lambda_k}{2e^2}\right)^k
\mathfrak h_kB_k
\qquad(k\ge64).
}
\tag{6.10}
$$


It gives the same $k^2$-constant $C_H$.

This is a corollary by reuse, not a repetition of A5’s proof. It does **not** extend the newly proved uniform Loewner assertion $M_y\succeq D_k/32$ down to $64$; that pointwise assertion has been proved here only for $k\ge512$.

The older constant $6-\log48$ remains an already established baseline, not a new result of this report.

---

## 7. Conditional arithmetic audit of A2turn7

### 7.1 Actual original rectangles and complete returns

Retain


$$
\sigma_n=c_{n+1}+c_n
$$


and the complete return


$$
\boxed{
\tau_n=r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
\tag{7.1}
$$


Neither factorial forcing term is removed.

The actual rectangles are


$$
Z_k=
\left[
(c_{m+j})_{\substack{m<2k\\j<k}}
\ \middle|\
(\Lambda_k\tau_{m+j})_{\substack{m<2k\\j<k-1}}
\right],
\tag{7.2}
$$




$$
Y_k=
\left[
(\sigma_{m+j})_{\substack{m<2k-1\\j<k}}
\ \middle|\
(\Lambda_k\tau_{m+j})_{\substack{m<2k-1\\j<k}}
\right].
\tag{7.3}
$$


Their actual maximal-minor contents are


$$
\mathscr R_k=\delta_{2k-1}(Z_k),
\qquad
\mathscr L_k=\delta_{2k-1}(Y_k).
\tag{7.4}
$$


The largest return index is $3k-3$, whose successor moment is the physical $3k-2$.

Reuse the established bordered-content relations at these exact objects:


$$
\boxed{
\operatorname{lcm}(\mathscr R_k,\mathscr L_k)
\mid G_k
\mid \Lambda_k\mathscr R_k\mathscr L_k.
}
\tag{7.5}
$$



### 7.2 Exact odd-descent hypothesis

Put


$$
W_k^{\mathrm{odd}}
=
3^{2k}\Lambda_k^k
\left(\prod_{j=0}^{k-1}\operatorname{odd}(j!)\right)^4.
\tag{7.6}
$$


The two required hypotheses are


$$
\boxed{
\operatorname{odd}(\mathscr R_k)\mid W_k^{\mathrm{odd}},
\qquad
\operatorname{odd}(\mathscr L_k)\mid W_k^{\mathrm{odd}}.
}
\tag{7.7}
$$


These concern the original, unweighted maximal-minor ideals.

For every odd prime $p$, the exact allowance is


$$
B_p(k)=
k\bigl(2\mathbf1_{p=3}+v_p(\Lambda_k)\bigr)
+4\sum_{j=0}^{k-1}v_p(j!).
\tag{7.8}
$$


Thus (7.7) means


$$
v_p(\mathscr R_k)\le B_p(k),
\qquad
v_p(\mathscr L_k)\le B_p(k)
\quad\text{for every odd }p.
\tag{7.9}
$$


For $p>6k-5$, this allowance is zero. Such primes cannot be ignored.

Under (7.7), the **odd part of the final gcd** satisfies


$$
\operatorname{odd}(G_k)
\mid
\Lambda_kW_k^{\mathrm{odd}\,2}.
\tag{7.10}
$$


This follows directly from the upper divisibility in (7.5).

Let


$$
a_G(k)=v_2(G_k).
$$


Then the exact finite inequality is


$$
\boxed{
\log G_k
\le a_G(k)\log2+\log\Lambda_k
+2\log W_k^{\mathrm{odd}}.
}
\tag{7.11}
$$



This is why a direct upper bound for $v_2(G_k)$ is sufficient. It is not necessary first to determine the binary depths of both rectangle contents separately.

---

### 7.3 Paid height of the odd certificate

From Legendre’s formula,


$$
v_2(j!)=j-s_2(j),
$$


so


$$
\sum_{j=0}^{k-1}v_2(j!)
=\frac12k^2+O(k\log k).
\tag{7.12}
$$


Using (6.4) and (6.8),


$$
\begin{aligned}
\log W_k^{\mathrm{odd}}
={}&2k\log3+k\log\Lambda_k
+4S(k)
-4\log2\sum_{j=0}^{k-1}v_2(j!)\\
={}&
2k^2\log k+(3-2\log2)k^2+o(k^2).
\end{aligned}
\tag{7.13}
$$



All finite factors remain in the first line. In particular, $3^{2k}$ and the full $\Lambda_k^k$ have not been deleted merely because part of their logarithm is lower order.

If, conditionally,


$$
a_G(k)\le Ak^2+o(k^2)
\tag{7.14}
$$


on the original indices, then (7.11)–(7.13) imply


$$
\boxed{
\log G_k
\le
4k^2\log k+
\bigl(A\log2+6-4\log2\bigr)k^2+o(k^2).
}
\tag{7.15}
$$



A2’s stated route uses


$$
a_Y=v_2(\mathscr L_k),\qquad
a_Z=v_2(\mathscr R_k),
$$


and the stronger hypothesis


$$
a_Y+a_Z\le Ak^2+o(k^2).
\tag{7.16}
$$


Because $\Lambda_k$ is odd, (7.5) gives


$$
a_G\le a_Y+a_Z.
$$


Thus (7.16) also proves (7.15).

**Important normalization point:** $A=3$ here means a coefficient $3$ for $a_G$, or for the **sum** $a_Y+a_Z$. Separate bounds $a_Y\le3k^2+o(k^2)$ and $a_Z\le3k^2+o(k^2)$ would give coefficient $6$, not $3$.

---

### 7.4 Divergence of the actual primitive whole error

Subtract (7.15) from the audited lower bound (1.3). At the same original indices,


$$
\begin{aligned}
\log\ell_k
&=\log|H_k(e+\pi)|-\log G_k\\
&\ge
\left(
19\log2-\frac92\log3-6-A\log2
\right)k^2+o(k^2).
\end{aligned}
\tag{7.17}
$$


Therefore, if $A<A_*$,


$$
\boxed{\ell_k\longrightarrow+\infty}
\qquad(k=K_u,\ u\to\infty).
\tag{7.18}
$$



For $A=3$, the margin is exactly


$$
\delta_3=16\log2-\frac92\log3-6>0.
\tag{7.19}
$$


For example, the conclusion then strengthens to


$$
\ell_k\ge \exp\!\left(\frac{\delta_3}{2}k^2\right)
$$


on a sufficiently large original tail.

**Decision: PASS as a conditional implication.**

If the hypotheses hold only on one unbounded original subset, divergence is proved only on that subset. To retire this producer on its entire original domain, the upper hypotheses must hold on an eventual tail of that domain.

Such divergence would retire this compact family as a source of primitive whole-error decay. It would not prove $e+\pi$ rational, and it would not exclude other producers.

---

## 8. Exact numerical certificates

### 8.1 Elementary bound for $e$

The factorial series gives


$$
e
=
\sum_{n=0}^3\frac1{n!}
+\sum_{n=4}^\infty\frac1{n!}
<
\frac83+\frac{1/24}{1-1/5}
=\frac{87}{32}
<\frac{11}{4}<3.
\tag{8.1}
$$


Thus all uses of $e<3$ in the cutoff proof are justified by an elementary exact estimate.

### 8.2 Positive $A=3$ margin

The inequality $\delta_3>0$ is equivalent to


$$
2^{32}>3^9e^{12}.
$$


By $e<11/4$, it suffices that


$$
2^{56}>3^9\,11^{12}.
$$


The exact integer comparison is


$$
\boxed{
72\,057\,594\,037\,927\,936
>
61\,773\,685\,738\,999\,443.
}
\tag{8.2}
$$


Hence the margin is rigorously positive without relying on a decimal evaluation.

### 8.3 Exact bracket for the binary threshold

For $0<t<1$,


$$
\log\frac{1+t}{1-t}
=
2\sum_{j=0}^{N-1}\frac{t^{2j+1}}{2j+1}
+\mathcal E_N(t),
$$


where


$$
0<\mathcal E_N(t)
\le
\frac{2t^{2N+1}}{(2N+1)(1-t^2)}.
\tag{8.3}
$$



A small rational certificate suffices. Let $T=10^{16}$, and define


$$
F(r,N)=
\sum_{j=0}^{N-1}
\left\lfloor
\frac{2T}{(2j+1)r^{2j+1}}
\right\rfloor.
$$


The evaluated integer sums are


$$
\begin{array}{c|c|r|c}
r&N&F(r,N)&T\,\mathcal E_N(1/r)\\ \hline
3&15&6\,931\,471\,805\,599\,445&<2\\
5&11&4\,054\,651\,081\,081\,639&<1
\end{array}
\tag{8.4}
$$


These are respectively certificates for $\log2$ and $\log(3/2)$. The floor error is less than $N$. Therefore they imply the convenient rational bounds


$$
\frac{69\,314\,718\,055\,994}{10^{14}}
<\log2<
\frac{69\,314\,718\,055\,995}{10^{14}},
\tag{8.5}
$$




$$
\frac{109\,861\,228\,866\,810}{10^{14}}
<\log3<
\frac{109\,861\,228\,866\,812}{10^{14}}.
\tag{8.6}
$$



For completeness, these bounds yield direct integer sign certificates for the proposed decimal cutoff. Let


$$
a_-=3.2114985014,\qquad a_+=3.2114985015.
$$


Using the lower bound for $\log2$ and upper bound for $\log3$,


$$
\begin{aligned}
&2(157\,885\,014\,986)(69\,314\,718\,055\,994)\\
&\quad
-9\cdot10^{10}(109\,861\,228\,866\,812)
-12\cdot10^{24}\\
&=28\,874\,954\,252\,168>0.
\end{aligned}
\tag{8.7}
$$


This proves


$$
(19-a_-)\log2-\frac92\log3-6>0,
$$


hence $a_-<A_*$.

Using the opposite bounds,


$$
\begin{aligned}
&2(157\,885\,014\,985)(69\,314\,718\,055\,995)\\
&\quad
-9\cdot10^{10}(109\,861\,228\,866\,810)
-12\cdot10^{24}\\
&=-109\,258\,711\,829\,850<0.
\end{aligned}
\tag{8.8}
$$


Thus $A_*<a_+$, proving (1.5).

This is bounded rational arithmetic for a constant. It is not a computation of any original content or primitive denominator.

---

## 9. What remains unpaid in the arithmetic

### 9.1 The now-sufficient compact arithmetic target

A concrete sufficient target for A2 is the following statement on an eventual tail of the unchanged original set $\mathcal K$:



$$
\boxed{
\begin{gathered}
\operatorname{odd}(\mathscr R_k)\mid W_k^{\mathrm{odd}},
\qquad
\operatorname{odd}(\mathscr L_k)\mid W_k^{\mathrm{odd}},\\[2mm]
v_2(G_k)\le3k^2+o(k^2).
\end{gathered}}
\tag{9.1}
$$


The stronger rectangle-content route


$$
v_2(\mathscr R_k)+v_2(\mathscr L_k)
\le3k^2+o(k^2)
\tag{9.2}
$$


would also suffice.

More generally, $3$ can be replaced by any fixed $A<A_*$.

This target is now decisive for **conditional producer retirement**, because the numerator’s critical constant has been evaluated. The target itself remains open.

### 9.2 Why the supplied local information does not prove it

Several logically different objects must remain separate.

1. **Binary lower divisors.**  
   An inequality
   

$$
v_2(\mathscr L_k)\ge\nu_k
$$


   is a lower bound. It cannot establish (9.1) or (9.2).

2. **Capped $3$-primary spectra.**  
   Even accepting the stated capped-spectrum theorem at every original index, knowledge of
   

$$
\min(e_i,h)
$$


   does not upper-bound the uncapped sum $\sum_i e_i$. Large tails remain possible.

3. **The finite-depth Schur reduction.**  
   Its stated support argument requires
   

$$
2h\le s+2,
   \qquad k=3^s.
$$


   Beyond that depth, return support need not preserve the contact residue classes. Beyond the separate factorial-vanishing range, the factorial forcing in $\Lambda_k\tau_n$ must also reappear. Extending the simplified Schur expression past these restrictions would discard genuine terms.

4. **Prime-local inverses.**  
   A matrix invertible over $\mathbb Z_{(3)}$ can have determinant divisible by other odd primes. Its inverse is not thereby permitted over $\mathbb Z[1/2]$.

5. **Weighted-stack or finite-jet certificates.**  
   Their contents are not automatically the contents of $Y_k$ and $Z_k$. The exact transfer payments must be retained.

These are precise mathematical obstructions, not merely a need for more small examples.

### 9.3 A concrete high-depth sublemma

At $k=3^s=K_u$, the exact $3$-allowance is


$$
B_3(k)=k^2+(2-s)k.
\tag{9.3}
$$


A concrete first high-depth target remains the two actual $Y_k$-cofactor inequality


$$
\min\!\left(
v_3(M_k^{(0)}),v_3(M_k^{(k-1)})
\right)
\le k^2+(2-s)k,
\tag{9.4}
$$


where the two minors omit respectively the first and last columns of the $\sigma$-block and retain **all $k$ original scaled return columns**.

This is an explicit original-object lemma, not an augmented-matrix substitute. It is still open. Even proving it would settle only the $3$-part for $Y_k$, not the other odd primes, $Z_k$, or the binary upper bound.

---

## 10. Retained payment ledger and separation of producers

### 10.1 Finite-jet payments are not assigned favorable values

The exact A2 transfers remain


$$
\mathscr R_k
=
\frac{\Lambda_k^{k-1}\mathscr C_{Z,k}\zeta_{Z,k}}{t_Z},
\qquad
\mathscr L_k
=
\frac{\Lambda_k^{k-1}\mathscr C_{Y,k}\chi_{Y,k}}{t_Y},
\tag{10.1}
$$


with


$$
t_Z=\prod_{m=0}^{2k-1}(2m+1)_{2k-3},
\qquad
t_Y=\prod_{m=0}^{2k-2}(2m+1)_{2k-1}.
\tag{10.2}
$$


Here $\mathscr C_{Z,k}$ and $\mathscr C_{Y,k}$ are the **actual** jet maximal-minor contents.

If $\mathbf v$ is the actual primitive signed cofactor vector specified in the finite-jet transfer, then


$$
\zeta_{Z,k}
=
\operatorname{lcm}_{m<2k}
\frac{(2m+1)_{2k-3}}
{\gcd((2m+1)_{2k-3},|v_m|)}.
\tag{10.3}
$$


Likewise,


$$
\chi_{Y,k}
=
\frac{\gcd(\Lambda_ka_Y,b_Y)}{\gcd(a_Y,b_Y)}
\mid\Lambda_k
\tag{10.4}
$$


for the actual two jet minor-type gcds in that transfer.

Neither correction is set equal to $1$. No upper bound for $\mathscr C_{Z,k}$ or $\mathscr C_{Y,k}$ is inferred from the analytic Gram comparison.

If the jet route is pursued, the already evaluated payment


$$
\log\mathscr R_k+\log\mathscr L_k
=
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
-8k^2\log k
+(24-18\log3)k^2+o(k^2)
\tag{10.5}
$$


must remain. For example, a sufficient paid-jet upper target would now be


$$
\log\mathscr C_{Z,k}+\log\mathscr C_{Y,k}
\le12k^2\log k+C_Jk^2+o(k^2)
$$


with


$$
C_J<
15\log2+\frac{27}{2}\log3-24.
\tag{10.6}
$$


This is another conditional formulation, not a proved content estimate.

### 10.2 Contact-frame and row-primitive routes

The present proof works directly with $H_k$; it performs no arithmetic contact projection. Thus it does not bypass any alternative-route payment.

In particular, the established contact polynomial clearers


$$
d_m=
\frac{|\det C_k|}
{\gcd\bigl(|\det C_k|,\operatorname{adj}(C_k)w_m\bigr)}
$$


and frame index


$$
J_k^{\mathrm{frame}}
=
\frac{\prod_{m=k}^{2k-1}d_m}{|\det C_k|/\delta_k}
$$


remain unchanged.

Likewise, if primitive contact rows $f_r$ are used, with


$$
u_r=f_r(-1),\qquad E_{rj}=\Lambda_kR(f_rx^j),
$$


their actual row clearer and row content remain


$$
\ell_r^{\mathrm{row}}
=
\frac{\Lambda_k}
{\gcd(\Lambda_k,E_{r0},\ldots,E_{r,k-1})},
$$




$$
\kappa_r=
\gcd\left(
\ell_r^{\mathrm{row}}u_r,\,
\frac{\ell_r^{\mathrm{row}}E_{r0}}{\Lambda_k},
\ldots,
\frac{\ell_r^{\mathrm{row}}E_{r,k-1}}{\Lambda_k}
\right).
$$


With the actual subsequent column contents $\gamma_j$, the paid multiplier is still


$$
T_k^{\mathrm{paid}}
=
\frac{\prod_r d_{k+r}\ell_r^{\mathrm{row}}}
{\prod_r\kappa_r\prod_j\gamma_j}.
\tag{10.7}
$$


None of these quantities is evaluated by a real integral comparison. After every legitimate route, the final primitive pair remains the pair obtained from the original $H_k/G_k$.

### 10.3 Separate binary producer

No compact estimate is transferred to the separate binary construction. Its original data remain


$$
b=9^{18+32u},\qquad n=4002b,
$$


with contact indices $0,\ldots,b-1$, physical reconstruction indices $0,\ldots,b$, and


$$
z_b=0.
$$



Its complete corrected columns remain


$$
x=\frac12RA^{-1}f,
\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad
x=2^ax_0,
\tag{10.8}
$$


and its complete return remains


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f.
\tag{10.9}
$$


The paid valuation statement is still only


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
\tag{10.10}
$$


The subtraction of $a$, the forcing $h^F$, the correction $e_0$, the factor $4b!$, and the physical terminal are all retained.

Its norm $x_0^Tx_0$, corrected-column contents, least simultaneous clearer, actual primitive denominator, and final all-prime gcd are not replaced by compact quantities.

---

## 11. Finite arithmetic and final proof status

### 11.1 Supplied reference receipt

The supplied reference receipt reports PASS for $k=1,\ldots,10$:

- $D_k=((2k+2i+2j)!)$;
- the lower bound $B_k$;
- the ordinary Laguerre determinant product;
- the elementary cutoff and positive-margin checks.

Its maximal reference factorial is $56!$. The separate Laguerre Gram check at $k=10$ uses factorials only through $47!$.

I do not rerun these matrices. Their role is limited to finite normalization support. The infinite theorem follows from the proofs in Sections 4–6, not from extrapolation of the receipt.

### 11.2 Bounded calculation available for coordinator inspection

No further matrix computation is needed for the analytic theorem.

If a separately authored constant certificate is desired, the only new bounded arithmetic to inspect is the logarithm bracket in Section 8:

- **Inputs:** $T=10^{16}$; $(r,N)=(3,15)$ and $(5,11)$; the 26 integer quotients in (8.4); the explicit geometric tail bounds (8.3).
- **Expected outputs:**
  

$$
F(3,15)=6\,931\,471\,805\,599\,445,
$$


  

$$
F(5,11)=4\,054\,651\,081\,081\,639,
$$


  tail bounds $<2/T$ and $<1/T$, the rational intervals (8.5)–(8.6), and the signed integer residuals
  

$$
28\,874\,954\,252\,168,\qquad
  -109\,258\,711\,829\,850.
$$


- **Scope:** certification of the displayed threshold bracket only. It says nothing about any content, final gcd, or original-index asymptotic.

No repetition of the closed original compact $k=5$, $k=32$, $k=81$, prefix-return, or other expensive arrays is requested.

## Final conclusion

The coordinator’s same-$H$ analytic candidate survives this full proof audit. The newly audited result is


$$
M_y\succeq \frac1{32}D_k
\qquad(k\ge512),
$$


with the complete overlap, actual negative atom, entire low reference cutoff, and original factorial terminal retained. The evaluated determinant comparison then gives


$$
\log|H_k(e+\pi)|
\ge
4k^2\log k+
\left(15\log2-\frac92\log3\right)k^2+o(k^2).
$$



The exact now-sufficient arithmetic target is an upper bound on the **actual** final gcd: both original odd-content descents, together with an actual binary coefficient below $A_*$, suffice. The convenient coefficient $A=3$ has a rigorously positive margin.

That arithmetic target remains open. In particular, no lower binary divisor, capped $3$-adic spectrum, local inverse, weighted-stack certificate, or finite receipt supplies the missing all-prime upper control.

Thus the report proves a stronger unconditional analytic lower bound and a sharper conditional retirement theorem for the unchanged compact producer. It proves **neither rationality nor irrationality of $e+\pi$**.
