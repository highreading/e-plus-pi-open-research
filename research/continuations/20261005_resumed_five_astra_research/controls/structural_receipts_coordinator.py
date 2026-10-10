"""Personally authored, bounded arithmetic. No network or credential access.

The binary calculation is a LOWER-BOUND graph, not an inverse evaluation.
Endpoint coefficients are allowed at their weakest integral valuation.
"""
from pathlib import Path
from math import comb
import hashlib, heapq, json

ROOT=Path(__file__).resolve().parent

def save(name,data):
    data['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (ROOT/name).write_text(json.dumps(data,indent=2)+'\n')
    print(name, data.get('status'),flush=True)

def vp(a,p):
    if a==0:return 10**9
    a=abs(a);v=0
    while a%p==0:a//=p;v+=1
    return v

def factorial_v(n,p):
    out=0
    while n:n//=p;out+=n
    return out

def lucas3(n,k):
    if k<0 or k>n:return 0
    out=1
    while n or k:
        a,b=n%3,k%3
        if b>a:return 0
        out=out*comb(a,b)%3;n//=3;k//=3
    return out

def signed_power(n,k):
    return lucas3(n,k)*(1 if (n-k)%2==0 else -1)%3

def inverse3(M):
    size=len(M)
    A=[list(M[i])+[int(i==j) for j in range(size)] for i in range(size)]
    for k in range(size):
        pivot=next(i for i in range(k,size) if A[i][k]%3)
        A[k],A[pivot]=A[pivot],A[k]
        unit=pow(A[k][k],-1,3)
        A[k]=[(x*unit)%3 for x in A[k]]
        for i in range(size):
            if i!=k:
                c=A[i][k]
                A[i]=[(x-c*y)%3 for x,y in zip(A[i],A[k])]
    assert all(A[i][j]==int(i==j) for i in range(size) for j in range(size))
    return [row[size:] for row in A]

def low_isotropy():
    H,D,kappa,nu=2187,18,6,8;r=(H-1)//2
    L=[[signed_power(H-D+a+b,r) for b in range(D)] for a in range(D)]
    Linv=inverse3(L)
    assert all(L[a][b]==0 for a in range(D) for b in range(D) if a+b>=D)
    assert all(L[a][D-1-a]==1 for a in range(D))
    assert all(Linv[a][b]==0 for a in range(D) for b in range(D) if a+b<D-1)
    vec=[]
    for b in range(kappa+1):
        for i in range(nu):
            v=[signed_power(H-kappa+u+b,r-i) for u in range(D)]
            assert all(x==0 for x in v[kappa:])
            vec.append({'b':b,'i':i,'vector':v})
    pairings=0
    for v in vec:
        for w in vec:
            pair=sum(v['vector'][a]*Linv[a][b]*w['vector'][b] for a in range(D) for b in range(D))%3
            assert pair==0;pairings+=1
    save('low_isotropy_certificate.json',{'status':'PASS','scope':'Auxiliary finite LOW algebra only; not an original producer or relative determinant theorem',
         'H':H,'D':D,'kappa':kappa,'nu':nu,'L':L,'inverse':Linv,'vectors':vec,'zero_pairings':pairings})

def normal29_constants():
    p=29;values=[1]
    for r in range(24):values.append(values[-1]*(5+r)%p)
    norm=sum(x*x for x in values)%p;tail=(1+16*norm)%p
    B=410910916;U=2001*B+3;V=2000*B+2
    F=factorial_v(B,p);E=factorial_v(U,p)-factorial_v(V,p)
    assert (norm,tail,F,E,2*E-F)==(8,13,14675386,14675390,14675394)
    floors=[];power=p
    while power<=max(U,V):
        floors.append({'power':power,'B_floor':B//power,'U_floor':U//power,'V_floor':V//power})
        power*=p
    save('normal29_constants_certificate.json',{'status':'PASS','scope':'Fixed arithmetic only; reachability and valuation of actual projected lift require symbolic proof',
         'p':p,'rising_values':values,'normal_norm_mod29':norm,'partial_tail_unit_mod29':tail,
         'B':B,'U':U,'V':V,'F_B':F,'E_B':E,'2E_B_minus_F_B':2*E-F,'floors':floors})

def binary_screen():
    precision=139;D=4*precision-1;maxs=4*(precision-1);mod=1<<precision
    h=-95;n=-190
    # q(z)=1-2z+2z^2-z^3+z^4/4, q*phi'=h*q'*phi.
    qdp=[0,-2,4,-6,6]
    phi=[1]
    for t in range(maxs):
        value=0
        for i in range(1,min(4,t+1)+1):
            b1=comb(t,i-1);b2=comb(t,i) if i<=t else 0
            value+=qdp[i]*(h*b1-b2)*phi[t-i+1]
        phi.append(value)
    # Independent expansion in powers of 2U, only orders r<precision.
    direct=[0]*(maxs+1);direct[0]=1
    power=[0]*(maxs+1);power[0]=1
    binom_h=1
    for r in range(1,precision):
        nxt=[0]*(maxs+1)
        for s in range(r,min(4*r,maxs)+1):
            nxt[s]=sum(comb(s,i)*qdp[i]*power[s-i] for i in range(1,min(4,s)+1))%mod
        power=nxt
        binom_h=binom_h*(h-r+1)//r
        for s in range(r,min(4*r,maxs)+1):direct[s]=(direct[s]+binom_h*power[s])%mod
    assert all(phi[s]%mod==direct[s] for s in range(maxs+1))
    symbol=[10**9]+[vp(phi[s],2) for s in range(1,maxs+1)]
    for s in range(1,maxs+1):
        assert symbol[s]>=factorial_v(s,2)-2*(s//4)
        assert symbol[s]>=(s+3)//4
    # Conservative complete force bounds. For i>=190, all ell<190 vanish.
    force=[]
    low_residue=[2,9,51,57,12,36,48,16]
    for i in range(D+1):
        if i<8:w=vp(low_residue[i],2)
        elif i<190:w=factorial_v(i//2,2)
        else:
            w=min(vp(comb(i,ell),2)+factorial_v(i-190,2)-factorial_v(ell-190,2)
                  +factorial_v(94+(ell+1)//2,2)-factorial_v(94,2)
                  for ell in range(190,i+1))
        assert i<=4*w+3
        force.append(w)
    # Complete endpoint remainder has output e<s and integral coefficients.
    # Allow EVERY such edge from EVERY degree; this only lowers path cost.
    endpoint_cost=[10**9]*(D+1);best_s=[None]*(D+1)
    current=10**9;current_s=None
    for e in range(D,-1,-1):
        s=e+1
        if s<=maxs and symbol[s]<current:current=symbol[s];current_s=s
        endpoint_cost[e]=current;best_s[e]=current_s
    dist=[min(w,precision) for w in force]
    predecessor=[{'kind':'force','degree':i,'cost':w} if w<precision else None for i,w in enumerate(force)]
    heap=[(v,i) for i,v in enumerate(dist) if v<precision];heapq.heapify(heap)
    visited=set();bulk_edges=0;endpoint_edges=0
    while heap:
        cost,d=heapq.heappop(heap)
        if cost!=dist[d] or d in visited:continue
        visited.add(d)
        # Every endpoint output is over-allowed, with the least symbol depth.
        for e in range(min(maxs,D+1)):
            c=endpoint_cost[e]
            if cost+c<dist[e]:
                dist[e]=cost+c;predecessor[e]={'kind':'endpoint','from':d,'s':best_s[e],'edge_cost':c}
                heapq.heappush(heap,(dist[e],e))
            if cost+c<precision:endpoint_edges+=1
        for s in range(1,min(maxs,D-d)+1):
            e=d+s
            if d<190<=e:continue
            coefficient=comb(189-d,s) if d<190 else comb(e-190,s)
            c=symbol[s]+vp(coefficient,2)
            if cost+c<dist[e]:
                dist[e]=cost+c;predecessor[e]={'kind':'bulk','from':d,'s':s,'edge_cost':c,'binomial_depth':vp(coefficient,2)}
                heapq.heappush(heap,(dist[e],e))
            if cost+c<precision:bulk_edges+=1
    assert dist[380]==precision
    # Cross-check telescoping in bounded positive-sector bulk chains.
    chains=[]
    for d in (190,191,192,200,220,250):
        for shifts in ((1,2,3,4),(4,4,4,4),(7,11,13),(19,23,29)):
            at=d;val=0
            for s in shifts:
                val+=vp(comb(at+s-190,s),2);at+=s
            quotient=factorial_v(at-190,2)-factorial_v(d-190,2)-sum(factorial_v(s,2) for s in shifts)
            assert val==quotient
            chains.append({'start':d,'shifts':list(shifts),'end':at,'edge_sum':val,'factorial_quotient':quotient})
    save('binary139_path_screen_certificate.json',{'status':'PASS','scope':'Conservative coefficient-path lower bound at negative continuation only, conditional on complete force/contact formulas; no inverse, nonzero bit or all-depth local factor was evaluated',
         'precision':precision,'degree_cutoff':D,'max_symbol_degree':maxs,'h':h,'n':n,'target':380,
         'target_certified_cost_at_least':dist[380],'target_paths_below_precision':[],
         'visited_degrees':sorted(visited),'bulk_edges_below_precision':bulk_edges,'endpoint_edges_below_precision':endpoint_edges,
         'complete_symbol_recurrence_vs_truncated_power_checks':maxs+1,
         'symbol_valuations':symbol[1:],'forcing_lower_bounds':force,'distances_capped':dist,
         'predecessors':predecessor,'bulk_factorial_crosschecks':chains,
         'discarded_state_reason':'Force indices above4p-1 and contact orders>=p vanish at precision p by the accepted whole Newton filtration; endpoint coefficients are integral and only reduce degree relative to d+s. Any path reaching cost p cannot decrease cost later.'})

if __name__=='__main__':
    low_isotropy();normal29_constants();binary_screen()
