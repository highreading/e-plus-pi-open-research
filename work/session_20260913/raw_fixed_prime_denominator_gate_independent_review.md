> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the fixed-prime primitive-denominator gate

Date: 2026-09-13. Reviewer: audit_results.
Target: raw_fixed_prime_primitive_denominator_gate.md, all sections.
Verdict: PASS. No mathematical correction required.
A small scope clarification, specifying positive nu / prime divisors of n
in the saturation discussion, was sent to the author.

The proved result is an exact border and a sufficient arithmetic target.
The proposed all-even fixed-prime lower bound is NOT proved. This review
does not promote the target to a theorem.

## 1. Exact reduced denominator and cofactor normalization

The actual endpoint rational is N/Z, with Z!=0 and both integers.
Thus q=|Z|/gcd(|Z|,|N|). The determinant identities retain the
appended n! in Delta_A:

    Delta_B=(-1)^(n+1)F Z,
    Delta_A=(-1)^n n! F N.

Consequently their reduction cancels F completely. The extremal
content is not automatically a divisor of the reduced q.

I checked the cofactor data against the previously passed
raw_endpoint_scalar_cauchy_restriction.md. Its unsigned minors delta_r,
weighted content h=gcd(c_r delta_r), unweighted content Theta,
and polynomial P are the same ones. The exact identity is

    h Qhat=R P,   R=(2n)!/n!,   content(P)=Theta.

The triangular integer coefficient transformation has unit diagonal,
so the content equality includes small primes; it is not a statement
localized only above 3n. Also Theta divides h and h divides R Theta.
For the latter, h divides every c_r delta_r and each c_r divides R,
hence h divides gcd(R delta_r)=R Theta.

Thus, for the source's valuations,

    0<=d=v_p(h)-v_p(Theta)<=v_p(R),
    kappa=v_p(K)-v_p(Theta)>=0,
    v_p(Z)=r_p-d+kappa.

The pair (RK,J_e+4J_a) is exactly (hZ,hN). Its gcd reduction therefore
gives the same q, even though h need not be one. This prevents a
normalization loss at precisely the primes the note studies.

## 2. The positive-integer exponential border and its sign

Applying the endpoint Taylor functional to a monomial
z^(2n-r-s) produces E_(r+s), not E_(2n-r-s).
Consequently the source's row ell_(e,r) follows exactly from P.

The integral identity

    E_k=(1/k!) integral_0^infinity exp(-t)(1+t)^k dt

follows by expansion and the gamma integrals. After substituting it
into ell_(e,r), the numerator sum is the nth derivative of
x^(n+r)(1-x)^n at x=1+t. All required boundary derivatives at x=1
vanish, and polynomial growth is killed at infinity. Transferring
the derivative n times to exp(-t) introduces two cancelling signs.
The remaining factor (1-x)^n contributes the one sign (-1)^n.

This gives exactly

    ell_(e,r)=(-1)^n n! sum_(j=0)^(n+r)
                          binom(n+j,j)/(n+r-j)!.

Multiplication by R yields (-1)^n c_r D_(n,r), where the displayed
D is a positive integer. Therefore

    J_e=sum_r (-1)^(r+n)c_r delta_r D_(n,r).

The last-column cofactor sign is (-1)^(r+n), so the determinant
identity (14), including its outer (-1)^n, also checks. Positivity
of each D does not remove the alternating cofactor signs.

## 3. Every stated finite-precision border reduction is valid

For the first layer, j>=p makes (n+r)_j divisible by p.
For j<p, the denominator j! is a unit and the numerator product
for binom(n+j,j) reduces to the one with n replaced by a_0.
It vanishes after a_0+j reaches p. The other falling factorial
vanishes after j exceeds b_0. This proves exactly the truncated
sum d_p(a_0,b_0), including cases where one endpoint is zero.

At precision p^b, the identity

    (n+r)_j=j! binom(n+r,j)

makes every term with v_p(j!)>=b vanish. Thus j<J_b suffices,
and J_b<=pb follows already from the multiples of p in (pb)!.

For a retained term, writing it as an integer polynomial divided
by j! shows that changing n or r by a multiple of p^(2b-1)
changes its numerator by that same power. Division loses at
most b-1 powers because v_p(j!)<=b-1. Its difference is therefore
zero modulo p^b. This proves the claimed periodicity.

One can regard the truncated sum as running through all j<J_b:
if j>n+r, its falling factorial is exactly zero. Hence the
degree-dependent original upper limit does not spoil periodicity.

These are statements about the scalar border weights. None
controls the weighted primitive cofactor vector with which they
are paired. The source preserves that distinction.

## 4. Separation from the arctangent numerator and the sufficient gate

Every coefficient of P is a multiple of Theta. The arctangent
endpoint Taylor weights have denominators dividing L_(2n), with
v_p(L_(2n))=a=floor(log_p(2n)). Therefore

    v_p(J_a)>=r_p+v_p(Theta)-a,
    v_p(Pahat(1))>=r_p-d-a.

This uses the scaled integral polynomial P, not an assertion that
each unscaled arctangent coefficient is p-integral. The ancillary
divisibility L_(2n)|R also holds: each prime power at most 2n
has a multiple in the interval (n,2n].

If d+e<r_p-a, then e<v_p(Pahat(1)); multiplying the latter by
4 cannot weaken this strict inequality at any prime. Hence
v_p(N)=e without a cancellation ambiguity, and

    v_p(q)=r_p-d+kappa-e>0.

If that strict condition fails, the proposed weaker lower bound
has a nonpositive inner expression. These two cases establish

    v_p(q)>=max(0,r_p-d-e-a)

universally. If Pehat(1)=0, interpret e=+infinity; the strict case
cannot hold and the universal assertion reduces to v_p(q)>=0.
No false inference is made when the two numerator valuations tie.

Legendre's factorial formula gives

    r_p=n/(p-1)+O_p(log n),  a=O_p(log n).

Thus d+e=O_p(log n) would imply the stated fixed-prime lower
bound. It is only sufficient: the nonnegative endpoint excess
kappa can compensate for larger losses. In particular the source
does not prove, or claim, d+e=O_p(log n).

The two losses are correctly identified:
d compares the weighted and unweighted maximal-minor minima,
while e is the valuation of the signed border above the weighted
minimum v_p(h). Matrix rank alone controls neither quantity.

## 5. The actual saturated ray and its limitation

For n=mp^nu with nu>=1 and 3m<p, the passed Cauchy theorem
gives delta_n,Theta,h all p-units. Every c_r for r<n contains
the factor 2n and is divisible by p. Every nonconstant term of
D_(n,n) contains the same factor 2n, so D_(n,n)=1 modulo p.
The signed sum therefore gives J_e=delta_n modulo p, hence
e=0 and d=0.

For n=2p^nu, p>=7, the fixed seed Q_2(1)=4/3 is a p-unit.
The already proved endpoint restriction therefore gives kappa=0.
Moreover

    r_p=2(p^nu-1)/(p-1),   a=nu,   r_p>a.

The strict numerator-separation condition holds, and the exact
reduced denominator valuation is

    v_p(q_(2p^nu))=(2p^nu-2)/(p-1).

No new endpoint unit theorem is assumed in this inference.

The simultaneous-saturation obstruction concerns distinct ODD
PRIME DIVISORS of the same n. If p and q both satisfied the
positive-nu hypothesis, each would divide the other's residual
m, forcing q<p/3 and p<q/3. This is impossible. It does not
exclude simultaneous estimates from a new nonsaturated theorem,
and it is not a counterexample to the conjectured fixed-prime
bound.

The source's general rank formula is restricted to odd p|n and
agrees with the passed Cauchy block theorem, including T<n.
That theorem fixes the nonunit Smith count and the exponents
only through their stated truncation. It supplies no deeper
minor-ratio or endpoint-border estimate by itself.

## 6. Independent exact checks using only the frozen inputs

I independently recomputed the cached reduced denominators from

    raw_accessory_scaling_probe.json
    -> cases -> exact_polynomial_input -> A,B

for the closed set n=2,4,8,16. I summed the exact integer
coefficient lists, formed gcd(sum A,sum B), reduced the
denominator, and checked the exact fixed prime list
2,3,5,7,11,13,17,19.

Every q, raw endpoint gcd and displayed valuation agrees with
raw_fixed_prime_denominator_cached_checks.json. The all-index
dyadic formula also gives exactly the four displayed values.

For the already frozen n=2 normalization, I independently obtained

    (D_(2,0),D_(2,1),D_(2,2))=(19,106,685),

and the signed border with coefficients (940,64,49) gives 44641.
The same endpoint follows directly from the saved primitive
Qhat_2 coefficients and the finite exponential Taylor sums.

These checks are saved in

    check_raw_fixed_prime_gate_existing.py,
    raw_fixed_prime_gate_independent_checks.json.

They construct no polynomial degree and add no index or prime
to the declared diagnostic. The finite checks verify formulas
and normalizations, not an all-even valuation rate.

## 7. Conditional accumulation and the current analytic input

If the fixed-prime lower bound held for every fixed prime, then
for each fixed finite set S the corresponding eventual bounds
could be applied simultaneously. Dividing their sum by n gives

    liminf log(q_n)/n >= sum_(p in S) log p/(p-1).

These finite sums are unbounded without needing a prime-density
theorem: for every integer M,

    log(M!)=sum_(p<=M)v_p(M!)log p
       <=M sum_(p<=M)log p/(p-1),

while log(M!)/M tends to infinity. Thus the hypothetical estimates
would indeed imply log(q_n)/n tends to infinity along even n.

The actual nonzero relative-error asymptotic has now separately
passed review in raw_even_endpoint_residue_independent_review.md:

    |(e+pi)-N_n/Z_n| ~ C_app rho^(5n),  C_app>0.

Combining that accepted ANALYTIC input with the still UNPROVED
fixed-prime hypothesis would force the primitive forms to grow,
and hence would exclude shrinking in this entire even family.
The unreduced Ra asymptotic alone would not have supplied that
implication, as the source correctly warns.

No fixed-prime hypothesis is discharged by the present note.
Neither the conditional growth conclusion nor the proved border
decides the rationality of e+pi.

## 8. Verdict

PASS on the exact integral border, finite-precision reductions,
actual reduced-denominator formulas, strict arctangent separation,
conditional logarithmic-defect target, special ray and its
simultaneous-saturation limitation. The cached checks also pass.

The main proposed all-even fixed-prime bound remains unproved.

