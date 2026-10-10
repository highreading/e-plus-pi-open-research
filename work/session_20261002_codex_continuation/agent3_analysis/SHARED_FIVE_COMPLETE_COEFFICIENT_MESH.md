> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete coefficient mesh and Gaussian phase of the shared-five correction

2026-10-02. Original author analysis by agent3. The selector owns the exact period elimination, primitive quadratic, endpoint formula and corrected-denominator arithmetic. The arithmetic agent owns the reflected actual prime depths. This note derives the real mesh, a Gaussian phase lower bound, and the cost of tuning the complete residual. It does not audit those interfaces or prove anything about the rationality of e+pi.

## 1. Fresh gate and exact interface

The dated archive queries, inspected overlap, fresh primary queries and URLs are preserved in `CORRECTION_REAL_MESH_PROGRESS.md`. The archive's adjacent-selector congruence notes retain a similar joint real/arithmetic obligation, but do not analyze this Gaussian endpoint mesh. Item389 concerns a different mixed polynomial identity. The present endpoint formula and actual q interface are attributed to `agent2_selector/EVEN_LEADING_QUADRATIC_CORRECTION_COST.md`, Sections6–7, and the selector's subsequent general rational-coefficient handoff saved in `agent2_selector/RATIONAL_SCALED_SHARED_FIVE_FULL_Q.md`. Search absence is not a global novelty claim.

The primary logarithmic-form inequality used below is read in Min Sha, *Effective results on the Skolem Problem for linear recurrence sequences*, https://arxiv.org/pdf/1505.07147, Section2.4, formula(2.19); its underlying source is Matveev, *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II*, https://www.mathnet.ru/eng/im314 . The original English PDF resource opened once, but its subsequent positioned text fetches timed out; this note attributes the usable complex-logarithm statement to Sha, rather than claiming that unavailable original pages were read. Sha's simple-recurrence theorem is not invoked.

Let the actual old reduced center be

    c=A/(2^tau B),  A odd, B odd, gcd(A,2^tau B)=1,
    B=5^b B0, 5 not dividing B0.

For odd r>=1 with5 not dividing r put d=r+1 and

    Y=Im[(4+4r−i(2+r))(2+i)^d],
    eta=Y/(2^tau5^d).

The complete correction is c_k=c−k eta, so the SIGNED COMPLETE residual is

    E_k=e+pi−c_k=E_old+k eta.                      (1)

Y includes H and H′ at both conjugate endpoints. The selector's exact Gaussian arithmetic gives Y odd and5 not dividing Y. Its general rational scalar exponent is

    j_scale=2d−3−tau,
    H=U k2^(j_scale) Q(w)^(-r), Q=2w²−10w+13,     (2)

where j_scale may be negative. That dyadic rational coefficient denominator is retained; no integral-coefficient premise is introduced.

For L=lcm(B,5^d), the actual primitive denominator remains

    q_k=2^tau L/gcd(2^tau L,A L/B−kY L/5^d).      (3)

Full dyadic cancellation fixes one odd class

    k=k0+2^tau m, m integer.                      (4)

Choose its centered representative |k0|<=2^(tau−1). The parameter m below is independent of j_scale in(2).

## 2. A phase lower bound for the COMPLETE endpoint integer

There is an absolute effective constant C such that, for all permitted r,

    (sqrt(17r²+36r+20)/4)·5^(d/2)
       ·exp[−C(1+log(r+2))²]
      <= |Y| <= sqrt(17r²+36r+20)·5^(d/2).        (5)

In particular

    log|Y|=(d/2)log5+O((log d)²),
    log(|Y|/5^d)=−(d/2)log5+O((log d)²).          (6)

The constant is deliberately not optimized. The conclusion is an asymptotic phase bound, not an effective small-index numerical enclosure.

Proof. Put Z=4+4r−i(r+2), z=2+i, W=Zz^d. Then

    |Z|²=17r²+36r+20,
    xi=Z/conjugate(Z), zeta=z/conjugate(z)=(3+4i)/5,
    xi zeta^d−1=2iY/conjugate(W).                (7)

Y's attributed5-unit property implies the left side is nonzero. All algebraic numbers in(7) belong to Q(i), whose degree is2. Their logarithmic heights satisfy

    h(zeta)=log5/2,
    h(xi)<=2h(Z)=log(17r²+36r+20).               (8)

Take principal logarithms and an integer a such that

    Lambda=log(xi)+d log(zeta)+2a log(−1)

is the principal logarithm of xi zeta^d. The branch correction has |2a|<=d+2. Since Y is nonzero, Lambda is nonzero. The fixed degree-three-logarithm bound of Sha(2.19), with logarithmic sizes O(log(r+2)), O(1), O(1) and coefficient height O(d), gives

    |Lambda|>=exp[−C(1+log(r+2))²].              (9)

If |xi zeta^d−1|<=1/2, the elementary bound |log(1+u)|<=2|u| and(7) give the lower inequality(5). If its modulus exceeds1/2, (7) gives the stronger bound |Y|>|Z|5^(d/2)/4 directly. The upper inequality is the modulus of W. This proves(5)–(6). The input logarithmic-form theorem is classical; only its present endpoint application is asserted here.

## 3. Exact real mesh without omitting the old error

Define the SIGNED quantum

    Delta=Y/5^d.

For all cancelling coefficients(4), the exact full residual is

    E_m=E_old+(k0/2^tau)Delta+m Delta.            (10)

Thus its complete mesh is Delta, with no discarded old endpoint, response U, or denominator. Formula(6) determines its exponential size even when the Gaussian phase approaches cancellation.

If d<b, the selector's full primitive arithmetic gives

    q_k=B,                                     (11)

for EVERY m. No5-unit restriction on k is needed: at5, the old numerator A is a unit and the correction numerator contains5^(b−d). Every prime of B0 also survives, as in(3). Hence all centers in(10) have the same ACTUAL q.

There is an integer m_star nearest to −E_old/Delta−k0/2^tau. It obeys

    |E_(m_star)|<=|Delta|/2,
    |k_star|<=2^tau (|E_old|/|Delta|+1/2).        (12)

This is an existence/rounding statement involving the actual complete E_old. It is not a cancellation deduced from the known rational dyadic congruence. The signed expression(10) remains essential.

The two consecutive m values bracketing zero have errors of opposite weak sign and absolute errors summing to |Delta|. Their farther node therefore satisfies

    |E_far|>=|Delta|/2,
    q_far|E_far|>=B0·5^(b−d)|Y|/2.              (13)

For d tending to infinity the right side grows at least like exp[(log5/2)d−O(log²d)], even if B0=1 and b−d remains bounded. On any given cell only one point can have error o(|Delta|). **There is no lower bound here for the nearer node.** It may have an exceptional much smaller residual or an exact equality. A mesh argument cannot exclude that event.

If d>b, requiring5 not dividing k to retain the simple untied denominator removes one m class modulo5. Consecutive surviving m values have gaps at most2, so a surviving rounding node has |E_m|<=|Delta| and

    q_k=B0·5^d,
    q_k|Delta|=B0|Y|.                           (14)

The tied case d=b remains exactly(3); its additional content is not discarded. No uniform primitive q lower bound is asserted there without resolving that content.

## 4. Full height needed to tune a nonexceptional old residual

If a cancelling coefficient achieves |E_k|<=|Delta|/2, the triangle inequality in(1) gives

    |k|>=2^tau(|E_old|/|Delta|−1/2).              (15)

When |E_old|>=|Delta|, combining(12),(15) gives |k| comparable, within absolute constants, to2^tau |E_old|/|Delta|. More generally, if log|E_old|=o(d) and the old error is nonzero, then(6) yields

    log|k|=tau log2+(d/2)log5+o(d),             (16)

for a rounding coefficient. This premise includes polynomially large or small old errors, but not unproved lower bounds for the actual nearest critical node.

The scalar in the rational kernel(2) therefore has

    log|U k2^(j_scale)|
       =log|U|+(2d−3)log2+(d/2)log5+o(d),       (17)

under that same premise. The explicit coefficient denominator when j_scale<0 is still the reduced dyadic denominator of U k2^(j_scale); since every cancelling k is odd, its exponent is

    max(0,tau−2d+3−v2(U)).                     (18)

Thus moving far along the class to cancel a polynomial residual incurs an additional exponential factor5^(d/2) in coefficient size. It is not obtained by taking the bounded representative that only removes2^tau.

For the reflected power-two inverse-critical subsequence, tau=N, v2(U)=1, and the selector can choose permitted even d=N/4−O(log N)<b using the arithmetic agent's actual b>=v5(N!). Then

    |Delta|=exp[−(log5/8)N+O(log²N)],
    q_k=B=q_old/2^N,
    q_k|Delta|=B0·5^(b−d)|Y|
          >=exp[(log5/8)N−O(log²N)].            (19)

The bounded representative has exponentially small shift and preserves the proved full O(N^(−1/4)) convergence. The real-rounding representative yields the stronger COMPLETE upper bound(12), while its height is(15)–(18). Its available mesh upper bound, even with the strong denominator reduction, does not make the primitive residual tend to zero. Equation(19) is a width statement and the farther-node lower bound(13); it is explicitly **not** a lower bound for the selected nearest residual.

## 5. Scope of the new result

The new conclusions are the full correction phase estimate, the exact complete-error mesh at actual constant q in the d<b regime, and the height and primitive-width comparison. They clarify two separate coefficient choices: bounded representatives preserve convergence while reducing q; much larger representatives can round the residual on an exponentially finer real mesh. Neither argument supplies a nonzero primitive residual tending to zero. Ordinary rounding to this one-dimensional mesh is not counted as a solution of the main e+pi problem, and no rationality statement follows.
