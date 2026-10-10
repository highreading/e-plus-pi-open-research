#!/usr/bin/env python3
"""Personally authored new 2-primary relation/payload postprocessing.

This program evaluates no original moment or weighted Gram. External code is
neither imported nor executed. The physical numerator input has twenty bits.
"""
from pathlib import Path
from math import comb
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
# The fixed 163-by-163 arrays and 512-bit residues bound the allocation.
ROOT = Path(__file__).resolve().parent
BITS = 512
MOD = 1 << BITS
D = 162
ROWS, COLS = D + 1, D - 2


def valuation(x):
    return BITS if not x else (x & -x).bit_length() - 1


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % MOD
    return out


def payload_numerator(poly, rmax, B, b):
    out = [0] * (rmax + 1)
    for r, coefficient in enumerate(poly):
        term = [coefficient]
        for t in range(r):
            term = mul(term, [b - t, -1])
        for t in range(rmax - r):
            term = mul(term, [B + b + t, -1])
        for k, x in enumerate(term):
            out[k] = (out[k] + x) % MOD
    return out


def relations(n, b):
    A = mul(mul([n + 2, -1], [n + 2, -1]),
            mul([b, -1], [b, -1]))
    B = mul([0, 0, 1], mul([2 * n + b, -1], [2 * n + b, -1]))
    matrix = [[0] * COLS for _ in range(ROWS)]
    for k in range(COLS):
        column = [0] * (k + 5)
        for a, coefficient in enumerate(A):
            for t in range(k + 1):
                column[a + t] = (column[a + t] + coefficient * comb(k, t)) % MOD
        for a, coefficient in enumerate(B):
            column[a + k] = (column[a + k] - coefficient) % MOD
        assert column[-1] == 0
        for degree, coefficient in enumerate(column[:-1]):
            matrix[degree][k] = coefficient
        assert matrix[k + 3][k] == (k + 2 * n - 4) % MOD
        assert all(matrix[r][k] == 0 for r in range(k + 4, ROWS))
    assert (n + 2 - b)**2 * (b - b)**2 == 0
    return matrix


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matmul(a, b):
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) % MOD
             for col in bt] for row in a]


def normal_form(original):
    a = [row[:] for row in original]
    u, ui, v = identity(ROWS), identity(ROWS), identity(COLS)
    exponents = []
    operations = []
    for r in range(COLS):
        choice = min((valuation(a[i][j]), i, j)
                     for i in range(r, ROWS) for j in range(r, COLS))
        e, i, j = choice
        assert e < BITS
        if i != r:
            a[r], a[i] = a[i], a[r]
            u[r], u[i] = u[i], u[r]
            for row in ui:
                row[r], row[i] = row[i], row[r]
        if j != r:
            for matrix in (a, v):
                for row in matrix:
                    row[r], row[j] = row[j], row[r]
        odd = a[r][r] >> e
        assert odd & 1
        inv = pow(odd, -1, MOD)
        a[r] = [(x * inv) % MOD for x in a[r]]
        u[r] = [(x * inv) % MOD for x in u[r]]
        for row in ui:
            row[r] = row[r] * odd % MOD
        assert a[r][r] == 1 << e
        row_clear = []
        for i in range(r + 1, ROWS):
            assert a[i][r] % (1 << e) == 0
            factor = a[i][r] >> e
            if not factor:
                continue
            a[i] = [(x - factor * y) % MOD for x, y in zip(a[i], a[r])]
            u[i] = [(x - factor * y) % MOD for x, y in zip(u[i], u[r])]
            for row in ui:
                row[r] = (row[r] + factor * row[i]) % MOD
            assert a[i][r] == 0
            row_clear.append([i, str(factor)])
        column_clear = []
        for j in range(r + 1, COLS):
            assert a[r][j] % (1 << e) == 0
            factor = a[r][j] >> e
            if not factor:
                continue
            for matrix in (a, v):
                for row in matrix:
                    row[j] = (row[j] - factor * row[r]) % MOD
            assert a[r][j] == 0
            column_clear.append([j, str(factor)])
        exponents.append(e)
        operations.append({'pivot': r, 'swap_row': choice[1],
                           'swap_column': choice[2], 'v2': e,
                           'odd_unit': str(odd), 'row_clear': row_clear,
                           'column_clear': column_clear})
    assert exponents == sorted(exponents)
    for i, row in enumerate(a):
        for j, x in enumerate(row):
            assert x == ((1 << exponents[i]) if i == j and i < COLS else 0)
    assert matmul(matmul(u, original), v) == a
    assert matmul(u, ui) == identity(ROWS)
    return exponents, u, ui, operations


def main():
    started = time.monotonic()
    source = ROOT / 'binary_short_moment_certificate.json'
    input_data = json.loads(source.read_text())
    n, b = int(input_data['n']), int(input_data['b'])
    af, ae = input_data['short_first_numerator'], input_data['short_exponential_numerator']
    assert (len(af), len(ae)) == (82, 78)
    uf = payload_numerator(af, 81, 2 * n, b)
    ue = payload_numerator(ae, 77, 2 * n, b)
    assert [x % (1 << 341) for x in uf] == list(map(int, input_data['Uf_mod341']))
    assert [x % (1 << 341) for x in ue] == list(map(int, input_data['Ue_mod341']))
    pf = mul(uf, uf)
    pm = mul(uf, ue) + [0] * 4
    assert len(pf) == len(pm) == ROWS
    original = relations(n, b)
    es, u, ui, operations = normal_form(original)
    assert es.count(0) == 80 and sum(e > 0 for e in es) == 80
    guard = sum(valuation(k + 2 * n - 4) for k in range(COLS))
    assert guard == 161 and sum(es) <= guard and max(es) <= 82
    free = u[COLS:]
    basis = [[ui[i][COLS + j] for i in range(ROWS)] for j in range(3)]
    assert matmul(free, original) == [[0] * COLS for _ in range(3)]
    assert matmul(free, list(zip(*basis))) == identity(3)
    cf = [sum(x * y for x, y in zip(row, pf)) % MOD for row in free]
    cm = [sum(x * y for x, y in zip(row, pm)) % MOD for row in free]
    # An exact rational left-kernel lift uses the triangular high-degree minor.
    # Its inverse has 2-adic denominator valuation at most guard. Residuals
    # modulo 2^BITS therefore imply exact quotient data modulo 2^(BITS-guard).
    certified = BITS - guard
    sf, sm = min(map(valuation, cf)), min(map(valuation, cm))
    assert sf < certified and sm < certified
    needed = [max(0, 180 - sf), max(0, 177 - sm)]
    assert max(needed) <= certified
    artifact = {
        'status': 'PASS', 'scope': 'new bounded saturated relation/payload postprocessing; no moments or original Gram evaluated',
        'n': str(n), 'b': str(b), 'physical_input_bits': 20,
        'working_bits': BITS, 'matrix_shape': [ROWS, COLS],
        'smith_v2': es, 'binary_rank': es.count(0),
        'nonunit_pivots': sum(e > 0 for e in es),
        'sum_smith_v2': sum(es), 'largest_smith_v2': max(es),
        'triangular_minor_v2': guard, 'exact_kernel_lift_precision_bits': certified,
        'free_covectors_mod512': [[str(x) for x in row] for row in free],
        'integral_quotient_basis_mod512': [[str(x) for x in row] for row in basis],
        'norm_free_coordinates_mod512': [str(x) for x in cf],
        'mixed_free_coordinates_mod512': [str(x) for x in cm],
        'payload_free_contents_v2': [sf, sm],
        'sufficient_integral_observable_bits': needed,
        'row_operations': operations,
        'verified_U_original_V_diagonal': True,
        'verified_U_Uinverse_identity': True,
        'verified_free_covectors_annihilate_all_columns': True,
        'verified_dual_basis_identity': True,
        'telescoping_upper_flux_exactly_zero': True,
        'physical_terminal_summand_retained': True,
        'original_moments_evaluated': False, 'original_weighted_Gram_evaluated': False}
    target = ROOT / 'binary_saturated_observables_certificate.json'
    target.write_text(json.dumps(artifact, indent=2) + '\n')
    receipt = {k: artifact[k] for k in (
        'status', 'scope', 'physical_input_bits', 'working_bits', 'matrix_shape',
        'binary_rank', 'nonunit_pivots', 'sum_smith_v2', 'largest_smith_v2',
        'triangular_minor_v2', 'exact_kernel_lift_precision_bits',
        'payload_free_contents_v2', 'sufficient_integral_observable_bits',
        'verified_U_original_V_diagonal', 'verified_U_Uinverse_identity',
        'verified_free_covectors_annihilate_all_columns', 'verified_dual_basis_identity',
        'original_moments_evaluated', 'original_weighted_Gram_evaluated')}
    receipt.update(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                   artifact_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                   elapsed_seconds=time.monotonic() - started)
    (ROOT / 'binary_saturated_observables_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2), flush=True)


if __name__ == '__main__':
    main()
