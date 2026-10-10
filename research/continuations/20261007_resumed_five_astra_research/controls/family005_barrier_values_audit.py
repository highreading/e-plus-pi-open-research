"""Parent-authored rational interval verification of all50 candidate values.

Reuses only the parent's exact coefficient transcription, never a downloaded
program. Log/argument series have explicit rational remainder bounds. No
floating-point value is used to accept a inequality.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import sys,json,hashlib
sys.path.insert(0,str(Path(__file__).resolve().parent))
import family005_barrier_roots_audit as C
R=C.R
def ia(a,b):return (a[0]+b[0],a[1]+b[1])
def isc(a,s):return (s*a[0],s*a[1]) if s>=0 else (s*a[1],s*a[0])
def iex(x):return (F(x),F(x))
def cm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def ca(a,b):return (a[0]+b[0],a[1]+b[1])
def cs(a,b):return (a[0]-b[0],a[1]-b[1])
def cp(a,k):
    z=(F(1),F(0))
    for _ in range(k):z=cm(z,a)
    return z
def hlog(y):
    q=(y-1)/(y+1);v=q;total=F(0)
    for j in range(18):total+=2*v/F(2*j+1);v*=q*q
    rem=2*q**37/(37*(1-q*q))
    return (total,total+rem)
L2=hlog(F(2))
@lru_cache(None)
def ln(s):
    assert s>0;s=F(s);y=s;m=0
    while y<1:y*=2;m-=1
    while y>2:y/=2;m+=1
    return ia(isc(L2,F(m)),hlog(y))
def at(t):
    assert abs(t)<=F(1,2);v=t;total=F(0)
    for j in range(24):total+=(-1)**j*v/F(2*j+1);v*=t*t
    rem=abs(t)**49/49
    return (total-rem,total+rem)
PI4=ia(at(F(1,2)),at(F(1,3)))
@lru_cache(None)
def clog(z):
    a,b=z;assert a or b
    real=isc(ln(a*a+b*b),F(1,2))
    if b==0 and a<0:return (real,isc(PI4,F(4)))
    rotations={0:(a,b),1:(a+b,b-a),2:(b,-a),3:(b-a,-a-b),4:(-a,-b),
               -1:(a-b,b+a),-2:(-b,a),-3:(-a-b,a-b),-4:(-a,-b)}
    possible=[]
    for k,(u,v) in rotations.items():
        if u<=0:continue
        t=v/u
        if abs(t)>F(1,2) or (k==4 and t>0) or (k==-4 and t<0):continue
        possible.append((abs(t),k,t))
    assert possible
    _,k,t=min(possible)
    arg=ia(isc(PI4,F(k)),at(t))
    return real,arg
def real_weight_log(weight,z):
    rl,im=clog(z)
    return ia(isc(rl,weight[0]),isc(im,-weight[1]))
def tails(k,u):
    if k==1:return []
    out=[]
    for aa,bb,AA,BB in C.tails[u]:
        a,b=F(aa),F(bb)
        if b==0:out.append(((a,b),(F(AA,10**8),F(0))))
        else:
            out += [((a,b),(F(AA,2*10**8),F(-BB,2*10**8))),
                    ((a,-b),(F(AA,2*10**8),F(BB,2*10**8)))]
    return out
def ch(k,x):
    if k==0:return F(1)
    a,b=F(1),x
    for _ in range(1,k):a,b=b,2*x*b-a
    return b
def norm(k,u):
    tt=tails(k,u);finite=C.finite[k][u];total=iex(0)
    for j,L in enumerate(finite,1):
        l=F(L,10**8);s=(F(0),F(0))
        for z,r in tt:s=ca(s,cm(r,cp(z,j)))
        assert s[1]==0
        total=ia(total,iex((l*l+2*l*s[0])/j))
    for z,r in tt:
        for w,q in tt:total=ia(total,isc(real_weight_log(cm(r,q),cs((F(1),F(0)),cm(z,w))),F(-1)))
    return total
def T(k,u,x):
    total=iex(sum(F(L,10**8)*ch(j,x)/j for j,L in enumerate(C.finite[k][u],1)))
    for z,r in tails(k,u):
        arg=ca(cs((F(1),F(0)),(2*x*z[0],2*x*z[1])),cm(z,z))
        total=ia(total,isc(real_weight_log(r,arg),F(-1,2)))
    return total
def S(k,u,x):
    total=iex(sum(F(L,10**8)*x**j/j for j,L in enumerate(C.finite[k][u],1)))
    for z,r in tails(k,u):total=ia(total,isc(real_weight_log(r,cs((F(1),F(0)),(x*z[0],x*z[1]))),F(-1)))
    return total
def barrier(k,kind,x):
    x=F(x)
    if kind=='X':
        out=ia(isc(ln(abs(x)),F(19,48)),isc(ln(1-x),F(1,12)))
        out=ia(out,isc(ln(1+x*x),-F(k,2)-F(17,48)))
        if k==1:out=ia(out,iex(F('2.47405979')*(F(1,6)-2*x*x/(1+x*x))))
        out=ia(out,isc(T(k,'p',x),F(-2*k)));out=ia(out,isc(S(k,'v',x),F(-1)))
    else:
        out=ia(isc(ln(x),F(7,48)),isc(ln(1-x),F(1,12)))
        out=ia(out,isc(T(k,'v',x),F(2)))
    return out
def enclosure(a):
    d=10**20;lo=a[0]*d;hi=a[1]*d
    return [lo.numerator//lo.denominator,-((-hi.numerator)//hi.denominator)]
def run():
    assert L2[0]>F('0.693146') and L2[1]<F('0.693149')
    normbounds={};values=[]
    for k in (2,1):
        ni=ia(isc(norm(k,'p'),F(k)),isc(norm(k,'v'),F(1,2)))
        assert ni[1]<F('0.77843' if k==2 else '0.93205')
        normbounds[k]=enclosure(ni)
        for kind in ('X','Y'):
            pts=list(C.roots[k,kind])
            pts += { (2,'X'):[-10**10],(2,'Y'):[2500000000,5000000000,7500000000],
                     (1,'X'):[-10**10,-5000000000,5000000000],(1,'Y'):[] }[k,kind]
            cutoff=F({(2,'X'):'-0.98400',(2,'Y'):'-1.60891',(1,'X'):'-1.32442',(1,'Y'):'-1.42805'}[k,kind])
            for s in pts:
                x=F(s,10**10);vi=barrier(k,kind,x);assert vi[1]<cutoff,(k,kind,s)
                values.append({'kappa':k,'barrier':kind,'x_scaled_1e10':s,'enclosure_scaled_1e20':enclosure(vi),'strict_upper_cutoff':str(cutoff)})
    assert len(values)==50
    # Verify the premises of the manuscript's generous120000 derivative bound.
    for kk,rr in C.roots.items():
        for s in rr:
            for x in [F(s,10**10),F(s+2,10**10)]:assert abs(x)>F('0.0007') and abs(1-x)>F('0.0007')
    for u,limit in [('p',F('0.94')),('v',F('0.984'))]:
        for aa,bb,AA,BB in C.tails[u]:
            assert F(aa)**2+F(bb)**2<=limit**2
            assert (F(AA,10**8)**2+F(BB,10**8)**2)/(4 if F(bb) else 1)<1
    xder=F(230)+F(19,48)/F('0.0007')+F(1,12)/F('0.0007')+3+4*F('2.47405979')+40/F('0.06')**2+13/F('0.016')
    yder=F(110)+(F(7,48)+F(1,12))/F('0.0007')+26/F('0.016')**2
    assert xder<120000 and yder<120000
    ups={2:-F(11,16)*F('0.693146')+F('0.77844')-F('0.98399')-F('1.60890')+F('0.000048'),
         1:-F(11,16)*F('0.693146')+F('0.9321')-F('1.3244')-F('1.4280')+F('0.000048')}
    assert ups[2]==F('-2.290939875') and ups[1]==F('-2.296789875')
    assert all(z<F('-2.2909') for z in ups.values())
    source=R/'literature/openai_math_20261006/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/certificate.tex'
    obj={'normalization':'enclosure endpoints are exact integers divided by10^20',
         'log2_enclosure_scaled_1e20':enclosure(L2),'norm_enclosures_scaled_1e20':normbounds,
         'candidate_values':values,'derivative_bound':'120000 on all43 complete root brackets, from exact coefficient/modulus bounds',
         'root_bracket_value_loss':str(F('0.000024')),'real_upper_constants':{str(k):str(v) for k,v in ups.items()},
         'rational_log_inputs_cached':ln.cache_info().currsize,'complex_log_inputs_cached':clog.cache_info().currsize,
         'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
         'scope':'All50 candidate values and trial norms satisfy the rigorous coarse cutoffs. Together with the exact root exhaustion this verifies the finite real-place certificate. The preceding energy/interpolation theorems and any e+pi transfer remain separate proof obligations.'}
    (R/'controls/family005_barrier_values_certificate.json').write_text(json.dumps(obj,indent=2)+'\n')
    print(json.dumps({'candidate_values':50,'all_rational_bounds_pass':True,'upper_constants':obj['real_upper_constants'],'scope':obj['scope']}))
if __name__=='__main__':run()
