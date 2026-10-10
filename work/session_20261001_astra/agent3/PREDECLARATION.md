> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Bounded prime-certificate extension: predeclaration

This manifest is written before any new seed computation in this task.

The candidate list is every prime 23 <= p <= 199, processed increasingly:

23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199.

There are 38 candidates. The existing uniform primes are 5 and 13, cited only within the scope of work/session_20260927/hp_b1_uniform_5_13_independent_review.md.

For each tested candidate, compute every scalar residue row r=0,...,p-1 and retain its complete Ccal zero set. A successful candidate must have zero set exactly {1}. Before counting its contribution, compare every H, K, Acal, Bcal, Ccal residue entry using two distinct exact constructions: modular Rodrigues contractions and ordinary integer Legendre coefficients followed by exact rational factorial functionals.

Accumulate the certified successful candidates with 5 and 13. After each success, compare W = sum_p 2 log(p)/(p-1) with tau = 2 log(1+sqrt(2)) using rigorous rational logarithm bounds or an exact integer/algebraic comparison. Refine arithmetic precision if necessary; floating-point logarithms are not certificates.

Stop immediately once W > tau is rigorously certified. Otherwise stop after testing 199. Do not extend the bound, rerun the old full atlas, construct canonical HP nullspaces, or scan actual degrees.

All new files belong exclusively under work/session_20261001_astra/agent3/. Historical and shared files are read-only inputs. No networking or installations.

The final proof must explicitly retain eventual Delta nonvanishing, the all-depth residue-one compensation, strict separation of the actual numerator terms, and reduction to the actual positive denominator q. A successful whole-b=1 exclusion does not establish irrationality of e+pi. A failed bounded search implies no infinite prime-density statement.
