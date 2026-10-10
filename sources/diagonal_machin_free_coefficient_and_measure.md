> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact-order subsequences for the diagonal Machin Hermite--Padé family

Checked: 2026-08-26 UTC

## Scope and result

Put



$$
G(z)=16\arctan(z/5)-4\arctan(z/239)=\sum_{r\geq0}g_rz^r .
\tag{1}
$$



For an integer $n\geq1$, consider polynomials



$$
\deg A,\deg B,\deg C\leq n,
\qquad C(1)=B(1),
\tag{2}
$$



such that



$$
R_n(z)=A(z)+B(z)e^z+C(z)G(z)=O(z^{3n+1}).
\tag{3}
$$



The all-degree rank theorem in
`sources/machin_bordered_rank_proof.md` shows that the rational solution
line is well defined and that every nonzero solution has
$B(1)=C(1)\ne0$.  The first coefficient not constrained in that theorem
is



$$
q_{3n+1,n}=[z^{3n+1}]\bigl(B(z)e^z+C(z)G(z)\bigr).
\tag{4}
$$



The new result proved here is the following infinite-subsequence statement.

**Theorem 1 (two exact-order residue classes).**  If $n\geq1$ and



$$
n\equiv0\text{ or }1\pmod4,
\tag{5}
$$



then every nonzero solution of (2)--(3) satisfies



$$
q_{3n+1,n}\ne0.
\tag{5a}
$$



Consequently the vanishing order of $R_n$ at zero is exactly
$3n+1$ on these two residue classes.

This theorem does **not** show that $R_n(1)\ne0$, that $R_n(1)\to0$,
or that the endpoint-primitive coefficient height is
$o(5^{2n})$.  In particular, it does not prove either algebraicity or
transcendence of $e+\pi$.  Section 6 records the remaining arithmetic
obstruction precisely.

## 1. The square determinant for the first free coefficient

Write



$$
\gamma_r=\frac{g_r}{4}=
\begin{cases}
0,&r\leq0\text{ or }r\text{ even},\\[2mm]
\displaystyle
(-1)^{(r-1)/2}\frac{4\,5^{-r}-239^{-r}}r,
&r>0\text{ odd}.
\end{cases}
\tag{6}
$$



The convention at nonpositive indices is harmless here, since all actual
coefficient indices below are nonnegative.  It makes the matrices
unambiguous.

On the endpoint hyperplane $C(1)=B(1)$, there are unique coordinates
$x\in\mathbb Q$ and polynomials
$\widetilde B,\widetilde C$ of degree less than $n$ such that



$$
B=x+(z-1)\widetilde B,
\qquad C=x+(z-1)\widetilde C.
\tag{7}
$$



Let



$$
\mathcal X'=\{n+1,n+2,\ldots,3n+1\}.
\tag{8}
$$



For $k\in\mathcal X'$, $0\leq j\leq n$, and $0\leq a<n$, define



$$
E_{k,j}=\frac1{(k-j)!},
\qquad
P_{k,a}=\frac{k-a-1}{(k-a)!},
\tag{9}
$$





$$
\Gamma_{k,j}=\gamma_{k-j},
\qquad
Q_{k,a}=\gamma_{k-a-1}-\gamma_{k-a}.
\tag{10}
$$



The $(2n+1)$-by-$(2n+1)$ matrix of the coefficient equations with
indices in $\mathcal X'$, in the coordinate order
$(x,\widetilde B,\widetilde C)$, is



$$
\mathcal T_n=\bigl(E_0+4\Gamma_0\mid P\mid4Q\bigr).
\tag{11}
$$



Indeed, $P_a=E_{a+1}-E_a$ and
$Q_a=\Gamma_{a+1}-\Gamma_a$.  Put



$$
D_E=\det(E\mid Q),
\qquad
D_G=\det(P\mid\Gamma).
\tag{12}
$$



The successive-difference column transformations have determinant one.
Moving $\Gamma_0$ past the $n$ columns of $P$ gives the exact
decomposition



$$
\boxed{
\det\mathcal T_n=4^n\bigl(D_E+4(-1)^nD_G\bigr).}
\tag{13}
$$



Thus it suffices to show that the two rational determinants on the right
cannot cancel.  Notice also that $\det\mathcal T_n\ne0$ is exactly the
assertion that the high coefficient equations together with the first free
coefficient equation have no nonzero solution on the endpoint hyperplane.
In view of the already-proved one-dimensionality of (2)--(3), this is
equivalent to (5a).

## 2. Valuation notation and imported kernel estimates

Write $\nu=v_2$, with $\nu(0)=+\infty$, and put



$$
\phi(k)=\nu(k!),
\qquad
A(q)=\sum_{j=0}^{q-1}\phi(j),
\tag{14}
$$





$$
g_2(q)=\frac{q(q-1)}2+A(q).
\tag{15}
$$



For $q\geq1$, put $z=q-1$ and define



$$
\beta(q)=\frac{z(z-1)}2+A(z)+
\begin{cases}
z,&z\text{ even},\\
z+1,&z\text{ odd}.
\end{cases}
\tag{16}
$$



We use the square and bordered Machin-kernel estimates proved in Sections
2--4 of `sources/machin_bordered_rank_proof.md`.  In the notation of that
proof, when $n=2R$, every $n$-row minor of $Q$ has valuation at
least



$$
L_Q=3g_2(R)+\beta(R+1).
\tag{17}
$$



For the consecutive row set of the first admissible parity orientation,
equality holds.  The other orientation has lower bound



$$
L_Q'=2g_2(R+1)+g_2(R-1)+\beta(R),
\tag{18}
$$



and the exact comparison is



$$
L_Q'-L_Q=
\begin{cases}
0,&R\text{ odd},\\
2+2\nu(R),&R\text{ even}.
\end{cases}
\tag{19}
$$



These estimates apply unchanged to row subsets of the enlarged interval
$\mathcal X'$, because the square and bordered lemmas in the cited proof
are stated for arbitrary distinct integer row points of the required
parities.  The equality assertions used below are checked separately from
the parity-block sizes and consecutiveness of the particular row sets; no
translation-invariance assumption is being added here.

We also use the elementary integral-Vandermonde bound



$$
\nu(V(S))\geq A(|S|)
\tag{20}
$$



for a set $S$ of distinct integers.  Equality holds for consecutive
integers.

## 3. The unique least term in $D_E$ when $n\equiv0\pmod4$

Assume from now on that



$$
n=4r,
\qquad R=n/2=2r.
\tag{21}
$$



Expand $D_E$ along its $n+1$ columns from $E$.  For an
$(n+1)$-element row set $S\subset\mathcal X'$, with complement
$U=\mathcal X'\setminus S$, its summand is, up to sign,



$$
\det E_S\det Q_U.
\tag{22}
$$



Since the falling factorials are monic,



$$
\det E_S=
\frac{V(S)}{\prod_{s\in S}s!}
\tag{23}
$$



up to the sign determined by the row order.  Therefore



$$
\nu(\det E_S)\geq
A(n+1)-\sum_{s\in S}\phi(s).
\tag{24}
$$



Because $\phi(k)$ is nondecreasing and its only consecutive ties occur
between $2m$ and $2m+1$, exactly two $(n+1)$-subsets maximize the
factorial sum in (24):



$$
S_0=\{2n+1,2n+2,\ldots,3n+1\},
\tag{25}
$$





$$
S_*=\{2n\}\cup\{2n+2,2n+3,\ldots,3n+1\}.
\tag{26}
$$



For $S_0$, the exponential rows are consecutive and



$$
U_0=\{n+1,n+2,\ldots,2n\}.
\tag{27}
$$



The two parity classes in $U_0$ are consecutive, and the equality case
of the Machin bordered estimate gives



$$
\nu(\det Q_{U_0})=L_Q.
\tag{28}
$$



Hence the $S_0$-summand has valuation



$$
v_0=A(n+1)-\sum_{k=2n+1}^{3n+1}\phi(k)
       +3g_2(R)+\beta(R+1).
\tag{29}
$$



For $S_*$, replacing the first point of the consecutive set by the
preceding integer multiplies the Vandermonde by $n+1$.  Since $n+1$
is odd,



$$
\nu(V(S_*))=\nu(V(S_0)).
\tag{30}
$$



However, its complementary row set replaces the final even row of
$U_0$ by the next odd row.  It therefore has the other admissible parity
orientation.  Since $R$ is even, (19) shows that its $Q$-minor costs
at least



$$
2+2\nu(R)>0
\tag{31}
$$



more than (28).  Every other $S$ has a strictly smaller factorial sum
than (25)--(26), while (20) and (17) remain valid; its summand therefore
has valuation at least $v_0+1$, or is zero.  Thus the $S_0$-summand is
the unique summand of least valuation.  It follows that



$$
\boxed{D_E\ne0,\qquad \nu(D_E)=v_0.}
\tag{32}
$$



## 4. The competing determinant $D_G$

Expand $D_G$ along its $n$ columns from $P$.  The exponential-minor
formula proved in `sources/raw_arctan_bordered_rank_proof.md` gives, for
every $n$-row set $S$,



$$
\nu(\det P_S)\geq
A(n)-\sum_{s\in S}\phi(s).
\tag{33}
$$



The maximum factorial sum for such an $S\subset\mathcal X'$ is attained
at



$$
S_G=\{2n+2,2n+3,\ldots,3n+1\}.
\tag{34}
$$



The complementary $(n+1)$-row $\Gamma$-minor is structurally zero
unless its odd and even row counts are $R+1$ and $R$, respectively.
When it is nonzero, parity splitting factors it into square Machin-kernel
determinants of sizes $R+1$ and $R$.  The square-kernel estimate and
(20) give



$$
\nu(\det\Gamma_U)\geq
2g_2(R+1)+2g_2(R).
\tag{35}
$$



Consequently



$$
\nu(D_G)\geq
A(n)-\sum_{k=2n+2}^{3n+1}\phi(k)
+2g_2(R+1)+2g_2(R).
\tag{36}
$$



Subtracting (29), and using that $R$ is even, gives



$$
\nu(D_G)-v_0\geq\eta_n,
\tag{37}
$$



where



$$
\boxed{
\eta_n=\phi(2n+1)-\phi(n)+R+2\phi(R)>0.}
\tag{38}
$$



For completeness, the only algebra needed here is



$$
2g_2(R+1)-g_2(R)-\beta(R+1)=R+2\phi(R)
\tag{39}
$$



for even $R$.  Equations (13), (32), and (37) now imply that the
$4D_G$ term has strictly larger valuation than $D_E$.  Hence it cannot
cancel the latter, and in fact



$$
\boxed{
\det\mathcal T_n\ne0,
\qquad
\nu(\det\mathcal T_n)=2n+v_0.}
\tag{40}
$$



This proves the $n\equiv0\pmod4$ part of Theorem 1.

## 5. The residue class $n\equiv1\pmod4$

The same determinant separation also works in one odd residue class.  Let



$$
n=4r+1,
\qquad R=(n+1)/2=2r+1.
\tag{40a}
$$



For an $n$-row minor of $Q$, the two pole parity sets both have size
$R$.  The general lower bound from the bordered-kernel proof is



$$
L_C=2g_2(R)+g_2(R-1)+\beta(R).
\tag{40b}
$$



In the $D_E$ expansion, retain the sets $S_0,S_*$ from (25)--(26).
The complement $U_0$ in (27) is consecutive.  Its parity split consists
of one square block of size $R$ and one bordered block with $R-1$
ordinary rows.  Since $R-1$ is even, the unconditional even-size
equality case in the bordered-kernel theorem applies.  Hence



$$
\nu(\det Q_{U_0})=L_C.
\tag{40c}
$$



The $S_0$-summand therefore has valuation



$$
v_1=A(n+1)-\sum_{k=2n+1}^{3n+1}\phi(k)
       +2g_2(R)+g_2(R-1)+\beta(R).
\tag{40d}
$$



The only other set with the same factorial sum is $S_*$.  Its
Vandermonde costs $\nu(n+1)=1$, while every $Q$-minor has valuation at
least $L_C$.  Every remaining set loses at least one in the factorial
sum.  Thus $S_0$ is again the unique least term and



$$
D_E\ne0,
\qquad \nu(D_E)=v_1.
\tag{40e}
$$



For $D_G$, a nonzero $(n+1)$-row $\Gamma$-minor now splits into two
square blocks of size $R$, so



$$
\nu(D_G)\geq
A(n)-\sum_{k=2n+2}^{3n+1}\phi(k)+4g_2(R).
\tag{40f}
$$



Subtracting (40d) gives



$$
\nu(D_G)-v_1\geq\eta_n^{(1)},
\tag{40g}
$$



where



$$
\eta_n^{(1)}=\phi(2n+1)-\phi(n)
 +(R-1)+2\phi(R-1)>0.
\tag{40h}
$$



Here the simplifying identity, valid for odd $R$, is



$$
2g_2(R)-g_2(R-1)-\beta(R)
=(R-1)+2\phi(R-1).
\tag{40i}
$$



Therefore the $4D_G$ term in (13) again has strictly larger valuation
than $D_E$, and



$$
\det\mathcal T_n\ne0,
\qquad
\nu(\det\mathcal T_n)=2n+v_1.
\tag{40j}
$$



This completes the proof of Theorem 1.

The exact script `scripts/machin_diagonal_free_coefficient.py` regenerates
$D_E,D_G,\mathcal T_n$ over $\mathbb Q$, checks (13), and checks
(29), (37), (40), and (40d)--(40j) at
$n=1,4,5,8,9,12,13,16$.  Its machine-readable output is
`results/machin_diagonal_free_coefficient.json`.  Those computations are
validation only; the proof above is all-degree in the two stated residue
classes.

## 6. What this leaves open for the diagonal family

Theorem 1 removes one analytic uncertainty on two infinite residue classes:
the Taylor remainder really begins at the predicted first free index.  It does
not control its value at $z=1$.  In particular, the signed one-term tail
estimate for $G$ cannot rule out cancellation among the adjacent
coefficient combinations in the exact endpoint identity.

The decisive unresolved arithmetic quantity remains the cofactor
$\Delta_A$, or equivalently the endpoint gcd $h_n$, in equations
(51)--(54) of `sources/machin_endpoint_asymptotics.md`.  A useful
constructive theorem would still have to prove, on some infinite
subsequence, both eventual nonvanishing of the endpoint form and the
effective height estimate



$$
H_C^*=o(5^{2n})
\tag{41}
$$



(together with the much easier factorial-scale exponential-tail condition),
or supply an alternative cancellation-sensitive endpoint estimate.  The
determinant in (40) contains no such gcd information.

## 7. Quantitative exponential-value measures for the nested Padé forms

This section tests a separate conditional construction against the strongest
directly applicable published measures.  Assume temporarily that



$$
s=e+\pi\in\overline{\mathbb Q},
\qquad d=[\mathbb Q(s):\mathbb Q].
\tag{42}
$$



Since $s$ is real,



$$
K=\mathbb Q(i,s),
\qquad h=[K:\mathbb Q]=2d.
\tag{43}
$$



For



$$
P_n(z)=\sum_{k=0}^n\frac{(2n-k)!}{k!(n-k)!}z^k,
\qquad Q_n(z)=P_n(-z),
\tag{44}
$$



the nested-exponential note proves



$$
\Lambda_n=-Q_n(ie)e^{is}-P_n(ie)\ne0
\tag{45}
$$



and the two-sided estimate



$$
\cos(e/2)\frac{e^{2n+1}n!}{(2n+1)!}
\leq|\Lambda_n|\leq
\frac{e^{2n+1}n!}{(2n+1)!}.
\tag{46}
$$



Define the **integer-coefficient** polynomial



$$
\widetilde F_n(X,Y)=-Q_n(X)Y-P_n(X).
\tag{47}
$$



Then $\widetilde F_n(ie,e^{is})=\Lambda_n$, and its exact total degree
and height are



$$
D_n=n+1,
\qquad
H_n=\frac{(2n)!}{n!}.
\tag{48}
$$



Using $ie$, rather than writing a Gaussian-integer polynomial in
$(e,e^{is})$, is important because the quantitative theorem below is
stated for polynomials with rational-integer coefficients.

The functions



$$
f_1(z)=ie^z,
\qquad f_2(z)=e^{isz}
\tag{49}
$$



are algebraically independent over $\overline{\mathbb Q}(z)$.  Indeed,
their monomials have exponential parts $e^{(m+nis)z}$, and the numbers
$m+nis$ are distinct for distinct pairs of nonnegative integers because
$1$ and $is$ are linearly independent over $\mathbb Q$.  The usual
linear independence of exponential functions with distinct exponents then
rules out a polynomial relation.  They satisfy the regular system



$$
Y'=\operatorname{diag}(1,is)Y
\tag{50}
$$



over $K$, so the hypotheses of the $E$-function case of
Adamczewski--Faverjon's Theorem A apply at $z=1$.

Adamczewski and Faverjon quote in their Section 6.1.1, equation (6.1), the
following state-of-the-art choices for the constants when there are $m$
algebraically independent $E$-functions:



$$
C_1(D)=\exp\!\left[-\exp\!\left(C_3D^{2m}\log(D+1)\right)\right],
\qquad
C_2=\sqrt m\,4^m h^{m+1},
\tag{51}
$$



where $C_3>0$ depends on the fixed functions and evaluation point.  With
$m=2$, (43), and (48), their inequality specializes to



$$
\boxed{
\begin{aligned}
\log|\Lambda_n|\geq{}&
-\exp\!\left(C_3(n+1)^4\log(n+2)\right)\\
&-128\sqrt2\,d^3(n+1)^2\log H_n.
\end{aligned}}
\tag{52}
$$



This is a genuine, uniform conditional lower bound for the fixed pair
$(ie,e^{is})$.  It is much too weak here.  Stirling's formula and (46)
give



$$
\log H_n=n\log n+(2\log2-1)n+O(\log n),
\tag{53}
$$





$$
-\log|\Lambda_n|
=n\log n-(3-2\log2)n+O(\log n),
\tag{54}
$$



and hence



$$
\frac{-\log|\Lambda_n|}{\log H_n}\longrightarrow1.
\tag{55}
$$



Even if the extremely small $C_1(D_n)$ in (52) were discarded, its
height term permits size $\exp(-\Theta_d(n^3\log n))$, whereas the actual
Padé form has size only $\exp(-\Theta(n\log n))$.  There is no
contradiction.

Fischler--Rivoal's Theorem 1 gives a second, linear-form comparison.  Expand
(45) into the values at $z=1$ of the $N_n=2n+2$ functions



$$
e^{kz}\ (0\leq k\leq n),
\qquad
e^{(k+is)z}\ (0\leq k\leq n).
\tag{56}
$$



The coefficients lie in $\mathbb Z[i]\subset\mathcal O_K$ and have
house at most $H_n$.  Their theorem therefore yields, for every fixed
$n$ and every $\varepsilon>0$,



$$
\boxed{
|\Lambda_n|>
c_{n,\varepsilon}
H_n^{-\,2d(2n+2)^{2d}+1-\varepsilon}.}
\tag{57}
$$



Here the dependence of the constant is essential:
$c_{n,\varepsilon}$ depends on the entire vector (56), whose dimension
and entries vary with $n$.  The theorem supplies no uniform lower bound
for these constants along this sequence.  Even if one optimistically
ignored that obstruction, the displayed height exponent grows like
$n^{2d}$, and is far too large compared with the limiting exponent one
in (55).

If $s\in\mathbb Q$, then all coefficients of (56) lie in the imaginary
quadratic field $\mathbb Q(i)$, and the classical imaginary-quadratic
version quoted by Fischler--Rivoal permits exponent
$N_n-1+\varepsilon=2n+1+\varepsilon$.  This still allows a logarithmic
size of order $-n^2\log n$, before the likewise nonuniform constant is
considered, so it also cannot contradict (54).

Finally, Fischler--Rivoal's 2025 one-variable transcendence measure for
$e^\alpha$ does not apply to (47).  It treats
$P(e^\alpha)$ for $P\in\mathbb Z[X]$; the present form involves the
two algebraically independent values $e$ and $e^{is}$.  Freezing either
variable leaves coefficients involving the other transcendental value, not
integer or algebraic coefficients.  The measure therefore cannot be
imported by treating (47) as a one-variable polynomial.

### Primary sources for Section 7

* B. Adamczewski and C. Faverjon, *Algebraic Independence Measures for
  Values of E-functions and M-functions*, arXiv:2502.09999v1 (2025),
  Theorem A and Section 6.1.1, equation (6.1):
  <https://arxiv.org/abs/2502.09999>.
* S. Fischler and T. Rivoal, *Values of E-functions are not Liouville
  numbers*, arXiv:2301.01158v3 (2023), Theorem 1:
  <https://arxiv.org/abs/2301.01158>.
* S. Fischler and T. Rivoal, *A new transcendence measure for the values of
  the exponential function at algebraic arguments*, arXiv:2502.17992v1
  (2025), Theorem 1:
  <https://arxiv.org/abs/2502.17992>.

No conjectural measure is used above.
