> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Two explicit next-moment coefficient proposals for critical four-fifths

These are coordinator derivations to audit, not assumed established results.
Use alpha=sqrt2/(1+sqrt2), Q=Q2, X=sum theta, C3=sum theta^3,
v1=t*g(t)/M and v3=t^3*g(t)/M in the exact circular loop identity.
The retained expansions are g/M=1-alpha*t^2/2+alpha*t^4/24+O(t^6)
and cot(delta/2)=2/delta-delta/6-delta^3/360+O(delta^5).
Endpoint and collision fluxes still require the safe-field proof.

For the v3 identity, keeping degree-four pair corrections gives

alpha*n*(E Q4-E Q6/6)
=2d*E Q+E X^2
-(alpha+1/6)*d*E Q4
+(1/6-alpha)*E(X*C3)-alpha/2*E Q^2
+O(n*E Q8+d*E Q6+E Q4).

The pair quartic identities used here are
sum_(i<j)(x-y)^2*(x^2+xy+y^2)=d*Q4-X*C3,
and
sum_(i<j)(x^4+x^3*y+x^2*y^2+x*y^3+y^4)
=(d-5/2)*Q4+X*C3+Q^2/2.
The derivative -5alpha*Q4/2 cancels the finite-degree part of the latter.
Using already proved E Q6=5d^4/(alpha^3*n^3)+controlled error,
E Q4=2d^3/(alpha^2*n^2)+lower error, E Q^2=d^4/(alpha^2*n^2)+
O(d^5/n^3+d^2/n^2), and E Q's first correction gives the candidate

E Q4=2d^3/(alpha^2*n^2)
+[(5/6-(9/2)*alpha)/alpha^3]*d^4/n^3
+O(d^2/n^2+d^5/n^4).

For v1, keeping the circular quartic pair terms and derivative cancellations:

alpha*n*(E Q-E Q4/6+E Q6/120)
=d^2-(alpha+1/6)*d*E Q+(1/6-alpha/2)*E X^2
+(alpha/6-1/360)*d*E Q4
+(alpha/24-1/120)*E Q^2+(1/90)*E(X*C3)
+O(n*E Q8+d*E Q6+E Q).

The quartic circular sum uses
sum_(i<j)(x-y)^4=d*Q4-4X*C3+3Q^2.
Substitution of the candidate Q4 coefficient gives

E Q=d^2/(alpha*n)
+[(1/6-alpha)/alpha^2]*d^3/n^2
+[(alpha^2-3alpha/8+1/18)/alpha^3]*d^4/n^3
+O(d^2/n^2+d^5/n^4).

Audit every coefficient, the bounded full-interval remainders, the explicit
h_q potential corrections, and the centered product estimates. In particular,
the h_q contributions may be absorbed into O(d^2/n^2), but must be bounded
before doing so. At critical d~n^(4/5) the stated remainders become negligible
after multiplication by d/n. Actual complex-weight corrections remain
centered: Q costsO(d/n),Q4 costsO(d^2/n^2),Q6 costsO(d^3/n^3).

If both coefficients pass, expand the first logarithmic derivative through
signed degree7 with Q8 remainder; a safe t^11 field gives Q12 and controls
signed C7 by variance and phase. Required first-derivative remainder is
O(d/n+d^5/n^4). The second derivative through degree4 needs the candidate
Q correction and leading Q4; its covariance isO(d/n), not a positive
complex variance. Third/fourth precisions are already in A3turn21.
Compare the resulting actual fifth stationary coefficient with the exact
archived equilibrium identity. No full critical relative theorem is asserted
in this note until all these actual errors and original scalar interfaces
are checked.
