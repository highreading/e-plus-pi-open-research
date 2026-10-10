"""Parent-authored selected ORIGINAL inverse coordinates, modulo4.

Uses accepted finite Schur completion; never constructs an original-size
matrix. Large binomial residues use an independently checked odd-factorial
recursion. Finite original values are not infinite-family proofs.
"""
from pathlib import Path
from functools import lru_cache
from math import comb
import hashlib, json, time
from finite_binary_profile_audit import product, inverse
from binary_actual_force_audit import force_head

ROOT=Path(__file__).resolve().parent
MOD=4
PREFIX=[1]
for j in range(1,MOD+1):
    PREFIX.append(PREFIX[-1]*(j if j%2 else 1)%MOD)

@lru_cache(maxsize=60000)
def odd_factorial(n):
    if n<=1:return 1
    return (pow(PREFIX[-1],n//MOD,MOD)*PREFIX[n%MOD]
            *odd_factorial(n//2))%MOD

@lru_cache(maxsize=60000)
def choose4(n,k):
    if k<0:return 0
    if n<0:return (-1 if k%2 else 1)*choose4(k-n-1,k)%MOD
    if k>n:return 0
    exponent=k.bit_count()+(n-k).bit_count()-n.bit_count()
    if exponent>=2:return 0
    return ((1<<exponent)*odd_factorial(n)
            *pow(odd_factorial(k)*odd_factorial(n-k)%MOD,-1,MOD))%MOD

def literal_algorithm_check():
    checks=0
    for n in range(81):
        for k in range(n+3):
            assert choose4(n,k)==(comb(n,k)%4 if k<=n else 0)
            checks+=1
    for n in range(-31,0):
        for k in range(32):
            assert choose4(n,k)==((-1)**k*comb(k-n-1,k))%4
            checks+=1
    return checks

def evaluate(b,positions):
    n=4002*b;h=n//2
    L=2;m=4;d=min(b,m);I=min(b-1,14)
    f,bits,_,_=force_head(h,L+I,I)
    assert min(bits)>=L
    f=[v%MOD for v in f]
    lam=[1,-n%MOD]
    for s in range(1,m):
        lam.append(((s-n)*lam[-1]+(s*n-s*(s-1)//2)*lam[-2])%MOD)
    cs=[1]
    for s in range(1,m+1):
        cs.append(-sum(choose4(s,r)*lam[r]*cs[s-r]
                       for r in range(1,s+1))%MOD)
    K=[[lam[d+r-t]*choose4(b+r,d+r-t)%MOD
        if 0<=d+r-t<=m else 0 for t in range(d)] for r in range(m)]
    def finite_f(j,v):
        return -sum(choose4(-n,b+q-j)*choose4(n,v-q)
                    for q in range(v+1))%MOD
    G=[[sum(cs[s]*choose4(j,s)*finite_f(j-s,v)
            for s in range(m+1) if s<=j)%MOD for v in range(m)]
       for j in range(b-d,b)]
    S=product(G,K,MOD)
    for i in range(d):S[i][i]=(S[i][i]+1)%MOD
    Si=inverse(S,MOD)
    def uncorrected_head(j,i):
        return sum((-1 if (j-i)%2 else 1)*choose4(n+q-1,q)
                   *choose4(j,i-q)*choose4(n+b-j-1,b-j-1-q)
                   for q in range(i+1))%MOD
    Df=[[sum(f[i]*sum(cs[s]*choose4(j,s)*uncorrected_head(j-s,i)
                      for s in range(m+1) if s<=j)
             for i in range(I+1))%MOD] for j in range(b-d,b)]
    zeta=product(Si,Df,MOD)
    beta=product(K,zeta,MOD)
    Um=[[choose4(n,j-i) for j in range(m)] for i in range(m)]
    eta=product(Um,beta,MOD)
    def head_profile(j,i):
        return sum((-1 if (j-i+s)%2 else 1)*cs[s]
                   *choose4(n+r-1,r)*choose4(2*n+r+q-1,q)
                   *choose4(s-r+i-q,s-r)*choose4(j,s-r+i-q)
                   *choose4(2*n+b+s-1-j,b+s-r-q-1-j)
                   for s in range(m+1) for r in range(s+1)
                   for q in range(i+1))%MOD
    def exterior_profile(j,v):
        return sum((-1 if (b+v-j+s)%2 else 1)*cs[s]
                   *choose4(n+r-1,r)*choose4(j,s-r)
                   *choose4(2*n+b+v+s-1-j,b+v+s-r-j)
                   for s in range(m+1) for r in range(s+1))%MOD
    residues={j:(sum(f[i]*head_profile(j,i) for i in range(I+1))
                 +sum(eta[v][0]*exterior_profile(j,v) for v in range(m)))%MOD
              for j in positions}
    return {'b':b,'n':n,'source_head_mod4':f,'lambda_mod4':lam,
            'inverse_symbol_mod4':cs,'Schur_matrix_mod4':S,
            'Schur_inverse_mod4':Si,'actual_tail_mod4':zeta,
            'actual_return_mod4':eta,'selected_contact_residues':residues}

def auxiliary_inverse_check():
    b=17;n=4002*b;h=n//2
    got=evaluate(b,list(range(b)))
    lam=got['lambda_mod4']
    A=[[sum(lam[s]*choose4(n+i,s)*choose4(2*n+i-s,j)
            for s in range(5))%MOD for j in range(b)] for i in range(b)]
    Ai=inverse(A,MOD)
    f,bits,_,_=force_head(h,2+b,b-1)
    want=product(Ai,[[v%4] for v in f],MOD)
    assert all(got['selected_contact_residues'][j]==want[j][0] for j in range(b))
    return {'auxiliary_b':b,'whole_finite_contact_positions':b,
            'all_passed':True,'scope':'Auxiliary verification of the new selected-row algorithm.'}

def main():
    started=time.monotonic()
    binomial_checks=literal_algorithm_check()
    auxiliary=auxiliary_inverse_check()
    cases=[]
    for u in range(5):
        b=9**(18+32*u)
        positions=[0,4,b-4,b-3,b-2,b-1]
        case=evaluate(b,positions)
        N=case['n']+2
        witnesses=[j for j in positions if choose4(N,j)%2
                   and case['selected_contact_residues'][j]==2]
        case.update({'original_u':u,'odd_weight_content_zero_witnesses':witnesses,
                     'content_zero_certified':bool(witnesses),
                     'scope':'Finite original index only. Infinite u not inferred.'})
        cases.append(case)
    out={'personally_authored':True,'network_and_credentials_denied':True,
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'literal_binomial_checks':binomial_checks,'auxiliary_inverse_check':auxiliary,
         'cases':cases,'all_passed':True,
         'elapsed_seconds':round(time.monotonic()-started,4),
         'scope':'Selected original inverse residues and sufficient actual a=0 '
                 'witnesses at u=0..4. No infinite-family or scalar-error theorem.'}
    (ROOT/'binary_actual_contact_mod4_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'all_passed':True,'cases':[{'u':c['original_u'],
          'zf_0_mod4':c['selected_contact_residues'][0],
          'zf_4_mod4':c['selected_contact_residues'][4],
          'a_zero_witnesses':c['odd_weight_content_zero_witnesses']} for c in cases],
          'seconds':out['elapsed_seconds']}),flush=True)

if __name__=='__main__':main()
