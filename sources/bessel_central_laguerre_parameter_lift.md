> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The central Bessel obstruction as a Laguerre parameter lift

Checked: 2026-08-27 UTC.

## 1. Scope and verdict

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\ge2).
\tag{1}
$$



For an odd prime $p$, put $m=(p-1)/2$.  This note gives an exact
Laguerre-polynomial normal form for the exceptional central question



$$
p^2\mid q_m.
\tag{2}
$$



Define



$$
A_m=m!L_m(-1)
     =\sum_{j=0}^m j!\binom mj^2
\tag{3}
$$



and



$$
C_m=m!\left.
       \frac{\partial}{\partial\alpha}L_m^{(\alpha)}(-1)
       \right|_{\alpha=0}.
\tag{4}
$$



The main congruence is



$$
\boxed{q_m\equiv(-1)^m(A_m-pC_m)\pmod {p^2}.}
\tag{5}
$$



Moreover, $C_m$ has the two exact forms



$$
C_m=\sum_{r=1}^m\frac{(m)_r}{r}A_{m-r}
 =\sum_{j=0}^m j!\binom mj^2
       (H_m-H_{m-j}),
\tag{6}
$$



where $(m)_r=m!/(m-r)!$ is falling and $H_0=0$.  The first sum in
(6) shows directly that $C_m$ is an integer: among $r$ consecutive
integers, one is divisible by $r$.

Consequently,



$$
p\mid q_m\Longleftrightarrow p\mid A_m,
\tag{7}
$$



and, conditional on this divisibility,



$$
\boxed{
 p^2\mid q_m
 \Longleftrightarrow
 \frac{A_m}{p}\equiv C_m\pmod p.}
\tag{8}
$$



Thus the extra lift is a first parameter derivative of a classical Laguerre
polynomial, together with the unknown divisibility quotient $A_m/p$.  Formula
(8) is a rigorous reduction, not an exclusion theorem.  In particular, this
note does **not** prove that (2) is impossible for every prime.

There is also an exact Padé Wronskian which proves that, whenever 

$$
p\mid
q_m
$$

, the polynomial whose value is $q_m$ has a simple root at $x=1$
modulo $p$.  Section 4 explains why that polynomial-root simplicity does
not imply $p^2\nmid q_m$.  Confusing these two lifting problems would give
an invalid proof.

## 2. Exact Bessel--Laguerre identity

For $n\ge0$, define the integer polynomial



$$
Q_n(x)=\sum_{k=0}^n(-1)^k
       \frac{(2n-k)!}{k!(n-k)!}x^k.
\tag{9}
$$



A coefficientwise calculation gives



$$
Q_n(x)=2(2n-1)Q_{n-1}(x)+x^2Q_{n-2}(x),
\tag{10}
$$



with $Q_0(x)=1$ and $Q_1(x)=2-x$.  Therefore $Q_n(1)$ has the
initial values and recurrence (1), and hence



$$
q_n=Q_n(1).
\tag{11}
$$



Use the normalization



$$
L_n^{(\alpha)}(x)
 =\sum_{j=0}^n\binom{n+\alpha}{n-j}\frac{(-x)^j}{j!}.
\tag{12}
$$



Since



$$
\binom{-n-1}{n-j}=(-1)^{n-j}\binom{2n-j}{n-j},
$$



substitution in (12) proves the exact polynomial identity



$$
Q_n(x)=(-1)^n n!L_n^{(-2n-1)}(-x).
\tag{13}
$$



At the central index $p=2m+1$, this becomes



$$
\boxed{q_m=(-1)^m m!L_m^{(-p)}(-1).}
\tag{14}
$$



This is an equality in the integers, not merely a congruence.

## 3. Connection formula and the parameter derivative

The Laguerre generating function is



$$
\sum_{n\ge0}L_n^{(\alpha)}(x)t^n
 =(1-t)^{-\alpha-1}
   \exp\!\left(-\frac{xt}{1-t}\right).
\tag{15}
$$



Factoring the right side with parameters $\alpha$ and $\beta$, then
extracting the coefficient of $t^n$, gives the exact connection formula



$$
L_n^{(\alpha)}(x)
 =\sum_{r=0}^n
   \binom{\alpha-\beta+r-1}{r}L_{n-r}^{(\beta)}(x).
\tag{16}
$$



Set $n=m$, $\alpha=-p$, $\beta=0$, and $x=-1$.  Since



$$
\binom{-p+r-1}{r}=(-1)^r\binom pr,
$$



we obtain the exact equality



$$
L_m^{(-p)}(-1)
 =L_m(-1)+\sum_{r=1}^m(-1)^r\binom prL_{m-r}(-1).
\tag{17}
$$



For $1\le r\le m<p$, in the localization $\mathbb Z_{(p)}$,



$$
(-1)^r\binom pr
 =-\frac pr\prod_{s=1}^{r-1}\left(1-\frac ps\right)
 \equiv-\frac pr\pmod {p^2}.
\tag{18}
$$



Multiplying (17) by $(-1)^m m!$ and using (14) proves



$$
q_m\equiv(-1)^m\left(
 A_m-p\sum_{r=1}^m\frac{(m)_r}{r}A_{m-r}
 \right)\pmod {p^2}.
\tag{19}
$$



On the other hand, differentiating (16) with $\beta=0$ at $\alpha=0$
uses



$$
\left.\frac{d}{d\alpha}
 \binom{\alpha+r-1}{r}\right|_{\alpha=0}=\frac1r
 \quad(r\ge1)
$$



and gives



$$
\left.\frac{\partial}{\partial\alpha}
 L_m^{(\alpha)}(-1)\right|_{\alpha=0}
 =\sum_{r=1}^m\frac{L_{m-r}(-1)}r.
\tag{20}
$$



Equations (19)--(20) prove (5) and the first equality in (6).

For the second equality, differentiate the defining sum (12).  At
$\alpha=0$,



$$
\left.\frac{d}{d\alpha}\binom{m+\alpha}{m-k}
 \right|_{\alpha=0}
 =\binom m{m-k}(H_m-H_k).
\tag{21}
$$



After multiplying by $m!$ and reindexing $j=m-k$, (21) is exactly the
harmonic sum in (6).  The same reindexing without differentiation proves
(3).  Because $m!$ is a unit modulo $p$, (5) immediately proves
(7)--(8).

The previously obtained truncated-hypergeometric expression is consistent
with (5).  Indeed, expansion of $(1/2)_j=(-m+p/2)_j$ gives



$$
\frac{(1/2)_j^2}{j!}
 \equiv j!\binom mj^2
 \left(1-p(H_m-H_{m-j})\right)\pmod {p^2},
\tag{22}
$$



and summing (22) recovers $A_m-pC_m$.

## 4. The Padé Wronskian and the crucial distinction

Put



$$
P_m(x)=Q_m(-x).
\tag{23}
$$



The elementary coefficient identity



$$
\sum_{k=0}^{\min(m,s)}(-1)^k
 \frac{(2m-k)!}{k!(m-k)!(s-k)!}
 =
 \begin{cases}
 \dfrac{(2m-s)!}{s!(m-s)!},&0\le s\le m,\\[6pt]
 0,&m<s\le2m
 \end{cases}
\tag{24}
$$



is Chu--Vandermonde after factorials are cleared.  It says precisely that



$$
P_m(x)-e^xQ_m(x)=O(x^{2m+1})
\tag{25}
$$



as a formal power series at zero.

Differentiate (25), replace $e^x$ by $P_m/Q_m+O(x^{2m+1})$, and
multiply by $Q_m$.  The polynomial



$$
W_m(x)=P_m'(x)Q_m(x)-P_m(x)Q_m'(x)-P_m(x)Q_m(x)
$$



is divisible by $x^{2m}$.  It has degree at most $2m$, and its leading
coefficient comes only from $-P_mQ_m$.  Since the leading coefficients of
$P_m,Q_m$ are $1,(-1)^m$, respectively,



$$
\boxed{W_m(x)=(-1)^{m+1}x^{2m}.}
\tag{26}
$$



Suppose now that $p=2m+1$ and $p\mid q_m=Q_m(1)$.  Reducing (26) at
$x=1$ modulo $p$ gives



$$
-P_m(1)Q_m'(1)\equiv(-1)^{m+1}\pmod p.
\tag{27}
$$



Therefore



$$
P_m(1)\not\equiv0\pmod p,
 \qquad Q_m'(1)\not\equiv0\pmod p.
\tag{28}
$$



In particular, $x=1$ is a simple root of the polynomial $Q_m(x)$ over
$\mathbb F_p$.  If $q_m=pa\pmod {p^2}$, its unique Hensel lift is



$$
x\equiv1-pa\,Q_m'(1)^{-1}\pmod {p^2}.
\tag{29}
$$



But (29) does not say that $a\ne0$.  If $p^2\mid q_m$, then $a=0$
and the unique lifted polynomial root is simply still $x=1$.  Hensel's
lemma permits this.  The central branching problem varies the Laguerre
**parameter** from $0$ to $-p$, as quantified by (5); the Wronskian
controls variation in the polynomial **argument** $x$.  These are distinct
directions.  Thus (28) cannot be used to turn (8) into a nonvanishing theorem.

## 5. First central root

For $p=79$, $m=39$, exact modular arithmetic gives



$$
A_{39}/79\equiv45\pmod {79},\qquad
 C_{39}\equiv57\pmod {79}.
\tag{30}
$$



Hence (5) gives



$$
q_{39}/79\equiv(-1)^{39}(45-57)=12\pmod {79},
$$



or



$$
q_{39}\equiv948=12\cdot79\pmod {79^2}.
\tag{31}
$$



Thus the first central root dies at the square level.  This single example
does not prove that every central root does so.

## 6. Exact finite certificate

The companion program

`scripts/bessel_central_laguerre_parameter_lift_certificate.py`

checks the integer/rational forms (3), (6), (14), (17), and (26) in bounded
degrees.  It then uses the Laguerre-value recurrence



$$
A_n=2nA_{n-1}-(n-1)^2A_{n-2},\qquad A_0=1,\quad A_1=2,
\tag{32}
$$



which follows from the ordinary Laguerre recurrence at $x=-1$.

For the finite prime scan, the program groups the transition matrices for
(32) between consecutive indices $(p-1)/2$ and evaluates all prefixes with
an accumulating remainder tree.  At every product-tree level, a node product
is retained modulo the product of all later node moduli.  This is sufficient
because that node product is used only to advance the state into a right
sibling.  The level-zero segment products remain exact so that they can also
be applied at their own leaves.  Thus the scan uses exact integer modular
arithmetic; it is not a floating-point or probable-prime calculation.

The archived run in

`results/bessel_central_laguerre_parameter_lift_certificate.json`

scans every odd prime $p\le2{,}000{,}001$, a total of $148{,}932$
primes.  Its SHA-256 digest of the ordered records $p:A_{(p-1)/2}\bmod p$
is

```
072ddd4c8400ed7a2e356aeeac42a8541db75c0e4f8b4aa3474c68df9ce5ec61
```

The only central root in that finite range is $p=79$.  Every root found is
then checked independently with the original recurrence (1) modulo $p^2$,
as well as against (5) and the Wronskian specialization (27).  No central
all-branch root occurs in the stated range.  This is finite evidence only and
does not exclude a later prime satisfying (8).

## 7. Research consequence

The central all-branch alternative is now equivalent to the integer quotient
congruence (8).  Ordinary Laguerre root separability, the Padé Wronskian, and
the nonzero neighboring Padé numerator do not determine $A_m/p\pmod p$.
An all-prime exclusion would need new arithmetic information connecting that
quotient to the parameter derivative $C_m$, or an independent theorem that
prevents their equality.  No such theorem is proved here.
