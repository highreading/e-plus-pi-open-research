from packet_tools import write_packets
from build_next_13_16 import analytic,S02
from build_renewed_14_17 import common

beta_note='''COORDINATOR PROPOSAL, TO AUDIT, NOT AN ACCEPTED THEOREM:
Classical beta evaluation is reused (DLMF5.12). For nonnegative s,H,
4*integral_0^1 x^(2s)*(x^2-1)^H dx
=(-1)^H*2^(H+2)*H!/product_(u=0)^H(2s+2u+1).
For H=3^u, 0<=s<=(H-3)/2, the first H odd factors form complete
residue cycles at every relevant 3-power; their product has valuation
F_H. The extra factor has valuation at most u-1, hence the integral
has valuation -v3(2s+2H+1). Scaling by3^h, h=u+1, gives depth>=2.
This evaluates the FULL atan functional, rather than a selected pole.
It does not itself prove all-depth matrix saturation.

For the weighted polynomial core (y+1)(y-1)^A*(beta0+3y), beta0 a
3-adic unit, finite geometric inverse T_r=sum_(a=0)^(r-1)(-3y/beta0)^a
satisfies (beta0+3y)T_r=beta0 mod3^r as a polynomial identity.
Take k_i=y^i(y-1)^D*T_r, A+D=H. This reduces the FULL rational moment
to beta moments through the required precision, but degree rises by
r-1 and may enter HIGH. Eliminate HIGH and the LOW unit block before
claiming a corrected kernel. Show every correction and precision loss.
Keep the exponential factorial functional f(y^s)=(2s)!, not the
derangement functional. Keep endpoint subtraction, cutoff4n-3 and
the actual primitive unit. Core errors need precision sufficient AFTER
the divisions used for the relevant Schur digit. A fifth-carry claim
cannot follow from a lower bound on raw moment valuations alone.
'''

analytic_note='''COORDINATOR DISTINCT PROPOSAL, TO AUDIT:
Your complete turn17 critical2/3 theorem has been read. A4 is assigned
an independent audit. The next target is b=o(n^(3/4)), for the SAME
actual coordinates, positive metric, forces and whole primitive error.
Bounded archive checks found no completed theorem in this range; DLMF2.4
is classical background, not a high-dimensional theorem imported here.

Improve the first logarithmic derivative remainder by retaining the
SIGNED cubic trace C3=sum(theta_i^3), instead of sum|theta_i|^3.
The positive q-tilted measure is reflection invariant, so E C3=0.
Brascamp-Lieb and your existing Q4 bound suggest
Var C3<=C/n*E Q4=O(d^3/n^3), while Var phase=O(d/n).
Thus E[C3 exp(i*phase)]=O(d^2/n^2). The actual insertion S_j-1=O(d/n)
adds at most O(d^(5/2)/n^(5/2)), which is no larger for d=o(n).
Taylor-expand H_q through cubic, bound the remaining term by Q4,
and center the Q covariance as in turn17. Candidate improved formula:
a_q=d/(1+q)+(d^2/n)*c1(q)+O(d/n+d^3/n^2),
c1(q)=(q-1)/(2*alpha0*(1+q)^3), alpha0=sigma/M.
Do not assume signed cancellation if the actual insertion or its
derivative destroys it; retain the full actual phase denominator.

Similarly expand J_q through its linear signed trace and quadratic
remainder. Candidate beta_q=-d/(1+q)^2+O(d/n+d^2/n), rather than an
absolute sqrt estimate. Its covariance term must be controlled using
the same complex-weight denominator. Higher fixed logarithmic
derivatives remain O(d) from the zero-free disks.
Then first derivative remainder times d/n and beta error times d^2/n^2
are O(d^2/n^2+d^4/n^3). The already computed cubic saddle and derivative
cross term cancel exactly. The next saddle remainder is O(d^4/n^3).
If every bound closes, prove the WHOLE relative law
epsilon=(-1)^(n+1)*4*pi*M^(-2n-b)*(1+o(1)) uniformly b=o(n^(3/4)),
both parities, retaining actual reconstruction, all sectors and
connectors, normality, nonzero whole error, full endpoint and final gcd.
A critical3/4 assertion is separate: d^4/n^3 is then order one. Do not
infer it from this small-range theorem. You may derive next coefficients
as an optional next-target proposal, but identify every unproved virial
and covariance precision explicitly.
'''

tasks={
'A1':('Audit an exact beta-moment approach to corrected weighted kernel lifts',
'''Your turn18 closes the full support map and fourth carry. Reuse these
results rather than reprove them. A4 is tasked to evaluate the actual
fifth digit on81|j,D<H/324. Your independent task is to audit the
coordinator's exact-beta/geometric-core proposal below and derive a
corrected FULL matrix kernel lift, or exhibit its precise obstruction.
Use full rational moments to contract all layers and HIGH corrections.
If it closes fifth carry, independently derive its rank and endpoint;
if only a raw valuation lemma closes, state it as such, with no all-depth
inference. An all-depth recurrence is valuable only if an actual formula
and uniform precision proof are supplied. Retain the final denominator
interface and actual complete-error nonvanishing obligations.
'''+beta_note,
[S02+'main/PAIRED_DERANGEMENT_LINEAR_S_CONSTRUCTION.md'],
['A1_turn18','A4_turn12','A4_turn13','A4_turn15','A4_turn18'],[]),
'A4':('Evaluate the fifth weighted Schur digit and audit critical two-thirds analysis',
'''Your turn18 and A1turn18 independently close fourth carry. The distinct
next arithmetic target is the actual fifth digit: restrict to81|j and
D<H/324, so the sharpened original Qloc has core3y-71 modulo243.
Retain five lower-pole layers with weights1,3,9,27,81 and grids down to
H/81. Re-expand the actual HIGH inverse and LOW-unit Schur elimination
one more digit, including every endpoint and the actual primitive unit.
Evaluate the resulting fifth carry and rank, rather than only naming
uncomputed arrays. Prove a zero matrix or show an explicit survivor;
identify the actual endpoint image and consequent gcd LOWER bound.
Do not subtract unrelated determinant/cofactor lower bounds to give q.
A1 independently explores the exact beta/core inverse approach; the
proposal below may help evaluate all-pole contractions, but is not a
theorem. Fourth cancellation is no all-depth induction by itself.

Independently audit the FULL A3turn17 critical b~kappa*n^(2/3) law,
including first derivative, second derivative, signed cubics, actual
phase denominator and reciprocal partition identity. Record exact
passes or repairs, not an extrapolation to a different metric. A3 now
works on b=o(n^(3/4)) by improving signed cubic-trace remainders.
'''+beta_note,
analytic,
['A1_turn18','A4_turn12','A4_turn13','A4_turn15','A4_turn18','A3_turn17'],[]),
'A3':('Prove the relative whole error below the three-quarters degree boundary',
analytic_note,
analytic,
['A3_turn14','A3_turn16','A3_turn17','A4_turn18'],[])
}

if __name__=='__main__':
    write_packets(19,{k:tasks[k] for k in ('A1','A4')},common)
    write_packets(18,{'A3':tasks['A3']},common)
