> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete actual theta source formulas modulo8

Coordinator derivation, 9 October2026. NEW parent source-level extension;
DIFFERENT audit PENDING. This is not an evaluation of the second effective
row lift, an upper-excess bound, or a decision of e+pi.

The scoped Desktop/current search for actual theta modulo8 and second
source lifts recovers the explicit current OPEN obligation. Archived
item209's scope concerns moving odd-prime rank-one Cartier cells, and the
earlier theta^P modulo8 formulas concern a different signed producer. They
are not the present normalized theta columns. FULL A2turn14's passed
dyadic trace recurrence is REUSE; it already evaluates the leading unit
blocks, so no new tensor-rank calculation is proposed. Primary exact-source
searches find no matching formula. Existing Bell/derangement and finite-field
Hankel abstracts are applicability filters only; no unread theorem is used.
Elementary finite product, Stirling and binomial identities are reuse.

## 1. Same retained objects and complete division

Use the EXACT theta, B_j(r), INTEGER filter K_b(z,r), R_j=(d+1)_j,
o_d, normalized top T_j^(a), atom A_j^(a) and actual pole polynomial Q_I
from COORDINATOR_THETA_FIRST_LIFT_AND_FOUR_ZERO_CANDIDATE.md. Keep ORIGINAL
v2(d)=4, full return/top/bottom divisors and physical terminal3d+1.
All reductions below concern already normalized integral entries.

The actual physical-base expansion satisfies the stronger formula

    theta_r^(m)=theta_r+2m(r+1)theta_(r+1) mod8.       (1)

For every term of index l>=2, its factor2^l(r+1)_l is divisible by8:
at l=2 the product(r+1)(r+2) is even, and at l>=3 the explicit2^l
already suffices. Thus the full finite source expansion proves(1).

## 2. The top and atom laws extend unchanged to modulo8

The bound v2 binom(d,h)>=4-v2(h) now implies that every h visible
modulo8 is divisible by4. Its complete Q_h(a) has d-h factors, a multiple
of4 consecutive odd integers. Each group of four has product1 modulo8,
so Q_h(a)=1 mod8. Also a+h=a mod4 and d-h=0 mod4.

The same exact shifted-binomial identity as in the first-lift note proves

    T_j^(a)(r)=o_d {K_d(j,r)+2a(j+1)K_d(j+1,r)} mod8. (2)

The w-atom h>=1 terms contain d in16Z. The complete h=0 product is1
modulo8, giving

    A_j^(a)=(-1)^(a+j) mod8.                         (3)

These retain the actual odd o_d and the rising atom ratios. The physical
source ranges a+j<=d-1 and r<=d are unchanged.

## 3. Complete mixed pole coefficient at the next precision

For ANY p-element I, p>=5, set x_t=d+t and

    X1=sum_(t in I)x_t, X2=sum_(s<t in I)x_s x_t,
    C_b=binom(p,b), j=p+z.

X1 is needed modulo4 and X2 modulo2; pole dependence is retained.
The elementary symmetric coefficient in the p odd factors1+2x_t is

    e_(p-l)=binom(p,l)+2X1 binom(p-1,l)
                               +4X2 binom(p-2,l) mod8.

The normalized finite-difference coefficient

    J_l=Delta^l Q_I(0)/(2^l l!)

receives ordinary powers of degree l,l+1,l+2 at this precision. Use

    S(l+1,l)=binom(l+1,2),
    S(l+2,l)=binom(l+2,3)+3binom(l+2,4).

After paying the integer binomial identities, the complete coefficient is

    J_l=binom(p,l)+2X1 binom(p-1,l)+4X2 binom(p-2,l)
         +2C_2 binom(p-2,l-1)
         +4{X1 binom(p-1,2)+C_3}binom(p-3,l-1)
         +4C_4 binom(p-4,l-2) mod8.                  (4)

Out-of-range binomial coefficients are0. The last coefficient uses
12=4 modulo8. Formula(4) includes both the first ordinary coefficient
correction and the second finite-difference carry.

## 4. A closed complete bottom formula

The shifted product rule and(1) give the full bottom entry as

    sum_l J_l {B_(j-l)+2l(j-l+1)B_(j-l+1)} mod8.

The first summand converts(4) directly to integer filters. In the physical
base correction J_l is required modulo4. The three contributions are

    2p*j*K_(p-1)(z+1)-2p(p-1)K_(p-2)(z+1),
    4X1(p-1)j K_(p-2)(z+2),
    4C_2*j {K_(p-2)(z+2)+(p-2)K_(p-3)(z+2)}.

For the second expression the omitted term has the even product
(p-1)(p-2). For the third use k(k+1)=0 mod2 after setting k=l-1.
Therefore the actual complete mixed entry is

    V_z^I=K_p(z)+2(X1+p*j)K_(p-1)(z+1)
               -2C_2 K_(p-2)(z+1)
       +4{X2+j[X1(p-1)+C_2]}K_(p-2)(z+2)
       +4{X1 binom(p-1,2)+C_3+j C_2(p-2)}K_(p-3)(z+2)
       +4C_4 K_(p-4)(z+2) mod8.                    (5)

This is an evaluated source formula, not an unnamed return coefficient.
It has no original-size input table or solve. Reducing(5) modulo4 agrees
with the already derived and finite-checked first-lift formula: -2C_2
and2C_2 are equal at that precision. Equality modulo8 is the NEW claim.

For I=T_p, use the ACTUAL identities

    X1=2dp-binom(p+1,2),
    X2=binom(ceil(p/2),2) mod2.

The second counts pairs of odd elements in that actual last-p interval.
No residue of a general pole set is substituted for this minimal set.

## 5. Exact remaining obligation and scope

Equations(2)--(5) now provide the full source entries modulo8 needed
BEFORE two successive row divisions. They do not evaluate the resulting
effective determinant or certify its unit minor. In particular the
first-lift parity combinations may acquire new carries when lifted as
integer combinations; their full coefficients and physical source base
must be kept. A presumed repetition of the modulo4 zero is insufficient.

The DIFFERENT audit of the complete source-jet aggregation, global
factorial/atom exclusions and four-zero candidate remains pending. Any
next whole coefficient digit must include ALL eligible product counts,
source-jet/index patterns, atom positions, odd prefactors and BOTH borders.
The constant coefficient retains -f+4rho. All-prime G/least clearer,
same-index primitive positive whole error and e+pi rationality remain OPEN.

No bounded check is indispensable to the algebra above, and none has yet
been run for modulo8. The CLOSED modulo4 raw receipt is not rerun or
silently promoted to modulo8 evidence. A new diagnostic, if needed, must
target only the genuinely new pre-division residues at this precision.
