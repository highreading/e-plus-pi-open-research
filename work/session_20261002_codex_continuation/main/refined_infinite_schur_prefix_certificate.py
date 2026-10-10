"""Exact refined prefix at R=2.665; same proved invariant as the reviewed2.65 case."""
from fractions import Fraction as Q
import hashlib,json
from integral_jet_schur_tree import sub,mul,div,scale,rec,ONE,SESSION
source=SESSION/'main/JET_TREE_2665_PREFIX_DIAGNOSTIC.json'
raw=json.loads(source.read_text());rows={tuple(v['prefix']):v for v in raw['nodes']}
jets=[1,0,0,-1,6,0,-49,-6,919];R=Q(533,200)
def read(v):return tuple(Q(x['numerator'],x['denominator']) for x in v)
prefix=[]
for k,j in enumerate(jets):
    row=rows[tuple(jets[:k])];child=next(v for v in row['children'] if v['jet']==j);assert child['status']=='SURVIVES'
    b=read(child['parameter']);pd=read(child['signed_pseudodistance'])
    assert -1<b[0]<=b[1]<1 and -1/R<pd[0]<=pd[1]<1/R
    prefix.append({'derivative_order':k+1,'integer_derivative':j,'schur_parameter':rec(b),'endpoint_after_strip':rec(scale(pd,R)),'affine_slope':row['slope']})
b=read(prefix[-1]['schur_parameter']);T=read(prefix[-1]['endpoint_after_strip'])
F=div(scale(read(prefix[-1]['affine_slope']),R/Q(10)),sub(ONE,mul(b,b)))
assert max(abs(v) for v in T)<Q(1,4) and 0<F[0]<=F[1]<Q(1,40)
B=Q(21,80);den=1-B*Q(1,4);newT=R*Q(1,40)/(2*den);ratio=R/(11*(1-B*B))
assert newT<Q(1,4) and ratio<1
record={'status':'PASS_EXACT_REFINED_INFINITE_JET_PREFIX','radius':{'numerator':R.numerator,'denominator':R.denominator},'integer_derivative_prefix':jets,'prefix_steps':prefix,'next_order':10,'next_endpoint':rec(T),'next_affine_slope':rec(F),'invariant_endpoint_bound':'1/4','invariant_spacing_bound':'1/40','inductive_next_endpoint_bound':{'numerator':newT.numerator,'denominator':newT.denominator},'inductive_spacing_contraction':{'numerator':ratio.numerator,'denominator':ratio.denominator},'source_certificate':source.name,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'scope':'Author refinement of the same invariant/normal-family/polynomial argument. Independent narrow audit applies to the prior2.65 case, not to this new prefix.'}
(SESSION/'main/REFINED_INFINITE_SCHUR_PREFIX2665_CERTIFICATE.json').write_text(json.dumps(record,indent=2)+'\n')
print(record['status'],'R=533/200','next T',tuple(float(v) for v in T),'next F',tuple(float(v) for v in F))
