> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Scalar center: gcd bounds and a ternary subsequence obstruction

New author deductions, 2026-10-01. The main SCALAR_FORCING_CENTER_DRAFT.md supplies the scalar construction, complete signed error, and 5-adic law as author inputs. The retained Acal transfer is used within its established odd-prime scalar scope. No prior calculation is replayed, and no independent review or numerical evidence is claimed.

Let n>=1, F_p=v_p(n!), P_n>0 be the actual integer Legendre endpoint, and

 N_n=(n!)^2 Qcal_n+2^n Acal_n,
 Z_n=(n!)^2 P_n,
 q_n=Z_n/gcd(Z_n,|N_n|).

Both complete numerator terms remain present. Valuations of zero are infinity.

## 1. Separate dyadic accounting

First Acal_n is integral, a stronger fact than merely dyadic integrality. In a coefficient a_s(n)=[z^s](1-z+z^2/2)^n, a monomial selecting k quadratic factors has denominator 2^k and s>=2k. Its multinomial coefficient is integral. The falling factorial (n)_s contains at least floor(s/2)>=k even factors. Thus every contribution to (n)_s a_s(n) is integral. Multiplication by the integers D_(2n-s) and summation proves Acal_n in Z.

Set h_2=floor(log_2 n). The supplied second-kind formula

 Qcal_n=8 sum_(j=1)^n P_(j-1)P_(n-j)/j

implies v_2(Qcal_n)>=3-h_2. Consequently the two terms separately satisfy

 v_2((n!)^2 Qcal_n)>=2F_2+3-h_2,
 v_2(2^n Acal_n)=n+v_2(Acal_n).

For every n>=4, both 2F_2>=n and 2F_2+3-h_2>=n. Indeed 2F_2>=2 floor(n/2)+2 floor(n/4)>=n-1+2 floor(n/4). If h_2>=2, then floor(n/4)>=2^(h_2-2), and 2^(h_2-1)+2>=h_2. These inequalities give both assertions. It follows that

 2^n divides gcd(Z_n,|N_n|), n>=4,
 q_n <= (n!)^2 P_n/2^n, n>=4.                     (1)

This is an all-size endpoint gcd bound, not just a coefficient clearer. It is too large to establish shrinking.

For more precise dyadic accounting let t_2=v_2(Acal_n), d_2=v_2(P_n). If

 n+t_2 < 2F_2+3-h_2,

then strict separation of the TWO terms proves

 v_2(N_n)=n+t_2,
 v_2(q_n)=max(0,2F_2+d_2-n-t_2).                  (2)

No uniform value of t_2 is asserted. If this strict inequality fails, the exact normalized quantity is

 R_(2,n)=Acal_n+((n!)^2/2^n)Qcal_n.

For n>=4 this is an integer by the bounds just proved. Exactly N_n=2^n R_(2,n), so, when R_(2,n)!=0,

 v_2(q_n)=max(0,2F_2+d_2-n-v_2(R_(2,n))).          (3)

If R_(2,n)=0 then N_n=0 and q_n=1. Formula (3) identifies the complete lifting problem; neither a vanishing Acal residue nor an equal-depth pair of terms justifies a unit argument.

## 2. Ternary residues and the actual endpoint

The three necessary scalar seeds can be derived directly, without a residue scan. D_0=1 and D_k=kD_(k-1)+1 give D_1=2,D_2=5,D_3=16,D_4=65. The defining finite formula yields

 Acal_0=1,
 Acal_1=D_2-D_1=3,
 Acal_2=D_4-4D_3+4D_2=21.

The retained all-index odd-prime transfer therefore gives

 Acal_n congruent to 1,0,0 modulo 3

according as n is 0,1,2 modulo 3. The two zero classes are not valuation theorems.

The supplied endpoint generating function G(z)=(1-4z-4z^2)^(-1/2) has the formal identity over F_3

 G(z)=(1-z-z^2)G(z^3).

For example this follows from G=H G^3 with H=1-4z-4z^2 and Frobenius G^3=G(z^3), using constant term one. Its digit coefficients are 1,2,2, all nonzero. Iteration over the base-3 digits proves

 v_3(P_n)=0 for every n>=0.                        (4)

This retains the actual endpoint; it is not replaced by a coefficient bound.

For h_3=floor(log_3 n), the complete second-kind term satisfies

 v_3(Qcal_n)>=-h_3.

For n>=3, F_3>=(3^h_3-1)/2>=h_3, and hence 2F_3-h_3>=1. If n is divisible by 3, the exponential numerator term is a 3-unit while the second-kind numerator term is divisible by 3. Thus

 v_3(N_n)=0,
 v_3(q_n)=2v_3(n!), n>=3, n congruent to 0 mod 3.  (5)

Equivalently the final endpoint gcd has zero ternary valuation in this class. This is an all-index consequence of transfer and strict separation, not a finite-data extrapolation.

## 3. Where the ternary unit argument stops

For n>=3 in either remaining residue class, Acal_n is divisible by 3. Define the complete p-integral quantity

 R_(3,n)=Acal_n+2^(-n)(n!)^2 Qcal_n.

Here 2^(-n) is a legitimate 3-adic unit. Both summands are 3-integral; both are divisible by 3 in these two classes. If R_(3,n)!=0, the exact denominator formula and (4) give

 v_3(q_n)=max(0,2F_3-v_3(R_(3,n))).                (6)

If t_3=v_3(Acal_n)<2F_3-h_3, strict separation proves v_3(R_(3,n))=t_3. When t_3 reaches or exceeds that bound, the first term alone no longer determines the result: the full R_(3,n) must be lifted. A zero residue of Acal supplies no upper bound on its valuation and no root-depth theorem. This unit route stops here for n congruent to 1 or 2 modulo 3.

## 4. Actual primitive forms cannot shrink on multiples of three

Retain, without recomputing its seeds, the main draft's author law

 v_5(q_n)=2v_5(n!), n>=5.

Together with (5), for every n>=6 divisible by 3,

 3^(2v_3(n!)) 5^(2v_5(n!)) divides q_n.            (7)

Legendre's formula, or the digit-sum formula for factorial valuations, now gives

 log q_n >= (log 3+(log 5)/2)n-O(log n).           (8)

To draw an exclusion we retain the supplied COMPLETE signed error, not just its logarithmic summand. Put M=1+sqrt(2), s=M^(-2), S=e+pi. The author inputs state

 c_n-S=eE/fP-(-1)^n epsilon_n,
 |eE/fP|<=27M/(sqrt(n)n!),
 epsilon_n>=2 exp(-s) M^(-2n).

The factorial bound is eventually at most epsilon_n/2. Therefore, at all sufficiently large indices,

 sign(c_n-S)=(-1)^(n+1),
 |c_n-S|>=exp(-s) M^(-2n).                        (9)

No effective threshold is claimed. These statements include the complete exponential correction, so the two signed errors have not been separated illegitimately.

The positive exponent margin is

 delta=log 3+(log 5)/2-2 log(1+sqrt(2))>0.

An exact verification of its sign is 3 sqrt(5)>(1+sqrt(2))^2=3+2sqrt(2): after squaring, this is 45>17+12sqrt(2), which follows from 7>3sqrt(2).

Equations (8)-(9) imply, along all n divisible by 3 tending to infinity,

 q_n |S-c_n| >= exp(delta n-O(log n)) -> infinity. (10)

Writing c_n=a_n/q_n in lowest terms with q_n>0, the actual primitive form is q_n S-a_n. It is eventually nonzero and has sign (-1)^n. Thus the specified subsequence is stopped as a route to nonzero primitive forms tending to zero. Multiplication by additional nonzero integers cannot restore shrinking on this subsequence.

This is an actual-form lower bound, not divergence of a positive upper certificate. It uses the new ternary law and the retained 5-adic law for this exact scalar construction. No identity with an older excluded family is assumed. It neither excludes all other index subsequences nor excludes new rational combinations of centers.

## 5. Status and remaining gap

New deductions are the dyadic endpoint gcd divisor (1), the conditional exact dyadic law (2), the complete dyadic lift (3), the ternary endpoint unit theorem (4), the exact ternary denominator law (5), and the primitive subsequence divergence (10). No numerical computation was needed for these proofs.

The scalar formulas, full error bounds, and 5-adic law retain their main-agent author status; this note does not independently audit or upgrade them. The completed TOEPLITZ_LOCAL_ARITHMETIC files and their exact prime/residue domains are unchanged. Their interior-window theorem is not extended to p=3 here: the ternary argument uses the separately retained scalar Acal transfer.

The remaining arithmetic for other indices is the valuation of R_(3,n) in the two zero classes and of R_(2,n) when strict separation fails, together with any further contributions to the final endpoint gcd. No useful exponential upper bound for q_n has been proved. No conclusion about the rationality or irrationality of e+pi follows.
