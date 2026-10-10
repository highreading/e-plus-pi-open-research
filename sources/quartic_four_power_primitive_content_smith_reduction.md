> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Four quartic powers: exact cofactor content and the selected Smith obstruction

Date: 2026-08-27.

## 1. Scope and conclusion

For four adjacent quartic powers, write the two rational rows which must
be cancelled as



$$
L=(L_0,L_1,L_2,L_3),\qquad E=(E_0,E_1,E_2,E_3).
$$



The accepted four-power construction forms a cubic coefficient polynomial
from the quadratic Hankel annihilator of $L$.  This note determines the
integer content of that cubic exactly and places the remaining endpoint
content in Smith normal form.  No saddle calculation is repeated here.

There are four exact conclusions.

1.  For any integral clearing $\lambda,\epsilon$ of the two rows, the raw
    phase-removing coefficient vector $c$ has

    

$$
\boxed{\operatorname {cont}(c)
      =\operatorname {cont}(q)\operatorname {cont}(e).}   \tag{1}
$$



    More precisely, if $q=g_q q^*$ with $q^*$ primitive and

    

$$
\widehat e_s=\sum_{j=0}^2q_j^*\epsilon_{j+s},
      \qquad h=\gcd(\widehat e_0,\widehat e_1),
$$



    then

    

$$
\boxed{\operatorname {cont}(c)=g_q^2h.}             \tag{2}
$$



2.  If $A=(\lambda;\epsilon)$ and $\delta_2(A)$ is the gcd of
    its $2$ by $2$ minors, then

    

$$
\boxed{\delta_2(A)\mid\gcd(e_0,e_1)\mid
      \operatorname {cont}(c).}                           \tag{3}
$$



    Thus much of the large raw cofactor content is forced saturation
    content.  Dividing it out is mandatory before discussing coefficient
    height.

3.  Let $K=\ker_{\mathbb Z}A$, let $B$ be a jointly cleared two-row
    endpoint matrix, and suppose

    

$$
M=\begin{pmatrix}A\\B\end{pmatrix}\in M_4(\mathbb Z)
$$



    has full rank.  If the endpoint image $B(K)$ has Smith invariants
    $s_1\mid s_2$, then

    

$$
s_1s_2=\frac{|\det M|}{\delta_2(A)}.                 \tag{4}
$$



    For every primitive $v\in K$, there is a primitive Smith-coordinate
    pair $(u,w)$ for which

    

$$
\boxed{\gcd((Bv)_1,(Bv)_2)
       =s_1\gcd\left(u,\frac{s_2}{s_1}\right).}            \tag{5}
$$



    This is the exact selected-content formula.  In particular every
    primitive-direction content divides $s_2$, while primitive directions
    attaining $s_1$ and $s_2$ both exist.

4.  The first Smith invariant also has an exact determinant-divisor
    formula.  If $\rho,\beta$ are the rows of $B$, put

    

$$
N_\rho=\begin{pmatrix}A\\\rho\end{pmatrix},\qquad
      N_\beta=\begin{pmatrix}A\\\beta\end{pmatrix}.
$$



    Then

    

$$
\boxed{
      s_1=\frac{\gcd(\delta_3(N_\rho),\delta_3(N_\beta))}
                    {\delta_2(A)},\qquad
      s_2=\frac{|\det M|}{\delta_2(A)s_1}.}                \tag{6}
$$



Equations (1)--(6) rigorously rule out any content estimate which is
uniform over all kernel directions and substantially smaller than the
largest Smith invariant.  They do **not** bound the selected Smith
coordinate $u$ of the canonical phase-removing vector.  That one gcd in
(5), together with the difference between a block clearing and the least
clearing of the selected endpoint pair, is the remaining arithmetic
obstruction.  The critical-regime computations in the certificate are
diagnostics only.  Nothing here classifies $e+\pi$.

## 2. Integral normalization

Start with the rational rows $L,E$.  Multiply each row by any nonzero
rational number which makes it integral, and write the resulting integer
rows as



$$
\lambda=(\lambda_0,\ldots,\lambda_3),\qquad
 \epsilon=(\epsilon_0,\ldots,\epsilon_3).                 \tag{7}
$$



The saturated coefficient lattice is



$$
K=\{v\in\mathbb Z^4:A v=0\},\qquad
 A=\begin{pmatrix}\lambda\\\epsilon\end{pmatrix}.        \tag{8}
$$



Scaling $\lambda$ and $\epsilon$ changes a raw determinant vector, but
does not change its primitive direction.  For a canonical computation one
may take each of the two integer rows in (7) primitive.  The proofs below
do not require that convention.

To match the rational endpoint pair requested here, put



$$
X=(8R_0,\ldots,8R_3),\qquad
 Y=(b_0,\ldots,b_3).                                      \tag{9}
$$



Choose one positive integer $\Delta$ which clears all eight entries of
$X,Y$, and set



$$
\rho=\Delta X,\qquad \beta=\Delta Y,\qquad
 B=\begin{pmatrix}\rho\\\beta\end{pmatrix}.              \tag{10}
$$



Using one common endpoint unit is important: for a coefficient vector
$v$, the integer pair $Bv$ is exactly



$$
Bv=\Delta(8v\cdot R,v\cdot b).                           \tag{11}
$$



The same lattice theorem applies to the alternative rows $(R,b/8)$ used
in the earlier note.  Passing from those rows to (9) multiplies both
endpoint units by $8$; it changes $s_1,s_2$ by that common unit but leaves
$s_2/s_1$ and the reduced rational endpoint direction unchanged.

## 3. The cubic and its exact coefficient content

Define



$$
\begin{aligned}
 q_0&=\lambda_1\lambda_3-\lambda_2^2,\\
 q_1&=\lambda_1\lambda_2-\lambda_0\lambda_3,\\
 q_2&=\lambda_0\lambda_2-\lambda_1^2,                    \tag{12}\\
 e_0&=q_0\epsilon_0+q_1\epsilon_1+q_2\epsilon_2,\\
 e_1&=q_0\epsilon_1+q_1\epsilon_2+q_2\epsilon_3.
 \end{aligned}
$$



Let



$$
Q(t)=q_0+q_1t+q_2t^2
$$



and form



$$
\begin{aligned}
 C(t)&=(e_1-e_0t)Q(t)=\sum_{j=0}^3c_jt^j,                 \tag{13}\\
 c&=(e_1q_0, e_1q_1-e_0q_0,
        e_1q_2-e_0q_1, -e_0q_2).
 \end{aligned}
$$



The cross-product definition of $q$ gives the two exact Hankel
identities



$$
\sum_{j=0}^2q_j\lambda_j=0,\qquad
 \sum_{j=0}^2q_j\lambda_{j+1}=0.                          \tag{14}
$$



Equations (12)--(14) imply



$$
c\cdot\lambda=c\cdot\epsilon=0.                         \tag{15}
$$



Assume $Q$ and $e_1-e_0t$ are nonzero.  For an integer polynomial $F$,
write $\operatorname {cont}(F)$ for the positive gcd of its coefficients.
Gauss's lemma says



$$
\operatorname {cont}(FG)
 =\operatorname {cont}(F)\operatorname {cont}(G).         \tag{16}
$$



Applying (16) to (13) proves (1).  There is a useful normalized form.
Write



$$
q=g_q q^*,\qquad g_q=\gcd(q_0,q_1,q_2),                 \tag{17}
$$



where $q^*$ is primitive, and define



$$
\widehat e_s=\sum_{j=0}^2q_j^*\epsilon_{j+s},\qquad
 h=\gcd(\widehat e_0,\widehat e_1),\qquad
 \eta_s=\widehat e_s/h.                                  \tag{18}
$$



Then $e_s=g_q\widehat e_s$, and hence



$$
\gcd(e_0,e_1)=g_qh,\qquad
 \operatorname {cont}(c)=g_q^2h.                         \tag{19}
$$



The primitive canonical coefficient polynomial is therefore



$$
\boxed{C^*(t)=Q^*(t)(\eta_1-\eta_0t),}                  \tag{20}
$$



where $Q^*(t)=\sum q_j^*t^j$.  Both factors in (20) are
primitive, so its coefficient vector $c^*$ is primitive.  It is exactly
$c/\operatorname {cont}(c)$ up to overall sign.

If the two cleared rows are rescaled by integers $a,b$, then



$$
q\mapsto a^2q,\qquad e\mapsto a^2be,\qquad
 c\mapsto a^4bc.                                         \tag{21}
$$



Thus division by the full content in (19) makes $c^*$ independent of the
chosen row clearing.  It is the intrinsic integer direction of the
rational four-power construction.

## 4. The forced determinantal divisor

For $0\leq i<j\leq3$, put



$$
p_{ij}=\lambda_i\epsilon_j-\lambda_j\epsilon_i.          \tag{22}
$$



Direct expansion of (12) gives



$$
\boxed{
 \begin{aligned}
 e_0&=-\lambda_3p_{01}+\lambda_2p_{02}-\lambda_1p_{12},\\
 e_1&= \lambda_0p_{23}-\lambda_1p_{13}+\lambda_2p_{12}.
 \end{aligned}}                                          \tag{23}
$$



The second determinantal divisor is



$$
\delta_2(A)=\gcd_{i<j}p_{ij}.                            \tag{24}
$$



Equation (23) proves



$$
\delta_2(A)\mid e_0,\qquad \delta_2(A)\mid e_1,         \tag{25}
$$



which is (3).  Combining (19) and (25) also gives the exact integral
quantity



$$
\frac{\operatorname {cont}(c)}{\delta_2(A)}
 =\frac{g_q^2h}{\delta_2(A)}\in\mathbb Z.                 \tag{26}
$$



This separates two effects which should not be conflated:

* $\delta_2(A)$ is forced by saturation of the two-row integer matrix;
* the remaining factor in (26) is special to the Hankel-selected cubic.

The raw content itself is not invariant under row rescaling.  The
primitive vector (20), the rational endpoint pair it produces, and the
selected Smith coordinate below are the scale-invariant objects.

## 5. A direct formula for the canonical endpoint pair

For any integer row $x=(x_0,x_1,x_2,x_3)$ define its two compressed
$q^*$-moments by



$$
\widehat x_0=\sum_{j=0}^2q_j^*x_j,\qquad
 \widehat x_1=\sum_{j=0}^2q_j^*x_{j+1}.                  \tag{27}
$$



Taking the scalar product of (20) with $x$ gives the exact identity



$$
\boxed{x\cdot c^*=\eta_1\widehat x_0-\eta_0\widehat x_1.} \tag{28}
$$



In particular the endpoint content of the canonical vector, in the
joint units (10), is exactly



$$
\boxed{
 g_\Delta(c^*)=\gcd\left(
 \eta_1\widehat\rho_0-\eta_0\widehat\rho_1,
 \eta_1\widehat\beta_0-\eta_0\widehat\beta_1
 \right).}                                               \tag{29}
$$



Thus the four large endpoint scalar products reduce to two $2$ by $2$
determinants after the primitive quadratic annihilator is known.  Formula
(29) is exact, but it is not by itself an upper bound: the two determinants
can still have a large common prime-power divisor.

## 6. The endpoint quotient and its two Smith invariants

Assume $A$ has rank two and $M=(A;B)$ has rank four.  Since $K$ is the
kernel of a homomorphism between free abelian groups, it is a saturated
rank-two lattice.  The endpoint restriction



$$
B|_K:K\longrightarrow\mathbb Z^2                       \tag{30}
$$



is injective: a vector in its kernel is in the kernel of the nonsingular
matrix $M$.  Put



$$
\Gamma=B(K).                                             \tag{31}
$$



To make the lattice convention explicit, define column maps



$$
\mathcal M:\mathbb Z^4\longrightarrow\mathbb Z^4,
 \qquad v\longmapsto(Av,Bv),
 \qquad
 \mathcal A:\mathbb Z^4\longrightarrow\mathbb Z^2,
 \qquad v\longmapsto Av.
$$



Projection onto the first two coordinates gives the exact sequence



$$
0\longrightarrow\mathbb Z^2/\Gamma
 \mathop{\longrightarrow}^{\iota}
 \operatorname{coker}\mathcal M
 \mathop{\longrightarrow}^{\bar\pi}
 \operatorname{coker}\mathcal A
 \longrightarrow0.                                       \tag{32}
$$



Here



$$
\iota([y])=[(0,y)],\qquad
 \bar\pi([(a,y)])=[a].
$$



Indeed, $\iota([y])=0$ precisely when $(0,y)=(Av,Bv)$ for some
$v$, which forces $v\in K$ and $y\in\Gamma$.  Conversely, if
$[(a,y)]$ maps to zero, then $a=Av$ for some $v$, and subtracting
$\mathcal M(v)$ leaves a representative of the form $(0,y-Bv)$.

The orders of the last two finite groups are $|\det M|$ and
$\delta_2(A)$.  Hence



$$
[\mathbb Z^2:\Gamma]=\frac{|\det M|}{\delta_2(A)}.      \tag{33}
$$



This proves (4).

The individual endpoint-coordinate ideals can also be read from
determinantal divisors.  For $x=\rho$ or $\beta$, let



$$
N_x=\begin{pmatrix}A\\x\end{pmatrix}.                   \tag{34}
$$



Equivalently, let



$$
\mathcal N_x:\mathbb Z^4\longrightarrow\mathbb Z^3,
 \qquad v\longmapsto(Av,xv).
$$



The same projection argument now gives



$$
0\longrightarrow\mathbb Z/x(K)
 \mathop{\longrightarrow}^{\iota_x}
 \operatorname{coker}\mathcal N_x
 \mathop{\longrightarrow}^{\bar\pi_x}
 \operatorname{coker}\mathcal A
 \longrightarrow0.                                       \tag{35}
$$



Here $\iota_x([t])=[(0,t)]$ and
$\bar\pi_x([(a,t)])=[a]$.  The same kernel calculation as above
proves exactness; in particular, these are cokernels of the displayed
column maps, not quotients by row lattices.

Therefore



$$
x(K)=d_x\mathbb Z,\qquad
 d_x=\frac{\delta_3(N_x)}{\delta_2(A)}.                  \tag{36}
$$



The first Smith invariant of $\Gamma$ is the gcd of every coordinate of
every vector in $\Gamma$.  Equations (31) and (36) give



$$
s_1=\gcd(d_\rho,d_\beta)
 =\frac{\gcd(\delta_3(N_\rho),\delta_3(N_\beta))}
        {\delta_2(A)}.                                    \tag{37}
$$



Together with (33), this proves (6).  It also gives the explicitly
integral Smith ratio



$$
\boxed{
 T=\frac{s_2}{s_1}
 =\frac{|\det M|\,\delta_2(A)}
 {\gcd(\delta_3(N_\rho),\delta_3(N_\beta))^2}
 \in\mathbb Z.}                                          \tag{38}
$$



## 7. Exact selected content in Smith coordinates

Choose bases of $K$ and $\mathbb Z^2$.  In these bases the map (30) is an
integer matrix $G$.  Smith normal form supplies unimodular matrices
$U,V$ such that



$$
UGV=\begin{pmatrix}s_1&0\\0&s_2\end{pmatrix},\qquad
 s_1\mid s_2.                                             \tag{39}
$$



Let a primitive vector of $K$ have coordinates $(u,w)$ in the Smith
domain basis.  Then $\gcd(u,w)=1$.  A unimodular transformation of the
endpoint coordinates preserves the ideal generated by the two
coordinates, so



$$
\begin{aligned}
 \gcd((Bv)_1,(Bv)_2)
 &=\gcd(s_1u,s_2w)\\
 &=s_1\gcd(u,(s_2/s_1)w)\\
 &=s_1\gcd(u,s_2/s_1).                                    \tag{40}
 \end{aligned}
$$



This proves (5).  Several consequences are worth recording explicitly:



$$
s_1\mid\gcd(Bv)\mid s_2                                  \tag{41}
$$



for every primitive $v\in K$, and the two Smith-basis directions attain
$s_1$ and $s_2$.  In particular



$$
\max_{\substack{v\ \mathrm{primitive}}}\gcd(Bv)=s_2
 \geq\sqrt{s_1s_2}
 =\sqrt{\frac{|\det M|}{\delta_2(A)}}.                   \tag{42}
$$



Thus, if the quotient index is exponential in a parameter, there are
primitive kernel directions with exponential endpoint content.  No bound
which is uniform over all directions can be subexponential in that
situation.

The canonical phase-removing vector $c^*$ is primitive in
$\mathbb Z^4$ by (20), hence also primitive as an element of
$K\subseteq\mathbb Z^4$.  Therefore (40) applies to this particular
direction and becomes



$$
\boxed{g_\Delta(c^*)=s_1\gcd(u_c,T),}                    \tag{43}
$$



where $u_c$ is its first Smith-domain coordinate and $T$ is (38).  This
is a complete exact reduction, not an estimate.  The quartic problem is
now the selected gcd $\gcd(u_c,T)$; the existence of some other direction
with content $s_2$ does not imply that this gcd is large.

The sharpness of this distinction is visible without any asymptotics.
Take



$$
A=\begin{pmatrix}1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
 B_N=\begin{pmatrix}0&0&1&0\\0&0&0&2^{2N}\end{pmatrix}. \tag{44}
$$



Then $K$ is generated by the last two coordinate vectors,
$s_1=1,s_2=2^{2N}$.  One primitive direction has endpoint content $1$ and
the other has endpoint content $2^{2N}$.  Hence even an exponentially
large quotient determinant cannot decide a preselected direction without
its Smith coordinate.  This example is a lattice sharpness example, not
a quartic-coordinate example.

## 8. Block content versus the intrinsic rational-pair content

There are two endpoint gcds, and confusing them creates a false
``exponential absorption'' conclusion.

For the canonical vector let



$$
z=(8c^*\cdot R,c^*\cdot b)\in\mathbb Q^2.               \tag{45}
$$



Let $\Delta_c$ be the least positive integer which clears these two
selected rational numbers, and define their intrinsic content by



$$
g_{\mathrm{rat}}(c^*)=\gcd((\Delta_cz)_1,(\Delta_cz)_2). \tag{46}
$$



The block clearing $\Delta$ in (10) clears every endpoint entry, so
$\Delta_c\mid\Delta$.  Equations (11) and (46) give



$$
\boxed{
 g_\Delta(c^*)=\frac{\Delta}{\Delta_c}\,
                 g_{\mathrm{rat}}(c^*).}                  \tag{47}
$$



The factor $\Delta/\Delta_c$ is common block-clearing content, whereas
$g_{\mathrm{rat}}$ is the gcd removed when the selected rational pair itself
is made primitive.  Formula (43) controls their product in the block
units.  A primitive-height argument needs (46), not merely a large value
of $s_1$ caused by (47).

## 9. What the critical computations do and do not establish

The accompanying certificate constructs the exact quartic coordinates at



$$
k=\operatorname {round}(n\log n)
$$



for a bounded set of even $n$.  It checks (1)--(3), (6), (29), (43) in
their divisibility form, and (47) exactly.  The observed quotient indices
and block contents are large, while the intrinsic selected contents
$g_{\mathrm{rat}}$ are usually very small in that bounded sample.

No asymptotic conclusion is drawn from those data.  In particular, this
note proves neither



$$
\log g_{\mathrm{rat}}(c^*)=o(k)
$$



nor an exponential counterexample for the canonical quartic direction.
It proves instead that:

1. the raw coefficient content is known exactly by (19);
2. its forced saturation divisor is known exactly by (23)--(26);
3. the whole endpoint quotient and both Smith invariants are known by
   determinant divisors through (6); and
4. the canonical endpoint obstruction is precisely the selected gcd in
   (43), after removing the block-clearing factor in (47).

This is the strongest clearing-independent arithmetic reduction obtained
here.  A subexponential bound for $g_{\mathrm{rat}}$ would require new local
information about $u_c$ modulo the prime powers dividing $T$; determinant
size or generic lattice geometry alone cannot supply it.

## 10. Reproducible certificate

Run

    python -m py_compile scripts/quartic_four_power_primitive_content_smith_certificate.py
    python scripts/quartic_four_power_primitive_content_smith_certificate.py

The certificate verifies the polynomial, kernel, scaling, Pluecker-minor,
and compressed-endpoint identities symbolically.  It then checks the
content and determinant-divisor conclusions with exact integer arithmetic
on deterministic matrices and on exact quartic-coordinate samples.  Its
JSON warnings mark every bounded quartic computation as diagnostic.

No README or research-log file is modified.
