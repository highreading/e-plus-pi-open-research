from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from build_next_packets import make,R,C
from build_memory_kernel_round import gate
make('A4',22,'''Independently audit A5turn19's exact fixed-denominator rational lifts Q_U,Q_L,Q_B, each coefficient target, finite-boundary encoding and ordinary expansion convention. Verify the prime-power Cartier transition including its negative-binomial exponent, denominator padding, layer precision and degree boxes. Check all numerical dense20bit complexity claims; do not turn an upper-bound implementation cost into an impossibility lower bound. Compare known primary Rowland--Yassawi methods with the actual parameterlift, and identify any reduction in variables/degrees justified by the common upper n+2 in the two weights.

Audit the actual76x76 endpointSchur formulas, maximal lowerindex227, F interval and correct primal/adjoint transpose orientation. These are proposed exactboundedoriginalu0 computations, not a Gramoutput. Coordinator is personally implementing the complete endpointmatrix and both inverse residuals, without executing remote code. Yourturn21 already accepts the operator/particular-input commutator certificate; its limitations are retained. The new recurrencekernel receipt passes522 sharper allphase/highprecision propagators plus260completeauxiliary source/particular checks and52independent polynomial/productimpulse checks. Audit the supplied new source, especiallyq_d degree, its shifts, the complete source cutoff, finite endpoints and scope. Give a corrected reusable exact identity if a claim fails. Original norm/mixed laws, true norm cancellation, fullgcd andwholeform remainopen.''',
     [R/'responses/A5_turn19.md',R/'responses/A4_turn21.md',
      C/'recurrence_kernel_audit_receipt.json',C/'recurrence_kernel_audit_coordinator.py',
      C/'original_binary_operator_audit_receipt.json'],gate)
