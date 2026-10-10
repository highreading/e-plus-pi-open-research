"""Coordinator-authored finite scalar/Pascal and full-contact displacement checks.

No network or credentials. Auxiliary finite cases do not prove original-family
relative norm laws. Run with the existing computation-only sandbox profile.
"""
from pathlib import Path
from math import factorial, comb
from fractions import Fraction as F
import hashlib, json
import sympy as sp

ROOT=Path(__file__).resolve().parent

def solve(A,B,mod):
    n=len(A);aug=[list(A[i])+list(B[i]) for i in range(n)]
    for k in range(n):
        p=next(i for i in range(k,n) if aug[i][k]%3)
        aug[k],aug[p]=aug[p],aug[k]
        inv=pow(aug[k][k],-1,mod);aug[k]=[x*inv%mod for x in aug[k]]
        for i in range(n):
            if i==k:continue
            c=aug[i][k]
            if c:aug[i]=[(x-c*y)%mod for x,y in zip(aug[i],aug[k])]
    assert all(aug[i][j]==int(i==j) for i in range(n) for j in range(n))
    return [row[n:] for row in aug]

def pascal_inverse_map(f):
    n=len(f);N=(n-2)//3;groups=[f[r::3] for r in range(3)]
    aa=[]
    for group in groups:
        aa.append([sum((-1)**(i-j)*comb(i,j)*group[j] for j in range(i+1))%3
                   for i in range(len(group))])
    bb=[aa[2]+[aa[0][-1]],[(2*x)%3 for x in aa[1]],
        [(aa[0][i]-aa[2][i])%3 for i in range(N)]]
    out=[0]*n
    for r,group in enumerate(bb):
        for i in range(len(group)):
            out[3*i+r]=sum((-1)**(j-i)*comb(j,i)*group[j]
                           for j in range(i,len(group)))%3
    return out

def scalar_case(n):
    mod=3**11;target=3**10;N=(n-2)//3
    gam=[1,0]
    for r in range(1,2*n):gam.append(((4*r+2)*gam[-1]+4*gam[-2])%mod)
    T=[[comb(i+j,i)*gam[i+j]%mod for j in range(n)] for i in range(n)]
    fac=factorial(n-1);u=[fac//factorial(i)*pow(-2,i,mod)%mod for i in range(n)]
    col=[comb(n+i,i)*gam[n+i]%mod for i in range(n)]
    w=[0]*n
    for i in range(N+1):
        ci=(-1)**(N-i)*comb(N,i);w[3*i]=ci;w[3*i+1]=-ci
    assert all((sum(T[i][j]*w[j] for j in range(n))-u[i])%3==0 for i in range(n))
    assert sum(u[i]*w[i] for i in range(n))%9==3*(N+1)%9
    assert sum(w[i]*T[i][j]*w[j] for i in range(n) for j in range(n))%9==6*N%9
    vectors=[]
    for rhs in (u,col):
        v=[0]*n
        for r in range(6):
            depth=3**r
            residual=[(rhs[i]-sum(T[i][j]*v[j] for j in range(n)))%mod for i in range(n)]
            assert all(x%depth==0 for x in residual)
            digit=pascal_inverse_map([(x//depth)%3 for x in residual])
            v=[x+depth*y for x,y in zip(v,digit)]
        assert all((rhs[i]-sum(T[i][j]*v[j] for j in range(n)))%3**6==0 for i in range(n))
        vectors.append(v)
    v,z=vectors
    eta_quad=(fac*fac-2*sum(u[i]*v[i] for i in range(n))
              +sum(v[i]*T[i][j]*v[j] for i in range(n) for j in range(n)))%mod
    sigma_quad=(sum(u[i]*z[i]+v[i]*col[i] for i in range(n))
                -sum(v[i]*T[i][j]*z[j] for i in range(n) for j in range(n)))%target
    direct=solve(T,[[u[i],col[i]] for i in range(n)],mod)
    eta_direct=(fac*fac-sum(u[i]*direct[i][0] for i in range(n)))%mod
    sigma_direct=sum(u[i]*direct[i][1] for i in range(n))%target
    assert eta_quad==eta_direct and sigma_quad==sigma_direct
    chi=3*(n*sigma_direct+2*u[-1])%mod
    bc=-68-(n-2)
    tau=[(3*n*col[i]+(bc+6)*T[i][-1]+2*bc*pow(n-1,-1,mod)*T[i][-2])%mod
         for i in range(n)]
    chi_full=sum(direct[i][0]*tau[i] for i in range(n))%mod
    assert chi_full==chi and eta_direct%9==3 and chi%9==3
    xi=(chi//3)*pow(eta_direct//3,-1,target)%target
    assert xi%3==1
    print(json.dumps({'scalar_n':n,'eta_mod9':eta_direct%9,'chi_mod9':chi%9,
                      'xi_mod3':xi%3,'quadratic_precision_match':True}),flush=True)
    return {'n':n,'modulus':mod,'quotient_modulus':target,'eta_residue':eta_direct,
            'chi_residue':chi,'xi_residue':xi,'six_digit_pascal_lift_match':True,
            'quadratic_scalar_match':True,'full_force_contraction_match':True}

def poly_mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def qpower(n):
    out=[F(1)]
    for _ in range(n):out=poly_mul(out,[F(1),F(-1),F(1,2)])
    return out

def rational(x):
    x=F(x);return sp.Rational(x.numerator,x.denominator)

def displacement(n,b):
    qp=qpower(n);qp1=qpower(n+1);fac=[factorial(i) for i in range(2*n+b+3)]
    def fall(N,s):return fac[N]//fac[N-s]
    Nt=sp.Matrix(b,b,lambda i,j:rational(sum(qp[s]*fall(n+i,s)*comb(n+i-s,j)
                              for s in range(min(2*n,n+i-j)+1))))
    upper=sp.Matrix(b,b,lambda i,j:comb(n,j-i) if j>=i else 0)
    A=Nt*upper
    def entry(power,m,N,j):
        Bj=[F(comb(m,j-k),fac[k]) for k in range(j+1)]
        pol=poly_mul(power,Bj)
        return sum((pol[s]*fall(N,s) for s in range(min(N,len(pol)-1)+1)),F(0))
    Ag=sp.Matrix(b,b,lambda i,j:rational(entry(qp,n,n+i,j)))
    assert A==Ag
    V=sp.Matrix(b-2,b+1,lambda row,j:rational(entry(qp1,n+1,n+row+1,j)))
    C=sp.Matrix(b+1,b,lambda j,k:(j if k==j-1 else 0)-(1 if k==j else 0))
    Dop=sp.zeros(b-2,b)
    for row in range(b-2):
        i=row+1;Dop[row,i+1]=1;Dop[row,i]=-(2*n+2*i+1)
        Dop[row,i-1]=F((n+i)*(n+3*i-1),2)
        if i>=2:Dop[row,i-2]=F((n+i)*(n+i-1)*(1-i),2)
    base=[F(1)]
    for _ in range(n):base=poly_mul(base,[F(1),F(2),F(2)])
    first=[]
    for i in range(b):
        J=sum(base[n-r]*comb(i,r) for r in range(min(n,i)+1))
        first.append(F(fac[n+i],fac[n])*J)
    alpha=[F(1),F(1)]
    for m in range(2,2*n+b):alpha.append(alpha[-1]-alpha[-2]/2)
    ew=[];lw=[];eacc=F(0);lacc=F(0)
    for m in range(2*n+b):
        eacc+=F(1,fac[m])
        if m:lacc+=2*alpha[m-1]/m
        ew.append(fac[m]*eacc);lw.append(fac[m]*lacc)
    eh=[];lh=[]
    for i in range(b):
        eh.append(sum(qp[s]*fall(n+i,s)*ew[2*n+i-s] for s in range(min(2*n,n+i)+1)))
        lh.append(sum(qp[s]*fall(n+i,s)*lw[2*n+i-s] for s in range(min(2*n,n+i)+1)))
    ff=sp.Matrix([rational(x) for x in first]);evec=sp.Matrix([rational(x) for x in eh]);lvec=sp.Matrix([rational(x) for x in lh])
    rvec=(evec+lvec-A*sp.Matrix([fac[j] for j in range(b)]))/fac[b]
    assert Dop*A+V*C==sp.zeros(b-2,b)
    assert Dop*ff==sp.zeros(b-2,1)
    assert Dop*rvec==V[:,-1]
    assert Dop*lvec==sp.zeros(b-2,1)
    assert V.rank()==b-2
    W=sp.diag(*[comb(n+2,j) for j in range(b+1)])
    RR=W*C
    def forward(a0,a1,forced):
        arr=[rational(a0),rational(a1)]
        for i in range(1,b-1):
            z=(2*n+2*i+1)*arr[i]-rational(F((n+i)*(n+3*i-1),2))*arr[i-1]
            if i>=2:z-=rational(F((n+i)*(n+i-1)*(1-i),2))*arr[i-2]
            if forced:z+=V[i-1,b]
            arr.append(z)
        return sp.Matrix(arr)
    h0,h1,tau=forward(1,0,False),forward(0,1,False),forward(0,0,True)
    inv=A.inv();BB=sp.Matrix.hstack(RR*inv*h0,RR*inv*h1,RR*inv*tau+W[:,-1])
    assert BB*sp.Matrix([ff[0],ff[1],0])==RR*inv*ff
    assert BB*sp.Matrix([rvec[0],rvec[1],1])==RR*inv*rvec+W[:,-1]
    assert BB.rank()==3
    gram=BB.T*BB
    print(json.dumps({'displacement_n':n,'b':b,'exact_residuals_zero':True,'basis_rank':3}),flush=True)
    return {'n':n,'b':b,'rows':list(range(1,b-1)),'contact_generating_identity':True,
            'contact_displacement':True,'complete_force_displacement':True,
            'first_force_homogeneity':True,'log_force_homogeneity':True,'three_column_rank':3,
            'gram_exact':[[str(gram[i,j]) for j in range(3)] for i in range(3)]}

def digit_table():
    p=29;rec=[1,2]
    for r in range(1,28):rec.append(((2*(2*r+1)*rec[-1]+4*r*rec[-2])*pow(r+1,-1,p))%p)
    direct=[sum(comb(r,2*a)*comb(2*a,a)*2**(r-a) for a in range(r//2+1))%p for r in range(29)]
    assert rec==direct and all(rec)
    expected=[1,2,8,3,20,12,14,2,13,24,22,21,21,20,6,7,17,19,6,16,4,2,2,18,25,14,15,14,1]
    assert rec==expected
    return {'p':p,'table':rec,'zero_set':[],'independent_coefficient_match':True,
            'low_digit_product':rec[0]*rec[7]*rec[24]*rec[7]%p}

if __name__=='__main__':
    out={'status':'PASS','scope':'Finite auxiliary Pascal/scalar implementation and complete contact identities; no original-family residual or norm-factor theorem',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'digit_table':digit_table(),'scalar_cases':[], 'displacement_cases':[]}
    for n in list(range(5,33,3))+[83,245]:out['scalar_cases'].append(scalar_case(n))
    for n,b in [(6,4),(7,5),(12,7),(3,3)]:out['displacement_cases'].append(displacement(n,b))
    dest=ROOT/'scalar_displacement_audit_certificate.json';dest.write_text(json.dumps(out,indent=2)+'\n')
    receipt={key:out[key] for key in ['status','scope','source_sha256','digit_table','scalar_cases']}
    receipt['displacement_cases']=[{k:v for k,v in row.items() if k!='gram_exact'} for row in out['displacement_cases']]
    receipt['artifact_sha256']=hashlib.sha256(dest.read_bytes()).hexdigest()
    (ROOT/'scalar_displacement_audit_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
