import sys,json
sys.path.insert(0,'[private local path removed]')
import sympy as s
from pathlib import Path
b=Path(__file__).parent; h,w=s.symbols('h w'); za=1-s.I; a=(1+s.I)/2
out=[]
for n in [4,8]:
    r=n//2
    data=json.loads((b/f'half_step_observability_n{n}.json').read_text())
    R=s.Matrix([[s.sympify(v) for v in data['row']]])
    F=R[0]; c=(2*h+2)/(2*h+3)
    M=s.Matrix([[c,0,1/(2*h+3)],[0,1,-1],[0,1,1]])
    k=(R.subs(h,h+1)*M/R[0].subs(h,h+1)-c*R/F).applyfunc(s.cancel)
    assert k[0]==0
    P=s.sympify(data['half_kernel']); V=w*w-w+s.Rational(1,2)
    deriv=s.cancel(P/V**r).subs(w,a)*s.factorial(r)*s.I**r
    gamma=s.simplify(s.I*a*deriv*(-a)**r/za**(r+1))
    cn=n*s.Rational(2)**(2-r)/s.factorial(r)*s.prod(n+1+2*j for j in range(r))
    zeta=s.expand_complex(s.simplify(gamma*(za-1)/(cn/4)))
    zr,zi=s.re(zeta),s.im(zeta); norm=zr*zr+zi*zi
    re=s.cancel((k[1]*zr+k[2]*zi)/norm)
    im=s.cancel((k[2]*zr-k[1]*zi)/norm)
    vals={'real':re.subs(h,0),'imag':im.subs(h,0),'real_plus_imag':(re+im).subs(h,0)}
    print('n',n,'gamma',gamma,'zeta',zeta,'h0',vals,flush=True)
    out.append({'n':n,'gamma':str(gamma),'zeta':str(zeta),'k_row':[str(v) for v in k],
                'normalized_real':str(re),'normalized_imag':str(im),
                'at_zero':{key:str(val) for key,val in vals.items()},
                'sector_at_zero':bool(vals['real']>=0 and vals['imag']<=0 and vals['real_plus_imag']>=0)})
(b/'half_step_markov_sector.json').write_text(json.dumps(out,indent=2))
