> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An explicit primitive pair from a rational quadratic bound

Status: new main-agent algebraic deduction, not independently reviewed. The required analytic and arithmetic estimates are unproved for the actual e+pi construction. This note replaces an unspecified shortest-vector choice with an explicit rational-center construction.

## 1. Assumptions

Let S be real. Suppose G is a rational positive definite two-by-two matrix and eta>0, and a complete linear-form bound has been proved:

    |P+QS| <= eta sqrt(a P^2+2h PQ+c Q^2)

for every integer pair (P,Q), where

    G=[[a,h],[h,c]],  D=ac-h^2>0.

The bound must include the full evaluated remainder. In the relaxed construction it can arise by pulling a coefficient norm through the rational endpoint lift. A companion-only estimate does not meet this hypothesis.

Write the rational center in lowest terms as

    h/a=p/q,  q>0, gcd(|p|,q)=1.

Completing the square gives the exact identity

    (P,Q)G(P,Q)^T = a(P+(p/q)Q)^2+(D/a)Q^2.       (1)

The center depends only on rational construction data. No approximation to S is needed to define it.

## 2. Explicit independent primitive vectors

Set v1=(-p,q). Choose integers x,y with

    qx+py=1.

Such integers exist by coprimality. Replacing (x,y) by (x-kp,y+kq) preserves the equation. Choose k so that |y|<=q/2, and put v2=(x,y).

Then

    det[v1 v2]=-1.

Both vectors are primitive. Their denominators are q and |y| when the latter is nonzero. These are actual endpoint denominators after primitive reduction, not denominators of coefficient lifts.

Equation (1) yields

    v1^T G v1 = D q^2/a,
    v2^T G v2 = a/q^2+(D/a)y^2
                <= a/q^2+D q^2/(4a).               (2)

Consequently, defining

    E=eta^2 a/q^2,
    F=eta^2 D q^2/a,

we have the complete-form bounds

    |-p+qS| <= sqrt(F),
    |x+yS| <= sqrt(E+F/4).                         (3)

The exact relation

    q(x+yS)-y(-p+qS)=1

also proves that these two forms cannot vanish simultaneously for any real S.

If the rational endpoint lift is an isomorphism, each vector lifts to an integer polynomial triple after multiplication by its own minimal integral lifting factor. As proved in ENDPOINT_PRIMITIVE_LIFT_AND_HEIGHT.md, that factor equals the endpoint gcd and cancels from the primitive remainder. Different lifting factors therefore do not alter (2)-(3) or the endpoint determinant -1.

## 3. A sufficient same-index criterion

For an unbounded sequence of actual constructions satisfying the complete-bound hypothesis, it is sufficient to establish

    E_n=eta_n^2 a_n/q_n^2 -> 0,
    F_n=eta_n^2 D_n q_n^2/a_n -> 0.                (4)

Both independent integer forms then tend to zero. If S=u/v were rational, multiplying both forms by v would give integers tending to zero. They would eventually both vanish, contradicting their determinant. Hence (4) would prove S irrational.

Neither condition in (4) has been established here for S=e+pi. The normality theorem reported by Child 3, even if accepted, supplies only a domain for the lift, not these quantitative estimates.

The two conditions require the actual reduced q to lie in a useful range:

    eta_n^2 a_n << q_n^2 << a_n/(eta_n^2 D_n),

where each comparison means that the corresponding ratio tends to zero. Their product is

    E_n F_n=eta_n^4 D_n.

Thus eta_n^4 D_n->0 is necessary for this particular certificate, but is not sufficient: the center denominator must also satisfy both separate inequalities.

A uniform rescaling G->lambda G and eta->eta/sqrt(lambda), for positive rational lambda, leaves the center, E, and F unchanged. A common scaling cannot create a gain.

## 4. The exact arithmetic object

Let L be any positive integer clearing a and h, and set

    A=L a>0,  B=L h.

Then

    q=A/gcd(A,|B|).                                (5)

Increasing L changes numerator and gcd together and leaves q unchanged. Estimating a coefficient clearer, the least denominator of the whole lift, or the endpoint-lattice index does not establish (5)'s asymptotics.

For an actual lift Phi and positive rational coefficient matrix W,

    a=Phi_1^T W Phi_1,
    h=Phi_1^T W Phi_2,
    D=det(Phi^T W Phi).

The final gcd in (5) can contain cancellations absent from entrywise denominator estimates. It must be retained exactly. The choice of W must be justified by a proved analytic inequality, not selected by assuming a favorable gcd.

## 5. Consistency and limitations

The uniform complete-form inequality at (P,Q)=(1,0) implies eta^2 a>=1. Therefore E_n->0 forces q_n->infinity. If q=1, the Bezout construction permits y=0 and v2=(1,0); its form equals one, so this case cannot yield a shrinking pair.

A small determinant alone does not suffice. A rational center with bounded q leaves the independent direction uncontrolled even when the first vector is very small. Conversely, an excessively large q can make F large. Both effects are visible in (4).

This criterion is sufficient, not necessary for the success of the family or for irrationality. Other primitive endpoint pairs can be more effective than this particular center pair. Failure of (4) closes only this certificate unless a separate argument proves more.

Unlike the previous first-minimum formulation, this construction requires no unspecified integer minimizer. Its unresolved arithmetic is concentrated in one explicit reduced rational center, and its unresolved analysis is concentrated in a, D, and eta in the same normalization.

## 6. Research allocation

Child 2 develops a complete direction-sensitive remainder bound and a defensible rational norm. Child 3 develops the actual inverse lift in its new slow-growth normality range. Child 4 examines that genuinely new normality claim and then researches the reduced center denominator. Child 1 develops a distinct fixed-weight asymmetric alternative.

No unconditional rationality or irrationality conclusion about e+pi is obtained in this note.
