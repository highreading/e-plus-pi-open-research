> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Weighted complete-source period at one extra input digit

Status: NEW parent deduction, DIFFERENT audit pending. This is conditional
on BOTH the precision-local producer theorem and A4turn14's every-precision
finite block theorem. Neither dependency is silently passed by this note.
The weaker degree-controlled E37 corollary is separate and needs only
the first dependency. No matrix solver is repeated here.

For M>=4, L<=3M, and sufficiently large original n=2 modulo3 satisfying
the reused scalar-unit law, the complete L top q coefficients modulo
3^(M-1) are determined by n modulo3^M. So are Xi and chi modulo3^M,
and xi modulo3^(M-1). The aligned window R is unchanged.

## 1. Paid matrix periodicity

Use the full-precision block theorem with q=3^M:

    T_hat_n = diag(T_hat_q,...,T_hat_q,T_hat_(n modq)) mod3^M.

This is the theorem for the ACTUAL finite Pascal transform, not a rule
invented from a size congruence. Its actual final incomplete block is
retained. Therefore, for any fixed offsets i,j from the physical right
edge, the entries T_hat_(n-i,n-j) have period q in n: the block positions
and within-block offsets are identical, including a crossing where the
entry is zero at that precision. Apply the SAME theorem to T_hat_(n+1)
to cover the complete next-column force T_hat_(n-i,n). The local R-by-R
matrix, next force k_hat, true left alignment and literal last-block
type are thus unchanged modulo3^M under n -> n+q. Their local inverses
are unchanged because the reused mod3 block law is invertible.

## 2. The factorial weight pays the Pascal continuity loss

Let

    A_r(n)=prod_{j=1}^{r-1}(n-j), r>=1.

For n=2 modulo3, precisely floor(r/3) factors in this product are
zero modulo3. Hence

    v3(A_r(n)) >=floor(r/3) >=floor(log_3 r), r>=1.       (1)

The latter inequality holds for r=1,2 directly; for r>=3 it follows on
each interval3^s<=r<3^(s+1) from3^(s-1)>=s. No exceptional high digit
of n is used. A_r is an INTEGER polynomial, so its own period modulo
3^M divides q. The raw top force is

    u_(n-r)=A_r(n)*(-2)^(n-r).

The unit power has period dividing3^(M-1), so this raw force is unchanged
modulo3^M. The deeper force support is paid by the full local theorem.

Classical Vandermonde continuity for a shift by q gives

    binom(a+q,s)-binom(a,s) in3^(M-floor(log_3 s))Z,

for1<=s<q, and an exact zero difference for s=0. In the raw-to-Pascal
force transform a term with i=n-r and b=n-r+s, 0<=s<=r-1, has coefficient
binom(n-r+s,s) times u_(n-r). Equation(1) pays EVERY possible lost digit
because s<=r-1. Thus u_hat is unchanged modulo3^M on the complete local
window. Both solved vectors v_hat and h_hat are unchanged modulo3^M.

For the raw reconstruction at a=n-r, r<=3M, a term from b=n-r+s has
the SAME coefficient binom(n-r+s,s), 0<=s<=r-1. Therefore the weighted
raw coordinates A_r*v_(n-r) and A_r*(h_(n-r)-h_known,(n-r)) are unchanged
modulo3^M, even though the UNWEIGHTED raw reconstruction may lose digits.
Do not claim that the Pascal matrix itself has period q modulo3^M.

The dense known part of h is

    h_known,(n-r)=(-1)^(r-1)*binom(n,r).

Its continuity loss is at most floor(log_3 r), also paid by(1). Hence
the COMPLETE A_r*h_(n-r) is unchanged modulo3^M for every needed r.
All these lower indices satisfy r<=3M<3^M, as required above.

## 3. Scalar division and complete q coefficients

Xi=F_fac^2-u_hat^T T_hat^-1 u_hat is unchanged modulo3^M. The first
term is zero at this precision by its original paid factorial valuation.
The scalar chi=3n*u^T h+6u_(n-1) uses only the last3M coordinates by
the full local theorem. Each product u_(n-r)*h_(n-r) is the weighted
raw coordinate from Section2 times the unchanged unit power, so chi
is unchanged modulo3^M. This retains its6u_(n-1) forcing constant.

Reuse v3(Xi)=v3(chi)=1. Dividing BOTH scalars by3 gives the SAME units
modulo3^(M-1), and then xi=chi/Xi is unchanged at exactly that precision.
No division by a nonunit is free.

The actual top coefficient is

    q_(n-r)=-A_r(n)*[3n*h_(n-r)
      +(-n-66+6)*1_(r=1)
      +2*(-n-66)/(n-1)*1_(r=2) +xi*v_(n-r)].

Both affine forcing constants and the actual unit denominator n-1 remain.
The weighted raw h and v differences are paid modulo3^M by Section2.
The xi difference is paid modulo3^(M-1) by the scalar argument. Every
other factor is integral and unchanged at sufficient precision. Thus
ALL required q_(n-r) are identical modulo3^(M-1). Their monic quotient
by x+2 is identical at the same precision with its paid endpoint.

## 4. Larger actual frozen original family

At M=33,L=72, this gives an input period3^33. The SAME saved original
j84645 jet and SAME620-coordinate window are reused. No new coefficients
are computed. The ACTUAL original progression

    j=84645+3^32*t, t>=0

lies inside j84645 modulo3^12 and has n=4^j+1 fixed modulo3^33 by LTE.
Its entire72-coefficient jet modulo3^32 is therefore frozen, conditional
on the TWO dependency proofs and this deduction. Its density is729
times the prior j84645+3^38*t family's density, and81 times the weaker
degree-controlled j84645+3^36*t family's density.

The existing irrational rotation argument still supplies infinitely
many visits to the SAME strict real RangeIII subwindow. It uses
3^32*log_3(4), irrational by unique prime factorization. The residual
chi_range/P and derived H,D,P,r remain the actual original parameters;
chi_range is different from the scalar chi in Section3. The base
j84645 itself is not asserted to meet that real interval.

This freezes only the source coefficients. Actual monomial exponents,
LOW/HIGH W, literal HIGH terminal and the complete returned physical7
Schur form remain to be evaluated. No primitive denominator saving or
rationality/irrationality conclusion for e+pi follows.
