import json, math, time, sys
from functools import reduce
from fractions import Fraction
import sympy as s
from sympy.polys.matrices import DomainMatrix
sys.set_int_max_str_digits(0)
start=time.time()
k=27; n=54
L=math.lcm(*range(1,6*k-4,2))
e=[0]
for r in range(3*k):
    e.append((2*r+2)*(2*r+1)*e[-1]+2*r*(r+1))
c=[e[r]+(1-(-1)**r)//2 for r in range(len(e))]
f=[math.factorial(2*r) for r in range(3*k+2)]
km=[-L*(f[r]+f[r+1])+4*(L//(2*r+1)) for r in range(3*k-2)]
W=s.Matrix([[c[i+j] for j in range(n)] for i in range(k)]+[[km[i+j] for j in range(n)] for i in range(k-1)])
# Exact characteristic-zero nullspace over ZZ, with no modular-kernel assumption.
N=DomainMatrix.from_Matrix(W).nullspace().to_Matrix()
assert N.rows==1
raw=[int(x) for x in N.row(0)]
graw=reduce(math.gcd,map(abs,raw))
q=[x//graw for x in raw]
if q[-1]<0:q=[-x for x in q]
assert reduce(math.gcd,map(abs,q))==1
assert W*s.Matrix(q)==s.zeros(53,1)
# Independent moment generation from the ordinary derangement recurrence.
D=[1,0]
for m in range(2,6*k+1):D.append((m-1)*(D[-1]+D[-2]))
assert all(sum((D[2*(i+j)]-(-1)**(i+j))*q[j] for j in range(n))==0 for i in range(k))
assert all(sum(Fraction(-(math.factorial(2*(i+j))+math.factorial(2*(i+j)+2)),1)*q[j]+Fraction(4*q[j],2*(i+j)+1) for j in range(n))==0 for i in range(k-1))
# Convert this actual polynomial, not the conversion operator as an experiment.
B=[[0]*n for _ in range(n)]
for j in range(n):
    for r in range(j+1):B[r][j]=(-1)**(j-r)*math.comb(2*j,j-r)*math.comb(2*j+2*r,2*j)
alpha=[Fraction(0) for _ in range(n)]
for j in reversed(range(n)):
    alpha[j]=(q[j]-sum(B[j][h]*alpha[h] for h in range(j+1,n)))/B[j][j]
assert all(sum(B[i][j]*alpha[j] for j in range(n))==q[i] for i in range(n))
# Independent exact extraction through the compact moment formula.
alpha2=[]
for j in range(n):
    integ=sum(Fraction(q[i]*B[r][j],2*(i+r)+1) for i in range(n) for r in range(j+1))
    alpha2.append(Fraction(4*j+1,16**j)*integ)
assert alpha==alpha2
clear=math.lcm(*(a.denominator for a in alpha))
zraw=[int(a*clear) for a in alpha]
zg=reduce(math.gcd,map(abs,zraw)); z=[x//zg for x in zraw]
assert zg==1
zeta=reduce(math.gcd,map(abs,z[:k-1]))
Delta=math.prod(B[j][j] for j in range(n))
v=[int(Delta*a) for a in alpha]
theta=reduce(math.gcd,map(abs,v)); Lambda=reduce(math.gcd,map(abs,v[:k-1]))
assert Lambda==theta*zeta and Delta%theta==0

def vp(x):
    if isinstance(x,Fraction):return vp(x.numerator)-vp(x.denominator)
    x=abs(int(x))
    if x==0:return None
    ans=0
    while x%3==0:ans+=1;x//=3
    return ans
endpoint=sum((-1)**j*q[j] for j in range(n))
receipt={'k':k,'matrix_shape':[53,54],'kernel_dimension_Q':int(N.rows),'rank_Q':53,'full_integer_residual_zero':True,'independent_derangement_and_rational_lower_residual_zero':True,'monomial_gcd':1,'leading_sign_positive':q[-1]>0,'raw_nullvector_content_v3':vp(graw),'max_coefficient_bits':max(abs(x).bit_length() for x in q),'v3_linear':vp(q[1]),'v3_endpoint':vp(endpoint),'v3_alpha':[vp(x) for x in alpha],'conversion_depth':-min(vp(x) for x in alpha if x),'v3_zeta_W':vp(zeta),'v3_Delta54':vp(Delta),'v3_theta_L':vp(theta),'v3_Lambda_for_Q0':vp(Lambda),'legendre_clearer':str(clear),'primitive_legendre_gcd':reduce(math.gcd,map(abs,z)),'independent_exact_legendre_reconstruction':True,'seconds':time.time()-start}
with open('ACTUAL_KERNEL_K27_VECTOR.json','w') as h:json.dump({'coefficient_order':'ascending monomial powers','Q0':[str(x) for x in q],'z_primitive':[str(x) for x in z],'alpha':[str(x) for x in alpha],'raw_nullvector_content':str(graw)},h)
with open('ACTUAL_KERNEL_K27_RECEIPT.json','w') as h:json.dump(receipt,h,indent=2)
print(json.dumps(receipt,indent=2))
