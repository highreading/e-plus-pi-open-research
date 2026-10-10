from pathlib import Path
import hashlib
import json
import datetime

HERE = Path(__file__).resolve().parent
assert pow(9, 41, 83) == 1 and pow(9, 21, 83) == 3
assert 9 % 83 != 1 and pow(32, -1, 41) == 9
assert pow(9, 32*41, 83) == 1
assert [u for u in range(41) if pow(9, 18+32*u, 83) == 3] == [27]
endpoint = (-14448 * pow(16, -1, 83)) % 83
arc_numerator, arc_denominator = -5850, -6750
assert arc_denominator % 83 != 0
arc = arc_numerator * pow(arc_denominator % 83, -1, 83) % 83
assert arc == 13 * pow(15, -1, 83) % 83 == 23
assert endpoint == 10
relative_y = (endpoint - arc) % 83
assert relative_y == -13 % 83 != 0
note = HERE / 'COORDINATOR_CENTERED_83_ENDPOINT_UNIT.md'
source = HERE / 'signed_centered_elimination_certificate.json'
assert json.loads(source.read_text())['status'] == 'PASS'
out = {
    'status': 'PASS', 'time': datetime.datetime.now().astimezone().isoformat(),
    'scope': 'NEW scalar checks for the proved original83 residue period and centered endpoint/complete reduced arc; not a Gaussian/common-source depth bound.',
    'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in (note, source)},
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'order_of9_mod83': 41, 'exceptional_original_u_mod41': 27,
    'E_K_mod83_on_collapsed_row': endpoint,
    'reduced_R_K_mod83_on_collapsed_row': arc,
    'actual_dK_is_83_unit': True,
    'yK_over_dK_mod83_on_collapsed_row': relative_y,
    'v83_J0_equals_v83_c_on_collapsed_row': True,
    'actual_v83_U_or_c_upper_bound_proved': False, 'global_proof': False,
}
(HERE/'centered83_endpoint_unit_certificate.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'status': 'PASS', 'exceptional_u_mod41': 27,
                  'actual_yK_is_unit_on_collapsed_row': True, 'global_proof': False}))
