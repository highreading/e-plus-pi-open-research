> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Five infinity coefficients handle every accessory degree type

Date: 2026-09-13. Root proposed the reciprocal-coordinate truncation;
this note proves its all-index form and gives the explicit fixed-size
matrices. It removes the cubic-degree assumption from the infinity
part of the degree-transfer construction. It does not assume generic
roots of Q or generic polynomial degrees.

## 1. Data and the finite defect ledger

For the actual degree-n raw family, n>=1, use the exact equation



$$
L=\sum_{j=0}^3 A_j(z)\partial_z^j,\quad
 A_3=z(1+z^2)Q,\quad q=\deg Q\in\{0,1,2,3\},
 \quad \lambda=[z^q]Q\ne0.
$$



The scalar-ODE note proves



$$
\deg(A_3,A_2,A_1,A_0)
 \le(q+3,q+3,q+2,q+1).
\tag{1}
$$



At infinity the actual solution space has one exponential germ
e^z z^b times a Laurent unit, and a two-dimensional convergent Laurent
plane with distinct highest powers c,d. One may take that plane to be
span(C_n,A_n+C_n(arctan z-F_infinity)). No selection of a particular
member as the higher-power branch is required.

Write delta_b=n-b, delta_c=n-c, delta_d=n-d. The exact Wronskian degree
ledger and the original polynomial degrees give



$$
\delta_b+\delta_c+\delta_d=4-q,\qquad
 \delta_b,\delta_c,\delta_d\ge0,\qquad\delta_c\ne\delta_d.
\tag{2}
$$



Hence delta_c,delta_d lie in {0,...,4}, and delta_b lies in {0,...,3}.
These are proven degree defects, not inferred from finite examples.

The leading equation coefficients are



$$
[z^{q+3}]A_3=\lambda,\quad [z^{q+3}]A_2=-\lambda,
$$




$$
[z^{q+2}]A_1=(c+d-1)\lambda,\quad
 [z^{q+1}]A_0=-cd\lambda.
\tag{3}
$$



Zero leading coefficients in the last two identities are allowed.

## 2. The reciprocal-coordinate Laurent operator

Put x=1/z, theta=x d/dx and y=z^n F(x). The exact derivative rule is



$$
\partial_z^j(z^nF(x))=z^{n-j}(n-\theta)_{\underline j}F(x),
\tag{4}
$$



where the subscript denotes the falling factorial polynomial. If
A_j(z)=sum_d A_(j,d) z^d, dividing Ly by z^(n+q+1) gives



$$
\boxed{\mathcal P_{\rm alg}(x,\theta)=
 \sum_{j=0}^3\sum_d A_{j,d}
      x^{q+1+j-d}(n-\theta)_{\underline j}.}
\tag{5}
$$



Every power of x is nonnegative by(1). The x powers are written to the
left of the theta polynomial, so the operator order is unambiguous.
Its constant-in-x polynomial, evaluated at theta=s, is



$$
-\lambda(n-s)(n-s-1)
 +(c+d-1)\lambda(n-s)-cd\lambda
 =-\lambda(s-\delta_c)(s-\delta_d).
\tag{6}
$$



Thus if F=sum_(r>=0)f_r x^r, its coefficient recursion is triangular.
The coefficient multiplying f_r is the nonzero-leading quadratic(6),
whose only zero indices are delta_c and delta_d, both at most4.

Define the five-by-five rational matrix M_alg by the equations through
power x^4. Explicitly, for 0<=s<=r<=4,



$$
(M_{\rm alg})_{rs}=
 \sum_{j=0}^3 A_{j,\,q+1+j-(r-s)}
                 (n-s)_{\underline j},
\tag{7}
$$



where a coefficient outside its polynomial range is zero; the entries
with s>r are zero. This matrix is computed solely from n and the bounded
accessory coefficients.

## 3. Why its kernel is exactly the actual Laurent plane

At an index other than delta_c,delta_d the triangular equation fixes
the next coefficient. At either exceptional index it can introduce at
most one free coefficient, possibly together with a compatibility
condition on earlier coefficients. Therefore the kernel of M_alg has
dimension at most2.

The two actual convergent Laurent germs, after multiplication by z^(-n),
are analytic at x=0 and have distinct leading orders delta_c,delta_d.
Both orders are at most4, so their five-coefficient vectors are linearly
independent and belong to the kernel. Consequently



$$
\boxed{\dim\ker M_{\rm alg}=2.}\tag{8}
$$



For every r>=5 the diagonal coefficient(6) is nonzero. Any vector in
this two-dimensional kernel therefore has a unique formal continuation
solving the equation. Since the actual Laurent vectors already span
the kernel, that continuation is their corresponding linear
combination and is convergent. This argument deals with the possible
low-index resonance without assuming it away or incorrectly counting
an incompatible free coefficient.

In particular, a rational basis of ker M_alg represents the entire
actual Laurent solution plane; no global connection constant is needed
to choose that basis.

## 4. The exponential branch has a one-dimensional five-jet kernel

Conjugating L by e^z gives



$$
e^{-z}Le^z=\sum_{k=0}^3\widetilde A_k(z)\partial_z^k,
 \qquad\widetilde A_k=\sum_{j=k}^3\binom jk A_j.
$$



The degree-q+3 terms cancel in tilde A_0, so
deg tilde A_0<=q+2. The other coefficients have degree at mostq+3,
and the degree-q+3 coefficient of tilde A_1 is lambda.
Since the actual exponential solution is e^z B_n with deg B_n=b,
its leading equation gives



$$
[z^{q+2}]\widetilde A_0=-b\lambda.
\tag{9}
$$



Now set y=e^z z^n G(x) and divide Ly/e^z by z^(n+q+2). The operator is



$$
\boxed{\mathcal P_{\rm exp}(x,\theta)=
 \sum_{k=0}^3\sum_d\widetilde A_{k,d}
          x^{q+2+k-d}(n-\theta)_{\underline k}.}
\tag{10}
$$



Again all powers of x are nonnegative. Its constant polynomial is



$$
\lambda(n-s)-b\lambda=\lambda(\delta_b-s).
\tag{11}
$$



The five-by-five coefficient matrix M_exp is



$$
(M_{\rm exp})_{rs}=
 \sum_{k=0}^3\widetilde A_{k,\,q+2+k-(r-s)}
                        (n-s)_{\underline k}
 \quad(0\le s\le r\le4).
\tag{12}
$$



Its triangular diagonal has exactly one zero, at delta_b<=3. Thus its
kernel has dimension at most1. The actual nonzero polynomial
x^n B_n(1/x) supplies a vector with that leading order, giving



$$
\boxed{\dim\ker M_{\rm exp}=1.}\tag{13}
$$



All later diagonal coefficients are nonzero. The five coefficients
therefore determine the whole actual exponential branch up to its
irrelevant scalar normalization. As in the Laurent case, the actual
solution proves compatibility at the possible resonance index.

## 5. Five coefficients suffice for every transfer degree test

Let



$$
S=\frac{\sum_{j=0}^2N_j(z)\partial_z^j}{Q(z)},
 \qquad\deg N_j\le6.
$$



For a Laurent input z^n F(x), write its numerator as z^(n+6) times



$$
\mathcal N_{\rm alg}F=
 \sum_{j=0}^2\sum_d N_{j,d}
          x^{6+j-d}(n-\theta)_{\underline j}F.
\tag{14}
$$



Every x power is nonnegative. Division by Q, whose leading degree is
q, gives growth at most z^(n+1) exactly when



$$
\boxed{[x^r]\mathcal N_{\rm alg}F=0,
                     \quad0\le r\le4-q.}\tag{15}
$$



These coefficients use only f_0,...,f_(4-q), hence only the first five.
Impose(15) for a rational basis of the two-dimensional kernel(8).
It then holds for every actual Laurent branch.

For the exponential input, replace N_j by
tilde N_k=sum_(j>=k)binom(j,k)N_j. The corresponding numerator is



$$
\mathcal N_{\rm exp}G=
 \sum_{k=0}^2\sum_d\widetilde N_{k,d}
       x^{6+k-d}(n-\theta)_{\underline k}G.
$$



The exponential degree condition is exactly the same coefficient
vanishing(15), applied to a basis of the one-dimensional kernel(13).
Again only five input coefficients are used.

Thus all infinity conditions are formed from two fixed five-by-five
nullspaces and at most3(5-q)<=15 linear equations on the transfer
numerators. Some equations can be identically zero or dependent; no
rank beyond the required actual degree tests is asserted. In the
generic cubic case with the sharper bound deg N_0<=5, they reduce to
the three explicit equations already proved in the generic-update note.

## 6. Scope in the unconditional finite-state construction

The two five-jet kernels and their transfer tests are valid for every
q=0,1,2,3 and every actual degree defect allowed by(2). They do not
require squarefreeness of Q, do not require Q to avoid0 or ±i, and do
not require selecting the polynomial C_n out of the Laurent plane.

Once finite local cancellation conditions have separately ensured that
the transferred expressions Ahat,Bhat,Chat are polynomials, these
infinity tests are necessary and sufficient for all three degrees to
be at most n+1. Indeed they control the whole Laurent plane and the
exponential branch; subtracting Chat(arctan z-F_infinity), which has
one lower power, gives the Ahat degree bound exactly as in the generic
global-sufficiency proof.

This closes the exceptional infinity degree types. It does not by
itself remove exceptional finite poles, prove asymptotic stability of
the resulting rational update, or bound the primitive endpoint forms.

## 7. Exact controls

`check_raw_infinity_five_jets.py` constructs the scalar coefficients
from the actual normalized triples at the preselected degrees n=1,3.
Both algebraic5-by5 matrices have rank3 and contain exactly the actual
two Laurent jets; both exponential matrices have rank4 and contain
the actual exponential jet. Direct conjugation of a trial Laurent
polynomial independently checks both matrix formulas.

The checker also verifies the two leading-polynomial factorizations
symbolically in n,b,c,d and the nonzero leading coefficient. Separate
exact germ-versus-truncation comparisons test the transfer cutoff for
each q=0,1,2,3. Those cutoff examples are controls of the differential
identity, not examples of canonical raw triples with exceptional q.
All checks pass in `raw_infinity_five_jet_checks.json`.
