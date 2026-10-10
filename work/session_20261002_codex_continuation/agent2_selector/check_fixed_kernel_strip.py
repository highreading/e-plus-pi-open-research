import sys,json
sys.path.insert(0,'[private local path removed]')
import sympy as s
from pathlib import Path
w=s.symbols('w');out={}
def routh(P):
    aa=P.all_coeffs();L=(len(aa)+1)//2
    rows=[aa[::2]+[s.S(0)]*(L-len(aa[::2])),aa[1::2]+[s.S(0)]*(L-len(aa[1::2]))]
    for j in range(2,len(aa)):
        if rows[-1][0]==0:raise ValueError('zero pivot')
        b=[s.cancel((rows[-1][0]*rows[-2][k+1]-rows[-2][0]*rows[-1][k+1])/rows[-1][0]) for k in range(L-1)]+[s.S(0)]
        if all(z==0 for z in b):raise ValueError('all-zero row')
        rows.append(b)
    signs=[s.sign(a[0]) for a in rows]
    return {'first_column':[str(a[0]) for a in rows],'signs':[int(z) for z in signs],'right_half_plane_count':sum(signs[j]!=signs[j-1] for j in range(1,len(signs)))}
for N in [4,8]:
    data=json.loads(Path(__file__).with_name(f'fixed_weight_kernel_n{N}.json').read_text());P=s.sympify(data['P'])
    R=s.cancel(P/(w*(w*w-1)**(N+1)*(w*w-w+s.Rational(1,2))**(N//2)))
    counts={str(a):routh(s.Poly(R.subs(w,w+a),w)) for a in [s.S(0),s.Rational(1,2)]}
    out[str(N)]={'R':str(R),'counts':counts,'open_strip_root_count':counts['0']['right_half_plane_count']-counts['1/2']['right_half_plane_count']}
    print(N,{z:v['right_half_plane_count'] for z,v in counts.items()},'open strip count',out[str(N)]['open_strip_root_count'],flush=True)
Path(__file__).with_name('fixed_kernel_exact_strip_counts.json').write_text(json.dumps(out,indent=2))
