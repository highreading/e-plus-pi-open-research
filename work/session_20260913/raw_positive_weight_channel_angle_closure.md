> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Positive polynomial weights close the actual channel-angle gap after a new cutoff

Date: 2026-09-13. Original root derivation.
Independent review: raw_positive_weight_angle_independent_review.md
passes the complete proof without correction. A separate derivation is
in raw_reoptimized_energy_angle_independent_proof.md.

This note proves a subexponential lower bound for the actual unprojected
channel angle after increasing the exceptional-node cutoff to order
n^(3/4). The key is a positive-power expansion of the metric, used only
on polynomial vectors whose required powers cannot reach the finite
boundary. The full conjugated reflection operator and its boundary
residue sum need not be bounded. This distinction is essential.

The resulting retained energy projection has at most O(n^(3/4)) poorly
controlled directions. This does not control those remaining directions,
the physical endpoint angle, or the primitive approximation remainder.

## 1. A finite positive-weight lemma

Let K=K_N be the actual symmetric five-diagonal row matrix, and C=C_N
the coefficient matrix of polynomial reflection E_k(x) -> E_k(1-x).
It satisfies C^2=I and preserves every coordinate prefix. For a vector
w supported in coordinates 0,...,s, the polynomial commutation identity
gives

    H^r Cw = C H^r w,  H=M I-K,  whenever s+2r<N.        (1)

Indeed both sides are the coefficient vectors of the same polynomial:
the infinite polynomial operator commutes with reflection, and every
intermediate degree is at most s+2r. Thus no finite truncation enters
either composition. This argument also applies to complex vectors.

Suppose H is positive definite and

    F = sum_(j=0)^h f_j H^j,     f_j >= 0,

with F positive definite. If s+h<N, then for all w in that prefix

    ||Cw||_F <= M_C ||w||_F,
    M_C = ||C|| sqrt(cond H),    ||w||_F^2=w*Fw.         (2)

For j=2r, (1) gives

    <Cw,H^(2r)Cw> = ||C H^r w||^2
                   <= ||C||^2 <w,H^(2r)w>.

For j=2r+1, putting v=H^r w gives

    <Cw,H^(2r+1)Cw> = <Cv,H Cv>
       <= lambda_max(H)||C||^2 ||v||^2
       <= cond(H)||C||^2 <v,Hv>.

Here (1) is needed only through r=floor(h/2); the slightly stronger
support assumption s+h<N covers both parities. Sum with the nonnegative
coefficients f_j. Because cond(H)>=1, this proves (2). No commutation
with F^(1/2), or with F itself, has been assumed.

If two subspaces of that prefix have C-eigenvalues +1 and -1, their
images under F^(1/2) have a combined, separately orthonormalized least
singular value at least

    delta_* = sqrt(2/(1+M_C^2)) >= 1/M_C.                (3)

The last inequality uses M_C>=1. The involution on their sum is
F^(1/2) C F^(-1/2), restricted to that sum. Its norm is bounded by (2).
The reviewed two-subspace involution identity gives (3). This local
involution is for the polynomial surrogate; it is not an assertion
about the full actual energy involution F^(-1/2) C F^(1/2).

## 2. Actual roots and a larger, still sublinear cutoff

Set N=2n, M=2n+1, and H=M I-K_N. The reviewed spectral bounds give

    lambda_min(H)>=1/4,
    lambda_max(H)<=4n^2+2n+5/8<=7n^2,
    cond(H)<=28n^2.                                    (4)

The reviewed reflection estimate, for n>=3, therefore gives

    M_C <= A_n := 12 sqrt(28) n^2 exp(2 sqrt(6n)).       (5)

All subsequent assertions are for sufficiently large n. Put

    b=ceil(n^(3/4)),       m=ceil(24 n^(3/4)).

Put the nodes with indices 0,...,b into their respective low factors.
If necessary, move one last high root into the corresponding low
factor to equalize the two high counts. The unchanged actual node
polynomials then factor into low factors L_a,L_b and equal-degree
high factors F_a,F_b, with interlacing roots

    alpha_1 < beta_1 < ... < alpha_h < beta_h.

Keep the original seeds and domain dimensions d_sigma=n-m_sigma.
As before set R=F_a/F_b, W_sigma=[L_sigma(K)K^j v_sigma]_(j<d_sigma).
The full vanishing matrix is exactly

    Z=F [R(K) W_a, W_b],       F=F_b(K).                (6)

Fixed signs and channel ordering are understood as in the preceding
ratio note. This only changes the factorization and metric; Z and its
retained block Z_L are unchanged. The new angle below is associated
with this new metric, not identified with the angle at the old cutoff.

For every retained high root and all large n,

    beta_i-M >= b^2/2,       beta_i> M.

This follows from xi_l>=l(l+1)+3/4, l>b, and b^2/n -> infinity.
Consequently

    F_b(K)=product_i[(beta_i-M)I+H]
          =sum_(j=0)^h f_j H^j,

with every f_j positive when h>0. The empty product is harmless.
This is exactly the positive expansion required in Section 1.

The low counts satisfy ell_sigma<=ceil((b+1)/2)+1; thus they are
O(n^(3/4)), and h<=ceil((n+1)/2)<=n/2+1. The coordinate support of
W_sigma ends no later than n+2 ell_max+2. Therefore the surrogate

    X_tilde=[p_m(K) W_a, W_b]                            (7)

ends at an index s<=n+2 ell_max+2m+2. In particular

    s+h <= 3n/2 + O(n^(3/4)) < 2n.                     (8)

Every column identity, including its C-eigenvalue, is consequently a
literal polynomial identity inside the finite matrix. Multiplication
by a nonzero p_m keeps the first channel independent, and the two
different components cannot cancel. Section 1 applies to their entire
sum, with the bound A_n from (5).

## 3. Exponentially accurate ratio localization with sublinear degree

Use the exact positive partial fractions and normalized weights of
raw_high_ratio_quasilocal_approximation.md. Its Chebyshev construction
applies verbatim to the larger root gap. On the actual spectral
interval [a_n,M_n]=[-4n^2+3/8,2n+3/4], its length is at most 6n^2.
For each high pole,

    z_beta-1 = 2(beta-M_n)/(M_n-a_n) >= b^2/(6n^2).

For all large n this lower bound is at most 1. The elementary
arcosh(1+u)>=sqrt(u), 0<=u<=1, yields a degree-m polynomial with

    ||R(K)-p_m(K)|| <= epsilon_n
       :=2 exp(-(m+1)b/(sqrt(6)n))
       <=2 exp(-4 sqrt(6n)).                           (9)

The same estimate holds in the F metric since R,p_m,F commute.
The old lower bound R(K)>=2I/n still holds for this larger cutoff:
its first gap is at least 2n and its last root is at most n^2 above
M_n. Equivalently it follows from the interlacing telescoping bound.
In particular p_m>0 on the row spectrum for all large n.

Let E=[E_a,E_b] be the actual two channels, separately orthonormalized
in the F metric exactly as in the ratio note. Let E_tilde use p_m
in place of R, retaining those same individual normalization matrices.
The established commuting-metric estimate gives

    ||E-E_tilde|| <= t_n := (n/2) epsilon_n.            (10)

No angle between the channels is used in this estimate.

Each column block of E_tilde has smallest singular value at least
1-t_n. On separately orthonormalizing those two surrogate blocks,
(3), (5), and (8) give a combined least singular value >=1/A_n.
Undoing this block normalization therefore proves

    sigma_min(E_tilde)>=(1-t_n)/A_n.

Weyl's singular-value inequality and (10) now give

    delta_n := sigma_min(E)
       >=(1-t_n)/A_n-t_n >= 1/(2A_n)                  (11)

for all large n. Indeed A_n t_n tends to zero by (5) and (9), so
eventually t_n<=1/(4A_n). The elementary last inequality is then
valid since A_n>=1. Thus the actual new-cutoff angle satisfies the
unconditional bound

    delta_n >= [24 sqrt(28) n^2]^-1 exp(-2 sqrt(6n)).  (12)

This is the desired subexponential estimate for the actual angle in
the reoptimized metric. It does not assert a bound for the full
conjugated reflection or for the old cutoff's angle.

## 4. Consequence for the actual retained matrix

Let O=E(E*E)^(-1/2), and let Pi_L^F be the orthogonal projection onto
F^(1/2) of the first n+1 coordinate space. The support and rank
argument from the reviewed ratio note, with the present b,m, gives

    sigma_(r+1)((I-Pi_L^F)O) <= t_n/delta_n
          <=2 A_n t_n = O(n^3 exp(-2 sqrt(6n))),        (13)

where r can be chosen as min(n-1,2(m+ell_max)+4)=O(n^(3/4)).
The harmless extra 4 covers the deliberately loose endpoint support
counts above. The two nested energy coordinate spaces differ by at
most r dimensions. There are n-1 columns in O.

Consequently at least n-1-r singular values of the retained projection
are at least sqrt(1-eta_n^2), where eta_n is the right side of (13).
In particular, for all large n,

    rank Z_L >= n-1-O(n^(3/4)).                        (14)

The actual normalization of that retained matrix is

    F[L,L]^(-1/2) Z_L B^(-1) (E*E)^(-1/2),

where B is the block diagonal matrix of individual energy Gram square
roots from the ratio note. All factors are invertible, so the rank
conclusion is about the original Z_L. The complementary reduction
H_high=-Z_H^(-T) Z_L^T S transfers the rank bound to the actual high
moment block as well, since its outside factors are invertible.

The preconditioned singular values in (13) cannot be reported as
unweighted or physical singular values. The remaining O(n^(3/4))
directions, the low-node cardinal factors S including g_l, and the
endpoint projection still require their own quantitative estimates.
Nothing here proves a full high-matrix rank theorem or the shrinking
of an integer linear form in 1 and e+pi.

## 5. Why the earlier full-operator obstruction is bypassed

The earlier Theta_N identity remains correct and its full norm may
still have an exponential loss. Here positive powers of H are bounded
only on the supported surrogate. Half of each power is enough for
its quadratic form, so the paths stay inside N even though F itself
has degree proportional to n. The larger low-node cutoff permits a
polynomial approximation accurate on the reflection's exp(O(sqrt n))
scale while using only O(n^(3/4)) new coordinates. Perturbation then
returns to the actual channels. These are the two reasons the old
global condition-number obstruction does not reappear in this proof.
