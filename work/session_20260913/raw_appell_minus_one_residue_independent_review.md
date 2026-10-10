> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit: the n−1 cofactor lift and actual endpoint residue

Date: 2026-09-13. Reviewer: audit_computations.

**FULL PASS.** This review covers the stable full-modulus version of
`raw_appell_minus_one_hook_and_endpoint_residue.md`, all Sections 1–9,
including the optional near-hook formula in Section 7 and the weighted
prime-power lift in Section 8. Every stated integral, normalization,
endpoint, and actual-denominator step passes. No mathematical correction
is required, and no new canonical degree, prime, or numerical scan was
used.

## 1. Integral content comparisons and the full determinant

The integral central-character lemma was independently verified against
Ryba's published Proposition 3.11 and Theorem 3.14 in
`raw_appell_neighbor_content_independent_review.md`. It applies at a
fixed symmetric-group size and retains an arbitrary composite modulus.
The present specialization is integral in power sums:
$p_1=x$, $p_{2h}=2n(-1)^{h-1}$, and all other odd power sums
vanish. Thus congruence in the integral power sums really does become
congruence in $\mathbb Z[x]$, despite rational complete functions.

Put $q=n-1\ge2$ and $N=n(n+1)=q(q+3)+2$. In the full
rectangle of width $q+1$ and height $q+2$, split the column
indices into one complete residue set and the singleton $1$, and
the row indices into one complete set and $1,2$. Their differences
give $q+3$ complete content residue sets and the two extras $0,-1$.
The same-size hook $(N-1,1)$ has exactly the same contents modulo
$q$. Both the group size and all residue multiplicities are retained.

For this hook, $s_{(N-1,1)}=h_{N-1}h_1-h_N$ and its hook product
is $N!/(N-1)$. Consequently its augmented polynomial is exactly



$$
\frac{N x\mathcal A_{N-1}^{[n]}(x)-\mathcal A_N^{[n]}(x)}{N-1},
 \qquad
 \mathcal A_k^{[n]}=k![t^k]e^{xt}(1+t^2)^n.
$$



Here $N-1\equiv1\pmod q$ is a unit. For every nonzero summand
with $h\ge2$,



$$
\binom nh(k)_{2h}
 =n(n-1)\cdots(n-h+1)\frac{(k)_{2h}}{h!}
$$



is divisible by $q$, because $(k)_{2h}/h!$ is an integer.
Thus $\mathcal A_k^{[n]}\equiv x^k+k(k-1)x^{k-2}\pmod q$.
Substitution into the exact hook formula leaves correction coefficient
$N(N-3)\equiv-2$, giving



$$
M_D(x)\equiv x^N-2x^{N-2}\pmod q,
 \qquad M_D(1)\equiv-1\pmod q.
 \tag{A}
$$



The square $(n^n)$ has $q+2$ full content sets and one extra
zero. It agrees with the row of size $n^2$, so
$M_0(x)\equiv x^{n^2}\pmod q$. There is also a valid independent
check of (A): the full rectangle can be compared directly with the
column of size $N$, whose elementary-function specialization gives
the same correction $-nN(N-1)\equiv-2$.

## 2. Primitive units do not require all intermediate minors to be units

The exact cofactor formula is



$$
b_l=\frac{U_l}{(n+l)!}
 =(-1)^{n-l}\binom nl V(1)\frac{M_{n-l}(1)}{M_D(1)}.
 \tag{B}
$$



The signs, reversed cofactor index, and factorial normalization agree
with the actual inverse-column hook identity. The vector $b$ is
integral and primitive because its two transformations from primitive
$V$ are integral triangular with diagonal one. Equation (A) makes
the denominator in (B) a unit at every prime dividing $q$. If such
a prime divided $V(1)$, it would divide every $b_l$, which is
impossible. At $l=n$, equation (B) and the square comparison give



$$
V_{\rm lead}=V(1)\frac{M_0(1)}{M_D(1)}
 \equiv-V(1)\pmod q.
$$



Both actual primitive endpoint values are therefore units modulo
$n-1$. No normalization factor has been canceled without checking
its valuation.

## 3. The weighted cofactor lift retains every prime-power depth

This is the key step beyond Lucas's first-layer argument. Fix
$p^\nu\mid q$ with $\nu=v_p(q)$, allowing $p=2$, and let
$t=v_p\binom nl$. If $t\ge\nu$, the corresponding coefficient
in (B) vanishes at the required depth because $M_D(1)$ is a unit.

If $t<\nu$, put $b=\nu-t\ge1$. For $2\le l\le n$, the
exact identity



$$
\binom nl=\frac{n(n-1)}{l(l-1)}\binom{n-2}{l-2}
$$



implies $v_p(l(l-1))\ge\nu-t=b$. Consecutive integers are coprime,
so $l\equiv0$ or $1\pmod{p^b}$. The indices $l=0,1$
satisfy the same alternative directly. No division by $l(l-1)$
is made modulo a prime power: the displayed rational identity is first
used as an equality of integer valuations.

Write $n=a p^b+1$. The square $(n^n)$ has $p^b a^2+2a$
copies of every content residue and one additional zero. Adding the
cofactor column boxes gives the sequence $1,0,-1,\ldots$. If a
cofactor index $j$ is zero or one modulo $p^b$, the additions
are full residue sets or full sets plus one extra $1$, respectively.
The resulting content multiset agrees with the row of the same size
$s=n^2+j$.

Its ordinary Appell specialization has residue
$x^s+s(s-1)x^{s-2}$. The proof of the coefficient divisibility in
Section 1 applies at this entire modulus, since $p^b\mid n-1$.
Therefore



$$
M_j(1)\equiv
 \begin{cases}1,&j\equiv0\pmod{p^b},\\
 3,&j\equiv1\pmod{p^b}.
 \end{cases}
 \tag{C}
$$



For $j=n-l$, equation (C), together with $M_D(1)\equiv-1$,
makes the cofactor quotient congruent to $2l-3\pmod{p^b}$.
Multiplication by $\binom nl$, whose valuation is exactly $t$,
upgrades the coefficient error to a multiple of $p^{b+t}=p^\nu$.
This proves, coefficient by coefficient and at every prime divisor,



$$
b_l\equiv V(1)(2l-3)(-1)^{n-l}\binom nl\pmod q.
$$



Summing and using $n\equiv1\pmod q$ yields the full polynomial
congruence



$$
b(t)\equiv V(1)(2t\partial_t-3)(t-1)^n
 \equiv V(1)(3-t)(t-1)^{n-1}\pmod{n-1}.
 \tag{D}
$$



This proof justifies the lifting directly. It does not assume that
Lucas's theorem itself gives a prime-power congruence, and it does not
require the unweighted intermediate cofactors to have uniform residues.

## 4. The full-modulus high-tail inverse and polynomial recovery

Let $H(t)=\sum_{j=0}^n w_{2n+j}t^j$. The exact inverse triangular
map obtained from $S=(1+t^2)^nU$ is



$$
w_{2n+j}=
 \sum_{a\ge0,\ j+2a\le n}
 \binom na\frac{(n+j+2a)!}{(n+j)!}b_{j+2a}.
 \tag{E}
$$



The factorials can also be checked from
$S_{2n+j}=(n+j)!w_{2n+j}$. There is no sign in this inverse.

For $a\ge2$, use



$$
\binom na\frac{(n+j+2a)!}{(n+j)!}
 =n(n-1)\binom{n-2}{a-2}
   \frac{(n+j+2a)!}{a(a-1)(n+j)!}.
$$



The last quotient is an integer: a product of $2a$ consecutive
integers is divisible by $(2a)!$, and $a(a-1)\mid(2a)!$.
Thus every term with $a\ge2$ is divisible by the full $n-1$,
including its powers of two. For $a=1$, the remaining coefficient
reduces to $(j+2)(j+3)$. Consequently (E) becomes



$$
H\equiv b+b''+2(b'-b_1)/t\pmod q.
 \tag{F}
$$



The quotient in (F) is polynomial. Put $g=(t-1)^{n-1}$. In
$(\mathbb Z/q\mathbb Z)[t]$, one has $g'=0$. Equation (D)
then gives



$$
H\equiv V(1)\left((3-t)g-2\frac{g-g(0)}t\right)\pmod q.
$$



The exact integer relation $W=t^n(t-1)^nV$ implies



$$
V=\operatorname{Pol}_\infty
   \left[\left(\frac t{t-1}\right)^nH\right].
 \tag{G}
$$



This is valid over any commutative coefficient ring, including
$\mathbb Z/p^\nu\mathbb Z$: the inverse Laurent series
$(1-t^{-1})^{-n}$ exists because its constant term is one, and
multiplying it by a strictly negative-power series cannot create a
nonnegative power. Neither (G) nor the next step requires a field.

The expression in (G), after substitution, is



$$
V(1)\left[t^{n-1}(2-t)
       +\frac{2g(0)t^{n-1}}{(t-1)^n}\right].
$$



The final rational term is strictly proper. Its polynomial part vanishes
over the same ring. Thus the actual primitive polynomial satisfies



$$
\boxed{V(t)\equiv V(1)(2t^{n-1}-t^n)\pmod{n-1}.}
 \tag{H}
$$



For every odd $p\mid n-1$, the coefficient $b_1$ in (D) is
$-V(1)(-1)^{n-1}$, a unit, and $p\nmid n+1$. Hence
$U_1=(n+1)!b_1$ has valuation $v_p(n!)$. Together with the
global factorial divisor this proves the stated exact local content.
At three the constant coefficient $b_0$ is not a unit; using index
one is necessary and correct.

## 5. The full endpoint residue and the special role of five

The evaluated exponential formula uses the actual positive orientation



$$
\widehat P_e(1)=\sum_rV_rD_{n,r},\qquad
 D_{n,r}=\sum_j\binom{n+j}{j}(n+r)_j.
$$



The two surviving coordinates in (H) need only two borders. For
$r=n-1$, every $j\ge2$ falling factorial contains
$2n-2=2q$, so
$D_{n,n-1}\equiv1+(n+1)(2n-1)\equiv3\pmod q$.
For $r=n$, every $j\ge3$ term likewise contains $2q$.
The $j=2$ term can be written without division as



$$
\binom{n+2}{2}(2n)(2n-1)
 =n(n+1)(n+2)(2n-1)\equiv6\pmod q.
$$



Together with $j=0,1$, this gives
$D_{n,n}\equiv1+4+6=11\pmod q$. These arguments retain the whole
modulus, even when it is even; no inversion of two is required.
Consequently



$$
\boxed{\widehat P_e(1)\equiv-5V(1)\pmod{n-1}.}
 \tag{I}
$$



Since $V(1)$ is a unit at every divisor of $n-1$, the exponential
endpoint is a unit at every such prime except five. At five it always
vanishes modulo five. If $25\mid n-1$, congruence (I) proves the
sharper equality $v_5(\widehat P_e(1))=1$, since the error is
divisible by at least $25$ while $-5V(1)$ has valuation one.
If $v_5(n-1)=1$, congruence (I) alone gives no upper bound on the
additional valuation, and no such bound should be inferred.

The global divisibility and Taylor loss are



$$
v_p(Z)\ge v_p(n!),\qquad
 v_p(\widehat P_a(1))\ge
 v_p(n!)-\lfloor\log_p(2n)\rfloor.
$$



At $p\ne5$, strict positivity of the latter bound makes the actual
integer numerator $N=\widehat P_e(1)+4\widehat P_a(1)$ a unit.
Then the exact reduction $q_n=|Z|/\gcd(|Z|,|N|)$ gives
$v_p(q_n)=v_p(Z)\ge v_p(n!)$. If $25\mid n-1$ and the latter
arctangent bound is greater than one, then $v_5(N)=1$, and instead
$v_5(q_n)=v_5(Z)-1\ge v_5(n!)-1$. The threshold ensures that
$v_5(Z)>1$, so there is no missing maximum with zero.

## 6. Independent ternary derivation and uniform consequence

A separate reconstruction appears in
`raw_ternary_numerator_unit_independent_review.md`. It needs only the
cofactor indices divisible by three. It begins with the exact identity



$$
V'(1)=\sum_{l=0}^n\binom{n+l}{n+1}w_{2n+l}.
$$



For $n\equiv1\pmod3$, Lucas eliminates all $l$ except those
congruent to one, where the first factorial factor in every added tail
term is divisible by three. The relevant cofactor comparison then gives



$$
V'(1)\equiv-V(1)
 \sum_{l=0}^n(-1)^{n-l}\binom nl\binom{n+l}{n+1}
 =-nV(1)\equiv-V(1)\pmod3.
$$



The integer sum is exactly $n$: it is the coefficient of
$x^{n+1}$ in


$$
(1+x)^n\sum_l(-1)^{n-l}\binom nl(1+x)^l
 =x^n(1+x)^n
$$

. The other residue classes of $l$ may be reinserted
in this sum because their displayed binomial factor is zero modulo
three. The border has $D_{n,r}\equiv-r\pmod3$, proving again
$\widehat P_e(1)\equiv V(1)\pmod3$.

Combining this with the previously reviewed classes $3\mid n$ and
$3\mid n+1$ makes the exponential endpoint a three-adic unit at
every degree. The sole boundary $n=1$ has the already fixed exact
values $V(t)=2-t$, $\widehat P_e(1)=-5$. For every $n\ge9$,
the factorial/Taylor threshold is positive: if 

$$
k=\lfloor n/3\rfloor
\ge3
$$

, then $2n\le6k+4<3^k$, while $v_3(n!)\ge k$.
Thus the factorial denominator lower bound is uniform at three from
that explicit sufficient threshold onward. This does not close the
remaining arithmetic needed for the research objective.

## 7. Optional whole-cofactor near-hook expression

The optional same-size formula in the target also checks. For
$q=n-1\ge2$, set $A=q^2+2$, $L=2q+j-1$, and
$\eta_j=(A,2,1^{L-2})$. This partition has size
$A+L=n^2+j$. At $j=0$, its first row contributes $q$ full
residue sets and extras $0,1$. The remainder of the first column
contributes two full sets with $0,1$ deleted, and box $(2,2)$
adds zero. Thus the total is $q+2$ full sets and an extra zero.
Appending a bottom box as $j$ increases adds content $2-j\pmod q$,
exactly the change in the actual cofactor partition.

The Frobenius coordinates are arms $(A-1,0)$ and legs $(L-1,0)$.
Their hook product is



$$
H_{\eta_j}=\frac{(A+L-1)A!L!}{(A-1)(L-1)}.
$$



The two-by-two Giambelli determinant is
$x\,s_{(A,1^{L-1})}-h_Ae_L$, and the standard hook expansion is
$s_{(A,1^{L-1})}=\sum_{r=0}^{L-1}(-1)^r h_{A+r}e_{L-1-r}$.
These yield exactly the target's formula (21). Reducing the background
parameter from $n$ to one is justified in the integral power sums,
whose differences are multiples of $n-1$. It is not a termwise
reduction of rational complete-function coefficients.

The denominator $L-1$ need not be a unit modulo $n-1$. The target
correctly requires forming the exact integer augmented polynomial
before reducing it. The same-size near-hook formula is consequently
valid, but does not by itself give an additional numerator-unit result.

## 8. Final stable-version cross-check and conclusion

The target states the weighted congruence using the cofactor index
$j$, whereas Section 3 of this review uses the coefficient index
$l$. These are compatible because $j=n-l$ and
$\binom nj=\binom nl$. In the target's notation, the weighted
cofactor scalar is $1+2j$; dividing by $M_D(1)\equiv-1$ gives
$-1-2(n-l)\equiv2l-3$, exactly the coefficient used in (D).
Thus the index reversal in passing from its (22) to the primitive
polynomial is sound.

The target's alternate proof for the high-tail terms with $a\ge2$
also passes: its factorization extracts $n(n-1)\cdots(n-a+1)$,
leaving a product of $2a$ consecutive integers divided by $a!$.
That quotient is integral. The entire $n-1$ divisor survives, not
only each of its primes. Its explicit discussion of Laurent series over
the composite ring handles possible zero divisors correctly.

All main claims now follow at their stated strength:

- The full determinant is congruent to
  $x^{n(n+1)}-2x^{n(n+1)-2}$ modulo $n-1$.
- The actual primitive polynomial is congruent to
  $V(1)(2t^{n-1}-t^n)$ at that same full modulus.
- The actual exponential endpoint is congruent to $-5V(1)$, with
  $V(1)$ a unit at every prime dividing $n-1$.
- The factorial lower bound for the actual reduced denominator holds
  at primes other than five under the specified Taylor-loss threshold.
- At $25\mid n-1$, the exponential endpoint has exactly one factor
  of five, giving the stated one-power loss for the actual denominator
  under the stronger threshold.
- The previously missing ternary residue class is closed, so the
  factorial denominator lower bound is uniform at three for all
  sufficiently large degrees.

The shallow class $v_5(n-1)=1$ and other prime residue classes remain
explicitly open. These results do not prove the original irrationality
objective or exclude every possible shrinking subsequence.
