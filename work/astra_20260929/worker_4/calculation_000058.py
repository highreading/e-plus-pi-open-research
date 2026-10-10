from fractions import Fraction as Q
from math import factorial as fac, comb, gcd, lcm
import json


def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c


def legendre_integer(m):
    out=[0]*(m+1)
    for j in range(m//2+1):
        d=m-2*j
        c=fac(2*m-2*j)//(fac(j)*fac(m-j)*fac(d))
        for r in range(d+1):
            out[r]+=c*comb(d,r)*2**r*(-1)**(d-r)
    return out


def moment(d):
    return Q(2,2**d)*sum((Q(comb(d,j)*(-1)**(j//2),j+1) for j in range(0,d+1,2)),Q(0))


def derivative_data(m):
    p=[1]
    for unused in range(m):
        p=mul(p,[2,-2,1])
    h=[Q(fac(m)*p[m-r],2**m*fac(r)) for r in range(m+1)]
    assert all(x.denominator==1 for x in h)
    vals=[]
    for order in range(4):
        vals.append(sum((x*Q(fac(m+r),fac(m+r-order)) for r,x in enumerate(h) if m+r>=order),Q(0)))
    assert all(x.denominator==1 for x in vals)
    return tuple(int(x) for x in vals)


def vp(x,p=3):
    x=Q(x)
    if not x:
        return None
    a,b=abs(x.numerator),x.denominator
    ans=0
    while a%p==0:
        ans+=1
        a//=p
    while b%p==0:
        ans-=1
        b//=p
    return ans


def cross(a,b):
    return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]


def det_mod(matrix,p):
    a=[[int(Q(x).numerator%p)*pow(Q(x).denominator%p,-1,p)%p for x in row] for row in matrix]
    ans=1
    for j in range(len(a)):
        pivot=next((r for r in range(j,len(a)) if a[r][j]),None)
        if pivot is None:
            return 0
        if pivot!=j:
            a[j],a[pivot]=a[pivot],a[j]
            ans=-ans
        v=a[j][j]
        ans=ans*v%p
        iv=pow(v,-1,p)
        for r in range(j+1,len(a)):
            t=a[r][j]*iv%p
            for k in range(j,len(a)):
                a[r][k]=(a[r][k]-t*a[j][k])%p
    return ans%p


expected_valuations={3:2,6:4,9:8,12:10}
results=[]
for n in (3,6,9,12):
    mu=[moment(d) for d in range(2*n+3)]
    Ls=[legendre_integer(m) for m in range(n+2)]
    assert Ls[0]==[1] and Ls[1]==[-2,4]
    # Independently check the recurrence against the coefficient construction.
    for m in range(1,n+1):
        rhs=mul(Ls[m],[-2*(2*m+1),4*(2*m+1)])
        for i,x in enumerate(Ls[m-1]):
            rhs[i]+=4*m*x
        assert rhs==[(m+1)*x for x in Ls[m+1]]
    kernel=[[Q(0) for j in range(n+1)] for i in range(n+1)]
    for m in range(n+1):
        weight=Q((-1)**m*(2*m+1),2*4**m)
        for i,x in enumerate(Ls[m]):
            for j,y in enumerate(Ls[m]):
                kernel[i][j]+=weight*x*y
    for d in range(n+1):
        for i in range(n+1):
            assert sum((kernel[i][j]*mu[j+d] for j in range(n+1)),Q(0))==int(i==d)
    U=Ls[n+1]
    functionals=[[sum((kernel[i][k]/fac(n+k+1-j) for k in range(n+1)),Q(0)) for i in range(n+1)] for j in range(3)]
    av=[sum((Q(x,fac(n+k+1-j)) for k,x in enumerate(U)),Q(0)) for j in range(3)]
    tv=[sum(row,Q(0)) for row in functionals]
    B=cross(av,[1+x for x in tv])
    Cstar_poly=[-sum((B[j]*functionals[j][i] for j in range(3)),Q(0)) for i in range(n+1)]
    C=Cstar_poly[::-1]
    def exponential(k):
        return Q(1,fac(k)) if k>=0 else Q(0)
    def fcoef(k):
        return mu[k-1] if k>=1 else Q(0)
    def tail_coefficient(d):
        return sum((B[j]*exponential(d-j) for j in range(3)),Q(0))+sum((C[j]*fcoef(d-j) for j in range(n+1)),Q(0))
    A=[-tail_coefficient(d) for d in range(n+1)]
    for d in range(2*n+3):
        assert (A[d] if d<=n else 0)+tail_coefficient(d)==0
    Y=sum(B,Q(0))
    assert Y!=0 and Y==sum(C,Q(0))
    original_system=[]
    for d in range(n+1,2*n+3):
        original_system.append([exponential(d-j) for j in range(3)]+[fcoef(d-j) for j in range(n+1)])
    original_system.append([1]*3+[0]*(n+1))
    original_system.append([0]*3+[1]*(n+1))
    determinant_mod=det_mod(original_system,1000003)
    assert determinant_mod!=0
    P=Ls[n]
    a,b=sum(P),sum(U)
    def w_value(poly):
        quotient=[sum(poly[k+1:]) for k in range(len(poly)-1)]
        check=mul(quotient,[-1,1])
        check[0]+=sum(poly)
        assert check==poly
        return sum((Q(x)*mu[k] for k,x in enumerate(quotient)),Q(0))
    wP,wU=w_value(P),w_value(U)
    G=Q((-1)**n*2**(2*n+3),n+1)
    assert a*wU-b*wP==G
    E=[]
    acc=Q(0)
    for k0 in range(2*n+2):
        acc+=Q(1,fac(k0))
        E.append(acc)
    TP=sum((Q(x)*E[n+d] for d,x in enumerate(P)),Q(0))
    TU=sum((Q(x)*E[n+d] for d,x in enumerate(U)),Q(0))
    h,J,K,M=derivative_data(n)
    eta,J1,K1,M1=derivative_data(n+1)
    h2,J2,K2,M2=derivative_data(n+2)
    S=J1*J1-eta*K1
    Cs=(J1-eta)*J-(K1-J1)*h
    W=J1*J-K1*h
    k=(n+1)**2
    f=Q(2**n,fac(n)**2)
    g=Q(2**(n+1),fac(n+1)**2)
    assert av==[g*eta,g*J1,g*K1]
    D=Q(k*b*Cs-2*a*S)
    terms=[2*(wP+TP)*S,-k*(wU+TU)*Cs,-2*f*eta*W]
    X=sum(terms,Q(0))
    alpha=g*f/(G*k)
    assert alpha==Q((-1)**n,4*(n+1)**3*fac(n)**4)
    assert X!=0 and D!=0
    assert Y==alpha*D
    assert sum(A,Q(0))==alpha*X
    ratio=sum(A,Q(0))/Y
    assert ratio==X/D
    q=ratio.denominator
    assert vp(X)==-expected_valuations[n] and vp(D)==0
    assert vp(q)==expected_valuations[n]
    assert vp(q)==max(0,vp(D)-vp(X))
    clearer=2**(n+1)*fac(2*n+2)*fac(n)**2
    Xi,Di=clearer*X,clearer*D
    assert Xi.denominator==Di.denominator==1
    assert abs(Di.numerator)//gcd(abs(Xi.numerator),abs(Di.numerator))==q
    matrix=[[h,J],[J1,K1],[K2,M2]]
    assert [[x%3 for x in row] for row in matrix]==[[1,0],[1,2],[2,0]]
    minors=[matrix[i][0]*matrix[j][1]-matrix[i][1]*matrix[j][0] for i,j in ((0,1),(0,2),(1,2))]
    assert [x%3 for x in minors]==[2,0,2]
    omega=gcd(*[abs(x) for x in minors])
    record={'n':n,'X':str(X),'D':str(D),'three_numerator_terms':[str(x) for x in terms],'reduced_ratio':str(ratio),'v3_X_D_q':[vp(X),vp(D),vp(q)],'system_determinant_mod_1000003':determinant_mod,'omega':omega,'order_verified_through':2*n+2}
    if n==3:
        assert q==414090
    if n==6:
        assert q==260737140696321600
    if n==12:
        normalized=[[x/Y for x in poly] for poly in (A,B,C)]
        coefficient_lcm=lcm(*[x.denominator for poly in normalized for x in poly])
        integers=[[int(coefficient_lcm*x) for x in poly] for poly in normalized]
        coefficient_gcd=gcd(*[abs(x) for poly in integers for x in poly])
        assert coefficient_gcd==1
        Ap,Bp,Cp=[sum(poly) for poly in integers]
        endpoint_gcd=gcd(abs(Ap),abs(Bp))
        assert coefficient_lcm==36403805741687347841562731899445831419791586099200000
        assert Ap==-213321732297551284888756637809663458680168482090637760
        assert Bp==Cp==coefficient_lcm
        assert endpoint_gcd==73920
        assert ratio==Q(-2885845945583756559642270533139386616344270591053,492475727024991177510318342795533433709301760000)
        assert omega==2
        raw_values=[[vp(x) for x in poly] for poly in (A,B,C)]
        expected_raw=[[-20,-29,-29,-30,-28,-27,-30,-28,-29,-31,-30,-30,-31],[-20,-20,-20],[-29,-28,-28,-29,-27,-25,-28,-27,-25,-29,-28,-28,-29]]
        assert raw_values==expected_raw
        assert A[9]==Q(70258319964601742651907386906257846183752669008862391,41862757044983129743635393450910276386816000000000000)
        assert A[12]==Q(-117101645785521063996267915148229150170255509691511,41115207812037002426784761425001164308480000000000000)
        normalized_min=min(vp(x) for poly in normalized for x in poly if x)
        raw_min=min(vp(x) for poly in (A,B,C) for x in poly if x)
        assert normalized_min==-11 and raw_min==-31 and vp(Y)==-20
        assert [vp(Ap),vp(Bp),vp(endpoint_gcd)]==[1,11,1]
        record['primitive_normalization']={'coefficient_lcm':str(coefficient_lcm),'coefficient_gcd':coefficient_gcd,'primitive_endpoints':[str(Ap),str(Bp),str(Cp)],'endpoint_gcd':endpoint_gcd,'normalized_min_v3':normalized_min,'raw_min_v3':raw_min,'raw_endpoint_scale_v3':vp(Y),'raw_coefficient_v3':raw_values}
    results.append(record)
print(json.dumps({'status':'all_assertions_passed','method':'explicit integer Legendre coefficients, verified reproducing kernel, cross-product projection, and independent modular nonsingularity certificates','results':results},indent=2))