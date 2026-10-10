> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Full prime-power lift of the positive-residue endpoint transfer

2026-09-13. Original continuation by root. Independent audit requested.
This extends the passed prime-level positive-residue theorem. The lift
is proved from integral identities, not assumed from a mod-p pattern.
Independent audit: **FULL PASS** by audit_sources; see
raw_positive_prime_power_lift_independent_review.md, including the
exact deeper classes at $(p,k)=(11,5)$ and $(13,3)$.

Fix k>=0, prime p>2k, nu>=1, T=p^nu, and n>=k with n=k mod T.
For k=0 retain the empty seed conventions. Assume p does not divide
M_D^[k](1). All V,b,Pe are the original primitive objects.

Claim: c=V_n(1)/V_k(1) is a p-adic unit and

    b_n(t) = c (t-1)^(n-k) b_k(t) mod T,
    V_n(t) = c t^(n-k) V_k(t) mod T,
    Pe_n(1) = c Pe_k(1) mod T.                           (1)

Congruences of rational quantities mean congruences in Z_(p). The
statements are exact for n=k, so below suppose n>k. No claim is made
at a prime dividing the determinant seed.

## 1. Same-size Schur inflation retains T

The ordinary Appell polynomial is

    A_L^[b](x)=sum_h binom(b,h) (L)_(2h) x^(L-2h).

Suppose L=ell mod T with 0<=ell<p and b=c mod T. If 2h>ell, every
nonzero falling factorial contains the factor L-ell, which is divisible
by T. If 2h<=ell, h! is a p-unit and both binomial and falling factorial
reduce at full precision. Therefore

    A_L^[b](x)=x^(L-ell) A_ell^[c](x) mod T.             (2)

The integral same-size content comparison holds for any integer
modulus. Replace p by T in the full rectangle and cofactor content
counts of raw_positive_residue_schur_and_endpoint_transfer.md. The
small degree sets remain contained in [k,2k], so their Vandermondes
are p-units. The enlarged degree differs by a multiple of T. Every
positive derivative of x^Delta is divisible by T when T|Delta.
Thus the same Wronskian calculation proves

    M_D^[n](1)=M_D^[k](1) mod T,
    M_j^[n](1)=M_a^[k](1) mod T if j=a mod T, 0<=a<=k.  (3)

The first congruence and primitive b formula force V_n(1),V_k(1)
to be p-units, as in the passed prime-level proof. Formula (3) alone
does not cover every j needed modulo T. The next step accounts for
that issue and for the exact loss in the binomial coefficient.

## 2. Weighted cofactor interpolation recovers the lost precision

Let F(X) be the polynomial of degree at most k over Z_(p) with

    F(a)=M_a^[k](1),       a=0,...,k.

Lagrange interpolation has only differences of numbers in [0,k] in
its denominators; they are p-units. We claim for EVERY 0<=j<=n that

    binom(n,j) (M_j^[n](1)-F(j)) = 0 mod T.              (4)

For j<=k this follows directly from (3). For j>k, put
u_j=v_p(binom(n,j)). If u_j>=nu there is nothing to prove. Otherwise
put beta=nu-u_j>0. The exact identity

    binom(n,j) = (n)_(k+1)/(j)_(k+1)
                 * binom(n-k-1,j-k-1)

shows that v_p((j)_(k+1))>=beta, since the numerator contains n-k
and the last binomial is an integer. Among j,j-1,...,j-k at most
one is divisible by p, because k<p. Hence j=a mod p^beta for one
0<=a<=k. Apply (3) with modulus p^beta, and use integrality of F:

    M_j^[n](1)=M_a^[k](1)=F(a)=F(j) mod p^beta.

Multiplication by binom(n,j) proves (4) at full depth nu. This also
handles j=n; j=0 and j=1 were covered without division by j(j-1).
For k=0 the same proof uses the one factor j and F=1.

## 3. The primitive b congruence

Let E=t*d/dt. The exact cofactor formula, (3), and (4) give

    b_n(t) = V_n(1)/M_D^[k](1)
             * F(n-E)(t-1)^n mod T.                    (5)

Indeed E multiplies the coefficient indexed by ell by ell, so F(n-E)
produces F(n-ell), with exactly the original sign and binomial weight.
At the seed k the corresponding expression is EXACT because F agrees
with every one of its k+1 cofactor values.

Every positive ordinary derivative of G=(t-1)^(n-k) is divisible
by T, since its first derivative contains n-k and further derivatives
preserve that integer factor. Thus E commutes with multiplication by
G modulo T. Also n=k mod T. It follows that

    F(n-E)[G(t)(t-1)^k] = G(t)F(k-E)(t-1)^k mod T.

Substitute the exact seed expression into (5). This proves the first
congruence in (1), with c=V_n(1)/V_k(1). No prime-power Lucas theorem
is being assumed.

## 4. An integral differential-operator congruence

For every positive integer M, as operators on Z[t],

    (1+D^2)^M = I mod M.                                (6)

For h>=1 its h-th term is

    binom(M,h)D^(2h)
      = M binom(M-1,h-1) [D^(2h)/h].

The operator in brackets preserves Z[t]: each nonzero monomial
coefficient is a product of 2h consecutive integers divided by h,
which is integral because (2h)! is divisible by h. This proves (6)
without dividing by a nonunit modulo M.

Take M=n-k, a multiple of T. The exact, independently reviewed identity

    (t-1)^nV_n(t)=(1+D^2)^n[t^n b_n(t)]

and (6) allow replacing the operator exponent n by k modulo T.
The first congruence in (1) rewrites its argument as

    c [t(t-1)]^(n-k) t^k b_k(t).

Every positive derivative of the bracketed factor is divisible by T,
by differentiating a positive integer power and retaining n-k. The
operator therefore passes through it modulo T. The seed identity gives

    (t-1)^n V_n(t)=c t^(n-k)(t-1)^n V_k(t) mod T.

Multiplication by the monic polynomial (t-1)^n is injective over
(Z/p^nu Z)[t], despite zero divisors in the coefficient ring: compare
the leading coefficient of a putative nonzero product. Cancel it to
prove the second congruence in (1).

## 5. The endpoint border also retains T

For a surviving index r=n-k+s, 0<=s<=k, the border is

    D_(n,r)=sum_j binom(n+j,j)(n+r)_j.

If j>k+s, every nonzero falling factorial includes
n+r-(k+s)=2(n-k), a multiple of T. If j<=k+s<=2k<p, j! is a
p-unit, so both factors reduce to those of D_(k,s). Therefore

    D_(n,n-k+s)=D_(k,s) mod T.

Substitution of the V congruence into the integral endpoint identity
Pe_n(1)=sum_r V_(n,r)D_(n,r) proves the third congruence in (1).

## 6. Exact finite loss at a previously exceptional numerator seed

Let e_k=v_p(Pe_k(1)), which is finite because Pe_k(1) is nonzero for
the specified seed. If nu>e_k, (1) and the unit c give

    v_p(Pe_n(1))=e_k.

If additionally v_p(n!)-floor(log_p(2n))>e_k, then the actual
arctangent numerator is strictly deeper. Consequently

    v_p(N_n)=e_k,
    v_p(q_n)=v_p(Z_n)-e_k >= v_p(n!)-e_k.               (7)

The positivity of the last factorial gap ensures that no negative
valuation is silently assigned to q. For fixed p,k these thresholds
hold eventually on n=k mod p^(e_k+1).

This extends the previously proved k=1 five-adic lift. It does not
bound numerator depth when v_p(n-k)<=e_k, and it does not resolve a
singular determinant seed. The new conclusions concern a specified
prime-power residue class; they are not uniform at an exceptional
prime over every degree.
