"""Exact unramified modulo8 spectral compression of L24's local inputs.

No determinant degrees are scanned. Coefficient support and the binary-lift
valuation filtration are certified in a fixed ring of rank4 over Z/8.
"""
from pathlib import Path
import json
from weighted_branch_mod8_lift import series
from weighted_endpoint_binary_inverse import rho
from weighted_regular_dyadic_subfamily import eo_residues

BASE=Path(__file__).resolve().parent
ZERO=(0,0,0,0);ONE=(1,0,0,0)


def add(a,b):return tuple((x+y)%8 for x,y in zip(a,b))
def scale(a,c):return tuple(c*x%8 for x in a)
def sub(a,b):return add(a,scale(b,-1))


def mul(a,b):
    out=[0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    # x^4=-x-1.
    for j in range(6,3,-1):
        out[j-3]-=out[j];out[j-4]-=out[j]
    return tuple(x%8 for x in out[:4])


def power(a,n):
    out=ONE
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n//=2
    return out


def inverse(a):
    assert any(x%2 for x in a)
    out=power(a,59)
    assert mul(a,out)==ONE
    return out


def root15():
    z=(0,1,0,0)
    for _ in range(2):
        z=sub(z,mul(sub(power(z,15),ONE),inverse(scale(power(z,14),15))))
    assert power(z,15)==ONE
    assert power(z,3)!=ONE and power(z,5)!=ONE
    return inverse(z)


def valuation(a):
    if a==ZERO:return 3
    return min((x&-x).bit_length()-1 for x in a if x)


def dft(values,zeta):
    zp=[power(zeta,j) for j in range(15)]
    out=[]
    for j in range(15):
        x=ZERO
        for r,value in enumerate(values):x=add(x,scale(zp[(-j*r)%15],value))
        out.append(scale(x,7)) # 1/15 mod8
    for r,value in enumerate(values):
        x=ZERO
        for j,c in enumerate(out):x=add(x,mul(c,zp[(j*r)%15]))
        assert x==(value%8,0,0,0)
    return out


def run():
    zeta=root15();four={1,2,4,8}
    e,o=eo_residues(15)
    binary=[]
    for name,values in (('e',e),('o',o)):
        out=dft(values,zeta)
        assert out[0]==ZERO
        for j in range(1,15):assert valuation(out[j])>=j.bit_count()-1
        assert {j for j in range(15) if valuation(out[j])==0}==four
        # Any lift of the four characteristic2 coefficients suffices.
        lift=[tuple(x%2 for x in out[j]) if j in four else ZERO for j in range(15)]
        zp=[power(zeta,j) for j in range(15)]
        for r,value in enumerate(values):
            z=ZERO
            for j,c in enumerate(lift):z=add(z,mul(c,zp[(j*r)%15]))
            assert power(z,4)==(value,0,0,0)
        binary.append({'branch':name,'DFT_coefficients':out,
                       'valuations_by_frequency':[valuation(c) for c in out],
                       'four_mode_lift_coefficients':lift,
                       'fourth_power_is_exact_binary_lift':True})
    saved=json.loads((BASE/'WEIGHTED_BRANCH_MOD8_LIFT_RECEIPT.json').read_text())
    O,E=[series(num,saved['common_denominator_D_power5'],483)
         for num in saved['numerators_O_E_mod8']]
    tables=[]
    for start in range(1,5):
        t=O if start%2 else E;c=start//2
        for ell in range(32):
            vals=[rho(t,ell+32*a if ell+32*a else 480,c) for a in range(15)]
            out=dft(vals,zeta)
            assert all(out[j]==ZERO for j in range(15) if j not in four)
            tables.append({'starting_b_index':start,'order_mod32':ell,
                           'coefficients_at_frequencies_1_2_4_8':[out[j] for j in sorted(four)]})
    out={'status':'AUTHOR exact rank4 unramified spectral compression',
         'coefficient_ring':'(Z/8)[x]/(x^4+x+1)',
         'primitive_root_zeta_coefficients':zeta,
         'positive_order_rho_fourier_support':[1,2,4,8],
         'rho_fourier_tables':tables,'binary_e_o_DFT':binary,
         'normalized_leading_rho_orders_64_256_mod8':[rho(O,r,0) for r in (64,256)],
         'full_endpoint_U_mod8_not_evaluated_by_this_receipt':True}
    (BASE/'WEIGHTED_ENDPOINT_SPECTRAL_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('coefficient_ring','primitive_root_zeta_coefficients',
        'positive_order_rho_fourier_support','normalized_leading_rho_orders_64_256_mod8')},indent=2))
    print(json.dumps([{'branch':s['branch'],'DFT_valuations':s['valuations_by_frequency']}
                      for s in binary],indent=2))


if __name__=='__main__':run()
