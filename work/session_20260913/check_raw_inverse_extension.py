"""Independent fixed controls for inverse norm, determinant bridge, signed minors."""
from fractions import Fraction as Q
from math import factorial, comb
from pathlib import Path
import json

def add(a,b):return [(a[k] if k<len(a) else Q())+(b[k] if k<len(b) else Q()) for k in range(max(len(a),len(b)))]
def scale(a,c):return [x*c for x in a]
def qs(top):
    a=[[Q(1)],[Q(),Q(1)]]
    for k in range(1,top):a.append(add([Q()]+a[-1],scale(a[-2],Q(k*k,4*k*k-1))))
    return a
def det(mat):
    a=[list(r) for r in mat];n=len(a);out=Q(1)
    for j in range(n):
        ii=next((k for k in range(j,n) if a[k][j]),None)
        if ii is None:return Q()
        if ii!=j:a[ii],a[j]=a[j],a[ii];out=-out
        pp=a[j][j];out*=pp
        for k in range(j+1,n):
            c=a[k][j]/pp
            for l in range(j+1,n):a[k][l]-=c*a[j][l]
    return out
def solve(aa,bb):
    a=[list(r)+[s] for r,s in zip(aa,bb)];n=len(a)
    for j in range(n):
        ii=next(k for k in range(j,n) if a[k][j]);a[ii],a[j]=a[j],a[ii]
        pp=a[j][j];a[j]=[x/pp for x in a[j]]
        for k in range(n):
            if k!=j:
                c=a[k][j];a[k]=[x-c*y for x,y in zip(a[k],a[j])]
    return [r[-1] for r in a]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q())
def gram(rows,H):return [[dot(a,[dot(h,b) for h in H]) for b in rows] for a in rows]

results=[]
for n in (1,3,5):
    q=qs(2*n-1)
    fs=[[c/Q(factorial(j)) for j,c in enumerate(v)] for v in q]
    hs=[Q((-1)**k*4**k,(2*k+1)*comb(2*k,k)**2) for k in range(n+1)]
    t=[Q()]*(n+1)
    for k in range(n+1):t=add(t,scale(fs[k],sum(q[k],Q())/hs[k]))
    H=[[Q(1,i+j+1) for j in range(n+1)] for i in range(n+1)]
    beta=[sum((Q((-1)**r*factorial(j),factorial(j-r)) for r in range(j+1)),Q()) for j in range(n+1)]
    Z=[Q()]*(n+1);normformula=Q()
    for k in range(n+1):
        bk=sum((Q((-1)**j*factorial(k+j),factorial(k-j)*factorial(j)) for j in range(k+1)),Q())
        jk=[Q((-1)**(k+j)*comb(k,j)*comb(k+j,j)) for j in range(k+1)]
        Z=add(Z,scale(jk,(2*k+1)*bk));normformula+=(2*k+1)*bk*bk
    assert [dot(r,Z) for r in H]==beta
    assert gram([Z],H)[0][0]==normformula
    high=[[sum((c/Q(i+j+1) for i,c in enumerate(fs[k])),Q()) for j in range(n+1)] for k in range(n+1,2*n)]
    trow=[dot(r,t) for r in H]
    L=high+[trow,beta];D=det(L)
    A=high+[add(trow,scale(beta,4))]
    cof=[(-1)**(n+i)*det([r[:i]+r[i+1:] for r in A]) for i in range(n+1)]
    P=solve(L,[Q()]*(n-1)+[Q(-4),Q(1)])
    assert P==[c/D for c in cof]
    reps=[solve(H,r) for r in A+[beta]]
    gg=gram(reps,H)
    ratio=det([r[:-1] for r in gg[:-1]])/det(gg)
    assert ratio==gram([P],H)[0][0]==gram([cof],H)[0][0]/D**2
    # Independently assemble the original integral high-jet determinant.
    original=[]
    for k in range(n+1,3*n+1):
        br=[Q(factorial(k),factorial(k-j)) for j in range(n+1)]
        cr=[Q((-1)**((k-j-1)//2)*factorial(k),k-j) if (k-j)%2 else Q() for j in range(n+1)]
        original.append(br+cr)
    original += [[Q(-4)]*(n+1)+[Q(1)]*(n+1),[Q(1)]*(n+1)+[Q()]*(n+1)]
    DB=det(original);facnum=1;facden=1;hprod=Q(1)
    for j in range(n+1):facnum*=factorial(j);hprod*=hs[j]
    for k in range(n+1,3*n+1):facden*=factorial(k)
    assert abs(D)==abs(DB)*Q(facnum,facden)/abs(hprod)
    row={'n':n,'Z_Riesz_and_exact_norm':True,'Gram_and_cofactor_norm_identity':True,'Delta_B_bridge':True,'D':str(D),'Delta_B':str(DB)}
    if n>=3:
        es=[k for k in range(n+1,2*n) if k%2==0];os=[k for k in range(n+1,2*n) if k%2]
        i0=sorted([2*j for j in range(len(es))]+[2*j+1 for j in range(len(os))])
        i1=sorted([d for d in i0 if d!=2*(len(es)-1)]+[2*len(es)])
        def minor(cols):return det([[fs[k][d] if d<len(fs[k]) else Q() for d in cols] for k in range(n+1,2*n)])
        z0,z1=minor(i0),minor(i1);assert z0*z1<0
        row['opposite_maximal_coefficient_minors']={'I0':i0,'I1':i1,'minor0':str(z0),'minor1':str(z1)}
    results.append(row)

out={'status':'PASS; independent controls n1,n3,n5','checks':results}
Path(__file__).with_name('raw_inverse_extension_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
