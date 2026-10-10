> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The forced next coefficient for three root-of-unity frequencies

## A one-border-row total-nonnegativity theorem and the corrected phase

Checked: 2026-08-27 UTC

## 1. Verdict and scope

This note treats the complete $m=3$ subfamily of the sole parity-forced
case left by the top-cardinal theorem:



$$
m=3,\qquad n\ge4\text{ even},\qquad
 D=2d+1\ge3\text{ odd},\qquad D\le n.                 \tag{1}
$$



Put $h=n+1$.  Then $h\ge5$ is odd and, because the two sides of
$D\le n$ have opposite parity, actually $D\le n-1$.

> **Three-frequency next-coefficient theorem.**  In (1), the top candidate
> $[z^{n+D}]\Gamma$ is parity-forced to vanish,
> but
> 

$$
>       \boxed{[z^{n+D-1}]\Gamma\ne0.}                    \tag{2}
>
$$


> Consequently, for the corrected polynomial
> $\Delta=W-\Gamma$,
> 

$$
>       \boxed{\deg\Delta=n+D-1.}                          \tag{3}
>
$$



Indeed, $\deg W\le2D-2$, whereas
$n+D-1\ge2D$, so the coefficient in (2) occurs strictly above the
degree of $W$.

The proof is all-parameter.  Its new ingredient is total nonnegativity of
one very specific bordered coefficient matrix.  It is important not to
enlarge the claim:

* the matrix contains the actual top-cardinal border row exactly once;
* a generic positive combination of divisor rows need not work;
* the full three-polynomial Lace matrix, which also contains shifted copies
  of the border row, need not be totally nonnegative;
* no assertion for $m\ge5$ is made here.

The proof also repairs a phase error in the preliminary forced-odd-$m$
audit.  With the positive Stieltjes normalization used below, the correct
identity is



$$
V\sigma=V\psi-\mathcal E(V\rho),                          \tag{4}
$$



not the same formula with a plus sign.  Correspondingly, the even and odd
extra cardinal rows have opposite prefactors.

No conclusion about the arithmetic nature of $e+\pi$ is claimed here.

The deterministic replay files are

* `scripts/root_unity_forced_odd_m3_next_coefficient_certificate.py`;
* `results/root_unity_forced_odd_m3_next_coefficient_certificate.json`.

## 2. Exact centered functions and the corrected sign

Center at $X=1+U$, and put



$$
\Phi(X)=\{X(X-1)(X-2)\}^{h},\qquad
 V(x)=(1+x)^h.                                             \tag{5}
$$



The positive top-cardinal residues are



$$
w_0=\frac1{n!},\qquad w_1=\frac1{n!2^h}.                 \tag{6}
$$



Thus, for $R(U)=\Lambda_n(1+U)/\Phi(1+U)$,



$$
R(U)=\frac{w_0}{U}+\frac{w_1}{U-1}+\frac{w_1}{U+1}.
                                                                    \tag{7}
$$



Define the positive Stieltjes function



$$
\rho(x)=\frac{w_0}{x}+\frac{2w_1}{x+1}.                  \tag{8}
$$



At $U=it$, equation (7) gives the sign which must be retained:



$$
\boxed{R(it)=-it\rho(t^2).}                  \tag{9}
$$



Let



$$
A_\Phi=i^h(-1)^h,
 \qquad
 C_*=\frac{-iA_\Phi}{2}=\frac{(-1)^{(h+1)/2}}2\ne0.
                                                                    \tag{10}
$$



Since



$$
\Phi(1+it)=A_\Phi t^hV(t^2),                              \tag{11}
$$



equation (9) implies



$$
\boxed{
 \Lambda_n(1+it)=-A_\Phi i\,t^{h+1}V(t^2)\rho(t^2).}     \tag{12}
$$



Write



$$
\Lambda_{n-1}(1+it)=A_\Phi t^hV(t^2)\sigma(t^2),
 \qquad
 \mathcal E=2x\frac d{dx}+h+1.                            \tag{13}
$$



Because $d/dX=-i\,d/dt$ on this line, differentiating (12) gives



$$
\Lambda_n'(1+it)=-A_\Phi t^h
                    \mathcal E(V\rho)(t^2).               \tag{14}
$$



For $F=\Lambda_{n-1}-\Lambda_n'$, the exact pole cancellation gives



$$
\frac{F(1+U)}{\Phi(1+U)}=\psi(-U^2),\qquad
 \psi(x)=\frac{\gamma_h}{x+1},                            \tag{15}
$$



where



$$
\gamma_h=2h\left(w_0+\frac{3h+1}{2}w_1\right)>0.        \tag{16}
$$



For completeness, (16) is the $k=r=1$ specialization of the exact
simple-residue formula.  Directly, the regular part at $U=1$ is
$w_0+w_1/2$, while
$H_2-H_0=3/2$; multiplication by $2h$ gives (16).
Equations (13)--(15) now prove (4):



$$
V\sigma+\mathcal E(V\rho)=V\psi.                         \tag{17}
$$



Set



$$
A_u=x^uV,\qquad G_u=\mathcal EA_u,qquad
 b=\mathcal E(V\rho),\qquad 0\le u<d.                    \tag{18}
$$



Let $H_{2v}(z)=Q_v(z^2)$, where $H_a$ is the csch derivative
polynomial, and use the positive pairing



$$
\langle f,Q_v\rangle=
 2\int_0^\infty
 f(t^2)Q_v(\coth^2\pi t)\frac{t^h}{\sinh\pi t}\,dt.
                                                                    \tag{19}
$$



For a row $f$, define



$$
\operatorname {NB}_A(f)=
 \frac{\det[\langle A_u,Q_v\rangle;\langle f,Q_v\rangle]
       _{0\le v\le d}}
      {\det[\langle A_u,Q_v\rangle;e_d^T]_{0\le v\le d}},
                                                                    \tag{20}
$$



and define $\operatorname {NB}_G$ analogously.  The denominators are
nonzero by endpoint normality.

Let $C$ and $D_o$ be the even and odd endpoint polynomials normalized
by



$$
[z^{D-1}]C=[z^D]D_o=1.                                   \tag{21}
$$



The contour phases can now be read without ambiguity.  For $0\le v\le d$,



$$
\begin{aligned}
 E_{n-1,2v}
   &=-C_* (-1)^v\pi^{2v}\langle V\sigma,Q_v\rangle,\\
 E_{n,2v+1}
   &=+C_* (-1)^v\pi^{2v}\langle b,Q_v\rangle.
 \end{aligned}                                             \tag{22}
$$



The sign difference in (22) is the correction mentioned above.  The
ordinary even and odd blocks have the common phase



$$
\begin{aligned}
 K_{2u,2v}&=C_* (-1)^{u+v}\pi^{2v}
               \langle A_u,Q_v\rangle,\\
 K_{2u+1,2v+1}&=C_* (-1)^{u+v}\pi^{2v}
               \langle G_u,Q_v\rangle.
 \end{aligned}                                             \tag{23}
$$



The endpoint identity is exact:



$$
[z^{n+D-1}]\Gamma
 =D_o\!\cdot E_n-C\!\cdot E_{n-1}.                       \tag{24}
$$



Normalizing the two right-null vectors in (23) at their last coordinates
and using (17), equations (22)--(24) give



$$
\boxed{
 [z^{n+D-1}]\Gamma
 =C_* (-1)^d\pi^{2d}
 \left\{
 \operatorname {NB}_A(V\psi)
 -\bigl(\operatorname {NB}_A(b)-
        \operatorname {NB}_G(b)\bigr)
 \right\}.}                                               \tag{25}
$$



Thus it is enough to prove



$$
\operatorname {NB}_A(V\psi)>0,
 \qquad
 \operatorname {NB}_A(b)\le\operatorname {NB}_G(b).      \tag{26}
$$



## 3. The reverse-totally-positive pairing kernel

Put



$$
p=\frac{h+1}{2}=\frac{n+2}{2}.
$$



For $j\ge-1$ and $0\le v\le d$, define



$$
B_{jv}=\langle x^j,Q_v\rangle.                            \tag{27}
$$



The range in (1) gives $d\le p-2$, so every integral and series below
converges, including $j=-1,v=d$.

The elementary expansion



$$
\frac1{\sinh\pi t}=2\sum_{q\ge0}e^{-(2q+1)\pi t}         \tag{28}
$$



and the defining derivative identity



$$
\frac{d^{2v}}{dt^{2v}}\frac1{\sinh\pi t}
 =\pi^{2v}Q_v(\coth^2\pi t)\frac1{\sinh\pi t}
$$



give (29).  Indeed, integrate by parts $2v$ times in (27).  All boundary
terms vanish because $2j+h-2v\ge1$ in the stated range.  Expanding the
remaining csch factor by (28), integrating each exponential, and cancelling
$\Gamma(2j+h-2v+1)$ against the falling factorial gives



$$
\boxed{
 B_{jv}=4\Gamma(2j+h+1)\pi^{-(2j+h+1)}
 \sum_{q\ge0}(2q+1)^{-2(p+j-v)}.}                         \tag{29}
$$



> **Reverse-TP kernel lemma.**  If
> $j_1<\cdots<j_r$ and $v_1<\cdots<v_r$, then
> 

$$
> \operatorname {sign}\det(B_{j_a v_b})
> =\epsilon_r:=(-1)^{r(r-1)/2},                            \tag{30}
>
$$


> and the determinant is nonzero.

To prove it, put $z_q=(2q+1)^{-2}$.  Apart from positive row factors,
(29) factors through



$$
\sum_q z_q^p z_q^j z_q^{-v}.                              \tag{31}
$$



Truncate the sum, order the selected $z$'s increasingly, and apply
Cauchy--Binet.  The generalized Vandermonde determinant
$\det(z_b^{j_a})$ is positive.  The second generalized Vandermonde has
the decreasing exponent list $-v_1>\cdots>-v_r$, hence has sign
$\epsilon_r$.  Every Cauchy--Binet summand has the same sign and at least
one is strict.  Absolute convergence permits passage to the limit.  This
proves (30).

Consequently, if a coefficient matrix $\mathcal C$, with exponent columns
$j=-1,0,1,\ldots$, is totally nonnegative, then its pairing matrix
$\mathcal C B$ has the sign pattern (30).  Reversing any finite initial
set of pairing columns makes that pairing matrix totally nonnegative.

## 4. The special one-border-row coefficient theorem

Multiplying the border row by the positive scalar $1/w_0$ does not affect
total nonnegativity.  Put



$$
c=\frac{2w_1}{w_0}=2^{1-h},qquad 0<c\le\frac12,          \tag{32}
$$



and temporarily use



$$
\rho_c(x)=\frac1x+\frac c{x+1}.                           \tag{33}
$$



Let $\mathcal C(c)$ be the infinite coefficient matrix whose ordered rows
are



$$
\boxed{
 b_c=\mathcal E(V\rho_c),\quad
 A_0,G_0,A_1,G_1,A_2,G_2,\ldots}                           \tag{34}
$$



and whose columns are the powers
$x^{-1},x^0,x^1,\ldots$, in that order.

> **One-border-row theorem.**  For every odd $h\ge5$ and every
> $0\le c\le1/2$,
> 

$$
>     \mathcal C(c)\text{ is totally nonnegative}.         \tag{35}
>
$$



This is the only coefficient-TN assertion used in the proof.  We now give
an entry-by-entry factorization.

Factor the common real-negative-rooted polynomial



$$
S(x)=(1+x)^{h-2}.                                        \tag{36}
$$



Put



$$
\alpha_u=h+1+2u,qquad \beta_u=3h+1+2u,qquad
 \beta_u-\alpha_u=2h>0.                                  \tag{37}
$$



A direct calculation gives



$$
\begin{aligned}
 A_u/S&=x^u(1+x)^2,\\
 G_u/S&=x^u(1+x)(\alpha_u+\beta_ux),                       \tag{38}\\
 b_c/S&=(h-1)x^{-1}+{4h-2+c(h+1)\}
          +(1+c)(3h-1)x.
 \end{aligned}
$$



### 4.1 The endpoint $c=0$

At $c=0$, every row in (38) has a further common factor $1+x$.  After
removing it, the ordered row polynomials are



$$
x^{-1}(\alpha_{-1}+\beta_{-1}x),\quad
 x^u(1+x),\quad x^u(\alpha_u+\beta_ux)\quad(u\ge0).     \tag{39}
$$



Their coefficient matrix is the product $\mathcal B_-\mathcal S_-$,
where



$$
\mathcal B_-=
 [\alpha_{-1}\ \beta_{-1}]
 \ \oplus\!
 \bigoplus_{u\ge0}
 \begin{pmatrix}1&1\\\alpha_u&\beta_u\end{pmatrix}.     \tag{40}
$$



The local output slots of the blocks in (40) are sent by
$\mathcal S_-$ to the global exponent columns



$$
-1,0,\ 0,1,\ 1,2,\ 2,3,\ldots                   \tag{41}
$$



in precisely that order.  Entry-by-entry,



$$
(\mathcal S_-)_{\ell j}=
 \begin{cases}
 1,&j=\tau_-(\ell),\\
 0,&j\ne\tau_-(\ell),
 \end{cases}                                               \tag{42}
$$



where $\tau_-$ is the nondecreasing sequence in (41).

Every block in (40) is TN: its only nontrivial determinant is
$\beta_u-\alpha_u=2h$.  The ordered block-direct-sum matrix is TN:
in any nonzero square minor, the selected row and column counts agree in
each isolated block, so the determinant is the product of the corresponding
block minors; otherwise it is zero.

The repeated-target selector (42) is also TN.  Indeed, choose local rows
$\ell_1<\cdots<\ell_r$ and global columns $j_1<\cdots<j_r$.  A
nonzero determinant would require every target $\tau_-(\ell_a)$ to be
one of the selected columns.  If two selected targets coincide, two rows
of the selected square matrix coincide and its determinant is zero.  If
the targets are distinct, their nondecreasing order makes them strictly
increasing, so the only nonzero permutation is the identity and the
determinant is $1$.  Thus every selector minor is $0$ or $1$.

Hence (39) is TN.  Multiplication first by the coefficient Toeplitz matrix
of $1+x$, and then by that of $S=(1+x)^{h-2}$, preserves TN: these
Toeplitz matrices are the planar path matrices for one-step binomial
convolution and are TN.  Therefore



$$
\mathcal C(0)\text{ is TN}.        \tag{43}
$$



### 4.2 The endpoint $c=1/2$

At the other endpoint, the last two coefficients of the reduced border row
coincide:



$$
\frac{b_{1/2}}S=(h-1)x^{-1}+B_h(1+x),qquad
 B_h=\frac{9h-3}{2}>0.                                    \tag{44}
$$



Consider an arbitrary minor after removal of the common factor $S$.
The tail consisting of the $A_u,G_u$ rows is TN by the $c=0$
factorization above (delete its border row before multiplying back by
$S$).

* If it contains the $x^{-1}$ column, then that column has only one
  nonzero entry, in the border row.  If the border row is absent the minor
  is zero; if it is present, expansion in the first column gives the
  positive factor $h-1$ times a tail minor.
* If it omits the border row, it is a tail minor.
* If it contains the border row but omits the $x^{-1}$ column, then all
  selected rows have the common factor $1+x$.  After removing it, and
  positively rescaling the first row by $B_h$, the ordered rows are
  

$$
1,\quad x^u(1+x),\quad
      x^u(\alpha_u+\beta_ux)\quad(u\ge0).                  \tag{45}
$$



The coefficient matrix in (45) factors as



$$
\mathcal B_+\mathcal S_+,qquad
 \mathcal B_+=[1]\ \oplus\!
 \bigoplus_{u\ge0}
 \begin{pmatrix}1&1\\\alpha_u&\beta_u\end{pmatrix},     \tag{46}
$$



where the local output slots are mapped to



$$
0,\ 0,1,\ 1,2,\ 2,3,\ldots.                \tag{47}
$$



Equivalently, $(\mathcal S_+)_{\ell j}=1$ exactly when
$j=\tau_+(\ell)$, for the nondecreasing sequence $\tau_+$ in (47).
The same block and repeated-target selector proof used in (40)--(42)
proves that (45)
is TN.  At matrix level, multiplying all these rows back by $1+x$ is
right multiplication by its TN coefficient Toeplitz matrix, so
Cauchy--Binet covers arbitrary (not necessarily consecutive) selected
regular columns.  All three kinds of minors above are therefore
nonnegative, and



$$
\mathcal C(1/2)\text{ is TN}.      \tag{48}
$$



### 4.3 Convexity uses the border row only once

The tails of $\mathcal C(0)$, $\mathcal C(c)$, and
$\mathcal C(1/2)$ are identical, while



$$
b_c=(1-2c)b_0+2c\,b_{1/2}.                              \tag{49}
$$



A minor which omits the border row is independent of $c$.  A minor which
contains it is linear in that one row, hence by (49) is the convex
combination, with coefficients $1-2c$ and $2c$, of the corresponding
endpoint minors.  This proves (35).

Notice why (49) does not prove TN for a full Lace matrix: shifted copies of
the border would occur more than once in a minor, destroying this affine
argument.

## 5. A terminal-flag ratio lemma

We record the exact TN comparison used below.

> **Terminal-flag lemma.**  Let $H$ be TN, let its first row be $b$,
> and use columns $0,1,\ldots,d$.  For an increasing $d$-row tuple
> $I$, disjoint from $b$, with
> $\Delta_{I,\{1,\ldots,d\}}>0$, put
> 

$$
> \mathfrak F(I)=
> \frac{\Delta_{\{b\}\cup I,\{0,\ldots,d\}}}
>      {\Delta_{I,\{1,\ldots,d\}}}.                       \tag{50}
>
$$


> If $I\le I'$ coordinatewise and both displayed denominators are
> positive, then $\mathfrak F(I)\le\mathfrak F(I')$.

Here all row sets are written in ambient order.  First suppose that $H$
is TP and that two tuples differ only by replacing a row $r$ by a later
row $s$, with both rows in the same gap between the common rows.  Let
$R$ be those common $d-1$ rows and put $P=\{2,\ldots,d\}$.
Condense on the positive pivot $\Delta_{R,P}$.  Sylvester's identity
produces the $3$-by-$2$ matrix $Z=(z_{yc})$, with
$y=b,r,s$ and $c=0,1$, where



$$
z_{yc}=
 \frac{\Delta_{R\cup\{y\},\{c\}\cup P}}
      {\Delta_{R,P}}.                                      \tag{51}
$$



All row and column sets in (51) retain ambient order.  The one-by-one
minors of $Z$ are positive.  Sylvester's identity says that each
ordered two-by-two minor of $Z$ is a positive pivot factor times the
corresponding ordered minor of $H$; hence $Z$ is TP.  The same
identity, or a two-column Schur complement, gives



$$
\mathfrak F(R\cup\{r\})
 =z_{b0}-z_{b1}\frac{z_{r0}}{z_{r1}},                      \tag{52}
$$



and the analogous formula with $s$.  Permuting the pivot rows and
columns to write the Schur complement creates the same sign in numerator
and denominator, so (52) has no hidden parity factor.  The $(r,s)$
minor of $Z$ gives



$$
\frac{z_{r0}}{z_{r1}}\ge\frac{z_{s0}}{z_{s1}},            \tag{53}
$$



so (52) is nondecreasing under $r\mapsto s$.

For arbitrary coordinatewise tuples
$I=(i_1<\cdots<i_d)\le I'=(i'_1<\cdots<i'_d)$, replace coordinates
from right to left: first $i_d$ by $i'_d$, then $i_{d-1}$ by
$i'_{d-1}$, and so on.  At every step the old and new row occupy the
same gap between the unchanged rows: the already-replaced right neighbor
is $i'_{a+1}>i'_a$, and the not-yet-replaced left neighbor satisfies
$i_{a-1}\le i'_{a-1}<i'_a$.  Thus the one-row comparison telescopes.

Finally, restrict attention to the finite submatrix containing the rows in
the chain.  Every finite TN matrix is a limit of TP matrices of the same
shape.  Apply the just-proved comparison to the approximants and pass to
the cross-multiplied inequality.  The two endpoint denominators are
positive by hypothesis, so division after taking the limit proves the TN
statement.  No positivity of an intermediate denominator in the limiting
TN matrix is required.

## 6. Completion of the proof

Apply the one-border-row theorem with the actual value
$c=2^{1-h}$.  Compose its coefficient matrix with the kernel (27).
By Section 3, the resulting pairing matrix, in the row order



$$
b,A_0,G_0,A_1,G_1,\ldots,                    \tag{54}
$$



has every ordered minor of size $r$ signed by $\epsilon_r$.  Reverse
the finite columns $Q_0,\ldots,Q_d$; the reversal contributes the same
factor $\epsilon_r$, so the resulting matrix $H$ is TN.

In $H$, take



$$
I_A=(A_0,A_1,\ldots,A_{d-1}),\qquad
 I_G=(G_0,G_1,\ldots,G_{d-1}).                             \tag{55}
$$



Their ambient row positions are



$$
(1,3,\ldots,2d-1)\le(2,4,\ldots,2d).                    \tag{56}
$$



The row and column reversal signs cancel exactly:



$$
\mathfrak F(I_A)=\operatorname {NB}_A(b),qquad
 \mathfrak F(I_G)=\operatorname {NB}_G(b).                \tag{57}
$$



Indeed, moving $b$ from the last to the first row contributes
$(-1)^d$, reversing $d+1$ numerator columns contributes
$\epsilon_{d+1}$, and reversing the $d$ denominator columns contributes
$\epsilon_d$; their quotient is
$(-1)^d\epsilon_{d+1}/\epsilon_d=1$.  The terminal-flag lemma therefore
proves the second inequality in (26).

It remains only to record strictness of the first.  Since
$\psi(x)=\gamma_h/(x+1)$ is strictly completely monotone, Andreief's
identity for the rows



$$
A_0,\ldots,A_{d-1},V\psi                  \tag{58}
$$



is explicit.  Order the integration nodes by
$0<t_1<\cdots<t_{d+1}$, and put $x_j=t_j^2$.  The determinant of
the row functions $1,x,\ldots,x^{d-1},\psi(x)$ equals the positive
$x$-Vandermonde times the divided difference
$\psi[x_1,\ldots,x_{d+1}]$.  Here it is explicit:



$$
\psi[x_1,\ldots,x_{d+1}]
 =\frac{(-1)^d\gamma_h}{\prod_{j=1}^{d+1}(1+x_j)},
$$



so it has strict sign $(-1)^d$.
The determinant of $Q_0(Y),\ldots,Q_d(Y)$, where
$Y=\coth^2(\pi t)$ is strictly decreasing and every $Q_v$ has positive
leading coefficient, has sign $\epsilon_{d+1}$.  Thus the numerator has
strict sign $(-1)^d\epsilon_{d+1}$.  The analogous $d$-node
Andreief formula for the initial $A$-denominator has sign
$\epsilon_d$.  Since
$(-1)^d\epsilon_{d+1}/\epsilon_d=1$, their ratio is strictly positive:



$$
\operatorname {NB}_A(V\psi)>0.        \tag{59}
$$



Equations (25), (57), and (59) prove (2), and the degree comparison after
(3) completes the theorem.

## 7. Deterministic replay

The certificate performs the following exact checks.

1. It verifies (38), (44), and (49) symbolically.
2. On finite windows it constructs the block matrices and the selectors in
   (40)--(47) entry-by-entry and checks their products against the stated
   coefficient matrices.
3. It constructs the rationally column-scaled version of (29) using the
   Bernoulli formula for $\zeta(2L)/\pi^{2L}$, and checks the reverse-TP
   signature exactly.
4. It checks the composed augmented pairing matrices and the terminal-flag
   inequality on several $(h,d)$ windows.
5. For $m=3$, even $4\le n\le10$, and every admissible odd $D$, it
   constructs the original rational endpoint matrix and Hermite cardinals.
   It verifies (22)--(25) against the raw bordered coefficient, with no
   floating point, and verifies that the bracket in (25) is positive.

These finite checks replay the signs and phases.  The all-parameter proof is
Sections 2--6, not an extrapolation from the grid.
