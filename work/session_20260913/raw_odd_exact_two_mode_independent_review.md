> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the exact odd two-mode factorization

Date: 2026-09-13. Reviewer: audit_sources.
Target: raw_odd_exact_two_mode_boundary_matrices.md.
Result: **FULL PASS. No correction required.**

## 1. Symbol, operator domains and invertible base product

On the unit circle J=[[0,t],[1,0]] satisfies J*J=JJ*=I. Thus it is normal with eigenvalues z,-z, |z|=1, and the eigenvalues of E=exp J are e^z,e^-z. Their real parts are at least e^-1 cos(1), proving the stated pointwise accretivity and norm bounds without a square-root branch choice.

The equality a0=J/(1+t) shows both a0E=Ea0 and the exact actual-symbol factorization. The rational multiplier is selfadjoint on its natural domain. Its simple pole is square-integrable on every polynomial and on E times every polynomial under the weight |1+t|^(2m+2), including m=0. Its finite restriction a0P is bounded. The bound sqrt(5/4) follows exactly by lowering the weight exponent by one and applying the previously proved positive-weight comparison.

The notation Pa0 beyond the natural multiplication domain is correctly defined as (a0P)*. It agrees with multiplication followed by projection whenever that multiplication is defined. Consequently all later adjoint identities are legitimate, rather than formal manipulations of an unbounded multiplier.

For K=P_s[t/(1+t)]P_s, pointwise conjugation gives K*=P_s[1/(1+t)]P_s. Their sum is I. Hence Re K=I/2 and ||Ku||>=||u||/2. In finite dimension K is invertible with inverse norm at most two. The same holds for A0=[[0,K],[K*,0]]. The compression E0 retains accretivity, so Q=(A0E0)^-1=E0^-1A0^-1 has the displayed uniform bound 2e/cos(1).

## 2. Exact boundary maps and correction sign

Let h=(I-P_s)/(1+t) and rho=||h||. It is nonzero: a rational function with its nonremovable pole cannot agree almost everywhere with a polynomial on the circle. Polynomial division yields


$$
(I-P)a_0(u,v)=(-v(-1)h,\ u(-1)h).
$$


Thus (I-P)a0P=Hhat J0 Lambda with exactly the J0 and rho factors in the source. Hhat J0 is an isometry, so the inherited bound on Lambda is valid.

Adjointing gives


$$
Pa_0(I-P)=\Lambda^*J_0^*\widehat H^*.
$$


Multiplication by EP therefore yields the exact correction


$$
A=A_0E_0+UV,\quad U=\Lambda^*,\quad V=J_0^*\widehat H^*EP.
$$


There is no missing minus sign or rho. The exponential factor is complete, not truncated.

## 3. Two and three exceptional singular modes

The right-inverse identity AQ=I+UVQ has rank-at-most-two correction. On its correction kernel it is the identity, so min-max and s_j(AQ)<=||Q||s_j(A) prove the N-2 bound exactly.

For the actual endpoint vector v and Pi=I-vv*, on v-perpendicular,


$$
BQ_B=I+\Pi UVQ\Pi-\Pi A v v^*Q\Pi.
$$


The new term has rank at most one. The space has dimension N-1, hence the index N-4 and the count of at most three exceptional modes are correct. Projection does not require an independent norm estimate for the compressed inverse.

## 4. Bounded-size matrices and the scalar quotient

D2=I+VQU is the correct determinant-lemma matrix for A=T+UV, T=A0E0. The actual nonvanishing theorem makes D2 invertible. Woodbury gives


$$
A^{-1}=Q-QU D2^{-1}VQ.
$$


In the stated D3, the scalar Schur complement is


$$
v^*Qv-v^*QU D2^{-1}VQv=v^*A^{-1}v=1/s_m.
$$


The positive lower-left block is therefore correct; placing a minus there would be wrong. It follows that det D3=det D2/s_m and det B=det T det D3. The actual high-compression theorem supplies the nonvanishing of D3.

All exterior operator norms in these formulas are uniform in m, so the fixed-size matrices have uniformly bounded entries. Such upper bounds do not lower-bound their determinants. The stated remaining condition
log|det D2|-log|det D3|=o(m)
is exactly equivalent to the odd scalar target, with no growing determinant normalization omitted.

The conditional full-inverse bound in (14) follows directly from Woodbury and the displayed U,V,Q bounds.

## 5. New exact boundary data, kept separate

The separate continuation raw_odd_explicit_circle_boundary_kernels.md derives explicit finite kernels and rational base inverses. In particular it sharpens the source's valid estimate on Lambda to


$$
\|\Lambda\|^2=
 \frac{3(m+1)^2}{4(2m+1)(2m+3)}\le\frac14.
$$


This refinement is not required for any of the audited arguments.

The exact rank-two theorem is valid at the actual exponential parameter 1. It does not establish nonzero limiting boundary determinants or a quantitative real lower bound. The five-mode predecessor remains correct but is quantitatively superseded by the two/three exceptional-mode counts.

