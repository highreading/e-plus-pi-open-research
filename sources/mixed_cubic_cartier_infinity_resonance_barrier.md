> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Cartier exactness and the degree-$p+1$ infinity resonance

Date: 2026-08-28

## 1. Scope and conclusion

This note audits a proposed closing argument for the remaining fixed-gap
fresh-prime obstruction. The Cartier reduction to an exact differential is
valid, but the subsequent assertion that its primitive may be taken with
numerator degree at most one is false.

The correct global conclusion is



$$
\deg V\le1\quad\text{or}\quad\deg V=p+1.             \tag{1.1}
$$



The second case is a genuine characteristic-$p$ infinity resonance.
Exact examples occur at



$$
(p,q)=(11,5),\quad(31,13),\quad(97,13),
$$



and their coefficient ratios agree with the actual weighted-Cayley residue
ratios. Thus exactness of the Cartier combination alone cannot force the
two coefficients to vanish. An additional branch, cube, or Frobenius-line
condition would have to eliminate the degree-$p+1$ mode.

These examples do **not** have $B_0=B_1=0$, so they are barriers to the
proposed proof step, not counterexamples to fresh-prime nonvanishing.

## 2. Exact Cartier reduction

Work over $k=\overline{\mathbb F}_p$, where



$$
p=6m+q,\qquad q<p,\qquad q\ {\rm odd},\qquad 3\nmid q.
$$



Put



$$
Q=(1+z)(1+z^2)=1+z+z^2+z^3,\qquad
 u=z(1-z),\qquad A=2q-3,
$$



and let



$$
E:\ y^3=Q.
$$



For $s=0,1$, define



$$
\eta_s=y^{A-3s}u^{-q}\,dz,\qquad
 J_s=Q^{(p+A)/3-s}u^{-q}\,dz=y^p\eta_s.
$$



Write



$$
c_s=\operatorname {Res}_{z=0}J_s,\qquad
 r_s=\operatorname {Res}_{z=1}J_s,\qquad
 B_s=2c_s+r_s.
$$



The usual two-coefficient Cartier calculation says that $B_s=0$ places
$\mathcal C(\eta_s)$ on one common line, with scalar $c_s$. Therefore
$B_0=B_1=0$ makes



$$
\Omega=c_1\eta_0-c_0\eta_1
 =y^{A-3}(c_1Q-c_0)u^{-q}\,dz                         \tag{2.1}
$$



Cartier-zero, hence exact on $E$.

Choose $r\in\{1,2\}$ with $r\equiv A-3\pmod3$, and put



$$
a=\frac{2p-r}{3},\qquad h=\frac{A-3-r}{3}.
$$



Since $3a+r=2p$ and



$$
h-a=-4m-2,
$$



equation (2.1) has the exact form



$$
\Omega=(y^2)^p\,g(z)\,dz,\qquad
 g(z)=\frac{c_1Q-c_0}{Q^{4m+2}u^q}.                  \tag{2.2}
$$



Cartier semilinearity gives



$$
0=\mathcal C(\Omega)=y^2\mathcal C(g(z)\,dz).
$$



Thus $g(z)\,dz$ is exact on the projective line. This reduction is
global and does not discard any $p$-th-power pole.

## 3. What global Hermite reduction actually gives

The finite pole orders of $g(z)\,dz$ are at most



$$
q\quad\text{at }z=0,1,\qquad 4m+2\quad\text{at the roots of }Q.
$$



Both are strictly less than $p$. Since the differential is exact, all
simple partial-fraction residues vanish, and every higher term can be
integrated with a nonzero denominator modulo $p$. Hence a rational
primitive can be chosen as



$$
H(z)=\frac{V(z)}{Q^{4m+1}u^{q-1}},                 \tag{3.1}
$$



with no polynomial part. The denominator in (3.1) has degree



$$
3(4m+1)+2(q-1)=2p+1,
$$



so properness gives only



$$
\deg V\le2p.                                       \tag{3.2}
$$



Differentiating (3.1) and using



$$
-(4m+1)\equiv \frac A3\pmod p
$$



gives



$$
D_A(V)=c_1Q-c_0,                                   \tag{3.3}
$$



where



$$
D_A(V)=QuV'+\frac A3uQ'V-(q-1)Qu'V.                \tag{3.4}
$$



The tempting degree-$\le1$ argument overlooks the behavior of (3.1) at
infinity.

## 4. Exact monomial action and the missing mode

The identities



$$
Qu=z-z^5
$$



and a direct collection of the remaining terms give, for every $d\ge0$,



$$
\boxed{
D_A(z^d)=
(d-q+1)z^d+\frac{5q-6}{3}
 (z^{d+1}+z^{d+2}+z^{d+3})+(1-d)z^{d+4}.}           \tag{4.1}
$$



Suppose $V\ne0$ solves (3.3), and let $d=\deg V$. Since the right side
has degree at most three, the highest coefficient in (4.1) gives



$$
1-d\equiv0\pmod p.
$$



Together with (3.2), this leaves precisely



$$
d=1\quad\text{or}\quad d=p+1.                      \tag{4.2}
$$



This proves (1.1), but it does not remove the second alternative. If
$\deg V=p+1$, then (3.1) starts with a $z^{-p}$, or $t^p$ for
$t=1/z$, term at infinity. Its ordinary derivative is zero in
characteristic $p$. Removing that term by a local $p$-th power need
not preserve the finite-pole bounds globally.

This is the precise failure of the proposed bounded-primitive lemma. The
familiar rational function $1/(z^p-z)$ already illustrates why local
removal of $p$-th-power principal parts does not by itself produce a
globally bounded primitive.

## 5. Three exact degree-$p+1$ witnesses

The companion certificate solves (3.3) by exact modular row reduction.
It normalizes $c_1=1$ and obtains:

| $p$ | $m$ | $q$ | $c_0/c_1$ | $\deg V$ | leading coefficient of $V$ | $(B_0,B_1)$ |
|---:|---:|---:|---:|---:|---:|---:|
| 11 | 1 | 5 | 10 | 12 | 7 | $(5,6)$ |
| 31 | 3 | 13 | 26 | 32 | 16 | $(21,2)$ |
| 97 | 14 | 13 | 87 | 98 | 2 | $(33,84)$ |

In every row:

1. $D_A(V)=Q-c_0$ holds coefficient by coefficient;
2. there is no solution of degree at most one;
3. the displayed ratio equals the independently computed actual residue
   ratio $c_0/c_1$.

For example, at $(p,q)=(11,5)$, the normalized witness is



$$
\begin{aligned}
V={}&5+9(z+z^2+z^3+z^4)
 +5(z^5+z^6+z^7+z^8)\\
 &+7(z^9+z^{10}+z^{11}+z^{12}),
\end{aligned}
$$



and



$$
D_A(V)=Q-10.
$$



The actual residues are $c_0=5,c_1=6$, so
$c_0/c_1=10\pmod {11}$, exactly the witness ratio. Nevertheless
$(B_0,B_1)=(5,6)\ne(0,0)$. The two larger examples behave in the same
way; their complete coefficient vectors are recorded in the JSON.

## 6. Consequence for the proposed closing proof

If one assumes $\deg V\le1$, comparing coefficients in (3.3) does indeed
force the linear coefficient to vanish through the nonzero minor
$\pm4A/3$, and then forces $c_0=c_1=0$. The computation itself is
correct. Its hypothesis is not.

The Cartier argument currently reaches only the dichotomy (4.2). The
degree-$p+1$ branch contains genuine exact combinations on known
connection-candidate pairs, so it cannot be dismissed as a formal
$p$-th-power gauge. A closing proof must supply one more invariant that
is sensitive to the distinguished branch or cube root and is transverse
to this infinity-resonant mode.

For $q=1$, the common zero is separately impossible:
$c_s=1$, $r_s=-4^{E-s}$, so $B_0=B_1=0$ would imply $4=1$ in a
prime characteristic greater than three. This elementary endpoint does
not affect the resonance barrier for $q\ge5$.

## 7. Replay and status

The standard-library file
mixed_cubic_cartier_infinity_resonance_certificate.py:

- replays (4.1) in exact rational arithmetic;
- constructs all three degree-$p+1$ witnesses;
- verifies (3.3) coefficient by coefficient;
- proves by row reduction that no degree-$\le1$ witness exists in those
  rows; and
- independently recomputes $c_s,r_s,B_s$ from the weighted-Cayley
  coefficient formulas.

Run

    python mixed_cubic_cartier_infinity_resonance_certificate.py --output mixed_cubic_cartier_infinity_resonance_certificate.json

The package proves a barrier to one proposed proof mechanism. It does not
assert that a compatible prime with $B_0=B_1=0$ exists, and it does not
settle the fixed-gap cube-support theorem.
