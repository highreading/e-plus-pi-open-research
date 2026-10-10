> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A normalized global lift for the balanced centered-cosh quadratic

## A direct Padé basis, exact division by the two-border content, and an $O(q^2)$ height bound

Checked: 2026-08-27 UTC

## 1. Statement

Put



$$
F(x)=\frac1{2\cosh\sqrt x},\qquad n=3q+1,qquad q\geq2,
 \qquad {\cal P}_d=\mathbb Q[x]_{\leq d}.                 \tag{1}
$$



Let $(Q,P)$ and $(G,R)$ be respectively the normal Padé pairs of
types $[q/q]$ and $[q+1/q-1]$, normalized by



$$
Q(0)=G(0)=1.                                             \tag{2}
$$



Thus



$$
FQ-P=O(x^{2q+1}),\qquad FG-R=O(x^{2q+1}),                \tag{3}
$$



and the adjacent cross identity is



$$
RQ-PG=\kappa x^{2q+1},\qquad \kappa\ne0.                \tag{4}
$$



Let ${\cal U}_{q,1}$ and its even endpoint-product image
${\cal E}_{q,1}\subseteq{\cal P}_{3q}$ be as in the residual-quotient
theorem.  The first result is the exact direct sum



$$
\boxed{
 {\cal E}_{q,1}
 =Q^2{\cal P}_{q}\ \oplus\ QG{\cal P}_{q-1}
       \ \oplus\ G^2{\cal P}_{q-2}.}                    \tag{5}
$$



This is stronger than a rational rank statement: it gives a canonical
three-block right inverse for every endpoint in the image.

Let $u_{4q},u_{4q+1}$ and



$$
K_q=\gcd(u_{4q},u_{4q+1})                                \tag{6}
$$



be the two bordered integers and their exact content from the balanced
border-content theorem.  Universal nonvanishing gives the primitive
quadratic



$$
T_q(x)=\frac{u_{4q}-u_{4q+1}x}{K_q}\in\mathbb Z[x].      \tag{7}
$$



Reduction modulo $Q$, represented in degree at most $q-1$, is
denoted by $\rho_Q$.  Define successively



$$
\begin{aligned}
 C_T&=\rho_Q(G^{-2}T_q),\\
 J_T&=\frac{T_q-G^2C_T}{Q},\\
 B_T&=\rho_Q(G^{-1}J_T),\\
 A_T&=\frac{J_T-GB_T}{Q}.
 \end{aligned}                                            \tag{8}
$$



Every displayed quotient is exact, and



$$
\deg A_T,\deg C_T\leq q-2,qquad \deg B_T\leq q-1.      \tag{9}
$$



The primitive endpoint has the exact decomposition



$$
\boxed{T_q=Q^2A_T+QGB_T+G^2C_T.}                         \tag{10}
$$



Set $x=z^2$ and



$$
\begin{aligned}
 {\cal Q}(z)&=Q(x)-2\cosh z\,P(x),\\
 {\cal G}(z)&=G(x)-2\cosh z\,R(x).
 \end{aligned}                                            \tag{11}
$$



Then



$$
\boxed{
 {\cal L}_q(z)=
 A_T(x){\cal Q}(z)^2+B_T(x){\cal Q}(z){\cal G}(z)
                  +C_T(x){\cal G}(z)^2}                  \tag{12}
$$



is a normalized global lift with



$$
\begin{array}{c|c|c|c}
 \text{frequency band}&\text{polynomial degree}&
 \text{origin order}&\text{value at }z=i\pi/2\\ \hline
 -2,-1,0,1,2&\leq6q&\geq8q+4&T_q(-\pi^2/4).
 \end{array}                                              \tag{13}
$$



No ambient product-matrix determinant or Cramer clearing occurs in
(8)--(12).  Moreover, the division by $K_q$ is exact globally: if
the same four linear operations in (8) are first applied to
$u_{4q}-u_{4q+1}x$, every centered coefficient of the resulting
global form is divided by precisely $K_q$ in (12).

The coefficients in (12) are rational and are used only in the analytic
Schwarz majorant for the already primitive integral endpoint (7).  They
do not have to be cleared to integers before applying the integer
polynomial measure to $T_q(-\pi^2/4)$; accordingly, (14) is a bound
for absolute rational coefficient size, not a claim about the common
denominator or primitive integral height of the five global coefficient
polynomials.

There is also a genuinely smaller all-parameter height bound:



$$
\boxed{
 \log H(T_q)=O(q^2),\qquad
 \log H_{\rm an}({\cal L}_q)=O(q^2).}                    \tag{14}
$$



Here, if



$$
{\cal L}_q(z)=\sum_{r=-2}^{2}e^{rz}L_r(z),
$$



then



$$
H_{\rm an}({\cal L}_q)
 =\max_{-2\leq r\leq2}\max_j|[z^j]L_r(z)|.               \tag{15}
$$



The improvement from $O(q^2\log q)$ to $O(q^2)$ comes from an
exact cancellation between a prime-by-prime denominator and the forced
columns of the secant Schur function.  It does not assume any lower
bound for $K_q$.

## 2. The direct Padé basis

Write a factor in ${\cal U}_{q,1}$ as
$A_0(x)+zA_1(x)$.  The parity-block and Krylov theorems can be used
before reduction modulo $Q$.  If $q=2a$, they give



$$
\begin{aligned}
 V_0&=Q{\cal P}_a\oplus G{\cal P}_{a-1},\\
 V_1&=Q{\cal P}_{a-1}\oplus G{\cal P}_{a-2}.
 \end{aligned}                                            \tag{16}
$$



Indeed, every displayed multiple of $G$ has the required zero block
by the $[q+1/q-1]$ Padé equations.  Its reduction modulo $Q$ is
the previously proved $G$-Krylov basis.  The sums are direct because
$\gcd(Q,G)=1$ and every multiplier of $G$ has degree less than
$q$.  Their dimensions are those of the full parity blocks.

If $q=2a+1$, the two parity blocks coincide and



$$
V_0=V_1=V=Q{\cal P}_a\oplus G{\cal P}_{a-1}.             \tag{17}
$$



For even $q$, expansion of $V_0^2+xV_1^2$ gives



$$
Q^2{\cal P}_{2a}+QG{\cal P}_{2a-1}+G^2{\cal P}_{2a-2}.
                                                                    \tag{18}
$$



The second block contributes only subspaces already present in (18).
This includes the edge $q=2$: then
${\cal P}_{a-2}=0$ in $V_1$, while $V_0^2$ still supplies all
three summands in (18).

For odd $q$, expansion of $V^2+xV^2$, using
${\cal P}_d+x{\cal P}_d={\cal P}_{d+1}$, gives



$$
Q^2{\cal P}_{2a+1}+QG{\cal P}_{2a}+G^2{\cal P}_{2a-1}.
                                                                    \tag{19}
$$



Equations (18)--(19) prove equality in (5).  To prove directness,
suppose



$$
Q^2A+QGB+G^2C=0,qquad
 A\in{\cal P}_q, B\in{\cal P}_{q-1}, C\in{\cal P}_{q-2}.
                                                                    \tag{20}
$$



Reduction modulo $Q$ and $\gcd(Q,G)=1$ give $Q\mid C$, hence
$C=0$.  After division by $Q$, the same argument gives
$Q\mid B$, hence $B=0$, and then $A=0$.  This proves the
direct sum without a dimension extrapolation.

## 3. Canonical decomposition of the primitive quadratic

The residual annihilator is



$$
\lambda(U)=[x^{q-1}]\rho_Q(G^{-2}U).                     \tag{21}
$$



The two first moments satisfy
$h_j=\lambda(x^j)$, and the primitive polynomial (7) is proportional
to $h_1-h_0x$.  Therefore



$$
\lambda(T_q)=0.                                          \tag{22}
$$



It follows from (21) that the first line of (8) has degree at most
$q-2$.  The definitions of $C_T$ and $B_T$ make the two
numerators in (8) divisible by $Q$.  Degree comparison gives



$$
\begin{aligned}
 \deg J_T&\leq2q-4,\\
 \deg B_T&\leq q-1,\\
 \deg A_T&\leq q-2.
 \end{aligned}                                            \tag{23}
$$



The two identities



$$
T_q=QJ_T+G^2C_T,qquad J_T=QA_T+GB_T                  \tag{24}
$$



prove (9)--(10).  Uniqueness also follows from the direct sum (5).

The construction is linear in $T_q$.  Consequently, with



$$
T_q^{\rm raw}=u_{4q}-u_{4q+1}x,                          \tag{25}
$$



one has coefficient by coefficient



$$
(A_T,B_T,C_T,{\cal L}_q)
 =\frac1{K_q}(A_{\rm raw},B_{\rm raw},C_{\rm raw},
                         {\cal L}_{\rm raw}).             \tag{26}
$$



This is the promised exact tracking of the two-border content.

## 4. The global identity

For every monomial shift that occurs in (16)--(19), the Padé zero
blocks and the degree bounds give



$$
\begin{aligned}
 R_n[x^sQ(z^2)]&=x^s{\cal Q}(z),\\
 R_n[x^sG(z^2)]&=x^s{\cal G}(z).
 \end{aligned}                                            \tag{27}
$$



For example, $FQ-P=O(x^{2q+1})$, while the largest allowed
$x^sP$ has $z$-degree at most $3q=n-1$.  Thus its canonical
lower lift is exactly the first line of (27).  The adjacent pair is
identical, using $\deg R=q+1$.  This proves that (12) is the
polarized global realization of (10).

Both ${\cal Q}$ and ${\cal G}$ vanish to order at least
$4q+2$ at the origin, proving the origin order in (13).  At
$z=i\pi/2$, $\cosh z=0$, and (10) gives the endpoint.  Finally,
the largest degree comes from the $B_T{\cal Q}{\cal G}$ and
$C_T{\cal G}^2$ terms:



$$
2(q-1)+(2q)+(2q+2)=6q,qquad
 2(q-2)+2(2q+2)=6q.                                       \tag{28}
$$



This proves all assertions in (13).

For the coefficient ledger, put



$$
\begin{aligned}
 U_T&=2A_TQP+B_T(QR+PG)+2C_TGR,\\
 V_T&=A_TP^2+B_TPR+C_TR^2.
 \end{aligned}                                            \tag{29}
$$



Then the exact centered expansion is



$$
{\cal L}_q
 =T_q-(e^z+e^{-z})U_T+(e^{2z}+2+e^{-2z})V_T.             \tag{30}
$$



Thus the five centered coefficient polynomials are
$V_T,-U_T,T_q+2V_T,-U_T,V_T$.

## 5. A prime-by-prime Schur denominator

Set



$$
H(y)=2F(-y)=\sec\sqrt y=\sum_{j\geq0}h_jy^j,
 \qquad h_j=\frac{|E_{2j}|}{(2j)!}.                       \tag{31}
$$



For $0\leq k\leq q$, put



$$
\lambda^{(k)}=((q+1)^k,q^{q-k}),qquad
 S_k=s_{\lambda^{(k)}}(t_0,t_1,\ldots),                  \tag{32}
$$



where $t_\nu=4/(\pi^2(2\nu+1)^2)$.  The cofactor formula gives



$$
Q(x)=\frac1{S_0}\sum_{k=0}^qS_kx^k.                    \tag{33}
$$



Define the integer



$$
{\mathfrak D}_q=
 \prod_{p\leq4q}p^{\left\lfloor
          2(q^2+q)/(p-1)\right\rfloor},                  \tag{34}
$$



the product being over primes.  Then



$$
\boxed{{\mathfrak D}_qS_k\in\mathbb Z
        \quad(0\leq k\leq q).}                          \tag{35}
$$



Here is the full denominator audit.  A nonzero term in the
Jacobi--Trudi expansion of $S_k$ is a product



$$
\prod_{i=1}^q h_{\lambda_i^{(k)}-i+\sigma(i)}.           \tag{36}
$$



Write $d_i=\lambda_i^{(k)}-i+\sigma(i)\geq0$.  Then



$$
\sum_i d_i=|\lambda^{(k)}|=q^2+k\leq q^2+q,qquad
 d_i\leq2q.                                               \tag{37}
$$



For every prime $p$, Legendre's bound gives



$$
v_p\!\left(\prod_i(2d_i)!\right)
 \leq\sum_i\frac{2d_i}{p-1}
 \leq\frac{2(q^2+q)}{p-1}.                               \tag{38}
$$



There are no denominator primes above $4q$.  Because the numerator
of every $h_{d_i}$ is an integer, (34) and (38) clear every term in
(36), proving (35).

The size of this clearing is sharp enough at the leading scale.  The
elementary Mertens estimate



$$
\sum_{p\leq X}\frac{\log p}{p-1}=\log X+O(1)            \tag{39}
$$



gives



$$
\log {\mathfrak D}_q=2q^2\log q+O(q^2).                 \tag{40}
$$



For completeness, (39) follows without the prime number theorem.
The divisor identity $\sum_{d\mid m}\Lambda(d)=\log m$, Stirling's
formula, and Chebyshev's bound $\sum_{d\leq X}\Lambda(d)=O(X)$
give
$\sum_{d\leq X}\Lambda(d)/d=\log X+O(1)$.  Expanding
$1/(p-1)=\sum_{r\geq1}p^{-r}$ changes this last sum by a bounded
prime-power tail, proving (39).

## 6. The forced-column cancellation and primitive endpoint height

The shape $\lambda^{(k)}$ has $q$ full columns of height $q$
and one additional column of height $k$.  If the row inequalities of
a semistandard tableau are discarded while the strict inequalities in
each column are retained, the columns become independent.  Therefore



$$
0<S_k\leq e_q(t)^q e_k(t)
 =\frac1{((2q)!)^q(2k)!}.                                 \tag{41}
$$



For $k=0$, the trailing height-zero column is simply omitted and the
same formula uses $e_0=1$.

Put



$$
V_q=\max_{0\leq k\leq q}{\mathfrak D}_qS_k.             \tag{42}
$$



Equations (35), (40), (41), and Stirling give the exact leading
cancellation



$$
\begin{aligned}
 \log V_q
 &\leq \underbrace{2q^2\log q}_{\log{\mathfrak D}_q}
   -\underbrace{2q^2\log q}_{q\log(2q)!}+O(q^2)\\
 &=O(q^2).                                                 \tag{43}
 \end{aligned}
$$



This is the step missed by rowwise factorial clearing.

Let $c=(c_0,\ldots,c_q)$ be the primitive integral diagonal Padé
denominator used in the border-content theorem, and let
$b_m$ be its cleared border row.  The integral vector



$$
v=({\mathfrak D}_qS_0,\ldots,{\mathfrak D}_qS_q)         \tag{44}
$$



lies in the same one-dimensional rational kernel.  Hence



$$
v=\gamma_q c\qquad\text{for a nonzero integer }\gamma_q.\tag{45}
$$



With $w_m=b_mv$, equations (45) and the definitions of $u_m,K_q$
give



$$
w_m=\gamma_qu_m,qquad
 \gcd(w_{4q},w_{4q+1})=|\gamma_q|K_q.                    \tag{46}
$$



Thus the Schur clearing produces exactly the same primitive endpoint,
not a new unsaturated multiple.

The border estimate already proved in the bordered-content theorem is



$$
|b_{m,k}|\leq\frac{3q}{4}\Lambda_q,qquad
 \Lambda_q=4(8q+2)!,qquad m\in\{4q,4q+1\}.              \tag{47}
$$



Consequently, with $\|T\|_1$ denoting coefficient $\ell^1$-norm,



$$
\boxed{
 \|T_q\|_1
 =\frac{|u_{4q}|+|u_{4q+1}|}{K_q}
 \leq\frac{3q(q+1)}2\Lambda_qV_q.}                      \tag{48}
$$



Since $\log\Lambda_q=O(q\log q)$, (43)--(48) prove the first
bound in (14).  Notice that (46)--(48) retain the exact division by
$K_q$; the universal upper bound merely uses
$|\gamma_q|K_q\geq1$.

## 7. Stable negative powers and the global coefficient norm

The Padé coefficient bounds needed here are normalization-specific.
From Pieri's rule, adding the vertical $k$-strip in (32) gives



$$
0\leq[x^k]Q=\frac{S_k}{S_0}\leq e_k(t)=\frac1{(2k)!}.   \tag{49}
$$



The adjacent denominator has the analogous cofactor shapes



$$
\mu^{(k)}=((q+2)^k,(q+1)^{q-1-k}),                      \tag{50}
$$



so the same Pieri argument gives



$$
0\leq[x^k]G\leq\frac1{(2k)!}.                           \tag{51}
$$



Set the absolute coefficient $\ell^1$-norm to $\|\cdot\|_1$, and
put



$$
a_0=\cosh1,qquad
 p_0=\frac12\sec1\cosh1,qquad
 d_0=\frac1{2-\cosh1}.                                   \tag{52}
$$



Equations (49)--(51), together with
$\sum h_j=\sec1$, imply



$$
\|Q\|_1,\|G\|_1\leq a_0,qquad
 \|P\|_1,\|R\|_1\leq p_0.                              \tag{53}
$$



The following elementary quotient-algebra lemma avoids division by the
small leading coefficient of $Q$.  Write



$$
Q=1+q_1x+\cdots+q_qx^q,qquad
 \sigma=\sum_{k=1}^qq_k\leq\cosh1-1<1.                  \tag{54}
$$



Then, for every $s\geq1$,



$$
\boxed{\|\rho_Q(x^{-s})\|_1\leq1.}                      \tag{55}
$$



Indeed, multiplication of $Q=0$ by $x^{-s}$ gives



$$
\rho_Q(x^{-s})=-\sum_{k=1}^qq_k\rho_Q(x^{k-s}).          \tag{56}
$$



If $k\geq s$, the exponent on the right lies between $0$ and
$q-1$; if $k<s$, induction applies.  The right side of (56) has
norm at most $\sigma<1$, proving (55).

Let $N=2q+1$ and $k_q=|\kappa|$.  Reduction of (4) modulo $Q$
gives, in the fixed normalization (2),



$$
G^{-1}\equiv-\kappa^{-1}Px^{-N},\qquad
 G^{-2}\equiv\kappa^{-2}P^2x^{-2N}\pmod Q.              \tag{57}
$$



All powers occurring in the second expression applied to $T_q$ are
negative.  In the first expression applied to $J_T$, every exponent
is either negative or at most $q-1$, because
$\deg P+\deg J_T-N\leq q-5$.  Hence (55) and (53) give the following
fully explicit majorant.  Put



$$
\begin{aligned}
 t_T&=\|T_q\|_1=\frac{|u_{4q}|+|u_{4q+1}|}{K_q},\\
 c_T&=k_q^{-2}p_0^2t_T,\\
 j_T&=d_0(t_T+a_0^2c_T),\\
 b_T&=k_q^{-1}p_0j_T,\\
 a_T&=d_0(j_T+a_0b_T),\\
 s_T&=a_T+b_T+c_T.
 \end{aligned}                                            \tag{58}
$$



Then



$$
\|C_T\|_1\leq c_T,qquad
 \|J_T\|_1\leq j_T,qquad
 \|B_T\|_1\leq b_T,qquad
 \|A_T\|_1\leq a_T.                                    \tag{59}
$$



The two quotient bounds in (59) use the convergent formal inverse



$$
\|Q^{-1}\|_1\leq\sum_{r\geq0}\sigma^r
 \leq d_0.                                                \tag{60}
$$



Finally, (29), (30), (53), and (59) give the concrete analytic-height
bound requested in (15):



$$
\boxed{
 H_{\rm an}({\cal L}_q)
 \leq
 \max\{t_T+2p_0^2s_T,\ 2a_0p_0s_T,\ p_0^2s_T\}.}       \tag{61}
$$



This formula displays the exact factor $K_q^{-1}$ through $t_T$.

## 8. A normalized Schur lower bound for the cross coefficient

It remains to bound $k_q^{-1}$ in the normalization (2).  Put



$$
\tau_q=\prod_{\nu=0}^{q-1}t_\nu
 =\frac{16^q(q!)^2}{\pi^{2q}((2q)!)^2}.                  \tag{62}
$$



Index the rows of a semistandard tableau from $1$ to $q$, and add a
new box on the left of row $i$, filled by $i-1$.  The new column is
strictly increasing.  Every old entry in row $i$ is at least
$i-1$, because entries are nonnegative and every old column is
strictly increasing from the first row.  Hence the new left box is no
larger than the old first box, so every row remains weakly increasing.
Deleting the new column recovers the original tableau, making this an
injection from shape $(q^q)$ to shape $((q+1)^q)$.  Its weight is
multiplied by exactly $\tau_q$.  Therefore



$$
\frac{s_{((q+1)^q)}}{s_{(q^q)}}\geq\tau_q.              \tag{63}
$$



The left side is $|\operatorname {lc}(Q)|$.  For the adjacent pair,
the last numerator coefficient is the augmented Jacobi--Trudi minor:



$$
|\operatorname {lc}(R)|
 =\frac12\frac{s_{((q+1)^q)}}
                    {s_{((q+1)^{q-1})}}.                 \tag{64}
$$



The numerator in (64) contains the principal tableau of weight
$\tau_q^{q+1}$.  Dropping row inequalities in the denominator gives



$$
s_{((q+1)^{q-1})}\leq e_{q-1}^{q+1}
 =((2q-2)!)^{-(q+1)}.                                     \tag{65}
$$



Since (4) gives
$|\kappa|=|\operatorname {lc}(R)\operatorname {lc}(Q)|$,
(63)--(65) prove



$$
\boxed{
 k_q\geq\frac12\tau_q
       \{\tau_q(2q-2)!\}^{q+1}.}                         \tag{66}
$$



Stirling's formula gives



$$
-\log k_q=O(q^2).                                        \tag{67}
$$



All quantities in (63)--(67) use $Q(0)=G(0)=1$.  There is no hidden
scaling assumption: under



$$
(Q,P,G,R)\mapsto(\alpha Q,\alpha P,\beta G,\beta R),     \tag{68}
$$



one has



$$
\kappa\mapsto\alpha\beta\kappa,\qquad
 (A_T,B_T,C_T)\mapsto
 (\alpha^{-2}A_T,(\alpha\beta)^{-1}B_T,\beta^{-2}C_T),   \tag{69}
$$



so the global form (12) is invariant.  We fix (2) before applying the
lower bound (66).

Equations (48), (58), (61), and (67) prove the second bound in (14).

## 9. Asymptotic ledger and logical boundary

For the balanced parameters, the centered Schwarz gain is



$$
G_{n,q}=2q\log q+O(q).                                   \tag{70}
$$



The present theorem replaces both the ambient $O(q^3\log q)$
absolute-coefficient lift majorant and the earlier row-cleared
$O(q^2\log q)$ endpoint majorant by $O(q^2)$ bounds.  It also proves
that the rational analytic quotient/Cramer gap is not intrinsic: the
direct formula (12) lifts the exact primitive endpoint.  It does not
claim an $O(q^2)$ common denominator or primitive integral height for
the five global coefficient polynomials; those denominators are not
part of the subsequent endpoint measure.

This does not make the measure margin positive.  The proved upper scale
$O(q^2)$ is still larger than the analytic gain (70), and an upper
bound cannot serve as a height lower bound or an impossibility theorem.
Exact computations show



$$
H_{\rm an}({\cal L}_q)=\frac32H(T_q)
$$



on the replay grid, but no all-$q$ coefficient-sign theorem proving
this sharper identity is asserted here.  It remains diagnostic only.
Nothing in this note classifies $e+\pi$.

## 10. Deterministic replay

The companion files are:

* scripts/centered_cosh_balanced_quadratic_normalized_global_lift_certificate.py;
* results/centered_cosh_balanced_quadratic_normalized_global_lift_certificate.json;
* results/centered_cosh_balanced_quadratic_normalized_global_lift_hashes.sha256.

The replay checks the direct-sum bases, the canonical decomposition,
the exact global endpoint and origin order, the Schur cofactors and
prime-by-prime clearing, the content relation (46), the normalized
cross coefficient and its lower bound, the stable negative-power
inequalities, and the concrete coefficient bound (61).  The finite
$3/2$ observation is explicitly marked diagnostic.
