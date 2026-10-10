"""L13 author h-dimensional seed quotient and 4h factorial-moment compression."""
from fractions import Fraction as Q
from pathlib import Path
from math import factorial,comb
import json
from finite_boundary_chart import conv,inverse_series,solve_lower,chart
from b4_finite_criterion import det,adj
from exact_local_probe import mm,mv

BASE=Path(__file__).resolve().parent


def residual_adjugate(A,p):
    # The one-dimensional residual block has adj([a])=[1], including a=0.
    return [[1]] if len(A)==1 else adj(A,p)


# Gaussian rational arithmetic; all pairs below are exact.
def ga(x):
    return (Q(x),Q(0)) if not isinstance(x,tuple) else x
def add(x,y):
    x,y=ga(x),ga(y); return (x[0]+y[0],x[1]+y[1])
def mul(x,y):
    x,y=ga(x),ga(y); return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def inv(x):
    x=ga(x);d=x[0]**2+x[1]**2;return (x[0]/d,-x[1]/d)
def power(x,n):
    if n<0:return power(inv(x),-n)
    r=ga(1)
    for _ in range(n):r=mul(r,x)
    return r
def binom_integer(n,k):
    r=Q(1)
    for j in range(k):r*=Q(n-j,j+1)
    assert r.denominator==1
    return int(r)
def residue(q,p):
    q=Q(q);return q.numerator*pow(q.denominator,-1,p)%p


def endpoint_fixed(h,b,chi):
    """Exact rational J_i(p-h), valid modulo p for p>2b and chi=(-1|p)."""
    assert chi in (-1,1)
    a=(Q(-1),Q(1));abar=(Q(-1),Q(-1))
    e=mul(abar,inv(a));d=add(1,mul(-1,e))
    L={h-k:mul((-1)**k*comb(h+k-1,k),mul(power(e,k),power(d,-h-k)))
       for k in range(h)}
    coefficients=[]
    for k in range(b):
        value=ga(0)
        for j in range(1,h+1):
            term=mul(L[j],binom_integer(-h-k+j-1,j-1))
            term=mul(term,mul((Q(-1),Q(chi)),power(a,-h-k)))
            # The conjugate branch is the conjugate of this exact expression.
            value=add(value,(2*term[0],Q(0)))
        assert value[1]==0
        coefficients.append(value[0])
    return [sum((Q(comb(i,k))*coefficients[k] for k in range(i+1)),Q(0))
            for i in range(b)]


def moment_sequences(p,h,min_c,max_c,alpha,Dc,qh):
    initial_mu=[];initial_lambda=[]
    tf=[factorial(t)%p for t in range(p)]
    for c in range(2*h):
        initial_mu.append(sum(alpha[t+c]*(-1)**t*tf[t] for t in range(p))%p)
        initial_lambda.append(sum(alpha[t+c]*(-1)**t*tf[t]*Dc[(-h-1-t)%p]
                                  for t in range(p))%p)
    def forcing(c,logarithmic):
        if not -(p-1)<=c<=0:return 0
        r=(-1)**(-c)*tf[-c]
        if logarithmic:r*=Dc[(c-h-1)%p]
        return r%p
    def expand(initial,logarithmic):
        values=dict(enumerate(initial))
        for c in range(2*h,max_c+1):
            values[c]=(forcing(c,logarithmic)-sum(qh[j]*values[c-j] for j in range(1,2*h+1)))%p
        for c in range(2*h-1,min_c+2*h-1,-1):
            values[c-2*h]=(forcing(c,logarithmic)-sum(qh[j]*values[c-j] for j in range(2*h))) *pow(qh[-1],-1,p)%p
        return values
    return initial_mu,initial_lambda,expand(initial_mu,False),expand(initial_lambda,True)


def compressed_chart(p,b,m,h):
    assert p>2*b and 1<=h<=min(m+1,b-m-2)
    d=b-h;M=m+1-h;chi=(-1)**((p-1)//2)
    inv2=pow(2,-1,p);q=[1,-1,inv2];qh=[1]
    for _ in range(h):qh=conv(qh,q,len(qh)+1,p)
    limit=max(p+2*h-2,b+h)
    alpha=inverse_series(qh,limit,p)
    Dc=[1]
    for j in range(1,p):Dc.append((j*Dc[-1]+1)%p)
    C=Dc[-1]
    im,il,mu,lam=moment_sequences(p,h,2-h-b,max(d,2*h-1),alpha,Dc,qh)
    invq=inverse_series(q,d,p)
    logarithm=[0]+[((-invq[j-1]+(invq[j-2] if j>=2 else 0))*pow(j,-1,p))%p for j in range(1,d)]
    adot=conv(alpha[:d],logarithm,d-1,p)
    Jfixed=endpoint_fixed(h,b,chi);J=[residue(x,p) for x in Jfixed];P=J[0]
    assert P
    Ntop=[];Atop=[]
    for i in range(h):
        t=h-i;factor=(-1)**(t-1)*pow(factorial(t-1),-1,p)%p
        Ntop.append([factor*mu[1-t-j]%p for j in range(b)])
        Atop.append(factor*lam[1-t]%p)
    T=[];Alower=[];G=[];F=[]
    g=[2*C%p]
    for j in range(1,d):g.append((j*g[-1]+2*Dc[j-1])%p)
    for l in range(d):
        f0=[1];f1=[0]
        for v in range(l):
            f1.append((f1[-1]*(l-v)+f0[-1])%p)
            f0.append(f0[-1]*(l-v)%p)
        tr=[];gr=[]
        for j in range(b):
            stop=max(0,l-j+1)
            tr.append(sum(alpha[s]*f0[j+s] for s in range(stop))%p)
            short=sum(alpha[s]*f1[j+s]+adot[s]*f0[j+s] for s in range(stop))
            gr.append((short+factorial(l)*mu[l+1-j])%p)
        av=sum(alpha[s]*f0[s]*Dc[(l-h-s)%p] for s in range(l+1))%p
        ff=factorial(l)*lam[l+1]
        for s in range(l+1):
            offset=l-h-s;base=Dc[offset%p]
            ff+=alpha[s]*f1[s]*base+adot[s]*f0[s]*base
            if offset>=0:ff+=alpha[s]*f0[s]*g[offset]
        T.append(tr);Alower.append(av);G.append(gr);F.append(ff%p)
    U0=[row[:d] for row in Ntop];U1=[row[d:] for row in Ntop]
    tau=factorial(0)
    for l in range(d):tau=tau*factorial(l)%p
    sigma=(-1)**(h*d);scale=sigma*tau%p
    Delta=scale*det(U1,p)%p
    top_endpoint=[];D0=1
    for i in range(h):
        if i:D0=D0*(-h+i)%p
        top_endpoint.append(D0*J[i]*pow(P,-1,p)%p)
    Yhigh=[scale*v%p for v in mv(residual_adjugate(U1,p),top_endpoint)]
    Ybar=[0]*d+Yhigh
    b0=solve_lower([row[:d] for row in T],Alower,p)
    rtop=[(Atop[i]-sum(U0[i][j]*b0[j] for j in range(d)))%p for i in range(h)]
    Bhigh=[scale*v%p for v in mv(residual_adjugate(U1,p),rtop)]
    Bbar=[Delta*v%p for v in b0]+Bhigh
    I=[[int(i==j) for j in range(b)] for i in range(b)]
    Dpol=[[j if j==i+1 else 0 for j in range(b)] for i in range(b)]
    U=[[I[i][j]+Dpol[i][j] for j in range(b)] for i in range(b)]
    Upow=I
    for _ in range(h):Upow=mm(Upow,U)
    Z=[[0]*b for _ in range(b+1)]
    for j in range(b):Z[j][j]=-1;Z[j+1][j]=1
    K0=[[v%p for v in row] for row in mm(Z,Upow)]
    L=[[0]*b for _ in range(b)];Dpow=I
    for k in range(1,b):
        Dpow=mm(Dpow,Dpol);factor=(-1)**(k+1)*pow(k,-1,p)
        for i in range(b):
            for j in range(b):L[i][j]=(L[i][j]+factor*Dpow[i][j])%p
    K1=[[-v%p for v in row] for row in mm(K0,L)]
    S=[(-1)**(h-1)*factorial(h-1)*factorial(l)*J[h+l]*pow(P,-1,p)%p for l in range(d)]
    GY=mv(G,Ybar);GB=mv(G,Bbar)
    yl=solve_lower([row[:d] for row in T],[(Delta*S[l]-GY[l])%p for l in range(d)],p)
    bl=solve_lower([row[:d] for row in T],[(Delta*F[l]-GB[l])%p for l in range(d)],p)
    xbar=[v%p for v in mv(K0,Ybar)];tbar=[v%p for v in mv(K0,Bbar)]
    X=[(sum(K0[j][i]*yl[i] for i in range(d))+sum(K1[j][i]*Ybar[i] for i in range(b)))%p for j in range(M+1)]
    Tc=[(sum(K0[j][i]*bl[i] for i in range(d))+sum(K1[j][i]*Bbar[i] for i in range(b)))%p for j in range(M+1)]
    low_weights=[];v=1
    for j in range(M+1):
        if j:v*=M+1-j
        low_weights.append(v*v%p)
    high_weights=[(factorial(M)*factorial(j-M-1))**2%p for j in range(M+1,b+1)]
    delta=(sum(w*x*x for w,x in zip(low_weights,X))+sum(w*x*x for w,x in zip(high_weights,xbar[M+1:])))%p
    nu=(sum(w*x*t for w,x,t in zip(low_weights,X,Tc))+sum(w*x*t for w,x,t in zip(high_weights,xbar[M+1:],tbar[M+1:])))%p
    return dict(p=p,b=b,m=m,h=h,chi=chi,C=C,initial_mu=im,initial_lambda=il,
                mu={str(k):v for k,v in sorted(mu.items())},lam={str(k):v for k,v in sorted(lam.items())},
                endpoint_fixed=[str(v) for v in Jfixed],J=J,P=P,U0=U0,U1=U1,tau=tau,
                Delta=Delta,T=T,G=G,F=F,Ybar=Ybar,Bbar=Bbar,X=X,Tc=Tc,
                xbar=xbar,tbar=tbar,delta=delta,nu=nu)


def run():
    expected=[]
    for r in json.loads((BASE/'B5_NORMALIZED_PRIME_CERTIFICATE.json').read_text())['residues']:
        expected.extend(r['normalized_charts'])
    expected.extend([chart(43,4,1,1),chart(17,7,2,3)])
    fields=['Delta','P','T','G','F','Ybar','Bbar','X','Tc','xbar','tbar','delta','nu']
    results=[]
    for reference in expected:
        p,b,m,h=[reference[k] for k in ('p','b','m','h')]
        result=compressed_chart(p,b,m,h)
        for key in fields:assert result[key]==reference[key],(p,b,m,h,key,result[key],reference[key])
        results.append(result)
        print(p,b,m,h,result['delta'],result['nu'],flush=True)
    (BASE/'BOUNDARY_MOMENT_QUOTIENT_RECEIPT.json').write_text(json.dumps(dict(
        status='AUTHOR exact compression verification against22 own finite quotient references; not independent review',
        parameter_count='4h factorial moments plus C_p and quadratic character; no b-dimensional adjugate',
        rows=results),indent=2)+'\n')


if __name__=='__main__':
    run()
