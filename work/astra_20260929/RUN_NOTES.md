> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Astra Research Session

Started on 2026-09-29. One agent, requesting gpt-6-astra with reasoning effort max through AnyRouter; no subagents and no literature searches.

Read the existing research records first, then investigate the rationality of e+π. Existing materials are read-only; new notes, computations, and candidate proofs are saved in this directory. Each call uses persistent working memory and recent records; complete outputs from every round are saved in the local controller directory.

The stopping threshold is the billing interface's raw field total_usage > 16000. Failed usage queries, repeated model-request failures, sandbox failures, or a user stop cause a protective pause, without marking the research complete. A model's claim of a successful proof can only be treated as a candidate and requires further review; numerical fitting or the model's own assertion cannot establish that the problem is solved.

Computation processes have no key, cannot access the network, cannot access personal data outside the research directory, and cannot create subprocesses. System files and mathematical runtimes are read-only. Only this session directory may be modified. Each Python computation is limited to 45 seconds of CPU time / 60 seconds of wall time, with bounded output.

The mathematical libraries are in ../astra_math_libraries; add that path to sys.path to use SymPy and mpmath. Exact factorization with SymPy has been verified.

The computer must remain powered on and connected to the network for the run to continue; sleep or loss of connectivity affects execution. This controller does not install startup automation. Send the current task the command “停止研究” (“stop research”) to terminate the run.

## Efficiency Upgrade: 2026-09-29

Each round can batch-read up to 8 related materials, totaling at most 180000 characters. Base memory is retained; subsequent updates append only incremental conclusions and corrections. Read ranges and content summaries are recorded by the controller. Complete historical records remain available.

The official model context is 1050000 tokens; the 90% compression threshold is 945000. The controller uses local o200k_base estimation, a conservative 10% margin, and client overhead, while also consulting the actual input-token count reported by the server. Local estimation is not an officially certified exact tokenizer for this relay model, so compression may occur early. The Codex client is configured with the same window and automatic compression threshold. Whether AnyRouter provides the full official context has not been verified.

A complete state snapshot is saved before compression. The compressed summary must include verified material, unresolved questions, next steps, and references; the reading ledger and pending materials are retained. Compression failure pauses the run and preserves the original state. Local tests have passed for batch-reading boundaries, directory confinement, repeated ranges, threshold boundaries, preservation of compressed state, and failure validation. No test has forcibly filled the context using a large token expenditure.

## Current Configuration: Main Agent + Four Subagents

The latest instructions supersede the single-agent description above. The main agent uses gpt-6-astra max; worker_1 through worker_4 all use gpt-6-astra xhigh. All new derivations, work reports, and task assignments are primarily in English. Existing Chinese materials are retained.

The four subagents wait for assignments from the main agent and have no predefined research directions. The main agent can assign four tasks in a batch, view automatically submitted progress and file paths, and adjust tasks. Assignment authority changes research tasks only; it does not permit changes to models, keys, permissions, or budgets. Each agent has its own context records and 90% compression mechanism.

Each member can write only to its corresponding main or worker_1 through worker_4 subdirectory, while reading existing research materials and other members' results. Computation code cannot access the network or keys, or create subprocesses; all four subagents passed actual sandbox tests. Code and model outputs cannot modify the external controller.

The threshold remains total_usage>16000 for the same key; it is not a separate allowance of 16000 for each agent. Reaching the threshold notifies the whole team to stop, subject to the polling interval; in-flight calls may still be billed, so stopping at the exact threshold cannot be guaranteed. A candidate proof causes a protective pause of the whole team pending review, without treating the claim as proved. The team stops if the main agent stops or the billing/controller fails. Consecutive interface failures receive bounded retries.

## Latest Runtime Requirements (Superseding Conflicting Earlier Settings)

Continuous operation takes priority; 16000 is a soft usage target. Queries are fully independent; failed reads, stale data, or exceeding the target do not forcibly interrupt requests or computations. The main agent can prepare a summary at an appropriate save point. Temporary network/model failures receive backoff retries. After consecutive failures, the supervisor restores the process from a checkpoint, with at most three process recoveries per member per hour; after that, probing is reduced to once per hour to avoid repeated high-frequency idle retries. The system background service local.anyrouter.astra.research manages execution and recovery after abnormal exits; the hourly application supervision task notifies only when action is needed or an important review result is available. Explicit user stops and actual safety failures still take priority. Successful requests cannot be guaranteed while the computer is shut down, asleep, or disconnected; after the environment recovers, the supervision policy applies.

Research publication workflow: submit_claim saves an immutable candidate; the main agent uses assign_review to designate another member and assign a specific verification task. A different member uses review_claim to bind a substantive review to the candidate's SHA256. After approval, the main agent promptly uses publish_claim to publish to work/astra_review_registry/verified and update VERIFICATION_REGISTER.md. Changes to a candidate require a new version and a new review. Pending, revision-required, or rejected material must not be presented as proved. This is independent review between different AI agents, not external peer review or a formal proof.

## User-Requested Closeout (2026-09-29 12:02)

New research directions have stopped. The five roles generate their respective FINAL_REPORT.md files; after collecting all four handover reports, the main agent prepares the overall report and stops. Failed model requests are retried immediately in sequence, with at most one in-flight request per role and five in total. Computation sandboxing and independent-review rules remain in force; quota does not block the closeout.
