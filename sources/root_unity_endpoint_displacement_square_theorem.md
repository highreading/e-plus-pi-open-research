> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Endpoint multiplication displacement and an exact Wronskian square

## A lower-parameter lift, an all-parameter low-degree rank gap, and the remaining primitive-height barrier

Checked: 2026-08-27 UTC

## 1. Scope and verdict

This note isolates an exact structure in the unconstrained root-of-unity
Hermite--Padé endpoint space. It gives a much smaller corrected endpoint
than generic exterior tail elimination, and it removes the universal
two-copy denominator from the intrinsic analytic normalization.

Let $m\ge2$ and $n\ge m+1$, and put



$$
M=m(n+1),
 \qquad
 s_{m,n}=\begin{cases}
 m-1,&m\text{ odd and }n\text{ even},\\
 m,&\text{otherwise}.
 \end{cases}                                                \tag{1}
$$



The main theorem is the following.

> **Endpoint-displacement square theorem.** There is an explicitly given
> primitive polynomial
>
> 

$$
>                         C_{m,n}\in\mathbb Z[z],
> \qquad \deg C_{m,n}=s_{m,n},                              \tag{2}
>
$$


>
> such that, in every full endpoint space
>
> 

$$
>       \mathbb Q[z]_{\le D},\qquad s_{m,n}+1\le D\le n,   \tag{3}
>
$$


>
> the associated upper-parameter remainders satisfy
>
> 

$$
> R_{zC_{m,n}}(z)=zR_{C_{m,n}}(z),\qquad
> W(R_{C_{m,n}},R_{zC_{m,n}})=R_{C_{m,n}}^2.               \tag{4}
>
$$


>
> Moreover
>
> 

$$
> R_{C_{m,n}}(z)=O(z^M),\qquad
> \Delta(C_{m,n},zC_{m,n})=C_{m,n}^2,                      \tag{5}
>
$$


>
> so the Wronskian in (4) has origin order at least $2M$ and a
> nonzero primitive corrected endpoint of degree $2s_{m,n}\le2m$.

The construction is a cofactor vector in an explicit matrix with only
$m$ rows. No Siegel lemma, Pluecker elimination, or conjectural gcd
cancellation is used. Its polarization maps products in a larger kernel
space to explicit nondecomposable exterior sums and gives a
basis-independent rank-gap theorem with target degree $2m$.

The result does **not** settle the arithmetic nature of $e+\pi$. At
fixed $m$, the proved intrinsic bounds are



$$
\begin{aligned}
 \log H(C_{m,n})&\le r_{m,n}\,m n\log n+O_m(n),\\
 \log H(R_{C_{m,n}})&\le \log H(C_{m,n})+mn\log n+O_m(n),  \tag{6}
 \end{aligned}
$$



where $r_{m,n}:=r_p\le\lceil m/2\rceil$ is the selected parity-block size
from (27)--(28). The
first inequality is only an upper bound: it assumes no saving from the
primitive gcd. Every exact $m=2,3$ sequence recorded below fails the
leading degree-one-field measure comparison. Thus (4) removes the
universal $Q^2$ scale, but it does not by itself make the primitive
factor small enough.

The deterministic replay files are

* `scripts/root_unity_endpoint_displacement_square_certificate.py`;
* `results/root_unity_endpoint_displacement_square_certificate.json`.

## 2. The full endpoint construction

For $C\in\mathbb Q[z]_{\le D}$, let



$$
T_C^{(n)}(z,y)=
 \sum_{j=0}^{m-1}\sum_{a=0}^{n}b_{j,a}(C)z^ay^j           \tag{7}
$$



be the unique auxiliary polynomial for which



$$
R_C^{(n)}(z)=C(z)+(1+e^z)T_C^{(n)}(z,e^z)=O(z^M).         \tag{8}
$$



Uniqueness follows from the nonsingular confluent Vandermonde matrix on
the nodes $0,1,\ldots,m-1$, each with multiplicity $n+1$. Define



$$
\beta_C^{(n)}(z)=T_C^{(n)}(z,-1).     \tag{9}
$$



The superscript will be omitted when the parameter is $n$. For two
endpoints $C,D$, the corrected endpoint polynomial is



$$
\Delta(C,D)=W(C,D)-\{C\beta_D-D\beta_C\}.                \tag{10}
$$



The standard endpoint calculation gives



$$
W(R_C,R_D)(i\pi)=\Delta(C,D)(i\pi).     \tag{11}
$$



Let the logistic functional be



$$
\mathcal L(X^k)=\mu_k,
 \qquad
 \sum_{k\ge0}\mu_k\frac{z^k}{k!}=\frac1{1+e^z}.          \tag{12}
$$



Thus



$$
\mu_0=\frac12,
 \qquad
 \mu_k=-\frac12\sum_{j=0}^{k-1}{k\choose j}\mu_j.       \tag{13}
$$



## 3. Multiplication displacement has rank at most $m$

Write



$$
E_{b,a}=[z^b]\beta_{z^a},\qquad 0\le b\le n.             \tag{14}
$$



For $0\le b\le n$, let $\Lambda_b$ be the degree-$<M$
Hermite cardinal characterized by



$$
\Lambda_b^{(a)}(j)=(-1)^j\delta_{a,b},
 \qquad 0\le j<m,\quad0\le a\le n.                       \tag{15}
$$



Applying the inverse confluent Vandermonde matrix to the target jets
$-\mathcal L((X^k)^{(a)})$ gives



$$
E_{b,a}=-\mathcal L(\Lambda_b^{(a)}).       \tag{16}
$$



Consider the endpoint multiplication displacement



$$
\mathscr K:\mathbb Q[z]_{\le D-1}\longrightarrow
                  \mathbb Q[z]_{\le n+1},
 \qquad
 \mathscr K(C)=\beta_{zC}-z\beta_C.                       \tag{17}
$$



With $E_{b,a}=0$ outside the range in (14), its monomial entries are



$$
[z^b]\mathscr K(z^a)=E_{b,a+1}-E_{b-1,a}.                \tag{18}
$$



Put $\Lambda_{-1}=\Lambda_{n+1}=0$ and



$$
F_b=\Lambda_{b-1}-\Lambda_b',\qquad0\le b\le n+1.        \tag{19}
$$



For $0\le r\le n-1$, (15) gives



$$
F_b^{(r)}(j)=(-1)^j
 \{\delta_{b-1,r}-\delta_{b,r+1}\}=0.                    \tag{20}
$$



Consequently



$$
\Psi_{m,n-1}(X):=\prod_{j=0}^{m-1}(X-j)^n
 \quad\hbox{divides}\quad F_b(X).                          \tag{21}
$$



Since $\deg F_b\le m(n+1)-1$, there is $P_b$ of degree at most
$m-1$ such that



$$
F_b=\Psi_{m,n-1}P_b.              \tag{22}
$$



Put $c=(m-1)/2$, expand $P_b=\sum_{q=0}^{m-1}p_{bq}(X-c)^q$, and
define



$$
H_{q,a}=\mathcal L\!\left(
       \bigl((X-c)^q\Psi_{m,n-1}(X)\bigr)^{(a)}\right),
 \quad 0\le q<m,\quad0\le a<D.                            \tag{23}
$$



Equations (16), (18), and (19) give the exact factorization



$$
\boxed{
 [z^b]\mathscr K(z^a)=\sum_{q=0}^{m-1}p_{bq}H_{q,a}.}     \tag{24}
$$



In particular,



$$
\operatorname {rank}\mathscr K\le m.       \tag{25}
$$



This is an all-parameter factorization theorem, not a finite rank pattern.
The replay reconstructs every $\Lambda_b$, quotient $P_b$, and both
sides of (24) exactly on six structural anchors.

## 4. An explicit primitive low-degree kernel vector

The lower-parameter form of the logistic normality theorem proved in
`sources/root_unity_gamma_logistic_minor_audit.md` applies to (23). Its
exact hypotheses used here are



$$
H_{q,a}=0\quad\text{unless}\quad
                         a\equiv q+m(n-1)\pmod2,            \tag{26}
$$



and nonvanishing of every initial square minor inside either nonzero
parity block. Arbitrary checkerboard matrices do not suffice.

For $p\in\{0,1\}$, set



$$
\begin{aligned}
 Q_p&=\{q:0\le q<m,\ q+m(n-1)\equiv p\pmod2\},\\
 r_p&=|Q_p|,\qquad s_p=p+2r_p.                              \tag{27}
 \end{aligned}
$$



Choose $p$ for which $s_p$ is least. Direct counting gives



$$
(p,s_p)=
 \begin{cases}
 (0,m),&m\text{ even},\\
 (0,m-1),&m\text{ odd and }n\text{ even},\\
 (1,m),&m\text{ odd and }n\text{ odd}.
 \end{cases}                                               \tag{28}
$$



List $Q_p=\{q_0<\cdots<q_{r_p-1}\}$, and form



$$
\mathscr H_{i,j}=H_{q_i,p+2j},
 \qquad 0\le i<r_p,\quad0\le j\le r_p.                    \tag{29}
$$



The initial $r_p$-square minor is nonzero. Hence the cofactor vector



$$
\widetilde c_{p+2j}=(-1)^j
       \det\mathscr H_{\widehat j},
 \qquad
 \widetilde c_a=0\quad(a\not\equiv p\bmod2)               \tag{30}
$$



is nonzero and lies in the kernel of every row in (23). Its last
coefficient is the nonzero initial minor, so its degree is exactly $s_p$.
Clear denominators and divide by the coefficient gcd. This gives the
primitive $C_{m,n}$ in (2). Equations (24) and (30) prove



$$
H C_{m,n}=0,\qquad
                   \mathscr K(C_{m,n})=0.                 \tag{31}
$$



For $m=2$, put $\Psi=X^n(X-1)^n$. Then



$$
C_{2,n}(z)=\operatorname {prim}
 \left\{\mathcal L(\Psi''),-\mathcal L(\Psi)\right\}
 =a_n+b_nz^2.                                               \tag{32}
$$



The first examples are



$$
C_{2,3}=48+5z^2,\quad
 C_{2,4}=128+13z^2,\quad
 C_{2,10}=14883512320+1508015087z^2.                       \tag{33}
$$



For $m=3$ and even $n$, (30) is again quadratic; for instance



$$
C_{3,4}=2576+261z^2,\qquad
 C_{3,10}=72411737572065280+7336842960399921z^2.           \tag{34}
$$



## 5. The lower-parameter lift and the global square

The rows in (23) have a second interpretation. Construct the
lower-parameter auxiliary $T_C^{(n-1)}$, whose frequency polynomials have
degree at most $n-1$. Its unconstrained remainder initially satisfies



$$
R_C^{(n-1)}=O(z^{mn}).                                    \tag{35}
$$



The usual annihilator induction says that vanishing of the next $m$
Taylor coefficients is equivalent to the $m$ constraints with row
polynomials $1,X,\ldots,X^{m-1}$. Replacing those rows by
$1,X-c,\ldots,(X-c)^{m-1}$ is an invertible triangular change of basis,
so the constraints are exactly $HC=0$. Thus (31) improves (35) to



$$
R_C^{(n-1)}=O(z^{mn+m})=O(z^M).    \tag{36}
$$



The polynomial $T_C^{(n-1)}$ is admissible in the upper parameter-$n$
space. By uniqueness in (8),



$$
T_C^{(n)}=T_C^{(n-1)},
 \qquad R_C^{(n)}=R_C^{(n-1)}.                             \tag{37}
$$



Multiplying (36) by $z$ gives



$$
zR_C=zC+(1+e^z)zT_C^{(n-1)}=O(z^{M+1}).                  \tag{38}
$$



Since $zT_C^{(n-1)}$ has degree at most $n$, it is an admissible upper
auxiliary for $zC$. Uniqueness proves



$$
R_{zC}=zR_C.                  \tag{39}
$$



The Wronskian calculation is then an identity of entire functions:



$$
W(R_C,zR_C)=R_C(R_C+zR_C')-zR_CR_C'=R_C^2.               \tag{40}
$$



At the polynomial endpoint, the same calculation is



$$
\begin{aligned}
 W(C,zC)&=C^2,\\
 C\beta_{zC}-zC\beta_C&=C\mathscr K(C)=0,
 \end{aligned}                                             \tag{41}
$$



which proves (5).

### 5.1 Polarization and a basis-independent rank gap

Let



$$
U_D=\ker H\subseteq\mathbb Q[z]_{\le D-1}.               \tag{42}
$$



For $D\ge m+1$, the two parity blocks in (23) each contain an initial
square minor of the required size. Hence



$$
\operatorname {rank}H=m,
 \qquad \dim U_D=D-m.                                      \tag{43}
$$



Every $C,D\in U_D$ obeys the same lift. Polarizing (40)--(41) gives



$$
\boxed{
 \begin{aligned}
 \Delta(C,zD)+\Delta(D,zC)&=2CD,\\
 W(R_C,R_{zD})+W(R_D,R_{zC})&=2R_CR_D.
 \end{aligned}}                                            \tag{44}
$$



Equivalently, the symmetric bilinear map



$$
C\odot D\longmapsto
 \frac12\{C\wedge zD+D\wedge zC\}                       \tag{45}
$$



has corrected endpoint $CD$. The map in (45) need not be injective;
the rigorous statement is that its corrected image is exactly the
ordinary product space $U_DU_D$.

If $V$ is any $v$-dimensional polynomial subspace, choose a basis with
strictly increasing leading degrees $e_1<\cdots<e_v$. The $v$ products
with degree $e_1+e_i$ and the $v-1$ additional products with degree
$e_v+e_i$, $2\le i\le v$, have pairwise distinct degrees. Therefore



$$
\dim(VV)\ge2v-1.             \tag{46}
$$



Combining (43) and (46),



$$
\dim(U_DU_D)\ge2D-2m-1.           \tag{47}
$$



The number of coefficient positions $2m+1,\ldots,2D-2$ is
$2D-2m-2$. Thus



$$
U_DU_D\cap\mathbb Q[z]_{\le2m}\neq0.      \tag{48}
$$



Equations (44)--(48) prove an all-parameter exterior rank gap at target
degree $2m$. This is weaker than the experimentally frequent quadratic
collapse, but it is universal and does not rely on the false
parity-maximal-rank conjecture.

The product formulation offers a larger lattice than the single square:
one may saturate $U_D\cap\mathbb Z[z]$, pass to its symmetric square, and
kill the product coefficients above degree $2m$. Dimension (48) alone,
however, supplies no primitive-height bound for the resulting product or
its exterior preimage.  In particular, this note does not assume that a
Siegel-lemma vector in that larger lattice inherits the gcd/content of the
single cofactor.  Establishing such a saturated product-lattice gain is a
separate arithmetic problem.

## 6. Primitive normalization and height

### 6.1 Exact cancellation of the universal $Q^2$

Because $C\in\mathbb Z[z]$ is primitive, Gauss's lemma gives



$$
\operatorname {cont}(C^2)=1. \tag{49}
$$



A standard denominator which clears every lower-parameter coefficient is



$$
Q_-=
 2^{mn}
 \left(\prod_{a=0}^{n-1}a!\right)^m
 \prod_{h=1}^{m-1}h^{(m-h)n^2}.                            \tag{50}
$$



Put $\overline R_C=Q_-R_C$. Then



$$
W(\overline R_C,z\overline R_C)=\overline R_C^2,
 \qquad
 W(\overline R_C,z\overline R_C)(i\pi)=Q_-^2C(i\pi)^2.   \tag{51}
$$



The endpoint coefficient content in (51) is exactly $Q_-^2$. Hence the
intrinsically normalized analytic function is



$$
\frac{W(\overline R_C,z\overline R_C)}{Q_-^2}
             =R_C^2.                                       \tag{52}
$$



Thus neither $Q_-^2$ nor the larger universal upper-parameter $Q^2$
appears in the normalized height. This cancellation is exact. It does
not assert that the rational coefficients of $R_C$ are small.

### 6.2 A rigorous fixed-$m$ cofactor bound

The recurrence (13) proves inductively that



$$
|\mu_k|\le k!,\qquad
                         \operatorname {den}(\mu_k)\mid2^{k+1}.    \tag{53}
$$



Let



$$
K_*=mn+m-1,
 \quad r=r_p,
 \quad c=\frac{m-1}{2},                                    \tag{54}
$$



and define



$$
B_H=\left\lceil
 2^{K_*+m}K_*!K_*^{s_{m,n}}(1+|c|)^{m-1}(m!)^n
 \right\rceil.                                             \tag{55}
$$



Indeed,



$$
\|\Psi_{m,n-1}\|_1\le(m!)^n,
 \qquad
 \|(X-c)^q\|_1=(1+|c|)^q,                                 \tag{56}
$$



and taking $a$ derivatives increases the coefficient $\ell^1$-norm by at
most $K_*^a$. Equation (53) then bounds the value before denominator
clearing. The single power $2^{K_*+m}$ clears simultaneously the
denominator of $c^q$ and every moment which occurs. Thus every entry of
the integer-cleared matrix (29) has absolute value at most $B_H$. The
Leibniz determinant bound and primitive division give



$$
H(C_{m,n})\le r!B_H^r.             \tag{57}
$$



No divisor of the cofactors is assumed in (57). Stirling's formula gives
the first line of (6).

### 6.3 A direct intrinsic remainder bound

There is also a bound which avoids the universal Cramer denominator. For
the lower multiplicity $n$, define



$$
L_j(X)=\prod_{\substack{0\le\ell<m\\\ell\ne j}}
 \left(\frac{X-\ell}{j-\ell}\right)^n.                    \tag{58}
$$



If



$$
\frac1{L_j(j+Y)}=\sum_{t\ge0}d_{j,t}Y^t,                 \tag{59}
$$



then the lower Hermite cardinal for derivative $a$ at node $j$ is



$$
H_{j,a}^{[-]}(X)=
 L_j(X)\frac{(X-j)^a}{a!}
 \sum_{t=0}^{n-1-a}d_{j,t}(X-j)^t.                         \tag{60}
$$



On $|Y|=1/(2m)$, every factor in $1/L_j(j+Y)$ has modulus at most
$(1-1/(2m))^{-n}$. Cauchy's estimate, followed by the coefficient
$\ell^1$-norm estimate in (60), gives



$$
\|H_{j,a}^{[-]}\|_1\le B_{\rm card}:=
 n(m!)^n\left(1-\frac1{2m}\right)^{-n(m-1)}
 (2m^3)^{n-1}.                                             \tag{61}
$$



The target jet for $T_C^{(n-1)}$ at order $k<mn$ is



$$
h_k=-\sum_{a=0}^{\min(d,k)}c_a\frac{k!}{(k-a)!}\mu_{k-a},
 \qquad d=\deg C.                                         \tag{62}
$$



By (53),



$$
|h_k|\le(d+1)H(C)(mn-1)!.         \tag{63}
$$



The inverse confluent Vandermonde formula says that every auxiliary
coefficient is $\sum_k[X^k]H_{j,a}^{[-]}h_k$. Therefore



$$
H(T_C^{(n-1)})\le(d+1)H(C)(mn-1)!B_{\rm card}.            \tag{64}
$$



In the frequency expansion of $R_C=C+(1+e^z)T_C$, at most two auxiliary
coefficients enter any one coefficient. Consequently



$$
\boxed{
 H(R_C)\le H(C)+2(d+1)H(C)(mn-1)!B_{\rm card}.}            \tag{65}
$$



Here $H(R_C)$ is the maximum absolute value of its rational
frequency-polynomial coefficients in the primitive endpoint
normalization. Equation (65) proves the second line of (6).

## 7. Centered Schwarz and the direct factor measure

The lifted $R_C$ has frequencies $0,1,\ldots,m$, polynomial degree at
most $n-1$, and origin order at least $M$. Multiplication by
$e^{-mz/2}$ centers the frequencies at
$-m/2,-m/2+1,\ldots,m/2$, preserves origin order, and has modulus one at
$i\pi$. On $|z|=\rho\ge1$,



$$
|e^{-mz/2}R_C(z)|
 \le(m+1)nH(R_C)\rho^{n-1}e^{m\rho/2}.                    \tag{66}
$$



Put



$$
A_C=M-(n-1)=(m-1)n+m+1,
 \qquad
 \rho_*={2A_C\over m},                                    \tag{67}
$$



and



$$
\mathcal G_C=
 A_C\log{2A_C\over e\pi m}-(n-1)\log\pi.                 \tag{68}
$$



For the parameters of the theorem, $\rho_*>\pi$. Schwarz's lemma at
the optimized radius gives



$$
\boxed{
 |C(i\pi)|=|R_C(i\pi)|
 \le(m+1)nH(R_C)e^{-\mathcal G_C}.}                        \tag{69}
$$



The algebraic lower bound should be applied to the primitive factor
$C(i\pi)$, not to $C(i\pi)^2$ as a generic polynomial value. Assume
temporarily that $s=e+\pi$ is algebraic of degree



$$
r=[\mathbb Q(s):\mathbb Q].       \tag{70}
$$



Choose $\delta\in\mathbb Z_{>0}$ so that
$\theta=\delta s$ is an algebraic integer, and put



$$
\Theta=\max_{\tau:\mathbb Q(s)\hookrightarrow\mathbb C}|\tau(\theta)|,
 \quad d=\deg C,                                           \tag{71}
$$





$$
\mathcal H_C=(d+1)H(C)(\Theta+\delta)^d,
 \qquad
 \mathcal T_C=(d+1)^{r-1}\mathcal H_C^r.                  \tag{72}
$$



The cofactor in (30) has one parity $p$. Therefore



$$
A(X):=i^{-p}C(iX)\in\mathbb Z[X],
 \qquad H(A)=H(C),\qquad |A(\pi)|=|C(i\pi)|.               \tag{73}
$$



This parity phase permits the integral descent



$$
P_A(X):=\delta^dA(s-X)\in\mathcal O_{\mathbb Q(s)}[X],
 \qquad |P_A(e)|=\delta^d|C(i\pi)|.                        \tag{74}
$$



Its coefficient house is at most $\mathcal H_C$. Norming from
$\mathbb Q(s)$ directly to $\mathbb Q$ produces an integer polynomial of
degree at most $rd$ and height at most $\mathcal T_C$. This is the
sharpest field normalization supplied by the parity construction. Using
the more general polynomial $\delta^dC(i(s-X))$ over
$\mathbb Q(s,i)$ gives the same degree and leading exponent, only
different fixed phases.

Let $\mathfrak s_N,\mathfrak D_N$, and
$\varepsilon_N(T)$ be the explicit functions in equations (33)--(39) of
`sources/root_of_unity_low_degree_polynomial_e_measure.md`, obtained from
Theorem 2.1 of Ernvall-Hytönen--Matala-aho--Seppälä. When $rd\ge2$ and



$$
\log\mathcal T_C\ge
                  \mathfrak s_{rd}e^{\mathfrak s_{rd}},   \tag{75}
$$



that theorem, applied to the rational norm polynomial, gives



$$
\boxed{
 |C(i\pi)|>
 {\delta^{-d}(2\mathcal T_C)^{-rd-
       \varepsilon_{rd}(\mathcal T_C)}
  \over
  2e^{\mathfrak D_{rd}}
  \bigl((d+1)e^d\mathcal H_C\bigr)^{r-1}}.}               \tag{76}
$$



The cases $d=0$ and $rd=1$ have the elementary explicit alternatives
recorded in that source. Combining (69) and (76), a finite contradiction
would follow from



$$
\begin{aligned}
 \mathcal G_C-\log\{(m+1)nH(R_C)\}
 >{}&d\log\delta+\log2+\mathfrak D_{rd}\\
 &+(rd+\varepsilon_{rd}(\mathcal T_C))\log(2\mathcal T_C)\\
 &+(r-1)\log\bigl((d+1)e^d\mathcal H_C\bigr).              \tag{77}
 \end{aligned}
$$



For fixed hypothetical field and fixed $d$, the leading height cost on
the right is



$$
\kappa_C\log H(C),
 \qquad \kappa_C=r^2d+r-1.                                 \tag{78}
$$



Since $|W(i\pi)|=|C(i\pi)|^2$, taking the square root means that the
Wronskian comparison costs $2\kappa_C\log H(C)$. In the easiest case
$r=1$, this is $2d\log H(C)$. Treating $C^2$ as an unrelated
degree-$2d$ polynomial of height on the $H(C)^2$ scale would instead
cost about $4d\log H(C)$. The factor formulation is therefore the
sharp normalization available from this construction.

## 8. Exact fixed-$m$ diagnostics

The replay constructs the primitive cofactors and lower lifted remainders
over $\mathbb Q$. The following table records natural logarithms. The
margin is



$$
\mathcal G_C-\log((m+1)n)-\log H(R_C)-d\log H(C),         \tag{79}
$$



the leading $r=1$ version of (77), before fixed field constants.

The JSON also records separately the actual absolute exponent and the
Schwarz-certified exponent



$$
\eta_{\rm act}=-\frac{\log|C(i\pi)|}{\log H(C)},
 \qquad
 \eta_{\rm Sch}=\frac{\mathcal G_C-\log((m+1)n)-\log H(R_C)}
                         {\log H(C)}.
$$



Thus the margin in (79) is
$(\eta_{\rm Sch}-d)\log H(C)$. Neither decimal exponent is used in an
exact symbolic assertion.



$$
\begin{array}{c|r|r|r|r|r}
m&n&\log H(C)&\log H(R_C)&\log|C(i\pi)|&\text{margin}\\ \hline
2&4 &4.8520&4.1589&-1.1879&-21.1738\\
2&8 &15.6631&15.4378&-0.2256&-55.1704\\
2&12&31.2823&40.4660& 6.3373&-110.7564\\
2&16&48.1906&70.4905&14.3388&-172.7195\\
2&20&68.4804&106.2283&25.7720&-246.2458\\
2&24&89.6705&144.6494&38.1291&-323.5159\\
2&28&112.8808&186.5408&52.5196&-407.6740\\
2&30&125.2689&208.7399&60.5009&-452.3660\\ \hline
3&4 &7.8540&7.2691&-3.4037&-29.9673\\
3&8 &22.8539&29.7613&-2.5527&-78.0372\\
3&12&44.1223&67.7274& 5.1740&-150.5390\\
3&16&75.2862&120.0676&22.9757&-254.7701\\
3&20&104.2164&173.3745&38.6152&-353.6435\\
3&24&137.9924&234.0337&59.1362&-468.0572
\end{array}                                                \tag{80}
$$



The actual relative exponent



$$
-{\log(|C(i\pi)|/H(C))\over\log H(C)}                    \tag{81}
$$



also eventually drops below one in both displayed families. In
particular, the primitive values themselves eventually grow. These are
finite exact-coefficient diagnostics; no asymptotic lower bound for the
true primitive height or value is inferred from them.

## 9. Replay and logical scope

The certificate

1. reconstructs the Hermite cardinals and verifies (16), (20)--(24)
   exactly on six structural anchors;
2. constructs the parity cofactor (30), clears it primitively, and checks
   both $HC=0$ and $\mathscr K(C)=0$;
3. reconstructs the upper and lower interpolation problems independently
   and verifies (37), (39), and (40) coefficientwise;
4. checks exact origin orders, endpoint contents, and Gauss primitivity;
5. verifies the finite cofactor bound (57) and the resulting remainder
   bound (65) on every recorded row; and
6. records fourteen fixed-$m$ sequence rows, including actual and
   Schwarz-certified exponents and the factor-measure margin.

The final run stays below the required 2 GiB resident-memory cap. Decimal
values are never used to prove a symbolic identity. The package proves an
exact low-degree survivor and a sharper arithmetic ledger, not a proof
about $e+\pi$.
