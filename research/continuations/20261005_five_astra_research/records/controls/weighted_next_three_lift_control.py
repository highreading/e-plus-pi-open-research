"""One bounded modular n65 audit, independently authored from defining moments."""
import json,math,resource,time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
n=65;depth=32;mod=3**depth;size=n-2
started=time.monotonic()

def normalized_b(s):
    rising=1;total=0
    for ell in range(s+1):
        if ell:rising*=s+ell
        total+=math.comb(s,ell)*(-2)**(s-ell)*rising
    return total

bs=[normalized_b(s) for s in range(2*n+2)]
cs=[(2*bs[s]+(s+1)*bs[s+1])%mod for s in range(2*n+1)]
es=[(4*bs[s]+4*(s+1)*bs[s+1]+(s+1)*(s+2)*bs[s+2])%mod for s in range(2*n)]
assert all(es[3*r]%9==3 for r in range((2*n-1)//3+1))
assert all(bs[3*r]%9==(1+6*r*(r+1))%9 for r in range((2*n+1)//3+1))
assert all(bs[3*r+1]%9==0 for r in range(2*n//3+1))

def gram(d,e):return math.comb(d+e,d)*es[d+e]%mod
E=[[gram(d,e) for e in range(size)] for d in range(size)]
last=n-2;degree=n-1
# Solve simultaneously E X = [constant coupling,last cross,degree-n cross].
aug=[E[d]+[cs[d],gram(d,last),gram(d,degree)] for d in range(size)]
for j in range(size):
    pivot=next(i for i in range(j,size) if aug[i][j]%3)
    aug[j],aug[pivot]=aug[pivot],aug[j]
    inv=pow(aug[j][j],-1,mod)
    aug[j]=[x*inv%mod for x in aug[j]]
    for i in range(size):
        if i==j:continue
        f=aug[i][j]
        if f:aug[i]=[(x-f*y)%mod for x,y in zip(aug[i],aug[j])]
sol=[[aug[d][size+k] for d in range(size)] for k in range(3)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))%mod
U0=cs[:size];U1=[gram(d,last) for d in range(size)]
a=(-dot(U0,sol[0]))%mod
b=(cs[last]-dot(U0,sol[1]))%mod
c=(gram(last,last)-dot(U1,sol[1]))%mod
xi0=(cs[degree]-dot(U0,sol[2]))%mod
xi1=(gram(last,degree)-dot(U1,sol[2]))%mod
assert a%3
ia=pow(a,-1,mod)
delta=(c-b*b*ia)%mod
mixed=(xi1-b*ia*xi0)%mod
endpoint_numerator=(c*xi0-b*xi1)%mod
assert delta%9==3 and mixed%3==2

def valuation_record(x):
    if not x:return {'valuation_lower_bound':depth,'exact_valuation_resolved':False}
    v=0
    while x%3==0:x//=3;v+=1
    return {'valuation':v,'first_unit_mod3':x%3,'first_unit_mod9':x%9,
            'exact_valuation_resolved':True}
values={'a':a,'b':b,'c':c,'delta':delta,'xi_const':xi0,'xi_last':xi1,
        'mixed_last_numerator':mixed,'coupled_endpoint_numerator':endpoint_numerator}
record={'n':n,'prime':3,'modulus':str(mod),'precision':depth,'unit_block_size':size,
        'method':'defining factorial-normalized moments, unit Gaussian elimination with three RHS',
        'checks':{'delta_mod9_equals3':True,'mixed_mod3_equals2':True,
                  'first_branch_residues_checked_in_required_range':True},
        'values':{k:{'residue':str(v),**valuation_record(v)} for k,v in values.items()},
        'finite_only':True,'seconds':round(time.monotonic()-started,3)}
vnum=record['values']['coupled_endpoint_numerator']
Fn=sum((n-1)//(3**j) for j in range(1,10))
if vnum.get('exact_valuation_resolved'):
    record['native_primitive_endpoint_v3_if_uniform_leading_theorem_passes']=Fn+vnum['valuation']
else:record['native_primitive_endpoint_v3_lower_bound_if_theorem_passes']=Fn+depth
(OUT/'weighted_next_three_lift_control.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
