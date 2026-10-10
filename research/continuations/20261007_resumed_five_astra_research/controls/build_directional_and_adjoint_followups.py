"""Coordinator-authored continuation assignments; source text is only evidence."""
from pathlib import Path
from packet_builder import build
R=Path(__file__).resolve().parents[1]
P=R.parent/'astra_pro5_resume_20261006'
O=R.parent/'astra_pro5_resume_20261005'
charge=(R/'gates/COMPLETE_CHARGE_AND_DIRECTIONAL_GATE_20261007.md').read_text()
arithmetic=(R/'gates/ALL_PRIME_FACTORIAL_TRANSFER_GATE_20261007.md').read_text()
binary=(R/'gates/BINARY_SHORT_ADJOINT_GATE_20261007.md').read_text()

build('A1',14,r'''Continue from your fully read turn13. The leading-completion
counterexamples are valid only for that implication class; do not treat them as
original-matrix examples. Stop extrapolating a common radical dimension into a
relative cofactor saving. Seek an ACTUAL complete-source directional inverse
bound Cw=z, or an evaluated relative determinant pair, on a stated infinite
unchanged original subfamily. Use the complete finite moment recurrence and
actual producer coefficients, with the factorial component and first returning
rank-two producer terms. Prove a genuine quantitative statement; a renamed
determinant, classical kernel formula, or conditional inverse lemma alone is
not an advance. Pay every coefficient/inverse divisor and complete diagonal.
If the proposed directional bound fails on the actual objects, give an actual
mechanism or counterexample with the original source, not arbitrary matrix
completions. Identify whether any result reaches an arithmetic scale that could
change the actual all-prime denominator/error comparison. The precision29
original identification remains under A4 review; flag dependence on it.
Supply all derivations for independently checking new source-level claims.''',[
 R/'responses/A1_turn13.md',R/'responses/A1_turn12.md',
 R/'controls/TERNARY_PRODUCER_COEFFICIENT_RECOVERY.md',
 R/'gates/TERNARY_HIGHER_RADICAL_REUSE_GATE_20261007.md',
 {'path':P/'responses/A1_turn19.md','lines':(179,230)},
 {'path':P/'responses/A1_turn19.md','lines':(752,785)}
],charge)

build('A2',10,r'''Continue from the fully read turn9 exact logarithmic charge
determinant. The Legendre recurrence/Casoratian is classical and reused in a
different archived endpoint family; do not claim the method itself as novel.
Now EVALUATE the complete exponential residue in actual normalization, or prove
a useful bound on the auxiliary clearer m_B after the same actual d_B is fixed.
Try the exact rational Rodrigues source, finite integration by parts or a
division-free two-direction source identity to reduce I_B+C_B and its actual
denominator. Keep the complete factorial subtraction, every exterior force,
physical endpoint and weighted column content. The turn9 conditional transfer
lemma is elementary and its crucial hypotheses are unproved: do not just name
F_n or repeat that lemma. Obtain an explicit nontrivial all-prime divisor of
the actual g_B, or a paid accepting scalar with a quantitative estimate on an
infinite unchanged original subfamily. State the established NEW logarithmic
denominator saving, including zero if none is proved. Do not infer a bound on
nu from c or reuse the closed scalar-antidifference obstruction as a general
impossibility statement. No new original-size computation is authorized here;
give bounded mathematical inputs if a genuinely new calculation is needed.''',[
 R/'responses/A2_turn9.md',R/'responses/A2_turn8.md',
 {'path':O/'responses/A2_turn6.md','lines':(692,1225)},
 {'path':R/'responses/A4_turn11.md','lines':(927,1343)},
 {'path':R/'responses/A4_turn11.md','lines':(1413,1476)}
],charge+'\n'+arithmetic)

build('A5',8,r'''Continue from the fully read turn7. Seek an INFINITE original
paid scalar consequence of the short adjoint, or an actual all-prime relative
scalar-cofactor bound; another fixed common content factor alone cannot close
the global objective. Evaluate the full head PLUS finite return of (3.15) at a
depth paying actual a or a proved sufficient upper bound, preferably on your
u=1 mod4 subfamily, and prove a growing result rather than extrapolating finite
prefix periodicity. If an explicit recurrence for that accepting scalar can
close a bound, derive it with the actual terminal and full forcing.
Alternatively use actual column saturation to derive a source-based divisor or
bound for delta or the remaining primitive scalar gcd; independent vectors can
still be isotropic, so minor saturation alone is insufficient. Keep the known
3-adic exponential denominator and compare gains at the same original indices.
The coordinator may perform your proposed new L12 u0 calculation after reviewing
the complete finite return; no numerical outcome has yet been supplied. Do not
invent its answer or repeat the completed finite DP. Your turn6 mod8 premises
are under independent review. All dependent original-family uses must state
that review dependency. Give a detailed self-contained mathematical report.''',[
 R/'responses/A5_turn7.md',R/'responses/A5_turn6.md',
 {'path':R/'responses/A5_turn2.md','lines':(190,248)},
 {'path':R/'responses/A4_turn10.md','lines':(499,668)},
 R/'controls/binary_actual_two_valuation_receipt.json',
 R/'controls/binary_original_low_prefix_certificate.json'
],binary+'\n'+arithmetic)
