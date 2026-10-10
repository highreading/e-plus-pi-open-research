> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Bounded independent examination of the new all-depth odd-prime Gram theorem

Examiner: Codex continuation Agent 3, 2026-10-02. Requested by the root after saving METRIC_CORRECTION_PROGRESS.md. One focused pass; the audit phase stops at this verdict. No old analytic infrastructure, accepted checker, historical controller or finite high-index scan was replayed.

Verdict: PASS for the new arithmetic theorem and the 17-prime finite criterion, for the exact b=3,m_w=1 factorial B-only Gram center and its complete endpoint correction. The theorem concerns its ACTUAL reduced denominator, at every sufficiently large normal index on either parity. Analytic construction-exclusion consequences retain the separate signed-asymptotic scope. The even asymptotic has the preceding narrow PASS; this agent's new odd/all-parity extension remains original author work awaiting another independent examination.

Examined source: agent1_arithmetic/ODD_PRIME_ALL_DEPTH_GRAM_DENOMINATOR.md and its exact normalization definitions. Only precise K_z and selector normalization definitions were recovered from the archive. No old result was re-audited.

## 1. Origin tails and the k=1 carry

For n=p^k a and s>=1, the coefficient bound
v_p(a_s(n))>=max(0,k-floor(log_p s)) follows directly by expanding Q(t)^n in powers of -t+t^2/2 and using binom(n,j)=(n/j)binom(n-1,j-1). All summands and coefficient denominators are p-integral at odd p.

At k>=2, every s>=3 matrix/A falling factorial contains n because i<=2. If s<p^k, its coefficient supplies an additional p. If s>=p^k, the factorial also contains n-p; p^k>=p^2>=p+3 supplies the needed range. Zero falling-factorial terms do not create an exception. The s=2 coefficient is n^2/2, and s=1 is -n. Thus the first-order N,A expansions are valid modulo p^(k+1).

At k=1, terms 3<=s<p have both the p from their coefficients and the factor n. Terms s>=p+3 have n and n-p. The remaining terms s=p+1,p+2 have coefficients zero modulo p by Frobenius, and still contain n. For s=p, a_p(n)=-a modulo p. The surviving matrix terms with j<=i obey

    (n+i)_(p+j)/n=-(i)_j mod p,

by Wilson's theorem. If j>i, the second multiple n-p is present and the term vanishes modulo p^2. This gives +na N0, not an independently placed carry. The A_i carry is +na Dcal_i=+na(A0)_i. The special n=p case has either a zero factorial polynomial or a term outside the finite sum.

The Dcal expansion also remains valid at k=1: every falling product (2n)_l with l>=p+1 contains both 2n and 2n-p. The l<=p coefficients produce C_p exactly. Hence the SAME scale 1+an multiplies N and A, as claimed.

The exact W0=0 can be checked without symbolic automation: adj(N0)A0=2(1,1,1)^T, H0 times this equals (2,0,0)^T, while det(N0)k0^T=(-2,0,0)^T. Scaling both N and A by s scales W by s^3, so the k=1 common scale changes W only at order n^2. It cannot change W/n modulo p.

The displayed first-order matrix contraction gives

    W/n=(20C+16,-24C-48,8C+32)^T,
    Y0=j(2,0,1)^T, D0=24j^2,
    V/n=16j(3C+4).

This agrees with the stated origin unit/depth conclusions.

## 2. All residues and endpoint units

The N,A finite sums reduce modulo p by truncating each falling factorial at the least nonnegative residue of n+i. Their surviving coefficient indices are <p, including residues r=p-1,p-2; Frobenius transfers those coefficients to Q(t)^r. The division-free Dcal recurrence resets at each multiple of p, so its residue depends only on its index modulo p. K and H are polynomial over Z[1/2]; their reductions do not divide by n+1 or n+2.

The generating function identity

    P(t)=Qend(t)^((p-1)/2)P(t^p),
    Qend(t)=1-4t-4t^2,

has a prefactor of degree p-1. Thus P_(pa+r)=P_a P_r exactly modulo p. Nonzero seed factors imply P_n is a unit at every base-p digit depth.

At r=p-2, the potentially carried P_(n+2) in D0J is killed by (n+1)(n+2). At r=p-1, factors n+1 kill both carried positive entries. Thus D0J transfers with its factor P_a at every residue, and V_n=P_aV_r, D_n=P_a^2D_r. No boundary residue was omitted.

## 3. Full beta and actual denominator reduction

The potentially misleading 1/n! in K_zhat causes no p-integrality loss: differentiating a monomial of degree m and dividing by n! contributes binom(m,n). The remaining factors and selector coefficients have only powers of two in their denominators. Therefore K_zhat has p-integral coefficients.

The exact endpoint equality K_zhat(1)=D follows from
zhat=D0 adj(N)^T H Y and Y=adj(N)D0J, with the retained forcing normalization. Polynomial division by t-1 preserves p-integrality. Its quotient degree is at most 2n+1. Each logarithmic moment has denominator dividing a power of two times j+1. Thus

    v_p(beta)>=-v_p(D)-floor(log_p(2n+2))

holds for the complete companion.

For n>=2p, writing a=floor(n/p)>=2 gives f=v_p(n!)>=a, v_p(n)<=a-1, and floor(log_p(2n+2))<=a. Consequently

    2f-v_p(n)>=a+1>floor(log_p(2n+2)).

This is strict. The factorial term 2^n V/((n!)^2D) has smaller p-adic valuation than beta, so the final rational sum cannot cancel it. Therefore

    v_p(q)=2f+v_p(D) when p does not divide n,
    v_p(q)=2f-v_p(n) when p divides n,

and in particular the claimed lower bound holds for actual reduced q. This includes the center's endpoint and final rational reduction; a clearing denominator was not substituted.

## 4. New finite certificate verification and rate comparison

The independent check_new_odd_atlas.py derives the finite seed data directly from the defining Q(t)^r coefficients, falling factorials, Dcal recurrence, exact K/Omega Gram matrices and endpoint generating polynomial. It does not import the author's residue algorithm or sample any n>=p. The 2927 NEW seeds for

    13,43,53,59,67,71,79,83,89,179,211,281,307,313,331,359,389

all satisfy criterion C, and every computed P_r and V_r agrees with the saved author certificate. The output is check_new_odd_atlas.json.

The compact-certificate interval formula was read: after reducing x to [1,2], log x=2 sum z^(2j+1)/(2j+1), z=(x-1)/(x+1), has the displayed positive geometric tail bound. The exact rational sqrt(2) bracket is valid. Thus its certified rho lower and tau upper are proper bounds. Their strict rational comparison was independently checked:

    rho=1.793505033394722...,
    tau=2log(1+sqrt(2))=1.762747174039086...,
    certified gap >0.0307578593556354.

At a common sufficiently large index all 17 prime factors divide q with their stated depths. Legendre's digit-sum estimate supplies the uniform O(log n) loss for this FINITE set. Therefore

    log q_n >=rho n-O(log n)

is an accepted arithmetic conclusion for this one center. If paired with a justified all-parity complete error at rate -tau, it excludes shrinking primitive forms for this center. Such exclusion does not decide the rationality of e+pi.

## 5. Search and primary-source record

Before this new audit, archive queries included origin-tail, origin k=1, all-depth Gram, endpoint P_n unit, n=-1 and n=-2. Earlier boundary-residue correction notes concern unnormalized contractions and do not replace the new normalization. No old review was replayed.

Current web queries: Hermite Pade factorial denominator p-adic carries Kummer binomial sums; Hermite Pade approximation factorial denominators arithmetic reduction prime valuations.

Primary papers opened:
- [Mano and Tsuda, Hermite-Pade approximation, isomonodromic deformation and hypergeometric integral](https://arxiv.org/html/1502.06695), structural HP/Toeplitz overlap.
- [Wielonsky, Asymptotics of Diagonal Hermite-Pade Approximants to e^z](https://www.i2m.univ-amu.fr/perso/franck.wielonsky/8.pdf), author PDF opened earlier in this same phase; a later reopen returned an internal error. Related HP remainder asymptotics, different arithmetic problem.
- [Sury, Revisiting Kummer's and Legendre's formulae](https://www.isibang.ac.in/~sury/kummerlegendre.pdf), elementary factorial/binomial valuation identities, not this Gram theorem.

No global novelty claim is inferred from search absence. Audit completed and stopped; original metric/tuning research resumes.

