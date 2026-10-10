> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Auxiliary special gcd: analytic disks and affine first lifts

Date: 2026-09-13. Original bounded reduction by audit_sources.
Independent root review: PASS in hp_auxiliary_analytic_reduction_root_review.md,
within the explicitly conditional unit-index-slope scope. No new prime, degree, or residue scan was
performed. The result is a local theorem for the auxiliary gcd; it is
not an endpoint-gcd exclusion.

Inspected inputs:
hp_special_gcd_unit_lift.md,
hp_special_two_branch_attempt.md,
hp_two_branch_extended_audit.md, and
hp_three_state_quadratic_obstruction.md.

Write



$$
h_n=H_n(1),\qquad e_n=E_n,\qquad
 j_n=J_{n+1}(1)=(n+1)(h_{n+1}+e_{n+1}),
$$




$$
g_n=\gcd(h_n,j_n),\qquad n\ge2.
$$



The known residue-1 and residue-minus-1 formulas, and the complete
fixed-prime formulas at 3 and 5, remain unchanged. The new point is
that every possible additional joint residue admits an explicit
analytic first-lift test of degree one, under the joint-root condition.

## 1. Genuine analytic interpolation on every odd-prime disk

Fix an odd prime p. For nonnegative b,c put R=b+2c and s=b+c.
Define on X in Z_p the two series



$$
\mathcal H(X)=\sum_{b,c\ge0}
 \frac{(-1)^b}{2^c b!c!}(X)_{\underline R}(X)_{\underline s},
$$




$$
\mathcal E(X)=\sum_{b,c\ge0}
 \frac{(-1)^b}{2^c b!c!}(X-1)_{\underline R}(X)_{\underline s}.
 \tag{1}
$$



At every nonnegative integer X=n these equal the actual h_n and e_n.
For E, the differentiated coefficient formula gives the identity when
n>=1. At n=0, every term with s>0 vanishes and the value is 1=E_0.
All sums are finite at those integer arguments.

For any a in {0,...,p-1}, substitute X=a+pY. Each falling product
of length L has at least floor(L/p) factors divisible by p as a
polynomial in Y. Put q=floor(s/p) and k=floor(R/p). Since
v_p(b!c!)<=v_p(s!)=q+v_p(q!), the Gauss valuation of either term
in (1) is at least



$$
k+q-v_p(s!)=k-v_p(q!)\ge k-v_p(k!).
 \tag{2}
$$



Here the Gauss valuation is the minimum valuation of its polynomial
coefficients, not only its values on integer Y. The same argument
applies to X-1, since the residue shift does not change the lower
count floor(L/p).

For odd p, k-v_p(k!) tends to infinity. Thus both series converge
in the restricted power-series algebra Z_p<Y> on each full closed
disk a+pZ_p. This is stronger than mere continuity or congruence
preservation. It justifies termwise coefficient extraction and
differentiation in Y.

Two useful precise cutoffs follow:

- R>=p implies Gauss valuation at least 1;
- R>=2p implies Gauss valuation at least 2.

For the second statement, k>=2 and
v_p(k!)<=(k-1)/(p-1)<=(k-1)/2, so the integer in (2) is at least 2.
Consequently all calculations modulo p^2 below use only R<2p.
The terms R<p have p-unit factorial denominators, so their reduction
modulo p is independent of Y. Therefore



$$
\mathcal H(a+pY)\equiv h_a,\qquad
 \mathcal E(a+pY)\equiv e_a\pmod p
 \quad\hbox{in }\mathbb Z_p\langle Y\rangle.
 \tag{3}
$$



Define


$$
\mathcal J(X)=(X+1)(\mathcal H(X+1)+\mathcal E(X+1)).
 \tag{4}
$$


It is likewise analytic and satisfies the actual values j_n and
constant reduction j_a on each disk.

## 2. The exact quadratic coefficient of the first lift

For every a in {0,...,p-1}, there are alpha_a,beta_a in F_p with



$$
\mathcal H(a+pY)
 \equiv h_a+p\alpha_aY+p h_aY^2\pmod{p^2},
$$




$$
\mathcal E(a+pY)
 \equiv e_a+p\beta_aY+p e_aY^2\pmod{p^2}.
 \tag{5}
$$



The reductions of h_a,e_a in the quadratic terms are understood.
These congruences hold as power series, not just as functions on F_p.

First, the terms R>=2p vanish by (2). If R<2p, then c<p and
v_p(b!c!)<=1. A coefficient of Y^j in the numerator has a factor
p^j. Hence all coefficients with j>=3 vanish modulo p^2.
For a quadratic term to survive, b must be at least p.

Write b=p+B, R=p+R', s=p+s', where R'=B+2c and s'=B+c.
For H, a nonzero quadratic contribution requires R'<=a; otherwise
the two falling products together have at least three p-divisible
factors and vanish modulo p^2 after dividing by b!c!.
When R'<=a, each falling product has exactly one such factor, namely
pY. Wilson's elementary product identity gives



$$
\frac{(a+pY)_{\underline{p+\ell}}}{p}
 \equiv-Y(a)_{\underline\ell}\pmod p
 \qquad(0\le\ell\le a),
$$




$$
\frac{(p+B)!}{p}\equiv-B!\pmod p.
$$



The sign (-1)^(p+B) cancels the last minus sign. The coefficient of
pY^2 is therefore the sum



$$
\sum_{B+2c\le a}
 \frac{(-1)^B}{2^cB!c!}
 (a)_{\underline{B+2c}}(a)_{\underline{B+c}}=h_a
 \pmod p.
$$



For E and a>=1, the same argument replaces the first falling product
by (a-1+pY)_R and requires R'<=a-1. Its sum is exactly e_a.
For a=0, the only surviving quadratic contribution is B=c=0:
the two p-divisible factors are p(Y-1) and pY. This contributes
pY(Y-1), whose quadratic coefficient is 1=e_0. This completes (5)
including the zero residue.

The corresponding J congruence is



$$
\boxed{\mathcal J(a+pY)
 \equiv j_a+p\gamma_aY+p j_aY^2\pmod{p^2}.}
 \tag{6}
$$



For a<=p-2 this follows by using (5) at a+1 and multiplying by
a+1+pY. For a=p-1, formula (3) at zero instead gives directly



$$
\mathcal J(p-1+pY)\equiv2p(1+Y)\pmod{p^2}.
 \tag{7}
$$



This is compatible with (6), since j_(p-1) is divisible by p;
it also gives gamma_(p-1)=2.

All slopes in (5)--(6) have an exact finite certificate from the terms
R<2p in (1), and no prime scan is needed to define them. They are
ordinary analytic derivatives with respect to the INDEX X:



$$
\alpha_a=\mathcal H'(a)\pmod p,\qquad
 \gamma_a=\mathcal J'(a)\pmod p.
 \tag{8}
$$



They are not derivatives of H_a(x) with respect to x.

## 3. Every joint residue has affine first-lift equations

Suppose h_a=j_a=0 modulo p. The residue a=0 is impossible because
h_0=1. Put



$$
F_a(Y)=\mathcal H(a+pY)/p,\qquad
 G_a(Y)=\mathcal J(a+pY)/p.
$$



By (3), these belong to Z_p<Y>. The quadratic coefficients in
(5)--(6) disappear, giving the exact first-lift system



$$
\boxed{\overline F_a(Y)=h_a/p+\alpha_aY,\qquad
 \overline G_a(Y)=j_a/p+\gamma_aY\quad\hbox{in }\mathbb F_p[Y].}
 \tag{9}
$$



In particular, if (alpha_a,gamma_a)!=(0,0), the joint residue has
at most one lift modulo p^2. It has one precisely when



$$
\boxed{\alpha_a(j_a/p)-\gamma_a(h_a/p)=0\pmod p.}
 \tag{10}
$$



If the slope vector is zero, unequal-to-zero constant data give no
lift, while two zero constants give all p lifts at this one level.
The latter case is a genuine remaining ramification possibility;
it is not excluded here.

## 4. Exact local gcd formula at a simple index root

Assume the joint residue condition and the nonzero slope condition of
Section 3. Choose as F whichever of H,J has a unit index derivative,
and call the other function G. There is a unique



$$
\xi_a\in a+p\mathbb Z_p,\qquad F(\xi_a)=0.
$$



Indeed F(a+pY)/p has affine reduction with unit slope, so it has
one simple residue root. The usual successive linear correction
constructs a unique root in Z_p, or equivalently the elementary
Hensel argument applies directly to this restricted power series.

More explicitly, its coefficient of Y is a unit and all coefficients
of Y^j for j>=2 are divisible by p. Factoring its zero therefore gives
a quotient which is a unit at every Y in Z_p. It follows that



$$
v_p(F(n))=v_p(n-\xi_a)\qquad(n\equiv a\pmod p).
$$



The other restricted series has integral coefficients, so its difference
at two arguments is divisible by their difference. Consequently



$$
G(n)-G(\xi_a)\in(n-\xi_a)\mathbb Z_p.
$$



Taking the smaller of the two valuations proves the exact formula



$$
\boxed{\displaystyle
 v_p(g_n)=
 \min\{v_p(n-\xi_a),\Lambda_a\},\qquad
 \Lambda_a=v_p(G(\xi_a))\in\{1,2,\ldots,\infty\}.}
 \tag{11}
$$



This holds for every actual integer n>=2 in that residue disk. Values
of zero have valuation infinity. If (10) fails, Lambda_a=1.
If (10) holds, Lambda_a>=2; a unique branch persists to each precision
at most Lambda_a and stops thereafter unless Lambda_a is infinite.
The unit-slope condition gives uniqueness, not existence of a common
zero at every precision and not a bound for Lambda_a.

This includes the known branches: at a=p-1 the J slope is the unit
2 and xi_a=-1, leaving precisely the old constant C_p=H(-1).
At a=1 the known unit-8 lift fixes the joint branch and gives its
already proved valuation. No previous complete formula at 3 or 5
is weakened or replaced.

## 5. What this does and does not resolve

The inherited simple-root lemma states H_a'(1)!=0 modulo p for an
interior joint residue, with the prime differentiating in x.
It does not prove either slope in (8) is a unit. The new explicit
remaining tests are:

1. the original finite-field joint-residue exclusion;
2. if an additional joint residue exists, the index-slope vector
   (alpha_a,gamma_a);
3. if that vector is nonzero, the compatibility value G(xi_a).

The rational three-state determinant obstruction remains relevant:
an invariant required as a rational identity in formal n cannot be
a nondegenerate quadratic similitude. The analytic disk method above
does not contradict that result. It is neither such a rational
invariant nor a proof that the projective state [0:1:a] is absent.

This gives a viable uniform-in-index method at any fixed odd p once
its simple joint residues are known. It supplies an exact finite
first-lift test and a single analytic compatibility constant per simple
residue. It does not classify the residues for every p or control
the constants uniformly in p.

Most importantly, the existing implication for the actual HP endpoint
gcd is only available at p>2n+2. For any fixed p this range eventually
fails as n increases. Applying (11) uniformly in n at that fixed p
therefore does not settle the growing-prime endpoint gate, nor a
primitive denominator bound. Even a unit index slope would permit
the actual integer n to be close to xi_a and the other gate to be
compatible. An exclusion or uniform valuation estimate for those
growing primes is still required.

No new main proof, two-branch theorem, or auxiliary global odd-gcd
bound is claimed.
