> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Gaussian parity mixing for nondecomposable exterior endpoints

## Exact phase descent, unchanged $e$-measure cost, and the Dirichlet boundary

Checked: 2026-08-27 UTC

## 1. Verdict

The corrected exterior endpoint map has an even-output block and an
odd-output block. Suppose two admissible cleared analytic sums have
integer endpoint polynomials



$$
N_{\mathrm e}(z)\in\mathbb Z[z^2],\qquad
 N_{\mathrm o}(z)\in z\mathbb Z[z^2].                     \tag{1}
$$



Multiplying the odd analytic sum by $-i$ and adding it to the even sum
does combine the two real endpoint problems into one:



$$
\widetilde N(z)=N_{\mathrm e}(z)-iN_{\mathrm o}(z),\qquad
 \widetilde N(i\pi)\in\mathbb R.                          \tag{2}
$$



This Gaussian polynomial is exactly an ordinary integer polynomial in
disguise. If $n_j=[z^j](N_{\mathrm e}+N_{\mathrm o})$, put



$$
A(X)=\sum_{j=0}^{d}(-1)^{\lfloor j/2\rfloor}n_jX^j.      \tag{3}
$$



Then



$$
\boxed{\widetilde N(z)=A(-iz),\qquad
        \widetilde N(i\pi)=A(\pi).}                       \tag{4}
$$



The consequences are exact.

1. Gaussian content and ordinary integer content agree, up to a Gaussian
   unit. After primitive normalization,

   

$$
H\!\left({\widetilde N\over g}\right)
   =H\!\left({A\over g}\right).                            \tag{5}
$$



2. Under the temporary hypothesis that $s=e+\pi$ is algebraic of degree
   $r$, an actual degree-$d$ primitive endpoint satisfies

   

$$
-\log|A(\pi)|
   \le \bigl(r^2d+r-1+o(1)\bigr)\log H(A)                 \tag{6}
$$



   at fixed $r,d$. Equivalently,

   

$$
-{\log(|A(\pi)|/H(A))\over\log H(A)}
   \le r^2d+r+o(1).                                       \tag{7}
$$



   Thus Gaussian mixing does **not** lower either the absolute cost
   $r^2d+r-1$ or the strict relative threshold $r^2d+r$.

3. If the joint low-image lattice has rank $t\le d+1$, elementary
   Dirichlet pigeonholing gives only the generic scale

   

$$
|A(\pi)|\ll H(A)^{-(t-1)},\qquad
   {|A(\pi)|\over H(A)}\ll H(A)^{-t}.                     \tag{8}
$$



   At full rank $t=d+1$, (8) reaches relative exponent $d+1$. For
   $r=1$, this merely meets the threshold in (7); the strict inequality
   needed for a contradiction is absent. For $r>1$, it is strictly
   below the threshold.

The exact replay finds full joint rank on many small rows and primitive
candidates involving every degree $0,\ldots,d$. This confirms that the
phase combination is a genuine enlargement over choosing one parity block
at a time. It does not supply exceptional smallness, intrinsic analytic
height, or corrected content. No rank pattern is extrapolated, and no
conclusion about $e+\pi$ is claimed.

The deterministic replay files are

* scripts/root_unity_gaussian_parity_mixing_certificate.py;
* results/root_unity_gaussian_parity_mixing_certificate.json.

The script imports the frozen nondecomposable-exterior certificate only
after verifying its SHA-256 hash.

## 2. The parity blocks and their exact phase

Use the notation of
sources/root_unity_nondecomposable_exterior_sum_audit.md. The integer
corrected coefficient map is



$$
(\mathcal A_Q)_{\ell,(u,v)}
 =Q(v-u)\mathbf1_{\ell=u+v-1}
  -E^Q_{\ell-u,v}+E^Q_{\ell-v,u}.                         \tag{9}
$$



The reflection gauge in that audit proves



$$
(\mathcal A_Q)_{\ell,(u,v)}=0
 \quad\hbox{if}\quad
 \ell\not\equiv u+v-1\pmod2.                              \tag{10}
$$



Consequently, mixed endpoint-parity wedges give even corrected output,
whereas same-parity wedges give odd corrected output. In a
parity-adapted admissible endpoint space, the high-tail kernels can be
taken separately in these two blocks. The finite replay below uses the
full endpoint space $E=\mathbb Q[z]_{\le D}$, where this separation is
canonical and no parity projection through a reduced basis is needed.

Let $x_{\mathrm e}$ and $x_{\mathrm o}$ be integral exterior vectors
in the respective saturated tail kernels, and write



$$
N_{\mathrm e}=Q\Delta_{x_{\mathrm e}},\qquad
 N_{\mathrm o}=Q\Delta_{x_{\mathrm o}}.                   \tag{11}
$$



They have the parities in (1). If



$$
N_{\mathrm e}(z)+N_{\mathrm o}(z)
 =\sum_{j=0}^{d}n_jz^j,                                   \tag{12}
$$



then the coefficient of $z^j$ in $A(-iz)$, with $A$ from (3), is



$$
(-1)^{\lfloor j/2\rfloor}n_j(-i)^j
 =\begin{cases}
 n_j,&j\text{ even},\\
 -in_j,&j\text{ odd}.
 \end{cases}                                               \tag{13}
$$



This proves (4). Choosing $+i$ instead of $-i$ gives the conjugate
normalization and changes no height or value modulus.

### 2.1 Content and endpoint height

Put



$$
g=\gcd(n_0,\ldots,n_d)>0.                                \tag{14}
$$



The Gaussian coefficient ideal of $\widetilde N$ is



$$
(n_0,-in_1,n_2,-in_3,\ldots)_{\mathbb Z[i]}
 =(n_0,n_1,\ldots,n_d)_{\mathbb Z[i]}
 =g\mathbb Z[i].                                           \tag{15}
$$



The last equality follows from the ordinary Bezout identity for the
integer gcd and the divisibilities $g\mid n_j$. Thus no additional
Gaussian prime can appear in the content. If the two nonzero blocks have
separate contents $g_{\mathrm e}$ and $g_{\mathrm o}$, the joint
content is



$$
g=\gcd(g_{\mathrm e},g_{\mathrm o}),\tag{16}
$$



not their product. Mixing can therefore decrease the content available
from either block; it creates no multiplicative content bonus.

Set



$$
C(z)={\widetilde N(z)\over g},\qquad
 A_0(X)={A(X)\over g}.                                    \tag{17}
$$



Then $A_0\in\mathbb Z[X]$ and $C\in\mathbb Z[i][z]$ are primitive,
$C(z)=A_0(-iz)$, and



$$
C(i\pi)=A_0(\pi),\qquad
 H(C)=H(A_0)={\max_j|n_j|\over g}.                         \tag{18}
$$



Every coefficient is changed only by a Gaussian unit, so (18) is exact
for the usual coefficient house.

## 3. Intrinsic analytic normalization

Let $\overline{\mathcal W}_{\mathrm e}$ and
$\overline{\mathcal W}_{\mathrm o}$ be the integer-cleared exterior
Wronskian sums. As in the nondecomposable audit,



$$
\overline{\mathcal W}_{\epsilon}=Q^2\mathcal W_{\epsilon},
 \qquad
 \overline{\mathcal W}_{\epsilon}(i\pi)
   =QN_{\epsilon}(i\pi),
 \qquad \epsilon\in\{\mathrm e,\mathrm o\}.                \tag{19}
$$



Define



$$
\overline{\mathcal W}
 =\overline{\mathcal W}_{\mathrm e}
  -i\overline{\mathcal W}_{\mathrm o},\qquad
 F={\overline{\mathcal W}\over Qg}.                        \tag{20}
$$



Then



$$
\boxed{F(i\pi)=C(i\pi)=A_0(\pi),\qquad
 H(F)={H(\overline{\mathcal W})\over Qg}.}                \tag{21}
$$



The divisor in (20) is $Qg$, not $Q^2g$. One factor of $Q$ in the
cleared Wronskian remains at the endpoint in (19).

If $H_{\mathrm e}$ and $H_{\mathrm o}$ denote the separate
coefficient heights of the two cleared analytic sums, then coefficientwise



$$
\max(H_{\mathrm e},H_{\mathrm o})
 \le H(\overline{\mathcal W})
 \le\sqrt{H_{\mathrm e}^2+H_{\mathrm o}^2}
 \le\sqrt2\max(H_{\mathrm e},H_{\mathrm o}).               \tag{22}
$$



Thus Gaussian mixing costs at most the fixed factor $\sqrt2$ in analytic
house. It does not change a height exponent.

If each parity sum has origin order at least $2L_\nu$, so does $F$.
Their frequencies remain $0,\ldots,2m$; multiplying by $e^{-mz}$
centers them at $-m,\ldots,m$, preserves origin order and coefficient
height, and changes the endpoint only by the unit $(-1)^m$. Therefore
the centered Schwarz estimate remains



$$
-\log|A_0(\pi)|
 \ge 2\mathcal G_{\nu}^{\rm ctr}
 -\log\{(2m+1)(2n+1)H(F)\},                               \tag{23}
$$



whenever the stationary circle is admissible. The phase rotation creates
no additional analytic gain.

## 4. Exact algebraic reduction under $s=e+\pi$

Assume temporarily that



$$
s=e+\pi\quad\hbox{is algebraic},\qquad
 E=\mathbb Q(s),\qquad r=[E:\mathbb Q].                   \tag{24}
$$



Let $A_0\ne0$ be the primitive polynomial in (17), let
$d=\deg A_0$, and choose $\delta\in\mathbb Z_{>0}$ such that



$$
\theta=\delta s\in\mathcal O_E.                          \tag{25}
$$



Define



$$
P_A(X)=\delta^dA_0(s-X)
 =\sum_{j=0}^d a_j\delta^{d-j}(\theta-\delta X)^j
 \in\mathcal O_E[X].                                      \tag{26}
$$



At $X=e$,



$$
P_A(e)=\delta^dA_0(\pi).           \tag{27}
$$



Let



$$
\Theta=\max_{\tau:E\hookrightarrow\mathbb C}|\tau(\theta)|,
 \qquad H_A=H(A_0),
 \qquad
 \mathcal H_A=(d+1)H_A(\Theta+\delta)^d.                  \tag{28}
$$



The coefficient house of every conjugate of $P_A$ is at most
$\mathcal H_A$. Take the polynomial norm



$$
Q_A(X)=N_{E/\mathbb Q}P_A(X)\in\mathbb Z[X].             \tag{29}
$$



Then



$$
\deg Q_A\le rd,\qquad
 H(Q_A)\le\mathcal T_A:=(d+1)^{r-1}\mathcal H_A^r.        \tag{30}
$$



The first $r-1$ input degrees determine the last in each coefficient of
the product, so there are at most $(d+1)^{r-1}$ terms. Every
non-distinguished factor obeys



$$
|P_A^\tau(e)|\le(d+1)e^d\mathcal H_A.                    \tag{31}
$$



Although $Q_A$ has rational-integer coefficients, it may be viewed as a
Gaussian-integer polynomial and the explicit imaginary-quadratic Mahler
measure for $e$ applies. Using the notation
$\mathfrak s_M,\mathfrak D_M,\varepsilon_M(T)$ defined in equations
(33)--(39) of
sources/root_of_unity_low_degree_polynomial_e_measure.md, equations
(27)--(31) give



$$
\boxed{
 |A_0(\pi)|>
 {\delta^{-d}(2\mathcal T_A)^{-rd-
       \varepsilon_{rd}(\mathcal T_A)}
  \over
  2e^{\mathfrak D_{rd}}
  \bigl((d+1)e^d\mathcal H_A\bigr)^{r-1}},}               \tag{32}
$$



provided $rd\ge2$ and



$$
\log\mathcal T_A\ge
 \mathfrak s_{rd}e^{\mathfrak s_{rd}}.                    \tag{33}
$$



The cases $d=0$ and $rd=1$ have the elementary bounds recorded in the
same measure audit. Hence no ineffective exceptional case is hidden.

For fixed $r,d$,
$\varepsilon_{rd}(\mathcal T_A)=o(1)$ as $H_A\to\infty$, while



$$
\log\mathcal H_A=\log H_A+O_{s,d}(1),\qquad
 \log\mathcal T_A=r\log H_A+O_{s,r,d}(1).                 \tag{34}
$$



The norm value contributes $r(rd)=r^2d$ powers of $H_A$, and the other
$r-1$ conjugate factors contribute $r-1$. This proves (6)--(7).

### 4.1 Why the real phase does not halve the norm degree

One could instead start with $C\in\mathbb Z[i][z]$, work over
$K=\mathbb Q(s,i)$, and norm $K/\mathbb Q(i)$. Since $s$ is real,



$$
[K:\mathbb Q(i)]=[\mathbb Q(s):\mathbb Q]=r,             \tag{35}
$$



so that route also has norm degree $rd$. The phase law (4) merely lets
the coefficients descend from $K$ to $E$; it does not reduce the
polynomial degree. There is no universal norm factorization: already an
arbitrary linear $A_0(X)=a_0+a_1X$ gives a generic degree-$r$ norm in
(29).

Likewise, viewing one parity block as a polynomial in $\pi^2$ does not
halve its degree as a polynomial in $e$, because
$\pi^2=(s-e)^2$. The measure sees total $\pi$-degree $d$.

## 5. The unchanged corrected-content threshold

Write



$$
H_N=H(N_{\mathrm e}+N_{\mathrm o})=\max_j|n_j|,\qquad
 H_{\mathcal W}=H(\overline{\mathcal W}),\qquad
 \kappa=r^2d+r-1.                                        \tag{36}
$$



By (18) and (21),



$$
H(A_0)=H_N/g,\qquad H(F)=H_{\mathcal W}/(Qg).             \tag{37}
$$



Comparing the Schwarz lower estimate (23) with the fixed-degree algebraic
upper estimate (6) shows that the leading sufficient inequality for a
contradiction is



$$
\boxed{
 (\kappa+1)\log g
 >\kappa\log H_N
  +\log\{(2m+1)(2n+1)H_{\mathcal W}\}
  -2\mathcal G_\nu^{\rm ctr}-\log Q
  +O_{s,r,d}(1).}                                        \tag{38}
$$



The coefficient of $\log g$ is



$$
\kappa+1=r^2d+r,                  \tag{39}
$$



the same strict threshold as before mixing. The only new height factor is
the bounded $\sqrt2$ loss in (22), while (16) shows that the joint
content can be smaller than either separate content.

## 6. Exact Dirichlet lemma for the joint lattice

Let



$$
\Lambda\subseteq\mathbb Z^{d+1}                         \tag{40}
$$



be any rank-$t$ endpoint coefficient lattice after applying the unit
phase in (3). Choose a basis $b_1,\ldots,b_t$, let $A_b$ denote the
polynomial with coefficient vector $b$, and put



$$
B_\Lambda=\sum_{j=1}^t\|b_j\|_\infty,\qquad
 S_\Lambda=\sum_{j=1}^t|A_{b_j}(\pi)|.                   \tag{41}
$$



For every integer $q\ge1$, there is a nonzero $a\in\Lambda$ such that



$$
H(A_a)\le qB_\Lambda,\qquad
 0<|A_a(\pi)|
 \le {qS_\Lambda\over(q+1)^t-1}.                          \tag{42}
$$



Indeed, consider the $(q+1)^t$ coefficient vectors
$\sum_j u_jb_j$, $0\le u_j\le q$. Their values at $\pi$ are all
distinct: equality would give a nonzero integer polynomial vanishing at
the transcendental number $\pi$. They lie in an interval of length at
most $qS_\Lambda$. Two adjacent values differ by at most the second
quantity in (42), and their coefficient-vector difference has height at
most $qB_\Lambda$.

For a fixed lattice, (42) gives, along an unbounded sequence,



$$
|A_a(\pi)|\ll_{\Lambda,\pi}H(A_a)^{1-t}.                 \tag{43}
$$



The selected heights must be unbounded: otherwise only finitely many
nonzero lattice polynomials could occur, whereas the right side of the
value bound in (42) tends to zero.

Since $t\le d+1$, the best dimension-only absolute exponent is $d$,
and the best relative exponent is $d+1$. Comparing with (6)--(7):



$$
\begin{array}{c|c|c}
 &\text{Dirichlet full-rank boundary}&\text{algebraic threshold}\\ \hline
 \text{absolute}&d&r^2d+r-1\\
 \text{relative}&d+1&r^2d+r
 \end{array}                                               \tag{44}
$$



For $r=1$, the two columns in (44) are equal. Equality is insufficient:
the measure is contradicted only by a strict exponent improvement. For
$r>1$, the algebraic threshold is strictly larger. If $t<d+1$, the
dimension-only comparison is worse still.

In an asymptotic construction the lattice itself changes with $n$, so
the basis quantities in (41), corrected content, and analytic height
cannot be discarded as constants. Equation (42) does not assert that a
particular Hermite--Padé family attains even its generic boundary. It
proves only that the extra parity coordinates, by themselves, supply no
exponent beyond that boundary. Beating (44) would require special
arithmetic or analytic cancellation not implied by Gaussian phase
alignment or rank.

## 7. Exact finite joint-lattice replay

The replay uses



$$
m\in\{2,3\},\qquad D=n,\qquad
 E=\mathbb Q[z]_{\le D}.                                  \tag{45}
$$



For each parity block it reconstructs (9), verifies every off-parity entry
is zero, takes the saturated integer kernel of coefficients in degrees
$d+1,\ldots,n+D$, and maps that kernel to degrees $0,\ldots,d$. It
then computes the joint image-lattice HNF, an LLL-reduced basis, and its
Smith invariant factors.

For $d=2$ and $n=2,\ldots,8$, the exact joint ranks are



$$
\begin{array}{c|rrrrrrr}
n&2&3&4&5&6&7&8\\ \hline
m=2&1&2&3&3&3&3&3\\
m=3&1&2&3&3&3&3&3
\end{array}.                                               \tag{46}
$$



For $d=3$ and $n=3,\ldots,8$, they are



$$
\begin{array}{c|rrrrrr}
n&3&4&5&6&7&8\\ \hline
m=2&3&4&4&4&4&4\\
m=3&3&4&4&4&4&4
\end{array}.                                               \tag{47}
$$



On the full rows in (46), the even and odd ranks are $2+1$; on the full
rows in (47), they are $2+2$. Thus the joint phase recovers every
coefficient degree on those rows. This is finite, not an all-parameter
rank theorem.

For example, at $(m,n,D)=(2,4,4)$, the Smith factors are



$$
\begin{aligned}
 d=2:&\quad
 84934656,\ 8153726976,\ 3131031158784,\\
 d=3:&\quad
 84934656,\ 169869312,\ 8153726976,\ 3131031158784.
 \end{aligned}                                             \tag{48}
$$



A deterministic bounded search in the reduced image-lattice basis gives
the raw vectors and contents



$$
\begin{array}{c|c|c}
 d&\text{raw coefficient vector}&\text{content}\\ \hline
 2&(173946175488,-24461180928,-254803968)&84934656\\
 3&(173946175488,-8153726976,-254803968,169869312)&84934656.
 \end{array}                                               \tag{49}
$$



After primitive phase normalization, the corresponding integer
polynomials in $\pi$ are



$$
A_2(X)=2048-288X+3X^2,\qquad
 A_3(X)=2048-96X+3X^2-2X^3.                               \tag{50}
$$



These examples verify that both parities and every degree can occur in one
primitive endpoint. They are not asserted to be shortest vectors or
unusually good approximations. The replay's decimal endpoint values are
diagnostics only.

## 8. Replay and logical scope

Run from the repository root:

    python3 scripts/root_unity_gaussian_parity_mixing_certificate.py

The deterministic JSON contains 26 exact rows. It records every parity
rank, saturated tail-kernel audit, HNF/LLL transformation check, Smith
factor, saturation index, selected raw content, primitive coefficient
vector, and symbolic identity $C(iy)=A(y)$. The bounded
$\{-1,0,1\}$ search is not a shortest-vector certificate. Decimal values
at $\pi$ are not used in an assertion.

The replay is required to remain below 2 GiB RSS. Variable elapsed time and
observed RSS are printed but omitted from the deterministic JSON.

This package proves the phase-descent and measure/Dirichlet barrier. It
does not prove an all-parameter rank theorem, intrinsic analytic-height
bound, corrected-content theorem, irrationality, or transcendence of
$e+\pi$.
