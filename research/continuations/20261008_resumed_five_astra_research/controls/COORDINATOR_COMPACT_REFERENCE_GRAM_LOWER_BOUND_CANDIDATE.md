> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Candidate: a stronger k^2 constant for the SAME compact whole determinant

Status: coordinator-derived candidate awaiting an independent external
proof audit. This is an analytic lower bound for the unchanged original
compact H, not a proof deciding e+pi or an actual content upper bound.
See the prior scoped archive/primary-literature gate. All logarithms are
natural. No numerical evidence is substituted for the proof below.

## 1. Precisely reused original interface

Keep H_k(s)=det[c_(m+j) | Lambda_k(r_(m+j)+s(-1)^(m+j))], m<2k,j<k,
c_n=a_(2n)-(-1)^n, a_0=1,a_d=1-d a_(d-1),
r_n=-(2n)!+4rho_n, rho_(n+1)+rho_n=1/(2n+1), and
Lambda_k=lcm(1,3,...,6k-5). The primitive pair still uses
G_k=gcd(|H_0,k|,|H_1,k|), q_k=|H_1,k|/G_k.

Old independently accepted A4turn19 Section7.3 gives the SAME-H identity

(-1)^k H_k(e+pi)
 = Lambda_k^k/k! integral_[0,1]^k V(y)^2 det M_y dnu^k(y),

where M_y(i,j)=L(x^(i+j) Q_y(x)), i,j<k,
Q_y(x)=product_(r=1)^k(x-y_r), L=mu-delta_(-1).
The measure mu is the pushforward of exp(-s)ds under x=(s-1)^2,
has total mass1, and for x>1 has density exp(-1-sqrt(x))/(2sqrt(x)).
The complete compact measure nu has density
(exp(sqrt(x))+4/(1+x))/(2sqrt(x)) on0<x<1, hence at least3/2.
Thus J_k^nu=(1/k!)integral V(y)^2dnu^k(y)>=(3/2)^k h_k,
where h_k=det[1/(i+j+1)]_(i,j<k).
All full corrections, signs, contact atom and maximum degree3k-2 remain.

## 2. A finite-degree extrapolation bound on a slightly larger interval

For deg p<=k-1 let E(p)=integral_[k^2,4k^2]p(x)^2dx.
The affine coordinate t=(2x-5k^2)/(3k^2) maps the exterior interval to
[-1,1]. For x in[-1,k] and k>=2, |t|<=2. The Legendre recurrence gives
|P_j(t)|<=5^j on |t|<=2: the induction step is bounded by
4*5^j+5^(j-1)<5^(j+1), with the usual0/1 base cases.
Orthogonality and Cauchy-Schwarz therefore give

 max_[-1,k]|p|^2 <= K'_k E(p), K'_k=25^(k-1)/3.

Indeed the orthonormal evaluation kernel on the exterior interval is
(3k^2)^-1 sum_(j<k)(2j+1)P_j(t)^2, at most
(3k^2)^-1*k^2*25^(k-1). This is a FINITE polynomial bound.

## 3. Pay the complete reference cutoff and all negative contributions

Define the positive reference quadratic form

 R_k(p)=integral_0^infinity p(x)^2 x^k exp(-sqrt(x))/(2sqrt(x)) dx.

On [k^2,4k^2] its density is at least
r_k=k^(2k)exp(-2k)/(4k), so R_k(p)>=r_k E(p).
For the part x<=k, use the preceding evaluation kernel and exp(-sqrt(x))<=1:

 R_k,low(p) <= K'_k E(p) * k^(k+1/2)/(2k+1).

Consequently, using e<3,

 R_k,low/R_k <= (2/75)sqrt(k)(225/k)^k <=1/4 for k>=512.

The last bound follows from225/k<1/2 and the decreasing sqrt(k)2^-k.
There is NO deletion of an uncontrolled low tail.

On x>=k, y_r in[0,1] implies
Q_y(x)>=(x-1)^k >=(1-1/k)^k x^k >=x^k/4 for k>=2.
The last elementary inequality follows from the monotonicity in k of
(1-1/k)^k, whose k2 value is1/4. Hence the positive exterior mu part
is at least (1/(4e))R_k,high >=3/(16e)R_k > R_k/16.

The ENTIRE possible loss on0<=x<=1 plus the atom at-1 is at most
(1+2^k)max_[-1,1]|p|^2 <=(1+2^k)K'_k E(p).
All other x>1 terms are nonnegative. Relative to R_k this loss is at most

 (8k/75)(450/k^2)^k <=1/32 for k>=512,

by450/k^2<1/2 and the decreasing k2^-k. Therefore, uniformly for every
actual y in[0,1]^k and every polynomial of the stated finite degree,

                 L(p^2 Q_y) >= R_k(p)/32.                 (A)

In matrix form M_y >= D_k/32 in the positive semidefinite order, where

 D_k(i,j)=(2k+2i+2j)!, 0<=i,j<k.

The substitution z=sqrt(x) proves the factorial identity exactly.
The reference maximum degree k+2(k-1)=3k-2 and its highest factorial
(6k-4)! coincide with the original physical terminal; no new row,
contact column, raw polynomial or cleared scalar is introduced.

## 4. An explicit factorial lower bound for the reference determinant

The Gram integral identity gives

 det D_k=(1/k!) integral_(0,infinity)^k
          V(z_1^2,...,z_k^2)^2 product z_i^(2k) exp(-z_i) dz_i.

For every positive z,

 V(z^2)^2=V(z)^2 product_(i<j)(z_i+z_j)^2
         >=2^(k(k-1)) V(z)^2 product z_i^(k-1).

This is just (z_i+z_j)^2>=4z_iz_j for each pair. The resulting Laguerre
Gram determinant with alpha=3k-1 has monic norms
j! Gamma(j+3k), so the established classical norm formula yields

 det D_k >= B_k := 2^(k(k-1)) product_(j=0)^(k-1) j!(3k-1+j)!.    (B)

The same proof works at k1 with equality. This is a numerical SIZE
inequality, not an integer divisibility assertion about either D or H.

## 5. The improved SAME-H lower bound and exact next constant

Combining (A), determinant monotonicity, the original conditional identity,
the complete compact nu lower density and (B), for EVERY integer k>=512,

 (-1)^k H_k(e+pi)
 >= (3 Lambda_k/64)^k h_k B_k >0.                         (C)

This includes every original index k=9^(18+32u). It is still the raw
whole determinant; the final all-prime G has not been discarded.

Stirling summation gives
 log B_k=4k^2 log k +(17log2-(9/2)log3-6)k^2+O(klogk).
For the h_k Hilbert determinant, log h_k=-2log2*k^2+O(klogk).
The previously established prime-number-theorem input log Lambda_k=6k+o(k)
then yields the proposed refinement

 log |H_k(e+pi)| >=4k^2 log k + C_H*k^2+o(k^2),
 C_H=15log2-(9/2)log3.                                   (D)

For clarity, with F(t)=t^2 log(t)/2-3t^2/4,
the constant for product j! is-3/4, that for product(3k-1+j)!
is F(4)-F(3)=16log2-(9/2)log3-21/4, and the extra binary
factor adds log2. These give (B)'s constant; h and Lambda give (D).

## 6. Actual arithmetic implications remain conditional

If at the SAME original indices one proved

 log G_k <=4k^2 log k + C_G*k^2+o(k^2), C_G<C_H,

then the actual positive primitive whole error |H_k(e+pi)|/G_k would
DIVERGE. This would retire this compact producer only, not prove rationality.
Neither such an upper bound nor primitive decay is asserted here.

Under the separately UNPROVED hypotheses that BOTH original odd contents
divide the proposed W_odd, and v2(G_k)<=A*k^2+o(k^2), A2turn7's paid
height gives C_G<=Alog2+6-4log2. The sufficient retirement condition is

 A < (19log2-(9/2)log3-6)/log2.

In particular A=3 would suffice, with positive margin
16log2-(9/2)log3-6. The odd-local certificate and actual binary upper
bound are STILL OPEN; lower binary divisors and capped3 spectra are not
upper bounds. No proof of irrationality/rationality follows from (C)/(D).

## 7. Proposed new bounded verification

Check exact D_k and B_k at k1..10, maximal factorial56, with exact
integer determinants. Verify the ordinary Laguerre Gram product separately.
Check the elementary512 cutoff inequalities by exact rational bounds.
These are NEW reference matrices, not a rerun of original compact finite
receipts and not original-index numerical evidence. An independent external
audit of the entire finite-degree comparison (A) remains the next requirement.
