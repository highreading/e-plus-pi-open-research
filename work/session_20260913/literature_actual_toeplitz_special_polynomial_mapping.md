> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact mapping audit: the actual Toeplitz family and Painlevé special polynomials

Date: 2026-09-13. Bounded primary-source audit and original specialization
by audit_sources.

The actual determinant is exactly a Wronskian Appell polynomial after a
known hook normalization. This directly supplies an arithmetic theorem.
The proposed generalized-Laguerre, Umemura and Yablonskii--Vorob'ev
identifications have not been established: their particular partitions
and generating-function parameters differ. No Painlevé resultant or
prime-reduction theorem is transferred on the basis of resemblance.

## 1. The actual object, with both Schur conventions

Keep the original background integer $n$ visible:


$$
a_k^{[n]}(x)=[t^k]e^{xt}(1+t^2)^n,\qquad
 D_n(x)=\det(a_{n+i-j}^{[n]}(x))_{i,j=0}^{n}.
                                                               \tag{1}
$$


The prior reviewed note raw_odd_toeplitz_deformation_and_schur_coefficients.md
proved the elementary-specialization identity


$$
D_n=s_{((n+1)^n)}[E],\qquad E(t)=e^{xt}(1+t^2)^n.       \tag{2}
$$


For comparison with papers using complete symmetric functions, there
are two equivalent precise conventions:

* Use complete generating series $H(t)=e^{xt}(1+t^2)^{-n}$ and the
  partition $((n+1)^n)$. Its times, defined by
  $H=\exp(\sum t_jt^j)$, are $t_1=x$,
  $t_{2j}=(-1)^j n/j$, and $t_{2j+1}=0$ for $j\ge1$.
* Treat the actual $a_k^{[n]}$ as complete functions, with generating
  series $e^{xt}(1+t^2)^n$, and use the conjugate rectangle
  $(n^{n+1})$. The even times have the opposite signs.

Both yield the same determinant. Conjugating the partition without
changing the elementary/complete specialization is not legitimate.
Its degree is $n(n+1)$, and it is an even polynomial in $x$.

## 2. Clarkson--Dunning generalized Laguerre polynomials

The correct authors of arXiv:2304.01579 are Peter Clarkson and Clare
Dunning. The final paper is *Studies in Applied Mathematics* 152 (2024),
453--507. Definition 3.1, Lemma 3.2 and Lemma 3.5 give its exact
Laguerre determinant, Wronskian, and rectangular Schur forms; Lemma 3.10
gives a differential Toda relation. Crucially, the general discriminant
product is explicitly **Conjecture 8.1**, with the discussion after it
asking for a proof. It must not be promoted from the abstract into a
proved arithmetic result.
[Primary v4, §§3 and 8.1](https://arxiv.org/html/2304.01579v4).

To compare the specialization directly, their $T_{M,N}^{(\mu)}(z)$
uses rectangle $((M+1)^N)$ and complete times


$$
t_j=\frac{\mu+N+1}{j}-z\quad(j\ge1).                   \tag{3}
$$


Matching the actual rectangle in the first convention of Section 1
would require $M=N=n$. But our times of orders three and five both
vanish. Equality with (3) would give
$(\mu+n+1)/3-z=(\mu+n+1)/5-z=0$, hence
$\mu+n+1=z=0$; the first time would then vanish rather than equal the
variable $x$. A nonzero linear rescaling of the generating variable
does not remove this contradiction.

Equivalently, their generating function is


$$
(1-t)^{-(\mu+N+1)}\exp\{-zt/(1-t)\},
$$


whereas ours has two distinct logarithmic poles at $t=\pm i$ and an
exponential linear in $t$. These are not identical coefficient
families. This proves the failure of the direct generating-function
matching; it does not purport to exclude every possible nontrivial
identity involving another partition or a quadratic change of the
external variable.

## 3. The 1999 PIII Umemura formula and the 2001 PV universal characters

Kajiwara and Masuda's *On the Umemura polynomials for the Painlevé III
equation*, arXiv:solv-int/9903015, Theorem 1 and equations (10)--(15),
uses a staircase Schur partition and coefficient generating function
$(1+t)^\eta e^{xt}$. Its Proposition 3 is a specific nonlinear
recurrence for that staircase family.
[Primary paper, pp.3--4](https://arxiv.org/pdf/solv-int/9903015).

Our rectangle is not that staircase, and our logarithm has two poles
rather than one. Substituting $t^2$ into the PIII generator would
change the exponential to $e^{xt^2}$, losing the actual odd
coefficients. Taking a square root instead requires two parity
components and does not yield the cited scalar determinant.

Masuda, Ohta and Kajiwara's *A determinant formula for a class of
rational solutions of Painlevé V*, arXiv:nlin/0101056, Definition 1.1,
defines universal characters for arbitrary pairs of partitions.
Theorem 1.2 specializes to **two staircase partitions** with times
$t_j^{(1)}=-t/2+(2s-m+n)/j$ and
$t_j^{(2)}=t/2+(2s-m+n)/j$.
[Primary paper, pp.2--3](https://arxiv.org/pdf/nlin/0101056).

An ordinary Schur function is tautologically a universal character
with one partition empty. Thus our determinant belongs to that broad
algebraic class. This tautological inclusion does not place its
rectangle and times on the particular two-staircase specialization
of Theorem 1.2. No exact parameter map to that theorem was found.

## 4. The 2026 discrete-PV paper

The verified article is Clarkson, Dunning and Mitchell, *Discrete
equations from Bäcklund transformations of the fifth Painlevé equation*,
published July 16, 2026, DOI 10.1007/s11040-026-09571-1.
Definition 4.7 expresses its generalized Umemura family using two
odd-degree Laguerre sequences; Theorem 4.9 and §5 construct rational
PV and discrete-PV solutions from those specified polynomials.
Remarks 4.10 describe certain additional logarithmic-derivative
identities as checked for small indices, rather than proved there.
[Primary article, §§4--5](https://pmc.ncbi.nlm.nih.gov/articles/PMC13372934/).

In particular, its equation (4.18) is a Wronskian of
$e^{-z/2}L_{1,3,\ldots,2m-1}^{(\kappa)}(z/2)$ together with
$L_{1,3,\ldots,2N-1}^{(\kappa)}(-z/2)$, with an explicit exponential
and scalar normalization. The actual determinant (1) instead has
consecutive Appell indices $n,\ldots,2n$ and a fixed background $n$
in its generator. No row operation, parameter assignment or
normalization identity identifying these has been proved.

This recent paper supplies neither an applicable prime-power
integrality theorem nor a resultant identity for our actual endpoint
values without that missing map.

## 5. The Yablonskii--Vorob'ev prime-reduction theorem

Kaneko and Ochiai, *On coefficients of Yablonskii--Vorob'ev polynomials*,
J. Math. Soc. Japan 55 (2003), 985--993, Theorem 3, proves


$$
T_{mp+n}(x)\equiv
 x^{d_{mp+n}-d_n}T_n(x)\pmod p,\qquad
 d_n=n(n+1)/2,\quad p>3.
$$


Their normalization is fixed by $T_0=1,T_1=x$.
Equations (4)--(7) identify the staircase determinant generated by
$\exp(xt+t^3/3)$.
[Primary paper, pp.986--987 and §4](https://www.jstage.jst.go.jp/article/jmath1948/55/4/55_4_985/_pdf/-char/en).

Both the staircase and the cubic-only nonconstant time are different
from (1). Applying this congruence to our rectangle would therefore be
invalid. Moreover, reducing a determinant with factorial coefficient
denominators modulo a small prime requires its actual integral
normalization first. The theorem's normalization cannot simply be
replaced by our raw Toeplitz determinant.

## 6. A published theorem that does apply exactly

Bonneux, Hamaker, Stembridge and Stevens, *Wronskian Appell polynomials
and symmetric functions*, Advances in Applied Mathematics 111 (2019),
101932, Theorem 4.1 and Proposition 4.3 identify normalized Appell
Wronskians with augmented Schur functions. Theorem 5.8 proves
integrality under integral cumulant-ratio hypotheses. Its proof uses
the stronger universal fact $H(\lambda)s_\lambda\in\mathbb Z[p_1,p_2,\ldots]$.
[Primary paper, §§4 and 5.4](https://arxiv.org/pdf/1812.01864v2).

For the actual Appell sequence
$\mathcal A_k=k!a_k^{[n]}$, the power-sum images are exactly


$$
p_1\mapsto x,\quad p_{2j}\mapsto2n(-1)^{j+1},
 \quad p_{2j+1}\mapsto0\quad(j\ge1).
$$


Thus the hypotheses hold for every fixed $n$. The original
specialization, including its complete row/corner normalization, is
proved in raw_appell_hook_normalization_congruence.md:


$$
H_DD_n(x)\equiv x^{n(n+1)}\pmod{2n},\qquad
 H_BB_n(x)\equiv x^{n^2}\pmod{2n},
$$




$$
H_D=\prod_{j=0}^{n}(n+j)!/j!,\qquad
 H_B=\prod_{j=0}^{n-1}(n+j)!/j!.
                                                               \tag{4}
$$


In particular, for every prime $p\mid2n$,


$$
\frac{V_n(1)}{[t^n]V_n}\in1+2n\mathbb Z_{(p)}.
                                                               \tag{5}
$$


This is a direct all-index arithmetic consequence, independent of a
Painlevé identification. It does not yet control the distinct actual
reduced denominator $q_n$.

## 7. A useful exact seed and the limitation of the Toda resemblance

The Appell property gives an additional elementary representation:


$$
D_n(x)=\operatorname{Wr}
   (a_n^{[n]},a_{n+1}^{[n]},\ldots,a_{2n}^{[n]}).
                                                               \tag{6}
$$


The final seed is explicitly


$$
P_n(x):=a_{2n}^{[n]}(x)
 =\sum_{k=0}^{n}\binom nk\frac{x^{2k}}{(2k)!}
 ={}_1F_2\left(-n;\frac12,1;-\frac{x^2}4\right).
                                                               \tag{7}
$$


This terminating identity follows by cancelling the Pochhammer
factors. Direct coefficient comparison, with no special-function
asymptotics, gives


$$
xP_n'''+2P_n''+xP_n'-2nP_n=0.                          \tag{8}
$$


Reversing the columns of (6),


$$
D_n=(-1)^{n(n+1)/2}
       \det(P_n^{(i+j)})_{i,j=0}^{n}.                  \tag{9}
$$


For each fixed background $n$, the determinants
$\tau_k^{[n]}=\det(P_n^{(i+j)})_{i,j=0}^{k-1}$
therefore satisfy the ordinary Sylvester identity


$$
\tau_k\tau_k''-(\tau_k')^2=\tau_{k+1}\tau_{k-1}.
                                                               \tag{10}
$$


It is an identity before division, so zeros do not invalidate it.
But $D_n$ lies on the diagonal $k=n+1$ while its background $n$
also changes. Equation (10) keeps the background fixed. It is not a
closed recurrence for $D_{n-1},D_n,D_{n+1}$.

The actual background shift is


$$
a_k^{[n+1]}=a_k^{[n]}+a_{k-2}^{[n]},
$$


which is a separate transformation. Any useful contiguous arithmetic
identity must combine this shift with (10), carry the hook factors
and any extra minors, and prove those extra factors are units or
quantitatively controlled. The formal Toda resemblance alone does
not do that.

## 8. Most useful next step and audit coverage

The strongest directly applicable arithmetic input found here is the
Appell integer-power-sum theorem, not a Painlevé discriminant formula.
The next concrete target is the corresponding augmented-Schur
description of the **actual endpoint numerator and denominator**
and their integral linear combinations. A successful description
could extend (4) to their normalized gcd. Alternatively, a complete
background-shift identity for (9), with controlled extra minors,
could provide a genuine neighboring-index resultant.

Downloaded primary PDFs and extracted text are in
literature_special_polynomial_mapping/. The 2026 full article was
also read from its publisher-deposited Europe PMC XML because the
ordinary PMC page intermittently returned a browser challenge.
This audit read the definitions, theorems and proof sections cited
above; it does not claim a line-by-line verification of every result
in these papers. No canonical-degree or prime scan was performed.
