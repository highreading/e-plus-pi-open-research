"""Parent-authored complete actual source periods at p7 and13.

Reuse the CLOSED U mod p cycles and the five completed original source jets.
Only previously unresolved residue classes get fresh paid source arithmetic.
No complete normalization or denominator is computed. All loops are bounded.
"""
from pathlib import Path
from math import factorial,gcd
import hashlib,json,time
OUT=Path(__file__).resolve().parent

def cm(a,b,m):return ((a[0]*b[0]-a[1]*b[1])%m,(a[0]*b[1]+a[1]*b[0])%m)
def cs(a,b,m):return ((a[0]-b[0])%m,(a[1]-b[1])%m)
def scale(a,k,m):return (a[0]*k%m,a[1]*k%m)
ID=((1,0),(0,0),(0,0),(1,0))
def mm(a,b,m):
    out=[]
    for i in range(2):
        for j in range(2):
            t1=cm(a[2*i],b[j],m);t2=cm(a[2*i+1],b[2+j],m)
            out.append(((t1[0]+t2[0])%m,(t1[1]+t2[1])%m))
    return tuple(out)
def mp(a,n,m):
    out=ID
    while n:
        if n&1:out=mm(out,a,m)
        a=mm(a,a,m);n//=2
    return out
def factors(n):
    out=[];d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:out.append(n)
    return out
def cheb(n,m):
    z=(-1%m,2%m);a=(1,0);b=z
    for bit in bin(n)[2:]:
        d=cs(scale(cm(a,a,m),2,m),(1,0),m)
        e=cs(scale(cm(a,b,m),2,m),z,m)
        f=cs(scale(cm(b,b,m),2,m),(1,0),m)
        a,b=(d,e) if bit=='0' else (e,f)
    prev=cs(scale(cm(z,a,m),2,m),b,m)
    inv=cs(cs(cm(a,a,m),scale(cm(z,cm(a,prev,m),m),2,m),m),scale(cm(prev,prev,m),-1,m),m)
    assert inv==cs((1,0),cm(z,z,m),m)
    return a,prev
def jet(n,J,m):
    a=1;out=[]
    for r in range(J):
        out.append(a%m)
        if r+1<J:
            a,rem=divmod(-2*(n*n-r*r)*a,(r+1)*(2*r+1));assert rem==0
    return out
def mul(a,b,J,m):
    out=[0]*J
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:J-i]):out[i+j]=(out[i+j]+x*y)%m
    return out
def dep(x,p,cap):
    if not x:return cap
    v=0
    while v<cap and not x%p:x//=p;v+=1
    return v

first_path=OUT/'signed_chebyshev_first_source_period_certificate.json'
first=json.loads(first_path.read_text())
u_tables={a['p']:{r['N_mod_p_squared']:r['U_mod_p'] for r in a['records']} for a in first['records']}
missing_path=OUT/'signed_chebyshev_missing_source_jet_certificate.json'
missing=json.loads(missing_path.read_text())
started=time.monotonic();result=[]
for p,cap,candidate in ((7,3,117600),(13,1,2184)):
    m=p**cap;J=cap*p;z=(-1%m,2%m)
    T=(scale(z,2,m),(-1%m,0),(1,0),(0,0))
    # The candidate is validated by explicit matrix powering, not assumed
    # from an unread group-order theorem.
    assert mp(T,candidate,p)==ID
    base=candidate
    for f in factors(base):
        while base%f==0 and mp(T,base//f,p)==ID:base//=f
    period=base*p**(cap-1)
    assert mp(T,period,m)==ID
    for f in factors(period):
        while period%f==0 and mp(T,period//f,m)==ID:period//=f
    assert mp(T,period,m)==ID
    minimality={str(f):mp(T,period//f,m)!=ID for f in factors(period)}
    assert all(minimality.values())
    # The integer binomial formula below r<J needs an extra r-division
    # budget and the largest binomial lower-index digit budget.
    digit_budget=0;bound=2*J-3
    while p**(digit_budget+1)<=bound:digit_budget+=1
    r_division_budget=max(dep(r,p,100) for r in range(1,J))
    exponent=cap+digit_budget+r_division_budget
    jet_period=p**exponent
    L=jet_period*period//gcd(jet_period,period)
    old_by_residue={}
    for a in missing['records']:
        if a['p']==p:
            key=pow(9,18+32*a['original_u'],L)
            old_by_residue[key]=a
    residue=pow(9,18,L);start=residue;step=pow(9,32,L)
    seen=set();rows=[];fresh=0;reused=0;unit_u=0
    moments=[(-1)**r*factorial(r)%m for r in range(J)]
    assert dep(factorial(J),p,100)>=cap
    t=[1,m-1]+[0]*(J-2);omt=[0,1]+[0]*(J-2)
    one_t2=mul(t,t,J,m);one_t2[0]=(one_t2[0]+1)%m
    H=mul(mul(t,omt,J,m),mul(one_t2,one_t2,J,m),J,m)
    while residue not in seen:
        assert len(rows)<100000
        seen.add(residue);u_mod_p=u_tables[p][residue%(p*p)]
        row={'u_cycle_position':len(rows),'N_residue':residue,'U_mod_p':u_mod_p}
        if u_mod_p:
            unit_u+=1;row.update({'c_depth':0,'reason':'reused_complete_U_unit_period'})
        else:
            if residue in old_by_residue:
                old=old_by_residue[residue];reused+=1
                cn=tuple(x%m for x in old['complex_C_N']);cp=tuple(x%m for x in old['complex_C_Nminus1'])
                V=old['raw_V']%m;U=old['U']%m;row['source']='reused_five_original_jet_receipt'
            else:
                fresh+=1;n=residue+L
                cn,cp=cheb(n,m);bn,bp=cn[1],cp[1]
                d=(cn[0]*bp-cp[0]*bn)%m
                jn,jp,jk=jet(n,J,m),jet(n-1,J,m),jet(n-3,J,m)
                bj=[(bp*jn[r]-bn*jp[r])%m for r in range(J)]
                B2=mul(bj,bj,J,m);K=mul(H,mul(jk,jk,J,m),J,m)
                U=-sum(K[r]*moments[r] for r in range(J))%m
                I=sum(B2[r]*moments[r] for r in range(J))%m;V=(I-d*d)%m
                row['source']='fresh_previously_unresolved_residue'
            assert U%p==0
            r=min(dep(cn[1],p,cap),dep(cp[1],p,cap));dv=dep(V,p,cap)
            row.update({'complex_C_N':cn,'complex_C_Nminus1':cp,'U_mod_p_power':U,
                        'raw_V_mod_p_power':V,'g_depth_capped':r,'raw_V_depth_capped':dv})
            if 2*r<cap:
                assert V%(p**(2*r))==0
                row['paid_square_division']=p**(2*r)
                row['divided_V_mod_p']=V//p**(2*r)%p
                if dv==2*r:row.update({'c_depth':0,'reason':'paid_divided_V_unit'})
                else:row.update({'c_depth_at_least':1,'reason':'potential_c_factor_or_precision_obligation'})
            else:row['reason']='square_division_precision_obligation'
        rows.append(row);residue=residue*step%L
    assert residue==start
    item={'p':p,'precision':cap,'Gaussian_matrix_period':period,
          'Gaussian_base_period':base,'matrix_period_identity_verified':True,
          'matrix_period_minimality_checks':minimality,
          'jet_period':jet_period,'jet_digit_budget':digit_budget,
          'jet_r_division_budget':r_division_budget,'combined_N_modulus':L,
          'cycle_length':len(rows),'cycle_closed_at_start':True,'start':start,'step':step,
          'unit_U_cases_reused':unit_u,'old_original_jet_cases_reused':reused,
          'fresh_source_cases':fresh,'all_c_units':all(r.get('c_depth')==0 for r in rows),
          'open_rows':[r for r in rows if r.get('c_depth')!=0],'records':rows}
    result.append(item)
    print(json.dumps({k:item[k] for k in ('p','Gaussian_matrix_period','jet_period','combined_N_modulus',
          'cycle_length','unit_U_cases_reused','old_original_jet_cases_reused','fresh_source_cases','all_c_units')}
          |{'open_row_count':len(item['open_rows'])}),flush=True)
obj={'checks_passed':True,'scope':'Complete fixed-prime actual-source periods at7/13, with explicit Gaussian period and paid finite-source periodicity. Subject to companion proof; not an ALL-prime estimate.',
     'records':result,'network_or_keys_used':False,'h_lambda_G_q_computed':False,
     'source_receipts':[{'file':a.name,'sha256':hashlib.sha256(a.read_bytes()).hexdigest()} for a in (first_path,missing_path)],
     'seconds':round(time.monotonic()-started,3),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'signed_chebyshev_complete_fixed_prime_period_certificate.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps({'complete':True,'seconds':obj['seconds']}),flush=True)
