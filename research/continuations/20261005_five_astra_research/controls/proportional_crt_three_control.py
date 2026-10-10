"""Coordinator original-coefficient local check for the same CRT n4482 center."""
import json,math,time,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent;started=time.monotonic()
p=3;n=4482;b=9;mod=729;cutoff=10
def F(k):
    z=0
    while k:k//=p;z+=k
    return z
def vp(k):
    if not k:return None
    z=0
    while k%p==0:k//=p;z+=1
    return z
ds=[]
for s in range(cutoff):
    fact=math.factorial(s)
    value=sum(((-1)**s)*(fact//(2**j))*math.comb(n,s-j)*math.comb(s-j,j)
              for j in range(s//2+1))
    ds.append(value%mod)
assert vp(n)+F(cutoff-1)>=6
N=[[sum(ds[s]*math.comb(n+i,s)*math.comb(n+i-s,j)
         for s in range(cutoff))%mod for j in range(b)] for i in range(b)]
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
tailend=next(t for t in range(b,b+50) if F(t)>=6)
assert tailend==15
rho=[sum(ds[s]*math.comb(n+i,s)*sum(math.factorial(t)*math.comb(2*n+i-s,t)
        for t in range(b,tailend)) for s in range(cutoff))%mod for i in range(b)]
previous=0;current=1;near={}
for r in range(n):
    numerator=2*(n-r)*current+2*(2*n-r+1)*previous
    nxt,rem=divmod(numerator,r+1);assert rem==0
    previous,current=current,nxt
    if r+1>=n-b+1:near[r+1]=current%mod
forcing=[];rising=1
for i in range(b):
    if i:rising=rising*(n+i)%mod
    forcing.append(rising*sum(math.comb(i,t)*near[n-t] for t in range(i+1))%mod)
def reconstruct(solution):
    theta=[sum((-1)**r*math.comb(n+r-1,r)*solution[j+r]
               for r in range(b-j))%mod for j in range(b)]
    return [math.comb(n+2,j)*((j*theta[j-1] if j else 0)-(theta[j] if j<b else 0))%mod
            for j in range(b+1)]
Z=reconstruct(solve(N,forcing));V=reconstruct(solve(N,rho))
V[b]=(V[b]+math.factorial(b)*math.comb(n+2,b))%mod
D=sum(x*x for x in Z)%mod;C=sum(x*y for x,y in zip(Z,V))%mod
beta=vp(n)+F(b)-2
assert beta==5 and vp(D)==1 and vp(C)==beta
assert [v//3**beta%3 for v in rho]==[2,1,1,2,1,1,2,1,1]
assert [v%3 for v in Z]==[1,1,1]+[0]*(b-2)
assert [v//3**beta%3 for v in V]==[1]+[0]*(b-1)+[1]
assert C//3**beta%3==1 and D%9==6
Fn=F(n);vA=4*Fn+vp(D);vH=2*Fn+vp(C)
upper=2*n+b-1;lg=0
while upper>=3:upper//=3;lg+=1
logdepth=Fn-lg;assert logdepth==2231 and logdepth>=6
report={'n':n,'b':b,'prime':3,'precision':6,'coefficient_cutoff':cutoff,
 'factorial_tail_end_exclusive':tailend,'complete_hF_depth_lower_bound':logdepth,
 'contact_matrix_mod729':N,'forcing_mod729':forcing,'whole_residual_mod729':rho,
 'residual_divided_3beta_mod3':[x//3**beta%3 for x in rho],
 'Z_mod3':[x%3 for x in Z],'V_divided_3beta_mod3':[x//3**beta%3 for x in V],
 'norm_mod9':D%9,'norm_depth':vp(D),'mixed_depth':vp(C),
 'mixed_divided_3beta_mod3':C//3**beta%3,'beta':beta,'n_factorial_depth':Fn,
 'actual_q_depth':vA-min(vA,vH),'actual_final_gcd_depth':min(vA,vH),
 'finite_only':True,'seconds':round(time.monotonic()-started,3)}
assert report['actual_q_depth']==4474 and report['actual_final_gcd_depth']==4483
(OUT/'proportional_crt_three_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if not isinstance(v,list)}))
