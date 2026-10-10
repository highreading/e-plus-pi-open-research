#!/usr/bin/env python3
"""New complete-prefix min-plus valuations for phase-compatible atoms."""
from pathlib import Path
import hashlib
import json
import resource
from normalized_gram29_coordinator import p,digits

resource.setrlimit(resource.RLIMIT_CPU,(90,90))
ROOT=Path(__file__).resolve().parent

def minimum(b,n,a,v):
    inp=(b-1,n+2,b+v,2*n+a-1)
    L=1
    while p**L<=max(inp):L+=1
    L+=2;ds=[digits(x,L) for x in inp]
    states={(0,0,0,0):(0,0)};low=None
    for i in range(L):
        J,N,K,A=(z[i] for z in ds);nxt={}
        for (qj,qw,qk,ca),(cost,j) in states.items():
            for d in range(p):
                qjp=int(J-d-qj<0);qwp=int(N-d-qw<0);qkp=int(K-d-qk<0)
                cap=(A+(K-d-qk)%p+ca)//p
                target=(qjp,qwp,qkp,cap)
                candidate=(cost+qwp+cap,j+d*p**i)
                if target not in nxt or candidate<nxt[target]:nxt[target]=candidate
        states=nxt
        if i==5:low={''.join(map(str,k)):z[0] for k,z in states.items()}
    value,j=states[(0,0,0,0)]
    assert 0<=j<b and b+v-j>=0
    # Independently check the witness valuation with the floor-factorial law.
    def vf(x):
        ans=0
        while x:x//=p;ans+=x
        return ans
    k=b+v-j;A=2*n+a-1
    check=vf(n+2)-vf(j)-vf(n+2-j)+vf(A+k)-vf(A)-vf(k)
    assert check==value
    return {'minimum':value,'witness_j':str(j),'layers':L,'six_digit_minimum_vector':low}

def main():
    rows=[]
    for C in (0,1,2,3,4,5,8,9,28):
        b=410910916+29**6*C;n=2001*b
        atoms=[{'a':a,'v':v,**minimum(b,n,a,v)} for a,v in ((1,0),(1,-1),(30,-29),(30,-30))]
        rows.append({'C':C,'b':str(b),'n':str(n),'original_power':False,'atoms':atoms})
    cert={'status':'PASS','scope':'complete-prefix valuation minima for nine new auxiliary phases and four normalized atoms, with independent floor-factorial witnesses',
          'controls':rows,'original_power_evaluated':False,'original_norm_evaluated':False}
    target=ROOT/'weighted_atom_minimum29_certificate.json';target.write_text(json.dumps(cert,indent=2)+'\n')
    receipt={'status':'PASS','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
             'minimum_table':[[z['C'],[a['minimum'] for a in z['atoms']]] for z in rows],
             'auxiliary_cases':len(rows),'witness_checks':4*len(rows),'original_power_evaluated':False}
    (ROOT/'weighted_atom_minimum29_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2),flush=True)

if __name__=='__main__':main()
