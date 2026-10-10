> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 248 — local logarithmic tails and the joint-root Wronskian no-go

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the actual rows


$$
p=4h+6s+3=2r+6s+3,
 \qquad r=2h,\qquad h,s\geq1,                               \tag{1.1}
$$


and Item 245's leading pairs
$(\alpha_\nu,\beta_\nu)$, $\nu=0,1$.  They are the
reductions modulo $Q=1+Z^2$ of the two actual target sections.

**PROVED — an exact local-tail formula.**  For a root $I^2=-1$, put
$x=I^p$, so that $x^p=I$ and $x^2=-1$.  Define


$$
A_p(u)=-2\sum_{j=1}^{p-1}\frac{u^{j-1}}j.                   \tag{1.2}
$$


If $C_{\nu,a}(Z)$ is the $a$-th $p$-section of
$B_0^2P_\nu$, then


$$
\boxed{\begin{aligned}
 x^{a_0}C_{0,a_0}(I)
  &=[u^{n_0}]A_p(u)^2(1-u)^{2s}(2-u)^{2s}
       (1-x+xu)^r(1+x-xu),\\
 x^{a_1}C_{1,a_1}(I)
  &=[u^{n_1}]A_p(u)^2(1-u)^{2s-1}(2-u)^{2s-1}
       (1-x+xu)^r(1+x-xu)^4,
\end{aligned}}                                               \tag{1.3}
$$


where


$$
\begin{array}{c|ccc}
\nu&a_\nu&m_\nu&n_\nu\\ \hline
0&p-2s-1&2s+2&p-2s-3=2r+4s\\
1&p-2s&2s+1&p-2s-2=2r+4s+1.
\end{array}                                                   \tag{1.4}
$$


The Item 245 normalization is


$$
\alpha_\nu+\beta_\nu I
                   =-24C_{\nu,a_\nu}(I).                    \tag{1.5}
$$



**PROVED — a short exact coefficient recurrence.**  Every coefficient
in (1.3) is generated from a fourth-order Pearson recurrence whose
pivots are $4n$, with $1\leq n<p$.  Also,


$$
[u^k]A_p(u)^2=\frac{8H_{k+1}}{k+2}            \tag{1.6}
$$


for every required $k$; all displayed denominators are $p$-units.
This removes the large $B_0^2$ convolution from the root test.

**PROVED — individual nonvanishing is false.**  The exact admissible
row


$$
(p,h,s,\nu)=(59,2,8,1)                 \tag{1.7}
$$


has


$$
(\alpha_1,\beta_1)=(0,0),\qquad
       \operatorname {rank}\mathcal T_1=6.                  \tag{1.8}
$$


Thus no proof can show that each actual pair is nonzero on every row.

**PROVED — division-free Wronskian reduction.**  The two local
coefficients are second parameter derivatives of explicit
hypergeometric coefficients $F_\nu(\lambda)$.  Both have the forced
factor


$$
F_\nu(\lambda)=\lambda^{\underline{r+1}}G_\nu(\lambda).     \tag{1.9}
$$


Writing primes for $\lambda$-derivatives at zero gives


$$
\boxed{
 G_1'G_0-G_1G_0'
 =\frac{F_0'F_1''-F_1'F_0''}{2((-1)^rr!)^2}.}                \tag{1.10}
$$


Consequently a common local zero of the two Item 245 leading factors
forces the right side of (1.10) to vanish.  This statement never
divides by $G_0(0)$ or $G_1(0)$.

**PROVED — the universal Wronskian-unit strategy fails.**  When
$p\equiv1\pmod4$, rootwise nonvanishing is controlled by the norm of
a coefficient pair, not by whether the pair itself is nonzero.  The
normalized Wronskian in (1.10) has exact one-root zeros


$$
\begin{array}{c|c|c|c}
(p,h,s)&W=(a,b)&I&a+bI\\ \hline
(109,4,15)&(88,70)&33&0\\
(149,26,7)&(42,60)&44&0.
\end{array}                                                   \tag{1.11}
$$


Here $I^2=-1$ in the indicated prime field.  Thus a universal proof
that (1.10) is a rootwise unit is impossible.

This is a no-go only for that Wronskian-unit strategy.  It is not a
counterexample to joint nonvanishing of the original two leading
factors.

**EXACT FINITE ONLY.**  Through $p\leq601$, all 2,435 actual rows
contain 19 individual leading-root losses, including (1.7), but no
common leading root.  There are 17 rootwise zeros of some
$G_\nu(0)$ and seven rootwise Wronskian zeros.  None of these counts
is extrapolated.

**OPEN.**  An all-row exclusion of a common leading root remains open.
Item 248 books no common-log exclusion, density estimate, Route-1
rate, or conclusion about $e+\pi$.

## 2. Folding a section into one local root

For a polynomial $F(z)=\sum_nt_nz^n$, define


$$
C_a(Z)=\sum_{j\geq0}t_{a+jp}Z^j,
 \qquad0\leq a<p.                                             \tag{2.1}
$$


Then $C_a(I)$ is the coefficient of $z^a$ in the remainder of
$F$ modulo $z^p-I$.

Because Frobenius is an automorphism of the quadratic splitting field,


$$
x=I^p,\qquad x^p=I,qquad x^2=-1.                            \tag{2.2}
$$


Set


$$
z=x(1-u).                              \tag{2.3}
$$


The quotient by $z^p-I$ is then exactly the local algebra
$\overline{\mathbb F}_p[u]/(u^p)$.

The following folding lemma is the key coefficient conversion.

> **Local folding lemma.**  Suppose the image of $F(x(1-u))$ modulo
> $u^p$ is $u^mG(u)$, and put $a=p-m+1$.  Then
> 

$$
> x^aC_a(I)=[u^{p-m-1}](1-u)^{m-2}G(u).                      \tag{2.4}
>
$$



To prove it, write the remainder as


$$
R(z)=\sum_{b=0}^{p-1}r_bz^b.
$$


If


$$
R(x(1-u))=\sum_{k=0}^{p-1}d_ku^k,
$$


then the inverse binomial change of basis gives


$$
r_ax^a=(-1)^a\sum_{k=a}^{p-1}\binom ka d_k.                 \tag{2.5}
$$


Put $k=p-j$.  Since $a=p-m+1$,


$$
\binom{p-j}{p-m+1}
   =(-1)^{m-j-1}\binom{m-2}{j-1}\pmod p.                    \tag{2.6}
$$


Substituting $d_k=[u^{k-m}]G$ in (2.5) gives exactly the
coefficient on the right of (2.4).

This proof is rootwise.  It is valid whether $Q$ is irreducible or
split.

## 3. The truncated logarithm in the local coordinate

Put $T=1+z^2$.  Expanding the Item 234 polynomial


$$
B_0=\sum_{k=1}^{p-1}\frac{(-1)^{k-1}z^{2k}}k               \tag{3.1}
$$


in powers of $T$ gives the exact identity


$$
B_0=-\sum_{j=1}^{p-1}\frac{T^j}{j}.    \tag{3.2}
$$


For example, for $j\geq1$, the coefficient of $T^j$ is


$$
(-1)^{j+1}\sum_{k=j}^{p-1}\frac1k\binom kj
 =\frac{(-1)^{j+1}}j\binom{p-1}{j}
 =-\frac1j.                                                   \tag{3.3}
$$


The constant coefficient is $-H_{p-1}=0$.

Under (2.3),


$$
T=u(2-u),\qquad1-T=(1-u)^2.                                 \tag{3.4}
$$


The truncated formal logarithm is valid in
$\overline{\mathbb F}_p[u]/(u^p)$, because its only denominators are
$1,\ldots,p-1$.  Equations (3.2)--(3.4) yield


$$
B_0(x(1-u))=-2\sum_{j=1}^{p-1}\frac{u^j}{j}
                         =uA_p(u)\pmod {u^p}.                 \tag{3.5}
$$



The two products $B_0^2P_\nu$ have respective local orders


$$
m_0=2s+2,\qquad m_1=2s+1.           \tag{3.6}
$$


Applying (2.4) and inserting


$$
\begin{aligned}
1-z&=1-x+xu,&1+z&=1+x-xu,\\
1+z^2&=u(2-u)
\end{aligned}                                                 \tag{3.7}
$$


proves (1.3).

Finally, for $0\leq k\leq n_\nu\leq p-4$,


$$
\begin{aligned}
[u^k]A_p^2
 &=4\sum_{j=1}^{k+1}\frac1{j(k+2-j)}\\
 &=\frac{8H_{k+1}}{k+2}.                                    \tag{3.8}
\end{aligned}
$$


This proves (1.6) and the claimed integrality.

## 4. The fourth-order local Pearson recurrence

Let


$$
\begin{array}{ll}
\ell_1=1-u,&\ell_2=2-u,\\
\ell_3=1-x+xu,&\ell_4=1+x-xu.                               \tag{4.1}
\end{array}
$$


The four-factor polynomial in (1.3) is


$$
H_\nu(u)=\prod_{j=1}^4\ell_j(u)^{e_{\nu,j}},                \tag{4.2}
$$


with


$$
e_0=(2s,2s,r,1),\qquad e_1=(2s-1,2s-1,r,4).                \tag{4.3}
$$


The product of the four distinct linears is independent of $x$:


$$
D(u)=\prod_{j=1}^4\ell_j(u)
     =4-10u+10u^2-5u^3+u^4.                                 \tag{4.4}
$$


Define


$$
N_\nu(u)=\sum_{j=1}^4e_{\nu,j}\ell_j'(u)
                         \prod_{k\ne j}\ell_k(u).            \tag{4.5}
$$


Then


$$
DH_\nu'=N_\nu H_\nu.               \tag{4.6}
$$


Write $D=\sum_{j=0}^4d_ju^j$,
$N_\nu=\sum_{j=0}^3q_ju^j$, and
$H_\nu=\sum_{n\geq0}h_n u^n$.  Coefficient extraction at
$u^{n-1}$ gives


$$
\boxed{
4nh_n=
 \sum_{j=0}^3q_jh_{n-1-j}
 -\sum_{j=1}^4d_j(n-j)h_{n-j},}                              \tag{4.7}
$$


where out-of-range coefficients are zero.  Every required index has
$1\leq n<p$, so (4.7) uses only $p$-unit pivots.  Combining
(4.7) with (3.8) proves the claimed finite recurrence interface.

## 5. The forced $\lambda$-roots and the tail lemma

Define


$$
\begin{aligned}
F_0(\lambda)
 &=[u^{n_0+2}](1-u)^{2s+\lambda}(2-u)^{2s}
       (1-x+xu)^r(1+x-xu),\\
F_1(\lambda)
 &=[u^{n_1+2}](1-u)^{2s-1+\lambda}(2-u)^{2s-1}
       (1-x+xu)^r(1+x-xu)^4.                                \tag{5.1}
\end{aligned}
$$


Since


$$
A_p(u)^2=\frac{4\log^2(1-u)}{u^2}\pmod {u^{p-2}},           \tag{5.2}
$$


equation (1.3) becomes


$$
x^{a_\nu}C_{\nu,a_\nu}(I)=4F_\nu''(0).         \tag{5.3}
$$



Both coefficient targets in (5.1) exceed the degree at
$\lambda=0$ by exactly


$$
R=r+1.                         \tag{5.4}
$$


For each integer $0\leq j\leq r$, increasing the exponent by $j$
still leaves the target above the degree.  Hence


$$
F_\nu(0)=F_\nu(1)=\cdots=F_\nu(r)=0,                       \tag{5.5}
$$


which proves (1.9).

There is a useful general closed form.  Let $H(u)=\sum_{j=0}^dh_ju^j$
and


$$
F(\lambda)=[u^{d+R}](1-u)^\lambda H(u)
             =\lambda^{\underline R}G(\lambda).              \tag{5.6}
$$


Reversing the coefficient index gives


$$
F(\lambda)=\sum_{k=0}^dh_{d-k}(-1)^{R+k}
                              \binom\lambda{R+k}.             \tag{5.7}
$$


Factoring $\lambda^{\underline R}$ term by term yields


$$
\begin{aligned}
G(0)
 &=\frac{(-1)^R}{(R-1)!}
       \sum_{k=0}^d\frac{h_{d-k}}{R+k},\\
G'(0)-H_{R-1}G(0)
 &=-\frac{(-1)^R}{(R-1)!}
       \sum_{k=0}^d\frac{h_{d-k}H_{R+k-1}}{R+k}.             \tag{5.8}
\end{aligned}
$$


All denominators in (5.8) are $p$-units in the two applications.

For $A(\lambda)=\lambda^{\underline{r+1}}$,


$$
A'(0)=(-1)^rr!,\qquad A''(0)=-2H_rA'(0).                    \tag{5.9}
$$


Thus


$$
F_\nu''(0)=2(-1)^rr!\bigl(G_\nu'(0)-H_rG_\nu(0)\bigr).    \tag{5.10}
$$


Taking the two-by-two determinant of $F_\nu'(0)$ and
$F_\nu''(0)$ proves (1.10).

The ratio of the two polynomial inputs is exactly


$$
\frac{H_0(u)}{H_1(u)}
   =\frac{(1-u)(2-u)}{(1+x-xu)^3},                            \tag{5.11}
$$


and the targets differ by one.  Equations (5.8)--(5.11) reduce the
joint-root problem to a two-by-two logarithmic-moment determinant.
They do not prove that determinant is a rootwise unit.

## 6. The split-root audit and exact no-go examples

From (1.1),


$$
p\equiv
 \begin{cases}
 1\pmod4,&s\text{ odd},\\
 3\pmod4,&s\text{ even}.
 \end{cases}                                                  \tag{6.1}
$$


Represent an element of $\mathbb F_p[I]/(I^2+1)$ by a pair
$(a,b)=a+bI$.  Its norm is


$$
a^2+b^2.                        \tag{6.2}
$$



If $p\equiv3\pmod4$, the algebra is a field.  Norm zero is equivalent
to $(a,b)=(0,0)$, and a root loss occurs simultaneously at the two
conjugate roots.  The row (1.7) is of this type.  Its exact $Q$-adic
digits are


$$
(0,0),\ (37,41),\ (29,9),\ (51,58),\ (0,0)                 \tag{6.3}
$$


over $\mathbb F_{59}$, and its generalized state has rank six.

If $p\equiv1\pmod4$, the algebra splits.  A nonzero pair can vanish
at one root.  This is the distinction that invalidates a test based
only on $(a,b)\ne(0,0)$.

The logarithmic-derivative interpretation itself has exact split
exceptions.  At


$$
(p,h,s,\nu)=(41,2,5,0),                \tag{6.4}
$$


one has


$$
G_0(0)=(12,15),\qquad
 12+15\cdot9=24,\qquad12+15\cdot32=0\pmod {41}.              \tag{6.5}
$$


Thus division by $G_0(0)$ would be invalid at the root $I=32$.
The division-free identity (1.10) remains valid.

The normalized Wronskian counterexamples in (1.11) verify rootwise as


$$
\begin{aligned}
p=109:&\quad 88+70\cdot33=0,
              &88+70\cdot76=67,\\
p=149:&\quad 42+60\cdot44=0,
              &42+60\cdot105=84.                            \tag{6.6}
\end{aligned}
$$


All equalities are in their displayed prime fields, and the two roots
in each row square to $-1$.

Through $p\leq601$, the seven Wronskian root-loss rows are


$$
109,\ 149,\ 181,\ 241,\ 389,\ 521,\ 601.                  \tag{6.7}
$$


These are **EXACT FINITE ONLY**.  The first two nevertheless suffice as
exact counterexamples to a universal Wronskian-unit theorem.

## 7. Deterministic replay and finite census

The standard-library checker
`work/item248_j1_joint_root_reduction_certificate.py` verifies:

- the local formulas (1.3)--(1.6) against all 368 frozen Item 245
  coordinate values through $p\leq151$;
- 66 direct polynomial-versus-Pearson recurrence comparisons;
- the exact counterexample (1.7), including all five $Q$-adic digits
  and rank six;
- the rootwise norm distinction in every row through $p\leq601$;
- all exceptional $G$, Wronskian, individual, and joint-root records.

The corrected census through $p\leq601$ is


$$
\begin{array}{c|r}
\text{quantity}&\text{count}\\ \hline
\text{actual rows}&2435\\
\text{split rows }(p\equiv1\bmod4)&1189\\
\text{inert rows }(p\equiv3\bmod4)&1246\\
\text{individual leading-root losses}&19\\
\text{whole leading-pair zeros}&1\\
\text{common leading roots}&0\\
\text{rootwise }G_\nu(0)\text{ zeros}&17\\
\text{rootwise normalized-Wronskian zeros}&7.
\end{array}                                                   \tag{7.1}
$$


Every number in (7.1), including zero common roots, is
**EXACT FINITE ONLY**.

## 8. Consequence for Route 1

Item 248 makes three exact advances:

1. it replaces the large leading-pair convolution by a local harmonic
   coefficient and a fourth-order recurrence;
2. it disproves universal individual-pair nonvanishing;
3. it reduces common-root exclusion to a division-free Wronskian, then
   proves by exact split examples that the simplest universal-unit
   theorem for that Wronskian is false.

The original common-root problem survives.  A future argument would
have to control the intersection of the Wronskian-zero locus with the
two simultaneous second-derivative zeros, rather than exclude the
Wronskian-zero locus itself.

No all-prime common-log obstruction or asymptotic rate follows here.

## 9. Final ledger

### PROVED

- The local logarithm, folding lemma, and the two formulas (1.3).
- The harmonic-square formula and fourth-order Pearson recurrence.
- The forced $r+1$ parameter roots and division-free Wronskian
  identity.
- The individual-pair counterexample at $p=59$.
- The split-root $G_0(0)$ exception at $p=41$.
- The split-root Wronskian counterexamples at $p=109,149$, which
  disprove a universal rootwise-unit strategy.

### EXACT FINITE ONLY

- Every bounded census count and exceptional record in the certificate,
  including no common root through $p\leq601$.

### OPEN

- All-row nonexistence of a common leading root.
- A replacement invariant on the exceptional Wronskian locus.
- Any all-prime $p^3$ terminal obstruction or common-log exclusion.
- Any Route-1 rate or conclusion about $e+\pi$.
