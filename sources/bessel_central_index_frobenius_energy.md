> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The central Charlier obstruction: index Frobenius, a resonant ODE, and two exact no-go identities

Checked: 2026-08-27 UTC.

## 1. Scope and verdict

Put



$$
F_n(a)=\sum_{j=0}^n\binom nj(a)_{\underline j},
 \qquad
 P_n(t)=2^nF_n\!\left(\frac{t-1}{2}\right).
 \tag{1}
$$



Thus



$$
\sum_{n\geq0}P_n(t)\frac{x^n}{n!}
 =e^{2x}(1+2x)^{(t-1)/2},
 \tag{2}
$$



and



$$
P_0=1,\quad P_1=t+1,\qquad
 P_{n+1}=(t+1-2n)P_n+4nP_{n-1}.
 \tag{3}
$$



Write



$$
u_n=P_n(0),\qquad w_n=P_n'(0).
 \tag{4}
$$



For an odd prime $p=2m+1$, reduction of the diagonal Laguerre
quantities gives



$$
A_m\equiv 2^{-m}u_m,
 \qquad
 C_m\equiv 2^{1-m}w_m
 \pmod p.
 \tag{5}
$$



Equivalently, $A_m\equiv F_m(-1/2)$ and
$C_m\equiv F_m'(-1/2)$.  The displayed powers of two are units.
Consequently the remaining central question is whether $u_m$ and $w_m$
can vanish simultaneously modulo $p=2m+1$.

This note proves three new exact statements.

1. There is an exact index-addition identity for $F_{p+n}$, and an
   explicit correction modulo $p^2$ to the index-Frobenius factorization
   $F_{p+n}\equiv F_pF_n\pmod p$.
2. The central root and derivative conditions are exactly a resonance
   compatibility and an endpoint integral for a first-order polynomial ODE.
   The endpoint integral has an exact quadratic energy form, including
   the characteristic-$p$ top-coefficient anomaly that ordinary
   integration by parts would miss.
3. The symmetric terminating ${}_2F_0$ representation of the Bessel
   number has an explicit second-order Dwork-style block correction.

Each identity is rigorous.  None proves nonvanishing of the forbidden
Hensel digit.  In particular, the first identity introduces an unconstrained
index-correction residue, the energy form is isotropic, and the Dwork block
introduces an unconstrained next-block residue.  These are no-go conclusions,
not an all-prime theorem.

All rational congruences are in $\mathbb Z_{(p)}$.  Ordinary derivatives
are always derivatives in the displayed polynomial variable.  They must not
be confused with the argument-root Wronskian: ordinary simplicity of a
Laguerre polynomial in its argument does not imply simplicity of the
parameter lift considered here.

## 2. Exact index addition and Frobenius propagation

Vandermonde's identity and



$$
(a)_{\underline{k+r}}=(a)_{\underline r}
                         (a-r)_{\underline k}
$$



give, over $\mathbb Z[a]$,



$$
\boxed{
 F_{p+n}(a)=\sum_{r=0}^p\binom pr(a)_{\underline r}F_n(a-r).}
\tag{6}
$$



Indeed, expand $\binom{p+n}{j}$ as
$\sum_{r+k=j}\binom pr\binom nk$, and then sum first over $k$.
Since



$$
F_p(a)=\sum_{r=0}^p\binom pr(a)_{\underline r},
$$



subtracting $F_p(a)F_n(a)$ from (6) gives the stronger exact identity



$$
\boxed{
\begin{aligned}
 F_{p+n}(a)-F_p(a)F_n(a)
  ={}&(a)_{\underline p}\{F_n(a-p)-F_n(a)\}\\
   &+\sum_{r=1}^{p-1}\binom pr(a)_{\underline r}
                   \{F_n(a-r)-F_n(a)\}.
\end{aligned}}
\tag{7}
$$



Modulo $p$, (6) immediately yields



$$
\boxed{F_{p+n}(a)\equiv F_p(a)F_n(a)\pmod p.}
\tag{8}
$$



Here one may work in $\mathbb F_p[a]$: the intermediate binomial
coefficients vanish, $(a)_{\underline p}=a^p-a$, and
$F_n(a-p)=F_n(a)$.  In the scaled variable,



$$
P_p(t)\equiv t^p-t+2\pmod p,
 \tag{9}
$$



so at $t=0$,



$$
P_p(0)=2,\qquad P_p'(0)=-1\pmod p.
 \tag{10}
$$



It follows from (8) and its derivative that a simultaneous zero of
$(u_n,w_n)$ modulo $p$ propagates from $n$ to $n+p$.  This explains
the observed progression $317+401k$; it is not evidence that all roots are
simple.

## 3. The explicit correction modulo $p^2$

For $1\le r<p$,



$$
\frac1p\binom pr\equiv\frac{(-1)^{r-1}}r\pmod p,
 \qquad
 \frac{F_n(a-p)-F_n(a)}p\equiv-F_n'(a)\pmod p.
\tag{11}
$$



Therefore (7) proves



$$
\boxed{
 F_{p+n}(a)\equiv F_p(a)F_n(a)+p\mathcal E_{p,n}(a)
 \pmod {p^2},}
\tag{12}
$$



where the correction polynomial in $\mathbb F_p[a]$ is



$$
\boxed{
\begin{aligned}
 \mathcal E_{p,n}(a)={}&-(a)_{\underline p}F_n'(a)\\
 &+\sum_{r=1}^{p-1}\frac{(-1)^{r-1}}r
 (a)_{\underline r}\{F_n(a-r)-F_n(a)\}.
\end{aligned}}
\tag{13}
$$



Formula (13), rather than a Taylor expansion in the old parameter lift, is
the genuine first correction to index Frobenius.  Notice that although
$(a)_{\underline p}=0$ as a function on $\mathbb F_p$, its polynomial
derivative is $-1$; consequently one must retain the first line before
differentiating (13).

Let $\widetilde a_0\in\mathbb Z_{(p)}$ lift
$a_0\in\mathbb F_p$, and suppose $a_0$ is a double root of $F_n$.
Put



$$
X_n=\frac{F_n(\widetilde a_0)}p,\qquad
 Y_n=\frac{F_n'(\widetilde a_0)}p\pmod p.
$$



Since $F_p(a_0)=1$ and $F_p'(a_0)=-1$ in $\mathbb F_p$, (12) and its
ordinary derivative give



$$
\boxed{
\begin{aligned}
 \frac{F_{p+n}(\widetilde a_0)}p
   &\equiv X_n+\mathcal E_{p,n}(a_0),\\
 \frac{F_{p+n}'(\widetilde a_0)}p
   &\equiv-X_n+Y_n+\mathcal E_{p,n}'(a_0)
   \pmod p.
\end{aligned}}
\tag{14}
$$



Thus index propagation modulo $p$ does **not** propagate a double zero
modulo $p^2$ for free: after the displayed product contributions, the two
new digits contain the a priori independent correction residues in (14).
Nor does (14) impose an equation on the original forbidden digit, because
$F_{p+n}$ is a new index value.

The exact counterexample to global fixed-parameter simplicity illustrates
the distinction.  Integer recurrence gives



$$
\gcd(u_{317},w_{317})=1203=3\cdot401.
\tag{15}
$$



Modulo $401$, the consecutive pairs are



$$
\begin{array}{c|rrrrrr}
 n&313&314&315&316&317&318\\ \hline
 u_n&179&204&275&256&0&199\\
 w_n&223&385&0&165&0&299.
\end{array}
\tag{16}
$$



Modulo $401^2$, the lift digits at indices $317$ and $718=317+401$
are



$$
(u_{317}/401,w_{317}/401)\equiv(188,361),
 \quad
 (u_{718}/401,w_{718}/401)\equiv(233,111)
 \pmod {401}.
\tag{17}
$$



After removing the product contributions from (10), the two correction
digits are



$$
233-2\cdot188=258,
 \qquad
 111+188-2\cdot361=379
 \pmod {401}.
\tag{18}
$$



Both are nonzero.  This is a direct adversarial check that (12) is a
correction formula, not a hidden repeated-root theorem.

## 4. The central root as a resonant polynomial ODE

Let



$$
B_0=0,\qquad B_1=1,\qquad
 B_{r+1}=\frac{2r-1}{2r+1}(2B_r-B_{r-1}).
\tag{19}
$$



Its ordinary generating function satisfies



$$
\boxed{
 2z(1-z)^2B'(z)+(-1+2z+z^2)B(z)=z.}
\tag{20}
$$



For $p=2m+1$, all denominators occurring in $B_0,\ldots,B_m$ are
prime to $p$.  Define



$$
D_m=B_{m-1}-2B_m,
 \qquad
 \beta_m=\sum_{r=1}^m\frac{B_r}{r}.
\tag{21}
$$



Reversing the Laguerre recurrence at $x=-1$ proves



$$
L_m(-1)=0\pmod p\quad\Longleftrightarrow\quad D_m=0\pmod p.
\tag{22}
$$



For completeness, under a root normalize
$B_r=L_{m-r}(-1)/L_{m-1}(-1)$.  This gives (19), and the terminal values
$L_0(-1)=1,L_1(-1)=2$ give $D_m=0$.  Conversely, if the universal
solution (19) has $D_m=0$, then $B_m\ne0$, the rescaled reversed
sequence has the correct terminal values, and uniqueness of the Laguerre
recurrence gives a root at level $m$.

The standard generating-function differentiation identity



$$
\left.\frac{\partial}{\partial\alpha}L_m^{(\alpha)}(x)
 \right|_{\alpha=0}
 =\sum_{k=0}^{m-1}\frac{L_k(x)}{m-k}
\tag{23}
$$



then gives, under (22),



$$
\left.\partial_\alpha L_m^{(\alpha)}(-1)\right|_{\alpha=0}
 =L_{m-1}(-1)\beta_m.
\tag{24}
$$



Thus the forbidden simultaneous zero is exactly



$$
D_m=\beta_m=0\pmod p.
\tag{25}
$$



Now truncate $B(z)=\sum_{r=1}^mB_rz^r$ in $\mathbb F_p[z]$.  Direct
coefficient extraction from (20) gives



$$
2z(1-z)^2B'+(-1+2z+z^2)B-z
 =(2m-1)D_mz^{m+1}.
\tag{26}
$$



The nominal coefficient of $z^{m+2}$ is $(2m+1)B_m=0$.  Hence the
central root condition is precisely the resonance compatibility that makes
the truncated series an exact polynomial solution of (20).

## 5. Exact energy identity, and why it is not yet nonvanishing

Assume the root compatibility $D_m=0$, and put



$$
K(z)=B(z)/z.
\tag{27}
$$



Then $K$ has degree at most $m-1$, $K(0)=1$, and (20) becomes



$$
\boxed{
 2z(1-z)^2K'+(1-2z+3z^2)K=1.}
\tag{28}
$$



Also



$$
\beta_m=\int_0^1K(z)\,dz,
\tag{29}
$$



where integration means termwise polynomial integration in $\mathbb F_p$.
Multiplying (28) by $K$ almost permits an integration by parts, but a
characteristic-$p$ endpoint anomaly must be retained.  If $H$ has degree
at most $p$, termwise integration in $\mathbb F_p$ gives



$$
\int_0^1H'(z)\,dz=H(1)-H(0)-[z^p]H.
\tag{30}
$$



The last term occurs because $(z^p)'=0$, although $z^p$ has endpoint
difference one.  Here



$$
H(z)=2z(1-z)^2K(z)^2,
 \qquad [z^p]H=2B_m^2,
\tag{31}
$$



because $B_m$ is the leading coefficient of $K$.  Therefore



$$
\begin{aligned}
 \int_0^1K
 &=-B_m^2
   +\int_0^1\left\{1-2z+3z^2
      -\frac12(2z(1-z)^2)'\right\}K^2\\
 &=-B_m^2+2\int_0^1zK(z)^2\,dz.
\end{aligned}
$$



The ordinary endpoint term is zero because $z(1-z)^2$ vanishes at both
endpoints.  The largest degree in the final integral is
$1+2(m-1)=p-2$, so every remaining integration denominator is at most
$p-1$ and is invertible.  We have therefore proved the exact conditional
identity



$$
\boxed{
 \beta_m=2\int_0^1zK(z)^2\,dz-B_m^2\pmod p.}
\tag{32}
$$



Dropping the $-B_m^2$ term would give a false identity.  For the central
root $p=79,m=39$, for example,



$$
\beta_m=16,\qquad
 \int_0^1zK^2=5,\qquad B_m=51,
$$



and $2\cdot5-51^2=16\pmod {79}$.

There is no positivity in $\mathbb F_p$.  The unrestricted quadratic form



$$
R(f)=2\int_0^1zf(z)^2\,dz-\operatorname{lc}(f)^2
\tag{33}
$$



is already isotropic with the degree and endpoint conditions suggested by
(28).  For example, in $\mathbb F_{11}[z]$,



$$
f(z)=1+z^2+3z^3+z^4,
 \qquad f(0)=1,\quad f(1)=\frac12,\quad R(f)=0.
\tag{34}
$$



The full ODE (28), not merely its endpoint conditions, selects at most one
polynomial $K$ of degree at most $m-1$: the difference of two solutions
satisfies the homogeneous equation, whose coefficient recurrence starts
with $h_0=0$ and then has invertible diagonal coefficients
$2r+1$ for $0\le r\le m-1$.  On that selected solution, however, (32)
says exactly
that isotropy is equivalent to $\beta_m=0$, which is the original
forbidden condition (25).  Producing a compatible isotropic example would
therefore itself be a counterexample to the desired theorem.  None is known;
(32) does not independently rule one out.  The top-coefficient term is also
the precise place where a characteristic-zero/Faulhaber integration argument
loses the Frobenius contribution.

## 6. Symmetric terminating ${}_2F_0$ and the first Dwork block

Let



$$
a_j=\frac{(1/2)_j^2}{j!},
 \qquad
 T_m=\sum_{j=0}^m a_j.
\tag{35}
$$



The exact Bessel representation is



$$
(-1)^mq_m={}_2F_0(-m,m+1;;1)
 =\sum_{j=0}^m
 \frac{(1/2-p/2)_j(1/2+p/2)_j}{j!}.
\tag{36}
$$



For every $j\le m$,



$$
(1/2-p/2)_j(1/2+p/2)_j
 =(1/2)_j^2\prod_{r=0}^{j-1}
 \left(1-\frac{p^2}{(2r+1)^2}\right).
\tag{37}
$$



Moreover $a_j$ is divisible by $p^2$ for $m<j<p$.  Hence



$$
\boxed{
 (-1)^mq_m\equiv T_m\equiv\sum_{j=0}^{p-1}a_j\pmod {p^2}.}
\tag{38}
$$



This symmetry explains why there is no first-order parameter term in this
form of the lift.

For $p\ge5$, define the Wilson and Fermat quotients



$$
W_p=\frac{(p-1)!+1}{p},
 \qquad
 Q_p(16)=\frac{16^{p-1}-1}{p},
\tag{39}
$$



and, in $\mathbb F_p$,



$$
H_k=\sum_{r=1}^k\frac1r,
 \qquad
 O_k=\sum_{r=1}^k\frac1{2r-1}.
\tag{40}
$$



For $0\le k\le m$, a direct block calculation gives



$$
\boxed{
 \frac{a_{p+k}}{p a_k}
 \equiv-\frac14\left[
 1+p\{4O_k-H_k-W_p-Q_p(16)\}\right]
 \pmod {p^2}.}
\tag{41}
$$



To prove it, first use the exact ratio



$$
\frac{a_{p+k}/(pa_k)}{a_p/p}
 =\left(\frac{(p+1/2)_k}{(1/2)_k}\right)^2
   \frac{(1)_k}{(p+1)_k}.
\tag{42}
$$



Its right side is
$1+p(4O_k-H_k)\pmod {p^2}$.  Next,



$$
\frac{a_p}{p}
 =\frac{\binom{2p}{p}^2(p-1)!}{16^p}.
\tag{43}
$$



The elementary product
$\binom{2p}{p}=2\prod_{r=1}^{p-1}(1+p/r)$, together with
$H_{p-1}=0\pmod p$, gives
$\binom{2p}{p}=2\pmod {p^2}$.  Expanding (43) then gives



$$
\frac{a_p}{p}
 \equiv-\frac14\{1-p(W_p+Q_p(16))\}\pmod {p^2},
\tag{44}
$$



and (41) follows.  The case $p=3$ can be checked directly and is not used
in the second-order statement.

## 7. Why the Dwork block leaves the lift digit free

Let



$$
\mathcal B_p=\sum_{k=0}^m a_{p+k}.
\tag{45}
$$



Suppose $p\mid T_m$, and write $h_p=T_m/p\pmod p$.  Summing (41)
modulo $p^3$, and using $\sum a_k=0\pmod p$ to cancel the constant
Wilson and Fermat quotient terms, gives



$$
\boxed{
 \frac{\mathcal B_p}{p^2}
 \equiv-\frac14\left[
 h_p+\sum_{k=0}^m a_k(4O_k-H_k)
 \right]\pmod p.}
\tag{46}
$$



Equation (46) is a genuine second-order index-block formula.  It is not an
independent equation for $h_p$: the left side is the new, otherwise
uncontrolled next-block residue.  At the known central root
$p=79,m=39$, exact modular arithmetic gives



$$
h_p=67,\qquad
 \sum_{k=0}^m a_k(4O_k-H_k)=7,\qquad
 \frac{\mathcal B_p}{p^2}=21\pmod {79},
\tag{47}
$$



and (46) reads $21=-\tfrac14(67+7)$.  In particular the next block does
not vanish and there is no hidden Dwork cancellation that determines the
old lift digit.

## 8. Finite evidence and the global-simplicity warning

An exact-integer recurrence scan through $n=3000$ found only the prime
factors $3$ and $401$ in $\gcd(u_n,w_n)$.  The non-$3$ factor occurs
at $n=317+401k$, as predicted by (8), through the cutoff.  The largest
observed value of $q-2n$, over prime factors $q$, is $-1$, attained at
$(n,q)=(2,3)$; for $(317,401)$ it is $-233$.

This is finite evidence only.  It does not prove that every prime divisor of
$\gcd(u_n,w_n)$ is at most $2n$.  In particular, (15) must be retained as
an explicit warning that global ordinary-derivative simplicity is false.

## 9. Reproducibility

The companion certificate checks:

* (6), (7), (12), and (13) by exact polynomial arithmetic for small primes;
* the exact $401$-counterexample and the lift digits (16)--(18);
* the resonant residual (26), the anomalous energy identity (32), and the
  isotropic example (34);
* the block formula (41), its sum (46), and the $p=79$ residues (47);
* the exact-integer gcd scan through $n=3000$.

No finite check is used as a proof of an all-prime assertion.
