#!/usr/bin/env python3
"""CRT reconstruction of the Item 243 cross-contiguous relations."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


item222 = load("item243_cross_rec_item222", "item222_j1_phase_resultant_certificate.py")
linear = load("item243_cross_rec_linear", "item237_residual_probe.py")


SPECS = {
    "xu": ("x", "u", 1, 1, 7, 31),
    "yv": ("y", "v", 0, 2, 12, 50),
}
NAMES = ("x", "y", "u", "v")


def vector_mod(residue, key, prime):
    left, right, left_order, right_order, degree, normalization = SPECS[key]
    count = (left_order + right_order + 2) * (degree + 1) + 8
    values = {name: [] for name in NAMES}
    for index in range(count + max(left_order, right_order) + 5):
        _, row = item222.phase_mod(3 * index + residue, prime)
        for name, value in zip(NAMES, row):
            values[name].append(value)
    matrix = []
    for index in range(count):
        row = []
        for name, order in ((left, left_order), (right, right_order)):
            for shift in range(order + 1):
                for power in range(degree + 1):
                    row.append(values[name][index + shift] * pow(index, power, prime) % prime)
        matrix.append(row)
    vector = linear.null_vector(matrix, prime)
    if vector is None or not vector[normalization]:
        raise ArithmeticError((residue, key, prime, "nullspace/normalization"))
    inverse = pow(vector[normalization], -1, prime)
    vector = [value * inverse % prime for value in vector]
    for index in range(count, len(values[left]) - max(left_order, right_order)):
        cursor = 0
        total = 0
        for name, order in ((left, left_order), (right, right_order)):
            for shift in range(order + 1):
                for power in range(degree + 1):
                    total += vector[cursor] * values[name][index + shift] * pow(index, power, prime)
                    cursor += 1
        if total % prime:
            raise AssertionError((residue, key, prime, index))
    return vector


def reconstruct(prime_count):
    primes = linear.reconstruction_primes(prime_count)
    modular = {
        (residue, key): [] for residue in (1, 2) for key in SPECS
    }
    for prime_index, prime in enumerate(primes):
        for key in modular:
            modular[key].append(vector_mod(*key, prime))
        print(json.dumps({"prime_index": prime_index + 1, "prime": prime}), flush=True)
    exact = {}
    for key, vectors in modular.items():
        answer = []
        for coordinate in range(len(vectors[0])):
            value = vectors[0][coordinate]
            modulus = primes[0]
            for prime_index in range(1, len(primes)):
                value, modulus = linear.crt_pair(
                    value,
                    modulus,
                    vectors[prime_index][coordinate],
                    primes[prime_index],
                )
            rational = linear.rational_reconstruct(value, modulus)
            if rational is None:
                raise ArithmeticError((key, coordinate, "reconstruction"))
            answer.append([rational.numerator, rational.denominator])
        exact[f"r{key[0]}_{key[1]}"] = answer
    return {"prime_count": prime_count, "primes": primes, "relations": exact}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-count", type=int, default=40)
    parser.add_argument(
        "--output", type=Path, default=HERE / "item243_cross_reconstruct.json"
    )
    args = parser.parse_args()
    result = reconstruct(args.prime_count)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(args.output)}))


if __name__ == "__main__":
    main()
