> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact binary high-tail compensation — active research note

The original family is b=9^(18+32u), n=4002b, u>=0, with k=2C+1, h=32k+1, n=64k+2 and b=(32k+1)/2001. The continued parameter k=-3 is a compatible coefficient-system continuation; no negative matrix dimension is introduced.

The complete suffix operator on the Newton basis E_d(x)=binom(x,d) is S_b E_d=binom(b,d+1)E_0-E_(d+1). Noncommutative telescoping, followed by Vandermonde in the complete contact formula, gives the endpoint coefficient

    [E_e] R_s P = (-1)^e binom(n+e,s) L_b S_b^(s-1-e) P,  e<s.

At n=-190 this vanishes for every e>=190. The high-sector equations therefore have neither low-sector inputs nor endpoint injections. Their exponential generating function is

    Q_*(t)=(1+t+t^2/2)^190 G(t).

The complete central formulas at h=-95 give

    C_*(x)=sum_(a>=0) B_(190+a)(-95) x^a/a!
          = B190(-95)(1+x+x^2/2)^(-190).

Transforming the complete force yields G(t)=B190(-95)(1+t)^189(1+t+t^2/2)^(-190), hence

    Q_*(t)=B190(-95)(1+t)^189.

Thus p_(190+m)=B190(-95)*(189)_falling_m for all m>=0, and p_d*(-3)=0 for every d>=380. A4 turn14 derives this directly from terminating hypergeometric sums and the defining Gegenbauer series. These are classical identities applied to the complete supplied producer.

The coordinator personally evaluated the finite p380 expression from all9216 required central summands, with independently implemented polynomial convolution and triangular inverse. All191 coefficients and inverse residuals agree exactly; the output is0/1. The observed falling-factorial pattern was also checked at all191 finite indices before the independent all-index derivation was received. The certificate and source are identified in binary_limit_rational_receipt.json. This finite check is corroboration of the now-symbolic identity.

The complete coefficient system has the uniform parameter estimate P(k)-P(k') in2^(v2(k-k')+3)M. The proof pays the binomial endpoint loss with the established degree/valuation filtration; it retains all endpoint constants and complete central factorial tails. Consequently, on every original index, p_d(u) in8(k+3)Z2 for d>=380. For d380, the uniform fixed96-bit theorem also applies.

This closes the previously identified individual shifted-moment obstruction. It does not settle the complete grouped first norm, the separate mixed contraction or the final all-prime gcd. The second full force, exterior+1, shortened last block and least actual clearer remain required. The next target is a grouped relative-content theorem including the endpoint-coupled low sector on the same original indices.
