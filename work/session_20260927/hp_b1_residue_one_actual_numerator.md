> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The residue-one actual numerator: a unit lift except at 3

Date: 2026-09-27. Author: audit_sources.
Status: FULL PASS in named scopes: Sections 1–2 by audit_results in hp_b1_uniform_5_13_independent_review.md; Sections 3–5 by root in hp_b1_ternary_root_independent_root_review.md.
No canonical degree or prime scan. The ternary calculation is an exact
identity of all coefficients of a restricted analytic index germ.

Use the actual b=1 normalization in hp_b1_ternary_actual_denominator.md:


$$
X/Y=\frac{\mathscr Q_n+2^{n+1}\mathscr C_n/(n!)^2}{\Delta_n},
 \qquad \mathscr C_n=K_{n+1}\mathscr A_n-H_n\mathscr B_n,
$$




$$
\mathscr Q_n=2K_{n+1}Q_n-(n+1)H_nQ_{n+1},\quad
 \Delta_n=(n+1)P_{n+1}H_n-2P_nK_{n+1}.                 \tag{1}
$$


Here K is the b=1 integer J_k/k, not the b=2 second derivative.

## 1. Integral analytic contractions for every odd prime

Let (X)_r denote the falling factorial and put


$$
{\cal D}(X)=\sum_{r\ge0}(X)_r.
$$


On X=a+pY its r-th summand has Gauss valuation at least floor(r/p).
It is therefore an integral restricted analytic function on every odd-p
disk. At integers d>=0 it equals d! sum_{j=0}^d1/j!.

Write R=b+2c, s=b+c and epsilon_{b,c}=(-1)^b/(2^c b!c!).
On X=1+pY define


$$
{\cal H}(X)=\sum_{b,c}\epsilon_{b,c}(X)_R(X)_s,
\quad
 {\cal A}(X)=\sum_{b,c}\epsilon_{b,c}(X)_R(X)_s{\cal D}(2X-R),
                                                               \tag{2}
$$




$$
{\cal K}(X)=\frac1{X+1}\sum_{b,c}
 \epsilon_{b,c}(X+1)_R(X+1)_s(2X+2-R),
$$




$$
{\cal B}(X)=\frac1{X+1}\sum_{b,c}
 \epsilon_{b,c}(X+1)_R(X+1)_s(2X+2-R){\cal D}(2X+1-R).       \tag{3}
$$


They interpolate exactly H_n, mathscr A_n, K_{n+1}, mathscr B_n.
For (3), R=0 gives 2, and for R>=1 the identity
(X+1)_R/(X+1)=(X)_{R-1} recovers the actual Rodrigues contractions.

Here is the complete convergence bound. Set k=floor(R/p),
q=floor(s/p). Since v_p(b!c!)<=v_p(s!)=q+v_p(q!),


$$
v_{\rm Gauss}\bigl(\epsilon_{b,c}(X)_R(X)_s\bigr)
 \ge k-v_p(q!)\ge k-v_p(k!)\longrightarrow\infty.             \tag{4}
$$


The shifted X+1 factors have the same bound. D(2X-R) and
D(2X+1-R) are integral restricted series, uniformly bounded in
Gauss norm by 1. The denominator X+1=2+pY is a unit.
Thus all sums converge in Z_p<Y>. Their products and derivatives are
legitimate. This proves analytic interpolation, not merely continuity.

Terms R>=p vanish modulo p by (4); the remaining denominators b!c!
are units. D modulo p likewise consists of finitely many integral
polynomial terms and is constant on each disk. Consequently


$$
{\cal A}(1+pY)\equiv{\cal A}(1)=3,\qquad
 {\cal B}(1+pY)\equiv{\cal B}(1)=10\pmod p.                  \tag{5}
$$


The exact values are D_2-D_1=3 and 2D_3-6D_2+4D_1=10.

## 2. The exact residue-one unit lift for every p>=5

Set C(X)=K(X)A(X)-H(X)B(X).
The already independently reviewed first-lift theorem in
../session_20260913/hp_auxiliary_simple_root_analytic_reduction.md,
Sections 2–3, gives


$$
{\cal H}(1+pY)\equiv-\frac32pY,\qquad
 {\cal K}(1+pY)\equiv4pY\pmod {p^2}.                       \tag{6}
$$


Both are identities in the restricted series ring. The quadratic
first-lift terms vanish because H(1)=K(1)=0.
For K use J_{X+1}/(X+1) and J's index slope 8.

For clarity these slopes are exact rational index derivatives.
Every term of H with s>=2 has two zero falling factors at X=1;
the three terms s<=1 give H_index'(1)=-2+1/2=-3/2.
The adjacent identity gives
K(X)=H_2(X)+(X-1)(H_1(X)-H(X)), where H_r interpolates
H_n^{(r)}(1). Only s<=1 contributes to H_2's index derivative;
its polynomial is (X)_2-X(X)_3+X(X)_4/2, whose derivative at 1
is 3. Since H_1(1)=1, K_index'(1)=4.

Combining (5)–(6) proves


$$
\boxed{{\cal C}(1+pY)\equiv27pY\pmod{p^2}.}              \tag{7}
$$


Also C(1)=0 exactly. Therefore C(1+pY)/(pY) is an integral
restricted series with constant nonzero reduction 27 for p>=5.
It is a unit at every Y in Z_p. For every actual n>=2 with p|n-1,


$$
\boxed{v_p(\mathscr C_n)=v_p(n-1)\quad(p\ge5).}           \tag{8}
$$


This includes a=1. No termwise two-a bound for H_n is invoked;
the reviewed first-lift theorem retains the high-tail cancellation.

Put a=v_p(n-1), f=v_p(n!), L=floor(log_p(n+1)).
The same analytic root divisions show v_p(H_n)>=a and
v_p(K_{n+1})>=a. Hence


$$
v_p(\mathscr Q_n)\ge a-L,\qquad v_p(\Delta_n)\ge a.
$$


If 2f>L, the exponential part of (1) has uniquely least valuation
a-2f. Thus, whenever Delta_n!=0,


$$
\boxed{v_p(q_n)=2f+v_p(\Delta_n)-a\ge2f
   \quad(p\ge5,\ p\mid n-1,\ 2f>L).}                     \tag{9}
$$


This is the actual reduced denominator, including its numerator.
It requires no unit assertion for P_n and no small-prime use of a
large-prime endpoint-gcd gate. Eventual Delta nonvanishing is provided
by the accepted analytic endpoint theorem.

Equation (9) may be combined with independently proved good-residue
seeds at the SAME prime and index. No such seed table is assumed here.

## 3. The exceptional ternary disk, with an exact finite certificate

At p=3, (7) has a nonunit slope. One additional lift resolves its
structure. In (2)–(3), all R>=12 terms vanish coefficientwise
modulo 27: k>=4 and k-v_3(k!)>=3 by v_3(k!)<=(k-1)/2.
Only r<9 is needed in D. Also


$$
1/(2+3Y)\equiv1/2-3Y/4+9Y^2/8\pmod{27}.
$$


Exact finite polynomial arithmetic gives the ENTIRE residue polynomials


$$
\begin{array}{c|c|c}
 \text{germ at }1+3Y&\text{modulus}&\text{polynomial}\\ \hline
 H&27&9Y+9Y^2\\
 K&9&3Y\\
 A&9&3+6Y\\
 B&3&1 .
 \end{array}                                               \tag{10}
$$


Thus


$$
\boxed{{\cal C}(1+3Y)\equiv9Y^2\pmod{27}.}                 \tag{11}
$$


Indeed C/9 modulo 3 equals Y(1+2Y)-(Y+Y^2)=Y^2.
The certificate checks all coefficients and p-unit denominators:
check_hp_b1_residue_one_analytic_germ.py and
hp_b1_residue_one_analytic_germ_checks.json. Its largest intermediate
degree is 54 in Y, not a canonical HP index. No integer-index samples
are used in proving (10).

Since A(1)=3,B(1)=10,H(1)=K(1)=0, the exact slopes above give


$$
{\cal C}'(1)=4\cdot3-(-3/2)\cdot10=27.                    \tag{12}
$$


Consequently


$$
F(Y)=\frac{{\cal C}(1+3Y)}{9Y}\in\mathbb Z_3\langle Y\rangle,
 \quad F(Y)\equiv Y\pmod3,\quad F(0)=9.                    \tag{13}
$$


Hensel gives one root eta in Z_3. Factoring Y-eta gives


$$
{\cal C}(1+3Y)=9Y(Y-\eta)U(Y),\quad U(Y)\equiv1\pmod3,   \tag{14}
$$


so U is a unit everywhere. To justify the global factorization, the
coefficient of Y in F is a unit and all higher coefficients are
divisible by 3; division by the root therefore preserves unit
reduction. Restricted convergence justifies the coefficient sums.

Moreover F(Y)-F(0) is Y times a unit, giving v_3(eta)=2.
The root equation divided by 9 gives eta/9=-1 modulo 3. Hence


$$
\boxed{\xi=1+3\eta\in55+81\mathbb Z_3.}                   \tag{15}
$$


For every integer n>=4 with n=1 modulo 3 and a=v_3(n-1),


$$
\boxed{v_3(\mathscr C_n)=a+v_3(n-\xi).}                   \tag{16}
$$


Zero valuations may be infinite. No irrationality, algebraicity, or
nonintegrality of xi is asserted.

## 4. Exact actual-denominator consequences at 3

From (10) and the exact zeros at X=1,


$$
v_3(H_n)\ge a+1,\qquad v_3(K_{n+1})=a.
$$


Every P_j is a 3-unit by the accepted Lucas identity. The two
terms of Delta_n consequently have unequal valuations, giving


$$
\boxed{v_3(\Delta_n)=a.}                                 \tag{17}
$$


This also proves all-index Delta nonvanishing in this class.

Write f=v_3(n!), L=floor(log_3(n+1)), c=v_3(n-xi).
The second-kind part has valuation at least a-L.
The exponential part has valuation a+c-2f. Therefore


$$
\boxed{c<2f-L\ \Longrightarrow\ v_3(q_n)=2f-c,}           \tag{18}
$$




$$
\boxed{c\ge2f-L\ \Longrightarrow\ v_3(q_n)\le L.}         \tag{19}
$$


The second statement is an upper bound; it preserves possible extra
cancellation rather than presuming a least term.

Outside n=55 modulo 81, c=min(a,3), by (15). For n=7 the
strict inequality in (18) holds directly. For n>=10 with n=1
modulo 3 it follows from 2v_3(n!)>L+3: if L=2,
2floor(n/3)>=6>5; if L>=3, then
2floor(n/3)>=2(3^{L-1}-1)>L+3. Thus


$$
\boxed{v_3(q_n)=2v_3(n!)-\min\{v_3(n-1),3\}
 \quad(n\ge7,\ n\equiv1\pmod3,\ n\not\equiv55\pmod{81}).} \tag{20}
$$


The small index 4 is not included.

The genuine ternary obstruction is now one explicit analytic root:
there is no proved Diophantine upper bound here for v_3(n-xi) as
the ordinary integer n increases. The Hensel lemma alone cannot
provide one.

## 5. The zero residue and scope

The separate hp_b1_ternary_zero_class_addendum.md was independently
checked while deriving this note. Its arithmetic theorem passes:
for n>=3, n=0 modulo 3,


$$
v_3(q_n)=2v_3(n!)+v_3(\Delta_n)\ge2v_3(n!)
 \quad\text{if }\Delta_n\ne0.                             \tag{21}
$$


Only s=0 survives in A, only s=0,1 in B, giving
(H,K,A,B,C)=(1,1,1,0,1) modulo 3. The strict factorial/logarithmic
comparison removes the second-kind part. Delta is divisible by 3
because P_{n+1}=-P_n modulo 3. This proves the numerator claim
without assuming all-index normality; eventual nonvanishing is
already available. The separate dyadic combination in that source
depends on its own proof and is not re-proved here.

Equations (8)–(9) are the main new uniform residue-one arithmetic
lemma. Equations (15)–(20) explain precisely why 3 differs from all
odd primes >=5. These results do not by themselves prove
irrationality or whole-family exclusion.

