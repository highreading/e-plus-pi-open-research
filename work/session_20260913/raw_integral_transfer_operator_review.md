> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the integral transfer and norm criterion

Date: 2026-09-13. Reviewer: audit_sources. Scope: Sections 3–6 of
`raw_hp_integral_transfer_operator.md`, with the notation and exact
primitive identity in Sections 1–2 checked as dependencies. No extra
degree or prime sample was generated for this review.

## 1. Full operator and cancellation: pass

After differentiating the primitive identity twice, the three groups
are a_d J^(4-d), b_d J^(5-d)(n-theta), and
c_d J^(6-d)(n-theta)_2. The exceptional first-derivative terms are
a_5 P'+b_6 partial(n-theta)P. Using a_5=-n gamma and b_6=gamma,
they give -gamma(P'+tP''). The c_6 term contributes

    gamma[t^2P''-2(n-1)tP'+n(n-1)P].

Their sum has the asserted leading second-order and first-order
coefficients. The b_5 and c_5 terms add -beta tP' and delta t^2P',
respectively.

For a fixed J^kP, ordinary terms contribute a_(4-k), the first-order
group contributes (n+k)b_(5-k)-t b_(4-k), and the second-order group
contributes

    (n+k)(n+k-1)c_(6-k)
      -2(n+k)t c_(5-k)+t^2c_(4-k).

This independently reconstructs the complete V_k formula, including
its shifts and signs. The actual origin-raising condition forces
c_0=N_2(0)=0, since its potential leading term cannot cancel against
the other two numerator terms. Thus V_6 is zero.

All three infinity conditions give beta=delta-2n gamma. Substitution
leaves exactly the shifted Legendre operator plus
delta t(t-1)partial; there is no remaining unweighted t partial term.
Furthermore

    V_0=W_0+n delta(1-2t)-n(n+1)gamma,

which verifies the alternative arrangement (11). The integration
identities include their endpoint terms correctly: the t and t^2
boundary factors vanish at zero, and the primitive equation has both
of its required zero constants.

## 2. Real and complex Volterra inverse: pass

Factoring Q gives the exact product of three commuting operators
(I-alpha J). Formula (13) is its individual resolvent kernel. The
kernel is integrable on the finite triangle for every fixed complex
alpha, so the Volterra series or direct substitution proves the
inverse on L2 without a root-separation assumption.

Young's inequality gives (14). For real nonpositive alpha, the
displayed accretivity identity is valid also for complex-valued input:
Re <g,Jg>=|integral g|^2/2. The inverse therefore has norm at most one.
For real positive alpha, the Young bound equals exp(alpha). The fixed
left-sector criterion follows from

    |alpha| integral_0^1 exp(Re(alpha)s) ds <= K.

Products of these bounds remain valid at repeated roots and when a
root equals one; neither a simple-root hypothesis nor Q(1)!=0 enters.

## 3. Weighted spectral estimate and optimized shift: pass

On polynomials of degree at most n, the shifted Legendre operator has
spectrum k(k+1), 0<=k<=n. The integration-by-parts identity gives

    ||t(t-1)P'||_2^2
       <= (1/4) integral_0^1 t(1-t)|P'|^2
       <= n(n+1)||P||_2^2/4.

Also ||J^k||<=1/k! by the L1 norm of its convolution kernel. These
give (18) exactly.

For the optimized shift, let [a,b] be the interval between 0 and
bar gamma n(n+1), and let [m,M] be the range of bar V_0. The two
triangle-bound terms are

    (b-a)/2 + |lambda-(a+b)/2|,
    (M-m)/2 + |lambda+(m+M)/2|.

Their minimum sum is

    (b-a+M-m)/2 + |(a+b+m+M)/2|
       = max(|a+m|,|b+M|),

which is precisely G_n in (19). Multiplication by V_0 need not
preserve the degree-n polynomial space or commute with the Legendre
operator: the proof is an operator triangle bound in L2 and makes
neither assumption.

The sufficient criterion (20), its easier componentwise conditions
(22), and iteration to ||P_n||_2<=n! exp(O(n)) therefore follow. The
normalization by Q_3 is consistent throughout.

## 4. Scope of acceptance

No correction to Sections 3–6 is needed. This review verifies the
identities and conditional inequalities; it does not establish any
uniform root condition, any of the required normalized coefficient
bounds, eventual cubic degree, the cancellation ratio in the full
remainder, or the primitive endpoint denominator. The passage from
these explicit sufficient conditions to an actual all-index bound
remains a separate mathematical problem.
