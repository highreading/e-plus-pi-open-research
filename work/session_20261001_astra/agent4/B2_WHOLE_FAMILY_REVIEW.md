> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the whole b=2 exclusion

Reviewer: Agent 4.
Overall verdict: PASS within the explicitly identified inherited theorem scopes. No mathematical repair is required.

| Component | Verdict | Accepted scope |
|---|---|---|
| Normalization and common factor | PASS | Exact identities over Q, including V=(n+1)Vtilde and cancellation in the complete endpoint quotient |
| All-index normalized transfer | PASS | Every odd prime and every residue, including p-1 |
| Ternary theorem and refinement | PASS | n>=3 on the nonzero-endpoint domain; exact factorial depth on residues 0 and 2, an additional lower-bound factor 3 on residue 1 |
| New normalized seeds at 7 and 11 | PASS | All 18 residue rows; both vectors have no zero |
| Whole-family synthesis | PASS | Eventual exponential growth of the primitive forms in this specific endpoint-matched degree-(n,2,n) family |

The central conclusion is

    liminf_(n->infinity) log|L_n|/n >= W-tau > log(27/25) > 2/27,
    W=log 3+(log 7)/3+(log 11)/5,
    tau=2log(1+sqrt(2)).

The limit runs through all sufficiently large integer indices. In particular |L_n|>=exp(n/27) eventually. The threshold is not claimed effective. This excludes shrinking subsequences of this construction; it does not decide rationality or irrationality of e+pi.

## 1. Exact endpoint normalization

Use t=n+1, f=2^n/(n!)^2, and

    H_n(x)=n![z^n] exp(xz)(1-z+z^2/2)^n,
    h=H_n(1), u=H'_n(1), v=H''_n(1), J=nh+u.

Here K_j means the b=2 second derivative of x^j H_j(x) at x=1. It is distinct from the b=1 scalar J_j/j. The scalar C below is the b=2 contiguous endpoint scalar.

The underlying transition can be derived directly from coefficient extraction. Differentiation with respect to x gives

    H'_(n+1)=t(H_n-H'_n+H''_n/2).

Differentiating exp(xz)(1-z+z^2/2)^(n+1) with respect to z gives

    H_(n+1)=xH''_n/2+(t-x)(H'_n-H_n).

Differentiating the second identity and subtracting the first yields

    xH'''_n+(n+2-2x)H''_n+2(x-1)H'_n-2nH_n=0.

At x=1, H'''_n(1)=2nh-nv. Therefore the transition is exactly

    a=H_(n+1)(1)=-nh+nu+v/2,
    H'_(n+1)(1)=t(h-u+v/2),
    H''_(n+1)(1)=t(nh+u-(n+2)v/2).

This agrees with the September 27 transition and its review. Only polynomial identities are used; its large-prime invertibility and maximal-minor theorems are not applied at small primes.

Define

    k=(1-n)h+(n-1)u+v,
    ell=(-n^2+3n+2)h+(n^2-2n-1)u+nv.

Substitution into the derivative definitions gives J_(n+1)=t k and K_(n+1)=t ell. Consequently, with the original S,W,C conventions,

    S=J_(n+1)^2-aK_(n+1)=t sigma,
    W=J_(n+1)J-K_(n+1)h=t omega,
    sigma=t k^2-a ell,
    omega=kJ-ell h,
    C=(t k-a)J-t(ell-k)h.

These are exact identities, not divisibility inferred from modular data.

Integrality is justified independently of division by t. Write a_s(n)=[z^s](1-z+z^2/2)^n. The coefficient of x^(n-s) in H_n is (n)_s a_s(n). A trinomial term with c quadratic factors has an integer multinomial coefficient divided by 2^c, with s>=2c. The consecutive product (n)_s contains at least c even factors. Thus H_n has integer coefficients, and v is even. The displayed a,k,ell,sigma,omega,C are integers.

The partial-exponential contractions use E_(n+j) at BOTH adjacent polynomial indices. The September 27 Rodrigues formulas give exactly

    T_P=f Acal_n,
    T_U=(2f/t) Bcal_n,

where

    Acal_n=sum_(s=0)^n (n)_s a_s(n)D_(2n-s),
    Bcal_n=2D_(2n+1)
      +sum_(s=1)^(n+1) (n)_(s-1)(2n+2-s)a_s(n+1)D_(2n+1-s),
    D_j=j! E_j.

The second scale contains precisely one t. In its coefficient calculation, the s=0 multiplier is (n!/(n+1)!)(2n+2)=2; for s>=1 the multiplier is (n)_(s-1)(2n+2-s). This explains the separate constant term and avoids any local division by t in the contraction formula.

The September 13 contiguous endpoint source, Sections 1-3, and its review supply the complete original quotient

    X/Y=Xcal/Dcal,
    Xcal=2(w_P+T_P)S-t^2(w_U+T_U)C-2f a W,
    Dcal=t^2 P_(n+1)C-2P_n S.

The necessary last term -2f a W is retained. Define

    Vtilde=sigma Acal-C Bcal-a omega,
    Qtilde=2w_P sigma-t w_U C,
    Dtilde=t P_(n+1)C-2P_n sigma.

Then direct substitution gives

    V=S Acal-t C Bcal-a W=t Vtilde,
    Xcal=t(Qtilde+2f Vtilde),
    Dcal=t Dtilde.

Since t is a nonzero ordinary integer, cancellation over Q proves

    X/Y=(Qtilde+2^(n+1)Vtilde/(n!)^2)/Dtilde.

This is the actual rational endpoint, with the entire second-kind part present. It does not invert t modulo p. Dtilde is integral, while Vtilde is in Z[1/2]. No assertion of minimality of this normalization is needed.

For an additional exact scale check, use the raw cross product whose high row is formed from integer L_(n+1), as in the contiguous source. Its rational minors have scales g^2 S, gf C, gf W, where g=2f/t^2, and its Wronskian is G=(-1)^n 2^(2n+3)/t. Hence

    Y_raw=gf Dcal/(G t^2)
         =(-1)^n Dtilde/[4t^2(n!)^4].

Thus Y_raw!=0 is exactly Dtilde!=0. Switching to the monic high row only changes a nonzero common projective scale. The independent checker verified both endpoint determinant identities, their scalar scales, and this relation in the existing scalar controls.

## 2. Transfer at every residue

For d=0,1,2, coefficient extraction gives

    H_n^(d)(1)=sum_(s=0)^(n-d) (n)_(s+d) a_s(n),

with an empty sum equal to zero. For n=mp+r, 0<=r<p, every term with s+d>r vanishes modulo an odd p. The surviving terms have s<p. Frobenius gives

    (1-z+z^2/2)^n
      =(1-z+z^2/2)^r (1-z^p+z^(2p)/2)^m modulo p,

so each surviving coefficient and falling factorial reduces to its seed-r value. This proves transfer of h,u,v, including residues r<d.

The recurrence D_j=jD_(j-1)+1 resets to 1 at multiples of p, proving D_j=D_(j mod p) modulo p. Only s<=r survives in Acal, and all remaining factors agree with the seed formula.

For Bcal, if r<=p-2, only s<=r+1<p survives. Its surviving D indices reduce to the nonnegative seed indices. At r=p-1 there are three separate cases:

- 1<=s<p: a_s(n+1)=0 modulo p by Frobenius.
- s=p: the factor 2n+2-s is divisible by p.
- s>=p+1: the falling factorial (n)_(s-1) is divisible by p.

Only 2D_(2n+1) remains, exactly as at the seed r=p-1. This proves the boundary case without dividing by n+1.

Every normalized scalar is a polynomial over Z[1/2] in n,h,u,v,Acal,Bcal. Therefore

    Vtilde_n=Vtilde_(n mod p) modulo p

for every odd p and every n>=0. This is an all-index proof by controlled finite sums. It is not inferred from a finite set of lifted indices. The original V=t Vtilde is a different scalar; its boundary zero does not transfer to the normalized scalar.

## 3. Independent complete seeds at exactly 3,7,11

I inspected the main-agent checker and Agent 1's normalized checker before the independent execution. Neither original program was executed or modified by this audit. The independent program uses two constructions:

1. Trinomial coefficients over Q for H_n and its derivatives, with direct finite sums for D_j and the Rodrigues contractions.
2. The explicit transformed ordinary Legendre expansion, followed by rational factorial-derivative functionals and direct exponential partial sums. Original S,W,C,V are constructed first; division by r+1 is then performed over Q.

The second route does not use Agent 1's Legendre recurrence. Both routes agree in all 13 normalized state coordinates for the 11 distinct seeds r=0,...,10. The corresponding saved exact states and endpoint scalars agree with Agent 1's certificate. The main-agent ternary states also agree.

The ternary derivative states (h,u,v) are (1,0,0), (0,1,0), and (1,-2,2). The decisive exact data are:

| r | Acal | Bcal | a | sigma | C | omega | Vtilde |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 3 | 0 | 1 | -1 | -2 | 4 |
| 1 | 3 | 10 | 1 | 2 | -1 | 0 | 16 |
| 2 | 21 | 133 | -5 | 53 | -33 | -10 | 5452 |

All three Vtilde values are 1 modulo 3. Their original V values are respectively 4,32,16356, consistent with the exact removed factor.

The complete normalized vectors, ordered by r=0,...,p-1, are

    p=3:  1,1,1
    p=7:  4,2,6,4,4,6,3
    p=11: 4,5,7,8,3,4,2,7,2,5,5.

Every entry is nonzero. All 18 rows at 7 and 11 match the saved modular states, including both normalized denominator coefficients and endpoint seed values. Together these are 21 complete residue rows at the three authorized primes.

The computation also verifies nine existing raw endpoint controls at n=2,...,10 and twelve applicable actual-denominator valuation checks within those scalar controls. These checks support normalization; the infinite-index theorem follows from the proofs, not those controls. In particular the 11-adic all-index conclusion does not depend on an additional sampled index n>=11.

No prime-13 verdict is supplied, and no 5-adic lifting is audited. Agent 1's other seed claims are outside this PASS.

## 4. Second-kind separation and full rational reduction

The exact moment is

    mu_j=((1+i)^(j+1)-(1-i)^(j+1))/(i 2^j(j+1)).

Its numerator after division by i is an integer. Hence for odd p,

    v_p(mu_j)>=-v_p(j+1).

The divided-difference polynomials defining w_P and w_U have integer coefficients and degrees at most n-1 and n. It follows, with ell_p=floor(log_p(n+1)), that

    v_p(w_P),v_p(w_U)>=-ell_p,
    v_p(Qtilde)>=-ell_p.

The latter uses integrality of sigma,t,C. No assertion that the moments or second-kind values are integers is made. Direct moment integration and the exact second-kind convolution also agreed in the finite independent controls.

For every odd p and n>=p, put F_p=v_p(n!). Then

    2F_p>ell_p.

If ell_p=1, use F_p>=1. If ell_p>=2, then n>=p^ell_p-1 and

    2F_p>=2 floor(n/p)>=2(p^(ell_p-1)-1)>ell_p.

The last strict inequality holds already at p=3, ell_p=2 and increases thereafter. Thus all thresholds used in the argument are justified.

Let

    Ntilde=Qtilde+2^(n+1)Vtilde/(n!)^2,
    Rtilde=Vtilde+(n!)^2 Qtilde/2^(n+1).

For the selected primes the all-index seed theorem makes Vtilde a p-unit. The second summand of Rtilde has valuation at least 2F_p-ell_p>=1. Therefore Rtilde is a unit, Ntilde is nonzero, and

    v_p(Ntilde)=-2F_p.

For Dtilde!=0, the positive reduced denominator of Ntilde/Dtilde satisfies the exact rational identity

    v_p(q_n)=max(0,v_p(Dtilde)-v_p(Ntilde)).

Equivalently, when Rtilde!=0,

    v_p(q_n)=max(0,2F_p+v_p(Dtilde)-v_p(Rtilde)).

If Rtilde=0 the endpoint fraction is zero and q_n=1; that possibility is excluded here by the proved unit. Because Dtilde is an integer, its finite valuation is nonnegative. Consequently

    v_p(q_n)=2v_p(n!)+v_p(Dtilde_n)>=2v_p(n!)

for each p=3,7,11, whenever n>=p and Dtilde_n!=0.

This includes all numerator cancellation and final reduction. It requires no unit hypothesis on a Legendre endpoint. A larger valuation of the nonzero Dtilde increases the reduced-denominator exponent in this situation.

The inequality 2F_p>ell_p is not asserted at n=p-1. The inherited theorem p does not divide q_(p-1) is therefore consistent with this result. The independent existing boundary controls at n=2,6,10 confirm that consistency at 3,7,11; no small-index extension is inferred.

## 5. Exact ternary refinement

The integer Legendre endpoint generating function is

    G(z)=sum P_n z^n=(1-4z-4z^2)^(-1/2).

Modulo 3, put A(z)=1-z-z^2. Since A G^2=1 and G(z)^3=G(z^3), multiplication gives G(z)=A(z)G(z^3). Thus

    P_(3m)=P_m,
    P_(3m+1)=2P_m,
    P_(3m+2)=2P_m modulo 3.

All digit factors are nonzero and P_0=1, so every P_m is a ternary unit. Substituting the proved seed values of sigma and C into Dtilde gives

    Dtilde_(3m)=2P_m,
    Dtilde_(3m+1)=0,
    Dtilde_(3m+2)=P_m modulo 3.

For the last residue the coefficient of P_(n+1) vanishes, so no unsupported replacement of P_(3m+3) by a multiple of P_m is used.

It follows that Dtilde is nonzero on residues 0 and 2. For n>=3 the exact reduced-denominator consequences are

    v_3(q_n)=2v_3(n!)                 if n=0 or 2 modulo 3,
    v_3(q_n)>=2v_3(n!)+1             if n=1 modulo 3 and Dtilde_n!=0.

On residue 1 the argument proves divisibility of Dtilde, not its exact positive depth. Eventual nonvanishing on that residue is retained as an analytic dependency. No all-depth denominator refinement is claimed there.

## 6. Analytic domain and whole-family rate

I inspected the September 13 b=2 endpoint theorem and its independent review, and retained the previously read September 27 fixed-b theorem and review at exactly b=2. They establish eventual projective uniqueness and nonzero endpoint. The exact Y_raw/Dtilde scale in Section 1 therefore supplies Dtilde_n!=0 for every sufficiently large n.

The analytic theorem treats the complete evaluated remainder. Its exact projection identity is R(1)=ell_B(W), incorporating both entire tails. In the b=2 determinant proof the two limiting derivative constants are

    d_V=1+1/sqrt(2), d_W=1/sqrt(2).

The additional determinant is smaller than the main remainder by O(n^4 V(0)/n!), tending to zero. The exact reference ratio retains (-1)^(n+1)epsilon_n and the minus sign in R/Y. The two limiting positive factors each equal sqrt(2)-1. Hence

    (-1)^n R_n(1)/(Y_n epsilon_n)->(sqrt(2)-1)^2>0,
    log epsilon_n/n->-tau.

This gives eventual remainder nonvanishing and sign (-1)^n for R_n(1)/Y_n. It does not follow merely from a first omitted Taylor coefficient. The fixed-b theorem gives the same conclusion, with no growing-b inference.

Write the actual endpoint in lowest terms as u_n/q_n, q_n>0. Then

    L_n=u_n+q_n(e+pi)=q_n R_n(1)/Y_n,
    gcd(u_n,q_n)=1,
    log|L_n|=log q_n-tau*n+o(n).

Thus q_n here already includes every polynomial scaling and endpoint gcd.

For n>=11 on the nonzero-endpoint domain, the three independently proved prime bounds concern the SAME q_n. Therefore

    3^(2v_3(n!)) 7^(2v_7(n!)) 11^(2v_11(n!)) divides q_n.

Legendre's factorial valuation formula gives v_p(n!)=n/(p-1)+O(log n). The prime list is fixed and finite, so the summed error is uniform and

    log q_n>=Wn-O(log n).

There is no residue-combination or subsequence qualification in this bound.

The proposed sufficient rate argument is correct. Its exact rational margins are

    7-(3/2)^3=29/8>0,
    11-(3/2)^5=109/32>0,
    (3/2)^2-2=1/4>0.

Monotonicity of logarithms therefore gives

    W>log 3+2log(3/2)=log(27/4),
    tau<2log(5/2)=log(25/4),
    W-tau>log(27/25).

Finally

    log(27/25)=integral_25^27 (1/x) dx > (27-25)/27=2/27,

because the integrand is strictly greater than 1/27 on [25,27). The strictness is justified on an interval of positive length. No numerical logarithms are needed or used.

Combining the simultaneous arithmetic bound with the full analytic identity proves

    liminf log|L_n|/n>=W-tau>log(27/25)>2/27.

For every fixed c<W-tau there is an eventual pointwise bound |L_n|>=exp(cn). In particular c=1/27 gives the stated convenient consequence. Neither the exact exponent W-tau itself as an eventual pointwise bound nor a numerical starting index follows merely from the liminf statement. The arithmetic cutoff n>=11 must not be confused with the unknown common analytic and exponential-growth threshold.

Every subsequence whose indices tend to infinity consequently has primitive forms growing in absolute value. This result excludes this endpoint-matched b=2 construction as a source of shrinking primitive forms. It makes no rationality assertion about e+pi and excludes no other construction by itself.

## 7. Evidence, dependencies, and preserved scope

The independent execution completed with exit code 0 and status PASS_INDEPENDENT_EXACT_CHECKS. It verified 14 formal identities, 11 distinct scalar seeds, all 21 residue rows, nine existing raw endpoint controls, and twelve applicable finite actual-denominator checks. The saved execution summary was read back successfully.

Local evidence under work/session_20261001_astra/agent4/:

- check_b2_whole_family.py
- b2_whole_family_checks.json
- b2_whole_family_check_stdout.txt
- B2_WHOLE_FAMILY_REVIEW.md

The certificate records the full independent states and residue rows, exact endpoint controls, rational rate margins, and hashes of its inputs and preserved b=1 artifacts. The original main-agent and Agent 1 programs and certificates were unchanged. The completed b=1 review documents, checkers, and results were unchanged.

Sources inspected for this audit or retained from the completed earlier audit:

- work/session_20261001_astra/B2_COMMON_FACTOR_TERNARY_DRAFT.md, check_b2_common_factor_ternary.py, and B2_COMMON_FACTOR_TERNARY_CHECKS.json.
- work/session_20261001_astra/agent1/NORMALIZED_PRIME_SEEDS.md, NORMALIZED_REPORT.md, check_normalized_prime_seeds.py, and the relevant exact and 7/11 sections of normalized_prime_seed_certificate.json.
- work/session_20261001_astra/B2_RATE_SYNTHESIS_DRAFT.md and B2_RATE_COMPARISONS.json.
- work/session_20260913/hp_b2_contiguous_endpoint_arithmetic.md and hp_b2_contiguous_endpoint_independent_review.md: actual endpoint determinants, signs, derivative scales, and nonzero-endpoint qualification.
- work/session_20260913/hp_b2_endpoint_attempt.md and hp_b2_independent_review.md: eventual endpoint and full signed remainder theorem.
- work/session_20260927/hp_b2_cubic_maximal_minor_gate.md Section 2 and its independent review: polynomial derivative transition only.
- work/session_20260927/hp_b1_ternary_actual_denominator.md Sections 1-2, hp_b1_prime_seed_transfer_and_closed_atlas.md Section 2, and hp_b1_uniform_5_13_independent_review.md: shared Rodrigues contractions and their residue transfer, not a b=1 reduced-denominator conclusion.
- work/session_20260927/fixed_exponential_degree_error_theorem.md and fixed_exponential_degree_error_independent_review.md: accepted analytic theorem specialized to fixed b=2.

The analytic results remain named accepted dependencies; this review checks their specialization, nonvanishing, signs, and connection to the actual normalized arithmetic quotient. It does not claim a new proof of all prior analytic infrastructure.

No unused 5-adic lift, prime-13 theorem, larger prime search, or new canonical HP degree scan is included. All new writes are confined to the assigned Agent 4 directory. No networking, external paths, installations, historical-link restoration, or security changes were used.
