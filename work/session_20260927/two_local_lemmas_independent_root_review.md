> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent root review of two local arithmetic lemmas

Date: 2026-09-27. Reviewer: root. Status: FULL PASS within the scopes below.

## 1. Adjacent b=2 contents

Reviewed `hp_b2_adjacent_content_coprimality.md` against the previously
independently accepted cubic gate. Substitution of
w=2(n+1)/z-2-(n-1)z into the displayed state matrix gives each of the
three displayed transported coordinates. Substitution into the next
quadratic obstruction gives the polynomial F with the sign -g as stated.
The displayed integral Bezout identity has constant -8(n+1)^2(n+2).
Thus its constant, 2, and z are all units for p>2n+6. This proves the
claimed impossibility of simultaneous positive valuations, with exactly
the stated cutoff for the two actual endpoint consequences.

For all-index nonvanishing, the primitive state and preceding minor
argument over Q indeed force h and u nonzero if all minors vanish.
The rational-root argument is legitimate because f is monic. Its
rearrangement yields n=2-z+(8-6z)/(z^2-2); the denominator is nonzero
for integer z. Multiplication by 8+6z gives the necessary divisibility
z^2-2 | 8. Enumerating these divisors gives precisely z=0,+/-1,+/-2,
and substitution gives the listed n values. At the sole nonnegative
candidate n=14, the proved differentiated coefficient congruence at 7
gives (h,u)=(1,0) mod7, inconsistent with u=-2h. This closes the
argument without any numerical approximant or prime factorization.

The proof does not bound isolated cancellation depths. In particular,
pairwise disjoint large-prime support is not a bound on the size of
either content. No denominator or main irrationality conclusion follows.

## 2. Odd-prime analytic interpolation and compactness certificate

Reviewed Sections 3--5 of
`literature_update_and_b2_analytic_certificate.md`. The multinomial
expansion yields exactly (X)_(b+2c+r)(X)_(b+c)/(2^c b!c!), including
the vanishing convention when the differentiation order is too large.
On X=a+pY each block of p falling-factorial factors supplies one
factor of p coefficientwise. With R=b+2c, s=b+c, k=floor(R/p),
q=floor(s/p), the denominator satisfies
v_p(b!c!)<=v_p(s!)=q+v_p(q!). Hence the displayed Gauss lower bound
k-v_p(k!) is valid, tends to infinity for every odd p, and proves
restricted analytic convergence. The proposed cutoff R>=p*K_d is
valid because k-v_p(k!)>=k(p-2)/(p-1)>=d. It is conservative, not
claimed optimal.

The four derivative combinations are exactly the product derivatives
of x^n H_n(x) at x=1 of orders zero through three. Index shifts preserve
the same coefficientwise estimates. Their finite sums and products
therefore compute the actual minors to the asserted precision.

The equivalence of absence of a common zero, bounded minimum valuation,
and a finite residue certificate follows from continuity, compactness
of Z_p, and preservation of congruences by integral restricted series.
No zero/nonzero result is inferred merely from the existence of the
criterion. For a common zero the finite search need not terminate.

This PASS covers the mathematical interpolation and certificate only;
it is not an independent complete bibliographic verification of Section 2.
The original note correctly retains the crucial limitation: a fixed
prime is outside the established large-prime endpoint-gcd range for
all sufficiently large n. Uniformity in growing primes and control of
the actual reduced numerator remain unresolved.
