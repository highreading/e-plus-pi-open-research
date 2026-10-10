> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact-monodromy, zero-order correction: a scoped Genesis bridge filter

Status: proved countermodel, not a retained new irrationality route or claimed new interpolation paradigm. The actual main problem remains open. This strengthens the earlier finite logarithmic-jet countermodel by preserving the COMPLETE monodromy increments, rather than finitely many local singularity coefficients.

## Candidate and required gate

Candidate claim tested: a rational-coefficient analytic germ with the same complete additive monodromy as F(z)=exp(z)+4 atan(z), the same leading exponential behavior in every closed right sector, any prescribed finite origin jet, and positivity on [0,1] cannot have rational endpoint value at1.

Archive searches used Staeckel/Stackel, rational Taylor coefficients/entire functions, zero-order perturbation, superexponential interpolation, and monodromy-preserving perturbation. They found Agent3's `GENESIS_ANALYTIC_CANDIDATE_LEDGER.md` A3 and its cited archived exact-jet source. A3 preserves FINITE logarithmic jets; its polynomial multiplier changes the whole monodromy increment. The stronger complete-monodromy construction below was not present in those inspected notes. This is a bounded archive result.

Fresh primary reads: https://arxiv.org/pdf/2306.03281, especially the introduction and Lemma1 on public rational-coefficient entire interpolation; https://arxiv.org/pdf/2305.13461, especially Theorem1 and its all-rational-input denominator hypotheses. A zero-order interpolation PDF link on mathnet failed to fetch and is NOT claimed as read. Entire interpolation is established background. The mechanism is not retained as a Genesis tool, irrespective of whether this exact specialization was previously written down.

## Exact correction lemma

For every real v and every integer J>=0 there is an entire H with rational Taylor coefficients, H^(j)(0)=0 for0<=j<=J, and H(1)=v. Moreover

    log max(1,M_H(R)) = O_v,J(log R log log R),  R>=e^2.

Here M_H(R)=max_|z|<=R |H(z)|. Consequently H has order at most zero, in the usual convention covering polynomials and the zero function. If v>=0, all coefficients of H can be chosen nonnegative.

Proof. Set K_n=2^(n+3) and q_n=2^(-K_n) floor(2^(K_n)v). Then q_n is rational and

    0 <= v-q_n < 2^(-K_n).

The nested dyadic grids imply q_n>=q_(n-1). Put d_0=q_0 and d_n=q_n-q_(n-1) for n>=1, and define

    H(z)=z^(J+1) sum_(n>=0) d_n z^n.

For n>=1,

    0 <= d_n <= 2^(-K_(n-1)) = 2^(-2^(n+2)).

This bound proves normal convergence on every compact subset of C and hence entire continuation. The endpoint sum telescopes to lim q_n=v. The factor z^(J+1) gives the origin jet. If v>=0, d_0>=0 as well, proving coefficient positivity.

For the quantitative growth bound let L=log R and N=ceil(2 log_2(L+2)). The first N+1 summands have total at most |q_0|+(N+1)R^N. For the majorizing terms T_n=R^n 2^(-2^(n+2)), n>=N, the ratio T_(n+1)/T_n=R 2^(-2^(n+2)) is below1/2. Thus the remaining majorant is at most2R^N. Multiplication by R^(J+1) gives log max(1,M_H(R))=O_v,J(L log L). This proves the lemma without invoking a general interpolation theorem.

## Application preserving the complete complex branch increments

Let S=e+pi and choose any rational r. Apply the lemma to v=r-S and put G=F+H on the branch real on [0,1]. Then:

1. G has rational Taylor coefficients and agrees with F through order J at0.
2. G(1)=r EXACTLY. The construction uses an arbitrary real value v; it does not assume S is irrational or use the desired conclusion.
3. H is single-valued entire. Therefore for EVERY continuation loop avoiding plus/minus i, the additive branch increment of G is EXACTLY that of F. In particular the two elementary loops have increments plus/minus4pi, with orientation/sign chosen consistently. The full logarithmic local coefficients, branch points, and derivative residues are unchanged.
4. In every closed sector |arg z|<=pi/2-epsilon, H(z)=exp(o(|z|)) uniformly. The arctangent contribution has at most logarithmic growth on a fixed continuation in that sector away from its finite branch points. Hence G(z)/exp(z)->1 uniformly as |z|->infinity in that sector. This preserves the full LEADING exponential asymptotic there, not just its indicator.
5. For r>S the coefficients of H are nonnegative. Thus H(x)>=0 and H'(x)>=0 on [0,1], and G'(x)=exp(x)+4/(1+x^2)+H'(x)>0. Also G(0)=1. The positive rational-coefficient density G' has rational total mass r-1 on [0,1].

There is an unconditional convenient rational choice r=6. The exponential tail after degree2 is bounded by (1/6)/(1-1/4)=2/9, giving e<49/18<11/4. The alternating arctangent upper sum through j=10 gives pi<4 sum_(j=0)^10 (-1)^j/(2j+1)<13/4. Therefore S<6 and the coefficient-positive countermodel applies with endpoint6, for every J.

## Scope and consequence

The candidate rigidity claim is false even with complete monodromy, leading right-sector exponential asymptotics, rational Taylor coefficients, arbitrarily many origin jets and a positive increasing real branch. A future new numerical bridge must use information not captured by these signatures.

This correction does not claim to preserve F's exact rational differential equation, its full Taylor sequence, arithmetic denominator-growth restrictions, a complete Stokes datum of a fixed differential module, or the actual exponential function exp(z). It therefore does not imply that all analytic approaches fail, and it is not a counterexample to any theorem with those stronger hypotheses. Entire interpolation remains credited public background; this is a specific derived exclusion used to guide the human-authorized Genesis research.
