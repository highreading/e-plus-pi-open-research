> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Multi-output Smith structure and the quadratic denominator obstruction

Checked: 2026-08-27 UTC.

## 1. Verdict

Let $N_1,\ldots,N_m$ be sign-possible native indices.  Write



$$
(1-i)^{N_i}=R_i+iI_i,qquad
 a_i=-I_i,qquad b_i=\frac{N_i!-R_i}{2},qquad f_i=N_i!.       \tag{1}
$$



For one shared integer localizer, the $i$-th rational output coordinate
has the exact form



$$
\rho_i=C_i-4\int_0^1(a_i+b_it)t(2-t)^2Q(t)\,dt.              \tag{2}
$$



The first result is an exact rank theorem: after clearing every beta-moment
denominator, the entire channel matrix factors through the two columns
$a=(a_i)$ and $b=(b_i)$.  Its rank is at most two, every $3$-minor
vanishes, and all nonzero Smith invariants and maximal minors reduce to
gcds of $2$-minors.  Adding the factorial column raises the rank to at
most three; adding the affine rational column raises it to at most four.
Thus any number of simultaneous outputs still has only two variable moment
directions.

The positive construction occurs first for five consecutive outputs.  Let



$$
N\equiv0\pmod8,\qquad
                         N,N+1,N+2,N+3,N+4.                    \tag{3}
$$



There is a primitive integer vector $c=(c_0,\ldots,c_4)$ satisfying



$$
\sum_{j=0}^4c_j(N+j)!=0,\qquad
 \sum_{j=0}^4c_jR_{N+j}=0,\qquad
 \sum_{j=0}^4c_jI_{N+j}=0,                                  \tag{4}
$$



for which every shared profile has the exact invariant value



$$
\boxed{
 \sum_{j=0}^4c_j{\cal L}_{N+j}(H)=\delta_N,\qquad
 \delta_N=\frac{2\eta_N}{(N+2)(N+3)}.}                       \tag{5}
$$



where



$$
\eta_N=
 \begin{cases}
 71,&N\equiv16\pmod {71},\\
 1,&N\not\equiv16\pmod {71}.
 \end{cases}                                                \tag{6}
$$



In particular, a primitive factorial-canceling combination really does tend
to zero, at scale $O(N^{-2})$.  This is the desired positive construction.
It does **not** give an integer contradiction.  The reduced denominator of
$\delta_N$ is exactly



$$
\boxed{Q_N=\frac{(N+2)(N+3)}2.}                            \tag{7}
$$



If $D$ is any common denominator of the five rational correction
coordinates, then



$$
\boxed{Q_N\mid D.}                    \tag{8}
$$



Consequently $D\delta_N$ is already a nonzero integer; the quadratic
denominator absorbs the $N^{-2}$ analytic gain exactly.  Under a temporary
rationality hypothesis for $e+\pi$, the same statement applies to every
common denominator clearing the five full outputs once the denominator of
$e+\pi$ divides $N!$.

The four-output comparison explains why the fifth coordinate is essential.
For four consecutive sign-possible indices, the unique primitive vector
annihilating the factorial and two Gaussian columns has invariant magnitude
asymptotic to a positive constant times $N^2$, rather than $o(1)$.
With five outputs the invariant lattice has rank two: one primitive direction
attains (5), while another nonzero primitive direction gives an exact zero
identity.  For still more outputs, further dimensions create further exact
zero relations, not additional independent moment freedom.

Finally, (7) is fully compatible with the raw beta clearing.  Since
$Q_N\mid\operatorname {lcm}(1,\ldots,N+3)$, it is already available inside
every clearing modulus used for degree at least $N+4$.  Even aggregating
many five-index blocks only forces an lcm which divides the global raw
clearing lcm.  Thus the Smith/content theorem is a sharp lattice obstruction,
not a proof that $e+\pi$ is irrational or transcendental.

## 2. The exact cleared beta matrix

Fix a Bernstein degree $n\geq\max_iN_i$, and put



$$
\Lambda=\operatorname {lcm}(1,\ldots,n+5). \tag{9}
$$



It is convenient first to use the monomial basis
$1,t,\ldots,t^n$.  Define



$$
\begin{aligned}
 \alpha_k&=4\Lambda\left\{
 \frac4{k+2}-\frac4{k+3}+\frac1{k+4}\right\},\\
 \beta_k&=4\Lambda\left\{
 \frac4{k+3}-\frac4{k+4}+\frac1{k+5}\right\}
 \qquad(0\leq k\leq n).                                      \tag{10}
\end{aligned}
$$



All $\alpha_k,\beta_k$ are integers.  They are the cleared responses of



$$
W_a=t(2-t)^2,qquad W_b=t^2(2-t)^2.    \tag{11}
$$



For the $i$-th native weight $W_i=a_iW_a+b_iW_b$, the cleared response
matrix is therefore



$$
\boxed{M_{ik}=a_i\alpha_k+b_i\beta_k.}                       \tag{12}
$$



The raw Bernstein polynomials



$$
t^k(1-t)^{n-k}\qquad(0\leq k\leq n)
$$



and the monomials are related by a triangular integer matrix with
diagonal entries one.  This matrix is unimodular.  Hence (12) has exactly the
same Smith form and determinantal divisors as the raw-Bernstein response
matrix from the single-output ledger.

If $P\in\mathbb Z[t]$ is the fixed initial polynomial and
$\kappa_i=\Lambda C_{i,P}\in\mathbb Z$, the cleared equations are



$$
\boxed{
 \Lambda{\cal L}_i
 =\Lambda f_i(e+\pi)+\kappa_i-\sum_{k=0}^nM_{ik}z_k.}          \tag{13}
$$



Thus the literal integer coefficient matrix is



$$
{\mathscr M}=[\,\Lambda f\mid\kappa\mid M\,]. \tag{14}
$$



Changing $P$, or translating the beta coefficients, changes $\kappa$ by
an integer combination of the columns of $M$.  It therefore does not
change the maximal-minor statements below.

## 3. Smith factors and maximal-minor factorization

Put



$$
A=\begin{pmatrix}a_1&b_1\\ \vdots&\vdots\\a_m&b_m\end{pmatrix},
 \qquad
 C=\begin{pmatrix}\alpha_0&\cdots&\alpha_n\\
                   \beta_0&\cdots&\beta_n\end{pmatrix}.       \tag{15}
$$



Then



$$
\boxed{M=AC.}                         \tag{16}
$$



For an integer matrix $X$, let $\Delta_r(X)$ be the gcd of all
$r\times r$ minors, with $\Delta_0=1$.  Every $2$-minor of $M$
factors without a sum:



$$
\det M_{\{i,j\},\{k,l\}}
 =(a_ib_j-a_jb_i)(\alpha_k\beta_l-\alpha_l\beta_k).            \tag{17}
$$



Consequently, when $M$ has rank two,



$$
\boxed{
 \Delta_2(M)=\Delta_2(A)\Delta_2(C),
 \qquad
 \operatorname {SNF}(M)_{\ne0}
 =\operatorname {diag}\left(
 \Delta_1(M),\frac{\Delta_2(A)\Delta_2(C)}{\Delta_1(M)}
 \right).}                                                   \tag{18}
$$



This is an exact all-parameter Smith formula, not a finite-data inference.

Let $F=[\,f\mid a\mid b\,]$.  A nonzero $3$-minor of
$[\,f\mid M\,]$ must use the factorial column and two response columns.
The same determinant factorization gives



$$
\boxed{
 \Delta_3([\,f\mid M\,])=\Delta_3(F)\Delta_2(C).}             \tag{19}
$$



Likewise, with $G=[\,f\mid\kappa\mid a\mid b\,]$, every nonzero
$4$-minor of (14) uses its first two columns and two response columns, so



$$
\boxed{
 \Delta_4({\mathscr M})
 =\Lambda\,\Delta_4(G)\Delta_2(C).}                           \tag{20}
$$



The single factor $\Lambda$ in (20) comes from the first column of (14).
Equations (18)--(20) are the promised exact minor ledger.  They show that
additional output rows create left kernels but never a third variable beta
direction.

## 4. The profile-independent left kernel

For $c=(c_i)\in\mathbb Z^m$, all beta responses and the common
$e+\pi$ term cancel exactly when



$$
c\mathbin\cdot f=c\mathbin\cdot a
                         =c\mathbin\cdot b=0.                  \tag{21}
$$



Since $a=-I$ and $2b=f-R$, conditions (21) are equivalent to



$$
c\mathbin\cdot f=c\mathbin\cdot R
                         =c\mathbin\cdot I=0.                  \tag{22}
$$



For such $c$, the output combination is independent of the common profile.
To evaluate it exactly, put



$$
B_j=\int_0^1e^{-t}t^j\,dt,qquad
 J_j=\int_0^1\frac{t^j}{t^2-2t+2}\,dt.                       \tag{23}
$$



The base output is



$$
{\cal L}_j(0)=eB_j+4J_j.               \tag{24}
$$



Also



$$
eB_j=j!e-E_j,qquad
 E_j=j!\sum_{h=0}^j\frac1{h!}\in\mathbb Z.                   \tag{25}
$$



For consecutive indices $N,\ldots,N+d$, encode $c$ by



$$
p(t)=\sum_{j=0}^dc_jt^j.               \tag{26}
$$



Then (22) is equivalent to



$$
\sum_{j=0}^dc_j(N+1)_j=0,\qquad
                         t^2-2t+2\mid p(t),                     \tag{27}
$$



where $(N+1)_j=(N+j)!/N!$ is rising.  Write



$$
p(t)=(t^2-2t+2)q(t).                    \tag{28}
$$



Equations (23)--(28) give the exact rational invariant



$$
\boxed{
 K_N(p):=\sum_{j=0}^dc_j{\cal L}_{N+j}(H)
 =-\sum_{j=0}^dc_jE_{N+j}+4\int_0^1t^Nq(t)\,dt\in\mathbb Q.}  \tag{29}
$$



This formula holds for every shared profile $H$.

For three consecutive indices, $d=2$, divisibility in (27) forces
$p=x_0(t^2-2t+2)$.  Its factorial functional is
$x_0(N^2+N+2)$, so $x_0=0$.  Thus three consecutive outputs have
no nonzero profile-independent relation.

## 5. Four consecutive outputs: the primitive invariant grows

Take $d=3$.  Put



$$
v=t^2-2t+2,qquad
 G=N^2+N+2,qquad
 H=(N+1)(N^2+3N+4),qquad d_N=\gcd(G,H).              \tag{30}
$$



Every polynomial satisfying (27) is an integer multiple of the primitive
polynomial



$$
p_{N,0}(t)=v(t)\frac{Gt-H}{d_N}.        \tag{31}
$$



Substitution in (29), using $E_{j+1}=(j+1)E_j+1$, gives



$$
\boxed{
 K_N(p_{N,0})
 =-\frac{5N^3+21N^2+50N+40}{d_N(N+2)}.}             \tag{32}
$$



The polynomial resultant is



$$
\operatorname {Res}_N(G,H)=16.         \tag{33}
$$



For the two four-index sign-possible windows,



$$
d_N=
 \begin{cases}
 2,&N\equiv0\pmod8,\\
 4,&N\equiv1\pmod8.
 \end{cases}                                                \tag{34}
$$



Thus the unique primitive profile-independent factorial-canceling
combination has magnitude asymptotic to $5N^2/d_N$.  Four simultaneous
outputs do not produce an $o(1)$ invariant.

## 6. Five consecutive outputs: exact lattice image

Now take $d=4$, so $q=x_0+x_1t+x_2t^2$.  The factorial condition in
(27) is



$$
u_0x_0+u_1x_1+u_2x_2=0,                 \tag{35}
$$



where



$$
\begin{aligned}
 u_0&=N^2+N+2,\\
 u_1&=(N+1)(N^2+3N+4),\\
 u_2&=(N+1)(N+2)(N^2+5N+8).                         \tag{36}
\end{aligned}
$$



Formula (29) becomes $K_N=z_0x_0+z_1x_1+z_2x_2$, with



$$
\begin{aligned}
 z_0&=-\frac{(N-1)(N+3)}{N+1},\\
 z_1&=-\frac{N^3+6N^2+14N+8}{N+2},\\
 z_2&=-\frac{N^4+11N^3+48N^2+99N+77}{N+3}.          \tag{37}
\end{aligned}
$$



Put



$$
\Omega=(N+1)(N+2)(N+3),qquad Z_i=\Omega z_i\in\mathbb Z.   \tag{38}
$$



We use the following elementary Smith lemma.  If $u,Z\in\mathbb Z^r$
and $u\ne0$, then



$$
\left\{\frac{Z\mathbin\cdot x}{\Omega}:
 x\in\mathbb Z^r, u\mathbin\cdot x=0\right\}
 =\frac{\Delta_2\binom{u}{Z}}
        {\Omega\Delta_1(u)}\mathbb Z.               \tag{39}
$$



Indeed, put the one-row matrix $u$ into Smith form by a unimodular column
operation.  Its integer kernel becomes the last $r-1$ coordinate axes;
the gcd of the corresponding coordinates of $Z$ is precisely the quotient
of determinantal divisors in (39).

Direct expansion gives the three $2$-minors in (39):



$$
\begin{aligned}
 u_0Z_1-u_1Z_0
 &=-(N+1)(N+3)A_0,\\
 u_0Z_2-u_2Z_0
 &=-(N+1)(N+2)A_1,\\
 u_1Z_2-u_2Z_1
 &=-(N+1)^2(N+2)A_2,                                \tag{40}
\end{aligned}
$$



where



$$
\begin{aligned}
 A_0&=5N^3+21N^2+50N+40,\\
 A_1&=5N^4+51N^3+201N^2+389N+298,\\
 A_2&=5N^3+36N^2+107N+116.                          \tag{41}
\end{aligned}
$$



## 7. Evaluation on the five-index sign window

Assume $N\equiv0\pmod8$.  From (36),



$$
\Delta_1(u)=2.                         \tag{42}
$$



For completeness, $u_0\equiv2\pmod8$, so the common $2$-adic valuation
is at most one; all three entries are even.  No odd common prime exists,
because $\operatorname {Res}(u_0,u_1)=16$.

Put



$$
\begin{aligned}
 B_0&=(N+3)A_0,\\
 B_1&=(N+2)A_1,\\
 B_2&=(N+1)(N+2)A_2.                                \tag{43}
\end{aligned}
$$



The exact resultants are



$$
\begin{aligned}
 |\operatorname {Res}(B_0,B_1)|&=2^{23}5^3\cdot71,\\
 |\operatorname {Res}(B_0,B_2)|&=2^{22}\cdot3\cdot5^2\cdot71. \tag{44}
\end{aligned}
$$



Hence an odd prime common to all three values must be $5$ or $71$.
There is no common root modulo $5$; modulo $71$, the unique common root is



$$
N\equiv16\pmod {71}.                    \tag{45}
$$



The exponent of $71$ is at most one by (44).  Finally, when
$N\equiv0\pmod8$, the exact $2$-adic valuations of
$B_0,B_1,B_2$ are $3,2,3$, respectively.  Therefore



$$
\gcd(B_0,B_1,B_2)=4\eta_N.              \tag{46}
$$



Combining (38)--(40), (42), and (46) proves



$$
\left\{K_N(p):p\in\mathbb Z[t],\ \deg p\le4,\ p\text{ satisfies (27)}
 \right\}
 =\frac{2\eta_N}{(N+2)(N+3)}\mathbb Z.              \tag{47}
$$



The generator in (47) is attained by an integer vector.  If its coefficient
gcd were larger than one, division by that gcd would produce a smaller
positive element of the same image.  Hence a primitive vector attains it,
proving (4)--(6).

If $\eta_N=71$, condition (45) gives
$N+2\equiv18$ and $N+3\equiv19\pmod {71}$.  Thus
$\gcd(\eta_N,Q_N)=1$.  Equation (7) follows in both cases.

There is also an exact-zero direction.  The lattice in (35) has rank two,
while its image (47) has rank one.  Its kernel therefore contains a nonzero
primitive vector.  This produces an identity



$$
\sum_{j=0}^4c_j{\cal L}_{N+j}(H)=0       \tag{48}
$$



for every common profile.  Extra output dimensions thus include tautological
zero relations; they cannot all be treated as nonzero small integers.

## 8. Denominator consequence and aggregate scope

Let $(\rho_N,\ldots,\rho_{N+4})$ be the five rational correction
coordinates of one shared integer profile, and let $D$ be any positive
integer clearing all five.  For the primitive vector attaining (5), the
factorial term cancels, so



$$
D\delta_N=\sum_{j=0}^4c_jD\rho_{N+j}
                         \in\mathbb Z.                         \tag{49}
$$



Since the reduced denominator of $\delta_N$ is $Q_N$, equation (49)
proves (8) unconditionally for the rational correction coordinates.

This divisor fits the raw clearing exactly.  The integers
$(N+2)/2$ and $N+3$ are coprime when $N\equiv0\pmod8$, and both are at
most $N+3$.  Therefore



$$
Q_N\mid\operatorname {lcm}(1,\ldots,N+3). \tag{50}
$$



For any finite collection of blocks, the lcm of their $Q_N$'s still
divides the global $\operatorname {lcm}(1,\ldots,N_{\max}+3)$.  Thus
aggregation cannot outrun the ordinary beta-moment denominator.  A useful
contradiction would require new numerator content beyond this exact Smith
divisibility.

## 9. Scope and replay

The all-parameter conclusions are:

* the exact beta-response factorization and Smith/minor formulas
  (12), (18)--(20);
* the complete profile-independent kernel description (21)--(29);
* the four-output quadratic-growth obstruction (32)--(34);
* the five-output primitive $O(N^{-2})$ construction (5);
* the exact reduced denominator and forced divisor (7)--(8);
* the existence of exact-zero relations and the aggregate-lcm obstruction.

Finite Smith tables in the replay are exact diagnostics for the displayed
matrices, but no finite pattern is extrapolated.  This source proves no
irrationality or transcendence result for $e+\pi$.

From the research directory run

    python3 scripts/common_kernel_multioutput_smith_quadratic_denominator_certificate.py

The replay uses memory-bounded exact integer, rational, and symbolic CPU
arithmetic.  A 40 GiB RAM guard is enforced; no accelerator is useful.

Pinned upstream manifests:

    559cc412db81ed449d4255654ad370f44a8ceb4d8acdce234a7f607d448ffcb7  results/common_kernel_native_output_bernstein_congruence_hashes.sha256
    b53b8e6f1855fe3eb7ef1b1eae1c303fad3b9cd5344462616606794fd0d9ce6d  results/common_kernel_finite_multimoment_exact_approximation_hashes.sha256
