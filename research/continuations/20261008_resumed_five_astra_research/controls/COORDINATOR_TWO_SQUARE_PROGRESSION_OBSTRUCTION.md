> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A paid whole-error obstruction on one infinite two-square progression

Coordinator derivation,8 October2026. Locally proved, pending independent
external audit of this argument and the last-prime-block theorem it uses.
This does not decide e+pi. It concerns only the new two-square family at
N=1 modulo255255, not every subsequence and not the compact/ternary producers.

## Scoped overlap and classical ingredients

The scoped archive/current-report search for this progression and a
two-square Legendre no-go found no exact earlier result. An unrelated
direct-integral denominator15015 was found and is not this construction.
The classical Legendre evaluation-kernel argument WAS already used in
20261007 A4turn20, Section9.2, and reused in20261008 A5turn0.
Its exact orthogonality/norm and integral normalization are reused.
The new complex-evaluation specialization is proved explicitly below.
An attempted fresh opening of DLMF18.10/18.3 failed due to connection errors;
it is not counted as a fresh reading. The explicit earlier proof and the
coefficient derivation below are the actual basis. No novelty is claimed
for Legendre kernels or factorial valuations. The new statement combines
them with the paid primitive-denominator theorem in the preceding note.

## 1. Original family and what is retained

Retain the source-normalized positive polynomial

    P_N=f_N^2+(1-tau_N)*g_N^2/T_N,
    f_N=Phi_N/Delta_N, f_N(i)=1, deg f_N<=N,
    g_N=(1+t^2)(1-t)^(N-2),
    T_N=(2N-4)!*R4(2N-4),
    R4(x)=x^4+6x^3+19x^2+22x+12.

The accepted source identity gives the actual reduced p_N/q_N and

    epsilon_N=(e+pi)-p_N/q_N
             =int_0^1 P_N(t)[e^t+4/(1+t^2)]dt>0.

Write J_N=int_0^1 P_N. The retained positive second square implies
J_N>=int f_N^2, and the complete weight implies epsilon_N>=3J_N.
The actual q_N includes polynomial content h, the LEAST affine clearer,
and the FINAL ALL-prime gcd. No replacement polynomial denominator is used.

## 2. Lower bound for the ordinary error at the complex normalization

Let L_j(t)=P_j(2t-1), where P_j is the ordinary Legendre polynomial.
Rodrigues' formula and j integrations by parts give

    int_0^1 L_j L_r=0 for r<j,
    int_0^1 L_j^2=1/(2j+1).

The boundary terms vanish because t^j(t-1)^j has j-fold zeros at
both endpoints. The second identity follows from its leading coefficient
binom(2j,j) and Beta(j+1,j+1)=j!^2/(2j+1)!.

The explicit finite expansion is

    L_j(t)=sum_(r=0)^j(-1)^(j+r)binom(j,r)binom(j+r,r)t^r.

Since |i|=1, the triangle inequality gives

    |L_j(i)|<=sum_(r=0)^j binom(j,r)binom(j+r,r)=P_j(3).

The last equality is evaluation at t=-1 followed by Legendre parity.
The already accepted normalized integral representation at3 gives

    0<P_j(3)<= (3+2sqrt2)^j <6^j for j>0,
    P_0(3)=1.

Expanding any REAL polynomial f of degree<=N in the L_j basis and
applying complex Cauchy--Schwarz proves

    |f(i)|^2 <= (int_0^1 f^2)*K_N(i,-i),
    K_N(i,-i)=sum_(j=0)^N(2j+1)|L_j(i)|^2
             <=(N+1)^2*36^N.

For the ACTUAL real rational f_N(i)=1, this gives the required lower bound

    J_N >= 1/[(N+1)^2*36^N].                         (1)

This is a lower bound, unlike the earlier root-exponential upper estimate.
No upper-bound comparison is used to claim failure.

## 3. Actual surviving prime powers on the progression

Let S={3,5,7,11,13,17} and M=product S=255255. The preceding
last-prime-block note proves, for N>=4 and each odd p|N-1,

    v_p(q_N)=v_p(T_N)+v_p(N-1).                       (2)

Its proof retains both arctan squares, the negative beta pole of the
second square, the least affine denominator and the final gcd. Formula(2)
is not an estimate for an unreduced polynomial content.

For N=1 modulo M, all p in S qualify. Put m=2N-4 and
C=sum_(p in S) log(p)/(p-1). The factorial identity

    v_p(m!)=(m-s_p(m))/(p-1)

and the digit bound s_p(m)<=(p-1)(floor(log_p m)+1) imply

    v_p(T_N)+v_p(N-1)
       >= m/(p-1)-floor(log_p m).

Here R4(m) is a positive integer, so its valuation is nonnegative,
and v_p(N-1)>=1 pays the last digit-bound constant. Consequently

    q_N >= exp(m*C)/m^6.                             (3)

No upper bound on q_N is assumed, and no other prime is removed from it.

## 4. A fully exact constant and a divergent whole-error bound

The fixed certificate two_square_progression_constant_certificate.json
checks the INTEGER inequality

    2^240 * 3^120 * 5^60 * 7^40 * 11^24 * 13^20 * 17^15
        > 13^240.

Each exponent equals240/(p-1). Thus exp(C)>13/2>6 without a
floating-point logarithm decision. The parent-authored bounded code ran
inside the key/network-denying math sandbox and computes no original
large index. The certificate includes the positive integer difference
and the exact source hash.

Combining(1)--(3) with epsilon_N>=3J_N yields the actual whole-error bound

    q_N*epsilon_N
      > (48/28561)*(13/12)^(2N)/[(2N-4)^6*(N+1)^2],
    N>=4, N=1 modulo255255.                          (4)

The right side tends to positive infinity along this infinite progression.
Therefore the complete sequence of this PARTICULAR two-square ansatz
cannot satisfy q_N*epsilon_N->0 across all N. The progression itself cannot
provide the required irrationality approximants. This does not exclude
other N subsequences, other positive polynomials in the established source
plane, or the compact/ternary routes.

The progression bound is a mathematical obstruction within a candidate
construction, not a theorem that e+pi is rational. No global decision,
growing favorable gcd estimate or stopping condition is claimed.
