"""Four requested prime-square values and independent polynomial slopes."""
import json,math,resource
from fractions import Fraction
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
saved=json.loads((OUT/'b5_symbolic_content_polynomials.json').read_text())
terms=[[(m,Fraction(c)) for m,c in row] for row in saved['quotients']]
def evaluate(row,coords,mod,derivative=None):
    value=0
    for mon,c in row:
        powers=list(mon);factor=1
        if derivative is not None:
            factor=powers[derivative]
            if not factor:continue
            powers[derivative]-=1
        value+=factor*int(c.numerator)*pow(int(c.denominator),-1,mod)*math.prod(pow(x,d,mod) for x,d in zip(coords,powers))
    return value*pow(1152,-1,mod)%mod
def advance(n,state,mod):
    h,u,v,A,M=state;t=n+1;iv2=pow(2,-1,mod)
    return ((-n*h+n*u+v*iv2)%mod,t*(h-u+v*iv2)%mod,t*(n*h+u-(n+2)*v*iv2)%mod,
      (t*M+h-u+v*iv2)%mod,(t**3*A+t*(2*n+3)*M+(n*n+3*n+4)*h-(n+3)*u+(n+2)*v)%mod)
p=7;mod=49;state=(1,0,0,1,2);records={}
for n in range(11):
    if n in (2,3,9,10):
        h,u,v,A,M=state;con=[evaluate(row,(n,h,u,v),mod) for row in terms]
        V=(con[0]*A-con[1]*(M+h-u)-con[2])%mod
        records[n]={'n':n,'state_mod49':list(state),'contractions_mod49':con,'V_mod49':V}
    state=advance(n,state,mod)
slopes=[]
for r,tangent in [(2,[0,0,2,1,0]),(3,[5,0,5,5,0])]:
    h,u,v,A,M=records[r]['state_mod49'];coords=(r,h%p,u%p,v%p)
    delta=[(evaluate(row,coords,p,0)+sum(tangent[j]*evaluate(row,coords,p,j+1) for j in range(3)))%p for row in terms]
    con=[c%p for c in records[r]['contractions_mod49']]
    dh,du,dv,dA,dM=tangent;B=(M+h-u)%p
    slope=(delta[0]*A+con[0]*dA-delta[1]*B-con[1]*(dM+dh-du)-delta[2])%p
    beta=records[r]['V_mod49']//p
    diff=(records[r+p]['V_mod49']-records[r]['V_mod49'])%mod
    assert diff%p==0 and diff//p==slope,(r,slope,diff)
    classification='unique simple p-adic root, pending paper expansion audit' if slope else ('valuation exactly one on whole disk, pending paper audit' if beta else 'second-layer unresolved')
    root_t=(-beta*pow(slope,-1,p))%p if slope else None
    slopes.append({'r':r,'beta_mod7':beta,'Lambda_mod7':slope,'derivative_circuit_equals_two_point_slope':True,'root_T_mod7':root_t,
      'root_n_mod49':r+p*root_t if root_t is not None else None,'classification':classification})
report={'prime':p,'rows_checked':4,'rows':[records[n] for n in (2,9,3,10)],'slopes':slopes,
 'status':'finite arithmetic agrees with proposed expansion; analytic extension must still be independently audited'}
(OUT/'b5_root_disk_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
