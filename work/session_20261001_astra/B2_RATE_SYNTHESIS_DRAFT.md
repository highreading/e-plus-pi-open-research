> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Proposed b=2 whole-family rate synthesis

Status: exact elementary rate argument; the new b=2 arithmetic inputs remain pending independent audit. This note does not itself accept a whole-family theorem.

Let q_n be the actual reduced endpoint denominator for the degree-(n,2,n) family. The main-agent common-factor draft proposes a uniform bound at p=3. Agent 1's completed normalized seed report proposes the same bound at p=7 and p=11:

    v_p(q_n)>=2v_p(n!)

for n>=p on the nonzero-endpoint domain. If these inputs pass independent review, the accepted fixed-b endpoint theorem supplies that domain eventually, and all three divisors concern the same q_n.

Legendre's factorial valuation formula then gives

    log q_n >= W n-O(log n),
    W=log(3)+log(7)/3+log(11)/5.

The elementary inequalities 7>(3/2)^3 and 11>(3/2)^5 imply W>log(27/4). Also sqrt(2)<3/2 implies

    tau=2log(1+sqrt(2))<log(25/4).

Consequently

    W-tau>log(27/25)>2/27.

For the last strict inequality, integrate 1/x on [25,27]; it is strictly greater than 1/27 except at the final endpoint. All algebraic comparisons are exact rational inequalities and are recorded in B2_RATE_COMPARISONS.json. No numerical logarithm is used.

The accepted full evaluated-error theorem at fixed b=2 gives eventual nonzero error and

    log|L_n|=log q_n-tau*n+o(n).

Thus the proposed audited synthesis would imply liminf log|L_n|/n>2/27, and in particular |L_n|>=exp(n/27) eventually. The initial index is not claimed effective. This would exclude all shrinking subsequences of this particular family; it would not settle rationality or irrationality of e+pi.

Dependencies awaiting independent acceptance are the normalized common-factor/transfer theorem and the complete unit seeds at 3,7,11. Prime 13 and the unresolved residue at prime 5 are unnecessary for this sufficient rate argument. Agent 4 has been requested to audit the complete synthesis without extending the prime list.
