import sympy as S
from pathlib import Path
sig=S.sqrt(2); M=1+sig; a=sig/(2*M); beta=sig*M/2; rho=1/sig
x,h=S.symbols('x h'); ii=S.I
simp=lambda z:S.simplify(S.expand(z))
def gauss(P,curv):
    P=S.Poly(S.expand(P),x)
    return simp(sum(c*S.factorial2(j-1)/(2*curv)**(j//2) for (j,),c in P.terms() if j%2==0))
def intcoeff(curv,k,phase,order=3):
    d=curv/12-curv**2/2; f=-curv/360+curv**2/12-curv**3/3
    g=curv/20160-curv**2/160+curv**3/12-curv**4/4
    delta=[0,ii*(k-phase)*x,phase*x*x/2+d*x**4,ii*phase*x**3/6,-phase*x**4/24+f*x**6,-ii*phase*x**5/120,phase*x**6/720+g*x**8]
    es=[S.Integer(1)]
    for m in range(1,2*order+1):
        es.append(S.expand(sum(j*delta[j]*es[m-j] for j in range(1,m+1))/m))
    return [gauss(es[2*j],curv) for j in range(order+1)]
def quotient(A,B,order):
    C=[]
    for j in range(order+1):
        C.append(simp((A[j]-sum(B[k]*C[j-k] for k in range(1,j+1)))/B[0]))
    return C
hc={k:intcoeff(a,k,sig) for k in range(-2,3)}
hn={k:quotient(hc[k],hc[0],3) for k in hc}
HH=S.Matrix(3,3,lambda i,j:sum(hn[j-i][k]*h**k for k in range(4)))
AR=HH.adjugate().row(2)
avec=[simp(2*a*(-sig)**i*sum(S.expand(AR[i]).coeff(h,j+1)*h**j for j in range(3))) for i in range(3)]
fp0=intcoeff(a,0,0,2); fm0=intcoeff(beta,0,0,2)
pm={k:quotient(intcoeff(a,k,0,2),fp0,2) for k in range(3)}
mm={k:quotient(intcoeff(beta,k,0,2),fm0,2) for k in range(3)}
fr=[simp(sum(S.binomial(i,k)*rho**k*sum(pm[k][j]*h**j for j in range(3)) for k in range(i+1))) for i in range(3)]
gr=[simp(sum(S.binomial(i,k)*(-rho)**k*sum(mm[k][j]*h**j for j in range(3)) for k in range(i+1))) for i in range(3)]
num=S.expand(sum(avec[i]*gr[i] for i in range(3)))
den=S.expand(sum(avec[i]*fr[i] for i in range(3)))
con=quotient([num.coeff(h,j) for j in range(3)],[den.coeff(h,j) for j in range(3)],2)
scalar=quotient(fm0,fp0,2)
full=[simp(M**2*sum(con[k]*scalar[j-k] for k in range(j+1))) for j in range(3)]
result='\n'.join([f'normalized_H_moment_coefficients={hn}',f'cofactor_coefficients={avec}',f'forcing_ratios={fr}',f'log_ratios={gr}',f'scalar_ratio_coefficients={scalar}',f'normalized_top_error_coefficients={full}',f'eta_top={full[2]}',f'eta_actual_Gram={simp(full[2]-1)}',f'coordinate_second_coefficients={[simp(full[2]-j) for j in [2,2,1,0]]}'])
print(result)
Path(__file__).with_suffix('.txt').write_text(result+'\n')

