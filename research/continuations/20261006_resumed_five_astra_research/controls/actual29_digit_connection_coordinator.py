#!/usr/bin/env python3
"""NEW integral carry connection, annihilating-word interface and original AP.
No original-length power, complete physical column or old sparse norm rerun.
"""
from pathlib import Path
from math import comb
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(120,120))
CROOT=Path(__file__).resolve().parent
start=time.monotonic()
p=29
H=[0]
for t in range(1,p):H.append((H[-1]+pow(t,-1,p))%p)
w=[comb(19,t)**2%p for t in range(20)]
h=[(H[9+t]-H[9])%p for t in range(20)]
tt=[(H[9+t]-H[t])%p for t in range(20)]
low={}
for delta in range(p):
    for eps in [0,1]:
        K=J=HH=T=0
        for d in range(20):
            e=delta+p*eps-d
            if 0<=e<=19:
                ww=w[d]*w[e]
                K+=ww;J+=d*d*ww;HH+=(e-d)*ww*h[e];T+=(e-d)*ww*tt[e]
        low[delta,eps]=[x%p for x in [K,J,HH,T]]

def matrix(ai,Bi,mi,weighted=False):
    result=[[0,0],[0,0]]
    for e in [0,1]:
        for f in [0,1]:
            for d in range(ai+1):
                k=mi+p*f-e-d
                if 0<=k<=p-1-Bi:
                    term=comb(ai,d)**2*comb(Bi+k,k)**2
                    result[e][f]=(result[e][f]+(d if weighted else 1)*term)%p
    return result

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2))%p for j in range(2)] for i in range(2)]
def moment_transport(a,B,m,eps,weighted):
    prod=[[1,0],[0,1]]
    first=True
    while first or max(a,B,m):
        M=matrix(a%p,B%p,m%p,weighted and first)
        prod=mm(prod,M)
        a//=p;B//=p;m//=p;first=False
    return prod[eps][0]

def direct_observables(C):
    X=2001*C+1382
    difference=S0=S2=0
    for q in range(C+1):
        V=comb(X,q)*comb(2*X+C-q,C-q)
        vr=V%841
        difference=(difference+((2*X+C+1-q)**2-(X-q)**2)*vr*vr)%841
        S0=(S0+vr*vr)%p
        S2=(S2+q*q*vr*vr)%p
    assert difference%p==0
    return difference//p,S0,S2

samples=[]
checks=0
for C in list(range(87))+[841,870,901]:
    delta,m=C%p,C//p
    a=69*C+47;B=2*a+1
    D0,S0,S2=direct_observables(C)
    predicted_D=predicted_S0=predicted_S2=0
    for eps in [0,1]:
        L=m-eps
        M0=moment_transport(a,B,m,eps,False)
        M1=moment_transport(a,B,m,eps,True)
        if L<0:
            assert M0==M1==0
        else:
            direct0=direct1=0
            for r in range(L+1):
                U=comb(a,r)*comb(B+L-r,L-r)
                direct0=(direct0+U*U)%p;direct1=(direct1+r*U*U)%p
            assert [M0,M1]==[direct0,direct1];checks+=2
        K,J,HH,T=low[delta,eps]
        predicted_S0+=K*M0;predicted_S2+=J*M0
        predicted_D+=(20+delta)*((3*a+2)*(K+2*HH)*M0+(K+2*T)*(L*M0-2*M1))
    assert [predicted_D%p,predicted_S0%p,predicted_S2%p]==[D0,S0,S2]
    kappa=(21*D0+16*S2+(25+18*C+19*C*C+24*C**3)*S0)%p
    if C<3:assert kappa==[26,9,10][C]
    samples.append({'C_aux':C,'D':D0,'S0':S0,'S2':S2,'kappa':kappa})

interface_checks=0
for incoming in range(69):
    for doubled in [0,1]:
        carry=incoming
        dbcarry=doubled
        ad=bd=[]
        a_digits=[];B_digits=[]
        for digit in [0,2,5]:
            value=69*digit+carry
            ai,carry=value%p,value//p
            bv=2*ai+dbcarry
            Bi,dbcarry=bv%p,bv//p
            a_digits.append(ai);B_digits.append(Bi)
        assert a_digits[-1]==1 and B_digits[-1]==3
        assert matrix(1,3,28)==[[0,0],[0,0]]
        interface_checks+=1

M=p**10;prefix=p**6;period=p**4;beta=410910916
B0=pow(3,249005515,M);G=pow(3,574312172,M)
assert B0%prefix==beta and G%prefix==1
C0=(B0-beta)//prefix%period;g=(G-1)//prefix%period
assert g%p
word=sum(d*p**i for i,d in enumerate([0,2,5,28]))
assert word==687155
ustar=(word-C0)*pow(beta*g,-1,period)%period
for multiple in [0,1,2,17]:
    u=ustar+period*multiple
    bres=pow(3,249005515+574312172*u,M)
    assert bres==(beta+prefix*word)%M
artifact={'status':'PASS','scope':'NEW unequal-precision29 carry connection/two-state moment verification,138 killing-word interfaces and numeric original annihilating progression',
    'low_connection_ordered_pairs':400,'auxiliary_C_samples':[s['C_aux'] for s in samples],
    'direct_whole_observable_comparisons':len(samples),'direct_high_moment_comparisons':checks,
    'small_auxiliary_values':samples[:3],'killing_word_LSF':[0,2,5,28],'incoming_interface_checks':interface_checks,
    'annihilating_digit_matrix':matrix(1,3,28),
    'original_progression':{'modulus':period,'u_star':ustar,'target_C_residue':word,'B0_mod29_10':B0,'G_mod29_10':G,'C0':C0,'g':g,'verified_progression_samples':4},
    'theorem_supported_conclusion':'kappa=0 modulo29 for every nonnegative original u congruent to u_star modulo707281, using A2turn9 killing-word proof',
    'density_one_proof_independently_reviewed':False,'complete_physical_mixed_alignment_evaluated':False,
    'original_length_power_constructed':False,'irrationality_proved':False,
    'report_sha256':hashlib.sha256((CROOT.parent/'responses/A2_turn9.md').read_bytes()).hexdigest(),'elapsed_seconds':round(time.monotonic()-start,3)}
out=CROOT/'actual29_digit_connection_certificate.json';out.write_text(json.dumps(artifact,indent=2)+'\n')
receipt=dict(artifact);receipt['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();receipt['artifact_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
(CROOT/'actual29_digit_connection_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
