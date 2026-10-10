> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Finite positive CRT channels cancel the full fixed correction residue

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
u=1+x^2,\qquad {\cal T}P=(1-x)P'-xP.
$$



Fix an arbitrary polynomial $K\in\mathbb Z[x]$, independently of the
large parameter below, and divide



$$
{\cal T}K=uG_0+(\alpha+\beta x),
 \qquad G_0\in\mathbb Z[x],\quad \alpha,\beta\in\mathbb Z.       \tag{1}
$$



This note constructs, for every sufficiently large integer $q$, an
integer polynomial $h_q$ such that



$$
\boxed{
 h_q\equiv1\pmod {u^2},\qquad h_q(0)=0,\qquad
 0\leq h_q(x)\leq1\quad(0\leq x\leq1).}                  \tag{2}
$$



Its order is exactly



$$
n_q=\operatorname {ord}_0h_q=20q,       \tag{3}
$$



and its degree is $48q+O_K(1)$.  Define



$$
r_q=\frac{h_q-1}{u},\qquad
 S_q=\frac{{\cal T}(h_qK)-{\cal T}K}{u},                 \tag{4}
$$



and the three rational coordinates



$$
I_{0,q}=\int_0^1r_q(x)\,dx,\qquad
 I_{1,q}=\int_0^1xr_q(x)\,dx,\qquad
 J_q=\int_0^1S_q(x)\,dx.                                \tag{5}
$$



Let $D_q$ be their least positive common clearing denominator.  There
are explicit constants $C_K\geq0$, $\Delta_K\geq1$, depending only
on $K$, for which



$$
\boxed{
 \gcd\!\left(
 D_q,
 \prod_{(48q+C_K)/3<p<20q}p
 \right)
 \ \bigm|\ 
 \Delta_K(40q^2+44q+5).}                                \tag{6}
$$



The product is over primes.  In particular its full Chebyshev mass is



$$
\sum_{(48q+C_K)/3<p<20q}\log p=4q+o(q),                \tag{7}
$$



whereas the possible surviving mass in (6) is only $O_K(\log q)$.
Thus a fixed finite number of nonnegative CRT coefficient channels
cancels asymptotically all of the one-third prime window simultaneously
from both defect moments and from the full fixed correction residue.

The number of channels is fixed once $K$ is fixed.  Every CRT
coefficient is an ordinary nonnegative integer; no rational scaling is
used.  Their total size costs only a fixed multiple of the same prime
product, while the positivity capacity has a strictly larger exponential
rate.

For a linear correction $K=k_0+k_1x$, a sharper conclusion uses only
two monomials.  Besides the moment channel $x$, the single channel
$x^2$ suffices when $k_0+k_1\ne0$, and the single channel $x^3$
suffices when $k_1=-k_0\ne0$.  The latter channel is intentionally
non-even.  This point reconciles the result with the earlier exact
linear-$K$ formula for **even** localizers; see Section 8.

The theorem concerns the three rational coordinates in (5).  It does
not control a correction $K$ whose degree grows with $q$, the
primitive content of an entire varying common-kernel form, or the sign
of a different residual after adding further terms.

This package proves neither irrationality nor transcendence of
$e+\pi$.

## 2. Base, padding, and residue classes

Use



$$
B_q=x^{20q}(5q+1-5qx^4),                               \tag{8}
$$





$$
w_q=x^{12q}(1-x^4)^{4q}(1-x^2).                        \tag{9}
$$



The identity



$$
y^m(m+1-my)-1
 =-(y-1)^2\sum_{j=0}^{m-1}(j+1)y^j                     \tag{10}
$$



with $m=5q,y=x^4$ proves $B_q\equiv1\pmod {u^2}$.
Moreover, $B_q$ increases from zero to one on $[0,1]$, because



$$
\frac d{dy}\{y^{5q}(5q+1-5qy)\}
 =5q(5q+1)y^{5q-1}(1-y)\geq0.                           \tag{11}
$$



Put



$$
V_q=x^{32q}(5q+1-5qx^4)(1-x^4)^{4q},                  \tag{12}
$$





$$
G_q=B_quw_q=V_q(1-x^4).                                \tag{13}
$$



Thus both $V_q$ and $G_q$ are supported only in degrees divisible
by four.

Every correction multiplier below has the form



$$
\boxed{
 h_q=B_q(1-u^2w_qC_q),}                                  \tag{14}
$$



where $C_q\in\mathbb Z_{\geq0}[x]$ is supported only in residue
classes $1,2,3\pmod4$.  Class zero is never used.  From (14),



$$
r_q=R_q-G_qC_q,
 \qquad R_q=\frac{B_q-1}{u}.                             \tag{15}
$$



Let $p<20q$ be an odd prime and put



$$
E=2p-2,\qquad O=2p-1,\qquad
 t=\frac{p-1}{2}-8q.                                    \tag{16}
$$



Then $E\equiv0\pmod4$, $O\equiv1\pmod4$.  Since no class-zero
monomial occurs in $C_q$, every correction term in (15) has zero
coefficient at $E$.  Only the class-one part of $C_q$ can contribute
at $O$.  This reserves classes two and three for the full correction
residue without disturbing either defect-moment equation.

Write



$$
V_q=x^{32q}\mathcal V_q(x^4),\qquad
 \mathcal V_q(y)=(5q+1-5qy)(1-y)^{4q}.                  \tag{17}
$$



If $C_q$ has class-one component $xC_1(x^4)$, then its moment
response at $O$ is



$$
[x^O]G_qC_q=[y^t]\mathcal V_q(y)(1-y)C_1(y).           \tag{18}
$$



## 3. Exact full-residue linearization

Define the fixed polynomial



$$
\boxed{
 H_K(x)=(1+x)(1-x^2)^2K(x).}                             \tag{19}
$$



It has a unique decomposition



$$
H_K(x)=H_0(x^4)+xH_1(x^4)+x^2H_2(x^4)+x^3H_3(x^4),    \tag{20}
$$



with $H_j\in\mathbb Z[y]$.

The response formula is most transparent directly from the Stein
operator.  If $\delta h=u^2Q$, then



$$
\frac{{\cal T}(\delta hK)}u
 =4x(1-x)QK+u(1-x)(QK)'-xuQK.                           \tag{21}
$$



For $L=QK=\sum L_jx^j$, its coefficient at an arbitrary index $N$
is



$$
(N+1)L_{N+1}-NL_N+(N+2)L_{N-1}
 -(N+2)L_{N-2}-L_{N-3}.                                 \tag{22}
$$



At $N=O=2p-1$, reduction modulo $p$ turns (22) into



$$
L_O+L_{O-1}-L_{O-2}-L_{O-3}
 =[x^O](1+x)(1-x^2)L.                                   \tag{23}
$$



In (14), $Q=-B_qw_qC_q=-V_q(1-x^2)C_q$.  Therefore



$$
\boxed{
 \delta s_O\equiv-[x^O]V_qH_KC_q\pmod p.}              \tag{24}
$$



If



$$
C_q=xC_1(x^4)+x^2C_2(x^4)+x^3C_3(x^4),                \tag{25}
$$



then (20), (24), and the residue-one target give



$$
\boxed{
 [x^O]V_qH_KC_q
 =[y^t]\mathcal V_q
 \{H_0C_1+yH_3C_2+yH_2C_3\}.}                          \tag{26}
$$



This is the promised two-row system: (18) is the moment row and (26) is
the full-output row.

There is no hidden low-degree term.  For fixed $K$, and all sufficiently
large $q$, the unmodified polynomial



$$
S_{B,q}=\frac{{\cal T}(B_qK)-{\cal T}K}{u}
$$



has degree at most $20q+O_K(1)<O$.  Also $p<n_q$, the forced prefix
of $r_q$ gives



$$
[x^{p-1}]S_q=\varepsilon_p\alpha,
 \qquad \varepsilon_p=(-1)^{(p+1)/2}.                   \tag{27}
$$



Thus the exact full-residue target is



$$
\boxed{
 [x^O]V_qH_KC_q\equiv2\varepsilon_p\alpha\pmod p.}     \tag{28}
$$



Indeed, (24) then gives
$2s_{p-1}+s_O\equiv0\pmod p$.

## 4. A finite coefficient-block lemma

The following elementary lemma supplies all needed ranks.

**Lemma.**  Let $F\in\mathbb Z[y]$ be nonzero modulo an odd prime
$p$.  Put $n=4q$,



$$
U_k=[y^k](5q+1-5qy)(1-y)^nF(y),                         \tag{29}
$$



and let



$$
e=\deg F+1.
$$



Assume $e<n$ and $p>n+e$.  Among any $e+1$ consecutive coefficients $U_k$
whose indices lie in $[0,n]$, at least one is nonzero modulo $p$.

To prove the lemma, write



$$
(5q+1-5qy)F(y)=\sum_{j=0}^e a_jy^j.                   \tag{30}
$$



For $0\leq k\leq n$, $\binom nk$ is a $p$-unit and



$$
\frac{U_k}{(-1)^k\binom nk}
 =\sum_{j=0}^e
 a_j(-1)^j\frac{(k)_j}{(n-k+1)_j}.                     \tag{31}
$$



After multiplication by



$$
\prod_{r=1}^e(n-k+r),            \tag{32}
$$



the right side is a polynomial in $k$ of degree at most $e$.
Every factor in (32) is a $p$-unit on $[0,n]$.

The resulting polynomial is not identically zero modulo $p$.  If it
were, (31) would make all coefficients in degrees $0,\ldots,n$ of
the nonzero product in (29) vanish.  But the first nonzero coefficient
of the polynomial in (30) occurs in degree at most $e<n$, and survives
unchanged after multiplication by $(1-y)^n$.  This is a contradiction.
A nonzero degree-$e$ polynomial has at most $e$ roots, proving the
lemma.

Notice that this is an all-parameter finite-field statement.  It does
not treat coefficients at different primes as random or independent.

## 5. The fixed channel set

This section gives explicit constants and channels.  Use
$\deg0=-\infty$, and put $k_K=\max\{0,\deg K\}$.

### Case A: an unused residue component is nonzero

If $H_3\ne0$, take



$$
F=H_3,\qquad \rho=2.
$$



If $H_3=0$ but $H_2\ne0$, take



$$
F=H_2,\qquad \rho=3.
$$



Put



$$
e_K=\deg F+1,\qquad
 \mathscr C_K=\{x\}\cup
 \{x^{\rho+4a}:0\leq a\leq e_K\}.                     \tag{33}
$$



Let $\Delta_K$ be the positive content of $F$.  Set



$$
s_K=\rho+4e_K,\qquad \tau_K=e_K+1.                     \tag{34}
$$



The class-one coefficient of $x$ first solves (18).  By the lemma,
the $e_K+1$ coefficients



$$
[y^{t-1-a}]\mathcal V_qF,\qquad 0\leq a\leq e_K,      \tag{35}
$$



cannot all vanish when $t\geq\tau_K$, $p\nmid\Delta_K$, and
$q$ is sufficiently large.  One class-$\rho$ coefficient then
solves (28).  It does not change (18).

### Case B: only the class-zero response remains

Suppose



$$
H_2=H_3=0,\qquad H_0\notin\mathbb Q\!\cdot\!(1-y).  \tag{36}
$$



Put



$$
e_K=\max\{\deg H_0,1\}+1,\qquad
 \mathscr C_K=\{x^{1+4a}:0\leq a\leq e_K\}.            \tag{37}
$$



Write $H_0=\sum h_jy^j$.  Since (36) holds, at least one integer in



$$
h_0+h_1, h_2, h_3,\ldots       \tag{38}
$$



is nonzero.  Define $\Delta_K$ as the absolute value of the first
fixed nonzero entry in this list.  Put



$$
s_K=1+4e_K,\qquad \tau_K=e_K.                           \tag{39}
$$



For the channel $x^{1+4a}$, the two response columns are



$$
m_a=[y^{t-a}]\mathcal V_q(1-y),\qquad
 f_a=[y^{t-a}]\mathcal V_qH_0.                           \tag{40}
$$



The first moment entry $m_0$ will be a unit.  If every two-by-two
minor with column zero vanished, put $\lambda=f_0/m_0$ in
$\mathbb F_p$.  Then



$$
[y^{t-a}]\mathcal V_q\{H_0-\lambda(1-y)\}=0
 \quad(0\leq a\leq e_K).                                \tag{41}
$$



Because $p\nmid\Delta_K$, the filter in braces is nonzero modulo
$p$.  Equation (41) contradicts the coefficient-block lemma.  Hence
the two rows have rank two, and the two targets (18), (28) can be solved
simultaneously.

### Case C: the apparently proportional case is automatic

Suppose



$$
H_2=H_3=0,\qquad
 H_0=\lambda(1-y)\quad(\lambda\in\mathbb Q).           \tag{42}
$$



In fact $\lambda=0$, $\alpha=\beta=0$, and there is no independent
full-output equation.

Here is the exact structural proof.  Write



$$
H_K=\lambda(1-x^4)+xQ(x^4).                             \tag{43}
$$



By definition, $H_K$ is divisible by



$$
(1+x)(1-x^2)^2=(1-x)^2(1+x)^3.                         \tag{44}
$$



The double zero at $x=1$ gives $Q(1)=0,Q'(1)=\lambda$.
The first derivative at the triple zero $x=-1$ is then
$8\lambda$, so $\lambda=0$.  The remaining multiplicity implies



$$
Q(y)=(1-y)^3R(y),\qquad R\in\mathbb Z[y],               \tag{45}
$$



and division in (44) gives



$$
\boxed{
 K=x(1-x)(1+x^2)^3R(x^4).}                               \tag{46}
$$



Thus ${\cal T}K$ is divisible by $u$, so $\alpha=\beta=0$.
Take



$$
\mathscr C_K=\{x\},\qquad
 \Delta_K=1,\qquad s_K=1,\qquad \tau_K=2.              \tag{47}
$$



The full response in (26) is identically zero and its target in (28) is
also zero.  Only the moment row remains.

Finally, in all three cases define the explicit fixed constant



$$
\boxed{
 C_K=\max\{10+s_K+k_K,\ 6\tau_K-3\}.}                   \tag{48}
$$



## 6. Primewise solvability and CRT

Define



$$
\mathcal P_{q,K}=\left\{p\text{ prime}:
 \frac{48q+C_K}{3}<p<20q,\quad
 p\nmid\Delta_K(40q^2+44q+5)\right\}.                  \tag{49}
$$



For $p\in\mathcal P_{q,K}$, (16) and (48) imply



$$
t\geq\tau_K.                    \tag{50}
$$



Also $t\leq2q-1$, so all coefficient blocks used above lie in
$[0,4q]$ for sufficiently large $q$.

The first moment coefficient is



$$
\begin{aligned}
 g_p
 &=[y^t](5q+1-5qy)(1-y)^{4q+1}\\
 &=(-1)^t\binom{4q+1}{t}
   \frac{(5q+1)(4q+2)-t}{4q+2-t}.                       \tag{51}
\end{aligned}

All displayed factorials and denominators are \(p\)-units.  Since

\[
 2\{(5q+1)(4q+2)-t\}=40q^2+44q+5-p,                    \tag{52}
$$



one has



$$
g_p\ne0\pmod p.                 \tag{53}
$$



In Case A, set the local residue of the $x$-coefficient to



$$
c_1=2\varepsilon_pg_p^{-1}.      \tag{54}
$$



Choose one nonzero response in (35), set every other auxiliary local
residue to zero, and solve (28) for the chosen residue.  In Case B,
choose a nonzero two-by-two minor proved above, set all other local
residues to zero, and solve the two equations with right side



$$
(2\varepsilon_p,2\varepsilon_p\alpha).    \tag{55}
$$



In Case C, use only (54).

Let



$$
P_{q,K}=\prod_{p\in\mathcal P_{q,K}}p.     \tag{56}
$$



Apply the ordinary Chinese remainder theorem independently to each
fixed channel and take its least nonnegative representative.  Every
coefficient of $C_q$ then lies in $[0,P_{q,K})$.  At least one is
positive because the first target in (55) is nonzero and
$\mathcal P_{q,K}\ne\varnothing$ for all sufficiently large $q$.

The prime number theorem gives



$$
\log P_{q,K}=4q+o(q).                                   \tag{57}
$$



Indeed, the fixed endpoint shift in (49) changes the interval mass by
only $o(q)$, while all excluded primes divide one integer of size
$O_K(q^2)$, and hence have total logarithmic mass $O_K(\log q)$.

## 7. Positivity and all three residue equations

Let $N_K=|\mathscr C_K|$.  On $[0,1]$,



$$
0\leq C_q(x)<N_KP_{q,K}.         \tag{58}
$$



For $z=x^4$,



$$
\max_{0\leq z\leq1}z^{3q}(1-z)^{4q}
 =\left(\frac37\right)^{3q}
  \left(\frac47\right)^{4q}.                           \tag{59}
$$



Set



$$
Q_q=\frac{7^{7q}}{4\,3^{3q}4^{4q}}.                   \tag{60}
$$



The strict entropy margin is



$$
\Gamma=7\log7-3\log3-4\log4-4>0,                     \tag{61}
$$



because $7^7/(3^3 4^4)>81>e^4$.  Equations (57), (60), and
(61) give



$$
Q_q/(N_KP_{q,K})\longrightarrow\infty.    \tag{62}
$$



Since $u^2\leq4$, $x\leq1$, and $1-x^2\leq1$, equations
(58)--(62) imply, for every sufficiently large $q$,



$$
0\leq u^2w_qC_q\leq1.           \tag{63}
$$



Together with $0\leq B_q\leq1$, this proves (2).  The second factor
in (14) has constant term one, so the order in (3) is exact.  If
$s_K$ is the largest channel exponent, then



$$
\deg h_q\leq48q+10+s_K.          \tag{64}
$$



For a target prime, $E>\deg R_q=20q+2$.  Equations (15), (18), and
(54)--(55) give



$$
r_E\equiv0,\qquad
 2r_{p-1}+r_O\equiv0\pmod p.                            \tag{65}
$$



The forced odd coefficient $r_{p-2}=0$ and the exact one-third-window
criterion show that both $I_{0,q}$ and $I_{1,q}$ are $p$-integral.

For the full channel, (24), (27), (28), and (55) give



$$
2s_{p-1}+s_O\equiv0\pmod p.     \tag{66}
$$



Moreover,



$$
\deg S_q+1
 \leq\deg h_q+k_K
 \leq48q+C_K<3p.                                        \tag{67}
$$



Thus only the monomial denominators $p$ and $2p$ can carry $p$
in $J_q$, and (66) is exactly its $p$-integrality criterion.

Every prime in $\mathcal P_{q,K}$ is consequently absent from $D_q$.
The remaining primes in the displayed interval (6) divide
$\Delta_K(40q^2+44q+5)$.  Since the interval product is squarefree,
(6) follows.  Equations (7) and (57) show that the cancelled fraction
of its Chebyshev mass tends to one.

When $K\ne0$, the actual one-third window based on $\deg S_q$
differs from the conservative window in (49) by only $O_K(1)$ in its
endpoint.  Hence its additional possible prime mass is only
$O_K(\log q)$; the same asymptotic full-window conclusion holds there
as well.  When $K=0$, the full correction residue is identically zero
and only the two moment coordinates remain.

## 8. Exact reconciliation with the even linear formula

Let



$$
K=k_0+k_1x.                      \tag{68}
$$



Then



$$
\alpha=2k_1,\qquad \beta=-(k_0+k_1),                   \tag{69}
$$



and the relevant residue components of (19) are



$$
\begin{aligned}
 H_2(y)&=(-2k_0+k_1)+k_1y,\\
 H_3(y)&=-2(k_0+k_1).                                    \tag{70}
\end{aligned}
$$



Write



$$
v_j=[y^j](5q+1-5qy)(1-y)^{4q}.                         \tag{71}
$$



The response of the single $x^2$ channel is



$$
a_2=-2(k_0+k_1)v_{t-1}.          \tag{72}
$$



For $k_0+k_1\ne0$, this is a unit outside primes dividing the fixed
coefficient and



$$
40q^2+34q+5,                    \tag{73}
$$



because



$$
v_{t-1}=(-1)^{t-1}\binom{4q}{t-1}
 \frac{(5q+1)(4q+1)-(t-1)}{4q+2-t}.                     \tag{74}
$$



If $k_1=-k_0\ne0$, the response (72) vanishes, but the single
$x^3$ channel has response



$$
a_3=-k_0(3v_{t-1}+v_{t-2}).      \tag{75}
$$



After clearing the displayed $p$-unit binomial and denominator, (75)
vanishes only if $p$ divides



$$
\boxed{
 1760q^3+1976q^2+644q+63.}                              \tag{76}
$$



Indeed the remaining numerator before substituting
$2t=p-16q-1$ is



$$
240q^3-80q^2t+308q^2-48qt+114q+4t^2-19t+21,            \tag{77}
$$



and four times (77) reduces modulo $p$ to twice (76).

Put $q_h=(h-1)/u^2$.  The earlier formula



$$
s_{2p-1}\equiv
 (k_0+k_1)((q_h)_{2p-2}-(q_h)_{2p-4})\pmod p            \tag{78}
$$



was proved in a section whose standing hypothesis was that $h$ is
even.  Under that hypothesis, $(h-1)G_0$ has no odd coefficient and
$q_h=(h-1)/u^2$ is even.  The $x^2$ channel preserves evenness, so
(72) agrees with (78).



$$
\boxed{\text{Identity (78) is an even-\(h\)-only identity.}}       \tag{79}
$$



The $x^3$ channel in (75) deliberately makes $h$ non-even.  The
odd coefficient of $(h-1)G_0$, together with the corresponding
derivative coefficient, is then nonzero and is exactly included in the
general operator calculation (21)--(24).  Applying (78) after adding an
$x^3$ channel would therefore drop a term under a hypothesis which no
longer holds.  There is no contradiction and no omitted fixed
$2s_{p-1}$ term: equation (28) explicitly sets the varying high
coefficient to the negative of that fixed low contribution.

## 9. Scope and replay

The deterministic replay includes three structurally different fixed
corrections:

* a generic linear correction, where an unused class-two channel works;
* the exceptional linear direction $K=1-x$, where the class-two
  response vanishes and a non-even class-three channel works;
* both subcases with $H_2=H_3=0$: a nonproportional class-zero filter,
  and the automatic structural family (46).

It verifies the operator identity coefficient by coefficient, the
two-row response decomposition, every modular system, ordinary CRT,
positivity with exact integers, degree/order, the three reduced rational
coordinates, and the even/non-even term decomposition.

From the research directory run

    python3 scripts/common_kernel_positive_crt_full_correction_certificate.py
    sha256sum -c results/common_kernel_positive_crt_full_correction_hashes.sha256

The coefficient-block lemma, prime number theorem step, and all
sufficiently-large quantifiers are proved above, not extrapolated from
the replay instances.

The replay uses exact CPU arithmetic, no hardware accelerator, and a
negligible fraction of the available Colab RAM.  No conclusion about
$e+\pi$ is claimed.
