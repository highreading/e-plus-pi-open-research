> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Research report: e + pi

13 September 2026. Quota-limited stopping condition reached at 04:39:23 UTC
(12:39:23 Asia/Shanghai).

**No rigorous proof that e+pi is rational or irrational was obtained.**
The research session ended under the user's revised quota condition:
the supported account tool showed 5% remaining core quota and zero reset
credits, and a separate fresh read confirmed both facts. Preparation of
this report began only after that observation.

The strongest completed mathematical development is an exclusion theorem
for the project's entire raw approximation family. Its reduced integer
errors tend to infinity in both parities, so no subsequence of that family
can yield the required shrinking integer forms. The principal surviving
concrete questions concern different, unequal-degree Hermite-Pade families
and the original synchronized integral construction.

## Research record and audit scope

The authoritative working directory remains
`[private local path removed]`.
New derivations, source reviews, failed attempts, exact checks and quota
records are in `work/session_20260913/`; the top-level session index is
`SESSION_20260913.md`. This report is also saved in that project.

The initial inventory contained 5,867 files,104,830,601 bytes and3,704
distinct SHA-256 contents. Every initial file was inventoried and hashed.
The audit covered text/code structure, result schemas, manifests, narrative
claims and failures. It included detailed mathematical reading of central
and recent arguments. This is not a claim that every historical proof was
independently re-proved or every numerical entry recomputed.

The sources collection contained 579 substantive Markdown notes; the
results audit parsed all 1,229 substantive unique JSON documents and
resolved all 2,501 substantive checksum lines. Five historical pins were
stale and were preserved as discrepancies. Draft/canonical differences
and runtime-version issues are documented in the three audit reports.
Instructions embedded in old documents were treated as historical data,
not as new instructions from the user.

The three agents initially divided the archive into results/manifests,
computations, and sources/literature. Subsequently all three worked on
bounded mathematical tasks and cross-reviewed each other's derivations:
operator and saddle analysis, exact arithmetic and certificate
reconstruction, and theorem-hypothesis and normalization audits. Root
also derived and reviewed mathematical lemmas, including the positive
residue prime-power lift and the final companion-error refinement.
The work went substantially beyond collecting references.

“Passed independent review” below means a separate agent or root checked
the displayed mathematical argument and applicable certificate. It does
not mean external peer review or formal verification in a proof assistant.
No assertion of worldwide novelty is made for these project deductions.

## 1. Completed exclusion of the entire raw family

Retain the original integer endpoint polynomials and set



$$
Z_n=\widehat Q_n(1),\qquad
 N_n=\widehat P_{e,n}(1)+4\widehat P_{a,n}(1),
$$




$$
g_n=\gcd(|Z_n|,|N_n|),\qquad
 q_n=|Z_n|/g_n,\quad
 p_n=\operatorname{sign}(Z_n)N_n/g_n.
$$



These are the actual reduced endpoints, including their final gcd. The
normality and nonzero-endpoint arguments establish their existence at
every sufficiently large index. Let rho=(sqrt(5)-1)/2 and phi=1/rho.

The completed theorem is



$$
\boxed{|q_n(e+\pi)-p_n|\longrightarrow\infty\quad(n\to\infty).}
$$



More precisely, for all sufficiently large integers n,



$$
|q_n(e+\pi)-p_n|\ge
 \frac{\exp(3n/200)}
 {4\sqrt2\,(25839289479611181)\,n^{10}}.
$$



The analytic part does not provide an effective first index. The
conclusion excludes all subsequences and nonzero integer multiples of
these forms. It does not exclude new linear combinations or other
constructions, and it implies neither rationality nor irrationality of
the main number.

### Signed analytic errors

The separate parity proofs give



$$
e+\pi-\frac{p_{2m}}{q_{2m}}
 =(-1)^m C_{\rm e}\rho^{10m}(1+o(1)),
$$




$$
e+\pi-\frac{p_{2m+1}}{q_{2m+1}}
 =(-1)^m C_{\rm o}\rho^{5(2m+1)}(1+o(1)),
 \qquad C_{\rm e},C_{\rm o}>0.
$$



The constants retain the actual limiting polynomials:



$$
C_{\rm e}=4\pi\rho A_{\rm e}/B_{\rm e},\qquad
 C_{\rm o}=-4\pi\rho A_{\rm o}/B_{\rm o}.
$$



Certified enclosures include



$$
.0493603201444840<A_{\rm e}<.0493603201863010,
$$




$$
.6040688968602422<B_{\rm e}<.6040688969081851,
$$




$$
-1.193<A_{\rm o}<-1.192,
 \qquad .282<B_{\rm o}<.283.
$$



These are interval certificates for fixed operator expressions, using
exact saved witnesses and bounds for the full infinite residuals. They
are not extrapolations from large-degree approximants. The proofs supply
uniform analytic bounds, kernel convergence with summable tails,
nonzero actual saddle multipliers, both contour contributions and signs,
and factorial separation of the exponential and arctangent errors.

The odd analysis needs its own reference exponent m+1 and the identity
Psi_(2m+1)(z)=(-1)^m z Phi_m(-z^2). The extra z, negative inverse corner,
and contour minus sign were retained. Copying the even formula without
these changes would give incorrect amplitudes or signs.

### Arithmetic at the reduced denominator

For every degree the exact dyadic valuation is



$$
v_2(q_n)=n+2\left\lfloor\frac{n+2}{4}\right\rfloor
 \ge\frac32n-\frac12.
$$



For the fixed set



$$
\mathcal P=\{3,7,23,43,71,83,101,109,127,151\},
$$



the reviewed residue-transfer theorems and independent exact seed
reconstructions prove, for every n>=302,



$$
v_p(q_n)=v_p(Z_n)\ge v_p(n!)\quad(p\in\mathcal P).
$$



The use of a finite certificate is legitimate here because an all-index
theorem first reduces each fixed prime to its complete finite set of
residue seeds. Checking isolated degrees would not establish this result.

Legendre's factorial-valuation formula now gives



$$
q_n\ge\frac{e^{Ln}}
 {\sqrt2\,(25839289479611181)n^{10}},\qquad
 L=\frac32\log2+\sum_{p\in\mathcal P}\frac{\log p}{p-1}.
$$



Two different exact rational logarithm calculations certify



$$
L-5\log\phi>0.015628796017>3/200.
$$



Both parity constants exceed1/2, so their relative errors have magnitude
at least rho^(5n)/4 beyond one finite index. Multiplication by the last
denominator bound proves the exclusion theorem.

The complete assembly and dependency ledger are in
[raw_all_parity_raw_exclusion.md](../../work/session_20260913/raw_all_parity_raw_exclusion.md). The odd contour review includes an
explicit acyclic dependency map. The next session should treat this
route as closed for shrinking raw forms; further scans for favorable
raw degrees or additional uniform primes cannot rescue it.

## 2. General arithmetic developed along the way

The Appell/augmented-Schur representation was extended to every
inverse-column cofactor. Integral symmetric polynomials in
Jucys-Murphy elements provide comparisons between same-size partitions
with matching content residues. The same-size condition is essential;
a comparison between different symmetric groups is not justified by
matching contents alone. The relevant primary structural input is
[Ryba, Stable centres of wreath products](https://alco.centre-mersenne.org/item/10.5802/alco.264.pdf).

The resulting actual-polynomial congruences cover n, n+1, n-1 and general
positive and negative small residues. The positive-residue theorem was
lifted to full prime-power precision, retaining binomial valuation loss.
An exact integral differential-operator identity supplies a step that a
naive Lucas-theorem lift cannot justify. Exceptional numerator seeds and
singular determinant seeds remain distinct.

For example, the reviewed lift proves bounded actual numerator losses
on the even classes n=5 modulo121 and n=3 modulo2197: their11-adic and
13-adic numerator valuations are respectively1 and2. These facts are
not needed for the completed raw exclusion but are useful arithmetic
lemmas. They do not transfer automatically to a different HP family.

Key records are [raw_positive_residue_full_prime_power_lift.md](../../work/session_20260913/raw_positive_residue_full_prime_power_lift.md),
[raw_positive_prime_power_lift_independent_review.md](../../work/session_20260913/raw_positive_prime_power_lift_independent_review.md),
[raw_negative_residue_schur_and_endpoint_seeds.md](../../work/session_20260913/raw_negative_residue_schur_and_endpoint_seeds.md), and their reviews.

## 3. Unequal-degree HP families: the main surviving concrete problem

Use the original Mobius pullback



$$
F(z)=4\arctan\frac z{2-z},\qquad F(1)=\pi,
$$



and degree patterns(n,b,n):



$$
R_n=A_n+B_ne^z+C_nF(z)=O(z^{2n+b+1}),
 \quad B_n(1)=C_n(1)=Y_n.
$$



For b=1 and b=2, eventual uniqueness, nonzero endpoints, and signed
evaluated error asymptotics have passed independent review. If q_n is
the reduced denominator of A_n(1)/Y_n, then the actual integer form
L_n=q_n R_n(1)/Y_n satisfies



$$
\log|L_n|=\log q_n-2n\log(1+\sqrt2)+o(n).
$$



Thus a concrete sufficient irrationality lemma is



$$
\liminf_{n\to\infty}\frac{\log q_n}{n}
 <2\log(1+\sqrt2)
$$



for either family. A fixed positive gap gives a nonzero shrinking
subsequence. No such estimate is proved. Conversely a strict lower
bound above that threshold would exclude that family; it too remains
unproved. The degree-two change improves a constant factor in the
normalized error, not its exponential rate.

The minimal coefficient clearer of C_0-C_1 in the degree-one family
has logarithm2n log n+O(n). More generally, every full integral triple
has a large forced divisor in every exponential coefficient. These are
actual coefficient statements, but dividing by the final endpoint gcd
can change the reduced denominator. They cannot be substituted for a
bound on q_n.

The final arithmetic continuation, with both independent reviews now
FULL PASS, eliminates the large kernel from
the degree-one and degree-two endpoint formulas. It rewrites the
remaining ratios as small determinants of adjacent integer Legendre
polynomials and explicit factorial transforms. This is a reduction of
the open arithmetic problem, not its resolution. The final review
statuses and exact file names are in the closing verification register.

### Exact error of the existing rational companion

The prior degree-one construction has a specific rational companion
r_n^* to e. Set V=K_n(t,1), W=1/(1-t)-H_n(t), and
ell_j(t^k)=1/(n+k+1-j)!. Here H_n denotes the projection of1/(1-t).
Writing t_j=ell_j(V), w_j=ell_j(W), its exact error is



$$
e-r_n^*=\frac{t_1w_0-t_0w_1}{t_1-t_0}.
$$



The final deduction from the project's factorial determinant method is



$$
e-r_n^*\sim\frac{e^{-\sqrt2}W(0)}{n^3n!},\qquad
 \log|e-r_n^*|=-n\log n+n+o(n).
$$



It closes the previously suggested possibility that this same companion
had hidden decay exp(-2n log n+O(n)). That stronger estimate cannot hold
on any unbounded subsequence. The proof and its final independent status
are recorded in [hp_b1_companion_exact_error_rate.md](../../work/session_20260913/hp_b1_companion_exact_error_rate.md) and its FULL PASS
review [hp_b1_companion_error_independent_review.md](../../work/session_20260913/hp_b1_companion_error_independent_review.md), as well as the closing
verification register. Another companion would need its own error and
reduced-height proofs.

### Auxiliary p-adic gcd information

For the separate auxiliary integers h_n=H_n(1) and J_(n+1)(1), the
session proves exact3-adic and5-adic gcd formulas and full unit lifts
on the residue1 branch. The last bounded extension proves restricted
analytic interpolation on every odd-prime residue disk. At a joint
residue, the first normalized lift equations are affine. Under an
explicit nonzero index-slope condition, the local gcd valuation is



$$
\min\{v_p(n-\xi),\Lambda\},
$$



where xi is the root of the chosen gate and Lambda is the valuation of
the other gate at xi. Root independently checked this conditional
reduction. Uniform slope nonvanishing and bounds for Lambda are open.
The known actual endpoint-gcd implication applies only at p>2n+2;
fixed-prime analytic information does not by itself settle those growing
primes. Simplicity in the polynomial variable is not simplicity in the
index, and the proof keeps them separate.

## 4. The original matched-integral route remains unresolved

The archive's original construction uses n=6m and constants



$$
h=2.3246783391437307\ldots,\quad
 d=2.3370623743589730\ldots,
$$




$$
T=h-d/2=1.1561471519642446\ldots.
$$



The booked positive arithmetic rate remains0.1365141682948128..., leaving
a deficit of1.0196329836694318.... The raw-family results above do not
alter this ledger.

With the actual primitive content c_m, synchronized matching gcd Delta_m,
and final gcd g_m at parity-compatible optimal beta indices, the exact
sufficient target is



$$
\limsup_m\frac{\log(c_m\Delta_mg_m)}{6m}>T.
$$



A favorable subsequence suffices; a global liminf is unnecessary. The
positive matched form ensures nonvanishing once the archived input
hypotheses hold. Gains at different indices cannot be added without
synchronization. Upper bounds for possible content are not positive
divisors, and fixed-layer support estimates cannot be summed through an
unbounded valuation tower without a tail estimate.

The old inference that d>h alone suffices after matching remains invalid.
Without extra content the generic positive matching threshold is d>2h.
Items424 and the work-only continuations give exact digit identities and
specific obstructions, but no sufficient moving-prime distribution or
all-depth gain theorem. Their detailed status is preserved in the archive
audits rather than silently promoted.

## 5. Literature and theorem applicability

The search included classical transcendence theory, mixed E/G values,
periods, arithmetic holonomy, Pade and auxiliary-function methods,
irrationality measures, and recent 2025-2026 work. No reviewed theorem
settles the target. A June2026 preprint explicitly leaves it open and
proves only scoped tail criteria and construction audits; the audit
also notes that resembling continued fractions does not invalidate an
independently proved shrinking integer form.
[Yu, Tail Criteria and Certificate Obstructions](https://arxiv.org/abs/2606.17303).

| Route and strongest relevant input | Applicability and exact obstruction | Useful next mathematical step |
|---|---|---|
| Unequal-degree Hermite-Pade; project endpoint sign and asymptotic theorems | Direct if its actual reduced denominator is small enough; the final gcd remains uncontrolled | Study the new small endpoint determinants at full prime-power depth |
| Original matched integrals and positive beta forms | Direct after synchronized gain exceeds T; current ledger falls short | Prove a lower gain on the same subsequence, including all depths and final gcds |
| Arithmetic holonomy and effective Apery-limit methods | Requires admissible denominator growth and enough continuation; the direct mixed germ has factorial denominators | Construct a value-retaining pair meeting the exact arithmetic and analytic margin |
| Parameterized Pade approximants and irrationality measures for pi | Separate pi estimates do not supply a mixed denominator-synchronization theorem | Optimize the combined matching objective and prove its actual divisor |
| Subspace-Theorem, S-unit and gcd methods | Fixed or controlled prime-support hypotheses are missing for actual reduced endpoints | Prove outside-prime mass and multiplicity estimates before invoking them |
| Lindemann-Weierstrass and Gelfond-Schneider | Algebraic-input hypotheses do not hold for the needed mixed additive relation | Supply a valid algebraic-input reduction; none is known here |
| Baker's logarithm theorems | pi is related to a logarithm of an algebraic number, but the e term has no applicable algebraic logarithm argument | Prove an actual reduction with algebraic arguments and coefficients |
| Schneider-Lang, Nesterenko and auxiliary functions | Existing independence results concern other values or require missing height, zero, or specialization estimates | Isolate and prove the target-specific auxiliary-function inequality |
| Schanuel and mixed-value/period conjectures | Conditional; the necessary numerical independence remains a major unresolved input | Pursue a sharply delimited special case without using it as a theorem |

The arithmetic holonomy review identifies the precise issue: a direct
germ a-exp(z)-4arctan(z) has even coefficients -1/(2m)!, requiring
factorial clearing. Fixed lcm-type denominator budgets grow only
exponentially. Polynomial factors or fixed rescaling cannot repair this.
The general method remains valuable for a different admissible
construction. [Calegari-Dimitrov-Tang, Arithmetic holonomy bounds](https://arxiv.org/abs/2510.04156).

The mixed-value literature contains substantial results and conditional
extensions, but does not prove the E/G-value separation needed here.
If e+pi were algebraic, e would be the difference of an algebraic number
and a G-value. Excluding that possibility is stronger than the currently
available direct inputs reviewed in this session.
[Fischler-Rivoal, Arithmetic Gevrey values](https://arxiv.org/abs/2301.13518).

Functional transcendence of periods in families does not supply the
missing arithmetic independence at one fixed numerical specialization.
The geometric theorem and its Ax-Schanuel setting were kept distinct
from numerical period-map injectivity.
[Bakker-Tsimerman, Functional Transcendence of Periods](https://arxiv.org/abs/2208.05182).

Under Schanuel's conjecture, applying it to the Q-linearly independent
numbers1 and i*pi gives transcendence degree at least2 for Q(e,pi),
because their exponentials are e and -1. Thus e and pi would be
algebraically independent and their sum transcendental. This is a
complete conditional implication, not an unconditional proof.

The September 10, 2026 preprint of Bai claims an improved upper
irrationality measure7.101862832357 for pi. The session checked selected
arithmetic and contour arguments and reproduced its rates, but did not
certify the entire preprint. Even accepting those rates, matching its
pi form with the available beta e form leaves a positive unsynchronized
upper exponent about1.61869 in the stated normalization. This means
the supplied estimates do not close; it does not prove those matched
forms actually diverge. [Bai preprint](https://arxiv.org/abs/2609.11276),
[Zeilberger-Zudilin published construction](https://arxiv.org/abs/1912.06345).

Full applicability notes and exact reading boundaries are in
[audit_sources.md](../../work/session_20260913/audit_sources.md), [literature_pi_20260910.md](../../work/session_20260913/literature_pi_20260910.md), and the session's
specialized literature notes. A source's title, publication status or
successful numerical replay was never treated as proof of its application.

## 6. Ranked continuation and tasks to avoid repeating

1. **Unequal-degree HP endpoint arithmetic.** Start with the degree-one
   and degree-two kernel eliminations and their final reviews. Determine
   actual numerator/denominator valuation differences, including singular
   seeds and higher digits. The goal is the precise q_n threshold above,
   not another coefficient-height bound or normality computation.
2. **The original synchronized gain.** Work directly on actual moving
   primes and the all-depth tail at the same m and beta index. Retain
   the unchanged lower-gain ledger and favorable-subsequence quantifier.
3. **New degree allocations or parameter choices.** First derive exact
   endpoint identities, evaluated nonvanishing, and full primitive
   normalization. Optimize the combined objective only after these exist.
4. **Alternative holonomy or special-function constructions.** Screen
   denominator and numerical-specialization hypotheses before investing
   in auxiliary computations. Conditional period membership is a barrier
   to examine, not a proof that every replacement is impossible.

Do not reopen the raw degree scan, the impossible degree-one coefficient
clearer target, or the faster-error hypothesis for the same companion.
Do not infer infinite density from fixed tables, promote diagnostic
quadrature to interval proof, omit the final endpoint gcd, or combine
arithmetic gains belonging to incompatible index sets.

## 7. Quota mechanism and stopping record

An app heartbeat and an active-session supported-tool loop were configured
to check quota each minute. The active loop logged a parsing interruption
and was restarted; the record does not claim an uninterrupted check in
every minute of the whole session.

The individually authorized reset was consumed when the monitor observed
5% at 22:57:37 UTC on September12. The reset tool returned success, and a
fresh read at 22:57:44 UTC showed 100% remaining and zero credits. The
attempt used a persisted idempotency key and was not redeemed again.

The user's later revision changed the stopping threshold from 10% to 5%.
Both the active goal and monitor instructions were updated. Research
continued below 10%. At04:39:23 UTC on September13 the monitor recorded
5% with zero credits, and root separately verified 95% used with zero
credits before starting this report. The completed monitor is paused
after report preparation to avoid redundant future research wakeups.

The exact quota evidence and reset verification remain in
`quota_log.jsonl`, `quota_reset_attempt.json`, and the closing record.
The main mathematical question remains unresolved. The next session
should resume from the ranked live estimates and final verification
register, not from a claim that any conjectural bridge has been proved.

The companion [closing verification register](CLOSING_VERIFICATION_REGISTER_20260913.md)
lists the final source/review pairs, the last exact endpoint formulas,
their normalization cautions and the next specific estimates to attack.
