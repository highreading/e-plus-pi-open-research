> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact coefficient-denominator obstruction and special-value congruences

Date: 2026-09-13. Bounded continuation of
`hp_b1_primitive_arithmetic_attempt.md`.

## Outcome

The proposed common-coefficient-denominator target in that note is
impossible. If S_n clears C_0-C_1, then



$$
\log S_n\ge 2n\log n-O(n).
$$



Together with the proved elementary clearer, this determines the leading
growth of the *actual minimal coefficient denominator*: it is
2n log n+O(n). Consequently a coefficient clearer with leading exponent
less than3/2 cannot extend the b=0 rational-companion obstruction to b=1.
This result does not bound the reduced endpoint height after its gcd.

For the special integers in the new endpoint-gcd gate, I prove full
odd-prime-power index congruences, not merely the proposed mod-p reduction:



$$
n\equiv m\pmod{p^a}\Longrightarrow
 H_n(1)\equiv H_m(1),\qquad J_n(1)\equiv J_m(1)\pmod{p^a}
$$



for every odd prime p and a>=1. These give an exact compatible residue
tree for the special gcd and an obligatory divisor, the odd part of n-1.
They give no upper valuation bound or common-zero count by themselves.
In particular, they do not close the existing large-prime endpoint-gcd
gate, whose range p>2n+2 has n<p already.

## 1. The coefficient denominator has leading exponent exactly2

Retain the exact moment functional and reproducing kernel



$$
\mathcal L(P)=\int_{-1}^1P((1+iu)/2)\,du,\qquad
 K_n(t,s)=\sum_{k=0}^n p_k(t)p_k(s)/h_k.
$$



Every polynomial Q of degree at most n satisfies



$$
\mathcal L^{(t)}(Q(t)K_n(t,s))=Q(s).
\tag{1}
$$



Set D_n^*=C_0^*-C_1^*=ell_Delta^{(s)}K_n(t,s), where



$$
\ell_\Delta(s^j)=\frac1{(n+j)!}-\frac1{(n+j+1)!}
 =\frac{n+j}{(n+j+1)!}.
$$



Applying (1) to Q(t)=t^n gives the exact identity



$$
\mathcal L(t^nD_n^*)=\frac{2n}{(2n+1)!}.
\tag{2}
$$



No limit or approximation is involved. The moments have the direct
formula



$$
\mathcal L(t^k)=2^{-k}\sum_{\substack{0\le j\le k\\j\text{ even}}}
 \binom{k}{j}(-1)^{j/2}\frac2{j+1}.
\tag{3}
$$



Here the summation condition in (3) means that j is even. Thus the integer



$$
d_n=2^{2n}\operatorname{lcm}(1,2,\ldots,2n+1)
\tag{4}
$$



clears every moment through degree2n. If S_n is any positive integer
clearing D_n^*, then S_n t^nD_n^* is an integer polynomial of degree
at most2n, so d_n S_n times (2) is integral. Its reduced denominator is



$$
D_n^{\mathrm{mom}}=\frac{(2n+1)!}{2n},
$$



because 2n divides (2n+1)!. Therefore the sharper exact divisibility



$$
\frac{D_n^{\mathrm{mom}}}
 {\gcd(D_n^{\mathrm{mom}},d_n)}\ \mid\ S_n
\tag{5}
$$



holds. In particular,



$$
S_n\ge D_n^{\mathrm{mom}}/d_n.
\tag{6}
$$



The standard elementary estimate log lcm(1,...,N)=O(N), together with
Stirling's formula, yields log S_n>=2n log n-O(n). Reversing polynomial
coefficients does not change their common denominator, so this applies
equally to C_0-C_1. The previously proved clearer



$$
T_n^\flat=
 2^{2n+1}(2n+1)!/\prod_{n<p\le2n+1}p
$$



has log T_n^flat=2n log n+O(n). Consequently the minimal coefficient
denominator, also if required to be a multiple of n!, has logarithm
2n log n+O(n).

The upper estimate used in the earlier rational-companion argument is
therefore sharp at its factorial scale. Its proposed improvement to
(3/2-eta)n log n is ruled out for every eta>0, on every infinite
subsequence.

## 2. What this does and does not say about the rational companion

The earlier exact companion is



$$
f_n^*=(g_0-g_1+1/n!)/\delta,
 \quad\delta=t_1-t_0,
 \quad g_j=[T_n(C_jF)](1).
$$



Choose the known T_n^flat as S_n and an exponential integer d_F clearing
the first n Taylor coefficients of F. Define actual integers



$$
N_n=d_F S_n(g_0-g_1+1/n!),\qquad
 M_n=d_F S_n\delta,\qquad
 G_n=\gcd(N_n,M_n)>0.
\tag{7}
$$



For all sufficiently large n, the existing analytic bounds and boundedness
of f_n^* imply



$$
\log\max(|N_n|,|M_n|)=n\log n+O(n),
$$



using the proved lower bound |delta|>=exp(-O(n))/n! as well as its upper
bound. Hence the exact reduced height satisfies



$$
\log H(f_n^*)=n\log n-\log G_n+O(n).
\tag{8}
$$



The obstruction in Section1 concerns coefficient clearing; it does not
exclude factorial cancellation in G_n. To obtain primitive growth by the
existing rational-companion/irrationality-measure argument, a sufficient
new statement would be



$$
\log G_n\ge(1/2+\eta)n\log n-O(n),\qquad\eta>0.
\tag{9}
$$



Indeed (8) and mu(e)=2 then give log q_n>=eta n log n-o(n log n).
No such lower bound for this *specific endpoint gcd* is proved here.
Equation(9) is a replacement arithmetic target, not a prediction that
such cancellation occurs. An upper bound for a different gcd, such as
the full-triple endpoint gcd below, is not interchangeable with (9).

## 3. Explicit special-value sums

Write h_n=H_n(1), u_n=H'_n(1), and j_n=J_n(1)=n h_n+u_n. With
(n)_r=n(n-1)...(n-r+1), set r=b+2c and s=b+c. Direct expansion of
e^t(1-t+t^2/2)^n gives



$$
h_n=\sum_{b,c\ge0}
 \frac{(-1)^b}{2^c}(n)_r\binom ns\binom sc,
\tag{10}
$$





$$
u_n=\sum_{b,c\ge0}
 \frac{(-1)^b}{2^c}(n)_{r+1}\binom ns\binom sc.
\tag{11}
$$



Both sums are finite at each nonnegative integer n: falling factorials
vanish when their index exceeds n. These are identities over the
rationals, and their total values are integers by the defining
exponential-series integrality argument. Notice r>=s, and r+1>=s.

## 4. A congruence-preserving factorial-binomial lemma

Let p be an odd prime. If r>=s>=0, the function



$$
V_{r,s}(n)=(n)_r\binom ns
$$



on nonnegative integers preserves congruences modulo every p^a.

To prove this, let m=n+v with p^a|v and v>=0. The factor (n)_r is an
integer polynomial, so (m)_r-(n)_r is divisible by p^a. For s>=1,
Vandermonde's identity gives



$$
\binom ms-\binom ns
 =\sum_{k=1}^s\binom vk\binom n{s-k}.
$$



For every nonzero summand, k binom(v,k)=v binom(v-1,k-1), whence



$$
v_p\left(\binom ms-\binom ns\right)
 \ge a-\lfloor\log_p s\rfloor.
\tag{12}
$$



This is a lower bound even when its right side is negative. Also



$$
v_p((n)_r)\ge v_p(r!)\ge\lfloor\log_p s\rfloor,
\tag{13}
$$



because (n)_r=r! binom(n,r); a zero falling factorial causes no problem.
The last inequality follows by summing floor(r/p^i) for
1<=i<=floor(log_p s). Multiplying (12) by (n)_r, and using the
integer-polynomial difference for the other product term, proves the
claim. The case s=0 is immediate. Exchanging m,n handles any pair with
n congruent to m modulo p^a.

Every term of (10) and (11) is a p-integral constant times such a
congruence-preserving function. Taking the union of the two finite
index sets therefore proves



$$
n\equiv m\pmod{p^a}\Longrightarrow
 h_n\equiv h_m,\quad u_n\equiv u_m,\quad j_n\equiv j_m
 \pmod{p^a}.
\tag{14}
$$



This is stronger than mod-p periodicity and is proved without an
assumption about carries. It is not asserted for p=2: for example
h_1=0 and h_3=-5 already disprove the analogous mod2 statement.

For computation modulo p^a one may truncate (10) to r<ap, because
v_p((n)_r)>=v_p(r!)>=a for r>=ap. The analogous truncation in (11)
uses r+1<ap. Thus this is also an explicit finite actual-state map
at each precision, with a number of summands bounded in terms of ap
alone, independent of n.

## 5. Exact consequences for the auxiliary gcd

Let g_n=gcd(h_n,j_(n+1)), for n>=2. If r is the least nonnegative
residue of n modulo p^a, then



$$
p^a\mid g_n
 \quad\Longleftrightarrow\quad
 h_r\equiv0,\ j_{r+1}\equiv0\pmod{p^a}.
\tag{15}
$$



If r=p^a-1, the second value may equivalently be replaced by j_0=0,
using (14). Therefore define an actual root set



$$
Z_{p,a}=\{0\le r<p^a:h_r=j_{r+1}=0\pmod{p^a}\}.
$$



The sets project compatibly under reduction modulo p^a. This is an
exact description of the valuation tree. A bound on the number or
depth of its branches is a separate mathematical requirement.

In particular h_1=0 and j_2=0. Equation(14) therefore proves the genuine
all-index divisibility



$$
\operatorname{oddpart}(n-1)\mid g_n.
\tag{16}
$$



This explains the recurrent factors n-1 in the already checked small
examples. It is a lower bound, not evidence for a complete gcd formula.

A subsequent exact local theorem in `hp_special_gcd_unit_lift.md`
sharpens this particular branch: for every odd p dividing n-1,
v_p(g_n)=v_p(n-1). Its proof gives J_(n+1)(1)=8(n-1) modulo
p^(v_p(n-1)+1). Thus there are no additional common lifts over the
forced residue1 modulo p. Other residue branches remain unresolved.

The previously proved full-triple endpoint restriction is



$$
v_p(d_n^{\rm endpoint})\le v_p(g_n),\qquad p>2n+2.
$$



In precisely that range n is already its least residue modulo p^a.
Thus (14) alone does not reduce the hard large-prime gate to smaller
indices. For small primes the full-triple restriction has additional
factorial and moment-matrix valuation obstructions; it has not been
silently extended to those primes. No upper bound for the actual
endpoint gcd or reduced q_n follows from (14)–(16) alone.

## 6. An exact recurrence, and its limitation

The exponential generating function of h_n is explicit. Let



$$
w=z(1-w+w^2/2),\quad w(0)=0,\qquad
 \Delta=1+2z-z^2.
$$



The formal Lagrange coefficient identity gives



$$
\sum_{n\ge0}h_n\frac{z^n}{n!}
 =\frac{e^{w(z)}}{\sqrt\Delta},\qquad
 w(z)=\frac{1+z-\sqrt\Delta}{z}.
\tag{17}
$$



All identities here are identities of formal power series; the apparent
singularity at z=0 is removable on the displayed branch. Differentiating
(17) and eliminating sqrt(Delta) yields, for G equal to its left side,



$$
z^2(z+1)(z^2-2z-1)G''
 +2(2z^4+z^3-5z^2-4z-1)G'
 +2z(z+1)^2G=0.
\tag{18}
$$



Equivalently, with h_0=1, h_1=0, h_2=1, h_3=-5,



$$
\begin{aligned}
 2h_{n+1}={}&-n(n+7)h_n+n(6-n-3n^2)h_{n-1}\\
 &+n(n-1)^2(6-n)h_{n-2}
 +n(n-1)^2(n-2)^2h_{n-3},\qquad n\ge3.
\end{aligned}
\tag{19}
$$



This gives a four-coordinate recurrence rather than a second-order
coprimality recurrence. Vanishing of the two special gcd coordinates
does not imply vanishing of the full state. No conclusion about gcd
support has been drawn just from the existence of (19).

## 7. Verification and next action

The new denominator obstruction was independently checked by
audit_computations and recorded in Section7 of
`hp_b1_prime_folding_independent_review.md`. Its exact meaning is the
growth of the common coefficient denominator; a reduced endpoint
denominator can still be much smaller.

`check_hp_b1_denominator_and_special_gcd.py` and its JSON result record
five fixed moment/divisibility controls, four fixed prime-power index
controls, seven obligatory-divisor controls, and five recurrence
controls. They all pass. The checker additionally verifies the two
quadratic-extension coefficients of (18) are identically zero as
rational functions, using exact symbolic arithmetic. None of the
finite controls is used to infer an asymptotic theorem.

The useful change in route priority is concrete: remove the impossible
coefficient-clearer target from the b=1 queue. Further work on this
rational companion must concern its actual evaluated gcd (7), or a
different rational companion with a proved stronger error rate. The
special-value residue tree may help future local arithmetic, but a
periodic index description alone supplies neither a positive irrationality
margin nor an upper endpoint-gcd bound.

## 8. A bounded direct test of the special prime-support hypothesis

The concrete statement tested was: every prime factor of
gcd(h_n,j_(n+1)) is at most2n+2, for n>=2. The test was predeclared to
stop at its first counterexample or n=256. It found no counterexample
in that finite range. This is explicitly inconclusive; it is not a
prime-support theorem or a gcd growth estimate.

The integers were computed by the proved recurrence (19), together with
E_n=n![z^n]e^{w(z)}. The exact identities z(e^w)'=wG and
z^2(e^w)'+e^w=(1+z)G give



$$
u_n=nE_n,\qquad
 E_n=h_n+nh_{n-1}-n(n-1)E_{n-1},\quad E_0=1.
\tag{20}
$$



For each tested n the exact gcd was stripped of all prime factors at
most2n+2; the remaining factor was1. No floating-point values or integer
relation searches were used.

A structural obstruction remains. A counterexample prime p>2n+2 would
give, over F_p, a remainder of order at least2n+2 for degree caps
(n-1,0,n-1), by the two extra orthogonality gates. This reaches the
existing general Wronskian multiplicity ceiling exactly. That ceiling
therefore permits the exceptional case; a strict finite-field normality
or multiplicity result would be needed to rule it out. The earlier
polynomial-in-x resultant examples do not decide this special-value
question, and the finite prefix cannot replace such a result.

## 9. Every integral exponential coefficient has a large forced divisor

This proposition was first derived here for b=1 from the last two moment
rows; root supplied the general interpolation argument below, which has
been independently checked.

Consider an integral HP triple (A,B,C) with degree caps (n,b,n),
1<=b<=n, satisfying the usual order2n+b+1 conditions for e^z and F(z).
Let B(z)=sum_(j=0)^b B_j z^j, and use the moment clearer d_n in (4).
Set



$$
N_0=2n-b+1,\qquad
 M_{n,b}=\frac{N_0!}{\gcd(N_0!,d_n b!)}.
\tag{21}
$$



Then



$$
M_{n,b}\mid B_j\quad(0\le j\le b).
\tag{22}
$$



Indeed, the high Taylor conditions give reproduced moments



$$
\mathcal L(t^k C^*)=-\sum_{j=0}^b\frac{B_j}{(n+k+1-j)!}.
$$



For k=n-b,...,n put N=n+k+1 and
P_B(N)=sum_j B_j(N)_j, an integer polynomial of degree at most b.
The left side has degree at most2n under the moment functional, so



$$
N_0!\mid d_n P_B(N),\qquad N=N_0,N_0+1,\ldots,N_0+b.
\tag{23}
$$



Lagrange interpolation at these consecutive integer nodes has denominator
k!(b-k)! at the k-th node, which divides b!. Therefore every monomial
coefficient of d_n b! P_B is divisible by N_0!. The change from monomial
coefficients to the falling-factorial basis is integral (its entries are
Stirling numbers of the second kind). Thus N_0! divides d_n b! B_j for
each j, proving (22).

The matched endpoint Y=B(1)=C(1) consequently is a multiple of M_(n,b).
Whenever it is nonzero,



$$
\log|Y|\ge\log((2n-b+1)!)-\log(b!)-O(n).
\tag{24}
$$



In particular log|Y|>=2n log n-O(n) for fixed b. The same leading
exponent2 holds when b is of order n/log n: the loss from b and b! is
only O(n). This applies to the primitive full integral triple as well
as to every integral multiple, provided the endpoint is nonzero.

For b=1, (23) at N=2n and2n+1 directly gives (2n)! dividing both
d_n B_0 and d_n B_1, without any interpolation denominator. Its matched
endpoint is known to be nonzero eventually from the analytic theorem.

This is an actual arithmetic constraint before the endpoint pair is
reduced. If d=gcd(A(1),Y), the final denominator is |Y|/d; (24) alone
does not bound d and therefore is not a lower bound for q_n. It precisely
quantifies the cancellation that a small primitive endpoint pair would
require.
