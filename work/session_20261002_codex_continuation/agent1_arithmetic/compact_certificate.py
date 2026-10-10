from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,math
BASE=Path(__file__).parent
selected=[13,43,53,59,67,71,79,83,89,179,211,281,307,313,331,359,389]
sources=[BASE/'residue_atlas.json',BASE/'residue_atlas_200_997.json']
rows={r['p']:r for f in sources for r in json.loads(f.read_text())}

def log_interval(x,terms=24):
 x=Q(x); k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def unit_interval(y):
  z=(y-1)/(y+1)
  lo=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(terms)),Q(0))
  hi=lo+2*z**(2*terms+1)/(Q(2*terms+1)*(1-z*z))
  return lo,hi
 l2,u2=unit_interval(Q(2));lx,ux=unit_interval(x)
 if k>=0:return k*l2+lx,k*u2+ux
 return k*u2+lx,k*l2+ux
out=[];rho_lo=Q(0);rho_hi=Q(0)
for p in selected:
 r=rows[p]
 assert all(p%d for d in range(2,math.isqrt(p)+1))
 assert not r['endpoint_zeros'] and r['V_zeros']==[0] and r['origin_coefficient']!=0
 assert len(r['states'])==p
 assert all(t['r']==i and t['J'][0]!=0 and (t['V']==0)==(i==0) for i,t in enumerate(r['states']))
 lo,hi=log_interval(p);rho_lo+=2*lo/(p-1);rho_hi+=2*hi/(p-1)
 out.append(dict(p=p,P_residues=[t['J'][0] for t in r['states']],V_residues=[t['V'] for t in r['states']],D_residues=[t['D'] for t in r['states']],C=r['C'],origin_coefficient=r['origin_coefficient']))
sqrt_lo=Q(1414213562373095,10**15);sqrt_hi=sqrt_lo+Q(1,10**15)
assert sqrt_lo**2<2<sqrt_hi**2
_,tau_hi=log_interval(1+sqrt_hi);tau_lo,_=log_interval(1+sqrt_lo);tau_lo*=2;tau_hi*=2
assert rho_lo>tau_hi
cert=dict(status='author finite certificate; not independent mathematical review',scope='criterion C finite residue data plus exact rational rate comparison; infinite theorem proved separately',selected=selected,total_seed_count=sum(selected),rho_lower=str(rho_lo),rho_upper=str(rho_hi),tau_lower=str(tau_lo),tau_upper=str(tau_hi),positive_gap_lower=str(rho_lo-tau_hi),decimal_display=dict(rho_lower=float(rho_lo),rho_upper=float(rho_hi),tau_lower=float(tau_lo),tau_upper=float(tau_hi),gap_lower=float(rho_lo-tau_hi)),sources=[dict(path=str(f),sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in sources],residues=out)
(BASE/'ODD_PRIME_ATLAS_CERTIFICATE.json').write_text(json.dumps(cert,indent=2))
print(json.dumps({k:cert[k] for k in ['selected','total_seed_count','decimal_display']},indent=2))
