#!/usr/bin/env python3
"""Discover exact univariate recurrences for the four Item 222 phase periods."""

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


item222 = load("item243_item222", "item222_j1_phase_resultant_certificate.py")
probe = load("item243_item237", "item237_residual_probe.py")


SPECS = {
    "x": (4, 15, 79),
    "y": (3, 14, 59),
    "u": (5, 15, 94),
    "v": (3, 16, 67),
}


def modular_vectors(prime, count=135):
    answer = {}
    for residue in (1, 2):
        values = {name: [] for name in SPECS}
        for index in range(count):
            _, components = item222.phase_mod(3 * index + residue, prime)
            for name, value in zip(values, components):
                values[name].append(value)
        for name, (order, degree, normalization) in SPECS.items():
            columns = (order + 1) * (degree + 1)
            matrix = probe.recurrence_matrix(
                values[name], order, degree, columns + 4, prime
            )
            vector = probe.null_vector(matrix, prime)
            if vector is None or not probe.verify(
                vector, values[name], order, degree, prime
            ):
                raise AssertionError((prime, residue, name, "recurrence"))
            if not vector[normalization]:
                raise AssertionError((prime, residue, name, "normalization"))
            inverse = pow(vector[normalization], -1, prime)
            answer[(residue, name)] = [
                value * inverse % prime for value in vector
            ]
    return answer


def reconstruct(prime_count):
    primes = probe.reconstruction_primes(prime_count)
    vectors = {(residue, name): [] for residue in (1, 2) for name in SPECS}
    for index, prime in enumerate(primes):
        current = modular_vectors(prime)
        for key, vector in current.items():
            vectors[key].append(vector)
        print(json.dumps({"prime_index": index + 1, "prime": prime}), flush=True)
    result = {}
    for key, modular in vectors.items():
        exact = []
        for coordinate in range(len(modular[0])):
            value = modular[0][coordinate]
            modulus = primes[0]
            for prime_index in range(1, len(primes)):
                value, modulus = probe.crt_pair(
                    value,
                    modulus,
                    modular[prime_index][coordinate],
                    primes[prime_index],
                )
            rational = probe.rational_reconstruct(value, modulus)
            if rational is None:
                raise ArithmeticError((key, coordinate, "reconstruction"))
            exact.append([rational.numerator, rational.denominator])
        result[f"r{key[0]}_{key[1]}"] = exact
    return {"prime_count": prime_count, "primes": primes, "recurrences": result}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-count", type=int, default=60)
    parser.add_argument(
        "--output", type=Path, default=HERE / "item243_univariate_recurrence_probe.json"
    )
    args = parser.parse_args()
    result = reconstruct(args.prime_count)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(args.output), "recurrences": len(result["recurrences"])}))


if __name__ == "__main__":
    main()
