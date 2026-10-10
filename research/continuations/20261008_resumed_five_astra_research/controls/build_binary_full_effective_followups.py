from pathlib import Path
import hashlib,json,sys
H=Path(__file__).resolve().parent;R=H.parent
sys.path.insert(0,str(H));from packet_builder import build
for agent,turn,lines in [('A2',18,1924),('A4',27,1873)]:
    gate=json.loads((H/f'{agent}_TURN{turn}_FULL_READ_GATE.json').read_text())
    assert gate['full_report_read'] and gate['full_line_count']==lines
    assert gate['report_sha256']==hashlib.sha256((R/f'responses/{agent}_turn{turn}.md').read_bytes()).hexdigest()

receipt=json.loads((H/'THETA_FIRST_SCHUR_NEW_AUXILIARY_RECEIPT.json').read_text())
summary={k:v for k,v in receipt.items() if k!='cases'}
summary['cases']=[{k:v for k,v in c.items() if k not in ('I','unit_pivot_operations','transformed_matrix_mod4','complete_divided_Schur_mod2')} for c in receipt['cases']]
summary['full_receipt_sha256']=hashlib.sha256((H/'THETA_FIRST_SCHUR_NEW_AUXILIARY_RECEIPT.json').read_bytes()).hexdigest()
summary['coordinate_scope']='Only full first-effective ranks are checked; equality under the proposed coordinate identification is NOT certified.'
sp=H/'THETA_FIRST_SCHUR_NEW_AUXILIARY_SUMMARY.json'
assert not sp.exists();sp.write_text(json.dumps(summary,indent=2)+'\n')

gate2=r'''The parent reads FULL A4turn27 ALL1873 lines and FULL A2turn18
ALL1924 lines. FULL27 DIFFERENT-passes your FULL16 exact chi/unit block
and whole linear lower theorem, with the required inverse-trace low
coordinate clarification. Your FULL18 DIFFERENT-passes the parent
all-precision/GF/period candidates, with w-atom versus c-atom scope
made explicit. NEW FULL27 first effective map/explicit C/two-level
all-pattern lower bound have favorable parent proof review; DIFFERENT
audit is assigned to YOU here. Do not re-audit your own FULL16/17 or
FULL18. FULL17 Section8 H8 and NEW FULL18 literal residual/path/paired
border application go to A4turn28 for a DIFFERENT audit.
NEW parent d80 p8/9 first-Schur diagnostic checks FOUR complete source
matrices at base0 with both actual pole sets: ranks57/56 and divided
rank21 match FULL27. It is CLOSED and is not rerun; it does not certify
coordinate equality or an original-index upper. The NEW exact d48 p12
literal-source determinant is nonzero with valuation30, but that
auxiliary is OUTSIDE the rank-window rho<L hypotheses and supplies no
contradiction to them. It is also CLOSED. Current/Desktop scoped
second-wrap/beyond-half/lacunary/Kempner searches find OLD unrelated
ternary Selberg and shared-germ lacunarity work, not a completed exact
rank of FULL27's binomially weighted Frobenius window. Primary
arXiv1806.08729 describes Hankel determinants of the characteristic
sequence of powers2, and1511.06569 a period-doubling sequence; abstracts
were opened as filters. Neither automatically supplies our shifted,
binomially weighted rectangular C or higher paid full coefficients.
Classical polynomial/Padé/Artin-Schreier methods are REUSE; no unread
theorem is imported. This is scoped overlap checking, not global novelty.'''
task2=r'''FIRST perform a DIFFERENT proof audit of ALL NEW FULL A4turn27
Sections11-15: the integer mod4 theta lift, indispensable degree2L carry,
complete first effective map on the ENTIRE chi radical, pole/base/atom
and lift-carry payments, both p-parity kernel parametrizations/terminal
conditions, exact C rank formula and constructive rho+1 unit pivots,
the two-level/source-excess tradeoff for EVERY I,J,U. Validate all rank
window hypotheses and finite cutoff r=d; repair any unsupported step.
The prior FULL16 rank theorem is reuse, not a self-audit assignment.

PRIMARY NEW RESEARCH: evaluate the rank/kernel of the ACTUAL matrix
C_(L,rho,p) in FULL27(14.1), particularly the minimizing count strip
p=d/4+O(logd) on the SAME original near-half interval and L=2mod3.
Use the binomial weighting, BOTH p parities, dyadic L and actual rho.
In local T coordinates the coefficients are those of
Phi(T)*(1+T)^a, Phi=sum_(e=1,2,4,...)T^e, Phi^2+Phi=T, with the EXACT
finite window in14.1. A useful new theorem must give an evaluated rank,
unit block or quantified defect on an infinite ORIGINAL subfamily,
not merely rename C as a Toeplitz/Hankel determinant. Classical
continued fractions or Artin-Schreier identities may be used after
proving applicability to this exact shifted, weighted rectangular
window. Finite auxiliaries are diagnostics, not that theorem.

Then derive the actual next divided matrix on the resulting kernel if
the rank structure permits a new recursive block argument. Aim toward
a proved O(dlogd) accumulated EXCESS upper or a genuinely quantitative
paid recurrence, not an unbounded sequence of digit extensions. Every
raw precision, full source/pole pattern, newly visible factorial/bottom-
atom competitor and both I,J/tied product counts must be paid at the
claimed depth. A pure-source minimal determinant never alone proves
the whole coefficient upper. The actual paired constant border -f+4rho
and ALL-prime scalar/G/primitive WHOLE error remain separate literal
requirements. FULL18 quadratic source-precision analysis is a valid
limitation of the current rational representation, not a theorem that
new algebraic valuation arguments are impossible. Do not repeat it or
the closed mod16/mod4096/d80/d48 checks. Detailed English proofs with
proved/conditional/open scopes; no original-sized solve or old scan.'''
assert not (R/'prompts/A2_turn19.txt').exists()
build('A2',19,task2,[R/'responses/A4_turn27.md',R/'responses/A2_turn18.md',
 {'path':R/'responses/A2_turn17.md','lines':(1360,1686)},sp,
 H/'THETA_LITERAL_EXACT_AUXILIARY_ATTAINMENT_RECEIPT.json'],gate2)

gate4=r'''The parent reads FULL A2turn17 ALL1824, FULL18 ALL1924 and your
FULL27 ALL1873 lines. Your NEW FULL27 first effective map and rank(C)
claims go to A2turn19 for DIFFERENT audit, not to self-review here.
NEW FULL17 Section8 common-minor/Cramer/H8 and FULL18 exact residual
functional/path/both-border recurrence have favorable parent proof
review; their DIFFERENT audit is assigned to YOU. FULL18 differently
passes the root all-precision theta/source and period candidates,
with actual c-atom versus w-atom repair, so no duplicate GF audit.
The new parent four d80 first-Schur ranks match your predictions; this
CLOSED check supplies only auxiliary ranks. The exact d48 p12 full
literal determinant is nonzero/valuation30 outside the rank-window,
also CLOSED. Never rerun either or the old mod16/mod4096 profiles.
Current/Desktop searches recover classical Laguerre Gamma moments,
Pascal/compact Wick audits and the DIFFERENT-passed weighted dyadic
gateway supplied below. Its operator T=((1-t)^2+1)/2 and integral
quadratic Laguerre blocks are REUSE. Our contact variable is y=T-1,
so the affine ring shift is an exact available transformation; neither
the OLD weighted orthogonal polynomial/arctangent theorem nor its
subfamily conclusion automatically controls the ACTUAL corrected
one-shot residual pair. No completed application to that actual path
functional was located by scoped theta/Laguerre/divided-basis searches.
Primary DLMF Laguerre recurrence and ordinary derangement Hankel
literature are classical input only, not our filtered determinant or
binary upper. No exhaustive novelty or unread theorem is claimed.'''
task4=r'''FIRST DIFFERENT-audit ALL NEW FULL A2turn17 Section8. This
includes the uniform minor lower for EVERY row/return-only selection,
the q+1 LOWER-only step, actual inverse least simultaneous clearer and
invariant-factor separation, both complete border payments, integer
K_A/E_A/e_h divisions, exact odd-pivot ALL-prime transfer and extracted
5/2*d^2 scale. Do not assume independently attaining minors give a
nested flag. Prove or repair H8 in FULL18 at the ORIGINAL interval.

Also DIFFERENT-audit NEW FULL18 Sections12-19 and21: actual finite
functional, selected-edge factorial-paid path contraction with s
components, determinant sign/multiplier, BOTH complete backward
factorial/reciprocal border recurrences, actual forcing-return
annihilation, rational-row application/finite overflow and paid input
precision, and the weak full actual height cap. GF/period audit is
already DIFFERENT-passed and is not repeated. Preserve original
moments<=3d+1, odd Lambda and complete factorial bottom correction.

PRIMARY NEW RESEARCH: seek a structural binary valuation argument for
this ACTUAL residual pair using its fully specified physical row
functional, rather than just the quadratic-order finite GF recurrence.
One exact classical input to rederive/use is, for x=1-t and
y=(x^2-1)/2,
 theta_r^(m)=integral_0^infty e^-t*x^(2m)*y^r dt/r!.
It follows directly from the ordinary derangement integral and the
finite Delta^r identity. The supplied OLD weighted gateway gives a
2-integral orthogonal Laguerre block lattice in x^2=2(y+1)-1,
with equal block norm valuations2*v2(h!). Our y-shift changes the
moment polynomials, and the DIVIDED contacts y^r/r!, actual source
filters and corrected functional must have ALL factorial/odd payments
proved; do not assume their Laguerre coefficients are integral.

Determine whether this exact lattice, or another concrete structural
argument suggested by the path components Z_j, produces a paid
triangular block/invariant-factor control for the actual residual
common rectangle and BOTH terminal outputs. Aim for the joint target
v2 gcd(2J0,J1)<=5/4*d^2+O(dlogd) on infinitely many SAME original
indices, or a genuinely quantitative new partial pivot/excess theorem
that advances it. Real positivity or nonzero Gram determinants alone
do not give a binary valuation upper. The filtered subspace and
complete -f+4rho border may create isotropy/cancellation and must be
kept. If this lattice cannot supply a needed normalization, derive
the exact obstruction in the actual divided/source/one-shot objects;
do not merely cite the old weighted counterexample or rename a
determinant. A2turn19 separately studies rank(C) and its next pure-
source quotient, so avoid duplicating that task.

Retain all-prime odd-pivot scalar, actual contents/least simultaneous
clearer, ALL-prime G, primitive q and nonzero WHOLE same-index error.
No original-sized calculation, old scan, or implicit source transfer.
Give detailed English proofs and precise scopes; no proof is presumed.'''
assert not (R/'prompts/A4_turn28.txt').exists()
build('A4',28,task4,[R/'responses/A2_turn17.md',R/'responses/A2_turn18.md',
 {'path':R/'responses/A4_turn27.md','lines':(929,1634)},
 Path('work/session_20261002_codex_continuation/agent1_arithmetic/WEIGHTED_DETERMINANT_DYADIC_GATEWAY.md'),
 sp,H/'THETA_LITERAL_EXACT_AUXILIARY_ATTAINMENT_RECEIPT.json'],gate4)
