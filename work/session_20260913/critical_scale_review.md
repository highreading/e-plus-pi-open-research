> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the critical-scale criterion

Reviewed 2026-09-13. Status: verified auxiliary deductions; the missing assertion about pi is unproved. No claim of novelty or of a solution to the main problem.

## Primary source and scope

C. S. Davis, “Rational approximations to e,” *Journal of the Australian Mathematical Society*, Series A 25 (1978), 497–502, [DOI 10.1017/S1446788700021480](https://doi.org/10.1017/S1446788700021480), [primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0A59D34AF70DE5ED9A5F3FB1E3703976/S1446788700021480a.pdf/rational_approximations_to_e.pdf).

The six-page PDF was downloaded. Theorem 1 and its proof on pp. 498–501 were read, with the mathematical display on p. 498 and proof pages visually checked against the scanned PDF. Theorem 2 about other exponentials is not needed and was not independently verified. The source establishes



$$
\mathcal C(e)=\frac12,\qquad
\mathcal C(x):=\liminf_{q\to\infty}\min_{p\in\mathbb Z}
q^2|x-p/q|\frac{\log q}{\log\log q}.
$$



Its lower bound explicitly quantifies over all integers numerator and denominator, not merely reduced fractions. The proof uses integral approximants, their recurrences, Euler's continued fraction and factorial asymptotics. The project’s independent continued-fraction proof avoids needing to import every intermediate integral identity. For nonconvergents it correctly uses the sufficient general lower bound $1/(2q^2)$; the stronger printed nonconvergent estimate in Davis is unnecessary here. The article is from 1978; its Cambridge online date is not its research date.

Saved PDF: `davis_1978.pdf`, 226381 bytes; SHA-256 `a242afa0ca3509f69d96f995ca705943857b226c3ab2f5b55037c9c0a90442d1`.

## Translation: direct proof, including unreduced fractions

Write $f(t)=\log t/\log\log t$ for sufficiently large $t$. Let $a\in\mathbb Z$, $b\ge1$ be fixed, and $\alpha=a/b-e$. For every integer $p$, positive integer $q$,



$$
|\alpha-p/q|=\left|e-\frac{aq-bp}{bq}\right|.
$$



For every $c<1/2$, Davis's lower bound applied at the *possibly unreduced* denominator $bq$ implies



$$
q^2|\alpha-p/q|f(q)\ge\frac{c}{b^2}\frac{f(q)}{f(bq)}.
$$



Since $f(bq)/f(q)\to1$, the quantifiers are uniform in $p$, and therefore



$$
\boxed{\mathcal C(a/b-e)\ge\frac1{2b^2}.}
$$



This is the recommended proof. Reduction is not needed.

For comparison, a reduced-fraction proof is also valid, but the original gcd assertion requires $\gcd(p,q)=1$. If additionally $\gcd(a,b)=1$, put $g=\gcd(aq-bp,bq)$. Then



$$
g\mid\gcd(bq,b^2p)=b\gcd(q,b)\mid b^2,
\qquad Q=bq/g\in[q/b,bq].
$$



This verifies the proposed reduction and the constant. Without reduced $p/q$, the divisibility $g\mid b^2$ is false: take $a=b=1,p=q=2$, giving $g=2$. The direct proof already handles that case.

There is also a useful upper complement. Choose Davis's sequence $P_n/Q_n$ for which $Q_n^2|e-P_n/Q_n|f(Q_n)\to1/2$. The fractions



$$
\frac{aQ_n-bP_n}{bQ_n}
$$



approximate $\alpha$, so their weighted error at denominator $bQ_n$ tends to $b^2/2$. Thus



$$
\boxed{\frac1{2b^2}\le\mathcal C(a/b-e)\le\frac{b^2}{2}.}
$$



Neither endpoint is claimed to be sharp for each individual rational translation. The consequence is that either $\mathcal C(\pi)=0$ **or** $\mathcal C(\pi)=+\infty$ would prove $e+\pi$ irrational. A hypothetical rational sum forces a finite, strictly positive critical-scale constant. This complement does not prove either alternative for pi.

## Continued fractions and exact quantifiers

For an irrational $x=[a_0;a_1,a_2,\ldots]$, write $p_k/q_k$ for its principal convergents. The exact error formula gives



$$
q_k^2|x-p_k/q_k|=\frac1{D_k},\qquad
D_k=[a_{k+1};a_{k+2},\ldots]+q_{k-1}/q_k,
\qquad a_{k+1}<D_k<a_{k+1}+2.
$$



Consequently the weighted convergent error has zero liminf exactly when



$$
\limsup_{k\to\infty}\frac{a_{k+1}}{f(q_k)}=+\infty.
$$



This is also equivalent to $\mathcal C(x)=0$ over all rational approximations. In the forward direction, a sequence of weighted errors tending to zero has unweighted $q^2$-error tending to zero. Reduce its fractions first. The function $t^2f(t)$ is increasing for all sufficiently large $t$, so reduction cannot increase the weighted error once the reduced denominators are large. Those denominators must tend to infinity: approximation to an irrational by fractions of bounded reduced denominator cannot have error tending to zero. Legendre's criterion then makes each sufficiently late fraction a principal convergent. The reverse implication simply uses the convergents as an admissible sequence in the liminf.

The exact sufficient statement for the zero alternative is therefore



$$
\boxed{\forall C>0\ \exists\text{ infinitely many }k:
 a_{k+1}(\pi)>C\frac{\log q_k}{\log\log q_k}.}
$$



This statement is equivalent to $\mathcal C(\pi)=0$, and sufficient for irrationality of the sum. It is **not** asserted to be equivalent to irrationality of the sum. Bare unboundedness of the partial quotients is weaker and does not supply the moving threshold. Conversely, bounded partial quotients would make $\mathcal C(\pi)=+\infty$, so would also imply irrationality by the upper complement. Neither property has been established here. More generally $a_{k+1}/f(q_k)\to0$ would give the infinite alternative.

## Check of the root's written independent proof

Read all of `critical_scale_criterion.md`, including its reduction, continued-fraction equivalence, independent lower-bound derivation and content-threshold connection. No mathematical correction was needed.

The index $k=\lfloor(n+1)/3\rfloor$ counts exactly the large Euler partial quotients $2,4,\ldots,2k$ occurring by index $n$. Thus



$$
q_n\ge2^k k!,\qquad a_{n+1}\le2(k+1),\qquad
q_n\le\prod_{j=1}^n(a_j+1).
$$



The product bounds imply $\log q_n=k\log k+O(k)$; their inversion yields $k\sim f(q_n)$. Along indices $n=3k+1$, the next partial quotient is $2(k+1)$, and the exact error formula makes the normalized error tend to $1/2$. At every index, the upper bound on $a_{n+1}$ gives the lower half. Nonconvergents are covered by Legendre's inequality. For unreduced fractions the decreasing function $1/(t^2f(t))$ transfers the lower bound from the reduced denominator to the supplied denominator; bounded reduced denominators are handled separately. No numerical extrapolation is involved.

For an integer pi-form $U_m+V_m\pi$ with $V_m\ne0$, set $c_m=\gcd(U_m,V_m)$, $b_m=|V_m|/c_m$. The reduced rational approximation has weighted error exactly



$$
\frac{|V_m|\,|U_m+V_m\pi|}{c_m^2}f(b_m).
$$



Under the archive convention
$\log|V_m|/(6m)\to h$,
$\log|U_m+V_m\pi|/(6m)\to h-d$,
its exponential part is $2h-d-2\log c_m/(6m)$. This confirms the threshold $\log c_m/(6m)>h-d/2$. At exact equality the logarithmic/lower-order terms and $b_m\to\infty$ matter. The criterion supplies neither the necessary gcd growth nor any cancellation estimate.

## Prior archive coverage and literature barrier

The archive search found no existing Davis citation. This is a search result, not a claim of global bibliographic originality. Two earlier notes overlap materially:

- `sources/algebraic_translation_approximation_no_go.md`, especially its eq. (10), derives a coarser bound $c/(q^2\log(2q))$ from Euler's continued fraction and explains the exponent-two obstruction.
- `sources/common_kernel_factorial_window_cf_entry_dichotomy.md`, eq. (13), already obtains the scale $\log\log q/(q^2\log q)$ for hypothetical infinitely many low factorial-window entries for $x=e+\pi$. Its estimate has a fixed constant; it neither gives the all-constant zero-liminf statement for $\pi$ nor proves that its low entries occur infinitely often. Its high-entry alternative and golden-ratio countermodel explicitly prevent that inference.

Michel Waldschmidt's [WAMS Erbil lectures, March 12–17, 2017](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/WAMS2017Erbil1.pdf), PDF pp. 98–99, identify boundedness of pi's partial quotients as an open problem. The exact relevant slides were extracted and checked; the other 137 slides were not comprehensively audited. This is a historical primary expert statement. Andrew Granville's [“Missing digits, and good approximations”](https://dms.umontreal.ca/~andrew/PDF/Maynard.BAMS.pdf), pp. 24–25, likewise describes the problem of good approximations to pi as open and discusses metric approximation results. Almost-everywhere theorems do not decide a named constant.

The separate full-PDF review `literature_pi_20260910.md` treats published Zeilberger–Zudilin and the new Bai preprint. Their irrationality-measure upper bounds restrict excessively good approximations; they do not construct the infinitely many approximations required above. None of the primary sources reviewed supplies the moving-threshold lemma for pi. This is a literature-search conclusion, not a proof that no such theorem exists anywhere.

The most useful next mathematical step is a pi-specific approximation construction or theorem yielding one of the two critical-scale extremes, with all infinite quantifiers proved. Finite continued-fraction data can test conjectures but cannot fill that gap. In the current mixed-cubic construction, the concrete intermediate problem remains additional provable integer content at or beyond the recorded threshold, with the lower-order factors and nonvanishing checked.
