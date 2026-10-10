> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A rectangular reference estimate and the missing mixed-source bridge

Coordinator derivation,8October2026, independently reviewed in A4turn2. It generalizes
the new A5 inverse-ensemble lemma as a reusable positive-reference statement.
It does not assert a complete new integer approximation family.

## Scoped gate

The prior compact square and the shifted short/wide pole-border analyses are
already established background. The coordinator read the complete prior
UNIFORM_GAMMA_COMPACT_LEADING_NONZERO.md and the short-rectangular gate, and
searched unequal/asymmetric channel degrees and the inverse-ensemble notation.
The former concerns a shifted leading coefficient, not the full unequal-channel
affine H below. A5turn0's inverse moment is a new active-round input, directly
checked by the coordinator; classical integration by parts and Andreief are
reused. Primary background and exact ensemble-scope cautions are recorded in
INVERSE_ENSEMBLE_AND_ARITHMETIC_GATE.md. No global novelty is asserted.

## 1. Reference trace for arbitrary sizes

For integers m,n>=1 use the probability density on(0,infinity)^m

    P(t)/[m! Z_(m,n)]
       =V(t_1^2,...,t_m^2)^2 prod_i t_i^(2n)e^(-t_i)/[m! Z_(m,n)],
    Z_(m,n)=det((2n+2i+2j)!)_(i,j<m).

Summing the derivatives of P gives

    2n E sum_i1/t_i-m+4 E sum_(i<j)1/(t_i+t_j)=0.

The last term is nonnegative, hence E sum1/t<=m/(2n). Summing derivatives
of P/t_i cancels the antisymmetric pair terms and gives

    (2n-1) E sum1/t_i^2=E sum1/t_i.

All boundary terms vanish; the collision expressions are derivatives of the
original polynomial density. Therefore, with

    M_0=((2n+2i+2j)!), M_-1=((2n-2+2i+2j)!),
    a_(m,n)=m/[2n(2n-1)],

one obtains

    tr(M_0^(-1)M_-1)<=a_(m,n),
    E prod(1+u/t_i^2)<=exp(u a_(m,n)) for u>=0.        (1)

No moment after2n+4m-4 is introduced, and the inverse matrix only lowers
moment powers. The reference density is V(t^2)^2, not V(t)V(t^theta).

## 2. Exterior mixed determinants at unequal dimensions

For any fixed compact nodes y_j in[0,1], with n nodes for the numerator
and n-1 nodes for the slope, use the positive exterior Gram weights

    Q_D(x)=prod_(j=1)^n(x-y_j),
    Q_S(x)=(x+1)prod_(j=1)^(n-1)(x-y_j), x>1.

Against dmu_ext=e^(-1-sqrt(x))dx/(2sqrt(x)), normalize the m-by-m
determinants by e^(-m)Z_(m,n). Bernoulli on the exterior and the nonpositive
right side when one x_i<=1 give, uniformly in every node tuple,

    1-n a_(m,n)<= normalized exteriorD <=1,
    1-(n-1)a_(m,n)<= normalized exteriorS <=exp(a_(m,n)), n>=2. (2)

At n=1 the cutoff argument for the slope's stated lower bound1 does not apply:
outside the exterior the right side1 is positive whereas the integrand is zero.
The independently verified universal replacement is

    1-a_(m,1)<= normalized exteriorS <=exp(a_(m,1)).

Indeed 1_{all t_i>1} prod(1+t_i^(-2))>=1-sum t_i^(-2).
This repairs the proof's scope; it does not assert that the stronger numerical
bound1 is false at every n=1 instance. Earlier request manifests retain the
pre-repair source hashes. All actual square uses have n>=64.

In particular the first lower bound is positive if m<4n-2. These are
EXTERIOR statements. No full overlap or negative-atom payment at unequal
sizes has been proved or inserted here.

For n>=2, the parent correlated comparison can be repeated with R_n(nu),
provided the underlying full two-measure identity has first been justified.
For the two slope weights Q_plus/minus=(x+/-1)prod_(j<n)(x-y_j), set

    c=1-(n-1)a_(m,n), eta=2a_(m,n)/c.

When c>0 and eta<1, the same trace proof gives detB_minus/detB_plus>=1-eta.
Indeed B_plus>=e^(-1)(M_0-(n-1)M_-1), their difference is2C with
0<=C<=e^(-1)M_-1, and tr(2B_plus^(-1/2)CB_plus^(-1/2))<=eta.
This leads to the exterior normalized ratio in[1-eta,1], but ONLY after
both original raw/J normalizations have been checked. It remains conditional
on the actual source identity and complete perturbation payments.

## 3. Unequal degrees do not automatically preserve the single affine period

Consider the naive(m+n)-row rational pencil

    H_(m,n)(s)=det[C_m | Lambda*(R_n+s w v_n^T)],

where contact column j is(c_(r+j)),0<=j<m, and the right block uses
r_(r+j),0<=j<n. Its s response is still rank one and its determinant affine.
At s0=e+pi the exact moment relation is

    r_(r+j)+s0*(-1)^(r+j)=nu_(r+j)-e*c_(r+j).

If m>=n, each of the n contact vectors is an original column of C_m,
so adding e times that column to the corresponding right column gives the
full compact block exactly. The same determinant-preserving bridge is valid.

If n>m, only the first m additions are available in the unchanged contact
span. The remaining n-m vectors require an additional linear-dependence or
source-cancellation theorem. Expanding those remaining columns can introduce
powers of e up to degree n-m; an exterior determinant bound is not a theorem
for H_(m,n)(e+pi) until this gap is paid. We do not assert that all these
coefficients are nonzero, merely that their vanishing is not supplied by the
old column-addition identity. Reducing contact count cannot silently retain
that identity.

For m>=n the physical contact maximum is n+2m-2, giving exactly the factorial
boundary2n+4m-4 in(1). The compact maximum is m+2n-2. The slope's(1+y)^2
factor restores this same compact boundary. All have explicit finite scope.

Thus m<n is a possible changed research problem only with a genuinely new
mixed-source bridge; m>=n preserves the basic bridge but still needs all
full signed estimates and actual all-prime content. Neither case currently
provides q*error decay or an irrationality theorem.
