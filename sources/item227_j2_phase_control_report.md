> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 227 — Order-four phase control and the $j=2$ terminal ceiling

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the normalized fixed-$j=2$ cell



$$
4m+1=5p-2s,\qquad
 2\le s\le\frac{p-3}{6},\qquad
 s\equiv\frac{p-1}{2}\pmod 2,\qquad p\ge17,          \tag{1.1}
$$



and put



$$
r=\frac{p-6s-3}{2},\qquad \epsilon=(-1)^r=-1.       \tag{1.2}
$$



Let $M,b,a$ be Item 226's exact one-phase matrix, forcing column, and
terminal covector, so that



$$
Y_{q+1}=MY_q+bw_q,\qquad aY_q=\epsilon w_q,\qquad
 (w_1,w_2,w_3,w_4)=(7,29,11,-11).                    \tag{1.3}
$$



This item gives two all-prime structural conclusions.

> **PROVED — exact order-four control theorem.**  Set
> 

$$
> u=\epsilon b,\qquad N=M+ua.                         \tag{1.4}
>
$$


> Then
> 

$$
> N^4=I,\qquad \det(xI-N)=x^4-1.                     \tag{1.5}
>
$$


> The observability matrix
> 

$$
> O=\begin{pmatrix}a\\aN\\aN^2\\aN^3\end{pmatrix} \tag{1.6}
>
$$


> is invertible on every row.  If
> $U=(u,Nu,N^2u,N^3u)$, then
> 

$$
> \boxed{\quad
> \Delta:=\det(I-M^4)=\det(O)\det(U)
> =F_1F_{-1}F_i.\quad}                                \tag{1.7}
>
$$


> Thus $\Delta=0$ means exactly that the source loses a Fourier/control
> mode.  It is not an affine contradiction: the inhomogeneous closure
> equation is consistent on every singular row.

> **PROVED — four terminals give only two invariants.**  Let $v$ be
> Item 224's canonical common-line state at the first terminal, put
> 

$$
> t_q=aN^{q-1}v,\qquad
> E_q=11t_q-\epsilon\beta w_q.                        \tag{1.8}
>
$$


> Then, for every row in (1.1),
> 

$$
> \boxed{\quad E_4=0,\qquad E_3=E_2-E_1.\quad}        \tag{1.9}
>
$$


> More precisely,
> 

$$
> E_1=-\Omega,qquad
> E_2=\Psi^\flat-\epsilon(ab)\Omega.                 \tag{1.10}
>
$$


> Consequently the bottom equation and all four phase-terminal
> equations are equivalent to the already known pair
> $\Omega=\Psi=0$, together with the usual nonzero normalization.
> Phases 3 and 4 provide no third arithmetic invariant.

> **EXACT FINITE ONLY.**  Through $p\le401$, the 1,115 admissible
> $s\ge2$ rows contain 15 zeros of $\Delta$: four in $F_1$, none
> in $F_{-1}$, and eleven in $F_i$.  Every one has closure rank
> three and a consistent affine right-hand side.  Every one also has
> $\Omega\ne0$, but this last disjointness is only finite evidence.

> **OPEN.**  There is no all-prime exclusion or zero-rate theorem for
> simultaneous zeros of $(\Omega,\Psi)$, no density theorem for the
> three factors in (1.7), and no result here for $s=1$.  Item 227
> books no capacity reduction and proves nothing about $e+\pi$.

## 2. General four-periodic endpoint weights

Let



$$
f_0(z)=z^r(1-z)^r(1+z)(1+z^2)^{2s}
       =z^r\sum_\ell g_\ell z^\ell.                  \tag{2.1}
$$



Instead of fixing Item 219's endpoint functional, let 

$$
W:\mathbb Z\to
\mathbb F_p
$$

 be an arbitrary four-periodic monomial-weight sequence.
Define the regularized moments



$$
\widehat T_k(W)=
 \sum_{\substack{\ell\\p\nmid r+\ell+k+1}}
 g_\ell\frac{W(r+\ell+k+1)}{r+\ell+k+1}.             \tag{2.2}
$$



At $k_1=2s-3$, put



$$
\Phi(W)=
 (\widehat T_{k_1}(W),\ldots,\widehat T_{k_1+3}(W))^t. \tag{2.3}
$$



The derivation of Item 226's one-phase transfer is coefficientwise and
linear in the terminal weight.  It therefore gives, for every $W$,



$$
a\Phi(W)=\epsilon W(p),\qquad
 \Phi(\sigma W)=M\Phi(W)+bW(p)=N\Phi(W),              \tag{2.4}
$$



where $(\sigma W)(n)=W(n+p)$.

The map $\Phi$ is injective.  Indeed, if $\Phi(W)=0$, then (2.4)
successively gives



$$
W(p)=W(2p)=W(3p)=W(4p)=0.                           \tag{2.5}
$$



Because $p$ is odd, these are the four residue classes modulo $4$,
so $W=0$.  Both source and target have dimension four; hence $\Phi$
is an isomorphism.  The shift $\sigma$ is a four-cycle, proving (1.5).
Moreover,



$$
O\Phi(W)=\epsilon
 (W(p),W(2p),W(3p),W(4p))^t,                         \tag{2.6}
$$



so $O$ is invertible.  If



$$
S=\begin{pmatrix}
 0&1&0&0\\0&0&1&0\\0&0&0&1\\1&0&0&0
 \end{pmatrix},                                      \tag{2.7}
$$



then $ON=SO$.  This proves the order-four theorem without a finite
scan or an eigenvalue assumption.

The parity assertion in (1.2) is also exact.  Writing $p=2d+1$, the
cell parity says $d\equiv s\pmod2$, while



$$
r=d-3s-1\equiv1\pmod2.                              \tag{2.8}
$$



## 3. Canonical feedback and the cyclotomic factors

Put



$$
h_q=aN^qu\quad(0\le q\le3).                         \tag{3.1}
$$



Since $M=N-ua$, the matrix determinant lemma and $N^4=I$ give



$$
\begin{aligned}
 \det(I-tM)
 &=\det(I-tN)+t\,a\operatorname{adj}(I-tN)u\\
 &=1-t^4+t(h_0+t h_1+t^2h_2+t^3h_3).                 \tag{3.2}
\end{aligned}
$$



Item 226's $M$ has its first column zero, hence $\det M=0$.  The
$t^4$-coefficient in (3.2) therefore gives



$$
h_3=1.                                               \tag{3.3}
$$



Writing $M$ in its upper $1+3$ block form and denoting the lower
right block by $B$, (3.2) becomes



$$
D(t):=\det(I-tB)=1+h_0t+h_1t^2+h_2t^3.              \tag{3.4}
$$



Now



$$
I-B^4=(I-B)(I+B)(I+B^2),                            \tag{3.5}
$$



and direct substitution into (3.4) gives



$$
\begin{aligned}
 F_1&=1+h_0+h_1+h_2,\\
 F_{-1}&=1-h_0+h_1-h_2,\\
 F_i&=(1-h_1)^2+(h_0-h_2)^2.                         \tag{3.6}
\end{aligned}
$$



Equations (3.4)--(3.6) prove the first equality in (1.7).

There is a second useful form.  The product $OU$ is the cyclic Hankel
matrix



$$
OU=
 \begin{pmatrix}
 h_0&h_1&h_2&1\\
 h_1&h_2&1&h_0\\
 h_2&1&h_0&h_1\\
 1&h_0&h_1&h_2
 \end{pmatrix}.                                      \tag{3.7}
$$



Its four Fourier factors are exactly (3.6), and hence



$$
\det(OU)=F_1F_{-1}F_i=\Delta.                       \tag{3.8}
$$



Because $O$ is invertible, (3.8) proves



$$
\Delta=0\iff \det U=0.                              \tag{3.9}
$$



Thus the singular determinant is a controllability defect, not a
generic rank mystery.

## 4. Exact singular left-null classification

Let



$$
A=I-M^4,\qquad
 C=M^3bw_1+M^2bw_2+Mbw_3+bw_4.                       \tag{4.1}
$$



We show that



$$
C\in\operatorname{im}A       \tag{4.2}
$$



on every row, including every row with $\Delta=0$.

Work temporarily over an algebraic closure.  Since $x^4-1$ is
separable, every left vector in $\ker A^t$ is a sum of vectors
$\ell$ satisfying



$$
\ell M=\zeta\ell,qquad
                         \zeta^4=1.                  \tag{4.3}
$$



Let $r_\zeta$ be a right $\zeta$-eigenvector of $N$.  The
invertibility of $O$ implies $ar_\zeta\ne0$, because



$$
Or_\zeta=(ar_\zeta)(1,\zeta,\zeta^2,\zeta^3)^t.     \tag{4.4}
$$



Using $M=N-ua$, multiply



$$
\ell(N-\zeta I)=(\ell u)a                           \tag{4.5}
$$



by $r_\zeta$.  Equations (4.4)--(4.5) give



$$
\ell u=0,\qquad \ell b=0.                          \tag{4.6}
$$



It follows termwise from (4.1) that $\ell C=0$.  This proves (4.2)
by the left-null criterion.

The same mechanism describes exactly why regular and singular rows
behave differently.  For an arbitrary phase orbit define the terminal
mismatch



$$
\delta_q=w_q-\epsilon aY_q.                         \tag{4.7}
$$



Then



$$
Y_{q+1}=NY_q+b\delta_q                              \tag{4.8}
$$



and $N^4=I$ gives



$$
Y_5-Y_1=
 (N^3b,N^2b,Nb,b)(\delta_1,\delta_2,\delta_3,\delta_4)^t. \tag{4.9}
$$



The determinant of the matrix in (4.9) vanishes exactly when
$\det U$, and hence $\Delta$, vanishes.  On a regular row, closure
forces every $\delta_q=0$.  On a singular row, a nonzero mismatch in
the missing Fourier mode can close after four phases.  This is the
precise scope of the singular exception in Item 226.

## 5. Why the canonical common line has no $-1$ mode

The four-periodic model in Section 2 may be realized by endpoint
functionals supported at $1,-1,i,-i$.  The original path functional
has no $-1$ endpoint.  It is important to prove, rather than assume,
that Item 224's canonical line retains this fact.

Item 224 proved



$$
z^3f_0\,dz=d(H_3f_0)+Q_3f_0\,dz,                   \tag{5.1}
$$



where



$$
H_3(z)=
 \frac{(10s-5)z+4z^2-4z^3+4z^4-(10s-1)z^5}
      {2(s-1)(10s-1)(1+z)}.                          \tag{5.2}
$$



The factor $1+z$ cancels against the corresponding factor in
$f_0$.  At $z=-1$, the numerator in (5.2) is exactly $16$, so



$$
(H_3f_0)(-1)=
 \frac{(-1)^r2^{r+2s+3}}{(s-1)(10s-1)}.              \tag{5.3}
$$



This is a $p$-unit: $s-1$ and $10s-1$ are the units audited in
Item 224.  The boundary term in (5.1) vanishes at $1,i,-i$, but (5.3)
shows that it does not vanish at $-1$.  Therefore a generalized
four-endpoint functional can satisfy Item 224's homogeneous canonical
line only if its $-1$ coefficient is zero.

Let $W_v$ be the unique four-periodic weight with



$$
\Phi(W_v)=v.                \tag{5.4}
$$



The preceding paragraph proves that $W_v$ is supported at
$1,i,-i$.  Fourier orthogonality then gives



$$
W_v(p)-W_v(2p)+W_v(3p)-W_v(4p)=0.                  \tag{5.5}
$$



Using (2.6), (5.5) becomes



$$
t_1-t_2+t_3-t_4=0.          \tag{5.6}
$$



## 6. Bottom reciprocity and terminal redundancy

At the lower terminal $k=-r-1$, Item 224's polynomial $K_k$ has
value $1$ at $0$ and value $0$ at every fourth root of unity.
For a generalized endpoint weight $W$, the same boundary evaluation
therefore gives



$$
\beta=-W(0).                \tag{6.1}
$$



Equations (2.6), (5.4), and (6.1) yield the exact sign



$$
t_4=\epsilon W_v(4p)=\epsilon W_v(0)
                         =-\epsilon\beta.            \tag{6.2}
$$



This is the negative sign: phase 4 repeats the bottom equation rather
than contradicting it.

The target weights also have no $-1$ Fourier component:



$$
7-29+11-(-11)=0.             \tag{6.3}
$$



Substituting (5.6), (6.2), and (6.3) into (1.8) proves (1.9).

For comparison with Items 224--225, $t_1=\tau$, and hence



$$
E_1=11\tau-7\epsilon\beta=-\Omega. \tag{6.4}
$$



Write Item 225's raw second-terminal equation as



$$
\rho_0+\lambda\rho_1=29\epsilon,\qquad
 \rho_0=7ab,qquad \rho_1=aMv,                      \tag{6.5}
$$



and recall



$$
\Psi^\flat=\beta(\rho_0-29\epsilon)+11\rho_1.      \tag{6.6}
$$



Because $t_2=aNv=aMv+\epsilon(ab)\tau$, direct subtraction gives



$$
E_2=\Psi^\flat-\epsilon(ab)\Omega.                 \tag{6.7}
$$



When $\Omega=0$, Item 225 proved



$$
11\Psi=7\epsilon\Psi^\flat. \tag{6.8}
$$



The constants $7$ and $11$ are units for $p\ge17$.  Thus all
four $E_q$ vanish exactly when the two existing invariants vanish.
No third invariant can be extracted merely by continuing the same
four-periodic terminal orbit.

## 7. Exact finite singular census

Through $p\le401$, the factor-zero rows are



$$
\begin{aligned}
 F_1=0:\quad
 &(103,15),(191,13),(191,19),(211,17),\\
 F_{-1}=0:\quad
 &\varnothing,\\
 F_i=0:\quad
 &(41,4),(73,8),(109,2),(193,16),(197,24),\\
 &(281,18),(337,16),(349,18),(373,38),(389,14),(401,46).
                                                               \tag{7.1}
\end{aligned}
$$



There is no overlap among the displayed families.  On all 15 rows,



$$
\operatorname{rank}(I-M^4)=3,qquad
 \operatorname{rank}U=3,                             \tag{7.2}
$$



and the affine closure is consistent, as the all-row theorem predicts.
Every displayed row has $\Omega\ne0$, so it is already excluded by
the first terminal condition within this finite range.  Neither the
empty $F_{-1}$ list nor the disjointness from $\Omega=0$ is promoted
to an all-prime statement.

The complete transcript of factor values, ranks, residuals, and
$(\Omega,\Psi)$ values has SHA-256 recorded in the canonical JSON.
The generalized four-periodic endpoint basis is independently replayed
coefficient by coefficient on all 74 admissible rows through
$p\le101$.

## 8. Structural no-go and remaining arithmetic target

Item 227 closes two tempting but invalid routes to an immediate
contradiction:

1. A zero of $\Delta$ cannot itself contradict affine closure;
   Section 4 proves the affine right-hand side is always in the image.
2. Phases 3 and 4 cannot supply a third independent terminal
   congruence; Sections 5--6 prove that they reduce to
   $\Omega$ and $\Psi$.

This is a scoped no-go for the present one-functional, four-periodic
closure mechanism.  It is not an impossibility theorem for a new
functional, a paired-cell argument, or a direct arithmetic
classification of simultaneous zeros.  The surviving all-prime target
is exactly



$$
\Omega_{p,s}=\Psi_{p,s}=0.   \tag{8.1}
$$



The factors $F_1,F_{-1},F_i$ and (8.1) are moving finite-log data.
No common resultant, Bezout unit, or density estimate is proved here.

## 9. Capacity bookkeeping

The $j=2$ common-log cell has capacity $2/35$ per $m$.  Structural
classification without an all-prime or zero-rate exclusion removes
none of it.  Therefore



$$
\boxed{\text{new booked rate from Item 227}=0.}        \tag{9.1}
$$



The conditional comparison from Item 219 remains unchanged: excluding
both $j=1$ and $j=2$ would leave



$$
0.1132379841892420\ldots\ \text{per }m
 =0.0188729973648737\ldots\ \text{per }6m,            \tag{9.2}
$$



below $G=0.01963298367\ldots$ per $6m$.  Item 227 does not establish
either exclusion.

## 10. Reproduction and status ledger

From the portable archive root:

~~~
python scripts/item227_j2_phase_control_certificate.py \
  --output results/item227_j2_phase_control_certificate.json
python scripts/item227_j2_phase_control_certificate.py \
  --output results/item227_j2_phase_control_certificate_replay.json
~~~

The checker uses only Python's standard library and the frozen Item 226
dependency chain stored beside it.

**PROVED**

- generalized endpoint-weight isomorphism, $N^4=I$, and the exact
  four-cycle conjugacy;
- cyclotomic/control factorization (1.7);
- exact singular left-null classification and affine consistency;
- phase-4/bottom reciprocity with the negative sign;
- $E_4=0$, $E_3=E_2-E_1$, and reduction to
  $(\Omega,\Psi)$.

**EXACT FINITE**

- the factor-family census (7.1) through $p\le401$;
- all 15 singular rows have ranks (7.2), consistent affine closure,
  and nonzero $\Omega$ through that bound;
- no simultaneous $\Omega=\Psi=0$ row occurs through that bound.

**OPEN**

- an all-prime exclusion or zero-rate theorem for (8.1);
- an all-prime density classification of $F_1,F_{-1},F_i$;
- the exceptional $s=1$ family;
- a zero-rate theorem for the fixed $j=2$ cell;
- any capacity reduction or conclusion about $e+\pi$.
