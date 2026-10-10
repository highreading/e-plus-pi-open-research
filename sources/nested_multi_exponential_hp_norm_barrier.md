> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Multi-exponential Hermite--Padé forms for the nested Euler identity

Checked: 2026-08-27 UTC

## Scope and conclusion

Assume temporarily that



$$
s=e+\pi\in\overline{\mathbb Q}.                 \tag{1}
$$



For an integer $N\geq2$, put



$$
\zeta=e^{i\pi/N}=\zeta_{2N},\qquad x={ie\over N},\qquad
 w={is\over N},\qquad Y=e^w.
$$



Then



$$
e^x=\zeta^{-1}Y.                         \tag{2}
$$



This note tests the saturated diagonal type-I and type-II
Hermite--Padé systems for



$$
1,e^z,e^{2z},\ldots,e^{mz}                   \tag{3}
$$



with fixed $m$.  The type-I construction really does improve the selected
small-value exponent: after primitive integer clearing it gives polynomials
of height $\exp(n\log n+O(n))$ and values of size
$\exp(-mn\log n+O(n))$.  Thus its limiting height exponent is $m$,
instead of the exponent one of ordinary Padé approximation.

That analytic improvement does not become an arithmetic contradiction.
Under (1), the two numbers



$$
e,\qquad e^{is/N}                         \tag{4}
$$



are algebraically independent.  Every nonconstant Hermite--Padé form in
them is therefore transcendental, not an algebraic integer.  Taking all
conjugates of the *coefficient field* gives another nonconstant polynomial
value, not a number-field norm.  Root-of-unity projections leave one of the
two transcendental generators.  Resultants which eliminate the exponential
generator leave a nonconstant polynomial in $e$.

There is also an exact adjacent-system determinant identity.  It is the
multi-exponential analogue of the ordinary Padé cross-product, and it
collapses to a monomial.  At $x=ie/N$, exact denominator clearing cancels
the entire apparent factor $N^{-U}$ and leaves an integer multiple of
$e^U$.  At the algebraic point $w=is/N$, it leaves an algebraic-integer
multiple of $(\delta s)^U$, whose full norm is at least one.  Thus the
canonical type-I/type-II elimination does not contract.

The best currently applicable algebraic-independence measures are also many
orders of magnitude too weak.  This is a rigorous barrier for this fixed
$(N,m)$ Hermite--Padé mechanism, not a classification of $e+\pi$ and not
a no-go theorem for an unknown construction using additional arithmetic
input.

## 1. The algebraic-independence obstruction

Under (1), both $1$ and $is/N$ are algebraic and linearly independent
over $\mathbb Q$.  If



$$
P(X,Z)=\sum_{r,j}c_{rj}X^rZ^j\in\overline{\mathbb Q}[X,Z]
$$



is nonzero, then



$$
P(e,e^{is/N})=\sum_{r,j}c_{rj}
                 \exp\left(r+{jis\over N}\right).                \tag{5}
$$



The algebraic exponents in (5) are distinct: equality of two of them forces
the real integer difference and the purely imaginary integer multiple of
$s$ to vanish separately.  Lindemann--Weierstrass therefore gives



$$
P(e,e^{is/N})\ne0.                                  \tag{6}
$$



Consequently $e$ and $e^{is/N}$ are algebraically independent.  In
fact, a nonconstant polynomial value in (4) is transcendental: if it were
an algebraic number $a$, then $P(X,Z)-a$ would contradict (6).

This observation will distinguish a small *transcendental value* from a
small algebraic integer throughout the note.

## 2. An exact saturated type-I system

Fix $m\geq1$, $n\geq0$, and set



$$
U=(m+1)(n+1),\qquad L=U-1.                                     \tag{7}
$$



For $0\leq j\leq m$, define



$$
A_{j,n}(z)=
 [u^n]\,{e^{uz}\over\displaystyle
                    \prod_{\substack{0\leq k\leq m\\k\ne j}}
                    (j-k+u)^{n+1}}.                              \tag{8}
$$



Then $A_{j,n}\in\mathbb Q[z]$ and $\deg A_{j,n}\leq n$.  Equivalently,
$e^{jz}A_{j,n}(z)$ is the residue at $t=j$ of



$$
{e^{tz}\over\prod_{k=0}^m(t-k)^{n+1}}.                         \tag{9}
$$



The sum of the finite residues gives the exact exponential polynomial



$$
R_{m,n}(z)=\sum_{j=0}^m A_{j,n}(z)e^{jz}.                        \tag{10}
$$



Expanding $e^{tz}$ in (9), the sum of the residues of
$t^q/\prod(t-k)^{n+1}$ vanishes for $q<L$, and equals one for $q=L$.
Hence



$$
R_{m,n}(z)={z^L\over L!}+O(z^{L+1}).                \tag{11}
$$



There are $(m+1)(n+1)=L+1$ coefficient unknowns.  Thus (11) is the
saturated diagonal type-I order.

The Hermite--Genocchi formula makes (11) global.  Let the multiset
$\mathcal X$ contain each of $0,1,\ldots,m$ exactly $n+1$ times.  With
the simplex measure normalized to have volume $1/L!$,



$$
R_{m,n}(z)=z^L\int_{\Delta_L}
       \exp\left(z\sum_{q=0}^L\lambda_q\mathcal X_q\right)d\lambda.
                                                                    \tag{12}
$$



In particular, for real $a$,



$$
|R_{m,n}(ia)|\leq {|a|^L\over L!}.              \tag{13}
$$



There is no unrecorded exponential cancellation in (13) when $m,a$ are
fixed.  Under the uniform probability measure on the simplex, group the
coordinates belonging to the same node.  The group weights have the
Dirichlet distribution



$$
(W_0,\ldots,W_m)\sim
             \operatorname{Dirichlet}(n+1,\ldots,n+1).
$$



For $T=\sum jW_j$,



$$
\mathbb E T={m\over2},\qquad
 \operatorname{Var}(T)=
 {m(m+2)\over12\big((m+1)(n+1)+1\big)}.                          \tag{14}
$$



Since $|e^{iv}-1|\leq|v|$, equations (12)--(14) give



$$
R_{m,n}(ia)={(ia)^L\over L!}e^{iam/2}
                 \left(1+O_{m,a}(n^{-1/2})\right).               \tag{15}
$$



Thus the magnitude in (13) is asymptotically sharp for every fixed real
$a$, without a restriction on the phase interval.

For example, primitive rational scaling gives



$$
\begin{array}{c|c|c}
(m,n)&L& (A_{0,n},\ldots,A_{m,n})\\ \hline
(1,2)&5&(-z^2-6z-12,\ z^2-6z+12)\\
(2,1)&5&(z+3,\ 4z,\ z-3)\\
(2,2)&8&(z^2+9z+24,\ -8z^2-48,\ z^2-9z+24).
\end{array}                                                       \tag{16}
$$



The displayed rows are independently scaled; (11) uses the residue
normalization (8).

## 3. Exact integer clearing and the height exponent

Write



$$
D_m=\operatorname{lcm}(1,\ldots,m).        \tag{17}
$$



The coefficient of $z^r$ in (8) is



$$
{1\over r!}\prod_{k\ne j}(j-k)^{-n-1}
 \sum_{\substack{\ell_k\geq0\\\sum_{k\ne j}\ell_k=n-r}}
 \prod_{k\ne j}(-1)^{\ell_k}
       {\binom{n+\ell_k}{\ell_k}\over(j-k)^{\ell_k}}.          \tag{18}
$$



Every denominator in a summand of (18) is cleared by



$$
C_{m,n}=n!(m!)^{n+1}D_m^n.                     \tag{19}
$$



Indeed, $n!/r!$ is integral,
$(m!/(j!(m-j)!))^{n+1}$ is integral, and a product of integer differences
with total extra exponent at most $n$ divides $D_m^n$.  Therefore



$$
C_{m,n}A_{j,n}\in\mathbb Z[z].           \tag{20}
$$



Let $F=\mathbb Q(i,\zeta)$, and define



$$
\mathcal P_{m,n,N}(X,Z)=C_{m,n}N^n
      \sum_{j=0}^m A_{j,n}(iX/N)\zeta^{-j}Z^j
      \in\mathcal O_F[X,Z].                                      \tag{21}
$$



Using (2),



$$
\mathcal P_{m,n,N}(e,Y)=C_{m,n}N^nR_{m,n}(ie/N).                \tag{22}
$$



Equations (15), (19), and Stirling's formula give the exact leading scale



$$
\log|\mathcal P_{m,n,N}(e,Y)|=-mn\log n+O_{m,N}(n).             \tag{23}
$$



The coefficient house of (21) satisfies



$$
\log H(\mathcal P_{m,n,N})
                         =n\log n+O_{m,N}(n).                    \tag{24}
$$



For the upper bound, use (18), the fixed number of compositions, and
$\binom{n+\ell}{\ell}\leq4^n$ when $0\leq\ell\leq n$.  For the lower
bound, the constant coefficient at $j=0$ has terms of one sign and includes
the term $\ell_1=n$, giving



$$
C_{m,n}N^n|A_{0,n}(0)|
       \geq n!(ND_m)^n\binom{2n}{n}.                              \tag{25}
$$



Primitive content cannot change either leading term.  The coefficient of
$X^nZ^0$ in (21) is, up to a root of unity, exactly $D_m^n$.  Hence the
norm of the coefficient ideal content is at most exponential in $n$, while
(25) contains the factorial term.  If $\mathcal P^{\rm prim}$ denotes any
primitive algebraic-integer normalization, then



$$
\boxed{
 \begin{aligned}
  \log H(\mathcal P^{\rm prim})&=n\log n+O_{m,N,F}(n),\\
  \log|\mathcal P^{\rm prim}(e,Y)|&=-mn\log n+O_{m,N,F}(n).
 \end{aligned}}                                                  \tag{26}
$$



Thus the improved limiting exponent is exactly $m$.  By Section 1, the
nonzero value in (26) is transcendental.

## 4. Why coefficient conjugates and root-of-unity projections do not form a norm

For $\sigma:F\hookrightarrow\mathbb C$, conjugating the coefficients in
(21) gives a nonconstant polynomial $\mathcal P^\sigma(X,Z)$.  The formal
coefficient norm



$$
\prod_{\sigma:F\hookrightarrow\mathbb C}
                    \mathcal P^\sigma(X,Z)\in\mathbb Q[X,Z]       \tag{27}
$$



is still nonconstant.  Its value at $(e,Y)$ is transcendental by Section 1.
It is not the number-field norm of $\mathcal P(e,Y)$, because that value is
not algebraic.  Moreover, only the distinguished coefficient embedding is
tied to the small analytic identity (2); conjugating $\zeta$ while fixing
the transcendental variable $Y$ does not transport (2).

The same obstruction can be seen by exact Fourier projection.  If
$P(X,Z)=\sum_{j=0}^mp_j(X)Z^j$ and $q>m$, then for a primitive
$q$-th root $\omega$,



$$
{1\over q}\sum_{a=0}^{q-1}\omega^{-ar}P(X,\omega^aZ)
                         =p_r(X)Z^r.                              \tag{28}
$$



For $r>0$, the exponential generator remains.  For $r=0$, one obtains a
nonconstant polynomial in $e$.  A full orbit product belongs to
$\overline{\mathbb Q}[X,Z^q]$, but $Z^q=e^{iqs/N}$ is still
transcendental and algebraically independent from $e$.  Complex
conjugation similarly gives a Laurent polynomial in $Y$; it does not make
the numerical product algebraic.

There is a branch-preserving version worth separating from coefficient
conjugation.  For any integer $a$, put



$$
z_a={i\big(ae+(1-a)s\big)\over N}.
$$



Then $e^{z_a}=\zeta^{-a}Y$, so a separate copy of (10) at each fixed
$z_a$ is small.  A fixed collection of such rows still has coefficients
which are polynomials in $e$.  It cannot yield an algebraic number unless
that dependence is eliminated exactly.  If enough logarithm sheets are used
to interpolate a degree-$n$ dependence on $e$, then some $|a|$ is of
order $n$; the term $|z_a|^L/L!$ in (13) loses its superfactorial decay,
and multiplication by (19) grows like $\exp(n\log n+O(n))$.  Thus growing
sheets do not preserve the selected smallness.

## 5. The exact adjacent-system determinant

The canonical way to obtain $m+1$ independent saturated rows is to raise
one pole multiplicity at a time.  Put



$$
D_k(t)=(t-k)^{n+2}\prod_{\substack{0\leq h\leq m\\h\ne k}}
                    (t-h)^{n+1},qquad 0\leq k\leq m,             \tag{29}
$$



and define



$$
A_{k,j}(z)=\operatorname*{Res}_{t=j}{e^{(t-j)z}\over D_k(t)},
 \qquad R_k(z)=\sum_{j=0}^mA_{k,j}(z)e^{jz}.                      \tag{30}
$$



The diagonal entry $A_{k,k}$ has degree at most $n+1$, the other entries
have degree at most $n$, and every $R_k$ vanishes to order



$$
U=(m+1)(n+1).                            \tag{31}
$$



Let $\mathcal A(z)=(A_{k,j}(z))_{0\leq k,j\leq m}$.  Replacing its last
column by the vector $(R_k(z))_k$ multiplies the determinant by $e^{mz}$.
The new last column is $O(z^U)$, so $\det\mathcal A(z)=O(z^U)$.  On the
other hand, $\deg\det\mathcal A\leq U$, and only the identity permutation
can contribute to degree $U$.  Its leading coefficients give the exact
identity



$$
\boxed{
 \det\mathcal A(z)=
 {(-1)^{(n+1)m(m+1)/2}z^U\over
  (n+1)!^{m+1}\left(\prod_{k=0}^m k!\right)^{2(n+1)}}.}           \tag{32}
$$



This is the multi-exponential Padé cross-product.  It also proves the needed
normality of the adjacent type-I system.

An exact common clearing for every entry in (30) is



$$
\Gamma_{m,n}=(n+1)!(m!)^{n+2}D_m^{n+1}.                         \tag{33}
$$



Set $G_m=\prod_{k=0}^m k!$.  After substituting $z=iX/N$, multiplying
every row by $N^{n+1}$, and optionally multiplying column $j$ by
$\zeta^{-j}$, (32) becomes



$$
\det\left(\Gamma_{m,n}N^{n+1}
             A_{k,j}(iX/N)\zeta^{-j}\right)
       =\varepsilon_{m,n,N}J_{m,n}X^U,                            \tag{34}
$$



where $|\varepsilon_{m,n,N}|=1$ is a root of unity and



$$
J_{m,n}={\big((m!)^{n+2}D_m^{n+1}\big)^{m+1}\over G_m^{2(n+1)}}
                              \in\mathbb Z_{>0}.                  \tag{35}
$$



Integrality in (35) also follows directly from
$\prod_{k=0}^m k!(m-k)!=G_m^2$ and
$k!(m-k)!\mid m!$.  The powers of $N$ cancel *exactly* in (34).  At
$X=e$, the magnitude of the determinant is



$$
J_{m,n}e^U\geq e^U,                    \tag{36}
$$



and its value is transcendental.

At the algebraic endpoint $z=is/N$, choose a positive integer $\delta$
such that $\delta s$ is an algebraic integer.  Multiplying every row by
the additional factor $\delta^{n+1}$ gives an algebraic-integer matrix,
and (32) gives, up to a root of unity,



$$
J_{m,n}(\delta s)^U.                   \tag{37}
$$



For any number field containing $s,i,\zeta$, its absolute norm is



$$
J_{m,n}^{[K:\mathbb Q]}
       \left|N_{K/\mathbb Q}(\delta s)\right|^U\geq1.             \tag{38}
$$



Thus the one adjacent determinant which is genuinely algebraic has a
noncontracting full norm.  Equation (38) explicitly includes all coefficient
and $s$-field conjugates.

## 6. The exact cost of eliminating the exponential variable

The ordinary two-endpoint cross-product is already contained in this
framework.  When $m=1$, equations (10) at $x$ and $w$, together with
$e^x=\zeta^{-1}e^w$, give the exact cancellation



$$
\begin{aligned}
 \mathcal C_n(x,w)
   &:=A_{0,n}(x)A_{1,n}(w)
       -\zeta^{-1}A_{1,n}(x)A_{0,n}(w)\\
   &=A_{1,n}(w)R_{1,n}(x)
       -\zeta^{-1}A_{1,n}(x)R_{1,n}(w).                         \tag{39a}
 \end{aligned}
$$



Under (1), $w$ is algebraic while $x=ie/N$, so a nonconstant
$\mathcal C_n(x,w)$ is a polynomial value in $e$, not an algebraic
number.  After the same primitive clearing as Section 3, each coefficient
factor has size $H=\exp(n\log n+O(n))$, while each remainder has size
$\epsilon=\exp(-n\log n+O(n))$.  Thus (39a) is at best
$\exp(O(n))$ on this scale.  It has lost the superfactorial gain before
any one-variable transcendence measure is applied.

Let $P_0(Z),\ldots,P_m(Z)$ be $m+1$ branch or adjacent forms, evaluated
at the same $X=e$, and suppose their coefficient magnitudes are at most
$H$, while $|P_a(Y)|\leq\epsilon$ and $|Y|=1$.  If $C_j$ is the
column of coefficients of $Z^j$, then



$$
(P_0(Y),\ldots,P_m(Y))^T=\sum_{j=0}^mY^jC_j.
$$



Replacing $C_m$ by this value vector gives



$$
Y^m\det(C_0,\ldots,C_m)
   =\det(C_0,\ldots,C_{m-1},(P_a(Y))_a).                          \tag{39}
$$



Consequently



$$
|\det C|\leq (m+1)!H^m\epsilon.                \tag{40}
$$



For the forms in Section 3,



$$
H=\exp(n\log n+O(n)),\qquad
 \epsilon=\exp(-mn\log n+O(n)),                                 \tag{41}
$$



so (40) is only $\exp(O(n))$.  The $m$ coefficient columns consume
exactly the height exponent $m$ gained by the type-I approximation.
The exact adjacent case is sharper still: it is the growing monomial (34).

Two degree-$m$ forms do no better through a Sylvester resultant.  The
standard Bézout cofactors have coefficient size
$O_m(H^{2m-1})$, hence at a common approximate value $Y$,



$$
|\operatorname{Res}_Z(P,Q)|
       \leq O_m(H^{2m-1})\big(|P(Y)|+|Q(Y)|\big)
       =\exp((m-1)n\log n+O(n)).                                 \tag{42}
$$



For $m\geq2$, (42) is not even contracting on the $n\log n$ scale.  For
$m=1$, it is at best exponential in $n$.  More importantly, a nonzero
resultant here is a polynomial in $e$, not an algebraic number.  If it is
constant, primitive algebraic-integer clearing precludes a contracting
nonzero norm; if it is identically zero, it provides no nonzero arithmetic
object.

Eliminating the remaining $e$-dependence requires a determinant or
resultant in a space of dimension proportional to $n$.  That pays the
remaining full polynomial dimension.  A fixed root-of-unity orbit has only
finitely many rows; a growing orbit has the loss described after (28).

Here is the exact determinant count behind that statement.  Let



$$
V=(n+1)(m+1),\qquad
             \mathbf v=(X^rZ^j)_{0\leq r\leq n,\ 0\leq j\leq m},
$$



and let $V$ cleared forms with coefficient matrix $M$ satisfy
$\mathbf L=M\mathbf v$.  Replacing any coefficient column $M_k$ by
$\mathbf L$ gives the identity



$$
v_k\det M=det(M_0,\ldots,M_{k-1},\mathbf L,
                         M_{k+1},\ldots,M_{V-1}).                 \tag{42a}
$$



At $(X,Z)=(e,Y)$, every $|v_k|\geq1$.  If the coefficient house is at
most $H$ and every selected value is at most $\epsilon$, then



$$
|\det M|\leq V!H^{V-1}\epsilon.           \tag{42b}
$$



Only one small-value column appears: all entries of $\mathbf L$ are the
coordinates of the same evaluation vector.  With (41), the logarithm of the
right side of (42b) is $\Theta_m(n^2\log n)$, not negative.  This is the
full Dirichlet-dimension cost of eliminating both transcendental generators
by a coefficient determinant.  Replacing more columns would require
independent evaluation or derivative vectors and corresponding simultaneous
smallness, which the single saturated identity (10) does not supply.

## 7. Type-II systems and Mahler duality

The normality used below is not a numerical assumption.  Formula (9) works
with arbitrary positive pole multiplicities $r_0,\ldots,r_m$ and gives a
type-I remainder of exact order $\sum r_j-1$.  Raising $r_k$ by one in
row $k$, the proof of (32) applies verbatim: the coefficient determinant
has degree at most $\sum r_j$, vanishes to that order, and has a nonzero
leading term from the identity permutation.  Hence every such multi-index
is normal.  Ordinary finite-dimensional Mahler duality then gives full rank
for the corresponding type-II constraint matrices.

For the $m$ nonconstant functions $e^{jz}$, the standard diagonal
type-II allocation takes a common denominator $Q$ of degree at most $mn$
and numerators $P_j$ of degree at most $mn$, with



$$
Q(z)e^{jz}-P_j(z)=O\big(z^{(m+1)n+1}\big),qquad1\leq j\leq m.  \tag{43}
$$



Writing $Q(z)=\sum_{k=0}^{mn}q_kz^k$, the exact homogeneous constraints
are



$$
\sum_{k=0}^{mn}q_k{j^{\ell-k}\over(\ell-k)!}=0,
 \quad 1\leq j\leq m,\quad mn+1\leq\ell\leq(m+1)n.              \tag{44}
$$



There are $mn$ independent equations in $mn+1$ unknowns.  Multiplying
each row by $((m+1)n)!$ gives an integer matrix, so its maximal minors give
an exact integer normalization of $Q$; multiplying the truncated
numerators by $(mn)!$ clears their remaining factorial denominators.

The advertised combination "order about $(m+1)n$ with every type-II
polynomial of degree $n$" is not the diagonal type-II dimension.  If
$Q,P_1,\ldots,P_m$ all have degree at most $n$, the numerators first
absorb the coefficients through degree $n$.  Every additional Taylor order
costs $m$ independent conditions on the $n+1$ coefficients of $Q$.
Normality of the exponential system therefore gives only



$$
\operatorname{ord}_0(Qe^{jz}-P_j)
                    \leq n+1+\left\lfloor{n\over m}\right\rfloor. \tag{45}
$$



Thus type II attains (43) by raising its denominator degree to $mn$, not by
retaining degree $n$.

The cofactors of the adjacent type-I matrix in Section 5 give the usual
Mahler-dual coefficient system.  The identity



$$
\operatorname{adj}(\mathcal A)\mathcal A
                         =c_{m,n}z^U I                            \tag{46}
$$



shows exactly where the dual denominator occurs.  A full type-II
cross-product which eliminates all exponential coordinates recovers the
same monomial $c_{m,n}z^U$.  Exact endpoint clearing again cancels
$N^{-U}$.  Partial cross-products such as



$$
P_jP_k-QP_{j+k}                               \tag{47}
$$



are polynomials in $z$; at $z=ie/N$ they are nonconstant polynomial
values in $e$, unless they vanish as formal Padé identities.  Type-II
duality therefore does not repair the missing algebraic norm.

## 8. Comparison with available transcendence measures

The fixed functions



$$
f_1(z)=e^z,\qquad f_2(z)=e^{isz/N}              \tag{48}
$$



are algebraically independent over $\overline{\mathbb Q}(z)$ under (1), by
the same distinct-exponent argument as Section 1.  The uniform
Adamczewski--Faverjon algebraic-independence measure for two fixed
$E$-functions applies after the routine fixed coefficient-field reduction.
For a polynomial of degree $D=O_m(n)$ and height $H$, the currently
available constants permit a lower logarithm of the shape



$$
-\exp\big(CD^4\log(D+1)\big)-C'D^2\log H.                       \tag{49}
$$



With $\log H=n\log n+O(n)$, (49) is vastly below the selected upper
logarithm $-mn\log n+O(n)$.  Even discarding its double-exponential term,
the height term allows $-\Theta(n^3\log n)$.

Alternatively, expand (21) into the



$$
M_n=(m+1)(n+1)                           \tag{50}
$$



values of the functions $e^{(r+jis/N)z}$ at $z=1$.  If $d$ is the
degree of a fixed number field containing the exponents and coefficients,
the Fischler--Rivoal linear-form theorem gives, for each fixed vector and
$\varepsilon>0$, a height exponent of the form



$$
2dM_n^{2d}-1+\varepsilon.                  \tag{51}
$$



This grows with $n$, whereas the Padé height exponent in (26) is the fixed
number $m$; the theorem's constant also varies with the expanding vector.
Even the sharper imaginary-quadratic exponent $M_n-1+\varepsilon$, when
available, grows linearly with $n$ and does not conflict with (26).

After eliminating $Y$, the best scale in (40) is merely exponential in
$n$ for a polynomial in $e$ of degree $O_m(n)$ and logarithmic height
$O_m(n\log n)$.  The current one-variable transcendence measure for $e$
allows values far smaller than this.  No known quantitative theorem closes
the gap.

## 9. Reproducible finite checks

The companion script

`scripts/nested_multi_exponential_hp_certificate.py`

uses exact rational arithmetic to check:

1. the order and leading coefficient in (11), and the clearing (19), for
   $1\leq m\leq4$, $0\leq n\leq4$;
2. the determinant (32), the clearing (33), and the integer coefficient
   (35), for $1\leq m\leq3$, $0\leq n\leq3$;
3. the standard and degree-restricted type-II ranks for
   $1\leq m\leq4$, $1\leq n\leq6$;
4. the variance formula (14) in 56 cases.

Its deterministic output is

`results/nested_multi_exponential_hp_certificate.json`.

These finite checks are certificates of the implementation and small
instances.  The all-parameter statements above follow from the displayed
residue, divisibility, determinant, and Dirichlet arguments.

## Final assessment

The saturated type-I construction is a genuine analytic improvement:



$$
|\mathcal P^{\rm prim}(e,e^{is/N})|
                       =H^{-m+o(1)}.                              \tag{52}
$$



For every fixed $N,m$, however, this is a small transcendental value at an
algebraically independent pair.  Coefficient Galois products remain
transcendental polynomial values; Fourier projection leaves $e$ or the
exponential generator; resultants pay the full $m$-column height cost and
leave a polynomial in $e$; the canonical adjacent/type-II elimination is
the exact monomial (32); and the only algebraic endpoint determinant has the
noncontracting norm (38).  Present transcendence measures are much too weak
to turn the residual polynomial values into a contradiction.

Accordingly, this fixed multi-exponential Hermite--Padé route does not prove
or disprove the transcendence of $e+\pi$.
