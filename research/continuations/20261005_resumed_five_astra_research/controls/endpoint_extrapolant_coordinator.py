"""Exact finite arithmetic for a new within-index center, using the complete lift.

The coordinator inspected the archival full_lift construction and copied only
its mathematical operations. No endpoint or forcing term is omitted.
"""
from fractions import Fraction as Q
from math import factorial,comb,gcd,lcm
from functools import reduce
from pathlib import Path
import json
import sys
import sympy as sp
import mpmath as mp

OUT=Path(__file__).resolve().parent
sys.set_int_max_str_digits(20000)

def full_lift(n,b):
    d=b-1;qp=[Q(1)]
    for _ in range(n):
        new=[Q(0)]*(len(qp)+2)
        for j,a in enumerate(qp):new[j]+=a;new[j+1]-=a;new[j+2]+=a/2
        qp=new
    maxjet=2*n+d;ainv=[Q(1),Q(1)]
    for j in range(2,maxjet):ainv.append(ainv[-1]-ainv[-2]/2)
    fcoef=[Q(0)]+[2*ainv[j-1]/j for j in range(1,maxjet+1)]
    hq=[];acc=Q(0)
    for j in range(maxjet+1):acc+=Q(1,factorial(j))+fcoef[j];hq.append(acc)
    ecoef=[sum((a/Q(factorial(k-j)) for j,a in enumerate(qp) if j<=k),Q(0)) for k in range(n+d+1)]
    t=sp.Matrix(b,b,lambda i,j:ecoef[n+i-j] if n+i-j>=0 else 0)
    fp=[];fq=[]
    for i in range(b):
        r=n+i
        fp.append(factorial(n)*sum((a*comb(n+r-j,n) for j,a in enumerate(qp) if j<=r),Q(0)))
        fq.append(sum((a*Q(factorial(n+r-j),factorial(r-j))*hq[n+r-j] for j,a in enumerate(qp) if j<=r),Q(0)))
    h=t.inv()*sp.Matrix.hstack(sp.Matrix(fp),sp.Matrix(fq))
    s=sp.zeros(b,b)
    for j in range(b):
        for k in range(j,b):s[j,k]=(-1)**(k-j)*comb(n+k-j-1,k-j)*factorial(k)//factorial(j)
    z=sp.zeros(b+1,b)
    for j in range(b):z[j,j]=-1;z[j+1,j]=1
    psi=z*s*h;psi[0,1]+=1
    db=lcm(*(int(value.q) for value in psi))
    u=[int(psi[j,0]*db) for j in range(b+1)]
    v=[int(psi[j,1]*db) for j in range(b+1)]
    assert sum(u)==0 and sum(v)==db and reduce(gcd,u+v)==1
    return u,v,db

def one(n,d):
    b=d+1;u,v,db=full_lift(n,b)
    r0=gcd(u[0],v[0]);rb=gcd(u[b],v[b])
    u0=u[0]//r0;ub=u[b]//rb;v0=v[0]//r0;vb=v[b]//rb
    h=gcd(u0,ub);aA=u0//h;bB=ub//h
    gg=gcd(n*n,d);a=n*n//gg;k=d//gg
    jj=bB*v0-aA*vb;tt=a*jj+k*aA*vb
    ff=gcd(abs(aA),a)*gcd(abs(bB),a-k)
    G=gcd(k,abs(jj));H=gcd(h,abs(tt)//ff//G)
    rawden=k*h*aA*bB;rawnum=tt
    actual=Q(rawnum,rawden)
    assert actual==Q(a,k)*Q(v0,u0)+Q(k-a,k)*Q(vb,ub)
    qformula=k*h*abs(aA*bB)//ff//G//H
    assert actual.denominator==qformula
    assert qformula>=Q(abs(aA*bB),ff)
    mp.mp.dps=4*n+240
    true=mp.e+mp.pi
    target=mp.mpf(actual.numerator)/actual.denominator
    whole=actual.denominator*true-actual.numerator
    err=target-true
    coord0=mp.mpf(v[0])/u[0]-true;coordb=mp.mpf(v[b])/u[b]-true
    data={'n':n,'d':d,'b':b,'actual_U':[str(x) for x in u],'actual_V':[str(x) for x in v],
          'least_clearer':str(db),'r0':str(r0),'rb':str(rb),'h':str(h),'A':str(aA),'B':str(bB),
          'a':str(a),'k':str(k),'J':str(jj),'T':str(tt),'F':str(ff),'G':str(G),'H_gcd':str(H),
          'p_hat':str(actual.numerator),'q_hat':str(actual.denominator),
          'log_q_hat':float(mp.log(actual.denominator)),
          'log_abs_whole_form':float(mp.log(abs(whole))),
          'log_abs_center_error':float(mp.log(abs(err))),
          'center_error_sign':int(mp.sign(err)),'error_ratio_to_endpoint_b':mp.nstr(err/coordb,24),
          'error_log_ratio_endpoints':mp.nstr(mp.log(coord0/coordb),24),
          'H_over_h':str(Q(H,h)),
          'scope':'Exact rational arithmetic; numerical error uses high precision and is finite reconnaissance.'}
    print(json.dumps({key:data[key] for key in ['n','d','log_q_hat','log_abs_whole_form','error_ratio_to_endpoint_b']}),flush=True)
    return data

def main():
    dest=OUT/'endpoint_extrapolant_certificate.json'
    result=json.loads(dest.read_text()).get('cases',[]) if dest.exists() else []
    finished={(item['n'],item['d']) for item in result}
    for n in (64,65,128,129):
        for d in (2,3,4,8):
            if (n,d) in finished:continue
            result.append(one(n,d))
            dest.write_text(json.dumps({'status':'FINITE_RECONNAISSANCE','cases':result},indent=2)+'\n')
    print('COMPLETE_16_ACTUAL_PAIRS',flush=True)

if __name__=='__main__':main()
