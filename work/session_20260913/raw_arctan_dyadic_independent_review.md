> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the raw-arctangent primitive dyadic theorem

Date: 2026-09-13. Reviewed `raw_arctan_endpoint_dyadic_attempt.md`
Sections2–6 against `sources/raw_arctan_endpoint_arithmetic.md`, including
its definitions of the actual augmented determinants and primitive ratio.

## Verdict

No substantive gap was found. The new argument proves



$$
v_2(\Delta_{A,n})=\phi(n)+\sum_{k=n+1}^{2n}\phi(k)+3S(n)-n
$$



in every degree. Combined with the established all-degree Delta_B
valuation and the exact cofactor normalization, it proves the actual
reduced denominator formula



$$
\boxed{v_2(q_n)=n+2\lfloor(n+2)/4\rfloor.}
$$



The endpoint gcd is retained. The result is not merely a raw cofactor
valuation or divisibility of an arbitrary polynomial normalization.

Because the displayed valuations strictly increase with n, the rational
endpoint approximants are pairwise distinct. Thus at most one evaluated
form can vanish for any fixed target, including e+pi. This is an
unconditional eventual-nonvanishing theorem; it does not assert which
index, if any, is exceptional and does not prove primitive shrinkage.

## 1. Actual row definitions and determinant scales

The canonical family uses C arctan(z) with C(1)=4B(1), so at the endpoint
its irrational part is B(1)(e+pi). The border row is therefore exactly
(-4,...,-4 | 1,...,1). This factor4 contributes valuation2 in the two
Laplace cases that put the border in the exponential block.

The high integer jet row at k is k! times the rational coefficient row
(1/(k-j)! | t_(k-j)). The archive's appended A row is exactly n! times



$$
(-E_{n-j}\mid-T_{n-j}),
$$



because all low Taylor coefficients through degree n determine A. It is
the actual endpoint functional, not a selected Taylor coefficient or
an auxiliary evaluation. Therefore



$$
\Delta_A=n!\prod_{k=n+1}^{3n}k!\det M_A
$$



up to only the harmless column-order sign when C columns are reversed.
The source retains both n! and every high-row factorial in its valuation
restoration. The n=0 determinant and primitive ratio agree with
(-1,1,4), so treating n>=1 in the main proof is legitimate.

## 2. Dyadic integrality and the universal moment bounds

For L(t^a)=t_(a+1), all denominators are odd. The monic raw Legendre
recurrence has coefficient j^2/(4j^2-1), whose denominator is odd, so
every Q_j belongs to Z_(2)[t]. Its norm is exactly



$$
h_j=\frac{(-1)^j2^{2j}}{(2j+1)\binom{2j}{j}^2},
 \qquad v_2(h_j)=2j-2s_2(j)=2\phi(j).
$$



These norms are nonzero even when several consecutive norms have equal
valuation. The latter plateaus cause no problem for the lower bounds.

For any moment row L(F_i times a polynomial), expand F_i in the monic
Q basis. This expansion has coefficients in Z_(2), because the basis
change and its inverse are unitriangular over that ring, even when F_i
has degree greater than the column range. Orthogonality gives
L(F_i Q_j)=h_j times an integral coefficient. Thus each moment column
has its asserted norm factor. With one extra integral functional row,
expansion along that row leaves n norms chosen from h_0,...,h_n.
Their least possible valuation sum is2S(n), since phi is nondecreasing.
An entirely moment matrix of size n+1 has bound2S(n+1).

These are lower bounds term by term in a dyadic ring. Cancellation can
increase valuations but cannot invalidate them.

## 3. Both C endpoint rows and the exact candidate Gram minor

After reversal, C column j is t^j. The high row at k is
L(t^(k-n-1) times a polynomial), while the A endpoint row is
D(t^j)=-T_j. Direct subtraction gives



$$
D((t-1)t^j)=-t_{j+1}=-L(t^j).
$$



The integral column basis1,(t-1),t(t-1),... has determinant1. Evaluation
at1 removes its first column. The remaining n columns are therefore
moment columns with row polynomials -1 and t^(k-n-1)(t-1). This verifies
the universal2S(n) bound even though both endpoint rows were initially
non-moment functionals.

For the complementary high set k=n+1,...,2n-1, those row polynomials
form a unimodular basis of all degrees through n-1. Hence the minor is
the ordinary moment Gram determinant up to sign and has valuation
exactly2S(n). The empty set at n=1 is also correct: the remaining
one-by-one determinant is -L(1)=-1.

## 4. Every exponential-row assignment

Each high exponential row is evaluation at the integer node k in the
falling-factorial basis, divided by k!. The Vandermonde lower bound
S(r) follows from the integer binomial-evaluation determinant and is
attained at consecutive nodes.

The border functional Lambda is integral on all integer polynomials:
it takes value1 on each falling factorial and the monomial-to-falling
basis change is integral. Its alternant with r evaluation rows is their
Vandermonde times Lambda of the monic polynomial having those roots.

The actual A functional satisfies



$$
E_{n-j}=\sum_{k=0}^n(k)_j/k!.
$$



Indeed the terms below j vanish and the remainder is the exponential
partial sum after shifting k by j. Its nodes are at most n and are
distinct from every high node n+1,...,3n. Its extra denominator has
valuation at most phi(n).

With H_r equal to the factorial-valuation sum of the largest r high
nodes and V*=3S(n)-n-H_n, the four assignments give:

| Endpoint rows in the exponential block | Exponential lower bound | Arctangent lower bound | Gap above V* |
|---|---:|---:|---:|
| Neither | S(n+1)-H_(n+1) | 2S(n) | 0 |
| A only | S(n+1)-H_n-phi(n) | 2S(n) | n |
| Border only | 2+S(n)-H_n | 2S(n) | n+2 |
| Both | 2+S(n)-H_(n-1)-phi(n) | 2S(n+1) | 2+2phi(2n) |

I checked the last gap explicitly: H_n-H_(n-1)=phi(2n+1), and
phi(2n)=phi(2n+1)=n+phi(n). Thus it equals2+2phi(2n)>0, including n=1.
The rho expansion introduces no equal high/low nodes. If some functional
minor vanishes, that term has infinite valuation and still satisfies the
lower bound.

## 5. Unique least term and restored valuation

In the first assignment, selecting high nodes2n,...,3n gives an
exponential Vandermonde on n+1 consecutive integers. The complementary
C minor is precisely the Gram minor from Section3. The term therefore
attains V*.

The maximizing high-node set is unique despite the plateaus of phi.
Any alternative must replace at least one chosen node by a node at most
2n-1. Every chosen node has valuation at least phi(2n), while
phi(2n)>phi(2n-1). Thus its factorial valuation sum drops by at least1.
Neither of its remaining factors can fall below the global bounds.
The other three assignments already have strict positive gaps.

There is consequently a unique nonzero term with least valuation. The
dyadic valuation of the whole determinant equals V*, rather than merely
being bounded below by it. Restoring the factorial row scales cancels
the range2n+1,...,3n and yields the claimed exact Delta_A formula.

## 6. Primitive normalization and the closed formula

The canonical cofactor identity is



$$
A(1)/B(1)=\Delta_A/(n!\Delta_B).
$$



For a rational ratio its reduced denominator therefore has valuation



$$
v_2(q_n)=\max(0,\phi(n)+v_2(\Delta_B)-v_2(\Delta_A)).
$$



The Delta_B formula used in the new note agrees exactly with Theorem2.1
of the canonical arithmetic source. Its bordered-Cauchy quantity
H(r+1) is g(r)+r+1_(r odd), so there is no parity or indexing mismatch
when that quantity is renamed beta in the new proof. The older full-rank
and Delta_B determinant theorem remains an explicit previously verified
dependency; the new Delta_A proof does not assume its finite numerical
pattern.

Substitution leaves n+L_n-2S(n). The identities
S(2r)=2g(r), S(2r+1)=2g(r)+r+phi(r), and
g(r+1)-g(r)=r+phi(r) give, in both parities,



$$
L_n-2S(n)=r+\mathbf1_{r\text{ odd}}
 =2\lfloor(n+2)/4\rfloor,
$$



where n=2r or2r+1 respectively. The result is positive for n>=1, so the
maximum introduces no further case or hidden cancellation.

## 7. Distinctness, nonvanishing, and limitations

The valuation increases by either1 or3 from n to n+1. Equal rational
numbers have equal reduced denominators, so the endpoint approximants
r_n=-A_n(1)/B_n(1) are pairwise distinct. Their equality with an arbitrary
fixed real target can occur at most once. Because B_n(1) is nonzero,
the evaluated remainder vanishes exactly at such an equality.

This argument does not assume irrationality of the target or of e+pi.
It proves eventual nonvanishing without an Archimedean sign assertion.
It also leaves open a single possible exceptional zero. Along any
unbounded shrinking subsequence, discarding that possible index is
legitimate; a rational target would force every remaining nonzero
integer form to have absolute value at least its fixed denominator's
reciprocal.

The lower bound q_n>=2^(3n/2+O(1)) is an actual primitive-height fact.
It does not bound the odd-prime factors, provide an upper height bound
suitable for irrationality, or estimate the entire evaluated remainder.
Those limitations are correctly retained in the source.

## 8. Fresh exact controls

`check_raw_arctan_dyadic_independent.py` uses direct actual coefficient
matrices, rather than rerunning the author's checker. At n=3,5,7 it
computes both augmented integer determinants, independently solves the
high equations with B(1)=1, reconstructs A(1) from its low Taylor
coefficients, and compares the actual reduced denominator. All agree.

It also checks every one of the70 Laplace assignments at n=3. The unique
least term has high nodes6,7,8,9 and valuation-18. The four observed case
minima are -18,-13,-13,-8, all consistent with the proved bounds. This
finite verification checks normalization and indexing; it is not used
to infer the all-degree theorem. Results are saved in
`raw_arctan_dyadic_independent_checks.json`.
