"""ONE NEW literal-base complete theta diagnostic at binary precision4.
The prior base0/mod8 receipt is CLOSED and not rerun. Here top base=d-p;
EVERY top/bottom contact uses the passed exact source identities, including
physical base d+ell and full normalized integer pole coefficients. No keys,
network, remote code, original-size solve or complete paired upper claim.
"""
from pathlib import Path
import hashlib,json,math,time
HERE=Path(__file__).resolve().parent
OUT=HERE/'THETA_LITERAL_MOD16_EFFECTIVE_AUXILIARY_RECEIPT.json'
assert not OUT.exists()
CASES=((144,64,16,36),(272,128,16,67),(272,128,16,68))
start=time.monotonic()

def capped_counts(rows):
    a=[r[:] for r in rows];counts=[]
    for level in range(4):
        modulus=1<<(4-level);size=len(a);pivot=0
        while pivot<size:
            found=next(((i,j) for i in range(pivot,size) for j in range(pivot,size) if a[i][j]&1),None)
            if found is None:break
            i,j=found;a[pivot],a[i]=a[i],a[pivot]
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
    return counts+[len(a)]

results=[]
for d,L,rho,p in CASES:
    assert d==2*L+rho and d%32==16 and p+rho<=L-2
    n,base=d+2,d-p
    theta=[1,0]
    for j in range(1,3*d+2):theta.append(((2*j+1)*theta[-1]+theta[-2])%16)
    pascal=[[1]]
    for j in range(1,3*d+3):
        prev=pascal[-1]
        pascal.append([1]+[(prev[i-1]+prev[i])%16 for i in range(1,j)]+[1])
    # Exact physical identity, with only the independently paid v>=3
    # terms removed modulo16. No assumption about the new top law.
    def physical(order,m):
        return (theta[order]+2*m*(order+1)*theta[order+1]
                +4*math.comb(m,2)*(order+1)*(order+2)*theta[order+2])%16
    suffix=[0]*(d+1);suffix[d]=1
    for h in range(d-1,-1,-1):suffix[h]=suffix[h+1]*(2*base+2*h+1)%16
    topterms=[(h,pascal[d][h]*suffix[h]%16) for h in range(d+1) if pascal[d][h]*suffix[h]%16]
    ratios=[0]*p;ratios[-1]=1
    for j in range(p-2,-1,-1):ratios[j]=ratios[j+1]*(d+j+1)%16
    rows=[];topchecks=0
    for j in range(p):
        contact=[sum(c*pascal[r+j+d-h][r]*physical(r+j+d-h,base+h) for h,c in topterms)%16 for r in range(d+1)]
        def kr(shift,r):return sum(c*pascal[r+shift+t][r]*theta[r+shift+t] for t,c in enumerate(pascal[d]))%16
        for r,x in enumerate(contact):
            expected=(kr(j,r)+2*base*(j+1)*kr(j+1,r)
                      +4*math.comb(base,2)*(j+1)*(j+2)*kr(j+2,r))%16
            assert x==expected
            topchecks+=1
        # Entire atom column is multiplied by the ACTUAL odd o_d, a unit.
        # Other factors are retained; no original integer content is divided.
        rows.append([(ratios[j]*(-1)**(base+j))%16]+contact)
    # Literal Q_I values at actual finite residual rows, BEFORE division.
    values=[]
    for i in range(p+1):
        q=1
        for t in range(d-p,d):q*=2*(d+i+t)+1
        values.append(q)
    pole=[]
    for ell in range(p+1):
        q,rem=divmod(values[0],(1<<ell)*math.factorial(ell))
        assert rem==0
        pole.append(q%16)
        values=[b-a for a,b in zip(values,values[1:])]
    terms=[(ell,c) for ell,c in enumerate(pole) if c]
    for z in range(d-p+2):
        j=p+z
        contact=[sum(c*pascal[r+j-ell][r]*physical(r+j-ell,d+ell) for ell,c in terms)%16 for r in range(d+1)]
        rows.append([0]+contact)
    assert len(rows)==n and all(len(row)==n for row in rows)
    counts=capped_counts(rows)
    chi=L-p-rho+1 if L%3==1 else p+rho+1
    assert n-counts[0]==chi and sum(counts)==n
    results.append({'d':d,'L':L,'rho':rho,'p':p,'literal_top_base':base,
                    'dimension':n,'parity_corank':chi,'capped_counts_v0_v1_v2_v3_vge4':counts,
                    'complete_effective_ranks':counts[1:4],
                    'complete_determinant_valuation_lower_at_precision4':sum(i*c for i,c in enumerate(counts)),
                    'actual_top_mod16_coordinates_checked':topchecks,
                    'full_pole_integer_divisions_checked':len(pole),
                    'matrix_mod16_sha256':hashlib.sha256(json.dumps(rows).encode()).hexdigest()})
receipt={'scope':'NEW auxiliary literal top-base d-p/physical-pole complete minimal theta matrix modulo16. Not original indices, complete I/J/U/tied aggregation, constant border, upper, or e+pi proof.',
         'coordinator_authored':True,'network_and_credentials_denied_by_sandbox':True,
         'results':results,'seconds':round(time.monotonic()-start,3),
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
OUT.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
