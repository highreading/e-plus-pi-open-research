> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Two Bessel centers: evaluation lattices and the cross-determinant

Checked: 2026-08-27 UTC.

## 1. Verdict

Let $m=n+h$, where $n\geq0$ and $h\geq1$.  Suppose local
ordinary-root arguments produce a modulus $P$ at $n$ and a modulus
$R$ at $m$.  For example, $P=p^a$ with
$a=v_p(n-\rho_p)$, and similarly at $m$.

This note gives the exact two-center coefficient lattice and audits the
natural nonlinear determinant supplied by the Bessel recurrence.

1. For every degree bound $d\geq1$, the lattice

   

$$
\Lambda_d(n,m;P,R)=
   \{B\in\mathbb Z[x]:\deg B\leq d,\
   P\mid B(n),\ R\mid B(m)\}
   \tag{1}
$$



   has index

   

$$
\boxed{
   [\mathbb Z^{d+1}:\Lambda_d(n,m;P,R)]
   =\frac{PR}{\delta},\qquad
   \delta=\gcd(P,R,h).}
   \tag{2}
$$



   Hence Chinese-remainder gain can lose only the compatibility already
   forced by the center separation.
2. In degree one, any two linearly independent residual polynomials
   $B,C\in\Lambda_1(n,m;P,R)$ satisfy

   

$$
\boxed{
   \frac{PR}{\delta}\mid
   \det
   \begin{pmatrix}
   [x^0]B&[x^0]C\\
   [x^1]B&[x^1]C
   \end{pmatrix}.}
   \tag{3}
$$



   Therefore

   

$$
\log P+\log R
   \leq\log H_1(B)+\log H_1(C)+\log h.
   \tag{4}
$$



   Two independent small residuals would be a true cross-center route.
   The lattice itself does not construct them below this determinant
   scale.
3. One residual can be much shorter than $PR$.  If both its evaluated
   values are nonzero, however, it gives only

   

$$
\boxed{
   \frac{\log P+\log R}{2}
   \leq
   \log H_1(B)+\deg(B)\log(m+1).}
   \tag{5}
$$



   This is ordinary two-evaluation dimensional compression, not a
   saving for the summed depth.
4. Let $p_k,q_k$ be the two primitive exponential Padé solutions and
   $s_k=(p_k-q_k)/2$.  There is an exact positive transfer polynomial
   $C_h(n)$ such that

   

$$
\boxed{
   q_ns_m-s_nq_m=(-1)^nC_h(n),}
   \tag{6}
$$



   and

   

$$
\boxed{
   \gcd(q_n,q_m)=\gcd(q_n,C_h(n)),\qquad
   1\leq C_h(n)\leq[4(n+h)]^{h-1}.}
   \tag{7}
$$



   Thus the natural primitive nonlinear cross-determinant is indeed
   far smaller than $q_nq_m$, but it sees only common prime-power
   depth.  It does not carry the product of two local moduli.

The exact survivor is correspondingly sharp: construct two
coefficient-independent residuals which satisfy both root conditions,
have nonzero coefficient determinant, and whose product of primitive
$\ell^1$-heights is sub-main.  Neither the evaluation lattice nor the
Bessel cross-determinant supplies such a pair.

No denominator-height, irrationality, or transcendence result is
proved.

## 2. The integral two-center evaluation image

For a coefficient vector $\boldsymbol b=(b_0,\ldots,b_d)$, put



$$
E_{n,m}(\boldsymbol b)=(B(n),B(m)).
\tag{8}
$$



Every integral polynomial satisfies



$$
B(m)-B(n)\equiv0\pmod h.
\tag{9}
$$



Conversely, if integers $u,v$ satisfy $v-u\equiv0\pmod h$, the
linear polynomial



$$
B(x)=u+\frac{v-u}{h}(x-n)
\tag{10}
$$



has $B(n)=u$ and $B(m)=v$.  Therefore, for every $d\geq1$,



$$
\boxed{
 E_{n,m}(\mathbb Z^{d+1})
 =L_h:=\{(u,v)\in\mathbb Z^2:u\equiv v\pmod h\}.}
\tag{11}
$$



The lattice $L_h$ has index $h$ in $\mathbb Z^2$.

Now impose $u\in P\mathbb Z$ and $v\in R\mathbb Z$.  Writing
$u=Pk,v=R\ell$, the compatibility condition is



$$
Pk-R\ell\equiv0\pmod h.
\tag{12}
$$



The image of the map



$$
(k,\ell)\longmapsto Pk-R\ell\pmod h
\tag{13}
$$



has order $h/\delta$, where
$\delta=\gcd(P,R,h)$.  Hence



$$
[P\mathbb Z\times R\mathbb Z:
 L_h\cap(P\mathbb Z\times R\mathbb Z)]
 =\frac h\delta.
\tag{14}
$$



Combining the indices in $\mathbb Z^2$ gives



$$
\begin{aligned}
 [L_h:L_h\cap(P\mathbb Z\times R\mathbb Z)]
 &=\frac{
 [\mathbb Z^2:P\mathbb Z\times R\mathbb Z]\,
 [P\mathbb Z\times R\mathbb Z:
  L_h\cap(P\mathbb Z\times R\mathbb Z)]
 }{[\mathbb Z^2:L_h]}\\
 &=\frac{PR}{\delta}.
\end{aligned}
\tag{15}
$$



The kernel of $E_{n,m}$ is contained in (1), so pulling (15) back
proves (2).

An explicit basis can also be written.  Put



$$
A=\frac P\delta,\qquad H=\frac h\delta,\qquad
 R'=\frac R\delta,\qquad g_0=\gcd(A,H),
\tag{16}
$$



and choose $u_0,v_0\in\mathbb Z$ with
$Au_0+Hv_0=g_0$.  The solution lattice in the variables
$(k,b_1)$, where $b_0=Pk-nb_1$, has the two basis columns



$$
\binom{H/g_0}{-A/g_0},
 \qquad
 R'\binom{u_0}{v_0},
\tag{17}
$$



Both columns solve the reduced congruence
$Ak+Hb_1\equiv0\pmod {R'}$, and their determinant has absolute value
$R'$.  Since $\gcd(A,H,R')=1$, the kernel of that congruence has
index $R'$, so the two columns are a basis.  The transformation
$(k,b_1)\mapsto(b_0,b_1)$ has determinant $P$, again giving
$PR/\delta$.

## 3. Rank-two determinant and primitive content

For $d=1$, identify a polynomial $b_0+b_1x$ with its coefficient
column.  Two columns in the index-$PR/\delta$ lattice (1) span a
sublattice of $\mathbb Z^2$.  If they are independent, the index of
their span is a multiple of the index of (1).  This proves (3).

Hadamard's elementary $\ell^1$ bound gives



$$
0<
 \left|\det(\operatorname{coeff}B,\operatorname{coeff}C)\right|
 \leq H_1(B)H_1(C).
\tag{18}
$$



Since $\delta\leq h$, equations (3) and (18) prove (4).

If the original columns have contents $c_B,c_C$, write
$B=c_BB_0,C=c_CC_0$ with primitive $B_0,C_0$.  Then



$$
\frac{PR/\delta}
 {\gcd(PR/\delta,c_Bc_C)}
 \mid
 \det(\operatorname{coeff}B_0,\operatorname{coeff}C_0).
\tag{19}
$$



The determinant order removed by primitive normalization is at most
$\log|c_Bc_C|$, exactly as in the one-center content accounting.

For a single polynomial with $B(n)B(m)\ne0$, one merely has



$$
PR\leq|B(n)B(m)|
 \leq
 \bigl(H_1(B)(m+1)^{\deg B}\bigr)^2,
\tag{20}
$$



which proves (5).

This factor two is attained at the level of scale.  For example, when
$h=1$ and $\gcd(P,R)=1$,



$$
B(x)=P+(R-P)(x-n)
\tag{21}
$$



is primitive and has $B(n)=P,B(n+1)=R$.  Its coefficient height is
linear in $P+R$, potentially far below $PR$.  That is a genuine
one-vector interpolation compression, but (20) shows why it cannot by
itself bound the sum of the two logarithmic moduli at the same
complexity.

## 4. The exact Bessel cross-center transfer

Retain



$$
\begin{aligned}
 &q_0=q_1=1,\qquad
 q_k=(4k-2)q_{k-1}+q_{k-2},\\
 &p_0=1,\quad p_1=3,\qquad
 p_k=(4k-2)p_{k-1}+p_{k-2},\\
 &s_k=(p_k-q_k)/2.
\end{aligned}
\tag{22}
$$



For fixed $n$, define $A_j(n),C_j(n)\in\mathbb Z[n]$ by



$$
\begin{aligned}
 &(A_0,C_0)=(1,0),\qquad(A_1,C_1)=(0,1),\\
 &(A_{j+2},C_{j+2})
 =(4n+4j+6)(A_{j+1},C_{j+1})+(A_j,C_j).
\end{aligned}
\tag{23}
$$



For either solution $X=p,q,s$, induction gives



$$
X_{n+j}=A_j(n)X_n+C_j(n)X_{n+1}.
\tag{24}
$$



The primitive adjacent Wronskian is



$$
q_ns_{n+1}-s_nq_{n+1}=(-1)^n.
\tag{25}
$$



Substitution of (24) into the separated determinant proves (6).

Since consecutive $q$'s are coprime, (24) also gives



$$
\begin{aligned}
 \gcd(q_n,q_{n+h})
 &=\gcd(q_n,C_h(n)q_{n+1})\\
 &=\gcd(q_n,C_h(n)),
\end{aligned}
\tag{26}
$$



which is the first part of (7).

For $j\geq1$, all $C_j(n)$ are positive and increasing.  If
$1\leq j\leq h-2$, then



$$
C_{j+2}(n)
 \leq(4n+4j+7)C_{j+1}(n)
 <4(n+h)C_{j+1}(n).
\tag{27}
$$



For $h\geq2$, the base value $C_2=4n+6$ is smaller than
$4(n+h)$.  Starting from $C_1=1$ and this base value proves the
second part of (7).

The original Padé determinant is the same identity before primitive
halving:



$$
p_{n+h}q_n-p_nq_{n+h}
 =2(-1)^nC_h(n).
\tag{28}
$$



Equation (6) is therefore the primitive cross-center determinant.

## 5. What the small determinant measures

Let an odd prime $\ell$ divide both $q_n$ and $q_m$, and put



$$
a=v_\ell(q_n),\qquad b=v_\ell(q_m).
\tag{29}
$$



Since $\gcd(q_k,s_k)=1$, both $s_n$ and $s_m$ are
$\ell$-adic units.  Equation (6) gives



$$
v_\ell(C_h(n))\geq\min\{a,b\}.
\tag{30}
$$



If $a\ne b$, the two terms in (6) have distinct valuations, so
equality holds in (30).  When $a=b$, additional cancellation can
increase $v_\ell(C_h(n))$, but no product-depth law follows.

For arbitrary divisors $P\mid q_n$ and $R\mid q_m$, equation (7)
implies



$$
\gcd(P,R)\leq C_h(n),\qquad
 \log\gcd(P,R)
 \leq(h-1)\log(4(n+h)).
\tag{31}
$$



Thus the strikingly small determinant (6) controls only the overlap of
the two denominator supports.  A prime occurring at just one center
need not divide it at all.  It therefore cannot replace the
rank-two residual determinant required in (3).

There is one useful root-geometric special case.  If $n$ and $m$
approximate the same $\ell$-adic root $\rho$, then



$$
\min\{v_\ell(n-\rho),v_\ell(m-\rho)\}\leq v_\ell(h).
\tag{32}
$$



For $P=\ell^a,R=\ell^b$ from that same branch, this means
$\delta=\gcd(P,R)$, and the index (2) is only
$\operatorname{lcm}(P,R)$.  These are nested conditions, not two
independent congruences.  Their duplicated depth is bounded by the
center separation and by (31).

## 6. Exact survivor

The two-center audit separates three phenomena.

- A single interpolating polynomial may have primitive height far below
  $PR$, but pays the factor two in (5).
- Two independent residual polynomials recover
  $\log P+\log R$ through (3), losing at most $\log h$, but their
  determinant cannot be below $PR/\delta$ unless content pays the
  difference.
- The natural Bessel state determinant is exceptionally small, but
  equations (30)--(31) show that it captures only common support.

A successful cross-center construction must combine the second
phenomenon with a genuinely new source of two coefficient-independent,
simultaneously small residuals.  The recurrence transfer and the
ordinary evaluation lattice do not provide them.

Nothing in this note proves a new individual digit-depth bound or
settles $e+\pi$.

## 7. Exact certificate

The companion script

    scripts/bessel_two_center_evaluation_lattice_certificate.py

checks the two-center image and index formula, explicit bases,
rank-two determinant divisibility, primitive content accounting,
single-vector interpolation, the $p,q,s$ transfers, cross-determinant,
gcd identity, valuation cases, and the height bound for $C_h(n)$ over
finite exact boxes.  The all-parameter statements are proved
symbolically above.

Run

    python -m py_compile scripts/bessel_two_center_evaluation_lattice_certificate.py
    python scripts/bessel_two_center_evaluation_lattice_certificate.py

For byte-identical replay, use

    python scripts/bessel_two_center_evaluation_lattice_certificate.py \
      --output /tmp/bessel_two_center_evaluation_lattice_certificate.json
    cmp results/bessel_two_center_evaluation_lattice_certificate.json \
      /tmp/bessel_two_center_evaluation_lattice_certificate.json
