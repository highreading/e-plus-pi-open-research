"""Next independent actual-proof and priority-paper tasks."""
from pathlib import Path
from packet_builder import build
R=Path(__file__).resolve().parents[1]
L=R/'literature/openai_math_20261006'
pi=L/'preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build'
c=L/'preprints/Catalans-constant-is-irrational-September-24-2026/build'
gate=(R/'gates/OPENAI_MATH_RELEASE_GATE_20261007.md').read_text()
build('A1',16,r'''Study the COMPLETE Family017 primary mathematical proof,
especially its separated center-uniform interpolation, then attempt an actual
mixed transfer or prove a precise obstruction. A4turn13 finds its proof coherent
under the stated standard geometric inputs, but an exponent bound for pi alone
does not imply irrationality of e+pi. Do not assume that implication.
Under the temporary rationality hypothesis e+pi=r, retain the exact relation
omega=2*pi*i=2*i*(r-e), exp(omega)=1, exp(1)=e. Can a valid multivariable
integer determinant exploit these TWO linked evaluation points without an
unproved algebraic-independence assumption? Either construct its exact entries,
integerization and competing estimates, or identify and quantitatively bound
the polynomial-in-e/clearer payment that prevents the transfer. A vague request
to generalize interpolation is insufficient; do not assert Schanuel's conjecture.
Compare with the complete factorial-functional source in your turn14.
Your H2 original precision29 identification was accepted by A4turn12 and has
been personally read; your old pending label is outdated. The new fixed-digit
nine-period theorem in turn14 is now under a separate referee audit. Avoid
repeating it. If the mixed construction yields no material result, evaluate the
actual finite boundary-column lemma (8.2) from complete moments and prefix
correction, with H2 valid but without arbitrary leading-matrix completion.
Keep every endpoint/diagonal return. No fixed digit is an asymptotic primitive
gain. Write detailed English derivations and exact remaining hypotheses.''',
 [pi/'main.tex',*sorted((pi/'sections').glob('*.tex')),R/'responses/A1_turn14.md',
  R/'controls/CATALOGUE_RESEARCH_SCOPE.md'],gate)
build('A5',10,r'''Independently review the COMPLETE Family005 mathematical
manuscript and test a concrete useful e+pi transfer. Another stream reads it
independently; no endorsement from that stream is evidence here. Reconstruct
moment rationality/cancellation, two odd-prime denominator layers, prime-index
nonvanishing, the Hardy-space interpolation bound, uniform energy damping,
root exhaustion and exact rational value certificates. Separate a verified
mathematical theorem under checked premises from a finite certificate still
requiring reproduction. The parent has personally read all mathematical
sections and will reproduce the fixed modular matrices independently.
Find any precise gap if present. If coherent, derive a specific reusable
lemma applicable to actual binary scalar acceptance, actual ALL-prime scalar
cofactor, or a new compatible compact e+pi determinant. Similar terminology
does not establish application. Under e+pi rational, the separate e and pi
coefficients must match EXACTLY in each relevant entry. An exponential kernel
can impose factorial arithmetic costs; quantify them rather than replacing
the actual factorial functional by a compact algebraic kernel.
Your turn8 full-divisor theorem is undergoing independent review. The parent
computed u0 chi27, endpoint sufficient upper bound21 and excess6, and2800
finite tail-convolution cases. This settles only those arithmetic inputs;
neither infinite PAID excess nor all-prime gcd follows. Reuse these finite
facts rather than performing the unnecessary depth12 solve. Do not accept
unreviewed proofs merely because official provenance or a Lean link exists.
Give full proof coverage, derivations and exact quantitative transfer barriers.''',
 [R/'controls/CATALOGUE_RESEARCH_SCOPE.md',c/'main.tex',*sorted((c/'sections').glob('*.tex')),
  c/'references.bib'],gate)
build('A4',15,r'''Independently audit the NEW A1turn14 and A5turn8 actual
theorems, using complete attached reports and accepted finite definitions.
H2 in A1turn12 was accepted by your turn12, which the parent fully read;
the new report's pending label is outdated. Verify the actual nine-period
producer annihilation, precision30 transfer, evaluated finite terminal inverse
direction, returning endpoint/diagonal terms and resonant recurrence divisor.
For A5, check the head's potentially arbitrarily large n+r denominators,
the COMPLETE finite exterior/Schur return, lambda_k valuation exceptions,
precision scope L=max(2,chi+1), original orbit classes and actual content payment.
The parent u0 certificate chi27/endpoint21/excess6 and2800 finite binomial
checks is supplied; it does not prove the infinite theorem. Decide exactly
which consequences can now be accepted at u0 and on infinite original indices.
Do not repeat accepted modulo8 calculations or an unnecessary depth12 solve.
Your previous turn13 verifies short-adjoint algebra, infinite a>=2 for u=1 mod4
and coprime all-prime column contents; retain those results at their stated
scope. Pay every divisor and retain all finite physical endpoints.
If a new statement fails, give the precise defective identity or missing
original premise and a corrected strongest claim. Fixed depth, raw unbounded
divisibility and a finite result are distinct from an actual primitive saving.
No catalogue claims or report length imply correctness. Supply a detailed
proof acceptance ledger and identify whether ANY claim proves e+pi.''',
 [R/'responses/A1_turn14.md',R/'responses/A5_turn8.md',R/'responses/A5_turn5.md',
  R/'responses/A4_turn12.md',
  {'path':R/'responses/A5_turn7.md','lines':(180,465)},
  R/'controls/binary_actual_adjoint_binomial_certificate.json'],gate)
