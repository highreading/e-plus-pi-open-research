> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large-selector dyadic denominator review

Status: PASS for the arithmetic of Sections 1–6, with the explicit domain and qualifications below. This completes the retained paper review; no completed computation was rerun. Sections 7 onward and moving-saddle/error asymptotics are outside scope.

## Domain and notation

Let n=4k>=4, m>=0 be integers, N=2n+4m and J=N-n=n+4m. Put

Bpoly(t)=(1-2t+2t^2)^n(1-4t+2t^2)^(2m)=sum b_j t^j,
K(t)=t^n Bpoly^(n)(t)/n!, U=K(1).

The rational companions alpha and beta require U!=0. Here beta=calL((K-U)/(t-1))/U, where calL(P)=integral from -1 to 1 of P((1+iu)/2) du. Throughout, den(0)=1, denominators are positive, and v_2(0)=+infinity.

## Explicit endpoint nonvanishing

The coefficient bound v_2(b_j)>=ceil(j/2) follows by multiplying the two factors: every monomial contributing degree j contains enough factors of 2 to meet this bound. Also b_N=2^(N/2). Consequently K0=2^(-n/2)K is integral. Terms of degree greater than n vanish modulo 2 in K0, while the degree-n term gives

K0(t) = binom(n+2m,n/2)t^n (mod 2).

Indeed equality in the coefficient valuation at degree n comes only from quadratic terms; their count is binom(n+2m,n/2). Equivalently,

U=[x^n](1+2x+2x^2)^n(1-2x^2)^(2m).

Choose a power of two P with k<P<=2k and impose m=-k (mod P). Lucas parity gives

binom(4k+2m,2k)=binom(2k+m,k)=1 (mod 2).

The last equality holds because 2k+m is congruent to k modulo P and all nonzero binary digits of k lie below P. Therefore U!=0 and v_2(U)=n/2. The polynomial content of K has exactly this same dyadic valuation; this is not a claim about its odd content.

For any fixed rho>0, the explicit integer allocation

m_n=P ceil((rho n log n+k)/P)-k

satisfies rho n log n<=m_n<rho n log n+P, and hence proves nonvanishing along an allocation with m_n=rho n log n+O(n). Logarithms are natural. The parity condition is sufficient, not a characterization of all nonzero U.

## Complete exponential numerator

Write D_j=j! sum_{r=0}^j 1/r! and use falling factorials (J)_h. The complete rational exponential companion is

alpha=Vexp/(n! J! U),
Vexp=sum_{j=n}^N b_j (J)_(N-j) D_j.

This formula retains every term. For even j, D_j is odd: the recurrence D_j=jD_(j-1)+1 proves this immediately. In particular D_N is odd. For 1<=h<=J, since J is divisible by 4,

v_2((J)_h)>=floor(h/2)+1.

For even h, the h consecutive factors include h/2 even numbers, including J with one extra factor of 2. For odd h there are (h+1)/2 even numbers, which is already enough. With h=N-j>0,

v_2(b_j (J)_h D_j)>=ceil((N-h)/2)+floor(h/2)+1=N/2+1.

The h=0 term has valuation exactly N/2. Thus the least-valuation term is unique and

v_2(Vexp)=N/2.

This also proves Vexp!=0 without a numerical check.

## Logarithmic companion and absence of dyadic cancellation

The moments are

mu_r=calL(t^r)=((1+i)^(r+1)-(1-i)^(r+1))/(i 2^r(r+1)).

They satisfy v_2(mu_r)>=1-floor((r+1)/2), with mu_r=0 when 4 divides r+1. To check the bound, put l=r+1. If l is odd, the numerator has valuation (l+1)/2 in the resulting rational expression before the factor 2^(l-1); if l=2 (mod 4), it has valuation l/2+1 and v_2(l)=1. These give the stated inequality; the remaining case vanishes.

The coefficient of t^r in (K-U)/(t-1) is a sum of coefficients of K of degrees at least r+1. Each has valuation at least ceil((r+1)/2). Multiplication by mu_r therefore gives valuation at least 1. Hence

v_2(beta)>=1-v_2(U).

For any positive integer a divisible by 4, v_2(a!)>=3a/4, by counting multiples of 2 and 4. Since n and J are divisible by 4,

v_2(n!)+v_2(J!)>=3N/4.

Thus

v_2(alpha)=N/2-v_2(n!)-v_2(J!)-v_2(U)<1-v_2(U)<=v_2(beta).

Moreover v_2(U)>=n/2 whenever U!=0, since K0 is integral. Consequently alpha has negative valuation. The complete sum cannot undergo cancellation at this prime, including when beta=0.

## Exact law and repairs

For EVERY n=4k>=4 and m>=0 with U!=0, the actual reduced denominator q=den(alpha+beta) obeys

v_2(q)=v_2(n!)+v_2(J!)+v_2(U)-N/2.

On the parity allocation above this becomes

v_2(q)=3n/2+2m-s_2(n)-s_2(n+4m),

where s_2 denotes binary digit sum. Thus m=rho n log n+O(n) implies

liminf log q/(n log n)>=2 rho log 2.

For completeness, if O_N is the least common multiple of the odd positive integers at most N, the moment formula shows that O_N calL((K-U)/(t-1)) is an even integer. Therefore den(beta) divides O_N |U|/2; in particular this holds on the allocation, where U is nonzero and even.

Required qualifications: outside the explicit allocation the exact law is conditional on U!=0; at U=0 these rational companions are undefined. The result concerns the fully reduced sum, not merely a clearing denominator or separate companion product. The proven endpoint nonvanishing is distinct from complete approximation-error nonvanishing. No signed error asymptotic, shrinking integer form, or irrationality statement follows from this arithmetic review alone.
