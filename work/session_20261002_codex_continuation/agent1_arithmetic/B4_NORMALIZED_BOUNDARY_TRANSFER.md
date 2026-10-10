> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A normalized n+1 boundary chart for the fixed b=4,m=1 Gram center

New author candidate, 2026-10-02. No independent review is asserted. This develops the boundary obstruction in GENERAL_FIXED_B_ODD_ORIGIN.md. It does not assert a signed-error theorem for b=4 or an e+pi conclusion. All endpoint and logarithmic terms are retained.

Use the exact general normalized N,A,K,Omega,Y,D,V and center c from that note, at b=4,m=1. Fix p>=5, assume P_r is nonzero modulo p for every0<=r<p, and write u=n+1, k=v_p(u)>=1. For this metric Omega_j=(n+2)_j²=(u+1)_j².

The theorem to be proved is a normalized boundary transfer:

    D_n/(u² P_n²)=delta_p mod p,
    V_n/(u² P_n)=nu_p mod p,                     (1)

where the quotients are p-integral and delta_p,nu_p are obtained at the single reference n*=p²−1. Specifically,

    delta_p=D_(p²−1)/(p⁴ P_(p²−1)²) mod p,
    nu_p=V_(p²−1)/(p⁴ P_(p²−1)) mod p.           (2)

If nu_p!=0, then v_p(V_n)=2k and v_p(D_n)>=2k at ALL boundary indices, regardless of the endpoint carry. A zero delta_p need not obstruct a denominator lower bound; it raises the depth of D rather than V.

## 1. Exact integrality of the boundary quotients

All reductions modulo u below mean modulo p^k, with the p-unit factor of u ignored. For the lower three rows of N, truncating individually at the factor u gives

    N_lower=T=[[1,0,0,0],[2,1,0,0],[4,4,2,0]] mod u.

This uses a_s(-1)=[t^s](1−t+t²/2)^(-1), whose first three coefficients are1,1,1/2; the short coefficients have p-unit polynomial denominators. Write T3 for the invertible first three columns of T.

Since D0_i has a factor u for i>=1, the identity N Y=det(N)D0J implies Y0,Y1,Y2 are divisible by u. Also K(-1)=Z(I+Dpol), whose first two rows are

    [-1,−1,0,0], [1,0,−2,0].

Hence x=KY has x0,x1 divisible by u. Every Omega_j with j>=2 is divisible by u². This proves D=x^T Omega x is divisible by u².

Let B=adj(N)A and t=KB. Put R=Dcal_(2u−1), without assuming any higher-precision value for R. The lower A rows reduce to

    A_lower=[R,1+R,4+R]^T mod u.

Indeed Dcal_(2u)=1 modulo u and Dcal_(2u+1)=2 modulo u. Solving the lower triangular equations N B=det(N)A gives

    B0=det(N)R,
    B1=det(N)(1−R),
    B2=det(N)R/2 mod u.

Therefore

    t0=−det(N), t1=0 mod u.

The complete numerator, WITH its correction, is

    V=x0(t0+det(N))+(u+1)²x1t1
             +sum_(j=2)^4 Omega_j x_j t_j.

Every term is divisible by u². Thus both quotients in (1) are p-integral. Omitting kappa would leave the first summand x0t0 with only one forced u factor and would change this normalization.

## 2. Uniform first-order lower-row expansions

There exist matrices G_p in F_p^(3x4) and vectors B_p in F_p^3, independent of n,k and endpoint digits, such that

    N_lower=T+u(G_p+epsilon T) mod p^(k+1),
    A_lower=Abar(R)+u(B_p+epsilon Abar(C_p)) mod p^(k+1),       (3)

where Abar(R)=(R,1+R,4+R)^T, C_p=Dcal_(p−1)=sum_(j=0)^(p−1)(−1)^j j! modulo p, and

    epsilon=u/p mod p if k=1; epsilon=0 if k>=2.

Here R is kept at its actual precision: it is not replaced by C_p before multiplication by a u factor. Only R modulo p is C_p.

A direct termwise proof of (3) follows. In lower row i=1,2,3, a falling factorial of length at least i contains u; one of length at least p+i contains both u and u−p. Thus terms of length at least p+i vanish modulo p^(k+1), or lie outside the finite sum when u=p. Short coefficients with s<=i−1 have p-unit polynomial denominators, so their first-order expansion at n=−1 is legitimate.

For the remaining one-u terms, only a_s(n) modulo p is needed. For k>=2,

    q0(t)^n=q0(t)^(-1) mod p in degrees less than2p,

because q0(t)^n=q0(t^p)^(u/p)/q0(t) and u/p=0 modulo p. Thus the one-u coefficients are fixed. For k=1, the additional coefficient in degrees p+ell,0<=ell<=2, is

    −epsilon a_ell(−1) mod p.

Wilson's theorem gives

    (u+i−1)_(p+j+ell)/u=−(i−1)_(j+ell) mod p

when j+ell<=i−1, and zero otherwise. Summing proves that the additional lower N-row term is exactly u epsilon T.

For A, short Dcal offsets are only−1,0,1, because s<=i−1. The recurrence propagates from the actual R=Dcal_(2u−1):

    Dcal_(2u)=1+2uR,
    Dcal_(2u+1)=2+2u(1+R) mod p^(k+1).

All other contributing terms already have a u factor, so their Dcal value is needed only modulo p and follows from the reset recurrence. The same Wilson/Frobenius calculation gives the extra u epsilon Abar(C_p). This proves existence of the fixed G_p,B_p, and the reference k=2 determines them if explicit values are wanted.

No first-residue tail is extrapolated to depth k: the precision bound and the possible k=1 coefficient correction are included in this argument.

## 3. Removing the free backward Dcal parameter

The high row of N,A modulo p is fixed by the all-residue transfer, as are det(N) modulo p and B3 modulo p. No inversion of det(N) is required.

Solve the lower rows of N B=det(N)A through one additional p-adic digit using T3^(-1). Their zeroth-order solution is det(N)(R,1−R,R/2). Its variation with R is proportional to

    e=(1,−1,1/2)^T.

The first two rows of K(-1) annihilate e. Thus the unknown higher digits of R cancel from (t0+det(N))/u and t1/u; their first-order values depend only on R modulo p=C_p and on fixed G_p,B_p.

The epsilon terms in (3) also cancel from these lower equations: epsilon T3 applied to the zeroth-order solution equals epsilon det(N)Abar(R), whereas the A-side term is epsilon det(N)Abar(C_p). Their difference has an additional p factor. The last column of T is zero. Therefore the normalized low t-corrections are independent of k=1 versus k>=2 and of u/p modulo p. This statement remains valid when p divides det(N), because only the unit lower matrix T3 is inverted.

## 4. Removing the endpoint carry from the low metric coordinates

Write n=pa−1. Put s=P_(a−1) and h=CT_z(z^(-1)+2+2z)^(a−1)z. Frobenius and the support interval give

    J0=P_(p−1)s,
    (J1,J2,J3)=s(J1*,J2*,J3*)+h(1,1,1/2) mod p,             (4)

where the starred entries are the seed p−1 values. The three carried coefficients1,1,1/2 follow by taking the coefficients of z^p in W0(z)^(p−1)(1+z)^i, i=1,2,3. Equivalently, the first three coefficients at the upper edge of W0^(p−1) are1,−1,1/2.

After dividing D0_i by u, the lower endpoint carry is exactly h(1,1,1). Its image under T3^(-1) is h e. Since K(-1)'s first two rows annihilate e, this carry does not affect x0/u or x1/u modulo p. The k=1 epsilon term in N likewise has no effect, because T's final column is zero and Y_lower is already divisible by u.

The last coordinate of Y modulo p is a fixed p-unit multiple of P_n, as proved by the lower triangular cofactor. Also P_(p−1) is a p-unit under the digit assumption, so s=P_n/P_(p−1). Consequently

    (x0/u,x1/u) modulo p is a fixed vector times P_n,
    (x2,x3,x4) modulo p is a fixed vector times P_n.          (5)

The fixed vectors are the same at every depth k. The high t coordinates modulo p are fixed by N,A; the normalized low t corrections are fixed by Section3. Substituting (5) into the normalized D,V formulas proves (1) with the reference constants (2).

## 5. Complete denominator consequence

If nu_p is a unit, (1) gives v_p(V)=2k and v_p(D)>=2k. The normalized selector is zhat=D0 adj(N)^T H Y. Since the two low entries of x have a u factor and the high metric weights have u², H Y is divisible by u. Thus every selector coefficient is divisible by u; the Rodrigues polynomial and logarithmic quotient share that factor. The exact odd-prime moment bound therefore gives

    v_p(beta)>=k−v_p(D)−floor(log_p(2n+3)).

The factorial term has valuation2k−2v_p(n!)−v_p(D). For n>=2p, the same elementary floor estimates as the general origin proof give

    2v_p(n!)−k>floor(log_p(2n+3)).

The factorial term is strictly deeper than beta. The ACTUAL reduced complete center therefore has

    v_p(q_n)=2v_p(n!)+v_p(D_n)−2k>=2v_p(n!)                 (6)

at every n=−1 modulo p. The final rational sum, and hence its endpoint gcd, is retained.

## 6. Finite b4 prime criterion and bounded evidence

Combine (6) with the general all-depth origin theorem and all-residue transfer. A prime p>=5 is sufficient if

    all P_r,0<=r<p, are units;
    the only seed V zeros are0 and p−1;
    the origin coefficient576(3C_p−13) is a unit;
    nu_p from the SINGLE reference p²−1 is a unit.

Then every normal n>=2p satisfies

    v_p(q_n)>=2v_p(n!)−v_p(n).

The bounded new data identify the primes5,7,43,67,71 as satisfying the finite parts. Their reference residues are

| p | n* | delta_p | nu_p |
|---:|---:|---:|---:|
|5|24|0|2|
|7|48|4|3|
|43|1848|39|25|
|67|4488|5|16|
|71|5040|56|13|

The p7 reference has det(N)=0 modulo p, illustrating why Section3 must not invert the full contact determinant. The p5 zero delta is retained, not treated as a failed numerator unit.

The evidence is b4_finite_criterion.json (bounded residue states) and b4_boundary_constants.json (the five reference states modulo p⁵). The earlier boundary probes motivated the proof strategy and are not infinite certificates. The all-depth transfer argument above and the identification of the actual canonical center are author-level obligations awaiting independent examination.

## 7. Full actual-denominator rate and explicit finite receipt

B4_NORMALIZED_PRIME_CERTIFICATE.json retains all193 seed states for the five primes, the five references modulo p^5, source hashes, and exact rational logarithm intervals. Its generation uses the finite identities (2); it does not infer (1) from further sample depths. The proof of (1) is Sections1–4. The rational rate is

    rho_4=sum_(p in {5,7,43,67,71}) 2log(p)/(p−1),
    1.8816662214728844<rho_4<1.8816662214728846.

All normal n>=142 obey, at author-proof status,

    log q_n >=rho_4 n−11log n−2log(5·7·43·67·71).             (7)

Indeed the local theorem supplies 2v_p(n!)−v_p(n) at each selected prime. Legendre's exact formula is v_p(n!)=(n−s_p(n))/(p−1), and s_p(n)/(p−1)<=floor(log_p n)+1. The five digit-sum losses therefore total at most10log n+2sum log p. Finally sum_selected v_p(n)log p<=log n. Equation (7) concerns the ACTUAL complete reduced center, with beta and the correction retained, rather than an unnormalized determinant or a separate exponential term.

The same exact rational receipt shows rho_4−2log(1+sqrt2)>0.1189190474337977. The second number is recorded only as the existing b3 analytic-rate benchmark. No b4 signed-error statement is assumed in (7), and comparing this benchmark does not by itself exclude the b4 center. A complete b4 analytic error theorem would be a distinct target requiring its own archive/literature gate.

For clarity, the beta comparison in Section5 uses polynomial content before evaluating the rational moment. In the canonical direct logarithmic formula beta=calL((K_zhat−D)/(t−1))/D, HY has coefficient content u in the p-local coefficient ring, so zhat=D0 adj(N)^T HY and K_zhat have that same content. Also D is divisible by u². Division by the monic polynomial t−1 preserves the u content, and its exact quotient exists by the endpoint contact condition. Under t=(1+iy)/2 all coefficient denominators are powers of2, which are p-units. Integrating the polynomial contributes denominators at most its degree plus1=2n+3. This gives the displayed valuation bound k−v_p(D)−floor(log_p(2n+3)) for the complete beta. The actual factorial term is strictly more negative; a rational sum of unequal p-adic valuations takes the smaller valuation. That last step is precisely the final evaluated gcd control and prevents a hidden beta cancellation from changing (6) or (7).
