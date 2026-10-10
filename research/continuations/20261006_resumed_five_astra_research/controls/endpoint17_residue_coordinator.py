#!/usr/bin/env python3
"""NEW independent exact auxiliaryn17 proof-class residues, no original producer."""
from pathlib import Path
from math import comb,factorial
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(30,30))
C=Path(__file__).resolve().parent
start=time.monotonic()
n=17;m=n+1;N=n+2
E=[1]
for k in range(1,2*n+3):E.append(k*E[-1]+1)
def falling(x,k):
    value=1
    for i in range(k):value*=x-i
    return value
def ci(i):
    return sum((-1)**i*(factorial(i)//(factorial(i-2*r)*factorial(r)*(1<<r)))*falling(n,i-r)
               for r in range(i//2+1))
coeff=[ci(i) for i in range(n+3)]
def moment(j):return sum(comb(j,i)*coeff[i] for i in range(j+1))
def force(j):return sum(comb(j,i)*coeff[i]*E[n+j-i] for i in range(j+1))
C0,B,A,D,F=[moment(j) for j in range(n-2,n+3)]
us=[force(j) for j in range(n,n+3)]
U=[m*N*(us[0]-A),N*(us[1]-D),us[2]-F]
X0=-m*N*A*A+n*N*B*D+n*n*B*F-n*N*A*D-n*N*D*D+n*m*A*F
Y0=n*(-(n-1)*N*C0*D+m*N*A*B+m*N*A*A-n*(n-1)*C0*F-n*m*B*F+m*N*A*D)
Z0=n*N*(-n*m*B*B+(n-1)*m*A*C0+n*(n-1)*C0*D-n*m*A*B-m*m*A*A+n*m*B*D)
raw3=[N*N*D*D-m*N*A*F,m*(n*N*B*F-N*N*A*D),m*N*N*(m*A*A-n*B*D)]
assert all(x%2==0 for x in raw3)
half3=[x//2 for x in raw3]
assert [x%16 for x in [C0,B,A,D,F]]==[11,9,8,8,9]
assert [x%16 for x in us]==[11,8,8]
assert [x%16 for x in U]==[2,0,15]
assert [X0%16,Y0%16,Z0%16]==[9,14,10]
assert [x%16 for x in half3]==[8,11,8]
products=[sum(x*y for x,y in zip(row,U))%16 for row in ([X0,Y0,Z0],half3)]
assert products==[8,8]
receipt={'status':'PASS','scope':'NEW exact auxiliaryn17 moment/full-exponential-force residue corroboration of the n17mod32 theorem class, not a new original producer',
    'auxiliary_n':n,'original_n_family_member':False,'complete_force_formula_used':True,
    'moments_mod16':[11,9,8,8,9],'forces_mod16':[11,8,8],'exterior_corrected_U_mod16':[2,0,15],
    'normalized_endpoint0_row_mod16':[9,14,10],'endpoint3_raw_row_div2_mod16':[8,11,8],
    'projected_force_mod16':products,'old_denominator_extraction_repeated':False,
    'infinite_family_scope_independently_proved':False,'irrationality_proved':False,
    'report_sha256':hashlib.sha256((C.parent/'responses/A4_turn12.md').read_bytes()).hexdigest(),
    'elapsed_seconds':round(time.monotonic()-start,3),
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(C/'endpoint17_residue_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
