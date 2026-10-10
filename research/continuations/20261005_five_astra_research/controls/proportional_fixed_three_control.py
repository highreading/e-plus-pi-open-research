"""Two requested large-index, small-dimension modular audits, CPU limited."""
import json,math,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
mod=81;p=3

def mulpoly(a,b,L):
    out=[0]*L
    for i,x in enumerate(a):
        for j,y in enumerate(b[:L-i]):out[i+j]=(out[i+j]+x*y)%mod
    return out

def powerpoly(base,k,L):
    out=[1]+[0]*(L-1)
    while k:
        if k&1:out=mulpoly(out,base,L)
        base=mulpoly(base,base,L);k//=2
    return out

def falling(x,r):
    out=1
    for j in range(r):out=out*(x-j)%mod
    return out

def Dmath(x):return sum(falling(x,r) for r in range(9))%mod

def inverse(A):
    size=len(A);rows=[row.copy()+[int(i==j) for j in range(size)] for i,row in enumerate(A)]
    for j in range(size):
        pivot=next(i for i in range(j,size) if rows[i][j]%3)
        rows[j],rows[pivot]=rows[pivot],rows[j];iv=pow(rows[j][j],-1,mod)
        rows[j]=[x*iv%mod for x in rows[j]]
        for i in range(size):
            if i==j:continue
            f=rows[i][j];rows[i]=[(x-f*y)%mod for x,y in zip(rows[i],rows[j])]
    return [row[size:] for row in rows]

def matvec(A,v):return [sum(x*y for x,y in zip(row,v))%mod for row in A]

def central_window(n,b):
    # Exact coefficient recurrence for (1+2t+2t^2)^n; only final b residues kept.
    prev=0;current=1;window={}
    for r in range(n):
        num=2*(n-r)*current+2*(2*n-r+1)*prev
        nxt,rem=divmod(num,r+1);assert rem==0
        prev,current=current,nxt
        if r+1>=n-b+1:window[r+1]=current%mod
    return [window[n-i] for i in range(b)]

def weighted(c,n,b):
    # Exact divided reconstruction. Generalized binomial(-n,r) remains integral.
    transformed=[sum(((-1)**r)*math.comb(n+r-1,r)*c[j+r] for r in range(b-j))%mod for j in range(b)]
    z=[-transformed[0]%mod]+[(j*transformed[j-1]-(transformed[j] if j<b else 0))%mod for j in range(1,b+1)]
    return [math.comb(n+2,j)%mod*z[j]%mod for j in range(b+1)]
records=[]
for a,n,b in ((1,6003,3),(2,18009,9)):
    phi=powerpoly([1,mod-1,pow(2,-1,mod)],n,9)
    N=[[sum(phi[s]*falling(n+i,s)*(math.comb(n+i-s,j)%mod) for s in range(9))%mod for j in range(b)] for i in range(b)]
    assert all(N[i][j]%9==math.comb(i,j)%9 for i in range(b) for j in range(b))
    near=central_window(n,b)
    J=[sum(math.comb(i,l)*near[l] for l in range(i+1))%mod for i in range(b)]
    assert J[0]%3
    f=[falling(n+i,i)*J[i]%mod for i in range(b)]
    inv=inverse(N);y=matvec(inv,f)
    he=[sum(phi[s]*falling(n+i,s)*Dmath(2*n+i-s) for s in range(9))%mod for i in range(b)]
    # hF is zero modulo 81: every factorial index >=n has valuation minus
    # its maximum log_3 denominator strictly greater than four.
    def factorial_v3(k):
        out=0
        while k:k//=3;out+=k
        return out
    max_index=2*n+b-1;logdepth=0;v=max_index
    while v>=3:v//=3;logdepth+=1
    hF_lower=factorial_v3(n)-logdepth
    assert hF_lower>=4
    yQ=matvec(inv,he)
    wz=weighted(y,n,b);wv=weighted(yQ,n,b);wv[0]=(wv[0]+1)%mod
    D=sum(x*x for x in wz)%mod;C=sum(x*y for x,y in zip(wz,wv))%mod
    assert [x%9 for x in y[:3]]==[J[0]%9,0,J[0]%9]
    assert y[-1]%3
    assert D%9==6*(J[0]%9)**2%9
    assert all(x%9==0 for x in wv)
    chi=None
    if C:
        chi=0;q=C
        while q%3==0:chi+=1;q//=3
        assert chi<4
    Fn=factorial_v3(n)
    record={'a':a,'n':n,'b':b,'modulus':81,'N_tilde_mod9':[[v%9 for v in row] for row in N],
      'J_mod81':J,'y_mod81':y,'yQ_mod81':yQ,'weighted_z_mod81':wz,'weighted_v_mod81':wv,
      'D_mod81':D,'C_mod81':C,'chi_if_resolved':chi,'F_n':Fn,
      'actual_q_v3_if_paper_formula_passes':2*Fn+1-chi if chi is not None else None,
      'logarithmic_forcing_v3_lower_bound':hF_lower,
      'all_mod9_predictions_pass':True,'finite_only':True,
      'truncation':'s>=9 and Dmath r>=9 vanish mod81 by factorial valuation; no approximate real arithmetic'}
    records.append(record)
report={'status':'two finite direct defining-coefficient modular audits pass; infinite theorem needs independent proof review','records':records}
(OUT/'proportional_fixed_three_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps([{k:v for k,v in r.items() if k not in ('N_tilde_mod9','J_mod81','y_mod81','yQ_mod81','weighted_z_mod81','weighted_v_mod81')} for r in records],indent=2))
