> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Four target returns and exact barriers to lowering the endpoint order

Date: 2026-08-27.

## 1. Outcome

Fix an even integer $n\ge2$, an odd prime $p>2n+1$, and



$$
c=\frac{p-2n-1}{2}.
 \tag{1}
$$



Retain the accepted one-block endpoint periods



$$
D_v=\int_{-1}^{0}z^{c-v-1}P_n(z)(1+z)^{2v+1}\,dz,
 \qquad
 U_v=\operatorname {Im}\int_1^i
 z^{c-v-1}P_n(z)(1+z)^{2v+1}\,dz
 \tag{2}
$$



for $0\le v\le c-1$.  On the simple Bessel-root branch, put



$$
F_v=4(q_n/p)U_v-p_nD_v\pmod p.
 \tag{3}
$$



The accepted scalar recurrence and nonzero Casoratian prove that $F$
is a nonzero order-three solution and has no run of three zeros.  This
note proves that recurrence order is not a bound on the total number of
target zeros.  In particular, even an at-most-three theorem is false:



$$
\boxed{
\begin{array}{c|c|c}
(n,p)&c&\{v:F_v=0\}\\ \hline
(3996,291869)&141938&\{34071,69843,112900,121346\},\\
(756,18313)&8400&\{2136,2883,7328\},\\
(946,14629)&6368&\{1778,2010,3483\}.
\end{array}}
\tag{4}
$$



Every zero in (4) is generic: both $D_v$ and $U_v$ are nonzero.
All ten zeros are isolated.

Three further exact reductions explain why two tempting improvements do
not work.

1. A new recurrence in the original parameter $k$ is exactly the
   accepted endpoint recurrence after one-block specialization.  It
   resets at both ends of the block and supplies no cross-boundary
   equation.
2. The ordinary generating function of any scalar solution obeys an
   explicit inhomogeneous differential equation of order two.  The map
   from the three initial values to its quadratic inhomogeneous term is
   injective.  Thus no nonzero endpoint solution enters the homogeneous
   order-two kernel.
3. The accepted Ore right factor removes the $p_nD_v$ term, but its
   remaining adjacent minor can vanish.  In the exact case
   $(n,p)=(2,109)$, it vanishes at $v=18,22,42$.

These are exact barriers, not a proof that no more subtle total-zero or
weighted-product estimate exists.

## 2. A global recurrence in $k$

Start from the positive Fourier integral



$$
J_{n,k}=\int_0^1\frac{x^n(1-x)^n}{(1+x^2)^k}\,dx,
 \qquad k>n.
 \tag{5}
$$



Put



$$
\begin{aligned}
c_0&=\frac{n+2}{8(k+1)(k+2)},&
c_1&=\frac{n+1}{4(k+1)(k+2)},\\
c_2&=-\frac{2k-n}{8(k+1)(k+2)},&
c_3&=-\frac{k-n}{4(k+1)(k+2)},
\end{aligned}
\tag{6}
$$



and define



$$
S(x)=c_0+c_1x+c_2x^2+c_3x^3,
 \qquad
 R(x)=\frac{x(1-x)S(x)}{(1+x^2)^2}.
 \tag{7}
$$



The logarithmic derivative of the integrand in (5) is



$$
\frac n x-\frac n{1-x}-\frac{2kx}{1+x^2}.
 \tag{8}
$$



Direct expansion gives the rational-function identity



$$
\begin{aligned}
R'(x)+R(x)\left(
\frac n x-\frac n{1-x}-\frac{2kx}{1+x^2}
\right)
={}&\frac1{8(k+1)(k+2)}
\sum_{j=0}^{3}\frac{a_j}{(1+x^2)^j},
\end{aligned}
\tag{9}
$$



where



$$
\begin{aligned}
a_0&=-2(k-n)(2k-2n-1),\\
a_1&=16k^2-20kn+10k+5n^2-7n+2,\\
a_2&=-4(k+1)(5k-3n+4),\\
a_3&=8(k+1)(k+2).
\end{aligned}
\tag{10}
$$



The product $R(x)x^n(1-x)^n/(1+x^2)^k$ vanishes at both endpoints.
Integrating its derivative proves



$$
\boxed{
\begin{aligned}
&8(k+1)(k+2)J_{n,k+3}
-4(k+1)(5k-3n+4)J_{n,k+2}\\
&\quad +(16k^2-20kn+10k+5n^2-7n+2)J_{n,k+1}\\
&\quad -2(k-n)(2k-2n-1)J_{n,k}=0.
\end{aligned}}
\tag{11}
$$



Retain the accepted coordinate identity



$$
X_k:=2^{2k-2}J_{n,k}
 =S_{n,k}+\frac{C_{0,k}}4\pi.
 \tag{12}
$$



Substituting $J_{n,k+j}=2^{-2(k+j)+2}X_{k+j}$ in (11) and multiplying
by eight gives



$$
\boxed{
\begin{aligned}
&(k+1)(k+2)X_{k+3}
-2(k+1)(5k-3n+4)X_{k+2}\\
&\quad+2(16k^2-20kn+10k+5n^2-7n+2)X_{k+1}\\
&\quad-16(k-n)(2k-2n-1)X_k=0.
\end{aligned}}
\tag{13}
$$



Since $1$ and $\pi$ are linearly independent over $\mathbb Q$,
both $S_{n,k}$ and $C_{0,k}$ separately satisfy (13).  So does every
fixed rational linear combination of these two coordinate sequences.

## 3. Exact specialization to the endpoint operator

For the one-block parameters, write



$$
K_v=n+\frac{p+2v+1}{2},
 \qquad k_v=K_v+1
 =n+\frac{p+2v+3}{2}.
 \tag{14}
$$



Reduce (13) modulo $p$, set $k=k_v$, and multiply all four
coefficients by four.  The coefficients, in the order
$X_v,X_{v+1},X_{v+2},X_{v+3}$, become



$$
\begin{aligned}
 &-64(v+1)(2v+3),\\
 &8(n^2+12nv+21n+16v^2+58v+53),\\
 &-2(2n+2v+5)(4n+10v+23),\\
 &(2n+2v+5)(2n+2v+7).
\end{aligned}
\tag{15}
$$



These are exactly the accepted endpoint scalar coefficients.  The
apparently new global recurrence is therefore the same operator in the
common one-block range.

The two boundary pivots show why it does not extend the theorem across
the block.  The first band index is



$$
k_0=n+\frac{p+3}{2}.
 \tag{16}
$$



At the preceding recurrence index,



$$
k=k_0-1=n+\frac{p+1}{2},
\tag{17}
$$



the backward coefficient is



$$
-16(k-n)(2k-2n-1)=-8p(p+1).
 \tag{18}
$$



At the upper recurrence index $k=p-2$, the forward coefficient is



$$
(k+1)(k+2)=p(p-1).
 \tag{19}
$$



Both vanish modulo $p$.  After passage to first $p$-adic digits,
the outside coordinate enters as an inhomogeneous boundary term; it is
not a fourth homogeneous endpoint value.  Thus (18)--(19) are exact
resets, not propagation identities.  This agrees with the accepted
outside-band example $n=2$, $p=7$, $k=10,11,12$, where the same
prime survives the complete match in all three consecutive forms.

## 4. The exact generating-function equation is inhomogeneous

Let $X_0,X_1,\ldots$ be any characteristic-zero solution of the
endpoint recurrence, extended for all $v\ge0$, and put



$$
G(t)=\sum_{v\ge0}X_vt^v,
 \qquad \vartheta=t\frac d{dt}.
 \tag{20}
$$



Multiplying the recurrence by $t^{v+3}$ and summing gives



$$
\mathscr L_nG(t)=B_0+B_1t+B_2t^2,
 \tag{21}
$$



where



$$
\begin{aligned}
\mathscr L_n={}&-4(2t-1)(4t-1)^2\vartheta^2\\
&-8(4t-1)(-3nt+n+10t^2-4t)\vartheta\\
&+8n^2t^2-16n^2t+4n^2+72nt^2-20nt\\
&\hspace{35mm}-192t^3+88t^2-6t-1,
\end{aligned}
\tag{22}
$$



and



$$
B_0=(2n-1)(2n+1)X_0,
 \tag{23}
$$





$$
B_1=-(2n+1)\{(8n+6)X_0-(2n+3)X_1\},
 \tag{24}
$$





$$
\begin{aligned}
B_2={}&8(n^2+9n+11)X_0
-2(4n+13)(2n+3)X_1\\
&+(2n+3)(2n+5)X_2.
\end{aligned}
\tag{25}
$$



The triangular map



$$
(X_0,X_1,X_2)\longmapsto(B_0,B_1,B_2)
 \tag{26}
$$



has diagonal



$$
(2n-1)(2n+1),\quad
 (2n+1)(2n+3),\quad
 (2n+3)(2n+5).
 \tag{27}
$$



It is injective in characteristic zero.  It is also injective modulo
every one-block prime with $p>2n+5$.  Therefore the attractive
second-order differential operator in (22) is necessarily inhomogeneous
for every nonzero endpoint solution.  Its singular factors
$(4t-1)^2(2t-1)$ reflect the endpoint geometry, but they do not lower
the three-dimensional initial-state problem.

## 5. What the known Ore right factor does and does not do

Write



$$
D_v=\kappa_v\phi_v,
 \qquad \phi_v=\Phi_n(2v+1),
 \qquad \widetilde U_v=U_v/\kappa_v,
 \qquad \widetilde F_v=F_v/\kappa_v.
 \tag{28}
$$



The accepted normalized operator has the exact right factor



$$
\widehat L=(E^2+\alpha_vE+\beta_v)(E-r_v),
 \qquad r_v=\frac{\phi_{v+1}}{\phi_v}.
 \tag{29}
$$



Where the displayed ratio is defined,



$$
(E-r_v)\widetilde F_v
 =4(q_n/p)(E-r_v)\widetilde U_v.
 \tag{30}
$$



Thus the right factor removes the complete $p_nD_v$ contribution.
Without any division by $\phi_v$, the same statement is



$$
\boxed{
\phi_v\widetilde F_{v+1}-\phi_{v+1}\widetilde F_v
=4(q_n/p)
\bigl(\phi_v\widetilde U_{v+1}
-\phi_{v+1}\widetilde U_v\bigr).}
\tag{31}
$$



The term in parentheses is the normalized adjacent minor



$$
\frac{D_vU_{v+1}-D_{v+1}U_v}
 {\kappa_v\kappa_{v+1}}.
 \tag{32}
$$



It is not always a unit.  Exact recurrence evaluation for
$(n,p)=(2,109)$, where $c=52$, gives



$$
D_vU_{v+1}-D_{v+1}U_v=0
 \quad\Longleftrightarrow\quad
 v\in\{18,22,42\}.
 \tag{33}
$$



Consequently (29)--(31) are a genuine order-two reduction, but not a
first-order injectivity theorem for the projective ratio $U_v/D_v$.

## 6. Exact four- and three-return counterexamples

The primitive Bessel recurrence, computed modulo $p^2$, gives



$$
\begin{array}{c|c|c|c}
(n,p)&p_n\pmod p&q_n\pmod {p^2}&q_n/p\pmod p\\ \hline
(3996,291869)&259933&12855661974&44046,\\
(756,18313)&17127&260026287&14199,\\
(946,14629)&7046&130563825&8925.
\end{array}
\tag{34}
$$



In all three rows $v_p(q_n)=1$.  The initial endpoint triples are obtained
in two independent exact ways: by direct construction of each
degree-$2n+1$ Fourier polynomial, and from the directly expanded
$n=2$ periods by the accepted exact contiguity matrices



$$
(n,c)\longmapsto(n+2,c-2).
 \tag{35}
$$



The direct construction does not use a quadratic-time convolution.  Put



$$
H(z)=(1+i)-2z+(1-i)z^2,
 \qquad P_n(z)=H(z)^n=\sum_{j=0}^{2n}\rho_jz^j.
 \tag{35a}
$$



Comparing coefficients in $HP_n'=nH'P_n$ gives



$$
\boxed{
(1+i)(j+1)\rho_{j+1}
=-2(n-j)\rho_j+(1-i)(2n-j+1)\rho_{j-1},}
\tag{35b}
$$



with $\rho_{-1}=0$ and $\rho_0=(1+i)^n$.  All divisors in (35b)
are units because $p$ is odd and $2n<p$.  Hence the complete direct
polynomial, and then all three initial endpoint sums, are constructed in
linear rather than quadratic time.  The certificate also verifies
$P_n(1)=P_n(i)=0$ and the terminal coefficient
$\rho_{2n}=(1-i)^n$.

Every matrix denominator is a nonzero residue because all of its positive
integer factors are below $p$.  Propagating the endpoint scalar
recurrence through all $c$ indices and evaluating (3) gives exactly
the zero sets in (4), with the following generic digits:



$$
\begin{array}{c|r|r|r|r}
(n,p)&v&K_v&D_v&U_v\\ \hline
(3996,291869)&34071&184002&4115&130564\\
&( )&69843&219774&204753&69916\\
&( )&112900&262831&34114&132031\\
&( )&121346&271277&5748&159822\\ \hline
(756,18313)&2136&12049&8874&12823\\
&( )&2883&12796&4296&7966\\
&( )&7328&17241&1408&4998\\ \hline
(946,14629)&1778&10039&13729&7813\\
&( )&2010&10271&3839&7033\\
&( )&3483&11744&3462&1057
\end{array}
\pmod p.
\tag{36}
$$



All displayed digits are nonzero.  The companion certificate checks all
$141938+8400+6368$ target values, not only the ten listed positions, and
proves that there are no additional zeros.

For context only, the four-return case was discovered by an exact modular
scan that completed every odd prime $p<291869$ and every even



$$
2\le n\le\min\left\{10000,\frac{p-7}{2}\right\},
 \tag{37}
$$



then reached $n=3996$ at $p=291869$.  It evaluated 1,758 simple
Bessel-root target sequences before stopping at the first four-return
record in that ordering.  This search scope is a finite diagnostic, not a
density estimate.  In particular, (4) proves that a universal bound of
three is false, but it gives no theorem that the number of returns is
unbounded.

## 7. Certificate and exact scope

The companion script performs the following exact checks.

1. It expands (9) symbolically and derives (11).
2. It specializes all four coefficients of (13) and verifies (15),
   (18), and (19) symbolically.
3. It derives (21)--(25) from the scalar recurrence and verifies the
   injective diagonal (27).
4. It computes the Bessel data modulo $p^2$, constructs the initial
   endpoint triples both directly and by exact contiguity, compares the
   two constructions, scans both full target sequences, and verifies
   (34)--(36).
5. It verifies the adjacent-minor obstruction (33) over all 51 adjacent
   pairs.

Run

    python -m py_compile scripts/critical_fourier_endpoint_target_four_return_barrier_certificate.py
    python scripts/critical_fourier_endpoint_target_four_return_barrier_certificate.py

For a byte-identical rerun, use

    python scripts/critical_fourier_endpoint_target_four_return_barrier_certificate.py \
      --output /tmp/critical_fourier_endpoint_target_four_return_barrier_certificate.json
    cmp results/critical_fourier_endpoint_target_four_return_barrier_certificate.json \
      /tmp/critical_fourier_endpoint_target_four_return_barrier_certificate.json

The exact counterexamples refute at-most-two and at-most-three target
theorems.  The
operator specialization and reset calculation prove that the global
$k$-recurrence does not add a cross-band homogeneous constraint.  The
generating equation and right factor remain potentially useful.  The four
returns do not prove that the number of returns is unbounded as $(n,p)$
varies.  No uniform total-zero bound, weighted-product bound, improved matching
threshold, or arithmetic classification of $e+\pi$ follows here.
