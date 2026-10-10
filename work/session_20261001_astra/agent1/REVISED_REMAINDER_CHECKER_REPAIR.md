> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact-rational comparison repair

Original: `20/8 == rat(5,2)`.

Corrected: `rat(20,8) == rat(5,2)`.

The current inspected file already contained the correction; this verification did not edit it. The preceding edit guard failed at `Expected exactly one original comparison` before writing anything. The original mathematical assertion is preserved.

Numeric audit: no float literals or wholly numeric Python divisions remain. Other divisions were inspected and use symbolic or exact-rational operands. No assertions were removed.

Actual checker execution outcome: PASS. Full output is saved in revised_remainder_independent_stdout.txt. The pre-existing certificate was preserved as revised_remainder_checks_before_verification.json.
