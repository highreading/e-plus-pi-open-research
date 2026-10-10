> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of draft observations

Reviewer: Agent 4.

## Verdicts

Draft (A): PASS, as a count and density of the intersection of the two inherited unexcluded conditions.

Draft (B): PASS, as an eventual necessary condition and eventual spacing theorem for any strictly increasing sequence of b=1 indices whose primitive forms tend to zero. The proof and zero-valuation conventions are supplied below. It is not an exclusion of infinite subsequences.

## Draft (A): precise intersection

The inherited reviews establish that a shrinking sequence must eventually satisfy n=15 modulo 16 and the six-prime unresolved condition

n modulo 7 in {2,3}, and at least two of
n modulo 11=2, n modulo 17 in {3,11}, n modulo 19=14.

The second condition consists of 146 classes modulo M=24871. Since gcd(16,M)=1, each such class r has exactly one lift satisfying n=15 modulo 16, modulo 16M=397936. Explicitly its representative is

r+M*((15-r)*M^(-1) modulo 16).

The independent checker constructs these lifts and compares them with direct enumeration on the 15 modulo 16 progression. Both give exactly 146 distinct classes. The natural density among all integers is

146/397936 = 73/198968.

There is no additional parity factor: n=15 modulo 16 already enforces oddness. This is the retained set for precisely these two restrictions. It is not a claim that other established or future restrictions cannot shrink the set, and does not count successful approximants.

## Draft (B): uniform exclusion when the numerator depth is low

Use the actual U_n/Delta_n normalization and bounds proved in INHERITED_SYNTHESIS_REVIEW.md. For odd n>=3 put

f=v_2(n!), ell=floor(log_2(n+1)), c=v_2(Ccal_n), s=s_2(n).

Assume c<=n/2. This assumption entails c finite. The factorial term then has valuation

a=n+1-2f+c <= -n/2+1+2s.

Meanwhile

v_2(Qpart_n)>=(n+7)/2-ell.

Since s<=floor(log_2 n)+1, the difference between the latter lower bound and the former upper bound is at least n+5/2-ell-2s, which is positive for all sufficiently large n, uniformly over every odd index satisfying c<=n/2. Thus the factorial term is uniquely least. The proposed unique-minimum inference is correct only with this eventual qualification, which suffices for the draft.

Consequently

v_2(q_n)>=2f-(n+1)/2+2-c >= n+3/2-2s = n-O(log n).

Because n is odd and c is an integer, c<=n/2 actually means c<=(n-1)/2 and yields the slightly sharper n+2-2s. No such sharpening is needed. The max-with-zero in rational reduction is harmless for this eventual positive bound; eventual Delta_n != 0 is supplied by the accepted analytic theorem.

At the same indices the uniform prime theorem gives

v_5(q_n)>=2v_5(n!), v_13(q_n)>=2v_13(n!).

Hence on the low-c set, uniformly,

log q_n >= L_B n-O(log n),
L_B=log 2+(1/2)log 5+(1/6)log 13.

The exact strict inequality L_B>t=2log(1+sqrt(2)) follows by exponentiating six times:

2^6*5^3*13=104000 > (1+sqrt(2))^12=19601+13860 sqrt(2).

For example sqrt(2)<2 makes the right side less than 47321; the saved checker also verifies the guarded exact squared comparison. This is an exact proof, not a numerical logarithm estimate.

The analytic identity log|L_n|=log q_n-tn+o(n) now supplies constants epsilon>0 and N such that every odd n>=N with c<=n/2 obeys |L_n|>=exp(epsilon n). Constants are independent of which low-c indices occur.

Let n_j be a strictly increasing sequence with |L_(n_j)| tending to zero. The all-even exclusion first makes n_j odd eventually. The uniform bound just proved makes c_(n_j)>n_j/2 eventually. The independently audited outside-disk exclusion further gives n_j=15 modulo 16 eventually. The accepted odd germ on 7 modulo 8 therefore yields

v_2(Ccal_(n_j))=v_2(n_j-nu)>n_j/2,
nu in 15+16 Z_2.

These implications are statements about a tail of every such sequence; they do not assume a uniform rate at which the candidate sequence tends to zero. An infinite collection of excluded indices in that sequence would contradict convergence to zero, because their indices necessarily tend to infinity.

## Zero numerator and valuation conventions

The low-c argument makes no assertion about c=infinity and must not subtract infinities in the unique-minimum calculation. On the exceptional disk, the accepted identity admits v_2(0)=infinity, so the displayed necessary condition remains meaningful even if Ccal_n=0.

The spacing proof below works with this extended valuation convention. If n=nu as a 2-adic equality, then n-nu is divisible by every power of 2. Two distinct ordinary integers cannot both equal nu. Thus even without further information an integer root can affect at most one index in a strictly increasing sequence, and cannot invalidate an eventual conclusion.

There is also a stronger deduction available from the named accepted prime inputs: Ccal_n is nonzero for every integer n>=2. At p=5 the complete seed table makes it a unit outside n=1 modulo 5. On n=1 modulo 5, the reviewed residue-one theorem gives v_5(Ccal_n)=v_5(n-1)<infinity for n>=2. This argument is independent of Delta_n and excludes exact zero. Its use is optional for draft (B); the extended-valuation proof already suffices. This does not establish a Diophantine upper bound for v_2(n-nu) or determine the general arithmetic nature of nu.

## Spacing and its limits

For any two indices n<m in the established tail,

v_2(n-nu)>n/2 and v_2(m-nu)>m/2>n/2.

The ultrametric inequality gives

v_2(m-n)>=min(v_2(m-nu),v_2(n-nu))>n/2.

Since m-n is a positive ordinary integer, this entails

m-n>=2^(floor(n/2)+1).

The retained n are odd, so floor(n/2)+1=ceil(n/2), exactly the draft bound. This holds for all pairs in the tail, in particular successive indices of the sequence. It does not assert anything about a pair straddling the finite discarded prefix. No equality of the two depths is required, and greater cancellation only strengthens the bound.

Exponential spacing alone does not exclude an infinite sequence. For instance an abstract recursively defined increasing sequence can always take its next value greater than n+2^ceil(n/2); spacing is logically compatible with infinitely many indices. This observation does not construct approximants in the present family. The present results prove necessary conditions only, not existence, whole-family failure, or irrationality of e+pi.

## Dependencies and real computation

Draft (A) uses both PASS results in INHERITED_SYNTHESIS_REVIEW.md, including the separately accepted all-even input. Draft (B) uses the exact quotient and odd Delta/Qpart bounds, the accepted odd-germ valuation theorem, the reviewed uniform 5/13 and all-even theorems, and the reviewed fixed-degree analytic theorem at b=1. Their full source paths and accepted scopes are recorded in the inherited review. The optional nonzero-Ccal observation uses the p=5 complete seed table plus hp_b1_residue_one_actual_numerator.md Section 2, as certified by hp_b1_uniform_5_13_independent_review.md.

check_inherited_rates_counts.py executed successfully with exit code 0. audit_rate_count_certificate.json stores all exact rate comparisons and the complete CRT representatives; audit_rate_count_stdout.txt stores the real execution summary. Draft (B)'s new rate comparison returned sign +1; draft (A)'s count and density were independently confirmed. No rerun of the accepted full dyadic-germ computation was needed.
