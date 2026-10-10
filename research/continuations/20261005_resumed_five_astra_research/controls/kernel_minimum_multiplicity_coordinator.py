"""Minimum-path multiplicity parity: an extension of the existing content DP."""
from pathlib import Path
from math import comb
import hashlib,json
OUT=Path(__file__).resolve().parent
CNEW=[[44,95,70,96,64],[52,76,80,0,0],[24,32,64,0,0],[64,0,0,0,0]]

def minimum_count(C,D):
    states={(0,0,0):(0,1)}
    for i in range(1+(2*C+D).bit_length()):
        nxt={};ci=(C>>i)&1;di=(D>>i)&1;ai=((2*C)>>i)&1
        for (a,h,w),(cost,count) in states.items():
            for tau in (0,1):
                rho=(ci-tau-a)%2;delta=(di-tau-h)%2
                ap=(tau+rho+a-ci)//2;hp=(tau+delta+h-di)//2
                assert ap in (0,1) and hp in (0,1)
                wp=(ai+delta+w)//2;key=(ap,hp,wp);nc=cost+ap+wp
                if key not in nxt or nc<nxt[key][0]:nxt[key]=(nc,count)
                elif nc==nxt[key][0]:nxt[key]=(nc,nxt[key][1]+count)
        states=nxt
    return states[(0,0,0)]

def model(C,D):
    xi=(D-1)//2
    aa=[sum(CNEW[i][j]*comb(xi,i) for i in range(4)) for j in range(5)]
    total=0
    for t in range(D):
        B=comb(C,t)*comb(2*C+D-t,D-t)
        total+=B*B*sum(aa[j]*comb(t,j) for j in range(5))
    B=comb(C,D);total+=B*B*(11+120*xi+32*comb(xi,2))
    return total

def main():
    aux=[]
    for D in range(1,64,2):
        C=4002*D+2532;mu,count=minimum_count(C,D)
        vals=[t.bit_count()+(C-t).bit_count()-C.bit_count()+(D-t).bit_count()+(2*C).bit_count()-(2*C+D-t).bit_count() for t in range(D+1)]
        assert mu==min(vals) and count==vals.count(mu)
        assert all(t%2==0 for t,v in enumerate(vals) if v==mu)
        S=model(C,D);assert S%(1<<(2*mu+2))==0
        parity=(S>>(2*mu+2))%2;pred=((D-1)//2*count)%2
        assert parity==pred
        aux.append({'D_auxiliary':D,'mu':mu,'minimizer_count':count,'model_next_bit':parity,'direct_minimum_count_and_model_match':True})
    known=json.loads((OUT/'binary_kernel_structure_packet.json').read_text())['actual_original_kernel_checks']
    actual=[]
    for item in known:
        D=int(item['D']);C=int(item['C']);mu,count=minimum_count(C,D)
        assert mu==item['kernel_content_depth']
        xi=(D-1)//2
        actual.append({'u_original':item['u_original'],'mu':mu,'minimum_multiplicity_parity':count%2,
                       'minimum_multiplicity_bits':count.bit_length(),'xi_parity':xi%2,
                       'model_normalized_next_bit':xi*count%2,
                       'actual_norm_transfer_established':False})
    cert={'status':'MINIMUM_MULTIPLICITY_AND_MODEL_PAIRING_CHECKS_PASS','auxiliary_checks':aux,
          'actual_original_multiplicity_parities':actual,
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'scope':'Exact original kernel minima/multiplicities and bounded direct MODEL pairing checks. No arbitrary-precision actual norm or relative valuation follows.'}
    (OUT/'kernel_minimum_multiplicity_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps({'status':cert['status'],'actual_original_multiplicity_parities':actual,'auxiliary_check_count':len(aux)}))

if __name__=='__main__':main()
