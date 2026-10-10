> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Agent 3 endpoint-nonvanishing report

Status: exact representation and sufficient coefficient criterion proved; unbounded endpoint nonvanishing remains open. This report completes the previously unsaved analysis. Full details are in GROWING_ENDPOINT_NONVANISHING.md.

With row-oriented Wronskians and the cofactor convention B dot a=det[M;a], the exact formulas are

    Phi_n(P;x)=sum_m [t^m]P x^(n+m+1)/(n+m+1)!,
    Phi_n(p_(n+l);x)
      =D_x^(l-1)[x^(n+l)H_(n+l)(x)]/(2n+2l)!,
    D_V=Wr(Phi_n(p_(n+1)),...,Phi_n(p_(n+b-1)),
             exp(x-1),Phi_n(V))(1),
    Y=-D_V.

The auxiliary H_k is k![z^k]exp(xz)(1-z+z^2/2)^k, distinct from the projection polynomial. All functional indices stay in 0<=j<=b<=n, so n+m+1-j>=1. Difference determinants require d<=b; ordinary determinants require d<=b+1. Agent 2's domain correction is preserved.

A real Volterra transform reduces this to an explicit polynomial Wronskian. Set

    T_n(P;x)=n! sum_m [t^m]P x^m/(n+m)!,
    J_n A=x^(-n) integral_0^x u^n A(u)du,
    r_k=(I-J_n)T_n(p_k), r_V=T_n((1-t)V),
    Z=Wr(r_(n+1),...,r_(n+b-1),r_V).

The apparent singularity in J_n is removable, and exactly

    D_V=(-1)^(b+1)Z(1)/(n!)^b,
    Y=(-1)^b Z(1)/(n!)^b.

The transforms obey the original three-term recurrence with multiplication by t replaced by J_n. This provides a concrete real polynomial route without a positive-measure assumption.

The proposed sufficient lemma expands

    Z=sum_(k=0)^n [p_k(1)/h_k]
                    Wr(r_(n+1),...,r_(n+b-1),r_k).

Explicit Cauchy-Binet formulas give each summand's rational coefficients and hence its Bernstein coefficients on [0,1]. A common coefficient sign with nonnegative row margins epsilon_(n,k), whose sum is positive, implies

    |D_V|>=sum_k epsilon_(n,k)/(n!)^b>0.

The concrete unresolved target is this inequality for every even n>=4, b=n/2, with sign (-1)^(b-1). It would imply D_V>0 and Y<0. It has not been proved on that or any other unbounded growing-degree index set.

The preserved n=4,b=2 control verifies all representation identities and all 45 strict negative Bernstein coefficients, reproducing

    D_V=135377/103219200.

This is exact finite evidence only. No new controls were added; the existing file is endpoint_wronskian_control.json.

Three stronger routes have exact obstructions:

- The moments mu_m=(n+m)/(n+m+1)! satisfy ((n+2)!)^2(mu_0 mu_2-mu_1^2)=-(n^2+3n+3)/(n+3)<0, excluding a nonnegative real representing measure.
- Weighted mixed Wronskians have leading signs (-1)^(k+1), excluding common sign on the entire positive half-line. At the frozen n=4,k=1 control, the value at one is negative and the leading coefficient positive, proving a zero beyond one. This does not contradict the interval criterion.
- The operator 1/2-J_n is not positivity preserving: on h(x)=1-x its value at one is -1/[(n+1)(n+2)]. No unrestricted positive-pivot argument follows from the Volterra kernel.

The elementary comparison in ../GROWING_BOUND_OBSTRUCTION_DRAFT.md checks correctly. The chosen special-row bounds satisfy M_W>4M_V and therefore B_W>4B_V. Since |D_V|<=B_V and q>=1,

    q(B_W+B_T)/|D_V|>4q>=4.

Those chosen bounds cannot certify shrinking, regardless of the endpoint gcd. This conclusion needs no proposed integer clearer and does not exclude the actual construction. No separate audit of the content or clearing assertions is claimed here.

The most useful next endpoint lemma is the explicit uniform Bernstein coefficient inequality above, with quantitative margins if possible. It would supply normality and an actual endpoint lower bound. Shrinking would additionally require new estimates for the actual projection remainder ell_B(W)=D_W+T on the same indices; full-remainder nonvanishing remains separate. Further optimization of the old Gaussian constants is not proposed.

Deliverables under work/session_20261001_astra/agent3/:

- GROWING_ENDPOINT_NONVANISHING.md — proofs, domains, orientation, coefficient lemma, frozen evidence, and counterexamples.
- ENDPOINT_NONVANISHING_REPORT.md — this report.
- endpoint_wronskian_control.json — preserved existing exact control.

The completed prime certificate and earlier audit/refinement files remain preserved. No networking, installations, additional prime or degree scans, or edits outside Agent 3's directory are part of this continuation.
