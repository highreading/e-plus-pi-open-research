from pathlib import Path
from math import factorial,comb
import json
from b4_finite_criterion import state,plus_coeffs,det
from residue_atlas import coeffs
from exact_local_probe import mm,mv
BASE=Path(__file__).parent

def conv(a,b,limit,p):
 c=[0]*(limit+1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):
   if i+j<=limit:c[i+j]=(c[i+j]+x*y)%p
 return c

def inverse_series(q,limit,p):
 assert q[0]%p==1
 a=[1]
 for k in range(1,limit+1):a.append(-sum(q[j]*a[k-j] for j in range(1,min(k,len(q)-1)+1))%p)
 return a

def solve_lower(T,v,p):
 x=[]
 for l,row in enumerate(T):x.append((v[l]-sum(row[j]*x[j] for j in range(l)))*pow(row[l],-1,p)%p)
 return x

def chart(p,b,m,h):
 assert p>b and 1<=h<=min(m+1,b-m-2)
 d=b-h;M=m+1-h;limit=p+d-1
 inv2=pow(2,-1,p);q=[1,-1,inv2];qh=[1]
 for _ in range(h):qh=conv(qh,q,len(qh)+1,p)
 alpha=inverse_series(qh,limit,p)
 invq=inverse_series(q,d,p)
 logarithm=[0]+[((-invq[j-1]+(invq[j-2] if j>=2 else 0))*pow(j,-1,p))%p for j in range(1,d)]
 adot=conv(alpha[:d],logarithm,d-1,p)
 Dc=[1]
 for j in range(1,p):Dc.append((j*Dc[-1]+1)%p)
 g=[2*Dc[p-1]%p]
 for j in range(1,d):g.append((j*g[-1]+2*Dc[j-1])%p)
 T=[];G=[];F=[]
 for l in range(d):
  f0=[1];f1=[0]
  for j in range(p+l):
   f1.append((f1[-1]*(l-j)+f0[-1])%p)
   f0.append(f0[-1]*(l-j)%p)
  tr=[];gr=[]
  for j in range(b):
   gr.append(sum(alpha[s]*f1[j+s]+(adot[s]*f0[j+s] if s<d else 0) for s in range(max(0,p+l-j+1)))%p)
   tr.append(sum(alpha[s]*f0[j+s] for s in range(max(0,l-j+1)))%p)
  ff=0
  for s in range(p+l+1):
   offset=l-h-s;base=Dc[offset%p]
   ff+=alpha[s]*f1[s]*base
   if s<=l:
    ff+=adot[s]*f0[s]*base
    if offset>=0:ff+=alpha[s]*f0[s]*g[offset]
  T.append(tr);G.append(gr);F.append(ff%p)
 r=p-h;seed=state(r,p,b,m,coeffs(r),plus_coeffs(r));N=seed['N'];A=seed['A'];J=seed['J'];P=J[0]
 assert P and N[h:]==T
 Delta=det(N,p)
 invP=pow(P,-1,p);Ybar=[v*invP%p for v in seed['Y']]
 assert Ybar[:d]==[0]*d
 from b4_finite_criterion import adj
 Bbar=[v%p for v in mv(adj(N,p),A)]
 I=[[int(i==j) for j in range(b)] for i in range(b)]
 Dpol=[[j if j==i+1 else 0 for j in range(b)] for i in range(b)]
 U=[[I[i][j]+Dpol[i][j] for j in range(b)] for i in range(b)]
 Upow=I
 for _ in range(h):Upow=mm(Upow,U)
 Z=[[0]*b for _ in range(b+1)]
 for j in range(b):Z[j][j]=-1;Z[j+1][j]=1
 K0=[[v%p for v in row] for row in mm(Z,Upow)]
 L=[[0]*b for _ in range(b)]
 Dpow=I
 for k in range(1,b):
  Dpow=mm(Dpow,Dpol);factor=(-1)**(k+1)*pow(k,-1,p)
  for i in range(b):
   for j in range(b):L[i][j]=(L[i][j]+factor*Dpow[i][j])%p
 K1=[[-v%p for v in row] for row in mm(K0,L)]
 S=[(-1)**(h-1)*factorial(h-1)*factorial(l)*J[h+l]*invP%p for l in range(d)]
 GY=mv(G,Ybar);GB=mv(G,Bbar)
 yl=solve_lower([row[:d] for row in T],[(Delta*S[l]-GY[l])%p for l in range(d)],p)
 bl=solve_lower([row[:d] for row in T],[(Delta*F[l]-GB[l])%p for l in range(d)],p)
 xbar=[v%p for v in mv(K0,Ybar)];tbar=[v%p for v in mv(K0,Bbar)]
 X=[(sum(K0[j][i]*yl[i] for i in range(d))+sum(K1[j][i]*Ybar[i] for i in range(b)))%p for j in range(M+1)]
 Tc=[(sum(K0[j][i]*bl[i] for i in range(d))+sum(K1[j][i]*Bbar[i] for i in range(b)))%p for j in range(M+1)]
 assert xbar[:M+1]==[0]*(M+1)
 assert (tbar[0]+Delta)%p==0 and tbar[1:M+1]==[0]*M
 low_weights=[];v=1
 for j in range(M+1):
  if j:v*=M+1-j
  low_weights.append(v*v%p)
 high_weights=[(factorial(M)*factorial(j-M-1))**2%p for j in range(M+1,b+1)]
 delta=(sum(w*x*x for w,x in zip(low_weights,X))+sum(w*x*x for w,x in zip(high_weights,xbar[M+1:])))%p
 nu=(sum(w*x*t for w,x,t in zip(low_weights,X,Tc))+sum(w*x*t for w,x,t in zip(high_weights,xbar[M+1:],tbar[M+1:])))%p
 return dict(p=p,b=b,m=m,h=h,delta=delta,nu=nu,seed_n=r,Delta=Delta,P=P,T=T,G=G,F=F,Ybar=Ybar,Bbar=Bbar,S=S,y_lower=yl,b_lower=bl,X=X,Tc=Tc,xbar=xbar,tbar=tbar,low_weights=low_weights,high_weights=high_weights)

if __name__=='__main__':
 expected=[]
 for r in json.loads((BASE/'b4_boundary_constants.json').read_text()):expected.append((r['p'],4,1,1,r['delta'],r['nu']))
 for r in json.loads((BASE/'H2_BOUNDARY_REFERENCE_CERTIFICATE.json').read_text())['references']:expected.append((r['p'],5,1,2,r['delta'],r['nu']))
 r=json.loads((BASE/'general_h_reference.json').read_text());expected.append((r['p'],r['b'],r['m'],r['h'],r['delta'],r['nu']))
 out=[]
 for p,b,m,h,dd,vv in expected:
  result=chart(p,b,m,h)
  assert (result['delta'],result['nu'])==(dd,vv),(p,b,m,h,result['delta'],result['nu'],dd,vv)
  out.append(result);print(p,b,m,h,dd,vv,flush=True)
 (BASE/'FINITE_BOUNDARY_CHART_RECEIPT.json').write_text(json.dumps(dict(status='author exact finite formula verification against eight own reference states; not independent review',rows=out),indent=2))
