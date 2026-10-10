> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The exact first lift of the relative Cartier endpoint determinant

Date: 2026-08-28

## 1. Scope and verdict

This note works locally at an odd prime $p$.  It supplies the missing
algebraic first-lift formula behind the relative endpoint congruence used in
item 149.  Its conclusions are deliberately separated.

**PROVED: universal coordinate formula.**  If a rational differential has
separable $p$-integral poles, no pole at $0,1$, pole orders at most
$p^2$, and polynomial quotient degree at most $p^2-2$, then its vector



$$
(pR,L,E)\pmod {p^2}
$$



is given exactly by (2.4) below.  The formula retains the pole bands
$j=pk+1$, not $j=pk$, modulo $p^2$, and it retains every other pole
band modulo $p$.  The analogous polynomial bands are $n=pk-1$.

**PROVED: Hasse--Fermat formula.**  For



$$
\omega=F^pP\,dx,
$$



every Laurent coefficient required by (2.4) is given by the exact local
formula (3.3).  Its second term is the Frobenius/Fermat defect of the whole
local unit of $F$, and the endpoint powers have the separate Fermat
correction (3.6).

**PROVED: determinant Bockstein.**  In the item-149 rank-one situation,
where $P_0,P_1$ have degree at most $2p-2$, the quotient



$$
{L_1(pR_0)-L_0(pR_1)\over p}\pmod p
$$



has the shorter exact formula (4.10).  It is controlled by the relative
Cartier vector of one differential



$$
\eta=F^{p-1}F'T\,dx,
       \qquad
       T'=\gamma _1P_0-\gamma _0P_1,
       \qquad
       \gamma_s=[x^{p-1}]P_s.
$$



The division defining $T$ is $p$-integral: after the $x^{p-1}$ term
cancels, none of the remaining denominators $n+1$, with
$0\le n\le2p-2$, is divisible by $p$.  Formula (4.13) gives the
corresponding quotient by $p^2$ on rank-zero rows.

**Sharp obstruction.**  At the actual forced row $(m,p)=(6,7)$, the
formula gives



$$
A_m\equiv4\pmod7.
$$



Thus $v_7(7A_m)=1$, and the hoped-for second $7$-adic content digit is
absent.  This is an exact obstruction, not a finite-pattern inference.

The result is a formula, not a positive-density higher-lift theorem.  It
does not improve the item-149 exponential content constant by itself.

## 2. The universal partial-fraction lift

Let $\mathcal O$ be the ring of integers of a finite unramified extension
of $\mathbb Q_p$.  Work in a splitting algebra large enough to contain the
finite poles.  Assume that distinct poles remain distinct modulo $p$, and
that $\alpha$ and $1-\alpha$ are units for every pole $\alpha$.

Write the partial fraction expansion of a differential as



$$
\omega=\left(
     \sum_{n=0}^{D}h_nx^n
     +\sum_{\alpha}\sum_{j=1}^{J_\alpha}
          {c_{\alpha,j}\over(x-\alpha)^j}
            \right)dx.                                      \tag{2.1}
$$



Separability makes every $h_n,c_{\alpha,j}$ $p$-integral.  Put



$$
\Delta_{\alpha,d}
   =(1-\alpha)^{-d}-(-\alpha)^{-d}.                           \tag{2.2}
$$



The simple residues $c_{\alpha,1}$ determine the period coordinates by
fixed $p$-integral linear maps



$$
L=\lambda((c_{\alpha,1})_\alpha),\qquad
       E=\epsilon((c_{\alpha,1})_\alpha).                    \tag{2.3}
$$



For the original mixed-cubic poles $-1,i,-i$, one may take



$$
\lambda(c)=4c_{-1}+2(c_i+c_{-i}),\qquad
 \epsilon(c)=2i(c_i-c_{-i}).
$$



The rational endpoint coordinate is obtained from all polynomial terms and
all nonsimple poles.  Suppose



$$
D\le p^2-2,\qquad J_\alpha\le p^2.              \tag{2.4a}
$$



Then no endpoint denominator in $pR$ contains $p^2$.  Direct integration
of (2.1), with $d=j-1$, gives the exact congruence



$$
\begin{aligned}
 pR(\omega)\equiv{}&
 \sum_{\substack{0\le n\le D\\ n+1=pk}}{h_n\over k}
 -\sum_\alpha\sum_{\substack{1\le d<J_\alpha\\ d=pk}}
       {c_{\alpha,d+1}\Delta_{\alpha,d}\over k}\\
 &+p\left(
 \sum_{\substack{0\le n\le D\\p\nmid n+1}}{h_n\over n+1}
 -\sum_\alpha\sum_{\substack{1\le d<J_\alpha\\p\nmid d}}
       {c_{\alpha,d+1}\Delta_{\alpha,d}\over d}
          \right) \pmod {p^2},                              \tag{2.4}
\end{aligned}
$$



and



$$
L(\omega)\equiv\lambda((c_{\alpha,1})_\alpha),\qquad
       E(\omega)\equiv\epsilon((c_{\alpha,1})_\alpha)
       \pmod {p^2}.                                          \tag{2.5}
$$



In the first line of (2.4), coefficients and endpoint powers are needed
modulo $p^2$.  Inside the parenthesis they are needed only modulo $p$.
Equations (2.4)--(2.5) are the promised universal first lift.

The indexing is worth emphasizing.  A pole term has primitive denominator
$j-1$, so the resonant layers are



$$
j=pk+1.                                    \tag{2.6}
$$



If the pole order is $ph$, these have $1\le k\le h-1$; there is no
$k=h$ layer.  The polynomial primitive denominator is $n+1$, hence its
resonant layers are



$$
n=pk-1.                                    \tag{2.7}
$$



Reducing (2.4) only modulo $p$ discards the second line and recovers the
relative Cartier endpoint lemma.  A lift modulo $p^2$ cannot discard that
line.

## 3. Local Hasse derivatives and Fermat defects

Now suppose $\omega=F^pP\,dx$, with $P$ regular at every pole of $F$.
At a pole $\alpha$ of order $h=h_\alpha$, set $z=x-\alpha$ and write



$$
A_\alpha(z)=z^hF(\alpha+z)=\sum_{r\ge0}a_{\alpha,r}z^r,
 \qquad
 P(\alpha+z)=\sum_{r\ge0}b_{\alpha,r}z^r.                   \tag{3.1}
$$



Thus $a_{\alpha,r}$ and $b_{\alpha,r}$ are Hasse derivatives at
$\alpha$.  Let $\sigma$ denote the unramified Frobenius lift and define
the integral series



$$
\mathfrak F_{p,\sigma}(A)(z)
   ={A(z)^p-\sigma(A)(z^p)\over p}
   =\sum_{r\ge0}\phi_rz^r.                                  \tag{3.2}
$$



The numerator is divisible by $p$, coefficient by coefficient.  Since



$$
c_{\alpha,j}=[z^{ph-j}]A_\alpha(z)^pP(\alpha+z),
$$



one has the exact identity



$$
\boxed{
 c_{\alpha,j}=
 \sum_{r\ge0}\sigma(a_{\alpha,r})
       b_{\alpha,ph-j-pr}
 +p\sum_{r\ge0}\phi_r b_{\alpha,ph-j-r}.}                   \tag{3.3}
$$



An out-of-range $b$-coefficient is zero.  Formula (3.3), truncated at the
displayed target degree, supplies $c_{\alpha,j}\bmod p^2$ for
(2.4)--(2.5).
Expanding (3.2) by the multinomial theorem shows explicitly that its two
sources are the coefficient Fermat quotients



$$
{a_r^p-\sigma(a_r)\over p}                      \tag{3.4}
$$



and every mixed multinomial whose coefficient is divisible by exactly one
copy of $p$.

There is a separate endpoint Fermat term.  For a unit $v\in\mathcal O$,
put



$$
\delta_\sigma(v)={v^p-\sigma(v)\over p}.            \tag{3.5}
$$



Then, for every $k<p$,



$$
v^{-pk}\equiv
 \sigma(v)^{-k}-pk\,\sigma(v)^{-k-1}\delta_\sigma(v)
 \pmod {p^2}.                                                 \tag{3.6}
$$



When $v\in\mathbb Z_p^\times$, this is the usual Fermat-quotient formula



$$
v^{-pk}\equiv v^{-k}(1-pkq_p(v))\pmod {p^2},\qquad
 q_p(v)={v^{p-1}-1\over p}.                                  \tag{3.7}
$$



Equations (3.3) and (3.6) make every term in (2.4) explicit.

The full coordinate lift is not a bounded-jet operation.  For example, put
$z=x+1$,



$$
F={1+z\over z},\qquad P(z)=\sum_{j=0}^{p-1}b_jz^j.
$$



The residue of $F^pP\,dz$ at $z=0$ is



$$
c_1=\sum_{j=0}^{p-1}{p\choose p-1-j}b_j
 \equiv b_{p-1}
 +p\sum_{j=0}^{p-2}{(-1)^{p-2-j}\over p-1-j}b_j\pmod {p^2}. \tag{3.8}
$$



Every $b_0,\ldots,b_{p-2}$ occurs with a nonzero coefficient.  Likewise,
with $P=1$ and



$$
F_a=z^{-1}(1+az^{p-1}),                          \tag{3.9}
$$



the residue is $pa$; changing the $(p-1)$-st local coefficient changes
the first digit although all lower jets agree.  Thus no jet bound independent
of $p$ determines the three lifted coordinates in the universal class.

## 4. Cancellation in the rank-one determinant

Assume now that $F$ is common and



$$
\omega_s=F^pP_s\,dx,\qquad \deg P_s\le2p-2\quad(s=0,1).     \tag{4.1}
$$



Put



$$
\gamma_s=[x^{p-1}]P_s,qquad
 \Theta=\gamma_1P_0-\gamma_0P_1.                             \tag{4.2}
$$



The $x^{p-1}$ coefficient of $\Theta$ is exactly zero.  Define



$$
T(x)=\sum_{\substack{0\le n\le2p-2\\n\ne p-1}}
          {[x^n]\Theta\over n+1}x^{n+1}.                     \tag{4.3}
$$



Here $n+1\le2p-1$, and the only multiple of $p$ in that interval is
$p$, whose numerator has been removed.  Hence



$$
T\in\mathcal O[x],\qquad T'=\Theta.        \tag{4.4}
$$



Set



$$
\eta=F^{p-1}F'T\,dx.                       \tag{4.5}
$$



The exact differential identity



$$
F^p\Theta\,dx=d(F^pT)-p\eta                           \tag{4.6}
$$



is the Bockstein behind the first lift.

Write $X_s=pR_s$, and let



$$
V=(V_R,V_L)
$$



be any $p$-integral lift of the common relative-Cartier vector, normalized
so that



$$
(X_s,L_s)\equiv\gamma_s(V_R,V_L)\pmod p.         \tag{4.7}
$$



Let



$$
B=[F^pT]_{0}^{1}.                              \tag{4.8}
$$



Assume that $pR(\eta)$ is $p$-integral.  A sufficient condition is that
the pole orders of $F$ are at most $p-1$, with the corresponding
polynomial-quotient bound.  From (4.6),



$$
\begin{aligned}
 {\gamma_1X_0-\gamma_0X_1\over p}
     &\equiv B-pR(\eta),\\
 {\gamma_1L_0-\gamma_0L_1\over p}
     &\equiv-L(\eta)\pmod p.                                \tag{4.9}
\end{aligned}
$$



This qualification is necessary.  If $F$ has a pole of order $p$, then
$\eta$ can have a pole term with $j=p^2+1$; its primitive has denominator
$p^2$, so $pR(\eta)$ need not be integral.  In that edge case one must
use the direct formula (2.4) for the original pair rather than divide the
two terms on the right of (4.9) separately.  On every fixed positive-mass
prime band of item 149, the order of $F$ is fixed while $p\to\infty$, so
the sufficient condition holds eventually.

Expanding the determinant once and using (4.7)--(4.9) gives



$$
\boxed{
 {L_1X_0-L_0X_1\over p}
 \equiv
 V_L\bigl(B-pR(\eta)\bigr)+V_RL(\eta)\pmod p.}              \tag{4.10}
$$



There is no division by a possibly zero $\gamma_s$ in (4.10).  Thus the
formula remains valid when one or both Cartier scalars vanish.  It also
shows exactly why a second Cartier iterate is not the first lift.

The right side can itself be evaluated in characteristic $p$.  Indeed,



$$
\overline\eta=\overline F^{p}
       \left(\overline T\,{d\overline F\over\overline F}\right),
\qquad
 \mathcal C(\overline\eta)
 =\overline F\,
   \mathcal C\left(\overline T\,{d\overline F\over\overline F}\right).
                                                                    \tag{4.11}
$$



If, over the residue splitting field,



$$
{d\overline F\over\overline F}
           =\sum_{a\in S}n_a{dx\over x-a},                         \tag{4.12}
$$



then Cartier of $\overline T\,d\log\overline F$ is determined by the
finite values $n_aT(a)$, together with at most the $x^{p-1}$ coefficient
of



$$
\sum_{a\in S}n_a{T(x)-T(a)\over x-a}.
$$



The latter produces a scalar multiple of $F\,dx$, which drops out of the
wedge in (4.10).  Consequently the rank-one determinant digit depends only
on the divisor evaluations $T(a)$, although those evaluations aggregate
all coefficients of $T$.  For the mixed-cubic
$F=u^a/Q^h$, the finite divisor support is the fixed five-point set
$0,1,-1,i,-i$.  This is a bounded-evaluation collapse, not a bounded-local-
jet theorem; (3.8)--(3.9) rule out the latter for the individual coordinates.

For a rank-zero row, write $P_s=T_s'$, which is $p$-integral when
$\deg P_s\le p-2$, and put
$\eta_s=F_s^{p-1}F_s'T_s\,dx$, $B_s=[F_s^pT_s]_0^1$.  Then



$$
\boxed{
 {L_1X_0-L_0X_1\over p^2}
 \equiv
 (-L(\eta_1))(B_0-pR(\eta_0))
 -(-L(\eta_0))(B_1-pR(\eta_1))\pmod p.}             \tag{4.13}
$$



Again the displayed quotient is legitimate under the stated integrality
hypothesis.  In the mixed-cubic application $F_s(0)=F_s(1)=0$, so all
the boundary terms in (4.10) and (4.13) vanish.

## 5. Exact item-149 band and the row $(m,p)=(6,7)$

For the mass-dominant $e_p=1$ rank-one bands, write



$$
6m=ap+r,\qquad4m+1=bp+t,qquad0\le r,t<p.                  \tag{5.1}
$$



The two degree inequalities force $t\ne0$.  Uniformly for
$1\le t\le p-1$, including the wrap $t=p-1$, one has



$$
F={u^a\over Q^{b+1}},\qquad
 P_0=u^rQ^{p-t},\qquad
 P_1=u^rQ^{p-t-1},\qquad P_0=QP_1.                            \tag{5.2}
$$



Their degrees are



$$
d_0=2r+3(p-t),\qquad d_1=d_0-3,                              \tag{5.3}
$$



and rank one means $d_0,d_1\le2p-2$.  This includes all wrap cases with
the same exponent convention; no separate fictitious $Q^{-1}$ term is
introduced.

At $(m,p)=(6,7)$,



$$
N=36,\quad K_0=25,\quad K_1=26,\quad
 a=5,\quad r=1,\quad b=3,\quad t=4,                          \tag{5.4}
$$



so



$$
F={u^5\over Q^4},\qquad P_0=uQ^3,qquad P_1=uQ^2,             \tag{5.5}
$$



with degrees $11,8\le12$.  Exact coefficient extraction gives



$$
\gamma_0=[x^6]P_0=0,\qquad
             \gamma_1=[x^6]P_1=-1.                           \tag{5.6}
$$



An independent rational Hermite reduction gives, modulo $7$,



$$
(V_R,V_L)=(4,2),\qquad
 (pR(\eta),L(\eta))=(2,2),\qquad B=0.                         \tag{5.7}
$$



Substitution into (4.10) yields



$$
{L_1(pR_0)-L_0(pR_1)\over7}
 \equiv-2\cdot2+4\cdot2\equiv4\pmod7.                       \tag{5.8}
$$



Since the numerator in (5.8) is $7A_m$, this proves



$$
A_6\equiv4\pmod7,
 \qquad v_7(7A_6)=1.                                         \tag{5.9}
$$



Here $q_p=p=7$ and the row is non-rank-zero, so
$\delta_{6,7}=0$.  The exact item-160 bridge therefore gives



$$
v_7(U_6)=v_7(q_pA_6)=1,\qquad v_7(c_6)=1.             \tag{5.10}
$$



The row is in $\mathcal H_6$, because $7<12$ and its two degrees are
at most $2p-2$; it is not rank zero because they are not both at most
$p-2=5$.  Thus (5.9) is precisely a sharp failure of the desired second
digit on an actual item-149 rank-one row.

## 6. Replay

The archived standard-library checker

`scripts/witt_endpoint_first_lift_checker.py`

reconstructs the exact mixed-cubic coordinates over $\mathbb Q$, verifies
$P_0=QP_1$, $[x^{p-1}]\Theta=0$, and $T'=\Theta$, and checks (4.10)
against the unreduced determinant.  It records



$$
v_7(7A_6)=1,\qquad v_7(A_6)=0,\qquad A_6\bmod7=4.
$$



Run it from the archive root with

```text
python scripts/witt_endpoint_first_lift_checker.py \\
  --output results/witt_endpoint_first_lift_checker.json
```

The checker is an audit of the symbolic proof, not the basis for it.
