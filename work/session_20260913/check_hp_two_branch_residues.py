"""Predeclared modular falsification: odd primes <=101, stop at first extra root.

Direct powers of phi and falling factorials, independent of H's recurrence.
No extension of the prime/index range is authorized by this checker.
"""
import json
from pathlib import Path

def prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p**0.5)+1))

def gates(p):
    inv2=pow(2,-1,p)
    coeff=[1]
    hh=[]
    jj=[]
    for n in range(p+1):
        ff=[1]
        for r in range(1,n+2):
            ff.append(ff[-1]*(n-r+1)%p)
        h=sum(coeff[r]*ff[r] for r in range(n+1))%p
        dh=sum(coeff[r]*ff[r+1] for r in range(n+1))%p
        hh.append(h)
        jj.append((n*h+dh)%p)
        out=[0]*(len(coeff)+2)
        for k,c in enumerate(coeff):
            out[k]=(out[k]+c)%p
            out[k+1]=(out[k+1]-c)%p
            out[k+2]=(out[k+2]+inv2*c)%p
        coeff=out
    return hh,jj

result={"predeclared_max_prime":101,"stop_rule":"first root outside ±1 mod p", "tested":[]}
for p in range(3,102,2):
    if not prime(p):
        continue
    hh,jj=gates(p)
    roots=[r for r in range(p) if hh[r]==jj[r+1]==0]
    extra=[r for r in roots if r not in (1,p-1)]
    result["tested"].append({"p":p,"roots":roots})
    if extra:
        result["counterexample"]={"p":p,"r":extra[0],"H_mod_p":hh[extra[0]],"Jnext_mod_p":jj[extra[0]+1]}
        break
else:
    result["counterexample"]=None
Path(__file__).with_name('hp_two_branch_residue_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
