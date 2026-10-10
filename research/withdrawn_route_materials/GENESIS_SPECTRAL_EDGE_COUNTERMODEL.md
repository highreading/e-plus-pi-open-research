> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Genesis nonlocal spectral candidate: exact object and failed rigidity bridge

Date: 2026-10-03 local time. Agent 3. Original structural screening, not a review. Candidate status: DISCARDED as an irrationality route. The operator identities below are saved as falsification data; their classical parts are attributed explicitly.

## Candidate, exact rationality link, and gate

The candidate sought to turn a rational spectral endpoint of a rational-entry positive operator into an actual eigenvalue or an algebraic finite certificate. A noncommuting analytic return operation could then potentially be tested at that certificate. The concrete operator below has upper spectral endpoint S=e+pi, so rationality of S would make this endpoint rational. The proposed general endpoint-to-eigenvalue implication is falsifiable and false; no narrower arithmetic implication is assumed.

Archive query: `Hilbert matrix|Hilbert operator|Toeplitz operator|spectral edge|spectral radius|tensor sum|Kronecker sum|arithmetic spectrum|resolvent.*branch`, across the full research directory, Markdown files. Located old finite Hilbert Grams and Toeplitz/resolvent approximation constructions, including `work/session_20260913/raw_arctan_inverse_norm_attempt.md`, `raw_inverse_norm_independent_extension.md`, and the old limiting boundary symbols. Those are different from this infinite tensor operator. No exact tensor object was located in that bounded archive query; this is not a global novelty assertion.

Fresh online mechanism queries:

- `Hilbert matrix operator pi spectral representation Rosenblum primary paper diagonalization`
- `rational operator spectral radius transcendental norm Hilbert matrix factorial Toeplitz operator e pi`
- `integer adjacency operator spectral radius rational infinite graph limit points Hoffman spectrum`
- `spectra tensor product sums bounded self adjoint operators primary tensor sum spectrum paper`

Opened primary source: Kalvoda–Štovíček, *A family of explicitly diagonalizable weighted Hankel matrices generalizing the Hilbert matrix*, https://arxiv.org/pdf/1506.01064, especially Section 4.1, formula (19), the transform with multiplier pi/cosh(pi x), and Theorem 8. It reproves Rosenblum's Hilbert-matrix spectral description; this description is classical background, not a newly created tool. Opened *On the spectrum of Hilbert matrix operator*, https://link.springer.com/article/10.1007/s00020-021-02637-5, including its explicit spectral statements. The attempted Ichinose AMS PDF URL and White Mathdoc fetch failed, so neither supplies a read theorem here. Tensor endpoint addition is proved elementarily below instead of relying on those failed fetches.

Public overlap: tensor sums and spectral convolution are existing tools. The only intended new ingredient was rational endpoint rigidity. The countermodels below reject it. Merely representing S as a norm is not a retained Genesis mechanism.

## 1. A positive rational-entry operator with norm e

On ell^2(Z), let A be the convolution operator with coefficients

    a_0=1,  a_n=1/(2|n|!) for n!=0.

The coefficients are absolutely summable. Fourier transformation makes A multiplication by

    phi(theta)=1+sum_(n>=1) cos(n theta)/n!
              =exp(cos theta) cos(sin theta).

This is strictly positive since |sin theta|<=1<pi/2. Also phi<=exp(cos theta)<=e, with equality at theta=0. Hence A is positive, all its matrix entries are rational, and ||A||=e. The top endpoint is not an eigenvalue: the set {theta:phi(theta)=e} consists of theta=0 modulo 2pi and has measure zero.

## 2. The complete S operator

Let H on ell^2(N_0) be the Hilbert matrix H_ij=1/(i+j+1). The opened primary theorem gives H>=0, ||H||=pi, and no point spectrum. Put

    K=A tensor I + I tensor H.

All standard-basis matrix entries of K are rational and K>=0. The upper bound ||K||<=e+pi follows from the operator norm triangle inequality. For every epsilon>0, choose unit vectors u and v with

    <Au,u>>e-epsilon,  <Hv,v>>pi-epsilon.

Then <K(u tensor v),u tensor v>>S-2epsilon. Therefore

    ||K||=sup spectrum(K)=S EXACTLY.

Moreover S is not an eigenvalue. If K w=S w, positivity gives

    0=<[(eI-A) tensor I + I tensor (pi I-H)]w,w>.

Each summand is nonnegative, so [(eI-A)^(1/2) tensor I]w=0. A has no eigenvalue e, and the tensor kernel is zero; hence w=0. This conclusion is unconditional and does not conflict with a hypothetical rational S: rational continuous-spectrum endpoints are possible.

## 3. A positive INTEGER-entry countermodel

Let U be the bilateral shift on ell^2(Z). T=2I+U+U^* is positive, has integer entries, spectrum [0,4], and no eigenvalue 4. Its Fourier multiplier is 2+2cos theta. Thus even positivity plus integer entries plus a rational upper edge does not force an edge eigenvector, a finitely supported state, or finite-dimensional collapse.

The two-component version T tensor I+I tensor T has rational upper edge 8 and no eigenvector there. It preserves the exact tensor-addition architecture used for K. Consequently the broad rational-edge rigidity target is falsified before any arithmetic conclusion is attempted.

## 4. Rational entries do not make an arithmetic operator algebra

There is a second exact obstruction to a proposed rational-return method. Although every H_ij is rational,

    (H^2)_00=sum_(j>=0) 1/(j+1)^2=pi^2/6,

which is transcendental. The infinite matrix product is an absolutely convergent sum but is not a finite rational operation. Similarly

    (A^2)_00=1+(1/2)sum_(n>=1)1/(n!)^2.

No rationality of this latter value is claimed or needed. The Hilbert example alone disproves the closure premise. A rational-entry resolvent or return series may introduce additional periods in its first few coefficients, so one cannot transfer integrality/rationality of the original matrix entries to its functional calculus.

## Exact status

The new concrete object has an exact bridge: S is its upper spectral endpoint. It provides no rationality contradiction. The two proposed auxiliary bridges—rational endpoint forces an edge eigenvector, and rational entries force rational return coefficients—are explicitly false. Restricting the endpoint rigidity claim only to this particular K would amount to an unproved separation assertion with no new mechanism behind it. This route is discarded; its norm representation is not counted as a solution or a retained tool.
