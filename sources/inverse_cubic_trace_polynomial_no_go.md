> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Inverse-cubic recurrence: a global trace-polynomial no-go

## 1. Statement

Put



$$
n=6m,\qquad A(t)=-2+3t-t^2,\qquad
 \phi(t)=t^3-2t^2+2t,
$$



and let $T_0,T_1,T_2$ be the three local inverse branches of
$\phi(t)=z$ above $z=0$, over an algebraic closure.  Define



$$
F_i(z)=\frac{A(T_i(z))^n}{\phi'(T_i(z))}.
$$



Each $F_i$ satisfies the exact order-three differential equation and the
eight-term coefficient recurrence of the inverse-cubic certificate.  The
branch $T_0(0)=0$ is the branch whose coefficients are the logarithmic
residues under study.

There is nevertheless a nonzero solution of the same recurrence whose
entire tail, beginning at the three target indices, is zero:



$$
\boxed{S_m(z):=F_0(z)+F_1(z)+F_2(z)
        \text{ is a polynomial of degree }4m-1,}
$$



and



$$
\boxed{[z^{4m-1}]S_m(z)=-10m.}
$$



Consequently, for every prime $p>6m$, the reduction of $S_m$ is
nonzero, while



$$
[z^{4m}]S_m=[z^{4m+1}]S_m=[z^{4m+2}]S_m=0
 \pmod p.
$$



Thus the eight-term recurrence, even when all of its rows are used and all
fresh-prime resonances are retained, cannot by itself propagate the target
triple zero to a contradiction at the initial end.  Any successful use of
the inverse-cubic model must add information not shared by the trace
solution, for example a Cartier or local-initial-value condition selecting
the branch $T_0(0)=0$.

## 2. The trace is a polynomial

Let $H_m(t,z)$ be the remainder of $A(t)^{6m}$ on division by
$\phi(t)-z$:



$$
A(t)^{6m}\equiv H_m(t,z)\pmod{\phi(t)-z},
 \qquad \deg_t H_m\le2.
$$



Lagrange interpolation at the three roots $T_i$ gives



$$
H_m(t,z)=\sum_{i=0}^2
 A(T_i)^{6m}
 \frac{\phi(t)-z}{(t-T_i)\phi'(T_i)}.
$$



Because $\phi$ is monic cubic, the coefficient of $t^2$ in
$(\phi(t)-z)/(t-T_i)$ is one.  Therefore



$$
\boxed{S_m(z)=[t^2]H_m(t,z).}                       \tag{2.1}
$$



This proves directly that the trace is a polynomial over $\mathbb Z$.
It also gives a finite exact way to compute it without choosing the three
algebraic branches.

## 3. Exact degree and leading coefficient

For $N\ge0$, change variables on each inverse branch.  The coefficient
sum is



$$
[z^N]S_m(z)=
 \sum_{\phi(a)=0}\operatorname {Res}_{t=a}
 \frac{A(t)^{6m}}{\phi(t)^{N+1}}\,dt.              \tag{3.1}
$$



The global residue theorem turns this into minus the residue at infinity.
If $N\ge4m$, the rational function in (3.1) is
$O(t^{-3})$, so the residue at infinity vanishes.  Hence



$$
[z^N]S_m=0\qquad(N\ge4m).                          \tag{3.2}
$$



At $N=4m-1$, the relevant differential is



$$
\frac{A(t)^{6m}}{\phi(t)^{4m}}\,dt.
$$



At infinity,



$$
A(t)^{6m}=t^{12m}\left(1-\frac{18m}{t}+O(t^{-2})\right),
$$





$$
\phi(t)^{4m}=t^{12m}\left(1-\frac{8m}{t}+O(t^{-2})\right).
$$



Thus



$$
\frac{A(t)^{6m}}{\phi(t)^{4m}}
 =1-\frac{10m}{t}+O(t^{-2}).
$$



Equation (3.1) therefore gives



$$
[z^{4m-1}]S_m=-10m.                               \tag{3.3}
$$



Equations (3.2)--(3.3) prove the asserted degree.  If $p>6m$ is prime,
then $p\ge7$, $p\nmid m$, and $p\nmid10$; consequently $-10m$
is a $p$-unit.

## 4. Where backward propagation loses its pivot

Write the certified recurrence as



$$
\sum_{h=-4}^{3}C_h(k,n)c_{k+h}=0.
$$



Its lower edge is



$$
C_{-4}(k,n)=5(5n-4)(5n-1)
 (3k-2n-10)(3k-2n-9)(3k-2n-8).
$$



Set $n=6m$ and $N=4m$.  If one tries to propagate backward from the
zero tail, the row $k=N+3$ has only the possible term
$C_{-4}(N+3,6m)c_{N-1}$.  But



$$
3(N+3)-2(6m)-9=0,
$$



so



$$
\boxed{C_{-4}(4m+3,6m)=0.}                        \tag{4.1}
$$



This is an exact characteristic-zero boundary resonance, not an accidental
prime divisor.  It is precisely what permits the nonzero polynomial
solution $S_m$ to terminate at degree $N-1$.  Reducing modulo a fresh
prime cannot remove it.

## 5. Scope of the no-go

The result rules out a recurrence-only implication



$$
c_{4m}=c_{4m+1}=c_{4m+2}=0
 \quad\Longrightarrow\quad
 \text{all initial data vanish}.
$$



Indeed, $S_m$ is a counterexample even after the hypothesis is strengthened
to the vanishing of every coefficient from $4m$ onward.  This does not
prove that the distinguished branch $F_0$ can have the target triple zero.
It says exactly that the scalar ODE and all rows of its coefficient
recurrence do not distinguish $F_0$ from the other inverse branches well
enough to prove nonvanishing.  A branch-specific condition remains
essential.

The deterministic companion certificate is
`scripts/inverse_cubic_trace_polynomial_no_go.py`; its byte-stable output is
`results/inverse_cubic_trace_polynomial_no_go.json`.
