> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact reflected-kernel coefficient handoff for actual prime content

2026-10-02. Derived coefficient formulas, supplied to the arithmetic agent for its separately gated actual5-depth research. No prime-depth conclusion is made here.

Use n=4k>=4,h>=1,N=n+h,L=h−1,epsilon=(−1)^h,T=L!, q(w)=1−2w+2w², F0=q(w)^N/[w^(N+1)(1−w)^h],F1=wF0.

For0<=j<=N and0<=j<=L respectively,

    d_j=(−1)^j Σ_(ell=0)^floor(j/2)
                     binom(N,ell)binom(N+n−2ell,j−2ell),
    c_j=Σ_(ell=0)^floor(j/2)
                     binom(N,ell)binom(N−1−2ell,j−2ell).

Set every negative-index d,c to0. Then

    R0=d_N−epsilon c_L,
    R1=d_(N−1)−epsilon(c_L+c_(L−1)),
    M0=epsilon Σ_(j=0)^L c_j(L)_j,
    M1=epsilon Σ_(j=0)^L(c_j+c_(j−1))(L)_j,
    mi=Mi−T Ri,
    U=M1R0−M0R1>0,
    E=m1 Σ_(j=0)^N d_j(N)_j
           −m0 Σ_(j=1)^N d_(j−1)(N)_j.

Here E=N!B(F) is the COMPLETE cleared exponential numerator, and is odd for everyh; this does not imply any5-adic unit statement.

The principal coefficients of F=m1F0−m0F1 are

    a_(0,t+1)=m1 d_(N−t)−m0 d_(N−t−1), 1<=t<=N,
    a_(1,t+1)=epsilon[m1c_(h−t−1)
                          −m0(c_(h−t−1)+c_(h−t−2))],1<=t<=h−1.

At infinity define for0<=j<=n

    k_j=(−1)^j Σ_(b=0)^floor(j/2)
                   binom(N,b)2^(−b)binom(n−b,j−2b),
    k_j=0 for j<0,
    p_ell=epsilon2^N[m1 k_(n−1−ell)−m0 k_(n−ell)],0<=ell<=n.

This follows from `(1−v+v²/2)^N(1−v)^(-h)=Σ_b binom(N,b)2^(-b)v^(2b)(1−v)^(n−b)`, before extracting the low infinity coefficients. The projected polynomial degree is at mostn. The entire rational primitive numerator is

    Pi=4Im[Σ_(ell=0)^n p_ell a^(ell+1)/(ell+1)
           −Σ_(t=1)^N a_(0,t+1)a^(−t)/t
           −Σ_(t=1)^(h−1)a_(1,t+1)(a−1)^(−t)/t],
    a=(1+i)/2.

All partial/polynomial coefficients are integers, Pi is2-integral, and O_N Pi∈Z for O_N=oddLCM(1,...,N). The ACTUAL complete center and q are

    c=−[E/N!+Pi]/U,
    q=N!O_N U/gcd(N!O_N U,O_N E+N!O_N Pi).

For actual5-depth, the final signed integer `O_N E+N!O_N Pi` and U must BOTH be retained. Raw factorial or lcm valuations do not themselves supply v5(q).
