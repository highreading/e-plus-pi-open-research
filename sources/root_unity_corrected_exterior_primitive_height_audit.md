> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Primitive height of the corrected root-of-unity two-column endpoint

## Exact denominators, saturated Pluecker content, a Smith theorem, and the
## Roth-exponent capacity ledger

Checked: 2026-08-27 UTC

## 1. Verdict

Put



$$
g(z)=1+e^z,\qquad \xi=i\pi,
 \qquad M=m(n+1),\qquad L=M+D-1,                         \tag{1}
$$



and let $E_2\subset\mathbb Q[z]_{\le D}$ be the natural
two-dimensional endpoint space from the constrained root-of-unity
construction.  For every $C\in E_2$, let



$$
R_C=C+gT_C(z,e^z)=O(z^L),\qquad
 \beta_C=T_C(z,-1).                                      \tag{2}
$$



For independent $C,D\in E_2$, define



$$
\Gamma_{C,D}=C\beta_D-D\beta_C,
 \qquad
 \boxed{\Delta_{C,D}=W(C,D)-\Gamma_{C,D}.}                \tag{3}
$$



The corrected endpoint is valid:



$$
\boxed{\Delta_{C,D}(i\pi)=W(R_C,R_D)(i\pi).}             \tag{4}
$$



Moreover, $W(R_C,R_D)$ has a zero of order at least $2L$ at the
origin.  Thus (3) really does transfer two analytic zero factors to one
polynomial value at $i\pi$, even when $\Gamma\ne0$.

The primitive-height audit gives the following conclusions.

1. The interpolation denominator can be cleared uniformly by

   

$$
\boxed{
   Q_{m,n}=2^M\mathscr V_{m,n},\qquad
   \mathscr V_{m,n}=
   \left(\prod_{a=0}^n a!\right)^m
   \prod_{h=1}^{m-1}h^{(m-h)(n+1)^2}.}                       \tag{5}
$$



   For every integer endpoint $C$, all coefficients of
   $Q_{m,n}T_C$, and hence all coefficients of
   $Q_{m,n}\beta_C$, are integers.  Formula (5) is a proved
   all-parameter denominator, not a pattern inferred from data.

2. The endpoint lattice must first be saturated.  If
   $p=(p_{ab})_{0\le a<b\le D}$ is its primitive Pluecker vector, then
   the bare Wronskian content, the $\Gamma$-content, and the corrected
   $\Delta$-content are three different contractions of $p$.  There
   is no divisibility implication from either of the first two to the
   third.

3. There is an exact Smith theorem for the corrected coefficient map.
   If that map has full column rank and largest Smith invariant
   $s_{\max}$, then the $q_E$-cleared corrected content divides
   $s_{\max}$.  This is sharp for arbitrary primitive exterior vectors.
   In the rank-deficient range there is no ambient primitive-vector
   content cap at all; a new theorem would have to use both decomposability
   and the special endpoint kernel.

4. The gain certified by the available Schwarz estimate is exactly a
   two-fold version of the one-column gain.  The coefficient height is
   quadratic in the two input forms.  Consequently, absent a degree
   collapse or a corrected-content theorem of the explicit size in (69)
   below, this estimate does not certify an amplified relative small-value
   exponent.  It merely duplicates the one-column ledger, while the
   corrected polynomial has degree

   

$$
d=\deg\Delta\le n+D,                 \tag{6}
$$



   usually larger than the original endpoint degree $D$.

5. On the six exact replay rows, the intrinsic corrected content is
   $1$ and the relative exponents are between
   $0.9174\ldots$ and $1.5335\ldots$, hence below the familiar Roth
   threshold $2$.  These are rigorous exact coefficient vectors followed
   by diagnostic decimal evaluations.  They are **not** extrapolated.

There is an additional logical warning.  The hypothesis $\Gamma\ne0$
alone does not prove $\Delta\ne0$, and it does not determine the degree
in (6).  In principle $\Gamma=W(C,D)\ne0$ could occur.  It is enough to
prove that $\Gamma$ has a nonzero coefficient above degree $2D-2$, but
mere nonvanishing of one low coefficient does not do this.

No conclusion about the arithmetic nature of $e+\pi$ is claimed here.

The replayable files are

* `scripts/root_unity_corrected_exterior_primitive_height_certificate.py`;
* `results/root_unity_corrected_exterior_primitive_height_certificate.json`.

## 2. The corrected endpoint identity

At $\xi=i\pi$,



$$
g(\xi)=0,\qquad g'(\xi)=-1.                                \tag{7}
$$



Therefore (2) gives



$$
R_C(\xi)=C(\xi),\qquad
 R_C'(\xi)=C'(\xi)-\beta_C(\xi),                            \tag{8}
$$



and similarly for $D$.  Taking the determinant of the two rows in (8)
gives



$$
\begin{aligned}
 W(R_C,R_D)(\xi)
 &=C(\xi)(D'-\beta_D)(\xi)
   -D(\xi)(C'-\beta_C)(\xi)\\
 &=\{W(C,D)-C\beta_D+D\beta_C\}(\xi)
 =\Delta_{C,D}(\xi),
\end{aligned}                                                \tag{9}
$$



which proves (4).

Write $R_C=z^Lu$, $R_D=z^Lv$.  The terms containing the derivative
of $z^L$ cancel, so



$$
W(R_C,R_D)=z^{2L}W(u,v).                                    \tag{10}
$$



Thus



$$
\operatorname {ord}_0W(R_C,R_D)\ge2L.   \tag{11}
$$



Finally,



$$
\deg W(C,D)\le2D-2,\qquad
 \deg\Gamma\le n+D,\qquad
 \deg\Delta\le n+D.                                        \tag{12}
$$



If $\deg\Gamma>2D-2$, then
$\Delta\ne0$ and $\deg\Delta=\deg\Gamma$.  This is the clean
degree/nonvanishing condition needed in addition to a proof that
$\Gamma\ne0$.

## 3. Exact interpolation and endpoint denominators

### 3.1 Logistic moments

Let



$$
\mu_k=\mathcal L(X^k)
 =\left.\frac{d^k}{dz^k}\frac1{1+e^z}\right|_{z=0}.          \tag{13}
$$



The identity $(1+e^z)f(z)=1$ gives



$$
\mu_0=\frac12,\qquad
 \mu_k=-\frac12\sum_{j=0}^{k-1}{k\choose j}\mu_j.          \tag{14}
$$



Induction in (14) proves



$$
2^{k+1}\mu_k\in\mathbb Z.           \tag{15}
$$



It also gives the useful absolute estimate



$$
|\mu_k|\le\frac{k!}{2}.           \tag{16}
$$



Indeed, assuming (16) below $k$,



$$
|\mu_k|\le\frac{k!}{4}\sum_{h=1}^k\frac1{h!}<\frac{k!}{2}.
$$



### 3.2 The confluent interpolation determinant

Index rows by $(j,a)$, with
$0\le j<m$, $0\le a\le n$, and columns by
$0\le k<M$.  The ordinary Hermite jet matrix is



$$
\mathscr H_{(j,a),k}=(k)_a j^{k-a},                         \tag{17}
$$



with the usual convention at $j=0$.  The confluent Vandermonde
determinant is



$$
|\det\mathscr H|
 =\left(\prod_{a=0}^n a!\right)^m
   \prod_{0\le j<\ell<m}(\ell-j)^{(n+1)^2}
 =\mathscr V_{m,n}.                                          \tag{18}
$$



Grouping the node differences by $h=\ell-j$ gives exactly (5).

For an integer endpoint
$C(z)=\sum_{a=0}^Dc_az^a$, the first $M$ jet values matched by
$T_C(z,e^z)$ are



$$
h_k=-\sum_{a\le\min(D,k)}c_a(k)_a\mu_{k-a}.                \tag{19}
$$



Equation (15) shows $2^Mh_k\in\mathbb Z$.  Cramer's rule applied to
$\mathscr H^T b=h$ now proves



$$
Q_{m,n}T_C\in\mathbb Z[z,y].         \tag{20}
$$



This proves the denominator assertion in (5).

The same conclusion can be read from the Hermite-cardinal rows.  If
$\Lambda_b$ is determined by



$$
\Lambda_b^{(a)}(j)=(-1)^j\delta_{a,b},                      \tag{21}
$$



then $\mathscr V_{m,n}\Lambda_b\in\mathbb Z[X]$, and



$$
E_{b,a}:=[z^b]\beta_{z^a}=-\mathcal L(\Lambda_b^{(a)}).    \tag{22}
$$



Equations (15), (18), and (22) imply



$$
Q_{m,n}E\in
                 \mathbb Z^{(n+1)\times(D+1)}.               \tag{23}
$$



The least common denominator $q_E$ of the entries of $E$ can be much
smaller, but always satisfies



$$
q_E\mid Q_{m,n}.                \tag{24}
$$



### 3.3 A completely explicit coefficient bound

The following bound is intentionally coarse but uniform.  Put



$$
B_0=\max\{1,(M-1)^n\max(1,m-1)^{M-1}\}.                    \tag{25}
$$



Every entry of $\mathscr H$ has absolute value at most $B_0$.  Every
cofactor therefore has absolute value at most
$(M-1)!B_0^{M-1}$.  If $H(C)\le A$, (16) and (19) give



$$
H(2^Mh)\le2^{M-1}(D+1)(M-1)!A.                             \tag{26}
$$



Consequently, for $U_C=Q_{m,n}T_C$,



$$
\boxed{
 H(U_C)\le
 2^{M-1}(D+1)M!(M-1)!B_0^{M-1}A.}                           \tag{27}
$$



This supplies an explicit numerator as well as denominator bound.

### 3.4 Saturating the endpoint kernel

Let



$$
K_{q,a}=\mathcal L\!\left((X^q\Phi_{m,n})^{(a)}\right),
 \quad0\le q\le D-2,\quad0\le a\le D,                     \tag{28}
$$



where $\Phi_{m,n}=\prod_{j=0}^{m-1}(X-j)^{n+1}$.  Put



$$
N_0=M+D-2,\qquad A_K=2^{N_0+1}K\in
 \mathbb Z^{(D-1)\times(D+1)}.                              \tag{29}
$$



The all-parameter normality theorem in the logistic-minor audit gives
$\operatorname {rank}A_K=D-1$.  Let



$$
\delta_K=\gcd\{\det(A_K)_{\widehat{a,b}}:0\le a<b\le D\}.
                                                                    \tag{30}
$$



The saturated kernel lattice
$\ker(A_K)\cap\mathbb Z^{D+1}$ has primitive Pluecker coordinates



$$
\boxed{
 p_{ab}=\pm\frac{\det(A_K)_{\widehat{a,b}}}{\delta_K},}      \tag{31}
$$



where the signs are the standard complementary-minor signs.  Formula (31)
is precisely the endpoint saturation; omitting $\delta_K$ can create a
spurious common factor in every later content.

For reference, the coefficient $\ell^1$-norm of $\Phi_{m,n}$ is
$(m!)^{n+1}$.  Equations (16) and (29) give



$$
H(A_K)\le B_K:=
 2^{N_0}N_0!N_0^D(m!)^{n+1}.                                 \tag{32}
$$



Thus



$$
H(p)\le\frac{(D-1)!B_K^{D-1}}{\delta_K}.                   \tag{33}
$$



Unlike a numerical nullspace height, (33) refers to the saturated
exterior line.

## 4. Exact corrected coefficient and content maps

Extend $p$ antisymmetrically by
$p_{aa}=0$, $p_{ba}=-p_{ab}$.  If
$C\wedge D=p$, then



$$
[z^\ell]W(C,D)
 =w_\ell(p):=
 \sum_{\substack{0\le a<b\le D\\a+b-1=\ell}}
       (b-a)p_{ab},                                          \tag{34}
$$



and (22) gives



$$
[z^\ell]\Gamma_{C,D}
 =\gamma_\ell(p):=
 \sum_{\substack{0\le a,j\le D\\0\le b\le n\\a+b=\ell}}
       E_{b,j}p_{aj}.                                        \tag{35}
$$



Let $q_E$ be as in (24), put $E^*=q_EE$, and define



$$
N_\ell=q_E[z^\ell]\Delta
       =q_Ew_\ell(p)-
        \sum_{a+b=\ell}\sum_jE^*_{b,j}p_{aj}\in\mathbb Z.  \tag{36}
$$



Equivalently, the integer linear map



$$
\mathcal A_\Delta:\bigwedge^2\mathbb Z^{D+1}
       \longrightarrow\mathbb Z^{n+D+1}                     \tag{37}
$$



has column $(u,v)$, $u<v$,



$$
(\mathcal A_\Delta)_{\ell,(u,v)}
 =q_E(v-u)\mathbf1_{\ell=u+v-1}
  -E^*_{\ell-u,v}+E^*_{\ell-v,u},                           \tag{38}
$$



where an out-of-range $E^*$-entry is zero.

There are four distinct arithmetic normalizations.



$$
\begin{aligned}
 \mathfrak c_W&=\gcd_\ell w_\ell(p),\\
 q_\Gamma&=\operatorname {lcm}_\ell\operatorname {den}
                    \gamma_\ell(p),\qquad
 \mathfrak c_\Gamma=\gcd_\ell q_\Gamma\gamma_\ell(p),\\
 q_\Delta&=\operatorname {lcm}_\ell\operatorname {den}
                    (w_\ell(p)-\gamma_\ell(p)),\\
 \mathfrak c_\Delta&=
 \gcd_\ell q_\Delta(w_\ell(p)-\gamma_\ell(p)).           \tag{39}
\end{aligned}
$$



The intrinsic primitive corrected polynomial is



$$
\boxed{
 P_\Delta(z)=\frac{q_\Delta}{\mathfrak c_\Delta}
                  \Delta(z)\in\mathbb Z[z],\qquad
 \operatorname {cont}(P_\Delta)=1.}                         \tag{40}
$$



If



$$
\mathfrak c_E:=\gcd_\ell N_\ell,
$$



then



$$
q_\Delta\mid q_E,\qquad
 \mathfrak c_E=\frac{q_E}{q_\Delta}\mathfrak c_\Delta,
 \qquad
 P_\Delta=\frac1{\mathfrak c_E}\sum_\ell N_\ell z^\ell.  \tag{41}
$$



Neither $\mathfrak c_W$ nor $\mathfrak c_\Gamma$ controls
$\mathfrak c_\Delta$.  The replay rows
$(3,5,4)$ and $(4,5,5)$, for example, have intrinsic
$\Gamma$-contents $729$ and $128$, respectively, but corrected
content $1$.  These two exact counterexamples already rule out any
general assertion that a large $\Gamma$-content automatically survives
the subtraction in (3).

Put



$$
\omega_D=\max_\ell
 \sum_{a<b,\ a+b-1=\ell}(b-a)
 =\left\lfloor\frac{(D+1)^2}{4}\right\rfloor.               \tag{42}
$$



The last equality follows by summing the arithmetic progression at fixed
$a+b$, and using symmetry about $a+b=D$.  From (36),



$$
\boxed{
 H(N)\le H(p)\{q_E\omega_D+D(D+1)H(E^*)\},}                 \tag{43}
$$



and therefore



$$
H(P_\Delta)\le
 \frac{H(p)\{q_E\omega_D+D(D+1)H(E^*)\}}{\mathfrak c_E}.   \tag{44}
$$



This is the basis-free primitive endpoint height bound.

For comparison, choose a saturated integer basis $C,D$, put
$A=\max(H(C),H(D))$, and let
$U_C=Q_{m,n}T_C$, $U_D=Q_{m,n}T_D$, with coefficient height at most
$B$.  Then



$$
N_Q:=Q_{m,n}\Delta
 =Q_{m,n}W(C,D)-C\,U_D(z,-1)+D\,U_C(z,-1),                  \tag{45}
$$



and



$$
H(N_Q)\le2D^2Q_{m,n}A^2+2m(D+1)AB.                         \tag{46}
$$



Equation (27) supplies an explicit admissible $B$.  Formula (46) is
coarser than (43), but it is convenient for the analytic remainder ledger.

## 5. The structured Smith theorem and its limitation

Let



$$
R={D+1\choose2},\qquad S=n+D+1,                             \tag{47}
$$



and regard $\mathcal A_\Delta$ as an $S$-by-$R$ integer matrix.

### Theorem

Suppose $\mathcal A_\Delta$ has full column rank $R$, with Smith
invariants



$$
s_1\mid s_2\mid\cdots\mid s_R.
$$



For every primitive $x\in\mathbb Z^R$,



$$
\operatorname {cont}
                  (\mathcal A_\Delta x)\mid s_R.             \tag{48}
$$



In particular, $\mathfrak c_E\mid s_R$.

### Proof

Choose unimodular matrices putting $\mathcal A_\Delta$ in Smith form.
Unimodular transformations preserve primitivity of the input and the gcd
of output coordinates.  Thus it is enough to consider



$$
x=(x_1,\ldots,x_R),\qquad
 \mathcal A_\Delta x=(s_1x_1,\ldots,s_Rx_R,0,\ldots,0).
$$



For each prime $p$, some $x_i$ is a $p$-adic unit.  Hence the
$p$-adic valuation of the displayed content is at most
$v_p(s_i)\le v_p(s_R)$.  This proves (48).  Equality is attained on the
last Smith basis vector, so the theorem is sharp for arbitrary primitive
inputs.  $\square$

If $\delta_j(\mathcal A_\Delta)$ denotes the gcd of the $j$-rowed
minors, then



$$
s_R=\frac{\delta_R}{\delta_{R-1}}.          \tag{49}
$$



Every entry in (38) has absolute value at most
$q_ED+2H(E^*)$, so Hadamard gives the unconditional but usually coarse
cap



$$
s_R\le R^{R/2}\{q_ED+2H(E^*)\}^{R}.                        \tag{50}
$$



Full column rank requires $S\ge R$.  When the map is rank deficient,
there is no analogue of (48) for all primitive ambient vectors.  Indeed,
take a primitive kernel vector, extend it to a unimodular basis, and write
it as the first basis vector.  If another column has nonzero image, then
$x_N=e_1+Ne_j$ is primitive while
$\operatorname {cont}(\mathcal A_\Delta x_N)$ is divisible by $N$.

This does **not** prove that endpoint Pluecker vectors have unbounded
content: $x_N$ need not be decomposable and need not arise from (28).
It proves that, in the rank-deficient range, an ambient Smith calculation
cannot supply the desired cap.  A useful theorem must exploit the
intersection of



$$
\{\text{decomposable primitive two-vectors}\}
 \cap
 \{\text{the complementary-minor vector of }K\}.             \tag{51}
$$



That is the precise structured Smith/content problem left open by this
stage.

## 6. Exact analytic height and value bounds

Use the universal clearing $Q=Q_{m,n}$, and set



$$
\overline R_C=QR_C=QC+gU_C(z,e^z),\qquad
 \overline R_D=QR_D.                                         \tag{52}
$$



These are exponential polynomials with frequencies $0,\ldots,m$,
polynomial degree at most $n$, and coefficient height at most



$$
H_R:=QA+2B.                          \tag{53}
$$



Their Wronskian has frequencies $0,\ldots,2m$, polynomial degree at
most $2n$, origin order at least $2L$, and coefficient height



$$
H_W:=H(W(\overline R_C,\overline R_D))
 \le2(m+1)(n+1)(n+m)H_R^2.                                  \tag{54}
$$



At $\xi=i\pi$, (9) gives the exact scaling



$$
W(\overline R_C,\overline R_D)(\xi)
 =Q^2\Delta(\xi)=Q\,N_Q(\xi).                               \tag{55}
$$



Let $\mathfrak c_Q=\operatorname {cont}(N_Q)$.  Then



$$
P_\Delta(\xi)
 =\frac{W(\overline R_C,\overline R_D)(\xi)}{Q\mathfrak c_Q}.
                                                                    \tag{56}
$$



For every $\rho>\pi$, Schwarz's lemma and the elementary coefficient
bound on the circle $|z|=\rho$ give



$$
|P_\Delta(i\pi)|\le
 \frac{(2m+1)(2n+1)H_W}{Q\mathfrak c_Q}
 \left(\frac\pi\rho\right)^{2L}
 \rho^{2n}e^{2m\rho}.                                       \tag{57}
$$



If



$$
\rho_*:=\frac{L-n}{m}>\pi,           \tag{58}
$$



this bound is optimized at $\rho=\rho_*$.  Define the one-column
Schwarz gain



$$
\mathcal G_1=(L-n)\log\frac{L-n}{e\pi m}-n\log\pi.         \tag{59}
$$



Then (57) becomes



$$
-\log|P_\Delta(i\pi)|\ge
 2\mathcal G_1+\log(Q\mathfrak c_Q)
 -\log\{(2m+1)(2n+1)H_W\}.                                  \tag{60}
$$



The factor $2\mathcal G_1$ is exactly twice the optimized gain for one
order-$L$, degree-$n$, frequency-$m$ remainder.  No analytic
exponent beyond duplication has appeared.

## 7. The Roth-type exponent ledger

Assume only in this section that $s=e+\pi$ is algebraic of degree $r$.
Let



$$
d=\deg P_\Delta,\qquad
 h=\log H(P_\Delta),\qquad
 u=-\log|P_\Delta(i\pi)|.                                   \tag{61}
$$



The affine substitution



$$
X\longmapsto i(s-X)
$$



turns $P_\Delta(i\pi)$ into the value at $e$ of a degree-$d$
polynomial over $\mathbb Q(s,i)$.  The relative-norm theorem in
`sources/root_of_unity_low_degree_polynomial_e_measure.md` gives, for
fixed $d$ and growing height,



$$
u\le\{r^2d+r-1+o(1)\}h.                                    \tag{62}
$$



Equivalently, the relative small-value exponent



$$
\Theta_\Delta=
 -\frac{\log(|P_\Delta(i\pi)|/H(P_\Delta))}
        {\log H(P_\Delta)}=1+\frac uh                       \tag{63}
$$



must exceed



$$
r^2d+r                          \tag{64}
$$



to contradict the algebraicity hypothesis asymptotically.  When
$r=d=1$, (64) is the familiar threshold $2$.  For growing $d$, the
exact finite-height or all-height theorem must be used; both retain a
leading height cost linear in the actual $d$.

The primitive content enters this comparison in one sharply delimited
place.  Put



$$
h_0=\log H(N_Q),\qquad \chi=\log\mathfrak c_Q,
 \qquad C_0=(2m+1)(2n+1).                                   \tag{65}
$$



Since scalar primitive normalization cancels from the ratio
$|P_\Delta(i\pi)|/H(P_\Delta)$, equations (60) and (65) give



$$
-\log\frac{|P_\Delta(i\pi)|}{H(P_\Delta)}
 \ge2\mathcal G_1+\log Q+h_0-\log(C_0H_W).                \tag{66}
$$



The numerator in (63) is independent of $\chi$; content helps only by
reducing the denominator $h=h_0-\chi$.  Writing



$$
\kappa=r^2d+r-1,                    \tag{67}
$$



the Schwarz bound can beat the leading measure only if



$$
2\mathcal G_1+\log Q-\log(C_0H_W)
      >\kappa h_0-(\kappa+1)\chi.                            \tag{68}
$$



Equivalently, the exact corrected content must meet the threshold



$$
\boxed{
 (\kappa+1)\log\mathfrak c_Q>
 \kappa\log H(N_Q)+\log(C_0H_W)
 -2\mathcal G_1-\log Q.}                                    \tag{69}
$$



Finite-height field and affine-substitution constants must be added to the
right side for a literal contradiction; (69) is the sharp leading
height/content requirement.

If $\mathcal A_\Delta$ has full column rank, (48) gives the necessary
test $\mathfrak c_E\mid s_R$.  Since



$$
\mathfrak c_Q=\frac{Q}{q_E}\mathfrak c_E,
$$



the Smith cap to insert into (69) is
$\log(Q/q_E)+\log s_R$, not merely $\log s_R$.  If even
$(\kappa+1)\{\log(Q/q_E)+\log s_R\}$ is below the right side of
(69), this Schwarz/Smith implementation cannot certify a contradiction.
If the map is rank deficient, (51) explains why a new endpoint-specific
content theorem is unavoidable.

Finally, suppose a proposed family proves a genuine noncollapse regime in
which



$$
\log H(N_Q)=(2+o(1))\eta,
 \quad\log H_W=(2+o(1))\eta,
 \quad\log Q=o(\eta),
 \quad\log\mathfrak c_Q=o(\eta).                             \tag{70}
$$



Then the lower bound for the exponent supplied by (66) is



$$
\Theta_\Delta^{\rm Schwarz}
                 :=\frac{\text{right side of (66)}}
                         {\log H(P_\Delta)}
              =\frac{\mathcal G_1}{\eta}+o(1),               \tag{71}
$$



and $\Theta_\Delta\ge\Theta_\Delta^{\rm Schwarz}$.  Thus the exponent
certified by this method is exactly the one-column relative exponent: the
analytic gain and the logarithmic height have both doubled.  A two-column
Schwarz estimate without exceptional corrected content or height/degree
collapse cannot certify an improvement.  It must still beat (64), now
with actual degree $d\le n+D$.  This is the capacity barrier, and its
hypotheses in (70) are explicit rather than inferred from a finite grid.
Additional cancellation making the true endpoint value smaller than (57)
remains a logically valid route, but would require a sharper theorem.

## 8. Exact replay

The certificate performs all rational calculations exactly.  It

1. constructs $K$, its saturated primitive Pluecker vector, every
   Hermite-cardinal row $E_b$, and the denominator in (5);
2. constructs the bare Wronskian, $\Gamma$, and corrected $\Delta$
   coefficient vectors independently and verifies their exterior
   contractions on a rational kernel basis;
3. computes the three separate intrinsic contents in (39);
4. constructs the global integer map (38), records its rank, and records
   exact Smith invariants when the selected full-column-rank map is small
   enough; and
5. evaluates the primitive corrected polynomial at $i\pi$ only as a
   high-precision diagnostic.

The exact rows are



$$
(1,4,4),\ (2,4,4),\ (3,3,2),\ (3,5,4),\ (4,5,5),\ (4,6,4). \tag{72}
$$



Their intrinsic corrected contents are all $1$.  Their relative
diagnostic exponents (63), in the order (72), are



$$
0.9174868\ldots,
 1.3671020\ldots,
 1.2873063\ldots,
 1.5334924\ldots,
 1.4468993\ldots,
 1.1304049\ldots.                                            \tag{73}
$$



The ambient map is frequently rank deficient.  For $(3,3,2)$ it has
Smith invariants



$$
1,1,64,                          \tag{74}
$$



confirming (48) on that exact row.  The much larger final invariant at
$(4,6,4)$ also illustrates that the general Hadamard/Smith cap can be far
too large to supply the desired obstruction.

The deterministic exact-row digest is

    dd7122ecfd37bc195697d973c4f5ae846b2af219944a61042cc73d3d52255a31

The replay hashes at the time of this audit are

    script  c00e04f61e323f2394cdc66cf866e7b14cfc191fcb3c39a9820264cfa6eecee1
    result  50fb246beccfc3a6eaedb78272eadb2212c3543d9b87ca9cbbb23b73d1fa40f6

The replay rows are evidence only.  The all-parameter statements in this
note are the proved identities, denominator bounds, coefficient bounds,
Smith theorem, and conditional exponent ledger above.

## 9. Exact remaining arithmetic target

Assuming an independent proof that $\Gamma\ne0$, the corrected route
still requires all of the following.

1. Prove $\Delta\ne0$, preferably together with its actual degree.  A
   nonzero $\Gamma$-coefficient above $2D-2$ suffices.
2. Compute or bound the saturated endpoint Pluecker height in (31), not
   the height of an arbitrary rational nullspace basis.
3. Prove a corrected-content or structured Smith theorem on the special
   locus (51), strong enough to meet (69).  Bare Wronskian content and
   $\Gamma$-content are irrelevant substitutes.
4. Supply a value estimate sharper than (57), or verify (69) with all
   finite-height constants and with the unknown algebraic degree $r$
   retained symbolically.

Without one of these genuinely new arithmetic inputs, the corrected
Wronskian is an exact and interesting endpoint form, but it does not yet
give a Roth-breaking exponent or a proof about $e+\pi$.
