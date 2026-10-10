> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exceptional fresh-prime ray: a complete log-residue coprimality theorem

Date: 2026-08-28

## 1. Statement

Let (m\geq1), and suppose



$$
p=10m+3
$$



is prime.  Let (L_0,L_1) be the two adjacent mixed-cubic logarithmic
residues.  Then



$$
\boxed{(L_0,L_1)\not\equiv(0,0)\pmod p.}             \tag{1.1}
$$



This closes the sole exceptional ray left by the scalar consecutive-zero
reduction.  It does not, by itself, prove coprimality for the other fresh
primes.

## 2. Exact conversion to residues of (y^5-y)

Put



$$
A(t)=(-1+t)(2-t),\qquad R(t)=t^2-2t+2,
$$



and set



$$
n=4m+3,\qquad y=1-t,
$$



so that



$$
A=-y(y+1),\qquad R=y^2+1,
$$





$$
S:=AR=-y(y+1)(y^2+1),\qquad
 F(y):=y^5-y=(y-1)y(y+1)(y^2+1)=tS.              \tag{2.1}
$$



For (p>6m), the fresh-prime Frobenius formula is



$$
L_s\equiv-4[t^{4m+s}]
 A(t)^{-(p-6m)}R(t)^{-(4m+1+s)}\pmod p.           \tag{2.2}
$$



The negative powers in (2.2) mean their formal Taylor expansions at
(t=0); their constant terms are units for every odd (p).

On (p=10m+3), (p-6m=n).  Therefore



$$
\begin{aligned}
 L_1&=-4[t^{n-2}]A^{-1}S^{-(n-1)},\\
 L_0&=-4[t^{n-3}]A^{-2}S^{-(n-2)}.                \tag{2.3}
\end{aligned}
$$



All equalities from here through the end of the proof are in
(\mathbb F_p).

The signs in the change of variables are important.  For (L_1), (n-1)
is even, so



$$
A^{-1}S^{-(n-1)}
 =-\frac{B^{-(n-1)}}{y(y+1)},
 \qquad B=y(y+1)(y^2+1),
$$



while (t^{-(n-1)}=(y-1)^{-(n-1)}) and (dt=-dy).  Thus



$$
[t^{n-2}]A^{-1}S^{-(n-1)}
 =\operatorname {Res}_{y=1}
 \frac{F(y)^{-(n-1)}}{y(y+1)},dy.                \tag{2.4}
$$



For (L_0), (n-2) is odd.  The three signs from
(S^{-(n-2)}=-B^{-(n-2)}),
(t^{-(n-2)}=-(y-1)^{-(n-2)}), and (dt=-dy) leave



$$
[t^{n-3}]A^{-2}S^{-(n-2)}
 =-\operatorname {Res}_{y=1}
 \frac{F(y)^{-(n-2)}}{y^2(y+1)^2},dy.            \tag{2.5}
$$



Since



$$
\frac{F}{y(y+1)}=(y-1)(y^2+1),\qquad
 \frac{F^2}{y^2(y+1)^2}=(y-1)^2(y^2+1)^2,
$$



define



$$
\rho_j=\operatorname {Res}_{y=1}y^jF(y)^{-n},dy. \tag{2.6}
$$



Equations (2.3)--(2.6) give the exact common-index formulas



$$
\boxed{L_1=-4(\rho_3-\rho_2+\rho_1-\rho_0),}    \tag{2.7}
$$





$$
\boxed{
 L_0=4(\rho_6-2\rho_5+3\rho_4-4\rho_3
              +3\rho_2-2\rho_1+\rho_0).}         \tag{2.8}
$$



The second polynomial is simply
((y-1)^2(y^2+1)^2=y^6-2y^5+3y^4-4y^3+3y^2-2y+1).

## 3. The residue recurrence and its singular classes

The residue of an exact derivative is zero.  Applying this to
(d(y^kF^{1-n})) gives, for every integer (k\geq0),



$$
\boxed{
 (k+5-5n)\rho_{k+4}+(n-1-k)\rho_k=0.}            \tag{3.1}
$$



Here



$$
5n=20m+15=2p+9.                                  \tag{3.2}
$$



At (k=0), equation (3.1) is
((n-1)(\rho_0-5\rho_4)=0).  The number
(n-1=4m+2) lies strictly between zero and (p), so it is a unit.  At
(k=4), the coefficient (9-5n=-2p) vanishes, while
(n-5=4m-2) is a nonzero (p)-unit, including at (m=1), where it is
2.  Hence



$$
\boxed{\rho_0=\rho_4=0.}                         \tag{3.3}
$$



At (k=p+4), the first coefficient is
(p+9-5n=-p=0), while



$$
n-1-(p+4)=-6m-5
$$



is a unit because (0<6m+5<p) for every (m\geq1).  Thus



$$
\rho_{p+4}=0.                                    \tag{3.4}
$$



Let (r\in\{1,3\}) be the residue class of (p) modulo 4.  Starting
with (3.4), apply (3.1) successively at



$$
k=p,p-4,p-8,\ldots,r.
$$



At each step, (n-1-k) is a unit.  Indeed, with (0\leq k\leq p), it
could vanish modulo (p) only at (k=n-1), but
(n-1=4m+2\equiv2\pmod4), whereas the entire backward chain has class
(r=1) or 3.  Therefore every step is legitimate and terminates at



$$
\boxed{
 \begin{cases}
 \rho_3=0,&m\text{ even},\quad p\equiv3\pmod4,\\
 \rho_1=0,&m\text{ odd},\quad p\equiv1\pmod4.
 \end{cases}}                                      \tag{3.5}
$$



No unlisted denominator is being divided by in this propagation.

Finally, (3.1) at (k=1,2), together with (3.2), gives



$$
\rho_5=\frac{n-2}{3}\rho_1,
 \qquad
 \rho_6=\frac{n-3}{2}\rho_2=2m\rho_2,            \tag{3.6}
$$



where 2 and 3 are units because (p\geq13).

## 4. A nonzero anchor from the global residue theorem

The roots of (F=y^5-y) are (0) and the four fourth roots of unity.
They are distinct in an algebraic closure of (\mathbb F_p), since
(p\ne2,5).  At a fourth root of unity (\zeta), substitute
(y=\zeta u).  Since



$$
F(\zeta u)=\zeta F(u),\qquad y^2dy=\zeta^3u^2du,
$$



and (n=4m+3), the residue of (y^2F^{-n}dy) at every such root is



$$
\zeta^{3-n}\rho_2=\zeta^{-4m}\rho_2=\rho_2.     \tag{4.1}
$$



At zero,



$$
y^2F^{-n}dy
 =-y^{2-n}(1-y^4)^{-n}dy
 =-\sum_{a\geq0}\binom{n+a-1}{a}y^{2-n+4a}dy.
$$



The exponent is (-1) exactly when (a=m).  Hence



$$
\operatorname {Res}_{y=0}y^2F^{-n}dy
 =-\binom{n+m-1}{m}=-\binom{5m+2}{m}.             \tag{4.2}
$$



At infinity the differential is (O(y^{2-5n})dy), so its residue is
zero.  The global residue theorem, applied over the algebraic closure,
therefore gives



$$
\boxed{4\rho_2=\binom{5m+2}{m}.}                 \tag{4.3}
$$



This is a (p)-unit.  Indeed



$$
0\leq m,\ 4m+2,\ 5m+2<p=10m+3,
$$



so the factorial identity



$$
\binom{5m+2}{m}=\frac{(5m+2)!}{m!(4m+2)!}
$$



contains no factor (p) in its numerator or denominator.  Equivalently,
Lucas's theorem has only one base-(p) digit and gives a nonzero binomial
coefficient.  Thus



$$
\boxed{\rho_2\ne0.}                              \tag{4.4}
$$



## 5. Exclusion of simultaneous vanishing

Using (3.3) and (3.6), equation (2.8) reduces to



$$
\boxed{
 \frac{L_0}{4}=(2m+3)\rho_2
 -\frac{8(m+1)}3\rho_1-4\rho_3.}                 \tag{5.1}
$$



If (m) is even, then (\rho_3=0).  A hypothetical (L_1=0) in
(2.7) would give (\rho_1=\rho_2), and hence



$$
\frac{L_0}{4}=\frac{1-2m}{3}\rho_2\ne0.         \tag{5.2}
$$



Here (3) is a unit and (0<2m-1<p).  Notice that positive even (m)
starts at (m=2), so no endpoint is missing.

If (m) is odd, then (\rho_1=0).  A hypothetical (L_1=0) would give
(\rho_3=\rho_2), and



$$
\frac{L_0}{4}=(2m-1)\rho_2\ne0,                 \tag{5.3}
$$



because (0<2m-1<p).  This includes the smallest case (m=1,p=13),
where the factor is 1.  Equations (5.2)--(5.3) prove (1.1).

## 6. Audit status

The companion script
`mixed_cubic_exceptional_ray_coprimality_certificate.py` independently
computes (L_0,L_1) from the original scalar Taylor recurrence and the
(\rho_j) from the polynomial congruence



$$
\rho_j=\frac14[x^{n-1}](1+x)^j
 \bigl(4+10x+10x^2+5x^3+x^4\bigr)^{6m}\pmod p.
$$



It checks the orientation signs in (2.7)--(2.8), every residue reduction,
the global binomial anchor, and the final parity contradiction.  These
finite replays are secondary audits; the proof above is uniform.
\r
