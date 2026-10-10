#!/usr/bin/env python3
"""NEW reference-filtered product certificate from retained original3375 data."""
from fractions import Fraction
from math import factorial,gcd,lcm
from pathlib import Path
import hashlib
import json
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU,(90,90))
sys.set_int_max_str_digits(500000)
C=Path(__file__).resolve().parent
started=time.monotonic()
source=C/'complete_endpoint_3375_certificate.json'
data=json.loads(source.read_text())
product_path=C/'endpoint3375_product_scalar_certificate.json'
prod=json.loads(product_path.read_text())
assert prod['input_sha256']==hashlib.sha256(source.read_bytes()).hexdigest()
n=int(data['n']);assert n==3375
m,N=n+1,n+2
def rat(x):return Fraction(int(x['numerator']),int(x['denominator'])) if isinstance(x,dict) else Fraction(int(x))
def integer(x):
    x=Fraction(x);assert x.denominator==1
    return x.numerator
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return [a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1)%3] for i in range(3)]
mom={k:integer(factorial(k)*rat(data['moment_states'][str(k)]['moment'])) for k in range(n-2,n+3)}
J=[[m*N*mom[n],n*m*N*mom[n-1],n*(n-1)*m*N*mom[n-2]],
   [N*mom[n+1],m*N*mom[n],n*m*N*mom[n-1]],
   [mom[n+2],N*mom[n+1],m*N*mom[n]]]
cols=[[J[i][j] for i in range(3)] for j in range(3)]
adj=[cross(cols[1],cols[2]),cross(cols[2],cols[0]),cross(cols[0],cols[1])]
raw=[[sum(seed[k]*adj[k][i] for k in range(3)) for i in range(3)] for seed in ([-1,n,-n*m],[0,0,1])]
rows=[[z//gcd(*map(abs,row)) for z in row] for row in raw]
v,w=[2*N,N,m],[0,N,2*n+3]
L=1<<(m//2)
hhat,ellhat=[integer(L*rat(data[key])) for key in ('tau_n','tau_n1')]
reference=[dot(row,v)*hhat+dot(row,w)*ellhat for row in rows]
assert all(reference)
D,Sigma,W=[int(prod[key]) for key in ('D_large','Sigma_large','product_certificate_W')]
joint=json.loads((C/'endpoint3375_joint_saturation_receipt.json').read_text())
assert joint['actual_boundary_gcd_large']=='1'
B=1 # Reused accepted content, never recomputed here.
Href=gcd(Sigma,*map(abs,reference))
exc=D//gcd(D,Sigma)
defect=Sigma//Href
stripped=exc
strip_steps=0
while True:
    divisor=gcd(stripped,defect)
    if divisor==1:break
    stripped//=divisor;strip_steps+=1
    assert strip_steps<200000
assert exc%stripped==0 and gcd(stripped,defect)==1
T=[abs(x)//gcd(abs(x),Sigma) for x in reference]
Vj=[gcd(stripped,x) for x in T]
V=lcm(*Vj)
Wref=gcd(W,Href**2*V)
assert W%Wref==0
artifact={'status':'PASS','scope':'NEW actual-reference filtered product fields at retained original3375; old producer and endpoint denominator/gcd not recomputed',
    'n':n,'hatted_references':[str(x) for x in reference],
    'H_ref':str(Href),'exclusive_divisor_before_filter':str(exc),
    'exclusive_divisor_after_defect_filter':str(stripped),
    'T_ref':[str(x) for x in T],'V_endpoint_filters':[str(x) for x in Vj],
    'V_lcm':str(V),'W_ref':str(Wref),
    'hatted_reference_bits':[abs(x).bit_length() for x in reference],
    'H_ref_bits':Href.bit_length(),'exclusive_divisor_before_bits':exc.bit_length(),
    'exclusive_divisor_after_bits':stripped.bit_length(),
    'endpoint_filter_bits':[x.bit_length() for x in Vj],
    'V_lcm_bits':V.bit_length(),'W_ref_bits':Wref.bit_length(),
    'W_ref_exactly_one':Wref==1,'defect_stripping_steps':strip_steps,
    'complete_endpoint_gcds_not_recomputed':True,'producer_regenerated':False,
    'whole_error_or_denominator_not_recomputed':True,
    'infinite_reference_filtered_bound_proved':False,'irrationality_proved':False,
    'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'product_input_sha256':hashlib.sha256(product_path.read_bytes()).hexdigest(),
    'elapsed_seconds':round(time.monotonic()-started,3)}
out=C/'endpoint3375_reference_filter_certificate.json'
out.write_text(json.dumps(artifact,indent=2)+'\n')
big=('hatted_references','H_ref','exclusive_divisor_before_filter','exclusive_divisor_after_defect_filter','T_ref','V_endpoint_filters','V_lcm','W_ref')
receipt={k:v for k,v in artifact.items() if k not in big}
receipt['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
receipt['artifact_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
(C/'endpoint3375_reference_filter_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
