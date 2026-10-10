> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The forced odd-frequency next coefficient

## A positive simple-pole cancellation theorem and the exact Euler-border obstruction

Checked: 2026-08-27 UTC

## 1. Scope and verdict

This note treats the only parity-forced top-zero family not covered by the
even-frequency constant-term argument:



$$
m=2k+1\ge3,\qquad n\text{ even},\qquad
 D=2d+1\text{ odd},\qquad n\ge D.                           \tag{1}
$$



Put $h=n+1$, $c=k$,



$$
P(X)=\prod_{j=0}^{2k}(X-j),\qquad \Phi=P^h,                \tag{2}
$$



and retain the centered endpoint matrix and Hermite cardinals from the
top-cardinal theorem.  The top coefficient of $\Gamma$ is structurally
zero.  The next coefficient is



$$
[z^{n+D-1}]\Gamma\ \doteq\
 \det\!\begin{pmatrix}K\\e_D^T\\E_{n-1}\end{pmatrix}
 +\det\!\begin{pmatrix}K\\e_{D-1}^T\\E_n\end{pmatrix}.    \tag{3}
$$



Here $\doteq$ means equality after division by the same nonzero endpoint
Plücker factor; its sign is retained in both displayed summands.  The exact
factor-free identity used for the sign audit is (7).

The two determinants in (3) have opposite signs in exact grids.  This note
does **not** prove their sum nonzero for every parameter.  It proves two new
all-parameter facts which substantially sharpen the remaining problem.

1. The derivative difference
   

$$
F=\Lambda_{n-1}-\Lambda_n'                               \tag{4}
$$


   is divisible by $P^n$, and after centering its quotient $F/\Phi$
   is a strict positive Stieltjes function with only the noncentral simple
   rates $1,4,\ldots,k^2$.  The double poles in
   $\Lambda_{n-1}/\Phi$ and the central pole cancel exactly.
2. Integrating every odd column one step less puts both parity blocks over
   the same even derivative-polynomial column basis.  The odd ordinary rows
   are obtained from the even rows by the positive Euler multiplier
   

$$
\mathcal E=2x\frac d{dx}+n+2.                            \tag{5}
$$


   The entire open problem becomes one normalized determinant-ratio
   inequality for this multiplier.  The imaginary-axis phases and the
   relative sign of the two parity blocks are tracked explicitly below.

There is also an exact endpoint identity.  Normalize the unique even and odd
endpoint polynomials by



$$
[z^{D-1}]C=1,\qquad[z^D]D=1,                               \tag{6}
$$



and put $R_*(z)=D(z)-zC(z)$.  Then



$$
\boxed{
 [z^{n+D-1}]\Gamma
 =\mathcal L\!\left(
 C(\partial)F-R_*(\partial)\Lambda_n\right).}               \tag{7}
$$



On every exact grid tested, the two terms on the right of (7) have opposite
signs and therefore reinforce after the displayed subtraction.  Equivalently,
the Euler-border remainder has the sign opposite to the positive-Stieltjes
border.  The missing theorem is this opposite-sign assertion for all
parameters, not a quantitative upper bound between the two original
summands.

No conclusion about $e+\pi$ is claimed here.

The replayable files are

* `scripts/root_unity_gamma_forced_odd_m_next_coefficient_certificate.py`;
* `results/root_unity_gamma_forced_odd_m_next_coefficient_certificate.json`.

## 2. Exact pole cancellation

Index the centered nodes by $r=-k,\ldots,k$, so $X=k+U$.  Since $n$
is even and $h$ is odd, the top-cardinal residues have no alternating
sign:



$$
w_r=\frac1{n![(k+r)!(k-r)!]^h} >0.                         \tag{8}
$$



Thus



$$
R(U):=\frac{\Lambda_n(k+U)}{\Phi(k+U)}
 =\sum_{r=-k}^{k}\frac{w_r}{U-r}.                           \tag{9}
$$



Let



$$
H_r^*=H_{k+r}-H_{k-r}
       =\sum_{s\ne r}\frac1{r-s}.                           \tag{10}
$$



The exact double-pole formula for the penultimate cardinal becomes



$$
S(U):=\frac{\Lambda_{n-1}(k+U)}{\Phi(k+U)}
 =\sum_{r=-k}^{k}\left{
 \frac{nw_r}{(U-r)^2}-\frac{nhH_r^*w_r}{U-r}
 \right}.                                                   \tag{11}
$$



Since



$$
\frac{\Lambda_n'}{\Phi}=R'+\frac{\Phi'}{\Phi}R,           \tag{12}
$$



the double coefficient at $r$ on the right of (12) is
$(h-1)w_r=nw_r$, exactly the double coefficient in (11).
Hence $F/\Phi$ has only simple poles.  Its residue at $U=r$ is



$$
\boxed{
 \eta_r=-h\left(
 hH_r^*w_r+\sum_{s\ne r}\frac{w_s}{r-s}
 \right).}                                                   \tag{13}
$$



Symmetry gives $\eta_0=0$ and $\eta_{-r}=-\eta_r$.  Therefore the
central pole cancels and there is a rational function $\psi$ with



$$
\frac{F(k+U)}{\Phi(k+U)}=\psi(-U^2),\qquad
 \psi(x)=\sum_{r=1}^{k}\frac{c_r}{x+r^2},                  \tag{14}
$$



where



$$
\boxed{
 c_r=-2r\eta_r
 =2rh\left(
 h(H_{k+r}-H_{k-r})w_r+
 \sum_{s\ne r}\frac{w_s}{r-s}
 \right).}                                                   \tag{15}
$$



## 3. Every residue in (15) is strictly positive

The weights are symmetric and strictly decrease with distance from zero:



$$
w_{-s}=w_s,qquad w_0>w_1>\cdots>w_k>0.                   \tag{16}
$$



For $1\le r\le k$, pair the negative-denominator terms in the regular
part of (15) with their reflections about $r$:



$$
\begin{aligned}
 \sum_{s\ne r}\frac{w_s}{r-s}
 &=\sum_{t=1}^{k-r}\frac{w_{r-t}-w_{r+t}}t
   +\sum_{t=k-r+1}^{k+r}\frac{w_{r-t}}t.                   \tag{17}
 \end{aligned}
$$



Every term is strictly positive.  In the first sum,
$|r-t|<r+t$, so (16) gives $w_{r-t}>w_{r+t}$; the second sum is
manifestly positive.  Also $H_{k+r}-H_{k-r}>0$.  Thus



$$
\boxed{c_r>0\qquad(1\le r\le k).}                         \tag{18}
$$



Equations (14) and (18) prove that $\psi$ is strictly completely
monotone on $(0,\infty)$.  In particular, the even parity block augmented
by $F$ is a strictly signed divided-difference determinant, by exactly the
Andreief argument used in the top-cardinal theorem.

The pairing proof in (17) is more general than needed: it applies to any
strictly positive symmetric sequence decreasing in $|s|$.

## 4. The exact endpoint decomposition

For a coefficient polynomial $A(z)=\sum_a a_az^a$, write



$$
A(\partial)Q=\sum_a a_aQ^{(a)}.                            \tag{19}
$$



The cardinal-row formula is



$$
[z^b]\beta_A=-\mathcal L(A(\partial)\Lambda_b).            \tag{20}
$$



In (1), the endpoint kernel is one even line and one odd line.  With the
normalization (6), only two products contribute to degree $n+D-1$:



$$
\begin{aligned}
 [z^{n+D-1}]\Gamma
 &= [z^n]\beta_D-[z^{n-1}]\beta_C\\
 &=\mathcal L\!\left(C(\partial)\Lambda_{n-1}
                    -D(\partial)\Lambda_n\right).          \tag{21}
 \end{aligned}
$$



Multiplication of a coefficient polynomial by $z$ differentiates its
operator argument:



$$
(zC)(\partial)\Lambda_n=C(\partial)\Lambda_n'.             \tag{22}
$$



Substituting $D=zC+R_*$ into (21) proves (7) exactly.

The first term in (7) is the positive-Stieltjes augmented border from
Sections 2--3.  The remaining sign is concentrated in the lower odd
polynomial $R_*$, whose degree is at most $D-2$.

## 5. Common-column reduction and exact phases

Let



$$
x=t^2,\qquad Y(t)=\coth^2(\pi t),\qquad
 V(x)=\prod_{r=1}^{k}(x+r^2)^h.                             \tag{23}
$$



Write the even csch derivative polynomials as



$$
H_{2v}(\coth(\pi t))=Q_v(Y(t)),\qquad\deg Q_v=v.           \tag{24}
$$



Use the positive pairing



$$
\langle f,Q_v\rangle=
 2\int_0^\infty
 f(t^2)Q_v(Y(t))\frac{t^h}{\sinh(\pi t)}\,dt.               \tag{25}
$$



Put



$$
A_u=x^uV(x),\qquad
 G_u=\mathcal E A_u,\qquad
 \mathcal E=2x\frac d{dx}+h+1.                             \tag{26}
$$



Integrating an odd column $a=2v+1$ only $a-1=2v$ times gives



$$
\frac d{dt}\{t^{h+1}A_u(t^2)\}
 =t^h(\mathcal EA_u)(t^2).                                  \tag{27}
$$



Thus the even ordinary block uses rows $A_u$, while the odd ordinary
block uses rows $G_u$, both against the same columns $Q_v$.

Define the $d$-by-$(d+1)$ matrices



$$
M_A=(\langle A_u,Q_v\rangle),\qquad
 M_G=(\langle G_u,Q_v\rangle),
 \quad0\le u<d,\quad0\le v\le d.                           \tag{28}
$$



For any row function $f$, define the normalized borders



$$
\operatorname {NB}_A(f)=
 \frac{\det\!\begin{pmatrix}M_A\\(\langle f,Q_v\rangle)_v\end{pmatrix}}
      {\det\!\begin{pmatrix}M_A\\e_d^T\end{pmatrix}},
 \qquad
 \operatorname {NB}_G(f)=
 \frac{\det\!\begin{pmatrix}M_G\\(\langle f,Q_v\rangle)_v\end{pmatrix}}
      {\det\!\begin{pmatrix}M_G\\e_d^T\end{pmatrix}}.    \tag{29}
$$



Both denominators are nonzero by endpoint normality.

The phases can be tracked without ambiguity.  Set



$$
A_\Phi=i^h(-1)^{kh},\qquad
 C_*=\frac{(-1)^kiA_\Phi}{2}
 =\frac12(-1)^{k+kh+(h+1)/2}\ne0.                          \tag{30}
$$



Then



$$
\begin{aligned}
 K_{2u,2v}&=C_* (-1)^{u-v}\pi^{2v}\langle A_u,Q_v\rangle,\\
 K_{2u+1,2v+1}&=C_* (-1)^{u-v}\pi^{2v}\langle G_u,Q_v\rangle.
                                                                    \tag{31}
 \end{aligned}
$$



Define the positive Stieltjes function $\rho$ and the signed rational
function $\sigma$ by



$$
\begin{aligned}
 \rho(x)&=\frac{w_0}{x}+2\sum_{r=1}^k\frac{w_r}{x+r^2}>0,\\
 \Lambda_n(k+it)&=-A_\Phi i\,t^{h+1}V(t^2)\rho(t^2),\\
 \Lambda_{n-1}(k+it)&=A_\Phi t^hV(t^2)\sigma(t^2).
                                                                    \tag{32}
 \end{aligned}
$$



The extra rows are



$$
\begin{aligned}
 E_{n-1,2v}&=-C_* (-1)^v\pi^{2v}
              \langle V\sigma,Q_v\rangle,\\
 E_{n,2v+1}&= C_* (-1)^v\pi^{2v}
              \langle\mathcal E(V\rho),Q_v\rangle.        \tag{33}
 \end{aligned}
$$



After the same column factors are removed, either raw coordinate row becomes
$(-1)^d\pi^{-2d}e_d^T$.  Consequently the two algebraic bordered ratios
have opposite prefactors:



$$
\begin{aligned}
 \frac{\det(K^{\rm e};E_{n-1})}{\det(K^{\rm e};e_{2d})}
 &=(-1)^{d+1}C_*\pi^{2d}\operatorname {NB}_A(V\sigma),\\
 \frac{\det(K^{\rm o};E_n)}{\det(K^{\rm o};e_{2d+1})}
 &=(-1)^dC_*\pi^{2d}
   \operatorname {NB}_G(\mathcal E(V\rho)).                \tag{34}
\end{aligned}
$$



Finally, (4) is exactly the real-row identity



$$
\boxed{V\sigma=V\psi-\mathcal E(V\rho).}                 \tag{35}
$$



The minus signs in (32) and (35) are forced by



$$
\frac{\Lambda_n(k+it)}{\Phi(k+it)}=-it\rho(t^2),\qquad
 \frac d{dX}\bigg|_{X=k+it}=-i\frac d{dt}.                \tag{35a}
$$



For direct comparison with the endpoint identity, put



$$
\alpha=(-1)^dC_*\pi^{2d}.
$$



The normalized endpoint null vectors in the common-column basis then give



$$
\begin{aligned}
 \mathcal L(C(\partial)F)
 &=\alpha\operatorname {NB}_A(V\psi),\\
 \mathcal L(C(\partial)\Lambda_n')
 &=-\alpha\operatorname {NB}_A(\mathcal E(V\rho)),\\
 \mathcal L(D(\partial)\Lambda_n)
 &=-\alpha\operatorname {NB}_G(\mathcal E(V\rho)).
                                                               \tag{35b}
 \end{aligned}
$$



Thus



$$
\mathcal L(R_*(\partial)\Lambda_n)
 =\alpha\left\{
 \operatorname {NB}_A(\mathcal E(V\rho))-
 \operatorname {NB}_G(\mathcal E(V\rho))\right\}.         \tag{35c}
$$



Equations (34) and (35b) are also consistent with the block permutation in
(3): after the common endpoint Plücker factor is removed, the even bordered
ratio enters with a minus sign and the odd bordered ratio with a plus sign.
There is therefore no untracked phase or scale in the remaining comparison.

## 6. The isolated Euler-multiplier theorem still needed

Equations (7) and (35b)--(35c) reduce the normalized next coefficient to the
sign of

 

$$
\boxed{
 \operatorname {NB}_A(V\psi)+
 \operatorname {NB}_G(\mathcal E(V\rho))-
 \operatorname {NB}_A(\mathcal E(V\rho)).}                 \tag{36}
$$



The first term is strictly positive by (14)--(18), with the normalization
(29).  Exact grids show



$$
\operatorname {NB}_A(\mathcal E(V\rho))
 <\operatorname {NB}_G(\mathcal E(V\rho)),                 \tag{36a}
$$



so the two terms in (36) reinforce.  Proving the weak inequality in (36a)
for all $k,n,d$ would close (3), since the first term is already strict;
no quantitative magnitude comparison would then be needed.

In monomial coefficients, $\mathcal E$ is the positive increasing diagonal
multiplier



$$
[x^j]\mathcal Ef=(2j+h+1)[x^j]f.                           \tag{37}
$$



The Laurent exponent $j=-1$ occurring in $V\rho$ has multiplier
$h-1=n>0$.  Moreover, with the positive convention fixed in (32),



$$
V\rho=\frac{w_0V}{x}+
       2\sum_{r=1}^{k}w_r\frac{V}{x+r^2},                  \tag{38}
$$



so it is a positive combination of divisor polynomials and one shifted
divisor.  The coefficient Toeplitz matrix of $V$ is totally nonnegative.
These facts make a Cauchy--Binet multiplier-sequence proof plausible, but the
needed normalized-ratio inequality is not inserted here without proof.

The formal adjoint does not give a finite triangular shortcut.  With



$$
w(x)=\frac{x^{(h-1)/2}}{\sinh(\pi\sqrt x)},                \tag{39}
$$



integration by parts gives



$$
\mathcal E^*Q(Y)=
 \pi\sqrt x\coth(\pi\sqrt x)
 \{Q(Y)+2(Y-1)Q'(Y)\}.                                     \tag{40}
$$



The bracket is the next odd derivative polynomial, but the prefactor
$\sqrt x\coth(\pi\sqrt x)$ is not a polynomial in $Y$.  Thus a genuine
multiplier or sign-regularity theorem is required.

### 6.1 The naive augmented-TN shortcut is false

It is not enough to prepend the Euler row to the totally nonnegative
coefficient lace of $V$.  The smallest polewise example already fails.
Take $k=1,h=5$, so $V=(x+1)^5$, and put



$$
W=\frac{V}{x+1}=(x+1)^4,\qquad b=\mathcal EW.
$$



In coefficient columns $x^0,x^1$, the two rows $b,V$ begin



$$
\begin{pmatrix}6&32\\1&5\end{pmatrix},qquad
 \det\begin{pmatrix}6&32\\1&5\end{pmatrix}=-2.           \tag{40a}
$$



Thus $(b,A_0,G_0,A_1,G_1,\ldots)$ is not totally nonnegative, even for a
single positive divisor.  The desired normalized-border inequality can
still hold--and does hold on every exact grid recorded here--but it cannot
be deduced by applying a generic flag-minor lemma to that augmented
coefficient matrix.

### 6.2 An exact biorthogonal Markov-transform criterion

There is a sharper post-pairing formulation.  Put



$$
z=\operatorname {csch}^2(\pi\sqrt x)=Y-1,qquad
 g(x)=\pi\sqrt x\coth(\pi\sqrt x),qquad
 T=1+2z\frac d{dz},                                      \tag{40b}
$$



and



$$
d\nu(x)=\frac{x^{(h-1)/2}}{\sinh(\pi\sqrt x)}\,dx.
$$



Equation (40) becomes, for every polynomial $p$,



$$
\langle\mathcal Ef,p(z)\rangle
 =\int_0^\infty g(x)f(x)(Tp)(z(x))\,d\nu(x).             \tag{40c}
$$



This applies to all row functions used below.  At infinity the exponential
factor kills the polynomial rows.  At zero the worst case is the central
row $f=V/x$ together with $\deg p=d$; the integration-by-parts boundary
term is
$O(x^{(h-2)/2-d})=o(1)$, because (1) gives $h\ge2d+3$.

Let $p_\nu$ and $p_{g\nu}$ be the monic degree-$d$ biorthogonal
polynomials characterized by



$$
\begin{aligned}
 \int_0^\infty x^uV(x)p_\nu(z(x))\,d\nu(x)&=0,\\
 \int_0^\infty x^uV(x)g(x)p_{g\nu}(z(x))\,d\nu(x)&=0,
 \qquad 0\le u<d.                                       \tag{40d}
 \end{aligned}
$$



If $\ell_d>0$ is the leading coefficient of $Q_d(1+z)$, set



$$
q_\nu=\frac{Tp_\nu}{2d+1},
$$



which is again monic.  For one of the pole parameters
$a\in\{0,1^2,\ldots,k^2\}$, put $W=V/(x+a)$; this is a Laurent
polynomial for $a=0$ and a polynomial otherwise.  Put
$b=\mathcal EW$.  Directly from
(29), the endpoint-normalized null polynomial for $M_A$ is
$\ell_d p_\nu$.  For $M_G$, applying $T$ to its endpoint-normalized
null polynomial gives $\ell_d(2d+1)p_{g\nu}$.  Hence (40c) gives



$$
\begin{aligned}
 \operatorname {NB}_A(\mathcal EW)
 &=\ell_d(2d+1)\int_0^\infty gW q_\nu\,d\nu,\\
 \operatorname {NB}_G(\mathcal EW)
 &=\ell_d(2d+1)\int_0^\infty gWp_{g\nu}\,d\nu.
                                                               \tag{40e}
 \end{aligned}
$$



Consequently,



$$
\boxed{
 \operatorname {NB}_A(b)-\operatorname {NB}_G(b)
 =\ell_d(2d+1)\int_0^\infty
 g(x)W(x)\{q_\nu(z(x))-p_{g\nu}(z(x))\}\,d\nu(x).}       \tag{40f}
$$



Therefore the still-needed polewise statement is the Cauchy/Markov-transform
inequality



$$
\int_0^\infty
 gW(q_\nu-p_{g\nu})\,d\nu\le0.                            \tag{40g}
$$



Linearity would then prove (36a) for every positive Stieltjes $\rho$, in
particular for (32).  The polynomials inside (40g) need not have one
pointwise sign; hence (40g), rather than coefficientwise domination, is the
correct remaining comparison.

## 7. A stronger formal-residue diagnostic

Keep $K$ fixed but replace the true positive weights (8) by independent
symmetric formal variables $w_0,\ldots,w_k$ in (9)--(11).  The target (3)
is linear in these variables.  For a single pair $r>0$, use



$$
\begin{aligned}
 \frac{\Lambda_n^{[r]}}\Phi
 &=\frac1{U-r}+\frac1{U+r},\\
 \frac{\Lambda_{n-1}^{[r]}}\Phi
 &=n\left\{\frac1{(U-r)^2}+\frac1{(U+r)^2}\right\}
 -nhH_r^*\left\{\frac1{U-r}-\frac1{U+r}\right\};         \tag{41}
\end{aligned}
$$



for $r=0$, use $1/U$ and $n/U^2$.  Exact symbolic grids show that
the coefficient of every $w_r$ in (3) has one common strict sign.  This is
stronger than needed, because the actual weights are positive.  It suggests
a direct oscillatory-kernel theorem for the paired-node rows as a possible
alternative to (37).  No extrapolation from this diagnostic is made.

## 8. Replay and open statement

The certificate verifies the Stieltjes identities and residues over



$$
3\le m\le11\ (m\text{ odd}),\qquad
 4\le n\le10\ (n\text{ even}),                              \tag{42}
$$



and verifies (7), the opposite reinforcing signs, and the original
two-border ratio on the smaller determinant grid



$$
3\le m\le7\ (m\text{ odd}),\quad
 4\le n\le8\ (n\text{ even}),\quad
 3\le D\le\min(7,n-1)\ (D\text{ odd}).                     \tag{43}
$$



The all-parameter results are the pole cancellation, residue formula,
strict positivity (18), endpoint identity (7), and common-phase reduction
(32)--(36).  The Euler-border inequality (36a), equivalently the
opposite-sign/reinforcing assertion for the second term in (7), remains open
in general.
