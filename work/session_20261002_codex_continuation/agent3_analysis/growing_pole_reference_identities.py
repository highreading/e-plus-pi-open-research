"""Bounded exact checks of M31's classical reference normalization and toy confluent factor.

These are not checks of Root's actual moment, content, or period certificates.
"""
import json
from pathlib import Path
import sympy as sp

OUT = Path(__file__).resolve().parent

def gamma_gram(n, power=0):
    return sp.Matrix(n, n, lambda i,j: sum(
        sp.binomial(power,r)/(sp.Rational(i+j+r)+sp.Rational(1,2))
        for r in range(power+1)))

def jet_matrix(n,m):
    return sp.Matrix(n,m,lambda i,j: sp.binomial(i,j)*(-1)**(i-j) if i>=j else 0)

reference=[]
for n in range(1,9):
    G=gamma_gram(n)
    inverse=G.inv()
    for m in range(1,n+1):
        V=jet_matrix(n,m)
        actual=sp.factor((V.T*inverse*V).det())
        modified=gamma_gram(n-m,2*m).det() if n>m else sp.Integer(1)
        modified=sp.factor(modified/G.det())
        successive=sp.Integer(1)
        for r in range(m):
            size=n-r
            H=gamma_gram(size,2*r)
            v=jet_matrix(size,1)
            successive*=sp.factor((v.T*H.inv()*v)[0])
        assert actual==modified==sp.factor(successive),(n,m)
        ordinary=sp.Integer(1)
        for size in range(n-m+1,n+1):
            H=gamma_gram(size)
            v=jet_matrix(size,1)
            ordinary*=sp.factor((v.T*H.inv()*v)[0])
        assert ordinary/4**(m*(m-1)//2)<=actual<=ordinary,(n,m)
        reference.append({"k":n,"m":m,"det_jet":str(actual),"pass":True})

def nu(r,m):
    return (-1)**r*sp.rf(sp.Rational(1,2)-r,m-1)/sp.rf(sp.Rational(1,2),m-1)

def mu(r):
    # Deliberately different toy positive measure: ordinary Lebesgue on [2,3].
    return sp.Rational(3**(r+1)-2**(r+1),r+1)

confluent=[]
for m in range(1,9):
    C=sp.Matrix(m,2*m,lambda i,j:mu(i+j)-nu(i+j,m))
    V=sp.Matrix(m,2*m,lambda i,j:nu(i+j,m))
    coefficient=C.col_join(V).det()
    positive=sp.Matrix(m,m,lambda i,j:sum(
        sp.binomial(m,r)*mu(i+j+r) for r in range(m+1))).det()
    kappa=(sp.factorial(m-1)/sp.rf(sp.Rational(1,2),m-1))**m
    expected=(-1)**(m+m*(m-1)//2)*kappa*positive
    assert coefficient==expected,m
    confluent.append({"m":m,"coefficient":str(coefficient),"kappa":str(kappa),"pass":True})

receipt={"scope":"Classical compact reference jet identity and unrelated toy positive-measure confluent factor; no actual e+pi certificate audit.",
         "reference_cases":reference,"confluent_cases":confluent,"all_pass":True}
(OUT/"GROWING_POLE_REFERENCE_IDENTITIES_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({"reference_cases":len(reference),"confluent_cases":len(confluent),"all_pass":True}))
