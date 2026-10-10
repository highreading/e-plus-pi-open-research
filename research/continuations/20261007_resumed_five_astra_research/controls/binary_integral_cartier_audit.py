"""Parent-authored bounded sparse-polynomial audit; no remote code execution."""
from pathlib import Path
from math import comb
import json, hashlib, time
ROOT=Path(__file__).resolve().parent
START=time.monotonic()

def binom(n,k):
    return comb(n,k) if 0<=k<=n else 0

def add_scaled(out,poly,scale,mod):
    for exp,val in poly.items():
        out[exp]=(out.get(exp,0)+scale*val)%mod
    return {e:v for e,v in out.items() if v}

def unary_mul(a,b,mod):
    out={}
    for i,x in a.items():
        for j,y in b.items():out[i+j]=(out.get(i+j,0)+x*y)%mod
    return {e:v for e,v in out.items() if v}

def unary_power(power,degree,sign,mod):
    return {power*j:(comb(degree,j)*sign**j)%mod for j in range(degree+1)
            if comb(degree,j)%mod}

def numerator_multiplier(N,L):
    mod=1<<L;h,eps=divmod(N,2);H=min(h,L-1);out={}
    for r in range(H+1):
        term={r+e:v for e,v in unary_power(2,H-r,1,mod).items()}
        out=add_scaled(out,term,(1<<r)*comb(h,r),mod)
    if eps:out=unary_mul(out,{0:1,1:1},mod)
    return out,h-H

def denominator_multiplier(M,L,repaired=True):
    mod=1<<L;h,eps=divmod(M,2);out={}
    for j in range(L):
        coefficient=1 if j==0 else (comb(h+j-1,j) if h else 0)
        if not coefficient:continue
        term=unary_power(2,L-1-j,-1,mod)
        if repaired:term=unary_mul(term,unary_power(1,j,-1,mod),mod)
        term={j+e:v for e,v in term.items()}
        out=add_scaled(out,term,(1<<j)*coefficient,mod)
    if eps:out=unary_mul(out,{0:1,1:1},mod)
    return out,h+eps+L-1

def line_multiply(P,U,direction,mod):
    out={};dt,dx,dy=direction
    for (t,x,y),v in P.items():
        for j,w in U.items():
            key=(t+j*dt,x+j*dx,y+j*dy)
            out[key]=(out.get(key,0)+v*w)%mod
    return {e:v for e,v in out.items() if v}

def box(P):
    if not P:return {'terms':0,'t_degree':0,'x_width':0,'y_width':0}
    ts,xs,ys=zip(*P)
    assert min(ts)>=0
    return {'terms':len(P),'t_degree':max(ts),
            'x_width':max(xs)-min(xs),'y_width':max(ys)-min(ys)}

def accept(N,M,target,d,delta,L,repaired=True):
    mod=1<<L;P={(0,d,delta):1};records=[]
    directions=[(0,1,0),(1,-1,0),(1,0,1),(0,0,-1)]
    max_steps=max([target,*N]).bit_length()+2
    for stage in range(max_steps):
        if target==0 and all(x==0 for x in N):
            return P.get((0,0,0),0),records
        multipliers=[];newN=[]
        for nn in N:
            uu,nnew=numerator_multiplier(nn,L);multipliers.append(uu);newN.append(nnew)
        den,Mnew=denominator_multiplier(M,L,repaired)
        P=line_multiply(P,den,(1,0,0),mod)
        for uu,vec in zip(multipliers,directions):P=line_multiply(P,uu,vec,mod)
        parity=target%2
        P={(t//2,x//2,y//2):v for (t,x,y),v in P.items()
           if t%2==parity and x%2==0 and y%2==0}
        N=newN;M=Mnew;target//=2
        rec=box(P);rec.update({'stage':stage+1,'target':target})
        J=2*L-1
        assert rec['x_width']<=2*J and rec['y_width']<=2*J
        assert rec['t_degree']<=3*J and rec['terms']<=(3*J+1)*(2*J+1)**2
        records.append(rec)
        if not P:return 0,records
        if time.monotonic()-START>240:raise RuntimeError('Audit time bound reached')
    raise AssertionError('Halving bound failed')

def audit_kernel(b,n,L,d,eta1,eps1,eta2,eps2):
    if eps1>eps2:eta1,eta2,eps1,eps2=eta2,eta1,eps2,eps1
    delta=eps2-eps1;a1=eta1-eps1;a2=eta2-eps2;mod=1<<L
    direct=sum(binom(n+2,j)**2*binom(j,d)*
               binom(2*n+b+eta1-j,b+eps1-j)*
               binom(2*n+b+eta2-j,b+eps2-j) for j in range(b))%mod
    N=[n+2-d,n+2,2*n+a1-delta,2*n+a2+delta]
    M=4*n+a1+a2+1
    assert min(N)>=0 and b+eps1>=0
    acc,records=accept(N,M,b+eps1,d,delta,L)
    acc=acc*binom(n+2,d)%mod
    tail=0
    if eps1>=0:
        A=2*n+a1;B=2*n+a2
        tail=sum(binom(n+2,b+eps1-j)**2*binom(b+eps1-j,d)*
                 binom(A+j,j)*binom(B+j+delta,j+delta) for j in range(eps1+1))%mod
    observed=(acc-tail)%mod
    assert observed==direct,(b,n,L,d,eta1,eps1,eta2,eps2,direct,acc,tail)
    maxima={k:max((r[k] for r in records),default=0) for k in ('terms','t_degree','x_width','y_width')}
    return {'b':b,'n':n,'L':L,'d':d,'eta1':eta1,'eps1':eps1,'eta2':eta2,'eps2':eps2,
            'direct':direct,'acceptance':acc,'tail':tail,'difference':(observed-direct)%mod,
            'stages':len(records),'maximum_observed_support':maxima,'stage_records':records}

# Exhibit the reported denominator error independently before kernel tests.
bad,_=denominator_multiplier(2,2,False)
good,_=denominator_multiplier(2,2,True)
def rational_coefficient(poly,M,targ,mod):
    return sum(v*binom(M+(targ-e)//2-1,(targ-e)//2) for e,v in poly.items()
               if e<=targ and (targ-e)%2==0)%mod
assert rational_coefficient(bad,2,2,4)==1
assert rational_coefficient(good,2,2,4)==3

rows=[(0,-1,0,-1,0),(3,2,-2,5,3),(2,2,1,4,3),(4,3,4,-1,0)]
cases=[]
for row in rows:
    case=audit_kernel(11,44022,5,*row);cases.append(case)
    print(json.dumps({k:v for k,v in case.items() if k!='stage_records'}),flush=True)
for b,L,row in [(3,2,(0,0,0,1,1)),(7,3,(1,3,-1,2,2)),(5,4,(2,2,0,0,-1))]:
    cases.append(audit_kernel(b,4002*b,L,*row))
out={'scope':'Seven new auxiliary finite kernel checks. Corrected denominator transition; exact finite boundary and short tails. No original-family primitive valuation, merging claim or all-prime denominator/error conclusion.',
     'reported_denominator_counterexample':{'M':2,'L':2,'t_degree':2,'actual':3,'reported':1,'repaired':3},
     'cases':cases,'all_passed':True,'elapsed_seconds':round(time.monotonic()-START,3),
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'binary_integral_cartier_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'all_passed':True,'case_count':len(cases),'seconds':out['elapsed_seconds']}),flush=True)
