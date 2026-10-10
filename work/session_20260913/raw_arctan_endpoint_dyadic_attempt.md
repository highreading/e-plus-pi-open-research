> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact dyadic valuation of the primitive raw-arctangent endpoint

Date: 2026-09-13. This proves the all-degree formula previously observed
only through n=30 in `sources/raw_arctan_endpoint_arithmetic.md`.
The result concerns the actual reduced endpoint denominator. It also
proves that at most one evaluated remainder can vanish, by distinguishing
all of the rational endpoint approximants. It does not prove smallness.

## 1. Result and precise normalization

Use the canonical raw family



$$
A+Be^z+C\arctan z=O(z^{3n+1}),\qquad
 \deg A,\deg B,\deg C\le n,\qquad C(1)=4B(1).
\tag{1}
$$



The archive proves uniqueness and B(1) nonzero in every degree. Let q_n be
the reduced positive denominator of A(1)/B(1), so that the primitive
endpoint form is p_n+q_n(e+pi). Define



$$
\phi(k)=v_2(k!),\qquad S(q)=\sum_{j=0}^{q-1}\phi(j).
\tag{2}
$$



Let Delta_A and Delta_B be exactly the integer augmented determinants
defined in the canonical arithmetic note: Delta_A appends the row n!A(1),
while Delta_B appends B(1), to its integer high-jet matrix.
Then for every n>=0,



$$
\boxed{v_2(\Delta_{A,n})
 =\phi(n)+\sum_{k=n+1}^{2n}\phi(k)+3S(n)-n,}
\tag{3}
$$



and consequently



$$
\boxed{v_2(q_n)=n+2\left\lfloor\frac{n+2}{4}\right\rfloor.}
\tag{4}
$$



In particular Delta_A and A(1) are nonzero in every degree, and
q_n>=2^{3n/2+O(1)}. The result keeps the endpoint gcd: it is not merely a
divisor of an unnormalized polynomial triple or cofactor.

The n=0 case is immediate from (A,B,C)=(-1,1,4), so assume n>=1 below.

## 2. The actual coefficient matrix and a dyadic moment lemma

For integer k, put



$$
f_k=\begin{cases}1/k!&k\ge0,\\0&k<0,\end{cases}
 \qquad
 t_k=\begin{cases}(-1)^{(k-1)/2}/k&k>0\text{ odd},\\0&\text{otherwise}.
 \end{cases}
$$



Divide the high jet rows by k! and the appended A row by n!. The resulting
square coefficient matrix, denoted M_A, has columns B_j,C_j, j=0,...,n.
Its 2n high rows, indexed by k=n+1,...,3n, are



$$
(f_{k-j}\mid t_{k-j}).
\tag{5}
$$



The last two rows are the actual endpoint rows



$$
(-4,\ldots,-4\mid1,\ldots,1),
 \qquad
 (-E_{n-j}\mid-T_{n-j}),
\tag{6}
$$



where E_a=sum_(r=0)^a1/r! and T_a=sum_(r=1)^a t_r. Thus exactly



$$
v_2(\Delta_A)=\phi(n)+\sum_{k=n+1}^{3n}\phi(k)+v_2(\det M_A).
\tag{7}
$$



Introduce the raw arctangent moment functional



$$
\mathcal L(t^a)=t_{a+1},\qquad
 \mathcal L(P)=\frac12\int_{-1}^1P(iu)\,du.
\tag{8}
$$



Every moment is dyadically integral. Its monic orthogonal polynomials are



$$
Q_j(t)=\frac{2^ji^j}{\binom{2j}{j}}P_j(-it),\qquad
 Q_{j+1}=tQ_j+\frac{j^2}{4j^2-1}Q_{j-1}.
\tag{9}
$$



The recurrence proves Q_j belongs to Z_(2)[t], where Z_(2) is the ring of
rationals with odd denominator. Their exact norms are



$$
h_j=\mathcal L(Q_j^2)
  =\frac{(-1)^j2^{2j}}{(2j+1)\binom{2j}{j}^2},
 \qquad v_2(h_j)=2\phi(j).
\tag{10}
$$



The latter equality follows from v_2(binom(2j,j))=s_2(j) and
phi(j)=j-s_2(j).

Here are the moment determinant consequences used below.

* For arbitrary F_i in Z_(2)[t], the determinant with n columns
  L(F_i t^j), j=0,...,n-1, has valuation at least 2S(n). Change the columns
  to the monic integral basis Q_j and expand each F_i in that same basis.
  Orthogonality factors h_j from column j, leaving a matrix over Z_(2).

* For n moment rows and one arbitrary Z_(2)-valued linear functional on
  polynomials of degree at most n, the determinant with n+1 columns
  t^0,...,t^n has valuation at least 2S(n). After the same column change,
  expand along the last row. Each term contains n of h_0,...,h_n, whose
  valuation is at least the sum for h_0,...,h_(n-1), because phi(j) is
  nondecreasing.

* A square (n+1)-by-(n+1) matrix consisting entirely of moment rows has
  valuation at least 2S(n+1).

These are divisibility statements in Z_(2), so cancellation between terms
can only raise their lower bounds. All changes of polynomial basis used
here are unitriangular over Z_(2).

## 3. The arctangent block with both endpoint rows

Reverse the C columns, identifying column j with t^j for j=0,...,n.
The high row at k is then the moment functional



$$
P\longmapsto\mathcal L(t^{k-n-1}P).
\tag{11}
$$



The C endpoint row is evaluation at1. The C part of the A endpoint row is
the integral functional D defined by



$$
D(t^j)=-T_j=-\sum_{a=0}^{j-1}\mathcal L(t^a).
\tag{12}
$$



In particular, D takes Z_(2)[t] to Z_(2), and



$$
D((t-1)t^j)=-\mathcal L(t^j).
\tag{13}
$$



Consider any arctangent minor containing both endpoint rows and n-1 high
rows. Change its column basis to



$$
1,\ (t-1),\ t(t-1),\ldots,t^{n-1}(t-1).
$$



This is an integral unimodular change. The evaluation-at1 row now removes
the first column. By (11)–(13), the remaining n-by-n determinant consists
of moment rows L(F_i t^j), j=0,...,n-1, with



$$
F_0=-1,\qquad F_i=t^{k_i-n-1}(t-1).
\tag{14}
$$



Its valuation is therefore at least 2S(n). When the retained high rows
are exactly



$$
U_0=\{n+1,n+2,\ldots,2n-1\},
\tag{15}
$$



the polynomials in (14) are, up to a sign, 1,(t-1),t(t-1),...,t^(n-2)(t-1).
They form an integral unimodular basis of degree at most n-1. This makes
the determinant equal up to sign to the ordinary moment Gram determinant.
Consequently its valuation is exactly 2S(n).

If an arctangent minor has only one endpoint row, its valuation is at
least 2S(n), by the second moment bound in Section2: both evaluation at1
and D are integral on the monic Q_j basis. If it has neither endpoint row,
its valuation is at least 2S(n+1).

## 4. The exponential minors and all four row assignments

Expand det M_A along its n+1 exponential columns. A high exponential row
at k is evaluation at k in the falling-factorial basis (x)_j, divided by
k!, because f_(k-j)=(k)_j/k! even when j>k.

For distinct integer nodes x_1,...,x_r, the standard integral alternant
bound is



$$
v_2\!\left(\prod_{i<j}(x_j-x_i)\right)\ge S(r).
\tag{16}
$$



Indeed division by product_(j=0)^(r-1) j! gives the determinant of the
integer binomial-evaluation matrix. Equality holds at consecutive nodes.

The exponential part of the endpoint border is -4 times the integral
functional Lambda with Lambda((x)_j)=1. The exponential part of the
A endpoint row, ignoring its harmless sign, is



$$
\rho((x)_j)=E_{n-j}
  =\sum_{k=0}^n\frac{(k)_j}{k!}.
\tag{17}
$$



Thus rho is a sum of ordinary evaluations at low nodes, with denominators
k!, k<=n. An alternant with r ordinary evaluation rows and the row Lambda
equals, up to sign, V(nodes) Lambda(product(x-node)). The final Lambda
factor is integral because falling-factorial change-of-basis coefficients
are integers. This is the same alternant identity used in the archived
rank proof.

Put



$$
H_r=\sum_{k=3n-r+1}^{3n}\phi(k),\qquad H_0=0.
\tag{18}
$$



This is an upper bound for the factorial valuation sum of any r high rows.
Since phi(2n)=phi(2n+1)=phi(n)+n, define the candidate minimal valuation



$$
V_* = S(n+1)-H_{n+1}+2S(n)
      =3S(n)-n-H_n.
\tag{19}
$$



There are exactly four types of Laplace term, according to which of the
two endpoint rows is assigned to the exponential block.

1. **Neither endpoint row is assigned to the exponential block.**
   This block has n+1 high evaluation rows, so its valuation is at least
   S(n+1)-H_(n+1). The arctangent block has both endpoints and has valuation
   at least 2S(n). Thus the total is at least V_*.

2. **Only the A endpoint row is assigned to the exponential block.**
   Expand rho using (17). There are n high nodes and one distinct low
   node k<=n. Equation (16) bounds the exponential determinant below by
   S(n+1)-H_n-phi(n)=S(n)-H_n. The arctangent block has one endpoint, so
   the total is at least 3S(n)-H_n=V_*+n.

3. **Only the border row is assigned to the exponential block.**
   The integral Lambda alternant, the n high nodes, and the factor4 give
   the exponential lower bound 2+S(n)-H_n. The arctangent bound is again
   2S(n), so the total is at least V_*+n+2.

4. **Both endpoint rows are assigned to the exponential block.**
   Expand rho into its low nodes. Together with the n-1 high nodes, the
   resulting n evaluation nodes are distinct. Apply the Lambda alternant
   and (16). The exponential lower bound is
   2+S(n)-H_(n-1)-phi(n). The arctangent block is entirely moment rows and
   has bound 2S(n+1). Their sum exceeds V_* by
   2+2phi(2n)>0.

All these lower bounds apply also when a minor is zero; cancellation
within rho or a minor cannot lower a valuation.

## 5. The unique least term and the primitive conclusion

In the first case, choose the exponential rows



$$
S_0=\{2n,2n+1,\ldots,3n\}.
\tag{20}
$$



Their Vandermonde attains (16), and the complementary arctangent rows are
exactly (15), whose minor attains 2S(n). This Laplace term has valuation
V_*.

It is the unique term with that valuation. The set S_0 is the unique
(n+1)-element set of high rows maximizing the sum of phi(k): its lowest
node is even, and phi(2n)>phi(2n-1). Any different set loses at least one
in that sum. Neither its exponential Vandermonde nor its arctangent minor
can fall below the global bounds used in the first case. The other three
cases have the strictly positive gaps just proved.

A sum of dyadic rationals with a unique summand of least valuation is
nonzero and has that valuation. Therefore



$$
v_2(\det M_A)=3S(n)-n-\sum_{k=2n+1}^{3n}\phi(k).
\tag{21}
$$



Substitution in (7) proves the exact new determinant formula (3).

To obtain the actual reduced denominator, use the canonical cofactor
identity, which already includes the endpoint gcd:



$$
v_2(q_n)=\max\{0,\phi(n)+v_2(\Delta_B)-v_2(\Delta_A)\}.
\tag{22}
$$



The archived exact valuation of Delta_B is



$$
v_2(\Delta_B)=\sum_{k=n+1}^{2n}\phi(k)+S(n)+L_n,
$$



where, with g(r)=r(r-1)/2+S(r) and
beta(r+1)=g(r)+r+1_(r odd),



$$
L_{2r}=3g(r)+\beta(r+1),\qquad
 L_{2r+1}=2g(r+1)+g(r)+\beta(r+1).
\tag{23}
$$



The elementary relations



$$
S(2r)=2g(r),\qquad
 S(2r+1)=2g(r)+r+\phi(r),\quad
 g(r+1)=g(r)+r+\phi(r)
$$



give



$$
L_n-2S(n)=2\left\lfloor\frac{n+2}{4}\right\rfloor.
\tag{24}
$$



Combining (3), (22), and (24) yields (4). Its right side is positive for
n>=1, so the maximum in (22) does not obscure any cancellation.

## 6. Distinct endpoint rationals and automatic eventual nonvanishing

The integer n+2floor((n+2)/4) strictly increases with n. Thus (4) proves
that the reduced denominators q_n have pairwise different dyadic
valuations. In particular the rational approximants



$$
r_n=-A_n(1)/B_n(1)
$$



are pairwise distinct. This includes n=0. For any fixed real number s,
the equality r_n=s can therefore hold at most once.

Apply this statement to s=e+pi. Since B_n(1) is nonzero,



$$
R_n(1)=0\quad\Longleftrightarrow\quad r_n=e+\pi.
$$



Consequently at most one of the raw family's evaluated endpoint forms
vanishes. All sufficiently large forms are nonzero, without an
Archimedean sign argument and without assuming irrationality. This does
not identify the possible exceptional index or rule out every individual
zero.

An unbounded subsequence of the primitive endpoint forms tending to zero
would now prove irrationality directly: all but at most one of those
forms are nonzero, while a rational target with denominator Q forces
every nonzero integer form in 1 and that target to have absolute value
at least 1/Q. The remaining requirement is actual primitive shrinkage.

## 7. Scope and the remaining research problem

This closes the specific dyadic endpoint-normalization gap identified in
the canonical raw-arctangent arithmetic note. It also proves A(1) nonzero
for every degree and eventual nonvanishing of the evaluated forms, with
at most one possible exceptional index.

The exact denominator has at least an exponential dyadic part, but its
odd-prime factors and its full size remain uncontrolled. The canonical
whole evaluated remainder is a sum of two integrals with varying
polynomial factors. An all-degree sign or asymptotic for that actual sum
would now have to be compared with (4) and any further odd-prime height
information. No conclusion about rationality or irrationality follows
from the dyadic theorem alone.

Selected exact determinant normalization checks are kept separately in
`raw_arctan_endpoint_dyadic_checks.py` and its JSON output. The proof above
does not use the finite observed pattern as a hypothesis.
