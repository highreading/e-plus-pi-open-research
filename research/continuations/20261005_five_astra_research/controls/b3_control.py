"""Coordinator-authored exact controls for the matched (n,3,n) family.

Two independent finite constructions check the received algebra. Residue
tables become all-index facts only together with a reviewed transfer proof.
"""
import json
import math
import resource
from fractions import Fraction as F
from pathlib import Path

import sympy as sy

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
OUT = Path(__file__).resolve().parent
x = sy.Symbol('x')


def transition(n, state):
    h,u,v,A,M = state
    t = n+1
    return (-n*h+n*u+v/2,
            t*(h-u+v/2),
            t*(n*h+u-(n+2)*v/2),
            t*M+h-u+v/2,
            t**3*A+t*(2*n+3)*M+(n*n+3*n+4)*h-(n+3)*u+(n+2)*v)


def determinant(rows):
    # Fixed four by four Leibniz formula; no remote program is executed.
    import itertools
    total = F(0)
    for perm in itertools.permutations(range(4)):
        sign = (-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        term = sign
        for i in range(4):
            term *= rows[i][perm[i]]
        total += term
    return total


def contractions(n,state):
    h,u,v,A,M=state
    t=n+1
    a=-n*h+n*u+v/2
    al=h-u+v/2
    be=n*h+u-(n+2)*v/2
    j=a+al
    k=(t-1)*a+2*t*al+be
    l=(t*t-3*t+4)*a+3*t*(t-1)*al+2*t*be
    row_r=(a,t*j,t*k,t*l)
    row_s=(
        (1-t)*a+t*(t-1)*al+t*be,
        (-t*t+3*t+2)*a+t*(t*t-2*t-1)*al+t*t*be,
        t*((-t*t+6*t+3)*a+(t**3-4*t*t+t+2)*al+(t*t-2*t-1)*be),
        t*(-t**3+10*t*t-7*t-6)*a+t*t*(t**3-7*t*t+11*t+7)*al+t*(t**3-5*t*t+2*t+2)*be)
    J=n*h+u
    K=n*(n-1)*h+2*n*u+v
    row_p=(0,h,h+J,h+J+K)
    row_u=(0,j,j+k,j+k+l)
    e=(1,1,1,1)
    sig=-determinant((row_r,row_s,e,row_u))
    chi=-determinant((row_r,row_s,e,row_p))
    kap=determinant((row_r,row_s,row_u,row_p))
    V=sig*A-chi*(M+h-u)-kap
    return (sig,chi,kap,V),row_r,row_s


def polynomial_H(n):
    z=sy.Symbol('z')
    phi=sy.Poly((1-z+z*z/2)**n,z)
    return sy.Poly(sum(math.factorial(n)//math.factorial(n-j)*phi.nth(j)*x**(n-j) for j in range(n+1)),x)


def polynomial_I(poly):
    return sum(sy.diff(poly.as_expr(),x,j).subs(x,1) for j in range(poly.degree()+1))


def modulo(q, modulus):
    return q.numerator*pow(q.denominator,-1,modulus)%modulus


states=[]
state=tuple(map(F,(1,0,0,1,2)))
for n in range(132):
    states.append(state)
    if n<=12:
        H=polynomial_H(n)
        P=sy.Poly(x**n*H.as_expr(),x)
        direct=(H.eval(1),sy.diff(H.as_expr(),x).subs(x,1),sy.diff(H.as_expr(),x,2).subs(x,1),polynomial_I(P),polynomial_I(sy.Poly(x*P.as_expr(),x)))
        assert state==tuple(F(a) for a in direct),(n,state,direct)
        c,r,s=contractions(n,state)
        H1=polynomial_H(n+1)
        H2=polynomial_H(n+2)
        expr1=x**(n+1)*H1.as_expr()
        expr2=x**(n+2)*H2.as_expr()
        assert r==tuple(F(sy.diff(expr1,x,j).subs(x,1)) for j in range(4)),n
        assert s==tuple(F(sy.diff(expr2,x,j+1).subs(x,1)/(n+2)) for j in range(4)),n
    state=transition(n,state)
    assert all(a.denominator==1 for a in state)

expected7=[(1,0,0,1,2,0,5,0,6),(0,1,0,3,4,5,1,1,4),(1,5,2,0,4,6,5,5,2),(2,5,2,2,4,1,2,1,6),(3,6,3,0,2,0,2,1,1),(3,3,3,5,0,2,4,5,5),(5,2,3,5,5,6,3,5,1)]
table_mismatches=[]
for n in range(7):
    c,_,_=contractions(n,states[n])
    actual=tuple(modulo(a,7) for a in states[n]+c)
    if actual!=expected7[n]:
        table_mismatches.append({'r':n,'actual':actual,'received':expected7[n],'exact_contractions':[str(a) for a in c]})

original_primes=[11,13,17,19,23,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
# A new bounded coordinator task: any additional unit prime from this list
# contributes enough to bridge the observed 0.07225 rate deficit.
extension_primes=[101,103,107,109,113,127,131]
primes=original_primes+extension_primes
rows=[]
for p in [7]+primes:
    seeds=[]
    for n in range(p):
        c,_,_=contractions(n,states[n])
        seeds.append({'r':n,'state':[modulo(a,p) for a in states[n]],'contractions':[modulo(a,p) for a in c]})
    zeros=[a['r'] for a in seeds if a['contractions'][-1]==0]
    # Independent control of one full residue period at the recurrence level.
    residue_state=tuple(F(a) for a in (1,0,0,1,2))
    for n in range(2*p):
        if n>=p:
            assert [modulo(a,p) for a in residue_state]==seeds[n-p]['state']
        residue_state=tuple(F(modulo(a,p)) for a in transition(n,residue_state))
    rows.append({'prime':p,'V_zeros':zeros,'seeds':seeds,'period_control':True})


def ln_interval(rational, terms=90):
    # ln(2) and the reduced argument use the convergent atanh series, with
    # explicit rational tails. Reduce to [1,2] to keep convergence uniform.
    q=F(rational)
    shift=0
    while q>=2:
        q/=2;shift+=1
    while q<1:
        q*=2;shift-=1
    def core(v):
        y=(v-1)/(v+1)
        lo=2*sum(y**(2*j+1)/F(2*j+1) for j in range(terms))
        tail=2*y**(2*terms+1)/(F(2*terms+1)*(1-y*y))
        return lo,lo+tail
    lo,hi=core(q)
    l2,h2=core(F(2))
    if shift>=0:return lo+shift*l2,hi+shift*h2
    return lo+shift*h2,hi+shift*l2

unit_primes=[r['prime'] for r in rows if not r['V_zeros']]
Wlo=Whi=F(0)
for p in unit_primes:
    lo,hi=ln_interval(p)
    Wlo+=2*lo/F(p-1);Whi+=2*hi/F(p-1)
scale=10**30
sq=math.isqrt(2*scale*scale)
tau_lo=2*ln_interval(1+F(sq,scale))[0]
tau_hi=2*ln_interval(1+F(sq+1,scale))[1]

def compact_lower(value):
    return F((value*scale).numerator//(value*scale).denominator,scale)

def compact_upper(value):
    a=value*scale
    return F(-((-a.numerator)//a.denominator),scale)

report={'finite_only_without_transfer_proof':True,'independent_polynomial_controls_n':list(range(13)),
        'requested_residue_rows':sum(original_primes),'coordinator_extension_rows':sum(extension_primes),
        'extension_primes':extension_primes,'seven_row_control':'FAIL' if table_mismatches else 'PASS',
        'received_table_mismatches':table_mismatches,
        'unit_primes':unit_primes,'rows':rows,
        'certified_rate':{'W_lower':str(compact_lower(Wlo)),'W_upper':str(compact_upper(Whi)),
                          'tau_lower':str(compact_lower(tau_lo)),'tau_upper':str(compact_upper(tau_hi)),
                          'W_lower_numeric':float(Wlo),'tau_upper_numeric':float(tau_hi),
                          'difference_lower_numeric':float(Wlo-tau_hi),'strict_crossing':Wlo>tau_hi}}
(OUT/'b3_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'seven_row_control':report['seven_row_control'],'received_table_mismatches':table_mismatches,'polynomial_controls':'PASS, n=0..12',
                  'unit_primes':unit_primes,'zero_sets':{r['prime']:r['V_zeros'] for r in rows},
                  'W_lower':float(Wlo),'tau_upper':float(tau_hi),'gap_lower':float(Wlo-tau_hi),
                  'strict_crossing':Wlo>tau_hi},indent=2))
