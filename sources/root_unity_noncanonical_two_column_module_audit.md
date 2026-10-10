> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Noncanonical two-column inheritance at the root-of-unity endpoint

## A local module obstruction, an exact coupled criterion, and the only
## all-parameter $m=1$ exception

Checked: 2026-08-27 UTC

## 1. Verdict

Write



$$
g(z)=1+e^z,\qquad \xi=i\pi,\qquad g(\xi)=0,
 \qquad g'(\xi)=-1.                                            \tag{1}
$$



The preceding exterior-power audit observed that a representation



$$
R=C+gB                                \tag{2}
$$



inherits only the value $C(\xi)=R(\xi)$, not the derivative.  The next
question was whether a noncanonical coupling of several pairs $(C,B)$
could make two determinant columns inherited even though no individual
$B(\xi)$ vanishes.

This note gives the exact answer available at present.

1. There is a universal local rank-one obstruction.  Over algebraic
   coefficients, the analytic order at $\xi$ of a Laurent polynomial in
   $z,e^z$ is exactly its $(y+1)$-adic order before substituting
   $y=e^z$.  Consequently, (2) inherits the first $q$ individual jets
   if and only if its bivariate auxiliary polynomial already contains
   $(y+1)^{q-1}$.  In particular, a second individually inherited column
   is exactly the higher-multiplicity construction $C+g^2\widetilde B$,
   not a new coupling.

2. A determinant can evade individual inheritance.  If $C\mapsto T_C$
   is the linear auxiliary map, with $B_C(z)=T_C(z,e^z)$, put

   

$$
\beta_C(z)=T_C(z,-1).                   \tag{3}
$$



   For two endpoints $C,D$, the exact correction is

   

$$
W(C,D)(\xi)-W(R_C,R_D)(\xi)
       =\Gamma_{C,D}(\xi),\qquad
    \Gamma_{C,D}=C\beta_D-D\beta_C.                            \tag{4}
$$



   Since $\xi$ is transcendental, the correction vanishes if and only if
   the rational polynomial $\Gamma_{C,D}(z)$ is identically zero.  Thus
   (4), not a numerical endpoint comparison, is the exact two-column module
   rank test.

3. Whenever

   

$$
n+(2-m)D-\nu+2\geq0,                           \tag{5}
$$



   for two forms selected from the $\nu$-dimensional constrained endpoint
   space, $\Gamma_{C,D}=0$ forces

   

$$
C T_D-D T_C=0.                             \tag{6}
$$



   The two forms are then polynomial multiples of one common form.  They
   have rank one over $\mathbb Q(z)$, so the inherited determinant is a
   square/product of one analytic remainder rather than two genuinely new
   directions.  For the natural two-dimensional construction
   $\nu=2$, condition (5) is

   

$$
n+(2-m)D\geq0,                       \tag{7}
$$



   and therefore covers every $m\leq3$, because $n\geq D$.

4. For $m=1$, the coupled criterion can be classified for all
   $n\geq D\geq2$.  The natural two-dimensional endpoint space has
   $\Gamma=0$ exactly when

   

$$
n\ {\rm is\ even},\qquad
                         D\ {\rm is\ odd}.                     \tag{8}
$$



   In that case it is spanned by $R_0$ and $zR_0$, where $R_0$ is the
   parity-defective one-dimensional Padé form of degrees $n-1,D-1$.
   Its endpoint Wronskian is, up to a nonzero rational constant,

   

$$
C_0(z)^2.                         \tag{9}
$$



   Thus the apparent two-column gain is exactly the square of the original
   one-column gain.  The polynomial degree and logarithmic height double as
   well; this does not cancel the degree-dependent measure for $e$.

The exact grid contains 252 natural two-dimensional spaces with
$1\leq m\leq6$, $2\leq n\leq10$, and
$2\leq D\leq\min(8,n)$.  Every reduced endpoint matrix has the expected
rank.  Exactly nine correction polynomials vanish, precisely the nine
$m=1$ tuples predicted by (8), and every one is factored exactly into
$R_0,zR_0$.  There is no vanishing correction for $m\geq2$ in this
finite grid.  The last observation is diagnostic, not a theorem outside
the range covered by (5).

The remaining genuine survivor is therefore sharply localized: for
parameters where (5) fails, one would need a nonzero secondary exponential
polynomial with the exceptional zero described in Section 5.  No such
example was found and no all-parameter zero estimate excluding it is proved
here.

The replayable files are

* scripts/root_unity_two_column_module_certificate.py;
* results/root_unity_two_column_module_certificate.json.

## 2. Endpoint valuation equals $y+1$-adic valuation

Let



$$
\mathcal A=\overline{\mathbb Q}[z,y,y^{-1}],
 \qquad \mathscr E(F)(z)=F(z,e^z).                            \tag{10}
$$



The Laurent form allows arbitrary shifted integer frequencies.  Denote by
$v_{y+1}(F)$ the multiplicity of $y+1$ in $F$.

**Endpoint valuation lemma.**  For every nonzero $F\in\mathcal A$,



$$
\operatorname {ord}_{z=\xi}\mathscr E(F)
                    =v_{y+1}(F).                               \tag{11}
$$



**Proof.**  Factor



$$
F=(y+1)^vG,\qquad G(z,-1)\ne0.         \tag{12}
$$



The Laurent polynomial $G(z,-1)$ is a nonzero polynomial in $z$ with
algebraic coefficients.  Since $\xi=i\pi$ is transcendental,



$$
G(\xi,-1)\ne0.                   \tag{13}
$$



Also $1+e^z$ has a simple zero at $\xi$.  Substitution in (12) proves
(11).  $\square$

The use of algebraic coefficients is exact for the present application.
Under the hypothetical algebraicity of $s=e+\pi$, coefficients in
$\mathbb Q(s,i)$ are still algebraic, so (13) remains valid.

Suppose $B=\mathscr E(T)$.  From (2),



$$
\begin{split}
 R^{[a]}(\xi)=C^{[a]}(\xi)\quad(0\leq a<q)
 &\Longleftrightarrow \operatorname {ord}_\xi(gB)\geq q\\
 &\Longleftrightarrow (y+1)^{q-1}\mid T.                       \tag{14}
 \end{split}
$$



Thus every individually inherited $q$-jet construction is already



$$
R=C+g^q\widetilde B.                  \tag{15}
$$



There is also a purely local module formulation.  Let $\mathcal O_\xi$
be the ring of analytic germs at $\xi$.  Since $g$ is a uniformizer,



$$
\mathcal O_\xi/g\mathcal O_\xi\simeq
                    \mathbb C.                                \tag{16}
$$



Hence the space of linear jet functionals which are unchanged by adding
$gB$ for *arbitrary* germs $B$ has dimension one: it is generated by
evaluation.  A restricted finite-dimensional auxiliary family can have
accidental extra invariants; Sections 3--5 give their exact test.

## 3. The two-column correction polynomial

Let $E$ be any rational vector space of endpoint polynomials, and suppose
the origin-matching problem determines $T_C\in\mathbb Q[z,y,y^{-1}]$
linearly from $C\in E$.  Set



$$
R_C(z)=C(z)+(1+e^z)T_C(z,e^z).                                \tag{17}
$$



At $\xi$, equations (1) and (3) give



$$
R_C(\xi)=C(\xi),\qquad
 R_C'(\xi)=C'(\xi)-\beta_C(\xi).                              \tag{18}
$$



For the ordinary two-by-two Wronskian



$$
W(U,V)=UV'-VU',                       \tag{19}
$$



substitution of (18) gives (4) exactly.

The two polynomial maps



$$
C\longmapsto C(z),\qquad
               C\longmapsto\beta_C(z)                         \tag{20}
$$



have rank one on $\operatorname {span}_{\mathbb Q}\{C,D\}$ over
$\mathbb Q(z)$ if and only if $\Gamma_{C,D}=0$.  Since a nonzero
rational polynomial cannot vanish at $\xi$, this algebraic rank condition
is equivalent to determinant inheritance at the endpoint.

For a space $E$ of dimension $\nu>2$, define the linear exterior map



$$
\Omega:\bigwedge^2E\longrightarrow\mathbb Q[z],\qquad
 \Omega(C\wedge D)=C\beta_D-D\beta_C.                         \tag{21}
$$



A noncanonical two-dimensional subspace inherits two determinant columns
if and only if $\ker\Omega$ contains a nonzero *decomposable* two-vector.
Merely finding a kernel vector is insufficient when $\nu\geq4$, because
a general two-vector need not be decomposable.  Equation (21) is the exact
Plücker/module-rank criterion for all linear couplings of the form (17).

## 4. The reduced constrained family

Return to consecutive frequencies $0,\ldots,m-1$.  Put



$$
\Phi_{m,n}(X)=\prod_{j=0}^{m-1}(X-j)^{n+1},
 \qquad M=m(n+1),
 \qquad f(z)=\frac1{1+e^z}.                                   \tag{22}
$$



For $1\leq\nu\leq D+1$, the reduced endpoint space is the kernel of



$$
\mathcal L((X^q\Phi_{m,n})^{(a)}),\qquad
 0\leq q<D-\nu+1,\quad0\leq a\leq D,                         \tag{23}
$$



where



$$
\mathcal L(Q)=Q(d/dz)f(z)|_{z=0}.     \tag{24}
$$



If (23) has full row rank, its dimension is $\nu$.  For every endpoint
$C$, unique Hermite interpolation determines



$$
T_C(z,y)=\sum_{j=0}^{m-1}\sum_{a=0}^{n}t_{j,a}z^ay^j,         \tag{25}
$$



and the associated form has



$$
R_C(z)=C(z)+g(z)T_C(z,e^z)=O(z^L),
 \qquad L=M+D-\nu+1.                                         \tag{26}
$$



The certificate solves this interpolation problem over $\mathbb Q$; it
does not reconstruct the much larger original $A_j$-vector.

## 5. A zero estimate forcing polynomial-multiple degeneracy

Take two independent endpoints $C,D\in E$ and suppose
$\Gamma_{C,D}=0$.  Define



$$
F(z,y)=C(z)T_D(z,y)-D(z)T_C(z,y).     \tag{27}
$$



By (3)--(4), $F(z,-1)=0$, so



$$
F(z,y)=(y+1)H(z,y).                  \tag{28}
$$



Here



$$
\deg_yH\leq m-2,\qquad \deg_zH\leq n+D.                    \tag{29}
$$



On the exponential curve,



$$
C R_D-D R_C
 =g(CB_D-DB_C)
 =g^2H(z,e^z).                                                 \tag{30}
$$



The left side is $O(z^L)$ by (26), while $g(0)=2\ne0$.  Therefore



$$
H(z,e^z)=O(z^L).                      \tag{31}
$$



If $m\geq2$, the right side of (31) belongs to the



$$
N_H=(m-1)(n+D+1)                     \tag{32}
$$



dimensional exponential-polynomial space



$$
\sum_{j=0}^{m-2}\mathbb Q[z]_{\leq n+D}e^{jz}.   \tag{33}
$$



Every member of (33) solves a monic constant-coefficient differential
equation of order $N_H$.  A nonzero member cannot have its first $N_H$
derivatives vanish at zero.  Hence $L\geq N_H$ forces $H=0$.  Since



$$
L-N_H=n+(2-m)D-\nu+2,                        \tag{34}
$$



condition (5) proves (6).  When $m=1$, $T_C,T_D$ have $y$-degree zero,
so $F(z,-1)=F(z,y)$, and (6) follows without a zero estimate.

It remains to interpret (6).  Let $G=\gcd(C,D)$ and write



$$
C=Ga,\qquad D=Gb,\qquad (a,b)=1.      \tag{35}
$$



Unique factorization in $\mathbb Q[z,y]$ gives



$$
T_C=aU,\qquad T_D=bU.                 \tag{36}
$$



Consequently



$$
\begin{split}
 R_C&=aR_0,\qquad R_D=bR_0,\\
 R_0&=G+gU.                                                     \tag{37}
 \end{split}
$$



The two forms are independent over $\mathbb Q$ when $a/b$ is
nonconstant, but they have rank one over $\mathbb Q(z)$.  Moreover,



$$
\begin{split}
 W(C,D)&=G^2(ab'-ba'),\\
 W(R_C,R_D)&=R_0^2(ab'-ba').                                  \tag{38}
 \end{split}
$$



Thus the two small determinant factors in (38) are two copies of the same
remainder.  This is not a new exterior direction.

## 6. Complete $m=1$, $\nu=2$ classification

Assume $m=1$, $n\geq D\geq2$, and let $E_2$ be the natural
two-dimensional space (23).  Then



$$
L=n+D.                             \tag{39}
$$



The Hankel positivity proof in
sources/root_unity_constrained_hermite_pade_audit.md shows that (23) has
rank $D-1$, so $\dim E_2=2$.

Suppose first that independent $C,D\in E_2$ have $\Gamma_{C,D}=0$.
Equations (35)--(37) apply.  Put



$$
q=\max(\deg a,\deg b)\geq1.           \tag{40}
$$



The common form $R_0$ has numerator degree at most $n-q$, endpoint
degree at most $D-q$, and order at least $n+D$: at least one of the
coprime multipliers $a,b$ is nonzero at zero.  The exact $m=1$ Padé
normality theorem bounds its order by



$$
n+D-2q+2,                             \tag{41}
$$



where the last $+1$ beyond the generic dimension bound is possible only
for the parity defect.  Comparing (39) and (41) forces



$$
q=1,\qquad n-1\ {\rm odd},\qquad D-1\ {\rm even}. \tag{42}
$$



This is exactly (8).

Conversely, suppose (8) holds.  The one-dimensional $m=1$ construction
with degree bounds $n-1,D-1$ has the parity bonus and hence a nonzero form



$$
R_0=O(z^{n+D}).                       \tag{43}
$$



Both $R_0$ and $zR_0$ lie in the degree-$(n,D)$ space and satisfy
(39).  They are independent and therefore span $E_2$.  Their endpoint
correction polynomial is zero, and



$$
W(C_0,zC_0)=C_0^2.                    \tag{44}
$$



This proves the claimed if-and-only-if classification and the exact square
identity (9).

After primitive integer normalization, Gauss's lemma makes (44) the square
of the primitive $C_0$, up to sign.  Hence



$$
\deg W=2\deg C_0,\qquad
 -\log|W(i\pi)|=2[-\log|C_0(i\pi)|],                          \tag{45}
$$



while Gauss's lemma leaves no primitive-content gain.  More quantitatively,
standard coefficient/Mahler bounds give



$$
\log H(C_0^2)=2\log H(C_0)+O(D+\log(D+1)).                    \tag{46}
$$



A polynomial measure whose height exponent is linear in degree is not
helped by this duplication; it charges the doubled degree against the
doubled height.

## 7. Exact certificate

The certificate uses exact logistic moments, the exact confluent
Vandermonde interpolation map from $C$ to $T_C$, and exact polynomial
arithmetic in $\mathbb Q[z,y]$.  Its grid is



$$
1\leq m\leq6,\qquad2\leq n\leq10,\qquad
 2\leq D\leq\min(8,n),\qquad\nu=2.                            \tag{47}
$$



There are 252 rows.  Exactly 152 satisfy the proved zero-estimate condition
(7); the other 100 are retained as diagnostics.  The exact results are:

* all 252 endpoint matrices have rank $D-1$;
* the correction polynomial $\Gamma$ vanishes in exactly nine rows;
* those rows are exactly

  

$$
\begin{split}
   &(1,4,3),\\
   &(1,6,3),(1,6,5),\\
   &(1,8,3),(1,8,5),(1,8,7),\\
   &(1,10,3),(1,10,5),(1,10,7);                               \tag{48}
  \end{split}
$$



* every zero row factors exactly as $R_0,zR_0$, with the lower-degree
  $m=1$ parity bonus;
* every $m\geq2$ row has $\Gamma\ne0$.

The last item is only a finite-grid statement where (7) is false.  Since
$\Gamma\ne0$ is an exact polynomial assertion, however, it rigorously
proves that none of those particular rows inherits two columns at
$i\pi$; no numerical evaluation is involved.

The exact-tuple digest is

    71a5f73797105fce915291c4b8537c8069bb9c35d8e04e888d170c68add6762f

The replay hashes are

    script  3be45a96b60b1c9628d174eeba032e66406c566417728ce47fa926f6fbf9b665
    result  39b79c4edcb0f9eb0116555de91f3634bd744d8f121b5feea5410a28784c2b11

## 8. The remaining high-frequency survivor

For $m\geq4$ with $n<(m-2)D$ in the natural two-dimensional space, the
dimension comparison (7) does not force $H=0$.  A genuinely noncanonical
two-column construction would have to produce



$$
0\ne H(z,e^z)\in
 \sum_{j=0}^{m-2}\mathbb Q[z]_{\leq n+D}e^{jz},\qquad
 \operatorname {ord}_0H\geq m(n+1)+D-1,                       \tag{49}
$$



together with the special factorization (27)--(30) coming from two
constrained endpoint solutions.  An arbitrary dimension count allows
(48) in this range, but it does not construct the required $H$.

This is the exact missing lemma.  Proving that no such structured $H$
exists would extend the polynomial-multiple obstruction to all $m,n,D$.
Constructing one would be a genuine new coupled mechanism, after which its
primitive endpoint determinant degree, height, and value would still have
to pass the norm criterion in
sources/root_unity_endpoint_exterior_power_audit.md.
