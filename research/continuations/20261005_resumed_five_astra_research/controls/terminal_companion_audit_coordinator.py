"""Personally authored bounded exact force/companion consistency certificate.

Direct finite original force sums are compared to contiguity identities. This
does not prove an infinite reconstruction-height or primitive-growth theorem.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb,gcd,log
from functools import lru_cache
import hashlib,json
import sympy as sp
from scalar_displacement_audit_coordinator import qpower,rational
from endpoint_recurrence_reconstruction_coordinator import vp,residue,factorial_depth,logarithm_floor,toF

ROOT=Path(__file__).resolve().parent

@lru_cache(None)
def producer(n):
    pol=qpower(n);fac=[factorial(i) for i in range(2*n+5)]
    e=[];l=[];es=F(0);ls=F(0);alpha=[F(1),F(1)]
    for j in range(2,2*n+4):alpha.append(alpha[-1]-alpha[-2]/2)
    for j in range(2*n+3):
        es+=F(1,fac[j])
        if j:ls+=2*alpha[j-1]/j
        e.append(fac[j]*es);l.append(fac[j]*ls)
    def force(seq):
        return [sum((pol[s]*F(fac[n+i],fac[n+i-s])*seq[2*n+i-s]
                     for s in range(min(2*n,n+i)+1)),F(0)) for i in range(3)]
    be=[sum((pol[s]*F(fac[j],fac[j-s]) for s in range(min(j,2*n)+1)),F(0))
        for j in range(n+3)]
    return {'n':n,'pol':pol,'B':be,'e':force(e),'l':force(l)}

def one(case):
    n=case['n'];a,b,c=[producer(n+i) for i in range(3)]
    fac=factorial(n);fn=fac*fac
    tau=[F(1),F(1)];rho=[F(0),F(1)]
    for j in range(n+1):
        tau.append(((2*j+3)*tau[-1]+(j+1)*tau[-2])/(j+2))
        rho.append(((2*j+3)*rho[-1]+(j+1)*rho[-2])/(j+2))
    for j in range(n+3):
        direct=sum((F(comb(j,2*k)*comb(2*k,k),1<<k) for k in range(j//2+1)),F(0))
        assert tau[j]==direct
    convolution=sum((tau[j]*tau[n-1-j]/(j+1) for j in range(n)),F(0))
    assert rho[n]==convolution
    assert tau[n]*rho[n+1]-tau[n+1]*rho[n]==F((-1)**n,n+1)
    E=b['B'][n+1];G=b['B'][n+2];Ep=c['B'][n+2]
    Psi=(n+1)*(n+2)*E+2*(n+2)*G+Ep
    for component in ('e','l'):
        lhs=c[component][0]-(n+2)*(2*n+3)*b[component][0]-(n+2)*(n+1)**3*a[component][0]
        assert lhs==(Psi if component=='e' else 0)
    z=[fn*tau[n],fn*F(n+1,2)*(tau[n]+tau[n+1]),fn*F((n+1)*(n+2),2)*tau[n+2]]
    predicted_log=[4*fn*rho[n],2*fn*(n+1)*(rho[n]+rho[n+1]),2*fn*(n+1)*(n+2)*rho[n+2]]
    assert predicted_log==a['l']
    omega=(-1)**n*(n+1)*(tau[n]*b['e'][0]/factorial(n+1)**2-tau[n+1]*a['e'][0]/fn)
    delta=a['e'][1]-z[1]*a['e'][0]/z[0]
    assert delta==(-1)**n*fn*omega/(2*tau[n])-E/(2*(n+1))
    P=[0,1,2*n+3]
    sigma=a['e'][0]/z[0]
    assert a['e']==[sigma*z[i]+delta*P[i]+(E if i==2 else 0) for i in range(3)]
    assert a['l']==[4*rho[n]*z[i]/tau[n]+2*(-1)**n*fn*P[i]/tau[n] for i in range(3)]
    C=sp.Matrix(3,3,lambda i,j:rational(F(factorial(n+i),factorial(n+i-j))*a['B'][n+i-j]))
    inv=C.inv();sv=sp.Matrix([1,-n,n*(n+1)])
    def endpoints(force,endpoint):
        v=inv*sp.Matrix([rational(x) for x in force])
        return toF(endpoint-(sv.T*v)[0]),toF(v[2])
    u0,ub=endpoints(z,0);v0,vb=endpoints(a['e'],1)
    v0full,vbfull=endpoints([a['e'][i]+a['l'][i] for i in range(3)],1)
    clear=int(case['least_clearer'])
    assert u0==F(int(case['U'][0]),clear) and ub==F(int(case['U'][-1]),clear)
    assert v0full==F(int(case['V'][0]),clear) and vbfull==F(int(case['V'][-1]),clear)
    uu=[int(case['U'][0]),int(case['U'][-1])]
    vv=[int(case['V'][0]),int(case['V'][-1])]
    rowgcd=[gcd(abs(x),abs(y)) for x,y in zip(uu,vv)]
    reduced_first=[x//r for x,r in zip(uu,rowgcd)]
    shared=gcd(abs(reduced_first[0]),abs(reduced_first[1]))
    AA,BB=[x//shared for x in reduced_first]
    assert AA==int(case['A']) and BB==int(case['B'])
    U0,U3=u0/fn,ub/fn
    g0,g3=endpoints(P,0);h0,h3=endpoints([0,0,1],0)
    A0=1+delta*g0+E*h0;A3=delta*g3+E*h3
    dd=U0*A3-U3*A0
    theta=(U0*A3+fn*sigma*U0*U3)/dd
    assert theta==u0*vb/(u0*vb-ub*v0)
    Fnum=fac*sum((F(1,factorial(j)) for j in range(n+1)),F(0))
    assert Fnum.denominator==1
    xi=sigma-Fnum/fac
    flat=(U0*A3+fn*xi*U0*U3)/dd;unit=U0*U3/dd
    assert theta-flat==fac*unit*Fnum
    local=[];AB=abs(AA*BB);unselected=AB
    for p in [p for p in (3,5,7) if n%p==0]:
        Np=factorial_depth(n,p);logp=logarithm_floor(n,p)
        assert residue(tau[n],p)!=0
        assert vp(omega,p)==-2*Np
        digit=residue(fn*omega,p)
        assert digit==residue(2*(-1)**n*tau[n],p)
        depths=[vp(x,p) for x in a['l']]
        assert all(v is None or v>=2*Np-logp for v in depths)
        abdepth=vp(AB,p);unselected//=p**abdepth
        local.append({'p':p,'K_star':2*Np-logp,'omega_depth':vp(omega,p),
                      'factorial_scaled_omega_digit':digit,'log_force_depths':depths,
                      'coprime_endpoint_product_depth':abdepth})
    out={'n':n,'original_complete_endpoints_match':True,'exact_zero_residual_checks':10,
         'adjacent_producer_maximum_source':2*n+6,
         'omega_numerator':str(omega.numerator),'omega_denominator':str(omega.denominator),
         'local':local,'coprime_endpoint_A':str(AA),'coprime_endpoint_B':str(BB),
         'endpoint_row_gcds':[str(v) for v in rowgcd],
         'endpoint_normalization_note':'A,B arise after BOTH complete endpoint rows are made primitive. They depend on the complete second force through the row gcds; the first-column ratio alone is insufficient.',
         'unselected_endpoint_product':str(unselected),
         'log_unselected_endpoint_product_over_n':log(unselected)/n}
    print(json.dumps({k:out[k] for k in ('n','exact_zero_residual_checks','local','log_unselected_endpoint_product_over_n')}),flush=True)
    return out

if __name__=='__main__':
    prior=json.loads((ROOT/'general_endpoint_weights_certificate.json').read_text())
    out={'status':'PASS','scope':'Four actual finite d2 endpoint producers with auxiliary adjacent producers; no infinite height, gap or primitive-growth theorem',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'cases':[one(v) for v in prior['cases']]}
    dest=ROOT/'terminal_companion_audit_certificate.json';dest.write_text(json.dumps(out,indent=2)+'\n')
    receipt={k:v for k,v in out.items() if k!='cases'}
    receipt['cases']=[{k:v for k,v in row.items() if k not in ('omega_numerator','omega_denominator','coprime_endpoint_A','coprime_endpoint_B','unselected_endpoint_product')} for row in out['cases']]
    receipt['artifact_sha256']=hashlib.sha256(dest.read_bytes()).hexdigest()
    (ROOT/'terminal_companion_audit_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
