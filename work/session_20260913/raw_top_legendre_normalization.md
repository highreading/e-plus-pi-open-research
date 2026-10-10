> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# What the actual normalization forces in Legendre coordinates

Date: 2026-09-13. Root deduction from the independently reviewed
factorial mass and endpoint representer theorems. This is a structural
constraint, not a concentration theorem for the remaining modes.

Use the reflected polynomial



$$
P_n(t)=\sum_{j=0}^n B_{n,j}\frac{t^{n-j}}{(n-j)!},
 \qquad \mathfrak b(P)=\sum_{r=0}^n P^{(r)}(0).
$$



Then the actual normalization is exactly b(P_n)=B_n(1)=1. Put
J_l(t)=P_l(2t-1), and phi_l=sqrt(2l+1) J_l. The phi_l form an
orthonormal basis on [0,1]. Write P_n=sum_l a_l phi_l.

## 1. A positive factorial sequence for the endpoint functional

The exact derivative formula at t=0 gives



$$
b_l:=\mathfrak b(J_l)
 =\sum_{r=0}^l(-1)^{l-r}\frac{(l+r)!}{(l-r)!r!}
 =\frac{(2l)!}{l!}\sigma_l,
$$





$$
\sigma_l=\sum_{s=0}^l\frac{(-1)^s}{s!}
                 \frac{(l)_{\underline s}}{(2l)_{\underline s}}.
\tag{1}
$$



For l>=1, the consecutive absolute summand ratio is at most
1/[2(s+1)]. The alternating-series bound gives 1/2<=sigma_l<=1.
Dominated summation gives sigma_l->exp(-1/2); in fact sigma_l equals
exp(-1/2)+O(1/l). One direct rate proof compares each falling-factorial
ratio with 2^(-s). Its relative discrepancy is at most a constant
times s(s-1)/l until that bound exceeds one, after which the trivial
bound suffices. The summable majorant s² 2^(-s)/s! gives the stated
rate, with the omitted tail bounded by the same exponential series.

Thus z_l:=b(phi_l)=sqrt(2l+1)b_l is positive, and



$$
\frac{z_{l-1}}{z_l}
 =\sqrt{\frac{2l-1}{2l+1}}
   \frac{1}{2(2l-1)}\frac{\sigma_{l-1}}{\sigma_l}
 =\frac1{4l}+O(l^{-2}).
\tag{2}
$$



The elementary upper bound z_(l-1)/z_l<=1/(2l-1) for l>=2 also yields



$$
\frac{(\sum_{l=0}^{n-1}z_l^2)^{1/2}}{z_n}=O(1/n),
 \qquad
 \frac{(\sum_{l=0}^{n-2}z_l^2)^{1/2}}{z_n}=O(1/n^2).
\tag{3}
$$



The finitely many small indices do not affect these bounds. Stirling's
formula gives z_n asymptotic to sqrt(2/pi) exp(-1/2) 4^n n!, as in the
existing inverse-norm audit.

## 2. The top mode is necessarily small

The identity sum_l z_l a_l=1 implies exactly



$$
a_n=\frac1{z_n}-\frac{z_{n-1}}{z_n}a_{n-1}
                    -\sum_{l=0}^{n-2}\frac{z_l}{z_n}a_l.
$$



Using (2)-(3),



$$
\boxed{a_n=-\left(\frac1{4n}+O(n^{-2})\right)a_{n-1}
               +O(\|P_n\|_2/n^2)+\frac1{z_n}.}
\tag{4}
$$



This is an all-degree estimate with absolute constants for sufficiently
large n. It uses the actual normalization, with its sign unchanged by
reflection.

The proved mass lower bound ||P_n||1>=n! exp(-O(n)) implies the same
lower bound for ||P_n||2. Therefore



$$
\frac{1}{z_n\|P_n\|_2}\le\frac{\exp(O(n))}{(n!)^2}.
\tag{5}
$$



Combining (3)-(5) proves



$$
\boxed{\frac{|a_n|}{\|P_n\|_2}=O(1/n),\qquad
 \frac{\|\operatorname{Proj}_{\le n-1}P_n\|_2^2}
      {\|P_n\|_2^2}=1-O(n^{-2}).}
\tag{6}
$$



Thus a claim that P_n is asymptotically dominated in L2 by phi_n would
contradict the already proved normalization and mass facts. Formula (4)
allows the adjacent top modes to cancel in b while adding at t=0.
It does not prove that a_(n-1) dominates the remaining coefficients.

If Z_n=sum z_l phi_l is the Riesz representer, (5) also gives the exact
angle consequence



$$
\frac{|\langle P_n,Z_n\rangle|}
 {\|P_n\|_2\|Z_n\|_2}
 \le\frac{\exp(O(n))}{(n!)^2}.
\tag{7}
$$



The increasingly strong endpoint cancellation is forced by the actual
equations. It cannot be removed by choosing another overall scale.

## 3. An exact link to the first root sum of B

Write P_n=sum_l p_l J_l, where p_l=sqrt(2l+1)a_l. Whenever B has
degree n, its first relative coefficient is



$$
\beta_n=\frac{B_{n,n-1}}{B_{n,n}}
         =\frac{P_n'(0)}{P_n(0)}.
$$



Since J_l(0)=(-1)^l and J_l'(0)=(-1)^(l-1)l(l+1),



$$
\boxed{
 \beta_n=-\frac{\sum_{l=0}^n(-1)^l l(l+1)p_l}
                 {\sum_{l=0}^n(-1)^l p_l}.}
\tag{8}
$$



Equivalently, putting S_n=P_n(0)!=0,



$$
\beta_n+n(n+1)
 =\frac{\sum_{l=0}^n(-1)^l(n-l)(n+l+1)p_l}{S_n}.
\tag{9}
$$



For example, a sufficient high-mode criterion for beta_n/n²->-1 is:
there are w_n=o(n), a fixed C, and nonzero S_n such that



$$
\sum_{l=0}^n|p_l|\le C|S_n|,\qquad
 \sum_{l<n-w_n}|p_l|=o(|S_n|).
\tag{10}
$$



Indeed the top band in (9) contributes at most
C w_n(2n+1)/n² after normalization, and the lower band contributes
o(1). This criterion retains endpoint noncancellation explicitly.
Unqualified L2 concentration by itself does not supply a lower bound
for |S_n|.

The concentration and noncancellation assumptions in (10) are unproved.
The exact new deductions here are (4), (6)-(9) and the sufficient
implication (10), which can guide the banded Legendre transfer analysis.
They do not estimate the primitive denominator or the actual mixed
remainder.
