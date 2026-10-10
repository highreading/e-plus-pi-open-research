"""New finite b5,m1 prime criterion; all-depth proof is a separate author input."""
from pathlib import Path
from math import factorial, log
import json
from b4_finite_criterion import state, plus_coeffs
from residue_atlas import coeffs, primes
from finite_boundary_chart import chart

HERE = Path(__file__).resolve().parent


def run(bound=199):
    b,m = 5,1
    cache = [(coeffs(n),plus_coeffs(n)) for n in range(bound)]
    rows=[];goods=[];rate=0
    for p in primes(bound):
        if p<=b:
            continue
        states=[state(n,p,b,m,*cache[n]) for n in range(p)]
        pz=[s['n'] for s in states if s['J'][0]==0]
        vz=[s['n'] for s in states if s['V']==0]
        C=sum((-1)**j*factorial(j) for j in range(p))%p
        origin=331776*(3*C+32)%p
        pre=not pz and vz==[0,p-2,p-1] and 497664%p and origin
        refs=[chart(p,b,m,h) for h in (1,2)] if pre else []
        good=bool(pre and all(r['nu'] for r in refs))
        rows.append(dict(p=p,endpoint_zeros=pz,V_zeros=vz,C=C,
                         origin_D=497664%p,origin_coefficient=origin,
                         normalized_charts=refs,good=good,
                         P_residues=[s['J'][0] for s in states],
                         V_residues=[s['V'] for s in states],
                         D_residues=[s['D'] for s in states]))
        if good:
            goods.append(p);rate+=2*log(p)/(p-1)
            print(p,'good',rate,flush=True)
    result=dict(status='BOUNDED_AUTHOR_B5_CRITERION_EVIDENCE',b=b,m=m,
                prime_bound=bound,good_primes=goods,rate_display=rate,rows=rows)
    out=HERE/f'B5_NORMALIZED_PRIME_ATLAS_{bound}.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('Saved',out,flush=True)
    return result


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--bound',type=int,default=199)
    args=parser.parse_args()
    run(args.bound)
