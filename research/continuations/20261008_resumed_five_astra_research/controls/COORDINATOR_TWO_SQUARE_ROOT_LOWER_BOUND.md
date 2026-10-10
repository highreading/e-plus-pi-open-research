> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A root-exponential ordinary-error lower bound for the two-square ansatz

Coordinator derivation,8 October2026. Locally proved, pending external
independent audit. It strengthens the preceding progression obstruction
to EACH fixed odd-prime progression N=1 modulo p. It does not classify
moving prime divisors of N-1, prime2, or every possible subsequence.

## Scoped archive and primary-source gate

A scoped search of archive sources and20261007/current Markdown reports
for Laguerre Taylor/effective-degree/root-exponential lower estimates found
no evaluated version for this new two-square family. One different sector
kernel hit is not imported. This is not exhaustive novelty evidence.
The finite Laguerre expansion in[DLMF18.5.12](https://dlmf.nist.gov/18.5.E12)
was read directly in the rendered HTML at its explicit formula. Cauchy's
coefficient bound and the earlier accepted Legendre kernel estimate are
classical. The argument below derives the particular effective-degree
and paid whole-error bounds directly; no outside asymptotic theorem is used.

## 1. The actual Laguerre coefficient norm

The source minimizer is real and expands exactly as

    f_N(t)=sum_(j=0)^N c_j L_j(1-t),
    c_j=N!*(W*alpha_j-V*beta_j)/Delta.

For the source measure eta=e^(t-1)dt on(-infinity,1], these basis
polynomials have unit orthogonal norms. The accepted minimizer gives

    sum c_j^2=tau_N=(N!)^2*W/Delta<=2/3<1,
    f_N(i)=1.

Thus its source coefficient norm is bounded uniformly. No coefficient
clearer, polynomial content or final gcd is divided out in this estimate.

## 2. An entire-polynomial growth bound

The finite expansion and binom(j,r)<=j^r/r! give, for complex z,

    |L_j(z)|<=sum_(r>=0)(j*|z|)^r/(r!)^2
             <=exp(2*sqrt(j*|z|)).

The second inequality follows by retaining only even terms in exp(2sqrt x):
its2r-th term dominates x^r/(r!)^2 because binom(2r,r)<=4^r.
It is valid also at j=0 and z=0. For |t|<=R=36,

    |f_N(t)|<=sqrt(N+1)*exp(2*sqrt(37N))=:C_N.

Here the coefficient norm bound is used by Cauchy--Schwarz, and
|1-t|<=37. There are no poles or unverified asymptotic expansions.

## 3. Truncation at degree at most16sqrt N+1

Set M=min(N,ceil(16sqrt N)), and let f_M be the Taylor polynomial
of the ACTUAL f_N at0 through degree M. If M=N, the tail is zero.
Otherwise Cauchy's coefficient bound on the circle of radius36 gives

    |f_N(t)-f_M(t)|<=delta_N:=C_N*36^(-M)/35,
    |t|<=1.                                                (1)

This includes t=i and the complete real integration interval[0,1].
For the nonzero-tail case, M>=16sqrt N and M+1<=18sqrt N. Since
sqrt(N+1)<=(3/2)sqrt N, 2sqrt37<13 and log6>3/2,

    delta_N*(M+1)*6^M
      <=(27N/35)*exp(-11sqrt N)<1/4, N>=1.                 (2)

The last bound is rigorous: x^2 exp(-11x) decreases for x>=1,
and exp(-11)<2^(-11), using e>2. The elementary log6 bound
follows from e<3 and3sqrt3<6. In particular delta_N<1/4.

The preceding progression note proves the complex Legendre evaluation
bound for any real polynomial of degree at most M:

    ||f_M||_(L2[0,1])>=|f_M(i)|/[(M+1)*6^M].

By(1)--(2), |f_M(i)|>=3/4 and the L2 norm of the tail is at
most1/[4(M+1)6^M]. The reverse triangle inequality therefore yields

    ||f_N||_(L2[0,1])>=1/[2(M+1)*6^M].

If M=N, the exact evaluation bound already implies this weaker estimate.
Thus the inequality is uniform in the actual family for every N>=2:

    J_N=int_0^1 P_N>=int_0^1 f_N^2
        >=1/[4(M+1)^2*36^M], M=min(N,ceil16sqrt N).        (3)

Since M<=16sqrt N+1, this is a genuine root-exponential LOWER bound
with a polynomial prefactor. The previously accepted upper bound was
root-exponential; their combination now controls the order of ordinary
decay. No comparison of upper bounds is presented as a no-go proof.

## 4. Paid primitive whole-error consequence on each fixed prime class

Fix ANY odd prime p. The last-prime-block theorem, still awaiting its
independent audit, evaluates the actual primitive denominator whenever
N>=4 and N=1 modulo p:

    v_p(q_N)=v_p(T_N)+v_p(N-1),
    T_N=(2N-4)!R4(2N-4).

Put m=2N-4. The factorial digit bound and v_p(N-1)>=1 give

    q_N>=p^(m/(p-1))/m.

Combining this with(3) and the complete positive source weight yields

    q_N*((e+pi)-p_N/q_N)
      >=3*p^(m/(p-1))/[4m*(M+1)^2*36^M]
       ->positive infinity,
    N->infinity, N=1 modulo p, p FIXED and odd.             (4)

The logarithm's leading term is(2N/(p-1))*log p, while the
negative term M*log36 is O(sqrt N). Every term is at the SAME N;
the actual final gcd is already included in the q valuation theorem.

This rules out each such fixed-prime progression for the two-square
irrationality criterion. It does not rule out sequences with the least
odd prime divisor of N-1 tending to infinity, or N-1 a power of2.
It does not apply to other producers without checking their exact
source coefficient norm and arithmetic. No global rationality decision
and no research stopping condition have been achieved.

## 5. Corollary for the ENTIRE original two-square index sequence

The actual proposed original indices in A3turn0 Section8 and A2turn1 are

    N=9^(18+32u)=81^(9+16u), u>=0.

Every such N is1 modulo5, because81=1 modulo5. Thus the fixed prime
p=5 in(4) applies at EVERY original index, not merely a diagnostic
subsequence. The actual primitive whole error of this precise two-square
ansatz tends to positive infinity on its entire original sequence.
In particular the proposed original-index primitive-saving lemma
q_N<=exp(sqrt N/4) is impossible here.

One may also evaluate the retained5-adic depth explicitly. At m=2N-4,
R4(m)=R4(-2)=12=2 modulo5, so it is a5-adic unit. The elementary
binomial lifting identity applied to81=1+5*16 gives

    v_5(N-1)=1+v_5(9+16u),
    v_5(q_N)=v_5((2N-4)!)+1+v_5(9+16u).                 (5)

For completeness, if a has5-adic depth s>=1 then(1+a)^5-1 has
depth s+1: its first term5a has that depth, its next three terms have
greater depth, and a^5 also has greater depth. For an exponent prime
to5, the first binomial term has unchanged depth and all later ones
have greater depth. This proves the lifting identity with no unpaid
division. It is a classical elementary reuse, not a novelty claim.

This is a LOCAL no-go for this newly defined producer on its unchanged
original sequence, pending independent A3/A5 review of the full proof.
It does not transfer to the distinct Laguerre, compact or ternary
producers, and it does not decide the rationality of e+pi. Research
continues on the remaining routes and genuinely different ansatzes.
