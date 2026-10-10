> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 389 — analytic-cost lower bounds for the mixed kernel and the continued-fraction threshold

Date: 2026-09-01

## 1. Outcome first

Put



$$
\alpha=e+\pi.
$$



Item 387 proves that every integer polynomial in Yu's mixed identity has
the unique form



$$
P=P_{A,C}+(1+D)\bigl(x(x-1)R\bigr),
 \qquad P_{A,C}=A+(A-C)x,                              \tag{1.1}
$$



where $A,C\in\mathbb Z$, $R\in\mathbb Z[x]$, and



$$
\int_0^1\left(e^xP(x)+{4A\over1+x^2}\right)dx
 =A\alpha-C.                                           \tag{1.2}
$$



This item settles the coefficient/analytic-cost question that remains
after the quotient theorem.  Write



$$
F_{A,C,R}(x)=e^xP(x)+{4A\over1+x^2},                  \tag{1.3}
$$



and, for $P(x)=\sum_{k=0}^dp_kx^k$, put



$$
B_0(P)=\sum_{k=0}^d|p_k|,
 \qquad B_1(P)=\sum_{k=0}^dk|p_k|.                    \tag{1.4}
$$



The main conclusions are all-degree theorems.

> **Uniform-cost theorem.**  One has the exact endpoint identity
> 

$$
> \boxed{F_{A,C,R}(0)=5A-R(0)\in\mathbb Z.}            \tag{1.5}
>
$$


> Consequently
> 

$$
> \boxed{\|F_{A,C,R}\|_\infty\geq|5A-R(0)|.}          \tag{1.6}
>
$$


> If $\|F\|_\infty<1$, then necessarily
> 

$$
> \boxed{R(0)=5A,\qquad p_0=-4A,}                     \tag{1.7}
>
$$


> and therefore
> 

$$
> \boxed{\max_k|[x^k]R|\geq5|A|,qquad
>        B_0(P)\geq4|A|.}                              \tag{1.8}
>
$$



> **$L^1$-cost dichotomy.**  Define
> 

$$
> \Lambda(P,A)=3\bigl(B_0(P)+B_1(P)+|A|\bigr).        \tag{1.9}
>
$$


> Then either $R(0)=5A$, or
> 

$$
> \boxed{\|F_{A,C,R}\|_1\geq{1\over2\Lambda(P,A)}.} \tag{1.10}
>
$$


> In particular, crossing the inverse analytic-cost threshold
> $\|F\|_1<1/(2\Lambda)$ forces the exact coefficient encoding (1.7)
> and the two linear lower bounds (1.8).

> **Global coefficient lower bound.**  For every $P,A,C,R$,
> 

$$
> \boxed{
> B_0(P)\geq{3|A|-\|F_{A,C,R}\|_1\over2}.}           \tag{1.11}
>
$$



> **Continued-fraction threshold.**  Suppose
> 

$$
> B_0(P)>0,\qquad 0<|A\alpha-C|\leq\|F\|_1
> <\min\left(1,{1\over2B_0(P)}\right).                \tag{1.12}
>
$$


> Then $A\ne0$, $|A|\leq B_0(P)$, and
> 

$$
> \boxed{
> \left|\alpha-{C\over A}\right|
> <{1\over2|A|^2}.}                                    \tag{1.13}
>
$$


> After reducing $C/A$, it is an ordinary continued-fraction
> convergent of $\alpha$ by Legendre's theorem (using the finite simple
> continued fraction if $\alpha$ were rational).  Moreover the degree-one
> representative with the same linear form has comparable coefficient
> cost:
> 

$$
> \boxed{B_0(P_{A,C})<9B_0(P)+1.}                       \tag{1.14}
>
$$



Thus a mixed-polynomial construction that becomes small beyond inverse
coefficient cost does not obtain a cheaper approximation lattice.  It has
already encoded an ordinary continued-fraction-quality pair $(A,C)$,
with denominator no larger than the polynomial coefficient budget.  At
the stronger uniform or inverse-Lipschitz threshold, the kernel polynomial
itself contains the denominator explicitly in its constant coefficient
$R(0)=5A$.

This is the requested structured-$R$ cost theorem.  It does not prove
that a separately specified Rodrigues, Padé, or sign-constrained family
cannot produce the required convergents non-circularly.  It proves that
analytic reshaping by the mixed kernel supplies no denominator-clearing
advantage by itself.

No sequence satisfying (1.12) is constructed here.  No nonzero linear
form is asserted without the explicit hypothesis in (1.12).  Hence no
irrationality conclusion is claimed.

---

## 2. Exact endpoint encoding

Let



$$
S(x)=x(x-1)R(x).                                       \tag{2.1}
$$



Then $S(0)=0$ and $S'(0)=-R(0)$.  Since the kernel term in
(1.1) is $(1+D)S=S+S'$,



$$
P(0)=P_{A,C}(0)+S(0)+S'(0)=A-R(0).                    \tag{2.2}
$$



At $x=0$, the exponential and rational weights both equal one in the
required normalization, so



$$
F(0)=P(0)+4A=5A-R(0).                                 \tag{2.3}
$$



Equations (1.5)--(1.6) follow.  Because (2.3) is an integer, uniform norm
strictly below one forces it to vanish.  Substitution into (2.2) gives



$$
R(0)=5A,qquad P(0)=-4A,                               \tag{2.4}
$$



which proves (1.7)--(1.8).

The conclusion is exact and independent of $\deg R$.  In particular,
raising the degree cannot distribute the endpoint cost away from all
coefficients: the constant term of $R$ alone has size $5|A|$.

---

## 3. The inverse analytic-cost barrier for $L^1$ smallness

On $[0,1]$,



$$
|P(x)|\leq B_0(P),qquad |P'(x)|\leq B_1(P),qquad e^x<3. \tag{3.1}
$$



Also



$$
\max_{0\leq x\leq1}{8x\over(1+x^2)^2}
 ={3\sqrt3\over2}<3.                                  \tag{3.2}
$$



The maximum follows by differentiating
$x(1+x^2)^{-2}$; its only interior critical point is
$x=1/\sqrt3$.  Hence



$$
|F'(x)|
 \leq3\bigl(B_0(P)+B_1(P)+|A|\bigr)=\Lambda(P,A).     \tag{3.3}
$$



Put $K=F(0)=5A-R(0)\in\mathbb Z$.  If $K\ne0$, then
$|K|\geq1$.  In that case $\Lambda\geq3$, and for
$0\leq x\leq1/\Lambda$,



$$
|F(x)|\geq1-\Lambda x.                                \tag{3.4}
$$



Integration gives



$$
\|F\|_1\geq
 \int_0^{1/\Lambda}(1-\Lambda x)dx
 ={1\over2\Lambda}.                                   \tag{3.5}
$$



This proves the dichotomy (1.10).  It can be restated for the usual
degree-height budget.  If



$$
H(P)=\max_k|p_k|,qquad d=\deg P,                      \tag{3.6}
$$



then



$$
B_0(P)+B_1(P)\leq(d+1)^2H(P).                        \tag{3.7}
$$



Therefore the sufficient all-degree condition



$$
\|F\|_1<
 {1\over6\bigl((d+1)^2H(P)+|A|\bigr)}                 \tag{3.8}
$$



already forces $R(0)=5A$.  Equation (3.8) is not claimed optimal; its
role is to exhibit an explicit denominator/analytic-cost threshold with
no hidden degree dependence.

---

## 4. Global coefficient cost and ordinary approximation quality

The rational part of the integrand has exact $L^1$ norm



$$
\left\|{4A\over1+x^2}\right\|_1=\pi|A|.              \tag{4.1}
$$



By the triangle inequality and $|P(x)|\leq B_0(P)$,



$$
\pi|A|
 \leq\|F\|_1+\int_0^1e^x|P(x)|dx
 \leq\|F\|_1+(e-1)B_0(P).                             \tag{4.2}
$$



Weakening the elementary bounds $\pi>3$ and $e<3$ gives the globally
valid inequality



$$
3|A|\leq\|F\|_1+2B_0(P),                             \tag{4.3}
$$



which is (1.11).  It is strict unless the entire tuple, and hence $F$,
is zero; the weak form is the correct all-tuple statement.

Now impose the explicit nonzero/smallness hypotheses (1.12).  If
$A=0$, then $A\alpha-C=-C$ is a nonzero integer and has absolute
value at least one, contradicting (1.12).  Thus $A\ne0$.  Put
$q=|A|$.  Since $\|F\|_1<1$, (1.11) gives



$$
B_0(P)\geq{3q-\|F\|_1\over2}
 >{3q-1\over2}\geq q.                                 \tag{4.4}
$$



Consequently



$$
\left|\alpha-{C\over A}\right|
 ={|A\alpha-C|\over q}
 \leq{\|F\|_1\over q}
 <{1\over2B_0(P)q}
 \leq{1\over2q^2}.                                    \tag{4.5}
$$



This proves (1.13).  If $C/A=c/q_0$ in lowest terms, then
$q_0\leq q$, so (4.5) is at least as strong as
$|\alpha-c/q_0|<1/(2q_0^2)$.  Legendre's theorem gives the stated
continued-fraction conclusion; its standard rational-endpoint version is
used if $\alpha$ has a finite simple continued fraction.

There is also a literal constant-factor replacement by the Item 387
degree-one section.  The elementary upper bounds $e<3$, $\pi<4$ give
$\alpha<7$.  Since $|A\alpha-C|<1$,



$$
|C|<7q+1.                                              \tag{4.6}
$$



Therefore



$$
\begin{aligned}
 B_0(P_{A,C})
 &=|A|+|A-C|\\
 &\leq2q+|C|<9q+1\leq9B_0(P)+1,
 \end{aligned}                                         \tag{4.7}
$$



which proves (1.14).  The high-degree polynomial can thus be replaced by
a degree-one polynomial of at most constant-factor coefficient cost while
preserving exactly the same integer linear form.

The same conclusion follows from a uniform estimate
$\|F\|_\infty<\min(1,1/(2B_0(P)))$, because
$\|F\|_1\leq\|F\|_\infty$.

---

## 5. Consequences for structured kernel families

Consider any explicitly generated integer family



$$
(A_n,C_n,R_n),qquad
 P_n=P_{A_n,C_n}+(1+D)(x(x-1)R_n).                       \tag{5.1}
$$



The theorems give three rigorous alternatives.

1. If $\|F_n\|_\infty<1$, then the family must satisfy the exact
   coefficient identity $R_n(0)=5A_n$.  A proposed family failing this
   identity cannot even enter the uniform-small regime.
2. If $\Lambda(P_n,A_n)\|F_n\|_1<1/2$, the same exact identity is
   forced.  Thus any successful decay exponent must pay at least the
   explicit constant-coefficient cost $5|A_n|$.
3. If the nonzero form and inverse coefficient threshold (1.12) hold,
   $(A_n,C_n)$ is already a continued-fraction-quality approximation at
   denominator $|A_n|\leq B_0(P_n)$, and its degree-one representative
   has coefficient cost below $9B_0(P_n)+1$.

This closes the following mechanism:



$$
\boxed{
 \text{use only high-degree exact-derivative reshaping to obtain a}\
 \text{small mixed integrand at coefficient cost sublinear in }|A|.} \tag{5.2}
$$



It does not close a structured family that independently proves all of:

1. integrality of $A_n,C_n,R_n$;
2. $0<|A_n\alpha-C_n|$;
3. the required analytic decay;
4. a coefficient-growth estimate passing the relevant threshold; and
5. a construction not chosen from prior continued fractions of $\alpha$.

No such family is produced here.

---

## 6. Deterministic certificate and strict labels

The standard-library certificate pins Item 387 and verifies the exact
decomposition, endpoint map, and identity (1.5) on six predeclared
polynomials through degree six.  It records $B_0,B_1,\Lambda$, checks
the coefficient consequences when $R(0)=5A$, and verifies exact rational
bounds $e<3$, $\pi>3$, and $(3\sqrt3/2)<3$.  These are controls of
the formulas, not a search for small forms.

### PROVED

- the exact endpoint identity and uniform-cost theorem;
- the all-degree inverse analytic-cost dichotomy;
- the explicit degree-height threshold (3.8);
- the global coefficient lower bound (1.11);
- the conditional continued-fraction theorem with every nonzero and
  smallness hypothesis stated explicitly;
- the constant-factor degree-one replacement theorem (1.14);
- the scoped high-degree reshaping/sublinear-denominator-cost no-go.

### DECLARED EXACT CONTROLS ONLY

- six fixed polynomial tuples and exact elementary constant bounds;
- no optimization, unstructured search, finite extrapolation, or claimed
  small nonzero linear form.

### OPEN

- a non-circular structured family passing all five conditions in Section
  5;
- any nonzero sequence satisfying (1.12);
- irrationality of $e+\pi$.

## 7. Ledger consequence

This is an analytic/coefficient-cost no-go for the post-Item-387 mixed
kernel.  It adds no Route-1 factor and changes no existing capacity number.
It also does not establish Route-2 success: the theorem classifies what a
successful structured family would have to encode.



$$
\begin{array}{c|c}
\text{quantity}&\text{Item 389 value}\\ \hline
\text{new nonzero linear-form sequence}&0\\
\text{new irrationality criterion beyond ordinary approximation}&0\\
\text{structured-}R\text{ cost theorem}&\text{PROVED}\\
\text{new Route-1 booking or capacity reduction}&0\\
\text{conclusion about }e+\pi&\text{OPEN}
\end{array}                                               \tag{7.1}
$$


