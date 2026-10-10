> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 304 — the Gaussian numerator and the exact boundary residue

Date: 2026-08-31

## 1. Exact outcome and capacity first

Item 301 reduces the structural-boundary scalar at



$$
p=4H+3                                      \tag{1.1}
$$



to one quadratic Gaussian moment $J_{2H}$.  This item evaluates its
moving-prime residue completely.

**PROVED — all actual boundaries.**  Put



$$
w_H=(-1)^{\lfloor H/2\rfloor}2^H.                              \tag{1.2}
$$



Then



$$
\boxed{B_H\equiv-24(1+w_H)\pmod p},          \tag{1.3}
$$



and $B_H\not\equiv0\pmod p$ for every actual boundary prime
$p\geq19$.

The residual moment is therefore not a left-factorial obstruction or an
uncontrolled hypergeometric value: after an exact integer normalization,
its truncated central-binomial sum collapses by the binomial theorem and
Frobenius.

This theorem does **not** reduce the retained fixed-$j=1$ ceiling.
Item 301 proves that the boundary-neighbor combination is
$-Q_0(h)E_h^*$, so $B_H$ is not itself a necessary-zero gate for the
pinned collision.  Its nonvanishing excludes no prime from the shifted
boundary union, whose raw Chebyshev mass is asymptotic to $2H$.
Capacity booking remains zero, and the conditional ceiling remains
$1/36$ per $6m$.

## 2. An exact Gaussian-integer numerator recurrence

Item 301 proves



$$
J_0=1,\qquad
 (1-i)^n(1-2i)=nJ_{n-1}-i(4n+2)J_n\quad(n\geq1).             \tag{2.1}
$$



Define the Gaussian integer



$$
N_n=2+(2+i)\sum_{k=1}^{n}\binom{2k}{k}(1+i)^k
     =A_n+iT_n.                                             \tag{2.2}
$$



Solving (2.1), or substituting (2.2) directly, gives



$$
\boxed{J_n=\frac{(-i)^n(n!)^2}{2(2n+1)!}\,N_n}.             \tag{2.3}
$$



Thus $A_n,T_n\in\mathbb Z$.  Eliminating the last summand of (2.2)
gives a fraction-free numerator recurrence:



$$
\begin{aligned}
N_0&=2,\qquad N_1=4+6i,\\
(n+1)(N_{n+1}-N_n)
 &=2(2n+1)(1+i)(N_n-N_{n-1})\qquad(n\geq1).          \tag{2.4}
\end{aligned}
$$



Equations (2.2)--(2.4) are identities for every $n$; no recurrence was
guessed from data.

## 3. Specialization at $n=2H$

Put



$$
m=2H+1=\frac{p-1}{2}.                       \tag{3.1}
$$



Because $p\equiv3\pmod4$, $m$ is odd.  Wilson's theorem, paired
around $p$, gives



$$
(m!)^2\equiv1\pmod p,qquad m\equiv-\frac12\pmod p.          \tag{3.2}
$$



Also $(p-2)!=(4H+1)!\equiv1\pmod p$.  Hence



$$
\frac{((2H)!)^2}{(4H+1)!}\equiv4\pmod p. \tag{3.3}
$$



Since $\operatorname {Im}(1-i)^{2H+1}=-w_H$, equations (2.3) and
Item 301's exact $Y_H$-bridge yield



$$
\boxed{2Y_H\equiv-w_H+3(-1)^HT_{2H}\pmod p}.       \tag{3.4}
$$



Thus the problem is reduced to the integer numerator $T_{2H}$.

## 4. Collapse of the truncated central-binomial residue

Work in $\mathbb F_{p^2}=\mathbb F_p(i)$; since $p\equiv3\pmod4$,
$i^p=-i$.  For $0\leq k\leq m$,



$$
\binom{2k}{k}\equiv(-4)^k\binom mk\pmod p.         \tag{4.1}
$$



With $x=1+i$, the sum in (2.2), truncated at $2H=m-1$, therefore is



$$
\begin{aligned}
S_{m-1}
&:=\sum_{k=1}^{m-1}\binom{2k}{k}x^k\\
&\equiv(1-4x)^m-(-4x)^m-1\pmod p.                    \tag{4.2}
\end{aligned}
$$



The two powers are elementary.  First,



$$
1-4x=-3-4i=-(2+i)^2,qquad
 (-3-4i)^m=-\frac{(2+i)^p}{2+i}=\frac{-3+4i}{5}.       \tag{4.3}
$$



Second, $(-4)^m=-1$, and



$$
(-4-4i)^m=
\begin{cases}
-e_H(1+i),&H\text{ even},\\
d_H(1-i),&H\text{ odd},
\end{cases}                                                \tag{4.4}
$$



where



$$
e_H=(-1)^{H/2}2^H,qquad
 d_H=(-1)^{(H-1)/2}2^H.                                    \tag{4.5}
$$



Taking $\operatorname {Im}((2+i)S_{m-1})$ in (4.2)--(4.4) gives the
complete numerator specialization



$$
\boxed{
T_{2H}\equiv
\begin{cases}
3e_H,&H\text{ even},\\
d_H,&H\text{ odd}
\end{cases}\pmod p.}                                      \tag{4.6}
$$



This is the promised exact hypergeometric evaluation; no prime examples
or interpolation enter its proof.

## 5. Evaluation and nonvanishing of $Y_H,B_H$

Substituting (4.6) into (3.4) gives



$$
\boxed{
Y_H\equiv
\begin{cases}
4e_H,&H\text{ even},\\
-2d_H,&H\text{ odd}
\end{cases}\pmod p.}                                      \tag{5.1}
$$



Item 301 proves



$$
B_H\equiv
\begin{cases}
6(2e_H-1)Y_H,&H\text{ even},\\
-6(Y_H+4+6d_H),&H\text{ odd}.
\end{cases}                                                \tag{5.2}
$$



Euler's criterion gives



$$
e_H^2\equiv-\frac12\pmod p,qquad
 d_H^2\equiv\frac12\pmod p.                               \tag{5.3}
$$



Equations (5.1)--(5.3) simplify in both parities to (1.3).  If
$B_H\equiv0$, then $w_H=-1$.  Squaring would give
$1=-1/2$ in the even case or $1=1/2$ in the odd case, impossible for
$p\geq19$.  This proves universal boundary nonvanishing.

## 6. Exact capacity audit

For $s=2j$, Item 301 defines



$$
L_j(h)=\frac{Q_j(h)}pB_{h+3j}
       +\sum_{\substack{1\leq k\leq3\\k\ne j}}
          Q_k(h)E_{h+3k}^*
       =-Q_0(h)E_h^*.                                      \tag{6.1}
$$



Therefore the complete nonvanishing theorem for $B_H$ does not make
$B_H$ a new necessary-zero scalar.  When $Q_j/p$ is a unit and
$E_h^*=0$, it only says that the neighboring terms must compensate a
nonzero boundary term.  This can exclude simultaneous vanishing of all
those terms, but it excludes no prime from the union of possible pinned
collisions.

The complete Item 297 boundary-coefficient drop set is



$$
\begin{array}{c|l}
s& p\text{ with }Q_j(h)/p\equiv0\pmod p\\ \hline
2&19\\
4&79\\
6&787067.
\end{array}                                                \tag{6.2}
$$



At these rows the boundary term is absent, so its nonvanishing yields no
recurrence consequence.  Off (6.2), compensation is required but still
does not remove the prime.  No $o(H)$ exceptional-mass bound and no
retained-ceiling reduction follows.



$$
\boxed{\text{new linear log rate}=0,\quad
       \text{new divisibility exponent}=0,\quad
       \text{capacity booked}=0.}                           \tag{6.3}
$$



The conditional fixed-$j=1$ ceiling remains $1/36$ per $6m$.

## 7. Reproducibility and strict labels

From the archive root, run

~~~text
python scripts/item304_j1_boundary_gaussian_residue_certificate.py --output results/item304_j1_boundary_gaussian_residue_certificate.replay.json
~~~

The checker uses exact standard-library integer and Gaussian-rational
arithmetic.  It replays (2.2)--(2.4) through $n=160$, with no actual
prime scan.  The binomial, Wilson, Frobenius, and Euler derivations in
Sections 3--5 are the logical basis of the all-prime theorem.

- **PROVED:** the Gaussian-integer numerator (2.2)--(2.4), the exact
  moving-prime specialization (3.3)--(5.3), and
  $B_H\not\equiv0\pmod p$ for every actual boundary.
- **OPEN:** nonvanishing or weighted density for the pinned $E_h^*$
  orbit, any $o(H)$ bound for actual collision primes, Route 1, and every
  conclusion about $e+\pi$.
- **NOT CLAIMED:** that boundary nonvanishing supplies an independent
  collision gate or a capacity saving.
