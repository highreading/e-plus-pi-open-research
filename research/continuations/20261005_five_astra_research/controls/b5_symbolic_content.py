"""Fixed sparse-polynomial content check, coordinator authored, CPU limited."""
import itertools
import json
import math
import resource
from pathlib import Path
from sympy import QQ
from sympy.polys.rings import ring
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
R,n,h,u,v=ring('n,h,u,v',QQ)
half=QQ(1,2)
def state_next(k,state):
    hh,uu,vv=state;t=k+1
    return (-k*hh+k*uu+half*vv,t*(hh-uu+half*vv),t*(k*hh+uu-half*(k+2)*vv))
def falling(k,r):
    z=R.one
    for j in range(r):z*=k-j
    return z
def jets(k,state,limit):
    z=list(state)
    while len(z)<=limit:
        d=len(z)-3
        z.append(-(k+d)*z[d+2]+2*d*z[d+1]+2*(k-d)*z[d])
    return [sum((math.comb(j,a)*falling(k,a)*z[j-a] for a in range(j+1)),R.zero) for j in range(limit+1)]
def divided_jets(k,previous,limit):
    hh,uu,vv=previous
    current=state_next(k-1,previous)
    alpha=hh-uu+half*vv
    beta=(k-1)*hh+uu-half*(k+1)*vv
    eta=[R.zero,alpha,beta,2*current[0]-k*beta]
    while len(eta)<=limit:
        d=len(eta)-3
        eta.append(-(k+d)*eta[d+2]+2*d*eta[d+1]+2*(k-d)*eta[d])
    raw=list(current)
    while len(raw)<=limit:
        d=len(raw)-3
        raw.append(-(k+d)*raw[d+2]+2*d*raw[d+1]+2*(k-d)*raw[d])
    return [R.zero]+[eta[j]+sum((math.comb(j,a)*falling(k-1,a-1)*raw[j-a] for a in range(1,j+1)),R.zero) for j in range(1,limit+1)]
states=[(h,u,v)]
for shift in range(3):states.append(state_next(n+shift,states[-1]))
F=jets(n+1,states[1],5)
G=jets(n+2,states[2],5)
z=divided_jets(n+2,states[1],6)[1:]
z2=divided_jets(n+3,states[2],6)[1:]
def J(vals):return [vals[0]]+[(vals[j+1]-vals[j])/math.factorial(j) for j in range(5)]
high=[J(a) for a in (F,z,G,z2)]
Pjet=jets(n,states[0],4)
Fdiv=divided_jets(n+1,states[0],5)
prow=[R.zero]+[Pjet[j]/math.factorial(j) for j in range(5)]
urow=[R.zero]+[Fdiv[j+1]/math.factorial(j) for j in range(5)]
e=[R.one]+[R.zero]*5
def determinant(rows):
    out=R.zero
    for perm in itertools.permutations(range(len(rows))):
        value=R.one
        for i,j in enumerate(perm):value*=rows[i][j]
        parity=sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
        out+=-value if parity%2 else value
    return out
minors={}
for i in range(6):
    for j in range(i+1,6):
        cols=[a for a in range(6) if a not in (i,j)]
        minors[i,j]=(-1)**(i+j+1)*determinant([[row[a] for a in cols] for row in high])
def contract(row1,row2):
    return sum((value*(row1[i]*row2[j]-row1[j]*row2[i]) for (i,j),value in minors.items()),R.zero)
sig=-contract(e,urow);chi=-contract(e,prow);kap=contract(urow,prow)
seed=[int(sum(c for mon,c in a.items() if mon[0]==mon[2]==mon[3]==0)) for a in (sig,chi,kap)]
assert seed==[76,-276,-56],seed
print(json.dumps({'phase':'determinants','terms':[len(a) for a in (sig,chi,kap)],'seed':seed}),flush=True)
common=sig.gcd(chi).gcd(kap)
quotients=[a.exquo(common) for a in (sig,chi,kap)]
assert all(q*common==a for q,a in zip(quotients,(sig,chi,kap)))
def numerical_content(poly):
    den=math.lcm(*(int(c.denominator) for c in poly.values()))
    content=math.gcd(*(int(c*den) for c in poly.values()))
    return {'denominator':den,'integer_coefficient_content':content}
record={'status':'exact fixed polynomial identities; integral removal requires denominator audit',
    'seed':seed,'terms':[len(a) for a in (sig,chi,kap)],
    'common_factor':str(common.as_expr()),'common_factor_total_degree':max(sum(m) for m in common),
    'coefficient_content':[numerical_content(a) for a in (sig,chi,kap)],
    'quotient_content':[numerical_content(a) for a in quotients],
    'recomposition_verified':True}
(OUT/'b5_symbolic_content_summary.json').write_text(json.dumps(record,indent=2)+'\n')
full={'variables':['n','h','u','v'],'common_factor':[[list(m),str(c)] for m,c in common.items()],
      'quotients':[[[list(m),str(c)] for m,c in a.items()] for a in quotients]}
(OUT/'b5_symbolic_content_polynomials.json').write_text(json.dumps(full)+'\n')
print(json.dumps(record,indent=2),flush=True)
