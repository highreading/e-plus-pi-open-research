> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact three-state output for the half-step certificate

2026-10-02. Original author continuation of `ODD_SELECTOR_HALF_STEP_DRAFT.md`; its archive and opened-primary-paper search ledger applies to this already stated target. This note proves the state and output formulas uniformly. Exact all-axis determinant calculations at n=4 and n=8 test the meaningful hypothesis that the actual three-output determinant has no nonnegative zero for every n=4k. They do not establish that infinite-n hypothesis.

Let z(w)=1−2w², a=(1+i)/2, z_+=1−i, z_−=1+i, and

    L_h=∫_(bar a)^a z(w)^h dw,
    D_h=i L_h,
    A_h=z_+^h+z_−^h,
    B_h=i(z_+^h−z_−^h).

For nonnegative integer h, these are rational numbers. The state X_h=(D_h,A_h,B_h)^T is nonzero: z_+^h and z_−^h cannot both vanish, and their invertible linear transformation to A_h,B_h cannot both vanish. No division by U_h occurs.

## 1. Regular transition at every h≥0

The identity

    D_w(w z^h)=(2h+1)z^h−2h z^(h−1)

and a z_+=bar a z_−=1 give

    X_(h+1)=M(h)X_h,
    M(h)=[ (2h+2)/(2h+3)    0      1/(2h+3) ]
         [       0           1          −1      ]
         [       0           1           1      ].

Thus det M(h)=2(2h+2)/(2h+3)>0 for every real h≥0. All products of forward matrices used below are regular throughout that axis.

Write S_0=I and S_j=M(h+j−1)…M(h). Retain the proved half-step fixed polynomial P̆_n(w), degree 3n+1, with coefficients p_k. If

    Y_h=i∫_(bar a)^a P̆_n(w)z(w)^h dw,

then the ACTUAL certificate is W̆(n,h)=2^(n+1)Y_h. Each even monomial contributes

    i∫ w^(2ell)z^h dw
       =2^(−ell) Σ_(j=0)^ell (−1)^j binom(ell,j) D_(h+j),

and each odd monomial contributes

    i∫ w^(2ell+1)z^h dw
       =−2^(−ell−2) Σ_(j=0)^ell (−1)^j binom(ell,j)
                                  B_(h+j+1)/(h+j+1).

The latter follows from dz=−4w dw and exact endpoint evaluation. Hence Y_h=R_n(h)X_h with an explicit rational row R_n(h), obtained by replacing D_(h+j) by the first row of S_j and B_(h+j+1) by its third row. Every unreduced denominator in this formula is positive when h≥0: it consists of h+j+1 or 2h+2j+3. Individual forcing zeros are harmless.

The three consecutive output rows pulled back to X_h are

    O_n(h)=[R_n(h); R_n(h+1)M(h); R_n(h+2)M(h+1)M(h)].

If det O_n(h)≠0, the nonzero actual state proves that at least one of W̆(n,h), W̆(n,h+1), W̆(n,h+2) is nonzero. The nonzero scalar 2^(n+1) was omitted only from the row normalization; it cannot alter this conclusion.

## 2. Exact n=4 and n=8 whole-axis evidence

`derive_half_step_observability.py` constructs the fixed polynomial from the proved old fixed kernel, derives the rational rows by the displayed identities, computes the exact determinant, and counts its nonnegative real roots by exact Sturm arithmetic. All coefficients and factorizations are saved in `half_step_observability_n4.json` and `half_step_observability_n8.json`, with logs. This is not a numerical sample grid and is not the archived fifteen-certificate rerun.

At n=4,

    det O_4(h)=−46080 P_4(h) /
        [ ∏_(j=3)^9(h+j) ∏_(j=1)^8(2h+2j+1) ],

    P_4=7h^8−132h^7−3144h^6+16566h^5+995193h^4
         +10688814h^3+71197592h²+270770544h+1247110848.

At n=8,

    det O_8(h)=−13005619200 P_8(h) /
        [ ∏_(j=3)^15(h+j) ∏_(j=1)^14(2h+2j+1) ],

where P_8 has degree 16 and its complete exact coefficients are in the saved JSON. Both numerators have mixed coefficient signs. Exact Sturm counts are

    #{nonnegative real zeros of P_4}=0,
    #{nonnegative real zeros of P_8}=0.

Their positive constant terms and continuity therefore prove P_4(h),P_8(h)>0 on the entire nonnegative axis. It follows that the actual certificates for n=4 or n=8 have no three consecutive zeros at any nonnegative integer start h. The actual state, the full contour output, and its normalization are retained in this conclusion.

The denominator patterns and degree 2n numerators in these two cases suggest a simpler structural target than the old even-step degrees 4n+6. The general degree pattern and uniform nonnegative-axis nonvanishing remain open. No all-n positivity is inferred from two exact cases; the signs of the coefficients already exclude the simplest coefficientwise proof.

## 3. What this would buy if extended uniformly

A uniform det O_n(h)≠0 for n=4k,h≥0 would select a nonzero certificate from h,h+1,h+2 and require direct center support through h+n+3. Its exact primitive lattice would use L*=3n+2h+6, center component length N*=4n+2h+6, and complete exponential majorant Λ*=6n+4h+12. These constants follow directly from the largest certificate start and largest direct node. They are recorded prospectively; the all-n premise is not yet proved.
