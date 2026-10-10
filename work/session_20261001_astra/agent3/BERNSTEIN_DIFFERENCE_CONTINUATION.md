> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Bernstein differences and an ordered-minor endpoint lemma

Status: all 126 successive differences in the saved n=6,b=3 control are strictly negative. The symbolic identities and conditional implications below are proved. Their sufficient inequalities remain unproved on any unbounded growing-degree set. A stronger recurrence shortcut has an exact counterexample and is closed.

The existing control certificate is preserved. No additional HP indices or primes are computed. Full-remainder nonvanishing remains separate. Agent 2 owns the two-scalar quotient audit; this note supplies only its polynomial-Wronskian connection.

## 1. Additional check of saved finite data

The input is bernstein_next_control_certificate.json, SHA-256

    2d2597a0c40f5d681912f33cb934d34e324b70fbad7f82cfbdd0397e0c9ebf20

Its exact Bernstein vectors were read directly. No Legendre family or polynomial Wronskian was reconstructed for the successive-difference check. For each k=0,...,6, the actual degree is L=15+k and the proposed sign is +1. All 133 signed coefficients remain strictly positive. All 126 differences gamma_(j+1)-gamma_j are strictly negative:

| k | Degree L | Strictly negative differences | Zero | Positive |
|---:|---:|---:|---:|---:|
| 0 | 15 | 15 | 0 | 0 |
| 1 | 16 | 16 | 0 | 0 |
| 2 | 17 | 17 | 0 | 0 |
| 3 | 18 | 18 | 0 | 0 |
| 4 | 19 | 19 | 0 | 0 |
| 5 | 20 | 20 | 0 | 0 |
| 6 | 21 | 21 | 0 | 0 |

The first-positive-difference witness is null. This calculation establishes monotonicity of the saved coefficient vectors directly; it does not deduce monotonicity from endpoint attainment of the minimum.

The saved monomial vectors also verify, for every j,

    L(gamma_(j+1)-gamma_j)
      =sum_(u=1)^(j+1) u a_u binom(j,u-1)/binom(L-1,u-1),

where a_u are the signed monomial coefficients. Exact vectors, differences, signs, and source preservation are recorded in bernstein_difference_saved_data_checks.json.

The original endpoint remains

    D_V=19532105792367929/2149019034696302985216000000,
    Y=-D_V.

This is one finite control, not an unbounded theorem.

## 2. Fixed high block and normalization

Fix an even n>=4 and b=n/2. All formulas in the continuation keep this n and this high block fixed. Write

    S=b(b-1)/2,
    c_(k,m)=[t^m]p_k(t),
    C_(k,m)=n![c_(k,m)-c_(k,m-1)]/(n+m)!,
    r_k(x)=sum_m C_(k,m)x^m.

Out-of-range polynomial coefficients are zero. Let

    Rhigh=(r_(n+1),...,r_(n+b-1)),
    w_k=p_k(1)/h_k,
    sigma=(-1)^(b-1),
    eta_k=(-1)^(k+b-1),
    F_k(x)=eta_k Wr(Rhigh,r_k)(x), 0<=k<=n.

The Wronskian has rows in exactly the displayed order and derivative columns 0,...,b-1. Since sign(w_k)=(-1)^k,

    sigma P_(n,k)=|w_k| F_k.

Thus dividing the signed weighted coefficient vector by |w_k| preserves every sign and every monotonicity inequality. Let g_(k,j) be the degree-L_k Bernstein coefficients of F_k, where

    L_k=(b-1)n+b+k,
    delta_(k,j)=g_(k,j+1)-g_(k,j).

The original signed differences are |w_k| delta_(k,j).

The factorial domains are unchanged: ell_j uses 0<=j<=b<=n and minimum factorial argument n+1-b>=1. The transform coefficients use (n+m)! with m>=0. Difference determinants have dimension at most b, and ordinary determinants at most b+1. No negative-factorial extension is used.

## 3. Explicit signed difference formula with actual ordered high-row minors

For an increasing list I of b-1 nonnegative column indices, define the actual high-row minor

    H_I=det[C_(n+l,m)]_(l=1,...,b-1; m in I),

with both row and column orders increasing as written. No sign or positivity property of H_I is assumed.

For M=(m_0<...<m_(b-1)), put

    V(M)=product_(a<c)(m_c-m_a)>0,
    u(M)=sum_a m_a-S,
    B_k(M)=sum_(a=0)^(b-1) (-1)^(b-1+a)
                            H_(M without m_a) C_(k,m_a).

The signs in B_k are expansion along the last row of the b-by-b coefficient minor. With 0<=m_a<=n+b, the coefficient-minor identity becomes

    [x^u]F_k=eta_k sum_(M: u(M)=u) V(M) B_k(M).          (1)

All sums are finite. Increasing nonnegative indices give u(M)>=0. A polynomial identity supplies zeros for coefficient sums above the actual degree.

The elementary binomial identity

    binom(j+1,u)-binom(j,u)=binom(j,u-1)

then gives the exact difference formula

    delta_(k,j)
      =eta_k sum_(M: 1<=u(M)<=j+1)
          V(M) B_k(M) binom(j,u(M)-1)/binom(L_k,u(M)),
      0<=j<L_k.                                       (2)

Equivalently, this follows from the derivative identity in Section 1 and
u/[L binom(L-1,u-1)]=1/binom(L,u).

Equation (2) is a concrete finite-sum inequality target: its right side must be nonpositive. It retains the actual ordered high-row minors, including their cancellations. It neither replaces them by arbitrary nonnegative functions nor presumes total positivity of their coefficient matrix.

## 4. The actual Volterra recurrence and degree elevation

For the same fixed n, the recurrence from GROWING_ENDPOINT_NONVANISHING.md is

    r_(k+1)=(J_n-1/2)r_k+beta_k r_(k-1),
    beta_k=k^2/[4(4k^2-1)],
    J_n(x^m)=x^(m+1)/(n+m+1).

Hence its exact coefficient recurrence is

    C_(k+1,m)=C_(k,m-1)/(n+m)-C_(k,m)/2
                                      +beta_k C_(k-1,m).       (3)

The first term is zero when m=0. The denominator n+m is always positive.

Linearity in the last Wronskian row, with eta_(k+1)=-eta_k, gives

    F_(k+1)=F_k/2+beta_k F_(k-1)+R_k,                  (4)
    R_k=-eta_k Wr(Rhigh,J_n r_k).

For 1<=k<=n-1, R_k has degree L_k+1. It is a shift contribution involving the same fixed high rows; it is not J_n applied to F_k.

Its coefficient-minor formula is obtained by replacing the low coefficient in (1):

    [x^u]R_k
      =-eta_k sum_(M: u(M)=u) V(M)
          sum_a (-1)^(b-1+a) H_(M without m_a)
                                  C_(k,m_a-1)/(n+m_a).         (5)

For a degree-L polynomial, define the elevation operator on its difference vector by

    (E_L d)_j=[(L-j)d_j+j d_(j-1)]/(L+1), 0<=j<=L,

where d_(-1)=d_L=0. This formula follows by subtracting adjacent degree-(L+1) elevated Bernstein coefficients. Its weights are nonnegative; they sum to L/(L+1), not one.

Let tau_(k,j) be the degree-(L_k+1) Bernstein differences of R_k. Equations (4) and degree elevation imply

    delta_(k+1)
      =E_L(delta_k)/2+beta_k E_L E_(L-1)(delta_(k-1))+tau_k,
    L=L_k.                                             (6)

The complete explicit formula for tau is

    tau_(k,j)
      =-eta_k sum_(M: 1<=u(M)<=j+1)
        V(M) binom(j,u(M)-1)/binom(L+1,u(M))
        *sum_a (-1)^(b-1+a) H_(M without m_a)
                                   C_(k,m_a-1)/(n+m_a).        (7)

This is a recurrence in the low-row index k at fixed n,b. It is not an induction from n to n+2: that change also changes the functional and adds a high row. Uniform growing-degree control still requires inequalities for the corresponding high minors.

## 5. A sufficient recurrence inequality, and a shortcut that fails

Equation (6) yields a precise sufficient inequality involving actual ordered minors:

    tau_(k,j)<=-[E_L(delta_k)/2
                       +beta_k E_L E_(L-1)(delta_(k-1))]_j.    (8)

If the preceding difference vectors are nonpositive, the right side is a nonnegative allowance for a positive shift contribution. Formula (7) makes the left side explicit in the high minors and the preceding low-row coefficients.

A quantitative induction form avoids assuming the conclusion. Choose nonnegative arrays a_k of length L_k. Suppose the two base vectors satisfy delta_0<=-a_0 and delta_1<=-a_1, and for k=1,...,n-1 prove

    tau_k<=E_L(a_k)/2+beta_k E_L E_(L-1)(a_(k-1))-a_(k+1).     (9)

Because elevation preserves componentwise inequalities, (6) proves inductively delta_k<=-a_k for all 0<=k<=n. This implication is a proved sufficient lemma. Finding such arrays and proving (9) uniformly for the actual high minors is unresolved. Positive endpoint coefficients g_(k,L_k) are an additional requirement if this route is used to prove the original coefficient-sign conjecture.

The stronger shortcut tau_k<=0 is false even at the existing control. Its first witness, ordered by k then j, is k=1,j=0, targeting the low row 2 and degree 17:

    tau_(1,0)=12152941/7064347530240>0,
    inherited contribution=-984229/144170357760,
    actual delta_(2,0)=-27329/5351778432<0.

Their sum agrees exactly with (6). All 95 shift differences in the five checked transitions k=1,...,5 are positive, whereas every complete difference remains negative. Thus positive inherited allowance matters; the termwise nonpositive-shift shortcut is closed.

This is not a counterexample to the proposed monotonicity of the full coefficient vectors. It is not a counterexample to the weaker original coefficient-sign conjecture, whose 133 coefficients remain strictly positive.

The residual vectors were obtained from saved polynomial data by

    R_k=F_(k+1)-F_k/2-beta_k F_(k-1),

then converted at the common degree L_k+1. No new polynomial Wronskian or HP index was constructed. Their exact values and the degree-elevation checks are in bernstein_difference_recurrence_checks.json. An independent finite-sum verifier accompanies this note to compare them with (7).

## 6. Two endpoint minor sums: a smaller sufficient target

Define

    A_k(x)=T_n(p_k;x)=sum_m D_(k,m)x^m,
    D_(k,m)=n!c_(k,m)/(n+m)!.

Using the same actual high minors, define the rational scalar

    E_k=eta_k sum_M V(M)
          sum_a (-1)^(b-1+a) H_(M without m_a) D_(k,m_a),
      k=n,n+1.                                         (10)

Here 0<=m_a<=n+b. There is no Bernstein conversion and no bound on all coefficients. Cauchy-Binet evaluated at x=1 proves the exact identity

    E_k=eta_k Wr(Rhigh,A_k)(1).                         (11)

Conditional ordered-minor endpoint lemma. For even n>=4, b=n/2, suppose the two explicit sums (10) satisfy

    E_n>=e_n>=0, E_(n+1)>=e_(n+1)>=0,
    e_n+e_(n+1)>0.                                     (12)

Then the actual endpoint obeys

    D_V >= [p_(n+1)(1)e_n+p_n(1)e_(n+1)]
                         /[h_n(n!)^b] >0,
    Y=-D_V<0.                                         (13)

Proof. The exact Christoffel-Darboux transform is

    r_V=[p_(n+1)(1)A_n-p_n(1)A_(n+1)]/h_n.

Since n is even, eta_n=(-1)^(b-1), eta_(n+1)=-eta_n, and h_n>0. Multilinearity and the previously proved cofactor orientation give

    D_V=[p_(n+1)(1)E_n+p_n(1)E_(n+1)]/[h_n(n!)^b].      (14)

The endpoint values p_n(1),p_(n+1)(1) are positive. For instance, this follows directly from p_0(1)=1, p_1(1)=1/2, and the positive three-term recurrence at t=1. Equations (12)-(14) prove the claimed positive lower bound. This also proves rank of the actual reduced system. QED.

The implication is a genuine proof; the uniform hypotheses (12) remain a precise unresolved pair of ordered-minor inequalities. They are not inferred from nonnegativity of arbitrary functions. This target asks for two aggregate minor sums rather than every Bernstein coefficient. No logical implication between the two sufficient sign hypotheses is assumed.

## 7. Connection to the two-scalar draft, without a quotient audit

Let z0 and z1 have the definitions in ../GROWING_TWO_SCALAR_QUOTIENT_DRAFT.md. For a polynomial P, extend Phi_n to P/(1-t) by its factorially convergent series. Its coefficients are eventually constant, so the defining series and every fixed derivative converge locally uniformly in x. The same coefficient cancellation as for polynomials gives

    (D_x-1)Phi_n(P/(1-t);x)=x^n T_n(P;x)/n!.

Removing the exponential row therefore identifies the two contractions as

    z0=(-1)^(b+1) Wr(Rhigh,A_(n+1))(1)/(n!)^b,
    z1=(-1)^(b+1) Wr(Rhigh,A_n)(1)/(n!)^b.

For even n this simplifies to

    z0=-E_(n+1)/(n!)^b,
    z1= E_n/(n!)^b.                                    (15)

Thus (12) supplies z0*z1<=0 and a nonzero pair. This is the polynomial bridge to the draft's sign hypothesis. It does not audit its principal-remainder quotient or companion determinant, which remain Agent 2's task.

Only saved n=6 data were used for a finite bridge check. Transforming its already saved p_6,p_7 coefficient vectors and contracting them with the saved high endpoint jets gives

    E_6=1355870278086451/73150524144312975360000>0,
    E_7=181648924564193/70441245472301383680000>0.

These new scalar contractions use no additional HP index or polynomial family. They are recorded in bernstein_difference_recurrence_checks.json. Their positivity verifies (12) at the existing control only.

The ordinary endpoint sign lemma (13) follows directly from polynomial identities, independently of whether the remainder quotient draft is accepted. The entire remainder is still D_W+T; its nonvanishing does not follow from E_6,E_7 or from an eventual proof of (12).

## 8. Outcome and stopping boundary

Proved identities: the ordered-minor formula (2), the Volterra coefficient recurrence (3), the elevated Bernstein-difference recurrence (6)-(7), and the polynomial bridge (10)-(15). Proved conditional lemmas: the quantitative recurrence implication (9), and the two-minor-sum endpoint implication (12)-(13).

Saved finite evidence: all 126 successive signed differences are negative; the original 133 coefficients remain positive; both endpoint bridge sums are positive at n=6,b=3. These are exact statements about this single frozen control.

Exact failed shortcut: every shift difference need not be nonpositive. The explicit positive tau_(1,0) witness closes that shortcut while leaving both the full monotonicity proposal and the original coefficient-sign conjecture unresolved uniformly.

The most focused next endpoint inequality is (12), expressed by the actual ordered high minors in (10). It could establish an endpoint lower bound with fewer sign requirements than a coefficientwise proof. Alternatively, continuation of the stronger monotonicity route must estimate the positive shift contribution against the inherited allowance in (9); it cannot discard that contribution.

No unbounded endpoint-nonvanishing theorem has been obtained. No full-remainder nonvanishing or reduced-denominator theorem is obtained. The earlier obstruction to the chosen absolute shrinking bounds remains intact; an endpoint gcd cannot overcome that bound ratio.

All new files are confined to work/session_20261001_astra/agent3/. No new degree list, primes, networking, installations, or changes to another agent's files are part of this continuation.
