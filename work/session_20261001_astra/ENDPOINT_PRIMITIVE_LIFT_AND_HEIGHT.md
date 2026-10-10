> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Primitive endpoint lifting and a quantitative height criterion

Status: new main-agent deductions, not independently reviewed. These are conditional structural results about the relaxed construction. No useful asymptotic estimate or conclusion about e+pi is established here.

This note extends TWO_DIMENSIONAL_ENDPOINT_BRIDGE.md. It identifies a limitation of unrestricted endpoint selection and supplies a precise coefficient-height target for the new research allocation.

## 1. Hypotheses and notation

Let V be a two-dimensional rational space of coefficient vectors for matched triples (A,B,C). Assume its endpoint map

    E: V -> Q^2, E(w)=(A(1),B(1))

is an isomorphism. In the relaxed-contact construction, the nonsingularity criterion in the preceding note is sufficient for this assumption; that normality has not yet been established on the desired unbounded family.

Write Phi: Q^2 -> V for the inverse endpoint map, represented by a rational N by 2 matrix. Let

    L=V intersect Z^N,
    Lambda=E(L).

Choose an integer basis K of the saturated coefficient lattice L and put H=EK. Then H is a nonsingular integer 2 by 2 matrix, Lambda=H Z^2, and its index is I=abs(det H)>0. Necessarily Phi=K H^(-1).

For a nonzero primitive endpoint vector v=(P,Q)^T, gcd(abs(P),abs(Q))=1, define kappa(v) to be the least positive integer t such that t Phi v has integer coefficients.

## 2. Exact minimal lift

Let w=adj(H)v, an integer two-vector. Then

    kappa(v)=I/gcd(I,abs(w_1),abs(w_2)).                 (1)

Indeed, t Phi v is integral if and only if t v belongs to Lambda: one implication follows by applying E, and the converse follows from the uniqueness of the lift under E. Membership is equivalent to

    t H^(-1)v = t w/det H in Z^2.

The least positive t satisfying these two divisibility conditions is (1). This also proves directly that kappa(v) divides I. Although H depends on the chosen lattice basis, the minimal t does not.

For primitive v, gcd(abs(w_1),abs(w_2)) divides I. To see this, use H w=(det H)v and a Bezout combination of P,Q equal to one. Thus (1) can also be written

    kappa(v)=I/gcd(abs(w_1),abs(w_2))

for primitive nonzero v. The version retaining I in the gcd is safer for general integer vectors.

The minimal lift c(v)=kappa(v) Phi v is primitive as a coefficient vector. If all its coefficients had a common divisor d>1, its endpoints kappa(v)P and kappa(v)Q would imply d divides kappa(v). The integer vector c(v)/d would then be a lift with the smaller positive multiplier kappa(v)/d, a contradiction.

Nevertheless, the gcd of its two endpoints is exactly kappa(v). Hence a primitive polynomial coefficient vector can still possess a large final endpoint gcd.

Every integer coefficient lift whose endpoint lies on the positive ray through v is a positive integer multiple of c(v). The corresponding multiplier t is a positive multiple of kappa(v).

## 3. Unrestricted primitive endpoint directions

Every primitive pair v in Z^2 occurs after endpoint-gcd normalization of an integer coefficient vector in L. One elementary existence proof is I Z^2 contained in Lambda, which follows from H adj(H)=(det H)Id. Formula (1) gives the minimal lift.

Consequently, at any fixed index where E is an isomorphism, the set of primitive endpoint directions of the unrestricted relaxed construction is exactly the set of all primitive integer pairs.

This observation has two consequences for the research plan:

- Endpoint rank two alone places no restriction on the rational approximants obtainable after arbitrary coefficient combinations and endpoint reduction.
- Neither the endpoint index nor the mere existence of a primitive lift gives a small linear form. Selecting endpoint directions without a quantitative restriction would reintroduce the original Diophantine approximation problem.

This does not exclude the relaxed construction. Its potentially useful content must be a quantitative, computable restriction on the coefficient lifts and their complete remainders, or a prescribed pair for which those estimates can be proved.

In particular, the earlier exclusions of specific one-dimensional constructions do not extend to arbitrary combinations in this larger space.

## 4. Exact cancellation of the lifting multiplier

Put S=e+pi. For w in V, the full evaluated remainder is

    R_w(1)=A(1)+B(1)S.

Thus for the minimal integer lift of a primitive v,

    R_c(v)(1)=kappa(v)(P+QS).

After division by its final endpoint gcd, the form is exactly P+QS. If Q is nonzero, its actual positive reduced denominator is abs(Q), not kappa(v)abs(Q).

For any homogeneous coefficient norm,

    norm(c(v))/kappa(v)=norm(Phi v).                    (2)

Therefore an increase in the arithmetic lifting multiplier cannot improve a homogeneous analytic certificate after primitive normalization. It multiplies the integer remainder, coefficient norm, and final endpoint gcd by the same factor. This is a distinct issue from possible arithmetic advantages in selecting the endpoint direction v itself.

## 5. Pulling a complete-remainder bound back to endpoint space

Let W be a positive definite rational N by N matrix defining a coefficient norm. Suppose a proved bound, valid for every w in V, is

    abs(R_w(1)) <= eta sqrt(w^T W w),                   (3)

where eta>0 and all complete tails are retained. This note does not assert that any currently saved majorant supplies a useful eta and W.

Define the positive definite rational endpoint matrix

    G=Phi^T W Phi.

Equations (2)-(3) give the scale-independent estimate

    abs(P+QS) <= eta sqrt(v^T G v).                     (4)

There is no kappa factor in (4). The rational matrix G records the cost of the coefficient lift in each endpoint direction. A scalar endpoint index does not replace it.

One may also start directly with any rational positive definite G and a separately proved complete-remainder inequality (4). The following lattice argument then applies without choosing a full coefficient matrix W.

A necessary consistency check for a uniform bound (4) is

    (1,S) G^(-1) (1,S)^T <= eta^2.                    (5)

To prove this, extend the inequality from rational to real vectors by continuity and maximize the squared ratio of the linear functional to the quadratic norm. The maximum equals the left side of (5), attained in the direction G^(-1)(1,S)^T. This check prevents interpreting a uniformly tiny coefficient bound as a certificate without retaining its large or poorly conditioned inverse endpoint map.

## 6. An explicit two-vector bound retaining the first minimum

Let

    mu=min {v^T G v : v in Z^2, v!=0} >0.

A minimizing integer vector v_1 exists because G is positive definite. It is primitive, since division by a nontrivial integer common divisor would decrease its squared norm. Complete it to an integer basis (v_1,v_2^0) of Z^2 using Bezout's identity.

Replace v_2^0 by v_2=v_2^0-m v_1, where m is a nearest integer to

    (v_1^T G v_2^0)/mu.

Then det(v_1,v_2)=+1 or -1 and

    abs(v_1^T G v_2) <= mu/2.

Taking the determinant of their Gram matrix gives

    mu*(v_2^T G v_2)-(v_1^T G v_2)^2=det G.

Therefore

    v_2^T G v_2 <= det G/mu + mu/4.                   (6)

Since v_1 is shortest, v_2^T G v_2>=mu. In particular det G>=3mu^2/4, and the right side of (6) also bounds the squared norm of v_1.

Combining (4) and (6), there is a primitive unimodular endpoint pair with

    max_i abs(P_i+Q_i S)
       <= eta sqrt(det G/mu + mu/4).                 (7)

Every such pair lifts to integer triples by Section 2. The two primitive pairs remain independent even though their minimal lifting multipliers can differ.

Thus a sufficient unbounded-family target is

    eta_n^2*(det G_n/mu_n + mu_n/4) -> 0,             (8)

together with the endpoint-isomorphism and complete-bound hypotheses at the same indices. The paired-form criterion then proves irrationality.

The first minimum mu_n cannot be omitted. A determinant estimate by itself does not control the second independent direction. For example, diag(epsilon^2,epsilon^(-2)) has determinant one but its second integer minimum grows without bound as epsilon tends to zero.

Everything defining G and mu is rational if the proposed analytic certificate has rational data. The argument does not use a numerical approximation to S to select directions. However, no favorable bound for the actual G_n or mu_n has been established here. Computing or estimating them must remain part of the construction, rather than an unrestricted search for good rational approximations to S.

## 7. Consequences for the current allocation

Child 3's contact-normality task addresses the endpoint-isomorphism hypothesis. Child 2's new analytic task must furnish a useful complete, direction-sensitive estimate, rather than only a common high-row majorant. Child 4's concrete arithmetic and basis task must retain the coefficient-lift cost, not use the endpoint index as an individual reduced denominator. Child 1's asymmetric family may change those costs and needs its own budget.

Equations (1), (2), and (6) are new exact deductions in this note. Equation (8) is a sufficient quantitative target, not an attained estimate. It provides a way to state precisely what a usable two-dimensional construction still has to prove.

The unconditional rationality or irrationality of e+pi remains unresolved.
