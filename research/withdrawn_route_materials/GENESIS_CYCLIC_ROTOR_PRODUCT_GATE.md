> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Cyclic rotor products: exact cancellation and failed arithmetic transfer

Agent 2 original bounded candidate test, 2026-10-03. Status: DISCARDED at the essential-mechanism gate. This is a nonadditive operation applied to the actual normalized rotor, not a new Padé, determinant, or selector family. The elementary specialization below is recorded to prevent a false arithmetic-norm inference; no essential novelty or rationality decision is claimed.

## 1. Candidate and scalar input

For q in Q put

    K_q(z)=exp(i[(q-1)z-exp(z)+1]).

As in G5, K_q(0)=1, its Taylor coefficients lie in Q(i), and the actual fixed exponential and circle laws give the exact input

    S=e+pi=q  implies  K_q(1)=-1.

The candidate operation is a cyclic product over fractional imaginary-period shifts. For n>=2 set delta_j=2pi i j/n and

    C_n[K](z)=product_(j=0)^(n-1) K(z+delta_j).

Its intended contradiction mechanism was to cancel the nested exponential globally, then transfer the algebraic input K_q(1)=-1 to an arithmetic orbit product. That transfer is a theorem target, not an assumed implication. The exact calculation below shows that the natural product is instead transcendental for every rational q.

## 2. Archive and primary-literature gate

Archive queries covered roots of unity, cyclic norms, cyclic products, root-of-unity filters and lacunary series. Opened `sources/nested_multi_exponential_hp_norm_barrier.md`, Sections 1–2 and its scope statement: it already distinguishes coefficient-field conjugate products and root-of-unity projections from actual number-field norms of evaluated transcendental values. Other hits included the archived quartic roots-of-unity filters and constrained exponential/logarithmic endpoint families; none is reopened here.

Fresh online queries used cyclic products of entire functions, product f(z)f(omega z), exponential root-of-unity filters, finite-group norms, and pseudo-hyperbolic functions. Opened full primary Dattoli–Sabia–Del Franco, *The Pseudo-Hyperbolic Functions and the Matrix Representation of Eisenstein Complex Numbers*, https://arxiv.org/pdf/1003.2698, especially its exponential cyclic matrix and determinant/trace identity in Section 1, equations (8)–(10). That identity is exactly the product-of-exponential-eigenvalues cancellation used here. Opened the related primary Dattoli–Migliorati–Ricci paper https://arxiv.org/pdf/1010.1676 and the full primary Stetkaer complex finite-group mean paper https://www.researchgate.net/publication/225491677_Functional_equations_involving_means_of_functions_on_the_complex_plane, its Introduction and Section 4. Also opened the authored Wilf textbook from https://www.math.cmu.edu/~af1p/Teaching/Combinatorics/Slides/Notes/gfology.pdf as background for the classical Fourier/root-of-unity projection. The attempted Penn copy failed and is not counted as a read.

The essential operation is public finite-group trace/norm cancellation, not a new law-coupled invariant. Hence the candidate is discarded. The following bounded calculation prices the actual evaluated product and identifies the missing arithmetic transfer precisely; it does not continue a known norm-approximation route.

## 3. Exact global product

For every complex z, every complex q and every integer n>=2,

    C_n[K_q](z)
      =exp(i n[(q-1)z+1] - pi(q-1)(n-1)).

Proof: exp(z+delta_j)=exp(z) zeta_n^j, whose sum over j is zero. Also sum_j delta_j=pi i(n-1). Addition of the displayed entire exponents therefore gives the formula with no branch choice. In particular,

    C_n[K_q](1)=exp(i n q - pi(q-1)(n-1)).

The nested exponential has disappeared exactly, but the fractional-period shifts introduce a full real exponential factor. It cannot be silently omitted.

## 4. Complete arithmetic value of the product

For EVERY rational q and EVERY n>=2, the actual number C_n[K_q](1) is transcendental.

For q!=1 its modulus is exp(-pi r), where r=(q-1)(n-1) is a nonzero rational. By the classical Gelfond–Schneider theorem, the value of (-1)^(i r) obtained using log(-1)=i pi is exp(-pi r) and is transcendental: the base -1 is algebraic and different from 0,1, and i r is algebraic irrational. If C_n[K_q](1) were algebraic, its modulus would be algebraic, since its product with its complex conjugate and the positive square root are algebraic. This is a contradiction.

For q=1 the product is exp(i n), transcendental by the classical Lindemann theorem, since i n is nonzero algebraic. These two cases cover all rational q. Under the specific scalar hypothesis q=S, q>1, so the first case applies directly.

Thus even the EXACT global removal of the nested exponential does not yield an algebraic integer or a number-field norm. One known algebraic factor K_q(1)=-1 supplies no algebraicity of the remaining shifted values, and the complete product proves they cannot all be algebraic under that hypothesis. No assertion about their individual transcendence is required.

## 5. The gauge that removes the extra factor loses the arithmetic input

Define

    P_q(z)=exp(-i[(q-1)z+1]) K_q(z)=exp(-i exp(z)).

Its cyclic product is exactly 1 for every z and n>=2. This is the classical trace-zero exponential norm identity in the coordinate w=exp(z): product_j exp(-i zeta_n^j w)=1.

However at the input point, CONDITIONAL ON S=q in Q,

    P_q(1)=-exp(-i q),

which is transcendental by Lindemann (q=S is nonzero). Hence this gauge is not an arithmetic-preserving normalization of the algebraic endpoint K_q(1)=-1. The identity product=1 does not imply any factor is algebraic; it is a functional norm identity, and evaluation at w=e is not a number-field specialization.

The alternatives are now exact: retain K_q and its evaluated cyclic product is transcendental, or take the gauge with product 1 and its endpoint input is already transcendental under the rational-sum hypothesis. This is a scoped failure of the candidate's natural transfer step, not an impossibility theorem for an unknown operation. Survivor count remains zero; no cyclic-product variant is pursued.
