"""L18: coupled scalar/root receipt and two new actual-boundary states.

This is not an atlas.  The index interpolation is kept separate from the
actual normalized Gram quotient and the final reduced denominator.
"""
from pathlib import Path
from math import factorial
import json
from h1_logarithmic_mahler_precision import jets_mod, vp
from b4_finite_criterion import state,plus_coeffs,det
from residue_atlas import coeffs

BASE=Path(__file__).resolve().parent


def phi(n,b,chi,s,d,t,mod):
    assert n>=1
    C=d[n];S=s[n];R=s[n-1];T=t[n]
    if b==4:
        return (-85*T+(156-194*C)*S+(163-97*C)*R+(12-85*chi)*C-78)%mod
    assert b==5
    return (-93*T+(24*C+90)*S+(155-31*C)*R-(148+93*chi)*C-28)%mod


def delta(n,b,s,mod):
    if b==4:return 4*(2*s[n]+s[n-1]-1)%mod
    assert b==5
    return 48*(1-s[n])%mod


def run():
    p=11;b=5;chi=-1;mod=p**4
    a,s,d,t=jets_mod(p**4+p,mod)
    scale=384
    r=p-1
    expected=scale*phi(r,b,chi,s,d,t,p)%p
    bridge=[]
    for n in (3*p-1,4*p-1):
        st=state(n,mod,b,1,coeffs(n),plus_coeffs(n))
        assert st['D']%(p*p)==st['V']%(p*p)==0
        P=st['J'][0]%(p*p);uunit=(n+1)//p
        actual_nu=(st['V']//(p*p))*pow(uunit,-2,p*p)*pow(P,-1,p*p)%(p*p)
        actual_delta=(st['D']//(p*p))*pow(uunit,-2,p*p)*pow(P,-2,p*p)%(p*p)
        raw=scale*phi(n,b,chi,s,d,t,p*p)%(p*p)
        compensated=(raw-scale*93*chi*((n-r)//p)*d[n])%(p*p)
        assert actual_nu%p==expected==compensated%p
        assert det(st['N'],mod)%p==delta(n,b,s,p)
        bridge.append(dict(n=n,depth=1,P_mod_p2=P,actual_nu_mod_p2=actual_nu,
                           actual_delta_mod_p2=actual_delta,uncompensated_nu_mod_p2=raw,
                           compensated_nu_mod_p2=compensated,contact_det_mod_p2=det(st['N'],mod)%(p*p),
                           coupled_Delta_mod_p2=delta(n,b,s,p*p),
                           normalized_model_equals_actual_mod_p=True,
                           compensated_model_equals_actual_mod_p2=actual_nu==compensated))
    assert bridge[0]['uncompensated_nu_mod_p2']%p!=bridge[1]['uncompensated_nu_mod_p2']%p
    assert all(row['actual_nu_mod_p2']%p==expected for row in bridge)
    # A fresh model root in the universal Delta5=0 residue cell r=0.
    n=p;root=[]
    slope=93*chi%p
    for precision in range(1,4):
        oldmod=p**(precision-1)
        value=phi(n,b,chi,s,d,t,p**precision)
        assert value%oldmod==0
        digit=-(value//oldmod)*pow(slope,-1,p)%p
        n+=p**precision*digit
        assert phi(n,b,chi,s,d,t,p**precision)==0
        dv=delta(n,b,s,p**(precision+1))
        root.append(dict(precision=precision,index_representative=n,lift_digit=digit,
                         Phi_mod_pk=0,Delta_mod_next_pk=dv,Delta_valuation_if_detected=vp(dv,p)))
    # The first root representative determines Delta at the unique model
    # root modulo p^2 by the proved stronger Lipschitz response.
    first=delta(root[0]['index_representative'],b,s,p*p)
    assert first%p==0 and first!=0
    common_cap=vp(first,p)
    comp=[]
    for cell in (0,p-1):
        for n0 in (p+cell,2*p+cell):
            for k in range(1,4):
                n1=n0+p**k
                tt0=(t[n0]+chi*((n0-cell)//p)*d[n0])%mod
                tt1=(t[n1]+chi*((n1-cell)//p)*d[n1])%mod
                assert (tt1-tt0)%p**k==0
                comp.append(dict(cell=cell,index=n0,depth=k,compensated_difference_mod_pk=0))
    out=dict(status='AUTHOR coupled model and actual first-digit bridge receipt; no final-q or higher-bridge theorem',
             p=p,b=b,chi=chi,actual_boundary_rows=bridge,model_root_lifts=root,
             model_common_content_cap=common_cap,compensation_rows=comp,
             actual_Gram_first_digit=expected,
             model_common_content_is_not_actual_Gram_content=True)
    (BASE/'H1_COUPLED_SCALAR_BRIDGE_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(actual_boundary_rows=bridge,model_root_lifts=root,
                          model_common_content_cap=common_cap),indent=2))


if __name__=='__main__':run()
