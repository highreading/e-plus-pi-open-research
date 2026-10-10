> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Prime-power divisibility of the Bessel denominator as exact Padé-root proximity

Checked: 2026-08-27 UTC.

## 1. Scope and verdict

Put



$$
Q_n(x)=\sum_{k=0}^n(-1)^k
 \frac{(2n-k)!}{k!(n-k)!}x^k,
 \qquad P_n(x)=Q_n(-x),                                    \tag{1}
$$



and



$$
q_n=Q_n(1),\qquad p_n=P_n(1).
\tag{2}
$$



Thus $q_0=q_1=1$, $p_0=1,p_1=3$, and both integer sequences
satisfy



$$
X_n=(4n-2)X_{n-1}+X_{n-2}.                              \tag{3}
$$



This note audits a natural proposed route to an upper bound for
$v_p(q_n)$: regard $p^a\mid Q_n(1)$ as a polynomial Hensel-lifting
problem in the argument of the Padé denominator.

The argument-root problem is, in fact, always simple.  More strongly,



$$
\boxed{P_n(1)Q_n'(1)\equiv(-1)^n\pmod {q_n}.}            \tag{4}
$$



Consequently, if $a=v_p(q_n)>0$, there is a unique root
$\xi_{n,p}\in\mathbb Z_p$ of $Q_n$ in $1+p\mathbb Z_p$, and



$$
\boxed{v_p(1-\xi_{n,p})=v_p(q_n)=a.}                    \tag{5}
$$



Its first nonzero Hensel displacement is completely explicit:



$$
\boxed{
 \xi_{n,p}\equiv
 1-(-1)^nP_n(1)q_n\pmod {p^{2a}}.}                        \tag{6}
$$



Thus the desired prime-power-height estimate is exactly a uniform
$p$-adic proximity estimate for a root which varies with both $n$ and
$p$.  Standard polynomial resultants do not supply such an estimate:



$$
\boxed{\operatorname {Res}_x(x-1,Q_n(x))=Q_n(1)=q_n.}    \tag{7}
$$



Moreover the naive coefficient height is already



$$
H(Q_n)=\frac{(2n)!}{n!},\qquad
 \log H(Q_n)=n\log n+O(n),                               \tag{8}
$$



the same main logarithmic scale as $q_n$.  Hence a Liouville/root-height
estimate applied separately to the changing algebraic number
$\xi_{n,p}$, or the resultant (7), merely repackages the original
$O(n\log n)$ bound.  It does not prove the required
$v_p(q_n)\log p=o(n\log n)$.

This is also a precise warning about two different Hensel problems.  The
argument root $x=1\pmod p$ is always simple by (4), even when the root of
the *index sequence* $r\mapsto q_r$ is singular under the shift
$r\mapsto r+p$.  The central index example $p=79,r=39$ is singular in
the latter sense while $Q_{39}'(1)$ is a unit modulo $79$.  Polynomial
argument simplicity therefore cannot exclude all-$p$ index branching or
bound the depth of an ordinary index lift.

Nothing in this note classifies $e+\pi$.

## 2. Exact Padé Wronskian

The defining coefficients in (1) give the diagonal Padé relation



$$
P_n(x)-e^xQ_n(x)=O(x^{2n+1})                             \tag{9}
$$



as a formal power series at the origin.  Differentiate (9), replace
$e^x$ by $P_n/Q_n+O(x^{2n+1})$, and multiply by $Q_n$.  The
polynomial



$$
W_n(x)=P_n'(x)Q_n(x)-P_n(x)Q_n'(x)-P_n(x)Q_n(x)          \tag{10}
$$



is divisible by $x^{2n}$.  It has degree at most $2n$.  Its leading
coefficient comes only from $-P_nQ_n$; the leading coefficients of
$P_n,Q_n$ are $1,(-1)^n$, respectively.  Hence



$$
\boxed{W_n(x)=(-1)^{n+1}x^{2n}.}                         \tag{11}
$$



At $x=1$, reduce (11) modulo $q_n=Q_n(1)$.  The two terms containing
$Q_n(1)$ disappear and give



$$
-P_n(1)Q_n'(1)\equiv(-1)^{n+1}\pmod {q_n},
$$



which is (4).  In particular,



$$
\gcd(P_n(1),q_n)=\gcd(Q_n'(1),q_n)=1.                  \tag{12}
$$



This is an integral congruence modulo the full denominator, not merely a
prime-level statement.

## 3. Exact Hensel valuation and displacement

Let $p$ be an odd prime and $a=v_p(q_n)>0$.  Equation (4) shows that
$Q_n'(1)$ is a $p$-adic unit.  The simple-root form of Hensel's lemma
therefore gives a unique



$$
\xi_{n,p}\in1+p\mathbb Z_p,\qquad Q_n(\xi_{n,p})=0.      \tag{13}
$$



The derivative remains a unit throughout this residue ball.  Taylor's
formula between $1$ and $\xi_{n,p}$ gives



$$
q_n=Q_n(1)=(1-\xi_{n,p})U,\qquad U\in\mathbb Z_p^\times,
\tag{14}
$$



which proves (5).

Modulo $p^a$, (4) also gives



$$
Q_n'(1)^{-1}\equiv(-1)^nP_n(1)\pmod {p^a}.              \tag{15}
$$



One Newton step at $1$ is accurate modulo $p^{2a}$, because its
displacement has valuation $a$.  Thus



$$
\xi_{n,p}
 \equiv1-q_nQ_n'(1)^{-1}
 \equiv1-(-1)^nP_n(1)q_n\pmod {p^{2a}},
$$



which proves (6).

For example, the previously certified values



$$
v_{13}(q_8)=2,\qquad v_7(q_{18})=3                      \tag{16}
$$



produce simple roots of $Q_8,Q_{18}$ whose distances from $1$ are
exactly $13^{-2}$ and $7^{-3}$, respectively.  These examples already
show why argument-root simplicity does not imply squarefreeness of
$q_n$.

## 4. Why resultants and elementary root heights remain at main scale

The first polynomial is $x-1$, so its resultant with $Q_n$ is its
evaluation on the root $1$:



$$
\operatorname {Res}_x(x-1,Q_n(x))=Q_n(1)=q_n,
$$



proving (7).  Therefore the resultant records the full prime-power depth
but is not an external integer of smaller size.

The absolute values of the coefficients in (1) decrease with $k$.  If



$$
c_{n,k}=\frac{(2n-k)!}{k!(n-k)!},
$$



then



$$
\frac{c_{n,k+1}}{c_{n,k}}
 =\frac{n-k}{(k+1)(2n-k)}<1                              \tag{17}
$$



for $0\le k<n$.  Hence



$$
H(Q_n)=c_{n,0}=\frac{(2n)!}{n!}.                         \tag{18}
$$



Stirling's formula proves (8).  Independently, the recurrence bounds



$$
\prod_{j=2}^n(4j-2)\le q_n<\prod_{j=2}^n4j
$$



give



$$
\log q_n=n\log n+O(n).                                  \tag{19}
$$



Thus the coefficient height, the exact resultant, and the integer whose
valuation is being estimated all live on the same $n\log n$ scale.  A
generic algebraic-number separation bound for a root of $Q_n$ cannot be
substituted for the missing arithmetic theorem: the target root changes
with $n,p$, and its defining polynomial already pays the forbidden main
height.

The Padé Wronskian remains useful as a structural statement: it proves
that high prime powers in $q_n$ are not caused by a repeated polynomial
root at $x=1$.  What remains is a squarefull-value problem for the
specialization $Q_n(1)$, or equivalently the moving-root proximity (5).

## 5. Exact certificate

The companion script

    scripts/bessel_pade_argument_hensel_certificate.py

checks with exact integer and modular arithmetic:

1. the polynomial recurrence and Wronskian (11) through degree $14$;
2. the full-modulus inverse congruence (4) through degree $80$;
3. the coefficient-height assertion (18) through degree $80$; and
4. the Hensel displacement (6), including exact valuation, for
   $(n,p,a)=(8,13,2),(18,7,3),(361,7,4),(1359,11,5)$.

The all-degree statements are proved above; the finite calculation is a
regression certificate rather than a substitute for those proofs.
