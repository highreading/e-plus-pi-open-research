> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The central Bessel lift: Charlier form and exact Wilson--Frobenius cancellations

Checked: 2026-08-27 UTC.

## 1. Scope and verdict

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\ge2),
\tag{1}
$$



and, for an odd prime $p$, put $m=(p-1)/2$.  Define



$$
A_m=\sum_{j=0}^m j!\binom mj^2,
 \qquad
 C_m=\sum_{j=0}^m j!\binom mj^2(H_m-H_{m-j}).
\tag{2}
$$



The preceding Laguerre reduction proved



$$
q_m\equiv(-1)^m(A_m-pC_m)\pmod {p^2}.
\tag{3}
$$



This note gives three exact refinements.

1.  $A_m$, $C_m$, and $q_m$ are respectively a value, an ordinary
    parameter derivative, and a value at a second integer lift of one monic
    Charlier polynomial.  Thus the exceptional condition is literally a
    Hensel/Wieferich condition in the Charlier parameter.
2.  There is an exact formula for $A_m/p-C_m$, conditional on 

$$
p\mid
    A_m
$$

, involving coefficients of degree strictly below $m$; see
    (40).  It is a genuine formula, but it does not have a known
    nonvanishing sign or residue mechanism.
3.  The natural Wilson-quotient term and the first nonzero Frobenius term
    both cancel at precisely the order at which one would need them.  The
    cancellations are formal identities, not observations from a scan.

The result is therefore a rigorous reduction and a rigorous no-go result for
two tempting approaches.  It is **not** an all-prime proof that
$p^2\nmid q_m$.  The residue



$$
\frac{A_m}{p}-C_m\pmod p
\tag{4}
$$



remains uncontrolled in general.

All congruences between rational numbers below are interpreted in
$\mathbb Z_{(p)}$; every displayed denominator is prime to $p$.

## 2. One Charlier polynomial contains all three quantities

For $n\ge0$, define the monic integer polynomial



$$
F_n(a)=\sum_{j=0}^n\binom nj(a)_{\underline j},
 \qquad
 (a)_{\underline j}=a(a-1)\cdots(a-j+1).
\tag{5}
$$



Its exponential generating function in $n$ is



$$
\boxed{
 \sum_{n\ge0}F_n(a)\frac{z^n}{n!}=e^z(1+z)^a.}
\tag{6}
$$



Indeed, after writing $n=j+r$, the coefficient of
$(a)_{\underline j}$ on the left is $z^je^z/j!$.  Multiplying the
derivative of (6) by $1+z$, and separately replacing $a$ by $a+1$,
gives the exact recurrence and forward-difference identities



$$
\boxed{F_{n+1}(a)=(a+1-n)F_n(a)+nF_{n-1}(a),}
\tag{7}
$$





$$
\boxed{\Delta_aF_n(a):=F_n(a+1)-F_n(a)=nF_{n-1}(a).}
\tag{8}
$$



At the diagonal,



$$
F_m(m)=\sum_{j=0}^m\binom mj(m)_{\underline j}=A_m.
\tag{9}
$$



Termwise differentiation of (5), at $a=m$, gives



$$
F'_m(m)=\sum_{j=0}^m j!\binom mj^2(H_m-H_{m-j})=C_m.
\tag{10}
$$



Finally, because $m-p=-m-1$,



$$
\begin{aligned}
 F_m(-m-1)
 &=\sum_{j=0}^m(-1)^j\frac{(m+j)!}{j!(m-j)!}\\
 &=(-1)^m\sum_{k=0}^m(-1)^k
       \frac{(2m-k)!}{k!(m-k)!}
 =(-1)^m q_m.
\end{aligned}
\tag{11}
$$



The second equality uses $k=m-j$, and the last sum is the standard exact
Bessel-polynomial formula for the recurrence (1).  Equations (9)--(11) give



$$
\boxed{
 F_m(m)=A_m,\quad F'_m(m)=C_m,\quad
 F_m(m-p)=(-1)^m q_m.}
\tag{12}
$$



Since $F_m\in\mathbb Z[a]$, Taylor expansion by the integer displacement
$-p$ immediately recovers



$$
F_m(m-p)\equiv F_m(m)-pF'_m(m)\pmod {p^2},
\tag{13}
$$



which is (3).

Conditional on $p\mid A_m$, the reduction $a=m$ is a root of
$F_m(a)$ modulo $p$.  If also $C_m\not\equiv0\pmod p$, its Hensel
lift has first digit



$$
a=m+pt,\qquad
 t\equiv-\frac{A_m}{p}C_m^{-1}\pmod p.
\tag{14}
$$



The distinguished integer representative $m-p$ corresponds to $t=-1$.
Whether or not $C_m$ vanishes, (12)--(13) prove the exact equivalence



$$
\boxed{
 p^2\mid q_m
 \quad\Longleftrightarrow\quad
 \frac{A_m}{p}\equiv C_m\pmod p,
 \qquad(p\mid A_m).}
\tag{15}
$$



Thus the missing theorem is an exclusion of one specific Charlier Hensel
digit, not polynomial-root simplicity in the argument of a Padé
denominator.

### Partial injections and a finite nilpotent algebra

For nonnegative integers $a$, the summand in (5) chooses $j$ elements
from an $n$-set, $j$ elements from an $a$-set, and a bijection between
them.  Hence $F_n(a)$ counts partial injections, and $A_m=F_m(m)$ counts
partial permutations of an $m$-set.

There is also an exact finite-algebra model.  Put



$$
R_m=\mathbb Z[\epsilon_1,\ldots,\epsilon_m]/(\epsilon_1^2,\ldots,
 \epsilon_m^2),\qquad X=\epsilon_1+\cdots+\epsilon_m,
\tag{16}
$$



and let $\lambda$ send every squarefree monomial to $1$.  Since



$$
\lambda(X^j)=j!\binom mj,
$$



the generalized binomial expansion, which terminates because $X^{m+1}=0$,
gives



$$
F_m(a)=\lambda((1+X)^a).
\tag{17}
$$



Consequently,



$$
A_m=\lambda((1+X)^m),\qquad
 C_m=\lambda((1+X)^m\log(1+X)).
\tag{18}
$$



In $R_m\otimes\mathbb Z_{(p)}$,



$$
(1+X)^{-p}=\exp(-p\log(1+X))
 \equiv1-p\log(1+X)\pmod {p^2},
\tag{19}
$$



so (13) is also the first-order logarithm of a finite nilpotent algebra.
This interpretation explains integrality and the partial-permutation
structure; it does not supply the missing nonvanishing in (15).

## 3. The exact $p$-step identity is Taylor expansion in disguise

Let $E f(a)=f(a+1)$, so $E=1+\Delta$.  Since $F_m$ has degree
$m$, the following Newton series terminates exactly:



$$
\begin{aligned}
 F_m(a-p)
 &=(1+\Delta)^{-p}F_m(a)\\
 &=\sum_{r=0}^m(-1)^r\binom{p+r-1}{r}\Delta^rF_m(a).
\end{aligned}
\tag{20}
$$



Iterating (8) gives



$$
\Delta^rF_m(a)=(m)_{\underline r}F_{m-r}(a),
\tag{21}
$$



and hence the requested exact relation between the two integer lifts is



$$
\boxed{
 F_m(m-p)=\sum_{r=0}^m(-1)^r\binom{p+r-1}{r}
 (m)_{\underline r}F_{m-r}(m).}
\tag{22}
$$



For $1\le r\le m<p$,



$$
(-1)^r\binom{p+r-1}{r}
 =(-1)^r\frac p r\prod_{s=1}^{r-1}\left(1+\frac p s\right)
 \equiv(-1)^r\left(\frac p r+\frac{p^2H_{r-1}}r\right)
 \pmod {p^3}.
\tag{23}
$$



On the other hand, the formal operator identities



$$
\log(1+\Delta)
 =\sum_{r\ge1}\frac{(-1)^{r-1}}r\Delta^r,
\tag{24}
$$





$$
\frac12\log^2(1+\Delta)
 =\sum_{r\ge2}\frac{(-1)^rH_{r-1}}r\Delta^r
\tag{25}
$$



terminate on $F_m$, and $\log E=d/da$ on polynomials.  Substitution of
(23)--(25) into (20) therefore gives exactly



$$
F_m(a-p)\equiv F_m(a)-pF'_m(a)+\frac{p^2}{2}F''_m(a)
 \pmod {p^3}.
\tag{26}
$$



Thus the harmonic term in the $p$-step Newton formula is not a second
congruence: it is exactly the second ordinary derivative in Taylor's
formula.  A Faulhaber or Bernoulli-number expansion of the same finite
$p$-step sum is merely another coordinate expression for the translation
operator $E^{-p}$; its Bernoulli terms must recombine into (26).  This does
not rule out using an additional, genuinely arithmetic Bernoulli identity,
but the translation identity alone supplies no independent restriction on
(4).

## 4. Wilson quotient: an exact coefficientwise cancellation

At $2m=p-1$, write



$$
\mathcal Q_m(x)=\sum_{k=0}^m(-1)^k
 \frac{(p-1-k)!}{k!(m-k)!}x^k,
 \qquad \mathcal Q_m(1)=q_m,
\tag{27}
$$



and define



$$
R_m(x)=\sum_{k=0}^m\frac{x^k}{k!^2(m-k)!},\qquad
 T_m(x)=\sum_{k=0}^m\frac{H_kx^k}{k!^2(m-k)!}.
\tag{28}
$$



Let $W_p=((p-1)!+1)/p$ be the Wilson quotient.  Factoring the last
$k$ terms of $(p-1)!$ gives, coefficientwise,



$$
\begin{aligned}
 (-1)^k(p-1-k)!
 &=\frac{(p-1)!}{k!}
   \prod_{j=1}^k\left(1-\frac pj\right)^{-1}\\
 &\equiv\frac{-1+p(W_p-H_k)}{k!}\pmod {p^2}.
\end{aligned}
\tag{29}
$$



Therefore



$$
\boxed{
 \mathcal Q_m(x)\equiv
 -R_m(x)+p\bigl(W_pR_m(x)-T_m(x)\bigr)\pmod {p^2}.}
\tag{30}
$$



At $x=1$, direct reindexing gives



$$
R_m(1)=\frac{A_m}{(m!)^2},\qquad
 (m!)^2T_m(1)=H_mA_m-C_m.
\tag{31}
$$



If $p\mid A_m$, the term $pW_pR_m(1)$ is already zero modulo
$p^2$.  Dividing (30) by $p$ then gives



$$
\frac{q_m}{p}\equiv-\frac{R_m(1)}p-T_m(1)\pmod p.
\tag{32}
$$



Wilson's theorem also gives



$$
(m!)^2\equiv(-1)^{m+1}\pmod p,
\tag{33}
$$



because $(p-1)!\equiv(-1)^m(m!)^2$.  Using (31) in (32) now yields



$$
\frac{q_m}{p}\equiv(-1)^m\left(\frac{A_m}{p}-C_m\right)\pmod p,
\tag{34}
$$



exactly (3) divided by $p$.  Thus the Wilson quotient itself disappears
under the central-root hypothesis.  It cannot be the universal nonzero term
needed to settle (15).

## 5. An exact lower-degree quotient formula

Put



$$
g_n=\frac{A_n}{n!}=L_n(-1),\qquad
 G(z)=\sum_{n\ge0}g_nz^n.
\tag{35}
$$



The Laguerre generating function gives



$$
G(z)=\frac1{1-z}\exp\left(\frac z{1-z}\right),
\qquad
 \ell(z):=\log G(z)
 =\sum_{n\ge1}\left(1+\frac1n\right)z^n.
\tag{36}
$$



Let $u(z)=G(z)-1$ and



$$
S_{m,r}=[z^m]u(z)^r.
\tag{37}
$$



For $r\ge2$, $S_{m,r}$ involves only
$g_1,\ldots,g_{m-r+1}$, hence only degrees strictly below $m$.
Extracting $z^m$ from
$\ell=\log(1+u)$ gives the exact rational identity



$$
g_m+\sum_{r=2}^m\frac{(-1)^{r-1}}rS_{m,r}
 =1+\frac1m.
\tag{38}
$$



Also, differentiating the Laguerre parameter generating function gives



$$
\frac{C_m}{m!}=\sum_{s=1}^m\frac{g_{m-s}}s.
\tag{39}
$$



Consequently, if $p\mid A_m$, then the parenthesized numerator below is
divisible by $p$ in $\mathbb Z_{(p)}$, and



$$
\boxed{
 \frac{A_m/p-C_m}{m!}
 =\frac1p\left(
 1+\frac1m-
 \sum_{r=2}^m\frac{(-1)^{r-1}}rS_{m,r}
 \right)
 -\sum_{s=1}^m\frac{g_{m-s}}s.}
\tag{40}
$$



This is an exact formula over $\mathbb Q$, and therefore an exact
modulo-$p$ formula after reduction.  Unlike a direct occurrence of
$A_m/p$, its right side is built entirely from lower-degree Laguerre
coefficients.  Nevertheless, the first parenthesis is itself a cancellation
to order $p$; no sign, norm, or nonzero residue is apparent.  The next
subsection shows why the most natural Frobenius attempt does not resolve it.

## 6. The universal Frobenius coefficient is nonzero, but the next order is tautological

Since $0<m<p$, the coefficient of $z^m$ in $G(z^p)$ is zero.  From
$G^p=\exp(p\ell)$,



$$
\begin{aligned}
 D_m&:=[z^m]\frac{G(z)^p-G(z^p)}p\\
 &\equiv [z^m]\ell(z)+\frac p2[z^m]\ell(z)^2\pmod {p^2}.
\end{aligned}
\tag{41}
$$



This truncation is $p$-integral: for $p\ge5$, every exponential
denominator that can contribute to degree $m<p$ is a $p$-unit.  For
$p=3$, one has $m=1$, so every term of degree two or higher in $\ell$
vanishes after extracting $z^m$.

In particular,



$$
D_m\equiv1+\frac1m\equiv-1\pmod p,
\tag{42}
$$



because $m=(p-1)/2$.  This is a universal nonzero first Frobenius
coefficient.

It is tempting to hope that (42) controls $g_m/p$ when $g_m\equiv0$.
It does not.  Expanding $G^p=(1+u)^p$ gives



$$
D_m=g_m+\sum_{r=2}^m\frac1p\binom prS_{m,r}.
\tag{43}
$$



For $2\le r\le m$,



$$
\frac1p\binom pr
 \equiv\frac{(-1)^{r-1}}r
 \left(1-pH_{r-1}\right)\pmod {p^2}.
\tag{44}
$$



The order-one part of (43) is exactly (38).  At the next order one obtains
the apparent new term



$$
-\sum_{r=2}^m\frac{(-1)^{r-1}H_{r-1}}rS_{m,r}.
\tag{45}
$$



But differentiating the formal identity



$$
G(z)^t=(1+u(z))^t
 =\sum_{r\ge0}\binom tr u(z)^r
\tag{46}
$$



twice at $t=0$ gives the exact identity



$$
\boxed{
 \frac12[z^m]\ell(z)^2
 =\sum_{r=2}^m\frac{(-1)^rH_{r-1}}rS_{m,r}.}
\tag{47}
$$



The expression in (47) is precisely (45).  Therefore the second-order
binomial expansion of (43) agrees identically with the second-order
exponential expansion (41); after (38) is canceled, the proposed equation
for $g_m/p$ reduces to $0=0$.  The nonzero $-1$ in (42) occurs one
order too early and supplies no nonvanishing theorem for (40).

## 7. Ordinary derivative simplicity is a different question, and can fail

The exact Padé Wronskian for the Bessel denominator concerns an argument
derivative $\mathcal Q_m'(x)$ at the argument root $x=1$.  Here the
relevant derivative is the Charlier parameter derivative
$F'_m(a)$ at $a=m$.  These are derivatives of different polynomials in
different variables.  Simplicity of the Pad\'e argument root therefore does
not decide (15).

Nor can one invoke global separability of $F_m(a)$ modulo every prime.  A
reproducible exact modular calculation gives



$$
F_{288}(186)\equiv F'_{288}(186)\equiv0\pmod {577}.
\tag{48}
$$



Thus $F_{288}$ has a repeated noncentral root modulo the prime $577$.
At the central parameter in the same example,



$$
F_{288}(288)\equiv8,\qquad F'_{288}(288)\equiv211\pmod {577},
\tag{49}
$$



so (48) is not a central counterexample.  It rigorously rules out only the
blanket claim that all roots of all these Charlier polynomials are simple.
It does not rule out a more specialized theorem conditional on
$F_m(m)=0$ and $p=2m+1$.

## 8. Certificate and theorem/evidence boundary

The companion program

`scripts/bessel_central_charlier_frobenius_barrier_certificate.py`

checks, using exact integers and rational numbers:

* (7)--(13), (20)--(26), and the nilpotent coefficient formula through a
  requested exact degree;
* the logarithm and second-derivative identities (38) and (47);
* the coefficientwise Wilson congruence (30) for every odd prime through a
  requested finite cutoff;
* formula (40) at every central root found within that cutoff; and
* the explicit repeated-root calculation (48)--(49).

With the frozen default cutoff $p\le1000$, the only central root is
$p=79,m=39$, and the recorded residues are



$$
\frac{A_m}{p}\equiv45,\quad C_m\equiv57,\quad
 \frac{A_m}{p}-C_m\equiv67,\quad \frac{q_m}{p}\equiv12\pmod {79}.
\tag{50}
$$



The identities proved in Sections 2--6 hold for all indicated degrees and
primes.  The cutoff statement and (50) are finite evidence only.  They are
not used to infer all-prime nonvanishing.

## 9. Final assessment

The central obstruction has an exact and economical formulation:



$$
\text{Does the root }a=m\pmod p\text{ of }F_m(a)
 \text{ lift to the integer representative }m-p\pmod {p^2}?
$$



Formula (40) removes the top-degree coefficient from the unknown quotient,
but leaves a lower-degree cancellation with no known nonzero mechanism.
Wilson's quotient is annihilated by the root hypothesis, the $p$-step
Newton/Faulhaber correction is ordinary Taylor expansion, and the first two
Frobenius orders are the first two derivatives of one formal identity.
Accordingly, none of these reductions proves $p^2\nmid q_m$ for every
prime.  A successful continuation needs genuinely new arithmetic input on
the Charlier Hensel digit (14), rather than another rearrangement of the same
translation or Frobenius identities.
