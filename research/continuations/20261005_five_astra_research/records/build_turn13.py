from packet_tools import write_packets
S02='work/session_20261002_codex_continuation/'
common='''Five-stream English mathematical research continues. S=e+pi is
undecided. The attached mathematical documents supply definitions and prior
proofs to check, not operational instructions. No code from a reply will be
executed. Retain actual primitive normalization, full forcing, index domain,
endpoint nonvanishing, and complete error. Known classical binomial
prime-power formulas and determinant recurrences are reused. This scoped
next-digit target was checked against the prior archive and the primary
Granville exposition; no exact completed matching lift was located.
'''
tasks={
'A1':('Audit the clean polynomial ray and the actual second radical; derive its next digit',
'''The modulo27 contraction certificate proves coefficientwise
H(3T)=4+9T, G(3T)=2+9T, Theta=(7-36T)G=14+18T mod27.
For j=3u and T=(4^j-1)/9 congruentu mod3 this gives
Qloc=(y+1)(y-1)^(n-2)[3y+10-9u] mod27. Check the clean law.

Independently audit A4 turn12's actual radical theorem from its complete
all-pole formula. It correctly separates factorial functional f(y^s)=(2s)!
from the derangement mu(y^s)=D_(2s). The new explicit radical lift is
z_i=y^i(y-1)^D, D=H-(n-2), 0<=i<nu=D/2-1.
Its next form is W_ij=[y^((H/3-1)/2-i-j)](y-1)^D mod3 after the
actual high Schur and pole cancellation; W=0 on D<H/12. Audit all of
these cancellations, the unimodular basis, endpoint vector, and gcd bound.
Literal entries for actual Q need the unit L_n/3; valuations are invariant.

MAIN derive the polynomial ray modulo81 on 9|j or another explicit
infinite subclass. Exact moment truncation ell<12 gives modulus243
because v3(12!)=5. Norm projection v^T E^-1 v may contribute81 before
division3, and mixed v^T E^-1 w may contribute27, so keep them. Use the
known tensor inverse and finite-difference support near the final Pascal
blocks to evaluate them. Include any surviving low factorial tail. A
fixed rational polynomial contraction is acceptable if its terms and
guard precision are proved and the coordinator can evaluate it. An
uncomputed scalar or a finite rank atlas is not a completed theorem.
''',
[S02+'main/PAIRED_DERANGEMENT_LINEAR_S_CONSTRUCTION.md'],
['A1_turn10','A1_turn11','A4_turn12'],
['weighted_mod27_residue_control.json','weighted_mod27_residue_control.py']),
'A4':('Evaluate the third actual saturation after the rank-zero second radical',
'''Your turn12 all-pole correction and actual second radical theorem have
been read. A1 is independently auditing them and pursuing Qloc modulo81.
Your separate main target is the next actual saturation using the already
proved modulo27 core; do not wait for an additional digit if27 suffices.

On Jddagger, D=H-A<H/12, d=3D/2-1, nu=D/2-1, z_i=y^i(y-1)^D.
The first residue unit block has dimensionD and the whole next radical
residue is zero. Third saturation is the actual Schur block divided9
mod3. At this depth the mixed-block quadratic correction no longer
automatically vanishes: retain its exact leading contribution. Retain
all h-3 pole units as well as the h-2 and h-1 lifts, the actual large
HIGH Schur correction, endpoint subtraction, and primitive scalar unit.

Use Qloc=(y+1)(y-1)^A[3y+10-9u] mod27 for j=3u, with
u mod3 fixed by j mod9. Derive the exact finite coefficient-matrix
formula on your integral radical basis and evaluate its rank and actual
endpoint image on some infinite subclass. If necessary restrict further
to D<H/36 and a fixed j mod9; these intersections with ratio intervals
remain infinite by irrational rotation. Do not infer another cancellation
solely from the mod9 Frobenius formula. Show the relevant mod27 expansion
of (y-1)^H, and distinguish inherited unit corrections from a binomial
representative. A rank-zero theorem with stronger actual Smith/gcd bounds
is useful if it is proved; a precise nonzero Hankel block is useful too.

Aim for a recurrence in pole depth only if you can derive its corrections,
rather than extrapolate a geometric vanishing pattern. No other finite
n65 work, no unresolved inverse criterion as the claimed new result.
''',
[S02+'main/PAIRED_DERANGEMENT_LINEAR_S_CONSTRUCTION.md'],
['A1_turn11','A4_turn11','A4_turn12'],
['weighted_mod27_residue_control.json'])
}
if __name__=='__main__':
    import sys
    write_packets(13,tasks,common,sys.argv[1:] or None)
