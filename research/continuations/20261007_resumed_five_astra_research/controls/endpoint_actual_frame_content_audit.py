"""Parent finite frame calculation, reusing the preserved original n225 producer."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, gcd, lcm
from functools import reduce
import itertools, hashlib, json, time

OUT=Path(__file__).resolve().parent
SOURCE=OUT.parents[1]/'astra_pro5_resume_20261006/controls/complete_endpoint_225_certificate.json'

def rational(x):
    return F(int(x['numerator']),int(x['denominator'])) if isinstance(x,dict) else F(x)

def integer(x):
    x=F(x);assert x.denominator==1;return x.numerator

def det(M):
    a,b,c=M[0];d,e,f=M[1];g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def matvec(M,v):return [sum(a*b for a,b in zip(row,v)) for row in M]
def colsdet(*columns):return det(list(zip(*columns)))
def content(v):return reduce(gcd,(abs(integer(x)) for x in v),0)

def inverse_boundary(v,n):
    s2=v[3];s1=v[2]+s2;s0=v[1]+s1
    return [s0+n*s1+n*(n-1)*s2,s1+2*n*s2,s2]

def smallprimes(N):
    flags=[1]*(N+1);flags[0]=flags[1]=0
    for k in range(2,int(N**.5)+1):
        if flags[k]:
            for j in range(k*k,N+1,k):flags[j]=0
    return [j for j in range(2,N+1) if flags[j]]

def largepart(v,primes):
    v=abs(v);assert v
    for p in primes:
        while v%p==0:v//=p
    return v

def source_crossing_check(p,K):
    mod=p*p;inv2=pow(2,-1,mod);chi=1 if p%4==1 else -1
    eps=1 if p%8 in (1,7) else -1
    alpha=[1,1]
    for s in range(2,K+1):alpha.append((alpha[-1]-inv2*alpha[-2])%mod)
    facts=[1]
    for s in range(1,K+1):facts.append(facts[-1]*s%mod)
    source=[1]
    for s in range(1,K+1):source.append((s*source[-1]+1+2*facts[s-1]*alpha[s-1])%mod)
    wq=((facts[p-1]+1)%mod)//p
    halfq=(pow(2,(p-1)//2,mod)-eps)//p
    predicted_R=(source[p-1]+2*chi*(wq+eps*halfq))%p
    E=1
    for d in range(K-p+1):
        B=(E-2*chi*facts[d])%mod
        assert (source[p+d]-B)%p==0
        actual_R=((source[p+d]-B)%mod)//p
        assert actual_R==predicted_R
        if d<K-p:
            dd=d+1
            a=alpha[dd] if chi==1 else (0 if dd==1 else inv2*alpha[dd-2])
            predicted_R=(dd*predicted_R+B-2*facts[dd-1]*a)%p
            E=(dd*E+1)%mod
    return {'prime':p,'checked_positions':K-p+1,'modulus':mod,
            'chi':chi,'all_first_and_second_level_identities':True}

def main():
    start=time.monotonic(); data=json.loads(SOURCE.read_text());n=int(data['n'])
    assert n==225;N=n+2;m=n+1
    T=[[rational(x) for x in row] for row in data['T']]
    u=[rational(x) for x in data['u']];v=[rational(x) for x in data['v']]
    assert len(u)==len(v)==4 and sum(u)==0 and sum(v)==1
    boundary=[[-1,n,-n*m],[1,-n-1,n*m+2*n],[0,1,-2*n-1],[0,0,1]]
    x=inverse_boundary(u,n);y=inverse_boundary(v,n)
    assert matvec(boundary,x)==u
    assert [a+b for a,b in zip(matvec(boundary,y),[1,0,0,0])]==v
    J=[[integer(factorial(N)*a) for a in row] for row in T]
    columns=[list(c) for c in zip(*J)];Delta=integer(det(J));assert Delta
    Asrc=[integer(a) for a in matvec(J,x)]
    H=[integer(F(a,factorial(n))) for a in Asrc]
    Bsrc=[integer(a) for a in matvec(J,[y[0]-1,y[1],y[2]])]
    En=sum(factorial(n)//factorial(k) for k in range(n+1))
    C=[a-En*b for a,b in zip(Bsrc,H)]
    def replacements(s):
        values=[]
        for i in range(3):
            cols=columns.copy();cols[i]=s;values.append(integer(colsdet(*cols)))
        return values
    a=replacements(Asrc);b=replacements(Bsrc)
    extra=[integer(colsdet(columns[i],Asrc,Bsrc)) for i in range(3)]
    for i in range(3):
        j,k=[z for z in range(3) if z!=i]
        assert Delta*extra[i]==(-1)**i*(a[j]*b[k]-a[k]*b[j])
    done=content([Delta]+a+b);dall=content([Delta]+a+b+extra)
    Q=abs(Delta);assert done%dall==0 and Q%done==0 and Q*dall%(done*done)==0
    U=matvec(boundary,a);V=matvec(boundary,b);V[1]+=Delta
    assert [F(z,Delta) for z in U]==u and [F(z,Delta) for z in V]==v
    clearer=reduce(lcm,[z.denominator for z in u+v],1)
    assert clearer==Q//done==int(data['least_clearer'])
    rowcontents=[gcd(abs(U[i]),abs(V[i]))//done for i in range(4)]
    assert rowcontents==[int(z) for z in data['all_row_contents']]
    primes=smallprimes(N);endpoint=[]
    for label in (0,3):
        if label==3:k1,k2,omitted=columns[0],columns[1],columns[2]
        else:
            k1=[n*z+w for z,w in zip(columns[0],columns[1])]
            k2=[-n*m*z+w for z,w in zip(columns[0],columns[2])]
            omitted=columns[0]
        cross=[k1[1]*k2[2]-k1[2]*k2[1],k1[2]*k2[0]-k1[0]*k2[2],k1[0]*k2[1]-k1[1]*k2[0]]
        h=content(cross);assert h and Q%h==0
        row=[z//h for z in cross]
        projection=sum(z*w for z,w in zip(row,omitted));assert abs(projection)==Q//h
        rh=sum(z*w for z,w in zip(row,H));rc=sum(z*w for z,w in zip(row,C))
        saturated=gcd(abs(rh),abs(rc));full=gcd(saturated,abs(projection))
        assert saturated and full and saturated%full==0
        endpoint.append({'endpoint':label,'kernel_content':str(h),
            'omitted_projection':str(projection),'saturated_content':str(saturated),
            'full_saturated_content':str(full),'discrepancy':str(saturated//full),
            'discrepancy_above227':str(largepart(saturated//full,primes))})
    crossing=[source_crossing_check(p,2*n+2) for p in (229,239)]
    full={'authorship':'Coordinator; no remote code executed',
        'scope':'Reuses one preserved original n225 producer; new fixed-size frame and prime-crossing audit only',
        'input_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'n':n,'Delta':str(Delta),'one_replacements':list(map(str,a+b)),
        'extra_minors':list(map(str,extra)),'d_one':str(done),'d_all':str(dall),
        'quotient_invariant_factors':[str(done//dall),str(Q//done)],
        'first_factor_above227':str(largepart(done//dall,primes)),
        'D8_matches_preserved_actual_clearer':True,'row_contents_match_preserved_values':True,
        'all_three_Pluecker_residuals_zero':True,'endpoint_records':endpoint,
        'source_crossing_checks':crossing,'seconds':round(time.monotonic()-start,4)}
    (OUT/'endpoint_actual_frame_content_certificate.json').write_text(json.dumps(full,indent=2)+'\n')
    receipt={k:full[k] for k in ['authorship','scope','input_sha256','script_sha256','n',
        'first_factor_above227','D8_matches_preserved_actual_clearer',
        'row_contents_match_preserved_values','all_three_Pluecker_residuals_zero',
        'source_crossing_checks','seconds']}
    receipt['endpoint_discrepancies']=[{k:z[k] for k in ['endpoint','discrepancy_above227']} for z in endpoint]
    receipt['invariant_factor_decimal_digits']=[len(z) for z in full['quotient_invariant_factors']]
    receipt['full_certificate_sha256']=hashlib.sha256((OUT/'endpoint_actual_frame_content_certificate.json').read_bytes()).hexdigest()
    (OUT/'endpoint_actual_frame_content_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt))

if __name__=='__main__':main()
