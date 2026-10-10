> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The n+2 boundary: a two-source kernel and complete denominator chart

New author mathematics, 2026-10-02, target L5. No independent review is asserted. This resolves the h=2 structural disk identified in GENERAL_BOUNDARY_KERNEL_CHART.md. Retain its exact normalized N,A,K,Omega,Y,D,V, the full kappa correction, and c=2^nV/((n!)²D)+beta.

Fix b,m in the canonical domain with

    b>m+3, 1<=m<=floor((b−1)/2), p>b,

and assume all endpoint digits P_r,0<=r<p, are p-units. Put u=n+2,k=v_p(u)>=1. The first condition is exactly the metric/kernel separation for this disk. The author theorem is

    D_n/(u²P_n²)=delta_(p,b,m,2) mod p,
    V_n/(u²P_n)=nu_(p,b,m,2) mod p,             (1)

at every nonnegative n=-2 modulo p and every depth k. Both quotients are p-integral; one reference n*=p²−2 determines their constants. A unit nu yields, for every normal n>=2p on this disk,

    v_p(q_n)=2v_p(n!)+v_p(D_n)−2k>=2v_p(n!).   (2)

For b5,m1, the new exact references at p7 and13 give (delta,nu)=(2,2),(12,6). These are finite inputs to the theorem, rather than higher-depth evidence for its proof. No whole b5 prime atlas or b5 error theorem is claimed.

## 1. The lower map and forced content

The lower rows are i=2,...,b−1. Write l=i−2 and d=b−2. Modulo u, their d x b contact matrix is

    T_lj=l![z^(l−j)] e^z/q0(z)^2, j<=l,
    T_lj=0, j>l,
    q0(z)=1−z+z²/2.                           (3)

Its first d columns T0 form a p-invertible triangle with diagonal l!, and its final TWO columns vanish. In ordinary coefficient coordinates, T0 acts by multiplication by e^z/q0(z)^2 followed by taking the first d coefficients, with row l scaled by l!.

All lower coordinates of D0J have u content. NY=Delta D0J consequently gives Y_j in uZ_(p) for j<d. The last two coordinates modulo p are a fixed vector times P_n, by all-residue transfer at the seed p−2; this vector need not be nonzero without further finite information. No full contact determinant is inverted.

At n=-2, K0=Z(I+Dpol)^2. Its image on the last two-coordinate subspace has no support below row b−4. The metric has support only through row m−1, which is strictly below b−4 by b>m+3. Thus x_j=(KY)_j has u content for j<=m−1. Every higher weight

    Omega_j=(u+m−1)_j², j>=m,

has u² content. This proves D in u²Z_(p).

## 2. Two backward factorial values and their annihilator

Keep both R2=Dcal_(2u−2) and R1=Dcal_(2u−1) at actual precision. They satisfy the recurrence R1=(2u−1)R2+1, but no higher-precision replacement by their first residues is made. Their first residues are Dcal_(p−2),Dcal_(p−1).

The lower A rows modulo u are given by Dcal_(l−2−s), with negative indices -2,-1 represented by R2,R1. Their coefficient generating function, through degree d−1, is

    sum_l Abar_l(R2,R1)z^l/l!
      =q0(z)^(-2)[R2+R1 z+integral_0^z (z−s)e^s/(1−s) ds].  (4)

Solving (3),(4), the lower coefficients B=adj(N)A equal Delta times the truncation of

    b_R(z)=e^(−z)[R2+R1 z+integral_0^z (z−s)e^s/(1−s) ds].  (5)

The exact formal identity is

    (I+partial_z)^2 b_R(z)=1/(1−z).            (6)

Hence t0=(KB)_0=-Delta and t_j=0 for1<=j<=b−5 modulo u. In particular this holds in every low metric row. In the complete numerator

    V=x0(t0+Delta)+sum_(j=1)^b Omega_j x_j t_j,               (7)

all terms have u² content. The kappa term supplies the +Delta cancellation in the first summand.

The two free backward directions in (5) are e^(−z) and z e^(−z). Both lie in the kernel of (I+partial_z)^2 in all available degrees. This handles the higher digits of R2,R1 without treating either as a locally constant sequence.

## 3. Uniform first-order precision and the depth1 correction

There are fixed p-residue matrices G and vectors F such that

    N_lower=T+u(G+epsilon T) mod p^(k+1),
    A_lower=Abar(R2,R1)+u(F+epsilon Abar(R2*,R1*)) mod p^(k+1), (8)

where (R2*,R1*) are the fixed first residues, epsilon=u/p modulo p for k=1 and epsilon=0 for k>=2. The argument works termwise. In row l, a falling factorial of length at least l+1 contains u; a length at least p+l+1 also contains u−p. The latter contribution vanishes modulo p^(k+1), or lies outside the finite range at u=p. Short coefficients have p-unit polynomial denominators, since l<b<p. All one-u terms need their remaining factors only modulo p.

Here n=u−2 and

    q0(z)^n=q0(z^p)^(u/p)/q0(z)^2 mod p.

The relevant degrees are below p+b−2<2p. At k>=2 the high factor contributes1. At k=1 the only extra coefficients are -epsilon[z^ell]q0(z)^(-2) in degree p+ell. Wilson's theorem gives

    (u+l)_(p+j+ell)/u=−(l)_(j+ell) mod p

when j+ell<=l. Thus N gets precisely the extra u epsilon T. For A the corresponding Dcal offsets modulo p are l−2−ell, so the extra term is u epsilon Abar(R2*,R1*). Positive short Dcal offsets are propagated from actual R1 by the recurrence; their first-order values depend only on R1 modulo p. This establishes (8).

Solving through T0 to first order, epsilon terms cancel because T0 sends Delta b_R to Delta Abar(R2,R1), whose difference from its first-residue specialization has an extra p factor. Higher R2,R1 digits cancel from low reconstruction by (6). Thus (t0+Delta)/u and t_j/u,1<=j<=m−1, modulo p are fixed at all depths. The last two B coordinates modulo p are fixed by seed transfer. Full N may be singular modulo p; the proof still uses only T0.

## 4. The carried endpoint lies in the same two-dimensional kernel

Write n=pa−2 and h_c=CT_z W0(z)^(a−1)z, W0=z^(-1)+2+2z. Frobenius gives

    J_i(n)=P_(a−1)J_i(p−2)+h_c c_i mod p,
    c_0=c_1=0,
    c_i=1/2 [y^(i−2)](1+y)^i/(1+y+y²/2)^2, i>=2.          (9)

The low Laurent interval contains0,p and no other multiple of p, because i<b<p. The baseline upper-edge coefficient is2^(p−2)=1/2 modulo p, and its following coefficients come from (1+y+y²/2)^(-2).

Since D0_i/u=−(i−2)! modulo p, the carried lower source in row l is -h_c l!c_(l+2). A binomial transform yields

    sum_(l>=0)c_(l+2)z^l=(1−z)/(2q0(z)^2).                 (10)

Indeed its left side is (1−z)^(-3)/2 times (1+z/(1−z)+(z/(1−z))²/2)^(-2). Comparing (3),(10), the lower solve maps the carried source to

    -h_c e^(−z)(1−z)/2.                                  (11)

This belongs to span{e^(−z),z e^(−z)} and is annihilated by (I+partial_z)^2. Thus it has no effect on any x_j/u seen by the low metric. The other first-order low Y terms involve G's last two columns times the fixed high Y vector, so they are fixed multiples of P_n. The epsilon correction has zero last two columns, and its low-coordinate action contains an extra u. As P_(p−2) is a p-unit, P_(a−1)=P_n/P_(p−2).

Consequently each x_j/u modulo p for j<=m−1 is a fixed multiple of P_n, while each high x_j modulo p is also a fixed multiple of P_n. The fixed constants are independent of the carry and k.

## 5. Normalized D,V and the actual complete beta

The low weights Omega_j modulo p and high weights Omega_j/u² modulo p are fixed. Section3 fixes the normalized low t terms; the high t coordinates modulo p are fixed. Substitution in D and (7) proves (1). Normalized constants can vanish, and this theorem does not silently identify 2k as the depth of D. If nu is a unit, it proves v_p(V)=2k while retaining v_p(D)>=2k, possibly strictly greater.

HY=K^TOmega x has u content. Hence every coefficient of zhat=D0 adj(N)^THY has u content, as does the canonical Rodrigues polynomial. The complete logarithmic difference K_zhat−D has u content, and division by its exact monic factor t−1 preserves it. The moment transformation has only p-unit powers of2 in its coefficient denominators; integration costs at most floor(log_p(2n+b−1)). Therefore

    v_p(beta)>=k−v_p(D)−floor(log_p(2n+b−1)).               (12)

For a0=floor(n/p)>=2, one has n+2<(a0+2)p<p^a0 and2n+b−1<p(2a0+3)<p^(a0+1). Thus k<=a0−1, the logarithmic floor is<=a0, and2v_p(n!)−k>=a0+1. The factorial term's valuation2k−2v_p(n!)−v_p(D) is strictly smaller than (12). The complete rational sum has this smaller valuation, proving (2) for actual q with its final evaluated gcd.

## 6. Exact finite references and scope

h2_boundary_probe.json retains only13 new bounded states chosen to test the distinct two-source mechanism: p7,13, unit multipliers1,2,3 at depths1,2, and one depth3 state at p7. They motivated and support the derivation; they are not its all-depth proof.

H2_BOUNDARY_REFERENCE_CERTIFICATE.json retains the exact references n47 and167 modulo p^5, endpoint unit receipts and source hashes. For b5,m1 its constants are

|p|n*|delta|nu|
|---:|---:|---:|---:|
|7|47|2|2|
|13|167|12|6|

Only the unit nu and endpoint digits are finite inputs to (1),(2). No broad prime scan or full b5 residue criterion has been executed. In particular these local results do not by themselves provide a global denominator rate or pair with an unproved b5 signed error.
