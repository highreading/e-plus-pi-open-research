> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Two-dimensional cancellation-preserving remainder research

Status: new paper deductions for the relaxed-contact family. No numerical controls were recomputed. No normality theorem, useful lattice basis, or shrinking primitive pair is claimed. The superseded factorial-kernel audit remains unfinished, and its materials are preserved. This note accepts the completed scoped verification and quotient review, including the correction that forward differences give H directly and expansion along evec supplies the sign (-1)^(b+1).

The principal quantitative result is an unconditional two-high-row estimate for an actual exponential companion. Compared with the explicitly stated one-high-row coefficient estimate, it gains an additional factor at most 101/[9(n+3-b)]. This is a strict improvement when n+3-b>101/9. No unidentified norm replaces this saving: the coefficient normalization is identical on both sides of the comparison. An exact signed identity also describes the cancellation required between the exponential and pi errors.

## 1. Definitions and the relaxed reduced system

Take integers n>=b>=2, set M=2n+b, and write

    B(z)=sum_(j=0)^b x_j z^j,
    R(z)=A(z)+B(z)exp(z)+C(z)F(z),
    F(z)=4 arctan(z/(2-z)),

with degree caps (n,b,n), contact R(z)=O(z^M), and B(1)=C(1). Initially b=floor(n/2). The quantitative two-row theorem below requires b>=4.

Use the established functional and monic orthogonal polynomials

    L(P)=integral_-1^1 P((1+iu)/2) du,
    p_k(t)=i^k LegendreP_k(-i(2t-1))/binom(2k,k),
    h_k=L(p_k^2)=2(-1)^k/[(2k+1)binom(2k,k)^2],
    ell_j(t^a)=1/(n+a+1-j)!,
    ell_x=sum_j x_j ell_j.

All factorial arguments are positive for a>=0 and j<=b<=n. Extend ell_j to the analytic functions used below by their Taylor series; the resulting factorial-weighted series converge absolutely.

Let Cstar(t)=t^n C(1/t). Since

    F(z)=z L(1/(1-tz)),

vanishing of the Taylor coefficients of R at indices n+1,...,2n+b-1 is exactly

    L(Cstar t^a)=-ell_x(t^a),  0<=a<=n+b-2.

The first n+1 equations give, uniquely,

    Cstar=-sum_(k=0)^n ell_x(p_k) p_k/h_k.

The remaining equations are precisely

    ell_x(p_(n+l))=0,  1<=l<=b-2.                 (1)

There is no equation with l=b-1. Define

    A_k=p_k(1),
    v_k=L(p_k/(1-t)),
    V_d(t)=sum_(k=0)^d A_k p_k(t)/h_k,
    H_d(t)=sum_(k=0)^d v_k p_k(t)/h_k,
    W_d(t)=1/(1-t)-H_d(t).

Put Y=B(1)=sum_j x_j. Endpoint matching is

    (evec+ell(V_n)) dot x=0,
    equivalently ell_x(V_n)=-Y.                 (2)

Thus the reduced matrix has b-2 high rows and one matching row, acting on b+1 B coefficients. It has a kernel of dimension at least two. If its rank is b-1, the dimension is exactly two. Normality and rank belong to Child 3; no proof of them is attempted here.

Finally,

    A(z)=-[B(z)exp(z)+C(z)F(z)]_(degree<=n).

This reconstruction establishes a linear bijection between the reduced kernel and the relaxed polynomial-triple space. Write X=A(1).

## 2. Complete remainders and projection identities that survive

Summing the complete Taylor tails, with no first-omitted-term replacement, gives

    R(1)=ell_x(W_n)=X+Y(e+pi).                  (3)

Indeed the exponential tail is ell_x(1/(1-t)), while the arctangent tail is L(Cstar/(1-t))=-ell_x(H_n).

Every retained high annihilation permits another exact projection subtraction. Put N=n+b-2. For every n<=d<=N,

    ell_x(V_d)=-Y,
    ell_x(W_d)=R(1).                            (4)

The actual reconstruction of Cstar still uses cutoff n; (4) is an identity for its endpoint functional, not a change of the degree cap.

For cutoff d the established Christoffel-Darboux identities remain

    V_d=[A_(d+1)p_d-A_d p_(d+1)]/[h_d(1-t)],
    W_d=[v_d p_(d+1)-v_(d+1)p_d]/[h_d(1-t)],
    A_(d+1)v_d-A_d v_(d+1)=h_d.                (5)

They concern reference polynomials and do not depend on the omitted last Taylor row. Their disk estimates, reference amplitudes, and complete-tail factorial identities remain valid within their original domains.

The old one-dimensional cofactor formulas must not simply be copied with a shorter high block. In particular, the previous determinant with b-1 high rows and two appended rows was square; it is not square after deleting one high row. The previous selected cofactor vector, rational two-scalar coordinates, primitive alternating matrix, and its specially constructed lambda do not automatically parametrize the new whole space. A further linear slice would have to be specified before importing those one-dimensional formulas.

## 3. An exact companion decomposition for every reduced vector

For any k with n+1<=k<=N+1, define

    a_k(x)=ell_x(p_k/(1-t)).

Apply (4)-(5) at cutoff k-1 and eliminate ell_x(p_(k-1)/(1-t)). The result is

    R(1)=[a_k(x)+v_k Y]/A_k.                  (6)

This is linear in x and also applies when Y=0. All A_k are positive.

For a polynomial P=sum_a P_a t^a, define the rational row

    T_j(P)=sum_a P_a sum_(r=0)^(n+a-j) 1/r!.

The complete factorial tail gives

    ell_j(P/(1-t))=e P(1)-T_j(P).

Consequently, for Y!=0,

    E_k(x)=a_k(x)/(A_k Y)
          =e-r_(e,k)(x),
    r_(e,k)(x)=T(p_k) dot x/(A_k Y).           (7)

Here T(p_k) is the rational row defined above.

Define the rational second-kind value

    w_k=L((p_k-A_k)/(t-1)),
    r_(pi,k)=w_k/A_k.

Then v_k=A_k pi-w_k, so

    R(1)/Y=E_k(x)+pi-r_(pi,k),
    r_(e,k)(x)+r_(pi,k)=-X/Y.                (8)

Unlike the earlier selected one-dimensional decomposition, r_(pi,k) here is fixed once k is fixed. The rational exponential companion absorbs the dependence on the chosen vector in the two-dimensional space. This is a choice of exact decomposition, not an assertion that the previous rational companions coincide with these.

The remaining conditioning in (7) is explicitly algebraic: it is division by the actual rational endpoint Y. In coefficient estimates below we use

    lambda_j=x_j/Y,
    sum_j lambda_j=1,
    K(x)=sum_j |lambda_j|>=1.                 (9)

No bound on K(x) is asserted. It is invariant under rescaling the whole triple and requires no cofactor normalization.

## 4. A signed relation controlling the two errors

The established reference identity v_k A_k/h_k=theta_k, with 1<=theta_k<=2, implies

    v_k/A_k=(-1)^k epsilon_k,
    epsilon_k=|v_k|/A_k>0.

In particular, using k=n+1 in (8),

    (-1)^n E_(n+1)(x)
       =epsilon_(n+1)+(-1)^n R(1)/Y.          (10)

Thus, if |R(1)/Y|<=eta<epsilon_(n+1), the exponential companion has the necessary sign (-1)^n and lies in the explicit interval

    epsilon_(n+1)-eta
      <=(-1)^n E_(n+1)(x)
      <=epsilon_(n+1)+eta.                   (11)

This does not assert that cancellation occurs. It specifies its signed size requirement. For example, for even n the fixed pi error is negative and successful cancellation requires a positive exponential companion.

For two endpoint vectors with nonzero Y_1,Y_2, the common e and fixed pi reference cancel exactly:

    E_k(x_1)-E_k(x_2)=X_1/Y_1-X_2/Y_2.        (12)

For their individually primitive integer pairs (P_i,Q_i), this becomes

    E_k(x_1)-E_k(x_2)
       =(P_1 Q_2-P_2 Q_1)/(Q_1 Q_2).         (13)

Thus an independent pair has distinct companions. Any two companion upper bounds B_i must obey

    |P_1 Q_2-P_2 Q_1|<=|Q_1 Q_2|(B_1+B_2).   (14)

Neither irrationality of e alone nor the nonzero fixed pi error rules out cancellation in the complete remainder.

## 5. Two retained high rows give a new factorial saving

Assume b>=4, put k=n+1, and abbreviate

    p=p_k, q=p_(k+1), A=A_k,
    beta_k=k^2/[4(4k^2-1)].

Both ell_x(p)=0 and ell_x(q)=0 are retained constraints. We construct a rational dual subtraction from their span that removes two Taylor coefficients of p/(1-t), with a bound independent of n on its coefficient cost.

Let

    b_k=A_(k+1)/A_k,
    d_k=p_k'(1)/A_k,
    delta_k=d_(k+1)-d_k.

The established recurrence

    p_(k+1)=(t-1/2)p_k+beta_k p_(k-1)

gives 1/2<=b_k<=2/3. It also proves

    1<=delta_k<=2.                            (15)

Here are the details, avoiding a rank or sign conjecture. At k=0, b_0=1/2 and delta_0=2. Differentiating the consecutive-polynomial ratio at t=1 gives, for k>=1,

    delta_k=1/b_k-[1-1/(2b_k)]delta_(k-1).

If 1<=delta_(k-1)<=2, its lower bound is 2/b_k-2>=1 and its upper bound is 3/(2b_k)-1<=2. Induction proves (15).

The symmetry p_j(1-t)=(-1)^j p_j(t) gives

    p_j(0)=(-1)^j A_j,
    p_j'(0)/p_j(0)=-d_j.

Set the explicit positive rational coefficients

    c_1=1+1/delta_k,
    c_2=1/(b_k delta_k).                       (16)

They satisfy c_1<=2 and c_2<=2. Direct evaluation and differentiation at zero show that

    D(t)=p(t)-(1-t)[c_1 p(t)+c_2 q(t)]

has D(0)=D'(0)=0. Hence D=t^2 J for a rational polynomial J, and

    p/(1-t)-c_1p-c_2q=t^2 J/(1-t),
    a_k(x)=ell_x(t^2 J/(1-t)).                (17)

This is an exact subtraction from the annihilated high-row span, not an approximate projection.

For a polynomial f define the ordinary coefficient norm

    ||f||_1=sum_a |[t^a]f|.

The p_j coefficients alternate in sign: this follows inductively from the recurrence after replacing p_j(t) by (-1)^j p_j(-t), whose coefficients are nonnegative. Therefore, with L_j=||p_j||_1,

    L_(j+1)=(3/2)L_j+beta_j L_(j-1),
    3/2<=L_(j+1)/L_j<=14/9.                  (18)

The initial values are L_0=1 and L_1=3/2; the upper bound follows from beta_j<=1/12 and the preceding ratio being at least 3/2.

Division by t^2 does not change the coefficient norm of D. Equations (16)-(18) give the explicit uniform estimate

    ||J||_1=||D||_1
       <=(1+2c_1)L_k+2c_2 L_(k+1)
       <=(101/9)L_k.                         (19)

For any rational polynomial J, integer d>=0, and s=n+d+1-j>=1,

    |ell_j(t^d J/(1-t))|
       <=||J||_1 sum_(a>=0) 1/(s+a)!
       <=e ||J||_1/s!.

The last step uses s!/(s+a)!<=1/a!. Thus (17)-(19) yield the new actual-tail inequality

    |a_(n+1)(x)|
       <=(101e/9)L_(n+1)
                    sum_(j=0)^b |x_j|/(n+3-j)!.              (20)

No sign assumption on x, no endpoint nonvanishing assumption, no determinant lower bound, and no normality assumption are needed for (20).

For Y!=0 the corresponding exponential companion estimate is

    |E_(n+1)(x)|
       <=(101e/9)[L_(n+1)/A_(n+1)]
                    sum_j |lambda_j|/(n+3-j)!
       <=(101e/9)[L_(n+1)/A_(n+1)] K(x)/(n+3-b)!.           (21)

The conditioning K(x) is the actual rational coefficient-to-endpoint ratio (9). It is the same in the comparison below, and is not an unnamed norm of a newly constructed combined polynomial.

## 6. Explicit comparison with using only one high row

The first high row alone gives the particularly simple exact subtraction

    a_(n+1)(x)=ell_x(t p_(n+1)/(1-t)),

and therefore the one-row bound

    B_one(x)=e L_(n+1) sum_j |x_j|/(n+2-j)!.                 (22)

Let B_two(x) denote the right side of (20). Direct comparison of these positive expressions gives

    B_two(x)<=101/[9(n+3-b)] B_one(x).                      (23)

For x!=0, B_one(x)>0. Therefore (20) is a strictly smaller companion majorant than (22) whenever n+3-b>101/9. In the growing regime b=floor(n/2), this holds for every n>=18 and the additional factor is O(1/n).

For comparison with a bound that uses no high annihilation, define

    B_zero(x)=e L_(n+1) sum_j |x_j|/(n+1-j)!.

Then

    B_two(x)<=101/[9(n+2-b)(n+3-b)] B_zero(x).              (24)

Equations (23)-(24) compare bounds built from the SAME coefficient data. They do not divide upper bounds to estimate a quotient of actual functions. They show a quantified gain from the second retained high row beyond the gain available from the first row alone.

This is not a claim that (20) always improves the earlier G_lambda bound when that bound is evaluated with its exact combined-polynomial norm; those two norms have not been compared. The new assertion is the unconditional improvement (23), with no additional conditioning factor.

The full-remainder bound obtained from (6) is

    |R(1)|<=|Y| epsilon_(n+1)+B_two(x)/A_(n+1).             (25)

Replacing B_two by B_one gives a valid older one-row majorant for the SAME decomposition. Equation (23) strictly reduces its exponential term for the indicated n. It does not prove that the unchanged pi term or the whole bound tends to zero after primitive reduction.

## 7. Projection shifting and further retained rows

For every available k, equation (6) remains exact. The reference estimate accepted from the earlier projection analysis is, for k>=1,

    2 exp(-s) s^k<=epsilon_k<=8 s^k/(1-s)^2,
    s=(sqrt(2)-1)^2.

Thus moving k upward reduces the fixed reference pi term on its proven exponential scale. But the exponential companion changes at the same time:

    E_l(x)-E_k(x)=v_k/A_k-v_l/A_l
                =r_(pi,l)-r_(pi,k).                       (26)

This difference is rational and independent of x. It is therefore invalid to claim a complete-remainder improvement from the smaller pi term alone.

The two-row construction can also be applied with p_k,p_(k+1) whenever BOTH are among the retained high rows, namely n+1<=k<=N-1. Its factorial denominator remains (n+3-j)! because ell_j retains the original n. Its polynomial norm and endpoint normalization become L_k and A_k. No monotonic improvement of the resulting full bound is asserted.

An all-retained-row subtraction would try to cancel more Taylor coefficients at t=0. That requires controlling the associated jet interpolation coefficients. This note has not proved a uniform bound for their conditioning. Rather than hiding that gap in an unspecified residual norm, the quantified claim is limited to the two-row construction (16)-(23), whose coefficient cost is bounded by 101/9 uniformly.

No product of separate high-row majorants is used. The documented quadratic high-row slack is not reintroduced, and no previously rejected loss objective is revived.

## 8. Individual endpoint gcds and coordination with the endpoint lattice

Apply the results to any integer triples in the relaxed kernel, including vectors supplied by a saturated integer-kernel basis or by integer combinations of such a basis. Write their integer endpoints as (X_i,Y_i) and their B coefficients as x_(i,j). For each nonzero endpoint pair separately define

    g_i=gcd(|X_i|,|Y_i|),
    P_i=X_i/g_i, Q_i=Y_i/g_i,
    L_i=P_i+Q_i(e+pi)=R_i(1)/g_i.

When Y_i!=0, the actual positive denominator is q_i=|Q_i|=|Y_i|/g_i. Equation (25) gives

    |L_i|<=q_i epsilon_(n+1)
       +(101e/9)[L_(n+1)/A_(n+1)]
                     sum_j |x_(i,j)|/[g_i (n+3-j)!]

or, equivalently,

    |L_i|<=q_i {epsilon_(n+1)
       +(101e/9)[L_(n+1)/A_(n+1)]
                     sum_j |lambda_(i,j)|/(n+3-j)!}.       (27)

Here lambda_(i,j)=x_(i,j)/Y_i. A coefficient clearer is never substituted for q_i. If starting with rational triples, first clear each whole triple and then take its own final endpoint gcd; lambda and the resulting primitive bound are invariant under this common scaling.

When Y_i=0, use (20) and (6) without dividing by Y_i. If its endpoint pair is nonzero, its primitive full form is +1 or -1, so such a vector cannot occur eventually in a pair of shrinking primitive forms.

The main TWO_DIMENSIONAL_ENDPOINT_BRIDGE.md establishes the intended arithmetic interface: under its rank hypotheses, an endpoint lattice basis has index I=|det(EK)|, and after separate endpoint gcds its primitive determinant is I/(g_1 g_2). For other independent integer combinations, replace I by I|det C|. Equations (13)-(14) and (27) apply to those actual vectors individually. They require no estimate obtained by replacing the primitive denominators with I.

Child 4's ENDPOINT_LATTICE_RESEARCH.md and ENDPOINT_LATTICE_REPORT.md have now been read. Under their stated normality hypothesis, let H be the actual rational coefficient lift and beta_j(u) its B coefficients for a primitive integer direction u=(P,Q). Child 4 proves that its minimal integral lift has coefficients m(u)H u, endpoint pair m(u)u, and endpoint gcd exactly m(u), where

    V=J^(-1)G, d=the least denominator of V, W=dV,
    m(u)=d/gcd(d, entries of Wu).

Consequently our variables on that integral lift are

    x_j=m(u) beta_j(u), Y=m(u)Q, g=m(u),
    q=|Q|, lambda_j=beta_j(u)/Q  when Q!=0.

Substitution in (25) gives the explicit directional bound

    |P+Q(e+pi)| <= B_new(u),
    B_new(u)=|Q| epsilon_(n+1)
       +(101e/9)[L_(n+1)/A_(n+1)]
                     sum_j |beta_j(u)|/(n+3-j)!.           (28)

Equation (28) also holds for Q=0, using the undivided identity (6). It displays exactly where the rational lift enters the estimate. Its denominator d and radial order m(u) supply no additional primitive saving: m(u) cancels term by term against the final endpoint gcd. The two-row versus one-row comparison (23) holds for these same beta_j(u), independently of the radial order.

For two independent primitive directions u_1,u_2, Child 4's sublattice index is m(u_1)m(u_2)|det[u_1,u_2]|/I. A lattice basis is unnecessary. Our analytic target is directly max_i B_new(u_i)->0, or a stronger signed estimate from (10)-(11), evaluated on the two actual rational lifts. This coordinates the new inequalities with Child 4's arithmetic without modifying or independently auditing its files. No comparison of (28) with Child 4's different absolute two-tail majorant is asserted.

For a sufficient paired-form target, choose independent integer endpoint pairs such that the two right sides of (27) tend to zero. The main bridge then removes the need to prove separate nonvanishing of each full remainder. This sufficient estimate has not been established: useful sizes of q_i and the normalized coefficient sums for two independent lattice vectors remain unresolved. Cancellation via (10)-(11) may allow better results than the triangle estimate (27), but no uniform cancellation theorem is claimed.

## 9. Scope of the result

Proved here by paper arguments: the reduced relaxed constraints; the complete linear functional; exact projection subtraction through all retained high rows; the vectorwise rational companion decomposition and signed cancellation relation; the positive rational two-row subtraction; its universal 101/9 coefficient cost; the strict extra factorial saving; and its individual-gcd primitive-pair formulation.

Unresolved: normality, useful endpoint-lattice basis geometry and content, simultaneous primitive smallness, and a stronger estimate exploiting an unbounded number of high rows without uncontrolled jet conditioning. None is inferred from frozen finite controls. No conclusion about the rationality of e+pi follows at this stage.
