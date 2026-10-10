# Reproducing and inspecting evidence

This release preserves existing mathematical programs and finite receipts. Publication preparation did not rerun those computations. The release validator checks file integrity, publication privacy, local Markdown targets, JSON validity and Python syntax; it does not certify mathematical conclusions.

Most computations use exact integers/rationals, with some relying on SymPy, mpmath, NumPy or specialized arithmetic libraries. Dependency requirements vary by program. Third-party environments, wheels and application builds are not bundled. Inspect the selected source and its imports and parameters before preparing a separate environment. A successful syntax check does not establish that all runtime dependencies are installed.

Legacy scripts may expect execution from the repository root, nearby modules or a particular output layout. Local personal paths were mapped to public relative paths where possible. Files retaining a private-path placeholder require a small portability adaptation before use; document that adaptation and review it. Do not assume every historical program is a turnkey command.

For an exact certificate, read its schema, scope, input and normalization with the proof it supports. The public JSON retains mathematical payloads while operational account/session metadata is omitted. Historical SHA references in proof notes describe their original versions; the release manifest hashes the sanitized files shipped here. The [public version map](../reviews/PUBLIC_VERSION_MAP.json) links historical source digests to the corresponding public files, without exposing private source paths. If a legacy script checks frozen historical bytes, review this map and the transcription checks before adapting its expected hashes; do not disable an integrity guard blindly.

To inspect release structure without running archived research:

```sh
python3 tools/validate_release.py
```

The validator is standalone and uses the Python standard library. Run it from the repository root. It does not install dependencies, call a model, fetch websites or execute archived mathematical programs.

A new computational contribution must specify its exact finite scope, resource limits, implementation and output. For large exact results, prefer an independently implemented arithmetic control where appropriate. Do not broaden a run simply because a sample passed, and do not infer an infinite statement from a table.
