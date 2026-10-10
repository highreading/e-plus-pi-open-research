> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An actual primitive-form and intrinsic content interface for proportional b

Agent 3, 2026-10-02. Original author connection, not independently reviewed. Fix 0<c<1/1000, b/n->c and the actual factorial B-only metric, with ANY allowed depth 1<=m<=floor((b-1)/2). Normality, the complete signed center error and uniform coordinate asymptotics are supplied by PROPORTIONAL_ACTUAL_CENTER_SIGNED_RATE.md. This note identifies the exact intrinsic arithmetic needed; it does not establish the favorable gcd condition.

Write S=e+pi and tau_c=(2+c)log(1+sqrt(2)). The main new quantitative input is the SAME-ALLOCATION height identity

    log A_B=2log d_B+2(n+b)log n+O(n),                 (1)

where d_B is the LEAST common denominator of the actual two-column B lift, and A_B is its actual integer factorial Gram contraction AFTER common lift content has been removed. All arbitrary row-clearer factors have already canceled in (1).

The actual primitive center form has exact size

    |-p_n+q_n S|=q_n |c_n-S|,
    (1/n)log|-p_n+q_n S|=(1/n)log q_n-tau_c+o(1).     (2)

Thus the concrete unresolved need is an actual reduced-denominator rate below tau_c, or equivalently sufficient cancellation in the explicit Gram gcd defined below. An exponential error alone is not a proof about S.

## 1. Archive and primary-source gates

The older RATIONAL_CENTER_PAIR_CRITERION.md already gives the Bezout primitive pair and exact denominator gcd, with a different route through a complete quadratic bound. The older agent4/RATIONAL_CENTER_ARITHMETIC.md already gives the actual B adjugate lift and factorial-weight contractions. These exact algebraic inputs are reused and are NOT claimed new. Archive rg for least B denominator, (n+b)log n, proportional content, proportional primitive and common B content located those formulas and logarithmic-b selector-height work, but not the intrinsic proportional height identity (1) supported by the new actual complex saddle theorem.

Primary searches included Hermite Pade irrationality rational approximations common denominator gcd determinants factorial; Pade Gram rational approximation content primitive denominator varying degree; Fischler Rivoal Pade approximants denominators arithmetic; and Hermite Pade polynomial integer coefficients factorial content denominators irrationality. Opened the full Fischler/Rivoal paper https://arxiv.org/pdf/0910.4448, its G-function approximation record https://arxiv.org/abs/1512.06534, the full Hermite-Pade paper https://arxiv.org/html/1502.06695 and the current fixed-parameter Toeplitz/saddle paper https://arxiv.org/abs/2407.04852. Primitive small-form criteria and determinant/Padé methods are established literature. The G-function result does not automatically apply to this mixed exponential/logarithmic system, and no theorem from it is imported. No global novelty claim is made.

## 2. Removing ALL common row-clearer content

Let Psi=[u,v] be the exact actual B lift,

    u=K T^(-1)fP, v=e0+K T^(-1)fQ,
    sum_j u_j=0, sum_j v_j=1.

The e0 term is included throughout. Choose the concrete integral rows

    L_i=2^n(n+i)!, 0<=i<b,
    M=diag(L_i)T, Fhat=diag(L_i)[fP,fQ],
    Delta=det M!=0,
    N=K adj(M)Fhat+Delta e0 e2^T.

These are integer matrices. For T this follows by clearing the 2^n denominator of Q0^n and the remaining exponential coefficient factorials. For the forcing columns, the Taylor jets of exp(z) and F(z)=4arctan(z/(2-z)) are integral; multiplication by 1/(1-z) and the n derivatives gives denominators dividing the coefficient factorial. The same row factorial clears every retained coefficient. The finite reconstruction K is integral. Therefore

    Psi=N/Delta, sum_j N_(j,1)=0, sum_j N_(j,2)=Delta.

Set g0=gcd(all entries of N)>0. The last identity proves g0 divides |Delta|. Define

    d_B=|Delta|/g0,
    N_B=sign(Delta)N/g0.

Then N_B is an INTEGER two-column matrix with gcd of ALL entries equal to one, and Psi=N_B/d_B. This proves that d_B is precisely the least common denominator of the B lift. Any prime dividing a proposed smaller common denominator would have to divide every entry of N_B, which is impossible. The argument uses both columns and the exact endpoint term.

Enlarging the row clearers multiplies N and Delta by the same integer, hence leaves d_B and N_B unchanged. The forced factor g0 has therefore been removed before any logarithmic content requirement is stated. d_B is not the center denominator and is not replaced by the determinant Delta.

## 3. Actual factorial contractions and the final primitive gcd

Put ell=n+m+1, omega_j=(ell)_j, and Omega=diag(omega_j^2). The common scalar in the original factorial weights cancels from the center. Define the actual integer contractions

    A_B=sum_(j=0)^b omega_j^2 N_B(j,1)^2>0,
    H_B=sum_(j=0)^b omega_j^2 N_B(j,1)N_B(j,2),
    C_B=sum_(j=0)^b omega_j^2 N_B(j,2)^2,
    g_B=gcd(A_B,|H_B|),
    p_n=H_B/g_B, q_n=A_B/g_B>0.                       (3)

Thus the ACTUAL center is p_n/q_n and the pair is primitive. N_B being primitive as a whole does not imply that g_B is one, or that the projected Gram contractions are primitive. Equation (3) retains the final metric-dependent cancellation at every prime, including 2.

The direct squared norm identity is

    A_B=d_B^2 sum_j omega_j^2 u_j^2.                    (4)

## 4. Proving the intrinsic proportional height (1)

Let Z_r(0) be the positive principal base partition, with the SAME n at dimensions b and d=b-1. The actual determinant is within fixed positive factors of Z_b(0). The full plus saddle formula gives, uniformly in EVERY coordinate,

    log|u_j|=log(n!)+log B_j+log[Z_d(0)/Z_b(0)]+O(n).

All scalar phase values are bounded, and the local Gaussian only contributes O(log n). Adjacent norm factorization gives Z_b(0)/Z_d(0)=h_d. Its monic trial-polynomial upper bound is exp(sigma)M^n; the exact arc lower bound is C g_delta^n B_delta^d/(d+1)^2. Hence log h_d=O(n) on this same allocation. Consequently

    log|u_j|=log(n!)+log B_j+O(n).                     (5)

For 1<=j<=b, the exact top-column gamma reference gives

    log B_j=(b-j)log n+O(n),

uniformly in j; the endpoint j=b has B_b=sigma^(-d). The binomial coefficients are between one and 2^d, and every rising factorial factor lies between n and 2n, so no fixed-b constant is being extrapolated. At j=0, log B_0=(b-1)log n+O(n).

The allowed depth gives n+2<=ell<=n+b/2+1. Every factor in omega_j=(ell)_j lies between a fixed positive multiple of n and a fixed upper multiple of n. Therefore

    log omega_j=j log n+O(n)

uniformly in both j and m. Stirling's formula and (5) show, for each positive coordinate,

    log|omega_j u_j|=(n+b)log n+O(n).

The zero coordinate is one power of n smaller, which does not affect the stated scale. Summing b+1 positive squares adds only O(log n). Substitution in (4) proves (1), uniformly over all allowed factorial depths.

For perspective ONLY, the unreduced natural determinant has

    log|Delta|=[bn+b(b-1)/2]log n+O(n^2).

The actual complex determinant factor has log scale O(n^2) by the proved principal empirical energy and noncancellation. This explains the artificial n^2 log n scale of raw adjugate contractions. It is NOT counted as a required new cancellation because its common content g0 was already removed in (1).

## 5. Complete primitive forms and the exact remaining arithmetic need

Let epsilon_n=c_n-S, including the full exponential residual and coordinate-zero endpoint. The actual-center theorem gives epsilon_n!=0 eventually and

    log|epsilon_n|=-tau_c n+o(n).

It also implies q_n->infinity WITHOUT an irrationality assumption. Otherwise a bounded-denominator subsequence of the bounded centers would lie in a finite set of rational numbers. Its limit S and the nonzero error would be incompatible.

Choose integers x_n,y_n with q_n x_n+p_n y_n=1 and |y_n|<=q_n/2. The exact primitive endpoint vectors

    v1=(-p_n,q_n), v2=(x_n,y_n)

have determinant -1. Their COMPLETE forms are

    L1=-p_n+q_n S=-q_n epsilon_n,
    L2=x_n+y_n S=1/q_n-y_n epsilon_n,
    |L2|<=1/q_n+(q_n/2)|epsilon_n|.                    (6)

No reference envelope, incomplete logarithmic remainder, unremoved lift scalar or alternate metric is substituted in (6). Their actual rational contact lifts can be cleared separately; the resulting endpoint gcd cancels the same scalar and returns exactly these primitive forms.

A sufficient SAME-INDEX condition for both forms to shrink is

    limsup (log q_n)/n < tau_c.                        (7)

The first form is already nonzero, so (7) would prove irrationality by the elementary integer-form argument. This is a CONDITIONAL criterion; (7) has not been established. If instead liminf(log q_n)/n>tau_c, the center form L1 grows exponentially, which excludes this selected center-form route on that sequence, not rationality or all possible endpoint directions. The boundary exponent needs finer estimates.

By (3), (7) is exactly an intrinsic Gram-content requirement:

    liminf [log g_B-log A_B]/n > -tau_c.                (8)

In view of (1), a strict linear margin requires cancellation of

    2log d_B+2(n+b)log n-tau_c n+O(n)

in the FINAL actual gcd g_B, after all forced common row-clearer content has been removed. Neither the analytic noncancellation theorem nor the relative metric-equivalence theorem bounds this gcd. A same-index arithmetic proof of (8), or a decisive lower bound on q_n, is the identified next need. No favorable prime sum, coprimality assumption, or global gcd estimate is claimed here.
