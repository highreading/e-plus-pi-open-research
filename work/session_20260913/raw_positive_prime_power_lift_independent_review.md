> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the full positive-residue prime-power lift

Date: 2026-09-13. Reviewer: audit_sources.

**FULL PASS.** Every section of
raw_positive_residue_full_prime_power_lift.md is correct. The proof
retains the entire modulus $T=p^\nu$ through the same-size Schur
comparison, the weighted binomial interpolation, the primitive
coefficient transfer, and the actual endpoint reduction. No correction
is required.

The review independently derived the weighted-precision and operator
steps, rather than inferring a lift from the already reviewed mod-$p$
theorem. The two requested exceptional seed depths were then computed
from the independently reconstructed finite atlas, without new degrees
or factorization. Their exact certificate is
positive_exceptional_seed_depths.json.

## 1. Ordinary Appell and same-size inflation modulo T

For $L\equiv\ell\pmod T$, $0\le\ell<p$, every nonzero term
with $2h>\ell$ in


$$
\mathcal A_L^{[b]}(x)=
 \sum_h\binom bh(L)_{\underline{2h}}x^{L-2h}
$$


contains $L-\ell$, hence a factor $T$. If $L=\ell$, such
falling factorials are instead zero, so the same conclusion holds.
For $2h\le\ell$, $h!$ is a $p$-unit and the binomial and
falling factorial reduce at the full precision $T$. This proves


$$
\mathcal A_L^{[b]}(x)\equiv
 x^{L-\ell}\mathcal A_\ell^{[c]}(x)\pmod T
 \quad(b\equiv c\pmod T).
$$


All coefficients being reduced are already integers.

The full and cofactor content counts in the prime-level proof use
uniform residue blocks and remain valid with modulus $T$. The
comparison partitions still have exactly the original large size.
Their low Appell degrees are at most $2k<p$, and the enlarged
degree changes by a multiple of $T$. Both Vandermondes are units
in $\mathbb Z_{(p)}$ and are congruent modulo $T$.
Every positive derivative of $x^\Delta$, $T\mid\Delta$,
retains its factor $T$. The normalized Wronskian therefore gives
the asserted full-depth $M_D$ congruence and the cofactor congruence
when its index is one of $0,\ldots,k$ modulo $T$.
The $k=0$ single-row comparison remains valid.

Primitivity of the actual integral $b$-vector, with denominator
$M_D^{[n]}(1)$ now known to be a $p$-unit, proves that $V_n(1)$
is a unit. The same argument at the seed proves the unit property of
$V_k(1)$. Thus the later scalar $c=V_n(1)/V_k(1)$ is a unit
before it is used in any polynomial congruence.

## 2. The binomial-loss interpolation is valid at every index

The interpolant $F$ has degree at most $k$ and coefficients in
$\mathbb Z_{(p)}$, because its Lagrange denominators are products
of nonzero differences of integers in $[0,k]$, all below $p$.
For $j\le k$, the desired weighted cofactor congruence is direct.

For $j>k$, the exact rational identity


$$
\binom nj=
 \frac{(n)_{\underline{k+1}}}{(j)_{\underline{k+1}}}
 \binom{n-k-1}{j-k-1}
$$


has no zero denominator, and its final binomial is an integer.
The numerator falling factorial contains $n-k$; its valuation
is at least $\nu$, possibly larger. If
$u=v_p\binom nj<\nu$, it follows that


$$
v_p((j)_{\underline{k+1}})\ge\nu-u.
$$


At most one factor $j-a$, $0\le a\le k<p$, is divisible by
$p$. Hence $j\equiv a\pmod{p^{\nu-u}}$ for one such $a$.
Apply the independently established same-size cofactor comparison
with modulus $p^{\nu-u}$; its hypotheses still hold, since this
modulus is at least $p>2k$. Integrality of $F$ then gives


$$
M_j^{[n]}(1)-F(j)\equiv0\pmod{p^{\nu-u}}.
$$


Multiplication by the actual binomial recovers all $\nu$ digits.
If $u\ge\nu$, both factors in the difference are $p$-integral,
and the weighted congruence is immediate. This covers every index
through $j=n$, not merely those surviving a first Lucas digit.
The $k=0$ case uses just the positive factor $j$, with $F=1$.

## 3. Euler-operator passage to the primitive b polynomial

In the exact cofactor formula, the index is $n-\ell$ at the
coefficient of $t^\ell$. The binomial is unchanged on replacing
$\ell$ by $n-\ell$. Thus the weighted congruence yields exactly


$$
b_n(t)\equiv
 \frac{V_n(1)}{M_D^{[k]}(1)}
 F(n-t\partial_t)(t-1)^n\pmod T,
$$


including its original alternating sign.

For $G=(t-1)^{n-k}$, every positive ordinary derivative is
divisible by $T$. Consequently


$$
[t\partial_t,\operatorname{mult}_G]
=\operatorname{mult}_{tG'}
$$

 vanishes modulo $T$, and so do
the commutators of all powers and the polynomial $F$.
Replacing $n$ by $k$ inside that polynomial is valid because
its coefficients are $p$-integral. The seed expression is exact,
since $F$ agrees with all of its cofactor values. Therefore the
first asserted congruence for $b_n$ follows at full precision.
This argument does not use a nonexistent naive prime-power Lucas lift.

## 4. Integral differential operators and monic cancellation

For every positive integer $M$, the operator


$$
(1+\partial_t^2)^M-I
$$


maps $\mathbb Z[t]$ into $M\mathbb Z[t]$. Indeed, its $h$-th
term is


$$
M\binom{M-1}{h-1}\frac{\partial_t^{2h}}h.
$$


The final operator is integral: the coefficient on a monomial
is a falling factorial divisible by $(2h)!$, hence by $h$.
This is an identity of integral operators, not a division by $h$
inside a modular ring. It remains true after extending scalars to
$\mathbb Z_{(p)}$.

Taking $M=n-k$, a multiple of $T$, reduces the exponent of the
operator from $n$ to $k$. The factor
$[t(t-1)]^{n-k}$ has all positive derivatives divisible by $T$,
so it passes through the remaining operator modulo $T$.
The exact factorial-coordinate identity at the two degrees gives
the claimed congruence after multiplication by $(t-1)^n$.
Cancellation is legitimate because that polynomial is monic:
multiplication by it is injective over any coefficient ring.
The source correctly does not call $\mathbb Z/p^\nu\mathbb Z$
an integral domain.

## 5. The actual endpoint and exact loss

For $r=n-k+s$, $0\le s\le k$, every nonzero border term with
$j>k+s$ has the factor


$$
n+r-(k+s)=2(n-k),
$$


which is divisible by $T$. For $j\le k+s\le2k<p$, the
denominator $j!$ is a unit, and both factors reduce to the
small border $D_{k,s}$ modulo $T$. This proves the full-depth
endpoint transfer by an integer coefficient calculation, independently
of the interpolation argument.

If the seed numerator has finite valuation $e$ and $\nu>e$,
the unit scalar $c$ prevents cancellation of its leading $p$-adic
digit. Hence $v_p(P_{e,n}(1))=e$. Under the stated strict
factorial/arctangent gap, the actual combined numerator $N_n$
also has valuation $e$. The original denominator identity gives


$$
v_p(q_n)=v_p(Z_n)-e\ge v_p(n!)-e.
$$


The strict gap ensures $v_p(Z_n)>e$, so there is no omitted
minimum in the actual gcd calculation. The requested finite seeds
are nonzero by their explicitly verified values.

## 6. Exact new classes at eleven and thirteen

Repeated division of the independently verified seed integers gives


$$
\begin{array}{c|c|c|c|c}
 (p,k)&M_D^{[k]}(1)\bmod p&e=v_p(P_{e,k}(1))
      &(P_{e,k}(1)/p^e)\bmod p&P_{e,k}(1)\bmod p^{e+1}\\ \hline
 (11,5)&6&1&6&66\\
 (13,3)&1&2&7&1183.
 \end{array}
$$


More explicitly,


$$
P_{e,5}(1)=11\cdot420144065447348684864195768231,
$$


whose quotient is $6\bmod11$, and


$$
P_{e,3}(1)=-13^2\cdot71005967,
$$


whose quotient is $7\bmod13$. No factorization is needed.

It follows that for every positive even $n\equiv5\pmod{121}$,


$$
\boxed{v_{11}(N_n)=1,\qquad
 v_{11}(q_n)=v_{11}(Z_n)-1\ge v_{11}(n!)-1.}
$$


Its first positive even index is 126. The required factorial gap
already holds for every $n\ge33$: if $m=\lfloor n/11\rfloor\ge3$,
then $2n<22(m+1)<11^{m-1}$, yielding
$v_{11}(n!)-\lfloor\log_{11}(2n)\rfloor\ge2$.

For every positive even $n\equiv3\pmod{2197}$,


$$
\boxed{v_{13}(N_n)=2,\qquad
 v_{13}(q_n)=v_{13}(Z_n)-2\ge v_{13}(n!)-2.}
$$


Its first positive even index is 2200. The required gap already
holds for $n\ge52$: with $m=\lfloor n/13\rfloor\ge4$,
$2n<26(m+1)<13^{m-2}$, yielding a gap at least three.
Both elementary exponential inequalities hold at their indicated
initial $m$ and persist on increasing it.

These are genuine improvements on two previously exceptional
positive residue classes. They do not establish the whole classes
$n\equiv5\pmod{11}$ or $n\equiv3\pmod{13}$, and do not resolve
the singular determinant seed $p=13,k=6$. The two new classes may
be included in a simultaneous mandatory divisor with their fixed
losses one and two; their supports are disjoint from the previously
certified unit classes at the respective primes.
