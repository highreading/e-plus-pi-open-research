> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# M29. Slow-growing-dimension short-shift obstruction

Original author theorem, Root, 2026-10-02. Status: complete within the stated family and regime; no decision of the main e+pi problem. This completes the conditional transfer in SHIFTED_SHORT_GROWING_DEGREE_HEIGHT_PROGRESS.md using Agent3's original uniform Gamma/compact leading-coefficient theorem.

## Scope and prior-work gate

The fresh archive and primary-paper gate recorded in the progress note remains the gate for this target. The external arithmetic input is Ernvall-Hytönen, Matala-aho and Seppälä, *On the transcendence measure of e*, Constructive Approximation 49 (2019), 405–444, https://arxiv.org/pdf/1704.01374v3, Definition1 and Theorem1.1. Its explicit degree-dependent height threshold is retained. The new analytic input is agent3_analysis/UNIFORM_GAMMA_COMPACT_LEADING_NONZERO.md, with its distinct fresh gate. No fixed-degree implicit constant is used for growing dimension.

Let S=e+pi. Use M26's actual k-by-2k short matching stack at even shift M, X=2M. Let c=p_c/q be its fully reduced center and q>0 its ACTUAL denominator. The old arctangent mass l=p_l/a is also reduced. Write f=X!, d=D_X, T=X+6k+1. The exact integer-cleared stack polynomials A,B satisfy

    a q A(d,f)+(q p_l+a p_c)B(d,f)=0.

Their total (d,f) degree is at most k. The coefficient of f^k in A is delta^k Z_k(X), and B has f-degree at most k-1.

## Uniform evaluated nonzero coefficient

Agent3 proves, for every k>=1 and X>=128k,

    Z_k(X)!=0,  sign Z_k(X)=(-1)^(k+1).

This is the actual evaluated integer polynomial det[P;Q-V], not a generic specialization assumption. Its proof uses exact signed Gamma-square conditional Grams and the true small Gamma lower-tail mass. The leading-homogeneous extraction below is therefore a NONZERO integer polynomial whenever this explicit condition holds.

For k>=2, X>=4, |c|<=8 and |l|<=4, define

    H0=a q T^(100k^2).

The determinant coefficient estimate in the progress note bounds every coefficient of F=a q A+(q p_l+a p_c)B by H0. With F_k its degree-k homogeneous part, put P_X(z)=F_k(z,1). The constant coefficient a q delta^k Z_k(X) is nonzero. The exact equation F(d,f)=0, d/f=1/e+O(1/(Xf)), and the lower-degree pieces give

    0<|P_X(1/e)|<=8k^2 H0/f.                         (1)

This estimate uses the final reduced q throughout.

## Explicit threshold alternative

For k>=3 let s=k(log k)^2; for k=2 let s=e. Put U=s exp(s), Hthr=ceil(exp(U)), and

    Omega(k,H)=k+[16k^2 log(k+1)+1]/log log H.

The primary measure gives |e^k P_X(1/e)|>H^(-Omega(k,H)) for H>=max(H0,Hthr). The extra positive slack avoids the infimum boundary in the definition. Combining with (1),

    log f < logH0+Omega(k,H)logH+k+log(8k^2).          (2)

There are two exact alternatives. If H0>=Hthr,

    logq > [logf-k-log(8k^2)]/[Omega(k,H0)+1]
              -loga-100k^2 logT.                    (3)

If H0<Hthr, instead

    logf < [Omega(k,Hthr)+1]logHthr+k+log(8k^2).       (4)

Thus raising the auxiliary height to the primary threshold is never silently converted into a denominator lower bound.

## The completed family exclusion

Consider any sequence of even M tending to infinity with integers k=k(M)>=2 such that

    k(log(k+1))^2=o(log M).                          (5)

Then X>=128k eventually, so the exact leading coefficient is nonzero. The complete analytic theorem SHIFTED_SHORT_UNBOUNDED_M_COMPLETE_ERROR.md applies because M>=max(100,16k) eventually. It gives both actual determinants nonzero, c tending to S, and hence the bounded-center hypotheses above. Also |l|<=4 directly from its compact integral.

Under (5), U=X^(o(1)); therefore the right side of (4) is X^(o(1)), whereas logf~XlogX. Alternative (4) is impossible eventually. Hence (3) applies. For unbounded k, loglogH0>=s and Omega=k(1+o(1)); for bounded k, loglogH0 tends to infinity and Omega=k+o(1). The elementary bound a<=lcm(1,...,X-1)<=4^X gives loga<=Xlog4. Both loga and 100k^2logT are negligible relative to logf/(k+1). Consequently

    logq >=[1-o(1)]log(X!)/(k+1).                    (6)

The exact Jacobi formula in Agent3's complete signed-error theorem yields, uniformly in this regime,

    log|S-c|=-(2k-1)logX+O(klog(k+1)+k^2/X).

Combining with (6) gives

    log(q|S-c|) -> +infinity.                        (7)

Indeed the positive term is asymptotic to XlogX/(k+1), whereas the negative term has size O(klogX), and X/k^2 tends to infinity. This includes every fixed k>=2; M27 separately closes k=1. It also excludes all slowly growing dimensions satisfying (5), after the complete final gcd, rather than only a raw factorial clearer.

This is a construction obstruction. The regime M proportional to k, faster growing k, other matching weights, and other approximation families are outside (5). No claim about the irrationality or rationality of S follows from (7). No proof-completion or quota stop condition has been met.
