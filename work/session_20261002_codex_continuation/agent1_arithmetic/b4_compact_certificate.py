from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
BASE=Path(__file__).parent
selected=[5,7,43,67,71]
seed_source=BASE/'b4_finite_criterion.json'
reference_source=BASE/'b4_boundary_constants.json'
rows={r['p']:r for r in json.loads(seed_source.read_text())['rows']}
references={r['p']:r for r in json.loads(reference_source.read_text())}

def log_interval(x,terms=24):
 x=Q(x);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def unit_interval(y):
  z=(y-1)/(y+1)
  lo=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(terms)),Q(0))
  hi=lo+2*z**(2*terms+1)/(Q(2*terms+1)*(1-z*z))
  return lo,hi
 l2,u2=unit_interval(Q(2));lx,ux=unit_interval(x)
 return (k*l2+lx,k*u2+ux) if k>=0 else (k*u2+lx,k*l2+ux)

out=[];rho_lo=Q(0);rho_hi=Q(0)
for p in selected:
 assert all(p%d for d in range(2,p))
 r=rows[p];ref=references[p]
 assert not r['endpoint_zeros'] and r['V_zeros']==[0,p-1] and r['origin_coefficient']!=0 and 864%p
 assert len(r['states'])==p
 assert all(t['n']==i and t['J'][0]!=0 and (t['V']==0)==(i in [0,p-1]) for i,t in enumerate(r['states']))
 assert ref['reference_n']==p*p-1 and int(ref['modulus'])==p**5
 assert ref['state']['D']==ref['D_residue'] and ref['state']['V']==ref['V_residue']
 assert ref['D_residue']%(p**4)==0 and ref['V_residue']%(p**4)==0
 invP=pow(ref['P_residue'],-1,p)
 delta=(ref['D_residue']//p**4)*invP**2%p
 nu=(ref['V_residue']//p**4)*invP%p
 assert delta==ref['delta'] and nu==ref['nu'] and nu
 lo,hi=log_interval(p);rho_lo+=2*lo/(p-1);rho_hi+=2*hi/(p-1)
 out.append(dict(p=p,P_residues=[t['J'][0] for t in r['states']],V_residues=[t['V'] for t in r['states']],D_residues=[t['D'] for t in r['states']],C=r['C'],origin_coefficient=r['origin_coefficient'],reference=dict(n=ref['reference_n'],modulus=ref['modulus'],D=ref['D_residue'],V=ref['V_residue'],P=ref['P_residue'],delta=delta,nu=nu)))
sqrt_lo=Q(1414213562373095,10**15);sqrt_hi=sqrt_lo+Q(1,10**15)
assert sqrt_lo**2<2<sqrt_hi**2
_,tau_hi=log_interval(1+sqrt_hi);tau_lo,_=log_interval(1+sqrt_lo);tau_lo*=2;tau_hi*=2
assert rho_lo>tau_hi
cert=dict(status='author finite certificate; infinite boundary/origin theorem and canonical identification remain separate proof obligations',scope='b4,m1 normalized finite prime criterion and exact rational rate; no b4 signed-error theorem assumed',selected=selected,total_seed_count=sum(selected),rho_lower=str(rho_lo),rho_upper=str(rho_hi),benchmark_tau_lower=str(tau_lo),benchmark_tau_upper=str(tau_hi),benchmark_gap_lower=str(rho_lo-tau_hi),decimal_display=dict(rho_lower=float(rho_lo),rho_upper=float(rho_hi),benchmark_tau_lower=float(tau_lo),benchmark_tau_upper=float(tau_hi),benchmark_gap_lower=float(rho_lo-tau_hi)),sources=[dict(path=str(f),sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in [seed_source,reference_source]],residues=out)
(BASE/'B4_NORMALIZED_PRIME_CERTIFICATE.json').write_text(json.dumps(cert,indent=2))
print(json.dumps({k:cert[k] for k in ['selected','total_seed_count','decimal_display']},indent=2))
