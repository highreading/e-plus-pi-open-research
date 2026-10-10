> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 338 - secondary Cartier carries, safe saturation, and the diagonal obstruction

Checked: 2026-09-01 (Beijing time)

## 1. Scope and strict verdict

Retain the actual ordinary-$j=2$ row



$$
p=2r+6s+3=6m+2d+1,
 \qquad m=s-1,
 \qquad d=r+4,
\tag{1.1}
$$



and Item 334's primitive target-retaining carrier



$$
\mathfrak G_{r,s}
 =\gcd\bigl(|\operatorname {num}D|,
             |\operatorname {num}T_0|,
             |\operatorname {num}T_1|\bigr).
\tag{1.2}
$$



Item 334 proves the exact actual-family equivalence



$$
p\text{ is an original collision on }(r,s)
 \quad\Longleftrightarrow\quad p\mid\mathfrak G_{r,s}.
\tag{1.3}
$$



Item 336 showed that affine resultants and qualitative carrier data do
not reduce the raw fixed-$M$ ceiling.  The present item examines the
first genuinely nontrivial foreign carrier primes, $23$ and $173$,
and proves the global base-prime Cartier decomposition that governs the
coefficient $c_p$.

The outcome is a rigorous obstruction, not a density theorem.

> **PROVED - two-state secondary Cartier theorem.**  For every prime
> $\lambda$, the global coefficient $c_p\bmod\lambda$ is an exact
> product of two-state base-$\lambda$ carry matrices.

> **PROVED - diagonal collapse.**  On the only specialization relevant
> to the collision ledger, $\lambda=p$, the matrix product has one
> surviving path and its only nontrivial entry is $c_p$ itself.  Thus
> the secondary-prime Frobenius factorization does not compress or
> further constrain the diagonal coefficient.

> **PROVED - tied-prime-safe saturation.**  Prime factors supported by
> the known ingredient denominators or by $\binom{2m}{m}$ can be
> removed from $\mathfrak G_{r,s}$ without changing (1.3).  The two
> requested hits $23$ and $173$ both disappear after this
> saturation, for different exact reasons.

> **PROVED - scoped no-go.**  A method using only (i) the base-prime
> carry factorization of $c_p$, (ii) finite-state dimension, and
> (iii) off-diagonal prime factors of the raw carrier supplies no new
> fixed-$M$ restriction.  A successful theorem must control the
> *diagonal correlation* between the old determinant gate and the
> moving affine target.

Consequently



$$
\boxed{\text{new booking}=0},\qquad
 \boxed{\text{new capacity reduction}=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling}=1/105\text{ per }6M}.
\tag{1.4}
$$



No finite carrier census is promoted.

## 2. The actual global coefficient

Item 328 writes



$$
F_{m,d}(x)=(1-x)^n(1+x)^{n+q}
            =\sum_k c_kx^k,
\tag{2.1}
$$



where



$$
n=3m+d=\frac{p-1}{2},\qquad
 q=2m+d,
\tag{2.2}
$$



so that



$$
n+q=p-m-1<p,
 \qquad c_p=[x^p]F_{m,d}(x).
\tag{2.3}
$$



The true Cartier target retained by Item 334 is



$$
\Phi_{r,s}=c_p+\epsilon_p h_mP_{r+2}(m),
 \qquad
 h_m=\frac1{8^m}\binom{2m}{m},
\tag{2.4}
$$



not $c_p$ by itself.  On a nondegenerate coordinate chart the second
collision condition has the form



$$
\Phi_{r,s}\equiv\Theta_{r,s}\pmod p,
\tag{2.5}
$$



where $\Theta_{r,s}$ is the legitimate moving affine target obtained
from $T_\nu=0$.  It is essential that (2.5) remain coupled to
$D\equiv0\pmod p$.

## 3. The all-prime two-state carry theorem

Let $\lambda$ be any prime and, temporarily, let



$$
a,b,k\geq0,
 \qquad
 a=\sum_i a_i\lambda^i,quad
 b=\sum_i b_i\lambda^i,quad
 k=\sum_i k_i\lambda^i
\tag{3.1}
$$



be their base-$\lambda$ expansions.  Put



$$
F_i(X)=(1-X)^{a_i}(1+X)^{b_i},
 \qquad
 u_i(j)=[X^j]F_i(X),
\tag{3.2}
$$



where $u_i(j)=0$ outside $0\leq j\leq a_i+b_i$.  For incoming and
outgoing carries $\alpha,\beta\in\{0,1\}$, define



$$
\mathcal M_i(\alpha,\beta)
 =u_i(k_i-\alpha+\lambda\beta).
\tag{3.3}
$$



> **PROVED - exact carry product.**
> 

$$
> \boxed{
> [X^k](1-X)^a(1+X)^b
> \equiv e_0^{\mathsf T}
>       \mathcal M_0\mathcal M_1\cdots\mathcal M_L e_0
>       \pmod\lambda,}
> \tag{3.4}
>
$$


> after adjoining one terminal zero digit.

Indeed, the freshman's-dream factorization gives



$$
(1-X)^a(1+X)^b
 \equiv\prod_iF_i(X^{\lambda^i})\pmod\lambda.
\tag{3.5}
$$



Every local degree is at most $2\lambda-2$, so only carries $0,1$
occur.  Equality of the $i$-th digit is precisely



$$
j_i=k_i-\alpha_i+\lambda\alpha_{i+1}.
\tag{3.6}
$$



Summing the products of the local coefficients over all carry paths
from $\alpha_0=0$ to the terminal carry $0$ proves (3.4).  This is
an all-prime theorem; it is not inferred from a scan.

For the actual coefficient, substitute



$$
a=n,\qquad b=n+q=p-m-1,qquad k=p.
\tag{3.7}
$$



## 4. Why the global Cartier product collapses on the diagonal

Now take $\lambda=p$.  Equations (2.2)-(2.3) give



$$
0\leq n<p,qquad0\leq n+q<p,qquad p=(0,1)_p.
\tag{4.1}
$$



Thus both exponent digit strings have only their zeroth digit.  At the
zeroth digit, a path ending with carry zero has local degree zero, but
it dies at the next digit because the target digit there is one.  The
unique surviving path is



$$
0\longrightarrow1\longrightarrow0.
\tag{4.2}
$$



Its weights are



$$
\mathcal M_0(0,1)=[X^p](1-X)^n(1+X)^{n+q}=c_p,
 \qquad
 \mathcal M_1(1,0)=1.
\tag{4.3}
$$



Therefore



$$
\boxed{e_0^{\mathsf T}\prod_i\mathcal M_i e_0=c_p\pmod p.}
\tag{4.4}
$$



Equation (4.4) is not merely a failure of one chosen recurrence depth.
It is the exact global base-$p$ factorization, with every digit
retained.  Its distinguished transition is the original unknown
coefficient.  Finite-state dimension, digit length, or formal
Frobenius factorization alone therefore gives no diagonal nonvanishing
or zero-density statement.

This does not close arithmetic study of the matrices.  A theorem about
their actual target-correlated distribution could still help.  It
closes only the use of the factorization identity or bounded state
dimension as a sufficient argument.

## 5. Exact anatomy of the hits 23 and 173

The first two carrier primes beyond $3,7$ arise by different
off-diagonal mechanisms.

### 5.1 The carrier 23: bad intermediate reduction

For



$$
(p,r,s,m)=(331,17,49,48),\qquad\lambda=23,
\tag{5.1}
$$



the relevant base-23 digits are



$$
p=(9,14)_{23},\quad n=(4,7)_{23},\quad
 n+q=(6,12)_{23}.
\tag{5.2}
$$



The two possible carry contributions in (3.4) are $20$ and $0$,
so



$$
c_{331}\equiv20\pmod{23}.
\tag{5.3}
$$



The reduced final rationals $D,T_0,T_1$ all have denominator a
23-unit and numerator valuation exactly one.  Hence



$$
\mathfrak G_{17,49}=23.
\tag{5.4}
$$



However the unrecombined ingredients $b_0,b_1,\kappa_{17}$ each
have reduced denominator valuation one at 23.  The finite target is
created only after exact cancellation of these poles.  Consequently 23
is a bad-intermediate-reduction prime for this representation, not a
model for the tied specialization $\lambda=p$, where Item 334 proves
all such denominators are units.

### 5.2 The carrier 173: a Kummer carry

For



$$
(p,r,s,m)=(599,7,97,96),\qquad\lambda=173,
\tag{5.5}
$$



all displayed ingredient denominators are 173-units.  The two-digit
data are



$$
p=(80,3)_{173},\quad n=(126,1)_{173},\quad
 n+q=(156,2)_{173}.
\tag{5.6}
$$



The no-carry and one-carry contributions are respectively 171 and 164;
therefore



$$
c_{599}\equiv171+164\equiv162\pmod{173}.
\tag{5.7}
$$



There is exactly one carry in adding $96+96$ in base 173.  Kummer's
theorem, or the direct factorial valuation, gives



$$
v_{173}\binom{192}{96}=1,qquad h_{96}\equiv0\pmod{173}.
\tag{5.8}
$$



Thus the correction in (2.4) vanishes.  Exact reduction of either
coordinate chart gives



$$
\Phi_{7,97}\equiv\Theta_{7,97}\equiv162\pmod{173},
\tag{5.9}
$$



and $D,T_0,T_1$ again have numerator valuation one and unit
denominator.  Hence



$$
\mathfrak G_{7,97}=173.
\tag{5.10}
$$



This is a genuine good-reduction foreign target hit.  It still cannot
occur by the same mechanism on the diagonal: from (1.1),



$$
2m<p,
\tag{5.11}
$$



so $p\nmid\binom{2m}{m}$.

### 5.3 A rejected character conjecture

The four first examples $3,7,23,173$ suggested that the carrier prime
might always have quadratic character of 2 opposite to that of the tied
prime.  This is false.  Exact counterexamples are



$$
(p,r,s,\mathfrak G)=(251,1,41,3),\qquad(281,1,46,7),
\tag{5.12}
$$



where the two characters agree in both rows.  Equation (5.12) is
**EXACT FINITE ONLY**; it refutes the universal character claim but
implies no density statement.

## 6. A tied-prime-safe saturation theorem

Let $\mathscr I_{r,s}$ be the exact ingredient list



$$
f_0,f_1,b_0,b_1,v_0,v_1,B_s,\kappa_r,\tau_{r,s},h_m,P_{r+2}(m),
\tag{6.1}
$$



and define



$$
S_{r,s}
 =6\binom{2m}{m}
   \prod_{x\in\mathscr I_{r,s}}\operatorname {den}(x).
\tag{6.2}
$$



For positive integers $A,S$, write $A_{(S)}$ for the largest
divisor of $A$ coprime to $S$; equivalently, remove from $A$ the
full prime powers at primes dividing $S$.  Put



$$
\mathfrak G^{\rm sat}_{r,s}
 =\bigl(\mathfrak G_{r,s}\bigr)_{(S_{r,s})}.
\tag{6.3}
$$



> **PROVED - diagonal-safe saturation.**  On every actual row,
> 

$$
> \boxed{
> p\mid\mathfrak G_{r,s}
> \quad\Longleftrightarrow\quad
> p\mid\mathfrak G^{\rm sat}_{r,s}.}
> \tag{6.4}
>
$$



Item 334 proves that the denominators in (6.1) are $p$-units, while
$p>2m$ proves that the central binomial coefficient is a $p$-unit.
Also $p\geq11$.  Hence $p\nmid S_{r,s}$, and removing
$S_{r,s}$-supported prime powers cannot change divisibility by $p$.
This proves (6.4).

The two exact mechanisms above give



$$
\mathfrak G^{\rm sat}_{17,49}=1,
 \qquad
 \mathfrak G^{\rm sat}_{7,97}=1.
\tag{6.5}
$$



For 23 this is denominator saturation; for 173 it is central-binomial
saturation.  Formula (6.3) is tied-prime-specific and is not claimed to
preserve the complete foreign-prime support of Item 334's canonical
primitive carrier.

## 7. Capacity consequence and the exact missing input

On a fixed-$M$ slice,



$$
\frac{4M+3}{5}\leq p\leq\frac{6M-1}{7},
\tag{7.1}
$$



and Item 336 proves the raw prime mass



$$
\sum_{p\text{ in }(7.1)}\log p
 =\frac{2}{35}M+o(M).
\tag{7.2}
$$



Saturation does not reduce this worst-case ceiling: the actual tied
prime is deliberately never removed.  If every tied row collided, each
such $p$ would still divide $\mathfrak G^{\rm sat}_{r,s}$.  Thus
the normalized ceiling remains



$$
\frac1{6}\frac{2}{35}=\frac1{105}.
\tag{7.3}
$$



The first foreign carrier hits therefore cannot be used as evidence for
or against tied-prime density.  Raw product or norm computations mix
three distinct phenomena:

1. bad intermediate reduction, as at 23;
2. off-diagonal factorial carries, as at 173; and
3. the unsolved diagonal correlation (2.5).

The smallest sufficient theorem is now most sharply stated as



$$
\boxed{
 \sum_{\substack{(r,s)\in\mathcal R_M\\
 D\equiv0\ (p)\\
 c_p+\epsilon_ph_mP_{r+2}(m)\equiv\Theta^{\rm chart}_{r,s}\ (p)}}
 \log p=o(M).}
\tag{7.4}
$$



Here $\Theta^{\rm chart}$ means the appropriate nondegenerate
coordinate or exterior target from Item 334; the chart-free equivalent
is $p\mid\mathfrak G^{\rm sat}_{r,s}$.  What is newly delimited is the
required input: a distribution, monodromy, large-sieve, or average-gcd
theorem for the *joint moving target* on the diagonal.  Another digit
factorization, state-dimension bound, or census of foreign factors does
not address (7.4).

## 8. Deterministic replay and labels

The certificate verifies:

- 20,160 exact finite comparisons between direct coefficients and the
  two-state carry product for $\lambda=3,5,7,11$;
- diagonal collapse on six declared actual rows through $p=599$;
- the exact carriers 23 and 173, including valuation one in all three
  primitive numerators;
- the two digit-path decompositions (5.3) and (5.7);
- bad-denominator support at 23 and the Kummer valuation at 173;
- the target equality (5.9);
- saturation (6.5); and
- the two character counterexamples (5.12).

The symbolic proof of (3.4), diagonal proof (4.1)-(4.4), saturation
proof (6.2)-(6.4), and capacity implication (7.1)-(7.3) are
**PROVED**.  All bounded row lists, digests, and numerical examples are
**EXACT FINITE ONLY**.

The following remain **OPEN**:

- the weighted diagonal correlation theorem (7.4);
- any strict improvement of the $1/105$ ceiling;
- any positive Route 1 booking from ordinary $j=2$; and
- an all-row structural description of
  $\mathfrak G^{\rm sat}_{r,s}$.
