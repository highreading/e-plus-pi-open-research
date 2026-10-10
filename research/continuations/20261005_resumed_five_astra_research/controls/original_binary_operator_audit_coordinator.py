"""Bounded originalu0 divided-power operator audit, not a full scalar evaluation."""
from pathlib import Path
from math import comb
from functools import lru_cache
import hashlib,json
ROOT=Path(__file__).resolve().parent
M=20;Q=1<<M;m=4*(M-1)
b=9**18;n=4002*b;h=n//2
def depth(x):return M if not x else (x&-x).bit_length()-1
def L(x):return x-x.bit_count()
def symbols():
    out=[0]*(m+1);dp=[1]
    for a in range(M):
        scale=(1<<a)*comb(h,a)%Q
        for s,z in enumerate(dp):out[s]=(out[s]+scale*z)%Q
        dp=[sum(comb(s,j)*dp[s-j]*v for j,v in enumerate((0,-1,2,-3,3))
                 if j<=s and 0<=s-j<len(dp))%Q for s in range(len(dp)+4)]
    return out
def main():
    lam=symbols();cc=[1]
    for k in range(1,m+1):cc.append(-sum(comb(k,s)*lam[s]*cc[k-s] for s in range(1,k+1))%Q)
    for k in range(1,m+1):
        assert depth(lam[k])>=(k+3)//4 and depth(cc[k])>=(k+3)//4
    for k in range(2*m+1):
        product=sum(comb(k,s)*lam[s]*cc[k-s] for s in range(max(0,k-m),min(k,m)+1))%Q
        assert product==int(k==0)
    # Exactly bounded table:1,048,577 residues; no object has original lengthb.
    prefix=[1]
    for i in range(1,Q+1):prefix.append(prefix[-1]*(i if i%2 else 1)%Q)
    @lru_cache(None)
    def uf(N):
        out=1
        while N:
            out=out*pow(prefix[Q],N//Q,Q)*prefix[N%Q]%Q;N//=2
        return out
    def bc(N,j):
        if j<0 or j>N:return 0
        e=L(N)-L(j)-L(N-j)
        if e>=M:return 0
        return (1<<e)*uf(N)*pow(uf(j),-1,Q)*pow(uf(N-j),-1,Q)%Q
    def neg(N,j):return (-1)**j*bc(N+j-1,j)%Q
    checks=0;nonzero=0
    for s in range(1,m+1):
        for r in range(s):
            d=b+r-s
            # Derivative of the full rational series independently gives the
            # returning endpoint coefficient, compared to coefficientwiseD.
            direct=comb(b+r,s)*neg(n,b+r)%Q
            full_derivative=neg(n,s)*neg(n+s,d)%Q
            assert direct==full_derivative
            checks+=1;nonzero+=direct!=0
    out={'status':'PASS','scope':'Actual original binaryu0 at20bits: interior divided-power inverse and finite endpoint commutator only; no original Gram or relative invariant',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'u':0,'b':str(b),'n':str(n),'raw_precision':M,'operator_degree':m,
         'inverse_coefficient_residual_checks':2*m+1,'filtration_checks':2*m,
         'endpoint_commutator_checks':checks,'nonzero_endpoint_return_coefficients':nonzero,
         'largest_allocated_residue_table':Q+1,'symbol_coefficients':lam,'inverse_coefficients':cc}
    dest=ROOT/'original_binary_operator_audit_certificate.json';dest.write_text(json.dumps(out,indent=2)+'\n')
    receipt={k:v for k,v in out.items() if k not in ('symbol_coefficients','inverse_coefficients')}
    receipt['artifact_sha256']=hashlib.sha256(dest.read_bytes()).hexdigest()
    (ROOT/'original_binary_operator_audit_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
