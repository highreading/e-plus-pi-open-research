"""Coordinator-authored exact Wilson one-carry arithmetic and full-tail checks.

This code consumes no model-generated code and accepts no operational input.
The initialization is finite; full recurrence checks are on auxiliary integers,
not on the huge original exponential family.
"""
from math import comb,factorial
from pathlib import Path
import hashlib,json,time

OUT=Path(__file__).resolve().parent
P=29;MOD=P*P
FAC=[factorial(i)%MOD for i in range(P)]
INV=[pow(x,-1,MOD) for x in FAC]
HARM=[0]
for i in range(1,P):HARM.append((HARM[-1]+pow(i,-1,P))%P)
WILSON=FAC[-1]

def step(states,a,eta,c):
    nxt={}
    for (sigma,beta,gamma,depth),(weight,zvec) in states.items():
        for k in range(P):
            ell=(eta-k-sigma)%P
            sig=(k+ell+sigma-eta)//P
            r=a-k-beta;bet=int(r<0);r%=P
            s=c+ell+gamma;gam=int(s>=P);s%=P
            newdepth=depth+bet+gam
            if newdepth>1:continue
            tup=(a,s,k,r,c,ell)
            unit=FAC[a]*FAC[s]%MOD
            for v in (k,r,c,ell):unit=unit*INV[v]%MOD
            g=unit*unit%MOD*pow(WILSON,2*(bet+gam),MOD)%MOD
            dot=sum(x*y for x,y in zip(tup,zvec))%P
            w=g*(weight+2*P*dot)%MOD
            hz=(HARM[a],HARM[s],-HARM[k],-HARM[r],-HARM[c],-HARM[ell])
            zv=[g%P*(weight%P)*x%P for x in hz]
            key=(sig,bet,gam,newdepth)
            old=nxt.setdefault(key,[0,[0]*6])
            old[0]=(old[0]+w)%MOD
            old[1]=[(x+y)%P for x,y in zip(old[1],zv)]
    return nxt

def initializer():
    data=[]
    for z in range(P):
        states=step({(0,0,0,0):[1,[0]*6]},9,20,18)
        states=step(states,19,z,9)
        assert all(beta==gamma==0 and depth==1 for sigma,beta,gamma,depth in states)
        for sigma in (0,1):
            w,zv=states.get((sigma,0,0,1),[0,[0]*6])
            assert w%P==0,(z,sigma,w)
            data.append({'G_low_digit':z,'sum_carry':sigma,'W_mod841':w,
                         'W_divisible_by29':True,'r_mod29':w//P,'Z_mod29':zv})
    return data

def full_recurrence(H):
    A=2001*H+67;C=2*A
    digits=[]
    while H or A or C:
        digits.append((A%P,H%P,C%P));H//=P;A//=P;C//=P
    digits.extend([(0,0,0)]*4)
    states={(0,0,0,0):[1,[0]*6]}
    for a,eta,c in digits:states=step(states,a,eta,c)
    return states.get((0,0,0,1),[0,[0]*6])[0]

def direct(H):
    A=2001*H+67;S=0;V=0;max_depth=0;units=0
    for k in range(H+1):
        X=comb(A,k)*comb(2*A+H-k,H-k)
        assert X%P==0,(H,k)
        quotient=X//P%MOD
        sq=quotient*quotient%MOD
        S=(S+sq)%MOD;V=(V+k*sq)%P
        if quotient%P:units+=1
    return S,V,units

def main():
    start=time.monotonic();init=initializer()
    (OUT/'onecarry29_initialization_406.json').write_text(json.dumps(init,indent=2)+'\n')
    checks=[]
    for G in list(range(29))+[29,30,57,100]:
        H=20+P*G
        exact,weighted,units=direct(H);rec=full_recurrence(H)
        assert exact==rec,(H,exact,rec)
        assert exact%P==weighted==0,(H,exact,weighted)
        checks.append({'G_auxiliary':G,'H_auxiliary':H,'A':2001*H+67,
                       'S_mod841':exact,'T_div29cubed_mod29':exact//P,
                       'weighted_S_mod29':weighted,'onecarry_unit_term_count':units,
                       'full_tail_recurrence_matches_direct':True})
        if G%7==0:print(json.dumps({'G_auxiliary':G,'matched':True,'seconds':round(time.monotonic()-start,2)}),flush=True)
    out={'status':'ONECARRY29_INITIALIZATION_AND_FULL_AUXILIARY_CHECKS_PASS',
         'modulus':MOD,'Wilson28_factorial_mod841':WILSON,
         'initialization_field_elements':406,'all58_W_divisible_by29':True,
         'r_nonzero_count':sum(v['r_mod29']!=0 for v in init),
         'Z_nonzero_entry_count':sum(z!=0 for v in init for z in v['Z_mod29']),
         'initialization_sha256':hashlib.sha256((OUT/'onecarry29_initialization_406.json').read_bytes()).hexdigest(),
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'complete_auxiliary_checks':checks,'seconds':round(time.monotonic()-start,2),
         'scope':'Finite preferred-cylinder initializer and full recurrence on 33 bounded auxiliary H. Neither a higher-tail unit theorem on original exponential indices nor any full-gcd estimate follows.'}
    (OUT/'onecarry29_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out),flush=True)

if __name__=='__main__':main()
