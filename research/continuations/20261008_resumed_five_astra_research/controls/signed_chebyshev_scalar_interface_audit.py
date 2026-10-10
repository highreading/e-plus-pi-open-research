"""New bounded scalar/interface checks, reusing the closed normalization receipt."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial,gcd,lcm
import json,hashlib
P=Path(__file__).resolve().parent
src=P/'signed_chebyshev_normalization_certificate.json'
data=json.loads(src.read_text())
def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z
def quotient(a,target):
    a=a[:];a[0]-=target;s=[0]*(len(a)-2)
    for j in range(len(a)-1,1,-1):
        s[j-2]=a[j];a[j-2]-=a[j];a[j]=0
    assert all(x==0 for x in a)
    return s
def endpoint(a):return sum(x*(-1)**j*factorial(j) for j,x in enumerate(a))
def integral(a):return sum((Q(x,j+1) for j,x in enumerate(a)),Q(0))
rows=[]
for old in data['records']:
    N=old['N'];U,I,d=old['U'],old['I'],old['d'];V=I-d*d
    F=mul(old['B'],old['B']);K=old['K'];L=lcm(*range(1,2*N))
    RF=endpoint(F)-4*integral(quotient(F,d*d))
    RK=endpoint(K)-4*integral(quotient(K,0))
    X,Y=L*RF,L*RK;assert X.denominator==Y.denominator==1
    X,Y=int(X),int(Y)
    Araw,Braw=U*X+V*Y,L*U*d*d;C=gcd(Braw,Araw)
    assert Araw//C==old['p'] and Braw//C==old['q']
    assert C==(L//old['lambda'])*old['h']*old['final_G']
    g=gcd(U,V);hp=old['h']//g;assert old['h']%g==0
    delta=0
    for i in range(len(F)):
        for j in range(i+1,len(F)):
            delta=gcd(delta,F[i]*K[j]-F[j]*K[i])
    assert delta>0 and delta%hp==0
    surviving=U//gcd(U,V*Y);assert old['q']%surviving==0
    assert gcd(U,V*Y)<=gcd(U,V)*gcd(U,Y)
    rows.append({'N':N,'L':L,'X':X,'Y':Y,'raw_A':Araw,'raw_B':Braw,
                 'raw_pair_gcd':C,'gcd_U_V':g,'gcd_U_Y':gcd(U,Y),
                 'coefficient_delta2':delta,'h_over_g':hp,
                 'actual_q_surviving_divisor':surviving,'q_from_closed_receipt':old['q']})

# Independent direct polynomial moments for the newly proposed forced recurrence.
cs=[[1],[-1,2]]
for j in range(1,40):
    nxt=[0]*(len(cs[-1])+1)
    for r,x in enumerate(cs[-1]):nxt[r]-=2*x;nxt[r+1]+=4*x
    for r,x in enumerate(cs[-2]):nxt[r]-=x
    cs.append(nxt)
mom=[1]
for j in range(1,41):mom.append(1-j*mom[-1])
S=[sum(x*mom[j] for j,x in enumerate(c)) for c in cs]
E=[endpoint(c) for c in cs]
for j in range(2,39):
    assert S[j+2]+12*S[j+1]+(14-16*j*j)*S[j]+12*S[j-1]+S[j-2]==8
    assert E[j+2]+12*E[j+1]+(14-16*j*j)*E[j]+12*E[j-1]+E[j-2]==-8*(-1)**j
for j in range(37):assert gcd(*S[j:j+5])==gcd(*E[j:j+5])==1
for r in data['records']:
    N=r['N'];bn=sum(x*(-1)**(j//2) for j,x in enumerate(r['C_N']) if j%2)
    bm=sum(x*(-1)**(j//2) for j,x in enumerate(r['C_Nminus1']) if j%2)
    assert 2*r['I']==bm*bm*(1+S[2*N])+bn*bn*(1+S[2*N-2])-2*bm*bn*(S[2*N-1]+S[1])
out={'all_checks_passed':True,'source_receipt_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
     'scope':'New scalar/endpoint/content interfaces N3..12 from CLOSED normalization receipt; direct forced-recurrence check j2..38 only. Uniform statements require the separate analytic proof.',
     'network_or_keys_used':False,'normalization_receipt_recomputed':False,
     'rows':rows,'new_recurrence_diagnostic':{'S0_through_S8':S[:9],'E0_through_E8':E[:9],
       'range_j':[2,38],'five_term_gcd_checks':[0,36]},
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'signed_chebyshev_scalar_interface_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checks':True,'rows':[{'N':r['N'],'gcd_U_V':r['gcd_U_V'],'gcd_U_Y':r['gcd_U_Y'],
    'delta2':r['coefficient_delta2'],'surviving_digits':len(str(r['actual_q_surviving_divisor']))} for r in rows],
    'S0_8':S[:9],'E0_8':E[:9]},indent=2))
