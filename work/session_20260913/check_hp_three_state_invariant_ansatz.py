"""Bounded symbolic search; no prime or index scan.

Predeclared polynomial degree bound: 6.
Multipliers: 1; -n^a(n+1)^(2-a), a=0,1,2;
and n^a(n+1)^(4-a)/4, a=0,...,4.
Search symmetric and skew-symmetric polynomial forms separately.
Failure means only that these fixed ansatz classes contain no form.
"""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent/'math_packages'))
import sympy as s

n=s.symbols('n')
M=s.Matrix([[-3*n,n*n,n*n],[2,0,0],[2-n,n*n,-n*(n+2)]])
MAX_DEGREE=6
choices=[s.Integer(1)]
choices += [-n**a*(n+1)**(2-a) for a in range(3)]
choices += [n**a*(n+1)**(4-a)/4 for a in range(5)]
result={"degree_bound":MAX_DEGREE,"multipliers":[str(x) for x in choices],"tests":[]}

for kind in ('symmetric','skew'):
    positions=[(i,j) for i in range(3) for j in range(i if kind=='symmetric' else i+1,3)]
    basis=[]
    for i,j in positions:
        for k in range(MAX_DEGREE+1):
            Q=s.zeros(3)
            Q[i,j]=n**k
            if i!=j:
                Q[j,i]=n**k if kind=='symmetric' else -n**k
            basis.append(Q)
    for rho in choices:
        columns=[]
        for Q in basis:
            F=s.expand(M.T*Q.subs(n,n+1)*M-4*rho*Q)
            columns.append(s.Matrix([s.Poly(F[i,j],n).nth(k) for i,j in positions for k in range(MAX_DEGREE+5)]))
        system=s.Matrix.hstack(*columns)
        null=system.nullspace()
        row={"kind":kind,"rho":str(rho),"unknowns":len(basis),"nullity":len(null),"kernel":[]}
        for v in null:
            Q=sum((v[k]*basis[k] for k in range(len(basis))),s.zeros(3))
            assert s.expand(M.T*Q.subs(n,n+1)*M-4*rho*Q)==s.zeros(3)
            row["kernel"].append([[str(s.factor(Q[i,j])) for j in range(3)] for i in range(3)])
        result["tests"].append(row)

assert s.factor(M.det()/8)==n**3*(n+1)/2
result["transition_determinant_verified"]=True
Path(__file__).with_name('hp_three_state_invariant_ansatz_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
