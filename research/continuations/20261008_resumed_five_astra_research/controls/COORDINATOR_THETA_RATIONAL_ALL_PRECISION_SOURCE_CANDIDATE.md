> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual theta: finite rational expansions and paid source extraction

Coordinator proof candidate, 9 October 2026. DIFFERENT audit pending.
Known recurrence/Bessel identification and standard formal-series methods
are reused. No complete determinant upper or irrationality proof follows.

## 1. Overlap and literature gate

The exact recurrence and finite physical/top/bottom identities are already
DIFFERENT-passed in FULL A4turn24/26. FULL A2turn16 section10 already
establishes the modulo4 theta anti-period; that is REUSE. Its NEW exact
parity corank is separately being audited by A4turn27. The full remaining
Schur quotient is not reduced to two rows.

Scoped current/Desktop generating-function/derivative/Neumann/source-pole
searches find the existing parity trace and distinct ternary source
operators, not the explicit all-precision actual formulas below.
Primary [OEIS A000806](https://oeis.org/A000806) and
[A278990](https://oeis.org/A278990) identify the known Bessel sequence;
their contributed recurrences are not novel here. Primary
[Rowland--Yassawi](https://arxiv.org/abs/1310.8635) gives a general
prime-power automatic-congruence framework for diagonals of rational
series. Its abstract is a scope filter; no global diagonal hypothesis or
actual determinant nonvanishing is imported. Standard formal differential
equations and precision-contractive iteration are reused, not a claimed
new general method. There is no exhaustive novelty claim.

## 2. Actual formal differential equation

Let F(Y)=sum_(n>=0) theta_n Y^n, as a FORMAL integer series. The
factorial-size coefficients give no assumed complex disk of convergence.
Summing the already proved recurrence gives exactly



$$
(1-Y-Y^2)F-2Y^2F'=1-Y.
\tag{2.1}
$$



Set S=1+Y+Y^2 and define the integral formal-series operator



$$
\mathcal T H=\frac{(Y+Y^2)H+Y^2H'}{S},\qquad
f_0=\frac{1+Y}{S},\qquad U=\frac{Y^2(1-Y)}{S^3}.
$$



The constant term of S is1, so its inverse is an integer formal series.
Differentiation preserves integer coefficients. Equation (2.1) becomes
F=f_0+2(TF-Y/S), and direct rational calculation gives T f_0-Y/S=U.
Thus, writing E=F-f_0,



$$
E=2U+2\mathcal T E.
\tag{2.2}
$$



For every h>=1, h-fold iteration leaves a remainder in 2^h Z[[Y]].
Consequently the exact finite precision law is



$$
\boxed{F\equiv f_0+
\sum_{j=0}^{h-2}2^{j+1}\mathcal T^jU\pmod{2^h}.}
\tag{2.3}
$$



The sum is empty for h=1. No division by a coefficient factorial or an
unpaid physical return occurs. This is coefficientwise precision, valid
at every actual finite index. The truncation is not an analytic limit.

If T^jU=N_j/S^(3+2j), then N_0=Y^2-Y^3 and the completely specified
INTEGER numerator recursion is



$$
N_{j+1}=(Y+Y^2)N_jS+Y^2N_j'S-(3+2j)Y^2N_jS'.
\tag{2.4}
$$



In particular deg N_j<=3+4j. The finite expansion at precision h has
denominator S^(2h-1) and numerator degree bounded linearly in h after
clearing that denominator. This is a representation bound, not a bound
on the complete determinant valuation or on automaton state complexity.

## 3. Evaluated first higher expansions, with integer carries retained

The first new numerator is



$$
N_1=3Y^3-3Y^4-4Y^5+2Y^6-Y^7.
\tag{3.1}
$$



From (2.4), its next numerator has parity



$$
N_2\equiv Y^5+Y^7+Y^8+Y^{10}+Y^{11}\pmod2.
\tag{3.2}
$$



Therefore F modulo16 is explicitly



$$
\boxed{
\begin{aligned}
F\equiv{}&\frac{1+Y}{S}+\frac{2Y^2(1-Y)}{S^3}\\
&+\frac{4(3Y^3-3Y^4-4Y^5+2Y^6-Y^7)}{S^5}\\
&+\frac{8(Y^5+Y^7+Y^8+Y^{10}+Y^{11})}{S^7}
\pmod{16}.
\end{aligned}}
\tag{3.3}
$$



The coefficient4 term must retain N_1 modulo4 at this precision;
replacing it by its parity loses actual carries. Reducing (3.3) gives
the corresponding complete modulo4 and modulo8 coefficient laws.

## 4. Integral Hasse extraction for all contact filters

Write partial^[j]F for the Hasse derivative, defined by
F(Y+Z)=sum_j Z^j partial^[j]F(Y). It has integer coefficients.
Then exactly



$$
\sum_{r\ge0}B_j(r)Y^r=\partial^{[j]}F(Y),\qquad
B_j(r)=\binom{r+j}{r}\theta_{r+j},
$$




$$
\boxed{\sum_{r\ge0}K_b(z,r)Y^r
=[Z^{z+b}](1+Z)^b F(Y+Z).}
\tag{4.1}
$$



The second identity follows by reversing t and b-t in the finite
binomial coefficient. It introduces no division by j!, nor an extra
physical return. Any coefficientwise law for F can therefore be used
at the same precision in these literal integral filters.

## 5. Paid physical-source extraction at arbitrary precision

The already passed physical formula says



$$
\binom{r+s}{r}\theta_{r+s}^{(m)}
=\sum_{v=0}^m\binom mv2^v(s+1)_v B_{s+v}(r).
\tag{5.1}
$$



Thus its row generating function is the finite sum of Hasse derivatives
partial^[s+v]F with the literal INTEGER weights in (5.1). Terms with
v+v2(v!)>=h vanish modulo2^h, since v! divides every integer rising
product (s+1)_v. In particular only finitely many small v are needed
at fixed precision, even when the original m is enormous.

For actual top base a, admitted a+j<=d-1, put Q_h(a) as in the
passed FULL26 formula2.5. The exact top CONTACT generating row is



$$
\frac{T_j^{(a)}}{o_d}
\longleftrightarrow
\sum_{\ell=0}^d\binom d\ell Q_\ell(a)
\sum_{v=0}^{a+\ell}\binom{a+\ell}{v}2^v
(j+d-\ell+1)_v\partial^{[j+d-\ell+v]}F.
\tag{5.2}
$$



This is the already paid exact top identity expressed as integral
coefficient extraction; o_d remains an actual odd determinant factor.

For arbitrary actual I, put J_l=Delta^l Q_I(0)/(2^l l!), j=p+z.
The exact bottom CONTACT generating row is



$$
\boxed{V_z^I\longleftrightarrow
\sum_{\ell=0}^p J_\ell
\sum_{v=0}^{d+\ell}\binom{d+\ell}{v}2^v
(j-\ell+1)_v\partial^{[j-\ell+v]}F.}
\tag{5.3}
$$



The physical base d+ell is unchanged. Each J_l is the already proved
integer, not a rational coefficient awaiting division. The atom is NOT
provided by F; the complete actual atom formula and rising ratios must
be included separately. Top raw indices stay <=3d-1, bottom raw indices
<=3d+1 by the passed finite formulas. Rational generating rows here
are proof devices, not extra physical data.

## 6. New actual top and atom laws modulo16

The original d has v2(d)=4. A nonzero binomial summand modulo16 with
valuation t<=3 has h divisible by 2^(4-t). Its odd product Q_h(a)
is1 modulo2^(4-t): the product length d-h is divisible by that power,
and complete odd residue blocks have product1 at the needed modulus.
For t=3 only parity is required. For t=2 the length is divisible by4;
for t=1 by8; for t=0 by16. Thus Q_h(a) may be removed modulo16 only
WITH its actual binomial weight.

The v=1 physical term has factor2. Differences from replacing a+h by a
and j+d-h+1 by j+1 contain h or d-h. Their binomial weight supplies
valuation at least4, hence the extra factor2 kills them modulo16.
The v=2 term has valuation at least3 before that binomial weight. Only
odd binomial terms can survive; their h and d-h are divisible by16,
so their remaining residues agree with a and j. Terms v>=3 have
v+v2(v!)>=4 and vanish.

It follows that, with all integer factors retained,



$$
\boxed{T_j^{(a)}/o_d\equiv K_d(j)+2a(j+1)K_d(j+1)
+4\binom a2(j+1)(j+2)K_d(j+2)\pmod{16}.}
\tag{6.1}
$$



Every nonconstant term in the exact atom formula has the factor d;
the constant odd product has length divisible by16 and is1 modulo16.
Consequently A_j^(a)=(-1)^(a+j) modulo16, still WITH the literal
R_m/R_j in the complete source-jet matrix. This is an auxiliary local
unit normalization, not an integer-pencil content division.

## 7. Application still open

Equations (2.3)-(6.1) are new actual proof candidates awaiting DIFFERENT
audit. They provide a concrete finite rational input for the full
corank-dimensional higher quotient. They do not prove its unit rank,
terminal noncancellation, an O(d log d) excess upper, the complete tied
source/index aggregation, or either whole paired coefficient valuation.
The complete constant border -f+4rho, actual least simultaneous clearer,
other-prime contents, ALL-prime G and same-index nonzero primitive whole
error are still required. No unconditional e+pi decision follows.
