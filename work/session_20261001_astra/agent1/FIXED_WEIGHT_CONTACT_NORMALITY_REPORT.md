> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fixed-weight contact-normality report

2026-10-01. New author proof; no independent-review claim and no numerical evidence used.

The actual square system with caps (n,b-1,n-1) and contact M=2n+b+1 is proved nonsingular for

    n >= ceil(exp(32)),   1 <= b <= floor(log n).

The proof does not assume the provisional balanced normality theorem and does not use Christoffel Gram norms as contact positivity.

The actual n+1-derivative transform is

    Q^(n+1) D^(n+1)(CF)=Q U'-n Q'U,
    U=Q^n D^n(CF), deg U<n.

Its image has dimension n inside polynomials of degree at most n. Its exact missing condition is

    Res_(1+i) P/Q^(n+1)=0.

The other pole 1-i has the opposite residue, so it too is retained. This is a codimension-one image, not the balanced degree-<n image.

After deriving that actual transform, keeping the final polynomial coefficient for an intermediate n-derivative step produces the equivalent exact border

    D_(n,b)=det [ [z^(n+r-j)]exp(z)Q(z)^n | [z^(n+r)]Q(z)^n ],
                r=0,...,b; j=0,...,b-1.

The last column, or the last row after transposition, is exceptional. Its contour representation contains the divided difference exp(-z)[z_1,...,z_(b+1)]. The simplex formula rewrites it as (-1)^b/b! times an average of exp(-sum t_j z_j). This is the new border-specific argument: near z=-sqrt(2), the resulting exponential has a uniformly small phase and nonzero real part.

A direct comparison of a separated local rectangle with the entire complementary domain proves

    sign D_(n,b)=(-1)^(n(b+1)+b).

Writing d=b+1, an explicit lower bound is

    |D_(n,b)| >= (1+sqrt(2))^(nd) exp(-2d)
       /[d! b! 2^(d^2+4d+2) d^(d^2) n^(d^2/2)] >0.

The cutoff is conservative and entirely deductive. No finite-degree scan or repeated symbolic control was used.

The endpoint consequence covers the full unselected allocation (n+1,b,n), rather than the stopped balanced-restoring selector. Its contact space maps isomorphically to Q^3 by (A(1),B(1),C(1)): a zero endpoint triple would be divisible by z-1 and contradict square normality. After matching B(1)=C(1), the space maps isomorphically to Q^2 by (X,Y). Every rational endpoint pair therefore has a unique matched solution.

This is full endpoint rank, not a coefficient-height or approximation theorem. It does not classify which individual endpoint directions have a nonzero highest A coefficient, and it does not invoke provisional balanced results to characterize the balanced-selector slice. Useful primitive normalization, controlled nonbalanced selection, companion conditioning and complete-remainder nonvanishing remain separate tasks. No shrinking or irrationality conclusion is claimed.

Full proof: work/session_20261001_astra/agent1/FIXED_WEIGHT_CONTACT_NORMALITY.md.

The next quantitative target is an inverse or endpoint-minor estimate adapted to the same simplex border, with the actual final endpoint gcd retained.
