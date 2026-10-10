> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The first matrix transport correction and its limiting transport equation

Date: 2026-09-13. Original continuation by audit_sources.
Independent review requested.

In the actual symmetric row normalization, order the two boundary
coordinates as (N-2,N-1). For every compact E contained in
H={c:Re c>0}, this note proves the uniform holomorphic expansion

    T_N(cN^2)=lambda(c)[I+A(c)/N+O_E(N^(-2))],             (1)

where lambda=(sqrt(c)+sqrt(c+1))^2 and

    s(c)=sqrt(c)/sqrt(c+1),

    A(c)= -I/(c+1)
           + [[s(c), 1/s(c)-1],
              [1/s(c)+1, -s(c)]].                        (2)

All square roots are principal on H. The coefficient is independent
of the parity of N in the stated boundary order. Relabeling the
coordinates by absolute even/odd parity conjugates (2) by the
coordinate swap when that order is reversed.

The proof below retains the second resolvent term. In particular
the O(N^-2) remainder is not obtained by differentiating the
previous O(N^-1) estimate or by asserting operator-norm convergence
of the entire finite matrix.

## 1. Two boundary channels on fixed half-lines

Use the exact row matrix

    K_(l,l)=d_l=a_l^2+a_(l+1)^2-l(l+1),
    K_(l,l+1)=-a_(l+1),
    K_(l,l+2)=a_(l+1)a_(l+2),
    a_l=l^2/sqrt(4l^2-1), l>=1, a_0=0.

Reverse each boundary parity chain onto a copy of N_0. Channel
beta=2 starts at l=N-2, and channel beta=1 starts at l=N-1;
at depth j its original index is

    l=N-beta-2j.

After both finite chains end, extend by a zero tail. The resulting
self-adjoint operator B_N on ell^2(N_0) plus ell^2(N_0) is the
embedded K_N/N^2, with additional zero eigenvalues. Its two
boundary coordinates are the depth-zero vectors e_(2,0), e_(1,0).

Let L have diagonal -1/2 and off-diagonal 1/4, and put
L_0=L direct-sum L in this channel order. The first coefficient
perturbation is the formally unbounded, symmetric band operator H_1
with diagonal blocks

    (H_beta)_(j,j)=beta+2j-1/2,
    (H_beta)_(j,j+1)=-(beta/2+j+1/4),                     (3)

and off-diagonal block from channel 1 to channel 2

    (H_(2,1)v)_j=-(v_j+v_(j+1))/2,
    H_(1,2)=H_(2,1)^T.                                  (4)

The two terms in (4) correspond respectively to the original
neighbors l+1 and l-1 of the channel-2 index l. Thus both
opposite-parity couplings are included; retaining only the
same-depth coupling would give a different correction.

## 2. Coefficient errors with weighted control

The exact coefficient formulas give

    a_l^2=l^2/4+delta_l, 0<=delta_l<=1/12,
    a_(l-1)a_l=l(l-1)/4+O(1),
    a_l=l/2+O(1),                                      (5)

with absolute bounded errors, including the small indices when
they are present. Substitution of l=N-beta-2j yields, for the
interior coefficients of B_N,

    (B_N)_(beta,j;beta,j)
       =-1/2+(beta+2j-1/2)/N+O((j+1)^2/N^2),

    (B_N)_(beta,j;beta,j+1)
       =1/4-(beta/2+j+1/4)/N+O((j+1)^2/N^2),

    (B_N)_(2,j;1,j)=-1/(2N)+O((j+1)/N^2),
    (B_N)_(2,j;1,j+1)=-1/(2N)+O((j+1)/N^2).             (6)

For example the diagonal quadratic remainder comes directly from
-l(l+1)/(2N^2); the two cross entries use a_(N-1-2j) and
a_(N-2-2j), respectively.

The same weighted estimates extend to every omitted coupling and
zero-tail row. At such a depth, j+1 is at least a fixed positive
multiple of N. The constant coefficients of L_0 and the
O((j+1)/N) coefficients of H_1/N are then bounded by a constant
times (j+1)^2/N^2. This argument includes the one-coordinate
difference between the two chain lengths when N is odd.

Write D_N=B_N-L_0. There is an absolute C, independent of N,
such that each of its finitely many bands, and the corresponding
band of D_N-H_1/N, satisfy respectively

    |coefficient at depth j| <= C(j+1)/N,
    |coefficient at depth j| <= C(j+1)^2/N^2.             (7)

Transposed bands obey the same bounds with a harmless change in
C. For the first estimate at interior depths one can use
j+1=O(N) in (6); at tail depths the coefficients of D_N are
bounded constants. The operators D_N themselves are bounded,
although H_1 is unbounded on unrestricted sequences.

## 3. The localized second resolvent identity

Use the holomorphic functions

    q=(sqrt(c+1)-sqrt(c))^2, m=4q,
    w_j=m q^j,

from `raw_holomorphic_normalized_transport.md`. On every compact
E contained in H, |q| is uniformly less than one, and every
fixed polynomially weighted norm of w is uniformly bounded.
Let w_beta be this vector on channel beta and zero on the other
channel. Then

    (cI-L_0)^(-1)e_(beta,0)=w_beta.

The band estimates (7), with their finitely many shifts, imply

    ||D_N w_beta||=O_E(N^-1),
    ||(D_N-H_1/N)w_beta||=O_E(N^-2).                    (8)

In particular w_beta belongs to the domain of H_1, so the second
expression is well defined. The actual resolvent
R_N=(cI-B_N)^(-1) has uniformly bounded norm on E for large N,
by the self-adjoint spectral bound and Re c>0.

For R_0=(cI-L_0)^(-1), the exact second resolvent identity is

    R_N=R_0+R_0 D_N R_0+R_0 D_N R_N D_N R_0.             (9)

After taking boundary entries, its final term is O_E(N^-2)
by (8) on both sides and the bound for R_N. These entries use
the analytic bilinear form w_beta^T D_N R_N D_N w_gamma;
the bound |u^T v|<=||u|| ||v|| is valid without identifying
this bilinear form with a squared Hilbert norm. The real
symmetric D_N and transpose-symmetric R_0 justify the displayed
left boundary vector.

The first correction in (9), by (8), is
N^-1 w_beta^T H_1 w_gamma+O_E(N^-2). Hence the actual
two-coordinate scaled boundary resolvent has the expansion

    iota_N^T(cI-K_N/N^2)^(-1)iota_N
       =m I+B(c)/N+O_E(N^-2),
    B_(beta,gamma)=w_beta^T H_1 w_gamma.                 (10)

This proof sandwiches the perturbations between localized
vectors. It does not need ||D_N||=O(1/N), which is false in
the remote part of the zero-tail construction.

## 4. Evaluation of the correction matrix

For a diagonal block (3), put r=q^2. Its geometric sums are

    B_(beta,beta)/m^2
      =(beta-1/2)/(1-r)+2r/(1-r)^2
       -q(beta+1/2)/(1-r)-2qr/(1-r)^2
      =[(2beta-1)+(2beta-3)q]/[2(1+q)^2].               (11)

For the cross block (4),

    B_(2,1)=B_(1,2)
      =-(m^2/2)sum_(j>=0)(q^(2j)+q^(2j+1))
      =-m^2/[2(1-q)].                                 (12)

Thus in the order (N-2,N-1),

    B(c)=m^2 [[(3+q)/(2(1+q)^2), -1/(2(1-q))],
               [-1/(2(1-q)), (1-q)/(2(1+q)^2)]].        (13)

The sums converge locally uniformly on H. In particular the
result and the remainder in (10) are holomorphic there on each
fixed compact domain for all sufficiently large N.

## 5. Expansion of the actual transfer

The exact boundary coupling in the same order is

    Gamma_N=[[a_(N-1)a_N,0],[-a_N,a_Na_(N+1)]].

Consequently

    Gamma_N/N^2=I/4+G_1/N+O(N^-2),
    G_1=[[-1/4,0],[-1/2,1/4]].                         (14)

Its two diagonal shifts must both be retained. From the exact
boundary form M_N=Gamma_N^T(iota_N^T(xI-K_N)^(-1)iota_N)Gamma_N,
equations (10) and (14) give

    M_N(cN^2)/N^2=m I/16
       +[B/16+(m/4)(G_1+G_1^T)]/N+O_E(N^-2).           (15)

The nonvanishing of m on H and the compact-domain bounds permit
a uniform Neumann expansion of this 2-by-2 matrix inverse.
Since T_N=M_N^(-1)Gamma_N^T and lambda=4/m, the relative
first correction is

    A(c)=4G_1^T-[B/m+4(G_1+G_1^T)]
         =-4G_1-B/m.                                 (16)

Substituting (13) yields

    A_11=(1-4q-q^2)/(1+q)^2,
    A_22=(q^2-4q-1)/(1+q)^2,
    A_12=2q/(1-q), A_21=2/(1-q).

The identities
(1-q)/(1+q)=sqrt(c)/sqrt(c+1) and
4q/(1+q)^2=1/(c+1) prove formula (2). This completes (1),
including its uniform O_E(N^-2) remainder. Cauchy's formula
on a slightly larger compact neighborhood also gives the same
order for every fixed number of c derivatives of the remainder.

The parity qualification in the opening statement is literal:
the boundary shift beta, rather than the absolute parity of its
original index, determines (3). The finite opposite-end boundary
has already been included in (7)-(9). No unresolved parity-sized
tail term can affect the first coefficient.

## 6. The limiting matrix transport equation

Fix chi in a compact subset of H, take n<=m<=2n of the same
parity, and remove the exact scalar product

    Lambda_(m,n)(chi)=product_(j=n+2,n+4,...,m)
                              lambda(chi n^2/j^2).

Let V_(m,n) be the exact normalized ordered transport from
`raw_holomorphic_normalized_transport.md`. Formula (1) gives
its factors as

    I+A(chi/(j/n)^2)/j+O_K(n^-2).

For t in [1,2], define Y(t,chi) as the solution of

    partial_t Y(t,chi)= [A(chi/t^2)/(2t)]Y(t,chi),
    Y(1,chi)=I.                                      (17)

The coefficient and its t derivative are uniformly bounded on
these compact domains. A mesh interval of length 2/n has local
propagator I+A(chi/t^2)/(nt)+O_K(n^-2), evaluated at its right
endpoint. Thus the exact factors above differ from the ODE
propagators by O_K(n^-2). Their ordered products and inverses
are uniformly bounded by the preceding holomorphic transport
theorem and the elementary ODE exponential bound. A telescoping
product estimate over O(n) steps proves

    V_(m,n)(chi)=Y(m/n,chi)+O_K(n^-1),
    V_(m,n)(chi)^(-1)=Y(m/n,chi)^(-1)+O_K(n^-1).          (18)

The bounds are uniform in m and chi. The solutions are
holomorphic in chi, and Cauchy's formula gives the same O(1/n)
convergence for first and second chi derivatives on smaller
compact sets. This supplies a limiting ordered matrix correction,
rather than only boundedness of that correction.

As an exact check on its scalar part, tr A(c)=-2/(c+1).
Liouville's determinant identity in (17) gives

    det Y(t,chi)=sqrt((chi+1)/(chi+t^2)),                (19)

with the nonzero holomorphic square-root branch equal to one at
t=1. Indeed its logarithmic derivative is -t/(chi+t^2).

## 7. An explicit solution of the matrix transport equation

The limiting orientation in (17) can be written without a
path-ordered exponential. For t in [1,2] and chi in H, put

    w_t=t/(sqrt(chi+t^2)+sqrt(chi)),
    D_t=diag(sqrt(w_t),1/sqrt(w_t)),
    eta=(t-1)/(2sqrt(chi)),
    f_t=exp([Log(chi+1)-Log(chi+t^2)]/4).

The roots of chi and chi+t^2 and both displayed logarithms
are principal. Their square-root sum has positive real part,
so w_t has positive real part as well; its principal square
root is nonzero and holomorphic. These choices make f_1=1
and select the positive values on the positive real axis.
The exact solution is

    Y(t,chi)=f_t D_t
             [[cosh(eta),sinh(eta)],
              [sinh(eta),cosh(eta)]] D_1^(-1).           (20)

For a direct check, let sigma_1=[[0,1],[1,0]] and
sigma_3=diag(1,-1). Differentiation gives

    f_t'/f_t=-t/[2(chi+t^2)],
    D_t'D_t^(-1)=sqrt(chi)/[2t sqrt(chi+t^2)] sigma_3,
    eta'=1/(2sqrt(chi)),
    D_t sigma_1 D_t^(-1)=[[0,w_t],[1/w_t,0]].

The sum of these three logarithmic derivative matrices is
exactly A(chi/t^2)/(2t): rationalizing w_t supplies the two
off-diagonal entries. Formula (20) equals I at t=1, and
therefore is the unique solution of (17). Its determinant
is f_t^2, agreeing with (19).

Equivalently, the substitution u=asinh(t/sqrt(chi)) and
the diagonal gauge with entries sqrt(tanh(u/2)) and its
inverse reduce the generator to the commuting matrices
-(tanh u)I/2+(cosh u)sigma_1/2. The direct derivative check
above avoids requiring any extra continuation convention
for that auxiliary substitution.

At a fixed x with Re x>0, this formula also has the cocycle
form Y(m/n,x/n^2)=F(m,x)F(n,x)^(-1), where

    w(t,x)=t/(sqrt(x+t^2)+sqrt(x)),
    F(t,x)=(x+t^2)^(-1/4)
            diag(sqrt(w(t,x)),1/sqrt(w(t,x)))
            exp(t sigma_1/(2sqrt(x))).                  (21)

The scalar and diagonal branches are those just specified.
This is an exact identity for the limiting transport; it does
not extend the uniform discrete error estimate to ratios
x/j^2 outside compact subsets of H.

## 8. Scope and the remaining initial orientation

The matrix ODE (17) determines the asymptotic change of the
two-component orientation across any fixed ratio of large cuts.
It does not determine the initial branch matrix P_n(chi n^2)
from a fixed finite seed, since this dyadic analysis keeps the
ratio chi bounded away from the imaginary axis and is local in
the growing cut scale. Nor does (18) by itself estimate a growing
mixed-node determinant after the prescribed low-row deletion.

The result is a concrete input for that next comparison: it
identifies both the common scalar factor and the limiting
noncommuting matrix transport, with a uniform error and parameter
derivatives. No root scan, new canonical degree solve, or
irrationality conclusion is used or asserted.
