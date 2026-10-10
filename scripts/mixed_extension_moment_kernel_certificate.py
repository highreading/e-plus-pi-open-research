#!/usr/bin/env python3
"""Exact and high-precision audit of the mixed moment kernel.

The exact part verifies the scalar/adjoint factorization, the equivalence
between rational adjoint certificates and split cross extensions, a
zero-moment split example, Hermite reduction for D-1, and polynomial
normal forms through a fixed degree.  The PSLQ part is explicitly only a
diagnostic; it is not used as a proof of independence.
"""

import json
import math

import mpmath as mp
import sympy as sp


z = sp.symbols("z")
q = -4 / (1 + z**2)
y = -4 * sp.atan(z)
w = sp.exp(-z) * y
h = sp.simplify(sp.diff(q, z) / q - 1)


def D_minus_one(f):
    return sp.simplify(sp.diff(f, z) - f)


def D_plus_h(f):
    return sp.simplify(sp.diff(f, z) + h * f)


def scalar_L(f):
    return sp.simplify(
        (sp.diff(sp.diff(f, z) + f, z)
         - h * (sp.diff(f, z) + f))
    )


def scalar_L_star(f):
    return sp.simplify(D_minus_one(D_plus_h(f)))


def polynomial_D_minus_one_inverse(poly):
    """Unique polynomial A with A'-A=poly."""
    p = sp.Poly(sp.expand(poly), z)
    degree = p.degree()
    if degree < 0:
        return sp.Integer(0)
    coefficients = sp.symbols(f"u0:{degree + 1}")
    candidate = sum(coefficients[j] * z**j for j in range(degree + 1))
    equations = sp.Poly(
        sp.expand(D_minus_one(candidate) - poly), z
    ).all_coeffs()
    solution = sp.solve(equations, coefficients, dict=True)[0]
    return sp.expand(candidate.subs(solution))


# A rational adjoint primitive with vanishing endpoint concomitant.
phi = z**2 * (1 - z) ** 2
A_phi = sp.factor(D_plus_h(phi))
B_phi = sp.factor(-q * phi)
r_phi = sp.factor(scalar_L_star(phi))
r_phi_expected = (
    z**8
    - 8 * z**7
    + 17 * z**6
    - 24 * z**5
    + 37 * z**4
    - 24 * z**3
    + 23 * z**2
    - 16 * z
    + 2
) / (z**2 + 1) ** 2

# Endpoint formula for a split r=L^*phi:
# K_r(1)=-pi*A(1)-q(1)*phi(1)+e*q(0)*phi(0).
split_boundary_phi = sp.simplify(
    -sp.pi * A_phi.subs(z, 1)
    - q.subs(z, 1) * phi.subs(z, 1)
    + sp.E * q.subs(z, 0) * phi.subs(z, 0)
)

# A quadratic Hermite interpolant realizes an arbitrary element of
# Qbar + Qbar*e + Qbar*pi as a split endpoint concomitant.
lambda_0, lambda_e, lambda_pi = sp.symbols(
    "lambda_0 lambda_e lambda_pi"
)
phi_boundary = sp.expand(
    -lambda_e / 4
    + (lambda_pi + lambda_e / 2) * z
    + (lambda_0 / 2 - lambda_pi - lambda_e / 4) * z**2
)
A_boundary = D_plus_h(phi_boundary)
split_boundary_general = sp.simplify(
    -sp.pi * A_boundary.subs(z, 1)
    - q.subs(z, 1) * phi_boundary.subs(z, 1)
    + sp.E * q.subs(z, 0) * phi_boundary.subs(z, 0)
)
split_boundary_target = lambda_0 + lambda_e * sp.E + lambda_pi * sp.pi

# Polynomial normal form audit.  For P=A'-A, the cross class is split
# iff A is divisible by z^2+1.  Modulo split classes A reduces to a*z+b,
# hence P reduces to -a*z+(a-b).
polynomial_cutoff = 12
polynomial_normal_forms = []
polynomial_checks = True
for n in range(polynomial_cutoff + 1):
    P = z**n
    A = -math.factorial(n) * sum(
        z**j / sp.factorial(j) for j in range(n + 1)
    )
    A = sp.expand(A)
    remainder = sp.rem(A, z**2 + 1, domain=sp.QQ)
    quotient = sp.cancel((A - remainder) / (z**2 + 1))
    P_normal = sp.expand(D_minus_one(remainder))

    # The split difference has A_split=(z^2+1)*quotient.  Construct
    # B_split with B'-B=-q*A_split=4*quotient and phi_split=-B/q.
    B_split = polynomial_D_minus_one_inverse(4 * quotient)
    phi_split = sp.factor(-B_split / q)
    split_difference = sp.simplify(P - P_normal)

    checks_n = [
        sp.simplify(D_minus_one(A) - P) == 0,
        sp.simplify(A - ((z**2 + 1) * quotient + remainder)) == 0,
        sp.degree(remainder, z) <= 1,
        sp.simplify(D_minus_one(B_split) + q * (A - remainder)) == 0,
        sp.simplify(scalar_L_star(phi_split) - split_difference) == 0,
    ]
    polynomial_checks = polynomial_checks and all(checks_n)
    polynomial_normal_forms.append(
        {
            "n": n,
            "A_remainder_mod_z2_plus_1": str(sp.expand(remainder)),
            "P_normal": str(P_normal),
        }
    )

# D-1 Hermite obstruction.  At a pole alpha with principal coefficients
# r_{-j}, the surviving simple-pole coefficient is
# sum_j (-1)^(j-1) r_{-j}/(j-1)!.
alpha = sp.symbols("alpha")
principal_coefficients = sp.symbols("c1:6")
hermite_obstruction_order_5 = sp.simplify(
    sum(
        (-1) ** (j - 1)
        * principal_coefficients[j - 1]
        / sp.factorial(j - 1)
        for j in range(1, 6)
    )
)

# For the adjoint example, the D-1 obstruction vanishes separately at
# i and -i, consistent with r_phi=A_phi'-A_phi.
u = sp.symbols("u")


def local_D_minus_one_obstruction(function, pole, order):
    series = sp.series(function.subs(z, pole + u), u, 0, 1).removeO()
    value = sp.Integer(0)
    for j in range(1, order + 1):
        coefficient = sp.expand(series).coeff(u, -j)
        value += (-1) ** (j - 1) * coefficient / sp.factorial(j - 1)
    return sp.simplify(value)


obstruction_phi_i = local_D_minus_one_obstruction(r_phi, sp.I, 2)
obstruction_phi_minus_i = local_D_minus_one_obstruction(r_phi, -sp.I, 2)
simple_pole_obstruction_at_2 = local_D_minus_one_obstruction(
    1 / (z - 2), sp.Integer(2), 1
)

# High-precision diagnostics for the two-dimensional polynomial core and
# a finite real simple-pole family.  These are intentionally not proofs.
mp.mp.dps = 220


def y_mp(t):
    return -4 * mp.atan(t)


def K_mp(kernel):
    return mp.e * mp.quad(
        lambda t_: mp.exp(-t_) * y_mp(t_) * kernel(t_), [0, 1]
    )


kappa_0 = K_mp(lambda t_: -1)       # A=1, r=-1
kappa_1 = K_mp(lambda t_: 1 - t_)   # A=z, r=1-z
moment_one = K_mp(lambda t_: 1)
moment_t = K_mp(lambda t_: t_)
weighted_mean = moment_t / moment_one

polynomial_pslq_values = [mp.mpf(1), mp.e, mp.pi, kappa_0, kappa_1]
polynomial_pslq = mp.pslq(
    polynomial_pslq_values,
    # In dimension five a generic size-10^50 relation can already have
    # residual near 10^-200.  We therefore demand 205 digits rather than
    # reporting a generic finite-precision lattice coincidence.
    tol=mp.mpf("1e-205"),
    maxcoeff=10**50,
    maxsteps=10000,
)

real_poles = [-3, -2, -1, 2, 3, 4]
simple_pole_values = [
    K_mp(lambda t_, pole_=pole: 1 / (t_ - pole_))
    for pole in real_poles
]
simple_pole_pslq = mp.pslq(
    [mp.mpf(1), mp.e, mp.pi] + simple_pole_values,
    # Nine coordinates make generic short relations much easier to find;
    # the smaller coefficient cap keeps this a meaningful diagnostic at
    # the working precision.
    tol=mp.mpf("1e-205"),
    maxcoeff=10**20,
    maxsteps=20000,
)

checks = {
    "w_satisfies_factored_scalar_operator": scalar_L(w) == 0,
    "adjoint_factorization_matches_expanded_form": (
        sp.simplify(
            scalar_L_star(phi)
            - (
                sp.diff(phi, z, 2)
                - (2 - sp.diff(q, z) / q) * sp.diff(phi, z)
                + (
                    1
                    - sp.diff(q, z) / q
                    - sp.diff(2 - sp.diff(q, z) / q, z)
                )
                * phi
            )
        )
        == 0
    ),
    "adjoint_example_r_formula": sp.simplify(r_phi - r_phi_expected) == 0,
    "adjoint_example_first_split_equation": (
        sp.simplify(D_minus_one(A_phi) - r_phi) == 0
    ),
    "adjoint_example_second_split_equation": (
        sp.simplify(D_minus_one(B_phi) + q * A_phi) == 0
    ),
    "adjoint_example_endpoint_period_zero": split_boundary_phi == 0,
    "quadratic_boundary_map_is_onto_1_e_pi_span": (
        sp.simplify(split_boundary_general - split_boundary_target) == 0
    ),
    "polynomial_normal_forms_through_cutoff": polynomial_checks,
    "adjoint_example_D_minus_one_obstruction_at_i": obstruction_phi_i == 0,
    "adjoint_example_D_minus_one_obstruction_at_minus_i": (
        obstruction_phi_minus_i == 0
    ),
    "simple_pole_at_2_is_not_D_minus_one_exact": (
        simple_pole_obstruction_at_2 == 1
    ),
}

assert all(checks.values())

digits = 110
result = {
    "certificate": "mixed_extension_moment_kernel",
    "sympy_version": sp.__version__,
    "mpmath_version": mp.__version__,
    "checks": checks,
    "exact_data": {
        "q": str(sp.factor(q)),
        "h=q'/q-1": str(sp.factor(h)),
        "scalar_L_factorization": "(D-(q'/q-1))*(D+1)",
        "scalar_L_star_factorization": "(D-1)*(D+(q'/q-1))",
        "phi": str(phi),
        "A_phi": str(A_phi),
        "B_phi": str(B_phi),
        "r_phi": str(r_phi),
        "split_boundary_phi": str(split_boundary_phi),
        "general_boundary_interpolant": str(phi_boundary),
        "general_boundary_value": str(split_boundary_general),
        "D_minus_one_hermite_obstruction_order_5": str(
            hermite_obstruction_order_5
        ),
        "polynomial_normal_form_cutoff": polynomial_cutoff,
        "polynomial_normal_forms": polynomial_normal_forms,
        "polynomial_core_basis": ["r=-1 (A=1)", "r=1-z (A=z)"],
        "single_pole_nonvanishing": (
            "K_{1/(z-alpha)} is a nonzero Stieltjes transform for "
            "alpha outside [0,1]"
        ),
    },
    "diagnostics_not_proofs": {
        "precision_decimal_digits": mp.mp.dps,
        "kappa_0": mp.nstr(kappa_0, digits),
        "kappa_1": mp.nstr(kappa_1, digits),
        "moment_r_1": mp.nstr(moment_one, digits),
        "moment_r_z": mp.nstr(moment_t, digits),
        "weighted_mean_moment_z_over_moment_1": mp.nstr(
            weighted_mean, digits
        ),
        "polynomial_core_pslq_vector": ["1", "e", "pi", "kappa_0", "kappa_1"],
        "polynomial_core_pslq_maxcoeff": "1e50",
        "polynomial_core_pslq_result": polynomial_pslq,
        "real_simple_poles": real_poles,
        "real_simple_pole_values": [
            mp.nstr(value, digits) for value in simple_pole_values
        ],
        "simple_pole_pslq_vector": (
            ["1", "e", "pi"]
            + [f"K_1/(z-({pole}))" for pole in real_poles]
        ),
        "simple_pole_pslq_maxcoeff": "1e20",
        "simple_pole_pslq_result": simple_pole_pslq,
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
