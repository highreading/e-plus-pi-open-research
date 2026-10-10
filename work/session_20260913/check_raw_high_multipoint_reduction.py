"""Two exact abstract band-matrix controls; no HP solve or degree scan.

The coefficients and nodes deliberately are not the research sequence.
These controls test normalization, orientation and complementary signs.
The all-index mathematical arguments are in the accompanying note.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "math_packages"))
import sympy as s

x = s.Symbol("x")
checks = []


def zero(M):
    return all(s.cancel(v) == 0 for v in M)


for n in (3, 4):
    size = 2*n
    seed = s.Rational(1, 2)
    aa = [s.Integer(0)] + [s.Integer(j+1) for j in range(1, size+2)]
    diag = [s.Integer(j*j+1) for j in range(size)]
    R = [s.Matrix([[1, 0]]), s.Matrix([[seed, 1]])]
    for j in range(size-2):
        val = (x-diag[j])*R[j] + aa[j+1]*R[j+1]
        if j >= 1:
            val += aa[j]*R[j-1]
        if j >= 2:
            val -= aa[j]*aa[j-1]*R[j-2]
        R.append(val.applyfunc(s.expand)/(aa[j+1]*aa[j+2]))

    coeff = s.Matrix(size, size,
                     lambda i,j: s.expand(R[i][j % 2]).coeff(x,j//2))
    assert coeff.is_lower
    nodes = [s.Integer(3*l+2) for l in range(n+1)]
    amps = [s.Rational(l+2,l+1) for l in range(n+1)]
    Q = [s.prod(x-nodes[l] for l in range(n+1) if l % 2 == sig)
         for sig in (0, 1)]
    vectors = []
    for sig in (0, 1):
        deg = s.degree(Q[sig], x)
        for j in range(n-int(deg)):
            vec = s.zeros(size,1)
            pol = s.Poly(Q[sig]*x**j,x)
            for (k,), val in pol.terms():
                vec[2*k+sig] = val
            vectors.append((2*(int(deg)+j)+sig, sig, j, vec))
    vectors.sort(key=lambda v: v[0])
    assert [v[0] for v in vectors] == list(range(n+1,size))
    Z = coeff.T.inv()*s.Matrix.hstack(*(v[3] for v in vectors))
    ZL, ZH = Z[:n+1,:], Z[n+1:,:]
    assert ZH.is_upper
    assert ZH.det() == s.prod(1/coeff[k,k] for k in range(n+1,size))

    K = s.zeros(size)
    for i in range(size):
        K[i,i] = diag[i]
        if i+1 < size:
            K[i,i+1] = K[i+1,i] = -aa[i+1]
        if i+2 < size:
            K[i,i+2] = K[i+2,i] = aa[i+1]*aa[i+2]
    seeds = [s.eye(size)[:,0], s.eye(size)[:,1]-seed*s.eye(size)[:,0]]
    for col, (_,sig,j,_) in enumerate(vectors):
        qK = s.zeros(size)
        for (k,), val in s.Poly(Q[sig],x).terms():
            qK += val*K**k
        assert zero(Z[:,col]-qK*K**j*seeds[sig])

    evals = s.Matrix(size,n+1,lambda i,l: R[i][l % 2].subs(x,nodes[l]))
    S = evals[:n+1,:]*s.diag(*amps)
    Hi = evals[n+1:,:]*s.diag(*amps)
    assert zero(Hi+ZH.T.inv()*ZL.T*S)
    assert ZL.rank() == n-1
    P = s.eye(n+1)-ZL*(ZL.T*ZL).inv()*ZL.T
    C = S.inv()*P*S.T.inv()
    common = (-1)**(n-1)*S.det()/ZH.det()
    for j in range(n+1):
        for k in range(j+1,n+1):
            I = [l for l in range(n+1) if l not in (j,k)]
            a = S.T.inv()[:,j]
            b = S.T.inv()[:,k]
            border = s.Matrix.hstack(ZL,a,b).det()
            assert Hi[:,I].det() == common*(-1)**(j+k+1)*border
            assert border**2 == (ZL.T*ZL).det()*C.extract([j,k],[j,k]).det()
    e2 = (s.trace(C)**2-s.trace(C*C))/2
    d = C.extract([n-1,n],[n-1,n]).det()/e2
    assert s.cancel(d-Hi[:,:n-1].det()**2/(Hi*Hi.T).det()) == 0
    checks.append({"abstract_n": n, "all_identities_passed": True,
                   "normalized_angle_determinant": str(d)})

out = {"scope": "Generic rational band coefficients and artificial nodes; no canonical HP or spectral diagnostic.",
       "checks": checks}
(HERE / "raw_high_multipoint_reduction_checks.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
