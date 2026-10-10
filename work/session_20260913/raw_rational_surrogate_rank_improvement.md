> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational surrogates reduce the exceptional dimension to O(sqrt(n) log(n))

Date: 2026-09-13. Original root derivation.
Independent review: raw_rational_surrogate_independent_review.md passes
the complete proof without correction. Related primary approximation
theorems and their precise limits are reviewed separately in
rational_stieltjes_displacement_literature.md.

This improves the n-O(n^(3/4)) rank result by using a common rational
denominator and restricting one multiplier space to its multiples. The
denominator degree is the explicit number of directions set aside. On
the remaining family the surrogate is polynomial, so the supported
positive-weight lemma still applies. No norm estimate for multiplication
by the rational denominator is required.

The result uses the original cutoff b=ceil(2sqrt(n)) and bounds the
angle only of a specified restricted family in that metric. It does not
prove a minimum-angle bound for the full family at that cutoff. The full
actual retained matrix nevertheless has rank n-O(sqrt(n)log(n)), and
the explicit exceptional Schur reduction can use that smaller dimension.

## 1. A common-denominator approximation of the actual high-factor ratio

Retain K=K_(2n), its spectral interval [a_n,M_n],

    a_n=-4n^2+3/8,   M_n=2n+3/4,

and the original b=ceil(2sqrt(n)) cutoff, including the optional last
high-root transfer to equalize counts. The actual interlaced ratio has
the reviewed representation

    R(t)=1-sum_i omega_i a_i/(a_i+x),
    x=M_n-t,  a_i=beta_i-M_n,  omega_i>0,
    sum_i omega_i<1,  2n<=a_i<=n^2.                    (1)

All statements are for sufficiently large n with a nonempty high list;
an empty list is elementary. Also 2/n<=R(t)<=1 on the row spectrum.

Let g=2n and J=1+floor(log_2(n/2)). Assign each a_i to the bin with
index j=floor(log_2(a_i/g)), 0<=j<J. Thus

    g 2^j <= a_i < g 2^(j+1),
    rho_j=(3/2)g 2^j,
    |a_i-rho_j|<=rho_j/3.                             (2)

The chosen J also covers an a_i exactly equal to the upper overall
endpoint n^2, including when n/2 is a power of two. Unoccupied bins may
be kept; they only enlarge the common denominator harmlessly.

For every integer nu>=1, the exact finite geometric expansion gives

    a/(a+x) = a sum_(r=0)^(nu-1) (rho-a)^r/(rho+x)^(r+1)
       + [a/(a+x)] [(rho-a)/(rho+x)]^nu.               (3)

For x>=0 and a in its bin, the absolute last term is at most 3^(-nu).
Use the truncated expressions in (1) to define a rational function
P(t)/Q(t), with the common denominator

    Q(t)=product_(j=0)^(J-1)(rho_j+M_n-t)^nu,
    D=deg Q=nu J.                                    (4)

Each correction to the leading 1 has denominator degree at least one.
After multiplying by Q its degree is at most D-1. Consequently

    deg P=deg Q=D,    lc(P)=lc(Q),
    Q(K)>0,
    ||R(K)-P(K)Q(K)^(-1)||<=epsilon:=3^(-nu).          (5)

The error follows by summing (3) with the weights in (1); there is no
factor equal to the number of roots or bins. The identical bound holds
in F=F_b(K) energy, since all operators in (5) commute with F.
Neither partial-fraction coefficients nor the condition number of Q
enter (5).

Set

    nu=ceil(4sqrt(6n)/log 3),
    D=nu J=O(sqrt(n)log(n)).                          (6)

Then epsilon<=exp(-4sqrt(6n)), and D is eventually less than each
original multiplier-space dimension d_sigma=n-m_sigma.

## 2. Restrict precisely D first-channel multiplier directions

The full actual vanishing matrix is

    Z=F [R(K)W_a,W_b],
    W_sigma=[L_sigma(K)K^j v_sigma]_(0<=j<d_sigma),     (7)

with the actual offset seed v_1=e_1-(sqrt(3)/2)e_0. Restrict the first
multiplier polynomial to u_a=Q v, deg v<d_a-D, leaving the second
channel unrestricted. Multiplication by the nonzero scalar polynomial
Q is an injective map into the original multiplier space. Thus this is
an explicitly specified p'=n-1-D dimensional subfamily of the actual
full family. Its pre-F matrix and surrogate are

    X_D=[R(K)L_a(K)Q(K)K^j v_a (j<d_a-D), W_b],
    Xtilde_D=[P(K)L_a(K)K^j v_a (j<d_a-D), W_b].       (8)

The maximal polynomial degree in the surrogate's first component is
D+ell_a+(d_a-D-1)=ell_a+d_a-1, exactly the old W_a degree.
Thus its support is no larger than that of [W_a,W_b], ending at an
index s<=n+2ell_max+2=n+O(sqrt(n)). The degree h of F is at most
n/2+1. In particular s+h<2n eventually.

All surrogate columns are therefore genuine polynomial vectors in the
finite matrix, with opposite C-eigenvalues in the two channels. P is
nonzero of degree D, so those component spaces remain independent.
The supported positive-weight lemma applies with H=(2n+1)I-K and

    A_n=12sqrt(28)n^2 exp(2sqrt(6n)).                  (9)

The surrogate's separately orthonormalized F-energy angle is at least
1/A_n. This uses positive coefficients of F in powers of H and only
half of the maximal power in each quadratic term, as already reviewed.

Let E_D be the two actual restricted channels in (8), separately
orthonormalized in F energy, and let Etilde_D replace only RQ by P
while retaining those same Gram normalizations. Equations (5) and the
lower bound R>=2/n give exactly

    ||E_D-Etilde_D||<=t_n:=(n/2)epsilon.               (10)

To see explicitly why Q causes no extra loss, the error operator on
the first input polynomial w=L_a(K)Q(K)v is (R-P/Q)w. Its F norm
is <=epsilon||w||_F, while the actual norm of Rw is >=(2/n)||w||_F.
This estimate is valid on the entire restricted input space and hence
after its actual Gram normalization. It never compares v with Qv.

The same separately-normalized perturbation argument as in the closure
theorem now proves

    sigma_min(E_D)>=(1-t_n)/A_n-t_n>=1/(2A_n)          (11)

for all large n, since A_n t_n tends to zero. This is a lower bound
only for the restricted actual family at the original cutoff.

Let G_D=E_D^T E_D and let B_D denote the block diagonal individual
Gram square roots. Define

    T_D=B_D^(-1)G_D^(-1/2),
    O_D=F^(1/2)X_D T_D,   Otilde_D=F^(1/2)Xtilde_D T_D.

Then O_D has p' orthonormal columns and

    ||O_D-Otilde_D||<=eta_n:=2A_n t_n
       =O(n^3 exp(-2sqrt(6n))).                       (12)

## 3. Count the actual good directions by degree

The retained prefix L={0,...,n} has component-degree bounds
q_sigma=floor((n-sigma)/2), with q_0+q_1=n-1. A restricted
surrogate has no coordinates above n exactly when

    deg v<=q_a-ell_a-D,
    deg u_b<=q_b-ell_b.                               (13)

For all large n these bounds are positive and below the relevant
multiplier dimensions. Since deg P=D, there is no hidden degree drop.
The number of good coefficient directions is exactly

    g_good=q_a-ell_a-D+1+q_b-ell_b+1
          =n+1-ell_0-ell_1-D.                         (14)

If I_good selects them in the restricted coefficient domain, the
corresponding actual orthonormal-input subspace is
T_D^(-1) ran(I_good). Take an orthonormal frame Q_good for it.
The columns of Otilde_D Q_good lie in F^(1/2)L. Thus, if Pi is the
orthogonal projection onto that retained energy space, (12) gives

    ||(I-Pi) O_D Q_good||<=eta_n.                     (15)

The columns of O_D Q_good are orthonormal, so their retained projection
has every singular value at least sqrt(1-eta_n^2). They are actual
vectors in the full vanishing image, not merely surrogate vectors.
Consequently the original retained matrix satisfies

    rank Z_L>=g_good=n-1-k,
    k=D+ell_0+ell_1-2 in {D+b-1,D+b}
      =O(sqrt(n)log(n)).                             (16)

The exact complementary factorization through Z_H and S transfers this
rank bound to the prescribed actual high moment/evaluation block.
In fact (15) supplies the same number of near-unit retained energy
singular values after an orthonormal basis change in the full image.

## 4. The smaller full-family Schur and physical-kernel problem

Complete the good frame O_D Q_good to an orthonormal frame O_full
of the entire n-1 dimensional space F^(1/2)ran(X), with X from (7).
Such a completion exists because the reviewed full unprojected Z has
independent columns. Since X is injective, this frame is F^(1/2)X
times an invertible coefficient matrix. The completion may depend on
the whole actual Gram matrix; no conditioning estimate for that full
coefficient change is asserted or needed here.

The first g_good columns obey (15), and O_full is an isometry. The
exact block construction in raw_explicit_exceptional_schur_reduction.md
therefore applies with the present smaller k. It gives

    retained energy matrix ~ [[R_g,B_ge],[0,T_n]],
    T_n of size (k+2)-by-k,
    sqrt(1-eta_n^2)I <= R_g <= I,
    ||B_ge||<=eta_n/sqrt(1-eta_n^2),
    rank Z_L=n-1-k+rank T_n.                          (17)

Here the transformations apart from the stated bounded triangular
elimination are orthogonal in the domain and retained energy spaces.
The existence of this full-family decomposition does not assume a
minimum-angle bound for the original full pair of channels.

Its physical kernel map is still exactly

    ker H_high=J_e ker T_n^T,
    J_e=S^(-1)F[L,L]^(-1/2)U_e,
    M_e=J_e^T J_e,                                   (18)

with all the actual low-cardinal and g_l factors inside S. The
coordinates and metric now have dimension k+2=O(sqrt(n)log(n)).
This gives a smaller exact remaining problem. It does not give a
condition bound for M_e, full rank of T_n, or the required endpoint
two-plane angle.

The earlier explicit polynomial-surrogate tail test (involving L_e)
does not automatically apply to every exceptional direction of this
new full frame: the D omitted first-channel multiplier directions
were not rational-surrogate approximated here. Equation (17) and the
physical map (18) remain exact, while a new all-exceptional surrogate
comparison would require a further argument.

## 5. Scope and remaining estimates

This proof reduces the outstanding dimension using rational
approximation, positive weights, exact divisibility in a polynomial
multiplier space, and finite support. The restricted angle bound and
good-block singular bounds are unconditional for all sufficiently large
n. Numerical experiments and asymptotic guesses about cofactors are
not inputs.

The next estimates must address the specific (k+2)-by-k block in (17)
and the physical metric in (18), or supply an alternative way to control
the endpoint projection. The prime-power denominator problem remains
separate. No irrationality or primitive shrinking is asserted.
