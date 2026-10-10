"""Coordinator check of the fixed coefficient-depth inequalities in A5t21."""
import json,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
old=json.loads((OUT/'binary_fifth_moment_control_compact.json').read_text())
rows={}
for rs,b,f,g in [((0,64),0,1,2),((4,68),0,4,4),((2,66),1,2,2),
   ((32,),1,1,2),((36,),1,4,4),((1,3,16,20,34,48,52,65,67),2,1,0),
   ((8,12,18,24,28,33,35,40,44,50,56,60),3,0,0),((96,),2,1,2),((100,),2,4,4)]:
    for r in rs:rows[r]=(b,f,g)
def vf(k):return k-k.bit_count()
def v2(x):return (x & -x).bit_length()-1 if x else 1000
receipt=[];fails=[]
for row in old['tables']:
    rho=row['rho'];eps=int(rho>68);ar=84-rho+128*eps
    b,f,g=rows[rho]
    ds=[]
    for name,lo,coeff,target in [('U',-1,row['U_s_minus1_to11_mod64'],f),
                               ('V',-8,row['V_s_minus8_to11_mod128'],g)]:
        for i,co in enumerate(coeff):
            s=lo+i;delta=int(s<-4);l=80-rho-s+128*eps;c=4+s+128*delta
            assert 0<=ar<128 and 0<=l<128 and 0<=c<128
            m=127*delta+vf(ar)-vf(l)-vf(c)
            assert m>=0
            d=v2(co)+m
            ds.append({'column':name,'s':s,'stripping_depth':m,'coefficient_residue':co,
                'combined_depth_lower_bound':d,'required_depth':target})
            if d<target:fails.append({'rho':rho,**ds[-1]})
    receipt.append({'rho':rho,'weight_depth':b,'f_bound':f,'g_bound':g,'comparisons':ds})
report={'comparisons':sum(len(r['comparisons']) for r in receipt),
    'all_fixed_depth_inequalities_pass':not fails,'failures':fails,'receipt':receipt,
    'scope':'Fixed low-factor inequalities only. No check of the remaining paired unit '
            'identity or infinite fifth-discrepancy theorem.'}
(OUT/'binary_fifth_stripping_depth_control.json').write_text(json.dumps(report,indent=2)+'\n')
(OUT/'binary_fifth_stripping_depth_control_compact.json').write_text(json.dumps(report,separators=(',',':'))+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='receipt'}))
assert not fails
