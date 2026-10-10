> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Historical research record recovery — 2026-10-02

This is a provenance and handoff audit, not a new mathematical verification. The actual e+pi problem remains OPEN.

Inspected the original session's 1761 messages and all 498 nonempty assistant replies, plus existing saved stage documents and visible write receipts. Preserved every original assistant reply in attributed, checked files; the private transcript, working contexts and child reports were not replaced.

48 replies explicitly mentioned unsaved material. Among them, 39 have related later stage documents, five are promises or references to another record, and four require distinct recovery here. Existence of a related document does not certify every sentence of an earlier draft: corrections and stated scopes remain controlling. The obsolete >3/4 content target is withdrawn and must not be revived.

## A concrete earlier omission

At 2026-10-01 13:31:20 the main agent gave a Laguerre row-and-derivative sign derivation, explicitly unsaved/unreviewed. No standalone version was found among the session's research papers; the verification register still describes a proposed row-sign reduction awaiting a derivation. Before recovery, none of the five complete working contexts contained its Laguerre/31/8/4−√15 markers. The original transcript did contain the full text. This establishes a missing shared artifact and working-memory omission; it does not establish that every agent internally forgot it, nor does it verify the claim. Individual row signs do not determine alternating determinant signs.

The three latest main-agent denominator deductions (03:51:51, 03:53:49, 03:55:33) also had no subsequent main write receipt. They are recovered verbatim as author drafts, retaining hypotheses and unresolved global estimates.

## Recovery catalog

HISTORY_RECOVERY_CATALOG_20261002.json records every source message ID, time, author, byte-independent source hash and note paths. HISTORY_UNSAVED_AUDIT_20261002.json maps the 48 explicit candidates to later documents or pending records. Each agent also has bounded INDEX_00001.json and subsequent pages under .astra-notes/<session-id>/<agent-id>/.

The automatic record store uses the existing confined write/read tools, follows no links, and does not execute saved text or access the network. Its index is published only after all note parts match read-back. If saving fails, the private original remains and a completion report is withheld. The trusted prompt keeps every agent's index location outside compressed working memory. Archive retrieval is selective; do not paste the entire historical catalog into every model request.

## Coordination findings

The 03:11 screenshot was an inefficient stage barrier: Child 1 finished at 02:58:48, Child 2 at 02:51:51, Child 4 at 02:51:38, while Child 3 finished at 03:19:51. Follow-up assignments were not accepted until 03:23–03:24. The program previously treated any actionless main reply as waiting if another child remained active. That rule was repaired. A separate three-actionless-turn watchdog then falsely stopped fresh mathematical deductions; that guard now distinguishes new substantive text from empty or repeated replies.

Main must receive reports as they arrive, reassign completed children to distinct useful research, and continue its own original work. Waiting requires an explicit dependency. At most Child 4 may review necessary new decisive claims, alongside original research. No replay of accepted old audits or the old 44 checks is requested.

## Evidence rows

| Candidate | Author and time | Record disposition | Related file |
|---|---|---|---|
| 1 | primary agent 2026-10-01T06:45:14+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/B2_COMMON_FACTOR_TERNARY_DRAFT.md |
| 2 | primary agent 2026-10-01T07:32:53+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/GROWING_CONTENT_CRITERION_DRAFT.md |
| 3 | subagent3 2026-10-01T07:47:12+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/agent3/GROWING_ENDPOINT_NONVANISHING.md |
| 4 | primary agent 2026-10-01T07:59:44+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/GROWING_BOUND_OBSTRUCTION_DRAFT.md |
| 5 | subagent3 2026-10-01T08:05:22+0800 | Intent/reference only | .astra-notes/[session identifier removed]/[session identifier removed]/notes/a9/[session identifier removed].001.json |
| 6 | primary agent 2026-10-01T09:00:53+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/GROWING_HIGH_ROW_SLACK_DRAFT.md |
| 7 | primary agent 2026-10-01T09:03:57+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/GROWING_HIGH_ROW_SLACK_DRAFT.md |
| 8 | subagent1 2026-10-01T10:30:18+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/agent1/REVISED_REMAINDER_INDEPENDENT_REVIEW.md |
| 9 | primary agent 2026-10-01T13:31:20+0800 | Recovered pending author draft | .astra-notes/[session identifier removed]/[session identifier removed]/notes/1a/[session identifier removed].001.json |
| 10 | primary agent 2026-10-01T14:33:01+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/EXPONENTIAL_COMPANION_HEIGHT_TRADEOFF.md |
| 11 | subagent4 2026-10-01T14:40:23+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/agent4/RATIONAL_CENTER_ARITHMETIC.md |
| 12 | primary agent 2026-10-01T15:31:16+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/LOG_TWO_FORCING_ENVELOPE_DRAFT.md |
| 13 | primary agent 2026-10-01T15:34:18+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/LOG_TWO_FORCING_ENVELOPE_DRAFT.md |
| 14 | primary agent 2026-10-01T15:36:08+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/LOG_TWO_FORCING_ENVELOPE_DRAFT.md |
| 15 | primary agent 2026-10-01T15:50:13+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/LOG_TWO_FORCING_ENVELOPE_DRAFT.md |
| 16 | primary agent 2026-10-01T16:13:37+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/POSITIVE_FORCING_EVEN_NORMALITY_TAU_DRAFT.md |
| 17 | primary agent 2026-10-01T16:14:43+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/POSITIVE_FORCING_EVEN_NORMALITY_TAU_DRAFT.md |
| 18 | primary agent 2026-10-01T16:19:35+0800 | Intent/reference only | .astra-notes/[session identifier removed]/[session identifier removed]/notes/65/[session identifier removed].001.json |
| 19 | primary agent 2026-10-01T16:28:59+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/SCALAR_FORCING_CENTER_DRAFT.md |
| 20 | primary agent 2026-10-01T16:34:55+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/DIRECT_SELECTOR_HEIGHT_OBSTRUCTION_DRAFT.md |
| 21 | subagent2 2026-10-01T16:38:22+0800 | Intent/reference only | .astra-notes/[session identifier removed]/[session identifier removed]/notes/a8/[session identifier removed].001.json |
| 22 | primary agent 2026-10-01T16:39:38+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/DIRECT_SELECTOR_HEIGHT_OBSTRUCTION_DRAFT.md |
| 23 | primary agent 2026-10-01T16:46:04+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/DIRECT_SELECTOR_HEIGHT_OBSTRUCTION_DRAFT.md |
| 24 | primary agent 2026-10-01T16:47:25+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/DIRECT_SELECTOR_HEIGHT_OBSTRUCTION_DRAFT.md |
| 25 | primary agent 2026-10-01T16:55:56+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/COMBINED_COMPANION_DENOMINATOR_DRAFT.md |
| 26 | subagent2 2026-10-01T17:01:42+0800 | Intent/reference only | .astra-notes/[session identifier removed]/[session identifier removed]/notes/c1/[session identifier removed].001.json |
| 27 | primary agent 2026-10-01T17:03:37+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/LARGE_SELECTOR_DYADIC_DENOMINATOR_DRAFT.md |
| 28 | primary agent 2026-10-01T17:06:35+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/LARGE_SELECTOR_DYADIC_DENOMINATOR_DRAFT.md |
| 29 | primary agent 2026-10-01T17:08:44+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/LARGE_SELECTOR_DYADIC_DENOMINATOR_DRAFT.md |
| 30 | primary agent 2026-10-01T17:18:51+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/LARGE_SELECTOR_SELECTION_DRAFT.md |
| 31 | primary agent 2026-10-01T17:20:01+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/LARGE_SELECTOR_SELECTION_DRAFT.md |
| 32 | primary agent 2026-10-01T17:21:27+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/LARGE_SELECTOR_SELECTION_DRAFT.md |
| 33 | primary agent 2026-10-02T02:01:05+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/LARGE_SELECTOR_SELECTION_DRAFT.md |
| 34 | primary agent 2026-10-02T02:38:57+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/DYADIC_CORRECTION_COMPANION_TRANSFER_DRAFT.md |
| 35 | primary agent 2026-10-02T02:45:10+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/PI_COMPANION_NECESSARY_BUDGET_DRAFT.md |
| 36 | primary agent 2026-10-02T02:46:31+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/PI_COMPANION_NECESSARY_BUDGET_DRAFT.md |
| 37 | primary agent 2026-10-02T02:51:06+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/LATEST_COMPANION_AND_SADDLE_EXTENSIONS_DRAFT.md |
| 38 | primary agent 2026-10-02T02:53:03+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/LATEST_COMPANION_AND_SADDLE_EXTENSIONS_DRAFT.md |
| 39 | primary agent 2026-10-02T02:54:33+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/LATEST_COMPANION_AND_SADDLE_EXTENSIONS_DRAFT.md |
| 40 | primary agent 2026-10-02T03:00:08+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/LATEST_COMPANION_AND_SADDLE_EXTENSIONS_DRAFT.md |
| 41 | primary agent 2026-10-02T03:03:10+0800 | Intent/reference only | .astra-notes/[session identifier removed]/[session identifier removed]/notes/23/[session identifier removed].001.json |
| 42 | primary agent 2026-10-02T03:04:55+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/LARGE_SELECTOR_PHASE_SPARSITY_DRAFT.md |
| 43 | primary agent 2026-10-02T03:25:54+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/JOINT_COMPANION_OVERLAP_BUDGET_DRAFT.md |
| 44 | primary agent 2026-10-02T03:29:09+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/JOINT_COMPANION_OVERLAP_BUDGET_DRAFT.md |
| 45 | subagent3 2026-10-02T03:30:38+0800 | Related later paper exists; preserve its scope/corrections | work/session_20261001_astra/agent3/CANONICAL_OVERLAP_DEFICIT.md |
| 46 | primary agent 2026-10-02T03:51:51+0800 | Recovered pending author draft | .astra-notes/[session identifier removed]/[session identifier removed]/notes/1b/[session identifier removed].001.json |
| 47 | primary agent 2026-10-02T03:53:49+0800 | Recovered pending author draft | .astra-notes/[session identifier removed]/[session identifier removed]/notes/66/[session identifier removed].001.json |
| 48 | primary agent 2026-10-02T03:55:33+0800 | Recovered pending author draft | .astra-notes/[session identifier removed]/[session identifier removed]/notes/6a/[session identifier removed].001.json |
