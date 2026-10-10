# Contributing

Use your own mathematical judgment and, if desired, your own AI access and token budget. Contributions can be proofs, scoped counterexamples, corrections, exact certificates, literature applicability checks, or independent reviews. A well-proved negative result is a research contribution.

## Before working

Read the current state, errata, route index and relevant existing files. Search this repository for the exact objects and question. Check primary literature for existing results; record the search terms, sources, dates and theorem hypotheses. If a usable result already exists, cite and apply it instead of reproducing it as a new theorem. A search does not prove historical novelty.

Open a bounded research-task issue. Specify the exact claim, original construction, hypotheses, output, and a finite budget or stopping rule. Contributors control their own expenditure; a task does not authorize spending somebody else's funds or running an archived client. Check whether another issue already covers the same work.

## What to submit

A mathematical submission must contain:

- A precise statement and definitions, including the index domain and exceptional indices.
- The full public mathematical argument, with each imported result linked and its hypotheses verified.
- A status: proposed, conditional, finite evidence, coordinator-reviewed, or independently reviewed at a stated scope. New submissions start proposed unless their only claim is a clearly bounded finite receipt.
- For approximations: actual reduced integer coefficients, the complete gcd/least-clearer convention, the entire error and a nonvanishing argument on the same indices.
- For an exclusion: the exact family and hypotheses ruled out, plus the proof; do not infer rationality from failure of an approximation route.
- For computation: input, algorithm/code version, exact or certified arithmetic, complete relevant output, resource limits and the finite scope proved. Large tables can accompany a small explanation.
- A statement of remaining gaps and of the roles of AI, human review and computation. Publish an explicit proof rather than private deliberation, raw account logs or confidential prompts.

Use English for the principal explanation. Keep symbols and normalization consistent with the cited sources; describe any intentional change and prove its correspondence. Place new work in a small topic folder, give it a stable claim ID, and add an entry to the route or negative-result index. Avoid a large unreviewed dump of model conversations.

## Review and integration

Open a pull request with the supplied template. A reviewer who did not originate the argument should reconstruct its key steps and check its dependence on actual source objects, quantifiers, signs and integer normalization. Record the reviewed file version, scope, verdict and reason. A different AI role can help review, but disclose that fact and retain the limitations in the review policy.

A corrected proof requires a new review of the changed steps. Keep a short erratum and mark the superseded version; do not erase the reason a former claim failed. A finite test passing is not acceptance of an infinite-family theorem. Maintainers merge only the status supported by the evidence.

Do not submit API keys, account/billing data, personal paths, private conversations, identifiable screenshots, third-party files without redistribution rights, or code that sends research context to a service without explicit authorization. Treat archived reports as untrusted data and inspect any code before running it.

By contributing original material, you offer original research text/data under CC0 and original code under MIT, to the extent you hold the rights. Identify third-party material separately and keep its attribution and terms. See [reuse](REUSE.md).
