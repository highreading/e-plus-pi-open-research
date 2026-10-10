> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 238 — squared-denominator recurrence and corrected $j=1$ lifted closure

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the actual $j=1$ rows


$$
p=2r+6s+3,\qquad r=2h,\qquad h,s\geq1,                        \tag{1.1}
$$


and the Item 234 squared-denominator coordinate $v_t$.

**PROVED — exact coupled recurrence.**  Put


$$
\begin{aligned}
\bar A_t&=2r+4s+t+2,&\bar B_t&=r+t+1,\\
\bar C_t&=2r+t+2,&\bar D_t&=r+4s+t+1
\end{aligned}                                                  \tag{1.2}
$$


in $\mathbb F_p$.  If $u_t=\widehat u_t\bmod p$, then


$$
\boxed{\;
\bar B_tv_t-\bar C_tv_{t+1}+\bar D_tv_{t+2}-\bar A_tv_{t+3}
=u_t-u_{t+1}+u_{t+2}-u_{t+3}.\;}                              \tag{1.3}
$$


The proof compares the exact regularized Pearson equations at $t$ and
$t+2p$, with every sign retained.  A $t$-versus-$t+4p$ proof
establishes the same identity for arbitrary endpoint-mode data.

**PROVED — corrected coefficientwise phase law.**  For every polynomial
endpoint mode $q$ in the three-mode space defined below, and every
integer $k$,


$$
\begin{aligned}
 \widehat U_{t+kp}(q)
 &\equiv\widehat U_t(\sigma^kq)
       -kp\,V_t(\sigma^kq)\pmod {p^2},\\
 V_{t+kp}(q)&=V_t(\sigma^kq)\pmod p,                            \tag{1.4}
\end{aligned}
$$


where $(\sigma q)(n)=q(n+p)$.  For the actual numerator
$q_\epsilon(n)=\ell_{n-1}$, this becomes


$$
\begin{aligned}
 \widehat u_{t+2p}+\widehat u_t&\equiv2p\,v_t\pmod {p^2},\\
 \widehat u_{t+4p}-\widehat u_t&\equiv-4p\,v_t\pmod {p^2}.
                                                                  \tag{1.5}
\end{aligned}
$$



**PROVED — endpoint-mode redundancy.**  On the three-dimensional
endpoint-mode space $\mathcal E=\langle1,i^n,(-i)^n\rangle$, define
the ordinary and squared-denominator terminal maps $\Phi,\Psi$.
Item 233's all-row argument proves that $\Phi$ is invertible.  Hence


$$
K=\Psi\Phi^{-1}                            \tag{1.6}
$$


is defined on every actual row, and at every terminal phase


$$
V_a=K\overline Y_a.                    \tag{1.7}
$$


Thus $v_t$ adds no fourth endpoint Fourier mode.  It is an explicit
linear carry attached to the existing three-mode state.

**PROVED — sharply scoped one-terminal no-go.**  At


$$
t_a=2s+1+(a-2)p
$$


the coefficient $\bar A_{t_a}$ vanishes.  The old terminal equation is
a scalar compatibility.  Equation (1.3) then determines the previously
free $u_{t_a+3}$, while $v_{t_a+3}$ remains free.  Therefore adjoining
$v$ creates no new scalar compatibility at a single terminal.

**SCOPED CONCLUSION.**  The corrected phase closures are


$$
\begin{aligned}
 Y_{a+2}+Y_a&\equiv2pK\overline Y_a\pmod {p^2},\\
 Y_{a+4}-Y_a&\equiv-4pK\overline Y_a\pmod {p^2}.                \tag{1.8}
\end{aligned}
$$


They are not the naive antiperiod/period equations, but their right sides
are already determined by the ordinary endpoint mode.  Consequently the
squared carry alone yields no invariant independent of the original
first-digit terminal state.

**OPEN.**  Item 238 does not prove that (1.8) is redundant after the
additional hypothesis $p^3\mid C_0,C_1$, equivalently
$\Omega_0^W=\Omega_1^W=0$ on the original common-log gate.  That
requires a full lift of Item 233's terminal-residual identity.  No
common-log exclusion or Route-1 rate is claimed.

**EXACT FINITE ONLY.**  The direct replay covers all 184 rows through
$p\leq151$.  A separate endpoint-map census covers all 2,435 rows
through $p\leq601$.  Those bounds are evidence and regression coverage,
not ingredients of the all-row proofs.

## 2. Regularized mode functionals

Put


$$
W(z)=(1-z)^r(1+z^2)^{2s-1}=\sum_dw_dz^d,\qquad
 T=2s+1,                                                       \tag{2.1}
$$


and, for a four-periodic endpoint numerator $q$, let


$$
N_{t,d}=p+r+t+d+1.                                            \tag{2.2}
$$


Define


$$
\begin{aligned}
 \widehat U_t(q)
 &=\sum_{\substack d\\p\nmid N_{t,d}}
     {w_dq(N_{t,d})\over N_{t,d}}\in\mathbb Z_{(p)},\\
 V_t(q)
 &=\sum_{\substack d\\p\nmid N_{t,d}}
     {w_dq(N_{t,d})\over N_{t,d}^2}\pmod p.                    \tag{2.3}
\end{aligned}
$$


Every retained denominator is a $p$-unit by definition.  For the
actual Item 223 functional,


$$
q_\epsilon(n)=\ell_{n-1}.                                    \tag{2.4}
$$


Then


$$
\widehat u_t=\widehat U_t(q_\epsilon),\qquad
 v_t=V_t(q_\epsilon).                                         \tag{2.5}
$$



The deleted-denominator set in (2.3) is unchanged by $t\mapsto t+kp$.
Term by term,


$$
{1\over N+kp}\equiv {1\over N}-{kp\over N^2}\pmod {p^2}.
                                                                  \tag{2.6}
$$


Since $q(N+kp)=(\sigma^kq)(N)$, summing (2.6) proves (1.4)
coefficientwise for arbitrary mode data.

The actual numerator satisfies


$$
\sigma^2q_\epsilon=-q_\epsilon,\qquad
 \sigma^4q_\epsilon=q_\epsilon.                               \tag{2.7}
$$


Substitution in (1.4) gives exactly the two signs in (1.5).

## 3. The $t$-versus-$t+2p$ recurrence

Let


$$
\begin{aligned}
 A_t&=p+2r+4s+t+2,&B_t&=p+r+t+1,\\
 C_t&=p+2r+t+2,&D_t&=p+r+4s+t+1,                              \tag{3.1}
\end{aligned}
$$


and use the signed Pearson row


$$
\mathcal R_t(X)
 =B_tX_t-C_tX_{t+1}+D_tX_{t+2}-A_tX_{t+3}.                   \tag{3.2}
$$


For a mode $q$, exact pole deletion gives


$$
\mathcal R_t(\widehat U(q))
 =S_t(q),\qquad
 S_t(q)=-\sum_{b\geq1}[z^{bp}]K_t\,q(bp),                     \tag{3.3}
$$


where


$$
K_t=z^{p+r+t+1}(1-z)(1+z^2)W.                               \tag{3.4}
$$



For $q=q_\epsilon$, multiplication of $K_t$ by $z^{2p}$
and (2.7) give


$$
S_{t+2p}(q_\epsilon)=-S_t(q_\epsilon).                        \tag{3.5}
$$


All four unsigned coefficients in (3.1) increase by $2p$.
Because of the alternating signs in (3.2), their signed increment is


$$
2p(1,-1,1,-1).                                               \tag{3.6}
$$


Use (1.5) componentwise:


$$
\widehat u_{t+2p+j}\equiv-\widehat u_{t+j}
             +2pv_{t+j}\pmod {p^2}\qquad(0\leq j\leq3).        \tag{3.7}
$$


Equations (3.2), (3.6), and (3.7) give


$$
\begin{aligned}
\mathcal R_{t+2p}(\widehat u)
\equiv{}&-\mathcal R_t(\widehat u)
+2p\{\overline{\mathcal R}_t(v)
 -(u_t-u_{t+1}+u_{t+2}-u_{t+3})\}\pmod {p^2}.                 \tag{3.8}
\end{aligned}
$$


The first terms on the two sides cancel by (3.3) and (3.5).  Dividing
the remaining congruence by $2p$ proves (1.3), with the signs shown.

For an arbitrary $q\in\mathcal E$, compare $t$ and $t+4p$
instead.  Then $S_{t+4p}(q)=S_t(q)$, every coefficient increases by
$4p$, and (1.4) gives


$$
\widehat U_{t+4p}(q)
\equiv\widehat U_t(q)-4pV_t(q)\pmod {p^2}.                    \tag{3.9}
$$


The same cancellation proves the $q$-version of (1.3).  Thus the
coupled recurrence is valid on the full three-mode space, not merely
for the actual numerator.

## 4. What happens at a terminal

Set


$$
t_a=T+(a-2)p,\qquad a\geq2.                                  \tag{4.1}
$$


Then


$$
A_{t_a}=ap,\qquad \bar A_{t_a}=0.                             \tag{4.2}
$$


The remaining reduced coefficients are independent of $a$:


$$
b=r+2s+2,\qquad c=2r+2s+3,\qquad d=r+6s+2.                   \tag{4.3}
$$


They lie strictly between $0$ and $p$.

As in Item 234, the support of $K_{t_a}$ contains one deleted
multiple, its top exponent $ap$, with coefficient $-1$.  Therefore
the ordinary terminal compatibility for a mode $q$ is


$$
bu_{t_a}-cu_{t_a+1}+du_{t_a+2}=q(ap).         \tag{4.4}
$$


Equation (1.3) at the same index is


$$
\begin{aligned}
 bv_{t_a}-cv_{t_a+1}+dv_{t_a+2}
 =u_{t_a}-u_{t_a+1}+u_{t_a+2}-u_{t_a+3}.                      \tag{4.5}
\end{aligned}
$$


It contains no $v_{t_a+3}$.  Instead it gives


$$
\boxed{\;
u_{t_a+3}
=u_{t_a}-u_{t_a+1}+u_{t_a+2}
-bv_{t_a}+cv_{t_a+1}-dv_{t_a+2}.\;}                           \tag{4.6}
$$


Thus (4.5) consumes the free $u$-digit left by (4.4), while releasing
the next free $v$-digit.  The number of scalar compatibilities does
not increase at one terminal.  This is an exact structural statement,
not a dimension count inferred from samples.

## 5. The three-mode space and the matrix $K$

Let $\mathcal E$ be the three-dimensional space with basis


$$
\begin{array}{c|rrrr}
n\bmod4&0&1&2&3\\ \hline
q_0(n)&1&1&1&1\\
q_c(n)&1&0&-1&0\\
q_s(n)&0&1&0&-1.
\end{array}                                                    \tag{5.1}
$$


These are the endpoint modes $1,i^n,(-i)^n$, written over the base
field.  The missing fourth Fourier mode is $(-1)^n$.  The actual
numerator is


$$
q_\epsilon=4\epsilon q_c-2q_s.          \tag{5.2}
$$



At the first upper terminal define


$$
\begin{aligned}
 \Phi(q)&=(\widehat U_T(q),\widehat U_{T+1}(q),
                         \widehat U_{T+2}(q))^t\bmod p,\\
 \Psi(q)&=(V_T(q),V_{T+1}(q),V_{T+2}(q))^t.                    \tag{5.3}
\end{aligned}
$$


Both maps are explicit finite binomial sums from (2.1)--(2.3).

For completeness, recall why $\Phi$ is invertible on every actual row.
The coefficientwise Pearson identity gives a terminal covector
$\alpha$ and a phase matrix $N$ satisfying


$$
\alpha\Phi(q)=q(2p),\qquad \Phi(\sigma q)=N\Phi(q).            \tag{5.4}
$$


If $\Phi(q)=0$, iteration gives


$$
q(2p)=q(3p)=q(4p)=0.                     \tag{5.5}
$$


On the basis (5.1), these are three consecutive evaluations of the
distinct phase roots $1,i^p,(-i)^p$.  Their Vandermonde determinant is
nonzero for odd $p$.  Hence $q=0$; since both spaces have dimension
three, $\Phi$ is an isomorphism.

Define $K$ by (1.6).  At the $a$-th terminal,


$$
\begin{aligned}
 \overline Y_a(q)&=\Phi(\sigma^{a-2}q),\\
 V_a(q)&=\Psi(\sigma^{a-2}q)
        =K\overline Y_a(q).                                   \tag{5.6}
\end{aligned}
$$


This proves (1.7) for arbitrary mode data and every phase.

Applying (1.4) componentwise to the three-entry terminal state and then
using (5.6) gives, for the actual numerator, the corrected closures
(1.8).  The equations are genuine $p^2$ corrections, but the carry
vector is a fixed linear image of the already existing endpoint state.

## 6. Consequence for independence

There are three separate levels:

1. **Original common-log gate.**  This is a first-digit hypothesis:
   $p^2\mid C_0,C_1$, equivalently the two Item 223 endpoint moments
   vanish modulo $p$.  At this level $v$ adds no endpoint mode by
   (5.6), and one terminal adds no scalar compatibility by (4.6).
2. **Extra integer multiplicity.**  On the original gate, the additional
   hypothesis $p^3\mid C_0,C_1$ is
   $\Omega_0^W=\Omega_1^W=0$, where $\Omega^W$ is Item 234's
   $j=1$ Witt digit.  It is not the $j=2$ notation of Item 224.
3. **Full lifted terminal system.**  Determining whether (1.8) adds a
   scalar condition after level 2 requires lifting the complete
   Item 233 terminal-residual identity, including the remaining
   second-digit state parameter.

Items 234 and 238 do not identify level 2 with a complete lifted terminal
state.  Therefore no claim of independence or redundancy is made at
level 3.  What is proved is the narrower no-go:

> The squared-denominator carry supplies neither a fourth endpoint mode
> nor a new one-terminal scalar compatibility.  Its corrected phase
> closure is automatic coefficientwise for arbitrary endpoint-mode data.

This rules out treating $v_t$ as a new independent first-digit
obstruction.  It does not rule out a subtler invariant after the extra
$p^3$ hypothesis.

## 7. Deterministic replay and finite status

The standard-library checker
work/item238_j1_squared_carry_certificate.py verifies on every actual row
through $p\leq151$:

- 17,610 instances of the coupled recurrence (1.3);
- 2,208 terminal free-digit identities (4.6);
- 13,248 arbitrary-mode $p,2p,4p$ phase identities (1.4);
- the actual $2p/4p$ closures (1.5); and
- $V_a=K\overline Y_a$ for all three basis modes and four phases.

The separate finite endpoint-map census through $p\leq601$ contains
2,435 rows.  In all of them $\Phi$ is invertible and the stacked map
$(\Phi,\Psi)$ has rank three, as the theorem requires.  The ranks of
$\Psi$ alone are


$$
\begin{array}{c|rrrr}
\operatorname {rank}\Psi&0&1&2&3\\ \hline
\text{rows}&0&0&7&2428.
\end{array}                                                     \tag{7.1}
$$


The $K$-row stream has SHA-256


$$
\texttt{bb6448a2c6d8f50a17922d737f75887984667430243a6f35b57e2dc64d5d959e}.
\tag{7.2}
$$


Every count and nonoccurrence in this section is
**EXACT FINITE ONLY**.

## 8. Final ledger

### PROVED

- The coupled inhomogeneous recurrence (1.3), including all signs.
- The arbitrary-mode phase law (1.4) and actual corrected closures (1.5).
- The exact terminal formula (4.6) and one-terminal no-go.
- All-row invertibility of $\Phi$, the explicit map
  $K=\Psi\Phi^{-1}$, and endpoint-mode redundancy (5.6).
- The scoped conclusion that $v_t$ is not an independent first-digit
  endpoint coordinate.

### EXACT FINITE ONLY

- Every replay count, rank count, sample matrix, and stream digest in
  the companion certificate.

### OPEN

- Independence or redundancy of the corrected closure after the extra
  $p^3$/$\Omega^W$ hypothesis.
- A full $p^2$ lift of Item 233's terminal-residual redundancy formula.
- Any all-prime common-log exclusion, weighted zero-rate theorem, Route-1
  exponent, or conclusion about $e+\pi$.
