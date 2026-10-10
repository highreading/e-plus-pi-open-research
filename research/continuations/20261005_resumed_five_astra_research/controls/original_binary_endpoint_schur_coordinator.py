"""Personally authored ORIGINALu0 complete finite endpoint Schur audit.

Only bounded lower indices and matrix dimensions are allocated. This advances
the endpoint operator solve; it does not compute the weighted Gram pair.
"""
from pathlib import Path
from math import comb
import hashlib,json,resource
from original_binary_operator_audit_coordinator import symbols,b,n,M,Q,m
resource.setrlimit(resource.RLIMIT_CPU,(120,120))
ROOT=Path(__file__).resolve().parent
def mm(A,B):return [[sum(x*y for x,y in zip(row,col))%Q for col in zip(*B)] for row in A]
def tr(A):return [list(row) for row in zip(*A)]
def eye(k):return [[int(i==j) for j in range(k)] for i in range(k)]
def inv(A):
    z=[r[:]+s for r,s in zip(A,eye(len(A)))]
    for k in range(len(A)):
        assert z[k][k]%2==1
        u=pow(z[k][k],-1,Q);z[k]=[x*u%Q for x in z[k]]
        for j in range(len(A)):
            if j!=k:
                f=z[j][k]
                if f:z[j]=[(x-f*y)%Q for x,y in zip(z[j],z[k])]
    assert [r[:len(A)] for r in z]==eye(len(A))
    return [r[len(A):] for r in z]
def lowbinom(N,limit,negative=False):
    out=[1];exact=1
    for d in range(1,limit+1):
        exact=exact*((-N-d+1) if negative else N-d+1)//d
        out.append(exact%Q)
    return out
def main():
    lam=symbols();cc=[1]
    for s in range(1,m+1):cc.append(-sum(comb(s,t)*lam[t]*cc[s-t] for t in range(1,s+1))%Q)
    neg=lowbinom(n,3*m-1,True);pos=lowbinom(n,m-1)
    # d=b-j; all required F rows have1<=d<=152.
    F=[[-sum(neg[d+v]*pos[r-v] for v in range(r+1))%Q for r in range(m)]
       for d in range(2*m,0,-1)]
    Kbar=[[lam[m+r-t]*comb(b+r,m+r-t)%Q if 1<=m+r-t<=m else 0
           for t in range(m)] for r in range(m)]
    G=[]
    for t in range(m):
        j=b-m+t
        G.append([sum(cc[s]*comb(j,s)*F[m+t-s][r] for s in range(m+1))%Q
                  for r in range(m)])
    S=mm(G,Kbar)
    for i in range(m):S[i][i]=(S[i][i]+1)%Q
    assert [[x%2 for x in row] for row in S]==eye(m)
    Sinv=inv(S)
    assert mm(S,Sinv)==eye(m) and mm(Sinv,S)==eye(m)
    # Independently solve H^T Z=E^T over228 terminal coordinates, with
    # 76 additional lower rows verifying the inverse's support cutoff.
    origin=b-3*m;Z=[[0]*m for _ in range(3*m)]
    for i in range(3*m-1,-1,-1):
        j=origin+i
        rhs=[int(j==b-m+t) for t in range(m)]
        weights=[(s,lam[s]*comb(j+s,s)%Q) for s in range(1,min(m,3*m-1-i)+1)]
        Z[i]=[(rhs[t]-sum(w*Z[i+s][t] for s,w in weights))%Q for t in range(m)]
    assert all(x==0 for row in Z[:m] for x in row)
    FtZ=mm(tr(F),Z[m:])
    Sadj=mm(tr(Kbar),FtZ)
    for i in range(m):Sadj[i][i]=(Sadj[i][i]+1)%Q
    assert Sadj==tr(S)
    nonid=sum(S[i][j]!=int(i==j) for i in range(m) for j in range(m))
    cert={'status':'PASS','scope':'Complete bounded originalu0 finite endpoint Schur operator solve at20bits; no weighted Gram output',
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'u':0,'b':str(b),'n':str(n),'precision_bits':M,'operator_degree':m,
          'largest_small_binomial_lower_index':3*m-1,'largest_solve_dimension':m,
          'padded_adjoint_rows':3*m,'largest_matrix_shape':[3*m,m],
          'nonidentity_schur_entries':nonid,'unit_parity_checks':m*m,
          'inverse_product_entries_checked':2*m*m,'transpose_entries_checked':m*m,
          'lower_padded_zero_entries_checked':m*m,
          'S_end':S,'S_end_inverse':Sinv,'G':G,'Kbar':Kbar,
          'original_norm_pair_computed':False,'original_length_array_allocated':False}
    out=ROOT/'original_binary_endpoint_schur_certificate.json';out.write_text(json.dumps(cert,indent=2)+'\n')
    receipt={k:v for k,v in cert.items() if k not in ('S_end','S_end_inverse','G','Kbar')}
    receipt['artifact_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
    (ROOT/'original_binary_endpoint_schur_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
