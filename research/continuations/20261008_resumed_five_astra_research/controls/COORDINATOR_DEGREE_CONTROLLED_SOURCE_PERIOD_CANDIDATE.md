> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Degree-controlled period for the complete local source jet

Status: a NEW coordinator corollary, conditional on the full
precision-local producer theorem. Its DIFFERENT audit is pending.
The classical binomial continuity estimate is established REUSE.
This does not compute a W-return, a physical7 Schur form, or a primitive
denominator. No old original matrix or coefficient solver is rerun.

Fix M>=4, 1<=L<=3M, H=6M-1, and the SAME aligned local window R from
the full candidate. Preserve the actual finite last block, actual force
u and next-column k_hat, top Pascal reconstruction, BOTH affine force
constants, and Xi/chi division. Assume the original n is large enough
for the candidate's factorial and support payments and its scalar unit
law. Then the complete L top q coefficients modulo3^(M-1), and their
monic quotient at x=-2, are determined by

    n modulo3^E,   E=M+floor(log_3(6M-1)).                 (1)

The same residue determines Xi and chi modulo3^M and xi modulo3^(M-1).
The window is NOT reduced. Only the input residue bound is reduced.

## 1. The complete sufficient-period lemma

For any integer a, h>=1, and E>floor(log_3 h), Vandermonde gives

    binom(a+3^E,h)-binom(a,h)
      = sum_{i=1}^h binom(3^E,i) binom(a,h-i).

Generalized binomial coefficients of integer upper arguments are integers.
For 1<=i<=h<3^E,

    binom(3^E,i) = (3^E/i) binom(3^E-1,i-1)

has 3-depth at least E-v3(i)>=E-floor(log_3 h). Thus the difference
is zero modulo3^(E-floor(log_3 h)). For h=0 it is exactly zero.
By repeated shifts, the same congruence holds for any two integer upper
arguments differing by a multiple of3^E. Negative intermediate upper
arguments do not create a denominator. In particular, (1) determines
EVERY binom(a,h) modulo3^M for 0<=h<=H and any fixed offset of a from n.

## 2. Audit every place the physical index enters

The degree-H diagonal Newton polynomials in the existing implementation
have coefficients calculated from the SAME fixed small gamma array.
Those coefficients do not depend on n. An end-window row has actual
index a=n-R+i. Every matrix entry and the next-column forcing entry uses
only binom(a,h) with h<=H. Consequently both the COMPLETE R-by-R matrix
and k_hat are identical modulo3^M under n -> n+3^E.

The window alignment depends only on n modulo3. This is unchanged.
The actual short final block is unchanged as a TYPE, with all its
entries determined by the preceding continuity payment. Its invertible
mod3 block law therefore supplies the SAME inverse modulo3^M. Nothing
here replaces the original size by its residue.

For the last3M raw force coordinates,

    u_{n-r} = (prod_{j=1}^{r-1}(n-j))*(-2)^(n-r),
    1<=r<=3M.

The finite product is an integer polynomial in n, so it is determined
modulo3^M by n modulo3^M. The unit -2 is1 modulo3 and its exponent has
period dividing3^(M-1) modulo3^M: induction on v3((-2)^(3^s)-1)
gives at least s+1. Since E>=M, its complete force factor is unchanged.
The omitted deeper force coordinates are paid by the original local
theorem; they are not newly discarded in this corollary.

The top Pascal transform taking u to u_hat uses gaps at most3M-1.
The reconstruction taking v_hat,h_hat to the needed raw v,h uses gaps
at mostmax(L,3M)-1=3M-1. Both are <=H. The explicit dense known part
of h is (-1)^(r-1)*binom(n,r), 1<=r<=max(L,3M)<=3M<=H.
The sign depends on the top OFFSET r, not the parity of an independently
chosen residue for n. Every one of these binomials is therefore paid by
Section1. This includes all last3M coordinates required for chi, even
when L<3M. No unbounded lower binomial index occurs in reconstruction.

The force products, u_hat, both solved vectors, and the needed raw v,h
are thus identical modulo3^M. Complete contractions

    Xi = F_fac^2 - u_hat^T T_hat^-1 u_hat,
    chi = 3n*u^T h + 6u_{n-1}

are identical modulo3^M. F_fac^2 is zero at this precision by its paid
valuation on the original domain. Divide Xi and chi by3 and invert the
UNIT Xi/3. This determines xi=chi/Xi only modulo3^(M-1), exactly the
required precision; there is no unpaid scalar division.

Finally each original q_{n-r} is

    -(prod_{j=1}^{r-1}(n-j)) *
      [3n*h_{n-r} +(-n-66+6)*1_{r=1}
       +2*(-n-66)/(n-1)*1_{r=2} +xi*v_{n-r}].

Here n-1 is a unit, both forcing constants remain, and every ingredient
has the preceding paid precision. All top q coefficients modulo3^(M-1)
are identical. Monic division by x+2 is an INTEGER linear operation on
these top coefficients, with the paid endpoint, so its quotient is
identical at the same precision. This proves (1), conditional only on
the stated full local theorem and original scalar/support hypotheses.

## 3. Actual original infinite subfamily at target precision32

For M=33, L=72, H=197, floor(log_3 H)=4. Hence E=37, rather than the
previous safe E=39. The SAME operative620-coordinate original receipt
at j84645 can be reused; this corollary does not produce new coefficients.
Only its input residue is reduced modulo3^37 by exact modular arithmetic.

Take the ACTUAL subset

    j=84645+3^36*t,  t>=0.                              (2)

It is still inside j=84645 modulo3^12. LTE gives
4^(3^36)=1 modulo3^37, so n=4^j+1 has the SAME required residue for
every member of (2). Thus the existing72-coefficient jet modulo3^32 is
frozen on this larger original subfamily. If the separate uniform56
candidate passes its audit, that same saved jet has its56-coefficient
representative; the present period proof does not depend on that width
candidate.

Reuse the existing density argument with alpha=log_3(4). It is
irrational because a rational relation would yield4^b=3^a. The rotation
step3^36*alpha is irrational, so this new arithmetic progression visits
each fixed strict interior real interval infinitely often. The SAME
identity D/H=1-3^(fractional_part(j*alpha)-1)+1/H then admits infinitely
many members into the original RangeIII window3/25<chi_range/P<31/250.
Here chi_range is the ORIGINAL residual parameter, not the producer
scalar contraction chi used above. All derived H,D,P,r and integer
conditions remain original. The base j84645 itself is not asserted to
meet that real window.

The new family contains the prior j84645+3^38*t family and has nine times
its density within the original arithmetic progression. This is a
source-jet reduction only. Monomial exponents, actual W, the HIGH
terminal and full physical7 returns still vary and remain to be evaluated.
