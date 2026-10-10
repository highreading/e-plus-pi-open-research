> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The $c=1$ factorial-digit determinant: exact cofactors, primitive content, and adversarial obstruction

## 1. Scope and verdict

Let



$$
g_0=3,\qquad g_1=0,\qquad
 g_n=d_n=\lfloor n!\pi\rfloor-n\lfloor(n-1)!\pi\rfloor
 \quad(n\geq2),
\tag{1}
$$



so that



$$
G(z)=\sum_{n\geq0}g_n\frac{z^n}{n!},\qquad G(1)=\pi.
\tag{2}
$$



This note analyzes the first genuinely new full polynomial-$C$ ray,
$\deg C\leq1$, in the endpoint-matched system



$$
A+Be^z+CG=O(z^{a+b+2}),\qquad B(1)=C(1),
\tag{3}
$$



where $\deg A\leq a$ and $\deg B\leq b$.  The conclusions are:

1. the $(b+1)$ by $(b+1)$ high-jet determinant has an explicit
   primitive integer recurrence;
2. every cofactor sign is known and alternates strictly;
3. after removing the universal factor $\prod_{j<b}j!$, the direct
   factorial-digit coefficient vector has ordinary gcd exactly one in
   every degree;
4. the auxiliary positive numbers are shifted-gamma moments and possess
   an explicit Jacobi continued fraction;
5. the bare digit bounds $0\leq d_n\leq n-1$ force neither a sign nor
   nonvanishing in fixed-$b$, $b=o(a)$, or diagonal regimes;
6. for the actual certified digits of $\pi$, an exact finite scan of all
   71,019 admissible pairs $a+b\leq530$ finds only three determinant
   zeros, all at the initial digit gap.

Items 1--5 are all-degree theorems.  Item 6 is a finite diagnostic and is
not extrapolated beyond the certified range.

## 2. The high block

Put



$$
u_j(k)=k^{\underline j}(k-j-1)
       =k^{\underline{j+1}}-k^{\underline j}
 \qquad(0\leq j<b)
\tag{4}
$$



and



$$
v(k)=kg_{k-1}-g_k.
\tag{5}
$$



The high equations obtained after normalizing
$B(1)=C(1)=1$ have the square matrix



$$
\mathcal H_{a,b,1}
 =\left(u_0,\ldots,u_{b-1},v\right)
 \big|_{k=a+1,\ldots,a+b+1}.
\tag{6}
$$



Thus the first $b$ columns depend only on $e^z$, while the final column
contains the factorial digits.  Formula (6) remains meaningful for
$b=0$, when it is the one by one matrix $(v(a+1))$.

## 3. The positive moment sequence

Define



$$
D_{a,m}=\frac{\Delta^m(a!)}{a!}
 =\sum_{j=0}^m(-1)^{m-j}\binom mj(a+1)^{\overline j}.
\tag{7}
$$



Here $(a+1)^{\overline j}=(a+1)\cdots(a+j)$.  Its exponential
generating function, recurrence, and integral representation are



$$
\sum_{m\geq0}D_{a,m}\frac{z^m}{m!}
 =e^{-z}(1-z)^{-a-1},
\tag{8}
$$





$$
D_{a,0}=1,\qquad D_{a,1}=a,\qquad
 D_{a,m}=(a+m-1)D_{a,m-1}+(m-1)D_{a,m-2},
\tag{9}
$$



and



$$
D_{a,m}=\frac1{a!}\int_0^\infty
 t^a(t-1)^m e^{-t}\,dt.
\tag{10}
$$



In particular, (9) proves $D_{a,m}>0$ for $a\geq1$.

There is also a precise continued-fraction interpretation.  The values
$D_{a,m}$ are the moments of $x=t-1$ for the probability density
$t^ae^{-t}/a!$.  The shifted monic Laguerre recurrence is



$$
xP_n(x)=P_{n+1}(x)+(a+2n)P_n(x)+n(a+n)P_{n-1}(x).
\tag{11}
$$



Therefore the ordinary moment series has the formal Jacobi fraction



$$
\sum_{m\geq0}D_{a,m}z^m
 =
 \cfrac{1}{
  1-az-\cfrac{(a+1)z^2}{
  1-(a+2)z-\cfrac{2(a+2)z^2}{
  1-(a+4)z-\cfrac{3(a+3)z^2}{\ddots}}}}}.
\tag{12}
$$



This continued fraction explains the positive moment structure behind the
cofactors.  It does not impose a sign on the final digit linear form.

## 4. Interpolation and the normalized determinant

On polynomials in the falling-factorial basis, define the Poisson
functional



$$
\mathscr L\left(\sum_jc_jk^{\underline j}\right)=\sum_jc_j.
\tag{13}
$$



Equivalently,



$$
\mathscr L(p)=e^{-1}\sum_{n\geq0}\frac{p(n)}{n!}.
\tag{14}
$$



The columns $u_0,\ldots,u_{b-1}$ form a basis for
$\ker\mathscr L$ among polynomials of degree at most $b$.

Let $p_{a,b}$ be the polynomial of degree at most $b$ interpolating
$v$ at $a+1,\ldots,a+b+1$.  Newton interpolation gives



$$
p_{a,b}(k)=\sum_{m=0}^b
 \frac{\Delta^mv(a+1)}{m!}(k-a-1)^{\underline m}.
\tag{15}
$$



The generating-function identity



$$
\mathscr L\bigl((k-a-1)^{\underline m}\bigr)
 =(-1)^mD_{a,m}
\tag{16}
$$



follows by applying $\mathscr L$ to
$(1+z)^{k-a-1}$ and comparing with (8).  Hence



$$
\mathscr L(p_{a,b})
 =\sum_{m=0}^b(-1)^m
   \frac{D_{a,m}}{m!}\Delta^mv(a+1).
\tag{17}
$$



Set



$$
F_{a,b}=b!\,\mathscr L(p_{a,b}),\qquad
 \kappa_b=\prod_{j=0}^{b-1}j!,
\tag{18}
$$



with an empty product equal to one.  Since
$1,u_0,\ldots,u_{b-1}$ is a monic graded basis and the nodes are
consecutive, the corresponding Vandermonde determinant is
$\kappa_b b!$.  Moving the constant column to the end introduces
$(-1)^b$.  Therefore



$$
\boxed{\det\mathcal H_{a,b,1}=(-1)^b\kappa_bF_{a,b}.}
\tag{19}
$$



Adding the last Newton term in (15) gives a particularly simple integer
recurrence:



$$
\boxed{
 F_{a,0}=v(a+1),\qquad
 F_{a,b}=bF_{a,b-1}
 +(-1)^bD_{a,b}\Delta^bv(a+1).}
\tag{20}
$$



Thus $F_{a,b}$, rather than the determinant containing the large
factorial product $\kappa_b$, is the natural normalized determinant.

## 5. Exact alternating cofactors

For $0\leq r\leq b$, define



$$
A_{a,b,r}
 =\frac{b!}{r!}\sum_{h=0}^{b-r}\frac{D_{a,r+h}}{h!}.
\tag{21}
$$



Expansion of (17) in the values $v(a+1+r)$ gives



$$
\boxed{
 F_{a,b}=\sum_{r=0}^b(-1)^r
 A_{a,b,r}v(a+1+r).}
\tag{22}
$$



The apparent denominators in (21) cancel.  Indeed,



$$
A_{a,0,0}=1,\qquad A_{a,b,b}=D_{a,b},
\tag{23}
$$



and, for $r<b$,



$$
A_{a,b,r}
 =bA_{a,b-1,r}+\binom brD_{a,b}.
\tag{24}
$$



Equations (9), (23), and (24) prove that every $A_{a,b,r}$ is a
strictly positive integer.  In the full determinant, the cofactor of
$v(a+1+r)$ is



$$
(-1)^{b+r}\kappa_bA_{a,b,r}.
\tag{25}
$$



This establishes the exact alternating cofactor signs in every degree.

## 6. Direct factorial-digit form and content one

For $a\geq2$, equation (5) reads



$$
v(a+1+r)=(a+r+1)d_{a+r}-d_{a+r+1}.
\tag{26}
$$



The same formula remains valid at $a=1$ if $d_1$ is interpreted as
the fixed jet $g_1=0$.  Put



$$
B_{a,b,0}=(a+1)A_{a,b,0},
\tag{27}
$$





$$
B_{a,b,s}=A_{a,b,s-1}+(a+s+1)A_{a,b,s}
 \quad(1\leq s\leq b),
\tag{28}
$$



and



$$
B_{a,b,b+1}=A_{a,b,b}.
\tag{29}
$$



Then every $B_{a,b,s}$ is positive and



$$
\boxed{
 F_{a,b}=\sum_{s=0}^{b+1}(-1)^s
 B_{a,b,s}d_{a+s}.}
\tag{30}
$$



Consequently the digit coefficient in the full determinant has sign
$(-1)^{b+s}$.

There is no further universal integer content.  First, (8) and (21) give



$$
A_{a,b,0}=b!\sum_{m=0}^b\frac{D_{a,m}}{m!}
           =D_{a+1,b}.
\tag{31}
$$



The integral (10), or the generating function (8), also gives



$$
(a+1)D_{a+1,b}=D_{a,b+1}+D_{a,b}.
\tag{32}
$$



Thus the first and last magnitudes in (30) are



$$
B_{a,b,0}=D_{a,b+1}+D_{a,b},\qquad
 B_{a,b,b+1}=D_{a,b}.
\tag{33}
$$



To see that these two integers are coprime, rewrite (7) as



$$
D_{a,m}=(-1)^m+
 \sum_{j=1}^m(-1)^{m-j}
 m^{\underline j}\binom{a+j}{j}.
\tag{34}
$$



Hence



$$
D_{a,m}\equiv(-1)^m\pmod m,
\tag{35}
$$



so $\gcd(D_{a,m},m)=1$.  Recurrence (9) now proves by induction that
consecutive values are coprime:



$$
\gcd(D_{a,m},D_{a,m+1})=1.
\tag{36}
$$



Combining (33) and (36) yields the all-degree primitive-content theorem



$$
\boxed{\gcd_{0\leq s\leq b+1}B_{a,b,s}=1.}
\tag{37}
$$



Thus $\kappa_b$ is the entire structural factorial factor visible in
(19); the normalized digit linear form (30) is primitive.

## 7. Sharp obstruction from digit bounds alone

The inequalities



$$
0\leq d_n\leq n-1
\tag{38}
$$



cannot force a sign.  For $a\geq2$, setting only $d_a=1$ makes
$F_{a,b}>0$, while setting only $d_{a+1}=1$ makes
$F_{a,b}<0$.  Both assignments satisfy (38).  Multiplication by the
fixed sign $(-1)^b$ in (19) does not change the conclusion for the full
determinant.

The bounds cannot force nonvanishing either:

* for $b=0$, the allowed block $d_a=d_{a+1}=0$ gives $F_{a,0}=0$;
* for every $b\geq1$, the allowed constant block
  $d_a=\cdots=d_{a+b+1}=1$ gives

  

$$
v(k)=k-1=u_0(k),
  \tag{39}
$$



  so the final column of (6) duplicates its first column and the
  determinant is zero.

These blocks can be placed at arbitrarily large indices.  A global
constant-one tail already defeats diagonal or $b=o(a)$ claims with
$b\geq1$; disjoint zero pairs defeat a fixed-$b=0$ claim.  Therefore
no argument using only (38) can prove eventual sign or nonvanishing in
any of the proposed asymptotic regimes.

There is a second, target-relevant obstruction.  The conditional
rationality pattern for $e+\pi$ is



$$
d_n=n-2
\tag{40}
$$



eventually.  It gives



$$
v(k)=k^2-4k+2=k^{\underline2}-3k^{\underline1}+2.
\tag{41}
$$



The right side has $\mathscr L(v)=1-3+2=0$.  Hence every
$b\geq2$ block entirely inside such a tail has $F_{a,b}=0$.
This is the determinant-level version of the polynomial syzygy that would
occur if $e+\pi$ were rational.

## 8. Exact canonical-$\pi$ diagnostic through total degree 530

The independent certificate encloses



$$
\pi=4\bigl(\arctan(1/2)+\arctan(1/3)\bigr)
\tag{42}
$$



by exact alternating rational bounds.  It certifies every floor through
$\lfloor531!\pi\rfloor$, including the new digit



$$
d_{531}=297.
\tag{43}
$$



The digit vector through $530$ has SHA-256



$$
\text{9823adbf8b8ee2e45695284428ae465af2247354bf889979e8ddceb6139326b4},
\tag{44}
$$



agreeing with the previous independent fixed-$b$ certificate.

The scan covers exactly the familiar admissible region



$$
a+b\leq530,\qquad a\geq\max(1,b-1),
\tag{45}
$$



which contains 71,019 pairs.  Every record was evaluated by the recurrence
(20), the cofactor form (22), and the direct digit form (30).  All three
integer values agree.  Additional checks include 107 direct
fraction-free determinants and 60 exact shifted-Laguerre moment checks.

The finite canonical-digit findings are:

* the only zeros are

  

$$
(a,b)=(1,0),\ (1,1),\ (2,0);
  \tag{46}
$$



* among the normalized values $F_{a,b}$, there are 35,252 negative,
  35,764 positive, and three zero records;
* the full determinant signs are 35,226 negative, 35,790 positive, and
  three zero records;
* the minimum nonzero $|F_{a,b}|$ is $1$, attained at
  $(5,0)$ and $(9,0)$;
* the one by one Schur residual has magnitude
  $|F_{a,b}|/D_{a,b}$; its finite minimum is also $1$, first attained
  at $(5,0)$;
* if the digit-box normalization is

  

$$
\mathcal R_{a,b}
  =\frac{|F_{a,b}|}{
    \sum_{s=0}^{b+1}B_{a,b,s}(a+s-1)},
  \tag{47}
$$



  with the $s=0,a=1$ upper bound interpreted as zero, then the smallest
  nonzero value in the scan occurs at $(318,212)$:

  

$$
\mathcal R_{318,212}
  =5.6157370861437676162\ldots\times10^{-7}.
  \tag{48}
$$



The normalized determinant at $(264,265)$ has 771 decimal digits, the
largest length in the finite box.  All large integers and exact rational
minimizers are archived in the result JSON.  These observations do not
constitute an all-degree sign or zero theorem.

## 9. Reproducibility

The theorem certificate and finite diagnostic are:

* <scripts/independent_factorial_digit_c1_determinant_certificate.py>;
* <results/independent_factorial_digit_c1_determinant_a_plus_b_530.json>.

The result contains a SHA-256 stream commitment to every exact tuple
$(a,b,F_{a,b},D_{a,b},\text{digit-box capacity})$, per-total and
fixed-$b$ summaries, all exceptional records, exact minimizer fractions,
selected full cofactor vectors, and the independent digit certificate.
The finite claims are reproducible byte-for-byte by rerunning the script.
