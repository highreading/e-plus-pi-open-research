> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A rising-factor contact-jet divisor and a finite dyadic kernel

Parent derivation, 9 October2026. This continues the exact weighted
contact source in FULL A2turn12. Its prerequisite full turn11 theorem
independently PASSES A4turn19; turn12 and the earlier parent F4 filter
independently PASS the completed full A4turn20 audit. The new statements
below await a different proof review.
They do not upper-bound the growing complete coefficient pair.

Scoped current/previous/Desktop English MD/TEX searches for the exact
rising contact-jet divisor recover turn12's low-order binom(d+j,j)
parity and an unrelated older Jacobi rising product in A4turn0.
No evaluated current all-order divisor/kernel statement is recovered.
Classical finite-difference product rules, Lucas, finite-field trace,
Kronecker products and generating-function algebra are reuse. The
previous primary Lucas/Rowland/Bacher gates give their stated scopes;
no generic inverse theorem is imported. Han2607.08279 was ALREADY
read in the October2 arithmetic/selector work. Its one-sided dilation
differs from these complete mixed corrected columns. The recovered
earlier full-reading gate is reused; the paper is not assigned again.

Keep the original k=9^(18+32u), d=k-1, v2(d)=4 and d=2mod3.
Let t_n^(r) be the actual top weighted Newton source, with its full
D_r=2^r r! division. The exact turn12 product-rule identity implies

    Delta^j t_n^(r) / [2^j(d+1)_j]
      = odd(d!) sum_(h=0)^d binom(d,h) Q_h(n)
          binom(d-h+r+j,r) eta_(d-h+r+j)^(n+h).          (1)

This holds for every permitted r,j, without r+j<16. To verify it,
multiply turn12(4.3) by (r+1)_j/(d+1)_j and use the EXACT identity

    (r+1)_j/(d+1)_j * binom(d+j,h)
      *binom(d-h+r+j,r+j)
       =binom(d,h)*binom(d-h+r+j,r).

Every summand in (1) is an integer. Thus the full rising integer
2^j(d+1)_j divides the actual source jet. No merely binary division
is substituted, and the annihilator is never commuted with Delta.
Its binary depth is 2j+s2(d)-s2(d+j). Compared with the old2^j j!
payment, the additional depth is v2 binom(d+j,j), the carry count.
The cumulative extra depth is O(q log d), not a new quadratic saving.

Define the additionally normalized parity

    U_(j,r)=Delta^j t_n^(r)/[2^j(d+1)_j] mod2.

The physical top row n disappears at THIS parity precision. Setting
t=d-h in (1), all odd Q_h and odd(d!) reduce to1, and

    U_(j,r)=sum_(t=0)^d binom(d,t)
                binom(t+j+r,r) eta_(t+j+r) mod2.       (2)

This is distinct from the earlier J parity; its divisor is different.
Over F4 with omega^2+omega+1=0 and Tr(x)=x+x^2, eta_m is
Tr(omega^(m+2)[1+(m+1)omega]). Since d is even, only even t contribute.
Putting s=j+r gives the complete coefficient law

    U_(j,r)=Tr(omega^(s+2)[1+(s+1)omega]
          [z^r](1+z)^s[1+omega(1+z)]^d).              (3)

The earlier two-carry rule evaluates this single coefficient with
fixed registers and logarithmic digit complexity. This is still an
entry algorithm, not a determinant algorithm.

There is now also a joint row/column generating kernel. Put S=X+Y.
The elementary identity

    sum_(j,r>=0) binom(t+j+r,r) X^j Y^r
       = (1-Y)^(-t)/(1-X-Y)

and (2) give

    sum U_(j,r) X^jY^r
      =Tr(omega^2 * B(Y) * (omega^2+omega S)
                          /(1+omega S)^2),            (4)
    B(Y)=[(omega^2+omega Y)/(1+omega Y)]^d.

The Euler derivative in j+r is retained in this calculation.
Differentiating B contributes zero in characteristic2 because d is
even. Multiplying (4) by the unit series C(Y)=(1+Y+Y^2)^d yields,
on the exact original d=2mod3,

    C(Y) sum U_(j,r) X^jY^r
       =Tr((1+omega^2 Y)^(2d)
                     *(omega^2+omega S)/(1+omega S)^2). (5)

At the level of this NORMALIZED PARITY matrix over F2, multiplication
by C(Y) is a unit triangular COLUMN transformation:
each first-q-column block depends only on its own previous columns.
It preserves every leading q-by-q determinant. This pays a literal
finite block operation, not a projected infinite inverse. This does
not claim a unimodular operation on the entire original integer pencil,
whose contact-column and row divisors must still be accounted for.

Because v2(2d)=5, the first nonconstant numerator term in (5) has
Y-degree32. Hence for q<=32 the transformed leading matrix is

    E_(j,r)=binom(j+r,r) epsilon_(j+r),
    epsilon=(1,1,1,0,0,1) with period6.                 (6)

The leading E blocks of sizes2,8,32 are units. Here is a symbolic
proof, not a finite scan. For q=2m, reorder rows and columns by parity:

    E_(2m) = [[C_m,A_m],[A_m,0]],
    A_(h,l)=binom(h+l,l) theta_(h+l),
    theta=(1,0,1) with period3.

Its determinant is det(A_m)^2 in characteristic2. For m=2^a let
P_m=(binom(h+l,l)) and D_omega=diag(omega^h). Lucas gives P_m as
the a-fold tensor of [[1,1],[1,0]]. Put B_omega=D_omega P_m D_omega.
Then A_m=omega^2 B_omega+omega B_(omega^2). A literal2-by-2 check
on each digit shows

    B_omega^(-1)B_(omega^2)
       =omega^(m-1) J_a,
    J_a=[[1,0],[1,1]] tensor ... tensor [[1,0],[1,1]],
    J_a^2=I.

For even a, m=1mod3 and I+omega^(m+1)J_a=I+omega^2 J_a is a unit,
since its square is the nonzero scalar1+omega times I. Therefore
A_m is a unit for m=1,4,16, proving the stated q=2,8,32 cases.
No assertion for q>32 is made: the actual d-dependent numerator
then becomes visible. Formula (5) identifies its precise deformation.

One consequence is an attaining33-column TOP-SOURCE minor using
the atom-contact source and weighted returns r=0,...,31. The uniform
source-minor lower divisor from Newton expansion is

    b'_q=binom(q,2)+sum_(j=0)^(q-2) v2((d+j)!/d!).

For q=33, original k=81^(9+16u)=17mod64 gives d=16mod64. For j<=31,
v2((d+j)!/d!)=v2(j!)+1_(j>=16), so b'_33=528+416+16=960.
Use the consecutive top rows d-33,...,d-1 and their determinant-one
forward-difference transform. The atom jet has exact depthj and odd
normalized value. The contact row factor v2((d+j)!/d!) is nondecreasing,
and it increases by4 at j=32. Consequently the unique minimum in the
atom-column expansion puts the atom in row32. Its contact cofactor is
the unit U leading32 block proved above. The full top-source minor
therefore has depth EXACTLY960 on every original index.

This crosses the old low-order source-unit limitation for a stated
block, but is still FIXED rank. A complete corrected cofactor would
also require the exact factorial-adjugate weights, complete Cauchy
factor, original bottom corrections and both affine borders. Those
are not evaluated here. A growing flag must handle the d-dependent
numerator in (5), then the first visible bottom corrections. Fixed
rank33 does not imply the target nu<=15k^2/4, any OTHER odd-prime
bound, primitive whole-error decay, producer retirement or e+pi proof.

No new arithmetic computation was run for this note. The general
identities and unit proofs are algebraic; a different review is pending.
