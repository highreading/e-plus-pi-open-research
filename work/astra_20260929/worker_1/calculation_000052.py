from pathlib import Path
import hashlib
root = Path('[private local path removed]')
p = root / 'work/astra_review_registry/candidates/worker3-simple-root-precision-transfer-v1.md'
data = p.read_bytes()
marker = b'STATUS: Unverified claim submitted for independent review.'
start = data.index(marker)
payload = data[start:]
expected = 'a11ba5a6caead9b36c8e46c5d17973533b12a5823bdab59e93b338fe10f8f3a4'
digest = hashlib.sha256(payload).hexdigest()
print({'file_sha256': hashlib.sha256(data).hexdigest(), 'payload_start': start, 'payload_length': len(payload), 'payload_sha256': digest, 'matches': digest == expected})
assert digest == expected

def val2(n):
    if n == 0:
        return float('inf')
    return (abs(n) & -abs(n)).bit_length() - 1

def lift_root(fun, bits):
    x = 0
    for k in range(bits):
        choices = [z for z in (x, x + (1 << k)) if fun(z) % (1 << (k+1)) == 0]
        assert len(choices) == 1
        x = choices[0]
    return x

checks = 0
for M in range(1, 17):
    bits = M + 5
    for c in (0, 1, 3, 6):
        F = lambda y, c=c: y + 2*c*y*y
        G = lambda y, c=c, M=M: y + 2*c*y*y + (1 << M)
        alpha = lift_root(F, bits)
        beta = lift_root(G, bits)
        assert val2(alpha-beta) == M
        for h in (0, 1, 3, 5):
            assert val2((1 << h)*(alpha-beta)) == M+h
            checks += 1
for x in range(-32, 33):
    for y in range(-32, 33):
        assert val2((x+2*x*x)-(y+2*y*y)) == val2(x-y)
        checks += 1
print({'finite_root_and_isometry_checks': checks, 'passed': True, 'scope': 'finite corroboration only'})