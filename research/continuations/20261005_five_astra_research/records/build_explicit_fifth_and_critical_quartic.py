from packet_tools import write_packets,HERE
from build_next_13_16 import S02,analytic
from build_renewed_14_17 import common
note=(HERE/'COORDINATOR_FIFTH_AND_QUARTIC_PROPOSALS.md').read_text()
tasks={
'A1':('Evaluate every explicit fifth contraction by actual support',
'''Your turn19 raw beta audit is accepted, including the exact depth2
HIGH obstruction. The coordinator now supplies a distinct LOW-first
fifth contraction expansion and candidate actual band proofs. Evaluate
all terms, on the smaller infinite D<H/972 domain, using the original
Z columns, not uncorrected geometric columns. The direct-beta law is
already available. Audit every new support/precision claim; show actual
coefficients or sufficient proved band support. Finish T5 and endpoint,
or exhibit the specific surviving term. The full A4turn19 source is
included. A4 independently evaluates the same contractions.
'''+note,
[S02+'main/PAIRED_DERANGEMENT_LINEAR_S_CONSTRUCTION.md'],
['A1_turn18','A1_turn19','A4_turn12','A4_turn13','A4_turn15','A4_turn18','A4_turn19'],[]),
'A4':('Close the evaluated fifth matrix and audit signed cubic improvement',
'''Your turn19 direct-beta lemma and critical2/3 audit are accepted.
The coordinator has reduced the remaining fifth arithmetic to explicit
contractions and actual band identities, supplied below. Evaluate each
one rather than restating the need for HIGH corrections. The smaller
D<H/972 infinite subclass gives useful index margins. Retain the core
at its available729 precision before divisions; F and J are actual
integral arrays with all higher digits. A1 independently audits them.
Also independently audit A3turn18 below3/4 theorem, especially the
signed C3 concentration with actual insertion and derivative covariance.
A3 now separately proves critical3/4 sharp moment inputs for the exact
quartic cancellation; do not assume that result in this audit.
'''+note,
analytic,
['A1_turn19','A4_turn12','A4_turn13','A4_turn15','A4_turn18','A4_turn19','A3_turn18'],[]),
'A3':('Prove the sharp moments and critical three-quarters quartic cancellation',
'''Your turn18 is read in full and assigned to A4 for independent audit.
The coordinator has now computed an exact proposed quartic cancellation,
not just an O(1) bound. Its required sharper moments and derivative
coefficients are supplied in the note. Prove them with endpoint-safe
virials in the SAME positive tilted ensemble, not a formal Gaussian
replacement. Verify every coefficient, actual insertion/phase covariance,
full denominator, scalar stationary value and remainder. Target
kappa0*n^(3/4)<=b<=kappa1*n^(3/4), full same-center relative law.
All lower-order identities are already known; reuse them. The receipt
is exact algebra only, not an analytic theorem. If cancellation fails,
give the corrected coefficient and relative factor. A further o(4/5)
theorem is optional and needs its own sufficient precision proof.
Bounded archive and primary DLMF2.4 checks locate no completed exact
critical3/4 result for this construction; no exhaustive novelty claim.
'''+note,
analytic,
['A3_turn17','A3_turn18','A4_turn19'],['quartic_saddle_algebra_control.json'])
}
if __name__=='__main__':
    write_packets(20,{k:tasks[k] for k in ('A1','A4')},common)
    write_packets(19,{'A3':tasks['A3']},common)
