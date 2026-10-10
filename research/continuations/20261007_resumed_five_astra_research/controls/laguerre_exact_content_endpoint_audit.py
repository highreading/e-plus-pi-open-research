"""One NEW auxiliary instance independently checks the exact-content theorem."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial as fac, comb, gcd, lcm
from functools import reduce
import json

n,b=13,3
d=b-1
h=n-d
prime=11
assert (h,d)==(11,2)
mu=[sum((-1)**(d-j)*comb(d,j)*fac(i+b+j) for j in range(d+1))
    for i in range(2*h)]
assert b+(2*h-1)+d==26
matrix=[[Q(mu[i+j]) for j in range(h)]+[Q(-mu[h+i])]
        for i in range(h)]
for j in range(h):
    pivot=next(i for i in range(j,h) if matrix[i][j])
    matrix[j],matrix[pivot]=matrix[pivot],matrix[j]
    v=matrix[j][j]
    matrix[j]=[x/v for x in matrix[j]]
    for i in range(h):
        if i==j:continue
        v=matrix[i][j]
        matrix[i]=[x-v*y for x,y in zip(matrix[i],matrix[j])]
ph=[row[-1] for row in matrix]+[Q(1)]
assert all(sum(ph[j]*mu[i+j] for j in range(h+1))==0 for i in range(h))
a=lcm(*(c.denominator for c in ph))
r=[0]*(n+1)
for i,c in enumerate(ph):
    for j in range(d+1):
        r[i+j]+=int(c*a)*(-1)**(d-j)*comb(d,j)
assert r[-1]==a and reduce(gcd,map(abs,r))==1
gamma=[]
for j in range(b):
    gamma.append((-1)**(n-j)*fac(n-j)*r[n-j]
                 -sum(comb(n+1,j-i)*gamma[i] for i in range(j)))
# Verify the complete expansion in all14 coefficients, not only its top3.
assert all(Q(r[k])==sum((Q(gamma[j]*(-1)**k*comb(n+1,n-j-k),fac(k))
                        if 0<=n-j-k<=n+1 else Q(0))
                       for j in range(b)) for k in range(n+1))
w=[comb(n,j)*gamma[j] for j in range(b)]
F=sum(r[k]*fac(k) for k in range(n+1))
E=sum(r[k]*sum(fac(k)//fac(v) for v in range(k+1)) for k in range(n+1))
B=[4*sum((Q((-1)**v,2*v+1) for v in range(2*j)),Q(0)) for j in range(b)]
T=sum((w[j]*B[j] for j in range(b)),Q(0))
c=Q(4,4*n+1)
R=Q(0)
for k in range(n+1):
    R+=abs(r[k])*c
    if k<n:c*=Q((k+1)*(4*k+3),4*n-4*k-3)
assert sum(w)==F
assert R==4*(-1)**n*sum((Q(w[j],4*j+1) for j in range(b)),Q(0))
assert T.denominator==R.denominator==1
T=int(T);R=int(R)
g=gcd(abs(F),abs(E+T))
q=abs(F)//g
expected=[0]*h+[a,-2*a,a]
assert all((x-y)%prime==0 for x,y in zip(r,expected))
assert gcd(a,h)==1
assert reduce(gcd,map(abs,gamma))==fac(h)==39916800
assert E%fac(d)==0 and (E//fac(d)-a)%prime==0
assert F%prime==T%prime==0 and g%prime!=0 and q%prime==0

result={'status':'PASS','scope':'One auxiliary (n,b)=(13,3) instance, NOT an '
        'original n=2001b or admissible gigantic-b asymptotic certificate.',
        'largest_factorial_input':26,'maximum_linear_system_dimension':11,
        'monic_least_clearer':a,'r':r,'gamma':gamma,'w':w,
        'exact_gamma_content':reduce(gcd,map(abs,gamma)),
        'F':F,'E':E,'T':T,'positive_integer_R':R,'final_all_prime_g':g,
        'primitive_q':q,'E_over_d_factorial_mod11':(E//fac(d))%prime,
        'least_clearer_mod11':a%prime,'g_mod11':g%prime,'q_mod11':q%prime,
        'all14_expansion_coefficients_checked':True,
        'repeated_contact_and_primitive_content_retained':True,
        'network_and_credential_access':False}
Path(__file__).with_name('laguerre_exact_content_endpoint_certificate.json').write_text(
    json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('status','exact_gamma_content',
  'E_over_d_factorial_mod11','least_clearer_mod11','g_mod11','q_mod11')}))
