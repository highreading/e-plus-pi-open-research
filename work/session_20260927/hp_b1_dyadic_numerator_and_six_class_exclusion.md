> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Dyadic numerator depth and exclusion of the n=2 mod 6 subsequence

Date: 2026-09-27. Author: audit_computations.
Status: FULL PASS by root in hp_b1_dyadic_independent_root_review.md.

This note continues `hp_b1_ternary_actual_denominator.md`, whose
complete independent review has passed. It uses the exact same actual
endpoint quotient and Rodrigues-normalized sums. There are no new
canonical degrees, prime scans, or extrapolated valuations.

## 1. Statement with the actual reduced endpoint retained

Use H_n,K_(n+1),P_n,Q_n,T_n,Delta_n and the sums
mathscr A_n,mathscr B_n,mathscr C_n from that note. Put



$$
\mathscr U_n=2K_{n+1}S_n-(n+1)H_nS_{n+1},\qquad X/Y=\mathscr U_n/\Delta_n.
 \tag{1}
$$


The first assertion holds for every even n>=2, without a
nonvanishing assumption on Delta:



$$
\boxed{v_2(\mathscr U_n)=n+2-2v_2(n!).}                 \tag{2}
$$


Consequently, whenever Delta_n!=0, the actual reduced denominator obeys



$$
v_2(q_n)=\max\{0,v_2(\Delta_n)-n-2+2v_2(n!)\},
$$




$$
\boxed{v_2(q_n)\ge 2v_2(n!)-n/2.}                   \tag{3}
$$


The lower bound is harmless if its right side is zero or negative.

On n=2 modulo 6, n>=8, the ternary theorem supplies both
Delta_n!=0 and v_3(q_n)=2v_3(n!). Thus



$$
\liminf_{\substack{n\to\infty\\n=2\ (6)}}\frac{\log q_n}{n}
 \ge\frac32\log2+\log3=\log(6\sqrt2).
 \tag{4}
$$


The independently proved analytic error formula for this very family is



$$
\log|\mathcal L_n|=\log q_n-2n\log(1+\sqrt2)+o(n),
$$


where mathcal L_n is its gcd-reduced integer form in e+pi. It follows that



$$
\boxed{\liminf_{\substack{n\to\infty\\n=2\ (6)}}
 \frac{\log|\mathcal L_n|}{n}
 \ge\log(18\sqrt2-24)>0.}                              \tag{5}
$$


This rules out shrinking on this specified infinite subsequence. It is
not a theorem excluding all indices of the degree-one family and is
not an irrationality proof.

## 2. Integer divided-power coefficients

Let phi(x)=1-x+x^2/2, and write



$$
g_s(k)=s![x^s]\phi(x)^k\in\mathbb Z.
$$


The integrality follows by multiplying exponential generating series:
the divided-power coefficient of a product is
sum_j binom(s,j) f_j g_(s-j). In this integer divided-power ring,
the square of any series with constant coefficient 1 is congruent to
1 modulo 2. Indeed the j and s-j terms pair when j!=s-j;
the unpaired middle term has binom(2j,j) even for j>=1.
Therefore



$$
g_s(k)\equiv
 \begin{cases}
  [s=0],&k\text{ even},\\
  [s=0]+[s=1]+[s=2],&k\text{ odd}
 \end{cases}\pmod2.
 \tag{6}
$$


Square brackets in (6) denote indicator functions.

The normalized contractions from the preceding note can be written



$$
H_n=\sum_{s=0}^n\binom ns g_s(n),\qquad
 \mathscr A_n=\sum_{s=0}^n\binom ns g_s(n)D_{2n-s},
 \tag{7}
$$


where D_j=j! sum_(r=0)^j1/r!. For k=n+1, write



$$
w_s=\frac{2k-s}{k}\binom ks g_s(k)\quad(0\le s\le k).
$$


Then, including w_0=2,



$$
K_k=\sum_{s=0}^k w_s,\qquad
 \mathscr B_n=\sum_{s=0}^k w_sD_{2k-1-s}.              \tag{8}
$$


When n is even, k is odd, so all w_s and both sums in (8)
are in Z_(2). No division by an even integer is used.

## 3. The exact normalized numerator has valuation one

The recurrence D_j=jD_(j-1)+1 proves the complete residue pattern



$$
D_{2r}=1\pmod4,\qquad
 D_{4r+1}=2\pmod4,\qquad D_{4r+3}=0\pmod4.
 \tag{9}
$$


For clarity, D_even=1 modulo 4 follows because D_odd is even;
the two odd residues then follow by one further recurrence step.

Suppose n is even. By (6), H_n is odd. In the difference
mathscr A_n-H_n, all even s terms vanish modulo 4 by (9).
For odd s, g_s(n) is even by (6), while binom(n,s) is even:
s binom(n,s)=n binom(n-1,s-1), and s is odd. Hence



$$
\mathscr A_n-H_n=0\pmod4.                             \tag{10}
$$



Next use k=n+1 odd in (8). In mathscr B_n-K_k, every odd
s term vanishes modulo 4 because 2k-1-s is even.
For the remaining terms:

* s=0 contributes 2(D_(2k-1)-1)=2 modulo 4, since 2k-1=1 modulo 4.
* s=2 has w_2=(k-1)^2 g_2(k), which is divisible by 4.
* Every even s>=4 has g_s(k) even by (6), and 2k-s is even;
  the denominator k is odd. Therefore w_s is divisible by 4 in Z_(2).

Consequently



$$
\mathscr B_n-K_{n+1}=2\pmod4.
 \tag{11}
$$


Since K_(n+1) is an integer and H_n is odd, (10)-(11) give



$$
\boxed{\mathscr C_n=K_{n+1}\mathscr A_n-H_n\mathscr B_n
                  =2\pmod4.}                         \tag{12}
$$


In particular its 2-adic valuation is exactly one. This proof does
not infer a congruence from the two frozen controls.

## 4. The rational second-kind part has strictly larger valuation

The integer Legendre endpoint generating function can be rewritten as



$$
(1-4t-4t^2)^{-1/2}
 =\frac1{1-2t}\left(1-\frac{8t^2}{(1-2t)^2}\right)^{-1/2}.
$$


Expanding first in the second factor gives the exact integer sum



$$
P_k=\sum_{j=0}^{\lfloor k/2\rfloor}
       2^{k-j}\binom{k}{2j}\binom{2j}{j}.
 \tag{13}
$$


It follows that



$$
v_2(P_k)\ge\lceil k/2\rceil.                         \tag{14}
$$


Root supplied the useful one-power sharpening: for k>=2, the j=0
term has valuation k>=ceil(k/2)+1; every j>=1 term gains another
factor 2 from the central binomial coefficient. Thus
v_2(P_k)>=ceil(k/2)+1 for k>=2.
The exact rational second-kind convolution therefore gives



$$
v_2(Q_k)\ge3+\lceil(k-1)/2\rceil-\lfloor\log_2 k\rfloor
 \quad(k\ge1).
 \tag{15}
$$


Indeed each product P_(j-1)P_(k-j) has valuation at least
ceil((k-1)/2), while v_2(j)<=floor(log_2 k).

For even n>=2, let ell=floor(log_2(n+1)). The elementary inequality
n+1<2^(n/2+1) gives ell<=n/2. Hence, using integral H,K,



$$
v_2(2K_{n+1}Q_n-(n+1)H_nQ_{n+1})
 \ge3+n/2-\ell\ge3.                                  \tag{16}
$$


On the other hand (12) gives



$$
v_2\left(\frac{2^{n+1}}{(n!)^2}\mathscr C_n\right)
 =n+2-2v_2(n!)\le2,
 \tag{17}
$$


because v_2(n!)>=n/2 for even n. The two summands in the
exact numerator identity (8) of the preceding note have strictly
different valuations. Thus their sum has valuation (17), proving (2).

Finally the sharpened bound after (14) shows both summands in Delta_n
are divisible by 2^(n/2+2): n+1 is odd, P_(n+1) has that valuation
lower bound, and 2P_n does as well. This proves (3).

## 5. The combined actual-denominator exclusion

For even n=2 modulo 3, n>=8, the reviewed ternary theorem gives
Delta_n a 3-adic unit and v_3(q_n)=2v_3(n!). Since q_n is the
same actual reduced denominator in both calculations, it has the divisor



$$
2^{\,2v_2(n!)-n/2}\,3^{\,2v_3(n!)}\mid q_n.
 \tag{18}
$$


The exponent of 2 is nonnegative in this range. The elementary formula
v_p(n!)=n/(p-1)+O(log n), obtained by summing the floors, proves (4).

The analytic input is the exact endpoint theorem in
`../session_20260913/hp_b1_endpoint_attempt.md`, equations (1),(2)
and its primitive ledger. Its sharpened signed asymptotic is also in
`hp_b2_endpoint_attempt.md`, Section 6.1. These sources concern the
same X/Y from (1), so multiplying by its actual reduced q requires
no additional coefficient normalization or unproved height estimate.

Combining the analytic rate with (4) gives (5). Its positivity has the
exact elementary certificate 18sqrt(2)>25, because 648>625.
Thus these primitive forms grow exponentially along n=2 modulo 6.
The other five residue classes remain outside this conclusion.

## 6. Reproducible finite checks

The existing frozen degrees n=2,8 suffice to check both exact rational
normalizations. The checker
`check_hp_b1_ternary_actual_denominator.py` is extended only to record
v_2(mathscr C_n)=1, formula (2), formula (3)'s exact endpoint
valuation, and the Legendre sum (13) at the already computed indices.
No new canonical index is introduced.

At n=2, v_2(mathscr U_n)=2 and v_2(q_n)=2.
At n=8, v_2(mathscr U_n)=-4 and v_2(q_n)=13.
The theorem, including all even n, follows from Sections 2-4 rather
than those finite values.
