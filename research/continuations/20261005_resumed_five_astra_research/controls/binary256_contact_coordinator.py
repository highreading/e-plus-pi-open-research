"""Coordinator-authored bounded finite contact calculation; no network or credentials.

Newton coefficients are reduced directly, with no modular division by even integers.
The exterior kernel and interior operator are also checked as finite matrices.
"""
from math import comb
from pathlib import Path
import json

OUT=Path(__file__).resolve().parent
N=322; BOUND=209
U={1:-1,2:2,3:-3,4:3}
EXTERIOR=[197,234,54,56,248,208,112,128,128]
FORCE=[66,247,115,135,76,92,176,112,0,192,64,64]

def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def values(a,count,mod):
    return [sum(c*comb(x,r) for r,c in enumerate(a) if r<=x)%mod for x in range(count)]

def newton(v,mod):
    result=[]
    while v:
        result.append(v[0]%mod)
        v=[(v[j+1]-v[j])%mod for j in range(len(v)-1)]
    return trim(result)

def cs_values(a,s,count,mod,n=N,b=BOUND):
    f=values(a,b,mod)
    ans=[]
    for x in range(count):
        total=0
        for v in range(s+1):
            shift=s-v
            if shift>x:continue
            y=x-shift
            weight=(-1)**shift*comb(x,shift)*comb(n,v)
            if v==0:tail=f[y]
            else:tail=sum(comb(v+k-y-1,v-1)*f[k] for k in range(y,b))
            total+=weight*tail
        ans.append(total%mod)
    return ans

def operator(a,terms,mod,n=N,b=BOUND):
    count=len(a)+max(terms)
    parts=[(c,cs_values(a,s,count,mod,n,b)) for s,c in terms.items()]
    return newton([sum(c*v[x] for c,v in parts)%mod for x in range(count)],mod)

def exterior_value(s,x,n=N,b=BOUND,mod=None):
    total=sum((-1)**(b+a+s-v)*ba*comb(x,s-v)*comb(n,v)*comb(b+a-x+s-1,v-1)
              for a,ba in enumerate(EXTERIOR) for v in range(1,s+1) if s-v<=x)
    return total if mod is None else total%mod

def a_poly(n=N,b=BOUND):
    return newton([sum(c*exterior_value(s,x,n,b) for s,c in U.items()) for x in range(4)],256)

def add_scaled(acc,a,c,mod):
    acc.extend([0]*max(0,len(a)-len(acc)))
    for r,v in enumerate(a):acc[r]=(acc[r]+c*v)%mod
    return trim(acc)

def pair(n=N,b=BOUND):
    p=[0];g=[x%128 for x in FORCE]
    for ell in range(7):
        add_scaled(p,g,pow(-66,ell,128),128)
        if ell<6:g=operator(g,U,128,n,b)
    a=a_poly(n,b);q=[0];state=a[:]
    for ell in range(7):
        add_scaled(q,state,66*pow(-66,ell,256),256)
        if ell<6:state=operator(state,U,256,n,b)
    add_scaled(q,[0,128,0,0,0,0,0,128],1,256)
    return p,q,a

def coefficient_residual(a,terms,mult,force,mod):
    r=a[:]
    add_scaled(r,operator(a,terms,mod),mult,mod)
    add_scaled(r,force,-1,mod)
    return trim(r)

def finite_kernel(s,i,j,n=N):
    total=0
    for v in range(s+1):
        shift=s-v
        low=j-i+shift
        if shift>i or low<0:continue
        if v==0:term=int(low==0)
        else:term=(-1)**low*comb(v+low-1,v-1)
        total+=comb(i,shift)*comb(n,v)*term
    return total

def main():
    p,q,a=pair()
    assert len(p)<=28 and len(q)<=28
    pres=coefficient_residual(p,U,66,FORCE,128)
    qforce=[66*c%256 for c in a]
    add_scaled(qforce,[0,128,0,0,0,0,0,128],1,256)
    qres=coefficient_residual(q,U,66,qforce,256)
    add_scaled(qres,operator(q,{2:1,5:1,7:1,8:1},256),128,256)
    assert all(x==0 for x in pres+qres),(pres,qres)
    oldp=[34,31,7,5,48,12,4,4,32,8,56,8]
    oldq=[52,36,24,6,112,48,64,8,32,32,64,112]
    p28=p+[0]*(28-len(p));q28=q+[0]*(28-len(q))
    assert [v%64 for v in p28]==oldp+[0]*16
    assert [v%128 for v in q28]==oldq+[0]*16
    jpoly=newton([sum(exterior_value(s,x) for s in (2,5,7,8)) for x in range(8)],2)
    assert jpoly==[0,1,0,0,0,0,0,1],jpoly
    # Independently evaluate the actual finite signed kernels at every reference row.
    fv=values(q,BOUND,256)
    for s in range(1,9):
        byop=cs_values(q,s,BOUND,256)
        for i in range(BOUND):
            bymatrix=sum(finite_kernel(s,i,j)*(-1)**(i+j)*fv[j] for j in range(BOUND))%256
            assert bymatrix==byop[i],(s,i)
        for i in range(4):
            raw=sum(finite_kernel(s,i,BOUND+j)*ba for j,ba in enumerate(EXTERIOR))*(-1)**i
            assert raw==exterior_value(s,i),(s,i)
    # Finite corroboration of the separate coefficient-cylinder proof.
    shifts=[]
    for n,b in [(834,209),(322,465),(834,465)]:
        pp,qq,aa=pair(n,b)
        assert pp==p and qq==q,(n,b)
        shifts.append({'n':n,'b':b,'coefficient_match':True})
    out={'status':'EXACT_FINITE_CONTACT_PASS','n_reference':N,'b_reference':BOUND,
         'boundary_A_mod128':[v%128 for v in a], 'P_mod128':p28,'Q_mod256':q28,
         'difference_Q_minus_2P_mod256':[(v-2*w)%256 for w,v in zip(p28,q28)],
         'P_residual_mod128':pres,'Q_residual_mod256':qres,
         'new_exterior_insertion_J_mod2':jpoly,'all_eight_finite_kernel_actions_checked_rows':BOUND,
         'finite_cylinder_corroboration':shifts,
         'scope':'Exact bounded coefficient vectors and finite matrix action. Arbitrary-size transfer still uses the mathematical proof; actual high carry not evaluated.'}
    (OUT/'binary256_contact_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))

if __name__=='__main__':main()
