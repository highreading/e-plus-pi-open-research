> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Diagonal linear review and endpoint contribution, stage 5

Status: limited independent review of Main's new Stage 7 implications, conditional on the inherited complete identities; separate original author proof of the endpoint scale. The original endpoint proof is not independently reviewed. S=e+pi remains unresolved.

## 1. Sources and scope

Read in full through actual controller results: work/parallel_batch_01/main/DIAGONAL_LINEAR_THRESHOLD_STAGE7.md and work/parallel_batch_01/agents/30dc1035/09f71b29/COMPLETE_ERROR_CONTENT_THRESHOLD_STAGE1.md. The historical complete-product identities are inherited hypotheses, as requested. Their source text is also preserved in the supplied transcript. No audit of those identities, previous root refinements, or multiplicity branches is undertaken.

Write gamma(dy)=y^(-1/2)dy on [0,1], w0=exp(sqrt(y))gamma/2, and sigma_k=[exp(sqrt(y))+c_k(1+y)^(-k)]gamma/2, where c_k=4^k/binom(2k-2,k-1). D_k denotes the degree-below-k Gram determinant. Our original target is E_k=log[D_k(sigma_k)/D_k(w0)]. All logarithms are natural.

## 2. Limited review of Stage 7

Base-Gram ratio monotonicity: VALID. For fixed B>=0, det(A+B)/det A=det(I+B^(1/2)A^(-1)B^(1/2)) decreases as positive definite A increases. In particular G0>=G/2 gives precisely the stated comparison with c_k times the gamma bump Gram. No factor two is missing.

Compressed-resolvent correction: VALID, including the infinite tail. Multiplication by y is a bounded positive self-adjoint Jacobi operator J. For t>0 its tail block plus tI has a bounded inverse, so the block inverse and Schur-complement formulas apply. The coupling has rank one. Consequently P(J+t)^(-1)P-(J_k+t)^(-1) is positive semidefinite of rank at most one. It is bounded above by the compressed resolvent, hence by t^(-1)I. The determinant-lemma correction at most 1+d/t follows with the correct inequality direction.

Legendre ratio: VALID. The degree-k gamma orthogonal polynomial is the monic normalization of P_(2k)(sqrt(y)). Evaluation at -u yields the ratio in Stage 7 with the same normalization canceling. Since all its y-roots are positive, its modulus at -t is at least its modulus at zero. The complex Laplace representation gives the displayed numerator bound exp[2k asinh(sqrt(u))]; choosing the imaginary square-root branch causes no sign or modulus problem. The lower central-binomial estimate used there is sufficient.

Fixed positive weight limit: VALID. The even Legendre recurrence coefficients give limiting diagonal 1/2 and off-diagonal 1/4 for multiplication by y. Fixed-length path traces yield the arcsine spectral limit. For a fixed polynomial p, P p(J)P-p(J_k) is supported at the omitted upper boundary and has bounded rank. Both approximating positive matrices have uniformly bounded positive spectra; rank interlacing controls their log determinants by O_p(1). Uniform approximation to a fixed positive continuous h then proves the first-order limit. It does not supply a uniform varying-weight theorem or a quantitative o(k) remainder.

Linear coefficient: VALID. The fixed-weight integral is 2/pi-log 2. Combining it with the reference linear term log(4pi), and subtracting the kappa linear term (log pi)/2, gives log(2sqrt(pi))+2/pi. The bounded log theta term has no effect at linear order. This concerns the complete ratio, with nonzero value and leading coefficient inherited.

Rational-denominator criterion: VALID. For the actual primitive integer polynomial of degree k, nonzero evaluation at a rational of reduced denominator v has modulus at least v^(-k). The exact inequality A_k<T_k(v) is therefore sufficient to exclude that denominator. A fixed finite residual linear coefficient does not exclude all v. The actual full gcd remains inside A_k throughout. No correction to the reviewed implications is required.

## 3. Original result: two-sided endpoint scale

There are absolute positive constants a and b such that, for all sufficiently large k,

 a sqrt(k)(log k)^(3/2) <= E_k <= b sqrt(k)(log k)^(3/2).

An explicit lower choice proved below is a=1/(16 pi e) for integer k>=ceil(exp(16)). The upper proof supplies a finite formula valid already for k>=4. These bounds determine a Theta scale; they do not establish a limiting coefficient.

## 4. Rational majorant for the upper bound

Let c=c_k, choose an integer r with 1<=r<=k, and put
 t=r/k, a_r=c^(1/r), d=t a_r, u=t+d.

For y>=0, (1+y)^k >= (1+ky/r)^r. Indeed log(1+z)/z decreases for z>0, or differentiate the equivalent inequality. Therefore

 1+c(1+y)^(-k)
 <=1+c[t/(y+t)]^r
 <=[1+a_r t/(y+t)]^r
 =f(y),

where f(y)=((y+u)/(y+t))^r. The second inequality is the binomial expansion with nonnegative terms. This majorizes the actual bump, without replacing its width by a fixed positive weight.

By the base-Gram comparison reviewed above and determinant monotonicity,

 E_k <= log det(P f(J)P),

where P projects onto the first k gamma orthonormal polynomials and the compressed operator is restricted to that k-dimensional space. We compare this with f(J_k), retaining the boundary correction.

### Rational compression rank lemma

For this f,

 rank[P f(J)P-f(J_k)] <= r.

Proof. Write e for the last coordinate vector of the first block. For s>0, the rank-one Schur formula gives

 P(J+s)^(-1)P-(J_k+s)^(-1)=eta(s) v(s)v(s)^T,
 v(s)=(J_k+s)^(-1)e,

with a real analytic scalar eta on s>0. This representation follows directly by the scalar rank-one inverse formula; the tail resolvent is analytic there because its spectrum is nonnegative. Differentiating q-1 times shows that the difference for inverse powers q has its column space in span{v(s),v'(s),...,v^(q-1)(s)}. The identity d^(q-1)(J+s)^(-1)/ds^(q-1)=(-1)^(q-1)(q-1)!(J+s)^(-q) holds in operator norm. Expand f(y)=sum_(q=0)^r binom(r,q)d^q(y+t)^(-q), and evaluate all terms at the same s=t. Their column spaces lie in one space of dimension at most r. This proves the lemma, including the infinite tail. Positivity of this higher-order difference is neither required nor asserted.

Both P f(J)P and f(J_k) have spectra in [1,M], where M=(1+a_r)^r, since J and J_k have spectra in [0,1]. If two positive k-dimensional matrices in this interval differ by rank at most r, their logarithmic determinants differ in absolute value by at most r log M. To see this, conjugate one by the inverse square root of the other: at most r eigenvalues differ from 1, and all eigenvalues lie between 1/M and M. Hence

 E_k <= r log[det(J_k+u)/det(J_k+t)] + r^2 log(1+a_r).

Using the Legendre bound verified in Section 2 gives the explicit finite estimate

 E_k <= 2rk asinh(sqrt(u)) + r log(2k+1) + r^2 log(1+c^(1/r)).       (U)

For k>=4 choose r=ceil(log c_k). The elementary bound c_k<=8sqrt(k) gives r<=k, and c_k^(1/r)<=e. Consequently

 E_k <= 2sqrt(1+e) sqrt(k) r^(3/2)
        +r log(2k+1)+r^2 log(1+e),
 r<=log(8sqrt(k))+1.                                               (U2)

This proves E_k=O(sqrt(k)(log k)^(3/2)). In particular the finite-rank correction is O((log k)^2), below the claimed scale. A trace estimate for the original bump alone would not give this bound: the proof controls the logarithmic determinant itself.

## 5. Logarithmic compression lower bound

Put b(y)=c_k exp(-sqrt(y))(1+y)^(-k). In L2(w0), the Gram ratio equals the determinant of the compression of multiplication by 1+b to degrees below k. Operator concavity of log yields

 E_k >= integral K_(w0,k)(y,y) log(1+b(y)) dw0(y).                  (L1)

For completeness, the compression inequality follows from the integral representation of log and the inequality P(A+s)^(-1)P >= (PAP+s)^(-1) for A>0, s>=0, proved by a Schur complement. Integrating their difference gives log(PAP)>=P(log A)P. Here A is bounded and bounded away from zero, so the integral argument applies directly. Taking the finite-dimensional trace proves (L1).

Since w0<=e gamma/2, the extremal characterization of the polynomial evaluation kernel gives K_(w0,k)>=2K_(gamma,k)/e. Also dw0>=dgamma/2. The integrand is nonnegative; with y=x^2 this gives

 E_k >= (2/e) integral_0^1 K_(gamma,k)(x^2,x^2)
                    log[1+c_k exp(-x)(1+x^2)^(-k)] dx.            (L2)

We now give an explicit kernel lower bound without any varying-weight asymptotic.

## 6. Chebyshev comparison near the endpoint

Under y=x^2, the gamma norm of a polynomial in y equals the norm of its even polynomial in L2([-1,1],dx). On [-1,1], dx<=dx/sqrt(1-x^2). Thus the evaluation kernel for even polynomials of degree at most 2k-2 in dx is at least the kernel in the larger Chebyshev measure. The latter has the exact orthonormal basis 1/sqrt(pi), sqrt(2/pi)T_(2i)(x), 1<=i<k. Therefore, writing theta=arccos x,

 K_(gamma,k)(x^2,x^2)
 >=1/pi+(2/pi)sum_(i=1)^(k-1)cos^2(2i theta)
 =k/pi+(1/pi)sum_(i=1)^(k-1)cos(4i theta).

The geometric-sum bound gives the final sum at least -1/|sin(2theta)|. For k^(-1/2)<=x<=1/2, sin(2theta)=2x sqrt(1-x^2)>=sqrt(3)/sqrt(k). It follows that

 K_(gamma,k)(x^2,x^2)>=k/(2pi)                               (L3)

for k>=4. This is a uniform bound on the interval used below, not a limiting kernel assertion.

The elementary central-binomial bound binom(2n,n)/4^n<=1/sqrt(n+1) gives c_k>=4sqrt(k). It follows by induction from the exact consecutive ratio (2n+1)/(2n+2), which is at most sqrt((n+1)/(n+2)); the base n=0 is equality.

Let L=log k and assume L>=16. Integrate (L2) only on

 k^(-1/2)<=x<=sqrt(L/(4k)).

This interval is contained in [k^(-1/2),1/2] and has length at least (1/4)sqrt(L/k). On it, using log(1+x^2)<=x^2,

 log[c_k exp(-x)(1+x^2)^(-k)]
 >=log 4+L/2-x-kx^2
 >=L/4.

Hence log(1+b)>=L/4. Substituting this, (L3), and the interval length into (L2) proves

 E_k >= [1/(16 pi e)] sqrt(k)(log k)^(3/2),

for integer k>=ceil(exp(16)). This lower bound and (U2) prove the asserted two-sided scale.

## 7. Interpretation and unresolved refinements

The actual bump has amplitude comparable to sqrt(k) and is appreciable in logarithmic weight over an x-window of width comparable to sqrt(log k/k). The proof above quantifies its determinant cost without using this heuristic as evidence: the lower bound is a compression inequality plus an explicit kernel bound, and the upper bound is a rational majorant plus a rigorously controlled finite-rank correction.

No exact coefficient in E_k/[sqrt(k)(log k)^(3/2)] is established. Determining one requires controlling the gap between a compressed logarithm and the logarithm of a compression at this varying scale, or an equivalent quantitative determinant theorem. Neither a formal equilibrium integral nor the fixed-weight first-order limit controls that gap. This stage stops before invoking any unavailable varying-weight theorem.

The new endpoint bound improves Stage 7's O(k^(3/4)) term and supplies a nontrivial matching lower rate. It does not turn Stage 7's separate fixed-weight o(k) remainder into a quantitative remainder for the entire diagonal ratio. In particular no sublinear asymptotic coefficient for the full ratio is claimed. The reviewed linear coefficient and rational-denominator threshold remain unchanged.

All new arguments are symbolic. No numerical experiment, network access, factorization scan, arithmetic content theorem, or proof concerning the rationality of S is claimed. The actual full primitive coefficient gcd remains Main's arithmetic bottleneck.
