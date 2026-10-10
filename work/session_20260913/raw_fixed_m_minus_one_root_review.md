> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent root review: fixed odd multiplier minus-one theorem

2026-09-13, 03:50 UTC. Reviewed
raw_fixed_m_prime_ray_minus_one_denominator.md against the previously
passed cofactor gate, pure Cauchy normalization, and prime-power-minus-one
proof. Verdict: PASS. No new numerical approximants were used.

I checked the theorem for odd m>=1, p>3m, nu>=1, n=m p^nu-1. The claim
is about the actual reduced q_n and not a rescaled polynomial.

1. The denominator lcm has valuation nu because 3m<p. Nonzero Taylor
   residues are exactly odd multiples of T=p^nu, with a common unit
   factor. The m by m blocks reverse to the stated parity Cauchy Gram
   matrices; all their denominators, differences and Legendre normalizing
   factorials are p-units under p>3m.
2. The tall exceptional block has the even degree-(m-1) Legendre null
   vector; its constant is a unit. Removing the last overall row creates
   one short block with the reversed right null vector. The square
   Cauchy matrix therefore has rank exactly n-1, with exactly the two
   stated even residue supports. The zero-dimensional m=1 convention
   agrees with the original theorem.
3. The exact row shift changes the binomial exponent from n to n+1.
   The last actual row is C_n-C_(n+1) modulo p. Its first term fills
   the missing block while its second term has disjoint column residue
   support. This proves full actual rank and unit ordinary cofactor
   content. Transferring the left null vector through G^T introduces
   coefficients (m+a)T, all zero modulo p. Supported row indices are
   even, so the signed cofactor ratios introduce no missing minus sign.
4. The endpoint row equals one on that support. Its sum gives precisely
   Q_(m-1)(1)/Q_(m-1)(0), so the unit seed criterion concerns K itself.
   Every supported weighted coefficient c_r contains (m+a)T; all other
   cofactors are p-divisible. Thus d>=1 is justified independently.
5. The pure Cauchy determinant ratio is 1/Q_n(0). Doubling n/2 has
   no base-p carries; adding n to n has exactly nu, with no extra top
   carry because 2m-1<p. Consequently its valuation is exactly nu.
6. The normalized correction E is integral. On the two null supports,
   for s<p the binomial has valuation nu and the Taylor denominator
   loses at most one extra p-power before multiplication by L. At the
   boundary nu=1,s=p-1, the remaining multiplier h+1 is less than p.
   For s=p the Taylor index is even and the term vanishes. For s>p,
   (s-1)! is p-divisible. This covers every summand, not just a leading
   range, and proves the linear determinant correction vanishes modulo
   p^(nu+1). All higher corrections contain T^2, whose valuation is at
   least nu+1 even when nu=1. Thus d+v_p(V(1))=nu exactly.
7. The integral border Pe=sum V_r D_(n,r), D_(n,r)=1 mod(n+1),
   transfers this valuation because d>=1 makes v_p(V(1))<nu. Hence
   d+e=nu. The factorial ratio has valuation
   r_p=m(p^nu-1)/(p-1), and the arctangent bound is strictly deeper
   than e whenever nu>=2 or m>=3. At m=1,nu=1, Z is a unit and
   the reduced denominator conclusion follows without assuming N unit.

Therefore the exact result is

    v_p(q_n)=m(p^nu-1)/(p-1)-nu+kappa_p,
    kappa_p>=0,
    kappa_p=0 iff Q_(m-1)(1) is a p-unit.

The explicit seed Q_4(1)=68/35 gives an extra factor at m=5,p=17.
No higher seed depth was inferred. This does not extend to arbitrary
p-free multipliers or permit combining incompatible rays at one index.
