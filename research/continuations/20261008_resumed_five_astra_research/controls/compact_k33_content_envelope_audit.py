"""Parent-authored, bounded exact test of the proposed k33 content envelope.

Only arithmetic is performed. The complete affine moment pencil is retained.
This finite certificate cannot establish an asymptotic law or irrationality.
"""
from pathlib import Path
from fractions import Fraction
from math import factorial, gcd, lcm, isqrt
import hashlib, json, sys, time

sys.set_int_max_str_digits(500000)
OUT=Path(__file__).resolve().parent
K=33
N=2*K
MAX_MOMENT=3*K-2

def bareiss(source):
    a=[row[:] for row in source]
    sign=1
    previous=1
    pivots=[]
    swaps=[]
    divisions=0
    for j in range(len(a)-1):
        pivot_row=next((r for r in range(j,len(a)) if a[r][j]),None)
        if pivot_row is None:
            return 0,{'pivots':pivots,'swaps':swaps,'exact_divisions':divisions,'zero_column':j}
        if pivot_row!=j:
            a[j],a[pivot_row]=a[pivot_row],a[j]
            sign=-sign
            swaps.append([j,pivot_row])
        pivot=a[j][j]
        pivots.append(str(pivot))
        for r in range(j+1,len(a)):
            left=a[r][j]
            for c in range(j+1,len(a)):
                value=pivot*a[r][c]-left*a[j][c]
                quotient,remainder=divmod(value,previous)
                assert remainder==0, (j,r,c)
                a[r][c]=quotient
                divisions+=1
            a[r][j]=0
        previous=pivot
    value=sign*a[-1][-1]
    return value,{'pivots':pivots,'swaps':swaps,'exact_divisions':divisions,
                  'last_diagonal':str(a[-1][-1]),'swap_sign':sign}

def prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))

def modular_det(source,p):
    a=[[v%p for v in row] for row in source]
    result=1
    for j in range(len(a)):
        r=next((r for r in range(j,len(a)) if a[r][j]),None)
        if r is None:return 0
        if r!=j:a[j],a[r]=a[r],a[j];result=-result
        pivot=a[j][j]
        result=result*pivot%p
        inverse=pow(pivot,-1,p)
        for r in range(j+1,len(a)):
            ratio=a[r][j]*inverse%p
            for c in range(j+1,len(a)):a[r][c]=(a[r][c]-ratio*a[j][c])%p
            a[r][j]=0
    return result%p

def bezout(a,b):
    old_r,r=abs(a),abs(b)
    old_s,s=1,0
    old_t,t=0,1
    while r:
        q=old_r//r
        old_r,r=r,old_r-q*r
        old_s,s=s,old_s-q*s
        old_t,t=t,old_t-q*t
    return old_r,old_s*(1 if a>=0 else -1),old_t*(1 if b>=0 else -1)

started=time.monotonic()
a=[1]
for n in range(1,2*MAX_MOMENT+1):a.append(1-n*a[-1])
c=[a[2*n]-(-1)**n for n in range(MAX_MOMENT+1)]
assert all(v%2==0 for v in c)
rho=[Fraction(0)]
for n in range(MAX_MOMENT):rho.append(Fraction(1,2*n+1)-rho[-1])
r=[-factorial(2*n)+4*rho[n] for n in range(MAX_MOMENT+1)]
column_clearers=[lcm(*range(1,4*K+2*j-2,2)) for j in range(K)]
full_clearer=lcm(*range(1,6*K-4,2))
E=full_clearer**K
for value in column_clearers:
    assert E%value==0
    E//=value
scalar=(2**K)*E

def matrix(s):
    rows=[]
    for m in range(N):
        right=[column_clearers[j]*(r[m+j]+s*(-1)**(m+j)) for j in range(K)]
        assert all(v.denominator==1 for v in right)
        rows.append([c[m+j]//2 for j in range(K)]+[int(v) for v in right])
    return rows

determinants=[]
certificates=[]
modular=[]
moduli=[1000000007,1000000009,1000000033]
assert all(prime(p) for p in moduli)
for s in (0,1,2):
    rows=matrix(s)
    value,certificate=bareiss(rows)
    determinant_hash=hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
    certificate.update({'parameter':s,'matrix_sha256':determinant_hash,'determinant':str(value)})
    certificates.append(certificate)
    determinants.append(value)
    for p in moduli:
        residue=modular_det(rows,p)
        assert value%p==residue
        modular.append({'parameter':s,'prime':p,'determinant_residue':residue})
    print(json.dumps({'parameter':s,'determinant_digits':len(str(abs(value))),
                      'seconds':round(time.monotonic()-started,3),'exact_divisions':certificate['exact_divisions']}),flush=True)

assert determinants[2]==2*determinants[1]-determinants[0]
H0=scalar*determinants[0]
H1=scalar*(determinants[1]-determinants[0])
G,U,V=bezout(H0,H1)
assert G==gcd(abs(H0),abs(H1)) and U*H0+V*H1==G
assert H0%G==H1%G==0 and H1<0
p=H0//G
q=-H1//G
assert gcd(abs(p),q)==1 and q>0
D=1
for t in range(K-1):D*=factorial(t)**2
assert G%(D*E)==0
B=D*E*(2**(2*K*K))*full_clearer**(2*K)
W=G//gcd(G,B)
residual=G
valuation_table=[]
for prime_value in range(2,6*K-4):
    if not prime(prime_value):continue
    v=0
    while residual%prime_value==0:residual//=prime_value;v+=1
    valuation_table.append({'prime':prime_value,'valuation':v})

coefficient_overlap=gcd(full_clearer**K,G)
record={'parent_authored':True,'scope':'Only the complete compact k33 pencil; not original binary indices or an infinite theorem.',
        'network_or_credentials_used':False,'k':K,'matrix_size':N,'max_moment':MAX_MOMENT,
        'max_factorial':2*MAX_MOMENT,'last_odd_denominator':6*K-5,
        'full_clearer':str(full_clearer),'column_clearers':[str(v) for v in column_clearers],
        'E':str(E),'contact_column_division':2,'total_determinant_scalar':str(scalar),
        'determinant_certificates':certificates,'independent_modular_checks':modular,
        'affinity_checked_at_0_1_2':True,'H0':str(H0),'H1':str(H1),'G':str(G),
        'bezout_U':str(U),'bezout_V':str(V),'bezout_identity_verified':True,
        'primitive_p':str(p),'primitive_q':str(q),'primitive_gcd_one':True,
        'D':str(D),'D_E_divides_G':True,'proposed_envelope_B':str(B),'W':str(W),
        'content_envelope_holds_at_k33':W==1,'small_prime_valuations':valuation_table,
        'remaining_gcd_factor_after_all_primes_at_most_193':str(residual),
        'least_simultaneous_coefficient_clearer':str(full_clearer**K//coefficient_overlap),
        'content_after_that_clearing':str(G//coefficient_overlap),
        'seconds':round(time.monotonic()-started,3)}
(OUT/'compact_k33_content_envelope_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'all_checks_passed':True,'k':K,'primitive_q_digits':len(str(q)),
                  'gcd_digits':len(str(G)),'W_is_one':W==1,'W_digits':len(str(W)),
                  'large_prime_residual_is_one':residual==1,'large_prime_residual_digits':len(str(residual)),
                  'seconds':record['seconds']}),flush=True)
