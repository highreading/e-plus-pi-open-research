from packet_tools import write_packets
from build_renewed_14_17 import common
from build_next_13_16 import S02

tasks={
'A2':('Close the norm-zero locus and the two remaining MAIN29 initial grades',
'''Your turn16 has been read in full. Reuse the proved disappearance of
grades>=3 and the explicit grade2 residual-norm factor. The distinct
next target is to evaluate the actual norm D0 in terms of your genuine
residual T(N1,H), including every zero low-digit multiplier. Derive its
exact factor or a rigorous zero-locus statement; do not identify D0=0
with T=0 by assumption. The original higher digits remain those of3^a.
Then evaluate grade0+grade1 in the complete scalar modulo29^6, keeping
all ghost paths and factorial boundaries. Prove a common norm factor
or give a precise surviving contraction. Prior Laurent-coefficient
nonvanishing did not settle the scalar; the last factorial block is
already handled and need not be rederived. The evaluated Phi=58zmod841
is available. An integral discrete-adjoint relation is useful only if
the full finite boundary is included and its scalar contraction proved.
Keep original exponent class, endpoint, final gcd and whole real error.

Also independently audit A5turn15's infinite original r18mod32 theorem:
fresh whole-column Y parity, full odd endpoint, reconstruction20/22/23,
the evaluated convolutions39/43 and norm>=3. The independent fixed
degree17/15 operator control is supplied and passes every reduction to
the earlier P/Q receipt. Its full coefficients are finite input, not
an infinite sampling proof. A5 now evaluates (H-N)/8mod2 using the
existing complete lift. Give precise repairs if any of the turn15
coordinate formulas or infinite convolution steps fail.
''',
[S02+'main/PAIRED_DERANGEMENT_LINEAR_S_CONSTRUCTION.md',
 S02+'agent3_analysis/PROPORTIONAL_PRIMITIVE_CENTER_INTERFACE.md'],
['A2_turn13','A2_turn15','A2_turn16','A5_turn15'],
['proportional_twenty_nine_interior_fourth_compact.json','binary_fixed_lift_control.json']),
'A5':('Evaluate the third binary contracted discrepancy with the existing complete lift',
'''Your turn15 has been read in full. Its assigned discrepancy vanishes,
and the claimed alpha,gamma>=3 is independently assigned to A2 for
audit. A coordinator-authored finite operator computation confirms all
P+mod16 and Q+mod32 Newton coefficients and their reductions. Reuse
the complete seven-boundary lift and exact convolution methods.

The next target on the SAME original r=18+32u domain is
Delta3=(H-N)/8mod2, along with the actual next norm digit when useful.
Because BOTH columns are even, X,Ymod8 suffice: changing either by8
changes H-N by a multiple of16. Hence the EXISTING raw A+=2Xmod16,
B+=4Ymod32 and degree17/15 closure suffice for this next scalar.
Do not request or develop a higher raw precision unless a separately
identified intermediate division actually needs it. Keep the seven
factorial tails and whole-force bound; retain all large binomial kernels,
actual finite boundaries, off-pair even and odd positions, and endpoint.
Evaluate the combined scalar, not only another unknown polynomial.
If it vanishes on all r18mod32, prove it. If a further low-digit subclass
is required, derive the necessary condition and account for the omitted
subclasses in the original-domain statement. If nonzero, explain the
precise norm/mixed valuation consequence without subtracting lowerbounds.
An all-depth gamma-alpha bound remains the useful final goal, but a
stable induction must retain every boundary enlargement and carry.
Never iterate the finite degree truncation without a uniform proof.
The distinct next digit is absent from the archive; Granville's binary
binomial congruence framework is reused as primary prior background.
''',
[S02+'main/PAIRED_DERANGEMENT_LINEAR_S_CONSTRUCTION.md',
 S02+'agent3_analysis/PROPORTIONAL_PRIMITIVE_CENTER_INTERFACE.md',
 S02+'agent3_analysis/PROPORTIONAL_ACTUAL_CENTER_SIGNED_RATE.md'],
['A5_turn12','A5_turn14','A5_turn15','A2_turn16'],
['binary_fixed_polynomial_control.json','binary_fixed_lift_control.json'])
}
if __name__=='__main__':
    write_packets(17,{'A2':tasks['A2']},common)
    write_packets(16,{'A5':tasks['A5']},common)
