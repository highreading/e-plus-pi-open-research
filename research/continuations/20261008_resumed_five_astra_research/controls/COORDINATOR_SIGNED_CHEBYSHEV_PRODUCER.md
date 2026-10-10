> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A distinct signed-source Chebyshev producer inside the established source plane

Coordinator proposal and derivation,8 October2026. Independent review is
required. This is a NEW explicitly defined ansatz, not a replacement of any
old matrix during its proof. It does not establish primitive-error decay.
All finite checks remain auxiliary; no global e+pi decision is claimed.

## Scoped archive/literature gate and reused barriers

The complete archive notes common_kernel_positive_cone_endpoint_bootstrap_barrier,
fixed_target_positive_common_kernel_primitive_gap and
growing_target_positive_two_place_synchronization_barrier were read.
Section11.3 of common_kernel_two_form_quotient_audit was read explicitly.
The full Stein--Robin source plane was already read and accepted.
These sources ALREADY explain that t(1-t)-weighted squares have a signed
source moment and that interval positivity alone does not imply source
positivity. That insight and Markov--Lukacs are reused, not rediscovered.
They also retain the fixed-target and synchronized ALL-prime output-gcd
barriers, which this proposal does not bypass by assertion.

Scoped searches in archive/20261007 Markdown for Chebyshev source-correction,
signed two-square and the exact normalization found no already evaluated
version of this specific producer. Primary arXiv e+pi/Chebyshev searches
returned the already read Yu2606.17303 and unrelated hits. No exhaustive
absence claim is made. DLMF18.5's classical Chebyshev representation is
reused. The primary Powers--Reznick2000 abstract was identified as general
interval-positivity background, not read as a proof of our arithmetic.
Our positivity follows directly from the displayed factors and requires
no general real SOS representation or its denominator assumptions.

## 1. Explicit two-column Chebyshev evaluation

For N>=3 put C_j(t)=T_j(2t-1), with the exact integral recurrence
C_0=1,C_1=2t-1,C_(j+1)=2(2t-1)C_j-C_(j-1).
Write C_j(i)=a_j+i b_j, a_j,b_j integers, and define

    d_N=a_N*b_(N-1)-a_(N-1)*b_N,
    B_N=b_(N-1)*C_N-b_N*C_(N-1),
    f_N=B_N/d_N.

The determinant never vanishes. At z=2i-1, the recurrence yields

    Im(C_(j+1)(i)*conjugate(C_j(i)))
      =4*|C_j(i)|^2+Im(C_j(i)*conjugate(C_(j-1)(i))).

The initial imaginary part is2. Therefore

    d_N=-2-4*sum_(j=1)^(N-1)(a_j^2+b_j^2)<0.             (1)

Exactly B_N(i)=d_N and f_N(i)=1, and conjugation gives the same
real value at-i. Since both b_N and b_(N-1) cannot be zero, B_N
has degree N or N-1. No numerical phase nonresonance is assumed.

## 2. A signed source correction, compactly nonnegative

Let eta(P)=int_(-infinity)^1 e^(t-1)P(t)dt, whose integer moments
are eta(t^j)=(-1)^j*derangement(j). Set

    K_N(t)=t(1-t)(1+t^2)^2*C_(N-3)(t)^2,
    U_N=-eta(K_N), I_N=eta(B_N^2).

K_N is nonnegative on[0,1], vanishes at i,-i, has degree2N,
and is negative for t<0 away from its finite zeros. In fact U_N>0
for all N>=3. On[0,1], K_N<=1, so its positive eta contribution
is at most1. On[-3,-2], |K_N|>=150 and |C_(N-3)|>=1;
its negative contribution is at least150*e^(-4)>150/81>1.
The remaining negative half-line only increases U_N. This proves
the sign without cancelling an unbounded integral informally.

Whenever I_N>d_N^2, define

    kappa_N=(I_N-d_N^2)/(U_N*d_N^2)>0,
    P_N=f_N^2+kappa_N*K_N.                             (2)

Then P_N is nonnegative on[0,1], is not identically zero, and

    eta(P_N)=1, P_N(i)=P_N(-i)=1.                       (3)

Unlike the preceding Laguerre two-square ansatz, it need not be
nonnegative on the entire source half-line. Its f_N has a growing
source norm, so the bounded-Laguerre-norm root-lower theorem does
not apply. Changing this hypothesis is explicit and essential.

The inequality I_N>d_N^2 holds uniformly for N>=256. Indeed
|C_j(i)|<=6^j by its finite coefficient bound, hence |d_N|<=6^(2N-1).
The rational polynomial f_N has degree at least N-1 and nonzero
leading coefficient of magnitude at least1/|d_N|. The classical monic
Laguerre minimum gives

    eta(f_N^2)>=[(N-1)!]^2/d_N^2.

The fixed exact certificate checks255!>6^511. Induction preserves
(N-1)!>6^(2N-1) for N>=256 because the factorial quotient N exceeds36.
Thus (2)--(3) hold at EVERY original N=9^(18+32u), with no huge
original-index computation. Small N3..12 are separately checked only
as finite diagnostics, not as the proof of eventual positivity.

## 3. Uniform exponential ordinary-error upper bound

Let z=2i-1 and choose zeta with zeta+zeta^(-1)=2z and R=|zeta|>1.
Then C_j(i)=(zeta^j+zeta^(-j))/2. This is the established exterior
capacity R=4.61158..., used here algebraically without a numerical decision.
For N>=2, (1) gives

    |d_N|>=4|C_(N-1)(i)|^2
           >=(1-R^(-2))^2*R^(2N-2).

Consequently, with

    s_N=(|b_(N-1)|+|b_N|)/|d_N|,
    K_R=R^2*(1+R^(-2))*(1+R^(-1))/[2(1-R^(-2))^2],

one has s_N<=K_R*R^(-N), and |f_N(t)|<=s_N on[0,1].

For x>=0, the shifted Chebyshev polynomial satisfies
|C_j(-x)|=T_j(1+2x)<=(4x+2)^j. Its coefficient formula
T_j(1+2x)=sum_(r=0)^j[j/(j+r)]binom(j+r,2r)4^r x^r
has positive coefficients for j>0, and leading coefficient2^(2j-1).
The j=0 polynomial is1. Thus |f_N(-x)|<=s_N*(4x+2)^N,
and integration gives

    eta(f_N^2)<=s_N^2*[1+4^(2N)*(2N)!].

For N>=4, put c=2^(2N-7), the leading coefficient of C_(N-3).
Positivity of its coefficients at-x gives C_(N-3)(-x)^2>=c^2*x^(2N-6).
Since |K_N(-x)|>=c^2*x^(2N),

    U_N>=e^(-1)*c^2*(2N)!-1
        >=(1/4)*c^2*(2N)!.

The last inequality follows from e<3 and c^2*(2N)!>12 for N>=4.
It follows that kappa_N<=2^17*s_N^2. Therefore

    0<=P_N(t)<=(1+2^17)*K_R^2*R^(-2N), t in[0,1],
    0<epsilon_N:=int_0^1 P_N(t)[e^t+4/(1+t^2)]dt
      <=7*(1+2^17)*K_R^2*R^(-2N), N>=256.               (4)

This is an explicit SAME-index exponential ordinary approximation.
It is not a primitive whole-error estimate. The preceding odd-prime
formula cannot be imported: its special source T=(2N-4)!R4 was replaced
by the fully evaluated signed U_N in this new producer.

## 4. Actual integer producer and complete primitive arithmetic

Define the integer raw pair

    Wraw=U_N*B_N^2+(I_N-d_N^2)*K_N,
    Z=U_N*d_N^2.

Then eta(Wraw)=Z and Wraw(i)=Wraw(-i)=Z exactly. Let
h=cont(Wraw)>0, Wprim=Wraw/h and M=Z/h. The integer source identity
proves h|Z. Monic division gives

    S=(Wprim-M)/(1+t^2) in Z[t], deg S<=2N-2.

Let E=sum_j w_j*(-1)^j*j! be the complete exponential endpoint.
Reduce the COMPLETE rational number4*int S to b/lambda, gcd(b,lambda)=1,
lambda>0. Thus lambda is the ACTUAL least affine denominator and

    A=lambda*E-b, gcd(A,lambda)=1,
    G=gcd(lambda*M,A)=gcd(M,A),
    q=lambda*M/G, p=A/G,
    q*(e+pi)-p=q*epsilon_N>0.                            (5)

Every coefficient content and final gcd is retained. Rational f_N(i)=1
is not an integer fixed-target family: Wprim's integer target M grows.
The archive fixed-target theorem and synchronization barriers remain
applicable at their exact hypotheses and are not contradicted by (4).

The crude paid height remains log q<=2N log N+O(N): the integral
coefficient norm of K is at most8*36^(N-3), so U<=8*36^(N-3)*(2N)!;
|d|<=6^(2N-1); and lambda divides lcm(1,...,2N-1). The classical
Chebyshev bound for that lcm, already in the archive, is exponential
in N. These estimates include all payments and discard h,G only
for an UPPER bound. They do not prove the desired q=o(R^(2N)).

## 5. New finite diagnostic and unresolved decisive issue

The parent-authored signed_chebyshev_normalization_diagnostic.py ran
inside the key/network-denying sandbox for ONLY N3..12, degree<=24.
It checks exact source/complex normalization, actual coefficient content
with Bezout witness, monic quotient, LEAST aggregate affine clearer,
FINAL gcd with Bezout witness, coprime p/q and positive rational J.
All passed. No old Laguerre N8 certificate was recomputed or changed.

These finite whole errors are large; the diagnostic provides no evidence
of primitive decay. In this range q has no factor2 and has small5-adic
depth, illustrating that the old producer's prime formula does not
transfer. This is finite scope only. The uniform task is now the
actual h/lambda/G arithmetic of this explicit signed producer, followed
by nonzero whole-error comparison at the original infinite indices.
Neither (4), real positivity, nor a generic source-plane representation
solves that task or decides the rationality of e+pi.
