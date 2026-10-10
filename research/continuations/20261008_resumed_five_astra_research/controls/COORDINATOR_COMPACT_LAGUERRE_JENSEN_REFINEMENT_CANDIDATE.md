> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Candidate: a paid Laguerre spread gain for the same reference determinant

Status: NEW coordinator derivation and exact auxiliary receipt PASS;
DIFFERENT external full-proof audit pending. The earlier complete M_y>=D/32
comparison is also still under external audit. This concerns the raw same-H
analytic lower bound only; actual all-prime content remains unknown.

## 1. Reuse the complete original interface and exact relative factor

Keep the original compact H, its highest factorial(6k-4)!, all source
corrections and contact atom, and the actual gcd G. Reuse the previous
reference D_k(i,j)=(2k+2i+2j)! and factorial lower bound

    B_k=2^(k(k-1)) product_(j=0)^(k-1) j!(3k-1+j)!.

The earlier proof's exact integral, BEFORE its AM-GM inequality, gives

    det D_k = B_k E[ product_(i<j) g_ij ],
    g_ij=(z_i+z_j)^2/(4z_i z_j).

Here E is the probability law with joint density proportional to
V(z)^2 product z_i^(3k-1)exp(-z_i), on z_i>0. Its normalizing integral
is k! product j!(3k-1+j)!, already checked in the previous receipt.
The exact equality follows by multiplying the displayed relative factors;
no entrywise comparison or divisibility assertion is used.

This is the classical complex Laguerre/Wishart law with matrix size k
and m=4k-1 Gaussian columns. [Cunden--Dahlqvist--O'Connell, Section1.2](https://arxiv.org/pdf/1809.10033) gives the density/normalization.
Their scaled eigenvalues must be multiplied by k to obtain the unscaled
exp(-z) convention here. All moments below use UNNORMALIZED traces and
complex Gaussians of E|X_ab|^2=1, not the real Wishart convention.

## 2. A deterministic relative spread inequality

For k>=2 define

    A=sum_(i<j)(z_i-z_j)^2 = k sum z_i^2-(sum z_i)^2,
    B=sum_(i<j)(z_i^2-z_j^2)^2 = k sum z_i^4-(sum z_i^2)^2.

Both are positive almost surely under the continuous Laguerre density.
Since r_ij=(z_i-z_j)/(z_i+z_j) has |r_ij|<1,

    log g_ij = -log(1-r_ij^2) >= r_ij^2.

Cauchy--Schwarz applied to the finite pair sum gives

    sum_(i<j) r_ij^2 >= A^2/B.

Indeed (sum a/b)(sum ab)>=(sum a)^2 with
a=(z_i-z_j)^2 and b=(z_i+z_j)^2. A second Cauchy--Schwarz, now in
probability, gives E[A^2/B]>=(EA)^2/EB. Jensen consequently proves

    log E[ product g_ij ] >= E[ sum log g_ij ]
                              >= (EA)^2/EB.

All expressions are integrable: the exact relative expectation is the
finite factorial determinant divided by B_k; log(product g)>=0 is
bounded above by product g. The intermediate A^2/B is bounded by the
finite pair count. There is no uncontrolled expectation or tail deletion.

## 3. Classical moments with an elementary complete derivation

Let W=XX^*, where X has k rows and m independent standard complex
Gaussian columns. For a permutation gamma on q positions whose cycles
specify the trace factors, elementary complex Wick contraction gives

    E product_(cycles c of gamma) Tr(W^|c|)
      = sum_(sigma in S_q) m^cycles(sigma) k^cycles(gamma sigma).

To see this, expand the q W entries as sums X_ab conjugate(X_cb).
A nonzero Gaussian pairing matches each unbarred X to a barred X by
sigma. Its column equalities have cycles(sigma) free indices and its
row equalities have cycles(gamma sigma) free indices. Each covariance
equals1. Summing all q! pairings gives the displayed formula. The
orientation inverse alternative gives the same full permutation sum.

Enumerating ONLY S2 and S4, with gamma respectively(12), identity,
(1234), and(12)(34), yields the following classical polynomials:

    ETr(W^2)=km(k+m),
    E(Tr W)^2=km(km+1),
    ETr(W^4)=km[k^3+6k^2m+6km^2+m^3+5k+5m],
    E(Tr W^2)^2=km[km(k+m)^2+4k^2+10km+4m^2+2].

Thus, EXACTLY,

    EA=km(k^2-1),
    EB=km(k^2-1)(k^2+5km+4m^2+2).

The parent symbolic receipt verifies both factorizations. Independent
direct polynomial integration against the Laguerre density at k2,3,4
agrees with them; no random sampling or asymptotic extrapolation is used.

## 4. The new finite and asymptotic gain

Substitute m=4k-1 in Section2:

    det D_k >= B_k exp(R_k),
    R_k = k(4k-1)(k^2-1)/(85k^2-37k+6) >0,   k>=2.

In particular R_k/k^2 tends to4/85. The bound is valid for every integer
k>=2 and hence for the unchanged original compact index set.

Combining it with the earlier complete-source candidate's Section5,
without changing its cutoff k>=512 or any negative-term payment,

    (-1)^k H_k(e+pi) >= (3 Lambda_k/64)^k h_k B_k exp(R_k) >0.

The candidate SAME-H asymptotic lower constant becomes

    C_H,new=15log2-(9/2)log3+4/85 =5.50051123292209779...

The leading4k^2logk term is unchanged. This is a stricter analytic size
lower bound; it does not estimate the actual gcd G from either side.

## 5. Scope of conditional arithmetic implications

Only if the still-unproved BOTH odd-content divisibility hypotheses and
an ACTUAL upper bound v2(G)<=A k^2+o(k^2) were established, the previously
paid height would make A<3.27939003275696796... sufficient for compact
retirement. The actual binary upper and odd-local hypotheses remain
OPEN. Retirement of this producer would not decide e+pi.

No request admitted before this note received it. Supply this new
candidate and its receipt in a subsequent independent audit packet.
Do not rerun the old reference matrices or reissue their earlier audit
as if it already covered this later spread correction.
