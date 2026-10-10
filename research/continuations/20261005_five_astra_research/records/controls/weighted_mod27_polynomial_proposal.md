> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Proposed uniform next polynomial digit: independent audit required

The ordinary prime-power factorial congruence is classical background, already
present in Granville's primary exposition and archive carry sources. This is
an application to the actual weighted residual, not a novelty claim for that
congruence. A1turn10's fixed polynomial H has been exactly expanded by the
coordinator: after M=3T, every nonconstant coefficient is divisible by9 in Z3,
and the constant is4. The receipt is an exact rational-polynomial certificate,
not a table of large degrees. Thus c/3=4,xi_last=2,Theta=5 modulo9 on3|j.

The following may evaluate the remaining scalar modulo27. It is not preaccepted.

For nonnegative a,b,c with a=b+c, separate the nonmultiples of3 in factorials:

U(a)=prod_{r=0}^{a-1}(3r+1)(3r+2)
    =2^a prod(1+(9/2)r(r+1)).

Modulo27 all products involving two9-factors vanish. Since
sum r(r+1)=a(a^2-1)/3 exactly, the unit factorial quotient gives

binom(3a,3b)=binom(a,b)[1+(9/2)abc] modulo27.

No division by a possibly nonunit binomial is required: the quotient of unit
factorials exists in Z3. The factor1/2 is a unit. Adjacent numerator factors give

binom(3a+1,3b)=binom(a,b)[1+3b-9bc+(9/2)abc] modulo27.

On3|M, A1 proved the pairing vector v of its approximate radical r is divisible
by9 (u=0mod3), while the mixed pairing vector w is divisible by3. Therefore
c=R-v^T E^-1 v agrees with R modulo81, and xi_last=X-v^T E^-1 w agrees with X
modulo27. This is exactly the precision needed for c/3 and xi_last modulo27.

The nine-term moment truncation still holds modulo81: every omitted rising
factorial at ell>=9 has depth at leastv3(9!)=4. Define f(s) exactly as in
A1turn10. Write F0(t)=4f(3t)-8(3t+1)f(3t+1)
                     +4(3t+1)(3t+2)f(3t+2).
Then E0(t)=(1-9t)F0(t)/3 represents e_(3t)/3 modulo27, because
(-8)^t=(1-9)^t=1-9t modulo81.

Similarly define F1(t)=-8f(3t+1)+16(3t+2)f(3t+2)
                      -8(3t+2)(3t+3)f(3t+3).
Then E1(t)=(1-9t)F1(t) represents e_(3t+1) modulo27.

Set t=D+E, with tau_D=(-1)^(M-D)binom(M,D). Then

c/3 = sum tau_D tau_E binom(D+E,D)
      [1+(9/2)(D+E)DE] E0(D+E) modulo27,

xi_last = sum tau_D tau_E binom(D+E,D)
      [1+3D-9DE+(9/2)(D+E)DE] E1(D+E) modulo27.

Each is now a fixed rational polynomial in D,E. Contract each monomial D^a E^b
using A1's exact fixed I_ab(M) formula. With M at least the largest degree,
both outputs become fixed rational polynomials in M, so a bounded residue rule
exists without an unknown inverse. On j>=6,3|j, M>=1365 exceeds every degree;
j=3,M21 must be checked separately if a degree exceeds21. The integer-valued
congruence and modulus of the rational polynomial coefficients require audit.

Then Theta=xi_last/(c/3) modulo27; the deep endpoint b-corrections vanish.
All lower factorial terms were removed by A1turn10 uniformly on3|j, so this
evaluates the entire local primitive ray modulo27. It does not evaluate the
actual rational-center gcd or prove irrationality ofe+pi.
