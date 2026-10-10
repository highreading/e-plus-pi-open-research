> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Full Galois balancing of the fixed two-log unit edge

Date: 2026-08-27.

## 1. Scope and conclusion

Temporarily assume



$$
s=e+\pi\in\overline{\mathbb Q},\qquad K=\mathbb Q(s),
\qquad h=[K:\mathbb Q].                                      \tag{1}
$$



This note completes the Galois audit of the fixed-root, two-log unit form
on the edge $c=f=0$ of the corrected Rivoal construction.  Choose an odd
prime $n\ge5$ which is unramified in $K$, put



$$
\xi=\zeta_n,\qquad x_k={1\over1+\xi^k},\qquad
y_k=1-x_k,
\qquad \rho_k=|x_k|={1\over2\cos(\pi k/n)},                 \tag{2}
$$



where each reduced residue $k$ is represented in $(-n/2,n/2)$, and
let $L=\mathbb Q(\xi,i)$.  For the paired form



$$
\Lambda_{n,d}=U_ds+V_d                                      \tag{3}
$$



the complete absolute norm has the two-sided asymptotic



$$
\boxed{
|N_{KL/\mathbb Q}(\Lambda_{n,d})|
\asymp_{K,n}
\left[\rho_1^2
 \left(\prod_{\rho_k>1}\rho_k^2\right)^h\right]^d
d^{-2(1+h|\{k:\rho_k>1\}|)}.}                              \tag{4}
$$



The exponential base in (4) is strictly greater than one.  Thus the full
absolute norm grows, and every positive rational integrality clearing only
increases it.  Multiplying the two locally small complex-conjugate factors
first merely changes the order of norm-taking and gives the same result.

The two most natural linear and exterior symmetrizations also fail:

* the ordinary coefficient-field trace is identically zero;
* the natural nonzero real trace reduces, after primitive projective
  normalization, to the elementary exponential partial-sum form;
* a two-fold exterior determinant eliminates $s$, and every exterior
  determinant of order at least three vanishes.

This is an unconditional no-go theorem *under the temporary algebraicity
hypothesis* for this particular auxiliary construction.  It is not a
contradiction to (1), and it does not classify $e+\pi$.  Varying
$n,c,d,f$, adding genuinely different logarithmic orbits, or proving a
new exponentially large coordinate-content ideal lies outside its scope.

## 2. The exact form and the endpoint estimates

On $c=f=0$, write $A_d,B_d,E_d$ for the reversed Rivoal
polynomials and



$$
R_{\exp,d}(z)=A_d(z)e^z-E_d(z),\qquad
R_{\log,d}(z)=A_d(z)\operatorname {Log}(1-z)-B_d(z).       \tag{5}
$$



The exact paired form at $x=x_1,y=y_1$ is



$$
\begin{aligned}
\Lambda_{n,d}={}&
2iA_d(x)A_d(y)R_{\exp,d}(1)\\
&+nA_d(1)\{A_d(y)R_{\log,d}(x)
              -A_d(x)R_{\log,d}(y)\}                    \tag{6}\\
={}&2iA_d(1)A_d(x)A_d(y)s
-2iA_d(x)A_d(y)E_d(1)\\
&-nA_d(1)A_d(y)B_d(x)+nA_d(1)A_d(x)B_d(y).
\end{aligned}
$$



The accepted endpoint analysis gives, uniformly on the fixed cyclotomic
orbit,



$$
A_d(z)=(-1)^d\left(e^{-z}
 +O_z\left({|z|^{d+1}\over(d+1)!}\right)\right),           \tag{7}
$$



and, with



$$
D_{d,k}=A_d(y_k)R_{\log,d}(x_k)
        -A_d(x_k)R_{\log,d}(y_k),                         \tag{8}
$$





$$
|D_{d,k}|\asymp_n{\rho_k^d\over d}.                       \tag{9}
$$



The leading sine in the endpoint expansion is bounded away from zero as
$d$ varies, so (9) is genuinely two-sided and also gives eventual
nonvanishing.  Moreover,



$$
A_d(1)A_d(x_k)A_d(y_k)=(-1)^de^{-2}+o_n(1).                \tag{10}
$$



## 3. A disjoint coefficient field always exists

Choose the odd prime $n$ so that



$$
n\nmid\operatorname {disc}(K).                            \tag{11}
$$



Then



$$
K\cap L=\mathbb Q.                                       \tag{12}
$$



Indeed, the intersection is a subfield of the abelian Galois extension
$L/\mathbb Q$, and hence is Galois and abelian over $\mathbb Q$.
Because $K=\mathbb Q(s)$ is embedded in $\mathbb R$, the intersection
is real.  At $n$, the inertia group in
$\mathbb Q(\zeta_n,i)/\mathbb Q$ fixes exactly $\mathbb Q(i)$.
Consequently every nontrivial real subfield of $L$ is ramified at
$n$.  Such a field cannot be contained in the $n$-unramified field
$K$, proving (12).

Since $L/\mathbb Q$ is Galois, (12) gives linear disjointness.  The
embeddings of $KL$ may therefore be indexed independently by



$$
s\mapsto s_j,\qquad \xi\mapsto\xi^k,qquad
i\mapsto\epsilon i,                                      \tag{13}
$$



where $0\le j<h$, $s_0=s$, $(k,n)=1$, and
$\epsilon\in\{1,-1\}$.

## 4. Every target conjugate and every coefficient branch

Put



$$
P_{d,k}=A_d(x_k)A_d(y_k),\qquad
D^B_{d,k}=A_d(y_k)B_d(x_k)-A_d(x_k)B_d(y_k),               \tag{14}
$$



and define the affine form



$$
\lambda_{k,\epsilon,d}(t)
=2\epsilon iA_d(1)P_{d,k}t
-2\epsilon iP_{d,k}E_d(1)-nA_d(1)D^B_{d,k}.               \tag{15}
$$



The conjugates of (3) are exactly
$\lambda_{k,\epsilon,d}(s_j)$.  At the distinguished target,
continuing the logarithms on their prescribed branches gives



$$
\lambda_{k,\epsilon,d}(s)
=\widetilde\lambda_{k,\epsilon,d}
+2i(\epsilon-k)\pi A_d(1)P_{d,k},                         \tag{16}
$$



where



$$
|\widetilde\lambda_{k,\epsilon,d}|
\asymp_n{\rho_k^d\over d}.                               \tag{17}
$$



For every conjugate of the target there is also the exact affine identity



$$
\lambda_{k,\epsilon,d}(s_j)
=\lambda_{k,\epsilon,d}(s)
+2\epsilon iA_d(1)P_{d,k}(s_j-s).                         \tag{18}
$$



If $\rho_k<1$ and $j\ne0$, equations (10), (16), and (18) give



$$
\lambda_{k,\epsilon,d}(s_j)
=2i(-1)^de^{-2}
\{\epsilon(s_j-s)+(\epsilon-k)\pi\}+o_{K,n}(1).          \tag{19}
$$



The bracket cannot vanish.  If $k\ne\epsilon$, its vanishing would
make the algebraic number $s_j-s$ a nonzero rational multiple of the
transcendental number $\pi$.  If $k=\epsilon$, it would say
$s_j=s$, impossible for a distinct embedding of the primitive
generator.

For $j=0$, the correction in (16) vanishes exactly at



$$
(k,\epsilon)=(1,1),\qquad(-1,-1).                         \tag{20}
$$



These are the two locally small factors, each of size
$\asymp_n\rho_1^d/d$.  Every other small-$\rho$ factor tends to a
nonzero constant.  If $\rho_k>1$, (17) dominates the fixed correction
in (18), uniformly over the finite target orbit, and



$$
|\lambda_{k,\epsilon,d}(s_j)|
\asymp_{K,n}{\rho_k^d\over d}.                            \tag{21}
$$



Multiplying (19)--(21) proves (4).

## 5. Strict growth of the norm

Let



$$
P_{\mathcal T}=\prod_{\rho_k>1}\rho_k.
$$



The earlier relative-norm calculation proves



$$
B_n=\rho_1^2P_{\mathcal T}^2>1.                           \tag{22}
$$



Since $P_{\mathcal T}>1$, the base in (4) is



$$
\rho_1^2P_{\mathcal T}^{2h}
=B_nP_{\mathcal T}^{2(h-1)}>1.                           \tag{23}
$$



If $\delta s$ is integral and $q_d$ is any positive rational
coefficient clearing, then



$$
X_{n,d}=\delta q_d\Lambda_{n,d}\in\mathcal O_{KL}
$$



and



$$
|N_{KL/\mathbb Q}(X_{n,d})|
=(\delta q_d)^{2\varphi(n)h}
 |N_{KL/\mathbb Q}(\Lambda_{n,d})|\longrightarrow\infty. \tag{24}
$$



For $n=5$, when $5\nmid\operatorname {disc}(K)$,
$\rho_{\pm1}=\varphi^{-1}$, $\rho_{\pm2}=\varphi$, and



$$
\boxed{
|N_{K\mathbb Q(\zeta_5,i)/\mathbb Q}(\Lambda_{5,d})|
\asymp_K\varphi^{(4h-2)d}d^{-(4h+2)}.}                   \tag{25}
$$



In particular, target conjugates worsen rather than improve the
coefficient-field obstruction.

## 6. Trace and exterior symmetrizations

Summing (15) over $\epsilon=\pm1$ cancels the two terms carrying
$\epsilon i$.  The remaining term is odd under $k\mapsto-k$, since
$D^B_{d,-k}=-D^B_{d,k}$.  Hence



$$
\boxed{\operatorname {Tr}_{KL/K}(\Lambda_{n,d})=0.}       \tag{26}
$$



Multiplication by $-i$ gives the natural nonzero trace.  Put



$$
R_{n,d}=\sum_{(k,n)=1}A_d(x_k)A_d(y_k)\in\mathbb Q.
$$



Then exact summation gives



$$
\boxed{
\operatorname {Tr}_{KL/K}(-i\Lambda_{n,d})
=4R_{n,d}\{A_d(1)s-E_d(1)\}.}                            \tag{27}
$$



Here $R_{n,d}\to\varphi(n)/e$,
$E_d(1)=(-1)^d$, and



$$
A_d(1)=(-1)^d\sum_{j=0}^d{(-1)^j\over j!}.               \tag{28}
$$



The rational trace factor in (27) is common to both coordinates and
disappears under primitive normalization.  If the reduced partial sum in
(28) is $p_d/q_d$, the remaining primitive direction is



$$
p_ds-q_d.                                                 \tag{29}
$$



Since $p_d/q_d\to e^{-1}$, every conjugate satisfies



$$
p_ds_j-q_d\sim q_d(s_j/e-1),                              \tag{30}
$$



and the norm of (29) diverges.  Thus this trace has discarded the
logarithmic gain.

Finally, every coefficient conjugate is affine in the same variable,
$\lambda_\sigma(t)=U_\sigma t+V_\sigma$.  Therefore



$$
\det\begin{pmatrix}U_\sigma&\lambda_\sigma(s)\\
                    U_\tau&\lambda_\tau(s)
    \end{pmatrix}
=U_\sigma V_\tau-U_\tau V_\sigma                         \tag{31}
$$



is independent of $s$.  The family has affine rank at most two, so every
exterior determinant of order at least three vanishes.  Exterior powers
therefore either eliminate the target or are zero; products retain it but
are governed by (4).

## 7. Exact boundary of the result

Equations (4), (24), and (26)--(31) exclude the natural fixed-$n$,
$c=f=0$ trace, norm, local-pair product, and exterior constructions.
They do not bound a common coordinate ideal by which one might subsequently
divide; such a division requires an independent all-degree content theorem.
They also do not analyze varying $n$ or nonzero $c,f$.  No conclusion
about the algebraicity or transcendence of $e+\pi$ is claimed.

