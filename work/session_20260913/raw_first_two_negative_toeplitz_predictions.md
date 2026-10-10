> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact first two negative-row prediction bounds

Date: 2026-09-13. Original continuation by audit_computations.
Independent review passed in `raw_first_two_predictions_independent_review.md`.
The proof applies to the actual primitive
dual polynomial at every even degree; it makes no root-location assumption.

## 1. Exact prediction coefficients

Retain the definitions in `raw_joint_dual_hankel_and_even_root_product.md`.
Let n=2m>=2, a_k=[z^k]e^z(1+z^2)^n, and

    A=(a_(n+i-j))_(i,j=0)^n,       v=A^(-1)e_0,
    b_r=sum_(j=0)^n a_(n-r-j)v_j,        0<=r<=n.              (1)

Set a_k=0 for k<0. The first row of Av=e_0 gives b_0=1.
All coefficients in (1) are real rational numbers. The exact identity is

    V(1+t)/V(1)=sum_(r=0)^n n!/(n+r)! b_r t^r.               (2)

To prove it, set a_k(x)=[z^k]e^(xz)(1+z^2)^n and use
q=n!V(1)v. The joint Hankel identity gives
sum_j a_(2n-j)(1+t)v_j=t^n V(1+t)/(n!V(1)). Expand
a_k(1+t)=sum_l t^l a_(k-l)(1)/l!. Terms with 0<=l<n
vanish by the rows n-l of Av=e_0; the l=n term is 1. The remaining
terms are b_(l-n), and no term with l>2n survives. Cancelling t^n
proves (2) polynomially, including at t=0.

## 2. Complex-weight bound by an exact base-weight distance

On the unit circle put

    w(theta)=|1+e^(2i theta)|^(2m),
    f(theta)=e^(e^(i theta))w(theta),
    ||p||_w^2=(1/(2pi)) integral w(theta)|p(e^(i theta))|^2 dtheta.

The Toeplitz equation gives <z^k,v>_f=0 for 1<=k<=n, where
the inner product notation means integration against f and is not
asserted Hermitian. Hence

    b_r=<z^(-r)-p,v>_f       for every p in span(z,...,z^n).

Let d_r be the distance of z^(-r) to this span in the positive
base norm ||.||_w. Since |f|<=e w,

    |b_r|<=e d_r ||v||_w.                                   (3)

The previously proved sector bounds give, with
c_m=((2m)!)^2/[m!(3m)!],

    Re A>=e^(-1)cos(1)G0,
    v_0=(A^(-1))_(0,0)<=e c_m/cos(1).

Also v*Re(A)v=Re(v*e_0)=v_0, so
||v||_w<=e sqrt(c_m)/cos(1). Therefore

    |b_r|<=C sqrt(c_m)d_r,        C=e^2/cos(1).               (4)

This estimate retains the complex weight. Replacing it directly
by positive orthogonality would not justify the same conclusion.

## 3. Exact first distance

The weight w is invariant under z -> -z, so the even and odd
Laurent subspaces are orthogonal. For r=1 only the odd positive
powers z,z^3,...,z^(2m-1) matter. Multiplication by z is an isometry;
then the substitution u=z^2 reduces the squared distance to that
of 1 from span(u,...,u^m), for the circle weight |1+u|^(2m).

Let

    T_L=(binom(2m,m+i-j))_(i,j=0)^(L-1),
    eta_j=j!(2m+j)!/(m+j)!^2.

The binomial Toeplitz determinant proved in the preceding note
gives det T_L=product_(j=0)^(L-1) eta_j. Consequently

    d_1^2=det T_(m+1)/det T_m=eta_m=1/c_m.                   (5)

This is the Schur-complement norm of the actual omitted negative
power, not the norm of that power before projection.

## 4. Exact second distance from a two-by-two Schur complement

For r=2 only the positive even powers z^2,...,z^(2m) matter.
Multiplication by z^2 and substitution u=z^2 reduce d_2^2 to

    dist_w^2(1, span(u^2,u^3,...,u^(m+1))).

Thus it is entry (0,0) of the leading two-by-two Schur complement
of T_(m+2), after the coordinates 2,...,m+1 have been eliminated.
The missing coordinate u^1 must not be filled in for free.

Here are the required inverse entries, proved directly from minors.
For arbitrary K>=1 let R=T_(K+1)^(-1). Then

    R_00=1/eta_K,
    alpha:=R_01/R_00=-Km/(m+K),
    beta:=R_(0,K)/R_00=(-1)^K m/(m+K).                       (6)

For beta, its cofactor is (-1)^K times the shifted binomial
Toeplitz determinant with parameters m-1,m+1 and size K. Dividing
by the unshifted determinant telescopes to m/(m+K).

For alpha, compare the cofactor minor with rows {0,2,...,K} and
columns {1,...,K} to the unshifted minor with rows and columns
{1,...,K}. Factor (2m)!/[(m-1+x)!(m+K-x)!] from a row indexed x.
The remaining columns are polynomials of degree at most K-1;
their evaluation determinant is a fixed constant times the
Vandermonde. Moving x=1 to x=0 changes the Vandermonde by K
and the row factor by m/(m+K). The cofactor sign is negative.
This proves alpha including zero binomial entries.

The leading and trailing K-by-K submatrices of T_(K+1) coincide,
and its inverse is persymmetric. Computing their inverse entries
by the two opposite Schur complements gives

    R_11=R_00+(R_01^2-R_(0,K)^2)/R_00
        =R_00(1+alpha^2-beta^2).                            (7)

In detail, the common entry of T_K^(-1) is both
R_00-R_(0,K)^2/R_00 and R_11-R_01^2/R_00. This proves (7)
without a formula for all entries of the inverse.

The inverse of the leading two-by-two block of R therefore has
entry (0,0) equal to

    eta_K(1+alpha^2-beta^2)/(1-beta^2).

Since eta_K/eta_(K-1)=1-m^2/(m+K)^2=1-beta^2, setting K=m+1
now gives the exact answer

    c_m d_2^2=1+m^3(m+2)/(2m+1)^2.                          (8)

All inverses are of positive definite circle Gram matrices. No
unproved leading minor or actual HP normality is used in this
distance computation.

## 5. Actual derivative and reciprocal-root-sum bounds

Combining (4), (5), and (8) yields

    |b_1|<=C,
    |b_2|<=C sqrt(1+m^3(m+2)/(2m+1)^2)<=C(m+2)/2.            (9)

For the last inequality use (2m+1)^2>=4m^2, followed by
1+m(m+2)/4<=(m+2)^2/4. From the exact factorials in (2),

    |V'(1)/V(1)|<=C/(n+1),
    |V''(1)/V(1)|<=C(m+2)/[(n+1)(n+2)]<=C/(n+1).            (10)

These estimates hold for every even n>=2. They do not imply local
uniform convergence on a fixed disk without control of higher
coefficients; that is a separate all-r prediction question.

If r_j are all roots of V with multiplicity, V(1)!=0 is already
proved and the logarithmic derivative identities give

    sum_j 1/(1-r_j)=O(1/n),
    sum_j 1/(1-r_j)^2=O(1/n).                                (11)

The second formula follows from (V'/V)^2-V''/V. These are complex
power sums; they do not bound a sum of absolute values, an individual
root distance, or the signed whole-error integral. The primitive
endpoint gcd remains unchanged.

## 6. Existing normalization control and scope

The saved n=2 example has V(t)=49t^2-64t+940 and V(1)=925.
Formula (2) gives exactly

    b_1=102/925,        b_2=588/925.

For m=1, the base distances in (5), (8) are d_1^2=3/2 and
d_2^2=2, respectively. These equal the direct projections for
the weight |1+u|^2; in the latter case <1,u^2>=0.
They agree with the existing n=2 Toeplitz inverse entry 588/925.
No new canonical degree or root scan was performed. The all-index
argument is the exact minor calculation, not these controls.
