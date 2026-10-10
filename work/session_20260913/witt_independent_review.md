> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the first-Witt recurrence, actual rank and support estimate

2026-09-13. Reviewed the new period operator, contiguity, exterior limit, actual rank and density notes against work-only Item426 and canonical Item194. Independently expanded both differential certificates, recomputed the degree23 rank determinant, reconstructed an actual characteristic-p correction, and checked the uniform summation.

**Verdict:** the revised projected-coordinate argument is sound. The first draft's homogeneous identities for the raw zero-constant primitives were false because of an x^p integration ambiguity. This review identified that gap. The exact Item194 endpoint kernel kills the ambiguity, so the corrected projected recurrence and contiguity are valid. The new determinant supplies the actual nonzero exterior-state bound. Together with the previously reviewed progression theorem, these establish the stated zero dyadic average for the first-Witt radical support, including j=0. No unbounded valuation estimate or irrationality proof follows.

Main reviewed notes:

- `witt_exterior_recurrence_attempt.md`
- `witt_actual_exterior_rank.md`
- `witt_roth_density.md`

Independent reproducible checks are in `witt_independent_checks.py` and `witt_independent_checks.json`.

## 1. Differential identities and the integration correction

For the order-three operator, the highest coefficient in the primitive operator applied to A of degree d is `(34+3nu-d)lc(A)`. At d=34+3nu it vanishes. The displayed number of equations and unknowns is correct. On an actual row with r>=18 the derivative primitive

    F=A u^(r-17)Q^(2s-nu+1)

has degree at most p. If all recurrence coefficients vanish, F'=0. Since F vanishes at both0 and1, the characteristic-p expression `F=ax^p+b` forces a=b=0. This correctly excludes a derivative-only kernel.

However, for a nonzero recurrence the same degree bound only proves

    F=sum_k c_k T_nu(r-6k)+beta x^p,

where beta is the x^p coefficient of F. The raw zero-constant primitives have degree below p; they cannot absorb this term. At the four endpoints where F vanishes,

    sum_k c_k T_nu(r-6k;zeta)=-beta zeta^p.

The contiguity identity has precisely the same issue, with primitive `A u^(r-11)Q^(2s)` of degree at most p. Its corrected endpoint relation is

    T_1(r;zeta)-sum_k a_k T_0(r-6k;zeta)=-beta zeta^p.

The stored leading A coefficients are nonzero rational functions, so this ambiguity cannot be dismissed just by inspecting the symbolic degrees.

I expanded the complete stored A and c coefficients for both nu=0 and nu=1 and verified that every coefficient of the differential identity is zero in Q[r,x]. I also verified the entire rational contiguity identity. These are coefficient identities, not evaluations at sample r.

As a concrete independent check of the correction, at p=59,s=1,r=25,j=0, direct finite-field primitives give the following raw residuals at zeta=1:

| Identity | Raw residual | beta | Projected (R,L) residual |
|---|---:|---:|---:|
| nu=0 recurrence | 21 | 38 | (0,0) |
| nu=1 recurrence | 57 | 2 | (0,0) |
| contiguity | 49 | 10 | (0,0) |

Each raw residual equals -beta modulo59 and is nonzero. Thus the original homogeneous raw-period statement was concretely false, while the corrected projected statement survives.

## 2. Why the complete endpoint map kills the correction

On fourth roots of unity, D_j has one value at1 and the same value at the other three points, so `D_j(zeta)=D_j(zeta^p)`. The Frobenius endpoint vector `T(zeta)=zeta^p` corresponds under the invertible evaluation transform to

    G_j=xD_j+uQ
       =(3j+2)x-(5j+2)(x^2+x^3+x^4).

This also follows directly from `uQ=x-x^5`. With `F_j=u^(3j+1)/Q^(2j+1)`,

    u^(3j)G_j/Q^(2j+2)=xF_j'+F_j=(xF_j)'.

The primitive xF_j vanishes at both0 and1, and its differential has zero finite residues. Therefore all three endpoint coordinates R,L,E kill G_j. This argument is exact in characteristic p under the ordinary pole-order bounds. It proves the projected homogeneous recurrence and projected contiguity without changing or discarding the raw Frobenius term.

The correction in the revised note is sufficient; the recurrence and contiguity coefficients do not need to be recomputed.

## 3. Actual evaluation rank, including the p-th-power term

The rank proof correctly begins with a putative relation

    W=c_0T(r)+c_1T(r-6)+c_2T(r-12)-delta x^p

that vanishes at the four roots. Here W(0)=0 and deg W<=p. Its derivative has factors `u^(r-12)Q^(2s)`. Local Taylor coefficients through the required orders can be recovered by dividing only by integers less than p. Hence the endpoint zeros imply

    u^(r-11)Q^(2s+1) divides W.

The divisor has degree p-22, so W has the form `A u^(r-11)Q^(2s+1)` with deg A<=22. Differentiation gives precisely the displayed26 by26 coefficient system. This converse divisibility argument is not affected by a possible local p-th-power term, which has higher order than all of the required local vanishing orders.

I independently reconstructed this matrix using the expanded operator stencil. For A=x^h, its five coefficients in degrees h through h+4 are

    3r-33+3h, 33-5r, 33-5r, 33-5r, 66-3h.

The last coefficient vanishes at h=22. The final three columns come from `-3u^12,-3u^6Q^4,-3Q^8`. The independently constructed matrix equals the saved matrix coefficient by coefficient. Recomputing its determinant over Z[r] gives exactly the saved factorization and degree23.

For r>=12, every displayed linear factor is positive and less than p=2r+6s+3. The fixed scalar primes2,3,5 are also units. The remaining sextic has integer content1, so its reduction cannot be identically zero modulo any prime, including primes dividing its leading coefficient. Thus at most six actual r can fail the evaluation-rank conclusion. The actual r-values are distinct modulo p along the fixed-prime interval.

The argument works in the four-dimensional F_p algebra `F_p[x]/(x^4-1)`. When i is not in F_p, adjoining it for evaluation and then descending gives the same rank. It does not assume that all four roots lie in the ground field.

## 4. The endpoint quotient and the exterior state

I checked Item194's kernel argument rather than using rank three as an unexplained assertion. Under `3j+1<p` and `2j+2<p`, zero logarithmic and circular coordinates imply zero finite residues. All pole orders are below p, so ordinary partial fractions give a rational primitive. The differential is proper of order at least two at infinity, and its primitive can be chosen finite there.

If the rational endpoint coordinate is also zero, subtract the common endpoint value. The primitive then has zeros of order at least3j+1 at0 and1 and poles of order at most2j+1 at roots of Q. Consequently it has the form

    u^(3j+1)(alpha+beta x)/Q^(2j+1).

Since H(0)=0 and3j+1 is a unit, differentiation forces alpha=0. Therefore the kernel is exactly the line spanned by G_j. The same argument works at j=0: the zero order is1 and the pole order is2<p. No j=0 exception is needed.

The four evaluation vectors T(r),T(r-6),T(r-12),Frobenius, when independent, map to four independent vectors H_0,H_1,H_2,G_j. Their three quotient classes form a basis of the endpoint-coordinate space. The two fixed coordinate rows R and L are therefore independent on this basis. Their exterior product is nonzero. This supplies the actual zero-full-state bound of at most six starts without a presumed seed and without propagation across a singular companion.

## 5. Exterior dynamics and limiting observation

The projected contiguity gives

    kappa=-a_1 w_01-a_2 w_02.

The signs follow directly from `kappa=f_1 g_0-f_0 g_1`, with f and g denoting the L and R coordinates and the subscript1 denoting the nu=1 form. Taking the exterior square of the displayed companion gives exactly

    W=[[0,0,1],[-C_20,0,C_22],[0,-C_20,-C_21]].

The limiting observation for r*kappa is the stated rational row. I independently evaluated `det(v,vW,vW^2)` and obtained `243/705100000`.

The characteristic polynomial of C is the previous nondegenerate cubic under the exact scale t->t/64. The pairwise-product eigenvalues of the exterior square are nonzero and distinct, and their quotients are original eigenvalue quotients. Thus the previously verified non-root-of-unity condition applies. Together with the cyclic row, this proves the limiting observation determinant is nonzero at every fixed spacing.

Multiplication of kappa by r preserves its zero set on the reviewed r>=12 range, since 0<r<p. The direction r->r-6 is the actual fixed-prime row direction. Endpoint boundary rows are finite in number; observation paths are used only where each intermediate transfer is defined.

## 6. Quantitative progression transfer and uniformity in j

The new density note keeps the rational denominator exceptions explicit. Choose fixed integer polynomial common denominators q,d for the exterior transfer and observation. If M=qT and V=dv, their leading coefficient matrix and row are integral scalar multiples of W and v. The three observation rows at spacing h have degrees E,E+Dh,E+2Dh. Their top determinant coefficient is exactly

    a^3 det(v,vL^h,vL^(2h)),

which is a nonzero integer. Since L and a v are fixed integer matrices/rows, the absolute value of that coefficient is at most an exponential in h. Thus for h<=c0 log p with c0 sufficiently small it remains nonzero modulo p. Shifts by6h change lower coefficients but do not change this leading-coefficient argument.

The observation polynomial and all necessary denominator products have degree O(h+1). Their zeros, the at most six zero full states, and terminal rows therefore contribute O(h+1) bad starts for each h. Removing all bad all-zero progression starts through K removes O(K^2) points. The remaining blocks of length K contain no three-term progression. The quantitative additive-combinatorial Roth bound imported in the earlier reviewed note then yields `Z_j(p)<=C p exp(-c(log log p)^(1/9))`.

Every constant in this argument is independent of j: the operator, observation row, coefficient-height bounds and sextic are fixed. The endpoint-map argument only needs the two displayed inequalities. Its proof introduces no separate j-dependent exceptional prime set. This uniformity is sufficient for the direct all-j sum in the density note.

## 7. Global sum and exact scope

On X<m<=2X, primes at most sqrt(12X)+2 contribute O(X^(3/2)) to the entire radical sum by Chebyshev, without using any recurrence theorem. For a larger prime, the exact bound on s gives

    j<=(4m+1+2s-p)/(2p)<=4X/p-1/3,

where the first relation is equality for the actual j. Hence `3j+1<=12X/p<p`. For j>=1 this also implies `2j+2<p`; for j=0 that inequality is automatic. The endpoint theorem therefore applies to every remaining cell.

For each p there are O(X/p+1) relevant j, and p<=12X. The uniform bound for Z_j(p) gives

    O(X^(3/2))
      +O(sum_(sqrt(12X)<p<=12X)(X/p+1)p delta(p)log p)
    =O(X^(3/2))+O(X^2 delta(sqrt(12X))).

Only Chebyshev estimates and monotonicity of delta are used. Adjusting its constant gives the claimed rate in X. This proves the first-Witt radical support has zero normalized dyadic average and is o(m) in density.

The summation counts one logarithmic copy per prime. Each fixed deeper layer is contained in the first layer, so fixed finite sums of radical layers inherit the estimate. Nothing here permits summing an unbounded number of valuation layers, changes an already booked lower bound, or proves anything about a sparse exceptional subsequence sufficient to settle e+pi.
