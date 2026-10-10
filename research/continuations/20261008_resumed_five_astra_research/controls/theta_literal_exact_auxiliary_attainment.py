"""NEW exact-Q singularity/attainment question on ONE bounded auxiliary.

Reuse DIFFERENT-passed exact source identities, not conjectured mod16 laws.
Prior overlap: existing raw d48 mod4 checks concern source normalization;
no exact complete literal minimal-source determinant at (48,12) was located.
Primary ordinary Bessel/partial-exponential Hankel results have different
weights/rows and are not imported as determinant evaluations here.
This answers only the specified auxiliary; never an original-family upper.
"""
from pathlib import Path
import functools,hashlib,json,math,time
H=Path(__file__).resolve().parent
OUT=H/'THETA_LITERAL_EXACT_AUXILIARY_ATTAINMENT_RECEIPT.json'
assert not OUT.exists()
start=time.monotonic();d,p=48,12;base=d-p;n=d+2
assert base+p-1==d-1
theta=[1,0]
for j in range(1,3*d+2):theta.append((2*j+1)*theta[-1]+theta[-2])
@functools.lru_cache(None)
def physical(order,m):
    assert 0<=m<=2*d and order+m<=3*d+1
    rise,ans=1,0
    for v in range(m+1):
        if v:rise*=order+v
        ans+=math.comb(m,v)*(1<<v)*rise*theta[order+v]
    return ans
suffix=[0]*(d+1);suffix[d]=1
for h in range(d-1,-1,-1):suffix[h]=suffix[h+1]*(2*base+2*h+1)
topterms=[(h,math.comb(d,h)*suffix[h]) for h in range(d+1)]
fall=[1]
for h in range(1,d+1):fall.append(fall[-1]*(d-h+1))
ratios=[0]*p;ratios[-1]=1
for j in range(p-2,-1,-1):ratios[j]=ratios[j+1]*(d+j+1)
rows=[]
for j in range(p):
    contacts=[sum(c*math.comb(r+j+d-h,r)*physical(r+j+d-h,base+h)
                  for h,c in topterms) for r in range(d+1)]
    atom=(-1)**(base+j)*sum(math.comb(d+j,h)*fall[h]*suffix[h] for h in range(d+1))
    rows.append([ratios[j]*atom]+contacts)
values=[]
for i in range(p+1):
    x=1
    for t in range(d-p,d):x*=2*(d+i+t)+1
    values.append(x)
pole=[]
for ell in range(p+1):
    x,rem=divmod(values[0],(1<<ell)*math.factorial(ell));assert rem==0
    pole.append(x);values=[b-a for a,b in zip(values,values[1:])]
for z in range(d-p+2):
    j=p+z
    contacts=[sum(c*math.comb(r+j-ell,r)*physical(r+j-ell,d+ell)
                  for ell,c in enumerate(pole)) for r in range(d+1)]
    rows.append([0]+contacts)
assert len(rows)==n and all(len(x)==n for x in rows)

def exact_bareiss_full_pivot(original):
    a=[x[:] for x in original];prev,sign=1,1;maxbits=0
    for k in range(n):
        ij=next(((i,j) for i in range(k,n) for j in range(k,n) if a[i][j]),None)
        if ij is None:return 0,k,maxbits
        i,j=ij
        if i!=k:a[i],a[k]=a[k],a[i];sign=-sign
        if j!=k:
            for row in a:row[j],row[k]=row[k],row[j]
            sign=-sign
        pivot=a[k][k]
        if k==n-1:return sign*pivot,n,maxbits
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=pivot*a[i][j]-a[i][k]*a[k][j]
                a[i][j],rem=divmod(numerator,prev);assert rem==0
                maxbits=max(maxbits,abs(a[i][j]).bit_length())
            a[i][k]=0
        prev=pivot
    raise AssertionError('unreachable')

det,rank,maxbits=exact_bareiss_full_pivot(rows)
valuation=(abs(det)&-abs(det)).bit_length()-1 if det else None
receipt={'time':time.strftime('%Y-%m-%d %H:%M:%S'),
 'scope':'ONE NEW exact rational/integer minimal-source auxiliary only; no original-index or full aggregate/paired upper or e+pi decision',
 'd':d,'p':p,'dimension':n,'literal_top_base':base,
 'network_and_credentials_denied_by_sandbox':True,'coordinator_authored':True,
 'exact_full_matrix_rank_over_Q':rank,'exact_determinant_is_zero':det==0,
 'exact_determinant_v2':valuation,'exact_determinant_bits':abs(det).bit_length(),
 'exact_determinant_signed_bytes_sha256':hashlib.sha256(
     bytes([det<0])+abs(det).to_bytes((abs(det).bit_length()+7)//8,'big')).hexdigest(),
 'maximum_bareiss_entry_bits':maxbits,'all_bareiss_divisions_exact':True,
 'all_actual_pole_divisions_exact':True,'physical_index_bound_checked_at_every_call':3*d+1,
 'odd_top_row_divisor_and_atom_column_multiplier':'o_d; determinant changes by an odd unit only',
 'matrix_sha256':hashlib.sha256(json.dumps(rows).encode()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'seconds':round(time.monotonic()-start,3)}
OUT.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
