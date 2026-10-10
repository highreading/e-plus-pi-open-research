> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Smallest non-split rational extensions of the explicit
# exponential/logarithmic system

Date: 2026-08-27 (UTC)

## 1. Question and verdict

The companion audit
`sources/explicit_mixed_pair_tensor_gauge_no_go.md` proves that
tensor constructions, split stabilizations, and rational gauges do
not add an arithmetic constraint to the elementary connection matrix
containing $e$ and $-\pi$. This note analyzes the remaining
possibility: a genuinely non-split rational extension coupling the
exponential and logarithmic pieces.

Assume, only to test the route, that


$$
({\rm H})\qquad s=e+\pi\in\overline{\mathbb Q}.       \tag{1}
$$


Write


$$
x=e^z,\qquad y=-4\arctan z,qquad
q=y'=-\frac4{1+z^2}.                                \tag{2}
$$



There is a complete low-rank classification. Retaining both the
rank-two logarithmic block and the rank-one exponential block requires
rank at least three. In a block-compatible basis, every rank-three
extension in either direction is determined by one rational row or
column $B$, modulo an explicit first-order rational coboundary. The
splitting equations are displayed in Section 3.

The obvious system whose solution is exactly


$$
x-y=e^z+4\arctan z                               \tag{3}
$$


is split: the rational change of variable $w\mapsto w+y$ separates
the exponential line. A genuine coupling necessarily introduces a
new exponential/logarithmic iterated integral.

An explicit smallest example is obtained from


$$
r(z)=\frac1{z-2},                                  \tag{4}
$$


which is regular at the base and evaluation points $0,1$. Define


$$
\begin{aligned}
J(z)&=e^z\int_0^z\frac{e^{-t}}{t-2}\,dt,\\
K(z)&=e^z\int_0^z
       \frac{e^{-t}(-4\arctan t)}{t-2}\,dt.          \tag{5}
\end{aligned}
$$


The non-split rank-three extension in Section 5 has a normalized
connection entry equal to


$$
e+\pi+K(1).                                         \tag{6}
$$


Moreover,


$$
K(1)>0.                                             \tag{7}
$$


Thus the genuine extension does not isolate $e+\pi$; it contaminates
it by a new nonzero period. Removing that term returns to the split
class, at least in this explicit algebraic one-parameter family.

The new functional data are maximal. The four functions


$$
x,\quad y,\quad J,\quad K                           \tag{8}
$$


are algebraically independent over $\mathbb C(z)$, and the
differential Galois group is the four-dimensional solvable group


$$
G_{\rm ns}=
\left\{
\begin{pmatrix}
1&0&0\\
b&1&0\\
u&v&a
\end{pmatrix}:
a\in\mathbb G_m,\ b,u,v\in\mathbb G_a
\right\}.                                         \tag{9}
$$


Monodromy around $i$ and around the new pole $2$ has a nonzero
central commutator. This proves that the coupling is genuinely
Heisenberg-like rather than a disguised direct sum.

This larger Picard--Vessiot group gives no stronger numerical
specialization theorem. Its connection field is


$$
\overline{\mathbb Q}(e,\pi,J(1),K(1)).              \tag{10}
$$


Under (1), it has transcendence degree at most three, whereas
$\dim G_{\rm ns}=4$. A conjectural connection-period injectivity
theorem would contradict (1), but no proved monodromy,
Siegel--Shidlovskii, $E$-operator, $1$-period, or exponential-
period theorem supplies that numerical lower bound. The extension
has enlarged the missing period problem from two constants to four.

No conclusion about the arithmetic nature of $e+\pi$ is claimed.

## 2. Why rank three is the first relevant size

The logarithmic coordinate is represented by the nontrivial
two-dimensional unipotent block


$$
A_U=
\begin{pmatrix}0&0\\q&0\end{pmatrix},
\qquad
\Phi_U=
\begin{pmatrix}1&0\\y&1\end{pmatrix}.              \tag{11}
$$


The exponential line has matrix $(1)$ and fundamental solution
$x=e^z$.

A differential module which retains $U$ as a subquotient and the
exponential line as another subquotient has rank at least
$2+1=3$. A two-dimensional faithful tensor representation of
$\mathbb G_m\times\mathbb G_a$ does exist--it is the tensor
matrix


$$
\begin{pmatrix}x&0\\xy&x\end{pmatrix},             \tag{12}
$$


but it belongs to the old Picard--Vessiot category and produces the
product $e\pi$, not separate additive connection coordinates. It
was exhausted by the tensor/gauge no-go.

There are also rank-two extensions of a trivial line by an
exponential line. They are useful as a warm-up but do not retain the
original logarithmic block. In lower-triangular orientation,


$$
A_r^{(2)}=
\begin{pmatrix}0&0\\r(z)&1\end{pmatrix},
\qquad
\Phi_r^{(2)}=
\begin{pmatrix}1&0\\J_r(z)&e^z\end{pmatrix},        \tag{13}
$$


where


$$
J_r(z)=e^z\int_0^z r(t)e^{-t}\,dt.                 \tag{14}
$$


The extension splits over $\overline{\mathbb Q}(z)$ exactly when


$$
r=R'-R\qquad(R\in\overline{\mathbb Q}(z));          \tag{15}
$$


then $J_r=R(z)-e^zR(0)$. In the opposite triangular orientation,
the splitting equation is $r=R'+R$.

Every polynomial $r$ is in the image of both $D-1$ and $D+1$
on polynomials: in the monomial basis these maps are triangular with
nonzero diagonal $-1$ and $1$, respectively. Hence a genuinely
non-split rational rank-two extension needs a finite pole. Its new
integral then has nontrivial logarithmic monodromy whenever the local
exponential residue is nonzero. Such a solution is not an entire
$E$-function; the monodromy jump is a nonzero multiple of $e^z$,
which also rules out the regular-singular growth of a $G$-function.

For $r=1/(z-2)$, (15) has no rational solution. If $R$ had a pole
of order $m\geq1$ at $2$, then $R'-R$ would have an uncancelled
pole of order $m+1$, whereas $r$ has order one. If $R$ were
regular at $2$, its left side would be regular there. Both cases
are impossible.

This rank-two warm-up already shows the tradeoff: non-splitting adds
a new exponential-integral connection constant rather than forcing a
relation between the old $e$ and $\pi$.

## 3. Classification of all rank-three cross extensions

Let $k=\overline{\mathbb Q}$. Once the submodule and quotient bases
are fixed, an extension in either direction has one of the following
two forms.

### 3.1 A logarithmic block below an exponential quotient

Let $B=(b_0,b_1)^T\in k(z)^2$, and put


$$
A_+(B)=
\begin{pmatrix}
A_U&B\\
0&1
\end{pmatrix}.                                     \tag{16}
$$


It has normalized fundamental matrix


$$
\Phi_+(z)=
\begin{pmatrix}
\Phi_U(z)&Z_+(z)\\
0&e^z
\end{pmatrix},                                     \tag{17}
$$


where


$$
Z_+(z)=\Phi_U(z)
\int_0^z\Phi_U(t)^{-1}B(t)e^t\,dt.                 \tag{18}
$$



A block gauge by a rational column $S=(s_0,s_1)^T$ splits the
extension exactly when


$$
B=S'+S-A_US.                                        \tag{19}
$$


In coordinates, this is


$$
b_0=s_0'+s_0,qquad
b_1=s_1'+s_1-q s_0.                                \tag{20}
$$



### 3.2 An exponential line below a logarithmic quotient

Let $B=(b_0,b_1)\in k(z)^2$, and put


$$
A_-(B)=
\begin{pmatrix}
A_U&0\\
B&1
\end{pmatrix}.                                     \tag{21}
$$


Its normalized fundamental matrix is


$$
\Phi_-(z)=
\begin{pmatrix}
\Phi_U(z)&0\\
Z_-(z)&e^z
\end{pmatrix},                                     \tag{22}
$$


with


$$
Z_-(z)=e^z\int_0^z e^{-t}B(t)\Phi_U(t)\,dt.        \tag{23}
$$


Writing $R=(r_0,r_1)$, the change
$w\mapsto w-RU$ splits this extension exactly when


$$
B=R'+RA_U-R.                                        \tag{24}
$$


Equivalently,


$$
b_0=r_0'+q r_1-r_0,qquad
b_1=r_1'-r_1.                                      \tag{25}
$$



Equations (19) and (24) prove that the classification is a rational
de Rham/cohomology quotient, not a visual test on whether the matrix
has off-diagonal entries. A dense-looking coefficient matrix can be
split, while a single rational pole can carry a nonzero extension
class.

All systems in (16) and (21) are ordinary at $0,1$ provided the
entries of $B$ are regular there. Thus ordinary-point regularity
places no restriction on poles such as $2$, $i$, or $-i$.

## 4. The exact $e+\pi$ carrier is split

In the lower orientation, choose


$$
B_0=(-q,1).                                         \tag{26}
$$


Then (25) holds with


$$
R=(0,-1).                                           \tag{27}
$$


Equivalently, for


$$
c'=0,\qquad y'=qc,qquad
w'=w-qc+y,                                          \tag{28}
$$


the rational algebraic change


$$
\widetilde w=w+y                                   \tag{29}
$$


gives $\widetilde w'=\widetilde w$. The normalized
fundamental matrix before splitting is


$$
\Phi_0(z)=
\begin{pmatrix}
1&0&0\\
y&1&0\\
-y&e^z-1&e^z
\end{pmatrix}.                                     \tag{30}
$$


For the algebraic initial vector $(1,0,1)^T$, the bottom solution is


$$
w(z)=e^z-y(z),qquad w(1)=e+\pi.                   \tag{31}
$$


Thus the lowest-order differential equation carrying the target
exactly is only a constant rational gauge of $U\oplus E$. This is
precisely the split case already covered by endpoint-field invariance.

The weight explanation is the same: $U$ has
$\mathbb G_m$-weight zero and $E$ has weight one. An extension
trivialized inside the old Picard--Vessiot field must split across
these distinct central weights. Therefore a non-split cross extension
must add a new Picard--Vessiot generator.

## 5. An explicit genuinely coupled family

Let $r\in k(z)$ be regular at $0,1$, and perturb (26) to


$$
B_r=(-q,1+r).                                       \tag{32}
$$


The system is


$$
\begin{pmatrix}c\\y\\w\end{pmatrix}'
=A_r(z)\begin{pmatrix}c\\y\\w\end{pmatrix},
\qquad
A_r(z)=
\begin{pmatrix}
0&0&0\\
q&0&0\\
-q&1+r&1
\end{pmatrix}.                                     \tag{33}
$$


After the split change $u=w+y$, the final equation becomes


$$
u'=u+r(z)y.                                         \tag{34}
$$


Thus $r y$, rather than a removable copy of $y$, is the genuine
cross term.

If (33) split rationally, the second equation of (25) would give


$$
r_1'-r_1=1+r.                                      \tag{35}
$$


Putting $R=r_1+1$ would imply


$$
R'-R=r.                                             \tag{36}
$$


For the explicit choice (4), the pole-order proof following (15)
shows that (36) is impossible. Hence (33) is genuinely non-split.

Define $J,K$ by (5). They satisfy


$$
J'=J+r,qquad K'=K+r y,qquad J(0)=K(0)=0.          \tag{37}
$$


A normalized fundamental matrix of (33) is


$$
\Phi_r(z)=
\begin{pmatrix}
1&0&0\\
y&1&0\\
-y+K&e^z-1+J&e^z
\end{pmatrix}.                                     \tag{38}
$$


Direct differentiation proves $\Phi_r'=A_r\Phi_r$.

At $z=1$, put $J_1=J(1)$, $K_1=K(1)$. Then


$$
C_r=\Phi_r(1)=
\begin{pmatrix}
1&0&0\\
-\pi&1&0\\
\pi+K_1&e-1+J_1&e
\end{pmatrix}.                                     \tag{39}
$$


The algebraic initial vector $(1,0,1)^T$ has bottom value


$$
e+\pi+K_1.                                         \tag{40}
$$



If one insists on a literal entry of a normalized connection matrix,
use the unimodular endpoint-regular gauge


$$
P(z)=I_3-(1-z)E_{31}.                               \tag{41}
$$


Here $P(1)=I$ and $P(0)^{-1}=I+E_{31}$, so the transformed
connection matrix is


$$
\widetilde C_r=C_r(I+E_{31}),                      \tag{42}
$$


and


$$
(\widetilde C_r)_{31}=e+\pi+K_1.                  \tag{43}
$$


The gauge merely selects the matrix coefficient; it does not split
the nonzero extension class.

For (4), the length-one new period has the exact form


$$
J_1=e^{-1}\bigl(\operatorname {Ei}(1)
                 -\operatorname {Ei}(2)\bigr),     \tag{44}
$$


and the genuinely mixed length-two period is


$$
K_1=-4e\int_0^1
\frac{e^{-t}\arctan t}{t-2}\,dt.                  \tag{45}
$$


On $0<t<1$, both $1/(t-2)$ and
$y(t)=-4\arctan t$ are negative. Therefore the integrand in the
definition (5) of $K_1$ is positive and (7) follows.

More generally, replace $r$ by $\lambda r$,
$\lambda\in k$. The selected connection entry is


$$
e+\pi+\lambda K_1.                                 \tag{46}
$$


Because $K_1>0$, (46) equals $e+\pi$ exactly when
$\lambda=0$, which is the split member of this family. Thus this
explicit algebraic family rigorously exhibits the tradeoff between
non-splitting and contamination by a new period.

## 6. The new differential Galois group is four-dimensional

The non-split extension has not merely changed the coefficient matrix.
It has enlarged the functional field.

### 6.1 Differential automorphisms

Every differential automorphism has the possible form


$$
\begin{aligned}
x&\longmapsto ax,\\
y&\longmapsto y+b,\\
J&\longmapsto J+cx,\\
K&\longmapsto K+bJ+dx,                             \tag{47}
\end{aligned}
$$


because these transformations preserve (37). Relative to (38), its
constant matrix is


$$
g(a,b,c,d)=
\begin{pmatrix}
1&0&0\\
b&1&0\\
-b+d&a+c-1&a
\end{pmatrix}.                                     \tag{48}
$$


As $a\ne0$ and $b,c,d$ vary, (48) is exactly the group (9).

### 6.2 Monodromy proves algebraic independence

The old functions $x,y$ are algebraically independent over
$\mathbb C(z)$. It remains to prove that $J,K$ add two more
independent generators.

Around $z=2$, the integrand defining $J/e^z$ has residue
$e^{-2}$. Hence positive monodromy gives


$$
J\longmapsto J+\kappa x,
\qquad
\kappa=2\pi i e^{-2}\ne0.                          \tag{49}
$$


The functions $x,y$ are single-valued around $2$. Iterating this
loop would give infinitely many roots $J+n\kappa x$ of any proposed
algebraic equation for $J$ over $\mathbb C(z)(x,y)$. Therefore


$$
J\text{ is transcendental over }\mathbb C(z)(x,y). \tag{50}
$$



To treat $K$, use one loop around $i$ and one around $2$.
Write


$$
B=-4\pi.                                           \tag{51}
$$


The two monodromy matrices have the forms


$$
T_i=
\begin{pmatrix}
1&0&0\\
B&1&0\\
\delta_i-B&0&1
\end{pmatrix},
\qquad
T_2=
\begin{pmatrix}
1&0&0\\
0&1&0\\
\lambda_2&\kappa&1
\end{pmatrix}.                                     \tag{52}
$$


The constants $\delta_i,\lambda_2$ depend on the chosen based
paths, but they cancel from the commutator. Exact multiplication gives


$$
T_iT_2T_i^{-1}T_2^{-1}
=I_3-B\kappa E_{31},                               \tag{53}
$$


where


$$
-B\kappa=8\pi^2 i e^{-2}\ne0.                     \tag{54}
$$


This commutator fixes $x,y,J$ and translates $K$ by a nonzero
constant multiple of $x$. Its iterates prove


$$
K\text{ is transcendental over }
\mathbb C(z)(x,y,J).                               \tag{55}
$$



Equations (50) and (55) give


$$
\operatorname {trdeg}_{\mathbb C(z)}
\mathbb C(z)(x,y,J,K)=4.                           \tag{56}
$$


The group (48) is an a priori four-dimensional containing group, so
(56) proves that the differential Galois group is the full group (9).
The unipotent radical at $a=1$ is the three-dimensional lower
unitriangular, or Heisenberg, group. Equation (53) is its nonzero
central commutator and is the exact certificate of genuine coupling.

## 7. Why the larger group does not strengthen specialization

### 7.1 The numerical period map has simply gained two variables

The entries of (39) recover all four constants:


$$
e=(C_r)_{33},\qquad
\pi=-(C_r)_{21},\qquad
J_1=(C_r)_{32}-e+1,\qquad
K_1=(C_r)_{31}-\pi.                                \tag{57}
$$


Thus the connection field is exactly (10).

Functional Picard--Vessiot theory proves the four-variable statement
(56). It does not prove


$$
\operatorname {trdeg}_{k}
k(e,\pi,J_1,K_1)=4.                                \tag{58}
$$


Under (1), the left side is at most three because
$\pi=s-e$. A theorem proving (58) would settle the target, but that
would be a numerical connection-period injectivity theorem, not a
consequence of the computed differential Galois group.

### 7.2 The new functions are neither pure $E$ nor pure $G$

Monodromy (49) shows that $J$ is not entire. The local residue for
$K$ at $2$ is $e^{-2}y(2)\ne0$, so $K$ is also multivalued.
Neither is an $E$-function.

Their monodromy jumps contain nonzero multiples of $e^z$. If either
were a $G$-function, all branches of its minimal $G$-operator
would have regular-singular, hence polynomial-logarithmic, growth at
infinity. The difference of two continued branches would then have
the same moderate growth, contradicting the $e^z$ jump. Thus neither
is a $G$-function.

Accordingly, Beukers' pure $E$-function specialization theorem does
not apply to the vector (38), and pure $G$/period theorems do not
apply to the new exponential integrals.

### 7.3 Arithmetic connection membership is not independence

The constants (44)--(45) are explicit exponential periods. The first
is a length-one exponential integral; the second is the length-two
iterated integral


$$
K_1=e\int_{0<u<t<1}
e^{-t}\frac{q(u)}{t-2}\,du\,dt.                    \tag{59}
$$


Arithmetic $E$-operator and $E$-period theories provide rings and
geometric realizations in which constants of this kind live. Their
proved theorems do not assert (58), nor a lower bound for a mixed
linear form involving $e,\pi,J_1,K_1$.

Even proving $K_1$ transcendental would not contradict (1): under
(1), (43) would simply equal the transcendental number $s+K_1$.
What is needed is separation of $e$ from $\pi$, not the addition
of a separately complicated period.

### 7.4 Path and commutator data do not remove the absolute period

Changing the connection path changes $J_1,K_1$ by the monodromy
increments in (49)--(54). Differences of two path values eliminate
the absolute connection constants and recover those increments. They
also eliminate the common $e+\pi$ term in (43). Thus monodromy
differences provide the already computed functional group, not an
algebraic value for the absolute target.

The ratio of the basic monodromy steps contains $e^{-2}$, but Ramis
density works over $\mathbb C$ and uses only that these steps are
nonzero. It imposes no arithmetic relation between their chosen
normalization and the connection entry $e$.

## 8. Sharp classification of the survivor

The rank-three classification gives the following exhaustive
dichotomy.

**Theorem 8.1.** Let a rank-three rational differential system,
ordinary at $0,1$, be an extension in either direction between the
logarithmic block $U$ and the exponential line $E$.

1. If its row or column $B$ satisfies the corresponding rational
   coboundary equation (19) or (24), the system is rationally split.
   Its connection matrix is an algebraic endpoint transform of
   $C_U\oplus(e)$, so an occurrence of $e+\pi$ is only the old
   target repackaged.
2. If the coboundary equation has no rational solution, the
   variation-of-constants matrix (18) or (23) contains at least one
   genuinely new Picard--Vessiot function. Any equality between its
   value at $1$ and an algebraic combination of $e,\pi$ is a new
   exponential-period relation, not a formal consequence of the
   extension.

For the explicit cross family (32) with
$r=\lambda/(z-2)$, $\lambda\in k$, the target-carrying entry is
exactly (46). It is uncontaminated if and only if $\lambda=0$, the
split case. For $\lambda\ne0$, the full functional Galois group is
larger and the numerical period problem has an additional variable.

For a more general rational $r$, it is logically possible that the
new iterated integral happens to vanish or satisfy an algebraic
relation at $1$ even though its function is new. Proving such a
numerical cancellation would itself be an arithmetic connection
theorem. Raw extension cohomology cannot supply it.

Therefore the exact surviving research targets are:

* find a non-split class whose new connection periods can be
  controlled by an existing arithmetic theorem and cancel without
  assuming the desired relation; or
* prove period-map injectivity for either the original
  $\mathbb G_m\times\mathbb G_a$ system or the larger group (9).

The explicit example shows that merely making the module non-split,
noncommutative, and functionally maximally independent does not
produce the needed numerical specialization.

## 9. Replayable exact certificate

The deterministic files are

* `scripts/explicit_nonsplit_mixed_extension_certificate.py`;
* `results/explicit_nonsplit_mixed_extension_certificate.json`.

They verify:

1. the differential equations (37);
2. $\Phi_r'=A_r\Phi_r$ and $\Phi_r(0)=I_3$;
3. rational splitting of the $r=0$ system;
4. the endpoint-regular gauge (41) and the exact entry (43);
5. the exponential-integral formula (44);
6. the generic differential-Galois action (47)--(48);
7. the exact monodromy commutator (53).

The pole-order nonsplitting proof and the algebraic-independence proof
are mathematical arguments archived above; they do not rely on
finite numerical experiments.

## 10. Primary sources and provenance

1. F. Beukers, *A refined version of the Siegel--Shidlovskii theorem*,
   Ann. of Math. **163** (2006), 369--379,
   [arXiv:math/0405549](https://arxiv.org/abs/math/0405549).
2. Y. Andr\'e, *S\'eries Gevrey de type arithm\'etique, I. Th\'eor\`emes
   de puret\'e et de dualit\'e*, Ann. of Math. **151** (2000),
   705--740,
   [arXiv:math/0003238](https://arxiv.org/abs/math/0003238).
3. S. Fischler and T. Rivoal, *Arithmetic theory of
   $E$-operators*, J. \`Ec. polytech. Math. **3** (2016), 31--65,
   [arXiv:1406.5995](https://arxiv.org/abs/1406.5995).
4. J. Fres\'an and P. Jossen, *Exponential motives*, especially the
   exponential period conjecture,
   [author PDF](https://javier.fresan.perso.math.cnrs.fr/expmot.pdf).
5. B. Snodgrass, *Periods of $E$-operators*,
   [arXiv:2608.06005v2](https://arxiv.org/abs/2608.06005).
6. T. Dreyfus, *A density theorem for parameterized differential
   Galois theory*, Pacific J. Math. **271** (2014), 87--141,
   [arXiv:1203.2904](https://arxiv.org/abs/1203.2904). The present
   group computation is elementary and does not depend on the
   parameterized theorem.

Relevant archived source hashes are listed in the two companion
audits. The exact new certificate replay is:

| Artifact | SHA-256 |
|---|---|
| Certificate script | `22527f6b416b249f4510c209860ba44aeae5ef26ec99f5e7d0ebb3c1c98478a0` |
| Byte-identical result | `cfa1b203629f61f4c538b29b4a1c381f72517e809aa05528f9fdfb6724283ff0` |
| Tensor/gauge companion source | `bb8347a7cd1cd91df990a5b09142bfadcfa18d6c273bf4070f4415c05393e36c` |

## 11. Final conclusion

The smallest relevant extension problem is completely explicit.
Rational extension matrices are classified by (19) and (24). The
functional solution that gives $e+\pi$ without an extra term is
split. The first genuinely cross-coupled example adds the nonzero
iterated exponential/logarithmic period $K_1$, and its differential
Galois group becomes the full four-dimensional solvable group (9).

Under (1), the selected connection entry is


$$
s+K_1,                                             \tag{60}
$$


which is perfectly compatible with every proved theorem audited here.
The larger group proves that $K$ is functionally new; it does not
prove an arithmetic lower bound for the numerical field generated by
$e,\pi,J_1,K_1$. Thus non-splitting alone enlarges the period
torsor but does not close the specialization gap.
