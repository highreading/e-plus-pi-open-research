> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Genesis analytic candidate ledger

Date: 2026-10-02. Agent 3. This is an original-research screening record, not an independent review and not a proof about the rationality of e+pi.

The active protocol is `main/GENESIS_STAGE_PROTOCOL.md`. Every mechanism must have an exact rationality bridge, an archive check, fresh searches under mechanism synonyms, and opened primary sources. An essential public equivalent causes immediate rejection even if it remains unresolved. An unsuccessful bounded search never establishes global novelty.

## A1. Nested-exponential zero rigidity — discarded

Proposed object: the entire nested exponential function exp(i b exp(z)), compared at z=1 with exp(i a), for integers a and b>0. If S=e+pi=a/b, the EXACT identity is

    exp(i b e)=(-1)^b exp(i a).

This does NOT say exp(i b e) is algebraic. Replacing its right side by (-1)^a would be an incorrect normalization. A hoped-for zero exclusion for this identity would be an iterated-exponential algebraic-independence assertion. The falsifiable target would exclude this equality for every integer pair a,b; proving that target by assuming the relevant independence is circular for this use.

Archive queries: `Schanuel|nested exponent|iterated exponent|exponential polynomial|composition.*exponent` across the full research directory. Opened `sources/nested_multi_exponential_hp_norm_barrier.md`, sections 1–2, and `sources/exponential_theorem_audit.md`, sections 1–2. The former already uses the same exact Euler substitution exp(i e/N)=zeta^(-1)exp(i S/N), and explains why auxiliary small values are transcendental rather than number-field norms. The latter records compatible nested-exponential consequences of assuming algebraic S.

Fresh online queries:

- `iterated exponential algebraic values exp i e Schanuel conjecture e pi irrational sum`
- `exponential arctangent algebraic values e plus pi transcendence mixed E G functions`
- `Cheng Dietel Herblot Huang Krieger Marques Mason Mereb Wilson algebraic independence iterated exponentials logarithms Schanuel paper`
- `exponential sine composition rational zeros Schanuel exp exp polynomial primary`

Primary sources opened:

- Cheng et al., *Some consequences of Schanuel's Conjecture*, https://arxiv.org/pdf/0804.3550. Theorem 1 and Corollaries 2–4 explicitly cover the exponential/logarithmic tower separation mechanism conditionally on Schanuel.
- Scanlon, *Model theoretic origins and approaches to unlikely intersection problems*, AWS 2023 notes, https://swc-math.github.io/aws/2023/2023ScanlonNotes.pdf. Sections 2 and 4 set out the existing exponential-field and differential Ax–Schanuel programs.

Verdict: discarded at the gate. The essential mechanism is already public and also archived. No new zero-exclusion lemma is developed under this label. This rejection is about the mechanism, not a purported global impossibility theorem.

## A2. Endpoint division followed by a natural-boundary test — discarded

Object: F(z)=exp(z)+4 atan(z), with the branch real on [0,1]. If S=r is rational, then G_r(z)=(F(z)-r)/(z-1) has rational Taylor coefficients at 0 and its principal continuation is removable at 1. A proposed Borel/Hadamard operation would turn its coefficients into an integer series with an analytic arc of continuation; a Carlson–Pólya theorem would then force rationality of that transformed series.

The exact rationality bridge is valid only through removability of the PRINCIPAL branch. It does not supply integer coefficients of any transformed series. More importantly, the essential analytic/arithmetic mechanism is the public Carlson–Pólya natural-boundary criterion, whose proof uses integer Hankel determinants. It is disallowed by the Genesis mechanism gate, independently of the missing integer-coefficient implication.

Archive searches: `P[oó]lya.{0,3}Carlson|natural boundary|Hadamard product|Borel transform|rational endpoint division|inverse branch|Lagrange inversion|exceptional set`. Opened `sources/e_function_logarithm_exceptional_set_no_go.md` and `work/session_20260913/raw_borel_legendre_literature.md`; their Borel/exceptional-point mechanisms and old raw transform families are credited, not renamed.

Fresh queries: `Pólya Carlson theorem rational power series Borel transform arithmetic entire functions Hadamard product`; `inverse function arithmetic power series algebraic values exponential logarithm Lagrange inversion transcendence`; `F Carlson Über Potenzreihen mit ganzzahligen Koeffizienten 1921 pdf`. Opened https://people.math.ethz.ch/~airibar/Polya_Carlson.pdf, including its self-contained account and appended English translation of Carlson's original paper. A later positional fetch failed and supplies no additional claim. The initial fetch and the search engine's extracted original-paper text expose the same mechanism. Verdict: discarded; no transformed integer-series claim is made.

## A3. Finite singularity/jet rigidity — falsified, discarded

Falsifiable target considered: rational Taylor coefficients, exponential growth in the right sector, a prescribed finite origin jet, and the fixed logarithmic singularities at ±i with prescribed finite leading logarithmic jets should forbid a rational value at 1. The intended bridge would apply this target to F(1)=S. The target is false.

Here is an explicit operation testing it. For arbitrary nonnegative integers J,L and an arbitrary rational r, put

    B(z)=z^(J+1)(1+z^2)^(L+1)/2^(L+1),
    F_r(z)=(1-B(z))F(z)+r B(z).

Then B(1)=1, B has a zero of order J+1 at 0 and a zero of order L+1 at each of ±i. Consequently:

1. F_r has rational Taylor coefficients and agrees with F through order J at 0.
2. F_r(1)=r EXACTLY.
3. Write F=A_±(z)+c_± log(z∓i) locally near each logarithmic singularity. The coefficient of the logarithm in F_r is c_±(1-B(z)), so its Taylor jet agrees with c_± through order L at the corresponding point. The branch points and their nonzero leading logarithmic coefficients remain present.
4. In every fixed closed sector |arg z|≤pi/2−epsilon, the nonzero polynomial multiplier (1-B) changes exp(z) only by a polynomial factor. Thus the exponential indicator there remains cos(arg z), while the logarithmic part is polynomial times log(z). No finite right-sector exponential-growth signature excludes rational endpoints in this class.
5. If r>S, the countermodel also preserves strict monotonicity and positivity on [0,1]. Indeed 0<=B<=1 and B'>0 on (0,1], F'>0, and r-F>0, so F_r'=(1-B)F'+B'(r-F)>0. Also F_r(0)=1. Thus its positive analytic density F_r' has rational mass r-1. Positivity of a mixed analytic normalization does not repair the failed target.

Proof: the displayed zero orders and endpoint evaluation give 1–3. Along a right-sector ray the exponential term dominates every polynomial times logarithm, and the logarithm of the absolute polynomial multiplier divided by the radius tends to zero; this proves 4. The explicit derivative proves 5. This is a countermodel operation, not a new irrationality tool, and does not preserve the exact differential equation of F.

The archive search in A2 also found `sources/independent_mixed_e_g_logarithm_value_audit.md`, which records exact-jet interpolation issues. Fresh synonym queries included `entire functions rational Taylor coefficients prescribed rational values interpolation transcendental exceptional sets`. Opened primary sources:

- Alves–Lelis–Marques–Trojovský, *On the exceptional set of transcendental entire functions in several variables*, https://arxiv.org/pdf/2306.03281, Introduction, Lemma 1 and Theorems 1–2. Arbitrary exceptional-set interpolation with rational coefficients is a public mechanism; this note makes no novelty claim for polynomial interpolation.
- Lelis–Marques–Moreira–Trojovský, *A note on transcendental analytic functions with rational coefficients mapping Q into itself*, https://arxiv.org/pdf/2305.13461, Theorem 1 and its proof. Their genuine rigidity requires rationality at ALL rational points with denominator bounds and uses Padé approximation. Rationality at the single point 1 supplies neither hypothesis and that method is not retained here.

Verdict: discard any proposed obstruction using only the listed finite analytic signatures. A stronger future operation must explicitly use information the displayed deformation does not preserve. This is a scoped counterexample, not a theorem that analytic structural methods cannot solve the original problem.

## Current boundary

A4, the nonlocal rational-entry spectral candidate, is recorded separately in `GENESIS_SPECTRAL_EDGE_COUNTERMODEL.md`. Its exact top edge is S; both proposed auxiliary rigidity bridges are false. The irrationality route has been discarded.

Further analytic candidates must distinguish a genuine new operation from a reformulation of one endpoint equality or an assumption of independence. In particular, a proposed functional rigidity theorem must survive explicit analytic countermodels with rational endpoint sums before it is retained.
# A5. Global reciprocal-residual transform — discarded at the mechanism gate

Consider a fixed rational partial-sum sequence s_n tending to S and the global operation T_r(z)=sum_n z^n/(r-s_n), omitting any zero coefficient. Its exact numerical bridge is modest: if r=S is rational, all coefficients are rational and their asymptotics are reciprocal tail asymptotics; if r differs from S, coefficients approach a nonzero constant. A proposed analytic obstruction would need to rule out the former singular behavior from coefficient arithmetic. This is a Hadamard-quotient/rationality mechanism, already public, not a retained Genesis tool.

Archive query: `Hadamard.{0,40}(inverse|reciprocal)|reciprocal.{0,40}(partial sum|residual|coefficient)|residual.{0,40}(generating|natural boundar)|coefficientwise.{0,40}(reciprocal|inversion)`. Matches included old all-jet resolvents, CONTACT_INVERSE_RESEARCH.md, and the already discarded Carlson/Hadamard gate. No exact reciprocal-endpoint-tail transform was located in the bounded query, which does not imply novelty of the essential operation.

Fresh queries: `Hadamard reciprocal partial sums power series natural boundary coefficientwise inverse`; `reciprocal tail generating function partial sum analytic continuation irrationality`; `Hadamard quotient theorem rational coefficients factorial sequences reciprocal`.

Opened primary sources: Dimitrov, [A note on a generalization of the Hadamard quotient theorem](https://arxiv.org/pdf/1309.1920), full 23-page paper, especially Theorem 1.4 and Conjecture 1.8(i) covering general G-series quotient/height rigidity, and van der Poorten, [Hadamard operations on rational functions](https://www.numdam.org/article/GAU_1982-1983__10_1_A3_0.pdf), full 12-page primary lecture paper. The rational-function Hadamard quotient theorem and its public generalized program are the essential proposed tool. Rational coefficients alone do not supply their finite-generation, height, or algebraicity hypotheses.

An elementary countermodel isolates this gap. Set s_n=1-(n+1)/(n^2+2). It is a rational sequence tending to the rational endpoint 1, with positive tail. The reciprocal residual is

    1/(1-s_n)=n-1+3/(n+1).

For n+1 equal to any prime other than 3, this coefficient has that prime in its reduced denominator. Hence these coefficients are not contained in any finitely generated subring of Q, despite the rational limiting endpoint and rational-function dependence on n. No inference to a fixed ring of S-integers is valid. The operation is discarded immediately; no extension of the public Hadamard-quotient program is opened.

## Subsequent actual-law and global-operation gates

The following incremental notes contain complete definitions, exact scope, archive queries and fresh primary-read receipts. None is a retained Genesis irrationality tool.

- `GENESIS_ACTUAL_ENDPOINT_SWAP_FIELD.md`: actual endpoint-swap transport has both endpoint jet fields exactly Q(e). Rational S supplies no algebraic jet closure. Public inverse-generator core discarded.
- `GENESIS_NONLINEAR_HURWITZ_GATE.md`: nested exponential/Stirling/Bell transform has an exact multiplicative rational-S bridge and integer Hurwitz germ. The essential transform and nested-exponential continuation are public and discarded.
- `GENESIS_VALUE_UNIFORMIZATION_INFORMATION_LOSS.md`: all nonlinear integrals integral F^j F' become rational under rational S, but the pushed-forward measure is exactly Lebesgue on [1,S] and forgets every interior law. Moment/shuffle descendants discarded.
- `GENESIS_TWO_LAW_TRANSPORT_COMMUTATOR_GATE.md`: actual rational-domain translation/Mobius transports give a valid global bilinear rational-S identity. The natural word-order comparison loses S; finite group-word cocycle closure is public and discarded. Both full source orbits are C(z)-linearly independent by distinct essential poles/logarithmic branch points, so finite full-orbit arithmetic closure is not inferred. Arbitrary nonlinear/infinite operator constructions are not classified by this note.
- `GENESIS_DIRECTED_ENERGY_BARRIER_GATE.md`: a nonlinear directed energy for the complete two-state law would directly exclude each rational target, without requiring a second algebraic output. The barrier-certificate core is publicly matched and discarded before search/optimization. A scoped semialgebraic feasibility lemma and exact sqrt(2) comparison model rule out a stronger false general no-go claim.
- `GENESIS_ACTUAL_FORMAL_GROUP_LOGARITHM_GATE.md`: the complete two-law logarithm gives a rational formal law and an exact rational-S logarithm-value bridge at state 1. Primary Fripertinger–Schwaiger Theorem 5 matches the essential inverse-logarithm addition core exactly, so it is discarded. The polynomial logarithm z+z^2 supplies a rational-logarithm/rational-state countermodel; the actual translated germ has transcendental derivative 5/(e+2). No formal-group or p-adic extension is opened.

Current author status after these gates: no retained fundamentally new analytic core, no rationality proof, and no exhaustion or global impossibility assertion. The search remains active under root steering and the actual quota stop rule.
