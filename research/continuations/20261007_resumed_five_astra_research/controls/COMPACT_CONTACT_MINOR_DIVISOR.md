> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A classical integral Gram frame and an all-prime contact-minor divisor

Coordinator derivation, 7 October 2026. This is an active structural result,
not an irrationality proof. It reuses classical Laguerre orthogonality and the
integer Gram-frame argument rather than claiming those methods are new.

The overlap check found no evaluated all-size divisor for this specific complete
even-contact rectangular matrix in the inspected archive notes. Miller and
Stanton, *Orthogonal polynomials and Smith normal form*, Theorem1 and its proof
(author PDF pages2–3), give the standard triangular integral Gram diagonalization:
https://arxiv.org/abs/1704.03539 and
https://www-users.cse.umn.edu/~stant001/PAPERS/StantonMillerFinal.pdf .
The coordinator inspected that theorem/proof, not the entire16-page paper.
It must be reused, with the even restriction and negative point mass retained.

## 1. The complete measure and its integral polynomial frame

For the already established full charge measure



$$
d\eta(t)=e^{t-1}\,dt\quad(t\le1),\qquad
 a_m=\int t^m\,d\eta(t),
$$



define



$$
Q_r(t)=r!L_r^{(0)}(1-t).
$$



The finite Laguerre coefficient formula proves that Q_r is a monic integer
polynomial. The substitution u=1-t in the ordinary gamma integral gives



$$
\int Q_rQ_s\,d\eta=(r!)^2\mathbf1_{r=s}.
$$



Equivalently Q_0=1, Q_1=t and



$$
Q_{r+1}(t)=(t+2r)Q_r(t)-r^2Q_{r-1}(t).
$$



Thus every monomial, including each t^(2i), has INTEGER coordinates in the
Q-frame: successive cancellation of its leading coefficient uses monic integer
polynomials. This is a finite unimodular frame statement, not an assertion that
the restricted even frame itself has diagonal Smith form.

## 2. Cross-moment minors

For any finite nonnegative index lists I,J, the cross-moment matrix
M_IJ=(a_(2i+2j)) admits the finite factorization



$$
M_{IJ}=R_I\operatorname{diag}((r!)^2)R_J^T
$$



with INTEGER frame-coordinate matrices R_I,R_J. Cauchy–Binet shows that every
size-s minor of any such matrix is divisible by



$$
D_s=\prod_{r=0}^{s-1}(r!)^2,\qquad D_0=1.
$$



Indeed each contributing set of distinct frame degrees r_0<...<r_(s-1)
satisfies r_j>=j, so the product of their squared factorials is divisible by D_s.
This uses the complete factorial charge, not its pole-only approximation.

## 3. Retain the negative point mass

The actual contact response is



$$
\Phi_{k,d}=(c_{i+m}),\qquad c_j=a_{2j}-(-1)^j.
$$



Each selected square submatrix has the form M-vw^T, with INTEGER v,w. Its
determinant is det M minus the scalar rank-one cofactor contribution. Every
cofactor is a size-(k-1) cross-moment minor. Consequently



$$
\boxed{D_{k-1}\mid\det\Phi_{k,d}[J]}
$$



for every maximal minor J, and hence



$$
\boxed{D_{k-1}\mid\delta_{k,d}}
$$



whenever d>=k-1. This is all-prime divisibility, including prime powers.
It is a LOWER divisor of the actual maximal-minor gcd, not its evaluation.

For the 2k-column block determinant H_k(s) specified in A5turn11, Laplace
expansion in its k contact columns now gives directly



$$
D_{k-1}\mid H_{0,k},\qquad D_{k-1}\mid H_{1,k}.
$$



This last conclusion does not require replacing the true final pair gcd by a
row content or choosing a nonsaturated contact basis.

## 4. Exact scope and remaining arithmetic

The divisor has



$$
\log D_{k-1}=k^2\log k+O(k^2).
$$



It does not evaluate delta_(k,2k-1), its Smith invariants, or the final pair gcd
G_k. It does not establish whole evaluated nonvanishing or primitive decay.
In particular, the available bound log F_k=4k^2 log k+O(k^2) is still too weak
to imply decay using this divisor alone; that comparison is a statement about
available bounds, not a lower bound on the actual error or an impossibility proof.

The next target is an additional correlated divisor or a substantially sharper
whole signed determinant estimate. Neither is asserted in this note.
