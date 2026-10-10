> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An exact positive quadratic Robin correction, and why it cannot shrink

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
t=1-x,\qquad w=1-i,\qquad a_N=N!,
$$



and let



$$
P_N^{(0)}(x)
 =N!\sum_{j=0}^{N-1}\frac{(1-x)^j}{(j+1)!}.
                                                                    \tag{1}
$$



For the Stein operator



$$
{\cal T}P=(1-x)P'-xP,
$$



the exact near-solution is



$$
a_N+{\cal T}P_N^{(0)}=t^N.                \tag{2}
$$



This note solves the previously open local correction problem, but the
solution exposes a primitive-invariant barrier rather than a small linear
form.

Write



$$
w^N=R_N+iI_N,\qquad M_N=N!-R_N.                           \tag{3}
$$



For every integer $q$, define the quadratic correction



$$
C_{N,q}(t)
 =I_N-4q+\left(q-\frac{M_N}{2}\right)t-qt^2.               \tag{4}
$$



Then



$$
P_{N,q}(x)=P_N^{(0)}(x)+C_{N,q}(1-x)                     \tag{5}
$$



is an integer polynomial satisfying both Robin conditions, and its
residual is



$$
\boxed{
 F_{N,q}(x)
 =t^N+M_Nt\left(1-\frac t2\right)
      -I_N(1-t)+q(4-6t+4t^2-t^3).}                         \tag{6}
$$



Every integer correction of degree at most two is obtained uniquely in
this way.

There is an all-$N$ positive choice:



$$
q_N=
 \begin{cases}
 0,&I_N\leq0,\\
 \lceil I_N/3\rceil,&I_N>0.
 \end{cases}                                                \tag{7}
$$



For this choice,



$$
F_{N,q_N}\geq
 M_Nt\left(1-\frac t2\right)\geq0
 \qquad(0\leq t\leq1).                                     \tag{8}
$$



Thus the Robin defect can be repaired by a quadratic, sparse, integral
correction while retaining positivity.  The residual has at most five
nonzero monomials in $t$.

However, no positive member of the entire quadratic family can shrink
after exact antiderivative clearing and primitive normalization.  If
$\Lambda_{N,q}>0$ denotes that fully primitive output, then



$$
\boxed{
 \liminf_{\substack{N\to\infty\\F_{N,q}\geq0}}
            \Lambda_{N,q}
 \geq\pi-\frac32>0.}                                       \tag{9}
$$



More generally, corrections of any fixed bounded degree have a positive
primitive gap depending only on that degree.  Therefore a viable Robin
repair must have correction degree tending to infinity.  The arguments
do not exclude growing-degree sparse corrections, a large nonlocal
correction, or an exceptional construction with new structure.

In fact (30) below shows that the unnormalized positive integral grows on
the factorial scale.  Multiplication by the antiderivative denominator
cannot make it smaller; even after removing all output content, (9)
leaves a positive gap.

This package proves neither irrationality nor transcendence of
$e+\pi$.

## 2. The Stein operator in the $t$-coordinate

If $C$ is written as a polynomial in $t=1-x$, then



$$
{\cal T}C=-tC'(t)-(1-t)C(t).                               \tag{10}
$$



For



$$
U(t)=t-\frac12t^2,\qquad
 J(t)=4-6t+4t^2-t^3,                                      \tag{11}
$$



direct substitution into (10) gives



$$
\begin{aligned}
 {\cal T}C_{N,q}
 &=-I_N+4q+(M_N+I_N-6q)t\\
 &\quad+\left(-\frac{M_N}{2}+4q\right)t^2-qt^3\\
 &=M_NU(t)-I_N(1-t)+qJ(t).                                \tag{12}
\end{aligned}
$$



The coefficient $M_N/2$ is integral.  This is immediate for $N=1$.
For $N\geq2$, $N!$ is even and
$w^N$ is divisible by $w^2=-2i$ in $\mathbb Z[i]$, so $R_N$
is even.

The three elementary identities



$$
\begin{aligned}
 A(U)&=0,& U(w)&=1,\\
 A(1-t)&=0,& 1-w&=i,\\
 A(J)&=0,& J(w)&=0                                        \tag{13}
\end{aligned}
$$



show that



$$
A({\cal T}C_{N,q})=0,\qquad
 ({\cal T}C_{N,q})(i)
     =M_N-iI_N=N!-w^N.                                    \tag{14}
$$



Equations (2), (12), and (14) prove



$$
A(F_{N,q})=F_{N,q}(i)=F_{N,q}(-i)=N!.               \tag{15}
$$



Consequently $P_{N,q}$ obeys the Robin conditions.  By the exact
integer Robin-lattice theorem, it has a unique representation



$$
P_{N,q}
 =(1+x^2)^2Q_{N,q}+u_{N,q}R_1+v_{N,q}R_2                 \tag{16}
$$



with



$$
R_1=1+2x+x^3,\qquad R_2=9x-x^2+4x^3,
$$



and $Q_{N,q}\in\mathbb Z[x]$, $u_{N,q},v_{N,q}\in\mathbb Z$.
Thus (4) is genuinely a correction inside the full lattice, not merely
an endpoint interpolation over $\mathbb Q$.

## 3. Exhaustion of every quadratic correction

Suppose another correction $C\in\mathbb Z[t]$, of degree at most two,
repairs (2), and put $H={\cal T}C$.  Then



$$
A(H)=0,\qquad H(w)=N!-w^N.             \tag{17}
$$



The difference between $H$ and the $q=0$ polynomial in (12) has
degree at most three, has $A$-value zero, and vanishes at both
$w$ and $\bar w$.  Since



$$
(t-w)(t-\bar w)=t^2-2t+2,                                \tag{18}
$$



the difference is $(ct+d)(t^2-2t+2)$.  Its $A$-value is
$4c+2d$, so $d=-2c$.  Hence it is an integer multiple of



$$
J(t)=(2-t)(t^2-2t+2).                   \tag{19}
$$



The integral inverse of the Stein operator is unique.  Comparing the
top coefficient shows that this integer multiple is precisely the
parameter $q$ in (4).  This proves that (4)--(6) exhaust all integral
quadratic corrections.

## 4. Positivity

For $0\leq t\leq1$,



$$
U(t)=t\left(1-\frac t2\right)\geq0.                       \tag{20}
$$



Also



$$
J(t)-3(1-t)
 =1-3t+4t^2-t^3
 =(1-t)^3+t^2\geq0.                                       \tag{21}
$$



For $N\geq3$, $N!>|w|^N=2^{N/2}$, so $M_N>0$: the inequality
starts at $3!=6>2^{3/2}$ and is preserved on multiplying the two sides
by $N+1>\sqrt2$.  The cases $N=1,2$ are immediate and have
$M_N\geq0$.

If $I_N\leq0$, take $q_N=0$; then
$-I_N(1-t)\geq0$.  If $I_N>0$, equations (7) and (21) give



$$
q_NJ(t)\geq I_N(1-t).                         \tag{22}
$$



Substitution into (6) proves (8).  Notice that no finite computation or
asymptotic sign inference enters this proof.

## 5. Exact output and the quadratic primitive gap

In the $t$-coordinate, the positive weight is



$$
\Omega(t)=e^{1-t}+\frac4{t^2-2t+2}.                       \tag{23}
$$



Three direct integrations give



$$
\begin{aligned}
 \int_0^1U(t)\Omega(t)\,dt
     &=\pi-\frac32=:c_0,\\
 \int_0^1(1-t)\Omega(t)\,dt
     &=1+2\log2=:c_1,\\
 \int_0^1J(t)\Omega(t)\,dt
     &=10.                                                  \tag{24}
\end{aligned}
$$



For example, $U=1-(t^2-2t+2)/2$ gives the rational-kernel
contribution $\pi-2$, while its exponential contribution is $1/2$.
Also $J=(2-t)(t^2-2t+2)$, so its rational-kernel contribution is
$6$; its exponential contribution is $4$.

Let



$$
L_{N,q}=\int_0^1F_{N,q}(x)
       \left(e^x+\frac4{1+x^2}\right)dx.
$$



Equation (6) gives the exact decomposition



$$
L_{N,q}
 =M_Nc_0+\int_0^1t^N\Omega(t)\,dt-I_Nc_1+10q.             \tag{25}
$$



If $F_{N,q}\geq0$, evaluation at $t=0$ forces



$$
q\geq I_N/4.                       \tag{26}
$$



The strict inequality



$$
\log2<\frac34                                             \tag{27}
$$



follows, for instance, because the trapezoidal rule overestimates the
integral of the strictly convex function $1/x$ on $[1,2]$.
Thus



$$
\eta:=\frac52-c_1=\frac32-2\log2>0.                       \tag{28}
$$



If $I_N\geq0$, (26) makes
$-I_Nc_1+10q\geq\eta I_N$; if $I_N<0$, it makes the same expression
at least $-\eta|I_N|$.  Hence, after dropping the positive $t^N$
integral, (25) gives



$$
L_{N,q}\geq M_Nc_0-\eta|I_N|.       \tag{29}
$$



Since $|R_N|,|I_N|\leq2^{N/2}$,



$$
\liminf_{\substack{N\to\infty\\F_{N,q}\geq0}}
                  \frac{L_{N,q}}{N!}
 \geq\pi-\frac32.                                         \tag{30}
$$



For the explicit choice (7), the pointwise inequality (8) gives the
slightly sharper finite bound



$$
L_{N,q_N}\geq M_N\left(\pi-\frac32\right).
                                                                    \tag{31}
$$



It remains to check that denominator clearing and content removal cannot
invalidate this obstruction.  Put



$$
G_{N,q}(x)=\frac{F_{N,q}(x)-N!}{1+x^2}\in\mathbb Z[x],
                                                                    \tag{32}
$$



and let



$$
D_P=\operatorname {lcm}_{g_j\ne0}
       \frac{j+1}{\gcd(j+1,g_j)},
 \qquad G_{N,q}=\sum_jg_jx^j.                              \tag{33}
$$



The exact rational coordinate is



$$
\rho_{N,q}
 =-N!-P_{N,q}(0)+4\sum_j\frac{g_j}{j+1}
 =\frac BD,\qquad \gcd(B,D)=1,\quad D>0.                  \tag{34}
$$



One has $D\mid D_P$.  If



$$
h=\gcd(N!D,B)=\gcd(N!,B),
$$



then $h\mid N!$, and the primitive output is exactly



$$
\Lambda_{N,q}
 =\frac{N!D}{h}(e+\pi)+\frac Bh
 =\frac D hL_{N,q}>0.                                     \tag{35}
$$



If one first clears by $D_P$, the content of the pair



$$
\left(N!D_P,\frac{D_P}{D}B\right)
$$



is exactly



$$
c_P=\frac{D_P}{D}h.                  \tag{36}
$$



Thus surplus antiderivative clearing cancels exactly during primitive
reduction.  Since $D\geq1$ and $h\leq N!$,



$$
\Lambda_{N,q}\geq\frac{L_{N,q}}{N!}.\tag{37}
$$



Equations (30) and (37) prove the primitive gap (9).  This is why even
factorial-scale output content cannot rescue a positive quadratic
correction.

## 6. Every uniformly bounded-degree correction has a primitive gap

There is a broader barrier which does not use the explicit quadratic
formulas.  Fix $m\geq0$.  Let $C_N\in\mathbb Z[x]$ have degree at
most $m$, put



$$
H_N={\cal T}C_N,\qquad F_N=t^N+H_N,
$$



and suppose



$$
F_N\geq0\text{ on }[0,1],\qquad
 F_N(i)=F_N(-i)=A(F_N)=N!.                                \tag{38}
$$



Set $d=m+1$ and



$$
K_N=H_N+1.
$$



Because $0\leq t^N\leq1$, positivity of $F_N$ gives
$K_N\geq0$ on $[0,1]$.  Moreover,



$$
\deg K_N\leq d,\qquad
 K_N(i)=N!-w^N+1.                                         \tag{39}
$$



Let



$$
R=4.61158178930871498088\ldots,\qquad C_R=\frac R{R-1},
$$



be the interval-capacity constant from the common-kernel endpoint
bootstrap.  The one-variable Bernstein--Walsh estimate gives



$$
|K_N(i)|\leq C_RR^d\|K_N\|_{[0,1]}.                       \tag{40}
$$



The shifted Markov inequality for the nonnegative polynomial $K_N$
gives



$$
\int_0^1K_N(x)\,dx
 \geq\frac{\|K_N\|_{[0,1]}}{8d^2}.                         \tag{41}
$$



Since



$$
\int_0^1F_N(x)\,dx
 =\int_0^1K_N(x)\,dx-1+\frac1{N+1}
$$



and the weight is at least $3$, equations (40)--(41) imply



$$
L(F_N)\geq
 3\left\{
 \frac{|N!-w^N+1|}{8d^2C_RR^d}
 -1+\frac1{N+1}
 \right\}.                                                  \tag{42}
$$



After exact primitive normalization, the same content argument as
(35)--(37) gives



$$
\Lambda(F_N)\geq\frac{L(F_N)}{N!}.
$$



Therefore, for every fixed $m$,



$$
\boxed{
 \liminf_{N\to\infty}\Lambda(F_N)
 \geq\frac3{8(m+1)^2C_RR^{m+1}}>0.}                        \tag{43}
$$



No uniformly bounded-degree correction of the Taylor near-solution can
produce a shrinking primitive output.  This theorem includes every
fixed sparse correction whose monomial degrees remain bounded.  It does
not include a fixed-number-of-terms correction whose exponents tend to
infinity.

## 7. Replay and scope

From the research directory run

    python3 scripts/common_kernel_stein_robin_quadratic_correction_certificate.py
    sha256sum -c results/common_kernel_stein_robin_quadratic_correction_hashes.sha256

The deterministic replay verifies the correction formulas, common
endpoint equalities, positivity decomposition, complete quadratic
parameterization, Robin-lattice division, exact $D_P,D,h,c_P$, and
primitive pairs through $N=80$.  It also checks the three integral
coordinates in (24) exactly.  Finite computations certify the displayed
normalizations and arithmetic examples only; all-degree statements are
the proofs above.

The package constructs a positive correction but proves that this local
success cannot yield a small primitive linear form.  Growing-degree
corrections and genuinely nonlocal mechanisms remain open.  No statement
about the arithmetic nature of $e+\pi$ follows.
