> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# M29 progress. Uniform growing-degree height transfer

Original root target, English research note. Status: the coefficient-height and primary-measure transfer below are proved conditional on the explicitly stated leading-coefficient nonzero input. Agent3 pursues that uniform Gamma/compact input as original research. This note is not an all-degree irrationality conclusion.

## Fresh gate

A fresh archive query for short-stack slow-growing dimensions, uniform Mahler thresholds and growing-degree height transfers found no completed version of this particular new specialization. M28's fixed-degree argument and all earlier generic algebraic-approximation strategies are credited. Fresh online primary searches found no specific answer; the exact definition, height threshold and Theorem1.1 of Ernvall-Hytönen--Matala-aho--Seppälä, arXiv:1704.01374v3, were reread for their UNIFORM degree dependence. This target must not reuse a fixed-degree implicit constant for growing k.

## Explicit coefficient-height bound

Let X=2M, f=X!, d=D_X, and use M26's full integer-cleared polynomials A,B. Let c=p_c/q be the actual primitive center and l=p_l/a the old mass. Assume |c|<=8, |l|<=4; the complete large-shift analytic theorem supplies these bounds eventually in the regime below.

Put

    T=X+6k+1,
    H0=a q T^(100k^2).

For k>=2, X>=4 this integer bounds every coefficient of

    F(d,f)=a q A+(q p_l+a p_c)B.

A direct proof uses |P_j(X)|<=T^j, |Q_j(X)|<=jT^(j-1), |h_r(X)|<=4r/(X+1), delta<=T^(3k-2), and the2k-square determinant expansion. Before multiplying by the center factors, (2k)!3^(2k)(12k)^(2k)T^(18k^2) bounds all coefficients. The larger exponent100 absorbs all coefficient counts and the bounded center factors. No primitive denominator estimate is presumed.

Let P_X(z)=F_k(z,1), F_k the total-degree-k homogeneous component. If Z_k(X)!=0, its constant coefficient is a q delta^k Z_k(X), so P_X is a NONZERO integer polynomial, degree<=k, height<=H0. Exact F(d,f)=0, d/f=1/e+O(1/(Xf)), and the lower homogeneous pieces give the uniform bound

    0<|P_X(1/e)|<=8k^2 H0/f.                (1)

This retains the ACTUAL q after the final gcd.

## Uniform primary transcendence threshold

For k>=3 put s=k(log k)^2; for k=2 use s=e. Define

    U=s exp(s),
    Hthr=ceil(exp(U)),
    Omega(k,H)=k+[16k^2 log(k+1)+1]/log log H.

For logH>=U, the primary Theorem1.1 implies

    |e^k P_X(1/e)|>H^(-Omega(k,H)),           (2)

provided H bounds the coefficients. The generous coefficient16 and added positive slack avoid using the infimum boundary of the measure and cover the explicitly listed small-degree constants.

With H=max(H0,Hthr), (1)--(2) give

    log f < logH0+Omega(k,H)logH+k+log(8k^2). (3)

If H0>=Hthr, this yields the exact conditional primitive budget

    logq > [logf-k-log(8k^2)]/[Omega(k,H0)+1]
             -loga-100k^2 logT.            (4)

If H0<Hthr, (3) instead forces

    logf < [Omega(k,Hthr)+1]logHthr
              +k+log(8k^2).               (5)

Thus artificially increasing the height to meet the theorem threshold does NOT silently supply a q lower bound; the alternative case must first be ruled out.

## Consequence conditional on uniform leading nonzero

Consider even M→infinity and k=k(M)>=2 with

    k(log(k+1))^2=o(log M).                 (6)

Then U=X^(o(1)). The right side of(5) is X^(o(1)), whereas logf~XlogX, so(5) is impossible eventually. Hence H0>=Hthr. For unbounded k, Omega(k,H0)=k(1+o(1)), using loglogH0>=s; for bounded k the correction tends to zero.

The terms loga<=Xlog4 and100k^2logT are negligible relative to logf/(k+1) under(6). Therefore, provided the uniform Z_k(X)!=0 input is established,

    logq >=[1-o(1)]log(X!)/(k+1).           (7)

Agent3's complete unbounded-shift error theorem gives

    log|S-c|=-(2k-1)logX+O(klog(k+1)+k^2/X)

in this regime. Combining with(7) would make the complete primitive forms diverge, since X/k^2→infinity. This would exclude slow-growing-dimension, extremely-large-shift branches; it would not exclude M proportional to k or decide the e+pi problem.

Historical dependency resolved: Agent3's UNIFORM_GAMMA_COMPACT_LEADING_NONZERO.md proves Z_k(X) nonzero for every k>=1 and X>=128k. The completed transfer and family exclusion are saved in SHIFTED_SHORT_SLOW_GROWING_DIMENSION_OBSTRUCTION.md. This progress note retains the original threshold derivation; its formerly conditional consequence is now proved in the stated slow-growing regime. No finite atlas replaces the uniform input.
