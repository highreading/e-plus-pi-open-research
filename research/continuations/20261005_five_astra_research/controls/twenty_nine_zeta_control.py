"""Coordinator finite sub-contraction of the complete leading Q boundary."""
import json,math
from pathlib import Path
import numpy as np
import twenty_nine_mixed_low_control as source

p=29;OUT=Path(__file__).resolve().parent
x,c,xi,e=source.x,source.c,source.xi,source.e
sel=(x%p==0)
assert int(sel.sum())==3036
zetas=[int(np.sum(c[sel & (e==j)]*xi[sel & (e==j)]))%p for j in (0,1)]
zeta=sum(zetas)%p
def harmonic(k):return sum(pow(i,-1,p) for i in range(1,k+1))%p
def functional(d):
    ts=[t for t in range(4) if 0<=d-t<=22]
    weights=[math.comb(3,t)**2*math.comb(d-t+6,6)**2%p for t in ts]
    rt=[(harmonic(3-t)-harmonic(t)+harmonic(d-t)-harmonic(d-t+6))%p for t in ts]
    k=[(11*(d+7-t)**2+18*(3-t)**2)%p for t in ts]
    kp=[(-22*(d+7-t)-36*(3-t))%p for t in ts]
    f=sum(w*a for w,a in zip(weights,k))%p
    beta=sum(w*(a+2*r*b) for w,a,r,b in zip(weights,kp,rt,k))%p
    assert f!=0
    l=sum(w*(-2*(3-t)+2*r*(3-t)**2-beta*pow(f,-1,p)*(3-t)**2)
          for w,t,r in zip(weights,ts,rt))%p
    return l
ells=[functional(d) for d in range(25)]
gam=[8*zeta*l%p for l in ells]
assert ells[0]==19 and gam[0]==7*zeta%p
triples=all(int(c[np.flatnonzero(x==xx+a)[0]])==math.comb(2,a)*int(c[i])%p
            for i,xx in enumerate(x) if xx%p==0 for a in range(3))
assert triples
report={'p':p,'representative_b':source.b,'representative_n':source.n,
    'old_support_size':len(x),'digit_zero_selected_coordinates':int(sel.sum()),
    'zeta0':zetas[0],'zeta1':zetas[1],'zeta':zeta,
    'complete_boundary_divisions_verified':True,'triple_c_identity_pass':triples,
    'kappa':source.report['kappa'],'g':source.report['mixed_low_constants_g0_g1'],
    'L_d_ell1_squared_mod29':ells,'Gamma1_d0_to24_mod29':gam,
    'Gamma1_0_check_pass':True,
    'scope':'Exact bounded contraction constants and finite functional table. '
      'Infinite Gamma1 consequence depends on A2turn23 reduction; Gamma0 remains uncomputed. '
      'No original-domain reachability, all-depth alignment or denominator theorem.'}
(OUT/'twenty_nine_zeta_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
