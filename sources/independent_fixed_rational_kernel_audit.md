> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the fixed-rational-kernel barrier

Audited: 2026-08-26 UTC

## Verdict and audited checkpoint

**ACCEPT** for the frozen target

    sources/fixed_rational_kernel_barrier.md
    SHA-256 13ce4459b6f3226a862f1cb3df1cf3b1d87a895e315a352f9a65caad6b850fba

The exponential-height lemma, its corollary, the prime-power content lemma,
both signs in the matching theorem, and every constant in target equations
(23)--(28) are correct at this checkpoint.  The conclusion is uniform in
all sufficiently large indices and therefore remains valid on an arbitrary
infinite, possibly sparse, set of even indices.

This acceptance is checkpoint-specific.  Two errors were found in earlier
drafts and were corrected in the target before this verdict:

1. the original equation (6) omitted the factor $(-1)^n$; at $n=1$ its
   displayed sum was $-1$, contradicting the asserted $q_1=1$ and the
   positive recurrence;
2. the rational-function division initially did not say that $P/Q$ was
   reduced.  Without that choice, a removable-factor presentation such as
   $1=x/x$ makes the auxiliary integral $\int_0^1dx/x$ divergent even
   though the rational function has no pole.

The frozen target now defines



$$
q_n=(-1)^n\sum_{j=0}^n(-1)^j
     \frac{(n+j)!}{j!(n-j)!}
$$



and explicitly chooses coprime $P,Q$, from which the zero-freeness of
$Q$ on $[0,1]$ follows.  The target itself was not edited during this
independent audit.

## 1. Primitive exponential form

Put



$$
a_{n,j}=\frac{(n+j)!}{j!(n-j)!}.
$$



These are integers.  The two target sums are the Bessel-polynomial
specializations



$$
p_n=\sum_{j=0}^na_{n,j},\qquad
 q_n=(-1)^n\sum_{j=0}^n(-1)^ja_{n,j}.
$$



Direct coefficient comparison gives, for either sequence,



$$
X_n=2(2n-1)X_{n-1}+X_{n-2},
$$



with



$$
(q_0,q_1)=(1,1),\qquad (p_0,p_1)=(1,3).
$$



The first values are



$$
\begin{aligned}
 q_n&=1,1,7,71,1001,18089,398959,\ldots,\\
 p_n&=1,3,19,193,2721,49171,1084483,\ldots .
 \end{aligned}
$$



For the adjacent determinant



$$
D_n=p_nq_{n-1}-p_{n-1}q_n
$$



the recurrence gives $D_n=-D_{n-1}$, while $D_1=2$.  Hence
$|D_n|=2$.  The recurrence also shows inductively that every $p_n,q_n$
is odd.  Any common divisor of $p_n,q_n$ divides $D_n$, but it cannot
be even, so



$$
\gcd(p_n,q_n)=1.
$$



This validates the target's primitive normalization.

For the lower bound on $q_n$, reverse the alternating sum.  Its absolute
terms are strictly decreasing because



$$
\frac{a_{n,j-1}}{a_{n,j}}
 =\frac{j}{(n+j)(n-j+1)}<1.
$$



The first two reversed terms differ by



$$
\frac{(2n)!}{n!}-\frac{(2n-1)!}{(n-1)!}
 =\frac{n(2n-1)!}{n!}.
$$



The remaining decreasing alternating tail is nonnegative.  Therefore



$$
q_n\geq\frac{n(2n-1)!}{n!},
$$



which is target (9).  Finally,



$$
E_n=\frac1{n!}\int_0^1x^n(1-x)^ne^x\,dx
$$



is positive and, since $e^x\leq e$,



$$
0<E_n\leq
 \frac e{n!}B(n+1,n+1)
 =\frac{e\,n!}{(2n+1)!}.
$$



Thus target (10) and all primitive-exponential inputs used later are
correct.

## 2. Uniform exponential height in Lemma 2.1

This section reconstructs the denominator argument rather than relying on
the target's qualitative wording.

### 2.1 Rational long division

Choose the target's fixed coprime representation



$$
K=P/Q,\qquad P,Q\in\mathbb Z[x],
$$



and write



$$
Q(x)=a_dx^d+\cdots+a_0,\qquad a_d\ne0.
$$



Because the representation is reduced and $K$ has no pole on
$[0,1]$, $Q$ has no zero there.  Thus all later definite integrals
against $1/Q$ exist.

Let



$$
D_n(x)=P(x)x^n(1-x)^n .
$$



Its degree is at most $2n+\deg P$, and



$$
\|D_n\|_1\leq\|P\|_1\,2^n.                       \tag{A1}
$$



Long division has at most



$$
T_n=2n+O_K(1)                                   \tag{A2}
$$



steps.  After $k-1$ steps, suppose the current polynomial is written on
the common denominator $a_d^{\,k-1}$.  Dividing its leading coefficient
by $a_d$ and subtracting the corresponding translate of $Q$ puts the
next polynomial on denominator $a_d^k$.  If $N_{k-1}$ is the
$\ell^1$-norm of its integer numerator, then



$$
N_k\leq\bigl(|a_d|+\|Q\|_1\bigr)N_{k-1}.         \tag{A3}
$$



Equations (A1)--(A3), with the fixed extra scaling needed to put all earlier
quotient coefficients on the final denominator, give constants
$\alpha,\beta\geq1$, depending only on $K$, such that the quotient
$S_n$ and remainder $R_n$ have one common denominator $D_n'$ with



$$
D_n'\leq\alpha^n,\qquad
 \max\{\|D_n'S_n\|_1,\|D_n'R_n\|_1\}\leq\beta^n. \tag{A4}
$$



Here $\deg R_n<d$ and $\deg S_n=O_K(n)$.  This proves the target's
long-division assertion without assuming that independently reduced
coefficient denominators are compatible.

The constant-denominator case $d=0$ is harmless: $R_n=0$, and the same
bounds hold after absorbing the fixed nonzero constant $Q$.

### 2.2 The least-common-multiple cost is exponential

Let



$$
\mathcal L_m=\operatorname{lcm}(1,2,\ldots,m).
$$



An entirely elementary exponential estimate suffices.  For every prime
power $p^a\leq2m$, either $p^a\leq m$, or the missing factor of $p$
occurs in $\binom{2m}{m}$.  Hence



$$
\mathcal L_{2m}\mid
 \mathcal L_m\binom{2m}{m},
\qquad
 \mathcal L_{2m}\leq4^m\mathcal L_m.             \tag{A5}
$$



Iteration at powers of two, followed by monotonicity, gives for example



$$
\mathcal L_m\leq16^m.    \tag{A6}
$$



If $S_n=(D_n')^{-1}\sum_{k=0}^{M_n}s_kx^k$, where
$M_n=O_K(n)$, then



$$
\int_0^1S_n(x)\,dx
 =\frac1{D_n'}\sum_{k=0}^{M_n}\frac{s_k}{k+1}.
$$



Putting the sum on denominator $D_n'\mathcal L_{M_n+1}$, using (A4),
(A6), and the $O_K(n)$ number of summands, proves



$$
H\!\left(\int_0^1S_n(x)\,dx\right)\leq C_2^n
$$



for a fixed $C_2$.  No factorial denominator is introduced here.

### 2.3 The finite-coordinate argument

For $0\leq j<d$, define the finite real constants



$$
\omega_j=\int_0^1\frac{x^j}{Q(x)}\,dx.
$$



The space



$$
V=\operatorname{span}_{\mathbb Q}
       \{1,\pi,\omega_0,\ldots,\omega_{d-1}\}
$$



is finite dimensional.  Since $\pi\notin\mathbb Q$, $1,\pi$ are
linearly independent and can be extended to a fixed basis



$$
1,\pi,\theta_1,\ldots,\theta_t.
$$



Write the fixed rational coordinates of every $\omega_j$ in this basis
as



$$
\omega_j=\lambda_{j,0}+\lambda_{j,1}\pi
            +\sum_{\ell=1}^t\lambda_{j,\ell+1}\theta_\ell,
\qquad\lambda_{j,k}\in\mathbb Q.                 \tag{A7}
$$



There are only $d$ remainder coefficients and the coordinate matrix
$(\lambda_{j,k})$ is fixed.  Combining (A4), the integrated-polynomial
bound, and (A7) therefore places every coordinate of $J_n(K)$ on a
denominator and numerator bounded by $C_3^n$.

If



$$
J_n(K)=r+c\pi,
$$



coordinate uniqueness says that these first two coordinates are exactly
$r,c$ and all $\theta_\ell$-coordinates vanish.  Therefore



$$
H(r),H(c)\leq C_K^n.
$$



Replacing $c$ by $-c$ proves the negative-sign version.  This completes
an independent derivation of Lemma 2.1.  It also shows why the hypothesis
that no other constants occur in a relevant moment is essential: it is what
forces the extra coordinates to vanish, not an assumption that the
individual $\omega_j$ themselves lie in $\mathbb Q+\mathbb Q\pi$.

## 3. Corollary 2.2 and normalization

Write in lowest terms



$$
r_n=\frac{a_n}{b_n},\qquad
 c_n=\frac{u_n}{v_n},
\qquad b_n,v_n>0,\quad u_n>0.
$$



Let $T_n=\operatorname{lcm}(b_n,v_n)$.  Before primitive reduction, the
integer coefficient of $\pi$ is



$$
\frac{T_nu_n}{v_n}
 \leq b_nu_n,                                    \tag{A8}
$$



because $T_n\leq b_nv_n$.  Dividing the integer pair by its content
cannot increase this coefficient, so



$$
B_n\leq b_nu_n.
$$



It follows more explicitly than in the target that



$$
c_nB_n
 \leq\frac{u_n}{v_n}b_nu_n
 \leq b_nu_n^2.                                  \tag{A9}
$$



Lemma 2.1 bounds $b_n$ and $u_n$ exponentially.  Absorbing the third
power of its constant proves



$$
c_nB_n\leq C^n.
$$



This remains true when $r_n=0$, using its reduced presentation $0/1$.
The primitive multiplier $m_n$ in $L_n=m_nJ_n(K)$ need only be a
positive rational number; no step of the target proof assumes that it is
an integer.

## 4. Full prime-power content calculation

Let the two primitive integer pairs be



$$
(-p,q),\qquad(A,\varepsilon B),
\qquad q,B>0,
$$



and set



$$
d=\gcd(q,B),\quad q=dq_0,\quad B=dB_0,
\quad\gcd(q_0,B_0)=1.
$$



The minimal positive multipliers are $B_0,q_0$, the common coefficient is



$$
C=dq_0B_0,
$$



and either sign produces



$$
M=-B_0p\pm q_0A.
$$



Let $\ell$ be a prime divisor of $q_0$.  Then $B_0$ is a unit modulo
$\ell$, and $p$ is a unit because $\gcd(p,q)=1$.  Hence



$$
M\equiv-B_0p\not\equiv0\pmod\ell.
$$



If instead $\ell\mid B_0$, then $q_0$ and $A$ are units modulo
$\ell$, giving



$$
M\equiv\pm q_0A\not\equiv0\pmod\ell.
$$



Thus



$$
\gcd(M,q_0B_0)=1.                              \tag{A10}
$$



This is stronger than a square-free argument: for every prime $\ell$
occurring in $q_0B_0$, it gives $v_\ell(M)=0$, regardless of the
exponent of $\ell$ in that product.  For primes not occurring in
$q_0B_0$,



$$
v_\ell(\gcd(M,C))\leq v_\ell(d).
$$



Consequently



$$
\gcd(M,C)\mid d
$$



for both signs, including every prime power.  The bound is sharp: for


$$
(p,q,A,B)=(-49,8,-49,72)
$$


and the plus sign, $d=8$, $M=392$, $C=72$, and
$\gcd(M,C)=8$.

An exhaustive exact-integer check over



$$
|p|,|A|\leq25,\qquad1\leq q,B\leq25,
$$



restricted to primitive input pairs and both signs, tested 1,276,802
instances and found no failure.

## 5. Both signs and constants (23)--(28)

### 5.1 Beta lower bound: (23) and (24)

The positivity hypothesis gives exactly



$$
J_n(K)\geq
 \kappa B(n+1,n+1)
 =\kappa\frac{(n!)^2}{(2n+1)!},
$$



which is target (23).  Multiplication by target (9) yields



$$
\begin{aligned}
 q_nJ_n(K)
 &\geq
 \frac{n(2n-1)!}{n!}
 \frac{\kappa(n!)^2}{(2n+1)!}\\
 &=\frac{\kappa n!}{2(2n+1)}.
 \end{aligned}
$$



The factor $2(2n+1)$ in target (24) is therefore exact.

### 5.2 Same-sign case: (25)

Put



$$
d_n=\gcd(q_n,B_n),\qquad
 u_n=B_n/d_n,\qquad v_n=q_n/d_n.
$$



When $\varepsilon_n=1$, the minimally matched value is



$$
W_n^+=u_nE_n+v_nL_n>0.
$$



Since $L_n/B_n=J_n(K)/c_n$,



$$
v_nL_n
 =\frac{q_nB_n}{d_n}\frac{J_n(K)}{c_n}
 \geq\frac{q_nJ_n(K)}{c_n}.                     \tag{A11}
$$



Lemma 3.1 bounds the final content $g_n$ by
$d_n\leq B_n$.  Therefore



$$
\frac{W_n^+}{g_n}
 \geq\frac{q_nJ_n(K)}{c_nB_n}
 \geq\frac{\kappa n!}
              {2(2n+1)c_nB_n}.
$$



This is exactly target (25), with no lost sign or multiplier.

### 5.3 Opposite-sign case: (26)--(28)

When $\varepsilon_n=-1$, subtracting $L_n$ makes the $e$- and
$\pi$-coefficients equal and positive:



$$
W_n^-=u_nE_n-v_nL_n
 =\frac{q_nB_n}{d_n}
   \left(\frac{E_n}{q_n}-\frac{J_n(K)}{c_n}\right). \tag{A12}
$$



The ratio of the two positive per-coefficient values is



$$
\frac{E_n/q_n}{J_n(K)/c_n}
 =\frac{c_nE_n}{q_nJ_n(K)}.
$$



Using target (10) in the numerator and target (24) in the denominator gives



$$
\begin{aligned}
 \frac{c_nE_n}{q_nJ_n(K)}
 &\leq
 \frac{ec_nn!}{(2n+1)!}
 \frac{2(2n+1)}{\kappa n!}\\
 &=\frac{2ec_n}{\kappa(2n)!}
  =\frac{ec_n}{\kappa n(2n-1)!}.
 \end{aligned}                                             \tag{A13}
$$



This verifies every factor in target (28).  Lemma 2.1 gives
$c_n\leq C_K^n$, so (A13) is below $1/2$ for every sufficiently large
relevant $n$.  Equation (A12) is then negative and



$$
|W_n^-|
 \geq\frac{q_nB_n}{d_n}\frac{J_n(K)}{2c_n}
 \geq\frac{q_nJ_n(K)}{2c_n}.
$$



The content is again at most $B_n$, whence



$$
\frac{|W_n^-|}{g_n}
 \geq\frac{q_nJ_n(K)}{2c_nB_n}
 \geq\frac{\kappa n!}
              {4(2n+1)c_nB_n}.
$$



This is target (26).  Finally, Corollary 2.2 reduces both signs to



$$
\frac{n!}{(2n+1)C^n}\longrightarrow\infty.
$$



Every infinite set of positive even integers is unbounded, so the same
limit holds along the possibly sparse index set in hypothesis (3).  No
density, recurrence within that set, or eventual occurrence of both signs
is assumed: each sign-specific inequality applies whenever that sign
occurs, after one common sufficiently-large threshold.

## 6. Hidden-assumption checklist

- **Uniqueness of $r+c\pi$:** valid because $1,\pi$ are
  $\mathbb Q$-linearly independent.  The fixed-basis construction makes
  this explicit.
- **Sparse indices:** harmless.  Uniform exponential heights hold for every
  $n$, and factorial growth dominates on every unbounded subsequence.
- **Rational-function poles:** resolved in the frozen checkpoint by choosing
  coprime $P,Q$; this makes $Q$ zero-free on the integration interval.
- **Coefficient normalization:** the input pairs are primitive, the
  coefficient-matching multipliers $B/d,q/d$ are minimal, and the last
  content is exactly a divisor of $d$, not an uncontrolled gcd.
- **Prime powers:** fully covered by (A10); reduction modulo the underlying
  prime makes $M$ a unit, so no power from $q_0B_0$ enters the content.
- **Sign changes:** the target does not assume that one sign occurs
  eventually.  It gives a same-sign bound whenever $\varepsilon_n=1$ and
  an opposite-sign bound for every sufficiently large index with
  $\varepsilon_n=-1$.
- **Zero coefficients:** $c_n>0$ guarantees $B_n>0$, while positivity of
  $J_n(K)$ prevents the normalized pair from being zero.
- **Dependence of constants:** all constants in Lemma 2.1 depend only on the
  single fixed kernel $K$; no $n$-dependent denominator, basis, or
  coordinate matrix is introduced.

## 7. Markup and byte validation

The frozen target passed all of the following checks:

- valid UTF-8;
- no NUL byte, carriage return, or C0 control byte other than line feed;
- 34 opening and 34 closing display-math delimiters;
- 109 opening and 109 closing inline-math delimiters;
- equation tags $1,2,\ldots,28$, each occurring exactly once;
- no trailing whitespace;
- one level-one Markdown title;
- no unfinished code fence, dollar-delimited display, or unfinished-work
  marker.

The final target checkpoint is 10,232 bytes and has the SHA-256 digest
recorded at the beginning of this audit.

## Conclusion

After the two explicitly documented corrections, the fixed-rational-kernel
barrier is rigorous for its stated scope.  The essential arithmetic fact is
that a fixed rational denominator creates only exponential height, while
the symmetric beta comparison contributes factorial growth.  The exact
prime-power content lemma prevents final primitive reduction from absorbing
that growth, and the factorial separation also forces the nominally
cancellative opposite-sign form to have a fixed sign and diverging
magnitude.
