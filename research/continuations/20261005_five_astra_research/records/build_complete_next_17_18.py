from packet_tools import write_packets,HERE
from build_renewed_14_17 import common
from build_next_13_16 import analytic,S02
note='COORDINATOR_COMPLETE_COORDINATE_AND_CUBIC_NOTES.md'
def packet_note():
    # Complete coordinator note is included as mathematical data.
    return (HERE/note).read_text()
tasks={
'A1':('Close the actual support map and sharpen the polynomial law',
'''Your turn17 correctly isolates the full divided-coordinate interface.
The complete earlier A1turn9 source is now supplied, along with the
coordinator's explicit regular block, full target force and exceptional
coordinate map. Audit every normalization in that note. If valid, close
the sharpened Qloc modulo3^(m+2) unconditionally on m>=2, rather than
leaving the asserted support as an unavailable hypothesis. The complete
constant row is essential. Then independently check the note's weighted
fourth-carry identities using A4turn12/13/15 exact matrices. A4 is tasked
to finish them, but your independent arithmetic perspective should catch
any precision, orientation or unit error. The earlier one-edge assumption
is corrected to two-edge support. Keep the final gcd and whole error
interfaces; no exact denominator follows from Smith lower bounds.
\n'''+packet_note(),
[S02+'main/PAIRED_DERANGEMENT_LINEAR_S_CONSTRUCTION.md'],
['A1_turn9','A1_turn14','A1_turn15','A1_turn17','A4_turn12','A4_turn13','A4_turn15'],
['weighted_true_linear_jet_control.json']),
'A4':('Evaluate fourth carry from the complete actual block formulas',
'''Your turn17 source-gap diagnosis is accepted; the needed COMPLETE
A4turn12/13 block definitions and A1turn14 modulo81 proof are now supplied.
The coordinator note derives the missing full divided-coordinate force
map. Audit it, then evaluate all four terms in (*) from actual entries.
The note corrects the prior one-edge claim: F e_d is supported at most
on m-1,m modulo3, which still suffices with the actual R and K. Prove
the extended lower Schur diagonal, J e_d, two-edge support and inverse
orientation, retaining every pole cutoff, full endpoint and primitive
unit. Either finish T4=0 with actual endpoint image and gcd lower bound,
or exhibit a specific surviving term. Do not respond only with a new
name for the same unknown vector. You have all actual formulas needed
to derive it. Also independently audit A3turn16 whole relative law on
b=o(n^(2/3)); its full sources are included, with same metric scope.
\n'''+packet_note(),analytic,
['A1_turn9','A1_turn14','A1_turn17','A4_turn12','A4_turn13','A4_turn14','A4_turn15','A4_turn17','A3_turn16'],[]),
'A3':('Evaluate the cubic cancellation at the critical two-thirds degree',
'''Your turn16 gives the relative theorem below the2/3 boundary; A4 now
independently audits it. The distinct next target is b~kappa*n^(2/3),
kappa in a fixed positive compact interval. The coordinator note derives
a candidate cancellation of the order-one cubic saddle difference with
the actual derivative's quadratic-characteristic correction. Verify the
full coefficients and signs, not only a formal pure saddle expansion.
Use the SAME q-tilted positive ensemble, endpoint-safe virials, VarQ,
reflection and the ACTUAL phase denominator. Avoid absolute remainder
estimates exp(Cd^2/n), now large. The second logarithmic derivative needs
its leading value up to o(d). The first derivative remainder, when
multiplied by d/n, must tend zero. Keep all original sectors, connectors,
actual reconstruction, complete exponential force and endpoint. If the
relative constant still4*pi, prove its uniformity and full nonvanishing.
A further b=o(n^(3/4)) law is a separate optional target only if all
derivative remainders are strengthened enough; do not infer it from a
critical2/3 result. Archive checks locate no completed critical2/3 theorem;
DLMF scalar saddle methods remain classical background.
\n'''+packet_note(),analytic,
['A3_turn14','A3_turn16','A4_turn14'],[])
}
if __name__=='__main__':
    write_packets(18,{k:tasks[k] for k in ('A1','A4')},common)
    write_packets(17,{'A3':tasks['A3']},common)
