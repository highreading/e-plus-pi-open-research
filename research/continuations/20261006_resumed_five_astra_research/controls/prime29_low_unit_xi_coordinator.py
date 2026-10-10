#!/usr/bin/env python3
"""NEW paid low-unit scalar, with complete classified support preserved."""
from pathlib import Path
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(45,45))
C=Path(__file__).resolve().parent
start=time.monotonic();p=29;mod=p*p;D=p**3
prefix=[1]
for x in range(1,mod):prefix.append(prefix[-1]*(x if x%p else 1)%mod)
assert prefix[-1]==mod-1
def F(N):
    assert N>=0
    return (-1 if (N//mod)%2 else 1)*prefix[N%mod]%mod
def P3(N):return F(N)*F(N//p)*F(N//mod)%mod
def quotient(a,bs):
    den=1
    for b in bs:den=den*b%mod
    assert den%p
    return a*pow(den,-1,mod)%mod
def vf(N):
    result=0
    while N:N//=p;result+=N
    return result

W=7663+19*D;B=16848+7*D;A=15327+38*D
low0=list(range(8))+list(range(15,29))
branches=[[],[]]
for j2 in range(21):
    for j0 in low0:
        r=j0+mod*j2
        vals=[]
        for q in (0,1):
            j=r+D*q
            L=quotient(P3(W),[P3(j),P3(W-j)])
            L=L*quotient(P3(A+B-j),[P3(A),P3(B-j)])%mod
            vals.append(L)
        delta=(vals[1]-vals[0])%mod
        assert delta%p==0
        branches[int(j2>=10)].append({'r':r,'j0':j0,'j2':j2,'L0':vals[0],
            'L1':vals[1],'unit_derivative':delta//p})
assert list(map(len,branches))==[220,242]
alpha=[sum(x['L0']**2 for x in group)%mod for group in branches]
beta=[2*sum(x['L0']*x['unit_derivative'] for x in group)%p for group in branches]

Cstar=20916;X=2001*Cstar+1382
paths=[]
for eps in (0,1):
    for d0 in range(20):
        k0=7+p*eps-d0
        if not 0<=k0<=19:continue
        for typ,second,third in [('I',range(9),3),('II',range(14-eps,26-eps),2)]:
            for d1 in second:
                k1=25-eps-d1
                assert 0<=k1<p
                q=d0+p*d1+mod*third
                assert 0<=q<=Cstar
                value=vf(X)-vf(q)-vf(X-q)+vf(2*X+Cstar-q)-vf(2*X)-vf(Cstar-q)
                assert value==1
                assert q//D==(Cstar-q)//D==0
                assert X//D==(X-q)//D
                assert (2*X+Cstar-q)//D==(2*X)//D
                low=quotient(P3(X),[P3(q),P3(X-q)])
                low=low*quotient(P3(2*X+Cstar-q),[P3(2*X),P3(Cstar-q)])%mod
                delta=(X+Cstar+1)*(3*X+Cstar+1-2*q)%mod
                paths.append({'type':typ,'cutoff_carry0':eps,'q':q,
                    'low_unit_mod841':low,'difference_multiplier_mod841':delta,
                    'valuation':value,'outgoing_interfaces':[0,0,0]})
assert len(paths)==231
num=sum(x['difference_multiplier_mod841']*x['low_unit_mod841']**2 for x in paths)%mod
assert num%p==0
gamma=num//p
assert (alpha[0]+alpha[1])%p==0
xi=(4*gamma+13*((alpha[0]+alpha[1])//p)+11*beta[0]+22*beta[1])%p
leading_ok=[a%p for a in alpha]==[4,25]
artifact={'status':'PASS' if leading_ok else 'SPECIFICATION_DISCREPANCY',
    'scope':'NEW complete p2 low-unit lift specified in A2turn12 Section18; source specification still independently audited',
    'p':p,'D':D,'physical_reference':[W,B,A],'normalized_tail_reference':[Cstar,X],
    'branch_counts':list(map(len,branches)),'valuation_one_path_count':len(paths),
    'alpha_mod841':alpha,'alpha_mod29':[x%p for x in alpha],
    'beta_mod29':beta,'gamma_mod29':gamma,'gamma_whole_numerator_mod841':num,
    'Xi_mod29':xi,'expected_leading_coefficients_passed':leading_ok,
    'unit_derivative_divisions_paid':True,'whole_gamma_division_paid':True,
    'low_branches':branches,'gamma_paths':paths,'old42_terms_or135918_sums_rerun':False,
    'complete_original_norm_evaluated':False,'irrationality_proved':False,
    'report_sha256':hashlib.sha256((C.parent/'responses/A2_turn12.md').read_bytes()).hexdigest(),
    'elapsed_seconds':round(time.monotonic()-start,3)}
out=C/'prime29_low_unit_xi_certificate.json'
out.write_text(json.dumps(artifact,indent=2)+'\n')
receipt={k:v for k,v in artifact.items() if k not in ('low_branches','gamma_paths')}
receipt['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
receipt['artifact_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
(C/'prime29_low_unit_xi_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
