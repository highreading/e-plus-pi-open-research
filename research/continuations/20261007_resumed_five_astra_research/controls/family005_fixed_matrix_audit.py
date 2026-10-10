"""Parent-authored exact reproduction of three rational determinant certificates.

Polynomial rows use closed Chebyshev coefficient formulas, independently of
the manuscript's polynomial recurrence. All arithmetic is in the prime field.
This runs no downloaded/agent code and has bounded 49x48 inputs.
"""
from pathlib import Path
from fractions import Fraction
import math,json,hashlib
R=Path(__file__).resolve().parents[1];p=101
inv=lambda a:pow(a%p,-1,p)
m=[0]*65;m[0]=2
for i in range(2,65,2):m[i]=i*m[i-2]*inv(i+1)%p
km=[0]*65;km[1]=2;kp=[0]*59
for i in range(2,65):km[i]=((i-1)*km[i-2]+m[i-2]+m[i-1])*inv(i)%p
for j in range(2,59):kp[j]=((j-2)*kp[j-2]+2*inv(j-1))*inv(j-1)%p
Y=[[0]*59 for _ in range(65)]
for i in range(65):Y[i][0]=km[i]
for j in range(59):Y[0][j]=kp[j]
for i in range(1,65):
    for j in range(1,59):Y[i][j]=(Y[i-1][j-1]-m[i-1]*inv(j))%p
bh=[0]*65;bs=[0]*65
for i in range(1,65):bh[i]=(bh[i-1]+inv(i))%p;bs[i]=(bs[i-1]+inv(i)**2)%p
def z0(i,j):return -bs[i]%p if i==j else (bh[i]-bh[j])*inv(i-j)%p
J=[[3*inv(2)*z0(i,j)%p for j in range(59)] for i in range(65)]
def rows(r):
    d=abs(r-4);P=[0]*65;D=[0]*65
    if d==0:P[62]=1
    else:
        for k in range(d//2+1):
            c=Fraction(d*(-1)**k*math.factorial(d-k-1)*2**(d-2*k),
                       2*math.factorial(k)*math.factorial(d-2*k))
            assert c.denominator==1
            P[62-d+2*k]=c.numerator
        for k in range((d-1)//2+1):
            c=(-1)**k*math.comb(d-1-k,k)*2**(d-1-2*k)
            D[63-d+2*k]=(1 if r>4 else -1)*c
    def filt(a):
        return [(a[i]-2*(a[i-1] if i else 0)+(a[i-2] if i>=2 else 0))%p for i in range(65)]
    return filt(P),filt(D)
B=[]
for r in range(49):
    P,D=rows(r)
    v=[sum(P[i]*Y[i][j]-D[i]*J[i][j] for i in range(65))%p for j in range(7,59)]
    for _ in range(4):v=[(v[j]-v[j+1])%p for j in range(len(v)-1)]
    assert len(v)==48;B.append(v)
expected={
0:[60,68,62,79,47,32,69,57,30,72,35,66,43,20,85,48,
   88,4,77,54,60,79,26,68,83,39,40,65,1,68,78,24,
   15,98,32,22,94,9,99,10,15,75,4,2,25,53,90,79],
1:[38,51,90,70,5,21,88,55,45,20,35,41,77,10,18,25,
   76,14,38,72,6,66,56,35,83,58,56,11,17,20,30,24,
   28,11,25,70,79,99,66,38,4,41,63,91,63,17,90,98],
-1:[82,92,26,87,21,74,87,88,88,3,14,23,38,58,36,20,
    26,33,94,74,78,45,93,86,73,66,45,30,61,3,88,27,
    20,58,69,48,78,39,48,1,66,18,86,93,52,92,39,77]}
cert=[]
for sigma in (0,1,-1):
    A=[[(B[i][j]+sigma*B[i+1][j])%p for j in range(48)] for i in range(48)]
    pivots=[];swaps=[];det=1
    for i in range(48):
        if not A[i][i]:
            k=next(k for k in range(i+1,48) if A[k][i])
            A[i],A[k]=A[k],A[i];swaps.append([i,k]);det=-det
        v=A[i][i];assert v;pivots.append(v);det=det*v%p
        for k in range(i+1,48):
            mult=A[k][i]*inv(v)%p
            for j in range(i,48):A[k][j]=(A[k][j]-mult*A[i][j])%p
    assert pivots==expected[sigma],(sigma,pivots)
    assert swaps==([[30,31],[45,46]] if sigma==1 else [])
    assert det%p
    cert.append({'sigma':sigma,'pivots':pivots,'swaps':swaps,'determinant_mod101':det%p})
source=R/'literature/openai_math_20261006/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/nonvanishing.tex'
obj={'modulus':p,'base_matrix_size':[49,48],
     'row_method':'Closed Chebyshev coefficients, followed by exact (1-t)^2 multiplication.',
     'base_matrix_mod101':B,'determinant_certificates':cert,
     'scope':'All three specified rational48x48 matrices have nonzero determinants. This checks the fixed finite certificate, not the Frobenius bridge, real energy bound, Catalan proof or e+pi transfer.',
     'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
(R/'controls/family005_fixed_matrix_certificate.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps({'matrices_checked':3,'pivots_checked':144,'all_expected_swaps_match':True,
                  'determinants_mod101':{str(c['sigma']):c['determinant_mod101'] for c in cert},'scope':obj['scope']}))
