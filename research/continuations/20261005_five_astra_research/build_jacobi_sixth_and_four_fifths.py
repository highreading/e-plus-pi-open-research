from packet_tools import write_packets
from build_renewed_14_17 import common
from build_next_13_16 import S02,analytic
tasks={
'A1':('Use classical Jacobi-Christoffel identities for the exact core cofactor ratio',
'''Your fifth proof passes coordinator review and independently A4turn20.
Reuse it. A4 now evaluates the sixth carry. Your distinct next target
is a closed relative endpoint-cofactor law for the exact linear-core
moment matrix, followed by a justified transfer to the ACTUAL matrix.
Bounded archive searches locate classical beta/Christoffel work for
other functionals and the weighted DYADIC Schur kernel. That established
mechanism is reused. Primary checked DLMF5.12 and18.3, Miller/Stanton
arxiv1704.03539 and Krattenthaler arxiv2101.04225v5/Theorem1.
No claim of a new generic Christoffel formula is made.

For Qcore=(y+1)(y-1)^A*(beta+3y), the atan moment equals
3^h*integral_0^1 x^(2s)*(x^2-1)^A*(beta+3x^2) dx.
After t=x^2 this is a constant times the Jacobi measure
t^(-1/2)*(1-t)^A dt, modified by beta+3t. Set r=-beta/3.
For monic Jacobi p_k and unmodified norm h_k, classical identities give
det Gcore=constant^k*3^k*(-1)^k*p_k(r)*det Gbase,
p_k^c(t)=[p_(k+1)(t)-a_k*p_k(t)]/(t-r),
a_k=p_(k+1)(r)/p_k(r), h_k^c=-3*a_k*h_k.
Audit every scalar, degree and nonzero condition. The exact endpoint
kernel is sum_(k=0)^m p_k^c(-1)^2/h_k^c with the common scalar restored.
It directly evaluates cofactor/determinant ratio for Gcore. Derive
actual3-adic valuations or an explicit all-depth sum whose dominant
terms/cancellation are evaluated, not just another inverse symbol.
Jacobi parameters are A,-1/2; its monic normalization is essential.

Gcore is a surrogate until transfer is proved. The actual Qloc error
has depth v3(j)+2; the factorial term and endpoint errors remain.
Determine exact inverse/unit losses for transfer at available precision,
including transported endpoint. Never infer Smith equivalence from a
rational orthogonal basis whose transformation is nonintegral.
If transfer fails, give the first precise unavailable depth and an
explicit core-only result. Final q requires the actual ratio, not
subtraction of unrelated lower bounds. Keep whole-error scope.
''',
[S02+'main/PAIRED_DERANGEMENT_LINEAR_S_CONSTRUCTION.md',
 S02+'main/GENERAL_POLE_RANK_M_GATE.md',
 S02+'agent1_arithmetic/WEIGHTED_REGULAR_EXACT_DYADIC_ENDPOINT_THEOREM.md'],
['A1_turn19','A1_turn20','A4_turn12','A4_turn13','A4_turn20'],[]),
'A4':('Evaluate the sixth carry and audit critical three-quarters analysis',
'''Your fifth proof agrees with A1turn20. Reuse those completed terms.
The distinct next target is sixth saturation on243|j,D<H/8748.
Available actual core precision is at least3^7 before divisions; use
beta=-71-3M0, including its depth6 constant term if a division needs it.
Prove full direct L_ext annihilation modulo729 through every extended
LOW index used. The original fivefold radical has a sixth form
T6=Rrad/243mod3. With LOW-first exact Ehat=E0+3F, exact
V=-2e e_m^T+3K+9J (J includes every higher digit), evaluate
V*sum_(ell=0)^4 (-3)^ell R(FR)^ell*V^T modulo243,
then divide81 for T6. Retain negligible-force proofs before dropping
ZTLU, the original endpoint and cutoff, all pole pairs and LOWunit
corrections. New F/J digits must be derived from actual entries.
Do not assert recurrence because all earlier layers vanished.

Potential general mechanism TO AUDIT: after resolving every coefficient
to cost<=r, pole bands are half-grids (odd*H/3^s-1)/2, while inverse
coefficient bands are integer multiples of H/3^s plus degree<=D.
Closed HIGH contractions may retain a half-grid parity gap, hence
cannot hit an inverse band when D is sufficiently small. Any all-depth
lemma needs an explicit precision-weighted support induction with
integer shifts, finite boundaries and LOW projections. Derive the sixth
first if this uniform assertion remains unproved.

Independently audit full A3turn19 critical3/4 whole theorem, including
third-derivative cumulant, quartic stationary remainder, original scalar
contours and complete residual. Your prior virial audit supplies its
sharp moments. A3 now separately strengthens signed fifth remainders
to seek b=o(n^(4/5)); do not assume that result.
''',analytic,
['A1_turn20','A4_turn12','A4_turn13','A4_turn15','A4_turn20','A3_turn19'],[]),
'A3':('Strengthen signed fifth remainders for the whole law below four-fifths degree',
'''Your critical3/4 report is read in full; A4 audits it independently.
The distinct next target is b=o(n^(4/5)), retaining the SAME actual
center/metric/forces and full denominator. Archive/prior reports leave
this range explicitly open; DLMF2.4 methods are reused.

Coordinator proposal: safe field t^7*g(t)/M gives E Q8=O(d^5/n^4).
For SIGNED C5=sum theta^5, reflection E C5=0, BLVar C5<=C/n*E Q8
=O(d^5/n^5). With VarphaseO(d/n) and S_j-1O(d/n), its ACTUAL weighted
mean is O(d^3/n^3). Expand the first logarithmic derivative through
degree5, using this signed mean, signed C3/X and Q6 for the remainder.
Your sharp Q and Q4 coefficients then have an improved remainder
O(d/n+d^4/n^3) (harmless smaller terms may remain). Multiplied by d/n,
it tends zero for d=o(n^(4/5)). The absolute fifth estimate used at
critical3/4 alone is not sufficient here.

Your second derivative remainder O(d/n+d^3/n^2) already has sufficient
precision after multiplication by d^2/n^2. Improve U^(3) by retaining its
SIGNED linear trace and bounding the rest by Q, not sum|theta|. Candidate
U^(3)=chain-signed2d/(1+q)^3+O(d/n+d^2/n+(d/n)^(3/2)). Prove all centered
covariances/cumulants with the actual complex-weight denominator.
Its remainder times d^3/n^3 then tends zero. The controlled quartic
coefficient still cancels; scalar next remainder is O(d^5/n^4).
If every step closes, prove whole4*pi relative law uniformly below4/5,
both parities, all actual coordinates and positive diagonal metrics,
outer sectors/connectors, full E_j, endpoint, normality and final gcd.
Critical4/5 is a separate target with a fifth stationary coefficient;
do not infer it from the subcritical theorem. An exact symmetry for
all sublinear b would be valuable only if its full actual insertion
and scalar-contour transformation are derived, not guessed from several
coefficient cancellations.
''',analytic,
['A3_turn17','A3_turn18','A3_turn19','A4_turn20'],
['quartic_saddle_algebra_control.json'])
}
if __name__=='__main__':
    write_packets(21,{k:tasks[k] for k in ('A1','A4')},common)
    write_packets(20,{'A3':tasks['A3']},common)
