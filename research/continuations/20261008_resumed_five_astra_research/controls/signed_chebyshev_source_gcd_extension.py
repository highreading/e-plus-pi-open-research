"""NEW source-only gcd diagnostic N13..80, without repeating normalization/q."""
from pathlib import Path
from math import gcd
import json,hashlib
P=Path(__file__).resolve().parent
def add(a,b):return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def scale(a,c):return [x*c for x in a]
def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z
def ei(a):return (sum(x*(-1)**(j//2) for j,x in enumerate(a) if j%2==0),sum(x*(-1)**(j//2) for j,x in enumerate(a) if j%2))
cs=[[1],[-1,2]]
for j in range(1,80):cs.append(add(mul([-2,4],cs[-1]),scale(cs[-2],-1)))
mom=[1]
for j in range(1,161):mom.append(1-j*mom[-1])
def eta(a):return sum(x*mom[j] for j,x in enumerate(a))
S=[1,-1,9,-113]
for j in range(2,159):S.append(8-12*S[j+1]-(14-16*j*j)*S[j]-12*S[j-1]-S[j-2])
assert len(S)==161
k=[0,1,-1,2,-2,1,-1]
assert eta(k)==-332
rows=[]
for N in range(13,81):
    an,bn=ei(cs[N]);am,bm=ei(cs[N-1]);d=an*bm-am*bn
    B=add(scale(cs[N],bm),scale(cs[N-1],-bn));F=mul(B,B)
    I=eta(F)
    assert 2*I==bm*bm*(1+S[2*N])+bn*bn*(1+S[2*N-2])-2*bm*bn*(S[2*N-1]+S[1])
    K=mul(k,mul(cs[N-3],cs[N-3]));U=-eta(K);V=I-d*d
    assert U>0 and V>0 and U%4==V%4==0
    g=gcd(U,V)
    rows.append({'N':N,'U':U,'I':I,'d':d,'V':V,'gcd_U_V':g,'residual_after4':g//4})
out={'checks_passed':True,'scope':'NEW source-only N13..80. Does NOT recompute primitive content, affine clearer or q and does NOT establish a uniform gcd theorem.',
     'degree_max':160,'source_factorial_max':160,'network_or_keys_used':False,
     'rows':rows,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'signed_chebyshev_source_gcd_extension_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checks_passed':True,'scope':out['scope'],
    'exceptions_to_gcd4':[{'N':r['N'],'gcd_U_V':r['gcd_U_V']} for r in rows if r['gcd_U_V']!=4],
    'row_count':len(rows)}))
