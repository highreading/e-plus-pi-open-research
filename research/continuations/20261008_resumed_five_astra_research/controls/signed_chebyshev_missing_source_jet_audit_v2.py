"""Parent-authored NEW original source pairs at previously uncovered U-zero classes.

This does not repeat any of the closed u0..7 source or normalization receipts.
Every coefficient division is paid over Z; only five bounded p^5 jets are used.
"""
from pathlib import Path
# CORRECTED source weights in x=1-t: positive r!, not (-1)^r r!.
from math import factorial
import hashlib,json,time
# Independent actual-source seeds and degree6 correction check.
assert sum(c*factorial(r) for r,c in enumerate([1,-2]))==-1
assert sum(c*factorial(r) for r,c in enumerate([1,-8,8]))==9
assert sum(c*factorial(r) for r,c in enumerate([0,4,-12,16,-12,5,-1]))==-332

OUT=Path(__file__).resolve().parent

def cmul(a,b,m):return ((a[0]*b[0]-a[1]*b[1])%m,(a[0]*b[1]+a[1]*b[0])%m)
def cs(a,b,m):return ((a[0]-b[0])%m,(a[1]-b[1])%m)
def scale(a,k,m):return (a[0]*k%m,a[1]*k%m)
def cheb(n,m):
    z=(-1%m,2%m);a=(1,0);b=z
    for bit in bin(n)[2:]:
        d=cs(scale(cmul(a,a,m),2,m),(1,0),m)
        e=cs(scale(cmul(a,b,m),2,m),z,m)
        f=cs(scale(cmul(b,b,m),2,m),(1,0),m)
        a,b=(d,e) if bit=='0' else (e,f)
    prev=cs(scale(cmul(z,a,m),2,m),b,m)
    invariant=cs(cs(cmul(a,a,m),scale(cmul(z,cmul(a,prev,m),m),2,m),m),scale(cmul(prev,prev,m),-1,m),m)
    assert invariant==cs((1,0),cmul(z,z,m),m)
    return a,prev
def jet(n,J,m):
    a=1;out=[]
    for r in range(J):
        out.append(a%m)
        if r+1<J:
            a,rem=divmod(-2*(n*n-r*r)*a,(r+1)*(2*r+1));assert rem==0
    return out
def mul(a,b,J,m):
    out=[0]*J
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:J-i]):out[i+j]=(out[i+j]+x*y)%m
    return out
def depth(a,p,cap):
    if not a:return cap
    v=0
    while v<cap and not a%p:a//=p;v+=1
    return v

start=time.monotonic();records=[]
for u,p in ((9,7),(13,7),(17,7),(23,13),(27,13)):
    N=9**(18+32*u);cap=5;m=p**cap;J=cap*p
    assert depth(factorial(J),p,100)>=cap
    cn,cp=cheb(N,m);bn,bp=cn[1],cp[1]
    d=(cn[0]*bp-cp[0]*bn)%m
    jn,jp,jm=jet(N,J,m),jet(N-1,J,m),jet(N-3,J,m)
    bj=[(bp*jn[r]-bn*jp[r])%m for r in range(J)]
    B2=mul(bj,bj,J,m)
    t=[1,m-1]+[0]*(J-2);omt=[0,1]+[0]*(J-2)
    one_t2=mul(t,t,J,m);one_t2[0]=(one_t2[0]+1)%m
    H=mul(mul(t,omt,J,m),mul(one_t2,one_t2,J,m),J,m)
    K=mul(H,mul(jm,jm,J,m),J,m)
    moments=[factorial(r)%m for r in range(J)]
    U=-sum(K[r]*moments[r] for r in range(J))%m
    I=sum(B2[r]*moments[r] for r in range(J))%m
    V=(I-d*d)%m
    r=min(depth(bn,p,cap),depth(bp,p,cap));du=depth(U,p,cap);dv=depth(V,p,cap)
    item={'original_u':u,'p':p,'N_bit_length':N.bit_length(),'precision':cap,
          'modulus':m,'jet_terms':J,'N_mod_p_squared':N%(p*p),
          'complex_C_N':cn,'complex_C_Nminus1':cp,'d':d,'U':U,'raw_V':V,
          'g_B_local_depth_capped':r,'U_depth_capped':du,'raw_V_depth_capped':dv,
          'source_K_jet':K,'source_B_squared_jet':B2,
          'exact_integer_coefficient_divisions':3*(J-1)}
    if 2*r<cap:
        assert V%(p**(2*r))==0
        vd=dv-2*r;cd=min(du,vd)
        exact=(du<cap and du<=vd) or (dv<cap and vd<=du)
        item.update({'paid_square_division':p**(2*r),'divided_raw_V':V//p**(2*r),
                     'divided_V_precision':cap-2*r,'actual_c_depth':cd,'depth_exact':exact})
    else:item['status']='unresolved_square_division_at_this_precision'
    records.append(item)
    print(json.dumps({k:v for k,v in item.items() if k not in
          ('source_K_jet','source_B_squared_jet','exact_integer_coefficient_divisions')}),flush=True)
obj={'checks_passed':True,'scope':'Five NEW original-index source pairs at the first uncovered U-zero residue classes. No all-prime bound and no h/lambda/G/q computation.',
     'records':records,'network_or_keys_used':False,'h_lambda_G_q_computed':False,
     'seconds':round(time.monotonic()-start,3),
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'signed_chebyshev_missing_source_jet_certificate_v2.json').write_text(json.dumps(obj,indent=2)+'\n')
