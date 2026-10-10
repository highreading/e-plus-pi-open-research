"""Personally authored finite F2 contact calculation for a filtered top bit.

This audits an explicitly stated coefficient candidate. The reduction to the
actual precision96 limit requires the separate mathematical filtration proof.
No growing original matrix or credential is read.
"""
from pathlib import Path
from math import comb
import hashlib,json

OUT=Path(__file__).resolve().parent
N=-190

def zbin(n,r):
    if r<0:return 0
    if n>=0:return comb(n,r) if r<=n else 0
    return (-1)**r*comb(r-n-1,r)
def bitbin(n,r):return int(r>=0 and r<=n and (r&~n)==0)
def suffix(a):
    acc=0;out=[0]*len(a)
    for i in range(len(a)-1,-1,-1):
        acc^=a[i];out[i]=acc
    return out
def op(a):
    T=[a]
    for _ in range(4):T.append(suffix(T[-1]))
    out=[0]*len(a)
    for s in [1,3,4]:
        for v in range(s+1):
            if zbin(N,v)%2==0:continue
            r=s-v
            for x in range(r,len(a)):
                if bitbin(x,r):out[x]^=T[v][x-r]
    return out
def newton_mod2(a):
    out=[]
    while a:
        out.append(a[0]);a=[x^y for x,y in zip(a,a[1:])]
    return out

def main():
    residue=(-95*pow(2001,-1,512))%512
    results=[]
    for B in [residue+512,residue+1024]:
        a=[bitbin(x,1)^bitbin(x,2)^bitbin(x,3) for x in range(B)]
        degrees=[]
        for q in range(1,96):
            a=op(a)
            if q in [1,2,3,4,8,16,32,64,94,95]:
                cs=newton_mod2(a[:])
                degree=max((i for i,x in enumerate(cs) if x),default=-1)
                assert all(x==0 for x in cs[4*q+4:])
                degrees.append({'q':q,'actual_F2_degree':degree,'top_coeff380':cs[380] if len(cs)>380 else 0})
        cs=newton_mod2(a[:])
        candidate=cs[380];direct=0
        for j in range(381):
            if bitbin(380,j):direct^=a[j]
        assert candidate==direct
        results.append({'finite_endpoint':B,'continuation_b_mod512':residue,
                        'E95_g_coefficient380_mod2':candidate,'degrees':degrees,
                        'finite_difference_and_Lucas_extraction_match':True})
    assert results[0]['E95_g_coefficient380_mod2']==results[1]['E95_g_coefficient380_mod2']
    payload={'status':'FILTERED_TOP_BIT_CANDIDATE_CERTIFIED','cases':results,
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'scope':'Complete finite F2 operator at two polynomial endpoint representatives. Actual precision96 coefficient reduction is a separately audited mathematical obligation.'}
    (OUT/'binary_limit_top_bit_certificate.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload),flush=True)
if __name__=='__main__':main()
