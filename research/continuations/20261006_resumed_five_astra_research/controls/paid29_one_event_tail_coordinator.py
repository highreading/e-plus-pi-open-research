#!/usr/bin/env python3
"""NEW paid one-event finite sums and originalu2 normalized-tail annihilation.
No earlier auxiliary support sums, producer or zero-prefix control is rerun.
"""
from pathlib import Path
from math import comb
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(90,90))
C=Path(__file__).resolve().parent
start=time.monotonic()
p=29
fac=[1]
for k in range(1,p):fac.append(fac[-1]*k%p)
def ratio(num,den):return num*pow(den%p,-1,p)%p

one_event=[]
R=[]
for eps in range(2):
    aa=[(comb(8,d)*ratio(fac[13-eps-d],fac[17]*fac[25-eps-d]))**2%p for d in range(9)]
    bb=[ratio(fac[8]*fac[17+k],fac[25-eps-k]*fac[12+eps+k]*fac[17]*fac[k])**2%p for k in range(12)]
    assert (sum(aa)%p,sum(bb)%p)==((3,26) if eps==0 else (23,6))
    one_event.append({'cutoff_branch':eps,'typeA_units':aa,'typeB_units':bb})
    R.append((20*sum(aa)+9*sum(bb))%p)
assert R==[4,21]
low=[]
for eps in range(2):
    sums=[0,0,0]
    for d in range(20):
        k=7+29*eps-d
        if 0<=k<=19:
            w=comb(19,d)**2*comb(19,k)**2%p
            for h in range(3):sums[h]=(sums[h]+w*pow(d,h,p))%p
    low.append(sums)
assert low==[[10,6,11],[13,2,25]]
E=[sum(R[e]*low[e][h] for e in range(2))%p for h in range(3)]
assert E==[23,8,18]

def factorial_parts(n):
    valuation,unit=0,1
    while n:
        q,r=divmod(n,p)
        valuation+=q
        unit=unit*fac[r]*(-1 if q%2 else 1)%p
        n=q
    return valuation,unit
def binomial_parts(n,k):
    vn,un=factorial_parts(n)
    vk,uk=factorial_parts(k)
    vl,ul=factorial_parts(n-k)
    return vn-vk-vl,ratio(un,uk*ul)

aux=[]
atoms=0
for t in range(3):
    cc=20916+p**3*t
    xx=2001*cc+1382
    moments=[0,0,0]
    count_one=0
    for q in range(cc+1):
        v1,u1=binomial_parts(xx,q)
        v2,u2=binomial_parts(2*xx+cc-q,cc-q)
        assert v1+v2>=1
        atoms+=1
        if v1+v2==1:
            count_one+=1
            w=(u1*u2)**2%p
            for h in range(3):moments[h]=(moments[h]+w*pow(q,h,p))%p
    a=1716+2001*t
    tail=sum(comb(a,r)**2*comb(2*a+t-r,t-r)**2 for r in range(t+1))%p
    assert moments==[x*tail%p for x in E]
    # Exact finite whole divided difference throughp2: squared units are paid
    # byp2, and only the whole modp3 numerator is then divided byp.
    raw_numerator=(xx+cc+1)*((3*xx+cc+1)*moments[0]-2*moments[1])%p
    assert raw_numerator==0
    aux.append({'t':t,'C_aux':cc,'valuation_one_atoms':count_one,
                'T0_T1_T2_div_p2_modp':moments,'ordinary_tail_modp':tail,
                'whole_divided_difference_modp2':0})

# New normalized tail is AFTER the paid three-digit block, at actualoriginalu2.
beta=410910916
exponent=1397629859
residue=pow(3,exponent,p**41)
assert (residue-beta)%p**6==0
cpart=(residue-beta)//p**6
assert (cpart-20916)%p**3==0
tpart=(cpart-20916)//p**3
A,B,M=1716+2001*tpart,2*(1716+2001*tpart),tpart
row=[1,0]
trace=[]
for i in range(32):
    ai,bi,mi=A%p,B%p,M%p
    K=[[0,0],[0,0]]
    for e in range(2):
        for f in range(2):
            for d in range(ai+1):
                k=mi+p*f-e-d
                if 0<=k<=p-1-bi:
                    K[e][f]=(K[e][f]+comb(ai,d)**2*comb(bi+k,k)**2)%p
    row=[sum(row[e]*K[e][f] for e in range(2))%p for f in range(2)]
    trace.append({'digit_index':i,'actual_A_B_M_digits':[ai,bi,mi],'matrix':K,'row':row})
    if row==[0,0]:break
    A//=p;B//=p;M//=p
annihilated=row==[0,0]
artifact={'status':'PASS','scope':'NEW42 paid one-event contributions, complete three-digit phase auxiliary high sums and ACTUALoriginalu2 normalized-tail prefix',
    'one_event_unit_terms':one_event,'low_moment_coefficients':low,
    'paid_interface_coefficients':R,'three_moment_coefficients':E,
    'complete_auxiliary_atoms':atoms,'new_auxiliary_sums':aux,
    'original_u':2,'original_power_exponent':exponent,
    'bounded_power_modulus_exponent':41,'bounded_original_residue':str(residue),
    'C_prefix':str(cpart),'normalized_tail_prefix':str(tpart),
    'tail_trace':trace,'normalized_tail_annihilated_for_every_high_continuation':annihilated,
    'prefix_digits_used':len(trace),'terminal_carry_zero_retained':True,
    'original_T0_T1_T2_modp3_if_paid_connection_accepted':[0,0,0] if annihilated else None,
    'complete_physical_norm_next_digit_evaluated':False,
    'primitive_column_content_evaluated':False,'all_prime_q_evaluated':False,
    'irrationality_proved':False,
    'report_sha256':hashlib.sha256((C.parent/'responses/A2_turn10.md').read_bytes()).hexdigest(),
    'elapsed_seconds':round(time.monotonic()-start,3)}
out=C/'paid29_one_event_tail_certificate.json'
out.write_text(json.dumps(artifact,indent=2)+'\n')
receipt={k:v for k,v in artifact.items() if k not in ('one_event_unit_terms','tail_trace','bounded_original_residue','C_prefix','normalized_tail_prefix')}
receipt['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
receipt['artifact_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
(C/'paid29_one_event_tail_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
