> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Moving prime rays and the $y^5-y$ residue mechanism

Date: 2026-08-28

## 1. Result

Let $m\geq 1$, and let $L_0,L_1$ be the adjacent mixed-cubic
logarithmic residues. For every



$$
b\in\{1,3,7,9,11,13,17,19,21,23\},
 \qquad p=10m+b\ \text{prime},
$$



one has



$$
\boxed{(L_0,L_1)\not\equiv(0,0)\pmod p.}             \tag{1.1}
$$



The case $b=3$ was already proved by the exceptional-ray theorem. Thus
the genuinely new rays in (1.1) are



$$
b=1,7,9,11,13,17,19,21,23.                         \tag{1.2}
$$



Every one is an infinite prime ray: since $\gcd(b,10)=1$, Dirichlet's
theorem gives infinitely many primes in the class $p\equiv b\pmod {10}$,
and all sufficiently large such primes have $m=(p-b)/10\geq1$.

The proof is uniform in $m$ on each listed ray. The finite computation is
only an exact factorization of a fixed ray determinant, followed by eight
small replays and one large candidate replay.

## 2. General affine-ray Frobenius formula

Put



$$
A(t)=(-1+t)(2-t),\qquad R(t)=t^2-2t+2,
$$



and let $d_s=4m+s$, $k_s=d_s+1$, $s=0,1$. For every prime
$p>6m$, put $r=p-6m$. The fresh-prime formula is



$$
L_s\equiv-4[t^{d_s}]A(t)^{-r}R(t)^{-k_s}\pmod p.   \tag{2.1}
$$



Set $y=1-t$, and define



$$
F(y)=y^5-y=tA(t)R(t),\qquad
 W(y)=tR(t)=(1-y)(1+y^2).                           \tag{2.2}
$$



For any fixed integer $c\geq0$, coefficient-as-residue conversion gives



$$
\boxed{
 L_s=4\operatorname {Res}_{y=1}
 A(y)^cW(y)^{\,r+c-k_s}F(y)^{-(r+c)}\,dy.}          \tag{2.3}
$$



Here $A(y)=-y(y+1)$. Formula (2.3) is an equality in
$\mathbb F_p$: multiply the coefficient differential by
$F^{r+c}=t^{r+c}A^{r+c}R^{r+c}$. The sign from $dt=-dy$ cancels
the minus sign in (2.1).

On a general affine ray $p=am+b$, the exponent of $W$ is



$$
r+c-k_s=(a-10)m+b+c-1-s.                          \tag{2.4}
$$



Thus $a=10$ is the unique slope for which a fixed exponent shift $c$
turns both residues into fixed-degree polynomial weights against one common
power of $F=y^5-y$.

## 3. The complete two-state reduction on slope 10

Let $p=10m+b$, where $b\geq1$ is odd. Choose $c\geq0$ so that
$b+c-2\geq0$, and set



$$
n=4m+b+c,\qquad q_s=b+c-1-s,
$$





$$
\rho_j=\operatorname {Res}_{y=1}y^jF(y)^{-n}\,dy,
 \qquad
 \Phi_s=\operatorname {Res}_{y=1}A(y)^cW(y)^{q_s}F(y)^{-n}\,dy.
                                                                    \tag{3.1}
$$



Then $L_s=4\Phi_s$. The residue of an exact derivative gives



$$
(k+5-5n)\rho_{k+4}+(n-1-k)\rho_k=0.              \tag{3.2}
$$



Since $5n=2p+3b+5c$, this becomes



$$
\boxed{
 (k-k_0)\rho_{k+4}+(4m+b+c-1-k)\rho_k=0,\qquad
 k_0=3b+5c-5.}                                     \tag{3.3}
$$



Assume first that $p>k_0$. At $k=k_0$, and again at $k=p+k_0$,
the first coefficient vanishes and the second is a unit. Backward
propagation in steps of four gives two zero residue classes:



$$
\begin{array}{c|c}
 \text{zero chain}&\text{class modulo }4\\ \hline
 \text{low singular chain}&k_0\\
 \text{high singular chain}&p+k_0=2m+c-1.
 \end{array}                                       \tag{3.4}
$$



No division crosses a zero of the second coefficient. Its possible
representatives are $n-1$ and $n-1+p$; modulo $4$, the first is the
class opposite the low chain and the second is the class opposite the high
chain. The interval bounds following from $p>k_0$ show that all other
second coefficients $4m+b+c-1-k$ used in the two backward chains are
nonzero modulo $p$. In the forward reductions below, the divisors are the
first coefficients $k-k_0$; over the needed range
$0\leq k\leq k_0+2$, each nonzero such integer has absolute value less
than $p$. Thus every stated division is by a $p$-unit.

The two weights in (3.1) have degrees



$$
\deg(A^cW^{q_0})=k_0+2,
 \qquad
 \deg(A^cW^{q_1})=k_0-1.                          \tag{3.5}
$$



Consequently the first member beyond the low singular index,
$\rho_{k_0+4}$, never occurs. Every residue needed by both functionals
therefore reduces to two states:



$$
E=\rho_{\,j_E},\quad j_E\equiv b+c-1\pmod4,
 \qquad
 O=\rho_{\,j_O},\quad j_O\equiv p+k_0+2\pmod4,     \tag{3.6}
$$



where $j_E,j_O\in\{0,1,2,3\}$. The labels $E,O$ mean the anchored
and the other class; their actual parities interchange when $c$ is odd.

The state $E$ is nonzero. If
$h=(b+c-j_E-1)/4$, the global residue theorem at the five simple roots
of $F$ gives



$$
\boxed{
 4E=(-1)^{n+1}\binom{5m+b+c+h-1}{m+h}\ne0\pmod p.} \tag{3.7}
$$



Indeed, the residue at zero supplies the binomial coefficient, the four
fourth roots of unity supply $4E$, and the residue at infinity is zero.
The top factorial argument is below $p$ when $p>k_0$, so (3.7) is a
$p$-unit.

Expanding the two fixed polynomials in (3.1) and using (3.3) gives



$$
\binom{\Phi_0}{\Phi_1}
 =M_{b,c,\epsilon}(m)\binom EO,
 \qquad \epsilon=m\bmod2.                         \tag{3.8}
$$



All denominators in $M$ are products of nonzero integers of absolute
value at most $k_0$, hence are units modulo $p>k_0$. Write



$$
\det M=u_{b,c,\epsilon}P_{b,c,\epsilon}(m),
$$



where $P\in\mathbb Z[m]$ is primitive and $u\in\mathbb Q^\times$.
The exact certificate retains and factors both the numerator and denominator
of $u$; all their prime factors are at most $k_0$, so $u$ is also a
$p$-unit.

If the two residues vanished, then



$$
p\mid P_{b,c,\epsilon}(m).
$$



Let $d=\deg P$. Because $10m\equiv-b\pmod p$, this forces



$$
\boxed{
 p\mid C_{b,c,\epsilon}:=
 10^dP_{b,c,\epsilon}(-b/10).}                    \tag{3.9}
$$



Thus every fixed intercept with $C_{b,c,\epsilon}\ne0$ has only finitely
many possible large exceptions, all among the prime divisors of one fixed
integer. This is the moving-ray analogue of the earlier fixed-gap
determinant, but here the determinant has fixed degree because the slope is
10.

## 4. Exact determinants for the proved rays

For $b\geq3$, take $c=0$. For $b=1$, take $c=1$. The companion
standard-library certificate constructs (3.8) by exact rational polynomial
arithmetic and completely factors every integer (3.9). The following table
lists the prime support of $C$; multiplicities, determinant scales, and
every primitive determinant coefficient are retained in the JSON.

| $b$ | even $m$: prime support of $C$ | odd $m$: prime support of $C$ | compatible $p>k_0$ |
|---:|---|---|---|
| 1 | 2, 3 | direct anchor $\Phi_1=-E$ | none |
| 3 | 2 | 2 | none |
| 7 | 2, 3, 5, 11 | 2, 3, 11 | none |
| 9 | 2, 3, 7, 11, 13, 17, 19, 53 | 2, 3, 7, 11, 13, 17 | none |
| 11 | 2, 3, 5, 7, 13, 17, 23, 103 | 2, 3, 7, 13, 17, 23, 59 | none |
| 13 | 2, 3, 7, 11, 17, 19, 29, 173 | 2, 3, 7, 11, 17, 19, 29 | $p=173,m=16$ |
| 17 | 2, 3, 7, 11, 13, 19, 23, 29, 31, 41, 113, 593 | 2, 3, 5, 7, 11, 13, 19, 23, 29, 31, 41 | none |
| 19 | 2, 3, 7, 11, 13, 17, 23, 37, 47, 1741 | 2, 3, 7, 11, 13, 17, 23, 37, 47, 139, 3919 | none |
| 21 | 2, 3, 7, 11, 13, 17, 19, 23, 29, 37, 43, 53, 2137, 11527 | 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 37, 43, 53, 103, 233 | none |
| 23 | 2, 3, 7, 11, 13, 17, 19, 29, 31, 41, 59, 139, 1559 | 2, 3, 7, 11, 13, 17, 19, 29, 31, 41, 59, 73303 | none |

Compatibility in the last column imposes
$p\equiv b\pmod {10}$, $m=(p-b)/10$, and the displayed parity.
For example, the factors $139,3919$ on the odd $b=19$ row correspond
to even $m$, so they are not candidates.

The only large candidate is excluded directly from the original scalar
Taylor recurrence:



$$
(b,m,p)=(13,16,173),\qquad
 (L_0,L_1)=(43,28)\pmod {173}.                    \tag{4.1}
$$



The prime cases with $p\leq k_0$, where the singular representative can
wrap around modulo $p$, are also replayed directly:

| $(b,m,p)$ | $(L_0,L_1)\bmod p$ |
|---|---|
| $(9,1,19)$ | $(15,15)$ |
| $(13,1,23)$ | $(20,8)$ |
| $(17,2,37)$ | $(9,30)$ |
| $(19,1,29)$ | $(13,19)$ |
| $(21,1,31)$ | $(30,13)$ |
| $(21,2,41)$ | $(24,1)$ |
| $(23,2,43)$ | $(23,28)$ |
| $(23,3,53)$ | $(27,16)$ |

Together, (3.7)--(3.9), the exact factorizations, and these replays prove
(1.1).

## 5. What this classifies, and where it stops

Among products of the pole factors already present, the two especially
simple separable polynomials are



$$
tA=y^3-y,\qquad tAR=y^5-y.                       \tag{5.1}
$$



The cubic $tR=(1-y)(1+y^2)$ is also separable, but using it alone leaves
the moving pole $A^{-r}$. Using $tA=y^3-y$ leaves the moving
$R^{-k_s}$. The quintic $tAR=y^5-y$ is the only one of these groupings
that absorbs all three pole sets simultaneously. By (2.4), its residual
weight has fixed degree precisely on slope $a=10$.

For $a>10$, (2.3) still gives residues of $y^5-y$, but the numerator
degree grows as $3(a-10)m+O(1)$; new post-singular residue states enter,
and there is no fixed determinant $P_b$ to reduce at $m=-b/a$. For
$6<a<10$, a fixed shift leaves a negative $W$-exponent of growing size,
so additional pole residues remain. These observations sharply classify
the present factor-grouping/Frobenius method; they are not a claim that a
different change of variables cannot handle another slope.

The method also does not prove all slope-10 intercepts at once. For a
general fixed odd $b$, it gives the exact finite criterion (3.9), but one
must still prove $C_{b,c,\epsilon}\ne0$, factor it, and check compatible
divisors. No uniform nonvanishing or factor-support theorem in $b$ has
yet been obtained.

## 6. Certificate

The companion files are:

* moving_ray_y5_minus_y_certificate.py, a standard-library exact generator;
* moving_ray_y5_minus_y_certificate.json, its byte-stable output.

The generator independently reconstructs both polynomial functionals from
$A^cW^{q_s}$, applies (3.3), retains the rational determinant scale,
forms primitive determinants, factors every scale and ray constant by
complete trial division through $100000$ (the largest ray-constant factor
here is $73303$), verifies the products exactly, filters by ray and
parity, and computes all direct pairs from the original scalar Taylor
recurrence. It also checks one prime of each parity on every ray by the
independent local expansion



$$
\rho_j=\frac14[x^{n-1}](1+x)^j
 (4+10x+10x^2+5x^3+x^4)^{p-n}\pmod p,
$$



thereby auditing both the sign and the normalization in (2.3).
