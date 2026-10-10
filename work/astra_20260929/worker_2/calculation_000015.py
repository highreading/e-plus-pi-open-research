import sys
sys.dont_write_bytecode = True
sys.path.insert(0, '[private local path removed]')
import hashlib
import json
import re
from pathlib import Path
import sympy as sp

project_path = Path('[private local path removed]')
candidate_specs = [
    ('b2-large-prime-content-normalization', 'a1e60ab2287008a0f177cf453b624f305f78327b23f4306abe5f555c5cd438dc'),
    ('worker3-ordinary-pade-prefactor-v1', 'e2b926b3f2d184f5cd501ef88d3031968ab3a8fb0bbce0fd456292ef52991aa3'),
]
fingerprints = []
for claim_id, expected in candidate_specs:
    candidate_path = project_path / 'work/astra_review_registry/candidates' / (claim_id + '.md')
    data = candidate_path.read_bytes()
    match = re.search(rb'^Content SHA256: ([0-9a-f]{64})$', data, re.MULTILINE)
    parts = data.split(b'\n\n', 2)
    payload = parts[2] if len(parts) == 3 else b''
    variants = {
        'payload_exact': payload,
        'payload_without_one_terminal_newline': payload[:-1] if payload.endswith(b'\n') else payload,
        'payload_stripped': payload.strip(),
    }
    payload_hashes = {name: hashlib.sha256(value).hexdigest() for name, value in variants.items()}
    fingerprints.append({
        'claim_id': claim_id,
        'bytes': len(data),
        'file_sha256': hashlib.sha256(data).hexdigest(),
        'registry_content_sha256': expected,
        'header_content_sha256': match.group(1).decode() if match else None,
        'payload_hashes': payload_hashes,
        'matching_payload_forms': [name for name, digest in payload_hashes.items() if digest == expected],
    })

A, B, wP, wU, TP, TU, G = sp.symbols('A B wP wU TP TU G')
a0, a1, a2, r1, r2 = sp.symbols('a0 a1 a2 r1 r2')
a_vec = sp.Matrix([a0, a1, a2])
e_vec = sp.ones(3, 1)
TU_vec = sp.Matrix([TU, TU-a1, TU-a1-a2])
TP_vec = sp.Matrix([TP, TP-r1, TP-r1-r2])
t_vec = (A*TU_vec-B*TP_vec)/G
x_vec = (wP*TU_vec-wU*TP_vec)/G
beta_vec = a_vec.cross(e_vec+t_vec)
Y_raw = beta_vec.dot(e_vec)
X_raw = beta_vec.dot(x_vec)
S_cal = a1**2-a0*a2
C_cal = (a1-a0)*r2-(a2-a1)*r1
W_cal = a1*r2-a2*r1
Y_formula = (B*C_cal-A*S_cal)/G
X_formula = ((wP+TP)*S_cal-(wU+TU)*C_cal-a0*W_cal)/G
residuals = {
    'raw_endpoint_Y': sp.factor(Y_raw-Y_formula),
    'raw_endpoint_X_using_Wronskian': sp.factor((X_raw-X_formula).subs(G, A*wU-B*wP)),
}

f, k, eta, S, C, W = sp.symbols('f k eta S C W')
g = 2*f/k
gamma = g*f/(G*k)
D_integer = k*B*C-2*A*S
X_scaled = 2*(wP+TP)*S-k*(wU+TU)*C-2*f*eta*W
Y_substituted = (B*g*f*C-A*g**2* S)/G
X_substituted = ((wP+TP)*g**2*S-(wU+TU)*g*f*C-(g*eta)*(g*f*W))/G
residuals['Y_common_scale'] = sp.factor(Y_substituted-gamma*D_integer)
residuals['X_common_scale'] = sp.factor(X_substituted-gamma*X_scaled)

n = sp.symbols('n', integer=True, nonnegative=True)
f_n = 2**n/sp.factorial(n)**2
g_n = 2**(n+1)/sp.factorial(n+1)**2
G_n = (-1)**n*2**(2*n+3)/(n+1)
gamma_direct = g_n*f_n/(G_n*(n+1)**2)
gamma_closed = (-1)**n/(4*(n+1)**3*sp.factorial(n)**4)
residuals['closed_factorial_scale'] = sp.simplify(sp.combsimp(gamma_direct/gamma_closed)-1)

print(json.dumps({
    'candidate_fingerprints': fingerprints,
    'symbolic_residuals': {name: str(value) for name, value in residuals.items()},
    'all_symbolic_residuals_zero': all(value == 0 for value in residuals.values()),
    'scope': 'Read-only fingerprint checks and exact algebra; no registry verdict, numerical denominator bound, or irrationality conclusion.'
}, indent=2))