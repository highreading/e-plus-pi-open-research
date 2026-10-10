> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 255 — incomplete-beta localization and the resonant reciprocal orbit

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Use the Item-253 phase notation



$$
p=6m+2d+1,\qquad d=r+4\geq5,qquad d\equiv3,5\pmod6,
 \qquad n=3m+d={p-1\over2}.                       \tag{1.1}
$$



Thus $m=s-1$ on the actual ordinary-$j=2$ row.  Define



$$
I_{m,d}=\int_0^1u^{2m+d-1}(1-2u)^m\,du.          \tag{1.2}
$$



The integral is only finite-polynomial shorthand:



$$
I_{m,d}=\sum_{k=0}^m\binom mk{(-2)^k\over2m+d+k}. \tag{1.3}
$$



> **PROVED — exact localization of the Item-252 period.**  If
> 

$$
> K_{d,m}=\sum_{k=0}^m\binom{3m+d}{k}(-1/2)^k,
>
$$


> then
> 

$$
> \boxed{
> 2^mK_{d,m}=(2m+d)\binom{3m+d}{m}I_{m,d}.}       \tag{1.4}
>
$$


> Every factor outside $I_{m,d}$ is a $p$-unit.  Since
> $K_{d,m}\equiv H_m\pmod p$,
> 

$$
> \boxed{H_m\equiv0\pmod p\iff I_{m,d}\equiv0\pmod p.}          \tag{1.5}
>
$$



> **PROVED — endpoint-retaining contiguous recurrence.**  For a unit
> parameter $c$, put
> 

$$
> M_q(c)=\int_0^1u^{2m+d+q-1}(1+cu)^m\,du.         \tag{1.6}
>
$$


> Then, exactly over $\mathbf Q(c)$,
> 

$$
> \boxed{
> (2m+d+q)M_q(c)+c(3m+d+q+1)M_{q+1}(c)
> =(1+c)^{m+1}.}                                  \tag{1.7}
>
$$


> In particular, for $c=-2$ the right side is
> $(-1)^{m+1}$; this endpoint is not discarded.

> **PROVED — exact phase reflection.**  Let $L=m+1$.  Pairing the
> denominators that sum to $p$ gives
> 

$$
> \boxed{M_L(c)\equiv-c^mM_0(c^{-1})\pmod p.}      \tag{1.8}
>
$$


> Thus $I_{m,d}=M_0(-2)$ is paired with the reciprocal companion
> $M_0(-1/2)$, not with a second copy of itself.

> **PROVED, SHARPLY SCOPED NO-GO — the natural two-moment orbit is
> resonant.**  Iterating (1.7) through $L=m+1$ steps has homogeneous
> multiplier
> 

$$
> A_c=\left(-{1\over c}\right)^L
> { (2m+d)_L\over(3m+d+1)_L}\equiv c^{-L}\pmod p. \tag{1.9}
>
$$


> Combining the iterations for $c$ and $c^{-1}$ with (1.8) gives a
> linear system for $X=M_0(c)$, $Y=M_0(c^{-1})$ whose coefficient
> matrix is
> 

$$
> \boxed{
> \begin{pmatrix}c^{-L}&c^m\\c^{-m}&c^L\end{pmatrix}.}           \tag{1.10}
>
$$


> Its determinant is zero; indeed the second row is $c$ times the
> first because $L=m+1$.  The affine endpoint constants satisfy the
> same compatibility.  Therefore the reciprocal-denominator pairing and
> the first contiguous orbit supply only one equation, not a fixed-$r$
> polynomial obstruction for $I_{m,d}$, $H_m$, or an affine target
> value of $H_m$.

> **PROVED — the first Hasse lift is another moving interval.**  Over
> $\mathbf Q$, put
> 

$$
> R={(2m+d)_L\over(3m+d+1)_L}.
>
$$


> The homogeneous determinant is $R^2-1\ne0$, whereas its reduction
> modulo $p$ is zero.  More precisely,
> 

$$
> \boxed{
> {R^2-1\over p}\equiv
> 2\sum_{t=0}^m{1\over2m+d+t}\pmod p.}             \tag{1.11}
>
$$


> Thus the first digit beyond the rank drop is a moving harmonic interval,
> not a fixed-$r$ polynomial.  Formula (1.11) does not assert that this
> interval is always nonzero.  Indeed, on the admissible row
> $(p,r,s,m,d)=(23,1,3,2,5)$, the interval
> $1/9+1/10+1/11=299/990$ vanishes modulo $23$, and the exact
> determinant numerator has $23$-adic valuation two.

> **OPEN / zero booking.**  This rank-drop theorem is scoped to the two
> reciprocal moments, their first-order contiguous recurrences, and the
> denominator-complement reflection.  All-prime control of the moving first
> Hasse digit, a higher Hasse lift, a derivative jet, or a genuinely
> independent period can still add information.  No such closing invariant
> is proved here, so this item books zero rate and zero capacity reduction.

All bounded row counts in the checker are **EXACT FINITE ONLY**.

## 2. Exact incomplete-beta identity

Let



$$
R(x)=\sum_{k=0}^m\binom nkx^k(1-x)^{n-k}.
$$



A direct telescoping derivative gives



$$
R'(x)=-(n-m)\binom nm x^m(1-x)^{n-m-1}.           \tag{2.1}
$$



Because $m<n$, $R(1)=0$, whereas



$$
R(-1)=2^nK_{d,m}.                                \tag{2.2}
$$



Integrating (2.1) from $-1$ to $1$, and then putting
$x=1-2u$, gives



$$
\begin{aligned}
 2^nK_{d,m}
 &=(n-m)\binom nm\int_{-1}^1x^m(1-x)^{n-m-1}\,dx\\
 &=(2m+d)\binom nm2^{2m+d}I_{m,d}.                \tag{2.3}
 \end{aligned}
$$



Since $n=3m+d$, division by $2^{2m+d}$ proves (1.4).

On the phase, $0\leq m\leq n<p$, and
$0<2m+d<p$.  Therefore $2^m$, $2m+d$, and
$\binom nm$ are all $p$-units.  Item 253's Frobenius identity
$K_{d,m}\equiv H_m$ then proves (1.5).

## 3. Contiguous recurrence with its endpoint

Differentiate



$$
u^{2m+d+q}(1+cu)^{m+1}.                          \tag{3.1}
$$



Its value at $u=0$ is zero and its value at $u=1$ is
$(1+c)^{m+1}$.  Integrating the derivative and collecting
$M_q(c)$, $M_{q+1}(c)$ proves (1.7).

For the two reciprocal parameters this reads



$$
\begin{aligned}
 (2m+d+q)M_q(-2)-2(3m+d+q+1)M_{q+1}(-2)
   &=(-1)^{m+1},\\
 2(2m+d+q)M_q(-1/2)-(3m+d+q+1)M_{q+1}(-1/2)
   &=2^{-m}.
 \end{aligned}                                                    \tag{3.2}
$$



The first line shows explicitly why replacing the endpoint by zero would
give the wrong phase state.

Solving (1.7) for the next moment gives



$$
M_{q+1}(c)=lambda_q(c)M_q(c)+\mu_q(c),           \tag{3.3}
$$



where



$$
\lambda_q(c)=-{2m+d+q\over c(3m+d+q+1)},\qquad
 \mu_q(c)={(1+c)^{m+1}\over c(3m+d+q+1)}.         \tag{3.4}
$$



After $L=m+1$ steps,



$$
M_L(c)=A_cM_0(c)+E_c,                             \tag{3.5}
$$



with



$$
A_c=\prod_{q=0}^{L-1}\lambda_q(c)
 =\left(-{1\over c}\right)^L
 { (2m+d)_L\over(3m+d+1)_L}.                     \tag{3.6}
$$



The explicit affine constant is



$$
E_c=\sum_{t=0}^{L-1}\mu_t(c)
                  \prod_{q=t+1}^{L-1}\lambda_q(c).               \tag{3.7}
$$



It is retained in the checker; no homogeneous replacement is made.

## 4. Complement reflection and exact resonance

Expanding the left side of (1.8) and putting $k=m-j$ gives



$$
M_L(c)=\sum_{j=0}^m\binom mj
 {c^{m-j}\over4m+d+1-j}.                          \tag{4.1}
$$



But



$$
(4m+d+1-j)+(2m+d+j)=p.                           \tag{4.2}
$$



Every displayed denominator is a $p$-unit, so reciprocal pairing in
$\mathbf F_p$ proves



$$
M_L(c)\equiv-c^m\sum_{j=0}^m\binom mj
 {(c^{-1})^j\over2m+d+j}=-c^mM_0(c^{-1}),         \tag{4.3}
$$



which is (1.8).

Likewise, for $0\leq q\leq m$,



$$
(3m+d+q+1)+(3m+d-q)=p.                           \tag{4.4}
$$



The second term in (4.4) runs through the numerator factors
$(2m+d)_L$ in reverse order.  Hence



$$
(3m+d+1)_L\equiv(-1)^L(2m+d)_L\pmod p,           \tag{4.5}
$$



which proves $A_c\equiv c^{-L}$.

Apply (3.5) and (4.3) first to $c$, then to $c^{-1}$.  With
$X=M_0(c)$, $Y=M_0(c^{-1})$, one obtains



$$
\begin{pmatrix}c^{-L}&c^m\\c^{-m}&c^L\end{pmatrix}
 \binom XY=-\binom{E_c}{E_{c^{-1}}}.              \tag{4.6}
$$



The rows are proportional and consistency gives



$$
E_{c^{-1}}\equiv cE_c\pmod p.                   \tag{4.7}
$$



Thus the endpoint constants do not break the resonance.  In characteristic
zero the corresponding homogeneous determinant is



$$
\left({(2m+d)_L\over(3m+d+1)_L}\right)^2-1,      \tag{4.8}
$$



which is nonzero because every numerator factor is smaller than the
corresponding denominator factor.  Its reduction vanishes precisely because
of the phase complement (4.4).  A next-digit analysis of (4.8) is a possible
Hasse-lift target.  In fact the first digit can be localized exactly.

The complementary-factor identity is



$$
(3m+d+1)_L
 =\prod_{t=0}^m(p-(2m+d+t))
 =(-1)^L(2m+d)_L
   \prod_{t=0}^m\left(1-{p\over2m+d+t}\right).    \tag{4.9}
$$



Therefore



$$
R=(-1)^L\prod_{t=0}^m
       \left(1-{p\over2m+d+t}\right)^{-1}.         \tag{4.10}
$$



Expanding the product modulo $p^2$ proves (1.11).  All interval
denominators lie between $2m+d$ and $3m+d=n<p$, so reducing
$(R^2-1)/p$ modulo $p$ is legitimate.  The right side still has
$m+1$ moving summands.  Hence the first Hasse digit identifies the next
period but does not close it.  The exact $p=23$ witness quoted in
Section 1 also rules out treating this first digit as a universal unit.

## 5. Denominator and boundary audit

All moment denominators in the full orbit are units.  For
$0\leq q,k\leq m$,



$$
0<2m+d+q+k\leq4m+d<p,                            \tag{5.1}
$$



and the contiguous denominators obey



$$
0<3m+d+q+1\leq4m+d+1<p.                          \tag{5.2}
$$



Indeed the differences from $p$ are at least $2m+d+1$ and
$2m+d$, respectively.  The reflected denominators in (4.1) have the
same upper bound.  The constants $2$, $-2$, and $-1/2$ are units.
The beta-localization factorials have arguments at most
$n=(p-1)/2<p$.

The endpoint at $u=1$ in (3.1) is retained as $(1+c)^{m+1}$, giving
$(-1)^{m+1}$ for the target moment.  There is no missing boundary at
$u=0$, because $2m+d+q>0$.

## 6. Consequences and strict limits

Equation (1.5) is an exact new interpretation of the universal prefix, and
(1.8)--(1.10) completely analyze the most natural denominator-complement
pair.  The outcome is a no-go, not a nonvanishing theorem: assuming
$I_{m,d}=0$ merely determines the reciprocal companion from the one
independent row of (4.6).  The second row repeats the first, so it yields no
fixed-$r$ polynomial.

The same conclusion holds when the Item-251 gate prescribes an affine value
of $H_m$, rather than zero: (1.4) prescribes $X$, while (4.6) only
determines $Y$.  No compatibility condition remains.

### PROVED

* the exact incomplete-beta identity (1.4) and zero equivalence (1.5);
* the endpoint-retaining recurrence (1.7);
* reciprocal denominator reflection (1.8);
* the product collapse (1.9), singular matrix (1.10), and affine
  compatibility (4.7);
* the exact complementary product (4.9) and first-Hasse formula (1.11);
* all denominator and endpoint bounds above.

### EXACT FINITE ONLY

* all bounded modular row counts and zero witnesses in the checker.

### OPEN

* all-prime or weighted control of the moving harmonic interval (1.11),
  or a derivative-jet companion beyond it;
* any independent condition on $I_{m,d}$ or the actual Item-251 gate;
* any weighted zero theorem, rate, capacity reduction, or conclusion about
  $e+\pi$.

Accordingly,



$$
\boxed{\text{new unconditional linear-log rate}=0,\qquad
        \text{capacity reduction}=0.}                            \tag{6.1}
$$


