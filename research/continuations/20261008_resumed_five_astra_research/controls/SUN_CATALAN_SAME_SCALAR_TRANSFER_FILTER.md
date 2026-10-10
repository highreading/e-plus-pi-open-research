> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Sun's Catalan preprint: inspected method and limits of transfer

9 October 2026. Ongoing funded research; no original e+pi endpoint,
all-prime gcd upper bound, or irrationality proof is established here.

## Source, prior overlap, and reading scope

Primary source: Zhi-Wei Sun, *Catalan's constant is irrational*,
arXiv:2609.04176v1, 3 September 2026:

https://arxiv.org/html/2609.04176v1

The complete locally extracted main text and bibliography, all 1625
lines, have been read. Its assertions are untrusted mathematical claims.
The numerical cell verification and its claimed global proof have NOT
been independently established. References listed in the bibliography
have not thereby been inspected or verified.

The locally retained primary HTML has SHA256
f068c0a4f25677c82c4072422fef093b04625347853cc8910db2c2573cbd0c1f;
the extracted text has SHA256
a7fa988d60177df9296c8ffca0c1d38693f006e7ec4591a179d12f80ff2a7c41.
Both are recorded in literature/sun_catalan_2609_04176_scope/SOURCE_MANIFEST.json.
Acquisition used verified TLS, a fixed public URL and no redirects or
credentials. Scripts were removed from extraction and never executed.

The existing OpenAI mathematics literature gate and Family005 material
already cite this preprint. Scoped archive searches recovered that
reference but did not recover an earlier complete audit of this exact
primary text. This is a scoped overlap finding, not a universal novelty
claim. Newton completion, Cauchy--Binet valuations, and keeping one scalar
for both arithmetic and real estimates are established techniques to reuse.

## The useful positive-part bridge, with its direction retained

The paper uses the alternating tails

    T_m + T_(m+1) = 1/(2m+1)^2,
    u_m = T_m/(2m+1),
    Pi_i = product_(h=1)^B (2(i+h)+1)^2.

Its residual matrix has entries

    R[a,j] = sum_(i=0)^(a+2B) (-1)^i binom(a+2B,i) Pi_i u_(i+j),

with S columns and S+3 rows. A full-rank claim selects S rows A. Newton
completion with exactly three auxiliary columns then gives a SINGLE
rational scalar qhat = signed F_B det(R[A,J])/product(Pi_i). Under the
hypothesis that Catalan's constant is a/q, put Hmin equal to the actual
denominator of q^S qhat. For every prime p, the identity is

    v_p(Hmin) = [A_p - R_p]_+,
    A_p = v_p(product(Pi_i)) - v_p(F_B),
    R_p = v_p(q^S det(R[A,J])).

The Cauchy--Binet expansion, when its precise source decomposition is
valid, supplies LOWER bounds R_p >= sum_nu m_(p^nu). An additional local
saturation inequality a_Q >= m_Q permits removing the positive part:

    [A_p-R_p]_+ <= A_p - sum_nu m_(p^nu).

Summing these inequalities gives an UPPER bound on the denominator of
the SAME scalar. The real estimate must then bound that scalar, including
every source, factorial, odd-linear and Vandermonde factor.

This is a lower-valuation-to-upper-denominator bridge. It is not an
upper bound on the valuation of a determinant, nor an upper bound on an
actual two-coordinate gcd. In particular it does not bound the OPEN nu
in A2turn11's exact identity v2(G)=chi+nu. Likewise it gives no upper bound
on A5's actual joint mass r_circle*sqrt(c). An unevaluated Cauchy--Binet
minimum cannot silently supply either of those opposite inequalities.

## Concrete text issues to resolve before importing a theorem

Section2 displays a recurrence expansion based at T_i and sums over
k=0,...,j-1. Its k=0 forcing denominator is (2i+1)^2. Pi_i starts at h=1,
so that denominator is not canceled. The following claim that the entire
correction is a polynomial is therefore false AS DISPLAYED. For j=1 the
correction contains Pi_i/((2i+3)(2i+1)^2), which retains a pole at i=-1/2.

The subsequent residual formula switches to T_(i+1) but retains the
coefficient (-1)^j. Expanding correctly from T_(i+1), for j>=1, gives

    T_(i+j) = (-1)^(j-1) T_(i+1)
              + sum_(k=1)^(j-1) (-1)^(j-1-k)/(2(i+k)+1)^2.

With this base index, all displayed correction denominators divide Pi_i,
and the degree bound can be reconsidered. This is a plausible repair;
it must be propagated through the rank proof and scalar identities.
The sign discrepancy alone can become a column sign, but the uncanceled
pole in the literal original formula cannot be dismissed as such.

The displayed Newton interpolant omits (-1)^n: if
a_n=sum_i (-1)^i binom(n,i) f_i, the interpolant is
sum_n (-1)^n a_n binom(x,n). Vanishing of high a_n remains useful after
repair. The displayed set containing the two endpoints of the Newton
range also needs to mean the complete integer range used in the proof.

Theorem5.1's proof invokes S<=B/20 and B>=20. Those restrictions must be
attached to any imported saturation statement; B>S alone does not record
the proof's actual scope. A reference-column parameter D in the Newton
completion also needs the explicit intended identification D=2B.

These issues do not by themselves prove that every proposed repair or
the paper's intended result fails. They do mean the displayed statements
are not adopted as verified theorems here.

The small-prime discussion reports 238 raw /178 merged cells and a
high-precision constant. The middle-prime discussion similarly reports
a finite affine-cell integral. Complete cell tables and a separately
checkable evaluation are not established by merely reading those claims.
Section9 states that its uniform raw real coefficient is 39/200 after
Stirling and cancellation. A fully paid expansion uniform in the selected
Cauchy--Binet index set is still required before using its sign margin.
No numerical certificate from this paper has been executed.

## Actual e+pi transfer requirements

Any application to our original objects has to supply all of the
following for the same actual infinite indices:

1. A source decomposition whose complete forcing correction becomes a
   polynomial after the chosen integer weight, including the exponential
   source and the original odd-pole source. Sun's alternating squared-
   denominator tail recurrence does not verify this mixed-source claim.
2. A full-rank or strictly nonzero argument for the resulting actual
   scalar. Rank for a different tail matrix does not certify our scalar.
3. Exact finite Newton completion, all omitted-row factors, actual
   contents, and every integer or odd-denominator division. A fixed
   integer row normalization must be traced back to the original scalar.
4. A simultaneous all-prime positive-part inequality, including p=2,
   powers beyond the visible index range and any parameter-dependent
   common divisors. Integrality at2 for Catalan's odd denominators is not
   integrality of our factorial-exponential source after division.
5. A real estimate of this SAME scalar and its least simultaneous
   denominator giving a negative final exponent, with a nonzero whole
   error. An upper bound for unscaled rational approximation error is
   insufficient.

None of these mixed-source obligations is settled by this filter.
The current compact producer's dyadic residual and its other odd-prime
upper controls remain OPEN. The signed producer's common collision mass
remains OPEN. The original local producer's complete higher-precision
endpoint remains OPEN. A new weighted mixed-source construction would
be a distinct research assignment only after its original decomposition
and previously studied overlap have been checked; no generic renaming
of the present gcd obstruction is counted as progress.
