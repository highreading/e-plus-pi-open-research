> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual primitive-dual endpoint scalar from a bordered Cauchy determinant

Date: 2026-09-13. Original bounded continuation by audit_sources.
Independent review passed: raw_endpoint_scalar_cauchy_independent_review.md.

This note handles the separate scalar $Z_n=\widehat Q_n(1)$ in the actual identity
$\mathcal E_n=(-1)^nF_nZ_n$. It does not replace that scalar by the extremal content. Its main infinite-family result is:


$$
\boxed{
n=mp^\nu,\quad \nu\ge1,\quad p\ {\rm odd},\quad 3m<p,\quad
Q_m(1)\not\equiv0\pmod p
\ \Longrightarrow\
v_p(Z_n)=\frac{n-m}{p-1}.
}
\tag{1}
$$


Here $p\nmid m$ follows from $3m<p$, and $Q_m$ is the monic raw Legendre polynomial for the imaginary-segment moment functional. In particular (1) holds for every $n=p^\nu$, $p>3$. On this family the normalized simultaneous denominator $\widehat Q_n/Z_n$ is $p$-integral and reduces to $z^n$.

The exact reduction also shows why saturation alone is insufficient for all $m$: $Q_4(1)=68/35$, so the saturated family $n=4\cdot17^\nu$ has an extra factor of 17 in its normalized simultaneous endpoint denominator. No numerical degree or prime scan is used.

## 1. Actual normalization and reviewed dependencies

The actual extremal matrix $X_n$ has rows $k=n,\ldots,3n$, columns $B_j,C_j$, $0\le j<n$, and entries


$$
(X_n)_{k,B_j}=(k)_j,\qquad
(X_n)_{k,C_j}=k!\tau_{k-j},\qquad
\tau_a=[z^a]\arctan z.
$$


Let


$$
u_k=(-1)^{k-n}\det X_n[\widehat k],\qquad
F_n=\gcd_k|u_k|>0,\qquad w_k=u_k/F_n.
$$


The reviewed primitive-dual normalization is


$$
\widehat Q_n(z)=\sum_{k=n}^{3n}\frac{k!}{n!}w_kz^{3n-k},
\quad Z_n=\widehat Q_n(1),\quad
\mathcal E_n=(-1)^nF_nZ_n.
\tag{2}
$$


These are exactly the objects in raw_extremal_dual_polynomial_and_content_identity.md. The name raw_endpoint_primitive_dual_factorization was not present in the project inventory; the cited reviewed note contains the actual factorization and endpoint coordinate change.

Retain the integer difference matrix


$$
G_{rj}=\sum_{s=0}^n(-1)^{n-s}\binom ns
(n+r+s)!\tau_{n+r+s-j},
\quad0\le r\le n,\quad0\le j<n.
$$


To avoid confusing an integer matrix with the scalar $Z_n$, write


$$
\mathsf Z_{rj}=\frac{L}{(n+r)!}G_{rj},
\quad L=\operatorname{lcm}(1,\ldots,3n).
$$


Set


$$
\delta_r=\det\mathsf Z[\widehat r,:],\quad
\Theta_n=\gcd_r|\delta_r|,\quad
c_r=\frac{(2n)!}{(n+r)!},\quad
h_n=\gcd_r|c_r\delta_r|,\quad
R_n=\frac{(2n)!}{n!}.
\tag{3}
$$


Both contents are positive. The exact weighted-minor identity already proved in raw_extremal_smooth_divisor_and_prime_power_saturation.md is


$$
F_n=\left(\prod_{j=0}^{n-1}j!\right)
\frac{\prod_{r=0}^{n-1}(n+r)!}{L^n}\,h_n.
\tag{4}
$$


In particular $\Theta_n\mid h_n$, but their small-prime valuations cannot generally be equated.

## 2. Exact cofactor transport, including its sign

Let $U$ be the unimodular row transformation keeping the first $n$ rows of $X_n$ and taking the consecutive $n$-th differences for the remaining $n+1$ rows. Then


$$
UX_n=\begin{pmatrix}V&C_0\\0&G\end{pmatrix},
\qquad \det U=1,\qquad \det V=\prod_{j=0}^{n-1}j!>0.
$$


Signed cofactor vectors transform by $u'=U^{-T}u$. The top $n$ coordinates of $u'$ are zero. Its bottom coordinate $r$ is


$$
u'_{n+r}=(-1)^{n+r}\det V\,\det G[\widehat r].
$$


Dividing by (4), with the exact row-factor identity for $\det G[\widehat r]$, gives


$$
w'_{n+r}=(-1)^{n+r}\frac{c_r\delta_r}{h_n}.
$$


Since $w=U^Tw'$, the original coordinate with $k=n+t$ is


$$
\boxed{
w_{n+t}=\frac{(-1)^t}{h_n}
\sum_{\substack{0\le r\le n\\0\le t-r\le n}}
\binom n{t-r}c_r\delta_r,\qquad0\le t\le2n.
}
\tag{5}
$$


This identity does not rescale the primitive left vector or the chosen endpoint pair.

Define the integer polynomial


$$
\mathscr P_n(z)=
\sum_{r=0}^n\sum_{s=0}^n
(-1)^{r+s}\binom ns\,\delta_r
\frac{(n+r+s)!}{(n+r)!}\,z^{2n-r-s}.
\tag{6}
$$


Substituting (5) into (2) yields the exact polynomial identity


$$
\boxed{h_n\widehat Q_n(z)=R_n\mathscr P_n(z).}
\tag{7}
$$


Every exponent in (6) is nonnegative and every coefficient multiplier is integral.

The coefficient content of $\mathscr P_n$ is precisely $\Theta_n$. One divisibility follows because every coefficient is an integer combination of the $\delta_r$. For the reverse divisibility, the first $n+1$ coefficients, indexed by powers $z^{2n-t}$, $0\le t\le n$, are


$$
(-1)^t\delta_t
+\sum_{r<t}(-1)^t\binom n{t-r}\delta_r
\frac{(n+t)!}{(n+r)!}.
$$


This is an integer triangular transformation of $(\delta_0,\ldots,\delta_n)$, with diagonal entries $(-1)^t$. Its inverse is integral. Consequently, if $c_n^Q$ denotes the coefficient content of the actual integer polynomial $\widehat Q_n$, then


$$
\boxed{
c_n^Q=\frac{R_n\Theta_n}{h_n},\qquad
\frac{h_n}{\Theta_n}\mid R_n.
}
\tag{8}
$$


The first equality can first be read in positive rational contents; integrality of $c_n^Q$, already guaranteed by (2), proves the stated integer divisibility.

## 3. A single exact bordered determinant for the endpoint

Put


$$
v_r=\sum_{s=0}^n(-1)^s\binom ns
\frac{(n+r+s)!}{(n+r)!},
\qquad
K_n=\mathscr P_n(1)=\sum_{r=0}^n(-1)^r\delta_r v_r.
$$


Laplace expansion along the last column gives


$$
\boxed{
K_n=(-1)^n\det[\mathsf Z\mid v],\quad
h_n Z_n=R_nK_n,\quad
d_n^{II}=\frac{|K_n|}{\Theta_n}.
}
\tag{9}
$$


Here $d_n^{II}$ is the least positive denominator making all coefficients of the actual normalized simultaneous polynomial


$$
S_0(z)=\widehat Q_n(z)/Z_n
$$


integral. The last formula follows from (8) and the reviewed equality $d_n^{II}=|Z_n|/c_n^Q$. Since $\Theta_n\mid K_n$, its right side is an integer.

The nonvanishing $K_n\ne0$ follows from the known nonzero actual endpoint determinant in (2). It is not inferred from a sign for the newly bordered matrix.

Equation (9) is a restriction of an explicit integer functional $v$ to the primitive left kernel of $\mathsf Z$. It retains the endpoint information that the maximal-minor content alone does not contain.

## 4. An exact congruence modulo the entire degree

For $s\ge1$,


$$
\binom ns\frac{(n+r+s)!}{(n+r)!}
=n(s-1)!\binom{n-1}{s-1}\binom{n+r+s}{s}.
\tag{10}
$$


Thus every positive-$s$ summand in (6) is divisible by $n$. Therefore


$$
\boxed{
\mathscr P_n(z)\equiv
\sum_{r=0}^n(-1)^r\delta_r z^{2n-r}\pmod n,
\qquad v_r\equiv1\pmod n.
}
\tag{11}
$$


Let $\mathsf C_{rj}=L\tau_{n+r-j}$. The same identity gives
$\mathsf Z\equiv(-1)^n\mathsf C\pmod n$. Consequently


$$
\boxed{K_n\equiv\det[\mathsf C\mid\mathbf1]\pmod n.}
\tag{12}
$$


The signs cancel: the first $n$ columns contribute $(-1)^{n^2}=(-1)^n$, and (9) contributes another $(-1)^n$.

This remaining bordered determinant has a closed rational evaluation that is an integer:


$$
\boxed{
\det[\mathsf C\mid\mathbf1]
=L^n\left(\prod_{j=0}^{n-1}|h_j^{\rm Leg}|\right)Q_n(1),
\quad
h_j^{\rm Leg}
=\frac{(-1)^j4^j(j!)^4}{((2j)!)^2(2j+1)}.
}
\tag{13}
$$


To prove it, reverse the $n$ moment columns. This gives entries
$L\mathcal L(t^{r+j})$, where
$\mathcal L(t^a)=\tau_{a+1}$. The standard monic orthogonal-polynomial determinant, obtained directly by solving its $n$ moment equations, is the Hankel determinant times $Q_n(1)$. The Hankel determinant is $\prod h_j^{\rm Leg}$. The column-reversal sign $(-1)^{n(n-1)/2}$ cancels exactly the product of the signs of these norms. This proves (13) over $\mathbb Q$; its left side establishes its integrality, so no unjustified localization of the monic Legendre basis is used.

For any $p^\nu\mid n$, (12) determines $v_p(K_n)$ exactly whenever the right side of (13) has valuation less than $\nu$. Otherwise it supplies only a lower bound of $\nu$. It is not an upper bound at arbitrarily large depth.

## 5. The saturated family reduces the endpoint to a fixed-degree Legendre value

Suppose $n=mT$, $T=p^\nu$, $\nu\ge1$, $3m<p$. The exact Cauchy-block analysis in raw_extremal_cauchy_congruence_rank_and_depth.md proves:


$$
\delta_n\not\equiv0\pmod p,\qquad
\Theta_n,\ h_n\in\mathbb Z_p^\times.
\tag{14}
$$


For clarity, the part of that analysis needed here can be read directly. Since $v_p(L)=\nu$, the only nonzero entries of $\mathsf C\bmod p$ have $n+r-j=T\ell$, $\ell$ odd. The index is at most $2n=2mT<pT$. On these entries


$$
L\tau_{T\ell}
=\frac LT(-1)^{(T-1)/2}\tau_\ell\pmod p.
$$


Thus, after grouping indices modulo $T$, every block is a nonzero common scalar times a small moment matrix. The residue-0 block has rows $r=uT$, $0\le u\le m$, columns $j=vT$, $0\le v<m$, and entries


$$
\tau_{m+u-v}.
\tag{15}
$$


Every other residue block is square $m$-by-$m$ and invertible. The first $m$ rows of (15) are also invertible. This follows by parity separation into signed Cauchy matrices: all positive denominators and nonzero row/column differences have magnitude less than $p$. In particular the cofactor $\delta_n$ is a unit.

The signed vector $((-1)^r\delta_r)_r$ is a left annihilator of $\mathsf Z\bmod p$. Invertibility of the square blocks forces it to vanish outside $r=uT$. Within (15), the monic left-annihilating polynomial is exactly $Q_m(t)$: reversing the column order changes its equations to
$\mathcal L(t^jQ_m(t))=0$, $0\le j<m$.
All denominators needed for this fixed-degree moment argument are $p$-units because $p>3m>2m$. Writing $Q_m(t)=\sum_{u=0}^m q_ut^u$, $q_m=1$, gives


$$
(-1)^{uT}\delta_{uT}
=(-1)^n\delta_nq_u\pmod p.
\tag{16}
$$


Combining with (11),


$$
\boxed{
\mathscr P_n(z)\equiv
(-1)^n\delta_n z^{2n}Q_m(z^{-T})\pmod p,
\qquad
K_n\equiv(-1)^n\delta_nQ_m(1)\pmod p.
}
\tag{17}
$$


The apparent reciprocal expression in (17) is a polynomial, with lowest possible exponent $n$ and a unit coefficient at that exponent.

This gives the exact local separation of the two quantities:


$$
\boxed{
v_p(c_n^Q)=v_p(R_n)=\frac{n-m}{p-1},\qquad
v_p(Z_n)=\frac{n-m}{p-1}+v_p(K_n),\qquad
v_p(d_n^{II})=v_p(K_n).
}
\tag{18}
$$


Indeed $h_n,\Theta_n$ are units. The factorial evaluation follows from $2m<p$:


$$
v_p(n!)=\frac{n-m}{p-1},\qquad
v_p((2n)!)=\frac{2(n-m)}{p-1}.
$$


Thus (1) follows precisely when $Q_m(1)$ is a unit.

If it is a unit, the actual normalized simultaneous polynomial has the explicit reduction


$$
\boxed{
S_0(z)\equiv
\frac{z^{2n}Q_m(z^{-T})}{Q_m(1)}
\pmod p.
}
\tag{19}
$$


This congruence is meaningful coefficientwise over $\mathbb Z_p$, as (18) has already proved its integrality.

## 6. Two infinite-family consequences and a genuine limitation

For $m=1$, $Q_1(t)=t$, so every $p>3$ and $\nu\ge1$ satisfies


$$
\boxed{
v_p(Z_{p^\nu})=\frac{p^\nu-1}{p-1},\quad
v_p(c_{p^\nu}^Q)=\frac{p^\nu-1}{p-1},\quad
v_p(d_{p^\nu}^{II})=0,\quad
S_0(z)\equiv z^{p^\nu}\pmod p.
}
\tag{20}
$$


Combining with the already proved extremal-content valuation gives the actual endpoint determinant valuation


$$
v_p(\mathcal E_n)
=\frac{(2n+1)(n-1)}{p-1}-2\nu n,\qquad n=p^\nu.
\tag{21}
$$


More generally, if the unit condition in (1) holds, the corresponding exact formula is


$$
v_p(\mathcal E_n)
=\frac{(2n+1)(n-m)}{p-1}-2\nu n.
\tag{22}
$$



Saturation does not automatically force this unit condition. One exact symbolic diagnostic is enough:


$$
Q_4(t)=t^4+\frac67t^2+\frac3{35},\qquad Q_4(1)=\frac{68}{35}.
$$


For $m=4,\ p=17>3m$, equation (17) gives $K_n\equiv0\pmod{17}$ for every $n=4\cdot17^\nu$. Hence


$$
\boxed{
v_{17}(d_n^{II})\ge1,\qquad
v_{17}(Z_n)\ge\frac{n-4}{16}+1.
}
\tag{23}
$$


This is a proved infinite family, not a scan or a guessed valuation at the next depth. The exact higher valuation remains unresolved.

The cross-product interpretation remains the reviewed actual one:
$S_0=B_EC_F-C_EB_F$, where the high solutions have endpoints
$(B_E(1),C_E(1))=(1,0)$, $(B_F(1),C_F(1))=(0,1)$.
The actual selected $(1,4)$ solution is $T_E+4T_F$, and its cross product with $T_F$ gives the same $S_0$. Thus (19)–(20) concern this actual endpoint normalization. They do not assert that each individual type-I triple is $p$-integral, or identify $d_n^{II}$ with the primitive rational denominator in the linear form approximating $e+\pi$.

The useful remaining scalar is now completely explicit: $K_n/\Theta_n$, the last expression in (9). At saturated primes it is governed initially by $Q_m(1)$; beyond the known congruence depth its factorial-difference corrections must still be retained. Above $3n$, congruence modulo $n$ gives no automatic information. No estimate that resolves the main irrationality problem is claimed.
