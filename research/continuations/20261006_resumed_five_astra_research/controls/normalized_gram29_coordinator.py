#!/usr/bin/env python3
"""New leading-unit/carry evaluator of an auxiliary normalized Gram matrix."""
from math import comb
from pathlib import Path
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(180,180))
ROOT=Path(__file__).resolve().parent
p=29
fact=[1]
for i in range(1,p):fact.append(fact[-1]*i%p)
invfact=[pow(a,-1,p) for a in fact]

def digits(x,L):return [(x//p**i)%p for i in range(L)]

def layers(b,n,a1,v1,a2,v2,coefficient=None):
    assert b+min(v1,v2)>=0
    inputs=(b-1,n+2,b+v1,b+v2,2*n+a1-1,2*n+a2-1)
    L=1
    while p**L<=max(inputs):L+=1
    L+=2
    ds=[digits(x,L) for x in inputs]
    # cutoff, weight and two lower subtraction borrows; two upper carries;
    # three monotone valuations; first digit pending the low coefficient.
    dp={(0,0,0,0,0,0,0,0,0,-1):(1,1,1)}
    maxstates=1;edges=0
    for i in range(L):
        nxt={}
        J,N,K1,K2,A1,A2=(z[i] for z in ds)
        for (qj,qw,qk1,qk2,ca1,ca2,ew,e1,e2,d0),vec in dp.items():
            for d in range(p):
                qjp=int(J-d-qj<0)
                wraw=N-d-qw; qwp=int(wraw<0); rd=wraw%p
                kraw1=K1-d-qk1;kraw2=K2-d-qk2
                qk1p,qk2p=int(kraw1<0),int(kraw2<0)
                kd1,kd2=kraw1%p,kraw2%p
                raw1=A1+kd1+ca1;raw2=A2+kd2+ca2
                ca1p,ca2p=raw1//p,raw2//p
                ewp,e1p,e2p=ew+qwp,e1+ca1p,e2+ca2p
                if ewp+e1p>2 or ewp+e2p>2:continue
                unitW=fact[N]*invfact[d]*invfact[rd]%p
                unit1=fact[raw1%p]*invfact[A1]*invfact[kd1]%p
                unit2=fact[raw2%p]*invfact[A2]*invfact[kd2]%p
                unit=unitW*unitW*unit1*unit2*(-1 if (ca1p+ca2p)%2 else 1)%p
                weights=coefficient(d0,d) if i==1 and coefficient else (1,1,1)
                nd0=d if i==0 else -1
                state=(qjp,qwp,qk1p,qk2p,ca1p,ca2p,ewp,e1p,e2p,nd0)
                old=nxt.get(state,(0,0,0))
                value=tuple((old[k]+vec[k]*unit*weights[k])%p for k in range(3))
                if any(value):nxt[state]=value
                elif state in nxt:del nxt[state]
                edges+=1
        dp=nxt;maxstates=max(maxstates,len(dp))
    answer=[0,0,0];accepted=[]
    for st,value in dp.items():
        if any(st[:6]) or st[6]+st[7]!=2 or st[6]+st[8]!=2:continue
        accepted.append(list(st[6:9]))
        for k in range(3):answer[k]=(answer[k]+value[k])%p
    sign=-1 if (v1+v2)%2 else 1
    return [sign*a%p for a in answer],{'layers':L,'max_states':maxstates,'candidate_edges':edges,'accepted_valuation_layers':accepted}

def no_shallow_weighted_atom(b,n,a,v):
    inputs=(b-1,n+2,b+v,2*n+a-1)
    L=1
    while p**L<=max(inputs):L+=1
    L+=2;ds=[digits(x,L) for x in inputs]
    states={(0,0,0,0,0,0)}
    for i in range(L):
        J,N,K,A=(z[i] for z in ds);new=set()
        for qj,qw,qk,ca,ew,ea in states:
            for d in range(p):
                qjp=int(J-d-qj<0);qwp=int(N-d-qw<0);qkp=int(K-d-qk<0)
                cap=(A+(K-d-qk)%p+ca)//p
                if ew+qwp+ea+cap<=1:new.add((qjp,qwp,qkp,cap,ew+qwp,ea+cap))
        states=new
    accepted=[z for z in states if not any(z[:4])]
    assert not accepted
    return True

def valunit(x):
    v=0
    while x%p==0:x//=p;v+=1
    return v,x%p

def small_check():
    records=[]
    for b,n,a1,v1,a2,v2 in [(35,29*35,1,-1,30,-30),(49,29*49,1,0,1,-1),
                           (78,29*78,30,-29,30,-30),(95,29*95,1,0,30,-29),
                           (120,2001*120,2,-1,31,-30),(90,2001*90,30,-29,1,-1)]:
        for variant in range(4):
            x1,x2=a1+variant,a2+variant
            expected=0;nonzero=0
            for j in range(b):
                k1,k2=b+v1-j,b+v2-j
                if min(k1,k2)<0:continue
                w=comb(n+2,j);q1=comb(2*n+x1+k1-1,k1);q2=comb(2*n+x2+k2-1,k2)
                ew,uw=valunit(w);e1,u1=valunit(q1);e2,u2=valunit(q2)
                if ew+e1==2 and ew+e2==2:
                    expected=(expected+(-1)**(k1+k2)*uw*uw*u1*u2)%p;nonzero+=1
            actual,budget=layers(b,n,x1,v1,x2,v2)
            assert actual==[expected]*3
            records.append({'b':b,'n':n,'a1':x1,'v1':v1,'a2':x2,'v2':v2,'residue':expected,'retained_integer_terms':nonzero})
    return records

def coefficient_tables():
    uu=[1,1]
    for r in range(2,p):uu.append((uu[-1]-pow(2,-1,p)*uu[-2])%p)
    LL=[0]
    for r in range(1,p):LL.append((LL[-1]+uu[r-1]*pow(r,-1,p))%p)
    FF=[];GG=[]
    for d in range(p):
        falling=1;f=g=0
        for r in range(d+1):
            f=(f+(-1)**r*falling)%p;g=(g+(-1)**r*falling*LL[r])%p
            falling*=d-r
        FF.append(f);GG.append(g)
    assert all(FF[d]==(1-d*FF[d-1])%p for d in range(1,p))
    def atoms(d,e):
        prev=(d-1)%p;eprev=(e-int(d==0))%p
        return [(d*FF[prev]%p,d*(GG[prev]+eprev*FF[prev])%p),
                (-FF[d]%p,-(GG[d]+e*FF[d])%p),
                (0,-14*d*FF[prev]%p),(0,14*FF[d]%p)]
    return FF,GG,LL,atoms

def main():
    start=time.monotonic()
    checks=small_check()
    b=2195380879;n=2001*b
    params=[(1,0),(1,-1),(30,-29),(30,-30)]
    for a,v in params:no_shallow_weighted_atom(b,n,a,v)
    FF,GG,LL,atoms=coefficient_tables()
    total=[0,0,0];pairs=[]
    for i,(a1,v1) in enumerate(params):
        for j in range(i,4):
            a2,v2=params[j]
            def coefficient(d,e):
                rows=atoms(d,e);Ai,Di=rows[i];Aj,Dj=rows[j]
                if i==j:return Ai*Aj,Ai*Dj,Di*Dj
                return 2*Ai*Aj,Ai*Dj+Aj*Di,2*Di*Dj
            value,budget=layers(b,n,a1,v1,a2,v2,coefficient)
            total=[(a+c)%p for a,c in zip(total,value)]
            pairs.append({'atom_pair':[i,j],'Gram_contribution_AA_AD_DD':value,'budget':budget})
    AA,AD,DD=total
    det=(AA*DD-AD*AD)%p
    isotropic=[[1,d] for d in range(p) if (AA+2*AD*d+DD*d*d)%p==0]
    if DD==0:isotropic.append([0,1])
    artifact={'status':'PASS','scope':'new phase-compatible auxiliary normalized leading Gram; not an original power or norm-relative whole alignment',
              'b':str(b),'n':str(n),'original_power':False,'basis':'(A,D) with D=B-A',
              'cutoff':'0<=j<b; coordinate b is zero after stated normalization at this precision',
              'pointwise_depth2_proved_by_no_shallow_digit_path':True,'F':FF,'G':GG,'L':LL,
              'atom_parameters':params,'atom_pairs':pairs,'Gram_matrix':[[AA,AD],[AD,DD]],'determinant_mod29':det,
              'isotropic_projective_lines':isotropic,'small_exact_integer_checks':checks,
              'original_norm_evaluated':False,'whole_force_evaluated':False,'irrationality_proved':False}
    target=ROOT/'normalized_gram29_certificate.json';target.write_text(json.dumps(artifact,indent=2)+'\n')
    receipt={'status':'PASS','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
             'scope':artifact['scope'],'b':str(b),'n':str(n),'exact_small_checks':len(checks),'auxiliary_atom_pairs':len(pairs),
             'pointwise_depth2_path_check':True,'Gram_matrix':artifact['Gram_matrix'],'determinant_mod29':det,
             'isotropic_projective_lines':isotropic,'maximum_states':max(z['budget']['max_states'] for z in pairs),
             'total_candidate_edges':sum(z['budget']['candidate_edges'] for z in pairs),
             'elapsed_seconds':round(time.monotonic()-start,3),'original_norm_evaluated':False,'whole_force_evaluated':False}
    (ROOT/'normalized_gram29_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2),flush=True)

if __name__=='__main__':main()
