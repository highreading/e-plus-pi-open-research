import sys, json
sys.path.insert(0, '[private local path removed]')
import sympy as S
n,h,u,v,Y = S.symbols('n h u v Y')

def T(t):
    return S.Matrix([[-t,t,S.Rational(1,2)], [t+1,-t-1,(t+1)/2], [t*(t+1),t+1,-(t+1)*(t+2)/2]])

state = S.Matrix([h,u,v])
r0 = S.Matrix([[1,0,0],[n,1,0]])*state
k = n+1
r1 = S.Matrix([[k,1,0],[k*(k-1),2*k,1]])*T(n)*state
k = n+2
r2 = S.Matrix([[k*(k-1),2*k,1],[k*(k-1)*(k-2)+2*k,3*k*(k-1),2*k]])*T(n+1)*T(n)*state
B = S.Matrix([[r0[0],r0[1]],[r1[0],r1[1]],[r2[0],r2[1]]])
pairs = [(0,1),(0,2),(1,2)]
minors = [S.expand(B.extract(list(pair),[0,1]).det()) for pair in pairs]
D = 2*(n+1)*h*h-2*h*u-(n-1)*u*u-u*v
E = -2*n*(n+2)*h*h+4*n*h*u+(n+2)*h*v+(n*n-2*n-1)*u*u+n*u*v
C = u**3+(n-2)*h*u*u+4*h*h*u-2*(n+2)*h**3
checks = {
 'first_minor_identity': S.expand(minors[0]-(n+1)*D)==0,
 'second_minor_identity': S.expand(minors[1]-(n+2)*(2*n+3)*E)==0,
 'cubic_elimination_identity': S.expand(u*E+(n*u+(n+2)*h)*D+(n+1)*C)==0
}
contents=[]
for f in minors:
    g=S.gcd_list(S.Poly(f,h,u,v).coeffs())
    contents.append(S.Poly(g,n).monic().as_expr())
exceptional={}
for value in [S.Integer(-1),S.Integer(-2),-S.Rational(3,2)]:
    exceptional[str(value)]={'formal_matrix': [[str(S.factor(B[i,j].subs(n,value))) for j in range(2)] for i in range(3)], 'formal_minors': [str(S.factor(f.subs(n,value))) for f in minors]}

def falling(x,m):
    return S.prod(x-j for j in range(m))

def trunc(a,r,cutoff=6):
    x=S.Integer(a)+3*Y
    ans=S.Integer(0)
    for c in range((cutoff-1)//2+1):
        for b in range(cutoff-2*c):
            ans += S.Rational((-1)**b,2**c*S.factorial(b)*S.factorial(c))*falling(x,b+2*c+r)*falling(x,b+c)
    return S.Poly(S.expand(ans),Y)

def reduce3(poly):
    terms={}
    for exponent,coefficient in poly.terms():
        num,den=S.fraction(coefficient)
        assert int(den)%3 != 0, ('nonintegral coefficient',coefficient)
        residue=(int(num)%3)*pow(int(den)%3,-1,3)%3
        if residue:
            terms[exponent]=residue
    return S.Poly.from_dict(terms,Y).as_expr()

# These are the three shifted entries of one selected index disk, not a disk scan.
derivatives={a:[reduce3(trunc(a,r)) for r in range(4)] for a in [0,1,2]}
entries={}
for a in [0,1,2]:
    x=S.Integer(a)+3*Y
    dh,du,dv,dw=derivatives[a]
    expressions=[dh,x*dh+du,x*(x-1)*dh+2*x*du+dv,x*(x-1)*(x-2)*dh+3*x*(x-1)*du+3*x*dv+dw]
    entries[a]=[reduce3(S.Poly(S.expand(f),Y)) for f in expressions]
Bmod=S.Matrix([[entries[0][0],entries[0][1]],[entries[1][1],entries[1][2]],[entries[2][2],entries[2][3]]])
minor_mod=[reduce3(S.Poly(S.expand(Bmod.extract(list(pair),[0,1]).det()),Y)) for pair in pairs]
checks['disk_3Z3_certificate']=(Bmod==S.Matrix([[1,0],[1,2],[0,0]]) and minor_mod==[S.Integer(2),S.Integer(0),S.Integer(0)])
print(json.dumps({'checks':checks,'formal_index_contents':[str(S.factor(g)) for g in contents],'common_formal_index_content':str(S.factor(S.gcd_list(contents))),'exceptional_parameters':exceptional,'budget_used':{'prime':3,'index_disk':'3 Z_3','precision':1,'truncation_R_exclusive':6,'subdivision_depth':0},'truncated_derivatives_mod3':{str(a):[str(f) for f in fs] for a,fs in derivatives.items()},'matrix_mod3':str(Bmod),'minors_mod3':[str(f) for f in minor_mod]},indent=2))