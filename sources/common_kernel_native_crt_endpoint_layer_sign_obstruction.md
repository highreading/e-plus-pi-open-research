> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The native endpoint layer defeats the critical full-window CRT localizer

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
u=1+x^2,\qquad t=1-x,\qquad
 {\cal T}P=(1-x)P'-xP,
$$





$$
(1-i)^N=R_N+iI_N,\qquad M_N=N!-R_N,
$$





$$
K_N(x)=I_N-\frac{M_N}{2}(1-x)\qquad(N\geq2).           \tag{1}
$$



The critical full-window CRT construction for this linear correction has



$$
B_q(x)=x^{20q}(5q+1-5qx^4),                            \tag{2}
$$





$$
w_q(x)=x^{12q-8}(1-x^4)^{4q}(1-x^2),                  \tag{3}
$$





$$
h_q(x)=B_q(x)\{1-E_q(x)\},\qquad
 E_q(x)=u^2w_q(x)C_q(x).                                \tag{4}
$$



Here $C_q\in\mathbb Z_{\geq0}[x]$ is supported on



$$
\{1,2,3,5,6,7,9,10,11\}.                              \tag{5}
$$



Let



$$
P_q=\prod_{(48q+14)/3<p<20q}p,\qquad
 m_q=\#\{p:(48q+14)/3<p<20q\}.                          \tag{6}
$$



The CRT construction gives, independently of the size of the
coefficients of $K_N$,



$$
\sum_j[x^j]C_q\leq(2m_q+1)P_q.                        \tag{7}
$$



It also gives



$$
h_q\equiv1\pmod {u^2},\qquad h_q(0)=0,\qquad
 0\leq h_q\leq1\quad\hbox{on }[0,1],                   \tag{8}
$$





$$
\operatorname {ord}_0h_q=20q,\qquad
 \deg h_q=48q+13.                                      \tag{9}
$$



The purpose of the construction was to cancel every prime in the full
one-third output-denominator window (6).  Algebraically, that
cancellation is valid.  This note proves that it is incompatible with
the missing native sign condition.

**Uniform CRT sign obstruction.**  There is an absolute $q_0$ such
that, for every $q\geq q_0$, every $N\geq2$, and every
nonnegative $C_q$ satisfying (5)--(7), the native residual



$$
F_{N,q}(x)=(1-x)^N+{\cal T}(h_qK_N)(x)                 \tag{10}
$$



changes sign on $[0,1]$.  More precisely,



$$
F_{N,q}(0)=1,                                         \tag{11}
$$



and either $F_{N,q}(1)=-I_N<0$, or, at the fixed endpoint-layer
point



$$
x_q=1-\frac1{5q},                                     \tag{12}
$$



one has



$$
F_{N,q}(x_q)<0.                                       \tag{13}
$$



Thus no member of the existing degree-$48q+13$, order-$20q$
full-window CRT family is a sign-controlled native common-kernel form
for all sufficiently large $q$.  In particular, the algebraic
denominator cancellations in (6) cannot be combined with the positive
integral needed by this construction.

The argument is uniform in $N$.  It does not merely compare $q$
with the factorial coefficients in $K_N$: the endpoint-layer
perturbation is small relative to both independent native coefficients
$-I_N$ and $M_N/2$.

This is a scoped obstruction for (2)--(7).  It does not exclude a
different critical-ratio localizer, and it does not classify
$e+\pi$.

## 2. Exact native differential form

Write



$$
H(t)=h(1-t),\qquad a=-I_N,\qquad b=\frac{M_N}{2}.
$$



For $N\geq2$, $M_N$ is a positive even integer, so $b\geq1$.
Direct substitution in (1) gives



$$
\boxed{
 F_{N,h}(1-t)
 =t^N+t(a+bt)H'(t)
  +\{a(1-t)+bt(2-t)\}H(t).}                             \tag{14}
$$



If $I_N>0$, then $F_{N,q}(1)=-I_N<0$, while (9) gives
$F_{N,q}(0)=1$.  Hence only the case



$$
a=-I_N\geq0                                           \tag{15}
$$



needs further analysis.

Let



$$
H_{B,q}(t)=B_q(1-t).
$$



At



$$
t_q=\frac1{5q},\qquad x_q=1-t_q,
$$



put



$$
\lambda_q
 =-\frac{H_{B,q}'(t_q)}{H_{B,q}(t_q)}
 =\frac{B_q'(x_q)}{B_q(x_q)}.                           \tag{16}
$$



The base polynomial has the exact logarithmic derivative



$$
\lambda_q
 =\frac{20q(5q+1)(1-x_q^4)}
        {x_q\{1+5q(1-x_q^4)\}}.                         \tag{17}
$$



## 3. A rational slope inequality at $t=1/(5q)$

Put $y=1/(5q)$ and



$$
A(y)=4-6y+4y^2-y^3,
\qquad 1-(1-y)^4=yA(y).
$$



Equation (17) becomes



$$
t_q\lambda_q
 =\frac{4(1+y)A(y)}
        {(1-y)\{1+A(y)\}}.                              \tag{18}
$$



For $0<y\leq1/5$, the difference between the left numerator in
(18) and three times its denominator is



$$
1+25y-38y^2+27y^3-7y^4>0.                             \tag{19}
$$



Indeed,
$38y^2\leq(38/5)y$ and $7y^4\leq(7/125)y$.
Thus



$$
t_q\lambda_q\geq3.                                    \tag{20}
$$



For $q\geq2$, one also has $y\leq1/10$, and



$$
5(1-y)\{1+A(y)\}-4(1+y)A(y)
 =5(1-y)+(1-9y)A(y)>0.
$$



Hence



$$
\boxed{3\leq t_q\lambda_q\leq5\qquad(q\geq2).}         \tag{21}
$$



There is also a uniform lower bound for the base value.  Since
$\log(1-y)\geq-y/(1-y)$,



$$
\begin{aligned}
 H_{B,q}(t_q)
 &=x_q^{20q}\{1+5q(1-x_q^4)\}\\
 &\geq x_q^{20q}\geq e^{-5}.                            \tag{22}
\end{aligned}
$$



## 4. The unperturbed residual is uniformly negative

Let $F_{B,N,q}$ be the right side of (14) with
$H=H_{B,q}$.  Since $H_{B,q}'=-\lambda_qH_{B,q}$,



$$
\begin{aligned}
 F_{B,N,q}(x_q)
 ={}&t_q^N\\
 &+aH_{B,q}(t_q)\{1-t_q-t_q\lambda_q\}\\
 &+bH_{B,q}(t_q)t_q\{2-t_q-t_q\lambda_q\}.
                                                               \tag{23}
\end{aligned}
$$



Equation (21) implies



$$
F_{B,N,q}(x_q)
 \leq t_q^N-H_{B,q}(t_q)(2a+bt_q).                     \tag{24}
$$



Uniformly for every $N\geq2$, $t_q^N\leq t_q^2$.  By
(22), $b\geq1$, and $t_q\to0$, one has, for all sufficiently
large $q$,



$$
t_q^N\leq\frac12bt_qH_{B,q}(t_q).
$$



Consequently



$$
\boxed{
 F_{B,N,q}(x_q)
 \leq-2aH_{B,q}(t_q)
     -\frac12bt_qH_{B,q}(t_q).}                         \tag{25}
$$



This estimate is uniform in $N$, $a$, and $b$ under (15) and
$b\geq1$.

## 5. The CRT correction is superexponentially invisible there

Let



$$
\epsilon_q(t)=E_q(1-t).
$$



The prime number theorem applied to (6) gives



$$
\log P_q
 =\vartheta(20q)
  -\vartheta((48q+14)/3)
 =4q+o(q).                                              \tag{26}
$$



Also $\log(2m_q+1)=o(q)$, so (7) gives



$$
\log\sum_j[x^j]C_q\leq4q+o(q).                         \tag{27}
$$



At $x_q$,



$$
1-x_q^4\leq4t_q=\frac4{5q}.
$$



Since $u^2\leq4$, $x_q^{12q-8}\leq1$,
$1-x_q^2\leq1$, and $C_q(x_q)$ is bounded by its
coefficient sum, equations (26)--(27) give, when $C_q\ne0$,



$$
\begin{aligned}
 0\leq\epsilon_q(t_q)
 &\leq4(2m_q+1)P_q
       \left(\frac4{5q}\right)^{4q},\\
 \log\epsilon_q(t_q)
 &\leq-4q\log q+O(q).                                  \tag{28}
\end{aligned}
$$



When $C_q=0$, the correction and its derivative vanish identically,
so the conclusions below are immediate.  Assume henceforth that
$C_q\ne0$.

The same is true after one derivative, up to a polynomial factor.
Its nonnegative coefficients and (5) give



$$
\frac{C_q'(x_q)}{C_q(x_q)}
 \leq\frac{11}{x_q}.
$$



Logarithmically differentiating (4), and using
$x_q\geq4/5$ and $1-x_q^4\geq t_q$, yields



$$
\begin{aligned}
 \frac{|E_q'(x_q)|}{E_q(x_q)}
 &\leq
 \frac{4x_q}{1+x_q^2}
 +\frac{12q-8}{x_q}
 +\frac{16q x_q^3}{1-x_q^4}\\
 &\quad+\frac{2x_q}{1-x_q^2}
 +\frac{11}{x_q}\\
 &\leq120q^2.                                           \tag{29}
\end{aligned}
$$



Since $|\epsilon_q'(t_q)|=|E_q'(x_q)|$, equations (28)--(29) prove



$$
\boxed{
 J_q:=7\epsilon_q(t_q)
       +t_q|\epsilon_q'(t_q)|
 \longrightarrow0.}                                    \tag{30}
$$



The crucial point is the factor
$(1-x^4)^{4q}$: at distance $1/(5q)$ from the endpoint it beats
the complete CRT coefficient budget by a factor
$\exp(-4q\log q+O(q))$.

## 6. Perturbation audit and sign change

Write at $t=t_q$



$$
H(t)=H_{B,q}(t)\{1-\epsilon_q(t)\}.
$$



Then



$$
H-H_{B,q}=-H_{B,q}\epsilon_q,
$$





$$
H'-H_{B,q}'
 =H_{B,q}\{\lambda_q\epsilon_q-\epsilon_q'\}.           \tag{31}
$$



Subtracting (23) from the exact native expression (14), and using
(21), gives



$$
\begin{aligned}
 |F_{N,q}(x_q)-F_{B,N,q}(x_q)|
 &\leq H_{B,q}(t_q)J_q(a+bt_q).                         \tag{32}
\end{aligned}
$$



For all sufficiently large $q$, equation (30) gives $J_q\leq1/4$.
Combining (25) and (32) yields



$$
\begin{aligned}
 F_{N,q}(x_q)
 &\leq
 -\frac74aH_{B,q}(t_q)
 -\frac14bt_qH_{B,q}(t_q)<0.                            \tag{33}
\end{aligned}
$$



This proves (13) in the remaining case $I_N\leq0$.  Finally, (9)
implies $h_q(0)=h_q'(0)=0$, and direct evaluation of (10) gives
$F_{N,q}(0)=1$.  Therefore the residual changes sign.

## 7. Exact scope

The proof uses all three pieces of the existing CRT architecture:

1. the beta-type base $B_q$;
2. the padding factor $(1-x^4)^{4q}$; and
3. the uniform coefficient budget (7).

It does not assert that positivity alone forces a prime of (6) back
into the denominator.  Instead it proves something stronger for this
family: the algebraically successful CRT localizer cannot satisfy the
native sign hypothesis in the first place.

A different critical-ratio construction could evade the theorem by
changing its endpoint profile, activating its correction on the
$1/q$ layer, or exceeding the coefficient budget (7).  Such a
construction would require a new positivity and arithmetic audit.

## 8. Replay

The companion certificate

    scripts/common_kernel_native_crt_endpoint_layer_sign_obstruction_certificate.py

checks with exact rational arithmetic:

1. the Gaussian recurrence and native differential identity (14);
2. the exact slope formula (18) and both inequalities in (21);
3. the base estimate (23)--(25);
4. the coefficient-budget bound (28) and logarithmic derivative bound
   (29) on a finite exact grid; and
5. the perturbation identity (31)--(32) for nonnegative test
   polynomials supported on (5).

The finite replay checks normalizations.  The all-parameter theorem is
the proof above.  It uses no hardware accelerator and stays far below
$2$ GiB RAM.
