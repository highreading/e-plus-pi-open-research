from pathlib import Path
from fractions import Fraction as F
from math import factorial
import json
ROOT=Path(__file__).parent
# One structural normalization witness, not a prime/degree atlas.
k,p=4,17;h=(p+1)//2;t=3*k-1-h;m=k-t
D=[1]
for r in range(1,6*k):D.append(r*D[-1]+(-1)**r)
def rat(r):return -F(factorial(2*r))+4*sum((F((-1)**(r-a),2*a-1) for a in range(1,r+1)),F(0))
def mod(x):return x.numerator*pow(x.denominator,-1,p)%p if isinstance(x,F) else x%p
def detmod(a):
 a=[list(map(mod,row)) for row in a];ans=1
 for j in range(len(a)):
  q=next((i for i in range(j,len(a)) if a[i][j]),None)
  if q is None:return 0
  if q!=j:a[q],a[j]=a[j],a[q];ans=-ans
  v=a[j][j];ans=ans*v%p;iv=pow(v,-1,p)
  for i in range(j+1,len(a)):
   fac=a[i][j]*iv%p
   for s in range(j,len(a)):a[i][s]=(a[i][s]-fac*a[j][s])%p
 return ans%p
N=2*k-t
C=[[D[2*(i+j)]-(-1)**(i+j) for j in range(N)] for i in range(k)]
R=[[rat(i+j) for j in range(N)] for i in range(m)]
V=[[(-1)**(i+j) for j in range(N)] for i in range(m)]
A=detmod(C+R);B=(detmod(C+[[R[i][j]+V[i][j] for j in range(N)] for i in range(m)])-A)%p
source=json.loads((ROOT.parent/'main/SHORT_PAIRED_KERNEL_CERTIFICATE.json').read_text())
row=next(r for r in source['rows'] if r['k']==k)
# Retain source shape in this bounded receipt; final-q lookup is adapted below.
print('LEADING_COMPLEMENT',k,p,'t',t,'A',A,'B',B,flush=True)
print('SOURCE_KEYS',list(row),flush=True)
(ROOT/'SHORT_STACK_LAURENT_RECEIPT.json').write_text(json.dumps({'k':k,'p':p,'h':h,'t':t,'complement_width':N,'leading_complement_constant_mod_p':A,'leading_complement_S_mod_p':B,'scope':'One structurally chosen leading/minor normalization witness; no prime atlas.'},indent=2)+'\n')
actualq=int(row['actual_q']);assert actualq%p!=0
record=json.loads((ROOT/'SHORT_STACK_LAURENT_RECEIPT.json').read_text())
record['full_actual_q_mod_p']=actualq%p
record['full_primitive_q_p_valuation']=0
record['basis_invariant_full_q_reference']='main/SHORT_PAIRED_KERNEL_CERTIFICATE.json'
(ROOT/'SHORT_STACK_LAURENT_RECEIPT.json').write_text(json.dumps(record,indent=2)+'\n')
Dsmall=[[D[2*(i+j)] for j in range(N)] for i in range(k)]
K=[[ -F(factorial(2*(i+j)))-F(factorial(2*(i+j)+2))+F(4,2*(i+j)+1) for j in range(N)] for i in range(m-1)]
B_reduced=detmod(Dsmall+[[(-1)**j for j in range(N)]]+K)
assert B_reduced==B
# Leading coefficient of z-polynomial by t-th finite differences, degree<=t.
Cfull=[[D[2*(i+j)]-(-1)**(i+j) for j in range(2*k)] for i in range(k)]
E=[[4*(-1)**(i+j-h) if i+j>=h else 0 for j in range(2*k)] for i in range(k)]
Rreg=[[rat(i+j)-F(E[i][j],p) for j in range(2*k)] for i in range(k)]
from math import comb
sigma=(-1)**(t*(t-1)//2)*pow(4,t,p)%p
for outi in [0,1]:
 vals=[]
 for zz in range(t+1):
  block=[[Rreg[i][j]+zz*E[i][j] for j in range(2*k)] for i in range(k)]
  constant=detmod(Cfull+block)
  if outi:
   vblock=[[block[i][j]+(-1)**(i+j) for j in range(2*k)] for i in range(k)]
   constant=(detmod(Cfull+vblock)-constant)%p
  vals.append(constant)
 lead=sum((-1)**(t-j)*comb(t,j)*vals[j] for j in range(t+1))*pow(factorial(t),-1,p)%p
 assert lead==sigma*([A,B][outi])%p
record=json.loads((ROOT/'SHORT_STACK_LAURENT_RECEIPT.json').read_text())
record['response_minor_reduction_verified']=True
record['full_laurent_polynomial_leading_coefficient_verified']=True
(ROOT/'SHORT_STACK_LAURENT_RECEIPT.json').write_text(json.dumps(record,indent=2)+'\n')
