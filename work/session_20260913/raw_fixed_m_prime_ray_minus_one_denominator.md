> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fixed odd-m extension: exact primitive denominator depth at n=mp^nu-1

Date: 2026-09-13. Original bounded arithmetic continuation by
audit_computations. No new canonical degree, matrix solve, or numerical
scan is used. The finite Cauchy seed is derived symbolically.

## 1. The theorem and its exact residual seed

Let $m\ge1$ be odd, let $p>3m$ be prime, and let $\nu\ge1$.
Put



$$
T=p^\nu,\qquad n=mT-1,\qquad
 r_p=\frac{m(T-1)}{p-1}.
\tag{1}
$$



Thus $n$ is even and $p\mid n+1$, while $p\nmid n$.
Use the actual canonical primitive denominator



$$
q_n=|Z_n|/\gcd(|Z_n|,|N_n|),\quad
 Z_n=\widehat Q_n(1),\quad
 N_n=\widehat P_e(1)+4\widehat P_a(1).
\tag{2}
$$



All three dual polynomials are globally integral, in the fixed
primitive-cofactor normalization of the passed endpoint notes.

**Theorem.** The ordinary normalized cofactor content $\Theta$ is a
$p$-unit, and the actual gate variables satisfy



$$
\boxed{d_p+e_p=\nu,\qquad
 v_p(q_n)=r_p-\nu+\kappa_p,\qquad\kappa_p\ge0.}
\tag{3}
$$



Here $d_p=v_p(h/\Theta)$,
$e_p=v_p(\widehat P_e(1))$, and $\kappa_p=v_p(K/\Theta)$
are the exact quantities in Section 2, with $K\ne0$. In particular,



$$
\boxed{v_p(q_n)\ge\frac{m(p^\nu-1)}{p-1}-\nu.}
\tag{4}
$$



Let $Q_j$ denote the monic raw imaginary-Legendre polynomial for
$\mathcal L(t^k)=\tau_{k+1}$. The finite seed criterion is



$$
\boxed{\kappa_p=0
 \ \Longleftrightarrow\ Q_{m-1}(1)\not\equiv0\pmod p.}
\tag{5}
$$



Every denominator in this seed is a $p$-unit. If the seed vanishes,
$\kappa_p\ge1$; that improves (4), rather than obstructing its
lower bound. The precise higher valuation of $K$ is not determined
by the seed's first residue alone.

For example, $m=5,p=17$ satisfies $p>3m$, while
$Q_4(1)=68/35\equiv0\pmod{17}$. Thus for every $\nu\ge1$,



$$
v_{17}(q_{5\cdot17^\nu-1})
 \ge\frac{5(17^\nu-1)}{16}-\nu+1.
\tag{6}
$$



This example is an exact degree-four seed evaluation, not a new
large-degree computation.

## 2. Actual integer matrices and normalization

Put $L=\operatorname{lcm}(1,\ldots,3n)$. The integer matrix is



$$
\mathsf Z_{rj}=L\sum_{s=0}^n(-1)^s\binom ns
 (n+r+1)_s^{\rm rise}\tau_{n+r+s-j},
 \quad0\le r\le n,\quad0\le j<n.
\tag{7}
$$



All Taylor indices are positive and at most $3n$. Define



$$
\delta_r=\det\mathsf Z[\widehat r,:],\quad
 \Theta=\gcd_r|\delta_r|,\quad
 c_r=(2n)!/(n+r)!,\quad h=\gcd_r|c_r\delta_r|,
 \quad R=(2n)!/n!.
\tag{8}
$$



The proved cofactor and endpoint identities, with their full scales, are



$$
V_r=(-1)^{n+r}c_r\delta_r/h,\qquad
 V(t)=\sum_{r=0}^nV_rt^r\in\mathbb Z[t],
$$




$$
v_r=\sum_{s=0}^n(-1)^s\binom ns(n+r+1)_s^{\rm rise},
 \quad K=\sum_{r=0}^n(-1)^r\delta_rv_r,
 \quad hZ_n=RK.
\tag{9}
$$



These are the actual primitive Rodrigues polynomial and endpoint,
not freely rescaled representatives. Also $\Theta\mid h\mid R\Theta$.

The square pure Cauchy matrix and its added last rows are denoted



$$
C_{rj}=L\tau_{n+r-j},\quad0\le j<n,
\tag{10}
$$



with row indices indicated explicitly below. Let $C_0$ consist of
rows $0,\ldots,n-1$, and $C^+$ of rows $0,\ldots,n$.
We also use row $C_{n+1,:}$, whose indices remain at most $3n$.

## 3. The residue blocks of the pure Cauchy matrix

Since $3m<p$, $v_p(L)=\nu$. A Taylor entry is nonzero modulo
$p$ only when its index is an odd multiple $hT$. Every such
$h$ here is positive and less than $3m<p$. Put



$$
\lambda=(L/T)(-1)^{(T-1)/2}\in\mathbb Z_p^\times.
$$



Then $L\tau_{hT}\equiv\lambda\tau_h\pmod p$. Thus the support
of $C\bmod p$ is $r-j\equiv1\pmod T$.

For each column residue $j_0=0,\ldots,T-2$, write
$j=j_0+bT$, $0\le b<m$. The associated rows of $C^+$ are
$r=j_0+1+aT$, $0\le a<m$. After division by $\lambda$,
the block is



$$
D_m=(\tau_{m+a-b})_{0\le a,b<m}.
\tag{11}
$$



Reversing its columns gives the ordinary moment Gram matrix
$(\tau_{a+b+1})$. Its even and odd parity blocks are Cauchy
matrices; all denominators and all nonzero row and column differences
are units because $p>3m$. Therefore $D_m$ is invertible modulo
$p$.

The last column residue $T-1$ has only $m-1$ columns
$j=T-1+bT$, $0\le b<m-1$. Its associated rows are
$r=aT$, $0\le a<m$, and its block is



$$
E_m=(\tau_{m-1+a-b})_{0\le a<m,\ 0\le b<m-1}.
\tag{12}
$$



After reversing columns, this is
$(\tau_{a+b+1})_{0\le a<m,\ 0\le b<m-1}$. Let



$$
Q_{m-1}(t)=\sum_{a=0}^{m-1}u_at^a.
\tag{13}
$$



Its coefficients are $p$-integral, $u_0$ is a unit, and
$u_a=0$ for odd $a$. These follow from the exact Legendre
coefficients with factorial arguments at most $2m-2<p$, and the
fact that $m-1$ is even. The block (12) has full column rank and
left kernel $(u_a)$; deleting its row 0 gives a unit square minor.
Thus the minor of $C^+$ deleting its overall row 0 is a unit.

For the square matrix $C_0$, one additional row is absent: row
$n=mT-1$. This removes the last row of the block with column residue
$T-2$. That block has $m-1$ rows and $m$ columns, with
right-null coordinates $u_{m-1-b}$ in column
$j=(b+1)T-2$. All other square blocks remain invertible. Therefore



$$
\operatorname{rank}_{\mathbb F_p}C_0=n-1.
\tag{14}
$$



Its left-null vector $\ell$ is supported on rows $r=aT$, with
coordinates $u_a$. Its right-null vector $b$ is supported on
columns $j=(b_0+1)T-2$, with coordinates $u_{m-1-b_0}$.
Only even $a,b_0$ occur. The apparent reuse of the letter $b$ for
the vector and $b_0$ for its residue-block index is separated here
to keep the actual column positions explicit.

The zero-dimensional blocks when $m=1$ have the same interpretation:
the left-null row is 0, the right-null column is $n-1$, and
$Q_0=1$.

## 4. Actual cofactor rank and the finite endpoint seed

Let $G$ be the unit upper-bidiagonal $(n+1)$-by-$(n+1)$
matrix whose rows $r<n$ subtract $(n+r+1)$ times row $r+1$,
and whose last row is unchanged. The exact Pascal identity gives



$$
(G\mathsf Z)_{r,:}\equiv C_{r,:}\pmod p
 \quad(0\le r<n),
\tag{15}
$$



because the resulting difference exponent is $n+1=mT$.

For the last row, terms of (7) with $s\ge p$ are divisible by
$p$. For $s<p$, the two signs cancel in
$(-1)^s\binom ns\equiv1$; its rising factorial is
$(-1)_s^{\rm rise}$ modulo $p$, since $r=n$. Thus only
$s=0,1$ remain and



$$
(G\mathsf Z)_{n,:}=\mathsf Z_{n,:}
 \equiv C_{n,:}-C_{n+1,:}\pmod p.
\tag{16}
$$



The row $C_n$ fills the missing row of the block (11), so it has
nonzero pairing with the right-null vector of $C_0$. Row
$C_{n+1}$, whose row residue is 0, is supported only on column
residue $T-1$. It therefore has zero pairing with that vector,
which is supported on column residue $T-2$. Equations (14)--(16)
prove



$$
\operatorname{rank}_{\mathbb F_p}\mathsf Z=n.
\tag{17}
$$



The left-null vector of $G\mathsf Z$ is $(\ell,0)$. Multiplying
by $G^{\mathsf T}$ does not change it modulo $p$: its only
nonzero row indices are $aT$, and the coefficient of the shifted
coordinate is $-(n+aT+1)=-(m+a)T$, divisible by $p$.
Consequently the signed cofactor vector of $\mathsf Z$ has the
same support and ratios:



$$
\boxed{\delta_0\in\mathbb Z_p^\times,\quad
 \frac{\delta_{aT}}{\delta_0}\equiv\frac{u_a}{u_0}\pmod p
 \ (a\text{ even}),\quad
 \delta_r\equiv0\pmod p\text{ otherwise}.}
\tag{18}
$$



No sign is omitted: the signed cofactor coordinate is
$(-1)^r\delta_r$, and $r=aT$ is even on the support.
Thus $\Theta$ is a unit. On that support $r\equiv0\pmod p$,
so the endpoint row in (9) has $v_r\equiv1\pmod p$. Therefore



$$
\boxed{\frac K{\delta_0}\equiv
 \frac{Q_{m-1}(1)}{Q_{m-1}(0)}\pmod p.}
\tag{19}
$$



This proves the finite criterion (5). Each supported $r=aT<n$
also has $p\mid c_r$, since the first factor in $c_r$ is
$n+r+1=(m+a)T$. All other minors are divisible by $p$, so



$$
d_p=v_p(h)\ge1.
\tag{20}
$$



## 5. The exact determinant depth survives the block correction

Let $Y$ consist of the first $n$ rows of $G\mathsf Z$.
The same exact row-difference and Cauchy--Binet identities as in the
prime-power-minus-one proof give



$$
Y=C_0+TE,\quad E\in\operatorname{Mat}_n(\mathbb Z),
 \qquad\det Y=hV(1).
\tag{21}
$$



The pure Cauchy determinant has valuation exactly $\nu$. Indeed,
the deleting-row-0 minor of $C^+$ is a unit by Section 3. Its
cofactor ratio is $1/Q_n(0)$, where



$$
Q_n(0)=\binom n{n/2}/\binom{2n}n.
$$



The digits of $n/2$ are $(p-1)/2$ in the bottom $\nu$
positions and $(m-1)/2$ above them. There is no carry in doubling
it. Adding $n$ to itself has exactly $\nu$ carries; the top
digit $2m-1<p$ creates no further carry. Thus



$$
v_p(\det C_0)=\nu.
\tag{22}
$$



Modulo $p$, the adjugate of $C_0$ is a nonzero scalar multiple
of the outer product of its right- and left-null vectors. It suffices
to prove $E_{aT,(b_0+1)T-2}\equiv0\pmod p$ for even
$a,b_0\in\{0,\ldots,m-1\}$.

The exact summand in this entry is



$$
m(-1)^s(s-1)!\binom n{s-1}
 \binom{n+aT+s}s\,L\tau_{(m+a-b_0-1)T+s+1},
 \quad 1\le s\le n+1.
\tag{23}
$$



For $s<p$, the second binomial contains the factor
$(m+a)T$ once and has valuation $\nu$, because
$1\le m+a<2m<p$. The Taylor factor has valuation at least
$\nu-1$ if nonzero: its index is $hT+s+1$, with even
$0\le h\le2m-2$, and $s+1\le p$. When $\nu=1$ and
$s=p-1$, the remaining multiplier $h+1\le2m-1<p$ is a unit;
there is no hidden extra denominator. Thus these terms are divisible
by $p$.

For $s=p$, the Taylor index is even, because both $hT$ and
$p+1$ are even. For $s>p$, $(s-1)!$ supplies a factor of
$p$, with every other factor integral. This proves the required
entrywise vanishing on the two null channels.

The linear determinant correction
$T\operatorname{tr}(\operatorname{adj}(C_0)E)$ is therefore
divisible by $p^{\nu+1}$, as are all corrections of order at least
two. Hence



$$
\boxed{\det Y\equiv\det C_0\pmod{p^{\nu+1}},\qquad
 d_p+v_p(V(1))=\nu.}
\tag{24}
$$



The full modulus in (24) is essential; a congruence only modulo
$p^\nu$ would not identify the valuation.

## 6. The exponential numerator and actual endpoint gcd

The general integral-border identity and its exact congruence give



$$
\widehat P_e(1)=\sum_rV_rD_{n,r},\qquad
 D_{n,r}\equiv1\pmod{n+1}.
\tag{25}
$$



By (20), (24), $v_p(V(1))=\nu-d_p<\nu$. Consequently



$$
\boxed{e_p=\nu-d_p,\qquad d_p+e_p=\nu.}
\tag{26}
$$



The factorial digit sums give $v_p(R)=r_p$. Equations (9),
(19), and (26) therefore imply



$$
v_p(Z_n)=r_p-d_p+\kappa_p.
\tag{27}
$$



The actual arctangent numerator bound, with no additional seed
assumption, is



$$
v_p(\widehat P_a(1))\ge r_p-d_p-\nu.
\tag{28}
$$



If $\nu\ge2$, then
$r_p=m(1+p+\cdots+p^{\nu-1})>2\nu$, because $p>3m\ge3$.
If $\nu=1,m\ge3$, then $r_p=m>2$. In both cases (28) is
strictly greater than $e_p=\nu-d_p$. Since 4 is a $p$-unit,
$v_p(N_n)=e_p$, and actual gcd reduction gives exactly



$$
v_p(q_n)=r_p-\nu+\kappa_p.
\tag{29}
$$



The remaining case is $m=1,\nu=1$. Here $d_p=1$ by (24),
the seed $Q_0(1)=1$ gives $\kappa_p=0$, and (27) says $Z_n$
is a unit. Thus $v_p(q_n)=0=r_p-\nu+\kappa_p$ without any
numerator cancellation assumption. This proves (3)--(4) in every case.

## 7. Scope of the seed and the next extension

The previously proved saturation theorem concerns $n=mp^\nu$,
where $p\mid n$, and has a different cofactor normalization
mechanism. This theorem concerns $n=mp^\nu-1$, where $p\mid n+1$.
Neither theorem is substituted for the other.

For fixed $m,p$ satisfying the hypotheses, the depth in (4) is
$n/(p-1)-O_{m,p}(\log n)$. The finite seed in (19) exactly decides
whether the nonnegative endpoint excess $\kappa_p$ is zero.
When the seed vanishes, no higher-depth equality is inferred from
its first residue; the unconditional lower bound (4) still holds.

This is not an all-even theorem for a fixed $p$, because it requires
the $p$-free part of $n+1$ to be the fixed odd integer $m<p/3$.
At larger $m$, the Cauchy seed denominators and differences can
vanish modulo $p$, and additional row and column blocks can become
singular. Those finite-rank and valuation changes must be analyzed
before extending the result. No numerical pattern is used to bypass
them.
