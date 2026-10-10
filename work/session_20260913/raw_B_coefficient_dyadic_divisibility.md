> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# All-coefficient dyadic divisibility of the actual normalized B polynomial

Date: 2026-09-13. Original continuation by audit_results.

This note proves a simultaneous lower valuation bound for every
coefficient of the canonical B_n polynomial. It is stronger than
knowing only the leading coefficient and supplies two of the
previously missing cubic-coefficient gates. It does not prove
squarefreeness of Q or a primitive remainder estimate.

## 1. Exact statement and audited inputs

Use the actual raw HP triple with B_n(1)=1 and C_n(1)=4. Write
B_n(z)=sum_(j=0)^n B_(n,j)z^j, and phi(j)=v_2(j!). Then



$$
\boxed{v_2(B_{n,j})\ge\phi(n)-\phi(j)
\quad(0\le j\le n,\ n\ge1).}                    \tag{1}
$$



Zero coefficients are allowed and have infinite valuation.
In particular every canonical coefficient is dyadically integral.

The proof uses the actual coordinate-minor normalization and two
universal arctangent-block lower bounds already audited in
raw_leading_B_dyadic_partial.md and raw_arctan_endpoint_dyadic_attempt.md.
Put



$$
S(n)=\sum_{j=0}^{n-1}\phi(j),\quad
c_n=2\lfloor(n+2)/4\rfloor,\quad L_n=2S(n)+c_n,
$$




$$
H_n=\sum_{k=2n+1}^{3n}\phi(k),\quad
V_n=S(n)-H_n+L_n.                                 \tag{2}
$$



The required existing inputs are:

- every size-n C block with n high rows and the endpoint row of
  ones has valuation at least L_n;
- every pure C block of size n+1 has valuation at least2S(n+1);
- the actual endpoint determinant satisfies
  v_2(Delta_B)=sum_(k=n+1)^(3n)phi(k)+V_n.

The last is the all-degree formula in
sources/raw_arctan_endpoint_arithmetic.md, Theorem2.1, after its
two parity expressions for the bordered-Cauchy valuation are
simplified to L_n. No actual-coordinate determinant is replaced
by this endpoint determinant before the final cofactor quotient.

## 2. Delete an arbitrary coordinate, keeping both border assignments

Let Delta_(B,j) be the determinant obtained by appending the
coordinate row extracting B_(n,j) to the same integer matrix used
for Delta_B. Cofactor reconstruction gives exactly



$$
B_{n,j}=\Delta_{B,j}/\Delta_B.                    \tag{3}
$$



Divide the high row k by k!, then expand the appended coordinate
row. The remaining square matrix has2n high rows k=n+1,...,3n,
one endpoint row, n exponential columns indexed by
{0,...,n} minus{j}, and n+1 arctangent columns. Its entries are
the same as in the reviewed leading-B calculation:



$$
\left(\frac1{(k-d)!}\ \middle|\ t_{k-d}\right),
\qquad\text{endpoint row }(-4,\ldots,-4\mid1,\ldots,1).
\tag{4}
$$



Expand along the n exponential columns. First assign the endpoint
row to the arctangent block. For any n high row indices I, the
exponential determinant factors exactly as



$$
\frac{\prod_{0\le d\le n,\ d\ne j}d!}
     {\prod_{k\in I}k!}
\det\left(\binom{k}{d}\right)_{k\in I,d\ne j}.
\tag{5}
$$



The remaining determinant is an integer; it need not be nonzero.
Therefore its valuation is at least
S(n)+phi(n)−phi(j)−sum_(k in I)phi(k).
The factorial sum is at most H_n, and the complementary C minor
has valuation at least L_n. Every term in this border assignment
has valuation at least



$$
V_n+\phi(n)-\phi(j).                             \tag{6}
$$



Now assign the endpoint row to the exponential block. Expand that
row on its chosen column ell, which is different from j. The
factor−4 contributes valuation2. The remaining exponential
determinant has n−1 high rows and columns with j,ell omitted.
Applying the same binomial factorization gives the lower bound



$$
2+S(n)+\phi(n)-\phi(j)-\phi(\ell)-H_{n-1}
\ge2+S(n)-\phi(j)-H_{n-1},                        \tag{7}
$$



where H_(n−1) is the sum of the largest n−1 high factorial
valuations, and H_0=0 when n=1. The complementary pure C block
has size n+1 and valuation at least2S(n+1). Subtracting(6),
the resulting gap is at least



$$
\begin{aligned}
&2+H_n-H_{n-1}+2S(n+1)-L_n-\phi(n)\\
&\qquad=2+n+2\phi(n)-c_n>0.                       \tag{8}
\end{aligned}
$$



Here H_n−H_(n−1)=phi(2n+1)=n+phi(n), and
S(n+1)=S(n)+phi(n). The positivity follows from
c_n<=(n+2)/2. All expansions and estimates include zero minors
and cancellations; cancellation can only raise a lower bound.

Thus the entire reduced coordinate determinant has the bound(6).
Restore the common high-row factorials and divide by the proved
valuation of Delta_B. Equations(3) and(6) give exactly(1).
No uniqueness of a least term was required for these arbitrary
coordinate minors.

## 3. Exact reduction of B modulo2

Combine(1) with the already proved leading-coefficient valuations
in raw_all_index_cubic_gate.md. The result is



$$
\boxed{
B_n(z)\equiv
\begin{cases}
z^{n-1},&n\equiv1\pmod4,\\
z^n,&n\not\equiv1\pmod4
\end{cases}
\quad\text{in }\mathbb F_2[z].}                 \tag{9}
$$



For even n, phi(n)>phi(n−1), so(1) makes every coefficient
below the leading one even; the leading one is a unit.
For odd n>=3, phi(n)=phi(n−1)>phi(n−2), so only the coefficients
of z^n and z^(n−1) can remain. If n=3 modulo4, the former is
a unit; B_n(1)=1 forces the latter to be even. If n=1 modulo4,
the leading coefficient is even by its proved valuation, so
B_n(1)=1 forces the penultimate coefficient to be a unit.
For n=1, B_1=−7+8z gives the same conclusion.

This is a statement about the actual canonical polynomial with
B_n(1)=1, not its primitive integer multiple or an arbitrarily
rescaled monic polynomial.

## 4. Reduction of the weaker cubic triple-root gate

In the notation of raw_cubic_dyadic_squarefreeness_attempt.md,
b_0,b_1,b_2 are counted down from the leading degree n. For every
even n, b_0 is a unit and(1) proves



$$
v_2(b_1/b_0)\ge v_2(n)\ge1,
\qquad v_2(b_2/b_0)\ge v_2(n(n-1))=v_2(n)\ge1.
\tag{10}
$$



The exact cubic formulas therefore show that the two remaining
conditions



$$
\boxed{\kappa_1/\kappa_0\in2\mathbb Z_2,
\qquad \kappa_2/\kappa_0\in\mathbb Z_2^\times}
\tag{11}
$$



would imply q_2/q_3 even and q_1/q_3 a unit, excluding a triple
root by the Hessian coefficient q_2²−3q_3q_1. The conditions in(11)
have not been proved for all even n.

Equivalently, if P=D(A'C−AC')+C² and p_j=[z^(2n−j)]P,
the remaining gate is



$$
v_2(p_1)>v_2(p_0),\qquad v_2(p_2)>v_2(p_0),
\tag{12}
$$



because p_0=kappa_0, p_1=kappa_1 and
p_2=kappa_2+kappa_0. This is a concrete pair of actual leading
cross-minor divisibilities, with the B-coordinate obstruction
now removed. It remains a separate unproved arithmetic lemma;
the present coefficient theorem does not establish squarefreeness.
