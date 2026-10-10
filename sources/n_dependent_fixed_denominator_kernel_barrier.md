> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An $n$-dependent fixed-denominator kernel barrier

Date: 2026-08-26

## Result

This note treats a surviving direct-integral direction left open by the
fixed-kernel theorem.  The numerator may now depend on $n$, may change
sign, and may have a growing zero at the midpoint.  The denominator remains
fixed.

Let $Q\in\mathbb Z[x]$ be fixed and have no zero on $[0,1]$.  For each
even $n$ in an infinite index set, let



$$
K_n(x)=\frac{P_n(x)}{Q(x)},\qquad
 0\ne P_n\in\mathbb Q[x],
$$



and suppose



$$
J_n=\int_0^1x^n(1-x)^nK_n(x)\,dx
 =r_n+\varepsilon_nc_n\pi,
 \quad r_n,c_n\in\mathbb Q,\quad c_n>0,\quad
 \varepsilon_n\in\{1,-1\}.                     \tag{1}
$$



The correct complexity of $P_n$ is projective, because multiplication of
the whole kernel by a nonzero rational number does not change its primitive
integer $\pi$-pair.  Choose a primitive integer polynomial
$\widehat P_n\in\mathbb Z[x]$, unique up to sign, and
$\lambda_n\in\mathbb Q^\times$ such that



$$
P_n=\lambda_n\widehat P_n.
$$



Put



$$
d_n=\deg\widehat P_n,\qquad
 \mathcal H_n=\max\{2,\|\widehat P_n\|_1\},\qquad
 S_n=n+d_n+\log\mathcal H_n.                    \tag{2}
$$



**Theorem.**  If



$$
S_n=o(n\log n),                                \tag{3}
$$



then the absolute values of the final primitive, minimally
coefficient-matched $e+\pi$ forms tend to infinity along the index set in
(1).

In particular, the theorem covers



$$
d_n=O(n),\qquad
 \|\widehat P_n\|_1=\exp(O(n)),                 \tag{4}
$$



and, more generally, any projective numerator degree and logarithmic
height whose sum is $o(n\log n)$.  It requires no sign condition, no
uniform midpoint Taylor expansion, and no analytic noncancellation
assumption.

For integer-coefficient $P_n$ of degree $O(n)$, a bound
$\max_j|[x^j]P_n|=\exp(O(n))$ implies (4).  For rational coefficients,
the height must be measured after clearing all coefficient denominators
and taking primitive content.  Separate height bounds on individual
coefficients are not equivalent: the least common multiple of many
unrelated denominators can be much larger.

The key new input is a finite irrationality measure for $\pi$.  It turns
an upper bound for the primitive $\pi$-coefficient into a lower bound for
the value of the $\pi$-form.  Thus arbitrary analytic cancellation cannot
beat the arithmetic height within this class.

This is still a construction-specific obstruction.  It does not prove any
unconditional arithmetic statement about $e+\pi$.

## 1. A uniform lower bound for integer $\pi$-forms

Salikhov proved that the irrationality measure of $\pi$ is at most
$7.6063\ldots$: for all sufficiently large positive $q$,



$$
\left|\pi-\frac pq\right|\geq q^{-\nu_0},
 \qquad \nu_0=7.6063\ldots .                    \tag{5}
$$



Only the weaker integer exponent $8$ is needed here.

### Lemma 1.1

There is a constant $c_\pi>0$ such that, for every $A\in\mathbb Z$,
$B\in\mathbb Z_{\geq1}$, and $\delta\in\{1,-1\}$,



$$
|A+\delta B\pi|\geq c_\pi B^{-7}.              \tag{6}
$$



### Proof

Write



$$
|A+\delta B\pi|
 =B\left|\pi-\frac{-\delta A}{B}\right|.
$$



When $-\delta A$ is positive and $B$ is sufficiently large, (5) is
stronger than $B^{-8}$, and hence the displayed expression is at least
$B^{-7}$.  A nonpositive numerator gives an elementary larger lower
bound.  The finitely many remaining denominator values have a positive
minimum after choosing the nearest integer numerator, because $\pi$ is
irrational.  Decreasing one fixed constant gives (6) in every case.
$\square$

Reference: V. Kh. Salikhov, “On the irrationality measure of
$\pi$,” Russian Mathematical Surveys 63:3 (2008), 570–572,
[DOI 10.1070/RM2008v063n03ABEH004543](https://doi.org/10.1070/RM2008v063n03ABEH004543).
Theorem 1 of that paper is (5).

## 2. The primitive exponential form

For even $n$, put



$$
E_n=\frac1{n!}\int_0^1x^n(1-x)^ne^x\,dx
 =q_ne-p_n>0.                                   \tag{7}
$$



Repeated integration by parts gives integer $p_n,q_n$.  Their common
endpoint sums are



$$
p_n=\sum_{j=0}^n\frac{(n+j)!}{j!(n-j)!},\qquad
 q_n=(-1)^n\sum_{j=0}^n(-1)^j
                 \frac{(n+j)!}{j!(n-j)!}.
$$



Both sequences satisfy



$$
X_n=2(2n-1)X_{n-1}+X_{n-2},
$$



with



$$
(p_0,p_1)=(1,3),\qquad(q_0,q_1)=(1,1).
$$



For



$$
D_n=p_nq_{n-1}-p_{n-1}q_n,
$$



the recurrence gives $D_n=-D_{n-1}$, while $D_1=2$.  Thus every
adjacent determinant has absolute value $2$, and the recurrence shows
that all entries of both sequences are odd.  Hence



$$
\gcd(p_n,q_n)=1.                               \tag{8}
$$



For every positive even $n$ (equivalently, $n\geq2$), reversing the
alternating endpoint sum for $q_n$ gives



$$
q_n\geq\frac{n(2n-1)!}{n!}
 =n\prod_{k=n+1}^{2n-1}k
 \geq n^n.                                      \tag{9}
$$



Positivity of the integrand and $e^x\leq e$ give



$$
0<E_n\leq\frac{e\,n!}{(2n+1)!}.                \tag{10}
$$



Consequently



$$
\frac{E_n}{q_n}
 \leq
 \frac{e}{n^n(n+1)^{n+1}}
 \leq e\,n^{-2n-1}.                             \tag{11}
$$



## 3. A universal subfactorial-coefficient matching lemma

The following statement no longer mentions integrals.

### Lemma 3.1

For each even $n$, let



$$
L_n=A_n+\varepsilon_nB_n\pi
$$



be a primitive integer pair, where $B_n>0$.  Orient it by its value:



$$
s_n=\operatorname{sgn}L_n,\qquad
 \widetilde L_n=s_nL_n
 =\widetilde A_n+\delta_nB_n\pi>0,
\qquad \delta_n=s_n\varepsilon_n.
$$



If



$$
\log B_n=o(n\log n),                            \tag{12}
$$



then the final primitive minimally matched $e+\pi$ forms obtained from
(7) and $\widetilde L_n$ tend to infinity in absolute value.

More quantitatively, for all sufficiently large $n$,



$$
|\Lambda_n^{\rm prim}|
 \geq\frac{c_\pi}{2}\frac{q_n}{B_n^9}.          \tag{13}
$$



### Proof

Put



$$
d=\gcd(q_n,B_n),\qquad q_n=dq_0,\qquad B_n=dB_0.
$$



The minimal positive coefficient multipliers are $B_0,q_0$, and the
common target coefficient is $dq_0B_0$.  The matched constant coefficient
has the form



$$
M=-B_0p_n\mathbin{\pm}q_0\widetilde A_n.        \tag{14}
$$



Every prime dividing $q_0$ is excluded from $M$ by
$\gcd(p_n,q_n)=1$, and every prime dividing $B_0$ is excluded by
$\gcd(\widetilde A_n,B_n)=1$.  Therefore the final content $g$
satisfies



$$
g\mid d.                                       \tag{15}
$$



This is a prime-power statement, not merely a square-free one.

If $\delta_n=1$, the raw matched form is the positive sum



$$
W_n^+=B_0E_n+q_0\widetilde L_n.
$$



Using $g\leq d\leq B_n$,



$$
\left|\frac{W_n^+}{g}\right|
 \geq\frac{q_n|L_n|}{B_n^2}
 \geq c_\pi\frac{q_n}{B_n^9},                  \tag{16}
$$



where the second inequality is (6).

If $\delta_n=-1$, the matched form with equal positive coefficients of
$e$ and $\pi$ is



$$
W_n^-=B_0E_n-q_0\widetilde L_n
 =\frac{q_nB_n}{d}
  \left(\frac{E_n}{q_n}-\frac{|L_n|}{B_n}\right).
                                                               \tag{17}
$$



By (6) and (11), the ratio of the first positive term in parentheses to
the second satisfies



$$
0\leq
 \frac{E_n/q_n}{|L_n|/B_n}
 \leq c_\pi^{-1}e\,B_n^8n^{-2n-1}.              \tag{18}
$$



Assumption (12) makes the right side tend to zero.  It is therefore at
most $1/2$ for all sufficiently large $n$.  Equations (15), (17), and
(6) then give



$$
\left|\frac{W_n^-}{g}\right|
 \geq\frac{q_n|L_n|}{2B_n^2}
 \geq\frac{c_\pi}{2}\frac{q_n}{B_n^9}.          \tag{19}
$$



Equations (16) and (19) prove (13).  Finally, (9) and (12) imply



$$
\frac{q_n}{B_n^9}
 \geq\exp\!\left(n\log n-o(n\log n)\right)
 \longrightarrow\infty.
$$



This proves the lemma. $\square$

## 4. Fixed-denominator projective height

### Lemma 4.1

Fix $Q$ as in the theorem.  There is a constant $C_Q$ with the
following property.  Let



$$
\widehat P\in\mathbb Z[x],\qquad
 d=\deg\widehat P,\qquad
 \mathcal H=\max\{2,\|\widehat P\|_1\},
$$



and, for a reduced rational number $a/b$ with $b>0$, write
$H(a/b)=\max\{|a|,b\}$.  Put



$$
\widehat J_n=
 \int_0^1x^n(1-x)^n\frac{\widehat P(x)}{Q(x)}\,dx.
$$



If



$$
\widehat J_n=\rho+\gamma\pi,\qquad
 \rho,\gamma\in\mathbb Q,
$$



then



$$
H(\rho),H(\gamma)
 \leq
 \exp\!\left(C_Q(n+d+\log\mathcal H)\right).     \tag{20}
$$



If $\gamma\ne0$, the $\pi$-coefficient $B$ in the primitive integer
normalization satisfies



$$
B\leq
 \exp\!\left(C_Q(n+d+\log\mathcal H)\right).     \tag{21}
$$



### Proof

The dividend



$$
D_n(x)=\widehat P(x)x^n(1-x)^n
$$



has degree $2n+d$ and



$$
\|D_n\|_1\leq\mathcal H\,2^n.                  \tag{22}
$$



Divide $D_n$ by the fixed polynomial $Q$.  There are
$2n+d+O_Q(1)$ long-division steps.  At each step a common denominator is
multiplied by at most the fixed leading coefficient of $Q$, while the
integer numerator norm is multiplied by at most a fixed constant depending
only on $Q$.  Thus



$$
\frac{D_n(x)}{Q(x)}
 =U_n(x)+\frac{R_n(x)}{Q(x)},\qquad
 \deg R_n<\deg Q,                               \tag{23}
$$



where all coefficients of $U_n,R_n$ can be put on one denominator, with
that denominator and all numerators at most



$$
\exp\!\left(C_Q(n+d+\log\mathcal H)\right).     \tag{24}
$$



The degree of $U_n$ is at most $2n+d$.  Its integral introduces only
the least common multiple of the integers through $2n+d+1$.  The
elementary bound



$$
\operatorname{lcm}(1,2,\ldots,m)\leq16^m
$$



shows that this cost is still covered by (24).

For $0\leq j<\deg Q$, put



$$
\omega_j=\int_0^1\frac{x^j}{Q(x)}\,dx.
$$



These are fixed finite real numbers because $Q$ is zero-free on the
interval.  If $\deg Q=0$, the remainder and this list are empty.  In the
finite-dimensional rational vector space spanned by



$$
1,\quad\pi,\quad\omega_0,\ldots,\omega_{\deg Q-1},
$$



extend $1,\pi$ to a fixed basis.  Expressing each $\omega_j$ in this
basis costs only a fixed rational coordinate matrix.  Equations
(23)--(24), followed by integration, therefore bound every coordinate of
$\widehat J_n$ by (20).  If the other coordinates vanish, coordinate
uniqueness identifies the first two as $\rho,\gamma$.

Writing $\rho=a/b$, $\gamma=u/v$ in lowest terms and clearing the two
denominators gives a pre-primitive $\pi$-coefficient at most $b|u|$.
Primitive reduction can only decrease it.  Equation (20), with an enlarged
constant, proves (21). $\square$

### Projective scaling

Since $P_n=\lambda_n\widehat P_n$,



$$
J_n=\lambda_n\widehat J_n.
$$



Multiplication of the rational coordinate pair by
$\lambda_n\in\mathbb Q^\times$ does not change its primitive integer
representative, except possibly for an overall sign.  Hence the $B_n$
appearing in Lemma 3.1 is exactly the projective $B_n$ bounded by Lemma
4.1.  An enormous common numerator or denominator in $\lambda_n$ is
irrelevant to matching.

Under (3), equations (2) and (21) give



$$
\log B_n=o(n\log n).
$$



Lemma 3.1 now proves the main theorem.

## 5. Variable midpoint order and the exact beta factor

This section quantifies what a growing midpoint zero can and cannot do.
It is not needed for the arithmetic proof above.

Symmetrize the projectively normalized kernel:



$$
\widehat K_{n,\mathrm s}(x)
 =\frac{\widehat P_n(x)Q(1-x)+
        \widehat P_n(1-x)Q(x)}
       {2Q(x)Q(1-x)}.                            \tag{25}
$$



If the numerator in (25) were identically zero, every symmetric beta
moment would vanish, contradicting (1) and $c_n>0$.  Otherwise its zero
at $x=1/2$ has an even finite order $2m_n$, and



$$
2m_n\leq d_n+\deg Q.                            \tag{26}
$$



There is a continuous function $G_n$, with $G_n(0)\ne0$, such that



$$
\widehat K_{n,\mathrm s}(1/2+t)
 =t^{2m_n}G_n(t).                               \tag{27}
$$



For integers $n,m\geq0$, define



$$
M_{n,m}=\int_{-1/2}^{1/2}
          (1-4t^2)^nt^{2m}\,dt.
$$



Two substitutions give the exact formula



$$
M_{n,m}
 =\frac1{2\cdot4^m}
   B\left(m+\frac12,n+1\right).                 \tag{28}
$$



Equivalently,



$$
4^{-n}M_{n,m}
 =
 \frac{2(2m)!\,n!\,(n+m+1)!}
      {4^m m!(2n+2m+2)!}.                       \tag{29}
$$



Equation (27) gives the always-valid upper bound



$$
|\widehat J_n|
 \leq4^{-n}\|G_n\|_{\infty}M_{n,m_n}.           \tag{30}
$$



If, for one sign $\sigma_n$, there are positive numbers
$g_n^-,g_n^+$ such that



$$
0<g_n^-\leq\sigma_nG_n(t)\leq g_n^+
 \qquad(-1/2\leq t\leq1/2),
$$



then the exact two-sided comparison is



$$
g_n^-4^{-n}M_{n,m_n}
 \leq|\widehat J_n|
 \leq g_n^+4^{-n}M_{n,m_n}.                     \tag{31}
$$



Without such sign control, the midpoint order by itself gives no analytic
lower bound: $G_n$ may change sign and its weighted integral may cancel.

The monomial beta factor is only exponentially small in $n+m$.  Indeed,
on $x\in[1/8,1/4]$,



$$
x(1-x)\geq\frac7{64},\qquad
 |x-1/2|\geq\frac14,
$$



whereas on all of $[0,1]$,



$$
x(1-x)\leq\frac14,\qquad |x-1/2|\leq\frac12.
$$



Therefore



$$
\frac18\left(\frac7{64}\right)^n16^{-m}
 \leq4^{-n}M_{n,m}
 \leq4^{-n-m}.                                  \tag{32}
$$



Thus a midpoint zero of order $O(n)$ supplies only an
$\exp(-O(n))$ beta penalty.  It does not approach the
$\exp(-n\log n)$ scale of the exponential coefficient $q_n$.

There is also a projective norm bound for the residual factor in (27).
The coefficient norm of the numerator in (25) is at most



$$
\mathcal H_n\exp(O_Q(d_n)).
$$



After translating $x=1/2+t$, its coefficient norm grows by at most
$\exp(O_Q(d_n))$; division by $t^{2m_n}$ merely removes leading zero
coefficients.  Since the fixed denominator in (25) is bounded away from
zero on the interval,



$$
\log\!\left(1+\|G_n\|_\infty\right)
 \leq C_Q(d_n+\log\mathcal H_n).                 \tag{33}
$$



Finally, Lemmas 1.1 and 4.1 give an arithmetic lower bound even when
$G_n$ changes sign.  In the projective normalization,



$$
|\widehat J_n|
 \geq
 \exp\!\left(-C_Q'(n+d_n+\log\mathcal H_n)\right)               \tag{34}
$$



for a fixed $C_Q'>0$.  To see this, the nonzero rational
$\pi$-coordinate has absolute value at least the reciprocal of its
height in (20), while



$$
\frac{|\widehat J_n|}{|\gamma_n|}
 =\frac{|L_n|}{B_n}
 \geq c_\pi B_n^{-8}.
$$



Equations (30), (33), and (34) state precisely how arithmetic prevents
uncontrolled analytic cancellation in the class of the theorem.

## 6. Necessary escape scales

The proof also gives quantitative necessary conditions for escaping this
obstruction.

Suppose the final primitive matched forms are bounded along an infinite
subsequence.

If $\delta_n=1$, equation (16) and $q_n\geq n^n$ force



$$
\log B_n\geq\frac19n\log n-O(1).                \tag{35}
$$



If $\delta_n=-1$ and the $\pi$-form term dominates by a factor at least
two, (19) gives the same condition.  If it does not dominate, (18) forces
the stronger estimate



$$
\log B_n\geq\frac14n\log n-O(\log n).           \tag{36}
$$



Thus, in every sign case, a bounded escaping subsequence requires at least



$$
B_n\geq n^{\,n/9-o(n)}.                         \tag{37}
$$



For genuine opposite-sign cancellation to remain competitive with
$E_n/q_n$, the stronger scale in (36), approximately
$n^{n/4}$, is necessary.

By (21), condition (37) is impossible when $S_n=o(n\log n)$.  More
generally, escape requires



$$
n+d_n+\log\mathcal H_n=\Omega_Q(n\log n).       \tag{38}
$$



Consequently, an $O(n)$ midpoint zero, an $O(n)$ degree, and
exponential projective coefficient height are all still inside the
barrier.  To leave by increasing the midpoint order itself, one must at
least move the numerator degree to the $n\log n$ scale; (26) makes this
necessary.  Alternatively, one needs factorial-scale projective
coefficient height, a denominator depending on $n$, or a construction
outside coefficient cross-matching.

Conditions (35)--(38) are necessary scales for evading this theorem, not a
claim that kernels at those scales succeed.

## 7. Residual scope

The theorem leaves the following direct-integral possibilities genuinely
open:

1. projective numerator degree or logarithmic height of order
   $n\log n$ or larger;
2. a denominator $Q_n$ whose degree, coefficients, or poles vary with
   $n$;
3. nonrational kernels;
4. different weights for the $e$- and $\pi$-forms;
5. synchronization mechanisms other than integer coefficient matching.

The main structural conclusion is that allowing a mildly growing,
sign-changing numerator does not repair the common-beta construction.
Within fixed denominator and subfactorial projective complexity, the
finite irrationality measure of $\pi$, the exact content lemma, and the
factorial growth of $q_n$ together force divergence.
