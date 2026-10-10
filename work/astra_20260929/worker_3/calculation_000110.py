from pathlib import Path
import hashlib, math
base=Path('[private local path removed]')
p=base/'work/astra_review_registry/candidates/worker1-b2-five-adic-residue-one-form-growth-v1.md'
b=p.read_bytes()
start=b.index(b'Status: UNREVIEWED candidate by worker_1.')
payload=b[start:]
h=hashlib.sha256(payload).hexdigest()
assert h=='b67f9a7d1027f0019f1f0bcd6599e582cec92ae9858195b9a7959044d4435bd8'
def digits(n,p):
    s=0
    while n:
        n,r=divmod(n,p)
        s+=r
    return s
def vf(n,p):
    s=0
    while n:
        n//=p
        s+=n
    return s
count=0
for n in range(6,20001,5):
    s3,s5=digits(n,3),digits(n,5)
    assert 2*vf(n,3)==n-s3
    assert 4*vf(n,5)==n-s5
    assert 3**(2*s3)*5**s5 <= 225**2*n**8
    assert n>=({0:3,1:4,2:5}[n%3])
    count+=1
print({'file_bytes':len(b),'file_sha256':hashlib.sha256(b).hexdigest(),'payload_offset':start,'payload_bytes':len(payload),'payload_sha256':h,'progression_indices_checked':count,'beta':3*math.sqrt(5)/(1+math.sqrt(2))**2,'log_beta':math.log(3*math.sqrt(5))-2*math.log(1+math.sqrt(2))})