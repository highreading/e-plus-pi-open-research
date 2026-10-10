> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A classical Laguerre congruence and the actual last prime block

Coordinator derivation,8 October2026. The polynomial congruence is classical;
the specialization below is a proposed interface for the actual two-square
kernel. External independent audit is required. No final denominator estimate
is claimed. Low-prime valuations and the ALL-prime final gcd remain open.

## Archive and primary literature gate

A scoped search of archive sources and20261007 Markdown reports for Laguerre
congruences, Carlitz and the two-square low-prime specialization found no
already evaluated last-block formula for this new family. Other dyadic Delta
hits use different matrices and are not imported. This is a scoped overlap
check, not an exhaustive absence statement.

The primary paper by Krylov and Li,
[A congruence property of irreducible Laguerre polynomials in two variables](https://math.colgate.edu/~integers/q57/q57.pdf),
was read in its Introduction and Section3, including Corollary2 and its proof
(pages6--8, extracted lines496--735). The classical one-variable identity
is reused; the new two-variable theorem and its remaining sections are not
needed and are not claimed fully verified. Carlitz's original1954 paper was
identified but its online opening failed; no full reading is claimed for it.
The Artin--Hasse article was opened but is not used in the derivation.

## 1. Integral polynomial block identity

Use H_j(x)=j!L_j(x), with alpha0 and integer coefficients

    H_j(x)=sum_(r=0)^j(-1)^r binom(j,r)*(j!/r!)*x^r.

For any prime p, j=kp+a,0<=a<p, the classical congruence gives

    H_j(x)=(-x)^(kp) H_a(x) modulo p.                 (1)

A direct proof at prime p also suffices. Terms r<kp contain the multiple
kp in j!/r! and vanish. At r=kp+b,0<=b<=a, Lucas gives
binom(kp+a,kp+b)=binom(a,b) modulo p; the factorial quotient equals
a!/b! modulo p. Restoring the sign proves(1). All quantities are integral
polynomials, so no division by p is performed.

## 2. The exact source-normalized basis E_j

Retain E_j(t)=N!L_j(1-t)=(N!/j!)*H_j(1-t),0<=j<=N.
For an odd prime p<=N write N=kp+a,0<=a<p. Then

    E_j=0 modulo p                  if j<kp,
    E_(kp+r)(t)=(a!/r!)*R_p(t)*H_r(1-t) modulo p,
                                      0<=r<=a,
    R_p(t)=(-(1-t))^(kp).                              (2)

In(2), the quotient a!/r! is a p-adic unit. Earlier blocks vanish because
N!/j! contains kp, regardless of H_j's coefficients. Thus the entire
actual source-normalized evaluation kernel modulo p is its LAST partial
block. It is not an unscaled Laguerre kernel at a replacement index.

Let zeta=R_p(i) in F_p[i]. Its norm is

    zeta*conjugate(zeta)=2^(kp),

which is a unit for odd p, including the split algebra p=1 modulo4.
For the partial block put

    A_r+i B_r=(a!/r!)*H_r(1-i), 0<=r<=a,
    U_a=sum A_r^2, V_a=sum A_r B_r, W_a=sum B_r^2.

Writing zeta=x+i y, multiplication by zeta rotates each evaluation
column by the matrix [[x,-y],[y,x]], of unit determinant x^2+y^2.
Consequently the actual U_N,V_N,W_N matrix is this congruence transform
of the partial-block2-by2 matrix, and

    Delta_N=2^(2kp)*(U_a W_a-V_a^2) modulo p.           (3)

This remains a statement modulo p. It proves no prime-power depth and
cannot justify division by a singular kernel determinant.

## 3. Two explicitly evaluated residue classes

If a=0, the last block consists of one evaluation column; hence

    p|N implies p|Delta_N.                             (4)

If a=1, H_0(1-i)=1 and H_1(1-i)=i. The partial matrix is the identity.
Thus for every odd p<=N with N=1 modulo p,

    U_N=W_N=2^(kp), V_N=0, Delta_N=2^(2kp) modulo p.    (5)

In particular Delta is a unit. B=(N!)^2 has positive valuation, so
D=Delta-BW is also a unit. The actual Phi modulo p is

    Phi_N(t)=2^(kp)*R_p(t)*(x-y*t) modulo p.            (6)

Since x,y are not both zero, (6) is a nonzero polynomial. Thus
d=cont(Phi_N) is a p-adic unit. For N>=4 these primes divide
T=(2N-4)!R4(2N-4), and the raw polynomial
T Phi^2+D Delta g^2 reduces to the nonzero polynomial D Delta g^2.
Therefore its actual polynomial content h is a p-adic unit, and

    v_p(M)=v_p(T),   p odd, p<=N, N=1 modulo p.         (7)

The next argument evaluates the complete affine clearer and final gcd
AT THESE PARTICULAR PRIMES. It does not handle other residue classes.

## 4. Actual affine denominator and final q at odd divisors of N-1

Put s=v_p(N-1)>=1 and m=2N-4=2kp-2. The actual integral quotient is

    S=(T*Q_Phi+D*Delta*S_g)/h,
    Q_Phi=(Phi^2-Delta^2)/(1+t^2),
    S_g=(1+t^2)(1-t)^m.

All three quotient polynomials are integral at the stated scope. Their
highest degree is2N-2, so every monomial integration denominator is
at most2N-1. Write a_max=floor(log_p(2N-1)). Thus

    v_p(int_0^1 Q_Phi)>=-a_max.

For every k>=1 and p>=3, 2kp+1<p^(2k), by induction on k.
Hence a_max<=2k-1. Also v_p(T)>=floor(m/p)=2k-1.
Therefore T*int Q_Phi is p-integral. This bound retains the full
first-square arctan term; it does not discard it by assumption.

The second-square beta integral was evaluated in A2turn1:

    beta_g=int_0^1 S_g
          =(m^2+5m+8)/[(m+1)(m+2)(m+3)].

At p|N-1, the outer denominators are units, m+2=2(N-1) has
valuation s, and m^2+5m+8=2 modulo p is a unit. Thus
v_p(beta_g)=-s. Since D,Delta and h are units, this negative
valuation strictly dominates the paid first-square term, giving

    v_p(int_0^1 S)=-s.

The exact affine rational source is an INTEGER endpoint functional
minus4*int S. Its least scalar denominator lambda therefore has
v_p(lambda)=s. In the accepted normalization gcd(lambda,A)=1;
hence A is a p-adic unit and the final G=gcd(M,A) has valuation0.
Combining this with(7) proves the proposed uniform formula

    v_p(q_N)=v_p(T_N)+v_p(N-1),
    N>=4, p an odd prime dividing N-1.                 (8)

This is an actual primitive-denominator statement with all payments.
It does not decide e+pi or show whole-error decay. Other primes,
prime2, source-kernel singularities and the ALL-prime product remain
open. It is not a no-go theorem without a matching lower bound on
the ordinary error at the same indices. Independent review is pending.
