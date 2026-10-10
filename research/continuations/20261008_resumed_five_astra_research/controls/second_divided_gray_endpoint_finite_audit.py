from pathlib import Path
from math import comb
from fractions import Fraction
import hashlib,json,time

HERE=Path(__file__).resolve().parent
started=time.monotonic()

def kernel(a):
    b=[[v%3 for v in row] for row in a]
    rows=len(b);cols=len(b[0]);pivots=[];r=0
    for col in range(cols):
        pivot=next((i for i in range(r,rows) if b[i][col]),None)
        if pivot is None:continue
        b[r],b[pivot]=b[pivot],b[r]
        inv=pow(b[r][col],-1,3)
        b[r]=[v*inv%3 for v in b[r]]
        for i in range(rows):
            if i!=r and b[i][col]:
                scalar=b[i][col]
                b[i]=[(v-scalar*w)%3 for v,w in zip(b[i],b[r])]
        pivots.append(col);r+=1
        if r==rows:break
    out=[]
    for col in range(cols):
        if col in pivots:continue
        v=[0]*cols;v[col]=1
        for i,p in enumerate(pivots):v[p]=-b[i][col]%3
        assert all(sum(x*y for x,y in zip(row,v))%3==0 for row in a)
        out.append(v)
    return r,out

def block(c,index,rows,cols):
    coeff=[(-1)**j*comb(2*c,j)%3 for j in range(2*c+1)]
    return [[coeff[index-i-j] if 0<=index-i-j<=2*c else 0
             for j in range(cols)] for i in range(rows)]

receipts=[]
for c in [46,55,64,73]:
    T=243;Pi=243*T;P=3*Pi;chi=243*c;delta=chi-1
    kappa=(Pi-1)//2
    assert delta==min(chi-1,(P+3)//2-3*chi)
    assert 2*chi+2*delta-1-kappa>delta and 2*chi+delta-Pi<=0
    rho=Fraction(25*P+2*chi,243*P)
    assert Fraction(103,1000)<rho<Fraction(104,1000)
    assert c%9==1 and T%9==0
    blocks={}
    for name,index,rows,cols in [('low',(T-1)//2,c,c),
                               ('high',(T-3)//2,c,c),
                               ('rectangle',(T-3)//2,c,c-1)]:
        a=block(c,index,rows,cols)
        rank,right=kernel(a)
        rank2,left=kernel(list(map(list,zip(*a))))
        assert rank==rank2
        right_e=[sum((-1)**j*v for j,v in enumerate(z))%3 for z in right]
        left_e=[sum((-1)**j*v for j,v in enumerate(z))%3 for z in left]
        witnesses=[{'side':side,'vector':vec,'endpoint_mod3':e}
                   for side,vecs,es in [('right',right,right_e),('left',left,left_e)]
                   for vec,e in zip(vecs,es) if e]
        blocks[name]={'shape':[rows,cols],'index':index,'rank':rank,
                      'right_kernel_dimension':len(right),'left_kernel_dimension':len(left),
                      'right_endpoint_values':right_e,'left_endpoint_values':left_e,
                      'endpoint_unit_witness':witnesses[0] if witnesses else None,
                      'matrix_sha256':hashlib.sha256(json.dumps(a,separators=(',',':')).encode()).hexdigest()}
    rank=122*blocks['low']['rank']+119*blocks['high']['rank']+2*blocks['rectangle']['rank']
    endpoint_unit=any(v['endpoint_unit_witness'] is not None for v in blocks.values())
    item={'scaled_T':T,'scaled_c':c,'P':P,'chi':chi,'delta':delta,
          'necessary_ratio':str(rho),'blocks':blocks,
          'assembled_rank_by_REUSED_sector_identity':rank,'assembled_nullity':delta-rank,
          'endpoint_nonzero_on_auxiliary_complete_kernel':endpoint_unit,
          'endpoint_annihilator_nullity_if_nonzero':delta-1-rank if endpoint_unit else None,
          'scope':'Auxiliary scaled tuple, not a certified original index; no uniform or physical directional conclusion.'}
    receipts.append(item)
    print(json.dumps({k:v for k,v in item.items() if k not in ['blocks','scope']}),flush=True)

out={'all_checks_passed':True,'coordinator_authored':True,
     'external_code_executed':False,'network_or_credentials_used':False,
     'old_T81_receipt_recomputed':False,'dense_assembled_matrix_created':False,
     'max_block_dimension':73,'receipts':receipts,
     'seconds':round(time.monotonic()-started,3),
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'second_divided_gray_endpoint_finite_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
