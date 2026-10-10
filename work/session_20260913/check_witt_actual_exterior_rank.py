#!/usr/bin/env python3
"""Exact coefficient determinant for the actual first-Witt exterior rank.

No interpolation or prime sample is used. The 26-by-26 determinant is
calculated over Z[r] and checked against its fully factored expression.
"""
from __future__ import annotations
import functools
import hashlib
import json
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / 'math_packages'))
import sympy as s


def run():
    x,r=s.symbols('x r')
    u=x*(1-x)
    q=(1+x)*(1+x*x)
    columns=[]
    for k in range(23):
        a=x**k
        # Three times the differentiated degree-p primitive operator.
        value=3*u*q*s.diff(a,x)+(3*(r-11)*q*s.diff(u,x)-2*r*u*s.diff(q,x))*a
        columns.append(s.Poly(s.expand(value),x))
    for k in range(3):
        columns.append(s.Poly(-3*u**(12-6*k)*q**(4*k),x))
    assert all(poly.degree()<=25 for poly in columns)
    matrix=s.Matrix([[poly.nth(k) for poly in columns] for k in range(26)])
    determinant=s.polys.matrices.DomainMatrix.from_Matrix(matrix).det().as_expr()
    sextic=(176275*r**6-6297825*r**5+89867547*r**4-649457253*r**3
            +2470644018*r**2-4573809342*r+3062922660)
    expected=(-s.Integer(2)**38*3**13*5**2*r**2*(r-11)*(r-10)*(r-9)
              *(r-8)*(r-7)*(r-6)*(r-3)**2*(r-1)*(2*r-21)*(2*r-15)
              *(2*r-9)**2*(2*r-3)**2*sextic)
    assert s.expand(determinant-expected)==0
    assert s.Poly(determinant,r).degree()==23
    coefficients=[int(c) for c in s.Poly(sextic,r).all_coeffs()]
    assert functools.reduce(math.gcd,coefficients)==1
    rows=[[str(value) for value in row] for row in matrix.tolist()]
    payload=json.dumps(rows,separators=(',',':')).encode()
    return dict(status='EXACT_POLYNOMIAL_DETERMINANT_PASS',
                coefficient_ring='Z[r]',matrix_shape=[26,26],
                row_order='coefficients of x^0,...,x^25',
                column_order='A=x^0,...,x^22, then c0,c1,c2',
                operator='3*u*Q*A_prime + [3*(r-11)*Q*u_prime-2*r*u*Q_prime]*A - 3*sum(c_k*u^(12-6k)*Q^(4k))',
                matrix_sha256=hashlib.sha256(payload).hexdigest(),
                matrix=rows,determinant_factored=str(expected),
                determinant_degree=23,sextic_coefficients_high_to_low=coefficients,
                sextic_integer_content=1,
                interpretation='On actual rows r>=12 all linear factors and the scalar are p-units; at most six starts can have zero exterior state. See the accompanying proof for the actual endpoint rank argument.')


if __name__=='__main__':
    data=run()
    output=Path(__file__).with_name('witt_actual_exterior_rank_certificate.json')
    output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:data[k] for k in ('status','matrix_shape','determinant_degree','sextic_integer_content')}))
