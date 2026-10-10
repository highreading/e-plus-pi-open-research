"""Parent-authored finite arithmetic check of A1turn15 Section7.

No credentials, network, downloaded code or original source vector.
Independent direct products verify the new bounded-register formula.
"""
from pathlib import Path
import hashlib
import json
import math

HERE=Path(__file__).resolve().parent
OUT=HERE/'factorial_unit_729_value_certificate.json'
TABLE=HERE/'factorial_unit_729_value_table.json'
if OUT.exists() or TABLE.exists():
    raise SystemExit('Refusing to repeat an existing arithmetic receipt')
M=3**28
B=729
C=[1]*B
H=[[0]*B for _ in range(4)]
for r in range(1,B):
    C[r]=C[r-1]
    for a in range(4):
        H[a][r]=H[a][r-1]
    if r%3:
        inv=pow(r,-1,M)
        C[r]=C[r]*r%M
        for a in range(4):
            H[a][r]=(H[a][r]+pow(inv,a+1,M))%M
assert C[-1]%B==B-1
rho=(-C[-1])%M
assert (rho-1)%B==0

def sums(q):
    return [q*(q-1)//2,
            q*(q-1)*(2*q-1)//6,
            (q*(q-1)//2)**2,
            q*(q-1)*(2*q-1)*(3*q*q-3*q-1)//30]

def block_formula(n):
    q,r=divmod(n,B)
    ss=sums(q)
    ll=0
    for a in range(1,5):
        if a==3:
            coefficient=B**3//3
        else:
            coefficient=B**a*pow(a,-1,M)%M
        coefficient*=1 if a%2 else -1
        ll=(ll+coefficient*(H[a-1][-1]*ss[a-1]+q**a*H[a-1][r]))%M
    assert ll%B==0
    ex=(1+ll+ll**2*pow(2,-1,M)
        +(ll**3//3)*pow(2,-1,M)
        +(ll**4//3)*pow(8,-1,M))%M
    cq=sum(math.comb(q,j)*(rho-1)**j for j in range(5) if j<=q)%M
    if q%2:
        cq=(-cq)%M
    return cq*C[r]*ex%M

def unit_formula(n):
    z=1
    while n:
        z=z*block_formula(n)%M
        n//=3
    return z

extra_q=[3,4,5,8,9,10,26,27,28,80,81]
extra_n=sorted({q*B+r for q in extra_q for r in [0,1,2,12,B-1]})
max_n=max(extra_n)
direct_f=1
direct_u=1
mismatches=[]
base_count=0
extra_count=0
for n in range(max_n+1):
    if n:
        if n%3:
            direct_f=direct_f*n%M
        stripped=n
        while stripped%3==0:
            stripped//=3
        direct_u=direct_u*stripped%M
    if n<=1470 or n in extra_n:
        actual_f=block_formula(n)
        actual_u=unit_formula(n)
        if actual_f!=direct_f or actual_u!=direct_u:
            mismatches.append({'n':n,'F3_formula':actual_f,'F3_direct':direct_f,
                               'U_formula':actual_u,'U_direct':direct_u})
        if n<=1470:
            base_count+=1
        else:
            extra_count+=1

table={'modulus':M,'block_length':B,'C_R':C,'H_a_R':H,
       'scope':'Universal factorial-unit helper only; not an original source/endpoint table.'}
table_bytes=(json.dumps(table,indent=2)+'\n').encode()
TABLE.write_bytes(table_bytes)
source=HERE.parent/'responses/A1_turn15.md'
record={'status':'PASS' if not mismatches else 'FAIL',
        'source':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'proof_scope':'Finite checks of Section7 only; the infinite identities and HIGH cancellation require proof audits.',
        'modulus':M,'block_length':B,'stored_residues':5*B,
        'table_sha256':hashlib.sha256(table_bytes).hexdigest(),
        'C728_mod729':C[-1]%B,'base_n_range':[0,1470],
        'base_comparisons':base_count,'extra_Q':extra_q,'extra_n':extra_n,
        'extra_comparisons':extra_count,'largest_direct_product_endpoint':max_n,
        'mismatches':mismatches,'original_source_or_inverse_computed':False,
        'original_factorial_array_computed':False,'network_or_credentials_used':False}
OUT.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:record[k] for k in ['status','stored_residues','base_comparisons',
                                     'extra_comparisons','largest_direct_product_endpoint','mismatches']}),flush=True)
if mismatches:
    raise SystemExit(1)
