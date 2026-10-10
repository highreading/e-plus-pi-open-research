> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete-error exclusion for selectors of subfactorial degree and height

Status: new main-agent author deduction from explicit inputs. The application uses a finite irrationality-measure theorem for pi whose offline source is still being located. This note is not independently reviewed. No computation is claimed. It concerns a family of rational approximations, not the rationality or irrationality of e+pi itself.

## 1. Domain and retained formulas

Let n tend to infinity. For each n choose a nonzero primitive integer polynomial L_n(t), of degree d_n and coefficient height H_n=sum_i |[t^i]L_n|. Assume

    d_n+log H_n=o(n log n).

Write V(t)=t^2-t+1/2 and

    K_n(t)=2^n t^n D_t^n(V(t)^n L_n(t))/n!,
    U_n=K_n(1), A_n=|U_n|, N_n=2n+d_n.

Restrict to indices with U_n!=0. The saved direct-selector construction gives an integer polynomial K_n and rational companions alpha_n,beta_n satisfying

    beta_n=calL((K_n-U_n)/(t-1))/U_n,
    calL(f)=integral_{-1}^1 f((1+iu)/2)du,

    |e-alpha_n|<=E_n,
    E_n=27(2M)^n H_n/((n+1)n! A_n),
    M=1+sqrt(2),

    A_n<=2^(n+d_n+1) H_n M^n/sqrt(n),
    den(beta_n)<=A_n D_(N_n),
    D_N=2^(N-1)lcm(1,...,N).

These are the retained exact-companion and height inputs from DIRECT_SELECTOR_HEIGHT_OBSTRUCTION_DRAFT.md. Their hypotheses and normalization are essential. No arbitrary reconstruction center is identified with these companions.

Optionally choose any rational correction r_n with

    log den(r_n)=o(n log n).

Put gamma_n=r_n+beta_n, c_n=alpha_n+gamma_n, and q_n=den(c_n), always after full rational reduction. Without a correction take r_n=0. Let B_n=den(gamma_n).

## 2. Subfactorial denominator of the logarithmic companion

Set X_n=n log n. Since A_n is a nonzero integer, A_n>=1. Its displayed upper bound and the degree/height assumption imply

    0<=log A_n=o(X_n).

The elementary bound lcm(1,...,N)<=4^N gives D_N<=8^N. Consequently

    log B_n<=log den(r_n)+log A_n+N_n log 8=o(X_n).

This is an upper bound for the actual denominator B_n; it does not assert that the separate denominators multiply without cancellation. It remains valid with any numerator size for r_n.

Stirling's formula and the exact definition of E_n give

    -log E_n=X_n+o(X_n).

Thus the exponential approximation is factorially accurate, while the rational companion gamma_n has subfactorial denominator.

## 3. Explicit quantitative inputs

The retained elementary project theorem for e states that, for every epsilon>0, a constant C_epsilon>0 satisfies

    |e-a/b|>=C_epsilon b^(-2-epsilon)

for every reduced rational a/b with b>=1.

For pi assume a finite exponent mu>0 and constant C_pi>0 satisfying

    |pi-a/b|>=C_pi b^(-mu)

for every such rational. A finite irrationality measure supplies this assertion when mu is chosen strictly above the stated measure bound. Ordinary irrationality of pi alone is insufficient. The source and its exact quantifiers remain an explicit dependency in this continuation.

## 4. Complete-error lower bound

The pi input and log B_n=o(X_n) imply

    |gamma_n-pi|>=C_pi B_n^(-mu)=exp(-o(X_n))

in the sense of an asymptotic lower bound. Since E_n=exp(-X_n+o(X_n)), eventually

    E_n< (C_pi/2) B_n^(-mu).

The reverse triangle inequality therefore retains both components and gives

    |c_n-(e+pi)|
      >=|gamma_n-pi|-|alpha_n-e|
      >=(C_pi/2) B_n^(-mu).

In particular,

    liminf log|c_n-(e+pi)|/X_n>=0.

This does not assert convergence of the complete error to zero or a positive constant lower bound. It says that the complete error cannot be factorially small at the X_n scale.

## 5. Actual primitive-form divergence

Because alpha_n=c_n-gamma_n, its reduced denominator is at most q_n B_n. The e inequality yields

    E_n>=C_epsilon(q_n B_n)^(-2-epsilon).

Hence

    liminf log q_n/X_n>=1/(2+epsilon).

Letting epsilon decrease to zero gives liminf log q_n/X_n>=1/2. More directly, combining the two quantitative inequalities gives

    q_n |c_n-(e+pi)|
      >=(C_pi/2) C_epsilon^(1/(2+epsilon))
        E_n^(-1/(2+epsilon)) B_n^(-(mu+1)).

Therefore

    liminf log(q_n |c_n-(e+pi)|)/(n log n)>=1/2.

If p_n=q_n c_n is the actual integer numerator, the primitive forms p_n-q_n(e+pi) diverge in absolute value along every admitted sequence.

## 6. Scope and dependencies

Given the finite-measure input for pi and the retained selector formulas, this proof removes any separate saddle-sign or logarithmic noncancellation hypothesis throughout d_n+log H_n=o(n log n). It also allows rational corrections with subfactorial reduced denominators.

It does not cover selectors of degree or logarithmic height comparable to n log n, corrections with factorial denominator cost, zero forcing U_n, or other centers without the stated companion decomposition. It supplies no useful upper bound for reconstructed-coordinate denominators.

The argument is an author deduction, not a newly completed independent examination. The pi source must be checked before this application is promoted from explicitly sourced-theorem-dependent status. Even a fully established exclusion of this entire selector class would not decide whether the actual number e+pi is irrational.
