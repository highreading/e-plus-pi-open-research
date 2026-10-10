> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Conditional endpoint scaling and the reciprocal polynomial

Date: 2026-09-13. Root derivation. The sole additional analytic
hypothesis below is unproved for the actual family. The argument
establishes consequences of that hypothesis, not unconditional limits.

Let P_n(t)=sum_{j=0}^n B_{n,j}t^{n-j}/(n-j)! be the reflected raw
polynomial, written sum_l a_l phi_l in the orthonormal shifted
Legendre basis. Assume the actual endpoint cancellation ratio is
bounded below: kappa_n>=kappa_0>0 eventually, where

    kappa_n=|P_n(0)|/sum_l sqrt(2l+1)|a_l|.             (H)

In particular P_n(0)=B_{n,n} is nonzero. The independently proved
sublinear concentration theorem already supplies, with any fixed
A>log16+3, w=ceil(A n/log(n+1)) and d=n-w,

    ||Proj_{<=d}P_n||_2 <=epsilon_n ||P_n||_2,
    epsilon_n=exp(-(A-log16-3+o(1))n).                 (1)

The previous note raw_weaker_top_two_endpoint_criterion.md gives a
sufficient unproved concentration condition for (H). No further
condition on the size of ||P_n|| is required here.

The broad-band estimate is transferred from the original moment
polynomial U_n(x)=P_n(1-x) by unitary reflection, which commutes with
all Legendre projections. The high test functions are reflected too;
see raw_reflection_convention_bridge.md for this convention.

## 1. All fixed leading coefficient ratios

For each fixed nonnegative integer r,

    B_{n,n-r}/(B_{n,n} n^{2r})
       =(-1)^r/r!+O_r(1/log n).                       (2)

To prove this, the exact shifted Legendre endpoint formula is

    phi_l^(r)(0)=(-1)^{l+r}sqrt(2l+1)
                     (l+r)!/[(l-r)!r!]    (l>=r),

and the derivative vanishes for l<r. Put h_{l,r}=(l+r)!/
[(l-r)!n^{2r}], with h=0 when l<r. Uniformly for n-w<l<=n,

    h_{l,r}=1+O_r(w/n).

The absolute sum of all endpoint contributions divided by |P_n(0)|
is at most1/kappa_0. The lower block's absolute endpoint mass is at
most (d+1)epsilon_n||P_n||_2. Since its full endpoint mass is at least
||P_n||_2, hypothesis(H) bounds the ratio of this lower mass to
|P_n(0)| by (d+1)epsilon_n/kappa_0. These estimates, applied to the
exact derivative formula, give (2). The coefficient identity used is
B_{n,n-r}=P_n^(r)(0), without an extra factorial.

For all 0<=r<=n, there is also the uniform bound

    |B_{n,n-r}/(B_{n,n} n^{2r})|
                  <=4^r/(kappa_0 r!).                 (3)

Indeed each of the2r factors in (l+r)!/(l-r)! is at most2n.
This deliberately rough bound is enough for locally uniform limits.

## 2. Two entire-function limits

Define the polynomial in the reciprocal variable w by

    E_n(w)=sum_{r=0}^n [B_{n,n-r}/(B_{n,n}n^{2r})]w^r.

For w!=0 this is exactly

    E_n(w)=B_n(n²/w)/[B_{n,n}(n²/w)^n],

and E_n(0)=1 by its polynomial definition. Equations(2)-(3), with the
summable majorant (4R)^r/(kappa_0 r!) on |w|<=R, prove

    E_n(w) -> exp(-w) locally uniformly on C.           (4)

Likewise the extra Taylor factorial gives

    P_n(t/n²)/P_n(0)
       -> F(t):=sum_{r=0}^infinity (-1)^r t^r/(r!)²
       =J_0(2sqrt(t)) locally uniformly on C.          (5)

The last expression denotes the entire power series F; it does not
require a branch choice for sqrt(t). The two functions in (4)-(5)
are different because P is the factorial transform of reversed B.
Dominated series convergence proves both statements and convergence
of every derivative on compact sets. No growing-radius convergence
is asserted.

The Bessel identification is the defining series in
[NIST DLMF 10.2.2](https://dlmf.nist.gov/10.2.E2).
The classical Legendre Mehler-Heine formula is recorded in
[NIST DLMF 18.11.5](https://dlmf.nist.gov/18.11.E5).
Our implication for the mixed-family polynomials is established
above by its coefficients and hypothesis(H); that classical formula
alone does not apply to the mixed family.

## 3. A conditional outer-root bound

Fix R>0. Since exp(-w) has modulus at least exp(-R) on |w|<=R,
(4) implies E_n has no zeros there for all sufficiently large n.
If a nonzero root rho of B_n had |rho|>=n²/R, its reciprocal point
w=n²/rho would contradict this fact. Roots rho=0 already obey the
bound. Thus

    max_{B_n(rho)=0}|rho|=o(n²).                       (6)

This remains weaker than the O(n) root bound needed in the accessory
compactness argument. For the root power sums s_{n,k}=sum_rho rho^k,
with multiplicities, the locally analytic logarithm of E_n normalized
by log E_n(0)=0 converges to -w. Consequently

    s_{n,1}/n² ->1,
    s_{n,k}/n^{2k} ->0 for every fixed k>=2.            (7)

This follows also by Newton identities from(2); it is a statement
about signed complex sums, not sums of absolute powers. In particular
max|rho|>=|s_{n,1}|/n=n(1+o(1)), consistently with(6).

The endpoint scale limit(5) also transports any isolated simple zero
of F to a unique nearby zero of t->P_n(t/n²), by Rouche's theorem.
For a real simple zero, choose a small conjugation-invariant disk;
the unique zero is real because P_n has real coefficients. This local
statement makes no claim about all the other zeros of P_n.

## 4. Remaining limitations

Hypothesis(H) is not proved. The unconditionally established broad
spectral band does not imply it on its own. These conditional results
do not estimate the primitive denominator, endpoint normalization
angle, or mixed remainder. In particular w=n² corresponds to B_n(1),
and t=n² corresponds to P_n(1); neither lies in a fixed compact set.
Using (4) or(5) at those growing arguments would be an invalid step.
The useful next problem remains a quantitative estimate establishing
(H), for example the weaker fixed-width concentration criterion.
