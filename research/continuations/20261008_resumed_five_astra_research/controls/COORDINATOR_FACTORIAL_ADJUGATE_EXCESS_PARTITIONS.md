> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact factorial-adjugate excess partitions and complete first-two inventories

Coordinator derivation, 9 October2026. NEW parent application; DIFFERENT
proof audit is pending. This localizes the TWO index sets in the actual
linear terminal expansion. It evaluates no complete coefficient residue.

Before this derivation, scoped Desktop/current MD/TEX search for near-minimal
factorial-adjugate index partitions recovers the unique minimum and the
explicit open all-competitor obligation in FULL A2turn14, but no complete
weighted-partition inventory in that scope. Primary exact-phrase arXiv
search finds no matching result. Standard Ferrers partitions and their
generating functions are established reuse, as in
[DLMF26.9](https://dlmf.nist.gov/26.9); no classical partition identity is
claimed new. The terminal-specific factorial weight, all finite boundaries
and its use in the actual excess bookkeeping are derived below. This is a
scoped overlap filter, not exhaustive literature novelty.

## 1. Retained actual diagonal and original indices

Keep ORIGINAL k=9^(18+32u), d=k-1, physical terminal3d+1, and BOTH exact
paired coefficient identities of FULL A2turn14. The actual factorial block
inverse uses

    N_d=(h_d D_f^-1) adj(K_d) (h_d D_f^-1),
    h_d=(2d-2)!, D_f=diag((2j)!)_(0<=j<d).

K_d is the actual finite integer unit block. Its complementary adjugate
minors remain actual integers and can contribute further divisibility;
their signs and odd residues are not replaced by1. Put

    alpha=v_2((2d)!)=2d-s_2(d), beta=alpha-5,
    e_j=beta-v_2((2j)!)=alpha-5-2j+s_2(j).

The original v_2(d)=4 gives beta=v_2((2d-2)!). Thus e_(d-1)=0, and ALL e_j
are nonnegative. For1<=t<=d-1, the exact finite increment is

    e_(t-1)-e_t = v_2((2t)(2t-1)) = 1+v_2(t).       (1)

For1<=p<=d, the unique diagonal-weight minimizer is

    T_p={d-p,...,d-1}, E_p=sum_(t in T_p)e_t.

Every p-minor of N_d with row set I and column set J has at least the
diagonal payment E(I)+E(J), with E(I)=sum_(i in I)e_i. A possibly zero or
even adj(K_d) minor can only increase it. This does not assert attainment.

## 2. Exact partition bijection and weighted loss

Order I={i_0<...<i_(p-1)} within the LITERAL range0..d-1. Write

    t_a=d-p+a, lambda_a=t_a-i_a, 0<=a<p.

Then

    d-p >= lambda_0 >= ... >= lambda_(p-1) >=0.       (2)

Indeed i_a>=a and i_(a+1)>=i_a+1 give the bounds and monotonicity.
Conversely every partition in the p by(d-p) rectangle gives exactly one
valid I by i_a=t_a-lambda_a. No coordinate below0 or beyond d-1 is added.

The exact EXTRA diagonal payment is

    W_(d,p)(lambda)=E(I)-E_p
       =sum_(a=0)^(p-1) sum_(t=t_a-lambda_a+1)^(t_a)(1+v_2(t))
       =2|lambda|+sum_a(s_2(t_a-lambda_a)-s_2(t_a)).   (3)

An empty inner sum is0. Every nonempty summand has t>=1, so v_2(0) is
never used, including the case p=d where the rectangle is empty.
Equation(3) follows by telescoping(1) and is exact, not asymptotic.

In particular

    W_(d,p)(lambda)>=|lambda|,
    W_(d,p)(lambda)=0 iff lambda is empty.           (4)

Use a SECOND independent partition mu for J. Then the complete extra
diagonal cost is W(lambda)+W(mu), not just one of them.

## 3. All competitors within a proved excess budget

For a pure-Cauchy, product-atom sector whose other payments are at least
the exact nominal L_p, EVERY term that can reach L_*+B must satisfy

    W(lambda)+W(mu)<=B-(L_p-L_*).                    (5)

This applies after the separate ALL-pattern correction exclusions have
been proved at that precision. In the proposed first B=floor(d/8) window,
the parent all-pattern locality note asserts precisely that pure-Cauchy,
product-atom restriction; it still awaits DIFFERENT audit. This note does
not extend(5) to a factorial-correction sector by ignoring its different
E_p+E_(p-v) bill. Nor does it discard atom-bottom terms without paying
their full rising divisor.

For an integer remaining budget b>=0, (4)--(5) give

    |lambda|+|mu|<=b.

Hence lambda_a=0 for every a>=min(p,b), and likewise for mu: a partition
with more than b positive parts has area>b. ALL suffix positions

    i_a=j_a=d-p+a, min(p,b)<=a<p

are therefore unchanged. Every changed coordinate is>=max(0,d-p-b).
Only a bounded low-edge portion of T_p can move; the upper suffix is not
silently replaced by a newly appended physical interval.

At a fixed product count the actual retained pairs form the explicit set

    {(lambda,mu) in two p by(d-p) rectangles:
          W_(d,p)(lambda)+W_(d,p)(mu)<=b}.           (6)

Each must carry its actual adjugate minor, source/Cauchy residue, sign and
relative odd factors. The inventory is necessary, not sufficient, for a
complete coefficient calculation. Extra valuation in any such factor
remains a further filter, not an assumed unit.

## 4. A dimension-independent bound on the inventory size

For b>=1 the number in(6) is at most exp(5 sqrt(b)). Here is an elementary
proof, without importing a partition asymptotic. Discard the two rectangle
restrictions and weights, retaining only total area<=b. For0<z<1, the
generating series of two unrestricted partitions is

    P(z)^2=prod_(r>=1)(1-z^r)^-2.

Every retained pair contributes z^area>=z^b. Thus its count is at most
z^-b P(z)^2. Set z=exp(-1/sqrt(b)). Expanding the logarithm gives

    log P(z)^2
      =2 sum_(j>=1) 1/(j*(exp(j/sqrt(b))-1))
      <=2 sqrt(b) sum_(j>=1)1/j^2 <=4 sqrt(b).

The last inequality follows from1+integral_1^infinity x^-2 dx=2.
Adding log z^-b=sqrt(b) proves the stated bound. At b=0 the only pair is
the two empty partitions. This is a finite inventory bound, not an
original-size algorithm request or an upper valuation theorem.

Combined with terminal count convexity, at excess B the full nominal
product-count/diagonal-index inventory has at most

    (2T_B+1) exp(5 sqrt(B)),
    T_B=(1+sqrt(1+2B))/2,                           (7)

before retaining ALL other scalar/source digits. Formula(7) can be enormous
for linear B and is not called a practical enumeration at original d.

## 5. COMPLETE first-two diagonal-index inventories

Suppose1<=p<d, put t=d-p, and define

    T_p^- = {d-p-1,d-p+1,...,d-1}.

It corresponds to lambda=(1,0,...,0) and has exact loss

    w=1+v_2(t).                                    (8)

Any other nonempty partition has at least two boxes. By monotonicity it
contains either(2) or(1,1). If t is odd, their losses are respectively

    (1+v_2(t))+(1+v_2(t-1))>=3,
    (1+v_2(t))+(1+v_2(t+1))>=3,

when the corresponding rectangle permits that shape. A forbidden shape
is simply absent. If t is even with v_2(t)=1, these two losses are also
at least3. If v_2(t)>=2, even the single box costs>=3.

Consequently ALL pairs of loss<=2 are exactly:

| Original case | Pair | Exact diagonal loss |
|---|---|---:|
| Any p | (T_p,T_p) |0|
| p odd, hence t odd |(T_p^-,T_p) or(T_p,T_p^-)|1|
| p odd |(T_p^-,T_p^-)|2|
| p even and v_2(d-p)=1 |(T_p^-,T_p) or(T_p,T_p^-)|2|

For p even with v_2(d-p)>=2 there is no nonminimal pair at loss<=2.
The case p=d has only the full set with loss0. These statements rely on
original d even; no parity-distribution hypothesis is introduced.

This table classifies the ADJUGATE DIAGONAL weights only. At complete
excess1 or2, one must ALSO include higher digits of the minimal pair,
actual adjacent nominal product counts with L_p-L_* within the budget,
their own table entries, and every odd relative prefactor. The table does
not prove that any listed nonminimal term is nonzero. It does not omit
a coefficient digit merely because its index pair has loss0.

## 6. Next mathematical use and remaining scope

The useful next evaluation is the full exact terminal aggregate through
one or two excess layers, now with a complete diagonal-index inventory,
or a compressed formula for the wider weighted partitions. In particular
the shifted I-only, J-only and BOTH-shifted terms are separate and their
possible cancellation must be computed. The previous first THETA layer
zero remains established at its own audit scope.

No numerical execution is required for(1)--(8). No old source table,
original-sized matrix, prime scan or closed auxiliary receipt is rerun.
The new application awaits DIFFERENT proof audit. The exact constant
border, scalar transfer, all-prime G and least clearer, primitive q,
complete same-index nonzero error and e+pi rationality remain OPEN.
