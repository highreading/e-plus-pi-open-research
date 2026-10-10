> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Small contiguous recurrences for the scalar forcing center

Status: original author derivation, not independently reviewed. Input definitions and the eventual alternating error are those of ../SCALAR_FORCING_CENTER_DRAFT.md, read in full. This scalar center is distinct from the B-only and full-coefficient Gram centers. No old check, HP scan, or plateau argument is repeated.

## 1. Normalization and second-kind contribution

Extend the definitions to n=0 by P_0=1, Qcal_0=0, Acal_0=1. Put

    E_n=2^n Acal_n/(n!)^2,
    U_n=Qcal_n+E_n=N_n/(n!)^2,
    c_n=U_n/P_n=N_n/Z_n,
    Z_n=(n!)^2 P_n.

Here E_n is a rational exponential companion, not an error. In particular P_1=2, Qcal_1=8, E_0=1, E_1=6, U_0=1, U_1=14.

The known endpoint and second-kind recurrences are, for n>=1,

    (n+1)V_(n+1)=2(2n+1)V_n+4n V_(n-1),
    V=P or Qcal.

Their initial conditions differ. The second-kind generating function satisfies

    R Qcal' -2(1+2t)Qcal=8,
    R=1-4t-4t^2,

where Qcal denotes the generating function in this display. For completeness, its defining convolution gives Qcal'=8G^2+8G' integral_0^t G, with G=R^(-1/2), and hence the displayed equation. Thus its contribution is not discarded when applying the recurrence at n>=1: it survives in the initial data and in the Casoratian below.

## 2. Exact exponential forcing by constant terms

All constant terms here are formal series in t. Each coefficient is well defined by expanding about t=0. Set

    w=(1+t)z-2t+2t/z,
    I(t)=CT_z exp(w)/(1-w),
    J(t)=CT_z exp(w).

Taylor expansion with respect to t, followed by coefficient extraction, gives

    [t^n]I=E_n,
    j_n:=[t^n]J=2^n [z^n](exp(z)q(z)^n)/n!,
    q(z)=1-z+z^2/2.

Indeed w=z+t(2q(z)/z), so the coefficient of t^n in I is the constant term of (2q/z)^n D_z^n(exp(z)/(1-z))/n!.

Define K=CT exp(w)/(1-w)^2 and

    alpha=(1+2t)/(2t(1+t)), gamma=-1/(1+t).

Formal differentiation, using CT zD_z f(w)=0, gives

    I'=gamma I-alpha J+(alpha+gamma)K.

Here the apparent pole at t=0 is removable in the final identity. To eliminate K put v=zD_z w. Then

    v^2=w^2+4tw-8t-4t^2,
    zD_z v=w+2t.

Taking the constant term of zD_z(v exp(w)/(1-w)) yields

    R K=(6t+4t^2)I+(1+4t)J+CT(w exp(w)).

Also J'=alpha CT(w exp(w))+gamma J. Substitution gives exactly

    R I'-2(1+2t)I
      = [J'+(4+8t+8t^2)J]/(1+2t).                 (1)

The controller-backed symbolic calculation simplified these rational coefficients successfully. The constant-term derivation above supplies the reason the identity applies to the actual companion.

Define tau_n by the right side of (1). Then

    tau_n+2tau_(n-1)
      =(n+1)j_(n+1)+4j_n+8j_(n-1)+8j_(n-2),       (2)

with negative-index j and tau equal to zero. In particular j_0=1, j_1=0, tau_0=4. Coefficients of (1) give, for n>=1,

    (n+1)E_(n+1)=2(2n+1)E_n+4nE_(n-1)+tau_n.

Consequently

    (n+1)U_(n+1)=2(2n+1)U_n+4nU_(n-1)+tau_n.      (3)

At n=0 the complete forcing is 8+tau_0=12, rather than tau_0 alone. This is the essential second-kind initial contribution.

## 3. A small explicit forcing generator

Let g_k^(n)=[z^k]exp(z)q(z)^n and set

    s_n=(2^n/n!)(g_n^(n),g_(n-1)^(n),g_(n-2)^(n))^T.

Its first coordinate is j_n. The coefficient recurrence and multiplication by q give

    s_(n+1)=M(n)s_n,

    M(n)=[-2n/(n+1)^2, 2n/(n+1)^2, 1/(n+1)^2;
           2/(n+1), -2/(n+1), 1/(n+1);
           2n/(n+1), 2/(n+1), -(n+2)/(n+1)].       (4)

Initialize s_0=(1,0,0)^T. Equations (2),(4), with two stored delayed j values and tau_(n-1), are a six-coordinate rational forcing generator. No denominator in this generator vanishes for integer n>=0. The factor 1+2t in (1) creates the multiplication by -2 in (2), not exceptional index divisors.

This is a small explicit coupled recurrence, not a large monomial-state closure. Storing additionally P_n,P_(n-1),U_n,U_(n-1) gives ten coordinates and determines the centers; the determinant recurrence below can be maintained with one additional scalar.

## 4. Integer numerator and denominator recurrences

For n>=1 define

    T_n=(n+1)(n!)^2 tau_n,
    a_n=2(2n+1)(n+1), b_n=4n^3(n+1).

Then (3) gives

    N_(n+1)=a_n N_n+b_n N_(n-1)+T_n,
    Z_(n+1)=a_n Z_n+b_n Z_(n-1),                    (5)

with N_0=Z_0=1, N_1=14, Z_1=2. In particular T_n is an integer: the defining formula equals the difference of the three integer terms in (5). This conclusion retains both numerator contributions. No individual summand of tau_n is asserted integral.

Equations (2),(4),(5) form a closed small recurrence for the requested unreduced pair. All index denominators and factorial rescalings are explicit. Only the n=0 initial step is treated separately.

## 5. Factorial cancellation and adjacent determinant

Define

    Delta_n=N_(n+1)Z_n-N_n Z_(n+1),
    D_n=P_n N_(n+1)-(n+1)^2P_(n+1)N_n.

Exactly

    Delta_n=(n!)^2 D_n,                              (6)

and D_n is an integer. Thus the common factorial contributed by both Z entries is removed explicitly before further arithmetic. Substituting (5) gives the first-order forced recurrence

    D_0=12,
    D_n=-4n(n+1)D_(n-1)+T_n P_n, n>=1.              (7)

This is more than a determinant notation: its only new forcing is the six-coordinate generator in Section 3 multiplied by the second-order endpoint sequence.

For a version with every normalization factorial removed, put

    W_n=U_(n+1)P_n-U_nP_(n+1)=D_n/((n+1)!)^2.

Then

    (n+1)W_n=-4n W_(n-1)+tau_n P_n,
    W_0=12,

and hence the closed finite-sum formula is

    W_n=(-4)^n/(n+1)
           [12+sum_(k=1)^n P_k tau_k/(-4)^k].        (8)

In particular

    c_(n+1)-c_n=W_n/(P_nP_(n+1)).                   (9)

There are no factorials hidden in (8),(9). Their entries are rational, not generally integers. Conversely

    D_n=n!(n+1)!(-4)^n
           [12+sum_(k=1)^n P_k tau_k/(-4)^k].

This last expression is NOT a claim that n!(n+1)! divides D_n: the bracket can have denominators. Only (6) asserts an automatic integer factorial divisor. Additional common factors must be determined arithmetically rather than canceled by inspection.

The pure second-kind contribution to W_n is exactly 8(-4)^n/(n+1). The exponential contribution has initial value 4 and the same sum of forcing terms as (8). Thus the constant 12 explicitly retains 8+4; neither component has been suppressed.

## 6. Exact cross-index arithmetic restriction

Let

    g_n=gcd(Z_n,|N_n|), q_n=Z_n/g_n,
    h_n=gcd(q_n,q_(n+1)).

For every prime p, integrality of the reduced adjacent cross numerator and (6) imply

    g_n g_(n+1) divides (n!)^2 D_n.                  (10)

When D_n!=0, write f=v_p(n!), a=v_p(n+1). Then

    v_p(q_n)+v_p(q_(n+1))
      >=2f+2a+v_p(P_n)+v_p(P_(n+1))-v_p(D_n).        (11)

Thus simultaneous reduction at adjacent indices is restricted by the SMALL forced sequence D_n, not merely by the two independent within-index gcds. Equation (7) makes the right side computable from the preceding determinant and the exact exponential forcing. Formula (11) is a necessary inequality; no claim of a sharp valuation of D_n is made.

There is a stronger analytic restriction on the shared reduced factor. For two distinct reduced fractions their nonzero cross numerator is divisible by h_n. Therefore

    |c_(n+1)-c_n| >= h_n/(q_n q_(n+1)),
    lcm(q_n,q_(n+1)) >= 1/|c_(n+1)-c_n|.             (12)

This uses the reduced cross numerator, not the unreduced Delta_n. It is valid even if additional factors cancel in the rational difference.

Put M=1+sqrt(2), s=M^(-2). The retained scalar error bounds imply, beyond the unspecified eventual threshold of the draft,

    |c_(n+1)-c_n| <= C s^n,
    C=12(1+s)/(1-s)^2.

Adjacent errors have opposite signs, so the difference is nonzero there. We use that existing author result rather than re-proving nonstabilization. Consequently

    q_n q_(n+1)/h_n >= C^(-1) M^(2n),
    h_n <= C q_n q_(n+1) M^(-2n).                  (13)

The draft additionally proves v_5(q_n)=2v_5(n!) for n>=5. Accepting that author input in its stated scope, without replaying its residue argument, gives

    v_5(h_n)=2v_5(n!),
    q_n q_(n+1) >= C^(-1) 5^(2v_5(n!)) M^(2n).      (14)

This is a substantive strengthening of the draft's adjacent-product bound: it explicitly removes the shared 5-part before rational separation. Equivalently,

    log q_n+log q_(n+1)
      >= [2log M+(log 5)/2]n-O(log n),

and therefore

    max(log q_n,log q_(n+1))
      >= [log M+(log 5)/4]n-O(log n).                (15)

Legendre's formula 2v_5(n!)=(n-s_5(n))/2 supplies the stated remainder. No dyadic or ternary within-index analysis is duplicated. The finite-sum recurrence (8) also gives an exact rational expression for the difference in (12); the stronger asymptotic statement (14) uses the retained error and 5-adic inputs, not an unproved valuation estimate for that sum.

## 7. Annihilator stopping boundary

Let L_n=Z_n(e+pi)-N_n be the complete unreduced linear form. Equation (5) implies

    L_(n+1)-a_n L_n-b_n L_(n-1)=-T_n.

The coefficient of e+pi is exactly zero in this operation. It creates a rational forcing identity, not an improved nonzero-coefficient approximation to e+pi. Any further annihilation of T_n would give a zero identity and is not pursued as an approximation construction. The same warning applies to applying a common scalar annihilator to P and U after closing the forcing system.

## 8. Scope and preservation

The new results are the constant-term forcing identity, a six-coordinate forcing generator, second-order integer recurrences (5), the first-order factorial-stripped determinant recurrence (7), the fully normalized sum (8), and the cross-index restrictions (10)-(15). No upper bound of the strength needed for an irrationality proof is established. No independent PASS is claimed.

CENTER_PLATEAU_PROPAGATION and its report are unchanged. Its reported textual correction remains F''-F'=-z^2/q^2, replacing the mistyped higher-derivative pair. That earlier proof is not reopened here.
