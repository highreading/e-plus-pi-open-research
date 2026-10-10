"""ONE new higher-precision raw-source diagnostic, coordinator authored.
No old mod4/mod8 receipt is rerun. Inputs d112/all contact columns, base0..3,
jet0..8; whole raw numerators are divided by passed complete integer factors.
Independent actual theta recurrence also checks the new rational formula16.
"""
from pathlib import Path
import hashlib, json, math, time
HERE=Path(__file__).resolve().parent
OUT=HERE/'THETA_RATIONAL_MOD16_RAW_TOP_AUXILIARY_RECEIPT.json'
assert not OUT.exists()
start=time.monotonic()
D,AMAX,JMAX=112,3,8
assert D%32==16 and AMAX+JMAX<D

def product(a):
    v=1
    for x in a:v*=x
    return v

# Actual raw recurrence through the unchanged auxiliary physical terminal.
aa=[1]
for n in range(1,2*(3*D+1)+1):aa.append(1-n*aa[-1])
u=aa[::2]
dif=[u]
for r in range(D):dif.append([b-a for a,b in zip(dif[-1],dif[-1][1:])])
theta=[1,0]
for n in range(1,4*D+20):theta.append((2*n+1)*theta[-1]+theta[-2])
checks=0
for r in range(D+1):
    den=(1<<r)*math.factorial(r)
    q,rem=divmod(dif[r][0],den)
    assert rem==0 and q==theta[r]
    checks+=1

def inverse_polynomial(a,length,modulus):
    s=[pow(a[0],-1,modulus)]
    for n in range(1,length):
        s.append(-s[0]*sum(a[j]*s[n-j] for j in range(1,min(n,len(a)-1)+1))%modulus)
    return s
def convolution(a,b,length,modulus):
    return [sum(a[i]*b[n-i] for i in range(max(0,n-len(b)+1),min(n,len(a)-1)+1))%modulus for n in range(length)]
LEN=256
inv=inverse_polynomial([1,1,1],LEN,16)
powers={1:inv}
for p in range(2,8):powers[p]=convolution(powers[p-1],inv,LEN,16)
parts=[(1,[1,1],1),(2,[0,0,1,-1],3),
       (4,[0,0,0,3,-3,-4,2,-1],5),
       (8,[0,0,0,0,0,1,0,1,1,0,1,1],7)]
f=[0]*LEN
for weight,num,p in parts:
    s=convolution(num,powers[p],LEN,16)
    f=[(x+weight*y)%16 for x,y in zip(f,s)]
assert f==[x%16 for x in theta[:LEN]]

def krow(j):
    return [sum(math.comb(D,t)*math.comb(r+j+t,r)*theta[r+j+t]
                for t in range(D+1))%16 for r in range(D+1)]
ks=[krow(j) for j in range(JMAX+3)]
pd=[product(2*x+2*h+1 for h in range(D)) for x in range(AMAX+JMAX+D+1)]
bin_d=[(-1)**(D-h)*math.comb(D,h) for h in range(D+1)]
raw=[[sum(bin_d[h]*pd[x+h]*dif[r][x+h] for h in range(D+1))
      for x in range(AMAX+JMAX+1)] for r in range(D+1)]
topchecks=0
for a in range(AMAX+1):
    for j in range(JMAX+1):
        for r in range(D+1):
            numerator=sum((-1)**(j-t)*math.comb(j,t)*raw[r][a+t] for t in range(j+1))
            # Complete norm 2^alpha D_r *2^j R_j *o_d simplifies to this.
            denominator=(1<<(D+r+j))*math.factorial(r)*math.factorial(D+j)
            value,rem=divmod(numerator,denominator)
            assert rem==0
            expected=(ks[j][r]+2*a*(j+1)*ks[j+1][r]
                      +4*math.comb(a,2)*(j+1)*(j+2)*ks[j+2][r])%16
            assert value%16==expected,(a,j,r,value%16,expected)
            topchecks+=1
atomchecks=0
for a in range(AMAX+1):
    for j in range(JMAX+1):
        aw=[]
        for x in range(a,a+j+1):
            val=sum(bin_d[h]*pd[x+h]*(-1)**(x+h) for h in range(D+1))
            q,rem=divmod(val,1<<D)
            assert rem==0
            aw.append(q)
        val=sum((-1)**(j-t)*math.comb(j,t)*aw[t] for t in range(j+1))
        q,rem=divmod(val,1<<j)
        assert rem==0 and q%16==(-1)**(a+j)%16
        atomchecks+=1
receipt={'scope':'NEW auxiliary d112 actual RAW complete top/atom modulo16 and rational theta coefficients16; not original indices, bottom/whole matrix upper or e+pi proof.',
         'd':D,'bases':[0,AMAX],'jets':[0,JMAX],'contact_columns':[0,D],
         'full_raw_divisions_paid':True,'raw_contact_normalizations_checked':checks,
         'rational_mod16_coefficients_checked':LEN,'raw_top_coordinates_checked':topchecks,
         'raw_atom_coordinates_checked':atomchecks,'failures':0,
         'network_and_credentials_denied_by_sandbox':True,
         'seconds':round(time.monotonic()-start,3),
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
OUT.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
