> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the b=2 contiguous endpoint bridge

Date: 2026-09-13. Reviewer: audit_sources. **FULL PASS after the explicit
nonzero-denominator scope clarification described below.**

Reviewed in full: hp_b2_contiguous_endpoint_arithmetic.md, against the
exact projection and raw cross-product conventions in
hp_b2_endpoint_attempt.md. The universal symbolic checker
check_hp_b2_contiguous_formal_identity.py was rerun unchanged and passed
both endpoint identities. No degree or prime sample was generated.

## 1. Integer Legendre and second-kind normalization

The leading coefficient of
L_k=2^k i^k P_k(-i(2t-1)) is
ell_k=2^k binom(2k,k). Its exact squared moment is



$$
{\cal L}(L_n^2)=\frac{(-1)^n2^{2n+1}}{2n+1}.
$$



Since ell_(n+1)/ell_n=4(2n+1)/(n+1), the CD denominator is



$$
G=\frac{\ell_{n+1}}{\ell_n}{\cal L}(L_n^2)
 =\frac{(-1)^n2^{2n+3}}{n+1}.
$$



This verifies both the magnitude and the alternating sign in (1).
Integration of the CD identity gives
A w_U-B w_P=G with the source's convention (P-A)/(t-1).

The projection remainder is indeed
D/(1-t)-pi K_n(1,t), where
D=(w_UP-w_PU)/G and D(1)=1. The elementary identity



$$
\ell_j(Q/(1-t))=eQ(1)-T_j(Q)
$$



is justified by absolutely convergent factorial sums. It gives the
actual reconstructed A_j(1), not merely a logarithmic or exponential
tail. The e terms cancel exactly. Both formulas (3) check.

## 2. Endpoint determinants and all scalar factors

The raw cross-product convention gives
Y=det(a,1+t,1) and X=det(a,1+t,x). The differences of the T columns
are exactly a_1,a_2 and r_1,r_2. Direct expansion gives all three
determinants quoted in Section 2.

The coefficient determinant expressing t,x in the T(U),T(P) rows is
-1/G. This supplies the minus sign on a_0 W and gives exactly



$$
Y=(B{\cal C}-A{\cal S})/G,\qquad
 X=((w_P+T_P){\cal S}-(w_U+T_U){\cal C}-a_0{\cal W})/G.
$$



I checked these expansions independently before rerunning the saved
formal-variable certificate. Both routes agree. Replacing monic U by
the integer L_(n+1) multiplies the cross-product scale uniformly and
does not change X/Y.

Rodrigues identity (8) has the correct x^k factor and scalar
2^k/(k!)^2. Its first three derivatives give precisely the H,J,K,M
definitions. In particular the second derivative includes 2k H',
and the third includes 3k(k-1)H' and 3kH''.

The five transforms in (7), g/f=2/(n+1)^2, and the substitutions
into (5) give exactly D_n and X_n in (9)--(11). The term
-2f H_(n+1) W in the rational numerator retains its necessary f
factor. None of the partial-exponential or second-kind contractions
has been discarded.

## 3. Integral presentation and scope

The quotient defining w_U has degree n, and w_P has lower degree.
The stated bound 2^(n+1)(n+2)! for their moment denominators is
conservative. The largest E index in T_U is 2n+1. Thus
Lambda=2^(n+1)(2n+2)!(n!)^2 clears every displayed term, including f.
No minimality is needed for the exact reduced-denominator formula.

At p>2n+2, Lambda is a unit and X_n,D_n are p-integral. Formula
(13) is therefore exactly the valuation of the reduced ratio, with
all cancellations retained.

The only requested clarification was to state explicitly that every
formula involving X/Y, q, or division by D_n assumes Y!=0,
equivalently D_n!=0. The inherited analytic theorem gives this for
all sufficiently large n, not all n>=2. The author incorporated that
sentence before this final PASS. The polynomial identities themselves
and the primitive endpoint-gcd statement have their original
unconditional scopes.

## 4. Full-depth primitive endpoint-gcd gate

Let p^d divide the two endpoints of a primitive full integral matched
triple. Matching gives the third endpoint as zero modulo p^d.
Division by z-1 is exact over Z/p^d, reduces the caps to
(n-1,1,n-1), and preserves order 2n+3 at zero.

The quotient B vector must be primitive modulo p. If it vanished,
the first n high logarithmic moments would make quotient C orthogonal
to every polynomial of degree at most n-1. The corresponding moment
matrix is nonsingular modulo p because its Legendre norms and leading
coefficients are units. The low equations would then kill quotient A.
This contradicts primitiveness of the original full triple.

The quotient's high rows have moment indices 0 through n+2. Testing
against L_n,L_(n+1),L_(n+2) removes quotient C. Its two factorial
columns have denominators (n+j)! and (n+j-1)!. The exact derivative
identity therefore gives, up to unit row factors,



$$
(H_n,J_n),\quad
 (J_{n+1},K_{n+1}),\quad
 (K_{n+2},M_{n+2}).
$$



The cutoff p>2n+4 is sufficient. The first n norm factors involve
degrees only through n-1; no norm of L_(n+2) is inverted.
The tests of higher degree use its integral orthogonality and its
p-unit leading coefficient. All needed factorial and Taylor
denominators are units at the stated cutoff.

The resulting 3-by-2 integer matrix has a primitive kernel vector
modulo p^d. Completing that vector to a unimodular two-column basis
puts a zero column modulo p^d in the transformed matrix. Each maximal
minor is therefore divisible by p^d. This proves the full inequality



$$
v_p\gcd(A(1),B(1))\le v_p(\Omega_n),
 \qquad p>2n+4,
$$



including its full prime-power depth. If all minors are zero, the
stated convention correctly makes the bound vacuous.

## 5. Final assessment

This is an actual numerator-and-denominator reduction, together with
a genuine large-prime primitive endpoint-gcd gate. It neither proves
a small-prime denominator lower bound nor removes the independent
contractions from X_n. The existing b=2 prime-family cancellation
obstruction remains consistent with it.

No additional mathematical correction was needed. The final scope
and the separation from the completed raw-family exclusion are sound.
