> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Approximant modules: primary literature and exact scope of the new arithmetic application

Date: 2026-09-13. Root literature follow-up to the self-contained
shared-core saturation proof. This records established algebraic
machinery separately from the application proved in this project.

Rosenkilde and Storjohann, *Algorithms for Simultaneous Pade
Approximations*, ISSAC 2016, Section 2.2 (printed page 407), state
the row-reduced predictable-degree identity over a field. Section
2.4 defines order-d approximant bases and their shifted versions;
Section 2.5 explains extracting degree-constrained solutions.
These provide the direct standard framework for the module used
here. [Author-hosted paper](https://cs.uwaterloo.ca/~astorjoh/issac16.pdf).

Storjohann's 2006 note treats reduction of classical Hermite-Pade
problems with arbitrary degree bounds to minimal approximant basis
computation. It supplies an algorithmic reference, without a
special arithmetic assertion for the present exponential/arctangent
pair. [Primary proceedings article](https://drops.dagstuhl.de/entities/document/10.4230/DagSemProc.06271.12).

Kuijper and Schindelar, *Minimal Groebner bases and the predictable
leading monomial property*, revised 2010, explain why ordinary
field properties need care over Z/p^r Z. Their Theorem 4.12 gives
a predictable leading monomial property for the constructed
p-basis. It is a possible exact parametrization tool for lifting
our remaining defect, but supplies no bound on how many p-adic
levels that defect persists. [Primary preprint, Theorem 4.12](https://arxiv.org/pdf/0906.4602).

## Our exact specialization and its limit

The field module here is the kernel of the single map

    (A,B,C) -> A+B E_T+C F_T mod z^(3n+1).

Its explicit polynomial basis has determinant z^(3n+1). The
project's independent Wronskian theorem bounds its degree<=n-1
slice by one dimension. Together these facts force the three
degree profiles and the degree<=n+1 dimension five, hence large-
prime saturation of the actual shared augmented core. The full
derivation is in `raw_shared_core_large_prime_saturation.md`.
The self-contained proof does not claim that row reduction itself
is new. The additional input is the actual minimal-degree bound
and the resulting application to these particular integer minors.

These degrees are invariants of a polynomial approximant MODULE.
They should not be confused with a minimum-degree basis of the
entire rational vector space it spans: over K(z) that space is
all of K(z)^3. Forney's classical rational-space minimal-basis
paper is background terminology, not a substitute for the module
determinant and degree constraints used here.
[Primary bibliographic record](https://epubs.siam.org/doi/10.1137/0313029).

The new saturation conclusion is proved by a unit minor modulo
p, so it excludes every power of that p in the shared-core content
without a ring-valued predictable-degree theorem. By contrast the
remaining high-content exponent is positive precisely at a possible
defective reduction and requires genuine lifting information.
Applying the field dimension formula unchanged over Z/p^r Z would
not supply that information. The separate elementary shifted-left-
annihilator argument in `raw_high_content_extremal_valuation_bound.md`
carries the actual full Smith depth into an extremal-content bound;
the size of that latter content remains unresolved.
