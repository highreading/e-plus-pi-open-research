> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# One extra column: analytic nonvanishing of the evaluation border

Author: Agent 3, 2026-10-02. This is the narrowly authorized analytic extension of SHORT_RECTANGULAR_COMPLETE_SIGNED_ERROR.md. Root reserves M25's integer lattice, actual final gcd, coefficient-height cost, and realizability algebra. Those questions are not re-derived here.

## Fresh gate and classical overlap

Fresh archive query in work/ and sources/, Markdown only:

```
border.{0,60}(derangement|rho|paired|eval)|eval.{0,50}rank.2.{0,50}(kernel|coefficient)|width.{0,20}2k.{0,40}paired
```

It found unrelated bordered Cauchy/endpoint determinants, no completion of this exact odd-width paired border. No global novelty follows from this bounded search.

Fresh primary query: `site:arxiv.org moment determinant evaluation row Christoffel Uvarov determinant identity`. Opened full primary Krattenthaler, *A determinant identity for moments of orthogonal polynomials that implies Uvarov's formula for the orthogonal polynomials of rationally related densities*, https://arxiv.org/pdf/2103.03969. Moment/characteristic-product and evaluation determinant identities are classical overlap. The present claim is uniform nonvanishing after the actual exterior atom is cancelled in this particular mixed measure; it is proved directly below.

## Exact actual bordered determinant

Use the same rho=mu-delta_{-1} and COMPLETE sigma measure as in the preceding theorem. Now take columns j=0,...,2k. The upper k rows are C_ij=rho(y^(i+j)), the next k rows are R_ij, and the last row is ell_j=(-1)^j. Set

    E_k=det[C;R;ell].

Adding the actual S V term to the middle block leaves E_k unchanged, because row i of S V is S(-1)^i ell. Adding e times each upper row also leaves the determinant unchanged. Entrywise the complete sigma moment block is L=eC+R+S V, so E_k is rational and EXACTLY equals det[C;L;ell] with L_ij=sigma(y^(i+j)). No exponential/arctangent endpoint is dropped.

Repeated Andreief and the last evaluation give

    E_k=(-1)^k/k! integral_[0,1]^k Vandermonde(x)^2 product_i(1+x_i)
          det M_[mu·(y+1)product_i(y-x_i),k] d sigma^k.           (1)

Indeed the two k-node Vandermondes produce (-1)^(k^2) from the cross product, while the fixed final node -1 gives product_a(-1-t_a)product_i(-1-x_i). Their 2k minus signs cancel. The factor y+1 kills the upper rho atom, leaving mu exactly. This is distinct from the M24 S-cofactor: there are k compact nodes here and a degree k+1 modifier.

## Uniform positivity from the existing coercivity constant

For any x_i in [0,1], put W_x(y)=(y+1)product_(i=1)^k(y-x_i). On the SAME tail I=[k^2,4k^2],

    W_x(y)>=(k^2+1)(k^2-1)^k.

On [0,1], |W_x|<=2; on y>1 its sign is positive, and there is no exterior atom. With the EXACT C_k from the preceding theorem,

    C_k=3exp(-2k-1)(k^2-1)^(k-1)/[4k16^(k-1)]>2^k  (k>=24),

the Legendre test estimate gives, for every nonzero deg p<k,

    integral W_x(y)p(y)^2dmu(y)
       >=[(k^2+1)(k^2-1)C_k-2]
            max(|p(-1)|^2,sup_[0,1]|p|^2)>0.                    (2)

Thus every modified k by k moment determinant in (1) is strictly positive, uniformly over all the compact nodes. Sigma's density is positive, the Vandermonde is nonzero on a set of positive measure, and product_i(1+x_i)>0. Therefore

    sign E_k=(-1)^k,    E_k!=0,    EVERY k>=24.                 (3)

This completes the analytic nonzero interface needed for Root's rank-two coefficient map in the width 2k+1 construction. Applying its exact algebra and integer-lattice consequences remains Root's work. In particular the sign/nonzero theorem alone gives no small coefficient height, favorable final denominator, or small primitive complete form, and no rationality conclusion.
