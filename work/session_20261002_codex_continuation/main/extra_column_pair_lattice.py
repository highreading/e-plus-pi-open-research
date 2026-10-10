from pathlib import Path
from math import factorial,gcd,lcm
import json,sys
import sympy as sp
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
sys.set_int_max_str_digits(1000000)
ROOT=Path('work/session_20261002_codex_continuation/main')
D=[1]
for n in range(1,100):D.append(n*D[-1]+(-1)**n)
def rat(r):return -sp.Integer(factorial(2*r))+4*sum((sp.Rational((-1)**(r-a),2*a-1)for a in range(1,r+1)),sp.Integer(0))
rows=[]
for k in range(1,7):
 C=sp.Matrix(k,2*k+1,lambda i,j:D[2*(i+j)]-(-1)**(i+j))
 R=sp.Matrix(k,2*k+1,lambda i,j:rat(i+j));V=sp.Matrix(k,2*k+1,lambda i,j:(-1)**(i+j))
 sm,left,right=smith_normal_decomp(DomainMatrix.from_Matrix(C).convert_to(ZZ));U=left.to_Matrix();T=right.to_Matrix();SM=sm.to_Matrix()
 assert U*C*T==SM and abs(T.det())==1 and all(SM[i,i]!=0 for i in range(k))
 Q=T[:,k:];assert C*Q==sp.zeros(k,k+1)
 d=lcm(*(int(a.q)for a in R*Q));H0=d*R*Q;H1=d*V*Q
 pair=[]
 for j in range(k+1):
  cols=[l for l in range(k+1)if l!=j];z0=H0[:,cols].det();z1=(H0+H1)[:,cols].det()-z0
  assert (H0+2*H1)[:,cols].det()==z0+2*z1
  pair.append([(-1)**j*z0,(-1)**j*z1])
 A=sp.Matrix(2,k+1,lambda i,j:pair[j][i]);assert A.rank()==2
 B=hermite_normal_form(A);assert B.shape==(2,2)
 sn=smith_normal_form(A,domain=ZZ);d1=abs(int(sn[0,0]));d2=abs(int(sn[1,1]));index=abs(int(B.det()))
 assert index==d1*d2 and d2%d1==0
 # The exact full coefficient-lattice image and minimal multiples for fresh rational directions.
 _,ls,rt=smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(ZZ));LA=ls.to_Matrix();RA=rt.to_Matrix();SN=LA*A*RA
 assert LA*A*RA==SN and abs(LA.det())==abs(RA.det())==1
 examples=[]
 for bb,aa in [(1,1),(-6,1),(-41,7),(-293,50)]:
  v=sp.Matrix([bb,aa]);vv=B.inv()*v;ell=lcm(*(int(a.q)for a in vv));assert d2%ell==0
  rhs=LA*(ell*v);z=sp.zeros(k+1,1)
  for i in range(2):z[i]=rhs[i]/SN[i,i];assert z[i].q==1
  w=RA*z;assert A*w==ell*v and all(a.q==1 for a in w)
  # A wedge cofactor vector w is realizable by k integer columns. Use Smith to complete w/g.
  wg=gcd(*(int(a)for a in w));wp=w/wg
  ss,uu,tt=smith_normal_decomp(DomainMatrix.from_Matrix(wp.T).convert_to(ZZ));TC=tt.to_Matrix();assert abs(ss.to_Matrix()[0,0])==1
  # TC[:,1:] spans kernel wp.T, whose oriented maximal minors equal +/-wp.
  Z=TC[:,1:];co=sp.Matrix([(-1)**j*Z.extract([i for i in range(k+1)if i!=j],range(k)).det()for j in range(k+1)])
  sg=int(co[0]/wp[0])if wp[0]else next(int(co[i]/wp[i])for i in range(k+1)if wp[i])
  assert sg in(-1,1)and co==sg*wp
  Z[:,0]=Z[:,0]*wg*sg;assert sp.Matrix([(-1)**j*Z.extract([i for i in range(k+1)if i!=j],range(k)).det()for j in range(k+1)])==w
  F0=(H0*Z).det();F1=((H0+H1)*Z).det()-F0;assert sp.Matrix([F0,F1])==ell*v
  content=gcd(int(F0),int(F1));assert content==ell and abs(int(F1)//content)==aa
  examples.append({'primitive_pair':[bb,aa],'minimum_lattice_multiple':str(ell),'parameter_vector':list(map(str,w)),'wedge_max_coefficient_bits':max(abs(int(a)).bit_length()for a in Z),'final_content':str(content),'actual_q':str(aa),'exact_full_realization':True})
 # Whole stacked maximal-minor coefficient lattice, without the kernel basis.
 L=lcm(*(2*a-1 for a in range(1,3*k)))
 assert L%d==0
 SA0=C.col_join(L*R);SA1=C.col_join(L*(R+V))
 stackpairs=[]
 for j in range(2*k+1):
  cols=[a for a in range(2*k+1)if a!=j];b0=SA0[:,cols].det();b1=SA1[:,cols].det()-b0
  stackpairs.append([(-1)**j*b0,(-1)**j*b1])
 STACK=sp.Matrix(2,2*k+1,lambda i,j:stackpairs[j][i]);dc=abs(int(sp.prod(SM[i,i]for i in range(k))))
 assert hermite_normal_form(STACK)==dc*(L//d)**k*B
 sstack=smith_normal_form(STACK,domain=ZZ)
 assert [abs(int(sstack[i,i]))for i in range(2)]==[dc*(L//d)**k*d1,dc*(L//d)**k*d2]
 # Rank-two criterion is the full bordered determinant with evaluation at -1.
 bordered=C.col_join(R).col_join(sp.Matrix(1,2*k+1,lambda i,j:(-1)**j)).det();assert bordered!=0
 rows.append({'k':k,'saturated_kernel_basis':[[str(Q[i,j])for i in range(Q.rows)]for j in range(Q.cols)],'entry_clearer':str(d),'coefficient_pair_map':[[str(A[i,j])for j in range(A.cols)]for i in range(2)],'hermite_image_basis':[[str(B[i,j])for j in range(2)]for i in range(2)],'smith_invariants':[str(d1),str(d2)],'lattice_index':str(index),'universal_full_entry_clearer':str(L),'matching_determinantal_divisor':str(dc),'stack_kernel_lattice_identity':True,'bordered_rank_two_determinant':str(bordered),'examples':examples,'exact_saturation_and_realization':True})
 print('EXTRA_COLUMN',k,'indexbits',index.bit_length(),'exponentbits',d2.bit_length(),flush=True)
(ROOT/'EXTRA_COLUMN_PAIR_LATTICE_CERTIFICATE.json').write_text(json.dumps({'status':'PASS_NEW_SATURATED_EXTRA_COLUMN_COEFFICIENT_LATTICE','rows':rows,'scope':'Exact integer coefficient map, saturated kernel, full rational-direction realization and final gcd. Arbitrary directions alone supply no approximation or irrationality proof.'},indent=2)+'\n')
