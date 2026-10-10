> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# All-index large-prime saturation of the shared augmented high core

Date: 2026-09-13. Original root derivation. Independent audit requested.

The shared-core content zeta_n introduced in
`raw_adjacent_high_content_condensation.md` has no prime divisor
greater than 3n. This closes that particular content-support target
at every index. It does not prove the corresponding assertion for
the full high-matrix content D_n or its reduced content eta_n.

More precisely, let C_n^+ have the actual integer high rows
k=n+2,...,3n and columns B_0,...,B_(n+1),C_0,...,C_(n+1), with
entries (k)_j and k! tau_(k-j), respectively. For n>=1,

    rank_(F_p) C_n^+ = 2n-1, for every prime p>3n.       (1)

Consequently the positive gcd zeta_n of its maximal minors satisfies

    v_p(zeta_n)=0 for every p>3n.                       (2)

The proof retains the actual exponential/arctangent Taylor jets.
No row or degree constraint is omitted, and no degree or prime scan
is involved.

## 1. An elementary polynomial-module degree lemma

Work over any field K. For fixed polynomials E,F and an integer
M>=1, define the K[z]-module

    A_M={(A,B,C): A+BE+CF is divisible by z^M}.

It has the explicit polynomial row basis

    (z^M,0,0), (-E,1,0), (-F,0,1).                    (3)

Indeed every member equals ((A+BE+CF)/z^M) times the first
row plus B times the second and C times the third. The coefficient
is a polynomial by definition. The determinant of (3) is z^M.

This basis can be transformed by invertible polynomial row
operations to a basis T_1,T_2,T_3 with independent leading row
vectors. Here the degree of a nonzero vector polynomial is the
maximum of its component degrees, and its leading row vector is
its coefficient at that degree.

For completeness, if the three leading vectors are dependent,
choose a nontrivial constant linear relation among them and choose
a row T_i of maximal degree d_i among the rows occurring in that
relation. Subtract appropriate scalar multiples of
z^(d_i-d_j)T_j for the other participating rows. The leading term
of T_i cancels and its degree strictly decreases. This is an
elementary invertible row operation; T_i cannot become zero since
the rows remain a module basis. The sum of the three nonnegative
row degrees decreases, so the process terminates. At termination
the leading vectors are independent. Permute rows to arrange

    d_1<=d_2<=d_3.

The determinant has nonzero leading coefficient equal to the
determinant of those leading row vectors. Elementary operations
preserve the determinant up to a nonzero constant. Hence

    d_1+d_2+d_3=M.                                    (4)

There is also an exact predictable-degree identity: for polynomials
f_i, not all zero,

    deg(sum_i f_i T_i)=max_i(deg f_i+d_i).              (5)

At the maximal candidate degree, the leading term is a nontrivial
linear combination of a subset of the independent leading row
vectors, with the nonzero leading coefficients of the relevant
f_i. It cannot vanish. This proves (5) and, by counting the allowed
coefficients of the f_i, the dimension formula

    dim_K {T in A_M: deg T<=D}
       =sum_(i=1)^3 max(0,D-d_i+1).                   (6)

Thus no unproved normality theorem or field-specific polynomial
reduction algorithm is required for the degree argument below.

## 2. Apply the already verified minimal-degree bound

Now fix n>=1 and p>3n, and take K=F_p, M=3n+1. Let E,F be the
actual Taylor polynomials of exp(z), arctan(z) through degree 3n,
reduced modulo p. Every denominator used is a unit because its
index is at most 3n<p. The module A_M depends only on these jets.

The verified theorem in `raw_large_prime_nullity_and_smith.md`
gives exactly

    dim_K {T in A_M: deg T<=n-1} <= 1.                (7)

Its proof used the nonzero cleared Wronskian and the injective
leading B coefficient on that degree slice. The bounded-degree
slice here is the same space: for degree at most n-1 it is a
subspace of the degree-n high kernel, with the uniquely recovered
A polynomial. No assumption about a particular endpoint-selected
canonical triple is needed.

If d_1<=n-2, the independent vectors T_1,zT_1 both have degree
at most n-1, contradicting (7). If d_2<=n-1, the independent
vectors T_1,T_2 likewise contradict (7). Therefore

    d_1>=n-1,  d_2>=n,  d_3<=n+2,                   (8)

where the last inequality follows from (4). The only possible
sorted degree profiles are

    (n,n,n+1), (n-1,n+1,n+1), (n-1,n,n+2).           (9)

To see the exhaustiveness, if d_1>=n then (4) forces d_1=d_2=n.
If d_1=n-1, the ordered remaining pair has sum 2n+2 and its
smaller member is n or n+1. These are precisely the other two
profiles. This is a classification of the possible degrees, not
an assertion that every profile occurs in the actual family.

Since each d_i<=n+2, (6) now gives the exact dimension

    dim_K {T in A_M: deg T<=n+1}
       =3(n+2)-(3n+1)=5.                             (10)

The equality remains valid when d_3=n+2: its contribution is
zero in both expressions.

## 3. The exact bridge to the shared integer matrix

Choose arbitrary polynomials B,C of degrees at most n+1. The
equations of A+BE+CF=0 through degree n+1 determine a unique
polynomial A of degree at most n+1: its coefficients are the
negatives of those of BE+CF in that range. The remaining
equations through degree 3n are exactly

    [z^k](BE+CF)=0, k=n+2,...,3n.                    (11)

Multiplying row k by k!, a unit modulo p, gives exactly C_n^+.
All its Taylor subscripts k-j are positive. Consequently its
kernel is in linear bijection with the space in (10), and it
has dimension five. There are 2n+4 columns, so its rank is
2n+4-5=2n-1, the number of rows. This proves (1).

Full rank modulo p means at least one maximal minor is a unit
at p. Thus its maximal-minor gcd has valuation zero, proving
(2) with all prime-power multiplicities excluded at once.
The characteristic-zero full row rank needed to define the
positive gcd also follows from any one of these finite-field
full-rank statements, or from the previously known high rank.

The n=1 case is included: C_1^+ has one row and six columns,
and (10) gives its kernel dimension five. No empty or negative
degree needs to be inserted into the module basis argument.

## 4. Consequences for the adjacent condensation

For p>3n+3, choose any unit (2n-2)-minor of the old shared core
as in `raw_adjacent_high_content_condensation.md`. Write rho
for the one remaining shared row and E_(rho,c) for its six
integer bordered entries, four in old columns and two in new
columns. The exact Schur-content identity there gives

    min_(all six c) v_p(E_(rho,c))=v_p(zeta_n)=0.       (12)

If the old shared core has rank only 2n-2 modulo p, all four
old-column entries are divisible by p. Equation (12) therefore
forces at least one of the two new-column entries to be a unit.
Adding the two new columns always restores full shared-row rank.
This is stronger than treating restoration as merely possible.

It follows that the next high matrix H_(n+1) can always be
condensed using a unit full shared-row pivot of size 2n-1,
leaving a 3-by-5 carrier for its last three rows. That pivot
may require a new column, so it does not automatically serve
as a pivot of the old matrix H_n.

The already proved integer relation zeta_n | gcd(D_n,D_(n+1))
has only primes at most 3n in its lower divisor. This does not
imply that the gcd on the right has no larger prime factors;
divisibility is in that direction only. Nor does the unit
single new-column pivot imply a unit 2-by-2 new-column pivot.
The lost low row and the Schur correction terms in the two
exterior vectors still require separate control.

## 5. An eventual-degree consequence and the remaining arithmetic problem

For the same fixed jets of order M=3n+1, (8) and (6) imply

    dim_K {T in A_M: deg T<=D}=3(D+1)-M, D>=n+1.      (13)

For n+1<=D<=3n this says that the actual remaining coefficient
matrix with rows k=D+1,...,3n and B,C degrees at most D has
full row rank. At D=3n the row set is empty, consistently.
This is a statement at fixed jet order; it must not be applied
as though the order stayed fixed when n is incremented in H_n.

At degree n, the three profiles (9) give respectively dimensions
2,2,3. Thus the only defective high-rank profile is
(n-1,n,n+2), exactly consistent with the previous description
span{T,zT,S}. The new theorem does not exclude that profile or
bound its lifting exponent over Z_p.

The remaining arithmetic targets are therefore the full high
content D_n (equivalently eta_n at p>3n), the separate endpoint
restriction content, and the size of the primitive endpoint
carrier. The shared augmented core is now saturated at all
large primes; it should no longer be listed as an unresolved
large-prime support obstruction.
