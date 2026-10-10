"""Parent-authored bounded verification of the new actual acceptance divisor.

No remote code is executed. This verifies u=0 digit arithmetic and a finite
range of the classical tail convolution only; the new full theorem needs review.
"""
from pathlib import Path
from fractions import Fraction
import math,json,hashlib
R=Path(__file__).resolve().parents[1]
b=9**18;n=4002*b;B=b-1;g=(n//2+1)//2;d=(b-1)//4
s=lambda z:z.bit_count()
chi=s(n)+s(B)-s(n+B)
a_end=s(d)+s(g-d)-s(g)
excess=2*s(n)-s(n+B)-s(n-B+2)
assert chi-a_end==excess
assert n%64==2 and s(n+2)==s(n)
checks=0
for nn in range(1,21):
    for q in range(1,15):
        for v in range(10):
            lhs=sum((-1)**(q+w)*math.comb(nn+q+w-1,q+w)*math.comb(nn,v-w)
                    for w in range(v+1) if v-w<=nn)
            rhs=Fraction((-1)**q*nn*math.comb(nn+q-1,q-1)*
                         (math.comb(nn-1,v) if v<=nn-1 else 0),q+v)
            assert lhs==rhs,(nn,q,v,lhs,rhs)
            checks+=1
certificate={'scope':'Finite u=0 arithmetic and finite classical identity checks; not an infinite-family proof.',
             'original_u':0,'b':str(b),'n':str(n),'B':str(B),
             'binary_words':{name:bin(value) for name,value in [('B',B),('n',n),('n_plus_B',n+B),('g',g),('d',d),('g_minus_d',g-d)]},
             'digit_sums':{name:s(value) for name,value in [('B',B),('n',n),('n_plus_B',n+B),('g',g),('d',d),('g_minus_d',g-d)]},
             'chi':chi,'endpoint_upper_bound':a_end,'sufficient_paid_excess':excess,
             'chi_ge_11':chi>=11,
             'conditional_on_unreviewed_A5_turn8':'If its full-return theorem is accepted, v2(S)>=chi+1, so the reviewed a<=a_end gives the stated lower bound on paid linear acceptance. Only modulo2 transfers to Q.',
             'conditional_v2_S_lower_bound':chi+1,
             'conditional_v2_paid_linear_acceptance_lower_bound':max(0,excess),
             'tail_convolution_checks':checks,'tail_convolution_range':{'n':[1,20],'q':[1,14],'v':[0,9]},
             'report_sha256':hashlib.sha256((R/'responses/A5_turn8.md').read_bytes()).hexdigest()}
p=R/'controls/binary_actual_adjoint_binomial_certificate.json'
p.write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps({k:certificate[k] for k in ['chi','endpoint_upper_bound','sufficient_paid_excess','chi_ge_11','tail_convolution_checks','scope']}))
