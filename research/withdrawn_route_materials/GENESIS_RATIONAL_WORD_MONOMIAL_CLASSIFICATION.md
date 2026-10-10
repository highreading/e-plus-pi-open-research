> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact rational-word monomial classification for the two actual laws

Status: proved classical support filter, not a retained Genesis core. Main problem open. Author: root, 2026-10-02. This is original bounded work within the ongoing stage, not a review of Agent3's work and not closeout.

## Gate and distinction from the existing target

Agent3's GENESIS_TWO_LAW_TRANSPORT_COMMUTATOR_GATE.md supplies an exact bilinear equivalence to rational S=e+pi and analyzes one word-order observable. Agent3 confirmed that the ALL finite monomial classification below had not been proved in that note. An inherited archive search for monomial / Mobius / arctan / transport returned only unrelated arctangent-tail monomials. The present goal is a proved boundary for an abelianized observable class; a genuinely noncommuting operator remains a separate possibility.

Fresh public queries used exponential rational functions / logarithm / Mobius cocycle and exponential rational-function independence. Opened NIST DLMF4.23, specifically the inverse-tangent logarithm and general-branch formulas4.23.26/33, https://dlmf.nist.gov/4.23 ; opened primary Adamczewski--Dreyfus--Hardouin--Wibmer, *Algebraic independence and linear difference equations*, https://arxiv.org/pdf/2010.09266 , introduction and precise hypotheses of Theorems1.1/1.3; opened the2026 primary article *Liouville points on rational affine varieties*, https://link.springer.com/article/10.1007/s00013-026-02255-w , which explicitly records exponential-polynomial functional independence as established background. These are essential public elementary exponential/logarithmic normal forms and difference-field machinery. No novelty is claimed for the core.

The 2010.09266 theorems concern specified commuting operator pairs and formal-field hypotheses. They are NOT applied to T/M, which do not commute. Nor is functional independence substituted for numerical independence of e and pi. The classification below has a direct elementary proof.

## Actual operations

Write E(w)=exp(w), A(w)=4 arctan(w). On any local branch avoiding the inverse-tangent singularities,

    exp(i A(w)/2)=(1+i w)/(1-i w).

Changing the arctangent branch adds an integer multiple of4*pi to A, so this exponential is branch invariant. For a finite list g_j in Q(z), and integers n_j,m_j, define the commutative monomial observable

    W(z)=product_j E(g_j(z))^n_j
         product_j exp(i A(g_j(z))/2)^m_j.

All compositions are of the actual laws. We initially exclude poles of g_j and points g_j=±i; meromorphic continuation of the circular factors is then unambiguous. A finite rational-Mobius word is a special case of a rational g_j.

## Complete normal form and functional algebraicity

The exact identity is

    W(z)=R(z)exp(Q(z)),
    Q(z)=sum_j n_j g_j(z) in Q(z),
    R(z)=product_j ((1+i g_j(z))/(1-i g_j(z)))^m_j in Q(i)(z), R≠0.

It follows immediately from multiplication of exponentials and the actual circular identity. This normal form erases the sheet index, while retaining rational singularities of the arguments.

W is algebraic over C(z) if and only if Q is constant. If Q has a finite pole, exp(Q) has an essential singularity there; multiplication by a nonzero rational R cannot remove it. If Q has no finite poles but is nonconstant, it is a nonconstant polynomial and exp(Q) has an essential singularity at infinity. An algebraic function has finite Puiseux branching and no essential singularity, so either case excludes algebraicity. Conversely, for constant Q, W is a rational function with complex constant coefficients.

W is algebraic over Qbar(z) if and only if Q=0. The nonconstant case was already excluded over C(z). For a nonzero rational constant c=Q, suppose R exp(c) satisfied an algebraic equation over Qbar(z). Evaluate it at a rational t outside the finite pole/zero/bad-leading-coefficient set. Then R(t)exp(c) is algebraic and R(t) is nonzero algebraic, forcing exp(c) algebraic, contrary to Hermite--Lindemann. For Q=0, R itself is rational over Q(i).

## Complete numerical specialization in this class

Let t be rational, with every g_j(t) finite. Then all g_j(t) are real rational, so R(t) is a nonzero element of Q(i). The exact numerical criterion is

    W(t) is algebraic  <=>  Q(t)=0.

The forward direction uses Hermite--Lindemann for the rational number Q(t) if it is nonzero; the reverse direction gives W(t)=R(t). This criterion applies even when Q(z) is nonconstant but vanishes at t. Therefore functional transcendence alone cannot be used to infer transcendence at every rational evaluation point.

All these identities and criteria are unconditional. No rational-S assumption is used. If a hypothetical rational r=S is included as a coefficient in rational arguments g_j, the same classification applies for that rational r; this does not establish that any new observable has an arithmetic property forced by the hypothesis.

## Exact finite word receipts

With T(z)=z+1, M(z)=(z+1)/(1-z), J(z)=M²(z)=−1/z, exact symbolic rational-function checks give

    (J T)^3(z)=z,
    T M T J(z)=2z,
    D_2^(-1) T D_2(z)=z+1/2,  D_2(z)=2z.

For P=T M=2/(1-z), B=M T=−(z+2)/z, the observable

    W=E(P)/E(B) * exp(i[A(P)−A(B)]/2)

has

    Q=(2+z−z²)/(z(1-z)),
    R=(i z²+z+3+i)/(z²+i z+1+3i).

These four rational-function identities were independently checked exactly. Unlike a half-exponent normalization, this circular factor has no residual square-root sheet choice. None of these group relations forces a second algebraic replica from r being rational. A conjugated argument identity E(T D_2 z)=e E(D_2 z) still has multiplier e; the separate actual half-translation multiplier is exp(1/2), and arithmetic preservation from r has not been proved.

## Research consequence and precise limit

Any proposed finite commutative-monomial rational-word tool in this class reduces to the established rational-exponential algebraicity test. It is discarded as a Genesis mechanism. The theorem does not classify noncommutative operator sums, nonlinear arguments involving the functions themselves, infinite word limits, or all imaginable rationality-sensitive observables. It supplies no irrationality proof for e+pi and no global exhaustion claim. A next operation must obtain an additional arithmetic consequence from the scalar equality and retain information that this branch-invariant monomial operation discards.
