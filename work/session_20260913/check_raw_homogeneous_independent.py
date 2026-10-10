"""Independent original-row controls n3,n5; no archived certificate replay."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'math_packages'))
import sympy as s
from math import factorial,comb
import json
z=s.symbols('z');D=1+z*z
def tau(k):return s.Rational((-1)**((k-1)//2),k) if k>0 and k%2 else s.S.Zero
def ff(k):return s.Rational(1,factorial(k)) if k>=0 else s.S.Zero
def clean(v):return s.cancel(v)
out=[]
for n in (3,5):
    mat=[]
    for k in range(n+1,3*n+1):
        mat.append([factorial(k)*ff(k-j) for j in range(n+1)]+[factorial(k)*tau(k-j) for j in range(n+1)])
    mat += [[-4]*(n+1)+[1]*(n+1),[1]*(n+1)+[0]*(n+1)]
    mm=s.Matrix(mat);sol=mm.inv()*s.Matrix([0]*(2*n+1)+[1]);DB=mm.det()
    bs=list(sol[:n+1]);cs=list(sol[n+1:]);aa=[-sum(bs[j]*ff(r-j)+cs[j]*tau(r-j) for j in range(n+1)) for r in range(n+1)]
    B=sum(bs[j]*z**j for j in range(n+1));C=sum(cs[j]*z**j for j in range(n+1));A=sum(aa[j]*z**j for j in range(n+1))
    fp=[None,1/D,-2*z/D**2,(6*z*z-2)/D**3]
    es=[s.diff(A,z,r)+sum(comb(r,j)*s.diff(C,z,r-j)*fp[j] for j in range(1,r+1)) for r in range(4)]
    us=[sum(comb(r,j)*s.diff(B,z,j) for j in range(r+1)) for r in range(4)]
    vs=[s.diff(C,z,r) for r in range(4)]
    def wr(rows):return clean(s.Matrix([[es[r],us[r],vs[r]] for r in rows]).det())
    w012=wr((0,1,2));Q=clean(D**2*w012/z**(3*n-1))
    a3=z*D*Q
    a2=-(((z+3*n-1)*D-2*z*s.diff(D,z))*Q+z*D*s.diff(Q,z))
    a1=clean(D**3*wr((0,2,3))/z**(3*n-2));a0=clean(-D**3*wr((1,2,3))/z**(3*n-2))
    coeff=[a0,a1,a2,a3]
    assert clean(s.diff(w012,z)+w012-wr((0,1,3)))==0
    assert clean(-D**3*wr((0,1,3))/z**(3*n-2)-a2)==0
    assert all(s.denom(clean(v))==1 or not s.denom(clean(v)).has(z) for v in [Q]+coeff)
    assert all(clean(sum(coeff[r]*ys[r] for r in range(4)))==0 for ys in (es,us,vs))
    assert [s.degree(v,z) for v in [a3,a2,a1,a0]] <= [6,6,5,4] # Also checked individually below.
    assert all(s.degree(v,z)<=lim for v,lim in zip([a3,a2,a1,a0],[6,6,5,4]))
    xi=aa[n]*cs[n-1]-aa[n-1]*cs[n]+cs[n]**2
    assert s.Poly(Q,z).nth(3)==bs[n]*xi
    # Exact original augmented minor form of the same identity.
    def aug(row):return s.Matrix(mat[:-1]+[row]).det()
    def unit(j):return [int(k==j) for k in range(2*n+2)]
    dB=aug(unit(n));dC=aug(unit(2*n+1));dCprev=aug(unit(2*n))
    arow=lambda r:[-factorial(r)*ff(r-j) for j in range(n+1)]+[-factorial(r)*tau(r-j) for j in range(n+1)]
    dA=aug(arow(n));dAprev=aug(arow(n-1))
    K=dA*dCprev-n*dAprev*dC+factorial(n)*dC*dC
    assert clean(s.Poly(Q,z).nth(3)-dB*K/(factorial(n)*DB**3))==0
    # Independent Laurent branch at infinity, including the C F tail.
    la={j:aa[j] for j in range(n+1)}
    for j,c in enumerate(cs):
        for r in range(1,2*n+9,2):la[j-r]=la.get(j-r,0)+c*s.Rational((-1)**((r+1)//2),r)
    la={j:clean(c) for j,c in la.items() if c};cc=s.degree(C,z);dd=max(la)
    if dd==cc:
        rat=la[cc]/cs[cc]
        for j,c in enumerate(cs):la[j]=clean(la.get(j,0)-rat*c)
        la={j:c for j,c in la.items() if c};dd=max(la)
    bb=s.degree(B,z);q=s.degree(Q,z);qc=s.Poly(Q,z).LC()
    assert bb+cc+dd==3*n+q-4 and cc!=dd
    assert s.Poly(a1,z).nth(q+2)==(cc+dd-1)*qc
    assert s.Poly(a0,z).nth(q+1)==-cc*dd*qc
    # Exact high-order and origin defect ledger.
    rcoeff=[aa[k] if k<=n else 0 for k in range(3*n+5)]
    for k in range(3*n+5):rcoeff[k]+=sum(bs[j]*ff(k-j)+cs[j]*tau(k-j) for j in range(n+1))
    M=next(k for k,v in enumerate(rcoeff) if v)
    jetrows=[];orders=[]
    for k in range(2*n+2):
        jetrows.append([sum(bs[j]*ff(k-j) for j in range(n+1)),cs[k] if k<=n else 0])
        rk=s.Matrix(jetrows).rank()
        if rk>len(orders):orders.append(k)
        if rk==2:break
    q0=min(m[0] for m,c in s.Poly(Q,z).terms())
    assert M+sum(orders)==3*n+2+q0
    generic=s.gcd(Q,s.diff(Q,z)).as_poly(z).degree()==0 and s.gcd(Q,z*D).as_poly(z).degree()==0
    if generic:
        assert s.rem(a1*(s.diff(a2,z)+a1)+s.diff(a3,z)*(s.diff(a1,z)+a0),Q,z)==0
        assert s.rem(a0*(s.diff(a2,z)+a1)+s.diff(a3,z)*s.diff(a0,z),Q,z)==0
    out.append({'n':n,'actual_endpoint_B1':str(sum(bs)),'actual_endpoint_C1':str(sum(cs)),'direct_three_solution_annihilation':True,'all_polynomial_degree_bounds':True,'q':int(q),'infinity_powers':[int(bb),int(cc),int(dd)],'q3_direct_and_original_minor_formulas':True,'B_top_nonzero':bool(bs[n]),'infinity_two_jet_nonzero':bool(xi),'origin_ledger':{'M':M,'echelon_orders':orders,'ord_Q0':q0},'simple_apparent_hypotheses':generic,'apparent_congruences':generic})
result={'status':'PASS; independent controls n3,n5','checks':out}
Path(__file__).with_name('raw_homogeneous_independent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
