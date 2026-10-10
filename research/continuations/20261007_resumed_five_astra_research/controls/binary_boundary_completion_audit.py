"""Parent-authored exact finite audit of new complete binary representations.

Auxiliary small b only. Full original-length valuation claims are not inferred.
"""
from pathlib import Path
from math import factorial
import hashlib, json, time
from finite_binary_profile_audit import choose, product, inverse, difference
ROOT=Path(__file__).resolve().parent

def audit(b,L):
    n=4002*b;mod=2**L;m=4*(L-1);d=min(b,m);T=2*L-1;V=T+m
    lam=[1,-n]
    for s in range(1,m+1):lam.append((s-n)*lam[-1]+(s*n-s*(s-1)//2)*lam[-2])
    cs=[1]
    for s in range(1,m+1):cs.append(-sum(choose(s,r)*lam[r]*cs[s-r] for r in range(1,s+1)))
    def source_col(column):
        return [sum(choose(n,column-r)*sum(lam[s]*choose(r+s,s)*choose(n+i,r+s)
                   for s in range(m+1)) for r in range(column+1))%mod for i in range(b)]
    A=[list(row) for row in zip(*(source_col(j) for j in range(b)))];Ai=inverse(A,mod)
    U=[[choose(n,j-i)%mod for j in range(b)] for i in range(b)]
    Ui=inverse(U,mod)
    P=[[choose(i,j)%mod for j in range(b)] for i in range(b)];Pi=inverse(P,mod)
    Hi=[[cs[i-j]*choose(i,j)%mod if i>=j else 0 for j in range(b)] for i in range(b)]
    K=[[lam[d+r-t]*choose(b+r,d+r-t)%mod if 0<=d+r-t<=m else 0 for t in range(d)] for r in range(m)]
    F=[[(-sum(choose(-n,b+q-j)*choose(n,v-q) for q in range(v+1)))%mod
        for v in range(V+1)] for j in range(b)]
    HiF=product(Hi,F,mod);G=HiF[b-d:]
    S=product([row[:m] for row in G],K,mod)
    for i in range(d):S[i][i]=(S[i][i]+1)%mod
    Si=inverse(S,mod)
    fails=[]
    def check(label,got,wanted):
        dd=difference(got,wanted,mod)
        if dd:fails.append({'identity':label,'nonzero_count':len(dd),'first':dd[:4]})
    def jentry(j,col):
        return sum(cs[s]*choose(-n,r)*choose(j,s-r)*choose(-2*n-r,col-j+s-r)
                   for s in range(m+1) for r in range(s+1))%mod
    J=[[jentry(j,col) for col in range(b+V+1)] for j in range(b+1)]
    # Compare the normal-ordered formula to independent finite matrix operators.
    size=b+V+m+1
    UU=[[choose(-n,j-i)%mod for j in range(size)] for i in range(size)]
    HH=[[cs[i-j]*choose(i,j)%mod if 0<=i-j<=m else 0 for j in range(size)] for i in range(size)]
    literal=product(product(UU[:b+1],HH,mod),UU,mod)
    check('integral normal ordering (3.3)',J,[row[:b+V+1] for row in literal])

    vec=[[2*i+1] for i in range(b)]
    zf=product(Ai,vec,mod)
    # The actual finite Schur solve supplies the same tail of U_n zf.
    direct_tail=product(U,zf,mod)[b-d:]
    Df=product(product(product(Hi,Ui,mod),Pi,mod)[b-d:],vec,mod)
    zeta=product(Si,Df,mod)
    check('first-force actual finite Schur tail',zeta,direct_tail)
    bet=product(K,zeta,mod)
    Um=[[choose(n,j-i)%mod for j in range(m)] for i in range(m)]
    eta=product(Um,bet,mod)
    qf=product(Pi,vec,mod)+eta+[[0] for _ in range(V+1-m)]
    got=product(J,qf,mod)
    check('first-force complete exterior completion (4.4)',got,zf+[[0]])

    # Check the displayed head-profile (6.2) against J applied to each
    # contact-truncated P^-1 basis vector. Includes every head coordinate.
    displayed=[]
    for j in range(b):
        rr=[]
        for i in range(b):
            val=sum((-1 if (j-i+s)%2 else 1)*cs[s]*choose(n+r-1,r)*choose(2*n+r+q-1,q)
                *choose(s-r+i-q,s-r)*choose(j,s-r+i-q)
                *choose(2*n+b+s-1-j,b+s-r-q-1-j)
                for s in range(m+1) for r in range(s+1) for q in range(i+1))
            rr.append(val%mod)
        displayed.append(rr)
    check('first-force explicit profile (6.2)',displayed,product([row[:b] for row in J[:b]],Pi,mod))

    aa=[factorial(b+t)//factorial(b)%mod for t in range(T+1)]
    rhs=[[sum(aa[t]*source_col(b+t)[i] for t in range(T+1))%mod] for i in range(b)]
    zk=product(Ai,rhs,mod)
    xi=[[sum(aa[t]*choose(n,t-r)*lam[v-r]*choose(b+v,v-r)
          for t in range(T+1) for r in range(t+1) if 0<=v-r<=m)%mod] for v in range(V+1)]
    zetaE=product(Si,product(G,xi,mod),mod)
    kz=product(K,zetaE,mod)+[[0] for _ in range(V+1-m)]
    delta=[[(kz[v][0]-xi[v][0])%mod] for v in range(V+1)]
    UV=[[choose(n,j-i)%mod for j in range(V+1)] for i in range(V+1)]
    theta=product(UV,delta,mod)
    gotk=product([row[b:] for row in J],theta,mod)
    check('complete exponential exterior cancellation (5.3)',gotk,zk+[[-1%mod]])

    # The new exterior profile has no first-type atoms. Check every retained
    # exterior label, including its finite boundary charge.
    ext=[]
    for j in range(b):
        ext.append([sum((-1 if (b+v-j+s)%2 else 1)*cs[s]*choose(n+r-1,r)*choose(j,s-r)
                    *choose(2*n+b+v+s-1-j,b+v+s-r-j)
                    for s in range(m+1) for r in range(s+1))%mod for v in range(V+1)])
    check('type2 exterior profile (6.1)',ext,[row[b:] for row in J[:b]])

    # Both terms of the physical exponential endpoint are included, using
    # zero-padded contact coordinates rather than the auxiliary value -1.
    Wb=choose(n+2,b)
    term=Wb*Wb*b*zf[-1][0]*(b*zk[-1][0]+1)%mod
    full=sum(choose(n+2,j)**2*((j*zf[j-1][0] if j else 0)-zf[j][0])
             *((j*zk[j-1][0] if j else 0)-zk[j][0]) for j in range(b))+term
    # The integral Vandermonde collapse used to eliminate the exceptional
    # type11 coefficient is separately checked at several finite offsets.
    vc=0
    for j in range(b):
        for v in range(1,4):
            tj=b-1-j
            for q0 in range(7):
                left=sum(choose(j,q0-pp)*choose(n+pp-1,pp)*choose(n+tj+v-1,tj+v-pp)
                         for pp in range(q0+1))
                right=choose(b-1+v,q0)*choose(n+tj+v-1,tj+v)
                vc+=1
                if left!=right:fails.append({'identity':'Vandermonde collapse (2.1)','j':j,'v':v,'q0':q0})
    choose.cache_clear()
    return {'b':b,'n':n,'L':L,'m':m,'T':T,'matrix_size_for_normal_order':size,
            'vandermonde_checks':vc,'full_raw_exponential_pair_modulus':full%mod,
            'physical_terminal_modulus':term,'failures':fails,
            'scope':'Auxiliary finite full-source identities only; no original-family primitive valuation.'}

if __name__=='__main__':
    start=time.monotonic()
    cases=[audit(b,L) for b,L in ((5,3),(7,3),(9,3),(5,4),(7,4),(9,4))]
    vf=lambda N:N-N.bit_count()
    eq=2*vf(379)+2*(vf(1022)-vf(331))+vf(1397)-vf(15)
    eE=vf(379)+vf(125)+vf(1022)-vf(331)+vf(767)-vf(331)+vf(1142)-vf(15)
    r32={'H0_mod256':2001*pow(9,18,256)%256,'H0_mod512':2001*pow(9,18,512)%512,
         'q_mod512':pow(9,32,512),'eQ':eq,'eE':eE}
    assert (eq,eE)==(3497,2735)
    out={'personally_authored':True,'network_and_credentials_denied':True,
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'cases':cases,'loss_arithmetic':r32,'all_passed':all(not c['failures'] for c in cases),
         'elapsed_seconds':round(time.monotonic()-start,3)}
    (ROOT/'binary_boundary_completion_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'all_passed':out['all_passed'],'seconds':out['elapsed_seconds'],
                      'failures':[(c['b'],c['L'],c['failures']) for c in cases if c['failures']],
                      'loss_arithmetic':r32}),flush=True)
