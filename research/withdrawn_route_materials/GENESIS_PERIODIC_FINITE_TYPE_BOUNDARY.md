> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The finite-type boundary of the rational-period countermodel

Status: proved classical support / discarded Genesis mechanism. Working research note, not a main proof. Created 2026-10-02 during the active Genesis stage.

## Gate and scope

The preceding exact-order-one countermodel has log maximum modulus O(R log R), not a proved finite exponential type. This note determines the stronger boundary. Session archive search found only that preceding candidate and its stated limitation. Fresh public searches used periodic entire / finite exponential type / rational Taylor, algebraic derivatives / period, and trigonometric polynomial / entire exponential type. The finite-Fourier-support core is established public mathematics. Opened primary author paper: Dryanov--Qazi--Rahman, *Entire Functions of Exponential Type in Approximation Theory*, Varna 2002 proceedings, pp.86--135, Corollary1.3 on printed p.92, https://www.math.bas.bg/mathmod/Proceedings_CTF/CTF-2002/files_CTF-2002/P1-04-Dryanov-Qazi-Rahman.pdf . Its proof was read. Waldschmidt's author course on finite exponential type, https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/CoursInterpolation1.pdf , was opened as background. A search result located a Pólya1943 discussion, but the direct PDF open returned a blocked one-line page; it is not counted as a full read.

This is a consequence of classical finite Fourier support and rational recurrence recovery, not a newly retained mathematical paradigm. No implication from rationality of S=e+pi to the required periodic entire object has been proved.

## Theorem

Let f be a nonconstant entire function of finite exponential type, with all Taylor coefficients at0 algebraic. If T>0 is a real period, then 2*pi*i/T is algebraic. In particular, f cannot have any nonzero real algebraic period. The same statement holds with rational Taylor coefficients as a special case.

### Proof

By rescaling the classical periodic finite-type theorem, f has finite Fourier support:

    f(z)=c_0 + sum_{j=1}^r c_j exp(lambda_j z),
    lambda_j=2*pi*i*k_j/T,  k_j distinct nonzero integers, c_j nonzero.

For completeness, finite support also follows directly by moving the Fourier coefficient integral from [0,T] to [0,T]+iy. A bound |f(z)|<=C exp(tau|z|) gives |c_k|<=C' exp(tau|y|+2*pi*k*y/T). For |2*pi*k/T|>tau, choosing the sign of y and letting |y| grow forces c_k=0. Only finitely many k survive. Nonconstancy gives r>=1.

Put a_n=f^(n)(0), so all a_n are algebraic and, for n>=1,

    a_n=sum_j c_j lambda_j^n.

The r by r Hankel matrix H=(a_{u+v+1}) with0<=u,v<r factors as V diag(c_j lambda_j) V^t, where V_{u,j}=lambda_j^u. Its determinant is nonzero: all lambda_j and c_j are nonzero and the lambda_j are distinct. Let

    P(X)=X^r+p_{r-1}X^(r-1)+...+p_0=product_j(X-lambda_j).

The equations a_{n+r}+sum_{v=0}^{r-1}p_v a_{n+v}=0 for1<=n<=r have invertible coefficient matrix H. Since the entries and right sides are algebraic, their unique solution consists of algebraic p_v. Thus every lambda_j is algebraic. Any j gives 2*pi*i/T=lambda_j/k_j algebraic. If T were nonzero algebraic, this would make pi algebraic, contradicting its established transcendence. QED.

The argument only needs algebraic coefficients, without a shared number field or common denominator bound. It does not assume that Fourier amplitudes c_j are algebraic; the Hankel recovery proves the required spectral algebraicity independently of that assumption.

## Consequences for the preceding construction

The function in GENESIS_PERIODIC_RATIONAL_GERM_COUNTERMODEL.md has period1, all Taylor coefficients rational and exact order1. The theorem therefore proves its exponential type is infinite. The distinction between finite order and finite type is necessary, not cosmetic.

This classical obstruction could be used only after a separately proved operation constructs a nonconstant periodic entire function of finite type with algebraic germ from the actual hypothetical endpoint equality. Such an operation is currently absent. Merely imposing these properties on a proposed completion is an extra hypothesis, not a consequence of S being rational. The finite-type obstruction itself is public and is not retained as a Genesis core.

## Polynomial differential equations do not escape this boundary

A further archive gate searched periodic / D-finite / holonomic / polynomial differential equations; the sole old archive hit was unrelated shifted endpoint periods. Public searches located Stanley's foundational1980 D-finite paper at https://math.mit.edu/~rstan/pubs/pubfiles/45.pdf and standard constant-coefficient differential solution theory in Sturmfels, *Solving Systems of Polynomial Equations*, Chapter10, https://math.berkeley.edu/~bernd/cbms.pdf . The latter's one-variable solution discussion and Theorem10.3 were read. These supply classical background; no novel differential mechanism is claimed.

Lemma. Any periodic entire function f satisfying a nonzero homogeneous linear differential equation with polynomial coefficients over C also satisfies a nonzero constant-coefficient linear differential equation over C. If the original polynomial coefficients are algebraic, the resulting constant coefficients are algebraic.

Proof. Write sum_j P_j(z) f^(j)(z)=0 and d=max_j deg P_j. For every integer n, periodicity with nonzero period T gives sum_j P_j(z+nT) f^(j)(z)=0. For fixed z this is a polynomial identity in n, since it holds for infinitely many integers. Its highest coefficient is T^d sum_j ell_j f^(j)(z)=0, where ell_j is the coefficient of z^d in P_j. At least one ell_j is nonzero. Division by T^d gives the claimed nonzero constant-coefficient operator. QED.

Its solutions are finite sums p_j(z)exp(lambda_j z). Periodicity first forces exp(lambda_j T)=1 for every surviving term, by independence of distinct exponential-polynomial terms; it then forces p_j(z+T)=p_j(z), hence p_j constant. Thus the finite-Fourier-support conclusion follows without a prior growth assumption. If the operator has algebraic coefficients, every lambda_j is algebraic. Nonconstancy gives a nonzero lambda_j with lambda_j T=2*pi*i*k for a nonzero integer k. Consequently T cannot be algebraic. This latter conclusion does not even require algebraic initial derivatives.

For an equation over arbitrary complex coefficients, algebraic Taylor germ instead recovers the algebraic spectrum by the Hankel proof above. Therefore the period-one countermodel is not D-finite even over C(z). A meromorphic periodic D-finite function has no poles: its poles would form an infinite translated set whereas a polynomial linear differential equation permits finite poles only at its finite leading-coefficient zero set. It is therefore entire and falls under the same argument.

The missing actual numerical bridge remains unchanged. Endpoint equality at two points does not supply equality of all seam jets or periodicity. In particular F=exp+4atan has F'(0)=5 and F'(1)=e+2, and these remain unequal under the rational-S hypothesis. Neither a periodic completion preserving the actual differential law nor its necessary arithmetic properties has been established. No such completion theorem is assumed here.
