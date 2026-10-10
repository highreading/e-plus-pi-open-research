"""Coordinator-authored exact homogeneous separation and complete budget audit.

Four finite actual endpoint producers. No new window enumeration; no inference
about infinite short reconstruction or all-prime asymptotic denominator bounds.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb,gcd
import hashlib,json
import sympy as sp
from scalar_displacement_audit_coordinator import qpower,poly_mul,rational
from endpoint_recurrence_reconstruction_coordinator import vp,residue,factorial_depth,logarithm_floor,toF

ROOT=Path(__file__).resolve().parent

def one(case):
    n=case['n'];fac=[factorial(i) for i in range(2*n+4)]
    qp=qpower(n);qp1=qpower(n+1)
    B=[];Bp=[]
    for pol,seq in ((qp,B),(qp1,Bp)):
        for N in range(n+3):
            seq.append(sum(pol[j]*(fac[N]//fac[N-j]) for j in range(min(N,len(pol)-1)+1)))
    alpha=[F(1),F(1)]
    for j in range(2,2*n+3):alpha.append(alpha[-1]-alpha[-2]/2)
    fnum=fac[n]*sum((F(1,fac[j]) for j in range(n+1)),F(0))
    assert fnum.denominator==1
    logscalar=sum((2*alpha[j-1]/j for j in range(1,n+1)),F(0))
    eta=fnum/fac[n]+logscalar
    R=[F(1)]
    for k in range(n):
        out=[F(0)]*(len(R)+1)
        for j,x in enumerate(R):
            if j:out[j-1]+=j*x;out[j]-=j*x;out[j+1]+=j*x/2
            out[j]+=(k+1)*x;out[j+1]-=(k+1)*x
        R=out
    def sequence(initial,include_log):
        arr=[initial]
        for N in range(n+2):
            a1=arr[N-1] if N else F(0);a2=arr[N-2] if N>=2 else F(0)
            source=Bp[N]+(2*fac[N]*R[N] if include_log and N<=n else 0)
            arr.append((2*N+1)*arr[N]+F(N*(2*n+1-3*N),2)*a1
                       +F(N*(N-1)*(N-n-1),2)*a2+source)
        return arr
    afull=sequence(fac[n]*eta,True);aflat=sequence(F(0),True);aexp=sequence(fnum,False)
    homogeneous=[fac[n]*fac[N]*sum(qp[j]*comb(n+N-j,n) for j in range(min(N,2*n)+1))
                 for N in range(n+3)]
    assert all(afull[N]-aflat[N]==eta*homogeneous[N] for N in range(n+3))
    z=sp.Matrix([rational(x) for x in homogeneous[n:n+3]])
    w=sp.Matrix([rational(x) for x in afull[n:n+3]])
    wf=sp.Matrix([rational(x) for x in aflat[n:n+3]])
    we=sp.Matrix([rational(x) for x in aexp[n:n+3]])
    terminal=sp.Matrix([[F((n+1)*(n+2),2),-(2*n+3),1]])
    assert (terminal*z)[0]==0
    assert (terminal*w)[0]==rational(Bp[n+1])
    assert (terminal*(w-we))[0]==0
    C=sp.Matrix(3,3,lambda i,j:rational(F(fac[n+i],fac[n+i-j])*B[n+i-j]))
    inv=C.inv();s=sp.Matrix([1,-n,n*(n+1)])
    first=inv*z;u0=toF(-(s.T*first)[0]);ub=toF(first[2])
    def endpoints(force):
        y=inv*force
        return toF(1-(s.T*y)[0]),toF(y[2])
    v0,vb=endpoints(w);v0f,vbf=endpoints(wf);v0e,vbe=endpoints(we)
    db=int(case['least_clearer'])
    assert (u0,ub,v0,vb)==(F(int(case['U'][0]),db),F(int(case['U'][-1]),db),
                             F(int(case['V'][0]),db),F(int(case['V'][-1]),db))
    DD=u0*vb-ub*v0;DDf=u0*vbf-ub*v0f
    assert DD==DDf and v0-v0f==eta*u0 and vb-vbf==eta*ub
    theta=u0*vb/DD;flat=u0*vbf/DD;exp=u0*vbe/(u0*vbe-ub*v0e)
    unit=u0*ub/(fac[n]**2*DD)
    assert theta-flat==fac[n]*unit*(fnum+fac[n]*logscalar)
    tau=sum((F(comb(n,2*k)*comb(2*k,k),1<<k) for k in range(n//2+1)),F(0))
    weights=[(1,1),(3,2),(11,3),(17,5),(23,7),(n*n+n,2),(n*n+1,n+1),(1,15)]
    local=[];budget_checks=[]
    for p in [p for p in (3,5,7) if n%p==0]:
        Np=factorial_depth(n,p);dp=logarithm_floor(2*n+2,p)
        assert vp(theta-flat,p)==Np
        digit=residue((theta-flat)/fac[n],p)
        assert digit==residue(tau/2,p)
        assert vp(theta-exp,p) is None or vp(theta-exp,p)>=2*Np-dp
        local.append({'p':p,'factorial_depth':Np,'middle_depth':vp(theta-flat,p),
                      'normalized_middle_digit':digit,'log_force_strip_depth':2*Np-dp})
        for aa,kk in weights:
            div=gcd(aa,kk);aa//=div;kk//=div;lam=F(aa,kk)
            center=lam*v0/u0+(1-lam)*vb/ub
            center_exp=lam*v0e/u0+(1-lam)*vbe/ub
            q=center.denominator;qe=center_exp.denominator
            difference=abs(vp(q,p)-vp(qe,p));assert difference<=dp
            budget_checks.append({'p':p,'a':aa,'k':kk,'actual_q_depth':vp(q,p),
                                  'exponential_q_depth':vp(qe,p),'difference':difference,'bound':dp,
                                  'actual_p':str(center.numerator),'actual_q':str(q),
                                  'exponential_p':str(center_exp.numerator),'exponential_q':str(qe)})
    print(json.dumps({'n':n,'homogeneous_coefficient_checks':n+3,'middle_digits':local,
                      'budget_checks':len(budget_checks)}),flush=True)
    return {'n':n,'homogeneous_coefficient_checks':n+3,'original_endpoints_match':True,
            'terminal_full_log_first_identities':True,'invariant_difference_determinant':True,
            'exact_resonance_decomposition':True,'local':local,'budget_checks':budget_checks}

if __name__=='__main__':
    prior=json.loads((ROOT/'general_endpoint_weights_certificate.json').read_text())
    out={'status':'PASS','scope':'Four actual finite complete endpoint producers and selected-prime budget probes; no infinite height or all-prime growth theorem',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'cases':[one(v) for v in prior['cases']]}
    dest=ROOT/'homogeneous_budget_audit_certificate.json';dest.write_text(json.dumps(out,indent=2)+'\n')
    receipt={k:out[k] for k in ['status','scope','source_sha256']}
    receipt['cases']=[{k:v for k,v in row.items() if k!='budget_checks'}|{'budget_checks':len(row['budget_checks'])} for row in out['cases']]
    receipt['artifact_sha256']=hashlib.sha256(dest.read_bytes()).hexdigest()
    (ROOT/'homogeneous_budget_audit_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
