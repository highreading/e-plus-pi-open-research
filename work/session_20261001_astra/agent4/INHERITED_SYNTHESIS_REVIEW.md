> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent inherited synthesis review

Reviewer: Agent 4. Scope: the two September 27 previously unmerged deductions only.

## Verdicts

1. hp_b1_odd_dyadic_actual_numerator.md, Section 3: PASS.
2. hp_b1_closed_prime_odd_index_restriction.md: PASS.

These verdicts certify the transfers and finite synthesis below using the explicitly identified accepted inputs. They do not extend either result to a whole-family exclusion.

## Actual quotient, signs, scales, and nonvanishing

The September 13 adjacent-scalar source and its independent review give

X/Y = [R_(n+1) S_n - R_n S_(n+1)]/[P_(n+1) R_n - P_n R_(n+1)],
R_n = 2^n H_n/(n!)^2,
R_(n+1) = 2^(n+1) K_(n+1)/[(n+1)(n!)^2].

Consequently X/Y = U_n/Delta_n, with

Delta_n = (n+1) P_(n+1) H_n - 2 P_n K_(n+1),
U_n = Qpart_n + 2^(n+1) Ccal_n/(n!)^2,
Qpart_n = 2 K_(n+1) Q_n - (n+1) H_n Q_(n+1),
Ccal_n = K_(n+1) Acal_n - H_n Bcal_n.

The Rodrigues calculation in the ternary source retains E_(n+j) for both adjacent indices. Its scales are 2^n/(n!)^2 and 2^(n+1)/[(n+1)(n!)^2]; these give precisely the displayed factorial term, including its sign. K is the b=1 integral quantity J_k/k. No coefficient clearer replaces q_n.

The original endpoint difference satisfies delta = (-1)^n Delta_n/[2^(n+3)(n!)^2]. Thus eventual nonzero endpoint in the accepted fixed-degree theorem, specialized to b=1, implies eventual Delta_n != 0 in this arithmetic normalization. That theorem and its review also give the full evaluated-error identity

log|L_n| = log q_n - t n + o(n),  t = 2 log(1+sqrt(2)).

This is an all-index asymptotic at fixed b=1, with eventual nonzero error; it is not a first Taylor coefficient estimate or a growing-b theorem.

For Delta_n != 0, rational reduction gives exactly

v_p(q_n) = max(0, v_p(Delta_n) - v_p(U_n)).

This follows equally from the integer clearing convention N_n=(2n+1)! U_n. Infinite numerator valuation gives denominator 1. The unique-minimum arguments below ensure finite U_n in their applicable ranges.

## Dyadic transfer, including small factors

The exact sum

P_k = sum_(j=0)^floor(k/2) 2^(k-j) binom(k,2j) binom(2j,j)

gives v_2(P_k) >= ceil(k/2) for every k>=0. In particular P_0=1 and P_1=2 satisfy this weaker bound; the stronger bound must not be applied to them. For k>=2, the j=0 term has valuation k>=ceil(k/2)+1; every j>=1 gains a factor 2 from its central binomial coefficient. Hence v_2(P_k)>=ceil(k/2)+1 for k>=2.

The exact second-kind normalization is Q_k=8 sum_(j=1)^k P_(j-1)P_(k-j)/j. Using the weaker bound for all factors, including P_0 and P_1, proves

v_2(Q_k)>=3+ceil((k-1)/2)-floor(log_2 k), k>=1.

For odd n=2r+1>=3 both P_n and P_(n+1) admit the stronger bound. The factor n+1 in the first Delta term and the explicit factor 2 in its second term show

v_2(Delta_n)>=r+3=(n+1)/2+2.

Let ell=floor(log_2(n+1)), f=v_2(n!), and c=v_2(Ccal_n). Integrality of H,K and the Q bound give the useful uniform estimate

v_2(Qpart_n)>=r+4-ell=(n+7)/2-ell.

Indeed its first term has the extra factor 2, and its second term has v_2(n+1)>=1. No unit assumption on H or K is needed.

The accepted odd-germ theorem yields, outside n=15 modulo 16 and excluding the isolated small n=1,

c=v_2(n-1) on n=1 modulo 8;
c=2 on n=3 or 5 modulo 8;
c=3 on n=7 modulo 16.

Thus c=O(log n) uniformly on this union. With s_2(n) the binary digit sum, f=n-s_2(n), so the factorial term has valuation

n+1-2f+c = -n+1+2s_2(n)+c = -n+O(log n).

It is strictly below the Qpart bound for every sufficiently large index in this union. Therefore v_2(U_n)=n+1-2f+c, and actual rational reduction gives

v_2(q_n)>=2f-(n+1)/2+2-c = 3n/2-O(log n).

The lower bound is eventually positive. Before that point the exact max-with-zero formula remains necessary; no small-index equality is claimed here.

The accepted uniform 5/13 theorem applies at the SAME n and to the SAME reduced q_n. Adding the three prime contributions gives the uniform lower rate

L_*=(3/2)log 2+(1/2)log 5+(1/6)log 13 > t.

The exact comparison is 832000>(1+sqrt(2))^12. Combined with the analytic error asymptotic, it yields a positive exponential lower rate uniformly on the stated odd union. The separately accepted all-even theorem uses this same rate. Together these results exclude shrinking outside n=15 modulo 16, eventually and uniformly. They do not resolve that exceptional disk.

## Six-prime threshold and CRT synthesis

Accepted prime inputs give v_p(q_n)>=2v_p(n!) eventually for p=5,13 everywhere, and for the other four primes outside

B_7={2,3}, B_11={2}, B_17={3,11}, B_19={14}.

These sets follow from the reviewed complete seed table and the separately reviewed all-depth residue-one lift. In particular residue 1 is good; it must not be left in the bad sets. Bad means unresolved by this certificate, not a proved small denominator.

Write b_0=(1/2)log 5+(1/6)log 13 and w_p=2log p/(p-1). The independently executed exact checker verifies

b_0+w_7>t,
b_0+w_17+w_19>t,
b_0+w_11<t.

The comparisons use the integer powers at exponents 6,72,30 and exact arithmetic in Z[sqrt(2)]. When the integer left side is at most the rational part A of A+B sqrt(2), the sign is immediately negative; squaring is used only after checking a positive difference. The old certificate and all three comparisons agree with the independent computation.

The function log x/(x-1) decreases for x>1: log x>1-1/x proves the derivative is negative. Hence among 11,17,19 even the largest single weight is insufficient, while the two smallest together suffice. Precisely the combinations with 7 good or at least two of 11,17,19 good exceed t using this mandatory divisor alone.

There are finitely many combinations. Factorial valuation errors are uniformly O(log n) for this fixed prime list; their strict margins have a positive finite minimum. Together with the all-index analytic o(n), this proves a single eventual positive exponential lower bound across the excluded union. There is no invalid passage from unrelated pointwise liminf statements.

The remaining condition is 7 bad and at least two of 11,17,19 bad. The latter count modulo 11*17*19 is

1*2*18 + 1*15*1 + 10*2*1 + 1*2*1 = 36+15+20+2 = 73.

Multiplying by the two bad residues at 7 gives 146 classes modulo 24871. Independent complete residue enumeration confirms this count. Parity is independent of the odd modulus, so restricting to odd indices leaves density 146/24871 among odd integers and 146/49742 among all integers. All-even exclusion is a separate accepted input to the latter interpretation.

This is the density of an unexcluded index set, not the density of successful approximants. The bound below threshold on a retained combination gives no upper bound on q_n and no existence of shrinking forms.

## Dependencies and reproducibility

Read and used directly:

- work/session_20260913/hp_b1_adjacent_scalar_valuation_gate.md and hp_b1_adjacent_scalar_independent_review.md: exact endpoint and delta scales.
- work/session_20260927/hp_b1_ternary_actual_denominator.md and its independent review: actual Rodrigues normalization.
- hp_b1_dyadic_numerator_and_six_class_exclusion.md and hp_b1_dyadic_independent_root_review.md: accepted dyadic bounds and the narrower original exclusion.
- hp_b1_odd_dyadic_actual_numerator.md Sections 1–3 and hp_b1_odd_dyadic_germs_independent_review.md: accepted coefficientwise odd-germ valuations; Section 3 is the newly audited transfer.
- hp_b1_prime_seed_transfer_and_closed_atlas.md, hp_b1_residue_one_actual_numerator.md Sections 1–2, and hp_b1_uniform_5_13_independent_review.md: accepted closed-prime seeds, full-depth residue-one lift, uniform primes, and all-even exclusion. The ternary-root portions of the residue-one source are not used or newly certified.
- fixed_exponential_degree_error_theorem.md and fixed_exponential_degree_error_independent_review.md: accepted eventual normality/nonzero endpoint and full evaluated error, used only at b=1.
- hp_b1_closed_prime_odd_index_restriction.md, its exact checker, and its certificate: newly audited finite synthesis.

Unless otherwise prefixed, the last entries are under work/session_20260927/. Earlier analytic/germ inputs are accepted at their named reviewed scopes; this audit does not claim a fresh reconstruction of their underlying full computations.

Local checker: check_inherited_rates_counts.py.
Real outputs: audit_rate_count_certificate.json and audit_rate_count_stdout.txt.
Execution returned exit code 0 with all_checks_pass=true. The independent computation used binary powering, exact comparisons, finite residue enumeration, and CRT lifting. No canonical HP degrees or new primes were computed, and the accepted full dyadic-germ computation was not rerun.
