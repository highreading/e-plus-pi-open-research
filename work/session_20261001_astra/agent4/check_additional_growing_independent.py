"""Independent structural audit; no actual HP index or prime scan.

All finite matrix controls use free columns, independent symbols, or one
explicit arbitrary matrix. Reviewed sources are read but never executed.
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import sympy as sp

SESSION = Path('work/session_20261001_astra')
OUT = SESSION / 'agent4'
checks = {}


def require(label, condition):
    if not bool(condition):
        raise AssertionError(label)
    checks[label] = True


def zero(label, expression):
    reduced = sp.simplify(sp.expand(expression))
    if reduced != 0:
        raise AssertionError((label, str(reduced)))
    checks[label] = True


def factorial_zero(label, expression):
    reduced = sp.simplify(sp.combsimp(expression))
    if reduced != 0:
        raise AssertionError((label, str(reduced)))
    checks[label] = True


def product(values):
    answer = 1
    for value in values:
        answer *= value
    return answer


def falling_polynomial(value, order):
    return product(value - j for j in range(order))


def permutation_sign(sequence):
    inversions = sum(sequence[i] > sequence[j]
                     for i in range(len(sequence))
                     for j in range(i + 1, len(sequence)))
    return -1 if inversions % 2 else 1


def elementary(nodes, degree):
    if degree < 0 or degree > len(nodes):
        return 0
    return sum(product(part) for part in combinations(nodes, degree))


def vandermonde(nodes):
    return product(nodes[j] - nodes[i]
                   for i in range(len(nodes))
                   for j in range(i + 1, len(nodes)))


def correction(nodes, holes):
    d = len(nodes)
    if not holes:
        return 1
    if len(holes) == 1:
        return elementary(nodes, d - holes[0])
    if len(holes) == 2:
        a, c = holes
        return (elementary(nodes, d - a) * elementary(nodes, d + 1 - c)
                - elementary(nodes, d - a + 1) * elementary(nodes, d - c))
    raise AssertionError('Only zero, one, or two missing powers are allowed.')


def ordered_partitions(remaining, sizes, group=0, previous=()):
    if group == 3:
        if len(remaining) == sizes[group]:
            yield previous + (tuple(remaining),)
        return
    for chosen in combinations(remaining, sizes[group]):
        chosen_set = set(chosen)
        rest = tuple(i for i in remaining if i not in chosen_set)
        yield from ordered_partitions(rest, sizes, group + 1,
                                      previous + (tuple(chosen),))


def main():
    input_paths = [
        SESSION / 'agent1/ADDITIONAL_GROWING_CONTENT.md',
        SESSION / 'agent1/check_additional_growing_content.py',
        SESSION / 'agent1/additional_growing_content_certificate.json',
        SESSION / 'agent1/GROWING_DEGREE_ARITHMETIC.md',
    ]
    preserved_names = [
        'B1_WHOLE_FAMILY_REVIEW.md', 'B2_WHOLE_FAMILY_REVIEW.md',
        'INHERITED_SYNTHESIS_REVIEW.md', 'DRAFT_OBSERVATIONS_REVIEW.md',
        'GROWING_ARITHMETIC_CONTENT_REVIEW.md',
        'check_inherited_rates_counts.py', 'audit_rate_count_certificate.json',
        'audit_rate_count_stdout.txt', 'check_whole_family.py',
        'whole_family_checks.json', 'whole_family_check_stdout.txt',
        'check_b2_whole_family.py', 'b2_whole_family_checks.json',
        'b2_whole_family_check_stdout.txt', 'check_growing_content_scales.py',
        'growing_content_scale_checks.json', 'growing_content_scale_stdout.txt',
        'growing_content_completion_verification.json', 'REPORT.md',
    ]
    protected_paths = input_paths + [OUT / name for name in preserved_names]
    hashes_before = {str(path): sha256(path.read_bytes()).hexdigest()
                     for path in protected_paths}
    author = json.loads(input_paths[2].read_text(encoding='utf-8'))
    require('author_certificate_payload_read',
            author['status'] == 'PASS_SYMBOLIC_STRUCTURAL_IDENTITIES'
            and len(author['checks']) == 12
            and all(value is True for value in author['checks'].values()))

    x = sp.symbols('x', positive=True)
    y = sp.symbols('y')
    k, r = sp.symbols('k r', integer=True, nonnegative=True)
    n = sp.symbols('n', integer=True, positive=True)
    hfun = sp.Function('H')(x)
    pfun = sp.Function('Pcal')(x)

    # Derive the raw third-order equation from the two adjacent identities.
    adjacent_zero = (x * sp.diff(hfun, x, 2) / 2
                     + (k + 1 - x) * (sp.diff(hfun, x) - hfun))
    adjacent_first = (k + 1) * (hfun - sp.diff(hfun, x)
                                + sp.diff(hfun, x, 2) / 2)
    raw_ode = (x * sp.diff(hfun, x, 3)
               + (k + 2 - 2*x) * sp.diff(hfun, x, 2)
               + 2*(x - 1) * sp.diff(hfun, x) - 2*k*hfun)
    zero('raw_ODE_from_adjacent_identities',
         2*(sp.diff(adjacent_zero, x) - adjacent_first) - raw_ode)

    substituted_h = x**(-k) * pfun
    translated_next = x**(k + 1) * (
        x * sp.diff(substituted_h, x, 2) / 2
        + (k + 1 - x) * (sp.diff(substituted_h, x) - substituted_h))
    second_coefficients = {
        2: x*x,
        1: 2*x*(1 - x),
        0: 2*x*x - 2*x - k*(k + 1),
    }
    predicted_twice_next = sum(
        coefficient * sp.diff(pfun, x, order)
        for order, coefficient in second_coefficients.items())
    zero('Pcal_adjacent_differential_operator',
         2*translated_next - predicted_twice_next)

    third_coefficients = {
        3: x*x,
        2: (2 - 2*k)*x - 2*x*x,
        1: k*(k - 1) + (4*k - 2)*x + 2*x*x,
        0: -2*k*k - 4*k*x,
    }
    predicted_ode = sum(coefficient * sp.diff(pfun, x, order)
                        for order, coefficient in third_coefficients.items())
    raw_substituted = (x * sp.diff(substituted_h, x, 3)
                       + (k + 2 - 2*x) * sp.diff(substituted_h, x, 2)
                       + 2*(x - 1) * sp.diff(substituted_h, x)
                       - 2*k*substituted_h)
    zero('Pcal_third_order_translation',
         x**(k + 1)*raw_substituted - predicted_ode)

    # Extract a general Taylor coefficient from the differential operator.
    theta = {shift: sp.Symbol('theta_shift_' + str(shift))
             for shift in range(-2, 3)}
    extracted = 0
    for order, coefficient in second_coefficients.items():
        polynomial = sp.Poly(sp.expand(coefficient.subs(x, 1 + y)), y)
        for (power,), value in polynomial.terms():
            shift = order - power
            extracted += (value * falling_polynomial(r + shift, order)
                          * theta[shift])
    predicted_taylor = (
        (r + 2)*(r + 1)*theta[2]/2
        + r*(r + 1)*theta[1]
        + (r*(r - 3) - k*(k + 1))*theta[0]/2
        - (r - 2)*theta[-1] + theta[-2])
    zero('Taylor_recurrence_extracted_from_operator',
         extracted/2 - predicted_taylor)
    zero('Taylor_middle_coefficient_integer_binomial_form',
         (r*(r - 3) - k*(k + 1))/2
         - (r*(r - 1)/2 - r - k*(k + 1)/2))

    # Independently apply general Leibniz coefficients to the third-order ODE.
    jets = {shift: sp.Symbol('E_shift_' + str(shift))
            for shift in range(-1, 4)}
    differentiated = 0
    for order, coefficient in third_coefficients.items():
        degree = sp.Poly(coefficient, x).degree()
        for derivatives_on_coefficient in range(degree + 1):
            a = derivatives_on_coefficient
            binomial_factor = falling_polynomial(r, a) / sp.factorial(a)
            differentiated += (
                binomial_factor * sp.diff(coefficient, x, a).subs(x, 1)
                * jets[order - a])
    predicted_derivative = (
        jets[3] - 2*(k - r)*jets[2]
        + (k - r)*(k - r + 3)*jets[1]
        - 2*(k - r)*(k - r + 2)*jets[0]
        - 2*r*(2*k - r + 1)*jets[-1])
    zero('derivative_recurrence_from_general_Leibniz',
         differentiated - predicted_derivative)
    require('negative_derivative_term_absent_at_r_zero',
            sp.expand(predicted_derivative).coeff(jets[-1]).subs(r, 0) == 0)

    ell, column = sp.symbols('ell column', integer=True, nonnegative=True)
    spectral_node = ell*(ell + 2*n + 1)
    zero('column_derivative_index',
         (ell + column + 3) - (ell + (column + 4) - 1))
    zero('column_k_minus_r', (n + ell) - (ell + column) - (n - column))
    zero('spectral_coefficient',
         (ell + column)*(2*n + ell - column + 1)
         - spectral_node - column*(2*n + 1 - column))
    uindex, vindex = sp.symbols('uindex vindex', integer=True)
    zero('quadratic_node_Vandermonde_difference',
         vindex*(vindex + 2*n + 1) - uindex*(uindex + 2*n + 1)
         - (vindex - uindex)*(2*n + 1 + uindex + vindex))

    # The integral normalized state is checked without evaluating any H index.
    h, unorm, vnorm = sp.symbols('h unorm vnorm')
    raw_u = k*unorm
    raw_v = k*(k - 1)*vnorm
    state_next = sp.Matrix([
        -k*h + k*raw_u + raw_v/2,
        h - raw_u + raw_v/2,
        sp.cancel((k*h + raw_u - (k + 2)*raw_v/2)/k),
    ])
    state_matrix = sp.Matrix([
        [-k, k*k, k*(k - 1)/2],
        [1, -k, k*(k - 1)/2],
        [1, 1, 1 - k*(k + 1)/2],
    ])
    require('normalized_three_state_transition',
            all(sp.simplify(value) == 0 for value in
                state_next - state_matrix*sp.Matrix([h, unorm, vnorm])))
    zero('normalized_three_state_determinant',
         state_matrix.det() - k*(k - 1)*(k + 1)**2/2)

    # Use a=2*lambda as the polynomial variable, so coefficient integrality
    # is checked directly, without division by powers of two.
    spectral_a = sp.symbols('spectral_a')
    abstract_column_count = 12
    initial = sp.eye(4)
    columns = [initial[:, seed] for seed in range(4)]
    for j in range(abstract_column_count - 4):
        nxt = (2*(n - j)*columns[j + 3]
               - (n - j)*(n - j + 3)*columns[j + 2]
               + 2*(n - j)*(n - j + 2)*columns[j + 1]
               + (spectral_a + 2*j*(2*n + 1 - j))*columns[j])
        columns.append(nxt.applyfunc(sp.expand))
    transform = sp.zeros(abstract_column_count)
    for j, vector in enumerate(columns):
        for seed in range(4):
            polynomial = sp.Poly(vector[seed], spectral_a)
            for (power,), coefficient in polynomial.terms():
                if coefficient == 0:
                    continue
                index = 4*power + seed
                assert index <= j, ('nontriangular entry', index, j)
                assert sp.Poly(coefficient, n).domain == sp.ZZ
                transform[index, j] = coefficient
    require('free_column_change_upper_unitriangular',
            all(transform[i, i] == 1 for i in range(abstract_column_count))
            and all(transform[i, j] == 0
                    for i in range(abstract_column_count) for j in range(i)))
    free_w = sp.Matrix(4, abstract_column_count,
                       lambda seed, j: spectral_a**(j//4)
                       if seed == j % 4 else 0)
    free_r = sp.Matrix.hstack(*columns)
    require('free_columns_R_equals_WT',
            all(sp.expand(value) == 0 for value in free_r - free_w*transform))
    inverse = sp.eye(abstract_column_count)
    for j in range(abstract_column_count):
        for i in range(j - 1, -1, -1):
            inverse[i, j] = sp.expand(-sum(
                transform[i, a]*inverse[a, j] for a in range(i + 1, j + 1)))
    require('column_change_inverse_integral',
            all(sp.Poly(value, n).domain == sp.ZZ for value in inverse))
    require('column_change_inverse_verified',
            all(sp.expand(value) == 0 for value in
                transform*inverse - sp.eye(abstract_column_count)))
    require('column_change_determinant_one', transform.det() == 1)

    # One arbitrary matrix checks both directions of Cauchy--Binet and
    # demonstrates why appended rows must transform. This is not HP data.
    small_t = transform[:5, :5]
    small_inverse = inverse[:5, :5]
    arbitrary_w = sp.Matrix([[1, 0, 0, 1, 2],
                             [0, 1, 0, 3, 5],
                             [0, 0, 1, 7, 11]])
    arbitrary_r = arbitrary_w*small_t
    triples = list(combinations(range(5), 3))
    minors_w = {indices: arbitrary_w[:, list(indices)].det()
                for indices in triples}
    minors_r = {indices: sp.expand(arbitrary_r[:, list(indices)].det())
                for indices in triples}
    for indices in triples:
        forward = sum(minors_w[other]
                      * small_t.extract(list(other), list(indices)).det()
                      for other in triples)
        backward = sum(minors_r[other]
                       * small_inverse.extract(list(other), list(indices)).det()
                       for other in triples)
        zero('Cauchy_Binet_forward_' + str(indices),
             minors_r[indices] - forward)
        zero('Cauchy_Binet_backward_' + str(indices),
             minors_w[indices] - backward)
    appended_v = sp.Matrix([[1, 0, 0, 0, 0]])
    appended_w = sp.Matrix([[0, 1, 0, 0, 0]])
    original_det = arbitrary_r.col_join(appended_v).col_join(appended_w).det()
    transformed_det = arbitrary_w.col_join(appended_v*small_inverse).col_join(
        appended_w*small_inverse).det()
    unchanged_rows_det = arbitrary_w.col_join(appended_v).col_join(appended_w).det()
    zero('appended_rows_transform_by_T_inverse', original_det - transformed_det)
    wrong_difference = sp.expand(original_det - unchanged_rows_det)
    zero('unchanged_appended_rows_error_control',
         wrong_difference - 2*n*(n + 2))
    require('unchanged_appended_rows_generally_incorrect', wrong_difference != 0)

    # Symbolic alternants, including empty groups. These are abstract
    # polynomial identities, not samples of any H_k or HP construction.
    alternant_records = []
    abstract_node_sets = ((), sp.symbols('z0:1'), sp.symbols('z0:3'))
    for nodes in abstract_node_sets:
        d = len(nodes)
        for missing in (0, 1, 2):
            available = tuple(range(d + missing))
            for holes in combinations(available, missing):
                powers = [power for power in available if power not in holes]
                determinant = (sp.Matrix(d, d,
                    lambda row, col: nodes[row]**powers[col]).det()
                    if d else sp.Integer(1))
                phi = correction(nodes, holes)
                label = 'alternant_d{}_holes{}'.format(d, holes)
                zero(label, determinant - vandermonde(nodes)*phi)
                alternant_records.append({'dimension': d, 'missing_powers': list(holes)})

    # One fixed seven-row abstract matrix tests the complete four-group sum
    # for prescribed omissions. Arbitrary square nodes are unrelated to n.
    nodes = (1, 4, 9, 16, 25, 36, 49)
    weights = ((2, 3, 5, 7), (1, -2, 4, 6), (3, 0, -1, 2),
               (-2, 5, 1, 4), (4, 1, 3, -3), (0, 6, -2, 1),
               (5, -1, 2, 0))
    available_columns = tuple(range(9))
    group_counts = [sum(j % 4 == seed for j in available_columns)
                    for seed in range(4)]
    arbitrary_spectral_w = sp.Matrix(7, 9,
        lambda row, j: (2*nodes[row])**(j//4)*weights[row][j % 4])
    omissions = ((0, 4), (0, 8), (4, 8), (1, 5), (0, 5), (2, 8))
    expansion_records = []
    signs_seen = set()
    for deleted in omissions:
        retained = [j for j in available_columns if j not in deleted]
        grouped = sorted(retained, key=lambda j: (j % 4, j//4))
        column_sign = permutation_sign(grouped)
        holes = [tuple(sorted(j//4 for j in deleted if j % 4 == seed))
                 for seed in range(4)]
        sizes = [group_counts[seed] - len(holes[seed]) for seed in range(4)]
        qsum = sum(j//4 for j in retained)
        summation = 0
        partition_count = 0
        nonzero_terms = 0
        term_cache = {}
        for partition in ordered_partitions(tuple(range(7)), sizes):
            concatenated = tuple(row for group in partition for row in group)
            row_sign = permutation_sign(concatenated)
            signs_seen.add(column_sign*row_sign)
            term = row_sign
            for seed, group in enumerate(partition):
                key = (seed, group)
                if key not in term_cache:
                    group_nodes = tuple(nodes[row] for row in group)
                    term_cache[key] = (
                        product(weights[row][seed] for row in group)
                        * vandermonde(group_nodes)
                        * correction(group_nodes, holes[seed]))
                term *= term_cache[key]
            summation += term
            partition_count += 1
            nonzero_terms += int(term != 0)
        predicted = 2**qsum * column_sign * summation
        direct = arbitrary_spectral_w[:, retained].det()
        require('four_group_expansion_' + str(deleted), direct == predicted)
        expansion_records.append({
            'deleted_columns': list(deleted),
            'retained_columns': retained,
            'grouped_columns': grouped,
            'column_permutation_sign': column_sign,
            'missing_exponents_by_group': [list(group) for group in holes],
            'retained_group_sizes': sizes,
            'power_of_two_exponent': qsum,
            'row_partitions': partition_count,
            'nonzero_partition_terms': nonzero_terms,
            'direct_determinant': str(direct),
            'expanded_determinant': str(predicted),
        })
    require('four_group_controls_include_both_permutation_signs', signs_seen == {-1, 1})

    # Exact endpoint clearer correspondence. Lambda_clear is unrelated to
    # the spectral diagonal Lambda used in the column theorem.
    Fclear = sp.factorial(2*n + 1)
    f = 2**n / sp.factorial(n)**2
    lambda_clear = (2**(n + 1)*sp.factorial(n + 2)*Fclear
                    * sp.factorial(n)**2)
    pair_scale = f*Fclear**2
    beta = 2**n*(2*n + 1)*sp.binomial(2*n, n)
    alpha = sp.binomial(2*n + 1, n)**2*sp.factorial(n + 1)
    factorial_zero('f_times_F_integral_expression', f*Fclear - beta)
    factorial_zero('second_kind_clearance_integral_expression',
                   pair_scale/(2**n*sp.factorial(n + 1)) - alpha)
    factorial_zero('factorial_term_clearance_integral_expression',
                   2*f*pair_scale - 2*beta**2)
    factorial_zero('denominator_pair_scale_integral_expression', pair_scale - beta*Fclear)
    rational_scale = Fclear/(2*sp.factorial(n + 2)*sp.factorial(n)**4)
    factorial_zero('new_pair_to_old_pair_rational_scale',
                   pair_scale/lambda_clear - rational_scale)

    sigma, cstar, kappastar, wp, wu, tp, tu = sp.symbols(
        'sigma cstar kappastar wp wu tp tu')
    w1, w2, at, bt = sp.symbols('w1 w2 at bt', integer=True)
    complete_numerator = (2*(wp + tp)*sigma
                          - (n + 1)*(wu + tu)*cstar - 2*f*kappastar)
    substitution = {wp: w1/(2**n*sp.factorial(n + 1)),
                    wu: w2/(2**n*sp.factorial(n + 1)),
                    tp: at/Fclear, tu: bt/Fclear}
    integral_n0 = (2*(alpha*w1 + beta*at)*sigma
                   - (n + 1)*(alpha*w2 + beta*bt)*cstar
                   - 2*beta**2*kappastar)
    factorial_zero('complete_N0_termwise_integer_clearing',
                   pair_scale*complete_numerator.subs(substitution) - integral_n0)
    rho_plus, gamma_high, dcontent, nstar, dstar = sp.symbols(
        'rho_plus Gamma dcontent Nstar Dstar', nonzero=True)
    monic_M = 2**(2*n + 3)*Fclear**2*rho_plus
    endpoint_factor = ((-1)**n*gamma_high*dcontent*f
                       /(rho_plus*2**(2*n + 3)))
    factorial_zero('monic_X_equals_signed_Gamma_d_N0',
                   monic_M*endpoint_factor*nstar
                   - (-1)**n*gamma_high*dcontent*pair_scale*nstar)
    factorial_zero('monic_Y_equals_signed_Gamma_d_Z0',
                   monic_M*endpoint_factor*dstar
                   - (-1)**n*gamma_high*dcontent*pair_scale*dstar)
    factorial_zero('old_and_new_g_formulas_have_identical_scale',
                   gamma_high*dcontent*pair_scale/lambda_clear
                   - gamma_high*dcontent*rational_scale)

    require('protected_inputs_and_completed_reviews_unchanged',
            all(sha256(Path(path).read_bytes()).hexdigest() == digest
                for path, digest in hashes_before.items()))
    result = {
        'status': 'PASS_INDEPENDENT_STRUCTURAL_CHECKS',
        'checks': checks,
        'check_count': len(checks),
        'author_certificate_checks_recorded': len(author['checks']),
        'author_program_executed': False,
        'scope': 'Formal recurrences and exact abstract linear-algebra controls; all-size results require the accompanying proof review.',
        'actual_HP_indices_evaluated': [],
        'primes_scanned': [],
        'abstract_free_column_count': abstract_column_count,
        'unitriangular_matrix': [[str(transform[i, j]) for j in range(abstract_column_count)]
                                for i in range(abstract_column_count)],
        'integer_inverse_matrix': [[str(inverse[i, j]) for j in range(abstract_column_count)]
                                  for i in range(abstract_column_count)],
        'Cauchy_Binet_control': 'Both directions for all ten three-column minors of one arbitrary 3-by-5 matrix.',
        'endpoint_appended_rows': 'det[R;v;w] = det[W;v*T_inverse;w*T_inverse]',
        'unchanged_appended_rows_error_polynomial': str(wrong_difference),
        'abstract_alternant_checks': alternant_records,
        'four_group_expansion_controls': expansion_records,
        'scale_correspondence': {
            'spectral_Lambda': 'diag(l(l+2n+1))',
            'endpoint_Lambda_clear': '2^(n+1)(n+2)!(2n+1)!(n!)^2',
            'new_integer_pair': 'f F^2 (Nstar,Dstar)',
            'g0': 'F*gamma_end/[2(n+2)!(n!)^4]',
            'g': 'Gamma*d*g0',
            'Gamma': 'Crows*mu',
            'gamma_min': 'Gamma/A_b^2; distinct from gamma_end',
            'g_over_A_b_squared': 'gamma_min*d*g0',
            'rational_scale_denominator_retained': True,
        },
        'strict_residual_target_above_one_half_endorsed': False,
        'growing_degree_nonvanishing_proved': False,
        'new_content_growth_rate_proved': False,
        'protected_sha256': hashes_before,
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    destination = OUT / 'additional_growing_independent_checks.json'
    payload = json.dumps(result, indent=2) + '\n'
    if destination.exists():
        assert destination.read_text(encoding='utf-8') == payload, 'An existing independent result differs; preserved.'
    else:
        destination.write_text(payload, encoding='utf-8')
    assert json.loads(destination.read_text(encoding='utf-8')) == result
    print(json.dumps({
        'status': result['status'],
        'check_count': result['check_count'],
        'abstract_free_columns': abstract_column_count,
        'abstract_alternant_checks': len(alternant_records),
        'four_group_expansion_controls': len(expansion_records),
        'appended_row_transformation_verified': True,
        'integer_pair_clearing_and_rational_scale_verified': True,
        'protected_artifacts_unchanged': True,
        'actual_HP_indices_evaluated': [],
        'primes_scanned': [],
        'certificate': str(destination),
    }, indent=2))


if __name__ == '__main__':
    main()
