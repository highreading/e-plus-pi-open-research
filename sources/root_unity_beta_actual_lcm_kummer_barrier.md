> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual beta-ratio denominator lcm is large, but Kummer periodicity cannot concentrate it

## A square-root block theorem and a first-period Euler-drop obstruction

Checked: 2026-08-27 UTC

## 1. Statement and scope

Let



$$
U_n=|E_{2n}|,\qquad A_n=(2n+1)(2n+2),
$$



and write the reduced adjacent Euler ratio as



$$
r_n=\frac{U_{n+1}}{A_nU_n}=\frac{P_n}{Q_n},
 \qquad
 Q_n=\frac{A_nU_n}{\gcd(A_nU_n,U_{n+1})}.                 \tag{1}
$$



For $N\geq1$ and $h\geq2$, define the actual block lcm



$$
\mathcal Q_{N,h}
                 =\operatorname {lcm}
                   (Q_N,Q_{N+1},\ldots,Q_{N+h-1}).         \tag{2}
$$



The universal product clearing used in the preceding higher-determinant
audit can be sharpened to this actual lcm.  The first theorem is



$$
\boxed{
 \mathcal Q_{N,h}\geq
 \frac{(2h-1)^{2N}}
 {\alpha\left((2h-1)^{-1}+(2N)^{-1}\right)}
 \qquad(N\geq N_0(h)),}                                   \tag{3}
$$



where $\alpha=4/\pi^2$ and the explicit $N_0(h)=O(h^2)$ is recalled
in Section 3.

In particular, for all sufficiently large $N$, with



$$
h_N=\left\lfloor\sqrt{\frac{N-2}{2}}\right\rfloor,
                                                                    \tag{4}
$$



one has



$$
\boxed{\log\mathcal Q_{N,h_N}
                        \geq N\log N-O(N).}                \tag{5}
$$



Thus the optimal beta filter really does force an $N\log N$-scale
**block lcm** on a square-root-length interval.

This still does not imply an individual $N\log N$ bound for any
$Q_n$.  The rest of the note proves a precise obstruction.  Remove the
elementary index factor $A_n$ and define



$$
B_n=\frac{U_n}{\gcd(U_n,U_{n+1})},\qquad
 \mathcal B_{N,h}=\operatorname {lcm}(B_N,\ldots,B_{N+h-1}). \tag{6}
$$



Then $\mathcal B_{N,h}$ and $\mathcal Q_{N,h}$ differ by at most the
lcm of the $A_n$'s.  On the square-root block,



$$
\log\mathcal B_{N,h_N}
                    \geq N\log N-O(N).                     \tag{7}
$$



Split $\mathcal B_{N,h_N}$ at the Kummer-period boundary
$\varphi(p^a)\leq2(N+h_N)$.  Its Kummer-visible part has logarithm
$O(N)$, while the complementary first-period factor
$\mathcal J_{N,h_N}$ satisfies



$$
\boxed{\log\mathcal J_{N,h_N}
                    \geq N\log N-O(N).}                    \tag{8}
$$



Every prime-power layer counted by $\mathcal J_{N,h_N}$ is an
asymmetric adjacent Euler valuation drop whose Kummer period is longer
than the entire block.  Consequently, the standard Kummer congruence
relates it to no second index in the block.  Canonical periodicity can
account for only the $O(N)$ visible part and is silent on the
$N\log N$ mass in (8).

This is a rigorous Kummer-periodicity/lcm obstruction, not a proof that
no stronger arithmetic theorem exists.  A new concentration or overlap
theorem for the first-period layers could still convert (5) into an
individual bound.  No such theorem is proved here.  Nothing in this note
classifies $e+\pi$.

## 2. Exact p-adic formulas and the lcm sandwich

For a prime $p$, write



$$
e_{p,n}=v_p(U_n),\qquad a_{p,n}=v_p(A_n),\qquad
 q_{p,n}=v_p(Q_n).
$$



Equation (1) gives the exact formula



$$
\boxed{
 q_{p,n}
 =\bigl(a_{p,n}+e_{p,n}-e_{p,n+1}\bigr)_+.}                \tag{9}
$$



On the other hand,



$$
v_p(B_n)=(e_{p,n}-e_{p,n+1})_+.         \tag{10}
$$



For $a\geq0$ and real $x$,



$$
x_+\leq(a+x)_+\leq a+x_+.
$$



Applied to (9)--(10), this proves the exact divisibility sandwich



$$
\boxed{B_n\mid Q_n\mid A_nB_n.}   \tag{11}
$$



Put



$$
\mathcal A_{N,h}=\operatorname {lcm}(A_N,\ldots,A_{N+h-1}).
$$



Taking lcms in (11) gives



$$
\boxed{
 \mathcal B_{N,h}\mid\mathcal Q_{N,h}
 \mid\mathcal A_{N,h}\mathcal B_{N,h}.}                    \tag{12}
$$



Let $M=N+h$ and
$\Lambda(x)=\operatorname {lcm}(1,2,\ldots,\lfloor x\rfloor)$.
Every factor $2n+1,2n+2$ occurring in the block is at most $2M$.
Therefore



$$
\mathcal A_{N,h}\mid\Lambda(2M)^2,
 \qquad
 \mathcal A_{N,h}\mid\prod_{n=N}^{N+h-1}A_n.               \tag{13}
$$



Consequently,



$$
\boxed{
 \log\mathcal A_{N,h}
 \leq
 \min\left(2\psi(2M),\,2h\log(2M)\right),}                 \tag{14}
$$



where $\psi(x)=\log\Lambda(x)=O(x)$.  In particular, the index-factor
cost is $o(N)$ on a square-root block, using the second bound in (14).

## 3. The optimal filter clears with the actual lcm

For $h\geq2$, set $q_h=2h-1$ and



$$
F_h(X)=(X-1)\prod_{j=1}^{h-2}((2j+1)^2X-1)
       =\sum_{\ell=0}^{h-1}f_{h,\ell}X^\ell.               \tag{15}
$$



The preceding higher-determinant theorem proves that



$$
\mathscr F_{N,h}
 :=\sum_{\ell=0}^{h-1}f_{h,\ell}r_{N+\ell}                 \tag{16}
$$



is nonzero for



$$
N\geq N_0(h)
 =1+\left\lceil\frac{q_h+2}{4}
 \left(
 3\log q_h+(h-2)\log\frac{5\mathrm e}{2}+\log\frac98
 \right)\right\rceil,                                     \tag{17}
$$



and satisfies



$$
|\mathscr F_{N,h}|
 \leq\alpha q_h^{-2N}
       \left(q_h^{-1}+(2N)^{-1}\right).                    \tag{18}
$$



Since $Q_{N+\ell}\mid\mathcal Q_{N,h}$,



$$
\mathcal Q_{N,h}\mathscr F_{N,h}
                   \in\mathbb Z.                           \tag{19}
$$



For $N\geq N_0(h)$, this integer is nonzero.  Equations (18)--(19)
prove (3).

For later use, there is a simple uniform bound on the certified range:



$$
\boxed{N_0(h)\leq2h^2+2.}          \tag{20}
$$



Indeed,


$$
3\log(2h-1)+(h-2)\log(5\mathrm e/2)+\log(9/8)\leq3h.
$$


One may use $\log(5\mathrm e/2)<2$,
$\log(9/8)<1$, and
$3\log(2h)\leq h+3$ for $h\geq2$.  Substitution in (17), followed by
$\lceil x\rceil\leq x+1$, gives (20).

For $h=h_N$ in (4), once $N$ is large enough that $h_N\geq2$,
one has $2h^2+2\leq N$, so the filter is certifiably nonzero.
Moreover, as $N\to\infty$,



$$
h_N=\sqrt{N/2}+O(1),\qquad
 2N\log(2h_N-1)=N\log N+O(N).                              \tag{21}
$$



Taking logarithms in (3) proves (5).

## 4. Removing the elementary index contribution

Combining (5), (12), and (14), with $h=h_N$, gives



$$
\begin{aligned}
 \log\mathcal B_{N,h_N}
 &\geq\log\mathcal Q_{N,h_N}
       -\log\mathcal A_{N,h_N}\\
 &\geq N\log N-O(N),
 \end{aligned}                                             \tag{22}
$$



which proves (7).  In fact, the short-block estimate in (14) is only
$O(\sqrt N\log N)=o(N)$; the displayed $O(N)$ allows for the harmless
constant-scale losses in (3) and (21).

The arithmetic content forced by the filter is therefore not supplied by
the neighboring integer factors $2n+1,2n+2$.  It is already present in
the lcm of the genuine Euler valuation drops (10).

## 5. The Kummer-visible and first-period parts

Continue to write $M=N+h$.  For an odd prime $p$, define



$$
\kappa_p(M)=
 \max\{a\geq1:\ \varphi(p^a)\leq2M\},                      \tag{23}
$$



with $\kappa_p(M)=0$ if the set is empty.  Put



$$
b_p=v_p(\mathcal B_{N,h}).
$$



Only odd primes occur here.  Indeed, the secant recurrence
$E_{2n}=-\sum_{k<n}\binom{2n}{2k}E_{2k}$, together with
$\sum_{k<n}\binom{2n}{2k}=2^{2n-1}-1$, proves inductively that every
$U_n$ is odd.  Split



$$
\mathcal B^{\rm vis}_{N,h}
 =\prod_{p\ {\rm odd}}p^{\min(b_p,\kappa_p(M))},
 \qquad
 \mathcal J_{N,h}
 =\frac{\mathcal B_{N,h}}{\mathcal B^{\rm vis}_{N,h}}.     \tag{24}
$$



The block factor $\mathcal J_{N,h}$ is distinct from the single-index
simultaneous-gcd excess $J_N$ in the earlier quadratic Kummer audit:
the present object records one-sided valuation drops across a block,
whereas the earlier object records common adjacent Euler divisibility at
one index.

This is a conservative split.  The $r$-th layer of a valuation drop is
witnessed at the absolute threshold $e_{p,n+1}+r$, not necessarily at
$r$ itself.  Hence $\mathcal B^{\rm vis}$ is an upper envelope for
the part that could be reached inside a Kummer period; it may retain some
layers that are already first-period.  What matters below is that every
layer discarded into $\mathcal J$ is certainly first-period.

If $\varphi(p^a)\leq2M$, then



$$
p^a=\frac p{p-1}\varphi(p^a)\leq3M.
$$



Therefore



$$
\boxed{
 \mathcal B^{\rm vis}_{N,h}\mid\Lambda(3M),
 \qquad
 \log\mathcal B^{\rm vis}_{N,h}=O(M).}                    \tag{25}
$$



Equations (22) and (25), with $h=h_N$ and $M=N+O(\sqrt N)$, prove
(8).

The factor $\mathcal J_{N,h}$ has an exact valuation-drop
interpretation.  Suppose



$$
b_p>\kappa_p(M).
$$



Choose $n\in[N,N+h-1]$ at which



$$
b_p=e_{p,n}-e_{p,n+1}>0,
$$



and put $v=e_{p,n+1}$.  For every



$$
r=\kappa_p(M)+1,\ldots,b_p,
$$



the exponent $t=v+r$ satisfies



$$
\boxed{
 \varphi(p^t)>2M,\qquad
 p^t\mid U_n,\qquad p^t\nmid U_{n+1}.}                    \tag{26}
$$



Thus every logarithmic layer in $\mathcal J_{N,h}$ is witnessed by a
strict adjacent Euler valuation drop at a prime-power threshold whose
first Kummer period exceeds all indices in the block.

The prime-power Euler congruence used in the frozen Kummer audit says
that divisibility by $p^t$ is periodic in the positive even index with
period $\varphi(p^t)$, equivalently in $n$ with period
$\varphi(p^t)/2$.  For the layers in (26),



$$
\frac{\varphi(p^t)}2>M.            \tag{27}
$$



No two distinct indices $1\leq n_1,n_2\leq M$ are congruent modulo
this period.  Hence the Kummer equivalence supplies no second divisibility
statement inside the block.  This proves the claimed periodicity
obstruction.

## 6. Common content and the missing concentration lemma

The difference between universal product clearing and actual lcm
clearing is the integer



$$
\mathcal C_{N,h}
 =\frac{\prod_{n=N}^{N+h-1}Q_n}{\mathcal Q_{N,h}}.          \tag{28}
$$



Its exact valuation is



$$
v_p(\mathcal C_{N,h})
 =\sum_{n=N}^{N+h-1}q_{p,n}
  -\max_{N\leq n<N+h}q_{p,n}.                              \tag{29}
$$



Repeated periodic layers can make $\mathcal C_{N,h}$ large.  Equation
(25) bounds only their **distinct lcm contribution**, not their repeated
multiplicity in (29).  The $N\log N$ *distinct* lcm mass forced by (8),
however, lies in layers for which periodicity gives no second related
index within the block.  Thus canonical periodicity controls neither how
those first-period layers are distributed among the $h$ denominators nor
how much of their mass is concentrated in one denominator.

The elementary inequality



$$
\mathcal Q_{N,h}\leq\prod_{n=N}^{N+h-1}Q_n
 \leq\left(\max_{N\leq n<N+h}Q_n\right)^h                 \tag{30}
$$



turns (5) only into



$$
\max_{N\leq n<N+h_N}\log Q_n
 \geq \frac{N\log N-O(N)}{h_N}
 =\Omega(\sqrt N\log N).                                  \tag{31}
$$



This is weaker than the already known individual $\Omega(N)$ bound.
More generally, combining (3) with (30) gives only



$$
\max_{N\leq n<N+h}\log Q_n
 \geq \frac{2N\log(2h-1)}h
 -\frac1h\log\!\left[
   \alpha\left((2h-1)^{-1}+(2N)^{-1}\right)\right].       \tag{31a}
$$



The elementary inequality



$$
(2h-1)^2\leq3^h                 \tag{31b}
$$



has equality only at $h=2$.  Hence the main exponential rate on the
right of (31a) is at most $N\log3$; for $2\leq h\leq N$, its remaining
term is only $O(\log N)$.  Thus, even after replacing product clearing
by the exact lcm, the $N$-linear main rate furnished by the
**unstructured** conversion $\mathcal Q\leq(\max Q_n)^h$ is rigorously
optimized by the original two-term filter and cannot yield an individual
$N\log N$ bound.

For completeness, (31b) starts with $3^2=3^2$ at $h=2$ and
$5^2<3^3$ at $h=3$; thereafter
$((2h+1)/(2h-1))^2<3$, so induction is strict.

To obtain an individual $N\log N$ estimate from (5), one would need a
new concentration inequality such as



$$
\log\mathcal Q_{N,h_N}
 \leq\max_{N\leq n<N+h_N}\log Q_n+O(N),                   \tag{32}
$$



or another theorem showing that only $O(1)$ denominators carry the
first-period factor in (8).  Equations (26)--(27) explain exactly why
canonical Kummer periodicity cannot prove such a statement.

This does not rule out a different p-adic $L$-function, resultant, or
Euler-irregularity theorem.  It isolates the missing arithmetic input:
**concentration or overlap of adjacent first-period Euler valuation
drops**, not further manipulation of the beta tail.

## 7. Deterministic replay

The companion certificate checks on declared exact grids:

* the valuation formulas (9)--(10) and divisibilities (11)--(12);
* the two bounds in (13)--(14);
* actual lcm clearing of the optimal filter and the lower bound (3);
* the bound $N_0(h)\leq2h^2+2$;
* square-root block instances of (5);
* the visible/excess split and first-period witnesses (24)--(27); and
* the common-content identity (29).

The finite replay is not the proof of the all-parameter statements.  Run

    python3 scripts/root_unity_beta_actual_lcm_kummer_certificate.py
    sha256sum -c results/root_unity_beta_actual_lcm_kummer_hashes.sha256

from the research directory.

No claim in this package classifies $e+\pi$.
