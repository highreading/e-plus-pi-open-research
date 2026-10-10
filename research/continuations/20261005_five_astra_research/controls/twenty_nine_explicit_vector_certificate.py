"""Coordinator comparison of explicit finite formulas with independent kernel values."""
import json,math,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
ROOT=Path(__file__).resolve().parent
old=json.loads((ROOT/'twenty_nine_kernel_control.json').read_text())
p=29;nbar=20387;n=old['n']
alpha=[]
for i in range(29):
    ci=(-1)**i*math.factorial(i)
    harmonic=sum(pow(s,-1,p) for s in range(1,i+1))%p
    ei=sum(math.comb(i,t)*7*(8*pow(20,t,p)-20*pow(8,t,p))*pow(12*t,-1,p)
           for t in range(1,i+1))%p
    vi=sum((pow(21,s,p)+pow(9,s,p))*pow(s,-1,p) for s in range(1,i+1))%p
    alpha.append((ci+p*((ci%p)*(7*harmonic+ei+7*vi)+(i==27)-7*(i==28)))%p**2)
alpha += [p*(6*(-1)**r*math.factorial(r)%p) for r in range(29)]
assert alpha==old['hA_newton_mod841']
ds=[1,(-nbar)%p**3]
for s in range(1,59):
    ds.append(((s-nbar)*ds[s]+s*(nbar-(s-1)*pow(2,-1,p**3))*ds[s-1])%p**3)
assert ds[1:59]==old['contact_d_s1_to58_mod24389']
assert ds[59]==0
beta=[]
for i in range(58):
    value=(-1)**(i+1)*((2-2*nbar)*ds[i+1]*math.comb(nbar+i,i+1)
                     +(-1+2*nbar)*ds[i+2]*math.comb(nbar+i,i+2))
    value-=p**2*({27:23,28:12,56:18,57:7}.get(i,0))
    beta.append(value%p**3)
assert beta==old['hQ_newton_mod24389']
def choose(a,k):
    if k<0:return 0
    if a>=0:return math.comb(a,k) if k<=a else 0
    return (-1)**k*math.comb(k-a-1,k)
high_checks=0
for coeff,modulus in [(alpha,p**2),(beta,p**3)]:
    at=[choose(2*n+t-1,t)%modulus for t in range(58)]
    def st(t,x):return sum(coeff[i]*choose(x,i-t) for i in range(t,58))%modulus
    for q in range(31,59):
        for x in range(59):
            value=at[q-1]*(st(q-1,x)+x*st(q-1,x-1))
            if q<58:value+=at[q]*x*st(q,x-1)
            assert value%modulus==0
            high_checks+=1
report={'status':'PASS','explicit_hA_matches_all58_entries':True,
        'explicit_hQ_matches_all58_entries':True,'contact_recurrence_matches_all58_entries':True,
        'high_laurent_zero_evaluations':high_checks,'max_polynomial_degree_for_zero_check':58,
        'positive_laurent_support':[0,30],
        'scope':'Exact bounded Newton coefficient and polynomial zero certificates at the fixed representative; RC constants and Gamma0 are not evaluated.'}
(ROOT/'twenty_nine_explicit_vector_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
