> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Arithmetic of the positive cardinal Newton coefficients

## Exact local germs, denominator bounds, primitive content, and why the
## clearing factors do not solve the corrected-content problem

Checked: 2026-08-27 UTC

## 1. Verdict

The positive pole-truncation theorem gives more than a sign certificate.  Its
three cardinal numerators have explicit rational local germs at integer square
nodes.  This note derives an exact confluent-residue formula for every ordered
Newton coefficient and proves all-parameter denominator and height bounds.

The main arithmetic conclusion is a no-go for one tempting use of the large
cardinal denominators.  In the odd-$m$ families the square coordinate
already has integer nodes.  In the even-$m$ family we first change to
$y=4x$; only in that scaled coordinate are all Newton nodes integers and
the Newton-to-monomial transition unimodular over $\mathbb Z$.  If $q_N$
is the least denominator of the normalized cardinal numerator and
$\mathfrak c_N$ is the content after $q_N$-clearing, then



$$
\boxed{
\begin{array}{c|c}
\text{family}&\mathfrak c_N\\ \hline
 m=2k,\ \Lambda_0\text{ in the }y\text{-coordinate}&1\\
 m=2k+1,\ \Lambda_0&\mathfrak c_N\mid2\\
 m=2k+1,\ \Lambda_1\text{ defect}&1.
\end{array}}                                                \tag{1}
$$



Thus the often enormous denominator-clearing factor does not reappear as a
large primitive common factor.  On the contrary, for every family,



$$
H(P_N)\ge q_N,                     \tag{2}
$$



where $P_N$ is the primitive integer numerator and $kh-1$ is its degree.
The denominator contributes to primitive height, while the intrinsic content
in the chosen integer-rate coordinate remains at most two.

This is relevant to the corrected-content threshold (69) in
`sources/root_unity_corrected_exterior_primitive_height_audit.md`: content
must be tracked in its coordinate.  For odd $m$, content obtained merely by
clearing the cardinal Newton numerator contributes at most $\log2$.  For even
$m$, the conclusion $\mathfrak c_N=1$ holds only in $y$.  Returning to
the original endpoint coordinate is non-unimodular and can create a growing
power of two.  Section 6 proves the universal bound $2^{2(kh-1)}$ for that
induced content, and the exact replay exhibits large instances.  Thus the
even-family $\log2$ claim must **not** be inserted into threshold (69).

Even in the odd families, this does **not** prove that the corrected content
$\mathfrak c_Q$ is bounded.  That content also depends on the saturated
endpoint Pluecker vector and on cancellation in $\Delta=W-\Gamma$.  The
present result isolates where any exceptional content would have to come
from.

The positive bordered minor gives one nonzero linear contraction of the
Pluecker vector, but its coefficient bounds point in the wrong direction for
an upper height estimate.  They yield no lower bound for the saturation gcd
$\delta_K$.  Consequently the general saturated height bound (33) of the
corrected audit is not improved here.

The replayable files are

* `scripts/root_unity_cardinal_newton_arithmetic_certificate.py`;
* `results/root_unity_cardinal_newton_arithmetic_certificate.json`.

No claim about the arithmetic nature of $e+\pi$ is made.

## 2. Integer-rate normalizations

Put



$$
h=n+1,\qquad
 \nu=2\left\lfloor\frac n2\right\rfloor+1,
 \qquad h\in\{\nu,\nu+1\}.                                 \tag{3}
$$



Use the one-sign normalized numerators from
`sources/root_unity_gamma_positive_pole_truncation_theorem.md`.

### 2.1 Even $m=2k$

If $N^+_{2k,n}(x)$ is the normalized numerator, set



$$
\mathcal N_E(y)=N^+_{2k,n}(y/4).        \tag{4}
$$



Its ordered rate list consists of $h$ copies of each integer



$$
b_r=(2r-1)^2,\qquad1\le r\le k.        \tag{5}
$$



### 2.2 Odd $m=2k+1$

For the generic $\Lambda_0$ numerator write $\mathcal N_O(x)$, and in
the odd-$n$ parity defect write $\mathcal N_D(x)$ for the normalized
$\Lambda_1$ numerator.  Both use $h$ copies of



$$
b_r=r^2,\qquad1\le r\le k.         \tag{6}
$$



For any of the three families, list the repeated rates as



$$
\lambda_1\le\cdots\le\lambda_{p},\qquad p=kh,             \tag{7}
$$



and write



$$
\mathcal N(x)=\sum_{d=0}^{p-1}\gamma_d
          \prod_{i=1}^{d}(x+\lambda_i),\qquad\gamma_d>0.   \tag{8}
$$



The positivity in (8) is the all-parameter theorem proved in the preceding
note.  The present note determines the rational data underlying it.

## 3. Exact local germs and jets

Let $z=-b_r$ and take the branch of $\sqrt{-z}$ which is positive at the
node.  The normalized Hermite data in the three cases are the following local
germs:



$$
\begin{aligned}
 G_{E,r}(z)&=2(-1)^{r-1}(-z)^{-1/2},\\
 G_{O,r}(z)&=2\mathbf1_{r\text{ odd}}(-z)^{-s},
          \qquad s=\frac{\nu+1}{2},\\
 G_{D,r}(z)&=(1-\epsilon_r)(-z)^{-h/2}
       +\epsilon_r r(-z)^{-(h+1)/2},
          \qquad\epsilon_r=(-1)^r.                         \tag{9}
\end{aligned}
$$



For the even family, (9) follows from the local value
$(-1)^{r-1}/u$ after $y=-4u^2$.  In the odd generic family it follows
from



$$
\frac{2V(u)}{\eta u^{\nu+1}},\qquad
 V(r)=\begin{cases}\eta,&r\text{ odd},\\0,&r\text{ even}.
       \end{cases}                                         \tag{10}
$$



In the defect, $2W/\eta=u-E_1(u)$, while locally
$E_1(u)=\epsilon_r(u-r)+O((u-r)^h)$.  This gives the third line of (9).

Let



$$
a_{r,q}=[(z+b_r)^q]G_r(z).              \tag{11}
$$



Direct binomial expansion gives



$$
a^{E}_{r,q}=
 \frac{2(-1)^{r-1}}{4^q(2r-1)^{2q+1}}{2q\choose q},        \tag{12}
$$





$$
a^{O}_{r,q}=
 2\mathbf1_{r\text{ odd}}
 {s+q-1\choose q}r^{-2(s+q)},                              \tag{13}
$$



and, putting $t=h/2$ in the defect,



$$
a^{D}_{r,q}=r^{-h-2q}\left\{
 (1-\epsilon_r){t+q-1\choose q}
 +\epsilon_r\frac{(t+\tfrac12)_q}{q!}\right\}.             \tag{14}
$$



All formulas are needed only for $0\le q<h$.  They are exact rational
identities, not asymptotic estimates.

## 4. A residue formula for every Newton coefficient

Write



$$
d=Rh+q,\qquad0\le q<h,\qquad t_0=R+1,                    \tag{15}
$$



and define prefix multiplicities



$$
\mu_j=h\quad(1\le j<t_0),\qquad \mu_{t_0}=q+1.           \tag{16}
$$



Then the coefficient in (8) is the confluent divided difference of the first
$d+1$ repeated nodes.  Using the local germs (9), it has the exact formula



$$
\boxed{
 \gamma_d=
 \sum_{j=1}^{t_0}\operatorname {Res}_{z=-b_j}
 \frac{G_j(z)}{\prod_{\ell=1}^{t_0}(z+b_\ell)^{\mu_\ell}}.} \tag{17}
$$



Formula (17) is valid even though the rational expressions used for the
different local germs need not agree globally.  A confluent divided
difference depends only on the prescribed jets at its nodes.  Equivalently,
one may use the entire cosine or sinc extension from the preceding theorem;
the same sum is then the ordinary residue theorem.

For a fully rational expansion, the contribution at node $j$ is the
coefficient of $w^{\mu_j-1}$ in



$$
\left(\sum_{a=0}^{\mu_j-1}a_{j,a}w^a\right)
 \prod_{\ell\ne j}
 (b_\ell-b_j+w)^{-\mu_\ell}.                               \tag{18}
$$



Every binomial coefficient in (18) is an integer.  This form proves the
denominator bounds below and is what the exact checker replays.

## 5. A two-sided denominator theorem

Let $q_N$ be the least positive integer for which
$q_N\mathcal N\in\mathbb Z[x]$.  Define the local-jet denominator



$$
\mathcal L_{\rm loc}
   =\operatorname {lcm}_{1\le r\le k,\ 0\le q<h}
             \operatorname {den}(a_{r,q}).                 \tag{19}
$$



For the upper bound put



$$
\mathcal V_{k,h}(b)=
   \prod_{1\le i<j\le k}(b_j-b_i)^{2h-1},                 \tag{20}
$$



and



$$
\begin{aligned}
 L_E&=4^{h-1}\prod_{r=1}^k(2r-1)^{2h-1},\\
 L_O&=\prod_{r=1}^k r^{2(s+h-1)},\\
 L_D&=4^{h-1}\prod_{r=1}^k r^{3h-2}.                     \tag{21}
\end{aligned}
$$



> **Denominator theorem.**  In each family,
>
> 

$$
> \boxed{
> \mathcal L_{\rm loc}\mid q_N
> \quad\text{and}\quad
> q_N\mid L_*\mathcal V_{k,h}(b),}                         \tag{22}
>
$$


>
> where $L_*$ is the corresponding line of (21).

To prove the left divisibility, observe that the Newton basis in (8) has
integer coefficients and leading coefficient one in every degree.  Its
transition matrix to the monomial basis is therefore unitriangular over
$\mathbb Z$, with an integer inverse.  Thus the least denominator is the
same in both bases.  If $q_N\mathcal N$ has integer coefficients, then for
every integer node $-b_r$,



$$
\frac{(q_N\mathcal N)^{(q)}(-b_r)}{q!}\in\mathbb Z.       \tag{23}
$$



Equations (11)--(14) prove the first divisibility in (22).

For the upper divisibility, expand (18).  A factor associated with a pair
$(j,\ell)$ has denominator exponent



$$
\mu_\ell+r_\ell
                 \le h+(\mu_j-1)\le2h-1.                  \tag{24}
$$



Thus (20) clears every cross-node denominator.  Equations (12)--(14) show
that the corresponding $L_*$ clears every local jet.  In (14), the only
point requiring comment is



$$
\frac{(t+\tfrac12)_q}{q!}\in4^{-q}\mathbb Z. \tag{25}
$$



This follows coefficientwise from
$(1-z)^{-t-1/2}=(1-z)^{-t}(1-z)^{-1/2}$ and
$[z^a](1-z)^{-1/2}=4^{-a}{2a\choose a}$.  Equations
(20)--(25) prove the second divisibility.

## 6. Primitive content is at most two

Let



$$
\mathfrak c_N=\operatorname {cont}(q_N\mathcal N).       \tag{26}
$$



Minimality of $q_N$ implies



$$
\gcd(q_N,\mathfrak c_N)=1.         \tag{27}
$$



Indeed, if a prime divided both, then $(q_N/p)\mathcal N$ would already
have integer coefficients.

The first Newton coefficient is simply the first local value.  Equations
(12)--(14) give



$$
\gamma_0=
 \begin{cases}
 2,&E\text{ and }O,\\
 1,&D.
 \end{cases}                                                \tag{28}
$$



Because the Newton-to-monomial matrix is unimodular, $\mathfrak c_N$ is
also the gcd of the $q_N\gamma_d$.  Hence



$$
\mathfrak c_N\mid q_N\gamma_0.           \tag{29}
$$



Equations (27)--(29) show $\mathfrak c_N\mid2$ generically and
$\mathfrak c_N=1$ in the defect.  In the even family, $h\ge3$ in the
root-of-unity application, and the first repeated-node block begins



$$
\gamma_0=2,\qquad
                      \gamma_1=1,\qquad
                      \gamma_2=\frac34.                    \tag{30}
$$



Thus $4\mid q_N$.  Equations (27) and (29) force
$\mathfrak c_N=1$.  This proves (1).

Notice the direction: multiplying by a convenient nonminimal clearing
integer multiplies the displayed content by the same integer.  Primitive
normalization removes it.  Only $\mathfrak c_N$ in (26) is intrinsic.

### 6.1 The even-family coordinate change can restore dyadic content

The first line of (1) is a theorem in the integer-rate variable $y$, not
in the original endpoint variable.  Put $d=kh-1$ and let



$$
P_E(y)=q_N\mathcal N_E(y)\in\mathbb Z[y]                  \tag{30a}
$$



be the primitive polynomial; here $\mathfrak c_N=1$.  If $Z$ denotes the
original polynomial variable, the centered even-family substitution is



$$
y=-4\left(Z-\frac{2k-1}{2}\right)^2
   =-\{2Z-(2k-1)\}^2.                                     \tag{30b}
$$



Let



$$
C_E=\operatorname {cont}
 P_E\!\left(-\{2Z-(2k-1)\}^2\right).
$$



Then the following universal, coordinate-sharp-enough statement holds:



$$
\boxed{C_E\text{ is a power of two},\qquad
        1\le C_E\le2^{2d}=2^{2(kh-1)}.}                   \tag{30c}
$$



Indeed, $Q(V)=P_E(-V^2)$ is primitive of degree $2d$.  Integer
translation preserves content, so
$R(W)=Q(W-(2k-1))$ is also primitive.  Write
$R(W)=\sum_{j=0}^{2d}r_jW^j$.  The endpoint polynomial is
$R(2Z)$.  No odd prime can divide all $2^jr_j$, because it would divide
all $r_j$.  Since $R$ is primitive, some $r_j$ is odd, and therefore



$$
v_2(C_E)=\min_j\{v_2(r_j)+j\}\le2d.                      \tag{30d}
$$



The bound in (30c) is not a cosmetic caveat: the exact replay contains large
dyadic values (for example $C_E=2^{32}$ at $k=3,n=5$, while
$2d=34$).  Thus $\mathfrak c_N=1$ in $y$ does not give bounded content
after returning to $Z$.

For odd $m=2k+1$, the center $k$ is integral.  The maps
$P(x)\mapsto P(-U^2)$, multiplication by a monomial, and
$U\mapsto Z-k$ preserve primitive content.  Hence no analogous
coordinate-created denominator occurs for the isolated odd cardinal
numerators.  This observation still says nothing about the corrected
contraction $W-\Gamma$.

## 7. Explicit height bounds and denominator barriers

Let



$$
J_*=\max_{1\le r\le k,\ 0\le q<h}|a_{r,q}|.              \tag{31}
$$



The following convenient explicit upper bounds follow from (12)--(14):



$$
\begin{aligned}
 J_E&\le2,\\
 J_O&\le2{s+h-2\choose h-1},\\
 J_D&\le2{h/2+h-2\choose h-1}
       +\frac{(h/2+\tfrac12)_{h-1}}{(h-1)!}.               \tag{32}
\end{aligned}
$$



Let $N=d+1$ be the total multiplicity in (17).  After absolute values are
taken, the sum of the binomial factors in one residue is at most



$$
\sum_{r=0}^{\mu_j-1}
 {N-\mu_j+r-1\choose r}\le2^{N-1}.                        \tag{33}
$$



The one-node case is interpreted separately and satisfies the same crude
bound.  Therefore



$$
0<\gamma_d\le kJ_*2^d.             \tag{34}
$$



Since every prefix polynomial in (8) has positive coefficients and



$$
\left\|\prod_{i=1}^d(x+\lambda_i)\right\|_1
     =\prod_{i=1}^d(1+\lambda_i),                           \tag{35}
$$



one obtains the completely explicit rational-height bound



$$
H(\mathcal N)\le
 \mathcal H_*:=kJ_*\sum_{d=0}^{kh-1}
 2^d\prod_{i=1}^d(1+\lambda_i).                            \tag{36}
$$



Let



$$
P_N=\frac{q_N}{\mathfrak c_N}\mathcal N
                    \in\mathbb Z[x]                        \tag{37}
$$



be primitive.  The first node is $-1$ in all three integer-rate
normalizations.  Equations (9) and (28) give



$$
|P_N(-1)|=
 \begin{cases}
 2q_N/\mathfrak c_N,&E,O,\\
 q_N,&D.
 \end{cases}                                                \tag{38}
$$



There is a sharper coefficientwise argument.  Every $\gamma_d$ is positive,
and every prefix in (8) has nonnegative integer coefficients because all
$\lambda_i$ are positive.  The constant coefficient of $\mathcal N$ is
therefore at least $\gamma_0$.  Thus (1) and (28) imply that the constant
coefficient of $P_N$ is at least $q_N$.  Combining this observation with
(22) and (36) gives



$$
\boxed{
 q_N\le H(P_N)
 \le L_*\mathcal V_{k,h}(b)\mathcal H_*.}                 \tag{39}
$$



Thus large denominators survive in primitive height rather than primitive
content.

There are useful unconditional lower divisors already in the local values.
Let



$$
\mathscr L(K)=\operatorname {lcm}(1,2,\ldots,K),\qquad
 \mathscr L_{\rm odd}(K)=
   \operatorname {lcm}\{r\le K:r\text{ odd}\}.            \tag{40}
$$



Then



$$
\begin{aligned}
 \mathscr L_{\rm odd}(2k-1)&\mid q_N&&\text{in family }E,\\
 \mathscr L_{\rm odd}(k)^{2s}&\mid q_N&&\text{in family }O,\\
 \mathscr L(k)^h&\mid q_N&&\text{in family }D.             \tag{41}
\end{aligned}
$$



The second line uses the nonzero odd-node values $2/r^{2s}$, and the third
uses the values $1/r^h$.  The prime number theorem in its standard Chebyshev
form gives



$$
\log\mathscr L(K)=K+o(K),\qquad
 \log\mathscr L_{\rm odd}(K)=K+o(K).                       \tag{42}
$$



Consequently the odd generic and defect families already satisfy



$$
\begin{aligned}
 \log H(P_N)&\ge2sk+o(sk)&&\text{in }O,\\
 \log H(P_N)&\ge hk+o(hk)&&\text{in }D.                   \tag{43}
\end{aligned}
$$



For completeness, the even family also has an $h$-dependent fixed-$h$
strengthening.  In (12) take $q=h-1$.  If an odd prime
$p>2h-2$ and $p^a\le2k-1$, the central binomial numerator is a
$p$-adic unit at the node $2r-1=p^a$.  Hence



$$
\prod_{\substack{p\le2k-1\\p>2h-2}}
 p^{(2h-1)\lfloor\log_p(2k-1)\rfloor}\mid q_N,             \tag{44}
$$



where the product is over primes.

For fixed $h$, (42) implies



$$
\log H(P_N)\ge(4h-2)k+o(k).              \tag{45}
$$



These are denominator-height barriers, not upper estimates for the endpoint
Pluecker height.

## 8. Why this does not improve the saturated Pluecker height

Let $p=(p_{ab})$ be the primitive Pluecker vector of the saturated endpoint
kernel.  It is determined by the complementary minors of $K$ and the
saturation divisor $\delta_K$:



$$
p_{ab}=\pm\frac{\det(A_K)_{\widehat{a,b}}}
                              {\delta_K}.                   \tag{46}
$$



The positive cardinal theorem proves that one bordered contraction is
nonzero.  After clearing the relevant row $E_b$, it has the form



$$
0\ne \langle p,e_0\wedge E_b^*\rangle\in\mathbb Z.        \tag{47}
$$



An upper bound for $E_b^*$, including the bounds derived from (36), gives
from (47) only



$$
H(p)\ge
 \frac1{\sum_{a,j}|(e_0\wedge E_b^*)_{aj}|}.               \tag{48}
$$



This points in the wrong direction and is weaker than the integrality fact
$H(p)\ge1$.  No equation in Sections 2--7 contains a lower bound for
$\delta_K$.  Therefore these cardinal estimates cannot reduce the existing
upper bound



$$
H(p)\le\frac{(D-1)!B_K^{D-1}}{\delta_K}.                  \tag{49}
$$



This is a precise limitation of the present information, not a proof that no
other use of the positive representation could ever bound $p$.  An improved
saturated height theorem still has to exploit the arithmetic of *all* kernel
minors or prove a new lower bound for $\delta_K$.

## 9. The corrected-content threshold

The corrected cleared vector is



$$
N_\ell=q_Ew_\ell(p)-\sum_{a+b=\ell}\sum_jE^*_{b,j}p_{aj}.
                                                                    \tag{50}
$$



The first term in (50) is the Wronskian contraction.  It is absent from the
cardinal numerator and destroys any general divisibility transfer from
$\mathfrak c_N$ to the corrected content.  The exact corrected audit already
contains rows where a large $\Gamma$-content becomes corrected content one.

What (1) and (30c) prove is coordinate-dependent.  If a proposed gain comes
only from the isolated cardinal numerator, then



$$
\begin{aligned}
 \chi_{\rm card}&\le\log2
      &&\text{for odd }m\text{ (and }\chi_{\rm card}=0
         \text{ in the defect)},\\
 \chi_{E,y}&=0
      &&\text{for even }m\text{ in the integer-rate coordinate},\\
 \chi_{E,Z}^{\rm coord}&\le2d_E\log2,\qquad d_E=kh-1
      &&\text{for the induced return to the endpoint coordinate}.
                                                               \tag{51}
\end{aligned}
$$



The last line is genuinely larger than $\log2$; it is the only universal
even-family conclusion established here.

Write the deficit in threshold (69) as



$$
\mathscr D=\kappa\log H(N_Q)+\log(C_0H_W)
             -2\mathcal G_1-\log Q.                        \tag{52}
$$



Thus isolated odd-family cardinal clearing can meet (69) only if



$$
\mathscr D<(\kappa+1)\log2.        \tag{53}
$$



For even $m$, if one assumes that the *only* available common factor is the
coordinate-induced factor in (30c), the corresponding necessary condition is



$$
\mathscr D<2(\kappa+1)d_E\log2.           \tag{54}
$$



Equation (53) is therefore not an even-family test.  In every regime where
the deficit in (52) tends to infinity, the isolated odd cardinal source is
asymptotically irrelevant; no such conclusion follows for even $m$ unless
the deficit is compared with the linear-in-$d_E$ cap in (54).  Equations
(39)--(45) explain why the same denominators tend to increase primitive
height.

This does not bound the true $\mathfrak c_Q$.  Exceptional content may still
arise from the special decomposable vector (46), from arithmetic shared among
all corrected contractions in (50), or from cancellation in
$W-\Gamma$.  Those are precisely the remaining structured-content routes.

## 10. Exact replay

The checker uses exact rational arithmetic.  On each recorded row it

1. constructs the appropriate normalized cardinal numerator by polynomial
   CRT;
2. verifies every local jet in (12)--(14);
3. reconstructs every Newton coefficient independently from the residue
   formula (17)--(18);
4. verifies equality of the least Newton and monomial denominators;
5. verifies both divisibilities in (22), the content theorem (1), and the
   height bounds (39);
6. reconstructs the even-family endpoint-coordinate transform and verifies
   its content is dyadic and satisfies (30c); and
7. records exact coefficient-vector digests.

The generic grid is $1\le k\le3$, $2\le n\le5$; the defect grid uses
$1\le k\le3$, $n=3,5$.  The universal statements come from the proofs
above, not from extrapolation of this grid.
