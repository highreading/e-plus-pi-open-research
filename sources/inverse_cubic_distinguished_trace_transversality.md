> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Distinguished inverse branch versus the trace line

## 1. Theorem and scope

Let



$$
n=6m,\qquad A(t)=-2+3t-t^2,\qquad
 \phi(t)=t^3-2t^2+2t,
$$



and let $F_0(z)=A(T_0(z))^n/\phi'(T_0(z))$, where
$T_0(0)=0$.  Let



$$
S_m(z)=\sum_{\phi(T_i)=z}\frac{A(T_i(z))^n}{\phi'(T_i(z))}
$$



be the trace polynomial, and write $f=(f_0,f_1,f_2)$ and
$\tau=(\tau_0,\tau_1,\tau_2)$ for the first three coefficients of
$F_0$ and $S_m$, respectively.

After removing a power of two from $f$, put



$$
V=(32,\ 32-24n,\ 9n^2-41n+36).
$$



Then $f=2^{n-6}V$.  The exact gcd of the three $2\times2$
minors of the two rows $\tau,V$ is exactly



$$
\boxed{
 \gcd(\tau\wedge V)=
 \begin{cases}
  2^{3m},&m\text{ odd},\\[2mm]
  3\,2^{3m+4}m(3m-1),&m\text{ even}.
 \end{cases}}                                      \tag{1.1}
$$



Consequently, if $p>6m$ is prime, the distinguished initial line and
the trace initial line are not proportional modulo $p$.

Over an algebraic closure of $\mathbb F_p$, let
$\mathcal B_m$ be the span of the three genuine inverse-branch series
$F_0,F_\alpha,F_{\bar\alpha}$, and let


$$
\operatorname {ev}_{4m}:\mathcal B_m\longrightarrow
 \overline{\mathbb F}_p^3
$$


take the coefficients in degrees $4m,4m+1,4m+2$.  The inverse branches
exist because the three roots of $\phi$ are simple at every fresh prime.
Since $\operatorname {ev}_{4m}(S_m)=0$, a hypothetical target triple
zero for $F_0$ puts both $S_m$ and $F_0$ in the kernel.  The two
series are independent by (1.1), while $\dim\mathcal B_m\le3$.  Therefore



$$
\boxed{F_0\text{ target triple }=0\pmod p
        \quad\Longrightarrow\quad
        \operatorname {rank}
        (\operatorname {ev}_{4m}|_{\mathcal B_m})\le1.} \tag{1.2}
$$



This is a uniform intrinsic rank-drop theorem, not a contradiction: the
quotient map really does have valid-prime rank drops, as the separate
$m=2,p=112291$ certificate demonstrates.

The intrinsic formulation is essential on the ray $p=12m-1$.  There
$2n-1=0\pmod p$, the rational recurrence transfer from three arbitrary
initial coordinates has $p$-denominators, and the three-branch initial
matrix can lose rank.  No reduction of that rational transfer matrix is
asserted on this ray.  Statement (1.2) remains valid because it uses only
the genuine inverse branches and the two explicitly independent series
$F_0,S_m$.

## 2. Distinguished initial vector

Put $F=A(T)^n/\phi'(T)$.  Since $T'(z)=1/\phi'(T)$,



$$
\frac{F'}F=
 \frac{nA'/A-\phi''/\phi'}{\phi'}.
$$



At $T=0$, direct differentiation gives



$$
F(0)=2^{n-1},\qquad
 \frac{F'(0)}{F(0)}=1-\frac{3n}{4},
$$



and



$$
\frac{F''(0)}{2F(0)}=\frac{9n^2-41n+36}{32}.
$$



Therefore



$$
(f_0,f_1,f_2)
 =2^{n-6}(32,32-24n,9n^2-41n+36)=2^{n-6}V.       \tag{2.1}
$$



All discarded scalars are powers of two and hence units at fresh primes.

## 3. The two conjugate branches

The other roots of $\phi(t)=0$ are



$$
\alpha=1+i,\qquad \bar\alpha=1-i.
$$



For a root $r$, the coefficient of $z^j$ on its inverse branch is



$$
\operatorname {Res}_{t=r}
 \frac{A(t)^n}{\phi(t)^{j+1}}\,dt.
$$



Dividing the first three coefficients on the $\alpha$-branch by
$\alpha^n$ gives



$$
r_0=-\frac{1+i}{4},
$$





$$
r_1=\frac{3n-4}{16}-i\frac{n+2}{16},
$$





$$
r_2=\frac{-n^2+25n-36}{128}
      +i\frac{7n^2-21n-6}{128}.                    \tag{3.1}
$$



The $\bar\alpha$-branch is the conjugate.  Since $n=6m$,



$$
\alpha^n=(-8i)^m=8^m(-i)^m.
$$



Define the integer vectors



$$
A_m=(-32,\ 24n-32,\ -n^2+25n-36),
$$





$$
B_m=(-32,\ -8n-16,\ 7n^2-21n-6).
$$



The sum $g$ of the two conjugate-branch initial vectors is



$$
g=2^{3m-6}W_m,
$$



where



$$
W_m=
 \begin{cases}
  A_m,&m\equiv0\pmod4,\\
  B_m,&m\equiv1\pmod4,\\
  -A_m,&m\equiv2\pmod4,\\
  -B_m,&m\equiv3\pmod4.
 \end{cases}                                      \tag{3.2}
$$



Thus



$$
\tau=f+g=2^{6m-6}V+2^{3m-6}W_m,                 \tag{3.3}
$$



and $\tau\wedge V=2^{3m-6}(W_m\wedge V)$.

## 4. Primitive gcd for even m

For $W_m=\pm A_m$, direct expansion gives



$$
A_m\wedge V=
 \bigl(0,\ -3072m(3m-1),\
 1536m(3m-1)(9m-2)\bigr).                          \tag{4.1}
$$



If $m$ is even, $9m-2$ is even, so the gcd of the three entries in
(4.1) is



$$
3072m(3m-1)=3\,2^{10}m(3m-1).
$$



Multiplication by the factor in (3.3) proves the even case of (1.1).

## 5. Primitive gcd for odd m

For $W_m=\pm B_m$, expansion gives



$$
B_m\wedge V=64\bigl(
 8(12m-1),\
 -3(96m^2-62m+5),\
 6(2m-1)(3m-1)(9m-1)
 \bigr).                                           \tag{5.1}
$$



When $m$ is odd, the second entry inside the parentheses is odd, so no
factor 2 is common.  The first entry is congruent to 1 modulo 3, so no
factor 3 is common.  If an odd prime $\ell\ne3$ divided the first two
entries, then $12m\equiv1\pmod\ell$; substituting this into the quadratic
factor gives



$$
96m^2-62m+5\equiv\frac12\pmod\ell,
$$



a contradiction.  Hence the three normalized entries in (5.1) have gcd
one.  It follows that $\gcd(B_m\wedge V)=64$, and (3.3) proves the odd
case of (1.1).

## 6. Fresh-prime consequence

For even $m$, every odd factor displayed in (1.1) is among
$3,m,3m-1$, all strictly smaller than $6m<p$.  For odd $m$, the gcd
is a power of two.  Thus no fresh prime divides all three minors, proving
the asserted transversality and the intrinsic rank-drop implication (1.2),
including the degenerate ray $p=12m-1$.

The deterministic exact certificate is
`scripts/inverse_cubic_distinguished_trace_transversality.py`; its byte-stable
output is
`results/inverse_cubic_distinguished_trace_transversality.json`.
