from packet_tools import write_packets
from build_next_13_16 import S02, common
from build_source_closure_and_coordinate_spread import common

a2='''Your turn22 has been read in full. The coefficientwise third-defect
reduction, explicit boundary correction and off-central moment recurrence
are useful. They are mathematical claims subject to audit; the 50-element
Gamma tables remain unevaluated. The coordinator is preparing bounded
controls, but a 25-fold full low loop times all Laurent powers is costly.

MAIN reduce the required low computation analytically before asking for
another huge low loop. First derive the COMPLETE h_B Newton coefficient
vector modulo29 from your formal J29 construction, and its reconstructed
Laurent coefficients, including the contact operator and all endpoint
absorption. Then exploit existing kappa=(11,18), g=(26,3), low support9108,
and the two shape polynomials ell0=d+7-J,ell1=3-J to evaluate R29 or prove
it belongs to span K_d and hence Gamma1=0. A leading constant analogy is
insufficient: every new low coefficient contraction must be explicit.
If new finite constants are genuinely needed, give their minimal exact
definition independent of d (a short fixed table), with all raw binomial
moduli, formulas and contact coefficients sufficient for the coordinator
to implement them without copying external code.

Then handle RC: separate degree-zero normalizations that vanish under
L_d from the first low-unit harmonic correction. Give a two-variable
fixed polynomial, or a universal finite set of low contraction constants,
instead of25 different complete arithmetic reconstructions. Verify the
claim that higher digits N,h cannot enter RC after division by29: the
leading cancellation must hold as an ordinary polynomial at the lifted
parameters, not only as values on F29. Retain parity, all negative boundary
powers, finite ranges and the explicit unfrozen boundary correction.
State the first nonzero obstruction if this compression fails.

Do not re-audit previous error laws or primitive formulas at length. Keep
them as precise dependencies and use the answer for the missing coefficient
evaluation. No arbitrary interpolation may discard ordinary derivatives.
'''

a5='''Your turn20 has been read in full. The central forcing, polynomial
parameter transfer, complete P64, raw moment identities, w>=4 exclusion,
and31-residue support reduction are valuable advances. The fifth scalar
convolution9.3 remains unevaluated. A4turn27 independently passed the
complete Q128 transfer and nextnormN64, so Q5 may now be reused at that
audited scope; it still does not evaluate H-N. A coordinator fixed moment
coefficient control is being prepared from your explicit formulas.

MAIN evaluate the unit-sensitive convolution rather than repeating its
definition. Perform seven-level 2-free factorial stripping on EACH
retained binomial moment and weight, keeping a common higher kernel and
all borrow polynomials. For each low residue, determine the actual
required unit precision from its known weight depth, then contract all31
residues coefficientwise before touching the high-index sum. Look for a
polynomial identity in the shared higher-binomial variables that vanishes
on the true commonzero, or a finite carry-state evaluation with explicit
state matrices and output, not an unevaluated length-D sum.

The prior nextnorm count gives N64=48T+32chi, C1=2T exact; it may be reused,
but every mixed coefficient must come from V_s rather than inferred from
the norm. Off-pair depth3/depth2 terms must be retained. Coordinator finite
count controls confirm the supplied DP on401 auxiliary odd D and64 genuine
original exponents; these are not an infinite proof or population result.

At minimum derive the COMPLETE fifth mixed digit for the genuinely
populated subclass r50mod128 (D7mod8, T=0 as an integer), where N64=0 but
H32 currently unknown. Prove whether H64=0 there or supply an explicit
remaining high-digit parity. A result for this subclass alone must be
scoped as such; don't infer all-zero-locus alignment. It is acceptable to
request a small fixed contraction/carry certificate with exact formulas,
but don't replace the main evaluation with another support-only statement.
Keep originalr, actual finite endpoint, final gcd, denominator and whole
error. No unrestricted valuation bound is presumed.
'''

if __name__=='__main__':
    write_packets(23, {'A2':('Compress and evaluate the third-defect coefficient tables',a2,
      [S02+'main/PAIRED_DERANGEMENT_LINEAR_S_CONSTRUCTION.md'],
      ['A2_turn13','A2_turn15','A2_turn18','A2_turn20','A2_turn21','A2_turn22'],
      ['twenty_nine_mixed_low_control.json','twenty_nine_carry_support_control.json',
       'twenty_nine_offcentral_control.json'])},common)
    write_packets(21, {'A5':('Evaluate the fifth bilinear carry convolution',a5,
      [S02+'main/PAIRED_DERANGEMENT_LINEAR_S_CONSTRUCTION.md'],
      ['A5_turn17','A5_turn18','A5_turn19','A5_turn20','A4_turn27'],
      ['binary_fifth_p_control.json','binary_fifth_q_control.json','binary_next_count_control.json',
       'binary_fifth_moment_control_compact.json'])},common)
