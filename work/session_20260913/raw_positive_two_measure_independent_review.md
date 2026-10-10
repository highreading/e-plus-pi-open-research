> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the finite positive two-measure reduction

Date: 2026-09-13. Reviewer: audit_results.
Source: raw_positive_two_measure_reduction.md, Sections1–5.

**Verdict:** the exact finite polynomial representation, positive
measures, degree caps, spectral identities, and scalar orthogonal
polynomial formulas pass. One normalization wording correction was
reported to root: the symmetric E_k basis carries a varying row radical,
not only the fixed seed factor sqrt3. Dividing each equation by its
known common row factor restores the original rational high-row ledger.
No analytic conclusion or zero constraint is changed by this correction.
Root has now incorporated the explicit row factor and the corrected
rationality statement in Section3 of the source note.

## 1. Finite representation and all power domains

The potential in T has leading term x² while its differential part
preserves polynomial degree. Thus T raises each nonzero polynomial's
degree by exactly2 and preserves its leading coefficient. The vectors

    T^j1,       T^j sqrt3(x-1/2)

in the displayed ranges have respectively all even and odd leading
degrees up to n. Their distinct leading degrees prove linear
independence, and their count n+1 proves completeness in the polynomial
space. The exact caps floor(n/2) and floor((n-1)/2) follow, including
the absent odd branch at n=0.

Reflection separates the two branches. The seeds and every iterate
are polynomials in the previously specified self-adjoint domain,
so they lie in the domains of all required powers. The coefficient
formula <P,psi_l>=g_l f_(l mod2)(xi_l) therefore follows from the
spectral theorem applied to a finite polynomial in T. No spectral
indices have been truncated.

## 2. Masses, moments, and exact norm

The odd seed equals phi_1/2, so its squared norm is1/4, while the even
seed equals phi_0 and has squared norm1. Parseval gives the two measure
masses exactly. The already proved nonzero amplitudes and disjoint
simple spectral intervals give positive atoms and infinite support.

Every polynomial moment is finite because each seed lies in all power
domains. Its value is <v_sigma,T^j v_sigma>. The T coefficients and
the even seed are rational, while the two odd seed factors sqrt3
multiply to3. Ordinary polynomial integration therefore makes all
these moments rational. This assertion is correct independently of
the later normalization of the E_k test polynomials.

The two seed spectral supports have opposite reflection parity.
Applying Parseval to the exact finite representation gives equation(5)
with no cross term and with no omitted high spectral tail.

## 3. Actual high rows and the row-radical correction

The initial E_0,E_1 identities and the nonzero forward coefficient
in the order-four recurrence prove the polynomial identity(6).
The uniqueness of the degree-bounded representation gives the stated
degree caps; the component matching k's reflection parity has full
leading degree. Applying the exact isometry proves(7).

However, multiplying the explicit row normalization factors gives

    a_1...a_k
       =2^k(k!)^3/[(2k)! sqrt(2k+1)],
    E_k=r_k F_k,
    r_k=2^(-k) binom(2k,k) sqrt(2k+1).

Therefore p_k^(sigma) generally includes the varying radical
sqrt(2k+1) as well as the seed factor. The statement that the test
branch equations involve only fixed sqrt3 factors requires this
common row factor to be divided out.

Specifically, q_k^(sigma)=p_k^(sigma)/r_k is the decomposition of the
original rational polynomial F_k. Its even coefficients are rational;
its odd coefficients lie in (1/sqrt3)Q. The high equation with p_k
is exactly r_k times the one with q_k, and r_k is nonzero. Thus using
q_k makes the rational normalization claim precise without changing
the nullspace, the positive norm representation, or the recurrence's
mathematical content. Root was notified before this review was saved.

## 4. Scalar orthogonal polynomials and every normalization factor

The parity block of the actual Legendre representation has diagonal
d_(sigma+2j) and adjacent coefficient b_(sigma+2j)=t_(sigma+2j)t_(sigma+2j+1).
Starting at v_sigma=h_sigma phi_sigma, with h_0=1 and h_1=1/2, the
standard monic recurrence is exactly(8).

I verified(9) directly by induction. Applying T-d_(sigma+2j) to its
right side gives an upper and a lower Legendre mode. The lower mode
has coefficient b_(sigma+2j-2)² times the previous right side and
is canceled by the recurrence's second term. The surviving upper
mode gains precisely b_(sigma+2j). The base j=0 and j=1 retain the
factor h_sigma, including the odd normalization1/2.

The images of these scalar polynomials under f(T)v_sigma are distinct
orthogonal Legendre modes. The spectral isometry therefore proves
their orthogonality and the norm product(10) exactly. The odd mass
1/4 is retained as h_1²; no probability-measure rescaling has been
silently applied. Since d_l and b_l² are rational, the scalar monic
recurrence and its norm products are rational as expected.

The argument constructs the actual two scalar measures and their
orthogonal polynomials. It does not invoke or require determinacy of
an abstract moment problem. It also does not assert that the different
mixed p_k branches are scalar orthogonal polynomials. The source's
final distinction between positive scalar moment structure and the
unresolved mixed high-row conditioning is correct.
