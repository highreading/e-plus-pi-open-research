> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact ternary depth of the actual degree-one endpoint denominator

Date: 2026-09-27. Author: audit_computations.
Status: FULL PASS in `hp_b1_ternary_actual_denominator_independent_review.md`
(audit_sources), including the general odd-prime gate and unchanged frozen
n=2,8 checker. No correction requested.

This continues the independently passed
`../session_20260913/hp_b1_adjacent_scalar_valuation_gate.md` and its
`hp_b1_adjacent_scalar_independent_review.md`. The closing register and
the project inventory contain no later result resolving this numerator.
The proof below concerns the **reduced endpoint denominator**, not a
coefficient clearer or the unreduced matched endpoint.

## 1. The actual endpoint and the theorem

Retain the degree-(n,1,n) family for exp(z) and
4 arctan(z/(2-z)), with matched exponential/arctangent endpoints.
Let X/Y be its rational A(1)/B(1) representative from the cited note,
and let q_n be its positive reduced denominator. Write



$$
L_k(t)=2^k i^k\operatorname{Leg}_k(-i(2t-1)),\qquad P_k=L_k(1),
$$




$$
Q_k=8\sum_{j=1}^k P_{j-1}P_{k-j}/j,
 \qquad T_k=\sum_j[t^j]L_k(t)E_{n+j},
 \quad E_d=\sum_{r=0}^d1/r!,\quad S_k=Q_k+T_k.
$$


The fixed n in T_k applies to both k=n and k=n+1. Also set



$$
H_k(x)=k![z^k]e^{xz}(1-z+z^2/2)^k,\quad H_k=H_k(1),
 \quad K_k=H_k+H'_k(1)/k\in\mathbb Z,
$$




$$
\Delta_n=(n+1)P_{n+1}H_n-2P_nK_{n+1}.
$$


The exact already reviewed endpoint formula is



$$
\frac XY=\frac{2K_{n+1}S_n-(n+1)H_nS_{n+1}}{\Delta_n}.
 \tag{1}
$$



**Theorem.** For every integer n>=5 with n=2 modulo 3,



$$
\boxed{v_3(q_n)=2v_3(n!).}                                      \tag{2}
$$



No parity assumption is needed. In particular this holds on every even
n=2 modulo 3 except the already known n=2 exception. The endpoint
denominator in (1) is nonzero throughout this residue class, because
Delta_n is a 3-adic unit. The theorem determines the full numerator
cancellation at this prime.

## 2. Rodrigues normalization removes the unnecessarily large factorial

Define dyadically integral coefficients and integer exponential sums



$$
a_s(k)=[x^s](1-x+x^2/2)^k\in\mathbb Z[1/2],\qquad
 D_d=d!E_d\in\mathbb Z\quad(d\ge0).
$$


The exact Rodrigues identity in this normalization is



$$
L_k(t)=\frac{2^k}{k!}\frac{d^k}{dt^k}(t^2-t+1/2)^k.
 \tag{3}
$$


If (n)_s is the falling factorial, define



$$
\mathscr A_n=\sum_{s=0}^n(n)_s a_s(n)D_{2n-s},
 \tag{4}
$$




$$
\mathscr B_n=2D_{2n+1}
 +\sum_{s=1}^{n+1}(n)_{s-1}(2n+2-s)a_s(n+1)D_{2n+1-s}.
 \tag{5}
$$


Both belong to Z[1/2]. Direct coefficient substitution in (3) gives



$$
\boxed{T_n=\frac{2^n}{(n!)^2}\mathscr A_n,\qquad
 T_{n+1}=\frac{2^{n+1}}{(n+1)(n!)^2}\mathscr B_n.}       \tag{6}
$$



Here are the factorial details. If c_r=[t^r](t^2-t+1/2)^k, then
[t^j]L_k=2^k c_{k+j}(k+j)!/(k!j!). For k=n, multiplication
by E_{n+j} gives D_{n+j}; use j=n-s and
c_{2n-s}=a_s(n). For k=n+1, the extra factorial ratio is
(n+1+j)!/(n+j)!=n+1+j. At s=0 the factor
n!/(n+1)! times (2n+2) is exactly 2; for s>=1 it is
(n)_{s-1}(2n+2-s). This proves both formulas without dividing by
n+1 in a local integer ring.

The same computation with D_d replaced by 1 proves



$$
H_n=\sum_{s=0}^n(n)_s a_s(n),
$$




$$
K_{n+1}=2+
 \sum_{s=1}^{n+1}(n)_{s-1}(2n+2-s)a_s(n+1).
 \tag{7}
$$


Alternatively, (7) follows from the exact factorial contractions in the
previous note. It supplies an independent local integrality proof for
the expressions used here.

Put



$$
\mathscr C_n=K_{n+1}\mathscr A_n-H_n\mathscr B_n,
\qquad \mathscr Q_n=2K_{n+1}Q_n-(n+1)H_nQ_{n+1}.
$$


Then the actual numerator of (1) is exactly



$$
\boxed{\mathscr Q_n+\frac{2^{n+1}}{(n!)^2}\mathscr C_n.} \tag{8}
$$


This is an equality of rational numbers before endpoint reduction.

## 3. The surviving ternary terms are a unit

The integer sequence D_d satisfies
D_0=1 and D_d=dD_{d-1}+1. Consequently



$$
(D_{3r},D_{3r+1},D_{3r+2})=(1,2,2)\pmod3
 \quad(r\ge0).                                             \tag{9}
$$


Now let n=2 modulo 3. In (4) and the first formula of (7), every
s>=3 term vanishes modulo 3: (n)_s contains a multiple of 3 and
a_s(n) is 3-integral. The coefficients for s=0,1,2 are



$$
(n)_s a_s(n)=(1,2,1)\pmod3.
 \tag{10}
$$


Indeed a_0=1, a_1=-n=1, and
a_2=binom(n,2)+n/2=n^2/2=2 modulo 3.
Since 2n=1 modulo 3, equations (9)-(10) give



$$
H_n=1+2+1=1\pmod3,\qquad
 \mathscr A_n=1\cdot2+2\cdot1+1\cdot2=0\pmod3.
 \tag{11}
$$



For (5), a_s(n+1)=0 modulo 3 when s=1,2, since
(1-x+x^2/2)^{n+1} is a polynomial in x^3 modulo 3.
The s=3 multiplier 2n+2-s is divisible by 3. Every s>=4
term contains (n)_{s-1}, which is also divisible by 3.
Only the displayed s=0 term remains. Equations (5),(7),(9) yield



$$
\mathscr B_n=2D_{2n+1}=1\pmod3,\qquad K_{n+1}=2\pmod3.
 \tag{12}
$$


In particular



$$
\boxed{\mathscr C_n=2\pmod3.}                         \tag{13}
$$



These are all-index congruences obtained by discarding terms with proved
valuation. They are not inferred from a list of canonical degrees.

## 4. The second-kind part cannot cancel this unit

The exact convolution for Q_k shows



$$
v_3(Q_k)\ge-\lfloor\log_3 k\rfloor\quad(k\ge1).
$$


Thus



$$
v_3(\mathscr Q_n)\ge-\lfloor\log_3(n+1)\rfloor.
 \tag{14}
$$


For every n>=5 with n=2 modulo 3,



$$
2v_3(n!)>\lfloor\log_3(n+1)\rfloor.                   \tag{15}
$$


An elementary verification of the inequality is as follows. For n=5,
its two sides are 2 and 1. If n>=8, put a=floor(log_3(n+1))>=2.
When a=2, floor(n/3)>=2, so 2v_3(n!)>=4>2.
When a>=3, n>=3^a-1, whence
2v_3(n!)>=2floor(n/3)>=2(3^{a-1}-1)>a.

Multiply (8) by (n!)^2/2^{n+1}. By (14)-(15), its Q part
is divisible by 3 in Z_(3), while (13) is a unit. Hence



$$
v_3\bigl(2K_{n+1}S_n-(n+1)H_nS_{n+1}\bigr)
       =-2v_3(n!).                                      \tag{16}
$$


Finally the Legendre generating function gives P_j a 3-adic unit for
every j: its Frobenius digit factor is 1-t-t^2, with no zero digit
coefficient. Thus Delta_n=-4P_n modulo 3 is a unit for n=2 modulo 3.
Combining (1),(16) proves (2), with the reduced endpoint gcd included.

In the old integer clearing convention M=(2n+1)! and
N_n=M[2K_{n+1}S_n-(n+1)H_nS_{n+1}], the equivalent exact statement is



$$
\boxed{v_3(N_n)=v_3((2n+1)!)-2v_3(n!)\quad(n\ge5,\ n=2\bmod3).}
 \tag{17}
$$


The right side is nonnegative, as is also clear from the binomial
factor (2n+1)!/(n!)^2. This describes the formerly unresolved numerator
cancellation, rather than bypassing it.

## 5. A precise general odd-prime gate

The same finite-tail argument has a useful exact prime-independent
form. For an odd prime p define d_r=D_r modulo p for 0<=r<p;
the recurrence proves D_j=d_(j mod p) modulo p for every j>=0.
Let alpha_s=[x^s](1-x+x^2/2)^(-1) in F_p[[x]], and set



$$
h_p=\sum_{s=0}^{p-1}(-1)^s s!\alpha_s,
\quad a_p=\sum_{s=0}^{p-1}(-1)^s s!\alpha_s
                       d_{(p-2-s)\bmod p},
$$




$$
c_p=2(a_p-h_p d_{p-1})\in\mathbb F_p.                  \tag{18}
$$


For every n=-1 modulo p, the first contraction has only s<p
surviving, while the second contraction has only s=0 surviving:
s=1,...,p-1 have a_s(n+1)=0; s=p has multiplier 0; s>p
has a falling-factorial multiple of p. Therefore



$$
\mathscr C_n=c_p\pmod p.                              \tag{19}
$$


If c_p!=0, P_n!=0 modulo p, and
2v_p(n!)>floor(log_p(n+1)), then the same proof gives



$$
\boxed{v_p(q_n)=2v_p(n!).}                            \tag{20}
$$


The condition on P_n is an exact Lucas digit condition and is not
silently assumed at primes other than 3. If c_p=0, this one-layer
argument gives no upper bound for the numerator valuation. No claim
about arbitrarily many good primes or their support follows here.

## 6. Reproducibility and scope

`check_hp_b1_ternary_actual_denominator.py` independently checks the
Rodrigues contractions and the actual rational endpoint numerator only
at the two previously frozen indices n=2,8. It also records the exact
three-residue D recurrence and the symbolic three surviving terms.
There is no new canonical degree construction or degree sweep.
Output: `hp_b1_ternary_actual_denominator_checks.json`.

At n=8 the theorem reproduces v_3(q_8)=4 and v_3(N_8)=2.
At n=2 the strict inequality (15) is unavailable, and the actual
endpoint has q_2=28, so v_3(q_2)=0. That exception is explicitly
excluded rather than used to guess a law.

This result supplies a factorial valuation at one fixed prime on a
specified infinite residue class. Its logarithmic contribution is
2v_3(n!)log3=n log3+O(log n). It does not alone decide shrinking of
the degree-one primitive forms, does not cover other ternary residue
classes, and proves no irrationality assertion.
