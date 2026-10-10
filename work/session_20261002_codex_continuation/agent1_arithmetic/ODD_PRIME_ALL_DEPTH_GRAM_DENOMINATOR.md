> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An all-depth odd-prime denominator theorem for the fixed b=3 Gram center

Author derivation, 2026-10-02. No independent mathematical review is asserted. This uses the fixed b=3,m_w=1 factorial B-only Gram center and retains its complete endpoint correction. The theorem below is arithmetic; the final comparison with the signed error depends separately on that asymptotic theorem's accepted scope.

The exact normalized definitions are in NORMALIZED_GRAM_IDENTITIES.md. In this note write D=Y^T H Y and V=Y^T H adj(N)A+det(N)(KY)_0, so

    c=2^n V/((n!)² D)+beta.

All entries of N,A,Y,H and all coefficients of the normalized selector belong to Z[1/2]. On a normal index D>0. This representation cancels the original d=(n+1)(n+2) over Q, before local reduction, and includes kappa in V. No coefficient-content quantity is identified with q=den(c).

## 1. A finite-prime criterion

For an odd prime p>=5 set

    C_p=sum_(j=0)^(p−1) (−1)^j j! mod p.

Define N_r,A_r,D_r,V_r by the exact normalized formulas at every seed 0<=r<p. These finite integer/rational contractions are defined regardless of whether the corresponding small approximant is normal. Suppose

    P_r !=0 mod p for every 0<=r<p,
    V_0=0 mod p and V_r !=0 mod p for every 1<=r<p,
    3C_p+4 !=0 mod p.                              (C)

Then for every normal integer index n>=2p, its ACTUAL reduced center denominator obeys

    v_p(q_n)>=2v_p(n!)−v_p(n).                     (T)

More precisely,

    v_p(q_n)=2v_p(n!)+v_p(D_n)       if p does not divide n,
    v_p(q_n)=2v_p(n!)−v_p(n)         if p divides n.

The prime criterion has only finitely many exact residue calculations. The all-index and all-depth deductions are proved below; a numerical test of large n is not their justification.

## 2. All-residue transfer, including endpoint carries

Let n=ap+r, 0<=r<p, and let a_s(n)=[t^s](1−t+t²/2)^n. These are p-integral. The defining expressions are

    N_ij=sum_s a_s(n)(n+i)_(j+s),
    A_i=sum_s a_s(n)(n+i)_s Dcal_(2n+i−s).

A falling factorial whose length is larger than the least nonnegative residue of n+i contains a multiple of p. Every surviving coefficient has index s<p. Frobenius gives a_s(n)=a_s(r) modulo p for these indices. The division-free recurrence Dcal_j=j Dcal_(j−1)+1 resets to1 at every multiple of p, so Dcal_j modulo p depends only on j modulo p. Consequently

    N_n=N_r, A_n=A_r, K_n=K_r, H_n=H_r mod p.

This argument includes r=p−2 and p−1; it does not divide by n+1 or n+2.

The endpoint generating function P(t)=(1−4t−4t²)^(-1/2) satisfies

    P(t)=(1−4t−4t²)^((p−1)/2)P(t^p) over F_p.

The polynomial prefactor has degree p−1. Thus P_(pa+r)=P_a P_r modulo p, including r=0 and p−1. In particular (C) makes every P_n a p-unit by iteration on base-p digits.

For r<=p−3, the endpoint vector J_n is P_a J_r modulo p directly. At r=p−2 the possible carry in P_(n+2) is multiplied by d_n=0 modulo p in D0J. At r=p−1, both carried entries are killed by their factors n+1. Hence, for EVERY residue r,

    D0(n)J_n=P_a D0(r)J_r mod p,
    Y_n=P_a Y_r,
    V_n=P_a V_r,
    D_n=P_a² D_r mod p.                          (1)

Thus p does not divide n implies V_n is a p-unit under (C). The remaining case p|n needs the higher-depth argument.

## 3. Coefficient bounds on the origin disk

Write k=v_p(n)>=1 and n=p^k a, p not dividing a. Expand

    a_s(n)=sum_j binom(n,j)[t^s](−t+t²/2)^j.

Every contributing j lies between ceil(s/2) and s. The identity binom(n,j)=(n/j)binom(n−1,j−1) gives

    v_p(a_s(n))>=max(0,k−floor(log_p s)), s>=1.    (2)

The bound is for the rational coefficient as a p-adic integer, using only powers of two as coefficient denominators.

Suppose k>=2. For every s>=3 in a matrix or A_i sum, the relevant falling factorial contains n, since i<=2. If s<p^k, (2) contributes at least one additional power of p. If s>=p^k, the falling factorial contains n and n−p, because p^k>=p²>=p+3; n−p is a nonzero multiple of p. Thus every such term vanishes modulo p^(k+1). The s=2 coefficient is a_2(n)=n²/2 and also vanishes at this precision; a_1(n)=−n.

Let

    N0=[[1,0,0],[1,1,0],[1,2,2]],
    N1=[[0,1,−1],[−1,1,1],[−2,−1,3]],
    A0=[1,2,5]^T,
    A1=[2C_p,1+2C_p,4+4C_p]^T.

For k>=2 the surviving terms give

    N_n=N0+n N1,
    A_n=A0+n A1 mod p^(k+1).                     (3)

To verify the Dcal part of A1 without a continuity assumption, use the exact identity Dcal_j=sum_(l=0)^j (j)_l. For j=2n every term with l>=p+1 contains 2n and 2n−p, and hence vanishes modulo p^(k+1). For 1<=l<=p,

    (2n)_l/(2n)=(−1)^(l−1)(l−1)! mod p.

Therefore Dcal_(2n)=1+2n C_p modulo p^(k+1). The two following recurrence steps, together with a_1(n)=−n, give exactly the displayed A1.

## 4. The k=1 layer and its common scale

Now k=1 and a=n/p. Terms with 3<=s<p vanish modulo p² by (2) and the factor n. Terms with s>=p+3 contain n and n−p and also vanish. In the remaining indices p,p+1,p+2, Frobenius gives

    a_p(n)=−a mod p,
    a_(p+1)(n)=a_(p+2)(n)=0 mod p.

For a matrix entry, the s=p term vanishes if j>i, because its falling factorial contains two multiples of p. If j<=i, Wilson's theorem gives

    (n+i)_(p+j)/n=−(i)_j mod p.

Hence this term is n a (N0)_ij modulo p². Similarly the extra s=p term in A_i is n a Dcal_i=n a (A0)_i modulo p². The case n=p presents no problem: every term that would require n−p=0 lies outside the permitted finite sum, or is a zero falling factorial polynomial term.

Thus

    N_n=N0+n(N1+a N0),
    A_n=A0+n(A1+a A0) mod p².                    (4)

The extra term is the SAME common scalar 1+a n on N and A. Treating that term as an independent numerator perturbation would create a false exceptional origin branch.

## 5. First-order Gram contraction at every depth

Put

    W=H adj(N)A+det(N)k0^T,

where k0 is row0 of K. The exact n=0 matrix identity gives W0=0. Scaling both N and A by 1+a n scales W by (1+a n)^3. Because W0=0, it does not change W/n modulo p. This removes the extra k=1 scale in (4).

The polynomial reconstruction and metric have first-order matrices

    K=[[-1,n,−n], [1,−1−n,3n], [0,1,−1−2n], [0,0,1]] +O(n²),
    H=[[5+4n,−4−9n,13n],
       [−4−9n,8+24n,−4−32n],
       [13n,−4−32n,4+28n]] +O(n²).

Substituting (3) into W and collecting the coefficient of n gives

    W/n=[20C_p+16,−24C_p−48,8C_p+32]^T mod p.     (5)

Since p|n, (1) gives J_n=P_(n/p)(1,1,1)^T modulo p. Also P_n=P_(n/p) modulo p; write j=P_n modulo p. Then

    Y_n=(2j,0,j)^T mod p,
    D_n=24j² mod p,
    V_n/n=16j(3C_p+4) mod p.                     (6)

Equations (2)–(6) prove this at EVERY k>=1, rather than extrapolating a first-residue truncation. Under (C), j and 3C_p+4 are units, and p>=5 makes24 a unit. Therefore

    v_p(D_n)=0, v_p(V_n)=v_p(n) whenever p|n.     (7)

The accompanying origin_derivative.py collects the finite symbolic matrix identity (5); the infinite precision argument is the proof above.

## 6. The logarithmic companion and final rational reduction

Write the normalized integer selector coefficients as

    zhat=D0 adj(N)^T H Y,
    z=2^(4n) zhat,
    Dg=2^(4n)D.

For odd p, every coefficient of zhat and the Rodrigues polynomial K_zhat is p-integral. The exact endpoint identity K_zhat(1)=D ensures that the quotient (K_zhat−D)/(t−1) has p-integral coefficients. Its degree is at most2n+1.

The exact moments

    mu_j=((1+i)^(j+1)−(1−i)^(j+1))/(i 2^j(j+1))

satisfy v_p(mu_j)>=−v_p(j+1). Thus, with l=floor(log_p(2n+2)),

    v_p(beta)>=−v_p(D)−l.                        (8)

Let f=v_p(n!) and a=floor(n/p)>=2. We have f>=a. Since n<(a+1)p<=p^a for p>=5,a>=2, v_p(n)<=a−1. Also 2n+2<=2p(a+1)<p^(a+1), so l<=a. Consequently

    2f−v_p(n)>=a+1>l.                           (9)

If p does not divide n then v_p(V)=0; if it does, (7) gives v_p(V)=v_p(n). Equations (8)–(9) show that the factorial rational term has strictly smaller p-adic valuation than beta. There is no equal-depth cancellation, and the ACTUAL complete center has

    v_p(c)=v_p(V)−2f−v_p(D)<0.

Its reduced denominator therefore has the exact depths claimed in Section1. This step incorporates the final endpoint gcd by reducing the actual rational sum. Neither selector primitivity nor a conjectured endpoint unit is used as a substitute for that reduction.

## 7. Aggregate consequence of a finite atlas

For any finite set P of primes satisfying (C), all sufficiently large normal indices satisfy

    log q_n>=sum_(p in P)(2v_p(n!)−v_p(n))log p
            =rho_P n−O_P(log n),
    rho_P=sum_(p in P)2log p/(p−1).               (10)

The error term follows from Legendre's digit-sum formula for each fixed prime and v_p(n)<=log_p n. All prime factors in the sum occur at the SAME index n; this avoids the incompatible-index limitation of the earlier p^k+3 progressions.

If a finite certified atlas has rho_P>2log(1+sqrt2), then (10), together with the separately justified signed-error asymptotic, excludes shrinking primitive forms for this particular fixed b=3 Gram center. It does not decide whether e+pi is irrational and does not apply to another center or growing b.

The bounded residue evidence and final atlas weight are recorded separately. The theorem is presently an author candidate; finite computational certificates must retain their finite scope and the all-depth argument above must be independently examined before an accepted construction exclusion is reported.
