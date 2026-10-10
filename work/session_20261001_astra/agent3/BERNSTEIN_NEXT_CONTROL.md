> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Bernstein-sign conjecture: frozen next control

Status: COMPLETE FROZEN CONTROL PASS; no uniform sign or unbounded nonvanishing theorem is established.

Only n=6,b=3 was computed. The proposed multiplier is sigma=(-1)^(b-1)=+1. All 133 Bernstein coefficients pass strictly: no negative coefficient, no zero coefficient, and no counterexample witness was found. The completed earlier artifacts are preserved.

## Exact objects and orientation

Use the monic polynomials p_k and h_k=2(-1)^k/[(2k+1)binom(2k,k)^2]. With the same fixed n=6 for every transform, define

    r_k(x)=6! sum_m ([t^m]p_k-[t^(m-1)]p_k)x^m/(6+m)!,
    w_k=p_k(1)/h_k,
    P_k(x)=w_k Wr(r_7,r_8,r_k)(x), 0<=k<=6.

Wronskian rows remain in the displayed order, and derivative columns are 0,1,2. Each P_k has actual degree L=15+k. Its Bernstein basis is binom(L,j)x^j(1-x)^(L-j), without degree elevation. If q_u=[x^u]P_k, then

    beta_(k,j)=sum_(u=0)^j q_u binom(j,u)/binom(L,u).

The endpoint uses the original functional columns ell_0,...,ell_3. Their factorial arguments are 6+m+1-j>=4. The difference determinant has dimension 3; the permitted ordinary dimension is 4. No negative-factorial convention is introduced.

Let V=sum_(k=0)^6 w_k p_k and Z=sum_k P_k. The preserved orientation gives

    D_V=Wr(Phi_6(p_7),Phi_6(p_8),exp(x-1),Phi_6(V))(1)
       =Z(1)/(6!)^3,
    Y=-D_V.

## Independent exact constructions

The checker constructs p_k using explicit ordinary Legendre binomial coefficients and verifies the monic recurrence. It forms each weighted mixed Wronskian in two ways:

1. Polynomial derivative determinants expanded with permutation signs.
2. Cauchy-Binet sums of rational coefficient minors multiplied by the increasing-index Vandermonde.

All polynomial coefficients agree. Bernstein-to-monomial reconstruction is checked exactly. The checker also verifies the Volterra recurrence, both high-function Phi identities, the Christoffel-Darboux transform, the kernel sum, the original endpoint functional determinant, and the cofactor sign. No canonical HP nullspace is used.

The checker ran successfully with exit code zero. Source hashes remained unchanged during the run.

## Complete sign results

| k | Actual degree | Positive coefficients | Zero | Negative | Minimum signed coefficient |
|---:|---:|---:|---:|---:|---|
| 0 | 15 | 16 | 0 | 0 | 175693221181/27488622889728000 |
| 1 | 16 | 17 | 0 | 0 | 126716045051/13962475118592000 |
| 2 | 17 | 18 | 0 | 0 | 327615371233/6717219847962624 |
| 3 | 18 | 19 | 0 | 0 | 3114246458797/22490691455232000 |
| 4 | 19 | 20 | 0 | 0 | 9793592991186997/22577322266763264000 |
| 5 | 20 | 21 | 0 | 0 | 327448134232868729/316668935689666560000 |
| 6 | 21 | 22 | 0 | 0 | 2998939805612037593/1741679146293166080000 |

Each minimum equals its polynomial's value at x=1. The certificate retains every monomial coefficient, every Bernstein coefficient, every sign, and the indices attaining each minimum. Checking order for a potential first witness was increasing k, then increasing j. The recorded witness is null.

The sum of row minima is

    Z(1)=19532105792367929/5757617012539392000>0.

Consequently this single control proves Z(x)>=Z(1)>0 throughout [0,1]. Its endpoint is

    D_V=19532105792367929/2149019034696302985216000000,
    Y=-19532105792367929/2149019034696302985216000000.

Both agree exactly with the existing n=6 certificate. This is a proved interval statement at this one frozen control, not an eventual statement.

## Specific next coefficient inequality

The endpoint-minimum observation suggests a stronger, concrete route that can be investigated symbolically. For general even n, b=n/2, set Q_k=sigma_n P_(n,k), sigma_n=(-1)^(b-1), and let gamma_j be its degree-L Bernstein coefficients. The derivative identity is exact:

    Q_k'(x)=L sum_(j=0)^(L-1)(gamma_(j+1)-gamma_j)
                         binom(L-1,j)x^j(1-x)^(L-1-j).

Thus the explicit inequalities

    gamma_(j+1)-gamma_j<=0, 0<=j<L,
    gamma_L>0

would imply every gamma_j>=gamma_L>0 and hence the required positive margins. This proposed monotonicity is stronger than what the successful control established; endpoint attainment of the minimum alone does not prove it.

Writing a_u=[x^u]Q_k, the first inequalities can be expressed directly in the existing rational coefficient data as

    sum_(u=1)^(j+1) u*a_u*binom(j,u-1)/binom(L-1,u-1)<=0,
        0<=j<L.

The left side equals L(gamma_(j+1)-gamma_j). These are definite finite-sum inequalities, suitable for a symbolic argument using the coefficient-minor formula and the actual Volterra recurrence

    r_(k+1)=(J_n-1/2)r_k+[k^2/(4(4k^2-1))]r_(k-1).

No positivity-preserving property of this recurrence is assumed. The previously identified obstruction to such a general property remains valid. Neither these derivative-coefficient inequalities nor their endpoint positivity hypothesis has been proved uniformly here. Failure of this stronger approach would not itself refute the original Bernstein-sign conjecture.

Recommendation: investigate the displayed coefficient differences and endpoint positivity symbolically, with the actual ordered minors retained. Do not extend the degree controls automatically. The present result justifies further work on a specific inequality; it does not supply an induction in n or b.

## Scope and reproducibility

Files in work/session_20261001_astra/agent3/:

- check_bernstein_next_control.py — reproducible exact checker restricted to n=6,b=3.
- bernstein_next_control_certificate.json — full rational polynomials, coefficients, signs, identity checks, and source hashes.
- bernstein_next_control_summary.json — sign counts, minima, and endpoint comparison.
- BERNSTEIN_NEXT_CONTROL.md — this report and next-step recommendation.

The certificate is 31645 bytes, with SHA-256

    2d2597a0c40f5d681912f33cb934d34e324b70fbad7f82cfbdd0397e0c9ebf20

Reproduction from the workspace root:

    python3 work/session_20261001_astra/agent3/check_bernstein_next_control.py --verify

The original execution passed; the verification mode is provided for reproducibility and is not claimed to have been separately executed.

No additional HP indices, primes, networking, installations, or changes to other agents' files were used. Endpoint nonvanishing on an unbounded set and full-remainder nonvanishing remain unresolved. The earlier obstruction to shrinking using the chosen absolute bounds also remains: a successful endpoint sign test cannot rescue that bound ratio through an endpoint gcd.
