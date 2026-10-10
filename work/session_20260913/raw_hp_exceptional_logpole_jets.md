> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exceptional logarithmic poles: an unconditional bounded local reconstruction

Date: 2026-09-13. Root proposed the local Wronskian argument; this note
independently verifies it and supplies the precise recurrence and
principal-part construction. The result is an auxiliary local theorem
for the actual raw family, not an asymptotic or arithmetic conclusion.

## 1. Setting and statement

Use the actual fundamental solutions R=A+Be^z+C arctan z, U=Be^z, C
and their scalar equation from `raw_hp_homogeneous_ode.md`. At either
xi=i or -i put x=z-xi and h=ord_xi Q. The exact Wronskian has order



$$
\operatorname{ord}_{\xi}W(R,U,C)=h-2,
 \qquad0\le h\le3.
\tag{1}
$$



The following hold even when Q(xi)=0.

1. The scalar equation is regular singular at xi. Its three indicial
   roots, with multiplicities, are nonnegative integers whose sum is
   h+1<=4. Each root is therefore at most4.
2. The entire local solution space can be reconstructed from an ansatz
   a(x)+b(x)log x, retaining only coefficients through degree4. Its
   finite homogeneous system has dimension3, and all later coefficients
   follow uniquely by rational recurrences.
3. For a trial transfer S=(N0+N1*d/dz+N2*d²/dz²)/Q, all forbidden
   negative-power coefficients of S(a+b log) depend only on a,b through
   degree h+1<=4. Thus all logarithmic-pole tests are bounded rational
   linear conditions on the coefficients of N0,N1,N2.

For the actual rational raw Q, the stronger h<=1 holds. In that case
only degree2 Taylor/log coefficients are needed, and the exceptional
indicial types are exactly {0,0,2} or {0,1,1}. No all-degree genericity
assumption is required.

## 2. Echelon reduction and the leading Wronskian

The analytic functions U,C are independent. Choose an analytic echelon
basis f0,f1 of their constant span, with distinct vanishing orders
l0<l1. Every nonzero member of this two-plane has order either l0 or
l1: a combination with nonzero f0 coefficient has order l0, while
the remaining line has order l1. In particular



$$
c:=\operatorname{ord}_{\xi}C\in\{l_0,l_1\}.
\tag{2}
$$



Locally F=gamma*log x+f(x), with gamma=1/D'(xi)!=0 and f analytic.
Write R=H+gamma*C log x, with H analytic. Subtract constant multiples
of f0,f1 from H until its order d differs from both l0 and l1, or
H vanishes identically, in which case d=infinity. At most two leading
cancellations are needed: canceling the l0 term raises the order above
l0, and canceling a subsequent l1 term raises it above l1. Thus
d!=c, and this constant column operation changes no Wronskian.

If H is nonzero, the ordinary leading-power determinant gives



$$
\operatorname{ord}W(H,f_0,f_1)=d+l_0+l_1-3.
\tag{3}
$$



Its leading coefficient is nonzero because d,l0,l1 are distinct.
For the logarithmic term, express C as a linear combination of f0,f1.
The term belonging to its leading order c dominates, and the confluent
power determinant gives



$$
\operatorname{ord}W(C\log x,f_0,f_1)=c+l_0+l_1-3.
\tag{4}
$$



For completeness, (4) is obtained by differentiating in an exponent
the identity for W(x^r,x^(l0),x^(l1)), then setting r=c. The Vandermonde
has a simple zero at c, and its derivative there is nonzero because
l0!=l1. The possible log term multiplying W(C,f0,f1) is identically
zero. Higher analytic coefficients do not alter the first nonzero power.

Since d!=c, (3) and (4) have different leading powers and cannot
cancel. Define rho=(l0,l1,min(c,d)), interpreting min(c,infinity)=c.
Comparing with (1) proves



$$
\boxed{\rho_0+\rho_1+\rho_2=h+1\le4.}
\tag{5}
$$



This also proves that no high-order hidden zero of an analytic column
can invalidate the bounded local construction.

## 3. Regular singularity and the exact indicial roots

Consider any three-row cofactor with derivative indices I. In its R
column subtract gamma*log x times the C column, expressed in the
f0,f1 basis. At derivative row r the first column becomes



$$
H^{(r)}+\gamma\sum_{j=1}^r\binom rj
                 C^{(r-j)}(\log x)^{(j)}.
\tag{6}
$$



Its order is at least min(c,d)-r. The other columns have orders at
least l0-r and l1-r. Therefore every such cofactor has order at least
sum(rho)-sum(I). Dividing by W012, whose order is exactly sum(rho)-3,
shows that W013/W012, W023/W012, W123/W012 have poles of order at most
1,2,3. This is precisely the scalar regular-singular condition. It is
proved here from the actual solutions, not assumed from bounded degree.

Let I(t) be the monic cubic indicial polynomial. The analytic solutions
f0,f1 show I(l0)=I(l1)=0. If d<c, the leading term of R after echelon
reduction has order d, giving I(d)=0, and the three roots are distinct.
If c<d, the leading term is a nonzero multiple of x^c log x. Acting on
that term with the Euler indicial operator gives
x^c(I(c)log x+I'(c)). Since I(c)=0 and there is no lower analytic term
to cancel this coefficient, I'(c)=0. Thus c is a repeated root and
the multiset of roots is again exactly rho. This proves the first
statement of Section1, including multiplicities and all exceptional
cases.

## 4. A fixed finite Taylor/log system

Write the monic equation in Euler form, with theta=x*d/dx:



$$
x^3L_{\rm monic}=\sum_{j\ge0}x^j I_j(\theta),
 \qquad I_0=I.
\tag{7}
$$



Each I_j is a polynomial of degree at most3, and its coefficients are
Taylor coefficients of analytic rational functions. At xi these lie
in Q(i). Explicitly the analytic coefficients are
x*A2/A3, x²*A1/A3, x³*A0/A3, together with the leading theta term.

For y=a+b log x, a=sum a_kx^k and b=sum b_kx^k, the exact recurrences
at index k are



$$
I(k)b_k+\sum_{j=1}^kI_j(k-j)b_{k-j}=0,
\tag{8}
$$





$$
I(k)a_k+I'(k)b_k+
 \sum_{j=1}^k\bigl(I_j(k-j)a_{k-j}+I_j'(k-j)b_{k-j}\bigr)=0.
\tag{9}
$$



Impose (8),(9) only for k=0,...,4 on the ten unknown coefficients
a0,...,a4,b0,...,b4. Because all roots of I are at most4, I(k)!=0
for every k>=5. Equations (8),(9) then extend any solution of this
finite system uniquely: compute b_k first and a_k second.

These formal extensions converge. To see this directly, choose a small
disk where the Euler coefficients are analytic, so the coefficients
of I_j(t), as polynomials in t, are bounded by C*R^(-j). For large k,
|I(k)|>=c*k³. The recurrence coefficients after division by I(k) are
therefore bounded by C'*R^(-j), uniformly for 1<=j<=k; the derivative
polynomials have degree at most2 and satisfy the same bound. After
substituting the b recurrence into the a recurrence, the magnitudes
obey a fixed convolution bound. Choosing S large enough that
C''*sum_(j>=1)(RS)^(-j)<1 proves by induction a bound C'''*S^k.
Thus a,b are analytic in a nonzero disk.

Conversely, the three actual solutions belong to this Taylor/log
class. The truncation map is injective on local solutions because
zero coefficients through4 extend only to the zero solution. Every
finite-system solution extends to an actual local solution of the
order-three equation on a punctured disk. Hence the finite kernel
has dimension exactly3. A rational basis over Q(i) gives all complex
local solutions by complex linear combinations.

This argument does not infer dimension merely from counting ten
equations against ten unknowns; the exact extension and the known
fundamental system prove it.

## 5. Principal parts of a trial transfer use the same finite jets

Write Q=x^h q(x), q(0)!=0. For y=a+b log x, applying the numerator
operator gives a logarithmic coefficient



$$
g_b=N_0b+N_1b'+N_2b'',
$$



and a nonlogarithmic coefficient



$$
g_a=N_0a+N_1a'+N_2a''
       +N_1b/x+N_2(2b'/x-b/x^2).
\tag{10}
$$



Thus S y=(g_a/(x^h q))+(g_b/(x^h q))log x. The logarithmic coefficient
can have negative powers only down to -h, while the other coefficient
can have them only down to -h-2. Requiring all negative coefficients
to vanish is exactly the condition that S y have an analytic part
and an analytic logarithmic coefficient at xi.

To calculate these principal parts, g_a/q and g_b/q are needed only
through power h-1. Formula(10) shows that a,b are needed only through
degree h+1<=4. The Taylor series of q^(-1) and of the unknown N_j are
likewise needed only to bounded degree. Thus applying these tests to
the three finite local basis vectors yields a bounded rational linear
system in the transfer coefficients. No evaluation of full A_n,B_n,C_n
at xi is required.

For global polynomiality this is the correct test: on the actual R,
the new logarithmic coefficient is the fixed residue times S C. Once
that coefficient and the remaining part are analytic, subtracting
(S C)F leaves an analytic rational part. On the two analytic columns,
the same test removes all poles.

## 6. Sharper corollary for the rational raw cubic

For the raw family Q has rational coefficients. Since z²+1 is
irreducible over Q and deg Q<=3, its two roots occur with the same
multiplicity, so h<=1. If h=0, (5) forces the generic roots{0,0,1}.
If h=1, the sum is2 and l0<l1. A third distinct nonnegative integer
would already make the sum at least3. Therefore the only possibilities
are



$$
\boxed{\{0,0,2\}\quad\hbox{or}\quad\{0,1,1\}.}
\tag{11}
$$



In the first case the analytic-plane orders are0,2 and C has order0;
in the second they are0,1 and C has order1. The general ten-variable
construction consequently sharpens to the six coefficients a0,a1,a2,
b0,b1,b2, with recurrence indices0,1,2. All later indicial denominators
are nonzero. Since h+1<=2, these same jets already suffice for every
principal-part test in Section5. Conditions at the conjugate poles
can be written over Q by separating the two Q(i) components.

## 7. Scope for an unconditional degree update

This lemma removes the local-data obstruction when Q meets a fixed
logarithmic pole. It complements the ordinary apparent-pole analytic
jet construction and the separate high-origin Frobenius construction.
If Q(0)=0, a complete update must still remove possible poles of S on
the two low analytic origin solutions; raising the high remainder alone
does not impose those low-solution conditions. Their needed jets are
also bounded, because a principal part needs only degree h+1<=4.

No statement here proves bounds for the accessories or for iterated
endpoint products. The theorem supplies exact finite local conditions
for such a construction, including the exceptional logarithmic cases.

