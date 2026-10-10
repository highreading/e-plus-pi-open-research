> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 240 — the (j=1) Witt digit and the endpoint denominator tower

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Work on the actual (j=1) row


$$
p=2r+6s+3=4h+6s+3,\qquad r=2h,\qquad h,s\geq1,              \tag{1.1}
$$


and retain the two original coefficient coordinates $\nu=0,1$.
This item compares Item 234's coefficient-level Witt digit with
Item 238's squared-denominator endpoint state.

**PROVED — exact bridge for the Hermite carry.**  Let
$v_t^{\sin}$ be the squared-denominator endpoint moment with numerator
$q_{\sin}(n)=(0,1,0,-1)$ for $n\bmod4=0,1,2,3$.  Then


$$
\begin{aligned}
 J_0&=2\epsilon(v_0^{\sin}+v_1^{\sin}
                    +v_2^{\sin}+v_3^{\sin}),\\
 J_1&=2\epsilon(v_0^{\sin}+4v_1^{\sin}+6v_2^{\sin}
                    +4v_3^{\sin}+v_4^{\sin})                 \tag{1.2}
\end{aligned}
$$


in $\mathbb F_p$, with $\epsilon=(-1)^{(p-1)/2}$.  The proof is
termwise and certifies every sign, index window, and denominator.

**PROVED — the exact extra-digit compatibility.**  On the original
per-coordinate common-log gate $p^2\mid C_\nu$, put
$M_\nu^{(1)}=M_\nu/p\pmod p$ and define


$$
\begin{aligned}
 V_0^{\sin}&=v_0^{\sin}+v_1^{\sin}+v_2^{\sin}+v_3^{\sin},\\
 V_1^{\sin}&=v_0^{\sin}+4v_1^{\sin}+6v_2^{\sin}
                       +4v_3^{\sin}+v_4^{\sin}.
                                                                  \tag{1.3}
\end{aligned}
$$


Item 234's $j=1$ Witt digit satisfies


$$
\boxed{\quad
 \Omega_\nu^W=-6\epsilon M_\nu^{(1)}
                  +12\epsilon V_\nu^{\sin}+E_\nu .\quad}       \tag{1.4}
$$


Consequently, still conditional on $p^2\mid C_\nu$,


$$
\boxed{\quad p^3\mid C_\nu
 \iff M_\nu^{(1)}=2V_\nu^{\sin}
                 +(6\epsilon)^{-1}E_\nu\pmod p.\quad}          \tag{1.5}
$$


Here $\Omega^W$ is Item 234's $j=1$ quantity; it is unrelated to
Item 224's $j=2$ notation.

**PROVED — all-level denominator recurrence and endpoint
factorization.**  For every $k\geq2$, the order-$k$ endpoint moment
satisfies


$$
\bar B_tV_t^{(k)}-\bar C_tV_{t+1}^{(k)}
 +\bar D_tV_{t+2}^{(k)}-\bar A_tV_{t+3}^{(k)}
 =V_t^{(k-1)}-V_{t+1}^{(k-1)}
  +V_{t+2}^{(k-1)}-V_{t+3}^{(k-1)}.                           \tag{1.6}
$$


There is no factor $k-1$.  On the three endpoint Fourier modes,
every terminal map factors through the ordinary-denominator terminal
map.  Thus no denominator power adds a fourth endpoint mode.  At a
terminal, level $k$ determines the free fourth coordinate at level
$k-1$ and releases the fourth coordinate at level $k$; it does not
create a new one-terminal scalar compatibility.

**PROVED — sharply scoped universal-linear obstruction.**  At
$(p,h,s,\nu)=(29,5,1,1)$, on the full coefficient space
$\mathbb F_{29}[z]_{\leq16}$, the six endpoint functionals with
denominator powers one and two have rank six, while adjoining the
Item 234 functional $E$ raises the rank to seven.  Therefore $E$
is not a universal $\mathbb F_{29}$-linear functional of the $(u,v)$
endpoint state on that specified polynomial input space.

This last theorem is deliberately narrow.  It is not an obstruction to
a nonlinear formula, an identity restricted to the actual binomial
family, or a formula whose coefficients are singular at $p=29$.

**EXACT FINITE ONLY.**  At the row $(109,10,11,0)$, adjoining all
three endpoint modes at every denominator power through $k=12$ still
leaves $E$ outside the tested span.  This is evidence, not an
all-power theorem.

**OPEN.**  It remains open whether $E_\nu$ has a finite enlarged
recurrence with a genuinely new endpoint mode, whether an
actual-family-specific identity eliminates it, and whether it is tied
to Item 237's all-$h$ residual.  No simultaneous common-log
exclusion, density estimate, or Route-1 rate is claimed.

## 2. Endpoint tower and support

Put


$$
W(z)=(1-z)^r(1+z^2)^{2s-1}=\sum_dw_dz^d,
 \qquad N_{t,d}=p+r+t+d+1.                                   \tag{2.1}
$$


On the three-dimensional four-periodic mode space


$$
\begin{array}{c|rrrr}
n\bmod4&0&1&2&3\\ \hline
q_0(n)&1&1&1&1\\
q_c(n)&1&0&-1&0\\
q_{\sin}(n)&0&1&0&-1
\end{array}                                                    \tag{2.2}
$$


define, for every $k\geq1$,


$$
V_t^{(k)}(q)=
 \sum_{\substack d\\p\nmid N_{t,d}}}
 {w_dq(N_{t,d})\over N_{t,d}^k}\pmod p.                      \tag{2.3}
$$


Every retained denominator is a $p$-unit by definition.  Item 238's
ordinary and squared coordinates are $V^{(1)}$ and $V^{(2)}$.
We abbreviate


$$
v_t^{\sin}=V_t^{(2)}(q_{\sin}).            \tag{2.4}
$$



For the two coefficient coordinates set


$$
\begin{aligned}
 q_\nu&=2s-\nu,\\
 P_0&=(1+z)(1+z^2)W,\\
 P_1&=(1+z)^4W,\\
 d_\nu&=\deg P_\nu=r+4s+1+\nu.                              \tag{2.5}
\end{aligned}
$$


Write $P_\nu=\sum_{a=0}^{d_\nu}p_{\nu,a}z^a$.  Each factor in
$P_\nu$ is reciprocal, because $r$ is even; hence


$$
p_{\nu,a}=p_{\nu,d_\nu-a}.           \tag{2.6}
$$



## 3. Termwise proof of the $J$-bridge

Item 234 defines


$$
J_\nu=
 \sum_{\substack{0\leq a\leq d_\nu\\D_{\nu,a}\ \mathrm{odd}}}
 {2\epsilon(-1)^{(D_{\nu,a}-1)/2}p_{\nu,a}
       \over D_{\nu,a}(D_{\nu,a}-p)},
 \qquad D_{\nu,a}=2p-q_\nu-1-a.                             \tag{3.1}
$$


The complete denominator window is


$$
\begin{aligned}
 p+r+1&\leq D_{\nu,a}\leq2p-q_\nu-1<2p,\\
 r+1&\leq D_{\nu,a}-p\leq p-q_\nu-1<p.                      \tag{3.2}
\end{aligned}
$$


Thus $D_{\nu,a}$ and $D_{\nu,a}-p$ are both $p$-units.

Let $b=d_\nu-a$.  The row equation and (2.5) give the exact index
identity


$$
\begin{aligned}
 D_{\nu,a}
 &=2p-q_\nu-1-d_\nu+b\\
 &=p+r+b+1=N_{0,b}.                                           \tag{3.3}
\end{aligned}
$$


Moreover, for every integer $D$,


$$
\mathbf1_{D\ \mathrm{odd}}(-1)^{(D-1)/2}=q_{\sin}(D).       \tag{3.4}
$$


Since $D(D-p)\equiv D^2\pmod p$, equations (2.6), (3.3), and
(3.4) give, with no endpoint truncation,


$$
J_\nu
 =2\epsilon\sum_{b=0}^{d_\nu}
 {p_{\nu,b}q_{\sin}(N_{0,b})\over N_{0,b}^2}\pmod p.         \tag{3.5}
$$



Finally expand the short multipliers in (2.5):


$$
\begin{aligned}
 (1+z)(1+z^2)&=1+z+z^2+z^3,\\
 (1+z)^4&=1+4z+6z^2+4z^3+z^4.                               \tag{3.6}
\end{aligned}
$$


Coefficientwise convolution of (3.5) with (3.6) is exactly (1.2).
This proves every sign and the terminal indices $0,\ldots,3$ and
$0,\ldots,4$.

## 4. Which hypothesis forces the Witt compatibility

The logical order is important.

1. Item 234 proves $p\mid C_\nu$ for every actual row by an exact
   support zero.
2. The original per-coordinate common-log gate is
   

$$
p^2\mid C_\nu
       \iff Q_\nu=0\pmod p
       \iff M_\nu\in p\mathbb Z_{(p)}.                       \tag{4.1}
$$


   Only after this gate is $M_\nu^{(1)}=M_\nu/p\pmod p$
   introduced.
3. On that gate, Item 234 proves
   

$$
{C_\nu\over p^2}=\Omega_\nu^W
      =-6\epsilon M_\nu^{(1)}+6J_\nu+E_\nu\pmod p.           \tag{4.2}
$$


   Substitution of (1.2) gives (1.4).
4. The extra multiplicity hypothesis is $p^3\mid C_\nu$.  Dividing
   by $p^2$ is legitimate because step 2 is already assumed, so
   (4.2) proves precisely (1.5).

No extra endpoint multiplicity $M_\nu\in p^2\mathbb Z_{(p)}$ is
assumed in (1.5).  If it is imposed separately, then (1.5) reduces to
$12\epsilon V_\nu^{\sin}+E_\nu=0$.  That is a stronger combined
hypothesis, not the original coefficient gate.

## 5. Proof of the all-power recurrence

Let


$$
\Sigma(z)=(1-z)(1+z^2),\qquad
 K_t(z)=z^{p+r+t+1}\Sigma(z)W(z).                             \tag{5.1}
$$


Direct differentiation and the logarithmic derivative of $W$ give
the polynomial identity


$$
\begin{aligned}
 K_t'(z)={}&B_tz^{p+r+t}W-C_tz^{p+r+t+1}W\\
           &+D_tz^{p+r+t+2}W-A_tz^{p+r+t+3}W,                 \tag{5.2}\\
 A_t&=p+2r+4s+t+2,&B_t&=p+r+t+1,\\
 C_t&=p+2r+t+2,&D_t&=p+r+4s+t+1.                             \tag{5.3}
\end{aligned}
$$


Reduce these four coefficients modulo $p$ to obtain
$\bar A_t,\bar B_t,\bar C_t,\bar D_t$.

For a monomial define the pole-deleted functional


$$
\Lambda_k(z^{N-1})=
 \begin{cases}
  q(N)/N^k,&p\nmid N,\\
  0,&p\mid N.
 \end{cases}                                                   \tag{5.4}
$$


If $p\nmid N$, then
$\Lambda_k((z^N)')=q(N)/N^{k-1}$.  If $p\mid N$, the
derivative coefficient $N$ is zero in $\mathbb F_p$, while the
pole-deleted right side is also zero.  Therefore


$$
\Lambda_k(F')=\Lambda_{k-1}(F)        \tag{5.5}
$$


for every polynomial $F$, interpreted with the same deletion rule.

Apply (5.5) to (5.1), and then use
$\Sigma=1-z+z^2-z^3$.  The right side of (5.2) yields the left
side of (1.6); $K_t$ yields the alternating difference on the right
side.  This proves (1.6) for every $k\geq2$, every integer $t$, and
every mode in (2.2).  The derivative cancels one denominator, so no
factor $k-1$ occurs.

## 6. Terminal factorization and the surviving coordinate

Let $T=2s+1$, and define the terminal map


$$
\Phi_k(q)=
 \bigl(V_T^{(k)}(q),V_{T+1}^{(k)}(q),V_{T+2}^{(k)}(q)\bigr)^t.
                                                                  \tag{6.1}
$$


Item 238 proves for every actual row that $\Phi_1$ is invertible on
the mode space (2.2).  Hence, for each fixed $k$,


$$
K_k=\Phi_k\Phi_1^{-1},\qquad
                  \Phi_k=K_k\Phi_1.                           \tag{6.2}
$$


If $(\tau q)(n)=q(n+p)$, then the state at the $a$-th phase is
$\Phi_k(\tau^{a-2}q)$, so (6.2) holds at every phase, not only the
first.  Every denominator level is therefore a linear image of the same
three endpoint Fourier modes.

At


$$
t_a=T+(a-2)p                                                    \tag{6.3}
$$


one has $\bar A_{t_a}=0$, and the other three coefficients are


$$
b=r+2s+2,\qquad c=2r+2s+3,\qquad d=r+6s+2.                    \tag{6.4}
$$


Equation (1.6) becomes


$$
\begin{aligned}
 V_{t_a+3}^{(k-1)}={}&V_{t_a}^{(k-1)}-V_{t_a+1}^{(k-1)}
                         +V_{t_a+2}^{(k-1)}\\
 &-bV_{t_a}^{(k)}+cV_{t_a+1}^{(k)}-dV_{t_a+2}^{(k)}.           \tag{6.5}
\end{aligned}
$$


Thus level $k$ fixes the free post-terminal coordinate at level
$k-1$ while $V_{t_a+3}^{(k)}$ remains free.  Iterating the
denominator tower shifts the free coordinate upward; it does not create
a new scalar compatibility at one terminal.

The exact bridge (1.4) therefore isolates the surviving coordinate:
the $J$-part is already in the squared endpoint state, whereas the
harmonic/quadratic Frobenius defect $E_\nu$ is not eliminated by the
proved endpoint-tower identities.

## 7. Exact rank witness for (E)

The following theorem concerns universal linear functionals, not just
the single actual polynomial.  Fix


$$
(p,h,s,\nu)=(29,5,1,1),\qquad q_\nu=1,qquad d_\nu=16,        \tag{7.1}
$$


and let
$\mathcal P_{16}=\{\sum_{a=0}^{16}c_az^a:c_a\in\mathbb F_{29}\}$.
Put


$$
D_a=2p-q_\nu-1-a=56-a.                \tag{7.2}
$$


For $q\in\{q_0,q_c,q_{\sin}\}$ and $k=1,2$, define


$$
T_{q,k}(c)=\sum_{a=0}^{16}{c_aq(D_a)\over D_a^k}.       \tag{7.3}
$$



To identify the seventh functional without circularity, let


$$
\mathcal H_E=L(A_1,B_1)+K(A_0,B_0)                           \tag{7.4}
$$


be exactly the Item 234 harmonic-plus-quadratic kernel, including its
Frobenius sections.  With $N=3p-q_\nu-1=85$, coefficient extraction
is linear in the input polynomial:


$$
E(c)=[z^N]\mathcal H_E(z)\sum_{a=0}^{16}c_az^a
     =\sum_{a=0}^{16}c_a[z^{N-a}]\mathcal H_E(z).              \tag{7.5}
$$


Thus the seventh matrix column is the universal Item 234 $E$-weight,
not a fit to the actual row.

In the ordered columns


$$
T_{q_0,1},T_{q_c,1},T_{q_{\sin},1},
 T_{q_0,2},T_{q_c,2},T_{q_{\sin},2},E,                        \tag{7.6}
$$


the explicit $17\times7$ matrix is stored in the deterministic
certificate.  Exact Gaussian elimination in $\mathbb F_{29}$ gives


$$
\operatorname {rank}(T_{q,1},T_{q,2})=6,\qquad
 \operatorname {rank}(T_{q,1},T_{q,2},E)=7.                   \tag{7.7}
$$


The row-major matrix SHA-256 is


$$
\texttt{90da523107e3f89122e5b33f71dec7fa093b21787ec747a269210832cab51659}.
                                                                  \tag{7.8}
$$


The certificate includes all matrix entries, each row hash, and
explicit nonzero maximal minors.  It also verifies the identification
(7.5) in two independent ways:

- on every one of the 368 actual direct-replay polynomials, kernel
  pairing equals both the frozen Item 234 $E_\nu$ and a separate
  direct sectioned-convolution calculation;
- on all 17 standard basis vectors of $\mathcal P_{16}$, each kernel
  weight equals the direct sectioned-convolution value.

It follows rigorously from (7.7) that no universal
$\mathbb F_{29}$-linear expression in the six $(u,v)$ endpoint
functionals equals $E$ on $\mathcal P_{16}$.

This does **not** exclude:

- a nonlinear relation;
- a relation valid only on the actual one-parameter binomial family;
- a relation involving a new kernel state rather than denominator
  powers; or
- a rational all-row formula with a denominator that vanishes at
  $p=29$.

## 8. Deterministic replay and finite evidence

The standard-library checker
`work/item240_j1_witt_endpoint_bridge_certificate.py` verifies, by
default:

- (1.2) for all 368 coordinates in the 184 actual rows through
  $p\leq151$;
- the kernel/direct/frozen identification of $E$ on the same 368
  polynomials;
- 13,800 instances of (1.6), for all three modes and powers
  $2\leq k\leq6$;
- the terminal factorization (6.2) at every tested row;
- (1.4) against Item 234 on each of the three individual first-gate
  records through $p\leq151$; and
- the exact rank witness (7.7), including 17 basis-vector checks.

At $(p,h,s,\nu)=(109,10,11,0)$, the ranks after retaining all three
modes through denominator power $K$ are


$$
\begin{array}{c|rrrrrrrrrrrr}
K&1&2&3&4&5&6&7&8&9&10&11&12\\ \hline
\text{tower rank}&3&6&9&12&15&18&21&24&27&30&33&36\\
\text{with }E&4&7&10&13&16&19&22&25&28&31&34&37.
\end{array}                                                     \tag{8.1}
$$


Equation (8.1) is **EXACT FINITE ONLY**.  It does not prove that $E$
stays outside the infinite denominator-power tower.

## 9. Final ledger

### PROVED

- The termwise identities (1.2), with the exact windows and signs.
- The conditional Witt bridge (1.4) and extra-$p^3$ equivalence
  (1.5).
- The all-$k$ coupled recurrence (1.6), including its terminal
  free-coordinate law (6.5).
- Factorization of every denominator-power terminal map through the
  ordinary three-mode state.
- The scoped $\mathbb F_{29}$-linear rank obstruction (7.7) on
  $\mathcal P_{16}$.

### EXACT FINITE ONLY

- Every replay count, first-gate record, matrix digest, and bounded
  power-span calculation in the companion certificate.
- The $K\leq12$ evidence (8.1).

### OPEN

- A finite enlarged recurrence for $E_\nu$ with a genuinely new
  endpoint mode.
- A nonlinear or actual-family-specific formula eliminating $E_\nu$.
- An all-power obstruction for the denominator tower.
- An all-$h$ relation between $E_\nu$ and Item 237's residual.
- Any all-prime common-log exclusion, zero-density theorem, Route-1
  exponent, or conclusion about $e+\pi$.
