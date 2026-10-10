> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 242 — finite phase state of the $j=1$ Witt kernel $E$

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Work on the actual $j=1$ row


$$
p=4h+6s+3=2r+6s+3,\qquad r=2h,\qquad h,s\geq1.               \tag{1.1}
$$


Here $E_\nu$, $\nu=0,1$, is exactly the harmonic-plus-quadratic
Frobenius defect in Item 234.  It is the remaining term in Item 240's
identity


$$
\Omega_\nu^W=-6\epsilon M_\nu^{(1)}
                   +12\epsilon V_\nu^{\sin}+E_\nu             \tag{1.2}
$$


on the original gate $p^2\mid C_\nu$.

**PROVED — exact finite phase realization.**  There is one common
rational kernel


$$
\mathcal H_E(z)={R_E(z)\over V(z)^5},
 \qquad V(z)=1+z^{2p},                                       \tag{1.3}
$$


for both $E_0$ and $E_1$.  If $S_p$ denotes coefficient-index
shift by $p$, then every coefficient channel of
$\mathcal H_EW$ satisfies


$$
(S_p^2+1)^5e=0.                    \tag{1.4}
$$


Equivalently,


$$
\boxed{\;
 e_{t+10p}+5e_{t+8p}+10e_{t+6p}+10e_{t+4p}
            +5e_{t+2p}+e_t=0.\;}                             \tag{1.5}
$$


This gives an exact ten-level companion realization for every fixed
residue channel used by the terminal phase shifts.

**PROVED — the phase order is genuinely minimal for the full
kernel.**  On every actual row,


$$
V\nmid R_EW.                           \tag{1.6}
$$


For each of the two roots of $1+Z^2$, some $p$-section retains the
fifth power of that root factor.  Consequently the least common
multiple of the reduced section denominators is
$(1+Z^2)^5$, $Z=z^p$, and the full section module has minimal
eventual phase polynomial $(X^2+1)^5$, of degree ten.  When
$1+Z^2$ splits, the two fifth powers need not occur in the same
section.

The entire denominator tower of Item 240 remains in the semisimple
three-mode space with phase polynomial
$(X-1)(X^2+1)$.  Thus the kernel $E$ introduces no new phase
eigencharacter, but it does introduce eight genuinely new generalized
$\pm i$ phase directions: the multiplicity of $X^2+1$ rises from
one to five.

**PROVED — common two-coordinate observation map.**  If
$F_E=\mathcal H_EW$ and


$$
e_t=[z^{\,3p-2s-4+t}]F_E,                                   \tag{1.7}
$$


then


$$
\boxed{\begin{aligned}
 E_0&=e_0+e_1+e_2+e_3,\\
 E_1&=e_0+4e_1+6e_2+4e_3+e_4.
\end{aligned}}                                                \tag{1.8}
$$


Thus both Witt coordinates observe one common enlarged kernel state.

**PROVED — sharply scoped universal-linear no-go.**  At
$(p,h,s)=(29,5,1)$, on arbitrary coefficient inputs of degree at
most $12$, the six ordinary/squared endpoint functionals have rank
six.  Adjoining $E_0$ raises the rank to seven, and adjoining $E_1$
raises it to eight.  Hence the two $E$-observations vary independently
while the whole $u/v$ state is held fixed.  The $p^3$ compatibility
therefore fixes two new coordinates of the enlarged state; it does not
collapse to a universal linear scalar condition on $u/v$.

This rank theorem is not an actual-family theorem.  It does not exclude
a nonlinear identity, an identity peculiar to the binomial polynomial
$W$, or a formula singular at $p=29$.

**EXACT FINITE ONLY.**  At $(p,h,s)=(109,10,11)$, the two
$E$-observations remain successively independent after all three
endpoint modes at every denominator power through $K=12$ are
adjoined.  This does not prove an all-power statement.

**OPEN.**  The phase realization does not give a uniform small
adjacent-$t$ Pearson realization, nor does it prove that the actual
binomial family leaves a new terminal scalar after all lifted data are
imposed.  No common-log exclusion or Route-1 rate is claimed.

## 2. The exact rational kernel

Work throughout this section in $\mathbb F_p[[z]]$.  Retain the Item
234 polynomials


$$
\begin{aligned}
 U&=1-z^p,&V&=1+z^{2p},\\
 A_0&=-\sum_{k=1}^{p-1}{z^k\over k},&
 A_1&=\sum_{k=1}^{p-1}{H_{k-1}z^k\over k},\\
 B_0&=\sum_{k=1}^{p-1}{(-1)^{k-1}z^{2k}\over k},&
 B_1&=-\sum_{k=1}^{p-1}{(-1)^{k-1}H_{k-1}z^{2k}\over k}.
                                                               \tag{2.1}
\end{aligned}
$$


Every displayed denominator is a $p$-unit.  Item 234's kernel is


$$
\begin{aligned}
 \mathcal H_E={}&4U^3V^{-3}A_1-3U^4V^{-4}B_1\\
 &+6U^2V^{-3}A_0^2-12U^3V^{-4}A_0B_0
       +6U^4V^{-5}B_0^2.                                     \tag{2.2}
\end{aligned}
$$


Putting the five terms over the common denominator $V^5$ gives


$$
\begin{aligned}
 R_E={}&4U^3V^2A_1-3U^4VB_1+6U^2V^2A_0^2\\
       &-12U^3VA_0B_0+6U^4B_0^2,                              \tag{2.3}\\
 \mathcal H_E={}&R_E/V^5.                                     \tag{2.4}
\end{aligned}
$$


This is an identity of formal series, not a fitted recurrence.  The
degree bound


$$
\deg R_E\leq8p-1                   \tag{2.5}
$$


follows term by term from (2.1)--(2.3).

## 3. Why both coordinates use the same state

Put


$$
W=(1-z)^r(1+z^2)^{2s-1},\qquad F_E=\mathcal H_EW.             \tag{3.1}
$$


The two Item 234 input polynomials and targets are


$$
\begin{array}{c|c|c}
\nu&P_\nu&N_\nu\\ \hline
0&(1+z)(1+z^2)W&3p-2s-1\\
1&(1+z)^4W&3p-2s.
\end{array}                                                    \tag{3.2}
$$


By definition,


$$
E_\nu=[z^{N_\nu}]\mathcal H_EP_\nu.
                                                                  \tag{3.3}
$$


The short multipliers are


$$
\begin{aligned}
 (1+z)(1+z^2)&=1+z+z^2+z^3,\\
 (1+z)^4&=1+4z+6z^2+4z^3+z^4.                               \tag{3.4}
\end{aligned}
$$


With the origin in (1.7), direct coefficient extraction from
(3.2)--(3.4) gives (1.8), including every index and sign.  No
self-reciprocity or finite-row inference is needed for this step.

## 4. Exact phase recurrence and a companion state

Write


$$
F_E(z)={S_E(z)\over(1+z^{2p})^5},
       \qquad S_E=R_EW.                                      \tag{4.1}
$$


The degree of $W$ is


$$
\delta=r+4s-2,\qquad p-\delta=r+2s+5>0,                      \tag{4.2}
$$


so (2.5) gives


$$
\deg S_E<9p.                       \tag{4.3}
$$


Let $f_n=[z^n]F_E$, with $f_n=0$ for $n<0$.  Multiplication by


$$
(1+z^{2p})^5
 =1+5z^{2p}+10z^{4p}+10z^{6p}+5z^{8p}+z^{10p}                \tag{4.4}
$$


and extraction at degree $n+10p$ give


$$
\begin{aligned}
 f_{n+10p}+5f_{n+8p}+10f_{n+6p}
 +10f_{n+4p}+5f_{n+2p}+f_n
 =[z^{n+10p}]S_E.                                             \tag{4.5}
\end{aligned}
$$


For every $n\geq0$, the right side is zero by (4.3).  This proves
(1.5) for all relevant initial and terminal offsets.

For a fixed residue $a\bmod p$, define


$$
\mathbf s_a(m)=
 (f_{a+mp},f_{a+(m+1)p},\ldots,f_{a+(m+9)p})^t.               \tag{4.6}
$$


Advancing $m$ shifts the first nine entries, while (1.5) supplies
the tenth.  Thus (4.6) is an explicit ten-level companion realization.
The terminal phases


$$
t_b=2s+1+(b-2)p                       \tag{4.7}
$$


advance the same residue channel one companion step at a time.

For several consecutive output residues one uses parallel copies of
(4.6).  Equation (1.5) controls the phase direction exactly; it does
not by itself relate different residues modulo $p$.  This is why the
construction is a phase realization, not yet a uniform adjacent-$t$
Pearson closure.

## 5. Proof that the generalized phase modes are unavoidable

In $\mathbb F_p[z]$,


$$
U=(1-z)^p,\qquad V=(1+z^2)^p.                               \tag{5.1}
$$


Also


$$
B_0(z)=A_0(-z^2).                     \tag{5.2}
$$


Now $A_0(1)=-H_{p-1}=0$, whereas


$$
A_0'(1)=-\sum_{k=1}^{p-1}1=1\pmod p.       \tag{5.3}
$$


Thus $A_0$ has a simple zero at $1$.  Over an algebraic closure,
if $\iota^2=-1$, then


$$
B_0'(\pm\iota)=-2(\pm\iota)A_0'(1)\ne0.                     \tag{5.3a}
$$


Hence $B_0$ has a simple zero at each of $z=\iota,-\iota$,
not merely one factor $1+z^2$ in aggregate.

Reducing (2.3) modulo $V$ leaves only the last term:


$$
R_E\equiv6U^4B_0^2\pmod V.             \tag{5.4}
$$


The factor $U$ is nonzero at both roots of $1+z^2$.  Hence $R_E$
has order exactly two at each root.  Multiplication by $W$ raises
the order at each root to


$$
2+(2s-1)=2s+1<p.                    \tag{5.5}
$$


Since $V=(1+z^2)^p$, equations (5.4)--(5.5) prove more precisely
that both root orders of $S_E$ are $2s+1<p$.

Use the unique $p$-section decomposition


$$
S_E(z)=\sum_{a=0}^{p-1}z^aS_a(Z),
 \qquad Z=z^p.                                                \tag{5.6}
$$


Fix a root $\iota^2=-1$ in an algebraic closure.  If every
$S_a(Z)$ vanished at the corresponding root
$\iota^p$, then every term in (5.6) would be divisible by


$$
Z-\iota^p=z^p-\iota^p=(z-\iota)^p,
$$


forcing $\operatorname{ord}_{z=\iota}S_E\geq p$, contrary to
(5.5).  Thus, for each sign separately, some section retains the fifth
power of the corresponding linear denominator.  The least common
multiple of all reduced section denominators is therefore
$(1+Z^2)^5$.  When $1+Z^2$ splits over $\mathbb F_p$, the two
root factors may be witnessed by different sections; no single
coprime section is asserted.  The full section module consequently has
minimal eventual recurrence polynomial $(X^2+1)^5$.

For the Item 240 denominator tower, shifting by $p$ fixes $q_0$ and
rotates the pair $(q_c,q_{\sin})$.  Its phase polynomial divides


$$
(X-1)(X^2+1),                        \tag{5.7}
$$


which is square-free for odd $p$.  Comparing (5.7) with
$(X^2+1)^5$ proves that $E$ contributes four additional Jordan
levels for each of the two conjugate $\pm i$ directions, eight
generalized directions in total.

## 6. What the $p^3$ gate does in the enlarged state

The hypotheses must remain separated:

1. The original per-coordinate gate is $p^2\mid C_\nu$.  It makes
   $M_\nu^{(1)}=M_\nu/p\pmod p$ integral and gives (1.2).
2. The extra integer multiplicity is $p^3\mid C_\nu$, equivalently
   $\Omega_\nu^W=0$.
3. Combining (1.2) with (1.8), the extra gate fixes
   

$$
E_\nu=6\epsilon M_\nu^{(1)}
                  -12\epsilon V_\nu^{\sin}\pmod p.            \tag{6.1}
$$



Thus the two extra-digit equations are two observations of the new
kernel state.  A phase recurrence alone does not turn them into a
constraint on the old $u/v$ state, because it needs independent
initial data for the generalized phase directions.

There is an exact finite-dimensional witness to this limitation.  At
$(p,h,s)=(29,5,1)$, let


$$
\mathcal P_{12}=\left\{\sum_{d=0}^{12}c_dz^d:
                    c_d\in\mathbb F_{29}\right\},             \tag{6.2}
$$


and put $D_d=p+r+d+1=40+d$.  For
$q\in\{q_0,q_c,q_{\sin}\}$ and $k=1,2$, define


$$
T_{q,k}(c)=\sum_{d=0}^{12}
                         {c_dq(D_d)\over D_d^k}.               \tag{6.3}
$$


Define $E_0(c),E_1(c)$ by the direct coefficient extractions
(3.2)--(3.4), with the same kernel $\mathcal H_E$.

In the column order


$$
T_{q_0,1},T_{q_c,1},T_{q_{\sin},1},
 T_{q_0,2},T_{q_c,2},T_{q_{\sin},2},E_0,E_1,                  \tag{6.4}
$$


exact elimination over $\mathbb F_{29}$ gives


$$
6,\qquad7,\qquad8                   \tag{6.5}
$$


for the ranks before $E_0$, after $E_0$, and after $E_1$.
The explicit $13\times8$ matrix has row-major SHA-256


$$
\texttt{39e13655ffdd3d1b2a0c44f572eae0a4084ab2f3f3364242e7fe42e30f782b20}.
                                                                  \tag{6.6}
$$


The certificate includes every entry, every row hash, and nonzero
maximal minors with determinants $1,5,9$, respectively.

The rank jump by two has a precise consequence:


$$
\ker(T_{q,k})\longrightarrow\mathbb F_{29}^2,
      \qquad c\longmapsto(E_0(c),E_1(c))                       \tag{6.7}
$$


is onto.  Both $E$-values can therefore change arbitrarily while all
six $u/v$ functionals stay fixed.  In this universal linear model,
(6.1) fixes two new coordinates rather than yielding an old-state
scalar obstruction.

Equation (6.7) is not extrapolated to the single binomial input $W$.
Whether the actual family and the divided lift coordinates
$M_\nu^{(1)}$ create a further relation remains open.

## 7. Replay and finite evidence

The standard-library checker
work/item242_j1_E_kernel_state_certificate.py verifies by default:

- the rational-kernel coefficients against the independent Item 240
  implementation on all 368 coordinates in the 184 actual rows through
  $p\leq151$;
- the two observation identities (1.8) against frozen Item 234 on the
  same 368 coordinates;
- 1,104 direct instances of the phase recurrence, including initial
  and terminal offsets;
- exact factor multiplicities on all 184 rows and the structural
  reduction (5.4) for all 31 distinct primes;
- the explicit rank-$6/7/8$ witness in (6.5).

At $(p,h,s)=(109,10,11)$, adjoining the three endpoint modes through
denominator power $K$ gives


$$
\begin{array}{c|rrrrrrrrrrrr}
K&1&2&3&4&5&6&7&8&9&10&11&12\\ \hline
\text{tower}&3&6&9&12&15&18&21&24&27&30&33&36\\
\text{with }E_0&4&7&10&13&16&19&22&25&28&31&34&37\\
\text{with }E_0,E_1&5&8&11&14&17&20&23&26&29&32&35&38.
\end{array}                                                     \tag{7.1}
$$


Every value in (7.1) is **EXACT FINITE ONLY**.  It is evidence against
a low denominator-power elimination, not an all-power theorem.

## 8. Final ledger

### PROVED

- The exact rational form (2.3)--(2.4) of the universal Item 234
  $E$-kernel.
- The common observation identities (1.8).
- The all-row phase recurrence (1.5) and ten-level companion
  realization.
- Minimal phase polynomial $(X^2+1)^5$ for the full kernel module on
  every actual row.
- Eight genuinely new generalized $\pm i$ phase directions beyond
  the denominator tower.
- The scoped universal-linear rank-$6/7/8$ no-go at $p=29$.

### EXACT FINITE ONLY

- Every direct-replay count, matrix entry, minor, digest, and bounded
  power rank in the certificate.
- The $K\leq12$ evidence (7.1).

### OPEN

- A uniform small adjacent-$t$ Pearson realization of the new kernel
  state.
- An actual-binomial-family or nonlinear elimination of $E_0,E_1$.
- Whether (6.1), after all lift data are imposed, creates an all-row
  terminal scalar obstruction.
- Any all-prime common-log exclusion, density theorem, Route-1
  exponent, or conclusion about $e+\pi$.

The quantity denoted $E_h^*$ in Item 237 is Item 222's rational-tail
eliminant, not the Witt kernel $E_\nu$ studied here.  No relation
between those differently defined objects is asserted.
