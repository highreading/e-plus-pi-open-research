"""Parent-authored bounded audit of a NEW precision-local producer algorithm.

No network, credentials, original huge matrix, or externally supplied code.
Auxiliary n200/203/206 only, mod3^4/3^5, literal end blocks and full forces.
"""
from pathlib import Path
from functools import lru_cache
from math import comb, factorial
import hashlib
import json
import time

HERE=Path(__file__).resolve().parent
START=time.monotonic()

def vp(x):
    if x==0:return 1000000
    x=abs(x);v=0
    while x%3==0:x//=3;v+=1
    return v

def moments(count,mod=None):
    out=[1,0]
    for r in range(1,count-1):
        z=(4*r+2)*out[-1]+4*out[-2]
        out.append(z if mod is None else z%mod)
    return out[:count]

def direct_solve(matrix,rhs,mod):
    """Unit-pivot modular Gaussian elimination, independent of Pascal locality."""
    n=len(matrix);nr=len(rhs)
    aug=[matrix[i][:]+[v[i]%mod for v in rhs] for i in range(n)]
    swaps=0
    for k in range(n):
        pivot=next((r for r in range(k,n) if aug[r][k]%3),None)
        assert pivot is not None,('nonunit pivot',n,k)
        if pivot!=k:aug[k],aug[pivot]=aug[pivot],aug[k];swaps+=1
        row=aug[k];inv=pow(row[k],-1,mod)
        for j in range(k,n+nr):row[j]=row[j]*inv%mod
        for i in range(k+1,n):
            m=aug[i][k]
            if not m:continue
            old=aug[i]
            for j in range(k+1,n+nr):old[j]=(old[j]-m*row[j])%mod
            old[k]=0
    xs=[[0]*n for _ in rhs]
    for i in range(n-1,-1,-1):
        for r in range(nr):
            xs[r][i]=(aug[i][n+r]-sum(aug[i][j]*xs[r][j] for j in range(i+1,n)))%mod
    return xs,swaps

def leading_block_inverse(v):
    """Actual residue blocks, verified directly over F3 for each digit."""
    out=[0]*len(v)
    n=len(v)
    for a in range(0,n,3):
        remain=min(3,n-a)
        if remain==3:
            # B3 inverse=[[0,2,0],[2,1,1],[0,1,2]] over F3.
            x,y,z=v[a:a+3]
            out[a:a+3]=[(2*y)%3,(2*x+y+z)%3,(y+2*z)%3]
        elif remain==2:
            x,y=v[a:a+2]
            out[a:a+2]=[(2*y)%3,(2*x+2*y)%3]
        else:out[a]=v[a]%3
    return out

def digit_solve(matrix,rhs,M):
    mod=3**M;n=len(matrix)
    x=[0]*n;step=1
    for _ in range(M):
        rem=[(rhs[i]-sum(a*b for a,b in zip(matrix[i],x)))%mod for i in range(n)]
        assert all(v%step==0 for v in rem)
        digit=leading_block_inverse([(v//step)%3 for v in rem])
        x=[a+step*b for a,b in zip(x,digit)]
        step*=3
    assert all((rhs[i]-sum(a*b for a,b in zip(matrix[i],x)))%mod==0 for i in range(n))
    return x

gamma=moments(161)
g=[1,-1,5]
for h in range(3,161):g.append(4*(h-1)*g[-1]+(8*h-7)*g[-2]+4*(h-2)*g[-3])
g_checks=[]
for h in range(9,161):
    exact=sum((-1)**(h-r)*comb(h,r)*gamma[r] for r in range(h+1))
    assert g[h]==exact,('g recurrence',h)
    bound=vp(factorial(h))-vp(factorial(h//2))
    assert vp(g[h])>=bound>=h//6,('valuation',h)
    g_checks.append({'h':h,'depth':vp(g[h]),'factorial_bound':bound})
print(json.dumps({'new_g_indices_checked':len(g_checks),'g_check':'PASS'}),flush=True)

cases=[]
for n in (200,203,206):
    for M in (4,5):
        mod=3**M;target=mod//3;L=12
        R=max(L,6*M)+13*(M-1)+4
        R+=(n-R)%3
        left=n-R
        assert left>=0 and left%3==0 and n%3==2
        terms={}
        for h in range(6*M):
            gh=g[h]%mod
            if not gh:continue
            for p in range(h+1):
                for q in range(h-p+1):
                    c=h-p-q;d=p-q
                    a=gh*(factorial(h)//(factorial(p)*factorial(q)*factorial(c)))*2**c%mod
                    if a:terms.setdefault(d,[]).append((a,h,q))

        @lru_cache(maxsize=None)
        def small_binom(a,h):
            return (comb(a,h) if a>=h else 0)%mod

        def transformed(a,b):
            return sum(v*small_binom(a+q,h) for v,h,q in terms.get(a-b,[]))%mod

        local=[[transformed(a,b) for b in range(left,n)] for a in range(left,n)]
        assert all(local[i][j]==local[j][i] for i in range(R) for j in range(R))
        # Verify actual block inverse rather than assuming a copied coefficient.
        for j in (0,1,2,R-2,R-1):
            e=[int(i==j) for i in range(R)]
            v=leading_block_inverse(e)
            assert all(sum(a*b for a,b in zip(local[i],v))%3==e[i] for i in range(R)),('B inverse',n,M,j)

        # Actual factorial ratios, with zeros justified only after their valuation.
        u=[0]*R
        ratios={}
        for a in range(n-3*M,n):
            facratio=factorial(n-1)//factorial(a)
            ratios[a]=facratio
            u[a-left]=facratio*pow(-2,a,mod)%mod
        uh=[sum((-1)**(b-a)*comb(b,a)*u[a-left] for a in range(max(left,n-3*M),b+1))%mod
            for b in range(left,n)]
        kh=[transformed(a,n) for a in range(left,n)]
        vh=digit_solve(local,uh,M)
        hh=digit_solve(local,kh,M)
        top=max(L,3*M)
        vtop={a:sum((-1)**(b-a)*comb(b,a)*vh[b-left] for b in range(a,n))%mod for a in range(n-top,n)}
        htop={a:((-1)**(n-a-1)*comb(n,a)+sum((-1)**(b-a)*comb(b,a)*hh[b-left] for b in range(a,n)))%mod for a in range(n-top,n)}
        xi_raw=(-sum(a*b for a,b in zip(uh,vh)))%mod
        sigma=sum(u[a-left]*htop[a] for a in range(n-3*M,n))%mod
        chi_raw=(3*n*sigma+6*u[-1])%mod
        assert xi_raw%3==0 and chi_raw%3==0 and (xi_raw//3)%3
        xi=(chi_raw//3)*pow(xi_raw//3,-1,target)%target

        gam=moments(2*n+1,mod)
        matrix=[[comb(a+b,a)*gam[a+b]%mod for b in range(n)] for a in range(n)]
        direct_u=[factorial(n-1)//factorial(a)*pow(-2,a,mod)%mod for a in range(n)]
        direct_k=[comb(n+a,a)*gam[n+a]%mod for a in range(n)]
        (vd,hd),swaps=direct_solve(matrix,[direct_u,direct_k],mod)
        assert all(vtop[a]==vd[a] and htop[a]==hd[a] for a in range(n-top,n)),('local/direct top',n,M)
        xi_direct=(factorial(n-1)**2-sum(a*b for a,b in zip(direct_u,vd)))%mod
        chi_direct=(3*n*sum(a*b for a,b in zip(direct_u,hd))+6*direct_u[-1])%mod
        assert xi_raw==xi_direct and chi_raw==chi_direct,('scalar budget',n,M)
        xi_d=(chi_direct//3)*pow(xi_direct//3,-1,target)%target
        assert xi==xi_d
        bc=-n-66
        qtop=[]
        for a in range(n-L,n):
            common=((bc+6) if a==n-1 else 0)
            if a==n-2:common+=2*bc*pow(n-1,-1,target)
            q=(-(factorial(n-1)//factorial(a))*(3*n*htop[a]+common+xi*vtop[a]))%target
            qd=(-(factorial(n-1)//factorial(a))*(3*n*hd[a]+common+xi_d*vd[a]))%target
            assert q==qd,('complete force',n,M,a)
            qtop.append(q)
        cases.append({'n':n,'M':M,'target_coefficient_precision':M-1,'window':R,
                      'literal_left':left,'literal_right':n-1,'top_inverse_values_compared':2*top,
                      'complete_top_q_compared':L,'xi_mod_target':xi,'q_top':qtop,
                      'independent_full_unit_pivot_row_swaps':swaps,'status':'PASS'})
        print(json.dumps({k:v for k,v in cases[-1].items() if k!='q_top'}),flush=True)

receipt={'status':'PASS','scope':'NEW bounded auxiliary locality implementation, not an original prefix contraction',
         'g_new_checks':g_checks,'cases':cases,'seconds':round(time.monotonic()-START,3),
         'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
             (HERE/'COORDINATOR_PRECISION_LOCAL_PRODUCER_CANDIDATE.md',HERE.parent/'gates/PRECISION_LOCAL_PRODUCER_GATE_20261009.md',Path(__file__))},
         'maximum_full_matrix':206,'maximum_moment':411,'maximum_local_window':86,
         'old_scalar_receipt_or_122_macro_table_rerun':False,
         'initial_implementation_repair':'First run caught one copied B3 inverse coefficient before direct comparisons; corrected by the literal three equations and verified against each local block.',
         'different_external_full_proof_audit_pending':True,'original_huge_matrix_constructed':False}
(HERE/'precision_local_producer_certificate.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'overall':'PASS','cases':len(cases),'seconds':receipt['seconds']}),flush=True)
