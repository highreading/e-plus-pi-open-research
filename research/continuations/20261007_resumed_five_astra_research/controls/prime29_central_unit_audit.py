from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parent
table=[];a=[1]
for m in range(29):
    table.append(a[m]%29)
    nxt=[0]*(len(a)+2)
    for i,v in enumerate(a):nxt[i]+=v;nxt[i+1]+=2*v;nxt[i+2]+=2*v
    a=nxt
expected=[1,2,8,3,20,12,14,2,13,24,22,21,21,20,6,7,17,19,6,16,4,2,2,18,25,14,15,14,1]
assert table==expected and all(table)
c=[1,20387]
for s in range(1,29):c.append((s+20387)*c[-1]-(s*20387+s*(s-1)//2)*c[-2])
record=json.loads((root/'prime29_low_observation_certificate.json').read_text())
assert [v%841 for v in c]==record['symbols']['c_mod841']
out={'scope':'Bounded exact verification of all one-digit central coefficients and the short inverse-symbol recurrence; universal Lucas proof is symbolic, not numerical extrapolation.',
     'central_digit_table_mod29':table,'all_digits_nonzero':True,'inverse_symbol_matches':True,
     'C7':table[7],'C24':table[24],'C7_C24_mod29':table[7]*table[24]%29,
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'prime29_central_unit_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
