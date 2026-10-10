> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual polynomial coprimality and a modular common-factor restriction

Date: 2026-09-13. Root deduction from the reviewed endpoint and
Wronskian results. Independent review pending.

The searched raw-family notes do not state the following coprimality
deduction. It uses the proved distinction of the actual rational
endpoint approximants, not an assumed genericity of accessory roots.

## 1. No common polynomial factor over the rationals

For every n>=0 the canonical triple (A_n,B_n,C_n) has gcd 1 in Q[z].
Consequently the three polynomials have no common complex root.

Proof. The n=0 triple is (-1,1,4). For n>=1 suppose its monic
common divisor H has degree d>=1, and write r=ord_0 H<=d.
Since B_n(1)=1, H(1) is nonzero. Dividing the three polynomials by
H produces a nonzero rational triple of degree at most m=n-d with

    ord_0 ((A_n+B_n exp(z)+C_n atan(z))/H)
      >=3n+1-r >=3(n-d)+1=3m+1.

The endpoint relation C(1)=4B(1) is preserved. The reviewed uniqueness
of the endpoint-bordered raw problem, including m=0, therefore
identifies this quotient with a nonzero scalar multiple of the
canonical degree-m triple. Its endpoint ratio A(1)/B(1) equals that
at degree n. This is impossible: the fully reduced denominator q_j
has the exact valuation

    v_2(q_j)=j+2 floor((j+2)/4),

which is strictly increasing in j. Thus the endpoint ratios at
distinct degrees are distinct. This contradiction proves gcd=1.
For rational polynomials a common complex root has a rational minimal
polynomial dividing all three, so the complex-root assertion follows.

This does not say that pairs such as A_n,B_n are coprime, that their
integer endpoint values are coprime, or that the Wronskian cubic is
squarefree.

## 2. Any modular common factor has degree at most one

Let n>=1, p>3n, and let (A,B,C) be any nonzero degree-at-most-n
triple over F_p satisfying the raw Taylor equations through degree
3n. No endpoint matching condition is needed. Let H=gcd(A,B,C),
monic, d=deg H, and r=ord_0 H. Then

    3d-r<=3, and hence d<=1.

Proof. The high-row Vandermonde and parity-Cauchy arguments in
`raw_large_prime_endpoint_gcd_carrier.md` show that B,C are both
nonzero. The rational residue/logarithmic-derivative lemma there
therefore makes the polynomial numerator N(A,B,C) nonzero, in this
characteristic as well.

Put (a,b,c)=(A,B,C)/H, of degree at most n-d. Its truncated raw
remainder has order at least M=3n+1-r. The same formal-truncation
Wronskian argument as in the independently reviewed large-prime note
gives

    ord_0 N(a,b,c)>=M-2=3n-r-1.

Only Taylor coefficients through degree M-1<=3n are used. Their
factorial and odd denominators are units for p>3n; after two
derivatives the discarded tails start at degree M-2, which is
already sufficient for this order bound. No infinite exponential
series over F_p is asserted.

The polynomial determinant formula gives

    deg N(a,b,c)<=3(n-d)+2.

Indeed the apparent degree 3(n-d)+3 terms in the derivative
determinant cancel; equivalently its leading coefficient is the
degree expression proved in the raw Wronskian calculation. This
degree bound is a polynomial identity with integer coefficients,
so remains valid in F_p. Since N(a,b,c) is nonzero, comparison
of its order and degree gives 3d-r<=3. As r<=d, this implies
2d<=3 and therefore d<=1.

In particular any common algebraic root of the reduced triple lies
in F_p and is simple in its common divisor. If H=z-a with a!=0,
the Wronskian covariance N(Ha,Hb,Hc)=H^3 N(a,b,c), together with
N=z^(3n-1)Q and deg Q<=3, forces

    Q=q_3(z-a)^3, q_3!=0.

If H=z, the sharper order above instead gives z^2 dividing Q;
this origin case is distinct from the nonzero-root formula.

These are restrictions on the common divisor over the residue
field. They do not determine which primes admit such a divisor,
the p-adic depth of endpoint cancellation, or an upper bound for
the integer gcd carrier.

## 3. Dependencies and next use

The characteristic-zero assertion uses actual bordered uniqueness
and the independently reviewed exact endpoint dyadic valuation.
The modular assertion uses only high-row rank, nonzero polynomial
Wronskian, its degree bound and its rigorously truncated origin
bound. It gives a precise common-root classification without
claiming that a triple root of Q implies a common root of A,B,C;
that converse needs an additional local rank condition.
