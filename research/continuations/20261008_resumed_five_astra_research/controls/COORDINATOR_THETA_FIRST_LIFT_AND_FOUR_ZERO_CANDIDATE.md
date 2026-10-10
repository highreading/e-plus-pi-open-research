> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual theta first-lift formulas and a four-zero terminal candidate

Coordinator derivation, 9 October2026. NEW parent application; DIFFERENT
proof audit PENDING. Exact source formulas below are derived from the
complete integer normalization DIFFERENT-passed in FULL A4turn24. The
stronger terminal consequence also uses finite source-jet aggregation and
global competitor payments whose new versions await DIFFERENT audit.
It gives a further lower divisor, not a noncancellation upper or e+pi proof.

Scoped Desktop/current MD/TEX searches before the calculation find the
explicit modulo4 first-lift obligation in FULL A2turn15, not its evaluation.
The complete archived D2621_WEIGHTED_REGULAR_DYADIC_SUBFAMILY.md is read:
its normalized quadratic Gamma moments and parity-disk difference theorem
belong to another construction. Their filtration result is REUSE and is
not substituted for the present theta jets. Primary
[Sun--Wu--Zhuang](https://arxiv.org/abs/1009.2929), abstract read, concerns
Bell/derangement polynomial congruences; no unread body theorem is imported.
The preceding exact-source primary searches find no matching actual formula.
This is a scoped reuse filter, not an exhaustive novelty claim. Elementary
finite differences, binomial/Stirling identities and valuations are reuse.

## 1. Exact retained source and definitions

Keep ORIGINAL k=9^(18+32u), d=k-1, v2(d)=4, n=d+2, physical terminal3d+1.
Let theta_0=1, theta_1=0 and

    theta_(r+1)=(2r+1)theta_r+theta_(r-1), r>=1.

These are the actual normalized differences of u_m=a_(2m). Write

    theta_r^(m)=Delta^r u_m/(2^r r!),
    B_j(r)=binom(r+j,r) theta_(r+j),
    K_b(z,r)=sum_(t=0)^b binom(b,t) B_(z+t)(r).

K here is an INTEGER finite filter, not merely its parity; it is not the
unrelated forcing matrix K_d. Every index below is nonnegative. The exact
Pascal filter identity is K_(b+1)(z)=K_b(z)+K_b(z+1).

The DIFFERENT-passed physical-base formula in A4turn24(9.4) gives

    theta_r^(m)=theta_r+2m(r+1)theta_(r+1) mod4.       (1)

Indeed terms j>=2 in that complete finite sum have 2^j and vanish modulo4.
No division is made after reducing an unnormalized finite difference.

Put R_j=(d+1)_j and o_d=d!/2^v2(d!). The exact source normalization is

    T_j^(a)(r)=Delta^j mathsf_v_a^(r)/(2^j R_j),

with the complete integer formula A4turn24(9.7). The w-atom jets are

    A_j^(a)=Delta^j mathsf_a_w(a)/2^j.

## 2. Evaluated top-source law modulo4

In that exact formula, the h-th summand contains binom(d,h) and
Q_h(a)=prod_(t=h)^(d-1)(2a+2t+1). For1<=h<=d,

    h binom(d,h)=d binom(d-1,h-1)

proves v2 binom(d,h)>=4-v2(h). Thus a summand visible modulo4 has h
divisible by8 (h=0 included). The complete product satisfies

    Q_h(a)=(-1)^(h*a+binom(h,2))=1 mod4

for these h, since d is divisible by16. Also a+h has parity a and d-h
is even. Substituting(1) and using

    (r+j+t+1)binom(r+j+t,r)
         =(j+t+1)binom(r+j+t+1,r)

gives the uniform actual top formula

    T_j^(a)(r)=o_d {K_d(j,r)+2a(j+1)K_d(j+1,r)} mod4. (2)

Every factor R_j and the full return divisor 2^r r! was divided while
integral, BEFORE this reduction. Formula(2) applies on the original finite
top ranges a+j<=d-1 and r<=d. Its recurrence indices stay within3d+1.

In the exact w-jet formula A4turn24(9.8), every term h>=1 contains the
integer falling product d!/(d-h)!, hence the factor d in16Z. The h=0
product is Q_0(a)=1 mod4. Therefore

    A_j^(a)=(-1)^(a+j) mod4.                         (3)

This supplies the actual atom first digit too. Rising ratios R_m/R_j must
still multiply(3) in a normalized determinant; they are not replaced by1.

## 3. Evaluated bottom mixed-source law modulo4

Let I be ANY actual p-element pole set in0..d-1, p>=2, and set

    Q_I(i)=prod_(t in I)(2(d+i+t)+1),
    S_I=sum_(t in I)(d+t) mod2,
    J_l=Delta^l Q_I(0)/(2^l l!).

Expand Q_I in ordinary powers of i and use integer Stirling numbers.
Only degrees l and l+1 survive in J_l modulo4. If e_m denotes the
elementary symmetric polynomial in its p odd constant factors, then

    J_l=e_(p-l)+2binom(l+1,2)e_(p-l-1) mod4,
    e_(p-l)=binom(p,l)+2S_I binom(p-1,l) mod4.

Thus the COMPLETE normalized coefficient is

    J_l=binom(p,l)+2S_I binom(p-1,l)
                    +2binom(l+1,2)binom(p,l+1) mod4. (4)

At l=p the last binomial is0; out-of-range terms are omitted. The exact
shifted product rule gives, for j>=p,

    Delta_i^j(Q_I(i)theta_r^(d+i))|0/(2^j j!)
       =sum_(l=0)^p J_l binom(r+j-l,r)theta_(r+j-l)^(d+l).

Here the base shift d+l is essential. Use(1), the preceding binomial
identity and l binom(p,l)=p binom(p-1,l-1). Since p(p-1) is even, its
physical-base correction reduces to 2p*j*K_(p-1)(j-p+1,r). Also

    binom(l+1,2)binom(p,l+1)
          =binom(p,2)binom(p-2,l-1).

Putting z=j-p, we obtain the actual bottom law

    V_z^I=K_p(z)+2(S_I+p*j)K_(p-1)(z+1)
                      +2binom(p,2)K_(p-2)(z+1) mod4. (5)

For the minimal pole set T_p={d-p,...,d-1}, S_I=binom(p+1,2) mod2.
The exact Pascal filter simplifies(5) to

    V_z^(T_p)=K_p(z)+2p*z*K_(p-1)(z+1)
                         +2binom(p,2)K_(p-2)(z+2) mod4. (6)

For general I put beta_I=S_I+p+binom(p,2) mod2. Then(5) is equivalently
(6) plus 2beta_I K_(p-1)(z+1). This retains all actual pole dependence
needed at the first lift, rather than importing a parity-only kernel.

## 4. Both first lifted relations remain in the bottom span

Let D=d-p>=2, so the complete normalized bottom rows have orders
z=0,...,D+1. Normalize each top row by the actual odd unit o_d; retain
this unit in the external determinant prefactor. It does not alter depth.

The exact integer identity K_d(j)=(1+E)^D K_p(j), where E shifts z, is
available before reduction. Subtract from top row j the bottom combination
sum_(t=0)^D binom(D,t)V_(j+t)^I, for j=0,1. Both combinations use only
the actual bottom rows. These two rows are even, as already proved.

Their contact coordinates after dividing by2 have the evaluated parity

    L_j=a(j+1)K_d(j+1)
          -(p*j+beta_I)K_(d-1)(j+1)
          -(p*D+binom(p,2))K_(d-2)(j+2) mod2.        (7)

To verify(7), sum the z-dependent correction in(6) using
sum t binom(D,t)E^t=D E(1+E)^(D-1). Every division uses the complete
modulo4 row, not merely its leading residue.

Crucially, BOTH vectors in(7) are in the existing bottom span:

* for j=0, (1+E)^D K_p(1) uses orders1..D+1;
* for j=1, a(j+1)=2a is0 modulo2, removing the only orderD+2 term;
* K_(d-1)(j+1)=(1+E)^(D-1)K_p(j+1) uses at mostD+1;
* K_(d-2)(j+2)=(1+E)^(D-2)K_p(j+2) also uses at mostD+1.

The bottom atom column is0. For a source-jet pattern containing0,1 whose
maximum jet order m>=4, its top atom entries are (R_m/R_j)A_j^(a)/o_d.
Because v2(R_4)>=3 and R_0,R_1 are odd, both entries remain even after
the first division by2. Thus(7) is a relation of the COMPLETE rows,
including their atom coordinate.

Subtract these certified binary bottom combinations from the two first
divided rows. Both become even once more. Equivalently, subtract twice
those combinations before the first division: each of the two original
rows is now divisible by4. These are operations on an already normalized
auxiliary matrix; no unpaid division in the original integer pencil is
asserted. Its complete determinant therefore has a factor16.

## 5. Candidate complete-sector consequence and its dependencies

The finite source-jet expansion in A4turn24 Section15 has the exact bill

    F(U)=2^sum(j_a) prod_(a=0)^(p-2)R_(j_a),
    v2(F(U)/F_p)>=sum(j_a-a).

For p>=5, EVERY jet pattern of excess<=3 contains0 and1: deleting0
costs at leastp>=5; deleting1 while retaining0 costs at leastp-1>=4.
Its maximum order is at leastp-1>=4. Section4 therefore supplies factor16
for every such normalized aggregate, for ANY pole set I and physical
source Newton base. Every other jet pattern already pays at least4.
Both actual forcing/source index sets, their adjugate minors and all odd
factors remain; their integer diagonal payment can only increase depth.

Consequently the pure-Cauchy atom-product p-sector should satisfy

    complete sector in 2^(L_p+4) Z_2, p>=5, d-p>=2. (8)

This uses the full source-jet aggregation, not one chosen source minor.
That NEW aggregation from A4turn24 is assigned to DIFFERENT A2turn16;
the present stronger use also requires DIFFERENT review.

For7<=p<=d/3, atom-bottom patterns pay v2((d+1)_(p-1))>=4, and factorial
patterns have margin alpha-4p-3m_d-12>4 at original sizes. Hence (8)
would extend to the COMPLETE p-sector in this strip.

Write m_d_star=min_(1<=p<=d)L_p for the nominal minimum; m_d above still
denotes the binary bit-length, not this minimum.

FULL A2turn15's NEW global comparison pays all factorial patterns by
m_d_star+4; it awaits DIFFERENT review. Nominal convexity localizes EVERY
count within three digits of the minimum to p=d/4+O(log d), inside the
above strip with p>=7. Other pure-Cauchy/atom counts already pay the
target. With these full global payments verified, the consequence is

    2^(m_d_star+4) divides det[w_*,v^(0),...,v^(d)]. (9)

Both known first zeros would be followed by TWO further zeros. Formula(9)
is a NEW proof candidate with explicit pending dependencies. It is not
labelled DIFFERENT-passed and does not supply any valuation UPPER bound.

## 6. Precision, verification, and next question

Equations(1)--(7) need the normalized full source entries modulo4 before
either /2. All source divisions 2^r r!, 2^j R_j and 2^j j! are already
integer-paid; top o_d is an actual odd unit. The physical indices remain
at most3d+1. Both borders of the paired coefficient system remain literal;
the constant border -f+4rho has not been evaluated by this theta argument.

A NEW bounded auxiliary receipt is now COMPLETE and CLOSED:
[THETA_FIRST_LIFT_RAW_AUXILIARY_RECEIPT.json](THETA_FIRST_LIFT_RAW_AUXILIARY_RECEIPT.json).
Raw INTEGER finite differences at fixed d=16,48,80 verify20,653 top
entries,317 atom entries,108,174 bottom entries and11,304 complete-row
second-even coordinates in90 configurations. Minimal and shifted actual
pole sets, physical source bases0/d-p and both admitted jet patterns are
retained. ALL checks PASS in30.783 seconds under the no-network/no-key
math sandbox. These are auxiliary parameters, not original-index tests or
an infinite proof. No old closed computation is rerun; this new receipt
must not be repeated in a subsequent request.

The next actual question is the second lift modulo8 of these two rows and
the complete remaining source-jet classes, or a different noncancellation
upper lemma. Repeated extra zero digits alone do not settle the required
joint terminal upper, other-prime arithmetic, actual all-prime G/clearer,
same-index positive primitive whole error, or rationality of e+pi.
