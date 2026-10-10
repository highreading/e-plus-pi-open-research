> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Maximal-order inverse-Apéry kernel: forced endpoint content and primitive gateway

Date: 2026-10-02. Status: new author derivation; main rationality problem open.

## Novelty gate and precise scope

The archive's `sources/item387_mixed_kernel_quotient_and_claim_audit_report.md` already proves that the unrestricted mixed kernel is the whole integer approximation lattice. That bare identity is not new. Archive searches for the maximal Taylor-zero constraint, structured restart, and the forced endpoint factorial content did not find a completed result. The July2026 primary paper *An Inverse Apéry Audit for e+pi: Positivity–Smallness Separation* imposes Taylor conditions in its finite Hermite–Padé restart, but its finite positivity/smallness observations do not supply the all-degree arithmetic theorem below. Primary PDF read through its exact conditions (11):
https://ir-api.ua.edu/api/core/bitstreams/[session identifier removed]/content
Repository metadata:
https://ir.ua.edu/items/[session identifier removed]/full

No unrestricted kernel-lattice search or historical claimed-proof audit is replayed. This target fixes the maximal Taylor-order ray and retains its actual endpoint gcd.

## Exact one-dimensional family

Let n>=2, R(x)=sum_{k=0}^n r_k x^k, A=R(1), C=R(0), and

K_R(x)=(R+R')exp(x)+4A/(1+x^2).

Require K_R=O(x^n). Put

u_k = [d^k/dx^k](4 exp(-x) atan x)|_{x=0},
v_k=(-1)^k u_k,
f_k=[d^k/dx^k](exp(-x)/(1+x^2))|_{x=0}.

All these are integers. Their exact recurrences are

f_0=1, f_1=-1,
f_k+k(k-1)f_{k-2}=(-1)^k,
u_0=0, u_{k+1}+u_k=4f_k.

Solving the differential equation through degree n gives

r_k=(-1)^k(C-A v_k)/k!,  0<=k<=n.                 (1)

Define

E_n=sum_{k=0}^n (-1)^k/k!,
V_n=sum_{k=0}^n u_k/k!,
D_n=n! E_n,
B_n=n!(1+V_n).

Here D_n is the derangement number, positive for n>=2. The endpoint condition is exactly

C/A=(1+V_n)/E_n=B_n/D_n.                          (2)

A=0 forces C=0 and R=0. Thus there is a unique nonzero rational ray. Write g_n=gcd(D_n,B_n), a_n=D_n/g_n, c_n=B_n/g_n. The actual primitive endpoint denominator is exactly

q_n=a_n=D_n/gcd(D_n,B_n).                        (3)

This formula is kept without replacing it by a raw coefficient clearer.

## Forced raw factor and stronger endpoint-content theorem

For any integer-coefficient member of this ray, (1) implies both k! divides C-A v_k and (k+1)! divides C-A v_{k+1}. Subtraction yields

k! divides 4A f_k,  1<=k<=n-1.                  (4)

For a prime p<=n-1 choose k=p floor((n-1)/p). Since p divides k, the f recurrence gives f_k=(-1)^k mod p. Also vp(k!)=vp((n-1)!), because there is no further multiple of p before n-1. Therefore

(n-1)! divides 4A.                              (5)

The stronger statement concerns the content removed by the FINAL endpoint reduction. Let h=gcd(A,C), and A=h a, C=h c with gcd(a,c)=1. For p not dividing a, repeat (4) to get vp(h)>=vp((n-1)!)-vp(4). For p dividing a, c-a v_n is a p-unit; the integrality of r_n gives vp(h)>=vp(n!). Hence

(n-1)! divides 4 gcd(A,C).                      (6)

In particular a huge factorial is already FORCED into the endpoint gcd. Raw A-growth cannot be interpreted as primitive denominator growth.

For the primitive integer-coefficient member, h is precisely the minimum clearer of the rational polynomial with endpoint pair (a_n,c_n). Formula (1) shows all its coefficient denominators divide n!, so

h divides n!,       (n-1)! divides 4h.          (7)

Consequently this coefficient-to-endpoint reduction removes a factor between (n-1)!/4 and n!, up to the integral interpretation of the lower bound. The integer polynomial can be enormous even when its primitive endpoint pair is small.

## Complete normalized error

Let S=e+pi. Since E_n tends to exp(-1) and V_n tends to pi/e,

c_n/a_n-S=(1+V_n-S E_n)/E_n.                     (8)

The exponential truncation term is factorially small. For the other tail, use L_z(x)=-log(1-zx), so

4 exp(-x) atan x=(2/i)exp(-x)(L_i(x)-L_{-i}(x)).

The exact tail of L_z at1 after degree m is

z^(m+1) integral_0^1 t^m/(1-z t) dt.

At z=+/-i this is z^(m+1)/[(m+1)(1-z)]+O((m+1)^(-2)), by one integration by parts with bounded derivative. Convolution with exp(-x), splitting its index j at n/2, gives the uniform four-parity expansion

c_n/a_n-S = -4e/(n+1) Im[e^i i^(n+1)/(1-i)] + O(n^(-2)).   (9)

All four leading constants are nonzero: their magnitudes are 2e(sin1-cos1) and 2e(sin1+cos1). Since pi/4<1<pi/2, both are positive. Thus the full normalized error has order1/n in every parity, and the actual primitive linear form has size comparable to q_n/n.

Therefore an irrationality proof from this PARTICULAR ray would need

q_n=o(n), equivalently gcd(D_n,B_n) >> D_n/n,

on an infinite selected subsequence. An exclusion would need a suitable opposite lower bound. Neither is established here. The apparent factorial raw growth cancels and does not decide this condition.

## Independent new exact arithmetic receipt

`inverse_apery_maximal_order.py` derives the new ray directly and checks n=2..100 using rational arithmetic. It verifies all n Taylor-zero equations, primitive coefficient content, endpoint relation, formula(3), and both divisibilities in(7). It does not replay inherited finite-search candidates or use floating-point sign decisions. The receipt is `INVERSE_APERY_MAXIMAL_ORDER_CERTIFICATE.json`.

Examples (n, primitive coefficient A, endpoint h, actual q):
(4,27,3,9), (6,7950,30,265), (8,1437660,1260,1141),
(10,121107661920,90720,1334961).

The finite values are diagnostic evidence for arithmetic identities, not a uniform gcd theorem.
