> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Shifted fixed-dimension recurrence compression

Author target, 2026-10-02. Root assigned this distinct continuation after the M22 content checkpoint. Root retains M24's shorter right-family full-kernel wedge construction; no kernel basis is selected here. Root's M23 complete fixed-k positive error and analysis's growing-dimensional coercivity remain their original work.

## Fresh archive and primary gate

Archive queries covered shifted derangement recurrences, D_(2M) compression, cofactor polynomials and large-M primitive content. The hits were root's `main/SHIFTED_PAIRED_FIXED_DIMENSION_POSITIVE_ERROR.md`, arithmetic's different exact-dyadic weighted-Gram target, and analysis's growing-shift gate. No evaluated common-content theorem for the compressed fixed-k pair was found. The unshifted moment interface and our M22 complete carry formulas are prior authored overlap.

Fresh online queries were `derangements arithmetic Hankel determinant shifted moments recurrence content` and `site:arxiv.org derangements p-adic incomplete gamma arithmetic factorial gcd`. Opened Miska, *Arithmetic properties of the sequence of derangements and its generalizations*, https://arxiv.org/pdf/1508.01987, including Section4.3's multi-step recurrence polynomials and Section6.1's factorial comparison. Also opened current O'Desky–Richman https://arxiv.org/html/2012.04615v4. The scalar derangement recurrence and its iterated polynomial form are established prior work. The new boundary is their exact substitution into the FULL primitive weighted coefficient pair, including all specialization gcds; no scalar recurrence novelty is claimed.

## Scalar compression

Set X=2M for even M, d=D_X and f=X!. Define integer polynomials

    P_j(X)=product_(a=1)^j(X+a),
    Q_0=0, Q_(j+1)=(X+j+1)Q_j+(−1)^(j+1).

Then EXACTLY

    D_(X+j)=P_j(X)d+Q_j(X),
    (X+j)!=P_j(X)f.

For even j=2r, this supplies every shifted derangement/factorial moment required by a fixed k. Let l=L_M, the rational arctangent remainder in beta_M, and define

    h_r(X)=4 sum_(a=0)^(r−1)(−1)^(r−1−a)/(X+2a+1).

The complete rational moment is

    beta_(M+r)=−P_(2r)(X)f+(−1)^r l+h_r(X).

All new denominators in h_r are among the fixed number of consecutive odd integers X+1,...,X+4n−3. The old l has its actual odd denominator, not an assumed odd-lcm equality.

The orthogonality matrix has entries

    rho_(M+r)=P_(2r)(X)d+Q_(2r)(X)−(−1)^r.

Its signed n-by-n cofactors give an integer polynomial vector in(X,d), of degree at most n in d. A polynomial gcd of this vector, a numerical gcd after(X,d) specialization, and the eventual determinant-pair gcd are three distinct arithmetic quantities. None may replace the others.

## Current goal

Derive the exact coefficient pair in(f,d,l) and count the complete specialization content. Generic polynomial common factors can be removed by a symbolic identity; extra numerical content needs an evaluated gcd theorem. The scalar compression by itself does not lower an ACTUAL denominator.
