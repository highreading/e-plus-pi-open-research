"""Exact interval enumeration of all integral jets compatible with an omission disk.

All operations round outwards on a fixed rational grid. Each pruning decision
is a necessary Schur interpolation inequality, never a numerical heuristic.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import factorial
import argparse,json
SESSION=Path('work/session_20261002_codex_continuation')
src=json.loads((SESSION/'main/SECOND_JET_RADIUS_CERTIFICATE.json').read_text())
GRID=10**40
def rd(x):
    a=x[0]*GRID;b=x[1]*GRID
    return Q(a.numerator//a.denominator,GRID),Q(-((-b.numerator)//b.denominator),GRID)
def pt(v):return Q(v),Q(v)
ZERO=pt(0);ONE=pt(1)
def add(x,y):return rd((x[0]+y[0],x[1]+y[1]))
def neg(x):return -x[1],-x[0]
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    c=[a*b for a in x for b in y];return rd((min(c),max(c)))
def div(x,y):
    assert y[0]>0,('Nonpositive denominator enclosure',y)
    return mul(x,rd((1/y[1],1/y[0])))
def scale(x,k):return mul(x,pt(k))
def read(key):return tuple(Q(v['numerator'],v['denominator']) for v in src[key])
def rec(x):return [{'numerator':v.numerator,'denominator':v.denominator} for v in x]
def smul(c,d,N):
    out=[]
    for k in range(N+1):
        v=ZERO
        for j in range(max(0,k-len(d)+1),min(k+1,len(c))):v=add(v,mul(c[j],d[k-j]))
        out.append(v)
    return out
def sinv(c,N):
    out=[div(ONE,c[0])]
    for k in range(1,N+1):
        v=ZERO
        for j in range(1,min(len(c),k+1)):v=add(v,mul(c[j],out[k-j]))
        out.append(neg(div(v,c[0])))
    return out
def strip(c):
    b=c[0];N=len(c)-2
    den=[sub(ONE,mul(b,b))]+[neg(mul(b,v)) for v in c[1:]]
    return smul(c[1:],sinv(den,N),N)
def coordinate_coefficients(N):
    a=read('a_interval');ell=read('ell_interval')
    S=smul([pt(-1),pt(-1),pt(Q(1,2))],sinv([pt(4),pt(-8),pt(8),pt(-4),pt(1)],N),N)
    r=[ell]
    for k in range(N):
        v=S[k]
        for j in range(k+1):v=add(v,scale(mul(r[j],r[k-j]),Q(1,2)))
        r.append(scale(v,Q(1,k+1)))
    v=[div(ONE,a)]
    for k in range(N):
        z=ZERO
        for j in range(k+1):z=add(z,mul(r[j],v[k-j]))
        v.append(scale(z,Q(1,k+1)))
    return [ZERO]+[scale(v[k],Q(1,k+1)) for k in range(N)]
def compose(xi,jets,N):
    phi=[ZERO]+[pt(Q(j,factorial(k+1))) for k,j in enumerate(jets)]
    phi+= [ZERO]*(N+1-len(phi));out=[ZERO]*(N+1);power=[ONE]+[ZERO]*N
    for k in range(1,N+1):
        power=smul(power,phi,N)
        out=[add(u,mul(xi[k],v)) for u,v in zip(out,power)]
    return out
def ceil(v):return -((-v.numerator)//v.denominator)
def floor(v):return v.numerator//v.denominator
def run(R,N):
    a=read('a_interval');t=read('t_interval');xi=coordinate_coefficients(N)
    s=1/R;front=[{'jets':[],'params':[],'target':scale(t,R)}];ledger=[];counts=[]
    for depth in range(1,N+1):
        nxt=[]
        for node in front:
            jets=node['jets'];target=node['target'];assert -1<target[0]<=target[1]<1
            baseline=compose(xi,jets+[0],depth)
            g=[scale(baseline[k],R**k) for k in range(1,depth+1)]
            for _ in range(depth-1):g=strip(g)
            b0=g[0]
            slope=div(pt(R**depth),scale(a,factorial(depth)))
            for b in node['params']:slope=div(slope,sub(ONE,mul(b,b)))
            bmin=div(sub(target,pt(s)),sub(ONE,scale(target,s)))
            bmax=div(add(target,pt(s)),add(ONE,scale(target,s)))
            jl=ceil(div(sub(bmin,b0),slope)[0]);jh=floor(div(sub(bmax,b0),slope)[1])
            row={'prefix':jets,'depth':depth,'b0':rec(b0),'slope':rec(slope),'target':rec(target),'allowed_parameter_interval':[rec(bmin)[0],rec(bmax)[1]],'candidate_integer_interval':[jl,jh],'children':[]}
            for j in range(jl,jh+1):
                b=add(b0,scale(slope,j))
                child={'jet':j,'parameter':rec(b)}
                if b[0]>1 or b[1]<-1:
                    child['status']='REJECT_COEFFICIENT';row['children'].append(child);continue
                assert -1<b[0]<=b[1]<1,('Boundary unresolved; increase precision',jets,j)
                pd=div(sub(target,b),sub(ONE,mul(b,target)))
                child['signed_pseudodistance']=rec(pd)
                if pd[0]>s or pd[1]<-s:
                    child['status']='REJECT_ENDPOINT';row['children'].append(child);continue
                newtarget=scale(pd,R)
                newtarget=(max(Q(-1),newtarget[0]),min(Q(1),newtarget[1]))
                assert -1<newtarget[0]<=newtarget[1]<1,('Boundary target unresolved',jets,j)
                child['status']='SURVIVES';row['children'].append(child)
                nxt.append({'jets':jets+[j],'params':node['params']+[b],'target':newtarget})
            ledger.append(row)
        front=nxt;counts.append(len(front))
        if not front:break
    return {'status':'PASS_EXACT_INTEGER_JET_OMISSION_REJECTION' if not front else 'SURVIVING_JETS_NO_RADIUS_CLAIM','test_radius':{'numerator':R.numerator,'denominator':R.denominator},'max_order':N,'input_certificate':'SECOND_JET_RADIUS_CERTIFICATE.json','rounding_grid_denominator':GRID,'frontier_counts':counts,'surviving_prefixes':[v['jets'] for v in front],'nodes':ledger,'scope':'Exact necessary-interpolation tree; empty frontier at finite order excludes this and all larger disks'}
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--radius',required=True);parser.add_argument('--order',type=int,required=True);parser.add_argument('--output')
    opt=parser.parse_args();r=run(Q(opt.radius),opt.order)
    if opt.output:Path(opt.output).write_text(json.dumps(r,indent=2)+'\n')
    print(r['status'],'R=',opt.radius,'frontiers=',r['frontier_counts'],'survivors=',r['surviving_prefixes'][:12])
