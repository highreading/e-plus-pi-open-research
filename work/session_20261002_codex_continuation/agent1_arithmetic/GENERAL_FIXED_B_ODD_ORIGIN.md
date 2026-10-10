> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# General fixed-b transfer and the origin coefficient of the B-only Gram center

New author mathematics, 2026-10-02. No independent review is asserted. This note extends the local arithmetic mechanism, not the independently reviewed scope of the b=3 candidate. It uses the actual canonical fixed-b,m metric from the companion-transfer source. No b=1 or b=2 denominator scan is repeated, and no fixed-b>=4 analytic exclusion is claimed.

Fix b>=3 and 1<=m<=floor((b−1)/2). Let p>b be an odd prime. Set

    q0(t)=1−t+t²/2, a_s(n)=[t^s]q0(t)^n,
    N_ij=sum_s a_s(n)(n+i)_(j+s), 0<=i,j<b,
    A_i=sum_s a_s(n)(n+i)_s Dcal_(2n+i−s), 0<=i<b,
    D0_i=(n+i)!/n!,
    K=Z(I+Dpol)^(-n), Omega_j=(n+m+1)_j², 0<=j<=b,
    H=K^T Omega K,
    J_i=[t^n](1+2t+2t²)^n(1+t)^i,
    Y=adj(N)D0J, D=Y^THY,
    W=H adj(N)A+det(N)k0^T, V=Y^T W.

Here Z multiplies coefficient polynomials by t−1, Dpol differentiates, and k0 is row0 of K. The summation ranges are the same nonnegative factorial-endpoint ranges as their direct normalized definitions. The normalized complete center is exactly

    c=2^n V/((n!)²D)+beta.                       (1)

To derive (1), the general canonical data satisfy M=2^nN, x=2^((b−1)n)KY, Dg=2^(2(b−1)n)D and z=2^(2(b−1)n)D0 adj(N)^T H Y. The exponential companion is 2^n z^T D0^(-1)A/((n!)²Dg), while kappa=det(M)x0/((n!)²Dg). Substitution gives the two terms in V. Equivalently one may multiply by d=(n+b−1)!/n! and cancel it over Q before local reduction. Thus the endpoint correction is retained.

## 1. Endpoint transfer at every residue

Write W0(t)=t^(-1)+2+2t. Then

    J_i=CT_t W0(t)^n(1+t)^i.                    (2)

This follows directly from the Rodrigues endpoint: differentiating Q(t)^n t^i at1 gives [z^n]Q(1+z)^n(1+z)^i, with Q(1+z)=1+2z+2z².

Let n=ap+r, 0<=r<p. Frobenius expresses the high factor as W0(t^p)^a. The low factor W0(t)^r(1+t)^i has exponents in[−r,r+i]. If r+i<p, only exponent0 in this interval is divisible by p. It follows that

    J_i(n)=P_a J_i(r) mod p.

If r+i>=p, then D0_i=(n+1)...(n+i) contains a multiple of p; the same is true at the seed r. Thus this coordinate is zero on both sides after multiplying by D0. Consequently

    D0(n)J_n=P_a D0(r)J_r mod p                 (3)

at ALL residues, without dividing by the boundary factors. The same coefficient/falling-factorial/reset argument as the b=3 proof gives N_n=N_r and A_n=A_r modulo p. Hence

    Y_n=P_aY_r, V_n=P_aV_r, D_n=P_a²D_r mod p.  (4)

In particular P_n=P_aP_r follows from (2) with i=0. A finite digit-unit check P_r!=0 for0<=r<p makes every P_n a p-unit.

## 2. General origin matrices

At n=0 define

    N0_i,j=(i)_j,
    A0_i=Dcal_i=sum_(j=0)^i(i)_j,
    t0=det(N0)=product_(j=0)^(b−1) j!,
    u_j=derangements(j)/j!, Y0=t0 u.

The formula for u follows by the finite Newton transform of i!. In particular N0u=(i!)_i. Also N0·1=A0.

Let Z be the same multiplication matrix, Omega0_j=(m+1)_j² and H0=Z^T Omega0 Z. Since b>m+1, the last diagonal weight is zero. Therefore Z·1 has first coordinate−1 and last coordinate1, and

    H0·1=(1,0,...,0)^T=−k0^T.

It follows that W(0)=0 exactly. Set

    D_origin=Y0^T H0 Y0>0.                      (5)

Positivity is immediate from the first weighted reconstruction coordinate, (Zu)_0=−1. The fact that H0 may have rank less than b for b>3 does not force this particular scalar contraction to vanish.

Define ell_s=[t^s]log q0(t), 1<=s<b. Let N1 and A1(C) be

    (N1)_ij=∂_x (x+i)_j|_(x=0)
                +sum_(s=1)^(b−1) ell_s (i)_(j+s),
    g_0(C)=2C,
    g_i(C)=i g_(i−1)(C)+2Dcal_(i−1),
    (A1(C))_i=g_i(C)+sum_(s=1)^i ell_s (i)_s Dcal_(i−s).

All their denominators have prime factors at most b or2, so they are p-integral for p>b. Let

    L=log(I+Dpol)=sum_(s=1)^(b−1)(−1)^(s+1)Dpol^s/s.

The first-order reconstruction is K=Z−n ZL+O(n²).

## 3. All-depth origin expansion

Suppose k=v_p(n)>=1. The coefficient bound

    v_p(a_s(n))>=max(0,k−floor(log_p s))

is unchanged. For k>=2, every term with s>=b contains n in its falling factorial. If s<p^k the coefficient supplies an additional p; if s>=p^k the falling factorial also contains n−p, because p>b. Thus all such terms vanish modulo p^(k+1). For s<b the polynomial coefficients may be expanded to first order with p-unit denominators. The reset-factorial identity for Dcal_(2n) gives C_p=sum_(j=0)^(p−1)(−1)^j j!, exactly as before. Therefore

    N=N0+n N1,
    A=A0+n A1(C_p) mod p^(k+1), k>=2.           (6)

For k=1 the sole additional Frobenius coefficient is s=p. Terms p+1,...,p+b−1 have zero coefficient modulo p, and terms with s>=p+b contain two multiples of p. Wilson's theorem yields the same common-scale term as in the b=3 proof:

    N=N0+n(N1+a N0),
    A=A0+n(A1(C_p)+a A0) mod p²,
    a=n/p mod p.                               (7)

Scaling N and A by1+a n scales W by(1+a n)^b. Since W0=0, it has no effect on W/n modulo p. Thus the same origin derivative governs every depth k>=1.

## 4. Explicit affine origin coefficient

Differentiating the adjugate by N0^(-1), the trace terms cancel because W0=0. Also the metric/reconstruction derivative satisfies

    H1·1+k0'=−H0 L·1.

Indeed the first metric weight is constant, the final weight and its derivative vanish at n=0, and K'=-ZL. Therefore

    W1(C)=t0 H0[ N0^(-1)(A1(C)−N1·1)−L·1 ].    (8)

Define the rational constant

    B_origin=Y0^T W1(0).

The coefficient of C in A1 is2(i!)_i, since g_i has C coefficient2i!. Hence adj(N0)A1's C coefficient is2Y0, and (8) proves

    Y0^T W1(C)=2D_origin C+B_origin.             (9)

At p|n, (3) gives J_i=P_n modulo p for every i<b. Combining (5)–(9),

    D_n=P_n² D_origin mod p,
    V_n/n=P_n(2D_origin C_p+B_origin) mod p.     (10)

This is an explicit general-b all-depth formula, not a parameter-uniform valuation bound inferred from first-layer seeds.

If P_n is a p-unit, p does not divide D_origin, and 2D_origin C_p+B_origin is a p-unit, then

    v_p(D_n)=0, v_p(V_n)=v_p(n) at every p|n.    (11)

The symbolic author script general_origin_coefficient.py computes only these finite rational constants; it is not a scan of actual denominators. Examples are

| b | m | D_origin | 2D_origin C+B_origin |
|---:|---:|---:|---|
|3|1|24|16(3C+4)|
|4|1|864|576(3C−13)|
|5|1|497664|331776(3C+32)|
|5|2|1658880|331776(10C+157)|
|6|1|7166361600|14332723200(C−46)|

These examples do not assert that the required finite nonzero-residue atlas exists for the corresponding b,m.

## 5. A coefficient-kernel-free expression for B_origin

The log-q0 contributions cancel from A1−N1·1. For each i, both are

    sum_(s=1)^i ell_s(i)_s Dcal_(i−s).

Also, the falling-factorial derivative identity gives

    N0 L·1=(∂_x sum_(j=0)^(b−1)(x+i)_j|_(x=0))_i.

Put

    t_i=i! sum_(k=1)^i Dcal_(k−1)/k!,
    r=N0^(-1)(t_i)_i.

The Dcal derivative recurrence gives g_i(C)=2(i!C+t_i). Substituting into (8) therefore simplifies it to

    W1(C)=2t0 H0(C u+r−L·1),
    B_origin=2t0² u^T H0(r−L·1).                (14)

Thus the first contracted origin coefficient is independent of the coefficients ell_s of log q0. It is determined by the reconstruction, the m-dependent metric and the finite dimension b. This identity concerns the origin coefficient, not the complete V sequence or its nonzero residue atlas.

The vectors u and r are rational and explicit. Their ordinary coefficient generating functions are

    sum_j u_j x^j=e^(−x)/(1−x),
    sum_j r_j x^j=e^(−x)/(1−x) integral_0^x e^t/(1−t) dt.

Only the first b coefficients are required. The second formula follows from the Newton transform of t_i and its displayed finite sum; no evaluation at a singularity or infinite p-adic convergence is used here.

## 6. General finite-prime denominator criterion

For any fixed b,m and prime p>b with p not dividing D_origin, suppose

    P_r!=0 mod p for every0<=r<p,
    V_r!=0 mod p for every1<=r<p,
    2D_origin C_p+B_origin!=0 mod p.             (12)

Then for every sufficiently large normal index n, in fact n>=2p, its ACTUAL complete center denominator satisfies

    v_p(q_n)>=2v_p(n!)−v_p(n).                  (13)

The proof is the same strict comparison with beta, now using degree at most2n+b−1. Its normalized selector coefficients are p-integral and

    v_p(beta)>=−v_p(D)−floor(log_p(2n+b−1)).

For a=floor(n/p)>=2, p>b and p>=5 imply n<(a+1)p<=p^a and2n+b−1<p(2a+3)<p^(a+1). Thus v_p(n)<=a−1 and floor(log_p(2n+b−1))<=a, whereas2v_p(n!)−v_p(n)>=a+1. The factorial term is strictly deeper. Equations (4),(11) then determine the valuation of the actual rational sum as in the b=3 theorem.

A finite set of primes satisfying (12) therefore gives a same-index uniform lower rate sum2log p/(p−1). No prime-supply statement, growing-b uniformity, analytic signed-error theorem for b>=4, or e+pi conclusion is established here. The new result is a structural parameter theorem that turns future fixed-b arithmetic into a finite residue criterion plus the explicit origin constants.

## 7. Structural boundary obstruction to the unnormalized criterion for b>=4

A later bounded b4 calculation led to the following exact deduction, which limits Section6's usefulness. With the allowed m, the unnormalized criterion (12) is impossible for every b>=4: V_(p−1)=D_(p−1)=0 modulo every p>b. Thus Section6 is a valid conditional statement but supplies no b>=4 atlas in these metrics. The origin formula remains substantive; the missing boundary normalization cannot be omitted.

To prove this, reduce n to−1 modulo p. For each row1<=i<b,

    N_ij=sum_(s=0)^max(i−1−j) a_s(−1)(i−1)_(j+s) mod p,

with empty sums equal0. Hence N_ij=0 for j>=i and N_(i,i−1)=(i−1)!. The rows1,…,b−1 restricted to columns0,…,b−2 form an invertible triangular matrix modulo p. Their nullspace is exactly the final coordinate line. The first column of adj(N) therefore equals a p-unit scalar times e_(b−1), irrespective of the first row or det(N).

At this boundary D0J has only its first coordinate. Thus Y is in the final coordinate line. Meanwhile

    K(−1)=Z(I+Dpol),
    Omega_j(−1)=(m)_j²=0 for j>m.

The vector K(−1)e_(b−1) is supported only in rows b−2,b−1,b. For b>=4 and m<=floor((b−1)/2), all three rows exceed m. Consequently H Y=0. Its first reconstructed coordinate is also0. Both terms in V vanish, and D=Y^THY vanishes as claimed.

At b=3,m=1, row b−2=1 is still in the metric support; this explains why that case escapes the obstruction and admits the17-prime theorem. A b>=4 actual-denominator theorem must divide the common n+1 boundary powers in the ratio before applying a residue-unit criterion. That division also exposes endpoint carries previously killed by D0, so the scalar transfer cannot simply be reused unchanged.
