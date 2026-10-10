> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fixed rational weights cancelling the leading matched error require denominator eight

Status: UNVERIFIED CANDIDATE
Author: worker_4
Content SHA256: 8901aa93f675fbd58e3c5a13b2cb1576cc5166615ac585d5ac05aac0181a3d09

Status: unverified submission requiring independent review.

Hypotheses and definitions. Let T be real and let r_n be rational for all sufficiently large integers n. Set rho=(1+sqrt(2))²=3+2sqrt(2) and z=-rho^(-1)=-3+2sqrt(2). Assume
T-r_n=Cz^n(1+epsilon_n), where C>0 is fixed and epsilon_n tends to zero.
Fix a finite J≥0 and rational weights w_0,...,w_J independent of n, with sum w_j=1. Define s_n=sum_j w_j r_(n+j), W(x)=sum_j w_j x^j, and let d be the least positive common denominator of the weights. Then P=dW belongs to Z[x] and P(1)=d.

Claims.
1. T-s_n=Cz^n(W(z)+o(1)). The leading term cancels exactly when g(x)=x²+6x+1 divides P in Z[x]. Cancellation therefore requires 8|d. In particular, fixed integer weights summing to one cannot cancel this leading term. Without cancellation, log|T-s_n|/n tends to -log(rho).
2. Among rational weights on the three shifts n,n+1,n+2, the unique weights preserving T and cancelling the leading term are (1,6,1)/8. They attain the smallest possible common denominator across all finite rational weight vectors admitting cancellation. The resulting error is o(rho^(-n)).
3. If q_n is the positive reduced denominator of r_n, the reduced denominator of this three-term filter divides 8 lcm(q_n,q_(n+1),q_(n+2)). This does not determine its cancellation gcd.
4. The hypotheses do not imply a better exponential rate after this filter. This remains true upon imposing q_n≥(3sqrt(5))^n/(1125n^4): an explicit rational example below has filtered error asymptotic to a nonzero constant times z^n/n², and its denominator times absolute error diverges.

Proof of claims 1 and 2. Since the number of shifts and all weights are fixed,
T-s_n=Cz^n[sum_j w_j z^j+sum_j w_j z^j epsilon_(n+j)].
The second sum tends to zero. Thus leading cancellation is equivalent to W(z)=0. The polynomial g has discriminant 32, which is not a rational square, and is the minimal polynomial of z over Q. Divide P by the monic integer polynomial g using polynomial long division: P=gQ+R with Q,R in Z[x] and deg R<2. If P(z)=0, then R(z)=0; irrationality of z forces R=0. The converse is immediate. Evaluating P=gQ at 1 gives d=P(1)=8Q(1), proving 8|d. For integer weights d=1, cancellation is impossible. If W(z) is nonzero, the absolute error is C|W(z)|rho^(-n)(1+o(1)), which proves the logarithmic rate.
For degree at most two, any rational polynomial vanishing at z is a rational scalar multiple of g. The condition W(1)=1 forces W=g/8. Its least common coefficient denominator is exactly eight, so the necessary lower bound is attained. This uniqueness concerns rational weights; no uniqueness over arbitrary real weights is asserted. Divisibility 8|d alone is not a sufficient cancellation criterion for a specified vector.

Proof of claim 3. Write r_(n+j)=p_(n+j)/q_(n+j) in lowest terms with positive denominators. Put L=lcm(q_n,q_(n+1),q_(n+2)) and
U=p_n L/q_n+6p_(n+1)L/q_(n+1)+p_(n+2)L/q_(n+2).
Then s_n=U/(8L), so its positive reduced denominator is exactly 8L/gcd(|U|,8L). This includes U=0, whose reduced denominator is one. No estimate of this gcd for the matched family is supplied here.

Proof of claim 4 by a rational counterexample. Take T=0 and any fixed C>0. For n≥1 set
t_n=-C·7^n·z^n(1+1/n),
a_n=1+7 floor((t_n-1)/7), and r_n=a_n/7^n.
Then a_n≡1 mod7 and 0≤t_n-a_n<7. Consequently r_n is reduced with q_n=7^n, and
T-r_n=Cz^n(1+1/n)+O(7^(-n))=Cz^n(1+o(1)),
because 7>rho. Also 7>3sqrt(5), so the stated individual denominator lower bound holds for every n≥1.
For s_n=(r_n+6r_(n+1)+r_(n+2))/8, use g(z)=0 and the exact identity
1/n+6z/(n+1)+z²/(n+2)=((2+6z)n+2)/(n(n+1)(n+2)).
It follows that
T-s_n=(Cz^n/8)·((2+6z)n+2)/(n(n+1)(n+2))+O(7^(-n)).
Since 2+6z=12sqrt(2)-16>0, this is asymptotic to C(2+6z)z^n/(8n²). Hence the logarithmic exponential rate remains -log(rho).
The numerator of s_n over 8·7^(n+2) is U_n=49a_n+42a_(n+1)+a_(n+2), which is 1 modulo seven. Its positive reduced denominator therefore contains 7^(n+2). Thus that denominator multiplied by |T-s_n| tends to infinity, since (7/rho)^n/n² tends to infinity.

Application and source dependencies. The algebraic claims above depend only on their explicitly stated asymptotic hypothesis. For the matched b=2 approximants r_n=-X_n/D_n to T=e+pi, the previously audited published transfer and endpoint identification supply this eventual hypothesis with C=4pi/(1+sqrt(2))³. Relevant records are work/astra_review_registry/verified/worker2-fixed-b-projection-and-error-transfer-v2.md and work/astra_review_registry/verified/w3-b2-eventual-d-nonzero-v1.md. The family denominator bound appears in work/astra_review_registry/verified/w3-b2-whole-family-obstruction-v1.md with its preserved hypotheses. The initial fixed-weight derivation is saved in work/astra_20260929/worker_4/note_000168.md. No effective analytic threshold or renewed audit of those dependency proofs is claimed in this submission.

Scope and unresolved issues. These statements concern a fixed finite set of rational weights applied to normalized approximants. They do not cover weights or numbers of shifts varying with n, or combinations of integer forms carrying index-dependent denominators. The constructed rational example establishes a limitation of the quantitative hypotheses and is not asserted to satisfy the matched endpoint equations. For the actual filtered matched approximants, further asymptotic information and control of the reduced denominator remain necessary to decide whether their integer forms shrink. No conclusion about the rationality of e+pi follows. Author verification is complete; independent approval remains outstanding.