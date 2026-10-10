> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Adjacent b=2 maximal-minor contents have no common large prime

Date: 2026-09-27. Author: audit_results.
Status: FULL PASS by root; see two_local_lemmas_independent_root_review.md.
Dependency: hp_b2_cubic_maximal_minor_gate.md.
No degree or prime scan.

**Theorem.** For n>=2 and every p>2n+6,


$$
\boxed{\min(v_p\Omega_n,v_p\Omega_{n+1})=0.}          \tag{1}
$$


Here Omega is exactly the content of the 3-by-2 matrix in the
previous independently reviewed b=2 endpoint-gcd gate.
Consequently the endpoint gcds of the primitive full integral
triples at n and n+1 cannot share such a prime. This does not
exclude isolated large-prime defects or bound either individual
depth.

Suppose p divides Omega_n. The cubic gate makes h=H_n(1) and
u=H'_n(1) units. Put z=u/h and w=H''_n(1)/h. Modulo p,


$$
f_n(z)=z^3+(n-2)z^2+4z-2(n+2)=0,\qquad
 w=2(n+1)/z-2-(n-1)z.                              \tag{2}
$$


The exact state shift T_n, evaluated under (2), gives


$$
h_1/h=(n+1)(z^2-2z+2)/(2z),
$$




$$
u_1/h=-(n+1)^2(z^2-2)/(2z),\quad
 v_1/h=(n+1)^2(nz^2-2n+4z-4)/(2z).                 \tag{3}
$$


The subscript 1 denotes the actual state at n+1. Evaluate its
quadratic obstruction D_(n+1) using (3). Exactly,


$$
D_{n+1}/h^2=\frac{(n+1)^2}{2z^2}F_n(z)
 \quad\hbox{modulo the relation }D_n=0,
$$




$$
F_n(z)=((2n+3)z-n-2)f_n(z)-g_n(z),
\quad
 g_n(z)=(n^2+4n+2)z^2-(6n+4)z-2n^2.                \tag{4}
$$


All denominators in (2)-(4) are units at the prime in (1).
If p also divides Omega_(n+1), its first minor forces
D_(n+1)=0 modulo p; thus both f_n and g_n vanish at z.

This is impossible by the following explicit integral Bezout identity.
Put


$$
A_n(z)=-(3n^3+14n^2+14n+4)z-4n^3+8n+4,
$$




$$
B_n(z)=(3n+2)z^2+(3n^2-2)z+4n^2+12n+8.
$$


Then a direct polynomial multiplication gives


$$
\boxed{A_n(z)f_n(z)+B_n(z)g_n(z)
                        =-8(n+1)^2(n+2).}           \tag{5}
$$


Its right side is a p-unit. This proves (1), hence excludes every
positive common valuation, not only a truncated computed depth.
For reference the exact resultant is


$$
\operatorname{Res}_z(f_n,g_n)=-32(n+1)^4(n+2)^2.
$$



The actual endpoint consequence uses the prior bound
v_p gcd(A_k(1),B_k(1))<=v_p Omega_k at k=n,n+1.
The stronger of its two required cutoffs is p>2n+6, retained in
(1). No inference at smaller primes is made from the formal
Bezout identity, and no bound on the reduced denominator q is
claimed.

The identities (3)-(5) and resultant were checked symbolically with
formal n,z; the mathematical proof is the displayed elimination.
The saved checker is check_hp_b2_adjacent_content.py and its passing
output is hp_b2_adjacent_content_symbolic_checks.json.

## All-index nonvanishing of the exact content carrier

The same cubic also proves


$$
\boxed{\Omega_n\ne0\quad\text{for every }n\ge2.}      \tag{6}
$$


Indeed if all three minors vanished over Q, the primitive-state
and row calculations in the preceding note, now over Q, would
force h and u both nonzero. Thus z=u/h would be a rational root
of the monic integer cubic f_n and hence an integer. Rearranging
f_n(z)=0 gives


$$
n=2-z+\frac{8-6z}{z^2-2}.
$$


Consequently z^2-2 divides 8-6z. Multiplying by 8+6z and reducing
z^2 modulo z^2-2 shows that z^2-2 divides 8.
The only possible integer z are 0,1,-1,2,-2. Their corresponding
n values are respectively -2,-1,-11,-2,14. Thus for n>=2 the
only candidate is n=14,z=-2.

The already proved all-index odd-prime congruence for differentiated
H values, from ../session_20260913/hp_special_gcd_unit_lift.md,
equation (7) and its residue consequence, gives
H_14(1)=H_0(1)=1 mod7 and H'_14(1)=H'_0(1)=0 mod7.
This contradicts u=-2h. No value of an index-14 approximant or
coefficient solve is required. It excludes the last candidate and
proves (6).

The previous endpoint-gcd inequality therefore has a nonzero
integer carrier at every index in its stated degree range, although
no useful uniform size or individual prime-depth bound follows
from this nonvanishing alone.
