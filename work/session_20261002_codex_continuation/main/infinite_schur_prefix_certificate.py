"""Exact finite prefix that enters a proved infinite integer-jet invariant."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json
from integral_jet_schur_tree import add,sub,mul,div,scale,pt,rec,ONE,SESSION
source=SESSION/'main/JET_TREE_265_PREFIX_DIAGNOSTIC.json'
raw=json.loads(source.read_text());rows={tuple(v['prefix']):v for v in raw['nodes']}
jets=[1,0,0,-1,6,0,-49,-5];R=Q(53,20)
def read(v):return tuple(Q(x['numerator'],x['denominator']) for x in v)
prefix=[]
for k in range(8):
    row=rows[tuple(jets[:k])];child=next(v for v in row['children'] if v['jet']==jets[k]);assert child['status']=='SURVIVES'
    b=read(child['parameter']);assert -1<b[0]<=b[1]<1
    pd=read(child['signed_pseudodistance']);assert -1/R<pd[0]<=pd[1]<1/R
    prefix.append({'derivative_order':k+1,'integer_derivative':jets[k],'schur_parameter':rec(b),'endpoint_after_strip':rec(scale(pd,R)),'affine_slope':row['slope']})
b=read(prefix[-1]['schur_parameter']);T=read(prefix[-1]['endpoint_after_strip'])
F=div(scale(read(prefix[-1]['affine_slope']),R/Q(9)),sub(ONE,mul(b,b)))
assert max(abs(v) for v in T)<Q(1,4)
assert 0<F[0]<=F[1]<Q(1,40)
bound_b=Q(21,80);den=1-bound_b*Q(1,4)
new_T=R*Q(1,40)/(2*den);slope_ratio=R/(10*(1-bound_b**2))
assert new_T<Q(1,4) and slope_ratio<1
record={'status':'PASS_EXACT_PREFIX_FOR_INFINITE_INTEGRAL_JET_CONSTRUCTION','radius':{'numerator':R.numerator,'denominator':R.denominator},'integer_derivative_prefix':jets,'prefix_schur_steps':prefix,'next_order':9,'next_endpoint':rec(T),'next_affine_slope':rec(F),'inductive_invariant':{'endpoint_absolute_bound':'1/4','affine_slope_upper':'1/40','parameter_absolute_bound':'21/80','next_endpoint_absolute_bound':{'numerator':new_T.numerator,'denominator':new_T.denominator},'slope_contraction_upper':{'numerator':slope_ratio.numerator,'denominator':slope_ratio.denominator}},'source_certificate':source.name,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'scope':'Exact prefix and elementary invariant constants. Infinite holomorphic and polynomial existence require the accompanying normal-family/endpoint-basis proof.'}
(SESSION/'main/INFINITE_SCHUR_PREFIX_CERTIFICATE.json').write_text(json.dumps(record,indent=2)+'\n')
print(record['status'],'R=53/20','next endpoint',tuple(float(v) for v in T),'next slope',tuple(float(v) for v in F))
