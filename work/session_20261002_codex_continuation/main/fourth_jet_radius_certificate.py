from integral_jet_schur_tree import run, SESSION
from fractions import Fraction as Q
import json
r=run(Q(27,10),4)
assert r["status"]=="PASS_EXACT_INTEGER_JET_OMISSION_REJECTION"
(SESSION/"main/FOURTH_JET_RADIUS_CERTIFICATE.json").write_text(json.dumps(r,indent=2)+"\n")
print(r["status"],r["test_radius"])
