"""Third CLOSED predeclared list; imports the unchanged exact seed engine.

The imported module is guarded and does not rerun its own prime list.
"""
import hashlib
import json
from pathlib import Path

from check_second_predeclared_uniform_seed_list import classify

BASE = Path(__file__).resolve().parent
PRIMES = (
    101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
    157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
)
results = classify(PRIMES)
payload = {
    "predeclared_primes": list(PRIMES),
    "scope": "Third closed finite list. Full residue certificates for uniform-good primes; first exact witness only for other primes.",
    "theorem_dependencies": [
        "raw_positive_residue_transfer_independent_review.md",
        "raw_negative_residue_transfer_independent_review.md",
    ],
    "all_internal_exact_cross_checks_passed": True,
    "results": results,
}
target = BASE / "raw_third_predeclared_uniform_seed_certificate.json"
target.write_text(json.dumps(payload, indent=2) + "\n")
summary = []
for row in results:
    witness = row["first_bad_witness"]
    summary.append({
        "p": row["p"], "all_residues_good": row["all_residues_good"],
        "tested": row["number_of_residues_tested_before_stopping"],
        "first_bad": {
            key: witness[key] for key in ("residue", "branch", "k", "status", "D", "E")
        } if witness else None,
    })
print(json.dumps(summary, indent=2))
print("certificate_sha256", hashlib.sha256(target.read_bytes()).hexdigest())
