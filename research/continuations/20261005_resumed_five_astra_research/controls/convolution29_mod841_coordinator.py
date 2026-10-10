"""Independent coordinator implementation of the carry-free squared convolution.

No remote code is executed. The derivation uses factorial units at precision29^2.
All finite comparisons use exact integer divisions of the complete convolution.
"""
from math import comb
from pathlib import Path
import json

P=29;MOD=P*P;OUT=Path(__file__).resolve().parent
HARM=[0]
for i in range(1,P):HARM.append((HARM[-1]+pow(i,-1,P))%P)

def recurrence(H,d):
    digits=[];z=H
    while z:digits.append(z%P);z//=P
    if not digits:digits=[0]
    digits.extend([0]*4)
    kappa=69*d+67;eps=0
    # Each given input digit fixes multiplier/doubling carry; only sum carry branches.
    states={0:(1,[0]*4,0)}
    max_states=1
    for position,eta in enumerate(digits):
        a=(2001*eta+kappa)%P;kappa=(2001*eta+kappa)//P
        c=(2*a+eps)%P;eps=(2*a+eps)//P
        nxt={}
        for sigma,(W,Z,V) in states.items():
            for k in range(a+1):
                ell=(eta-k-sigma)%P
                sigma_next=(k+ell+sigma-eta)//P
                assert sigma_next in (0,1)
                if ell>P-1-c:continue
                weight=(comb(a,k)*comb(c+ell,ell))**2%MOD
                correction=a*Z[0]+k*Z[1]+c*Z[2]+ell*Z[3]
                ww=weight*(W+2*P*correction)%MOD
                vec=[(HARM[a]-HARM[a-k])%P,(HARM[a-k]-HARM[k])%P,
                     (HARM[c+ell]-HARM[c])%P,(HARM[c+ell]-HARM[ell])%P]
                zz=[weight%P*(W%P)*v%P for v in vec]
                vv=weight%P*((W%P)*k if position==0 else V)%P
                if sigma_next not in nxt:nxt[sigma_next]=(0,[0]*4,0)
                ow,oz,ov=nxt[sigma_next]
                nxt[sigma_next]=((ow+ww)%MOD,[(u+v)%P for u,v in zip(oz,zz)],(ov+vv)%P)
        states=nxt;max_states=max(max_states,len(states))
    assert kappa==0 and eps==0
    W,Z,V=states.get(0,(0,[0]*4,0))
    return W,V,max_states

def direct(H,d):
    A=2001*H+69*d+67
    x=comb(2*A+H,H);T=0;U=0
    for k in range(H+1):
        T=(T+x*x)%MOD;U=(U+k*x*x)%P
        if k<H:
            numerator=x*(A-k)*(H-k);denominator=(k+1)*(2*A+H-k)
            assert numerator%denominator==0
            x=numerator//denominator
    return T,U

def main():
    total=0;maxs=0;examples=[]
    for H in range(151):
        for d in range(25):
            W,U,ns=recurrence(H,d);expected=direct(H,d)
            assert (W,U)==expected,(H,d,W,U,expected)
            total+=1;maxs=max(maxs,ns)
    for H in (299,840,841,842,900):
        for d in (0,3,11,24):
            W,U,ns=recurrence(H,d);assert (W,U)==direct(H,d)
            total+=1;maxs=max(maxs,ns);examples.append({'H':H,'d':d,'Tcal_mod841':W,'U_mod29':U})
    out={'status':'FINITE_MOD841_RECURRENCE_PASS','compared_complete_integer_convolutions':total,
         'base_rectangle':{'H_min':0,'H_max':150,'d_min':0,'d_max':24},
         'boundary_examples':examples,'maximum_live_sum_carry_states_for_fixed_input':maxs,
         'scope':'Independent finite implementation certificate. The factorial-unit/carry derivation establishes general validity; no actual third norm digit or infinite norm-unit locus is evaluated.'}
    (OUT/'convolution29_mod841_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))

if __name__=='__main__':main()
