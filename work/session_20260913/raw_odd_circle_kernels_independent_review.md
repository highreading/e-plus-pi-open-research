> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the explicit odd circle boundary kernels

Date: 2026-09-13. Reviewer: audit_results.
Target: raw_odd_explicit_circle_boundary_kernels.md.
Verdict: FULL PASS. No correction required.

## 1. Kernels and residual normalization

I checked the coefficient formula (1), its endpoint sum (2), and the beta integral (3). Expanding the beta integral gives the coefficient

    (-1)^j binom(M,j)
    B(a+j+1,a+M-j+1)/B(a+1,a+1),

which is exactly the displayed kernel coefficient divided by H_M^(a). The a=0 case is the Haar kernel and includes M=0 without an exception.

The map r-p -> 1-(1+t)p identifies the residual minimization bijectively with degree-at-most-m+1 polynomials having value one at -1. The weight drops by one exactly, so its minimizer is the lower-weight normalized kernel and rho^2=1/H. The ratio of the two endpoint kernels gives

    ||Lambda||^2=3(m+1)^2/[4(2m+1)(2m+3)]<=1/4.

This agrees independently with the Cayley-coordinate top Jacobi coupling squared divided by four. The constants k(0)=1/2 and R(0)=(2m+1)/((m+1)H), including the sign of R_(m+1), follow directly from the coefficient formula.

## 2. Rational inverses and the actual endpoint vector

Polynomial division gives the two formulas (7). In the first inverse formula (8), the top coefficient is canceled and the resulting f(-1) equals -g_m/R_(m+1). In the second, the constant coefficient is canceled and f(-1)=g(0)/R(0). Substitution into (7) gives g in both cases. The stated block order in A0^(-1) is correct.

The reversed OPUC identity gives K_m(t,0)=Phi_m^*(t)/h_m and c_m=1/h_m. Thus v=(sqrt(c_m)Phi_m^*,0), and pairing with v returns f_1(0)/sqrt(c_m). This is the actual original endpoint-coordinate vector, not the kernel at -1.

The three inputs (10) have the correct components and ordering. Their norm bounds follow from ||A0^(-1)||<=2 and ||U||<=1/2.

## 3. Finite coefficient functional

Canceling one conjugate factor 1+bar(t) converts the original residual pairing exactly to the lower-weight projection in (11). The symmetry

    conjugate(Klow(t))=(-1)^(m+1)t^(-m-1)Klow(t)

then shows that a monomial t^k selects coefficient 2m+1-k of P=(1+t)^(2m+1)Klow, with the displayed sign.

The ratio of successive coefficients of Klow is

    - (m+j)(m+2-j)/[j(2m+2-j)],

which verifies its differential equation directly. Conjugation gives the displayed equation for P and the recurrence

    P_v/P_(v-1)
       =(m+1-v)(3m+3-v)/[v(2m+2-v)].

For v<=m this is exactly the ratio of the L_v in the note. At v=m+1 it forces a zero, and all coefficients through 2m+1 remain zero; division is not made at the resonant index 2m+2. The central zero block and the negative coefficient-index cutoff prove (12) for analytic g, including the absence of every Taylor coefficient outside m+1,...,2m+1.

At m=0, Klow=1-t, P=1-t^2 and the functional is -[t]g/sqrt(2), confirming both the sign and the endpoint case.

## 4. Boundary matrices and profiles

The equations (13) solve E0, with its established accretive inverse, and preserve the factor order Q=E0^(-1)A0^(-1). The two-component testing functional is J0* times the normalized residual pairings. Consequently every block in (14) agrees with D2=I+VQU and D3=[[D2,VQv],[v*QU,v*Qv]], including the positive lower-left row. No compressed exponential identity is being assumed.

For the endpoint kernels, the exact squared tail is H_(M-r)/H_M. The factorial formula gives the product (15), hence the uniform bounds 3^(-r) and 2^(-r). The top squared coefficient tends to 2/3, each fixed backward ratio tends to 1/3, and the alternating signs follow from Phi_j(-1). These tails justify norm convergence of (16).

For the origin kernel, h_j/h_(j-1)=j(2a+j)/(a+j)^2. At a=m+1 and j<=m this is below 3/4, proving the uniform tail bound. Its top coefficient is Phi_m(0)=(-1)^m a/(a+m), whose squared magnitude tends to 1/4. This gives exactly the profile (17), including its signs and total norm one.

These are circular orthonormal coefficient profiles. The source correctly keeps them distinct from the Cayley-basis endpoint profile and from any assertion of multiplication-operator convergence.

## 5. Scope

Every finite formula, sign, factorial normalization, inverse order, and small-index case passes. The norm bounds do not establish determinant lower bounds. The explicit E0^(-1) remains present, and replacement by limiting operators requires the separate operator-limit proof.

No new degree, prime, root, or singular-value scan was used in this review.
