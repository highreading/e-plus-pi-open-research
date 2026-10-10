"""Parent-authored bounded source jets at 24 original-index/prime pairs.

Only 9p jet coefficients are evaluated, using exact paid coefficient
division and independent logarithmic-time complex Chebyshev evaluation.
No dense original polynomial, primitive affine clearer or q is computed.
"""
from pathlib import Path
from math import factorial
import hashlib,json,time
P=Path(__file__).resolve().parent

def cmul(a,b,m):
    return ((a[0]*b[0]-a[1]*b[1])%m,(a[0]*b[1]+a[1]*b[0])%m)
def csub(a,b,m):return ((a[0]-b[0])%m,(a[1]-b[1])%m)
def cscale(a,k,m):return (a[0]*k%m,a[1]*k%m)
def cheb_pair(n,m):
    z=(-1%m,2%m);a=(1,0);b=z
    for bit in bin(n)[2:]:
        d=csub(cscale(cmul(a,a,m),2,m),(1,0),m)
        e=csub(cscale(cmul(a,b,m),2,m),z,m)
        f=csub(cscale(cmul(b,b,m),2,m),(1,0),m)
        a,b=(d,e) if bit=='0' else (e,f)
    prev=csub(cscale(cmul(z,a,m),2,m),b,m)
    inv=csub(csub(cmul(a,a,m),cscale(cmul(z,cmul(a,prev,m),m),2,m),m),
             csub((0,0),cmul(prev,prev,m),m),m)
    assert inv==csub((1,0),cmul(z,z,m),m)
    return a,prev

def jet(n,J,m):
    # T_n(1-2x): a_(r+1)=-2(n^2-r^2)a_r/[(r+1)(2r+1)].
    # Every division is performed over Z BEFORE reducing modulo m.
    a=1;out=[]
    for r in range(J):
        out.append(a%m)
        if r+1<J:
            numerator=-2*(n*n-r*r)*a
            denominator=(r+1)*(2*r+1)
            a,rem=divmod(numerator,denominator)
            assert rem==0
    return out

def mul(a,b,J,m):
    out=[0]*J
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:J-i]):out[i+j]=(out[i+j]+x*y)%m
    return out
def add(a,b,J,m):return [((a[j] if j<len(a) else 0)+(b[j] if j<len(b) else 0))%m for j in range(J)]
def depth(x,p,cap):
    if x==0:return cap
    v=0
    while v<cap and x%p==0:x//=p;v+=1
    return v

# Finite independent checks of the two evaluation algorithms, not a repeat
# of any complete normalization receipt.
for m in (7**3,11**3):
    z=(-1%m,2%m);old=(1,0);cur=z
    for n in range(1,31):
        fast,prev=cheb_pair(n,m);assert fast==cur and prev==old
        j=jet(n,n+1,m)
        # Direct polynomial value at t=i means x=1-i.
        val=(0,0);power=(1,0)
        for c in j:
            val=((val[0]+c*power[0])%m,(val[1]+c*power[1])%m)
            power=cmul(power,(1,m-1),m)
        assert val==fast
        old,cur=cur,csub(cscale(cmul(z,cur,m),2,m),old,m)

started=time.monotonic();records=[]
for u in range(8):
    N=9**(18+32*u)
    for p in (7,11,13):
        cap=9;m=p**cap;J=cap*p
        assert depth(factorial(J),p,100)>=cap
        cn,cp=cheb_pair(N,m)
        bn,bp=cn[1],cp[1]
        d=(cn[0]*bp-cp[0]*bn)%m
        jn,jp,jm=jet(N,J,m),jet(N-1,J,m),jet(N-3,J,m)
        bj=[(bp*jn[r]-bn*jp[r])%m for r in range(J)]
        B2=mul(bj,bj,J,m)
        t=[1,m-1];one_minus_t=[0,1]
        one_t2=add([1],mul(t,t,J,m),J,m)
        H=mul(mul(t,one_minus_t,J,m),mul(one_t2,one_t2,J,m),J,m)
        K=mul(H,mul(jm,jm,J,m),J,m)
        moments=[((-1)**r*factorial(r))%m for r in range(J)]
        U=-sum(K[r]*moments[r] for r in range(J))%m
        I=sum(B2[r]*moments[r] for r in range(J))%m
        V=(I-d*d)%m
        r=min(depth(bn,p,cap),depth(bp,p,cap))
        du,dv=depth(U,p,cap),depth(V,p,cap)
        obj={'original_u':u,'N':str(N),'N_bit_length':N.bit_length(),'p':p,
             'precision':cap,'modulus':m,'jet_terms':J,
             'complex_C_N':cn,'complex_C_Nminus1':cp,'b_N':bn,'b_Nminus1':bp,
             'd':d,'U':U,'I_minus_d2':V,'local_g_depth_capped':r,
             'U_depth_capped':du,'raw_V_depth_capped':dv,
             'source_jet_K':K,'source_jet_B_squared':B2,
             'exact_jet_coefficient_divisions':3*(J-1)}
        if r<=4:
            assert V%(p**(2*r))==0
            vd=dv-2*r;cd=min(du,vd)
            exact=(du<cap and du<=vd) or (dv<cap and vd<=du)
            obj.update({'paid_square_division':p**(2*r),
                        'divided_raw_V_residue':V//(p**(2*r)),
                        'divided_raw_V_precision':cap-2*r,
                        'actual_c_depth':cd,'c_depth_exact':exact,
                        'status':'exact_local_c_depth' if exact else 'certified_c_depth_lower_truncation'})
        else:obj['status']='unresolved_square_division_at_this_precision'
        records.append(obj)
        print(json.dumps({k:obj[k] for k in ('original_u','p','local_g_depth_capped','U_depth_capped','raw_V_depth_capped','status')}
                         | {k:obj[k] for k in ('actual_c_depth','c_depth_exact') if k in obj}),flush=True)

out={'all_checks_passed':True,'scope':'24 original-index pairs u0..7,p7/11/13 at p^9. Bounded source jets ONLY, not complete primitive normalization or an infinite all-prime theorem.',
     'network_or_keys_used':False,'actual_normalization_h_lambda_G_q_computed':False,
     'max_jet_degree':116,'max_factorial':116,'records':records,
     'seconds':round(time.monotonic()-started,3),
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'signed_chebyshev_original_source_jet_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checks':True,'records':len(records),'seconds':out['seconds'],
                  'odd_c_factors_found':[{'u':r['original_u'],'p':r['p'],'depth':r.get('actual_c_depth'),'exact':r.get('c_depth_exact')} for r in records if r.get('actual_c_depth',0)>0]}),flush=True)
