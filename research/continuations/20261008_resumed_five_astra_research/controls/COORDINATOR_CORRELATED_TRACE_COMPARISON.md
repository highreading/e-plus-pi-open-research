> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Correlating the two independent inverse-moment arguments

Coordinator derivation,8October2026. A proposed sharper SAME-H theorem for
independent review. It combines the two independent new derivations, and does
not settle the actual primitive denominator or the rationality of e+pi.

## 1. Inputs and scope

Reuse A5turn0's directly checked integration-by-parts trace estimate

    tr(M_0^(-1) M_-1) <= a_k=1/(4k-2),                (1)

for the SAME reference Gram matrices ((2k+2i+2j)!) and
((2k-2+2i+2j)!). The proof is in A5turn0 Section6. It is independent of the
parent's Gauss-Laguerre proof and uses no moment after6k-4. All matrices here
are real positive Gram matrices; final integer H coefficients remain intact.

Reuse the parent correlated positive exterior identities in Section8 of
COORDINATOR_UNIFORM_GAMMA_COMPARISON.md. These are proposed and currently in
independent review. Write E_D,E_S for the exterior-only normalized numerator
and slope, and R_k=J_k(nu)/J_(k-1)((1+y)^2nu). Integrating the compact variables
first and applying the Christoffel variational inequality gives

    R_k mathcal_S_minus <= mathcal_D_ext <= R_k mathcal_S_ext.   (2)

Here the raw S_minus differs from raw S_ext only by replacing the exterior
product prod(x_i+1) by prod(x_i-1). This identity retains the same compact
weight and the same number k-1 of compact variables in both slope integrals.

## 2. A trace comparison retains the determinant loss

For each compact tuple y_1,...,y_(k-1) in[0,1], define exterior Gram matrices
B_plus,B_minus for weights

    (x+1) prod_j(x-y_j),  (x-1) prod_j(x-y_j), x>1,

with the exact exterior measure dmu=e^(-1-sqrt(x))dx/(2sqrt(x)). Their
positive difference is2C(y), where C has weight prod_j(x-y_j).

On x>1, C(y)<=e^(-1)M_-1 as a matrix: prod_j(x-y_j)<=x^(k-1), and x=t^2.
Also Q_plus(x)>=x prod_j(x-y_j)>=x^k-(k-1)x^(k-1), by Bernoulli.
For0<x<=1 the right side is nonpositive for k>=2, so its integral over that
interval can be added to the lower bound. Consequently

    B_plus >=e^(-1)(M_0-(k-1)M_-1).                  (3)

Since the normalized inverse matrix in(1) is positive, its largest eigenvalue
is at most its trace. Thus M_-1<=a_k M_0, and(3) implies

    B_plus >= e^(-1)c_k M_0,
    c_k=1-(k-1)a_k=(3k-1)/(4k-2)>0.                  (4)

Put L_y=2B_plus^(-1/2)C(y)B_plus^(-1/2). It is positive, and inverse order
in(4), followed by trace order for positive matrices, gives

    tr L_y <= (2/c_k) tr(M_0^(-1)M_-1)
              <=2a_k/c_k=2/(3k-1)=eta_k.            (5)

For k>=2, eta_k<1, so every eigenvalue of L_y is in[0,1). The elementary
inequality prod(1-lambda_i)>=1-sum(lambda_i) therefore gives

    det B_minus/det B_plus
       =det(I-L_y)>=1-eta_k.                         (6)

This uses a TRACE bound on the full determinant loss. Replacing it by k times
a spectral norm would unnecessarily lose a factor of k. All inequalities
hold for every compact tuple, hence survive its positive integration.

Equations(2) and(6), with their original J normalizations, give

    (1-eta_k) E_S <= E_D <= E_S.                     (7)

The largest compact moment in these integrations is3k-2. The exterior weights
have degree k, and the largest factorial remains6k-4. No successor is used.

## 3. Restore the complete signed determinants before forming the ratio

A5turn0 Section7 gives E_S>=c_k e^(-k)Z_k, directly from the same exterior
ensemble product. Note c_k>=3/4. The accepted COMPLETE overlap and atom bounds,
not an unsigned substitution, give for k>=64

    |D_k-E_D| <= e^(-k)Z_k d_k,
    |S_k-E_S| <= e^(-k)Z_k d_k^+,
    d_k,d_k^+<=2*4^(-k).

Thus both losses are at most tau_k E_S, where

    tau_k=(8/3)*4^(-k).

Combining with(7), the proposed sharpened full theorem is

    (1-eta_k-tau_k)/(1+tau_k)
       <= eps_k/R_k <= (1+tau_k)/(1-tau_k), k>=64.    (8)

Its numerator is positive. In particular eps_k/R_k tends to1 with the explicit
relative lower loss eta_k+2tau_k and upper loss2tau_k/(1-tau_k).
No strong compact-polynomial asymptotic theorem is presumed.

The already accepted R bounds with A=17+12sqrt(2) and the quarter contraction
remain valid. Formula(8) sharpens their constants but does not supply any
actual arithmetic restriction on q_k or G_k. All final gcd payments are
unchanged. The coefficient ratio proves the ordinary error only.

## 4. Referee obligations

Independently verify(3) outside and inside the physical interval, inverse and
trace directions in(5), determinant positivity in(6), both compact/raw
normalizations in(2)/(7), and the full negative-atom/overlap restoration in(8).
Any problem with the pending parent correlated integral identity must be
reported before using this sharpened conclusion. The independently derived
A5turn0 constant-factor ordinary-error theorem remains available separately.

Overlap gate: this is a new elementary combination of two explicit same-pencil
proofs already generated in this active round. Classical integrations by parts,
Andreief, variational minima and matrix trace inequalities are reused. The
scoped archive/literature gate is INVERSE_ENSEMBLE_AND_ARITHMETIC_GATE.md;
no global novelty assertion, new experiment or imported ensemble formula occurs.
