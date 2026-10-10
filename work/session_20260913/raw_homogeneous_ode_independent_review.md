> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Homogeneous raw HP equation: independent audit and exact cubic-degree gate

Date: 2026-09-13. Reviewer: audit_results. Source reviewed:
raw_hp_homogeneous_ode.md, Sections1--8, with the original raw high-jet
and endpoint determinant normalizations.

## Verdict and new result

The cofactor equation, degree bounds, infinity ledger, exceptional-case
scopes, apparent-root conditions, and conditional scaling argument pass.
No substantive gap was found. The opening general quadratic extension
applies to the cofactor construction; the numerical leading coefficients
and fixed finite points in the main text are for raw D=1+z^2.

Write a_j,b_j,c_j for the actual polynomial coefficients of A,B,C.
The new exact all-index formula is



$$
\boxed{[z^3]Q=b_n\Xi_n,\qquad
 \Xi_n=a_nc_{n-1}-a_{n-1}c_n+c_n^2.}                     \tag{1}
$$



Thus q=3 is equivalent to both b_n and Xi_n being nonzero. It does not
require a prior assertion deg C=n. The known endpoint valuations do
not establish these two nonvanishing statements. Section5 identifies
the exact original augmented integer minors that would settle them.

## 1. Cofactors, polynomial division, and degrees

The four-column Wronskian expansion gives
W012*y'''-W013*y''+W023*y'-W123*y=0, with the source's signs. Subtracting
U and F times C from the R column gives



$$
E_r=A^{(r)}+\sum_{j=1}^r\binom rj C^{(r-j)}F^{(j)}.
$$



Only one column is rational, so D^3 clears every cofactor through row3.
Its origin order is at least M-3>=3n-2. Since D(0)!=0, division by
z^(3n-2) in A1,A0 is legitimate. The derivative W013=W012' includes
the derivative of e^z, and gives exactly



$$
A_2/A_3=-1-(3n-1)/z+2D'/D-Q'/Q.
$$



For W023, the potentially leading algebraic factor A C''-A''C loses
its equal-degree term and has degree at most2n-3. The other factors
and the F-derivative terms have the corresponding same growth bound,
giving3n-3 before multiplication by D^3. W123 gives3n-4. Removing
the origin power yields deg A1<=5 and deg A0<=4. Lower polynomial
degrees or vanishing derivatives improve these inequalities; no
full-degree assumption is being used.

## 2. Infinity and its degree defects

Put H=A+C(F-F_infinity). In span(C,H), keep C as the Laurent basis
member with highest power c=deg C. If H has the same highest power,
subtract its leading multiple of C; otherwise keep H. The remaining
germ is nonzero because F is not rational, and has highest power d!=c.

For U~u z^b e^z the leading W012 term is



$$
(d-c)uvh\,e^z z^{b+c+d-1},
$$



with nonzero coefficient. Comparing with z^(3n-1)Q/D^2 proves
b+c+d=3n+q-4, including negative d. The three nonnegative defects
from n sum to4-q, and c,d are distinct. This verifies b>=n-3 and
all of the source's exceptional infinity degree types.

The other leading cofactor ratios are



$$
W023/W012=(c+d-1)/z+O(z^{-2}),\qquad
 W123/W012=cd/z^2+O(z^{-3}).
$$



The minus sign in A0 gives the source's -cd coefficient. If cd or
c+d-1 is zero, the degree drops and the displayed coefficient is zero,
as allowed in the note. Thus deg A1<=q+2 and deg A0<=q+1 for every q.

## 3. Fixed points, accessory roots, and scaling

When Q(0)Q(i)Q(-i)!=0, the residues of A2/A3 at those points are
-(3n-1),2,2. The other monic coefficients have only simple poles.
The resulting indicial polynomials give 0,1,3n+1 at0 and0,0,1 at
the logarithmic poles. The actual rank-one logarithmic monodromy is
consistent with them.

If Q has an origin zero, the orders l0<l1 of an echelon basis of
span(U,C) satisfy l1<=2n+1<M. The Wronskian order is M+l0+l1-3,
which proves the exact origin defect ledger without assuming l0=0
or l1=1. The source correctly does not reuse its generic indicial
formula when Q shares a fixed logarithmic pole.

At a simple accessory root a outside0,+i,-i, all solutions are analytic
and their Wronskian has order1. The echelon orders must be0,1,3.
For the normalized local equation
x*y'''+b(x)y''+c(x)y'+d(x)y=0 with b0=-1, its first equation gives
2y2=c0*y1+d0*y0. The next equation cancels y3 and leaves exactly the
two compatibility conditions(13) in the source. Later coefficients
of y_(j+2) equal(j+2)(j+1)(j-1), nonzero for j>=2. The analytic
regular-singular recurrence consequently supplies the convergent
solutions with free data y0,y1,y3.

Writing s(x)=A3(a+x)/x, the contributions from
s'(0)=A3''(a)/2 cancel in both compatibility equations. This verifies
the compact polynomial identities(14). Divisibility by all Q needs
the stated squarefree/coprimality hypotheses. For other Q, only the
simple factor outside the fixed points is covered. No repeated-root
or collided-root condition is silently inferred.

The parameter count is(q+1)+(q+3)+(q+2)-1=3q+5 after scaling.
Neither independence nor completeness of those constraints is asserted.

On a fixed-q subsequence, c,d=n+O(1), so the scaled leading coefficients
of Q,A1,A0 tend to1,2,-1. The other coefficient limits remain assumptions.
On a zero-free domain, locally uniform holomorphic convergence of
y'(n*zeta)/y(n*zeta), with Cauchy estimates and the factor1/n from a
z derivative, justifies the conditional characteristic cubic. The
source does not establish these domains, coefficient compactness,
or a connection constant, and keeps the collapsed finite poles separate.

Scaling the original triple by c multiplies all three-column cofactors,
Q, and every A_j by c^3; the jet matrix scales by c. The companion
matrix is unchanged. Its gauge and degree-shift determinant warning
therefore have the correct powers.

## 4. Exact leading coefficient of the cubic

At raw infinity,



$$
F-F_\infty=-z^{-1}+\tfrac13z^{-3}-\tfrac15z^{-5}+\cdots.
$$



Allowing zero top coefficients, this gives



$$
H=a_nz^n+(a_{n-1}-c_n)z^{n-1}+O(z^{n-2}),\qquad
 C=c_nz^n+c_{n-1}z^{n-1}+O(z^{n-2}).
$$



Therefore



$$
H'C-HC'=\Xi_nz^{2n-2}+O(z^{2n-3}),\qquad
 \Xi_n=\det\begin{pmatrix}
 a_n&a_{n-1}-c_n\\c_n&c_{n-1}
 \end{pmatrix}.
$$



The U'' term of W012 is U''(H'C-HC'). Terms containing U' or U
lose at least one further power of z. Since
U''=e^z(b_nz^n+O(z^(n-1))), multiplying by D^2 and dividing by
z^(3n-1) proves(1).

If c_n!=0, Xi_n!=0 says that the remaining Laurent branch after
canceling the top C multiple has degree n-1. If c_n=0, then
Xi_n=a_n c_(n-1); nonvanishing instead gives deg C=n-1 and degree n
for the other branch. Hence



$$
\boxed{q=3\quad\Longleftrightarrow\quad b_n\ne0
                     \ \hbox{and}\ \Xi_n\ne0,}
$$



without a separate assumption that A or C has full degree.

## 5. Exact original integer minors for the remaining gates

Let J_n be the integral (2n+1)-by-(2n+2) high-jet matrix including
its final row C(1)-4B(1), with columns b0,...,bn,c0,...,cn. Set



$$
\Delta(u)=\det\begin{pmatrix}J_n\\u\end{pmatrix},\qquad
 \Delta=\Delta(u_{B(1)})\ne0.
$$



For the integer coordinate rows define



$$
B^*=\Delta(u_{b_n}),\quad C^*=\Delta(u_{c_n}),\quad
 C^-=\Delta(u_{c_{n-1}}).
$$



For r=n,n-1, let u_(a_r) be the exact rational reconstruction row



$$
a_r=-\sum_{j=0}^n b_j/(r-j)!
                  -\sum_{j=0}^n c_j\tau_{r-j},
$$



with negative-index factorial terms zero and tau_s=(-1)^((s-1)/2)/s
for positive odd s, zero otherwise. Put



$$
A^*=\Delta(n!u_{a_n}),\qquad
 A^-=\Delta((n-1)!u_{a_{n-1}}).
$$



These appended rows are integral. In the actual B(1)=1 normalization,
the cofactor identity gives



$$
b_n=B^*/\Delta,\quad c_n=C^*/\Delta,\quad
 c_{n-1}=C^-/\Delta,\quad
 a_n=A^*/(n!\Delta),\quad
 a_{n-1}=A^-/((n-1)!\Delta).
$$



Define the integer



$$
\mathcal K_n=A^*C^- -nA^-C^*+n!(C^*)^2.
$$



The exact original-minor cubic-degree gate is



$$
\boxed{[z^3]Q=\frac{B^*\mathcal K_n}{n!\Delta^3},\qquad
 q=3\Longleftrightarrow B^*\mathcal K_n\ne0.}             \tag{2}
$$



The completed dyadic proofs append B(1) or n!A(1), not these leading
coefficient rows. A nonzero endpoint evaluation does not imply a
nonzero top coefficient. Their known valuations also do not compare
the three summands of K_n, so cannot exclude exact cancellation.

The immediate arithmetic targets are a separate nonvanishing/valuation
theorem for B^* and one for K_n. A unique least-valuation term in K_n
would suffice once the valuations of these five actual minors are
known. The old unique-term proofs have not been transferred to these
different appended rows in this continuation.

Before imposing the endpoint ratio, the high system has a two-dimensional
kernel and B(1),C(1) are coordinates on it by the existing rank proof.
With B(1)=1,C(1)=lambda, every polynomial coefficient is affine in
lambda. Thus the top B gate is affine and Xi_n is quadratic in that
ratio. Full rank for all rational ratios does not exclude an exceptional
zero of either polynomial at lambda=4.

## 6. Independently selected exact controls

check_raw_homogeneous_independent.py solves the original integral
high-jet system directly for the two predeclared degrees n=3,5, using
B(1)=1,C(1)=4. It does not import the author's checker or n=1,2,4
certificates.

It constructs every cofactor through row3; checks polynomial division,
direct annihilation of all three columns, global degree bounds, the
Laurent infinity ledger and both top coefficients, the origin ledger,
and the apparent-root congruences after verifying their hypotheses.
It also compares(1) with the separate original integer-minor formula(2).
All controls pass. Both have q=3 and infinity powers(n,n,n-1).

Results are in raw_homogeneous_independent_checks.json. They verify
normalization and the exact formulas, not q=3 in unbounded degree.
The all-index cubic-degree assertion, accessory asymptotics, and any
consequence for shrinking primitive forms remain unproved.
