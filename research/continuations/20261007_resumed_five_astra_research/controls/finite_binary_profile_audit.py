"""Independent bounded arithmetic audit of A5turn14 finite identities.

All code is personally authored by the coordinator. Auxiliary small b values are
NOT original approximation indices. This can refute identities, not prove an
original-family valuation or irrationality claim.
"""
from pathlib import Path
from functools import lru_cache
from math import comb
import json, time

ROOT = Path(__file__).resolve().parent

@lru_cache(None)
def choose(n, k):
    if k < 0: return 0
    if n < 0: return (-1)**k * comb(k-n-1,k)
    return comb(n,k) if k <= n else 0

def product(a,b,mod):
    return [[sum(x*y for x,y in zip(row,column))%mod for column in zip(*b)] for row in a]

def inverse(a,mod):
    size=len(a)
    rows=[[x%mod for x in row]+[int(i==j) for j in range(size)] for i,row in enumerate(a)]
    for column in range(size):
        pivot=next(i for i in range(column,size) if rows[i][column]%2)
        rows[column],rows[pivot]=rows[pivot],rows[column]
        unit=pow(rows[column][column],-1,mod)
        rows[column]=[(unit*x)%mod for x in rows[column]]
        for i in range(size):
            if i!=column:
                factor=rows[i][column]
                rows[i]=[(x-factor*y)%mod for x,y in zip(rows[i],rows[column])]
    return [row[size:] for row in rows]

def difference(a,b,mod):
    return [(i,j,(a[i][j]-b[i][j])%mod) for i in range(len(a)) for j in range(len(a[0])) if (a[i][j]-b[i][j])%mod]

def audit(b,L):
    n=4002*b;mod=2**L;m=4*(L-1);d=min(m,b)
    lam=[1,-n]
    for s in range(1,m+5):
        lam.append((s-n)*lam[-1]+(s*n-s*(s-1)//2)*lam[-2])
    cs=[1]
    for s in range(1,m+1):
        cs.append(-sum(choose(s,r)*lam[r]*cs[s-r] for r in range(1,s+1)))
    P=[[choose(i,j)%mod for j in range(b)] for i in range(b)]
    U=[[choose(n,j-i)%mod for j in range(b)] for i in range(b)]
    T=[[choose(n+i,j)%mod for j in range(b)] for i in range(b)]
    Hi=[[cs[i-j]*choose(i,j)%mod if i>=j else 0 for j in range(b)] for i in range(b)]
    H=[[lam[i-j]*choose(i,j)%mod if i>=j else 0 for j in range(b)] for i in range(b)]
    Ui=inverse(U,mod);Pi=inverse(P,mod)
    bulk=product(product(product(Ui,Hi,mod),Ui,mod),Pi,mod)
    failures=[]
    def check(name,diffs):
        if diffs: failures.append({'identity':name,'nonzero_count':len(diffs),'first':diffs[:5]})
    check('T=P U',difference(T,product(P,U,mod),mod))
    check('H Hinv=I',difference(product(H,Hi,mod),[[int(i==j) for j in range(b)] for i in range(b)],mod))

    selected_i=sorted({0,1,b//2,b-1})
    profiles=[[0]*len(selected_i) for _ in range(b)]
    for j in range(b):
      B=b-1-j
      for index,i in enumerate(selected_i):
        total=0
        for s in range(m+1):
          for q in range(i+1):
            weight=(-1)**s*cs[s]*choose(n+q-1,q)*choose(s+i-q,s)
            for p in range(s+i-q+1):
              C=choose(2*n+B+s,B+s-q-p)-sum(
                  choose(n+B+v-1,B+v-p)*choose(n+s-v,s-q-v)
                  for v in range(1,max(s-q,0)+1))
              total+=weight*choose(j,s+i-q-p)*choose(n+p-1,p)*C
        profiles[j][index]=((-1 if (j-i)%2 else 1)*total)%mod
    check('bulk profile (3.3)',difference(profiles,[[bulk[j][i] for i in selected_i] for j in range(b)],mod))

    ext_labels=[0,1,3]
    direct_B=[[choose(-n,b+a-r)%mod for a in ext_labels] for r in range(b)]
    direct_M=product(product(Ui,Hi,mod),direct_B,mod)
    profiles_M=[[0]*len(ext_labels) for _ in range(b)]
    for j in range(b):
      B=b-1-j
      for index,a in enumerate(ext_labels):
        total=0
        for s in range(m+1):
          for p in range(s+1):
            D=choose(2*n+B+a+s,B+a+s+1-p)-sum(
                choose(n+B+v-1,B+v-p)*choose(n+a+s-v,a+s+1-v)
                for v in range(1,a+s+2))
            total+=(-1)**s*cs[s]*choose(j,s-p)*choose(n+p-1,p)*D
        profiles_M[j][index]=((-1)**(b+a-j)*total)%mod
    check('exterior profile (3.5)',difference(profiles_M,direct_M,mod))

    # Build the original finite operator from its full source convolution. It
    # includes every s needed at this precision, even those crossing b.
    def source_col(column):
        return [sum(choose(n,column-r)*sum(
                    lam[s]*choose(r+s,s)*choose(n+i,r+s)
                    for s in range(m+1)) for r in range(column+1))%mod for i in range(b)]
    direct_A=[list(row) for row in zip(*(source_col(j) for j in range(b)))]
    Ainv=inverse(direct_A,mod)
    extT=[[choose(n+i,b+r)%mod for r in range(m)] for i in range(b)]
    K=[[lam[d+r-t]*choose(b+r,d+r-t)%mod if 0<=d+r-t<=m else 0 for t in range(d)] for r in range(m)]
    tailH=[row[:] for row in H]
    TH=product(T,tailH,mod)
    extK=product(extT,K,mod)
    for i in range(b):
        for t in range(d): TH[i][b-d+t]=(TH[i][b-d+t]+extK[i][t])%mod
    check('complete factorization (2.5)',difference(direct_A,product(TH,U,mod),mod))

    F=[[(-sum(choose(-n,b+q-j)*choose(n,v-q) for q in range(v+1)))%mod for v in range(m)] for j in range(b)]
    Hif=product(Hi,F,mod)
    S=product(Hif[b-d:],K,mod)
    for i in range(d):S[i][i]=(S[i][i]+1)%mod
    Sinv=inverse(S,mod)
    correction=product(product(Hif,K,mod),Sinv,mod)
    for i in range(b):
        for j in range(b):
            Hi[i][j]=(Hi[i][j]-sum(correction[i][t]*tail for t,tail in enumerate([cs[b-d+t-j]*choose(b-d+t,j)%mod if b-d+t>=j else 0 for t in range(d)])))%mod
    formula_Ainv=product(product(product(Ui,Hi,mod),Ui,mod),Pi,mod)
    check('full finite inverse (2.8)',difference(Ainv,formula_Ainv,mod))

    # Direct source solutions versus (4.4), including the contact-side return F.
    for t in (0,1,2):
        solve=product(Ainv,[[x] for x in source_col(b+t)],mod)
        max_v=t+m
        ext_all=[[choose(n+i,b+v)%mod for v in range(max_v+1)] for i in range(b)]
        Y=product(Ainv,ext_all,mod)
        estimate=[]
        for j in range(b):
            Fj=-sum(choose(-n,b+q-j)*choose(n,t-q) for q in range(t+1))
            estimate.append([(Fj+sum(choose(n,t-r)*sum(lam[s]*choose(b+r+s,s)*Y[j][r+s] for s in range(m+1)) for r in range(t+1)))%mod])
        check('complete source response (4.4), t='+str(t),difference(solve,estimate,mod))
    result={'b':b,'n':n,'L':L,'modulus':mod,'m':m,'tested_head_indices':selected_i,
            'tested_exterior_labels':ext_labels,'failures':failures,
            'scope':'auxiliary finite identity audit; not original b=9^(18+32u), not growth/valuation proof'}
    choose.cache_clear()
    return result

if __name__=='__main__':
    start=time.monotonic()
    cases=[audit(b,L) for b,L in ((5,3),(7,3),(9,3),(5,4),(7,4),(9,4))]
    report={'personally_authored':True,'network_and_key_reads_denied':True,
            'scope':'Independent bounded refutation/verification of finite formulas only.',
            'elapsed_seconds':round(time.monotonic()-start,3),'cases':cases,
            'all_passed':all(not x['failures'] for x in cases)}
    out=ROOT/'finite_binary_profile_audit_certificate.json'
    out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'all_passed':report['all_passed'],'cases':len(cases),'seconds':report['elapsed_seconds'],
                      'failures':[(x['b'],x['L'],x['failures']) for x in cases if x['failures']]}))
