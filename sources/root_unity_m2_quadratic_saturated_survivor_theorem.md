> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A fixed-space quadratic survivor in the saturated $m=2$ global image

## Exact hyperbolic-secant positivity, a uniform $O(n\log n)$ global vector, and the current sharp height ledger

Checked: 2026-08-27 UTC

## 1. Scope and verdict

For every $n\geq5$, take the six-dimensional endpoint space



$$
E_6=\mathbb Q[z]_{\leq5}
$$



in the $m=2$ root-of-unity Hermite--Padé construction. This note gives
an explicit rational exterior sum



$$
\Omega_n\in\Lambda^2E_6
$$



whose corrected endpoint is an exact, nonzero quadratic:



$$
\Delta_{\Omega_n}(z)=p_{0,n}+p_{2,n}z^2,
 \qquad p_{0,n}p_{2,n}>0.                                 \tag{1}
$$



The exterior sum lies in the mixed even--odd parity block. Its complete
global Wronskian image has frequencies $0,1,2,3,4$, polynomial degree
at most $2n-2$, and origin order at least $4n+4$. After a completely
explicit clearing it is an integral vector of height



$$
\exp\{(16+o(1))n\log n\}.             \tag{2}
$$



Primitive division can only decrease (2). Thus the intrinsically
saturated low-endpoint global image contains a nonzero quadratic survivor
with uniformly $O(n\log n)$ logarithmic global height. This is an
all-parameter theorem, not an extrapolation from HNF or LLL grids.

The leading constants are nevertheless too large. If $g_n$ is the exact
common content of the two endpoint coefficients after the fixed clearing
in Section 6, put



$$
\chi_n=\frac{\log g_n}{n\log n}.      \tag{3}
$$



The coefficientwise estimates proved below are



$$
\begin{aligned}
 \log H(P_n^{\mathrm{prim}})
    &\leq(10-\chi_n)n\log n+O(n),\\
 \log H_{\mathrm{an}}(\mathscr F_n)
    &\leq(14-\chi_n)n\log n+O(n).                          \tag{4}
 \end{aligned}
$$



Here $H_{\mathrm{an}}$ is the complete global coefficient height after
normalizing the endpoint to the primitive quadratic. It is exactly the
primitive integral global height divided by its endpoint content; no
unproved global gcd cancellation is used.

Centered Schwarz supplies only



$$
2G_n=2n\log n+O(n).               \tag{5}
$$



If $e+\pi$ were rational, the degree-two polynomial measure for $e$
would have leading height exponent $2$. The sufficient leading
inequality obtained from the present bounds would be



$$
2>34-3\chi_n.                     \tag{6}
$$



But the endpoint formula itself gives only



$$
0\leq\chi_n\leq10+o(1).           \tag{7}
$$



Thus even the largest common endpoint content compatible with the proved
majorant leaves a leading deficit of at least $2n\log n$. This is a
barrier for the currently proved coefficientwise bounds, not a lower
bound for the true height and not a proof that no shorter vector exists
elsewhere in the saturated image. No lower bound for $g_n$, no
unproved gcd cancellation, and no all-parameter Smith pattern is assumed.

This note does not prove that $e+\pi$ is rational, irrational, algebraic,
or transcendental.

## 2. The five-coordinate lower excess kernel

Let



$$
\mathcal L(X^k)=\mu_k,
 \qquad
 \sum_{k\geq0}\mu_k\frac{z^k}{k!}=\frac1{1+e^z},           \tag{8}
$$



and put



$$
\Psi_n(X)=X^n(X-1)^n.             \tag{9}
$$



The two lower excess rows on endpoint degrees $0,\ldots,4$ are



$$
H_{q,a}=\mathcal L\!\left(
   \bigl((X-\tfrac12)^q\Psi_n(X)\bigr)^{(a)}\right),
 \qquad q=0,1,\quad0\leq a\leq4.                          \tag{10}
$$



Reflection gives the checkerboard pattern



$$
H_{q,a}=0
                  \quad\text{if }q\not\equiv a\pmod2.     \tag{11}
$$



Write



$$
A=H_{0,0},\quad B=H_{0,2},\quad C=H_{0,4},
 \qquad g_1=H_{1,1},\quad g_3=H_{1,3}.                    \tag{12}
$$



The contour proof below gives the exact phases needed for (13) and shows
that $A,B,g_1$ are nonzero. Consequently



$$
\begin{aligned}
 E_0(z)&=B-Az^2,\\
 E_1(z)&=C-Az^4,\\
 O(z)&=g_3z-g_1z^3                                      \tag{13}
 \end{aligned}
$$



have the displayed degrees. Equation (11) gives immediately



$$
HE_0=HE_1=HO=0.                  \tag{14}
$$



Thus every polynomial in (13) has the exact lower-parameter lift supplied
by the endpoint-displacement theorem.

## 3. The explicit exterior sum and its global image

Put



$$
x=2Ag_1g_3-Bg_1^2,\qquad
 y=-Ag_1^2,\qquad
 w=A^3.                                                   \tag{15}
$$



For $U,V\in\ker H$, the endpoint-displacement square and polarization
identities are



$$
\Delta(U,zU)=U^2,\qquad
 \Delta(U,zV)+\Delta(V,zU)=2UV.                           \tag{16}
$$



Consequently



$$
\Omega_n=
 xE_0\wedge zE_0
 +\frac y2\{E_0\wedge zE_1+E_1\wedge zE_0\}
 +wO\wedge zO                                             \tag{17}
$$



lies in $\Lambda^2\mathbb Q[z]_{\leq5}$, and



$$
P_n(z)=xE_0(z)^2+yE_0(z)E_1(z)+wO(z)^2.                 \tag{18}
$$



All coefficients in degrees $4,6,8$ cancel identically. Direct
expansion gives



$$
\boxed{
 \begin{aligned}
 p_0&=Bg_1\{2ABg_3-(B^2+AC)g_1\},\\
 p_2&=A\{A^2g_3^2-4ABg_1g_3+ACg_1^2+2B^2g_1^2\}.
                                                               \tag{19}
 \end{aligned}}
$$



Every term of (17) wedges an even endpoint with an odd endpoint:
$E_0,E_1,O$ have parities even, even, odd, while multiplication by
$z$ reverses parity. Thus $\Omega_n$ belongs to one mixed-parity
exterior block.

Let $R_U$ be the lifted global remainder attached to $U\in\ker H$.
The global versions of (16) are



$$
W(R_U,R_{zU})=R_U^2,\qquad
 W(R_U,R_{zV})+W(R_V,R_{zU})=2R_UR_V.                    \tag{20}
$$



The complete global image of (17) is therefore exactly



$$
\mathscr F_n=xR_{E_0}^2+yR_{E_0}R_{E_1}+wR_O^2. \tag{21}
$$



Each factor has frequencies $0,1,2$, polynomial degree at most $n-1$,
and origin order at least $2n+2$. Hence



$$
\begin{gathered}
 \mathscr F_n=O(z^{4n+4}),\\
 \operatorname{freq}(\mathscr F_n)\subseteq\{0,1,2,3,4\},
 \qquad \deg_z\mathscr F_n\leq2n-2,                       \tag{22}\\
 \mathscr F_n(i\pi)=P_n(i\pi).
 \end{gathered}
$$



Any integral clearing of (21) lies in the rational global image and hence
in its intrinsic saturation. This is the exact link with the frozen
tall-HNF saturation theorem.

## 4. Hyperbolic-secant model and fixed-size recurrence

Set



$$
S(t)=t^2+\frac14,\qquad
 V_n(t)=S(t)^n,\qquad
 q(t)=\operatorname{sech}(\pi t).                         \tag{23}
$$



The centered contour formula and the shift relation for $\mathcal L$
give, since $a<n$,



$$
H_{q,a}=\frac{(-1)^{n+1}}2\,i^{q-a}
       \int_{-\infty}^{\infty}(t^qV_n(t))^{(a)}q(t)\,dt.  \tag{24}
$$



Define



$$
\begin{aligned}
 a_n&=\int V_nq,& b_n&=\int V_n''q,& c_n&=\int V_n''''q,\\
 u_n&=\int(tV_n)'q,& v_n&=\int(tV_n)'''q.                 \tag{25}
 \end{aligned}
$$



All integrals in this note are over $\mathbb R$. We use only
$a_n,b_n,u_n>0$, which follows in Section 5; no sign is assumed for
$c_n$ or $v_n$. With $\sigma_n=(-1)^{n+1}$, equation (24) says



$$
(A,B,C,g_1,g_3)
       =\frac{\sigma_n}{2}(a_n,-b_n,c_n,u_n,-v_n).         \tag{26}
$$



Let $E_{2j}$ be the signed Euler numbers. The Fourier transform of the
hyperbolic secant yields



$$
a_n=4^{-n}\sum_{j=0}^n\binom nj|E_{2j}|.     \tag{27}
$$



Writing $a_j=0$ for $j<0$, differentiation of $S^n$ gives



$$
\begin{aligned}
 b_n={}&2n(2n-1)a_{n-1}-n(n-1)a_{n-2},\\
 u_n={}&(2n+1)a_n-\frac n2a_{n-1},\\
 v_n={}&2n(2n-1)(2n+1)a_{n-1}
       -2n(n-1)(2n-1)a_{n-2}
       +\frac{n(n-1)(n-2)}2a_{n-3},\\
 c_n={}&4n(n-1)(2n-1)(2n-3)a_{n-2}\\
      &-4n(n-1)(n-2)(2n-3)a_{n-3}
       +n(n-1)(n-2)(n-3)a_{n-4}.                         \tag{28}
 \end{aligned}
$$



Equations (27)--(28) are a fixed-size exact recurrence description of
the survivor. They avoid a growing tail-kernel HNF or Smith computation.

## 5. Uniform nonvanishing and exact degree two

Define



$$
\begin{aligned}
 K_n&=2a_nb_nv_n-(b_n^2+a_nc_n)u_n,\\
 L_n&=a_n^2v_n^2-4a_nb_nu_nv_n+a_nc_nu_n^2+2b_n^2u_n^2.
                                                               \tag{29}
 \end{aligned}
$$



We prove



$$
K_n>0,\qquad L_n<0
                         \qquad(n\geq5).                   \tag{30}
$$



### 5.1 Three monotone expectations

Normalize $V_n(t)q(t)\,dt$ to a probability measure and put



$$
x(t)=\frac14\operatorname{sech}^2(\pi t),\qquad
 h(t)=t\tanh(\pi t),                                      \tag{31}
$$





$$
\alpha=\mathbb E x,\qquad
 \beta=\mathbb E x^2,\qquad
 \gamma=\frac{\mathbb E(hx)}{\mathbb E h}.                \tag{32}
$$



On $t>0$, $S(t)$ and $h(t)$ are strictly increasing, while
$\operatorname{sech}^2(\pi t)$ and $x(t)$ are strictly decreasing.
The strict reversed Chebyshev covariance identity gives



$$
\gamma<\alpha.                   \tag{33}
$$



For odd $r$, define



$$
I_r(n)=\int_{-\infty}^{\infty}
     S(t)^n\operatorname{sech}^r(\pi t)\,dt.              \tag{34}
$$



The same covariance identity proves that



$$
\frac{I_{r+2}(n)}{I_r(n)}
              \quad\text{strictly decreases with }n.     \tag{35}
$$



Indeed, the ratio at $n+1$ is the expectation of
$\operatorname{sech}^2(\pi t)$ after tilting the measure at $n$ by
the strictly increasing function $S(t)$.

Since $I_3(0)/I_1(0)=1/2$, equations (32), (34), and (35) give



$$
\alpha<\frac18.                  \tag{36}
$$



Also



$$
\frac\beta\alpha
                         =\frac{I_5(n)}{4I_3(n)}.          \tag{37}
$$



The elementary Fourier transforms are



$$
\begin{aligned}
 \int e^{iut}\operatorname{sech}^3(\pi t)\,dt
   &=\frac{u^2+\pi^2}{2\pi^2}\operatorname{sech}(u/2),\\
 \int e^{iut}\operatorname{sech}^5(\pi t)\,dt
   &=\frac23\left(\frac{u^2}{4\pi^2}+\frac14\right)
      \left(\frac{u^2}{4\pi^2}+\frac94\right)
      \operatorname{sech}(u/2).                          \tag{38}
 \end{aligned}
$$



Applying $(1/4-\partial_u^2)^5$ at $u=0$ gives



$$
I_3(5)-3I_5(5)
  =\frac{5\{2688\pi^2-4416-227\pi^4\}}{32\pi^4}>0.       \tag{39}
$$



For completeness, the sign uses no decimal approximation. Machin's
identity and alternating arctangent series give



$$
\pi<
 16\sum_{j=0}^{4}\frac{(-1)^j}{(2j+1)5^{2j+1}}
 -4\sum_{j=0}^{1}\frac{(-1)^j}{(2j+1)239^{2j+1}}
 <\frac{355}{113}.                                       \tag{40}
$$



The second gap is
$45167474711/189820334689453125$. On $x\geq9$, the polynomial
$2688x-4416-227x^2$ is strictly decreasing, and its value at
$(355/113)^2$ is



$$
\frac{265760749}{163047361}>0.   \tag{41}
$$



Together with the elementary $\pi>3$, this proves (39). Equations
(35), (37), and (39) imply



$$
\beta<\frac{\alpha}{12}
                         \qquad(n\geq5).                   \tag{42}
$$



### 5.2 The two signs

Repeated integration by parts and the derivative polynomials of the
hyperbolic secant give



$$
\begin{aligned}
 b_n&=\pi^2a_n(1-8\alpha),\\
 c_n&=\pi^4a_n(1-80\alpha+384\beta),\\
 u_n&=\pi a_n\mathbb E h,\\
 v_n&=\pi^3a_n\mathbb E h\,(1-24\gamma).                 \tag{43}
 \end{aligned}
$$



Substitution into $K_n$ yields



$$
\frac{K_n}{\pi^5a_n^3\mathbb E h}
 =16\{2\alpha+20\alpha^2-24\beta
        +(24\alpha-3)(\gamma-\alpha)\}.                  \tag{44}
$$



By (33), (36), and (42), the second summand in braces is positive
and the first is greater than $20\alpha^2$. Thus $K_n>0$.

Put $\delta=\alpha-\gamma$, so
$0<\delta<\alpha<1/8$. The analogous identity for $L_n$ is



$$
\frac{L_n}{16\pi^6a_n^4(\mathbb E h)^2}
 =\delta(36\delta-24\alpha-3)
   +24\beta-2\alpha-4\alpha^2.                            \tag{45}
$$



Here $36\delta-24\alpha-3<12\alpha-3<0$, while (42) makes
$24\beta-2\alpha-4\alpha^2<0$. Therefore $L_n<0$.

Finally, (19), (26), and (29) reduce to



$$
|p_0|=\frac{b_nu_nK_n}{32},
 \qquad
                         |p_2|=\frac{a_n(-L_n)}{32}.       \tag{46}
$$



Both coefficients are nonzero and have the same sign. This proves (1),
including exact degree two. Since $\pi$ is transcendental,
$P_n(i\pi)\neq0$.

## 6. Denominators, content, and a primitive global vector

The logistic recurrence gives



$$
|\mu_k|\leq k!,
 \qquad
                         \operatorname{den}(\mu_k)\mid2^{k+1}. \tag{47}
$$



Define



$$
D_n=2^{2n+3},\qquad
 \mathcal B_n=3\cdot2^n(2n+1)^4(2n+1)!.                  \tag{48}
$$



Coefficient $\ell^1$-norms of $\Psi_n$ and
$(X-\tfrac12)\Psi_n$, followed by at most four differentiations, give



$$
D_nA,D_nB,D_nC,D_ng_1,D_ng_3\in\mathbb Z,
\qquad
 \max(|A|,|B|,|C|,|g_1|,|g_3|)\leq\mathcal B_n.           \tag{49}
$$



In particular,



$$
\log\mathcal B_n
                         =2n\log n+O(n).                  \tag{50}
$$



The integers



$$
U_{0,n}=D_n^5p_0,\qquad
                         U_{2,n}=D_n^5p_2                 \tag{51}
$$



are nonzero. Define their exact common content by



$$
g_n=\gcd(|U_{0,n}|,|U_{2,n}|).    \tag{52}
$$



Then, up to one common sign,



$$
P_n^{\mathrm{prim}}(z)
     =\frac{U_{0,n}}{g_n}+\frac{U_{2,n}}{g_n}z^2          \tag{53}
$$



is primitive. There is no asserted common factor beyond (52), and no
finite gcd pattern is extrapolated. Formula (19) gives



$$
H(P_n^{\mathrm{prim}})
       \leq\frac{8(D_n\mathcal B_n)^5}{g_n},
\qquad
 1\leq g_n\leq8(D_n\mathcal B_n)^5.                      \tag{54}
$$



This proves the first line of (4) and (7).

For the explicit $m=2$ lower Hermite cardinals, put



$$
\mathcal C_n
   =n\,2^n\left(\frac43\right)^n16^{n-1}.                 \tag{55}
$$



For any endpoint $U$ of degree at most four, the direct cardinal bound is



$$
H(R_U)\leq H(U)\{1+10(2n-1)!\mathcal C_n\}.              \tag{56}
$$



Let



$$
\mathcal R_n
   =\mathcal B_n\{1+10(2n-1)!\mathcal C_n\}.              \tag{57}
$$



Then



$$
\log\mathcal R_n
                         =4n\log n+O(n).                  \tag{58}
$$



A coefficient in a product of two three-frequency degree-$(n-1)$
forms contains at most $3n$ summands. Equations (15), (21), and
(49)--(57) give



$$
H\!\left(\frac{D_n^5}{g_n}\mathscr F_n\right)
 \leq\frac{15nD_n^5\mathcal B_n^3\mathcal R_n^2}{g_n}.   \tag{59}
$$



This proves the second line of (4).

There is also an explicit integral vector. The two lower $m=2$ Hermite
cardinals for derivative $a$ are



$$
\begin{aligned}
 K_{0,a}(X)
 &=\frac{X^a}{a!}(1-X)^n
   \sum_{t=0}^{n-1-a}\binom{n+t-1}{t}X^t,\\
 K_{1,a}(X)
 &=\frac{(X-1)^a}{a!}X^n
   \sum_{t=0}^{n-1-a}(-1)^t
          \binom{n+t-1}{t}(X-1)^t.                       \tag{60}
 \end{aligned}
$$



Thus $(n-1)!$ clears their coefficients. The matched target jets have
moment denominators dividing $2^{2n}$ by (47), so



$$
q_n=2^{2n}(n-1)!                  \tag{61}
$$



clears $R_U$ whenever $U\in\mathbb Z[z]_{\leq4}$. The endpoints
$D_nE_0,D_nE_1,D_nO$ are integral, and their scalar coefficients are
$D_n^3x,D_n^3y,D_n^3w$. Therefore



$$
\mathbf V_n=q_n^2D_n^5\mathscr F_n
                  \in\mathbb Z^{5(2n-1)}.                 \tag{62}
$$



Equations (50), (58), and
$\log q_n=n\log n+O(n)$ give



$$
\log H(\mathbf V_n)
                         \leq16n\log n+O(n),              \tag{63}
$$



which proves (2). Its endpoint is



$$
q_n^2(U_{0,n}+U_{2,n}z^2),        \tag{64}
$$



so its endpoint content is exactly $q_n^2g_n$.

Let $h_n$ be the complete coefficient content of $\mathbf V_n$, and
put $\mathbf V_n^{\mathrm{prim}}=\mathbf V_n/h_n$. Integral endpoint
evaluation implies $h_n\mid q_n^2g_n$, and the endpoint content of the
primitive global vector is



$$
c_n=\frac{q_n^2g_n}{h_n}.         \tag{65}
$$



The intrinsic analytic normalization is the exact identity



$$
\boxed{
 \frac{H(\mathbf V_n^{\mathrm{prim}})}{c_n}
 =H\!\left(\frac{D_n^5}{g_n}\mathscr F_n\right).}         \tag{66}
$$



The unknown global content cancels. No assumption about $h_n$, Smith
invariants, or gcd cancellation is hidden in (59) or (66).

For the explicit one-dimensional rational image line, this also gives its
complete Smith description:



$$
\operatorname{Sat}(\mathbb Z\mathbf V_n)
   =\mathbb Z\mathbf V_n^{\mathrm{prim}},\qquad
 [\operatorname{Sat}(\mathbb Z\mathbf V_n):\mathbb Z\mathbf V_n]
   =h_n,\qquad \operatorname{SNF}=(h_n).                 \tag{66a}
$$



Thus $h_n\mid q_n^2g_n$ is the exact obstruction remaining in this
rank-one sublattice. Equation (66a) is not asserted to describe every
other direction of the full low-endpoint saturated image.

## 7. Centered Schwarz and the degree-two barrier

Multiplying $\mathscr F_n$ by $e^{-2z}$ centers its frequencies at
$-2,-1,0,1,2$ and changes neither its origin order nor its modulus at
$i\pi$. Put



$$
G_n=(n+3)\log\frac{n+3}{e\pi}-(n-1)\log\pi.              \tag{67}
$$



Using the radius $\rho=n+3$ in Schwarz's lemma and (22) gives



$$
|P_n^{\mathrm{prim}}(i\pi)|
 \leq5(2n-1)
 H\!\left(\frac{D_n^5}{g_n}\mathscr F_n\right)e^{-2G_n}. \tag{68}
$$



In particular,



$$
\frac{2G_n}{n\log n}\longrightarrow2. \tag{69}
$$



The polynomial is even, so



$$
A_n(X)=P_n^{\mathrm{prim}}(iX)
       =\frac{U_{0,n}}{g_n}-\frac{U_{2,n}}{g_n}X^2
       \in\mathbb Z[X].                                  \tag{70}
$$



If $s=e+\pi$ were rational, substituting $s-X$ and clearing its fixed
denominator would give an integer polynomial at $e$ of degree two and
height $O_s(H(P_n^{\mathrm{prim}}))$. The degree-two measure for $e$
therefore has leading threshold



$$
(2+o(1))\log H(P_n^{\mathrm{prim}}). \tag{71}
$$



Combining (4), (68), and (71), the present bounds could prove a
contradiction only if



$$
2>(14-\chi_n)+2(10-\chi_n)+o(1)
   =34-3\chi_n+o(1),                                     \tag{72}
$$



which is (6). Since (54) gives
$\chi_n\leq10+o(1)$, common endpoint content alone cannot make this
majorant ledger close.

More generally, if new structure saves $\eta_Gn\log n$ in the global
analytic height and $\eta_Pn\log n$ in the primitive endpoint height,
the exact missing weighted gain is



$$
\eta_G+2\eta_P+3\chi_n>32.        \tag{73}
$$



Even at the formal maximum $\chi_n=10+o(1)$, one still needs
$\eta_G+2\eta_P>2+o(1)$. A proof of large actual content, a structured
Smith/content theorem giving additional coefficient cancellation, or a
different lower-degree factor is needed to improve the current verdict.

## 8. Replay and logical scope

The package consists of:

* sources/root_unity_m2_quadratic_saturated_survivor_theorem.md;
* scripts/root_unity_m2_quadratic_saturated_survivor_certificate.py;
* results/root_unity_m2_quadratic_saturated_survivor_certificate.json;
  and
* results/root_unity_m2_quadratic_saturated_survivor_hashes.sha256.

Replay from the archive root with

    python3 scripts/root_unity_m2_quadratic_saturated_survivor_certificate.py

The replay:

1. verifies the symbolic identities (44)--(45);
2. certifies the Machin-series bound (40)--(41);
3. reconstructs the Fourier anchor (38)--(39);
4. builds $E_0,E_1,O$, their exact lower lifts, and (21) over
   $\mathbb Q$ for $5\leq n\leq20$;
5. verifies the exact quadratic endpoint, same-sign coefficients, finite
   origin orders, and all denominator/content normalizations;
6. verifies the $q_n^2$ integral clearing and (66); and
7. records finite height and measure-margin diagnostics without using
   them in the all-parameter proof.

The all-parameter conclusions are (1)--(5), (22), (30), (46), (54),
(59), (62)--(66), and the barrier (72)--(73). Finite Smith or gcd patterns
in the JSON are diagnostics only. The theorem neither classifies
$e+\pi$ nor licenses stopping the larger research program.
