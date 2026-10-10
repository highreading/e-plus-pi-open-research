> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Algebraicity-direction audit

Date: 2026-08-26

Let



$$
s=e+\pi.
$$



The requested statement that $s$ is “not transcendental” is exactly
$s\in\overline{\mathbb Q}$. This note investigates that direction rather
than treating a search for transcendence as a substitute.

## 1. Exact algebraic structure if the requested conclusion is true

Put $K=\overline{\mathbb Q}$, and assume $s\in K$. Consider



$$
\operatorname{ev}:K[X,Y]\longrightarrow\mathbb C,
\qquad P\longmapsto P(e,\pi).
$$



Then



$$
\ker(\operatorname{ev})=(X+Y-s).
$$



Indeed, the relation $e+\pi=s$ gives the inclusion from right to left. On
the other hand,



$$
K[X,Y]/(X+Y-s)\simeq K[X]
$$



by $Y\mapsto s-X$, and evaluation $K[X]\to\mathbb C$, $X\mapsto e$,
is injective because $e$ is transcendental. This proves the equality of
ideals.

Thus the algebraicity hypothesis is internally consistent with the known
individual transcendence of $e$ and $\pi$: it would leave exactly one
algebraic relation over $K$, namely the requested linear relation and its
multiples. In particular,



$$
K(e)=K(\pi),\qquad \operatorname{trdeg}_{K}K(e,\pi)=1.
$$



More generally, after substituting $Y=s-X$, every rational expression in
$e,\pi$ becomes a rational function of the one transcendental element
$e$. Every nonconstant such rational function is transcendental over
$K$. This immediately proves, under the hypothesis, that $e\pi$,
$e-\pi$, $e/\pi$, and $\pi/e$ are transcendental. None of these
consequences contradicts an accepted theorem.

This relation-ideal calculation also identifies what individual
transcendence arguments cannot do: proving only that each coordinate is
transcendental is compatible with the prime ideal $(X+Y-s)$. One needs a
genuinely mixed theorem or an exact mixed identity.

## 2. Model-theoretic formulation: a predimension-minus-one point

Let



$$
z_1=1,\qquad z_2=i\pi,\qquad w_j=\exp(z_j).
$$



The numbers $z_1,z_2$ are linearly independent over $\mathbb Q$, and
$w_1=e,\ w_2=-1$. If $s\in K$, then



$$
w_1-i z_2=s.
$$



Consequently,



$$
\operatorname{trdeg}_{\mathbb Q}
 \mathbb Q(z_1,z_2,w_1,w_2)
=\operatorname{trdeg}_{\mathbb Q}\mathbb Q(\pi,e)=1,
$$



whereas



$$
\dim_{\mathbb Q}\langle z_1,z_2\rangle=2.
$$



In the usual predimension notation this gives



$$
\delta(z_1,z_2)=1-2=-1.
$$



Hence the requested algebraicity would be an explicit counterexample to
Schanuel’s conjecture.

The same point can be encoded geometrically. For an algebraic parameter
$s$, let $V_s\subset\mathbb G_a^2\times\mathbb G_m^2$ be defined by



$$
z_1=1,\qquad w_2=-1,\qquad w_1-i z_2=s.
$$



This irreducible variety has dimension $1<2$. The requested conclusion says
that for some $s\in K$, $V_s$ contains the exponential-graph point
$(1,i\pi,e,-1)$ whose additive coordinates are
$\mathbb Q$-linearly independent. This is precisely the low-dimensional
configuration excluded by Schanuel’s conjecture.

Zilber’s exponential-algebraic closedness philosophy does not positively
predict such a point. Its existence statements require freeness/rotundity and
the corresponding dimension inequalities; the variety above is already one
dimension too small. Thus “converse Schanuel” or existential closedness cannot
be used as evidence for algebraicity here.

Primary source for the model-theoretic dimension distinction:

- F. P. Gallinaro, *Exponential sums equations and tropical geometry*,
  Selecta Math. 29 (2023), article 49,
  https://doi.org/10.1007/s00029-023-00853-y . The introduction explicitly
  notes that the $n=2$ Schanuel case would imply algebraic independence of
  $e$ and $\pi$, while exponential-algebraic closedness applies on the
  existence side only after the required dimension conditions.

## 3. E-values and G-values: algebraicity would create forbidden overlap

Let $\mathbf E$ be the ring of values of Siegel E-functions at algebraic
points and $\mathbf G$ the ring of values of analytic continuations of
G-functions at algebraic points. The function $\exp z$ is an E-function,
so $e\in\mathbf E$. The function



$$
\arctan z=\sum_{n\geq0}\frac{(-1)^n z^{2n+1}}{2n+1}
$$



is a G-function, and $4\arctan(1)=\pi$, so
$\pi\in\mathbf G$. Both rings contain $K$.

If $s\in K$, ring closure gives



$$
\pi=s-e\in\mathbf E\cap\mathbf G,
\qquad
e=s-\pi\in\mathbf E\cap\mathbf G.
$$



Both elements are transcendental. Therefore the requested conclusion would
refute the standard intersection conjecture



$$
\mathbf E\cap\mathbf G=\overline{\mathbb Q}.
$$



This is a conjecture about *value rings*. It must not be confused with the
proved fact that the intersection of the corresponding classes of power
series consists only of algebraic polynomials. Special values are the hard
part.

Primary source:

- S. Fischler and T. Rivoal, *Relations between values of arithmetic Gevrey
  series, and applications to values of the Gamma function*, J. Number Theory
  261 (2024), 36–54,
  https://arxiv.org/abs/2301.13518 . The authors state explicitly that
  $\mathbf E\cap\mathbf G=\overline{\mathbb Q}$ is natural and currently
  out of reach.

Recent $p$-adic algebraic-independence theorems for selected E- and
G-*functions* do not close this gap: they prove independence over fields of
analytic elements, not algebraic independence of their complex values at
$z=1$. See D. Vargas-Montoya, *On the Algebraic Independence of E- and
G-Functions, II: An Effective Version*, https://arxiv.org/abs/2507.20429 .

## 4. Period formulation: algebraicity would turn $e$ into a usual period

Algebraic numbers and $\pi$ are ordinary periods, and ordinary periods form
a ring. Thus $s\in K$ would imply



$$
e=s-\pi
$$



is an ordinary period.

Fresán and Jossen’s exponential period conjecture predicts the opposite in a
strong form. Their Proposition 12.1.4 says, conditional on their exponential
period conjecture, that the exponential of every nonzero algebraic number is
transcendental over the field generated by ordinary periods. Taking the
algebraic exponent $1$ says that $e=\exp(1)$ is transcendental over that
field. It therefore cannot itself be an ordinary period.

Hence



$$
e+\pi\in\overline{\mathbb Q}
\quad\Longrightarrow\quad
\text{the exponential period conjecture is false}.
$$



Primary source:

- J. Fresán and P. Jossen, *Exponential motives*, Conjecture 8.2.6 and
  Proposition 12.1.4,
  https://javier.fresan.perso.math.cnrs.fr/expmot.pdf .

The ordinary Kontsevich–Zagier period conjecture alone should not be cited as
proving that $e$ is not a period: the relevant separator is the extension to
exponential motives.

## 5. Why numerical evidence cannot certify the requested conclusion

Every nonempty real interval contains both algebraic and transcendental
numbers. Rationals are dense, and the transcendental numbers are dense because
an interval is uncountable whereas the algebraic numbers are countable. It
follows rigorously that:

1. no finite decimal prefix can distinguish algebraicity from transcendence;
2. no finite continued-fraction prefix can do so;
3. a finite exact interval enclosure, however narrow, cannot do so;
4. excluding polynomials only up to fixed degree and height leaves infinitely
   many algebraic candidates of larger complexity.

PSLQ can propose a polynomial. It cannot certify that the polynomial
vanishes. Once a candidate $P\in\mathbb Z[T]$ is proposed, interval
arithmetic can often prove $P(s)\ne0$, but arbitrarily many matching digits
cannot prove $P(s)=0$ without an independent exact identity. Algebraicity
itself supplies no a priori finite bound on the degree or height of the
minimal polynomial.

For the rational subcase there is a valid exact target. Runlong Yu proves
that, with



$$
A_N=\lceil N!\pi\rceil,
$$



one has $e+\pi\in\mathbb Q$ if and only if there exists $N_0$ such that



$$
A_{N+1}=(N+1)A_N-1
$$



for every $N\geq N_0$. Proving this recurrence eventually would be a
correct positive proof (indeed, a proof of rationality), but checking any
finite number of instances cannot establish the universal tail statement.

Primary source:

- R. Yu, *Tail Criteria, No-Go Audits, and Apéry-Type Certificate
  Obstructions for the Irrationality of $e+\pi$*, Theorem 3.1,
  https://arxiv.org/abs/2606.17303 .

## 6. Why standard functional identities do not certify algebraicity

Euler’s identity gives



$$
\exp(i\pi)=-1,
$$



and the definition of $e$ gives $e=\exp(1)$. These are two values of the
same function, but no proved theorem converts them into a polynomial relation
between the input $i\pi$ of one value and the output $e$ of the other.
Schanuel’s conjecture is exactly a framework designed to control such mixed
input-output relations, and it predicts that the requested cancellation does
not occur.

Ax–Schanuel is a functional/differential theorem, not the missing numerical
specialization theorem. Its hypotheses measure nonconstant functions modulo
constants; substituting constant functions removes the derivative rank and
does not yield a statement about $1,i\pi,e,-1$.

Likewise, Siegel–Shidlovskii/Beukers lifting controls algebraic relations
among values of E-functions in a common E-function system. The arctangent
side is a G-function. There is currently no mixed E/G lifting theorem that
turns functional independence into the needed statement about the complex
values $e$ and $\pi$. The conjectured mixed separator would again prove
the opposite, not algebraicity.

## 7. What a correct positive proof must contain

There is no numerical shortcut. A positive solution must ultimately prove
the existence of a polynomial relation by at least one of the following kinds
of exact argument (the polynomial could in principle be obtained
nonconstructively):

1. a displayed nonzero polynomial $P\in\mathbb Z[T]$ together with an exact
   proof that
   

$$
P\bigl(\exp(1)+4\arctan(1)\bigr)=0;
$$


2. an exact analytic or arithmetic identity identifying $e+\pi$ with a
   specified algebraic number, or with a specified root of such a polynomial;
3. in the rational subcase, a proof of an eventual all-$N$ criterion such as
   Yu’s ceiling recurrence;
4. in period language, an explicit unexpected relation making the exponential
   period $e$ equal to an ordinary period $s-\pi$.

Any such proof would have major collateral consequences: it would give a
counterexample to Schanuel’s conjecture, to the E/G value-ring intersection
conjecture, and to the exponential period conjecture. This does not logically
make algebraicity impossible, but it shows that no accepted structural
conjecture currently supports the requested direction. The standard
conjectural frameworks independently support transcendence.

A sharp theorem that would settle the problem in the opposite direction, and
is much weaker than full Schanuel, is the following kernel–exponential
separation statement. If $\omega=2\pi i$ generates the kernel of the
complex exponential, prove that for nonzero
$a,b\in\overline{\mathbb Q}$,



$$
\exp(a)+b\omega\notin\overline{\mathbb Q}.
$$



The choice $a=1$ and $b=1/(2i)$ is exactly $e+\pi$. No such theorem is
known. Schanuel’s conjecture implies it by applying the transcendence-degree
bound to $a$ and $\omega$.

## Conclusion of this audit

No rigorous positive implication or accepted conjecture supporting
$e+\pi\in\overline{\mathbb Q}$ was found. The hypothesis is compatible with
all currently proved individual facts examined here, but it forces one
specific mixed relation and would simultaneously violate three central
conjectural separation principles. Numerical and global functional identities
cannot certify that isolated mixed relation without a new exact special-value
theorem or an explicit polynomial certificate.
