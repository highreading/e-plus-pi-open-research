> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exponential-theorem audit under the hypothesis $e+\pi\in\overline{\mathbb Q}$

Checked: 2026-08-26 UTC

## Verdict

Let



$$
s=e+\pi.
$$



This audit found several rigorous consequences of the temporary hypothesis



$$
(H)\qquad s\in\overline{\mathbb Q},
$$



including the following two particularly strong ones:

1. $\exp(qe)$ is transcendental for every
   $q\in\overline{\mathbb Q}^{\times}$.  In particular, $e^e$ is
   transcendental under $(H)$.
2. $\exp(\pi^2)$ is transcendental under $(H)$, by the
   Brownawell--Waldschmidt algebraic-independence theorem.

These conclusions do **not** contradict one another or any other presently
proved theorem.  After substituting $\pi=s-e$, they become statements about
additional nested exponential values, whose transcendence is compatible with
the single algebraic relation $e+\pi=s$.  Thus the theorems audited here do
not prove or disprove $(H)$.

Throughout, $\exp z$ denotes the complex exponential.  Superscripts such as
$e^2$ denote powers of Euler's number, so, for example,
$\exp(e^2)=e^{e^2}$.

## 1. The exact logarithmic setting

Write



$$
\mathcal L=\{z\in\mathbb C:\exp z\in\overline{\mathbb Q}^{\times}\}
$$



for the $\mathbb Q$-vector space of logarithms of nonzero algebraic
numbers, and write



$$
\widetilde{\mathcal L}
=\overline{\mathbb Q}+\overline{\mathbb Q}\mathcal L
$$



for the $\overline{\mathbb Q}$-vector space spanned by $1$ and
$\mathcal L$.  Choose



$$
\ell=i\pi=\log(-1)\in\mathcal L.
$$



Under $(H)$,



$$
\pi=-i\ell,
\qquad
e=s+i\ell,
$$



so both $e$ and $\pi$ belong to
$\widetilde{\mathcal L}$.  This membership is not forbidden by Baker's
theorem or by the strong six exponentials theorem.  In particular,
$\widetilde{\mathcal L}$ is only a vector space; it is not known to be
closed under products.

## 2. What Baker's theorem actually gives

We use the following standard nonhomogeneous consequence of Baker's theorem:
if $\lambda_1,\ldots,\lambda_n$ are logarithms of nonzero algebraic
numbers and $\beta_1,\ldots,\beta_n$ are algebraic, then



$$
\beta_1\lambda_1+\cdots+\beta_n\lambda_n
$$



is either zero or transcendental.  This is the form stated, for example, in
Alan Baker's paper *Linear forms in the logarithms of algebraic numbers
(III)* and in Waldschmidt's period survey.

### Lemma 2.1

Assume $(H)$.  If $q,r\in\overline{\mathbb Q}$ and $q\ne0$, then



$$
\exp(qe+r\pi)
$$



is transcendental.

### Proof

Suppose instead that $\alpha=\exp(qe+r\pi)$ is algebraic.  Then



$$
\lambda=qe+r\pi
$$



is a chosen logarithm of the algebraic number $\alpha$, while
$\ell=i\pi$ is a logarithm of $-1$.  Since $e=s-\pi$,



$$
\lambda-i(q-r)\ell
=qe+r\pi-i(q-r)i\pi
=q(e+\pi)
=qs.
$$



The left side is a linear form, with algebraic coefficients, in logarithms
of algebraic numbers.  The right side is a nonzero algebraic number because
$q\ne0$ and $s=e+\pi>0$.  Baker's theorem says that the nonzero left
side must be transcendental, a contradiction.  QED.

Taking $r=0$ gives



$$
\boxed{\ \exp(qe)\text{ is transcendental for every }
q\in\overline{\mathbb Q}^{\times}.\ }
$$



Important special cases are



$$
e^e=\exp(e),
\qquad
\exp(-2se).
$$



Both are therefore transcendental under $(H)$.  The same lemma also
implies that $\sin(qe)$ and $\cos(qe)$ are transcendental for every
nonzero algebraic $q$: if either were algebraic, then
$z=\exp(iqe)$ would satisfy a quadratic equation over
$\overline{\mathbb Q}$, contradicting the lemma with coefficient $iq$.

An unconditional way to record the first special case is the disjunction



$$
\text{at least one of }e+\pi\text{ and }e^e\text{ is transcendental}.
$$



This is useful structural information, but it does not decide which member is
transcendental.

### Why Baker does not settle the original relation

Under $(H)$, Baker's theorem applied directly to



$$
e=s+i\log(-1)
$$



merely re-proves that $e$ is transcendental.  On substituting this
expression into $e+\pi-s$, the two occurrences of $\log(-1)$ cancel and
the linear form is exactly zero.  Baker's lower bounds apply to nonzero
linear forms and give no contradiction for this tautological zero.

Also, $1=\log e$ cannot be used as a Baker logarithm: Baker's inputs are
logarithms of **algebraic** numbers, whereas Euler's number $e$ is
transcendental.  The hypothesis $(H)$ supplies only one certified
logarithmic direction, namely $i\pi$, not a second independent logarithm.

## 3. The Brownawell--Waldschmidt disjunction

A theorem of Brownawell and Waldschmidt has the following consequence:



$$
\boxed{\quad
\exp(\pi^2)\text{ is transcendental}
\quad\text{or}\quad
e,\pi\text{ are algebraically independent}.
\quad}
$$



Here is an exact derivation from the algebraic-independence theorem stated as
Theorem 2.49(4) in Waldschmidt's lecture notes.  That theorem says that, if
$x_1,x_2$ and $y_1,y_2$ are each $\mathbb Q$-linearly independent
and $\exp(x_1y_1),\exp(x_1y_2)$ are algebraic, then at least two of



$$
x_1,x_2,y_1,y_2,\exp(x_2y_1),\exp(x_2y_2)
$$



are algebraically independent.  Put



$$
x_1=y_1=i\pi,
\qquad
x_2=y_2=1.
$$



If $\exp(\pi^2)$ were algebraic, then



$$
\exp(x_1y_1)=\exp(-\pi^2),
\qquad
\exp(x_1y_2)=\exp(i\pi)=-1
$$



would both be algebraic.  The six numbers in the conclusion reduce to



$$
i\pi,1,i\pi,1,-1,e.
$$



Thus the only possible algebraically independent pair is $i\pi,e$, so
$e$ and $\pi$ must be algebraically independent.

Under $(H)$, however, $e$ and $\pi$ are algebraically dependent: if
$M\in\mathbb Q[T]$ is the minimal polynomial of $s$, then the nonzero
polynomial $M(X+Y)$ vanishes at $(e,\pi)$.  Consequently the second
branch of the boxed disjunction is impossible, and we obtain the rigorous
conditional consequence



$$
\boxed{\ (H)\Longrightarrow \exp(\pi^2)\text{ is transcendental}.\ }
$$



This is not a contradiction.  The theorem forces a new transcendental value;
it does not assert that $\exp(\pi^2)$ is algebraic.

The other classical Brownawell--Waldschmidt consequence says that at least
one of $e^e$ and $e^{e^2}$ is transcendental.  Under $(H)$, Lemma
2.1 already forces the first member $e^e$ to be transcendental, so this
disjunction is automatically satisfied and gives no information about
$e^{e^2}$.

## 4. Exact comparison with Nesterenko's theorem

Nesterenko proved that



$$
\pi\quad\text{and}\quad V=\exp(\pi)
$$



are algebraically independent.  Under $(H)$, translating
$\pi=s-e$ by the algebraic number $s$ gives



$$
e\quad\text{and}\quad V
$$



algebraically independent.  Equivalently, if



$$
K=\overline{\mathbb Q}(e)=\overline{\mathbb Q}(\pi),
$$



then $V$ is transcendental over $K$.

Set



$$
U=\exp(s),
\qquad
A=\exp(e)=e^e.
$$



The identity $s=e+\pi$ gives



$$
U=AV,
\qquad
V=\frac{U}{A}.
$$



There are two genuinely different algebraic cases for $s$.

* If $s=a/b\in\mathbb Q$, then $U^b=e^a$, so $U$ is algebraic
  over $K$.  Since $V=U/A$ is transcendental over $K$, $A$ is
  transcendental over $K$.  Hence $e$ and $e^e$ are algebraically
  independent in this special rational case.
* If $s$ is algebraic irrational, Lindemann--Weierstrass shows that
  $e=\exp(1)$ and $U=\exp(s)$ are algebraically independent.  Indeed,
  a polynomial relation would expand into a nontrivial algebraic linear
  relation among exponentials of the distinct algebraic numbers $m+ns$.
  Thus both $U$ and $V$ are transcendental over $K$, but the two
  pairwise algebraic-independence statements do not control their quotient
  $A=U/V$ over $K$.  Baker's theorem proves that $A$ is
  transcendental over $\overline{\mathbb Q}$, not that it is
  transcendental over $K$.

More generally, if $s$ has algebraic degree $d$, then



$$
\exp(1),\exp(s),\ldots,\exp(s^{d-1})
$$



are algebraically independent by Lindemann--Weierstrass, because
$1,s,\ldots,s^{d-1}$ are $\mathbb Q$-linearly independent.  There is
no upper bound coming from $(H)$ on the transcendence degree contributed
by such new exponential values, so this also creates no contradiction.

## 5. Why the substitution in $\exp(\pi^2)$ does not close

Introduce



$$
B=\exp(e^2),
\qquad
C=\exp(\pi^2),
\qquad
D=\exp(s^2),
\qquad
E=\exp(-2se).
$$



The exact substitution $\pi=s-e$ gives



$$
\pi^2=s^2-2se+e^2
$$



and hence



$$
\boxed{\ C=DBE.\ }
$$



Equivalently, because $A=\exp(e)>0$,



$$
C=D\,B\,A^{-2s},
$$



where $A^{-2s}$ means the unambiguous positive real value
$\exp(-2se)$.

Under $(H)$, the currently proved statuses are:

| Quantity | What is rigorously known under $(H)$ | Reason |
|---|---|---|
| $A=\exp(e)$ | transcendental | Lemma 2.1 |
| $D=\exp(s^2)$ | transcendental | Hermite--Lindemann, since $s^2\ne0$ is algebraic |
| $E=\exp(-2se)$ | transcendental | Lemma 2.1 with $q=-2s$ |
| $C=\exp(\pi^2)$ | transcendental | Brownawell--Waldschmidt plus the dependence of $e,\pi$ |
| $B=\exp(e^2)$ | undetermined | its exponent is quadratic in the logarithmic parameter |

The identity $C=DBE$ is therefore an equality among several
transcendental quantities and one uncontrolled quantity.  A product or
quotient of transcendental numbers may be algebraic or transcendental, so
these classifications do not conflict.  Lindemann--Weierstrass cannot be
applied directly to $e^2$ or $-2se$, because those exponents are not
algebraic; Lemma 2.1 handles the latter only through a proof by contradiction
using Baker's theorem.  Gelfond--Schneider also does not control
$A^{-2s}$ from the displayed power expression, because its base $A$ is
transcendental under $(H)$.

The unavoidable quadratic term $e^2$, or equivalently
$(\log(-1))^2$, is precisely where the linear-forms-in-logarithms method
stops.

## 6. Six exponentials, strong six exponentials, and four-exponential variants

### 6.1 The sharp six exponentials theorem

The sharp six exponentials theorem permits algebraic shifts
$\beta_{ij}$: under its independence hypotheses, if all
$\exp(x_i y_j-\beta_{ij})$ are algebraic, then every logarithmic part
$x_i y_j-\beta_{ij}$ must vanish.

Take



$$
\lambda=i\pi,
\qquad
x_1=y_1=1,
\qquad
x_2=y_2=\lambda,
\qquad
y_3=\lambda^2,
$$



with $\beta_{11}=1$ and all other $\beta_{ij}=0$.  Since
$1,\lambda,\lambda^2$ are $\mathbb Q$-linearly independent, the
theorem shows that $\exp(\lambda^2)$ and $\exp(\lambda^3)$ cannot both
be algebraic.  Thus, unconditionally, at least one of



$$
\exp(\pi^2)
\quad\text{and}\quad
\exp(-i\pi^3)
$$



is transcendental.  (Taking an inverse does not change algebraicity.)  Under
$(H)$, the Brownawell--Waldschmidt result is stronger for the present
purpose because it selects $\exp(\pi^2)$ itself.

The unshifted six exponentials theorem does not give this selection: the
same natural array contains $\exp(1)=e$, which is already known to be
transcendental, so its conclusion is satisfied before the quadratic entries
are examined.

### 6.2 A rigorous consequence of Roy's strong six exponentials theorem

Roy's strong six exponentials theorem states that if
$x_1,x_2$ are linearly independent over $\overline{\mathbb Q}$ and
$y_1,y_2,y_3$ are linearly independent over
$\overline{\mathbb Q}$, then at least one of the six products
$x_i y_j$ does not belong to $\widetilde{\mathcal L}$.

Under $(H)$, take



$$
(x_1,x_2)=(1,e),
\qquad
(y_1,y_2,y_3)=(e^n,e^{n+1},e^{n+2})
$$



for any integer $n\ge0$.  The required independence holds because $e$
is transcendental.  The six products are the four consecutive powers



$$
e^n,e^{n+1},e^{n+2},e^{n+3}
$$



with repetitions.  Therefore every block of four consecutive powers
contains some $e^k\notin\widetilde{\mathcal L}$.  For such a $k$,
$\exp(e^k)$ is transcendental, since algebraicity of $\exp(e^k)$
would put $e^k$ in $\mathcal L$.

In particular, the first block gives



$$
e^2\notin\widetilde{\mathcal L}
\quad\text{or}\quad
e^3\notin\widetilde{\mathcal L},
$$



and hence at least one of $\exp(e^2)$, $\exp(e^3)$ is
transcendental under $(H)$.  This is a genuine all-degree consequence,
but again it supplies new transcendental values rather than contradicting
$(H)$.

### 6.3 What remains conjectural

The following tempting strengthenings are not theorems.

* The four exponentials conjecture replaces the $2$-by-$3$ array by a
  $2$-by-$2$ array.
* The strong four exponentials conjecture makes the analogous replacement in
  Roy's theorem for $\widetilde{\mathcal L}$.  Applied to
  $(1,\pi)$ on both sides, it would imply
  $\pi^2\notin\widetilde{\mathcal L}$, and hence the transcendence of
  $\exp(\pi^2)$.  It would not by itself contradict $(H)$.
* The sharp five exponentials conjecture would also imply the
  transcendence of $\exp(\pi^2)$ unconditionally.  Waldschmidt explicitly
  presents this as a conjectural consequence; the proved sharp six theorem
  only gives the disjunction involving $\exp(-i\pi^3)$.

There are proved four-exponential special cases based on complex conjugation
(Diaz, Theorems 1--3).  The special case relevant here (Diaz, Theorem 2)
requires three quantities
$1,y,\overline y$ to be linearly independent over
$\overline{\mathbb Q}$.  Natural choices built only from the affine space
$\overline{\mathbb Q}+\overline{\mathbb Q}e$ forced by $(H)$ fail
this condition; introducing $e^2$ or another new quantity restores the
hypothesis only by introducing exactly the uncontrolled product one hoped to
avoid.

## 7. Synthesis: why there is no contradiction

The assumption $(H)$ has two different effects:

1. It collapses the ordinary field
   $\overline{\mathbb Q}(e,\pi)$ to the one-variable field
   $\overline{\mathbb Q}(e)$.
2. It does **not** bound the transcendence degree of fields obtained after
   adjoining nested exponential values such as
   $\exp(e)$, $\exp(e^2)$, $\exp(\pi^2)$, or $\exp(s)$.

Each applicable theorem uses the second freedom to avoid a contradiction:

* Baker forces $\exp(qe)$ to be transcendental.
* Brownawell--Waldschmidt forces $\exp(\pi^2)$ to be transcendental.
* Nesterenko forces $\exp(\pi)$ to be transcendental over
  $\overline{\mathbb Q}(e)$.
* Roy's strong six exponentials theorem forces infinitely many powers to
  leave $\widetilde{\mathcal L}$.

None of these theorems gives an upper bound that those forced new
transcendental values violate.  The exact identities



$$
\exp(s)=\exp(e)\exp(\pi)
$$



and



$$
\exp(\pi^2)=
\exp(s^2)\exp(e^2)\exp(-2se)
$$



therefore remain compatible with all their conclusions.  The audit has not
produced a proof of either algebraicity or transcendence of $e+\pi$.

## Primary papers and first-party theorem expositions

1. W. Dale Brownawell, *The algebraic independence of certain numbers
   related by the exponential function*, Journal of Number Theory 6 (1974),
   22--31,
   [DOI 10.1016/0022-314X(74)90005-5](https://doi.org/10.1016/0022-314X%2874%2990005-5).
2. Michel Waldschmidt, *Solution du huitième problème de Schneider*, Journal
   of Number Theory 5 (1973), 191--202,
   [DOI 10.1016/0022-314X(73)90044-9](https://doi.org/10.1016/0022-314X%2873%2990044-9),
   and the later exposition
   [*On the numbers $e^e,e^{e^2}$ and $e^{\pi^2}$*](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/HRJ.html).
3. Michel Waldschmidt, *AWS Lecture 2*, Theorem 2.49 and its explicit
   [$e^{\pi^2}$ corollary](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/AWSLecture2.pdf).
4. Alan Baker, *Linear forms in the logarithms of algebraic numbers (III)*,
   Mathematika 14 (1967), 220--228,
   [DOI 10.1112/S0025579300003843](https://doi.org/10.1112/S0025579300003843).
5. Yu. V. Nesterenko, *Modular functions and transcendence questions*,
   Sbornik: Mathematics 187 (1996), 1319--1348,
   [DOI 10.1070/SM1996v187n09ABEH000158](https://doi.org/10.1070/SM1996v187n09ABEH000158);
   [full text](https://www.mathnet.ru/eng/sm158).
6. Damien Roy, *Matrices whose coefficients are linear forms in logarithms*,
   Journal of Number Theory 41 (1992), 22--47, especially Section 4,
   Corollary 2,
   [DOI 10.1016/0022-314X(92)90081-Y](https://doi.org/10.1016/0022-314X%2892%2990081-Y).
7. Michel Waldschmidt, *The Role of Complex Conjugation in Transcendental
   Number Theory*, especially Sections 2--5 for the six/strong-six theorems,
   the four/strong-four conjectures, and
   [Diaz's special cases](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/DION2005proceedings.pdf).
8. Guy Diaz, *Utilisation de la conjugaison complexe dans l'étude de la
   transcendance de valeurs de la fonction exponentielle usuelle*, Journal de
   théorie des nombres de Bordeaux 16 (2004), 535--553,
   [DOI 10.5802/jtnb.459](https://doi.org/10.5802/jtnb.459).
9. Michel Waldschmidt, *Hopf Algebras and Transcendental Numbers*, especially
   [Theorem 1.4 and the discussion of the sharp five exponentials conjecture](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/ztq2003.pdf).
