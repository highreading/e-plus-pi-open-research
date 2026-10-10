from pathlib import Path
from math import comb
import json, hashlib

OUT = Path(__file__).resolve().parent

def rref_and_kernel(a):
    b = [[v % 3 for v in row] for row in a]
    n = len(b[0]); row = 0; pivots = []
    for j in range(n):
        i = next((i for i in range(row, len(b)) if b[i][j]), None)
        if i is None: continue
        b[row], b[i] = b[i], b[row]
        v = pow(b[row][j], -1, 3)
        b[row] = [(v*x) % 3 for x in b[row]]
        for i in range(len(b)):
            if i != row and b[i][j]:
                v = b[i][j]
                b[i] = [(x-v*y) % 3 for x,y in zip(b[i], b[row])]
        pivots.append(j); row += 1
        if row == len(b): break
    vectors = []
    for j in range(n):
        if j in pivots: continue
        v = [0]*n; v[j] = 1
        for i,p in enumerate(pivots): v[p] = -b[i][j] % 3
        assert all(sum(x*y for x,y in zip(rr,v)) % 3 == 0 for rr in a)
        vectors.append(v)
    return row, vectors

def hankel(c, index, rows, cols):
    return [[((-1)**k*comb(2*c,k)) % 3 if 0<=k<=2*c else 0
             for j in range(cols) for k in [index-i-j]] for i in range(rows)]

receipts = []
for c in (10,19,28):
    T = 81; k = (T-1)//2
    blocks = {}
    for name, ind, nr, nc in [('low',k,c,c), ('high',k-1,c,c),
                               ('rectangle',k-1,c,c-1)]:
        a = hankel(c,ind,nr,nc)
        rank, right = rref_and_kernel(a)
        rank2, left = rref_and_kernel(list(map(list,zip(*a))))
        assert rank == rank2
        rob = [sum(((-1)**j)*v for j,v in enumerate(x)) % 3 for x in right]
        lob = [sum(((-1)**j)*v for j,v in enumerate(x)) % 3 for x in left]
        blocks[name] = {'shape':[nr,nc], 'index':ind, 'rank':rank,
            'right_nullspace':right, 'left_nullspace':left,
            'right_endpoint_observations':rob, 'left_endpoint_observations':lob,
            'matrix_sha256':hashlib.sha256(json.dumps(a,separators=(',',':')).encode()).hexdigest()}
    dimension = 243*c-1
    rank = 122*blocks['low']['rank']+119*blocks['high']['rank']+2*blocks['rectangle']['rank']
    endpoint_unit = any(v for b in blocks.values() for f in
                       ['right_endpoint_observations','left_endpoint_observations'] for v in b[f])
    receipts.append({'scaled_T':T,'scaled_c':c, 'chi':243*c, 'P':729*T,
        'delta':dimension,'low_congruence_c_mod9':c%9,'blocks':blocks,
        'assembled_rank_by_REUSED_sector_identity':rank,
        'assembled_nullity':dimension-rank,
        'actual_leading_endpoint_nonzero_on_full_kernel':endpoint_unit,
        'endpoint_annihilator_rank_if_nonzero':rank if endpoint_unit else None,
        'endpoint_annihilator_nullity_if_nonzero':dimension-1-rank if endpoint_unit else None,
        'scope':'Auxiliary scaled finite tuple, not an original index. No uniform rank or directional conclusion.'})
    print(json.dumps({k:v for k,v in receipts[-1].items() if k not in ['blocks','scope']}),flush=True)

obj={'all_checks_passed':True,'coordinator_authored':True,
     'old_sector_decomposition_reused':True,'external_code_executed':False,
     'network_or_credentials_used':False,'max_block_dimension':28,
     'receipts':receipts,
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'second_divided_sector_finite_certificate.json').write_text(json.dumps(obj,indent=2)+'\n')
