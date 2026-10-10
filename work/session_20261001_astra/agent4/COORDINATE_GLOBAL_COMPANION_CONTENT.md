> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Global companion content for eligible positive coordinates

Status: new exact paper arithmetic. This note preserves the completed logarithmic-depth theorem and saddle review without repeating their proofs or computations. No prime scan or numerical experiment is used.

## 1. Domain and the global question

Fix b=3, the eligibility weight parameter m=1, and n=13^(s+1)+3, s>=5. Use the retained nonempty rational eligible set of positive coordinates j in {1,2,3}. The construction below actually works whenever the retained coordinate lift exists and X_j is nonzero, but every approximation-related assertion here retains this stated eligible domain.

Write F=(n!)^2, Q(t)=1-2t+2t^2, and

C_j=a_j adj(M)diag(1,n+1,(n+1)(n+2)).

Regard C_j as a column of three coefficients when applying the integer matrices below. Define

K_j(t)=t^n D^n[Q(t)^n C_j(t)]/n!.

The retained exact identities are

X_j=K_j(1),
R_j:=L_j/F=calL((K_j-X_j)/(t-1)).

Here calL(P)=integral from -1 to 1 of P((1+iu)/2) du. The actual companion is gamma_j=R_j/X_j, and

B_j=F|X_j|/gcd(F|X_j|,|L_j|).

No prime is discarded. There is no coordinate-zero correction in these positive rows. Nothing below is transferred to a Gram center.

The result will isolate a common rational factor of the pair (X_j,R_j) by reducing a universal two-by-three integer map. This permits cancellation arising from the effective two-dimensional image even when it is not coefficient content of C_j or K_j.

## 2. An odd global moment clearer

Put N=2n+2 and O=lcm of the odd positive integers at most N. For i=0,1,2 define

K_i(t)=t^n D^n[Q(t)^n t^i]/n!,
U_i=K_i(1),
R_i=calL((K_i-U_i)/(t-1)),
J_i=O R_i.

All U_i and J_i are integers. The nontrivial point is that no power of two is needed in O, even though the individual moments have powers of two in their denominators.

Proof. Write K_i=sum_d k_(i,d)t^d. Its coefficient is

k_(i,d)=binom(d,n)[t^(d-i)]Q(t)^n,

and is zero for d<n. Each coefficient of Q^n of degree l has dyadic valuation at least ceil(l/2), so

v_2(k_(i,d))>=ceil((d-2)/2).

For k>=1, the coefficient A_(i,k) of t^(k-1) in (K_i-U_i)/(t-1) is sum_(d>=k) k_(i,d). Thus

v_2(A_(i,k))>=ceil((max(n,k)-2)/2)

whenever the sum is nonzero. The exact moment

mu_(k-1)=((1+i)^k-(1-i)^k)/(i 2^(k-1) k)

satisfies v_2(mu_(k-1))>=1-floor(k/2), with zero moments allowed. Therefore every A_(i,k)mu_(k-1) is dyadically integral: using max(n,k)>=k gives a lower bound of zero for even k and one for odd k. At an odd prime, the denominator of the moment divides the odd part of k. Since k<=N, multiplication by O clears it. This proves J_i is integral.

Consequently

X_j=sum_i U_i(C_j)_i,
O R_j=sum_i J_i(C_j)_i.

In particular the exact original factorial formula is equivalently

B_j=O|X_j|/gcd(O|X_j|,|sum_i J_i(C_j)_i|).             (1)

This identity removes the factorial scale globally. It does not assume that O is the least possible clearer.

The universal entries are completely explicit finite integer sums. For example, set

q_l=[t^l]Q(t)^n
=sum_(a+b+c=n, b+2c=l) n!/(a!b!c!) (-2)^b 2^c.

Then k_(i,d)=binom(d,n)q_(d-i), U_i=sum_d k_(i,d), and

J_i=sum_(k=1)^N O mu_(k-1) sum_(d>=k) k_(i,d).

Individual summands in this last expression are rational as written; the preceding valuation argument proves that each full product O mu_(k-1) A_(i,k) is integral. One must not reduce O mu_(k-1) alone modulo a dyadic modulus before its coefficient is included.

## 3. An exhaustive universal rank test

Define the integer matrix

Z=[[O U_0,O U_1,O U_2],[J_0,J_1,J_2]].

Its first row is nonzero because U_0=[x^n](1+2x+2x^2)^n>0. Thus its rank is either one or two. No assertion selecting either rank is needed for the exhaustive result below.

Define the three explicit integers

D_(ik)=O(U_i J_k-U_k J_i), 0<=i<k<=2.

If at least one is nonzero, use the rank-two reduction in Sections 4–7. If all vanish, use the rank-one conclusion in Section 8. These entries and minors are defined by the finite sums in Section 2; no contact solve or numerical rank inference is involved. No computation of this rank test is claimed here.

Both alternatives give exact global denominator descriptions and deterministic bounds. The effective-content rate reduction in Section 5 applies in the rank-two branch; the rank-one branch already has an exponential denominator bound.

## 4. Universal integer reduction and the new common rational factor

Suppose Z has rank two. Let g_U=gcd(U_0,U_1,U_2)>0. Extended Euclidean operations give H_1 in GL_3(Z) with

(U_0,U_1,U_2)H_1=(g_U,0,0).

Write (J_0,J_1,J_2)H_1=(a,b,c). Rank two means (b,c)!=(0,0). Integer operations on the last two columns give a further unimodular matrix H_2, preserving the first column and first row, such that

Z H_1 H_2=[[g,0,0],[a,t,0]],
g=O g_U>0, t=gcd(b,c)>0.

Put H=H_1 H_2 and z=H^(-1)C_j. All coordinates of z are integers. The third coordinate is in the exact kernel of both endpoint and logarithmic functionals, so it contributes neither X_j nor R_j.

Let

d=gcd(g,a,t)>0,
g'=g/d, a'=a/d, t'=t/d,
r_j=gcd(|z_0|,|z_1|)>0,
u_j=z_0/r_j, v_j=z_1/r_j.

Because X_j!=0, z_0 and u_j are nonzero; gcd(|u_j|,|v_j|)=1. Then the pair of rational numbers factors exactly as

(X_j,R_j)=(d r_j/O)(g' u_j, a' u_j+t' v_j).           (2)

This is the requested common rational factor. It incorporates the effective image content r_j; a large third, kernel coordinate does not obstruct this cancellation. In particular r_j need not equal the content of C_j. Since H is unimodular, content(C_j)=gcd(z_0,z_1,z_2), which divides r_j, but equality need not hold.

Define the universal integer

D=gt/d^2.

It has the invariant expression

D=gcd(|D_(01)|,|D_(02)|,|D_(12)|)/d^2,
d=gcd(all six entries of Z).

Thus neither d nor D depends on the particular Euclidean choices. Define

e_j=gcd(g'|u_j|,|a'u_j+t'v_j|).

Then

e_j divides D,
B_j=g'|u_j|/e_j.                                    (3)

Proof of the divisibility. The two-by-two matrix W=[[g',0],[a',t']] has determinant D. Multiplication by adj(W) shows that e_j divides D u_j and D v_j. Their primitive gcd is one, so e_j divides D. This proof includes a zero logarithmic numerator.

Consequently the remaining exact gcd may be written as the bounded universal-modulus calculation

e_j=gcd(D,g'u_j,a'u_j+t'v_j).                        (4)

Equations (2)–(4) are an exact global content factorization. They replace a gcd involving the raw factorial contractions by effective coordinate content r_j and a residual gcd that divides an explicit universal determinantal content.

## 5. Deterministic bounds and the remaining rate

The universal modulus has only exponential size in n. To see this without evaluating its entries, put M_0=4*20^n. Since ||Q^n t^i||_1=5^n and binom(d,n)<=2^(2n+2),

||K_i||_1<=M_0, |U_i|<=M_0.

On the integration segment |t|<=1, so |mu_(k-1)|<=2. It follows that

|R_i|<=2N M_0, |J_i|<=2N O M_0.

Write H_0=2N O M_0. Every entry of Z has absolute value at most H_0. Thus

D<=2H_0^2,
g'<=O M_0.

The elementary lcm bound O<=lcm(1,...,N)<=4^N shows that log D and log g' are O(n), with explicit constants available from these displayed inequalities. Therefore (3) gives the deterministic interval

|u_j|/(2H_0^2)<=B_j<=O M_0 |u_j|,                   (5)

and the stronger exact bounds

g'|u_j|/D<=B_j<=g'|u_j|.

In particular

log B_j=log|u_j|+O(n)
       =log|X_j|-log r_j+O(n),                      (6)

uniformly in the three positive coordinates whenever the rank-two branch holds. The second equality uses X_j=g_U r_j u_j and 1<=g_U<=M_0.

This identifies the factorial-scale rate obstruction precisely: it is the effective coordinate quotient |X_j|/r_j, up to exponential factors. In particular

log B_j=o(n log n) if and only if log|u_j|=o(n log n).

No estimate on r_j large enough to prove this condition for the actual adjugate rows is supplied here. Thus (5) is a deterministic global bound and (6) is an exact rate reduction, not a proof of a favorable numerical growth exponent for this family.

## 6. Every prime and its actual lifting precision

All prime conditions now involve W and the primitive effective pair (u_j,v_j). For a prime p put

A=v_p(g'), T=v_p(t'), k=v_p(D)=A+T,
x=v_p(u_j), y=v_p(a'u_j+t'v_j).

Use v_p(0)=infinity. Then exactly

v_p(e_j)=min(A+x,y),
v_p(B_j)=A+x-min(A+x,y),
min(A+x,y)<=k.                                     (7)

For p not dividing D, no residual cancellation is possible: v_p(B_j)=v_p(u_j), because g' divides D and is also a unit. No assertion is made that u_j is a unit.

For p dividing D, determination of e_j needs the two integers g'u_j and a'u_j+t'v_j only modulo p^k. If both vanish modulo p^k, the exponent of e_j is exactly k because e_j divides D. Otherwise its first nonzero level below k determines the minimum. The exponent of u_j is retained separately to obtain the denominator exponent in (7).

In particular the condition v_p(e_j)>=ell, for 1<=ell<=k, is exactly the pair of congruences

g'u_j=0 mod p^ell,
a'u_j+t'v_j=0 mod p^ell.                            (8)

There is no need for factorial-depth lifting once the image content has been removed. There is, however, a real cost in computing r_j before removing it. If v_p(r_j)=r_p, primitive effective coordinates modulo p^k require z_0,z_1 modulo p^(r_p+k), followed by exact division by p^r_p and by the prime-to-p part of r_j. Certifying r_p from modular data requires observing a nonzero coordinate at precision p^(r_p+1). A residue computation only modulo p cannot replace these requirements.

An equivalent direct moment precision statement, useful before the integer reduction, is as follows. Write o_p=v_p(O), X-depth x_p=v_p(X_j), and J_j=sum_i J_i(C_j)_i. To decide complete p-cancellation in (1) requires J_j modulo p^(o_p+x_p); to certify its exact valuation at that threshold or above requires one further digit if that exact valuation is wanted. Below the threshold its first nonzero digit determines the denominator exponent. For odd p the moment terms can be grouped by v_p(k), but at precision p^ell every group whose scaled valuation is less than ell must be retained. The top layer alone is not a global lift.

The dyadic conditions in (7)–(8) use the integral J_i established in Section 2, and therefore require no invalid division by even moment denominators.

## 7. Relation to the completed 13-adic result

The completed theorem supplies v_13(B_j)=s+1. It is retained, not reproved. In the new global representation this imposes the exact consistency condition

v_13(g')+v_13(u_j)-v_13(e_j)=s+1.

The content factorization does not assume the other primes are units, and (7)–(8) give their full remaining conditions. The global factor d r_j/O is generally rational; treating it as an integer divisor would lose the normalization in (2).

## 8. Exhaustive rank-one branch

If all three minors D_(ik) vanish, the nonzero first row implies that R is a rational multiple of evaluation on the entire three-dimensional selector space. After H_1, necessarily b=c=0. Hence

Z H_1=[[g,0,0],[a,0,0]],
B_j=g/gcd(g,|a|)

for every defined positive coordinate, independently of C_j. This includes a=0, when B_j=1. In particular B_j<=g<=O M_0 and log B_j=O(n).

This branch is not claimed to occur. Its inclusion makes the global conclusion exhaustive without an unproved rank assertion or an additional computation. It also means that a universal rank test is sufficient to decide which explicit reduction to use; no large contact solve is required.

## 9. What has and has not been obtained

New results are the odd moment clearer, the universal two-by-three integer image, the common rational factor (2), the universal residual divisor e_j|D, the exact effective-gcd rate reduction (6), and all-prime lifting conditions with precision loss from removing r_j explicitly retained. The rank-one alternative is handled separately and completely.

The remaining substantive arithmetic problem in the rank-two case is to bound r_j relative to X_j for the actual adjugate selector. An exponential bound for D does not bound the actual effective coordinate u_j. No favorable global companion exponent, shrinking pair of primitive forms, or conclusion about e+pi follows without that further control. All results retain positive-coordinate eligibility and complete global cancellation.
