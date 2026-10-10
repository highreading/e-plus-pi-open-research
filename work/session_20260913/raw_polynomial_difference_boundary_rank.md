> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual polynomial difference leaves a large scalar boundary map

Date: 2026-09-13. Original bounded continuation by audit_results.
Independent review requested.

This tests whether the positive polynomial F_b-F_a, of degree one below the high factors, makes the mixed correction disappear after a few top-degree conditions. It proves an exact obstruction at the actual second-channel boundary: the polynomial difference has boundary rank h-1, and the rational ratio has boundary rank h. Removing O(sqrt(n)) scalar degree directions leaves rank of order n. These are actual-family statements using the true factors and seed, not examples for an arbitrary positive matrix.

The final projection against the first channel may still cause additional cancellation. Its rank or sign is not settled here. The new result identifies precisely where a further theorem must act.

## 1. The actual scalar support is large enough for polynomial identities

Use the established cutoff b=ceil(192sqrt(n)), equalized high counts, and N=2n. Let m_b be the number of true nodes of the second-channel parity through n, ell_b its low count after the optional root transfer, and h its high count. Then exactly

    d=d_b=n-m_b,
    h=m_b-ell_b,
    d+h=n-ell_b.                                  (1)

For all sufficiently large n, h is positive, d>=h, and both have order n, while d-h=O(sqrt(n)). In particular h=n/2-O(sqrt(n)). The fixed signs of the node polynomials have no effect on the following arguments.

The actual positive scalar measure for the second polynomial space is

    dchi_b(t)=F_b(t)L_b(t)^2 dSigma_bb(t).

Its support consists only of actual row eigenvalues. Every high root alpha_i,beta_i lies strictly above that spectrum. The support has at least d+h distinct points.

Proof of this last assertion: if u has degree <d+h=n-ell_b and is nonzero, then L_b u has degree <n and is nonzero. The exact finite two-component polynomial representation implies

    (L_b u)(K_N)v_b != 0.

Indeed its component degree is <n, so its maximal coefficient index is <2n, and the triangular branch-coefficient basis is injective. Multiplication by the positive invertible F_b(K)^(1/2) preserves nonzero vectors. Thus the chi_b norm of every nonzero polynomial of degree <d+h is positive. A positive finite measure with fewer than d+h distinct support points would contradict this by the polynomial vanishing on its support. This also handles possible repeated K eigenvalues and possible zeros of L_b on the row spectrum: neither is silently assumed absent.

Consequently, whenever a polynomial of degree <d+h vanishes chi_b-almost everywhere, it vanishes identically. This is the decisive actual-family input below.

## 2. Exact boundary rank for the positive polynomial difference

Write

    F_a(t)=product_(i=1)^h(alpha_i-t),
    F_b(t)=product_(i=1)^h(beta_i-t),
    alpha_1<beta_1<...<alpha_h<beta_h.

Set q=F_b-F_a. The exact telescoping formula from the preceding note proves that q has degree h-1 and is nonzero. Its leading coefficient in t is

    (-1)^(h-1) sum_i(beta_i-alpha_i).

It also has positive coefficients in (2n+1)-t. These positivity facts are retained, but the rank calculation needs only its exact degree.

Let V_m denote scalar polynomials of degree <m in L^2(chi_b), and let P_d be the orthogonal projection onto V_d. For an integer r with 0<=r<=d, consider

    T_(q,r)=(I-P_d) M_q|_(V_(d-r)).

Then, for h>=1,

    rank T_(q,r)=max(h-1-r,0).                     (2)

Proof: T_(q,r)u=0 means that qu agrees on the scalar support with some v of degree <d. The difference qu-v has degree at most d+h-2-r, or degree <d if u=0; in every case its degree is <d+h. By Section 1 this is a polynomial identity. Thus the kernel consists exactly of the u in V_(d-r) with deg(qu)<d, that is deg u<d-(h-1). Its dimension is min(d-r,d-h+1), using d>=h. Subtracting it from d-r proves (2). For h=1, q is a nonzero constant and the boundary map is zero, in agreement with (2).

Under the isometry u -> F_b(K)^(1/2)L_b(K)u(K)v_b, (2) is the rank of the actual off-block q(K) map from the first d-r second-channel Krylov degrees into the orthogonal complement of the full d-degree second channel. It holds in the actual F_b energy coordinates used by the mixed reduction. It is not a claim about a coordinate-prefix projection in the original E basis.

In particular r=O(sqrt(n)) leaves rank h-1-r=n/2-O(sqrt(n)). For arbitrary linear conditions of total codimension at most r, the general restriction inequality also leaves rank at least h-1-r. Thus neither the one-degree drop nor O(sqrt(n)) top constraints reduce this boundary operator to rank O(sqrt(n)).

## 3. Exact boundary rank of the rational ratio itself

The actual ratio R=F_a/F_b has no poles on the scalar support. Define

    T_(R,r)=(I-P_d) M_R|_(V_(d-r)).

Then

    rank T_(R,r)=min(d-r,h).                       (3)

Proof: T_(R,r)u=0 is equivalent to R u=v on the support for some v in V_d. Multiplying by F_b gives

    F_a u-F_b v=0

on the support. Its degree is at most d+h-1, hence <d+h; Section 1 makes this a polynomial identity. The true high lists have distinct interlaced roots, so F_a and F_b are coprime over R. Therefore F_b divides u. Conversely, u=F_b w with degree <d-r gives R u=F_a w of degree <d-r<=d. The kernel dimension is max(d-r-h,0), proving (3).

For r=0 the rank is exactly h. For arbitrary codimension-r conditions it is at least h-r. At top truncations the sharper formula (3) can keep the full rank h until r exceeds d-h. Thus the ratio correction does not acquire a small rank merely because its numerator and denominator share their leading term.

This proof retains the actual multiplier dimensions and every zero of the true low factor through the scalar support argument. It uses neither simple K spectrum nor a generic scalar-measure assertion.

## 4. Consequence for the actual rank-one boundary sum

Use the notation of `raw_mixed_channel_boundary_schur_reduction.md`. The columns V_b are an orthonormal basis of V_d under the isometry above, ordered by scalar polynomial degree, and P=I-V_bV_b^T. Equation (3) gives

    rank(P R(K)V_b)=h.                            (4)

The exact Stieltjes/boundary expression is a sum of h rank-one matrices,

    P R(K)V_b
      =-sum_i c_i beta_b P(beta_i I-K)^(-1)eta_b
                     e_b^T(beta_i I-J_b)^(-1).     (5)

The constant part of R contributes zero. Because (4) is h, the two h-column/row factor families in (5) each have rank h and their product attains that rank. In particular the scalar boundary coefficient beta_b is nonzero here. This also follows directly from positivity of the next scalar polynomial norm supplied by Section 1.

So there is no hidden cancellation of the h-pole sum before the first-channel compression. The rank-one formula is exact and useful, but its sum is not a low-rank operator of order sqrt(n).

The final mixed correction contains the further maps

    Z^T [P R(K)V_b] C,
    C=V_b^T V_a,
    Z=P V_a.                                      (6)

No lower rank bound for (6) is claimed. Its first-channel overlap and projection are exactly the remaining location where special cancellation or a useful signed bound could occur. Deleting C or replacing the cross spectral measure by diagonal weights would change this term.

## 5. Exact support commutation leaves a separate reflection skew form

There is a second precise way to see what the polynomial support argument does and does not remove. Let u and v be raw coefficient vectors of opposite component parity, so C_Nu=u and C_Nv=-v. Suppose v has support ending at s_v and s_v+2(h-1)<N. This condition is fulfilled for retained-degree v and the present h=n/2-O(sqrt(n)), for all sufficiently large n. The exact finite polynomial identity gives

    C_N q(K)v=q(K)C_Nv=-q(K)v.

It follows exactly that

    2 u^T q(K)v
       =u^T [C_N^T-C_N] q(K)v.                    (7)

Indeed u^T C_N^T=u^T, while C_Nq(K)v=-q(K)v. If the component labels are interchanged, the corresponding fixed sign changes. Thus eliminating the finite commutator boundary does not make the cross pairing vanish: its remaining form is the actual skew-adjoint part C_N^T-C_N. For example its first 2-by-2 block is already nonzero because E_1(1-x)=sqrt(3)E_0-E_1. Equation (7) is an identity, not a claim that this small block alone proves a rank bound for a large restricted pairing.

The positive-power lemma controls the norm of C_N in the q metric on supported polynomials; it does not assert selfadjointness there. Equation (7) isolates the missing selfadjointness rather than attributing the cross term to a discarded finite boundary.

## 6. Status of a signed or accretive Schur estimate

The mixed reduction writes S=S_+-UV^T with S_+=Z^T RZ positive definite. Its symmetric part is exactly

    (S+S^T)/2=S_+-(UV^T+VU^T)/2.

The present calculation proves that the uncompressed boundary factor in U,V has full pole rank. It does not give a sign for the displayed symmetric correction after the two different first-channel projections. Positivity of F_b-F_a supplies no new positive lower bound for this actual Schur form in the derivation above.

The smaller remaining task is therefore specific: estimate the first-channel compression in (6), equivalently the normalized boundary correction in the mixed note, using its actual overlap C. An O(sqrt(n)) rank conclusion cannot be justified solely by the polynomial's one-degree drop or by removing O(sqrt(n)) scalar top degrees. Any successful argument must use additional first-channel information or bound the signed compression without asserting low rank.

No new canonical degree, prime, or numerical scan was used. No mixed retained-rank improvement or irrationality conclusion follows from this bounded result.
