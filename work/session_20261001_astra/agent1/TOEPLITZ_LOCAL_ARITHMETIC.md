> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Balanced Toeplitz local arithmetic

Author derivation, 2026-10-01. The conclusions below are deductive and conditional where explicitly stated. No numerical checks, prime scans, or independent review are claimed. Earlier research is retained without recalculation.

## Definitions and initial interior window

Let Q0(z)=1-z+z^2/2, F(0)=0, F'(z)=2/Q0(z). Assume 1<=b<=n, and index the square Toeplitz matrix by 0<=i,j<b:

 T_ij=[z^(n+i-j)] exp(z)Q0(z)^n.

Put m_i=n+i. The two forcing columns are

 fP_i=[z^m_i] Q0^n D^n(1/(1-z)),
 fQ_i=[z^m_i] Q0^n D^n((exp(z)+F(z))/(1-z)).

Split fQ=fE+fL, retaining its exponential and logarithmic parts separately.

Fix an odd prime p>2b+3 and additionally require p>=3b. Write n=ap+r, and restrict initially to

 b<=r<=floor((p-b)/2).

This window is nonempty under the two stated prime restrictions. The additional restriction p>=3b is necessary for this particular interval; p>2b+3 alone does not ensure nonemptiness. It ensures r+i<p, r+i-j>=0, and 2r+i<p for every matrix index. Thus the low coefficient windows below do not cross a multiple of p. Higher-index recurrence arguments still require their own boundary treatment; these inequalities alone do not authorize any division modulo p.

## Integral row normalization

Write q_s=[z^s]Q0^n, with q_s=0 outside 0<=s<=2n. Since (2Q0)^n has integer coefficients, 2^n q_s is an integer.

Normalize row i by the positive integer c_i=2^n m_i!. For a nonnegative integer m, use (m)_s=m!/(m-s)! for 0<=s<=m, and zero outside that range.

The normalized Toeplitz entry is exactly

 M_ij=c_i T_ij
     =2^n sum_(s=0)^(m_i-j) q_s (m_i)_(s+j).

Every summand is integral. This proves integrality before any modular use of the proposed row normalization.

More generally let g(z)=sum_(l>=0) a_l z^l/l!, where every a_l is integral. Direct differentiation and convolution give

 c_i [z^m_i]Q0^n D^n g
   =2^n sum_(s=0)^m_i q_s (m_i)_s a_(n+m_i-s).       (1)

All factorial quotients here are literal nonnegative integer falling factorials. Formula (1) proves integral forcing columns once the sequences a_l are identified.

For gP=1/(1-z), aP_l=l!.

For gE=exp(z)/(1-z), define E_l=l! sum_(h=0)^l 1/h!. Then E_0=1 and

 E_l=l E_(l-1)+1, l>=1.

For gL=F(z)/(1-z), put d_l=F^(l)(0) and L_l=l! sum_(h=0)^l d_h/h!. Here

 d_0=0, d_1=2,
 d_(l+1)=l d_l-binomial(l,2)d_(l-1), l>=1,
 L_0=0, L_l=l L_(l-1)+d_l, l>=1.

The d recurrence follows by comparing exponential-generating coefficients in Q0 F'=2. Consequently d_l, E_l, and L_l are integers. Equation (1) therefore proves integrality of all three normalized forcing pieces. The total forcing uses a_l=E_l+L_l, with no discarded logarithmic term.

## The positive forcing has a separate exact factorial factor

Since D^n(1/(1-z))=n!/(1-z)^(n+1), its normalized column satisfies

 P_i=c_i fP_i=n! m_i! H_i,
 H_i=2^n [z^m_i]Q0^n/(1-z)^(n+1) in Z.             (2)

This exact factor is stronger and structurally different from the integrality assertion for the other forcing columns. In particular, once n>=p, the raw positive column is zero modulo p. A modulo-p transfer of P alone then carries no information about its residual coefficient H_i.

No corresponding n!m_i! factor is asserted for E or L. Their separate recurrence sequences in (1) must be analyzed before a common factor is removed from fQ. A factor of the positive column cannot be canceled from a different column without a proof.

## All-index reduction of the matrix and exponential forcing

All following congruences are in Z_(p), or its residue field. Put n=ap+r, with a>=0 and the interior range stated above. Write M(n), E(n), L(n), P(n) for the row-normalized matrix and separate forcing columns. A parenthesized r means the same construction at n=r, with the same b.

For any nonnegative m with residue t, (m)_k is zero modulo p when k>t, and is (t)_k modulo p when 0<=k<=t. This includes k>m through the zero convention. Thus every surviving summand for row i has s+j<=r+i for M, and s<=r+i for a forcing column. In particular s<p. Frobenius gives

 Q0(z)^n = Q0(z^p)^a Q0(z)^r mod p,
 q_s(n)=q_s(r) mod p for 0<=s<p.

Since 2^n=2^(a+r) mod p, the matrix transfer is

 M(n)=2^a M(r) mod p.                              (3)

For E_l the recurrence E_l=l E_(l-1)+1 restarts at EVERY multiple of p: E_(kp)=1. Induction within the block proves E_(kp+t)=E_t for 0<=t<p, including k=0. No inverse of l is used.

For surviving forcing terms, l=n+m_i-s=2ap+2r+i-s, where 0<=2r+i-s<p by the interior inequalities. Hence

 E(n)=2^a E(r) mod p                               (4)

for every a>=0. These are genuine all-index transfers, not finite seed observations. Exponential series themselves are never reduced coefficientwise modulo p; only the integral factorial-normalized expressions are reduced.

## Logarithmic boundary and its factorial depth

Work temporarily in Z_(p)[i]; this is an unramified quadratic algebra, possibly split. Both alpha=1+i and beta=1-i are units, since their norm is 2. Formal expansion of F gives, for l>=1,

 d_l=-(2/i)(l-1)!(alpha^(-l)-beta^(-l)).             (5)

This also supplies an independent all-index description of the integer recurrence above. At l=p, Wilson and Frobenius give

 d_p=-2 chi mod p,  chi=(-1)^((p-1)/2).

Indeed alpha^p=1+chi i, beta^p=1-chi i. For l>=p+1 the factorial in (5) proves d_l=0 mod p. Consequently the cumulative logarithmic sequence satisfies

 L_(p+t)=-2 chi t! mod p, 0<=t<p;
 L_(kp+t)=0 mod p, k>=2, 0<=t<p.                  (6)

The exceptional block beginning at p must not be discarded. Formula (6) follows from L_l=l L_(l-1)+d_l, using its restart at each multiple of p; it involves no modular division.

In our interior window, if a>=1, all surviving terms in (1) have l=2ap+2r+i-s>=2p. Terms excluded by their falling factorial remain zero since L_l is integral. Therefore

 L(n)=0 mod p, n>=p.                               (7)

At a=0 the seed logarithmic column L(r) must instead be retained. In particular Z(n):=E(n)+L(n) transfers to 2^a E(r), NOT generally to 2^a Z(r), when a>=1.

A stronger depth bound keeps the potentially important logarithmic correction visible. Put N=2n+b-1 and h=floor(log_p N). Equation (5) gives

 L_l=-(2/i)l! sum_(v=1)^l (alpha^(-v)-beta^(-v))/v,
 v_p(L_l)>=v_p(l!)-floor(log_p l), l>=1.

For a term with u=m_i-s>=0 and l=n+u, equation (1) therefore gives valuation at least

 v_p(m_i!)-v_p(u!)+v_p((n+u)!)-h
 >=v_p(m_i!)+v_p(n!)-h.

The last step uses integrality of binomial(n+u,n); 2^n q_s is integral and introduces no negative odd-prime valuation. Summing yields

 v_p(L_i(n))>=v_p(n!)+v_p(m_i!)-h.                 (8)

In particular it is at least 2v_p(n!)-h, as well as at least zero by integrality. This is a valuation bound, not an asserted exact common factorial factor. It explains when the logarithmic part reappears at the precision needed for a cancellation argument. The exponential part has no analogous bound asserted here.

## Residual positive forcing: the second transfer

The raw positive column vanishes modulo p for n>=p. Remove its exact factorial factor OVER Q before reduction. Set

 u_i(n)=(n+i)!/n!=product_(v=1)^i(n+v), u_0=1,
 V_i(n)=u_i(n) H_i(n).

Then all entries are integers and

 P(n)=(n!)^2 V(n).                                 (9)

Under the interior window u_i(n) is a p-unit and reduces to u_i(r). Removing (n!)^2 is a uniform column operation; removing the different m_i! separately would change the equations unless their remaining row multipliers were retained. Formula (9) retains them.

Define the dyadic rational diagonal coefficient

 h_a=[w^a] Q0(w)^a/(1-w)^(a+1)
     =sum_(k=0)^floor(a/2) a!/[k! k! (a-2k)! 2^k].  (10)

The displayed sum follows by writing Q0(w)/(1-w)=1+w^2/(2(1-w)). Thus h_a belongs to Z[1/2] and is always p-integral, but need not be a p-unit.

Here is a coefficient-level Frobenius proof valid for arbitrary a, not merely a<p. In F_p[[z]],

 Q0(z)^n/(1-z)^(n+1)
 = [Q0(z^p)/(1-z^p)]^a N_r(z)/(1-z^p),
 N_r(z)=Q0(z)^r(1-z)^(p-r-1).

The exponent p-r-1 is nonnegative, and deg N_r=p+r-1. Write the target degree as m_i=ap+t, t=r+i<p. Among degrees congruent to t modulo p, the numerator N_r can contribute only t: the next candidate p+t is at least p+r, outside its degree bound. Negative degrees contribute zero. Its coefficient at t equals

 [z^t]Q0(z)^r/(1-z)^(r+1),

because t<p. Taking the coefficient at m_i therefore proves

 H_i(n)=2^a h_a H_i(r) mod p,
 V(n)=2^a h_a V(r) mod p.                           (11)

The high block a survives as the scalar h_a. Replacing it by 1 or assuming it is a unit would be incorrect. Formula (10) is an exact expression for this scalar at every index; no prime scan is involved.

Combining the two actual forcings, for a>=1 we have the local input

 M(n)=2^a M(r),
 V(n)=2^a h_a V(r),
 Z(n)=2^a E(r) mod p,
 P(n)=(n!)^2 V(n) exactly.                         (12)

Thus the two columns have different factorial scales and different residual transfer laws.

## Concrete conditional valuation gates

These gates concern the actual normalized Toeplitz forcing equations. They do not select a center and do not replace the final endpoint gcd. Assume det M(n) is nonzero over Q when discussing its unique rational solutions, and write d=v_p(det M(n))>=0. No assumption that d=0 is made.

First consider the residual positive equation M(n)x_V=V(n). For column j let C_j(n) be the determinant obtained from M(n) by replacing column j by V(n), with its position unchanged. From (12) and determinant multilinearity,

 C_j(n)=2^(ab) h_a C_j(r) mod p.                   (13)

If h_a C_j(r) is nonzero modulo p for at least one j, that C_j(n) is a unit. Cramer's rule then proves

 min_j v_p((x_V)_j)=-d,
 min_j v_p((x_P)_j)=2v_p(n!)-d,                    (14)

where M(n)x_P=P(n). All other Cramer numerators are integral, so they cannot give a smaller valuation. Formula (14) is a concrete valuation gate for a normalized forcing obstruction and the corresponding positive forcing response. It remains valid when d>0; it explicitly retains the unremoved factorial depth in the raw response.

For the full second forcing M(n)x_Z=Z(n), let B_j(r) be the column-replacement determinant of M(r) with E(r), not with Z(r). Then, for a>=1,

 det M(n)[j<-Z(n)]=2^(ab) B_j(r) mod p.            (15)

If some B_j(r) is nonzero, then

 min_j v_p((x_Z)_j)=-d.                            (16)

These gates give finite-characteristic tests that transfer to every admissible n, and exact response valuations conditional on their nonzero residual tests. They do not claim that those tests always succeed. When det M(r)=0 but a replacement determinant is nonzero, d>=1, so (16) proves an actual pole in the normalized second-forcing solution. This is stronger than merely listing residues.

There is also a direct compatibility formulation that does not require any determinant unit. If a row lambda over F_p satisfies

 lambda M(r)=0, lambda E(r)!=0,

then for n>=p no p-integral vector x can solve

 M(n)x=P(n)X+Z(n)Y

with X p-integral and Y a p-unit. Reduce the equation and use (12): the positive contribution vanishes, whereas the second contribution does not. This is an obstruction on an actual forcing equation, not yet an assertion about the reduced denominator of a coordinate-selected center.

For the stripped two-column problem one must instead keep lambda h_a V(r) and lambda E(r) separately. Their possible cancellation depends on the prescribed coefficients and is not controlled by the one-column gates.

## Exact stopping and lifting problem

A transfer using raw P(n) modulo p is vacuous for n>=p. Equation (9) removes precisely that common factorial zero before the test. The scalar h_a may still vanish, and residual replacement minors may vanish even when h_a does not. In either case (13) supplies no unit numerator: this branch stops at first order.

Likewise, if all B_j(r) vanish, (15) alone does not determine the second-forcing pole. Rank deficiency of M(r) by two or more forces every one-column replacement determinant to vanish and is a structural reason this can happen. No division by det M(r) is permitted in this situation.

The exact higher-precision problem is to determine the first nonzero p-adic coefficients of

 det M(n),
 C_j(n)=det M(n)[j<-V(n)],
 D_j(n)=det M(n)[j<-E(n)+L(n)].

If d=v_p(det M(n)), response integrality is equivalent to all relevant replacement determinants having valuation at least d. For the raw positive response the thresholds shift by exactly 2v_p(n!), by (9). For a combined forcing, the actual numerator is

 (n!)^2 X C_j(n)+Y D_j(n),

and its cancellation must be determined at the required depth. Testing the summands separately cannot settle equal-depth cancellation.

There is an exact recurrence-based lift with specified arithmetic: compute q_s(n) in Z[1/2] from the polynomial power, and use the finite sums (1) and the falling-factorial formula for M modulo p^k. Generate E_l, d_l, and L_l by their integer recurrences through l=2n+b-1. Compute V through its exact coefficient formula (2) and u_i(n); never obtain V by modular inversion of (n!)^2. All dyadic divisions are legal for odd p. Falling-factorial terms omitted in the mod-p proof must be restored for the lift unless their valuations are separately shown to be at least k. Formula (8) permits omission of the logarithmic column only below its proved valuation bound. No smaller universal precision or favorable lift has been proved.

These finite exact procedures define the unresolved leading coefficients without claiming a new computation was performed. The present work provides their first-order all-index structure and conditional nonvacuous gates. It does not establish a uniform unit minor, a prime contribution to a selected center denominator, shrinking, or irrationality.

A row clearer is not a reduced endpoint denominator. Coordinate-center selection and general endpoint gcd formulas remain Child 4's task. The local transfer input to that task is (9), (12), the depth bound (8), and the response/compatibility gates (14)-(16).
