> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Centered imaginary zeros: a useful theorem and a transform obstruction

Date: 2026-09-13. Root mathematical and literature check.

The previously proved imaginary-root property of the Borel-Legendre
polynomials F_k implies that G_k(s)=F_k(s+1/2) is strictly Hurwitz
stable: every zero has real part−1/2. Writing

    G_k(s)=a_k(s²)+s b_k(s²),

the Hermite-Biehler theorem gives real interlacing for
Re G_k(it)=a_k(−t²) and Im G_k(it)=t b_k(−t²), after ignoring an
identically zero component in the smallest degree. Thus the nonconstant
a_k,b_k have negative real roots in their own polynomial variable.
A primary modern statement of the classical implication appears in
[Ellard and Šmigoc, 2017](https://arxiv.org/abs/1701.07912).

For this special vertical-line zero set, a direct argument avoids any
extra theorem hypotheses. Write the zeros of G_k as−1/2+i rho_j, with
rho_j real. Along the imaginary axis a continuous argument theta(t)
has derivative

    theta'(t)=sum_j (1/2)/[(t−rho_j)²+1/4]>0.

Its total increase is k pi. The alternating crossings of real and
imaginary axes are therefore simple and interlace; counting their
number against the polynomial degrees gives all the required roots.
This also handles possible repeated zeros off the imaginary axis.

However, these centered polynomials are not the spectral branch
polynomials r_k(xi). Passing through the module f(T)1 changes the
variable by a nontrivial triangular transform. Imaginary roots and
Hermite-Biehler interlacing alone cannot justify preservation of
negative roots under that transform.

Here is an exact counterexample to that general implication. Take

    F(x)=x²+epsilon²,  0<epsilon²<1/2.

It has two simple imaginary roots. Its centered even part is
s²+1/4+epsilon². With s=x−1/2, our operator satisfies

    T1=s²+3/4.

Therefore that centered even polynomial equals

    (T−1/2+epsilon²)1.

Its spectral module polynomial xi−1/2+epsilon² has the positive root
1/2−epsilon². For a completely rational example choose epsilon=1/2,
which gives the positive root1/4. This is not an actual higher F_k
counterexample; it disproves only a proposed inference from the
imaginary-root and centering hypotheses alone.

The already proved nonnegative coefficients in xi−1 for the actual
branches remain valid by their separate recurrence proof. The closed
actual negative-root observations through k12 remain evidence, and
would need an additional family-specific argument to become a theorem.
