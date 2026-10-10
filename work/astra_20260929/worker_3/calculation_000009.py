import json
from math import factorial
from pathlib import Path

MOD = 1024
pairs = [(b,c) for b in range(55) for c in range(28) if b+2*c < 55]
def v2(x):
    return (abs(x) & -abs(x)).bit_length()-1 if x else 100000
max_shift = max(v2((1 << c)*factorial(b)*factorial(c)) for b,c in pairs)
GUARD = 1 << (10+max_shift)

def trim(p):
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def product(p,q,mod):
    out=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        if x:
            for j,y in enumerate(q):
                if y: out[i+j]+=x*y
    return trim([x%mod for x in out])

def plus(p,q):
    out=p.copy()+[0]*max(0,len(q)-len(p))
    for j,x in enumerate(q): out[j]=(out[j]+x)%MOD
    return trim(out)

def falling_table(a,slope,degree,mod):
    table=[[1]]
    for j in range(degree):
        table.append(product(table[-1],[a-j,slope],mod))
    return table

checks=0
minimum_margin=100000

def normalize(poly,den,sign):
    global checks, minimum_margin
    shift=v2(den)
    # Residues modulo GUARD retain every bit required for divisibility
    # and the quotient modulo 1024; odd denominators are then units.
    assert all(x%(1<<shift)==0 for x in poly)
    checks+=1
    minimum_margin=min(minimum_margin,min(v2(x) for x in poly)-shift)
    inv=pow(den>>shift,-1,MOD)
    return trim([((x>>shift)*inv*sign)%MOD for x in poly])

rows=[]
for a in (1,3,5,7):
    ft=falling_table(a,8,54,GUARD)
    ft1=falling_table(a+1,8,54,GUARD)
    dcache={}
    def dpoly(z):
        if z not in dcache:
            out=[0]
            for term in falling_table(z,16,19,MOD): out=plus(out,term)
            dcache[z]=out
        return dcache[z]
    H=K=A=B=[0]
    for b,c in pairs:
        R=b+2*c
        s=b+c
        den=(1<<c)*factorial(b)*factorial(c)
        sign=1 if b%2==0 else -1
        h=normalize(product(ft[R],ft[s],GUARD),den,sign)
        if R==0:
            k=[2]
        else:
            raw=product(ft[R-1],ft1[s],GUARD)
            raw=product(raw,[2*a+2-R,16],GUARD)
            k=normalize(raw,den,sign)
        H=plus(H,h)
        K=plus(K,k)
        A=plus(A,product(h,dpoly(2*a-R),MOD))
        B=plus(B,product(k,dpoly(2*a+1-R),MOD))
    C=plus(product(K,A,MOD),[-x for x in product(H,B,MOD)])
    rows.append(dict(residue_mod8=a,H=H,K=K,A=A,B=B,C=C,v2_gauss_C=min(map(v2,C))))

source=Path('work/session_20260927/hp_b1_odd_dyadic_germs_checks.json')
archived=json.loads(source.read_text())
differences=[]
for fresh,old in zip(rows,archived['rows']):
    for key in fresh:
        if fresh[key]!=old.get(key):
            differences.append({'residue':fresh['residue_mod8'],'field':key,'fresh':fresh[key],'archived':old.get(key)})
assert len(archived['rows'])==4
print(json.dumps({'outer_R_less_than':55,'inner_j_less_than':20,'modulus':MOD,'pairs_per_disk':len(pairs),'guard_bits':10+max_shift,'kernel_divisibility_checks':checks,'minimum_divisibility_margin':minimum_margin,'rows':rows,'differences':differences,'all_coefficients_match':not differences,'scope':'Finite coefficient reconstruction only; infinite tails depend on separately audited analytic bounds. No denominator-transfer or irrationality conclusion.'},indent=2))
assert not differences
