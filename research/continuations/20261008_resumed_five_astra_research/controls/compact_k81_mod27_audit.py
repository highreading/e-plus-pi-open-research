from pathlib import Path
from math import factorial,lcm
from collections import Counter
import hashlib,json,time

OUT=Path(__file__).resolve().parent
started=time.monotonic()
k=81; mod=27; last=3*k-2
lam=lcm(*range(1,6*k-4,2))
aa=[1]
for j in range(1,2*last+1):aa.append(1-j*aa[-1])
uu=[aa[2*j] for j in range(last+1)]
cc=[(uu[j]-(-1)**j)%mod for j in range(last+1)]
sig=[(uu[j]+uu[j+1])%mod for j in range(last)]
ret=[]
for j in range(last):
    assert lam%(2*j+1)==0
    ret.append((-lam*(factorial(2*j)+factorial(2*j+2))+4*(lam//(2*j+1)))%mod)

def digest(a):
    return hashlib.sha256(json.dumps(a,separators=(',',':')).encode()).hexdigest()

def valuation(v):
    if not v:return 3
    n=0
    while v%3==0:n+=1;v//=3
    return n

def apply(a,op):
    typ=op[0]
    if typ=='rs':a[op[1]],a[op[2]]=a[op[2]],a[op[1]]
    elif typ=='cs':
        for row in a:row[op[1]],row[op[2]]=row[op[2]],row[op[1]]
    elif typ=='rm':a[op[1]]=[x*op[2]%mod for x in a[op[1]]]
    elif typ=='ra':
        i,j,q=op[1:];a[i]=[(x-q*y)%mod for x,y in zip(a[i],a[j])]
    elif typ=='ca':
        i,j,q=op[1:]
        for row in a:row[i]=(row[i]-q*row[j])%mod
    else:raise AssertionError(typ)

def eliminate(original):
    a=[row[:] for row in original];ops=[];piv=[]
    nr=len(a);nc=len(a[0])
    def record(op):
        if op[0]=='rm':assert op[2]%3
        ops.append(op);apply(a,op)
    for d in range(min(nr,nc)):
        best=(3,None,None)
        for i in range(d,nr):
            for j in range(d,nc):
                v=valuation(a[i][j])
                if v<best[0]:best=(v,i,j)
                if not v:break
            if not best[0]:break
        v,i,j=best
        if v==3:break
        if i!=d:record(['rs',i,d])
        if j!=d:record(['cs',j,d])
        power=3**v
        unit=a[d][d]//power
        record(['rm',d,pow(unit,-1,mod)])
        assert a[d][d]==power
        for i in range(d+1,nr):
            assert a[i][d]%power==0
            q=a[i][d]//power
            if q:record(['ra',i,d,q])
        for j in range(d+1,nc):
            assert a[d][j]%power==0
            q=a[d][j]//power
            if q:record(['ca',j,d,q])
        assert all(a[i][d]==0 for i in range(nr) if i!=d)
        assert all(a[d][j]==0 for j in range(nc) if j!=d)
        piv.append(v)
    replay=[row[:] for row in original]
    for op in ops:apply(replay,op)
    assert replay==a
    assert all(a[i][j]==(3**piv[i] if i==j and i<len(piv) else 0)
               for i in range(nr) for j in range(nc))
    profile=Counter(piv);profile[3]=min(nr,nc)-len(piv)
    assert dict(profile)=={0:84,2:3,3:74}
    return {'shape':[nr,nc],'original_matrix_mod27':original,
            'original_sha256':digest(original),'operations':ops,
            'operations_sha256':digest(ops),'operations_replayed':True,
            'diagonal_sha256':digest(a),'capped_valuations':dict(profile),
            'capped_total':sum(v*n for v,n in profile.items())}

z=[cc[m:m+k]+ret[m:m+k-1] for m in range(2*k)]
y=[sig[m:m+k]+ret[m:m+k] for m in range(2*k-1)]
receipts={name:eliminate(a) for name,a in [('Z',z),('Y',y)]}
full={'k':k,'modulus':mod,'Lambda':lam,
      'physical_boundaries':{'moment_max':last,'factorial_max':6*k-4,'last_odd':6*k-5},
      'receipts':receipts,'coordinator_authored':True,'external_code_executed':False,
      'network_or_credentials_used':False,'all_checks_passed':True,
      'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'seconds':round(time.monotonic()-started,3),
      'scope':'Finite local modulo27 only. No maximal content, all-prime descent or global proof.'}
fullpath=OUT/'compact_k81_mod27_certificate.json'
fullpath.write_text(json.dumps(full,separators=(',',':'))+'\n')
small={key:val for key,val in full.items() if key!='receipts'}
small['full_receipt_sha256']=hashlib.sha256(fullpath.read_bytes()).hexdigest()
small['receipts']={name:{key:val for key,val in rec.items()
                  if key not in ['original_matrix_mod27','operations']}
                  for name,rec in receipts.items()}
(OUT/'compact_k81_mod27_selected.json').write_text(json.dumps(small,indent=2)+'\n')
print(json.dumps(small))
