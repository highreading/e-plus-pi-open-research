"""Coordinator-authored finite checks of two new, distinct determinant ledgers.

All inputs are hard-bounded below; no remote code, network or credential access.
These checks establish finite equalities only, not asymptotic error bounds.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial as fac, comb, gcd, lcm
from functools import reduce
import json

OUT=Path(__file__).resolve().parent

def determinant(rows):
    a=[[Q(x) for x in row] for row in rows]
    n=len(a)
    if n==0:return Q(1)
    answer=Q(1)
    for j in range(n):
        p=next((i for i in range(j,n) if a[i][j]),None)
        if p is None:return Q(0)
        if p!=j:a[j],a[p]=a[p],a[j];answer=-answer
        pivot=a[j][j];answer*=pivot
        for i in range(j+1,n):
            ratio=a[i][j]/pivot
            for k in range(j+1,n):a[i][k]-=ratio*a[j][k]
            a[i][j]=Q(0)
    return answer

def solve(rows,rhs):
    a=[[Q(x) for x in row]+[Q(rhs[i])] for i,row in enumerate(rows)]
    n=len(a)
    for j in range(n):
        p=next(i for i in range(j,n) if a[i][j])
        a[j],a[p]=a[p],a[j]
        pivot=a[j][j];a[j]=[v/pivot for v in a[j]]
        for i in range(n):
            if i==j:continue
            ratio=a[i][j];a[i]=[x-ratio*y for x,y in zip(a[i],a[j])]
    return [row[-1] for row in a]

def multiply(a,b):
    result=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):result[i+j]+=x*y
    return result

def laguerre(degree,alpha):
    return [Q((-1)**j*comb(degree+alpha,degree-j),fac(j)) for j in range(degree+1)]

def atan_bounds(den,terms=60):
    s=sum((Q((-1)**j,(2*j+1)*den**(2*j+1)) for j in range(terms)),Q(0))
    next_term=Q((-1)**terms,(2*terms+1)*den**(2*terms+1))
    return min(s,s+next_term),max(s,s+next_term)

en=50
el=sum((Q(1,fac(j)) for j in range(en+1)),Q(0))
eu=el+Q(1,en*fac(en))
a5,b5=atan_bounds(5);a239,b239=atan_bounds(239)
sl=el+16*a5-4*b239;su=eu+16*b5-4*a239

def primitive_pair(c0,c1):
    assert c1
    den=lcm(c0.denominator,c1.denominator)
    v0=int(c0*den);v1=int(c1*den);content=gcd(abs(v0),abs(v1))
    return (-v0*(1 if v1>0 else -1)//content,abs(v1)//content)

def finite_error(p,q):
    lo=q*sl-p;hi=q*su-p
    return {'interval_excludes_zero':lo>0 or hi<0,
            'lower':str(lo),'upper':str(hi)}

laguerre_receipts=[]
for n,b in [(3,3),(7,3),(11,3),(7,5),(11,5)]:
    d=b-1;h=n-d;alpha=d+1
    A=lambda m,j:sum((Q((-1)**s*comb(m-j,s)*fac(j),fac(j+s)) for s in range(m-j+1)),Q(0))
    B=[4*sum((Q((-1)**s,2*s+1) for s in range(2*j)),Q(0)) for j in range(b)]
    matrix=lambda X:[[Q(X)-A(n+r,j)-B[j] for j in range(b)] for r in range(b)]
    c0=determinant(matrix(0));c1=determinant(matrix(1))-c0
    assert c1>0
    mu=[sum((-1)**(d-a)*comb(d,a)*fac(j+d+1+a) for a in range(d+1)) for j in range(2*h+1)]
    gram=[[mu[i+j] for j in range(h)] for i in range(h)]
    ph=solve(gram,[-mu[h+i] for i in range(h)])+[Q(1)]
    clearer=lcm(*(x.denominator for x in ph))
    r=[int(x*clearer) for x in multiply(ph,[(-1)**(d-a)*comb(d,a) for a in range(d+1)])]
    assert reduce(gcd,(abs(x) for x in r))==1
    assert all(sum(ph[j]*mu[i+j] for j in range(h+1))==0 for i in range(h))
    F=sum(r[j]*fac(j) for j in range(n+1))
    E=sum(r[j]*sum(fac(j)//fac(k) for k in range(j+1)) for j in range(n+1))
    residual=[Q(x) for x in r];gamma=[]
    for j in range(b):
        gj=laguerre(n-j,j+1)
        coefficient=residual[n-j]/gj[n-j]
        assert coefficient.denominator==1
        gamma.append(int(coefficient))
        for a,v in enumerate(gj):residual[a]-=coefficient*v
    assert not any(residual)
    w=[comb(n,j)*gamma[j] for j in range(b)]
    assert sum(w)==F
    arctan_charge=sum((w[j]*B[j] for j in range(b)),Q(0))
    ell=arctan_charge.denominator;T=arctan_charge.numerator
    delta=determinant(gram)
    base_delta=reduce(lambda x,y:x*y,(fac(i)*fac(i+alpha) for i in range(h)),1)
    z0=Q(reduce(lambda x,y:x*y,(fac(s) for s in range(d)),1),reduce(lambda x,y:x*y,(fac(i) for i in range(h,n)),1))*delta/base_delta
    tau=Q((-1)**n,fac(n))*z0
    K=Q(reduce(lambda x,y:x*y,(fac(n+j) for j in range(b)),1),reduce(lambda x,y:x*y,(fac(j)*fac(n-j) for j in range(b)),1))
    assert K.denominator==1
    sigma=tau/(clearer*K)
    assert c1==sigma*F and c0==-sigma*(E+arctan_charge)
    nu=[sum((-1)**(d-a)*comb(d,a)*fac(j+a) for a in range(d+1)) for j in range(d+2*h+1)]
    exponents=[0]+[d+i for i in range(1,h+1)]
    Z=determinant([[nu[i+j] for j in range(h+1)] for i in exponents])
    assert Z>0 and Z.denominator==1 and Z==(-1)**h*Q(F,clearer)*delta
    prefactor=Q(reduce(lambda x,y:x*y,(fac(s) for s in range(d)),1)*reduce(lambda x,y:x*y,(fac(j) for j in range(b)),1),base_delta*reduce(lambda x,y:x*y,(fac(n+j) for j in range(b)),1))
    assert c1==prefactor*Z
    g=gcd(abs(F),abs(ell*E+T))
    p=(1 if F>0 else -1)*(ell*E+T)//g;q=ell*abs(F)//g
    assert (p,q)==primitive_pair(c0,c1)
    receipt={'n':n,'b':b,'scope':'Auxiliary finite instance, not an original A2 index.',
             'r':r,'F':F,'E':E,'w':w,'ell':ell,'T':T,'g':g,
             'constant':str(c0),'affine_coefficient':str(c1),
             'Z':int(Z),'primitive_p':p,'primitive_q':q,'identities_passed':True,
             'finite_error':finite_error(p,q)}
    if (n,b)==(3,3):
        assert r==[-84,181,-110,13] and (F,E)==(-45,-64)
        assert w==[-78,276,-243] and arctan_charge==Q(1136,35)
        assert c0==Q(-368,100800) and c1==Q(525,100800)
        assert sum((Q(w[j])*Q(5,9)**j for j in range(b)),Q(0))==Q(1,3)
    laguerre_receipts.append(receipt)

# A different compact family: independently check the new saturated k3 ledger.
a=[1]
for j in range(1,15):a.append(1-j*a[-1])
c=[a[2*j]-(-1)**j for j in range(8)];ds=[x//2 for x in c]
qs={}
Qrows={}
for m in range(2,6):
    row=[Q(4*ds[m]-ds[m+1]),Q(-ds[m])]+[Q(0)]*(m-2)+[Q(1)]
    Qrows[m]=row;qs[m]=ds[m+2]-4*ds[m+1]-117*ds[m]
assert 6498*401-67*38891==1
R=[6498*(Qrows[2][i] if i<len(Qrows[2]) else 0)-67*(Qrows[3][i] if i<len(Qrows[3]) else 0) for i in range(4)]
rows=[[401*(Qrows[3][i] if i<4 else 0)-38891*(Qrows[2][i] if i<3 else 0) for i in range(4)]]
for m in (4,5):
    assert qs[m]%16==0
    rows.append([Qrows[m][i]-Q(qs[m],16)*(R[i] if i<4 else 0) for i in range(m+1)])
assert rows[0]==[1789763,102231,-38891,401]
assert all(reduce(gcd,(abs(int(v)) for v in row))==1 for row in rows)
assert all(sum(row[m]*c[m+j] for m in range(len(row)))==0 for row in rows for j in range(3))
rho=[Q(0)]
for j in range(7):rho.append(Q(1,2*j+1)-rho[-1])
corrections=[-fac(2*j)+4*rho[j] for j in range(8)]
periods=[sum((v*(-1)**j for j,v in enumerate(row)),Q(0)) for row in rows]
entry=[[sum((row[m]*corrections[m+j] for m in range(len(row))),Q(0)) for j in range(3)] for row in rows]
L=lcm(*(v.denominator for row in entry for v in row));assert L==45045
moment=lambda X:[[entry[i][j]+Q(X)*periods[i]*(-1)**j for j in range(3)] for i in range(3)]
m0=determinant(moment(0));m1=determinant(moment(1))-m0
block=lambda X:[[c[m+j] for j in range(3)]+[L*(corrections[m+j]+Q(X)*(-1)**(m+j)) for j in range(3)] for m in range(6)]
H0=determinant(block(0));H1=determinant(block(1))-H0
assert H0.denominator==H1.denominator==1
scale=128*L**3
sign=1 if H0==scale*m0 else -1
assert H0==sign*scale*m0 and H1==sign*scale*m1
G=gcd(abs(int(H0)),abs(int(H1)))
p,q=primitive_pair(H0,H1)
assert (p,q)==primitive_pair(m0,m1)
compact={'k':3,'scope':'One finite compact determinant, not infinite nonvanishing/decay.',
         'rows':[[int(v) for v in row] for row in rows],'actual_entry_clearer':L,
         'H0':int(H0),'H1':int(H1),'final_all_prime_gcd':G,
         'block_factor':scale,'block_factor_sign':sign,
         'primitive_p':p,'primitive_q':q,'finite_error':finite_error(p,q),
         'all_checks_passed':True,'smith_data_reused_from_prior_certificate':True}
out={'parent_authored':True,'network_or_credentials_used':False,
     'scope':'Finite independent normalization checks only; no infinite theorem.',
     'laguerre':laguerre_receipts,'compact_k3':compact}
(OUT/'new_mixed_normalization_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'all_checks_passed':True,'laguerre_instances':len(laguerre_receipts),
                  'laguerre_finite_nonzero':[v['finite_error']['interval_excludes_zero'] for v in laguerre_receipts],
                  'compact_k3_primitive_p':p,'compact_k3_primitive_q':q,
                  'compact_k3_nonzero':compact['finite_error']['interval_excludes_zero']}))
