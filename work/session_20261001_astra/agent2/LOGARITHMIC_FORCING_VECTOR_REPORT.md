> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Logarithmic forcing vector report

New author paper result, with no numerical scans or repeated checks. SIGNED_ADJOINT_REMAINDER and its log(2) envelope are preserved.

The proposed vector rate holds. For n>=16 and 2<=b<=n,

    ||D_R eF||_2 <= 2 sqrt(pi b/n) n! (sqrt(2)-1)^n.

This is stronger than the requested bound and does not require the additional slow-growth restriction or an inverse estimate.

The necessary arbitrary-vector specialization was derived directly. For any polynomial L, coefficient comparison, n integrations by parts with all endpoint terms zero, and deformation away from the pole at 1 give

    sum_i lambda_i eF_i
      =(-1)^(n+1)2n! integral_(-pi/4)^(pi/4)
        [sqrt(2)cos(theta)-1]^n
        L(1-exp(i theta)/sqrt(2)) dtheta.

No center normalization is assumed. Both conjugate endpoints and the orientation factor 2 are retained. Taking L(t)=t^i gives each forcing entry. The bounds |t(theta)|<=1/sqrt(2) and h(theta)<=chi exp(-theta^2) prove the vector estimate.

There is also a signed additive vector identity

    eF=(-1)^(n+1)2n! J_n (tstar^i)_i+rvec,

where J_n is the explicit positive arc integral, tstar=1-1/sqrt(2), and

    ||D_R rvec||_2 <= sqrt(pi)/(2n^(3/2))
                     n! chi^n sqrt(sum_(i=0)^(b-1)i^4).

Moreover J_n>=chi^n/(2sqrt(n)), so eF_0 has the displayed parity sign. No coordinatewise relative asymptotic is asserted.

For the actual center adjoint, the COMPLETE identity remains

    t-(e+pi)=c0+lambda^T eE+lambda^T eF.

With Jlambda=||D_R^(-1)lambda||_2, its new bound is

    |t-(e+pi)|<=|c0|+
      [2sqrt(pi b/n)n!chi^n+9(1+sqrt(2))^n/(n+1)]Jlambda.

The exponential forcing and actual endpoint constant are both retained. The research note states the further propagation conditional on the separate author inverse input, without duplicating the main agent's positive-fP work.

The unresolved issue for a signed center asymptotic is the actual adjoint evaluation at tstar and its cancellation with the bounded remainder, exponential forcing, and endpoint term. No reduced-denominator or center-recurrence result is claimed. Primitive pair estimates must still retain q times the complete directional error and 1/q, with separate endpoint gcd cancellation.

Full derivation: LOGARITHMIC_FORCING_VECTOR.md. Both files require read-back before reporting completion.
