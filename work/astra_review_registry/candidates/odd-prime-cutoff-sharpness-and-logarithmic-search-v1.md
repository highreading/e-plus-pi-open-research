> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Infinite sharpness and a logarithmic search interval for odd-prime individual-summand cutoffs

Status: UNVERIFIED CANDIDATE
Author: worker_4
Content SHA256: cb90914afe3b69d4f1db4bbed7c007e1bb7eb0cb3ecf0abb6274cfe4971bbd93

UNREVIEWED AUTHOR CANDIDATE

Fix an odd prime p. For k≥0 define g(k)=k−v_p(k!), with g(0)=0. For integer precision d≥1 define J(d)=1+max{k≥0:g(k)<d} and K(d)=max(1,ceil((p−1)(d−1)/(p−2))). The maximum exists by the bounds proved below.

Scope and dependency. The reviewed candidate odd-prime-interpolation-tail-cutoff-v1, payload SHA-256 2757da21024783fba7cd9c881de89c14db59b114a26787209ef0e639b8130799, identifies J as the optimal uniform individual-summand block cutoff for the interpolation terms T_{b,c,r}(X)=(-1)^b (X)_{b+2c+r}(X)_{b+c}/(2^c b!c!), where (X)_m is the falling factorial and b,c,r are nonnegative integers. A block cutoff retains b+2c<pJ. Optimality includes derivative order r=0 and concerns coefficientwise divisibility on odd-prime residue disks. The arithmetic results below are proved independently; their interpretation as interpolation cutoffs uses that exact scoped theorem.

Claim 1: infinite sharpness. For every t≥0 put q=p^t and d_t=1+((p−2)q+1)/(p−1). Then d_t is an integer and J(d_t)=K(d_t)=p^t+1. In particular equality occurs at infinitely many distinct precisions.

Claim 2: logarithmic search interval. For d=1, J=K=1. For d≥2 set A=p−2, B=(p−1)(d−1), let L be the number of base-p digits of K−1, and put H=max(0,floor((B−(p−1)L)/A)). Then H+1≤J≤K and K−H≤ceil((p−1)L/A)+1. Thus testing g(k)<d for H≤k<K suffices to recover J, and 0≤K−J≤ceil((p−1)L/A)=O_p(log d).

Proof. Write s_p(k) for the base-p digit sum, including s_p(0)=0. Legendre's formula gives (p−1)g(k)=(p−2)k+s_p(k). For k≥1 this tends to infinity and is positive. Consequently at d=1 the only bad index is zero and J=K=1.

For d≥2, K=ceil(B/A). For k≥K we have Ak≥B and s_p(k)≥1, so (p−1)g(k)>B. Since g(k) is an integer, g(k)≥d. This proves J≤K without any monotonicity assumption on g.

For Claim 1, q≡1 modulo p−1 makes d_t integral. Since s_p(q)=1, g(q)=((p−2)q+1)/(p−1)=d_t−1. Therefore J(d_t)≥q+1. Direct substitution gives K(d_t)=ceil(q+1/(p−2))=q+1. The preceding sufficiency bound proves equality. The sequence d_t is strictly increasing and unbounded.

For Claim 2, put C=(p−1)L. Because C≥1, floor((B−C)/A)≤ceil(B/A)−1=K−1; also K≥2, so H≤K−1. If H>0, it has at most L base-p digits. Thus s_p(H)≤C and AH+C≤B, giving g(H)≤d−1. If H=0, it is bad since g(0)=0<d. Hence the last bad index lies in [H,K−1], proving H+1≤J≤K. For real x,y, ceil(x)−floor(x−y)≤ceil(y)+1. Apply this with x=B/A and y=C/A. Replacing a negative floor by zero only shortens the interval, so K−H≤ceil(C/A)+1. Subtracting H+1≤J gives the asserted gap bound. Since K=O_p(d) and L=O_p(log d), the search interval has logarithmic length for fixed p.

Sharpness witness. The obstruction in Claim 1 is an actual interpolation summand. Choose r=c=0 and b=pq. Up to sign it is (X)_{pq}^2/(pq)!. On each residue disk X=a+pY, 0≤a<p, exactly q linear factors in (X)_{pq} have Gauss valuation one: their constant terms are divisible by p and their Y coefficients equal p. Every other factor has Gauss valuation zero. Multiplicativity of Gauss valuation gives v_G((X)_{pq})=q. As v_p((pq)!)=q+v_p(q!), the summand has exact Gauss valuation q−v_p(q!)=g(q)=d_t−1. Every smaller block cutoff omits it. At index zero, the witness b=c=r=0 is the constant polynomial 1, of valuation zero.

Evidence paths: work/astra_20260929/worker_4/note_000030.md and note_000031.md contain the original derivations; note_000032.md records successful arithmetic checks for p=3,5,7,11,13 and d=1,…,1000. The dependent interpolation candidate is work/astra_review_registry/candidates/odd-prime-interpolation-tail-cutoff-v1.md.

Self-audit and limitations. No monotonicity of k−v_p(k!) is used. The d=1 boundary and zero-index witness are treated explicitly. Finite computations are supplementary, not proof of the quantified results. Independent approval of this new candidate remains pending. Neither claim establishes optimality after cancellation in the summed tail, optimality for a fixed positive derivative order, estimates for actual reduced denominators, or rationality or irrationality of e+pi.