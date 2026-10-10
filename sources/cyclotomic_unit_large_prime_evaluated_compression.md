> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact evaluated compression on the large-prime $u_7^d$ branch

## Status

Let $p\nmid20$ be prime, $1\le d<p$, and
$r=p-1-d$. Assume the derangement root



$$
E_d(-1)=0\pmod p.
\tag{1}
$$



The boundary-resultant construction introduces a primitive polynomial
$R_{p,r}$ of degree $p-2$ and the evaluated resultant



$$
\mathcal M_{p,r}=R_{p,r}(a)R_{p,r}(b),
 \qquad a=\eta^{-1},\quad b=\bar\eta^{-1}.
\tag{2}
$$



This note proves that evaluation removes all of the apparent moving
factorial coefficient family. Exactly modulo $p$,



$$
\boxed{
 \mathcal M_{p,r}=\chi_p^{-1}Z_d,
 \qquad
 Z_d=P_d(\eta)P_d(\bar\eta),
 \qquad \chi_p=q^{p-1}.}
\tag{3}
$$



After the scalar $\chi_p$ is cancelled, the norm-one equation is the
fixed bilinear trace equation



$$
\boxed{
 \operatorname {Tr}_{F/\mathbb Q}(Z_dT_d)=0\pmod p,
 \qquad
 T_d=\operatorname {Tr}_{K/F}(u_7^d).}
\tag{4}
$$



Thus the evaluated problem does lie on a fixed bidegree-$(1,1)$ curve,
and $Z_d$ satisfies an explicit order-four polynomial recurrence.
However, the curve is a nondegenerate rational graph, so membership in it
alone gives no restriction. Equation (4) is exactly the original trace
congruence in compressed coordinates; it is not a new uniform bound on
the selected gcd.

This distinction is important. The large primitive coefficient height
of $R_{p,r}$ does **not** transfer to a lower bound for the intrinsic
height of its evaluated conjugate ratio. Conversely, the compression
(3) does not control the coordinate content or prime divisors of $Z_d$.

This is an exact algebraic compression and an obstruction to obtaining a
uniform restriction merely from the resultant presentation. It proves
nothing about the arithmetic nature of $e+\pi$.

The exact symbolic certificate is
<scripts/cyclotomic_unit_large_prime_evaluated_compression.py>, with
output
<results/cyclotomic_unit_large_prime_evaluated_compression.json>.

## 1. Wilson reversal after evaluation

Use the integer polynomial



$$
P_d(X)=\sum_{j=0}^d(-1)^{d-j}\frac{d!}{j!}X^j
       =(-1)^dd!E_d(-X).
\tag{5}
$$



The boundary tail and its quotient are



$$
S_{p,r}(Y)=\sum_{k=r}^{p-1}k!Y^k,
 \qquad S_{p,r}(Y)=(Y-1)Q_{p,r}(Y).
\tag{6}
$$



The integer lift in the norm-one obstruction theorem reduces to



$$
R_{p,r}=\frac{Q_{p,r}}{r!}\pmod p.
\tag{7}
$$



The sign-sensitive boundary identity says



$$
E_d(-x)=-x^{p-1}S_{p,r}(x^{-1}).
\tag{8}
$$



Put $x=\eta$ and $a=\eta^{-1}$. Equations (6)--(8) give



$$
Q_{p,r}(a)
   =-\frac{a^{p-1}E_d(-\eta)}{a-1}.
\tag{9}
$$



Wilson's theorem, with $r=p-1-d$, gives the exact sign



$$
d!r!=(-1)^{d+1},
 \qquad
 \frac1{r!}=(-1)^{d+1}d!\pmod p.
\tag{10}
$$



Substituting (5) and (10) into (9) proves



$$
\boxed{
 R_{p,r}(a)=a^{p-1}\frac{P_d(\eta)}{a-1}.}
\tag{11}
$$



The same calculation with $b=\bar\eta^{-1}$ gives



$$
\boxed{
 R_{p,r}(b)=b^{p-1}\frac{P_d(\bar\eta)}{b-1}.}
\tag{12}
$$



Now



$$
ab=q^{-1},
 \qquad
 (a-1)(b-1)=1.
\tag{13}
$$



Multiplying (11) and (12) proves (3). No asymptotic estimate or
coefficient-height argument enters this identity.

## 2. Cancellation of the Frobenius scalar

Let $\iota$ be the nontrivial conjugation of
$F=\mathbb Q(\sqrt5)$, and define



$$
\delta(x)=\frac{\iota(x)}x.
\tag{14}
$$



At a nonzero boundary cancellation, the norm-one equation is



$$
\delta(\mathcal M_{p,r})
   =-\frac{\chi_pW_{c,r}}{\iota(\chi_pW_{c,r})},
\tag{15}
$$



where



$$
W_{c,r}=\operatorname {Tr}_{K/F}
 \bigl(\sigma_c(u_7)u_7^{-r-1}\bigr).
\tag{16}
$$



Equation (3) transforms the left side of (15) into



$$
\delta(\chi_p^{-1}Z_d)
   =\frac{\chi_p}{\iota(\chi_p)}
      \frac{\iota(Z_d)}{Z_d}.
\tag{17}
$$



The identical scalar occurs on the right side and cancels. Therefore



$$
\boxed{
 \frac{\iota(Z_d)}{Z_d}
   =-\frac{W_{c,r}}{\iota(W_{c,r})}.}
\tag{18}
$$



Frobenius gives



$$
u_7^d=u_7^{p-1-r}
 \equiv\sigma_c(u_7)u_7^{-r-1}\pmod p,
\tag{19}
$$



and hence $W_{c,r}=T_d\pmod p$. Cross-multiplying (18) now gives
exactly (4). The cross-multiplied form remains meaningful if one of the
two factors vanishes; the quotient form (18) is asserted only when both
are nonzero.

## 3. The fixed rational curve

Put



$$
t=\zeta_5+\zeta_5^{-1},
 \qquad t^2+t-1=0,
 \qquad F=\mathbb Q(t).
\tag{20}
$$



Write



$$
Z_d=z_0+z_1t,
 \qquad T_d=w_0+w_1t.
\tag{21}
$$



Since $\operatorname {Tr}_{F/\mathbb Q}(A+Bt)=2A-B$, equation (4)
is



$$
\boxed{
 2z_0w_0-z_0w_1-z_1w_0+3z_1w_1=0\pmod p.}
\tag{22}
$$



The trace-pairing matrix is



$$
\begin{pmatrix}2&-1\\-1&3\end{pmatrix},
 \qquad \det=5.
\tag{23}
$$



Because $p\ne5$, (22) is a nondegenerate bidegree-$(1,1)$ curve in
$\mathbb P^1\times\mathbb P^1$. For every projective $Z$ there is
exactly one projective $T$ trace-orthogonal to it. Thus the curve is a
rational graph, not a proper subgroup or a positive-genus curve on which
uniform finiteness follows automatically. Any restriction must use the
two specific recurrence orbits $Z_d,T_d$, together with the separate
derangement root (1).

## 4. A fixed order-four recurrence for $Z_d$

For $n\ge1$, the polynomials in (5) satisfy



$$
P_{n+1}(X)=(X-n-1)P_n(X)+nX P_{n-1}(X).
\tag{24}
$$



At $n=0$, the same transition gives $P_1=(X-1)P_0$, because the
coefficient of the unused $P_{-1}$ is zero. Hence it can be used in
the tensor calculation starting at $n=0$.

Tensoring this order-two recurrence at $X=\eta$ and
$X=\bar\eta$, and reducing with
$\eta+\bar\eta=1$, gives



$$
\boxed{
 \sum_{j=0}^4\bigl(A_j(n)+tB_j(n)\bigr)Z_{n+j}=0
 \qquad(n\ge0).}
\tag{25}
$$



The coefficient polynomials are as follows.



$$
\begin{array}{c|l|l}
j&A_j(n)&B_j(n)\\ \hline
0&(n+1)^2(n+2)(n+3)(2n^2+14n+19)
  &-(n+1)^2(n+2)(n+3)(3n^2+21n+28)\\
1&-(n+2)(n+3)(n^4+10n^3+35n^2+54n+31)
  &(n+2)(n+3)(n^4+10n^3+35n^2+56n+34)\\
2&-(n+3)^2(n^3+7n^2+13n+8)
  &-(n+3)^2(2n^2+13n+14)\\
3&-(n^2+6n+7)(n^2+6n+10)&-3\\
4&n^2+5n+5&1
\end{array}
\tag{26}
$$



This is an all-degree identity in $\mathcal O_F$. The certificate does
not guess it from data: it forms the four-dimensional tensor transition
matrix associated with (24) and verifies (25)--(26) symbolically in
$\mathbb Z[n,\zeta_5]/(\Phi_5)$.

The unit trace has the much simpler recurrence



$$
\boxed{
 T_0=2,\quad T_1=4+2t,\quad
 T_{n+2}=(4+2t)T_{n+1}+(2+t)T_n.}
\tag{27}
$$



Indeed,



$$
\operatorname {Tr}_{K/F}(u_7)=4+2t,
 \qquad
 \operatorname {N}_{K/F}(u_7)=-2-t.
\tag{28}
$$



Equations (25) and (27) compress the evaluated dynamics to two fixed
recurrences. They do not, by themselves, bound the primes dividing the
simultaneous integer sequence in (4).

## 5. Exact verdict

The moving degree-$(p-2)$ resultant admits a complete evaluated
compression: after Wilson reversal and removal of its Frobenius scalar,
it is just $Z_d$. The resulting norm-one equation is a fixed rational
bilinear curve, and both coordinate sequences are fixed-order recurrent.

This is algebraically sharper than the coefficient-height formulation,
but it exposes rather than resolves the arithmetic obstacle. Equation
(22) is exactly the original trace congruence, and the nondegenerate
trace pairing allows every projective value in the ambient space. The
four certified large-prime witnesses show that the two specific orbits
do meet on this curve in every Frobenius class. A uniform large-prime
bound would require a theorem controlling prime divisors in the
intersection of the derangement recurrence (1) with the fixed
P-recursive/C-finite trace sequence (4); no such theorem is proved here.
