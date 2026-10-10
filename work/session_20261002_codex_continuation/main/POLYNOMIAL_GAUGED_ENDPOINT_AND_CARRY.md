> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fixed polynomial amplitudes: complete endpoint, carry, and singularity order

Root original target M20, 2026-10-02. Author theorem and finite exact receipt; research remains ACTIVE.

## Prior-result and literature gate

Fresh archive searches covered polynomial gauges, weighted derangements, exponential endpoint amplitudes, and Hermite–Padé constructions. Generic polynomial exponential gauges already occur in the archive; M11–M15 already establish the unweighted endpoint and its carry law. The new target is their exact extension to one fixed polynomial amplitude, including the actual primitive denominator and complete signed error. Generic Hermite–Padé theory is prior work, not a new claim here.

Fresh primary searches identified Van Assche, Padé and Hermite–Padé approximation and orthogonality, arXiv:math/0609094. The O'Desky–Richman primary paper https://arxiv.org/html/2012.04615v4 was reopened, particularly its two-variable continuity discussion and Theorem4.5. Its generic continuity statements do not supply the full numerator carry below. Singularity transfer uses the primary Flajolet–Odlyzko paper https://algo.inria.fr/flajolet/Publications/FlOd90b.pdf already read for M13; the direct finite-log proof from M13 also applies. No external solution of the present normalized complete endpoint problem was found in this gate.

## Exact complete endpoint

Keep one fixed rational polynomial P with P(0)=0, P(1)=1 and integral derivative jets. Write

    G(z)=4 arctan(P(z)/(2-P(z))), S=e+pi,
    g_j=G^(j)(0), u_j=(exp(-z)G(z))^(j)(0).

All g_j are even integers. The original integer arrays are

    D_N=N! sum_(k=0)^N (-1)^k/k!,
    B_N=N!+sum_(j=0)^N binom(N,j)g_j D_(N-j).

Take a fixed A(z)=sum_(j=0)^m a_j z^j in Q[z] whose derivative jets alpha_j=j!a_j are integral, and require A(1) != 0. For N>=m define

    D_N^A=N! sum_(k=0)^N (A exp(-z))^(k)(0)/k!,
    B_N^A=N! [A(1)+sum_(k=0)^N (A exp(-z)G)^(k)(0)/k!].

The exact finite identities are

    D_N^A=sum_(j=0)^m binom(N,j)alpha_j D_(N-j),
    B_N^A=sum_(j=0)^m binom(N,j)alpha_j B_(N-j).       (1)

They follow by exchanging the finite sums, including the A(1) term. Both arrays are integers for N>=m. For all sufficiently large N, D_N^A is nonzero since D_N^A/N! tends to A(1)/e. Thus

    c_N^A=B_N^A/D_N^A -> S,
    q_N^A=|D_N^A|/gcd(D_N^A,B_N^A).                 (2)

Equation(2) uses the FULL numerator and final gcd. Removing the A(1) term would change the target. The condition A(1)!=0 is essential: A=1-z gives D_N^A=(-1)^N and B_N^A=u_N, so factorial cancellation alone does not retain convergence to S.

## All-depth good-prime carry

Let D*(x) and C*(x) be M15's continuous Mahler interpolations of (-1)^N D_N and (-1)^N(B_N-N!). For an odd prime p at which every ordinary coefficient of P and A is integral, put chi=(-1|p). No condition p>deg A is needed. Define

    D_A*(x)=sum_(j=0)^m (-1)^j a_j (x)_j D*(x-j),
    C_A*(x)=sum_(j=0)^m (-1)^j a_j (x)_j C*(x-j).

At integers N>=m these equal (-1)^N D_N^A and (-1)^N(B_N^A-A(1)N!). For every x in Z_p, k>=1 and t in Z_p,

    C_A*(x+p^k t)-C_A*(x)
        =p^(k-1)t chi g_1 D_A*(x)  (mod p^k).       (3)

Indeed each polynomial weight a_j(x)_j is integral and 1-Lipschitz. Its change is divisible by p^k; apply M15's shift law at x-j to the remaining change and sum. D_A* is 1-Lipschitz. C_A* has the same global loss of one p-adic digit as C*, and becomes 1-Lipschitz on a denominator-zero residue cell. Once N!A(1) vanishes modulo p^k, the actual common-content criterion is D_A*(N)=C_A*(N)=0 modulo p^k. Thus A can move denominator-root cells, but does not automatically remove the numerator precision defect or produce global common content.

For example A=1-az gives

    D_A*=(1-a)D*+a,
    B_N^A=(1-a)B_N+a u_N.

The first identity follows from D*(x)=1-xD*(x-1). Its numerator counterpart is equally exact; it is not a denominator-only optimization.

## What fixed zeros at logarithmic singularities achieve

Use M13's exact decomposition G=sum_lambda L_lambda log(1-z/lambda), where lambda are the distinct algebraic roots of P=1+i and P=1-i, with nonzero algebraic L_lambda incorporating root multiplicity. Let R0=min|lambda|>1, m_lambda=ord_lambda A, and m0 be the smallest such order among roots of modulus R0.

The COMPLETE normalized error has leading contribution

    c_N^A-S = N^(-m0-1)
       sum_(|lambda|=R0, m_lambda=m0)
       [exp(1-lambda)L_lambda lambda^m0 A^(m0)(lambda)
        /(A(1)(lambda-1))] lambda^(-N)
       +O(R0^(-N)N^(-m0-2)).                        (4)

Roots with larger modulus contribute exponentially smaller terms. The tails of A exp(-z) and the endpoint A(1) term are included before taking this asymptotic; their remainder is factorially small for this ONE fixed A.

To check the sign, the exact coefficient of (1-z/lambda)^m log(1-z/lambda), for n>m, is (-1)^(m+1)m! lambda^(-n)/[n(n-1)...(n-m)]. The Taylor coefficient of A at lambda contributes (-lambda)^m A^(m)(lambda)/m!. Their product has a minus sign. Summing the complete negative tail and dividing by A(1)/e gives(4).

On any fixed arithmetic progression, group the surviving nearest roots by equal powers lambda^h. Every grouped leading coefficient is nonzero by Lindemann–Weierstrass at distinct algebraic lambda; all remaining multipliers are nonzero algebraic numbers. The finite Vandermonde argument from M13 therefore gives a bounded block with error of order R0^(-N)/N^(m0+1). A fixed polynomial weight improves only the power of N. It cannot remove the exponential radius: a finite-order zero weakens a logarithmic singularity without making it analytic.

This block statement is not an every-index lower bound. None of its constants is uniform in independently varying A_N. There is no claim that variable-degree weights fail, that a favorable global gcd exists, or that e+pi has been decided.

## New exact receipt

POLYNOMIAL_GAUGED_ENDPOINT_CERTIFICATE.json rebuilds the frozen degree81 P and checks A=1-2z, 1+z^2, and 1-2z+2z^2. A separate derivative-product recurrence verifies(1) through N=140. Actual primitive q is stored at N=10,50,140. Weighted Mahler evaluation verifies(3) at p=83 through three depths, at14 new indices per depth including indices above10^20. These checks test the new endpoint normalization and carry law; they do not prove a global denominator rate. The receipt passed all exact assertions.
