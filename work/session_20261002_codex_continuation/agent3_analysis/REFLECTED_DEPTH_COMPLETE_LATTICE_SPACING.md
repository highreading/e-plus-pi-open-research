> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete discrete depth spacing at the convergent reflected window

2026-10-02. Original author theorem, Agent 3. Fresh archive/primary-paper queries, opened URLs, and exact prior overlap are saved in `REFLECTED_DEPTH_LATTICE_PROGRESS.md`. The quadratic actual-center theorem is `REFLECTED_KERNEL_QUADRATIC_CRITICAL_WINDOW.md`. Agent 2 owns the all-h positive determinant and exact final-q arithmetic. No audit or rationality conclusion is involved here.

## 1. The discrete theorem

Keep n=4k, h>=1, N=n+h, R=sqrt(N/n), and the ACTUAL reflected kernels/projection of the quadratic note. Define

    Theta_n(N)=n/R-2R-(1/2)log n-log(4sqrt(2)).

In any fixed bounded Theta window, uniformly as n tends to infinity,

    log[alpha_(N+1)/alpha_N]
        =-1/(2R³)-1/(nR)+O(n^-2),                       (1)
    c_(n,h+1)-c_(n,h)
        =-alpha_(n,h)[1/(2R³)+1/(nR)](1+o(1))<0.        (2)

The COMPLETE c includes both the exponential residues and both rational primitive endpoints. In particular, wherever alpha tends to e,

    c_(n,h+1)-c_(n,h)
        =-2sqrt(2)e n^(-3/2)(1+o(1)).                  (3)

The proof uses exact neighboring-depth identities. It does not differentiate an o(1) asymptotic or replace an actual projected error by a single kernel component.

## 2. Exact Pascal coupling

For a function f of integer X, with zero extension below its stated support, put

    Z_N(f)=sum_(l=0)^N binom(N,l) f(N-2l).

Pascal's identity gives EXACTLY

    Z_(N+1)(f)=sum_(l=0)^N binom(N,l)[f(X+1)+f(X-1)].    (4)

The polynomial/binomial functions for ordinary origin and pole-1 responses are

    f_D(X)=binom(X+n,n), X>=0,
    f_C(X)=binom(X-1,n), X>=n+1.

On their support their exact increment multipliers are

    k_D(X)=2+n(n-1)/[(X+1)(X+n)],
    k_C(X)=2+n(n-1)/[(X-n)(X-1)].                       (5)

Formula (4) also has boundary terms when f(X)=0 but f(X+1)!=0. Those terms are not discarded algebraically. They have binomial size at most 2^N times a bounded-degree factor, whereas the central partition sum has size 2^N R^n exp[O(n)]. They are therefore exp[-n log R+O(n)] relative corrections, with the same control after bounded exponential forcing.

Using the quadratic binomial means X_D=nR-n/4+O(R+n/R), X_C=nR+n/4+O(R+n/R), variance N/2+O(N/sqrt(n)), and the inverse-power moment bounds, (5) gives

    D_(N+1)/D_N=2+R^-2-(1/2)R^-3+O(n^-2),
    C_(N+1)/C_N=2+R^-2+(1/2)R^-3+O(n^-2).

Thus the exact discrete ordinary response comparison is

    log(D_(N+1)/D_N)-log(C_(N+1)/C_N)
          =-1/(2R³)+O(n^-2).                           (6)

## 3. Neighboring Laguerre forcing, with derivative control

Define the full origin mixture B_N(z) as in the quadratic note and the positive pole-1 mixture

    A_N(z)=sum_(X>=n+1) binom(N,(N-X)/2)
                              L_(X-n-1)^(n)(-z).

At z=1, A_N(1)=A and Aplus/A=1+(log A_N)'(1). The exact origin identity is D1/D=-(log B_N)'(0).

For Q_m(z)=L_m^(n)(z)/binom(m+n,n), its reciprocal root sums satisfy

    s1=mu=m/(n+1),
    s_j=[s_(j-1)+sum_(a=1)^(j-1) s_a s_(j-a)]/(n+j), j>=2. (7)

This follows directly from the Laguerre Riccati equation. It shows that s_j is a polynomial in mu with nonnegative coefficients and degree at most j. In the central range m~nR the s3 tail is O(n^-1/2), while its unit-degree finite difference is O(n^-2). The smallest central root tends to infinity. Therefore the root-product expansion and (7), including two z derivatives, give

    log[Q_(m+1)(z)/Q_m(z)]
       =-z/(n+1)-z²(2mu+1)/[2(n+1)(n+2)]+O(n^-2),
    log[Q_(m-1)(z)/Q_m(z)]
       =+z/(n+1)+z²(2mu+1)/[2(n+1)(n+2)]+O(n^-2).       (8)

All estimates are uniform for z in a fixed compact set. The polynomial positivity in (7) bounds successive differences of the tail by j/m times the corresponding root sum, and the root-product radius bounds the sum over j>=3. Thus (8) is a finite-difference bound; its O(n^-2) remainder does not come from subtracting two separate O(n^-1/2) expansions.

Apply (4) to f_D(X)Q_X(z). On the central range its multiplier is

    k_B(X,z)=k_D(X)-2z/X+O(n^-2).                       (9)

The z² terms in (8) have opposite signs; their sum is only O(n^-2) after multiplication by f_D(X+/-1)/f_D(X). The B-tilted mean shifts by

    E_B X-E_D X=-z N/[2(n+1)]+O(R).

Since k_D'(X)=-2n²/X³+O(n³/X^4), this shifts the expected k_D upward by z/(nR)+O(n^-2). The extra term in (9) contributes -2z/(nR)+O(n^-2). Variance and second-derivative terms are O(n^-2). Therefore

    log[B_(N+1)(z)/B_N(z)]
       =log[D_(N+1)/D_N]-z/(2nR)+O(n^-2),              (10)

with two z derivatives. For the pole-1 mixture, the degree is X-n-1 and forcing is -z; the same calculation gives

    log[A_(N+1)(z)/A_N(z)]
       =log[C_(N+1)/C_N]+z/(2nR)+O(n^-2).              (11)

The signed remote origin Laguerre terms are bounded by their finite series and are exponentially negligible, as in the quadratic proof. Thus (10) estimates the actual mixture, not its absolute-value replacement. The binomial laws and their bounded tilts are controlled uniformly in the neighboring N window, so the derivative bounds in (10)-(11) remain valid.

## 4. Actual determinant and projection covariance

Write

    gamma_N=-[(log B_N)'(1)-(log B_N)'(0)]
               =lambda/2+O(n^-1/2)>0,
    rho_N=Aplus/A+D1/D=2R+O(1).

The exact projection formula and C/D tending exponentially to zero give, in the fixed bounded Theta window,

    U/T=D A rho_N[1+O(exp(-a sqrt(n)))],
    alpha_N=(gamma_N/rho_N)[B_N(1)/A_N(1)]
                                [1+O(exp(-a sqrt(n)))],       (12)

for some window-dependent a>0. This is the actual determinant/projection: the other numerator terms have relative exponential suppression here because A/D=exp[-(1/sqrt(2)+o(1))sqrt(n)].

By the two-derivative control in (10), gamma_(N+1)-gamma_N=O(n^-2); the leading linear z term cancels when its first derivative is compared at z=0 and z=1. Equations (10)-(11) similarly give

    rho_(N+1)-rho_N=1/(nR)+O(n^-2),
    log[(gamma_(N+1)/rho_(N+1))/(gamma_N/rho_N)]=O(n^-2).

Taking the logarithm of (12), and combining (6), (10) and (11), proves (1). Since alpha is positive and bounded away from zero in the fixed Theta window, (1) proves the alpha increment in (2).

The complete two-endpoint beta bound at both neighbors is

    |beta_N-pi|+|beta_(N+1)-pi|
          <=exp[-(n/2)log n+O(n)].                      (13)

Its difference is negligible against n^-3/2. Adding (13) proves (2)-(3) for the COMPLETE center c.

## 5. What integer depth rigorously supplies

Take any fixed K>0. The exact critical-window construction with Theta near +K has c>(e+pi) eventually; the one near -K has c<(e+pi). Equation (2) proves strict decrease between these endpoints. Hence there is a unique adjacent bracketing pair h_n,h_n+1 in that window with

    c_(n,h_n)>=e+pi>=c_(n,h_n+1),
    Delta_n=c_(n,h_n)-c_(n,h_n+1)
                =2sqrt(2)e n^-3/2(1+o(1)).              (14)

The nearer of these actual rational centers has

    |c-(e+pi)|<=Delta_n/2
                 =sqrt(2)e n^-3/2(1+o(1)).              (15)

This improves the exact-leading-curve tuning's O(n^-1/2) upper bound to a guaranteed mesh bound. It uses the actual centers, not a real-parameter surrogate. The bracketing pair lies within O(n) integer depths of the theta=0 depth defined by Psi(n,N)=n/R-2R+log(R/(4n))=0 in the amended quadratic note, because that center has O(n^-1/2) error and every step in the window has size comparable with n^-3/2. Relative to the simpler closed radical rule (15) of that note, whose error is O(log n/sqrt(n)), the guaranteed search radius is O(n log n). The limiting convergence and spacing statements are the same for both rules.

If a guaranteed nonzero error is needed, choose the farther bracketing node. Its error lies between Delta_n/2 and Delta_n, so it is nonzero and of exact order n^-3/2. This selected farther node is not a small-linear-form construction.

For any eta_n=o(n^-3/2), at most one integer h in this fixed window can satisfy |c_(n,h)-(e+pi)|<=eta_n. A spacing theorem does not provide a lower bound for the nearer node: e+pi could be much closer to that one center, or could equal it. The theorem isolates the exceptional alignment; it does not exclude it.

## 6. Complete actual q remains quadratic exponential

For every depth here, retain Agent 2's EXACT final reduced denominator

    q=N! O_N U/gcd(N! O_N U,
                       O_N[N!B(F)]+N! O_N[4 Im P(a)]),

where O_N is the odd part of lcm(1,...,N). Its all-h parity theorem gives

    v2(q)=v2(N!)+v2(U)>=v2(N!)+1,
    log q >= (log2/2+o(1))n².                            (16)

This applies to BOTH bracketing nodes and retains all determinant/projection content and primitive endpoint terms. Changing h by one does not remove the factorial dyadic cost. The guaranteed farther node has q|e+pi-c| tending to infinity by (14)-(16). For the nearer node, (15) is only an upper bound, so no lower conclusion follows. A rationality argument would require a separate theorem about the exceptionally small aligned residual, below the scale exp[-(log2/2+o(1))n²], and any additional surviving q. Neither the polynomial mesh nor a formal derivative proves such a theorem.
