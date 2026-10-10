"""Exact finite input and rational log comparison for the b5,m1 author theorem."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial,isqrt
import json,hashlib
from finite_boundary_chart import chart

BASE=Path(__file__).resolve().parent
SELECTED=[11,13,29,53,59,89,101,173,193,199]


def log_interval(x,terms=24):
    x=Q(x); k=0
    while x>=2:
        x/=2; k+=1
    while x<1:
        x*=2; k-=1
    def unit(y):
        z=(y-1)/(y+1)
        lo=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(terms)),Q(0))
        hi=lo+2*z**(2*terms+1)/(Q(2*terms+1)*(1-z*z))
        return lo,hi
    l2,u2=unit(Q(2)); lx,ux=unit(x)
    return (k*l2+lx,k*u2+ux) if k>=0 else (k*u2+lx,k*l2+ux)


def run():
    source=BASE/'B5_NORMALIZED_PRIME_ATLAS_199.json'
    data=json.loads(source.read_text())
    assert data['b']==5 and data['m']==1 and data['good_primes']==SELECTED
    rows={r['p']:r for r in data['rows']}
    out=[]; rho_lo=Q(0); rho_hi=Q(0)
    for p in SELECTED:
        assert p>5 and all(p%d for d in range(2,isqrt(p)+1))
        r=rows[p]
        assert len(r['P_residues'])==len(r['V_residues'])==len(r['D_residues'])==p
        assert all(0<x<p for x in r['P_residues'])
        assert [j for j,v in enumerate(r['V_residues']) if v==0]==[0,p-2,p-1]
        assert not r['endpoint_zeros'] and r['V_zeros']==[0,p-2,p-1]
        C=sum((-1)**j*factorial(j) for j in range(p))%p
        assert C==r['C'] and r['origin_D']==497664%p!=0
        assert r['origin_coefficient']==331776*(3*C+32)%p!=0
        for h,stored in zip((1,2),r['normalized_charts']):
            # Recompute only the twenty finite inputs used by this theorem.
            assert stored==chart(p,5,1,h)
            assert stored['nu']!=0
            assert stored['P']==r['P_residues'][p-h]
        lo,hi=log_interval(p)
        rho_lo+=2*lo/(p-1); rho_hi+=2*hi/(p-1)
        out.append(r)
    sqrt_lo=Q(1414213562373095,10**15)
    sqrt_hi=sqrt_lo+Q(1,10**15)
    assert sqrt_lo**2<2<sqrt_hi**2
    tau_lo,_=log_interval(1+sqrt_lo)
    _,tau_hi=log_interval(1+sqrt_hi)
    tau_lo*=2; tau_hi*=2
    assert rho_lo-tau_hi>Q(1,25)
    inputs=[source,BASE/'b5_normalized_prime_atlas.py',BASE/'finite_boundary_chart.py',
            BASE/'b4_finite_criterion.py',BASE/'residue_atlas.py',BASE/'exact_local_probe.py']
    cert=dict(status='AUTHOR exact finite certificate; all-depth theorem and signed-error inputs are separately stated',
              family=dict(b=5,m=1),selected=SELECTED,total_seed_count=sum(SELECTED),
              total_normalized_charts=2*len(SELECTED),normal_index_minimum=2*max(SELECTED),
              rho_lower=str(rho_lo),rho_upper=str(rho_hi),tau_lower=str(tau_lo),tau_upper=str(tau_hi),
              gap_lower=str(rho_lo-tau_hi),strict_gap_lower='1/25',
              decimal_display=dict(rho_lower=float(rho_lo),rho_upper=float(rho_hi),
                                   tau_lower=float(tau_lo),tau_upper=float(tau_hi),
                                   gap_lower=float(rho_lo-tau_hi)),
              log_method='24-term rational atanh expansion after dyadic normalization; exact positive remainder bound',
              sqrt2_interval=[str(sqrt_lo),str(sqrt_hi)],
              sources=[dict(path=str(f),sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in inputs],
              residues=out)
    (BASE/'B5_NORMALIZED_PRIME_CERTIFICATE.json').write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps({k:cert[k] for k in ['selected','total_seed_count','total_normalized_charts','decimal_display','strict_gap_lower']},indent=2))
    return cert


if __name__=='__main__':
    run()
