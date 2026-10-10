from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json

base=Path('work/session_20261001_astra')
source=base/'agent2/ACTUAL_PROJECTION_REMAINDER.md'
source_text=source.read_text(encoding='utf-8')
assert 'H_b=(3/4)^((b-1)(b-2)/2)' in source_text
assert 'B_W^sharp/B_V^sharp=(37/67)epsilon_n' in source_text
adjacent=F(11,20)+F(1,12)/F(9,20)
checks={
 'adjacent_bound': adjacent==F(397,540),
 'strict_improvement': adjacent<F(3,4),
 'product_ratio': adjacent/F(3,4)==F(397,405),
 'special_row_ratio': F(740,513)/F(1340,513)==F(37,67),
 'positive_log_argument': F(405,397)>1,
 'lower_scalar_prefactor': F(2)*F(37,67)==F(74,67),
}
assert all(checks.values())
record={
 'status':'PASS_EXACT_RATIONAL_CONSTANTS',
 'checks':checks,
 'adjacent_bound':str(adjacent),
 'high_row_product_ratio':str(F(397,405)),
 'revised_special_row_ratio':str(F(37,67)),
 'source_sha256':sha256(source.read_bytes()).hexdigest(),
 'scope':'Rational constants and the inspected source definitions only. No determinant, degree sample, asymptotic theorem, or independent researcher audit was computed.',
 'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
}
out=base/'GROWING_HIGH_ROW_SLACK_CHECKS.json'
out.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
assert json.loads(out.read_text(encoding='utf-8'))==record
print(json.dumps({'status':record['status'],'certificate':str(out)}))
