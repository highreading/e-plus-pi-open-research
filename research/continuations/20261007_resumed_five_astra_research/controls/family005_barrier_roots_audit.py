"""Parent-authored exact polynomial/root-bracket certificate reconstruction.

Only mathematical coefficient tables are transcribed. No supplied program,
build file or agent code is executed. Pure rational polynomial arithmetic.
"""
from fractions import Fraction as F
from pathlib import Path
import math,json,hashlib
R=Path(__file__).resolve().parents[1]
def trim(a):
    a=[F(x) for x in a]
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def add(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def scale(a,s):return trim([x*s for x in a])
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def div(a,b):
    rem=trim(a);b=trim(b);out=[F(0)]*max(1,len(a)-len(b)+1)
    while len(rem)>=len(b) and any(rem):
        i=len(rem)-len(b);v=rem[-1]/b[-1];out[i]+=v
        for j,w in enumerate(b):rem[i+j]-=v*w
        rem=trim(rem)
    assert not any(rem),(len(a),len(b),rem)
    return trim(out)
def val(a,x):
    y=F(0)
    for z in reversed(a):y=y*x+z
    return y
def product(a):
    q=[F(1)]
    for b in a:q=mul(q,b)
    return q
def upoly(k):
    a=[F(1)];b=[F(0),F(2)]
    if k==0:return a
    for _ in range(1,k):a,b=b,add(mul([0,2],b),scale(a,-1))
    return b
finite={
2:{'p':[45559127,-50750856,-6578767,13970217,4786184,-4292433,-576704,1311615,671564,-346453],
   'v':[-23910158,21152432,-2885110,-11558199,6485289,1456821,-1912176,-2263524,2742210,-1162454]},
1:{'p':[11913521,-79993701,-21956443,37903579,10744022,-2073193,570246,-24939103],
   'v':[-89913025,52874280,45168341,-30708629,-19269841,33922112,9819141,-16992389]}}
tails={
'p':[('0.85','0',-9338452,0),('0.94','0',-2141509,0),
     ('0','0.7',-66277922,-31907569),('0','0.85',-1231651,6002645),
     ('0.092','0.92',-3225918,8928234),('-0.092','0.92',-2105536,-9091287)],
'v':[('-0.8','0',15199211,0),('-0.96','0',4451662,0),('0.88','0',2545398,0),
     ('0.95','0',-4932634,0),('0.984','0',11618157,0),
     ('0','0.78',27238714,-38447936),('0','0.9',-31341084,-30188786),
     ('0','0.955',-6693542,11912254),('0','0.984',2055213,-21715849)]}
def tail_terms(u,kind):
    out=[]
    for aa,bb,AA,BB in tails[u]:
        a,b,A,B=F(aa),F(bb),F(AA,10**8),F(BB,10**8)
        dr=[1+a*a-b*b,-2*a] if kind=='t' else [1,-a]
        di=[2*a*b,-2*b] if kind=='t' else [0,-b]
        if b==0:out.append(([A*a],dr))
        else:
            # Pair with its conjugate: 2 Re(r*z/D), r=(A-iB)/2.
            nr,ni=A*a+B*b,A*b-B*a
            out.append((add(scale(dr,nr),scale(di,ni)),add(mul(dr,dr),mul(di,di))))
    return out
def poly_part(k,u,kind):
    a=[F(0)]
    for i,L in enumerate(finite[k][u],1):
        b=upoly(i-1) if kind=='t' else [F(0)]*(i-1)+[F(1)]
        a=add(a,scale(b,F(L,10**8)))
    return a
def numerator(k,kind):
    tp=tail_terms('p','t') if k==2 else []
    tv=tail_terms('v','t') if k==2 else []
    hv=tail_terms('v','h') if k==2 else []
    if kind=='X':
        Q=product([[0,1],[1,-1]]+[[1,0,1]]*(3-k)+[d for n,d in tp+hv])
        terms=[([F(19,48)],[0,1]),([-F(1,12)],[1,-1]),([-F(0),-F(k)-F(17,24)],[1,0,1])]
        # 2alpha+2eta+2gamma=17/24.
        if k==1:terms.append(([0,-4*F('2.47405979')],[1,0,2,0,1]))
        terms += [(scale(n,-2*k),d) for n,d in tp]+[(scale(n,-1),d) for n,d in hv]
        A=mul(Q,add(scale(poly_part(k,'p','t'),-2*k),scale(poly_part(k,'v','h'),-1)))
    else:
        Q=product([[0,1],[1,-1]]+[d for n,d in tv])
        terms=[([F(7,48)],[0,1]),([-F(1,12)],[1,-1])]+[(scale(n,2),d) for n,d in tv]
        A=mul(Q,scale(poly_part(k,'v','t'),2))
    for n,d in terms:A=add(A,mul(n,div(Q,d)))
    return trim(A),trim(Q)
def integerize(A):
    l=math.lcm(*(a.denominator for a in A));a=[int(z*l) for z in A]
    g=math.gcd(*a)
    return [z//g for z in a]
def variations(A,b,c):
    # Exact (1+t)^d A((b+c*t)/(1+t)) coefficient transform.
    d=len(A)-1;out=[F(0)]*(d+1)
    for j,Aj in enumerate(A):
        left=[F(math.comb(j,i))*b**(j-i)*c**i for i in range(j+1)]
        right=[F(math.comb(d-j,i)) for i in range(d-j+1)]
        z=mul(left,right)
        for i,q in enumerate(z):out[i]+=Aj*q
    s=[1 if x>0 else -1 for x in out if x]
    return sum(a!=b for a,b in zip(s,s[1:]))
roots={
(2,'X'):[-9601109148,-8942317572,-7608305633,-6503394794,-5185864065,-4015634158,-3108806646,-2067921826,-1589849496,1531948062,2072448179,3208186484,4381119427,5851354199,7269030693,8390277402,9332614564,9709786219],
(2,'Y'):[176402802,330649406,764952882,1227250753,2149465998,3048189112,4322699096,5564757994,6801929373,8031988371,8877037851,9577761832,9838463999,9972727815,9992037196],
(1,'X'):[-9917299785,-2259572153,2543808026,4437270259,6348298970],
(1,'Y'):[532669786,2504239325,5701738806,7966939383,9454490138]}
parts={(2,'X'):([-1,0,1],[9,9],36),(2,'Y'):([0,F(1,4),F(1,2),F(3,4),1],[5,2,2,6],24),
       (1,'X'):([-1,-F(1,2),0,F(1,2),1],[1,1,2,1],13),(1,'Y'):([0,1],[5],9)}
def run():
    cert=[]
    for k,kind in [(2,'X'),(2,'Y'),(1,'X'),(1,'Y')]:
        A,Q=numerator(k,kind);Ai=integerize(A);pp,expected,degree=parts[k,kind]
        assert len(A)-1==degree,(k,kind,len(A)-1)
        vv=[variations(A,F(b),F(c)) for b,c in zip(pp,pp[1:])]
        assert vv==expected,(k,kind,vv)
        signs=[]
        for left in roots[k,kind]:
            a=val(Ai,F(left,10**10));b=val(Ai,F(left+2,10**10));assert a*b<0,(k,kind,left)
            signs.append([1 if a>0 else -1,1 if b>0 else -1])
        counts=[sum(F(b)<F(left,10**10)<F(c) for left in roots[k,kind]) for b,c in zip(pp,pp[1:])]
        assert counts==expected,(k,kind,counts)
        cert.append({'kappa':k,'barrier':kind,'degree':degree,'integer_numerator_coefficients':list(map(str,Ai)),
                     'division_points':list(map(str,pp)),'sign_variations':vv,'root_bracket_left_scaled':roots[k,kind],
                     'bracket_endpoint_signs':signs,'coverage':'Exactly one simple root in every bracket and none in the remaining open intervals, by exact sign changes and Descartes exhaustion.'})
    source=R/'literature/openai_math_20261006/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/certificate.tex'
    obj={'certificates':cert,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
         'scope':'Exact exhaustion of43 stationary points of four specified barriers. Values and global energy bounds still require their own checks; no e+pi implication.'}
    (R/'controls/family005_barrier_roots_certificate.json').write_text(json.dumps(obj,indent=2)+'\n')
    print(json.dumps({'barriers':4,'stationary_roots':sum(len(x) for x in roots.values()),'all_degrees_variations_and_brackets_match':True,'scope':obj['scope']}))
if __name__=='__main__':run()
