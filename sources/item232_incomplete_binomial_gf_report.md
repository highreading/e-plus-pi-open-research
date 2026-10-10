> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 232 — algebraic generating function and Ore reduction of the incomplete-binomial coordinate

## 1. Outcome

Item 229 leaves the integer



$$
S_n=\sum_{j=0}^{n}(-1)^j\binom{2n+j-1}{j},\qquad S_0=1,       \tag{1.1}
$$



in the corrected $j=1$ determinant.  This item proves that its ordinary
generating function is algebraic.  If $X\in z\mathbb Q[[z]]$ is the unique
solution of



$$
X={z\over(1+X)^2},                    \tag{1.2}
$$



then



$$
\boxed{\mathcal G(z):=\sum_{n\geq0}S_nz^n
       ={1+X\over(1-X)(1+3X)}.}                              \tag{1.3}
$$



An exact differential certificate gives the proposed order-two polynomial
recurrence.  More importantly, that recurrence factors in the Ore ring.  The
factorization identifies the first difference $S_{n+1}-S_n/4$ with the
boundary binomial already present in Item 229:



$$
\boxed{2n(2n+1)(4S_{n+1}-S_n)
       =(28n^2+25n+5)(-1)^{n+1}\binom{3n}{n+1}.}              \tag{1.4}
$$



Thus the two residual coordinates of Item 229 are related, but at adjacent
indices.  A collision at the row $s$ supplies no collision equation at
$s+1$.  Consequently (1.4) does not by itself eliminate the remaining
coordinate, exclude any all-prime family, or book a positive Route-1 rate.

## 2. Formal diagonal and generating function

The generalized binomial theorem gives



$$
[x^j](1+x)^{-2n}=(-1)^j\binom{2n+j-1}{j}.
$$



Taking a partial sum is the same as multiplying by $(1-x)^{-1}$, so



$$
S_n=[x^n]{1\over1-x}(1+x)^{-2n}.          \tag{2.1}
$$



We use the following standard formal diagonal form of Lagrange inversion.
If $X=z\phi(X)$, $\phi(0)=1$, then



$$
\sum_{n\geq0}z^n[x^n]A(x)\phi(x)^n
             ={A(X)\over1-z\phi'(X)}.                        \tag{2.2}
$$



Indeed, the left side is the formal constant term



$$
\operatorname {CT}_x{A(x)\over1-z\phi(x)/x},
$$



and the formal residue at the unique small root $x=X$ of
$x-z\phi(x)$ is the right side of (2.2).  Apply (2.2) with



$$
A(x)={1\over1-x},\qquad \phi(x)=(1+x)^{-2}.
$$



Since $z\phi'(X)=-2X/(1+X)$, equation (1.3) follows immediately.
This is a formal-power-series proof; no analytic convergence or finite
interpolation is being used.

Eliminating $X$ from (1.2)--(1.3) also gives the explicit algebraic
equation



$$
\boxed{(16+104z-27z^2)\mathcal G^3
 -(16+108z)\mathcal G^2+21z\mathcal G-z=0.}                  \tag{2.3}
$$



The companion checker verifies (2.3) as a rational-function identity after
the substitution $z=X(1+X)^2$.

## 3. Exact polynomial recurrence

Let



$$
\begin{aligned}
 P_0(n)&=-(348+2052n+3921n^2+2943n^3+756n^4),\\
 P_1(n)&=1332+7838n+14978n^2+11280n^3+2912n^4,\\
 P_2(n)&=240+1480n+2824n^2+1968n^3+448n^4.                 \tag{3.1}
\end{aligned}
$$



Then, for every integer $n\geq0$,



$$
\boxed{P_0(n)S_n+P_1(n)S_{n+1}+P_2(n)S_{n+2}=0.}           \tag{3.2}
$$



Here is an exact certificate for (3.2).  Put



$$
z=X(1+X)^2,\qquad
 g(X)={1+X\over(1-X)(1+3X)},\qquad
 \mathscr D={X(1+X)\over1+3X}{d\over dX}.                  \tag{3.3}
$$



The operator $\mathscr D$ is $z\,d/dz$ under this parametrization.
Direct rational differentiation and cancellation give



$$
z^2P_0(\mathscr D)g+zP_1(\mathscr D-1)g
                    +P_2(\mathscr D-2)g=40z.                \tag{3.4}
$$



The checker performs this calculation over $\mathbb Q(X)$ and obtains an
identically zero numerator after subtracting $40z$.  Taking the coefficient
of $z^{n+2}$ in (3.4) proves (3.2).  The low-degree term $40z$ only
accounts for the initial boundary.  In addition,



$$
P_2(n)=8(n+2)(2n+3)(28n^2+25n+5)>0\quad(n\geq0),           \tag{3.5}
$$



so (3.2), together with $S_0=1,S_1=-1$, uniquely determines the sequence.

## 4. Ore factorization and the boundary coordinate

Set



$$
Q(n)=28n^2+25n+5.                 \tag{4.1}
$$



The end coefficients factor as



$$
\begin{aligned}
 P_0(n)&=-3(3n+1)(3n+2)Q(n+1),\\
 P_2(n)&= 8(n+2)(2n+3)Q(n),                                 \tag{4.2}
\end{aligned}
$$



and the middle coefficient obeys



$$
16P_0+4P_1+P_2=0.                  \tag{4.3}
$$



If $E$ denotes the forward shift, (4.2)--(4.3) give the exact Ore
factorization



$$
P_0+P_1E+P_2E^2=(-4P_0+P_2E)(E-\tfrac14).                  \tag{4.4}
$$



Consequently



$$
u_n:=S_{n+1}-{S_n\over4}
$$



is hypergeometric and satisfies



$$
{u_{n+1}\over u_n}={4P_0(n)\over P_2(n)},\qquad u_0=-{5\over4}.             \tag{4.5}
$$



Using (4.2) and telescoping the products in (4.5) yields



$$
\boxed{u_n={(-1)^{n+1}Q(n)\over4(n+1)(2n+1)}\binom{3n}{n}.} \tag{4.6}
$$



For $n\geq1$,



$$
(-1)^{n+1}\binom{3n}{n+1}
 ={2n\over n+1}(-1)^{n+1}\binom{3n}{n}.                    \tag{4.7}
$$



Equations (4.6)--(4.7) prove (1.4).  The denominator-free form (1.4)
also remains true, trivially, at $n=0$.

This factorization explains the two leading characteristic roots of (3.2),
$1/4$ and $-27/4$, but no asymptotic or density claim is needed here.

## 5. Exact rewrite of the Item 229 determinant

To avoid confusing the generating function $\mathcal G$ with Item 229's
rational coefficient, denote the latter by $G_h(s)$.  Item 229 proves



$$
\Theta_h(s)=c_h(s)S_s+t_{s+1}G_h(s)-2\Delta_-(h,s),
 \qquad t_{s+1}=(-1)^{s+1}\binom{3s}{s+1}.                  \tag{5.1}
$$



Multiplying (5.1) by $Q(s)$ and using (1.4) gives the all-$h$, all-$s$
identity



$$
\boxed{\begin{aligned}
 Q(s)\Theta_h(s)={}&
  \bigl(Q(s)c_h(s)-2s(2s+1)G_h(s)\bigr)S_s\\
 &+8s(2s+1)G_h(s)S_{s+1}-2Q(s)\Delta_-(h,s).
\end{aligned}}                                               \tag{5.2}
$$



This is a genuine Ore reduction: the separate boundary binomial has been
removed.  It is not a scalar elimination, because $S_{s+1}$ appears.
Modulo a row prime, (5.2) is equivalent to $\Theta_h(s)=0$ only when
$Q(s)$ is a unit.  At the Item 229 row phase



$$
s_*=-{4h+3\over6},
$$



one has



$$
Q(s_*)={224h^2+36h-9\over18}.              \tag{5.3}
$$



Thus any future argument that divides by $Q$ must separately control the
quadratic exceptional locus in (5.3).

## 6. Same-row Frobenius lift and the limit of direct Cartier reduction

There is a second exact description on an actual row.  Since



$$
(-1)^k\binom{2s+k-1}{k}=\binom{-2s}{k}
                      \equiv\binom{p-2s}{k}\pmod p,
$$



the row relation $p=6s+4h+3$ gives



$$
\boxed{S_s\equiv\sum_{k=0}^{s}\binom{p-2s}{k}
       =\sum_{k=0}^{s}\binom{4s+4h+3}{k}\pmod p.}            \tag{6.1}
$$



Equivalently,



$$
S_s\equiv[x^s]{(1+x)^{4s+4h+3}\over1-x}\pmod p.           \tag{6.2}
$$



This lift also has an algebraic generating function.  For fixed $h$, put



$$
A_{h,n}=\sum_{k=0}^{n}\binom{4n+4h+3}{k}.
$$



Applying the same diagonal lemma (2.2), now with
$A(x)=(1+x)^{4h+3}/(1-x)$ and $\phi(x)=(1+x)^4$, proves



$$
\boxed{\sum_{n\geq0}A_{h,n}z^n
 ={(1+Y)^{4h+4}\over(1-Y)(1-3Y)},\qquad
 Y=z(1+Y)^4.}                                                \tag{6.3}
$$



Thus (6.1)--(6.3) are a legitimate same-row algebraic reformulation.  They do
not create a neighboring collision condition.  In fact, keep one row
$(p,h,s)$ fixed and shift the coefficient index to $s+r<p$.  Freshman's
dream gives the exact drift formula



$$
\boxed{\begin{aligned}
 A_{h,s+r}\equiv[x^{s+r}]&(1-x)^{-1}(1+x)^{-2(s+r)}\\
                         &\times(1+x)^{6r}\pmod p.
\end{aligned}}                                               \tag{6.4}
$$



Only $r=0$ recovers $S_s$.  For $r>0$, the extra factor
$(1+x)^{6r}$ mixes lower coefficients of the series defining
$S_{s+r}$.  Hence the fixed-$h$ recurrence implicit in (6.3) cannot be
inserted as a recurrence for $S_n$ in a neighborhood of the collision row.

The direct Cartier viewpoint has the same precise limitation.  Over
$\mathbb F_p$, write



$$
\Lambda_a\!\left(\sum_{m\geq0}b_mz^m\right)
       =\sum_{m\geq0}b_{pm+a}z^m.
$$



Because $0<s<p$,



$$
(\Lambda_s\mathcal G)(0)=S_s.       \tag{6.5}
$$



This operation merely extracts the unknown coefficient at the moving base-$p$
digit $s$; the quotient index is already zero, so there is no descent to a
smaller coefficient.  Algebraicity ensures a finite $p$-kernel for each
fixed $p$, but neither (2.3) nor (6.3) identifies a uniform state as the
digit $s=(p-4h-3)/6$ varies with the row.  This is a scoped no-go for the
one-step diagonal/Cartier substitution, not an impossibility theorem for all
finite-field or Ore identities.

The checker replays (6.1) on all 22,934 actual rows through $p\leq2000$.
That replay is **EXACT_FINITE_ONLY**; the congruence itself is proved for every
row by the generalized-binomial calculation above.

## 7. Interface with Item 231's second same-row partial sum

Item 231 supplies a second same-row reciprocity sum.  This subsection only
records how the Item 232 recurrence interfaces with that separately certified
identity; it does not replace the Item 231 proof.  Put



$$
\begin{gathered}
 r=2h,\quad J=3h+3s+1,\quad
 A=2r+4s-1,\quad B=r+1,\quad C=-(r+8s),\\
 t_j=(-1)^j\binom{2s+j-1}{j},\qquad
 S^{(s)}_m=\sum_{j=0}^{m}t_j.                                \tag{7.1}
\end{gathered}
$$



The high reciprocity polynomial is



$$
P_{\rm hi}(j)=C\binom{2j-r-1}{r}
              +B\binom{2j-r}{r}
              +A\binom{2j-r+1}{r}.                           \tag{7.2}
$$



With the same Gosper operator as Item 229,



$$
\mathscr L_sR(j)=-(2s+j)R(j+1)-jR(j),
$$



write uniquely



$$
P_{\rm hi}(j)=c_{\rm hi}(h,s)+\mathscr L_sR_{\rm hi}(j),
 \qquad \deg_jR_{\rm hi}\leq2h-1.                            \tag{7.3}
$$



The Item 231 Frobenius difference $H=g_{a+p}-g_a$, after reciprocity,
has the exact reduced form



$$
\boxed{\begin{aligned}
 H={}&c_{\rm hi}(h,s)\,\mathcal T_{h,s}
 +(J+1)t_{J+1}R_{\rm hi}(J+1)-rt_rR_{\rm hi}(r)\\
 &-A t_J\binom{2J-r+1}{r},\\
 \mathcal T_{h,s}:={}&\sum_{j=r}^{J}t_j
       =S^{(s)}_J-S^{(s)}_{r-1}.
\end{aligned}}                                                \tag{7.4}
$$



The telescoping in (7.4) is immediate from
$(j+1)t_{j+1}=-(2s+j)t_j$.  Item 231 further shows that a collision
forces $H=-3\Delta_-$.

Equation (7.4) identifies the surviving nonhypergeometric coordinate
exactly: it is the fixed-parameter tail



$$
\boxed{\mathcal T_{h,s}
                         =S^{(s)}_J-S^{(s)}_{r-1}.}            \tag{7.5}
$$



The recurrence (3.2) acts on



$$
S_n=S^{(n)}_n,
$$



so both the binomial parameter and the upper endpoint change when $n$ is
shifted.  It does **not** act on $S^{(s)}_m$ as $m$ varies with $s$
fixed.  Consequently it supplies no relation between the low coordinate
$S^{(s)}_s$ and the high tail (7.5).  The remaining terms in (7.4) are
explicit hypergeometric endpoints $t_r,t_J$; they do not remove
$\mathcal T_{h,s}$.

At the phase $s_*=-(4h+3)/6$, Item 231's exact computations find
$c_{\rm hi}=c_h$ through $h\leq20$.  That equality is
**EXACT_FINITE_ONLY** until an all-$h$ certificate is supplied.  It is not
used here to cancel (7.5) or to claim an all-prime exclusion.

## 8. What the recurrence does and does not eliminate

For each fixed $h$, (3.2) makes the residual coordinate holonomic, and
(5.2) is suitable input for further Ore elimination.  It does not complete
that elimination for three independent reasons:

1. the collision hypothesis is a condition at one index $s$, not at
   $s+1$;
2. shifting (5.1) would describe a different row (its row prime changes by
   six), so $\Theta_h(s+1)=0$ cannot be inserted;
3. division by $Q(s)$ is not universally justified modulo the row prime.

A useful next target is therefore a second same-row transfer identity whose
residual part is linearly independent in $(S_s,S_{s+1})$, together with a
separate resultant analysis of (5.3).  Neither is supplied by the generating
function alone.  Item 231 does supply a second same-row identity, but Section 7
shows that its new partial sum is $\mathcal T_{h,s}$, outside the diagonal
sequence controlled by (3.2).

## 9. Literature status and exact equivalence

The unsigned sequence was already catalogued as
[OEIS A371813](https://oeis.org/A371813).  With the OEIS notation $a(n)$,
reindexing its defining sum by $k=n-j$ gives



$$
a(n)=\sum_{k=0}^{n}(-1)^k\binom{3n-k-1}{n-k}
     =(-1)^nS_n.                                              \tag{9.1}
$$



The OEIS algebraic form uses $g=1+xg^3$ and



$$
A(x)={g\over(2g-1)(3-2g)}.
$$



At $x=-z$, equation (1.2) gives $g(-z)=1/(1+X)$, and direct
substitution yields



$$
A(-z)=\mathcal G(z).                  \tag{9.2}
$$



The recurrence attributed there to Vaclav Kotesovec (April 7, 2024) is



$$
\begin{aligned}
8N(2N-1)(28N^2-87N+67)a_N={}&
2(1456N^4-6008N^3+8593N^2-4949N+960)a_{N-1}\\
&+3(3N-5)(3N-4)(28N^2-31N+8)a_{N-2}.            \tag{9.3}
\end{aligned}
$$



Substituting $a_N=(-1)^NS_N$ and then setting $N=n+2$ turns the
three coefficients in (9.3) exactly into $P_0(n),P_1(n),P_2(n)$ of
(3.1).  The checker verifies this shift as a polynomial identity.  Thus
Item 232 is an independent exact proof and a Route-1-specific Ore/application
analysis; it makes no novelty claim for the sequence, its algebraic generating
function, or its order-two recurrence.

## 10. Reproducibility and labels

The standard-library checker verifies (2.3) and (3.4) symbolically over
$\mathbb Q(X)$, verifies every polynomial factor in (4.2)--(4.4), and
replays (3.2), (4.6), and (1.4) through $n=400$.  The finite replay is a
regression test for the symbolic proof, not an extrapolation.

Classification:

* **PROVED:** (1.2)--(2.3), the all-$n$ recurrence (3.2), the Ore
  factorization (4.4), the boundary coupling (1.4), and the scoped Item 229
  rewrite (5.2), together with the same-row lift (6.1), its fixed-$h$
  algebraic series (6.3), the drift identity (6.4), and the exact
  sign/index equivalence with OEIS A371813.
* **EXACT_FINITE_ONLY:** the independent coefficient replay through
  $n\leq400$, the same-row congruence replay through $p\leq2000$, and
  Item 231's observed phase equality $c_{\rm hi}=c_h$ through $h\leq20$.
* **OPEN:** a second same-row condition controlling $S_{s+1}$, a universal
  unit theorem for $Q(s)$, a uniform Cartier state or scalar phase formula
  for the moving digit $s$, control of the high fixed-parameter tail
  $\mathcal T_{h,s}$, any all-prime exclusion or density theorem, and any
  positive Route-1 rate or divisibility exponent.

This item books



$$
\boxed{\text{new unconditional linear log rate}=0,\qquad
        \text{new divisibility exponent}=0.}                \tag{10.1}
$$


