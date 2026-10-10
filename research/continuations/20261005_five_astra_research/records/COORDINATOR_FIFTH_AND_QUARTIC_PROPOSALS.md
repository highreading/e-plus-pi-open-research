> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Coordinator proposals requiring complete independent audit

## Fifth weighted carry: finite contractions and band support

Reuse the actual A4turn12/13/15/18/19 block formulas. Here e is the LAST
STANDARD VECTOR in radical coordinates, not the endpoint vector. The
endpoint is ((-1)^i). Set r1=(H-1)/2, r2=(H/3-1)/2, r*= (3H-1)/2.
Restrict further to 81|j, D<H/972. This still infinite subclass gives
ample integer margin for extended LOW tests through d+2. Prove any
nonempty small-index qualifications rather than ignoring them.

Let U be the leading D monomials, L_U its actual unit block, X_U the
corresponding coupling, Ehat=E-3X_U^T L_U^-1 X_U. Let E0 be the integral
top-pole anti-triangular matrix, R=E0^-1, F=(Ehat-E0)/3, and use the
EXACT decomposition V=Z^T X=-2e e_m^T+3K+9J, with J integral and
K_(i,b)=1_(i+b=r2). J includes all its higher digits; do not introduce
an independent unexplained fourth coupling array. The negligible
Z^TLU corrections must first be proved negligible at fifth precision.

A4turn19 proves extended direct annihilation modulo243. On D<H/972,
extend the same beta lemma through test monomials d+2, using shifts
at most 2D+1 (core adds one) and 4D+5<H/81 on every nonempty sufficiently
large domain. Monic division by (y-1)^D then gives lower Schur pairings
zero modulo243 for the first three HIGH coordinates d,d+1,d+2, and
V columns there zero modulo243. The top pole is absent in these
pairings. In particular F_dd in243Z3 and J e_d,J e_(d+1) in27Z3.

Expansion to mod81 gives, after killing the deep F_dd term,
V Ehat^-1 V^T = 9 A9 +27 A27 mod81, where

A9= K R K^T -2 Sym(e,J e_d) +2 Sym(e,K R F e_d)
     +4 (F R F)_dd e e^T,

A27= K R J^T+J R K^T +2 Sym(e,J R F e_d)-K R F R K^T
      -2 Sym(e,K R F R F e_d)-4(F R F R F)_dd e e^T.

Sym(e,v)=e v^T+v e^T. All terms are ACTUAL integral contractions.
Check this expansion independently, including signs and precision.
The fourth result proves A9 divisible by3; fifth T5 is
-(A9/3+A27) mod3. Naming A9 and A27 is not the intended endpoint:
evaluate every term using the following candidate support arguments.

1. Exact R_ab=[z^(d+m-a-b)](1-z)^(-A). For degrees less than H,
   modulo9 the inverse equals
   (1-z)^D*(1+3 z^(H/3)-3 z^(2H/3)).
   K R K^T selects degrees (H+3)/6+D+i+j, between D and H/3 on the
   small-D domain. Thus candidate K R K^T=0 mod9, not just mod3.

2. For w=F e_d the established mod3 support is at m-1,m. Choose an
   integral u supported at these edges with w=u+3v. Extend the division
   argument for y^d modulo243. Its lower Schur column is a combination
   of L_ext(y^a,y^i(y-1)^D), 0<=i<=nu; errors vanish modulo243.
   The FULL lower functional modulo9 suggests v mod3 has support only
   in the last two HIGH coordinates and b=r2-i, 0<=i<=nu. This follows
   by listing the (y-1)^H mod9 grid and ALL depth-h-2 poles; the unit
   pairs c,c+6 cancel at their required modulus. Verify this support
   from actual coefficients, not as an assumption. K R u=0 EXACTLY;
   K R v=0 mod3 by inverse degree gaps. Thus K R F e_d/3=0 mod3.
   R u lies at d,d+1. Since v_d,v_(d+1)=0 mod3 and R has zero entries
   among its last two coordinates, (F R F)_dd/3=0 mod3 as well.

3. Compute V modulo27 by multiplying the actual core with the complete
   (y-1)^H mod27 grid and including every depth-h-2/h-3 pole. Candidate
   support of J mod3, apart from the last two HIGH coordinates, is
   b=r1-k*H/9-i-a, k=1,2,3,4, a=0,1, 0<=i<nu. Some bands may have
   zero coefficients; that is harmless. Check this covering support
   rigorously, including core precision. Then K R J^T=0 mod3: for
   nonedge bands its selected degrees are approximately H/2-H/6-
   (9-2k)H/18, either negative or strictly between D and H. Edge
   terms are killed by K R e_m=K R e_(m-1)=0. Full index margins matter.

4. A useful EXACT mod3 interpretation of R K^T: its i-th column is
   the coefficient vector of y^(H/3+i)*(y-1)^D. Indeed R's nonzero
   coefficients below H equal those of (1-z)^D and d+m-D=r1.
   Contract these polynomials with the ACTUAL F mod3. The top
   perturbation selects a degree between D and H after multiplication
   by y^(2H/3+i+j)(y^H-1)(y-1)^D; the lower first pole is below the
   shift. Their X_U couplings vanish for the same degree reason, so
   the LOW unit correction in F also vanishes. This would prove
   K R F R K^T=0, including that correction rather than dropping it.

5. J R F e_d vanishes because R F e_d is supported at d,d+1 modulo3
   and those J columns are deep. Extend the edge-support proof to
   F e_(d+1), supported at most at m-2,m-1,m modulo3. K R kills all
   these edges, proving K R F R F e_d=0. Finally (F R F R F)_dd is
   (R F e_d)^T F (R F e_d); it vanishes if F's first 2x2 corner is
   zero modulo3, as supplied by extended direct annihilation.

If these actual bands and precision claims close, A9/3=A27=0 and
T5=0. Otherwise give the precise counterterm. Keep the primitive unit,
transported endpoint and final gcd; no exact q follows from Smith
lower bounds. Fourth rank alone is not evidence for this proposal.

## Critical three-quarters saddle: proposed sharp moments and exact algebra

Use the SAME q-tilted positive principal ensemble as A3turn18.
Let alpha0=sigma/M and Q_(2r)=sum theta_i^(2r), X=sum theta_i.
At d~kappa*n^(3/4), propose endpoint-safe virial identities

E Q6=O(d^4/n^3),
E Q4=2*d^3/(alpha0^2*n^2)+O(d^2/n^2+d^4/n^3),
E Q=d^2/(alpha0*n)+(1/6-alpha0)*d^3/(alpha0^2*n^2)
      +O(d^2/n^2+d^4/n^3).

The safe vector fields are t*g(t)/M and t^3*g(t)/M. Establish fluxes,
pair expansions and errors. The pair correction to the sharp Q mean
must retain the circular cotangent term. Do not replace it by a line
ensemble. For the t^3 virial, sum x^2+xy+y^2 across pairs; the leading
term is 2d E Q and the X^2 term is lower order. The t safe field has
coefficient 1/6-alpha0 after all pair contributions are combined.

For A=1+q, the real characteristic Taylor coefficients are
c2=(q-1)/(2A^3), c4=(1-q)*(q^2-10q+1)/(24A^5).
The candidate actual derivative expansion is
a_q=d/A+(d^2/n)c2/alpha0
    +(d^3/n^2)[c2*(1/6-alpha0)+2*c4]/alpha0^2 +remainder.
The remainder times d/n must tend zero. Signed X and C3 retain the
full phase denominator; fifth absolute moment is O(d^(7/2)/n^(5/2))
by Q4/Q6 and is sufficient at this critical scale. The centered Q
and Q4 covariances must be kept. No large absolute characteristic
partition correction is expanded as a small term.

Candidate second derivative:
beta_q=-d/A^2+(d^2/n)*(2-q)/(alpha0*A^4)+remainder,
with remainder times d^2/n^2=o(1). The algebraic complex covariance
is O(d/n), using the actual denominator; do not delete it without
this estimate. U''' has leading chain-signed 2d/A^3 and a remainder
times d^3/n^3=o(1). Base f''''(1)=12*alpha-3*alpha^2.

For epsilon=d/n, put a=n(a1*epsilon+a2*epsilon^2+a3*epsilon^3),
beta=n(b1*epsilon+b2*epsilon^2), U'''=n*g1*epsilon.
x1=-a1/alpha, x2=-(a2+b1*x1+f3*x1^2/2)/alpha.
The fourth stationary-value coefficient is
-alpha*x2^2/2 +f4*x1^4/24+a3*x1+b2*x1^2/2+g1*x1^3/6.

Independent coordinator exact algebra gives BOTH plus and minus
coefficients (-41+29*sqrt(2))/192, hence their difference is ZERO.
The attached receipt certifies this algebra only. Sharp moment and
actual derivative estimates above remain unproved inputs until audited.
If all inputs close, the critical3/4 whole relative constant remains
4*pi, with actual sectors, connectors, full residual, endpoint,
normality, positive diagonal metric and final gcd retained. Do not
infer b=o(n^(4/5)) without a separately strengthened remainder proof.
