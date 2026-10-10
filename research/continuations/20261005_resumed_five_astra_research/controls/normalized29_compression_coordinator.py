"""Personally authored independent compression audit from saved initializer.

No growing original matrix is evaluated. This preserves every digit of each
bounded auxiliary argument and compares different exact representations.
"""
from pathlib import Path
from math import comb
import hashlib,json
from onecarry29_coordinator import full_recurrence

OUT=Path(__file__).resolve().parent
P=29
def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%P
    return c
def pi(m): return [comb(m,j)**2%P for j in range(m+1)]
def lucas(n,k):
    if k<0 or k>n:return 0
    result=1
    while n or k:
        a,b=n%P,k%P
        if b>a:return 0
        result=result*comb(a,b)%P;n//=P;k//=P
    return result
def tails(C,E,L):
    if L<0:return 0,0
    T=V=0
    for u in range(L+1):
        x=lucas(C,u)*lucas(E+L-u,L-u)%P
        x=x*x%P; T=(T+x)%P; V=(V+(2*u-L)*x)%P
    return T,V
def product_coeff(seed,C,E,R):
    polys=[x%P for x in seed]
    C//=P;E//=P;shift=P
    while C or E or shift<=R:
        a=conv(pi(C%P),pi(P-1-E%P))
        result=[0]*(R+1)
        for i,x in enumerate(polys):
            if i>R:break
            for j,y in enumerate(a):
                if i+shift*j>R:break
                result[i+shift*j]=(result[i+shift*j]+x*y)%P
        polys=result;C//=P;E//=P;shift*=P
    return polys[R] if R<len(polys) else 0

def main():
    initial=json.loads((OUT/'onecarry29_initialization_406.json').read_text())
    table={(r['G_low_digit'],r['sum_carry']):r for r in initial}
    seeds=[];checks=[]
    expected9=[[11,3,5,26],[25,5,10,24],[2,26,8,3],[17,6,17,23],
               [17,7,22,22],[17,6,27,23],[9,26,5,3],[18,5,11,24],[7,3,27,26]]
    lambdas=[7,9,25,2,27,7,9,8,27,9,1,9,19,13,10,26,10,25,10,14]
    for z in range(P):
        c=(11*z+18)%P;e=(2*c+1)%P;f=28-e
        coeff=[]
        for sig in (0,1):
            row=table[z,sig];Z=row['Z_mod29']
            assert Z==[0,Z[1],Z[2],Z[1],0,(-Z[2])%P]
            coeff.extend([(row['r_mod29']+2*Z[1]*(3*c+1))%P,2*(Z[2]-Z[1])%P])
        if z<9:assert coeff==expected9[z]
        else:assert coeff==[lambdas[z-9],0,0,0]
        a0,b0,a1,b1=coeff
        pc,pf=pi(c),pi(f);prod=conv(pc,pf)
        dpc=[j*x%P for j,x in enumerate(pc)];dpf=[j*x%P for j,x in enumerate(pf)]
        p1,p2=conv(dpc,pf),conv(pc,dpf)
        centered=[(x-y)%P for x,y in zip(p1,p2)]
        seed=[0]*(len(prod)+1)
        for j in range(len(prod)):
            seed[j]=(seed[j]+a0*prod[j]+b0*centered[j])%P
            seed[j+1]=(seed[j+1]+a1*prod[j]+b1*centered[j])%P
        while len(seed)>1 and seed[-1]==0:seed.pop()
        assert len(seed)<=44
        seeds.append({'z':z,'c':c,'e':e,'f':f,'a0_b0_a1_b1':coeff,'seed':seed})
        for R in [0,1,2,3,5,8,13,20,28,29,30,57,100,128,841]:
            C=2001*R+69*z+47;E=2*C+1;H=20+29*z+841*R
            T,V=tails(C,E,R);T1,V1=tails(C,E,R-1)
            scalar=(a0*T+b0*V+a1*T1+b1*V1)%P
            poly=product_coeff(seed,C,E,R)
            rec=full_recurrence(H)
            assert rec%P==0 and scalar==rec//P==poly,(z,R,scalar,rec,poly)
            checks.append({'z':z,'R':R,'H_auxiliary':H,'normalized_T_residue':scalar,'all_digit_product_matches':True,'full_recurrence_matches':True})
    cert={'status':'NORMALIZED29_COMPRESSION_PASS','seeds':seeds,'checks':checks,
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'initializer_sha256':hashlib.sha256((OUT/'onecarry29_initialization_406.json').read_bytes()).hexdigest(),
          'scope':'29 finite scalar seeds and435 complete bounded auxiliary tails; no all-depth actual norm/mixed theorem.'}
    target=OUT/'normalized29_compression_certificate.json';target.write_text(json.dumps(cert,indent=2)+'\n')
    receipt={'seed_count':len(seeds),'check_count':len(checks),'all_pass':True,
             'max_seed_degree':max(len(x['seed'])-1 for x in seeds),
             'originally_reachable_annihilating_prefix_z9_R28_residue':next(x['normalized_T_residue'] for x in checks if x['z']==9 and x['R']==28),
             'artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'scope':cert['scope']}
    (OUT/'normalized29_compression_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
