> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The cyclic Euler square root has no bounded-window eliminant

## 1. Result and quantitative role

Let $p$ be an odd prime and put $r=(p-1)/2$.  The exact
finite-field moment theorem gives



$$
C_p(X)=-2E_{2r}-2\sum_{k=1}^{r-1}E_{2k}X^k,\qquad
 C_p(X)^2\equiv4\pmod {X^r-1}.                              \tag{1}
$$



Define



$$
A_p(X)=-\frac12C_p(X)
       =\sum_{k=0}^{r-1}a_kX^k,\qquad
 a_0=E_{2r},\quad a_k=E_{2k}\ (1\leq k<r).                 \tag{2}
$$



Then $A_p^2=1$ in $\mathbb F_p[X]/(X^r-1)$.  This note
derives every cyclic quadratic equation explicitly and proves a
structural obstruction: once $r$ exceeds an explicit linear threshold,
any bounded interval of those equations admits an explicit polynomial
section over every ring in which $2$ is a unit.  Consequently, such a
window adds no eliminant in the prescribed low coefficients, even after
the adjacent conditions



$$
a_N=a_{N+1}=0                      \tag{3}
$$



are imposed.

The result aligns exactly with the desired product scale.  For any fixed
linear-size coefficient and equation windows, primes below the threshold
where the section applies have total logarithmic mass $O(N)$ by the
elementary Chebyshev bound.  Above that threshold, the bounded-window
quadratic equations add no algebraic condition at all.  Thus this
formal bounded-window elimination route alone cannot prove the missing
$o(N\log N)$ first-period product estimate.

This is a theorem about bounded windows of the cyclic convolution
system.  It does not treat an eliminant using all $r$ equations,
nonlocal equations selected in a $p$-dependent pattern, or additional
arithmetic information about the actual sign assignment.  It proves no
bound for $J_N$ and does not classify $e+\pi$.

## 2. The complete cyclic convolution equations

For $t\in\mathbb Z/r\mathbb Z$, let



$$
F_t(\boldsymbol a)
   =\sum_{i=0}^{r-1}a_i a_{\langle t-i\rangle_r},            \tag{4}
$$



where $\langle\cdot\rangle_r$ is the representative in
$\{0,\ldots,r-1\}$.  Comparing coefficients in $A_p^2=1$ gives



$$
\boxed{\qquad
 F_t(\boldsymbol a)=
 \begin{cases}
 1,&t=0,\\
 0,&t\ne0.
 \end{cases}
 \qquad}                                                     \tag{5}
$$



In ordinary, noncyclic indices this is



$$
\sum_{i=0}^{t}a_i a_{t-i}
 +\sum_{i=t+1}^{r-1}a_i a_{r+t-i}
 =\delta_{t,0},
 \qquad0\leq t<r.                                           \tag{6}
$$



The second sum is the obstruction to treating (6) as a recurrence in
the low coefficients.  Every low equation contains a long wraparound
correlation among coefficients near the far end of the Euler--Kummer
period.

Extend the $a_k$ periodically, with the zero residue represented by
the positive half-index $r$, not by the Euler index $0$.  The
Euler--Kummer/moment period then gives only



$$
a_{k+r}=a_k.                        \tag{7}
$$



This convention does not assert $E_{p-1}\equiv E_0$.  The positive
endpoint is essential.  Periodicity also does not turn the far coefficient
$a_{r-k}=E_{p-1-2k}$ into $a_k=E_{2k}$.  Indeed, their Euler
indices are congruent modulo $p-1=2r$ precisely when



$$
2(r-k)\equiv2k\pmod {2r}
                  \quad\Longleftrightarrow\quad r\mid2k.    \tag{8}
$$



For $1\leq k<r$, this never happens when $r$ is odd and happens only
at $k=r/2$ when $r$ is even.  Thus Kummer periodicity is already
fully represented by the cyclic indexing in (4); it supplies no general
reflection symmetry with which to replace the wraparound variables by
low Euler data.

## 3. An anchor criterion for a polynomial section

The following theorem is purely algebraic.  It identifies exactly why a
bounded collection of equations from (5) cannot eliminate the unseen
coefficients.

Let $S,T$ be subsets of $\mathbb Z/r\mathbb Z$.  The coefficients
$a_s$, $s\in S$, are to be prescribed, and the convolution values
$F_t$, $t\in T$, are to be prescribed.  All sumsets below are cyclic.

**Theorem 3.1 (anchor section).**  Suppose there is a residue $u$ such
that



$$
\begin{aligned}
 &u\notin S,\qquad (T-u)\cap S=\varnothing,\\
 &(u+S)\cap T=\varnothing,\qquad
      (T-u+S)\cap T=\varnothing,\\
 &2u\notin T,\qquad
      (T+T-2u)\cap T=\varnothing.                            \tag{9}
\end{aligned}
$$



Then, over every commutative ring $R$ in which $2$ is invertible,
for every choice



$$
a_s=b_s\ (s\in S),\qquad F_t=c_t\ (t\in T),    \tag{10}
$$



there is an explicit completion of the other $a_i$ satisfying (10).
The completion is polynomial in the $b_s,c_t$.

**Proof.**  For each $t\in T$, put



$$
v_t=t-u.                           \tag{11}
$$



The first and third lines of (9) make the residues



$$
S,\quad\{u\},\quad\{v_t:t\in T\}           \tag{12}
$$



pairwise disjoint.  Define the contribution from prescribed
coefficients alone by



$$
B_t(\boldsymbol b)
   =\sum_{\substack{s,s'\in S\\s+s'=t}}b_sb_{s'}.            \tag{13}
$$



Set



$$
\begin{aligned}
 a_s&=b_s &&(s\in S),\\
 a_u&=1,\\
 a_{v_t}&=\frac {c_t-B_t(\boldsymbol b)}2 &&(t\in T),\\
 a_i&=0 &&\text{at every remaining residue}.                \tag{14}
\end{aligned}
$$



The first line of (9) prevents a selected coefficient from colliding
with a prescribed coefficient.  The second line prevents a
prescribed--selected product from contributing to any $F_t$ with
$t\in T$.  The last line prevents $a_u^2$ and every
$a_{v_t}a_{v_{t'}}$ from contributing to that window.  The only
selected--selected products which remain in $F_t$ are the two ordered
products



$$
a_ua_{v_t}+a_{v_t}a_u
                =c_t-B_t(\boldsymbol b).                    \tag{15}
$$



Together with (13), this gives $F_t=c_t$ for every $t\in T$.
Every expression in (14) is polynomial over $\mathbb Z[1/2]$.
$\square$

There is an exact elimination consequence.  Work first over



$$
{\cal R}=\mathbb Z[1/2][\,b_s\ (s\in S),c_t\ (t\in T)\,],
$$



substitute $a_s=b_s$, and let ${\cal I}_T$ be the ideal generated
by $F_t-c_t$, $t\in T$, in the polynomial ring containing the other
$a_i$.  Formula (14) defines a retraction which is the identity on
${\cal R}$.  Hence



$$
{\cal I}_T\cap{\cal R}=0.           \tag{16}
$$



More generally, after imposing any pre-existing ideal
${\cal J}\subset{\cal R}$ of low-data relations,



$$
({\cal I}_T+{\cal J})\cap{\cal R}
                              ={\cal J}.                     \tag{17}
$$



This remains true when ${\cal J}$ contains $b_N,b_{N+1}$, the two
adjacent-zero conditions.  Therefore the bounded convolution window
adds no polynomial relation beyond the relations already imposed on
the low data.  In particular it cannot, by formal elimination alone,
produce a new nonzero integer divisor independent of the original two
Euler divisibilities.

## 4. Explicit interval sections

The anchor criterion has a particularly sharp form for the initial
windows relevant to low Euler data.

**Corollary 4.1 (initial windows).**  Suppose



$$
S\subseteq\{0,\ldots,L\},\qquad
 T\subseteq\{0,\ldots,K\},\qquad
                         r>2L+3K+2.                         \tag{18}
$$



Then Theorem 3.1 applies with



$$
u=L+K+1.                           \tag{19}
$$



To verify this, use ordinary representatives.  The selected partners
lie in the far interval



$$
v_t=r+t-u\in[r-u,r-u+K].                            \tag{20}
$$



The prescribed--anchor sums lie above $K$, the
prescribed--partner sums remain in a far interval ending at $r-1$,
and



$$
v_t+v_{t'}\pmod r
       \in[r-2u,r-2u+2K]\subseteq\{K+1,\ldots,r-1\}.         \tag{21}
$$



The inequalities in (18) also put $2u$ strictly between $K$ and
$r$.  These statements are exactly the six conditions in (9).

The same phenomenon is not tied to a window beginning at zero.

**Corollary 4.2 (arbitrary cyclic intervals).**  Let $S,T$ be cyclic
intervals of cardinalities at most $L+1,K+1$, respectively.  If



$$
r>3L+11K+7,                        \tag{22}
$$



then an anchor satisfying (9) exists.

Indeed, an anchor can fail only in the union



$$
\begin{split}
 S\ \cup\ (T-S)\ \cup\ (T+S-T)\
 \cup\{u:2u\in T\}\
 \cup\{u:2u\in T+T-T\}.                                    \tag{23}
\end{split}
$$



The first three cyclic intervals have cardinalities at most
$L+1,L+K+1,L+2K+1$.  The doubling map has fibers of size at most two,
so the last two sets have cardinalities at most $2K+2$ and $6K+2$.
Their total is at most $3L+11K+7<r$, leaving an admissible $u$.

The constants are not claimed optimal.  What matters is that the
threshold is linear, not quadratic, in the two window lengths.

## 5. Why the near primes are already harmless

Take the full low prefix and the equally long initial equation window



$$
L=K=N+1.                           \tag{24}
$$



Corollary 4.1 applies whenever



$$
r>5N+7,\qquad\text{equivalently}\qquad p>10N+15.           \tag{25}
$$



For every such prime, the equations



$$
F_0=1,\quad F_1=\cdots=F_{N+1}=0       \tag{26}
$$



admit a polynomial section for arbitrary prescribed
$a_0,\ldots,a_{N+1}$, including $a_N=a_{N+1}=0$.

On the other hand, all primes in the complementary interval



$$
2N+2<p\leq10N+15                   \tag{27}
$$



have total logarithmic mass at most



$$
\sum_{p\leq10N+15}\log p=O(N)                             \tag{28}
$$



by Chebyshev's estimate.  Thus (27) is already negligible relative to
$N\log N$, without using Euler divisibility at all.

More generally, if $L\leq\alpha N+O(1)$ and
$K\leq\beta N+O(1)$ for fixed constants $\alpha,\beta$, then the
initial-window section applies above a fixed multiple of $N$, while
the product of all smaller primes is still $\exp(O(N))$.  Hence a
fixed-linear-size low convolution window is algebraically nonrestrictive
on precisely the far-prime range where a new product estimate is needed.

## 6. Exact seed completion

For the actual adjacent seed



$$
N=1643,\qquad p=151483,\qquad r=75741,         \tag{29}
$$



take



$$
L=K=1644,\qquad u=3289.                                   \tag{30}
$$



The selected partners are the $1645$ distinct residues



$$
72452,\ldots,74096.                 \tag{31}
$$



Use the actual low Euler residues



$$
a_0=E_{p-1}=2,\qquad a_k=E_{2k}\pmod p
                  \quad(1\leq k\leq1644),                  \tag{32}
$$



for which $a_{1643}=a_{1644}=0$.  Formula (14), with
$c_0=1$ and $c_t=0$ for $1\leq t\leq1644$, produces a sparse
synthetic completion satisfying all $1645$ equations in (26).

The deterministic replay verifies every one of those equations by
direct cyclic convolution.  The next coefficient is



$$
F_{1645}=131736\ne0\pmod {151483}.   \tag{33}
$$



Thus the synthetic vector is intentionally only a section of the stated
window, not a global square root.  This finite seed is a transparent
instance of the all-parameter section theorem; it is not used to infer
an asymptotic estimate.

## 7. What remains open

The complete system of all $r$ equations is strong: over a splitting
field it has the $2^r$ square roots corresponding to independent signs
at the $r$ roots of $X^r-1$.  The section theorem does not assert
that a global eliminant is impossible.  It says that such an argument
must use genuinely nonlocal information:

1. equations outside every fixed-linear-size bounded window;
2. a $p$-dependent global property of the actual alternating sign
   assignment; or
3. arithmetic input not contained in cyclic convolution and ordinary
   Kummer periodicity.

No estimate for



$$
\sum_{\substack{p>2N+2\\p\mid E_{2N},E_{2N+2}}}\log p
$$



is proved here.  The missing lemma remains a global cross-prime coupling
whose information survives elimination at subfactorial height.

## 8. Replay

From the research directory run

    python3 scripts/root_unity_adjacent_euler_cyclic_window_section_certificate.py
    sha256sum -c results/root_unity_adjacent_euler_cyclic_window_section_hashes.sha256

The replay checks the complete cyclic equations on a declared prime
grid, the anchor construction on deterministic exact grids, the
interval inequalities, the absence of a Kummer reflection, and the
full $p=151483$ seed-window completion.  Finite computations certify
normalizations and examples only; Theorem 3.1 and its corollaries are
the all-parameter proofs.
