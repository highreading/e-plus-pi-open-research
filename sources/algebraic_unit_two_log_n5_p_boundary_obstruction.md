> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The exact $p$-boundary obstruction for the $n=5$ common-zero problem

Checked: 2026-08-27 UTC

## Verdict

The direct attempt to obtain a new terminal constraint by matching the
period-$p$ law to the five residue-class recurrences does not work for a
simultaneous zero



$$
P_d(\eta)=P_d(\bar\eta)=0,
                         \qquad d<p.
$$



At the characteristic-$p$ boundary, every one of the five first-order
recurrences has zero transition multiplier.  The boundary equations
therefore reset to the five initial values and erase, rather than constrain,
the five pre-boundary endpoint values.  This does not assert that a subtler
global use of the recurrence can never classify its zero pairs; it proves
that boundary matching alone contributes no such classification.

There is nevertheless an exact complementary-degree reformulation.  If
$m=p-1-d$, a simultaneous $P$-zero is equivalent to two weighted
left-factorial congruences at the cyclotomic units $u=1+\zeta _5$ and
$v=1+\zeta _5^{-1}$.  This is the sharp boundary obstruction obtained
here.  No identity proved below forces its common ideal to be supported only
over $19$.

## 1. The scalar recurrence and its reciprocal coefficients

Use the notation of the common-zero reduction:



$$
u=1+\zeta _5,\quad v=1+\zeta _5^{-1},\quad
 A=u+v=uv,\quad A^2-3A+1=0,
$$



and



$$
Q(z)=1+Az+Az^2,\qquad
 \sum_{n\ge0}h_n\frac{z^n}{n!}=\frac{e^z}{Q(z)}.
\tag{1}
$$



Thus



$$
h_0=1,\quad h_1=1-A,\quad
 h_n+Anh_{n-1}+An(n-1)h_{n-2}=1.
\tag{2}
$$



Put



$$
\frac1{Q(z)}=\sum_{j\ge0}q_jz^j.
\tag{3}
$$



Since $A^2=3A-1$, direct recurrence in (3) gives



$$
\begin{aligned}
 q_0&=1,&q_1&=-A,&q_2&=2A-1,\\
 q_3&=1-2A,&q_4&=0,
 \end{aligned}
\tag{4}
$$



and, with $\kappa=5A-2$,



$$
q_{j+5}=\kappa q_j.
\tag{5}
$$



Equivalently,



$$
Q(z)\{1-Az+(2A-1)z^2+(1-2A)z^3\}=1-\kappa z^5.
\tag{6}
$$



Multiplying (3) by $e^z$ proves the exact convolution



$$
h_n=n!\sum_{j=0}^n\frac{q_j}{(n-j)!}.
\tag{7}
$$



Equation (5) is the reciprocal-series form of the five-step law for
$h_n$.

## 2. Exact period and exact loss of endpoint data

Let $p\ne5$ be an odd rational prime and reduce (2) at a prime above
$p$.  At $n=p$ and $n=p+1$, (2) gives



$$
h_p=1=h_0,qquad h_{p+1}=1-A=h_1.
$$



Induction in (2), whose coefficients depend only on $n\bmod p$, then
gives



$$
h_{n+p}=h_n\qquad(n\ge0).
\tag{8}
$$



This period does not impose a hidden terminal condition.  The five-step
law is



$$
h_n-\kappa(n)_5h_{n-5}=T_n,
\tag{9}
$$



where



$$
T_n=1-An+(2A-1)n(n-1)+(1-2A)n(n-1)(n-2).
\tag{10}
$$



For every $s\in\{0,1,2,3,4\}$, the product $(p+s)_5$ contains the
factor $p$.  Hence (9) reduces to



$$
h_{p+s}=T_{p+s}=T_s=h_s.
\tag{11}
$$



Crucially, the right side of (11) contains none of the last value in the
corresponding residue-class chain.  In transition-matrix language, each of
the five boundary maps has rank zero in its old-state coordinate.  Thus the
five endpoint values immediately before $p$ are discarded.  Equations
(8)--(11) prove precisely that propagating a zero pair forward and then
matching across the $p$-boundary yields only the fixed reset identities,
with no equation involving the propagated pre-boundary data.  They do not
preclude a different argument that uses the entire recurrence, its known
initial values, and additional arithmetic structure.

The two endpoint values adjacent to the boundary can be written explicitly,
but not reduced to fixed small algebraic integers.  Wilson's theorem gives



$$
(p-1-j)!\,j!\equiv(-1)^{j+1}\pmod p.
$$



Using (7), $(p-1)!\equiv-1$, and $(p-2)!\equiv1$, one obtains



$$
\boxed{\begin{aligned}
 h_{p-1}&=\sum_{j=0}^{p-1}(-1)^j j!\,q_j,\\
 h_{p-2}&=\sum_{j=0}^{p-2}(-1)^j(j+1)!\,q_j
 \end{aligned}}\qquad(\bmod p).
\tag{12}
$$



By (4)--(5), these are five-block weighted left-factorial sums.  They are
the free pre-boundary data that (11) erases.

## 3. The complementary weighted-factorial criterion

Let



$$
E_d(Z)=\sum_{k=0}^d\frac{Z^k}{k!},\qquad
 P_d(X)=(-1)^d d!E_d(-X),
$$



and suppose $0\le d<p$.  Put



$$
m=p-1-d.
\tag{13}
$$



The normalized value at $x=\eta=u^{-1}$ is



$$
x^{-d}P_d(x)=
 \sum_{j=0}^d(-1)^j(d)_j u^j.
\tag{14}
$$



Because $d\equiv-m-1\pmod p$, for $0\le j\le d$,



$$
(-1)^j(d)_j
 =\frac{(m+j)!}{m!}\qquad(\bmod p).
\tag{15}
$$



Consequently the precise unit-factor identities are



$$
\boxed{\begin{aligned}
 P_d(x)&=\frac{x^d}{m!}
       \sum_{j=0}^d(m+j)!u^j,\\
 P_d(y)&=\frac{y^d}{m!}
       \sum_{j=0}^d(m+j)!v^j
 \end{aligned}}\qquad(\bmod p),
\tag{16}
$$



where $y=\bar\eta=v^{-1}$.  All displayed prefactors are units.
Therefore



$$
P_d(x)=P_d(y)=0
 \quad\Longleftrightarrow\quad
 \begin{cases}
 \displaystyle\sum_{j=0}^d(m+j)!u^j=0,\\[3pt]
 \displaystyle\sum_{j=0}^d(m+j)!v^j=0.
 \end{cases}
\tag{17}
$$



The factorial indices in (17) run exactly from the complementary degree
$m$ through $p-1$.  This is a two-point, cyclotomic weighted analogue
of a left-factorial congruence; it is not an ordinary truncated exponential
of degree $m$.

## 4. A remainder identity at $p-1$

Let



$$
B_n(z)=\sum_{j=0}^n h_j\frac{z^j}{j!}.
$$



Coefficient comparison in $Q(z)B_n(z)$ gives



$$
E_n(z)\equiv
 -A\left(\frac{h_n}{n!}+\frac{h_{n-1}}{(n-1)!}\right)z^{n+1}
 -A\frac{h_n}{n!}z^{n+2}pmod{Q(z)}.
\tag{18}
$$



At $n=p-1$, this becomes



$$
E_{p-1}(z)\equiv
 A(h_{p-1}-h_{p-2})z^p+Ah_{p-1}z^{p+1}pmod{Q(z)}.
\tag{19}
$$



If $Q\mid E_d$ and $m=p-1-d$, Wilson's theorem applied to the tail
from $d+1$ to $p-1$ also gives



$$
E_{p-1}(z)\equiv
 (-1)^d z^{d+1}
 \sum_{j=0}^{m-1}(-1)^j(m-1-j)!z^j
 \pmod{Q(z)},
\tag{20}
$$



with an empty sum when $m=0$.  Combining (19)--(20) is an exact boundary
identity relating a hypothetical zero to $h_{p-1},h_{p-2}$ and a
complementary reverse-factorial polynomial.  It does not eliminate the two
endpoint sums in (12).

## 5. What Frobenius adds, split by $p\bmod5$

Write $u_a=1+\zeta^a$.  The coefficients of the weighted polynomial in
(17) lie in $\mathbb F_p$, so a zero at $u_a$ is carried to a zero at
$u_{ap}$.  Hence:

* if $p\equiv1\pmod5$, Frobenius fixes $u=u_1$ and $v=u_4$
  separately and adds no equation;
* if $p\equiv4\pmod5$, Frobenius interchanges $u_1,u_4$, so it only
  swaps the two equations already present in (17);
* if $p\equiv2\pmod5$, it sends $(u_1,u_4)$ to $(u_2,u_3)$, and
  iteration supplies all four cyclotomic conjugates;
* if $p\equiv3\pmod5$, it sends $(u_1,u_4)$ to $(u_3,u_2)$, again
  supplying all four conjugates after iteration.

Equivalently, $A^p=A$ in the first two cases, whereas
$A^p=3-A=A^{-1}$ in the last two.  Thus Frobenius strengthens the inert
cases to vanishing at the full degree-four orbit, but it supplies no new
condition at split primes.  In particular, Frobenius and the reset identity
cannot by themselves prove that $(p,d)=(19,15)$ is the only solution.

The companion certificate verifies (4)--(12), (16), and (18)--(20) in
exact finite-field arithmetic over a stated finite range.  Those checks are
diagnostic and do not replace the proofs above.  Nothing here proves either
algebraicity or transcendence of $e+\pi$.
