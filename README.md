# e + pi: an open, AI-assisted research archive

**No proof deciding whether $e+\pi$ is rational or irrational has been accepted in this project.** This repository preserves mathematical constructions, complete proof attempts, scoped internal reviews, exact finite certificates, and proved failures of specific approaches. Its research snapshot ends on **9 October 2026**; the anonymous release was prepared on **10 October 2026**.

We invite people to contribute their own mathematical work and their own AI resources. Each participant can use an AI system and a personal token budget to tackle a bounded task, build on the accumulated results, and submit a proof, counterexample, correction, or independent review. The aim is a cumulative, checkable research record. There is no guarantee that this approach will resolve the open problem.

The most useful contribution may be a proof that a tempting route fails. Such results prevent other contributors from spending their budgets on the same obstruction. We preserve full negative-result proofs and their hypotheses, alongside positive results.

The shared repository is [highreading/e-plus-pi-open-research](https://github.com/highreading/e-plus-pi-open-research). Use [Issues](https://github.com/highreading/e-plus-pi-open-research/issues) for bounded tasks and proof reviews, and [Discussions](https://github.com/highreading/e-plus-pi-open-research/discussions) for coordination. The [initial snapshot release](https://github.com/highreading/e-plus-pi-open-research/releases/tag/snapshot-2026-10-09) includes the complete downloadable archive and a SHA-256 checksum.

## Start here

| Entry | What it provides |
|---|---|
| [Start here](START_HERE.md) | A short reading sequence and first contribution |
| [Current project state](docs/PROJECT_STATE.md) | Established inputs, pending audits and the exact missing conclusion |
| [Results and routes](docs/RESULTS_AND_ROUTES.md) | Separate constructions and their scopes |
| [Proved route exclusions](no_go/README.md) | Complete proof files, dependencies and recorded reviews |
| [Open tasks](docs/OPEN_TASKS.md) | Bounded problems, context and completion criteria |
| [Contributing](CONTRIBUTING.md) | The submission and review process |
| [AI guide](AI_GUIDE.md) | A small context packet and a reusable task prompt |
| [Searchable file catalog](CATALOG.html) | Offline search across the published corpus |
| [File index](docs/FILE_INDEX.md) | Browsable category indexes for GitHub |
| [Publication coverage](docs/PUBLICATION_COVERAGE.md) | What was included, omitted and anonymized |

## What success would require

One sufficient route is to construct integers $p_j,q_j$, with $q_j>0$, on an infinite valid index set such that



$$
0<|q_j(e+\pi)-p_j|\longrightarrow0.
$$



Ordinary convergence of rational approximations does not establish this. A small approximation error must survive multiplication by the **actual denominator after complete reduction**, and nonvanishing must be proved on the selected infinite set. See the [criterion and proof](docs/IRRATIONALITY_CRITERION.md).

The current constructions have substantial arithmetic obligations. A result about one prime, one auxiliary matrix, a coefficient clearer, or a finite sample cannot be substituted for the complete original object. The [review policy](docs/REVIEW_POLICY.md) makes those distinctions explicit.

## Contribute your AI work

1. Read the current state, errata and relevant existing proof files.
2. Choose a small task from the task board or propose a clearly different question. Search the archive and primary literature before allocating a substantial budget.
3. Use your own AI access and set a finite task budget. Publish a mathematical argument and reproducible evidence; keep credentials and private account records out of submissions.
4. Open an issue or pull request using the supplied templates. Label a new claim **proposed** until an independent review checks its exact scope.
5. Help review another contribution. Record both useful conclusions and failed approaches.

Human reasoning, AI assistance, symbolic computation and exact arithmetic are all welcome. A long model response is not a proof; a short rigorous correction can be valuable. We ask contributors to disclose the role of AI and computation without publishing private deliberation or account data.

The original mathematical writing and project data use [CC0](LICENSES/CC0-1.0.txt), and original project code uses [MIT](LICENSES/MIT.txt), to the extent contributors hold the relevant rights. Third-party works retain their own terms and are generally linked rather than redistributed. See [reuse and attribution](REUSE.md). This repository does not collect API keys, pool billing credentials, or run a funded research service.
