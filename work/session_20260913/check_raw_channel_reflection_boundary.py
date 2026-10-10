"""Closed symbolic controls at N=2,3; no HP solve or degree scan."""
from pathlib import Path
import sys
import json

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'math_packages'))
import sympy as s

x, t = s.symbols('x t')

def raw_basis(k):
    p = s.Poly(s.I**k * s.legendre(k, -s.I*x), x)
    return s.sqrt(2*k+1)*sum(v*x**int(m[0])/s.factorial(m[0])
                            for m, v in p.terms())

def reflection_matrix(dim):
    basis = [raw_basis(k) for k in range(dim)]
    coeff = s.Matrix(dim, dim, lambda j,k: s.expand(basis[k]).coeff(x,j))
    reflected = s.Matrix(dim, dim,
                         lambda j,k: s.expand(basis[k].subs(x,1-x)).coeff(x,j))
    return (coeff.inv()*reflected).applyfunc(s.simplify)

def aa(k):
    return s.Integer(0) if k == 0 else k*k/s.sqrt(4*k*k-1)

def row_matrix(dim):
    out = s.zeros(dim)
    for k in range(dim):
        out[k,k] = aa(k)**2+aa(k+1)**2-k*(k+1)
        if k+1 < dim:
            out[k,k+1] = out[k+1,k] = -aa(k+1)
        if k+2 < dim:
            out[k,k+2] = out[k+2,k] = aa(k+1)*aa(k+2)
    return out

checks = []
for dim in (2,3):
    c = reflection_matrix(dim)
    k = row_matrix(dim)
    u = reflection_matrix(dim+2)[:dim,dim:dim+2]
    gamma = s.Matrix([[aa(dim-1)*aa(dim),0],
                      [-aa(dim),aa(dim)*aa(dim+1)]])
    injection = s.eye(dim)[:,dim-2:dim]
    comm = (k*c-c*k-u*gamma.T*injection.T).applyfunc(s.simplify)
    involution = (c*c-s.eye(dim)).applyfunc(s.simplify)

    # Exact backward-difference/residue identity on every monomial
    # of this fixed-size polynomial space.
    p = sum(s.Symbol(f'c{j}')*t**j for j in range(dim))
    coeff = s.Poly(p,t)
    exp_back = 0
    term = p
    for j in range(dim):
        exp_back += (-s.I)**j*term/s.factorial(j)
        term = s.cancel((term-term.subs(t,0))/t)
    translated_borel = sum(v*(-s.I*x)**int(m[0])/s.factorial(m[0])
                           for m,v in coeff.terms()).subs(x,x+1)
    back_borel = sum(v*(-s.I*x)**int(m[0])/s.factorial(m[0])
                    for m,v in s.Poly(s.expand(exp_back),t).terms())
    translation_zero = s.expand(translated_borel-back_borel) == 0
    checks.append({'N':dim, 'reflection':str(c),
                   'commutator_zero':comm == s.zeros(dim),
                   'involution_zero':involution == s.zeros(dim),
                   'translation_identity':translation_zero})
    assert all(checks[-1][key] for key in
               ('commutator_zero','involution_zero','translation_identity'))

(HERE/'raw_channel_reflection_boundary_checks.json').write_text(
    json.dumps({'scope':'Only N=2,3 symbolic normalization controls',
                'checks':checks}, indent=2)+'\n')
print(json.dumps(checks, indent=2))
