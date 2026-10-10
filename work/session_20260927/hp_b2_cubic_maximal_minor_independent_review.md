> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the b=2 cubic maximal-minor gate

Date: 2026-09-27. Reviewer: audit_sources.
Source: hp_b2_cubic_maximal_minor_gate.md.
Status: FULL PASS, including the full prime-power assertions in their
stated range p>2n+4. No correction requested.

## 1. The state and its normalization

I checked the source's identities against the already reviewed b=2
contiguous endpoint reduction, retaining its H,J,K,M derivative
normalization. In particular K is the second derivative of x^kH_k,
not the differently named b=1 scalar J_k/k.

The two adjacent H identities imply



$$
xH_n'''+(n+2-2x)H_n''+2(x-1)H_n'-2nH_n=0.
$$



At x=1, H_n'''=2nh-nv. Differentiating the first adjacent identity
independently gives



$$
H_{n+1}''(1)=(n+1)(nh+u-(n+2)v/2),
$$



which verifies the third transition row. The determinant is
(n+1)^4/2. For odd p>n the product of the transitions through
index n-1 is invertible over Z_p. Since the initial state is
(1,0,0), the current three-state vector is primitive at p.
This is the needed content statement; it does not assert that h
itself is always a unit.

## 2. Actual minors and local ideal equality

I verified the coefficient rows for J_{n+1},K_{n+1} by direct
application of their derivative definitions. For the final row,
M_k has coefficient of H_k'' equal to 2k after use of the ODE.
Thus the two row formulas do not introduce an unaccounted derivative.

The accepted formal identities are



$$
I_{01}=(n+1)D_n,\qquad I_{02}=(n+2)(2n+3)E_n,
$$




$$
uE_n+(nu+(n+2)h)D_n=-(n+1)C_n,
$$




$$
I_{12}|_{h=u=0}=(n+1)(n+2)^2(2n+3)v^2.
$$



All displayed factors that are inverted are units for p>2n+4.
If p divides h and u is a unit, vanishing of D_n gives
v=-(n-1)u modulo p, hence E_n=-(n+1)u^2 is a unit.
If p divides both h and u, state primitivity makes v a unit,
and the final displayed minor is a unit. Thus Omega_n is a unit
whenever h is not.

If h is a unit, subtracting (n+u/h) times the first column leaves
first row (h,0). The third minor is then an integral linear
combination of the first two. This establishes the ideal equality,
not just equality of residue zero sets.

When u is a unit the elimination identity yields
(D_n,E_n)=(D_n,C_n) over Z_p. When u is a nonunit,
D_n=2(n+1)h^2 and C_n=-2(n+2)h^3 modulo p are both units, so
the same assertion holds as an equality of unit ideals. This proves
the exact valuation formula at every depth.

## 3. Actual endpoint factor, including the exception

I rechecked the earlier endpoint-gcd proof that is used here:
after division by z-1 modulo the endpoint depth, the degree-one
quotient exponential coefficient vector is primitive and lies in the
kernel of the exact three-row matrix, up to unit row scalings.
Those column conventions are (constant coefficient, linear
coefficient), so the first row forces b_0=-t b_1 with
t=n+u/h. Primitivity and the unit h force b_1 to be a unit.
Restoring the divided factor yields



$$
B(z)=b_2(z-1)(z-t)\pmod {p^{d_p}}.
$$



The resulting cubic is



$$
P_n(t)=t^3-(2n+2)t^2+(n+2)^2t-2(n+1)(n+2).
$$



Its values at 0 and n prove t and t-n are units. Its value at 1
is -(n^2+4n+1), so the separate exception for B'(1) is necessary.
The source correctly retains it. The polynomial difference identity
also proves the more precise restriction



$$
\min(d_p,v_p B'(1))\le
 \min(d_p,v_p(n^2+4n+1)).
$$



This statement is independent of the choice of lift of t or b_2
modulo p^{d_p}. No converse from the cubic/minor conditions to
actual endpoint cancellation is claimed.

## 4. Separability and what remains open

The discriminant and shift calculation check:



$$
\operatorname{disc}P_n=
 4(n+2)(2n^3-12n^2-35n-22),\qquad
 h^3P_n(n+u/h)=C_n.
$$



If the cubic is separable at p and t is in a root residue,
ordinary simple-root Hensel factorization gives
v_p(P_n(t))=v_p(t-\tau). Combining it with the integral ideal
identity yields the source's exact minimum-depth formula.
It does not bound either depth. The second-derivative
compatibility D_n cannot be discarded.

The result is only a large-prime necessary gate for the primitive
endpoint gcd. At small primes both the transition determinants and
the inherited factorial/moment normalization may be nonunits.
The source makes no unsupported transfer to actual q at such primes.

## 5. Exact verification

I inspected and reran check_hp_b2_cubic_gate.py with the archived
symbolic library. All twelve formal checks pass, including the
transition determinant, both selected minors, homogeneous
elimination, exceptional third minor, first-column determinant,
cubic pencil, shift, discriminant and three evaluations.
The source's symbolic variables are unrestricted; this is not a
degree sample. The proof of the integral ideal equality was
reviewed separately from the symbolic identities.

No new degree or prime scan was performed.
