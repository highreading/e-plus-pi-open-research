"""ONE NEW bounded attainment question, not a repeat of closed mod16.
All contacts/atom use DIFFERENT-passed EXACT finite source identities.
No conjectured high-precision source law, root conjectured rank formula,
network, credentials, remote code, or original-size matrix is used.
"""
from pathlib import Path
import functools,hashlib,json,math,time
HERE=Path(__file__).resolve().parent
OUT=HERE/'THETA_LITERAL_MOD4096_ATTAINMENT_AUXILIARY_RECEIPT.json'
assert not OUT.exists()
CAP,MOD=12,4096
CASES=((144,64,16,36),(272,128,16,67),(272,128,16,68))
start=time.monotonic()

def module_counts(rows):
    a=[r[:] for r in rows];counts=[]
    for level in range(CAP):
        modulus=1<<(CAP-level);size=len(a);pivot=0
        while pivot<size:
            ij=next(((i,j) for i in range(pivot,size) for j in range(pivot,size) if a[i][j]&1),None)
            if ij is None:break
            i,j=ij;a[pivot],a[i]=a[i],a[pivot]
            for row in a:row[pivot],row[j]=row[j],row[pivot]
            inverse=pow(a[pivot][pivot],-1,modulus)
            for i in range(pivot+1,size):
                factor=a[i][pivot]*inverse%modulus
                if factor:
                    for j in range(pivot+1,size):a[i][j]=(a[i][j]-factor*a[pivot][j])%modulus
                    a[i][pivot]=0
            pivot+=1
        counts.append(pivot)
        tail=[row[pivot:] for row in a[pivot:]]
        assert all(x%2==0 for row in tail for x in row)
        a=[[x//2 for x in row] for row in tail]
        if not a:return counts+[0]*(CAP-len(counts))+[0]
    return counts+[len(a)]

results=[]
for d,L,rho,p in CASES:
    n,base=d+2,d-p
    assert base+p-1==d-1
    theta=[1,0]
    for j in range(1,3*d+2):theta.append(((2*j+1)*theta[-1]+theta[-2])%MOD)
    pascal=[[1]]
    for j in range(1,3*d+3):
        v=pascal[-1];pascal.append([1]+[(v[i-1]+v[i])%MOD for i in range(1,j)]+[1])
    vmax=0
    for v in range(CAP):
        if v+(math.factorial(v)&-math.factorial(v)).bit_length()-1<CAP:vmax=v
    # Every omitted physical term has its explicit2^v and rising-product
    # v! payment. Full integer binomials remain in all retained terms.
    coeff={m:[((1<<v)*math.comb(m,v))%MOD if v<=m else 0 for v in range(vmax+1)]
           for m in range(2*d+1)}
    @functools.lru_cache(None)
    def physical(order,m):
        assert order+m<=3*d+1
        rise,ans=1,0
        for v,c in enumerate(coeff[m]):
            if v:rise=rise*(order+v)%MOD
            if c:ans=(ans+c*rise*theta[order+v])%MOD
        return ans
    suffix=[0]*(d+1);suffix[d]=1
    for h in range(d-1,-1,-1):suffix[h]=suffix[h+1]*(2*base+2*h+1)%MOD
    topterms=[(h,pascal[d][h]*suffix[h]%MOD) for h in range(d+1) if pascal[d][h]*suffix[h]%MOD]
    fall=[1]
    for h in range(1,d+1):fall.append(fall[-1]*(d-h+1)%MOD)
    atomterms=[(h,fall[h]*suffix[h]%MOD) for h in range(d+1) if fall[h]*suffix[h]%MOD]
    ratios=[0]*p;ratios[-1]=1
    for j in range(p-2,-1,-1):ratios[j]=ratios[j+1]*(d+j+1)%MOD
    rows=[]
    for j in range(p):
        contacts=[sum(c*pascal[r+j+d-h][r]*physical(r+j+d-h,base+h)
                      for h,c in topterms)%MOD for r in range(d+1)]
        actual_atom=(-1)**(base+j)*sum(pascal[d+j][h]*c for h,c in atomterms)%MOD
        rows.append([ratios[j]*actual_atom%MOD]+contacts)
    values=[]
    for i in range(p+1):
        val=1
        for t in range(d-p,d):val*=2*(d+i+t)+1
        values.append(val)
    pole=[]
    for ell in range(p+1):
        val,rem=divmod(values[0],(1<<ell)*math.factorial(ell));assert rem==0
        pole.append(val%MOD);values=[b-a for a,b in zip(values,values[1:])]
    terms=[(ell,c) for ell,c in enumerate(pole) if c]
    for z in range(d-p+2):
        j=p+z
        contacts=[sum(c*pascal[r+j-ell][r]*physical(r+j-ell,d+ell)
                      for ell,c in terms)%MOD for r in range(d+1)]
        rows.append([0]+contacts)
    assert len(rows)==n and all(len(row)==n for row in rows)
    counts=module_counts(rows);assert sum(counts)==n
    exact=counts[-1]==0
    results.append({'d':d,'L':L,'rho':rho,'p':p,'literal_top_base':base,'dimension':n,
                    'precision':CAP,'all_source_divisions': 'passed full integer/odd-unit normalization retained',
                    'capped_invariant_counts':counts,'remaining_dimension_at_cap':counts[-1],
                    'exact_auxiliary_determinant_valuation_attained':exact,
                    'determinant_valuation':sum(i*c for i,c in enumerate(counts)) if exact else None,
                    'determinant_valuation_lower':sum(i*c for i,c in enumerate(counts)),
                    'physical_terms_retained_through_v':vmax,
                    'physical_index_bound_checked_at_every_call':3*d+1,
                    'matrix_mod4096_sha256':hashlib.sha256(json.dumps(rows).encode()).hexdigest()})
    physical.cache_clear()
receipt={'scope':'NEW precision12 attainment in auxiliary literal-base complete normalized MINIMAL theta matrices only. No original-index, full source-set/tied aggregate/paired/constant-border upper or e+pi proof.',
         'network_and_credentials_denied_by_sandbox':True,'coordinator_authored':True,
         'results':results,'seconds':round(time.monotonic()-start,3),
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
OUT.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
