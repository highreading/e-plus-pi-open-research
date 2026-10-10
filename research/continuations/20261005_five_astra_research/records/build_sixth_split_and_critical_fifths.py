from packet_tools import write_packets
from build_renewed_14_17 import common
from build_next_13_16 import S02,analytic
sixth='''The weighted sixth target remains unresolved; this is a continuation,
not a repeated new target. Domain243|j,D<H/8748, full actual core depth7,
actual monomial matrices, LOW projections, endpoints and all poles.
A4turn21 now proves direct L_ext annihilationmod729 and the exact identity
T6=-(A9/9+A27/3+A81)mod3, with A9 in9 and A27 in3. Reuse this completed
identity. A1 and A4 now work on disjoint parts, so together every
remaining contraction is evaluated rather than merely renamed.
'''
tasks={
'A1':('Evaluate the higher digits of the lower sixth contractions and audit MAIN29',sixth+'''
Your exact Jacobi core law is accepted as core-only; its unavailable
actual precision is retained. Do not try to transfer it without the
inverse and endpoint loss. Instead MAIN evaluate A9mod27 and A27mod9,
including actual nonedge F/J entries and LOW-unit projections. A4 now
handles A81mod3 separately. Derive full coefficient bands and unit
inverses at required depths, not just A9in9,A27in3 again. If half-grid
gaps kill every component, prove it at the new precision; otherwise
give the explicit surviving matrix and endpoint image. The actual
beta=-71-A must retain any digit needed after division. Cutoffs and
finite HIGH ranges remain part of every convolution.

Secondary independent audit of A2turn18: K01=0, corrected multiplier
C_n^2*f(d), and D0=0=>M0=0 on the actual four-digit exponent class.
The coordinator tested all707281 low cases for eachq=-60..87 and all
support/high-carry conditions; those finite digit tests pass but do not
establish the high-index factorization or full inverse by themselves.
Audit Lemma2's e+u=1, dependence of factorial units on higher indices,
contact correction at old support, last factorial block and actual
endpoint. Both MAIN29 and binary metrics are FALLING:
omega_j=j!*binom(n+2,j). A2turn18's rising label in section7 is a wording
error and must not change the actual W_j used in the proof. Give a pass
or precise repair rather than inferring authority from the other answer.
''',[S02+'main/PAIRED_DERANGEMENT_LINEAR_S_CONSTRUCTION.md'],
['A1_turn20','A1_turn21','A4_turn20','A4_turn21','A2_turn15','A2_turn17','A2_turn18'],
['twenty_nine_carry_support_control.json']),
'A4':('Evaluate the new sixth contraction and audit the subcritical four-fifths theorem',sixth+'''
MAIN evaluate A81mod3 from your exact expression(16). A1 separately
evaluates A9mod27,A27mod9; do not duplicate those parts. Derive actual
Fmod3,Jmod3 with their HIGH finite ranges, LOWunit projections and
unit-pole pairing. Evaluate JRJT, KRFRJT and transpose, KRFRFRKT,
JRFRFe_d, KRFRFRFe_d and (FRFRFRF)dd. Extended direct annihilation and
small corners are available but cannot alone delete nonedge terms.
If a uniform support proof gives zero, state the complete actual
polynomial/half-grid argument. If a term survives, evaluate its rank
and image, retaining the actual endpoint. No sixth gcd bound follows
until the two other normalized contributions are also evaluated.

Independently audit full A3turn20 below4/5 theorem. Check endpoint-safe
Q8 virial, signedC5 actual complex expectation, improved third derivative
including Poincare fourth-moment bound, scalar error exponents and
complete residual/normality/diagonal-metric transfer. Keep all previously
proved contour/residual estimates as explicit dependencies and identify
any unavailable defining formula, rather than calling conditional
interfaces a newly proved unconditional whole theorem.
''',analytic,
['A1_turn20','A4_turn20','A4_turn21','A3_turn19','A3_turn20'],[]),
'A3':('Evaluate the critical four-fifths stationary coefficient with actual moment errors',
'''Your turn20 is read in full and assigned to A4 for independent audit.
The distinct next target is criticalb~kappa*n^(4/5),0<kappa0<=kappa<=kappa1.
Archive/current bounded query leaves this exact critical range open;
DLMF2.4 and the existing proportional equilibrium calculation are prior
methods. Do NOT redo generic steepest descent or use an unverified
high-dimensional theorem. Reuse the exact equilibrium-resolvent formulas
in PROPORTIONAL_SHIFTED_SADDLE_PROGRESS: its two formal stationary phase
values differ exactly -(2+c)logM. If its analytic small-c expansion
supplies the fifth coefficient, reuse it instead of rediscovering an
already calculated formal cancellation. Finite-n actual precision must
still be proved separately.

Required actual logarithmic derivative precisions for the fifth value:
first through d^4/n^3, second through d^3/n^2, third through d^2/n,
fourth leading chain-signed(-6d/(1+q)^4). Every omitted term is multiplied
respectively by d/n,d^2/n^2,d^3/n^3,d^4/n^4. Safe higher virials and
centered covariances may give EQ6=5d^4/(alpha0^3*n^3)+lower error;
EQ4 next coefficient and EQ second correction are also needed. Use
explicit safe fields/loop identities, retaining circular cotangent,
finite-degree lower terms and actual complex-weight denominator.
Gaussian Catalan values are conjectural inputs until justified here.

An alternative is a rigorous small-c comparison of actual finite-n
characteristic log derivatives with the exact equilibrium resolvent,
with error small enough after those multipliers. Uniform free-energy
O(log n) would NOT suffice for an order-one critical coefficient.
Prove whichever route supplies explicit error control. The retained
actual insertion defect/phase estimates are O(d/n); check all centered
moment losses. Compute fifth stationary correction; if plus/minus
cancel, prove whole relative4pi at critical4/5 with scalar remainder
O(d^6/n^5)=o1, original remote sectors/connectors and full E_j/endpoint.
If a nonzero coefficient survives, give its explicit limiting factor.
Do not infer all-sublinear symmetry from finitely many cancellations.
Keep final gcd and actual primitive denominator separate.
''',analytic+[S02+'agent3_analysis/PROPORTIONAL_SHIFTED_SADDLE_PROGRESS.md'],
['A3_turn18','A3_turn19','A3_turn20','A4_turn21'],
['quartic_saddle_algebra_control.json'])
}
if __name__=='__main__':
    write_packets(22,{k:tasks[k] for k in ('A1','A4')},common)
    write_packets(21,{'A3':tasks['A3']},common)
