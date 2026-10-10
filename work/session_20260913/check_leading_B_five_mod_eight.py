"""Exact formula controls at the already studied degree n=5 only."""
import sys,math,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'math_packages'))
import sympy as s

n=5
h=2*n
high=list(range(n+1,3*n+1))
def f(k):return s.Rational(1,math.factorial(k))
def t(k):return s.Rational((-1)**((k-1)//2),k) if k%2 else s.Integer(0)
def v(x):
    if not x:return None
    a,b=map(int,s.fraction(s.cancel(x)))
    return (abs(a)&-abs(a)).bit_length()-(b&-b).bit_length()
def beta(j):return s.Rational(j*j,4*j*j-1)
def sn(j):return s.Rational(j*(j-1),2*(2*j-1))
q=[s.Integer(1),s.Integer(1)]
for j in range(1,n):q.append(s.cancel(q[-1]+beta(j)*q[-2]))
base=list(range(h+1,3*n+1))
sets={'S0':base,'Sstar':[h]+base[1:],
      'SA':[h-1]+base[1:],'SB':[h-2]+base[1:],
      'SC':[h]+base[:1]+base[2:],'SD':[h]+base[:2]+base[3:]}
out={}
arc={}
terms={}
for name,sel in sets.items():
    comp=[k for k in high if k not in sel]
    e=s.Matrix([[f(k-j) for j in range(n)] for k in sel]).det()
    c=s.Matrix([[t(k-j) for j in range(n+1)] for k in comp]+[[1]*(n+1)]).det()
    sign=(-1)**(sum(high.index(k) for k in sel)+n*(n-1)//2)
    terms[name]=sign*e*c
    arc[name]=c
    out[name]={'selected_rows':sel,'exponential_v2':v(e),'C_v2':v(c),'term_v2':v(terms[name])}
assert s.cancel(arc['SA']/arc['S0']-(sn(n)+beta(n)*beta(n-1)*q[n-2]/q[n]))==0
assert s.cancel(arc['SB']/arc['S0']-beta(n)*(sn(n-1)*q[n-1]+beta(n-1)*beta(n-2)*q[n-3])/q[n])==0
phi=lambda k:k-k.bit_count()
sf=lambda j:sum(phi(k) for k in range(j))
baseline=sf(n)-sum(phi(k) for k in base)+2*sf(n)+2*((n+2)//4)
rows=[[f(k-j) for j in range(n)]+[t(k-j) for j in range(n+1)] for k in high]
dc=s.Matrix(rows+[[0]*n+[1]*(n+1)]).det()
pair=terms['S0']+terms['Sstar']
visible=pair+terms['SA']+terms['SB']
remainder=dc-visible
assert v(pair)==v(terms['SA'])==v(terms['SB'])==v(visible)==v(dc)==baseline+2
assert remainder==0 or v(remainder)>=baseline+3
result={'degree':n,'scope':'single previously studied degree, not a degree scan','baseline':baseline,
        'six_terms':out,'C_A_ratio':str(s.cancel(arc['SA']/arc['S0'])),
        'C_B_ratio':str(s.cancel(arc['SB']/arc['S0'])),
        'paired_v2':v(pair),'three_contribution_sum_v2':v(visible),
        'all_other_C_terms_v2':v(remainder),'whole_C_v2':v(dc)}
Path(__file__).with_name('leading_B_five_mod_eight_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
