> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A finite kernel chart for every structurally null negative residue

New author mathematics, 2026-10-02, target L6. No independent review is asserted. This extends the separately derived h1/h2 author charts by resolving their common finite coefficient problem. Use the exact canonical fixed-b,m normalized definitions in GENERAL_FIXED_B_ODD_ORIGIN.md, including V=Y^TH adj(N)A+det(N)(KY)_0 and c=2^nV/((n!)²D)+beta.

Fix b>=4, 1<=m<=floor((b−1)/2), p>b. Let

    1<=h<=min(m+1,b−m−2), u=n+h, k=v_p(u)>=1.

These h are precisely the metric-null negative disks already proved by triangular contact support. Assume every endpoint digit P_r,0<=r<p, is a p-unit. The new author statement is that fixed constants delta_(p,b,m,h),nu_(p,b,m,h) obey

    D_n/(u²P_n²)=delta_(p,b,m,h) mod p,
    V_n/(u²P_n)=nu_(p,b,m,h) mod p               (1)

at every n=-h modulo p and every depth k. Both quotients are p-integral. A single reference n=p²−h modulo p^5 determines them. A unit nu supplies, for every normal n>=2p in that disk,

    v_p(q_n)=2v_p(n!)+v_p(D_n)−2k>=2v_p(n!).   (2)

D can have deeper raw content if delta vanishes; no exact depth for D is presumed. Full beta and the final rational gcd are included in (2).

## 1. One contact transform, with an h-dimensional unknown subspace

Put d=b−h, M=m+1−h>=0. Lower row i=h+l,0<=l<d, has modulo-u contact map

    T_lj=l![z^(l−j)] e^z/q0(z)^h, j<=l,
    T_lj=0, j>l.                               (3)

The first d columns T0 form a p-invertible triangle with diagonal l!, while the final h columns vanish. Its coefficient form is

    (Tv)_l/l!=[z^l](e^z v(z)/q0(z)^h).

All lower coordinates of D0J have u content; NY=Delta D0J gives Y_j in uZ_(p) for j<d. Its last h coordinates modulo p are a fixed vector times P_n by all-residue seed transfer at p−h. Their possible vanishing is retained.

At n=-h, K0=Z(I+Dpol)^h. Acting on the last h-coordinate subspace, it has support only in rows>=b−2h. The metric Omega_j=(u+M)_j² has low support j<=M and u² content in every higher row. The strict separation M<b−2h follows from h<=b−m−2. Hence every low x_j=(KY)_j has u content and D has u² content.

## 2. The backward values span e^(−z)Pol_(h−1)

Keep the actual values R_j=Dcal_(2u−j),1<=j<=h. Write the formal polynomial

    R(z)=sum_(l=0)^(h−1) R_(h−l) z^l/l!.

These h symbols are recurrence-related, but the argument cancels their larger h-dimensional ambiguity and does not need to replace their higher digits. Each first residue is fixed as R_j*=Dcal_(p−j).

Define the h-fold formal antiderivative

    I_h(z)=integral_0^z (z−s)^(h−1)/(h−1)! · e^s/(1−s) ds.

Then the lower A-row generating function and its triangular solution are

    sum_l Abar_l(R)z^l/l!=q0(z)^(-h)[R(z)+I_h(z)],
    B_lower/Delta = coefficients of b_R(z)=e^(−z)[R(z)+I_h(z)]
                   through degree d−1.                      (4)

Since I_h^(h)=e^z/(1−z), the decisive identity is

    (I+partial_z)^h b_R(z)=1/(1−z).             (5)

The low reconstructed coordinates of B are therefore t0=-Delta and t_j=0 for1<=j<=b−2h−1 modulo u. This includes all j<=M. Thus the complete corrected numerator

    V=x0(t0+Delta)+sum_(j=1)^b Omega_j x_j t_j

has u² content. Its full correction is required in the first summand.

Changing the backward values changes b_R by e^(−z) times a polynomial of degree at most h−1. This entire subspace is killed by (I+partial_z)^h, so arbitrary higher backward digits do not enter the normalized low t residues.

## 3. All-depth first-order expansion

The same explicit precision argument as in H2_MULTIPLE_SOURCE_BOUNDARY_CHART.md now applies with l=i−h. There are fixed p-residue G,F such that

    N_lower=T+u(G+epsilon T) mod p^(k+1),
    A_lower=Abar(R)+u(F+epsilon Abar(R*)) mod p^(k+1),       (6)

where epsilon=u/p modulo p at k=1, and epsilon=0 at k>=2.

A falling factorial in row l contains u once its length is at least l+1, and contains u−p once its length is at least p+l+1. Thus all two-factor tails vanish to precision p^(k+1), or are outside the finite range when u=p. The short coefficients have p-unit polynomial denominators because l<b<p. For the remaining one-u window, only coefficients modulo p matter, and

    q0(z)^(u−h)=q0(z^p)^(u/p)/q0(z)^h mod p.

This window lies below p+b−h<2p. At depth1, the sole extra block is -epsilon[z^ell]q0(z)^(-h) in degree p+ell. Wilson gives

    (u+l)_(p+j+ell)/u=−(l)_(j+ell) mod p

whenever j+ell<=l. Summing gives epsilon T. The analogous A sum sees offsets l−h−ell modulo p; its negative offsets use the fixed R_j*, and its nonnegative offsets use Dcal of that fixed small index. This gives epsilon Abar(R*). Positive short Dcal offsets follow from the actual R1 via the recurrence and need only R1 modulo p in their first-order correction. This proves (6).

In the lower B solve, epsilon terms cancel since T0 sends Delta b_R to Delta Abar(R), and Abar(R)−Abar(R*) has an extra p factor. The last h columns of T are zero. Higher R digits vanish under (5). Therefore (t0+Delta)/u and t_j/u,1<=j<=M, modulo p are fixed at every depth. The high B coordinates modulo p are fixed by seed transfer. Only T0 is inverted, even if p divides Delta.

## 4. The endpoint carry is a vector in the same h-dimensional kernel

Write n=pa−h, s=P_(a−1), eta=CT_z W0(z)^(a−1)z, W0=z^(-1)+2+2z. The low Laurent interval[-p+h,p−h+i] contains0 and possibly p, with no other multiple of p. Frobenius and the upper-edge expansion give

    J_i(n)=sJ_i(p−h)+eta c_i mod p,
    c_i=0 for i<h,
    c_i=2^(1−h)[y^(i−h)](1+y)^i/(1+y+y²/2)^h for i>=h.   (7)

The baseline upper-edge coefficient is2^(p−h)=2^(1−h) modulo p. Its next coefficients through degree b−h−1 are those of (1+y+y²/2)^(-h); all relevant degrees are below p.

For l=i−h, D0_i/u=(-1)^(h−1)(h−1)!l! modulo p. The shifted binomial transform is

    sum_(l>=0)c_(l+h)z^l
       =2^(1−h)(1−z)^(-h−1)
                    (1+z/(1−z)+(z/(1−z))²/2)^(-h)
       =2^(1−h)(1−z)^(h−1)/q0(z)^h.                       (8)

Combining (3),(8), the carried lower source pulls back to the coefficient vector of

    eta (-1)^(h−1)(h−1)!2^(1−h) e^(−z)(1−z)^(h−1).       (9)

This lies in e^(−z)Pol_(h−1), the same subspace as the backward ambiguity, and is annihilated by (I+partial_z)^h. It does not affect x_j/u in any low metric coordinate.

Every other first-order low Y contribution is a fixed multiple of the fixed high Y vector, hence of P_n. The depth1 epsilon term has no last-h-column part, and its low-column action has extra u content. Since P_(p−h) is a unit, s=P_n/P_(p−h). Thus all low x_j/u residues are fixed multiples of P_n, while high x_j residues are fixed multiples of P_n. This is independent of eta, k and u/p.

## 5. Contraction, complete beta and actual q

Low Omega_j modulo p and high Omega_j/u² modulo p are fixed:

    Omega_j/u²=[M!(−1)^(j−M−1)(j−M−1)!]², j>M.

All factors are p-units because j<=b<p. The normalized low t residues and high t residues are fixed, so substitution proves (1). A reference with u=p² determines the normalized coefficients modulo p using D,V modulo p^5.

As in the h1/h2 notes, HY=K^TOmega x has u content. Therefore zhat=D0 adj(N)^THY, its Rodrigues polynomial, and the exact logarithmic difference quotient have u content. The canonical complete moment companion satisfies

    v_p(beta)>=k−v_p(D)−floor(log_p(2n+b−1)).               (10)

When nu is a unit, the factorial term has valuation2k−2v_p(n!)−v_p(D). For a0=floor(n/p)>=2, n+h<(a0+2)p<p^a0 and2n+b−1<p(2a0+3)<p^(a0+1), because p>b>=4. Thus2v_p(n!)−k>floor(log_p(2n+b−1)). The factorial term is uniquely deeper than complete beta, and the actual rational sum has its valuation. This proves (2), rather than merely a statement about raw Gram content.

## 6. A non-vacuous conditional fixed-b finite criterion

Set Hset={1,...,min(m+1,b−m−2)}. Suppose a prime p>b satisfies:

1. All P_r,0<=r<p, are units.
2. p does not divide D_origin, and 2D_origin C_p+B_origin is a unit.
3. The only seed V zeros are r=0 and r=p−h for h in Hset.
4. Each finite reference nu_(p,b,m,h), h in Hset, is a unit.

Then the origin theorem, seed unit transfer and all these boundary charts prove

    v_p(q_n)>=2v_p(n!)−v_p(n)

at every normal n>=2p. This replaces the structurally impossible unnormalized criterion in GENERAL_FIXED_B_ODD_ORIGIN.md for b>=4. It does not claim that condition3 holds for every b,m or a supply of primes. Extra seed zeros, vanishing nu or nonunit endpoint digits require distinct analysis; no numerical extrapolation closes them.

A finite set S of such primes would give

    log q_n >= rho_S n−(2|S|+1)log n−2sum_(p in S)log p,
    rho_S=sum_(p in S)2log p/(p−1),

for every normal n>=2max S. This includes beta and the final evaluated gcd. No growing-b rate uniformity, signed-error theorem, broad prime atlas or e+pi conclusion follows without the corresponding hypotheses.

## 7. A single h3 reference, kept separate from proof

To ensure the new chart has a concrete higher-order instance, general_h_reference.py/json records the SINGLE b7,m2,h3 reference at p13,n166, using direct normalized definitions modulo p^7. It has P_n=7 modulo13 and (delta,nu)=(4,4). The endpoint-digit unit receipt is already preserved in the existing p13 atlas. This reference supplies the finite unit input for that one disk. It is not an all-depth probe, a whole b7 criterion, or an independent review.
