> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# HP prime folding: independent review and an actual denominator exclusion

2026-09-13. Bounded arithmetic continuation of the proved b=1 analytic theorem. This note reviews `hp_b1_primitive_arithmetic_attempt.md` and adds a complete prime exclusion at n=p-1, an explicit harmonic-number formula for the first kernel defect, and an exact fixed-offset endpoint gate. No degree scan or numerical asymptotic inference is used.

**New proved statement:** for every odd prime p, the actual reduced endpoint denominator at index n=p-1 satisfies

    p does not divide q_(p-1).

This concerns the fully reduced endpoint ratio, rather than a chosen coefficient clearer. It is a restricted prime exclusion and does not bound the total size of q_n.

## 1. Objects and the reviewed folding theorem

Use the already proved b=1 projection with

    K_n(t,s)=1/2 sum_(k=0)^n(2k+1)P_k(x)P_k(y),
    x=-i(2t-1), y=-i(2s-1),
    ell_j(s^a)=1/(n+a+1-j)!, j=0,1,
    C_j^*(t)=-ell_j K_n(t,s), t_j=-C_j(1),
    a_j=-[T_n(z^j e^z+C_jF)](1).

The rational representative of the endpoint pair is

    X=(1+t_1)a_0-(1+t_0)a_1,
    Y=delta=t_1-t_0,
    q_n=denominator(X/Y) in lowest terms.

For an odd prime p satisfying n<p<=2n+1, set m=p-2-n>=-1 and K_(-1)=0. The coefficient identity

    P_(p-1-k)(x)=P_k(x) mod p

follows from the binomial expansion of P_k. Pairing k with p-1-k cancels both weighted terms modulo p, while the central weight is p. The surviving kernel is exactly

    K_n=K_m mod p.

The cutoff is p-2-n, not p-1-n. I independently verified the pairing and the central case.

Set b=p-n-1=m+1 and E=(K_n-K_m)/p. In ell_0, the factorial denominator contains p exactly when its s-degree is at least b. In ell_1 the threshold is b+1. Those kernel coefficients are divisible by p, and their factorials are less than2p. Therefore the apparent poles cancel. Wilson's theorem gives the precise residues

    ell_0 K_n = sum_(a=0)^m K_(m,a)/(n+a+1)!
                    -sum_(a=b)^n E_a/(a-b)! mod p,

    ell_1 K_n = sum_(a=0)^m K_(m,a)/(n+a)!
                    -sum_(a=b+1)^n E_a/(a-b-1)! mod p.

Here K_(m,a) and E_a denote coefficients of s^a. These formulas and the p-integrality conclusion in the reviewed note are correct.

In particular C_0,C_1,t_0,t_1 are p-integral for every odd p>n. For n<p<=2n+1 this follows from folding; for larger p it is immediate from the denominators. The Taylor coefficients of e^z and F through n are p-integral when p>n, so a_0,a_1 and X,Y are p-integral as well. For n>=2, every reduced denominator in this elementary projection is consequently supported on primes at most n. This alone says nothing about primes introduced by the numerator of Y when X/Y is reduced.

## 2. A complete primitive-prime exclusion when n=p-1

Let p be any odd prime and n=p-1. The standard Legendre Christoffel–Darboux identity gives the polynomial identity

    K_(p-1)(t,s)/p
      = [P_p(x)P_(p-1)(y)-P_(p-1)(x)P_p(y)]/[2(x-y)].

The numerator is divisible by x-y over the p-integral polynomial ring. We have

    P_(p-1)(x)=1 mod p,
    P_p(x)=x^p mod p.

The first is the folding identity with k=0. For the second, use

    P_p(1-2z)=sum_(j=0)^p (-1)^j binom(p,j)binom(p+j,j)z^j.

All intermediate coefficients vanish modulo p; the final coefficient is -2, since binom(2p,p)=2 modulo p. Thus the reduction is `1-2z^p=(1-2z)^p`.

Reducing the polynomial quotient therefore gives

    K_(p-1)(t,s)/p = (x-y)^(p-1)/2 mod p.

Put chi_p=(-1)^((p-1)/2). Since x-y=-2i(t-s), Fermat's theorem gives

    E(t,s):=K_(p-1)(t,s)/p
           =chi_p (t-s)^(p-1)/2 mod p.

At t=1, each coefficient of s^a in (1-s)^(p-1) equals1 modulo p. Hence E_a(1)=chi_p/2 for every0<=a<=p-1.

Here m=-1 and b=0. The exact Wilson contraction formulas become

    t_0=-chi_p/2 sum_(a=0)^(p-1) 1/a! mod p,
    t_1=-chi_p/2 sum_(a=0)^(p-2) 1/a! mod p.

Subtracting cancels every common term:

    delta=t_1-t_0=chi_p/[2(p-1)!]=-chi_p/2 mod p.

This is a unit. Therefore Y is nonzero as a rational number and v_p(Y)=0. Section1 proves X is p-integral, including the factorials and logarithmic Taylor coefficients used to reconstruct a_j. Consequently

    v_p(q_(p-1))=max(0,v_p(Y)-v_p(X))=0.

This proves the claimed actual denominator exclusion. No assumption about the primitive content of a chosen clearing is used.

The odd-prime condition is necessary for this proof. The omitted p=2 corresponds to n=1, where the exact endpoint is Y=0 and q_n in this normalization is undefined. There is no claim at that exceptional index. Every odd p>=3 is covered, including n=2 below the eventual analytic thresholds.

Selected exact normalization checks, computed without solving new HP matrices, are:

| p | n=p-1 | delta modulo p | Actual q_n |
|---:|---:|---:|---:|
|3|2|2|28|
|5|4|2|71872|
|7|6|4|389565936000|
|11|10|6|546392884125661977600000|

The n=4 denominator also matches the independent pre-existing primitive profile. These values check normalization only; the all-prime proof is above.

## 3. Explicit harmonic coefficients for the first Legendre defect

The first kernel quotient can be made explicit without treating it as unspecified p^2 data. Fix0<=k<=(p-3)/2, put l=p-1-k, and define

    D_(p,k)(x)=(P_l(x)-P_k(x))/p in Z_(p)[x].

Let H_a=sum_(b=1)^a 1/b modulo p, H_0=0, and write

    A_(k,j)=(-1)^j binom(k,j)binom(k+j,j).

Then the coefficients of D_(p,k)(1-2z) are explicitly

    [z^j]D_(p,k)(1-2z)
      = A_(k,j)(H_(k-j)-H_(k+j))             for0<=j<=k,

      = (-1)^k (k+j)!(j-k-1)!/(j!)^2        for k<j<=p-1-k,

      =0                                    for j>p-1-k,

all modulo p. Every displayed factorial and harmonic denominator is a p-unit.

To prove this, write the coefficient of P_l(1-2z) as

    (k+1-p)_j(-k+p)_j/(j!)^2.

For j<=k, expand both products to first order in p. Their logarithmic derivative difference is

    sum_(a=0)^(j-1)1/(-k+a)-sum_(a=0)^(j-1)1/(k+1+a)
      =H_(k-j)-H_(k+j).

For j>k, the second product contains exactly one factor p, at a=k. After dividing by p, its other factors reduce to `(-1)^k k!(j-k-1)!`, while the first product reduces to `(k+j)!/k!`. This proves the second line. The omitted coefficients are identically zero because both Legendre degrees are smaller.

This is an exact first-lift formula. It does not assert any nonvanishing of its factorial contraction or a bound for an endpoint gcd.

## 4. Fixed offsets n=p-h: an explicit endpoint gate

Let h>=1 and p be an odd prime with h<=(p+1)/2, and set n=p-h, m=h-2. Thus the folding range still holds. Define

    mathcal P_k(t)=P_k(-i(2t-1)),
    mathcal D_k(t)=D_(p,k)(-i(2t-1)).

The first kernel quotient has the explicit reduction

    E(t,s)=chi_p(t-s)^(p-1)/2
      -sum_(k=0)^(h-2) [mathcal P_k(t)mathcal P_k(s)
          -(2k+1)/2*(mathcal D_k(t)mathcal P_k(s)
                        +mathcal P_k(t)mathcal D_k(s))] mod p.       (A)

For h=1 the sum is empty. To derive(A), start with the full kernel K_(p-1), then remove its last h-1 summands. Pair each removed degree p-1-k with k and use `P_(p-1-k)=P_k+pD_(p,k)` modulo p^2. Dividing that paired expression by p gives exactly the bracket in(A). The result descends from the splitting algebra to rational coefficients, as the original kernel does.

Let k_a=[s^a]K_(h-2)(1,s), e_a=[s^a]E(1,s). Applying Wilson's theorem also to the low-degree factorials gives the fully explicit first-lift endpoint gate

    delta mod p
      =sum_(a=0)^(h-2) (-1)^(h-a)(h-a)(h-a-2)! k_a
       +sum_(d=0)^(p-2h+1) (1-d)e_(h-1+d)/d!.                  (B)

Indeed the low factorial identity is `1/(p-j)!=(-1)^j(j-1)!`, and the two high sums combine into `(1-d)/d!`. Formula(B), together with the harmonic coefficients in Section3, is an explicit arithmetic condition. It is not a generic nonzero-polynomial argument or an all-prime unit theorem.

For h=1, (B) telescopes to the constant unit in Section2. For h=2, a uniform unit conclusion is actually false. Exact selected computations give

    (n,p)=(5,7): delta=0, X=2 mod7, v_7(q_5)=1,
    (n,p)=(9,11): delta=0, X=8 mod11, v_11(q_9)=1.

These are exact counterexamples to extending `p does not divide q_(p-1)` unchanged to n=p-2. If both X and delta vanish, one further digit is still required. No distribution or asymptotic claim is inferred from these examples.

## 5. Review of the endpoint-gcd theorem and rational companion

The local endpoint-gcd restriction in Section3 of `hp_b1_primitive_arithmetic_attempt.md` is sound. If p^h divides both endpoints of a primitive full triple, division by z-1 modulo p^h leaves a constant exponential coefficient. That coefficient must be a unit: otherwise the original high moments, with the unit Gram norms h_0,...,h_n, force the entire full triple to vanish modulo p, contrary to primitive coefficient content.

The quotient still vanishes to order2n+2. Its extra moment equations therefore include tests against p_n and p_(n+1). These polynomials and all needed moment denominators are p-integral for p>2n+2. At the possible prime p=2n+3, h_(n+1) need not be a unit, but it is never inverted in the argument; only the earlier norms are used for the unit assertion.

I independently derived the two Rodrigues contractions. With the integer polynomials H_k,J_k defined in that note, they are exactly

    ell_(n-1)(p_n)=H_n(1)/(2n)!,
    ell_(n-1)(p_(n+1))=J_(n+1)(1)/(2n+2)!.

Thus the claimed prime-power upper bound for the actual full-triple endpoint gcd follows. It remains restricted to p>2n+2 and does not by itself bound that auxiliary integer gcd.

The new rational companion algebra in Section4 also checks. Its error is factorially small because each t_j,g_j is of size exp(O(n))/n!, while delta has the proved factorial lower bound. If S_n is a multiple of n! clearing C_0-C_1, then d_F*S_n*delta is a valid denominator for the companion, with absolute size at most exp(log S_n-log n!+O(n)). Boundedness of the companion controls its numerator as well. Consequently the quoted continued-fraction lower bound for q_n and the sufficient leading exponent3/2-eta are correct. The current clearer has leading exponent2, so the argument remains inconclusive.

## 6. Verification and most useful next problem

`hp_b1_prime_folding_independent_checks.py` uses standard-library exact rational arithmetic. It verifies the full boundary kernel congruence and actual q values at four preselected primes, all coefficients of six harmonic defect polynomials, and the fixed-offset gate at six preselected pairs. All checks pass and are recorded in `hp_b1_prime_folding_independent_checks.json`. There is no matrix scan or prime-density inference.

The n=p-1 result supplies an actual primitive-factor exclusion. Formula(B) gives a concrete first-lift problem at other fixed offsets, but its zeros occur in the actual family. To control those primes in q_n one needs the companion X residue and, at simultaneous zeros, another p-adic digit. A bound for the special H_n(1),J_(n+1)(1) gcd or for the reduced rational companion after endpoint cancellation remains relevant. The coefficient-clearer improvement proposed in the initial arithmetic note has now been ruled out by the independently checked argument in Section7. None of the present statements proves primitive nondecay or irrationality of e+pi.

## 7. Subsequent reproduction obstruction: the coefficient-clearer scale is exact

The arithmetic agent subsequently supplied a short obstruction to its own proposed coefficient-clearer target. I independently verified it; the target is impossible for this actual family.

Put D^*=C_0^*-C_1^*=ell_Delta^(s) K_n(t,s), where ell_Delta=ell_1-ell_0. Kernel reproduction gives, exactly over Q,

    L_t(t^n K_n(t,s))=s^n.

Applying ell_Delta in s therefore gives

    L(t^n D^*)=1/(2n)!-1/(2n+1)!
              =2n/(2n+1)!.

For n>=1, the reduced denominator of this number is exactly `(2n+1)!/(2n)`.

Every monomial moment L(t^k), k<=2n, has denominator dividing `2^k(k+1)`: integrate `((1+iu)/2)^k` termwise or use its endpoint antiderivative. Thus the integer

    d_n=2^(2n) lcm(1,2,...,2n+1)

clears all those moments and has log d_n=O(n).

If S is any positive integer clearing the coefficients of D^*, then t^n S D^* is an integer polynomial of degree at most2n. Therefore

    d_n S * 2n/(2n+1)! is an integer,

or equivalently

    (2n+1)!/(2n) divides d_n S.

Taking sizes gives

    log S >= log((2n+1)!)-log(2n)-log d_n
           =2n log n-O(n).

The established explicit coefficient clearer gives the matching upper bound `2n log n+O(n)`. Hence the least common coefficient denominator of C_0-C_1 has this exact leading scale. Reversal does not change the coefficient denominator, and imposing the additional requirement n! divides S does not change the conclusion because the known upper clearer already has that property.

Consequently no bound `log S <=(3/2-eta)n log n+O(n)`, eta>0, can hold along an unbounded sequence. The proposed route through an improved coefficient clearer is closed. This conclusion concerns the polynomial coefficients. It does not rule out a smaller *reduced* height for the rational companion after division by delta and cancellation of its endpoint numerator and denominator; that remains a separate arithmetic problem.
