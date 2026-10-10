> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 163 independent cross-audit: matching adversary package

Date: 2026-08-29 (Beijing time)

## Verdict

**FINAL PASS.** The central divisibility theorem, the small-index capacity
no-go, the antiperiod-block span bound, the balanced-scale constants, and every
reported finite count replay correctly. All issues found in the initial audit
were corrected, the checker was rerun byte-deterministically, and the final
manifest is internally consistent. The package does not prove irrationality or
rationality of $e+\pi$.

## Files audited and current hashes

| file | SHA-256 |
|---|---|
| `work/item163_match_adversary_report.md` | `1c0045cf28e78aa6685c2f1337f993f9aa0aa4eeab02851b8cb7c86cf46ff54a` |
| `work/item163_match_adversary_check.py` | `281e1fd209b5d7150182153d5e87852255d8ba87cf86dd473c022bcb2aead0cc` |
| `work/item163_match_adversary_certificate.json` | `f76fc492f86a3db3ce199c069b65db7d7985e1f017718e852f43160b6b226c32` |
| `work/item163_match_adversary_hashes.sha256` | `9b8481dc83098b7382cd3f974211373e0630aeea3181a5038c9e574ccec46fc7` |

The checker independently verified all six Desktop input pins. Re-running it
reproduced the certificate byte for byte with SHA-256
`f76fc492f86a3db3ce199c069b65db7d7985e1f017718e852f43160b6b226c32`.
The three entries in the supplied hash manifest all match their files.

## Independent derivation of the capacity claims

Let



$$
\Delta=\gcd(b,q_N),\qquad b=\Delta b_0,\qquad q_N=\Delta q_0,
$$



and $g=\gcd(P^*,\Delta)$. Since $g\mid\Delta$,



$$
\Delta g\mid\Delta^2=\gcd(b,q_N)^2.
$$



As $\Delta\mid b$ and $\Delta\mid q_N$, this also gives



$$
\Delta g\mid b^2,\qquad \Delta g\mid q_N^2,
$$



and hence



$$
\log(\Delta g)\le 2\min\{\log b,\log q_N\}.
$$



If $|V|=cb$, then



$$
|V|q_N=c\Delta^2b_0q_0
$$



is divisible by $c\Delta g$. This independently recovers every claimed
global divisibility.

For $N\ge2$, induction from the recurrence gives



$$
q_N<4^{N-1}N!,
$$



while the product of the recurrence's positive leading terms gives the
matching lower order; consequently $\log q_N=N\log N+O(N)$. Thus
$N_m\log N_m=o(m)$ implies $\log(\Delta g)=o(m)$. If a squarefree
family $\mathcal S_m$ is forced into $\Delta$, then



$$
\prod_{p\in\mathcal S_m}p\mid q_N,
 \qquad
 \sum_{p\in\mathcal S_m}\log p\le\log q_N,
$$



so the stated prime-mass floor is correct.

Primewise, if $B=v_p(b)$ and $Q=v_p(q_N)$ are unequal and positive,
division by $p^{\min(B,Q)}$ makes exactly one term in $P^*$ a unit and
the other a multiple of $p$. Hence $v_p(g)=0$. If $B=Q>0$, then



$$
v_p(g)=\min\{B,v_p(P^*)\}.
$$



This verifies the equal-valuation condition used by the checker.

The sharpness example at $N=2$ is exact. In fact the exponent-two envelope
is asymptotically sharp in the abstract class: for every even $N$, taking
$\varepsilon=1$ and $(a,b)=(p_N,q_N)$ gives a primitive positive form,
$P^*=0$, and $\Delta g=q_N^2$.

## Independent derivation of the antiperiod span theorem

For each distinct odd prime $p$ and $1\le k_p<p/2$, the archived
all-even antiperiod theorem gives, pointwise in the base index,



$$
p^{k_p}\mid(1+S^p)^{2k_p}q.
$$



The shift polynomials commute and have integer coefficients. Applying every
other block preserves the displayed divisibility, and coprimality of the
distinct primes yields



$$
D=\prod_p p^{k_p}\mid
 \left(\prod_p(1+S^p)^{2k_p}q\right)_N.
$$



The forward span is $W=\sum_p2k_pp$. Because $\log x/x$ is decreasing
for $x\ge3$,



$$
\frac{k_p\log p}{2k_pp}=\frac{\log p}{2p}
 \le\frac{\log3}{6}.
$$



Summation gives the claimed sharp method-level bound



$$
\log D\le\frac{\log3}{6}W.
$$



If all actually used forward indices remain $O(m/\log m)$, the nonzero
top-shift coefficient forces $W=O(m/\log m)$, and therefore
$\log D=o(m)$. Primitive reduction can only remove forced raw content.
Even granting complete survival and a second copy through $g$ leaves
$2\log D=o(m)$. The report's scope for repeated same-prime blocks is also
properly cautious.

Besides the package's 33 product checks, an independent implementation tested
3,276 individual $(p,k,N)$ cases for all odd primes below 50 and 153 new
multi-prime product cases; all passed.

## Constants and exact finite replay

Independent 100-digit decimal evaluation gives



$$
r_1=0.136514168294812818450423822617\ldots,
$$





$$
T_1=1.019632983669431793880306401240\ldots,
$$





$$
\frac{T_1}{\theta}
 =0.872576611438626561637682081243\ldots,
 \qquad
 \frac{T_1}{2\theta}
 =0.436288305719313280818841040621\ldots.
$$



An independent recurrence/factorization replay, which did not import the
package checker, reproduced:

- 15,150 parity-compatible candidates and 100 stored maxima;
- 6,057 candidates with nontrivial equal-valuation ceiling;
- 7,393 equal-valuation prime slots;
- 234 candidates with $g>1$ and 236 prime slots entering $g$;
- largest $\Delta=596038519=31\cdot97\cdot379\cdot523$ at
  $(m,N)=(92,544)$, with $g=1$;
- largest $g=1133=11\cdot103$ at $(m,N)=(91,455)$, with
  $\Delta=12463$;
- exactly ten $p>6m$ candidate-prime events, with unique primes
  $31,97,173,691,797$, and no such event entering $g$;
- every repeated-maximizer group and every ten-row block statistic in the
  certificate;
- the last-twenty means
  $0.1845733550,0.0303135500,0.0017099311,0.0320234811,0.2165968361$.

The percentages $234/6057=3.863298662704\ldots\%$ and
$236/7393=3.192208846206\ldots\%$ are correct.

## Corrections verified as resolved

The corrected package now has valid `\quad` TeX, qualifies the factorial
bound by $N\ge2$, uses the right references to (20) and (21), scopes the OPEN
upper-bound statement below the universal $2\log q_N$ capacity, separates
first-level singular-prime abundance from deeper all-lift/Wieferich behavior,
and removes the stale factorizer-size comment. The same scope corrections are
present in the regenerated JSON certificate.

## Formatting audit

The report has balanced inline delimiters (83 opening and 83 closing), balanced
display delimiters (37 and 37), balanced code fences, sequential equation tags
1 through 21, valid UTF-8, and no forbidden control bytes. The checker, JSON,
and manifest also contain no forbidden control bytes. No remaining malformed
TeX or stale equation reference was found.

## Final scope judgment

The corrected item is suitable for archival as a rigorous
capacity/no-go result plus exact finite diagnostics. It does not establish an
actual asymptotic matching rate, does not exclude a route-closing matching
theorem special to the mixed-cubic coordinates, and does not settle
$e+\pi$.
