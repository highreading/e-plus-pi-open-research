from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ARCHIVE = Path(__file__).resolve().parents[1]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


digits = load("item173_digits", ARCHIVE / "scripts" / "item163_deeper_digits_certificate.py")
extended = load(
    "item173_extended", ARCHIVE / "scripts" / "lifted_endpoint_hasse_extended_certificate.py"
)
second = load(
    "item173_second", ARCHIVE / "scripts" / "item164_third_layer_certificate.py"
)


def pow_poly(poly: list[int], exponent: int, p: int) -> list[int]:
    out = [1]
    base = poly[:]
    while exponent:
        if exponent & 1:
            out = second.conv(out, base, p)
        exponent >>= 1
        if exponent:
            base = second.conv(base, base, p)
    return out


def rank_zero_second(m: int, p: int) -> dict[str, object]:
    b = (4 * m + 1) // p
    j = b // 2
    t = (4 * m + 1) % p
    s = (p - t) // 2
    r = (p - 6 * s - 3) // 2
    a = 3 * j + 1
    c = 2 * j + 1
    u = [0, 1, -1]
    q = [1, 1, 1, 1]
    up = pow_poly(u, r, p)
    records = []
    for shift in (0, 1):
        p_poly = second.conv(up, pow_poly(q, 2 * s - shift, p), p)
        t_poly = second.primitive(p_poly, p)
        w = second.add(
            second.scale(second.conv([1, -2], q, p), a, p),
            second.scale(second.conv([1, 2, 3], u, p), -c, p),
            p,
        )
        n_poly = second.conv(t_poly, w, p)
        maximum_n = (len(n_poly) - 1 + 4 * (p - 1)) // p
        h = [0] * (maximum_n + 1)
        for n in range(maximum_n + 1):
            h[n] = sum(
                n_poly[index]
                for z in range(p)
                if 0 <= (index := p * n - 4 * z) < len(n_poly)
            ) % p
        h = second.trim(h)
        if h[0] or len(h) > 5:
            raise AssertionError((m, p, j, s, h))
        records.append({
            "H": h,
            "T_at_1": sum(t_poly) % p,
            "N_at_1": sum(n_poly) % p,
        })

    numerator_exponent = a - 1
    denominator_exponent = c + 1
    if denominator_exponent >= p:
        raise ValueError("second transform crosses a p-pole band")

    def coords(h: list[int]) -> tuple[int, int, int]:
        degree = denominator_exponent - 1
        minus_base = second.base_local_coefficients(
            numerator_exponent, denominator_exponent, "minus_one", p
        )
        i_base = second.base_local_coefficients(
            numerator_exponent, denominator_exponent, "i", p
        )
        minus_h = second.gaussian_shift(h, (-1 % p, 0), p)
        i_h = second.gaussian_shift(h, (0, 1), p)
        c_minus = second.multiply_truncated(minus_base, minus_h, degree, p)
        c_i = second.multiply_truncated(i_base, i_h, degree, p)
        residue_minus = c_minus[degree][0]
        residue_i = c_i[degree]
        l_value = (4 * residue_minus + 4 * residue_i[0]) % p
        e_value = (-4 * residue_i[1]) % p
        roots_and_coefficients = [
            ((-1 % p, 0), c_minus),
            ((0, 1), c_i),
            ((0, -1 % p), [(x, -y % p) for x, y in c_i]),
        ]
        total = (0, 0)
        for n in range(1, denominator_exponent):
            contribution = (0, 0)
            for root, coefficients in roots_and_coefficients:
                term = extended.base.gmul(
                    coefficients[degree - n], extended.base.endpoint_factor(root, n, p), p
                )
                contribution = extended.base.gadd(contribution, term, p)
            contribution = extended.base.gscale(contribution, pow(n, -1, p), p)
            total = extended.base.gadd(total, contribution, p)
        if total[1]:
            raise AssertionError((m, p, total))
        return total[0], l_value, e_value

    coords0, coords1 = coords(records[0]["H"]), coords(records[1]["H"])
    r0, l0, e0 = coords0
    r1, l1, e1 = coords1
    return {
        "j": j,
        "s": s,
        "H": [record["H"] for record in records],
        "endpoint_identity": [
            {
                "H_at_1": sum(record["H"]) % p,
                "N_at_1": record["N_at_1"],
                "minus_4aT_at_1": (-4 * a * record["T_at_1"]) % p,
            }
            for record in records
        ],
        "coordinates": [coords0, coords1],
        "A0_raw": (l1 * r0 - l0 * r1) % p,
        "B0_raw": (l1 * e0 - l0 * e1) % p,
    }


def row(m: int, p: int, precision: int = 6) -> dict[str, object]:
    modulus = p**precision
    l0, x0, e0, _ = digits.coordinates_mod(extended, m, 4 * m + 1, p, precision)
    l1, x1, e1, _ = digits.coordinates_mod(extended, m, 4 * m + 2, p, precision)
    determinant_a = (l1 * x0 - l0 * x1) % modulus
    determinant_b = (l1 * e0 - l0 * e1) % modulus
    a = (6 * m) // p
    b = (4 * m + 1) // p
    t = (4 * m + 1) % p
    return {
        "m": m,
        "p": p,
        "j": b // 2,
        "s": (p - t) // 2,
        "kappa": 2 * a - 3 * b,
        "A": digits.p_digits(determinant_a // (p**2), p, precision - 2),
        "B": digits.p_digits(determinant_b // (p**2), p, precision - 2),
        "coordinate_digits": {
            "L0_over_p": digits.p_digits(l0 // p, p, 3),
            "L1_over_p": digits.p_digits(l1 // p, p, 3),
            "X0_over_p": digits.p_digits(x0 // p, p, 3),
            "X1_over_p": digits.p_digits(x1 // p, p, 3),
            "E0_over_p": digits.p_digits(e0 // p, p, 3),
            "E1_over_p": digits.p_digits(e1 // p, p, 3),
        },
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int, nargs="*")
    parser.add_argument("--tail-bound", type=int)
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    out = []
    if args.tail_bound:
        def prime(n: int) -> bool:
            return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))

        for p in range(7, args.tail_bound + 1, 2):
            if not prime(p):
                continue
            for j in range(1, (p - 1) // 2 + 1):
                if 3 * j + 1 < p or 2 * j + 2 > p:
                    continue
                for s in range(1, (p - 3) // 6 + 1):
                    numerator = (2 * j + 1) * p - 2 * s - 1
                    if numerator % 4:
                        continue
                    m = numerator // 4
                    out.append(row(m, p, precision=4))
    else:
        for p in args.p:
            m = (p * p - 5) // 4
            out.append(row(m, p))
    if args.summary:
        print(json.dumps({
            "rows": len(out),
            "A0_nonzero": sum(bool(r["A"][0]) for r in out),
            "B0_nonzero": sum(bool(r["B"][0]) for r in out),
            "A1_zero": [
                {key: r[key] for key in ("m", "p", "j", "s")}
                for r in out if r["A"][1] == 0
            ],
            "A1_residue_counts": {
                str(a): sum(r["A"][1] == a for r in out)
                for a in sorted({r["A"][1] for r in out})
            },
        }, indent=2, sort_keys=True))
    else:
        print(json.dumps(out, indent=2, sort_keys=True))
