import sys
sys.dont_write_bytecode = True
sys.path.insert(0, '[private local path removed]')
import json
import sympy as S

x, z, Y = S.symbols('x z Y')

def falling(t, length):
    return S.prod(t-j for j in range(length))

def direct_H(n):
    exponential = sum(x**j*z**j/S.factorial(j) for j in range(n+1))
    return S.expand(S.factorial(n)*S.expand(exponential*(1-z+z*z/2)**n).coeff(z,n))

def interpolation(r, t, cutoff):
    terms = []
    for c in range((cutoff-1)//2+1):
        for b in range(cutoff-2*c):
            terms.append((-1)**b*falling(t,b+2*c+r)*falling(t,b+c)/(S.Integer(2)**c*S.factorial(b)*S.factorial(c)))
    return S.expand(sum(terms))

def mod3(poly):
    answer = 0
    for (degree,), coefficient in S.Poly(S.expand(poly),Y,domain=S.QQ).terms():
        numerator, denominator = coefficient.as_numer_denom()
        denominator = int(denominator)
        assert denominator % 3 != 0, ('nonintegral coefficient', coefficient)
        answer += (int(numerator)*pow(denominator,-1,3) % 3)*Y**degree
    return S.expand(answer)

def combinations(t, ds):
    h,u,v,w = ds
    return [h, t*h+u, t*(t-1)*h+2*t*u+v,
            t*(t-1)*(t-2)*h+3*t*(t-1)*u+3*t*v+w]

def minors(matrix):
    return [S.expand(matrix[i,0]*matrix[j,1]-matrix[i,1]*matrix[j,0])
            for i,j in [(0,1),(0,2),(1,2)]]

polynomials = [direct_H(a) for a in range(3)]
tuples = [[S.diff(polynomials[a],x,r).subs(x,1) for r in range(4)] for a in range(3)]
assert polynomials == [S.Integer(1), x-1, x*x-4*x+4]
assert tuples == [[1,0,0,0],[0,1,0,0],[1,-2,2,0]]

truncated = [[interpolation(r,a+3*Y,6) for r in range(4)] for a in range(3)]
short = [[interpolation(r,a+3*Y,3) for r in range(4)] for a in range(3)]
for a in range(3):
    for r in range(4):
        assert mod3(truncated[a][r]) == int(tuples[a][r]) % 3
        assert mod3(truncated[a][r]-short[a][r]) == 0

term_checks = 0
for R in range(3,6):
    for c in range(R//2+1):
        b = R-2*c
        for a in range(3):
            t = a+3*Y
            for r in range(4):
                term = (-1)**b*falling(t,R+r)*falling(t,b+c)/(S.Integer(2)**c*S.factorial(b)*S.factorial(c))
                assert mod3(term) == 0
                term_checks += 1

cs = [combinations(a+3*Y,truncated[a]) for a in range(3)]
B = S.Matrix([[cs[0][0],cs[0][1]],[cs[1][1],cs[1][2]],[cs[2][2],cs[2][3]]])
Bmod = B.applyfunc(mod3)
minor_mod = [mod3(value) for value in minors(B)]
assert Bmod == S.Matrix([[1,0],[1,2],[2,0]])
assert minor_mod == [2,0,2]

at_zero = [combinations(a,tuples[a]) for a in range(3)]
Bzero = S.Matrix([[at_zero[0][0],at_zero[0][1]],[at_zero[1][1],at_zero[1][2]],[at_zero[2][2],at_zero[2][3]]])
assert Bzero == S.Matrix([[1,0],[1,2],[-4,0]])
assert minors(Bzero) == [2,0,8]

# Separate formal algebra check of the source prefactors; not an endpoint transfer.
n,h,u,v = S.symbols('n h u v')
def transition(t):
    return S.Matrix([[-t,t,S.Rational(1,2)], [t+1,-t-1,(t+1)/2], [t*(t+1),t+1,-(t+1)*(t+2)/2]])
state = S.Matrix([h,u,v])
s1 = transition(n)*state
s2 = transition(n+1)*s1
k = n+1
row1 = [(S.Matrix([[k,1,0]])*s1)[0], (S.Matrix([[k*(k-1),2*k,1]])*s1)[0]]
k = n+2
row2 = [(S.Matrix([[k*(k-1),2*k,1]])*s2)[0], (S.Matrix([[k*(k-1)*(k-2)+2*k,3*k*(k-1),2*k]])*s2)[0]]
formal_B = S.Matrix([[h,n*h+u],row1,row2])
formal_minors = minors(formal_B)
D = 2*(n+1)*h*h-2*h*u-(n-1)*u*u-u*v
E = -2*n*(n+2)*h*h+4*n*h*u+(n+2)*h*v+(n*n-2*n-1)*u*u+n*u*v
assert S.expand(formal_minors[0]-(n+1)*D) == 0
assert S.expand(formal_minors[1]-(n+2)*(2*n+3)*E) == 0
contents = [S.factor(S.gcd_list(S.Poly(value,h,u,v).coeffs())) for value in formal_minors]

print(json.dumps({
    'status':'all asserted finite checks passed',
    'direct_H':[str(value) for value in polynomials],
    'derivative_tuples':[[int(value) for value in row] for row in tuples],
    'interpolation_reductions':[[str(mod3(value)) for value in row] for row in truncated],
    'matrix_mod3':[[int(Bmod[i,j]) for j in range(2)] for i in range(3)],
    'ordered_minors_mod3':[int(value) for value in minor_mod],
    'matrix_at_zero':[[int(Bzero[i,j]) for j in range(2)] for i in range(3)],
    'ordered_minors_at_zero':[int(value) for value in minors(Bzero)],
    'individual_tail_term_checks':term_checks,
    'formal_minor_contents_in_n':[str(value) for value in contents],
    'formal_common_content':str(S.factor(S.gcd_list(contents))),
    'scope':'finite coefficient arithmetic only; the infinite tail proof and complete corrected claim await independent review'
},indent=2))