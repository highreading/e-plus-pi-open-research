"""Personally authored audit of the new polynomial impulse kernels.

Every finite source row is retained. Auxiliary recurrence outputs only;
neither contact-inverted norms nor original relative defects are computed.
"""
from pathlib import Path
from math import comb, factorial
import hashlib, json, resource
from odd29_nilpotent_memory_coordinator import product
resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
ROOT = Path(__file__).resolve().parent
p = 29
K = 2
mod = p**K
inv2 = pow(2, -1, mod)

def add(a, b, scale=1):
    r = [0]*max(len(a), len(b))
    for i,x in enumerate(a): r[i] += x
    for i,x in enumerate(b): r[i] += scale*x
    return [x % mod for x in r]
def mul(a,b):
    r = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j] = (r[i+j]+x*y)%mod
    return r
def shift(a,c):
    r=[0]*len(a)
    for i,x in enumerate(a):
        for j in range(i+1): r[j]=(r[j]+x*comb(i,j)*pow(c,i-j,mod))%mod
    return r
def value(a,j):
    r=0
    for x in reversed(a): r=(r*j+x)%mod
    return r
def impulse_polynomials(n, count):
    # Polynomials in the final index j, using the exact accepted recurrence.
    alpha=[2*n-1,2]
    beta=[((n-1)*(n-4)*inv2)%mod, ((4*n-7)*inv2)%mod, (3*inv2)%mod]
    # gamma(j-1)=(n+j-1)(n+j-2)(2-j)/2.
    gamma=mul(mul([n-1,1],[n-2,1]),[2,-1])
    gamma=[x*inv2%mod for x in gamma]
    q=[[1]]
    for d in range(1,count):
        r=mul(alpha,shift(q[d-1],-1))
        if d>=2:r=add(r,mul(beta,shift(q[d-2],-2)),-1)
        if d>=3:r=add(r,mul(gamma,shift(q[d-3],-3)),-1)
        assert all(x==0 for x in r[d+1:])
        q.append(r[:d+1])
    return q
def phi_coeff(a,limit):
    return [sum(comb(a,t)*comb(a-t,s-2*t)*(-1)**(s-2*t)*pow(inv2,t,mod)
                for t in range(max(0,s-a),(s//2)+1) if s-t<=a)%mod
            for s in range(limit+1)]
def binom(a,b):return comb(a,b)%mod if 0<=b<=a else 0
def one(n,b):
    limit=min(2*n+2,29*K-1)
    coeff=phi_coeff(n+1,limit)
    H=[0]*b; Hg=[0]*b
    for i in range(b):
        falling=1
        for s,a in enumerate(coeff):
            if s:falling=falling*(n+i-s+1)%mod
            H[i]=(H[i]+a*falling*binom(2*n+i-s+1,b))%mod
            # Independent coefficient of R_s(z(1+X)) from its rational poles.
            rs=sum(binom(n,s-k)*binom(i,k) for k in range(min(s,i)+1))%mod
            Hg[i]=(Hg[i]+a*(factorial(s)%mod)*rs*binom(2*n+i-s+1,b))%mod
    assert H==Hg
    q=impulse_polynomials(n,58*K+1)
    tau=[0]*b
    for i in range(1,b-1):
        tau[i+1]=((2*n+2*i+1)*tau[i]
                  -(n+i)*(n+3*i-1)*inv2*tau[i-1]
                  -((n+i)*(n+i-1)*(1-i)*inv2*tau[i-2] if i>=2 else 0)+H[i])%mod
    regen=[]
    for j in range(b):
        regen.append(sum(value(q[j-l-1],j)*H[l]
                         for l in range(max(1,j-(58*K+1)),j))%mod)
    assert regen==tau
    # Compare polynomial impulse weights to independently multiplied matrices.
    checks=0
    for j in (7,32,117,201):
        for d in (0,1,2,3,28,57,58,115,116):
            if d<=j-2:
                assert value(q[d],j)==product(n,j-d,d,mod)[0][0]
                checks+=1
    return {'n':n,'b':b,'precision':K,'source_coefficient_checks':b,
            'complete_particular_output_checks':b,'impulse_product_checks':checks,
            'nonzero_source_rows':sum(bool(H[i]) for i in range(1,b-1)),
            'nonzero_particular_entries':sum(bool(x) for x in tau),
            'source_rows_end_at':b-2,'last_state_index':b-1}
if __name__=='__main__':
    cases=[one(29,57),one(203,203)]
    sharp=[]
    for n in (29,203,191110):
        for k in range(1,7):
            for phase in range(29):
                assert product(n,phase,58*k+1,p**k)==[[0]*3 for _ in range(3)]
                sharp.append((n,k,phase))
    out={'status':'PASS','scope':'Auxiliary complete source/particular rational-kernel identity and original-coefficient uniform propagation audit; no Gram or relative defect',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'cases':cases,'all_phase_sharp_propagation_checks':len(sharp),
         'sharp_bound':'58K+1','aligned_initial_phase_bound':'58K',
         'original_norm_pair_computed':False}
    (ROOT/'recurrence_kernel_audit_receipt.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out),flush=True)
