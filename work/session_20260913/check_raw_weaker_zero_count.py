"""Closed exact diagnostic at n=4,5 only; no canonical HP solve."""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'math_packages'))
import sympy as s
x=s.symbols('x'); Q=[s.Integer(1),x]
for k in range(1,9):Q.append(s.expand(x*Q[-1]+s.Rational(k*k,4*k*k-1)*Q[-2]))
F=[sum(c*x**i/s.factorial(i) for (i,),c in s.Poly(q,x).terms()) for q in Q]
out={}
for n in (4,5):
    fs=F[n+1:2*n]
    rec=[]
    # Exact Wronskians of the natural consecutive initial subfamilies.
    for r in range(1,len(fs)+1):
        w=s.Poly(s.wronskian(fs[:r],x),x)
        intervals=s.polys.polytools.intervals(w,eps=s.Rational(1,10**8))
        interior=[(str(a),str(b),m) for (a,b),m in intervals if a>0 and b<1]
        rec.append({'r':r,'degree':w.degree(),'factors':str(s.factor(w.as_expr())), 'interior_root_intervals':interior})
    out[str(n)]={'wronskians':rec}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
# Exact proof certificates, only for the same predeclared degrees 4 and 5.
y=s.symbols('y')
cert={}
for label,idx,strip in [('n4W3',[5,7,6],True),('n5W3',[6,8,7],False),('n5W4',[6,8,7,9],False)]:
    wx=s.Poly(s.wronskian([F[k] for k in idx],x),x)
    px=s.Poly(wx.as_expr()/x if strip else wx.as_expr(),x).clear_denoms()[1].primitive()[1]
    assert all(i%2==0 for (i,),c in px.terms())
    p=s.Poly(sum(c*y**(i//2) for (i,),c in px.terms()),y)
    if p.eval(0)<0:p=-p
    pieces=[(s.Rational(0),s.Rational(1))] if label!='n5W4' else [(s.Rational(0),s.Rational(1,2)),(s.Rational(1,2),s.Rational(1))]
    rows=[]
    for aa,bb in pieces:
        dp=s.Poly(p.diff().as_expr().subs(y,aa+(bb-aa)*y),y);d=dp.degree()
        bc=[sum(dp.nth(j)*s.binomial(k,j)/s.binomial(d,j) for j in range(k+1)) for k in range(d+1)]
        assert all(v<=0 for v in bc) and any(v<0 for v in bc)
        rows.append({'interval':[str(aa),str(bb)],'bernstein_derivative_coefficients':[str(v) for v in bc]})
    assert p.eval(0)>0>p.eval(1)
    bracket=(s.Rational(3,4),s.Rational(1)) if label=='n5W4' else (s.Rational(1,4),s.Rational(1,2))
    assert p.eval(bracket[0])>0>p.eval(bracket[1])
    cert[label]={'primitive_polynomial_in_x_squared':str(p.as_expr()),'derivative_certificates':rows,'root_bracket_x_squared':[str(z) for z in bracket],'endpoint_values':[str(p.eval(0)),str(p.eval(1))]}
for n,idx in [(4,[5,7]),(5,[6,8])]:
    wx=s.Poly(s.wronskian([F[k] for k in idx],x),x)
    assert all(c>0 for c in wx.all_coeffs() if c)
    cert[f'n{n}W2']={'positive_monomial_coefficients':str(wx.as_expr())}
Path(__file__).with_name('raw_weaker_zero_count_exact_certificates.json').write_text(json.dumps(cert,indent=2))
print('Exact positivity, derivative Bernstein, and separated-root certificates PASS for n=4,5.')
