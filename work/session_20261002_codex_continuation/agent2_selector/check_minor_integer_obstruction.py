import sys,json
sys.path.insert(0,"[private local path removed]")
import sympy as s
from pathlib import Path
m=s.symbols("m");out={}
def v2(a):
 a=abs(int(a));return None if a==0 else (a&-a).bit_length()-1
for N in [4,8]:
 data=json.loads(Path(__file__).with_name(f"weighted_observability_n{N}.json").read_text());num=s.cancel(s.sympify(data["tau"])).as_numer_denom()[0]
 P=s.Poly(num,m); _,P=P.primitive(); coeff=P.all_coeffs(); vv=[v2(c) for c in reversed(coeff)]
 mods={}
 for p in [2,3,5,7,11,13,17,19,23,29,31]:
  roots=[j for j in range(p) if int(P.eval(j))%p==0]
  mods[str(p)]=roots
 out[str(N)]={"degree":P.degree(),"v2_low_to_high":vv,"constant_v2":vv[0],"minimum_v2":min(v for v in vv if v is not None),"modular_roots":mods}
 print(N,out[str(N)],flush=True)
Path(__file__).with_name("weighted_observability_integer_obstruction.json").write_text(json.dumps(out,indent=2))
