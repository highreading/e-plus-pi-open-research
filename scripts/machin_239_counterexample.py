#!/usr/bin/env python3
"""Exact modular certificate disproving the naive all-n 239-adic pattern.

For the endpoint-matched Machin Hermite--Pade system, bordered determinants
Delta_A and Delta_B represent A(1) and B(1), up to one common nonzero scalar.
At n=65 this script applies explicit row/column p-power scalings and computes

    p^8580 Delta_A mod p,
    p^8515 Delta_B mod p^2,

with p=239.  All arithmetic below is integer arithmetic modulo p or p^2.
The output proves

    v_p(Delta_A) = -8580,
    v_p(Delta_B) = -8514,

and hence

    v_p(B(1)/A(1)) = 66,

not the largest odd integer <=65, which is 65.

The determinant modulo p^2 is evaluated using unit pivots.  The transformed
Delta_B matrix has rank N-1 modulo p, so N-1 unit pivots suffice and the last
diagonal entry carries exactly one factor p.
"""

from __future__ import annotations

from math import factorial

P = 239
N_DEGREE = 65


def rational_mod(numerator: int, denominator: int, modulus: int) -> int:
    """Reduce a rational whose denominator is prime to P."""
    assert denominator % P
    return numerator % modulus * pow(denominator % modulus, -1, modulus) % modulus


def scaled_machin_coefficient(
    degree: int, exponent: int, modulus: int
) -> int:
    """Return p^exponent*g_degree modulo modulus.

    Here

      g_r = (-1)^((r-1)/2)/r * (16/5^r - 4/p^r)

    for positive odd r, and g_r=0 for even r.  The callers ensure that
    exponent >= degree, so the scaled value is p-integral.
    """
    if degree < 1 or degree % 2 == 0:
        return 0
    assert exponent >= degree
    sign = -1 if ((degree - 1) // 2) & 1 else 1
    inv_degree = pow(degree, -1, modulus)
    inv_five_power = pow(pow(5, degree, modulus), -1, modulus)
    value = (
        16 * pow(P, exponent, modulus) * inv_five_power
        - 4 * pow(P, exponent - degree, modulus)
    )
    return sign * inv_degree * value % modulus


def determinant_mod_with_unit_pivots(
    matrix: list[list[int]], modulus: int, prime: int
) -> tuple[int, int]:
    """Return determinant modulo modulus and rank modulo prime.

    Row and column swaps are allowed.  As long as a unit remains in the
    trailing submatrix, it is used as pivot.  This is exact over Z/modulus.
    For the p^2 matrix certified here, the mod-p rank is N-1.
    """
    a = [row[:] for row in matrix]
    size = len(a)
    assert all(len(row) == size for row in a)
    sign = 1
    product = 1
    unit_rank = 0

    for k in range(size):
        pivot_position: tuple[int, int] | None = None
        for i in range(k, size):
            for j in range(k, size):
                if a[i][j] % prime:
                    pivot_position = (i, j)
                    break
            if pivot_position is not None:
                break

        if pivot_position is None:
            # No unit remains.  In the present certificate this happens only
            # at the final 1 x 1 block.
            if k != size - 1:
                raise RuntimeError(
                    f"unit rank only {k}; expected at least {size - 1}"
                )
            determinant = sign * product * a[k][k] % modulus
            return determinant, unit_rank

        i, j = pivot_position
        if i != k:
            a[k], a[i] = a[i], a[k]
            sign = -sign
        if j != k:
            for row in a:
                row[k], row[j] = row[j], row[k]
            sign = -sign

        pivot = a[k][k] % modulus
        product = product * pivot % modulus
        inverse_pivot = pow(pivot, -1, modulus)
        unit_rank += 1

        for i in range(k + 1, size):
            factor = a[i][k] * inverse_pivot % modulus
            if factor:
                for j in range(k + 1, size):
                    a[i][j] = (a[i][j] - factor * a[k][j]) % modulus
            a[i][k] = 0

    return sign * product % modulus, unit_rank


def delta_b_scaled_matrix(n: int) -> list[list[int]]:
    """Matrix for p^(n(2n+1))*Delta_B modulo p^2.

    First add the appended B-endpoint row to the matching endpoint row,
    turning the latter into the pure C-endpoint row.  The p-power potentials
    are

      jet row k: max(0,k-2n),
      C-endpoint row: -n,
      B-endpoint row: 0,
      b_j column: 0,
      c_j column: 2n-j.

    Their total is n(2n+1), and every scaled entry is p-integral.
    """
    modulus = P * P
    factorials = [factorial(k) for k in range(3 * n + 1)]
    rows: list[list[int]] = []

    for k in range(n + 1, 3 * n + 1):
        row_power = max(0, k - 2 * n)
        row: list[int] = []
        for j in range(n + 1):
            row.append(
                rational_mod(
                    pow(P, row_power, modulus),
                    factorials[k - j],
                    modulus,
                )
            )
        for j in range(n + 1):
            exponent = row_power + 2 * n - j
            row.append(scaled_machin_coefficient(k - j, exponent, modulus))
        rows.append(row)

    # Pure C endpoint after H <- H + B.
    rows.append(
        [0] * (n + 1)
        + [pow(P, n - j, modulus) for j in range(n + 1)]
    )
    # B endpoint.
    rows.append([1] * (n + 1) + [0] * (n + 1))
    return rows


def delta_a_scaled_matrix_mod_p(n: int) -> list[list[int]]:
    """Matrix for p^(2n(n+1))*Delta_A modulo p, for odd n.

    The p-power potentials are

      jet row k: max(0,k-(2n-1)),
      endpoint and A rows: 0,
      b_j column: 0,
      c_j column: 2n-1-j.

    For n=65, the C entries in the final two rows vanish after this scaling
    modulo p.  The resulting determinant is a unit.
    """
    assert n % 2 == 1
    modulus = P
    factorials = [factorial(k) for k in range(3 * n + 1)]
    rows: list[list[int]] = []

    for k in range(n + 1, 3 * n + 1):
        row_power = max(0, k - (2 * n - 1))
        row: list[int] = []
        for j in range(n + 1):
            row.append(
                rational_mod(
                    pow(P, row_power, modulus),
                    factorials[k - j],
                    modulus,
                )
            )
        for j in range(n + 1):
            exponent = row_power + 2 * n - 1 - j
            row.append(scaled_machin_coefficient(k - j, exponent, modulus))
        rows.append(row)

    # Original endpoint row C(1)-B(1)=0.  Its scaled C entries all vanish
    # modulo p for n=65.
    rows.append([P - 1] * (n + 1) + [0] * (n + 1))

    # A(1) after eliminating the coefficients of A(z):
    # b_j coefficient = -sum_{r=0}^{n-j} 1/r!.
    partial_exp: list[int] = []
    value = 0
    for r in range(n + 1):
        value += rational_mod(1, factorials[r], modulus)
        value %= modulus
        partial_exp.append(value)
    rows.append(
        [(-partial_exp[n - j]) % P for j in range(n + 1)]
        + [0] * (n + 1)
    )
    return rows


def bessel_residue_certificate(n: int) -> tuple[int, int]:
    """Return T_(n-1),T_n modulo p.

    The leading low-block determinant for Delta_B is, up to a p-unit,

      S_n = (-1)^n T_n,

    where T_0=T_1=1 and

      T_(m+1) = (4m+2)T_m + T_(m-1).
    """
    if n == 0:
        return 0, 1
    previous, current = 1, 1
    for m in range(1, n):
        previous, current = current, (
            (4 * m + 2) * current + previous
        ) % P
    return previous, current


def low_a_block_certificate(n: int) -> tuple[int, int, int, int, int]:
    """Return the four low-A functionals and their 2-by-2 determinant.

    For n=65, let

      Q(x) = product_(k=66)^129 (x-k).

    This computes the falling-factorial coefficient vectors of Q and xQ,
    applies the endpoint and A functionals modulo p, and returns

      L(Q), M(Q), L(xQ), M(xQ), determinant.
    """
    assert n == 65
    q = []
    for j in range(n):
        numerator = factorial(2 * n - 1 - j)
        denominator = n * factorial(j) * factorial(n - 1 - j)
        assert numerator % denominator == 0
        coefficient = numerator // denominator
        if (n - 1 - j) & 1:
            coefficient = -coefficient
        q.append(coefficient % P)
    q.append(0)

    # x*(x)_j = (x)_(j+1) + j*(x)_j.
    xq = [0] * (n + 1)
    for j in range(n):
        xq[j] = (xq[j] + j * q[j]) % P
        xq[j + 1] = (xq[j + 1] + q[j]) % P

    partial_exp = []
    value = 0
    for r in range(n + 1):
        value = (value + pow(factorial(r), -1, P)) % P
        partial_exp.append(value)

    def functionals(vector: list[int]) -> tuple[int, int]:
        endpoint = sum(vector) % P
        a_value = -sum(
            partial_exp[n - j] * vector[j] for j in range(n + 1)
        ) % P
        return endpoint, a_value

    lq, mq = functionals(q)
    lxq, mxq = functionals(xq)
    determinant = (lq * mxq - lxq * mq) % P
    return lq, mq, lxq, mxq, determinant


def main() -> None:
    n = N_DEGREE
    assert 3 * n < P

    t64, t65 = bessel_residue_certificate(n)
    assert all(
        bessel_residue_certificate(m)[1] != 0 for m in range(1, n)
    )
    assert (t64, t65) == (111, 0)
    assert [
        bessel_residue_certificate(m)[1] for m in range(58, 66)
    ] == [68, 214, 93, 15, 198, 42, 111, 0]
    assert low_a_block_certificate(n) == (113, 205, 111, 177, 114)

    matrix_b = delta_b_scaled_matrix(n)
    det_b_mod_p2, rank_b_mod_p = determinant_mod_with_unit_pivots(
        matrix_b, P * P, P
    )
    assert rank_b_mod_p == len(matrix_b) - 1
    assert det_b_mod_p2 == P * 121

    matrix_a = delta_a_scaled_matrix_mod_p(n)
    det_a_mod_p, rank_a_mod_p = determinant_mod_with_unit_pivots(
        matrix_a, P, P
    )
    assert rank_a_mod_p == len(matrix_a)
    assert det_a_mod_p == 181

    weight_b = n * (2 * n + 1)
    weight_a = 2 * n * (n + 1)
    valuation_delta_b = -weight_b + 1
    valuation_delta_a = -weight_a
    endpoint_ratio_valuation = valuation_delta_b - valuation_delta_a

    assert (weight_b, weight_a) == (8515, 8580)
    assert (valuation_delta_b, valuation_delta_a) == (-8514, -8580)
    assert endpoint_ratio_valuation == 66

    print(f"p={P}, n={n}, 3n={3*n}<p")
    print(f"T_64 mod p={t64}, T_65 mod p={t65}")
    print(
        "scaled Delta_B: rank mod p="
        f"{rank_b_mod_p}, determinant mod p^2={det_b_mod_p2}"
        f"={P}*{det_b_mod_p2 // P}"
    )
    print(f"scaled Delta_A: determinant mod p={det_a_mod_p}")
    print(f"v_p(Delta_B)={valuation_delta_b}")
    print(f"v_p(Delta_A)={valuation_delta_a}")
    print(f"v_p(B(1)/A(1))={endpoint_ratio_valuation}")
    print("largest odd integer <=n is 65; the proposed pattern is false.")


if __name__ == "__main__":
    main()
