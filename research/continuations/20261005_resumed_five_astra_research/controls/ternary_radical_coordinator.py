"""Bounded exact F3 residue-block and force assembly corroboration."""
from pathlib import Path
from math import comb
import hashlib,json

OUT=Path(__file__).resolve().parent
def rank_kernel(mat,cols=None):
    a=[row[:] for row in mat];n=cols if cols is not None else len(a[0])
    piv=[];r=0
    for j in range(n):
        found=next((i for i in range(r,len(a)) if a[i][j]%3),None)
        if found is None:continue
        a[r],a[found]=a[found],a[r];inv=pow(a[r][j]%3,-1,3)
        a[r]=[x*inv%3 for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                scale=a[i][j]%3;a[i]=[(x-scale*y)%3 for x,y in zip(a[i],a[r])]
        piv.append(j);r+=1
    kernels=[]
    for j in range(n):
        if j in piv:continue
        v=[0]*n;v[j]=1
        for i,k in enumerate(piv):v[k]=-a[i][j]%3
        assert all(sum(x*y for x,y in zip(row,v))%3==0 for row in mat)
        kernels.append(v)
    return r,kernels

def coeff(D,k):return (-1)**k*comb(D,k)%3 if 0<=k<=D else 0

def main():
    data=[]
    for g,L,delta,expected in [(9,9,2,0),(9,9,4,16),(9,27,8,20)]:
        s=delta//2;D=g*delta;nu=g*s-1;rho=(g*L-1)//2;a0=(g-1)//2;eta=(L-1)//2
        full=[[coeff(D,rho-i-j) for j in range(nu)] for i in range(nu)]
        order=[i for r in range(g) for i in range(nu) if i%g==r]
        assembly=[]
        for i in order:
            r=i%g;a=i//g;row=[]
            for j in order:
                rp=j%g;b=j//g;total=r+rp
                row.append(coeff(delta,eta-(total-a0)//g-a-b) if (total-a0)%g==0 else 0)
            assembly.append(row)
        assert assembly==[[full[i][j] for j in order] for i in order]
        rank,kernels=rank_kernel(full);assert rank==expected
        endpoint=[(-1)**i%3 for i in range(nu)]
        augmented=[row+[endpoint[i]] for i,row in enumerate(full)]
        assert rank_kernel(augmented)[0]>rank
        pairings=[sum(x*y for x,y in zip(endpoint,v))%3 for v in kernels]
        assert any(pairings)
        if delta==4:
            assert len(kernels)==1 and kernels[0][14]==1 and sum(x!=0 for x in kernels[0])==1
        # Sparse auxiliary actual-force ASSEMBLY, without claiming a producer.
        H=729*g*L;r1=(H-1)//2;zeta=(H//g-1)//2
        for u in [r1-D,r1-2*D,r1-D-nu//2]:
            c=u%g;monomial=u//g
            for i in range(nu):
                for j in range(nu):
                    direct=coeff(2*D,r1-i-j-u)
                    r=i%g;rp=j%g;a=i//g;b=j//g
                    rc=(a0-r-rp)%g
                    offset=(a0-r-rp-rc)//g
                    block=coeff(2*delta,zeta+offset-a-b-monomial) if rc==c else 0
                    assert direct==block
        data.append({'g_auxiliary':g,'L_auxiliary':L,'delta':delta,'dimension':nu,
                     'rank':rank,'radical_basis':kernels,'endpoint_radical_pairings':pairings,
                     'endpoint_outside_image':True,'full_residue_block_match':True,
                     'three_sparse_force_block_checks':True})
    cert={'status':'BOUNDED_TERNARY_RESIDUE_RADICAL_AND_FORCE_ASSEMBLY_PASS','cases':data,
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'scope':'Auxiliary exact finite-field identities only. These do not prove the missing actual producer strip or an actual inverse/denominator depth.'}
    (OUT/'ternary_radical_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    brief={**cert,'cases':[{k:v for k,v in x.items() if k!='radical_basis'} for x in data]}
    (OUT/'ternary_radical_packet.json').write_text(json.dumps(brief,indent=2)+'\n')
    print(json.dumps(brief))

if __name__=='__main__':main()
