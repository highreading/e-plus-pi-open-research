"""Coordinator-authored direct checks of two prescribed 23-adic lifts."""
import json,math,resource,time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
def vp_fact(k,p):
    value=0
    while k:k//=p;value+=k
    return value
def valuation(k,p):
    if not k:return None
    v=0
    while k%p==0:k//=p;v+=1
    return v
records=[]
for n,b in [(46023,23),(54027,27)]:
    started=time.monotonic();p=23;depth=3;mod=p**depth
    cutoff=next(s for s in range(1,p*depth+1) if vp_fact(s,p)>=depth)
    def mulpoly(x,y):
        z=[0]*cutoff
        for i,v in enumerate(x):
            if v:
                for j,w in enumerate(y[:cutoff-i]):z[i+j]=(z[i+j]+v*w)%mod
        return z
    phi=[1]+[0]*(cutoff-1);base=[1,mod-1,pow(2,-1,mod)]+[0]*(cutoff-3)
    exponent=n
    while exponent:
        if exponent&1:phi=mulpoly(phi,base)
        base=mulpoly(base,base);exponent//=2
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
            pivot=next(i for i in range(j,b) if rows[i][j]%p)
            rows[j],rows[pivot]=rows[pivot],rows[j]
            inv=pow(rows[j][j],-1,mod);rows[j]=[v*inv%mod for v in rows[j]]
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
    V=weighted(solve(N,he));V[0]=(V[0]+1)%mod
    previous=0;current=1;near={}
    for r in range(n):
        numerator=2*(n-r)*current+2*(2*n-r+1)*previous
        nxt,rem=divmod(numerator,r+1);assert rem==0
        previous,current=current,nxt
        if r+1>=n-b+1:near[r+1]=current%mod
    J=[sum(math.comb(i,t)*near[n-t] for t in range(i+1))%mod for i in range(b)]
    forcing=[falling(n+i,i)*J[i]%mod for i in range(b)]
    Z=weighted(solve(N,forcing));D=sum(v*v for v in Z)%mod;C=sum(v*w for v,w in zip(Z,V))%mod
    logdepth=0;upper=2*n+b-1
    while upper>=p:upper//=p;logdepth+=1
    hF_lower=vp_fact(n,p)-logdepth;assert hF_lower>=depth
    record={'n':n,'b':b,'prime':p,'precision':depth,'modulus':mod,'factorial_cutoff':cutoff,
      'complete_log_forcing_vp_lower_bound':hF_lower,'log_forcing_zero_at_requested_precision_proved':True,
      'J0_modp':J[0]%p,'weighted_P_column_modulus':Z,'weighted_Q_column_modulus':V,
      'complete_residual_modulus':residual,'norm_modulus':D,'cross_modulus':C,
      'cross_depth_if_below_precision':valuation(C,p),'finite_only':True}
    if b==23:
        expected=[0]*(b+1);expected[0]=6877;expected[b]=2645
        assert J[0]%p==6 and D%p==9 and V==expected and C==7406
        record.update({'all_requested_predictions_pass':True,'actual_q_vp_from_finite_local_identity':4180})
    else:
        Fb=vp_fact(b,p);unit=math.factorial(b)//(p**Fb)
        assert C%(p**Fb)==0
        Xi=(C//(p**Fb))*pow(unit,-1,p**(depth-Fb))%(p**(depth-Fb))
        assert J[0]%p==10 and D%p==1 and Xi%p==0
        record.update({'divided_cross_Xi_mod529':Xi,'Xi_div23_mod23':Xi//23,
            'first_layer_predictions_pass':True,'actual_q_vp_if_Xi_depth_one':4908 if Xi//23 else None})
    record['seconds']=round(time.monotonic()-started,3);records.append(record)
report={'status':'direct prescribed finite 23-adic normalization checks complete','records':records}
(OUT/'proportional_twenty_three_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps([{k:v for k,v in r.items() if 'column' not in k and k!='complete_residual_modulus'} for r in records],indent=2))
