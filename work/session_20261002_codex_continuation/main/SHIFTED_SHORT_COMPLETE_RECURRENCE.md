> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# M26. Shifted short paired determinants: exact scalar compression

Author all-degree algebraic theorem and eight new exact instances. The complementary complete analytic target is assigned to the analysis agent in SHIFTED_SHORT_RECTANGULAR_GATE.md. This note does not prove an actual primitive-denominator rate or irrationality of e+pi.

## Fresh target gate

Fresh archive searches for shifted short rectangular determinants and factorial-degree compression found the current scope notes, not a completed theorem for this family. M23's common-orthogonal-polynomial shifted family and the selector's scalar compression are explicitly credited. M26 uses the smaller right degree2k-1 from M24 and its full stacked determinant, which is a different approximation family.

Fresh primary searches covered shifted derangement Hankel moments, mixed moment block determinants and recurrence compression. Miska, *Arithmetic properties of the sequence of derangements*, arXiv:1508.01987, Section4.3 equations(17)--(18), was read; its scalar recurrence is classical and not claimed new. The generic integer relation and minimum-denominator context in Labahn–Storjohann's May2026 primary manuscript was also read. Generic ordinary derangement Hankel determinant evaluations do not identify this mixed even-moment stack or its final e+pi coefficient gcd.

## Three complete scalar states

Fix even M>=0, k>=1, X=2M, and define

    d=D_X, f=X!,
    l=4 sum_(a=1)^M (-1)^(M-a)/(2a-1).

The symbol l is the arctangent remainder only; it is not the full rational endpoint constant, which equals -f+l at the base index.

Set

    P_j(X)=product_(a=1)^j (X+a),
    Q_0=0, Q_(j+1)=(X+j+1)Q_j+(-1)^(j+1),
    h_r(X)=4 sum_(a=0)^(r-1) (-1)^(r-1-a)/(X+2a+1).

Empty sums are zero. Exact iteration gives

    D_(X+j)=P_j d+Q_j,
    (X+j)!=P_j f,
    R_(M+r)=-P_(2r)f+(-1)^r l+h_r.          (1)

Let P,Q,H,V denote k by2k matrices with entries P_(2(i+j)), Q_(2(i+j)), h_(i+j), (-1)^(i+j). The complete shifted matching and rational matrices are

    C=dP+Q-V,
    R=-fP+H+lV.

The physical lower moment block of y^M[exp(sqrt y)+4/(1+y)]dy/(2sqrt y), after eliminating the e-response using C, is exactly R+S V. This retains both endpoint contributions.

Define the full coefficient pair without the old mass by

    det[C; -fP+H+T V]=A0(X,d,f)+T B0(X,d,f). (2)

The actual full pair is therefore

    beta0=A0+lB0, beta1=B0.                  (3)

All formulas remain polynomial identities even at singular matrices; no inverse is assumed.

## Strong all-degree scalar-degree reduction

Over Q(X), the variable part of the stacked matrix in(2) factors as

    [ d I_k ; -f I_k ] P,

and has rank at most k. Any determinant term containing more than k variable rows vanishes. Equivalently use the rank-k determinant expansion, which does not require its constant part to be invertible. Consequently

    total_(d,f)degree A0 <= k,
    total_(d,f)degree B0 <= k,
    degree_f B0 <= k-1.                     (4)

The final inequality holds because differentiating in T consumes one of the k lower rows. The naive product of2k degree-one entries has degree2k; matching removes every homogeneous degree above k in the COMPLETE output pair. This is a structural cancellation, not a finite numerical conjecture.

A second useful exact fraction-free row identity is

    d(-fP+H)+fC = dH+fQ-fV.

Thus multiplying every lower row by d and adding f times the corresponding upper row preserves the full determinant up to d^k, including its complete response coefficient. This identity alone is not a favorable gcd claim.

## Old mass denominator once and the actual final gcd

The fixed tail denominator is cleared by

    delta(X)=product_(a=0)^(3k-3)(X+2a+1),

with degree3k-2. Let A=delta^k A0 and B=delta^k B0. These are integer polynomials in X,d,f. Write l=p/a in lowest terms with a>0. Whenever B!=0, the complete primitive center and denominator are exactly

    c=-(aA+pB)/(aB),
    q_actual=abs(aB)/gcd(aA+pB,aB).          (5)

The old arctangent mass enters only through the single factor a. Clearing it in each lower row would have unnecessarily inserted a^k; (3) removes a^(k-1) before the final gcd. The remaining specialized gcd in(5) is retained without an unsupported estimate.

The exact complete primitive residual is

    abs(q_actual(S-c))
      =abs(aB S+aA+pB)/gcd(aA+pB,aB).

No separate exponential or arctangent error is used in place of this full residual.

## Uniform raw upper cost

The scalar recurrence polynomials and tail clearer have coefficient bounds giving, for X>=1,

    log q_actual
       <= k log(X!)+log a+O(k^2 log(X+k+1)). (6)

For example, bound the degrees-j recurrence entries by powers of X+6k, use the determinant expansion and(4), and use d<=f. The O term includes the fixed tail clearer and all determinant coefficients. This bound concerns the full specialized integer pair and is valid after the final gcd, since dividing can only reduce its denominator. It is not a lower bound and does not establish a favorable asymptotic q.

For M/k in a fixed positive range, (6) still allows an order-k^2 logk raw cost. The analytic continuation must be combined with the actual denominator in(5), rather than this coarse bound, to decide whether a nonzero integer form tends to zero.

## New exact receipts

The driver uses eight new short-family instances k1..4 and M8,32. It checks the scalar recurrence against independently built full endpoint matrices, the old-mass rank-one identity, the fraction-free complete row identity, two independent full-pair gcd reductions, and beta1!=0 in these instances.

The actual denominator bit lengths for M8 are70,162,299,463; for M32 they are390,755,1173,1640. These are different families from the earlier symmetric shifted receipts. Decimal full errors are diagnostics only.

Three exact symbolic fixed-X models k1..3 have total degrees(A0,B0)=(1,1),(2,2),(3,3), and factorial degrees of B0 respectively0,1,2, agreeing with the proved all-degree bound(4). The proof of(4) does not depend on these checks.

Files: SHIFTED_SHORT_RECURRENCE_CERTIFICATE.json and shifted_short_recurrence.py.

## Open arithmetic step

A theorem controlling the FULL specialized common content in(5) is still missing. No irrationality or rationality conclusion for e+pi is established by the construction or its scalar compression.
