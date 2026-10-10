> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Universal nonvanishing of the balanced centered-cosh quadratic

## A Jacobi--Trudi sign law and the forced-column factorial bound

Checked: 2026-08-27 UTC

## 1. Statement

Put



$$
F(x)=\frac1{2\cosh\sqrt x}.
$$



For $q\geq1$, let $P,Q\in\mathbb Q[x]$ be the normal diagonal
Padé pair



$$
\deg P=\deg Q=q,\qquad FQ-P=O(x^{2q+1}),\qquad Q(0)>0.     \tag{1}
$$



Define



$$
a_m=[x^m]\frac{P(x)^2}{Q(x)}.                             \tag{2}
$$



Then the two coefficients used by the balanced quadratic construction
never vanish.  In fact they have fixed signs:



$$
\boxed{a_{4q}>0,\qquad a_{4q+1}<0\qquad(q\geq1).}          \tag{3}
$$



Consequently the primitive polynomial



$$
\operatorname {prim}\bigl(a_{4q}-a_{4q+1}x\bigr)          \tag{4}
$$



is defined and has degree exactly one for every $q\geq1$.  In the
original even endpoint variable its degree is exactly two.

The proof uses more than generic Pólya-frequency normality.  It uses the
special elementary symmetric functions of the secant alphabet,



$$
e_j(t_0,t_1,\ldots)=\frac1{(2j)!}.                         \tag{5}
$$



That distinction is important: generic positive alphabets need not have
the coefficient sign law in (3).

## 2. The secant alphabet and the Padé cofactors

Set



$$
H(y)=2F(-y)=\sec\sqrt y
      =\prod_{\nu\geq0}(1-t_\nu y)^{-1}
      =\sum_{n\geq0}h_ny^n,                                \tag{6}
$$



where



$$
t_\nu=\frac4{\pi^2(2\nu+1)^2}>0.                          \tag{7}
$$



Thus $h_n=h_n(t_0,t_1,\ldots)$ is the complete homogeneous
symmetric function.  The product formula for $\cosh\sqrt y$ gives



$$
e_j(t_0,t_1,\ldots)=\frac1{(2j)!},\qquad
 h_1=\sum_{\nu\geq0}t_\nu=\frac12,\qquad
 t_0=\frac4{\pi^2}.                                        \tag{8}
$$



We use the convention



$$
s_\alpha=\det(h_{\alpha_i-i+j})_{1\leq i,j\leq\ell},
 \qquad h_0=1,\quad h_r=0\ (r<0),                          \tag{9}
$$



for an integer sequence $\alpha=(\alpha_1,\ldots,\alpha_\ell)$.
For a partition this is the ordinary Jacobi--Trudi formula.

Consider the $q\times(q+1)$ Padé matrix



$$
M_q=(h_{q+r-k})_{\substack{1\leq r\leq q\\0\leq k\leq q}}.
                                                                    \tag{10}
$$



For $0\leq k\leq q$, put



$$
\lambda^{(k)}=((q+1)^k,q^{\,q-k}),\qquad
 S_k=s_{\lambda^{(k)}}.                                    \tag{11}
$$



Deleting column $k$ from (10), transposing, and indexing its retained
columns by



$$
j_i=\begin{cases}i-1,&i\leq k,\\ i,&i>k,\end{cases}
$$



turns its $(i,r)$-entry into



$$
h_{q+r-j_i}=h_{\lambda_i^{(k)}-i+r}.
$$



Therefore the deleted-column minor is exactly $S_k>0$.  The signed
cofactor vector gives the denominator



$$
B(y)=\sum_{k=0}^q(-1)^kS_ky^k,\qquad B(0)=S_0>0,           \tag{12}
$$



and $M_q((-1)^kS_k)_k=0$.  In particular $M_q$ has rank $q$,
because $S_0=s_{(q^q)}>0$.

There is a unique polynomial $p$ for which



$$
BH-p=O(y^{2q+1}),\qquad \deg p=q.                          \tag{13}
$$



The transformed pair $(2P(-y),Q(-y))$ is a positive scalar multiple
of $(p,B)$.  It is enough to prove the sign theorem in the cofactor
normalization (12); positive rescaling will not change it.

## 3. One Jacobi--Trudi determinant controls numerator and error

Define



$$
\Phi_n=[y^n](BH)
       =\sum_{k=0}^q(-1)^kS_kh_{n-k}.                       \tag{14}
$$



Expand the Jacobi--Trudi determinant $s_{(q^q,n)}$, of length
$q+1$, along its last row.  Column $j=q+1-k$ contains
$h_{n-k}$, its cofactor sign is $(-1)^k$, and its remaining
minor is $S_k$.  Hence



$$
\boxed{\Phi_n=s_{(q^q,n)}.}                               \tag{15}
$$



This generalized Schur determinant straightens explicitly.  The shifted
row indices $\alpha_i-i$ of $\alpha=(q^q,n)$ are



$$
q-1,q-2,\ldots,0,n-q-1.                                  \tag{16}
$$



It follows that



$$
\Phi_n=
 \begin{cases}
 s_{(q^q,n)}>0,&0\leq n\leq q,\\
 0,&q<n\leq2q,\\
 (-1)^q s_{(n-q,(q+1)^q)},&n\geq2q+1.
 \end{cases}                                               \tag{17}
$$



Indeed, the first line is already a partition.  In the middle range the
last number in (16) duplicates one of $0,\ldots,q-1$, so two
Jacobi--Trudi rows coincide.  In the last range, moving the final shifted
index to the front takes $q$ transpositions and gives the partition
$(n-q,(q+1)^q)$.

Consequently



$$
p(y)=\sum_{n=0}^q s_{(q^q,n)}y^n                         \tag{18}
$$



has strictly positive coefficients, while the error



$$
E(y)=BH-p=\sum_{n\geq2q+1}\Phi_ny^n                       \tag{19}
$$



has coefficient sign $(-1)^q$.

## 4. Reduction of the target coefficients

From $BH=p+E$,



$$
\frac{p^2}{B}
 =BH^2-2HE+\frac{E^2}{B}
 =pH-HE+\frac{E^2}{B}.                                    \tag{20}
$$



Since $\operatorname {ord}_0E=2q+1$, the last term begins in degree
$4q+2$.  Thus, for $m\leq4q+1$,



$$
A_m:=[y^m]\frac{p^2}{B}=[y^m]H(p-E).                      \tag{21}
$$



If $q$ is odd, every nonzero coefficient of $E$ is negative by
(17), while $H$ and $p$ have strictly positive coefficients.
Therefore



$$
A_m>0\qquad(m\leq4q+1)             \tag{22}
$$



in the odd case.  Only even $q$ requires an estimate.

## 5. The forced-column bound for even $q$

Assume $q$ is even and $n\geq2q+1$.  Put



$$
\mu=(q^q),\qquad \Lambda_n=(n-q,(q+1)^q).                 \tag{23}
$$



The diagram of $\mu$ is contained in that of $\Lambda_n$.  The
Littlewood--Richardson expansion gives



$$
s_{\Lambda_n/\mu}=\sum_\nu c_{\mu\nu}^{\Lambda_n}s_\nu.
$$



After multiplication by $s_\mu$, the coefficient of
$s_{\Lambda_n}$ is
$\sum_\nu(c_{\mu\nu}^{\Lambda_n})^2\geq1$; all other Schur
coefficients are nonnegative.  Evaluation at the positive alphabet
$(t_\nu)$, first finitely and then by monotone convergence, proves



$$
\frac{s_{\Lambda_n}}{s_\mu}\leq s_{\Lambda_n/\mu}.         \tag{24}
$$



Here is a direct bound for the skew function.  In
$\Lambda_n/\mu$, column $q+1$ contains one box in every row
$1,\ldots,q+1$, hence exactly $q+1$ boxes.  The remaining boxes
are:

* $n-2q-1$ boxes in the first row to the right of that column; and
* $q$ boxes in the last row to the left of that column.

Thus there are $n-q-1$ remaining boxes.  Map a semistandard tableau
to the strictly increasing entries in the distinguished column and to
the entries in all remaining labelled boxes.  This is a
weight-preserving injection.  If all constraints on the remaining
boxes are discarded, summing the enlarged set gives



$$
s_{\Lambda_n/\mu}(t)
 \leq e_{q+1}(t)h_1(t)^{\,n-q-1}
 =\frac{2^{-(n-q-1)}}{(2q+2)!}.                            \tag{25}
$$



Equations (17), (24), and (25) therefore give



$$
0<\frac{\Phi_n}{S_0}
 \leq\frac{2^{-(n-q-1)}}{(2q+2)!}
 \qquad(q\ {\rm even},\ n\geq2q+1).                        \tag{26}
$$



Also,



$$
h_j\leq h_1^j=2^{-j},\qquad
 h_m\geq t_0^m=\left(\frac4{\pi^2}\right)^m.               \tag{27}
$$



The first inequality follows by enlarging weakly increasing
index-tuples to all ordered tuples; the second retains the monomial
$t_0^m$.

Since $p_0=S_0$, equations (18) and (26)--(27) yield



$$
[y^m](Hp)\geq S_0h_m
$$



and



$$
[y^m](HE)
 \leq
 S_0\frac{(m-2q)2^{-(m-q-1)}}{(2q+2)!}.                   \tag{28}
$$



Consequently $[y^m](HE)<[y^m](Hp)$ follows from



$$
{\cal R}_{q,m}:=
 \frac{(m-2q)2^{-(m-q-1)}}{(2q+2)!}
 \left(\frac{\pi^2}{4}\right)^m<1.                         \tag{29}
$$



## 6. The endpoint majorant is strictly below one

For $q\geq2$,



$$
\frac{{\cal R}_{q,4q+1}}{{\cal R}_{q,4q}}
 =\frac{\pi^2(2q+1)}{16q}>1,                               \tag{30}
$$



using $\pi^2>9$.  It is therefore enough to put



$$
U_q={\cal R}_{q,4q+1}
 =\frac{(2q+1)2^{-3q}}{(2q+2)!}
  \left(\frac{\pi^2}{4}\right)^{4q+1}.                    \tag{31}
$$



The elementary bound $\pi^2<10$ gives



$$
U_2<
 \frac{5^{10}}{720\cdot2^{15}}<1.                         \tag{32}
$$



Moreover,



$$
\frac{U_{q+1}}{U_q}
 =\frac{\pi^8}{2048(2q+1)(2q+4)}
 <\frac{10^4}{2048\cdot5\cdot8}<1
 \qquad(q\geq2).                                          \tag{33}
$$



Thus ${\cal R}_{q,4q},{\cal R}_{q,4q+1}<1$ for every
$q\geq2$.  Equations (21), (28), and (29) prove



$$
A_{4q}>0,\qquad A_{4q+1}>0                                \tag{34}
$$



for even $q$, completing the cofactor-normalized proof.

## 7. Return to $P,Q$ and exact signs

Let $B_*(y)=Q(-y)$ and $p_*(y)=2P(-y)$ for the normalization
in (1).  Uniqueness and $Q(0)>0$ give



$$
B_*=cB,\qquad p_*=cp,\qquad c=\frac{Q(0)}{S_0}>0.         \tag{35}
$$



Therefore



$$
[y^m]\frac{p_*^2}{B_*}
 =cA_m
 =4[y^m]\frac{P(-y)^2}{Q(-y)}
 =4(-1)^ma_m.                                              \tag{36}
$$



Equations (22), (34), and (36) prove (3), including all signs and the
factor $4$.

## 8. Consequences and logical boundary

The earlier residue identity for the balanced residual functional was



$$
h_j^{\rm res}
 =-\frac{\operatorname {lc}(Q)}{\kappa^2}
   a_{4q+1-j}\qquad(j=0,1).                                \tag{37}
$$



Equation (3) proves that both first moments in (37) are nonzero, not
merely that their pair is nonzero.  It removes the last conditional
nonvanishing clause from the balanced quadratic border construction;
it does not alter any of that package's frozen identities.

The theorem is a local algebraic-sign result.  It does not estimate the
primitive content $K_q$, prove a lower bound for the primitive
quadratic height, control the normalized global lift height, or classify
$e+\pi$.

The companion files are:

* scripts/centered_cosh_balanced_quadratic_nonvanishing_certificate.py
* results/centered_cosh_balanced_quadratic_nonvanishing_certificate.json
* results/centered_cosh_balanced_quadratic_nonvanishing_hashes.sha256

The deterministic replay checks all Padé, cofactor, Jacobi--Trudi,
straightening, endpoint-sign, forced-column count, and rational
majorant identities on a declared exact grid.  Finite checks are not
used in the all-parameter proof.
