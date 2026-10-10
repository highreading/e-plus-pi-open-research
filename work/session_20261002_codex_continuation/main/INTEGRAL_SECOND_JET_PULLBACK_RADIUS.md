> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A two-integral-jet pullback ceiling

Root author deduction, 2026-10-02. This extends the new first-jet theorem; it has no independent review. No closing condition for the main research has been reached.

## 1. Novelty and literature

Searches of the old sources/work for second-jet radius bounds and integral Pick constraints found no previous completion. The new first-jet theorem in this session supplied the normalized covering and branch proof; the inherited unrestricted radius theorem supplies only the punctured-plane uniformization. A fresh online search for Schwarz-Pick Taylor coefficients and prescribed derivatives located the classical Schur/Nevanlinna framework. The previously opened primary Abate paper, https://pagine.dm.unipi.it/abate/articoli/artric/files/multiJulia.pdf, supplies the hyperbolic difference-quotient context. This is a new application of that standard method to the archive's integral-Hurwitz pullbacks, not a new interpolation principle.

## 2. Statement and extra constant

Retain A,B,a,t,p from INTEGRAL_FIRST_JET_PULLBACK_RADIUS.md. Define

    C=A^2-B^2,
    ell=1-Im(H(z1)H'(z1))/C,
    z1=(1+i)/2,
    R_test=3.475103224038694.                         (1)

Here H=2K/pi uses the elliptic parameter. The new exact certificate proves0<ell<1 and encloses ell=0.68178771180186722....

Theorem. If the endpoint-fixing real-coefficient phi avoids1+i and1-i and has BOTH phi'(0) and phi''(0) integral, its omission radius is strictly less than R_test. In particular the same ceiling holds for the Taylor radius of every integral-Hurwitz polynomial pullback F composed with phi.

The numerical root3.47510322403869350... is a diagnostic for the active k=0 boundary, not the basis of this theorem. The proof below rejects one exact rational radius and uses restriction to a subdisk; it requires no unproved monotonicity of a numerical root equation.

## 3. Lifted second derivative

Let xi be the local inverse of p at0. The curvature-minus-one density satisfies lambda_Omega(w)=2|xi'(w)|/(1-|xi(w)|^2). On the real axis, using the inherited elliptic inverse coordinate,

    lambda_Omega(w)=2/[pi(1+(w-1)^2)Re(H(z)^2)],
    z=(1-i(w-1))/2.

Differentiation at0 gives

    (d/dw)log lambda_Omega(w)|_0=ell,
    xi'(0)=1/a, xi''(0)=ell/a.                     (2)

Thus for j=phi'(0), k=phi''(0), f=xi composed with phi has

    f'(0)=j/a,
    f''(0)=(k+ell j^2)/a.

This is a local calculation at the actual normalized covering. The real-path proof in the preceding note fixes its endpoint branch globally, so f(1)=t for the lifted map.

## 4. Two Schur steps

Suppose phi existed on |z|<R_test. Set R=R_test, s=1/R and h(z)=f(Rz). The first-jet theorem excludes every integer j except1 at this radius: R exceeds the upper bounds for j=0,2, and all other j are smaller by the proved piecewise monotonicity.

Write h(z)=z g(z), and put

    x=R/a,
    y=Rt,
    g(0)=x,
    g(s)=y,
    g'(0)=R^2(k+ell)/(2a).

The next Schur function is

    g1(z)=(g(z)-x)/[z(1-xg(z))].

Its prescribed values are

    g1(0)=B_k=R^2(k+ell)/[2a(1-R^2/a^2)],
    g1(s)=Z=R^2(t-1/a)/(1-tR^2/a).                (3)

All denominators in (3) are positive at this radius by exact interval checks. Since g1 maps the disk into its closure, |B_k|<=1. The new certificate bounds the possible integers as precisely k in{-1,0}; every k>=1 and k<=-2 violates this constant bound.

For each surviving k, Schwarz-Pick requires

    Z <= (B_k+s)/(1+s B_k).                       (4)

The denominator is positive because |B_k|<1 and s<1. The certificate's exact rational outward intervals prove the strict reverse inequality for BOTH k=-1 and k=0. Hence phi cannot exist on this disk. If a phi existed on any larger disk, restriction would give the same contradiction at R_test. This proves the theorem, without extrapolating a finite radius scan.

## 5. Certificate provenance and limitations

SECOND_JET_RADIUS_CERTIFICATE.json gives compact rational outward enclosures for a,t,ell,H', the forced j, the two possible k, Z, and their two upper capacities. The new script uses180 elliptic-series terms, with derivative-tail bound

    sum_(q>N) q(71/100)^(q-1)
      =(71/100)^N[(N+1)-N(71/100)]/(1-71/100)^2,

because each hypergeometric coefficient is at most1. It reuses the established elliptic-series definition-level helper and the new exact Machin-series pi bounds. The older universal theorem is not rerun. All rejection calculations are rational and their rounded outputs are outward enclosures.

This improves the analytic ceiling to3.4751... from the single-jet3.6443... ceiling and the old unrestricted5.2624... ceiling. It does not attain that radius with all integral jets, change any mixed-approximation factorial normalization, or settle the endpoint gcd. Higher jet constraints form the next target; the main e+pi problem remains open.
