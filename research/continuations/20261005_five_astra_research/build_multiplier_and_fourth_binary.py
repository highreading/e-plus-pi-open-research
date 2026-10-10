from packet_tools import write_packets
from build_renewed_14_17 import common
from build_next_13_16 import S02
tasks={
'A2':('Evaluate the remaining corrected norm multiplier explicitly',
'''Your turn17 has been read in full. The coordinator's requested exact
four-digit computation is complete: kappa0=11,kappa1=18. The base norm
multiplier for d0..24 is
(5,25,21,14,23,15,7,9,9,28,6,9,6,9,6,28,9,9,7,15,23,14,21,25,5),
all nonzero, and d25..28 zero. All707281 low-digit cases were checked.
Stronger than requested, the tau=-1 product has at least THREE low
carries uniformly, so mu_-1=0 in your formula. Prove that directly:
digit0 forces one carry across the weight and second binomial (N0=2,
b0=27,c_-1,0=28), and digits1 and3 force the other two as in your proof.
This removes the h0 term from the base normalized column.

Main next target: evaluate K01 and Lambda as an explicit finite
polynomial in the needed actual Laurent moments/central coefficients,
not only as an instruction to sum ghost paths. The bounded P1 forcing
and contact closure have indices<=58; all low parameters are fixed on
the original exponent class. Identify the remaining moment parameters
(e.g. J0,J29,J58 if sufficient), derive every coefficient and either
classify Lambda zeros or state their explicit scalar condition. Use
known Frobenius/contiguous moment identities to reduce those parameters
when justified. Keep every finite boundary and higher digit.
Then evaluate the remaining lowest-grade defect on the true norm-zero
locus, including d25..28, rather than only T=0. A discrete-adjoint
approach may avoid enumerating all carry paths but must retain the
boundary contribution. No global denominator follows from a factor
whose multiplier is still unevaluated.

Independent secondary audit: A5turn16 (full source) now claims Delta3=0
and alpha,gamma>=4 on the SAME r18mod32 class. Check off-pair support,
sampled-polynomial K(16s)=16mod32, unrestricted convolution and the
next norm parity. Retain final gcd and whole-error scope.
''',
[S02+'main/PAIRED_DERANGEMENT_LINEAR_S_CONSTRUCTION.md'],
['A2_turn13','A2_turn15','A2_turn16','A2_turn17','A5_turn16'],
['twenty_nine_low_constants_control.json','binary_fixed_lift_control.json']),
'A5':('Evaluate the fourth contracted binary carry with its required precision',
'''Your turn16 is read in full and assigned to A2 for independent audit.
It proves every defect summand divisible16 and alpha,gamma>=4, but
does not decide (H-N)/16mod2. Evaluate that scalar on the same original
r18mod32 domain, including actual next norm digit if useful.
Both columns are even, so X,Ymod16 suffice for H-Nmod32: raw A=2Xmod32
and B=4Ymod64. The existing raw16/32 lift alone is not sufficient for
all products. The seven boundary factorial tails may still suffice,
since the next b+7 factor has depth7; derive all seven residuesmod64
from the actual factorial products and prove the whole-force cutoff.
Derive the complete P/Q forcing at these precisions before using any
reference substitution. Expected degree bounds21/19 need a proof.

Useful coordinator observation TO AUDIT: on r18mod32, h=n/2 is1mod32.
In the integral divided-power ring, phi^2=1+2U, so
phi^(2h)=(1+2U)^h congruent phi^2 mod64 if all k>=2 binomial terms
have depth>=6. This may retain the same four contact coefficients
(-1,2,-3,3) mod32, but verify the coefficient ring and weighted losses.
The normalized P forcing is a separate calculation; do not infer it
solely from this contact identity. Seven factorial residues must be
recomputedmod64, not reusedmod32 silently.

Use the infinite sampled-polynomial/convolution mechanism to evaluate
paired contributions; keep off-pair even, odd and the full endpoint.
Prove a zero scalar, a specific nonzero carry or an explicit further
subclass condition with original-domain accounting. All-depth alignment
requires a stable induction beyond finite polynomial closure. Keep
the actual primitive denominator and whole real error. Bounded archive
checks locate no completed fourth carry on this domain; classical
binary binomial congruences and your exact lower-layer proofs are reused.
''',
[S02+'main/PAIRED_DERANGEMENT_LINEAR_S_CONSTRUCTION.md',
 S02+'agent3_analysis/PROPORTIONAL_PRIMITIVE_CENTER_INTERFACE.md',
 S02+'agent3_analysis/PROPORTIONAL_ACTUAL_CENTER_SIGNED_RATE.md'],
['A5_turn12','A5_turn14','A5_turn15','A5_turn16','A2_turn17'],
['binary_fixed_polynomial_control.json','binary_fixed_lift_control.json'])
}
if __name__=='__main__':
    write_packets(18,{'A2':tasks['A2']},common)
    write_packets(17,{'A5':tasks['A5']},common)
