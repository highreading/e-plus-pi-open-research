"""Independent exact checks of the new parity bridge; no archive imports."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json


def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c


def rise(a,n):
    v=F(1)
    for j in range(n): v*=a+j
    return v


def phase(r):
    q=F(-2*r-3,3); h=r//2; ep=r%2
    ks=[mul([(-1)**j*comb(r,j) for j in range(r+1)],
            [comb(1+3*nu,j) for j in range(2+3*nu)]) for nu in (0,1)]
    d=F(r+3-3*ep,6); rr=-F(r+1+ep,2); rho=-d/q
    f=[]; u=[]
    for nu,k in enumerate(ks):
        f.append((rho if nu else 1)*sum(k[ep+2*t]*(-1)**t*rise(-rr,t)/rise(1-d-nu,t)
                     for t in range((len(k)-1-ep)//2+1)))
        cc=F((-1)**(r+nu)*factorial(r+nu))/rise(q+1-nu,r+1+nu)
        u.append(cc*sum(k[nu+2*t]*(-1)**t*rise(-F(r,3),t)/rise(-r-nu,t)
                     for t in range((len(k)-1-nu)//2+1)))
    # Solve odd chain down from the exact affine resonant terminal.
    states={0:(F(1),F(0),F(0)),2*r+3:(F(0),1/(q+2*r+3),-1/(q+2*r+3))}
    for k in range(2*r+1,0,-2):
        st=states[k+2]
        states[k]=tuple(((1 if j==1 else 0)-(3*q+k)*st[j])/(q+k) for j in range(3))
    for k in range(0,r+3,2):
        st=states[k]
        states[k+2]=tuple(((1 if j==1 else 0)-(q+k)*st[j])/(3*q+k) for j in range(3))
    x=[tuple(sum(v*(states[l+1][j]+states[l+3][j]) for l,v in enumerate(ks[0])) for j in range(3)),
       tuple(sum(v*states[l][j] for l,v in enumerate(ks[1])) for j in range(3))]
    kap=(-1)**(r+h)*rise(-d,h+2)/(rho*rise(-rr,h+2))
    for nu in (0,1):
        assert x[nu][0]==kap*f[nu]
        assert x[nu][2]==u[nu]/2
    return dict(k=ks,x=x,f=f,u=u)


def red(x,p):
    x=F(x)
    return x.numerator*pow(x.denominator,-1,p)%p


def coeff(p,poly,at,logkind):
    v=0
    for k,c in enumerate(poly):
        d=at-k
        if logkind=='A' and 0<d<p: v-=c*pow(d,-1,p)
        if logkind=='B' and d%2==0 and 0<d//2<p:
            t=d//2; v+=c*(-1)**(t-1)*pow(t,-1,p)
    return red(v,p)


def actual_check(p,j,s):
    q=2*s;r=(p-6*s-3)//2; nu_rows=[]; ph=phase(r)
    assert ((2*j+1)*p-2*s-1)%4==0
    m=((2*j+1)*p-2*s-1)//4
    uvw=[]
    for kind in range(3):
        at=2*j-(kind==2); a=3*j+(kind!=0); b=2*j+1+(kind!=0)
        uvw.append(sum((-1)**(at-t)*comb(a,at-2*t)*comb(b+t-1,t)
                       for t in range(at//2+1) if at-2*t<=a))
    ABC=((3*j+1)*uvw[0],-(2*j+1)*uvw[1],-(2*j+1)*uvw[2])
    for nu in (0,1):
        even=[F(0)]*(2*(q-nu)+1)
        for t in range(q-nu+1):even[2*t]=comb(q-nu,t)
        pol=mul(ph['k'][nu],even);tau=p-q+nu-1;T=p-r-1
        moments=[coeff(p,pol,tau,'A'),coeff(p,pol,tau,'B'),coeff(p,pol,tau+p,'B')]
        integral=sum(v/F(q-nu+l+1) for l,v in enumerate(pol))
        assert moments[0]==red(integral,p)
        assert moments[1]==red(ph['u'][nu],p)
        ep=r%2; ra=(T-ep)//2; da=ra-q
        period=F((-1)**(da-1)*factorial(q)*factorial(da-1),factorial(ra))
        assert red(period,p)
        assert moments[2]==red((-1)**r*ph['f'][nu]*period,p)
        E=sum(F(comb(q-1,t),q+2*t) for t in range(q))
        assert moments[0]==red(ph['x'][nu][0]*E+ph['x'][nu][1]*2**q+ph['x'][nu][2],p)
        at=4*m+nu;extra=1+3*nu;denpow=4*m+1+nu
        C=sum((-1)**t*comb(denpow+t-1,t)*sum((-1)**(at-2*t-k)*comb(6*m,at-2*t-k)*comb(extra,k)
                for k in range(extra+1) if 0<=at-2*t-k<=6*m) for t in range(at//2+1))
        assert C%p==0
        divided=(C//p)%p
        assert divided==sum(a*b for a,b in zip(ABC,moments))%p
        nu_rows.append(dict(nu=nu,moments=moments,actual_divided_log=divided))
    f0,f1=ph['f'];x0,x1=ph['x'];u0,u1=ph['u']
    db=f0*x1[1]-f1*x0[1];du=f0*u1-f1*u0
    eliminant=ABC[0]*2**q*db+(F(ABC[0],2)+ABC[1])*du
    assert red(f0*nu_rows[1]['actual_divided_log']-f1*nu_rows[0]['actual_divided_log'],p)==red(eliminant,p)
    return dict(p=p,j=j,s=s,r=r,M=m,rows=nu_rows,eliminant=red(eliminant,p))


def series_rat(n,d,length):
    a=[]
    for j in range(length):a.append((F(n[j] if j<len(n) else 0)-sum(d[k]*a[j-k] for k in range(1,min(j,len(d)-1)+1)))/d[0])
    return a


def series_pow(poly,power,length):
    assert poly[0]==1
    a=[F(1)]
    for n in range(1,length):a.append(sum(((power+1)*k-n)*poly[k]*a[n-k] for k in range(1,min(n,len(poly)-1)+1))/n)
    return a


def branch(r,minus):
    N=[54,-144,258,-240,354,-48,150,48] if minus else [432,2064,4440,5376,4044,1860,486,48]
    D=[-3,6,1,2] if minus else [6,14,7,2]
    C=series_rat(N,mul(mul(D,D),D),r+1)
    diff=[(i+1)*C[i+1] for i in range(r)]
    Q=[F(1),F(0),F(1)] if minus else [F(1),F(1),F(1,2)]
    kernel=mul(series_pow(Q,F(2*r,3),r),series_pow([1,-1 if minus else 1],F(-r),r))
    return sum(diff[k]*kernel[r-1-k] for k in range(r))/r


def run():
    initials=[];minors={}
    for e,lam in ((2,F(-729,98)),(4,F(59049,3025))):
        g=F(1)
        for n in range(3):
            r=e+6*n; ph=phase(r);f0,f1=ph['f'];x0,x1=ph['x'];u0,u1=ph['u']
            db=f0*x1[1]-f1*x0[1];du=f0*u1-f1*u0
            a,b=branch(r,True),branch(r,False)
            assert 16**n*db/g==lam*a
            assert 16**n*du/g==lam*b
            initials.append(dict(r=r,a=str(a),b=str(b),Db=str(db),Du=str(du)))
            g/=F((r+3)**2*(2*r+9)**2*(2*r+15)**2,78732*(r+1)*(r+2)**2*(r+4)**2*(r+5))
        minors[str(e)]=str(branch(e,True)*branch(e+6,False)-branch(e+6,True)*branch(e,False)/16)
    assert minors=={'2':'-4424709835/1594323','4':'3604770571325/774840978'}
    rows=[actual_check(p,j,s) for p,j,s in [(17,3,1),(19,3,2),(23,3,2),(29,3,1),(29,3,3),(31,3,2),(31,3,4),
                                                        (19,2,1),(23,2,1),(23,2,3),(31,2,1),(31,2,3)]]
    return dict(status='PASS',imports='Python standard library only; no archived or new production formula imports',
                scope='Finite independent consistency checks; all-index proof requires archived rational tensor identities.',
                even_initials=initials,even_minors=minors,actual_original_coefficient_checks=rows)


if __name__=='__main__':
    result=run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],even_initials=len(result['even_initials']),actual_rows=len(result['actual_original_coefficient_checks']))))
