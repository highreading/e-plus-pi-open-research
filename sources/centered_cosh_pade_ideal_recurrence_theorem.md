> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A Padé-ideal theorem for the balanced centered-cosh product spaces

Checked: 2026-08-27 UTC

## 1. Scope and theorem

Put



$$
F(x)=\frac1{2\cosh\sqrt x}=\sum_{j\geq0}f_jx^j,
 \qquad {\cal P}_d=\mathbb Q[x]_{\leq d}.                    \tag{1}
$$



Let $Q_q\in\mathbb Q[x]$ be a nonzero diagonal $[q/q]$ Padé
denominator for $F$, normalized arbitrarily.  Thus



$$
\deg Q_q=q,
 \qquad
 [x^j](FQ_q)=0\quad(q+1\leq j\leq2q).                       \tag{2}
$$



For $r\in\{1,2\}$, set



$$
n=3q+r,\qquad D=n-1,\qquad
 {\cal U}_{q,r}=
 \left\{C\in\mathbb Q[z]_{\leq D}:
 [z^k]F(z^2)C(z)=0\ (n\leq k\leq n+q)\right\}.             \tag{3}
$$



Let ${\cal E}_{q,r}$ be the even endpoint-product image,



$$
{\cal E}_{q,r}=
 \operatorname {span}_{\mathbb Q}
 \left\{\frac{C(z)D(z)+C(-z)D(-z)}2:
 C,D\in{\cal U}_{q,r}\right\},                              \tag{4}
$$



identified with a subspace of $\mathbb Q[x]$ by $x=z^2$.

The exact all-parameter ideal inclusions are



$$
\boxed{
 Q_q{\cal P}_{2q}\subseteq{\cal E}_{q,1}\quad(q\geq2),
 \qquad
 xQ_q{\cal P}_{2q}\subseteq{\cal E}_{q,2}\quad(q\geq1).}    \tag{5}
$$



The omitted edge is a genuine exception:



$$
{\cal E}_{1,1}=Q_1^2{\cal P}_1,
 \qquad
 Q_1{\cal P}_2\not\subseteq{\cal E}_{1,1}.                  \tag{6}
$$



Consequently, if a coefficient functional



$$
L_h\left(\sum_j a_jx^j\right)=\sum_jh_ja_j                \tag{7}
$$



annihilates the relevant even product image, then it obeys the finite
Padé recurrence



$$
\sum_{k=0}^q [x^k]Q_q\,h_{j+k}=0
 \quad(0\leq j\leq2q)                                      \tag{8}
$$



for $r=1,\ q\geq2$, and



$$
\sum_{k=0}^q [x^k]Q_q\,h_{j+1+k}=0
 \quad(0\leq j\leq2q)                                      \tag{9}
$$



for $r=2,\ q\geq1$.

Equations (5), (8), and (9) do **not** assert that the annihilator is
one-dimensional.  A separate codimension-one theorem for
${\cal E}_{q,r}$ would be needed for uniqueness.  The result here is the
rigorous ideal/recurrence part of the observed Smith-quotient pattern.

## 2. Parity blocks

Write



$$
C(z)=A(x)+zB(x),\qquad x=z^2.                               \tag{10}
$$



For $\epsilon\in\{0,1\}$, define



$$
d_\epsilon=\left\lfloor\frac{D-\epsilon}{2}\right\rfloor,
 \qquad
 I_\epsilon=
 \left\{\frac{k-\epsilon}{2}:
 n\leq k\leq n+q,\ k\equiv\epsilon\pmod2\right\},           \tag{11}
$$



and



$$
V_\epsilon=
 \left\{R\in{\cal P}_{d_\epsilon}:
 [x^j](FR)=0\ (j\in I_\epsilon)\right\}.                    \tag{12}
$$



Then



$$
{\cal E}_{q,r}=V_0V_0+xV_1V_1,                             \tag{13}
$$



where a product of spaces denotes the linear span of pairwise products.

For $r=1$, the parameters needed below are as follows.

If $q=2a$, then



$$
d_0=3a,\qquad I_0=[3a+1,4a],\qquad |I_0|=a.                \tag{14}
$$



If $q=2a+1$, then the two parity blocks coincide:



$$
V_0=V_1=:V,\qquad
 d_0=d_1=3a+1,\qquad
 I_0=I_1=[3a+2,4a+2],\qquad |I_0|=a+1.                     \tag{15}
$$



## 3. Padé division

Choose $P_q\in{\cal P}_q$ so that



$$
FQ_q=P_q+O(x^{2q+1}).                  \tag{16}
$$



Suppose $I=[A,B]\subseteq[q+1,2q]$, $c=B-A+1$, and



$$
V=\{R\in{\cal P}_d:[x^j](FR)=0\ (A\leq j\leq B)\},
 \qquad m=d-q,                                               \tag{17}
$$



with $m\geq0$ and $q+m<A$.  Polynomial division by $Q_q$
then gives the exact direct sum



$$
\boxed{
 V=Q_q{\cal P}_m\ \oplus\ W,
 \qquad
 W=\{R\in{\cal P}_{q-1}:[x^j](FR)=0\ (A\leq j\leq B)\}.}    \tag{18}
$$



Indeed, if $H\in{\cal P}_m$, then (16) and
$\deg(P_qH)\leq q+m<A$ show that $Q_qH\in V$.  Dividing any
$R\in V$ by $Q_q$ leaves a unique remainder in ${\cal P}_{q-1}$,
and the same calculation shows that this remainder lies in $W$.

## 4. The Schur-controllability lemma

Let



$$
{\cal A}_q=\mathbb Q[x]/(Q_q),                  \tag{19}
$$



and let $T$ be multiplication by $x$ on ${\cal A}_q$.  We use the
unique representatives of degree at most $q-1$.  Define



$$
\phi_j(R)=[x^j](FR),\qquad R\in{\cal P}_{q-1}.              \tag{20}
$$



If $q+1\leq j\leq2q$, then



$$
T^*\phi_j=\phi_{j-1}.               \tag{21}
$$



To see this, write $Q_q=\sum_{k=0}^qq_kx^k$, with $q_q\ne0$, and
$R=\sum_{k=0}^{q-1}r_kx^k$.  The representative of $xR$ modulo
$Q_q$ is



$$
xR-\frac{r_{q-1}}{q_q}Q_q.
$$



Applying $\phi_j$, the correction vanishes by (2), proving (21).

The required independence is not a finite-grid assumption.  From



$$
\cosh\sqrt x=\prod_{\ell\geq0}(1+t_\ell x),
 \qquad
 t_\ell=\frac4{\pi^2(2\ell+1)^2}>0,                          \tag{22}
$$



one has



$$
f_j=\frac{(-1)^j}{2}h_j(t_0,t_1,\ldots),                   \tag{23}
$$



where $h_j$ is the complete homogeneous symmetric function.  Assume
$c+1\leq q$.  In the coordinate matrix of
$\phi_{A-1},\ldots,\phi_B$, select the $c+1$ columns



$$
q-c-1,q-c,\ldots,q-1.                 \tag{24}
$$



After harmless row and column signs, the resulting determinant is



$$
2^{-(c+1)}
 \det[h_{L+r-s}]_{r,s=0}^c
 =2^{-(c+1)}s_{(L^{c+1})}(t_0,t_1,\ldots)>0,
 \qquad L=A-q+c.                                            \tag{25}
$$



The equality is Jacobi--Trudi after reversing both rows and columns.
Strict positivity follows from $t_\ell>0$.  Hence



$$
\phi_{A-1},\phi_A,\ldots,\phi_B
                 \quad\hbox{are linearly independent}.      \tag{26}
$$



Put $U=\operatorname {span}(\phi_A,\ldots,\phi_B)$.  If
$\lambda,(T^*)\lambda,\ldots,(T^*)^c\lambda$ all lie in $U$,
then $\lambda=0$.  Indeed, write
$\lambda=\sum_{j=A}^Bb_j\phi_j$.  Equations (21) and (26), applied
successively, force



$$
b_A=b_{A+1}=\cdots=b_B=0.           \tag{27}
$$



Since $W=\bigcap_{j=A}^B\ker\phi_j$, duality now gives the
controllability statement



$$
\boxed{
 \operatorname {span}\{x^sW:0\leq s\leq c\}
       ={\cal A}_q.}                                        \tag{28}
$$



This is the only rank input in the ideal proof.  Its certificate is the
single positive Schur minor (25).

## 5. Proof for $n=3q+1$

First let $q=2a\geq2$.  Use the even block (14).  In (17)--(18),



$$
d=3a,\qquad c=m=a,\qquad A=3a+1.          \tag{29}
$$



Here $L=A-q+c=q+1$, and $c+1\leq q$, so (28) applies.  Set



$$
{\cal L}={\cal P}_aV_0.             \tag{30}
$$



It is contained in ${\cal P}_{2q}$.  By (18), it contains
$Q_q{\cal P}_{2a}=Q_q{\cal P}_q$, which is exactly the kernel of
the reduction map



$$
{\cal P}_{2q}\longrightarrow{\cal A}_q. \tag{31}
$$



Its reduction is all of ${\cal A}_q$ by (28).  Therefore



$$
{\cal P}_aV_0={\cal P}_{2q}.         \tag{32}
$$



Because $Q_q{\cal P}_a\subseteq V_0$, products inside $V_0V_0$
now contain



$$
Q_q({\cal P}_aV_0)=Q_q{\cal P}_{2q}.     \tag{33}
$$



Next let $q=2a+1\geq3$.  Use the common block $V$ in (15).  Now



$$
d=3a+1,\qquad c=a+1,\qquad m=a,\qquad A=3a+2.         \tag{34}
$$



Again $L=A-q+c=q+1$ and $c+1\leq q$.  The even product image
$V^2+xV^2$ contains



$$
Q_q\bigl({\cal P}_aV+x{\cal P}_aV\bigr)
       =Q_q({\cal P}_{a+1}V).                               \tag{35}
$$



The space ${\cal P}_{a+1}V\subseteq{\cal P}_{2q}$ contains
$Q_q{\cal P}_q$, and its reduction modulo $Q_q$ is all of
${\cal A}_q$ by (28).  Thus



$$
{\cal P}_{a+1}V={\cal P}_{2q},        \tag{36}
$$



and (35) proves the first inclusion in (5).

For the exceptional value $q=1$, both parity blocks in (15) are the
one-dimensional space $\mathbb QQ_1$.  This proves (6).  Notice that
the Schur argument correctly stops here: in this case the proposed
$c+1=2$ independent functionals live on the one-dimensional algebra
${\cal A}_1$.

## 6. Proof for $n=3q+2$

For $q\geq2$, multiplication by $z$ gives an injection



$$
z{\cal U}_{q,1}\subseteq{\cal U}_{q,2}. \tag{37}
$$



Indeed, it raises the endpoint degree bound from $3q$ to $3q+1$,
and it moves the zero-coefficient interval
$[3q+1,4q+1]$ to $[3q+2,4q+2]$.  Products of two injected factors
are multiplied by $z^2=x$.  The already proved $r=1$ inclusion
therefore gives



$$
xQ_q{\cal P}_{2q}\subseteq{\cal E}_{q,2}.\tag{38}
$$



It remains to prove $q=1$.  Write $f_j=[x^j]F$ and put



$$
A=f_1,\qquad B=f_2,\qquad C=f_3,\qquad
 Q_1=A-Bx,\qquad u=B-Cx,\qquad v=xQ_1.                       \tag{39}
$$



The odd parity factor space is $\mathbb QQ_1$, while the even factor
space is $\operatorname {span}(u,v)$.  Moreover,



$$
B\ne0,\qquad A C-B^2\ne0.                                  \tag{40}
$$



Indeed, (23) makes $B=h_2/2>0$, while $B^2-AC$ is a positive
multiple of the Schur value $s_{(2,2)}(t_0,t_1,\ldots)$.  Direct
polynomial identities give



$$
\begin{aligned}
 xQ_1&=\frac{-Buv+CxQ_1^2}{AC-B^2},\\
 x^2Q_1&=\frac{-Auv+BxQ_1^2}{AC-B^2},\\
 x^3Q_1&=-\frac{A^2}{B(AC-B^2)}uv-\frac1Bv^2
             +\frac{A}{AC-B^2}xQ_1^2.
 \end{aligned}                                              \tag{41}
$$



Every term on the right belongs to
$V_0V_0+xV_1V_1={\cal E}_{1,2}$.  The three left sides span
$xQ_1{\cal P}_2$, finishing the proof of (5).

## 7. Arithmetic boundary

The theorem replaces a generic large cofactor certificate for the
balanced product image by the degree-$q$ Padé polynomial $Q_q$ as an
exact recurrence certificate.  Standard cofactor clearing for the
diagonal Padé system has logarithmic size $O(q^2\log q)$, rather than
the ambient product-system $O(n^3\log n)$ majorant.  This statement is
only a bound for the **recurrence ideal**.  It is not yet a bound for a
primitive nonzero class in the residual quotient



$$
{\cal E}_{q,r}/(x^{r-1}Q_q{\cal P}_{2q}).  \tag{42}
$$



In particular, (5) alone neither proves that this quotient has the
finite-grid dimension $q-1$, nor evaluates its Smith invariants, nor
bounds the primitive quadratic survivor.  Any use of the smaller Padé
height in the transcendence ledger must first supply that missing
quotient-saturation theorem.

## 8. Deterministic replay and logical boundary

The companion files are

* scripts/centered_cosh_pade_ideal_recurrence_certificate.py;
* results/centered_cosh_pade_ideal_recurrence_certificate.json;
* results/centered_cosh_pade_ideal_recurrence_hashes.sha256.

The replay checks exact Padé zero blocks, all parity parameters, the
selected Toeplitz/Schur-controllability minors, the two ideal inclusions,
the edge exception, and the annihilator recurrences on a finite exact
grid.  These finite checks are diagnostics.  The all-$q$ proof is
(16)--(41).

Nothing here proves that $e+\pi$ is algebraic or transcendental.
