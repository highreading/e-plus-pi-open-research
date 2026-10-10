> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Polynomial pullbacks: an exact surviving factorial core at the Taylor endpoint

Status: original author derivation, 2026-10-02; not independently reviewed. This concerns ordinary Taylor truncations of the specified pullbacks, after the final endpoint gcd. It proves no assertion about the arithmetic nature of e+pi and does not identify a Hermite–Padé center with a Taylor truncation.

Let F(w)=4 arctan(w/(2-w)), with F(0)=0, and let P be a rational polynomial with P(0)=0, P(1)=1. Assume that P has integer derivative jets at zero. Put G=F∘P as a germ at zero and assume, when identifying its endpoint, that the specified branch has G(1)=pi. The root's polynomial constructions satisfy that endpoint condition. Define

    G_N=sum_{j=1}^N G^(j)(0)/j!,
    E_N=sum_{j=0}^N 1/j!,
    c_N=E_N+G_N=p_N/q_N in lowest terms,
    A_N=N! E_N, B_N=N! G_N, Z_N=A_N+B_N.

All gcds below concern the complete Z_N. The logarithmic Taylor contribution is retained.

## 1. A support-only common denominator

Let S be any finite set containing 2 and every prime dividing a monomial coefficient denominator of P. Let L_N=lcm(1,...,N), and use the notation X_S for the part of a positive integer X supported on S. Set

    M_N=(N!)_S (L_N)_(S^c),  F_N=N!/M_N.

Since L_N divides N!, these are positive integers and M_N divides N!.

The exact differential identity is

    G'=2P'/(1-P+P^2/2).

For p outside S, P and P' have p-integral ordinary coefficients, and the denominator polynomial has constant coefficient 1. Its formal inverse is therefore p-integral. If G'=sum r_j z^j, every r_j is p-integral. Integration gives

    v_p([z^j]G)>=-v_p(j),
    v_p(G_N)>=-floor(log_p N).                       (1)

The Hurwitz composition law gives G^(j)(0)∈Z at every order: F has integer derivative jets, as follows from (2-2w+w^2)F'=4, and composition uses integer Bell polynomials. Consequently N!G_N∈Z. At primes in S its denominator depth is at most v_p(N!). Combining both estimates proves the exact divisibility

    den(G_N) | M_N,  F_N | B_N.                     (2)

The bound has no dependence on the sizes of the coefficients of P. In particular, the possible enormous powers in its fixed rational coefficient denominator need not be charged as C^N.

## 2. Exact transfer through the final endpoint gcd

Equation (2) immediately gives

    gcd(Z_N,F_N)=gcd(A_N,F_N).                       (3)

Therefore the explicit integer

    K_N=F_N/gcd(A_N,F_N)

divides the actual reduced denominator q_N. This is a content identity at the evaluated endpoint, not a raw Taylor coefficient statement.

Write Q_N=den(E_N)=N!/gcd(A_N,N!). Rational addition and subtraction, using (2), also give the two exact divisibilities

    Q_N | q_N M_N,  q_N | Q_N M_N.                 (4)

In particular,

    Q_N/M_N <= q_N <= min(N!, Q_N M_N),
    |log q_N-log Q_N| <= log M_N.                  (5)

For completeness the stronger local alternative at p outside S is explicit. Write f=v_p(N!), ell=floor(log_p N), a=v_p(A_N). Then

    a<f-ell  =>  v_p(q_N)=f-a=v_p(Q_N);
    a>=f-ell =>  0<=v_p(q_N)<=ell.                 (6)

Indeed B_N has depth at least f-ell. In the first case strict valuation domination forbids cancellation; in the second both summands Z_N have depth at least f-ell. Thus the pullback can change a good-prime exponential denominator only in its logarithmic-depth boundary layer. No finite residue atlas or unproved all-depth scalar-root assertion is used.

## 3. Uniform factorial-scale actual denominator

The archive already proves the uniform rational approximation bound

    |e-a/b|>=c_e/(b^2 log(2b)),

using Euler's continued fraction. Its application to E_N and the elementary positive-tail bound |e-E_N|<2/(N+1)! gives

    Q_N >= sqrt(c_e (N+1)!/[2 log(2N!)]).           (7)

This is an existing input, not a newly asserted gcd asymptotic for A_N. Equations (5) and (7) give, after the actual final gcd,

    q_N >= sqrt(c_e (N+1)!/[2 log(2N!)])/M_N.       (8)

For fixed S put c_S=sum_{p∈S} log(p)/(p-1). Legendre's formula and L_N<=4^N give

    log M_N <= (c_S+log 4)N.

Hence

    liminf log q_N/(N log N) >= 1/2.               (9)

The same statement holds for an index-dependent P_N, each integral Hurwitz and endpoint fixed, whenever its corresponding support denominator M_N satisfies log M_N=o(N log N). A sufficient arithmetic condition is c_(S_N)=o(log N). Neither analytic radius nor coefficient height enters this implication.

## 4. The complete primitive Taylor forms diverge in this domain

The published Zeilberger–Zudilin theorem permits the safe exponent mu=36/5: there exists c_pi>0 such that |pi-a/b|>=c_pi b^(-mu) for every reduced rational. For gamma_N=G_N, equation (2) gives

    |pi-G_N|>=c_pi M_N^(-mu).

If log M_N=o(N log N), the exponential tail is eventually smaller than half this lower bound. Keeping both tails, the reverse triangle inequality gives

    |(e+pi)-c_N| >= (c_pi/2) M_N^(-mu),
    |q_N(e+pi)-p_N|
      >= (c_pi/2) sqrt(c_e (N+1)!/[2 log(2N!)])
                       /M_N^(mu+1).               (10)

Consequently

    liminf log |q_N(e+pi)-p_N|/(N log N) >= 1/2.    (11)

This is a full-sequence divergence statement; no limsup geometric tail estimate is substituted for a pointwise lower bound. It excludes all ordinary Taylor truncations of every fixed polynomial supplied by the root's radius theorem, including the degree61 example. It also excludes varying polynomials under the displayed subfactorial support-cost condition. It does not exclude index-dependent polynomials whose denominator supports have factorial-scale cost, an infinite nonpolynomial Hurwitz pullback, rational corrections with factorial denominators, or an independent Hermite–Padé construction.

## 5. Coefficient clearing is a different, stronger factorial statement

There is also an exact dyadic statement that does not require a fixed denominator support. The recurrence for f_j=F^(j)(0) is f_1=f_2=2 and f_(j+1)=j f_j-binomial(j,2)f_(j-1). Thus every f_j is even, and integral-Hurwitz composition gives every G jet even. B_N is consequently even. At every even N, A_N=N A_(N-1)+1 is odd, so Z_N is odd and

    v_2(q_N)=v_2(N!)       (N even).               (12)

This remains valid for varying integral-Hurwitz P_N. Under a hypothesis e+pi=a/b rational, (12) guarantees c_N≠a/b for every sufficiently large even N, since v_2(N!)>v_2(b). It supplies a nonzero interface only; its exponential lower denominator rate alone proves no irrationality.

For p outside S, (1) gives v_p(G^(N)(0))>=v_p((N-1)!). If p<=N-1 then this depth is positive, so the N-th derivative jet of e^z+G is 1 modulo p. Its N-th ordinary coefficient has exactly depth -v_p(N!). Thus a common denominator clearing the Taylor coefficients through order N contains the part (N!)_(S^c), apart from a possible single factor N when N itself is a good prime. Its logarithm is N log N-O_S(N).

That coefficient theorem cannot be silently promoted to q_N. Equations (3)-(8) supply the separate endpoint argument, whose uniform bound is a half-factorial scale. The unknown e partial-sum gcd remains visible.

## 6. Sources and novelty boundary

Archive inputs: sources/algebraic_translation_approximation_no_go.md, §3 supplies (7); work/session_20260913/audit_sources.md has the raw even-coefficient obstruction; work/session_20261001_astra/GENERAL_SMALL_SELECTOR_COMPLETE_EXCLUSION_DRAFT.md and JOINT_COMPANION_OVERLAP_BUDGET_DRAFT.md supply the existing general companion-budget strategy. These do not give (2)-(3) for an arbitrary polynomial pullback. The new application resolves its support-only arithmetic interface and exact endpoint factorial core. It does not claim a new general irrationality-measure method.

Primary sources opened in this target:

- Henry Cohn, [A Short Proof of the Simple Continued Fraction Expansion of e](https://arxiv.org/pdf/math/0601660), supports the explicit Euler expansion used in the existing bound.
- Jonathan Sondow and Kyle Schalm, [Which partial sums of the Taylor series for e are convergents to e? II](https://arxiv.org/pdf/0709.0671), defines the exact A_N/gcd normalization and supplies block gcd relations. No conjectural scalar-zero assertion is used here.
- Doron Zeilberger and Wadim Zudilin, [The irrationality measure of pi is at most 7.103205334137...](https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimPDF/pimeas.pdf), published 2020, supplies the finite-measure input with mu=36/5 strictly above its bound. The source's definition and quantifiers were inspected; this is use of a published theorem, not an independent proof audit.
- Dreyfus and Rivoal, [Representability of G-functions as rational functions in hypergeometric series](https://arxiv.org/pdf/2405.12568), is background on the G-function denominator class. The elementary rational-derivative proof above is sufficient and does not invoke a representation theorem.

No numerical probe is needed for (1)-(11). Any saved bounded exact receipt only demonstrates the normalization on specified polynomial instances.

The bounded receipt script pullback_factorial_core_receipt.py reads the root's degree61 endpoint-basis integers and computes our exact jet recurrence and final Taylor fraction for N=1,...,240. It does not examine or rerun the analytic radius proof. POLYNOMIAL_PULLBACK_FACTORIAL_CORE_RECEIPT.json preserves six complete actual q/gcd examples and hashes of the integer arrays. All cases are supporting normalization evidence only.
