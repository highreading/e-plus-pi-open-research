> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact finite pole-pair reduction for the complete ternary core

Coordinator derivation, October 6, 2026. This is an auxiliary algebraic reduction, not a determinant valuation or irrationality proof.

## Overlap and scope

A1's preceding turn13 section8.3 already notes possible cancellation of the finest pole pair modulo3. That observation is reused. The local packet search did not locate the following exact whole-layer identity with its explicit finite-cutoff condition. The primary literature searches did not locate this specialized statement; this is not an exhaustive novelty guarantee. Reciprocal-weight subtraction is elementary. The purpose is to supply a complete precision reduction for the present core, not to claim a new general p-adic method.

Let h>=3, H=3^(h-1), n=H-D+2, and Rmax=2n-2. For 0<=ell<=h, put delta_ell=3^(h-ell) and r_c=(c delta_ell-1)/2. Define the actual finite layer

P_ell(T)=3^ell sum_{c>=1 odd, 3 not dividing c, r_c<=Rmax} T[r_c]/c.

Coefficients at negative indices are zero. The complete pole functional is sum_ell P_ell, with no layer beyond h and no coordinate beyond Rmax.

Take F in Z3[y], with deg F=B>=0 and H+B<=Rmax. For ell>=2, let a_ell=2*3^(ell-1). The map c -> c+a_ell preserves positive odd 3-adic units, and r_(c+a_ell)=r_c+H.

## Exact identity

The finite degree bound makes every nonzero coefficient of F at r_c occur with its shifted high-copy coefficient inside the same original cutoff. Reindexing only those nonzero coefficients gives

P_ell((y^H-1)F)
=3^ell sum_c ((c+a_ell)^(-1)-c^(-1)) F[r_c]
=-2*3^(2ell-1) sum_c F[r_c]/(c(c+a_ell)).

The last sum has r_c in [0,B]; all denominators are units. Hence

P_ell((y^H-1)F) belongs to 3^(2ell-1) Z3.

This identity requires ell>=2. At ell1 the shift is2 and need not preserve the exclusion of multiples of3; that layer must be kept separately. At ell0 the required shift is not an integer. Neither low layer is silently removed.

For reduction modulo3^K, layers with 2ell-1>=K contribute zero to this paired part. Thus only ell2 through floor(K/2) need remain in the paired part. At K27, these are ell2..13; the entire correction below is still present.

## The binomial correction is retained

Write (y-1)^H=(y^H-1)+Delta_H. For 1<=r<H,

Delta_H[r]=(-1)^(H-r) binom(H,r),
v3(Delta_H[r])=h-1-v3(r).

The valuation identity follows from binom(H,r)=H/r binom(H-1,r-1), and binom(H-1,r-1) is a3-adic unit. Its mod3 coefficients are supplied by (1+z)^(H-1)=(1+z^H)/(1+z) modulo3.

In a layer ell<K, Delta_H only needs precision q=K-ell. Its possible nonzero coefficients modulo3^q occur at r divisible by 3^max(0,h-q). The interior coefficient range remains 1..H-1. This is a sparse index restriction, not a feasible-state theorem: at fixed q it can still have 3^(q-1)-1 slots.

For ell>=K the entire original integral pole layer is zero modulo3^K.

## Application to the corrected core representatives

For phi_i=x^D psi_i, x=y-1, and Q_c=(y+1)x^(H-D)(beta+3y), set

F_ij=x^D(beta+3y)psi_i psi_j.

If deg phi_i,deg phi_j<=m-1, m=(n-1)/2, then

deg F_ij<=2m-D-1=H-2D.

Consequently H+deg F_ij<=2H-2D<Rmax=2H-2D+2. The exact finite pairing is admissible on every layer ell>=2.

The complete core pairing, before any normalization, is

G_c(phi_i,phi_j)
=-(3^h/4) f((y+1)(y-1)^H F_ij)
+P_0((y^H-1)F_ij)+P_1((y^H-1)F_ij)
-2 sum_{ell=2}^h 3^(2ell-1) sum_c F_ij[r_c]/(c(c+a_ell))
+sum_{ell=0}^h P_ell(Delta_H F_ij).

Here f(y^r)=(2r)!, the original finite Rmax cutoff is used everywhere, and the whole sum is evaluated before division. The factorial term is integral times3^h, so it can be omitted modulo3^K only after h>=K is checked. No assertion about the first normalized layer follows without evaluating the surviving low layers and binomial correction.

When used with preceding A1turn13's P25 representatives, the pairing-to-Schur error has depth50. Thus modulo3^27 this exact reduction can be inserted into its complete coefficient formula. The actual/core transfer remains dependent on all earlier simultaneous hypotheses.

## Remaining task

Determine the actual residual low-layer/correction combination, not just one pair. Prove a complete moment/rank statement or actual relative determinant/cofactor law. The reduction alone supplies no s_c<32 bound, no all-prime gcd bound, and no shrinking nonzero integer forms.

