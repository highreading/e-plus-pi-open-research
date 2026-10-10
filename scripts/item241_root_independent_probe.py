#!/usr/bin/env python3
"""Independent convolution and state checks for frozen Item 241."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


PRIMES = [17, 19, 23, 29, 43, 101, 211, 401, 503, 809, 1009]


def convolution(left, right, p):
    out = [0] * (len(left) + len(right) - 1)
    left_support = [(i, x) for i, x in enumerate(left) if x]
    right_support = [(j, y) for j, y in enumerate(right) if y]
    for i, x in left_support:
        for j, y in right_support:
            out[i + j] = (out[i + j] + x * y) % p
    return out


def coefficient(values, index):
    return values[index] if 0 <= index < len(values) else 0


def build_prefixes(p):
    inv = [0] + [pow(k, -1, p) for k in range(1, p)]
    harmonic = [0] * p
    alpha = [0] * p
    for k in range(1, p):
        harmonic[k] = (harmonic[k - 1] + inv[k]) % p
        alpha[k] = (alpha[k - 1] + (inv[k] if k % 2 == 0 else -inv[k])) % p
    h = (p - 1) // 2
    odd_character = [0] * (h + 1)
    for u in range(h):
        term = inv[2 * u + 1]
        odd_character[u + 1] = (
            odd_character[u] + (term if u % 2 == 0 else -term)
        ) % p
    return inv, harmonic, alpha, odd_character


def endpoint_values(p, n):
    h = (p - 1) // 2
    chi = 1 if h % 2 == 0 else -1
    c_value = (2, 0, -2, 0)[n % 4]
    j_value = (0, -2 * chi, 0, 2 * chi)[n % 4]
    return c_value % p, j_value % p


def original_arrays(p):
    inv = [0] + [pow(k, -1, p) for k in range(1, p)]
    a_base = [0] * p
    b_base = [0] * (2 * p - 1)
    for k in range(1, p):
        a_base[k] = -inv[k] % p
        b_base[2 * k] = (inv[k] if k % 2 else -inv[k]) % p
    return (
        convolution(a_base, a_base, p),
        convolution(b_base, b_base, p),
        convolution(a_base, b_base, p),
    )


def original_components(p, n, arrays, prefixes):
    a, b, c = arrays
    inv, harmonic, _, _ = prefixes
    inverse_n = inv[n]
    c_endpoint, j_endpoint = endpoint_values(p, n)
    k1 = (
        -j_endpoint * inverse_n * inverse_n
        - 9 * harmonic[n - 1] * inverse_n
    )
    if n % 2 == 0:
        k1 += 10 * c_endpoint * harmonic[n // 2 - 1] * inverse_n
    else:
        k1 -= (
            j_endpoint
            * harmonic[(p + n) // 2 - 1]
            * inverse_n
        )
    aa = 9 * coefficient(a, p + n) - 18 * coefficient(a, n)
    bb = (
        -3 * coefficient(b, 3 * p + n)
        + 6 * coefficient(b, 2 * p + n)
        + 6 * coefficient(b, p + n)
        - 36 * coefficient(b, n)
    )
    ab = (
        -9 * coefficient(c, 2 * p + n)
        - 16 * coefficient(c, p + n)
        + 54 * coefficient(c, n)
    )
    return tuple(value % p for value in (k1, aa, bb, ab))


def collapsed_components(p, n, prefixes):
    inv, harmonic, alpha, odd_character = prefixes
    h = (p - 1) // 2
    chi = 1 if h % 2 == 0 else -1
    inverse_n = inv[n]
    inverse_n2 = inverse_n * inverse_n % p
    c_endpoint, j_endpoint = endpoint_values(p, n)

    k1 = (
        -j_endpoint * inverse_n2
        - 9 * harmonic[n - 1] * inverse_n
    )
    if n % 2 == 0:
        k1 += 10 * c_endpoint * harmonic[n // 2 - 1] * inverse_n
    else:
        k1 -= j_endpoint * harmonic[(p + n) // 2 - 1] * inverse_n

    aa = -54 * harmonic[n - 1] * inverse_n - 18 * inverse_n2

    if n % 2 == 0:
        u = n // 2
        eps = 1 if u % 2 == 0 else -1
        bb = (2 * eps) * (
            -30 * harmonic[u - 1] * inv[u] + 6 * inv[u] * inv[u]
        )
        c0 = (1 + eps) * alpha[u - 1] * inverse_n
        c1 = (
            alpha[h + u] - alpha[u]
            + 2 * chi * eps * odd_character[h]
        ) * inverse_n
        c2 = (
            alpha[p - 1] - alpha[h + u]
            - eps * (alpha[h] - alpha[u])
        ) * inverse_n
        full = (
            (
                -63 * harmonic[2 * u - 1]
                - 100 * eps * harmonic[u - 1]
                - 9 * alpha[p - 1]
                - 7 * alpha[h + u]
                + 9 * eps * alpha[h]
                - 32 * chi * eps * odd_character[h]
                + (70 + 45 * eps) * alpha[u - 1]
            )
            * inverse_n
            + (80 * eps - 36) * inverse_n2
        )
    else:
        u = (n - 1) // 2
        eps = 1 if u % 2 == 0 else -1
        hn = (p + n) // 2
        bb = j_endpoint * (
            3 * harmonic[hn - 1] * inv[hn] - 3 * inv[hn] * inv[hn]
        )
        c0 = (alpha[u] + 2 * eps * odd_character[u]) * inverse_n
        c1 = (
            alpha[h + u] - alpha[u] - chi * eps * alpha[h]
        ) * inverse_n
        c2 = (
            alpha[p - 1] - alpha[h + u + 1]
            - 2 * eps * (odd_character[h] - odd_character[u + 1])
        ) * inverse_n
        full = (
            (
                -63 * harmonic[2 * u]
                - 10 * chi * eps * harmonic[h + u]
                - 9 * alpha[p - 1]
                - 7 * alpha[h + u]
                + 70 * alpha[u]
                + 16 * chi * eps * alpha[h]
                + 18 * eps * odd_character[h]
                + 90 * eps * odd_character[u]
            )
            * inverse_n
            + (8 * chi * eps - 36) * inverse_n2
        )
    ab = -9 * c2 - 16 * c1 + 54 * c0
    return tuple(value % p for value in (k1, aa, bb, ab, c0, c1, c2, full))


def transition_failures(p, prefixes):
    inv, harmonic, alpha, odd_character = prefixes
    h = (p - 1) // 2
    chi = 1 if h % 2 == 0 else -1
    failures = []
    even_checks = 0
    odd_checks = 0
    z_checks = 0
    for u in range(1, h):
        eps = 1 if u % 2 == 0 else -1
        identities = [
            harmonic[2 * u + 1]
            - harmonic[2 * u - 1] - inv[2 * u] - inv[2 * u + 1],
            (-eps) * harmonic[u] + eps * harmonic[u - 1] + eps * inv[u],
            alpha[h + u + 1] - alpha[h + u]
            + chi * eps * inv[h + u + 1],
            alpha[u] - alpha[u - 1] - eps * inv[u],
            (-eps) * alpha[u] + eps * alpha[u - 1] + inv[u],
        ]
        if any(value % p for value in identities):
            failures.append(["even", p, u])
        even_checks += 1
    for u in range(0, h - 1):
        eps = 1 if u % 2 == 0 else -1
        r_u = eps * odd_character[u] % p
        r_next = (-eps) * odd_character[u + 1] % p
        identities = [
            harmonic[2 * u + 2]
            - harmonic[2 * u] - inv[2 * u + 1] - inv[2 * u + 2],
            (-eps) * harmonic[h + u + 1]
            + eps * harmonic[h + u] + eps * inv[h + u + 1],
            alpha[h + u + 1] - alpha[h + u]
            + chi * eps * inv[h + u + 1],
            alpha[u + 1] - alpha[u] + eps * inv[u + 1],
            r_next + r_u + inv[2 * u + 1],
        ]
        if any(value % p for value in identities):
            failures.append(["odd", p, u])
        odd_checks += 1
        z_u = 90 * r_u * inv[2 * u + 1] % p
        z_next = 90 * r_next * inv[2 * u + 3] % p
        z_rhs = (
            -(2 * u + 1) * inv[2 * u + 3] * z_u
            - 90 * inv[2 * u + 1] * inv[2 * u + 3]
        ) % p
        if z_next != z_rhs:
            failures.append(["z", p, u])
        z_checks += 1
    return failures, even_checks, odd_checks, z_checks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    failures = []
    pair_count = 0
    component_count = 0
    transition_counts = [0, 0, 0]
    digest_rows = []
    for p in PRIMES:
        prefixes = build_prefixes(p)
        arrays = original_arrays(p)
        for n in range(1, p):
            original = original_components(p, n, arrays, prefixes)
            collapsed = collapsed_components(p, n, prefixes)
            if original != collapsed[:4]:
                failures.append(["component", p, n, list(original), list(collapsed[:4])])
            full_original = sum(original) % p
            if full_original != collapsed[7]:
                failures.append(["full", p, n, full_original, collapsed[7]])
            # Compare each mixed coefficient before taking its weighted sum.
            c_array = arrays[2]
            actual_c = [
                coefficient(c_array, n) % p,
                coefficient(c_array, p + n) % p,
                coefficient(c_array, 2 * p + n) % p,
            ]
            if actual_c != list(collapsed[4:7]):
                failures.append(["mixed", p, n, actual_c, list(collapsed[4:7])])
            digest_rows.append((p, n, full_original))
            pair_count += 1
            component_count += 7
        local_failures, ec, oc, zc = transition_failures(p, prefixes)
        failures.extend(local_failures)
        transition_counts[0] += ec
        transition_counts[1] += oc
        transition_counts[2] += zc

    digest = hashlib.sha256(
        "\n".join(f"{p},{n},{value}" for p, n, value in digest_rows).encode()
    ).hexdigest()
    result = {
        "schema": "item241-root-independent-audit-v1",
        "classification": "EXACT_INDEPENDENT_AUDIT",
        "primes": PRIMES,
        "maximum_prime": max(PRIMES),
        "pairs": pair_count,
        "component_checks": component_count,
        "transition_checks": {
            "even": transition_counts[0],
            "odd": transition_counts[1],
            "isolated_z": transition_counts[2],
        },
        "full_kernel_digest": digest,
        "failures": failures,
        "all_pass": not failures,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
