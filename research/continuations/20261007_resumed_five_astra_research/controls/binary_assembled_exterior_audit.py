"""Parent-authored bounded audit of the NEW assembled boundary cancellation.

This is an auxiliary b=2 test over (Z/8)[F0,F1]. It tests whole polynomial
completion, including exterior positions, rather than individual kernel tails.
It cannot establish an infinite-family valuation or a primitive denominator.
"""
from pathlib import Path
from math import factorial
import hashlib, json, time
from finite_binary_profile_audit import choose, product, inverse, difference

ROOT = Path(__file__).resolve().parent

def run():
    start = time.monotonic()
    b, n, L = 2, 8004, 3
    mod, m, T = 2**L, 4*(L-1), 2*L-1
    V, d = T+m, min(b,m)
    # Degree b+V+m is one beyond the largest possible nonzero coefficient.
    size = b+V+m+2
    failures = []
    def check(label, got, wanted, modulus=mod):
        diffs = difference(got, wanted, modulus)
        if diffs:
            failures.append({'identity':label, 'differences':diffs[:10]})

    lam = [1,-n]
    for s in range(1,m+1):
        lam.append((s-n)*lam[-1]+(s*n-s*(s-1)//2)*lam[-2])
    cs = [1]
    for s in range(1,m+1):
        cs.append(-sum(choose(s,r)*lam[r]*cs[s-r] for r in range(1,s+1)))
    def source_col(column):
        return [sum(choose(n,column-r)*sum(
            lam[s]*choose(r+s,s)*choose(n+i,r+s) for s in range(m+1))
            for r in range(column+1)) % mod for i in range(b)]

    A = [list(row) for row in zip(*(source_col(j) for j in range(b)))]
    Ai = inverse(A,mod)
    U = [[choose(n,j-i)%mod for j in range(b)] for i in range(b)]
    Ui = inverse(U,mod)
    P = [[choose(i,j)%mod for j in range(b)] for i in range(b)]
    Pi = inverse(P,mod)
    Hi = [[cs[i-j]*choose(i,j)%mod if i>=j else 0 for j in range(b)] for i in range(b)]
    K = [[lam[d+r-t]*choose(b+r,d+r-t)%mod if 0<=d+r-t<=m else 0
          for t in range(d)] for r in range(m)]
    F = [[-sum(choose(-n,b+q-j)*choose(n,v-q) for q in range(v+1)) % mod
          for v in range(V+1)] for j in range(b)]
    G = product(Hi,F,mod)[b-d:]
    S = product([row[:m] for row in G],K,mod)
    for i in range(d):
        S[i][i] = (S[i][i]+1)%mod
    Si = inverse(S,mod)
    def jentry(j,col):
        return sum(cs[s]*choose(-n,r)*choose(j,s-r)*choose(-2*n-r,col-j+s-r)
            for s in range(m+1) for r in range(s+1)) % mod
    J = [[jentry(j,col) for col in range(b+V+1)] for j in range(size)]

    # Two columns stand for independent force indeterminates F0 and F1.
    Df = product(product(Hi,Ui,mod),Pi,mod)[b-d:]
    zeta = product(Si,Df,mod)
    beta = product(K,zeta,mod)
    Um = [[choose(n,j-i)%mod for j in range(m)] for i in range(m)]
    eta = product(Um,beta,mod)
    qf = Pi+eta+[[0,0] for _ in range(V+1-m)]
    hat_zf = product(J,qf,mod)
    check('complete first-force vector through all 25 positions',
          hat_zf,Ai+[[0,0] for _ in range(size-b)])

    aa_exact = [factorial(b+t)//factorial(b) for t in range(T+2)]
    aa = [x%mod for x in aa_exact]
    rhs = [[sum(aa[t]*source_col(b+t)[i] for t in range(T+1))%mod]
           for i in range(b)]
    zk = product(Ai,rhs,mod)
    xi = [[sum(aa[t]*choose(n,t-r)*lam[v-r]*choose(b+v,v-r)
               for t in range(T+1) for r in range(t+1) if 0<=v-r<=m)%mod]
          for v in range(V+1)]
    zetaE = product(Si,product(G,xi,mod),mod)
    kz = product(K,zetaE,mod)+[[0] for _ in range(V+1-m)]
    delta = [[(kz[v][0]-xi[v][0])%mod] for v in range(V+1)]
    UV = [[choose(n,j-i)%mod for j in range(V+1)] for i in range(V+1)]
    theta = product(UV,delta,mod)
    hat_zk = product([row[b:] for row in J],theta,mod)
    wanted_zk = zk+[[-aa[j-b]%mod if b<=j<=b+T else 0] for j in range(b,size)]
    check('complete exponential vector including the full exterior prefix',hat_zk,wanted_zk)

    hatF = [[((j*hat_zf[j-1][i] if j else 0)-hat_zf[j][i])%mod
             for i in range(2)] for j in range(size)]
    hatG = [[((j*hat_zk[j-1][0] if j else 0)-hat_zk[j][0])%mod]
            for j in range(size)]
    wantF = [[b*x%mod for x in Ai[-1]]]+[[0,0] for _ in range(size-b-1)]
    wantG = [[(b*zk[-1][0]+1)%mod] if j==b else
             [-aa[T+1]%mod] if j==b+T+1 else [0] for j in range(b,size)]
    check('first-force complete exterior difference',hatF[b:],wantF)
    check('exponential exterior difference with retained high endpoint',hatG[b:],wantG)
    source_telescoping = all((b+t)*aa_exact[t-1]==aa_exact[t] for t in range(1,T+1))
    if not source_telescoping:
        failures.append({'identity':'exact factorial prefix telescoping'})

    # Quadratic coefficient order F0^2,F0*F1,F1^2; the mixed channel is linear.
    extQ = [0,0,0]
    extE = [0,0]
    for j in range(b,size):
        w2 = choose(n+2,j)**2 % mod
        x,y = hatF[j]
        extQ = [(extQ[0]+w2*x*x)%mod,(extQ[1]+2*w2*x*y)%mod,
                (extQ[2]+w2*y*y)%mod]
        extE = [(extE[i]+w2*hatF[j][i]*hatG[j][0])%mod for i in range(2)]
    w2 = choose(n+2,b)**2 % mod
    x,y = Ai[-1]
    terminalQ = [w2*b*b*x*x%mod,2*w2*b*b*x*y%mod,w2*b*b*y*y%mod]
    terminalE = [w2*b*Ai[-1][i]*(b*zk[-1][0]+1)%mod for i in range(2)]
    check('assembled exterior equals physical norm terminal',[extQ],[terminalQ])
    check('assembled exterior equals physical mixed terminal',[extE],[terminalE])
    check('nonzero symbolic norm boundary residue',[extQ],[[4,0,4]])
    check('nonzero symbolic mixed boundary residue modulo four',[extE],[[2,2]],4)
    result = {'personally_authored':True,'network_and_key_reads_denied':True,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'b':b,'n':n,'L':L,'modulus':mod,'m':m,'T':T,'V':V,
        'checked_vector_positions':size,'contact_matrix_mod8':A,'physical_zf_coefficients':Ai,
        'physical_zk_mod8':zk,'exterior_Q_coefficients_mod8':extQ,
        'exterior_E_coefficients_mod8':extE,
        'exact_retained_high_source_endpoint':-aa_exact[T+1],
        'exact_factorial_prefix_telescoping':source_telescoping,
        'all_passed':not failures,'failures':failures,
        'scope':'Auxiliary b=2 whole polynomial completion and assembled exterior identities only; no infinite original-family, kernel-level, or primitive-content conclusion.',
        'elapsed_seconds':round(time.monotonic()-start,3)}
    (ROOT/'binary_assembled_exterior_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)

if __name__=='__main__':
    run()
