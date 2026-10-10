> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Conditional reduction of the next J boundary contribution

Status: elementary Schur-complement REUSE after the new A4turn12 candidate.
It gives a smaller next obligation, not its evaluated source-specific answer.
The new complete9M J theorem still needs a DIFFERENT external proof audit.

## 1. Scope and reuse check

The parent recovered the complete A4turn11/A4turn12 finite bordered
inverse identities before this deduction. Scoped current/prior controls
and the pertinent A3/A4 reports contain the older next-digit identities
and the new9M cancellation, but no evaluated physical7 boundary polynomial.
The established symmetric Schur inverse is reused; no general matrix
formula is claimed new. The purpose here is to expose which ACTUAL
boundary precision the next source calculation requires.

For either original core or actual finite J block, write its exact
first/interior/last partition as

    B = [ b00   e^T   a ;
          e     C     w ;
          a     w^T   bTT ],      l_z=(l0,z, lI,z, lT,z).

C is the actual finite interior unit block. The first/interior leading
row e is zero modulo3, the first corner is zero modulo9, and a is a unit.
These are hypotheses supplied at their original scopes by the new report.
No last-middle value is replaced by an ordinary compressed column.

## 2. Exact two-coordinate elimination

Eliminate C, defining

    s=b00-e^T C^-1 e,
    a'=a-e^T C^-1 w,
    c'=bTT-w^T C^-1 w,
    t_z=l0,z-e^T C^-1 lI,z,
    u_z=lT,z-w^T C^-1 lI,z,
    kappa_zv=lI,z^T C^-1 lI,v.

a' is a unit. The new report's X_z=C^-1 lI,z modulo3 satisfies
e^T X_z=0 modulo9, and l0,z=0 modulo9. Since e is divisible by3
and C^-1 lI,z-X_z is divisible by3, both

    s in9Z3,   t_z in9Z3

are paid. They do not require the last-row coupling's next digit.

The exact symmetric inverse gives

    l_z^T B^-1 l_v = kappa_zv
      + [ c't_z t_v-a'(t_z u_v+u_z t_v)+s u_z u_v ]
        / [s c'-(a')^2].

This identity includes every actual last-row and last-column parameter.

## 3. Boundary dependence at the third quadratic digit

Assume the new report's9M quadratic theorem. Since the displayed border
contribution is in9M, kappa_zv is also in9M. Put

    sigma=s/9 modulo3,
    tau_z=t_z/9 modulo3,
    theta_z=u_z/a' modulo3,
    kappa7,zv=kappa_zv/9 modulo3.

The determinant denominator is -(a')^2 modulo9. Since t_z t_v has
valuation at least4, the exact identity reduces to

    (l_z^T B^-1 l_v)/9
       = kappa7,zv + tau_z theta_v + theta_z tau_v
                       -sigma theta_z theta_v   (mod3).

For a single direction this is kappa7,zz+2tau_z theta_z-sigma theta_z^2.
Thus the next physical7 J return needs ONLY the LEADING actual terminal
combination theta, together with the evaluated interior/first-coordinate
coefficients sigma,tau,kappa7. It does not need the terminal coupling
modulo9 or27 merely to write this third-digit return. Its leading actual
value must still be kept unless the coefficient terms are PROVED zero.

The new9M theorem does not set sigma,tau or kappa7 to zero. The report's
(B^-1 l_z)_last in9Z3 is consistent with the same formula but does not
erase the leading theta from this next divided quadratic.

## 4. A useful partial source observation, with its limit

In A4turn12(5.1), the three DISPLAYED terms at B00 have unshifted
indices outside U's degree, except the explicit3 shifted-Q term.
Its reversed index (35P-8chi+7)/2 is125 modulo243, hence a3-unit.
The original N0=25P+2chi has v3(N0)=5. The elementary identity
binom(N0,r)=(N0/r)binom(N0-1,r-1) therefore puts that coefficient in3^5Z3.
Those displayed terms contribute zero even modulo3^6.

However(5.1) is ONLY a modulo9 formula. Its omitted9-weighted source
and finite prefix-inverse terms can contribute to sigma. This partial
observation is not a proof that the COMPLETE B00 or Schur s vanishes
modulo27. Their next exact pole and finite inverse layers are still needed.

All source-specific scalar/bilinear coefficients above remain open, as
does the actual/core next jet transfer. The OTHER physical7 prefix,
rank-b, first4 and new physical5-complement returns are separate. No
complete7 matrix/force or actual primitive saving follows from this note.
