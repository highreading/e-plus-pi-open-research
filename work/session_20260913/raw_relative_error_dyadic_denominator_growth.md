> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Denominator growth and neighboring odd factors forced by the actual relative error

Date: 2026-09-13. Original bounded continuation by audit_sources.
Independent review requested.

This note combines two proved facts about the same actual endpoint rational:
the exact dyadic denominator theorem in raw_arctan_endpoint_dyadic_attempt.md,
and the even-degree relative-error theorem in
raw_even_endpoint_residue_asymptotic.md, whose full passing audit is
raw_even_endpoint_residue_independent_review.md. No assumption about
odd-prime saturation is made.

Write


$$
S=e+\pi,\qquad
 \frac{p_n}{q_n}=\frac{N_n}{Z_n},\qquad q_n>0,\quad
 \gcd(p_n,q_n)=1,
$$


where the sign of $Z_n$ has been absorbed into the numerator and
denominator. The raw type-I convention uses the negative of this
numerator, which does not affect any valuation below. Put


$$
\rho=\frac{\sqrt5-1}{2},\quad \phi=\rho^{-1},\quad
 C=4\pi\rho A_s/B_s>0,\quad r=\rho^{10}\in(0,1).
$$


For even $n$,


$$
\epsilon_n=S-p_n/q_n
 =C(-1)^{n/2}\rho^{5n}(1+o(1)),                         \tag{1}
$$


and, in every degree,


$$
a_n=v_2(q_n)=n+2\left\lfloor\frac{n+2}{4}\right\rfloor.
                                                                    \tag{2}
$$


For $n\ge1$, $a_n>0$, so reducedness forces $p_n$ odd. Define the
positive odd integer $o_n=q_n/2^{a_n}$.

## 1. Exact adjacent determinant depth

For any two even indices $m>n\ge2$, set


$$
D_{n,m}=p_mq_n-p_nq_m
        =q_nq_m(\epsilon_n-\epsilon_m).
$$


Since $a_m>a_n$, its two integer terms have different dyadic
valuations. Thus, without an asymptotic argument,


$$
\boxed{v_2(D_{n,m})=a_n.}                              \tag{3}
$$


In particular $D_{n,m}\ne0$. For adjacent even indices,


$$
a_{n+2}-a_n=
 \begin{cases}4,&n\equiv0\pmod4,\\2,&n\equiv2\pmod4.\end{cases}          \tag{4}
$$


Equation (1) gives


$$
\boxed{|D_{n,n+2}|
 =C(1+r)q_nq_{n+2}\rho^{5n}(1+o(1)).}                  \tag{5}
$$


Its sign is eventually $(-1)^{n/2}$. Combining (3) and (5),


$$
q_nq_{n+2}\ \ge\
 \frac{2^{a_n}\phi^{5n}}{C(1+r)}(1+o(1)).               \tag{6}
$$


Here and below an inequality with $1+o(1)$ means that its positive
right-hand side is multiplied by a real factor tending to one.

## 2. A rigorous lower bound on denominator growth

For even $n$, $a_n/n\to3/2$. Taking logarithms in (6) gives


$$
\liminf_{\substack{n\to\infty\\n\ {\rm even}}}
 \frac{\log q_n+\log q_{n+2}}n
 \ge \frac32\log2+5\log\phi.
$$


If the limsup of $\log q_n/n$ were smaller than half this value, an
eventual bound for each of the two neighboring terms would contradict
the display. Consequently


$$
\boxed{\limsup_{\substack{n\to\infty\\n\ {\rm even}}}q_n^{1/n}
 \ge \Gamma:=2^{3/4}\phi^{5/2}.}                        \tag{7}
$$


The exact constant is approximately $5.60069$; this decimal is only a
description of the displayed algebraic constant.

Since $2^{a_n/n}\to2^{3/2}$, multiplication by this convergent positive
factor commutes with the limsup, including an infinite limsup. Thus


$$
\boxed{\limsup_{\substack{n\to\infty\\n\ {\rm even}}}o_n^{1/n}
 \ge \Omega:=\frac{\phi^{5/2}}{2^{3/4}}.}                \tag{8}
$$


Here $\Omega$ is approximately $1.98014$. These are limsup statements;
neither is a bound for every individual index or every subsequence.
They remain below the sufficient primitive-shrinking threshold
$\phi^5$, and do not decide whether a shrinking subsequence exists.

## 3. Full gcd normalization strengthens the pairwise restriction

Let $H_{n,m}=\gcd(o_n,o_m)$. The full denominator gcd is


$$
\gcd(q_n,q_m)=2^{a_n}H_{n,m}.
$$


It divides $D_{n,m}$, and the quotient is odd by (3). Hence


$$
\boxed{\frac{D_{n,m}}{2^{a_n}H_{n,m}}
 \text{ is a nonzero odd integer}.}                    \tag{9}
$$


Equivalently, the rational spacing obeys


$$
|\epsilon_n-\epsilon_m|
 \ge\frac1{\operatorname{lcm}(q_n,q_m)}.                \tag{10}
$$



For $m=n+2k$, $k\ge1$, (1) implies the uniform estimate


$$
|\epsilon_n-\epsilon_m|
 =C\rho^{5n}\bigl(1-(-1)^kr^k\bigr)(1+o(1)),           \tag{11}
$$


where the error tends to zero uniformly in all $m>n$ even. Indeed,
write (1) with errors $\eta_j$, and bound them by
$\sup_{j\ge n,\ j\ {\rm even}}|\eta_j|\to0$. The main factor in (11)
lies between $1-r^2$ and $1+r$, so the absolute error is also a
uniform relative error.

Therefore


$$
\operatorname{lcm}(o_n,o_m)
 \ge
 \frac{\phi^{5n}}{C\,2^{a_m}(1-(-1)^kr^k)}(1+o(1)),     \tag{12}
$$


and


$$
q_nq_m
 \ge
 \frac{2^{a_n}H_{n,m}\phi^{5n}}
 {C(1-(-1)^kr^k)}(1+o(1)).                             \tag{13}
$$


This includes all exponents of the common odd factors. There is no
replacement of a full gcd by its radical.

For adjacent pairs, put


$$
h=\limsup_{\substack{n\to\infty\\n\ {\rm even}}}
        \frac{\log H_{n,n+2}}n\in[0,\infty].
$$


The same comparison of (13) with an eventual upper bound for each
denominator yields the conditional strengthening


$$
\limsup_{n\ {\rm even}}\frac{\log q_n}{n}
 \ge \frac34\log2+\frac52\log\phi+\frac h2.              \tag{14}
$$


For $h=\infty$, this says the left side is infinite. No positive value
of $h$ is established here. Thus a new lower bound for the shared odd
part of neighboring denominators would improve (7), while (7) itself
uses only $h\ge0$.

Fixed nonadjacent gaps, or gaps $m-n=o(n)$, give the same exponential
constant $\Gamma$ without extra gcd information. If instead
$m/n\to\lambda>1$, the denominator-product argument alone gives only
$(2^{3/2}\phi^5)^{1/(1+\lambda)}$, a weaker constant. No improvement
is obtained by silently treating widely separated indices as adjacent.

## 4. A necessary odd-factor condition for a shrinking subsequence

Let


$$
\ell_n=q_nS-p_n=q_n\epsilon_n.
$$


For large even $n$, this is nonzero by (1). Use the exact spacing
inequality (10), first with $n-2,n$, and then with $n,n+2$.
After cancelling the denominators it gives


$$
|\ell_n|\ge
 \frac{H_{n-2,n}}{o_{n-2}}\,
 \frac{|\epsilon_n|}{|\epsilon_{n-2}-\epsilon_n|},
$$




$$
|\ell_n|\ge
 2^{a_n-a_{n+2}}\frac{H_{n,n+2}}{o_{n+2}}\,
 \frac{|\epsilon_n|}{|\epsilon_n-\epsilon_{n+2}|}.
$$


The two error ratios in these displays tend respectively to
$r/(1+r)$ and $1/(1+r)$. Thus


$$
\boxed{
 \frac{o_{n-2}}{\gcd(o_{n-2},o_n)}
 \ge \frac{r}{1+r}\,\frac{1+o(1)}{|\ell_n|},}            \tag{15}
$$




$$
\boxed{
 \frac{o_{n+2}}{\gcd(o_n,o_{n+2})}
 \ge \frac{2^{a_n-a_{n+2}}}{1+r}\,
       \frac{1+o(1)}{|\ell_n|}.}                        \tag{16}
$$


The dyadic factor in (16) is exactly $1/16$ or $1/4$, according
to (4). Therefore if $\ell_n\to0$ along any even subsequence, both
integer quotients in (15)--(16) must tend to infinity on that same
subsequence. If $|\ell_n|\le e^{-\delta n}$, they must both be at least
a fixed positive multiple of $e^{\delta n}$ eventually.

This is a necessary restriction on the portions of the neighboring odd
denominators absent from the central denominator. It is not a claim
that those portions actually grow. For example, if
$o_{n-2}\mid o_n$ along a proposed shrinking subsequence, (15) rules
that subsequence out. Likewise bounded values of either quotient rule
out primitive shrinkage there. No such divisibility or boundedness
property is proved for the actual family here.

For an arbitrary later even $m$, one also has


$$
q_m\ge
 \frac{2^{a_n}H_{n,m}}
 {|\ell_n|\,|1-\epsilon_m/\epsilon_n|}.                 \tag{17}
$$


Its odd-part version contains the essential factor $2^{a_n-a_m}$.
It cannot be discarded when the gap grows.

## 5. Scope

The new results are the exact normalized determinant depth, the lower
growth constants (7)--(8), and the neighboring odd-factor conditions
(12)--(16). They use the actual reduced endpoint rational and therefore
retain every common factor already cancelled from the raw construction.
They are compatible with both rationality and irrationality of $e+\pi$.
The known asymptotic and these arithmetic restrictions still do not
prove $q_n\rho^{5n}\to0$ on any subsequence.
