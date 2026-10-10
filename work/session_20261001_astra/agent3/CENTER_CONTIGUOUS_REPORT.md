> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Report: contiguous factorially weighted B-only centers

Status: original algebraic research, conditional on the retained provisional contact reduction/normality. Nonstabilization remains open. No samples, scans, old-check replay, or independent audit.

Main note: CENTER_CONTIGUOUS_RESEARCH.md in this directory. This concerns the actual B-only center with w_j=(n+m+1-b)!/(n+m+1-j)!, not the earlier full-coefficient center.

The explicit family is b=floor(log n), m=floor((b-1)/2), n>=2^96. The note proves the sufficient inequality n>=512(b+1)^4 log n, ensuring all old/new dimensions used in the update are admissible under the retained theorem.

The key new cancellation is as follows. For either actual forcing H_n=q^n D^n h, and its solved transformed polynomial x, put R=H_n-G_n x. Then

    H_{n+1}-G_{n+1}(I+D)x=(qD-nq')R.

The old contact window makes R_n,...,R_{n+b-1} zero. Consequently the new forcing defect has only TWO possibly nonzero entries at fixed b:

    (n+b)R_{n+b},
    (n+b+1)R_{n+b+1}-bR_{n+b}.

At a dimension border it has one additional entry

    (n+b+2)R_{n+b+2}-(b+1)R_{n+b+1}
                                      +(b-n)R_{n+b}/2.

This applies separately to both P and Q forcing columns. The correct transformed predictor is (I+D)x because (I+D)^(-(n+1))(I+D)=(I+D)^(-n). It therefore preserves the embedded old actual B polynomial before the sparse correction is added. The endpoint constant in the Q column remains present.

The note also gives the exact Toeplitz row-shift formula with its two missing boundary rows, and treats a b increase as a separate matrix border. It records the ordinary factorial weight change and both possible m behaviors at a b border.

A fully rational adjugate implementation gives

    beta'=(Delta' A0+P)/(Delta Delta'),
    gamma'=(Delta' C0+Q)/(Delta Delta'),

where A0,C0 are embedded old adjugate-normalized B columns and P,Q use only two or three specified adjugate columns and the explicit boundary numerators. No second center is left as an unspecified fraction.

After documenting cancellation of common scalar normalizations, the exact center-change numerator splits as

    H_n=Delta'^2 H_weight+Delta' H_linear+H_quadratic.

The three terms are, respectively, the changed factorial metric on the old columns, the linear sparse forcing correction, and its quadratic correction. Their formulas are in Section 7. The denominator U Dnew is strictly positive, so sign(t_{n+1}-t_n)=sign H_n. Section 8 supplies a finite positive denominator clearer L with I_n=L^6 H_n integer and J_n=L^6 U Dnew positive integer. Thus equality is exactly I_n=0, retaining rational normalizations and gcd reduction without making denominator-growth claims.

The unresolved condition is exclusion of eventual cancellation in this particular explicit integer expression. Globally, nonstabilization is equivalent to I_n being nonzero for arbitrarily large n. On the explicit interior pairs n_k=ceil(exp(k))+2 and n_k+1, k>=96, b=k and m are both unchanged; infinitely many nonzero I_{n_k} would suffice. No such infinite nonvanishing or signed domination has been proved.

The main structural advance is that only two forcing-tail defects per column are needed on those interior pairs, rather than recomputation of unrelated contact quotients. Finite evidence and a nonzero error for the different full-coefficient center are not used. Other agents retain ownership of forcing bounds, the positive-column lower bound, and reduced denominators.

Operational completion requires controller-confirmed saving and read-back of this report and the main note. This sentence records the requirement, not a claim that the pending operations have already occurred.
