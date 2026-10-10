"""Parent-authored bounded sparse Lucas-mask extension of the mod4 audit."""
from pathlib import Path
import hashlib,json,time
from binary_actual_contact_mod4_audit import evaluate,choose4
ROOT=Path(__file__).resolve().parent

def main():
    started=time.monotonic();cases=[]
    for u in range(3):
        b=9**(18+32*u);N=4002*b+2
        one=[1<<k for k in range(N.bit_length()) if (N>>k)&1 and (1<<k)<b]
        short=one[:32]
        pairs=[x+y for i,x in enumerate(short) for y in short[i+1:] if x+y<b]
        positions=sorted(set([0]+one+pairs))
        assert len(positions)<=1000
        data=evaluate(b,positions)
        assert all(choose4(N,j)%2 for j in positions)
        witnesses=[j for j in positions if data['selected_contact_residues'][j]==2]
        counts={str(r):sum(v==r for v in data['selected_contact_residues'].values())
                for r in range(4)}
        cases.append({'original_u':u,'n_bit_length':N.bit_length(),
                      'odd_weight_rows':len(positions),'mod4_residue_counts':counts,
                      'content_zero_witnesses':witnesses,
                      'contact_residues':data['selected_contact_residues']})
    result={'personally_authored':True,'network_and_credentials_denied':True,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'algorithm':'Independently checked selected-row finite Schur completion.',
            'cases':cases,'seconds':round(time.monotonic()-started,3),
            'scope':'Finite original u0,1,2: every singleton bit and pairs among '
                    'the lowest32 allowed bits, restricted to j<b. Other rows '
                    'and infinite original indices are not inferred.'}
    (ROOT/'binary_actual_sparse_lucas_mask_certificate.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print(json.dumps({'seconds':result['seconds'],'cases':[
        {k:v for k,v in c.items() if k!='contact_residues'} for c in cases]}),flush=True)

if __name__=='__main__':main()
