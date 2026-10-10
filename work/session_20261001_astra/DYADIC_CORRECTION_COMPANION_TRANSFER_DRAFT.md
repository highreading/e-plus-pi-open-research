> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational corrections and the complete dyadic denominator

Status: main-agent author deductions, not independently reviewed. The elementary rational-addition lemma below is independent of the large-selector construction. Its application retains the pending complete dyadic theorem and the quantitative approximation input for pi. No numerical calculation is claimed. This note preserves the previously unsaved deduction.

## 1. Exact rational-addition lemma

Write two reduced rational numbers as

    c0=A/(2^a B), r=C/(2^d D),

where B,D are positive odd integers, a>0, and d>=0. For r=0 use C=0,d=0,D=1. Since c0 is reduced, A is odd; if d>0 then C is odd.

If a>d, addition over denominator 2^a BD gives numerator

    AD+2^(a-d)CB,

which is odd. If d>a, the numerator over denominator 2^d BD is

    2^(d-a)AD+CB,

which is odd. Odd cancellations do not change the power of two in a denominator. Therefore, whenever a!=d,

    v_2(den(c0+r))=max(a,d).                       (1)

If d=a, the numerator is AD+CB and the exact formula is

    v_2(den(c0+r))=max(0,a-v_2(AD+CB)).             (2)

Here v_2(0)=infinity, so a zero sum has denominator one. Thus dyadic cancellation requires equality of the two initial denominator exponents. Equation (2) retains the exact numerator whose valuation decides the cancellation depth.

## 2. Application to the complete large-selector center

Let n=4k tend to infinity, fix rho>0, and suppose

    m=rho n log n+o(n log n).

Use the saved large-selector construction

    Bpoly(t)=(1-2t+2t^2)^n(1-4t+2t^2)^(2m),
    K(t)=t^n Bpoly^(n)(t)/n!, U=K(1),
    J=n+4m, N=2n+4m.

Restrict to U!=0. Let c0=alpha+beta be its complete rational center and q0=den(c0). The author coefficient proof gives v_2(U)>=n/2.

The complete dyadic theorem awaiting its limited examination asserts

    a:=v_2(q0)=v_2(n!)+v_2(J!)+v_2(U)-N/2.

Conditional on that theorem, the coefficient divisibility and binary factorial formula imply

    a>=3n/2+2m-s_2(n)-s_2(J),                      (3)

where s_2 denotes binary digit sum. In particular, with X=n log n,

    liminf a/X>=2rho.

Now let r=r_n be a rational correction satisfying

    log den(r_n)=o(X).

Its dyadic denominator exponent d satisfies d log 2<=log den(r_n), hence d=o(X). Since rho>0, eventually d<a. Formula (1) proves

    v_2(den(c0+r_n))=v_2(q0)                       (4)

for every sufficiently large admitted index. This preserves the actual dyadic denominator, not merely a denominator clearer. It does not determine the odd part of the corrected denominator.

More generally, any correction with a different dyadic denominator exponent obeys (1). Corrections whose exponent equals a require the exact test (2); their cancellation must not be assumed or ruled out without that test.

## 3. Transfer through the actual combined companion

Put

    gamma=beta+r_n, c=alpha+gamma,
    q=den(c), Bgamma=den(gamma).

All denominators are reduced positive denominators. Assume

    limsup log Bgamma/X<=b,

where b>=0 is finite. This is a condition on the actual sum beta+r_n, not on a product of separately cleared denominators.

The saved author exponential estimate is

    |e-alpha|<=E,
    E=3 Lambda^n exp(Lambda/(n+1))
                    /((n+1)(n!)^2 |U|),
    Lambda=2n+8m.

The coefficient divisibility and saved Cauchy bound give log|U|=o(X), hence

    -log E/X -> 1.                                (5)

Use the retained elementary approximation theorem for e: for every epsilon>0 there is C_epsilon>0 such that

    |e-u/v|>=C_epsilon v^(-2-epsilon)

for every reduced rational u/v. Since alpha=c-gamma,

    den(alpha)<=q Bgamma.

Combining this with (5) gives

    liminf log q/X>=1/2-b.                         (6)

Under the dyadic input and correction hypothesis of Section 2, equation (4) also gives

    liminf log q/X>=2rho log 2.                    (7)

Together, (6)-(7) yield

    liminf log q/X>=max(2rho log 2,1/2-b).          (8)

Now assume a finite quantitative approximation bound for pi:

    |pi-u/v|>=C_pi v^(-mu),

with mu>0 and C_pi>0, uniformly over reduced rationals. If mu b<1, then (5) makes E negligible relative to C_pi Bgamma^(-mu). The reverse triangle inequality gives, eventually,

    |c-(e+pi)|>=C_pi Bgamma^(-mu)/2.

Consequently

    liminf log(q|c-(e+pi)|)/X
      >=max(2rho log 2,1/2-b)-mu b.                 (9)

A strictly positive right side proves divergence of these primitive errors. A nonpositive bound supplies no divergence conclusion. The separate strict condition mu b<1 is retained; denominator growth alone does not establish dominance of the logarithmic component.

## 4. Dependencies and unresolved arithmetic

Equations (1)-(2) are elementary author proofs for reduced rational numbers. Equations (3)-(4) and (7)-(9) depend on the complete dyadic denominator theorem. Its review has not yet been reported complete.

The external pi theorem must be checked in the located offline primary source, using an exponent strictly above its stated irrationality-measure bound. No unchecked numerical exponent is used here. The transfer argument itself is proved from the displayed quantitative inputs.

The decisive arithmetic target is an upper bound for Bgamma=den(beta+r_n) after cancellation. The subfactorial denominator condition on r_n preserves the dyadic contribution but does not itself establish a useful upper bound for Bgamma.

The new Child 1 report claims the refinement den(beta) divides O_J|U|/2, where O_J is the odd lcm through J=n+4m. Its proof has not yet been inspected by the main in this continuation. Replacing N by J changes the existing coarse logarithmic bound by O(n), not its leading n log n rate. No improved leading rate is inferred from that report.

This criterion concerns specified rational approximation families. It does not decide the irrationality or rationality of e+pi.
