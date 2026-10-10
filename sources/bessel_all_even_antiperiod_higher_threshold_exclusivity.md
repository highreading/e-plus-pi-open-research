> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# All even anti-periods and higher-threshold Bessel exclusivity

Checked: 2026-08-27 UTC.

## 1. The all-order congruence

Let



$$
q_0=q_1=1,\qquad
 q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\geq2).
\tag{1}
$$



For an odd prime $p$, integers $m\geq0$, $n\geq0$, define



$$
S_m(n)=\sum_{j=0}^m\binom mjq_{n+jp}.
\tag{2}
$$



Also put $C_0=1$, consistently with $C_k=(2k)!/k!$.

**Theorem 1 (all even anti-periods).**  Let $k\geq1$ and let $p$ be a
prime satisfying



$$
p>2k.
\tag{3}
$$



Then, for every $n\geq0$,



$$
\boxed{
 S_{2k}(n)\equiv C_kp^kq_n\pmod {p^{k+1}},
 \qquad C_k={ (2k)!\over k!}.}
\tag{4}
$$



The adjacent odd sum satisfies



$$
\boxed{S_{2k-1}(n)\equiv0\pmod {p^k}.}
\tag{5}
$$



For $k=1$, equation (4) is the second anti-period congruence
$S_2(n)\equiv2pq_n\pmod {p^2}$.  For $k=2$, it is the fourth
anti-period congruence



$$
S_4(n)\equiv12p^2q_n\pmod {p^3}.
$$



The theorem is uniform over all pairs $(k,p)$ satisfying (3).  The proof
uses $2kp+1<p^2$, which follows from (3).  No claim is made here when
$p\leq2k$; in that range additional multiples of $p^2$ enter the
factorial quotients and the endpoint elimination below no longer has the
stated form.

## 2. Higher Newton laws on a root fibre

Let $p\mid q_r$ and put



$$
a_t=(-1)^tq_{r+tp}\qquad(t\geq0),
 \qquad D_j=\Delta_t^ja_0.
\tag{6}
$$



**Theorem 2 (degree $2k-1$ law).**  Under (3),



$$
\boxed{
 a_t\equiv\sum_{j=0}^{2k-1}\binom tjD_j
 \pmod {p^{k+1}}\qquad(t\geq0).}
\tag{7}
$$



Moreover,



$$
\boxed{
 p^{h+1}\mid\Delta_t^{2h}a_t\quad(0\leq h\leq k),
 \qquad
 p^{h+1}\mid\Delta_t^{2h+1}a_t\quad(0\leq h\leq k-1).}
\tag{8}
$$



For $h=0$, the first assertion in (8) is simply $p\mid a_t$, and the
second follows by differencing.  Formula (7) is an exact congruence for every
nonnegative translate parameter; it is not a formal Taylor approximation.

## 3. A full-fibre threshold polynomial

Suppose, in addition, that the $p$ standard representatives in the fibre
all survive through $p^k$:



$$
p^k\mid q_{r+tp}\qquad(0\leq t<p).
\tag{9}
$$



Because $2k-1<p$, every $D_j$ below uses only the standard
representatives covered by (9).  It is therefore divisible by $p^k$, and
the following divided coefficients are integral.  Define



$$
\boxed{
 P_{r,k}(T)=
 \sum_{j=0}^{2k-1}{D_j\over p^k}\binom Tj
 \quad\text{in }\mathbf F_p[T].}
\tag{10}
$$



**Theorem 3 (higher-threshold exclusivity).**  Under (3) and (9),



$$
\boxed{
 p^{k+1}\mid q_{r+tp}
 \quad\Longleftrightarrow\quad
 P_{r,k}(t)=0
 \qquad(0\leq t<p).}
\tag{11}
$$



Hence exactly one of the following holds.

1. The polynomial $P_{r,k}$ is nonzero.  At most $2k-1$ of the $p$
   standard representatives survive to $p^{k+1}$.

2. The polynomial $P_{r,k}$ is zero.  All $p$ standard representatives
   survive, and this full-fibre alternative is equivalent to the explicit
   divided-difference conditions

   

$$
\boxed{
    p^{k+1}\mid D_j\qquad(0\leq j\leq2k-1).}
   \tag{12}
$$



The hypothesis (9) is essential.  An ordinary root fibre has only one child
at each exponent and need not produce integral coefficients in (10) after
division by $p^k$.

## 4. Reflection-paired and window counts

Let



$$
s=p-1-r,
$$



and suppose $r<s$ and that both fibres satisfy (9).  Exact reflection
modulo $p^{k+1}$ gives



$$
\boxed{
 P_{s,k}(T)=P_{r,k}(-1-T)
 \quad\text{in }\mathbf F_p[T].}
\tag{13}
$$



Consequently, if this polynomial is nonzero, at most $4k-2$ of the
$2p$ standard representatives



$$
r+tp,\quad s+tp\qquad(0\leq t<p)
\tag{14}
$$



survive to $p^{k+1}$.  If it is zero, all $2p$ survive.

More precisely, let $1\leq L\leq p$.  The representatives of the pair in
the window $0\leq n<Lp$ evaluate the one polynomial $P_{r,k}$ on



$$
\{0,1,\ldots,L-1\}\cup\{-1,-2,\ldots,-L\}.
\tag{15}
$$



If $2L\leq p$, these $2L$ arguments are distinct.  A nonzero polynomial
therefore permits at most $2k-1$ survivors across the whole pair; for
arbitrary $L\leq p$, each argument is repeated at most twice and the bound
is $4k-2$.  A zero polynomial permits all $2L$.

At the central fixed point $r=s=(p-1)/2$, reflection gives



$$
P_{r,k}(T)=P_{r,k}(-1-T).
\tag{16}
$$



After centering at $-1/2$, this is an even polynomial.  Its degree is at
most $2k-2$.  Thus a nonzero central polynomial has at most $2k-2$
roots, while a zero polynomial permits all $p$ standard representatives.

For $k=2$, the degree is three.  In the original large-prime window
$n<2p$, the paired test arguments are $0,1,-1,-2$; all four surviving
to $p^3$ forces the polynomial to vanish identically.  For $k\geq3$,
four low test points no longer force a degree-$(2k-1)$ polynomial to be
zero.  Thus the especially sharp four-to-full-fibre cube dichotomy is a
genuine low-order feature, not an assertion silently extended to every
threshold.

## 5. Frozen inputs

The all-modulus period theorem gives, for odd $p$,



$$
q_{n+p}\equiv-q_n\pmod p.
\tag{17}
$$



A complete proof is contained in the frozen source

    sources/bessel_denominator_zero_gap_smooth_radical_barrier.md

with SHA-256

    dac7cd496b4342a8afc6d379274986d2030bc327c9017b3f6fa877108e62e1fc.

The exact odd-modulus reflection congruence



$$
q_{M-1-u}\equiv q_u\pmod M
\tag{18}
$$



is proved by running the recurrence backwards in

    sources/bessel_large_prime_four_point_exclusivity.md

with SHA-256

    1e8fed0a5ab04c97c4e0749d40304d6398f9fd32d55c7b49085fb4b4ecca4e41.

Finally, for $f(n)=(-1)^nq_n$, its Mahler coefficients
$A_j=\Delta^jf(0)$ satisfy



$$
A_j=(-1)^j j!\sum_{m=0}^{\lfloor j/2\rfloor}
 {(-1)^m\over m!}\binom{2j-2m}{j},
\tag{19}
$$



and



$$
{j!\over\lfloor j/2\rfloor!}\mid A_j.
\tag{20}
$$



Their derivation is in the frozen source

    sources/bessel_padic_index_interpolation_analytic_height_barrier.md

with SHA-256

    a50f45248133e437ee318b8cc28e6bbcc51de3568f3e621043221c90ddb4f348.

All additional valuation estimates needed for Theorem 1 are proved below.

## 6. Recurrence induction

For every $m\geq1$, summing (1) over the shifts in (2) and using
$j\binom mj=m\binom{m-1}{j-1}$ gives



$$
\boxed{
 S_m(n)=(4n-2)S_m(n-1)+S_m(n-2)
       +4mpS_{m-1}(n+p-1)}
\tag{21}
$$



for $n\geq2$.  Also,



$$
S_{2k-1}(n)=S_{2k-2}(n+p)+S_{2k-2}(n).
\tag{22}
$$



We induct on $k$, beginning with the exact identity $S_0(n)=q_n$.
Suppose (4) has been proved at $k-1$, modulo $p^k$.  Equation (22),
the induction hypothesis, and (17) give



$$
\begin{aligned}
 S_{2k-1}(n)
 &\equiv C_{k-1}p^{k-1}(q_{n+p}+q_n)\\
 &\equiv0\pmod {p^k}.
 \end{aligned}
\tag{23}
$$



For $k=1$, this uses $S_0=q$ and is simply (17).  Now take $m=2k$
in (21).  Its inhomogeneous term is divisible by $p^{k+1}$ by (23), so
$S_{2k}(n)$ satisfies the same homogeneous recurrence as $q_n$ modulo
$p^{k+1}$.  It remains to identify its two initial values.

## 7. Complete endpoint elimination

### 7.1 Operator expansion and non-endpoint valuations

Let $E=1+\Delta$ be the unit-shift operator and put



$$
R(z)=(1+z)^p-1=z^p+B(z),
 \qquad
 B(z)=\sum_{d=1}^{p-1}\binom pdz^d.
\tag{24}
$$



Every coefficient of $B$ contains $p$.  Expand



$$
R(z)^{2k}
 =\sum_{\ell=0}^{2k}
   \binom{2k}{\ell}z^{(2k-\ell)p}B(z)^\ell.
\tag{25}
$$



Terms with $\ell\geq k+1$ already have coefficients divisible by
$p^{k+1}$.  Fix $1\leq\ell\leq k$.  A monomial in its term has degree



$$
j=(2k-\ell)p+d,
 \qquad \ell\leq d\leq\ell(p-1).
\tag{26}
$$



Put $a=\lfloor d/p\rfloor$, so $0\leq a\leq\ell-1$, and write
$j=Np+b$, $0\leq b<p$.  Since $p>2k$, one has $j<p^2$, and



$$
N=2k-\ell+a.
$$



Legendre's formula and (20) give



$$
\begin{aligned}
 v_p(A_j)
 &\geq v_p(j!)-v_p(\lfloor j/2\rfloor!)\\
 &=N-\left\lfloor{N\over2}\right\rfloor
 =\left\lceil{N\over2}\right\rceil\\
 &\geq k-\left\lfloor{\ell\over2}\right\rfloor
 \geq k+1-\ell.
 \end{aligned}
\tag{27}
$$



Thus the coefficient contribution $p^\ell A_j$ vanishes modulo
$p^{k+1}$.  At the shifted initial value we need $A_j+A_{j+1}$.
The same estimate applies to $A_{j+1}$.  The only endpoint not literally
covered by $a\leq\ell-1$ is $\ell=1,j+1=2kp$; there (20) gives
$v_p(A_{2kp})\geq k$, exactly the required bound.  Hence every
non-endpoint term in (25) vanishes at both initial values.

This proves the full valuation claim used in the endpoint elimination; no
generic statement that “the other terms are smaller” is being assumed.

### 7.2 The even endpoint

Put $h=kp$.  In (19), after division by $(2h)!/h!$, every summand with
$m<h$ contains the factor $h$, while the summand $m=h$ survives.
Therefore



$$
{A_{2kp}\over(2kp)!/(kp)!}\equiv(-1)^{kp}=(-1)^k\pmod p.
\tag{28}
$$



Because $2kp<p^2$, the interval $(kp,2kp]$ contains exactly the $k$
multiples



$$
(k+1)p,(k+2)p,\ldots,2kp.
$$



After removing their factors of $p$, the $k$ intervening blocks each
contribute $(p-1)!$.  Wilson's theorem gives



$$
{1\over p^k}{(2kp)!\over(kp)!}
 \equiv(-1)^k{(2k)!\over k!}=(-1)^kC_k\pmod p.
\tag{29}
$$



Combining (28)--(29),



$$
\boxed{A_{2kp}\equiv C_kp^k\pmod {p^{k+1}}.}
\tag{30}
$$



### 7.3 The shifted endpoint

For $j=2h+1$, the same normalized sum has surviving term



$$
(-1)^{h+1}(2h+2).
$$



At $h=kp$, this is $2(-1)^{k+1}\pmod p$.  The factorial quotient for
$A_{2kp+1}$ differs from that in (29) by $2kp+1\equiv1\pmod p$.
Consequently



$$
\boxed{A_{2kp+1}\equiv-2C_kp^k\pmod {p^{k+1}}.}
\tag{31}
$$



Now $R(\Delta)=E^p-1$.  Since $p$ is odd and $2k$ is even,



$$
R(\Delta)^{2k}f(0)=S_{2k}(0).
$$



Equations (25), (27), and (30) give



$$
S_{2k}(0)\equiv C_kp^k\pmod {p^{k+1}}.
\tag{32}
$$



At $x=1$, one has $\Delta^jf(1)=A_j+A_{j+1}$, and parity gives



$$
R(\Delta)^{2k}f(1)=-S_{2k}(1).
$$



The endpoint is, by (30)--(31), $-C_kp^k$.  Hence



$$
S_{2k}(1)\equiv C_kp^k\pmod {p^{k+1}}.
\tag{33}
$$



The homogeneous recurrence from Section 6 and the two initial values
(32)--(33) prove Theorem 1.

## 8. Proofs of the Newton and reflection theorems

For every $h\leq k$, Theorem 1 at order $h$ (with the exact identity
$S_0=q$ when $h=0$) gives



$$
\Delta_t^{2h}a_t=(-1)^tS_{2h}(r+tp)\equiv0\pmod {p^{h+1}},
\tag{34}
$$



because every $q_{r+tp}$ is divisible by $p$.  Differencing (34) gives
the adjacent odd assertion in (8).  At $h=k$, (34) says that all forward
differences of order at least $2k$ vanish modulo $p^{k+1}$.  Newton's
exact finite-difference formula therefore truncates to (7).

Under (9), each $D_j$, $0\leq j\leq2k-1<p$, is an integer linear
combination of $a_0,\ldots,a_j$, hence is divisible by $p^k$.  Divide
(7) by $p^k$ and reduce modulo $p$ to obtain (10)--(11).  The binomial
polynomials $\binom Tj$, $0\leq j\leq2k-1<p$, form a basis for
polynomials of degree at most $2k-1$ over $\mathbf F_p$.  This proves
the root count and the equivalence (12).

Finally apply (18) with $M=p^{k+1}$.  For $0\leq t<p$,



$$
p^{k+1}-1-r-tp=s+(p^k-1-t)p.
\tag{35}
$$



The two translate parameters have the same parity, and
$p^k-1-t\equiv-1-t\pmod p$.  Hypothesis (9) on the $s$-fibre makes all
its coefficients in (10) integral, so the divided form of (7) evaluates
$P_{s,k}$ for the possibly large parameter $p^k-1-t$, not only for its
standard representatives.  Reflection makes both displayed values
divisible by $p^k$; division of its modulus-$p^{k+1}$ congruence is
therefore legitimate and gives (13).  The paired, truncated-window, and
central counts now follow from elementary root counting, as stated in
Section 4.

## 9. Limits for the large-prime valuation problem

Theorem 1 gives an exact hierarchy at every fixed order $k$ once
$p>2k$, and Theorem 3 bounds the next survivors on a fibre that has already
branched completely through $p^k$.  It does not control the unique Hensel
path of an ordinary root.  In particular, for an index $n<2p$, the higher
base-$p$ digits of that unique path may still be zero for arbitrarily many
levels as far as these congruences show.

Nor does the theorem exclude the explicit full-fibre condition (12).  Thus
it proves neither a uniform $O(1)$ bound nor the sublinear estimate



$$
v_p(q_n)\log p=o(n\log n)
$$



needed at the denominator-height frontier.  The hierarchy replaces an
unstructured higher lift by finite-degree polynomials; a genuinely new
nonvanishing or digit-height input is still required.

## 10. Replay

The companion script independently reconstructs $q_n$, the Mahler
coefficients, every factorial endpoint, and the general $S_{2k}$
congruence on a deterministic grid of pairs $(k,p)$ satisfying $p>2k$.
It also verifies the Newton laws on actual root fibres and records the number
of fibres in its grid satisfying the full-survival hypothesis (9).  For
$k\geq2$, that qualifying count is zero on the default grid; the
higher-threshold and reflection conclusions are symbolic theorems, not
finite extrapolations from a nonexistent example.

Run

    python -m py_compile scripts/bessel_all_even_antiperiod_higher_threshold_exclusivity_certificate.py
    python scripts/bessel_all_even_antiperiod_higher_threshold_exclusivity_certificate.py

The replay uses exact CPU arithmetic and negligible memory relative to the
available 50 GiB RAM; no hardware accelerator is useful for these short
integer recurrences.
