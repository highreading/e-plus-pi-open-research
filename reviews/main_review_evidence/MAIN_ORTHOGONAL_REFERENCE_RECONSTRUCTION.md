> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Primary reconstruction: monic Legendre reference quantities and complete tails

Reviewer: main Codex. This verifies existing archive lemmas without a priority claim or a new e+π proof. The source remains unchanged.

Use the archive's monic normalization



$$
p_k(t)=\frac{i^k\operatorname{Leg}_k(-i(2t-1))}{\binom{2k}{k}},
\quad A_k=p_k(1),\quad
h_k=\frac{2(-1)^k}{(2k+1)\binom{2k}{k}^2}.
$$



Write $R=\sqrt2$, $M=1+R$, $s=M^{-2}$, and $a=M/4$. The three-term recurrence gives
$p_{k+1}=(t-1/2)p_k+\beta_kp_{k-1}$，
$\beta_k=k^2/[4(4k^2-1)]$. Initial values are $p_0=1$ and $p_1=t-1/2$.

## 1. Constant bounds at the endpoint

Set $B_k=\binom{2k}{k}$ and $c_k=B_k/4^k$. Rodrigues or the Legendre generating function gives



$$
\sum_{k\ge0}B_kA_kx^k=(1-2x-x^2)^{-1/2}.
$$



Thus $B_kA_k=M^kd_k$, where



$$
d_k=\sum_{l=0}^k(-s)^l c_lc_{k-l}.
$$



The adjacent ratio of absolute terms is at most $2s<1$:
$c_{l+1}/c_l\le1$ and $c_{j-1}/c_j=2j/(2j-1)\le2$. The finite alternating sum lies between its first term and the sum of its first two terms, so



$$
(1-s)c_k\le d_k\le c_k,
\qquad (1-s)a^k\le A_k\le a^k.
$$



The lower bound also follows directly from the endpoint recurrence: $A_0/a^0=1$, $A_1/a=1-s$, and the two weights in the normalized recurrence sum to at least one.

Endpoint ratios $b_k=A_{k+1}/A_k$ satisfy
$b_0=1/2$, $b_k=1/2+\beta_k/b_{k-1}$. Using $\beta_k\le1/12$, induction gives
$1/2\le b_k\le2/3$。

Also $c_k\ge1/(2\sqrt{k})$ for $k\ge1$, with equality initially and subsequent induction from
$(2k+1)/(2k+2)\ge\sqrt{k/(k+1)}$. The sequence
$(2k+1)c_k^2$ decreases from one; its adjacent ratio is
$1-1/[4(k+1)^2]$。

## 2. Sign and bounds of the complete second-kind error

Set


$$
v_k=\int_{-1}^1\frac{p_k((1+iu)/2)}{1-(1+iu)/2}\,du,
\quad I_k=\int_0^\infty(1+R\cosh u)^{-k-1}\,du.
$$



Here $I_k$ is a positive convergent integral. Integrating the derivative of
$\sinh u/(1+R\cosh u)^{k+1}$ gives, for $k\ge1$,



$$
(k+1)I_{k+1}=kI_{k-1}-(2k+1)I_k.
$$



The boundary at $k=0$ gives $I_0+I_1=1$. Substitution $y=\tanh(u/2)$ yields
$I_0=2\arctan(R-1)=\pi/4$. On the other hand, $v_0=\pi$,
$v_1=\pi/2-2$, and orthogonality gives the same three-term recurrence for $v_k$.
Comparing initial values and recurrences gives the exact identity



$$
v_k=\frac{4(-1)^kI_k}{B_k}.
$$



Hence $w_k=(-1)^kv_k>0$. The recurrence gives
$w_{k+1}=-w_k/2+\beta_kw_{k-1}$, and
$0<w_{k+1}/w_k<2\beta_{k+1}\le1/6$。

The Wronskian identity
$A_{k+1}v_k-A_kv_{k+1}=h_k$ holds from the $k=0$ initial values and recurs by $-\beta_k$. Therefore



$$
\theta_k:=\frac{v_kA_k}{h_k}
=\frac1{A_{k+1}/A_k+w_{k+1}/w_k},
\qquad 1\le\theta_k\le2.
$$



Thus $\epsilon_k=|v_k|/A_k$ satisfies, for $k\ge1$,



$$
2s^k\le\epsilon_k\le\frac{8s^k}{(1-s)^2}.
$$



The lower bound uses $A_k\le a^k$, $\theta_k\ge1$, and
$(2k+1)c_k^2\le1$. The upper bound uses $A_k\ge(1-s)a^k$,
$\theta_k\le2$ and $(2k+1)c_k^2\ge1/2$. This also verifies the archive's weaker lower bound
$2e^{-s}s^k$. These are complete reference errors and cannot replace the complete e+π remainder.

## 3. Coefficient budget and complete projection

The coefficients of $(-1)^kp_k(-t)$ are nonnegative. Set $L_k=\|p_k\|_1$;
then $L_0=1$, $L_1=3/2$, and
$L_{k+1}=3L_k/2+\beta_kL_{k-1}$. Hence
$3/2\le L_{k+1}/L_k\le14/9$, in particular $L_k\le2^k$.
The displayed formula for $h_k$ directly gives
$1/|h_k|\le(2k+1)16^k/2$。

For contact order $2n+b$ and degree bounds $(n,b,n)$,
$F(z)=z\mathcal L((1-tz)^{-1})$, and $C^*(t)=t^nC(1/t)$.
Comparing coefficients $n+1$ through $2n+b-1$ gives exactly
$\mathcal L(C^*t^j)=-\ell_B(t^j)$（$0\le j\le n+b-2$）。
Orthogonal expansion gives



$$
C^*=-\sum_{k=0}^n\ell_B(p_k)p_k/h_k,
\quad\ell_B(p_{n+l})=0\ (1\le l\le b-2).
$$



Together with endpoint matching and complete Taylor tails, this yields the archive's CD projection identity and
$R(1)=\ell_B(W_n)$. There is no high-row constraint indexed by $b-1$.
$\ell_j(P/(1-t))=eP(1)-\sum_m[t^m]P\,E_{n+m-j}$
This comes from the entire factorial tail sum, whose starting index is $n+m+1-j$.

Using $|\ell_B(p_k)|\le\|B\|_1 2^k/(n+1-b)!$ and the budgets above,
$\|C\|_2\le c_0\|B\|_2$，
$c_0=(b+1)(n+1)^2 64^n/[2(n+1-b)!]$。
the total absolute coefficient sums of $e$ and $F$ are less than 3 and 10 respectively,
so $\|A\|_2\le(3+10c_0)\|B\|_2$. This verifies the complete three-polynomial norm budget in the contact inverse-matrix manuscript.

Review scope: reference lemmas, complete projection, and norm budgets under the same normalization.
No denominator bound for the actual rational center or vanishing of two independent complete integer forms is proved.
