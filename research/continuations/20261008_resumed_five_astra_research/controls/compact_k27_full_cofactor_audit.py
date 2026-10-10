"""Parent-authored NEW complete Y27 cofactors, not capped spectra."""
from pathlib import Path
from math import factorial, lcm
import datetime
import hashlib
import json

HERE=Path(__file__).resolve().parent
R=HERE.parent
k=27
nrows=2*k-1
maximum_moment=3*k-2
maximum_factorial=2*maximum_moment
last_odd=6*k-5
modulus=3**251
lam=lcm(*range(1,last_odd+1,2))


def valuation(n,p=3):
    if n==0:
        return None
    count=0
    while n%p==0:
        count+=1
        n//=p
    return count


def integer_bareiss(matrix):
    a=[row[:] for row in matrix]
    n=len(a)
    previous=1
    sign=1
    divisions=0
    swaps=[]
    for r in range(n-1):
        if a[r][r]==0:
            i=next((i for i in range(r+1,n) if a[i][r]),None)
            if i is None:
                return 0,{'exact_divisions':divisions,'row_swaps':swaps}
            a[i],a[r]=a[r],a[i]
            swaps.append([r,i]);sign=-sign
        pivot=a[r][r]
        for i in range(r+1,n):
            for j in range(r+1,n):
                numerator=pivot*a[i][j]-a[i][r]*a[r][j]
                value,remainder=divmod(numerator,previous)
                assert remainder==0,('unpaid Bareiss division',r,i,j)
                a[i][j]=value
                divisions+=1
            a[i][r]=0
        previous=pivot
    return sign*a[-1][-1],{'exact_divisions':divisions,'row_swaps':swaps}


def paid_ternary_elimination(matrix):
    # Each active-submatrix p-power division factors that power from ALL
    # remaining rows. The diminished residue modulus and determinant
    # exponent payment are retained, so no nonunit is inverted.
    a=[[value%modulus for value in row] for row in matrix]
    n=len(a)
    current_modulus=modulus
    precision=251
    total_depth=0
    unit=1
    log=[]
    for r in range(n):
        options=[(valuation(a[i][j]),i,j)
                 for i in range(r,n) for j in range(r,n) if a[i][j]]
        assert options,('insufficient precision',r,precision)
        depth,i,j=min(options)
        assert depth<precision
        payment=(n-r)*depth
        total_depth+=payment
        if depth:
            divisor=3**depth
            for ii in range(r,n):
                for jj in range(r,n):
                    assert a[ii][jj]%divisor==0
                    a[ii][jj]//=divisor
            current_modulus//=divisor
            precision-=depth
        row_swap=i!=r
        column_swap=j!=r
        if row_swap:
            a[i],a[r]=a[r],a[i]
            unit=-unit
        if column_swap:
            for row in a:
                row[j],row[r]=row[r],row[j]
            unit=-unit
        pivot=a[r][r]
        assert pivot%3
        unit=unit*(pivot%3)%3
        inverse=pow(pivot,-1,current_modulus)
        for ii in range(r+1,n):
            multiplier=a[ii][r]*inverse%current_modulus
            for jj in range(r+1,n):
                a[ii][jj]=(a[ii][jj]-multiplier*a[r][jj])%current_modulus
            a[ii][r]=0
        log.append({'stage':r,'active_size':n-r,'divided_depth':depth,
                    'determinant_depth_payment':payment,'total_depth':total_depth,
                    'remaining_entry_precision':precision,
                    'row_swap':i if row_swap else None,
                    'column_swap':j if column_swap else None,
                    'unit_pivot_mod3':pivot%3})
    assert total_depth<251
    assert precision>=251-total_depth
    return (3**total_depth)*unit%modulus,total_depth,unit,log


a=[1]
for n in range(1,maximum_factorial+1):
    a.append(1-n*a[-1])
u=[a[2*n] for n in range(maximum_moment+1)]
sigma=[u[n]+u[n+1] for n in range(maximum_moment)]
forcing=[]
for n in range(maximum_moment):
    odd=2*n+1
    assert lam%odd==0
    forcing.append(-lam*(factorial(2*n+2)+factorial(2*n))+4*(lam//odd))
y=[[sigma[m+j] for j in range(k)]+[forcing[m+j] for j in range(k)]
   for m in range(nrows)]
assert maximum_moment==79 and maximum_factorial==158 and last_odd==157
assert len(y)==53 and all(len(row)==54 for row in y)
assert valuation(lam)==4 and (lam//81)%3==2
expected_depth=250
expected_residue=3**250
rows=[]
for omitted in (0,k-1):
    matrix=[[v for j,v in enumerate(row) if j!=omitted] for row in y]
    determinant,exact_log=integer_bareiss(matrix)
    residue,depth,unit,modular_log=paid_ternary_elimination(matrix)
    exact_depth=valuation(determinant)
    exact_unit=(determinant//(3**exact_depth))%3
    assert exact_depth==depth==expected_depth
    assert exact_unit==unit==1
    assert determinant%modulus==residue==expected_residue
    determinant_bytes=abs(determinant).to_bytes((abs(determinant).bit_length()+7)//8,'big')
    rows.append({'omitted_contact_column':omitted,
                 'retained_original_forcing_columns':k,
                 'exact_v3':exact_depth,'normalized_unit_mod3':exact_unit,
                 'determinant_mod_3_251':str(residue),
                 'determinant_sign':1 if determinant>0 else -1,
                 'absolute_determinant_bit_length':abs(determinant).bit_length(),
                 'absolute_determinant_bytes_sha256':hashlib.sha256(determinant_bytes).hexdigest(),
                 'exact_bareiss':exact_log,'paid_ternary_replay':modular_log})
payload=json.dumps(y,separators=(',',':')).encode()
sources=[R/'responses/A2_turn8.md',R/'gates/NEW_FULL_K27_AND_NON_P_54_CHECK_GATE_20261009.md']
output={'status':'PASS','time':datetime.datetime.now().astimezone().isoformat(),
        'scope':'ONLY new auxiliary full Y27 cofactor residues. NOT an original-index experiment or an all-prime proof.',
        'k':k,'shape':[53,54],'maximum_moment':79,'maximum_factorial':158,
        'last_odd_denominator':157,'complete_Lambda':str(lam),
        'complete_matrix_sha256':hashlib.sha256(payload).hexdigest(),
        'expected_v3':250,'expected_unit_mod3':1,'cofactors':rows,
        'all_nonunit_divisions_paid':True,'closed_capped_spectra_recomputed':False,
        'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'original_index_claim':False,'global_proof':False}
(HERE/'compact_k27_full_cofactor_certificate.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'status':'PASS','scope':output['scope'],'cofactors':[
    {key:row[key] for key in ('omitted_contact_column','exact_v3','normalized_unit_mod3','exact_bareiss')}
    for row in rows],'global_proof':False}))
