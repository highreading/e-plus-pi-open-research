> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of global adjacent-branch polynomial conditioning

Date: 2026-09-13. Reviewer: audit_results.

Reviewed raw_global_adjacent_branch_conditioning.md in full and
the parity-block comparison in Section 1 of
raw_two_step_channel_transport.md. The theorem and all displayed
constants pass the independent audit. No correction was required.
This is an audit of the exact proof, with no additional degree
construction or numerical diagnostic.

## 1. The resolvent estimates remain uniform at early cuts

Fixing x>=c_0 N^2 and taking N>=max(8,4/c_0) ensures x>=4N.
Thus for every 8<=j<=N the upper spectral bounds of K_j and
K_(0,j) are at most x/2, giving both resolvent norms <=2/x.
Since K_j=K_(0,j)-J_j and ||J_j||<=j, the resolvent difference
is at most 4j/x^2. No comparison of x with an upper multiple
of j^2 enters this argument.

I checked the additional alignment assertion directly. The even
and odd parity blocks of K_(0,j) have consecutive diagonal
differences bounded by k+1+1/12 and consecutive distance-two
coupling differences bounded by (k+2)/2+1/6. At even j,
aligning index 2r with 2r+1 gives row sums <2j. At odd j,
pad the shorter odd block at the left by the scalar d_0=1/3
and align its remaining indices 2r-1 with the even indices 2r.
The sole additional uncoupled edge has size a_1 a_2<1, and
the row-sum bound <=2j persists. The two final coordinates
remain the original boundary coordinates. The padding does not
alter the relevant resolvent entry and obeys the same spectral
upper bound.

The aligned-block resolvent comparison is therefore <=8j/x^2.
Adding the two 4j/x^2 errors from K_(0,j) to K_j gives the
claimed 16j/x^2 diagonal difference. For the off-diagonal entry,
the unperturbed parity resolvent vanishes, so 4j/x^2 suffices.

## 2. Verification of the normalized transfer constant

Use Gamma=[[d_1,0],[ell,d_2]] and the boundary resolvent R.
The lower bound R>=I/(x+j^2), combined with the reviewed
least singular value of Gamma >=j^2/8, gives
M>=j^4 I/[64(x+j^2)]. Its upper norm is <=j^4/(2x).
Together with gamma=(d_1+d_2)/2>=j^2/8 this gives
m/gamma<=4j^2/x, where m=tr(M)/2.

Expanding M_12 gives the two stated terms j^5/x^2 and j^3/x.
The diagonal difference contributes respectively
4j^5/x^2, 3j^3/x, 4j^4/x^2, 2j^2/x. Half their sum,
plus the off-diagonal bound, is

    3j^5/x^2+2j^4/x^2+(5j^3/2+j^2)/x,

which is safely at most 5j^5/x^2+4j^3/x for j>=8.
The exact algebraic identity for T/tau-I then gives

    ||T_j/tau_j-I||
      <=64(1+j^2/x)(11/j+5j/x).

Because j^2/x<=1/c_0, the replacement by
K(1/j+j/x), K=704(1+1/c_0), is valid uniformly at every cut.
The potentially unbounded ratio x/j^2 at fixed early j has
not been hidden in a constant.

## 3. Accumulation and both starting parities

With the fixed starting cut J>=4K and N>=4K/c_0, each error
in the step-two product has norm <=1/2. The scalar tau_j is
positive and has no effect on the condition number. The ordered
matrix product need not commute. Submultiplicativity and
log((1+t)/(1-t))<=3t yield exactly the claimed estimate.
The two step-two sums are bounded by (1/2)log(N/J) and
N^2/(2x), respectively. Thus the accumulation is O(log N),
not a vanishing error.

For the fixed matrix P_J, the Casoratian determinant has degree
exactly J. The eigenvalue upper bound gives the lower magnitude
(x/2)^J divided by its fixed positive normalization whenever
x>=2(J+3/4). The maximum degree of an entry is ceil(J/2),
including the unequal leading degrees when J is odd. Consequently

    cond(P_J)=||P_J||^2/|det P_J|
             <=A_J x^(2ceil(J/2)-J).

The initial even cut costs a constant and the initial odd cut at
most one power of x. This argument avoids assuming that a guessed
leading coefficient matrix is nonsingular. On the final compact
parameter range, the odd cost is at most a constant times N^2.
It follows that A=3K/2+2 is a valid uniform exponent for all
sufficiently large N, with constants depending only on c_0,c_1
and the two fixed starting cuts.

## 4. Normalization and exact scope

The rational-to-symmetric adjacent matrix transformation has row
condition number sqrt((2N+3)/(2N+1)) and column condition number
sqrt3; a factor of three safely covers their product. Thus the
same polynomial conditioning result holds for the rational branches.

For a nonsingular two-by-two matrix, the logarithms of the two
singular values differ by log(cond), while their sum is the
logarithm of the determinant magnitude. This proves equation (16)
with O(log N) uniformly over c in a positive compact interval.
The determinant limit itself is correctly retained as a separately
proved input, rather than assumed by this proof.

The theorem controls the two coherent channels at one positive
parameter. It does not control a growing matrix evaluated at
different parameters, a row-deleted cofactor, or the remainder
matrix A_rem. The note preserves these distinctions, as well as
the sufficiently-large-index condition needed to avoid small
parameter intervals containing row eigenvalues.
