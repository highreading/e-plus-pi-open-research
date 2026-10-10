> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent root review of the norm-resultant and height theorem

Date: 2026-09-13. Verdict: PASS without a required correction.

Reviewed `raw_accessory_norm_resultant_and_height.md` in full. This is a
structural identity and an explicit upper bound, not an improvement of
the best available bound for the original extremal content.

## Normalization and the factor at infinity

The previously reviewed finite algebra uses weights 1,2 on beta,gamma.
After gamma=y², the actual leading forms have degrees n=d+1 and n+1:
P_n(x,y²) and y²P_d(x,y²). The recurrence
P_r=xP_(r−1)+(r−1)y²P_(r−2) gives the binary resultant
Gamma_d=product_(k=1)^d k^k. The contribution of y² is one because
P_n(1,0)=1. In the univariate recurrence the sign on swapping consecutive
degrees is (−1)^(r(r−1))=1. This fixes the displayed positive factor.

It is nonzero over Q and has no prime factors above d. The affine
intersection algebra after the substitution is free of rank two over
the original algebra, even at gamma=0. The multiplication operator for
R0+tR1 therefore has squared norm, including all local multiplicities.
No separability assumption is needed for this assertion.

For the third homogeneous polynomial of degree 2n, the homogeneous
Poisson formula gives the factor Gamma_d^(2n). It can first be checked
on the generic simple affine intersection and extended while Gamma_d
is invertible; equivalently both sides are regular functions there.
Specializing the third polynomial to Z^(2n) fixes the multiplicative
constant and sign. Hence the exact identity

    T_d(t)=Gamma_d^(2n) N_d(t)²

is correct. Padding a lower-degree residue polynomial by homogenization
introduces no missing affine factor, because the first two forms have
no common point at infinity. The argument does not incorrectly apply a
torus-only assertion to a root on an axis.

## Integral clearing and coefficient content

For a rational polynomial U, its Gauss p-valuation is the minimum of
its coefficient valuations. Multiplicativity gives v_p(U²)=2v_p(U).
Thus U² integral implies U integral at every prime. Applying this to
U=Gamma_d^n N_d gives the claimed explicit integral clearer, and Gauss's
lemma gives content(T_d)=content(U)² exactly. The choice of clearer is
stated and does not introduce an uncontrolled multiplier in a height
claim. Its prime support is at most d, so the prior large-prime norm
comparison is preserved without changing any depth.

## Input norms and the specialized resultant inequality

I checked the downward pivot recurrence and the cofactor row-norm
argument against their explicit matrices. The bound H=32(d+1)³ is
conservative for the five coefficients of L^[1]z^m, 0≤m≤d. Ignoring
the helpful division by r in each downward step gives
sum ||b_r||₁≤(1+H)^d. The factor d! is retained in E0,E1.

The cofactor sum is bounded by (d+1)(4H)^d. The residue numerator's
coefficient norm costs at most 2d+(8d+4)=10d+4, including its derivative,
both accessory variables, and all constant terms. Reduction modulo
1+z² cannot increase the coefficient l1 norm. Thus the displayed H_E
and H_R bounds hold in the actual normalization.

I separately opened Sombra's primary paper,
[The height of the mixed sparse resultant](https://arxiv.org/pdf/math/0211449),
and checked Lemma 1.3 on printed page 2. For full degree simplexes the
lattice index is one; its partial degrees here are 2n(n+1), 2n² and
n(n+1). Specializing some coefficients to zero is permitted. Applying
the inequality for |t|=1 and then Cauchy's coefficient bound proves

    log c_d≤n(2n+1)log H_E+[n(n+1)/2]log H_R.

The factor one half comes from content(T_d)=c_d², not from an omitted
resultant degree. Since log H_E=4d log d+O(d) and log H_R=3d log d+O(d),
the resulting leading coefficient is 8+3/2=19/2, as stated.

## Comparison and actual limitation

In each original extremal matrix column the j! factor can be removed
without affecting primes above 3n. The exponential entries then have
size at most 2^(3n), and the arctangent entries at most
2^(3n)(3n)!, with exactly n columns in each group. Hadamard gives the
displayed (2n)^n 2^(6n²)((3n)!)^n bound. A nonzero maximal minor exists
by the already proved characteristic-zero rank theorem. Its
large-prime part dominates the corresponding content, proving
3n²log n+O(n²). The new resultant estimate is weaker in order.

Finally the note correctly keeps the full residue hypotheses on the
pole identity. Taking that identity's product over arbitrary
exponential accessory points would be invalid. No small-prime
factorization of the finite norm content, isolated-depth bound, or
primitive endpoint-error estimate has been established here.
