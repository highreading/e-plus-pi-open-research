"""One prescribed finite rank/cofactor control of the first lower-pole matrix."""
import json,math,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
p=3;d=26;A=63;r=40
def coeff(k):return ((-1)**(A-k))*math.comb(A,k)%p if 0<=k<=A else 0
M=[[coeff(r-i-j) for j in range(d)] for i in range(d)]
v=[(-1)**i%p for i in range(d)]
rows=[row[:] for row in M];origins=list(range(d));pivots=[];minorrows=[];step=0
for col in range(d):
    pivot=next((i for i in range(step,d) if rows[i][col]),None)
    if pivot is None:continue
    rows[step],rows[pivot]=rows[pivot],rows[step]
    origins[step],origins[pivot]=origins[pivot],origins[step]
    minorrows.append(origins[step]);pivots.append(col)
    inv=pow(rows[step][col],-1,p);rows[step]=[x*inv%p for x in rows[step]]
    for i in range(d):
        if i!=step:
            f=rows[i][col]
            if f:rows[i]=[(x-f*y)%p for x,y in zip(rows[i],rows[step])]
    step+=1
    if step==d:break
rank=step;free=[i for i in range(d) if i not in pivots];kernels=[]
for col in free:
    x=[0]*d;x[col]=1
    for row,pivot in enumerate(pivots):x[pivot]=-rows[row][col]%p
    assert all(sum(a*b for a,b in zip(line,x))%p==0 for line in M)
    kernels.append(x)
def determinant(matrix):
    matrix=[row[:] for row in matrix];n=len(matrix);answer=1
    for j in range(n):
        pivot=next((i for i in range(j,n) if matrix[i][j]),None)
        if pivot is None:return 0
        if pivot!=j:matrix[j],matrix[pivot]=matrix[pivot],matrix[j];answer=-answer%p
        a=matrix[j][j];answer=answer*a%p;inv=pow(a,-1,p)
        for i in range(j+1,n):
            f=matrix[i][j]*inv%p
            for k in range(j+1,n):matrix[i][k]=(matrix[i][k]-f*matrix[j][k])%p
    return answer
minor=[[M[i][j] for j in pivots] for i in minorrows];minorvalue=determinant(minor);assert minorvalue
# endpoint-zero basis columns have y^(j+1)+y^j.
endpoint=[[sum(M[i+a][j+b] for a in (0,1) for b in (0,1))%p for j in range(d-1)] for i in range(d-1)]
cofactor=determinant(endpoint)
if rank<d-1:assert cofactor==0
report={'n':65,'prime':p,'dimension':d,'A':A,'r_lower':r,'rank':rank,
  'radical_dimension':d-rank,'kernel_basis':kernels,
  'endpoint_functional_on_kernel':[sum(a*b for a,b in zip(v,x))%p for x in kernels],
  'endpoint_cofactor_vTadjMv':cofactor,
  'unit_rank_minor_rows':minorrows,'unit_rank_minor_columns':pivots,'unit_rank_minor_value':minorvalue,
  'matrix_mod3':M,'all_kernel_products_zero':True,'finite_only':True}
(OUT/'weighted_first_low_rank_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:value for k,value in report.items() if k not in ('matrix_mod3','kernel_basis')},indent=2))
