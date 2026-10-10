"""Coordinator-written, bounded actual-seed moving-prime audit."""
from pathlib import Path
import hashlib, json, time

def primes_between(lo, hi):
    flags=[True]*(hi+1); flags[0]=flags[1]=False
    for k in range(2,int(hi**0.5)+1):
        if flags[k]:
            for v in range(k*k,hi+1,k): flags[v]=False
    return [k for k in range(lo+1,hi+1) if flags[k]]

def clipped(v,p):
    if v==0: return 4
    e=0
    while v%p==0:
        v//=p;e+=1
    return e

def run():
    start=time.monotonic();n=225;t=3375
    primes=primes_between(t+2,5000)
    assert len(primes)<=250
    records=[]; A=1;L=1; initial=1;terminal=1;steps=0
    for p in primes:
        modulus=p**4; inv2=pow(2,-1,modulus)
        P,Q,F=0,10,-66%modulus;u,v=2,4
        overlaps=[];positions=[];depth_n=depth_t=None;previous=None
        for k in range(2,t+1):
            depth=min(clipped(F,p),clipped((Q*u-P*v)%modulus,p))
            assert any(z%p for z in (P,Q,F)) and (u%p or v%p)
            if k==n: depth_n=depth
            if k==t: depth_t=depth
            if n<=k<=t and depth: positions.append([k,depth])
            if k>n:
                shared=min(previous,depth)
                if shared:
                    root=(2*(k-1)+3)*((k-1)**2+8*(k-1)+11)
                    assert shared==1 and root%p==0
                    overlaps.append([k-1,shared])
            if k>=n: previous=depth
            if k==t: break
            m=k+1;N=k+2;ak=k*k+3*k+1;bk=2*k+3
            invm=pow(m,-1,modulus); invN=pow(N,-1,modulus)
            Pn=(m*N*Q+N*F*inv2)%modulus
            Qn=(N*P-ak*Q-k*N*F*inv2*invm)%modulus
            Fn=(-N*bk*P+N*ak*Q+N*(k*k-2)*F*inv2*invm)%modulus
            un=v;vn=(m*u+bk*v)*invN%modulus
            if n<=k<t:
                entrance_L=-2*m*bk*P+2*m*ak*Q+(k*k-2)*F
                entrance_E=(2*m*N*P*v-2*m**3*Q*u
                            -2*m*(3*k*k+8*k+4)*Q*v
                            -(m*m*u+(3*k*k+7*k+3)*v)*F)
                assert (entrance_L-2*m*invN*Fn)%modulus==0
                assert (entrance_E-2*m*(Qn*un-Pn*vn))%modulus==0
            P,Q,F,u,v=Pn,Qn,Fn,un,vn;steps+=1
        assert len(overlaps)<=3
        assert not any(positions[i][0]+1==positions[i+1][0]
                       and positions[i+1][0]+1==positions[i+2][0]
                       for i in range(max(0,len(positions)-2)))
        initial*=p**depth_n;terminal*=p**depth_t
        A*=p**max(depth_t-depth_n,0);L*=p**max(depth_n-depth_t,0)
        records.append({'prime':p,'initial_depth_clipped4':depth_n,
                        'terminal_depth_clipped4':depth_t,'overlaps':overlaps,
                        'positive_positions':positions,
                        'unresolved_depths_ge4':[x for x in positions if x[1]==4]})
    assert terminal*L==initial*A
    result={'authorship':'Coordinator; no remote-authored code executed',
            'scope':'One original 15-power block; primes3377<p<=5000; depths clipped at4',
            'n':n,'t':t,'prime_count':len(primes),'recurrence_steps':steps,
            'seed_moments':[0,10,-66],'seed_reference':[2,4],
            'acquisition_clipped4':str(A),'terminal_loss_clipped4':str(L),
            'initial_inventory_clipped4':str(initial),'terminal_inventory_clipped4':str(terminal),
            'identity_verified':True,'records':records,
            'seconds':round(time.monotonic()-start,3),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (Path(__file__).resolve().parent/'endpoint_actual_temporal_repulsion_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'prime_count':len(primes),'recurrence_steps':steps,
        'overlap_positions':sum(len(x['overlaps']) for x in records),
        'positive_positions':sum(len(x['positive_positions']) for x in records),
        'initial_nonzero_primes':[x['prime'] for x in records if x['initial_depth_clipped4']],
        'terminal_nonzero_primes':[x['prime'] for x in records if x['terminal_depth_clipped4']],
        'seconds':result['seconds']}))

if __name__=='__main__':run()
