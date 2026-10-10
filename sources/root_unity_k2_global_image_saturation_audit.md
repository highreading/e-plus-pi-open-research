> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Saturating the global $k=2$ Wronskian image after endpoint-tail cancellation

## Exact HNF/Smith formulas, covolume collapse, and finite $O(n\log n)$-scale evidence

Checked: 2026-08-27 UTC

## 1. Scope and verdict

This note isolates an arithmetic normalization that is invisible if one
looks only at the size of exterior coordinates.  Take the minimal full
endpoint space



$$
E=\mathbb Q[z]_{\le D},\qquad \nu=D+1,
$$



and let $K$ be a saturated integral basis of the exterior-coordinate
kernel which kills every corrected endpoint coefficient above a fixed
target degree $d$.  Map every column of $K$ to the **complete** cleared
Wronskian coefficient vector, including all frequencies and polynomial
degrees.  The resulting rows form an integral lattice



$$
L_{\rm raw}\subseteq\mathbb Z^P,\qquad
 P=(2m+1)(2n+1).
$$



Its intrinsic rational saturation is



$$
L_{\rm sat}
 =\operatorname {span}_{\mathbb Q}(L_{\rm raw})\cap\mathbb Z^P.
$$



There are four exact conclusions.

1. A single tall Hermite normal form gives an explicit basis of
   $L_{\rm sat}$, the exact index
   $[L_{\rm sat}:L_{\rm raw}]$, and an exact change-of-basis
   factorization.
2. The same index is the product of the nonzero Smith invariants and the
   gcd of all maximal minors.  It is also exactly the ratio of the raw and
   saturated Euclidean covolumes.
3. If $g$ is the common content of all entries of a raw row basis, then

   

$$
[L_{\rm sat}:L_{\rm raw}]
                  =g^r I_{\rm cross},                    \tag{1}
$$



   where $r=\operatorname {rank}L_{\rm raw}$ and $I_{\rm cross}$ is
   the residual Smith index.  Thus a large scalar content contributes
   $g$ once per image dimension, while non-scalar cross-content is
   measured separately.
4. The saturation is independent of the size or conditioning of the
   chosen tail-kernel basis and is unchanged by any nonzero global scalar
   clearing.  Hence huge exterior coordinates and a $Q^2$-scale cleared
   global map do **not** force equally huge primitive global coefficient
   vectors.

On the exact representative grid



$$
m\in\{2,3\},\qquad n\in\{2,3,5,8,10\},\qquad d=2,
$$



the common scalar factor accounts for between
$96.3970\%$ and $100\%$ of the logarithmic saturation index.  For
$n\ge3$, the logarithm of the shortest row in the saturated LLL basis,
divided by $n\log n$, lies between
$2.63$ and $3.74$ for $m=2$, and between $4.71$ and $6.12$ for
$m=3$.  This is finite evidence consistent with an intrinsic
$O(n\log n)$-scale global image, despite much larger raw coordinates and
raw global vectors.

It is **not** an asymptotic theorem.  The generic HNF identities do not
bound the Pluecker height of the rational global image subspace, and no
uniform formula for the Smith invariants is proved.  LLL vectors are
certified lattice vectors but not shortest-vector certificates.  A short
global vector can also have zero corrected low endpoint.  No conclusion
about $e+\pi$ follows.

## 2. The exact global image lattice

Let



$$
N={\nu\choose2}
$$



be the exterior-coordinate dimension.  For the full monomial endpoint
basis, let



$$
\overline R_a=Q R_{z^a},\qquad 0\le a\le D,
$$



be the cleared remainders.  Flatten the coefficient array of



$$
W(\overline R_a,\overline R_b)
 =\sum_{q=0}^{2m}\sum_{k=0}^{2n}
     G_{(a,b),(q,k)}z^ke^{qz}
$$



in frequency-major order.  This defines the integer global coefficient
matrix



$$
G\in\mathbb Z^{N\times P},
 \qquad P=(2m+1)(2n+1).                                  \tag{2}
$$



Let



$$
T_{>d}\in\mathbb Z^{S\times N}
$$



be a row-primitive clearing of the corrected endpoint tail map, and let



$$
K\in\mathbb Z^{N\times t},\qquad
 K\mathbb Z^t=\ker(T_{>d})\cap\mathbb Z^N,                \tag{3}
$$



be a saturated kernel basis.  With row-vector convention, the raw global
image matrix is



$$
B=K^tG\in\mathbb Z^{t\times P}.  \tag{4}
$$



If $B$ has rank $r$, discard zero rows after a unimodular row HNF and
write the resulting row basis as



$$
R\in\mathbb Z^{r\times P}.       \tag{5}
$$



Then



$$
\begin{aligned}
 L_{\rm raw}&=\operatorname {row}_{\mathbb Z}(R),\\
 L_{\rm sat}&=\operatorname {row}_{\mathbb Q}(R)
                         \cap\mathbb Z^P.                 \tag{6}
 \end{aligned}
$$



The more conceptual form of the second line is



$$
\boxed{
 L_{\rm sat}
 =G\!\left(\ker_{\mathbb Q}T_{>d}\right)\cap\mathbb Z^P.} \tag{7}
$$



Equation (7) is independent of every choice of basis for the rational
tail kernel.

Endpoint evaluation is the integral map



$$
{\cal E}:\mathbb Z^P\longrightarrow\mathbb Z^{2n+1},
 \qquad
 {\cal E}(v)_k=\sum_{q=0}^{2m}(-1)^qv_{q,k}.              \tag{8}
$$



To track the normalization exactly, let $N$ denote the unprimitivized
integer corrected-endpoint map $x\mapsto Q\Delta_x$.  Row
primitivization does not change its tail kernel, and the complete cleared
Wronskian map obeys



$$
\ker_{\mathbb Q}T_{>d}=\ker_{\mathbb Q}N_{>d},
             \qquad {\cal E}(Gx)=Q\,Nx.
$$



Indeed $Gx$ is the coefficient array of
$W(QR_a,QR_b)=Q^2W(R_a,R_b)$, whereas $Nx=Q\Delta_x$.
Every $v\in L_{\rm sat}$ lies in the rational image of the tail kernel.
Therefore



$$
{\cal E}(v)_k=0\quad(k>d).       \tag{9}
$$



Thus saturation preserves the endpoint-tail cancellation exactly, even
though a saturated global vector can require a rational, rather than
integral, exterior preimage.

## 3. The tall-HNF saturation theorem

The following elementary lattice theorem is the structural core.

> **Theorem 3.1.** Let $R\in\mathbb Z^{r\times P}$ have full row rank
> $r$.  Compute a row Hermite normal form of its transpose with
> transformation:
>
> 

$$
>  H=UR^t=
>  \begin{pmatrix}H_0\\0\end{pmatrix},\qquad
>  U\in\operatorname {GL}_P(\mathbb Z),                  \tag{10}
>
$$


>
> where $H_0\in\mathbb Z^{r\times r}$ is nonsingular.  Let
>
> 

$$
>  S=\left(U^{-1}_{[:,\,0:r]}\right)^t\in\mathbb Z^{r\times P}.
>                                                                    \tag{11}
>
$$


>
> Then the rows of $S$ form a basis of
> $\operatorname {row}_{\mathbb Q}(R)\cap\mathbb Z^P$, and
>
> 

$$
>  \boxed{
>  R=H_0^tS,\qquad
>  [L_{\rm sat}:L_{\rm raw}]=|\det H_0|.}                \tag{12}
>
$$



**Proof.**  The unimodular map $U$ sends the rational column span of
$R^t$ to the first $r$ coordinate axes because $H_0$ is invertible
over $\mathbb Q$.  The integer saturation of that coordinate subspace is
exactly



$$
\mathbb Z^r\times0^{P-r}.        \tag{13}
$$



Pulling the standard basis in (13) back by $U^{-1}$ gives the columns
of $S^t$, proving the saturation assertion.  Multiplying (10) by
$U^{-1}$ gives



$$
R^t=U^{-1}
 \begin{pmatrix}H_0\\0\end{pmatrix}=S^tH_0,
$$



which is the first identity in (12).  The coefficient matrix from the
saturated basis $S$ to the raw basis $R$ is $H_0^t$, so its
determinant gives the index. $\square$

The theorem is constructive and does not enumerate minors.  It also gives
an exact saturation certificate: the tall HNF of $S^t$ is



$$
\begin{pmatrix}I_r\\0\end{pmatrix}. \tag{14}
$$



## 4. Smith invariants, maximal minors, and common content

Let



$$
d_1\mid d_2\mid\cdots\mid d_r    \tag{15}
$$



be the nonzero Smith invariants of $R$.  The standard determinantal
divisor theorem and Theorem 3.1 give



$$
\boxed{
 [L_{\rm sat}:L_{\rm raw}]
 =\prod_{j=1}^r d_j
 =\gcd\{|\det R_I|:I\subseteq\{1,\ldots,P\},\ |I|=r\}
 =|\det H_0|.}                                           \tag{16}
$$



The first Smith invariant is exactly the common entry content



$$
g=\gcd_{i,j}R_{i,j}=d_1.         \tag{17}
$$



Because $d_1\mid d_j$, write



$$
d_j=g e_j,\qquad e_1=1.          \tag{18}
$$



Then



$$
\boxed{
 [L_{\rm sat}:L_{\rm raw}]
 =g^r\prod_{j=1}^r e_j.}                                 \tag{19}
$$



The scalar term $g^r$ and residual cross-index



$$
I_{\rm cross}=\prod e_j          \tag{20}
$$



are exact, basis-independent invariants of the raw lattice.  Factoring



$$
R=gR_{\rm prim}                  \tag{21}
$$



does not change $L_{\rm sat}$, while it divides the raw index by $g^r$.

More generally, for every nonzero integer $c$,



$$
\boxed{
 \operatorname {Sat}(cL_{\rm raw})
 =\operatorname {Sat}(L_{\rm raw}),\qquad
 [L_{\rm sat}:cL_{\rm raw}]
 =|c|^r[L_{\rm sat}:L_{\rm raw}].}                       \tag{22}
$$



This scaling identity explains why the $Q^2$ clearing in the complete
Wronskian matrix does not itself impose a $Q^2$-scale primitive global
height.  Saturation remembers the rational row space, not its scalar
presentation.

If $g_G$ is the common content of the full pair map $G$, then every
entry of $K^tG$ is divisible by $g_G$.  Hence



$$
g_G\mid g,\qquad
 [L_{\rm sat}:L_{\rm raw}]\ge g_G^r.                     \tag{23}
$$



This is a uniform exact divisibility statement.  The replay also finds
$g\mid Q^2$ in every displayed row and records the quotient $Q^2/g$.
That latter pattern is finite evidence only; no all-parameter divisibility
formula is asserted.

For completeness, if $H=\max|R_{ij}|$, Hadamard's inequality gives the
generic upper bound



$$
1\le [L_{\rm sat}:L_{\rm raw}]
 \le r^{r/2}H^r.                                         \tag{24}
$$



It is far too coarse to establish an intrinsic $O(n\log n)$ height
theorem.

## 5. Gram covolumes and root determinants

Give the rational row space its induced Euclidean metric.  For any row
basis $A$, define



$$
\operatorname {covol}(A)=\sqrt{\det(AA^t)},\qquad
 \operatorname {rd}(A)=\operatorname {covol}(A)^{1/r}.   \tag{25}
$$



Equation (12) implies



$$
RR^t=H_0^t(SS^t)H_0.
$$



Therefore



$$
\boxed{
 \det(RR^t)
 =[L_{\rm sat}:L_{\rm raw}]^2\det(SS^t),\qquad
 \frac{\operatorname {covol}(R)}
      {\operatorname {covol}(S)}
 =[L_{\rm sat}:L_{\rm raw}].}                            \tag{26}
$$



The root-determinant logarithms differ by



$$
\log\operatorname {rd}(R)-\log\operatorname {rd}(S)
 =\frac1r\log[L_{\rm sat}:L_{\rm raw}].                  \tag{27}
$$



The replay verifies (26) as an exact integer identity, not through
floating-point determinants.

## 6. Why huge exterior coordinates need not force huge global vectors

There are two separate coordinate artifacts.

First, the columns of $K$ can be very large because they are an integral
basis of a rational kernel cut out by a high-height endpoint-tail matrix.
But equation (7) depends only on
$\ker_{\mathbb Q}T_{>d}$, not on the norm of that basis.  Replacing
$K$ by $KV$, $V\in\operatorname {GL}_t(\mathbb Z)$, leaves even the
raw lattice unchanged; replacing it by any rational basis leaves the
saturation unchanged.

Second, the global image $K^tG$ has large scalar and cross-content.
Equation (19) divides those factors intrinsically.  A vector in
$L_{\rm sat}$ is an integral complete Wronskian coefficient vector with
a rational tail-kernel preimage.  It is therefore the correct object for
an intrinsically scaled exterior construction.

This does **not** say that every saturated vector has a useful endpoint.
The low endpoint map



$$
L_{\rm sat}\longrightarrow\mathbb Z^{d+1}               \tag{28}
$$



can have a kernel.  A proof construction still needs a short saturated
vector outside that kernel, control of the primitive endpoint height, and
the analytic small-value inequality.

## 7. Exact representative grid

The replay uses the least full endpoint degree $D$ satisfying



$$
{D+1\choose2}>n+D-2              \tag{29}
$$



for each sampled $n$.  The main lattice statistics are:



$$
\begin{array}{cc|c|c|r|c|r|r|r}
m&n&D&r&
\#\text{ index digits}&
\dfrac{r\log g}{\log I}&
\log\lambda_{\rm raw}^{\rm LLL}&
\log\lambda_{\rm sat}^{\rm LLL}&
\dfrac{\log\lambda_{\rm sat}^{\rm LLL}}{n\log n}\\ \hline
2&2 &2&1&4  &1.0000&13.252&5.627 &4.059\\
2&3 &3&2&17 &0.9640&29.184&9.824 &2.981\\
2&5 &4&3&72 &0.9715&75.792&21.201&2.635\\
2&8 &5&4&276&0.9829&205.205&46.500&2.795\\
2&10&5&3&351&0.9894&355.643&86.037&3.737\\
3&2 &2&1&10 &1.0000&35.236&12.362&8.917\\
3&3 &3&2&45 &0.9728&68.294&18.034&5.472\\
3&5 &4&3&173&0.9679&171.895&39.470&4.905\\
3&8 &5&4&618&0.9770&433.654&78.470&4.717\\
3&10&5&3&758&0.9901&722.800&140.857&6.117
\end{array}                                               \tag{30}
$$



Here $I=[L_{\rm sat}:L_{\rm raw}]$, and
$\lambda^{\rm LLL}$ denotes the minimum Euclidean norm among the rows of
the corresponding LLL-reduced basis.  It is an explicit lattice-vector
upper bound for the first successive minimum, not a proof of the shortest
vector.

The residual Smith invariants after removing the common scalar $g$ are



$$
\begin{array}{cc|l}
m&n&(e_1,\ldots,e_r)\\ \hline
2&2 &(1)\\
2&3 &(1,4)\\
2&5 &(1,2,54)\\
2&8 &(1,1,21,2520)\\
2&10&(1,30,180)\\
3&2 &(1)\\
3&3 &(1,16)\\
3&5 &(1,20,17280)\\
3&8 &(1,128,20736,62705664)\\
3&10&(1,32,933120).
\end{array}                                               \tag{31}
$$



Thus almost all logarithmic index comes from one common scalar repeated
in every image dimension; the residual cross-index is real but much
smaller on this grid.

The normalized saturated LLL and root-determinant scales stay bounded by
small constants times $n\log n$ on the sampled rows.  In contrast, the
raw LLL logs grow from $29.18$ to $355.64$ for $m=2$, and from
$68.29$ to $722.80$ for $m=3$, between $n=3$ and $n=10$.
This is exact finite evidence for the proposed saturation mechanism.

It is not legitimate to infer an asymptotic $O(n\log n)$ theorem from
(30).  A proof would require an all-parameter bound for a primitive
Pluecker coordinate of the rational subspace
$G(\ker_{\mathbb Q}T_{>d})$, or an explicit network/recurrence basis for
its saturation.  The generic determinant bounds still live on the
previous $n^2\log n$ scale.

## 8. Replay and logical scope

The package consists of:

* sources/root_unity_k2_global_image_saturation_audit.md;
* scripts/root_unity_k2_global_image_saturation_certificate.py;
* results/root_unity_k2_global_image_saturation_certificate.json; and
* results/root_unity_k2_global_image_saturation_hashes.sha256.

The replay imports the already audited interpolation and Wronskian
constructors from
scripts/root_unity_nondecomposable_exterior_sum_certificate.py and records
that dependency's SHA-256 digest.

Replay from the archive root with

    python3 scripts/root_unity_k2_global_image_saturation_certificate.py

For every row, it:

1. reconstructs the minimal full endpoint space and saturated tail kernel;
2. constructs every complete cleared pairwise Wronskian coefficient row;
3. forms $B=K^tG$;
4. verifies the tall-HNF factorization (12);
5. computes the complete Smith invariant list and exact index;
6. verifies the exact Gram determinant identity (26);
7. LLL-reduces both the raw and saturated lattices; and
8. verifies that endpoint evaluation of every saturated basis row has no
   coefficient above degree two.

The run asserts a per-process resident-memory ceiling of $2$ GiB.  The
all-parameter statements are the lattice identities (7), (12), (16),
(19), (22), (23), and (26), not the finite growth pattern in (30).

This audit proves no all-parameter formula for the Smith invariants, no
$O(n\log n)$ bound for a saturated successive minimum, no guarantee that
the shortest global vector has nonzero low endpoint, and no irrationality
or transcendence result.
