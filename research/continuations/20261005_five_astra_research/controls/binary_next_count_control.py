"""Coordinator-authored bounded arithmetic count control, not an infinite proof."""
import json
import resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent

def vb(n,k):
    if k<0 or k>n:return 999999
    return k.bit_count()+(n-k).bit_count()-n.bit_count()

def t_count(a,v):
    return sum(not(i & ~a) and not((v-i)&(2*a+1)) for i in range(v+1))

def t_mod4(a,v):
    states=[1,0]
    previous=0
    for k in range(max(1,v.bit_length())):
        digit=(a>>k)&1
        h=digit if k==0 else 1+digit-previous
        target=(v>>k)&1
        new=[0,0]
        for carry in (0,1):
            for nxt in (0,1):
                picked=target+2*nxt-carry
                coefficient=(1 if picked in (0,h) else 2) if 0<=picked<=h else 0
                new[nxt]=(new[nxt]+states[carry]*coefficient)%4
        states=new
        previous=digit
    return states[0]

failures=[]
for D in range(1,802,2):
    C=4002*D+2532
    e=2*C+1
    a=(C-2)//4
    v=D//4
    valuations=[vb(C,t)+vb(e+D-t,D-t) for t in range(D+1)]
    c1=valuations.count(1)
    c2=valuations.count(2)
    total=t_count(a,v)
    chi=(vb(a+v+1,v-1)==0) if D%4==1 else 0
    if c1!=2*total or c2%2!=chi or t_mod4(a,v)!=total%4:
        failures.append({'D':D,'C1':c1,'C2':c2,'T':total,'chi':int(chi)})
assert not failures

# These are genuine original powers. Only bounded arithmetic carry tests
# are evaluated, with no matrices or claims of uniform exponent behavior.
original=[]
for u in range(64):
    r=18+32*u
    b=9**r
    assert b%128==81
    D=(b-81)//128
    C=4002*D+2532
    a=(C-2)//4
    v=D//4
    total=t_mod4(a,v)
    zero=bool(v&(a+1))
    chi=(vb(a+v+1,v-1)==0) if D%4==1 else 0
    norm5=(total//2+chi)%2 if zero else None
    if r%128==50:
        assert total==0 and not chi
    original.append({'r':r,'fourth_norm_bit':0 if zero else 1,
                     'T_mod4':total,'fifth_norm_bit_on_zero_locus':norm5})

report={'auxiliary_D_range':[1,801,2],'auxiliary_cases':401,
 'C1_exact_doubling_and_C2_parity_and_two_state_count_pass':True,
 'failures':failures,'actual_exponent_tests':original,
 'finite_scope_only':True,'large_original_norms_not_computed':True,
 'no_infinite_population_or_alignment_claim':True}
(OUT/'binary_next_count_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'cases':401,'all_count_checks_pass':True,
                 'original_powers_checked':64,
                 'first_original_rows':original[:6]}))
