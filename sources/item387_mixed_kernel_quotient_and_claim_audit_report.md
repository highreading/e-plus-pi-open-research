> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 387 — exact mixed-kernel quotient and audit of the 2026 claimed proof

Date: 2026-09-01

## 1. Outcome first

Two recent preprints must be separated sharply.

* [Yu, arXiv:2606.17303](https://arxiv.org/abs/2606.17303) explicitly says
  that the irrationality of $e+\pi$ remains open and introduces the exact
  mixed identity

  

$$
\int_0^1\left(P(x)e^x+{4A(P)\over1+x^2}\right)dx
  =A(P)(e+\pi)-S_P(0),                         \tag{1.1}
$$



  where

  

$$
S_P=\sum_{j\geq0}(-1)^jP^{(j)},\qquad A(P)=S_P(1).   \tag{1.2}
$$



* [Carella, arXiv:2007.15000v3](https://arxiv.org/abs/2007.15000)
  claims that $1,e,\pi$ are linearly independent.  That argument is not a
  proof: its decisive nonvanishing lemma is the desired conclusion in
  disguise, and under the contradiction hypothesis the sine value declared
  nonzero is identically zero.

This item proves a global structural theorem for (1.1): the map from integer
polynomials to integer linear forms is already onto in degree one, and every
higher-degree freedom is an exact derivative with zero integral.  Thus the
unrestricted mixed-polynomial construction is a repackaging of the full
integer approximation lattice, not a generator of new arithmetic
restrictions.

This is a genuine all-degree no-go for the *bare identity*.  It does not rule
out a separately defined polynomial family whose coefficients, signs, or
norms force smallness and nonvanishing without using a prior approximation to
$e+\pi$.

No irrationality proof, Route-1 rate, or capacity reduction is obtained.

---

## 2. The exact quotient theorem

Write $D=d/dx$ and define



$$
U(P)=S_P=\sum_{j=0}^{\deg P}(-D)^jP,
\qquad P\in\mathbb Z[x].                         \tag{2.1}
$$



### Theorem 2.1 (integral automorphism)

The map $U:\mathbb Z[x]\to\mathbb Z[x]$ is a $\mathbb Z$-module
automorphism with inverse



$$
U^{-1}(S)=(1+D)S=S+S'.                           \tag{2.2}
$$



Indeed, if $d=\deg P$, then



$$
(1+D)\sum_{j=0}^{d}(-D)^jP=P+(-1)^dD^{d+1}P=P.  \tag{2.3}
$$



### Theorem 2.2 (degree-one section and exact kernel)

Define the endpoint map



$$
E(P)=\bigl(S_P(1),S_P(0)\bigr)\in\mathbb Z^2.   \tag{2.4}
$$



Then $E$ is surjective.  For every $(A,C)\in\mathbb Z^2$, the
degree-one polynomial



$$
P_{A,C}(x)=A+(A-C)x                              \tag{2.5}
$$



satisfies



$$
S_{P_{A,C}}(x)=C+(A-C)x,qquad E(P_{A,C})=(A,C). \tag{2.6}
$$



Moreover,



$$
\ker E=(1+D)\bigl(x(x-1)\mathbb Z[x]\bigr).     \tag{2.7}
$$



Consequently every $P\in\mathbb Z[x]$ has a unique decomposition



$$
P=P_{A,C}+(1+D)\bigl(x(x-1)R(x)\bigr),
\qquad A=S_P(1),\ C=S_P(0),\ R\in\mathbb Z[x].  \tag{2.8}
$$



The proof of (2.7) is exact over $\mathbb Z$: under the automorphism
$U$, the kernel is the set of $S\in\mathbb Z[x]$ vanishing at both
0 and 1, hence exactly $x(x-1)\mathbb Z[x]$.  Both factors are monic, so
no denominator or content issue occurs.

It follows that



$$
\boxed{\mathbb Z[x]/\ker E\cong\mathbb Z^2}      \tag{2.9}
$$



and degree one already represents every quotient class.

---

## 3. Exact-derivative interpretation

Since $P=S_P+S_P'$,



$$
P(x)e^x={d\over dx}\bigl(e^xS_P(x)\bigr).       \tag{3.1}
$$



Therefore



$$
\int_0^1P(x)e^x\,dx=eS_P(1)-S_P(0)=eA-C.        \tag{3.2}
$$



The second term in (1.1) contributes



$$
4A\int_0^1{dx\over1+x^2}=A\pi.                  \tag{3.3}
$$



For a kernel element



$$
P_R=(1+D)\bigl(x(x-1)R\bigr),                   \tag{3.4}
$$



one has



$$
P_Re^x={d\over dx}\bigl(e^xx(x-1)R(x)\bigr),
\qquad \int_0^1P_Re^x\,dx=0.                    \tag{3.5}
$$



Thus all higher-degree freedom in (2.8) is a zero-endpoint exact-derivative
gauge.  It can reshape the pointwise integrand but cannot change the integer
linear form $A(e+\pi)-C$.

### Corollary 3.1 (certificate equivalence)

The following are equivalent.

1. There exist $P_n\in\mathbb Z[x]$ for which the mixed integrals in
   (1.1) are nonzero and tend to zero.
2. There exist $(A_n,C_n)\in\mathbb Z^2$ for which
   $A_n(e+\pi)-C_n\ne0$ and tends to zero.
3. The number $e+\pi$ is irrational.

The equivalence of (1) and (2) follows from the quotient theorem and its
degree-one section.  The equivalence of (2) and (3) is the standard integer
linear-form criterion: rationality gives a fixed positive lower bound for
nonzero forms, while Dirichlet approximation supplies such forms for every
irrational real number.

Hence the unrestricted polynomial identity is an exact reformulation of the
problem.  To become a proof mechanism, an additional family theorem must
select $(A_n,C_n)$ independently and prove both nonvanishing and decay
after all arithmetic normalization.

---

## 4. Audit of the claimed linear-independence proof

In Section 9 of arXiv:2007.15000v3, the contradiction hypothesis is



$$
A+Be+C\pi=0.                                     \tag{4.1}
$$



The paper rewrites this as



$$
-2\pi C=2(Be+A)                                  \tag{4.2}
$$



and evaluates a Cesaro exponential average at both equal arguments.  It
correctly obtains 1 on the left.  On the right it invokes Lemma 7.2 to assert



$$
\sin(Be+A)\ne0,                                  \tag{4.3}
$$



and hence claims that the average is 0.  But (4.1) gives immediately



$$
Be+A=-C\pi,qquad \sin(Be+A)=\sin(-C\pi)=0.      \tag{4.4}
$$



So the right average is also 1.  There is no contradiction.

The dependence is circular, not merely a missing estimate.  Lemma 7.2,
case 3, invokes Lemma 6.2(ii), whose assertion is



$$
ke+m\ne r\pi\quad(k,m\ne0),                     \tag{4.5}
$$



which is precisely the relevant three-term linear-independence statement.
It cannot be used to prove that same statement.

There are also independent invalid steps in the attempted proof of Lemma
6.2.  Its equation (6.7) uses the purported general inequality



$$
|x+m-a|\ge\bigl||x-m|-a\bigr|,                   \tag{4.6}
$$



which is false.  With $x=e$, $m=1$, and $a=3\pi/2$, elementary
rational bounds $2.718<e<2.719$ and
$3.141<\pi<3.142$ give



$$
|e+1-3\pi/2|<1,qquad
\bigl||e-1|-3\pi/2\bigr|>2.9.                   \tag{4.7}
$$



The subsequent assertion $|u-v|\ge u$ for positive quantities is likewise
false without an additional separation hypothesis.  Finally, Lemma 6.1
infers $ek\ne m\pi$ for all $k,m$ from the much weaker observation that
$e\ne n\pi$ for integer $n$; that inference is invalid.

Therefore arXiv:2007.15000v3 does not establish the irrationality of
$e+\pi$.

---

## 5. Side audit of the claimed product theorem

[Carella, arXiv:1706.08394v7](https://arxiv.org/abs/1706.08394) claims that
$e\pi$ is irrational by synchronizing convergent denominators of $e$
and $\pi$.  Its main proof chooses a denominator $v_{m_k}$ in a fixed
multiplicative window around
$(2k)^{1-\varepsilon}q_{3k-2}$.  No known theorem guarantees that the
continued-fraction denominators of $\pi$ hit all such windows.

The supporting Lemma 3.1 is conditional on unproved growth assumptions for
the partial quotients of $\pi$, then assumes that
$b_{m_k}\asymp m_k^{1-\delta}$ follows from $b_m=o(m)$, which is false
(a bounded sequence is already a counterexample to that implication).  It
also promotes one window hit to infinitely many by writing multiplicative
relations between unrelated continuants that do not follow from the
continued-fraction recurrence.  The synchronization step is therefore
unproved, and this paper supplies no theorem about $e+\pi$.

---

## 6. Ledger and route consequence

* The 2026 claimed direct proof is rejected for an exact circularity and
  explicit invalid inequalities.
* The mixed-polynomial identity is globally classified at all degrees.
  Its bare higher-degree search space is one degree-one quotient plus an
  exact zero-integral gauge.
* This closes unrestricted degree escalation as an independent arithmetic
  mechanism.  It does not close structured mixed Pade, sign-constrained,
  Rodrigues, or other families with genuinely new coefficient theorems.
* No Route-1 booked factor, ceiling, or deficit changes.
* Route 1 remains `ACTIVE`; Route 2 remains `QUEUED` under the existing
  requirement that Route 1 first succeed or be closed within its declared
  architecture.
* Every conclusion about the irrationality of $e+\pi$ remains `OPEN`.

The certificate performs exact coefficient-ring checks of Theorems 2.1 and
2.2 through degree eight and records the rigorous rational interval
counterexample to (4.6).  Those finite checks are controls only; the proofs
above are symbolic and all-degree.
