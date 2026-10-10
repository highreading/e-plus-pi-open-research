#!/usr/bin/env python3
"""New exact coefficient-content/min-plus corroboration; no Schur evaluation."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json
import resource

resource.setrlimit(resource.RLIMIT_CPU,(120,120))
ROOT = Path(__file__).resolve().parent

def digits3(x):
    out = []
    while x:
        x,r = divmod(x,3)
        out.append(r)
    return out or [0]

def valuation(x):
    x = F(x)
    if not x:
        return 100000
    a,b = abs(x.numerator),x.denominator
    v = 0
    while a%3 == 0:
        a //= 3
        v += 1
    while b%3 == 0:
        b //= 3
        v -= 1
    return v

def content_dp(m,adjacent=False):
    degree = m-int(adjacent)
    assert degree>=0
    N = 3*m-1-int(adjacent)
    numerator = 2*m-1-2*int(adjacent)
    L = len(digits3(N))+3
    q = 3**L
    alpha = (numerator*pow(2,-1,q))%q
    ds = [digits3(x)+[0]*L for x in (degree,N,alpha)]
    states = {(0,0,0):(0,0)}
    max_states = 1
    for i in range(L):
        new = {}
        mi,ni,ai = (z[i] for z in ds)
        for (carry,borrow,ab),(cost,k) in states.items():
            for kd in range(3):
                for rd in range(3):
                    total = kd+rd+carry-mi
                    if total not in (0,3):
                        continue
                    bnew,anew = int(ni-kd-borrow<0),int(ai-rd-ab<0)
                    st = (total//3,bnew,anew)
                    candidate = (cost+bnew+anew,k+kd*3**i)
                    if st not in new or candidate<new[st]:
                        new[st] = candidate
        states = new
        max_states = max(max_states,len(states))
        assert len(states)<=8
    result,k = states[(0,0,0)]
    assert 0<=k<=degree
    return result,k,max_states,L

def content_exact(m,adjacent=False):
    degree = m-int(adjacent)
    N = 3*m-1-int(adjacent)
    alpha = F(2*m-1-2*int(adjacent),2)
    b = [F(1)]
    for r in range(1,degree+1):
        b.append(b[-1]*(alpha-r+1)/r)
    costs = [valuation(comb(N,k)*b[degree-k]) for k in range(degree+1)]
    return min(costs),costs

def main():
    bounded = []
    for m in range(1,161):
        for adj in (False,True):
            dp,k,states,L = content_dp(m,adj)
            exact,costs = content_exact(m,adj)
            assert dp==exact and costs[k]==exact
            bounded.append({'m':m,'adjacent':adj,'content':dp,'witness_k':k,'max_states':states})
    powers = []
    # These are genuine original powers but lack the very narrow real window.
    for j in (81,324,567,810,1053,1296,1539,1782,2025,2268,2511):
        m = 1<<(2*j-1)
        r,kr,_,Lr = content_dp(m)
        u,ku,_,Lu = content_dp(m,True)
        powers.append({'j':j,'j_mod243':j%243,'m_binary_digits':m.bit_length(),
                       'm_ternary_digits':len(digits3(m)),'r':r,'u':u,
                       'J_witness_k':str(kr),'adjacent_witness_k':str(ku),
                       'layers':[Lr,Lu],'real_window_certified':False,
                       'resonance_depth_truncated_at16':next((t for t in range(1,17) if pow(4,j+1,3**t)!=247%(3**t)),17)-1})
    cert = {'status':'PASS','scope':'320 bounded exact full-coefficient minima and11 genuine power-of-two inputs; no narrow real-window or whole inverse-content certificate',
            'bounded_cases':bounded,'power_inputs':powers,'whole_E_content_computed':False,
            'original_window_inverse_loss_decided':False,'irrationality_proved':False}
    target = ROOT/'jacobi_content_digit_certificate.json'
    target.write_text(json.dumps(cert,indent=2)+'\n')
    receipt = {'status':'PASS','scope':cert['scope'],
               'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
               'bounded_exact_checks':len(bounded),'power_inputs':len(powers),
               'power_content_pairs':[[z['j'],z['r'],z['u']] for z in powers],
               'max_observed_states':max(z['max_states'] for z in bounded),
               'whole_E_content_computed':False,'original_window_inverse_loss_decided':False}
    (ROOT/'jacobi_content_digit_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':
    main()
