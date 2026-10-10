> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Paired derangement determinant: analytic gate

Author: Agent 3, 2026-10-02. This is original analysis of Root's M22 fixed construction, not an audit. All new work is confined to this agent directory.

## Target and archive gate

The target is the actual determinant from the primitive scalar polynomial q_n(y), with n=2k-1 and rho(y^j q_n)=0 for 0<=j<n, where rho(y^r)=D_{2r}-(-1)^r. Root owns the exact rational coefficient and primitive-content interface. The analytic question is the full signed determinant at S=e+pi and its actual center, retaining both exponential and arctangent integrals.

The archive searches used the following expressions in work/ and sources/, restricted to Markdown:

```
(D_\(2|D_\{2|derangement).{0,70}(orthogonal|Hankel|pushforward|delta)|pushforward.{0,50}(exponential|exp|negative)|Uvarov.{0,50}(derangement|negative|delta)|even.{0,30}scalar.{0,30}orthogonal|rho.{0,30}q_n.{0,30}(orthogonal|delta)
negative.{0,20}(mass|atom)|Uvarov|D_\(2r\)|D_\{2r\}|pushforward.{0,30}square
```

The first search had no matches. The second returned earlier even-derangement congruences and an unrelated two-seed Weyl/Nikishin negative-measure experiment. The main-directory filename search for M22, EVEN, ORTHOGONAL, DETERMINANT, SCALAR, and RANK initially found only the unrelated gauged divisor/grid note. No completion of this exact signed scalar/actual determinant target was identified in these bounded searches. This is not a claim of global novelty.

Root then supplied `main/PAIRED_DERANGEMENT_LINEAR_S_CERTIFICATE.json` and the read-only driver `work/research_root/paired_derangement_determinant.py` in the projectless working directory. These are exact finite matching/content receipts with diagnostic real values, not an analytic theorem.

## Fresh primary-literature gate

Queries searched online:

* `site:arxiv.org Uvarov modification negative mass orthogonal polynomials zeros external mass point`
* `site:arxiv.org Hankel determinant moment derangement exponential pushforward square orthogonal polynomial`

Primary full papers opened:

* Delgado, Fernandez, Perez, Pinar, *Multivariate Orthogonal Polynomials and Modified Moment Functionals*, https://arxiv.org/pdf/1601.07194. Section 3, especially Theorem 3.1, supplies the classical Uvarov finite-rank kernel formula and non-singularity criterion. Its general theorem assumes quasi-definiteness. Our rho has rho(1)=0, so that global hypothesis fails; the finite-degree formula must be derived directly at the nonsingular sizes instead of invoking a full orthogonal sequence.
* Krattenthaler, *A determinant identity for moments of orthogonal polynomials that implies Uvarov's formula for the orthogonal polynomials corresponding to a rationally modified weight*, https://arxiv.org/pdf/2103.03969. This is primary overlap for moment/characteristic-product determinants and rational modifications. It does not identify the full mixed exponential/arctangent matrix in this construction.
* Arceo, Huertas, Marcellan, *On polynomials associated with an Uvarov modification of a quartic potential Freud-like weight*, https://arxiv.org/pdf/1505.01528. It treats a positive added mass for a quartic weight, so its zero/asymptotic results do not directly establish the present negative exterior atom or actual determinant.

Classical kernel and determinant identities will be attributed as such. New claims require a proof for the precise rho and complete M22 matrix.
