# Review policy and status vocabulary

| Status | Meaning |
|---|---|
| Proposed | A claim or argument is submitted; it has not received a scoped independent audit |
| Finite evidence | A computation proves only the explicitly bounded assertion in its receipt |
| Conditional | The implication is justified subject to named hypotheses that remain unproved |
| Coordinator-reviewed | A recorded internal review found no gap at the stated scope; an independent audit remains pending |
| Independently reviewed, scoped | A different role completed a specified audit and its verdict/version is recorded |
| Proved exclusion, scoped | A complete recorded proof excludes the stated family/shortcut; the supporting review and dependencies are linked |
| Rejected or withdrawn | A specific claim has a known error or counterexample; preserve the correction and scope |

These statuses describe the evidence in this project. Internal reviews can be mistaken, and review by another AI role is not proof-assistant verification or external peer review. No claim becomes correct because several systems use PASS. Reviewers should reconstruct the argument, verify definitions and inspect imported lemmas.

A review must identify the exact statement and version, assumptions, dependencies, checked scope, verdict, reason and unresolved steps. Distinguish the author's claims from the reviewer's judgment. A review of Sections 1–2 does not certify Section 3; a review of an extracted body does not certify its entire JSON container.

Check quantifiers and simultaneous indices. A prime-by-prime estimate at different indices cannot supply a same-index global estimate. A pointwise necessary-and-sufficient test on a restricted class does not prove useful coverage of that class. An all-prime gcd lower bound does not furnish the needed upper bound. Adjacency/coprimality need not bound isolated high contact.

For code, verify the literal mathematical object and exact arithmetic, limits and exception handling before accepting a finite certificate. Separate an algorithm's output from the all-index proof using it. Floating-point evidence and integer-relation searches cannot certify exact equality or nonzero errors.

Old hashes refer to historical prepublication versions. Publication anonymization, path changes and translation can change bytes while preserving mathematical expressions. Use current release hashes for public files and the recorded scope for historical audits. See publication coverage for the transformation checks.
