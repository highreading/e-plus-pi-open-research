> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual short-stack response scale and its primitive-content cost

Author theorem: Agent 2, 2026-10-02. The fresh archive and opened-primary gate is `SHORT_STACK_COEFFICIENT_SCALE_GATE.md`. This is an original coefficient-size component of the lower-block-dependent content target. The exact coefficient integral and uniform conditional comparison are USED WITH AUTHOR ATTRIBUTION from Agent 3's `SHORT_RECTANGULAR_COMPLETE_SIGNED_ERROR.md`, equations (5), (6), and (14). The signed error and positivity are not re-presented as new results here.

## 1. Full coefficient pair and the result

Keep Root's actual unshifted M24 stack

    beta(T)=det[C;R+TV]=beta0+T beta1,
    C_ij=D_(2(i+j))-(-1)^(i+j),
    R_ij=-(2(i+j))!+4 sum_(a=1)^(i+j)(-1)^(i+j-a)/(2a-1),
    V_ij=(-1)^(i+j),  0<=i<k, 0<=j<2k.

Let L=lcm(1,3,...,6k-5), I0=L^k beta0, J1=L^(k-1) beta1, and I1=L J1. The FINAL reduced denominator is

    q_k=|I1|/G_k,   G_k=gcd(I0,I1).

All logarithms below are natural. As k tends to infinity,

    log|beta1|=4k^2 log k+O(k^2),                         (1)
    log|I1|=log|J1|=4k^2 log k+O(k^2).                   (2)

The previously proved full-pair factorial/dyadic divisor then gives the improved honest ceiling

    log q_k <= 3k^2 log k+O(k^2).                        (3)

This is an UPPER bound for the actual primitive denominator. It proves no lower growth law and does not establish primitive smallness. Combined with the all-depth two-rectangle sandwich, (1) also prices the unresolved arithmetic: any subsequence with primitive forms tending to zero must have

    liminf log(h_N h_W)/(k^2 log k) >= 4.                (4)

Here h_N and h_W are the actual maximal-minor contents in `SHORT_STACK_SIMULTANEOUS_JET_CONTENT.md`. In particular their sizes cannot be inferred merely from the generic Gamma divisor.

## 2. The exact analytic input, with its actual normalization

Let mu be the pushforward of exp(-t)dt, t>=0, by y=(1-t)^2, and let

    d sigma(y)=[exp(sqrt(y))+4/(1+y)]dy/(2sqrt(y)), 0<y<1.

Agent 3 proves, for every k>=100 and every k-node vector z in [-1,1]^k,

    exp(-4/a) F_k^* <= F_k(z) <= F_k^*,
    a=1/(48e^4),
    F_k^*=det[mu(y^(i+j)(y+1)^k)]_(0<=i,j<k)>0.         (5)

Inserting one node -1 kills the upper signed atom exactly. Its coefficient identity is

    |beta1|=1/(k-1)! integral_[0,1]^(k-1) Vand(x)^2
       product_i(1+x_i)^2 F_k(x_1,...,x_(k-1),-1) d sigma^(k-1).

Define the positive compact factor

    B_k=1/(k-1)! integral Vand(x)^2 product_i(1+x_i)^2 d sigma^(k-1).

Therefore, retaining BOTH exp(sqrt(y)) and 4/(1+y),

    exp(-4/a) F_k^* B_k <= |beta1| <= F_k^* B_k.         (6)

No inverse-cofactor or conditional-normalization loss is being dropped. The constant in (5) is independent of k and of all compact integration nodes.

## 3. The weighted Gamma determinant has scale 4k^2 log k

On I=[k^2,4k^2] the complete measure has density at least exp(-2k-1)/(4k). Consequently

    (y+1)^k dmu/dy >= w_k,
    w_k=exp(-2k-1)(k^2+1)^k/(4k).

For every polynomial p of degree <k, the positive weighted Gram form is at least w_k integral_I p^2 dy. Loewner monotonicity of positive definite Gram matrices gives

    F_k^* >= w_k^k det[ integral_I y^(i+j)dy ].           (7)

Translation and scaling y=k^2+3k^2 u give exactly

    det[ integral_I y^(i+j)dy ]=(3k^2)^(k^2) H_k,
    H_k=det[1/(i+j+1)]_(0<=i,j<k).

The classical Cauchy determinant, as in Krattenthaler's opened primary *Advanced Determinant Calculus*, gives

    H_k=(product_(r=0)^(k-1) r!)^4 / product_(r=0)^(2k-1)r!.

Stirling summation yields

    log H_k=-2(log 2) k^2+O(k log k).

Also k log w_k=2k^2 log k+O(k^2). Hence (7) proves

    log F_k^* >=4k^2 log k-O(k^2).                      (8)

For the upper bound, mu(y^s)=D_(2s)<=(2s)!, including s=0. Every entry of the weighted matrix is bounded by

    sum_(a=0)^k binom(k,a) D_(2(i+j+a))
       <=2^k (2(i+j+k))!.

For each determinant permutation pi, sum_i(i+pi(i)+k)=2k^2-k, and each factorial argument is at most 6k-4. The determinant expansion therefore gives

    F_k^* <= k! 2^(k^2) (6k)^(4k^2-2k).

Together with (8),

    log F_k^*=4k^2 log k+O(k^2).                        (9)

The lower bound is a Gram comparison on a moving interval of scale k^2; the upper bound retains the TOTAL factorial index in each permutation. A separate worst-entry estimate would lose this leading constant.

## 4. The entire compact coefficient factor costs only O(k^2)

Put n=k-1. Since sigma has density at least 1 on (0,1) and (1+y)^2>=1, Heine's formula and the same Cauchy determinant give

    B_k >= H_n.

On the other hand Vand(x)^2<=1 and product_i(1+x_i)^2<=4^n. The FULL mass is exactly

    sigma([0,1])=e-1+pi=S-1<6.

Thus

    H_n <= B_k <= 24^n/n!,
    -O(k^2)<=log B_k<=O(k).

Using (6) and (9) proves (1). This compact estimate is deliberately sufficient rather than a new sharp compact-measure asymptotic. Charlier--Deano's opened primary supplies the classical Heine framework; none of that paper's Hermite-weight asymptotics is imported into this measure.

## 5. The actual gcd, improved ceiling, and required Smith content

The classical Chebyshev bound for the least common multiple gives log L=O(k); its previously opened Rosser--Schoenfeld refinement is already recorded in `SHORT_STACK_ACTUAL_ODD_LAURENT_CONTENT.md`. Hence multiplying beta1 by L^k or L^(k-1) changes its logarithm by O(k^2), proving (2).

Let F_s=product_(r=0)^(s-1)r!. Our proved integer basis argument in `SHORT_STACK_FACTORIAL_ACTUAL_CONTENT.md` gives the PRODUCT divisor

    2^(k(k-1)) F_(k-1)^2 | I0 and I1.

This includes the factorial's own 2-content only once. In particular

    log G_k >= log F_(k-1)^2
             =k^2 log k+O(k^2).

Subtracting this from the actual response size (2) proves (3). The previously proved W_k odd-prime common divisor is coprime to these factorial/dyadic factors and may also be retained; its logarithm k^2+o(k^2) changes the subleading O(k^2), not the leading constant 3.

The simultaneous-output proof gives, for EVERY prime depth,

    lcm(h_N,h_W) | G_k | L h_N h_W,
    q_k >= |J1|/(h_N h_W).                             (10)

Agent 3's COMPLETE signed-error theorem gives

    log(q_k(S-c_k))=log q_k-4k log(1+sqrt(2))+O(log k).

If the left-hand primitive forms tend to zero along any subsequence, then log q_k<=4k log(1+sqrt(2))+O(log k) along that subsequence. Equations (2) and (10) force (4). More exactly the physical gcd must satisfy

    log G_k >= log|I1|-4k log(1+sqrt(2))-O(log k).

This records the required FULL specialized cancellation. Neither (3), the generic Gamma saturation theorem, nor one finite rectangular-content receipt proves or disproves that cancellation. The open task remains a uniform lower-block-dependent law for h_N and h_W and its final pair carries.
