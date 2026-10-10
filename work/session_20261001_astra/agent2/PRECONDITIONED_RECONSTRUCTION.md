> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Factorially weighted finite reconstruction

Status: new author deductions, not independently reviewed. The main POSITIVE_FORCING_EVEN_NORMALITY_TAU_DRAFT.md and ADAPTIVE_ARC_INVERSE_DRAFT.md were read as author dependencies. LOGARITHMIC_FORCING_VECTOR is preserved without replay. No scans, computations, or independent audits are performed.

## Fixed center and coordinates

Assume even n>=16 and 3<=b<=n. Put d=b-1, m=floor((b-1)/2), N=n+m+1, r=N-b, R=sqrt(2), M=1+R. Fix exactly the existing factorial weights

    w_j=r!/(N-j)!, 0<=j<=b,
    S_B=diag(w_0,...,w_b), S_v=diag(w_0,...,w_d),
    W=S_B^2.

The actual B-only rational center is t=u^T W v/(u^T W u), where

    H=(I+D)^(-n), K=D_B H,
    u=K T^(-1)f_P,
    v=e_0+K T^(-1)f_Q.

Here D differentiates polynomials of degree at most d and D_B multiplies by z-1. All coefficients are ordinary ascending coefficients. The actual endpoint constant e_0 remains present. No new center is introduced.

The exact complete forcing decomposition is

    f_Q=S f_P+e_F+e_E, S=e+pi.

Thus v-Su=e_0+K T^(-1)(e_F+e_E). This identity combines the two actual forcing columns before any estimates.

## Weighted differential cancellation

Define

    A=(n+d)/(r+1), C_H=b(1+A)^d.

For i<=j and l=j-i the exact finite inverse entries are

    H_ij=(-1)^l binom(j,l)(n)_l,
    w_i/w_j=(N-j)!/(N-i)!,

where (n)_l is a rising factorial. Therefore

    |(S_v H S_v^(-1))_ij|<=binom(j,l) A^l.

Indeed each numerator factor in (n)_l is at most n+d, and each denominator factor in the weight ratio is at least r+1. The same bound holds for H^(-1)=(I+D)^n: its rising factorial is replaced by n(n-1)...(n-l+1), with zero entries when l>n.

Each column sum of either absolute matrix is at most (1+A)^d. Bounding its Frobenius norm by its entrywise sum gives

    ||S_v H S_v^(-1)||_2<=C_H,
    ||S_v H^(-1) S_v^(-1)||_2<=C_H.                 (1)

This is cancellation of exact factorial ratios inside each entry, before absolute values. It does not delete the weights. For b=o(n), A=1+O(b/n), so

    log C_H=O(b+log b).

Both directions of the finite reconstruction are controlled in the same norm. An upper bound for H alone would not supply the first-column lower bound needed below.

## Multiplication by z-1 and its inverse on its image

The weighted matrix S_B D_B S_v^(-1) is the sum of a negative diagonal embedding and a shifted embedding with coefficients

    w_(j+1)/w_j=N-j.

Consequently its Euclidean operator norm is at most N+1.

For B=(z-1)y, the exact reverse cumulative identity is

    y_j=sum_(i=j+1)^b B_i.

Its weighted coefficients satisfy

    w_j/w_i<= (r+1)^(-(i-j)), i>j.

The associated rectangular matrix has every absolute row sum and column sum at most sum_(l>=1)(r+1)^(-l)=1/r. Hence its Euclidean norm is at most 1/r. Thus

    ||S_B D_B y||_2> = r ||S_v y||_2,
    ||S_B D_B y||_2<= (N+1)||S_v y||_2.              (2)

The spaced inequality in the first line means greater than or equal to. These identities use the image condition B(1)=0, which holds for u and the reconstructed residual excluding e_0. They are not applied to e_0 itself.

Combining (1)-(2), for every transformed polynomial x,

    r/C_H ||S_v x||_2<=||S_B Kx||_2
                            <=(N+1)C_H||S_v x||_2. (3)

## Coordinate conversion: the remaining cost

Let D_R=diag((-R)^j), 0<=j<b. The diagonal magnitudes of S_v D_R^(-1) are w_j/R^j. They increase with j, since (N-j)/R>1 in the domain. Therefore

    w_0||D_R x||_2<=||S_v x||_2
                         <=(w_d/R^d)||D_R x||_2.

Define their exact ratio

    C_w=w_d/(R^d w_0)=N!/((N-d)! R^d).              (4)

This ratio remains in the proof. Conjugating the Toeplitz inverse by S_v instead of D_R cannot, from the available norm estimates alone, remove it. Indeed the standard conjugation bound introduces exactly the condition number C_w. Calling the conjugated matrix a new preconditioned inverse would not prove a gain.

No lower bound saying that the actual inverse attains this loss is claimed. Its removal would require additional directional information about T^(-1)f_P and T^(-1)(e_F+e_E). Formula (4) diagnoses the precise remaining conversion loss of this argument.

## Both reconstructed forcing columns

Write F_P=||D_R f_P||_2. The main drafts supply the following author dependencies:

    ||D_R T D_R^(-1)||_2<=9M^n,
    ||D_R T^(-1)D_R^(-1)||_2<=K_adapt M^(-n),

    K_adapt=512 sqrt(bn) exp(b)
                (16bn)^d binom(2d,d)/(d!)^2.

Apply the forward bound to x=T^(-1)f_P and then use (3)-(4). This gives a genuine first-column lower bound

    ||S_B u||_2>= r w_0 F_P/(9 C_H M^n).             (5)

For the other column, retain its difference from S times the first column. Equations (3)-(4) give

    ||S_B(v-Su)||_2
      <=w_0+(N+1)C_H(w_d/R^d)K_adapt M^(-n)
                    ||D_R(e_F+e_E)||_2.             (6)

The endpoint term is exactly ||S_B e_0||=w_0. Both complete residuals remain in (6); their signed sum is retained until the following explicit upper bound is used:

    ||D_R(e_F+e_E)||_2
      <=2sqrt(pi b/n)n!M^(-n)+27sqrt(b)M^n/(n+1).   (7)

The logarithmic bound is the existing author vector result; the exponential bound is the author input in the main draft. No additional cancellation between the two residuals is assumed.

Weighted Cauchy-Schwarz and the actual lower bound (5), not a quotient of upper bounds, prove

    |t-S|<=B_rec,

    B_rec=9 C_H M^n/(r F_P)
       +9(N+1)C_H^2 C_w K_adapt/(r F_P)
          [2sqrt(pi b/n)n!M^(-n)
                         +27sqrt(b)M^n/(n+1)].     (8)

This bounds the two reconstructed columns together. The cancellation of common coordinate factors w_0 is legitimate because (5) and (6) were derived in the same fixed norm. The remaining factor is exactly C_w, not the previous product of two unweighted differential norms and a smallest-weight loss.

## Explicit complete envelope and growing range

The main positive-forcing draft supplies, as an author dependency,

    F_P>=n!M^(n-1)sqrt(2^b-1)/sqrt(n).

Define

    J=9M C_H sqrt(n)/(r sqrt(2^b-1)).

Substitution in (8) yields the complete explicit envelope

    B_rec<=J/n!
       +J(N+1)C_H C_w K_adapt
          [2sqrt(pi b/n)M^(-2n)
                       +27sqrt(b)/((n+1)n!)].     (9)

The first term is the endpoint constant. The last factorial term is the complete exponential residual. The geometric term is the complete logarithmic residual. None is omitted.

For fixed beta>0 and even n tending to infinity, take

    b=floor(beta n/log n).

Eventually all the domain conditions hold. In this allocation,

    log C_H=o(n), log K_adapt=o(n),
    log C_w=d log n-d log R+O(b^2/n)=beta n+o(n).

The other dimension factors in (9) have logarithm o(n). Thus its geometric term has logarithm

    -[2log(1+sqrt(2))-beta]n+o(n),

whereas its two factorial terms have logarithm -n log n+O_beta(n). Therefore

    |t-(e+pi)|<=exp(-[tau-beta]n+o(n)),
    tau=2log(1+sqrt(2)).                             (10)

The complete envelope decays for every fixed 0<beta<tau. This replaces the former conservative restriction beta<tau/3, preserving precisely the same rational B-only center and factorial norm. It is a new author consequence conditional on the named even-normality, adaptive inverse, positive forcing, and complete residual inputs.

For a more general quantitative selection one can use the explicit positive expression (9) directly. The asymptotic claim (10) does not assert a sign or a matching lower rate for the actual error.

## Complete forms, denominators, and the stopping boundary

The directional complete-form bound is

    |P+Q(e+pi)|<=|P+tQ|+B_rec |Q|.

For the actual reduced center t=p/q, choose qx+py=1 and |y|<=q/2. The primitive pair obeys

    |-p+q(e+pi)|<=q B_rec,
    |x+y(e+pi)|<=1/q+q B_rec/2.

The center and its reduced denominator have not changed. Each minimal integral lift multiplies the coefficients and its endpoint gcd by the same factor, which cancels separately for each pair. A coefficient clearer, a conjugation scale, or a lattice index does not replace q.

No favorable denominator estimate is obtained. A sufficient conditional arithmetic target for this allocation is q->infinity and limsup log(q)/n<tau-beta.

The proved reconstruction cost in its compatible factorial coordinates is exp(O(b+log b)). The full propagation still pays C_w when importing the available Toeplitz inverse estimate. An exp(O(b log(n/b))) cost for this entire conversion has not been proved. Attempting to remove C_w merely by diagonal conjugation returns exactly the same factor and that shortcut is stopped. Further improvement requires an actual directional estimate across the transformed inverse, rather than another upper norm of H alone.

No scans, repeated successful checks, or independent review were performed. Earlier results are preserved. Read-back of this file and PRECONDITIONED_RECONSTRUCTION_REPORT.md is required before reporting completion.
