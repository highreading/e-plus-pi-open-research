> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exterior powers of root-of-unity endpoint polynomials

## Exact determinant criteria, coupled degree, and the rank-one obstruction

Checked: 2026-08-27 UTC

## 1. Verdict

Continue to assume, only in order to test this route, that



$$
s=e+\pi\in\overline{\mathbb Q},
 \qquad r=[\mathbb Q(s):\mathbb Q].                            \tag{1}
$$



The proposed survivor was to keep several independent constrained
root-of-unity forms, take an exterior determinant of their endpoint
polynomials, and let the endpoint degree grow.  There are two exact facts
which sharply limit that proposal.

1. If $\nu$ independent endpoint polynomials have degree at most $D$,
   their canonical divided-derivative Wronskian

   

$$
W_\nu(z)=\det\bigl(C_j^{[a]}(z)\bigr)_
          {1\leq j\leq\nu,\ 0\leq a<\nu},
    \qquad C^{[a]}=\frac{C^{(a)}}{a!},                         \tag{2}
$$



   is a nonzero integer polynomial after choosing an integer basis, with

   

$$
\deg W_\nu\leq\nu(D-\nu+1).           \tag{3}
$$



   Dividing its coefficient content gives a basis-independent primitive
   polynomial up to sign.  Under (1), that primitive Wronskian gives a
   polynomial in $e$, over $\mathbb Q(s,i)$, of its *actual* degree.
   Section 5 gives an exact finite-height norm criterion.

2. In the original factorization

   

$$
R_j(z)=C_j(z)+(1+e^z)B_j(z),                 \tag{4}
$$



   only the zeroth endpoint jet is inherited:

   

$$
C_j(i\pi)=R_j(i\pi).                  \tag{5}
$$



   The derivatives of $(1+e^z)B_j$ do not vanish at $i\pi$.
   Thus all of the small numbers in (5) occupy one column of (2).  A
   determinant uses that column once, not $\nu$ times.  Equivalently, the
   exterior square of the single evaluation covector is zero.  Several
   independent small scalar values therefore do **not** automatically give
   a $\nu$-fold small determinant.

The top exterior power makes the obstruction completely visible.  For
$D+1$ independent integer polynomials with coefficient matrix $A$,



$$
\det\bigl(C_j^{[a]}(z)\bigr)_{0\leq j,a\leq D}=\det A
       \in\mathbb Z\setminus\{0\}.                             \tag{6}
$$



For the saturated full lattice it is $\pm1$, at every $z$, so it cannot
be a small endpoint value.

Higher endpoint multiplicity



$$
R_j=C_j+(1+e^z)^{h_{\rm end}}B_j             \tag{7}
$$



does supply $q=\min(h_{\rm end},\nu)$ endpoint-jet columns.  Even in the
optimistic
case $q=\nu$, however, the ordinary exterior bookkeeping does not cancel
the degree cost: when (3) is sharp and there is no exceptional primitive
height collapse, the necessary analytic gain per input height remains at
least of order



$$
r^2\nu(D-\nu+1),                          \tag{8}
$$



whose minimum for $1\leq\nu\leq D$ is $r^2D$.  With the simple factor
$h_{\rm end}=1$, the scale is worse by another factor $\nu$.  Formula
(8) is a
rigorous implication of the stated height-scale hypotheses; it is not a
universal lower bound on every possible Wronskian height.

Accordingly, the exterior-power idea has not proved (or disproved) the
transcendence of $e+\pi$.  What it leaves is now exact.  A surviving
construction must prove at least one of the following genuinely arithmetic
phenomena:

* a large degree collapse in the endpoint Wronskian;
* a large gcd in the Wronskian image of the *primitive saturated Plücker
  vector*;
* a primitive Wronskian height far below its natural exterior height; or
* sufficiently many independently small endpoint jets from (7), together
  with an analytic gain which still exceeds the degree-dependent measure.

None follows from dimension counting.  The exact grid in Section 9 finds no
large instance of any of the first three phenomena: all 460 endpoint
matrices have the expected rank, every Wronskian is nonzero, every degree
defect is only one, and the largest saturated exterior content is six.  The
grid is a finite diagnostic, not an extrapolated theorem.

The replayable files are

* `scripts/root_unity_endpoint_exterior_certificate.py`;
* `results/root_unity_endpoint_exterior_certificate.json`.

## 2. Producing $\nu$ independent endpoints

Put



$$
f(z)=\frac1{1+e^z},\qquad
 \Phi_{m,n}(X)=\prod_{j=0}^{m-1}(X-j)^{n+1},\qquad
 M=m(n+1).                                                       \tag{9}
$$



For $1\leq\nu\leq D+1$, set



$$
t=D-\nu+1.                             \tag{10}
$$



The reduced endpoint space is



$$
\begin{aligned}
 \mathcal L(Q)&:=Q(d/dz)f(z)|_{z=0},\\
 \mathcal V_\nu&:=\left\{C(z)=\sum_{a=0}^{D}c_az^a:
 \sum_{a=0}^{D}c_a\,
 \mathcal L((X^q\Phi_{m,n})^{(a)})=0,
 \ 0\leq q<t\right\}.
 \end{aligned}                                                  \tag{11}
$$



All entries in (11) are rational.  Its matrix is the
$t$-by-$(D+1)$ matrix



$$
K^{(\nu)}_{q,a}=
       \mathcal L\!\left((X^q\Phi_{m,n}(X))^{(a)}\right),
 \quad 0\leq q<t,\quad0\leq a\leq D.                          \tag{12}
$$



The division argument from
`sources/root_unity_constrained_hermite_pade_audit.md` proves the following
statement exactly.  For every $C\in\mathcal V_\nu$, there is a unique



$$
B\in\sum_{j=0}^{m-1}\mathbb Q[z]_{\leq n}e^{jz}   \tag{13}
$$



matching the first $M$ Taylor coefficients, and



$$
B(z)+C(z)f(z)=O(z^{M+t}),
 \qquad R(z)=C(z)+(1+e^z)B(z)=O(z^{M+t}).                       \tag{14}
$$



If (12) has full row rank $t$, then



$$
\dim_{\mathbb Q}\mathcal V_\nu=\nu.  \tag{15}
$$



Thus one obtains $\nu$ independent endpoints by sacrificing precisely
$\nu-1$ orders from the one-dimensional construction.  In particular,



$$
\operatorname {ord}_0R\geq
                    M+D-\nu+1.                                 \tag{16}
$$



Full rank in (15) is an exact normality requirement, not a consequence of
the variable count.  The certificate proves it only on the stated finite
grid.  No all-parameter normality theorem is claimed here.

## 3. The canonical exterior polynomial

Let $C_1,\ldots,C_\nu\in\mathbb Z[z]_{\leq D}$ be an integer basis of
the saturated lattice



$$
\Lambda_\nu=\mathcal V_\nu
                         \cap\mathbb Z[z]_{\leq D}.             \tag{17}
$$



Write $A=(c_{j,k})$ for its $\nu$-by-$(D+1)$ coefficient matrix and,
for $I=\{k_1<\cdots<k_\nu\}$, put



$$
\Delta_I=\det A_{*,I}.                 \tag{18}
$$



The vector $(\Delta_I)_I$ is primitive because (17) is saturated.  It is
canonical up to sign.  Cauchy--Binet applied to (2) gives the exact formula



$$
W_\nu(z)=
 \sum_{|I|=\nu}\Delta_I
   \det\!\left(\binom{k_j}{a}\right)_
       {1\leq j\leq\nu,\ 0\leq a<\nu}
   z^{\sum_{k\in I}k-\nu(\nu-1)/2}.                            \tag{19}
$$



Every exponent in (19) is nonnegative.  Its maximum gives (3).

The Wronskian is nonzero.  Indeed, row-reduce the basis so that its distinct
pivot degrees are



$$
0\leq d_1<\cdots<d_\nu\leq D.          \tag{20}
$$



The leading coefficient in (2) contains



$$
\det\!\left(\binom{d_j}{a}\right)_
       {1\leq j\leq\nu,\ 0\leq a<\nu}
 =\frac{\prod_{j>k}(d_j-d_k)}{\prod_{a=0}^{\nu-1}a!}\ne0.     \tag{21}
$$



Consequently the *actual* degree is



$$
d=\deg W_\nu=
                 \sum_{j=1}^{\nu}d_j-\frac{\nu(\nu-1)}2.      \tag{22}
$$



Equation (22) is the exact degree-collapse criterion.  The maximal pivot
pattern $D-\nu+1,\ldots,D$ gives $d=\nu(D-\nu+1)$.  Any improvement
must be proved as a rank defect in the filtered spaces
$\mathcal V_\nu\cap\mathbb Q[z]_{\leq k}$; it cannot be inferred from
(3).

Let



$$
G_\nu=\gcd\{[z^k]W_\nu:0\leq k\leq d\},\qquad
 \widetilde W_\nu=G_\nu^{-1}W_\nu\in\mathbb Z[z].              \tag{23}
$$



Then $\widetilde W_\nu$ is primitive and is independent of the saturated
integer basis up to sign.  The content $G_\nu$ in (23) is not the
irrelevant denominator/content of the auxiliary Hermite--Pade vector.  It
is genuine endpoint-only exterior content, and a large value of it would
be a real survivor.

Since $i\pi$ is transcendental, (21) also gives



$$
\widetilde W_\nu(i\pi)\ne0.            \tag{24}
$$



## 4. Exact coefficient and endpoint bounds

Suppose the chosen saturated basis satisfies



$$
H(C_j)\leq H_0.                        \tag{25}
$$



The divided derivative has integer coefficients and



$$
\|C_j^{[a]}\|_1
 \leq H_0\sum_{k=a}^{D}\binom{k}{a}
 =H_0\binom{D+1}{a+1}.                                        \tag{26}
$$



The determinant expansion therefore gives



$$
H(W_\nu)\leq
 \nu!H_0^\nu\prod_{a=0}^{\nu-1}\binom{D+1}{a+1},              \tag{27}
$$



and hence



$$
H(\widetilde W_\nu)\leq
 {\nu!H_0^\nu\over G_\nu}
       \prod_{a=0}^{\nu-1}\binom{D+1}{a+1}.                   \tag{28}
$$



These are upper bounds.  They do not rule out cancellation in the actual
primitive Wronskian height.

Now let $\xi=i\pi$.  If, for some $0\leq q\leq\nu$, certified endpoint
estimates give



$$
\max_j|C_j^{[a]}(\xi)|\leq
 \begin{cases}
   \epsilon_a,&0\leq a<q,\\
   B_a,&q\leq a<\nu,
 \end{cases}                                                    \tag{29}
$$



then the same determinant expansion gives



$$
|\widetilde W_\nu(i\pi)|\leq
 {\nu!\over G_\nu}
       \prod_{a<q}\epsilon_a\prod_{q\leq a<\nu}B_a.           \tag{30}
$$



Equations (28) and (30) track the same endpoint content.  No full-vector
height occurs.

For uniform notation, put



$$
H_0=e^\eta,\qquad G_\nu=e^g,\qquad
 \epsilon_a\leq e^{-u},\qquad B_a\leq e^b.                    \tag{31}
$$



Then (28)--(30) read



$$
\begin{split}
 \log H(\widetilde W_\nu)
   &\leq\nu\eta+A_{D,\nu}-g,\\
 -\log|\widetilde W_\nu(i\pi)|
   &\geq q u-(\nu-q)b+g-\log\nu!,                             \tag{32}\\
 A_{D,\nu}&=\log\nu!+
       \sum_{a=0}^{\nu-1}\log\binom{D+1}{a+1}.
 \end{split}
$$



The opposite directions in (32) are important: these elementary bounds
alone do not prove a two-sided primitive height scale.

## 5. Exact polynomial-in-$e$ norm criterion

Choose $\delta\in\mathbb Z_{>0}$ such that



$$
\theta=\delta s
                    \in\mathcal O_{\mathbb Q(s)},              \tag{33}
$$



and let



$$
\Theta=\max_{\tau:\mathbb Q(s)\hookrightarrow\mathbb C}
                      |\tau(\theta)|.                          \tag{34}
$$



For the actual degree $d$ in (22), define



$$
P_W(X)=\delta^d\widetilde W_\nu(i(s-X))
       \in\mathcal O_{\mathbb Q(s,i)}[X].                      \tag{35}
$$



Then



$$
P_W(e)=\delta^d\widetilde W_\nu(i\pi),\qquad
 H(P_W)\leq\widehat H:=(d+1)H(\widetilde W_\nu)
                              (\Theta+\delta)^d.                \tag{36}
$$



This uses the actual $d$, not the ambient bound in (3).

Assume $rd\geq2$, put



$$
T=(d+1)^{r-1}\widehat H^r,                  \tag{37}
$$



and suppose the explicit threshold



$$
\log T\geq\mathfrak s_{rd}e^{\mathfrak s_{rd}}  \tag{38}
$$



holds.  The constants $\mathfrak s_M,\mathfrak D_M$ and
$\varepsilon_M(T)$ are defined explicitly in equations (33)--(39) of
`sources/root_of_unity_low_degree_polynomial_e_measure.md`.  Its relative
norm theorem gives



$$
|P_W(e)|>
 \frac{(2T)^{-rd-\varepsilon_{rd}(T)}}
 {2e^{\mathfrak D_{rd}}
       ((d+1)e^d\widehat H)^{r-1}}.                            \tag{39}
$$



Combining (30), (36), and (39) gives the promised exact criterion.  The
algebraicity hypothesis (1) is impossible if



$$
\boxed{
 {\delta^d\nu!\over G_\nu}
       \prod_{a<q}\epsilon_a\prod_{q\leq a<\nu}B_a
 \leq
 \frac{(2T)^{-rd-\varepsilon_{rd}(T)}}
 {2e^{\mathfrak D_{rd}}
       ((d+1)e^d\widehat H)^{r-1}}.}                           \tag{40}
$$



Every object in (40) is explicit, and the only endpoint height is
$H(\widetilde W_\nu)$.  When (38) is unavailable, equation (46) of the
same companion source gives a completely explicit all-height replacement
for the right side of (40), with field degree $2r$ and polynomial degree
$d$.

For fixed $d$ and growing primitive height, (39) becomes



$$
-\log|\widetilde W_\nu(i\pi)|
 \leq(r^2d+r-1+o(1))\log H(\widetilde W_\nu).                  \tag{41}
$$



Equivalently, if one measures the relative endpoint
$|\widetilde W_\nu(i\pi)|/H(\widetilde W_\nu)$, its exponent must exceed
$r^2d+r$, including the familiar extra $+1$, to contradict (1).

If $d=0$, primitivity gives $\widetilde W_\nu=\pm1$, so there is no
small value.  The exceptional case $rd=1$ has the elementary continued-
fraction estimate recorded in the companion source and introduces no
ineffective gap.

## 6. Why repeated scalar endpoint values give only one gain

From (4), differentiation at $\xi=i\pi$ gives



$$
R_j'(\xi)=C_j'(\xi)-B_j(\xi),                                 \tag{42}
$$



and higher derivatives contain further jets of $B_j$.  Thus a bound for
$R_j(\xi)$ transfers to column $a=0$ of (2), but bounds for the other
columns do not follow.  In (29)--(32), the original construction has only



$$
q=1.                              \tag{43}
$$



There is no determinant arrangement which uses the same column more than
once.  In invariant language, evaluation at $\xi$ is one covector
$\ell_\xi$, and



$$
\ell_\xi\wedge\ell_\xi=0.             \tag{44}
$$



Multiplying the $\nu$ small values instead would give a polynomial of
degree at most $\nu D$; it is a symmetric product, not an exterior
power, and does not remove the linear degree cost.

For (7), the difference $R_j-C_j$ has a zero of order
$h_{\rm end}$ at $\xi$.
Therefore



$$
R_j^{[a]}(i\pi)=C_j^{[a]}(i\pi),
                         \qquad0\leq a<h_{\rm end}.            \tag{45}
$$



This is the exact way to obtain $q=\min(h_{\rm end},\nu)$ small columns.
It still
requires separate, uniform analytic estimates for those derivatives of
$R_j$; equation (45) by itself supplies no smallness.

## 7. Coupled $D\to\infty$: the exponent ledger

Let



$$
h_W=\log H(P_W),\qquad u_W=-\log|P_W(e)|.                     \tag{46}
$$



When the finite-height theorem applies, the logarithm $L^{\rm EH}$ of
the reciprocal right side in (39) satisfies exactly



$$
L^{\rm EH}\geq r^2d\,h_W.             \tag{47}
$$



Indeed, the norm polynomial has degree $rd$, and
$\log T\geq r h_W$.  If the threshold fails, the optimized all-height
Fischler--Rivoal bound gives



$$
L^{\rm FR}\geq(c_r d-1)h_W,
 \quad
 c_r=8r^2+4r\sqrt{4r^2-2r}-2r>0.                              \tag{48}
$$



Consequently, a contradiction through either available measure must beat
a height budget linear in the *actual exterior degree* $d$.  This is a
necessary condition, not a claim that either lower bound is optimal.

To compare the formal exterior scales, suppose in addition that a proposed
family proves the two-sided, noncollapse estimates



$$
\log H(\widetilde W_\nu)=(1+o(1))\nu\eta,
 \qquad g=o(\nu\eta),
 \qquad (\nu-q)b+\log\nu!=o(qu),                              \tag{49}
$$



with the affine-substitution terms $O_s(d+\log d)$ negligible relative
to $\nu\eta$.  Equations (32) and (47) then force, as a necessary scale
for contradiction,



$$
\frac u\eta\gtrsim r^2\frac{d\nu}{q}.\tag{50}
$$



If the maximal degree in (3) is attained, (50) becomes



$$
\frac u\eta\gtrsim
 \begin{cases}
   r^2\nu^2(D-\nu+1),&h_{\rm end}=1\text{ and hence }q=1,\\
   r^2\nu(D-\nu+1),&h_{\rm end}\geq\nu\text{ and hence }q=\nu.
 \end{cases}                                                    \tag{51}
$$



For $1\leq\nu\leq D$,



$$
\nu(D-\nu+1)-D=(\nu-1)(D-\nu)\geq0.        \tag{52}
$$



Thus even the optimistic $q=\nu$ exterior power retains at least the
linear $r^2D$ cost; middle exterior powers are quadratically worse in
$D$.  With the original $q=1$, adding independent scalar endpoints is
worse still.

The hypotheses in (49) delimit the logical scope.  A large $g$, a small
actual height, or a collapse in the pivot-degree sum (22) invalidates the
generic reduction to (51) and remains a legitimate arithmetic target.
This audit has not assumed those phenomena away; it has isolated them.

## 8. The top determinant and its norm

Let $N=D+1$ and take any $N$ independent integer polynomials
$C_0,\ldots,C_D$ with coefficient matrix $A$.  The Taylor map from
coefficients to divided derivatives at $z$ is triangular with diagonal
one.  This proves (6) directly.

Under (1), define the uniformly cleared polynomials



$$
P_j(X)=\delta^D C_j(i(s-X)).                  \tag{53}
$$



Their coefficient determinant, equivalently their full divided-derivative
Wronskian, is the exact constant



$$
\det(P_j^{[a]}(X))_{0\leq j,a\leq D}
 =\delta^{DN}(-i)^{N(N-1)/2}\det A.                            \tag{54}
$$



It is a nonzero algebraic integer, independent of $s$ and $X$.  Its
absolute norm is at least one; in fact (54) gives it explicitly.  If the
integer basis is saturated in the full coefficient lattice, $|\det A|=1$.

For example, if $q$ endpoint-jet columns in (54) had entries at most
$\delta^D\epsilon$, and all remaining columns had entries at most
$\delta^DB$, the determinant expansion would force



$$
1\leq N!\epsilon^qB^{N-q}.             \tag{55}
$$



Thus making more columns small necessarily makes other jets compensate.
For the top exterior power there is no primitive-height loophole: after
primitive normalization its polynomial is exactly $\pm1$.

## 9. Exact finite grid

The certificate uses exact rational logistic moments, exact nullspaces of
(12), and exact determinants.  For each rational endpoint space it first
makes the vector of maximal minors primitive; this is the saturated
Plücker vector.  It then evaluates (19) over $\mathbb Z$, records its
coefficient gcd $G_\nu$, and makes the Wronskian primitive.  Selected
cases are independently checked by constructing (2) directly and by two
basis changes.

The grid is



$$
1\leq m\leq4,\quad2\leq D\leq6,\quad D\leq n\leq8,
 \quad1\leq\nu\leq D+1,                                       \tag{56}
$$



containing 460 quadruples.  The exact results are:

* every matrix (12) has rank $D-\nu+1$;
* every Wronskian is nonzero and obeys (3);
* every top exterior primitive Wronskian is $1$;
* 44 Wronskians have a degree defect, always exactly one;
* within this grid, those 44 tuples are exactly
  $m,n$ odd, $D\equiv\nu\pmod2$, and $\nu\leq D$;
* 50 saturated Wronskians have nontrivial content, but the maximum is only
  six.

The parity description in the fifth item is an exact description of this
finite list, not an all-parameter parity theorem.

Here is one diagnostic slice.  Decimal values are not used for any exact
claim.



$$
\begin{array}{c|c|c|c|c}
 (m,n,D)&\nu&d&\text{digits of }H(\widetilde W_\nu)
              &|\widetilde W_\nu(i\pi)|\\ \hline
 (4,8,6)&1&6&22&4.6515\times10^{-7}\\
         &2&10&39&1.2610\times10^{15}\\
         &3&12&45&9.2009\times10^{22}\\
         &4&12&45&3.9367\times10^{29}\\
         &5&10&42&2.0766\times10^{28}\\
         &6&6&25&1.2081\times10^{26}\\
         &7&0&1&1
\end{array}                                                     \tag{57}
$$



In this slice the one-dimensional endpoint is small in absolute value;
every higher nontrivial exterior value is large.  This is consistent with
the rank-one obstruction, but it is not an asymptotic lower bound.

The deterministic exact-tuple digest is

    bfc5cd29de8cd7e7394a6f75885298b0da9445b04656d9f21fdf32f7b9bc9fae

The replay hashes at the time of this audit are

    script  b233dea8890e530f0017958bca9cfdbbb7a072d617b4c922afb62cde0cf08313
    result  f0b3dac47625930a698c2bb5f69ef79b8b9e89380f32c18d9d19dd6b5f753a52

## 10. Exact remaining lemma

The naive exterior-power claim is now ruled out: $\nu$ independent
values of the same scalar endpoint functional do not yield $\nu$ small
determinant factors, and the top exterior power is an integer constant.
This is a rigorous obstruction, independent of the finite grid.

What is not ruled out is a construction proving, uniformly in a coupled
$(m,n,D,\nu,h_{\rm end})$-regime, all of the following:

1. normality of (12) and nonvanishing of the chosen endpoint jets;
2. an actual degree $d$ from (22) much smaller than its generic value;
3. an endpoint-only content/height estimate for (23), not for the auxiliary
   vector;
4. $q$ independent derivative estimates in (29), necessarily using
   higher endpoint multiplicity when $q>1$; and
5. the strict explicit norm comparison (40), or its all-height analogue.

Absent such a theorem, exterior powers do not cancel the linear-in-degree
cost of the available measure for $e$.  Proving one of items 2--4 at the
required scale would be genuinely new arithmetic information rather than a
repackaging of the original Hermite--Pade dimension count.
