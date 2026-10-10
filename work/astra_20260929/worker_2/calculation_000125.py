from pathlib import Path
import hashlib
p = Path('work/astra_review_registry/candidates/main-b2-five-adic-residue-four-cancellation-v1.md')
b = p.read_bytes()
expected = 'b123168c159b9a62d863ee40ffdae485533f2229e99c368b6cd671e04f321519'
starts = [0] + [i+1 for i,c in enumerate(b) if c == 10]
matches = [i for i in starts if hashlib.sha256(b[i:]).hexdigest() == expected]
assert len(matches) == 1, ('payload hash mismatch', matches)
assert hashlib.sha256(b).hexdigest() == 'b03b141d729f45e7f56a419902a2cb68f6e8bf891aa3bf2d4e4bbb2d096ff29e'
print({'payload_start': matches[0], 'end': len(b), 'payload_sha256': expected, 'ledger_file_hash_matches': True})