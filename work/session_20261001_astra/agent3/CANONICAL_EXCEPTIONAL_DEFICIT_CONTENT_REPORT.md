> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exceptional canonical deficit content report

Original author research for the same b=3,m=1 factorial B-only Gram center. CANONICAL_OVERLAP_DEFICIT.md, its factorization, and the completed seed/modulo-121 transfer are preserved. No old calculation or independent review was performed.

The new normalization removes common scalars before evaluating the binary forms. With

    k_C=content(C), Cbar=C/k_C,
    k_R=content(Cbar[j0 j1]),
    Rbar=Cbar[j0 j1]/k_R,

one has k_C dividing |Delta| and

    Bform=k_C^2 k_R^2 Bbar,
    urow=k_C^2 k_R uhat,
    vrow=k_C^2 k_R vhat.

The endpoint term is retained explicitly in vhat. These exact identities remove k_C^2 k_R from the common companion denominator. The old normalized rows, final evaluated gcd h0, D2, and Wcancel remain unchanged.

Writing Bbar=abar_B Bprim, the strengthened bound is

    delta_exc divides
      gcd(d0 L t0 k_R abar_B c_H Rresultant,|Wcancel|).

The primitive resultant is unchanged. The note also gives exact raw-resultant factorizations, separating matrix content, joint row content, and sum-row content before evaluation.

A further content restriction isolates a reconstruction-lattice factor. The primitive rank-two matrix

    Ybar=adj(M)Drow[j0 j1]/(k_C k_R)

has Smith factors 1,kappa2. Its restricted Gram content satisfies

    abar_B divides 2 kappa2^2 det(G_K),
    det(G_K)=sum_i product_(j!=i) omega_j^2<=4(n+2)^12.

Thus, for

    a_reg=gcd(abar_B,2det(G_K)), a_lat=abar_B/a_reg,

one has a_reg<=8(n+2)^12 and a_lat dividing kappa2^2. Moreover

    kappa2=4(n+2)d0 |Delta|m_n/(k_C^2 k_R^2),
    m_n=content(M^T(d0/2,-(2n+3),1)^T),
    m_n divides |Delta|.

This identifies residual maximal-minor saturation after entry content is removed. It does not prove that this actual factor has either small or large asymptotic size.

The exceptional deficit now has an exact further separation:

    K_reg=d0 L t0 a_reg,
    delta_reg=gcd(delta_exc,K_reg),
    delta_res=delta_exc/delta_reg.

Then

    log delta_reg=O(n),
    delta_res divides k_R a_lat c_H Rresultant,
    delta_res divides Wcancel/delta_reg.

The factors need not be coprime. A uniform coarse ceiling is also proved:

    log delta_exc<=4log(n!)-2log k_C-log k_R+O(n).

Explicit ceilings for every matrix, row, and resultant factor are supplied in the main note. They are upper bounds, not evidence of favorable gcd cancellation.

The remaining condition is exact. For a prime p put f_p=2v_p(n!), d_p=v_p(D2), w_p=v_p(Wcancel), and k_p=v_p(K_reg). Then

    v_p(delta_res)=max(0,min(d_p,w_p)-f_p-k_p).

Loss of j powers therefore requires denominator depth at least f_p+k_p+j and cancellation to that precision in Wcancel. Before dividing the integer sum row by shat h0, the required precision increases by v_p(shat)+v_p(h0). A first-order zero or prime-support argument cannot substitute for these depths.

Since log delta_reg=O(n), log delta_exc=o(n log n) is equivalent to the corresponding weighted sum of these residual exponents being o(n log n). That estimate remains unproved.

The separate delta_F is unchanged and is not estimated here. Even a subfactorial exceptional factor alone would not establish the total-deficit condition for the 5/72 overlap threshold. No global application or irrationality conclusion is claimed.

Both deliverables require successful saving and full read-back before operational completion is reported.
