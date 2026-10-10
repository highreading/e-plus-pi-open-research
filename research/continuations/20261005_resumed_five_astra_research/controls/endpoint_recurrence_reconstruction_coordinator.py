"""Personally authored actual finite d=2 recurrence and reconstruction audit.

Uses prior exact whole-column outputs as normalization comparisons. No network,
credentials, or remote code. Four finite cases cannot establish infinite scale.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb,gcd,isqrt
import hashlib,json
import sympy as sp

ROOT=Path(__file__).resolve().parent

def vp_int(a,p):
    if not a:return None
    a=abs(a);v=0
    while a%p==0:a//=p;v+=1
    return v

def vp(a,p):
    a=F(a)
    return None if not a else vp_int(a.numerator,p)-vp_int(a.denominator,p)

def residue(a,mod):
    a=F(a);return a.numerator*pow(a.denominator,-1,mod)%mod

def mulQ(a):
    out=[F(0)]*(len(a)+2)
    for i,x in enumerate(a):out[i]+=x;out[i+1]-=x;out[i+2]+=x/2
    return out

def matrix(values):
    return sp.Matrix([sp.Rational(x.numerator,x.denominator) for x in values])

def toF(x):return F(int(x.p),int(x.q))
def floor(x):return x.numerator//x.denominator
def ceil(x):return -floor(-x)

def factorial_depth(n,p):
    s=0
    while n:n//=p;s+=n
    return s

def logarithm_floor(n,p):
    v=0
    while n>=p:n//=p;v+=1
    return v

def crt(entries):
    root=0;mod=1
    for r,m in entries:
        root+=mod*((r-root)*pow(mod,-1,m)%m);mod*=m
    return root%mod,mod

def Sbounds():
    degree=256
    lo=sum((F(1,factorial(k)) for k in range(degree+1)),F(0))
    hi=lo+F(degree+2,(degree+1)*factorial(degree+1))
    def atan(c):
        x=F(1,c);v=sum(((-1)**k*x**(2*k+1)/(2*k+1) for k in range(degree)),F(0))
        return v,v+x**(2*degree+1)/(2*degree+1)
    a,b=atan(5),atan(239)
    return lo+16*a[0]-4*b[1],hi+16*a[1]-4*b[0]

def one(case):
    n=case['n'];U=[int(x) for x in case['U']];V=[int(x) for x in case['V']];db=int(case['least_clearer'])
    qp=[F(1)]
    for _ in range(n):qp=mulQ(qp)
    qp1=mulQ(qp);fac=[factorial(i) for i in range(2*n+4)]
    alpha=[F(1),F(1)]
    for i in range(2,2*n+3):alpha.append(alpha[-1]-alpha[-2]/2)
    W=[];We=[];acc=F(0);logacc=F(0)
    for m in range(2*n+3):
        acc+=F(1,fac[m])
        if m:logacc+=2*alpha[m-1]/m
        We.append(fac[m]*acc);W.append(fac[m]*(acc+logacc))
    def exponential(q):
        return [sum((q[j]*(fac[N]//fac[N-j]) for j in range(min(N,len(q)-1)+1)),F(0)) for N in range(n+3)]
    B=exponential(qp);Bp=exponential(qp1)
    R=[F(1)]
    for k in range(n):
        out=[F(0)]*(len(R)+1)
        for j,x in enumerate(R):
            if j:
                out[j-1]+=j*x;out[j]-=j*x;out[j+1]+=j*x/2
            out[j]+=(k+1)*x;out[j+1]-=(k+1)*x
        R=out
    assert R[-1]==F((-1)**n*fac[n+1],1<<n)
    a=[W[n]]
    for N in range(n+2):
        prev1=a[N-1] if N else F(0);prev2=a[N-2] if N>=2 else F(0)
        polynomial=2*fac[N]*R[N] if N<=n else F(0)
        a.append((2*N+1)*a[N]+F(N*(2*n+1-3*N),2)*prev1
                 +F(N*(N-1)*(N-n-1),2)*prev2+Bp[N]+polynomial)
    # Independently use the complete finite sum for every retained a_N.
    direct=[]
    for N in range(n+3):
        direct.append(sum((qp[j]*(fac[N]//fac[N-j])*W[n+N-j]
                           for j in range(min(2*n,N)+1)),F(0)))
    assert a==direct
    C=sp.Matrix(3,3,lambda i,j:sp.Rational((F(fac[n+i],fac[n+i-j])*B[n+i-j]).numerator,
                                          (F(fac[n+i],fac[n+i-j])*B[n+i-j]).denominator))
    tau=[]
    for N in range(n,n+3):tau.append(sum((F(comb(N,2*k)*comb(2*k,k),1<<k) for k in range(N//2+1)),F(0)))
    t=[sum((qp[j]*comb(2*n+i-j,n) for j in range(min(2*n,n+i)+1)),F(0)) for i in range(3)]
    assert t==[tau[0],(tau[0]+tau[1])/2,tau[2]/2]
    z=[fac[n+i]*fac[n]*t[i] for i in range(3)]
    w=a[n:n+3]
    wexp=[sum((qp[j]*(fac[n+i]//fac[n+i-j])*We[2*n+i-j]
               for j in range(min(2*n,n+i)+1)),F(0)) for i in range(3)]
    inv=C.inv();x=inv*matrix(z);y=inv*matrix(w);ye=inv*matrix(wexp)
    s=sp.Matrix([1,-n,n*(n+1)])
    u0=toF(-(s.T*x)[0]);ub=toF(x[2]);v0=toF(1-(s.T*y)[0]);vb=toF(y[2]);v0e=toF(1-(s.T*ye)[0])
    assert (u0,ub,v0,vb)==(F(U[0],db),F(U[-1],db),F(V[0],db),F(V[-1],db))
    theta=u0*vb/(u0*vb-ub*v0)
    A=int(case['A']);Brow=int(case['B']);J=int(case['J']);h=int(case['h'])
    v0row=V[0]//int(case['r0']);vbrow=V[-1]//int(case['rb'])
    assert theta==-F(A*vbrow,J)
    primes=[p for p in (3,5,7) if n%p==0];info=[]
    for p in primes:
        m=2*factorial_depth(n,p);K=m-logarithm_floor(2*n+2,p)
        assert vp(v0-v0e,p) is None or vp(v0-v0e,p)>=K
        assert vp(theta-1,p)==vp(v0,p)
        row={'p':p,'m':m,'K':K,'v_p_v0':vp(v0,p),'log_force_difference_depth':vp(v0-v0e,p),
             'theta_full_residue':str(residue(theta,p**m)),
             'theta_denominator_unit':theta.denominator%p!=0}
        if p==3:assert residue(v0/n,3)==2;row['v0_over_n_mod_p']=2
        if p==7:assert residue(v0/n,7)==6;row['v0_over_n_mod_p']=6
        if p==5:assert vp(v0,p)>=2
        info.append(row)
    # Exact conservative Q(sqrt2) window. Endpoints differ by less than2^-245.
    pow2=1<<256;rootlo=F(isqrt(2*pow2*pow2),pow2);roothi=rootlo+F(1,pow2)
    tlo=F(n*n+n,2)-F(3*n,2)*roothi;thi=F(n*n+n,2)-F(3*n,2)*rootlo
    height=n**3;Cwindow=16;kmax=floor(F(height)/(tlo-Cwindow));windows=[]
    sets=[(3,5)]+([(3,5,7)] if n%7==0 else [])
    slo,shi=Sbounds()
    for pset in sets:
        for kind in ('strip','penultimate','full'):
            entries=[]
            for p in pset:
                row=next(v for v in info if v['p']==p)
                level=row['K'] if kind=='strip' else row['m']-(kind=='penultimate')
                mod=p**level;entries.append((residue(theta,mod),mod))
            rt,L=crt(entries);candidates=[];eligible=0
            for k in range(1,kmax+1):
                if gcd(k,L)!=1:continue
                eligible+=1
                amin=max(-height,ceil(k*(tlo-Cwindow)));amax=min(height,floor(k*(thi+Cwindow)))
                r=rt*k%L;start=r+ceil(F(amin-r,L))*L
                for aa in range(start,amax+1,L):
                    if gcd(aa,k)!=1:continue
                    # Inner bounds certify the same exact algebraic window.
                    assert k*(thi-Cwindow)<=aa<=k*(tlo+Cwindow)
                    TT=aa*J+k*A*vbrow
                    FF=gcd(abs(A),abs(aa))*gcd(abs(Brow),abs(aa-k));GG=gcd(k,abs(J))
                    assert TT%(FF*GG)==0
                    HH=gcd(h,abs(TT)//(FF*GG));q=k*h*abs(A*Brow)//(FF*GG*HH)
                    pn=(1 if A*Brow>0 else -1)*TT//(FF*GG*HH)
                    center=F(aa,k)*F(v0row,U[0]//int(case['r0']))+F(k-aa,k)*F(vbrow,U[-1]//int(case['rb']))
                    assert center==F(pn,q) and gcd(abs(pn),q)==1
                    lo,hi=q*slo-pn,q*shi-pn
                    candidates.append({'a':aa,'k':k,'F':str(FF),'G':str(GG),'H':str(HH),
                                       'q':str(q),'p':str(pn),'whole_form_sign':1 if lo>0 else (-1 if hi<0 else 0)})
            windows.append({'primes':list(pset),'modulus_kind':kind,'modulus':str(L),'residue':str(rt),
                            'height':height,'window_radius':Cwindow,'denominator_upper_bound':kmax,
                            'eligible_denominators_checked':eligible,'candidates':candidates,
                            'empty_certified':not candidates})
    result={'n':n,'d':2,'complete_recurrence_checks':n+3,'three_tau_identity_pass':True,
            'whole_column_endpoints_match':True,'moving_residue_match':True,'local_depths':info,'windows':windows}
    print(json.dumps({'n':n,'recurrence_checks':n+3,'w5':next(v['v_p_v0'] for v in info if v['p']==5),
                     'window_counts':[len(v['candidates']) for v in windows]}),flush=True)
    return result

if __name__=='__main__':
    prior=json.loads((ROOT/'general_endpoint_weights_certificate.json').read_text())
    out={'status':'PASS','scope':'Four actual complete finite producers, recurrence identities and bounded height/window lists; no infinite reconstruction or all-prime asymptotic theorem',
         'cases':[one(v) for v in prior['cases']],
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    dest=ROOT/'endpoint_recurrence_reconstruction_certificate.json';dest.write_text(json.dumps(out,indent=2)+'\n')
    receipt={'status':'PASS','artifact_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'source_sha256':out['source_sha256'],
             'cases':[{'n':v['n'],'recurrence_checks':v['complete_recurrence_checks'],'local_depths':v['local_depths'],
                       'window_candidate_counts':[len(w['candidates']) for w in v['windows']]} for v in out['cases']],
             'scope':out['scope']}
    (ROOT/'endpoint_recurrence_reconstruction_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
