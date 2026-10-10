> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the odd Hardy/reference framework

Date: 2026-09-13. Reviewer: audit_computations.

**FULL PASS.** All six sections of
`raw_odd_hardy_reference_and_reversal_framework.md` pass. No correction
is required. This review uses the previously accepted circular-binomial
orthogonality and odd operator/inverse theorems. It does not depend on
the new odd saddle asymptotics or on the nonzero saddle amplitudes.

## 1. Reference degree, norm and finite-moment identity

Parity reduces the w_+ metric on degree 2m+1 to two copies of the
degree-m circular space with parameter a=m+1. The monic polynomial of
odd top degree is therefore exactly



$$
\Psi=(-1)^m z\Phi_m^{[m+1]}(-z^2),\qquad
 F=\Phi_m^{[m+1]*}(-z^2).
$$



The leading sign makes Psi monic, while F has constant one. The positive
norm is m!(3m+2)!/((2m+1)!)^2=1/c_m; Haar pushforward under -z^2
introduces no factor. Degree-n reversal gives Psi^*=F even though F
has degree n-1. All roots of Psi are strictly inside the circle, and
all roots of F strictly outside, so these polynomials are coprime.

For dnu=(1/c_m)|F|^-2 dtheta/(2pi), the identity
Psi=z^n conjugate(F) on the unit circle gives



$$
\int\Psi z^{-j}d\nu
 =\frac1{c_m}\int z^{n-j}/F\,\frac{d\theta}{2\pi}.
$$



This vanishes for 0<=j<n and equals 1/c_m for j=n. Under the original
measure the same identities follow from monic orthogonality and its
norm. The conjugate equations also coincide. After multiplying the
resulting Laurent span by z^n, its span is Psi P_n+F P_n.

To verify its dimension in the exceptional degree configuration, an
intersection element must be Psi F h. The multiplier of F is Psi h
and must have degree at most n, forcing h constant. The nonzero product
Psi F is allowed because deg F=n-1<=n. The intersection is exactly
one-dimensional; hence the sum has dimension 2n+1 and fills P_(2n).
The moments at every exponent -n,...,n therefore agree. This proves
the exact identity



$$
\|p/F\|_{H^2}^2=c_m\|p\|_{w_+}^2\quad(\deg p\le n).
$$



The fact that F is one degree shorter does not lose a moment.

## 2. Actual inverse normalization and both Hardy bounds

From u=A^-1e0 and the positive metric normalization,
$\|u\|_{w_+}\le K_A\sqrt{c_m}$. The accepted odd scalar identity is
u0=c_m/s_m, including its sign. Thus



$$
\left\|\frac{u}{u_0F}\right\|_{H^2}^2
 \le K_A^2|s_m|^2.
$$



The degree-n reversal u^* has the same circle modulus as u, so the
same estimate applies to u^*/(u0 F). The known nonzero scalar limit and
finitely many finite initial values give S=sup_m|s_m|<infinity. No lower
bound on s_m is used in this estimate. Invertibility and u0!=0 have
already been established independently. The constant is K_A S; the
even positive-sector constant is not silently reused.

Analyticity of 1/F and Hardy evaluation then give the stated disk bounds
and Cauchy derivative bounds. R(0)=1, while Rtilde(0) is the original
top-to-bottom coefficient ratio and need not equal one.

## 3. Reversal phase and the two coordinate channels

The exact identity Rtilde(1/z)=u(z)/(u0 Psi(z)) retains the extra z in
Psi. Under the Cayley map, the constant coefficient is the plus-i
functional in component one, and the odd top coefficient is the minus-i
functional in component two. Both finite scaling factors are 2^-m.
Accordingly the finite exterior denominator has g_m z times the
minus-i reference pairing. There is no missing scalar norm or channel.

With x=i^m x^o, k=(-i)^m k^o and ell=(-i)^m ell^o, the numerator pairing
ell^*x is (-1)^m times its unphased value, whereas ell^*k is unchanged.
This proves the alternating factor in the target's equation (11).
At z=-phi both the explicit negative z and the possibly negative
g_m=1/s_m must remain. The interior reference and evaluation carry
matching phases, so it has no such alternation. None of this establishes
a nonzero limiting pairing without the separate multiplier calculation.

## 4. Alternative absolute weight and frozen control

The optional a=m+1/2 reference has its own norm and reversal. The accepted
comparison w_- to w_+ on the actual two degree-m components yields
$\|p\|_{w_{abs}}^2\le(\sqrt5/2)\|p\|_{w_+}^2$ by Cauchy–Schwarz.
Since w_+<=2w_abs, the inverse evaluation norm satisfies c_abs<=2c_m.
Combining these with the exact finite-moment identity gives precisely
the target's squared Hardy bound sqrt(5) K_A^2 S^2. The literal absolute
weight is therefore available, but it is not identified with the metric
used by the accepted odd operator.

The frozen n=1 values u=-2+3z, c0=1/2, s0=-1/4, F=1 and Psi=z give
R=1-3z/2 and Rtilde=z-3/2 exactly. They check the degree-n reversal,
the sign of u0 and the exterior z factor. No new finite degree is used.
