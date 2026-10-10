"""Direct defining-coefficient audit of prescribed even centers at 2."""
import json,math,resource,time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
def vp_fact(k,p=2):
    value=0
    while k:k//=p;value+=k
    return value
def valuation(k):
    if not k:return None
    return (k&-k).bit_length()-1
records=[]
for n,b in [(324162,81)]:
    started=time.monotonic();depth=16;mod=2**depth;cutoff=64
    # For s>=64, v2(s!)-floor(s/2)>=floor(s/2)-floor(log2 s)-1>=25.
    # Thus every omitted divided coefficient is zero at depth16.
    divided=[]
    for s in range(cutoff):
        fact=math.factorial(s)
        divided.append(sum(((-1)**s)*(fact//(2**j))*math.comb(n,s-j)*math.comb(s-j,j)
            for j in range(s//2+1))%mod)
    N=[[sum(divided[s]*math.comb(n+i,s)*math.comb(n+i-s,j)
            for s in range(cutoff))%mod for j in range(b)] for i in range(b)]
    Fb=vp_fact(b);tailend=next(t for t in range(b,b+2*depth+20) if vp_fact(t)-Fb>=depth)
    residual=[sum(divided[s]*math.comb(n+i,s)*
        sum((math.factorial(t)//math.factorial(b))*math.comb(2*n+i-s,t)
            for t in range(b,tailend)) for s in range(cutoff))%mod for i in range(b)]
    def solve(A,rhs):
        rows=[row.copy()+[rhs[i]] for i,row in enumerate(A)]
        for j in range(b):
            pivot=next(i for i in range(j,b) if rows[i][j]%2)
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
    # Independent multinomial expansion of the ORIGINAL coefficient.
    # A_l/R=sum_{r>=ceil(l/2)} 2^(r-l) h!^2 /
    # [(2r-l)! (h-r)! (h-r+l)!]. Multiply by D_l before summing.
    # For l=2j (resp.2j+1), t=r-ceil(l/2) terms have depth
    # >=v2((h)_j)+v2(t!) (resp.v2((h)_(j+1))+v2(t!)).
    # This follows by cancelling D_l and using (x)_t=t!*binom(x,t).
    # Consequently t>=64 is zero at depth16, uniformly in l<=80.
    h=n//2;vR=h+valuation(math.comb(n,h))
    pref=[1]*(n+b+1)
    for t in range(1,n+b+1):
        pref[t]=pref[t-1]*(t if t%2 else 1)%mod
    units=[1]*(n+b+1)
    for t in range(1,n+b+1):units[t]=units[t//2]*pref[t]%mod
    Ddepth=[0]*b;Dunit=[1]*b
    for l in range(1,b):
        v=valuation(n+l);Ddepth[l]=Ddepth[l-1]+v
        Dunit[l]=Dunit[l-1]*((n+l)//(2**v))%mod
    normalized=[]
    for l in range(b):
        total=0;r0=(l+1)//2
        for r in range(r0,min(h,h+l)+1):
            t=r-r0
            if t>=64:break
            indices=(2*r-l,h-r,h-r+l)
            vv=Ddepth[l]+r-l+2*vp_fact(h)-sum(vp_fact(z) for z in indices)
            assert vv>=0
            if vv>=depth:continue
            unit=Dunit[l]*units[h]*units[h]%mod
            for z in indices:unit=unit*pow(units[z],-1,mod)%mod
            total=(total+(2**vv)*unit)%mod
        normalized.append(total)
    force=[]
    for i in range(b):
        total=0
        for l in range(i+1):
            rising=math.prod(range(n+l+1,n+i+1))%mod
            total=(total+math.comb(i,l)*rising*normalized[l])%mod
        force.append(total)
    ZR=weighted(solve(N,force));Vb=weighted(solve(N,residual));Vb[b]=(Vb[b]+math.comb(n+2,b))%mod
    assert all(v%2==0 for v in ZR) and all(v%4==0 for v in Vb)
    commonmod=2**(depth-2)
    X=[(v//2)%commonmod for v in ZR];Y=[v//4 for v in Vb]
    D=sum(v*v for v in X)%commonmod;C=sum(v*w for v,w in zip(X,Y))%commonmod
    d=valuation(D);c=valuation(C);assert d is not None and c is not None
    vlam=2*vp_fact(n)-n
    qdepth=max(0,vlam+vR-Fb-1+d-c)
    vDb=2*(vR+1)+d;vCb=vR+1+Fb+2+c
    vAb=2*vlam+vDb;vHb=vlam+vCb
    assert qdepth==vAb-min(vAb,vHb)
    hF_lower=n//2+1-2*((2*n+b-1).bit_length()-1)
    assert hF_lower-Fb>=depth
    expected_force=[2,1,3,1,4,4]+[0]*(b-6)
    assert [v%8 for v in force]==expected_force
    expected_z=[0]*(b+1);expected_z[0]=expected_z[64]=2
    assert [v%4 for v in ZR]==expected_z
    assert D%4==2 and d==1
    records.append({'n':n,'b':b,'precision':depth,'common_contraction_precision':depth-2,
      'divided_coefficient_cutoff':cutoff,'factorial_tail_end_exclusive':tailend,
      'R_depth':vR,'lambda_depth':vlam,'b_factorial_depth':Fb,
      'contact_matrix_modulus':N,'forcing_divided_R_modulus':force,
      'complete_residual_divided_bfactorial_modulus':residual,
      'weighted_P_divided_R_modulus':ZR,'weighted_Q_divided_bfactorial_modulus':Vb,
      'normalized_X_modulus':X,'normalized_Y_modulus':Y,
      'X_common_depth':min(valuation(v) for v in X if v),
      'Y_common_depth':min(valuation(v) for v in Y if v),
      'norm_modulus':D,'norm_depth':d,'norm_leading_mod4':D//(2**d)%4,
      'mixed_modulus':C,'mixed_depth':c,'mixed_leading_mod4':C//(2**c)%4,
      'complete_log_forcing_divided_bfactorial_depth_lower_bound':hF_lower-Fb,
      'complete_log_forcing_zero_at_requested_precision_proved':True,
      'actual_q_depth_from_exact_local_identity':qdepth,'actual_final_gcd_depth':min(vAb,vHb),
      'actual_Gram_norm_depth':vAb,'actual_Gram_cross_depth':vHb,
      'finite_only':True,'seconds':round(time.monotonic()-started,3)})
(OUT/'proportional_even_four_control.json').write_text(json.dumps({'status':'prescribed a4 direct multinomial even audit passes','records':records},indent=2)+'\n')
print(json.dumps([{k:v for k,v in rec.items() if 'modulus' not in k} for rec in records],indent=2))
