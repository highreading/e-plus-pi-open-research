> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Proportional size: exact full-coordinate Selberg representation

Author: Codex continuation Agent 3, 2026-10-02. Incremental original analysis. The exact formulas below hold at every normal index. The subsequent equilibrium computation is for the positive ABSOLUTE principal ensemble; it has not been promoted to an asymptotic theorem for the complete signed actual center.

## 1. Checks and primary-source overlap

Archive queries before this target included proportional, b=floor(n/2), b/n, equilibrium, Selberg, characteristic product, Cauchy, double scaling and saddle in CONTACT_NORMALITY_RESEARCH.md, CONTACT_INVERSE_RESEARCH.md, GROWING_TWO_SCALAR_QUOTIENT_DRAFT.md, RATIONAL_SADDLE_SELECTOR.md and GAUSSIAN_VANDERMONDE_BOUND.md. The old b^4 log n normality and proportional high-row bounds were located; neither supplies a complete proportional-size center asymptotic. The two-scalar projective quotient concerns another exact determinant reduction. No accepted audit was replayed.

Primary queries:
- site:arxiv.org Toeplitz determinant characteristic polynomial Jacobi Selberg integral varying weight two singularities equilibrium measure
- site:arxiv.org unitary ensemble two logarithmic singularities equilibrium measure phase transition characteristic polynomial

Opened [Luque and Thibon, Hankel hyperdeterminants and Selberg integrals](https://arxiv.org/abs/math-ph/0211044), [Charlier and Gharakhloo, Jacobi/Laguerre Hankel asymptotics](https://arxiv.org/abs/1902.08162), and the full [Claeys and Grava primary chapter on critical random-matrix behavior](https://library.slmath.org/books/Book65/files/140317-Claeys.pdf). Also reopened the primary Chen/Xu/Zhao and Kuijlaars/Van Assche/Wielonsky records already logged for the uniform growing-size work. Exact Selberg/characteristic methods and equilibrium variational conditions are established literature; the present actual reconstruction insertion and rational potential are derived explicitly. The opened Hankel theorem's hard-edge hypotheses do not directly apply to the present soft-edge, signed full-circle problem. No global novelty is inferred from the searches.

## 2. A reconstruction insertion for EVERY actual coordinate

Retain sigma=sqrt(2), M=1+sigma, d=b-1, the unnormalized complex circle functional nu_(n,d) and exact characteristic-force factors from GROWING_B_CHARACTERISTIC_PRODUCT_ASYMPTOTIC.md. Define

    p_z(t)=product_(l=1)^d(z_l+t/sigma),
    R_j(z)=[t^j](t-1)(1+D_t)^(-n)p_z(t), 0<=j<=b.       (1)

This is exactly sum_l K_(j,l)sigma^(-l)e_(d-l)(z). It retains every coefficient of K at growing b; no top-column approximation is made. For n>=1 it has the gamma representation

    R_j(z)=sigma^(-d)/Gamma(n) integral_0^infinity
       u^(n-1)exp(-u)
       [e_(d-j+1)(sigma z-u)-e_(d-j)(sigma z-u)]du,        (2)

where an elementary polynomial with index outside 0,...,d is zero. This follows from
(1+D_t)^(-n)p(t)=Gamma(n)^(-1)integral u^(n-1)e^(-u)p(t-u)du; the finite polynomial expansion justifies all interchanges. In particular R_b=sigma^(-d) exactly.

Let Cplus(z) be

    n!/(2pi) integral_(-pi)^pi (1+sigma cos s)^n
                           product_l(z_l^-1+sigma+exp(is))ds,

and Cminus(z) be

    2n! integral_(-pi/4)^(pi/4)(sigma cos s-1)^n
                           product_l(z_l^-1+sigma-exp(is))ds.

Define

    P_j=nu_d(R_j Cplus), F_j=nu_d(R_j Cminus),
    E_j=nu_d(R_j sum_(i=0)^d sigma^i e_(d-i)(z^-1)eE_i),
    D=det H_b.

The exact actual coefficient equations are

    u_j=(-1)^n P_j/D,
    v_j-(e+pi)u_j=delta_(j,0)+(-1)^n E_j/D-F_j/D.        (3)

Consequently whenever u_j!=0,

    c_j-(e+pi)=E_j/P_j+(-1)^(n+1)F_j/P_j
                                    +(-1)^n delta_(j,0)D/P_j. (4)

No complete exponential forcing or endpoint is dropped. There is an exact full-Gram version that does not divide individual coordinates:

    c_W-(e+pi)=
      [sum_j W_jj P_j(E_j+(-1)^(n+1)F_j)
                             +(-1)^n W_00 P_0 D]
                        /(sum_j W_jj P_j^2).             (5)

All these integrals are real after the conjugate symmetry is used. The only domain assumptions are D!=0 and the actual positive Gram denominator nonzero. Equations (1)-(5) are the desired complete characteristic-product interface for moderate or proportional b.

## 3. Exact Jacobi/Selberg transformation

Put x=tan(t/2), z(x)=(1+ix)/(1-ix). Then

    1+sigma cos t=M(1-x^2/M^2)/(1+x^2),
    |z(x_q)-z(x_p)|^2=4(x_q-x_p)^2/[(1+x_q^2)(1+x_p^2)].

For every insertion G, the FULL circle functional is exactly

    nu_(n,r)(G)=2^(r(r-1)) M^(rn)/(r!pi^r)
       integral_(R^r) Delta(x)^2 product_l
         [(1-x_l^2/M^2)^n/(1+x_l^2)^(n+r)
           exp(-sigma z(x_l))] G(z(x)) dx.               (6)

The integral includes the outer region |x|>M. If k coordinates lie there, the base has sign (-1)^(nk). Partitioning by k and using symmetry gives its exact sector decomposition. The odd-index outer sectors cannot be silently discarded.

Restricting ONLY the principal sector |x_l|<=M and putting x_l=M y_l gives

    nu_principal(G)=2^(r(r-1)) M^(rn+r^2)/(r!pi^r)
       Z_(n,r)^Jac E_Jac[
           product_l(1+M^2 y_l^2)^(-n-r)exp(-sigma z(My_l))
                                      G(z(My))],         (7)

where the positive Jacobi expectation has density proportional to
Delta(y)^2 product_l(1-y_l^2)^n on [-1,1]^r. Its exact Selberg normalizer is

    Z_(n,r)^Jac=2^(r^2+2nr) product_(j=0)^(r-1)
       [Gamma(n+1+j)^2 Gamma(j+2)/Gamma(2n+r+j+1)].        (8)

Formula (8) uses the standard Selberg integral after y=2u-1. It is not a new general Selberg identity. Substitution of G=R_j Cplus, R_j Cminus, or the exact E insertion in (7), together with the other sectors in (6), supplies an exact Selberg expectation for every full actual coordinate and the actual Gram center.

## 4. Explicit positive equilibrium on the principal interval

Let r/n tend to c>0. Ignoring the order-r analytic amplitude only at the leading order-r^2 energy level, the mapped positive principal ensemble has external field

    V_c(x)=(1+1/c)log(1+x^2)-(1/c)log|M^2-x^2|,

up to an irrelevant additive constant. Its principal-interval equilibrium density is

    mu_c(x)=C_c/pi *sqrt(A_c^2-x^2)
                  /[(1+x^2)(M^2-x^2)], |x|<=A_c,

    A_c^2=M^2 c(c+2)/[M^2+(c+1)^2],
    C_c=sqrt((M^2+1)(M^2+(c+1)^2))/c.                    (9)

Here A_c<M. Derive (9) from the resolvent

    R_c(z)=V_c'(z)/2
       -C_c sqrt(z^2-A_c^2)/[(z^2+1)(M^2-z^2)],          (10)

with sqrt(z^2-A^2)~z at infinity. Removal of the poles at i and M gives

    C_c sqrt(1+A_c^2)/(M^2+1)=(c+1)/c,
    C_c sqrt(M^2-A_c^2)/[M(M^2+1)]=1/c.

Its asymptotic R_c(z)~1/z verifies total mass one; its jump is the positive density (9). On (A_c,M), the variational gap increases, so this is the principal constrained equilibrium.

For the FULL absolute ensemble, the gap decreases on (M,infinity) and is minimal at infinity (the circle point -1). Its limiting gap relative to the support is

    Delta_c=2/c [arccoth(Q_c)-(c+1)artanh(Q_c/(c+1))],
    Q_c=sqrt(M^2+(c+1)^2)/sqrt(M^2+1)>1.                 (11)

This follows by integrating
2C_c sqrt(x^2-A_c^2)/[(1+x^2)(M^2-x^2)] from A_c to infinity in the real principal-value sense; the logarithmic singularity at M cancels between the two sides. Thus (9) obeys the full absolute-ensemble variational inequality exactly when Delta_c>=0.

The bracket in (11), as a function of q=c+1, has derivative

    -artanh(sqrt(M^2+q^2)/(q sqrt(M^2+1)))<0.

Its limit at q=1 is log M>0, and it tends to minus infinity as q tends to infinity. There is one transition c_star>0, defined by its zero. The full absolute equilibrium first acquires support near the circle point -1 beyond that transition. This is an auxiliary positive equilibrium statement; the actual complex amplitude and odd signed sectors require their own noncancellation estimates.

## 5. Proportional forcing has a moving complex saddle

At the order-n level the characteristic product cannot be replaced by its value at one. If the necessary characteristic expectation and contour estimates were proved, the plus/minus scalar phases would be

    Phi_plus(zeta)=log[1+(sigma/2)(zeta+zeta^-1)]
                       +c L_c(sigma+zeta),
    Phi_minus(zeta)=log[(sigma/2)(zeta+zeta^-1)-1]
                       +c L_c(sigma-zeta),
    L_c(q)=integral log(z(x)^(-1)+q) dmu_c(x).             (12)

The branch is real on the positive real arguments under consideration. Although the modulus on the original circle is symmetric, the derivative of its complex phase at zeta=1 is generally nonzero. The true stationary point therefore need not remain at one: this is why a modulus-only approximation does not establish the actual n-exponent.

At zeta=1, the reciprocal relation L_c(M)-L_c(M^-1)=log M gives the formal difference (2+c)log M. This is not yet the full-center rate: moving saddles, coordinate insertions (2), the outer sectors, full exponential forcing and endpoint dominance must all be controlled on the SAME proportional sequence. The next calculation will examine (12) using the explicit resolvent, with any candidate rate kept distinct from a proved signed-error theorem.
