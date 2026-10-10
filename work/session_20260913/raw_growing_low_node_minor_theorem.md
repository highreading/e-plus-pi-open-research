> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A growing low-node minor with uniformly controlled endpoint errors

Date: 2026-09-13. Original continuation by audit_sources.
Independent review in `raw_growing_low_node_root_review.md`
passes the full theorem, including the sharpened excess-degree
Cauchy-Binet estimate and its growing-node scope.

Independent root review passes in `raw_growing_low_node_root_review.md`.

This note quantifies the fixed-size endpoint determinant argument
for the actual consecutive low nodes ell=0,...,m-1, with m tending
to infinity. It proves eventual nonvanishing for, in particular,

    m=floor((log n)^(1/3)).

All selected rows lie in the actual high interval n+1,...,2n-1.
The proof tracks the node dependence of the eigenfunction Taylor
coefficients, the growing-order endpoint moments, and every error
before division by the leading determinant. No fixed-m implicit
constant is reused as a uniform estimate.

## 1. The actual matrix and quantitative conclusion

Use the normalization from the reviewed fixed-size theorem:

    L_k=integral_0^1 E_k(x) dx>0,
    M_(k,ell)=<E_k,psi_ell> / [L_k psi_ell(1)]
       =g_ell p_k^(ell mod 2)(xi_ell)/[L_k psi_ell(1)].

The actual endpoint values and amplitudes are nonzero. For m>=2
define, for i,j=1,...,m,

    t_i=1+i/(m+1),  k_i=floor(n t_i),
    x_i=t_i^(-1/2),  zeta_j=xi_(j-1),
    q=m(m-1)/2,  epsilon=n^(-1/2),
    A_(n,m)=(M_(k_i,j-1))_(i,j=1)^m.                  (1)

The proportions are evenly spaced in the interior of [1,2].
For n>=m+1 the rows are distinct and belong to n+1,...,2n-1.
Choosing the endpoint-inclusive equally spaced grid instead
gives the same analytic estimates, but (1) keeps every row
inside the prescribed high interval.

There are absolute constants C and n_0 such that, whenever
n>=n_0 and q+1<=n^(1/8),

    det A_(n,m)
       = L_m n^(-q/2) (1+R_(n,m)),

    L_m= [(-1)^q / product_(r=0)^(m-1) r!]
             Delta(zeta_1,...,zeta_m) Delta(x_1,...,x_m)>0,

    |R_(n,m)| <= n^(-1/2) exp(C m^2 log(m+1)).         (2)

Here Delta(v)=product_(i<j)(v_j-v_i). In particular, for
m=floor((log n)^(1/3)), the relative error in (2) is
n^(-1/2+o(1)) and the determinant is positive for all
sufficiently large n. More generally this conclusion holds
whenever m^2 log(m+1)=o(log n), including every fixed power
m=floor((log n)^c) with 0<c<1/2.

This is an actual growing low-node rank statement. The exact
normalization by L_k, g_ell, and psi_ell(1) is retained; it is
not a singular-value statement for the unscaled full high matrix.

## 2. Uniform endpoint coefficients and derivatives

For an actual node put

    f_ell(y)=psi_ell(1-y)/psi_ell(1)
            =sum_(r>=0) a_r(xi_ell)y^r.

The reviewed endpoint equation gives a_0=1, negative-index
coefficients zero, and

    r^2 a_r=[r(r-1)+1-xi]a_(r-1)-a_(r-2)+a_(r-3).     (3)

Its leading coefficient is exactly (-1)^r/(r!)^2. Let
A_r=max_(0<=h<=r)|a_h(xi)| for real xi>=0. Equation (3) gives

    A_r <= [1+(xi+3)/r^2] A_(r-1).

For s=ceil(sqrt(xi+3)), split the resulting product at s.
For h<=s, 1+s^2/h^2<=2s^2/h^2, while for h>s the sum of
s^2/h^2 is at most s. Using s!>=(s/e)^s proves

    product_(h>=1)(1+(xi+3)/h^2)
       <= exp((log 2+3)s) <= exp(4s).                 (4)

For ell<m, the actual spectral enclosure gives 0<xi_ell<=m^2.
Thus, with E_m=exp(4m+8),

    |a_r(xi_ell)| <= E_m, every r>=0, ell<m.           (5)

This bound is uniform in the Taylor order, not only for fixed r.
On 0<=y<=1/2, termwise differentiation and the geometric series
give

    |f_ell^(s)(y)|
       <= E_m sum_(r>=s) r!/(r-s)! y^(r-s)
       = E_m s!/(1-y)^(s+1)
       <= E_m s! 2^(s+1).                            (6)

The actual eigenfunction has reflection parity ell. Therefore
f_ell(1-y)=(-1)^ell f_ell(y), and the same absolute derivative
bound holds on the other half of the interval. Consequently

    ||f_ell^(s)||_[0,1] <= E_m s! 2^(s+1),

    |f_ell(y)-sum_(r=0)^R a_r(xi_ell)y^r|
          <= E_m 2^(R+2) y^(R+1), 0<=y<=1.            (7)

In particular ||f_ell||_infinity<=2E_m. These estimates do
not divide by an unbounded unknown endpoint value: the
endpoint normalization is controlled directly by (3), and
reflection transfers that control across the interval.

## 3. Endpoint moments through a growing Taylor order

Put

    mu_r(k)=integral_0^1 (1-x)^r E_k(x) dx / L_k.

There is an absolute constant C_0 such that, for all sufficiently
large k and integers 0<=r<=k^(1/8),

    mu_r(k)=r! k^(-r/2)(1+delta_(r,k)),
    |delta_(r,k)| <= C_0(r+1)^2/sqrt(k).                (8)

For r=0, mu_0=1 exactly. Here is a proof uniform in this range.
The already reviewed Borel coefficient estimate on [1/2,1]
has relative error O(k^(-1/2)) with an absolute constant and
common shape x^(-1/4) exp(2 sqrt(kx)). Multiplying by the
nonnegative (1-x)^r preserves that relative precision.

For the main shape integral substitute u=sqrt(x) and then
v=2 sqrt(k)(1-u). With V=2(1-1/sqrt(2))sqrt(k), it becomes

    exp(2sqrt(k)) k^(-(r+1)/2)
       integral_0^V exp(-v) v^r
          (1-v/(2sqrt(k)))^(1/2)
          (1-v/(4sqrt(k)))^r dv.                      (9)

Both final factors are between zero and one. The difference
of their product from one is at most (r+2)v/(4sqrt(k)), by
1-sqrt(1-z)<=z and the elementary Bernoulli inequality.
Its integral is at most

    [(r+2)(r+1)/(4sqrt(k))] r!.

The missing gamma tail is bounded by

    integral_V^infinity exp(-v)v^r dv
       <= 2^(r+1) exp(-V/2) r!,                       (10)

which is exponentially small in sqrt(k) uniformly for
r<=k^(1/8). This proves the claimed relative precision for
the endpoint interval.

On [0,1/2], the global Borel bound gives
E_k(x)<=C exp(2 sqrt((k+1)x)). Its contribution divided by
the proposed numerator scale is at most

    C k^(r/2+3/4) exp(-c sqrt(k))/r!.

This is also exponentially small uniformly for r<=k^(1/8),
since r log(k)=o(sqrt(k)) uniformly in that range. Dividing
the resulting numerator estimate by its r=0 estimate proves
(8), after increasing an absolute constant. This proof
retains the k-dependent tail; a fixed-r endpoint estimate
alone would not justify (8).

For the rows in (1), k_i lies in [n,2n]. Integer rounding
changes k_i^(-r/2) relative to (nt_i)^(-r/2) by O(r/n),
uniformly for the displayed range. Thus, for 0<=r<=q+1,

    mu_r(k_i)=epsilon^r r! [x_i^r+e_(i,r)],
    |e_(i,r)| <= C_0(r+1)^2 epsilon.                  (11)

Increasing n_0 if necessary, q+1<=n^(1/8) makes all the
relative errors in (8) at most one. In particular

    0<=mu_r(k_i)<=2r! epsilon^r.                       (12)

The constants in (8)-(12) are independent of m, i, and r
within their specified ranges.

## 4. Both Vandermondes have explicit uniform lower bounds

The actual node enclosures imply, for 0<=a<b<m,

    xi_b-xi_a >= b(b+1)-a(a+1)-1/4 >= 7/4>1.

Hence Delta(zeta)>=1. The derivative of t^(-1/2) on [1,2]
has absolute value at least gamma=1/(4sqrt(2)). The equally
spaced proportions therefore give

    |x_j-x_i| >= gamma (j-i)/(m+1).

Put P_m=product_(r=0)^(m-1)r! and
H_m=((m+1)/gamma)^q. Since product_(i<j)(j-i)=P_m,

    |Delta(x)| >= H_m^(-1) P_m,
    L_m=Delta(zeta)|Delta(x)|/P_m >= H_m^(-1).          (13)

The signs in (2) follow because the x_i decrease while the
zeta_j increase. These lower bounds are deliberately
conservative, but they track the dependence on the growing
number of nodes and prevent division by an unspecified
Vandermonde constant.

## 5. Quantitative Cauchy-Binet and the integrated Taylor error

Take R=q. Equations (7), (11), and (12) give

    A_(n,m)=U C+E,
    U_(i,r)=mu_r(k_i), C_(r,j)=a_r(zeta_j), 0<=r<=q,

    max|E_(i,j)| <= E_m 2^(q+3) (q+1)!
                                      epsilon^(q+1). (14)

All actual entries of A have modulus at most 2E_m. Also
q epsilon<=1/2 for the stated range and large n, so
sum_(r=0)^q mu_r(k_i)<=2 sum_(r=0)^q(q epsilon)^r<=4.
Thus the entries of U C have modulus at most 4E_m.
Determinant multilinearity on this bounded set proves

    |det A-det(U C)|
       <= m m! (4E_m)^(m-1) E_m 2^(q+3)(q+1)!
                                      epsilon^(q+1). (15)

This is an entry-error estimate made before invoking
Cauchy-Binet. Its Taylor order q is essential.

In Cauchy-Binet the distinguished degree set is 0,...,m-1.
For it, factor epsilon^r r! from moment column r. The
remaining matrix is (x_i^r+e_(i,r)), with entry error at
most C_0 m^2 epsilon. Its determinant differs from Delta(x)
by at most

    C_0 m^3 m! 2^(m-1) epsilon.                       (16)

The coefficient determinant is exactly

    det(a_r(zeta_j))_(r=0,...,m-1;j=1,...,m)
       =(-1)^q Delta(zeta)/P_m^2.

Dividing the distinguished term's error by its nonzero
leading term and using (13) bounds the relative error by

    epsilon C_0 m^3 m! 2^m H_m.                       (17)

Every other Cauchy-Binet degree set has degree sum q+d with
d>=1. Write its ordered indices as r_1<...<r_m. Since
r_s>=s-1 and r_s<=q,

    product_(s=1)^m r_s! <= P_m q^d.

Indeed r_s!/(s-1)! is a product of exactly r_s-(s-1)
integers, each at most q. Thus (12) and (5) give respectively
the determinant bounds

    m! 2^m P_m epsilon^q (q epsilon)^d,
    m! E_m^m.

There are at most (q+1)^m degree sets. As q epsilon<=1/2,
their entire sum divided by L_m epsilon^q is bounded by

    epsilon q(q+1)^m (m!)^2 2^m P_m E_m^m H_m.         (18)

Retaining this excess degree is useful: replacing every
factorial by q! would needlessly lose an extra factor of m
in the logarithm of the error bound.

Likewise (15) divided by that leading scale is bounded by

    epsilon m m! (4E_m)^(m-1) E_m
                          2^(q+3)(q+1)! H_m.          (19)

These are explicit uniform bounds for the three errors.
Since q<=m^2/2, log(E_m)=4m+8, and log(H_m)=O(m^2 log(m+1)),
the sum of (17)-(19) is at most

    epsilon exp(C m^2 log(m+1))                       (20)

for an absolute C. Here log(P_m)=O(m^2 log(m+1)), while
log((q+1)!)=O(m^2 log(m+1)) controls the Taylor error.
Equations (14)-(20) prove (2). No fixed-m determinant
continuity constant or hidden count of Taylor terms remains.

## 6. A quantitative singular-value consequence for this block

Suppose the relative bound in (2) is at most 1/2. Retaining
only Taylor degrees 0,...,r-1 gives a rank-at-most-r matrix.
The derivative bound (7), positive moment bound (12), and
the matrix norm bound by m times its largest entry show that
its error is at most

    m E_m 2^(r+2) r! epsilon^r, 0<=r<=m-1.             (21)

For r=0 the zero approximant and ||A||<=2mE_m also satisfy
this inequality. In decreasing singular-value order, put

    U_m=m E_m 2^(m+1)(m-1)!.

Then all upper bounds read s_j<=U_m epsilon^(j-1).
The determinant lower bound (13) and (2) gives

    s_j >= [1/(2 H_m U_m^(m-1))] epsilon^(j-1).

In particular, with a further absolute constant C,

    exp(-C m^2 log(m+1)) n^(-(j-1)/2)
       <= s_j(A_(n,m))
       <= exp(C m log(m+1)) n^(-(j-1)/2).              (22)

This quantifies the fixed-size singular-value hierarchy in
the growing range just proved. It is not a polynomial-in-n
condition bound uniform for arbitrarily growing m; the
factor n^((m-1)/2) in the condition number is retained.

## 7. Consequences and remaining obstruction

For m=floor((log n)^(1/3)), the selected actual low-node
columns have a nonzero square minor in the prescribed high
rows for all sufficiently large n. Restoring their nonzero
column amplitudes and row masses preserves this rank
conclusion. The relative determinant formula (2) retains
all normalization factors before such restoration.

This result concerns a genuinely growing initial set of
consecutive low nodes. It is separate from the sparse bulk
node theorem and does not by itself prove independence of
the union of the two column families. Nor does it estimate
the full high-row inverse, the physical amplitude-weighted
cardinal determinant, or the primitive mixed remainder.

The displayed proof remains effective whenever
m^2 log(m+1)=o(log n). Its conservative quantitative bounds
does not yield a vanishing relative error when that quantity
is comparable to or larger than log n without further
constant control or sharper cancellation. Improving the
uniform Taylor and Vandermonde losses while retaining the
excess-degree factor in (18) is a concrete next analytic step.

No new numerical degree, node, or root scan was performed.
