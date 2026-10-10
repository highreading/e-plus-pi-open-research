> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fixed-wall density control from the actual ordered chamber

This is a coordinator-derived proof proposal for independent audit. It
continues A3's finite-bias target; no all-sublinear error theorem is assumed.

The archive/current-report check supplies no evaluated conditioned-wall
density bound for this rescaled ensemble. The unimodal representation used
below is classical prior art, not a new theorem. A checked primary reference
is the Appendix, Lemmas A.1--A.2, of the research article
https://link.springer.com/article/10.1007/s11749-022-00844-9 .

Assume the exact results of A3 turn23: on its ordered convex chamber the
Hamiltonian has Hessian at least k*d with k=1/16; its mode a has all
coordinates in [-16,16]; its radius about a is stochastically bounded by
the norm of N(0,(k*d)^-1 I_d). Thus

    E ||u-a|| <= (E ||u-a||^2)^(1/2) <= 4.

For Z=u_d=max_i u_i, we get EZ<=20. Brascamp--Lieb gives Var(Z)<=16/d.
Prékopa's marginal theorem for the ordered chamber gives a log-concave,
therefore unimodal, density f_Z. The classical representation of a
unimodal variable with mode m is Z=m+U*Y, where U is uniform on [0,1]
and independent of Y. Since

    EZ-m=EY/2,
    Var(Z)=EY^2/3-(EY)^2/4 >= (EY)^2/12,

we have |EZ-m|<=sqrt(3 Var(Z)). Hence for d>=48 its mode is at most21.
In particular f_Z is nonincreasing on [23,24]. Consequently

    f_Z(24) <= integral_23^24 f_Z(t) dt <= P(Z>23)
              <= exp(-gamma_23*d),
    gamma_23 = (49/16 - 1 - log(49/16))/2 > 0.

The last inequality follows from A3's complete-domain radial tail with
T=7. Reflection gives the same bound for the lower extreme at -24.

Let Z(a_minus,a_plus) be the SAME ordered partition function with both
walls truncated, and P24=P(all coordinates in [-24,24]). Differentiation
in the upper wall, keeping the lower wall fixed, gives its boundary
surface integral. It is at most the unrestricted marginal density f_Z(24)
times the unrestricted partition function. Division by the truncated
partition function gives

    0 <= partial_(a_plus) log Z(-24,24)
       <= f_Z(24)/P24 <= 2 exp(-gamma_23*d)

for d sufficiently large, uniformly in small c. The absolute lower-wall
derivative has the same bound. No density bound is inferred merely from
an exponentially small event; marginal monotonicity supplies the missing
pointwise step. No extra factor d occurs if f_Z is the maximum's density
on the normalized ordered chamber.

This would justify using the usual soft-wall rank-one resolvent equation
and its exponentially small wall term on the fixed circles, avoiding
any issue introduced by an algebraic field vanishing at the walls.
Audit smooth boundary differentiation, log-concave ordered marginals,
and every normalization before using the lemma. The result still needs
uniform instantaneous-equilibrium loop inversion to control mean bias.
