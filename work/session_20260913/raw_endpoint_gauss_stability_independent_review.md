> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of Gauss stability and the exact 17-adic endpoint depth

Date: 2026-09-13. Reviewer: audit_results.

Target: raw_endpoint_gauss_stability_and_exact_17_depth.md, original
Sections 1–5, plus the explicitly identified reviewer addendum in
Section 6. The preceding endpoint restriction has independently passed
raw_endpoint_scalar_cauchy_independent_review.md.

**Verdict: FULL PASS.** The constant-term normalization, Frobenius
lifting, limit precision, actual endpoint transfer, and infinite
17-adic conclusion all hold. I independently reproduced all 35 terms
of the single predeclared $A_{68}\bmod289$ certificate, including
its normalized residue and the binomial-unit entry.

The only scope clarification was to state $m\ge1$ explicitly in
the endpoint application; the pure sequence congruence may also
include $m=0$. The correctly unresolved $\nu=1$ endpoint case
remains excluded from the exact-depth conclusion.

## 1. Exact sequence normalization

The standard monic normalization is


$$
Q_n(x)=\frac{i^nP_n(x/i)}{2^{-n}\binom{2n}{n}}.
$$


Using the ordinary Legendre generating function or expanding its
constant-term formula gives exactly (3). The possible sign of the
square root does not affect a constant term: only an even number of
the nonconstant summands survives. Their expansion is precisely
the positive integer sum (2).

An independent check avoids all complex factors. Rodrigues gives


$$
\binom{2n}{n}Q_n(1)
=\frac1{n!}\left.\frac{d^n}{dx^n}(1+x^2)^n\right|_{x=1}
=[t^n](t^2+2t+2)^n
=\operatorname{CT}(2+t+2/t)^n.
$$


The substitution $t=\sqrt2z$ recovers the symmetric expression.
This proof is now included as the alternative in Section 6.

## 2. Frobenius and prime-power lifting

For odd $p$, the quadratic algebra
$\mathbb Z_p[t]/(t^2-2)$ is free with basis $1,t$.
The map $t\mapsto\chi t$, $\chi=(2/p)$, is an automorphism;
modulo $p$, Euler's criterion gives $t^p=\chi t$.
It is therefore the Frobenius on the whole residue algebra, in
both the split and nonsplit cases.

If $U-V\in p^sR$, $s\ge1$, each term in the binomial expansion
of $U^p-V^p$ belongs to $p^{s+1}R$: the intermediate binomial
coefficients contain $p$, and the final term contains $p^{sp}$.
This argument applies to the Laurent-polynomial algebra as well.
Iteration followed by the $m$-th power proves the exact modulus
in (4).

Constant-term extraction commutes with the coefficient automorphism
and is unchanged by $z\mapsto z^p$. Its value $A_n$ is an
ordinary integer, so it is fixed by the automorphism. Freeness of
the quadratic algebra makes $p^rR\cap\mathbb Z_p=p^r\mathbb Z_p$.
Thus the descent of divisibility is valid.

Alternatively, the integer Laurent form above uses
$f(t)^p\equiv f(t^p)\pmod p$ and the same lifting argument,
without any quadratic algebra. Both proofs give the claimed result.

The cited terminology is accurate: Beukers–Houben–Straub define
these Gauss congruences and develop a Frobenius-lift framework;
Mellit–Vlasenko prove stronger constant-term congruences under an
explicit Newton-polyhedron condition. Neither stronger theorem nor
a limit-nonvanishing claim is used in this proof.
Sources checked directly:
[Beukers–Houben–Straub](https://arxiv.org/pdf/1710.00423),
[Mellit–Vlasenko, Theorem 1](https://arxiv.org/pdf/1306.5811).

## 3. Exact limit precision and stability threshold

The difference between successive indices $r-1,r$ is divisible
by $p^r$. The sequence is consequently Cauchy, and the entire
tail after index $\nu$ lies in the closed ideal
$p^{\nu+1}\mathbb Z_p$. This proves (5), including $\nu=0$.

If $v_p(A_{mp^{r_0}})=e\le r_0$, the error to the limit has
strictly larger valuation, so the limit and every subsequent term
have valuation $e$. If the limit vanishes, (5) gives the stated
lower bound $\nu+1$ for the sequence terms. The real positivity
of the integers does not imply a nonzero $p$-adic limit.

## 4. Actual endpoint transfer and all retained units

For the saturated family $n=mp^\nu$, $1\le m$, $3m<p$,
the first $n$ Cauchy rows have a unit determinant modulo $p$.
Their exact determinant, after accounting for column reversal
and the signs of the Legendre norms, is


$$
L_{3n}^n\prod_{j<n}|h_j^{\rm Leg}|.
$$


This proves that the *whole* prefactor is a $p$-unit. It does
not require individual Legendre norms to be units, and the proof
does not make that incorrect assertion.

Since $2m<p$, Legendre's factorial formula gives
$v_p((2n)!)=2v_p(n!)$. Thus $\binom{2n}{n}$ is also a unit.
The exact endpoint congruence from the preceding note therefore
becomes $K_n\equiv U_nA_n\pmod{p^\nu}$, with $U_n$ a unit.
Its possible variation with $n$ has no effect on valuations.

The independently proved identities


$$
v_p(d_n^{II})=v_p(K_n),\qquad
v_p(Z_n)=\frac{n-m}{p-1}+v_p(K_n)
$$


then give (9) for $\nu>e$. The strict inequality matters:
knowledge modulo $p^\nu$ cannot resolve a residue whose valuation
is exactly $\nu$. The zero-limit alternative (10) gives only a
lower bound, as stated.

The review addendum sharpens this to the exact truncated identity


$$
\min\{v_p(d_{mp^\nu}^{II}),\nu\}
=\min\{v_p(A_{(m,p)}^\infty),\nu\},
\qquad \nu\ge1,
$$


where $v_p(0)=\infty$. This follows by applying the two preceding
congruences successively and makes no nonvanishing assumption.

## 5. The single certificate and the infinite family

The independent calculation used


$$
\sum_{j=0}^{34}
\binom{68}{2j}\binom{2j}{j}2^{68-j}\pmod{289},
$$


with exact integer binomial coefficients and modular powers.
No factorial inverse or modular division was used. Every term
matches the saved list, its sum is $136$, its quotient by $17$
modulo $17$ is $8$, and
$\binom{136}{68}\equiv2\pmod{17}$.
The separate verification record is
endpoint_gauss_17_independent_certificate_check.json.

Thus $r_0=e=1$ certifies a limit of valuation one, and the actual
endpoint congruence gives, for every $\nu\ge2$,


$$
v_{17}(d_{4\cdot17^\nu}^{II})=1,\qquad
v_{17}(Z_{4\cdot17^\nu})=\frac{4\cdot17^\nu-4}{16}+1.
$$


Adding the independently known extremal-content valuation gives
(13) with its additional $+1$.

At $\nu=1$, the result remains only
$v_{17}(d_{68}^{II})\ge1$. The certificate for $A_{68}$ does
not delete the factorial-difference corrections in $K_{68}$,
so promoting this boundary case to exact valuation would be
unjustified. The note and its addendum correctly preserve that
distinction.

This is a proved fixed-prime infinite-family endpoint result.
It does not identify the simultaneous coefficient denominator
with the selected type-I primitive denominator, nor establish
the rationality or irrationality of $e+\pi$.
