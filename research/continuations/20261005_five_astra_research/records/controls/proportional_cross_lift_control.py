"""Two prescribed first-lift modular checks; no remote code or network."""
import json,math,resource,time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
records=[]
def vp_fact(k,p=3):
    out=0
    while k:k//=p;out+=k
    return out
for a,n,b,depth in [(2,18009,9,6),(3,54027,27,15)]:
    started=time.monotonic();mod=3**depth;beta=(b+1)//2
    cutoff=next(s for s in range(1,3*depth+10) if vp_fact(s)>=depth)
    def mulpoly(x,y):
        z=[0]*cutoff
        for i,v in enumerate(x):
            for j,w in enumerate(y[:cutoff-i]):z[i+j]=(z[i+j]+v*w)%mod
        return z
    phi=[1]+[0]*(cutoff-1);base=[1,mod-1,pow(2,-1,mod)]+[0]*(cutoff-3)
    exp=n
    while exp:
        if exp&1:phi=mulpoly(phi,base)
        base=mulpoly(base,base);exp//=2
    def falling(k,s):
        v=1
        for j in range(s):v=v*(k-j)%mod
        return v
    def Dmath(k):return sum(falling(k,r) for r in range(cutoff))%mod
    N=[[sum(phi[s]*falling(n+i,s)*math.comb(n+i-s,j) for s in range(cutoff))%mod
        for j in range(b)] for i in range(b)]
    he=[sum(phi[s]*falling(n+i,s)*Dmath(2*n+i-s) for s in range(cutoff))%mod for i in range(b)]
    def solve(A,rhs):
        rows=[row.copy()+[rhs[i]] for i,row in enumerate(A)]
        for j in range(b):
            pivot=next(i for i in range(j,b) if rows[i][j]%3)
            rows[j],rows[pivot]=rows[pivot],rows[j]
            iv=pow(rows[j][j],-1,mod);rows[j]=[v*iv%mod for v in rows[j]]
            for i in range(b):
                if i!=j:
                    f=rows[i][j]
                    if f:rows[i]=[(v-f*w)%mod for v,w in zip(rows[i],rows[j])]
        return [row[b] for row in rows]
    def weighted(y):
        t=[sum((-1)**r*math.comb(n+r-1,r)*y[j+r] for r in range(b-j))%mod for j in range(b)]
        z=[-t[0]%mod]+[(j*t[j-1]-(t[j] if j<b else 0))%mod for j in range(1,b+1)]
        return [math.comb(n+2,j)*z[j]%mod for j in range(b+1)]
    factorials=[math.factorial(j)%mod for j in range(b)]
    x=[sum(math.comb(n,r)*factorials[j+r] for r in range(b-j))%mod for j in range(b)]
    residual=[(he[i]-sum(N[i][j]*x[j] for j in range(b)))%mod for i in range(b)]
    expected_r=[2*(-1)**a*Dmath(i)%3 for i in range(b)]
    actual_r=[v//(3**beta)%3 for v in residual]
    assert all(v%(3**beta)==0 for v in residual) and actual_r==expected_r
    yQ=solve(N,he);V=weighted(yQ);V[0]=(V[0]+1)%mod
    expected_V=[(-1)**a%3 if j in (0,b) else 0 for j in range(b+1)]
    actual_V=[v//(3**beta)%3 for v in V]
    assert all(v%(3**beta)==0 for v in V) and actual_V==expected_V
    previous=0;current=1;near={}
    for r in range(n):
        numerator=2*(n-r)*current+2*(2*n-r+1)*previous
        nxt,rem=divmod(numerator,r+1);assert rem==0
        previous,current=current,nxt
        if r+1>=n-b+1:near[r+1]=current%mod
    J=[sum(math.comb(i,t)*near[n-t] for t in range(i+1))%mod for i in range(b)]
    f=[falling(n+i,i)*J[i]%mod for i in range(b)]
    Z=weighted(solve(N,f));D=sum(v*v for v in Z)%mod;C=sum(v*w for v,w in zip(Z,V))%mod
    assert D%9==6 and C%(3**beta)==0 and C//(3**beta)%3==2*(-1)**a%3
    upper=2*n+b-1;logdepth=0
    while upper>=3:upper//=3;logdepth+=1
    hF_lower=vp_fact(n)-logdepth;assert hF_lower>=depth
    records.append({'a':a,'n':n,'b':b,'precision':depth,'modulus':str(mod),'cutoff':cutoff,
      'complete_logarithmic_forcing_v3_lower_bound':hF_lower,'log_forcing_zero_at_requested_modulus_proved':True,
      'complete_residual_modulus':[str(v) for v in residual],'normalized_residual_mod3':actual_r,
      'normalized_weighted_Q_column_mod3':actual_V,'cross_contraction_modulus':str(C),
      'chi':beta,'norm_modulus':str(D),'norm_v3':1,
      'actual_q_v3_if_paper_formula_passes':2*vp_fact(n)+1-beta,
      'all_first_lift_predictions_pass':True,'finite_only':True,'seconds':round(time.monotonic()-started,3)})
report={'status':'two finite direct defining-coefficient first-lift audits pass','records':records}
(OUT/'proportional_cross_lift_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps([{k:v for k,v in r.items() if k not in ('complete_residual_modulus','normalized_residual_mod3','normalized_weighted_Q_column_mod3')} for r in records],indent=2))
