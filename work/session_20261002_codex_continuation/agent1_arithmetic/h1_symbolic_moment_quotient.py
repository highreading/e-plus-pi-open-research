"""Exact h1 corrected local quotient polynomial, without numerical interpolation."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
from boundary_moment_quotient import endpoint_fixed
from exact_local_probe import mm,mv

BASE=Path(__file__).resolve().parent
NAMES=['mu0','mu1','lambda0','lambda1','C']
ZERO=(0,)*len(NAMES)


class P:
    def __init__(self,x=0):
        self.d={k:Q(v) for k,v in x.items() if v} if isinstance(x,dict) else ({ZERO:Q(x)} if x else {})
    def __add__(self,x):
        x=x if isinstance(x,P) else P(x);d=self.d.copy()
        for k,v in x.d.items():d[k]=d.get(k,Q(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self):return P({k:-v for k,v in self.d.items()})
    def __sub__(self,x):return self+-x if isinstance(x,P) else self+P(-x)
    def __rsub__(self,x):return -self+x
    def __mul__(self,x):
        x=x if isinstance(x,P) else P(x);d={}
        for a,v in self.d.items():
            for b,w in x.d.items():
                k=tuple(i+j for i,j in zip(a,b));d[k]=d.get(k,Q(0))+v*w
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,q):return self*Q(1,q)
    def __pow__(self,n):
        result=P(1)
        for _ in range(n):result=result*self
        return result
    def evaluate(self,values):
        return sum((v*product(Q(x)**k for x,k in zip(values,a)) for a,v in self.d.items()),Q(0))
    def output(self):
        return [dict(powers=dict(zip(NAMES,k)),coefficient=str(v)) for k,v in sorted(self.d.items())]


def product(values):
    result=Q(1)
    for v in values:result*=v
    return result
def var(j):
    k=list(ZERO);k[j]=1;return P({tuple(k):1})
def solve(T,rhs):
    x=[]
    for l,row in enumerate(T):x.append((rhs[l]-sum(row[j]*x[j] for j in range(l)))/row[l])
    return x


def symbolic(b,m,chi):
    h=1;d=b-1;M=m
    mu={0:var(0),1:var(1)};lam={0:var(2),1:var(3)};C=var(4)
    Dneg={1:C}
    for j in range(1,2*b):Dneg[j+1]=(1-Dneg[j])/j
    Dpos=[1]
    for j in range(1,b):Dpos.append(j*Dpos[-1]+1)
    def Dc(j):return P(Dpos[j]) if j>=0 else Dneg[-j]
    for c in range(1,1-d-1,-1):
        forcing=P((-1)**(-c)*factorial(-c)) if c<=0 else P(0)
        mu[c-2]=2*(forcing-mu[c]+mu[c-1])
        lforce=forcing*Dc(c-2)
        lam[c-2]=2*(lforce-lam[c]+lam[c-1])
    for c in range(2,d+1):
        mu[c]=mu[c-1]-mu[c-2]/2
        lam[c]=lam[c-1]-lam[c-2]/2
    alpha=[Q(1)]
    for s in range(1,b):alpha.append(alpha[-1]-(alpha[-2]/2 if s>=2 else 0))
    log=[Q(0)]+[(-alpha[j-1]+(alpha[j-2] if j>=2 else 0))/j for j in range(1,b)]
    adot=[sum(alpha[j]*log[s-j] for j in range(s+1)) for s in range(b)]
    J=endpoint_fixed(1,b,chi);Pseed=J[0]
    Ntop=[mu[-j] for j in range(b)]
    tau=product(factorial(l) for l in range(d));scale=(-1)**d*tau
    Delta=scale*Ntop[-1];Ybar=[P(0)]*d+[P(scale)]
    T=[];Alower=[];G=[];F=[]
    g=[2*C]
    for j in range(1,d):g.append(j*g[-1]+2*Dpos[j-1])
    for l in range(d):
        f0=[Q(1)];f1=[Q(0)]
        for v in range(l):
            f1.append(f1[-1]*(l-v)+f0[-1]);f0.append(f0[-1]*(l-v))
        T.append([sum(alpha[s]*f0[j+s] for s in range(max(0,l-j+1))) for j in range(b)])
        G.append([factorial(l)*mu[l+1-j]+sum(alpha[s]*f1[j+s]+adot[s]*f0[j+s] for s in range(max(0,l-j+1))) for j in range(b)])
        Alower.append(sum(alpha[s]*f0[s]*Dc(l-1-s) for s in range(l+1)))
        short=sum((alpha[s]*f1[s]+adot[s]*f0[s])*Dc(l-1-s) for s in range(l+1))
        short+=sum(alpha[s]*f0[s]*g[l-1-s] for s in range(max(0,l)))
        F.append(factorial(l)*lam[l+1]+short)
    b0=solve([row[:d] for row in T],Alower)
    Bbar=[Delta*v for v in b0]+[scale*(lam[0]-sum(Ntop[j]*b0[j] for j in range(d)))]
    Dpol=[[j if j==i+1 else 0 for j in range(b)] for i in range(b)]
    U=[[int(i==j)+Dpol[i][j] for j in range(b)] for i in range(b)]
    Z=[[0]*b for _ in range(b+1)]
    for j in range(b):Z[j][j]=-1;Z[j+1][j]=1
    K0=mm(Z,U)
    L=[[Q(0)]*b for _ in range(b)];Dp=[[int(i==j) for j in range(b)] for i in range(b)]
    for k in range(1,b):
        Dp=mm(Dp,Dpol)
        for i in range(b):
            for j in range(b):L[i][j]+=Q((-1)**(k+1),k)*Dp[i][j]
    K1=[[-v for v in row] for row in mm(K0,L)]
    S=[Q(factorial(l))*J[1+l]/Pseed for l in range(d)]
    GY=mv(G,Ybar);GB=mv(G,Bbar)
    yl=solve([row[:d] for row in T],[Delta*S[l]-GY[l] for l in range(d)])
    bl=solve([row[:d] for row in T],[Delta*F[l]-GB[l] for l in range(d)])
    xbar=mv(K0,Ybar);tbar=mv(K0,Bbar)
    X=[sum(K0[j][i]*yl[i] for i in range(d))+sum(K1[j][i]*Ybar[i] for i in range(b)) for j in range(M+1)]
    Tc=[sum(K0[j][i]*bl[i] for i in range(d))+sum(K1[j][i]*Bbar[i] for i in range(b)) for j in range(M+1)]
    low=[Q(factorial(M),factorial(M-j))**2 for j in range(M+1)]
    high=[Q(factorial(M)*factorial(j-M-1))**2 for j in range(M+1,b+1)]
    delta=sum(w*x*x for w,x in zip(low,X))+sum(w*x*x for w,x in zip(high,xbar[M+1:]))
    nu=sum(w*x*t for w,x,t in zip(low,X,Tc))+sum(w*x*t for w,x,t in zip(high,xbar[M+1:],tbar[M+1:]))
    return dict(b=b,m=m,h=h,chi=chi,delta=delta,nu=nu,X=X,Tc=Tc,Delta=Delta)


def run():
    cases=[]
    receipt=json.loads((BASE/'BOUNDARY_MOMENT_QUOTIENT_RECEIPT.json').read_text())['rows']
    for b,m in ((4,1),(5,1)):
        for chi in (-1,1):
            result=symbolic(b,m,chi)
            matches=[r for r in receipt if (r['b'],r['m'],r['h'],r['chi'])==(b,m,1,chi)]
            for r in matches:
                values=r['initial_mu']+r['initial_lambda']+[r['C']]
                for key in ('Delta','delta','nu'):
                    value=result[key].evaluate(values)
                    assert value.numerator*pow(value.denominator,-1,r['p'])%r['p']==r[key],(b,chi,r['p'],key)
            out={k:v for k,v in result.items() if k not in ('delta','nu','X','Tc','Delta')}
            out.update({key:result[key].output() for key in ('Delta','delta','nu')})
            out['X']=[v.output() for v in result['X']];out['Tc']=[v.output() for v in result['Tc']]
            out['checks']=len(matches)
            cases.append(out)
            print(b,chi,'terms',len(result['delta'].d),len(result['nu'].d),
                  'lambda variables',[NAMES[j] for j in (2,3) if any(k[j] for k in result['nu'].d)],
                  'C terms',sum(bool(k[4]) for k in result['nu'].d),flush=True)
    (BASE/'H1_SYMBOLIC_MOMENT_QUOTIENT.json').write_text(json.dumps(dict(
        status='AUTHOR exact symbolic derivation; finite evaluation checks are supporting evidence only',variables=NAMES,rows=cases),indent=2)+'\n')


if __name__=='__main__':run()
