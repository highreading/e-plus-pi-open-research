> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Integral content congruences at n+1 and actual factorial denominator depth

Date: 2026-09-13. Original arithmetic continuation by audit_results.
Independent review: **FULL PASS** by audit_computations; see
raw_appell_neighbor_content_independent_review.md.
No new canonical degree, prime, or root scan
is used. The source theorem is applied integrally, so the conclusions below
retain the entire modulus $n+1$, not only its prime support.

This note proves a new uniform result at every prime dividing $n+1$.
It extends beyond the already reviewed special families $n=p^\nu-1$.
The key input is integral generation of the symmetric-group centre by
symmetric polynomials in Jucys--Murphy elements. A prime-block statement
alone would not justify the composite-modulus step used here.

## 1. Actual objects and the new conclusions

Retain the already reviewed normalization


$$
a_k(x)=[t^k]e^{xt}(1+t^2)^n,\qquad
 A_n(x)=(a_{n+i-j}(x))_{0\le i,j\le n}.
$$


Put


$$
\lambda_D=(n^{n+1}),\quad N=n(n+1),\quad
 \lambda_j=((n+1)^j,n^{n-j}),\quad N_j=n^2+j.
$$


Write $H_\lambda$ for the hook product and
$M_\lambda=H_\lambda s_\lambda(a(x))$. Thus
$M_D=H_D\det A_n$, and $M_j$ is the normalized inverse-column minor
used in raw_appell_all_cofactors_and_endpoint_units.md.

The following are integer-polynomial congruences for every $n\ge1$:


$$
\boxed{M_D(x)\equiv x^{n(n+1)}\pmod{n+1},}                 \tag{1}
$$




$$
\boxed{M_j(x)\equiv x^{n^2+j}
       +j(j+1)x^{n^2+j-2}\pmod{n+1},\quad 0\le j\le n.}   \tag{2}
$$


The second term is omitted when its coefficient is zero or its exponent
would be negative. In particular,


$$
M_D(1)\equiv M_0(1)\equiv M_n(1)\equiv1\pmod{n+1}.         \tag{3}
$$


The intermediate minors need not be units.

In the **actual primitive dual normalization**, these imply


$$
\boxed{\gcd(V_n(1),n+1)=\gcd(V_{n,\mathrm{lead}},n+1)=1,}
 \qquad
 \boxed{V_n(1)\equiv V_{n,\mathrm{lead}}\pmod{n+1}.}         \tag{4}
$$


For every prime $p\mid n+1$,


$$
v_p(\operatorname{cont}U_n)=v_p(n!),\qquad
 v_p(Z_n)\ge v_p(n!),\qquad v_p(\widehat P_{e,n}(1))=0.     \tag{5}
$$


When $v_p(n!)>\lfloor\log_p(2n)\rfloor$, the actual reduced denominator
satisfies


$$
\boxed{v_p(q_n)=v_p(Z_n)\ge v_p(n!).}                     \tag{6}
$$


The prime-two case needs no threshold. For a fixed odd prime, (6) applies
to **every sufficiently large integer $n\equiv-1\pmod p$**, with
no restriction on the other factors of $n+1$.

## 2. The integral central-character lemma

The primary source used here is Christopher Ryba, *Stable centres of
wreath products*, Algebraic Combinatorics 6 (2023), 413--455,
Proposition 3.11, the integral isomorphism in Theorem 3.8, and
Theorem 3.14. At fixed symmetric-group size $s$, every class sum is an
integer-coefficient symmetric polynomial in the Jucys--Murphy elements.
On the irreducible representation indexed by a partition, its scalar is
that symmetric polynomial evaluated at the multiset of box contents.
[Primary paper](https://alco.centre-mersenne.org/item/10.5802/alco.264.pdf).

The integrality can also be seen directly from the triangular assertion
in Proposition 3.11. A monomial symmetric polynomial in the JM elements
is its indicated reduced-cycle class sum, with coefficient one, plus
integer multiples of class sums earlier in a finite order. Induction
expresses each class sum as an integer symmetric polynomial. Thus no
rational division is introduced. The parameter-dependent formulation
uses integer-valued polynomials evaluated at the fixed size $s$, which
again gives integer coefficients.

**Lemma.** Suppose $\lambda,\eta\vdash s$, and their multisets of box
contents agree modulo an integer $q\ge2$, including multiplicities.
Then


$$
H_\lambda s_\lambda\equiv H_\eta s_\eta
      \pmod{q\,\mathbb Z[p_1,p_2,\ldots]}.                 \tag{7}
$$



**Proof.** For every conjugacy class $\mathcal C_\mu$, its central scalar


$$
\omega_\lambda(\mathcal C_\mu)
 =|\mathcal C_\mu|\chi^\lambda(\mu)/f^\lambda
$$


is the value of an integer symmetric polynomial on the contents.
Matching the two content multisets modulo $q$ makes these scalars
congruent modulo $q$. Frobenius's formula says exactly


$$
H_\lambda s_\lambda
   =\sum_{\mu\vdash s}\omega_\lambda(\mathcal C_\mu)p_\mu.
$$


Thus the congruence holds coefficientwise. Both partitions have the
same size, so all integer-valued size parameters are evaluated at the
same integer. This proves (7) for arbitrary $q$, including prime
powers and composite moduli. $\square$

The lemma is stronger than the consequence obtained solely from equal
prime cores and ordinary block theory: no unproved lift from modulo
$p$ to modulo $p^a$ is used.

## 3. The exact content multisets of the actual rectangles and minors

Set $q=n+1$. For the full rectangle $\lambda_D=(n^q)$, each column
has $q$ consecutive contents. Hence its contents contain each residue
modulo $q$ exactly $n$ times. The row partition $(N)$, with
$N=nq$, has the same multiset of contents modulo $q$. The lemma gives


$$
M_D(x)\equiv
 N![t^N]e^{xt}(1+t^2)^n\pmod q.                           \tag{8}
$$


The right side is


$$
\sum_{h=0}^{\min(n,\lfloor N/2\rfloor)}
  \binom nh (N)_{2h}x^{N-2h}.
$$


Every $h\ge1$ term contains $N$, which is divisible by $q$.
This proves (1), coefficientwise.

For the square $(n^n)$, a direct residue count gives $q-2$ copies
of each residue, plus one extra zero. Indeed the row and column indices
run through all nonzero residues modulo $q$; there are $q-1$ pairs
with equal residues and $q-2$ pairs for any specified nonzero difference.

The shape $\lambda_j$ adds $j$ boxes in column $q$, in rows
$1,\ldots,j$. Their contents are $-1,\ldots,-j$ modulo $q$.
Therefore its complete content multiset is


$$
q-2\text{ copies of every residue, plus }0,-1,\ldots,-j. \tag{9}
$$


Its size is $N_j=q(q-2)+(j+1)$. The single column
$(1^{N_j})$ has exactly the content multiset (9). These statements
include $q=2$, where the uniform multiplicity $q-2$ is zero.

Apply (7) to this column partition. Under our complete-function
specialization the elementary generating series is


$$
\sum_{k\ge0}e_k t^k
 =\frac1{\sum_{k\ge0}a_k(x)(-t)^k}
 =e^{xt}(1+t^2)^{-n}.
$$


Thus


$$
M_j(x)\equiv
 N_j![t^{N_j}]e^{xt}(1+t^2)^{-n}\pmod q.                  \tag{10}
$$


This elementary function arises because the comparison partition is a
column; the actual minors retain their original complete-function
convention throughout.

For $s=N_j$ the right side of (10) is


$$
\sum_{h=0}^{\lfloor s/2\rfloor}
 (-1)^h\binom{n+h-1}{h}(s)_{2h}x^{s-2h}.                 \tag{11}
$$


When $h\ge2$, write its coefficient as


$$
(-1)^h\,n(n+1)\cdots(n+h-1)\frac{(s)_{2h}}{h!}.
$$


The last ratio is an integer because $(s)_{2h}$ is divisible by
$(2h)!$. Hence every such coefficient contains $q=n+1$;
there is no denominator loss even when $h!$ contains $q$'s primes.
The remaining $h=1$ term is $-n\,s(s-1)x^{s-2}$.
Modulo $q$, $-n\equiv1$, $s\equiv j+1$, so its coefficient
is $j(j+1)$. This proves (2) and (3).

## 4. Primitive normalization forces actual endpoint units

Retain the original primitive polynomials and the exact reviewed relations


$$
W=t^n(t-1)^nV,\qquad
 b_j=U_j/(n+j)!\in\mathbb Z,\qquad \gcd_j b_j=1.
$$


The last assertion follows from two integral triangular transformations
with diagonal one, from the coefficients of primitive $V$ to the
high coefficients of $W$, and then to $b$. It is independent of
any new local unit claim.

The exact cofactor formula, not just its congruence, is


$$
b_j=(-1)^{n-j}\binom nj V(1)\frac{M_{n-j}(1)}{M_D(1)}.    \tag{12}
$$


Let $p\mid q$. By (3), $M_D(1)$ is a $p$-unit; each $M_{n-j}$
is an integer. If $V(1)$ were divisible by $p$, equation (12)
would make every $b_j$ divisible by $p$, contradicting primitivity.
Thus $V(1)$ is a unit.

Since $b_n=V_{\rm lead}$, and $M_0(1)/M_D(1)\equiv1\pmod q$
in the ring with denominators prime to $q$, (12) at $j=n$ gives
the full integer congruence $V_{\rm lead}\equiv V(1)\pmod q$.
This proves (4), retaining all prime-power depths dividing $n+1$.

For completeness, the inverse-column ratio itself satisfies


$$
\frac{v_j}{(-1)^jr_j}
  =\frac{M_j(1)}{M_D(1)}
  \equiv1+j(j+1)\pmod{q\,\mathcal R_q},\qquad
 r_j=\frac{(2n-j)!}{j!(n-j)!},                            \tag{13}
$$


where $\mathcal R_q$ consists of rational numbers whose reduced
denominators are prime to $q$.
Formula (13) is not a unit assertion for every $j$; for example its
right side is zero modulo three at $j\equiv1\pmod3$.

Combining (4) with the previously reviewed $2n$ result gives


$$
\gcd(V(1)V_{\rm lead},\,2n(n+1))=1,\qquad
 V(1)\equiv V_{\rm lead}\pmod{\operatorname{lcm}(2n,n+1)}.
                                                               \tag{14}
$$


No monomial congruence for the whole polynomial $V$ modulo $n+1$
is claimed.

## 5. Global factorial divisibility and the exact local content

The integrality of every $b_j$ already implies
$n!\mid\operatorname{cont}U$ for every $n$, globally.
With $S=(1+t^2)^nU$, the exact reconstruction


$$
\widehat Q(z)=z^{2n}S^{(n)}(1/z)/n!
$$


maps $S_k$ to $\binom kn S_k$. Therefore


$$
n!\mid\operatorname{cont}U
 \mid\operatorname{cont}\widehat Q,\qquad n!\mid Z,
                                                               \tag{15}
$$


without any prime restriction. This uses the divided derivative with
its precise factorial, not an assumption that differentiation preserves
content.

At $p\mid n+1$, equation (12) with $j=0$, together with (3), shows
that $b_0$ is a unit. Consequently $U_0=n!b_0$ has valuation
exactly $v_p(n!)$, proving


$$
v_p(\operatorname{cont}U)=v_p(n!).                       \tag{16}
$$


The inequality for $\widehat Q$ and $Z$ in (5) follows from (15).
No exact equality for either of these latter valuations is asserted.

## 6. The evaluated numerator and the actual reduced denominator

The passed exponential endpoint border has the corrected orientation


$$
\widehat P_e(1)=\sum_{r=0}^n V_rD_{n,r},\qquad
 D_{n,r}=\sum_{j=0}^{n+r}\binom{n+j}{j}(n+r)_j.
$$


For each $j\ge1$ its coefficient satisfies the all-integer identity


$$
\binom{n+j}{j}(n+r)_j
 =(n+1)(j-1)!\binom{n+j}{j-1}\binom{n+r}{j}.
$$


Thus


$$
D_{n,r}\equiv1\pmod{n+1},\qquad
 \boxed{\widehat P_e(1)\equiv V(1)\pmod{n+1}.}             \tag{17}
$$


This congruence was already proved in the prime-power-minus-one work;
what is new here is the unit conclusion for every divisor of $n+1$.

Every rational coefficient in the Taylor truncation of $\arctan$
through degree $2n$ has denominator dividing
$\operatorname{lcm}(1,\ldots,2n)$.
Using the global divisor (15) gives


$$
v_p(\widehat P_a(1))\ge
 v_p(n!)-\lfloor\log_p(2n)\rfloor.                        \tag{18}
$$


For $p\mid n+1$, if the right side is positive, then (17) forces
$N=\widehat P_e(1)+4\widehat P_a(1)$ to be a unit.
The actual exact reduction


$$
q_n=|Z_n|/\gcd(|Z_n|,|N_n|)
$$


therefore proves (6), with its full factorial depth.

At $p=2$, the previously reviewed exponential unit at every degree
and integrality of $\widehat P_a$ make $N$ odd regardless of (18).
For each fixed odd $p$, Legendre's formula shows that the threshold
in (18) holds for every sufficiently large $n$. Hence, uniformly on
the entire residue class $n\equiv-1\pmod p$,


$$
v_p(q_n)\ge n/(p-1)-O_p(\log n).                         \tag{19}
$$


The same statement for $n\equiv0\pmod p$ was proved in the preceding
Appell note. This is not an assertion for the other residue classes.

On the already reviewed special family $n=p^\nu-1$, the previous
identity $d_p+v_p(V(1))=\nu$ now yields $d_p=\nu$ and $e_p=0$.
The previously proved exact formula $v_p(q_n)=v_p(n!)$ on that family
is consistent with (6); it is not used to prove the present theorem.

## 7. A wider explicit family of excluded even degrees

For even $n$ with


$$
3\cdot5\cdot7\cdot11\mid n(n+1),
$$


each indicated odd prime lies in one of the two now-proved residue
classes. The exact dyadic rate and (19), or its $p\mid n$ counterpart,
give the same lower exponential rate as at multiples of $2310$:


$$
\liminf\frac{\log q_n}{n}\ge
 \frac32\log2+\frac{\log3}{2}+\frac{\log5}{4}
 +\frac{\log7}{6}+\frac{\log11}{10}>5\log\phi.
$$


The numerical-free inequality is proved in
raw_appell_column_endpoint_independent_review.md.
The accepted even error asymptotic therefore makes the absolute
primitive forms tend to infinity along these degrees.

By the Chinese remainder theorem these comprise exactly sixteen
residue classes modulo $2310$: choose independently residue zero or
minus one at each of the four odd primes, and impose even parity.
This is a deterministic residue-class consequence, not an arithmetic
scan. It excludes more than the single earlier class of multiples
of $2310$, while leaving other even subsequences open.

## 8. Limits and a precise next target

The integral content comparison establishes the full normalized-minor
congruences (1)--(2) at $n+1$. It does not identify the other residue
classes of $n$ modulo an odd prime with the trivial or sign
representation: their content multiplicities differ.

For a fixed prime $p$, the residual rectangle of size
$r(r+1)$, $r=n\bmod p$, describes the nonuniform part of the
full rectangle's content residues. An extension must evaluate the
associated central-character specialization at the same symmetric-group
size, or prove a justified size-reduction formula. Simply deleting the
uniform content blocks changes the group size and its integer-valued
character-polynomial coefficients; that is not an automatic congruence.
This finite-residue specialization is the next concrete target.
