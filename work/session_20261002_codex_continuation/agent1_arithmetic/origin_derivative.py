import sympy as s
n,c,j=s.symbols('n c j')
cut=lambda A:A.applyfunc(lambda x:s.expand(x).series(n,0,2).removeO())
N=s.Matrix([[1,n,-n],[1-n,1+n,n],[1-2*n,2-n,2+3*n]])
A=s.Matrix([1+2*c*n,2+(1+2*c)*n,5+(4+4*c)*n])
U=s.Matrix([[1,-n,n*(n+1)],[0,1,-2*n],[0,0,1]])
Z=s.Matrix([[-1,0,0],[1,-1,0],[0,1,-1],[0,0,1]])
K=cut(Z*U)
Om=s.diag(1,(n+2)**2,((n+2)*(n+1))**2,((n+2)*(n+1)*n)**2)
H=cut(K.T*Om*K)
D0=s.diag(1,n+1,(n+1)*(n+2))
Y=cut(N.adjugate()*D0*s.Matrix([j,j,j]))
W=cut(H*N.adjugate()*A+N.det()*K[0,:].T)
V=cut(Y.T*W)[0]
D=cut(Y.T*H*Y)[0]
print('K=',K,'H=',H,'Y=',Y,'W=',W,'V=',V,'D=',D,sep='\n')
