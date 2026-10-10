> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large-selector phase drift and sparse exceptional nodes

Status: main-agent author deduction, not independently reviewed. The analytic input is agent2/LARGE_SELECTOR_RELATIVE_SADDLE.md, read in full by the main but not yet independently examined. The complete dyadic law has a separate scoped PASS in agent4/LARGE_SELECTOR_DYADIC_REVIEW.md, also read by the main. This note does not extend that PASS to analysis. No calculation or numerical selection is claimed.

## 1. Domain and analytic input

Fix rho>0 and a fixed C>0. Let n tend to infinity and restrict integer m to

    |m-rho n log n|<=C n log n/log log n.

Put lambda=n/m, nu=1/n, alpha=(1+i)/2,

    V(w)=w^2-w+1/2, A(w)=(2w^2-1)^2,
    J_m=integral_(1/2)^alpha V(w)^n A(w)^m/w^(n+1) dw.

The path is the straight segment. The cited author saddle theorem supplies a nonzero J_m and a relative formula

    J_m=P_(n,m) exp(n F(lambda,nu))
          sqrt(2pi/n) beta(lambda,nu)^(-1/2)(1+e_m),
    |e_m|<=C1/n,

uniformly, with the exact displaced critical point retained in F. The prefactor has phase consisting of a term independent of m and (-2i)^m; its other m-dependent factor is positive lambda^(n+1). The functions F and beta are analytic near lambda=0, uniformly for the stipulated nu. The square root is continued from beta(0,nu)=4.

The explicit expansion in the cited proof is

    F(lambda,nu)=-log 2-1
       +lambda(-1/8+3i/8+nu alpha/2)+O(lambda^2).

Thus

    Im F_lambda(lambda,nu)=3/8+O(lambda+nu).

Here differentiation is justified by the analytic expansion of F itself. We do not differentiate the merely bounded remainder e_m.

## 2. Signed phase drift beyond the quarter turn

For neighboring integers,

    lambda'=n/(m+1),
    lambda'-lambda=-lambda^2/n+O(lambda^3/n^2).

Taylor expansion of the analytic F gives

    n Im(F(lambda',nu)-F(lambda,nu))
       =-3lambda^2/8+O(lambda^3+lambda^2/n).

The square-root factor contributes O(lambda^2/n) to the phase increment. The quotient (1+e_(m+1))/(1+e_m) contributes O(1/n), since each remainder is uniformly O(1/n). This step uses only their two bounds, not a bound on their derivative.

Choose consistent real phase lifts theta_m=arg J_m whose neighboring increments are near -pi/2. The exact prefactor and these estimates prove

    theta_(m+1)-theta_m
       =-pi/2-3lambda^2/8+O(lambda^3+1/n).           (1)

Uniformly in the block, lambda~1/(rho log n), so both error terms are o(lambda^2). Consequently, for all sufficiently large n, the positive drift

    d_m=-(theta_(m+1)-theta_m+pi/2)

satisfies

    lambda^2/4<=d_m<=lambda^2/2.                    (2)

Enlarging the threshold if necessary gives the convenient uniform bounds

    1/(8rho^2(log n)^2)<=d_m<=1/(rho^2(log n)^2).    (3)

All increments used must lie inside the stated saddle domain.

## 3. At most one exceptional node in a logarithmic-square window

Define

    L=floor(rho^2(log n)^2/8),
    delta=1/(100rho^2(log n)^2).

Eventually L>=2. Call an integer m exceptional when

    dist(theta_m,pi Z)<delta.

Any L consecutive nodes entirely inside the saddle domain contain at most one exceptional node.

Proof. Suppose two such nodes differ by s, with 1<=s<=L-1. Summing (1) in its exact drift notation gives

    theta_(m+s)-theta_m=-s pi/2-D,
    D=sum_(j=0)^(s-1) d_(m+j).

Equation (3) implies 0<D<1/8. If s is even, s>=2 and

    dist(theta_(m+s)-theta_m,pi Z)=D
       >=1/(4rho^2(log n)^2)>2delta.

If s is odd, the same distance is at least pi/2-1/8, also greater than 2delta eventually. But two exceptional phases would give distance less than 2delta by the triangle inequality modulo pi. This contradiction proves the assertion.

In particular, exceptional nodes in such an interval are separated by at least L integer steps. An interval of k nodes contains at most ceil(k/L) exceptional nodes. This is a counting theorem, not an identification of their integer locations.

## 4. Complete-error divergence away from the exceptional set

Now take n=4k>=4 and retain the actual direct-selector construction

    Bpoly_m(t)=(1-2t+2t^2)^n(1-4t+2t^2)^(2m),
    K_m=t^n Bpoly_m^(n)/n!, U_m=K_m(1).

Only U_m!=0 nodes define rational companions alpha_m,beta_m and c_m=alpha_m+beta_m. The retained coefficient and Cauchy bounds give, uniformly in the block,

    |U_m|>=2^(n/2),
    log|U_m|<=(n/2)log log n+O_(rho,C)(n).

At a nonexceptional node, the distance to pi Z is in [delta,pi/2], hence

    |sin theta_m|>=2delta/pi.

The author saddle magnitude theorem gives

    log|J_m|=m log 2-n log(m/n)+O_(rho,C)(n)
             =m log 2-n log log n+O_(rho,C)(n).

The exact complete logarithmic residual is

    beta_m-pi=(-1)^(n+1)2^(n+2)Im J_m/U_m.

Combining these statements proves

    log|beta_m-pi|
       >=m log 2-(3n/2)log log n-O_(rho,C)(n).       (4)

The logarithm of delta contributes only O_rho(log log n), absorbed into the displayed remainder. The entire exponential residual satisfies

    |alpha_m-e|<=exp(-n log n+n log log n+O_(rho,C)(n)).

For fixed rho>0, this is negligible compared with (4). The reverse triangle inequality therefore proves, eventually at every nonexceptional nonzero-forcing node,

    log|c_m-(e+pi)|
       >=m log 2-(3n/2)log log n-O_(rho,C)(n).       (5)

The exact m is retained. Its allowed adjustment cannot be discarded at the subleading n log log n scale.

Let q_m be the fully reduced denominator of c_m. The separately reviewed arithmetic theorem gives

    v_2(q_m)=v_2(n!)+v_2((n+4m)!)+v_2(U_m)-n-2m.

Using v_2(U_m)>=n/2 and the binary factorial formula, (5) implies

    log(q_m|c_m-(e+pi)|)
       >=3m log 2-(3n/2)log log n-O_(rho,C)(n).      (6)

The analytic dependency of (5)-(6) remains the unreviewed relative-saddle proof. Raw complete-error divergence in (5) already implies primitive-error divergence because q_m>=1.

## 5. Parity-qualified runs and scope

For n=2^s, s>=3, every integer m with residue in [n/4,n/2-1] modulo n/2 satisfies v_2(U_m)=n/2. A full such run has k=n/4 nodes, all with nonzero forcing.

For each full run contained in the saddle domain, Section 3 bounds the exceptional fraction by

    ceil(k/L)/k<=1/L+1/k=O_rho(1/(log n)^2).

Thus all but this proportion obey (5)-(6), conditional on the analytic input. More generally, an eligible subinterval of length k' has exceptional fraction at most 1/L+1/k'. No assertion about an arbitrarily short fragment having small exceptional fraction is made.

The result permits an unbounded sequence selecting isolated exceptional nodes. It does not prove that those nodes have small errors, nor that they cannot have small errors. The exponentially precise phase-alignment requirement in LATEST_COMPANION_AND_SADDLE_EXTENSIONS_DRAFT.md remains the relevant necessary condition for bounded primitive errors at such nodes. A relative O(1/n) saddle remainder alone is insufficient to exclude that precision.

This note is a conditional sparsity theorem for failures of a large-error lower bound. It is not an all-node exclusion, an irrationality theorem, or a numerical density observation. The actual e+pi problem remains open.
