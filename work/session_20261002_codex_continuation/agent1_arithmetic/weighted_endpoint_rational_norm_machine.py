"""L24 fixed rational diagonal modulo8 on an all-ones binary word.

Exact polynomial Cartier states, not increasing matrix determinants.
The primitive endpoint also has linear terms; this norm machine alone does
not prove q2=n+2.
"""
from pathlib import Path
from math import comb
from functools import lru_cache
import json,time,argparse
from weighted_endpoint_spectral import root15,power as rpower

BASE=Path(__file__).resolve().parent
MASK=0x7777;SHIFT=0x8888
ZERO=0;ONE=1


def pack(v):return sum((x%8)<<(4*i) for i,x in enumerate(v))
def unpack(a):return tuple((a>>(4*i))&7 for i in range(4))
def add(a,b):return (a+b)&MASK
def sub(a,b):return (a+SHIFT-b)&MASK
def scale(a,c):return pack(x*c for x in unpack(a))


@lru_cache(maxsize=262144)
def mul(a,b):
    a0,a1,a2,a3=unpack(a);b0,b1,b2,b3=unpack(b)
    d4=a1*b3+a2*b2+a3*b1;d5=a2*b3+a3*b2;d6=a3*b3
    return pack((a0*b0-d4,a0*b1+a1*b0-d4-d5,
                 a0*b2+a1*b1+a2*b0-d5-d6,
                 a0*b3+a1*b2+a2*b1+a3*b0-d6))


def power(a,n):
    out=ONE
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n//=2
    return out


def padd(a,b):
    out=a.copy()
    for ij,c in b.items():
        out[ij]=add(out.get(ij,0),c)
        if not out[ij]:del out[ij]
    return out


def pscale(a,c):return {ij:z for ij,x in a.items() if (z:=mul(x,c))}


def pmul(a,b,cartier=False):
    out={}
    for (i,j),c in a.items():
        for (u,v),d in b.items():
            x=i+u;y=j+v
            if cartier:
                if not(x%2 and y%2):continue
                x//=2;y//=2
            z=mul(c,d)
            if z:
                key=x,y;out[key]=add(out.get(key,0),z)
    return {ij:c for ij,c in out.items() if c}


def ppow(a,n):
    out={(0,0):ONE}
    while n:
        if n&1:out=pmul(out,a)
        a=pmul(a,a);n//=2
    return out


def trace(a):
    a0,a1,a2,a3=unpack(a)
    return (4*a0-3*a3)%8


def initial():
    saved=json.loads((BASE/'WEIGHTED_ENDPOINT_MOMENT_POLYNOMIAL_RECEIPT.json').read_text())
    zeta=pack(saved['zeta_coefficients']);eta=power(zeta,5)
    rise=[]
    for row in saved['positive_order_rho_polynomials_degree_at_most10']:
        coeff=[pack(a) for a in row['four_modes'][0]['integer_valued_Newton_coefficients'][:5]]
        rise.append([sumring([scale(coeff[t],(-1)**(t-s)*comb(t,s)) for t in range(s,5)])
                     for s in range(5)])
    def fourier(vals):
        return [scale(sumring([scale(power(eta,(-a*d)%3),val)
                               for d,val in enumerate(vals)]),3) for a in range(3)]
    ph=fourier([1,0,1]);rh=fourier([1,0,0]);states=[];multipliers=[];terms=[]
    for a in range(3):
        for b in range(a,3):
            if a==b:
                wa=mul(ph[a],rh[a]);wb=add(mul(ph[a],ph[a]),mul(rh[a],rh[a]))
            else:
                wa=add(mul(ph[a],rh[b]),mul(ph[b],rh[a]))
                wb=scale(add(mul(ph[a],ph[b]),mul(rh[a],rh[b])),2)
            pole={(0,0):1,(1,0):sub(0,mul(zeta,power(eta,a))),
                  (0,1):sub(0,mul(zeta,power(eta,b)))}
            num={}
            for s in range(5):
                coef=add(mul(wa,add(rise[1][s],rise[3][s])),mul(wb,rise[2][s]))
                num=padd(num,pscale(ppow(pole,4-s),coef))
            xy={(0,0):1,(1,0):7,(0,1):7,(1,1):1}
            Q=pmul(xy,ppow(pole,5))
            P=pmul(num,ppow(Q,3))
            states.append(P);terms.append([a,b]);qs=[]
            for phase in range(4):
                z=power(zeta,2**phase);et=power(eta,2**phase)
                qp={(0,0):1,(1,0):sub(0,mul(z,power(et,a))),
                    (0,1):sub(0,mul(z,power(et,b)))}
                qs.append(ppow(pmul(xy,ppow(qp,5)),4))
            multipliers.append(qs)
    return states,multipliers,terms


def sumring(a):
    z=0
    for x in a:z=add(z,x)
    return z


def key(states,phase):
    return phase,tuple(tuple(sorted(p.items())) for p in states)


def serialize(states):
    return [[[i,j,c] for (i,j),c in sorted(p.items())] for p in states]


def run(limit=32):
    started=time.monotonic();states,qs,terms=initial();phase=0;seen={};receipts=[];orbit=[]
    while len(receipts)<=limit:
        statekey=key(states,phase)
        if statekey in seen:
            pre=seen[statekey];period=len(receipts)-pre
            out={'status':'AUTHOR fixed rational norm Cartier orbit CLOSED',
                 'coefficient_ring':'(Z/8)[x]/(x^4+x+1)',
                 'unordered_root3_terms':terms,'initial_and_orbit_states':orbit,
                 'outputs':receipts,'full_state_preperiod':pre,'full_state_period':period,
                 'coefficient_box_bound':[24,24],
                 'primitive_endpoint_linear_corrections_not_evaluated':True}
            (BASE/'WEIGHTED_ENDPOINT_RATIONAL_NORM_RECEIPT.json').write_text(json.dumps(out)+'\n')
            print(json.dumps({'orbit_closed':True,'preperiod':pre,'period':period,'outputs':receipts},indent=2),flush=True)
            return
        seen[statekey]=len(receipts)
        value=trace(sumring([p.get((0,0),0) for p in states]))
        h=len(receipts)
        if h in (1,3,5):assert value=={1:2,3:4,5:6}[h]
        receipts.append({'h':h,'m_power2':h,'periodic_norm_q0_mod8':value,
                         'state_nonzero_counts':[len(p) for p in states]})
        orbit.append(serialize(states))
        print(json.dumps({'h':h,'q0':value,'counts':[len(p) for p in states],
                          'elapsed_seconds':round(time.monotonic()-started,1)}),flush=True)
        states=[pmul(p,qs[i][phase],cartier=True) for i,p in enumerate(states)]
        phase=(phase+1)%4
        assert all(max((i for i,j in p),default=0)<=24 and max((j for i,j in p),default=0)<=24 for p in states)
    out={'status':'AUTHOR fixed rational norm Cartier orbit PARTIAL, no closure claim',
         'unordered_root3_terms':terms,'outputs':receipts,'orbit_states':orbit,
         'primitive_endpoint_linear_corrections_not_evaluated':True}
    (BASE/'WEIGHTED_ENDPOINT_RATIONAL_NORM_RECEIPT.json').write_text(json.dumps(out)+'\n')


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--max-depth',type=int,default=32)
    run(parser.parse_args().max_depth)
