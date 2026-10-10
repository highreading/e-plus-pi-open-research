"""New d80,p8/9 first-effective-rank check; no closed source scan repeated.

Coordinator-authored from DIFFERENT-passed exact physical source laws.
It checks A4turn27's NEW first Schur rank claim only on four auxiliaries.
No original-index upper or coordinate-identification theorem is inferred.
"""
from pathlib import Path
import functools,hashlib,json,math,time
H=Path(__file__).resolve().parent
OUT=H/'THETA_FIRST_SCHUR_NEW_AUXILIARY_RECEIPT.json'
assert not OUT.exists()
start=time.monotonic()
L,rho,d=32,16,80
theta=[1,0]
for j in range(1,3*d+2):theta.append(((2*j+1)*theta[-1]+theta[-2])%4)
@functools.lru_cache(None)
def physical(order,m):
    assert 0<=m<=2*d and order+m<=3*d+1
    # v>=2 has v+v2(v!)>=3, so vanishes mod4 before any division.
    return (theta[order]+2*m*(order+1)*theta[order+1])%4

def parity_rank(a):
    rows=[sum((x&1)<<j for j,x in enumerate(row)) for row in a]
    rank=0
    for col in range(len(a[0]) if a else 0):
        k=next((k for k in range(rank,len(rows)) if (rows[k]>>col)&1),None)
        if k is None:continue
        rows[rank],rows[k]=rows[k],rows[rank]
        for i in range(rank+1,len(rows)):
            if (rows[i]>>col)&1:rows[i]^=rows[rank]
        rank+=1
    return rank

def full_unit_elimination(original):
    a=[row[:] for row in original];n=len(a);pivots=[];k=0
    while k<n:
        ij=next(((i,j) for i in range(k,n) for j in range(k,n) if a[i][j]&1),None)
        if ij is None:break
        i,j=ij;pivots.append([k,i,j,a[i][j]])
        a[i],a[k]=a[k],a[i]
        for row in a:row[j],row[k]=row[k],row[j]
        inv=pow(a[k][k],-1,4)
        a[k]=[(x*inv)%4 for x in a[k]]
        for i in range(k+1,n):
            c=a[i][k]
            if c:
                a[i]=[(x-c*y)%4 for x,y in zip(a[i],a[k])]
        k+=1
    s=[row[k:] for row in a[k:]]
    assert all(x%2==0 for row in s for x in row)
    quotient=[[x//2 for x in row] for row in s]
    return k,quotient,pivots,a

cases=[]
for p in (8,9):
    # Minimal top source pattern at the literal base0 required by FULL27.
    suffix=[0]*(d+1);suffix[d]=1
    for h in range(d-1,-1,-1):suffix[h]=suffix[h+1]*(2*h+1)%4
    topterms=[(h,math.comb(d,h)*suffix[h]%4) for h in range(d+1)]
    fall=[1]
    for h in range(1,d+1):fall.append(fall[-1]*(d-h+1)%4)
    ratios=[0]*p;ratios[-1]=1
    for j in range(p-2,-1,-1):ratios[j]=ratios[j+1]*(d+j+1)%4
    top=[]
    for j in range(p):
        contacts=[sum(c*math.comb(rr+j+d-h,rr)*physical(rr+j+d-h,h)
                      for h,c in topterms)%4 for rr in range(d+1)]
        atom=(-1)**j*sum(math.comb(d+j,h)*fall[h]*suffix[h] for h in range(d+1))%4
        # Top row /o_d and atom column *o_d: complete odd-unit normalization.
        top.append([ratios[j]*atom%4]+contacts)
    P=p//2;eps=p%2;r=rho//2;Q=L-P;aa=L-p-r
    powers=[];e=1
    while e<L:powers.append(e);e*=2
    C=[[sum(math.comb(aa,z) if 0<=z<=aa else 0
            for z in (Q-eps+i-r-j-e for e in powers))%2
        for j in range(P)] for i in range(P+eps)]
    cr=parity_rank(C);pred1=d+2-(p+rho+1);pred2=rho+1+cr
    for shifted in (False,True):
        I=list(range(d-p,d))
        if shifted:I[0]-=1
        values=[math.prod(2*(d+i+t)+1 for t in I) for i in range(p+1)]
        pole=[]
        for ell in range(p+1):
            value,rem=divmod(values[0],(1<<ell)*math.factorial(ell));assert rem==0
            pole.append(value%4);values=[b-a for a,b in zip(values,values[1:])]
        rows=[x[:] for x in top]
        for z in range(d-p+2):
            j=p+z
            contacts=[sum(c*math.comb(rr+j-ell,rr)*physical(rr+j-ell,d+ell)
                          for ell,c in enumerate(pole))%4 for rr in range(d+1)]
            rows.append([0]+contacts)
        assert len(rows)==d+2 and all(len(x)==d+2 for x in rows)
        leading,schur,pivots,transformed=full_unit_elimination(rows)
        divided=parity_rank(schur)
        cases.append({'p':p,'I':I,'top_base':0,'matrix_dimension':d+2,
            'actual_leading_rank':leading,'predicted_leading_rank':pred1,
            'actual_first_divided_rank':divided,'predicted_first_divided_rank':pred2,
            'actual_remaining_first_divided_corank':len(schur)-divided,
            'explicit_C':C,'C_rank':cr,'all_predictions_pass':leading==pred1 and divided==pred2,
            'unit_pivot_operations':pivots,'transformed_matrix_mod4':transformed,
            'complete_divided_Schur_mod2':schur,
            'matrix_sha256':hashlib.sha256(json.dumps(rows).encode()).hexdigest()})
receipt={'time':time.strftime('%Y-%m-%d %H:%M:%S'),
 'scope':'FOUR NEW d80 base0 auxiliaries only; full first Schur rank, not proof of coordinate equality/upper/original family',
 'L':L,'rho':rho,'d':d,'physical_maximum_checked_at_every_call':3*d+1,
 'network_and_credentials_denied_by_sandbox':True,'coordinator_authored':True,
 'all_actual_pole_divisions_exact':True,'all_predictions_pass':all(c['all_predictions_pass'] for c in cases),
 'cases':cases,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'seconds':round(time.monotonic()-start,3)}
OUT.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='cases'}))
for c in cases:print(json.dumps({k:v for k,v in c.items() if k not in ('I','unit_pivot_operations','transformed_matrix_mod4','complete_divided_Schur_mod2')}))
