> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Original Xi/3 unit from a finite Pascal generating identity

Status: NEW coordinator full derivation; bounded universal arithmetic
receipt pending; DIFFERENT external complete proof audit pending. This
note postdates the admissions of A4turn14 and A1turn11. Neither already
admitted packet receives it. No original dense T_n matrix is computed.

## 1. Reuse and scope check

The coordinator read ALL of A4turn13 and recovered its original forcing
definitions, ternary-unit block proof and Xi/3 scalar reduction. Scoped
current/prior response and Desktop-register searches for gamma period9,
gamma modulo9, widehat-T diagonals and bandwidth8 recovered unrelated
Gamma(2) and operator-band results, not this source-specific scalar
evaluation. The actual-scalar gate already checks primary Riordan/Hankel
background. The Pascal binomial transform and Newton generating identity
below are classical algebra, reused with a complete derivation; no global
novelty assertion or theorem from an unread search hit is made.

Retain gamma0=1,gamma1=0,gamma[r+1]=(4r+2)gamma[r]+4gamma[r-1],
T_n[a,b]=binom(a+b,a)gamma[a+b], F=(n-1)!,
u_a=F*(-2)^a/a!, v=T_n^-1u, and the COMPLETE force t from A4turn13.
Xi=F^2-u^Tv and xi=(u^Tt)/Xi. Let P_n[a,b]=binom(a,b) and
T_hat=P_n^-1 T_n P_n^-T. All domains, forces and finite endpoints stay.

## 2. A universal finite gamma period and Newton expansion

The recurrence modulo9 gives gamma0..10 equal to

    1,0,4,4,0,7,1,0,4,1,0.

Its coefficient4r+2 has period9, and the pair(gamma9,gamma10) equals
(gamma0,gamma1). Induction in the SAME recurrence proves gamma[r+9]
=gamma[r] modulo9 for ALL r>=0. Modulo3 the period is3.

Let S be forward shift. Modulo9,

    (S-1)^9 = S^9-1+3S^3-3S^6.

The period9 kills the first term; the period3 modulo3 kills the other
terms after their explicit3 factor. Hence Delta^9 gamma=0 modulo9
at every nonnegative starting index, so all higher differences vanish.
The first nine Newton coefficients g_h=Delta^h gamma0 modulo9 are

    g=(1,8,5,0,0,6,3,6,6).

Consequently the ordinary generating function obeys the exact formal
modulo9 identity

    Gamma(z)=sum_h=0^8 g_h z^h/(1-z)^(h+1).

This is an infinite coefficient identity from the recurrence, not a
finite-pattern extrapolation. Every denominator has constant term1.

## 3. Complete Pascal transformation of the bivariate matrix

The complete bivariate generating series of the INFINITE entry array
is Gamma(x+y), since sum_[a+b=r] binom(r,a)x^a y^b=(x+y)^r.
Double inverse-Pascal transformation replaces each variable by
x/(1+x),y/(1+y) and multiplies by1/[(1+x)(1+y)]. Therefore

    sum_ab T_hat[a,b]x^a y^b
      = sum_h=0^8 g_h (x+y+2xy)^h/(1-xy)^(h+1)  (mod9).       (1)

For any finite n, each transformed entry a,b<n uses ONLY raw indices
<=a,<=b. Thus(1) gives the LITERAL finite T_hat entry, with no added
row, infinite inverse assumption or extended physical terminal.

Extracting x^d y^d in(1) gives

    T_hat[d,d] = sum_h=0^8 g_h sum_a=0^floor(h/2)
        h!/[a!^2(h-2a)!] *2^(h-2a)*binom(d+a,h)  (mod9).    (2)

All factorial quotients are integers. Out-of-range binomial coefficients
are zero; for d>=0 the displayed formula also handles those cases.
The integer weight counts a copies of x, a copies of y and h-2a copies
of2xy, whose common exponent is h-a. The remaining denominator series
contributes binom(d+a,h).

For1<=r<=8, v3(binom(27,r))=3-v3(r)>=2. Vandermonde consequently
proves binom(d+27+a,h)=binom(d+a,h) modulo9 for0<=h<=8. Thus(2)
depends ONLY on d modulo27. At d=1 the literal transformed2x2 matrix
is [[1,-1],[-1,9]], so its diagonal entry is0mod9.

The original progression has n-1=4^j=1mod243. In particular d=n-1
=1mod27. We therefore PROVE at every original index

                  T_hat[n-1,n-1] =0 (mod9).                 (3)

No small n is substituted into an inverse; only the polynomial coefficient
identity and its PROVED27-period are used for this diagonal entry.

## 4. Pay the actual inverse and both forcing constants

For completeness, gamma_r=(r-1)^2 modulo3. Conjugating its Pascal-Hankel
array gives X^2+2XX^T+(X^T)^2+X+X^T+I, where X=P^-1 diag(a)P has
diagonal a and subdiagonal a. Its subdiagonal vanishes at multiples3,
so its finite blocks are

    B3=[[1,2,2],[2,0,0],[2,0,2]],
    B2=[[1,2],[2,0]], B1=[1].

Their determinants modulo3 are1,2,1. Thus ALL finite T_n are ternary
units. The original n=2mod243 has a last B2 block, with inverse
[[0,2],[2,2]]. Since n-2 is divisible by9 and n-1=1mod9, u modulo9
has only its two last entries1 and7. Therefore

    u_hat=P^-1u =e_(n-2)+6e_(n-1) (mod9).

Modulo3, use the leading inverse-image lift z=2e_(n-1). The exact
quadratic completion identity, with u_hat-T_hat z divisible by3 and
T_hat^-1 integral, gives

    u^T T_n^-1 u
      =2 u_hat^T z-z^T T_hat z (mod9)
      =6-4 T_hat[n-1,n-1] (mod9).

F^2 is zero modulo9 on the original family. Equation(3) yields

             Xi=3 (mod9), hence v3(Xi)=1.                   (4)

The original force t=3n h+(b_force+6)e_(n-1)
                   +2b_force/(n-1)e_(n-2) has BOTH displayed terms.
Their exact combination is

    u^Tt=3n*u^Th+6*(-2)^(n-1).

To pay u^Th, use the next column of the finite T_(n+1), transformed by
the SAME Pascal embedding. In its last B3 block the column above the
last entry is(2,0); B2^-1(2,0)^T=(0,1)^T modulo3. The additional
Pascal last-row entry at n-2 is binom(n,n-2)=1mod3. Pairing with
u_hat=e_(n-2) proves u^Th=1mod3. Since n=2mod3 and(-2)=1mod3,

    (u^Tt)/3=1mod3, v3(u^Tt)=1, xi=1mod3.                 (5)

No Gaussian/ternary nonunit is inverted. Equations(4)--(5) establish
the EXACT integral scalar hypothesis of A4turn13 Section12, together
with its leading unit. They do not evaluate any higher xi digit.

## 5. The shortened producer consequence and remaining correction

With the now-PROVED v3(Xi)=1, the stated72-original-coefficient source
reduction has its required scalar hypothesis. Retain its COMPLETE
projection payment: omitted factorial tail is in3^34, full endpoint
remainder in3^32, two corrected columns cost at most3^-2, and the
complete Schur perturbation lies in3^30. Thus its prefix divided by
3^26 agrees modulo81. A DIFFERENT complete audit of that projection
argument remains appropriate before common-ledger promotion.

The actual coefficients of V70 and the contracted stationary expression

    [M(deltaQ*Fhat_i*Fhat_j)-b_i^T E_act^-1 b_j]/3^29 (mod3)

remain UNEVALUATED. A short uncorrected producer is not a short projected
column; the closed observed-support obstruction remains. No actual
Delta_A, full7 matrix/force, denominator saving or e+pi proof follows.
