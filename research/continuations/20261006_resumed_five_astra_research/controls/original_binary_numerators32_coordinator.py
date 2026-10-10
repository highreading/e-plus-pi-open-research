#!/usr/bin/env python3
"""New originalu0 finite Laurent-numerator construction and independent jets.

All arithmetic is integral modulo2^32. Uses only bounded degree and archived
finite Schur data. No remote code, original-length arrays, or Gram evaluation.
"""
from math import comb
from pathlib import Path
import hashlib
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(300,300))
ROOT = Path(__file__).resolve().parent
OLD = ROOT.parents[1]/'astra_pro5_resume_20261005'/'controls'
Q = 1<<32
b = 9**18
n = 4002*b
B = b-1
I,m,T,R,L0,K0 = 72,124,35,160,284,196
JET = 247
MAX = JET+m

def sign(x):
    return -1 if x%2 else 1

def small_lower_table(N,length):
    vals = [1]
    exact = 1
    for k in range(1,length+1):
        exact = exact*(N-k+1)//k
        vals.append(exact%Q)
    return vals

def inverse_power_table(N,length):
    vals = [1]
    exact = 1
    for k in range(1,length+1):
        exact = exact*(N+k-1)//k
        vals.append(exact%Q)
    return vals

def convolution(a,c,length):
    return [sum(a[j]*c[k-j] for j in range(max(0,k-len(c)+1),min(k,len(a)-1)+1))%Q
            for k in range(length)]

def mv(A,x):
    return [sum(a*z for a,z in zip(row,x))%Q for row in A]

def load_polynomials(load):
    count = len(load)
    a,c = [0]*count,[0]*count
    for r,z in enumerate(load):
        if not z:
            continue
        base = count-r-1
        scale = sign(r)*z
        c[base] = (c[base]-scale)%Q
        for e in range(r+1):
            a[base+e] = (a[base+e]+scale*sign(e)*POS[e])%Q
    return a,c

def load_jets(load):
    result = [0]*(MAX+1)
    for r,z in enumerate(load):
        if z:
            for k in range(MAX+1):
                value = sum(sign(e)*POS[e]*TP[k+r+1-e] for e in range(r+1))%Q
                result[k] = (result[k]+sign(r)*z*value)%Q
    return result

def psi_jets(Y,length):
    return [sum(sign(s)*CC[s]*CHOOSE[k][s]*Y[k+s]
                for s in range(m+1))%Q for k in range(length)]

def schur_load(Y):
    terminal = psi_jets(Y,m)
    selected = [sign(b-m+t)*terminal[m-1-t]%Q for t in range(m)]
    return mv(KBAR,mv(SINV,selected))

def polynomial_source_f(head):
    out = [0]*I
    for ell,z in enumerate(head):
        if z:
            for dd in range(ell+1):
                scale = sign(ell+dd)*z*comb(B-dd,ell-dd)%Q
                for e in range(I-dd):
                    out[dd+e] = (out[dd+e]+scale*sign(e)*comb(I-1-dd,e))%Q
    return out

def numerator_psi(sources,Y):
    """Return common Laurent numerators of t*Psi(Y), including all prefixes.

    A source is (coefficient, Laurent exponent, base_n, fixed_offset), for
    coeff*z^r/(1-z)^(base_n*n+fixed_offset). base_n is0 or1.
    """
    p2,p1 = [0]*(L0+K0),[0]*L0
    contributions = 0
    for coefficient,r,base,extra in sources:
        if not coefficient:
            continue
        derivatives = DERIV[extra] if base else [1]+[0]*m
        for s in range(m+1):
            scale = coefficient*sign(s)*CC[s]%Q
            if not scale:
                continue
            for e in range(s+1 if base else 1):
                weight = scale*sign(e)*RISING_CHOOSE[r][s-e]*derivatives[e]%Q
                if not weight:
                    continue
                shift = r-s+e+L0
                assert shift>=0
                if base:
                    power = K0-extra-e
                    assert 0<=power<=K0
                    for j,z in enumerate(ONE_MINUS[power]):
                        assert shift+j<len(p2)
                        p2[shift+j] = (p2[shift+j]+weight*z)%Q
                else:
                    assert shift<len(p1)
                    p1[shift] = (p1[shift]+weight)%Q
                contributions += 1
    # Prefix subtraction is applied to the WHOLE analytic source Y.
    for s in range(1,m+1):
        scale = -sign(s)*CC[s]
        for k in range(s):
            weight = scale*Y[k]*RISING_CHOOSE[k][s]%Q
            p1[k-s+L0] = (p1[k-s+L0]+weight)%Q
    return p2,p1,contributions

def series(p2,p1,k):
    target = k+L0
    if target<0:
        return 0
    return (sum(z*TP2[target-j] for j,z in enumerate(p2[:target+1]))
            +sum(z*TP[target-j] for j,z in enumerate(p1[:target+1])))%Q

def reconstruct(p,rho):
    delta = K0 if rho==2 else 0
    H = [((j-b-L0)*(p[j] if j<len(p) else 0)-(p[j-1] if 0<=j-1<len(p) else 0))%Q
         for j in range(len(p)+1)]
    return [((H[j] if j<len(H) else 0)-(H[j-1] if j else 0)
             +(rho*n+delta)*(p[j-1] if 0<=j-1<len(p) else 0))%Q
            for j in range(len(p)+2)]

def degree(p):
    return next((j for j in range(len(p)-1,-1,-1) if p[j]),-1)

def main():
    global POS,TP,TP2,CC,CHOOSE,RISING_CHOOSE,DERIV,ONE_MINUS,KBAR,SINV
    started = time.monotonic()
    headfile = ROOT/'original_binary_head32_certificate.json'
    head = json.loads(headfile.read_text())
    assert (int(head['b']),int(head['n']),head['precision_bits'])==(b,n,32)
    schurfile = ROOT/'original_binary_operator_schur32_certificate.json'
    schur = json.loads(schurfile.read_text())
    SINV,KBAR = schur['S_end_inverse'],schur['Kbar']
    CC = head['inverse_coefficients']
    POS = small_lower_table(n,R-1)
    TP = inverse_power_table(n,JET+L0)
    TP2 = inverse_power_table(2*n+K0,JET+L0)
    CHOOSE = {k:small_lower_table(B-k,m) for k in range(MAX+1)}
    RISING_CHOOSE = {r:inverse_power_table(B-r+1,m) for r in range(-R,m)}
    DERIV = {extra:inverse_power_table(n+extra,m) for extra in (0,I)}
    ONE_MINUS = [[sign(j)*comb(k,j)%Q for j in range(k+1)] for k in range(K0+1)]

    f = head['first_force_0_71']
    Ff = [sum(sign(ell)*z*comb(B-k,ell) for ell,z in enumerate(f))%Q for k in range(MAX+1)]
    Yf = convolution(TP,Ff,MAX+1)
    eta_f = schur_load(Yf)
    hout = head['complete_exterior_load_0_159']
    Yexp = load_jets(hout)
    eta_e = schur_load(Yexp)
    eta_f_jets,eta_e_jets = load_jets(eta_f),load_jets(eta_e)
    Jf = [(x-y)%Q for x,y in zip(psi_jets(Yf,JET+1),psi_jets(eta_f_jets,JET+1))]
    Je = [(x-y)%Q for x,y in zip(psi_jets(Yexp,JET+1),psi_jets(eta_e_jets,JET+1))]
    v = head['factorial_tail_v_0_35']
    direct_exp = load_jets(v)
    numerical_f = convolution(TP,Jf,JET+1)
    numerical_e = [(x+direct_exp[k])%Q for k,x in enumerate(convolution(TP,Je,JET+1))]

    Pf = polynomial_source_f(f)
    Af = [(z,k,1,I) for k,z in enumerate(Pf)]
    af,bf = load_polynomials([(-x)%Q for x in eta_f])
    Af += [(z,k-m,1,0) for k,z in enumerate(af)]
    Af += [(z,k-m,0,0) for k,z in enumerate(bf)]
    fsource = [(Yf[k]-eta_f_jets[k])%Q for k in range(MAX+1)]
    pf2,pf1,ncf = numerator_psi(Af,fsource)

    combined_e = [(hout[r]-(eta_e[r] if r<m else 0))%Q for r in range(R)]
    ae,be = load_polynomials(combined_e)
    Ae = [(z,k-R,1,0) for k,z in enumerate(ae)]
    Ae += [(z,k-R,0,0) for k,z in enumerate(be)]
    esource = [(Yexp[k]-eta_e_jets[k])%Q for k in range(MAX+1)]
    pe2,pe1,nce = numerator_psi(Ae,esource)
    av,_ = load_polynomials(v)
    for j,z in enumerate(av):
        pe1[L0-len(v)+j] = (pe1[L0-len(v)+j]+z)%Q

    assert degree(pf2)<L0+K0 and degree(pe2)<L0+K0 and degree(pf1)<L0 and degree(pe1)<L0
    # Independent coefficientwise finite inverse vs rational numerator jets.
    checks = 0
    for k in range(-L0,JET+1):
        actual_f = numerical_f[k] if k>=0 else 0
        actual_e = numerical_e[k] if k>=0 else (sign(-k-1)*v[-k-1]%Q if -k<=len(v) else 0)
        assert series(pf2,pf1,k)==actual_f, ('first',k)
        assert series(pe2,pe1,k)==actual_e, ('exponential',k)
        checks += 2
    hf2,hf1,he2,he1 = reconstruct(pf2,2),reconstruct(pf1,1),reconstruct(pe2,2),reconstruct(pe1,1)
    old_TP,old_TP2 = TP,TP2
    TP,TP2 = inverse_power_table(n+1,JET+L0),inverse_power_table(2*n+K0+1,JET+L0)
    reconstruct_checks = 0
    for k in range(-L0,JET+1):
        # Use the independently verified original jets/principal parts.
        gf = numerical_f[k] if k>=0 else 0
        gfprev = numerical_f[k-1] if k>=1 else 0
        ge = numerical_e[k] if k>=0 else (sign(-k-1)*v[-k-1]%Q if -k<=len(v) else 0)
        geprev = numerical_e[k-1] if k>=1 else (sign(-k)*v[-k]%Q if 0<=-k<len(v) else 0)
        assert series(hf2,hf1,k)==((k-b)*gf-gfprev)%Q
        assert series(he2,he1,k)==((k-b)*ge-geprev)%Q
        reconstruct_checks += 2
    assert series(he2,he1,0)==(-b*numerical_e[0]-1)%Q
    old = json.loads((ROOT/'original_binary_numerators_certificate.json').read_text())
    assert [z % (1<<20) for z in numerical_f[:152]] == old['independent_first_response_coefficients_0_151']
    assert [z % (1<<20) for z in numerical_e[:152]] == old['independent_exponential_response_coefficients_0_151']
    branch_tests = []
    for name,p2,p1 in (('first',hf2,hf1),('second',he2,he1)):
        record = {'column':name,'n_branch_zero':all(z == 0 for z in p1),'contact_z_factor':L0}
        if record['n_branch_zero']:
            record['contact_z_factor_verified'] = all(z == 0 for z in p2[:L0])
            if record['contact_z_factor_verified']:
                short = p2[L0:]
                while len(short)>1 and not short[-1]:
                    short.pop()
                before = short[:]
                factor = 0
                while len(short)>1:
                    quotient = [short[0]]
                    for z in short[1:-1]:
                        quotient.append((z+quotient[-1]) % Q)
                    remainder = (short[-1]+quotient[-1]) % Q
                    if remainder:
                        break
                    short = quotient
                    factor += 1
                # Rebuild every removed unit polynomial factor independently.
                rebuilt = short[:]
                for _ in range(factor):
                    rebuilt = [(rebuilt[k] if k<len(rebuilt) else 0)-(rebuilt[k-1] if k else 0) for k in range(len(rebuilt)+1)]
                    rebuilt = [z % Q for z in rebuilt]
                assert rebuilt == before
                record.update({'removed_one_minus_z_factors':factor,'first_nonzero_division_remainder':remainder,
                               'common_order_before_removal':K0+1,'short_denominator_order':K0+1-factor,
                               'short_degree':degree(short),'short_numerator':short})
        branch_tests.append(record)
    cert = {'status':'PASS','scope':'NEW original u0 physical32-bit complete two-branch numerator and bounded-jet gluing; no Gram evaluation',
            'u':0,'b':str(b),'n':str(n),'precision_bits':32,'L0':L0,'k0':K0,
            'first_numerators':[pf2,pf1],'exponential_numerators':[pe2,pe1],
            'reconstructed_first_numerators':[hf2,hf1],'reconstructed_exponential_numerators':[he2,he1],
            'eta_first':eta_f,'eta_exponential':eta_e,
            'independent_first_response_coefficients_0_247':numerical_f,
            'independent_exponential_response_coefficients_0_247':numerical_e,
            'full_principal_parts_verified':True,'exterior_plus_one_verified':True,
            'jet_checks':checks,'reconstruction_checks':reconstruct_checks,
            'new_branch_and_factor_tests':branch_tests,'old20_bit_response_reduction_passed':True,
            'surviving_integral_band_contributions':ncf+nce,
            'head_artifact_sha256':hashlib.sha256(headfile.read_bytes()).hexdigest(),
            'schur_artifact_sha256':hashlib.sha256(schurfile.read_bytes()).hexdigest(),
            'original_Gram_pair_computed':False,'norm_relative_logarithmic_omission_proved':False,
            'wall_seconds':time.monotonic()-started,
            'physical_tail_proof_report_sha256':hashlib.sha256((ROOT.parent/'responses/A5_turn4.md').read_bytes()).hexdigest()}
    target = ROOT/'original_binary_numerators32_certificate.json'
    target.write_text(json.dumps(cert,indent=2)+'\n')
    receipt = {k:v for k,v in cert.items() if k not in ('first_numerators','exponential_numerators',
               'reconstructed_first_numerators','reconstructed_exponential_numerators',
               'eta_first','eta_exponential','independent_first_response_coefficients_0_247',
               'independent_exponential_response_coefficients_0_247')}
    receipt.update({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    'artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
                    'numerator_degrees':[degree(z) for z in (pf2,pf1,pe2,pe1)],
                    'reconstructed_degrees':[degree(z) for z in (hf2,hf1,he2,he1)]})
    (ROOT/'original_binary_numerators32_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    public = dict(receipt)
    public['new_branch_and_factor_tests'] = [{k:v for k,v in z.items() if k != 'short_numerator'} for z in branch_tests]
    print(json.dumps(public,indent=2))

if __name__=='__main__':
    main()
