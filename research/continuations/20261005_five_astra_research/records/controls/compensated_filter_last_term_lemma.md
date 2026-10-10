> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Coordinator draft: a unique last factorial pole for compensated b=2 filters

2026-10-04. Candidate paper proof for independent review. This is a new filter lemma, not an irrationality decision. It reuses the original independently reviewed scalar transfer and second-kind valuation estimates, rather than repeating them.

Let S=e+pi. Use A3 turn3's exact raw-scale outputs

    H_k=(Qcal_k+2^(k+1)Vraw_k/(k!)^2)/(k!)^2,
    J_k=Dcal_k/(k!)^2,
    Vraw_k=(k+1)Vtilde_k,
    Qcal_k=(k+1)Qtilde_k,
    Dcal_k=(k+1)Dtilde_k.

The old B2_WHOLE_FAMILY_REVIEW gives Dtilde integral and Vtilde in Z[1/2], all-index transfer at every odd prime, Vtilde_0=4, and

    vp(Qtilde_k) >= -floor(log_p(k+1)).

Fix positive coprime integers a,b, w_j=binom(m,j)a^j b^(m-j), N=n+m, n>=2. Define Hsum=sum w_j H_(n+j), Jsum=sum w_j J_(n+j), and c=-Hsum/Jsum on Jsum nonzero. Let q be its actual reduced denominator, irrespective of which common clearer is chosen.

Claim: for EVERY odd prime p dividing N with p not dividing a,

    vp(Hsum)=-4vp(N!),
    vp(Jsum)>=-2vp(N!),
    vp(q)>=2vp(N!).                                      (1)

This includes a prime that grows with N; it does not need an all-residue unit atlas.

Proof. Write F_k=vp(k!), ell_k=floor(log_p(k+1)). At k=N, scalar transfer on residue zero gives Vtilde_N=4 mod p, and N+1 is a unit, hence Vraw_N is a unit. The factorial part of H_N has valuation -4F_N. The second-kind part has valuation at least -ell_N-2F_N. The inherited elementary inequality 2F_N>ell_N holds at every N>=p, so these valuations are strictly separated and vp(H_N)=-4F_N.

For every earlier k>=2 we have vp(H_k)>=-4F_k. Indeed Vraw_k is p-integral. If k>=p, 2F_k>ell_k, so the second-kind part also has valuation greater than -4F_k. If k<=p-2, ell_k=0 and F_k=0. At k=p-1, F_k=0 and ell_k=1, but the factor k+1=p in Qcal_k raises its valuation to at least zero. These cases exhaust all k.

All w_j are ordinary integers. The last coefficient w_m=a^m is a p-unit. For k<N,

    F_k<=F_(N-1)=F_N-vp(N)<F_N.

Thus every earlier weighted H_k has valuation at least -4F_k>-4F_N. The last summand is the unique minimum; it proves the first equality in (1), even if some earlier weights vanish or acquire extra p-content. Dcal_k is integral, so vp(J_k)>=-2F_k and vp(Jsum)>=-2F_N. Finally, for Jsum nonzero, ordinary rational reduction gives

    vp(q)=max(0,vp(Jsum)-vp(Hsum))>=2F_N.

This is after the FULL cross-index endpoint gcd. No global scalar normalization or positivity hypothesis has been omitted.

The proof of 2F_k>ell_k, used above, is elementary and uniform over odd p. If ell_k=1, k>=p gives F_k>=1. If ell_k>=2, k>=p^ell_k-1, so 2F_k>=2 floor(k/p)>=2(p^(ell_k-1)-1)>ell_k. The strict inequality already holds at p=3, ell_k=2. If ell_k=0 it is automatic for k>=p only vacuously; such k actually have ell_k>=1.

For n above the inherited eventual sign threshold, J_k has one nonzero sign at every k>=n. Positive w_j then give Jsum nonzero for every m. If an unbounded sequence N divisible by one fixed p not dividing a is chosen and starting indices n remain above that threshold, (1) forces q to infinity.

This also gives unconditional EVENTUAL NONVANISHING of S-c on that sequence: if S is irrational, it differs from every rational c; if S is rational with reduced denominator q_S, equality c=S forces q=q_S, impossible eventually. This case split proves nonvanishing without deciding which case holds.

A stronger denominator budget follows on odd primorial indices. Let N_x be the product of all odd primes p<=x that do not divide a, and take any starting index 2<=n<=N_x above the sign threshold, with m=N_x-n. Then (1) implies

    log q >= 2 sum_(p<=x, p odd, p not dividing a) vp(N_x!) log p.

Legendre's formula bounds vp(N!)>=N/(p-1)-O(log N/log p), uniformly in p. Summing gives

    log q >= 2N_x sum_(p<=x, p odd, p not dividing a) log p/(p-1)
             -O(pi(x)log N_x).

PNT and partial summation yield log N_x=(1+o(1))x and the sum=(1+o(1))log x. The subtracted term is O(x^2/log x)=o(N_x log x). Hence

    liminf log q/[N_x log log N_x] >= 2.                  (2)

Only finitely many primes are omitted, which does not affect the leading term. The denominator grows faster than exp(CN) on these explicit indices. This still does NOT exclude the filtered route without a matching lower bound for the whole signed error, and it does not decide the irrationality of S. It gives a new arithmetic constraint that any claimed signed filter gain must meet at the same final N.

Review requirements: verify A3's precise raw constants, Vraw=(k+1)Vtilde, Qcal=(k+1)Qtilde, the second-kind bound, final rational reduction, and the legitimacy of the uniform-in-p primorial estimate. Finite spot checks may be requested only to audit scale, not to justify the infinite assertion.
