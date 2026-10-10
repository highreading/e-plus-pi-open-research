> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A normalized two-step transfer and its accumulated channel mixing

Date: 2026-09-13. Original bounded continuation by audit_computations.

Inputs: the reviewed matrix CD identity and root's independently
reviewed `raw_matrix_resolvent_parity_decoupling.md`.
The result below normalizes the actual matrix transfer, retains its
errors, and bounds their product over a dyadic interval. It does not
claim that the branch matrix itself is diagonal.

## 1. An additional diagonal balance estimate

Write (K_N=K_{0,N}-J_N), where (K_{0,N}) is the compression
of (J^2-\Lambda). Fix (0<c\le C), and assume



$$
cN^2\le x\le CN^2,\qquad N\ge\max\{8,4/c\}.
\tag{1}
$$



Let (R=(xI-K_N)^{-1}), (R_0=(xI-K_{0,N})^{-1}).
The reviewed inequalities give (K_{0,N}\preceq(9/8)I),
(K_N\preceq(N+3/4)I), and (\|J_N\|\le N). Hence



$$
\|R\|,\|R_0\|\le\frac2{cN^2},\qquad
\|R-R_0\|\le\frac4{c^2N^3}.
\tag{2}
$$



The last inequality is the ordinary resolvent identity; its sign
is irrelevant for the norm estimate.

Compare the even and odd parity blocks of (K_{0,N}), aligning
their indices one apart. Their diagonal entries are



$$
d_k=-\frac{k(k+1)}2+\frac14+\delta_k+\delta_{k+1},
\qquad a_k^2=\frac{k^2}4+\delta_k,
$$



where (\delta_0=0) and (0\le\delta_k\le1/12).
Thus ( |d_{k+1}-d_k|\le k+1+1/12). Their distance-two
entries satisfy



$$
a_{k+1}a_{k+2}=\frac{(k+1)(k+2)}4+\varepsilon_k,
\qquad 0\le\varepsilon_k\le1/6,
$$



so the adjacent difference is at most ((k+2)/2+1/6).
The error bound follows from (j/2\le a_j\le j/2+1/(12j)):
the product error is at most (3/24+1/288<1/6).

For even (N), the parity blocks have equal size. Their difference
has norm at most (2N) by these row-sum estimates. For odd (N),
pad the shorter block on the left by a decoupled entry (d_0=1/3),
then align its remaining indices with the adjacent longer-block
indices. The newly omitted coupling is (a_1a_2<1), and the same
(2N) row-sum bound holds. The last coordinate still refers to
the actual boundary coordinate in each parity. The padding does
not change its resolvent entry, and its added eigenvalue obeys the
same upper spectral bound.

The resolvent identity for these aligned blocks gives a difference
at most (8/(c^2N^3)) between the two boundary diagonal entries
of (R_0). Adding the two errors in (2) proves



$$
\boxed{|R_{N-2,N-2}-R_{N-1,N-1}|
\le\frac{16}{c^2N^3}.}
\tag{3}
$$



Write (\Gamma_N=\bigl(\begin{smallmatrix}d_1&0\\\ell&d_2\end{smallmatrix}\bigr))
and (M_N=\Gamma_N^T(\iota_N^TR\iota_N)\Gamma_N).
Here (d_2-d_1=a_N(a_{N+1}-a_{N-1})), so
(0<d_2-d_1\le3N/2). The already reviewed bounds give
(d_1+d_2\le N^2), ( |\ell|\le N), and
( |R_{N-2,N-1}|\le4/(c^2N^3)). Expanding the two diagonal
entries now gives



$$
\boxed{|(M_N)_{11}-(M_N)_{22}|
\le(5/c+8/c^2)N.}
\tag{4}
$$



For detail, the four bounds before rounding are
(3N/c\), (4N/c^2\), (4/c^2\), and (2/c\), respectively
from the diagonal factor difference, (3), the cross term, and the
$\ell^2$ term. This verifies (4) without an asymptotic assumption.

## 2. Scalar normalization of the exact transfer

The actual two-step identity is



$$
M_N(x)P_N(x)=\Gamma_N^TP_{N-2}(x).
$$



All these matrices are invertible in (1). Put



$$
T_N=M_N^{-1}\Gamma_N^T,\qquad
m_N=\tfrac12\operatorname{tr}M_N,\quad
\gamma_N=\tfrac12(d_1+d_2),\quad
\tau_N=\gamma_N/m_N>0.
\tag{5}
$$



Equations (4) and the reviewed off-diagonal bound imply



$$
\|M_N-m_NI\|\le(4/c+5/c^2)N,
\qquad \|\Gamma_N^T-\gamma_NI\|\le7N/4.
$$



Also



$$
M_N\succeq\frac{N^2}{64(C+1)}I,\quad
m_N\le\frac{N^2}{2c},\quad
N^2/8\le\gamma_N\le N^2/2.
$$



It follows that



$$
\boxed{T_N=\tau_N(I+E_N),\qquad
\|E_N\|\le\frac{K(c,C)}N,\quad
K(c,C)=64(C+1)(11/c+5/c^2),}
\tag{6}
$$



and (c/4\le\tau_N\le32(C+1)).
Indeed



$$
E_N=M_N^{-1}
\left[\frac{m_N}{\gamma_N}(\Gamma_N^T-\gamma_NI)
-(M_N-m_NI)\right],
$$



with (m_N/\gamma_N\le4/c). This proves (6) with the stated
constant. Both diagonal balance and small off-diagonal coupling
are used; a merely nearly diagonal transfer would not justify
this scalar normalization.

## 3. Accumulation over a dyadic interval

Fix (0<c_0\le C_0), (x\in[c_0n^2,C_0n^2]), and take
same-parity cuts (N=n+2,n+4,\ldots,m\le2n). The same constants
apply at every cut with (c=c_0/4), (C=C_0). Let
(K=K(c,C)), and assume (n\ge\max\{8,4/c,2K\}).
Define the actual positive scalar product



$$
S_{m,n}(x)=\prod_{N=n+2,n+4,\ldots,m}\tau_N(x).
$$



Then



$$
\boxed{P_m(x)=S_{m,n}(x)\,\mathcal U_{m,n}(x)P_n(x),
\quad
\|\mathcal U_{m,n}\|\le2^{K/2},\quad
\|\mathcal U_{m,n}^{-1}\|\le2^K.}
\tag{7}
$$



Here (\mathcal U_{m,n}) is the ordered product of the actual
(I+E_N), with larger cuts on the left. No commuting approximation
is made. Since



$$
\sum_{N=n+2,n+4,\ldots,m}\frac1N
\le\frac12\log(m/n),
$$



submultiplicativity and (\log(1+t)\le t) give the first norm
bound. The inequality ( -\log(1-t)\le2t) for (0\le t\le1/2)
gives the inverse bound. More precisely,



$$
\|\mathcal U_{m,n}-I\|
\le(m/n)^{K/2}-1.
\tag{8}
$$



Thus a full dyadic interval allows a bounded, generally nonvanishing
amount of normalized mixing. On a window (m-n=o(n)), this error
does tend to zero. An (O(1/N)) per-cut estimate has not been
summed and then incorrectly discarded.

## 4. Consequence and remaining scope

After dividing by the exact common scalar (S_{m,n}), all singular
values of the adjacent branch-pair matrix at cut (m) are comparable
to those at cut (n), within constants depending only on (c_0,C_0).
In particular its condition number changes by at most
(2^{3K/2}) over this window. This does not assert that the initial
matrix (P_n) is diagonal or well-conditioned.

The product remains a function of the spectral parameter (x).
The nodewise remainder matrix (A_{\mathrm{rem}}) from
`raw_separated_channel_low_evaluation.md` compares different
parameters and deletes prescribed low rows. Formula (7) alone
does not control those operations or their cancellations. A
sharper scalar factor and its variation are supplied by the local
resolvent limit in the next continuation; neither result alone is
a high-cofactor lower bound.
