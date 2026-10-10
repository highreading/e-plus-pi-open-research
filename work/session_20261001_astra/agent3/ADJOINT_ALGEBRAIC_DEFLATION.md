> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Algebraic deflation of the actual factorial B-Gram adjoint

Original author research, offline; not an independent audit. The retained B_CENTER_ADJOINT_NONVANISHING criteria and their moment bounds are inputs, not rechecked here. Work concerns the actual B-only factorial metric, not another center. Retain the even-index domain and provisional contact reduction of that note.

## 1. Primitive normalization retaining the actual equations

Use K=Krec^T W Krec, X=adj(T)fP, V=X^T KX>0, and ell=adj(T)^T KX. The actual adjoint polynomial is L=P/V, P(t)=sum ell_i t^i. In particular ell^T fP=V.

Let D be the least common multiple of the positive denominators of ell_i. Put c=gcd_i |D ell_i|>0 and G=P D/c in Z[t]. This fixes its sign by P, rather than changing the leading coefficient sign. Thus G is primitive and

    L=eta G, eta=c/(DV)>0,
    F_n(G):=sum_i G_i fP_i=1/eta>0.

All scaling and content remain recorded. The positive normalization is an exact constraint on this particular reconstructed polynomial.

## 2. Exact maximal deflation and a matrix criterion

Set psi=1-4t+2t^2. For a coefficient vector g of degree d, formal division at t=0 defines

    h_-2=h_-1=0,
    h_k=g_k+4h_(k-1)-2h_(k-2), 0<=k<=d,

where g_k=0 beyond its degree. For d>=2, psi divides G if and only if h_(d-1)=h_d=0. In that case H=sum_(k=0)^(d-2) h_k t^k is the exact quotient. For d<2 a nonzero polynomial cannot be divisible. Repeating this test gives the maximal r and G=psi^r H. It terminates with r<=floor(d/2).

The recurrence is integral: there is no suppressed power of two or denominator. Gauss's lemma gives content(H)=1 at every successful division, because content(psi)=content(G)=1. If instead a nonprimitive integer multiple cG is divided, its quotient retains content c. This distinguishes polynomial content from an endpoint or companion gcd.

Equivalently let M_r be multiplication by psi^r from degree <=d-2r to degree <=d. It is an explicit integer convolution matrix. The actual condition is

    ell in image_Q M_r,
    rank[M_r | adj(T)^T K adj(T)fP]=rank M_r.

One can also impose the original adjoint equation without an adjugate:

    K T^(-1)fP in image_Q(T^T M_r).

Thus common factors arise exactly when the reconstructed weighted forcing covector lies in this specified subspace. This includes both inverse factors and the factorial reconstruction metric. Accretivity alone does not prohibit the subspace intersection. No assertion that the actual r is always zero is proved.

A quotient-ring implementation reduces powers of t modulo psi^r and applies the resulting 2r-by-(d+1) remainder matrix to ell. Its kernel gives the same test. These criteria are finite rational algebraic conditions on the actual solved equations, rather than independent assignments of saddle multiplicities.

The roots a=1-1/sqrt(2) and A=1+1/sqrt(2) have the same multiplicity r in G. Maximality implies H(a)H(A)!=0.

## 3. Resultant lower bound

For h=deg H, the nonzero integer resultant satisfies

    R=Res(psi,H)=2^h H(a)H(A),
    |H(a)|>=1/(2^h |H(A)|).

This includes constant primitive H, where |H|=1. It is useful only with an upper bound on the conjugate value. A coefficient-height estimate is not substituted for the normalization below.

## 4. The actual normalization at the conjugate saddle

Put rho=1/sqrt(2), v(t)=t^2-t+1/2. The retained forcing identity gives

    F_n(G)=[D_t^n(v(t)^n G(t))]_(t=1).

Cauchy's derivative formula on t=1+rho exp(i theta), -pi<=theta<=pi, yields exactly

    F_n(G)=n!/(2pi) integral (1+sqrt(2)cos theta)^n
                                  G(1+rho exp(i theta)) dtheta.

Indeed v(t)/(t-1)=1+sqrt(2)cos theta on this circle. Define

    Zplus=1/(2pi) integral (1+sqrt(2)cos theta)^n dtheta>0,
    Eplus[f]= integral weight*f / integral weight,
    B=F_n(G)/(n! Zplus)>0.

For even n the weight is nonnegative on the full circle, including its distant portion. Conjugation makes the integral real. Precisely what normalization controls is

    Eplus[G(1+rho exp(i theta))]=B.

It does not directly bound G(A), H(A), or a positive average of H on a real interval. Polynomial values on the circle can have either sign in their real part.

Here is an explicit derivative condition that closes this loss. Write delta=rho(exp(i theta)-1), p=exp(2i theta)-1, and H_k=H^(k)(A)/k!. Since psi(1+rho exp(i theta))=p,

    B=sum_(k=0)^h beta_(r,k) H_k,
    beta_(r,k)=Eplus[p^r delta^k].

Every beta is real and exactly specified. In fact it belongs to Q(sqrt(2)): expand the trigonometric polynomials and take their constant terms; the common Zplus is their positive constant-term denominator. Define the equally explicit positive bounds

    b_(r,k)=Eplus[|p|^r |delta|^k].

Then |beta_(r,k)|<=b_(r,k). If beta_(r,0)!=0 and derivative information supplies

    sum_(k=1)^h b_(r,k)|H_k|
                 <=epsilon |beta_(r,0)| |H(A)|, epsilon<1,

normalization gives the two-sided bound

    B/((1+epsilon)|beta_(r,0)|) <= |H(A)|
       <= B/((1-epsilon)|beta_(r,0)|).

Consequently

    |H(a)| >= (1-epsilon)|beta_(r,0)|/(2^h B).

This is a normalization-based resultant bound, with its exact missing derivative hypothesis displayed. Alternatively any known absolute bound E on the derivative sum gives |H(A)|<=(B+E)/|beta_(r,0)|. When beta_(r,0)=0 the normalization has no H(A) term at all; derivative information must include another relation to recover that value. The exact coefficient beta_(r,0), rather than its nonvanishing by assumption, is part of the criterion.

For r=0, beta_(0,0)=1. Thus the preceding result specializes to the particularly direct condition sum_(k>=1)b_(0,k)|H_k|<=epsilon|H(A)|. Without this or an absolute derivative bound, the positive forcing normalization only fixes an average, not a pointwise upper bound. No such derivative control for the actual reconstructed family has yet been proved.

## 5. Deflation on the left arc: odd multiplicity matters

On t=1-rho exp(i theta), psi(t)=exp(2i theta)-1 again. Define x=1-cos theta and the real polynomial

    C_G(x)=Re[psi(t)^r H(t)].

It is exactly computable by the retained Chebyshev coefficient transformation applied to G; all coefficients are in Q(sqrt(2)). Let C_G=sum c_j x^j. Its degree is at most d and it is not identically zero. The retained transformation is invertible on real polynomials.

There are explicit first possible terms. If r=2s is even,

    c_j=0 for j<s,
    c_s=(-8)^s H(a)!=0.

This follows from psi(t)=2i theta+O(theta^2), t-a=-i rho theta+O(theta^2), and theta^(2s)=2^s x^s+O(x^(s+1)). Thus even multiplicity determines the first surviving real-arc order exactly. The resultant bound of Section 4 gives, under its stated derivative condition,

    |c_s| >= 8^s(1-epsilon)|beta_(r,0)|/(2^h B).

If r=2s+1 is odd, the leading odd power of theta has zero real part. Instead

    c_j=0 for j<s+1,
    c_(s+1)=(-1)^(s+1)2^(3s+2)
                        [r H(a)-rho H'(a)].

This uses psi=2i theta-2theta^2+O(theta^3). Therefore H(a)!=0 does NOT by itself guarantee a nonzero first possible real saddle term in the odd case.

Define the integer polynomial

    J_r(t)=rH(t)+(t-1)H'(t).

The odd leading coefficient vanishes exactly when psi divides J_r. This is a new explicit secondary algebraic obstruction, tested by the same remainder recurrence. Rational conjugacy forces its conjugate relation rH(A)+rho H'(A)=0 as well. There is no license to prescribe those relations independently.

If psi does not divide J_r and j=deg J_r, its integer resultant supplies

    |J_r(a)|>=1/(2^j |J_r(A)|).

For r>0, J_r is nonzero: in powers of t-1 its operator has positive diagonal entries r+k. With a derivative bound |H'(A)|<=D1|H(A)|, the conjugate bound becomes

    |J_r(A)|<=(r+rho D1)|H(A)|.

Combine it with Section 4 to lower-bound the odd coefficient. If psi divides J_r, further c_j must be retained; the exact finite transformation identifies the first nonzero coefficient, but no universal claim about that later order is made.

## 6. Positive-moment remainder and complete error

Use the retained left-arc Jminus and normalized positive moments mu_j of x, with their established lower and upper bounds L_j(n),U_j(n). For even n,

    epsilon_F=-2n! eta Jminus sum_j c_j mu_j.

If k is the first nonzero coefficient, the explicit sufficient domination condition is

    |c_k| L_k > sum_(j>k)|c_j| U_j + Eother,

where

    Eother=(|kappa|+9 eta N_G M^n/(n+1))
                                      /(2n! eta Jminus),
    N_G=sum_i |G_i|rho^i, M=1+sqrt(2).

Use L_0=1. A fully elementary upper bound for Eother follows by replacing Jminus with the retained lower bound chi^n sqrt(pi/(cn))(1-10/n). No endpoint term or exponential contribution has been omitted. Under this inequality the complete B-center error is nonzero and has sign opposite c_k.

For even r, the first term is therefore the resultant-controlled c_s, with every later coefficient retained as a derivative remainder. For odd r, the same mechanism first requires nondivisibility of J_r by psi and a bound on its conjugate value. This explains exactly why simply deflating G and applying a resultant to H is insufficient in the odd case.

## 7. Outcome and remaining gap

The new results are an integer division recurrence preserving content, an actual Toeplitz/reconstruction subspace criterion for maximal r, an exact conjugate-circle normalization, and normalization-based resultant bounds conditional on explicit derivative control. Even and odd multiplicities lead to different real-arc orders; the odd case exposes the additional polynomial J_r.

No claim is made that the actual family satisfies the derivative inequality, avoids the secondary factor, or dominates the complete remainder on an unbounded set. Those are explicit next algebraic and analytic conditions, not a missing tool or a finite-sample question. No coefficient-height substitute, selector-prime analysis, companion-gcd work, old checker replay, or independent audit is performed. The existing nonvanishing criteria are preserved.
