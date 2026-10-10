"""Personally authored bounded exact audits, with no network or credentials.

Remote mathematical assertions are tested, not executed as instructions.
Finite cases do not certify asymptotic or complete higher-depth applications.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial, gcd
import hashlib, json, sys
import sympy as sp

OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(OUT))
from endpoint_extrapolant_coordinator import full_lift

def vp(x, p):
    x = abs(int(x))
    if x == 0: return None
    v = 0
    while x % p == 0:
        x //= p; v += 1
    return v

def vq(x, p):
    x = F(int(x.p),int(x.q)) if isinstance(x,sp.Rational) else F(x)
    if not x: return None
    return vp(x.numerator, p)-vp(x.denominator, p)

def det_mod(a, p):
    a = [[int(x)%p for x in row] for row in a]
    n = len(a); val = 1
    for j in range(n):
        z = next((i for i in range(j,n) if a[i][j]), None)
        if z is None: return 0
        if z != j: a[z],a[j] = a[j],a[z]; val = -val
        val = val*a[j][j]%p; inv = pow(a[j][j], -1, p)
        for i in range(j+1,n):
            c = a[i][j]*inv%p
            if c:
                for k in range(j,n): a[i][k]=(a[i][k]-c*a[j][k])%p
    return val%p

def solve_mod(a,b,p):
    a = [[int(x)%p for x in row]+[int(z)%p] for row,z in zip(a,b)]
    n=len(a)
    for j in range(n):
        z=next(i for i in range(j,n) if a[i][j])
        a[z],a[j]=a[j],a[z]; inv=pow(a[j][j],-1,p)
        a[j]=[x*inv%p for x in a[j]]
        for i in range(n):
            if i==j: continue
            c=a[i][j]
            a[i]=[(x-c*y)%p for x,y in zip(a[i],a[j])]
    return [row[-1] for row in a]

def audit_even_moments():
    gam=[1,0]
    for r in range(1,320): gam.append((4*r+2)*gam[-1]+4*gam[-2])
    for r in range(48):
        direct=sum(comb(r,k)*(-2)**(r-k)*factorial(r+k) for k in range(r+1))
        assert direct==factorial(r)*gam[r]
    assert all(x%3==(0 if r%3==1 else 1) for r,x in enumerate(gam))
    residues=[]
    for n in list(range(1,33))+[47,48,49,80,81,82,120,121,122]:
        a=[[comb(i+j,i)*gam[i+j]%3 for j in range(n)] for i in range(n)]
        m=[sum(i%3==r for i in range(n)) for r in range(3)]
        actual=det_mod(a,3); expected=pow(2,m[1]+m[2],3)
        assert actual==expected
        row={'n':n,'det_mod3':actual,'expected':expected}
        if n%3==2:
            lastfact=factorial(n-1)
            u=[lastfact//factorial(i)*(-2)**i for i in range(n)]
            sol=solve_mod(a,u,3)
            assert sol[-1]==2
            row['terminal_pivot_mod3']=sol[-1]
        residues.append(row)
    exact=[]
    for n in [2,5,8,11,14,17]:
        T=sp.Matrix(n,n,lambda i,j:comb(i+j,i)*gam[i+j])
        fac=factorial(n-1); J=sp.diag(*(factorial(i) for i in range(n)))
        u=sp.Matrix([fac//factorial(i)*(-2)**i for i in range(n)])
        eta=fac**2-(u.T*T.inv()*u)[0]
        G=sp.Matrix(n,n,lambda i,j:factorial(i+j)*gam[i+j]-(-2)**(i+j))
        assert G==J*(T-u*u.T/fac**2)*J
        assert G.det()==J.det()**2*T.det()*eta/fac**2
        assert eta<0
        A=n-2; bb=-68-A
        H=sp.Matrix([3*factorial(n+i)*gam[n+i]+(bb+6)*factorial(n-1+i)*gam[n-1+i]+2*bb*factorial(n-2+i)*gam[n-2+i] for i in range(n)])
        tau=sp.Matrix([H[i]/(factorial(i)*fac) for i in range(n)])
        ts=T.inv()*tau; vs=T.inv()*u; xi=(u.T*ts)[0]/eta
        ecoef=sp.Matrix([-sp.Rational(fac,factorial(i))*(ts[i]+xi*vs[i]) for i in range(n)])
        assert G*ecoef==-H
        ev=sum(ecoef[i]*(-2)**i for i in range(n))
        assert ev==-fac**2*xi
        exact.append({'n':n,'eta_v3':vq(eta,3),'xi_v3':vq(xi,3),
                      'terminal_correction_v3':vq(ecoef[-1],3),
                      'rank_one_formula_pass':True,'actual_force_identity_pass':True,
                      'scope':'Auxiliary finite order; retained original order-six congruence is not assumed here.'})
    result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'gamma_direct_cases':48,'unit_and_pivot_cases':residues,'exact_signed_cases':exact,
            'scope':'Finite exact audit; general unit/localization theorem still needs its proof.'}
    (OUT/'even_moment_unit_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'even_moment_unit_cases':len(residues),'signed_cases':len(exact),'all_pass':True}),flush=True)

def s_bounds():
    N=256
    es=sum((F(1,factorial(k)) for k in range(N+1)),F(0))
    elo=es; ehi=es+F(1,factorial(N+1))*F(N+2,N+1)
    def atan(z):
        z=F(1,z)
        lo=sum(((-1)**k*z**(2*k+1)/(2*k+1) for k in range(N)),F(0))
        return lo,lo+z**(2*N+1)/(2*N+1)
    a0,a1=atan(5); b0,b1=atan(239)
    return elo+16*a0-4*b1,ehi+16*a1-4*b0

def audit_weights():
    slo,shi=s_bounds(); cases=[]; receipts=[]
    for n in [15,30,105,210]:
        d=2; U,V,db=full_lift(n,3)
        r0=gcd(U[0],V[0]); rb=gcd(U[-1],V[-1])
        uu0=U[0]//r0; uub=U[-1]//rb; vv0=V[0]//r0; vvb=V[-1]//rb
        h=gcd(uu0,uub); A=uu0//h; B=uub//h
        J=B*vv0-A*vvb; VV=A*vvb; WW=B*vv0
        assert gcd(A,B)==1
        primes=[p for p in [3,5,7] if n%p==0]
        primeinfo=[]; probes=[]; weights={(0,1),(1,1),(n*n//gcd(n*n,2),2//gcd(n*n,2))}
        for p in primes:
            m=2*vp(factorial(n),p); w=vq(F(V[0],db),p)
            assert w>=vp(n,p) and vp(db,p)==0
            assert vq(F(U[0],db),p)==m and vq(F(U[-1],db),p)==m
            assert vq(F(V[-1],db),p)==0 and vp(J,p)==0
            primeinfo.append({'p':p,'m':m,'w':w,'v_p_n':vp(n,p)})
            weights.add((1,p*p))
            for r in sorted(set([max(0,w-1),w+1])): weights.add((1+p**r,1))
            if w<m:
                for level in sorted(set([w+1,m-1,m])):
                    mod=p**level; root=(-VV*pow(J,-1,mod))%mod
                    weights.add((root,1)); weights.add((root+mod,1))
        for a,k in sorted(weights):
            assert gcd(a,k)==1
            TT=a*J+k*VV
            FF=gcd(abs(A),abs(a))*gcd(abs(B),abs(a-k)); GG=gcd(k,abs(J))
            assert TT%(FF*GG)==0
            HH=gcd(h,abs(TT)//(FF*GG))
            q=k*h*abs(A*B)//(FF*GG*HH); pn=(1 if A*B>0 else -1)*TT//(FF*GG*HH)
            center=F(a,k)*F(V[0],U[0])+F(k-a,k)*F(V[-1],U[-1])
            assert center==F(pn,q) and center.denominator==q and center.numerator==pn
            checks=[]
            for info in primeinfo:
                p,m,w=info['p'],info['m'],info['w']; kap=vp(k,p); r=vp(a-k,p)
                vt=vp(TT,p)
                expected=max(0,m+kap-(vt if vt is not None else m+kap))
                assert vp(q,p)==expected
                t=min(m,w); expected_f=t if r is None else min(t,r)
                assert vp(FF,p)==expected_f and vp(GG,p)==0
                expected_h=min(m-t, (vt if vt is not None else m)-expected_f)
                assert vp(HH,p)==expected_h
                checks.append({'p':p,'q_valuation':vp(q,p),'m':m,'w':w,'r':r,'T_valuation':vt,
                               'F_valuation':vp(FF,p),'H_valuation':vp(HH,p)})
            lo=q*slo-pn; hi=q*shi-pn
            sign=1 if lo>0 else (-1 if hi<0 else 0)
            probes.append({'a':str(a),'k':str(k),'checks':checks,'q_bits':q.bit_length(),
                           'whole_form_interval_sign':sign,'whole_form_excludes_zero':sign!=0})
        saved={'n':n,'d':d,'U':[str(x) for x in U],'V':[str(x) for x in V],'least_clearer':str(db),
               'r0':str(r0),'rb':str(rb),'h':str(h),'A':str(A),'B':str(B),'J':str(J),
               'primes':primeinfo,'probes':probes}
        cases.append(saved); receipts.append({'n':n,'d':d,'primes':primeinfo,'probe_count':len(probes),
                                              'all_direct_gcd_checks_pass':True,
                                              'all_whole_intervals_nonzero':all(x['whole_form_excludes_zero'] for x in probes)})
        print(json.dumps(receipts[-1]),flush=True)
    payload={'scope':'Actual complete finite producers and full gcd; no infinite reconstruction theorem.',
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':cases}
    target=OUT/'general_endpoint_weights_certificate.json'
    target.write_text(json.dumps(payload,indent=2)+'\n')
    (OUT/'general_endpoint_weights_receipt.json').write_text(json.dumps({'cases':receipts,'artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest()},indent=2)+'\n')

def audit_shift():
    rows=[]
    for ell in range(5,17):
        prec=ell+5; mod=2**prec
        def Dmod(u): return ((pow(9,18+32*u,2**(prec+7))-81)//128)%mod
        u=0
        # Solve 2001 D +1267=0 through ell-2 bits, and force the next bit nonzero.
        for q in range(2,ell-1):
            if (2001*Dmod(u)+1267)%(2**q): u+=2**(q-2)
            assert (2001*Dmod(u)+1267)%(2**q)==0
        if (2001*Dmod(u)+1267)%(2**(ell-1))==0: u+=2**(ell-3)
        D0=Dmod(u); k=(8004*D0+5065)%mod
        assert vp((k+3)%mod,2)==ell
        values=[(k+D0)%mod,D0,(D0-1)%mod,(D0-2)%mod,k,(k+1)%mod,(k+2)%mod,(k+3)%mod]
        vals=[vp(x,2) for x in values]
        assert vals==[1,0,2,0,0,1,0,ell]
        A=(128*k+4)%(2**(prec+7))
        av=sum(vp(A+r,2) for r in range(380))-vp(factorial(380),2)
        assert av==0
        rows.append({'ell':ell,'u_residue':u,'precision':prec,'D_residue':D0,'k_residue':k,
                     'valuation_tuple':vals,'moment_relative_valuation':sum(vals[:4])-sum(vals[4:]),
                     'mandatory_multiplier_valuation':av})
    (OUT/'binary_shift380_certificate.json').write_text(json.dumps({'cases':rows,'scope':'Twelve reachable finite residue classes; full coefficient p380 is not evaluated.'},indent=2)+'\n')
    print(json.dumps({'shift380_cases':len(rows),'all_pass':True}),flush=True)

if __name__=='__main__':
    action=sys.argv[1]
    {'moments':audit_even_moments,'weights':audit_weights,'shift':audit_shift}[action]()
