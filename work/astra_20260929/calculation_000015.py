import json, math
from functools import lru_cache
M=1024
path='work/session_20260927/hp_b1_odd_dyadic_germs_checks.json'
with open(path,encoding='utf-8') as f:
    cert=json.load(f)
assert (cert['precision'],cert['modulus'],cert['outer_R_less_than'],cert['inner_D_r_less_than'])==(10,M,55,20)
def trim(p):
    while len(p)>1 and p[-1]==0: p.pop()
    return p
def add(p,q,mod=None):
    r=[0]*max(len(p),len(q))
    for i,x in enumerate(p): r[i]+=x
    for i,x in enumerate(q): r[i]+=x
    return trim([x%mod for x in r] if mod else r)
def mul(p,q,mod=None):
    r=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        if x:
            for j,y in enumerate(q):
                if y: r[i+j]+=x*y
    return trim([x%mod for x in r] if mod else r)
@lru_cache(None)
def fall(a,t,k):
    if k==0: return (1,)
    return tuple(mul(fall(a,t,k-1),[a-k+1,t]))
@lru_cache(None)
def euler(a):
    out=[0]
    for j in range(20): out=add(out,fall(a,16,j),M)
    return tuple(out)
checks=0
coeff_checks=0
def divide(p,d,sign):
    global checks,coeff_checks
    tw=d&-d
    assert all(x%tw==0 for x in p), 'nonintegral dyadic coefficient'
    checks+=1
    coeff_checks+=len(p)
    inv=pow(d//tw,-1,M)
    return trim([(x//tw*inv*sign)%M for x in p])
results=[]
assert [r['residue_mod8'] for r in cert['rows']]==[1,3,5,7]
for row in cert['rows']:
    a=row['residue_mod8']
    H,K,A,B=[0],[0],[0],[0]
    terms=0
    for c in range(28):
        for b in range(55-2*c):
            R=b+2*c
            s=b+c
            den=2**c*math.factorial(b)*math.factorial(c)
            sign=(-1)**b
            hn=mul(fall(a,8,R),fall(a,8,s))
            kn=mul(add(fall(a+1,8,R),fall(a,8,R)),fall(a+1,8,s))
            hp=divide(hn,den,sign)
            kp=divide(kn,den,sign)
            H=add(H,hp,M)
            K=add(K,kp,M)
            A=add(A,mul(hp,euler(2*a-R),M),M)
            B=add(B,mul(kp,euler(2*a+1-R),M),M)
            terms+=1
    C=add(mul(K,A,M),[-x for x in mul(H,B,M)],M)
    actual=dict(H=H,K=K,A=A,B=B,C=C)
    for key,p in actual.items():
        assert p==row[key], (a,key,p,row[key])
    v=min((x&-x).bit_length()-1 for x in C if x)
    assert v==row['v2_gauss_C']
    results.append(dict(residue_mod8=a,terms=terms,all_five_arrays_match=True,C=C,v2_gauss_C=v))
print(json.dumps(dict(results=results,exact_dyadic_division_checks=checks,integer_coefficients_checked=coeff_checks,full_polynomials=True,files_written=False),ensure_ascii=False))