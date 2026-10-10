> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The n−1 hook congruence and an exact primitive endpoint residue

Date: 2026-09-13. Original continuation by root and audit_results.
Independent review: **FULL PASS** by audit_computations; see
raw_appell_minus_one_residue_independent_review.md and the separate
raw_ternary_numerator_unit_independent_review.md.
Root supplied the full-hook comparison and
the normalized-coefficient polynomial in Section 4; audit_results checked
them, derived the inverse transformation and endpoint residue, and wrote
the same-size near-hook formula for every cofactor. Root subsequently
supplied the weighted-cofactor lift in Section 8, retaining the entire
modulus n−1; audit_results checked and integrated that argument.
No new canonical degree or prime scan is used.

## 1. Main statements and the genuine exceptional prime

Use the exact polynomials and hook-normalized minors from
raw_appell_all_cofactors_and_endpoint_units.md and the independently
reviewed integral content lemma in
raw_appell_neighbor_content_and_denominator.md.

For $n\ge3$, put $q=n-1$ and $N=n(n+1)$. Then


$$
\boxed{M_D(x)\equiv x^N-2x^{N-2}\pmod q,\qquad
 M_D(1)\equiv-1\pmod q.}                                  \tag{1}
$$


The actual primitive normalization gives


$$
\boxed{\gcd(V(1),n-1)=\gcd(V_{\rm lead},n-1)=1,\qquad
 V_{\rm lead}\equiv -V(1)\pmod{n-1}.}                      \tag{2}
$$



The whole actual primitive polynomial satisfies the full-depth congruence


$$
\boxed{V(t)\equiv V(1)\bigl(2t^{n-1}-t^n\bigr)\pmod{n-1}.} \tag{3}
$$


Consequently the exact exponential endpoint residue is


$$
\boxed{\widehat P_e(1)\equiv-5V(1)\pmod{n-1}.}            \tag{4}
$$


Thus it is a unit for every prime $p\mid n-1$, $p\ne5$, whereas it is divisible by
five for **every** $n\equiv1\pmod5$, $n\ge6$. This is an actual
residue obstruction to an exponential-unit argument, not a hypothetical
counterexample based on arbitrary formal series.

When $p\ne5$, $p\mid n-1$, and
$v_p(n!)>\lfloor\log_p(2n)\rfloor$, the actual reduced denominator obeys


$$
\boxed{v_p(q_n)=v_p(Z_n)\ge v_p(n!).}                     \tag{5}
$$


If $25\mid n-1$, (4) instead gives $v_5(\widehat P_e(1))=1$,
and eventually $v_5(q_n)\ge v_5(n!)-1$, as proved in Section 9.
The case $v_5(n-1)=1$ still requires additional depth control.

Sections 3–6 first prove and cross-check the prime-level mechanism.
Section 8 supplies the separate argument needed for the full modulus
in (3)–(4); no prime-block congruence is extrapolated to prime powers.

## 2. Full determinant: a same-size hook and no division loss

Let $q=n-1$, so the rectangle $\lambda_D=(n^{n+1})$ has width $q+1$
and height $q+2$. Modulo $q$, its contents consist of $q+3$ copies
of every residue plus the two contents $0,-1$. This follows by
splitting the column indices into one full residue set plus $1$,
and the row indices into one full residue set plus $1,2$.

The hook $\eta=(N-1,1)$, of the **same size** $N=q(q+3)+2$, has
the identical content multiset. Its first row contributes $q+3$
full residue sets and one zero; its second row contributes $-1$.
The integral central-character lemma therefore compares their augmented
Schur polynomials modulo $q$.

Write


$$
\mathcal A_k^{[n]}(x)=k![t^k]e^{xt}(1+t^2)^n.
$$


Jacobi--Trudi for the hook and $H_\eta=N!/(N-1)$ give the exact
polynomial identity


$$
M_\eta(x)=
 \frac{N x\mathcal A_{N-1}^{[n]}(x)
            -\mathcal A_N^{[n]}(x)}{N-1}.                \tag{6}
$$


Since $N\equiv2\pmod q$, its denominator $N-1$ is a unit modulo
$q$. No other division in (6) is performed modulo $q$.

For any $k$, the ordinary Appell polynomial expands as


$$
\mathcal A_k^{[n]}(x)
 =\sum_h\binom nh(k)_{2h}x^{k-2h}.
$$


For $h\ge2$, its coefficient is


$$
n(n-1)\cdots(n-h+1)\frac{(k)_{2h}}{h!},
$$


which is divisible by $q=n-1$: the last ratio is an integer and the
first product contains $n-1$. Therefore


$$
\mathcal A_k^{[n]}(x)
 \equiv x^k+k(k-1)x^{k-2}\pmod q,                         \tag{7}
$$


omitting terms with negative exponent. Substitution in (6) gives the
coefficient $N(N-3)\equiv-2$ at $x^{N-2}$, proving (1).

The square $\lambda_0=(n^n)$ has $q+2$ copies of every content
residue plus one zero. It matches the row partition $(n^2)$, so (7)
also gives


$$
M_0(x)\equiv x^{n^2}\pmod q.                             \tag{8}
$$


The primitive formula


$$
b_l=\frac{U_l}{(n+l)!}
 =(-1)^{n-l}\binom nl V(1)\frac{M_{n-l}(1)}{M_D(1)},
 \qquad b_l\in\mathbb Z,\quad\gcd_l b_l=1                 \tag{9}
$$


now forces $V(1)$ to be a unit at every prime dividing $q$, because
$M_D(1)$ is a unit and every $M_j$ is an integer.
At $l=n$, (9) gives $V_{\rm lead}=V(1)M_0(1)/M_D(1)$;
equations (1), (8) prove (2) with the full modulus.

## 3. Cofactor residues needed for the normalized coefficient vector

Fix an odd prime $p\mid n-1$. Write $n=ap+1$.
The contents of the square $(n^n)$ consist of
$ap\,a+2a=pa^2+2a$ copies of each residue, plus one extra zero.

The cofactor partition


$$
\lambda_j=((n+1)^j,n^{n-j})
$$


adds $j$ boxes in column $n+1$, with residues
$1,0,-1,\ldots,2-j$.
If $j\equiv0\pmod p$, these additions are uniform residue blocks;
if $j\equiv1\pmod p$, they are uniform blocks plus one extra $1$.
In these two cases $\lambda_j$ has the same content multiset as the
row partition of size $N_j=n^2+j$. Thus


$$
M_j(1)\equiv
 \begin{cases}
 1,&j\equiv0\pmod p,\\
 3,&j\equiv1\pmod p.
 \end{cases}                                             \tag{10}
$$


Indeed the ordinary Appell comparison is (7) modulo $p$, and
$N_j\equiv1$ or $2$, respectively.

These are exactly the cofactor residues needed in (9).
Lucas's theorem says that $\binom nl$ vanishes modulo $p$ unless
$l\equiv0$ or $1$, because the lowest base-$p$ digit of $n$ is
one. On those surviving terms $j=n-l$ has residue one or zero.
Using $M_D(1)\equiv-1$, equation (9) gives, for **all** $l$,


$$
b_l\equiv V(1)(2l-3)(-1)^{n-l}\binom nl\pmod p.
$$


Therefore the whole normalized polynomial $b(t)=\sum_l b_lt^l$ obeys


$$
\boxed{
 b(t)\equiv V(1)(2t\partial_t-3)(t-1)^n
      \equiv V(1)(3-t)(t-1)^{n-1}\pmod p.}               \tag{11}
$$


No assertion that every cofactor has residue one or three is used;
the other cofactor indices are multiplied by a binomial divisible by
$p$.

The coefficient of $t$ in (11) is
$-V(1)(-1)^{n-1}$, a unit. Since $n+1\equiv2\pmod p$,
$U_1=(n+1)!b_1$ has valuation exactly $v_p(n!)$.
Together with the global factorial divisor, this proves


$$
v_p(\operatorname{cont}U)=v_p(n!)\quad(p\text{ odd},\
 p\mid n-1).                                             \tag{12}
$$


At three, the constant coefficient $b_0$ vanishes modulo three;
index one, rather than index zero, supplies the unit in (12).

## 4. Exact inversion to the actual primitive V polynomial

Set


$$
H(t)=\sum_{j=0}^n w_{2n+j}t^j.
$$


The original Rodrigues relation
$S=(1+t^2)^nU$, together with $S_{2n+j}=(n+j)!w_{2n+j}$,
gives the exact inverse of the previously used triangular map:


$$
w_{2n+j}=
 \sum_{\substack{a\ge0\\j+2a\le n}}
 \binom na\frac{(n+j+2a)!}{(n+j)!}\,b_{j+2a}.             \tag{13}
$$


This formula has integer coefficients and diagonal one.

Modulo an odd $p\mid n-1$, every $a\ge2$ summand vanishes.
If $2a\ge p$, its factorial ratio contains $p$.
If $2a<p$, then $a<p$, and Lucas gives $\binom na=0\pmod p$
for $a\ge2$. Thus only $a=0,1$ remain, and


$$
w_{2n+j}\equiv b_j+(j+2)(j+3)b_{j+2}\pmod p.
$$


Summing over $j$ yields the polynomial identity


$$
H=b+b''+2(b'-b_1)/t\quad\text{over }\mathbb F_p[t].        \tag{14}
$$


The quotient is a polynomial, because its numerator has zero constant
term; coefficients outside the actual degree range are zero.

Put $g=(t-1)^{n-1}$. Its derivative is zero in $\mathbb F_p[t]$.
Equation (11) makes (14)


$$
H=V(1)\left((3-t)g-\frac{2(g-g(0))}{t}\right).            \tag{15}
$$



Let $\operatorname{Pol}_\infty$ mean the nonnegative-power part of
a formal Laurent expansion at infinity. The identity
$W=t^n(t-1)^nV$ gives


$$
V(t)=\operatorname{Pol}_\infty
       \left[\left(\frac{t}{t-1}\right)^n H(t)\right].     \tag{16}
$$


To justify this precisely, the discarded low part of
$t^{-2n}W=(1-t^{-1})^nV$ has strictly negative powers. Multiplying it
by $(1-t^{-1})^{-n}=1+O(t^{-1})$ cannot create a nonnegative power.
Thus (16) is valid over any field.

Substitute (15). The rational expression in (16) becomes


$$
V(1)\left[
 t^{n-1}(2-t)+\frac{2g(0)t^{n-1}}{(t-1)^n}\right].
$$


The final fraction is strictly proper. Its polynomial part is zero,
which proves (3) modulo p. Section 8 justifies the full modulus.

## 5. Evaluated exponential residue and primitive denominator

The exact, sign-corrected border is


$$
\widehat P_e(1)=\sum_{r=0}^n V_rD_{n,r},\qquad
 D_{n,r}=\sum_{j=0}^{n+r}\binom{n+j}{j}(n+r)_j.
$$


For $n\equiv1\pmod p$, terms with $j\ge p$ vanish modulo $p$.
For $j<p$, the binomial is $j+1$ modulo $p$. Therefore


$$
D_{n,n-1}\equiv 1+2=3,\qquad
 D_{n,n}\equiv1+4+6=11\pmod p.                            \tag{17}
$$


At $p=3$, the final summand six is zero modulo three, so (17)
still holds without an exception. Higher falling factorials vanish
because their starting residues are one or two.
Equations (3), (17) prove


$$
\widehat P_e(1)\equiv(2\cdot3-11)V(1)=-5V(1)\pmod p,
$$


establishing (4) modulo p. Its full-depth version is proved in Section 8.

Globally, $n!\mid\operatorname{cont}\widehat Q$ and $n!\mid Z$.
The Taylor denominator loss for $\arctan$ is at most
$\lfloor\log_p(2n)\rfloor$, so


$$
v_p(\widehat P_a(1))\ge v_p(n!)-
                     \lfloor\log_p(2n)\rfloor.
$$


For $p\ne5$ in the stated family, if this is positive then
$N=\widehat P_e(1)+4\widehat P_a(1)$ is a unit. The exact actual
reduction $q=|Z|/\gcd(|Z|,|N|)$ gives (5).
At five the exponential term itself vanishes at first order, so the
same argument cannot make $N$ a unit. Section 9 handles the
subclass $25\mid n-1$ by the exact full-modulus lift.

## 6. Independent ternary derivative derivation

The following second derivation checks the special case that motivated
this continuation. High-tail inversion of $W=t^n(t-1)^nV$ gives


$$
V'(1)=\sum_{l=0}^n\binom{n+l}{n+1}w_{2n+l}.              \tag{18}
$$


Indeed the coefficient of $w_{2n+l}$ is


$$
\sum_{j=1}^l j\binom{n+l-j-1}{l-j}
 =\binom{n+l}{n+1}
$$

, by the generating function
$t(1-t)^{-n-2}$.

When $n\equiv1\pmod3$, Lucas kills every $l$ except $l\equiv1$.
For these $l$, the first factorial factor $n+l+1$ in every
off-diagonal term of the original $b$-map is divisible by three,
so $w_{2n+l}\equiv b_l\pmod3$.
Now $j=n-l\equiv0\pmod3$; the same-size row comparison in (10)
gives $M_j(1)\equiv1$, while $M_D(1)\equiv-1$.
Thus


$$
V'(1)\equiv
 -V(1)\sum_{l=0}^n(-1)^{n-l}\binom nl\binom{n+l}{n+1}
 =-nV(1)\equiv -V(1)\pmod3.                              \tag{19}
$$


The exact sum equals $n$, as seen by taking coefficient $x^{n+1}$
in $(1+x)^n[(1+x)-1]^n$.
The ternary border is $D_{n,r}\equiv-r$, so
$\widehat P_e(1)\equiv -V'(1)\equiv V(1)\pmod3$,
in agreement with (4).

Together with the passed cases $3\mid n$ and $3\mid n+1$, this makes
$\widehat P_e(1)$ a three-adic unit in every degree.
The boundary $n=1$ is covered directly by the frozen
$V(t)=2-t,\ \widehat P_e(1)=-5$; no new system is solved.
Consequently


$$
v_3(q_n)\ge v_3(n!)=\frac n2-O(\log n)
$$


for all sufficiently large $n$, with no residue restriction.
This is a proved fixed-prime lower bound. Its rate, combined with the
dyadic rate, remains below the accepted approximation-error threshold;
it is not a proof about $e+\pi$.

## 7. An exact same-size near-hook expression for every cofactor

The preceding residue argument intentionally used only those $j$
surviving Lucas. There is also a whole-cofactor comparison modulo
$q=n-1$, with no prime restriction or discarded depth.

Let


$$
A=q^2+2,\qquad L=2q+j-1,\qquad
 \eta_j=(A,2,1^{L-2}).
$$


For $q\ge2,\ 0\le j\le n$, this is a partition of
$A+L=n^2+j=N_j$.
At $j=0$, its contents modulo $q$ are $q+2$ uniform copies plus
one zero, matching the square $\lambda_0$.
Increasing $j$ by one appends a bottom box of content
$2-j\pmod q$, exactly matching the box added to $\lambda_j$.
Therefore the multisets agree for every $j$, and


$$
\boxed{M_j(x)\equiv H_{\eta_j}
       s_{\eta_j}\!\left([t^k]e^{xt}(1+t^2)\right)
                   \pmod{n-1}.}                         \tag{20}
$$


The background parameter has been reduced from $n$ to one only
after applying the integral power-sum specialization: all power sums
are integers and differ by multiples of $n-1$.

For an explicit formula set


$$
h_k=[t^k]e^{xt}(1+t^2),\qquad
 e_k=[t^k]e^{xt}/(1+t^2).
$$


Frobenius Giambelli gives the exact expression in (20) as


$$
\frac{(A+L-1)A!L!}{(A-1)(L-1)}
 \left[
 x\sum_{r=0}^{L-1}(-1)^r h_{A+r}e_{L-1-r}
       -h_Ae_L
 \right].                                                \tag{21}
$$


This is an integer polynomial by augmented-Schur integrality.
It must be formed as that exact polynomial before reduction:
$L-1\equiv j-2\pmod q$ need not be invertible.
Thus (20)--(21) are a full-depth, same-size cofactor description and
a possible starting point for the remaining higher-five-adic question.
They do not justify cancelling the displayed denominator modulo $q$.

The near-hook formula does not by itself remove the five-adic exception.
The weighted-cofactor argument below gives a stronger composite-modulus
result for the combinations actually needed by the primitive vector.

## 8. The weighted-cofactor lift to the entire modulus n−1

Fix a prime power $p^\nu\mid n-1$. The full determinant is a unit
modulo $p^\nu$ by (1). For $0\le j\le n$, put
$t=v_p\binom nj$. We prove


$$
\binom nj M_j(1)
 \equiv \binom nj(1+2j)\pmod{p^\nu}.                      \tag{22}
$$


If $t\ge\nu$, both sides vanish at the required depth.
Suppose $t<\nu$ and set $b=\nu-t>0$.

The boundary indices $j=0,1$ already match same-size row partitions
modulo $p^\nu$, so their residues are $1,3$, respectively.
For $2\le j\le n$, the exact integer identity


$$
\binom nj=\frac{n(n-1)}{j(j-1)}\binom{n-2}{j-2}
$$


gives


$$
v_p(j(j-1))
 =v_p(n-1)+v_p\binom{n-2}{j-2}-t
 \ge\nu-t=b.
$$


Since consecutive integers are coprime, $j\equiv0$ or $1\pmod{p^b}$.
Also $n\equiv1\pmod{p^b}$.
The same content count as in Section 3, now modulo $p^b$, compares
$\lambda_j$ to the row partition of the same size.
The integral JM theorem, not a modular-block lift, gives


$$
M_j(1)\equiv1+N_j(N_j-1)
       \equiv1+j(j+1)\equiv1+2j\pmod{p^b}.
$$


Multiplying by $\binom nj$ recovers the missing $t$ powers,
proving (22). This covers the full index range, including $j=n$.

Dividing (22) by the unit $M_D(1)\equiv-1\pmod{p^\nu}$, and using
the exact primitive identity (9), proves the coefficients of


$$
b(t)\equiv V(1)(3-t)(t-1)^{n-1}\pmod{p^\nu}.
$$


Combining prime powers gives this identity modulo **all** of $q=n-1$.

The inverse transformation (13) also truncates modulo $q$, not merely
modulo its primes. For $a\ge2$, its off-diagonal coefficient is


$$
n(n-1)\cdots(n-a+1)
       \frac{(n+j+2a)!}{(n+j)!\,a!}.
$$


The last ratio is an integer because it is a product of $2a$
consecutive integers divided by $a!$; the first product contains
$n-1$. Hence all $a\ge2$ terms vanish modulo $q$.
The $a=1$ coefficient reduces to $(j+2)(j+3)$, exactly as in (14).

Equations (14)–(16) are therefore valid over $(\mathbb Z/q\mathbb Z)[t]$.
The derivative of $g=(t-1)^{n-1}$ is zero in this ring.
The Laurent operations at infinity use only series with constant term
one, so they remain valid even though this ring can have zero divisors.
The strictly proper final fraction still contributes no nonnegative
power. This proves the full polynomial congruence (3).

Finally the two border evaluations hold modulo $q$ directly.
For $D_{n,n-1}$, every term of order $j\ge2$ contains $2n-2=2q$;
its first two terms give $1+2=3$.
For $D_{n,n}$, every term of order $j\ge3$ contains $2q$.
Its order-two term is the integer


$$
\binom{n+2}{2}(2n)(2n-1)
 =n(n+1)(n+2)(2n-1)\equiv6\pmod q,
$$


so no division by two is performed modulo an even $q$.
Together with the first two terms this gives $11$.
Thus (3) implies the full endpoint congruence (4).

## 9. The controlled five-adic subclass and the remaining gap

If $25\mid n-1$, then $V(1)$ is a five-adic unit by (2), and (4)
gives


$$
\widehat P_e(1)=-5V(1)+25u,\qquad u\in\mathbb Z.
$$


Hence $v_5(\widehat P_e(1))=1$, exactly.
If


$$
v_5(n!)>\lfloor\log_5(2n)\rfloor+1,
$$


the arctangent endpoint has valuation strictly greater than one.
The factor four is a five-adic unit, so the actual numerator has
valuation one and


$$
v_5(q_n)=v_5(Z_n)-1\ge v_5(n!)-1.                        \tag{23}
$$


This holds for all sufficiently large $n\equiv1\pmod{25}$.

If $v_5(n-1)=1$, equation (4) proves divisibility of $\widehat P_e(1)$
by five but does not determine its next digit. The exact higher-depth
remainder of the actual cofactor expression is still needed there.
No uniform bound on that remainder, or on the corresponding endpoint
gcd, is claimed.

Thus the new first-neighbor theorem controls primes dividing $n-1$
apart from the explicitly retained shallow five-adic class. Together
with the preceding results it proves actual factorial-denominator
bounds at the residue classes $n\equiv0,-1,1\pmod p$ for every fixed
odd $p\ne5$; at five the class $n\equiv1\pmod{25}$ has the one-power
loss in (23). Further residue classes remain unproved.
