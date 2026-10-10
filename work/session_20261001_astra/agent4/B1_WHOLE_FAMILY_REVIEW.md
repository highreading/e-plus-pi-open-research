> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the whole b=1 exclusion

Reviewer: Agent 4.
Verdict: PASS, using the explicitly identified, previously reviewed analytic and arithmetic inputs. No mathematical repair required.

The accepted conclusion concerns the endpoint-matched degree-(n,1,n) family for exp(z) and F(z)=4 arctan(z/(2-z)). If q_n is the positive reduced denominator of its rational endpoint and L_n its primitive integer form, then

liminf log(q_n)/n >= W,
liminf log|L_n|/n >= W-2log(1+sqrt(2)) >= 20453/200000 > 0,

where W=sum_{p in {5,13,41,43,59,67}} 2log(p)/(p-1). All limits are as n tends to infinity through all integers in the eventual nonzero-endpoint domain, which contains every sufficiently large integer. Every subsequence with indices tending to infinity therefore has |L_n| tending to infinity. This excludes shrinking in this particular family. It proves neither rationality nor irrationality of e+pi.

## 1. Inspected sources and independent execution

I read Agent 3's PROOF_DRAFT.md, REPORT.md, the entire check_bounded_prime_extension.py, and exact_certificate.json. The original artifacts were preserved. The default author script writes in Agent 3's directory, so I did not invoke its default entry point. Instead I wrote and executed check_whole_family.py in my own directory.

The independent computation returned exit code 0 and all_checks_pass=true. It reconstructed all 67 rational scalar seeds, checked 210 selected residue rows, and compared all 1,050 coordinates against EACH of the two saved constructions. Its real outputs are whole_family_checks.json and whole_family_check_stdout.txt. The input certificate SHA-256 is a422ac8d69dc74d4f15ce26906216ce4ddbf925e0fd60c676b8c6a59c8399e48, matching Agent 3's report.

No additional primes were scanned. The nonselected prime tables are not needed for the exclusion theorem and were not independently recomputed in this audit. The saved rate history was independently checked; its verdicts are below, below, below, below, above. This confirms the rate crossing for the recorded sequence of accepted subsets, without claiming independent historical verification of when a predeclaration was written.

## 2. Complete scalar constructions

Construction I in Agent 3's code correctly multiplies by phi(x)=1-x+x^2/2 modulo p and implements the finite Rodrigues contractions for H,K,Acal,Bcal. Its falling-factorial updates, the separate constant terms K=2 and Bcal=2D_(2n+1), and the determinant Ccal=K Acal-H Bcal are correct. The largest D index is 2p-1, which is included. All rows r=0,...,p-1 are covered, including the boundary r=p-1.

Construction II uses the correct transformed ordinary Legendre formula

L_k(t)=sum_j (2k-2j)!/[j!(k-j)!(k-2j)!] (2t-1)^(k-2j).

The apparent absence of an alternating j sign is correct: the ordinary Legendre sign cancels the powers of i from the change of variable. Both adjacent factorial and exponential-partial-sum functionals use n+j, not k+j. Exact rational normalization is performed before modular inversion, with scales (n!)^2/2^n and (n+1)(n!)^2/2^(n+1). Thus no inversion of n+1 modulo p occurs at r=p-1.

My independent construction uses the integer recurrence

(k+1)L_(k+1)=2(2k+1)(2t-1)L_k+4k L_(k-1),
L_0=1, L_1=4t-2,

rather than the author's explicit binomial expansion or modular polynomial multiplication. Every coefficient division by k+1 was checked exactly. Direct rational factorial functionals and sums of reciprocal factorials then reconstructed the normalized five coordinates for every r=0,...,66. Every saved exact rational coordinate agreed; H,K were integral and all five denominators were powers of two.

Reducing these independently reconstructed coordinates gives complete zero sets

41: {1}; 43: {1}; 59: {1}; 67: {1}.

The row counts are 41+43+59+67=210, giving exactly 5*210=1,050 coordinate positions. All positions agree with both saved arrays. These are exact finite certificates for scalar seeds, not empirical sampling of canonical HP solutions.

## 3. All-index transfer and full-depth root lift

The all-residue transfer in work/session_20260927/hp_b1_prime_seed_transfer_and_closed_atlas.md applies to every odd prime. The D recurrence resets modulo p. If n=r modulo p, the H,Acal sums retain only s<=r; Frobenius reduces the surviving coefficients to those at r. For K,Bcal and r<=p-2 only s<=r+1 survives. At r=p-1, coefficients for 1<=s<p vanish by Frobenius, s=p is killed by 2n+2-s, and s>=p+1 is killed by (n)_(s-1). The constant terms remain. This establishes transfer at the prime boundary without division by a nonunit.

The separate residue-one argument is essential. I checked work/session_20260927/hp_b1_residue_one_actual_numerator.md Sections 1-2, its scope in hp_b1_uniform_5_13_independent_review.md, and the underlying September 13 hp_auxiliary_simple_root_analytic_reduction.md with hp_auxiliary_analytic_reduction_root_review.md.

For R=b+2c, s=b+c, the product of falling factorials divided by 2^c b!c! has Gauss valuation at least k-v_p(k!), k=floor(R/p), tending to infinity. The D interpolants are integral restricted series; on X=1+pY the denominator X+1=2+pY is a unit. This proves convergence of the actual contractions in the restricted series ring.

The first-lift argument retains R in [p,2p); those terms cannot simply be discarded. Its possible quadratic coefficient is proportional to the exact seed value H(1), respectively the adjacent J seed, both zero. The exact index slopes give

H(1+pY)=-3pY/2 mod p^2,
K(1+pY)=4pY mod p^2.

Together with Acal=3 and Bcal=10 modulo p, this gives Ccal(1+pY)=27pY modulo p^2 coefficientwise. Exact vanishing at Y=0 permits division by Y, and Ccal(1+pY)/(pY) has constant reduction 27. Every prime used here is at least 5, so this is a unit everywhere on the disk. Therefore, for actual n>=2 and a=v_p(n-1)>=1,

v_p(Ccal_n)=a, v_p(H_n)>=a, v_p(K_(n+1))>=a.

This holds at every depth a. The finite seed tables alone would not prove it. The inherited auxiliary review's conditional slope qualification is satisfied here by the explicit slopes; no conclusion about other auxiliary residue disks is imported.

## 4. Actual numerator and fully reduced q

The exact endpoint normalization, already checked in my INHERITED_SYNTHESIS_REVIEW.md against the September 13 adjacent-scalar source and review, is

x_n=Ucal_n/Delta_n,
Ucal_n=Qcal_n+2^(n+1)Ccal_n/(n!)^2,
Qcal_n=2K_(n+1)Q_n-(n+1)H_n Q_(n+1),
Delta_n=(n+1)P_(n+1)H_n-2P_n K_(n+1),
Q_k=8 sum_{j=1}^k P_(j-1)P_(k-j)/j.

The signs, fixed n in both adjacent partial sums, and single factor n+1 in the Rodrigues scale are retained. Delta is integral.

Fix p in S and n>=p. Write f=v_p(n!), ell=floor(log_p(n+1)). The convolution gives v_p(Q_k)>=-floor(log_p k). Also 2f>ell: for ell=1 use f>=1; for ell>=2 use 2f>=2(p^(ell-1)-1)>ell.

Outside residue one, Ccal is a unit. The factorial term has valuation -2f, strictly smaller than the Qcal lower bound -ell. Hence v_p(Ucal)=-2f.

On residue one, the full-depth lift gives valuation a-2f for the factorial term and the larger lower bound a-ell for Qcal. Thus v_p(Ucal)=a-2f. Both terms of Delta are divisible by p^a, so v_p(Delta)>=a. These arguments also ensure Ucal is nonzero on their applicable domain.

For Delta!=0, the exact rational reduction formula is

v_p(q_n)=max(0,v_p(Delta_n)-v_p(Ucal_n)).

It gives 2f+v_p(Delta) outside residue one and 2f+v_p(Delta)-a on residue one, each at least 2f. Their nonnegativity justifies removing the maximum. There is no unit assumption on P_n and no substitution of a coefficient clearer for q_n.

Consequently, for n>=67 whenever Delta_n!=0,

product_{p in S} p^(2v_p(n!)) divides q_n.

The previously reviewed 5/13 seeds are used within their accepted scope; my new scalar recomputation covers only 41,43,59,67.

## 5. Endpoint nonvanishing and full signed error

The arithmetic and analytic endpoints are related by the exact identity

delta_n=(-1)^n Delta_n/[2^(n+3)(n!)^2].

The accepted endpoint theorem gives delta_n!=0 eventually. Its explicit b=1 source work/session_20260913/hp_b1_endpoint_attempt.md proves nonzero endpoint for n>=64; the reviewed work/session_20260927/fixed_exponential_degree_error_theorem.md and its independent review also give eventual normality and nonzero endpoint at fixed b=1. Thus no unresolved endpoint-zero subsequence remains at infinity.

The analytic proof treats both full evaluated tails, using R(1)=ell_B(W). Its determinant quotient retains the minus sign and the exact reference factor (-1)^(n+1)epsilon_n. At b=1 its signed conclusion is

(-1)^n R_n(1)/(B_n(1)epsilon_n) -> sqrt(2)-1 >0,
log epsilon_n/n -> -2log(1+sqrt(2)).

Thus the full normalized error is eventually nonzero and has sign (-1)^n. If x_n=u_n/q_n in lowest terms with q_n>0, then

L_n=u_n+q_n(e+pi)=q_n R_n(1)/B_n(1).

Its integer coefficients are primitive because gcd(u_n,q_n)=1. Therefore

log|L_n|=log q_n-2n log(1+sqrt(2))+o(n).

These analytic results are used as named, previously reviewed inputs; this audit checks their specialization, signs, exact normalization, and connection to q. It does not claim a new independent reproduction of every underlying analytic computation or a theorem for b growing with n.

## 6. Exact rate certificate

The positive series 2 sum_{j>=0} z^(2j+1)/(2j+1) equals log((1+z)/(1-z)) for 0<=z<1. The remainder after m terms is bounded above by 2z^(2m+1)/[(2m+1)(1-z^2)]. All range-reduction exponents used for x>=1 are nonnegative, so multiplying log-2 intervals preserves their ordering.

I inspected the author's 16-term exact implementation and independently verified every saved prime logarithm interval and every saved target interval with fresh 32-term rational sums. No floating-point logarithms are used. The exact square-root bracket has d=18446744073709551616 and a=26087635650665564424, with

2d^2-a^2=36478007661041971136>0,
(a+1)^2-2d^2=15697263640289157713>0.

I checked these integer identities and monotonic logarithm bounds. I also recomputed the weighted sums from all saved prime bounds, the differences, coarse outward inequalities, and all five stopping-rate comparisons. They passed. In particular,

W >= 4308181309389547/2310000000000000,
tau <= 44068679351/25000000000,
W-tau >= 236235337357147/2310000000000000 > 20453/200000.

The simpler recorded weakening is W>=1865013/1000000 and tau<=440687/250000. Their difference is exactly 20453/200000. No essential certificate failed.

For this fixed finite S, Legendre's valuation formula supplies a uniform O(log n) error when summing 2v_p(n!)log p. Hence log q_n>=Wn-O(log n) at all sufficiently large indices. Combining it with the full signed error gives the stated positive liminf, with no parity restriction and no interchange over infinitely many primes. For each fixed 0<c<20453/200000, eventually |L_n|>=exp(cn). The endpoint c itself is not asserted as an eventual pointwise exponent merely from a liminf bound.

## 7. Scope and artifacts

PASS is for this whole b=1 family using the named accepted dependencies. The argument does not require controlling the dyadic or ternary exceptional analytic roots. It does not show that infinitely many primes have the selected zero-set property. It does not exclude other degree allocations or other approximation constructions, and it says nothing decisive about rationality of e+pi.

Independent local evidence:

- check_whole_family.py
- whole_family_checks.json
- whole_family_check_stdout.txt

Earlier normalization and analytic dependency details remain in INHERITED_SYNTHESIS_REVIEW.md. All new writes were confined to work/session_20261001_astra/agent4/. No original artifacts, historical links, runtime settings, or security restrictions were changed.
