"""Closed n=4,8,16 spectral diagnostic, no canonical HP solves.

Parity Jacobi cutoff64, precision100 and160. Analytic rational truncation
bounds are separate from floating eigensystem/SVD estimates.
"""
import json
import math
import sys
import time
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import mpmath as mp

DEGREES=(4,8,16)
CUTOFF=64
PRECISIONS=(100,160)

def qpoly_upto(K):
    out=[[F(1)],[F(0),F(1)]]
    for k in range(1,K):
        nxt=[F(0)]+out[-1]
        beta=F(k*k,4*k*k-1)
        for j,v in enumerate(out[-2]):nxt[j]+=beta*v
        out.append(nxt)
    return out

def inner_monomial_legendre(power,degree):
    if power<degree:return F(0)
    return F(math.factorial(power)**2,
             math.factorial(power-degree)*math.factorial(power+degree+1))

Q=qpoly_upto(31)
row_mom={}
row_normsq={}
for k in sorted({k for n in DEGREES for k in range(n+1,2*n)}):
    fc=[v/F(math.factorial(j)) for j,v in enumerate(Q[k])]
    mu=[sum((fc[j]*inner_monomial_legendre(j,l) for j in range(l,k+1)),F(0)) for l in range(k+1)]
    ck=F(math.comb(2*k,k),2**k)
    row_mom[k]=(ck,mu)
    row_normsq[k]=ck*ck*(2*k+1)*sum(((2*l+1)*v*v for l,v in enumerate(mu)),F(0))

def branches_at(xi,K,cast):
    all_branches=[]
    for seed in ((1,F(1,2)),(0,1)):
        rr=[cast(seed[0]),cast(seed[1])]
        dd=[cast(0),cast(seed[1])]
        for k in range(K-1):
            A=cast(F(2*k+3,(k+1)*(k+2)))
            B=cast(F(k*k*(k-1)*(2*k+3),(k+1)**2*(k+2)*(2*k-1))) if k>=2 else cast(0)
            C=cast(F((2*k+1)*(2*k+3),(k+1)**2*(k+2)))
            dd.append(A*dd[k+1]+B*dd[k]+C*((xi-cast(1))*rr[k]+k*(rr[k-1] if k else cast(0))))
            rr.append((dd[-1]+(k+1)*rr[k])/(k+2))
        all_branches.append(rr)
    return all_branches

ones=branches_at(F(1),31,F)

def ceil_sqrt_fraction(x):
    z=math.isqrt(x.numerator//x.denominator)
    while F(z*z)<x:z+=1
    return F(z)

def certified_truncation_data(n):
    B=F(3,40)
    errors=[]
    residuals=[]
    for l in range(n+1):
        eps=B
        last=CUTOFF if (CUTOFF-l)%2==0 else CUTOFF-1
        for j in range(l+2,last+1,2):
            eps*=B/(F(j*(j+1)-l*(l+1))-F(13,40))
        gap=F(7,4) if l==0 else F(2*l)-F(1,4)
        residuals.append(eps)
        errors.append(2*eps/gap)
    e_all=sum(errors,F(0));e_top=errors[n-1]+errors[n]
    l=n-1;m=l//2
    Hm=sum((F(1,j) for j in range(1,m+1)),F(0))
    eta=3*Hm/(23*(l+1))
    # Lower bound for either exact finite or infinite g_l; rational only.
    base=F(math.factorial(l)**4,
           math.factorial(2*l)**2*math.factorial(m)**2*(2*l+1))
    if l%2:base*=2
    lower_g=base*(1-F(1,(16*l-1)**2))*(1-eta)
    assert lower_g>0
    bounds=[]
    for k in range(n+1,2*n):
        d_lower=lower_g*ones[l%2][k]
        if l%2:d_lower/=2  # 1/sqrt3 >=1/2; sqrt(2k+1)>=1
        assert d_lower>0
        norm_upper=ceil_sqrt_fraction(row_normsq[k])
        err=norm_upper*e_all/d_lower+norm_upper**2*e_top/d_lower**2
        bounds.append(err)
    return {'vector_errors':errors,'residuals':residuals,
            'matrix_error_bound':sum(bounds,F(0))}

def mf(q):
    if isinstance(q,F):return mp.mpf(q.numerator)/q.denominator
    return mp.mpf(q)

def matnorm(M):
    return mp.sqrt(mp.fsum(abs(M[i,j])**2 for i in range(M.rows) for j in range(M.cols)))

def stringify(x):return mp.nstr(x,55)

out={'scope':'Only n=4,8,16; no canonical HP triple constructed; finite Jacobi cutoff64',
     'precision_levels':list(PRECISIONS),'jacobi_cutoff':CUTOFF,
     'normalization':'u_k(l)=g_l sqrt(2k+1) r_k^0 for even l; g_l sqrt((2k+1)/3) r_k^1 for odd l; g_odd=phi1 coefficient/2',
     'certification':'Rational analytic Jacobi truncation bounds are rigorous for exact finite eigenpairs. Floating eigensystem and SVD are estimates, not interval-certified.',
     'runs':[]}
for precision in PRECISIONS:
    mp.mp.dps=precision
    started=time.monotonic()
    tcoef=lambda l:mp.mpf(l+1)/(2*mp.sqrt((2*l+1)*(2*l+3)))
    eigen={}
    for parity in (0,1):
        indices=list(range(parity,CUTOFF+1,2))
        S=mp.matrix(len(indices))
        for j,l in enumerate(indices):
            S[j,j]=l*(l+1)+mp.mpf(3)/4+(tcoef(l-1)**2 if l else 0)+tcoef(l)**2
            if j+1<len(indices):S[j,j+1]=S[j+1,j]=tcoef(l)*tcoef(l+1)
        vals,vecs=mp.eigsy(S)
        for l in range(parity,17,2):
            index=(l-parity)//2
            vec=vecs[:,index]
            if vec[index]<0:vec=-vec
            full=mp.matrix(CUTOFF+1,1)
            for j,k in enumerate(indices):full[k]=vec[j]
            finite_res=matnorm(S*vec-vals[index]*vec)
            eigen[l]={'xi':vals[index],'vector':full,
                      'g':vec[0]/(2 if parity else 1),
                      'finite_residual':finite_res}
        print(json.dumps({'stage':'eigenpairs','precision':precision,'parity':parity,'seconds':time.monotonic()-started}),flush=True)
    urows={}
    direct_error=mp.mpf(0)
    for l,e in eigen.items():
        br=branches_at(e['xi'],31,mf)[l%2]
        for k,(ck,mu) in row_mom.items():
            value=e['g']*mp.sqrt(mp.mpf(2*k+1)/(3 if l%2 else 1))*br[k]
            urows[k,l]=value
            direct=mf(ck)*mp.sqrt(2*k+1)*mp.fsum(mf(mu[j])*mp.sqrt(2*j+1)*e['vector'][j] for j in range(k+1))
            direct_error=max(direct_error,abs(value-direct)/max(abs(value),mp.mpf('1e-200')))
    run={'precision':precision,'finite_eigenpairs':[
        {'l':l,'xi':stringify(eigen[l]['xi']),'g':stringify(eigen[l]['g']),
         'residual':stringify(eigen[l]['finite_residual'])} for l in range(17)],
         'branch_vs_exact_polynomial_projection_max_relative_error':stringify(direct_error),'cases':[]}
    for n in DEGREES:
        r=n-1
        M=mp.matrix(r,n+1)
        normalizers=[]
        for i,k in enumerate(range(n+1,2*n)):
            d=mp.sqrt(urows[k,n-1]**2+urows[k,n]**2)
            normalizers.append(d)
            for l in range(n+1):M[i,l]=urows[k,l]/d
        U,Sval,V=mp.svd(M,full_matrices=True)
        Z=mp.matrix(n+1,2)
        for i in range(n+1):
            for j in range(2):Z[i,j]=V[r+j,i]
        low=mp.matrix([[Z[i,j] for j in range(2)] for i in range(n-1)])
        sinsq,_=mp.eigsy(low.T*low)
        sins=[mp.sqrt(max(mp.mpf(0),min(mp.mpf(1),v))) for v in sinsq]
        cert=certified_truncation_data(n)
        trunc_bound=mf(cert['matrix_error_bound'])
        reconstructed=U*mp.diag(list(Sval))*V[:r,:]
        case={'n':n,'singular_values_descending':list(map(stringify,Sval)),
              'smallest_nonzero_singular_value':stringify(Sval[r-1]),
              'n_squared_times_smallest_singular_value':stringify(n*n*Sval[r-1]),
              'condition_number_nonzero':stringify(Sval[0]/Sval[r-1]),
              'kernel_principal_sines_ascending':list(map(stringify,sins)),
              'kernel_principal_angles_degrees_ascending':[stringify(mp.asin(v)*180/mp.pi) for v in sins],
              'worst_kernel_sine':stringify(sins[-1]),
              'kernel_residual_Frobenius':stringify(matnorm(M*Z)),
              'kernel_orthogonality_residual':stringify(matnorm(Z.T*Z-mp.eye(2))),
              'svd_reconstruction_relative_residual':stringify(matnorm(reconstructed-M)/matnorm(M)),
              'analytic_exact_finite_to_infinite_matrix_error_upper_bound':stringify(trunc_bound),
              'analytic_error_over_numerical_sigma_min':stringify(trunc_bound/Sval[r-1]),
              'row_normalizer_min':stringify(min(normalizers)),
              'row_normalizer_max':stringify(max(normalizers)),
              'matrix_entry_max_modulus':stringify(max(abs(v) for v in M)),
              'exact_rational_matrix_error_bound':str(cert['matrix_error_bound'])}
        run['cases'].append(case)
        print(json.dumps({k:case[k] for k in ('n','smallest_nonzero_singular_value','n_squared_times_smallest_singular_value','condition_number_nonzero','worst_kernel_sine','analytic_error_over_numerical_sigma_min')},indent=2),flush=True)
    run['elapsed_seconds']=time.monotonic()-started
    out['runs'].append(run)
    (HERE/'relative_spectral_matrix_probe.json').write_text(json.dumps(out,indent=2)+'\n')
out['status']='completed'
(HERE/'relative_spectral_matrix_probe.json').write_text(json.dumps(out,indent=2)+'\n')
