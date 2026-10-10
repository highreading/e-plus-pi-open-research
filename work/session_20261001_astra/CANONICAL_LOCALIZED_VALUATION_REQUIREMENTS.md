> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Localized valuation requirements for a small canonical denominator

Status: main-agent author deductions, not independently reviewed. This paper preserves the latest interval refinement and adds a counting consequence for distinct deeply dividing primes. It uses the canonical identity established in CANONICAL_HIGH_DENOMINATOR_STAGE.md with that paper's retained construction-specific hypotheses. No computation, numerical prime scan, or replay of an accepted review is claimed. The actual rationality or irrationality of e+pi remains OPEN.

## 1. Exact input and scope

Use the SAME factorial B-only Gram construction, b=3 and weight parameter m_w=1, at sufficiently large normal even indices n. Retain its integer data

    F=(n!)^2, d=(n+1)(n+2),
    h=det(Krec^T Omega Krec)>0,
    g=gcd(z), A=Dg/g>0,
    S_eff=h(Acal+d Delta x_0)/g in Z.

The endpoint correction Delta x_0 remains present. The retained fixed-b analytic estimates imply S_eff!=0 eventually; alternatively all assertions below can be read on the explicitly restricted nonzero-numerator indices. Let

    L=2^(N-1)lcm(1,...,N), 2n<=N<=2n+2,
    q=den(alpha+kappa+beta).

The stage paper gives the exact identity

    q/gcd(q,LA)=Fdh/gcd(Fdh,|L S_eff|).             (1)

It also gives log(dh)=O(log n), since dh is a fixed degree-fourteen polynomial. These are author inputs, not a new independent PASS.

For every prime satisfying

    sqrt(2n+2)<p<=n, p not dividing dh,

we have v_p(L)=1 and v_p(F)=2 floor(n/p). Define

    D_p=2 floor(n/p)-1,
    c_p=min(D_p,v_p(S_eff)).

Then (1) implies

    v_p(q)>=D_p-c_p.                              (2)

The effective cancellation c_p is truncated at the available denominator depth. Divisibility beyond that depth cannot compensate for uncanceled factors at other primes.

## 2. Elementary prime estimates used

The retained elementary lcm bound yields

    theta(x)=sum_(p<=x)log p=O(x),
    psi(x)=sum_(p^j<=x)log p=O(x).

Expanding log(N!) by prime powers, dividing by N, and bounding the rounding error by psi(N)/N gives

    log(N!)/N=sum_(p<=N)log p/p+O(1).

The higher-power contribution is bounded uniformly by the convergent sum

    sum_(l>=2)log l/[l(l-1)].

Thus the elementary factorial estimate proves

    sum_(p<=x)log p/p=log x+O(1), x>=2.             (3)

No additional prime-distribution hypothesis is used in the arguments below.

## 3. Available mass in a fixed exponent interval

Fix real constants

    1/2<=a<b<=1.

Let I_n(a,b) contain the primes

    max(sqrt(2n+2),n^a)<p<=n^b,
    p not dividing dh.

By (3), replacing floor(n/p) by n/p costs O(theta(n^b))=O(n). The subtraction of one in D_p also costs O(n). Excluding primes dividing dh costs at most

    2n^(1-a) log(dh)=O(n^(1-a)log n)=O(n).

The square-root lower boundary when a=1/2 changes the harmonic estimate by O(1). Consequently

    W_n:=sum_(p in I_n(a,b))D_p log p
        =2(b-a)n log n+O(n).                       (4)

The constants depend on the fixed interval parameters and retained construction bounds. In particular the interval contains admissible primes eventually.

Equation (2) gives the same-index inequality

    log q>=W_n-sum_(p in I_n(a,b))c_p log p.        (5)

## 4. Uniform bound for cancellation capped at K

For every integer K>=0 and z=n^b, define

    V(K,z)=sum_(p<=z)min(K,2 floor(n/p))log p.

Uniformly in K,

    V(K,n^b)
      <=2n log^+((K+1)n^(b-1))+O(n),              (6)

where log^+(x)=max(0,log x). The O(n) constant is independent of K.

Proof. K=0 is immediate. For K>=1 split at y=2n/(K+1). If 2<=y<z, the lower part is at most K theta(y)=O(n). The upper part is at most

    2n sum_(y<p<=z)log p/p
       <=2n log(z/y)+O(n),

which proves (6). If y>=z, the whole sum is at most K theta(z)=O(n), since (K+1)z<=2n. If y<2, use V(K,z)<=2n sum_(p<=z)log p/p and K+1>n; this is again bounded by (6). These cases cover all K without assuming a growth restriction on K.

Let

    K_n(a,b)=max_(p in I_n(a,b)) c_p.

Combining (4)-(6) proves

    log q>=2n[(b-a)log n
              -log^+((K_n(a,b)+1)n^(b-1))]-O(n). (7)

## 5. Where the deep prime must lie

Suppose a geometric denominator bound holds along the admitted sequence:

    log q<=C_q n,

with C_q fixed. Since b>a, (7) implies eventually

    K_n(a,b)+1>=c n^(1-a)                         (8)

for a positive constant c depending on the proposed bound and fixed parameters. Thus K_n(a,b) grows, and a prime attaining this maximum has

    v_p(S_eff)>=c' n^(1-a),
    D_p>=c' n^(1-a).

The second inequality is essential. Since D_p=2 floor(n/p)-1, it also gives

    p<=2n/(K_n(a,b)+1)<=C' n^a.                   (9)

Therefore geometric q requires a prime between the interval's lower endpoint and a constant multiple of n^a with valuation depth at least a constant multiple of n^(1-a).

For a=1/2, the prime lies above sqrt(2n+2) and below C' sqrt(n), and its depth is at least c' sqrt(n). A huge valuation at an unrelated prime near n cannot witness this requirement, because its available denominator depth D_p is too small.

More generally, log q=o(n log n) gives

    K_n(a,b)+1>=n^(1-a-o(1)).

These are necessary conditions, not established valuations of the actual numerator.

A useful sufficient obstruction is the bound

    K_n(a,b)+1<=n^(1-a)/omega(n), omega(n)->infinity.

Substitution into (7) gives

    log q>=2n min((b-a)log n,log omega(n))-O(n),    (10)

excluding every uniform geometric bound. No such estimate for K_n(a,b) is currently proved.

## 6. New counting consequence: many distinct deep primes are required

Fix an additional exponent t with

    a<t<b,

and set

    T_n=floor(n^(1-t)),
    H_n={p in I_n(a,b):c_p>T_n}.

The shallow primes have total cancellation bounded by V(T_n,n^b). Equation (6) gives

    sum_(p in I_n(a,b), c_p<=T_n)c_p log p
       <=2(b-t)n log n+O(n).                       (11)

Indeed (T_n+1)n^(b-1)=n^(b-t)(1+o(1)). Subtracting (11) from the cancellation required by (5) proves the unconditional lower bound

    sum_(p in H_n)c_p log p
       >=2(t-a)n log n-log q-O(n).                (12)

If log q=O(n), the right side is 2(t-a)n log n-O(n). Each summand is at most

    2b n^(1-a)log n,

because p>n^a, log p<=b log n, and c_p<=2n/p. Therefore

    |H_n|>=((t-a)/b-O(1/log n))n^a.               (13)

In particular, for all sufficiently large admitted indices under the proposed geometric bound,

    |H_n|>=(t-a)/(2b) * n^a.                      (14)

Every one of these distinct primes satisfies

    v_p(S_eff)>=T_n+1>n^(1-t),
    max(sqrt(2n+2),n^a)<p<2n^t.                   (15)

The upper location bound follows from D_p>=c_p>=T_n+1, which implies p<=2n/(T_n+2)<2n^t.

Thus a small denominator cannot be explained by only one extremely deep prime. For each fixed exponent triple a<t<b it requires at least a constant times n^a distinct primes, in the specified range, each carrying the stated depth. If merely log q=o(n log n), the same calculation gives the leading count ((t-a)/b-o(1))n^a.

This result concerns effective cancellation in the actual normalized numerator. It does not infer such cancellation from the existence of those primes, nor establish a contradiction with the available numerator-height bounds.

## 7. Relation to the lifting problem and limits

CANONICAL_FACTORIAL_COEFFICIENT_LIFTING.md supplies a recurrence with integer coefficients and leading coefficient one for C_s=s!b_s, and exact binomial-weight formulas for the unnormalized canonical contractions. At p not dividing dh, testing depth K in S_eff still requires the unnormalized numerator through p^(K+v_p(g)) and the actual content valuation v_p(g).

The requirements (8), (12), and (15) specify the depths and ranges which that arithmetic must address. They are not consequences of a first-residue gate alone. Proving a uniform bound that violates either the maximum-depth requirement or the many-prime requirement would obstruct geometric q. No such upper bound has been obtained.

These statements are confined to the same b=3,m_w=1 Gram center with its endpoint correction. They do not apply automatically to the coordinate centers or adjacent large-selector combinations studied by the children. They neither prove complete-error nonvanishing nor decide whether e+pi is irrational.
