> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent root review of paired-log valuation separation

2026-09-13. Reviewed the full proof in
`paired_log_valuation_separation.md` against the already independently
verified original-row bridge and the exact symbolic operators.

**Verdict:** the all-level separation and every fixed fractional-moment
theorem with exponent strictly between0 and1 are valid on the stated
ordinary PNT-side set. The first-moment endpoint remains unproved.
The proposed logarithmic improvement for the common-log support is
also valid by the argument below. It counts t>=1, which is distinct
from the complete first-Witt support d>=1.

## Exact recurrence and state hypotheses

For the original characteristic-zero differential the exponents are
z=6m and -2z/3-1-nu. The rational differential identities therefore
apply literally; taking a residue kills their derivative terms. There
is no characteristic-p primitive selection in this step. Dividing all
three consecutive logarithmic coordinates by the same fixed p gives
the actual state in the depth note.

The earlier full integral bridge, with a common diagonal matrix for
the three shifted rows, proves that this log column is primitive away
from the specified sextic exceptions. This is stronger than just the
nonvanishing of one exterior minor. All three shifted rows must remain
in the same cell; the fixed terminal band is consequently essential.

`check_paired_log_valuation_structure.py` independently parses the
exact rational coefficients, verifies that the proposed common
denominator makes both h numerators integer polynomials of degree12,
and checks the companion's limit and degree17. It also reconstructs
the original C_nu coefficients by a finite integer sum and checks the
characteristic-zero recurrence and contiguity on four distinct rows.
The results are in `paired_log_valuation_structure_checks.json`.
These finite equalities check normalization; the all-index identities
are supplied by the exact differential identity already audited.

## Determinant and uniform valuation bound

The observation rows are e1, h(z), and e1 T_d(z). Their orientation
indeed gives H1 times the third entry minus H2 times the second.
For one and two steps the last observation is respectively e2 and e3.
For all further steps its entries are positive when all arguments are
sufficiently large, since every companion's last row is positive.
Together with h1<0<h2 this makes the actual real determinant strictly
negative, uniformly in the gap. This supplies nonzero integer values
J_d(6m), beyond merely proving the polynomial is not identically zero.

The polynomial degree is exactly17d+12. The stated coefficient norm
bound follows from translation by6h and a submultiplicative matrix
norm. Since d<p and6m<2p^2, its logarithmic height contributes at most
51d+24 plus a term bounded by d+1 for every sufficiently large p,
with an absolute threshold. Thus52d+25 is a valid uniform upper bound.

The adjugate argument uses only p-integral observations and a primitive
state. Unit denominators then identify the determinant valuation with
v_p(J_d(6m)). No inverse of a possibly nonunit determinant is used.
Remove the fixed polynomial singularities and terminal rows once per
cell and split the rest into regular consecutive intervals. This
justifies every intervening transfer and makes the number of removed
positions and intervals absolute, independent of j and the depth.
The resulting weak tail Cp/u+C follows by spacing within each interval.

## Moment estimate and its endpoint

At least one original logarithmic coefficient is nonzero for every
sufficiently large m, by the independently verified nonvanishing of
B_m. The elementary coefficient-height bound therefore yields the
finite depth cap T=O(X/log p). It is legitimate to use the smaller
valuation of the two coefficients even if the other coefficient is zero.

Combining the weak tail with the support estimate, and integrating
theta*u^(theta-1), gives the displayed bound for0<theta<1. The bounded
exceptional positions cost O(T^theta). Summing over O(X/p) cells per
prime and using Chebyshev and partial summation gives an exceptional
total O(X^(1+theta)(log X)^(1-theta)), which is o(X^2) precisely in
this range. On the PNT-side cells,3j+1<=p-1 and r<p/2 in fact imply
6m<p^2, so the lower prime cutoff used in the sum is valid.

The integral at theta=1 has a logarithmic divergence and the exceptional
term loses its power saving. Allowing theta to approach1 without
uniform constants would be invalid. The proof and its limitations
are correctly distinguished in the source note.

## Strengthening the common-log support to O(p/log p)

This is a continuation proposed by the root and independently checked
by the construction agent. Let L be the leading coefficient matrix of
M(z), and let v1,v2 be the leading coefficients of H1,H2. The leading
coefficient of J_d is

    v1(e1 L^d)_3-v2(e1 L^d)_2.

It is a nonzero integer for every d by the limiting sign argument.
There are fixed A>0,B>1 with its absolute value at most A B^d.
Choose D=floor(log p/(2 log B)). For all sufficiently large p, this
leading coefficient is nonzero modulo p for every1<=d<=D. Thus each
J_d has at most17d+12 roots modulo p.

Within a cell, positions are injective modulo p. Delete the roots of
all these J_d, a total O(D^2) positions, and O(D) neighborhoods of the
fixed singular positions and terminal band. If two retained indices
with t>=1 had distance d<=D, the primitive-state argument would force
J_d(6m)=0 modulo p, contradicting their retention. Their distances
are therefore greater than D, so their number is O(p/D). Restoring
the deleted positions gives

    #{m in a fixed ordinary PNT-side cell: t_m>=1}
        <=O(p/D+D^2)=O(p/log p),

uniformly in j. This does not assert the same estimate for the extra
one-copy case d=1,t=0. The older first-Witt estimate is still used for
that separate contribution.

Consequences are a common-log fractional-moment bound with main term
O_theta(p/(log p)^(1-theta)), and zero normalized dyadic average for
the complete clipped depth min(d,K_X) whenever K_X=o(log X). For the
latter, use min(d,K)<=K*1_(t>=1)+1_(d>=1) and retain the earlier
first-Witt support bound. Neither consequence bounds the full
untruncated first moment or any depth outside the specified cell set.
