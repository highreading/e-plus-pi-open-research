#!/usr/bin/env python3
"""New short-numerator and single-summand polynomial certificates."""
from math import comb
from pathlib import Path
import hashlib
import json
import resource

resource.setrlimit(resource.RLIMIT_CPU,(90,90))
ROOT=Path(__file__).resolve().parent
Q=1<<20

def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def multiply(a,b,M):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%M
    return trim(c)

def linear(a,c,M):return multiply(a,[c%M,-1%M],M)

def divide_one(a):
    a=trim(a[:]);out=[];acc=0
    for x in a[:-1]:acc=(acc+x)%Q;out.append(acc)
    assert (acc+a[-1])%Q==0
    assert multiply(out,[1,-1],Q)==a
    return trim(out)

def remove(a,r):
    for _ in range(r):a=divide_one(a)
    return a

def makeU(poly,R,B,b,M):
    result=[0]*(R+1)
    for r,co in enumerate(poly):
        term=[co%M]
        for t in range(r):term=linear(term,b-t,M)
        for t in range(R-r):term=linear(term,B+b+t,M)
        for i,x in enumerate(term):result[i]=(result[i]+x)%M
    return trim(result)

def delta_column(k,A,Bpoly,M):
    out=[0]*(k+5)
    for j,co in enumerate(A):
        for t in range(k+1):out[j+t]=(out[j+t]+co*comb(k,t))%M
    for j,co in enumerate(Bpoly):out[j+k]=(out[j+k]-co)%M
    return trim(out)

def v2(n):
    assert n
    return (abs(n)&-abs(n)).bit_length()-1

def certificate(payload,n,b,bits):
    M=1<<bits;D=len(payload)-1
    A=multiply([n+2,-1],[n+2,-1],M);A=multiply(A,multiply([b,-1],[b,-1],M),M)
    Bpoly=multiply([0,0,1],multiply([2*n+b,-1],[2*n+b,-1],M),M)
    tau=2*n-4
    cols=[delta_column(k,A,Bpoly,M) for k in range(D-2)]
    for k,col in enumerate(cols):assert len(col)==k+4 and col[-1]==(k+tau)%M
    P=payload[:];R=[0]*(D-2);Gamma=1;guard=0
    for k in range(D-3,-1,-1):
        pivot=k+tau;lc=P[k+3]
        P=[x*pivot%M for x in P]
        for i,x in enumerate(cols[k]):P[i]=(P[i]-lc*x)%M
        R=[x*pivot%M for x in R];R[k]=(R[k]+lc)%M
        Gamma=Gamma*pivot%M;guard+=v2(pivot)
        assert P[k+3]==0
    assert all(x==0 for x in P[3:])
    rhs=[0]*(D+1)
    for k,r in enumerate(R):
        for i,x in enumerate(cols[k]):rhs[i]=(rhs[i]+r*x)%M
    for i,x in enumerate(P[:3]):rhs[i]=(rhs[i]+x)%M
    assert rhs==[Gamma*x%M for x in payload]
    boundary=sum(r*pow(b+1,k,M) for k,r in enumerate(R))%M
    return {'degree':D,'precision_bits':bits,'tau':str(tau),'Gamma_modulus':str(Gamma),'pivot_product_v2':guard,
            'R_coefficients':[str(x) for x in R],'remaining_Q012':[str(x) for x in P[:3]],'boundary_R_b1':str(boundary),
            'full_polynomial_identity_residual_zero':True}

def main():
    original=ROOT/'original_binary_numerators_certificate.json';x=json.loads(original.read_text());n,b=int(x['n']),int(x['b'])
    Fwide=x['reconstructed_first_numerators'][0];Ewide=x['reconstructed_exponential_numerators'][0]
    assert not any(Fwide[:176]) and not any(Ewide[:176])
    Vf=Fwide[176:];Ve=Ewide[176:]
    assert not any(x['reconstructed_first_numerators'][1]) and not any(x['reconstructed_exponential_numerators'][1])
    Af,Ae=remove(Vf,44),remove(Ve,48)
    assert len(Af)==82 and len(Ae)==78
    B=2*n
    df=1;de=1
    for k in range(81):df*=B+k
    for k in range(77):de*=B+k
    assert (v2(df),v2(de))==(80,77)
    M=1<<341
    Uf,Ue=makeU(Af,81,B,b,M),makeU(Ae,77,B,b,M)
    norm=multiply(Uf,Uf,M);mixed=multiply(Uf,Ue,M)
    assert len(norm)==163 and len(mixed)==159
    certificates=[certificate(norm,n,b,341),certificate(mixed,n,b,341)]
    guards=[z['pivot_product_v2']+v2(df)*(2 if i==0 else 1)+(v2(de) if i else 0) for i,z in enumerate(certificates)]
    assert guards==[321,315]
    # Verify the new independent-shift conversion at a few bounded coefficients.
    # These are polynomial identities, not contact-jet reruns or Gram evaluation.
    conversion=[]
    for poly,R,U,D in ((Af,81,Uf,df),(Ae,77,Ue,de)):
        for k in (0,1,2,9,24,83):
            lhs=sum(co*comb(B+R+k-r-1,k-r) for r,co in enumerate(poly) if r<=k)%M
            payload=sum(U[i]*pow(b-k,i,M) for i in range(len(U)))%M
            rhs=comb(B+k-1,k)*payload%M
            assert lhs*(D%M)%M==rhs
            conversion.append({'degree':R,'k':k,'residual_zero':True})
    artifact={'status':'PASS','scope':'new synthetic factor removal and TWO single22-summand moment identities for complete original20bit columns; no Gram evaluated',
              'b':str(b),'n':str(n),'precision_bits_physical':20,'short_first_numerator':Af,'short_exponential_numerator':Ae,
              'short_degrees':[81,77],'denominator_exponents':['2n+81','2n+77'],'removed_factors':[44,48],
              'common_summand':'binom(n+2,j)^2 * binom(2n+b-j-1,b-j)^2, 0<=j<=b',
              'Df_v2':80,'De_v2':77,'Uf_mod341':[str(a) for a in Uf],'Ue_mod341':[str(a) for a in Ue],
              'moment_certificates':certificates,'total_denominator_guards':guards,'conversion_checks':conversion,
              'original_weighted_Gram_evaluated':False,'norm_relative_logarithmic_guard_proved':False}
    target=ROOT/'binary_short_moment_certificate.json';target.write_text(json.dumps(artifact,indent=2)+'\n')
    receipt={'status':'PASS','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'input_artifact_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),
             'artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'scope':artifact['scope'],
             'short_degrees':[81,77],'factor_divisions_with_zero_remainders':92,'denominator_valuations':[80,77],
             'payload_degrees':[162,158],'pivot_product_valuations':[z['pivot_product_v2'] for z in certificates],
             'total_denominator_guards':guards,'pure_kernel_precision_bits_sufficient':[341,335],
             'complete_polynomial_identity_checks':2,'bounded_conversion_checks':len(conversion),'original_weighted_Gram_evaluated':False}
    (ROOT/'binary_short_moment_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2),flush=True)

if __name__=='__main__':main()
