> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A two-function Padé equation with a quadratic accessory polynomial

Date: 2026-09-13. Original continuation by audit_computations.
Independent review pending. All statements concern the actual even
subsequence n=2m>=2. No new canonical degree is constructed.

This is a two-dimensional equation for the normalized Toeplitz pair
C and exp(z)(1+z^2)^n v. It is distinct from both the selected type-I
three-function equation with a cubic, and the simultaneous dual
three-function equation with a quadratic. The latter has functions
Qhat, Pe exp(-z), Pa-Qhat atan(z). Neither is being renamed here.

The inspected inputs were raw_joint_dual_hankel_and_even_root_product.md,
raw_dual_arctangent_toeplitz_second_kind.md, the reviewed product/Mahler
continuation, and raw_dual_origin_defects_and_scalar_equation.md. The
proof below uses no unproved accessory bounds or polynomial root ansatz.

## 1. The actual Padé pair and its normalization

Set D=1+z^2 and E=exp(z)D^n. Retain

    v=A^(-1)e_0=q/(n!V(1)),       v_0=v(0)>0,
    B(z)=sum_(r=0)^n b_r z^r,     b_0=1,
    C(z)=z^n B(1/z).                                      (1)

The passed second-kind and prediction identities give b_n=v_0.
Consequently C is monic of degree exactly n, C(0)=v(0)=v_0,
and deg v<=n. Both polynomials have rational real coefficients.
The exact coupled-origin identity is

    E(z)v(z)-C(z)=z^(2n+1)G_n(z),                         (2)

where G_n is entire. This is the ordinary [n/n] Padé problem for
the n-dependent analytic function E. The error in (2) is not the
original simultaneous exponential error Re=Qhat exp(z)-Pe.

Equivalently, if a_j=[z^j]E and A_ij=a_(n+i-j), 0<=i,j<=n,
the coefficient equations at degrees n,...,2n are Av=e_0.
The known sector argument proves that A is invertible for even n.

C and v are coprime, including over C. Indeed a common nonconstant
factor h would have h(0)!=0. Dividing (2) by h would give

    E v_tilde-C_tilde=O(z^(2n+1)),
    deg C_tilde<=n-1,             deg v_tilde<=n-1.

The coefficients at degrees n,...,2n would then give A v_tilde=0,
with the coefficient vector padded by zero to length n+1. This
contradicts invertibility and v_tilde!=0. No normality theorem for
an unrelated Padé table is needed.

## 2. A nonzero quadratic and exact degree/order defects

Use W(f,g)=fg'-f'g and define the polynomial

    Kcal=D(Cv'-C'v)+(D+2nz)Cv.                            (3)

Direct differentiation gives

    W(C,Ev)=exp(z)D^(n-1) Kcal.                           (4)

The degree of Kcal is at most 2n+2. It is nonzero: otherwise
Ev/C would be constant near zero, hence Ev=C, which would make
exp(z) rational after division by the nonzero polynomials D^n v.

Put F=Ev-C and M=2n+1. If ord_0 F=M+t, then C(0)!=0 gives

    ord_0 W(C,F)=M+t-1=2n+t,

with nonzero leading coefficient (M+t)C(0)[z^(M+t)]F.
Since W(C,F)=W(C,Ev), equation (4) proves

    Kcal=z^(2n) K(z),    0!=K in Q[z],
    t=ord_0 K <= deg K=:k <=2,
    ord_0(Ev-C)=2n+1+t.                                  (5)

In particular this derivation does not assume that the first
omitted Padé coefficient is nonzero.

Let d=deg v, with top coefficient v_d. The term z^2 Cv in (3)
is uniquely of highest degree n+d+2; all other terms have degree
at most n+d+1. Comparing with z^(2n)K proves the exact infinity
ledger

    d=n+k-2,                 [z^k]K=v_d.                 (6)

Thus the only possible denominator degrees are n-2,n-1,n.
The nonzero accessory K here is not either earlier accessory
polynomial, despite the same upper bound of two on its degree.

## 3. An exact bounded-degree second-order scalar equation

Define the rational logarithmic derivative

    h=E'/E=1+2nz/D

and

    N=C'v''-C''v'+2h C'v'+(h'+h^2)C'v-h C''v.             (7)

Then W(C',(Ev)')=E N. The standard two-function determinant
identity gives

    W(C,Ev)y''-W(C,Ev)'y'+W(C',(Ev)')y=0

for both y=C and y=Ev. After multiplying by the exact rational
factor which makes its leading coefficient zDK, it becomes

    A2 y''+A1 y'+A0 y=0,                                 (8)

where

    A2=z D K,
    A1=-{[(z+2n)D+(n-1)zD']K+zD K'},
    A0=D^2 N/z^(2n-1).                                   (9)

All three A_j are polynomials over Q. In particular the numerator
in A0 can be written without rational functions as

    D^2(C'v''-C''v')+2D(D+2nz)C'v'
      +[D^2+4nzD+2nD+4n(n-1)z^2]C'v
      -D(D+2nz)C''v.                                    (10)

Its required origin divisibility is essential: replace Ev by
C+F in W(C',(Ev)'). Then W(C',F') has order at least M-2=2n-1.
Multiplication by D^2/E, a unit at zero, proves that the polynomial
in (10) is divisible by z^(2n-1). This is not merely a formal
division of a displayed polynomial.

The monic first-derivative coefficient is

    A1/A2=-1-2n/z-(n-1)D'/D-K'/K.                         (11)

At infinity C'/C=n/z+O(z^-2) and C''/C=O(z^-2). Substituting
the polynomial solution C into the monic equation gives

    A0/A2=n/z+O(z^-2).                                   (12)

Hence the degree bounds, including the actual top coefficients,
are

    deg A2=deg A1=k+3<=5,    deg A0=k+2<=4,
    lc(A2)=K_k,             lc(A1)=-K_k,
    lc(A0)=nK_k.                                          (13)

No lower bound, compactness, or n-limit for the coefficients of K
or A0 follows from their bounded degrees. Those are separate
analytic questions.

Where A2 does not vanish, the full solution space of (8) is exactly
the constant span of C and Ev, since their Wronskian is nonzero.
For K(0)!=0 the origin orders are 0 and 2n+1, and the indicial
polynomial is r(r-2n-1). With an origin defect, use the exact
orders 0 and 2n+1+t from (5); do not apply the generic leading
coefficient formula before canceling common powers of z.

## 4. First-order pair constraints and exact reconstruction

The following bounded-degree bilinear identity is equivalent to
the actual Padé conditions, once the normalization is specified:

    D(Cv'-C'v)+(D+2nz)Cv=z^(2n)K,                        (14)
    C monic of degree n, deg v<=n,
    C(0)=v(0)!=0, deg K<=2.

Necessity was proved above. Conversely (14) gives

    (Ev/C)'=exp(z)D^(n-1) z^(2n) K/C^2.                  (15)

The ratio has value one at zero. Integrating locally therefore
gives Ev-C=O(z^(2n+1)); the monic coefficient of C at degree n
then yields Av=e_0. Invertibility identifies the unique actual v,
and C is its Taylor numerator. Thus (14) is not an equation for
an unspecified family with a free normalization or connection.

The exact local error representation is

    Ev-C=C(z) integral_0^z
          exp(t)D(t)^(n-1)t^(2n)K(t)/C(t)^2 dt.            (16)

It continues along paths avoiding the zeros of C. Its integrand
is the derivative of the globally meromorphic function Ev/C,
so all its closed-path periods, including residues at C roots,
vanish. Formula (16) itself does not bound an integral continued
near those roots, nor the separate arctangent endpoint functional.

## 5. Local multiplicities and actual negative-real zero counts

At an ordinary point a outside {0,i,-i}, coprimality implies that
C(a) and Ev(a) are not both zero. The local echelon orders of
their two-dimensional span are consequently

    0,                    1+ord_a K.                    (17)

Indeed their Wronskian has order ord_a K there. Every nonzero
solution therefore has vanishing order at most three at such a
point. In particular any root of C or v there has multiplicity
1+ord_a K and is simple if K(a)!=0. This is a local multiplicity
statement, not a bound on the number of roots in an interval.

For clarity, the fixed points +/-i can also be described exactly.
At xi let r=ord_xi C, s=ord_xi v. Coprimality gives min(r,s)=0.
Real coefficients and deg C=n imply r<=n/2<n+s. The two distinct
local orders are r,n+s. Comparing their Wronskian order with (4)
gives

    r+s=ord_xi K.                                        (18)

If K vanishes at i, reality and deg K<=2 force K to be a nonzero
multiple of D; each fixed root is simple and r+s=1 there.

There is also a global result on the negative real axis. The
independently passed second-kind theorem gives

    v(x)>0, B(x)>0   on [-1,0].                           (19)

Since n is even, C(x)=x^nB(1/x)>0 for x<=-1. On that half-line
the real function R=Ev/C is analytic, tends to zero at -infinity,
and has derivative (15). Its derivative has at most k zeros
counted with multiplicity, all supplied by K.

Here one can use the endpoint at infinity in Rolle's argument:
if R has distinct finite roots x1<...<xr of total multiplicity d,
its derivative has at least d-r zeros at the roots and r-1 between
them. There is one more derivative zero before x1. To see the
last assertion, choose a point x0<x1 with R(x0)!=0 and then a
sufficiently negative L with |R(L)|<|R(x0)|. A maximum or minimum
of nonzero absolute magnitude on [L,x1] occurs in its interior.
Thus the derivative has at least d zeros in total. It follows that

    v has at most k<=2 negative real roots,
    all in (-infinity,-1), counting multiplicity.          (20)

In reciprocal form, U has at most two negative real roots, all
in (-1,0); the previously proved exclusion on (-infinity,-1]
is retained. A possible root of U at zero is not counted here.

For C in (-1,0), use S=C/(Ev). Its denominator is strictly positive
there by (19), and

    S'=-exp(z)D^(n-1) z^(2n)K/(Ev)^2.

Thus S' has at most k zeros counted with multiplicity. Rolle's
theorem gives at most k+1 zeros of S with multiplicity. Both
endpoint values S(-1) and S(0)=1 are positive, so the total
multiplicity is even. Since k<=2, it is at most two, and is zero
if k=0. There are no C roots at or below -1 by (19). Consequently

    C has at most two negative real roots, all in (-1,0),
    B has at most two negative real roots, all below -1.    (21)

These proofs make no assertion about the zeros of the real part
of U on a complex arc. That real part already changes sign in
the frozen degree-two example, and (20)-(21) do not remove it.

## 6. The unchanged signed arctangent connection and arithmetic

Retain the clockwise left unit semicircle gamma_L from -i to i,
and the exact partial Cauchy transform

    J_n(a)=(1/(2i)) integral_gamma_L
       D(z)^n v(z)/[z^(2n+1)(z-a)] dz.

The passed whole-error identity is

    Ra(1)/(n!V(1))=J_n^(n)(1)/n!,
    a_n=(2n+1)! J_n^(n)(1)/n!.                           (22)

Equation (2) lets one write the numerator in (22) as
exp(-z)[C(z)+z^(2n+1)G_n(z)]. Equations (14)-(16) determine this
tail through the same actual Padé pair, but do not estimate its
signed incomplete-circle integral. In particular a bounded-degree
equation is not a bound on its connection values.

The current exact endpoint ledger remains

    Re(1)+4Ra(1)=n!V(1)/(2n+1)!
        {exp(1/2)[1+theta_n]+4a_n},   theta_n=O(1/n).

With Z=Qhat(1), N=Pe(1)+4Pa(1), and g=gcd(|Z|,|N|), the actual
primitive form is sign(Z)[Re(1)+4Ra(1)]/g. Nothing in this note
bounds g or proves that this form shrinks. The concrete smaller
analytic problem is now to control the actual two-function
quadratic equation's partial-contour connection (22), rather than
an arbitrary solution of a three-function accessory equation.

## 7. Bounded normalization control

The checker check_raw_two_function_dual_existing.py uses only
the frozen n=2 data already present in the project. It checks
the Padé order, coprimality, quadratic factorization, all three
polynomial coefficients in (9), and both scalar-equation solutions.
Its exact output is raw_two_function_dual_existing_checks.json.
It is a normalization control, not the proof of any all-index claim.
