> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the Machin rank proof and nested-exponential Padé note

Audited: 2026-08-26 UTC

## Scope and verdict

This is an adversarial audit of the following two notes, without editing either
target file:

1. `sources/machin_bordered_rank_proof.md`, including its dependence on
   `sources/raw_arctan_bordered_rank_proof.md`;
2. `sources/nested_exponential_pade_audit.md`.

The files at the audited checkpoint had SHA-256 hashes

```text
733267e4983672b66114b2649f430e221866e190aa7f49a2d7b028c929cc93e7  sources/machin_bordered_rank_proof.md
3ab3ec41f83ccfd5e45f0875465c1d6d3be0db8a0944c45c667ffc028d2c547d  sources/nested_exponential_pade_audit.md
6427308f1759e6ff6aa70cb634e66fb1edbfde3fb41406f037ff8cbb98f7bffd  scripts/machin_rank_crosscheck.py
d7323699208219da7fd50d4d54a493d5aade3c8a45303b949ac47b6e33aac133  results/machin_rank_crosscheck_n8.json
```

The verdicts are:

* **ACCEPT A.**  The all-degree full-row-rank theorem for the endpoint-matched
  Machin matrix is proved.  I found no normalization, parity, sign, index, or
  valuation gap in the proof.  Its stated limitations are accurate: this is a
  matrix theorem, not a nonvanishing or smallness theorem for the specialized
  endpoint linear form.
* **ACCEPT B.**  The integral Padé identity, two-sided noncancellation bound,
  conditional Lindemann--Weierstrass argument, algebraic-independence
  observation, height calculation, and asymptotics are all correct.  The note
  also correctly explains why the forms do not prove anything about the
  algebraicity or transcendence of $e+\pi$.

The finite computations described below are cross-checks rather than substitutes
for the proofs.

## A. Audit of the Machin bordered-rank proof

### A.1 Definitions and reduction to the square matrix

For positive odd $r$, direct expansion of



$$
G(z)=16\arctan(z/5)-4\arctan(z/239)
$$



gives



$$
g_r=4(-1)^{(r-1)/2}\frac{4\,5^{-r}-239^{-r}}{r},
$$



and the even coefficients vanish.  Thus division of the entire $C$-block
by $4$ produces exactly the kernel used later in the proof.

If the bordered $(2n+1)$-by-$(2n+2)$ matrix had row rank below
$2n+1$, its kernel would have dimension at least two.  Restricting the
linear functional $(B,C)\mapsto B(1)$ to that kernel therefore leaves a
nonzero vector in its kernel.  The endpoint equation then also gives
$C(1)=0$, irrespective of the rational border multiplier.  Factoring both
polynomials by $z-1$ gives, for $0\leq a<n$,



$$
[z^k]z^a(z-1)e^z=\frac{k-a-1}{(k-a)!},
$$



and



$$
[z^k]z^a(z-1)G(z)=g_{k-a-1}-g_{k-a}.
$$



The row range $k=n+1,\ldots,3n$ has exactly $2n$ rows, so the reduced
matrix $T_n$ is square of order $2n$.  This exactly matches the raw proof
under $m=n+1$ and $\ell=m-1=n$.  There is no off-by-one shift.

The converse endpoint assertion is also valid: nonsingularity of $T_n$
precludes a nonzero bordered-kernel vector with $B(1)=0$.  Hence every
nonzero vector has $B(1)\ne0$, and it has $C(1)\ne0$ when the border
multiplier is nonzero.

### A.2 Square part of the stability lemma

Let



$$
H(t)=\sum_{m\geq0}h_mt^m,\qquad h_m\in2^m\mathbb Z_2.
$$



For a polynomial truncation, each monomial in
$\det(H(x_i-y_j))$ has a factor $2^M$, where $M$ is its total degree
in the combined $x$- and $y$-variables.  Alternation separately in the
two sets forces degrees at least $q(q-1)/2$ in each set.  Division by the
two Vandermondes is integral because an alternating polynomial over
$\mathbb Z_2$ is divisible by the corresponding monic Vandermonde, with
integral quotient.  This proves the factor



$$
2^{q(q-1)}V(x)V(y).
$$



If at least one determinant entry is taken from
$H-H_0\in\mathcal A_h$, the same degree count has the additional factor
$2^h$.  Multilinear expansion of the determinant difference proves the
claimed normalized congruence.  Passing from polynomial truncations to the
series is legitimate because the defining coefficient bounds give uniform
$2$-adic convergence at every argument in $\mathbb Z_2$, while all
normalizing integers are fixed and nonzero.

This verifies both the integrality and congruence assertions in the square
case.

### A.3 Bordered part of the stability lemma

The upper-triangular finite-difference column operation has determinant one.
On the appended row it sends the $r$-th column to



$$
\sum_{j=0}^r(-1)^{r-j}\binom rj(-1)^j=(-1)^r2^r.
$$



For an ordinary row it gives an $r$-th forward or backward finite
difference of $H$; the orientation affects only harmless signs and integer
translations.  The key divisibility statement is correct:



$$
\frac{\Delta^rH(t)}{2^rr!}\in\mathcal A_0.
$$



Indeed, write ordinary powers in the integral falling-factorial basis and
use



$$
\Delta^r(t)_m=r!\binom mr(t)_{m-r}.
$$



Starting with a coefficient divisible by $2^m$, division by $2^r$
leaves $2^{m-r}$; every resulting term has degree at most $m-r$, which
is precisely the coefficient divisibility required for $\mathcal A_0$.
Integer translation preserves this property.  The same argument preserves
an additional common factor $2^h$ for a series in $\mathcal A_h$.

After expansion along the appended row, the powers of two from the ordinary
columns and the selected appended-row entry total



$$
2^{0+1+\cdots+s}=2^{s(s+1)/2}.
$$



The factorials in the remaining columns contain
$\prod_{j=0}^{s-1}j!$, since the leftover quotient is $s!/r!\in\mathbb Z$.
The determinant of the normalized ordinary columns is alternating in the
$s$ row variables.  The one-variable degree argument contributes



$$
2^{s(s-1)/2}V(x).
$$



The powers add to $s^2$, exactly as claimed.  Multilinearity again proves
the normalized congruence, and replacing $H_0$ by $cH_0$, with $c$ a
$2$-adic unit, multiplies the comparison determinant by $c^s$ (or by
$c^q$ in the square case).

I actively searched for counterexamples to both parts of the lemma using
exact rational arithmetic.  The test covered square sizes $q=1,\ldots,5$,
bordered sizes $s=1,\ldots,6$, nonconsecutive and negative row/pole
arguments, polynomial degrees through nine, congruence depths
$h=0,\ldots,6$, and odd unit scalings.  All 3,800 randomly generated exact
tests satisfied the asserted integrality and normalized congruence.  These
tests include cases in which the determinants vanish or have valuation well
above the universal bound.

For $n=1$, one parity factor can be a bordered block with zero ordinary
rows.  The lemma extends to this case by the standard empty-product and
zero-by-zero determinant conventions: the bordered determinant is the
one-by-one matrix $(1)$.  Alternatively, $n=1$ is checked directly.
This is only a presentational edge case, not a gap.

### A.4 The Machin kernel and its $2$-adic approximation

For $d=1+2t$, the divided Machin coefficient is, up to its already
extracted alternating sign,



$$
K_d=F(t)=\frac{N(t)}{1+2t},
$$



where



$$
N(t)=\frac45(1/25)^t-\frac1{239}(1/239^2)^t.
$$



The constant



$$
c=N(0)=\frac{951}{1195}
$$



is odd over odd and therefore a $2$-adic unit.  The logarithm valuations
used in the proof are exact:



$$
v_2(\log(1/25))=v_2(1/25-1)=3,
$$





$$
v_2(\log(1/239^2))=v_2(1/239^2-1)=5.
$$



For $r\geq1$, the two contributions to the coefficient of $t^r$ in
$N-c$ have valuations at least



$$
2+3r-v_2(r!)\geq r+4,
\qquad
5r-v_2(r!)\geq r+4.
$$



Cancellation can only increase these valuations.  Hence
$N-c\in\mathcal A_4$.  Since
$R(t)=(1+2t)^{-1}\in\mathcal A_0$, coefficient convolution gives



$$
F-cR\in\mathcal A_4.
$$



The use of $2$-adic powers at negative integer arguments is valid:
both bases lie in $1+8\mathbb Z_2$, their logarithms are in the convergence
domain of the $2$-adic exponential, and $1+2t$ is a unit throughout
$\mathbb Z_2$.  In the actual matrices all odd differences are positive
anyway.

### A.5 Exact normalization against the raw Cauchy determinant

After writing an original row point as



$$
x_i=p+1+2X_i,
$$



the kernel argument is $X_i-j$.  Therefore the universal bordered factor
from the stability lemma has valuation



$$
s^2+v_2(V(X))+A(s).
$$



The raw bordered-Cauchy formula in the comparison note has valuation



$$
s(s-1)+v_2(V(X))+A(s)+v_2(S_s).
$$



The normalized raw quotient consequently has valuation



$$
v_2(S_s)-s.
$$



The raw proof establishes this as zero for even $s$, at least one for odd
$s$, and exactly one in the odd equality case used later.  Congruence
modulo $16$ therefore does everything required:

* a normalized raw square determinant is a unit, so the Machin square
  determinant has exactly the same valuation;
* a raw bordered quotient of valuation zero or one retains that exact
  valuation after a perturbation divisible by $16$;
* in all other odd bordered cases, congruence to an even raw quotient still
  gives the required lower bound of one.

Thus the stability lemma has exactly the normalization needed by the raw
minor bounds.  There is no missing factor of $2$, a Vandermonde, or a
factorial.

### A.6 Incidence identity, parity splitting, and signs

For



$$
I_{j,a}=\mathbf1_{j=a+1}-\mathbf1_{j=a},
$$



one has $Q_U=M_UI$ entry by entry.  The maximal minors of this incidence
matrix are alternating units, giving



$$
\det Q_U=(-1)^n\det\begin{pmatrix}M_U\\1&\cdots&1\end{pmatrix}.
$$



The sign is confirmed already at $n=1$, and the general identity follows
by Laplace expansion or Cauchy--Binet.  No denominator is introduced.

For an even row and odd pole,



$$
(-1)^{(2K-(2J+1)-1)/2}=(-1)^{K-1}(-1)^J,
$$



and for an odd row and even pole,



$$
(-1)^{((2K+1)-2J-1)/2}=(-1)^K(-1)^J.
$$



Consequently the claimed row and column sign extraction is exact.  The
appended row becomes $(-1)^J$ within each parity block.  Opposite-parity
entries are the only nonzero entries, so a nonzero maximal minor factors
into one square kernel determinant and one bordered kernel determinant;
all other row-count profiles are structurally zero.

The two equality cases inherited from the raw proof also have the stated
indices:

* when $n=2r$, $U=\mathcal X\setminus S_0$ has consecutive parity
  rows, and the relevant first row-to-pole difference is $2r+1$, which is
  $3\pmod4$ exactly when the bordered size $r+1$ is even;
* when $n=2r+1$, $U=\mathcal X\setminus S_*$ again has consecutive
  parity rows, and the bordered first difference is $2r+1$, which is
  $3\pmod4$ exactly in the odd-row-count equality case.

Thus there is no hidden parity or pole-origin shift.

### A.7 Unique least-valuation Laplace term

The exponential-minor formula is unchanged from the raw proof.  Among the
$n$-subsets of $\{n+1,\ldots,3n\}$, only



$$
S_0=\{2n+1,\ldots,3n\}
$$



and



$$
S_*=\{2n\}\cup\{2n+2,\ldots,3n\}
$$



maximize $\sum_{u\in S}v_2(u!)$.  This follows from monotonicity of
$v_2(k!)$ and the sole boundary tie
$v_2((2n)!)=v_2((2n+1)!)$.  The additional Vandermonde cost for $S_*$
is $v_2(n)$.

For even $n$, the $S_0$ term attains all bounds and has an odd
$\Lambda(W_{S_0})$; $S_*$ pays the positive Vandermonde cost and every
other set loses in the factorial sum.  For odd $n$, the $S_*$ term
attains all bounds and has odd $\Lambda(W_{S_*})$; $S_0$ has even or
zero $\Lambda(W_{S_0})$, and every other set again loses in the factorial
sum.  The Machin perturbation preserves precisely the square and bordered
equality valuations needed for these statements.  Hence there is a unique
least-valuation summand, so the reduced determinant cannot vanish in
$\mathbb Q_2$.

I also substituted the definitions of $A$, $g$, and $\beta$ in the
raw comparison formulas.  In particular, for the two even-size parity
orientations,



$$
L_B-L_A=0\quad(r\text{ odd}),\qquad
L_B-L_A=2+2v_2(r)\quad(r\text{ even}),
$$



as quoted.  The odd-size orientations have the same lower bound.  The final
valuation comparison is therefore transferred correctly rather than merely
suggested by the finite data.

### A.8 Reproducibility checks

Running

```text
python scripts/machin_rank_crosscheck.py --max-n 8
```

reproduced `results/machin_rank_crosscheck_n8.json` byte for byte, with the
same SHA-256 hash
`d7323699208219da7fd50d4d54a493d5aade3c8a45303b949ac47b6e33aac133`.
The stored raw/Machin determinant valuation pairs are

```text
(-1,-1), (-5,-5), (-13,-13), (-25,-25),
(-33,-33), (-50,-50), (-69,-69), (-91,-91).
```

An additional exact `Fraction` run through $n=20$ found both determinants
nonzero and their $2$-adic valuations equal in every degree.  The final
five common valuations, for $n=16,\ldots,20$, were

```text
-327, -359, -394, -433, -476.
```

The stored JSON parses successfully, and the script compiles successfully.

### A.9 Verdict and scope

**ACCEPT.**  The proof establishes full row rank for every $n$ and the
stated endpoint-coefficient nonvanishing.  It does not establish
nonvanishing, decay, or primitive-height control for
$A(1)+B(1)(e+\pi)$.  The note makes that distinction correctly.

## B. Audit of the nested-exponential Padé note

### B.1 Integrality and the exact Padé identity

For $0\leq k\leq n$,



$$
\frac{(2n-k)!}{k!(n-k)!}
=\binom{2n-k}{n}\frac{n!}{k!}
$$



is an integer, so $P_n,Q_n\in\mathbb Z[z]$.

For a coefficient of degree $m>n$ in $Q_n(z)e^z$, multiplication by
$m!/n!$ converts the coefficient sum into



$$
\sum_{k=0}^n(-1)^k\binom mk\binom{2n-k}{n-k}.
$$



Terms with $k>n$ cannot contribute to $[x^n]$, so the sum is



$$
[x^n](1+x)^{2n}
\left(1-\frac{x}{1+x}\right)^m
=[x^n](1+x)^{2n-m}
=\binom{2n-m}{n}.
$$



For $n<m\leq2n$ this is zero; for $m\geq2n+1$, generalized-binomial
reflection gives



$$
(-1)^n\binom{m-n-1}{n}.
$$



Undoing the factor $m!/n!$ yields exactly equation (5) of the note.  The
coefficients through degree $n$ are exactly $P_n$, so they cancel.
Expanding the beta integral gives



$$
\frac{(-1)^nz^{2n+1}}{n!}
\sum_{r\geq0}\frac{z^r}{r!}
B(n+r+1,n+1)
=(-1)^n\sum_{r\geq0}
\frac{(n+r)!}{r!(2n+r+1)!}z^{2n+r+1},
$$



which is the same series.  Thus the identity is exact for every $n\geq0$.

As a finite independent check, exact rational coefficient comparison was
performed for $n=0,\ldots,12$, through degree $4n+8$.  Every coefficient
agreed with the integral formula.

### B.2 Upper bound, lower bound, and noncancellation

At $z=ie$, taking absolute values in the exact identity gives



$$
|\Lambda_n|\leq
\frac{e^{2n+1}}{n!}B(n+1,n+1)
=\frac{e^{2n+1}n!}{(2n+1)!}.
$$



Its consecutive ratio is exactly



$$
\frac{e^2(n+1)}{(2n+3)(2n+2)},
$$



so the upper bound tends to zero.

For the lower bound, set $u=t-1/2$.  Symmetry of
$t^n(1-t)^n$ makes the sine integral vanish, and hence



$$
\int_0^1t^n(1-t)^ne^{iet}\,dt
=e^{ie/2}\int_0^1t^n(1-t)^n\cos(eu)\,dt.
$$



The remaining real integral is positive.  Since $e<3<\pi$, one has
$|eu|\leq e/2<\pi/2$, and therefore



$$
\cos(e/2)B(n+1,n+1)
\leq\left|\int_0^1t^n(1-t)^ne^{iet}\,dt\right|
\leq B(n+1,n+1).
$$



This proves unconditional nonvanishing of every $\Lambda_n$, as well as
the fixed-factor two-sided estimate.  No phase or absolute-value step is
missing.

### B.3 Conditional Lindemann--Weierstrass claims

If $s=e+\pi$ is algebraic, Euler's identity gives
$e^{ie}=-e^{is}$.  Expanding $P_n(ie)$ and $Q_n(ie)e^{is}$ makes
$\Lambda_n$ an algebraic linear combination of exponentials with
exponents



$$
k\quad\hbox{and}\quad k+is,\qquad 0\leq k\leq n.
$$



These are distinct algebraic numbers: $s$ is the actual positive real
number $e+\pi$, so every exponent in the second family has nonzero
imaginary part.  The coefficients are Gaussian integers and are not all
zero.  Lindemann--Weierstrass therefore gives the claimed conditional
nonvanishing independently of the integral argument.

The stronger observation that $e=e^1$ and $e^{is}$ are algebraically
independent is also correct.  A nonzero polynomial relation would expand as
a nontrivial algebraic linear relation among



$$
e^{m+nis},
$$



where the finitely many exponents $m+nis$ are distinct algebraic numbers.
This contradicts Lindemann--Weierstrass.  The argument uses only
nonnegative integer $m,n$, as appropriate for an ordinary polynomial.

### B.4 Height and asymptotics

Writing



$$
a_k=\frac{(2n-k)!}{k!(n-k)!},
$$



one has



$$
\frac{a_{k+1}}{a_k}
=\frac{n-k}{(k+1)(2n-k)}<1
\qquad(0\leq k<n).
$$



Thus the coefficient height of $F_n$ is exactly



$$
H_n=a_0=\frac{(2n)!}{n!}.
$$



Stirling's formula gives



$$
\log H_n=n\log n+(2\log2-1)n+O(\log n).
$$



For the upper bound $U_n=e^{2n+1}n!/(2n+1)!$, it gives



$$
\log U_n=-n\log n+(3-2\log2)n+O(\log n).
$$



The fixed-factor lower bound proves



$$
-\log|\Lambda_n|=-\log U_n+O(1),
$$



and hence



$$
\lim_{n\to\infty}\frac{-\log|\Lambda_n|}{\log H_n}=1.
$$



Adding the two displayed logarithms gives
$\log(H_nU_n)=2n+O(\log n)$, so the product grows rather than tends to
zero.  All asymptotic constants in the note are consistent.

### B.5 Why the construction is not a proof about $e+\pi$

Even under the algebraicity hypothesis on $s$, the values
$F_n(e,e^{is})$ are not nonzero algebraic integers or nonzero rational
integers.  Qualitative algebraic independence supplies nonvanishing but no
height-free lower bound for a varying sequence of polynomial values.  The
fact that the values tend to zero is therefore fully compatible with
Lindemann--Weierstrass.  The note correctly refuses to apply an integer
linear-form criterion and correctly identifies the missing ingredient as a
sufficiently strong quantitative algebraic-independence measure.

### B.6 Verdict and scope

**ACCEPT.**  Every substantive displayed identity and inference in the
Padé note checks out.  The construction is a valid sharper reduction and a
valid no-go diagnosis, but neither an algebraicity proof nor a
transcendence proof for $e+\pi$.

