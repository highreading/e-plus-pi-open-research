"""Parent-authored bounded NEW mixed Z/Y maximal-minor content experiment.

Do not repeat pure-contact Smith forms or completed mixed k3/k5/32/33.
The output certifies only k6,7,8 and the exact original finite boundaries.
"""
from pathlib import Path
from math import factorial, gcd, lcm, prod
from fractions import Fraction
import hashlib
import json
import time
import sympy as s

OUT=Path(__file__).resolve().parent
start=time.monotonic()

def egcd_positive(a,b):
    old_r,r=a,b
    old_s,st=1,0
    old_t,tt=0,1
    while r:
        q=old_r//r
        old_r,r=r,old_r-q*r
        old_s,st=st,old_s-q*st
        old_t,tt=tt,old_t-q*tt
    return old_r,old_s,old_t

def content_and_bezout(values):
    g=0
    coeff=[]
    for v in values:
        g2,a,b=egcd_positive(g,abs(v))
        coeff=[a*x for x in coeff]+[b if v>=0 else -b]
        g=g2
    assert sum(a*b for a,b in zip(coeff,values))==g
    assert all(v%g==0 for v in values) if g else all(v==0 for v in values)
    return g,coeff

def strip_small(value,bound):
    remaining=value
    powers={}
    if not remaining:return remaining,powers
    for p in s.primerange(2,bound+1):
        p=int(p)
        e=0
        while remaining%p==0:
            remaining//=p
            e+=1
        if e:powers[str(p)]=e
    return remaining,powers

receipts=[]
for k in (6,7,8):
    last=3*k-2
    moment=[1]
    for j in range(1,2*last+1):
        moment.append(1-j*moment[-1])
    u=[moment[2*n] for n in range(last+1)]
    c=[u[n]-(-1)**n for n in range(last+1)]
    f=[factorial(2*n) for n in range(last+1)]
    sigma=[u[n]+u[n+1] for n in range(last)]
    lam=lcm(*range(1,6*k-4,2))
    tau=[Fraction(-f[n]-f[n+1])+Fraction(4,2*n+1) for n in range(last)]
    paid_tau=[lam*x for x in tau]
    assert all(x.denominator==1 for x in paid_tau)
    rt=[int(x) for x in paid_tau]
    z=s.Matrix([[*c[m:m+k],*rt[m:m+k-1]] for m in range(2*k)])
    y=s.Matrix([[*sigma[m:m+k],*rt[m:m+k]] for m in range(2*k-1)])
    assert z.shape==(2*k,2*k-1) and y.shape==(2*k-1,2*k)
    zv=[int((-1)**r*z.extract([i for i in range(2*k) if i!=r],range(2*k-1)).det(method='domain-ge')) for r in range(2*k)]
    yv=[int((-1)**j*y.extract(range(2*k-1),[i for i in range(2*k) if i!=j]).det(method='domain-ge')) for j in range(2*k)]
    assert z.T*s.Matrix(zv)==s.zeros(2*k-1,1)
    assert y*s.Matrix(yv)==s.zeros(2*k-1,1)
    R,zb=content_and_bezout(zv)
    L,yb=content_and_bezout(yv)
    zr,zsmall=strip_small(R,6*k-4)
    yr,ysmall=strip_small(L,6*k-4)
    W=(2**15*3**2*lam)**k*prod(factorial(j) for j in range(k))**4
    descent=bool(L and W%L==0)
    if descent:
        assert sum(a*(W//L)*b for a,b in zip(yb,yv))==W
    canonical={'Z':[[int(v) for v in z.row(i)] for i in range(z.rows)],
               'Y':[[int(v) for v in y.row(i)] for i in range(y.rows)]}
    receipt={'k':k,'Lambda':lam,'source_boundaries':{'moment_max':last,'factorial_max':6*k-4,'last_odd':6*k-5},
             'Z_shape':list(z.shape),'Y_shape':list(y.shape),
             'matrix_sha256':hashlib.sha256(json.dumps(canonical,separators=(',',':')).encode()).hexdigest(),
             'all_Z_signed_maximal_minors':zv,'all_Y_signed_maximal_minors':yv,
             'actual_R_content':R,'actual_L_content':L,
             'Z_Bezout_coefficients':zb,'Y_Bezout_coefficients':yb,
             'Bezout_and_kernel_identities_verified':True,
             'Z_small_prime_depths':zsmall,'Y_small_prime_depths':ysmall,
             'Z_good_prime_part':zr,'Y_good_prime_part':yr,
             'good_prime_cutoff':6*k-4,
             'specific_W_k':W,'W_k_in_actual_Y_maximal_minor_ideal':descent,
             'W_over_L':W//L if descent else None,
             'scope':'Finite actual mixed rectangles only. No uniform content/rank, final q or irrationality conclusion.'}
    receipts.append(receipt)
    print(json.dumps({'k':k,'Z_good_prime_part':zr,'Y_good_prime_part':yr,
                     'W_k_descent':descent,'seconds':round(time.monotonic()-start,3)}),flush=True)

obj={'all_checks_passed':True,'coordinator_authored':True,
     'external_code_executed':False,'network_or_credentials_used':False,
     'pure_contact_receipt_not_recomputed':True,'closed_k3_k5_k32_k33_not_recomputed':True,
     'receipts':receipts,'seconds':round(time.monotonic()-start,3),
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'compact_k6_k8_mixed_content_certificate.json').write_text(json.dumps(obj,indent=2)+'\n')
