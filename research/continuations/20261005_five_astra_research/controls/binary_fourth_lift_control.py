"""Coordinator-authored higher finite lift and global polynomial certificates."""
import math,json,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
out=Path(__file__).resolve().parent
n,b,mod=2,81,64
cs=(-1,2,-3,3)
def choose(x,k):
    if k<0:return 0
    if x>=0:return math.comb(x,k) if k<=x else 0
    return (-1)**k*math.comb(k-x-1,k)
E=[[sum(cs[s-1]*sum(choose(i,s-v)*choose(n,v)*choose(-v,j-i+s-v)
    for v in range(min(s,n)+1)) for s in range(1,5))%mod for j in range(b)] for i in range(b)]
def newton(values,precision):
    coeff=[]
    while values:
        coeff.append(values[0]%precision)
        values=[(values[i+1]-values[i])%precision for i in range(len(values)-1)]
    return coeff
def inverse(coeff,weight,precision):
    term=[(-1)**i*sum(c*choose(i,k) for k,c in enumerate(coeff))%mod for i in range(b)]
    result=[0]*b
    for depth in range(5):
        result=[(r+weight*(-2)**depth*t)%precision for r,t in zip(result,term)]
        term=[sum(a*c for a,c in zip(row,term))%mod for row in E]
    return newton([(-1)**i*r%precision for i,r in enumerate(result)],precision)
p=inverse((2,-9,19,-25,12,-4,16,-16),1,32)
q=inverse((10,2,24,15),2,64)
assert not any(p[22:]) and not any(q[20:])
old=json.loads((out/'binary_fixed_lift_control.json').read_text())
assert [v%16 for v in p[:18]]==old['P_newton_mod16'] and not any(v%16 for v in p[18:])
assert [v%32 for v in q[:16]]==old['Q_newton_mod32'] and not any(v%32 for v in q[16:])
d=[(q[i]-2*p[i])%64 for i in range(22)]
B=(5,42,54,56,56,16,48)
f=[1]
for a in range(1,7):f.append(f[-1]*(81+a)%64)
assert f==[1,18,22,56,24,16,48]
actualB=[sum(f[u]*choose(132,u-a) for u in range(a,7))%64 for a in range(7)]
assert actualB==list(B)
def K(L):
    return (sum((-1)**a*ba*choose(L+a+4,3) for a,ba in enumerate(B))+
        sum(dr*choose(r+3,3)*choose(L+4,r+4) for r,dr in enumerate(d)))%64
# K has degree at most25. Newton certificates of compositions/translated
# differences give identities for all integer inputs, not sample extrapolation.
cert4=newton([K(4*s)%4 for s in range(26)],4)
certper=newton([(K(16*s+64)-K(16*s))%64 for s in range(26)],64)
cert16=newton([(K(16*s)-16)%32 for s in range(26)],32)
assert not any(cert4) and not any(certper) and not any(cert16)
assert K(16)%16==0 and (K(16)//16)%2==1
report={'reference_n':n,'reference_b':b,'P_newton_mod32':p[:22],
'Q_newton_mod64':q[:20],'difference_newton_mod64':d,
'factorial_residues_mod64':f,'boundary_values_mod64':actualB,
'degree_bounds':[21,19],'reductions_to_previous_lift_pass':True,
'K16':K(16),'K16_div16_mod4':K(16)//16,
'Newton_certificate_K4s_mod4':cert4,
'Newton_certificate_K16s_minus16_mod32':cert16,
'Newton_certificate_K16s_plus64_minus_K16s_mod64':certper,
'fixed_polynomial_identities_certified':True,
'original_large_convolution_not_evaluated':True,'finite_operator_lift_only':True}
(out/'binary_fourth_lift_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
