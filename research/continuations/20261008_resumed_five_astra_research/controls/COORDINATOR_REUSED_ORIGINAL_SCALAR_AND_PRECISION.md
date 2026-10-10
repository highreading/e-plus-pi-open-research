> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Reuse: the original producer scalar and its exact precision budget

Status: recovered established mathematics, 9 October 2026. This note supersedes
the novelty and OPEN labels for the producer scalar in the 08:00 checkpoint,
the A4 turn14 assignment, and the parent alternative Pascal derivation.
The complete old theorem and its DIFFERENT independent audit have been read
in full. No admitted request, historical response, or arithmetic receipt is
rewritten. Research remains active.

## Primary proof and independent audit

The primary source is
`research/continuations/20261005_resumed_five_astra_research/responses/A1_turn9.md`
(all 1234 lines read). Its Theorems 5.1, 7.1 and 11.1 prove the scalar and
precision results. The DIFFERENT audit is
`research/continuations/20261005_resumed_five_astra_research/responses/A4_turn17.md`
(all 895 lines read), Part I, especially sections 2–5. It confirms the actual
shorter residue class, complete-force cancellation, endpoint, and quadratic
precision accounting. The old scalar receipt is not to be recomputed.

The old A1 turn9 explicitly reuses ternary invertibility of the finite
normalized forcing matrix. Thus the current A4 turn13 unit proof and the
modulo9 gamma period are also corroboration of known results, not newly
opened producer problems. Results beyond the scalar's domain must retain
their original-family hypotheses.

## Exact bridge to current notation

Let `n >= 5`, `n = 2 mod3`, `F = (n-1)!`,



$$
T_n[a,b]=\binom{a+b}{a}\gamma_{a+b},\quad
u_a=\frac{F(-2)^a}{a!}\quad(0\le a,b<n),
$$



with the actual recurrence
$\gamma_0=1,\gamma_1=0,\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1}$.
Set $A=n-2$, $b_c=-68-A=-n-66$, and



$$
k_a=\binom{n+a}{a}\gamma_{n+a},\qquad
h=T_n^{-1}k.
$$



The COMPLETE old force is exactly the current force:



$$
t=T_n^{-1}\tau
=3n h+(b_c+6)e_{n-1}+\frac{2b_c}{n-1}e_{n-2}.
$$



No lower-degree term is omitted. In old notation
$\eta_n=F^2-u^TT_n^{-1}u$, $\chi_n=u^Tt$.
In current A4 notation $\Xi=\eta_n$, $\xi=\chi_n/\Xi$. Consequently



$$
\boxed{\Xi\equiv u^Tt\equiv3\pmod9,\quad
v_3(\Xi)=v_3(u^Tt)=1,\quad\xi\in1+3\mathbb Z_3.}
$$



This is proved for ALL `n >= 5, n=2 mod3`. The current original indices
`n=4^j+1`, `j=84645 mod531441`, satisfy these hypotheses. There is no need
to assume a further original low-digit residue to obtain this conclusion.
The exceptional `n=2` is excluded.

The old proof uses the actual residue-class sizes `(N+1,N+1,N)` for
`n=3N+2`, with the finite Pascal vector
$c_i=(-1)^{N-i}\binom Ni$, $w_{3i}=c_i$,
$w_{3i+1}=-c_i$, $w_{3i+2}=0$. It proves
$T_nw=u\pmod3$, $u^Tw=3(N+1)\pmod9$,
$w^TT_nw=6N\pmod9$, then pays the quadratic completion.
The exact complete-force identity is



$$
u^Tt=3n\,u^Th+6u_{n-1}.
$$



These identities and the modulo9 moment recurrence are already proved;
the present continuation should reuse them directly.

## What is now available without another scalar audit

The old independent audit accepts



$$
v_3(\det C_n)=2\sum_{a=0}^{n-2}v_3(a!)+1,
\qquad
\min_{a,b}v_3((\Gamma_n^{-1})_{ab})=-2v_3(F)-1.
$$



The actual endpoint is nonzero:
$Q_n^{\rm loc}(-1)=-F^2\xi$, with valuation $2v_3(F)$.
It must not be replaced by the zero endpoint of the uncorrected core.

Sections 9–11 of old A1 turn9 give a prescribed finite Pascal digit solver,
including the genuinely shorter residue class. If inputs are known modulo
$3^{M+1}$, solution precision
$r=\lceil(M+1)/2\rceil$, together with exact quadratic/bilinear
completion and division by the scalar `Xi/3`, computes `xi mod3^M`.
Section 12 gives the terminal correction budget: inputs modulo
$3^{p+7}$ suffice for $R=\mathcal E_n/3^6\pmod{3^p}$, under
the accepted original-family order-six divisibility and factorial-tail
hypotheses. The state and matrix size still grow with `n`; this is not a
precision-sized original-index algorithm.

In the current A4 turn13 72-coefficient truncation argument the scalar
condition `v3(Xi)=1` is therefore PAID by reuse, rather than OPEN.
The 72 actual coefficients and complete projection are still required.

## Exact remaining research task

The actual degree70 correction `V70`, the complete W-return, and the
actual physical7 prefix contraction remain unevaluated. The target keeps
the literal negative endpoint and highest HIGH coordinate:



$$
\frac{M(\delta Q\,\widehat F_i\widehat F_j)
-b_i^T E_{\rm act}^{-1}b_j}{3^{29}}\pmod3.
$$



The already-paid scalar removes an avoidable source precision uncertainty;
it does not evaluate this contraction. The old observed-support obstruction
continues to apply. A complete core matrix jet modulo81 would still leave
the actual correction unless the latter is separately computed. Actual
all-prime contents, the least clearer, primitive denominator and whole
nonzero-error decay remain open.

The parent `COORDINATOR_ORIGINAL_XI_UNIT_CANDIDATE.md` and its universal
finite receipt remain saved as an alternative corroborating proof for a
smaller original low-digit domain. Their earlier NEW label is superseded
by this recovery. They need not consume another external full-proof audit
or another round of scalar tests.
