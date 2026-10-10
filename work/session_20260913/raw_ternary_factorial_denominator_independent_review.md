> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the exact ternary denominator subsequence

Date: 2026-09-13. Reviewer: audit_sources.

**PASS.** The theorem and intermediate valuations in
raw_ternary_factorial_denominator_subsequence.md hold with the stated
original integral normalization. No mathematical correction is required.
The later extra-arctangent-power argument in Section 6 of
raw_prime_power_minus_one_denominator_extension.md has also passed
independent audit; it removes both frozen prefix cases as required
inputs to an all-index proof. See the addendum in
raw_prime_power_minus_one_independent_review.md.
The all-index argument gives, for $n=3^\nu-1$,


$$
d_3+e_3=\nu,\qquad\kappa_3=0.
$$


It proves the actual reduced-denominator formula


$$
\boxed{v_3(q_n)=n/2-\nu\qquad(\nu\ge1)}
$$


directly for $\nu\ge3$; the two independently rechecked frozen cases
$n=2,8$ complete the statement. There is no extrapolation from samples,
unproved lift of a rank calculation, or surviving unreduced content.

The audit read the entire target, the original cofactor-family note,
the fixed-prime primitive-denominator gate, and the endpoint Cauchy
normalization. It independently reconstructed the identities below.
The exact re-reduction of only the two saved original triples is in
raw_ternary_prefix_independent_checks.json. No new degree construction,
approximant solve, or prime scan was made.

## 1. Original scale and first residue layer

Write $T=3^\nu=n+1$, $L=\operatorname{lcm}(1,\ldots,3n)$,
$\delta_r=\det\mathsf Z[\widehat r,:]$ without alternating signs,


$$
c_r=\frac{(2n)!}{(n+r)!},\quad
 \Theta=\gcd_r|\delta_r|,\quad h=\gcd_r|c_r\delta_r|,\quad
 R=\frac{(2n)!}{n!}.
$$


The original primitive polynomial is
$V_r=(-1)^{n+r}c_r\delta_r/h$.
The factor $h$, not merely a projective coefficient line, occurs
in every later determinant identity. The target retains it correctly
and uses $hZ_n=RK$, $\Theta\mid h\mid R\Theta$ in the established
normalization.

Since $T\le3n<3T$, $v_3(L)=\nu$. Precisely the positive odd index
$T$ gives a unit $L\tau_k$; $2T$ is even and contributes zero.
Rising-factorial lengths at least three vanish modulo three.
The remaining coefficients reduce to $1,r,r(r+1)$, so


$$
\lambda^{-1}\mathsf Z_{rj}
 ={\bf1}_{j=r-1}+r{\bf1}_{j=r}
   +r(r+1){\bf1}_{j=r+1}\pmod3,\quad
 \lambda=L\tau_T\in\mathbb Z_3^\times.
$$


Row zero is zero; rows $1,\ldots,n$ form an upper triangular square
with diagonal $\lambda$. Therefore $\delta_0,\Theta$ are units
and all other $\delta_r$ vanish modulo three. Separately
$v_r\equiv1+r+r(r+1)=(r+1)^2$, so $K\equiv\delta_0\ne0$.
Thus $\kappa_3=0$ without a higher-depth assumption.

The factorial digit sums of $n$ and $2n$ are both $2\nu$,
giving $v_3(R)=n/2$. All $c_r\delta_r$ are divisible by three:
the zeroth uses $c_0=R$, and the others use their minors. Hence
$d_3=v_3(h)\ge1$, the strict inequality needed for the later
numerator lift.

## 2. Exact row difference and signed determinant

Let $H_{r,r}=1$, $H_{r,r+1}=-(n+r+1)$. In $Y=H\mathsf Z$,
the reindexed second summand has coefficient
$(-1)^s\binom n{s-1}(n+r+1)^{\overline s}$. It adds to the
first summand by Pascal's identity, giving binomial parameter $n+1$.
For $s\ge1$,


$$
\binom{n+1}s(n+r+1)^{\overline s}
 =(n+1)(s-1)!\binom n{s-1}\binom{n+r+s}s.
$$


All factors after $n+1$ are integers. The largest new Taylor index
is $3n$, at $r=n-1,j=0,s=n+1$. Thus $L$ still clears every
denominator and


$$
Y=C+TE,\qquad C_{rj}=L\tau_{n+r-j},\quad E\in M_n(\mathbb Z)
$$


is an exact integral decomposition.

Deleting column $r$ of $H$ leaves the diagonal ones before that
column and the superdiagonal product after it. Consequently


$$
\det H[:,\widehat r]
 =(-1)^{n-r}\prod_{j=r}^{n-1}(n+j+1)=(-1)^{n-r}c_r.
$$


Cauchy--Binet uses the same ordered deleted-row sets on $\mathsf Z$,
so there is no further permutation sign. As
$(-1)^{n-r}=(-1)^{n+r}$, the exact original-scale bridge is


$$
\boxed{\det Y=\sum_r(-1)^{n-r}c_r\delta_r=hV(1)}.
$$



## 3. Pure Cauchy valuation and the only first correction

Adjoin row $n$ to $C$. Its reduction is
$\lambda{\bf1}_{j=r-1}$, and the minor deleting row zero is a unit.
Reversing all columns gives the moment matrix
$L\mathcal L(t^{r+j})$, $\mathcal L(t^k)=\tau_{k+1}$.
The signed minors form a left kernel. Comparing the constant and
monic coefficients of the raw imaginary-Legendre polynomial yields


$$
\frac{\det C}{\det C^+[\widehat0,:]}=\frac1{Q_n(0)},\qquad
 Q_n(0)=\frac{\binom n{n/2}}{\binom{2n}n}.
$$


Here $n$ is even, and column reversal contributes the same sign to
both minors. The numerator binomial is a three-unit, since $n/2$
has every ternary digit one. The denominator has valuation $\nu$.
Therefore $v_3(Q_n(0))=-\nu$ and $v_3(\det C)=\nu$.
This rational identity does not assume integrality of the remaining
monic Legendre coefficients.

Modulo three, the square $C$ has zero row zero, zero last column,
and $\lambda$ at $(r,r-1)$. Its adjugate has only one possible
nonzero entry, at $(n-1,0)$, explicitly
$(-1)^{n-1}\lambda^{n-1}$. The first-order determinant term
therefore sees only


$$
E_{0,n-1}
 =L\sum_{s=1}^{T}(-1)^s(s-1)!
 \binom{T-1}{s-1}\binom{T-1+s}s\tau_{s+1}.
$$


Terms $s=1,3$ vanish by parity. Terms $s\ge4$ are divisible
by three through $(s-1)!$, grouping $L\tau_{s+1}$ as an integer.
At $s=2$ the second binomial has valuation $\nu$ and $L\tau_3$
has valuation $\nu-1$. Its valuation is at least $2\nu-1\ge1$.
Thus $E_{0,n-1}=0\pmod3$ for every $\nu\ge1$.

Terms of determinant degree at least two in $TE$ have valuation
at least $2\nu\ge\nu+1$, including $\nu=1$. The linear term
$T\operatorname{tr}(\operatorname{adj}C\,E)$ has the extra three
just proved. Hence


$$
\det Y\equiv\det C\pmod{3^{\nu+1}},\qquad
 v_3(hV(1))=\nu.
$$


The precision is one digit beyond the valuation of $\det C$, so
it excludes cancellation. In particular $1\le d_3\le\nu$ and
$v_3(V(1))=\nu-d_3$.

## 4. Integral numerator lift and the actual endpoint gcd

The original exponential border is


$$
\widehat P_e(1)=\sum_rV_rD_{n,r},\qquad
 D_{n,r}=\sum_{j=0}^{n+r}\binom{n+j}j(n+r)_{\underline j}.
$$


For $j\ge1$, direct factorial cancellation gives


$$
\binom{n+j}j(n+r)_{\underline j}
 =(n+1)(j-1)!\binom{n+j}{j-1}\binom{n+r}j.
$$


Thus $D_{n,r}\equiv1\pmod{n+1}$ for every $n,r$, and
$\widehat P_e(1)\equiv V(1)\pmod T$. The strict inequality
$\nu-d_3<\nu$ proves


$$
e_3=v_3(\widehat P_e(1))=\nu-d_3.
$$


The lift is applied to the actual integral primitive $V$;
there is no hidden cofactor rescaling.

The scalar identity with unit $K$ gives $v_3(Z_n)=n/2-d_3$.
The proved arctangent estimate retains its entire loss:


$$
v_3(\widehat P_a(1))\ge n/2-d_3-\nu,\qquad
 \lfloor\log_3(2n)\rfloor=\nu.
$$


For $\nu\ge3$, $n/2>2\nu$, so this is strictly deeper than
$e_3=\nu-d_3$. Since four is a unit, the actual numerator
$N_n=\widehat P_e(1)+4\widehat P_a(1)$ has exactly that valuation.
Taking the original endpoint gcd yields


$$
v_3(q_n)=(n/2-d_3)-(\nu-d_3)=n/2-\nu>0.
$$


The strict arctangent comparison is not asserted for the two smaller
indices.

## 5. Frozen prefix and scope

I independently summed the saved original coefficient arrays $A,B,C$
in raw_accessory_scaling_probe.json, using exact rational arithmetic
only for $n=2,8$. Both satisfy $C(1)=4B(1)$, and reducing
$-A(1)/B(1)$ gives


$$
q_2=16432,\qquad
 q_8=
 20724321309281294147345873943566640417894382678327987115681587154600279263123428741120.
$$


Their three-valuations are respectively zero and two. The saved check
records the original endpoint sums and reduced numerators as well.

Combining with the established dyadic valuation gives, on this family,


$$
\frac{\log q_n}{n}\ge
 \frac32\log2+\frac12\log3-o(1).
$$


This is a lower bound for the actual primitive denominator. It is not
a statement at arbitrary even indices, does not permit adding
unrelated fixed-prime families at one index, and does not alone
resolve the primitive shrinking threshold. The source retains
these limitations correctly.
