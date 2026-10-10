> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Degree-one HP arithmetic through adjacent scalar factorial sums

Date: 2026-09-13. Original bounded continuation by audit_computations.
Independent review: FULL PASS in
`hp_b1_adjacent_scalar_independent_review.md` (audit_results), including
an unchanged rerun of the two frozen controls. No new canonical degree
or prime scan.

The archive already contains the general two-by-two endpoint kernel gate,
the large-prime folding theorem, and the actual exclusion p not dividing
q_(p-1). This note does not repeat those as new results. It eliminates
the whole reproducing kernel from the endpoint quotient, gives an exact
integer valuation criterion in four scalar factorial sums, and determines
the endpoint-difference valuation on a general n=ap-1 class. The final
numerator cancellation remains explicit.

## 1. Integer Legendre and second-kind data

Use the same degree-(n,1,n) family and moment functional as
`hp_b1_endpoint_attempt.md`,


$$
\mathcal L(f)=\int_{-1}^1f((1+iu)/2)du.
$$


Write ordinary Legendre polynomials as Leg_k and define


$$
L_k(t)=2^ki^k\operatorname{Leg}_k(-i(2t-1))\in\mathbb Z[t],
 \quad P_k=L_k(1)\in\mathbb Z,
$$




$$
Q_k=\mathcal L\!\left(\frac{L_k(t)-P_k}{t-1}\right)\in\mathbb Q.
                                                               \tag{1}
$$


These Q_k are rational second-kind endpoint values; they contain no pi.
The exact explicit identity is


$$
\boxed{Q_k=8\sum_{j=1}^k\frac{P_{j-1}P_{k-j}}j,\quad Q_0=0.}
                                                               \tag{2}
$$


To verify the constant, the ordinary polynomial second kind is


$$
W_{k-1}(x)=\tfrac12\int_{-1}^1
(\operatorname{Leg}_k(u)-\operatorname{Leg}_k(x))/(u-x)du
$$

.
Its generating function is the Legendre generating function multiplied
by its integral from zero. This follows directly from the inhomogeneous
first-order equation for that generating function, or from the monic
three-term recurrence and the initial value W_0=1. Consequently


$$
W_{k-1}(x)=\sum_{j=1}^k\operatorname{Leg}_{j-1}(x)
\operatorname{Leg}_{k-j}(x)/j
$$

. Changing variables in (1) gives
Q_k=2^(k+2)i^(k-1)W_(k-1)(-i), which is exactly (2).
In particular lcm(1,...,k) clears Q_k; no growing dyadic denominator is
hidden in (2).

For the rest of the note n is fixed. Set E_d=sum_(r=0)^d 1/r! and


$$
R_k=\sum_{j=0}^k\frac{[t^j]L_k(t)}{(n+j)!},\qquad
 T_k=\sum_{j=0}^k[t^j]L_k(t)E_{n+j},\qquad S_k=Q_k+T_k,
 \quad k=n,n+1.                                        \tag{3}
$$


The dependence of R_k,T_k on the fixed n is understood. In particular
T_(n+1) still uses E_(n+j), not E_(n+1+j).

## 2. Exact cancellation of the entire kernel

First use monic p_k, write $\mathsf P_k=p_k(1)$,
$\mathsf Q_k=\mathcal L((p_k(t)-p_k(1))/(t-1))$, and let h_n be the
monic norm. Define the rational kernel polynomials


$$
V(s)=K_n(1,s),\quad
 J(s)=\mathcal L_t\!\left(\frac{K_n(t,s)-K_n(1,s)}{t-1}\right).
$$


The established endpoint reconstruction is


$$
t_j=\ell_j V,\quad a_j=-E_{n-j}+\ell_jJ,\quad
 X=(1+t_1)a_0-(1+t_0)a_1,\quad Y=\delta=t_1-t_0.
                                                               \tag{4}
$$


Here $\ell_j(s^r)=1/(n+r+1-j)!$, j=0,1. This is precisely the actual
rational representative already used in the archived endpoint theorem.

Christoffel–Darboux and its second-kind integral give


$$
(1-s)V=\frac{\mathsf P_{n+1}p_n-\mathsf P_np_{n+1}}{h_n},
$$




$$
(1-s)J=\frac{\mathsf Q_{n+1}p_n-\mathsf Q_np_{n+1}}{h_n}-1,
 \quad
 \mathsf Q_{n+1}\mathsf P_n-\mathsf Q_n\mathsf P_{n+1}=h_n.
                                                               \tag{5}
$$


The constant -1 follows from reproduction of the constant polynomial.
For example the last identity starts at n=0 with Q_1=2,h_0=2 in the
monic normalization and propagates by the norm ratio. No singular
integral is taken at s=1; every divided difference is polynomial.

Let D(s)=(p_n(s)-\mathsf P_n)/(s-1), d_j=ell_jD, and use a sans-serif
R,T for the corresponding monic versions of (3). Equations (5) imply


$$
J=\frac{\mathsf Q_n}{\mathsf P_n}V-\frac D{\mathsf P_n},
$$




$$
\delta=\frac{\mathsf P_{n+1}\mathsf R_n-
                         \mathsf P_n\mathsf R_{n+1}}{h_n},
$$




$$
t_0=\frac{\mathsf P_n\mathsf T_{n+1}
                   -\mathsf P_{n+1}\mathsf T_n}{h_n}.       \tag{6}
$$


The functional identity ell_1(sD)=ell_0(D) additionally gives


$$
d_1-d_0=\mathsf P_n/n!-\mathsf R_n,
 \qquad d_0=\mathsf T_n-\mathsf P_n E_n.
$$


Substituting into (4) first yields


$$
X/Y=-\mathsf Q_n/\mathsf P_n-\mathsf T_n/\mathsf P_n
               -(1+t_0)\mathsf R_n/(\mathsf P_n\delta).
$$


Using (6) cancels both $\mathsf T_n\mathsf P_{n+1}\mathsf R_n$
terms; the last identity in (5) cancels the remaining norm. Since each
degree's scaling factor cancels from both determinants, the result in
the integer L_k normalization is


$$
\boxed{\frac XY=
 \frac{R_{n+1}S_n-R_nS_{n+1}}
      {P_{n+1}R_n-P_nR_{n+1}}.}                         \tag{7}
$$


This formula requires Y!=0, exactly as does the original endpoint ratio.
It involves only the two adjacent polynomial indices. In particular it
does not retain an implicit sum over every intermediate kernel mode.

## 3. Two exact derivative-factorial sums and an integral endpoint scalar

Use the already proved integer sequence


$$
H_k=k![z^k]e^z(1-z+z^2/2)^k,\qquad
 J_k=kH_k+H_k'(1),\qquad K_k=J_k/k\quad(k\ge1),
                                                               \tag{8}
$$


where in the first two expressions H_k(x)=k![z^k]e^(xz)(1-z+z²/2)^k
and H_k without an argument means H_k(1). The earlier integral recurrence
H_k'(1)=k E_k, with integer E_k, proves K_k=H_k+E_k is an integer;
division by k is not assumed harmless. This auxiliary E_k is distinct
from the exponential partial sum E_d used in (3).

The reviewed Rodrigues contractions give exactly


$$
R_n=\frac{2^n H_n}{(n!)^2},\qquad
 R_{n+1}=\frac{2^{n+1}K_{n+1}}{(n+1)(n!)^2}.           \tag{9}
$$


For the second formula, start with
ell_1 p_(n+1)=J_(n+1)/(2n+2)! and multiply by
2^(n+1) binom(2n+2,n+1). Substitution of J_(n+1)=(n+1)K_(n+1)
gives (9), including its single factor n+1.

Define the integer


$$
\boxed{\Delta_n=(n+1)P_{n+1}H_n-2P_nK_{n+1}.}         \tag{10}
$$


Then the original endpoint difference, not a new normalization, is


$$
\boxed{\delta=\frac{(-1)^n\Delta_n}{2^{n+3}(n!)^2}.}  \tag{11}
$$


Indeed h_n=2(-1)^n/((2n+1)binom(2n,n)^2), and the monic scaling factors
in (6) reduce to (11). Eliminating the common factor in (9) from (7)
also gives the simpler exact quotient


$$
\boxed{\frac XY=
 \frac{2K_{n+1}S_n-(n+1)H_nS_{n+1}}{\Delta_n}.}        \tag{12}
$$



## 4. An exact fixed-prime criterion for the reduced denominator

Put M=(2n+1)! and


$$
A_0=M S_n,\quad A_1=M S_{n+1},\quad
 \mathcal N_n=2K_{n+1}A_0-(n+1)H_nA_1.                \tag{13}
$$


These are integers. The factorials in T_n,T_(n+1) have indices at most
2n+1, and (2) has denominators j<=n+1, which also divide M.
Consequently


$$
\boxed{q_n=\frac{|M\Delta_n|}{\gcd(|\mathcal N_n|,|M\Delta_n|)},}
$$




$$
\boxed{v_p(q_n)=\max\{0,\ v_p(M)+v_p(\Delta_n)
                                      -v_p(\mathcal N_n)\}.}   \tag{14}
$$


This is valid for every prime, including 2, whenever Delta_n!=0. If
N_n=0 its valuation is infinity and the formula gives q_n=1.

Thus modular endpoint research reduces to the four factorial sums
H_n,K_(n+1),T_n,T_(n+1), together with the elementary integer Legendre
values and rational second-kind convolution (2). The exact common
factor in (13) is retained: a lower bound for M or for a coefficient
clearer is not an actual lower bound for q_n. A large valuation of
N_n can cancel every such factor.

## 5. General n=ap-1 classes: the denominator-side valuation is exact

The independently proved unit-two identity in
`hp_special_gcd_unit_lift.md`, Section 7, says for every odd p dividing k


$$
J_k\equiv2k\pmod{p^{v_p(k)+1}},\quad K_k\equiv2\pmod p.
$$


Therefore, whenever p divides n+1,


$$
\boxed{\Delta_n\equiv-4P_n\pmod p.}                  \tag{15}
$$


If p does not divide P_n, equations (11),(14) become


$$
\boxed{v_p(\delta)=-2v_p(n!),\qquad
 v_p(q_n)=\max\{0,v_p((2n+1)!)-v_p(\mathcal N_n)\}.}   \tag{16}
$$


In particular Delta_n and Y are nonzero on this entire class. This is a
general prime-block statement, not just the archived single block n=p-1.

The Legendre endpoint sequence has the exact generating function


$$
\sum_{j\ge0}P_jt^j=(1-4t-4t^2)^{-1/2}.
$$


In characteristic p it factors as


$$
F(t)=(1-4t-4t^2)^{(p-1)/2}F(t^p).
$$


The polynomial factor has degree p-1, and its coefficients through that
degree equal P_0,...,P_(p-1) modulo p. Hence the genuine Lucas product is


$$
P_{ap+b}\equiv P_aP_b\pmod p\quad(0\le b<p).
$$


Its last digit has $P_{p-1}\equiv\chi_p=(-1)^{(p-1)/2}$, proving


$$
\boxed{P_{ap-1}\equiv\chi_pP_{a-1}\pmod p.}          \tag{17}
$$


Thus (16) holds for every a>=1 with p not dividing P_(a-1), without a
bound on a. This is an explicit finite-digit condition at any fixed p.

At p=3 the digit polynomial is exactly 1-t-t^2. None of its three
coefficients vanishes. Therefore P_j is a ternary unit for every j,
and (16) holds for **every** n congruent to 2 modulo 3. Equivalently,
the endpoint difference has its full factorial pole of order
2v_3(n!), while the actual reduced q is governed by the one remaining
integer numerator N_n in (13).

For a=1, the separately proved folding theorem gives p not dividing
q_(p-1). Equations (14)-(17) consequently force N_(p-1) divisible by p,
despite Delta_(p-1) being a unit and M having valuation one. This
demonstrates why the new denominator-side unit must not be promoted
to a uniform factorial lower bound for the reduced q.

## 6. Two frozen normalization controls and the remaining arithmetic

`check_hp_b1_adjacent_scalar_gate.py` uses only the previously studied
indices n=2,8. It reconstructs the old endpoint quotient directly from
the full kernel formula and checks it against (12)-(14). It also verifies
the second-kind convolution by direct moment integration and both
Rodrigues factorial contractions. Output:
`hp_b1_adjacent_scalar_gate_checks.json`; all checks pass.

| n | Delta_n | reduced X/Y | v3(M) | v3(N_n) | v3(q_n) |
|---:|---:|---|---:|---:|---:|
| 2 | 112 | -165/28 | 1 | 2 | 0 |
| 8 | 7665681841664 | -10187838555646506983/1738576641689395200 | 6 | 2 | 4 |

These are exact normalization controls, not evidence for a growth law.
The new all-index statement is (16)-(17), with its explicit ternary
specialization. The next missing scalar estimate is an upper bound on
v_p(N_n) relative to v_p((2n+1)!) on a specified sequence, or a proved
opposite cancellation theorem. Neither has been established here.
The b=1 analytic error rate and its actual primitive endpoint gcd
therefore remain unresolved arithmetically.
