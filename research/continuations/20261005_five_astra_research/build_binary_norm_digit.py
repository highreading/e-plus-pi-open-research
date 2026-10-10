from packet_tools import write_packets
from build_renewed_14_17 import common
from build_next_13_16 import S02
assignment='''Your turn17 is read in full. The coordinator independently computed
P#mod32,Q#mod64, all7 boundary values, K16=48, and Newton certificates
for K4s=0mod4,K16s=16mod32,K(16s+64)=K(16s)mod64. Complete certificates
and lower lift are attached. These establish fixed polynomial identities
only, not the large actual convolution/off-pair arguments. A second
researcher will audit your infinite fourth-carry proof.

CONTINUATION main target: evaluate the actual norm N/16mod2 on SAME
r18mod32. This is the unresolved norm part of your fourth-lift assignment,
not an invitation to redo the fourth discrepancy. It decides whether
alpha=gamma=4 everywhere or whether further original subclasses have
common scalar zeros. Both columns are even; for normNmod32, Xmod8 already
suffices, since changing an even X by8 changes its square by a multiple32.
Thus raw A=2Xmod16 and the accepted Pmod16 lift may suffice even though
fourth mixed discrepancy needed raw32/64. Avoid unnecessary deeper
forcing just to evaluate this norm digit.

Coordinator proposal TO AUDIT: at prescribed paired coordinates the
low formula gives the same valuation pattern as E_t=choose(C,t)*
choose(2C+1+D-t,D-t). If v2E_t=1, each squared X contributes4mod32;
if v2E_t=2, each contributes16 and the two cancelmod32. Hence pair norm
could be 8 times the count of t with v2E_t=1 modulo32. This may also be
written2*sum E_t^2mod32, but audit the units and existing formula needed
for every valuation case before accepting it. Odd X has depth>=3 and
other even coordinates mostlydepth>=3, but the remaining j32mod64 can
have depth2 and contribute16 each. Compute those residual contributions
rather than deleting them by the earlier defect argument.

Derive evaluated finite-binomial/convolution expressions with high
C,D and actual finite boundaries retained. Obtain an explicit zero/
nonzero scalar or an original-domain subclass condition, including
whether every selected original exponent occurs in a claimed subclass.
Use Frobenius/Kummer/contiguous identities already in the archive and
primary Granville method; bounded archive/current target checks locate
no completed evaluation of N/16 on this class. If N/16 also vanishes,
identify its first genuine residual quantity and move on to the fifth
contracted discrepancy only after accounting for its required precision.
Keep the actual falling metric, final gcd and complete real error.
'''
if __name__=='__main__':
    write_packets(18,{'A5':('Evaluate the unresolved fourth binary norm digit',assignment,
    [S02+'main/PAIRED_DERANGEMENT_LINEAR_S_CONSTRUCTION.md',
    S02+'agent3_analysis/PROPORTIONAL_PRIMITIVE_CENTER_INTERFACE.md'],
    ['A5_turn14','A5_turn15','A5_turn16','A5_turn17','A2_turn18'],
    ['binary_fixed_lift_control.json','binary_fourth_lift_control.json'])},common)
