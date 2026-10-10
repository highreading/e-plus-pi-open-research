> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Finite propagation for factorially weighted B-only centers

Original author research; no independent audit or numerical scan. The existing CENTER_CONTIGUOUS_RESEARCH.md and its integer zero test are preserved. Contact reduction and eventual normality retain their previously stated provisional status. The recurrence identities below concern exact rational construction data.

## 1. Object and notation

Fix integers b>=3 and 1<=m<=floor((b-1)/2). Write q=1-z+z^2/2, a=n+m+1, f_j=(a)_j (falling factorial), and W=diag(f_j^2), 0<=j<=b. These weights differ from the actual factorial weights by the common positive scalar (a!/(a-b)!)^2; hence they define the same B-only center.

Let G_n=exp(z)q^n, T_ij=[z^(n+i-j)]G_n, and let u,v be the TWO actual forcing columns [z^(n+i)]q^n D^n h, with h^P=1/(1-z) and h^Q=(exp(z)+F)/(1-z), F'=2/q, F(0)=0. Set

    Delta=det T, X=adj(T)u, Y=adj(T)v,
    J=(I+D)^(-n), U=ZJ, Zp=(z-1)p,
    Bp=UX, Bq=Delta e0+UY,
    A_n=Bp^T W Bp, H_n=Bp^T W Bq.

These are UNREDUCED contractions. The notation H_n here is not the contiguous-difference numerator of the preserved note. Wherever the actual endpoint lift is defined and nonzero, A_n>0 and t_n=H_n/A_n. No reduced-coordinate arithmetic is needed below.

## 2. Three-coordinate Toeplitz state

Write g_k=[z^k]G_n. The coefficient equation is

    (k+1)g_(k+1)=(k+1-n)g_k
                    +(2n-k-1)g_(k-1)/2+g_(k-2)/2.

For s_n=(g_n,g_(n-1),g_(n-2))^T, multiplication by q gives

    s_(n+1)=M_g(n)s_n,
    M_g(n)=[-n/(n+1), n/(n+1), 1/(2(n+1));
             1, -1, 1/2;
             n, 1, -1-n/2].

All Toeplitz entries are linear functions of s_n over Q(n). Forward recovery divides by k+1; backward recovery divides only by the constant 1/2. Work henceforth at n>=b+16, so all coefficient indices used in these recoveries are nonnegative and all forward divisors are positive.

## 3. A common forcing equation

For either forcing seed h, put y=(1-z)h. Both y=1 and y=exp(z)+F satisfy

    zq(y'''-y'')-(2q-2zq')(y''-y')=0.

For the latter, F'''-F''=-2(q'+q)/q^2=-z^2/q^2, which verifies the equation directly; the exponential contribution cancels. Thus Lh=0 with L=sum_(i=0)^3 p_i D^i and

    p0=z^2-2,
    p1=2z^3-5z^2+6,
    p2=(z^4-8z^3+12z^2-4z-4)/2,
    p3=-z(z-1)q.

Here is a finite specification of every coefficient of the ensuing recurrence, avoiding a long coefficient table. Define

    a_j=sum_(i,ell: i+2-ell=j) binom(n+2,ell) D^ell p_i,
    0<=j<=5, 0<=ell<=deg p_i.

Define differential operators O_0=1 and O_(j+1)=(D-nq'/q)O_j, with operator multiplication, including differentiation of coefficients. Write

    sum_(t=0)^5 b_t(n,z)D^t=q^5 sum_(j=0)^5 a_j O_j.

The b_t are polynomials. This equation is obtained by differentiating Lh=0 exactly n+2 times and conjugating by q^n. In particular every derivative remaining is D^(n+j)h with j>=0: no omitted integration constants occur.

For K_n^alpha=q^n D^n h^alpha, write k^alpha_(n,l)=[z^l]K_n^alpha. Define

    C_d(n,k)=sum_(t,ell: t-ell=d) [z^ell]b_t(n,z)
                                      product_(v=1)^t(k-ell+v).

Then exactly

    sum_(d=-10)^4 C_d(n,k) k^alpha_(n,k+d)=0.

Each C_d has total degree at most five in n,k. The extreme factors, obtained by the new symbolic derivation recorded in the controller results, are

    C_-10=(k-n-9)^2(k-n-8)^2/64,
    C_4=(k+1)(k+2)(k+3)(k+4)(k+n).

These factors are retained. Backward elimination across offsets k-n=8,9 would fail. The construction below uses only forward elimination, so it does not divide by C_-10.

## 4. Closed 31-coordinate state

For each alpha=P,Q use the 14-coordinate window

    w_n^alpha=(k^alpha_(n,n+j): -2<=j<=11).

Recover the three additional coefficients at offsets 12,13,14 by the preceding recurrence, successively at k=n+8,n+9,n+10. Their divisors are

    d_j(n)=(n+j+1)(n+j+2)(n+j+3)(n+j+4)(2n+j),
    j=8,9,10.

The exact contiguous forcing equation is

    K_(n+1)=q K_n'-nq'K_n.

Consequently the new window is given, for -2<=j<=11, by

    k_(n+1,n+1+j)=(n+j+2)k_(n,n+j+2)
                       -(j+1)k_(n,n+j+1)
                       +(j-n)k_(n,n+j)/2.

Every coefficient on the right belongs to the original window or the three forward recoveries. This is an explicit algorithm for a 14-by-14 rational matrix M_f(n), identical for both forcing columns.

Thus

    v_n=(s_n,w_n^P,w_n^Q),
    v_(n+1)=M(n)v_n,
    M=diag(M_g,M_f,M_f),

has exactly 31 stored coordinates. This is a specified state size, not a claim of minimality. A common denominator is

    q0(n)=(n+1)d_8(n)d_9(n)d_10(n).

Its degree is 16; all its factors are positive at n>=b+16. The numerator matrix q0 M has degree at most 17. Indeed each forward recovery uses coefficients of degree at most five, three successive recoveries have common denominator and numerator degree at most 15, and the forcing update adds at most one degree. Including the g block and the extra n+1 factor gives the stated bound.

Initialization uses the exact finite coefficient definitions in the preserved contiguous note. It does not use any approximation to e+pi. Initializing at an arbitrary admissible n does not infer an identity from samples.

## 5. Recovering the contractions with explicit size bounds

The forcing entries at offsets 0,...,b-1 are already in the window when b<=12. For b>12, obtain further offsets using C_4 forward, through k=n+b-5. A permissible common recovery denominator is

    B(n)=product_(c=1)^(b-1)(n+c)
          * product_(j=8)^(b-5)
             [(n+j+1)(n+j+2)(n+j+3)(n+j+4)(2n+j)],

where an empty product equals one. Repeated factors are deliberately retained. The first product clears Toeplitz forward recovery; backward recovery has only rational constant divisors. Hence deg B<=6b and B(n)>0 in the working range.

After multiplication by B, every recovered T,u,v entry is a linear form in the 31 coordinates with polynomial coefficients. A conservative degree bound for these coefficients is 10b+20: forcing recovery takes at most b steps of degree five; the Toeplitz recurrence takes at most b steps in either direction of degree one, and multiplication by the other recovery denominator is included in this bound.

Both X and Y, and also Delta, are homogeneous of degree b in v_n. J has polynomial entries in n of degree at most b-1, with rational constant denominators only. W has polynomial entries of degree at most 2b. Consequently

    F_n=B(n)^(2b) A_n,
    E_n=B(n)^(2b) H_n

are homogeneous degree-2b polynomials in the 31 state coordinates, whose coefficient polynomials in n have degree at most

    e=40(b+1)^2.

For example the preceding bounds give 2b(10b+20)+4b-2<e. This clearing factor is explicit and positive; it is not a reduced denominator.

Let z_n be the vector of ALL degree-2b monomials in v_n, in any fixed lexicographic order. Its exact allocated dimension is

    N=binom(2b+30,30).

Substitution of M(n)v gives an explicit symmetric-power matrix T_s(n) with

    z_(n+1)=T_s(n)z_n,
    T_s=P_s/Q, Q=q0^(2b),
    deg Q<=32b, deg P_s<=34b.

Polynomial row vectors ell_E,ell_F of degree <=e satisfy E_n=ell_E(n)z_n and F_n=ell_F(n)z_n. All entries are defined by finite polynomial operations, determinants, and the recurrences above. No abstract closure assertion is required.

## 6. A scalar recurrence independent of the proposed constant

The following determinantal construction provides one recurrence annihilating BOTH E and F. It avoids choosing coefficients depending on a proposed rational constant r.

For j>=0 put

    D_j(n)=product_(h=0)^(j-1) Q(n+h), D_0=1,
    P_[j](n)=P_s(n+j-1)...P_s(n), P_[0]=I,
    R_j(n)=(ell_E(n+j)P_[j](n),
            ell_F(n+j)P_[j](n)).

These are polynomial rows of length 2N and degree <=e+34bj. The corresponding rational row is R_j/D_j. Choose the first d>=1 such that rows R_0,...,R_d are dependent over Q(n). If R_0 is zero, both output polynomials are identically zero and the construction stops with that identity. Otherwise 1<=d<=2N.

Choose any d columns making the square submatrix of rows R_0,...,R_(d-1) have nonzero determinant. The signed d-by-d minors after deleting each row from the resulting (d+1)-by-d matrix give polynomials a_0,...,a_d with

    sum_(j=0)^d a_j R_j=0, a_d nonzero.

This relation holds in all 2N columns because R_d belongs to the span of the preceding independent rows. Thus c_j=a_j D_j supplies

    sum_(j=0)^d c_j(n) E_(n+j)=0,
    sum_(j=0)^d c_j(n) F_(n+j)=0.

In particular the SAME coefficients annihilate E-rF for every rational or real constant r. The construction never uses r. A nonzero polynomial bound for the leading coefficient is

    deg c_d <= K,
    K=d(e+34bd)+32bd.

The same bound applies to all c_j. This is deliberately generous: each minor has d entries of degree at most e+34bd.

Returning to the original unreduced contractions gives the explicit recurrence

    sum_(j=0)^d c_j(n) B(n+j)^(2b)
                    (H_(n+j)-r A_(n+j))=0.

Every denominator-clearing factor is displayed. Neither a Gram denominator nor a reduced center denominator has been substituted for B.

## 7. Finite propagation and exceptional indices

Define the exact forward exceptional set

    Z_bm={integer n>=b+16: c_d(n)=0}.

It has at most K elements. All q0 and B factors are positive in this range, so they add no admissible exceptions. The set is specified by a polynomial computed by the finite elimination above, not by a numerical sampling procedure.

If H_n-rA_n vanishes at d consecutive indices starting at N0>=b+16, and c_d(n) is nonzero for every n>=N0, the recurrence proves H_n-rA_n=0 for all n>=N0 by induction. More locally, propagation continues until the first index in Z_bm. To propagate through a singular step, the next value must be supplied separately; a leading-coefficient zero cannot be canceled without further argument.

Thus, after the last forward exceptional index, at most 2N consecutive zeros force a tail identity for the actual fixed-b,m sequence. This is a proved finite-propagation implication, not a claim that such zeros occur or that the identity is impossible. It establishes an eventual bound on zero runs for every fixed-b,m sequence that is not eventually identically zero. The exceptional-set cardinality bound does not bound the location of its last member.

No backward-propagation claim is made: c_0 may vanish identically. No invertibility of the forcing transition or of its symmetric power has been assumed.

## 8. The logarithmic allocation and the missing estimates

For b(n)=floor(log n), m(n)=floor((b(n)-1)/2), the previously proved sufficient admissible range n>=2^96 is retained. Inside an integer block ceil(exp(b))<=n<exp(b+1), b,m are fixed and the recurrence just constructed applies while its output indices remain inside that block. At a boundary the dimension N, the output rows, and potentially m change. The fixed-b recurrence still defines a valid continued fixed-b family past that boundary, but that continuation is not the prescribed variable-b family.

The allocated dimension 2N and the bound K (using d<=2N) are explicit polynomials in b of degrees 30 and at most 61 respectively. Therefore they are eventually smaller than the block length, which grows exponentially in b. Nevertheless this observation alone does not prove nonstabilization or an effective bound on constant stretches of the variable-b family.

Two gaps remain. First, one needs control of the locations of roots of the actual leading polynomial c_d, or a nonsingular propagation argument covering the relevant part of each block. A degree bound controls the number of exceptional starts, not their last location. Coefficient-height/root bounds could address location, but none of suitable size has been established here. Second, one must exclude the resulting fixed-b identity H_n=rA_n on a tail, for the pertinent b,m and rational r, or derive a contradiction compatible across successive dimensions. No such identity-exclusion theorem has been proved. Even a demonstrated fixed-b identity is not an identity for the variable-b construction.

A long constant block can supply many zero windows and propagate through regular subintervals; without these missing ingredients it does not force a contradiction. Convergence of the actual centers to e+pi, and results concerning a different full-coefficient center, do not fill this gap.

## 9. Outcome and provenance

The advance is an explicit 31-coordinate rational input state, a homogeneous monomial state of allocated size binom(2b+30,30), and an r-independent scalar recurrence of order at most twice that size. Its leading polynomial has at most K admissible integer zeros. Beyond the last such zero, d consecutive equal-center values force a fixed-b tail identity.

The two symbolic calculations supplied actual controller results for the common differential operator and its conjugated recurrence, including both extreme factors. They were new algebraic derivations, not numerical scans, old-check replays, or independent audits. No finite sample implies nonvanishing or an identity in this note. Primewise normalization and reduced-coordinate denominators remain with their assigned owners. The preserved contiguous note is not modified.
