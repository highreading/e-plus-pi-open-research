> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact ternary factorial depth on the even subsequence n=3^nu-1

Date: 2026-09-13. Original bounded continuation by audit_computations.
Independent audit: **PASS** by audit_sources; see
raw_ternary_factorial_denominator_independent_review.md.
No new degree construction, canonical solve, or scan is used. The two
small base cases use only already saved exact triples.

## 1. Statement with the actual reduced denominator

For the canonical raw endpoint approximation, use the proved integral
dual normalization



$$
Z_n=\widehat Q_n(1),\qquad
 N_n=\widehat P_{e,n}(1)+4\widehat P_{a,n}(1),\qquad
 q_n=|Z_n|/\gcd(|Z_n|,|N_n|).
\tag{1}
$$



Here $\widehat P_e=[\widehat Q e^z]_{\le2n}$ and
$\widehat P_a=[\widehat Q\arctan z]_{\le2n}$ are globally integral.

**Theorem.** For every integer $\nu\ge1$,



$$
\boxed{n=3^\nu-1\quad\Longrightarrow\quad
 v_3(q_n)=\frac n2-\nu.}
\tag{2}
$$



The all-index argument below proves (2) directly for $\nu\ge3$.
The already saved exact cases $n=2,8$ prove the two remaining cases.
In fact the proof establishes the exact sufficient-gate identity



$$
\boxed{d_3+e_3=\nu,\qquad\kappa_3=0,}
\tag{3}
$$



where $d_3=v_3(h/\Theta)$,
$e_3=v_3(\widehat P_e(1))$, and
$\kappa_3=v_3(K/\Theta)$ are the actual quantities defined below.
Thus (3) is a logarithmic bound on an infinite family, not merely a
divisor of an unreduced clearing factor.

It does not prove the corresponding bound for all even indices, nor
the required fixed-prime bounds at 5, 7, or 11. Consequently it does not
by itself rule out shrinking of the full raw family or settle the
rationality of $e+\pi$.

## 2. The cofactor normalization and its reduction modulo 3

Put $T=3^\nu=n+1$ and $L=\operatorname{lcm}(1,\ldots,3n)$.
The normalized integer matrix is



$$
\mathsf Z_{rj}=L\sum_{s=0}^n(-1)^s\binom ns
 (n+r+1)_s^{\rm rise}\tau_{n+r+s-j},
 \quad0\le r\le n,\quad0\le j<n.
\tag{4}
$$



Here $\tau_k=(-1)^{(k-1)/2}/k$ at positive odd $k$, and zero at
positive even $k$. The sign in (4) uses that $n$ is even.
Define unsigned minors and positive contents



$$
\delta_r=\det\mathsf Z[\widehat r,:],\quad
 \Theta=\gcd_r|\delta_r|,\quad
 c_r=(2n)!/(n+r)!,\quad h=\gcd_r|c_r\delta_r|,
 \quad R=(2n)!/n!.
\tag{5}
$$



The previously proved cofactor transport gives the primitive integer
Rodrigues polynomial $V(t)=\sum_{r=0}^nV_rt^r$ by



$$
\boxed{V_r=(-1)^{n+r}c_r\delta_r/h.}
\tag{6}
$$



One can also check (6) by expanding
$W=t^n(t-1)^nV$ and comparing its coefficients with the original
primitive cofactor vector. This fixes the common scale, not just a
projective polynomial line.

Let



$$
v_r=\sum_{s=0}^n(-1)^s\binom ns(n+r+1)_s^{\rm rise},
 \qquad K=\sum_{r=0}^n(-1)^r\delta_rv_r.
\tag{7}
$$



The exact endpoint and content identities are



$$
hZ_n=RK,\qquad \Theta\mid h\mid R\Theta.
\tag{8}
$$



Now $v_3(L)=\nu$. The only positive odd index at most $3n<3T$
whose $L\tau$ value is a 3-unit is $T$. Put
$\lambda=L\tau_T\in\mathbb Z_3^\times$. For $s\ge3$, the
rising factorial in (4) is divisible by 3. Since $n\equiv-1\pmod3$,
the three remaining coefficients at $s=0,1,2$ are $1,r,r(r+1)$.
Consequently



$$
\lambda^{-1}\mathsf Z_{rj}
 \equiv\mathbf1_{j=r-1}+r\mathbf1_{j=r}
       +r(r+1)\mathbf1_{j=r+1}\pmod3.
\tag{9}
$$



Row 0 is zero. Rows $1,\ldots,n$ form an upper triangular square
matrix with diagonal $\lambda$. Therefore $\delta_0$ and
$\Theta$ are 3-units, while every $\delta_r$, $r>0$, is
divisible by 3. The same three-term reduction in (7) gives
$v_r\equiv(r+1)^2\pmod3$. Hence



$$
\boxed{v_3(K)=v_3(\Theta)=0,\qquad\kappa_3=0.}
\tag{10}
$$



All $c_r$ are integral, and $c_0=R$ is divisible by 3. Thus



$$
d_3=v_3(h)\ge1.
\tag{11}
$$



Legendre's factorial formula also gives



$$
v_3(R)=n/2,
\tag{12}
$$



because $n=T-1$ and $2n=2T-2$ both have ternary digit sum
$2\nu$.

## 3. An exact row difference changes the parameter n into n+1

Let $H$ be the $n$-by-$(n+1)$ bidiagonal matrix with
$H_{r,r}=1$ and $H_{r,r+1}=-(n+r+1)$, $0\le r<n$.
Set $Y=H\mathsf Z$. Pascal's identity, with all rising-factorial
factors retained, gives



$$
Y_{rj}=L\sum_{s=0}^{n+1}(-1)^s\binom{n+1}s
 (n+r+1)_s^{\rm rise}\tau_{n+r+s-j}.
\tag{13}
$$



The largest Taylor index here is $3n$, so $L\tau$ is integral
in every term. For $s\ge1$, the exact integer identity



$$
\binom{n+1}s(n+r+1)_s^{\rm rise}
 =(n+1)(s-1)!\binom n{s-1}\binom{n+r+s}s
\tag{14}
$$



shows that



$$
\boxed{Y=C+T E,\quad
 C_{rj}=L\tau_{n+r-j},\quad E\in\operatorname{Mat}_n(\mathbb Z).}
\tag{15}
$$



This congruence is modulo $n+1$, not the earlier congruence modulo
$n$; it therefore applies to the present family, where $3\nmid n$.

The maximal minors of $H$ are



$$
\det H[:,\widehat r]=(-1)^{n-r}c_r.
$$



Cauchy--Binet and (6) therefore give the exact determinant bridge



$$
\boxed{\det Y=\sum_{r=0}^n(-1)^{n-r}c_r\delta_r=hV(1).}
\tag{16}
$$



No appended endpoint row is discarded, and no untracked common factor
is introduced in (16).

## 4. The Cauchy determinant and its only possible first correction

First, $v_3(\det C)=\nu$. Here is a direct proof including the
normalization. Adjoin to $C$ the row indexed by $r=n$, obtaining
the rectangular pure Cauchy matrix $C^+$. Its reduction modulo 3 has
only the entries $\lambda\mathbf1_{j=r-1}$. Its minor deleting
row 0 is a unit.

After reversing the columns, $C^+$ is the moment matrix
$L\mathcal L(t^{r+j})$, with
$\mathcal L(t^k)=\tau_{k+1}$. Its left kernel is the coefficient
vector of the monic raw imaginary-Legendre polynomial $Q_n$.
The ratio of the minors deleting rows $n$ and 0 is therefore
$1/Q_n(0)$, since $n$ is even. The exact constant term is



$$
Q_n(0)=\frac{\binom n{n/2}}{\binom{2n}n}.
\tag{17}
$$



The numerator is a 3-unit: $n/2$ has all ternary digits one, so its
addition to itself has no carry. The denominator has valuation $\nu$,
as follows either from the $\nu$ carries or the digit sums used in
(12). Thus $v_3(Q_n(0))=-\nu$, and the unit deleting-row-0 minor
proves



$$
\boxed{v_3(\det C)=\nu.}
\tag{18}
$$



The reduction of the square $C$ has zero row 0, zero last column,
and $\lambda$ at $(r,r-1)$, $1\le r<n$. Therefore its
adjugate modulo 3 has only one potentially nonzero entry, at
$(n-1,0)$. It remains to examine $E_{0,n-1}$.

From (13)--(15),



$$
E_{0,n-1}=L\sum_{s=1}^{T}(-1)^s(s-1)!
 \binom{T-1}{s-1}\binom{T-1+s}s\tau_{s+1}.
\tag{19}
$$



Terms $s=1,3$ vanish because the Taylor indices are even. Every
$s\ge4$ term is divisible by 3 through $(s-1)!$, with all
remaining factors integral. The $s=2$ term has valuation at least



$$
v_3\left(T(T+1)/2\right)+v_3(L\tau_3)
 =\nu+(\nu-1)=2\nu-1\ge1.
$$



Hence



$$
E_{0,n-1}\equiv0\pmod3.
\tag{20}
$$



Expand the determinant of $C+TE$ multilinearly. Terms using two or
more entries from $TE$ are divisible by $3^{2\nu}$, hence by
$3^{\nu+1}$. The linear term is
$T\operatorname{tr}(\operatorname{adj}(C)E)$, which is also
divisible by $3^{\nu+1}$, by the support of the adjugate and (20).
Thus



$$
\boxed{\det Y\equiv\det C\pmod{3^{\nu+1}},\qquad
 v_3(\det Y)=\nu.}
\tag{21}
$$



Combining (16), (18)--(21), and $v_3(\Theta)=0$ proves the exact
balance



$$
\boxed{d_3+v_3(V(1))=\nu.}
\tag{22}
$$



In particular $V(1)\ne0$, and $1\le d_3\le\nu$. This is
obtained without extrapolating the first cofactor layer or asserting
an unproved recursive inverse pattern.

## 5. The exponential border has the same valuation

The passed integral endpoint-border identity gives



$$
\widehat P_e(1)=\sum_{r=0}^nV_rD_{n,r},\qquad
 D_{n,r}=\sum_{j=0}^{n+r}\binom{n+j}j(n+r)_j.
\tag{23}
$$



For every $n,r$, not only this family, its nonconstant terms satisfy



$$
\binom{n+j}j(n+r)_j
 =(n+1)(j-1)!\binom{n+j}{j-1}\binom{n+r}j
 \quad(j\ge1).
\tag{24}
$$



Consequently $D_{n,r}\equiv1\pmod{n+1}$. The coefficients $V_r$
are integers, so



$$
\widehat P_e(1)\equiv V(1)\pmod T.
\tag{25}
$$



By (11), (22), $v_3(V(1))=\nu-d_3<\nu$. Equation (25) therefore
forces



$$
\boxed{e_3=v_3(\widehat P_e(1))=\nu-d_3.}
\tag{26}
$$



This proves (3), including the absence of an unbounded signed
exponential-border cancellation on this subsequence.

## 6. Passing to the actual endpoint gcd

Equations (8), (10), and (12) give



$$
v_3(Z_n)=n/2-d_3.
\tag{27}
$$



The passed arctangent valuation bound retains its exact denominator
loss $\lfloor\log_3(2n)\rfloor=\nu$:



$$
v_3(\widehat P_a(1))\ge n/2-d_3-\nu.
\tag{28}
$$



For $\nu\ge3$, $n/2>2\nu$. The right side of (28) is then
strictly larger than $e_3=\nu-d_3$. Multiplication by 4 is a 3-unit,
so no equality-of-valuations cancellation is possible in (1):



$$
v_3(N_n)=\nu-d_3,
\qquad
 v_3(q_n)=v_3(Z_n)-v_3(N_n)=n/2-\nu.
\tag{29}
$$



The difference is positive. This proves (2) for all $\nu\ge3$.

The remaining $\nu=1,2$ correspond to the already saved degrees
$n=2,8$. Their exact canonical endpoint sums, reduced by their exact
gcd, have respectively $v_3(q_2)=0$ and $v_3(q_8)=2$. These are
recorded in raw_fixed_prime_denominator_cached_checks.json, reconstructed
independently in raw_fixed_prime_gate_independent_checks.json from
raw_accessory_scaling_probe.json, keys cases/exact_polynomial_input/A,B.
No new solve is used. They equal $n/2-\nu$, completing the finite
base cases of the theorem.

## 7. What this closes and what it leaves

The proof closes the proposed $p=3$ factorial-depth estimate on a
specific infinite family of even indices, with the exact logarithmic
loss $\nu$. It also proves the new general congruence
$\widehat P_e(1)\equiv V(1)\pmod{n+1}$, from (23)--(24).

The key mechanism is the exact row difference (13), which replaces
the exponent $n$ by $n+1$ and exposes a single Cauchy adjugate
coordinate. It is distinct from the saturation argument at primes
dividing $n$, and from the separate Appell congruence modulo $2n$.

Combining (2) with the proved dyadic formula gives, on this subsequence,
$\log q_n/n\ge(3/2)\log2+(1/2)\log3-o(1)$. This is a genuine
bound for the primitive denominator, but is insufficient by itself to
exclude shrinking at the known exponential approximation-error rate.
Extensions to all even indices or to further fixed primes require new
control of the corresponding row-difference and adjugate coordinates.
