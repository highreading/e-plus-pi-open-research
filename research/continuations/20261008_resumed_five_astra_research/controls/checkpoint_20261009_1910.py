from pathlib import Path
import datetime, json

HERE = Path(__file__).resolve().parent
R = HERE.parent
metrics = json.loads((HERE / 'ACTIVE_COMPLETED_CALL_METRICS.json').read_text())
assert len(metrics['completed_reports']) == 91
for agent, tail in [('A2', 16), ('A3', 21), ('A4', 26)]:
    assert json.loads((HERE / f'{agent}_TURN{tail}_FULL_READ_GATE.json').read_text())['full_report_read']
stamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat()
text = '''## Ongoing checkpoint, 9 October19:10 —91 FULL completed reports

ALL91 completed public mathematical reports are fully read and have retained
review records. FULL A2turn16(1763 lines) DIFFERENT-passes FULL A4turn24 exact
every-I,J source-jet reduction and parent nominal convexity/all-pattern
locality/partition inventory. Its NEW exact full-theta parity corank is
chi=L-p-rho+1 for L=1mod3, and chi=p+rho+1 for L=2mod3, under its original
finite hypotheses. It constructs an actual-rank unit block and gives a
chi-dimensional effective Schur quotient and whole linear-excess LOWER
divisors on an infinite ORIGINAL interval. Favorable parent review;
DIFFERENT audit PENDING. No exact corank2 or joint upper is inferred.

FULL A3turn21(3265 lines; initial truncated endpoint range recovered)
DIFFERENT-passes FULL A1turn19 actual complementary eta_I=0 and FULL
A5turn18/19 complete actual affine/Hermite defects, integer remainders,
Gaussian divisions, third source/endpoints and critical-credit payments.
NEW Delta height uses 5^(2N)/gB^2 rather than 5^(4N)/gB^2; favorable
parent review, DIFFERENT audit PENDING. Contact noncollision/mass and
actual primitive whole-error decay remain OPEN. FULL A3turn22(session7779;
143360bytes/planning52176) now DIFFERENT-audits FULL A5turn20/21/22 actual
mixed height, finite Hermite obstruction and fourth arithmetic, without
duplicating A5turn23's actual separation question.

FULL A4turn26(1763 lines) DIFFERENT-passes parent complete theta mod4/mod8
physical/top/atom/arbitrary-pole laws, full source-jet aggregation and
whole four-zero consequence. It DIFFERENT-passes FULL A2turn15 ALL global
factorial/bottom-atom/p0/small-p payments. NEW evaluated second effective
rows retain full integer carries; the odd-base overflow is repaired by
the exact finite base0 Newton expansion. Its whole six-zero LOWER and
next tied residue have favorable parent review, DIFFERENT audit PENDING.
A4turn27(session42209;102611bytes/planning35404) now DIFFERENT-audits FULL
A2turn16 NEW exact corank/unit-block/linear-whole divisor and then computes
the actual FULL chi-dimensional quotient, rather than assuming two rows.

NEW parent first-wrap binary phase proof and near-half cofactor corollary
are now supplied FULL to DIFFERENT A2turn17(session70012;82664bytes/
planning27169), with both FULL prior wrap/root-jet interfaces and FULL
A2turn15. On a narrower infinite ORIGINAL even dyadic-phase interval,
the candidate reaches q=d/2-m-1 with exact residual margins >=3. It is a
cofactor candidate, not a full terminal/joint upper or G theorem.

A1turn23(session67043) targets actual remaining critical coordinates and
the repaired true kernel. A5turn23(session8029) targets actual fourth-depth
noncoincidence or a paid quantified weaker saturation/contact-mass theorem.
ALL FIVE actual external roles remain live, with fresh per-attempt guards.
No incomplete stream is promoted. Latest-three FULL A2turn16/A3turn21/
A4turn26 and admitted request hashes refresh successfully. Actual maximum
reported input235787<272000. Requests pro/max/high, no max_output_tokens.
Saved public independent o200k counts9511..29769 are distinguished from
provider usage accounting. No old closed calculation is rerun.

[Private account record omitted.]
Both available credentials are usable. Neither stopping condition holds.
Research stays ACTIVE; no closeout/final Desktop organization or mirror.
Actual ternary full kernel/force/mod9/physical7/source34, complete binary
paired upper/constant border, other-prime contents, actual simultaneous
clearer/ALL-prime G and same-index nonzero primitive error decay are OPEN.
There is no e+pi decision or producer retirement.

'''
for name in ('ACTIVE_RESEARCH_STATE.md', 'COORDINATOR_REVIEW.md'):
    p = R / name
    old = p.read_text()
    title, sep, rest = old.partition('\n\n')
    assert '9 October19:10' not in old
    p.write_text(title + sep + text + rest)
print(json.dumps({'time': stamp, 'completed_full_reports': 91, 'state': 'ACTIVE'}))
