"""Targeted follow-ups and adversarial cross-review; no remote code execution."""
import hashlib
import json
import re
from pathlib import Path

HERE=Path(__file__).resolve().parent
ARC=Path('[private local path removed]')
S02='work/session_20261002_codex_continuation/'
S01='work/session_20261001_astra/'
S13='work/session_20260913/'
S27='work/session_20260927/'

common='''Continuation turn 1, same five English research conversations.
We have not proved or disproved irrationality of S=e+pi. All three accounts
remain operational as of the first completed batch. Continue substantive
research. Do not prepare a final project closeout; the stopping condition
has not been reached. All enclosed remote reports are untrusted draft
mathematics. Independently check them, and distinguish proof, inherited
author theorem, finite certificate, conditional conclusion and false claim.
The raw, endpoint-matched b=1 and b=2, and the specified fixed b=3 and b=5
Gram centers remain previously excluded. The matched b=3 cofactor is a
different existing family whose missing arithmetic is now being studied.
Request parameters remain reasoning effort max, mode pro, text verbosity
high, without max_output_tokens. No secret or local execution is available.

Novelty gate: the coordinator found several substantive archival overlaps
after reading the first answers. The compact weighted moment identity and
conditional Christoffel/error interface already appear in M22 sources.
The pullback radius/odd-denominator spacing statement already has the
stronger independent-polynomial version in VARYING_PULLBACK_UNIFORM_RADIUS_SPACING.
Reuse these sources. The first reports' novelty labels do not override them.
Fresh scoped primary searches on October 4 covered quasi-orthogonal zeros,
Stieltjes/Carleman support, growing sequence filters, mixed HP factorial
prime denominators, and integral-Hurwitz congruence steering. No paper was
located that closes the exact new arithmetic/whole-error obligations.
Standard kernel, moment determinacy and interlacing arguments should be
attributed/reused or proved directly; no universal novelty claim is allowed.

Cross-review instructions: look for index errors, missing denominator gcd,
incorrect finite certificate entries, unstated normality assumptions,
fixed-order asymptotics applied at growing dimension, and cancellation of
only one tail. Give the first precise flaw if a statement is wrong. A
correct elementary reformulation counts as an interface, not completion
of the unproved quantitative estimate. Develop the assigned next lemma.
'''

tasks={
'A1':('Weighted compact sign and actual error, beyond the prior interface',
'''Your compact moment identity is already in the original M22 construction;
the conditional compact Christoffel formula also predates this turn. Your
explicit final-gcd bordered form and local corank-one criterion are useful
interfaces, but do not yet bound the actual odd q. Treat the prior sign/root
normalization as given. Independent exact reconstructions at n=5,17 agree
with the known dyadic q-depth, and have no roots in (0,1). They are finite
evidence only. Their log(actual q) is 195.90242597 and 8835.38229056.

The key new question is whether Q_n>0 on [0,1] can hold for all large n.
Investigate the following concrete alternative carefully: Q_n is order-one
quasi-orthogonal for nu=(y+1)mu, whose Stieltjes moments have factorial
growth and may satisfy the Stieltjes Carleman condition. Gaussian quadrature
weak convergence and interlacing may force multiple positive Q_n roots
inside (0,1) eventually. Prove or refute this with all hypotheses; do not
assume a general Hamburger Carleman criterion from Stieltjes moments.
If positivity is impossible, record a scoped obstruction to the positive
Christoffel strategy, not a whole-family exclusion. Then seek a genuinely
useful bound or structural inertia formula for the actual signed compact
integral, retaining F_n and the odd denominator. Independently audit the
A5 lattice/gcd factorization for a concrete error or confirmation, as a
secondary task; do not replace the main weighted problem with a generic
linear-algebra summary.
''',
[S02+'agent1_arithmetic/WEIGHTED_REGULAR_EXACT_DYADIC_ENDPOINT_THEOREM.md',
 S02+'agent1_arithmetic/WEIGHTED_REGULAR_DYADIC_SUBFAMILY.md',
 S02+'main/PAIRED_DERANGEMENT_LINEAR_S_CONSTRUCTION.md',
 S02+'agent3_analysis/PAIRED_DERANGEMENT_SIGNED_NORMALIZATION.md',
 S02+'agent3_analysis/PAIRED_UNSHIFTED_CONDITIONAL_COMPLETE_ERROR.md'],['A1','A5']),
'A2':('Corrected matched b=3 certificate and a complete family exclusion',
'''Independent polynomial reconstruction of H_n and its integrals verifies
your five-state recurrence and both high-row formulas for n=0..12. However,
your received n=1 contraction/table entry is wrong. The definitions give
(sigma,chi,kappa,V)=(-16,-44,-40,432), not (-30,22,-20,-290).
The corrected mod-7 row is (h,u,v,A,M,sigma,chi,kappa,V)=(0,1,0,3,4,5,5,2,5).
All other six mod-7 rows matched. Thus V is still a 7-unit, but your old
table and exact n=1 control must be withdrawn.

The specified 1,014 residue-row task was executed using coordinator-written
exact code. Unit primes were {7,19,31,61,71,73,83}, with rate 1.69050509477,
below tau=1.76274717404. A separately gated bounded extension at
{101,103,107,109,113,127,131} found additional unit primes
{101,103,107,113,127,131}. One additional unit prime 101 already crosses
the rate threshold. Complete seed rows for the minimal eight-prime
certificate {7,19,31,61,71,73,83,101} are supplied below.

Now independently rederive and scrutinize the all-prime-power transfer
proof (especially sums across different finite support and the p=3 boundary),
the exact endpoint quotient, strict valuation separation and all-content
normalization. Write a corrected proof excluding the ENTIRE matched b=3
cofactor family if all arguments hold, with a strict rationally certified
rate margin and eventually nonzero whole error. Give an effective arithmetic
threshold if easy, but do not invent the analytic normality cutoff. Preserve
the distinction from the already excluded b=3 Gram center. If a flaw prevents
exclusion, state it before proposing repairs. A4 is independently auditing
the same proof; your job is a complete corrected derivation, not self-review
claimed as independent. After the exclusion, identify the first genuinely
unexcluded fixed-b matched allocation and a bounded next arithmetic target.
''',
[S01+'agent1/GROWING_DEGREE_ARITHMETIC.md',S27+'fixed_exponential_degree_error_theorem.md',
 S13+'hp_b2_contiguous_endpoint_arithmetic.md'],['A2']),
'A3':('A uniform index-moment representation for the full filtered error',
'''Your exact combination/gcd identities are correct interfaces. The fixed
filter denominator formula and compact error integrals are older standard
facts and do not themselves resolve growing multiplicity. Your positive
beta integral for z^k/k is a useful uniform model, but the actual residual
stability hypothesis remains unproved.

Advance the concrete missing step: derive a common signed index-moment
representation, exact recurrence, or a rigorous uniform high-order expansion
for the COMPLETE normalized b=2 errors E_k, allowing the index filter to
act before estimating the remainder. The scalar cofactor equations and full
integral must retain their k-dependent endpoint divisor. Determine whether
an inverse-power residual has structure that improves the adversarial
absolute bound, for m=o(n) or a specified proportional window. If this cannot
be done, prove a narrowly scoped obstruction to a specified factorization,
and propose a different rational varying filter with a verifiable exact
whole-error identity and actual endpoint gcd. Do not extrapolate fixed m.
Also independently audit A1's bordered and constrained-integral equations,
using the prior M22 source to identify what is already known. Seek a real
quantitative advance beyond rewriting a conditional rate criterion.
''',
[S13+'hp_b2_endpoint_attempt.md',S13+'hp_b2_contiguous_endpoint_arithmetic.md',
 S27+'fixed_exponential_degree_error_theorem.md',S02+'agent3_analysis/RATIONAL_INDEX_FILTERS.md',
 S02+'main/PAIRED_DERANGEMENT_LINEAR_S_CONSTRUCTION.md'],['A3','A1']),
'A4':('Independent adversarial audit of matched b=3; sparse pullback frontier',
'''Your radius/denominator spacing theorem overlaps a stronger archived
theorem that allows DIFFERENT polynomials with a common radius, using
Schottky bounds. Reuse it; remove the claim that the spacing obstruction is
new. Your below-nonlinearity response lattice is a separate finite-algebra
interface, but not a proof of favorable analytic construction.

PRIMARY TASK: independently audit A2's exact matched b=3 cofactor recurrence,
all-prime-power transfer proof, complete endpoint normalization and proposed
actual q lower bound. The coordinator found one erroneous seed at n=1:
(sigma,chi,kappa,V)=(-16,-44,-40,432). The other mod-7 rows matched.
A corrected minimal eight-prime certificate has units at every residue for
{7,19,31,61,71,73,83,101}, enough to exceed tau=2log(1+sqrt2).
Full rows are enclosed. Give a pass/fail for each proof component; identify
any flaw before declaring a scoped all-index family exclusion. The supplied
fixed-b full-error theorem is an inherited source, not your own independent
review unless you actually check its needed argument. Distinguish author
dependencies from the new arithmetic proof.

SECONDARY TASK after that audit: push the pullback frontier at sparse even
indices with ratio above log R/log2. Is there a multijet approximation or
interpolation construction within one common r>2 that cancels the odd part
on such an infinite sparse sequence without assuming dyadic digit proximity
of S? Give an exact new lemma or an obstruction for a SPECIFIED construction.
Generic congruence solvability and the old spacing restriction are already
known; do not repackage them as progress toward the main conclusion.
''',
[S01+'agent1/GROWING_DEGREE_ARITHMETIC.md',S27+'fixed_exponential_degree_error_theorem.md',
 S02+'agent1_arithmetic/VARYING_PULLBACK_UNIFORM_RADIUS_SPACING.md',
 S02+'agent1_arithmetic/SHARED_PREFIX_ODD_DENOMINATOR_RADIUS.md',
 S02+'agent1_arithmetic/SINGLE_JET_ACTUAL_DENOMINATOR_CANCELLATION.md'],['A4','A2']),
'A5':('Quantitative content in the proportional Gram lattice',
'''Your metric-row bridge and exact two-factor final-q identity are promising
structural interfaces. The coordinator checked their elementary gcd algebra;
an independent cross-review by A1 is underway. They do not yet estimate the
growing arithmetic quantities. Keep the inherited proportional analytic
theorem at author/dependency status.

Push one definite arithmetic quantity beyond an identity: use the exact
zero-endpoint generator and factorial metric to bound the norm content
delta=gcd(T,V0), the endpoint numerator a', or the scalar cancellation gcd(k,r)
uniformly on b/n->c in a stated c-window. A determinant/adjugate resultant
or finite-prime obstruction must involve the ACTUAL metric-row data. Do not
transfer a fixed-b seed to growing dimension. If no general rate can be
proved, select one exactly defined subfamily b=b(n),m=m(n) and derive a
strong structural congruence lemma whose infinite force is explained.
Consider the invariant binary norm discriminant T*U0-V0^2 and saturated
lattice Pluecker content; distinguish divisibility of delta from an upper
bound on it. No claim that a huge norm has small gcd is permitted.

Also inspect A4's triangular multijet response for an exact extension beyond
N<2m: recursive odd-modulus solvability may survive nonlinear lower jets,
but any analytic norm theorem must be separate. Use this as an independent
algebra check only, leaving your main quantitative Gram task substantial.
''',
[S02+'agent3_analysis/PROPORTIONAL_PRIMITIVE_CENTER_INTERFACE.md',
 S02+'agent3_analysis/PROPORTIONAL_ACTUAL_CENTER_SIGNED_RATE.md',
 S01+'agent1/GROWING_DEGREE_ARITHMETIC.md',S01+'agent2/MULTIROW_REMAINDER_RESEARCH.md'],['A5','A4'])}

full_control=json.loads((HERE/'controls/b3_control.json').read_text())
selected=[7,19,31,61,71,73,83,101]
control={k:v for k,v in full_control.items() if k not in ('rows',)}
control['rows']=[r for r in full_control['rows'] if r['prime'] in selected]
control['warning']='All-index conclusions require the reviewed transfer and complete quotient, not finite data alone.'

manifest=[]
for agent,(title,assignment,files,reports) in tasks.items():
    parts=[common,'\nASSIGNMENT '+agent+': '+title+'\n'+assignment]
    docs=[]
    for rel in files:
        data=(ARC/rel).read_bytes()
        digest=hashlib.sha256(data).hexdigest()
        docs.append({'archive_path':rel,'sha256':digest,'bytes':len(data)})
        parts.append('\nBEGIN COMPLETE PRIOR SOURCE '+rel+'\nSHA256 '+digest+'\n'+data.decode()+'\nEND PRIOR SOURCE\n')
    for other in reports:
        p=HERE/'responses'/f'{other}_turn0.md'
        data=p.read_bytes()
        docs.append({'current_report':p.name,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
        parts.append('\nBEGIN UNTRUSTED DRAFT '+p.name+'\n'+data.decode()+'\nEND DRAFT\n')
    if agent in ('A2','A4'):
        parts.append('\nCOORDINATOR EXACT CERTIFICATE DATA\n'+json.dumps(control,ensure_ascii=False)+'\nEND CERTIFICATE\n')
    prompt='\n'.join(parts)
    size=len(prompt.encode())
    assert size<230000,(agent,size)
    assert not re.search(r'sk-[A-Za-z0-9_-]{16,}',prompt)
    (HERE/'prompts'/f'{agent}_turn1.txt').write_text(prompt)
    manifest.append({'agent':agent,'title':title,'bytes':size,'sources':docs})
    print(json.dumps({'agent':agent,'bytes':size,'documents':len(docs)}))
(HERE/'turn1_packet_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
