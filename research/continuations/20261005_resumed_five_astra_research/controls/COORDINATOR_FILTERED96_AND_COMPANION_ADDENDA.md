> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Two coordinator derivations for independent audit

These are mathematical proposals and source completions, not closure of the e+pi problem. All actual primitive normalizations and full-gcd obligations remain.

## Companion coefficient integrality

The personally inspected complete producer defines alpha as the coefficients of 1/(1-z+z^2/2). Thus alpha_0=alpha_1=1 and alpha_r=alpha_(r-1)-alpha_(r-2)/2. Induction gives alpha_r in Z[1/2] for EVERY r; equivalently beta_r=2^r alpha_r obeys beta_0=1,beta_1=2,beta_r=2beta_(r-1)-2beta_(r-2) with integer coefficients. Consequently alpha_r is integral at every odd prime, uniformly through the growing force endpoint. This supplies the explicit coefficient hypothesis requested by A4 turn10. It does not assert an exact valuation for v0.

The defining recurrence occurs in the personally authored complete-lift implementation endpoint_extrapolant_coordinator.py. It follows coefficientwise from multiplying its generating series by 1-z+z^2/2, and is not inferred from samples.

## A candidate reduction of the coefficient380 limit at precision96

This argument uses the central formulas and integral Newton contact transport attached separately. It is pending independent audit.

At k=-3, h=-95 and n=-190. The contact-symbol order r has divided-power valuation at least r+v2((h)_fall_r), since U^r is coefficientwise divisible by r!. For every r>=2, the falling product contains h-1=-96 and has valuation at least5. Such a contact occurrence costs at least r+5 bits and adds at most4r degrees. Combining this with i-4w_i<=3, any word containing r>=2 has degree at most4(95)-20+3=363 when it survives modulo2^96. Hence it cannot contribute to coefficient380.

Only repetitions of the order1 correction K1=2h E remain, where E=C_1(-1)+2C_2-3C_3+3C_4 is the full finite contact action of U.

For a word of length q<=93, put z=95-q>=2. A coefficient of degree380 would require initial degree i>=380-4q=4z. The sharper forcing bound from A4 turn11 is v2(F_i)>=v2(floor(i/2)!)>=v2((2z)!)>=z+1. Its total depth is at least q+z+1=96, so it vanishes. For q=94, only initial indices4..7 could survive the envelope; the complete fixed-precision force (reused only after parameter transfer) gives F_4..F_7=0 mod4 at h=-95,n=-190. Thus these terms also vanish modulo2^96. For q=95, only F_0..F_3 mod2 are needed. They are (0,1,1,1), so the input is g=B_1+B_2+B_3 in the Newton basis.

If these force transfers and degree/depth bounds pass, the actual limit bit reduces to

    p380*(-3)/2^95 mod2 = [B_380] E^95 (B_1+B_2+B_3) mod2.

The personally authored binary_limit_top_bit_coordinator.py evaluates this complete finite F2 operator at endpoints721 and1233. Both represent b=-95/2001 mod512, whose residue is209; binomial endpoint constants of order<=384 have this period modulo2 by Lucas. It uses the entire suffix T_v=S_b^v, not an interior-only top-degree action. The output is zero in both cases. In fact E g has degree3 and E^2 g is the zero vector in both complete finite matrices. The Newton extraction and independent Lucas finite-difference extraction agree.

If the polynomial identity E^2 g=0 can be proved uniformly at the continued endpoint, this gives an inexpensive proof of the zero precision96 bit, avoiding the dense O(p^5) calculation. It does NOT prove the whole coefficient limit is zero or supply a linear(k+3) valuation gain. It does NOT prove the complete actual norm residual.

## Evidence limits

The finite operator certificate tests an explicit filtered candidate. The transfer to the actual coefficient is the mathematical proof obligation above. Original family indices were not replaced by negative-sized matrices; negative parameters are used only after the endpoint dependence is encoded by polynomial continuation.
