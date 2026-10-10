from pathlib import Path
import hashlib, json, sys

H = Path(__file__).resolve().parent
R = H.parent
sys.path.insert(0, str(H))
from packet_builder import build

for agent, turn in [('A1', 23), ('A5', 25)]:
 g = json.loads((H / f'{agent}_TURN{turn}_FULL_READ_GATE.json').read_text())
 assert g['full_report_read']
 assert g['report_sha256'] == hashlib.sha256((R / f'responses/{agent}_turn{turn}.md').read_bytes()).hexdigest()

gate1 = r'''The parent reads FULL23 ALL1605 lines. NEW actual finite
mod27 quotient/remainder compression, all-fourteen-source uniform
eta=h=0, exact original leading ranks/kernels, unit pivot frame and
leading particular force solution receive favorable parent algebraic
review; DIFFERENT audit is PENDING and will be assigned to A4 AFTER its
live FULL28 has been read. The finite macro exclusion is consistent
with the saved coordinator dagger candidate/closed bounded receipt.
Do not rerun that receipt, your former alternating failure, or the
five-pole evaluation. Current and Desktop endpoint/arithmetic registers
recover OLD higher block theorems and source grading warnings, not a
completed actual annihilator-filtered NEXT operator/force calculation.
The only exact new annihilator-filtered task located is your FULL23
open lemma. This scoped check is not exhaustive novelty. The previously
checked binomial/Hankel literature is classical reuse; an auxiliary
integer moment representative is not the original next block.
FULL A4turn25 is supplied. Its audits of your FULL20..22 already PASS.
Only its NEW Section6 requires your DIFFERENT audit; its actual DeltaA/
DeltaC restrictions and separate complete force remain expressly OPEN.
No original-sized inverse/array, old table or scan is requested.'''
task1 = r'''FIRST DIFFERENT-audit NEW FULL A4turn25 Section6, all literal
integer moment lifts, finite boundary contractions, exact R4-sharp=-3
Cmom modulo9, actual DeltaA/DeltaC perturbation formula and ALL listed
raw/core/physical precision costs. Retain its distinction between
integer representatives and actual complete first-four blocks. Do not
re-audit its reviews of your own reports.

PRIMARY NEW RESEARCH: use your NEW FULL23 explicit actual annihilator
frame to evaluate the WHOLE NEXT operator and complete force in (8.4)
and (8.5), or close an exact first-four correction needed for them.
The unknown object is the original complete B6 modulo9, filtered by
literal integer binomial lifts Khat of y^r(1-y)^(2u), with 0<=r<=u-3,
and the actual unit complement E on 0..2u-1. All indices and both finite
boundaries stay literal. Seek a symbolic evaluated coefficient law for
Khat^T B6 Khat/3 modulo3 and the complete returned force, without an
original-sized inverse. Include any first-four correction surviving
this filter, ALL fourteen source terms, the complete stationary source
through its required precision34, both mixed LOW returns, the next
first-four force and separate lambda4, and physical7 transport at their
exact costs. Any sublemma must be paid at its original precision.

The vanishing leading Cmom contraction and leading force compatibility
can simplify the filtered calculation; they do NOT prove the actual
DeltaA/DeltaC correction or a deeper return vanishes. In particular do
not replace actual blocks with A-sharp/C-sharp or infer an inverse
grading from source support. If a source-specific carry or finite
quotient compression yields the NEXT original polynomial law, prove
both admitted degree boundaries and the complete carry before division.
Determine the resulting exact kernel/force compatibility and allowed
3^(-1) solve criterion, or isolate a genuinely smaller unpaid actual
operator lemma. Merely defining the projected matrix is insufficient.

Reuse eta=h=0, all leading ranks, explicit z_p and pivot frame; do not
spend another report reproving them. Keep the complete forcing identity,
all later physical5/7 and kernel returns, actual contents, least all-prime
clearer, ALL-prime G, actual primitive denominator and nonzero WHOLE error
at the SAME original indices. No global proof or allowed-lift success
is assumed. Detailed English derivations are required. A suggested
bounded computation must have new explicit inputs/expected outputs for
the parent to author; no remote code is run.'''
assert not (R / 'prompts/A1_turn24.txt').exists()
build('A1', 24, task1, [R / 'responses/A1_turn23.md', R / 'responses/A4_turn25.md',
                       R / 'responses/A1_turn22.md'], gate1)

gate5 = r'''The parent reads FULL25 ALL2006 lines. Your DIFFERENT audit
of A3turn22 normalization rigidity PASSES. NEW degree16 complete source
norm reduction, actual reflected companion at p-N,p-N+1 with UNCHANGED
physical moment index N, positivity, evaluated paid factorization,
split/inert contact rules and full Hasse harmonic condition receive
favorable parent algebraic review; DIFFERENT audit is PENDING and will
go to A3 AFTER its live FULL24 is read. Do not self-audit or rederive
these identities. Current response and Desktop endpoint/arithmetic
register/topic searches locate no completed norm-regularity or fixed-N
exponential-height exceptional-factor certificate for these ACTUAL
new companions. This is a scoped check, not exhaustive novelty.
Older resultant/value-contact warnings, mixed-ratio factorial rigidity,
classical norm/adjacent Chebyshev identities and the already reviewed
Gaussian-prime applicability filter are REUSE. A nonzero polynomial
coefficient alone is not nonzero actual evaluation. FULL A3turn23 new
endpoint-G/odd-clearer/factorial laws are supplied for DIFFERENT audit;
A3's present PRIMARY work remains p>2N, distinct from your interval
N<p<2N companion exceptional classes. No old scan is requested.'''
task5 = r'''FIRST DIFFERENT-audit ALL NEW FULL A3turn23 claims: actual
square/K odd arc support and exact least D/lambda; primitive q odd and
all 2-primary valuation/credit values; exact p>n G/q formulas and gamma
factor isolation; paying b-degree via a_K and remaining content via
delta^2; unit-Delta state/endpoint contact; explicit Chebyshev factorial
weights and ALL degree-six A6/B6 source/endpoint constants; exact
remaining r-degree mass formula and raw paid normalization precision.
Its audit of your FULL23 is already complete, not part of this audit.
Preserve all exact hypotheses and report each PASS/repair.

PRIMARY NEW RESEARCH: use the ACTUAL source collisions and unit-Delta
chart to remove the factorial-height terminal states from your NEW
norm-companion EXCEPTION tests. On original p in S_N, B_p=j_p=0 and
p^3|U,V, your first-raw-source residue and xi_p/K-star tests are actual.
The source collision modulo p gives M_c*t_ell=C with Delta a unit;
evaluate this target, transport through the COMPLETE six-step return,
and substitute it into Q00,Q01,Q11 and hence the reflected and cross
residue tests. Determine whether xi_p and K-star(Z0) must be units on
either unpaid class p=3,5 mod8, or derive their exact exceptional
restrictions AFTER this actual substitution.

If universal regularity fails, aim at explicit p-INDEPENDENT integers
H_N of height exp(O(N)) receiving the exceptional primes at this fixed
original N (with exact multiplicities where proved). At residue level
Gamma_p^8=16 modulo p and X_p=I_p; both original Gaussian adjacent
values are prescribed. One may eliminate the FINITELY many prime-half
base roots and the short residual values using the exact adjacent
dictionary, rather than retain p-dependent factorial Hermite states.
Every denominator, Gaussian content and conditioning factor must be
paid. The resulting receiving integer must be ACTUALLY evaluated,
proved nonzero at every original N to which the bound applies, and
have a proved height bill. Do not leave a named resultant, use independent
Gaussian digits, or infer nonzero evaluation from a nonzero coefficient.
An explicitly evaluated finite-degree polynomial in N and actual
original Gaussian coefficients could be useful because those coefficients
have exponential height; establish its receiving divisibility and
actual nonvanishing rather than assuming either.

This task concerns the reflected/cross norm EXCEPTIONS, not a reprint
of FULL25's equivalence or merely a fifth-digit extension. A bound on
distinct exceptional-prime mass does not bound deeper multiplicities
unless their receiving order is proved. Norm-regular primes still need
actual norm-harmonic separation; do not declare that missing step done.
Keep literal S_N p2-block membership/conditioning, exact larger target
4+B+j, 2*a_G+target raw costs, both signs/physical states/returns, original
arcs/least clearers, ALL-prime G, actual primitive q and positive WHOLE
error at the SAME original indices. No e+pi decision is presumed.
Supply detailed English proofs, exact unresolved claims, and only new
bounded computation suggestions for the parent to author safely.'''
assert not (R / 'prompts/A5_turn26.txt').exists()
build('A5', 26, task5, [R / 'responses/A5_turn25.md', R / 'responses/A3_turn23.md'], gate5)
