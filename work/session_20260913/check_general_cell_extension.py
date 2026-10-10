#!/usr/bin/env python3
"""Exact finite identities/initials for general_cell_roth_attempt.md.

This verifies finite rational identities and initial data. The all-index bridge
uses the archived rational Hermite/tensor identities as an explicit dependency;
this script does not substitute a finite sample for those identities.
"""
from __future__ import annotations
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent / "math_packages"))
from item250_j2_ordinary_phase_certificate import conv, poly_pow, rising, b_sum
from item309_j2_l_second_branch_bridge_certificate import branch_coefficients
from item237_j1_algebraic_residual_certificate import lagrange_coefficient
import sympy as sp


def phase(r):
    assert r > 0 and r % 3
    q = F(-2*r-3, 3)
    k0 = conv(poly_pow([1, -1], r), [1, 1])
    k1 = conv(poly_pow([1, -1], r), poly_pow([1, 1], 4))
    ks = 2*r+3
    alpha = 1/(q+ks)
    beta = -alpha
    for k in range(ks-2, 0, -2):
        alpha = (1-(3*q+k)*alpha)/(q+k)
        beta = -(3*q+k)*beta/(q+k)
    states = [None]*(r+5)
    states[0] = (F(1), F(0), F(0))
    states[1] = (F(0), alpha, beta)
    for k in range(r+3):
        u, v, w = states[k]
        states[k+2] = (-(q+k)*u/(3*q+k),
                       (1-(q+k)*v)/(3*q+k), -(q+k)*w/(3*q+k))
    x0 = tuple(sum(c*(states[l+1][i]+states[l+3][i])
                   for l,c in enumerate(k0)) for i in range(3))
    x1 = tuple(sum(c*states[l][i] for l,c in enumerate(k1)) for i in range(3))
    n = r+q+1
    ca0 = F((-1)**r*math.factorial(r))/rising(q+1,r+1)
    ca1 = F((-1)**(r+1)*math.factorial(r+1))/rising(q,r+2)
    u0 = ca0*b_sum(k0,0,n,F(r+1))
    u1 = ca1*b_sum(k1,1,n,F(r+2))
    eps = r%2
    d, rr = F(r+3-3*eps,6), -F(r+1+eps,2)
    rho = -d/q
    f0 = b_sum(k0,eps,rr,d)
    f1 = rho*b_sum(k1,eps,rr,d+1)
    return dict(q=q, k0=k0, k1=k1, x0=x0, x1=x1,
                u=(u0,u1), f=(f0,f1), d=d, rr=rr, rho=rho)


def gauge_even(r):
    return F((r+3)**2*(2*r+9)**2*(2*r+15)**2,
             78732*(r+1)*(r+2)**2*(r+4)**2*(r+5))


def run():
    tested = [r for r in range(1,29) if r%3]
    for r in tested:
        data = phase(r)
        eps, h = r%2, r//2
        kappa = ((-1)**(r+h)*rising(-data['d'],h+2)
                 / (data['rho']*rising(-data['rr'],h+2)))
        for nu in (0,1):
            assert data[f'x{nu}'][0] == kappa*data['f'][nu]
            assert data[f'x{nu}'][2] == data['u'][nu]/2
            # Exact opposite-parity period, whose beta first argument is integer.
            part = F(0)
            for ell, coefficient in enumerate(data[f'k{nu}']):
                if ell%2 != 1-eps:
                    continue
                t = (ell-(1-eps))//2
                aa = (r+ell+1)//2
                part += (coefficient*(-1)**t*F(math.factorial(aa-1),2)
                         /rising(F(-2*r,3)-nu,aa))
            assert 2*(-1)**(h+eps)*part == data['u'][nu]
    r = sp.symbols('r')
    ke = 64*(r+6)*(2*r+3)*(2*r+9)/(27*(r+1)*(r+3)*(r+5))
    ko = 64*(r+3)*(2*r+3)*(2*r+9)/(27*r*(r+2)*(r+4))
    re = (r+3)**2*(2*r+9)**2*(2*r+15)**2/(78732*(r+1)*(r+2)**2*(r+4)**2*(r+5))
    ro = r*(r+6)*(2*r+9)**2*(2*r+15)**2/(78732*(r+1)**2*(r+2)*(r+4)*(r+5)**2)
    assert sp.cancel(re*ke-ro*ko)==0
    # Symbolic all-j coefficient-triple lemma: both rational differential
    # identities precede coefficient extraction and backward propagation.
    jj, yy = sp.symbols('j y')
    log_derivative=-(3*jj+1)/(1-yy)-(4*jj+4)*yy/(1+yy**2)
    assert sp.cancel((1-yy)*(1+yy**2)*log_derivative
                     -(-(3*jj+1)-(4*jj+4)*yy+(jj+3)*yy**2))==0
    assert sp.cancel(2*yy+(1+yy**2)*log_derivative
                     +(3*jj+1)*(1+yy**2)/(1-yy)+(4*jj+2)*yy)==0
    # Beta six-step ratio: B(a,b)/B(a+3,b-4).
    for eps, expected in ((0,ke),(1,ko)):
        aa=(r+1+eps)/2
        bb=-2*r/3
        ratio=sp.prod(bb-t for t in range(1,5))/(sp.prod(aa+t for t in range(3))*(aa+bb-1))
        # (-1)^(h+eps) changes sign after the six-step shift.
        assert sp.cancel(-ratio-expected)==0
    branches=branch_coefficients(28)
    initials=[]
    minors={}
    for e, expected in ((2,F(-729,98)),(4,F(59049,3025))):
        g=F(1)
        for n in range(3):
            rr=e+6*n
            data=phase(rr)
            f0,f1=data['f']
            db=f0*data['x1'][1]-f1*data['x0'][1]
            du=f0*data['u'][1]-f1*data['u'][0]
            assert 16**n*db/g==expected*branches[rr]
            assert 16**n*du/g==expected*lagrange_coefficient(rr)
            initials.append(dict(e=e,n=n,r=rr,db=str(db),du=str(du),g=str(g),scalar=str(expected)))
            g/=gauge_even(rr)
        minor=branches[e]*lagrange_coefficient(e+6)-branches[e+6]*lagrange_coefficient(e)/16
        assert minor
        minors[str(e)]=str(minor)
    assert minors == {'2':'-4424709835/1594323','4':'3604770571325/774840978'}
    j=3
    u=sum((-1)**t*math.comb(2*j+t,t)*math.comb(3*j,2*j-2*t) for t in range(j+1))
    v=sum((-1)**t*math.comb(2*j+1+t,t)*math.comb(3*j+1,2*j-2*t) for t in range(j+1))
    w=-sum((-1)**t*math.comb(2*j+1+t,t)*math.comb(3*j+1,2*j-1-2*t) for t in range(j))
    assert (u,v,w)==(126,30,348)
    return dict(status='EXACT_FINITE_IDENTITIES_AND_INITIALS_PASS',
                scope='All-index proof additionally imports archived Hermite/tensor identities; no numerical density inference.',
                rational_identity_indices=tested,gauge_weight_identity=True,beta_six_step_identity=True,
                all_j_triple_nonvanishing_differential_identities=True,
                even_bridge_initials=initials,even_initial_minors=minors,j3_UVW=[u,v,w])


if __name__=='__main__':
    result=run()
    output=Path(__file__).with_name('general_cell_extension_checks.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'output':str(output)}))
