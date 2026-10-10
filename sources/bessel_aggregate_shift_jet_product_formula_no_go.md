> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Aggregate product formulas for Bessel shifts and first jets: an exact no-go

Checked: 2026-08-27 UTC.

## 1. Verdict

Let



$$
q_0=q_1=1,
 \qquad q_n=(4n-2)q_{n-1}+q_{n-2},
\tag{1}
$$



and let $f_p$ be the canonical interpolation of



$$
f_p(n)=(-1)^nq_n.
\tag{2}
$$



Fix an integer center $n$.  Consider any polynomial expression, with
integral polynomial coefficients, in finitely many parameter shifts



$$
f_p(x+j),\qquad f_p'(x+j)\qquad(j\in J\subset\mathbb Z).
\tag{3}
$$



This includes linear forms, products, Wronskians, and determinants whose
entries are finite linear shift--jet forms.  There is an exact dichotomy.

1. Every expression in (3) reduces over $\mathbb Z[x]$ to a polynomial
   in the four boundary symbols

   

$$
F=f_p(x),\quad G=f_p(x+1),\quad X=f_p'(x),\quad Y=f_p'(x+1).
   \tag{4}
$$



2. If its vanishing at a zero of $F$ is forced **formally**, using only
   the recurrence, its derivative, and $F=0$, then the reduced
   polynomial is divisible by $F$.  If the formal order is $s$, it is
   divisible by $F^s$.
3. At the integer center, the two jet symbols are

   

$$
\begin{aligned}
   X&=(-1)^{n+1}(p_n\mathcal K_p-b_n),\\
   Y&=(-1)^{n+2}(p_{n+1}\mathcal K_p-b_{n+1}),
   \end{aligned}
   \tag{5}
$$



   where $p_n,b_n\in\mathbb Z$ and
   $\mathcal K_p=\sum_{m\geq0}m!\in\mathbb Z_p$.  Therefore the
   integer-center value of a reduced expression is a polynomial

   

$$
\Psi_n(K)\in\mathbb Z[K]
   \tag{6}
$$



   evaluated at $K=\mathcal K_p$.
4. Suppose the formal root order is $s$, and the dependence on the
   indeterminate $K$ cancels identically, so that a single rational
   integer $I_n$, independent of $p$, remains.  Then

   

$$
\boxed{q_n^s\mid I_n.}
   \tag{7}
$$



   Thus either $I_n=0$, or

   

$$
\boxed{\log|I_n|\geq s\log q_n
                    =s n\log n+O(sn).}
   \tag{8}
$$



Consequently a rational product formula aggregated over varying primes
cannot gain from this formal shift--jet algebra.  For every finite set
$\mathcal P$ of primes put



$$
D_{n,\mathcal P}
 =\prod_{p\in\mathcal P}p^{v_p(q_n)}.
\tag{9}
$$



If a nonzero integer auxiliary of formal order $s$ is obtained as
above, then



$$
D_{n,\mathcal P}^s\mid I_n,
 \qquad
 s\log D_{n,\mathcal P}\leq\log|I_n|.
\tag{10}
$$



But (7) shows that the auxiliary already contains the whole factor
$q_n^s$.  Dividing it out removes exactly the forced local orders.
The product formula therefore repackages the original estimate



$$
\log D_{n,\mathcal P}\leq\log q_n=n\log n+O(n),
\tag{11}
$$



and cannot prove the required little-oh bound.

If $\Psi_n(K)$ is nonconstant, its values
$\Psi_n(\mathcal K_p)$ for different $p$ are prime-dependent
$p$-adic numbers, not the local embeddings of one already controlled
rational or algebraic number.  The ordinary product formula is then not
available.  Making this branch arithmetic would require a genuinely new
global relation or height theorem for the Euler factorial values.

This is an all-shift, all-polynomial-degree theorem within the stated
formal algebra.  It is not a claim that every possible auxiliary must
fail.  In particular, it does not cover a special small-height polynomial
which is unusually small at the actual Bessel zero for a reason not
forced by the recurrence, a new integral transform, or a separately
controlled infinite tail.

## 2. Four-generator reduction

The interpolation satisfies



$$
f_p(x+1)+(4x+2)f_p(x)-f_p(x-1)=0.
\tag{12}
$$



Define $U_j,V_j\in\mathbb Z[x]$, for $j\in\mathbb Z$, by



$$
U_0=1,\quad V_0=0,
 \qquad U_1=0,\quad V_1=1,
\tag{13}
$$



and



$$
\begin{aligned}
 U_{j+1}&=-(4x+4j+2)U_j+U_{j-1},\\
 V_{j+1}&=-(4x+4j+2)V_j+V_{j-1}.
 \end{aligned}
\tag{14}
$$



The recurrence is read backwards for negative $j$.  Induction gives



$$
\boxed{f_p(x+j)=U_j(x)F+V_j(x)G.}
\tag{15}
$$



Differentiating the polynomial identity (15) gives



$$
\boxed{
 f_p'(x+j)
 =U_j'(x)F+V_j'(x)G+U_j(x)X+V_j(x)Y.}
\tag{16}
$$



Equations (15)--(16) prove the reduction in (4) for an arbitrary finite
set of shifts.  No division is used.  Therefore an expression with
coefficients in $\mathbb Z[x]$ reduces to a polynomial



$$
\overline E(x,F,G,X,Y)
 \in\mathbb Z[x,F,G,X,Y].
\tag{17}
$$



The reduction need not be injective; this is immaterial.  All recurrence
identities have already become zero in (17).

## 3. Formal root order is exactly an $F$-factor

The phrase *formally forced by the root equation* has a precise algebraic
meaning:



$$
\overline E(x,0,G,X,Y)=0
 \quad\text{in }\mathbb Z[x,G,X,Y].
\tag{18}
$$



Treating (17) as a polynomial in $F$, condition (18) says that its
constant coefficient is zero.  Hence



$$
\overline E=F\,\overline C,
 \qquad
 \overline C\in\mathbb Z[x,F,G,X,Y].
\tag{19}
$$



More generally, if the first $s$ coefficients in $F$ vanish and the
coefficient of $F^s$ does not, then



$$
\overline E=F^s\overline C,
 \qquad F\nmid\overline C.
\tag{20}
$$



This proves the formal factor statement for arbitrary products and
determinants, not only for linear forms.

A linear expression illustrates the rigidity.  After reduction it is



$$
A(x)F+B(x)G+C(x)X+D(x)Y.
\tag{21}
$$



Formal vanishing on $F=0$ forces $B=C=D=0$, so it is exactly a
multiple of $F$.  Introducing more shifted values or shifted first
jets cannot change this conclusion, because (15)--(16) have already
reduced all of them to (21).

## 4. Arithmetic specialization and coefficientwise divisibility

Define



$$
\begin{aligned}
 &p_0=1,\quad p_1=3,
 &&p_n=(4n-2)p_{n-1}+p_{n-2},\\
 &b_0=0,\quad b_1=4,
 &&b_{n+2}=(4n+6)b_{n+1}+b_n+4q_{n+1}.
 \end{aligned}
\tag{22}
$$



The exact all-integer jet identity proved in the companion note is (5).
At $x=n$, substitute in (17)



$$
\begin{aligned}
 F&=(-1)^nq_n,\\
 G&=(-1)^{n+1}q_{n+1},\\
 X&=(-1)^{n+1}(p_nK-b_n),\\
 Y&=(-1)^{n+2}(p_{n+1}K-b_{n+1}),
 \end{aligned}
\tag{23}
$$



where $K$ is now an indeterminate.  Because every quantity other than
$K$ is an integer, the result is the polynomial $\Psi_n(K)$ in (6).

If (20) holds, substitution gives the stronger coefficientwise statement



$$
\boxed{
 \Psi_n(K)=((-1)^nq_n)^s C_n(K),
 \qquad C_n(K)\in\mathbb Z[K].}
\tag{24}
$$



If all positive powers of $K$ cancel, then
$\Psi_n(K)=I_n\in\mathbb Z$, while (24) gives (7).  Notice that this
does not assume anything about the unknown arithmetic nature of
$\mathcal K_p$: cancellation is an identity in $\mathbb Z[K]$.

The same proof handles rational coefficients after multiplying by their
common denominator.  That clearing factor must then be included in the
archimedean height and in the product formula.

## 5. The sharp adjacent-jet boundary

For a linear combination of the two boundary jets, (23) gives



$$
\alpha X+\beta Y
 =(-1)^{n+1}
 \left((\alpha p_n-\beta p_{n+1})K
       -\alpha b_n+\beta b_{n+1}\right).
\tag{25}
$$



Consecutive $p_n$'s are coprime, because recurrence (22) preserves
their gcd and $\gcd(p_0,p_1)=1$.  Thus the $K$-coefficient vanishes
if and only if



$$
(\alpha,\beta)=t(p_{n+1},p_n)
 \qquad(t\in\mathbb Z).
\tag{26}
$$



The primitive cancellation already has coefficient height
$p_{n+1}$, with



$$
\log p_{n+1}=n\log n+O(n).
\tag{27}
$$



Explicitly,



$$
p_{n+1}X+p_nY
 =(-1)^{n+1}
  (p_nb_{n+1}-p_{n+1}b_n)\in\mathbb Z.
\tag{28}
$$



This adjacent statement is not needed for the factor theorem, but it
shows that even the smallest direct first-jet cancellation pays the
Bessel main scale before any root factor is imposed.  Longer shift
syzygies can encode recurrence cancellations with smaller displayed
coefficients; after the four-generator reduction, however, the formal
root factor is still exactly the $q_n$ factor in (24).

## 6. Aggregate consequence and exact scope

Let $\mathcal P$ contain primes for which $q_n\ne0$; no ordinary-root
hypothesis is needed for the elementary divisibility (7).  Since
$D_{n,\mathcal P}\mid q_n$, equations (7) and (10) follow.  The
standard recurrence bounds give



$$
\prod_{j=2}^{n}(4j-2)<q_n<\prod_{j=2}^{n}4j
 \qquad(n\geq2),
\tag{29}
$$



and hence (8).

The obstruction is exact in the following scope.

- **Covered:** arbitrary finite parameter shifts; first parameter jets;
  arbitrary polynomial combinations and determinants; coefficients in
  $\mathbb Q[x]$ after honest denominator clearing; and local order
  certified solely by the recurrence, its first derivative, and the
  equation $f_p(\rho)=0$.
- **Not covered:** an auxiliary whose residual polynomial has special
  high order at the actual $\rho$; arithmetic relations among the
  different $\mathcal K_p$; higher or infinite jet data supplied with
  a new height theorem; integral transforms; or nontrivial infinite-tail
  cancellation.

Thus (7) is a rigorous no-go for the proposed aggregate product-formula
shortcut within the finite shift--first-jet algebra.  It does not prove
the desired bound on $v_p(q_n)$, and it makes no claim about
irrationality or transcendence of $e+\pi$.

## 7. Certificate

The companion script

    scripts/bessel_aggregate_shift_jet_product_formula_no_go_certificate.py

checks with exact symbolic and integer arithmetic:

1. the value and first-jet reductions (15)--(16) on a shift grid;
2. the all-integer affine jet formulas (5) under those reductions;
3. coefficientwise $q_n^s$-divisibility after substituting (23) into
   sample formal root factors of several orders;
4. the primitive adjacent cancellation (26)--(28); and
5. finite aggregate divisibility instances of (10).

The certificate is a regression check.  The all-parameter proof is
Sections 2--6.
