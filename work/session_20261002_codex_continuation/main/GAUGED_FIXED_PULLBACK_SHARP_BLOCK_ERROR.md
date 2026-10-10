> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete exponential-gauged error and sharp blocks on every fixed progression

Root original application,2026-10-02. Author theorem; main research ACTIVE.

## Target and overlap boundary

The target is the complete normalized center c_N=(1+V_N)/E_N from M11 for ONE fixed rational polynomial P. Earlier archive pullbacks already locate genuine logarithmic singularities, and M11 already proves an upper error bound and an exact nonzero three-even-index block. Those are retained as prior results. The new statement specifies the signed leading coefficients of the complete center, proves their noncancellation on every fixed arithmetic progression, and supplies a sharp error magnitude within a bounded progression block. Generic singularity transfer and Vandermonde elimination are established methods, not claimed new.

Before this target, archive searches/readings covered the high-radius pullback, mixed extension/tensor gauge, and weighted-difference block files. No complete theorem for this normalized endpoint center and all fixed progressions was found. Fresh primary searches and reads: Flajolet and Odlyzko, Singularity Analysis of Generating Functions (1990), https://algo.inria.fr/flajolet/Publications/FlOd90b.pdf , especially its multiple-dominant-singularity discussion and logarithmic transfers; Popescu, A simple and self-contained proof for the Lindemann-Weierstrass theorem, https://arxiv.org/html/2306.14352v2 , Theorem3.2; and the original new p-adic proof https://annals.math.princeton.edu/1989/129-1/p05 . The proof below also gives a direct finite-log convolution argument instead of assuming a transfer theorem with unchecked continuation hypotheses.

## Assumptions and exact logarithmic decomposition

Let P in Q[z] be nonconstant with P(0)=0,P(1)=1. Set G(z)=4 arctan(P(z)/(2-P(z))) on its origin germ, and assume its nearest singularity radius R0 is greater than1. Write Lambda_plus for the DISTINCT roots of P-(1+i), Lambda_minus for those of P-(1-i), retaining root multiplicities m_lambda. Define

    L_lambda=-2i m_lambda on Lambda_plus,
    L_lambda=+2i m_lambda on Lambda_minus.

No root is0 or1, and the two root sets are disjoint. Factoring the two polynomials gives the exact origin germ

    G(z)=sum_lambda L_lambda log(1-z/lambda).

Indeed the derivative is4P'/((P-1)^2+1), and both sides vanish at0. Every root remains a genuine logarithmic singularity even if its multiplicity exceeds1. Consequently R0=min|lambda|.

For H(z)=exp(-z)G(z), put u_n=H^(n)(0), E_N=sum_0^N(-1)^n/n!, V_N=sum_0^N u_n/n!, c_N=(1+V_N)/E_N, S=e+pi. All e endpoint terms are included. Exactly,

    c_N-S=(S T_E(N)-T_H(N))/E_N,

where T_E and T_H are the tails of exp(-z) and H evaluated at1. The exp(-z) tail is factorially small; it is not silently dropped before normalization.

## Full two-term signed error

Set A_lambda=L_lambda exp(1-lambda)/(lambda-1), which is nonzero. Then

    c_N-S = (1/N) sum_lambda A_lambda lambda^(-N)
             -(1/N^2) sum_lambda A_lambda lambda^2/(lambda-1) lambda^(-N)
             +O(R0^(-N)/N^3).                         (1)

The implicit constant depends on the fixed P. Keeping only roots on |lambda|=R0 changes the first-order expression by an exponentially smaller term.

A direct proof starts from the EXACT coefficient identity

    [z^n]exp(-z)L log(1-z/lambda)
       =-L lambda^(-n)/n sum_(k=0)^(n-1) (-lambda)^k/k! * n/(n-k).

For k<=n/2 expand n/(n-k); the weighted exponential sums are exp(-lambda),-lambda exp(-lambda), and(lambda^2-lambda)exp(-lambda). The k>n/2 part is factorially small, uniformly for each of finitely many fixed roots. Thus the coefficient equals

    -L exp(-lambda) lambda^(-n)/n [1-lambda/n+O(n^-2)].

Summing n>N geometrically gives the terms sum_(s>=1)lambda^(-s)=1/(lambda-1) and sum s lambda^(-s)=lambda/(lambda-1)^2. Dividing the negative H tail by E_N gives(1), while S T_E/E_N remains factorially small. This derivation includes every logarithmic branch and the full exponential endpoint.

## Every fixed arithmetic progression retains the sharp radius

Fix h>=1 and a residue r mod h. Let Lambda0 contain the roots with modulus R0 and group them by equality of lambda^h. For a group C define

    C_(r,C)=sum_(lambda in C) A_lambda lambda^(-r).

Each coefficient is NONZERO. After removing the common factor exp(1), it is a linear combination of exp(-lambda) at distinct algebraic lambda, with nonzero algebraic coefficients L_lambda lambda^(-r)/(lambda-1). Lindemann-Weierstrass rules out its vanishing. This use of the theorem concerns exponentials at algebraic singularity locations; it assumes nothing about the rationality of e+pi.

Let K be the number of such groups. The K distinct phases beta_C=R0^h/lambda^h have modulus1. For N=r+hm, the K errors at N,N+h,...,N+(K-1)h, after multiplying each by its own order and R0 to that order, equal a fixed invertible Vandermonde matrix applied to the vector R0^r C_(r,C) beta_C^m, up to O(1/N). That vector has a fixed positive norm for every m. Consequently constants c,C>0 and N0 exist such that every N>=N0 on this progression has

    c R0^(-N)/N <= max_(0<=j<K)|c_(N+jh)-S|
                       <= C R0^(-N)/N.               (2)

In particular the complete error has exponential rate log R0 in a bounded block of every fixed progression, including the even progression. One may always use K<=2 deg P. This is a magnitude statement stronger than bare block nonvanishing, though its block can be longer than M11's exact three-even-index selector.

## Actual primitive denominator interface and limitations

If P has integral derivative jets, B_N,D_N are the actual integer endpoint arrays from M11 and q_N=|D_N|/gcd(D_N,B_N). If a theorem supplies q_(N+jh)>=exp(sigma(N+jh)) at EVERY member of the fixed block, for some sigma>log R0, then(2) forces at least one primitive form in each block to grow exponentially. Conversely a uniform upper bound q_N<=exp(sigma N), sigma<log R0, paired with M11 nonvanishing would prove irrationality. Neither such global gcd-rate estimate is proved here.

The sharp block lower bound is NOT an every-index lower bound, and does not rule out an arbitrarily sparse subsequence with unusually small oscillating errors. The constants depend on one fixed P; they are not uniform under independently varying P_N. No main rationality decision or global exclusion of the gauged family follows.

## New finite receipt

GAUGED_SHARP_ERROR_PROFILE.json verifies exact endpoint identities at all orders1..360 for P=z and P=z-z^2/2+z^3/2. It separately stores numerical root/asymptotic profiles. The first residual scales as R0^-N/N^2 and the second as R0^-N/N^3 in these diagnostics. Those finite profiles test the newly derived normalization and signs; they are not the proof of(1) or(2), which is the all-order argument above.
