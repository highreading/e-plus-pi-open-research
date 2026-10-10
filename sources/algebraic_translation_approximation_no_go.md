> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Algebraic-translation approximants to $\pi$: exact heights and a quantitative no-go

**Date:** 2026-08-26  
**Status:** rigorous conditional analysis.  Throughout this note we assume, only for the
purpose of testing the idea, that


$$
s=e+\pi\in\overline{\mathbf Q},\qquad [\mathbf Q(s):\mathbf Q]=d.
$$


Nothing below proves that assumption or its negation.  The conclusion is that the
Taylor approximants considered here, and in fact every construction obtained by
subtracting a rational approximant to $e$ from $s$, are quantitatively compatible
with the established approximation measures for $\pi$.

**Asymptotic convention.** An unlabeled $O(\cdot)$, $\ll$, or $\gg$ has an
absolute implied constant.  A subscript, as in $O_s(1)$ or
$O_{s,d}(1)$, lists all fixed data on which the constant is allowed to depend;
no such constant depends on $n$ or on a reduced numerator or denominator.

## 1. The Taylor approximants and their exact reduced denominators

Put


$$
E_n=\sum_{k=0}^n\frac1{k!}=\frac{A_n}{n!},\qquad
 A_n=\sum_{k=0}^n\frac{n!}{k!}\in\mathbf Z.
$$


Let


$$
g_n=\gcd(A_n,n!),\qquad p_n=A_n/g_n,\qquad q_n=n!/g_n,
$$


so that $E_n=p_n/q_n$ is in lowest terms.  Thus $q_n$, not the
unreduced denominator $n!$, is the quantity relevant to height.  Two useful exact
relations are


$$
A_n=nA_{n-1}+1,
 \qquad \gcd(A_n,n)=1.
$$


Also $A_n=\lfloor en!\rfloor$ for $n\geq1$.

For


$$
R_n=e-E_n=\sum_{k=n+1}^{\infty}\frac1{k!}
$$


one has the elementary sharp-enough bounds


$$
\frac1{(n+1)!}<R_n<
 \frac{n+2}{n+1}\frac1{(n+1)!}.                                      \tag{1}
$$


Indeed, after the first term, bound each successive denominator factor from below
by $n+2$ and sum a geometric series.  In particular,


$$
-\log R_n=\log((n+1)!)+O(1/n).                                      \tag{2}
$$



Define the conditional algebraic approximant


$$
\alpha_n=s-E_n=s-\frac{p_n}{q_n}.
$$


Then


$$
\alpha_n-\pi=e-E_n=R_n,
       \qquad |\pi-\alpha_n|=R_n,                                   \tag{3}
$$


and rational translation does not change the generated number field:


$$
\mathbf Q(\alpha_n)=\mathbf Q(s),\qquad \deg\alpha_n=d.       \tag{4}
$$



## 2. Exact Weil-height and naive-height scales

Let $h$ denote the absolute logarithmic Weil height.  The standard height
inequality


$$
h(x+y)\leq h(x)+h(y)+\log2
$$


applied once to $\alpha_n=s-E_n$ and once to $E_n=s-\alpha_n$
gives


$$
|h(\alpha_n)-h(E_n)|\leq h(s)+\log2.                           \tag{5}
$$


Since $2\leq E_n<3$ for $n\geq1$, and $p_n/q_n$ is reduced,


$$
h(E_n)=\log\max(p_n,q_n)=\log p_n=\log q_n+O(1).
$$


Consequently the exact height statement is


$$
\boxed{\ h(\alpha_n)=\log q_n+O_s(1).\ }               \tag{6}
$$



Let $P_n\in\mathbf Z[X]$ be the primitive irreducible polynomial of
$\alpha_n$, let


$$
H(P_n)=\max_j|[X^j]P_n|,
 \qquad L(P_n)=\sum_j|[X^j]P_n|,
$$


and write $M(P_n)$ for its Mahler measure.  Since


$$
\log M(P_n)=d h(\alpha_n),
$$


while


$$
M(P_n)\leq\sqrt{d+1}\,H(P_n),
 \qquad H(P_n)\leq 2^d M(P_n),
 \qquad H(P_n)\leq L(P_n)\leq(d+1)H(P_n),
$$


we obtain


$$
\boxed{
 \begin{aligned}
   \log H(P_n)&=d\log q_n+O_{s,d}(1),\\
   \log L(P_n)&=d\log q_n+O_{s,d}(1).
 \end{aligned}}                                                     \tag{7}
$$


Equivalently, $H(P_n)\asymp_{s,d}q_n^d$ and
$L(P_n)\asymp_{s,d}q_n^d$.

There is also a concrete polynomial realizing this scale.  If


$$
F_s(X)=a_dX^d+\cdots+a_0\in\mathbf Z[X]
$$


is the primitive minimal polynomial of $s$, then


$$
G_n(X)=q_n^dF_s\left(X+\frac{p_n}{q_n}\right)
       =\sum_{j=0}^d a_jq_n^{d-j}(q_nX+p_n)^j\in\mathbf Z[X]          \tag{8}
$$


has $\alpha_n$ as a root.  It is irreducible over $\mathbf Q$ up to a
nonzero rational scalar.  Its leading coefficient is $a_dq_n^d$, and, because
$p_n/q_n$ stays in a compact interval,


$$
H(G_n)\asymp_s q_n^d.                                \tag{9}
$$


Equations (7) and (9) also show that the content of $G_n$ is bounded in
terms of $s$; its primitive part is $P_n$, up to sign.

## 3. How much cancellation can occur in $n!$?

The exact answer is $q_n=n!/\gcd(A_n,n!)$.  A full asymptotic formula for this
gcd is not needed, and no such formula is assumed here.  What is needed is a
rigorous lower bound for $q_n$.

### Lemma (a uniform rational-approximation bound for $e$)

There is an absolute constant $c>0$ such that every reduced $p/q$, $q\geq1$,
satisfies


$$
\left|e-\frac pq\right|
           \geq \frac{c}{q^2\log(2q)}.                              \tag{10}
$$



**Proof.** Euler's exact simple continued fraction is


$$
e=[2;1,2,1,1,4,1,1,6,1,\ldots],
 \quad a_{3m-2}=1, a_{3m-1}=2m, a_{3m}=1.
$$


If $|e-p/q|\geq1/(2q^2)$, (10) follows after reducing $c$ if necessary.
Otherwise Legendre's continued-fraction criterion says that $p/q$ is a
convergent, say $P_k/Q_k$.  The standard convergent inequalities give


$$
\left|e-\frac{P_k}{Q_k}\right|
 >\frac1{Q_k(Q_{k+1}+Q_k)}
 >\frac1{(a_{k+1}+2)Q_k^2}.                                        \tag{11}
$$


Now $a_{k+1}=O(k)$, while $Q_k\geq F_{k+1}$, so
$k=O(\log(2Q_k))$.  Hence $a_{k+1}+2=O(\log(2Q_k))$, proving
(10).  This also gives the familiar equality $\mu(e)=2$: convergents give the
opposite inequality $|e-P_k/Q_k|<Q_k^{-2}$ infinitely often. $\square$

Applying (10) to $p_n/q_n$ and comparing with (1) yields


$$
q_n^2\log(2q_n)\gg (n+1)!.                                        \tag{12}
$$


Since trivially $q_n\leq n!$, for all sufficiently large $n$,


$$
\boxed{
 \frac12\log((n+1)!)-\frac12\log\log(2n!)-C
 \leq\log q_n\leq\log(n!).}                                      \tag{13}
$$


Here $C>0$ is an absolute constant.
Thus, without making any unproved assertion about the gcd,


$$
\begin{aligned}
 h(\alpha_n)&=\Theta_s(n\log n),\\
 \log H(P_n)&=\Theta_{s,d}(d n\log n).
 \end{aligned}                                                      \tag{14}
$$


More quantitatively, if


$$
\rho_n=\frac{-\log|\pi-\alpha_n|}{h(\alpha_n)},
 \qquad
 \sigma_n=\frac{-\log|\pi-\alpha_n|}{\log H(P_n)},
$$


then (2), (6), (7), and (13) imply


$$
\liminf_{n\to\infty}\rho_n\geq1,
     \qquad \limsup_{n\to\infty}\rho_n\leq2,                    \tag{15}
$$


and


$$
\liminf_{n\to\infty}\sigma_n\geq\frac1d,
     \qquad \limsup_{n\to\infty}\sigma_n\leq\frac2d.           \tag{16}
$$


The location inside these intervals depends on the actual denominator
cancellation in $E_n$.

## 4. Comparison with the established algebraic-approximation measure for $\pi$

Aleksentsev's 1999 theorem gives the following explicit broad measure.  If
$\zeta$ is algebraic, $D\geq\deg\zeta$, $L\geq L(\zeta)$,
$L\geq3$, and the parameter $D$ is sufficiently large, then


$$
|\pi-\zeta|\geq
 \exp\!\left[-21.4708D(\log L+D\log D)(1+\log D)\right].            \tag{17}
$$


Here $L(\zeta)$ is the length of the primitive minimal polynomial.  This is
the explicit theorem stated in the primary article's abstract.

Choose once and for all a sufficiently large $D\geq d$, and apply (17) with
$\zeta=\alpha_n$ and $L=\max(3,L(P_n))$.  Equation (7) gives


$$
|\pi-\alpha_n|\geq C_{s,D}\,q_n^{-K_{D,d}},
 \qquad
 K_{D,d}=21.4708\,D d(1+\log D).                                   \tag{18}
$$


By contrast, (3) and (10) already give the much stronger sequence-specific
bound


$$
|\pi-\alpha_n|=\left|e-\frac{p_n}{q_n}\right|
 \geq\frac{c}{q_n^2\log(2q_n)}=q_n^{-2-o(1)}.                       \tag{19}
$$


Thus (17) cannot contradict these approximants.  The exact quantitative gap is:

* in logarithmic Weil height, the construction has exponent at most $2$,
  while (17) has exponent $21.4708D d(1+\log D)$;
* in naive height/length, the construction has exponent at most $2/d$,
  while (17) has exponent $21.4708D(1+\log D)$.

For $d=1$, the specialized rational result is much stronger than (17):
Zeilberger and Zudilin proved


$$
\mu(\pi)\leq7.103205334137\ldots.                \tag{20}
$$


Even this says only $|\pi-a/b|\geq b^{-7.103205\ldots-\varepsilon}$
for all sufficiently large $b$, whereas the translated construction is bounded
by exponent $2+o(1)$.  The power-exponent gap is still more than $5.10$.

## 5. A general no-go theorem for Taylor, Padé, and all rational translations

The preceding obstruction has nothing specifically to do with Taylor series.

### Theorem (rational-translation barrier)

Assume $s=e+\pi$ is algebraic of degree $d$.  Let
$r_j=p_j/q_j\in\mathbf Q$ be any sequence in lowest terms, with
$q_j>0$, with $r_j\to e$,
and put $\beta_j=s-r_j$.  Then


$$
\begin{aligned}
 \deg\beta_j&=d,\\
 h(\beta_j)&=\log q_j+O_s(1),\\
 \log H_{\rm naive}(\beta_j)&=d\log q_j+O_{s,d}(1),\\
 |\pi-\beta_j|&=|e-r_j|
        \geq\frac{c}{q_j^2\log(2q_j)}.
\end{aligned}                                                       \tag{21}
$$


Here $H_{\rm naive}(\beta_j)$ means the maximum absolute coefficient of
the primitive integral minimal polynomial of $\beta_j$.  In (21), as everywhere
in this note, $q_j$ is the denominator **after** reducing $p_j/q_j$.
The asymptotic height identities in (21) hold for all sufficiently large $j$;
then $r_j$, for example, lies in the fixed interval $[2,3]$, so their implied
constants depend only on $s$ (and $d$), not on the chosen sequence.
In particular, for every fixed $\eta>0$, only finitely many members of such a
sequence can satisfy


$$
|\pi-\beta_j|\leq\exp(-(2+\eta)h(\beta_j)).                  \tag{22}
$$



**Proof.** The degree and height statements are exactly the rational-translation
arguments (4)--(7), with $r_j$ in place of $E_n$.  The error identity is
$\pi-(s-r_j)=r_j-e$, and the lower bound is (10). $\square$

Every rational Padé approximant to $e$, including one obtained by evaluating a
rational-function Padé approximant to $e^z$ at $z=1$, falls under this theorem
after reducing the resulting fraction.  Large unreduced integer coefficients do not
help: the relevant height is governed by the reduced denominator.  Continued-fraction
convergents are already optimal at the power level, because $\mu(e)=2$.

This gives a precise methodological no-go.  A pure fixed-degree/fixed-height lower
bound for $\pi$ with power exponent strictly larger than $2$ in Weil height is too
weak to contradict any rational-translation construction.  An exponent strictly
smaller than $2$ cannot hold uniformly even for rational approximants to an
arbitrary irrational number, by Dirichlet approximation.  The boundary exponent
$2$ would require sharp constants or logarithmic factors; no established measure
for $\pi$ supplies anything close to what is needed here.

This theorem does **not** rule out an argument using additional, highly special
arithmetic information about the numerators $p_j$, rather than merely degree and
height.  It does rule out replacing Taylor truncations by better rational Padé
approximants and then feeding only their degree, height, and error into a standard
algebraic-approximation measure for $\pi$.

## 6. Why conjugates and norms do not amplify the small error usefully

Let $s=s_1,s_2,\ldots,s_d$ be the conjugates of $s$, and let
$r=p/q\to e$.  For the integral translated polynomial


$$
G_r(X)=q^dF_s(X+r),
$$


factorization at $X=\pi$ gives the exact identity


$$
\begin{aligned}
 G_r(\pi)
 &=a_dq^d\prod_{i=1}^d(\pi+r-s_i)\\
 &=a_dq^d(r-e)\prod_{i=2}^d(\pi+r-s_i).                             \tag{23}
 \end{aligned}
$$


For $i\geq2$,


$$
\pi+r-s_i\longrightarrow \pi+e-s_i=s-s_i\neq0.
$$


Hence


$$
|G_r(\pi)|\asymp_s q^d|e-r|.                          \tag{24}
$$


The primitive minimal polynomial differs from $G_r$ by a bounded integer
content, so the same estimate holds for it.  Combining (10), (9), and (24),


$$
|G_r(\pi)|\gg_s\frac{q^{d-2}}{\log(2q)}
 \asymp_{s,d}\frac{H(G_r)^{1-2/d}}{\log H(G_r)}.                   \tag{25}
$$


Thus conjugate multiplication makes the polynomial value grow for $d\geq3$,
leaves at best a subpower-small value for $d=2$, and gives only the ordinary
rational-approximation scale for $d=1$.  It does not manufacture an exceptionally
small integer polynomial value at $\pi$.

There is also a basic norm obstruction.  The genuine field norm
$N_{\mathbf Q(s)/\mathbf Q}(s-r)$ contains no approximation error to $\pi$.
On the other hand,


$$
s-(\pi+r)=e-r
$$


is transcendental and is not an element of $\mathbf Q(s)$, so its field norm is
not defined.  The product in (23) is the transcendental number $G_r(\pi)$, not a
nonzero rational integer.  Therefore one cannot invoke the elementary lower bound
$|N|\geq1$.

## 7. Bottom line

For the Taylor sequence,


$$
|\pi-\alpha_n|\asymp\frac1{(n+1)!},
 \quad
 h(\alpha_n)=\log\!\left(\frac{n!}{\gcd(A_n,n!)}\right)+O_s(1),
$$


with the rigorous range


$$
\frac12\log((n+1)!)-O(\log\log(n!))
 \leq h(\alpha_n)\leq\log(n!)+O_s(1).
$$


The resulting approximation exponent is between $1$ and $2$ in Weil height,
and between $1/d$ and $2/d$ in naive height.  Established measures for $\pi$
have much larger lower-bound exponents, so there is no contradiction.

The obstruction is structural: under the algebraicity assumption, approximation of
$\pi$ by the affine rational line $s-\mathbf Q$ is exactly rational approximation
of $e$.  Since $\mu(e)=2$, Taylor truncations, rational Padé approximants, and
continued-fraction approximants cannot cross the power exponent $2$.  Any successful
argument along this conditional route must use information beyond a standard
degree-height approximation measure.

## Primary sources used

1. Yu. M. Aleksentsev, **“On the measure of approximation of the number $\pi$ by
   algebraic numbers,”** *Mathematical Notes* **66** (1999), 395--403,
   DOI [10.1007/BF02679086](https://doi.org/10.1007/BF02679086).  The primary
   publisher page states (17), including the constant $21.4708$ and its hypotheses.

2. Doron Zeilberger and Wadim Zudilin, **“The irrationality measure of $\pi$ is at
   most $7.103205334137\ldots$,”** *Moscow Journal of Combinatorics and Number
   Theory* **9** (2020), 407--419,
   DOI [10.2140/moscow.2020.9.407](https://doi.org/10.2140/moscow.2020.9.407);
   [authors' primary PDF](https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimPDF/pimeas.pdf).

3. Damien Roy and Michel Waldschmidt, **“Approximation diophantienne et
   indépendance algébrique de logarithmes,”** *Annales scientifiques de l'École
   Normale Supérieure* **30** (1997), 753--796,
   DOI [10.1016/S0012-9593(97)89938-7](https://doi.org/10.1016/S0012-9593(97)89938-7),
   [primary archive](https://www.numdam.org/articles/10.1016/s0012-9593(97)89938-7/).
   This supplies the general approximation-measure framework; the later explicit
   Aleksentsev bound is the one used quantitatively above.
