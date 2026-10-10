> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Third exterior sums of root-of-unity remainders

## The corrected $3\times3$ endpoint jet, cubic dimension gain, and the surviving normalization barrier

Checked: 2026-08-27 UTC

## 1. Scope and verdict

Let $E_\nu$ be a reduced endpoint space and, for $C\in E_\nu$, let



$$
R_C(z)=C(z)+(1+e^z)T_C(z,e^z)=O(z^{L_\nu}),
 \qquad L_\nu=M+D+1-\nu,
 \qquad M=m(n+1).                                      \tag{1}
$$



This note studies a genuinely multilinear analytic object.  For an
arbitrary exterior vector



$$
p\in\bigwedge^3E_\nu,             \tag{2}
$$



define



$$
\mathcal W^{(3)}_p(z)=
 \sum_{i<j<k}p_{ijk}
 \det\begin{pmatrix}
 R_i&R_i'&R_i''\\
 R_j&R_j'&R_j''\\
 R_k&R_k'&R_k''
 \end{pmatrix}.                                           \tag{3}
$$



The sum in (3) need not be one determinant: $p$ is not assumed
decomposable.  This is distinct from the canonical divided-derivative
Wronskian of an endpoint subspace.  It is the analytic third exterior sum
of the remainders themselves, evaluated at the antiperiodic endpoint.

The exact conclusions are as follows.

1. There is a linear corrected endpoint map

   

$$
\Delta^{(3)}:\bigwedge^3E_\nu
                    \longrightarrow\mathbb Q[z]_{\le2n+D}, \tag{4}
$$



   including two different auxiliary-jet corrections, such that

   

$$
\mathcal W^{(3)}_p(i\pi)
                       =\Delta^{(3)}_p(i\pi).              \tag{5}
$$



2. Every such analytic sum has origin order at least $3L_\nu$, raw
   frequencies $0,\ldots,3m$, and polynomial coefficient degree at most
   $3n$.  Exact midpoint centering gives exponential type $3m/2$.
3. Killing all endpoint coefficients above fixed degree $d$ is a linear
   problem with

   

$$
N_3={\nu\choose3},\qquad S_3=2n+D-d.              \tag{6}
$$



   Thus the dimension loss can genuinely be reduced to
   $\nu=\Theta(n^{1/3})$.  As in the second exterior construction, a
   strict full-versus-tail rank gap is still necessary and sufficient;
   dimension counting alone does not prove nonzero output.
4. The integral normalization is less favorable than the raw analytic
   gain suggests.  If $Q=Q_{m,n}$ is the common remainder denominator,
   then $Q^2\Delta^{(3)}_p$ is integral while the cleared analytic sum is
   $Q^3\mathcal W^{(3)}_p$.  After primitive endpoint normalization, two
   powers of $Q$ remain in the presently proved analytic-height
   majorant.
5. The optimized analytic gain is $3\mathcal G_\nu^{\rm ctr}$, but the
   existing all-parameter inequality

   

$$
2\mathcal G_\nu^{\rm ctr}<\log Q \tag{7}
$$



   makes the content-free universal certificate strictly negative by at
   least one half-copy of $\log Q$, before slot factors.  In a hypothetical
   intrinsic matched-height model, the determinant height and the analytic
   gain both triple, so the admissible *per-column* height threshold is
   exactly the same as for $k=2$.

Consequently the cubic dimension reduction is real, but it is not by itself
an arithmetic improvement.  A large corrected content or an exceptional
intrinsic height collapse could still change the conclusion; neither is
proved here.  There is no irrationality or transcendence conclusion.

## 2. The exact endpoint jet

Put



$$
\beta_C(z)=T_C(z,-1),\qquad
 \theta_C(z)=(\partial_z-\partial_y)T_C(z,-1).             \tag{8}
$$



To avoid a common ambiguity, the first partial derivative in (8) holds
$y$ fixed.  Let



$$
U_C(z)=T_C(z,e^z),\qquad h(z)=1+e^z.          \tag{9}
$$



At $z_0=i\pi$,



$$
h(z_0)=0,\qquad h'(z_0)=h''(z_0)=-1,                    \tag{10}
$$



and the chain rule gives



$$
U_C'(z_0)
 =\{\partial_zT_C-\partial_yT_C\}(z_0,-1)
 =\theta_C(z_0).                                         \tag{11}
$$



Differentiating $R_C=C+hU_C$ zero, one, and two times therefore yields



$$
\boxed{
 \begin{aligned}
 R_C(z_0)&=C(z_0),\\
 R_C'(z_0)&=(C'-\beta_C)(z_0),\\
 R_C''(z_0)&=(C''-\beta_C-2\theta_C)(z_0).
 \end{aligned}}                                           \tag{12}
$$



For three endpoint directions, write the three entries of a column as
bold symbols, for example



$$
\mathbf C=(C_1,C_2,C_3)^t,
 \qquad\boldsymbol\beta=(\beta_{C_1},\beta_{C_2},\beta_{C_3})^t. \tag{13}
$$



The corrected endpoint polynomial is



$$
\boxed{
 \Delta^{(3)}(C_1,C_2,C_3)=
 \det(\mathbf C,\mathbf C'-\boldsymbol\beta,
       \mathbf C''-\boldsymbol\beta-2\boldsymbol\theta).} \tag{14}
$$



Expanding (14) displays every correction term explicitly:



$$
\begin{aligned}
 \Delta^{(3)}={}&W_3(C_1,C_2,C_3)
 -\det(\mathbf C,\boldsymbol\beta,\mathbf C'')
 -\det(\mathbf C,\mathbf C',\boldsymbol\beta)\\
 &-2\det(\mathbf C,\mathbf C',\boldsymbol\theta)
 +2\det(\mathbf C,\boldsymbol\beta,\boldsymbol\theta),  \tag{15}
\end{aligned}
$$



where $W_3(C_1,C_2,C_3)=\det(\mathbf C,\mathbf C',\mathbf C'')$.
Equations (12)--(15), followed by linearity in $p$, prove (5).

Since



$$
\deg C\le D,\qquad \deg\beta_C\le n,
 \qquad\deg\theta_C\le n,                               \tag{16}
$$



and $D\le n$, equation (14) proves the endpoint support bound



$$
\deg\Delta^{(3)}_p\le D+2n.      \tag{17}
$$



If $\Delta^{(3)}_p\ne0$, then (5) is nonzero: a nonzero rational
polynomial cannot vanish at the transcendental number $i\pi$.

## 3. The integer coefficient map and exact $Q$-normalization

The common denominator is



$$
Q=2^M\left(\prod_{a=0}^{n}a!\right)^m
   \prod_{h=1}^{m-1}h^{(m-h)(n+1)^2}.
$$



For an integral endpoint $C$, the common denominator theorem gives



$$
\overline T_C=QT_C\in\mathbb Z[z,y]. \tag{18}
$$



Consequently



$$
\overline\beta_C=Q\beta_C\in\mathbb Z[z],\qquad
 \overline\theta_C=Q\theta_C\in\mathbb Z[z].             \tag{19}
$$



Define the two integral corrected jet columns



$$
\begin{aligned}
 \mathsf A_C&=Q(C'-\beta_C)=QC'-\overline\beta_C,\\
 \mathsf B_C&=Q(C''-\beta_C-2\theta_C)
             =QC''-\overline\beta_C-2\overline\theta_C.
 \end{aligned}                                             \tag{20}
$$



For a saturated integral basis $C_1,\ldots,C_\nu$ and
$p\in\bigwedge^3\mathbb Z^\nu$, equations (14) and (20) give the exact
integer polynomial



$$
\boxed{
 N^{(3)}_{Q,p}:=Q^2\Delta^{(3)}_p
 =\sum_{i<j<k}p_{ijk}
   \det(\mathbf C_{ijk},\mathsf A_{ijk},\mathsf B_{ijk})
 \in\mathbb Z[z].}                                       \tag{21}
$$



This is also an explicit coefficient map.  If $e_a=z^a$ is the ambient
monomial basis, set



$$
A^Q_a=Qe_a'-Q\beta_{e_a},\qquad
 B^Q_a=Qe_a''-Q\beta_{e_a}-2Q\theta_{e_a}.                \tag{22}
$$



Then its ambient matrix is



$$
\boxed{
 (\mathcal A^{(3)}_Q)_{\ell,(u,v,w)}
 =[z^\ell]\det\begin{pmatrix}
 z^u&A^Q_u&B^Q_u\\
 z^v&A^Q_v&B^Q_v\\
 z^w&A^Q_w&B^Q_w
 \end{pmatrix},\quad u<v<w.}                             \tag{23}
$$



No denominator is hidden in (23).

Now put $\overline R_i=QR_i$.  Multilinearity gives



$$
\overline{\mathcal W}^{(3)}_p
 :=\sum_{i<j<k}p_{ijk}W_3(\overline R_i,\overline R_j,
                                      \overline R_k)
 =Q^3\mathcal W^{(3)}_p.                                 \tag{24}
$$



Combining (5), (21), and (24),



$$
\overline{\mathcal W}^{(3)}_p(i\pi)
      =Q\,N^{(3)}_{Q,p}(i\pi).                           \tag{25}
$$



Let



$$
c_p=\operatorname {cont}(N^{(3)}_{Q,p}),\qquad
 P_p=N^{(3)}_{Q,p}/c_p.                                  \tag{26}
$$



The intrinsic analytic normalization is therefore



$$
\boxed{
 F_p=\frac{\overline{\mathcal W}^{(3)}_p}{Qc_p},
 \qquad F_p(i\pi)=P_p(i\pi),
 \qquad H(F_p)=\frac{H(\overline{\mathcal W}^{(3)}_p)}{Qc_p}.} \tag{27}
$$



The divisor in (27) is $Qc_p$, not $Q^2c_p$.  This is the decisive
normalization fact: the analytic determinant has three cleared columns,
whereas the endpoint determinant has only two denominator-bearing jet
columns.

## 4. Origin order, frequency support, and centered type

For any $k$, multiplication of every input by a common scalar function
obeys



$$
W_k(hf_1,\ldots,hf_k)=h^kW_k(f_1,\ldots,f_k).            \tag{28}
$$



Indeed, the derivative columns are related by a triangular matrix whose
diagonal entries are all $h$.  Since $R_i=z^{L_\nu}f_i$ with $f_i$
analytic, (28) gives



$$
\boxed{
             \operatorname {ord}_0\mathcal W^{(3)}_p
                          \ge3L_\nu.}                     \tag{29}
$$



Cancellation in the sum can increase this order but cannot decrease it.

Every remainder has frequencies $0,\ldots,m$ and coefficient-polynomial
degree at most $n$.  Differentiation preserves both bounds, while a
product adds frequencies and degrees.  Hence



$$
\mathcal W^{(3)}_p(z)
   =\sum_{q=0}^{3m}A_q(z)e^{qz},
 \qquad\deg A_q\le3n.                                    \tag{30}
$$



The exact midpoint centering is



$$
\widetilde F_p(z)=e^{-3mz/2}F_p(z).                     \tag{31}
$$



It has frequency interval



$$
-\frac{3m}{2},\ldots,\frac{3m}{2} \tag{32}
$$



in unit steps.  Half-integral frequencies when $m$ is odd are harmless:
every term remains entire.  At the endpoint,



$$
\widetilde F_p(i\pi)=\zeta_mP_p(i\pi),
 \qquad \zeta_m=e^{-3mi\pi/2}\in\{\pm1,\pm i\}.         \tag{33}
$$



Thus the endpoint modulus is unchanged, although the exact phase is not
always rational.

If all exterior coordinates have the same endpoint-parity product
$\tau=\sigma_i\sigma_j\sigma_k$, the centered sum also has the exact
reflection parity



$$
\widetilde F_p(-z)=(-1)^{m+1}\tau
                                      \widetilde F_p(z).   \tag{34}
$$



To prove (34), use the half-centered remainder parity
$S_C(-z)=(-1)^m\sigma_CS_C(z)$, identity (28), and the derivative sign
$(-1)^{0+1+2}=-1$.  This can add one parity-forced origin zero in a
particular block, but it does not change the leading order or type.

For $\rho\ge1$, the elementary centered circle bound is



$$
\max_{|z|=\rho}|\widetilde F_p(z)|
 \le(3m+1)(3n+1)H(F_p)\rho^{3n}e^{(3m/2)\rho}.            \tag{35}
$$



Put



$$
A_\nu=L_\nu-n,
 \qquad
 \mathcal G_{\nu,\rm ctr}
 =A_\nu\log\frac{2A_\nu}{e\pi m}-n\log\pi.             \tag{36}
$$



Schwarz's lemma with the zero order $3L_\nu$ has the same stationary
radius as every exterior order:



$$
\rho_*=\frac{2A_\nu}{m}.       \tag{37}
$$



This is an admissible Schwarz radius throughout the endpoint range:
since $L_\nu\ge M=m(n+1)$,



$$
\rho_*\ge2+\frac{2n(m-1)}m\ge n+2>\pi.
$$



At that radius, equations (27), (29), and (35) give



$$
\boxed{
 -\log|P_p(i\pi)|
 \ge3\mathcal G_{\nu,\rm ctr}+\log Q+\log c_p
 -\log\{(3m+1)(3n+1)H(\overline{\mathcal W}^{(3)}_p)\}.} \tag{38}
$$



The factor three in (38) is a real analytic gain, not a heuristic.

## 5. Tail elimination and the exact rank-gap condition

Restrict the integer map (23) to $\bigwedge^3E_\nu$.  Fix a target
degree $d$.  Let $\mathcal T^{(3)}_{>d}$ contain the coefficient rows
$d+1,\ldots,2n+D$, and let $\mathcal T^{(3)}_{\rm all}$ contain all
rows.  Their domain dimension and the number of high rows are exactly



$$
N_3={\nu\choose3},\qquad
                    S_3=2n+D-d.                           \tag{39}
$$



If $N_3>S_3$, then the high-tail kernel is nonzero.  A usable nonzero
low-degree endpoint exists if and only if



$$
\boxed{
 \operatorname {rank}\mathcal T^{(3)}_{\rm all}
   >\operatorname {rank}\mathcal T^{(3)}_{>d}.}           \tag{40}
$$



The proof is exact: the tail rows are a subset of the full rows, and (40)
is equivalent to



$$
\ker\mathcal T^{(3)}_{>d}
      \not\subseteq\ker\mathcal T^{(3)}_{\rm all}.        \tag{41}
$$



There is no general rank-gap theorem in this note.

For fixed $d$, $D/n\to\delta\in[0,1]$, and a fixed oversampling factor
$\tau>1$, choosing $N_3\sim\tau S_3$ gives



$$
\boxed{
 \nu\sim\{6\tau(2+\delta)n\}^{1/3}.}                    \tag{42}
$$



Consequently



$$
L_\nu-n=(m-1+\delta)n-O(n^{1/3}).                       \tag{43}
$$



There is again a favorable full-endpoint specialization.  Put
$D=\nu-1$ and take the least $\nu$ satisfying



$$
{\nu\choose3}>2n+\nu-1-d.                  \tag{44}
$$



Then $E_\nu=\mathbb Q[z]_{\le D}$, its monomial basis has height one,
$\nu\sim(12n)^{1/3}$, and $L_\nu=M$.  Thus the cube-root dimension
gain is genuine and removes the endpoint-lattice basis cost in this
subfamily.

A nonzero decomposable three-vector has contraction-map rank exactly
three:



$$
E_\nu^*\longrightarrow\bigwedge^2E_\nu,qquad
 \lambda\longmapsto\iota_\lambda p.                      \tag{45}
$$



Therefore a contraction rank greater than three is an exact certificate
that the chosen sum is not a single $3\times3$ determinant.  This
sufficient test is used in the replay.

## 6. Height bounds and why the triple gain does not close the ledger

Let $H_E=\max_iH(C_i)$, and let $C_B$ be the existing universal
cleared interpolation bound



$$
H(QT_{C_i})\le C_BH_E.            \tag{46}
$$



Evaluation at $y=-1$ and the two derivatives in (8) give



$$
\begin{aligned}
 H(Q\beta_{C_i})&\le mC_BH_E,\\
 H(Q\theta_{C_i})
 &\le m\left(n+\frac{m-1}{2}\right)C_BH_E.
 \end{aligned}                                             \tag{47}
$$



Thus, with



$$
X_1=QD+mC_B,\qquad
 X_2=QD^2+m(2n+m)C_B,                                    \tag{48}
$$



equation (21) gives the elementary coefficient bound



$$
H(N^{(3)}_{Q,p})
 \le6{\nu\choose3}H(p)(n+1)^2H_E^3X_1X_2.               \tag{49}
$$



The factor $(n+1)^2$ bounds the number of degree convolutions in a
three-polynomial product; the six is the determinant expansion.

Similarly, if



$$
H_R=H_E(Q+2C_B),                 \tag{50}
$$



then differentiating once and twice costs at most $n+m$ and
$(n+m)^2$, respectively.  The two frequency and degree convolutions
give



$$
\boxed{
 H(\overline{\mathcal W}^{(3)}_p)
 \le \widehat H_3:=
 6{\nu\choose3}H(p)(m+1)^2(n+1)^2(n+m)^3H_R^3.}          \tag{51}
$$



These are universal upper bounds, not lower bounds for the intrinsic
heights.  Nevertheless, the *proved majorant* (51) contains three powers
of $Q$:



$$
\widehat H_3\ge Q^3.         \tag{52}
$$



Setting $\chi_p=\log c_p$, the content-free absolute exponent certified
by (38) and (51) satisfies



$$
\begin{aligned}
 u^{(3)}_{\rm univ}
 &:=3\mathcal G_{\nu,\rm ctr}+\log Q
   -\log\{(3m+1)(3n+1)\widehat H_3\}\\
 &\le3\mathcal G_{\nu,\rm ctr}-2\log Q
       -\log\{(3m+1)(3n+1)\}\\
 &<-\frac12\log Q-\log\{(3m+1)(3n+1)\}<0.              \tag{53}
\end{aligned}
$$



The strict penultimate inequality is exactly (7), proved independently in
the centered-frequency Schwarz correction note.  Thus the extra analytic
copy does not overcome the extra cleared denominator in the present
content-free universal ledger; it makes its denominator deficit stronger.

This is not an intrinsic impossibility theorem.  A large content $c_p$
or an analytic determinant much shorter than (51) could invalidate the
coarse comparison.  The exact required scale is as follows.  Suppose
temporarily that $s=e+\pi$ is algebraic of degree $r$, put



$$
d_p=\deg P_p,\qquad
 \kappa=r^2d_p+r-1,
 \qquad h_0=\log H(N^{(3)}_{Q,p}).                         \tag{54}
$$



The same polynomial $e$-measure used in the second exterior audit has
leading height exponent $\kappa$, because the endpoint is still one
rational polynomial of degree $d_p$.  Comparing it with (38) requires



$$
\boxed{
 (\kappa+1)\chi_p>
 \kappa h_0+
 \log\{(3m+1)(3n+1)H(\overline{\mathcal W}^{(3)}_p)\}
 -3\mathcal G_{\nu,\rm ctr}-\log Q,}                     \tag{55}
$$



up to the same explicit finite field and substitution constants as before.

In an intrinsically normalized formulation, suppose



$$
\begin{aligned}
 \log H(F_p)&=a\,n\log n+o(n\log n),\\
 \log H(P_p)&=b\,n\log n+o(n\log n).
 \end{aligned}                                             \tag{56}
$$



For fixed $m$, fixed $d_p$, and $D/n\to\delta$, the sharp leading
conditional requirement is



$$
\boxed{a+\kappa b<3(m-1+\delta).}                        \tag{57}
$$



If one intrinsically normalized column has height exponent $\lambda$,
and both the analytic determinant and primitive endpoint have their
natural cubic matched scale $a=b=3\lambda$, then (57) becomes



$$
\boxed{
 \lambda<\frac{m-1+\delta}{\kappa+1}
          =\frac{m-1+\delta}{r^2d_p+r}.}                  \tag{58}
$$



This is exactly the matched per-column threshold obtained for $k=2$.
The factor three in analytic gain is canceled by the factor three in
multilinear height and in the algebraic-height payment.  Thus the
cube-root endpoint dimension can help only if it also lowers the actual
per-column intrinsic height, produces exceptional content, or creates a
sub-cubic determinant-height collapse.

Finally, the present Cramer bound remains far outside (56).  For fixed
$m$,



$$
\log C_B=mn^2\log n+O_m(n^2),     \tag{59}
$$



and (49)--(51) contain two and three copies of that scale, whereas
$3\mathcal G_{\nu,\rm ctr}=O(n\log n)$.  Passing from square-root to
cube-root endpoint dimension does not repair this factor-$n$ arithmetic
gap.

## 7. Exact finite diagnostics

The replay checks four small rows at target degree $d=2$:



$$
\begin{array}{c|c|c|c|c|c|c|c|c}
m&n&D&\nu&\#\text{ constraints}&N_3&S_3&
 \operatorname {rank}_{\rm all}&\operatorname {rank}_{>2}\\ \hline
2&5&5&6&0&20&13&16&13\\
3&5&5&6&0&20&13&16&13\\
2&6&6&6&1&20&16&19&16\\
3&6&6&6&1&20&16&19&16
\end{array}                                                \tag{60}
$$



Thus every displayed rank gap is three.  The last two rows are properly
reduced endpoint spaces, not full endpoint spaces.  In every row the
selected tail-kernel vector has contraction rank six, the primitive output
has exact degree two, both extreme raw frequencies $0,3m$ survive, and
the origin order is at least $3L_\nu$.  The selected coordinate-height
digit counts are



$$
29,\ 57,\ 41,\ 67,               \tag{61}
$$



and the primitive quadratic-height digit counts are



$$
25,\ 50,\ 31,\ 56.               \tag{62}
$$



These large tiny-case values are arithmetic warnings, not asymptotic lower
bounds.  The rank gaps in (60) are finite diagnostics only and are not
promoted to an all-parameter theorem.

For each row, the replay independently performs both endpoint evaluations:

1. substitute $e^z=-1$ after constructing the complete analytic
   $3\times3$ determinant; and
2. use the corrected jet determinant (14).

It verifies exact equality, $Q^2$-integrality of (21), $Q^3$-integrality
of (24), the normalization (25)--(27), complete origin jets, frequency and
degree support, saturated endpoint bases, and nondecomposability by (45).

## 8. Replay and logical scope

The package consists of

* sources/root_unity_third_exterior_sum_endpoint_audit.md;
* scripts/root_unity_third_exterior_sum_certificate.py;
* results/root_unity_third_exterior_sum_certificate.json; and
* results/root_unity_third_exterior_sum_hashes.sha256.

Replay from the archive root with

    python3 scripts/root_unity_third_exterior_sum_certificate.py

The all-parameter statements are equations (12), (14), (17), (21),
(27), (29)--(30), (35), (38), (40), (42), and (53)--(58).  They are
proved above and are not inferred from the finite grid.  The replay is
deterministic and asserts a resident-memory ceiling of $2$ GiB.

This audit does **not** prove:

1. an all-parameter rank gap;
2. a useful lower bound for the corrected content;
3. an intrinsic $O(n\log n)$-scale height theorem;
4. that the natural matched cubic-height model is sharp in either
   direction; or
5. any conclusion about the arithmetic nature of $e+\pi$.
