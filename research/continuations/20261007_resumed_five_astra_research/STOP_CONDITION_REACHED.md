> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Financial stopping condition reached

The mathematical objective is unresolved. This round stopped because every
available credential was verified strictly below the user's USD3 floor.
The private directory inventory contains exactly two credential files; its
unrelated .DS_Store file is not a credential. No key content is copied here.

The first verified all-below-floor observation was2026-10-07T22:59:07.673958+08:00.
At the final verification, after every admitted request returned:

[Private account record omitted.]
|---|---:|---|
| Account2 | 2.83693999999997 | Below3; stopped |
| Account3 | 2.055724 | Below3; stopped |

No model attempt was admitted after the first verified collective floor.
Pending calls had been admitted at their recorded fresh balances>=3.
A3turn15 failed without a completed terminal response; its retry was skipped
by the fresh floor guard. This is not zero-balance exhaustion or a proof result.
All admitted sessions have ended. There are88 completed public reports across
the five real external streams: {'A1': 19, 'A5': 15, 'A2': 18, 'A4': 21, 'A3': 15}.

The final billing time is2026-10-07T23:04:56.404441+08:00. Exact receipts are preserved in
billing/final_balance_20261007.json and STOP_CONDITION_REACHED.json.
