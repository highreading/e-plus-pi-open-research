> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The primitive dual polynomial and an exact extremal-content factorization

Date: 2026-09-13. Original bounded arithmetic continuation by audit_results.
Independent audit: raw_extremal_dual_content_independent_review.md
passes the complete proof, including the cofactor signs and prime
localizations.

This note identifies the primitive left annihilator of the actual
extremal matrix with a polynomial having two prescribed multiple
zeros, and with a simultaneous type-II Padé denominator. It also
proves an exact integer factorization of the actual endpoint
determinant into the extremal content and one explicit scalar.

The factorization retains every prime-power exponent. It does not
prove that the extremal content has only small prime factors, or
give a recurrence for that content. Its final section isolates the
remaining arithmetic condition and a specific obstruction to using
the ordinary Legendre recurrence as an automatic large-prime proof.

## 1. Matrices, cofactor orientation and primitive polynomial

Let X_n have rows k=n,...,3n and columns
B_0,...,B_(n−1),C_0,...,C_(n−1), with integer entries



$$
(X_n)_{k,B_j}=(k)_j,\qquad
(X_n)_{k,C_j}=k!\tau_{k-j},\qquad
\tau_s=[z^s]\arctan z.
\tag{1}
$$



All subscripts k−j are positive. Its full characteristic-zero
column rank is proved in raw_high_content_extremal_valuation_bound.md.
Define its signed cofactor vector, with row positions starting at0,
by



$$
u_k=(-1)^{k-n}\det X_n[\text{all rows except }k],\quad
F_n=\gcd_{k=n}^{3n}|u_k|>0,\quad w_k=u_k/F_n.
\tag{2}
$$



Then w is an integer primitive vector, its sign fixed by (2), and
w^T X_n=0. Its rational span is the complete left nullspace.
Put



$$
W_n(z)=\sum_{k=n}^{3n}w_kz^k.
\tag{3}
$$



The exponential-column equations say exactly
W_n^(j)(1)=0 for j=0,...,n−1. Its support already supplies a zero
of order at least n at0. Hence



$$
\boxed{W_n(z)=z^n(z-1)^nV_n(z),\qquad
V_n\in\mathbb Z[z],\quad \deg V_n\le n,\quad
\operatorname{content}(V_n)=1.}
\tag{4}
$$



Polynomial division by the monic factors is integral; Gauss's
content lemma then proves primitivity because z^n(z−1)^n is
primitive. No assertion that V_n has full degree, or nonzero values
at0 or1, is made. Those would be additional normality statements.

This ordinary polynomial uses the left vector for the integer
row-scaled matrix. For the unscaled Taylor matrix the left vector
is proportional to (k!w_k). Confusing these two vectors would give
the wrong derivative and shift identities below.

## 2. A second exact representation by the raw Legendre moment functional

Define the inverse-Borel polynomial with its origin factor removed,



$$
T_n(z)=\sum_{r=0}^{2n}(n+r)!w_{n+r}z^r.
\tag{5}
$$



For the raw moment functional
L(z^a)=tau_(a+1)=(1/(2i)) integral_(-i)^i z^a dz, the arctangent
columns in (1) give precisely



$$
\boxed{L(z^sT_n(z))=0,\qquad 0\le s\le n-1.}
\tag{6}
$$



Indeed the j-th column sum is
sum_r (n+r)!w_(n+r)tau_(n+r−j)
=L(z^(n−j−1)T_n). Every exponent in this integral is nonnegative;
there is no dropped low-A-degree constraint or singular moment.

Over Q, the reviewed raw monic Legendre polynomials Q_l are an
orthogonal basis for L with nonzero norms. Therefore (6) is
equivalent to



$$
T_n\in\operatorname{span}_{\mathbb Q}\{Q_n,Q_{n+1},\ldots,Q_{2n}\}.
\tag{7}
$$



The remaining exponential equations take the form



$$
\ell_s(T_n):=\sum_{r=0}^{2n}\frac{[z^r]T_n}{(r+s)!}=0,
\qquad 1\le s\le n.
\tag{8}
$$



For a basis element, these functionals have the exact integral form



$$
\ell_s(Q_l)=\frac1{(s-1)!}
 \int_0^1(1-t)^{s-1}F_l(t)dt.
\tag{9}
$$



This follows coefficientwise from the beta integral and the actual
Borel transform F_l. Thus the dual problem is a shifted factorial
moment system on the consecutive Legendre block n,...,2n.
It is not a statement that the cofactor vector satisfies the
ordinary three-term Legendre recurrence: its coefficients are the
solution of all n additional conditions (8).

## 3. Reversal gives the simultaneous type-II denominator

Introduce an integer reciprocal polynomial



$$
\widehat Q_n(z)=\sum_{k=n}^{3n}\frac{k!}{n!}\,w_k z^{3n-k}
=\frac{z^{2n}}{n!}T_n(1/z),\qquad
Z_n=\widehat Q_n(1).
\tag{10}
$$



Every multiplier k!/n! is an integer supported on primes at most3n.
Consequently



$$
\min_jv_p([z^j]\widehat Q_n)=0\qquad(p>3n).
\tag{11}
$$



For j=0,...,n−1, the coefficient of degree 3n−j in
widehat(Q)_n exp(z) is

    (1/n!) sum_(k=n)^(3n) k!w_k/(k−j)!,

which is zero by (1). The arctangent counterpart is the same
calculation with tau_(k−j). Thus



$$
\boxed{
\begin{aligned}
\deg\widehat Q_n&\le2n,\\
[z^s](\widehat Q_ne^z)&=[z^s](\widehat Q_n\arctan z)=0,
\quad 2n+1\le s\le3n.
\end{aligned}}
\tag{12}
$$



Conversely reversing the coefficients in any solution of (12)
and undoing the nonzero factorials produces a left annihilator of
X_n. Hence the solution space of (12) is exactly one-dimensional
over Q. These are the simultaneous Padé conditions: both truncated
numerators have degree at most2n and their errors have order at
least3n+1. They are not assertions about the values e or pi.

## 4. Exact endpoint determinant factorization

Let H_n be the actual integer high matrix with rows n+1,...,3n
and B,C degrees at most n. Define the nonzero integer determinant



$$
\mathcal E_n=\det\begin{pmatrix}H_n\\ B(1)\\ C(1)\end{pmatrix},
\tag{13}
$$



where the columns have the usual order B_0,...,B_n,C_0,...,C_n.
This order of the last two rows is part of the definition. In the
archive convention appending B(1) after C(1)−4B(1), its Delta_B
is −mathcal(E)_n. Only this sign differs.

The exact identity is



$$
\boxed{\mathcal E_n=(-1)^nF_nZ_n.}
\tag{14}
$$



In particular Z_n is a nonzero integer and F_n divides the actual
endpoint determinant globally, not just at primes above3n.

Here is a proof with all row factors retained. Divide high row k
by k!, and denote the unscaled X_n by X_n^0. Let
P_n=product_(k=n)^(3n)k!. Its signed cofactor in row k is



$$
u_k^0=\frac{k!}{P_n}\,u_k.
\tag{15}
$$



In the endpoint system make the integral polynomial change of
coordinates



$$
B=(z-1)b+\beta,\qquad C=(z-1)c+\gamma,
\quad\deg b,\deg c<n,
\tag{16}
$$



using new column order b_0,...,b_(n−1),c_0,...,c_(n−1),beta,gamma.
Its determinant relative to the old coefficient columns is (−1)^n.
To check the sign, the single-polynomial basis
((z−1),z(z−1),...,z^(n−1)(z−1),1) has determinant (−1)^n;
the two such blocks have combined determinant1, and moving beta
past the n c columns adds the factor (−1)^n.

The two endpoint rows become the identity on beta,gamma. On the
remaining columns, high row k is exactly row(k−1)−row(k) of
X_n^0. Thus its square high block is D X_n^0, where D is the
2n-by-(2n+1) consecutive-difference matrix with rows e_r−e_(r+1).
For this even number of rows,

    det D[all columns except r]=(-1)^r.

Finite Cauchy–Binet therefore gives



$$
\det(DX_n^0)=\sum_{k=n}^{3n}u_k^0
=\frac{F_n}{P_n}\sum_{k=n}^{3n}k!w_k.
\tag{17}
$$



The coordinate change (16) shows that the unscaled endpoint
determinant is (−1)^n times (17). Restoring its row factors
product_(k=n+1)^(3n)k!=P_n/n! proves exactly (14).
This argument also fixes the cofactor orientation in (2).

An alternative exact expression for the scalar is



$$
\boxed{
Z_n=\frac1{n!}\int_0^\infty e^{-t}W_n(t)dt
=\frac1{n!}\int_0^\infty
e^{-t}t^n(t-1)^nV_n(t)dt.}
\tag{18}
$$



This is simply the factorial moment integral of a polynomial.
The integral converges absolutely, but its integrand is not asserted
positive. Its nonzero value follows from (14), not from a sign
assumption about V_n.

## 5. The normalized denominator is an actual type-I cross product

Let T_E=(A_E,B_E,C_E) and T_F=(A_F,B_F,C_F) be the rational
degree-at-most-n high solutions with endpoints respectively
(B_E(1),C_E(1))=(1,0) and (B_F(1),C_F(1))=(0,1). They exist
uniquely because the determinant in (13) is nonzero. Their
remainders have order at least3n+1.

Their polynomial cross product is



$$
S_0=B_EC_F-C_EB_F,\qquad
S_1=C_EA_F-A_EC_F,\qquad
S_2=A_EB_F-B_EA_F.
\tag{19}
$$



Substituting A_E=−B_Ee^z−C_E arctan(z)+O(z^(3n+1)), and the
same identity for F, gives



$$
S_1-S_0e^z=O(z^{3n+1}),\qquad
S_2-S_0\arctan z=O(z^{3n+1}).
\tag{20}
$$



All three polynomials have degree at most2n, and S_0(1)=1.
Thus S_0 is a nonzero solution of (12). One-dimensionality and
(14) imply the exact identification



$$
\boxed{S_0(z)=\widehat Q_n(z)/Z_n.}
\tag{21}
$$



One may equivalently use the existing canonical solution with
endpoints (1,4) instead of T_E, since it is T_E+4T_F and the
same cross product with T_F is unchanged. This relates the dual
object to the actual type-I family rather than to an arbitrary
solution of a differential equation.

## 6. A new exact large-prime ledger and its missing scalar gate

Let d_n^II be the least positive integer making every coefficient
of S_0 in (21) integral. If c_n^Q is the integer coefficient content
of widehat(Q)_n, elementary reduction gives



$$
d_n^{II}=\frac{|Z_n|}{c_n^Q}.
\tag{22}
$$



By (11), c_n^Q has no prime factor above3n. Hence for every p>3n,



$$
\boxed{
v_p(d_n^{II})=v_p(Z_n),\qquad
v_p(\mathcal E_n)=v_p(F_n)+v_p(d_n^{II})
=v_p(\theta_n)+v_p(d_n^{II}).}
\tag{23}
$$



Here c_n^Q divides Z_n because Z_n is the sum of the integer
coefficients of widehat(Q)_n. The last equality in (23) uses the
reviewed finite-difference Smith
equivalence between F_n and theta_n at these primes. This gives
an exact complement to the root theorem
v_p(eta_n)<=v_p(theta_n), including all prime-power multiplicities.

Consequently the sufficient saturation target for the original
unbordered high matrix can now be stated as the concrete scalar
condition



$$
v_p(Z_n)=v_p(\mathcal E_n)\quad\text{for every }p>3n,
\tag{24}
$$



or equivalently that the normalized simultaneous denominator
S_0 has exactly those large-prime denominator exponents of the
endpoint determinant. Neither (18) nor (21) proves (24). The
condition concerns the extremal matrix and remains stronger than
merely excluding a rank defect of H_n.

## 7. Exact normalization controls from the already known smallest cases

For n=1, (1) has rows (1,1),(1,0),(1,−2). Its signed cofactor
vector is (−2,3,−1), F_1=1, and

    V_1(z)=2−z,
    Qhat_1(z)=−2z²+6z−6,
    Z_1=−2,
    E_1=2=(-1)^1 F_1 Z_1,
    S_0(z)=z²−3z+3.

For n=2, the five already recorded minors in
raw_extremal_no_accessory_compatibility.md give

    F_2=4,  w=(940,−1944,1117,−162,49),
    V_2(z)=49z²−64z+940,
    Qhat_2(z)=17640−9720z+13404z²−5832z³+940z⁴,
    Z_2=16432,  E_2=65728=4 Z_2.

These values satisfy both exponential and arctangent columns
directly. The Qhat_2 coefficient content is4, so d_2^II=4108.
The large primes13 and79 of E_2 occur in that simultaneous
denominator, whereas F_2=4 has neither. This is a normalization
check using existing degrees, not an extrapolation or new scan.

## 8. Why a scalar orthogonal recurrence has not yet closed the gate

The dual construction does not identify V_n, T_n or S_0 with a
single ordinary Legendre polynomial. In (7) there are n+1 Legendre
coordinates, determined by the additional n shifted-factorial
conditions (8). Their cofactors remain determinants of that whole
system. The three-term recurrence for Q_l acts on its basis entries;
it does not supply a recurrence for these cofactor coordinates or
their common content when n changes.

There is also a precise localization issue. The monic Legendre
basis through degree2n has recurrence coefficients
l²/(4l²−1). Its construction can involve denominator primes
up to4n−1, while the associated norms can involve primes up
to4n+1, including the very range p>3n under
investigation. Thus the rational basis change in (7) is not
automatically unimodular at every p>3n. The polynomial moment
identities (6) remain valid at that prime threshold, but invoking
the ordinary monic recurrence as though all its outer coefficients
were products of units there would lose actual primes. This is
why (7) has explicitly been used over Q.

A useful next step is therefore an integral determinant or
contiguous relation for the combined shifted-factorial system
(7)–(9), or an arithmetic evaluation of the scalar (18), with
all multipliers localized only at primes<=3n. No such relation
has been proved in this bounded task. The new output is the exact
primitive dual object, the simultaneous type-II identification,
and the content factorization (14), (23), rather than a claimed
large-prime valuation bound.
